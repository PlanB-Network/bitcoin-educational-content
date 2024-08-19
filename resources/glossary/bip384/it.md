---
term: BIP384
---

Introduce la funzione `combo(KEY)` per i descrittori. Questa funzione descrive un insieme di possibili script di output per una data chiave pubblica. Copre quindi contemporaneamente più tipi di script, inclusi P2PK, P2PKH, P2WPKH e P2SH-P2WPKH. Se la chiave fornita è compressa, tutti e 4 i tipi di script vengono testati, e se non lo è, vengono testati solo i 2 tipi di script Legacy. L'obiettivo è semplificare la rappresentazione delle chiavi nei descrittori fornendo un unico metodo per generare diverse varianti di script di output basate sulla stessa chiave pubblica. BIP384 è stato implementato insieme a tutti gli altri BIP relativi ai descrittori (eccetto BIP386) nella versione 0.17 di Bitcoin Core.