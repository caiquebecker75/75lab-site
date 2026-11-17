# Conteúdo das páginas "display para <categoria>". Marcação: **negrito** e [texto](url).
# Blocos: {"p": ...}, {"lista": [...]}, {"tabela": {"cab": [...], "linhas": [[...]]}}

GUIA_TOMBA = '[display que não tomba](guia-display-que-nao-tomba.html)'
GUIA_MAT = '[guia de materiais](guia-material-display-pdv.html)'
CALC = '[calculadora de display](calculadora-display-pdv.html)'
RAST = '[como rastrear material de PDV](guia-como-rastrear-material-de-pdv.html)'
CLIP = '[guia de clip strip](guia-clip-strip.html)'
PONTA = '[guia de ponta de gôndola](guia-ponta-de-gondola.html)'
BRIEF = '[briefing de display](guia-briefing-display-pdv.html)'
EXEC = '[checklist do executivo](guia-checklist-executivo-pdv.html)'
RA = '[realidade aumentada](guia-realidade-aumentada-no-pdv.html)'
ENX = '[enxoval de PDV](guia-o-que-e-enxoval-de-pdv.html)'

PAGINAS = []

# 1 ---------------------------------------------------------------------------
PAGINAS.append({
 'slug': 'display-para-chocolate-e-confeitos',
 'cat': 'chocolate e confeitos', 'curto': 'Display para chocolate e confeitos',
 'titulo': 'Display para chocolate e confeitos no PDV · 75 LAB',
 'descricao': 'Como expor chocolate, bala e confeito no PDV: display de checkout, clip strip, parreiral de Páscoa, material indicado, cuidado com calor e checklist de projeto.',
 'h1': 'Display de PDV para **chocolate** e confeitos.',
 'lead': 'Chocolate vende por impulso, sofre com calor e vive de datas. O display certo resolve as três coisas antes de ir para a loja.',
 'k': 'Alimentos', 'card': 'Checkout, clip strip, parreiral de Páscoa e o cuidado com calor e luz que o chocolate pede.',
 'segmento': ('PDV para alimentos', 'pdv-para-alimentos.html'),
 'guias': [('Guia de clip strip', 'guia-clip-strip.html'), ('Display que não tomba', 'guia-display-que-nao-tomba.html')],
 'resumo': 'Display para chocolate e confeitos precisa resolver três coisas: estar onde a compra por impulso acontece, proteger o produto do calor e da luz e aguentar picos curtos de volume em datas como a Páscoa. Na prática, funcionam display de balcão no checkout, clip strip em cross merchandising, display de chão de papelão para ação sazonal e estrutura metálica para o parreiral de ovos.',
 'secoes': [
  {'h2': 'O que muda no PDV de chocolate e confeitos', 'blocos': [
   {'p': 'Barra, bombom, bala, chiclete e confeito vivem de impulso: a decisão acontece na frente da peça, e a localização vale mais que o tamanho do display. Checkout de supermercado, balcão de padaria, conveniência e farmácia são canais em que um display pequeno e bem abastecido trabalha muito.'},
   {'p': 'A sazonalidade é das mais fortes de alimentos: a Páscoa muda o layout da loja, com ovos pendurados em estrutura própria no corredor. Fora das datas, o trabalho é de giro: muitos itens pequenos, reposição frequente e ruptura que aparece rápido.'},
   {'p': 'E chocolate amolece e perde aparência com calor: peça perto de vitrine com sol, luminária quente, forno ou motor de refrigerador estraga o produto e gera troca.'}]},
  {'h2': 'Peças que funcionam e onde ficam', 'blocos': [
   {'tabela': {'cab': ['Peça', 'Onde fica', 'Quando usar'], 'linhas': [
    ['Display de balcão', 'Checkout, balcão de padaria, conveniência e farmácia', 'Barra, bala, chiclete e confeito de impulso, com reposição diária'],
    ['Clip strip', 'Lateral de gôndola de café, biscoito ou sorvete, ou perto do caixa', 'Confeito e bala em embalagem com furo, em cross merchandising'],
    ['Display de chão', 'Ponto extra no corredor ou na entrada da loja', 'Lançamento e ação sazonal de algumas semanas'],
    ['Ponta de gôndola', 'Cabeceira do corredor de doces', 'Caixas de bombom no Natal e no Dia das Mães, promoção de multipack'],
    ['Parreiral de Páscoa', 'Corredor ou área sazonal da loja', 'Ovos pendurados, com estrutura de carga e comunicação no alto'],
    ]}}]},
  {'h2': 'Material indicado e por quê', 'blocos': [
   {'p': 'Para ação sazonal em muitas lojas, papelão ondulado é o caminho natural: vai plano, monta sem ferramenta e a carga de chocolate por nível é baixa. Para checkout que fica meses, acrílico, PETG ou chapa metálica com comunicação trocável duram mais.'},
   {'p': 'O parreiral carrega muitos ovos pendurados ao mesmo tempo, então pede estrutura metálica ou arame soldado, com a carga por gancho calculada. O ' + GUIA_MAT + ' compara as opções por tempo de exposição, peso e número de lojas.'}]},
  {'h2': 'Calor, luz e carga: os cuidados de projeto', 'blocos': [
   {'lista': [
    '**Posição:** defina no briefing onde a peça fica, longe de sol direto, vitrine, luminária quente, forno e saída de ar de equipamento.',
    '**Luz da própria peça:** LED de baixo aquecimento, afastado do produto.',
    '**Carga pendurada:** no parreiral e no clip strip, a conta é peso da unidade vezes unidades por gancho vezes número de ganchos, mais 20% de folga, regra de projeto que usamos. O ponto de fixação no alto carrega tudo isso.',
    '**Prateleira:** a carga é leve, mas prateleira de MDF à vista segue o limite de flecha L/300 com a fluência do material somada. A ' + CALC + ' faz a conta.',
    '**Estabilidade:** display de chão alto e leve tomba com esbarrão de carrinho. Veja o guia ' + GUIA_TOMBA + '.']}]},
  {'h2': 'Datas fortes do ano', 'blocos': [
   {'lista': [
    '**Páscoa:** parreiral, ponta de gôndola e ilha de ovos e caixas; é a data que mais exige estrutura e logística.',
    '**Dia das Mães e Dia dos Namorados:** caixas de bombom e embalagens para presente na ponta e no checkout.',
    '**Dia das Crianças:** confeitos e itens com brinde, na altura do olhar da criança.',
    '**Natal:** caixas de bombom, kits e itens para presente, em ilha e ponta de gôndola.']},
   {'p': 'Cada data tem entrada e retirada combinadas com a rede, e a retirada também entra no plano.'}]},
  {'h2': 'Checklist rápido', 'blocos': [
   {'lista': [
    'Posição na loja definida, longe de calor e sol.',
    'Peso real das embalagens tirado da ficha técnica, com 20% de folga.',
    'Carga por gancho conferida no clip strip e no parreiral.',
    'Reposição combinada: quem abastece e com que frequência.',
    'Montagem registrada loja a loja, com foto e localização. Veja ' + RAST + '.']}]}],
 'faq': [
  {'q': 'Qual o melhor display para chocolate no checkout?', 'a': 'Um display de balcão compacto, que não atrapalhe o caixa, com frentes estreitas para muitos itens e preço fácil de ler. Para peça que fica meses, acrílico, PETG ou metal com comunicação trocável duram mais que papelão.'},
  {'q': 'Display de papelão serve para chocolate?', 'a': 'Serve bem para ação sazonal de algumas semanas, porque a carga de chocolate por nível é baixa. Os cuidados são a umidade do piso e a posição longe de calor.'},
  {'q': 'Como evitar que o chocolate derreta no display?', 'a': 'Escolha a posição antes de desenhar a peça: longe de sol direto, vitrine envidraçada, luminária quente, forno e saída de ar de equipamentos. Se o display tiver luz própria, use LED de baixo aquecimento afastado do produto.'},
  {'q': 'Quando começar o projeto do PDV de Páscoa?', 'a': 'Conte de trás para frente a partir da data de entrada combinada com a rede: montagem, frete, produção, aprovação e projeto. A aprovação em realidade aumentada encurta a etapa de aprovação, mas produção e logística para muitas lojas pedem folga no cronograma.'}],
})

# 2 ---------------------------------------------------------------------------
PAGINAS.append({
 'slug': 'display-para-biscoitos-e-snacks',
 'cat': 'biscoitos e snacks', 'curto': 'Display para biscoitos e snacks',
 'titulo': 'Display para biscoitos e snacks no PDV · 75 LAB',
 'descricao': 'Como expor biscoito e salgadinho no PDV: display de chão, gancheira, clip strip em cross merchandising, ponta de gôndola, material, volume da embalagem e checklist.',
 'h1': 'Display de PDV para **biscoitos** e snacks.',
 'lead': 'Snack é leve e ocupa muito espaço; biscoito mistura compra planejada e impulso. O display precisa ser pensado pelo volume da embalagem e pela reposição.',
 'k': 'Alimentos', 'card': 'Display de chão, gancheira e clip strip perto da bebida, com projeto pelo volume da embalagem.',
 'segmento': ('PDV para alimentos', 'pdv-para-alimentos.html'),
 'guias': [('Guia de clip strip', 'guia-clip-strip.html'), ('Guia de ponta de gôndola', 'guia-ponta-de-gondola.html')],
 'resumo': 'Display para biscoitos e snacks se projeta pelo volume da embalagem, não pelo peso: salgadinho é leve e cheio de ar, e a peça lota antes de chegar ao limite de carga. Funcionam display de chão de papelão para ação curta, gancheira e clip strip para pacote com furo, ponta de gôndola para promoção e cross merchandising perto da bebida, com reposição pensada para girar o estoque.',
 'secoes': [
  {'h2': 'O que muda no PDV de biscoitos e snacks', 'blocos': [
   {'p': 'São duas lógicas de compra na mesma categoria. Biscoito de café da manhã, cream cracker e multipack de lancheira entram na lista de compras e são comprados no corredor. Recheado, wafer, salgadinho e amendoim têm muita compra por impulso, e respondem a ponto extra fora da gôndola da categoria.'},
   {'p': 'O canal muda a peça. No supermercado, a disputa é por ponta de gôndola e ponto extra no corredor de bebidas. No atacarejo, o produto vai em caixa de embarque e multipack, e a peça precisa aguentar volume e reposição com caixa fechada. Na conveniência e na padaria, a embalagem individual fica perto do caixa e da geladeira.'},
   {'p': 'E o lote mais antigo precisa sair primeiro: peça que só permite repor pela frente empurra o pacote velho para o fundo.'}]},
  {'h2': 'Peças que funcionam e onde ficam', 'blocos': [
   {'tabela': {'cab': ['Peça', 'Onde fica', 'Quando usar'], 'linhas': [
    ['Display de chão', 'Corredor de bebidas, entrada da loja, área de promoção', 'Lançamento, sabor novo e ação de algumas semanas'],
    ['Gancheira', 'Ponta de gôndola ou lateral de corredor', 'Salgadinho em pacote com furo, que fica melhor pendurado do que deitado'],
    ['Clip strip', 'Gôndola de cerveja e refrigerante, perto do caixa', 'Amendoim, snack pequeno e biscoito individual em cross merchandising'],
    ['Ponta de gôndola', 'Cabeceira do corredor de biscoitos', 'Promoção, multipack e lançamento com volume'],
    ['Ilha', 'Salão do atacarejo e do supermercado', 'Caixa de embarque e multipack em grande quantidade'],
    ['Display de balcão', 'Checkout, padaria e conveniência', 'Embalagem individual de impulso']]}}]},
  {'h2': 'Material indicado e por quê', 'blocos': [
   {'p': 'Como a carga é baixa, papelão ondulado atende bem a maior parte das ações de snack: é barato por unidade em grande tiragem, vai plano e aceita impressão em toda a superfície. O limite é o tempo e a umidade do piso, então para peça de meses vale estrutura de arame ou metal com comunicação trocável.'},
   {'p': 'Gancheira e cesto de arame resolvem o pacote pendurado e o produto a granel com pouco material. Biscoito em lata e caixa de presente de fim de ano pesam mais e pedem prateleira calculada. O ' + GUIA_MAT + ' detalha cada opção.'}]},
  {'h2': 'Volume, carga e reposição: os cuidados de projeto', 'blocos': [
   {'p': 'Exemplo ilustrativo: um nível com 6 frentes e 4 pacotes de salgadinho de cerca de 100 g na profundidade soma uns 2,4 kg, ou perto de 2,9 kg com os 20% de folga que usamos como regra de projeto. A conta de carga quase sempre passa; o que decide o projeto é altura livre entre níveis, profundidade e quantos pacotes cabem sem amassar.'},
   {'lista': [
    '**Altura entre níveis:** meça o pacote cheio, não o arquivo da embalagem. Pacote com ar ocupa mais do que o desenho indica.',
    '**Empilhamento:** não conte com pacote em cima de pacote; o de baixo amassa e o shopper desiste.',
    '**Reposição:** prateleira com rampa ou abastecimento por trás ajuda a vender primeiro o lote mais antigo.',
    '**Gancho:** carga por gancho conferida com o peso real, como no ' + CLIP + '.',
    '**Estabilidade:** display de papelão alto e leve precisa de base larga ou lastro. Veja ' + GUIA_TOMBA + '.']}]},
  {'h2': 'Datas fortes do ano', 'blocos': [
   {'lista': [
    '**Volta às aulas:** multipack, biscoito de lancheira e porção individual.',
    '**Verão e férias:** snack de festa e de consumo em casa, perto da bebida.',
    '**Festas juninas:** amendoim, pipoca e paçoca em cesto e display de chão.',
    '**Jogos e campeonatos de futebol:** cross merchandising com cerveja e refrigerante.',
    '**Fim de ano:** biscoito em lata e caixa para presente na ponta de gôndola.']}]},
  {'h2': 'Checklist rápido', 'blocos': [
   {'lista': [
    'Pacote real medido cheio, com altura e profundidade.',
    'Carga por nível e por gancho calculada, com 20% de folga.',
    'Forma de reposição definida para girar o lote mais antigo.',
    'Ponto de cross merchandising negociado com a rede.',
    'Material escolhido pelo tempo de exposição e pela umidade do piso.',
    'Instalação conferida loja a loja. Veja ' + RAST + '.']}]}],
 'faq': [
  {'q': 'Qual display usar para salgadinho?', 'a': 'Para ação curta, display de chão de papelão no corredor de bebidas ou na entrada da loja. Para pacote com furo, gancheira na ponta de gôndola. Para impulso no caixa, display de balcão com porção individual.'},
  {'q': 'Por que o display de snack se projeta pelo volume e não pelo peso?', 'a': 'Porque o pacote é leve e cheio de ar: a peça lota antes de chegar perto do limite de carga. Altura livre entre níveis, profundidade e quantos pacotes cabem sem amassar decidem mais que a conta de flecha.'},
  {'q': 'Onde colocar biscoito e snack fora do corredor?', 'a': 'Perto da bebida é o cross merchandising mais comum, com clip strip ou display de chão. No caixa, entra a embalagem individual de impulso. Em todo caso, o ponto precisa ser negociado com a rede.'}],
})

# 3 ---------------------------------------------------------------------------
PAGINAS.append({
 'slug': 'display-para-cerveja',
 'cat': 'cerveja', 'curto': 'Display para cerveja',
 'titulo': 'Display de PDV para cerveja: peças e carga · 75 LAB',
 'descricao': 'Como expor cerveja no PDV: ilha de fardos, ponta de gôndola, comunicação de geladeira, display de chão, carga de lata e garrafa, umidade e checklist de projeto.',
 'h1': 'Display de PDV para **cerveja**.',
 'lead': 'Cerveja é pesada, vende gelada e concentra o volume no calor e nas festas. O display precisa aguentar o fardo e conviver com a umidade.',
 'k': 'Bebidas', 'card': 'Ilha de fardos, geladeira, ponta de gôndola e a conta de carga que lata e garrafa exigem.',
 'segmento': ('PDV para bebidas', 'pdv-para-bebidas.html'),
 'guias': [('Display que não tomba', 'guia-display-que-nao-tomba.html'), ('Guia de ponta de gôndola', 'guia-ponta-de-gondola.html')],
 'resumo': 'Display para cerveja começa pela carga: lata e garrafa cheias pesam, e a peça precisa ser calculada para o fardo e conferida contra tombamento. Funcionam ilha e pilha de fardos no atacarejo e no supermercado, ponta de gôndola, display de chão em metal ou arame e comunicação de geladeira na conveniência. Papelão só com reforço e base protegida, porque lata gelada condensa e o piso é lavado.',
 'secoes': [
  {'h2': 'O que muda no PDV de cerveja', 'blocos': [
   {'p': 'A cerveja tem dois momentos de compra. Para casa e para a festa, a compra é planejada, em fardo, no supermercado e no atacarejo. Para consumo imediato, a compra é gelada, na conveniência, na padaria e no bar, e o PDV mais importante é a geladeira.'},
   {'p': 'O volume se concentra no calor e nas datas: verão, Carnaval, fim de ano, festas e jogos de futebol. Em poucas semanas, a loja precisa de muito produto exposto e de peça que aguente reposição constante. Cerveja especial vende também em adega e empório, com peça menor que conta a história do produto.'}]},
  {'h2': 'Peças que funcionam e onde ficam', 'blocos': [
   {'tabela': {'cab': ['Peça', 'Onde fica', 'Quando usar'], 'linhas': [
    ['Ilha ou pilha de fardos', 'Salão do atacarejo e do supermercado', 'Datas fortes e promoção de volume; o fardo carrega o fardo e a peça faz moldura e comunicação'],
    ['Ponta de gôndola', 'Cabeceira do corredor de bebidas', 'Lançamento, promoção e sazonalidade'],
    ['Display de chão em metal ou arame', 'Ponto extra no corredor ou perto do açougue', 'Lata e long neck em ação de semanas'],
    ['Comunicação de geladeira', 'Porta, testeira e régua do refrigerador', 'Conveniência, padaria e bar, onde a compra é gelada'],
    ['Refrigerador da marca', 'Checkout e salão da conveniência', 'Quando a rede aceita equipamento próprio'],
    ['Display de balcão', 'Adega, empório e conveniência', 'Cerveja especial, kit e lançamento em garrafa']]}}]},
  {'h2': 'Material indicado e por quê', 'blocos': [
   {'p': 'Chapa de aço dobrada, tubo e arame soldado são a base do display de cerveja: carregam muito peso com pouca estrutura e aguentam a reposição de fardo. A comunicação vai em placa de PS, PETG ou chapa, trocável entre campanhas.'},
   {'p': 'Papelão é usado em ação curta, mas perde resistência com umidade. Lata gelada condensa, o fardo molha o fundo e o piso é lavado todos os dias. Se for papelão, a base precisa de proteção e a prateleira de reforço interno. Em MDF, a prateleira pede conta de flecha com fluência, porque fica carregada a campanha inteira. O ' + GUIA_MAT + ' compara os materiais.'}]},
  {'h2': 'Carga e estabilidade: os cuidados de projeto', 'blocos': [
   {'p': 'Exemplo ilustrativo: uma lata de 350 ml cheia pesa por volta de 0,37 kg. Um nível com 8 frentes e 3 latas na profundidade soma cerca de 8,9 kg; com os 20% de folga que usamos como regra de projeto, são quase 10,7 kg por nível. Em long neck de vidro a conta sobe e entra o risco de quebra. Use sempre o peso da ficha técnica do produto.'},
   {'lista': [
    '**Peso embaixo:** o produto pesado fica nos níveis baixos e o fardo vai no chão, nunca no alto da peça.',
    '**Tombamento:** confira peça vazia, cheia e o pior caso de reposição, com o nível de cima cheio e os de baixo vazios. Veja ' + GUIA_TOMBA + '.',
    '**Flecha:** prateleira à vista no limite L/300; em MDF, some a fluência. A ' + CALC + ' faz a conta.',
    '**Batente:** borda frontal para a garrafa não escorregar.',
    '**Comunicação:** bebida alcoólica segue a autorregulamentação publicitária e regras de rede e de estado, como frases de advertência e aviso de venda proibida para menores de 18 anos. Confira com o jurídico da marca e com a rede antes de fechar a arte.']}]},
  {'h2': 'Datas fortes do ano', 'blocos': [
   {'lista': [
    '**Verão e Carnaval:** o pico de volume, com ilha de fardos e geladeira cheia.',
    '**Fim de ano:** festas e confraternizações, com fardo e kit.',
    '**Jogos de futebol e campeonatos:** ponto extra com cross merchandising de snack.',
    '**Dia dos Pais:** kits e cervejas especiais.',
    ]}]},
  {'h2': 'Checklist rápido', 'blocos': [
   {'lista': [
    'Peso real de lata, garrafa e fardo tirado da ficha técnica, com 20% de folga.',
    'Produto pesado embaixo e tombamento conferido no pior caso de reposição.',
    'Material resistente à umidade, ou papelão com base protegida.',
    'Arte conferida pelo jurídico e pela regra da rede.',
    'Reposição de fardo combinada para o pico.',
    'Montagem registrada loja a loja. Veja ' + RAST + '.']}]}],
 'faq': [
  {'q': 'Qual o melhor material para display de cerveja?', 'a': 'Metal e arame soldado, porque carregam muito peso com pouca estrutura e aguentam umidade e reposição. Papelão funciona em ação curta, com prateleira reforçada e base protegida contra o piso molhado.'},
  {'q': 'Quanto peso aguenta um display de cerveja?', 'a': 'Depende do material, do vão e da espessura de cada prateleira. A conta parte do peso real da lata ou garrafa vezes frentes vezes profundidade, mais 20% de folga, e confere flecha, fluência e tombamento.'},
  {'q': 'Display de cerveja precisa de aviso de venda proibida para menores?', 'a': 'A comunicação de bebida alcoólica segue a autorregulamentação publicitária e regras de rede e de estado, que podem pedir frases de advertência e aviso de venda proibida para menores de 18 anos. Confira com o jurídico da marca e com a rede antes de produzir.'},
],
})

# 4 ---------------------------------------------------------------------------
PAGINAS.append({
 'slug': 'display-para-vinhos-e-destilados',
 'cat': 'vinhos e destilados', 'curto': 'Display para vinhos e destilados',
 'titulo': 'Display para vinhos e destilados no PDV · 75 LAB',
 'descricao': 'Como expor vinho e destilado no PDV: expositor de garrafas, ilha de Natal, vitrine para destilado premium, carga de vidro, fluência do MDF, antifurto e checklist.',
 'h1': 'Display de PDV para **vinhos** e destilados.',
 'lead': 'Vinho e destilado são compra mais pensada, de ticket alto e presente. O display precisa informar, valorizar a garrafa e segurar o peso do vidro.',
 'k': 'Bebidas', 'card': 'Expositor de garrafas, ilha de Natal, vitrine para destilado premium e a carga do vidro.',
 'segmento': ('PDV para bebidas', 'pdv-para-bebidas.html'),
 'guias': [('Display que não tomba', 'guia-display-que-nao-tomba.html'), ('Material do display', 'guia-material-display-pdv.html')],
 'resumo': 'Display para vinhos e destilados precisa informar, valorizar a garrafa e aguentar o vidro. Funcionam expositor de chão com nichos ou prateleiras com batente, ilha e ponta de gôndola de Natal, display de balcão e vitrine com trava para destilado premium, e comunicação no gargalo. A prateleira cheia de garrafas é o caso clássico em que o MDF passa na conta inicial e reprova com a fluência.',
 'secoes': [
  {'h2': 'O que muda no PDV de vinhos e destilados', 'blocos': [
   {'p': 'É uma compra mais pensada que a cerveja: o shopper lê rótulo, país, uva e preço, compara e muitas vezes compra para presente. A peça precisa de informação clara, preço legível e um jeito de destacar a garrafa.'},
   {'p': 'Os canais são supermercado, atacarejo, adega e empório, onde existe atendimento. O destilado premium tem ticket alto, o que traz o furto para o projeto, e o fim de ano concentra as vendas para presente.'}]},
  {'h2': 'Peças que funcionam e onde ficam', 'blocos': [
   {'tabela': {'cab': ['Peça', 'Onde fica', 'Quando usar'], 'linhas': [
    ['Expositor de chão com nichos ou prateleiras', 'Corredor de vinhos, adega e empório', 'Linha de rótulos ou país, com informação de uva e harmonização'],
    ['Ilha de Natal', 'Salão do supermercado e do atacarejo', 'Caixas para presente, kits e espumante de fim de ano'],
    ['Ponta de gôndola', 'Cabeceira do corredor de bebidas', 'Promoção e lançamento de rótulo'],
    ['Vitrine ou display de balcão com trava', 'Perto do caixa ou do atendimento', 'Destilado premium, com garrafa exposta e estoque protegido'],
    ['Glorifier', 'Ponta, balcão ou nicho de destaque', 'Uma garrafa só, iluminada, para lançamento ou rótulo premium'],
    ['Comunicação no gargalo', 'Na própria garrafa', 'Prêmio, harmonização ou promoção sem ocupar espaço']]}}]},
  {'h2': 'Material indicado e por quê', 'blocos': [
   {'p': 'Madeira e MDF com bom acabamento combinam com o vinho, e metal pintado resolve estrutura e carga. Acrílico entra no glorifier, na vitrine e no porta-preço. Papelão funciona para ação curta de fim de ano em muitas lojas, com reforço interno, porque garrafa é carga alta para ele.'},
   {'p': 'A escolha sai da conta de carga, do tempo de exposição e do custo por loja, como explica o ' + GUIA_MAT + '.'}]},
  {'h2': 'Vidro, carga e fluência: os cuidados de projeto', 'blocos': [
   {'p': 'Exemplo ilustrativo: uma garrafa de 750 ml cheia costuma pesar entre 1,2 e 1,6 kg, conforme o vidro. Um nível com 12 garrafas soma perto de 18 kg; com os 20% de folga que usamos como regra de projeto, chega perto de 22 kg. É o caso do guia ' + GUIA_TOMBA + ': prateleira de MDF de 18 mm, com vão de 600 mm, 400 mm de profundidade e cerca de 20 kg, passa na flecha inicial e reprova depois de somada a fluência do MDF, que multiplica a flecha por perto de 3,25. Na prática, a garrafa pede vão menor, borda dobrada, travessa ou chapa de aço.'},
   {'lista': [
    '**Batente e berço:** garrafa em pé pede borda frontal; garrafa deitada pede berço que trave o giro e o deslizamento.',
    '**Tombamento:** expositor alto e cheio de vidro pede conferência do pior caso de reposição e, às vezes, fixação.',
    '**Luz e calor:** evite sol direto e luminária quente sobre a garrafa durante semanas; se a peça tiver luz, use LED de baixo aquecimento.',
    '**Antifurto:** destilado premium pede vitrine com trava, garrafa cenográfica na exposição com o estoque no atendimento, ou o sistema que a rede usar.',
    '**Comunicação:** bebida alcoólica tem regras de comunicação e de venda, como advertências e venda proibida para menores de 18 anos. Confira com o jurídico da marca, com a rede e com a regra do estado.']}]},
  {'h2': 'Datas fortes do ano', 'blocos': [
   {'lista': [
    '**Natal e Réveillon:** o grande pico, com ilha, kits, caixas para presente e espumante.',
    '**Dia dos Pais:** destilados e kits para presente.',
    '**Dia dos Namorados:** vinho e espumante.',
    '**Inverno e festas juninas:** vinho tinto e ações de vinho quente.']}]},
  {'h2': 'Checklist rápido', 'blocos': [
   {'lista': [
    'Peso real da garrafa cheia tirado da ficha técnica, com 20% de folga.',
    'Flecha conferida com fluência quando a prateleira for de MDF ou MDP. Use a ' + CALC + '.',
    'Batente ou berço em toda prateleira.',
    'Tombamento conferido com o expositor cheio, vazio e no pior caso de reposição.',
    'Estratégia de antifurto definida para o destilado premium.',
    'Arte conferida pelo jurídico e instalação registrada loja a loja. Veja ' + RAST + '.']}]}],
 'faq': [
  {'q': 'Qual o melhor display para vinho no supermercado?', 'a': 'Um expositor com nichos ou prateleiras com batente, que mostre o rótulo e traga informação clara de uva, país e preço. Para o fim de ano, ilha e ponta de gôndola com caixas para presente e kits.'},
  {'q': 'Prateleira de MDF aguenta garrafa de vinho?', 'a': 'Depende do vão, da espessura e da carga. Com garrafas, a carga por nível passa facilmente de 20 kg, e o MDF continua cedendo com o tempo. Muitas vezes a prateleira passa na conta inicial e reprova com a fluência; vão menor, borda dobrada ou chapa de aço resolvem.'},
  {'q': 'Como expor destilado premium sem perder para o furto?', 'a': 'Com vitrine ou display de balcão com trava, garrafa cenográfica na exposição e estoque no atendimento, ou com o sistema antifurto que a rede já usa. Defina isso no briefing, porque muda o desenho da peça.'}],
})

# 5 ---------------------------------------------------------------------------
PAGINAS.append({
 'slug': 'display-para-refrigerante-e-agua',
 'cat': 'refrigerante e água', 'curto': 'Display para refrigerante e água',
 'titulo': 'Display para refrigerante e água no PDV · 75 LAB',
 'descricao': 'Como expor refrigerante e água no PDV: ilha de fardos, display de chão para PET, ponta de gôndola, geladeira no checkout, carga de garrafa cheia e checklist de projeto.',
 'h1': 'Display de PDV para **refrigerante** e água.',
 'lead': 'É a categoria mais pesada do autosserviço por nível de peça. O display bom deixa o fardo carregar o fardo e a estrutura cuidar da comunicação.',
 'k': 'Bebidas', 'card': 'Ilha de fardos, display para PET, geladeira no checkout e a carga da garrafa cheia.',
 'segmento': ('PDV para bebidas', 'pdv-para-bebidas.html'),
 'guias': [('Display que não tomba', 'guia-display-que-nao-tomba.html'), ('Guia de ponta de gôndola', 'guia-ponta-de-gondola.html')],
 'resumo': 'Display para refrigerante e água lida com a maior carga do autosserviço: garrafa PET cheia e fardo pesam muito por nível. Funcionam ilha e pilha de fardos com moldura de comunicação, display de chão em metal ou arame com o produto nos níveis baixos, ponta de gôndola e geladeira ou cooler no checkout para a compra gelada. O verão e as festas concentram o volume.',
 'secoes': [
  {'h2': 'O que muda no PDV de refrigerante e água', 'blocos': [
   {'p': 'São dois produtos com duas compras. A garrafa grande e o fardo vão para casa, em compra planejada no supermercado e no atacarejo, muito guiada por preço e promoção. A embalagem individual é compra gelada e de impulso, na conveniência, na padaria, no posto e no checkout do supermercado.'},
   {'p': 'O calor muda tudo: no verão a água e o refrigerante giram muito mais rápido, a ruptura aparece em horas e a reposição precisa ser fácil. A peça é testada pelo peso, pela umidade da garrafa gelada e pelo repositor que chega com o carrinho cheio de fardos.'}]},
  {'h2': 'Peças que funcionam e onde ficam', 'blocos': [
   {'tabela': {'cab': ['Peça', 'Onde fica', 'Quando usar'], 'linhas': [
    ['Ilha ou pilha de fardos com moldura', 'Salão do atacarejo e do supermercado', 'Verão, festas e promoção de volume'],
    ['Display de chão em metal ou arame', 'Corredor de bebidas ou ponto extra', 'Garrafa PET e lata em ação de semanas'],
    ['Ponta de gôndola', 'Cabeceira do corredor de bebidas', 'Lançamento, sabor novo e promoção'],
    ['Geladeira ou cooler de checkout', 'Caixa do supermercado, conveniência e padaria', 'Embalagem individual gelada, de impulso'],
    ['Comunicação de geladeira', 'Porta, testeira e régua do refrigerador', 'Destacar a marca onde a compra é gelada'],
    ['Cesto', 'Perto do caixa ou da área de lanches', 'Água em garrafa individual e combo com snack']]}}]},
  {'h2': 'Material indicado e por quê', 'blocos': [
   {'p': 'Metal e arame soldado são a regra para carregar garrafa cheia: módulo alto, pouca estrutura e boa resistência a umidade. A comunicação vai em placa de PS, PETG ou chapa. Na ilha de fardos, a peça costuma ser base, moldura e testeira, e o próprio produto empilhado faz o volume.'},
   {'p': 'Papelão aparece em saia e moldura de ação curta, mas não deve carregar garrafa sem reforço, porque perde resistência com a condensação e com o piso lavado. Prateleira de MDF para PET pede conta de flecha com fluência. O ' + GUIA_MAT + ' compara as opções.'}]},
  {'h2': 'Carga e estabilidade: os cuidados de projeto', 'blocos': [
   {'p': 'Exemplo ilustrativo: uma garrafa PET de 2 litros cheia pesa um pouco mais de 2 kg. Um nível com 4 frentes e 3 garrafas na profundidade passa de 24 kg, e com os 20% de folga que usamos como regra de projeto chega perto de 30 kg. É carga para aço, vão curto ou produto apoiado no chão. Use o peso da ficha técnica do produto.'},
   {'lista': [
    '**O fardo carrega o fardo:** quando possível, o produto pesado fica empilhado no chão e a estrutura cuida da comunicação, sem depender do produto para ficar de pé.',
    '**Empilhamento:** respeite a altura de pilha indicada para a embalagem; fardo amassado vira perda.',
    '**Peso embaixo:** garrafa grande nos níveis baixos, embalagem individual no alto.',
    '**Tombamento:** confira peça vazia, cheia e o pior caso de reposição. Veja ' + GUIA_TOMBA + '.',
    '**Flecha:** prateleira à vista no limite L/300, com fluência somada em MDF. A ' + CALC + ' faz a conta.',
    '**Umidade:** base elevada ou protegida contra a água da condensação e do pano de limpeza.']}]},
  {'h2': 'Datas fortes do ano', 'blocos': [
   {'lista': [
    '**Verão:** o pico de água e refrigerante, com ilha de fardos e geladeira cheia.',
    '**Natal e Réveillon:** garrafa grande para a ceia e para as festas.',
    '**Carnaval e férias:** água e embalagem individual na conveniência e no checkout.',
    '**Festas juninas e jogos de futebol:** combos com snack e ponto extra.']}]},
  {'h2': 'Checklist rápido', 'blocos': [
   {'lista': [
    'Peso real da garrafa e do fardo, com 20% de folga.',
    'Decisão escrita: o produto apoia no chão ou na prateleira.',
    'Altura de empilhamento respeitada.',
    'Material resistente à umidade e base protegida.',
    'Reposição planejada para o pico do verão.',
    'Montagem registrada loja a loja. Veja ' + RAST + '.']}]}],
 'faq': [
  {'q': 'Qual display usar para garrafa PET de 2 litros?', 'a': 'Display de chão em metal ou arame, com a garrafa nos níveis baixos e vãos curtos, ou ilha de fardos com moldura de comunicação. Papelão só com reforço, porque a carga é alta e a condensação enfraquece o material.'},
  {'q': 'Ilha de fardos de água precisa de estrutura?', 'a': 'O fardo empilhado faz o volume, e a peça entra como base, moldura e testeira. O cuidado é respeitar a altura de empilhamento da embalagem e garantir que a moldura fique de pé sozinha.'},
  {'q': 'Onde colocar refrigerante gelado na loja?', 'a': 'No checkout e perto da área de lanches, em geladeira ou cooler, onde a compra é de impulso e de consumo imediato. Equipamento próprio da marca depende de a rede aceitar.'}],
})

# 6 ---------------------------------------------------------------------------
PAGINAS.append({
 'slug': 'display-para-racao-e-petiscos-pet',
 'cat': 'ração e petiscos pet', 'curto': 'Display para ração e petiscos pet',
 'titulo': 'Display para ração e petiscos pet no PDV · 75 LAB',
 'descricao': 'Como expor ração e petisco no PDV: display para saco de ração, ilha em pet shop, clip strip de petisco, material lavável, carga de embalagem grande e checklist.',
 'h1': 'Display de PDV para **ração** e petiscos pet.',
 'lead': 'Ração é compra planejada, recorrente e pesada; petisco é impulso. O PDV pet precisa das duas lógicas na mesma loja.',
 'k': 'Pet', 'card': 'Saco de ração no chão, petisco no caixa e material lavável para a gordura e o pó.',
 'segmento': ('PDV para pet', 'pdv-para-pet.html'),
 'guias': [('Guia de clip strip', 'guia-clip-strip.html'), ('Display que não tomba', 'guia-display-que-nao-tomba.html')],
 'resumo': 'Display para ração e petiscos pet junta duas lógicas: ração é compra planejada, recorrente e pesada, que pede peça de chão e prateleira calculada; petisco é impulso, que pede clip strip e display de balcão perto do caixa. No pet shop a peça também precisa explicar o produto, e o material deve ser lavável, porque ração solta gordura e pó.',
 'secoes': [
  {'h2': 'O que muda no PDV de ração e petiscos', 'blocos': [
   {'p': 'Ração é comprada de forma recorrente e com fidelidade: o tutor costuma repetir a marca que deu certo e só troca por recomendação, por um problema ou por uma oferta forte. Por isso o PDV de ração trabalha lançamento, troca de embalagem, experimentação e preço, mais do que impulso.'},
   {'p': 'O canal muda muito a peça. O pet shop especializado tem atendimento e espaço para ponto de experiência, e o display pode explicar fase de vida, porte e benefício. O supermercado e o atacarejo pedem leitura rápida, reposição de saco grande e preço visível. A agropecuária e a clínica veterinária têm espaço curto e público próprio.'},
   {'p': 'Petisco, sachê e brinquedo são outra história: impulso, item pequeno e ponto perto do caixa ou do corredor de ração.'}]},
  {'h2': 'Peças que funcionam e onde ficam', 'blocos': [
   {'tabela': {'cab': ['Peça', 'Onde fica', 'Quando usar'], 'linhas': [
    ['Display de chão ou base para saco grande', 'Corredor pet, ponta de gôndola, salão do atacarejo', 'Saco grande de ração, com o produto apoiado no chão'],
    ['Ponta de gôndola', 'Cabeceira do corredor pet', 'Lançamento, troca de embalagem e promoção'],
    ['Ilha ou ponto de experiência', 'Salão do pet shop', 'Linha completa, com informação por fase de vida e porte'],
    ['Clip strip', 'Corredor de ração ou perto do caixa', 'Petisco em embalagem com furo, em cross merchandising'],
    ['Display de balcão', 'Checkout do pet shop e da clínica', 'Petisco, sachê e item pequeno de impulso'],
    ['Cesto', 'Frente da ponta ou área de promoção', 'Sachê e brinquedo em volume']]}}]},
  {'h2': 'Material indicado e por quê', 'blocos': [
   {'p': 'Para saco de ração, metal pintado e arame soldado são os mais seguros: carregam muito e aceitam limpeza. Prateleira de MDF serve para embalagem pequena, com conta de flecha e fluência e acabamento que proteja a chapa da gordura.'},
   {'p': 'Ração e petisco soltam gordura e pó, que mancham papelão e acabamento poroso. Em peça de meses, prefira superfície lavável, como metal com pintura, PS, PETG ou MDF revestido. Papelão segue bom para ação curta de petisco. O ' + GUIA_MAT + ' compara os materiais.'}]},
  {'h2': 'Carga e estabilidade: os cuidados de projeto', 'blocos': [
   {'p': 'Exemplo ilustrativo: uma prateleira com 6 sacos de 3 kg soma 18 kg, ou perto de 21,6 kg com os 20% de folga que usamos como regra de projeto. Saco grande, de 10 kg ou mais, quase sempre vai melhor apoiado no chão ou em base baixa do que em prateleira. Use o peso da ficha técnica de cada embalagem.'},
   {'lista': [
    '**Peso embaixo:** saco grande no chão, embalagem pequena e petisco no alto.',
    '**Saco escorrega:** borda frontal alta ou batente, porque o saco deforma e desliza para fora.',
    '**Areia higiênica:** também é carga alta; trate como ração no projeto.',
    '**Flecha e fluência:** prateleira à vista no limite L/300, com fluência somada em MDF. A ' + CALC + ' faz a conta.',
    '**Tombamento:** confira o pior caso de reposição. Veja ' + GUIA_TOMBA + '.',
    '**Petisco pendurado:** carga por gancho com peso real, como no ' + CLIP + '.']}]},
  {'h2': 'Datas e momentos fortes', 'blocos': [
   {'p': 'O pet tem menos datas que alimentos e bebidas, e os grandes motivos de PDV são lançamento de linha, troca de embalagem e campanha de experimentação. Mesmo assim, alguns momentos se repetem:'},
   {'lista': [
    '**Outubro:** o Dia Mundial dos Animais, em 4 de outubro, é usado por redes e marcas em ações.',
    '**Natal:** petisco e brinquedo para presente, perto do caixa.',
    '**Verão:** mais procura por cuidado com pulgas e carrapatos, que pode puxar cross merchandising com ração e petisco.',
    '**Black Friday:** promoção de saco grande, na loja e no e-commerce.']}]},
  {'h2': 'Checklist rápido', 'blocos': [
   {'lista': [
    'Peso real de cada embalagem, com 20% de folga.',
    'Saco grande no chão e batente nas prateleiras.',
    'Material lavável em peça de meses.',
    'Versão para pet shop e versão para supermercado, se o canal pedir.',
    'Reposição combinada para não deixar o ponto vazio.',
    'Instalação registrada loja a loja. Veja ' + RAST + '.']}]}],
 'faq': [
  {'q': 'Qual o melhor display para saco de ração?', 'a': 'Base ou display de chão em metal ou arame, com o saco grande apoiado no chão e embalagens menores no alto. Prateleira de MDF só para embalagem pequena, com conta de flecha e fluência.'},
  {'q': 'Onde colocar petisco no pet shop?', 'a': 'Perto do caixa, em display de balcão, e no corredor de ração, em clip strip. Petisco é compra por impulso e funciona onde o tutor já está decidindo a compra.'},
  {'q': 'Display pet precisa ser diferente para pet shop e supermercado?', 'a': 'Muitas vezes sim. O pet shop tem atendimento e espaço para explicar o produto; o supermercado pede leitura rápida, preço visível e reposição fácil de saco grande. Um projeto modular atende os dois com a mesma base.'}],
})

# 7 ---------------------------------------------------------------------------
PAGINAS.append({
 'slug': 'display-para-cosmeticos-e-maquiagem',
 'cat': 'cosméticos e maquiagem', 'curto': 'Display para cosméticos e maquiagem',
 'titulo': 'Display para cosméticos e maquiagem · 75 LAB',
 'descricao': 'Como expor cosméticos e maquiagem no PDV: display com testador, expositor de parede, display de checkout, material, acabamento, antifurto, iluminação e checklist.',
 'h1': 'Display de PDV para **cosméticos** e maquiagem.',
 'lead': 'Cosmético é escolhido experimentando, vale muito em pouco espaço e é a marca na mão do shopper. O display precisa de testador, luz, acabamento e antifurto.',
 'k': 'Beleza', 'card': 'Testador, espelho, luz, acabamento e antifurto em uma peça leve e de alto valor por item.',
 'segmento': ('PDV para beleza e moda', 'pdv-para-beleza-e-moda.html'),
 'guias': [('Material do display', 'guia-material-display-pdv.html'), ('Enxoval de PDV', 'guia-o-que-e-enxoval-de-pdv.html')],
 'resumo': 'Display para cosméticos e maquiagem é decidido mais por experimentação, acabamento e antifurto do que por carga. Funcionam display de balcão com testador e espelho, expositor de parede com testeira, ilha de maquiagem, ponta de gôndola em farmácia e display de checkout para itens pequenos. Acrílico, PETG e MDF laqueado são os materiais mais usados, com luz de cor fiel.',
 'secoes': [
  {'h2': 'O que muda no PDV de cosméticos e maquiagem', 'blocos': [
   {'p': 'Maquiagem é escolhida por cor, tom e textura, e a decisão quase sempre passa por experimentar. Por isso o testador, o espelho e a luz fazem parte do display, e não são acessórios. Dermocosmético e cuidado com a pele pedem informação: tipo de pele, uso e benefício.'},
   {'p': 'Os canais são farmácia, perfumaria, loja de departamento, supermercado, franquia e loja multimarca. Em cada um muda o espaço, a altura do balcão e o padrão visual da rede. O mesmo produto pode precisar de versão de balcão, de parede e de ponta, todas com a mesma identidade.'},
   {'p': 'Item pequeno e de alto valor também é alvo de furto, e isso entra no desenho desde o briefing.'}]},
  {'h2': 'Peças que funcionam e onde ficam', 'blocos': [
   {'tabela': {'cab': ['Peça', 'Onde fica', 'Quando usar'], 'linhas': [
    ['Display de balcão com testador', 'Balcão de farmácia, perfumaria e loja', 'Lançamento e linha de maquiagem com experimentação'],
    ['Expositor de parede com testeira', 'Parede de beleza de farmácia e loja de departamento', 'Linha completa organizada por tom e família'],
    ['Ilha de maquiagem', 'Salão de loja de departamento e perfumaria', 'Marca com espaço próprio e atendimento'],
    ['Ponta de gôndola', 'Corredor de beleza em farmácia e supermercado', 'Promoção, kit e data comemorativa'],
    ['Display de checkout', 'Caixa da farmácia e da loja', 'Batom, lápis, esmalte e item pequeno de impulso'],
    ['Totem ou display de chão', 'Entrada da loja e corredor', 'Lançamento com comunicação forte']]}}]},
  {'h2': 'Material indicado e por quê', 'blocos': [
   {'p': 'Acrílico, PETG e PS entram onde o acabamento pesa: vitrine, porta-preço, testeira, nicho de testador. MDF laqueado ou revestido dá corpo e cor de marca, e metal com pintura resolve estrutura de parede e de ilha. A peça é leve, então a decisão vem de acabamento, durabilidade e limpeza.'},
   {'p': 'Dois cuidados técnicos: acrílico extrudado trinca em furo perto da borda, então mantenha pelo menos 2 vezes a espessura, e PS fino não segura rosca, então use rebite com arruela, encaixe ou fita dupla-face estrutural. O ' + GUIA_MAT + ' detalha.'}]},
  {'h2': 'Testador, luz e antifurto: os cuidados de projeto', 'blocos': [
   {'lista': [
    '**Testador separado do estoque:** nicho próprio para o testador, longe do produto lacrado, com lugar para lenço e descarte.',
    '**Limpeza:** superfície que aceita álcool e pano sem manchar; maquiagem e base sujam tudo em volta do testador.',
    '**Luz de cor fiel:** LED com boa reprodução de cor, para o tom no rosto bater com o tom na embalagem.',
    '**Espelho:** na altura do rosto, com o shopper em pé.',
    '**Antifurto:** compartimento com tampa ou trava, empurrador que mostra uma unidade por vez, produto cenográfico com estoque no atendimento, ou o sistema que a rede já usa.',
    '**Planograma por tom:** a grade de cores precisa caber na peça e ser fácil de repor sem trocar posição.',
    '**Comunicação:** o que a arte diz sobre benefício precisa bater com o que está aprovado para o produto. Passe a arte pelo regulatório da empresa.']}]},
  {'h2': 'Datas fortes do ano', 'blocos': [
   {'lista': [
    '**Dia das Mães:** kits e embalagens para presente, a data mais forte de beleza.',
    '**Dia dos Namorados:** perfumaria e kits.',
    '**Black Friday:** promoção em ponta e checkout.',
    '**Natal:** kits, embalagem especial e ilha de presentes.',
    '**Verão:** cuidado com a pele e produtos de sol na farmácia.']}]},
  {'h2': 'Checklist rápido', 'blocos': [
   {'lista': [
    'Testador, espelho e luz previstos no desenho, não depois.',
    'Estratégia de antifurto definida com a rede.',
    'Material com acabamento de marca e fácil de limpar.',
    'Versões para balcão, parede e ponta com a mesma identidade. Veja ' + ENX + '.',
    'Arte conferida pelo regulatório.',
    'Instalação registrada loja a loja. Veja ' + RAST + '.']}]}],
 'faq': [
  {'q': 'Qual material usar em display de maquiagem?', 'a': 'Acrílico, PETG e PS para vitrine, testeira e nicho de testador; MDF laqueado ou revestido para corpo e cor de marca; metal para estrutura de parede e ilha. A carga é baixa, então acabamento e limpeza decidem.'},
  {'q': 'Como organizar o testador no display de cosméticos?', 'a': 'Em nicho próprio, separado do estoque lacrado, com espelho na altura do rosto, luz de cor fiel e lugar para lenço e descarte. A superfície precisa aceitar limpeza frequente sem manchar.'},
  {'q': 'Como reduzir furto em display de cosméticos?', 'a': 'Com compartimento com tampa ou trava, empurrador que libera uma unidade por vez, produto cenográfico com estoque no atendimento, ou o sistema antifurto da rede. A escolha muda o desenho e precisa estar no briefing.'}],
})

# 8 ---------------------------------------------------------------------------
PAGINAS.append({
 'slug': 'display-para-higiene-e-cuidados-pessoais',
 'cat': 'higiene e cuidados pessoais', 'curto': 'Display para higiene e cuidados pessoais',
 'titulo': 'Display para higiene e cuidados pessoais · 75 LAB',
 'descricao': 'Como expor higiene pessoal no PDV: ponta de gôndola, clip strip em cross merchandising, ilha de volume, gancheira com trava, material, carga de frascos e checklist.',
 'h1': 'Display de PDV para **higiene** e cuidados pessoais.',
 'lead': 'Higiene é compra recorrente, sensível a preço e cheia de complementos. O display trabalha promoção, kit e cross merchandising, com frasco pesado e pacote volumoso.',
 'k': 'Higiene', 'card': 'Ponta de promoção, kit, cross merchandising e a diferença entre frasco pesado e pacote volumoso.',
 'segmento': ('PDV para farmácia', 'pdv-para-farma.html'),
 'guias': [('Guia de clip strip', 'guia-clip-strip.html'), ('Guia de ponta de gôndola', 'guia-ponta-de-gondola.html')],
 'resumo': 'Display para higiene e cuidados pessoais trabalha compra recorrente e sensível a preço: promoção, kit, lançamento e cross merchandising. Funcionam ponta de gôndola, display de chão para lançamento, clip strip de escova perto do creme dental, gancheira com trava para lâmina, ilha de volume para papel higiênico e fralda e display de checkout na farmácia. Frasco cheio pesa; pacote grande ocupa espaço.',
 'secoes': [
  {'h2': 'O que muda no PDV de higiene e cuidados pessoais', 'blocos': [
   {'p': 'Sabonete, shampoo, desodorante, creme dental, absorvente, fralda, papel higiênico e barbeador são comprados com frequência e com lista. A troca de marca acontece por promoção, por lançamento e por indicação, e o PDV é o lugar onde isso se decide.'},
   {'p': 'Os canais são supermercado, atacarejo, farmácia e conveniência. No atacarejo, papel higiênico e fralda vão em volume. Na farmácia, a categoria divide espaço com dermocosmético e o checkout vende item pequeno e de viagem. Na conveniência, o que vende é o item de emergência.'},
   {'p': 'É a categoria com mais complementos naturais: escova e creme dental, lâmina e espuma, shampoo e condicionador. Isso faz do cross merchandising e do kit dois caminhos fortes.'}]},
  {'h2': 'Peças que funcionam e onde ficam', 'blocos': [
   {'tabela': {'cab': ['Peça', 'Onde fica', 'Quando usar'], 'linhas': [
    ['Ponta de gôndola', 'Cabeceira do corredor de higiene', 'Promoção de leve mais pague menos, kit e lançamento'],
    ['Display de chão', 'Corredor ou entrada da loja', 'Lançamento e ação de algumas semanas'],
    ['Clip strip', 'Gôndola de creme dental, de shampoo ou do caixa', 'Escova, fio dental e item pequeno em cross merchandising'],
    ['Gancheira com trava', 'Corredor de barbear', 'Lâmina e barbeador, itens pequenos de alto valor'],
    ['Ilha de volume', 'Salão do atacarejo e do supermercado', 'Papel higiênico e fralda em pacote grande'],
    ['Display de checkout', 'Caixa da farmácia e da conveniência', 'Tamanho de viagem e item de emergência']]}}]},
  {'h2': 'Material indicado e por quê', 'blocos': [
   {'p': 'Para promoção de semanas, papelão ondulado resolve bem e aceita impressão forte. Para peça de meses, metal e arame carregam frascos sem problema, e PS ou PETG fazem testeira e porta-preço. Gancheira com trava é peça metálica.'},
   {'p': 'Frasco que vaza mancha papelão e incha MDF sem revestimento, então em peça longa prefira superfície lavável. O ' + GUIA_MAT + ' compara as opções.'}]},
  {'h2': 'Peso, volume e furto: os cuidados de projeto', 'blocos': [
   {'p': 'Exemplo ilustrativo: um frasco de shampoo de 400 ml pesa por volta de 0,45 kg. Um nível com 8 frentes e 4 frascos na profundidade soma cerca de 14,4 kg, ou perto de 17,3 kg com os 20% de folga que usamos como regra de projeto. Já o papel higiênico e a fralda são o contrário: leves e muito volumosos, e o projeto se decide por altura e profundidade.'},
   {'lista': [
    '**Frasco pesado:** prateleira à vista no limite L/300, com fluência somada em MDF. A ' + CALC + ' faz a conta.',
    '**Pacote volumoso:** meça o pacote real e deixe a peça como moldura; o pacote empilhado faz o volume.',
    '**Lâmina e barbeador:** gancho com trava, empurrador ou o sistema antifurto da rede.',
    '**Aerossol:** desodorante em aerossol fica longe de luminária quente e de fonte de calor, como a própria embalagem orienta.',
    '**Tombamento:** display de chão leve tomba fácil com o nível de cima cheio. Veja ' + GUIA_TOMBA + '.',
    '**Gancho:** carga por gancho com peso real no clip strip, como no ' + CLIP + '.']}]},
  {'h2': 'Datas fortes do ano', 'blocos': [
   {'lista': [
    '**Dia dos Pais:** barbear e kits masculinos.',
    '**Dia das Mães e Natal:** kits para presente na ponta e na ilha.',
    '**Volta às aulas:** escova e creme dental infantil.',
    '**Verão:** desodorante e cuidados de banho.']}]},
  {'h2': 'Checklist rápido', 'blocos': [
   {'lista': [
    'Peso real dos frascos, com 20% de folga.',
    'Volume real dos pacotes grandes medido.',
    'Par de cross merchandising escolhido e negociado com a rede.',
    'Antifurto definido para lâmina e item de alto valor.',
    'Superfície lavável em peça de meses.',
    'Instalação registrada loja a loja. Veja ' + RAST + '.']}]}],
 'faq': [
  {'q': 'Qual display usar para promoção de higiene pessoal?', 'a': 'Ponta de gôndola para promoção e kit, display de chão para lançamento e clip strip para o complemento, como escova perto do creme dental. A peça depende do espaço que a rede libera e do tempo da ação.'},
  {'q': 'Como expor lâmina de barbear sem furto?', 'a': 'Em gancheira com trava, com empurrador que libera uma unidade por vez, ou com o sistema antifurto que a rede já usa. Isso precisa entrar no briefing, porque muda a peça.'},
  {'q': 'Como expor papel higiênico e fralda em volume?', 'a': 'Em ilha ou pilha com moldura de comunicação, deixando o pacote empilhado fazer o volume. O projeto se decide pela medida real do pacote, pela altura de pilha e pela leitura de preço.'}],
})

# 9 ---------------------------------------------------------------------------
PAGINAS.append({
 'slug': 'display-para-mip-e-suplementos',
 'cat': 'MIP e suplementos', 'curto': 'Display para MIP e suplementos',
 'titulo': 'Display para MIP e suplementos na farmácia · 75 LAB',
 'descricao': 'Como expor medicamentos isentos de prescrição e suplementos no PDV: display de balcão, gancheira para blister, ilha modular, regras de exposição, validade e checklist.',
 'h1': 'Display de PDV para **MIP** e suplementos.',
 'lead': 'Medicamento isento de prescrição e suplemento vendem em espaço curto, com regras de exposição e comunicação. O display precisa ser compacto, organizado e conferido antes de produzir.',
 'k': 'Farma', 'card': 'Balcão, gancheira para blister, ilha modular e as regras de exposição que a farmácia pede.',
 'segmento': ('PDV para farmácia', 'pdv-para-farma.html'),
 'guias': [('Briefing de display', 'guia-briefing-display-pdv.html'), ('Guia de clip strip', 'guia-clip-strip.html')],
 'resumo': 'Display para medicamentos isentos de prescrição (MIP) e suplementos vive em espaço curto e com regras: o que pode ficar ao alcance do cliente, como organizar e o que a peça pode dizer seguem a regra sanitária e a regra da rede, que precisam ser conferidas antes do projeto. Funcionam display de balcão compacto, gancheira para blister, testeira de categoria, ilha modular multimarca e display de chão para suplemento em pote.',
 'secoes': [
  {'h2': 'O que muda no PDV de MIP e suplementos', 'blocos': [
   {'p': 'O MIP é vendido em farmácia e drogaria, e a compra mistura necessidade imediata, como dor e gripe, com reposição de itens de uso frequente. Em muitas farmácias o MIP fica em gôndola de autosserviço, mas o que pode ficar ao alcance do cliente, como organizar e o que a comunicação pode dizer seguem regras sanitárias. Confira a regra da rede e da vigilância sanitária antes de desenhar a peça.'},
   {'p': 'O suplemento alimentar vende em farmácia, loja de suplementos, supermercado, academia e e-commerce. Não é medicamento, e a comunicação não pode prometer tratamento ou cura; o texto da arte deve passar pelo regulatório da empresa.'},
   {'p': 'Nos dois casos, o espaço é curto e disputado: balcão, checkout e gôndola com muitas marcas. A peça precisa ser compacta, fácil de repor e organizada por necessidade.'}]},
  {'h2': 'Peças que funcionam e onde ficam', 'blocos': [
   {'tabela': {'cab': ['Peça', 'Onde fica', 'Quando usar'], 'linhas': [
    ['Display de balcão', 'Balcão de atendimento e checkout', 'Itens permitidos pela regra da rede, em espaço curto'],
    ['Gancheira para blister', 'Gôndola de autosserviço', 'Produto em blister ou cartela com furo'],
    ['Prateleira com divisória e testeira', 'Gôndola de autosserviço', 'Frasco e caixa organizados por necessidade, com comunicação de categoria'],
    ['Ilha modular multimarca', 'Salão da farmácia', 'Várias marcas na mesma estrutura, trocando só a comunicação'],
    ['Display de chão', 'Corredor e entrada', 'Suplemento em pote e lançamento'],
    ['Clip strip', 'Gôndola ou checkout', 'Sachê e item leve em embalagem com furo']]}}]},
  {'h2': 'Material indicado e por quê', 'blocos': [
   {'p': 'Acrílico, PETG e PS são os mais usados em farmácia: acabamento limpo, leveza e boa aparência em balcão. Metal resolve gancheira e estrutura de ilha. MDF revestido dá corpo à ilha e ao display de chão. Papelão serve para ação curta de suplemento ou de sazonalidade.'},
   {'p': 'Um projeto modular costuma valer a pena na farmácia: a mesma estrutura atende marcas e campanhas diferentes trocando só a comunicação. O ' + GUIA_MAT + ' compara os materiais.'}]},
  {'h2': 'Organização, validade e carga: os cuidados de projeto', 'blocos': [
   {'lista': [
    '**Regra antes do desenho:** confirme com a rede e com a vigilância sanitária o que pode ficar ao alcance do cliente, onde a peça pode ficar e o que a arte pode dizer. Registre isso no ' + BRIEF + '.',
    '**Ferragem pelo produto:** frasco e caixa em prateleira, blister em gancho.',
    '**Validade:** a peça precisa permitir vender primeiro o lote que vence antes; rampa ou reposição por trás ajudam.',
    '**Balcão:** peça compacta que não atrapalhe o atendimento nem cubra a visão do balconista.',
    '**Suplemento em pote:** é mais pesado do que parece. Exemplo ilustrativo: 6 potes de 900 g somam pelo menos 5,4 kg só de produto, perto de 6,5 kg com os 20% de folga que usamos como regra de projeto. Use o peso da ficha técnica.',
    '**Estabilidade:** display de chão leve precisa de base ou lastro. Veja ' + GUIA_TOMBA + '.']}]},
  {'h2': 'Datas e momentos fortes', 'blocos': [
   {'lista': [
    '**Outono e inverno:** gripe e resfriado, com ponto extra para as categorias ligadas à estação.',
    '**Começo de ano e pré-verão:** suplemento esportivo e de rotina.',
    '**Verão:** hidratação e cuidados ligados ao calor.',
    '**Volta às aulas:** vitaminas e itens de rotina da família.']}]},
  {'h2': 'Checklist rápido', 'blocos': [
   {'lista': [
    'Regra de exposição e comunicação confirmada com a rede e a vigilância sanitária.',
    'Arte aprovada pelo regulatório da empresa.',
    'Ferragem escolhida pelo tipo de embalagem.',
    'Reposição que respeite a validade.',
    'Peso real dos potes e frascos, com 20% de folga.',
    'Instalação registrada loja a loja. Veja ' + RAST + '.']}]}],
 'faq': [
  {'q': 'MIP pode ficar em display de autosserviço na farmácia?', 'a': 'Em muitas farmácias o MIP fica em gôndola de autosserviço, mas o que pode ficar ao alcance do cliente, como organizar e o que a peça pode comunicar seguem regras sanitárias. Confira a regra da rede e da vigilância sanitária antes de desenhar o display.'},
  {'q': 'Qual display usar para blister?', 'a': 'Gancheira na gôndola, com ganchos compatíveis com o furo da embalagem e carga por gancho calculada. Frasco e caixa vão melhor em prateleira com divisória.'},
  {'q': 'O que o display de suplemento pode dizer?', 'a': 'Suplemento alimentar não é medicamento, e a comunicação não pode prometer tratamento ou cura. O texto da peça deve ser aprovado pelo regulatório da empresa antes da produção.'},
  {'q': 'Vale a pena display modular em farmácia?', 'a': 'Costuma valer, porque o espaço é curto e as campanhas mudam rápido. A mesma estrutura atende marcas e ações diferentes trocando só a comunicação.'}],
})

# 10 --------------------------------------------------------------------------
PAGINAS.append({
 'slug': 'display-para-pilhas-e-acessorios-eletronicos',
 'cat': 'pilhas e acessórios eletrônicos', 'curto': 'Display para pilhas e acessórios eletrônicos',
 'titulo': 'Display para pilhas e acessórios eletrônicos · 75 LAB',
 'descricao': 'Como expor pilhas, cabos, fones e acessórios no PDV: clip strip, display de checkout, gancheira com trava, cross merchandising com brinquedo, carga por gancho e checklist.',
 'h1': 'Display de PDV para **pilhas** e acessórios eletrônicos.',
 'lead': 'Pilha é compra de necessidade e de impulso; cabo e fone são item pequeno de valor alto. O display vive de gancho, checkout e antifurto.',
 'k': 'Eletro', 'card': 'Clip strip, checkout, gancheira com trava e a carga que a pilha, pequena e densa, põe no gancho.',
 'segmento': ('PDV para eletro', 'pdv-para-eletro.html'),
 'guias': [('Guia de clip strip', 'guia-clip-strip.html'), ('Display que não tomba', 'guia-display-que-nao-tomba.html')],
 'resumo': 'Display para pilhas e acessórios eletrônicos trabalha impulso, necessidade e furto. Funcionam clip strip e display de balcão no checkout, gancheira com trava para cabo e fone, display de chão em ponto extra e cross merchandising com brinquedo, controle remoto e lanterna. A pilha é pequena e densa: a carga por gancho surpreende e precisa de conta.',
 'secoes': [
  {'h2': 'O que muda no PDV de pilhas e acessórios', 'blocos': [
   {'p': 'Pilha é lembrada quando falta: no controle remoto, no brinquedo, na balança. Por isso vende muito no checkout e em cross merchandising, perto do produto que precisa dela. Cabos, carregadores e fones têm compra de necessidade, quando o antigo quebra, e de impulso, perto do caixa.'},
   {'p': 'Os canais são supermercado, farmácia, conveniência, loja de eletro, papelaria, bazar e home center. Em todos, o item é pequeno e de valor alto para o tamanho, o que coloca o furto no centro do projeto.'}]},
  {'h2': 'Peças que funcionam e onde ficam', 'blocos': [
   {'tabela': {'cab': ['Peça', 'Onde fica', 'Quando usar'], 'linhas': [
    ['Clip strip', 'Corredor de brinquedos, de eletro e perto do caixa', 'Cartela de pilha em cross merchandising'],
    ['Display de balcão', 'Checkout do supermercado, farmácia e conveniência', 'Pilha e acessório de impulso'],
    ['Gancheira com trava', 'Corredor de eletro e de acessórios', 'Cabo, fone e carregador de valor alto'],
    ['Display de chão ou torre', 'Ponto extra no corredor ou na entrada', 'Lançamento e linha completa de acessórios'],
    ['Expositor de parede', 'Loja de eletro e home center', 'Linha completa organizada por tipo de conexão ou uso'],
    ['Coletor de pilhas usadas', 'Entrada da loja ou perto do checkout', 'Ponto de coleta, conforme a regra vigente']]}}]},
  {'h2': 'Material indicado e por quê', 'blocos': [
   {'p': 'Gancheira, clip strip de carga maior e display de checkout costumam ser de metal ou arame, porque o gancho carrega peso concentrado e precisa de rigidez. PS, PETG e acrílico fazem testeira, porta-preço e o corpo do display de balcão. Papelão funciona em ação curta, desde que o gancho não seja preso direto nele.'},
   {'p': 'Plástico fino não segura rosca, então gancho preso em PS ou PVC expandido pede rebite com arruela ou encaixe. O ' + GUIA_MAT + ' compara as opções.'}]},
  {'h2': 'Carga por gancho e antifurto: os cuidados de projeto', 'blocos': [
   {'p': 'Exemplo ilustrativo: uma cartela com 4 pilhas AA pesa por volta de 100 g. Um clip strip com 8 ganchos e 5 cartelas por gancho carrega 4 kg mais o peso da tira; com os 20% de folga que usamos como regra de projeto, passa de 4,8 kg. É bastante para uma tira presa na régua de preço, e é por isso que o ' + CLIP + ' manda conferir o ponto de fixação.'},
   {'lista': [
    '**Ponto de fixação:** a carga total puxa a régua ou a prateleira para baixo e para fora; quando a conta dá alta, divida em duas tiras.',
    '**Gancho com trava:** cabo, fone e carregador de valor alto em gancho com trava ou com empurrador que libera uma unidade por vez.',
    '**Produto cenográfico:** em item muito caro, embalagem vazia na exposição e estoque no caixa.',
    '**Organização:** separar por tipo de conexão e por uso reduz a dúvida e a devolução.',
    '**Estabilidade:** torre de acessórios é alta e leve; confira o tombamento. Veja ' + GUIA_TOMBA + '.',
    '**Coletor de pilhas:** se a peça incluir ponto de coleta, confira a regra ambiental vigente e combine quem faz a destinação.']}]},
  {'h2': 'Datas fortes do ano', 'blocos': [
   {'lista': [
    '**Dia das Crianças e Natal:** pilha em cross merchandising com brinquedo, as datas mais fortes da categoria.',
    '**Black Friday:** acessórios e carregadores em promoção, perto dos aparelhos.',
    '**Volta às aulas:** fones, cabos e pilhas para itens escolares.',
    '**Férias:** carregador portátil e cabo para viagem.']}]},
  {'h2': 'Checklist rápido', 'blocos': [
   {'lista': [
    'Peso real da cartela e carga por gancho calculada, com 20% de folga.',
    'Ponto de fixação conferido em cada rede.',
    'Antifurto definido para item de valor alto.',
    'Ponto de cross merchandising negociado com a rede.',
    'Regra do coletor confirmada, se houver.',
    'Instalação registrada loja a loja. Veja ' + RAST + '.']}]}],
 'faq': [
  {'q': 'Qual o melhor display para pilhas?', 'a': 'Clip strip em cross merchandising, perto de brinquedo e eletro, e display de balcão no checkout. A pilha é pequena e densa, então a carga por gancho precisa de conta.'},
  {'q': 'Quanto peso aguenta um clip strip de pilhas?', 'a': 'Depende do material da tira e do ponto de fixação. A conta é o peso real da cartela vezes cartelas por gancho vezes ganchos, mais o peso da tira e 20% de folga. Se a carga ficar alta, divida em duas tiras mais curtas.'},
  {'q': 'Como expor fone e cabo sem furto?', 'a': 'Em gancheira com trava, com empurrador que libera uma unidade por vez, ou com embalagem cenográfica na exposição e estoque no caixa. A escolha precisa entrar no briefing, porque muda a peça.'}],
})
