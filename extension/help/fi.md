---
layout: bare
title: Bopomofo Reader - Käyttöopas
lang: fi
---

# Bopomofo Reader - Käyttöopas

> Versio: v1.5.0

## Johdanto

Bopomofo Reader on selainlaajennus kiinan oppijoille. Se käyttää paranneltua bopomofo-moottoria modernin kiinan sanakirjan ja yli 200 monisanaisen sanan korjauksen kanssa lisätäkseen bopomofo-annotointia kiinalaisiin merkkeihin verkkosivuilla.

---

## Pääominaisuudet

- **Tekstin valinnan annotointi** — Valitse kiinalainen teksti verkkosivuilla nähdäksesi bopomofo ja puhe-painikkeet
- **Koko sivun bopomofo-tila** — Yhdellä klikkauksella lisää bopomofo kaikkiin merkkeihin sivulla
- **Tekstistä puheeksi** — Klikkaa kaiuttimen painiketta kuullaksesi mandariinin ääntämisen
- **Valitun tekstin puhe** — Valitse teksti ja käytä kelluvaa painiketta tai oikean painikkeen valikkoa lukeaksesi ääneen
- **Hiiren päällä ohjeet** — Vieraile annotoitujen merkkien päällä nähdäksesi bopomofo
- **Useita bopomofo-tyylejä** — Sävelmerkinnät (hàn yǔ) ja ilman säveliä (han yu)
- **Monikielinen käyttöliittymä** — Tukee 38 käyttöliittymäkieltä
- **Selection Speech with Karaoke Effect** — Select any Chinese text; a compact toolbar appears with speak and translate buttons; speech plays with real-time word-by-word highlighting (karaoke effect)
- **Selection Translation** — Select any text, click the translate button to get instant translation via Bing or Google Translate, displayed in an inline bubble
- **Hover Dictionary** — Hover over annotated characters to see Bopomofo, dictionary definitions from CC-CEDICT English dictionary with TOCFL levels (155K+ entries), and pronunciation buttons
- **Keyboard Shortcuts** — Quick access via Alt+Shift+B (toggle), Alt+Shift+S (speak), Alt+Shift+T (translate)

---

## Käyttöohje

### Vaihe 1: Asenna

Asenna **Bopomofo Reader** [Chrome Web Storesta](https://chromewebstore.google.com/detail/bopomofo-reader/jkibgddokcnhedkhmleaohojhlnemmkg) tai lataa kehittäjätilassa.

### Vaihe 2: Avaa sivu

Vieraile millä tahansa sivulla, jolla on kiinalaista sisältöä.

### Vaihe 3: Valitse teksti tai kelluva painike

Valitse teksti tai klikkaa kelluvaa painiketta koko sivun tilaan.

### Vaihe 4: Näytä bopomofo

Vieraile hiirellä saadaksesi ohjeita, klikkaa kaiutinta ääntämystä varten.

### Vaihe 5: Lue valinta

Valitse teksti, klikkaa kelluvaa 🔊-painiketta tai oikean painikkeen «Lue valinta».

---

## Selection Speech & Karaoke

Select any Chinese text and read it aloud with one click — perfect for learning sentence pronunciation.

**Method 1: Selection Toolbar**
Select Chinese text with your mouse. A compact toolbar appears near the selection with a 🔊 speak button and a 🌐 translate button. Click speak to play. Words highlight in real time (karaoke effect).

**Method 2: Right-Click Menu**
Select text, right-click and choose "Bopomofo Reader > Speak Selection".

**Method 3: Keyboard Shortcut**
Select text and press `Alt+Shift+S` (Mac: `Ctrl+Shift+S`).

---

## Translation

Select any text on the page to get instant translations.

**Method 1: Selection Toolbar**
Select text, then click the 🌐 translate button. A translation bubble appears with the result and a copy button.

**Method 2: Right-Click Menu**
Select text, right-click and choose "Bopomofo Reader > Translate Selection".

**Method 3: Keyboard Shortcut**
Select text and press `Alt+Shift+T` (Mac: `Ctrl+Shift+T`).

**Translation Engines:**
- **Bing Translate** (default) — Powered by Microsoft Translator
- **Google Translate** — Powered by Google

Both engines support **108 target languages**.

---

## Keyboard Shortcuts

| Shortcut | Mac Shortcut | Action |
|----------|-------------|--------|
| `Alt+Shift+B` | `Ctrl+Shift+B` | Toggle Bopomofo annotations on/off |
| `Alt+Shift+S` | `Ctrl+Shift+S` | Speak selected text |
| `Alt+Shift+T` | `Ctrl+Shift+T` | Translate selected text |

> **Tip:** Customize shortcuts in Chrome at `chrome://extensions/shortcuts`.

## Built-in PDF Reader

Bopomofo Reader v1.5.0 includes a powerful built-in PDF reader that automatically adds Bopomofo annotations to any PDF file.

### Opening PDFs

- **Automatic**: Any PDF opened in the browser is automatically redirected to the Bopomofo Reader PDF viewer
- **From Popup**: Click the extension icon and choose "Open PDF Reader"
- **Drag & Drop**: Drag a local PDF file into the reader
- **Paste URL**: Paste any PDF link directly into the viewer

### PDF Features

| Feature | Description |
|---------|-------------|
| **Dictionary Lookup** | Accurate Bopomofo annotation above each Chinese character, scaled with zoom |
| **Dictionary Mode** | Tone marks, no tones, hover-only, or hidden |
| **Click Dictionary** | Click any Chinese character to see dictionary definitions (CC-CEDICT English dictionary, 110K entries, TOCFL levels) |
| **Selection Toolbar** | Select text, then use the toolbar to read aloud, translate, or copy |
| **Sidebar** | Table of contents, page thumbnails, and Bopomofo search |
| **3 Themes** | Dark, Light, and Sepia reading modes |
| **Zoom Adaptive** | Bopomofo scales perfectly with zoom level, no overlap |
| **Keyboard Shortcuts** | ←→ page navigation, +- zoom, Ctrl/Cmd+F search, Escape to dismiss popups |

> **Tip:** The PDF reader works with both local files and online PDFs. All Bopomofo processing happens locally in your browser.

---

## Asetusten opas

| Asetus | Kuvaus |
|---|---|
| **Ota käyttöön Bopomofo** | Pääkytkin |
| **Koko sivun bopomofo** | Näytä bopomofo kaikille merkkeille |
| **Bopomofo-tyyli** | Sävelmerkinnät tai ilman säveliä |
| **Lauseen lukunopeus** | Säädä lauseen lukunopeutta |
| **Hiiren päällä ohjeet** | Näytä ohje hiiren päällä ollessa |

---

## Open-source Dictionary Attribution

Bopomofo Reader bundles offline pronunciation and dictionary resources from open-source or community projects:

- **Bopomofo conversion**: pinyin-pro and @pinyin-pro/data/modern power local Mandarin pronunciation conversion and word-level corrections; Bopomofo Reader converts pinyin syllables to Zhuyin/Bopomofo locally and applies Taiwan-pronunciation polyphonic corrections.
- **Chinese-English dictionary**: CC-CEDICT provides English definitions and base dictionary entries.
- **Multilingual definitions**: CFDICT (French), HanDeDict (German), and Wiktionary-derived datasets from kaikki.org provide Japanese, Korean, Vietnamese, and Chinese definition data.
- **Script conversion**: OpenCC-js and the bundled local conversion module are used for Simplified/Traditional Chinese conversion where needed.

All dictionary lookups run locally in your browser. Upstream projects retain their own copyright and license terms; see the Privacy Policy for more details.

---

## Usein kysytyt kysymykset

**K: Miksi se ei toimi joillakin sivuilla?**  
V: Laajennukset eivät voi toimia chrome://- tai selaimen asetussivuilla.

**K: Epätarkka bopomofo?**  
V: Monisanaisten merkkien bopomofo voi sisältää virheitä; parannamme jatkuvasti.

**K: Ei ääntä?**  
V: Tarkista äänenvoimakkuus ja varmista, että kiinan äänipaketit on asennettu.

---
## Aiheeseen liittyvät linkit

- [Tietosuojakäytäntö](../privacy-policy)
- [Tuki](../support)

---
