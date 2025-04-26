---
name: Ledger Nano S

description: Kako postaviti svoj Ledger Nano S uređaj
---

![image](assets/cover.webp)


Cold physical Wallet – €60 – Beginner – Da obezbedi €2,000 do €50,000


Ledger je francusko rešenje za jednostavno osiguranje bitkoina.


U ovom vodiču takođe diskutujemo o odeljku sa lozinkama, naprednom sigurnosnom rešenju za čuvanje velikih suma: 20,000€ – 100,000€.


https://www.youtube.com/watch?v=_vsHNTLi8MQ


# Poveži Ledger sa Sparrow Bitcoin Wallet (vodič za pisanje)


Obavezno prvo pročitajte drugi deo „Korišćenje Bitcoin hardverskih novčanika“. Ovde ću preleteti kroz neke korake i fokusiraću se uglavnom na ono što je specifično za Ledger.


## Podešavanje uređaja


Ledger dolazi sa sopstvenim USB kablom. Uverite se da koristite taj kabl, a ne bilo koji stari kabl. Neki USB kablovi služe samo za napajanje. Ovaj prenosi podatke I napajanje. Kada sam koristio uređaj sa USB kablom za punjenje telefona koji je bio pri ruci, uređaj nije uspeo da se poveže.


Povežite ga sa računarom i uređaj će se uključiti.


![image](assets/1.webp)


Prođite kroz opcije. Videćete


1. Postavite kao novi uređaj

2. Obnovi iz rezervne fraze


U suštini, pita vas da li želite da uređaj kreira seed za vas ili već imate jedan koji biste želeli da koristite. Najbolja praksa je da napravite svoj sopstveni seed, ali to uraditi bezbedno je veoma napredno i van okvira ovog članka. Izaberite „Postavi kao novi uređaj“


Bićete zamoljeni da izaberete PIN. Ovo nije deo vašeg Bitcoin seed i specifično je samo za ovaj uređaj. On zaključava uređaj.


Zatim će vam predstaviti 24 reči koje treba da prelistate i zapišete.


Čudno, kada dođete do kraja, piše „pritisnite levo da proverite svoje reči“. To ne opisuje kako potvrđujete da nastavite, već samo znači da možete da se vratite i ponovo pogledate reči. Umesto toga, pritisnite desno i potvrdite pritiskom na levo i desno istovremeno.


Sledeći deo je super dosadan. Meša 24 reči i morate potvrditi svaku, od 1 do 24, prolazeći kroz sve reči za svaki izbor. Kada završite, omogućava vam da potvrdite pritiskom na dva dugmeta i nastavite.


![image](assets/2.webp)


Videćete na vašoj kontrolnoj tabli da imate dugme za podešavanja i dugme sa znakom plus koje vam omogućava instalaciju aplikacija. Ali prvo morate da se povežete sa Ledger Live. To ćemo uraditi sledeće…


## Preuzmi Ledger Uživo


Možete preuzeti Ledger Live sa njihove veb stranice, ali je bolje da ga preuzmete sa GitHub-a, gde se čuva izvorni kod.


Google „Ledger live GitHub“ ili kliknite ![ovde](link https://github.com/LedgerHQ/Ledger-live-desktop)


![image](assets/3.webp)


Pomerite dole dok ne vidite naslov „Downloads“…


![image](assets/4.webp)


Na dnu ćete videti link: Instructions for verifying the Hash and signatures of the installation packages are available on this page. Click that link.(https://live.Ledger.tools/lld-signatures)


![image](assets/5.webp)


Na vrhu se nalaze opcije linkova za softverski paket koji vam je potreban, u zavisnosti od vašeg operativnog sistema. Kliknite na odgovarajući da biste preuzeli.


Dalje, želimo da verifikujemo Hash preuzimanja, radi dodatne sigurnosti. Ledger objavljuje Hash za svaku od dostupnih datoteka. Sada ćemo Hash preuzimanje i uporediti izlaz. Mora biti identičan kako bismo bili sigurni da datoteka nije izmenjena.


Otvorite terminal na Mac-u ili CMD na Windows-u; upišite unutar njega sledeće komande i pritisnite enter:


```bash
cd Downloads
```


```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- For Mac
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- For Windows
```


Nadam se da je očigledno da komande počinju posle strelica. Uverite se, ako je ovaj članak zastareo, da promenite ime datoteke u komandama tačno u ime datoteke koju ste preuzeli. Potrebno je da pritisnete taster <Enter> nakon svake komande. Komande kako su ovde prikazane možda neće stati u jedan red u vašem veb pregledaču. Napomena, sve je otkucano u jednom redu.


Pogledaj izlaz Hash i uveri se da je identičan onom objavljenom na GitHub-u.


Idealno, želite da budete dodatno otmeni i osigurate da objavljeni heševi nisu lažni. To radimo pomoću gpg potpisa, ali to je van okvira ovog članka. Ako želite da naučite o tome (i predlažem da to na kraju uradite), onda pregledajte ovaj članak.


## Poveži se na Ledger Uživo


Pre nego što pokrenete Ledger Live, pomaže malo privatnosti da uključite VPN. Ledger će i dalje dobiti sve vaše adrese, ali neće znati vaš IP Address, koji otkriva vaš dom Address. Mullvad VPN je odlična VPN usluga i nije veoma skupa (ne reklamiram, samo je koristim).


Instalirajte softver na vaš računar i pokrenite ga.


![image](assets/6.webp)


Odaberite svoj uređaj i izaberite „Prvi put koristim…”


![image](assets/7.webp)


Bićete zatim vođeni kroz čarobnjaka, ali mi smo prošli sve ove korake tako da možete proći kroz njih.


![image](assets/8.webp)


Nakon mnogo koraka i kviza, proveriće da li je uređaj originalan. Morate se uveriti da ste povezani i da ste uneli pin, a zatim će vas uređaj pitati da li dozvoljavate Ledger Live da se poveže. Naravno, morate to potvrditi.


![image](assets/9.webp)


U sledećem iskačućem prozoru bilo je reklamiranje shitcoina prerušenog u „beleške o izdanju“. Zatvorite ga, a zatim biste trebali doći do ovog ekrana.


![image](assets/10.webp)


Morate kliknuti „Dodaj nalog“ da biste dobili Bitcoin Wallet.


![image](assets/11.webp)


Obavezno izaberite Bitcoin, a ne Bitcoin Cash ili bilo koji drugi shitcoin. Proveriće uređaj, i morate potvrditi da nastavite NA UREĐAJU. Izračunavaće adrese nekoliko minuta. Zatim kliknite DONE.


![image](assets/12.webp)

![image](assets/13.webp)


Sjajno. Sada imate shitcoin Wallet menadžer koji sadrži Bitcoin Wallet na vašem računaru. Zapravo vam više nije potreban i možete ga se rešiti. Prava svrha je bila da se Bitcoin aplikacija dobije na samom uređaju, i to je bio jedini način, osim primene nekih ekstremnih tehnika softverskog inženjeringa.


Zapamtite da smo ranije na uređaju imali dugme za podešavanja i dugme sa znakom plus. Sada imamo dodatno dugme – dugme za Bitcoin aplikaciju.


Možete isključiti Ledger Live sada.


## Dodaj passphrase


Sada kada imamo Bitcoin App, možemo dodati passphrase našoj seed frazi. To nismo mogli ranije kada je seed prvi put kreiran jer na početku nismo imali Bitcoin App, i trebali smo se povezati na Ledger Live da bismo ga dobili.


Idite na meni „settings“ unutar uređaja, zatim na podmeni „security“. Zatim izaberite passphrase. Videćete „Advanced feature“. Kliknite desno dugme, videćete „read manuel…“ i zatim nakon klika na desno dugme, videćete „back“. Ali to nije kraj. Intuitivno biste to pomislili, ali kliknite desno dugme ponovo. Videćete „set up passphrase“.


Možete odlučiti da „prikačite na PIN“ ili „Postavite privremeno“. Preporučujem da „prikačite na PIN“. Na taj način možete pristupiti različitim novčanicima u zavisnosti od PIN-a koji unesete kada prvi put uključite uređaj. Ako „postavite privremeno“, moraćete da unosite passphrase svaki put kada želite da pristupite tom Wallet, ali uvek sa podrazumevanog PIN-a.


Unesite passphrase i potvrdite ga.


Tražiće od vas “Trenutni PIN”. Ovo nije PIN koji povezujete sa novim passphrase. To je PIN koji ste uneli kada ste uključili uređaj za ovu sesiju.


Sada možete izaći u glavni meni tako što ćete nekoliko puta odabrati opciju nazad.


## Gledanje Wallet


U prethodnim člancima, objasnio sam kako preuzeti i verifikovati Sparrow Wallet, i kako ga povezati sa vašim sopstvenim čvorom, ili javnim čvorom. Trebalo bi da pratite ove vodiče:



- Instaliraj Bitcoin Core ( https://armantheparman.com/bitcoincore/)



- Instaliraj Sparrow Bitcoin Wallet (https://armantheparman.com/download-sparrow/)



- Poveži Sparrow Bitcoin Wallet sa Bitcoin Core (https://armantheparman.com/sparrowcore/)


Alternativa za korišćenje Sparrow Bitcoin Wallet je Electrum Desktop Wallet, ali ću nastaviti da objašnjavam Sparrow Bitcoin Wallet jer smatram da je najbolji za većinu ljudi. Napredni korisnici možda će želeti da koriste Electrum kao alternativu.


Sada ćemo ga učitati i povezati Ledger, pri čemu Wallet sadrži passphrase. Ovaj Wallet nikada nije bio izložen Ledger Live jer je kreiran NAKON što smo povezali uređaj sa Ledger Live. Uverite se da ga nikada više ne povezujete sa Ledger Live kako ne biste izložili vaš novi privatni Wallet.


Kreiraj novi Wallet:


![image](assets/14.webp)


Nazovi to nečim lepim


![image](assets/15.webp)


Obratite pažnju na polje za potvrdu, „Ima postojeću transakciju“. Ako je ovo Wallet koji ste ranije koristili, označite ovo inače će vaš saldo pogrešno prikazivati nulu. Označavanje ovog polja traži od Sparrow-a da pregleda bazu podataka Bitcoin Core-a (Blockchain) za prethodne transakcije. Za ovaj vodič, koristimo potpuno novi Wallet, tako da možete ostaviti polje neoznačeno.


![image](assets/16.webp)


Kliknite na „Connected Hardware Wallet“ i proverite da li je uređaj zaista povezan, uključen, unet PIN i da li ste ušli u aplikaciju Bitcoin.


![image](assets/17.webp)


Kliknite „Skeniraj“ i zatim „Uvezi Keystore“ na sledećem ekranu.


![image](assets/18.webp)


Nema ničega za uređivanje na sledećem ekranu, Ledger ga je popunio za vas. Kliknite „Primeni“


![image](assets/19.webp)


Sledeći ekran vam omogućava da dodate lozinku. Nemojte ovo pomešati sa “passphrase”; mnogi ljudi hoće. Ime je nesrećno odabrano. Lozinka vam omogućava da zaključate ovaj Wallet na vašem računaru. Ona je specifična za ovaj softver na ovom računaru. Nije deo vašeg Bitcoin privatnog ključa.


![image](assets/20.webp)


Nakon pauze, dok računar razmišlja, videćete kako se dugmad sa leve strane menja iz sive u plavu. Čestitamo, vaš Wallet je sada spreman za korišćenje. Pravite i šaljite transakcije koliko god želite.


![image](assets/21.webp)


## Primanje


Da biste primili neki Bitcoin, idite na karticu Adrese sa leve strane i izaberite jednu od adresa za primanje. Samo kliknite desnim tasterom miša na Address koji želite i izaberite „kopiraj Address“. Zatim idite na svoj Exchange odakle se novac šalje i nalepite ga tamo. Ili možete dati Address kupcu koji ga može koristiti da vam plati.


Kada prvi put koristite Wallet, trebalo bi da primite veoma malu količinu, vežbajte trošenje na drugi Address, bilo unutar Wallet ili nazad na Exchange, kako biste dokazali da Wallet funkcioniše kako se očekuje.


Jednom kada to uradite, morate napraviti rezervnu kopiju reči koje ste zapisali. Jedna kopija nije dovoljna. Imajte najmanje dve papirne kopije (metal je bolji), i čuvajte ih na dve različite, dobro osigurane lokacije. Ovo smanjuje rizik da prirodna katastrofa uništi vaš HWW i papirnu rezervnu kopiju u jednom incidentu. Pogledajte “Korišćenje Bitcoin hardverskih novčanika” za potpunu diskusiju o tome.


## Slanje


![image](assets/22.webp)


Kada vršite uplatu, potrebno je da nalepite Address kojem plaćate u polje „Pay to“. Ne možete zapravo ostaviti Polje za oznaku prazno, to je samo za evidenciju vaših novčanika, ali Sparrow to ne dozvoljava – samo unesite nešto (samo vi ćete to videti). Unesite iznos i možete ručno prilagoditi naknadu koju želite.


Wallet ne može potpisati transakciju osim ako HWW nije povezan. To je posao HWW-a – da primi transakciju, potpiše je i vrati nazad, potpisanu. Uverite se da kada potpisujete na uređaju, vizuelno proverite da li je Address kojem plaćate isti na uređaju i na ekranu računara, i Invoice koji primate (npr. možda ste primili email da platite određeni Address).


Takođe obratite pažnju da ako odlučite da koristite novčić koji je veći od iznosa plaćanja, ostatak će biti poslat nazad na jednu od adresa za kusur vaših novčanika. Neki ljudi nisu znali ovo, i proverili su svoju transakciju na javnom Blockchain, i pomislili da je neki Bitcoin poslat na napadačev Address, ali u stvari, to je bio njihov sopstveni kusur Address.


## Firmware


Da biste ažurirali firmware, potrebno je da se povežete sa Ledger Live. Ako želite to da uradite, prvo treba da obrišete uređaj i da se uverite da imate svoje rezervne reči i passphrase dostupne za vraćanje uređaja. Razlog zašto preferiram da prvo obrišem uređaj je taj što morate povezati svoj uređaj sa Ledger Live da biste ažurirali firmware, i ne želim da izložim vaš novi Wallet (onaj sa passphrase) Ledger Live, nikada. Jednostavno ne verujem da Ledger ne izvlači informacije o mom javnom ključu sa uređaja kada se povežem sa Ledger Live. Oni tvrde da ne rade to, ali ne mogu to da proverim sam osim ako ne pročitam kod i razumem unutrašnji hardver takođe.


## Zaključak


Ovaj članak vam je pokazao kako da koristite Ledger HWW na sigurniji i privatniji način nego što je reklamirano – ali ovaj članak sam po sebi nije dovoljan. Kao što sam rekao na početku, trebalo bi da ga kombinujete sa informacijama iz „Korišćenje Bitcoin hardverskih novčanika“.

Saveti:


Static Lightning Address: dandysack84@walletofsatoshi.com

https://armantheparman.com/ledgersparrow/


Da biste dalje istražili ovu temu i ojačali sigurnost vašeg Wallet na Ledger Nano sa BIP39 passphrase, pozivam vas da pogledate ovaj sveobuhvatni vodič:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49