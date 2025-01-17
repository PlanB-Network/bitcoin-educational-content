---
term: WITNESSSSSCRIPT

---
Skripti, joka määrittää ehdot, joiden mukaisesti bitcoineja voidaan käyttää P2WSH- tai P2SH-P2WSH UTXO:sta. Tyypillisesti `witnessScript` määrittää SegWit-standardin mukaisen monisignatuurilompakon ehdot. Näissä skriptistandardeissa UTXO:n `scriptPubKey` (ulostulo) sisältää `witnessScript`:n hashin. Jotta tätä UTXO:ta voitaisiin käyttää syötteenä uudessa transaktiossa, haltijan on paljastettava alkuperäinen `witnessScript` todistaakseen, että se vastaa `scriptPubKey`:ssä olevaa sormenjälkeä. Tämän jälkeen `witnessScript` on sisällytettävä transaktion `scriptWitness`-tietueeseen, joka sisältää myös skriptin validointiin tarvittavat elementit, kuten allekirjoitukset. Näin ollen `witnessScript` vastaa SegWitissä P2SH-tapahtuman `redeemScript`:iä sillä erotuksella, että se sijoitetaan tapahtuman todistajaan eikä `scriptSig`:iin.

> ► *Varoitus, `witnessScript` ei pidä sekoittaa `scriptWitness`:iin. Siinä missä `witnessScript` määrittelee P2WSH- tai P2SH-P2WSH-UTXO:n käyttöehdot ja muodostaa oman skriptinsä, `scriptWitness` sisältää minkä tahansa SegWit-syötteen todistajatiedot.*