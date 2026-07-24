/* ============================================================
   75 LAB — i18n PT/EN
   - Dicionário PT -> EN (chave = texto EXATO em português)
   - Troca instantânea, salva em localStorage, vale em todas as páginas
   - Traduz text nodes + atributos + títulos + conteúdo dinâmico
   - As traduções dos 84 cases ficam em I18N_CASES (arquivo mesclado abaixo)
   ============================================================ */
(function () {
  'use strict';

  var DICT = {
    /* ---- navegação / rodapé / comum ---- */
    "Soluções": "Solutions",
    "Sobre": "About",
    "Mídia": "Media",
    "Contato": "Contact",
    "Início": "Home",
    "75 LAB — Aceleradora de Trade Marketing.": "75 LAB — Trade Marketing Accelerator.",
    "Transformamos intenção em realidade no ponto de venda.": "We turn intention into reality at the point of sale.",
    "Abrir menu": "Open menu",
    "Reproduzir vídeo": "Play video",
    "Role para descobrir": "Scroll to explore",
    "% — ideia boa é a que acontece": "% — a good idea is one that happens",

    /* ---- titles das páginas (document.title) ---- */
    "75 LAB — Aceleradora de Trade Marketing": "75 LAB — Trade Marketing Accelerator",
    "Sobre — 75 LAB": "About — 75 LAB",
    "Soluções — 75 LAB": "Solutions — 75 LAB",
    "Mídia — 75 LAB": "Media — 75 LAB",
    "Contato — 75 LAB": "Contact — 75 LAB",

    /* ---- HERO (home) ---- */
    "Aceleradora de Trade Marketing": "Trade Marketing Accelerator",
    "Ideia boa": "A good idea",
    "é a que": "is one that",
    "acontece.": "happens.",
    "A distância entre a sua intenção e a gôndola tem um nome.": "The gap between your intention and the shelf has a name.",
    "A 75 LAB pluga o hub de soluções que a sua marca precisa — de eventos, stands e promoção a retail media e PDV — para acelerar a intenção comercial em toda a cadeia.": "75 LAB plugs in the hub of solutions your brand needs — from events, booths and promotion to retail media and POS — to accelerate commercial intention across the whole chain.",
    "Acelerar minha marca": "Accelerate my brand",
    "Ver provas reais": "See real proof",
    "anos no trade": "years in trade",
    "PDVs positivados": "POS activated",
    "projetos aprovados": "projects approved",
    "TRANSFORMAMOS INTENÇÃO EM REALIDADE · IDEIA BOA É A QUE ACONTECE ·": "WE TURN INTENTION INTO REALITY · A GOOD IDEA IS ONE THAT HAPPENS ·",

    /* ---- MARQUEE ---- */
    "ideia boa é a que acontece": "a good idea is one that happens",
    "do evento à gôndola, a solução certa": "from event to shelf, the right solution",
    "para cada desafio, a equipe certa": "for every challenge, the right team",
    "estratégia · design · produção": "strategy · design · production",
    "plugamos a solução que o cliente precisa": "we plug in the solution the client needs",

    /* ---- POR QUE / manifesto ---- */
    "Por que existimos": "Why we exist",
    "Não somos uma": "We're not a",
    "agência tradicional": "traditional agency",
    ". Somos uma": ". We're an",
    "aceleradora": "accelerator",
    "de trade marketing.": "of trade marketing.",
    "Modelo tradicional": "Traditional model",
    "Modelo 75 LAB": "75 LAB model",
    "Comparação entre o modelo tradicional e o modelo 75 LAB": "Comparison between the traditional model and the 75 LAB model",
    "RETRABALHO": "REWORK",
    "ATRASO": "DELAY",
    "VERBA EVAPORA": "BUDGET EVAPORATES",
    "INTENÇÃO": "INTENTION",
    "IMERSÃO": "IMMERSION",
    "SOLUÇÃO": "SOLUTION",
    "EXECUÇÃO": "EXECUTION",
    "RESULTADO": "RESULT",

    /* ---- ENTREGAS / hub de soluções (home) ---- */
    "Hub de soluções": "Solutions hub",
    "Plugamos a solução que a sua marca precisa.": "We plug in the solution your brand needs.",
    "Trade marketing vai muito além do PDV. A gente conecta um hub de soluções e pluga exatamente o que a sua intenção comercial pede — do evento à gôndola, da promoção ao retail media.": "Trade marketing goes far beyond POS. We connect a hub of solutions and plug in exactly what your commercial intention calls for — from event to shelf, from promotion to retail media.",
    "Eventos": "Events",
    "Experiências de marca que aproximam canal e shopper.": "Brand experiences that bring channel and shopper closer.",
    "Stand": "Booth",
    "Presença marcante em feiras, convenções e ativações.": "A standout presence at trade shows, conventions and activations.",
    "Material de PDV": "POS material",
    "Material certo, no prazo, sem retrabalho.": "The right material, on time, no rework.",
    "Programa de incentivo": "Incentive program",
    "Engajamento de equipes, canal e força de vendas.": "Engaging teams, channel and sales force.",
    "Promoção": "Promotion",
    "Mecânicas que geram giro e conversão.": "Mechanics that drive turnover and conversion.",
    "A marca nos canais de mídia do varejo.": "Your brand across retail's media channels.",
    "Promotoria": "Field merchandising",
    "Time de campo executando na ponta.": "A field team executing at the front line.",
    "+ e muito mais": "+ and much more",
    "Plugamos o especialista certo para cada desafio.": "We plug in the right specialist for every challenge.",

    /* ---- HUB de especialistas (home + sobre) ---- */
    "Hub de especialistas": "Specialist hub",
    "O cliente não compra uma entrega. Acessa uma rede.": "The client doesn't buy a deliverable. They tap into a network.",
    "Conectamos o parceiro certo, com a especialidade certa, para construir a melhor resposta a cada desafio.": "We connect the right partner, with the right expertise, to build the best answer to every challenge.",
    "Se já está no ecossistema, conectamos": "If they're already in the ecosystem, we connect them",
    "Se ainda não, buscamos e trazemos": "If not, we go find and bring them in",
    "Governança ponta a ponta, sem markup oculto": "End-to-end governance, no hidden markup",
    "Rede de parceiros conectados à 75 LAB": "Network of partners connected to 75 LAB",
    "ESTRATÉGIA": "STRATEGY",
    "PRODUÇÃO": "PRODUCTION",
    "DADOS": "DATA",
    "LOGÍSTICA": "LOGISTICS",
    "CRIAÇÃO": "CREATIVE",

    /* ---- MÉTODO (home + solucoes) ---- */
    "O Método 75 — passe o mouse": "The 75 Method — hover",
    "Seis passos até": "Six steps to",
    "o ponto de venda.": "the point of sale.",
    "Imersão": "Immersion",
    "Laboratório": "Lab",
    "Especialistas": "Specialists",
    "Estratégia + Design": "Strategy + Design",
    "Produção": "Production",
    "Execução no PDV": "POS execution",
    "Imersão no desafio": "Immersion in the challenge",
    "Entramos no contexto da marca, do canal, do produto e do shopper.": "We step into the context of the brand, the channel, the product and the shopper.",
    "Entender a intenção comercial real": "Understand the real commercial intention",
    "Mapear gargalos e custos absorvidos": "Map bottlenecks and absorbed costs",
    "Laboratório de soluções": "Solutions lab",
    "Desenhamos caminhos, testamos ideias e conectamos referências.": "We sketch paths, test ideas and connect references.",
    "Soluções com intenção, não peças bonitas": "Solutions with intent, not pretty props",
    "Validação antes de produzir": "Validation before production",
    "Conexão de especialistas": "Connecting specialists",
    "Montamos o time certo para cada projeto.": "We assemble the right team for each project.",
    "A especialidade adequada à necessidade": "The right expertise for the need",
    "Parceiros acionados na hora certa": "Partners brought in at the right time",
    "Estratégia e design": "Strategy and design",
    "Pensamento estratégico e criação visual com função comercial.": "Strategic thinking and visual design with a commercial function.",
    "Estética a serviço da conversão": "Aesthetics in service of conversion",
    "Forma e sentido de negócio": "Form and business sense",
    "Produção inteligente": "Smart production",
    "Material e logística tratados como estratégia.": "Material and logistics handled as strategy.",
    "Qualidade e controle do início ao fim": "Quality and control from start to finish",
    "A ideia não fica no plano": "The idea doesn't stay on paper",
    "A solução certa, materializada no ponto de venda.": "The right solution, made real at the point of sale.",
    "Venda, penetração e presença": "Sales, penetration and presence",
    "Impacto medido no shopper": "Impact measured on the shopper",

    /* ---- IMPACTO ---- */
    "Impacto": "Impact",
    "Prova acima": "Proof over",
    "de promessa.": "promises.",
    "Projetos aprovados": "Projects approved",
    "índice de aprovação": "approval rate",
    "Custo de produção": "Production cost",
    "com o fornecedor certo": "with the right supplier",
    "pontos de venda positivados": "points of sale activated",
    "Anos no trade": "Years in trade",
    "dos dois lados do balcão": "from both sides of the counter",

    /* ---- CASES (destaques home) ---- */
    "A prova está na gôndola.": "The proof is on the shelf.",
    "Projetos reais para marcas líderes. Aqui vão alguns destaques — o portfólio completo tem 84 cases.": "Real projects for leading brands. Here are a few highlights — the full portfolio has 84 cases.",
    "Ver todos os 84 cases": "See all 84 cases",

    /* ---- DEPOIMENTO ---- */
    "Depoimento": "Testimonial",
    "Resolveram no": "They solved, at the",
    "ponto de venda": "point of sale",
    "o que a gente tentava há meses.": "what we'd been trying to do for months.",
    "— Diretor": "— Director",
    "Uma": "A",
    "extensão estratégica": "strategic extension",
    "do nosso time de trade.": "of our trade team.",
    "Cliente 75 LAB": "75 LAB client",
    "— Liderança de Trade Marketing": "— Trade Marketing Lead",

    /* ---- VÍDEOS ---- */
    "Vídeos": "Videos",
    "A 75 LAB": "75 LAB",
    "em movimento.": "in motion.",
    "Vídeo em destaque": "Featured video",
    "Vídeo 01": "Video 01",
    "Vídeo 02": "Video 02",
    "Vídeo 03": "Video 03",

    /* ---- MÍDIA / canais (home + midia) ---- */
    "Canais": "Channels",
    "Acompanhe": "Follow",
    "a 75 LAB.": "75 LAB.",
    "Conteúdo proprietário no LinkedIn e no Instagram. Imprensa: em breve.": "Owned content on LinkedIn and Instagram. Press: coming soon.",
    "Bastidores, projetos e design estratégico no nosso Instagram.": "Behind the scenes, projects and strategic design on our Instagram.",
    "Seguir →": "Follow →",
    "Visão de trade, cases e conteúdo para indústria e varejo.": "Trade insight, cases and content for industry and retail.",
    "Conectar →": "Connect →",
    "Site": "Website",
    "Conteúdos e novidades da aceleradora de trade marketing.": "Content and news from the trade marketing accelerator.",
    "Acessar →": "Visit →",
    "Onde": "Where they",
    "falam": "talk",
    "da gente.": "about us.",
    "Imprensa, conteúdos proprietários e o que publicamos no LinkedIn e no Instagram.": "Press, owned content and what we publish on LinkedIn and Instagram.",
    "Na mídia": "In the media",
    "Onde já": "Where they've",
    "falaram da gente.": "talked about us.",
    "A 75 LAB nasceu em 2024. Cobertura de imprensa: em breve — por enquanto, acompanhe nossos canais.": "75 LAB was born in 2024. Press coverage: coming soon — for now, follow our channels.",
    "Nas redes": "On social",
    "O que a gente": "What we",
    "posta por aí.": "post out there.",
    "Cole aqui um post de LinkedIn: visão sobre trade, intenção transformada em solução, dado proprietário.": "Drop a LinkedIn post here: a take on trade, intention turned into solution, proprietary data.",
    "Bastidor de uma execução no PDV: parceiros acionados, material certo e resultado na gôndola.": "Behind the scenes of a POS rollout: partners activated, the right material and results on the shelf.",
    "Opinião dos sócios: por que solução certa não é solução pronta.": "The partners' view: why the right solution isn't an off-the-shelf one.",
    "Ver post →": "View post →",
    "Agência 75 LAB": "75 LAB Agency",
    "CEO 75 LAB": "75 LAB CEO",

    /* ---- SLOGAN ---- */
    "A tese": "The thesis",
    "ideia boa é a que": "a good idea is one that",
    "acontece": "happens",
    "A assinatura é simples. A exigência por trás dela é alta: fazer acontecer.": "The tagline is simple. The bar behind it is high: making it happen.",

    /* ---- CTA band ---- */
    "Tem uma intenção comercial?": "Got a commercial intention?",
    "vamos fazer": "let's make it",
    "acontecer": "happen",

    /* ---- CONTATO (home + contato) ---- */
    "Conta a": "Tell us your",
    "intenção.": "intention.",
    "intenção": "intention",
    "Qual é o desafio da sua marca no canal? A gente traduz e materializa a solução certa para o PDV.": "What's your brand's challenge in the channel? We translate it and make the right solution real at POS.",
    "Qual é o desafio da sua marca no canal? A gente traduz a intenção e pluga a solução certa para acelerar o resultado.": "What's your brand's challenge in the channel? We translate the intention and plug in the right solution to accelerate results.",
    "Conte o desafio da sua marca. Respondemos rápido — e já começamos a desenhar a solução.": "Tell us your brand's challenge. We reply fast — and start designing the solution right away.",
    "E-mail": "Email",
    "Base": "Based in",
    "Nome": "Name",
    "Empresa": "Company",
    "Qual a intenção comercial?": "What's your commercial intention?",
    "Seu nome": "Your name",
    "Marca / rede de varejo": "Brand / retail chain",
    "voce@empresa.com": "you@company.com",
    "Ex.: lançar produto, aumentar penetração, melhorar exposição no PDV...": "e.g. launch a product, grow penetration, improve POS visibility...",
    "Ex.: lançar produto, aumentar penetração, ativar um evento, melhorar exposição no PDV...": "e.g. launch a product, grow penetration, run an event, improve POS visibility...",
    "Enviar briefing": "Send briefing",

    /* ---- SOBRE (página) ---- */
    "Os dois lados do": "Both sides of the",
    "balcão": "counter",
    "Nascemos da soma do varejo com a indústria. Por isso entregamos soluções que geram valor para toda a cadeia.": "We were born from retail and industry combined. That's why we deliver solutions that create value across the whole chain.",
    "“Criamos o que": "“We built what we",
    "gostaríamos": "wish",
    "de ter tido como clientes.”": "we'd had as clients.”",
    "Daniel Coimbra · CEO 75 LAB": "Daniel Coimbra · 75 LAB CEO",
    "A 75 LAB nasceu da soma de dois lados que quase nunca se sentam à mesma mesa:": "75 LAB was born from two sides that almost never sit at the same table:",
    "o varejo e a indústria": "retail and industry",
    ". Por mais de 15 anos, vivemos a distância entre a intenção comercial de uma marca e o que de fato acontece no canal.": ". For over 15 years, we lived the gap between a brand's commercial intention and what actually happens in the channel.",
    "Por isso não entregamos solução de prateleira. A gente entende os dois lados do balcão e": "That's why we don't deliver off-the-shelf solutions. We understand both sides of the counter and",
    "pluga a solução certa": "plug in the right solution",
    "— sem markup oculto, com a língua do cliente: ROI, margem, sell-out, positivação.": "— no hidden markup, in the client's language: ROI, margin, sell-out, in-store presence.",
    "Vivemos o trade — não só aprendemos.": "We've lived trade — not just studied it.",
    "Solução certa, nunca de prateleira.": "The right solution, never off the shelf.",
    "Para cada desafio, a equipe certa.": "For every challenge, the right team.",
    "Prova acima de promessa.": "Proof over promises.",
    "Os dois lados do balcão": "Both sides of the counter",
    "Veio do varejo": "From retail",
    "Co-fundador · Head de Trade": "Co-founder · Head of Trade",
    "Veio do varejo e conhece o PDV pelo lado de quem opera a loja: layout de loja, execução no ponto e a régua de aprovação das iniciativas da indústria passaram pela mão dele.": "Came from retail and knows POS from the operator's side: store layout, in-store execution and the approval bar for industry initiatives all passed through his hands.",
    "Layout de loja e execução no ponto": "Store layout and in-store execution",
    "Aprovação das iniciativas da indústria": "Approval of industry initiatives",
    "Merchandising e campanhas cooperadas": "Merchandising and co-op campaigns",
    "Veio da indústria": "From industry",
    "Co-fundador · CEO": "Co-founder · CEO",
    "Veio da indústria e pensa a marca a partir do P&L: lançamento de produtos, gestão de categoria e a estratégia comercial que precisa virar venda na ponta.": "Came from industry and thinks about the brand from the P&L: product launches, category management and the commercial strategy that has to turn into sales at the front line.",
    "Lançamento de produtos": "Product launches",
    "Gestão de categoria": "Category management",
    "P&L e estratégia comercial": "P&L and commercial strategy",
    "A 75 LAB conecta indústria e varejo gerando valor para os dois lados da cadeia": "75 LAB connects industry and retail, creating value for both sides of the chain",
    "INDÚSTRIA": "INDUSTRY",
    "lançamentos": "launches",
    "VAREJO": "RETAIL",
    "execução": "execution",
    "← valor →": "← value →",
    "Valor para a indústria e para o varejo — na mesma mesa.": "Value for industry and retail — at the same table.",
    "Tem uma intenção comercial?": "Got a commercial intention?",

    /* ---- SOLUÇÕES (página) ---- */
    "Um hub de soluções,": "A solutions hub,",
    "plugado": "plugged",
    "à sua intenção.": "into your intention.",
    "Trade marketing vai muito além do PDV. Conectamos um hub de soluções e plugamos exatamente o que a sua intenção comercial pede — do evento à gôndola.": "Trade marketing goes far beyond POS. We connect a hub of solutions and plug in exactly what your commercial intention calls for — from event to shelf.",
    "Plugue a solução.": "Plug in the solution.",
    "Veja o que entra junto.": "See what comes with it.",
    "Trade marketing é um hub de soluções plugáveis. Passe o mouse (ou toque) em cada uma para ver como ela acelera a sua intenção.": "Trade marketing is a hub of pluggable solutions. Hover (or tap) each one to see how it accelerates your intention.",
    "Material PDV": "POS material",
    "Incentivo": "Incentive",
    "Promocao": "Promotion",
    "+ Mais": "+ More",
    "Experiencias de marca que aproximam canal, shopper e equipe — do conceito a execucao.": "Brand experiences that bring channel, shopper and team closer — from concept to execution.",
    "Presenca que chama atencao em feiras e eventos: projeto, producao e montagem.": "An attention-grabbing presence at fairs and events: design, production and build.",
    "O material certo na gondola — display, comunicacao e exposicao que convertem.": "The right material on the shelf — displays, communication and merchandising that convert.",
    "Engajamento de forca de vendas e canal com mecanicas que movem o resultado.": "Engaging the sales force and channel with mechanics that move results.",
    "Mecanicas promocionais que geram giro, experimentacao e sell-out.": "Promotional mechanics that drive turnover, trial and sell-out.",
    "A sua marca nos canais de midia do varejo, dentro e fora da loja.": "Your brand across retail's media channels, in-store and out.",
    "Time de campo executando na ponta, com inteligencia e cobertura.": "A field team executing at the front line, with intelligence and coverage.",
    "Nao achou? A gente pluga o especialista certo do hub para o seu desafio.": "Didn't find it? We plug in the right specialist from the hub for your challenge.",
    "Solucao plugada": "Solution plugged in",
    "Convencoes": "Conventions",
    "Ativacoes": "Activations",
    "Experiencias": "Experiences",
    "Projeto": "Design",
    "Producao": "Production",
    "Montagem": "Build",
    "Displays": "Displays",
    "Comunicacao": "Communication",
    "Exposicao": "Merchandising",
    "Forca de vendas": "Sales force",
    "Canal": "Channel",
    "Premiacao": "Rewards",
    "Giro": "Turnover",
    "Experimentacao": "Trial",
    "Midia de varejo": "Retail media",
    "Time de campo": "Field team",
    "Execucao": "Execution",
    "Cobertura": "Coverage",
    "Hub de parceiros": "Partner hub",
    "Sob medida": "Tailor-made",

    /* ---- CASES (página) — rótulos fixos ---- */
    "A prova está na": "The proof is on the",
    "gôndola": "shelf",
    "+500 projetos executados para marcas líderes. Abaixo, 84 do portfólio —": "500+ projects delivered for leading brands. Below, 84 of the portfolio —",
    "clique em qualquer um": "click any one",
    "para ver as fotos e a história completa.": "to see the photos and the full story.",
    "Performance comprovada": "Proven performance",
    "Números que comprovam.": "The numbers that prove it.",
    "anos de experiência": "years of experience",
    "fornecedores cadastrados": "registered suppliers",
    "projetos executados": "projects delivered",
    "redução média de custo": "average cost reduction",
    "Portfólio": "Portfolio",
    "Projetos que aconteceram.": "Projects that happened.",
    "84 projetos reais para marcas líderes. Filtre por tipo de solução e clique para abrir.": "84 real projects for leading brands. Filter by solution type and click to open.",
    "Todos": "All",
    "Ativações": "Activations",
    "Campanhas": "Campaigns",
    "Objetivo": "Objective",
    "Quero um resultado assim": "I want results like this",
    "Detalhes do case": "Case details",
    "Fechar": "Close",

    /* ---- 404 ---- */
    "Erro 404": "Error 404",
    "Página": "This page",
    "não": "never",
    "Mas ideia boa é a que acontece. Volte para o início e siga a aceleração.": "But a good idea is one that happens. Head back home and keep the acceleration going.",
    "Voltar ao início": "Back to home",
    "Falar com a gente": "Talk to us"
  };

  /* mescla traduções dos 84 cases, se presentes (I18N_CASES vem de i18n-cases.js / inline) */
  if (typeof window !== 'undefined' && window.I18N_CASES) {
    for (var ck in window.I18N_CASES) { if (!(ck in DICT)) DICT[ck] = window.I18N_CASES[ck]; }
  }

  var ATTRS = ['placeholder', 'aria-label', 'title'];
  var SKIP = { SCRIPT: 1, STYLE: 1, NOSCRIPT: 1 };
  var origText = new WeakMap();
  var origAttr = new WeakMap();
  var origTitle = null;
  var lang = 'pt';

  function translatable(s) {
    if (!s) return false;
    var t = s.trim();
    if (!t) return false;
    // ignora números / pontuação / símbolos puros
    if (/^[\d\s.,;:%°+·\-–—\/()→←↗↓×"'’“”]*$/.test(t)) return false;
    return true;
  }

  function applyText(node) {
    var raw = node.nodeValue;
    if (!translatable(raw)) return;
    var en = DICT[raw.trim()];
    if (en == null) return;
    if (!origText.has(node)) origText.set(node, raw);
    var lead = raw.match(/^\s*/)[0], trail = raw.match(/\s*$/)[0];
    node.nodeValue = lead + en + trail;
  }
  function restoreText(node) { if (origText.has(node)) node.nodeValue = origText.get(node); }

  function applyAttr(el) {
    if (!el.getAttribute) return;
    for (var i = 0; i < ATTRS.length; i++) {
      var a = ATTRS[i];
      if (!el.hasAttribute(a)) continue;
      var v = el.getAttribute(a);
      var en = DICT[v && v.trim()];
      if (en == null) continue;
      var store = origAttr.get(el) || {};
      if (!(a in store)) { store[a] = v; origAttr.set(el, store); }
      el.setAttribute(a, en);
    }
  }
  function restoreAttr(el) {
    var store = origAttr.get(el); if (!store) return;
    for (var a in store) el.setAttribute(a, store[a]);
  }

  function each(root, textFn, attrFn) {
    if (root.nodeType === 3) { textFn(root); return; }
    if (root.nodeType !== 1) return;
    if (root.nodeType === 1) attrFn(root);
    var tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        return (n.parentNode && SKIP[n.parentNode.nodeName]) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
      }
    });
    var n; while (n = tw.nextNode()) textFn(n);
    var ew = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT, null);
    var e; while (e = ew.nextNode()) attrFn(e);
  }
  function toEN(root) { each(root, applyText, applyAttr); }
  function toPT(root) { each(root, restoreText, restoreAttr); }

  function setLang(l) {
    lang = (l === 'en') ? 'en' : 'pt';
    try { localStorage.setItem('lang75', lang); } catch (e) {}
    document.documentElement.setAttribute('lang', lang === 'en' ? 'en' : 'pt-BR');
    if (lang === 'en') {
      toEN(document.body);
      var t = DICT[document.title]; if (t) { if (origTitle == null) origTitle = document.title; document.title = t; }
    } else {
      toPT(document.body);
      if (origTitle != null) { document.title = origTitle; origTitle = null; }
    }
    updateToggle();
  }

  function buildToggle() {
    var navs = document.querySelectorAll('header .nav-links');
    navs.forEach(function (nav) {
      if (nav.querySelector('.langtoggle')) return;
      var wrap = document.createElement('div');
      wrap.className = 'langtoggle';
      wrap.setAttribute('role', 'group');
      wrap.setAttribute('aria-label', 'Idioma / Language');
      wrap.innerHTML =
        '<button type="button" data-lang="pt" title="Português" aria-label="Português"><span class="flag">🇧🇷</span></button>' +
        '<button type="button" data-lang="en" title="English" aria-label="English"><span class="flag">🇺🇸</span></button>';
      nav.appendChild(wrap);
      wrap.addEventListener('click', function (e) {
        var b = e.target.closest('button[data-lang]');
        if (b) setLang(b.getAttribute('data-lang'));
      });
    });
  }
  function updateToggle() {
    document.querySelectorAll('.langtoggle button[data-lang]').forEach(function (b) {
      b.classList.toggle('on', b.getAttribute('data-lang') === lang);
    });
  }

  function observeDynamic() {
    var ids = ['caseModal', 'hubpanel', 'hubstage', 'nodes'];
    var targets = [];
    ids.forEach(function (id) { var el = document.getElementById(id); if (el) targets.push(el); });
    if (!targets.length) return;
    var queue = [];
    var scheduled = false;
    function flush() {
      scheduled = false;
      if (lang !== 'en') { queue = []; return; }
      queue.forEach(function (nd) {
        if (nd.nodeType === 1) toEN(nd);
        else if (nd.nodeType === 3) applyText(nd);
      });
      queue = [];
    }
    var obs = new MutationObserver(function (muts) {
      if (lang !== 'en') return;
      muts.forEach(function (m) {
        if (m.type === 'childList') { m.addedNodes.forEach(function (nd) { queue.push(nd); }); }
        else if (m.type === 'characterData') { queue.push(m.target); }
      });
      if (!scheduled) { scheduled = true; requestAnimationFrame(flush); }
    });
    targets.forEach(function (t) { obs.observe(t, { childList: true, subtree: true, characterData: true }); });
  }

  function init() {
    buildToggle();
    observeDynamic();
    var saved = 'pt';
    try { saved = localStorage.getItem('lang75') || 'pt'; } catch (e) {}
    setLang(saved);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();

  window.i18n75 = {
    set: setLang,
    get: function () { return lang; },
    apply: function (root) { if (lang === 'en') toEN(root || document.body); }
  };
})();
