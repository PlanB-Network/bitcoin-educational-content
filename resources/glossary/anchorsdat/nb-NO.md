---
term: ANCHORS.DAT

---
Fil som brukes i Bitcoin Core-klienten til å lagre IP-adressene til utgående noder som en klient var koblet til før den ble stengt ned. Anchors.dat opprettes hver gang noden stoppes, og slettes når den startes på nytt. Nodene med IP-adresser i denne filen brukes til å raskt etablere forbindelser når noden startes på nytt.