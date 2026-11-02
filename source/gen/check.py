"""Check the built site before publishing: python3 source/gen/check.py
Builds nothing itself; run `NOPUSH=1 source/gen/deploy.sh x` first to write public/index.html.
Checks: accessibility (axe-core) on home, calendar and About; missing images/audio/fonts; JS errors; em-dashes in visible text."""
import asyncio, http.server, os, socketserver, subprocess, sys, threading
from playwright.async_api import async_playwright
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PUB = os.path.join(ROOT, 'public')
AXE = os.path.join(os.path.expanduser('~'), '.cache', 'axe', 'node_modules', 'axe-core', 'axe.min.js')
if not os.path.exists(AXE):
    os.makedirs(os.path.dirname(os.path.dirname(os.path.dirname(AXE))), exist_ok=True)
    subprocess.run(['npm', 'install', '--silent', '--prefix', os.path.dirname(os.path.dirname(os.path.dirname(AXE))), 'axe-core@4.10.2'], check=True)
A = open(AXE).read()
class Q(http.server.SimpleHTTPRequestHandler):
    def __init__(s, *a, **k): super().__init__(*a, directory=PUB, **k)
    def log_message(s, *a): pass
srv = socketserver.TCPServer(('127.0.0.1', 0), Q); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
JS = "() => axe.run(document,{resultTypes:['violations']}).then(r=>r.violations.map(v=>v.impact+' '+v.id+' x'+v.nodes.length+': '+v.help+' | e.g. '+v.nodes[0].target.join(' ')+' '+(v.nodes[0].any[0]||{message:''}).message))"
async def axe(pg, label):
    await pg.add_script_tag(content=A); await pg.evaluate("() => document.querySelectorAll('.rise').forEach(e => e.classList.add('in'))")
    r = await pg.evaluate(JS); print('==', label, len(r), 'accessibility issue types'); [print('  ', x) for x in r]
    return len(r)
async def main():
    bad = 0
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); pg = await b.new_page(viewport={'width': 1440, 'height': 900})
        fails, errs = [], []
        pg.on('response', lambda r: fails.append(f'{r.status} {r.url}') if r.status >= 400 else None)
        pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto(f'http://127.0.0.1:{port}/'); await pg.wait_for_timeout(3000)
        for y in range(0, 40000, 800): await pg.evaluate(f'scrollTo(0,{y})'); await pg.wait_for_timeout(40)
        bad += await axe(pg, 'home')
        await pg.evaluate("() => document.querySelector('#all-concerts').click()"); await pg.wait_for_timeout(3500); bad += await axe(pg, 'calendar')
        await pg.evaluate("() => document.querySelector('#cal-back').click()"); await pg.wait_for_timeout(1200)
        await pg.evaluate("() => document.querySelector('#full-bio').click()"); await pg.wait_for_timeout(1500)
        for y in range(0, 30000, 800): await pg.evaluate(f'scrollTo(0,{y})'); await pg.wait_for_timeout(40)
        bad += await axe(pg, 'about')
        broken = await pg.evaluate("[...document.images].filter(i=>i.complete&&i.naturalWidth==0&&i.src).map(i=>i.src)")
        for t in await pg.evaluate("[...new Set([...document.querySelectorAll('[data-src],audio')].map(x=>x.src||x.dataset.src))]"): pass
        await b.close()
    html = open(os.path.join(PUB, 'index.html'), encoding='utf-8').read()
    dash = html.count('—')
    for src in __import__('re').findall(r"src: '(audio/[^']+)'", html):
        if not os.path.exists(os.path.join(PUB, src)): fails.append('missing ' + src)
    print('== failed requests:', fails or 'none'); print('== broken images:', broken or 'none'); print('== script errors:', errs or 'none'); print('== em-dashes:', dash)
    bad += len(fails) + len(broken) + len(errs) + dash
    print('ALL CLEAR' if not bad else 'PROBLEMS FOUND'); sys.exit(1 if bad else 0)
asyncio.run(main())
