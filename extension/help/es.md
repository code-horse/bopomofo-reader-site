---
layout: bare
title: Bopomofo Reader - Guía de uso
lang: es
---

# Bopomofo Reader - Guía de uso

> Versión: v1.5.0

## Introducción

Bopomofo Reader es una extensión de navegador diseñada para estudiantes de chino. Impulsada por un motor de bopomofo mejorado (con diccionario de chino moderno y más de 200 correcciones de caracteres polifónicos), añade anotaciones de pronunciación bopomofo a los caracteres chinos en páginas web con precisión.

---

## Funciones principales

- **Anotación por selección** — Seleccione texto chino en páginas web para mostrar automáticamente el bopomofo y los botones de pronunciación
- **Modo bopomofo de página completa** — Añada anotaciones bopomofo a todos los caracteres chinos de la página con un clic
- **Texto a voz** — Haga clic en el botón del altavoz para escuchar la pronunciación estándar del mandarín
- **Lectura de selección** — Seleccione cualquier texto chino y use el botón flotante o el menú contextual para leer en voz alta
- **Información emergente al pasar el cursor** — Pase el cursor sobre caracteres anotados para ver el bopomofo y los botones de pronunciación
- **Varios estilos de bopomofo** — Marcas de tono (hàn yǔ) y sin tonos (han yu)
- **Interfaz multilingüe** — Compatible con 38 idiomas de interfaz
- **Selection Speech with Karaoke Effect** — Select any Chinese text; a compact toolbar appears with speak and translate buttons; speech plays with real-time word-by-word highlighting (karaoke effect)
- **Selection Translation** — Select any text, click the translate button to get instant translation via Bing or Google Translate, displayed in an inline bubble
- **Hover Dictionary** — Hover over annotated characters to see Bopomofo, dictionary definitions from CC-CEDICT English dictionary with TOCFL levels (155K+ entries), and pronunciation buttons
- **Keyboard Shortcuts** — Quick access via Alt+Shift+B (toggle), Alt+Shift+S (speak), Alt+Shift+T (translate)

---

## Cómo usar

### Paso 1: Instalar la extensión

Instale **Bopomofo Reader** desde la [Chrome Web Store](https://chromewebstore.google.com/detail/bopomofo-reader/jkibgddokcnhedkhmleaohojhlnemmkg) o cárguela en modo desarrollador.

### Paso 2: Abrir cualquier página web

Visite cualquier página que contenga contenido en chino.

### Paso 3: Seleccionar texto o usar el botón flotante

Seleccione el texto chino que desea anotar, o haga clic en el botón flotante inferior derecho para activar el modo bopomofo de página completa.

### Paso 4: Ver el bopomofo

Pase el cursor sobre los caracteres para ver la información bopomofo, haga clic en el icono del altavoz para escuchar la pronunciación.

### Paso 5: Leer texto seleccionado

Seleccione texto chino con el ratón, haga clic en el botón flotante 🔊 para leer; o haga clic derecho y elija «Leer selección».

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

## Guía de configuración

| Configuración | Descripción |
|---------------|-------------|
| **Activar Bopomofo** | Interruptor principal para activar/desactivar la función de anotación bopomofo |
| **Bopomofo de página completa** | Muestra bopomofo para todos los caracteres (puede afectar el diseño de la página) |
| **Estilo de bopomofo** | Elegir entre marcas de tono o sin tonos |
| **Velocidad de lectura** | Ajustar la velocidad de lectura de oraciones (la pronunciación de caracteres individuales no se ve afectada) |
| **Información al pasar el cursor** | Mostrar información bopomofo al pasar el cursor |

---

## Preguntas frecuentes

**P: ¿Por qué no funciona en algunas páginas?**  
R: Por razones de seguridad, las extensiones del navegador no pueden ejecutarse en páginas especiales como `chrome://` o la configuración del navegador.

**P: ¿Qué pasa si el bopomofo es incorrecto?**  
R: El bopomofo para caracteres con múltiples pronunciaciones puede tener errores. Mejoramos continuamente. Por favor, comparta casos específicos para ayudarnos a mejorar.

**P: ¿No hay sonido en el texto a voz?**  
R: Verifique la configuración de volumen del sistema y asegúrese de que los paquetes de voz en chino estén instalados.

---

## Open-source Dictionary Attribution

Bopomofo Reader bundles offline pronunciation and dictionary resources from open-source or community projects:

- **Bopomofo conversion**: pinyin-pro and @pinyin-pro/data/modern power local Mandarin pronunciation conversion and word-level corrections; Bopomofo Reader converts pinyin syllables to Zhuyin/Bopomofo locally and applies Taiwan-pronunciation polyphonic corrections.
- **Chinese-English dictionary**: CC-CEDICT provides English definitions and base dictionary entries.
- **Multilingual definitions**: CFDICT (French), HanDeDict (German), and Wiktionary-derived datasets from kaikki.org provide Japanese, Korean, Vietnamese, and Chinese definition data.
- **Script conversion**: OpenCC-js and the bundled local conversion module are used for Simplified/Traditional Chinese conversion where needed.

All dictionary lookups run locally in your browser. Upstream projects retain their own copyright and license terms; see the Privacy Policy for more details.

---

## Enlaces relacionados

- [Política de privacidad](../privacy-policy)
- [Soporte y comentarios](../support)

---

