"""SEO da 75 LAB: aplica título, descrição, canonical, prévia de link (Open Graph) e dados
estruturados (schema.org) em todas as páginas listadas em PAGINAS, e gera sitemap.xml.

Uso, na raiz do repositório:  python3 _build/seo.py
É idempotente: o bloco gerado fica entre <!-- seo:inicio --> e <!-- seo:fim -->.
Página nova = acrescentar uma entrada em PAGINAS (ou em _build/paginas_extra.json) e rodar de novo.
"""
import html, json, os, re, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://75lab.com.br'
OG_PADRAO = SITE + '/img/og-75lab.jpg'
HOJE = datetime.date.today().isoformat()

# ---------- folha de fatos oficial (a mesma em todo lugar) ----------
FATOS = {
    'nome': '75 LAB',
    'razao': '75 LAB ESTRATÉGIA, DESIGN E PRODUÇÃO LTDA',
    'cnpj': '55.470.982/0001-77',
    'fundacao': '2024',
    'email': 'contato@75lab.com.br',
    'telefone': '+55-11-98676-5634',
    'descricao': ('Agência de PDV e trade marketing em São Paulo. Cria, projeta e produz displays, '
                  'ilhas, pontas de gôndola, enxovais de PDV e estandes para a indústria, com teste em '
                  'realidade aumentada antes de produzir e rastreamento do material depois de instalado.'),
    'endereco': {
        '@type': 'PostalAddress',
        'streetAddress': 'Av. das Nações Unidas, 12.901, Torre Norte (CENU)',
        'addressLocality': 'São Paulo', 'addressRegion': 'SP',
        'postalCode': '04578-910', 'addressCountry': 'BR'},
    'redes': ['https://www.instagram.com/setecincolab/', 'https://www.linkedin.com/company/75lab'],
}

ORG = {
    '@type': ['Organization', 'ProfessionalService'],
    '@id': SITE + '/#org',
    'name': FATOS['nome'],
    'legalName': FATOS['razao'],
    'alternateName': ['75LAB', 'Sete Cinco Lab'],
    'url': SITE + '/',
    'logo': SITE + '/img/logo-wordmark-black.png',
    'image': OG_PADRAO,
    'description': FATOS['descricao'],
    'slogan': 'Ideia boa é a que acontece',
    'foundingDate': FATOS['fundacao'],
    'taxID': FATOS['cnpj'],
    'email': FATOS['email'],
    'telephone': FATOS['telefone'],
    'address': FATOS['endereco'],
    'areaServed': {'@type': 'Country', 'name': 'Brasil'},
    'founder': [
        {'@type': 'Person', 'name': 'Caique Becker', 'jobTitle': 'Cofundador e Head de Trade',
         'sameAs': ['https://www.linkedin.com/in/caiquebecker/']},
        {'@type': 'Person', 'name': 'Daniel Coimbra', 'jobTitle': 'Cofundador e CEO'},
    ],
    'sameAs': FATOS['redes'],
    'knowsAbout': ['trade marketing', 'material de ponto de venda', 'display de PDV',
                   'ponta de gôndola', 'ilha promocional', 'enxoval de PDV', 'estande',
                   'realidade aumentada no PDV', 'rastreamento de material de PDV',
                   'conteúdo rico para e-commerce'],
}
SITE_LD = {'@type': 'WebSite', '@id': SITE + '/#site', 'url': SITE + '/', 'name': '75 LAB',
           'inLanguage': 'pt-BR', 'publisher': {'@id': SITE + '/#org'}}

# ---------- páginas ----------
# arquivo: (caminho canônico, título, descrição, prioridade no sitemap)
PAGINAS = {
    'index.html': ('/', '75 LAB · Agência de PDV e trade marketing em São Paulo',
                   'Displays, ilhas, pontas de gôndola, enxovais e estandes com engenharia, teste em realidade '
                   'aumentada antes de produzir e rastreio depois de instalado. PDV comprovado para indústria e varejo.',
                   '1.0'),
    'solucoes.html': ('/solucoes.html', 'Soluções de PDV e trade marketing · 75 LAB',
                      'Display de PDV, ilha e ponta de gôndola, enxoval, estande, realidade aumentada, rastreamento '
                      'de material de PDV, conteúdo rico, promoção, incentivo, eventos e retail media.', '0.9'),
    'cases.html': ('/cases.html', 'Cases de PDV e trade marketing · 75 LAB',
                   '84 projetos reais de display, ponta de gôndola, enxoval, estande e ativação para marcas como '
                   'O Boticário, Unilever, Whirlpool, Seara, LG, Polenghi e 3 Corações.', '0.9'),
    'sobre.html': ('/sobre.html', 'Sobre a 75 LAB · agência de PDV fundada por varejo e indústria',
                   'Fundada em 2024 por Caique Becker (varejo) e Daniel Coimbra (indústria), a 75 LAB cria e produz '
                   'PDV comprovado. Sede no CENU, Av. das Nações Unidas, São Paulo.', '0.7'),
    'midia.html': ('/midia.html', '75 LAB na imprensa · Propmark, Giro News e ABCCOM',
                   'Artigos e notícias sobre a 75 LAB em Propmark, Giro News e ABC da Comunicação, e os canais da '
                   'agência no LinkedIn e no Instagram.', '0.6'),
    'contato.html': ('/contato.html', 'Contato e orçamento de display e material de PDV · 75 LAB',
                     'Peça orçamento de display, ilha, enxoval de PDV, estande ou projeto de trade marketing. '
                     'WhatsApp (11) 98676-5634, contato@75lab.com.br, CENU São Paulo.', '0.8'),
}
EXTRA = os.path.join(RAIZ, '_build', 'paginas_extra.json')
SEM_SITEMAP = {'404.html'}


def carregar_extra():
    """Páginas geradas (serviços, cases, guias) registram-se aqui:
    {"arquivo.html": {"titulo":..., "descricao":..., "prioridade":"0.8", "imagem": "/img/x.jpg",
                      "tipo": "article", "ld": [ {...schema extra...} ], "migalhas": [["Soluções","/solucoes.html"]]}}"""
    if not os.path.exists(EXTRA):
        return {}
    return json.load(open(EXTRA, encoding='utf-8'))


LOCAIS = {'pt': ('pt-BR', 'pt_BR'), 'en': ('en', 'en_US'), 'es': ('es', 'es_ES')}
HREFLANG = os.path.join(RAIZ, '_build', 'hreflang.json')


def alternativos(caminho):
    if not os.path.exists(HREFLANG):
        return []
    for grupo in json.load(open(HREFLANG, encoding='utf-8')):
        if caminho in grupo.values():
            linhas = [f'<link rel="alternate" hreflang="{LOCAIS[l][0]}" href="{SITE}{c}">' for l, c in grupo.items()]
            linhas.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}{grupo["pt"]}">')
            return linhas
    return []


def bloco(arquivo, caminho, titulo, desc, imagem=OG_PADRAO, tipo='website', ld_extra=None, migalhas=None, lang='pt'):
    url = SITE + caminho
    e = lambda s: html.escape(s, quote=True)
    pagina = {'@type': 'WebPage', '@id': url + '#pagina', 'url': url, 'name': titulo,
              'description': desc, 'inLanguage': LOCAIS[lang][0], 'isPartOf': {'@id': SITE + '/#site'},
              'about': {'@id': SITE + '/#org'}, 'primaryImageOfPage': imagem}
    grafo = [ORG, SITE_LD, pagina]
    if migalhas:
        itens = [{'@type': 'ListItem', 'position': 1, 'name': 'Início', 'item': SITE + '/'}]
        for i, (nome, cam) in enumerate(migalhas, start=2):
            itens.append({'@type': 'ListItem', 'position': i, 'name': nome, 'item': SITE + cam})
        grafo.append({'@type': 'BreadcrumbList', 'itemListElement': itens})
    grafo += ld_extra or []
    ld = json.dumps({'@context': 'https://schema.org', '@graph': grafo}, ensure_ascii=False,
                    separators=(',', ':')).replace('</', '<\\/')
    return '\n'.join([
        '<!-- seo:inicio (gerado por _build/seo.py; não editar à mão) -->',
        f'<title>{e(titulo)}</title>',
        f'<meta name="description" content="{e(desc)}">',
        f'<link rel="canonical" href="{url}">',
        '<meta name="robots" content="index, follow, max-image-preview:large">',
        f'<meta property="og:locale" content="{LOCAIS[lang][1]}">',
        *alternativos(caminho),
        f'<meta property="og:type" content="{tipo}">',
        '<meta property="og:site_name" content="75 LAB">',
        f'<meta property="og:title" content="{e(titulo)}">',
        f'<meta property="og:description" content="{e(desc)}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{imagem}">',
        '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{e(titulo)}">',
        f'<meta name="twitter:description" content="{e(desc)}">',
        f'<meta name="twitter:image" content="{imagem}">',
        f'<script type="application/ld+json">{ld}</script>',
        '<!-- seo:fim -->'])


def aplicar(arquivo, novo):
    p = os.path.join(RAIZ, arquivo)
    h = open(p, encoding='utf-8').read()
    if '<!-- seo:inicio' in h:
        h = re.sub(r'<!-- seo:inicio.*?<!-- seo:fim -->', lambda m: novo, h, flags=re.S)
    else:
        h = re.sub(r'\s*<title>.*?</title>', '', h, count=1, flags=re.S)
        h = re.sub(r'\s*<meta name="description"[^>]*>', '', h, count=1)
        h = re.sub(r'(<meta name="viewport"[^>]*>)', lambda m: m.group(1) + '\n' + novo, h, count=1)
    open(p, 'w', encoding='utf-8').write(h)


def main():
    todas = []
    for arq, (cam, tit, desc, prio) in PAGINAS.items():
        aplicar(arq, bloco(arq, cam, tit, desc, migalhas=None if cam == '/' else [(tit.split(' · ')[0], cam)]))
        todas.append((cam, prio))
    for arq, c in carregar_extra().items():
        cam = '/' + (arq[:-len('index.html')] if arq.endswith('index.html') else arq)
        img = SITE + c['imagem'] if c.get('imagem') else OG_PADRAO
        aplicar(arq, bloco(arq, cam, c['titulo'], c['descricao'], img, c.get('tipo', 'website'),
                           c.get('ld'), c.get('migalhas'), c.get('lang', 'pt')))
        todas.append((cam, c.get('prioridade', '0.7')))
    # 404 não entra no índice
    p404 = os.path.join(RAIZ, '404.html')
    h = open(p404, encoding='utf-8').read()
    if 'noindex' not in h:
        h = re.sub(r'(<meta name="viewport"[^>]*>)', r'\1\n<meta name="robots" content="noindex">', h, count=1)
        open(p404, 'w', encoding='utf-8').write(h)
    linhas = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for cam, prio in todas:
        linhas.append(f'  <url><loc>{SITE}{cam}</loc><lastmod>{HOJE}</lastmod><priority>{prio}</priority></url>')
    linhas.append('</urlset>')
    open(os.path.join(RAIZ, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(linhas) + '\n')
    print(f'ok: {len(todas)} páginas, sitemap.xml gerado')


if __name__ == '__main__':
    main()
