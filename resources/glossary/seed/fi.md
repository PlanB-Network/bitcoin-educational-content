---
term: VILJA
---

Bitcoin-hierarkkisen deterministisen portfolion yhteydessä seed on 512-bittinen tieto, joka on johdettu satunnaistapahtumasta. Sitä käytetään deterministisesti ja hierarkkisesti generate yksityisten avainten ja niitä vastaavien julkisten avainten joukkoon Bitcoin-salkkua varten. seed sekoitetaan usein itse palautuslausekkeeseen. Se ei kuitenkaan ole sama asia. seed saadaan soveltamalla `PBKDF2`-funktiota Mnemonic-lauseeseen ja mihin tahansa passphrase-lauseeseen.


seed keksittiin yhdessä BIP32:n kanssa, joka määritteli hierarkkisen deterministisen portfolion perustan. Tässä standardissa seed:n mitat olivat 128 bittiä. Tämän ansiosta kaikki salkun avaimet voidaan johtaa yhdestä ainoasta tiedosta, toisin kuin JBOK-salkuissa (*Just a Bunch Of Keys*), jotka vaativat uusia varmuuskopioita jokaista luotua avainta varten. BIP39 ehdotti tämän jälkeen seed:n koodausta, jotta ihmisten olisi helpompi lukea sitä. Tämä koodaus tapahtuu lauseen muodossa, jota kutsutaan yleisesti Mnemonic-lauseeksi tai palautuslauseeksi. Tällä standardilla vältetään virheet seed:n tallentamisessa erityisesti tarkistussumman käytön ansiosta.


Bitcoin-kontekstin ulkopuolella seed on kryptografiassa yleisesti generate-kryptografisten avainten tai laajemmin minkä tahansa pseudosattumanumerogeneraattorin tuottaman datan alkuarvo. Tämän alkuarvon on oltava satunnainen ja arvaamaton, jotta salausjärjestelmän turvallisuus voidaan taata. seed tuo järjestelmään entropiaa, mutta sitä seuraava generointiprosessi on deterministinen.


> ► *Yleiskielessä suurin osa bitcoin-käyttäjistä viittaa Mnemonic-lauseeseen puhuessaan "seed:stä", eikä välitilaan, joka on Mnemonic-lauseen ja pääavaimen välissä.*