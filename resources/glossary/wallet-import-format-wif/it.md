---
term: Wallet import format (WIF)

definition: Metodo di codifica Base58Check di una chiave privata Bitcoin per facilitarne l'importazione o l'esportazione tra portafogli.
---
Un metodo per codificare una chiave privata Bitcoin in modo che possa essere importata o esportata più facilmente tra diversi portafogli. Il WIF si basa sulla codifica `Base58Check`, che include informazioni sulla versione, la compressione della chiave pubblica corrispondente e un checksum per il rilevamento degli errori di digitazione. Una chiave privata WIF inizia con i caratteri `5` per le chiavi non compresse, o `K` e `L` per le chiavi compresse, e contiene tutti i caratteri necessari per ricostruire la chiave privata originale. Il formato WIF fornisce un mezzo standardizzato per trasferire una chiave privata tra diversi software di portafoglio.