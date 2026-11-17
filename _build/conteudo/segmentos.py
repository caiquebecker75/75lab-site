"""Páginas por segmento. Só clientes que já estão no portfólio público (cases.html) e os 4 cases
liberados. Nada de número inventado, nunca Pokémon, nunca travessão."""

AR = 'https://projetos.75lab.com.br/ar/'
SOL = ('Soluções', '/solucoes.html')


def g(n, leg):
    return {'img': f'img/g{n:02d}-1.jpg', 'leg': leg, 'href': 'cases.html'}


REL = [('Display de PDV', 'display-de-pdv.html'), ('Enxoval e material de PDV', 'enxoval-de-pdv.html'),
       ('Realidade aumentada para PDV', 'realidade-aumentada-pdv.html'), ('Rastreamento de material de PDV', 'rastreamento-material-pdv.html'),
       ('Guias de PDV', 'guias.html')]

COMO = {'h2': 'Como a 75 LAB trabalha', 'blocos': [{'passos': [
    '**Imersão** no produto, no canal e na loja, com o peso e as medidas reais das embalagens.',
    '**Projeto e engenharia**, com carga por prateleira e estabilidade conferidas no executivo técnico.',
    '**Aprovação em realidade aumentada**, com a peça em tamanho real na gôndola antes de produzir.',
    '**Produção** com fornecedores homologados e **rastreio por QR** depois de instalada.']}]}

PAGINAS = [
 {
  'slug': 'pdv-para-alimentos', 'servico': 'Material de PDV para indústria de alimentos',
  'titulo_seo': 'Display e material de PDV para alimentos · 75 LAB',
  'descricao': 'Displays, pontas de gôndola, clip strips e enxovais de PDV para indústrias de alimentos, do seco ao refrigerado, com aprovação em AR e rastreio por QR.',
  'eyebrow': 'Alimentos', 'migalhas': [SOL, ('PDV para alimentos', None)],
  'h1': 'PDV para a indústria de **alimentos**.',
  'lead': 'Do corredor de seco à porta da geladeira: peças que aguentam o peso do produto, cabem no espaço negociado e chegam montadas.',
  'resumo': 'A 75 LAB cria e produz material de PDV para indústrias de alimentos: displays de chão e de balcão, pontas de gôndola sazonais, clip strips para cross merchandising e peças para a área refrigerada. Cada peça é aprovada em realidade aumentada antes de produzir e pode sair com QR para registrar onde foi montada.',
  'secoes': [
   {'h2': 'O que pesa no PDV de alimentos', 'blocos': [{'lista': [
     '**Peso e volume:** latas, vidros e caixas exigem prateleira calculada para não envergar com o tempo.',
     '**Sazonalidade:** Páscoa, festas juninas, Natal e Black Friday pedem ponto extra rápido de montar e de tirar.',
     '**Refrigerado:** régua, glorifier e comunicação de geladeira lidam com umidade, frio e pouco espaço.',
     '**Cross merchandising:** o clip strip leva o produto para perto de outra categoria e precisa aguentar a carga por gancho.']}]},
   COMO,
   {'h2': 'Alimentos que já passaram por aqui', 'blocos': [
     {'galeria': [{'img': 'img/cases/savencia-clipstrip.webp', 'leg': 'Savencia · clip strip Frescatino (AR)', 'href': 'case-savencia-frescatino.html'},
                  g(50, 'Seara · ponta de gôndola'), g(16, 'Polenghi · varejo e food'), g(39, 'Bem Brasil · ponta de gôndola'),
                  g(19, 'Cuétara · display sazonal'), g(46, 'Lactalis · displays especiais')]},
     {'p': 'Veja também os guias [clip strip](guia-clip-strip.html) e [ponta de gôndola](guia-ponta-de-gondola.html).'}]},
  ],
  'faq': [
   {'q': 'Qual material de display é melhor para alimentos?', 'a': 'Depende do tempo de exposição e do peso. Para campanha curta, papelão bem dimensionado costuma bastar; para ponto permanente ou produto pesado, metal, arame ou MDF com prateleira calculada. O [guia de materiais](guia-material-display-pdv.html) compara as opções.'},
   {'q': 'A 75 LAB faz peças para a área refrigerada?', 'a': 'Sim. Réguas, glorifiers e peças de porta de geladeira, como o glorifier Frescatino da Savencia, pensadas para umidade, frio e fixação na parede ou no equipamento.'},
   {'q': 'Dá para ver a ponta de gôndola no corredor antes de produzir?', 'a': 'Sim. A peça abre em realidade aumentada no celular, em tamanho real, para conferir altura, leitura e espaço.'},
  ],
  'relacionados': [('Ilha e ponta de gôndola', 'ilha-e-ponta-de-gondola.html'), ('Case Savencia', 'case-savencia-frescatino.html')] + REL,
 },
 {
  'slug': 'pdv-para-pet', 'servico': 'Material de PDV para indústria pet',
  'titulo_seo': 'Display e material de PDV para o mercado pet · 75 LAB',
  'descricao': 'Displays, pontos de experiência, enxovais e conteúdo rico para indústrias pet, do pet shop ao supermercado, com aprovação em AR e rastreio por QR.',
  'eyebrow': 'Pet', 'migalhas': [SOL, ('PDV para pet', None)],
  'h1': 'PDV para a indústria **pet**.',
  'lead': 'Saco de ração pesado, petisco de impulso e loja especializada com espaço disputado: cada formato pede uma peça diferente.',
  'resumo': 'A 75 LAB cria e produz PDV para indústrias pet: displays modulares, pontos de experiência em redes especializadas, enxovais de lançamento, clip strips de petisco e conteúdo rico para o e-commerce. A Kelco, por exemplo, tem displays, parede modular, ponto de experiência na Petz e ClickLab feitos pela 75 LAB.',
  'secoes': [
   {'h2': 'O que pesa no PDV pet', 'blocos': [{'lista': [
     '**Embalagens grandes e pesadas:** estrutura e prateleira precisam ser calculadas para o saco cheio, não para o render.',
     '**Pet shop x supermercado:** a loja especializada pede experiência e consultoria; o supermercado pede leitura rápida e reposição.',
     '**Petisco é impulso:** clip strip e display de balcão perto do caixa e do corredor de ração.',
     '**Online pesa muito:** a página de produto do e-commerce também é PDV.']}]},
   COMO,
   {'h2': 'Pet que já passou por aqui', 'blocos': [
     {'galeria': [g(43, 'Kelco · display modular'), g(52, 'Kelco · experiência Petz'), g(49, 'Kelco · parede modular'),
                  g(40, 'Petz · ponta de gôndola'), g(85, 'Kelco · Bifinhos'), g(81, 'Kelco · ClickLab Petz')]}]},
  ],
  'faq': [
   {'q': 'Como fazer display para ração pesada?', 'a': 'Com a carga real de cada nível no projeto: peso da embalagem vezes frentes e profundidade, com folga. A prateleira é conferida contra a flecha e o conjunto contra o tombamento, como explica o guia [display que não tomba](guia-display-que-nao-tomba.html).'},
   {'q': 'O que é um ponto de experiência em pet shop?', 'a': 'É um espaço fora do corredor, temático, onde o tutor conhece e experimenta a marca. Pede cenografia, comunicação da campanha e montagem simples para a equipe da loja.'},
   {'q': 'A 75 LAB faz conteúdo para e-commerce pet?', 'a': 'Sim. O [ClickLab](conteudo-rico-ecommerce.html) é o conteúdo rico da página de produto, com 3D, vídeo e simulação da loja do varejista.'},
  ],
  'relacionados': [('Conteúdo rico para e-commerce', 'conteudo-rico-ecommerce.html')] + REL,
 },
 {
  'slug': 'pdv-para-farma', 'servico': 'Material de PDV para farmácia e dermocosméticos',
  'titulo_seo': 'Display e material de PDV para farmácia · 75 LAB',
  'descricao': 'Displays de balcão, gôndola e ilhas modulares para indústrias que vendem em farmácia, com ferragem por produto, aprovação em AR e rastreio por QR.',
  'eyebrow': 'Farma', 'migalhas': [SOL, ('PDV para farmácia', None)],
  'h1': 'PDV para **farmácia**.',
  'lead': 'Loja pequena, balcão disputado e muitas marcas no mesmo metro: a peça certa é compacta, modular e fácil de repor.',
  'resumo': 'A 75 LAB cria e produz PDV para indústrias que vendem em farmácia: displays de balcão e de checkout, gôndola com prateleira ou gancheira conforme o produto e ilhas modulares multimarca. Para a NGV, um mesmo módulo de display atende quatro marcas e forma uma ilha de quatro faces.',
  'secoes': [
   {'h2': 'O que pesa no PDV de farmácia', 'blocos': [{'lista': [
     '**Espaço curto:** balcão e checkout pedem peça compacta que não atrapalhe o atendimento.',
     '**Produto define a ferragem:** frasco vai em prateleira, blister vai em gancho.',
     '**Muitas marcas, uma estrutura:** o display modular troca só a comunicação entre marcas e campanhas.',
     '**Regras de comunicação** de cada categoria precisam estar resolvidas na arte antes da produção.']}]},
   COMO,
   {'h2': 'Farma que já passou por aqui', 'blocos': [
     {'galeria': [{'img': 'img/cases/ngv-ilha.webp', 'leg': 'NGV · ilha de quatro marcas (AR)', 'href': 'case-ngv-display-universal.html'},
                  {'img': 'img/cases/ngv-vitalitabs.webp', 'leg': 'NGV · Vitalitabs', 'href': 'case-ngv-display-universal.html'},
                  {'img': 'img/cases/ngv-stand.webp', 'leg': 'NGV · estande Conexão Farma', 'href': 'case-ngv-display-universal.html'},
                  g(10, 'Pague Menos · institucional'), g(68, 'DPSP · inauguração de loja'), g(71, 'DPSP · lançamento hub')]}]},
  ],
  'faq': [
   {'q': 'Qual o melhor display para balcão de farmácia?', 'a': 'Um display compacto, estável e fácil de repor, com a ferragem certa para o produto. A medida é definida pelo balcão da rede, por isso vale aprovar a peça em AR no próprio balcão.'},
   {'q': 'Dá para usar o mesmo display para várias marcas?', 'a': 'Sim, quando ele nasce modular. A estrutura é a mesma e mudam a arte e a ferragem, como no Display Universal da NGV.'},
   {'q': 'Como saber em quais farmácias o display foi instalado?', 'a': 'Com QR na peça e página de montagem: quem instala registra loja, foto e localização, e a marca acompanha no painel.'},
  ],
  'relacionados': [('Case NGV', 'case-ngv-display-universal.html'), ('Ilha e ponta de gôndola', 'ilha-e-ponta-de-gondola.html')] + REL,
 },
 {
  'slug': 'pdv-para-beleza-e-moda', 'servico': 'Material de PDV para beleza e moda',
  'titulo_seo': 'Display e material de PDV para beleza e moda · 75 LAB',
  'descricao': 'Displays modulares, enxovais de loja e ativações para marcas de beleza e moda, com acabamento premium, aprovação em AR e rastreio por QR.',
  'eyebrow': 'Beleza e moda', 'migalhas': [SOL, ('PDV para beleza e moda', None)],
  'h1': 'PDV para **beleza e moda**.',
  'lead': 'Categoria em que a peça é parte da marca: acabamento, luz e experimentação contam tanto quanto a exposição.',
  'resumo': 'A 75 LAB cria e produz PDV para marcas de beleza e moda: displays modulares para franquia e multimarca, enxovais de loja, cestos promocionais e embalagens sazonais. O Boticário e a Loungerie têm displays modulares e enxovais feitos pela 75 LAB.',
  'secoes': [
   {'h2': 'O que pesa no PDV de beleza e moda', 'blocos': [{'lista': [
     '**Acabamento é marca:** material, cor e luz precisam bater com a identidade em toda loja.',
     '**Experimentação:** testers, espelhos e espaço para pegar o produto.',
     '**Franquia e multimarca:** a mesma peça precisa caber em lojas de tamanhos diferentes.',
     '**Datas fortes:** Dia das Mães, Dia dos Namorados e Natal pedem enxoval e embalagem especial.']}]},
   COMO,
   {'h2': 'Beleza e moda que já passaram por aqui', 'blocos': [
     {'galeria': [g(48, 'O Boticário · display modular'), g(41, 'Loungerie · display modular'), g(31, 'Loungerie · enxoval de loja'),
                  g(84, 'Loungerie · embalagem de Natal'), g(32, 'Loungerie · cesto promocional')]}]},
  ],
  'faq': [
   {'q': 'Como manter o mesmo padrão de PDV em franquias diferentes?', 'a': 'Com display modular e guia de implantação: a peça se adapta ao espaço de cada loja sem mudar a identidade, e a página de montagem mostra como deve ficar.'},
   {'q': 'Dá para ver o display na loja antes de produzir?', 'a': 'Sim. A peça abre em realidade aumentada, em tamanho real, para conferir medida, acabamento e leitura.'},
   {'q': 'A 75 LAB faz embalagem e enxoval sazonal?', 'a': 'Sim, como a embalagem de Natal e o enxoval de loja da Loungerie.'},
  ],
  'relacionados': REL,
 },
 {
  'slug': 'pdv-para-bebidas', 'servico': 'Material de PDV para bebidas',
  'titulo_seo': 'Display e material de PDV para bebidas · 75 LAB',
  'descricao': 'Displays, pontos extras e materiais de PDV para indústrias de bebidas, de vinho a café, com estabilidade calculada, aprovação em AR e rastreio por QR.',
  'eyebrow': 'Bebidas', 'migalhas': [SOL, ('PDV para bebidas', None)],
  'h1': 'PDV para **bebidas**.',
  'lead': 'Garrafa pesa, quebra e vende em data comemorativa. A peça precisa ser estável, segura e pronta para o pico.',
  'resumo': 'A 75 LAB cria e produz PDV para indústrias de bebidas e café: displays de ponto extra, materiais de foodservice, ações de campanha e peças de apoio à força de vendas. A estabilidade é conferida no projeto, porque garrafa cheia muda o centro de gravidade do display.',
  'secoes': [
   {'h2': 'O que pesa no PDV de bebidas', 'blocos': [{'lista': [
     '**Peso e quebra:** garrafa cheia exige base larga, prateleira calculada e conferência de tombamento.',
     '**Sazonalidade forte:** fim de ano e datas comemorativas concentram o sell-out em poucas semanas.',
     '**Foodservice:** bar, restaurante e cafeteria pedem peça robusta e fácil de montar.',
     '**Ponto extra:** a ilha e a ponta de gôndola disputam o mesmo espaço com outras categorias.']}]},
   COMO,
   {'h2': 'Bebidas que já passaram por aqui', 'blocos': [
     {'galeria': [g(11, '3 Corações · foodservice'), g(74, '3 Corações · uniforme'), g(21, 'Evino · corta gotas'), g(54, 'Vissimo · corta gotas')]},
     {'p': 'Para conferir estabilidade com garrafa, veja o guia [display que não tomba](guia-display-que-nao-tomba.html).'}]},
  ],
  'faq': [
   {'q': 'Como evitar que um display de garrafas tombe?', 'a': 'Calculando o centro de gravidade com o display cheio e no pior caso (nível de cima cheio, de baixo vazio), com base larga, lastro ou fixação quando preciso. O guia [display que não tomba](guia-display-que-nao-tomba.html) mostra a conta.'},
   {'q': 'A 75 LAB atende foodservice?', 'a': 'Sim. Materiais para bar, restaurante e cafeteria, como o projeto de foodservice da 3 Corações.'},
   {'q': 'Dá para rastrear o ponto extra nas lojas?', 'a': 'Sim, com QR na peça: o promotor registra loja, foto e localização ao montar.'},
  ],
  'relacionados': REL,
 },
 {
  'slug': 'pdv-para-eletro', 'servico': 'Material de PDV para eletro e linha branca',
  'titulo_seo': 'Display e enxoval de PDV para eletro e linha branca · 75 LAB',
  'descricao': 'Ilhas, pórticos, toppers e enxovais de PDV para eletro e linha branca, com o produto real em exposição, aprovação em AR e conteúdo rico para o e-commerce.',
  'eyebrow': 'Eletro', 'migalhas': [SOL, ('PDV para eletro', None)],
  'h1': 'PDV para **eletro e linha branca**.',
  'lead': 'Produto grande, decisão pesquisada e venda que começa no site: o PDV precisa explicar, demonstrar e continuar online.',
  'resumo': 'A 75 LAB cria e produz PDV para eletro e linha branca: ilhas com o produto real, pórticos, backdrops, toppers e placas de especificação, displays de varejo e conteúdo rico para a página do produto. A SEMP tem o enxoval do Split HW inteiro em realidade aumentada; Whirlpool, LG e Dako também estão no portfólio.',
  'secoes': [
   {'h2': 'O que pesa no PDV de eletro', 'blocos': [{'lista': [
     '**Produto grande e caro:** a exposição precisa ser segura, estável e bonita com o aparelho real.',
     '**Especificação vende:** placa de BTU, topper e orelha explicam o produto sem vendedor por perto.',
     '**Campanha nacional:** promoções e cashback pedem material em muitas lojas ao mesmo tempo.',
     '**Online e loja juntos:** a página do produto no marketplace continua a conversa do PDV.']}]},
   COMO,
   {'h2': 'Eletro que já passou por aqui', 'blocos': [
     {'galeria': [{'img': 'img/cases/semp-portico.webp', 'leg': 'SEMP · pórtico Split HW (AR)', 'href': 'case-semp-split-hw.html'},
                  {'img': 'img/cases/semp-ilha.webp', 'leg': 'SEMP · ilha premium (AR)', 'href': 'case-semp-split-hw.html'},
                  g(14, 'Whirlpool · lavadora BWD16'), g(35, 'Whirlpool · displays magazine'), g(9, 'LG · cashback'), g(38, 'Dako · display varejo')]}]},
  ],
  'faq': [
   {'q': 'Quais peças formam o enxoval de PDV de um eletrodoméstico?', 'a': 'Em geral pórtico ou backdrop, ilha ou berço para o produto, topper, orelha e placa de especificação aplicados no aparelho, régua, tapete e comunicação aérea. O enxoval do Split HW da SEMP tem 15 peças.'},
   {'q': 'Dá para ver o enxoval inteiro em realidade aumentada?', 'a': 'Sim. No case SEMP, as 15 peças ficam numa página de AR, uma a uma, todas juntas ou em tamanho real.'},
   {'q': 'A 75 LAB faz o conteúdo da página do produto no e-commerce?', 'a': 'Sim, com o [ClickLab](conteudo-rico-ecommerce.html), como fizemos para Whirlpool e SEMP.'},
  ],
  'relacionados': [('Case SEMP Split HW', 'case-semp-split-hw.html'), ('Conteúdo rico para e-commerce', 'conteudo-rico-ecommerce.html')] + REL,
 },
]
