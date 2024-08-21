---
termi: SIGHASH_ALL/SIGHASH_ACP
---

SigHash-lipun tyyppi (`0x81`), joka on yhdistetty `SIGHASH_ANYONECANPAY`-modifioijaan (`SIGHASH_ACP`), jota käytetään Bitcoin-siirtojen allekirjoituksissa. Tämä yhdistelmä määrittää, että allekirjoitus koskee kaikkia lähtöjä ja vain tiettyä siirron sisääntuloa. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` sallii muiden osallistujien lisätä lisäsisääntuloja siirtoon sen alkuperäisen allekirjoituksen jälkeen. Se on erityisen hyödyllinen yhteistyöskentelyskenaarioissa, kuten joukkorahoitustransaktioissa, joissa eri osallistujat voivat lisätä omat sisääntulonsa säilyttäen samalla alkuperäisen allekirjoittajan sitoutumien lähtöjen eheyden.