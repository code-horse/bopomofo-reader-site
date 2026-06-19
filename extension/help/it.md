---
layout: bare
title: Bopomofo Reader - Guida utente
lang: it
---

# Bopomofo Reader - Guida utente

> Versione: v1.6.0

## Introduzione

Bopomofo Reader è un'estensione del browser progettata per chi studia il cinese. Con un motore bopomofo migliorato (con dizionario di cinese moderno e oltre 200 correzioni di caratteri polifonici), aggiunge con precisione annotazioni di pronuncia bopomofo ai caratteri cinesi nelle pagine web, facilitando l'apprendimento della pronuncia cinese.

---

## Funzionalità principali

- **Annotazione per selezione** — Seleziona testo cinese nelle pagine web per visualizzare automaticamente bopomofo e pulsanti vocali
- **Modalità bopomofo pagina intera** — Aggiungi annotazioni bopomofo a tutti i caratteri cinesi della pagina con un clic
- **Sintesi vocale** — Clicca il pulsante altoparlante per sentire la pronuncia standard in mandarino
- **Lettura selezione con effetto karaoke** — Seleziona qualsiasi testo cinese; appare una barra degli strumenti compatta con pulsanti di lettura e traduzione; la voce evidenzia parole o caratteri in tempo reale (effetto karaoke)
- **Traduzione selezione** — Seleziona qualsiasi testo, clicca tradurre per ottenere traduzione istantanea via Bing o Google Translate, mostrata in una bolla integrata
- **Dizionario al passaggio del mouse** — Passa il mouse sui caratteri annotati per vedere bopomofo, definizioni del dizionario CC-CEDICT inglese (110.000 voci, livelli TOCFL) e pulsanti di pronuncia
- **Lettore PDF** — Lettore PDF integrato che aggiunge automaticamente annotazioni bopomofo al testo cinese nei documenti PDF
- **Più stili bopomofo** — Con segni di tono (hàn yǔ) o senza toni (han yu)
- **Scorciatoie da tastiera** — Accesso rapido alle funzioni principali tramite scorciatoie personalizzabili
- **Interfaccia multilingue** — Supporta 38 lingue dell'interfaccia

---

## Come usare

### Passo 1: Installare l'estensione

Installa **Bopomofo Reader** dal [Chrome Web Store](https://chromewebstore.google.com/detail/bopomofo-reader/jkibgddokcnhedkhmleaohojhlnemmkg), o caricala in modalità sviluppatore.

### Passo 2: Aprire una pagina web

Visita qualsiasi pagina con contenuto cinese.

### Passo 3: Selezionare testo o usare il pulsante flottante

Seleziona il testo cinese da annotare, o clicca il pulsante flottante in basso a destra per attivare la modalità bopomofo pagina intera.

### Passo 4: Visualizzare bopomofo

Passa il mouse sui caratteri per vedere i tooltip bopomofo, clicca l'icona altoparlante per sentire la pronuncia.

### Passo 5: Leggere e tradurre il testo selezionato

Seleziona qualsiasi testo cinese con il mouse. Appare una barra degli strumenti compatta con due pulsanti:
- **🔊 Leggi** — Legge il testo selezionato con evidenziazione tipo karaoke
- **🌐 Traduci** — Mostra una bolla di traduzione integrata sotto la barra

Puoi anche fare clic destro e scegliere « Bopomofo Reader > Leggi selezione » o « Bopomofo Reader > Traduci selezione ».

> **Suggerimento:** Clicca l'icona dell'estensione nella barra del browser per aprire il pannello impostazioni e regolare stile bopomofo, velocità vocale, motore di traduzione, ecc.

---

## Lettura selezione e Karaoke

La funzione di lettura selezione permette di leggere qualsiasi testo cinese con un clic — ideale per imparare la pronuncia delle frasi e praticare la lettura.

**Metodo 1: Barra degli strumenti di selezione**  
Seleziona testo cinese con il mouse. Appare una barra compatta con pulsanti 🔊 Leggi e 🌐 Traduci. Clicca Leggi per riprodurre. Le parole o caratteri vengono evidenziati in tempo reale (effetto karaoke).

**Metodo 2: Menu contestuale**  
Seleziona testo cinese, clic destro e scegli « Bopomofo Reader > Leggi selezione ».

**Metodo 3: Scorciatoia da tastiera**  
Seleziona testo e premi `Alt+Shift+S` (Mac: `Ctrl+Shift+S`).

> **Suggerimento:** L'effetto karaoke funziona meglio quando il browser supporta eventi di limite di parole TTS. Altrimenti, l'estensione usa un fallback basato sul tempo.

---

## Traduzione

Seleziona qualsiasi testo nella pagina e usa la funzione di traduzione per ottenere traduzioni istantanee.

**Metodo 1: Barra degli strumenti di selezione**  
Seleziona testo, poi clicca 🌐 Traduci. Appare una bolla con il risultato e un pulsante copia.

**Metodo 2: Menu contestuale**  
Seleziona testo, clic destro e scegli « Bopomofo Reader > Traduci selezione ».

**Metodo 3: Scorciatoia da tastiera**  
Seleziona testo e premi `Alt+Shift+T` (Mac: `Ctrl+Shift+T`).

**Motori di traduzione:**
- **Bing Translate** (predefinito) — Powered by Microsoft Translator
- **Google Translate** — Powered by Google

Entrambi i motori supportano **108 lingue di destinazione**.

Puoi cambiare motore di traduzione e lingua di destinazione nelle impostazioni dell'estensione. La lingua di destinazione viene rilevata automaticamente dalla lingua del browser.

> **Suggerimento:** Clicca fuori dalla barra o bolla per chiuderle.

---

## Lettore PDF

Bopomofo Reader include un lettore PDF integrato che aggiunge automaticamente annotazioni bopomofo al testo cinese nei documenti PDF.

### Aprire PDF

- **Intercettazione automatica**: Qualsiasi PDF aperto nel browser viene reindirizzato automaticamente al visualizzatore PDF Bopomofo Reader
- **Trascina e rilascia**: Rilascia un file PDF locale sul visualizzatore
- **Incolla URL**: Incolla un link PDF direttamente nel visualizzatore
- **Dal popup**: Clicca l'icona dell'estensione, poi « Apri lettore PDF »

### Funzionalità PDF

| Funzionalità | Descrizione |
|--------------|-------------|
| **Ricerca dizionario** | Clicca un carattere cinese per definizione inglese istantanea, lettura bopomofo e livello TOCFL |
| **Modalità dizionario** | Clicca un carattere per vedere definizioni inglesi, pronuncia bopomofo e badge livello TOCFL |
| **Dizionario al clic** | Clicca testo cinese per definizioni (dizionario CC-CEDICT inglese, 110.000 voci, livelli TOCFL) e pronuncia |
| **Barra strumenti selezione** | Seleziona testo, poi usa la barra per leggere, tradurre o copiare |
| **Ricerca testo** | Cerca per testo cinese |
| **Barra laterale** | Indice, miniature pagine e navigazione |
| **3 temi** | Modalità lettura scuro, chiaro e seppia |
| **Traduzione** | Seleziona testo e traduci via Bing o Google Translate |

### Scorciatoie PDF

| Chiave | Azione |
|--------|--------|
| ← / → | Pagina precedente / successiva |
| + / - | Zoom in / out |
| Ctrl+F / Cmd+F | Apri ricerca |
| Escape | Chiudi tutti i pannelli flottanti |

> **Nota:** PDF protetti da password e PDF scansionati (solo immagine) non sono supportati, perché mancano di un livello di testo per le annotazioni bopomofo.

---

## Scorciatoie da tastiera

| Scorciatoia | Scorciatoia Mac | Azione |
|-------------|-----------------|--------|
| `Alt+Shift+B` | `Ctrl+Shift+B` | Attiva/disattiva annotazioni bopomofo |
| `Alt+Shift+S` | `Ctrl+Shift+S` | Leggi testo selezionato |
| `Alt+Shift+T` | `Ctrl+Shift+T` | Traduci testo selezionato |

> **Suggerimento:** Puoi personalizzare queste scorciatoie in Chrome su `chrome://extensions/shortcuts`.

---

## Guida impostazioni

| Impostazione | Descrizione |
|--------------|-------------|
| **Attiva Bopomofo** | Interruttore principale per attivare/disattivare l'annotazione bopomofo |
| **Bopomofo pagina intera** | Mostra bopomofo per tutti i caratteri cinesi (può influire sul layout) |
| **Stile bopomofo** | Scegli tra segni di tono o senza toni |
| **Velocità lettura frasi** | Regola la velocità di lettura delle frasi (la pronuncia dei singoli caratteri non è influenzata) |
| **Modalità hover** | Comportamento al passaggio: Dizionario (definizioni CC-CEDICT inglese con livelli TOCFL), solo bopomofo o disattivato |
| **Motore traduzione** | Scegli tra Bing Translate e Google Translate |
| **Lingua destinazione** | Imposta lingua di destinazione traduzione (rilevata automaticamente dal browser) |
| **Rilevamento PDF** | Rileva e reindirizza automaticamente PDF al lettore PDF integrato |

---

## FAQ

**D: Perché non funziona su alcune pagine?**  
R: Per sicurezza, le estensioni non possono funzionare su pagine speciali come `chrome://`, impostazioni del browser o Chrome Web Store.

**D: Cosa fare se il bopomofo è impreciso?**  
R: Il bopomofo dei caratteri polifonici può avere errori. Miglioriamo continuamente. Condividi casi specifici per aiutarci.

**D: Nessun suono dalla sintesi vocale?**  
R: Controlla le impostazioni del volume e assicurati che i pacchetti vocali cinesi siano installati. Il supporto vocale varia tra browser e sistemi operativi.

**D: La modalità pagina intera influisce sul layout?**  
R: Le annotazioni bopomofo richiedono spazio aggiuntivo, che può influire sul layout. Disattiva la modalità pagina intera e usa i tooltip al passaggio del mouse.

**D: La traduzione non funziona?**  
R: La traduzione richiede connessione Internet. Se Bing Translate fallisce, prova Google Translate nelle impostazioni. Alcune reti possono bloccare i servizi di traduzione.

---

## Attribuzione dizionari open source

Bopomofo Reader include risorse di pronuncia e dizionario offline da progetti open source o della community:

- **Conversione bopomofo**: pinyin-pro e @pinyin-pro/data/modern alimentano la conversione locale della pronuncia mandarina e le correzioni a livello di parola; Bopomofo Reader converte le sillabe pinyin in Zhuyin/Bopomofo localmente e applica correzioni polifoniche di pronuncia taiwanese.
- **Dizionario cinese-inglese**: CC-CEDICT fornisce definizioni inglesi e voci base del dizionario.
- **Definizioni multilingue**: CFDICT (francese), HanDeDict (tedesco) e dataset derivati da Wiktionary di kaikki.org forniscono definizioni in giapponese, coreano, vietnamita e cinese.
- **Conversione script**: OpenCC-js e il modulo di conversione locale integrato sono usati per la conversione cinese semplificato/tradizionale quando necessario.

Tutte le ricerche nel dizionario avvengono localmente nel browser. I progetti upstream mantengono i propri diritti e licenze; consulta la Politica sulla privacy per maggiori dettagli.

---

## Link correlati

- [Politica sulla privacy](../privacy-policy)
- [Supporto e feedback](../support)

---
