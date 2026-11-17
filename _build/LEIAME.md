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

## IndexNow (Bing, Copilot, busca do ChatGPT)
Depois de publicar página nova ou mudar página existente, rode `python3 _build/indexnow.py /pagina.html` (sem argumento manda o sitemap inteiro). A chave fica em `/<chave>.txt` na raiz; não apague. O `guia_site.py publicar` do conteudo-75lab já chama sozinho.

## Google Analytics 4
Tag G-JL0KM1HHNM (propriedade "75 LAB", conta Agência Becker Marketing) no `<head>` de todas as páginas, junto com a do Google Ads. O gerador copia o cabeçalho do sobre.html, então página nova já sai com a tag.

## Ordem obrigatória
Sempre `python3 _build/paginas.py` ANTES de `python3 _build/seo.py`. O paginas.py copia o cabeçalho do sobre.html (com o bloco SEO dele); o seo.py é que reescreve o bloco certo de cada página.
