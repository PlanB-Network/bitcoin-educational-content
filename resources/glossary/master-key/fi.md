---
termi: PÄÄAVAIN
---

HD (Hierarkkinen Deterministinen) lompakoissa pääyksityisavain on uniikki yksityisavain, joka johdetaan lompakon siemenestä. Pääavaimen saamiseksi `HMAC-SHA512` funktiota sovelletaan siemeneen, käyttäen sanoja "*Bitcoin siemen*" kirjaimellisesti avaimena. Tämän toimenpiteen tulos tuottaa 512-bittisen tulosteen, josta ensimmäiset 256 bittiä muodostavat pääavaimen, ja jäljelle jäävät 256 bittiä muodostavat pääketjukoodin. Pääavain ja pääketjukoodi toimivat lähtökohtana kaikkien lapsi yksityis- ja julkisavainten johdannaisille HD lompakon puurakenteessa. Siksi pääyksityisavain on johdannaisuuden syvyydessä 0.

![](../../dictionnaire/assets/19.png)