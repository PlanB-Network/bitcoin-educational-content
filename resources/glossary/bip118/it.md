---
term: BIP118

---
Proposta di miglioramento di Bitcoin volta a introdurre due nuovi modificatori del flag SigHash: `SIGHASH_ANYPREVOUT` e `SIGHASH_ANYPREVOUTANYSCRIPT`. Queste caratteristiche estendono le capacità delle transazioni Bitcoin, in particolare in termini di contratti intelligenti e soluzioni di overlay come la Lightning Network. Il BIP118 permetterebbe in particolare l'uso di Eltoo. Il vantaggio principale di `SIGHASH_ANYPREVOUT` è quello di consentire il riutilizzo delle firme in più transazioni, il che offre maggiore flessibilità. In particolare, queste SigHash consentono una firma che non copre nessuno degli input della transazione.