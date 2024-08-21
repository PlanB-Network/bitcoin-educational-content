---
termi: SCRIPTWITNESS
---

Elementti SegWit-siirtotapahtumien merkinnöissä, joka sisältää allekirjoitukset ja julkiset avaimet, jotka ovat tarpeen lähetettyjen bitcoinien lunastamiseksi. Samankaltainen kuin perinteisten siirtojen `scriptSig`, `scriptWitness` ei kuitenkaan sijaitse samassa paikassa. Todellakin, juuri tämä osa, jota kutsutaan "todistajaksi" (`*witness*` englanniksi), siirretään erilliseen tietokantaan ratkaisemaan siirtojen muunneltavuusongelma. Jokaisella SegWit-syötteellä on oma `scriptWitness`-elementtinsä, ja kaikki `scriptWitness`-elementit yhdessä muodostavat siirtotapahtuman `Witness`-kentän.

> ► *Ole varovainen, ettei sekoita `scriptWitness`-elementtiä `witnessScript`-elementtiin. Vaikka `scriptWitness` sisältää todistusdatan mille tahansa SegWit-syötteelle, `witnessScript` määrittelee kulutusehdot P2WSH- tai P2SH-P2WSH UTXO:lle ja muodostaa itsessään skriptin, samankaltaisen kuin `redeemScript` P2SH-lähdölle.*