---
term: BIP0093
---

BIP informativo che propone uno standard per il salvataggio e il ripristino del seed di un portafoglio deterministico gerarchico (secondo BIP32) utilizzando la condivisione segreta della chiave di Shamir. Questo protocollo definisce il formato "codex32", che si ispira al formato bech32, introducendo una stringa strutturata composta da un prefisso, un parametro di soglia, un identificatore, un indice di condivisione, un payload e un checksum (BCH). Il metodo consente di suddividere il seed in un massimo di 31 condivisioni, di cui è richiesta una soglia definita (tra 1 e 9) per il recupero completo del seed.