---
term: BIP383
---

Introduce le funzioni `multi(NUM, KEY, ..., KEY)` e `sortedmulti(NUM, KEY, ..., KEY)` per i descrittori. Queste funzioni consentono la descrizione di script multisignature nei descrittori, con `sortedmulti` che ordina le chiavi pubbliche in ordine lessicografico per garantire la compatibilità durante l'importazione. BIP383 è stato implementato insieme a tutti gli altri BIP relativi ai descrittori (eccetto BIP386) nella versione 0.17 di Bitcoin Core.