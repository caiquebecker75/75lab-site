"""Avisa Bing/Copilot/ChatGPT (IndexNow) que URLs do site mudaram.
Uso: python3 _build/indexnow.py            -> todas as URLs do sitemap
     python3 _build/indexnow.py /guia-x.html /outra.html
Rodar DEPOIS do push (o arquivo da chave precisa estar no ar)."""
import json, re, sys, urllib.request, pathlib
RAIZ = pathlib.Path(__file__).resolve().parent.parent
CHAVE = "e650d5bb460475c496f3eb8dc35b60ac"
HOST = "75lab.com.br"
def urls():
    if len(sys.argv) > 1:
        return ["https://%s/%s" % (HOST, u.lstrip("/")) for u in sys.argv[1:]]
    return re.findall(r"<loc>(.*?)</loc>", (RAIZ / "sitemap.xml").read_text())
corpo = {"host": HOST, "key": CHAVE, "keyLocation": "https://%s/%s.txt" % (HOST, CHAVE), "urlList": urls()}
req = urllib.request.Request("https://api.indexnow.org/indexnow", json.dumps(corpo).encode(), {"Content-Type": "application/json; charset=utf-8"})
try:
    r = urllib.request.urlopen(req, timeout=30); print("IndexNow", r.status, len(corpo["urlList"]), "URLs")
except urllib.error.HTTPError as e:
    print("IndexNow erro", e.code, e.read()[:200]); sys.exit(1)
