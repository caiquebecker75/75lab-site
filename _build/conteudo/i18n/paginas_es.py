"""Versiones en español (servidas en /es/) de las páginas de servicio y de cases de la 75 LAB.
Misma estructura que _build/conteudo/servicos.py y cases.py. Reglas: solo hechos que están en los
originales en portugués, nunca raya ni semirraya, marcación limitada a [texto](url) y **negrita**.
Los links internos apuntan a las páginas traducidas cuando existen (es/...); si no, a la página
en portugués sin prefijo de carpeta, avisando "(en portugués)" en el texto del link."""

AR = 'https://projetos.75lab.com.br/ar/'
SOL = ('Soluciones', '/solucoes.html')
CAS = ('Cases', '/cases.html')
REL_PADRAO = [('Realidad aumentada para PDV', 'es/realidad-aumentada-pdv.html'),
              ('Rastreo de material de PDV', 'es/rastreo-material-pdv.html'),
              ('Cases detallados (en portugués)', 'cases.html#detalhados'),
              ('Guías de PDV (en portugués)', 'guias.html')]
REL_CASES = [('Exhibidor de PDV', 'es/exhibidor-pdv.html'), ('Realidad aumentada para PDV', 'es/realidad-aumentada-pdv.html'),
             ('Rastreo de material de PDV', 'es/rastreo-material-pdv.html'), ('Todos los cases (en portugués)', 'cases.html')]


def g(n, leg):
    return {'img': f'img/g{n:02d}-1.jpg', 'leg': leg, 'href': 'cases.html'}


HOME = {
 'titulo_seo': 'Agencia de PDV comprobado en São Paulo · 75 LAB',
 'descricao': '75 LAB diseña y produce exhibidores, islas, cabeceras de góndola, kits de PDV y stands, aprobados en realidad aumentada antes de producir y rastreados por QR.',
 'eyebrow': 'Agencia de PDV comprobado',
 'h1': 'Una buena idea es la que **sucede**.',
 'lead': '75 LAB crea, diseña y produce exhibidores, islas, kits de PDV y stands, y lo prueba en los dos extremos: ves el exhibidor en tu góndola en realidad aumentada antes de producir, y sabes dónde está montado después de salir de la fábrica.',
 'resumo': '75 LAB es una agencia de punto de venta (PDV) y trade marketing con sede en el CENU, en São Paulo, fundada en 2024 por Caique Becker, que viene del retail, y Daniel Coimbra, que viene de la industria. Crea, diseña y produce material de punto de venta para la industria de bienes de consumo: exhibidores de piso y de mostrador, clip strips, islas promocionales, cabeceras de góndola, kits de lanzamiento y stands para ferias. Trabaja por proyecto, con alcance, plazo y precio cerrados.',
 'secoes': [
  {'h2': 'Qué hace la 75 LAB', 'blocos': [{'lista': [
    '[**Exhibidor de PDV**](es/exhibidor-pdv.html): de piso, de mostrador, clip strip y modular, con ingeniería y AR antes de producir.',
    '[**Isla y cabecera de góndola** (en portugués)](ilha-e-ponta-de-gondola.html): los espacios más disputados de la tienda, aprobados en el pasillo en AR.',
    '[**Kit de PDV** (en portugués)](enxoval-de-pdv.html): pieza por pieza, con página de montaje y QR en el embalaje.',
    '[**Stands** (en portugués)](estandes.html): ferias y eventos con recorrido en AR y modo inmersivo.',
    '[**Realidad aumentada**](es/realidad-aumentada-pdv.html): el exhibidor en tamaño real en la tienda, desde el celular, sin aplicación.',
    '[**Rastreo de material de PDV**](es/rastreo-material-pdv.html): QR, foto y ubicación para saber dónde se montó cada pieza.',
    '[**Contenido enriquecido, ClickLab** (en portugués)](conteudo-rico-ecommerce.html): la página de producto del e-commerce como pieza de marca.']}]},
  {'h2': 'Cómo funciona el PDV comprobado', 'blocos': [{'passos': [
    '**Antes de producir:** cada pieza se aprueba en realidad aumentada, en tamaño real, en la góndola de la propia cadena, desde el celular. Marketing, trade, el área comercial y el comprador del retail aprueban viendo la pieza, no un PDF.',
    '**Después de instalada:** la pieza puede llevar un QR que abre la página de montaje y registra tienda, fecha, foto y ubicación, en un panel que la marca sigue en vivo.']}]},
  {'h2': 'Cases', 'blocos': [{'lista': [
    '[**NGV: un exhibidor, cuatro marcas**](es/caso-ngv-exhibidor-universal.html). El Exhibidor Universal adaptado para Vitalitabs, De Llares, Bella Fio y Savedent, una isla de cuatro caras y el stand de Conexão Farma, todo en AR.',
    '[**SEMP: 15 piezas de PDV, todas en AR**](es/caso-semp-split-hw.html). El kit del aire acondicionado Split HW en una sola página de realidad aumentada, con página de montaje y contenido enriquecido para el marketplace.',
    '[**Todos los cases** (en portugués)](cases.html): Savencia, Alltak y el portafolio completo.']}]},
 ],
}


PAGINAS = [
 {
  'slug': 'es/exhibidor-pdv', 'servico': 'Diseño y producción de exhibidores de PDV',
  'titulo_seo': 'Exhibidor de PDV: diseño y producción para industria · 75 LAB',
  'descricao': 'Exhibidores de piso, de mostrador, clip strips y modulares para la industria, con ingeniería, aprobación en realidad aumentada y rastreo por QR en la tienda.',
  'eyebrow': 'Exhibidor de PDV', 'migalhas': [SOL, ('Exhibidor de PDV', None)],
  'h1': 'Exhibidores de PDV para la industria, del proyecto a la **tienda**.',
  'lead': 'Creamos, diseñamos y producimos exhibidores que se mantienen en pie, aguantan el producto y llegan montados. Antes de producir, ves el exhibidor en tamaño real en tu góndola desde el celular.',
  'resumo': '75 LAB hace el exhibidor de punto de venta (PDV) completo: concepto, ingeniería, producción con proveedores homologados y entrega. La diferencia es la prueba en los dos extremos: el exhibidor se aprueba en realidad aumentada, en tamaño real, antes de gastar en producción, y cada pieza puede salir con un QR que registra dónde y cuándo se montó.',
  'secoes': [
   {'h2': 'Tipos de exhibidor que diseñamos', 'blocos': [{'lista': [
     '**Exhibidor de piso** autoportante, con estantes, ganchos o bandejas.',
     '**Exhibidor de mostrador** para caja, farmacia y puntos de impulso.',
     '**Clip strip** y regleta de ganchos para venta cruzada.',
     '**Exhibidor modular**, que se reutiliza de una campaña a otra cambiando solo la comunicación.',
     '**Exhibidor por gravedad**, que repone el producto por el frente.',
     '**Exhibidor permanente** y vitrina, en MDF, metal o acrílico.']}]},
   {'h2': 'Cómo avanza el proyecto', 'blocos': [{'passos': [
     '**Inmersión:** producto, peso, canal, tienda, presupuesto y plazo. Aquí se decide el material.',
     '**Concepto y render** con la comunicación de la marca aplicada.',
     '**Ingeniería:** planos técnicos con vistas, cotas, materiales, espesores, carga por estante y estabilidad contra vuelco.',
     '**Aprobación en realidad aumentada:** un link abre el exhibidor en tamaño real en el celular, en el piso de la tienda o en la sala de reuniones. El área comercial, trade y el comprador aprueban viendo la pieza, no un PDF.',
     '**Producción** con proveedores homologados por proceso (cartón, MDF, metal, acrílico, alambre) y control de calidad.',
     '**Entrega y montaje**, con página de montaje y QR en el embalaje para quien instala, y registro de la instalación con foto y ubicación.']}]},
   {'h2': 'Por qué la ingeniería va antes que el arte', 'blocos': [
     {'p': 'Un exhibidor bonito que se vuelca, un estante que se comba con el producto y una pieza que exige herramientas para montar son los retrabajos más caros del trade, porque aparecen recién en la tienda. Por eso todo exhibidor de la 75 LAB pasa por planos técnicos con verificación de carga, estabilidad, montaje sin herramientas y transporte antes de ir a producción.'},
     {'p': 'Para elegir el material, consulta la guía [Cartón, MDF, metal, acrílico o alambre (en portugués)](guia-material-display-pdv.html). Para verificar la estabilidad, [Exhibidor que no se vuelca y estante que no se comba (en portugués)](guia-display-que-nao-tomba.html).'}]},
   {'h2': 'Exhibidores que ya salieron de aquí', 'blocos': [
     {'galeria': [g(20, 'Unilever · display cash'), g(48, 'O Boticário · exhibidor modular'), g(43, 'Kelco · exhibidor modular'),
                  g(16, 'Polenghi · retail y food'), g(38, 'Dako · exhibidor retail'), g(41, 'Loungerie · exhibidor modular')]},
     {'p': 'Míralos también en realidad aumentada:'},
     {'demo': [{'t': 'Clip strip Frescatino en AR', 'href': AR + 'savencia-clipstrip-frescatino/'},
               {'t': 'Exhibidor Universal NGV en AR', 'href': AR + 'ngv-displays/'}]}]},
  ],
  'faq': [
   {'q': '¿Cuánto tarda un proyecto de exhibidor de PDV?', 'a': 'Depende del material, de la cantidad y de la complejidad de la pieza. En la primera conversación, la 75 LAB te entrega el cronograma con las etapas de concepto, ingeniería, aprobación en AR, producción y entrega, para que planifiques la campaña de atrás hacia adelante.'},
   {'q': '¿Necesito tener el archivo 3D para ver el exhibidor en realidad aumentada?', 'a': 'No. Si tu marca ya tiene el 3D, lo convertimos a AR. Si no lo tiene, el modelo nace en nuestro proyecto. El link abre en iPhone y Android desde el navegador, sin instalar ninguna aplicación.'},
   {'q': '¿La 75 LAB fabrica el exhibidor?', 'a': 'La 75 LAB diseña y coordina la producción con una red de proveedores homologados por proceso, con control de calidad y un único responsable del brief a la entrega. Contratas un proyecto, no una lista de proveedores.'},
   {'q': '¿Se puede reutilizar el exhibidor en otra campaña?', 'a': 'Sí, cuando nace modular. La estructura se mantiene y cambia solo la comunicación. El Exhibidor Universal que adaptamos para cuatro marcas de NGV es un ejemplo: el mismo módulo, con arte y herrajes distintos para cada marca.'},
   {'q': '¿Cómo saber si el exhibidor se montó en la tienda?', 'a': 'Cada pieza puede salir con un QR. Quien instala abre la página de montaje, registra tienda, foto y ubicación, y la marca sigue todo en un panel con mapa. Mira [rastreo de material de PDV](es/rastreo-material-pdv.html).'},
  ],
  'relacionados': [('Isla y cabecera de góndola (en portugués)', 'ilha-e-ponta-de-gondola.html'),
                   ('Kit y material de PDV (en portugués)', 'enxoval-de-pdv.html')] + REL_PADRAO,
 },
 {
  'slug': 'es/realidad-aumentada-pdv', 'servico': 'Realidad aumentada para PDV',
  'titulo_seo': 'Realidad aumentada para PDV: el exhibidor en tienda · 75 LAB',
  'descricao': 'Ve el exhibidor, la isla o el stand en tamaño real en la tienda desde el celular antes de producir. AR en el navegador, sin aplicación, para aprobar y vender.',
  'eyebrow': 'Realidad aumentada', 'migalhas': [SOL, ('Realidad aumentada para PDV', None)],
  'h1': 'Ve el exhibidor en la tienda **antes** de producir.',
  'lead': 'Realidad aumentada en el navegador, sin aplicación: el exhibidor aparece en tamaño real en el piso de la tienda, en la góndola o en la pared, en el celular de quien tiene que aprobarlo.',
  'resumo': '75 LAB convierte cada proyecto de punto de venta (PDV) en un link de realidad aumentada. Quien lo abre en el celular ve el exhibidor, la isla o el stand en tamaño real, en el lugar donde va a estar. Eso acorta la aprobación, evita piezas que no caben y ayuda a vender el proyecto al comprador del retail.',
  'secoes': [
   {'h2': 'Cómo funciona', 'blocos': [{'lista': [
     '**iPhone:** el link abre directo en la realidad aumentada nativa del equipo.',
     '**Android:** el link abre en el visor de AR de Google, también sin aplicación.',
     '**Computadora:** el modelo aparece en 3D para girarlo, con un QR para seguir en el celular.',
     'La pieza aparece **en tamaño real**, apoyada en el piso o fijada a la pared, según el tipo.']}]},
   {'h2': 'Para qué sirve en el día a día del trade', 'blocos': [{'lista': [
     '**Aprobar sin PDF:** marketing, trade y el área comercial ven la misma pieza a escala.',
     '**Vender al retail:** el comprador ve el exhibidor en su propia tienda antes de aceptar el espacio.',
     '**Verificar medidas:** altura, profundidad y pasillo, en el lugar real.',
     '**Capacitar a quien monta:** la página de montaje muestra la pieza en AR junto al paso a paso.']}]},
   {'h2': 'Proyectos publicados en AR', 'blocos': [
     {'p': 'Más de 30 proyectos de la 75 LAB ya se publicaron en realidad aumentada, desde clip strips hasta stands completos. Algunos que puedes abrir ahora:'},
     {'galeria': [{'img': 'img/cases/savencia-clipstrip.webp', 'leg': 'Savencia · clip strip Frescatino', 'href': AR + 'savencia-clipstrip-frescatino/'},
                  {'img': 'img/cases/ngv-vitalitabs.webp', 'leg': 'NGV · Exhibidor Universal', 'href': AR + 'ngv-displays/'},
                  {'img': 'img/cases/semp-ilha.webp', 'leg': 'SEMP · kit de PDV Split HW', 'href': AR + 'semp-split-hw/'},
                  {'img': 'img/cases/alltak-r05.webp', 'leg': 'Alltak · stand Revest Fácil', 'href': AR + 'alltak-stand-revest-facil/'}]}]},
   {'h2': 'Tu exhibidor en AR en 48 horas hábiles, sin costo', 'blocos': [
     {'p': 'Para industrias que quieren ver cómo funciona: envía por WhatsApp las medidas del producto y la idea del exhibidor. En hasta 48 horas hábiles te devolvemos el link del exhibidor en realidad aumentada para que lo abras en la tienda. Una pieza por marca, sin compromiso de contratación.'},
     {'demo': [{'t': 'Quiero mi exhibidor en AR', 'href': 'https://wa.me/5511986765634?text=' + 'Quiero%20mi%20exhibidor%20en%20AR%20en%2048%20horas'}]}]},
  ],
  'faq': [
   {'q': '¿Hay que instalar una aplicación para ver el exhibidor en realidad aumentada?', 'a': 'No. El link abre en el navegador del iPhone y del Android y usa el AR nativo de cada sistema. En la computadora aparece el 3D con un QR para abrirlo en el celular.'},
   {'q': '¿El exhibidor aparece en tamaño real?', 'a': 'Sí. La pieza abre a escala real, apoyada en el piso o fijada a la pared. En stands grandes puedes reducirla con el gesto de pinza y volver al tamaño real.'},
   {'q': '¿Necesito tener el modelo 3D?', 'a': 'No. Si la marca ya tiene el archivo 3D, lo preparamos para AR. Si no lo tiene, el modelo nace en el proyecto de la 75 LAB.'},
   {'q': 'En los iPhone más nuevos, parte del exhibidor desaparece detrás de objetos. ¿Es un defecto?', 'a': 'No. Los iPhone con sensor LiDAR ocultan la pieza virtual detrás de objetos reales, como una persona o una caja, y eso no se puede desactivar. Basta con despejar el espacio frente a la cámara.'},
  ],
  'cta': {'k': 'Oferta para la industria', 'h': 'Tu exhibidor en AR en 48 horas hábiles', 'p': 'Envía las medidas del producto y la idea. Te devolvemos el link del exhibidor en realidad aumentada, sin costo.'},
  'relacionados': [('Exhibidor de PDV', 'es/exhibidor-pdv.html'), ('Stands (en portugués)', 'estandes.html'),
                   ('Rastreo de material de PDV', 'es/rastreo-material-pdv.html'), ('Guías de PDV (en portugués)', 'guias.html')],
 },
 {
  'slug': 'es/rastreo-material-pdv', 'servico': 'Rastreo de material de PDV',
  'titulo_seo': 'Rastreo de material de PDV con QR y panel · 75 LAB',
  'descricao': 'Sabe dónde se montó cada exhibidor y pieza de PDV: QR en la pieza, registro con foto y ubicación, panel con mapa y link en vivo para el cliente.',
  'eyebrow': 'Rastreo de material de PDV', 'migalhas': [SOL, ('Rastreo de material de PDV', None)],
  'h1': 'Sabe dónde se **montó** cada pieza de PDV.',
  'lead': 'El material de punto de venta (PDV) suele salir de la fábrica y desaparecer. Con un QR en la pieza y un registro en la instalación, la marca pasa a saber en qué tienda, cuándo y cómo quedó cada pieza.',
  'resumo': '75 LAB rastrea el material de PDV con un QR en cada pieza. Quien instala abre la página de montaje, registra la tienda con foto y ubicación, y la marca sigue todo en un panel con mapa, tiendas con presencia, ritmo de instalación y fotos de las fachadas. El cliente puede recibir un link en vivo, sin login.',
  'secoes': [
   {'h2': 'Por qué importa', 'blocos': [
     {'p': 'Medir el retorno del trade todavía es la excepción. En la encuesta de madurez de Abratrade divulgada en noviembre de 2026, solo el 15,1% de los profesionales dijo medir el retorno de forma estandarizada ([Giro News](https://gironews.com/negocios/pesquisa-abratrade-aponta-baixa-maturidade-na-mensuracao-de-resultados-do-trade-marketing/), en portugués). Sin saber si la pieza se montó, no hay cómo medir lo demás.'}]},
   {'h2': 'Cómo funciona', 'blocos': [{'passos': [
     'Cada pieza sale con un **QR** impreso en la pieza o en el embalaje.',
     'Quien instala abre la **página de montaje** y registra nombre, tienda, foto de la fachada y ubicación del celular.',
     'El registro llega a un **panel** con mapa, tiendas con presencia, ritmo diario, ranking por cadena, ciudad y estado, y fotos.',
     'La marca genera un **link en vivo para el cliente** o para la dirección, sin login, con vencimiento y control de lo que se muestra.']}]},
   {'h2': 'Qué muestra el panel', 'blocos': [{'lista': [
     'Tiendas con presencia y cobertura por cadena, ciudad y estado.',
     'Ritmo de instalación día a día y acumulado.',
     'Piezas instaladas por tienda, con foto de la fachada.',
     'Cruces de cadena con proyecto y de día con horario.',
     'Exportación a planilla.']},
     {'demo': [{'t': 'Ver la presentación del rastreo', 'href': 'https://projetos.75lab.com.br/rastreamento-75lab/'}]}]},
  ],
  'faq': [
   {'q': '¿Cómo rastrear material de PDV?', 'a': 'La forma más simple es un QR en cada pieza conectado a una página de montaje. Al instalar, el promotor registra tienda, foto y ubicación, y cada registro se convierte en un punto en el panel de la marca.'},
   {'q': '¿El promotor tiene que instalar una aplicación?', 'a': 'No. El QR abre una página en el navegador del celular. El registro pide nombre, tienda y la ubicación del equipo.'},
   {'q': '¿El cliente puede seguir el avance sin entrar al panel?', 'a': 'Sí. La marca genera un link público por campaña, en vivo y sin login, con vencimiento y elección de lo que aparece, como fotos y nombre de los promotores.'},
   {'q': '¿Funciona con piezas que la 75 LAB no produjo?', 'a': 'Sí. El QR y la página de montaje se pueden aplicar a cualquier pieza de la campaña, siempre que la etiqueta vaya en la pieza o en el embalaje antes del envío.'},
  ],
  'relacionados': [('Kit y material de PDV (en portugués)', 'enxoval-de-pdv.html'), ('Exhibidor de PDV', 'es/exhibidor-pdv.html'),
                   ('Realidad aumentada para PDV', 'es/realidad-aumentada-pdv.html'), ('Guías de PDV (en portugués)', 'guias.html')],
 },
 {
  'slug': 'es/caso-ngv-exhibidor-universal', 'cliente': 'NGV', 'imagem': '/img/cases/og-ngv.jpg', 'imagem_og': '/img/cases/og-ngv.jpg',
  'titulo_seo': 'Caso NGV: un exhibidor para cuatro marcas, en AR · 75 LAB',
  'descricao': 'Exhibidor Universal adaptado para Vitalitabs, De Llares, Bella Fio y Savedent, isla de cuatro caras y stand Conexão Farma, todo en realidad aumentada.',
  'eyebrow': 'Caso · NGV', 'migalhas': [CAS, ('NGV', None)],
  'h1': 'NGV: un exhibidor, **cuatro marcas**.',
  'lead': 'Un mismo módulo de exhibidor atiende a cuatro marcas, cada una con su comunicación y sus herrajes. Juntos, los módulos se convierten en una isla de cuatro caras.',
  'resumo': 'Para NGV, la 75 LAB adaptó el Exhibidor Universal a las marcas Vitalitabs, De Llares, Bella Fio y Savedent. La estructura es la misma; cambian el arte y los herrajes, con estantes para unas y ganchos para otras. Cuatro módulos forman una isla de 112 × 112 × 170 cm con una marca por cara. Todo se publicó en realidad aumentada, junto con el stand de NGV para Conexão Farma.',
  'secoes': [
   {'h2': 'El desafío', 'blocos': [{'p': 'Cuatro marcas de categorías distintas necesitaban presencia en el punto de venta (PDV) sin cuatro proyectos, cuatro moldes y cuatro proveedores. Y cada producto pide una exhibición diferente: el frasco va en estante, el blíster va en gancho.'}]},
   {'h2': 'Lo que hizo la 75 LAB', 'blocos': [
     {'fichas': [['62 × 65', 'cm por módulo'], ['170 cm', 'de altura'], ['112 × 112', 'cm en la isla'], ['4', 'marcas']]},
     {'lista': ['**Un módulo, cuatro comunicaciones:** cada marca con su arte y su frase.',
                '**Herrajes según el producto:** Vitalitabs y De Llares con estantes; Bella Fio y Savedent con regletas de ganchos de arriba abajo.',
                '**Isla de cuatro caras**, una marca por cara, armada con los mismos módulos.',
                '**Página de producto con QR** para quien monta, sin contraseña.',
                '**Stand Conexão Farma** en AR y en modo inmersivo, para recorrerlo antes de construirlo.']},
     {'galeria': [{'img': 'img/cases/ngv-vitalitabs.webp', 'leg': 'Vitalitabs', 'href': AR + 'ngv-displays/?modelo=vitalitabs'},
                  {'img': 'img/cases/ngv-dellares.webp', 'leg': 'De Llares', 'href': AR + 'ngv-displays/?modelo=dellares'},
                  {'img': 'img/cases/ngv-bellafio.webp', 'leg': 'Bella Fio', 'href': AR + 'ngv-displays/?modelo=bellafio'},
                  {'img': 'img/cases/ngv-savedent.webp', 'leg': 'Savedent', 'href': AR + 'ngv-displays/?modelo=savedent'},
                  {'img': 'img/cases/ngv-ilha.webp', 'leg': 'Isla de cuatro marcas', 'href': AR + 'ngv-displays/?modelo=ilha'},
                  {'img': 'img/cases/ngv-stand.webp', 'leg': 'Stand Conexão Farma', 'href': AR + 'ngv-stand-conexao-farma/'}]},
     {'demo': [{'t': 'Abrir los exhibidores en AR', 'href': AR + 'ngv-displays/'}, {'t': 'Página de producto', 'href': 'https://projetos.75lab.com.br/produtos/ngv-displays/'}]}]},
   {'h2': 'Por qué un exhibidor modular', 'blocos': [{'p': 'Con un solo módulo, la marca negocia una estructura, aprueba un proyecto de ingeniería y cambia solo la comunicación en cada campaña o marca. La isla nace de los mismos módulos, sin molde nuevo.'}]},
  ],
  'relacionados': [('Isla y cabecera de góndola (en portugués)', 'ilha-e-ponta-de-gondola.html'), ('Stands (en portugués)', 'estandes.html')] + REL_CASES,
 },
 {
  'slug': 'es/caso-semp-split-hw', 'cliente': 'SEMP', 'imagem': '/img/cases/og-semp.jpg', 'imagem_og': '/img/cases/og-semp.jpg',
  'titulo_seo': 'Caso SEMP: kit de PDV del Split HW en AR · 75 LAB',
  'descricao': 'El kit de PDV del aire acondicionado SEMP Split HW, con 15 piezas, en realidad aumentada, con página de montaje y contenido enriquecido para marketplace.',
  'eyebrow': 'Caso · SEMP', 'migalhas': [CAS, ('SEMP', None)],
  'h1': 'SEMP: 15 piezas de PDV, **todas en AR**.',
  'lead': 'El kit del aire acondicionado Split HW, del pórtico a la alfombra de piso, en una sola página de realidad aumentada, con página de montaje y contenido enriquecido para el marketplace.',
  'resumo': '75 LAB llevó a la realidad aumentada el kit de punto de venta (PDV) del aire acondicionado SEMP Split HW: 15 piezas en una sola página, que se pueden ver una por una, todas juntas o en tamaño real. El mismo material se convirtió en página de montaje con QR para la tienda y en contenido enriquecido para la página del producto en el marketplace.',
  'secoes': [
   {'h2': 'El desafío', 'blocos': [{'p': 'La línea blanca vende con demostración y con espacio grande en la tienda. Un kit de 15 piezas tiene que entenderse como conjunto, por quien aprueba y por quien monta, y la misma historia tiene que continuar en el e-commerce.'}]},
   {'h2': 'Lo que hizo la 75 LAB', 'blocos': [
     {'lista': ['**15 piezas en AR**: pórtico, backdrop, isla premium, cuna, cubo, póster y faja, regleta, placa de especificaciones, topper, oreja, cabezal, lamá (panel curvo de pie), comunicación aérea, alfombra de piso y póster de caja.',
                '**Vitrina de piezas** para presentar el kit: una pieza a la vez, todas en grilla o en tamaño real para comparar.',
                '**Piezas planas en AR de pared**, como placa, topper y oreja aplicadas en el equipo.',
                '**Página de montaje con QR** para todo el kit.',
                '**Contenido enriquecido** para la página del producto en el marketplace.']},
     {'galeria': [{'img': 'img/cases/semp-portico.webp', 'leg': 'Pórtico', 'href': AR + 'semp-split-hw/?modelo=portico'},
                  {'img': 'img/cases/semp-ilha.webp', 'leg': 'Isla premium', 'href': AR + 'semp-split-hw/?modelo=ilha'},
                  {'img': 'img/cases/semp-backdrop.webp', 'leg': 'Backdrop', 'href': AR + 'semp-split-hw/?modelo=backdrop'},
                  {'img': 'img/cases/semp-cubo.webp', 'leg': 'Cubo', 'href': AR + 'semp-split-hw/?modelo=cubo'},
                  {'img': 'img/cases/semp-berco.webp', 'leg': 'Cuna', 'href': AR + 'semp-split-hw/?modelo=berco'},
                  {'img': 'img/cases/semp-lama.webp', 'leg': 'Lamá', 'href': AR + 'semp-split-hw/'}]},
     {'demo': [{'t': 'Abrir el kit en AR', 'href': AR + 'semp-split-hw/'}, {'t': 'Ver la vitrina de piezas', 'href': AR + 'semp-split-hw/embed.html'}]}]},
  ],
  'relacionados': [('Kit y material de PDV (en portugués)', 'enxoval-de-pdv.html'),
                   ('Contenido enriquecido para e-commerce (en portugués)', 'conteudo-rico-ecommerce.html')] + REL_CASES,
 },
]
