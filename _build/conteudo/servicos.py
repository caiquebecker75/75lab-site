"""Conteúdo das páginas de serviço. Regras: só fatos que a 75 LAB pode provar, nenhum número
inventado, nenhum cliente fora da lista liberada nos textos novos (Savencia, NGV, SEMP, Alltak),
nunca citar a Pokémon, nunca usar travessão. Os cards gNN usam as fotos que já estão em cases.html."""

AR = 'https://projetos.75lab.com.br/ar/'
SOL = ('Soluções', '/solucoes.html')
REL_PADRAO = [('Realidade aumentada para PDV', 'realidade-aumentada-pdv.html'),
              ('Rastreamento de material de PDV', 'rastreamento-material-pdv.html'),
              ('Cases detalhados', 'cases.html#detalhados'), ('Guias de PDV', 'guias.html')]


def g(n, leg):
    return {'img': f'img/g{n:02d}-1.jpg', 'leg': leg, 'href': 'cases.html'}


PAGINAS = [
 {
  'slug': 'display-de-pdv', 'servico': 'Projeto e produção de display de PDV',
  'titulo_seo': 'Display de PDV para indústria: projeto e produção · 75 LAB',
  'descricao': 'Displays de chão, de balcão, clip strips e modulares para a indústria, com engenharia, aprovação em realidade aumentada antes de produzir e rastreio por QR depois de instalado.',
  'eyebrow': 'Display de PDV', 'migalhas': [SOL, ('Display de PDV', None)],
  'h1': 'Display de PDV para a indústria, do projeto à **loja**.',
  'lead': 'Criamos, projetamos e produzimos displays que ficam de pé, aguentam o produto e chegam montados. Antes de produzir, você vê o display em tamanho real na sua gôndola pelo celular.',
  'resumo': 'A 75 LAB faz o display de PDV inteiro: conceito, engenharia, produção com fornecedores homologados e entrega. A diferença é a prova nas duas pontas: o display é aprovado em realidade aumentada, em tamanho real, antes de gastar com produção, e cada peça pode sair com QR para registrar onde e quando foi montada.',
  'secoes': [
   {'h2': 'Tipos de display que projetamos', 'blocos': [{'lista': [
     '**Display de chão** autoportante, com prateleiras, gancheiras ou bandejas.',
     '**Display de balcão** para checkout, farmácia e pontos de impulso.',
     '**Clip strip** e régua de gancheira para cross merchandising.',
     '**Display modular**, reaproveitado entre campanhas trocando só a comunicação.',
     '**Display gravitacional**, que repõe o produto pela frente.',
     '**Expositor permanente** e vitrine, em MDF, metal ou acrílico.']}]},
   {'h2': 'Como o projeto anda', 'blocos': [{'passos': [
     '**Imersão:** produto, peso, canal, loja, verba e prazo. É aqui que se decide o material.',
     '**Conceito e render** com a comunicação da marca aplicada.',
     '**Engenharia:** executivo técnico com vistas, cotas, materiais, espessuras, carga por prateleira e estabilidade contra tombamento.',
     '**Aprovação em realidade aumentada:** um link abre o display em tamanho real no celular, no chão da loja ou na sala de reunião. Comercial, trade e comprador aprovam vendo a peça, não um PDF.',
     '**Produção** com fornecedores homologados por processo (papelão, MDF, metal, acrílico, arame) e controle de qualidade.',
     '**Entrega e montagem**, com página de montagem e QR na embalagem para quem instala, e registro da instalação com foto e localização.']}]},
   {'h2': 'Por que a engenharia vem antes da arte', 'blocos': [
     {'p': 'Display bonito que tomba, prateleira que enverga com o produto e peça que exige ferramenta para montar são os retrabalhos mais caros do trade, porque aparecem só na loja. Por isso todo display da 75 LAB passa por executivo técnico com conferência de carga, estabilidade, montagem sem ferramenta e transporte antes de ir para produção.'},
     {'p': 'Para escolher o material, veja o guia [Papelão, MDF, metal, acrílico ou arame](guia-material-display-pdv.html). Para conferir estabilidade, [Display que não tomba e prateleira que não enverga](guia-display-que-nao-tomba.html).'}]},
   {'h2': 'Displays que já saíram daqui', 'blocos': [
     {'galeria': [g(20, 'Unilever · display cash'), g(48, 'O Boticário · display modular'), g(43, 'Kelco · display modular'),
                  g(16, 'Polenghi · varejo e food'), g(38, 'Dako · display varejo'), g(41, 'Loungerie · display modular')]},
     {'p': 'Veja também em realidade aumentada:'},
     {'demo': [{'t': 'Clip strip Frescatino em AR', 'href': AR + 'savencia-clipstrip-frescatino/'},
               {'t': 'Display Universal NGV em AR', 'href': AR + 'ngv-displays/'}]}]},
  ],
  'faq': [
   {'q': 'Quanto tempo leva um projeto de display de PDV?', 'a': 'Depende do material, da quantidade e da complexidade da peça. Na primeira conversa a 75 LAB devolve o cronograma com as etapas de conceito, engenharia, aprovação em AR, produção e entrega, para você planejar a campanha de trás para frente.'},
   {'q': 'Preciso ter o arquivo 3D para ver o display em realidade aumentada?', 'a': 'Não. Se a sua marca já tem o 3D, nós o convertemos para AR. Se não tem, o modelo nasce no nosso projeto. O link abre no iPhone e no Android pelo navegador, sem instalar aplicativo.'},
   {'q': 'A 75 LAB fabrica o display?', 'a': 'A 75 LAB projeta e coordena a produção com uma rede de fornecedores homologados por processo, com controle de qualidade e um responsável único do briefing à entrega. Você contrata um projeto, não uma lista de fornecedores.'},
   {'q': 'Dá para reaproveitar o display em outra campanha?', 'a': 'Sim, quando ele nasce modular. A estrutura fica e muda só a comunicação. O Display Universal que adaptamos para quatro marcas da NGV é um exemplo: o mesmo módulo, com arte e ferragem diferentes por marca.'},
   {'q': 'Como saber se o display foi montado na loja?', 'a': 'Cada peça pode sair com QR. Quem instala abre a página de montagem, registra loja, foto e localização, e a marca acompanha tudo num painel com mapa. Veja [rastreamento de material de PDV](rastreamento-material-pdv.html).'},
  ],
  'relacionados': [('Ilha e ponta de gôndola', 'ilha-e-ponta-de-gondola.html'), ('Enxoval e material de PDV', 'enxoval-de-pdv.html')] + REL_PADRAO,
 },
 {
  'slug': 'ilha-e-ponta-de-gondola', 'servico': 'Ilha promocional e ponta de gôndola',
  'titulo_seo': 'Ilha promocional e ponta de gôndola para indústria · 75 LAB',
  'descricao': 'Projeto e produção de ilhas promocionais, pontas de gôndola e enxovais de gôndola, aprovados em realidade aumentada no corredor antes de produzir.',
  'eyebrow': 'Ilha e ponta de gôndola', 'migalhas': [SOL, ('Ilha e ponta de gôndola', None)],
  'h1': 'Ilha promocional e ponta de **gôndola**.',
  'lead': 'Os espaços mais disputados da loja pedem peça que chama de longe, cabe no corredor e é montada do jeito certo. A gente projeta, prova em AR e produz.',
  'resumo': 'A 75 LAB projeta e produz ilhas promocionais, pontas de gôndola e o enxoval que vai com elas (testeira, régua, wobbler, stopper, adesivo de chão). Antes de produzir, a ilha ou a ponta aparece em tamanho real no corredor pelo celular, em realidade aumentada, para aprovar medida, leitura e circulação.',
  'secoes': [
   {'h2': 'O que entregamos', 'blocos': [{'lista': [
     '**Ponta de gôndola** com estrutura, testeira, laterais e régua de preço.',
     '**Ilha promocional** de várias faces, inclusive uma marca por face.',
     '**Enxoval de gôndola:** testeira, wobbler, stopper, faixa de gôndola, régua e adesivo de chão.',
     '**Guia de implantação** com foto de como a ponta deve ficar montada.']}]},
   {'h2': 'Ilha de quatro marcas, uma por face', 'blocos': [
     {'p': 'Para a NGV, a ilha junta quatro módulos do Display Universal em 112 × 112 × 170 cm, com uma marca por face (Vitalitabs, De Llares, Bella Fio e Savedent). Duas faces usam prateleiras e duas usam gancheira, porque cada produto pede uma exposição. A ilha inteira pode ser vista em AR antes de produzir.'},
     {'fichas': [['112 × 112', 'cm de base'], ['170 cm', 'de altura'], ['4', 'marcas, uma por face']]},
     {'demo': [{'t': 'Ver a ilha NGV em AR', 'href': AR + 'ngv-displays/?modelo=ilha'}, {'t': 'Ver a ilha SEMP em AR', 'href': AR + 'semp-split-hw/?modelo=ilha'}]}]},
   {'h2': 'Pontas e ilhas que já saíram daqui', 'blocos': [
     {'galeria': [{'img': 'img/cases/ngv-ilha.webp', 'leg': 'NGV · ilha de 4 marcas (AR)', 'href': 'case-ngv-display-universal.html'},
                  {'img': 'img/cases/semp-ilha.webp', 'leg': 'SEMP · ilha premium (AR)', 'href': 'case-semp-split-hw.html'},
                  g(50, 'Seara · ponta de gôndola'), g(40, 'Petz · ponta de gôndola'), g(39, 'Bem Brasil · ponta de gôndola'), g(47, 'Bem Brasil · ponta de gôndola')]}]},
  ],
  'faq': [
   {'q': 'Qual a diferença entre ponta de gôndola e ilha promocional?', 'a': 'A ponta de gôndola fica na cabeceira do corredor e é vista de frente. A ilha fica solta no salão e é vista de todos os lados, por isso costuma ter três ou quatro faces e pede mais cuidado com estabilidade e circulação.'},
   {'q': 'Quais peças formam o enxoval de uma ponta de gôndola?', 'a': 'Em geral testeira, laterais, régua de preço, wobbler ou stopper e adesivo de chão. O conjunto muda conforme a rede e o contrato de espaço, então o enxoval é definido junto com o guia de implantação.'},
   {'q': 'Dá para ver a ilha no corredor antes de produzir?', 'a': 'Sim. A ilha é aberta em realidade aumentada, em tamanho real, pelo celular. Dá para conferir altura, leitura das marcas e se ela cabe no espaço negociado com a rede.'},
   {'q': 'Como garantir que a ponta foi montada como no projeto?', 'a': 'Com QR na peça e página de montagem. O promotor registra foto e localização ao instalar, e a marca vê no painel quais lojas já estão com a ponta montada.'},
  ],
  'relacionados': [('Display de PDV', 'display-de-pdv.html'), ('Enxoval e material de PDV', 'enxoval-de-pdv.html')] + REL_PADRAO,
 },
 {
  'slug': 'enxoval-de-pdv', 'servico': 'Enxoval e material de ponto de venda',
  'titulo_seo': 'Enxoval e material de PDV para lançamento · 75 LAB',
  'descricao': 'Enxoval completo de material de PDV para lançamento e campanha: testeira, wobbler, régua, totem, backdrop e mais, com página de montagem e QR em cada peça.',
  'eyebrow': 'Enxoval e material de PDV', 'migalhas': [SOL, ('Enxoval e material de PDV', None)],
  'h1': 'Enxoval e material de PDV, **peça por peça**.',
  'lead': 'Lançamento e campanha pedem um enxoval que conversa entre si e chega à loja com instrução. Cada peça da 75 LAB sai com página de montagem e QR na embalagem.',
  'resumo': 'A 75 LAB cria e produz o enxoval de PDV completo de um lançamento ou campanha, da testeira ao backdrop. Toda peça sai com uma página de montagem acessada por QR na embalagem: quem instala vê o passo a passo, o vídeo e a peça em realidade aumentada, e registra a instalação com foto e localização.',
  'secoes': [
   {'h2': 'Peças que entram num enxoval', 'blocos': [{'tabela': {'cab': ['Onde fica', 'Peças'], 'linhas': [
     ['Gôndola', 'testeira, régua de preço, wobbler, stopper, faixa de gôndola, precificador'],
     ['Chão', 'adesivo de chão, tapete, totem, display de chão, cubo'],
     ['Parede e alto', 'backdrop, pórtico, comunicação aérea, móbile, frame'],
     ['Produto exposto', 'topper, orelha, cinta, placa de especificação, berço']]}}]},
   {'h2': 'O enxoval que vem com manual', 'blocos': [
     {'p': 'O ponto fraco de quase todo enxoval é a ponta: a peça chega à loja e ninguém sabe montar, ou monta errado. Na 75 LAB cada peça tem uma página de produto com o que vem na caixa, passos de montagem, vídeo com capítulos, a peça em AR, medidas, checklist e perguntas frequentes. O QR vai impresso na embalagem.'},
     {'p': 'Quando o promotor abre a página, ele registra a instalação. A marca acompanha num painel com mapa, lojas positivadas e fotos das fachadas, e pode mandar um link ao vivo para o cliente acompanhar a campanha sem login.'}]},
   {'h2': 'Enxovais que já saíram daqui', 'blocos': [
     {'galeria': [{'img': 'img/cases/semp-portico.webp', 'leg': 'SEMP · pórtico do enxoval Split HW', 'href': 'case-semp-split-hw.html'},
                  {'img': 'img/cases/savencia-glorifier.webp', 'leg': 'Savencia · glorifier Frescatino', 'href': 'case-savencia-frescatino.html'},
                  g(12, 'Kelco · enxoval institucional'), g(18, 'Kelco · enxoval de lançamento'), g(25, 'FTW · enxoval de loja'), g(30, 'Lactalis · enxoval de loja')]}]},
  ],
  'faq': [
   {'q': 'O que é enxoval de PDV?', 'a': 'É o conjunto de materiais de ponto de venda de uma campanha ou lançamento, pensado para funcionar junto na loja: peças de gôndola, de chão, de parede e no próprio produto. O enxoval segue uma linha visual e um guia de implantação.'},
   {'q': 'Como a peça chega com instrução de montagem?', 'a': 'Cada peça tem uma página de produto com passo a passo, vídeo e AR, aberta pelo QR impresso na embalagem. Não precisa de aplicativo.'},
   {'q': 'Dá para saber em quais lojas o enxoval foi instalado?', 'a': 'Sim. O registro feito pela página de montagem grava loja, foto e localização. O painel mostra mapa, lojas positivadas e ritmo de instalação por rede e por cidade.'},
   {'q': 'A 75 LAB faz só a criação ou também a produção?', 'a': 'As duas coisas, com um responsável único. A produção roda com fornecedores homologados por processo e controle de qualidade até a entrega.'},
  ],
  'relacionados': [('Display de PDV', 'display-de-pdv.html'), ('Ilha e ponta de gôndola', 'ilha-e-ponta-de-gondola.html')] + REL_PADRAO,
 },
 {
  'slug': 'estandes', 'servico': 'Projeto de estande para feiras e eventos',
  'titulo_seo': 'Estande para feira com tour em realidade aumentada · 75 LAB',
  'descricao': 'Estandes para feiras e eventos B2B com aprovação em realidade aumentada e modo imersivo: a equipe caminha pelo estande antes de construir.',
  'eyebrow': 'Estandes', 'migalhas': [SOL, ('Estandes', None)],
  'h1': 'Estandes que você **percorre** antes de construir.',
  'lead': 'Do layout de circulação à comunicação visual. Antes da montagem, o estande abre em realidade aumentada e em modo imersivo, para a equipe caminhar por ele e decidir com o projeto na frente.',
  'resumo': 'A 75 LAB projeta e produz estandes para feiras e eventos B2B e leva o projeto para realidade aumentada antes da construção. Pelo celular, o estande aparece em escala no chão; no modo imersivo, a equipe anda por dentro dele, compara versões e aprova sem depender de render estático.',
  'secoes': [
   {'h2': 'O que entregamos', 'blocos': [{'lista': [
     'Layout de circulação, áreas de reunião, produto e captação de leads.',
     'Comunicação visual e acabamentos calibrados para o objetivo na feira.',
     'Estande em **realidade aumentada** e em **modo imersivo** para aprovação.',
     'Produção, montagem e desmontagem com parceiros homologados.']}]},
   {'h2': 'Comparar versões andando dentro delas', 'blocos': [
     {'p': 'No estande Revest Fácil da Alltak, de 12 × 7 metros, duas revisões do projeto ficaram lado a lado na mesma página de AR, com e sem testeira. A equipe comparou as versões no celular e escolheu a testeira vendo o estande em escala. Veja o [case completo](case-alltak-revest-facil.html).'},
     {'fichas': [['12 × 7 m', 'área do estande'], ['6,8 m', 'até o topo da testeira'], ['2', 'versões comparadas em AR']]},
     {'demo': [{'t': 'Estande Alltak em AR', 'href': AR + 'alltak-stand-revest-facil/'}, {'t': 'Estande NGV em AR', 'href': AR + 'ngv-stand-conexao-farma/'}]}]},
   {'h2': 'Estandes que já saíram daqui', 'blocos': [
     {'galeria': [{'img': 'img/cases/alltak-r05.webp', 'leg': 'Alltak · Revest Fácil (AR)', 'href': 'case-alltak-revest-facil.html'},
                  {'img': 'img/cases/ngv-stand.webp', 'leg': 'NGV · Conexão Farma (AR)', 'href': 'case-ngv-display-universal.html'},
                  g(1, 'Alltak · Future Print'), g(6, 'Alltak · Cambea Fortaleza'), g(5, 'Ciranda · Bienal RJ'), g(2, 'Pinc · mini stand')]}]},
  ],
  'faq': [
   {'q': 'O que é o modo imersivo do estande?', 'a': 'É o estande em 3D em tela cheia no celular ou no computador, sem a câmera. Você olha ao redor movendo o aparelho e anda com um joystick na tela, como se estivesse dentro do estande.'},
   {'q': 'Preciso instalar algum aplicativo para ver o estande em AR?', 'a': 'Não. O link abre no navegador do iPhone e do Android. No computador, o estande aparece em 3D com um QR para abrir no celular.'},
   {'q': 'A 75 LAB também cuida da montagem na feira?', 'a': 'Sim, com parceiros homologados de montagem e um responsável único da 75 LAB do projeto à desmontagem.'},
  ],
  'relacionados': [('Realidade aumentada para PDV', 'realidade-aumentada-pdv.html'), ('Display de PDV', 'display-de-pdv.html'), ('Cases detalhados', 'cases.html#detalhados')],
 },
 {
  'slug': 'realidade-aumentada-pdv', 'servico': 'Realidade aumentada para PDV',
  'titulo_seo': 'Realidade aumentada para PDV: veja o display na loja · 75 LAB',
  'descricao': 'Veja o display, a ilha ou o estande em tamanho real na loja pelo celular antes de produzir. AR no navegador, sem aplicativo, para aprovar e vender o projeto.',
  'eyebrow': 'Realidade aumentada', 'migalhas': [SOL, ('Realidade aumentada para PDV', None)],
  'h1': 'Veja o display na loja **antes** de produzir.',
  'lead': 'Realidade aumentada no navegador, sem aplicativo: o display aparece em tamanho real no chão da loja, na gôndola ou na parede, pelo celular de quem precisa aprovar.',
  'resumo': 'A 75 LAB transforma cada projeto de PDV em um link de realidade aumentada. Quem abre no celular vê o display, a ilha ou o estande em tamanho real, no lugar onde ele vai ficar. Isso encurta a aprovação, evita peça que não cabe e ajuda a vender o projeto para o comprador do varejo.',
  'secoes': [
   {'h2': 'Como funciona', 'blocos': [{'lista': [
     '**iPhone:** o link abre direto na realidade aumentada nativa do aparelho.',
     '**Android:** o link abre no visualizador de AR do Google, também sem aplicativo.',
     '**Computador:** o modelo aparece em 3D para girar, com um QR para continuar no celular.',
     'A peça fica **em tamanho real**, apoiada no chão ou presa à parede, conforme o tipo.']}]},
   {'h2': 'Para que serve no dia a dia do trade', 'blocos': [{'lista': [
     '**Aprovar sem PDF:** marketing, trade e comercial veem a mesma peça em escala.',
     '**Vender para o varejo:** o comprador vê o display na própria loja antes de aceitar o espaço.',
     '**Conferir medida:** altura, profundidade e corredor, no lugar real.',
     '**Treinar quem monta:** a página de montagem mostra a peça em AR junto do passo a passo.']}]},
   {'h2': 'Projetos publicados em AR', 'blocos': [
     {'p': 'Mais de 30 projetos da 75 LAB já foram publicados em realidade aumentada, de clip strips a estandes inteiros. Alguns que você pode abrir agora:'},
     {'galeria': [{'img': 'img/cases/savencia-clipstrip.webp', 'leg': 'Savencia · clip strip Frescatino', 'href': AR + 'savencia-clipstrip-frescatino/'},
                  {'img': 'img/cases/ngv-vitalitabs.webp', 'leg': 'NGV · Display Universal', 'href': AR + 'ngv-displays/'},
                  {'img': 'img/cases/semp-ilha.webp', 'leg': 'SEMP · enxoval Split HW', 'href': AR + 'semp-split-hw/'},
                  {'img': 'img/cases/alltak-r05.webp', 'leg': 'Alltak · estande Revest Fácil', 'href': AR + 'alltak-stand-revest-facil/'}]}]},
   {'h2': 'Seu display em AR em 48 horas úteis, sem custo', 'blocos': [
     {'p': 'Para indústrias que querem ver como funciona: mande pelo WhatsApp as medidas do produto e a ideia do display. Em até 48 horas úteis devolvemos o link do display em realidade aumentada para você abrir na loja. Uma peça por marca, sem compromisso de contratação.'},
     {'demo': [{'t': 'Quero meu display em AR', 'href': 'https://wa.me/5511986765634?text=' + 'Quero%20meu%20display%20em%20AR%20em%2048%20horas'}]}]},
  ],
  'faq': [
   {'q': 'Precisa instalar aplicativo para ver o display em realidade aumentada?', 'a': 'Não. O link abre no navegador do iPhone e do Android e usa o AR nativo de cada sistema. No computador, aparece o 3D com um QR para abrir no celular.'},
   {'q': 'O display aparece em tamanho real?', 'a': 'Sim. A peça abre em escala real, apoiada no chão ou presa à parede. Em estandes grandes dá para reduzir com o gesto de pinça e voltar ao tamanho real.'},
   {'q': 'Preciso ter o modelo 3D?', 'a': 'Não. Se a marca já tem o arquivo 3D, nós o preparamos para AR. Se não tem, o modelo nasce no projeto da 75 LAB.'},
   {'q': 'Em iPhones mais novos parte do display some atrás de objetos. É defeito?', 'a': 'Não. iPhones com sensor LiDAR escondem a peça virtual atrás de objetos reais, como uma pessoa ou uma caixa, e isso não pode ser desligado. Basta liberar o espaço na frente da câmera.'},
  ],
  'cta': {'k': 'Oferta para indústria', 'h': 'Seu display em AR em 48 horas úteis', 'p': 'Mande as medidas do produto e a ideia. Devolvemos o link do display em realidade aumentada, sem custo.'},
  'relacionados': [('Display de PDV', 'display-de-pdv.html'), ('Estandes', 'estandes.html'), ('Rastreamento de material de PDV', 'rastreamento-material-pdv.html'), ('Guias de PDV', 'guias.html')],
 },
 {
  'slug': 'rastreamento-material-pdv', 'servico': 'Rastreamento de material de PDV',
  'titulo_seo': 'Rastreamento de material de PDV com QR e painel · 75 LAB',
  'descricao': 'Saiba onde cada display e peça de PDV foi montado: QR na peça, registro com foto e localização, painel com mapa e link ao vivo para o cliente.',
  'eyebrow': 'Rastreamento de MPDV', 'migalhas': [SOL, ('Rastreamento de material de PDV', None)],
  'h1': 'Saiba onde cada peça de PDV foi **montada**.',
  'lead': 'Material de PDV costuma sair da fábrica e sumir. Com QR na peça e registro na instalação, a marca passa a saber em que loja, quando e como cada peça ficou.',
  'resumo': 'A 75 LAB rastreia material de PDV com um QR em cada peça. Quem instala abre a página de montagem, registra a loja com foto e localização, e a marca acompanha tudo num painel com mapa, lojas positivadas, ritmo de instalação e fotos das fachadas. O cliente pode receber um link ao vivo, sem login.',
  'secoes': [
   {'h2': 'Por que isso importa', 'blocos': [
     {'p': 'Medir o retorno do trade ainda é exceção. Na pesquisa de maturidade da Abratrade divulgada em novembro de 2026, só 15,1% dos profissionais disseram medir o retorno de forma padronizada ([Giro News](https://gironews.com/negocios/pesquisa-abratrade-aponta-baixa-maturidade-na-mensuracao-de-resultados-do-trade-marketing/)). Sem saber se a peça foi montada, não há como medir o resto.'}]},
   {'h2': 'Como funciona', 'blocos': [{'passos': [
     'Cada peça sai com um **QR** impresso na peça ou na embalagem.',
     'Quem instala abre a **página de montagem** e registra nome, loja, foto da fachada e localização do celular.',
     'O registro cai num **painel** com mapa, lojas positivadas, ritmo diário, ranking por rede, cidade e estado, e fotos.',
     'A marca gera um **link ao vivo para o cliente** ou para a diretoria, sem login, com validade e controle do que aparece.']}]},
   {'h2': 'O que o painel mostra', 'blocos': [{'lista': [
     'Lojas positivadas e cobertura por rede, cidade e estado.',
     'Ritmo de instalação dia a dia e acumulado.',
     'Peças instaladas por loja, com foto da fachada.',
     'Cruzamentos de rede com projeto e de dia com horário.',
     'Exportação para planilha.']},
     {'demo': [{'t': 'Ver a apresentação do rastreamento', 'href': 'https://projetos.75lab.com.br/rastreamento-75lab/'}]}]},
  ],
  'faq': [
   {'q': 'Como rastrear material de PDV?', 'a': 'O jeito mais simples é um QR em cada peça ligado a uma página de montagem. Ao instalar, o promotor registra loja, foto e localização, e cada registro vira um ponto no painel da marca.'},
   {'q': 'O promotor precisa instalar aplicativo?', 'a': 'Não. O QR abre uma página no navegador do celular. O registro pede nome, loja e a localização do aparelho.'},
   {'q': 'O cliente consegue acompanhar sem acessar o painel?', 'a': 'Sim. A marca gera um link público por campanha, ao vivo e sem login, com validade e escolha do que aparece, como fotos e nome dos promotores.'},
   {'q': 'Funciona para peças que a 75 LAB não produziu?', 'a': 'Sim. O QR e a página de montagem podem ser aplicados a qualquer peça da campanha, desde que a etiqueta entre na peça ou na embalagem antes do envio.'},
  ],
  'relacionados': [('Enxoval e material de PDV', 'enxoval-de-pdv.html'), ('Display de PDV', 'display-de-pdv.html'), ('Realidade aumentada para PDV', 'realidade-aumentada-pdv.html'), ('Guias de PDV', 'guias.html')],
 },
 {
  'slug': 'conteudo-rico-ecommerce', 'servico': 'Conteúdo rico para e-commerce (ClickLab)',
  'titulo_seo': 'Conteúdo rico para página de produto no e-commerce · 75 LAB',
  'descricao': 'ClickLab: conteúdo rico em HTML para a descrição do produto no marketplace e na loja virtual, com 3D, realidade aumentada, vídeo e simulação da loja.',
  'eyebrow': 'ClickLab', 'migalhas': [SOL, ('Conteúdo rico para e-commerce', None)],
  'h1': 'O PDV também é a **página de produto**.',
  'lead': 'ClickLab é o conteúdo rico da 75 LAB: a descrição do produto no e-commerce vira uma peça de marca, com 3D, realidade aumentada, vídeo e perguntas frequentes.',
  'resumo': 'O ClickLab substitui o parágrafo de texto do campo Descrição da página de produto por um conteúdo rico em HTML, feito para funcionar dentro do layout de cada varejista. Toda entrega vem com a simulação da loja, para a marca ver a peça aplicada antes de publicar.',
  'secoes': [
   {'h2': 'O que entra no conteúdo rico', 'blocos': [{'lista': [
     'Capa e benefícios com a linguagem da marca.',
     'Produto em **3D e realidade aumentada**, quando há modelo.',
     'Vídeo, comparadores interativos, tabelas e especificações.',
     'Perguntas frequentes que funcionam mesmo sem JavaScript.',
     'Texto técnico tirado do rótulo e da ficha oficial, sem promessa inventada.']}]},
   {'h2': 'Feito para rodar dentro da loja do varejista', 'blocos': [
     {'p': 'O conteúdo é entregue como um bloco único para colar no campo Descrição. Ele é isolado do estilo da loja para não quebrar o layout e se adapta à largura disponível. Junto vem uma simulação navegável da página do varejista com o conteúdo no lugar, já feita para lojas como Mercado Livre, Carrefour, Decathlon e Sonda.'},
     {'demo': [{'t': 'Ver uma simulação de loja', 'href': 'https://projetos.75lab.com.br/ftw-vitrine-ecommerce/'}]}]},
   {'h2': 'ClickLab que já saiu daqui', 'blocos': [
     {'galeria': [g(82, 'Whirlpool · ClickLab'), g(80, 'Whirlpool · loja perfeita online'), g(81, 'Kelco · ClickLab Petz'),
                  {'img': 'img/cases/semp-placa.webp', 'leg': 'SEMP · Split HW', 'href': 'case-semp-split-hw.html'}]}]},
  ],
  'faq': [
   {'q': 'O que é conteúdo rico de e-commerce?', 'a': 'É o conteúdo em HTML que ocupa o campo de descrição da página de produto, com imagens, vídeo, 3D e informação organizada, no lugar de um parágrafo de texto. Também é chamado de conteúdo A+ ou vitrine virtual.'},
   {'q': 'O conteúdo rico funciona em qualquer marketplace?', 'a': 'Depende do que cada loja aceita no campo de descrição. A 75 LAB monta o bloco para rodar dentro do estilo da loja e entrega a simulação da página do varejista para validar antes de publicar.'},
   {'q': 'Dá para mostrar o produto em realidade aumentada na página do e-commerce?', 'a': 'Sim, quando existe o modelo 3D do produto. O visitante gira o produto na tela e, no celular, coloca o produto no ambiente em tamanho real.'},
  ],
  'relacionados': [('Realidade aumentada para PDV', 'realidade-aumentada-pdv.html'), ('Case SEMP Split HW', 'case-semp-split-hw.html'), ('Guias de PDV', 'guias.html')],
 },
]
