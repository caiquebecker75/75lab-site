"""Gera a página livre do glossário a partir de termos.py. Rodar antes de paginas.py e seo.py:
python3 _build/conteudo/glossario/gerar.py && python3 _build/paginas.py && python3 _build/seo.py"""
import html, json, os, re, sys, unicodedata
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from termos import T  # noqa: E402
SITE = 'https://75lab.com.br'
SLUG = 'glossario-trade-marketing'

def chave(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()

def ancora(s):
    return re.sub(r'[^a-z0-9]+', '-', chave(s)).strip('-')

termos = sorted(T, key=lambda x: chave(x[0]))
letras = []
for t in termos:
    l = chave(t[0])[0].upper()
    if l not in letras:
        letras.append(l)
ld = [{'@type': 'DefinedTermSet', '@id': f'{SITE}/{SLUG}.html#glossario', 'name': 'Glossário de trade marketing e PDV',
       'url': f'{SITE}/{SLUG}.html', 'inLanguage': 'pt-BR', 'publisher': {'@id': SITE + '/#org'},
       'hasDefinedTerm': [{'@type': 'DefinedTerm', 'name': n, 'description': d, 'url': f'{SITE}/{SLUG}.html#{ancora(n)}',
                           'inDefinedTermSet': {'@id': f'{SITE}/{SLUG}.html#glossario'}} for n, d, _ in termos]}]
meta = {'slug': SLUG, 'titulo': 'Glossário de trade marketing e PDV: 65 termos explicados · 75 LAB',
        'descricao': 'O que é ponta de gôndola, planograma, enxoval de PDV, clip strip, ruptura, sell-out, wobbler e mais 58 termos de trade marketing e ponto de venda, em linguagem direta.',
        'prioridade': '0.8', 'migalhas': [['Guias', '/guias.html'], ['Glossário', f'/{SLUG}.html']], 'ld': ld}
blocos, atual = [], None
for n, d, link in termos:
    l = chave(n)[0].upper()
    if l != atual:
        if atual:
            blocos.append('</dl>')
        blocos.append(f'<h2 id="letra-{l.lower()}">{l}</h2><dl class="glos">')
        atual = l
    mais = f' <a href="{link}">Saiba mais →</a>' if link else ''
    blocos.append(f'<dt id="{ancora(n)}"><dfn>{html.escape(n)}</dfn></dt><dd>{html.escape(d)}{mais}</dd>')
blocos.append('</dl>')
nav = ' '.join(f'<a href="{SLUG}.html#letra-{l.lower()}">{l}</a>' for l in letras)
corpo = f'''<!--{json.dumps(meta, ensure_ascii=False)}-->
<section class="phero"><span class="glow g1"></span><span class="glow g2"></span>
  <div class="wrap inner">
    <div class="crumbs fx"><a href="index.html">Início</a> / <a href="guias.html">Guias</a> / Glossário</div>
    <span class="eyebrow fx" data-n="">Glossário</span>
    <h1 class="fx" data-fx="left">Glossário de <em>trade</em> e PDV.</h1>
    <p class="fx">{len(termos)} termos que aparecem todo dia em quem toca trade marketing e ponto de venda, explicados em duas frases e ligados aos guias completos.</p>
  </div>
</section>
<style>
  .glos{{margin:0 0 30px}} .glos dt{{font-weight:700;font-size:18px;margin-top:18px;scroll-margin-top:90px}} .glos dfn{{font-style:normal}}
  .glos dd{{margin:4px 0 0;font-size:16px;line-height:1.55}} .glos dd a{{white-space:nowrap}}
  .letras{{font-family:var(--mono);font-size:14px;letter-spacing:.06em;display:flex;flex-wrap:wrap;gap:6px 12px;margin:0 0 30px}}
  .art-main h2[id^=letra]{{border-top:2px solid var(--ink);padding-top:18px;scroll-margin-top:80px}}
</style>
<section class="section--paper artigo">
  <div class="wrap art-grid">
    <div class="art-main">
      <p class="resumo">Trade marketing é a área que faz a ponte entre a indústria e o varejo para o produto vender na loja. Este glossário reúne os termos que mais aparecem nesse trabalho, do briefing do display à prova de execução, escritos pela 75 LAB a partir do dia a dia de projeto e produção de PDV.</p>
      <nav class="letras" aria-label="Letras">{nav}</nav>
      {chr(10).join(blocos)}
      <p>Faltou algum termo? Escreva para contato@75lab.com.br que a gente inclui.</p>
    </div>
    <aside class="art-aside">
      <div class="cta-card"><span class="k">Ferramenta grátis</span><h3>Calculadora de display de PDV</h3><p>Material indicado, carga e flecha da prateleira e carga do clip strip, em segundos.</p>
        <a class="btn btn--onink" href="calculadora-display-pdv.html">Usar a calculadora <span class="arr">→</span></a></div>
      <div class="rel"><span class="k">Veja também</span><a href="guias.html">Guias práticos de PDV</a><a href="display-de-pdv.html">Display de PDV</a><a href="raio-x-pdv.html">Pesquisa Raio-X do PDV</a></div>
    </aside>
  </div>
</section>
'''
assert '—' not in corpo and '–' not in corpo
open(os.path.join(AQUI, '..', 'livres', SLUG + '.html'), 'w', encoding='utf-8').write(corpo)
print('ok', len(termos), 'termos')
