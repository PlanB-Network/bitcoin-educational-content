---
term: SCRIPTWITNESS

---
SegWit-tapahtumamerkintöjen elementti, joka sisältää allekirjoitukset ja julkiset avaimet, joita tarvitaan tapahtumassa lähetettyjen bitcoinien lukituksen avaamiseen. Samanlainen kuin Legacy-tapahtumien `scriptSig`, `scriptWitness` ei kuitenkaan sijaitse samassa paikassa. Juuri tämä "todistajaksi" (englanniksi `*witness*`) kutsuttu osa siirretään erilliseen tietokantaan, jotta transaktion muokattavuusongelma voidaan ratkaista. Jokaisella SegWit-syötteellä on oma `scriptWitness`-elementtinsä, ja kaikki `scriptWitness`-elementit muodostavat yhdessä tapahtuman `Witness`-kentän.

> ► *Varo sekoittamasta `scriptWitness` ja `witnessScript` keskenään. Vaikka `scriptWitness` sisältää minkä tahansa SegWit-syötteen todistajatiedot, `witnessScript` määrittelee P2WSH- tai P2SH-P2WSH-UTXO:n käyttöehdot ja muodostaa oman skriptinsä, joka on samanlainen kuin P2SH-ulostulon `redeemScript`.*