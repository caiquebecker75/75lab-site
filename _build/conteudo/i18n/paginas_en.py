"""English versions (served under /en/) of the 75 LAB service and case pages.
Same structure as _build/conteudo/servicos.py and cases.py. Rules: only facts that are in the
Portuguese originals, never an em or en dash, markup limited to [text](url) and **bold**.
Internal links point to the translated pages when they exist (en/...); otherwise to the
Portuguese page with no folder prefix, flagged "(in Portuguese)" in the link text."""

AR = 'https://projetos.75lab.com.br/ar/'
SOL = ('Solutions', '/solucoes.html')
CAS = ('Cases', '/cases.html')
REL_PADRAO = [('Augmented reality for POS', 'en/augmented-reality-pos.html'),
              ('POS material tracking', 'en/pos-material-tracking.html'),
              ('Detailed cases (in Portuguese)', 'cases.html#detalhados'),
              ('POS guides (in Portuguese)', 'guias.html')]
REL_CASES = [('POP display', 'en/pop-display.html'), ('Augmented reality for POS', 'en/augmented-reality-pos.html'),
             ('POS material tracking', 'en/pos-material-tracking.html'), ('All cases (in Portuguese)', 'cases.html')]


def g(n, leg):
    return {'img': f'img/g{n:02d}-1.jpg', 'leg': leg, 'href': 'cases.html'}


HOME = {
 'titulo_seo': 'Proven point of sale agency in São Paulo · 75 LAB',
 'descricao': '75 LAB designs and produces POP displays, islands, end caps, in-store kits and booths, approved in AR before production and tracked by QR code after install.',
 'eyebrow': 'Proven point-of-sale agency',
 'h1': 'A good idea is one that **happens**.',
 'lead': '75 LAB creates, engineers and produces displays, islands, in-store kits and booths, with proof at both ends: you see the display on your shelf in augmented reality before production, and you know where it is installed after it leaves the factory.',
 'resumo': '75 LAB is a point of sale (POS) and trade marketing agency based at CENU in São Paulo, founded in 2024 by Caique Becker, who came from retail, and Daniel Coimbra, who came from industry. It creates, engineers and produces POS material for consumer goods manufacturers: floor and counter displays, clip strips, promotional islands, end caps, launch kits and trade show booths. It works by project, with fixed scope, timeline and price.',
 'secoes': [
  {'h2': 'What 75 LAB does', 'blocos': [{'lista': [
    '[**POP display**](en/pop-display.html): floor, counter, clip strip and modular, with engineering and AR before production.',
    '[**Islands and end caps** (in Portuguese)](ilha-e-ponta-de-gondola.html): the most contested spaces in the store, approved in the aisle in AR.',
    '[**In-store kits** (in Portuguese)](enxoval-de-pdv.html): piece by piece, with an assembly page and a QR code on the packaging.',
    '[**Booths** (in Portuguese)](estandes.html): trade shows and events with an AR tour and immersive mode.',
    '[**Augmented reality**](en/augmented-reality-pos.html): the display at full scale in the store, on your phone, with no app.',
    '[**POS material tracking**](en/pos-material-tracking.html): QR code, photo and location, so you know where each piece was installed.',
    '[**Rich content, ClickLab** (in Portuguese)](conteudo-rico-ecommerce.html): the e-commerce product page treated as a brand piece.']}]},
  {'h2': 'How proven POS works', 'blocos': [{'passos': [
    '**Before production:** each piece is approved in augmented reality, at full scale, on the retailer\'s own shelf, on a phone. Marketing, trade, sales and the retail buyer approve by seeing the piece, not a PDF.',
    '**After installation:** the piece can carry a QR code that opens the assembly page and records the store, date, photo and location, on a dashboard the brand follows live.']}]},
  {'h2': 'Cases', 'blocos': [{'lista': [
    '[**NGV: one display, four brands**](en/case-ngv-universal-display.html). The Universal Display adapted for Vitalitabs, De Llares, Bella Fio and Savedent, a four-sided island and the Conexão Farma booth, all in AR.',
    '[**SEMP: 15 POS pieces, all in AR**](en/case-semp-split-hw.html). The Split HW air conditioner kit on a single augmented reality page, with an assembly page and rich content for the marketplace.',
    '[**All cases** (in Portuguese)](cases.html): Savencia, Alltak and the full portfolio.']}]},
 ],
}


PAGINAS = [
 {
  'slug': 'en/pop-display', 'servico': 'POP display design and production',
  'titulo_seo': 'POP display design and production for brands · 75 LAB',
  'descricao': 'Floor, counter, clip strip and modular POP displays for consumer brands, engineered, approved in augmented reality before production and tracked by QR in store.',
  'eyebrow': 'POP display', 'migalhas': [SOL, ('POP display', None)],
  'h1': 'POP displays for brands, from design to **store**.',
  'lead': 'We create, engineer and produce displays that stand up, hold the product and arrive assembled. Before production, you see the display at full scale on your own shelf, on your phone.',
  'resumo': '75 LAB handles the entire point-of-purchase (POP) display for the point of sale (POS): concept, engineering, production with approved suppliers, and delivery. The difference is proof at both ends: the display is approved in augmented reality, at full scale, before you spend on production, and each unit can ship with a QR code that records where and when it was installed.',
  'secoes': [
   {'h2': 'Types of displays we design', 'blocos': [{'lista': [
     '**Floor display**, freestanding, with shelves, peg hooks or trays.',
     '**Counter display** for checkout, pharmacy and impulse spots.',
     '**Clip strip** and peg bar for cross merchandising.',
     '**Modular display**, reused from campaign to campaign by changing only the graphics.',
     '**Gravity-feed display**, which restocks the product from the front.',
     '**Permanent fixture** and showcase, in MDF, metal or acrylic.']}]},
   {'h2': 'How a project runs', 'blocos': [{'passos': [
     '**Immersion:** product, weight, channel, store, budget and deadline. This is where the material gets decided.',
     '**Concept and render** with the brand\'s graphics applied.',
     '**Engineering:** technical drawings with views, dimensions, materials, thicknesses, load per shelf and tip-over stability.',
     '**Augmented reality approval:** a link opens the display at full scale on a phone, on the store floor or in the meeting room. Sales, trade and the buyer approve by seeing the unit, not a PDF.',
     '**Production** with suppliers approved by process (corrugated board, MDF, metal, acrylic, wire) and quality control.',
     '**Delivery and assembly**, with an assembly page and a QR code on the packaging for the installer, and an installation record with photo and location.']}]},
   {'h2': 'Why engineering comes before artwork', 'blocos': [
     {'p': 'A beautiful display that tips over, a shelf that sags under the product and a unit that needs tools to assemble are the most expensive rework in trade marketing, because they only show up in the store. That is why every 75 LAB display goes through technical drawings, with checks on load, stability, tool-free assembly and shipping, before it goes into production.'},
     {'p': 'To choose the material, see the guide [Corrugated board, MDF, metal, acrylic or wire (in Portuguese)](guia-material-display-pdv.html). To check stability, see [A display that does not tip over and a shelf that does not sag (in Portuguese)](guia-display-que-nao-tomba.html).'}]},
   {'h2': 'Displays we have delivered', 'blocos': [
     {'galeria': [g(20, 'Unilever · cash display'), g(48, 'O Boticário · modular display'), g(43, 'Kelco · modular display'),
                  g(16, 'Polenghi · retail and food'), g(38, 'Dako · retail display'), g(41, 'Loungerie · modular display')]},
     {'p': 'See them in augmented reality too:'},
     {'demo': [{'t': 'Frescatino clip strip in AR', 'href': AR + 'savencia-clipstrip-frescatino/'},
               {'t': 'NGV Universal Display in AR', 'href': AR + 'ngv-displays/'}]}]},
  ],
  'faq': [
   {'q': 'How long does a POP display project take?', 'a': 'It depends on the material, the quantity and the complexity of the unit. In the first conversation, 75 LAB sends back a schedule with the concept, engineering, AR approval, production and delivery stages, so you can plan the campaign backwards.'},
   {'q': 'Do I need a 3D file to see the display in augmented reality?', 'a': 'No. If your brand already has the 3D model, we convert it for AR. If not, the model is built as part of our project. The link opens in the browser on iPhone and Android, with no app to install.'},
   {'q': 'Does 75 LAB manufacture the display?', 'a': '75 LAB designs the display and coordinates production with a network of suppliers approved by process, with quality control and a single person in charge from brief to delivery. You hire a project, not a list of suppliers.'},
   {'q': 'Can the display be reused in another campaign?', 'a': 'Yes, when it is designed to be modular. The structure stays and only the graphics change. The Universal Display we adapted for four NGV brands is an example: the same module, with different artwork and hardware for each brand.'},
   {'q': 'How do I know the display was set up in the store?', 'a': 'Each unit can ship with a QR code. The installer opens the assembly page and records the store, a photo and the location, and the brand follows everything on a dashboard with a map. See [POS material tracking](en/pos-material-tracking.html).'},
  ],
  'relacionados': [('Islands and end caps (in Portuguese)', 'ilha-e-ponta-de-gondola.html'),
                   ('In-store kits and POS material (in Portuguese)', 'enxoval-de-pdv.html')] + REL_PADRAO,
 },
 {
  'slug': 'en/augmented-reality-pos', 'servico': 'Augmented reality for POS',
  'titulo_seo': 'Augmented reality for POS: see the display in store · 75 LAB',
  'descricao': 'See the display, island or booth at full scale in the store on your phone before production. Browser-based AR with no app, to approve and sell in the project.',
  'eyebrow': 'Augmented reality', 'migalhas': [SOL, ('Augmented reality for POS', None)],
  'h1': 'See the display in the store **before** you produce it.',
  'lead': 'Augmented reality in the browser, with no app: the display appears at full scale on the store floor, on the shelf or on the wall, on the phone of whoever needs to approve it.',
  'resumo': '75 LAB turns every point of sale (POS) project into an augmented reality link. Anyone who opens it on a phone sees the display, the island or the booth at full scale, right where it will stand. That shortens approval, avoids units that do not fit and helps sell the project to the retail buyer.',
  'secoes': [
   {'h2': 'How it works', 'blocos': [{'lista': [
     '**iPhone:** the link opens straight into the phone\'s native augmented reality.',
     '**Android:** the link opens in Google\'s AR viewer, also with no app.',
     '**Desktop:** the model appears in 3D so you can rotate it, with a QR code to continue on your phone.',
     'The unit appears **at full scale**, standing on the floor or mounted on the wall, depending on the type.']}]},
   {'h2': 'What it does for trade marketing, day to day', 'blocos': [{'lista': [
     '**Approve without a PDF:** marketing, trade and sales see the same unit to scale.',
     '**Sell in to retail:** the buyer sees the display in their own store before agreeing to the space.',
     '**Check dimensions:** height, depth and aisle, in the real location.',
     '**Train installers:** the assembly page shows the unit in AR next to the step by step instructions.']}]},
   {'h2': 'Projects published in AR', 'blocos': [
     {'p': 'More than 30 projects by 75 LAB have already been published in augmented reality, from clip strips to entire booths. A few you can open right now:'},
     {'galeria': [{'img': 'img/cases/savencia-clipstrip.webp', 'leg': 'Savencia · Frescatino clip strip', 'href': AR + 'savencia-clipstrip-frescatino/'},
                  {'img': 'img/cases/ngv-vitalitabs.webp', 'leg': 'NGV · Universal Display', 'href': AR + 'ngv-displays/'},
                  {'img': 'img/cases/semp-ilha.webp', 'leg': 'SEMP · Split HW in-store kit', 'href': AR + 'semp-split-hw/'},
                  {'img': 'img/cases/alltak-r05.webp', 'leg': 'Alltak · Revest Fácil booth', 'href': AR + 'alltak-stand-revest-facil/'}]}]},
   {'h2': 'Your display in AR within 48 business hours, free of charge', 'blocos': [
     {'p': 'For brands that want to see how it works: send us the product dimensions and the display idea on WhatsApp. Within 48 business hours we send back the link to the display in augmented reality, so you can open it in the store. One unit per brand, with no obligation to hire us.'},
     {'demo': [{'t': 'I want my display in AR', 'href': 'https://wa.me/5511986765634?text=' + 'I%20want%20my%20display%20in%20AR%20within%2048%20hours'}]}]},
  ],
  'faq': [
   {'q': 'Do I need to install an app to see the display in augmented reality?', 'a': 'No. The link opens in the browser on iPhone and Android and uses each system\'s native AR. On a computer, the 3D model appears with a QR code to open it on your phone.'},
   {'q': 'Does the display appear at full scale?', 'a': 'Yes. The unit opens at real scale, standing on the floor or mounted on the wall. With large booths you can pinch to shrink it and then go back to full scale.'},
   {'q': 'Do I need a 3D model?', 'a': 'No. If the brand already has the 3D file, we prepare it for AR. If not, the model is built as part of the 75 LAB project.'},
   {'q': 'On newer iPhones, part of the display disappears behind objects. Is that a defect?', 'a': 'No. iPhones with a LiDAR sensor hide the virtual unit behind real objects, such as a person or a box, and this cannot be turned off. Just clear the space in front of the camera.'},
  ],
  'cta': {'k': 'Offer for brands', 'h': 'Your display in AR within 48 business hours', 'p': 'Send the product dimensions and the idea. We send back the link to the display in augmented reality, free of charge.'},
  'relacionados': [('POP display', 'en/pop-display.html'), ('Booths (in Portuguese)', 'estandes.html'),
                   ('POS material tracking', 'en/pos-material-tracking.html'), ('POS guides (in Portuguese)', 'guias.html')],
 },
 {
  'slug': 'en/pos-material-tracking', 'servico': 'POS material tracking',
  'titulo_seo': 'POS material tracking with QR codes and a dashboard · 75 LAB',
  'descricao': 'Know where every display and POS piece was installed: a QR code on the piece, a record with photo and location, a map dashboard and a live link for your client.',
  'eyebrow': 'POS material tracking', 'migalhas': [SOL, ('POS material tracking', None)],
  'h1': 'Know where every point-of-sale piece was **installed**.',
  'lead': 'Point of sale (POS) material tends to leave the factory and vanish. With a QR code on the piece and a record at installation, the brand knows which store it went to, when, and how it was set up.',
  'resumo': '75 LAB tracks POS material with a QR code on every piece. The installer opens the assembly page and records the store with a photo and location, and the brand follows everything on a dashboard with a map, activated stores, installation pace and storefront photos. The client can get a live link, with no login.',
  'secoes': [
   {'h2': 'Why it matters', 'blocos': [
     {'p': 'Measuring the return on trade marketing is still the exception. In the Abratrade maturity survey released in November 2026, only 15.1% of professionals said they measure return in a standardized way ([Giro News](https://gironews.com/negocios/pesquisa-abratrade-aponta-baixa-maturidade-na-mensuracao-de-resultados-do-trade-marketing/), in Portuguese). Without knowing whether the piece was installed, there is no way to measure the rest.'}]},
   {'h2': 'How it works', 'blocos': [{'passos': [
     'Each piece ships with a **QR code** printed on the piece or on the packaging.',
     'The installer opens the **assembly page** and records name, store, a storefront photo and the phone\'s location.',
     'The record lands on a **dashboard** with a map, activated stores, daily pace, rankings by chain, city and state, and photos.',
     'The brand generates a **live link for the client** or for leadership, with no login, an expiry date and control over what is shown.']}]},
   {'h2': 'What the dashboard shows', 'blocos': [{'lista': [
     'Activated stores and coverage by chain, city and state.',
     'Installation pace, day by day and cumulative.',
     'Pieces installed per store, with a storefront photo.',
     'Cross views of chain by project and of day by time.',
     'Export to spreadsheet.']},
     {'demo': [{'t': 'See the tracking presentation', 'href': 'https://projetos.75lab.com.br/rastreamento-75lab/'}]}]},
  ],
  'faq': [
   {'q': 'How do you track POS material?', 'a': 'The simplest way is a QR code on each piece, linked to an assembly page. During installation, the field rep records the store, a photo and the location, and each record becomes a point on the brand\'s dashboard.'},
   {'q': 'Does the field rep need to install an app?', 'a': 'No. The QR code opens a page in the phone\'s browser. The record asks for name, store and the device\'s location.'},
   {'q': 'Can the client follow along without accessing the dashboard?', 'a': 'Yes. The brand generates a public link per campaign, live and with no login, with an expiry date and a choice of what appears, such as photos and the field reps\' names.'},
   {'q': 'Does it work for pieces 75 LAB did not produce?', 'a': 'Yes. The QR code and the assembly page can be applied to any piece in the campaign, as long as the label goes on the piece or the packaging before shipping.'},
  ],
  'relacionados': [('In-store kits and POS material (in Portuguese)', 'enxoval-de-pdv.html'), ('POP display', 'en/pop-display.html'),
                   ('Augmented reality for POS', 'en/augmented-reality-pos.html'), ('POS guides (in Portuguese)', 'guias.html')],
 },
 {
  'slug': 'en/case-ngv-universal-display', 'cliente': 'NGV', 'imagem': '/img/cases/og-ngv.jpg', 'imagem_og': '/img/cases/og-ngv.jpg',
  'titulo_seo': 'NGV case: one display for four brands, in AR · 75 LAB',
  'descricao': 'The Universal Display adapted for Vitalitabs, De Llares, Bella Fio and Savedent, a four-sided island and the Conexão Farma booth, all in augmented reality.',
  'eyebrow': 'Case · NGV', 'migalhas': [CAS, ('NGV', None)],
  'h1': 'NGV: one display, **four brands**.',
  'lead': 'A single display module serves four brands, each with its own graphics and its own hardware. Put together, the modules become a four-sided island.',
  'resumo': 'For NGV, 75 LAB adapted the Universal Display to the Vitalitabs, De Llares, Bella Fio and Savedent brands. The structure is the same; the artwork and the hardware change, with shelves for some and peg hooks for others. Four modules form a 112 × 112 × 170 cm island with one brand per side. Everything was published in augmented reality, together with the NGV booth for Conexão Farma.',
  'secoes': [
   {'h2': 'The challenge', 'blocos': [{'p': 'Four brands from different categories needed a presence at the point of sale (POS) without four projects, four molds and four suppliers. And each product calls for its own kind of display: bottles go on shelves, blister packs go on hooks.'}]},
   {'h2': 'What 75 LAB did', 'blocos': [
     {'fichas': [['62 × 65', 'cm per module'], ['170 cm', 'tall'], ['112 × 112', 'cm as an island'], ['4', 'brands']]},
     {'lista': ['**One module, four sets of graphics:** each brand with its own artwork and its own line.',
                '**Hardware by product:** Vitalitabs and De Llares with shelves; Bella Fio and Savedent with peg bars from top to bottom.',
                '**Four-sided island**, one brand per side, built from the same modules.',
                '**Product page with a QR code** for installers, with no password.',
                '**Conexão Farma booth** in AR and in immersive mode, to walk through before it is built.']},
     {'galeria': [{'img': 'img/cases/ngv-vitalitabs.webp', 'leg': 'Vitalitabs', 'href': AR + 'ngv-displays/?modelo=vitalitabs'},
                  {'img': 'img/cases/ngv-dellares.webp', 'leg': 'De Llares', 'href': AR + 'ngv-displays/?modelo=dellares'},
                  {'img': 'img/cases/ngv-bellafio.webp', 'leg': 'Bella Fio', 'href': AR + 'ngv-displays/?modelo=bellafio'},
                  {'img': 'img/cases/ngv-savedent.webp', 'leg': 'Savedent', 'href': AR + 'ngv-displays/?modelo=savedent'},
                  {'img': 'img/cases/ngv-ilha.webp', 'leg': 'Four-brand island', 'href': AR + 'ngv-displays/?modelo=ilha'},
                  {'img': 'img/cases/ngv-stand.webp', 'leg': 'Conexão Farma booth', 'href': AR + 'ngv-stand-conexao-farma/'}]},
     {'demo': [{'t': 'Open the displays in AR', 'href': AR + 'ngv-displays/'}, {'t': 'Product page', 'href': 'https://projetos.75lab.com.br/produtos/ngv-displays/'}]}]},
   {'h2': 'Why a modular display', 'blocos': [{'p': 'With a single module, the brand negotiates one structure, approves one engineering project and only swaps the graphics for each campaign or brand. The island is built from the same modules, with no new mold.'}]},
  ],
  'relacionados': [('Islands and end caps (in Portuguese)', 'ilha-e-ponta-de-gondola.html'), ('Booths (in Portuguese)', 'estandes.html')] + REL_CASES,
 },
 {
  'slug': 'en/case-semp-split-hw', 'cliente': 'SEMP', 'imagem': '/img/cases/og-semp.jpg', 'imagem_og': '/img/cases/og-semp.jpg',
  'titulo_seo': 'SEMP case: Split HW in-store kit in AR · 75 LAB',
  'descricao': 'The in-store kit for the SEMP Split HW air conditioner: 15 POS pieces in augmented reality, with an assembly page and rich content for the marketplace.',
  'eyebrow': 'Case · SEMP', 'migalhas': [CAS, ('SEMP', None)],
  'h1': 'SEMP: 15 point-of-sale pieces, **all in AR**.',
  'lead': 'The in-store kit for the Split HW air conditioner, from the archway to the floor mat, on a single augmented reality page, with an assembly page and rich content for the marketplace.',
  'resumo': '75 LAB brought the point of sale (POS) kit for the SEMP Split HW air conditioner into augmented reality: 15 pieces on a single page, which can be viewed one at a time, all together or at full scale. The same material became an assembly page with a QR code for the store and rich content for the product page on the marketplace.',
  'secoes': [
   {'h2': 'The challenge', 'blocos': [{'p': 'Major appliances sell through demonstration and through large spaces in the store. A 15-piece kit has to be understood as a set, by the people who approve it and the people who install it, and the same story has to carry on into e-commerce.'}]},
   {'h2': 'What 75 LAB did', 'blocos': [
     {'lista': ['**15 pieces in AR**: archway, backdrop, premium island, cradle, cube, poster and band, shelf strip, spec sign, topper, side tag, header, lamá (curved standing panel), ceiling hanger, floor mat and checkout poster.',
                '**Piece showcase** to present the kit: one piece at a time, all of them in a grid, or at full scale to compare.',
                '**Flat pieces in wall AR**, such as the sign, topper and side tag applied to the unit.',
                '**Assembly page with a QR code** for the entire kit.',
                '**Rich content** for the product page on the marketplace.']},
     {'galeria': [{'img': 'img/cases/semp-portico.webp', 'leg': 'Archway', 'href': AR + 'semp-split-hw/?modelo=portico'},
                  {'img': 'img/cases/semp-ilha.webp', 'leg': 'Premium island', 'href': AR + 'semp-split-hw/?modelo=ilha'},
                  {'img': 'img/cases/semp-backdrop.webp', 'leg': 'Backdrop', 'href': AR + 'semp-split-hw/?modelo=backdrop'},
                  {'img': 'img/cases/semp-cubo.webp', 'leg': 'Cube', 'href': AR + 'semp-split-hw/?modelo=cubo'},
                  {'img': 'img/cases/semp-berco.webp', 'leg': 'Cradle', 'href': AR + 'semp-split-hw/?modelo=berco'},
                  {'img': 'img/cases/semp-lama.webp', 'leg': 'Lamá', 'href': AR + 'semp-split-hw/'}]},
     {'demo': [{'t': 'Open the kit in AR', 'href': AR + 'semp-split-hw/'}, {'t': 'See the piece showcase', 'href': AR + 'semp-split-hw/embed.html'}]}]},
  ],
  'relacionados': [('In-store kits and POS material (in Portuguese)', 'enxoval-de-pdv.html'),
                   ('Rich content for e-commerce (in Portuguese)', 'conteudo-rico-ecommerce.html')] + REL_CASES,
 },
]
