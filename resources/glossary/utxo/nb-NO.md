---
term: UTXO

---
Forkortelse for *Unspent Transaction Output*. En UTXO er en transaksjonsutgang som ennå ikke har blitt brukt, noe som betyr at den ikke har blitt brukt som input for en ny transaksjon. UTXO-er representerer den brøkdelen av bitcoins som en bruker eier og som for øyeblikket er tilgjengelig for bruk. Hver UTXO er knyttet til et spesifikt utgangsskript (`scriptPubKey`), som definerer de nødvendige betingelsene for å bruke bitcoinsene. Transaksjoner i Bitcoin bruker disse UTXOene som input og skaper nye UTXOer som output. UTXO-modellen er grunnleggende for Bitcoin, ettersom den gjør det enkelt å verifisere at transaksjoner ikke forsøker å bruke bitcoins som ikke eksisterer eller som allerede er brukt.