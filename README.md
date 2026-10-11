# Advent Mitmach-Konzert – Webseite

Statische Webseite (Hugo) für das Advent Mitmach-Konzert des MGV 1874 Erlenbach e.V.
Sie liegt in einem privaten GitHub-Repo und wird automatisch über Vercel veröffentlicht.
Die Seite ist für Suchmaschinen gesperrt (`noindex`) und nur über den direkten Link erreichbar.

## Häufige Änderungen

| Was | Datei |
|---|---|
| **Liedfolge** (Reihenfolge, ein-/ausblenden, Titel) | `data/lieder.toml` |
| Datum, Uhrzeit, Ort, Anmelde-Link, Kontakte | `hugo.toml` (Abschnitt `[params]`) |
| Instrumentengruppen / Stimmen | `data/stimmen.toml` |
| Texte auf Start- und Infoseite | `content/_index.md`, `content/infos.md` |
| Noten-PDFs | `static/noten/{b,c,es,f}/<datei>.pdf` |
| Hörbeispiele | `static/audio/<datei>.mp3` |

### Liedfolge ändern
In `data/lieder.toml` die `[[lied]]`-Blöcke in die gewünschte Reihenfolge bringen.
Mit `aktiv = false` wird ein Lied ausgeblendet. Die Nummerierung, die Infoseite und die
ZIP-Downloads passen sich automatisch an.

### Neues Lied hinzufügen
1. PDFs als `static/noten/b/mein-lied.pdf`, `…/c/…`, `…/es/…`, `…/f/…` ablegen (optional `static/audio/mein-lied.mp3`).
2. In `data/lieder.toml` einen Block mit `datei = "mein-lied"` ergänzen.

Fehlt eine Datei, zeigt die Seite „Noten folgen“ an.

## Lokal ansehen
```sh
hugo server            # → http://localhost:1313
```
Die ZIP-Downloads entstehen erst beim Build: `hugo && python3 scripts/build-zips.py`.

## Veröffentlichen (Vercel)
1. Privates Repository auf GitHub anlegen und diesen Ordner pushen (Branch `main`).
2. Auf vercel.com mit GitHub anmelden → *Add New → Project* → Repository importieren.
   Die Build-Einstellungen kommen aus `vercel.json` (Hugo wird beim Build geladen, danach entstehen die ZIPs).
3. Jeder Push auf `main` veröffentlicht die Seite automatisch.

### Nicht in Suchmaschinen
`noindex` wird doppelt gesetzt: als Meta-Tag (`noindex = true` in `hugo.toml`) und als
HTTP-Header `X-Robots-Tag` (`vercel.json`). Das ist kein Zugriffsschutz – wer den Link hat, kann die Seite öffnen.
