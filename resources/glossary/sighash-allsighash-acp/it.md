---
term: SIGHASH_ALL/SIGHASH_ACP

---
Tipo di flag SigHash (`0x81`) combinato con il modificatore `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) utilizzato nelle firme delle transazioni Bitcoin. Questa combinazione specifica che la firma si applica a tutti gli output e solo a uno specifico input della transazione. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` consente ad altri partecipanti di aggiungere ulteriori input alla transazione dopo la firma iniziale. È particolarmente utile in scenari collaborativi, come le transazioni di crowdfunding, dove i diversi partecipanti possono aggiungere i propri input preservando l'integrità degli output impegnati dal firmatario iniziale.