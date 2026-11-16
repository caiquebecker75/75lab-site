# Ferramentas do site (não são servidas: o .htaccess bloqueia /_build)

Depois de mexer em conteúdo:

    python3 _build/paginas.py   # gera serviços, cases, guias e guias.html a partir de _build/conteudo/
    python3 _build/seo.py       # título, descrição, canonical, prévia de link, schema.org e sitemap.xml
    python3 _build/og.py        # só se quiser refazer img/og-75lab.jpg

- Serviço novo: acrescentar um dicionário em `conteudo/servicos.py`.
- Case novo: `conteudo/cases.py` (só cliente liberado por escrito; nunca Pokémon).
- Guia novo: um JSON em `conteudo/guias/` no mesmo formato dos existentes.
- Página fixa (index, cases, sobre...): título e descrição ficam em `PAGINAS` dentro de `seo.py`.
- Fatos oficiais (CNPJ, endereço, sócios, contato) ficam em `FATOS` dentro de `seo.py` e no `llms.txt`.
- Regra de texto: nada de travessão; o gerador recusa.
