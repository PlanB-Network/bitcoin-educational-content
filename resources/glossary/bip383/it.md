---
term: BIP383

---
Introduce le funzioni `multi(NUM, KEY, ..., KEY)` e `sortedmulti(NUM, KEY, ..., KEY)` per i descrittori. Queste funzioni consentono di descrivere gli script a più firme nei descrittori, mentre `sortedmulti` ordina le chiavi pubbliche in ordine lessicografico per garantire la compatibilità durante l'importazione. BIP383 è stato implementato insieme a tutti gli altri BIP relativi ai descrittori (tranne BIP386) nella versione 0.17 di Bitcoin Core.