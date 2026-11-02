import asyncio,sys
from playwright.async_api import async_playwright
S=sys.argv[1]; U=f'file://{S}/fonts/dot.html'; A=open(f'{S}/fonts/node_modules/axe-core/axe.min.js').read()
JS = r'''() => axe.run(document, {resultTypes: ['violations']}).then(r => r.violations.map(v => ({
  id: v.id, impact: v.impact, n: v.nodes.length, help: v.help,
  eg: v.nodes.slice(0, 4).map(n => n.target.join(' ') + ' | ' + (n.any.concat(n.all)[0] || {message: ''}).message)
})))'''
REVEAL = "() => document.querySelectorAll('.rise').forEach(e => e.classList.add('in'))"
async def run(pg, label):
    await pg.add_script_tag(content=A); await pg.evaluate(REVEAL)
    r = await pg.evaluate(JS); print('==', label, len(r), 'issue types')
    for v in r:
        print(v['impact'], v['id'], v['n'], v['help'])
        for e in v['eg']: print('   ', e[:220])
async def m():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); pg = await b.new_page(viewport={'width': 1440, 'height': 900})
        await pg.goto(U); await pg.wait_for_timeout(3500)
        await run(pg, 'home')
        await pg.evaluate("() => document.querySelector('#all-concerts').click()"); await pg.wait_for_timeout(1500); await run(pg, 'calendar')
        await pg.evaluate("() => document.querySelector('#cal-back').click()"); await pg.wait_for_timeout(1200)
        await pg.evaluate("() => document.querySelector('#full-bio').click()"); await pg.wait_for_timeout(1500); await run(pg, 'about')
        await b.close()
asyncio.run(m())
