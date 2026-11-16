"""Gera img/og-75lab.jpg (1200x630), a imagem de prévia de link do site.
Uso: python3 _build/og.py  (rodar na raiz do repositório)"""
from PIL import Image, ImageDraw, ImageFont
import os
F = os.path.expanduser('~/Library/Fonts/')
INK, LIME, PAPER = (5, 5, 5), (192, 238, 78), (242, 241, 233)
W, H = 1200, 630
og = Image.new('RGB', (W, H), INK)
# faixa do render (recorte sem a moldura de slide)
src = Image.open('img/g43-1.jpg').convert('RGB')
sw, sh = src.size
crop = src.crop((int(sw*.055), int(sh*.33), int(sw*.945), int(sh*.905)))
pw = 640
crop = crop.resize((pw, int(crop.height * pw / crop.width)))
panel = Image.new('RGB', (pw, H), crop.getpixel((5, 5)))
panel.paste(crop, (0, (H - crop.height)//2))
og.paste(panel, (W - pw, 0))
d = ImageDraw.Draw(og)
logo = Image.open('img/logo-wordmark-lime.png').convert('RGBA')
lw = 150; logo = logo.resize((lw, int(logo.height*lw/logo.width)))
og.paste(logo, (56, 56), logo)
big = ImageFont.truetype(F + 'BigShouldersDisplay-900.ttf', 80)
small = ImageFont.truetype(F + 'Lexend-Regular.ttf', 24)
mono = ImageFont.truetype(F + 'Lexend-Medium.ttf', 18)
y = 230
for line, col in (('PDV', PAPER), ('COMPROVADO.', LIME)):
    d.text((56, y), line, font=big, fill=col); y += 86
y += 18
for line in ('Display, ilha, enxoval e estande com', 'AR antes de produzir e rastreio depois.'):
    d.text((56, y), line, font=small, fill=PAPER); y += 34
d.text((56, H - 64), 'AGÊNCIA DE PDV E TRADE MARKETING · SÃO PAULO', font=mono, fill=(1, 162, 144))
og.save('img/og-75lab.jpg', quality=88)
print('ok img/og-75lab.jpg')
