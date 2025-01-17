---
term: BIP384

---
Introduce la funzione `combo(KEY)` per i descrittori. Questa funzione descrive un insieme di possibili script di output per una determinata chiave pubblica. Copre quindi più tipi di script contemporaneamente, inclusi P2PK, P2PKH, P2WPKH e P2SH-P2WPKH. Se la chiave data è compressa, vengono testati tutti e 4 i tipi di script, mentre se non lo è, vengono testati solo i 2 tipi di script Legacy. L'obiettivo è semplificare la rappresentazione delle chiavi nei descrittori, fornendo un unico metodo per generare diverse varianti di script di output basati sulla stessa chiave pubblica. Il BIP384 è stato implementato insieme a tutti gli altri BIP relativi ai descrittori (tranne il BIP386) nella versione 0.17 di Bitcoin Core.