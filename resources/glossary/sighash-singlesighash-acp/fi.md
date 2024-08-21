---
termi: SIGHASH_SINGLE/SIGHASH_ACP
---

SigHash-lipun tyyppi (`0x83`), joka on yhdistetty `SIGHASH_ANYONECANPAY`-modifioijaan (`SIGHASH_ACP`), jota käytetään Bitcoin-siirtojen allekirjoituksissa. Tämä yhdistelmä määrittää, että allekirjoitus koskee vain tiettyä yksittäistä syötettä ja vain ulostuloa, jolla on sama indeksi kuin tällä syötteellä. Muita syötteitä ja ulostuloja voidaan lisätä tai muokata toisten osapuolten toimesta. Tämä konfiguraatio on hyödyllinen yhteistyössä tehtävissä transaktioissa, joissa osallistujat voivat lisätä omia syötteitään rahoittamaan tiettyä ulostuloa.