---
term: SIGHASH_SINGLE/SIGHASH_ACP

---
Bitcoin-tapahtumien allekirjoituksissa käytetty SigHash-merkinnän tyyppi (`0x83`) yhdistettynä `SIGHASH_ANYONECANPAY`-modifikaattoriin (`SIGHASH_ACP`). Tämä yhdistelmä määrittää, että allekirjoitus koskee vain tiettyä yksittäistä syötettä ja vain tuotosta, jolla on sama indeksi kuin tällä syötteellä. Muut osapuolet voivat lisätä tai muuttaa muita tuloja ja lähtöjä. Tämä määritys on hyödyllinen yhteistoiminnallisissa transaktioissa, joissa osallistujat voivat lisätä omia panoksiaan tietyn tuotoksen rahoittamiseksi.
