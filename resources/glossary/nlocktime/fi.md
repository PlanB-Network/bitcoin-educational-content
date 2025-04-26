---
term: NLOCKTIME

---
Transaktioihin upotettu kenttä, joka asettaa aikapohjaisen ehdon, jota ennen transaktiota ei voida lisätä kelvolliseen lohkoon. Tämän parametrin avulla voidaan määrittää tarkka aika (Unix-ajastinleima) tai tietty määrä lohkoja ehdoksi sille, että transaktio katsotaan kelvolliseksi. Kyseessä on siis absoluuttinen aikalukko (ei suhteellinen). `nLockTime` vaikuttaa koko transaktioon ja mahdollistaa käytännössä ajan tarkistamisen, kun taas op-koodi `OP_CHECKLOCKTIMEVERIFY` mahdollistaa vain pinon ylimmän arvon vertaamisen `nLockTime`-arvoon.