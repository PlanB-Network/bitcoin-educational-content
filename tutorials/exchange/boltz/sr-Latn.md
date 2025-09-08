---
name: Boltz
description: Prebacivanje između različitih Bitcoin slojeva uz održavanje kontrole.
---


![cover](assets/cover.webp)



Od svog uvođenja 2009. godine, Bitcoin-ov peer-to-peer elektronski novčani sistem eksponencijalno je rastao, dajući život rešenjima koja danas omogućavaju da bude sistem koji možemo koristiti trenutno u našim svakodnevnim aktivnostima, posebno kroz Lightning Network.



Međutim, veliki problem je ostao između slojeva Bitcoin protokola: fluidna interoperabilnost. Da bi se iskoristio puni potencijal Bitcoin, bilo je neophodno pronaći rešenje koje bi omogućilo transakcije između različitih slojeva protokola. Ova potreba je dovela do nastanka Boltz-a 2019. godine, mosta koji povezuje nekoliko slojeva Bitcoin.



## Šta je Boltz?



[Boltz](https://boltz.Exchange) je ne-kustodijalna platforma idealna za svakoga ko želi da transakcioniše između različitih slojeva Bitcoin protokola:




- on chain**: Glavni lanac Bitcoin gde se transakcije potvrđuju u proseku svakih 10 minuta, naknade za transakcije su često visoke, što ne mora nužno zadovoljiti potrebe korisnika ;
- Lightning Network**: Bitcoin prekrivanje za trenutna plaćanja uz niske naknade, omogućavajući korišćenje Bitcoin za dnevna plaćanja;
- Liquid Network**: preklop za Bitcoin koji je kreirao Blockstream, omogućavajući brzo, Confidential Transactions i korišćenje drugih finansijskih instrumenata zasnovanih na Bitcoin;
- RootStock**: Rešenje za razvoj pametnih ugovora zasnovanih na Bitcoin protokolu.



![layers](assets/fr/01.webp)



Interoperabilnost između ovih različitih slojeva je od velike važnosti, jer korisnicima pruža fleksibilnost koja im je potrebna da u potpunosti iskoriste sve što ekosistem Bitcoin nudi.



Boltz koristi atomic swaps. Ova tehnologija omogućava razmenu bitcoina između 2 sloja (npr. BTC onchain u Exchange za BTC na Lightningu) direktno između dve strane, bez potrebe za poverenjem i bez potrebe za posrednikom. Ove razmene se nazivaju "atomske" jer mogu proizvesti samo dva rezultata:




- Ili je Exchange uspešan i dva učesnika su efikasno razmenila svoj BTC ;
- Ili Exchange ne uspe, i oba učesnika odlaze sa svojim originalnim BTC.



Na ovaj način, zadržavate trajno samostalno staranje nad svojim bitcoinima, a Exchange nije zasnovan na poverenju u drugu stranu: ili Exchange uspeva ili ne uspeva, ali nijedna strana ne može ukrasti sredstva druge strane.



An atomic Exchange radi sa pametnim ugovorima [HTLC](https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). U ovoj vrsti Contract, iznos je "zaključan" u dvosmernom kanalu i uvodi se vremensko ograničenje, tako da ako transakcija nije završena u određenom vremenu, saldo se vraća deponentu. Ovo je mehanizam koji koristi Boltz platforma.



## Vaši prvi razgovori sa Boltz



Boltz je nedepozitna veb platforma koja ne zahteva nikakve lične informacije od vas. Boltz ima minimalistički, fluidni Interface koji vam omogućava da počnete sa trgovanjem za manje od jednog minuta.



![boltz](assets/fr/02.webp)



Jednom na platformi, možete kreirati atomske razmene između različitih slojeva ekosistema Bitcoin.



![home](assets/fr/03.webp)



Videćete minimalni i maksimalni broj satoshija (najmanja jedinica Bitcoin) koje možete trgovati putem Boltz-a, uključujući mrežne troškove i procenat koji Boltz naplaćuje između 0.1% i 0.5%.



![fees](assets/fr/04.webp)



Zatim izaberite Layer sa kojeg želite da napravite atomski Exchange, i izaberite Layer na koji želite da primite bitkoine.



![couches](assets/fr/05.webp)



U ovom vodiču, fokusiraćemo se na atomski Exchange od glavnog Layer do Lightning Network.



Možete konfigurisati osnovnu jedinicu za vaše razmene birajući između opcija:




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



Jednom kada završite osnovne konfiguracije, unesite iznos vašeg atomskog Exchange, zatim kreirajte Lightning Invoice za ekvivalentan iznos, ili jednostavno unesite vaš LNURL.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



Da biste bili sigurni, proverite parametre vašeg atomskog Exchange da biste izvezli rezervne ključeve povezane sa vašim Exchange.



Na ikoni **Settings**, preuzmite rezervni ključ i sačuvajte datoteku na odgovarajući način.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



Ova datoteka sadrži 12 ključnih reči portfolija povezanih sa vašim atomskim razmenama.



Zatim kliknite na dugme **Create atomic Exchange** i nastavite sa plaćanjem naznačenog iznosa.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Jednom kada vaša uplata bude izvršena i potvrđena, automatski ćete primiti ekvivalentan iznos na vaš Lightning Wallet.



U meniju **Refund** pronađite svoju atomsku Exchange istoriju da biste identifikovali Exchange za koji želite povrat novca. Takođe možete uvesti istoriju razmena koje ste napravili na drugom uređaju, na primer, koristeći rezervni ključni fajl povezan sa tim razmenama.



![refund](assets/fr/11.webp)



U meniju **History** možete preuzeti detaljniju istoriju razmena povezanih sa vašim ključem za spasavanje klikom na dugme **Backup**.



![backup](assets/fr/12.webp)



⚠️ Molimo vas da ne otkrivate ovu datoteku, jer sadrži sve informacije povezane sa vašim transakcijama i rezervni ključ povezan sa tim transakcijama.



Boltz vam nudi visok nivo poverljivosti zahvaljujući pristupu putem `.onion` linka na Tor mreži. Učinite atomske razmene potpuno anonimnim odabirom menija **Onion**, nakon aktiviranja Tor pretraživanja u vašem pregledaču.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Do sada ste upoznati sa Boltzom, jedinstvenom Exchange platformom koja omogućava interoperabilnost između različitih slojeva Bitcoin ekosistema.