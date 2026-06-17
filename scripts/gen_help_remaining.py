#!/usr/bin/env python3
"""Generate remaining help locale files with full translations."""
import os

BASE = os.path.join(os.path.dirname(__file__), "..", "extension", "help")

def write(name, content):
    with open(os.path.join(BASE, name), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"wrote {name}")

# Shared attribution block translations
ATTR = {
    "it": """- **Conversione bopomofo**: pinyin-pro e @pinyin-pro/data/modern alimentano la conversione locale della pronuncia mandarina e le correzioni a livello di parola; Bopomofo Reader converte le sillabe pinyin in Zhuyin/Bopomofo localmente e applica correzioni polifoniche di pronuncia taiwanese.
- **Dizionario cinese-inglese**: CC-CEDICT fornisce definizioni inglesi e voci base del dizionario.
- **Definizioni multilingue**: CFDICT (francese), HanDeDict (tedesco) e dataset derivati da Wiktionary di kaikki.org forniscono definizioni in giapponese, coreano, vietnamita e cinese.
- **Conversione script**: OpenCC-js e il modulo di conversione locale integrato sono usati per la conversione cinese semplificato/tradizionale quando necessario.

Tutte le ricerche nel dizionario avvengono localmente nel browser. I progetti upstream mantengono i propri diritti e licenze; consulta la Politica sulla privacy per maggiori dettagli.""",
    "pt": """- **Conversão bopomofo**: pinyin-pro e @pinyin-pro/data/modern alimentam a conversão local de pronúncia mandarim e correções em nível de palavra; Bopomofo Reader converte sílabas pinyin em Zhuyin/Bopomofo localmente e aplica correções polifônicas de pronúncia taiwanesa.
- **Dicionário chinês-inglês**: CC-CEDICT fornece definições em inglês e entradas base do dicionário.
- **Definições multilingues**: CFDICT (francês), HanDeDict (alemão) e dados derivados de Wiktionary de kaikki.org fornecem definições em japonês, coreano, vietnamita e chinês.
- **Conversão de script**: OpenCC-js e o módulo de conversão local integrado são usados para conversão chinês simplificado/tradicional quando necessário.

Todas as consultas ao dicionário são executadas localmente no navegador. Os projetos upstream mantêm seus próprios direitos e licenças; consulte a Política de Privacidade para mais detalhes.""",
}

def make_file(title, lang, rtl, h1, ver, sections):
    fm = f"""---
layout: bare
title: {title}
lang: {lang}
"""
    if rtl:
        fm += "dir: rtl\n"
    fm += "---\n"
    return fm + sections

# Due to size, load from pre-built files - script writes key remaining locales
FILES = {}
