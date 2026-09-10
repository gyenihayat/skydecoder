#!/usr/bin/env python3
"""kartlar/*.md dosyalarını okur, site/kartlar.json ve site/index.html üretir.

Kullanım:  python3 build.py
Bağımlılık yok (yalnızca standart kütüphane).
"""
import datetime as dt
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
KART_DIR = ROOT / "kartlar"
SITE_DIR = ROOT / "site"
TEMPLATE = ROOT / "template.html"

FIELDS = [
    ("kisa_tanim", "Kısa tanım"),
    ("esik", "Eşik / Formül"),
    ("nasil", "Nasıl çalışır"),
    ("ornek", "Günlük hayattan örnek"),
    ("hata", "Sık yapılan hata"),
    ("kaynaklar", "Kaynaklar"),
]
LABELS = {label: key for key, label in FIELDS}

CONSISTENCY = {"🟢": "yuksek", "🟡": "orta", "🔴": "dusuk"}
REVERIFY = [(re.compile(r"(\d+)\s*ayda bir"), 30)]

TR_MAP = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosucgiosu")


def slugify(text: str) -> str:
    text = text.translate(TR_MAP).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


# ---------- küçük Markdown -> HTML dönüştürücü ----------

def inline(text: str) -> str:
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(
        r"\x00(\d+)\x00",
        lambda m: f"<code>{html.escape(codes[int(m.group(1))], quote=False)}</code>",
        text,
    )
    return text


def render_table(lines):
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    if len(rows) >= 2 and all(re.fullmatch(r":?-{2,}:?", c) for c in rows[1]):
        head, body = rows[0], rows[2:]
    else:
        head, body = None, rows
    out = ['<div class="tablo"><table>']
    if head:
        out.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>")
    out.append("<tbody>")
    for r in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def md_to_html(text: str) -> str:
    lines = text.strip("\n").split("\n")
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.lstrip().startswith("|"):
            block = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                block.append(lines[i])
                i += 1
            out.append(render_table(block))
            continue
        m_ul = re.match(r"^\s*[-*]\s+(.*)", line)
        m_ol = re.match(r"^\s*\d+[.)]\s+(.*)", line)
        if m_ul or m_ol:
            tag = "ul" if m_ul else "ol"
            pat = r"^\s*[-*]\s+(.*)" if m_ul else r"^\s*\d+[.)]\s+(.*)"
            items = []
            while i < len(lines):
                m = re.match(pat, lines[i])
                if m:
                    items.append(m.group(1))
                    i += 1
                elif lines[i].startswith("  ") and items and lines[i].strip():
                    items[-1] += " " + lines[i].strip()  # girintili devam satırı
                    i += 1
                else:
                    break
            out.append(f"<{tag}>" + "".join(f"<li>{inline(it)}</li>" for it in items) + f"</{tag}>")
            continue
        para = []
        while i < len(lines) and lines[i].strip() and not lines[i].lstrip().startswith("|") \
                and not re.match(r"^\s*([-*]|\d+[.)])\s+", lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
    return "".join(out)


# ---------- kart ayrıştırma ----------

def parse_frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("["):
            meta[k.strip()] = json.loads(v)
        else:
            meta[k.strip()] = v.strip('"')
    return meta, text[m.end():]


def parse_consistency(quote_lines, guncelleme):
    joined = "\n".join(quote_lines)
    result = {"seviye": None, "simge": None, "not": "", "dogrulama": guncelleme,
              "celiski": "", "yeniden_dogrulama": None}
    m = re.search(r"\*\*Tutarlılık:\*\*\s*([🟢🟡🔴])\s*(\S+)\s*(?:\((.*?)\))?", joined)
    if m:
        result["simge"] = m.group(1)
        result["seviye"] = CONSISTENCY.get(m.group(1))
        result["seviye_adi"] = m.group(2)
        result["not"] = m.group(3) or ""
    m = re.search(r"Son doğrulama:\s*(\d{4}-\d{2}-\d{2})", joined)
    if m:
        result["dogrulama"] = m.group(1)
    m = re.search(r"Çelişki:\s*(.*)", joined)
    if m:
        c = m.group(1).strip()
        c = re.sub(r"^—\s*", "", c)
        c = re.sub(r"^\*\((.*)\)\*$", r"\1", c)  # şablondaki italik parantez
        result["celiski"] = inline(c) if c else ""
    for pat, unit in REVERIFY:
        mm = pat.search(joined)
        if mm:
            months = int(mm.group(1))
            base = dt.date.fromisoformat(result["dogrulama"])
            result["yeniden_dogrulama"] = (base + dt.timedelta(days=months * unit)).isoformat()
            result["yeniden_dogrulama_ay"] = months
    return result


def parse_card(title, body, meta, dosya, sira):
    fields = {k: [] for k, _ in FIELDS}
    quote = []
    current = None
    for line in body.split("\n"):
        if line.strip() == "---":
            continue
        m = re.match(r"^\*\*(.+?):\*\*\s*(.*)", line)
        if m and m.group(1) in LABELS:
            current = LABELS[m.group(1)]
            if m.group(2):
                fields[current].append(m.group(2))
            continue
        if line.startswith(">"):
            quote.append(line.lstrip("> ").rstrip())
            current = None
            continue
        if current:
            fields[current].append(line)
    kaynaklar = []
    for line in fields["kaynaklar"]:
        m = re.match(r"^\s*\d+[.)]\s+(.*)", line)
        if m:
            kaynaklar.append(inline(m.group(1)))
    return {
        "id": slugify(title),
        "baslik": title,
        "kategori": meta.get("kategori", ""),
        "kategori_id": slugify(meta.get("kategori", "")),
        "seviye": meta.get("seviye", ""),
        "etiketler": meta.get("etiketler", []),
        "dosya": dosya,
        "sira": sira,
        "kisa_tanim_duz": " ".join(l.strip() for l in fields["kisa_tanim"] if l.strip()),
        "alanlar": {k: md_to_html("\n".join(v)) for k, v in fields.items() if k != "kaynaklar"},
        "kaynaklar": kaynaklar,
        "tutarlilik": parse_consistency(quote, meta.get("guncelleme", "")),
    }


def parse_file(path: Path, order: int):
    meta, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    parts = re.split(r"^## +", body, flags=re.M)
    cards = []
    for i, part in enumerate(parts[1:]):
        title, _, rest = part.partition("\n")
        cards.append(parse_card(title.strip(), rest, meta, path.name, order * 100 + i))
    return meta, cards


def main():
    kategoriler, kartlar = [], []
    for n, path in enumerate(sorted(KART_DIR.glob("*.md"))):
        meta, cards = parse_file(path, n)
        kategoriler.append({
            "id": slugify(meta.get("kategori", "")),
            "ad": meta.get("kategori", ""),
            "seviye": meta.get("seviye", ""),
            "dosya": path.name,
            "kart_sayisi": len(cards),
        })
        kartlar.extend(cards)
    dogrulamalar = [k["tutarlilik"]["dogrulama"] for k in kartlar if k["tutarlilik"]["dogrulama"]]
    data = {
        "uretim": dt.datetime.now().isoformat(timespec="seconds"),
        "son_dogrulama": max(dogrulamalar) if dogrulamalar else None,
        "kategoriler": kategoriler,
        "kartlar": kartlar,
    }
    SITE_DIR.mkdir(exist_ok=True)
    (SITE_DIR / "kartlar.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    tpl = TEMPLATE.read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    (SITE_DIR / "index.html").write_text(tpl.replace("/*__VERI__*/null", payload), encoding="utf-8")
    print(f"{len(kartlar)} kart, {len(kategoriler)} kategori -> site/index.html")
    for k in kartlar:
        t = k["tutarlilik"]
        flag = f" yeniden:{t['yeniden_dogrulama']}" if t["yeniden_dogrulama"] else ""
        print(f"  {t['simge']} {k['kategori']:<26} {k['baslik'][:60]}{flag}")


if __name__ == "__main__":
    main()
