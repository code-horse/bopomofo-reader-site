---
layout: bare
title: Bopomofo Reader - Gebruikershandleiding
lang: nl
---

# Bopomofo Reader - Gebruikershandleiding

> Versie: v1.6.0

## Introductie

Bopomofo Reader is een browserextensie voor Chinese taalleerders. Met een verbeterde bopomofo-engine (met modern Chinees woordenboek en 200+ polyfone woordcorrecties) voegt het nauwkeurig bopomofo-uitspraakannotaties toe aan Chinese karakters op webpagina's, waardoor het leren van Chinese uitspraak gemakkelijker wordt.

---

## Belangrijkste functies

- **Tekstselectie-annotatie** — Selecteer Chinese tekst op webpagina's om automatisch bopomofo en spraakknoppen te tonen
- **Hele pagina bopomofo-modus** — Voeg met één klik bopomofo toe aan alle Chinese karakters op de pagina
- **Tekst-naar-spraak** — Klik op de speakerknop om Mandarijnse uitspraak te horen
- **Selectie voorlezen met karaoke-effect** — Selecteer Chinese tekst; een compacte werkbalk met voorlezen en vertalen knoppen verschijnt; spraak speelt met realtime woord- of karaktermarkering (karaoke-effect)
- **Selectievertaling** — Selecteer tekst, klik op vertalen voor directe vertaling via Bing of Google Translate, weergegeven in een inline bubbel
- **Hover-woordenboek** — Beweeg over geannoteerde karakters voor bopomofo, CC-CEDICT Engels woordenboekdefinities (110.000 items, TOCFL-niveaus) en uitspraakknoppen
- **PDF-lezer** — Ingebouwde PDF-lezer die automatisch bopomofo-annotaties toevoegt aan Chinese tekst in PDF-documenten
- **Meerdere bopomofo-stijlen** — Met toontekens (hàn yǔ) of zonder tonen (han yu)
- **Sneltoetsen** — Snelle toegang tot kernfuncties via aanpasbare sneltoetsen
- **Meertalige interface** — Ondersteunt 38 interfacetalen

---

## Gebruiksaanwijzing

### Stap 1: Extensie installeren

Installeer **Bopomofo Reader** vanuit de [Chrome Web Store](https://chromewebstore.google.com/detail/bopomofo-reader/jkibgddokcnhedkhmleaohojhlnemmkg), of laad in ontwikkelaarsmodus.

### Stap 2: Webpagina openen

Bezoek een pagina met Chinese inhoud.

### Stap 3: Tekst selecteren of zwevende knop gebruiken

Selecteer Chinese tekst om te annoteren, of klik op de zwevende knop rechtsonder voor de hele pagina bopomofo-modus.

### Stap 4: Bopomofo bekijken

Beweeg over karakters voor bopomofo-tooltips, klik op het speakerpictogram voor uitspraak.

### Stap 5: Geselecteerde tekst voorlezen en vertalen

Selecteer Chinese tekst met de muis. Een compacte werkbalk verschijnt met twee knoppen:
- **🔊 Voorlezen** — Leest geselecteerde tekst met karaoke-markering
- **🌐 Vertalen** — Toont een inline vertaalbubbel onder de werkbalk

U kunt ook rechtsklikken en « Bopomofo Reader > Selectie voorlezen » of « Bopomofo Reader > Selectie vertalen » kiezen.

> **Tip:** Klik op het extensiepictogram in de browserwerkbalk om het instellingenpaneel te openen en bopomofo-stijl, spreeksnelheid, vertaalservice, enz. aan te passen.

---

## Selectie voorlezen & Karaoke

Met selectie voorlezen kunt u Chinese tekst met één klik voorlezen — ideaal voor het leren van uitspraak en leespraktijk.

**Methode 1: Selectie-werkbalk**  
Selecteer Chinese tekst met de muis. Een compacte werkbalk met 🔊 Voorlezen en 🌐 Vertalen knoppen verschijnt. Klik op Voorlezen. Woorden of karakters worden realtime gemarkeerd (karaoke-effect).

**Methode 2: Contextmenu**  
Selecteer Chinese tekst, rechtsklik en kies « Bopomofo Reader > Selectie voorlezen ».

**Methode 3: Sneltoets**  
Selecteer tekst en druk `Alt+Shift+S` (Mac: `Ctrl+Shift+S`).

> **Tip:** Het karaoke-effect werkt het beste wanneer uw browser TTS-woordgrens-events ondersteunt. Anders gebruikt de extensie een tijdgebaseerde fallback.

---

## Vertaling

Selecteer tekst op de pagina en gebruik de vertaalfunctie voor directe vertalingen.

**Methode 1: Selectie-werkbalk**  
Selecteer tekst, klik op 🌐 Vertalen. Een vertaalbubbel verschijnt met resultaat en kopieerknop.

**Methode 2: Contextmenu**  
Selecteer tekst, rechtsklik en kies « Bopomofo Reader > Selectie vertalen ».

**Methode 3: Sneltoets**  
Selecteer tekst en druk `Alt+Shift+T` (Mac: `Ctrl+Shift+T`).

**Vertaaldiensten:**
- **Bing Translate** (standaard) — Powered by Microsoft Translator
- **Google Translate** — Powered by Google

Beide diensten ondersteunen **108 doeltalen**.

U kunt vertaaldienst en doeltaal wijzigen in de extensie-instellingen. Doeltaal wordt automatisch gedetecteerd uit de browser-taal.

> **Tip:** Klik buiten de werkbalk of bubbel om te sluiten.

---

## PDF-lezer

Bopomofo Reader bevat een ingebouwde PDF-lezer die automatisch bopomofo-annotaties toevoegt aan Chinese tekst in PDF-documenten.

### PDF's openen

- **Auto-redirect**: Elke PDF in de browser wordt automatisch doorgestuurd naar de Bopomofo Reader PDF-viewer
- **Slepen en neerzetten**: Lokale PDF op de viewer neerzetten
- **URL plakken**: PDF-link direct in de viewer plakken
- **Van popup**: Klik op extensiepictogram, dan « PDF-lezer openen »

### PDF-functies

| Functie | Beschrijving |
|---------|--------------|
| **Woordenboekopzoeking** | Klik op een Chinees karakter voor directe Engelse definitie, bopomofo-lezing en TOCFL-niveau |
| **Woordenboekmodus** | Klik op een karakter voor Engelse definities, bopomofo-uitspraak en TOCFL-niveau-badge |
| **Klik-woordenboek** | Klik op Chinese tekst voor woordenboekdefinities (CC-CEDICT Engels, 110.000 items, TOCFL-niveaus) en uitspraak |
| **Selectie-werkbalk** | Selecteer tekst, gebruik werkbalk om voor te lezen, vertalen of kopiëren |
| **Tekstzoeken** | Zoeken op Chinese tekst |
| **Zijbalk** | Inhoudsopgave, paginaminaturen en navigatie |
| **3 thema's** | Donker, licht en sepia-leesmodi |
| **Vertaling** | Selecteer tekst en vertaal via Bing of Google Translate |

### PDF-sneltoetsen

| Sleutel | Actie |
|---------|-------|
| ← / → | Vorige / volgende pagina |
| + / - | In-/uitzoomen |
| Ctrl+F / Cmd+F | Zoeken openen |
| Escape | Alle zwevende panelen sluiten |

> **Opmerking:** Wachtwoordbeveiligde en gescannde (alleen afbeelding) PDF's worden niet ondersteund vanwege ontbrekende tekstlaag voor bopomofo-annotatie.

---

## Sneltoetsen

| Sneltoets | Mac-sneltoets | Actie |
|-----------|---------------|-------|
| `Alt+Shift+B` | `Ctrl+Shift+B` | Bopomofo-annotaties aan/uit |
| `Alt+Shift+S` | `Ctrl+Shift+S` | Geselecteerde tekst voorlezen |
| `Alt+Shift+T` | `Ctrl+Shift+T` | Geselecteerde tekst vertalen |

> **Tip:** Pas sneltoetsen aan in Chrome op `chrome://extensions/shortcuts`.

---

## Instellingengids

| Instelling | Beschrijving |
|------------|--------------|
| **Bopomofo inschakelen** | Hoofdschakelaar voor bopomofo-annotatie |
| **Hele pagina bopomofo** | Toont bopomofo voor alle Chinese karakters (kan layout beïnvloeden) |
| **Bopomofo-stijl** | Keuze tussen toontekens of zonder tonen |
| **Zin-voorleessnelheid** | Snelheid van selectie-voorlezen aanpassen (enkel karakter niet beïnvloed) |
| **Hover-modus** | Hover-gedrag: Woordenboek (CC-CEDICT Engels met TOCFL-niveaus), alleen bopomofo of uit |
| **Vertaaldienst** | Bing Translate of Google Translate |
| **Doeltaal** | Doeltaal voor vertaling (automatisch uit browser-taal) |
| **PDF-detectie** | PDF's automatisch doorsturen naar ingebouwde PDF-lezer |

---

## Veelgestelde vragen

**V: Waarom werkt het niet op sommige pagina's?**  
A: Vanwege beveiliging kunnen extensies niet op speciale pagina's zoals `chrome://`, browserinstellingen of Chrome Web Store draaien.

**V: Wat als bopomofo onjuist is?**  
A: Bopomofo voor polyfone karakters kan fouten bevatten. We verbeteren continu. Deel specifieke gevallen om ons te helpen.

**V: Geen geluid bij tekst-naar-spraak?**  
A: Controleer volume-instellingen en zorg dat Chinese spraakpakketten geïnstalleerd zijn. Spraakondersteuning varieert per browser en OS.

**V: Hele pagina-modus beïnvloedt layout?**  
A: Bopomofo-annotaties vereisen extra ruimte. Schakel hele pagina-modus uit en gebruik hover-tooltips.

**V: Vertaling werkt niet?**  
A: Vertaling vereist internet. Als Bing Translate faalt, probeer Google Translate in instellingen. Sommige netwerken blokkeren vertaaldiensten.

---

## Open-source woordenboekattributie

Bopomofo Reader bundelt offline uitspraak- en woordenboekbronnen uit open-source of community-projecten:

- **Bopomofo-conversie**: pinyin-pro en @pinyin-pro/data/modern voor lokale Mandarijn-uitspraakconversie en woordcorrecties; Bopomofo Reader converteert pinyin-lokalen lokaal naar Zhuyin/Bopomofo en past Taiwan-uitspraak polyfone correcties toe.
- **Chinees-Engels woordenboek**: CC-CEDICT levert Engelse definities en basiswoordenboekitems.
- **Meertalige definities**: CFDICT (Frans), HanDeDict (Duits) en Wiktionary-data van kaikki.org voor Japans, Koreaans, Vietnamees en Chinees.
- **Scriptconversie**: OpenCC-js en het gebundelde lokale conversiemodule voor vereenvoudigd/traditioneel Chinees indien nodig.

Alle woordenboekopzoekingen lopen lokaal in uw browser. Upstream-projecten behouden eigen copyright en licenties; zie Privacybeleid voor details.

---

## Gerelateerde links

- [Privacybeleid](../privacy-policy)
- [Ondersteuning en feedback](../support)

---
