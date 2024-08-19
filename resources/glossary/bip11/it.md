---
termine: BIP11
---

BIP introdotto da Gavin Andresen nel marzo 2012 che propone un metodo standard per creare transazioni multisignature su Bitcoin. Questa proposta mira a migliorare la sicurezza dei bitcoin richiedendo più firme per convalidare una transazione. BIP11 introduce un nuovo tipo di script, denominato "M-di-N multisig", dove `M` rappresenta il numero minimo di firme richieste tra `N` potenziali chiavi pubbliche. Questo standard utilizza l'opcode `OP_CHECKMULTISIG`, già esistente in Bitcoin, ma che precedentemente non era conforme alle regole di standardizzazione dei nodi. Sebbene questo tipo di script non sia più comunemente usato per effettive wallet multisig, preferendo P2SH o P2WSH, il suo utilizzo rimane possibile. È notevolmente utilizzato in meta-protocolli come Stamps. I nodi possono, tuttavia, scegliere di non inoltrare queste transazioni P2MS con il parametro `permitbaremultisig=0`.

> ► *Oggi, questo standard è conosciuto come "bare-multisig" o "P2MS".*