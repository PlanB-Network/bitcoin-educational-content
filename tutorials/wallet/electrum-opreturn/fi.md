---
name: Electrum OP_RETURN
description: Rekisteröi viesti osoitteessa Blockchain Bitcoin with Electrum
---

![cover](assets/cover.webp)




Tämä vaiheittainen opetusohjelma näyttää, miten kirjoitat viestin Blockchain Bitcoin:een Wallet Electrum -laitteella. Tässä toiminnossa käytetään OP_RETURN-ohjetta tekstin lisäämiseksi tapahtumaan, joka on julkisesti näkyvissä Blockchain:ssa. Seuraa näitä yksinkertaisia vaiheita rekisteröinnin onnistumiseksi.



---
## Edellytykset





- Tietokone (Windows, macOS tai Linux).
- Internet-yhteys.
- Muutama satoshi (Sats) tai bitcoin (BTC) Wallet:ssäsi transaktion summan ja maksujen kattamiseksi.
- Teksti-heksamuunnin (esim. online-sivusto) tai erityinen työkalu, kuten [tämä OP_RETURN-skriptigeneraattori](https://resources.davidcoen.it/opreturnelectrum/).



---

## Vaihe 1: Lataa ja asenna Electrum



![image](assets/fr/01.webp)



1. Vieraile Electrumin virallisilla verkkosivuilla: [electrum.org](https://electrum.org/).


2. Lataa käyttöjärjestelmääsi (Windows, macOS, Linux) vastaava versio.


3. Asenna Electrum asennusohjelman ohjeiden mukaisesti.


4. Tarkista ladatun tiedoston eheys (valinnainen, mutta turvallisuussyistä suositeltavaa) vertaamalla tiedoston allekirjoitusta tai Hash:tä.



→ Lisätietoja Electrumin opetusohjelmasta :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Vaihe 2: Luo tai tuo Wallet



1. Käynnistä Electrum.


2. Valitse Luo uusi Wallet tai Palauta olemassa oleva Wallet, jos sinulla on jo seed-lause (palautuslause).


3. Seuraa ohjeita Wallet:n konfiguroimiseksi:




 - Jos kyseessä on uusi Wallet, merkitse muistiin seed-lauseesi ja säilytä sitä turvallisessa paikassa (paperilla, kassakaapissa jne.).
 - Jos käytössä on Wallet, palauta se kirjoittamalla seed-lauseesi.


4. Aseta salasana Wallet:n suojaamiseksi.



→ Lisätietoja Electrumin opetusohjelmasta :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Vaihe 3: Tarkista käytettävissä olevat varat



Varmista, että Wallet:ssäsi on tarpeeksi bitcoineja (BTC) tai satosheja (Sats), jotta :




- Transaktion määrä (esimerkiksi 0,00001 BTC tai 1000 Sats).
- Transaktiomaksut, jotka vaihtelevat verkon koon mukaan (yleensä muutama tuhat Sats).



Tarkista varasi Electrumin saldosta.



![image](assets/fr/02.webp)



Siirrä tarvittaessa BTC:tä tai Sats:tä Wallet:n ruokkimiseksi. Tee tämä siirtämällä 'Receive' -välilehdelle ja klikkaamalla 'Create Request' :



![image](assets/fr/03.webp)



Tämä näyttää vastaanoton Address:



![image](assets/fr/04.webp)



→ Lisätietoja Electrumin opetusohjelmasta :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Vaihe 4: Valmistele kirjoitettava viesti



Valitse haluamasi viesti (esim. "Kiitos Satoshi"). Huomautus: OP_RETURN-viestien koko on rajoitettu 80 tavuun eli noin 80 ASCII-merkkiin.



*Mieti hetki: se, mitä kirjoitat Blockchain Bitcoin:een, on ikuista ja kaikkien saatavilla, joten :*




- jättävät kauniin osoituksen ihmisyydestämme,
- vältä sisällön syöttämistä, jota saatat katua



*Blockchain-tila ja bitcoinit ovat arvokkaita, käytä niitä viisaasti ja tarkoituksella*



Muunna viestisi heksadesimaaliksi :




- Voit käyttää [online-työkalua] (https://www.rapidtables.com/convert/number/ascii-to-hex.html), mutta varo käsittelemästä arkaluonteisia tietoja siellä (vaikka periaatteessa Blockchain Bitcoin:ssä OP_RETURN:n kautta julkaistavaksi tarkoitetut tiedot eivät aiheuta luottamuksellisuusongelmia);
- Suuremman luottamuksellisuuden vuoksi voit suorittaa muunnoksen paikallisesti pienellä Python :



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



Esimerkki: `Kiitos Satoshi` ASCII-kielellä antaa heksadesimaalina `5468616e6b73205361746f736869`.



Valmistele tapahtumakäsikirjoitus. Tässä on esimerkki odotetusta muodosta:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



joka koostuu :





- **Kohde Address**: Address. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Tämä voi olla oma Address, jos haluat palauttaa siirretyt varat itsellesi;
- **Siirretty summa**: transaktion summa, tässä `0.00001` BTC. **Huomaa**: Koska Electrumissa käytetty yksikkö on BTC, transaktiokomentosarjassa ilmoitettu summa on myös ilmaistava BTC:nä eikä Sats:na;
- Käsikirjoitus **OP_RETURN**: OP_RETURN <viesti>), 0`. Tässä `5468616e6b73205361746f736869` tarkoittaa viestiä heksadesimaalisena.



⚠️ **Varoitus**: On erittäin tärkeää ilmoittaa "0" OP_RETURN:n jälkeen, koska tämä op-koodi merkitsee skriptin virheelliseksi, jolloin tulosteet eivät ole pysyvästi käytettävissä. Verkkosolmut poistavat tämän tulosteen UTXO-joukostaan. Jos annat muun arvon kuin `0`, se menetetään peruuttamattomasti: bitcoinisi katsotaan palaneiksi. Siksi sinun tulisi aina syöttää `0` OP_RETURN:llä, jotta voit tallentaa halutun tiedon, mutta liittämättä siihen varoja, jotka menetettäisiin.



Vihje: Käytä [OP_RETURN Generator]-työkalua (https://resources.davidcoen.it/opreturnelectrum/) generate-käsikirjoituksen automaattiseen luomiseen. Vaikka tämä työkalu ehdottaa summan syöttämistä BTC:nä, pidä yksikkönä Electrum.



![image](assets/fr/05.webp)



Jos haluat vaihtaa Electrumin käyttämää yksikköä, valitse valikkopalkista "Asetukset" ja valitse sitten "Yksiköt"-välilehdeltä BTC / mBTC / bitit tai Sats :



![image](assets/fr/06.webp)




---

## Vaihe 5: Lähetä tapahtuma



Siirry Electrumissa Lähetä-välilehdelle.



![image](assets/fr/07.webp)



Liitä valmis käsikirjoitus (esimerkiksi yllä oleva) "Pay to" -kenttään.



![image](assets/fr/08.webp)



"Pay to" -kentän pitäisi näkyä muodossa Green, ja tapahtuman summan pitäisi näkyä alla olevalla rivillä.



Tarkista summa ja sen yksikkö Amount-kentästä.



Napsauta "Maksa..." ja säädä transaktiomaksut sen summan mukaan, jonka olet valmis maksamaan, ja sen nopeuden mukaan, jolla haluat, että Miner käsittelee transaktiosi ja integroi sen lohkoon.



![image](assets/fr/09.webp)



Napsauta OK ja vahvista tapahtuma salasanallasi. Vahvistusikkuna tulee näkyviin.




---

## Vaihe 6: Tarkista rekisteröinti



Kun maksutapahtuma on vahvistettu (tämä voi kestää muutaman minuutin), siirry "Historia"-välilehdelle.



![image](assets/fr/10.webp)



Napsauta tapahtumaa hiiren kakkospainikkeella ja valitse "View on Explorer" nähdäksesi tiedot.



Vaihtoehtoisesti voit kopioida kohteen Address (esimerkiksi `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) ja tarkastella sitä Blockchain-selaimella, kuten [Mempool.space](https://Mempool.space/) tai [blockstream.info](https://blockstream.info/).



Etsi OP_RETURN-kenttä tapahtuman tiedoista nähdäksesi viestisi.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Vinkkejä ja parhaita käytäntöjä





- Testaa pienellä määrällä: Aloita pienellä tapahtumalla (esim. Sats 1000), jotta vältät kalliit virheet.
- Varmista, että OP_RETURN:n sisältävä lähtöarvo on nolla, muuten bitcoinisi menetetään pysyvästi.
- Tarkista laite: Varmista, että syötetty summa vastaa Electrumissa näkyvää yksikköä (BTC, mBTC tai Sats).
- Transaktiomaksu: Jos verkko on ruuhkautunut, korota maksua nopeamman vahvistuksen saamiseksi.
- Lyhyt viesti: OP_RETURN-merkinnät on rajoitettu 80 tavuun. Suunnittele viestisi sen mukaisesti.



---

## Hyödyllisiä resursseja





- Lataa Electrum: [electrum.org](https://electrum.org/)
- OP_RETURN-skriptigeneraattori: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain Explorers: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)