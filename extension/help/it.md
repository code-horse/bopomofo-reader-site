---
layout: bare
title: Bopomofo Reader - Guida utente
lang: it
---

# Bopomofo Reader - Guida utente

> Versione: v1.5.0

## Introduzione

Bopomofo Reader è un'estensione per browser pensata per chi studia cinese. Utilizza un motore bopomofo potenziato con dizionario cinese moderno e oltre 200 correzioni per parole polifoniche, per aggiungere annotazioni bopomofo accurate ai caratteri cinesi sulle pagine web.

---

## Funzioni principali

- **Annotazione per selezione** — Seleziona testo cinese sulle pagine web per visualizzare bopomofo e pulsanti audio
- **Modalità bopomofo intera pagina** — Un clic per aggiungere bopomofo a tutti i caratteri della pagina
- **Sintesi vocale** — Clicca il pulsante audio per ascoltare la pronuncia in mandarino standard
- **Lettura selezione** — Seleziona il testo, usa il pulsante flottante o il menu contestuale per leggere ad alta voce
- **Tooltip al passaggio** — Passa il mouse sui caratteri annotati per vedere il bopomofo
- **Stili bopomofo multipli** — Toni (hàn yǔ) e senza toni (han yu)
- **Interfaccia multilingue** — Supporta 38 lingue di interfaccia
- **Selection Speech with Karaoke Effect** — Select any Chinese text; a compact toolbar appears with speak and translate buttons; speech plays with real-time word-by-word highlighting (karaoke effect)
- **Selection Translation** — Select any text, click the translate button to get instant translation via Bing or Google Translate, displayed in an inline bubble
- **Hover Dictionary** — Hover over annotated characters to see Bopomofo, dictionary definitions from CC-CEDICT English dictionary with TOCFL levels (155K+ entries), and pronunciation buttons
- **Keyboard Shortcuts** — Quick access via Alt+Shift+B (toggle), Alt+Shift+S (speak), Alt+Shift+T (translate)

---

## Come usare

### Passo 1: Installazione

Installa **Bopomofo Reader** dal [Chrome Web Store](https://chromewebstore.google.com/detail/bopomofo-reader/jkibgddokcnhedkhmleaohojhlnemmkg) oppure carica in modalità sviluppatore.

### Passo 2: Aprire la pagina

Visita qualsiasi pagina con contenuti in cinese.

### Passo 3: Selezione o pulsante flottante

Seleziona il testo da annotare oppure clicca il pulsante flottante per la modalità intera pagina.

### Passo 4: Visualizzare il bopomofo

Passa il mouse per i tooltip, clicca sul pulsante audio per la pronuncia.

### Passo 5: Leggere la selezione

Seleziona il testo, clicca il pulsante 🔊 flottante oppure tasto destro "Leggi selezione".

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

- **Automatic**: Any PDF opened in the browser is automatically redirected to the Bopomofo PDF reader
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

## Guida impostazioni

| Impostazione | Descrizione |
|---|---|
| **Attiva Bopomofo** | Interruttore principale |
| **Bopomofo intera pagina** | Mostra bopomofo per tutti i caratteri |
| **Stile bopomofo** | Toni o senza toni |
| **Velocità lettura frase** | Regola la velocità di lettura delle frasi |
| **Tooltip al passaggio** | Mostra tooltip al passaggio del mouse |

---

## FAQ

**D: Perché non funziona su alcune pagine?**  
R: Le estensioni non possono funzionare su pagine chrome:// o impostazioni del browser.

**D: Bopomofo impreciso?**  
R: I caratteri polifonici possono avere errori, miglioriamo continuamente.

**D: Nessun audio?**  
R: Controlla il volume, assicurati di avere installati i pacchetti vocali cinesi.

---

## Open-source Dictionary Attribution

Bopomofo Reader bundles offline pronunciation and dictionary resources from open-source or community projects:

- **Bopomofo conversion**: pinyin-pro and @pinyin-pro/data/modern power local Mandarin pronunciation conversion and word-level corrections; Bopomofo Reader converts pinyin syllables to Zhuyin/Bopomofo locally and applies Taiwan-pronunciation polyphonic corrections.
- **Chinese-English dictionary**: CC-CEDICT provides English definitions and base dictionary entries.
- **Multilingual definitions**: CFDICT (French), HanDeDict (German), and Wiktionary-derived datasets from kaikki.org provide Japanese, Korean, Vietnamese, and Chinese definition data.
- **Script conversion**: OpenCC-js and the bundled local conversion module are used for Simplified/Traditional Chinese conversion where needed.

All dictionary lookups run locally in your browser. Upstream projects retain their own copyright and license terms; see the Privacy Policy for more details.

---

## Link utili

- [Informativa sulla privacy](../privacy-policy)
- [Supporto](../support)

---

