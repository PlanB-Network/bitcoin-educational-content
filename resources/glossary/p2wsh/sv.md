---
term: P2WSH
definition: Native SegWit-skript som låser bitcoin till hashen av ett skript, bc1q-adresser.
---

P2WSH står för *Pay to Witness Script Hash*. Det är en standardskriptmodell som används för att fastställa utgiftsvillkor för en UTXO. P2WSH introducerades i samband med implementeringen av SegWit i augusti 2017.


Det här skriptet liknar P2SH (*Pay to Public Script Hash*), eftersom det också låser bitcoins baserat på Hash i ett skript. Skillnaden ligger i hur signaturer och skript inkluderas i transaktionen. För att spendera bitcoins på den här typen av skript måste mottagaren tillhandahålla det ursprungliga skriptet, kallat `witnessScript` (motsvarande `redeemscript`), tillsammans med de nödvändiga signaturerna. Denna mekanism gör det möjligt att implementera mer sofistikerade utgiftsvillkor, till exempel multisigs.


I samband med P2WSH flyttas informationen om signaturens skript (`scriptWitness`, motsvarande `scriptSig`) från den traditionella transaktionsstrukturen till ett separat avsnitt som kallas `Witness`. Denna flyttning är en funktion i SegWit-uppdateringen (*Segregated Witness*) som hjälper till att förhindra att signaturer kan manipuleras. P2WSH-transaktioner är i allmänhet mindre dyra när det gäller avgifter jämfört med Legacy-transaktioner, eftersom delen i vittnet kostar mindre.


P2WSH-adresser skrivs med `Bech32`-kodning med en kontrollsumma i form av BCH-kod. Dessa adresser börjar alltid med `bc1q`. P2WSH är en version 0 SegWit utdata.