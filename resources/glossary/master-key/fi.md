---
term: MASTER KEY

---
HD-lompakoissa (Hierarchical Deterministic) yksityinen pääavain on ainutlaatuinen yksityinen avain, joka on johdettu lompakon siemenestä. Pääavaimen saamiseksi siemeneen sovelletaan `HMAC-SHA512`-funktiota käyttäen sanoja "*Bitcoin seed*" kirjaimellisesti avaimena. Tämän operaation tuloksena saadaan 512-bittinen tuloste, josta 256 ensimmäistä bittiä muodostavat pääavaimen ja loput 256 bittiä muodostavat pääketjukoodin. Pääavain ja pääketjukoodi toimivat lähtökohtana kaikkien HD-lompakon puurakenteessa olevien yksityisten ja julkisten lapsiavainten johtamiselle. Näin ollen yksityinen pääavain on johdannassa syvyydellä 0.

![](../../dictionnaire/assets/19.webp)
