---
layout: bare
title: Bopomofo Reader - Brugervejledning
lang: da
---

# Bopomofo Reader - Brugervejledning

> Version: v1.5.1

## Introduktion

Bopomofo Reader er en browserudvidelse til dem, der lærer kinesisk. Med en forbedret bopomofo-motor (moderne kinesisk ordbog og 200+ polyfoniske rettelser) tilføjer den nøjagtige bopomofo-udtaleannoteringer til kinesiske tegn på websider.

---

## Hovedfunktioner

- **Tekstmarkering** — Markér kinesisk tekst på websider for automatisk bopomofo og taleknapper
- **Bopomofo på hele siden** — Tilføj bopomofo til alle kinesiske tegn med ét klik
- **Tekst til tale** — Klik på højttalerknappen for standard mandarinudtale
- **Markeringstale med karaoke-effekt** — Markér kinesisk tekst; kompakt værktøjslinje med tale og oversæt; ord eller tegn fremhæves i realtid (karaoke)
- **Markeringsoversættelse** — Markér tekst, klik oversæt for øjeblikkelig oversættelse via Bing eller Google Translate i inline boble
- **Hover-ordbog** — Hold musen over annoterede tegn for bopomofo, CC-CEDICT engelsk ordbog (110.000 poster, TOCFL-niveauer) og udtaleknapper
- **PDF-læser** — Indbygget PDF-læser med automatisk bopomofo til kinesisk tekst i PDF
- **Flere bopomofo-stilarter** — Med tone (hàn yǔ) eller uden (han yu)
- **Tastaturgenveje** — Hurtig adgang via tilpassede genveje
- **Flersproget grænseflade** — 38 grænsefladesprog

---

## Sådan bruges det

### Trin 1: Installer udvidelsen

Installer **Bopomofo Reader** fra [Chrome Web Store](https://chromewebstore.google.com/detail/bopomofo-reader/jkibgddokcnhedkhmleaohojhlnemmkg), eller load lokalt i udviklertilstand.

### Trin 2: Åbn en webside

Besøg en side med kinesisk indhold.

### Trin 3: Markér tekst eller brug flydende knap

Markér kinesisk tekst eller klik flydende knap nederst til højre for bopomofo på hele siden.

### Trin 4: Se bopomofo

Hold musen over tegn for bopomofo-værktips, klik højttalerikon for udtale.

### Trin 5: Læs og oversæt markeret tekst

Markér kinesisk tekst med musen. Kompakt værktøjslinje med to knapper:
- **🔊 Læs** — Læser markeret tekst med karaoke-fremhævning
- **🌐 Oversæt** — Viser inline oversættelsesboble under værktøjslinjen

Højreklik også « Bopomofo Reader > Læs markering » eller « Bopomofo Reader > Oversæt markering ».

> **Tip:** Klik udvidelsesikonet i browserens værktøjslinje for indstillinger.

---

## Markeringstale & Karaoke

Markér kinesisk tekst og læs med ét klik.

**Metode 1: Værktøjslinje** — Markér tekst, klik 🔊 Læs. Karaoke-fremhævning i realtid.
**Metode 2: Kontekstmenu** — « Bopomofo Reader > Læs markering »
**Metode 3:** `Alt+Shift+S` (Mac: `Ctrl+Shift+S`)

> **Tip:** Karaoke virker bedst med TTS ordgrænse-events.

---

## Oversættelse

**Metode 1:** Markér tekst, klik 🌐 Oversæt.
**Metode 2:** « Bopomofo Reader > Oversæt markering »
**Metode 3:** `Alt+Shift+T` (Mac: `Ctrl+Shift+T`)

- **Bing Translate** (standard) — Microsoft Translator
- **Google Translate** — Google

108 målsprog. Skift i indstillinger.

---

## PDF-læser

Indbygget PDF-læser med automatisk bopomofo.

**Åbning:** Auto-redirect, træk & slip, indsæt URL, fra popup « Åbn PDF-læser »

| Funktion | Beskrivelse |
|----------|-------------|
| **Ordbogsopslag** | Klik tegn for engelsk definition, bopomofo, TOCFL |
| **Ordbogstilstand** | Engelske definitioner, bopomofo-udtale, TOCFL-badge |
| **Klik-ordbog** | CC-CEDICT engelsk, 110.000 poster, TOCFL |
| **Værktøjslinje** | Læs, oversæt, kopier |
| **Tekstsøgning** | Søg kinesisk tekst |
| **Sidepanel** | Indhold, miniaturebilleder, navigation |
| **3 temaer** | Mørk, lys, sepia |
| **Oversættelse** | Bing eller Google |

**Genveje:** ←/→ sider, +/- zoom, Ctrl/Cmd+F søg, Escape luk

> **Bemærk:** Password- og scannede PDF'er uden tekstlag understøttes ikke.

---

## Tastaturgenveje

| Genvej | Mac | Handling |
|--------|-----|----------|
| `Alt+Shift+B` | `Ctrl+Shift+B` | Bopomofo til/fra |
| `Alt+Shift+S` | `Ctrl+Shift+S` | Læs markering |
| `Alt+Shift+T` | `Ctrl+Shift+T` | Oversæt markering |

> **Tip:** Tilpas på `chrome://extensions/shortcuts`.

---

## Indstillinger

| Indstilling | Beskrivelse |
|-------------|-------------|
| **Aktivér Bopomofo** | Hovedkontakt |
| **Bopomofo hele siden** | Alle tegn (kan påvirke layout) |
| **Bopomofo-stil** | Med/uden toner |
| **Talehastighed** | Hastighed for markering |
| **Hover-tilstand** | Ordbog, kun bopomofo eller fra |
| **Oversættelsesmotor** | Bing eller Google |
| **Målsprog** | Auto fra browser |
| **PDF-detektion** | Auto-redirect PDF |

---

## FAQ

**Hvorfor ikke på nogle sider?** Sikkerhed: `chrome://`, browserindstillinger, Chrome Web Store.
**Ukorrekt bopomofo?** Polyfone tegn kan have fejl. Vi forbedrer løbende.
**Ingen lyd?** Tjek volumen og kinesiske talepakker.
**Hele side påvirker layout?** Brug hover i stedet.
**Oversættelse virker ikke?** Kræver internet. Prøv Google hvis Bing fejler.

---

## Open source ordbog-attribution

- **Bopomofo-konvertering**: pinyin-pro og @pinyin-pro/data/modern; lokal Zhuyin/Bopomofo-konvertering.
- **Kinesisk-engelsk ordbog**: CC-CEDICT.
- **Flersprogede definitioner**: CFDICT, HanDeDict, kaikki.org Wiktionary.
- **Scriptkonvertering**: OpenCC-js.

Alle ordbogsopslag kører lokalt. Se privatlivspolitik.

---

## Relaterede links

- [Privatlivspolitik](../privacy-policy)
- [Support og feedback](../support)

---
