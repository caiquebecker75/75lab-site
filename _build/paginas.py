"""Gera as páginas de conteúdo do site (serviços, cases, guias e o índice de guias) a partir de
_build/conteudo/*.py e _build/conteudo/guias/*.json, usando o cabeçalho e o rodapé de sobre.html.
Registra cada página em _build/paginas_extra.json; depois rode _build/seo.py.

Uso, na raiz do repositório:
  python3 _build/paginas.py && python3 _build/seo.py

Marcação aceita nos textos: [texto](url) vira link e **texto** vira negrito. Nunca use travessão.
"""
import glob, html, importlib.util, json, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = os.path.join(RAIZ, '_build')
SITE = 'https://75lab.com.br'
WHATS = 'https://wa.me/5511986765634'
HOJE = __import__('datetime').date.today().isoformat()


def carregar(nome):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(B, 'conteudo', nome + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    def link(m):
        t, u = m.group(1), m.group(2)
        ext = u.startswith('http') and '75lab.com.br' not in u.split('/')[2] if u.startswith('http') else False
        alvo = ' target="_blank" rel="noopener"' if ext else ''
        return f'<a href="{html.escape(u, quote=True)}"{alvo}>{t}</a>'
    return re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', link, s)


def bloco(b):
    if 'p' in b: return f'<p>{inline(b["p"])}</p>'
    if 'h3' in b: return f'<h3>{inline(b["h3"])}</h3>'
    if 'lista' in b: return '<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in b['lista']) + '</ul>'
    if 'passos' in b: return '<ol>' + ''.join(f'<li>{inline(x)}</li>' for x in b['passos']) + '</ol>'
    if 'tabela' in b:
        t = b['tabela']
        cab = ''.join(f'<th>{inline(c)}</th>' for c in t['cab'])
        lin = ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in l) + '</tr>' for l in t['linhas'])
        return f'<div class="tabela"><table><thead><tr>{cab}</tr></thead><tbody>{lin}</tbody></table></div>'
    if 'fichas' in b:
        return '<div class="fichas">' + ''.join(
            f'<div class="ficha"><b>{inline(v)}</b><span>{inline(k)}</span></div>' for v, k in b['fichas']) + '</div>'
    if 'galeria' in b:
        out = []
        for g in b['galeria']:
            fig = (f'<figure><img loading="lazy" src="{g["img"]}" alt="{html.escape(g["leg"], quote=True)}">'
                   f'<figcaption>{inline(g["leg"])}</figcaption></figure>')
            if g.get('href'):
                ext = g['href'].startswith('http')
                fig = f'<a href="{g["href"]}"' + (' target="_blank" rel="noopener"' if ext else '') + f'>{fig}</a>'
            out.append(fig)
        return '<div class="galeria">' + ''.join(out) + '</div>'
    if 'demo' in b:
        return '<div class="demo">' + ''.join(
            f'<a class="btn" href="{d["href"]}" target="_blank" rel="noopener">{inline(d["t"])} <span class="arr">→</span></a>'
            for d in b['demo']) + '</div>'
    raise ValueError(b)


UI = {
    'pt': {'inicio': 'Início', 'home': 'index.html', 'faq': 'Perguntas frequentes', 'rel': 'Veja também', 'whats': 'Chamar no WhatsApp',
           'cta': {'k': 'Fale com a 75 LAB', 'h': 'Tem um PDV para tirar do papel?', 'p': 'Conte o produto, o canal e o prazo. A gente responde com o caminho e o cronograma.'},
           'band_k': 'Tem uma intenção comercial?', 'band_h': 'vamos fazer <em>acontecer</em>', 'band_btn': 'Pedir orçamento', 'html': 'pt-BR', 'og': 'pt_BR'},
    'en': {'inicio': 'Home', 'home': 'en/', 'faq': 'Frequently asked questions', 'rel': 'See also', 'whats': 'Message us on WhatsApp',
           'cta': {'k': 'Talk to 75 LAB', 'h': 'Have a POS project to get off the ground?', 'p': 'Tell us the product, the channel and the deadline. We reply with the path and the timeline.'},
           'band_k': 'Have a commercial goal?', 'band_h': "let's make it <em>happen</em>", 'band_btn': 'Request a quote', 'html': 'en', 'og': 'en_US'},
    'es': {'inicio': 'Inicio', 'home': 'es/', 'faq': 'Preguntas frecuentes', 'rel': 'Ver también', 'whats': 'Escríbenos por WhatsApp',
           'cta': {'k': 'Habla con 75 LAB', 'h': '¿Tienes un PDV para hacer realidad?', 'p': 'Cuéntanos el producto, el canal y el plazo. Te respondemos con el camino y el cronograma.'},
           'band_k': '¿Tienes una intención comercial?', 'band_h': 'hagámoslo <em>realidad</em>', 'band_btn': 'Pedir presupuesto', 'html': 'es', 'og': 'es_ES'},
}
# páginas equivalentes entre idiomas (hreflang)
PARES = [
    {'pt': '/', 'en': '/en/', 'es': '/es/'},
    {'pt': '/display-de-pdv.html', 'en': '/en/pop-display.html', 'es': '/es/exhibidor-pdv.html'},
    {'pt': '/realidade-aumentada-pdv.html', 'en': '/en/augmented-reality-pos.html', 'es': '/es/realidad-aumentada-pdv.html'},
    {'pt': '/rastreamento-material-pdv.html', 'en': '/en/pos-material-tracking.html', 'es': '/es/rastreo-material-pdv.html'},
    {'pt': '/case-ngv-display-universal.html', 'en': '/en/case-ngv-universal-display.html', 'es': '/es/caso-ngv-exhibidor-universal.html'},
    {'pt': '/case-semp-split-hw.html', 'en': '/en/case-semp-split-hw.html', 'es': '/es/caso-semp-split-hw.html'},
]


def molde():
    h = open(os.path.join(RAIZ, 'sobre.html'), encoding='utf-8').read()
    topo = h[:h.index('</header>') + len('</header>')]
    rodape = h[h.index('<footer>'):]
    return topo, rodape


def pagina(p, tipo, lang='pt'):
    topo, rodape = molde()
    u = UI[lang]
    if lang != 'pt':
        topo = topo.replace('<html lang="pt-BR"', f'<html lang="{u["html"]}"', 1)
        topo = topo.replace('<head>', f'<head>\n<base href="/">\n<script>try{{localStorage.setItem("lang75","{lang}")}}catch(e){{}}</script>', 1)
    migalhas = p['migalhas']  # [(nome, caminho)]
    crumbs = f'<a href="{u["home"]}">{u["inicio"]}</a>' + (' / ' if migalhas else '') + ' / '.join(
        (f'<a href="{c.lstrip("/")}">{html.escape(n)}</a>' if c else html.escape(n)) for n, c in migalhas)
    secoes = []
    for s in p['secoes']:
        secoes.append(f'<h2>{inline(s["h2"])}</h2>' + ''.join(bloco(b) for b in s['blocos']))
    faq = ''
    if p.get('faq'):
        faq = f'<h2>{u["faq"]}</h2><div class="faq">' + ''.join(
            f'<details><summary>{inline(f["q"])}</summary><p>{inline(f["a"])}</p></details>' for f in p['faq']) + '</div>'
    rel = ''
    if p.get('relacionados'):
        rel = f'<div class="rel"><span class="k">{u["rel"]}</span>' + ''.join(
            f'<a href="{u}">{html.escape(t)}</a>' for t, u in p['relacionados']) + '</div>'
    cta = p.get('cta') or u['cta']
    meio = f'''
<section class="phero"><span class="glow g1"></span><span class="glow g2"></span>
  <div class="wrap inner">
    <div class="crumbs fx">{crumbs}</div>
    <span class="eyebrow fx" data-n="">{html.escape(p['eyebrow'])}</span>
    <h1 class="fx" data-fx="left">{inline(p['h1']).replace('<strong>','<em>').replace('</strong>','</em>')}</h1>
    <p class="fx">{inline(p['lead'])}</p>
  </div>
</section>
<section class="section--paper artigo">
  <div class="wrap art-grid">
    <article class="art-main">
      <p class="resumo">{inline(p['resumo'])}</p>
      {''.join(secoes)}
      {faq}
    </article>
    <aside class="art-aside">
      <div class="cta-card"><span class="k">{html.escape(cta['k'])}</span><h3>{html.escape(cta['h'])}</h3><p>{html.escape(cta['p'])}</p>
        <a class="btn btn--onink" href="{WHATS}" target="_blank" rel="noopener">{u['whats']} <span class="arr">→</span></a></div>
      {rel}
    </aside>
  </div>
</section>
<section class="cta-band">
  <div class="wrap">
    <span class="eyebrow plain fx">{u['band_k']}</span>
    <h2 class="fx" data-fx="scale">{u['band_h']}</h2>
    <a class="btn btn--lg fx" href="{WHATS if lang != 'pt' else 'contato.html'}" data-magnetic>{u['band_btn']} <span class="arr">→</span></a>
  </div>
</section>

'''
    destino = os.path.join(RAIZ, p['slug'] + '.html')
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    open(destino, 'w', encoding='utf-8').write(topo + meio + rodape)

    url = f'{SITE}/{p["slug"]}.html'
    ld = []
    if tipo == 'servico':
        ld.append({'@type': 'Service', '@id': url + '#servico', 'name': p['servico'], 'serviceType': p['servico'],
                   'description': p['descricao'], 'provider': {'@id': SITE + '/#org'},
                   'areaServed': {'@type': 'Country', 'name': 'Brasil'}, 'url': url})
    elif tipo == 'case':
        ld.append({'@type': 'CreativeWork', '@id': url + '#case', 'name': p['h1'].replace('**', ''),
                   'description': p['descricao'], 'creator': {'@id': SITE + '/#org'},
                   'about': {'@type': 'Organization', 'name': p['cliente']}, 'image': SITE + p['imagem'],
                   'url': url, 'inLanguage': u['html']})
    elif tipo == 'guia':
        ld.append({'@type': 'Article', '@id': url + '#artigo', 'headline': p['h1'], 'description': p['descricao'],
                   'author': {'@id': SITE + '/#org'}, 'publisher': {'@id': SITE + '/#org'},
                   'datePublished': p.get('data', HOJE), 'dateModified': HOJE, 'inLanguage': u['html'],
                   'mainEntityOfPage': url, 'image': SITE + p.get('imagem', '/img/og-75lab.jpg'),
                   'keywords': ', '.join(p.get('palavras_chave', []))})
    if p.get('faq'):
        ld.append({'@type': 'FAQPage', '@id': url + '#faq', 'mainEntity': [
            {'@type': 'Question', 'name': re.sub(r'\*\*|\[|\]\([^)]*\)', '', f['q']),
             'acceptedAnswer': {'@type': 'Answer', 'text': re.sub(r'\*\*|\]\([^)]*\)|\[', '', f['a'])}}
            for f in p['faq']]})
    return {'titulo': p['titulo_seo'], 'descricao': p['descricao'], 'prioridade': p.get('prioridade', '0.8'), 'lang': lang,
            'imagem': p.get('imagem_og'), 'tipo': 'article' if tipo in ('case', 'guia') else 'website',
            'ld': ld, 'migalhas': [(n, c or '/' + p['slug'] + '.html') for n, c in migalhas]}


def paginas_traduzidas(extra):
    for lang in ('en', 'es'):
        arq = os.path.join(B, 'conteudo', 'i18n', f'paginas_{lang}.py')
        if not os.path.exists(arq):
            continue
        spec = importlib.util.spec_from_file_location('t' + lang, arq)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        home = dict(m.HOME, slug=f'{lang}/index', migalhas=[], faq=[], relacionados=[])
        extra[f'{lang}/index.html'] = pagina(home, 'home', lang)
        for p in m.PAGINAS:
            tipo = 'case' if 'cliente' in p else 'servico'
            extra[p['slug'] + '.html'] = pagina(p, tipo, lang)
    json.dump(PARES, open(os.path.join(B, 'hreflang.json'), 'w', encoding='utf-8'), indent=1)


def guia_de_json(g):
    secoes = []
    for s in g['secoes']:
        blocos = []
        for b in s['blocos']:
            if 'tabela' in b: blocos.append({'tabela': {'cab': b['tabela']['cab'], 'linhas': b['tabela']['linhas']}})
            else: blocos.append(b)
        secoes.append({'h2': s['h2'], 'blocos': blocos})
    return {'slug': g['slug'], 'titulo_seo': g['titulo_seo'], 'descricao': g['descricao'], 'eyebrow': 'Guia',
            'h1': g['titulo'], 'lead': g['descricao'], 'resumo': g['resumo'], 'secoes': secoes,
            'faq': g.get('faq', []), 'palavras_chave': g.get('palavras_chave', []),
            'migalhas': [('Guias', '/guias.html'), (g['titulo'].split(':')[0], None)],
            'relacionados': [('Kit Páscoa 2027 (PDF grátis)', 'kit-pascoa-2027.html'), ('Calculadora de display de PDV', 'calculadora-display-pdv.html'), ('Display de PDV', 'display-de-pdv.html'), ('Realidade aumentada para PDV', 'realidade-aumentada-pdv.html'),
                             ('Todos os guias', 'guias.html')],
            'prioridade': '0.7', 'data': g.get('data', HOJE)}


def indice_guias(guias):
    topo, rodape = molde()
    cards = ('<a class="lcard" href="kit-pascoa-2027.html"><span class="k">Kit grátis · Páscoa 2027</span><h3>Kit Páscoa 2027 para trade marketing</h3>'
             '<p>Cronograma reverso até 28/03, briefing da parreira, calculadora de carga e checklist de montagem. PDF para baixar.</p><span class="go">Baixar o kit →</span></a>'
             '<a class="lcard" href="calculadora-display-pdv.html"><span class="k">Ferramenta grátis</span><h3>Calculadora de display de PDV</h3>'
             '<p>Qual material usar, se a prateleira aguenta o produto com a fluência do MDF e a carga do clip strip por gancho.</p><span class="go">Usar a calculadora →</span></a>'
             '<a class="lcard" href="glossario-trade-marketing.html"><span class="k">Glossário</span><h3>Glossário de trade marketing e PDV</h3>'
             '<p>Ponta de gôndola, planograma, enxoval, ruptura, sell-out e mais 60 termos explicados em duas frases.</p><span class="go">Abrir o glossário →</span></a>'
             '<a class="lcard" href="displays-por-categoria.html"><span class="k">Por categoria</span><h3>Display de PDV por categoria de produto</h3>'
             '<p>Chocolate, cerveja, ração, cosméticos, MIP, pilhas e mais: que peça usar, material e cuidado de carga em cada categoria.</p><span class="go">Ver categorias →</span></a>') + ''.join(
        f'<a class="lcard" href="{g["slug"]}.html"><span class="k">Guia</span><h3>{html.escape(g["titulo"])}</h3>'
        f'<p>{html.escape(g["resumo"][:180].rsplit(" ", 1)[0])}...</p><span class="go">Ler guia →</span></a>' for g in guias)
    meio = f'''
<section class="phero"><span class="glow g1"></span><span class="glow g2"></span>
  <div class="wrap inner">
    <div class="crumbs fx"><a href="index.html">Início</a> / Guias</div>
    <span class="eyebrow fx" data-n="">Guias</span>
    <h1 class="fx" data-fx="left">Guias práticos de <em>PDV</em>.</h1>
    <p class="fx">O que a 75 LAB aprendeu projetando e produzindo PDV para a indústria, escrito para quem toca trade marketing no dia a dia.</p>
  </div>
</section>
<section class="section section--paper">
  <div class="wrap"><div class="lista-cards">{cards}</div></div>
</section>
'''
    open(os.path.join(RAIZ, 'guias.html'), 'w', encoding='utf-8').write(topo + meio + rodape)
    return {'titulo': 'Guias práticos de PDV e trade marketing · 75 LAB',
            'descricao': 'Guias da 75 LAB sobre display de PDV, materiais, estabilidade, executivo técnico, realidade aumentada e rastreamento de material de PDV.',
            'prioridade': '0.8', 'migalhas': [('Guias', '/guias.html')], 'ld': []}


def main():
    extra = {}
    serv = carregar('servicos')
    for p in serv.PAGINAS:
        extra[p['slug'] + '.html'] = pagina(p, 'servico')
    for p in carregar('segmentos').PAGINAS:
        extra[p['slug'] + '.html'] = pagina(p, 'servico')
    cases = carregar('cases')
    for p in cases.PAGINAS:
        extra[p['slug'] + '.html'] = pagina(p, 'case')
    guias = [json.load(open(f, encoding='utf-8')) for f in sorted(glob.glob(os.path.join(B, 'conteudo', 'guias', '*.json')))]
    for g in guias:
        extra[g['slug'] + '.html'] = pagina(guia_de_json(g), 'guia')
    extra['guias.html'] = indice_guias(guias)
    paginas_traduzidas(extra)
    # páginas livres: _build/conteudo/livres/*.html, 1ª linha = <!--{json com slug, titulo, descricao, prioridade, migalhas}-->
    topo, rodape = molde()
    for arq in sorted(glob.glob(os.path.join(B, 'conteudo', 'livres', '*.html'))):
        t = open(arq, encoding='utf-8').read()
        meta = json.loads(t[t.index('<!--') + 4:t.index('-->')])
        corpo = t[t.index('-->') + 3:]
        open(os.path.join(RAIZ, meta['slug'] + '.html'), 'w', encoding='utf-8').write(topo + '\n' + corpo + '\n' + rodape)
        extra[meta['slug'] + '.html'] = {'titulo': meta['titulo'], 'descricao': meta['descricao'],
                                         'prioridade': meta.get('prioridade', '0.6'), 'migalhas': meta.get('migalhas', []), 'ld': meta.get('ld', [])}
    # trava de qualidade: nada de travessão nas páginas geradas
    for arq in extra:
        t = open(os.path.join(RAIZ, arq), encoding='utf-8').read()
        corpo = t[t.index('<section class="phero"'):t.index('<footer>')]
        if '—' in corpo or '–' in corpo:
            sys.exit(f'travessão em {arq}: corrija o conteúdo')
    json.dump(extra, open(os.path.join(B, 'paginas_extra.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'ok: {len(extra)} páginas geradas')


if __name__ == '__main__':
    main()
