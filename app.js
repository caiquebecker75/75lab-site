(function(){
  var reduce=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  var yrEl=document.getElementById('yr');if(yrEl)yrEl.textContent=new Date().getFullYear();
  // destacar link da página atual
  (function(){var f=(location.pathname.split('/').pop()||'index.html');if(!f)f='index.html';document.querySelectorAll('.nav-links a.lk').forEach(function(a){var h=a.getAttribute('href')||'';if(h===f||(f==='index.html'&&(h==='index.html'||h==='./'||h==='/'))){a.classList.add('current');}});})();

  (function(){var L=document.getElementById('loader'),bar=document.getElementById('lbar'),pct=document.getElementById('lpct');function ready(){document.body.classList.add('ready');}function finish(){document.body.classList.remove('loading');L.classList.add('done');ready();setTimeout(function(){L.style.display='none';},1000);}if(reduce){document.body.classList.remove('loading');L.style.display='none';ready();return;}var p=0;var iv=setInterval(function(){p+=Math.random()*16+7;if(p>=100){p=100;clearInterval(iv);}bar.style.width=p+'%';pct.textContent=Math.floor(p);if(p>=100)setTimeout(finish,240);},85);})();

  var hdr=document.getElementById('hdr'),prog=document.getElementById('progress');
  function onScroll(){hdr.classList.toggle('solid',window.scrollY>40);var h=document.documentElement;prog.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight||1)*100)+'%';}
  onScroll();window.addEventListener('scroll',onScroll,{passive:true});

  var burger=document.getElementById('burger'),links=document.getElementById('navlinks');
  burger.addEventListener('click',function(){links.classList.toggle('open');});
  links.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){links.classList.remove('open');});});

  (function(){var nodes=document.getElementById('nodes'),edges=document.getElementById('edges');if(!nodes)return;var cx=230,cy=180,R=128,labels=['Estratégia','Design','Produção','Dados','Logística','Criação'],pts=[];for(var i=0;i<6;i++){var a=(Math.PI*2/6)*i-Math.PI/2;pts.push([cx+Math.cos(a)*R,cy+Math.sin(a)*R]);}var eh='';pts.forEach(function(p){eh+='<line x1="'+cx+'" y1="'+cy+'" x2="'+p[0]+'" y2="'+p[1]+'" class="flow" stroke-dasharray="6 8"/>';});edges.innerHTML=eh;var h='<circle cx="'+cx+'" cy="'+cy+'" r="34" fill="#050505" class="pulse" style="transform-box:fill-box;transform-origin:'+cx+'px '+cy+'px"/><text x="'+cx+'" y="'+(cy+6)+'" text-anchor="middle" font-family="Big Shoulders Display" font-weight="900" font-size="26" fill="#C0EE4E">75</text>';pts.forEach(function(p,i){h+='<circle cx="'+p[0]+'" cy="'+p[1]+'" r="20" fill="#050505" class="twinkle" style="animation-delay:'+(i*0.3)+'s"/>';h+='<text x="'+p[0]+'" y="'+(p[1]+34)+'" text-anchor="middle" font-family="Space Mono" font-size="10" font-weight="700" fill="#050505">'+labels[i].toUpperCase()+'</text>';});nodes.innerHTML=h;})();

  (function(){var s=document.getElementById('dotgrid');if(!s)return;var h='';for(var r=0;r<6;r++)for(var c=0;c<6;c++){var on=(r*6+c)<34;h+='<circle cx="'+(18+c*17)+'" cy="'+(18+r*17)+'" r="4" fill="'+(on?'#C0EE4E':'rgba(242,241,233,.18)')+'" '+(on?'class="twinkle" style="animation-delay:'+(((r+c)%5)*0.2)+'s"':'')+'/>';}s.innerHTML=h;})();

  function runCount(el){var t=parseFloat(el.getAttribute('data-target'))||0,suf=el.getAttribute('data-suffix')||'',dur=1400,st=null;function step(ts){if(!st)st=ts;var p=Math.min((ts-st)/dur,1),e=1-Math.pow(1-p,3);el.textContent=Math.round(t*e).toLocaleString('pt-BR')+suf;if(p<1)requestAnimationFrame(step);}requestAnimationFrame(step);}
  if('IntersectionObserver' in window){var ioc=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){if(!e.target.dataset.done){e.target.dataset.done=1;runCount(e.target);}ioc.unobserve(e.target);}});},{threshold:0.4});document.querySelectorAll('.count').forEach(function(el){ioc.observe(el);});}

  document.querySelectorAll('#mpanels .mpanel').forEach(function(p){p.addEventListener('click',function(){document.querySelectorAll('#mpanels .mpanel').forEach(function(x){x.classList.remove('open');});p.classList.add('open');});});

  (function(){var sc=document.getElementById('casesScroller');if(!sc)return;var down=false,sx=0,sl=0;sc.addEventListener('mousedown',function(e){down=true;sc.classList.add('drag');sx=e.pageX;sl=sc.scrollLeft;});window.addEventListener('mouseup',function(){down=false;sc.classList.remove('drag');});sc.addEventListener('mouseleave',function(){down=false;sc.classList.remove('drag');});sc.addEventListener('mousemove',function(e){if(!down)return;e.preventDefault();sc.scrollLeft=sl-(e.pageX-sx)*1.5;});})();

  var mq=[].slice.call(document.querySelectorAll('[data-marquee]'));
  if(!reduce&&mq.length){var ly=scrollY,vel=0;addEventListener('scroll',function(){var y=scrollY;vel=Math.max(-90,Math.min(90,y-ly));ly=y;},{passive:true});mq.forEach(function(m){var tr=m.querySelector('.ticker-track'),base=parseFloat(m.getAttribute('data-speed'))||0.1,pos=0,half=0;function meas(){half=tr.scrollWidth/2;}meas();addEventListener('resize',meas);function loop(){var b=1+Math.min(Math.abs(vel)/12,4);pos-=base*b;if(half&&-pos>=half)pos+=half;var sk=Math.max(-6,Math.min(6,vel*0.13));tr.style.transform='translateX('+pos+'px) skewX('+sk+'deg)';vel*=0.9;requestAnimationFrame(loop);}loop();});}

  (function(){var dex=document.getElementById('sidedex');if(!dex)return;var ids=['top','porque','metodo','impacto','cases','midia','contato'];var dark={top:1,metodo:1,impacto:1,cases:1,contato:1};var anchors=[].slice.call(dex.querySelectorAll('a'));var secs=ids.map(function(k){return document.getElementById(k);}).filter(Boolean);if('IntersectionObserver' in window){var so=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var id=e.target.id;anchors.forEach(function(a){a.classList.toggle('active',a.getAttribute('data-sec')===id);});dex.classList.toggle('on-dark',!!dark[id]);}});},{rootMargin:'-50% 0px -50% 0px'});secs.forEach(function(s){so.observe(s);});}})();

  if(!reduce&&matchMedia('(hover:hover) and (pointer:fine)').matches){document.querySelectorAll('[data-magnetic]').forEach(function(b){b.addEventListener('mousemove',function(e){var r=b.getBoundingClientRect();b.style.transform='translate('+((e.clientX-r.left-r.width/2)*0.3)+'px,'+((e.clientY-r.top-r.height/2)*0.4)+'px)';});b.addEventListener('mouseleave',function(){b.style.transform='';});});}

  var cur=document.getElementById('cursor'),ctxt=document.getElementById('ctxt');
  if(cur&&!reduce&&matchMedia('(hover:hover) and (pointer:fine)').matches){var x=0,y=0,tx=0,ty=0;addEventListener('mousemove',function(e){tx=e.clientX;ty=e.clientY;});(function l(){x+=(tx-x)*.22;y+=(ty-y)*.22;cur.style.transform='translate('+x+'px,'+y+'px) translate(-50%,-50%)';requestAnimationFrame(l);})();document.querySelectorAll('a,button,.pf-card,.press,.post,input,textarea,.logo-cell,.mpanel,.ent').forEach(function(el){el.addEventListener('mouseenter',function(){cur.classList.add('big');});el.addEventListener('mouseleave',function(){cur.classList.remove('big');});});document.querySelectorAll('[data-cursor]').forEach(function(el){el.addEventListener('mouseenter',function(){cur.classList.remove('big');cur.classList.add('label');ctxt.textContent=el.getAttribute('data-cursor');});el.addEventListener('mouseleave',function(){cur.classList.remove('label');ctxt.textContent='';});});}else if(cur){cur.style.display='none';}

  var sendBtn=document.getElementById('send');
  if(sendBtn)sendBtn.addEventListener('click',function(){var g=function(id){return (document.getElementById(id).value||'').trim();};var emp=g('empresa'),nome=g('nome');var s=encodeURIComponent('[Briefing 75 LAB] '+(emp||nome||'Novo contato'));var b=encodeURIComponent('Nome: '+nome+'\nEmpresa: '+emp+'\nE-mail: '+g('email')+'\n\nIntenção comercial:\n'+g('msg'));location.href='mailto:contato@75lab.com.br?subject='+s+'&body='+b;});

  // ===== FX engine: entrada + saída de tela =====
  function fallbackShow(){document.querySelectorAll('.fx').forEach(function(el){el.classList.add('shown');});document.querySelectorAll('.fxstag').forEach(function(el){el.classList.add('shown');});}
  window.addEventListener('load',function(){
    var lenis=null;
    if(!reduce&&typeof Lenis!=='undefined'){try{lenis=new Lenis({lerp:0.075,smoothWheel:true});window.__lenis=lenis;}catch(e){lenis=null;}}
    var hasG=!reduce&&window.gsap&&window.ScrollTrigger;
    if(hasG){
      gsap.registerPlugin(ScrollTrigger);
      if(lenis){lenis.on('scroll',function(){ScrollTrigger.update();onScroll();});gsap.ticker.add(function(t){lenis.raf(t*1000);});gsap.ticker.lagSmoothing(0);}
      function fromV(el){var d=el.getAttribute('data-fx')||'up';if(d==='left')return{opacity:0,xPercent:-12,x:-40};if(d==='right')return{opacity:0,xPercent:12,x:40};if(d==='scale')return{opacity:0,scale:.86};return{opacity:0,y:70};}
      function outV(el){var d=el.getAttribute('data-fx')||'up';if(d==='left')return{opacity:0,xPercent:10,x:30};if(d==='right')return{opacity:0,xPercent:-10,x:-30};if(d==='scale')return{opacity:0,scale:1.12};return{opacity:0,y:-70};}
      gsap.utils.toArray('.fx').forEach(function(el){
        var fv=fromV(el);
        gsap.timeline({scrollTrigger:{trigger:el,start:'top bottom',end:'bottom top',scrub:true}})
          .fromTo(el,fv,{opacity:1,x:0,y:0,xPercent:0,scale:1,ease:'none',duration:.32})
          .to(el,{opacity:1,duration:.36})
          .to(el,Object.assign({ease:'none',duration:.32},outV(el)));
      });
      gsap.utils.toArray('.fxstag').forEach(function(grid){
        var kids=grid.children;
        gsap.set(kids,{opacity:0,y:60});
        gsap.timeline({scrollTrigger:{trigger:grid,start:'top 88%',end:'top 42%',scrub:true}}).to(kids,{opacity:1,y:0,stagger:.06,ease:'none'});
        gsap.timeline({scrollTrigger:{trigger:grid,start:'bottom 38%',end:'bottom top',scrub:true}}).to(kids,{opacity:0,y:-50,stagger:.04,ease:'none'});
      });
      if(lenis){requestAnimationFrame(function r(t){lenis.raf(t);requestAnimationFrame(r);});}
      setTimeout(function(){ScrollTrigger.refresh();},300);
    }else{
      if(lenis){(function rl(t){lenis.raf(t);requestAnimationFrame(rl);})();lenis.on('scroll',onScroll);}
      if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('shown');if(e.target.classList.contains('fxstag'))Array.prototype.forEach.call(e.target.children,function(c,i){c.style.transitionDelay=(i*0.06)+'s';});io.unobserve(e.target);}});},{threshold:0.12});document.querySelectorAll('.fx,.fxstag').forEach(function(el){io.observe(el);});}else{fallbackShow();}
    }
    document.querySelectorAll('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(ev){if(a.hasAttribute('data-id'))return;var id=a.getAttribute('href');if(id.length<2)return;var el=document.querySelector(id);if(!el)return;ev.preventDefault();if(lenis)lenis.scrollTo(el,{offset:-60});else el.scrollIntoView({behavior:'smooth'});});});
  });
  setTimeout(function(){if(!window.gsap&&!document.querySelector('.fx.shown')){fallbackShow();}},2500);

  // filtro da pagina de cases
  (function(){var fb=[].slice.call(document.querySelectorAll('[data-filter]'));if(!fb.length)return;var rows=[].slice.call(document.querySelectorAll('[data-cat]'));fb.forEach(function(b){b.addEventListener('click',function(){fb.forEach(function(x){x.classList.remove('active');});b.classList.add('active');var f=b.getAttribute('data-filter');rows.forEach(function(r){var ok=(f==='all'||r.getAttribute('data-cat')===f);r.style.display=ok?'':'none';});if(window.ScrollTrigger){try{ScrollTrigger.refresh();}catch(e){}}});});})();

  // infografico interativo (hub de solucoes)
  (function(){
    var stage=document.getElementById('hubstage');var panel=document.getElementById('hubpanel');var chips=document.getElementById('hubchips');
    if(!stage||!panel)return;
    var I={
      ev:'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M16 4v5M16 23v5M4 16h5M23 16h5M8 8l3.2 3.2M20.8 20.8L24 24M24 8l-3.2 3.2M11.2 20.8L8 24"/><circle cx="16" cy="16" r="3.6"/></svg>',
      st:'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"><path d="M7 13h18v12H7z"/><path d="M6 13l3-5h14l3 5"/></svg>',
      mt:'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"><rect x="7" y="11" width="18" height="14"/><path d="M7 16h18M12 11l4-5 4 5"/></svg>',
      nc:'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"><path d="M11 7h10v5a5 5 0 0 1-10 0z"/><path d="M11 9H7a4 4 0 0 0 4 5M21 9h4a4 4 0 0 1-4 5M16 17v5M12 25h8"/></svg>',
      pr:'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"><path d="M9 9h7l8 8-7 7-8-8z"/><path d="M15 20l5-5"/><circle cx="13" cy="13" r="1.3" fill="currentColor" stroke="none"/></svg>',
      rm:'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"><rect x="6" y="8" width="20" height="13" rx="1.5"/><path d="M14 12l5 2.5-5 2.5z" fill="currentColor" stroke="none"/><path d="M12 25h8M16 21v4"/></svg>',
      pm:'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.4"><circle cx="16" cy="12" r="4.4"/><path d="M8 26a8 8 0 0 1 16 0"/></svg>',
      pl:'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M16 9v14M9 16h14"/></svg>'
    };
    var data=[
      {k:'eventos',l:'Eventos',ic:I.ev,d:'Experiencias de marca que aproximam canal, shopper e equipe \u2014 do conceito a execucao.',t:['Convencoes','Ativacoes','Experiencias']},
      {k:'stand',l:'Stand',ic:I.st,d:'Presenca que chama atencao em feiras e eventos: projeto, producao e montagem.',t:['Projeto','Producao','Montagem']},
      {k:'pdv',l:'Material PDV',ic:I.mt,d:'O material certo na gondola \u2014 display, comunicacao e exposicao que convertem.',t:['Displays','Comunicacao','Exposicao']},
      {k:'incentivo',l:'Incentivo',ic:I.nc,d:'Engajamento de forca de vendas e canal com mecanicas que movem o resultado.',t:['Forca de vendas','Canal','Premiacao']},
      {k:'promocao',l:'Promocao',ic:I.pr,d:'Mecanicas promocionais que geram giro, experimentacao e sell-out.',t:['Sell-out','Giro','Experimentacao']},
      {k:'retail',l:'Retail media',ic:I.rm,d:'A sua marca nos canais de midia do varejo, dentro e fora da loja.',t:['Midia de varejo','In-store','Digital']},
      {k:'promotoria',l:'Promotoria',ic:I.pm,d:'Time de campo executando na ponta, com inteligencia e cobertura.',t:['Time de campo','Execucao','Cobertura']},
      {k:'mais',l:'+ Mais',ic:I.pl,d:'Nao achou? A gente pluga o especialista certo do hub para o seu desafio.',t:['Hub de parceiros','Sob medida']}
    ];
    var pos=[[88,50],[77,77],[50,88],[23,77],[12,50],[23,23],[50,12],[77,23]];
    var lines=stage.querySelector('.hublines');
    var lh='';data.forEach(function(d,i){lh+='<line data-k="'+d.k+'" x1="50" y1="50" x2="'+pos[i][0]+'" y2="'+pos[i][1]+'"></line>';});
    if(lines)lines.innerHTML=lh;
    data.forEach(function(d,i){var b=document.createElement('button');b.className='hubnode';b.setAttribute('data-k',d.k);b.setAttribute('aria-label',d.l);b.style.left=pos[i][0]+'%';b.style.top=pos[i][1]+'%';b.innerHTML='<span class="dot">'+d.ic+'</span><span>'+d.l+'</span>';stage.appendChild(b);});
    if(chips){var ch='';data.forEach(function(d){ch+='<button class="hubchip" data-k="'+d.k+'">'+d.l+'</button>';});chips.innerHTML=ch;}
    var map={};data.forEach(function(d){map[d.k]=d;});
    function activate(k){var d=map[k];if(!d)return;stage.querySelectorAll('.hubnode').forEach(function(n){n.classList.toggle('on',n.getAttribute('data-k')===k);});if(lines)lines.querySelectorAll('line').forEach(function(l){l.classList.toggle('on',l.getAttribute('data-k')===k);});if(chips)chips.querySelectorAll('.hubchip').forEach(function(n){n.classList.toggle('on',n.getAttribute('data-k')===k);});panel.innerHTML='<div class="pk"><i></i> Solucao plugada</div><h3>'+d.l+'</h3><p>'+d.d+'</p><div class="tags">'+d.t.map(function(x){return '<span>'+x+'</span>';}).join('')+'</div>';}
    stage.querySelectorAll('.hubnode').forEach(function(n){var k=n.getAttribute('data-k');n.addEventListener('mouseenter',function(){activate(k);});n.addEventListener('focus',function(){activate(k);});n.addEventListener('click',function(e){e.preventDefault();activate(k);});});
    if(chips)chips.querySelectorAll('.hubchip').forEach(function(n){n.addEventListener('click',function(){activate(n.getAttribute('data-k'));});});
    activate(data[0].k);
  })();


  // modal de case (pop-up com galeria + storytelling + big number)
  (function(){
    var modal=document.getElementById('caseModal');if(!modal)return;
    var dataEl=document.getElementById('casedata');var DATA={};
    try{JSON.parse(dataEl.textContent).forEach(function(c){DATA[c.id]=c;});}catch(e){}
    var gal=document.getElementById('modalGallery'),mTag=document.getElementById('mTag'),mBig=document.getElementById('mBig'),mBigL=document.getElementById('mBigL'),mTitle=document.getElementById('mTitle'),mProj=document.getElementById('mProj'),mStory=document.getElementById('mStory'),mObj=document.getElementById('mObj');
    function openCase(id){var c=DATA[id];if(!c)return;
      gal.innerHTML=(c.ph||[]).map(function(f){return '<img loading="lazy" src="img/'+f+'" alt="'+c.cli+'">';}).join('');
      mTag.textContent=c.tag;mBig.textContent=c.big;mBigL.textContent=c.bigl;mTitle.textContent=c.cli;mProj.textContent=c.proj||'';if(mObj)mObj.textContent=c.obj||'';mStory.textContent=c.story;
      modal.classList.add('open');modal.setAttribute('aria-hidden','false');document.body.style.overflow='hidden';
      if(window.__lenis){try{window.__lenis.stop();}catch(e){}}
      var mm=modal.querySelector('.modal-media');if(mm)mm.scrollTop=0;
    }
    function closeCase(){modal.classList.remove('open');modal.setAttribute('aria-hidden','true');document.body.style.overflow='';if(window.__lenis){try{window.__lenis.start();}catch(e){}}}
    document.addEventListener('click',function(e){var a=e.target&&e.target.closest?e.target.closest('.ccard[data-id]'):null;if(a){e.preventDefault();openCase(a.getAttribute('data-id'));}});
    modal.querySelectorAll('[data-close]').forEach(function(b){b.addEventListener('click',closeCase);});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'||e.keyCode===27)closeCase();});
  })();


  // vídeos: clicar para incorporar (data-embed = link de embed do YouTube/Vimeo)
  (function(){
    var vids=[].slice.call(document.querySelectorAll('.vfeature[data-embed],.vcard[data-embed]'));
    if(!vids.length)return;
    function play(el){
      var u=el.getAttribute('data-embed');
      if(!u){return;}
      var sep=u.indexOf('?')>-1?'&':'?';
      el.innerHTML='<iframe src="'+u+sep+'autoplay=1" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe>';
    }
    vids.forEach(function(el){
      el.addEventListener('click',function(){play(el);});
      el.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();play(el);}});
    });
  })();


  // camada cinematográfica (grão de filme + vinheta + luz que segue o cursor)
  (function(){
    if(document.querySelector('.cine-grain'))return;
    ['cine-grain','cine-vignette','cine-spot'].forEach(function(c){
      var d=document.createElement('div');d.className='cine '+c;d.setAttribute('aria-hidden','true');document.body.appendChild(d);
    });
    var spot=document.querySelector('.cine-spot');
    if(spot && window.matchMedia('(hover:hover) and (pointer:fine)').matches){
      window.addEventListener('pointermove',function(e){
        spot.style.setProperty('--mx', e.clientX+'px');
        spot.style.setProperty('--my', e.clientY+'px');
      },{passive:true});
    }
  })();


  // parallax de profundidade (sem conflitar com hover/scale)
  (function(){
    if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var items=[];
    document.querySelectorAll('.hero-float svg').forEach(function(el,i){ items.push({el:el,type:'t',sp:[34,-24,18,-28][i%4]}); });
    document.querySelectorAll('.vfeature .vthumb,.vcard .vthumb').forEach(function(el){ items.push({el:el,type:'bg',sp:10}); });
    if(!items.length) return;
    var H=window.innerHeight, vis=new Set(), map=new Map();
    items.forEach(function(it){ map.set(it.el,it); });
    var io=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting) vis.add(e.target); else vis.delete(e.target); }); },{rootMargin:'140px 0px'});
    items.forEach(function(it){ io.observe(it.el); });
    function frame(){
      if(vis.size){
        vis.forEach(function(el){
          var it=map.get(el); if(!it) return;
          var r=el.getBoundingClientRect();
          var prog=((r.top + r.height/2) - H/2)/H;
          var amt=prog*it.sp;
          if(it.type==='t'){ el.style.transform='translate3d(0,'+(-amt)+'px,0)'; }
          else if(it.type==='op'){ el.style.objectPosition='50% '+(50+amt)+'%'; }
          else if(it.type==='bg'){ el.style.backgroundPosition='50% '+(50+amt)+'%'; }
        });
      }
      requestAnimationFrame(frame);
    }
    window.addEventListener('resize', function(){ H=window.innerHeight; }, {passive:true});
    requestAnimationFrame(frame);
  })();

})();
