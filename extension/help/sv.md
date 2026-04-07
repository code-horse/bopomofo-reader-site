---
layout: bare
title: Bopomofo Reader - Användarguide
lang: sv
---

# Bopomofo Reader - Användarguide

> Version: v1.4.1

## Introduktion

Bopomofo Reader är ett webbläsartillägg utformat för kinesiskstuderande. Det använder en förbättrad bopomofo-motor (med modernt kinesiskt lexikon och över 200 korrigeringar av flertydiga tecken) för att lägga till exakta bopomofo-uttalsbeteckningar till kinesiska tecken på webbsidor.

---

## Huvudfunktioner

- **Textmarkeringsnotering** — Markera kinesisk text på webbsidor för att automatiskt visa bopomofo och uttalsknappar
- **Helsides bopomofo-läge** — Lägg till bopomofo till alla kinesiska tecken på sidan med ett klick
- **Text-till-tal** — Klicka på högtalarknappen för att höra standardkinesiskt uttal
- **Läs markering** — Markera valfri kinesisk text och använd den flytande knappen eller högerklicksmenyn för uppläsning
- **Hovra-verktygstips** — Håll musen över kommenterade tecken för att se bopomofo
- **Flera bopomofo-stilar** — Tonmarkeringar (hàn yǔ) och utan toner (han yu)
- **Flerspråkigt gränssnitt** — Stöder 38 gränssnittsspråk
- **Selection Speech with Karaoke Effect** — Select any Chinese text; a compact toolbar appears with speak and translate buttons; speech plays with real-time word-by-word highlighting (karaoke effect)
- **Selection Translation** — Select any text, click the translate button to get instant translation via Bing or Google Translate, displayed in an inline bubble
- **Hover Dictionary** — Hover over annotated characters to see Bopomofo, dictionary definitions from Taiwan MOE Revised Dictionary (155K+ entries), and pronunciation buttons
- **Keyboard Shortcuts** — Quick access via Alt+Shift+B (toggle), Alt+Shift+S (speak), Alt+Shift+T (translate)

---

## Hur man använder

### Steg 1: Installera tillägget

Installera **Bopomofo Reader** från [Chrome Web Store](https://chromewebstore.google.com/detail/bopomofo-reader/jkibgddokcnhedkhmleaohojhlnemmkg) eller ladda det lokalt i utvecklarläge.

### Steg 2: Öppna en webbsida

Besök vilken webbsida som helst med kinesiskt innehåll.

### Steg 3: Markera text eller använd flytande knapp

Markera kinesisk text du vill kommentera, eller klicka på den flytande knappen i nedre högra hörnet för att aktivera helsides bopomofo-läge.

### Steg 4: Visa bopomofo

Håll musen över tecken för att se bopomofo-verktygstips, klicka på högtalarikonen för uttal.

### Steg 5: Läs markerad text

Markera kinesisk text med musen, klicka på den flytande 🔊-knappen för uppläsning; eller högerklicka och välj "Läs markering".

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

Bopomofo Reader v1.4.1 includes a powerful built-in PDF reader that automatically adds Bopomofo annotations to any PDF file.

### Opening PDFs

- **Automatic**: Any PDF opened in the browser is automatically redirected to the Bopomofo PDF reader
- **From Popup**: Click the extension icon and choose "Open PDF Reader"
- **Drag & Drop**: Drag a local PDF file into the reader
- **Paste URL**: Paste any PDF link directly into the viewer

### PDF Features

| Feature | Description |
|---------|-------------|
| **Per-character Bopomofo** | Accurate Bopomofo annotation above each Chinese character, scaled with zoom |
| **4 Bopomofo Modes** | Tone marks, no tones, hover-only, or hidden |
| **Click Dictionary** | Click any Chinese character to see dictionary definitions (Taiwan MOE Revised Dictionary, 155K entries) |
| **Selection Toolbar** | Select text, then use the toolbar to read aloud, translate, or copy |
| **Sidebar** | Table of contents, page thumbnails, and Bopomofo search |
| **3 Themes** | Dark, Light, and Sepia reading modes |
| **Zoom Adaptive** | Bopomofo scales perfectly with zoom level, no overlap |
| **Keyboard Shortcuts** | ←→ page navigation, +- zoom, Ctrl/Cmd+F search, Escape to dismiss popups |

> **Tip:** The PDF reader works with both local files and online PDFs. All Bopomofo processing happens locally in your browser.

---

## Inställningsguide

| Inställning | Beskrivning |
|-------------|-------------|
| **Aktivera Bopomofo** | Huvudströmbrytare för bopomofo-notering |
| **Helsides bopomofo** | Visar bopomofo för alla tecken (kan påverka sidlayouten) |
| **Bopomofo-stil** | Välj tonmarkeringar eller utan toner |
| **Meningsläshastighet** | Justera hastigheten för meningsläsning (enstaka tecken påverkas inte) |
| **Hovra-verktygstips** | Visa bopomofo-tips vid mushovring |

---

## Vanliga frågor

**F: Varför fungerar det inte på vissa sidor?**  
S: Av säkerhetsskäl kan webbläsartillägg inte köras på specialsidor som `chrome://` eller webbläsarinställningar.

**F: Vad händer om bopomofo är felaktig?**  
S: Bopomofo för tecken med flera uttal kan innehålla fel. Vi förbättrar kontinuerligt. Rapportera gärna specifika fall.

**F: Inget ljud?**  
S: Kontrollera systemets volyminställningar och se till att kinesiska röstpaket är installerade.

---

## Relaterade länkar

- [Integritetspolicy](../privacy-policy)
- [Support och feedback](../support)

---

