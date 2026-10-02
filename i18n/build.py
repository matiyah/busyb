#!/usr/bin/env python3
"""
Build the localized copies of the home page.

    python3 i18n/build.py

index.html (English) is the source of truth. Every language page is that file
with its text swapped for the matching entry in i18n/tr_<lang>.py, and its asset
paths, store links and hreflang tags adjusted. Edit the English page, add or
change the matching entry in en.py and every tr_*.py (same order), then run this.
It also refreshes the hreflang block and the language switcher in index.html.

Outputs: <folder>/index.html for every language except English (root).
Images come from img/<folder>/ (root img/ for English).

Legal pages (privacy, terms, support) are English only; localized pages link
to the English ones.
"""

import importlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "i18n"))
import en  # noqa: E402
import support_tr  # noqa: E402

SITE = "https://busybplanner.com"

# folder, <html lang>, og:locale, store country, badge locale, module, switcher label
LANGS = [
    ("",      "en",    "en_US", "us", "en-us", None,        "English"),
    ("en-gb", "en-GB", "en_GB", "gb", "en-us", "tr_en_gb", "English (UK)"),
    ("fr",    "fr",    "fr_FR", "fr", "fr-fr", "tr_fr",    "Français"),
    ("de",    "de",    "de_DE", "de", "de-de", "tr_de",    "Deutsch"),
    ("es",    "es",    "es_ES", "es", "es-es", "tr_es",    "Español (España)"),
    ("es-mx", "es-MX", "es_MX", "mx", "es-mx", "tr_es_mx", "Español (México)"),
    ("it",    "it",    "it_IT", "it", "it-it", "tr_it",    "Italiano"),
    ("nl",    "nl",    "nl_NL", "nl", "nl-nl", "tr_nl",    "Nederlands"),
    ("pt-br", "pt-BR", "pt_BR", "br", "pt-br", "tr_pt_br", "Português (Brasil)"),
]
# Flag per language (regional-indicator emoji; platforms without flag glyphs show
# the country letters, and the language name is always next to it).
FLAG = {"": "🇺🇸", "en-gb": "🇬🇧", "fr": "🇫🇷", "de": "🇩🇪", "es": "🇪🇸",
        "es-mx": "🇲🇽", "it": "🇮🇹", "nl": "🇳🇱", "pt-br": "🇧🇷"}
# English strings that sit inside an attribute; every other short string is
# matched only as a whole element text (>text<) so "Capture" can't hit "Capturing".
ATTR = {6}
CSS = ("footer .langs{display:flex;flex-wrap:wrap;gap:4px 14px;flex-basis:100%}\n"
       "footer .langs a[aria-current]{color:var(--ink);font-weight:600;text-decoration:none}\n")


def url(folder):
    return f"{SITE}/{folder}/" if folder else f"{SITE}/"


def hreflang_block():
    lines = ["<!--HREFLANG-->"]
    for folder, html_lang, _, _, _, _, _ in LANGS:
        lines.append(f'<link rel="alternate" hreflang="{html_lang}" href="{url(folder)}">')
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{url("")}">')
    lines.append("<!--/HREFLANG-->")
    return "\n".join(lines)


def switcher(current):
    links = []
    for folder, html_lang, _, _, _, _, label in LANGS:
        href = f"/{folder}/" if folder else "/"
        cur = ' aria-current="page"' if folder == current else ""
        links.append(f'<a href="{href}" hreflang="{html_lang}" lang="{html_lang}"{cur}>{label}</a>')
    return "<!--LANGS-->" + " ".join(links) + "<!--/LANGS-->"


MENU_CSS = """/*LANGCSS*/
.langmenu{position:absolute;top:14px;right:18px;z-index:50;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-size:14px}
.langmenu summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:8px;padding:7px 12px;border-radius:999px;background:var(--surface,#fff);color:var(--ink,#2A2520);border:1px solid var(--rule,rgba(60,40,20,.14));box-shadow:0 1px 2px rgba(60,40,20,.06)}
.langmenu summary::-webkit-details-marker{display:none}
.langmenu summary:focus-visible,.langmenu a:focus-visible{outline:2px solid var(--clay,#C2603F);outline-offset:2px}
.langmenu .fl{font-size:18px;line-height:1}
.langmenu .chev{width:10px;height:10px;opacity:.6;transition:transform .15s}
.langmenu details[open] .chev{transform:rotate(180deg)}
.langmenu ul{list-style:none;margin:6px 0 0;padding:6px;position:absolute;right:0;min-width:210px;border-radius:14px;background:var(--surface,#fff);border:1px solid var(--rule,rgba(60,40,20,.14));box-shadow:0 12px 32px -10px rgba(60,40,20,.3)}
.langmenu li a{display:flex;align-items:center;gap:10px;padding:8px 10px;border-radius:9px;color:var(--ink,#2A2520);text-decoration:none}
.langmenu li a:hover{background:var(--clay-soft,#F2D9CC)}
.langmenu li a[aria-current]{font-weight:600}
@media (max-width:620px){.langmenu{top:10px;right:12px}.langmenu .nm{display:none}}
/*/LANGCSS*/"""

MENU_JS = """<script>(function(){var d=document.querySelector('.langmenu details');if(!d)return;document.addEventListener('click',function(e){if(!d.contains(e.target))d.open=false});document.addEventListener('keydown',function(e){if(e.key==='Escape')d.open=false})})();</script>"""


def lang_menu(current, page):
    """Flag menu. `page` is "" for the home page or "support.html"."""
    cur_flag, cur_label = FLAG[current], next(l[6] for l in LANGS if l[0] == current)
    items = []
    for folder, html_lang, _, _, _, _, label in LANGS:
        href = (f"/{folder}/" if folder else "/") + page
        mark = ' aria-current="page"' if folder == current else ""
        items.append(f'<li><a href="{href}" hreflang="{html_lang}" lang="{html_lang}"{mark}><span class="fl">{FLAG[folder]}</span><span>{label}</span></a></li>')
    chev = '<svg class="chev" viewBox="0 0 10 10" aria-hidden="true"><path d="M1.5 3.5 L5 7 L8.5 3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return ("<!--LANGMENU--><div class=\"langmenu\"><details><summary aria-label=\"Language: " + cur_label + "\">"
            f'<span class="fl">{cur_flag}</span><span class="nm">{cur_label}</span>{chev}</summary><ul>' + "".join(items)
            + "</ul></details></div>" + MENU_JS + "<!--/LANGMENU-->")


def ensure_menu(src):
    """First run only: add the menu CSS and placeholder to a source page."""
    if "/*LANGCSS*/" not in src:
        src = src.replace("</style>", MENU_CSS + "\n</style>", 1)
    if "<!--LANGMENU-->" not in src:
        src = src.replace("<body>", "<body>\n<!--LANGMENU--><!--/LANGMENU-->", 1)
    return src


def refresh_menu(src, current, page):
    return re.sub(r"<!--LANGMENU-->.*?<!--/LANGMENU-->", lambda m: lang_menu(current, page), src, flags=re.S)


def ensure_markers(src):
    """First run only: add the hreflang block, the switcher and its CSS to the English page."""
    if "<!--HREFLANG-->" not in src:
        src = src.replace('<meta name="theme-color"', hreflang_block() + '\n<meta name="theme-color"', 1)
    if "<!--LANGS-->" not in src:
        src = src.replace('<span class="sp">', f'<span class="langs">{switcher("")}</span>\n    <span class="sp">', 1)
    if "footer .langs" not in src:
        src = src.replace("footer .sp{margin-left:auto}", "footer .sp{margin-left:auto}\n" + CSS.rstrip("\n"), 1)
    return src


def refresh_markers(src, current):
    src = re.sub(r"<!--HREFLANG-->.*?<!--/HREFLANG-->", lambda m: hreflang_block(), src, flags=re.S)
    src = re.sub(r"<!--LANGS-->.*?<!--/LANGS-->", lambda m: switcher(current), src, flags=re.S)
    return src


def translate(src, strings, folder):
    # Pass 1: longest English strings first, replaced by placeholders so a short
    # string can never match inside a longer one that was already translated.
    order = sorted(range(len(en.EN)), key=lambda i: -len(en.EN[i]))
    for i in order:
        e = en.EN[i]
        if len(e) <= 45 and "<" not in e and i not in ATTR:
            pat, rep = f">{e}<", f">\x00{i}\x00<"
        else:
            pat, rep = e, f"\x00{i}\x00"
        n = src.count(pat)
        if n == 0:
            raise SystemExit(f"[{folder or 'en'}] English string #{i} not found in index.html: {e[:60]!r}")
        src = src.replace(pat, rep)
    # Pass 2: placeholders become the translation.
    for i, t in enumerate(strings):
        src = src.replace(f"\x00{i}\x00", t)
    return src


def localize(src, folder, html_lang, og_locale, cc, badge):
    s = src
    s = s.replace('<html lang="en">', f'<html lang="{html_lang}">', 1)
    s = s.replace('<link rel="canonical" href="https://busybplanner.com/">', f'<link rel="canonical" href="{url(folder)}">', 1)
    s = s.replace('<meta property="og:url" content="https://busybplanner.com/">',
                  f'<meta property="og:url" content="{url(folder)}">\n<meta property="og:locale" content="{og_locale}">', 1)
    s = s.replace('href="icon.png"', 'href="../icon.png"')
    s = s.replace('src="img/', f'src="../img/{folder}/')
    s = s.replace('href="privacy.html"', 'href="../privacy.html"')   # privacy is English only for now
    s = s.replace("apps.apple.com/us/app/", f"apps.apple.com/{cc}/app/").replace("ct=website&", f"ct=website_{folder}&")
    s = s.replace("/black/en-us?", f"/black/{badge}?")
    return s


def build_support(folder, html_lang):
    src = (ROOT / "support.html").read_text(encoding="utf-8")
    strings = support_tr.LANGS[folder]
    if len(strings) != len(support_tr.EN):
        raise SystemExit(f"support_tr[{folder}]: {len(strings)} strings, expected {len(support_tr.EN)}")
    order = sorted(range(len(support_tr.EN)), key=lambda i: -len(support_tr.EN[i]))
    for i in order:
        e = support_tr.EN[i]
        short = len(e) <= 45 and "<" not in e
        pat, rep = (f">{e}<", f">\x00{i}\x00<") if short else (e, f"\x00{i}\x00")
        if src.count(pat) == 0:
            raise SystemExit(f"[support {folder}] English string #{i} not found: {e[:50]!r}")
        src = src.replace(pat, rep)
    for i, t in enumerate(strings):
        src = src.replace(f"\x00{i}\x00", t)
    src = src.replace('<html lang="en">', f'<html lang="{html_lang}">', 1)
    src = src.replace('href="privacy.html"', 'href="../privacy.html"')
    src = refresh_menu(src, folder, "support.html")
    (ROOT / folder / "support.html").write_text(src, encoding="utf-8")
    print("wrote", f"{folder}/support.html")


def main():
    path = ROOT / "index.html"
    src = ensure_menu(ensure_markers(path.read_text(encoding="utf-8")))
    path.write_text(refresh_menu(refresh_markers(src, ""), "", ""), encoding="utf-8")
    spath = ROOT / "support.html"
    ssrc = ensure_menu(spath.read_text(encoding="utf-8"))
    spath.write_text(refresh_menu(ssrc, "", "support.html"), encoding="utf-8")
    for folder, html_lang, og_locale, cc, badge, module, _ in LANGS:
        if not folder:
            continue
        strings = importlib.import_module(module).T
        if len(strings) != len(en.EN):
            raise SystemExit(f"{module}: {len(strings)} strings, expected {len(en.EN)}")
        page = translate(src, strings, folder)
        page = localize(page, folder, html_lang, og_locale, cc, badge)
        page = refresh_menu(refresh_markers(page, folder), folder, "")
        out = ROOT / folder
        out.mkdir(exist_ok=True)
        (out / "index.html").write_text(page, encoding="utf-8")
        print("wrote", f"{folder}/index.html")
        build_support(folder, html_lang)


if __name__ == "__main__":
    main()
