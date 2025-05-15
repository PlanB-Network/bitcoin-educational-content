---
name: Sviluppo su Lightning con SDK
goal: Migliora le tue competenze di sviluppo su Lightning con una formazione intermedia in Rust e SDK.
objectives:
  - Abituarsi al linguaggio Rust
  - Capire perché utilizzare Rust per lo sviluppo di Bitcoin
  - Ottenere le basi dell'SDK
---

# Avanzare nelle tue competenze di sviluppo LN

Benvenuto nel tuo percorso LN con l'SDK.

In questo corso, imparerai le basi del libro Rust, quindi passerai alla programmazione LN utilizzando gli SDK e concluderai con alcuni esercizi pratici. I nostri insegnanti provenienti da diverse esperienze ti guideranno verso competenze pratiche e ti spiegheranno le diverse sfide che gli ingegneri LN affrontano spesso.

Questo corso è stato registrato durante un seminario LIVE organizzato da Fulgur'Ventures durante l'evento LN Tuscany nell'ottobre 2023.

Buon corso!

+++

# Introduzione
<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>

## Panoramica del corso
<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>

**Introduzione**

Benvenuto in questo corso avanzato di programmazione sugli SDK. In questa formazione, imparerai le basi di Rust, quindi ti concentrerai su BTC e Rust e concluderai con alcuni esercizi pratici utilizzando gli SDK.

Questa formazione sarà disponibile solo in inglese per ora ed è stata parte di un seminario dal vivo organizzato lo scorso ottobre in Toscana da Fulgure Venture. Il programma dell'evento LIVE può essere trovato di seguito e questa formazione si concentrerà solo sulla prima settimana. La seconda metà era incentrata su RGB e può essere trovata nel corso RGB.

**Insegnanti**

Un grande ringraziamento ai nostri insegnanti che hanno fatto parte di questo programma:

- Alekos: "Ciao, sono un programmatore e hacker italiano. Ho lavorato su vari progetti come bitcoindevkit, magicalbitcoin e h4ckbs"
- Andrei: "Esperto di Lightning presso LIPA"
- Gabriel: "Scrivo codice e faccio cose."
- Jesse de wit: "Appassionato di Lightning network | sviluppatore | Breez"

**Programma del seminario**

Settimana 1 dell'evento LN Tuscany
![image](assets/1.webp)

Una volta completato questo corso, se sei interessato alla formazione successiva, ecco la seconda parte del programma:
![image](assets/2.webp)


Questa formazione ti offre l'opportunità di sviluppare le tue competenze di programmazione sul Lightning Network utilizzando Rust e vari SDK. È progettata per sviluppatori con una buona padronanza della programmazione che desiderano approfondire lo sviluppo specifico del Lightning Network. Imparerai le basi del linguaggio Rust, perché è adatto allo sviluppo su Bitcoin, e poi passerai alla pratica utilizzando SDK specializzati.

**Sezione 2: Impara a programmare con Rust**  
In questa sezione scoprirai i fondamenti di Rust attraverso una serie di capitoli progressivi. Imparerai a scrivere codice in Rust, a comprenderne le specificità e a padroneggiare le sue funzionalità essenziali attraverso sette parti dettagliate. Questo modulo è essenziale per capire perché Rust è un linguaggio privilegiato per lo sviluppo su Bitcoin.

**Sezione 3: Rust & Bitcoin**  
Qui esploreremo in profondità perché Rust è una scelta rilevante per lo sviluppo su Bitcoin. Scoprirai il suo modello di gestione degli errori, lo strumento UniFFI e i tratti asincroni, elementi fondamentali per la costruzione di software robusto e sicuro.

**Sezione 4: Sviluppo LNP/BP con SDK**  
Imparerai a sviluppare nodi LN utilizzando vari SDK come Breez SDK e Greenlight per Lipa. Vedrai come implementare applicazioni Lightning Network utilizzando librerie progettate per facilitare lo sviluppo di applicazioni Bitcoin e Lightning.

Pronto a sviluppare le tue competenze sul Lightning Network con Rust? Iniziamo!
# Impara a programmare con il libro Rust
<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>

## Introduzione a Rust (1/7)
<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

## Introduzione a Rust (2/7)
<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>

:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::

## Introduzione a Rust (3/7)
<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>

:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

## Introduzione a Rust (4/7)
<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>

:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

## Introduzione a Rust (5/7)
<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>

:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

## Introduzione a Rust (6/7)
<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>

:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

## Introduzione a Rust (7/7)
<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>

:::video id=5e96914d-df02-4781-ae54-b06008952301:::

# Rust & BTC
<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>

## Perché Rust per Bitcoin
<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>

:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::

## Modello di errore
<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>

:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

## Unniffit
<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>

:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

## Async traits
<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>

:::video id=8926dd48-3613-43b6-a509-60ba26ec337f:::

# Sviluppo di LNP/BP con SDK
<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>

## Nodo LN su SDK
<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>
:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::
## Breez sdk
<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>

:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

## Greenlight per lipa
<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>

:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

## Breez sdk per lipa
<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>

:::video id=f2770a37-a22f-43d7-9334-8de60eaacff8:::

# Conclusioni
<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Recensioni & Valutazioni
<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>
<isCourseReview>true</isCourseReview>

## Conclusioni
<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>
<isCourseConclusion>true</isCourseConclusion>
