"""Gera as 10 páginas livres display-para-<categoria>.html e o índice displays-por-categoria.html."""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from conteudo_cat import PAGINAS

SITE = 'https://75lab.com.br'
DEST = '/Volumes/hd caique becker/Mac Caique/Projetos/75lab-site/_build/conteudo/livres'


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    return re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>', s)


def limpo(s):
    return re.sub(r'\*\*|\]\([^)]*\)|\[', '', s)


def bloco(b, ind='      '):
    if 'p' in b:
        return f'{ind}<p>{inline(b["p"])}</p>'
    if 'lista' in b:
        return f'{ind}<ul>\n' + '\n'.join(f'{ind}  <li>{inline(x)}</li>' for x in b['lista']) + f'\n{ind}</ul>'
    if 'tabela' in b:
        t = b['tabela']
        cab = ''.join(f'<th>{inline(c)}</th>' for c in t['cab'])
        lin = '\n'.join(f'{ind}    <tr>' + ''.join(f'<td>{inline(c)}</td>' for c in l) + '</tr>' for l in t['linhas'])
        return (f'{ind}<div class="tabela"><table>\n{ind}  <thead><tr>{cab}</tr></thead>\n{ind}  <tbody>\n{lin}\n'
                f'{ind}  </tbody>\n{ind}</table></div>')
    raise ValueError(b)


def h1(s):
    return inline(s).replace('<strong>', '<em>').replace('</strong>', '</em>')


def pagina(p):
    url = f'{SITE}/{p["slug"]}.html'
    meta = {'slug': p['slug'], 'titulo': p['titulo'], 'descricao': p['descricao'], 'prioridade': '0.7',
            'migalhas': [['Soluções', '/solucoes.html'], [p['curto'], f'/{p["slug"]}.html']],
            'ld': [{'@type': 'FAQPage', '@id': url + '#faq', 'mainEntity': [
                {'@type': 'Question', 'name': limpo(f['q']), 'acceptedAnswer': {'@type': 'Answer', 'text': limpo(f['a'])}}
                for f in p['faq']]}]}
    secoes = []
    for s in p['secoes']:
        secoes.append(f'      <h2>{inline(s["h2"])}</h2>\n' + '\n'.join(bloco(b) for b in s['blocos']))
    faq = ('      <h2>Perguntas frequentes</h2>\n      <div class="faq">\n' + '\n'.join(
        f'        <details><summary>{inline(f["q"])}</summary><p>{inline(f["a"])}</p></details>' for f in p['faq'])
        + '\n      </div>')
    seg_t, seg_u = p['segmento']
    rel = [(seg_t, seg_u), ('Display de PDV', 'display-de-pdv.html'), ('Calculadora de display de PDV', 'calculadora-display-pdv.html')] \
        + p['guias'] + [('Display por categoria de produto', 'displays-por-categoria.html')]
    rel_html = ''.join(f'<a href="{u}">{html.escape(t)}</a>' for t, u in rel)
    corpo = f'''<section class="phero"><span class="glow g1"></span><span class="glow g2"></span>
  <div class="wrap inner">
    <div class="crumbs fx"><a href="index.html">Início</a> / <a href="solucoes.html">Soluções</a> / {html.escape(p['curto'])}</div>
    <span class="eyebrow fx" data-n="">Display por categoria</span>
    <h1 class="fx" data-fx="left">{h1(p['h1'])}</h1>
    <p class="fx">{inline(p['lead'])}</p>
  </div>
</section>
<section class="section--paper artigo">
  <div class="wrap art-grid">
    <div class="art-main">
      <p class="resumo">{inline(p['resumo'])}</p>

{chr(10).join(secoes)}

      <h2>Do projeto à loja</h2>
      <p>Na 75 LAB, o display para {html.escape(p['cat'])} parte do {inline(BRIEF_LINK)} com o peso real do produto, é aprovado em {inline(RA_LINK)} na gôndola antes de produzir e sai com QR para registrar a montagem. Veja o {inline(EXEC_LINK)} e a página de {inline(DISPLAY_LINK)}.</p>

{faq}
    </div>
    <aside class="art-aside">
      <div class="cta-card"><span class="k">Próximo passo</span><h3>Veja o display na gôndola antes de produzir</h3><p>Mandamos o seu display para {html.escape(p['cat'])} em realidade aumentada, em tamanho real, em até 48 horas úteis e sem custo.</p>
        <a class="btn btn--onink" href="realidade-aumentada-pdv.html">Quero ver em AR <span class="arr">→</span></a></div>
      <div class="rel"><span class="k">Veja também</span>{rel_html}</div>
    </aside>
  </div>
</section>'''
    return '<!--' + json.dumps(meta, ensure_ascii=False, separators=(',', ':')) + '-->\n' + corpo + '\n'


BRIEF_LINK = '[briefing](guia-briefing-display-pdv.html)'
RA_LINK = '[realidade aumentada](guia-realidade-aumentada-no-pdv.html)'
EXEC_LINK = '[checklist do executivo](guia-checklist-executivo-pdv.html)'
DISPLAY_LINK = '[display de PDV](display-de-pdv.html)'


def indice():
    slug = 'displays-por-categoria'
    url = f'{SITE}/{slug}.html'
    meta = {'slug': slug, 'titulo': 'Display de PDV por categoria de produto · 75 LAB',
            'descricao': 'Como expor cada categoria no PDV: chocolate, snacks, cerveja, vinhos, refrigerante e água, pet, cosméticos, higiene, MIP e suplementos, pilhas e acessórios.',
            'prioridade': '0.7',
            'migalhas': [['Soluções', '/solucoes.html'], ['Display por categoria', f'/{slug}.html']],
            'ld': [{'@type': 'ItemList', '@id': url + '#lista', 'name': 'Display de PDV por categoria de produto',
                    'itemListElement': [{'@type': 'ListItem', 'position': i, 'name': p['curto'], 'url': f'{SITE}/{p["slug"]}.html'}
                                        for i, p in enumerate(PAGINAS, start=1)]}]}
    cards = '\n'.join(
        f'      <a class="lcard" href="{p["slug"]}.html"><span class="k">{html.escape(p["k"])}</span><h3>{html.escape(p["curto"])}</h3>'
        f'<p>{html.escape(p["card"])}</p><span class="go">Ver a categoria →</span></a>' for p in PAGINAS)
    cards += ('\n      <a class="lcard" href="calculadora-display-pdv.html"><span class="k">Ferramenta grátis</span><h3>Calculadora de display de PDV</h3>'
              '<p>Qual material usar, se a prateleira aguenta o produto com a fluência do MDF e a carga do clip strip por gancho.</p>'
              '<span class="go">Usar a calculadora →</span></a>')
    corpo = f'''<section class="phero"><span class="glow g1"></span><span class="glow g2"></span>
  <div class="wrap inner">
    <div class="crumbs fx"><a href="index.html">Início</a> / <a href="solucoes.html">Soluções</a> / Display por categoria</div>
    <span class="eyebrow fx" data-n="">Display por categoria</span>
    <h1 class="fx" data-fx="left">Display de PDV por <em>categoria</em> de produto.</h1>
    <p class="fx">Cada categoria muda o display: o peso do produto, o canal, a sazonalidade, o calor, o furto e as regras da loja. Escolha a sua e veja que peças funcionam, que material usar e o que conferir antes de produzir.</p>
  </div>
</section>
<section class="section section--paper">
  <div class="wrap"><div class="lista-cards">
{cards}
  </div></div>
</section>'''
    return '<!--' + json.dumps(meta, ensure_ascii=False, separators=(',', ':')) + '-->\n' + corpo + '\n'


def palavras(h):
    t = h[h.index('<div class="art-main">'):h.index('</div>\n    <aside')]
    return len(re.sub(r'<[^>]+>', ' ', t).split())


if __name__ == '__main__':
    for p in PAGINAS:
        h = pagina(p)
        assert '—' not in h and '–' not in h, p['slug']
        open(os.path.join(DEST, p['slug'] + '.html'), 'w', encoding='utf-8').write(h)
        print(p['slug'], palavras(h), 'palavras')
    h = indice()
    assert '—' not in h and '–' not in h
    open(os.path.join(DEST, 'displays-por-categoria.html'), 'w', encoding='utf-8').write(h)
    print('displays-por-categoria ok')
