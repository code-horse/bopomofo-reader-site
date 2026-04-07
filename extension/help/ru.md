---
layout: bare
title: Bopomofo Reader - Руководство пользователя
lang: ru
---

# Bopomofo Reader - Руководство пользователя

> Версия: v1.4.0

## Введение

Bopomofo Reader — это расширение для браузера, предназначенное для изучающих китайский язык. Благодаря усовершенствованному движку пиньинь (с современным китайским словарём и более чем 200 исправлениями полифонических иероглифов) оно точно добавляет аннотации пиньинь к китайским иероглифам на веб-страницах.

---

## Основные функции

- **Аннотация выделенного текста** — Выделите китайский текст на веб-странице, чтобы автоматически отобразить пиньинь и кнопки произношения
- **Режим пиньинь для всей страницы** — Добавьте пиньинь ко всем иероглифам на странице одним щелчком
- **Озвучивание текста** — Нажмите кнопку динамика, чтобы услышать стандартное произношение на мандаринском
- **Чтение выделенного** — Выделите любой китайский текст и используйте плавающую кнопку или контекстное меню для озвучивания
- **Всплывающие подсказки** — Наведите курсор на аннотированные иероглифы, чтобы увидеть пиньинь и кнопки произношения
- **Несколько стилей пиньинь** — С тоновыми знаками (hàn yǔ) и без тонов (han yu)
- **Многоязычный интерфейс** — Поддержка 38 языков интерфейса
- **Selection Speech with Karaoke Effect** — Select any Chinese text; a compact toolbar appears with speak and translate buttons; speech plays with real-time word-by-word highlighting (karaoke effect)
- **Selection Translation** — Select any text, click the translate button to get instant translation via Bing or Google Translate, displayed in an inline bubble
- **Hover Dictionary** — Hover over annotated characters to see Bopomofo, dictionary definitions from Taiwan MOE Revised Dictionary (155K+ entries), and pronunciation buttons
- **Keyboard Shortcuts** — Quick access via Alt+Shift+B (toggle), Alt+Shift+S (speak), Alt+Shift+T (translate)

---

## Как использовать

### Шаг 1: Установите расширение

Установите **Bopomofo Reader** из [Chrome Web Store](https://chromewebstore.google.com/detail/bopomofo-reader/jkibgddokcnhedkhmleaohojhlnemmkg) или загрузите локально в режиме разработчика.

### Шаг 2: Откройте веб-страницу

Посетите любую веб-страницу с китайским контентом.

### Шаг 3: Выделите текст или используйте плавающую кнопку

Выделите китайский текст для аннотации или нажмите плавающую кнопку в правом нижнем углу для активации режима пиньинь для всей страницы.

### Шаг 4: Просмотрите пиньинь

Наведите курсор на иероглифы, чтобы увидеть подсказки с пиньинь, нажмите значок динамика для прослушивания произношения.

### Шаг 5: Озвучьте выделенный текст

Выделите мышью китайский текст, нажмите плавающую кнопку 🔊 для озвучивания; или щёлкните правой кнопкой мыши и выберите «Прочитать выделенное».

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

Bopomofo Reader v1.4.0 includes a powerful built-in PDF reader that automatically adds Bopomofo annotations to any PDF file.

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

## Настройки

| Настройка | Описание |
|-----------|----------|
| **Включить Bopomofo** | Главный переключатель для включения/выключения аннотаций пиньинь |
| **Пиньинь для всей страницы** | Отображает пиньинь для всех иероглифов (может влиять на компоновку страницы) |
| **Стиль пиньинь** | Выбор между тоновыми знаками или без тонов |
| **Скорость чтения предложений** | Регулировка скорости чтения предложений (произношение отдельных иероглифов не затрагивается) |
| **Всплывающие подсказки** | Показывать подсказки пиньинь при наведении курсора |

---

## Часто задаваемые вопросы

**В: Почему расширение не работает на некоторых страницах?**  
О: По соображениям безопасности расширения браузера не могут работать на специальных страницах, таких как `chrome://` или настройки браузера.

**В: Что делать, если пиньинь неточный?**  
О: Пиньинь для иероглифов с несколькими произношениями может содержать ошибки. Мы постоянно совершенствуемся. Пожалуйста, сообщайте нам о конкретных случаях.

**В: Нет звука при озвучивании?**  
О: Проверьте настройки громкости системы и убедитесь, что установлены голосовые пакеты для китайского языка.

---

## Полезные ссылки

- [Политика конфиденциальности](../privacy-policy)
- [Поддержка и обратная связь](../support)

---

