---
term: SIGHASH_ALL/SIGHASH_ACP

---
Bitcoin-tapahtumien allekirjoituksissa käytetty SigHash-merkinnän tyyppi (`0x81`) yhdistettynä `SIGHASH_ANYONECANPAY`-modifikaattoriin (`SIGHASH_ACP`). Tämä yhdistelmä määrittää, että allekirjoitus koskee kaikkia transaktion ulostuloja ja vain tiettyä tuloa. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` mahdollistaa sen, että muut osallistujat voivat lisätä transaktioon lisää syötteitä sen alkuperäisen allekirjoituksen jälkeen. Se on erityisen hyödyllinen yhteistyöskenaarioissa, kuten joukkorahoitustapahtumissa, joissa eri osallistujat voivat lisätä omia panoksiaan säilyttäen alkuperäisen allekirjoittajan sitoutuneiden tuotosten eheyden.
