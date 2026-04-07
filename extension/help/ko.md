---
layout: bare
title: Bopomofo Reader - 사용 가이드
lang: ko
---

# Bopomofo Reader - 사용 가이드

> 버전: v1.4.1

## 소개

Bopomofo Reader는 중국어 학습자를 위한 브라우저 확장 프로그램입니다. 강화된 핀인 엔진(현대 중국어 사전 및 200개 이상의 다음자 교정 포함)을 탑재하여, 웹 페이지의 한자에 정확한 병음 주석을 자동으로 추가하여 중국어 발음 학습을 돕습니다.

---

## 주요 기능

- **텍스트 선택 주석** — 웹 페이지에서 중국어 텍스트를 선택하면 자동으로 병음과 음성 버튼을 표시
- **전체 페이지 병음 모드** — 한 번의 클릭으로 페이지의 모든 한자에 병음 추가
- **텍스트 음성 변환** — 스피커 버튼을 클릭하여 표준 중국어 발음 듣기
- **선택 텍스트 읽기** — 임의의 중국어 텍스트를 선택하고 플로팅 버튼이나 우클릭 메뉴로 음성 읽기
- **호버 툴팁** — 주석이 달린 한자에 마우스를 올리면 병음과 발음 버튼 표시
- **다양한 병음 스타일** — 성조 부호 포함(hàn yǔ)과 성조 없음(han yu) 전환 지원
- **다국어 인터페이스** — 38개 인터페이스 언어 지원
- **Selection Speech with Karaoke Effect** — Select any Chinese text; a compact toolbar appears with speak and translate buttons; speech plays with real-time word-by-word highlighting (karaoke effect)
- **Selection Translation** — Select any text, click the translate button to get instant translation via Bing or Google Translate, displayed in an inline bubble
- **Hover Dictionary** — Hover over annotated characters to see Bopomofo, dictionary definitions from Taiwan MOE Revised Dictionary (155K+ entries), and pronunciation buttons
- **Keyboard Shortcuts** — Quick access via Alt+Shift+B (toggle), Alt+Shift+S (speak), Alt+Shift+T (translate)

---

## 사용 방법

### 1단계: 확장 프로그램 설치

[크롬 웹 스토어](https://chromewebstore.google.com/detail/bopomofo-reader/jkibgddokcnhedkhmleaohojhlnemmkg)에서 「Bopomofo Reader」를 설치하거나 개발자 모드로 로컬에서 로드합니다.

### 2단계: 웹 페이지 열기

중국어 콘텐츠가 포함된 웹 페이지를 방문합니다.

### 3단계: 텍스트 선택 또는 플로팅 버튼 사용

주석을 달고 싶은 중국어 텍스트를 선택하거나, 페이지 오른쪽 하단의 플로팅 버튼을 클릭하여 전체 페이지 병음 모드를 활성화합니다.

### 4단계: 병음 확인

한자 위에 마우스를 올려 병음 툴팁을 확인하고 스피커 아이콘을 클릭하여 발음을 듣습니다.

### 5단계: 선택 텍스트 읽기

마우스로 중국어 텍스트를 선택한 후 🔊 플로팅 버튼을 클릭하여 읽기, 또는 우클릭 후 「선택 텍스트 읽기」를 선택합니다.

> **팁:** 브라우저 도구 모음의 확장 프로그램 아이콘을 클릭하면 설정 패널이 열리고 병음 스타일, 읽기 속도 등을 조정할 수 있습니다.

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

## 설정 가이드

| 설정 항목 | 설명 |
|-----------|------|
| **병음 활성화** | 병음 주석 기능의 마스터 스위치 |
| **전체 페이지 병음** | 활성화하면 모든 한자에 병음 표시 (페이지 레이아웃에 영향을 줄 수 있음) |
| **병음 스타일** | 성조 부호 포함 또는 성조 없음 표시 선택 |
| **문장 읽기 속도** | 문장 읽기 속도 조절 (단일 문자 발음에는 영향 없음) |
| **호버 툴팁** | 마우스 호버 시 병음 툴팁 표시 |

---

## 자주 묻는 질문

**Q: 일부 페이지에서 작동하지 않는 이유는?**  
A: 보안상의 이유로 `chrome://`, 브라우저 설정 페이지 등 특수 페이지에서는 브라우저 확장 프로그램이 작동하지 않습니다.

**Q: 병음이 부정확한 경우?**  
A: 다음자의 병음에는 오류가 있을 수 있습니다. 지속적으로 개선하고 있으니 구체적인 사례를 피드백해 주시면 감사하겠습니다.

**Q: 음성이 나오지 않는 경우?**  
A: 시스템 볼륨 설정을 확인하고 중국어 음성 팩이 설치되어 있는지 확인해 주세요.

---

## 관련 링크

- [개인정보 처리방침](../privacy-policy)
- [지원 및 피드백](../support)

---

