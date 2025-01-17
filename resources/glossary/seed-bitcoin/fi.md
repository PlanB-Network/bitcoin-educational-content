---
term: SEED (BITCOIN)

---
Bitcoinin yhteydessä siemen on 512-bittinen arvo, jota käytetään kaikkien HD-lompakkoon (Hierarchical Deterministic) liittyvien yksityisten ja julkisten avainten johtamiseen. Teknisesti ottaen siemen on eri arvo kuin palautuslause (tai muistisana). Lause, joka koostuu yleensä 12 tai 24 sanasta, luodaan pseudosattumanvaraisesti entropialähteestä ja täydennetään tarkistussummalla. Tämä lause helpottaa ihmisen varmuuskopiointia antamalla tekstimuotoisen esityksen lompakon pohjalla olevasta arvosta.

Varsinaisen siemenen saamiseksi palautuslausetta, johon mahdollisesti liittyy valinnainen salasana, käsitellään PBKDF2-algoritmilla (*Password-Based Key Derivation Function 2*). Laskennan tuloksena saadaan 512-bittinen siemen. Tätä siementä käytetään deterministisesti pääavaimen ja sen jälkeen koko HD-lompakon avainsarjan luomiseen BIP32:n mukaisesti.

![](../../dictionnaire/assets/31.webp)

> ► *Kielessä suurin osa bitcoin-käyttäjistä viittaa kuitenkin muistisääntöön puhuessaan "siemenestä", eikä välitilaan, joka on muistisäännön ja pääavaimen välissä.*