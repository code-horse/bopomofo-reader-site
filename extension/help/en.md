---
layout: bare
title: Bopomofo Reader Extension - User Guide
lang: en
---

# Bopomofo Reader - User Guide

> Version: v1.3.0

## Introduction

Bopomofo Reader is a browser extension designed for Chinese learners. Powered by an enhanced bopomofo-pro engine (with modern Chinese dictionary and 200+ polyphonic word corrections), it accurately adds Bopomofo pronunciation annotations to Chinese characters on web pages, helping you learn Chinese pronunciation more easily.

---

## Main Features

- **Text Selection Annotation** — Select Chinese text on web pages to automatically display Bopomofo and speech buttons
- **Whole Page Bopomofo Mode** — Add Bopomofo annotations to all Chinese characters on the page with one click
- **Text-to-Speech** — Click the speaker button to hear standard Mandarin pronunciation
- **Selection Speech with Karaoke Effect** — Select any Chinese text; a compact toolbar appears with speak and translate buttons; speech plays with real-time word-by-word or character-by-character highlighting (karaoke effect) synced to the audio
- **Selection Translation** — Select any text, click the translate button in the toolbar to get instant translation via Bing or Google Translate, displayed in an inline bubble
- **Hover Tooltips** — Hover over annotated characters to see Bopomofo and pronunciation buttons
- **Multiple Bopomofo Styles** — Support for tone marks (hàn yǔ) and without tones (han yu)
- **Keyboard Shortcuts** — Quick access to core features via customizable keyboard shortcuts
- **Multilingual Interface** — Supports 38 interface languages

---

## How to Use

### Step 1: Install the Extension

Install **Bopomofo Reader** from the [Chrome Web Store](https://chromewebstore.google.com/detail/bopomofo-reader/jkibgddokcnhedkhmleaohojhlnemmkg), or load it locally in developer mode.

### Step 2: Open Any Web Page

Visit any web page containing Chinese content.

### Step 3: Select Text or Use Floating Button

Select Chinese text you want to annotate, or click the floating button at the bottom right to enable whole page Bopomofo mode.

### Step 4: View Bopomofo

Hover over characters to see Bopomofo tooltips, click the speaker icon to hear pronunciation.

### Step 5: Speak and Translate Selected Text

Select any Chinese text with your mouse. A compact toolbar appears near the selection with two buttons:
- **🔊 Speak** — Reads the selected text aloud with karaoke-style highlighting
- **🌐 Translate** — Shows an inline translation bubble below the toolbar

You can also right-click and choose "Bopomofo Reader > Speak Selection" or "Bopomofo Reader > Translate Selection".

> **Tip:** Click the extension icon in your browser toolbar to open the settings panel and adjust Bopomofo style, speech rate, translation engine, and more.

---

## Selection Speech & Karaoke

The selection speech feature allows you to select any Chinese text and read it aloud with one click — perfect for learning sentence pronunciation and reading practice.

**Method 1: Selection Toolbar**  
Select Chinese text with your mouse. A compact toolbar appears near the selection with a 🔊 speak button and a 🌐 translate button. Click the speak button to play. As the text is read aloud, each word or character is highlighted in real time (karaoke effect), helping you follow along.

**Method 2: Right-Click Menu**  
After selecting Chinese text, right-click and choose "Bopomofo Reader > Speak Selection".

**Method 3: Keyboard Shortcut**  
Select text and press `Alt+Shift+S` (Mac: `Ctrl+Shift+S`) to speak.

> **Tip:** The karaoke highlighting effect works best when your browser supports TTS word boundary events. If not supported, the extension uses a timing-based fallback for smooth highlighting.

---

## Translation

Select any text on the page and use the translation feature to get instant translations.

**Method 1: Selection Toolbar**  
Select text, then click the 🌐 translate button in the toolbar. A translation bubble appears below showing the result, with a copy button.

**Method 2: Right-Click Menu**  
Select text, right-click and choose "Bopomofo Reader > Translate Selection".

**Method 3: Keyboard Shortcut**  
Select text and press `Alt+Shift+T` (Mac: `Ctrl+Shift+T`) to translate.

**Translation Engines:**
- **Bing Translate** (default) — Powered by Microsoft Translator
- **Google Translate** — Powered by Google

Both engines support **108 target languages**.

You can switch the translation engine and target language in the extension settings. The target language is automatically detected from your browser language.

> **Tip:** Click anywhere outside the toolbar or bubble to dismiss them.

---

## Keyboard Shortcuts

| Shortcut | Mac Shortcut | Action |
|----------|-------------|--------|
| `Alt+Shift+B` | `Ctrl+Shift+B` | Toggle Bopomofo annotations on/off |
| `Alt+Shift+S` | `Ctrl+Shift+S` | Speak selected text |
| `Alt+Shift+T` | `Ctrl+Shift+T` | Translate selected text |

> **Tip:** You can customize these shortcuts in Chrome at `chrome://extensions/shortcuts`.

---

## Settings Guide

| Setting | Description |
|---------|-------------|
| **Enable Bopomofo** | Master switch to enable or disable the Bopomofo annotation feature |
| **Whole Page Bopomofo** | When enabled, displays Bopomofo for all Chinese characters (may affect page layout) |
| **Bopomofo Style** | Choose between tone marks or without tones display |
| **Sentence Speech Rate** | Adjust the speed of sentence reading (single character speech is not affected) |
| **Hover Tooltips** | Show Bopomofo tooltip on mouse hover |
| **Translation Engine** | Choose between Bing Translate and Google Translate |
| **Target Language** | Set the translation target language (auto-detected from browser language) |

---

## FAQ

**Q: Why doesn't it work on some pages?**  
A: For security reasons, browser extensions cannot run on special pages like `chrome://`, browser settings, or the Chrome Web Store.

**Q: What if Bopomofo is inaccurate?**  
A: Bopomofo for characters with multiple pronunciations may have errors. We're continuously improving. Please share specific cases to help us improve.

**Q: No sound from text-to-speech?**  
A: Please check your system volume settings and ensure Chinese voice packs are installed. Speech support varies across browsers and operating systems.

**Q: Whole page mode affects layout?**  
A: Bopomofo annotations require extra space, which may affect the original page layout. If it affects reading, disable whole page mode and use hover tooltips instead.

**Q: Translation not working?**  
A: Translation requires an internet connection. If Bing Translate fails, try switching to Google Translate in the settings. Some network environments may block access to translation services.

---

## Related Links

- [Privacy Policy](../privacy-policy)
- [Support & Feedback](../support)

---

