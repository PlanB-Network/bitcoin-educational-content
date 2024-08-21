---
termi: WITNESSSCRIPT
---

Skripti, joka määrittelee ehdot, joiden mukaisesti bitcoineja voidaan käyttää P2WSH tai P2SH-P2WSH UTXOista. Tyypillisesti `witnessScript` määrittää moniallekirjoituslompakon ehdot SegWit-standardin mukaisesti. Näissä skriptistandardeissa UTXO:n (tuloksen) `scriptPubKey` sisältää hashin `witnessScriptistä`. Jotta tämä UTXO voidaan käyttää syötteenä uudessa siirrossa, haltijan on paljastettava alkuperäinen `witnessScript`, todistaakseen sen vastaavan sormenjälkeä `scriptPubKeyssä`. `witnessScript` on sen jälkeen sisällytettävä siirron `scriptWitnessiin`, joka sisältää myös elementit skriptin validointiin, kuten allekirjoitukset. Siksi `witnessScript` on SegWitin vastine `redeemScriptille` P2SH-siirrossa, eroavaisuutena se, että se sijoitetaan siirron todistajaosaan, eikä `scriptSigiin`.

> ► *Varoitus, `witnessScriptiä` ei tule sekoittaa `scriptWitnessiin`. Vaikka `witnessScript` määrittelee P2WSH:n tai P2SH-P2WSH:n UTXO:n käyttöehdot ja muodostaa itsessään skriptin, `scriptWitness` sisältää kaikki SegWit-syötteen todistusdatan.*