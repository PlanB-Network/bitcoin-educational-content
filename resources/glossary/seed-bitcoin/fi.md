---
termi: SEED (BITCOIN)
---

Bitcoinin kontekstissa seed on 512-bittinen arvo, jota käytetään johdattamaan kaikki yksityiset ja julkiset avaimet, jotka liittyvät HD (Hierarkkinen Deterministinen) lompakkoon. Teknisesti seed on eri arvo kuin palautuslause (tai mnemoninen). Lause, joka tyypillisesti koostuu 12 tai 24 sanasta, generoidaan pseudo-satunnaisesti entropian lähteestä ja täydennetään tarkistussummalla. Tämä lause helpottaa ihmisen tekemää varmuuskopiointia tarjoamalla tekstuaalisen esityksen lompakon perustana olevasta arvosta.

Jotta varsinaisen seedin saa, palautuslause, mahdollisesti valinnaisen salasanan kanssa, käsitellään PBKDF2-algoritmin (*Password-Based Key Derivation Function 2*) läpi. Tämän laskennan tulos on 512-bittinen seed. Juuri tätä seediä käytetään deterministisesti pääavaimen generointiin, ja sitten koko avainsetin generointiin HD-lompakkoon, BIP32:n mukaisesti.

![](../../dictionnaire/assets/31.png)

> ► *Kuitenkin yleisessä kielessä suurin osa bitcoin-käyttäjistä viittaa mnemoniseen lauseeseen puhuessaan "seedistä", eikä johdannaisvaiheeseen, joka sijaitsee mnemonisen lauseen ja pääavaimen välillä.*