---
term: BIP11

---
BIP introdotto da Gavin Andresen nel marzo 2012 che propone un metodo standard per creare transazioni con più firme su Bitcoin. Questa proposta mira a migliorare la sicurezza dei bitcoin richiedendo firme multiple per convalidare una transazione. BIP11 introduce un nuovo tipo di scrittura, denominata "M-of-N multisig", dove `M` rappresenta il numero minimo di firme richieste tra `N` potenziali chiavi pubbliche. Questo standard utilizza l'opcode `OP_CHECKMULTISIG`, già presente in Bitcoin, ma che in precedenza non era conforme alle regole di standardizzazione dei nodi. Sebbene questo tipo di script non sia più comunemente utilizzato per i portafogli multisig, a favore di P2SH o P2WSH, il suo utilizzo rimane possibile. Viene utilizzato in particolare in metaprotocolli come Stamps. I nodi possono tuttavia scegliere di non trasmettere queste transazioni P2MS con il parametro `permitbaremultisig=0`.

> ► *Oggi questo standard è noto come "bare-multisig" o "P2MS "*