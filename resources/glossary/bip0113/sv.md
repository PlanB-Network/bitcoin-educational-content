---
term: BIP0113
---

En ändring har införts i beräkningen av alla tidslåsoperationer (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` och `OP_CHECKSEQUENCEVERIFY`). Den anger att för att utvärdera giltigheten av tidslås måste de nu jämföras med MTP (*Median Time Past*), som är medianen av tidsstämplarna för de senaste 11 blocken. Tidigare användes endast Timestamp för det föregående blocket. Den här metoden gör systemet mer förutsägbart och förhindrar att miners manipulerar tidsreferensen. BIP113 introducerades via en Soft Fork den 4 juli 2016, tillsammans med BIP68 och BIP112, som för första gången aktiverades med BIP9-metoden.