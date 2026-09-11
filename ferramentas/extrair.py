#!/usr/bin/env python
"""
Ferramentas de extracao do PDF de Bolfarine & Bussab, Elementos de
Amostragem (IME-USP, maio de 2004 -- a versao pre-print que circula em PDF;
o livro saiu depois pela Blucher, 2005).

O PDF e NATIVO, gerado por pdfTeX: a camada de texto existe, mas as fontes
de TeX gravam os ACENTOS SEPARADOS da letra ("S~ao", "Matem'atica", ",c~ao").
`limpar()` recompoe os acentos e as ligaturas (fi, fl); todo comando de texto
passa por ela. As formulas saem com as quebras de linha do TeX (fracoes e
somatorios empilhados), o que basta para localizar e conferir. As figuras
(poucas: tres no cap. 1) sao desenhos vetoriais ou diagramas em texto.

Uso:
  python extrair.py texto  13 48           -> imprime o texto das paginas 13..48 (numeracao do PDF)
  python extrair.py texto  --livro 1 36    -> idem, mas usando a numeracao impressa no livro
  python extrair.py pagina 22 saida.png    -> renderiza a pagina inteira como PNG
  python extrair.py recorte 22 80 120 520 600 saida.png   -> recorta uma regiao (x0 y0 x1 y1, em pontos)
  python extrair.py imagens 22 pasta/      -> extrai as imagens embutidas da pagina
  python extrair.py buscar "Horvitz"       -> lista as paginas onde o termo aparece
  python extrair.py sumario                -> imprime o sumario (bookmarks) do PDF, se houver

Offset: CONSTANTE. Pagina do PDF = pagina do livro + 12, em todo o volume
(o cap. 1 comeca na p. 1 do livro = p. 13 do PDF). Use `livro2pdf` /
`pdf2livro` mesmo assim, para o codigo continuar valendo se o PDF mudar.

No Windows, redirecionar a saida para arquivo exige PYTHONIOENCODING=utf-8.
"""
import sys
import os
import glob
import re
import unicodedata

import fitz  # PyMuPDF

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Localiza o PDF sozinho: o nome do arquivo pode mudar, a pasta nao.
_pdfs = sorted(glob.glob(os.path.join(RAIZ, "*.pdf")), key=os.path.getsize, reverse=True)
if not _pdfs:
    raise SystemExit(f"nenhum PDF encontrado em {RAIZ}")
_amostra = [p for p in _pdfs if "amostra" in os.path.basename(p).lower()]
PDF = (_amostra or _pdfs)[0]

OFFSET = 12          # pagina do PDF = pagina do livro + 12 (constante neste PDF)

# Acentos "soltos" das fontes de TeX -> acento combinante Unicode. O acento
# vem ANTES da letra no texto extraido; a NFC junta os dois num caractere so.
_ACENTOS = {
    "\u00b4": "\u0301",   # ´ agudo
    "\u02dc": "\u0303",   # ˜ til
    "\u02c6": "\u0302",   # ˆ circunflexo
    "\u00b8": "\u0327",   # ¸ cedilha
    "\u00a8": "\u0308",   # ¨ trema
    "\u0060": "\u0300",   # ` grave
}
_RE_ACENTO = re.compile("([" + "".join(map(re.escape, _ACENTOS)) + r"])(\w)")
_LIGATURAS = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi", "\ufb04": "ffl"}


def limpar(texto):
    """Recompoe os acentos separados pelo TeX e desfaz as ligaturas."""
    for lig, sub in _LIGATURAS.items():
        texto = texto.replace(lig, sub)
    texto = _RE_ACENTO.sub(lambda m: m.group(2) + _ACENTOS[m.group(1)], texto)
    # o "i sem pingo" das fontes de TeX nao compoe com o acento pela NFC
    texto = texto.replace("ı́", "í").replace("ı̂", "î")
    return unicodedata.normalize("NFC", texto)


def livro2pdf(p):
    """Pagina do livro -> pagina do PDF."""
    return p + OFFSET


def pdf2livro(n):
    """Pagina do PDF -> pagina do livro (None nas paginas preliminares)."""
    return n - OFFSET if n > OFFSET else None


def abrir():
    return fitz.open(PDF)


def cmd_texto(args):
    """Imprime o texto de um intervalo de paginas, com os acentos recompostos."""
    if args and args[0] == "--livro":
        args = args[1:]
        ini = livro2pdf(int(args[0]))
        fim = livro2pdf(int(args[1])) if len(args) > 1 else ini
    else:
        ini = int(args[0])
        fim = int(args[1]) if len(args) > 1 else ini
    doc = abrir()
    for n in range(ini, fim + 1):
        print(f"\n{'=' * 70}\n### PDF p.{n}  (livro p.{pdf2livro(n)})\n{'=' * 70}")
        print(limpar(doc[n - 1].get_text()))


def cmd_pagina(args):
    """Renderiza uma pagina inteira como PNG a 200 dpi."""
    n, saida = int(args[0]), args[1]
    doc = abrir()
    pix = doc[n - 1].get_pixmap(dpi=200)
    pix.save(saida)
    print(f"salvo: {saida}  ({pix.width}x{pix.height})")


def cmd_recorte(args):
    """Recorta uma regiao retangular da pagina em alta resolucao."""
    n = int(args[0])
    x0, y0, x1, y1 = (float(v) for v in args[1:5])
    saida = args[5]
    doc = abrir()
    rect = fitz.Rect(x0, y0, x1, y1)
    pix = doc[n - 1].get_pixmap(dpi=300, clip=rect)
    pix.save(saida)
    print(f"salvo: {saida}  ({pix.width}x{pix.height})")


def cmd_imagens(args):
    """Extrai as imagens embutidas de uma pagina."""
    n, pasta = int(args[0]), args[1]
    os.makedirs(pasta, exist_ok=True)
    doc = abrir()
    for i, info in enumerate(doc[n - 1].get_images(full=True)):
        xref = info[0]
        img = doc.extract_image(xref)
        caminho = os.path.join(pasta, f"p{n}_{i}.{img['ext']}")
        with open(caminho, "wb") as f:
            f.write(img["image"])
        print(f"salvo: {caminho}  ({img['width']}x{img['height']})")


def cmd_buscar(args):
    """Lista as paginas em que um termo aparece (busca no texto ja limpo)."""
    termo = limpar(args[0]).lower()
    doc = abrir()
    for n, page in enumerate(doc, start=1):
        if termo in limpar(page.get_text()).lower():
            print(f"PDF p.{n}  (livro p.{pdf2livro(n)})")


def cmd_sumario(args):
    """Imprime os bookmarks do PDF. Este PDF nao tem: use o Conteudo (PDF p. 3-7)."""
    doc = abrir()
    toc = doc.get_toc()
    if not toc:
        print("o PDF nao tem bookmarks; o sumario impresso esta nas paginas 3 a 7 do PDF")
        return
    for nivel, titulo, pagina in toc:
        print(f"{'  ' * (nivel - 1)}{titulo}  ->  PDF p.{pagina}  (livro p.{pdf2livro(pagina)})")


COMANDOS = {
    "texto": cmd_texto,
    "pagina": cmd_pagina,
    "recorte": cmd_recorte,
    "imagens": cmd_imagens,
    "buscar": cmd_buscar,
    "sumario": cmd_sumario,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMANDOS:
        print(__doc__)
        sys.exit(1)
    COMANDOS[sys.argv[1]](sys.argv[2:])
