---
term: LIBSECP256K1
---

Libreria C ad alte prestazioni e sicurezza per firme digitali e altre primitive crittografiche sulla curva ellittica `secp256k1`. Poiché questa curva non è mai stata ampiamente utilizzata al di fuori del Bitcoin (a differenza della curva `secp256r1`, spesso preferita), questa libreria vuole essere il riferimento più completo per il suo utilizzo. Lo sviluppo di libsecp256k1 è stato orientato principalmente alle esigenze di Bitcoin, e le caratteristiche destinate ad altre applicazioni possono essere meno testate o verificate. L'uso appropriato di questa libreria richiede un'attenzione particolare, per garantire che sia adatta agli scopi specifici di applicazioni diverse da Bitcoin.


La libreria libsecp256k1 offre una serie di funzionalità, tra cui:




- Firma e verifica ECDSA-secp256k1 e generazione di chiavi crittografiche ;
- Operazioni additive e moltiplicative su chiavi pubbliche e segrete ;
- Serializzazione e analisi di chiavi segrete, chiavi pubbliche e firme ;
- Firma e generazione di chiavi pubbliche a tempo costante con accesso costante alla memoria;
- E una serie di altre primitive crittografiche.