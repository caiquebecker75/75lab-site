import json, html
faq = [
 ("Quando começar o projeto de PDV de Páscoa 2027?", "A Páscoa 2027 é em 28 de março e o Carnaval em 9 de fevereiro. Como a área de Páscoa costuma subir logo depois do Carnaval, o ideal é fechar o briefing até a primeira semana de dezembro de 2026, aprovar o projeto antes do recesso de fim de ano e ter o lote entregue antes do Carnaval."),
 ("Quanto peso uma parreira de Páscoa carrega?", "Depende do produto, mas costuma ser muito mais do que parece. Multiplique o peso do ovo embalado pelos ovos por gancho, pelos ganchos por barra e pelo número de barras, e some 20% de folga. Um exemplo com ovo de 350 g, 6 por gancho, 10 ganchos e 4 barras passa de 100 kg de carga de projeto."),
 ("Qual o erro mais comum na parreira de Páscoa?", "Fazer a conta de carga com o peso líquido do chocolate em vez do peso do ovo embalado, com caixa e brinde. O segundo é usar a mesma parreira para lojas de tamanhos muito diferentes."),
 ("Como saber se a parreira foi montada em todas as lojas?", "Registrando cada montagem com loja, data e foto desde o primeiro dia, por exemplo com um QR na peça. Assim a lista de lojas sem montagem aparece em 48 horas, e não no fim da campanha."),
 ("O Kit Páscoa 2027 é pago?", "Não. O PDF é gratuito: você preenche nome, empresa e e-mail e baixa na hora."),
]
ld = [{"@type":"FAQPage","@id":"https://75lab.com.br/kit-pascoa-2027.html#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},
      {"@type":"HowTo","name":"Planejar o PDV de Páscoa 2027","inLanguage":"pt-BR","step":[
        {"@type":"HowToStep","name":"Fechar o briefing","text":"Até 04/12/2026: SKUs com peso embalado, lojas por perfil, medidas aceitas por rede e quem monta."},
        {"@type":"HowToStep","name":"Aprovar o projeto","text":"Até 18/12/2026: projeto 3D aprovado, de preferência visto em tamanho real na loja por realidade aumentada."},
        {"@type":"HowToStep","name":"Protótipo e teste de carga","text":"Até 15/01/2027: executivo, protótipo e teste com o produto real pendurado."},
        {"@type":"HowToStep","name":"Produzir e entregar","text":"Lote pronto até 05/02/2027 e entregue no CD ou nas lojas até 12/02/2027, antes do Carnaval."},
        {"@type":"HowToStep","name":"Implantar e conferir","text":"Implantação concluída até 06/03/2027, com registro de montagem por loja, e conferência semanal até a Páscoa em 28/03/2027."}]}]
meta = {"slug":"kit-pascoa-2027","titulo":"Kit Páscoa 2027 para trade marketing: cronograma, parreira e carga · 75 LAB",
 "descricao":"Planejamento do PDV de Páscoa 2027: cronograma reverso até 28/03, briefing da parreira, calculadora de carga e checklist de montagem. PDF grátis para baixar.",
 "prioridade":"0.9","migalhas":[["Guias","/guias.html"],["Kit Páscoa 2027","/kit-pascoa-2027.html"]],"ld":ld}
faqhtml = "\n".join(f'        <details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q,a in faq)
corpo = open(__import__('os').path.join(__import__('os').path.dirname(__file__),'kit_corpo.html'), encoding='utf-8').read().replace('{{FAQ}}', faqhtml)
out = '/Volumes/hd caique becker/Mac Caique/Projetos/75lab-site/_build/conteudo/livres/kit-pascoa-2027.html'
open(out,'w',encoding='utf-8').write('<!--'+json.dumps(meta,ensure_ascii=False)+'-->\n'+corpo)
print('ok')
