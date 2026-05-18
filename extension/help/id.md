---
layout: bare
title: Bopomofo Reader - Panduan Pengguna
lang: id
---

# Bopomofo Reader - Panduan Pengguna

> Versi: v1.5.0

## Pengantar

Bopomofo Reader adalah ekstensi peramban untuk pembelajar bahasa Mandarin. Menggunakan mesin bopomofo yang ditingkatkan dengan kamus Mandarin modern dan 200+ koreksi kata polifonik untuk menambahkan anotasi bopomofo pada karakter Tionghoa di halaman web.

---

## Fitur Utama

- **Anotasi Pemilihan Teks** — Pilih teks Mandarin di halaman web untuk menampilkan bopomofo dan tombol ucapan
- **Mode Bopomofo Seluruh Halaman** — Satu klik untuk menambahkan bopomofo ke semua karakter di halaman
- **Ucapan Teks** — Klik tombol speaker untuk mendengar pengucapan Mandarin
- **Ucapan Pemilihan** — Pilih teks, gunakan tombol mengambang atau menu klik kanan untuk membacakan dengan suara
- **Tooltip Hover** — Arahkan kursor ke karakter yang telah diberi anotasi untuk melihat bopomofo
- **Berbagai Gaya Bopomofo** — Tanda nada (hàn yǔ) dan tanpa nada (han yu)
- **Antarmuka Multibahasa** — Mendukung 38 bahasa antarmuka
- **Selection Speech with Karaoke Effect** — Select any Chinese text; a compact toolbar appears with speak and translate buttons; speech plays with real-time word-by-word highlighting (karaoke effect)
- **Selection Translation** — Select any text, click the translate button to get instant translation via Bing or Google Translate, displayed in an inline bubble
- **Hover Dictionary** — Hover over annotated characters to see Bopomofo, dictionary definitions from CC-CEDICT English dictionary with TOCFL levels (155K+ entries), and pronunciation buttons
- **Keyboard Shortcuts** — Quick access via Alt+Shift+B (toggle), Alt+Shift+S (speak), Alt+Shift+T (translate)

---

## Cara Penggunaan

### Langkah 1: Pasang

Pasang **Bopomofo Reader** dari [Chrome Web Store](https://chromewebstore.google.com/detail/bopomofo-reader/jkibgddokcnhedkhmleaohojhlnemmkg) atau muat dalam mode pengembang.

### Langkah 2: Buka halaman

Kunjungi halaman apa pun dengan konten Mandarin.

### Langkah 3: Pilih teks atau tombol mengambang

Pilih teks yang ingin diberi anotasi atau klik tombol mengambang untuk mode seluruh halaman.

### Langkah 4: Lihat bopomofo

Arahkan kursor untuk tooltip, klik speaker untuk pengucapan.

### Langkah 5: Baca pemilihan

Pilih teks, klik tombol mengambang 🔊 atau klik kanan "Bacakan Pemilihan".

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

## Panduan Pengaturan

| Pengaturan | Deskripsi |
|---|---|
| **Aktifkan Bopomofo** | Saklar utama |
| **Bopomofo Seluruh Halaman** | Tampilkan bopomofo untuk semua karakter |
| **Gaya Bopomofo** | Tanda nada atau tanpa nada |
| **Kecepatan Ucapan Kalimat** | Sesuaikan kecepatan membaca kalimat |
| **Tooltip Hover** | Tampilkan tooltip saat hover |

---

## FAQ

**T: Mengapa tidak bekerja di beberapa halaman?**  
J: Ekstensi tidak dapat berjalan di halaman chrome:// atau halaman pengaturan peramban.

**T: Bopomofo tidak akurat?**  
J: Karakter polifonik mungkin memiliki kesalahan, kami terus meningkatkan.

**T: Tidak ada suara?**  
J: Periksa volume, pastikan paket suara Mandarin sudah terpasang.

---

## Open-source Dictionary Attribution

Bopomofo Reader bundles offline pronunciation and dictionary resources from open-source or community projects:

- **Bopomofo conversion**: pinyin-pro and @pinyin-pro/data/modern power local Mandarin pronunciation conversion and word-level corrections; Bopomofo Reader converts pinyin syllables to Zhuyin/Bopomofo locally and applies Taiwan-pronunciation polyphonic corrections.
- **Chinese-English dictionary**: CC-CEDICT provides English definitions and base dictionary entries.
- **Multilingual definitions**: CFDICT (French), HanDeDict (German), and Wiktionary-derived datasets from kaikki.org provide Japanese, Korean, Vietnamese, and Chinese definition data.
- **Script conversion**: OpenCC-js and the bundled local conversion module are used for Simplified/Traditional Chinese conversion where needed.

All dictionary lookups run locally in your browser. Upstream projects retain their own copyright and license terms; see the Privacy Policy for more details.

---

## Tautan Terkait

- [Kebijakan Privasi](../privacy-policy)
- [Dukungan](../support)

---
