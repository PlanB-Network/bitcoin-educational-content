---
term: (TRANSAKTIO)

---
Coinbase-tapahtuma on erityinen ja ainutlaatuinen tapahtuma, joka sisältyy Bitcoin-lohkoketjun jokaiseen lohkoon. Se edustaa lohkon ensimmäistä transaktiota, ja sen on luonut louhija, joka on onnistuneesti löytänyt työstötodistuksen (*Proof-of-Work*) vahvistavan otsikon, joka on pienempi tai yhtä suuri kuin tavoite.

Coinbase-transaktiolla on pääasiassa kaksi tarkoitusta: lohkopalkkion myöntäminen louhijalle ja uusien bitcoin-yksiköiden lisääminen kiertävään rahavarantoon. Lohkopalkkio, joka on taloudellinen kannustin louhijoille harjoittaa proof of work -toimintaa, sisältää lohkoon sisältyvistä transaktioista kertyneet palkkiot ja määritetyn määrän uusia luotuja bitcoineja ex-nihilo (lohkotuki). Tämä määrä, joka oli alun perin 50 bitcoinia lohkoa kohti vuonna 2009, puolitetaan 210 000 lohkon välein (noin neljän vuoden välein) tapahtuman nimeltä "puolitus" aikana

Coinbase-transaktio eroaa tavallisista transaktioista monin tavoin. Ensinnäkin sillä ei ole panosta, mikä tarkoittaa, että se ei kuluta mitään olemassa olevaa transaktiotulosta (UTXO). Seuraavaksi coinbase-transaktion allekirjoituskomentosarja (`scriptSig`) sisältää yleensä mielivaltaisen kentän, johon voidaan sisällyttää lisätietoja, kuten mukautettuja viestejä tai kaivosohjelmiston versiotietoja. Lopuksi coinbase-tapahtuman tuottamille bitcoineille asetetaan 100 lohkon (101 vahvistusta) pituinen maturiteettijakso, ennen kuin ne voidaan käyttää, jotta estetään mahdollisten olemattomien bitcoinien käyttäminen ketjun uudelleenjärjestelyn yhteydessä.

> ► *Kielelle "Coinbase" ei ole olemassa ranskankielistä käännöstä. Siksi on hyväksyttävää käyttää tätä termiä suoraan.*