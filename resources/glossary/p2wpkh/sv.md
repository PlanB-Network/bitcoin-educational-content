---
term: P2WPKH
definition: Native SegWit-skript som låser bitcoin till hashen av en publik nyckel, bc1q-adresser.
---

P2WPKH står för *Pay to Witness Public Key Hash*. Det är en standardskriptmodell som används för att fastställa utgiftsvillkor för en UTXO. P2WPKH introducerades i samband med implementeringen av SegWit i augusti 2017.


Det här skriptet liknar P2PKH (*Pay to Public Key Hash*), eftersom det också låser bitcoins baserat på Hash för en publik nyckel, det vill säga en mottagande Address. Skillnaden ligger i hur signaturer och skript inkluderas i transaktionen. I fallet med P2WPKH flyttas informationen om signaturskriptet (`scriptSig`) från den traditionella transaktionsstrukturen till ett separat avsnitt som kallas `Witness`. Denna flytt är en funktion i uppdateringen SegWit (*Segregated Witness*) som hjälper till att förhindra att signaturer kan manipuleras. P2WPKH-transaktioner är i allmänhet billigare när det gäller avgifter jämfört med Legacy-transaktioner, eftersom delen i vittnet kostar mindre.


P2WPKH-adresser skrivs med `Bech32`-kodning med en kontrollsumma i form av BCH-kod. Dessa adresser börjar alltid med `bc1q`. P2WPKH är en version 0 SegWit utdata.