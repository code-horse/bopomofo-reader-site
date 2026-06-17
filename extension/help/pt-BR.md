---
layout: bare
title: Bopomofo Reader - Guia do usuário
lang: pt-BR
---

# Bopomofo Reader - Guia do usuário

> Versão: v1.5.1

## Introdução

Bopomofo Reader é uma extensão de navegador projetada para estudantes de chinês. Com um motor bopomofo melhorado (com dicionário de chinês moderno e mais de 200 correções de caracteres polifônicos), adiciona com precisão anotações de pronúncia bopomofo aos caracteres chineses em páginas web, facilitando o aprendizado da pronúncia chinesa.

---

## Principais funcionalidades

- **Anotação por seleção** — Selecione texto chinês em páginas web para exibir automaticamente bopomofo e botões de voz
- **Modo bopomofo página inteira** — Adicione anotações bopomofo a todos os caracteres chineses da página com um clique
- **Texto para fala** — Clique no botão do alto-falante para ouvir a pronúncia padrão em mandarim
- **Leitura de seleção com efeito karaokê** — Selecione qualquer texto chinês; uma barra de ferramentas compacta aparece com botões de leitura e tradução; a fala destaca palavras ou caracteres em tempo real (efeito karaokê)
- **Tradução de seleção** — Selecione qualquer texto, clique em traduzir para obter tradução instantânea via Bing ou Google Translate, exibida em uma bolha integrada
- **Dicionário ao passar o mouse** — Passe o mouse sobre caracteres anotados para ver bopomofo, definições do dicionário CC-CEDICT inglês (110.000 entradas, níveis TOCFL) e botões de pronúncia
- **Leitor PDF** — Leitor PDF integrado que adiciona automaticamente anotações bopomofo ao texto chinês em documentos PDF
- **Múltiplos estilos bopomofo** — Com marcas de tonalidade (hàn yǔ) ou sem tons (han yu)
- **Atalhos de teclado** — Acesso rápido às funções principais via atalhos personalizáveis
- **Interface multilíngue** — Suporta 38 idiomas de interface

---

## Como usar

### Passo 1: Instalar a extensão

Instale **Bopomofo Reader** na [Chrome Web Store](https://chromewebstore.google.com/detail/bopomofo-reader/jkibgddokcnhedkhmleaohojhlnemmkg), ou carregue em modo desenvolvedor.

### Passo 2: Abrir qualquer página web

Visite qualquer página com conteúdo chinês.

### Passo 3: Selecionar texto ou usar o botão flutuante

Selecione o texto chinês a anotar, ou clique no botão flutuante inferior direito para ativar o modo bopomofo página inteira.

### Passo 4: Ver bopomofo

Passe o mouse sobre os caracteres para ver tooltips bopomofo, clique no ícone do alto-falante para ouvir a pronúncia.

### Passo 5: Ler e traduzir o texto selecionado

Selecione qualquer texto chinês com o mouse. Uma barra de ferramentas compacta aparece com dois botões:
- **🔊 Ler** — Lê o texto selecionado com destaque tipo karaokê
- **🌐 Traduzir** — Mostra uma bolha de tradução integrada abaixo da barra

Você também pode clicar com o botão direito e escolher « Bopomofo Reader > Ler seleção » ou « Bopomofo Reader > Traduzir seleção ».

> **Dica:** Clique no ícone da extensão na barra do navegador para abrir o painel de configurações e ajustar estilo bopomofo, velocidade de fala, motor de tradução, etc.

---

## Leitura de seleção e Karaokê

A função de leitura de seleção permite ler qualquer texto chinês com um clique — ideal para aprender pronúncia de frases e praticar leitura.

**Método 1: Barra de ferramentas de seleção**  
Selecione texto chinês com o mouse. Uma barra compacta aparece com botões 🔊 Ler e 🌐 Traduzir. Clique em Ler para reproduzir. Palavras ou caracteres são destacados em tempo real (efeito karaokê).

**Método 2: Menu de contexto**  
Selecione texto chinês, clique com o botão direito e escolha « Bopomofo Reader > Ler seleção ».

**Método 3: Atalho de teclado**  
Selecione texto e pressione `Alt+Shift+S` (Mac: `Ctrl+Shift+S`).

> **Dica:** O efeito karaokê funciona melhor quando o navegador suporta eventos de limite de palavras TTS. Caso contrário, a extensão usa um fallback baseado em tempo.

---

## Tradução

Selecione qualquer texto na página e use a função de tradução para obter traduções instantâneas.

**Método 1: Barra de ferramentas de seleção**  
Selecione texto, depois clique em 🌐 Traduzir. Uma bolha aparece com o resultado e um botão de copiar.

**Método 2: Menu de contexto**  
Selecione texto, clique com o botão direito e escolha « Bopomofo Reader > Traduzir seleção ».

**Método 3: Atalho de teclado**  
Selecione texto e pressione `Alt+Shift+T` (Mac: `Ctrl+Shift+T`).

**Motores de tradução:**
- **Bing Translate** (padrão) — Powered by Microsoft Translator
- **Google Translate** — Powered by Google

Ambos os motores suportam **108 idiomas de destino**.

Você pode alternar o motor de tradução e o idioma de destino nas configurações da extensão. O idioma de destino é detectado automaticamente do idioma do navegador.

> **Dica:** Clique fora da barra ou bolha para fechar.

---

## Leitor PDF

Bopomofo Reader inclui um leitor PDF integrado que adiciona automaticamente anotações bopomofo ao texto chinês em documentos PDF.

### Abrir PDFs

- **Interceptação automática**: Qualquer PDF aberto no navegador é redirecionado automaticamente ao visualizador PDF Bopomofo Reader
- **Arrastar e soltar**: Solte um arquivo PDF local no visualizador
- **Colar URL**: Cole um link PDF diretamente no visualizador
- **Do popup**: Clique no ícone da extensão, depois em « Abrir leitor PDF »

### Funcionalidades PDF

| Funcionalidade | Descrição |
|----------------|-----------|
| **Consulta ao dicionário** | Clique em um caractere chinês para definição em inglês instantânea, leitura bopomofo e nível TOCFL |
| **Modo dicionário** | Clique em um caractere para ver definições em inglês, pronúncia bopomofo e badge de nível TOCFL |
| **Dicionário ao clicar** | Clique em texto chinês para ver definições (dicionário CC-CEDICT inglês, 110.000 entradas, níveis TOCFL) e pronúncia |
| **Barra de ferramentas de seleção** | Selecione texto, depois use a barra para ler, traduzir ou copiar |
| **Busca de texto** | Buscar por texto chinês |
| **Barra lateral** | Índice, miniaturas de páginas e navegação |
| **3 temas** | Modos de leitura escuro, claro e sépia |
| **Tradução** | Selecione texto e traduza via Bing ou Google Translate |

### Atalhos PDF

| Tecla | Ação |
|-------|------|
| ← / → | Página anterior / seguinte |
| + / - | Aumentar / diminuir zoom |
| Ctrl+F / Cmd+F | Abrir busca |
| Escape | Fechar todos os painéis flutuantes |

> **Nota:** PDFs protegidos por senha e PDFs escaneados (somente imagem) não são suportados, pois não têm camada de texto para anotações bopomofo.

---

## Atalhos de teclado

| Atalho | Atalho Mac | Ação |
|--------|-----------|------|
| `Alt+Shift+B` | `Ctrl+Shift+B` | Ativar/desativar anotações bopomofo |
| `Alt+Shift+S` | `Ctrl+Shift+S` | Ler texto selecionado |
| `Alt+Shift+T` | `Ctrl+Shift+T` | Traduzir texto selecionado |

> **Dica:** Você pode personalizar estes atalhos no Chrome em `chrome://extensions/shortcuts`.

---

## Guia de configurações

| Configuração | Descrição |
|--------------|-----------|
| **Ativar Bopomofo** | Interruptor principal para ativar/desativar anotação bopomofo |
| **Bopomofo página inteira** | Exibe bopomofo para todos os caracteres chineses (pode afetar o layout) |
| **Estilo bopomofo** | Escolher entre marcas de tonalidade ou sem tons |
| **Velocidade de leitura** | Ajustar velocidade de leitura de frases (pronúncia de caracteres individuais não é afetada) |
| **Modo hover** | Comportamento ao passar mouse: Dicionário (definições CC-CEDICT inglês com níveis TOCFL), apenas bopomofo ou desativado |
| **Motor de tradução** | Escolher entre Bing Translate e Google Translate |
| **Idioma de destino** | Definir idioma de destino da tradução (detectado automaticamente do navegador) |
| **Detecção PDF** | Detectar e redirecionar automaticamente PDFs ao leitor PDF integrado |

---

## Perguntas frequentes

**P: Por que não funciona em algumas páginas?**  
R: Por segurança, extensões não podem executar em páginas especiais como `chrome://`, configurações do navegador ou Chrome Web Store.

**P: O que fazer se o bopomofo está incorreto?**  
R: O bopomofo de caracteres polifônicos pode ter erros. Melhoramos continuamente. Compartilhe casos específicos para nos ajudar.

**P: Sem som na conversão de texto para fala?**  
R: Verifique as configurações de volume e certifique-se de que pacotes de voz chineses estão instalados. O suporte de fala varia entre navegadores e sistemas operacionais.

**P: O modo página inteira afeta o layout?**  
R: Anotações bopomofo requerem espaço adicional, o que pode afetar o layout. Desative o modo página inteira e use tooltips ao passar o mouse.

**P: A tradução não funciona?**  
R: A tradução requer conexão à Internet. Se Bing Translate falhar, tente Google Translate nas configurações. Algumas redes podem bloquear serviços de tradução.

---

## Atribuição de dicionários de código aberto

Bopomofo Reader inclui recursos de pronúncia e dicionário offline de projetos de código aberto ou da comunidade:

- **Conversão bopomofo**: pinyin-pro e @pinyin-pro/data/modern alimentam a conversão local de pronúncia mandarim e correções em nível de palavra; Bopomofo Reader converte sílabas pinyin em Zhuyin/Bopomofo localmente e aplica correções polifônicas de pronúncia taiwanesa.
- **Dicionário chinês-inglês**: CC-CEDICT fornece definições em inglês e entradas base do dicionário.
- **Definições multilíngues**: CFDICT (francês), HanDeDict (alemão) e dados derivados de Wiktionary de kaikki.org fornecem definições em japonês, coreano, vietnamita e chinês.
- **Conversão de script**: OpenCC-js e o módulo de conversão local integrado são usados para conversão chinês simplificado/tradicional quando necessário.

Todas as consultas ao dicionário são executadas localmente no navegador. Os projetos upstream mantêm seus próprios direitos e licenças; consulte a Política de Privacidade para mais detalhes.

---

## Links relacionados

- [Política de Privacidade](../privacy-policy)
- [Suporte e feedback](../support)

---
