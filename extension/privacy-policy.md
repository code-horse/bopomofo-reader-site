---
layout: bare
title: Privacy Policy — Bopomofo Reader Extension
---

# Privacy Policy — Bopomofo Reader Extension

**Last updated**: April 7, 2026

**Effective date**: March 30, 2026

---

## Privacy Policy for Bopomofo Reader Browser Extension

### 1. Introduction

Welcome to Bopomofo Reader Extension ("we", "our", "us"). We are committed to protecting your privacy. This Privacy Policy explains how our Chrome browser extension ("Bopomofo Reader" or "the Extension") handles your information.

**Developer**: code-horse  
**Contact**: 2008-horse@163.com

### 2. Information We Do NOT Collect

Bopomofo Reader Extension is designed with privacy as a core principle:

- **No account registration required** — You can use all features without creating an account.
- **No personal data collection** — We do not collect, store, or transmit any personal information to external servers.
- **No analytics or tracking** — We do not use any analytics SDKs or tracking tools.
- **No advertising** — The extension contains no advertisements or ad-related tracking.
- **No browsing history recording** — We do not record or transmit the URLs you visit.

### 3. Data Stored Locally in Your Browser

The Extension stores the following data **locally in your browser only** (via Chrome Storage API):

| Data Type | Purpose | Storage |
|-----------|---------|---------|
| Extension settings | Preferences (enable/disable, bopomofo style, hover mode, speech rate, translation engine, target language, PDF detection, etc.) | Browser local storage |
| UI language preference | Remember your chosen interface language | Browser local storage |
| PDF banner preference | Remember whether you dismissed the PDF detection banner | Browser local storage |
| Floating button position | Remember the position of the floating annotation button | Browser local storage |

**Important**: All data listed above exists **only in your browser**. It is never uploaded to any server. If you uninstall the extension, this data will be permanently deleted.

### 4. Translation Feature & Third-Party Services

The Extension includes an optional translation feature that sends text to third-party translation services for processing:

| Service | Provider | Endpoint | Data Sent |
|---------|----------|----------|-----------|
| Bing Translate | Microsoft Corporation | `api-edge.cognitive.microsofttranslator.com` | Selected or page text only |
| Google Translate | Google LLC | `translate.googleapis.com` | Selected or page text only |

**Important**:
- Translation is triggered **only when you explicitly click the translate button**, use the translate keyboard shortcut, or invoke the context menu. Text is never sent automatically.
- Only the **text being translated** is transmitted — no URLs, browsing history, personal data, or other page content is sent.
- For Bing Translate, the extension obtains an anonymous authentication token from `edge.microsoft.com/translate/auth`. This token contains no personal information.
- The text is sent directly to the translation provider's API from the extension's background service worker. We do not relay, store, or log any translation requests or responses on our servers.
- Please refer to [Microsoft's Privacy Statement](https://privacy.microsoft.com/en-us/privacystatement) and [Google's Privacy Policy](https://policies.google.com/privacy) for details on how these providers handle data.

### 5. PDF Reader

The Extension includes a built-in PDF reader that adds Bopomofo annotations to PDF documents. When PDF detection is enabled:

- The extension uses Chrome's `declarativeNetRequest` API to automatically redirect PDF URLs opened in the browser to the built-in PDF viewer.
- When viewing a remote PDF, the browser fetches the PDF file directly from the original server — this is standard browser behavior and no data passes through our servers.
- The extension may display a browser notification when a PDF is detected, allowing you to open it in the Bopomofo Reader PDF viewer.
- All PDF processing (text extraction, bopomofo annotation, dictionary lookup) is performed **entirely locally** within your browser.

### 6. Permissions Explained

The Extension requests the following browser permissions:

| Permission | Purpose |
|------------|---------|
| `storage` | Store user settings (enable/disable state, bopomofo style, hover mode, speech rate, translation preferences, PDF detection preference, etc.) |
| `tts` | Use Chrome's built-in Text-to-Speech to read Chinese pronunciation |
| `scripting` | Execute scripts in web pages to add bopomofo annotations |
| `contextMenus` | Add right-click menu options to speak and translate selected text |
| `notifications` | Show a notification when a PDF file is detected, allowing one-click opening in the Bopomofo Reader PDF viewer |
| `declarativeNetRequest` | Redirect PDF URLs to the built-in Bopomofo Reader PDF viewer when PDF detection is enabled |
| `declarativeNetRequestWithHostAccess` | Required alongside `declarativeNetRequest` to apply PDF redirect rules across all URLs |
| `<all_urls>` (host permission) | Add bopomofo annotations to Chinese characters on any webpage; proxy translation requests to third-party APIs from the background service worker; detect and redirect PDF files to the built-in viewer |

### 7. How Bopomofo Processing Works

All bopomofo conversion is performed **entirely locally** within your browser:

- The Extension uses the [pinyin-pro](https://github.com/zh-lx/pinyin-pro) JavaScript library bundled within the extension, enhanced with modern Chinese dictionary data and 200+ polyphonic word corrections, then converts pinyin to bopomofo locally.
- A WebAssembly (WASM) module is used for traditional Chinese character conversion and additional bopomofo corrections — this module runs entirely locally.
- The built-in hover dictionary data from Taiwan Ministry of Education's Revised Dictionary of Chinese (155K+ entries) provides hover dictionary definitions — the dictionary data is bundled within the extension and loaded locally.
- Chinese character recognition, segmentation (via `Intl.Segmenter`), and bopomofo annotation all happen on-device.
- **No text is sent to any external server** for bopomofo processing or dictionary lookup.

### 8. Text-to-Speech

The Extension uses Chrome's built-in TTS (Text-to-Speech) API:

- Speech synthesis is handled by your browser's built-in engine.
- No audio data is recorded or transmitted.
- The extension includes tone sandhi and polyphonic character pronunciation optimization, all processed locally.

### 9. Children's Privacy

The Extension does not knowingly collect personal information from children under 13 years of age. Since we do not collect any personal information from any users, the Extension is safe for users of all ages.

### 10. Data Deletion

To remove all Extension data:

- Uninstalling the extension will permanently remove all associated settings from your browser.
- You can also clear extension data via Chrome Settings > Extensions > Bopomofo Reader > Details > Clear Data.

### 11. Changes to This Privacy Policy

We may update this Privacy Policy from time to time. Any changes will be reflected in the "Last updated" date at the top of this page.

### 12. Contact Us

If you have any questions about this Privacy Policy, please contact us at:

- **Email**: 2008-horse@163.com

---

*This privacy policy applies to the Bopomofo Reader browser extension (v1.4.1). For the Bopomofo Reader mobile app privacy policy, please see [App Privacy Policy](../privacy-policy).*
