---
termine: BIP118
---

Proposta per il miglioramento di Bitcoin volta all'introduzione di due nuovi modificatori di SigHash Flag: `SIGHASH_ANYPREVOUT` e `SIGHASH_ANYPREVOUTANYSCRIPT`. Queste funzionalità estendono le capacità delle transazioni Bitcoin, in particolare per quanto riguarda i contratti intelligenti e le soluzioni di overlay come la Lightning Network. BIP118 consentirebbe in modo notevole l'uso di Eltoo. Il principale vantaggio di `SIGHASH_ANYPREVOUT` è permettere il riutilizzo delle firme attraverso multiple transazioni, offrendo maggiore flessibilità. Specificamente, questi SigHash consentono una firma che non copre nessuno degli input della transazione.