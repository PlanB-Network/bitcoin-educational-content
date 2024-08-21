---
termi: COINBASE (TRANSACTION)
---

Coinbase-transaktio on erityinen ja ainutlaatuinen transaktio, joka sisältyy jokaiseen Bitcoin-lohkoketjun lohkoon. Se edustaa lohkon ensimmäistä transaktiota ja sen luo louhija, joka on onnistuneesti löytänyt otsikon, joka validoi työtodistuksen (*Proof-of-Work*), eli on yhtä suuri tai pienempi kuin kohde.

Coinbase-transaktiolla on pääasiassa kaksi tarkoitusta: palkita louhijaa lohkopalkkiolla ja lisätä uusia bitcoin-yksiköitä kiertävään rahamäärään. Lohkopalkkio, joka on taloudellinen kannustin louhijoille osallistua työtodistukseen, sisältää kertyneet maksut lohkoon sisältyvistä transaktioista ja määrätyn määrän ex-nihilo luotuja uusia bitcoineja (lohkotuki). Tämä määrä, joka alun perin asetettiin 50 bitcoiniin lohkoa kohden vuonna 2009, puolittuu joka 210 000 lohkon jälkeen (noin joka 4. vuosi) tapahtumassa, jota kutsutaan "puolittumiseksi".

Coinbase-transaktio eroaa tavallisista transaktioista usealla tavalla. Ensinnäkin sillä ei ole syötettä, mikä tarkoittaa, että sitä ei kuluta mikään olemassa oleva transaktion ulostulo (UTXO). Seuraavaksi coinbase-transaktion allekirjoitusskripti (`scriptSig`) sisältää tyypillisesti mielivaltaisen kentän, joka mahdollistaa lisätietojen, kuten mukautettujen viestien tai louhintasovelluksen version tiedot, sisällyttämisen. Lopuksi coinbase-transaktiolla luodut bitcoinit ovat kypsymisajan alaisia 100 lohkon ajan (101 vahvistusta) ennen kuin niitä voidaan käyttää, jotta estetään mahdollisten olemattomien bitcoinien käyttö ketjun uudelleenjärjestelyssä.

> ► *Ranskaksi termille "Coinbase" ei ole käännöstä. Siksi on hyväksyttävää käyttää tätä termiä suoraan.*