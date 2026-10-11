#!/usr/bin/env python3
"""Erzeugt nach dem Hugo-Build je Stimme ein ZIP mit allen aktiven Liedern.

Aufruf (im Projektordner, nach `hugo`):  python3 scripts/build-zips.py
Ergebnis: public/noten/<stimme>/alle-noten-<stimme>.zip
"""
import re
import sys
import tomllib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"


def dateiname(nr: int, titel: str) -> str:
    sauber = re.sub(r'[\\/:*?"<>|]', "", titel).strip()
    return f"{nr:02d} - {sauber}.pdf"


def main() -> int:
    lieder = tomllib.loads((ROOT / "data/lieder.toml").read_text("utf-8"))["lied"]
    stimmen = tomllib.loads((ROOT / "data/stimmen.toml").read_text("utf-8"))["stimme"]
    aktiv = [l for l in lieder if l.get("aktiv")]

    if not PUBLIC.is_dir():
        print("public/ fehlt – erst `hugo` ausführen.", file=sys.stderr)
        return 1

    for stimme in stimmen:
        key = stimme["key"]
        ziel = PUBLIC / "noten" / key / f"alle-noten-{key}.zip"
        ziel.parent.mkdir(parents=True, exist_ok=True)
        anzahl = 0
        with zipfile.ZipFile(ziel, "w", zipfile.ZIP_DEFLATED) as zf:
            for nr, lied in enumerate(aktiv, start=1):
                pdf = ROOT / "static" / "noten" / key / f"{lied.get('datei', '')}.pdf"
                if lied.get("datei") and pdf.is_file():
                    zf.write(pdf, dateiname(nr, lied["titel"]))
                    anzahl += 1
        print(f"{ziel.relative_to(ROOT)}: {anzahl} PDFs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
