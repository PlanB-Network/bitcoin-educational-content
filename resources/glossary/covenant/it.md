---
term: PENSIERO

---
Un meccanismo che consente di imporre condizioni specifiche su come un determinato pezzo di valuta può essere speso, anche in transazioni future. Oltre alle condizioni normalmente consentite dal linguaggio di script di un UTXO, il covenant impone ulteriori vincoli su come questo Bitcoin può essere speso nelle transazioni successive. Tecnicamente, l'istituzione di un patto avviene quando la `scriptPubKey` di un UTXO definisce restrizioni sulla `scriptPubKey` degli output di una transazione che spende tale UTXO. Ampliando la portata dello script, i patti consentirebbero numerosi sviluppi su Bitcoin, come l'ancoraggio bilaterale delle drivechain, l'implementazione dei caveau o il miglioramento dei sistemi di overlay come Lightning. Le proposte di patto si differenziano in base a tre criteri:


- Il loro scopo;
- La loro attuazione;
- La loro ricorsività.

Esistono molte proposte che consentirebbero l'uso di covenant su Bitcoin. Le più avanzate nel processo di implementazione sono: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO) e `OP_VAULT`. Tra le altre proposte, ci sono: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, ecc.

Per capire meglio il concetto di patto, considerate questa analogia: immaginate una cassaforte contenente 500€ in banconote di piccolo taglio. Se riuscite a sbloccare questa cassaforte con la chiave giusta, siete liberi di usare questo denaro come volete. Questa è la situazione normale con i Bitcoin. Ora immaginate che la stessa cassaforte non contenga 500€ in banconote, ma piuttosto buoni pasto di valore equivalente. Se riuscite ad aprire la cassaforte, potete utilizzare questa somma. Tuttavia, la vostra libertà di spesa è limitata, poiché potete usare questi buoni solo per pagare in determinati ristoranti. Quindi, c'è una prima condizione per spendere questo denaro, che è quella di riuscire ad aprire la cassaforte con la chiave appropriata. Ma c'è anche un'ulteriore condizione che riguarda l'uso futuro di questa somma: deve essere spesa esclusivamente nei ristoranti convenzionati, e non liberamente. Questo sistema di vincoli sulle transazioni future è quello che viene chiamato patto.

> *In francese non esiste un termine che catturi esattamente il significato della parola "patto". Si potrebbe parlare di "clausola", "patto" o "impegno", ma questi non corrispondono esattamente al termine "patto". Questo termine è mutuato dalla terminologia giuridica che permette di descrivere una clausola contrattuale che impone obblighi persistenti su una proprietà*