#!/usr/bin/env python3
import pathlib, sys
raiz = pathlib.Path(__file__).resolve().parents[1]
erros = []
def precisa(cond, msg):
    if not cond:
        erros.append(msg)
for slug, link in (("raissa", "https://t.me/+d4x8YLbSfxQ0ZTU8"), ("matheus", "https://t.me/+D76e2NFJbyFmYmQ0")):
    html = (raiz / slug / "index.html").read_text(encoding="utf-8")
    precisa("viewport" in html, f"{slug} sem viewport")
    precisa(link in html, f"{slug} sem link do Telegram")
    precisa("Entrar no Telegram" in html, f"{slug} sem botão")
    precisa("Maiores de 18" in html, f"{slug} sem aviso 18+")
    precisa("\u2014" not in html and "\u2013" not in html, f"{slug} tem travessão")
    precisa("<form" not in html, f"{slug} não pode ter formulário")
    for nome in ("perfil.jpg", "convite.jpg", "01.jpg", "06.jpg"):
        precisa((raiz / slug / "img" / nome).stat().st_size > 1000, f"{slug} imagem {nome} faltando")
home = (raiz / "index.html").read_text(encoding="utf-8")
precisa("raissa/" in home and "matheus/" in home, "home sem os dois links")
if erros:
    print("\n".join(erros))
    sys.exit(1)
print("ok")
