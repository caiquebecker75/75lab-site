import subprocess, os
D=os.path.dirname(os.path.abspath(__file__)); CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
LG="file://"+os.path.expanduser("~/75lab-site/img/logo-wordmark-lime.png"); LGP=LG.replace('lime','black')
css='''<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@900&family=Space+Grotesk:wght@500;700&family=Space+Mono:wght@700&display=swap" rel="stylesheet"><style>
html,body{margin:0;width:1080px;height:1920px;overflow:hidden}body{background:#050505;color:#F2F1E9;font-family:"Space Grotesk";padding:260px 90px 0;box-sizing:border-box;position:relative}
body.l{background:#C0EE4E;color:#050505}.k{font-family:"Space Mono";font-size:30px;letter-spacing:.14em;text-transform:uppercase;color:#C0EE4E}.l .k{color:#050505}
h1{font-family:"Big Shoulders Display";font-weight:900;text-transform:uppercase;font-size:190px;line-height:.86;margin:40px 0}em{font-style:normal;color:#C0EE4E}
p{font-size:48px;line-height:1.3;margin:0 0 30px}.big{font-family:"Big Shoulders Display";font-weight:900;font-size:300px;line-height:.9;color:#C0EE4E}
.zona{position:absolute;left:90px;right:90px;bottom:430px;border:4px dashed currentColor;border-radius:30px;height:170px;display:flex;align-items:center;justify-content:center;font-family:"Space Mono";font-size:28px;opacity:.55;text-transform:uppercase;letter-spacing:.1em}
img{position:absolute;left:90px;bottom:170px;height:60px}</style>'''
S=[('', f'<span class="k">Páscoa 28/03 · Carnaval 09/02</span><h1 style="font-size:150px">Sua parreira<br>chega <em>antes</em><br>do Carnaval?</h1><p>O briefing precisa fechar até 4 de dezembro.</p><div class="zona">link aqui</div><img src="{LG}">'),
   ('', f'<span class="k">Conta de carga · exemplo</span><div class="big" style="margin-top:60px">100 kg</div><p style="margin-top:40px">é o que uma parreira cheia pode carregar. Fez a conta com o peso do ovo embalado?</p><div class="zona">link aqui</div><img src="{LG}">'),
   ('l', f'<span class="k">PDF grátis</span><h1>Kit<br>Páscoa<br>2027.</h1><p>Cronograma, briefing da parreira, conta de carga e checklist de montagem.</p><div class="zona">toque no link</div><img src="{LGP}">')]
for i,(c,b) in enumerate(S,1):
    f=f'{D}/story{i}.html'; open(f,'w').write(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">{css}</head><body class="{c}">{b}</body></html>')
    subprocess.run([CH,'--headless=new','--hide-scrollbars','--window-size=1080,1920','--virtual-time-budget=6000',f'--screenshot={D}/story-kit-{i}.png','file://'+f],capture_output=True)
    subprocess.run(['sips','-s','format','jpeg','-s','formatOptions','90',f'{D}/story-kit-{i}.png','--out',f'{D}/story-kit-{i}.jpg'],capture_output=True)
print('ok')
