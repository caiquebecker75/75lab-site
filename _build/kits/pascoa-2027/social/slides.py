import subprocess, os
D=os.path.dirname(os.path.abspath(__file__))
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
LOGO="file://"+os.path.expanduser("~/75lab-site/img/logo-wordmark-lime.png")
css='''<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@900&family=Space+Grotesk:wght@400;500;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box}html,body{margin:0;width:1080px;height:1350px;overflow:hidden}
body{font-family:"Space Grotesk",sans-serif;background:#050505;color:#F2F1E9;padding:90px 84px;position:relative}
body.p{background:#F2F1E9;color:#050505} body.l{background:#C0EE4E;color:#050505}
.k{font-family:"Space Mono",monospace;font-size:26px;letter-spacing:.14em;text-transform:uppercase;color:#C0EE4E}
.p .k,.l .k{color:#050505;opacity:.75}
h1{font-family:"Big Shoulders Display",sans-serif;font-weight:900;text-transform:uppercase;font-size:200px;line-height:.86;margin:40px 0}
h2{font-family:"Big Shoulders Display",sans-serif;font-weight:900;text-transform:uppercase;font-size:104px;line-height:.9;margin:26px 0 44px}
em{font-style:normal;color:#C0EE4E} .p em{color:#050505;background:#C0EE4E;padding:4px 12px 0;display:inline-block;line-height:.95;margin-top:10px}
p{font-size:38px;line-height:1.3;margin:0 0 26px} .row{display:flex;gap:34px;border-top:2px solid currentColor;padding:24px 0;font-size:36px;line-height:1.25}
.row b{font-family:"Space Mono",monospace;min-width:230px;font-size:34px}
.foot{position:absolute;left:84px;right:84px;bottom:70px;display:flex;justify-content:space-between;align-items:center;font-family:"Space Mono",monospace;font-size:24px;letter-spacing:.1em;text-transform:uppercase}
.foot img{height:44px} .num{font-family:"Big Shoulders Display",sans-serif;font-weight:900;font-size:230px;line-height:.9}
</style>'''
foot=lambda n,cls='': f'<div class="foot"><img src="{LOGO if cls!="p" and cls!="l" else LOGO.replace("lime","black")}"><span>{n}/5 · 75lab.com.br</span></div>'
S=[
('', '<span class="k">Kit grátis para trade marketing</span><h1>Kit<br><em>Páscoa</em><br>2027.</h1><p>Páscoa em 28/03. Carnaval em 09/02.<br>A sua parreira precisa estar na loja antes dele.</p><p style="color:#C0EE4E">Arraste para o lado →</p>'),
('p', '<span class="k">1 · Cronograma reverso</span><h2>Da Páscoa<br><em>para trás.</em></h2><div class="row"><b>04/12</b>Briefing fechado, com o peso do ovo embalado</div><div class="row"><b>18/12</b>Projeto aprovado, visto em tamanho real na loja</div><div class="row"><b>15/01</b>Protótipo e teste com produto pendurado</div><div class="row"><b>12/02</b>Entregue no CD, antes do Carnaval</div><div class="row"><b>06/03</b>Montado em todas as lojas, com registro</div>'),
('', '<span class="k">2 · Conta de carga</span><h2>Quanto a parreira<br><em>carrega?</em></h2><p>Ovo de 350 g embalado × 6 por gancho × 10 ganchos × 4 barras, com 20% de folga:</p><div class="num" style="color:#C0EE4E">100,8 kg</div><p style="margin-top:30px">Exemplo ilustrativo. Faça a conta do seu projeto na calculadora do kit.</p>'),
('p', '<span class="k">3 · O que mais custa</span><h2>Os erros<br><em>da Páscoa.</em></h2><div class="row">Conta de carga com o peso líquido do chocolate</div><div class="row">Uma parreira só para lojas de todos os tamanhos</div><div class="row">Briefing em janeiro, entrega depois do Carnaval</div><div class="row">Gancho curto, sem trava</div><div class="row">Nenhuma prova de que a peça foi montada</div>'),
('l', '<span class="k">Kit Páscoa 2027 · PDF grátis</span><h2 style="font-size:120px">Baixe o kit<br>completo.</h2><p>Cronograma para preencher, briefing da parreira, conta de carga, checklist de montagem e os 8 erros que mais custam.</p><p style="font-weight:700">Link na bio<br>75lab.com.br/kit-pascoa-2027.html</p>'),
]
for i,(cls,body) in enumerate(S,1):
    h=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">{css}</head><body class="{cls}">{body}{foot(i,cls)}</body></html>'
    f=os.path.join(D,f's{i}.html'); open(f,'w',encoding='utf-8').write(h)
    subprocess.run([CH,'--headless=new','--disable-gpu','--hide-scrollbars','--window-size=1080,1350','--virtual-time-budget=6000',f'--screenshot={D}/kit-pascoa-{i}.png','file://'+f],capture_output=True)
    subprocess.run(['sips','-s','format','jpeg','-s','formatOptions','90',f'{D}/kit-pascoa-{i}.png','--out',f'{D}/kit-pascoa-{i}.jpg'],capture_output=True)
print('ok')
