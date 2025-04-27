---
name: Tor Pregledač
description: Kako koristiti Tor Browser?
---
![cover](assets/cover.webp)


Kao što ime sugeriše, pregledač je softver koji se koristi za navigaciju Internetom. On služi kao prolaz između korisničkog računara i veba, prevodeći kod veb-sajtova u interaktivne i čitljive stranice. Izbor vašeg pregledača je veoma važan, jer ne utiče samo na vaše iskustvo pretraživanja, već i na vašu onlajn sigurnost i privatnost.


Pazite da ne pomešate pregledač sa pretraživačem. Pregledač je softver koji koristite za pristup internetu (kao što su Chrome ili Firefox), dok je pretraživač usluga, kao što su Google ili Bing, na primer, koja vam pomaže da pronađete informacije na mreži.


Danas je Google Chrome daleko najkorišćeniji pregledač. On čini oko 65% globalnog tržišta u 2024. godini. Chrome je cenjen zbog svoje brzine i performansi, ali nije nužno najbolji izbor za svakoga, posebno ako vam je privatnost prioritet. Chrome pripada Google-u, kompaniji poznatoj po prikupljanju i analizi ogromnih količina podataka o svojim korisnicima. I zaista, njihov interni pregledač je u srcu njihove strategije nadzora. Ovaj softver je centralna komponenta u većini vaših online interakcija. Ovladavanje prikupljanjem podataka na vašem pregledaču je važno pitanje za Google.

![TOR BROWSER](assets/notext/01.webp)

*Izvor: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*


Postoji nekoliko glavnih porodica pregledača, od kojih je svaka zasnovana na specifičnom render engine-u. Pregledači kao što su Google Chrome, Microsoft Edge, Brave, Opera ili Vivaldi su svi zasnovani na Chromium pregledaču, laganoj i open-source verziji Chrome-a koju je razvio Google. Svi ovi pregledači koriste Blink render engine, koji je Fork WebKit-a, koji je sam izveden iz KHTML-a. Dominacija Chromium-a na tržištu čini pregledače izvedene iz njega posebno efikasnim, jer web developeri imaju tendenciju da optimizuju svoje sajtove prvenstveno za Blink.


Safari, Apple-ov pregledač, koristi WebKit, koji takođe potiče iz KHTML-a.


S druge strane, pregledači kao što su Mozilla Firefox, LibreWolf i Tor Browser oslanjaju se na Gecko, drugačiji rendering engine, poreklom iz Netscape pregledača.


Odabir pravog pregledača zavisi od vaših potreba. Ali ako ste barem malo zabrinuti za svoju privatnost, a samim tim i sigurnost, preporučujem da koristite Firefox za opštu upotrebu i Tor Browser za još veću privatnost. U ovom vodiču pokazaću vam kako da lako počnete sa korišćenjem Tor Browser-a.

![TOR BROWSER](assets/notext/02.webp)


## Uvod u Tor Browser


Tor Browser je pregledač posebno dizajniran za sigurno i što privatnije pretraživanje Interneta. Pregledač je zasnovan na Firefox-u, a samim tim i na Gecko rendering engine-u.

Tor Browser koristi Tor mrežu za šifrovanje i usmeravanje vašeg saobraćaja kroz više relej servera pre nego što ga prenese do odredišta. Ovaj proces višeslojnog usmeravanja, poznat kao "*onion routing*", pomaže u skrivanju vaše prave IP Address, što otežava identifikaciju vaše lokacije i online aktivnosti. Međutim, pretraživanje je nužno sporije nego sa standardnim pregledačem koji ne koristi Tor mrežu, jer je indirektno.

Za razliku od drugih pregledača, Tor Browser integriše specifične funkcije za sprečavanje praćenja vaših online aktivnosti, kao što su izolovanje svake posećene veb stranice i automatsko brisanje kolačića i istorije prilikom zatvaranja. Takođe je dizajniran da minimizira rizike od otiska prsta, čineći da svi korisnici izgledaju što sličnije posećenim sajtovima.


Možete sasvim dobro koristiti Tor Browser za pristup standardnom vebsajtu (`.com`, `.org`, itd.). U ovom slučaju, vaš saobraćaj je anonimizovan prolaskom kroz nekoliko Tor čvorova pre nego što stigne do izlaznog čvora koji komunicira sa krajnjim sajtom na clearnet-u.

![TOR BROWSER](assets/notext/03.webp)

Takođe možete koristiti Tor Browser za pristup skrivenim servisima (adrese koje se završavaju sa `.onion`). U ovom scenariju, sav saobraćaj ostaje unutar Tor mreže, bez izlaznog čvora, što osigurava potpunu privatnost kako za korisnika, tako i za odredišni server. Ovaj način rada se naročito koristi za pristup onome što se ponekad naziva "*dark web*," delu Interneta koji nije indeksiran od strane tradicionalnih pretraživača.

![TOR BROWSER](assets/notext/04.webp)


## Koja je razlika između Tor mreže i Tor pretraživača?


Tor mreža i Tor pregledač su dve različite stvari koje ne treba mešati, ali su komplementarne. Tor mreža je globalna infrastruktura relej servera, kojima upravljaju korisnici, i koja anonimizuje internet saobraćaj tako što ga prosleđuje kroz nekoliko čvorova pre nego što ga usmeri ka konačnom odredištu. Ovo je čuveno onion rutiranje.


Tor pregledač, s druge strane, je specifičan pregledač dizajniran da olakša pristup ovoj mreži na jednostavan način. On integriše po podrazumevanim podešavanjima sve neophodne postavke za povezivanje na Tor mrežu i koristi modifikovanu verziju Firefox-a kako bi pružio poznato iskustvo pregledanja dok maksimizira privatnost i sigurnost.


Tor mreža se ne koristi samo putem Tor pregledača. Može se koristiti od strane različitog softvera i aplikacija za osiguranje njihove komunikacije. Na primer, moguće je omogućiti komunikaciju putem Tor mreže na vašem Bitcoin čvoru kako biste sakrili vaš IP Address od drugih korisnika i sprečili nadzor nad saobraćajem povezanim sa vašim Bitcoin od strane vašeg internet provajdera.

Ukratko, Tor mreža je infrastruktura koja obezbeđuje privatnost u našem pretraživanju interneta, a Tor pretraživač je softver koji nam omogućava da koristimo ovu mrežu kao deo našeg pretraživanja interneta.


## Kako instalirati Tor Browser?


Tor Browser je dostupan za Windows, Linux i macOS za računare, kao i za Android na pametnim telefonima. Da biste instalirali Tor Browser na vašem računaru, posetite [zvaničnu veb stranicu Tor Project-a](https://www.torproject.org/).

![TOR BROWSER](assets/notext/05.webp)

Kliknite na dugme "*Download Tor Browser*".

![TOR BROWSER](assets/notext/06.webp)

Izaberite verziju koja odgovara vašem operativnom sistemu.

![TOR BROWSER](assets/notext/07.webp)

Kliknite na izvršnu datoteku da biste započeli instalaciju, a zatim izaberite svoj jezik.

![TOR BROWSER](assets/notext/08.webp)

Izaberite fasciklu u koju će softver biti instaliran, zatim kliknite na dugme "*Install*".

![TOR BROWSER](assets/notext/09.webp)

Sačekajte da se instalacija završi.

![TOR BROWSER](assets/notext/10.webp)

Na kraju, kliknite na dugme "*Finish*".

![TOR BROWSER](assets/notext/11.webp)


## Kako koristiti Tor Browser?


Tor Browser se koristi kao standardni pregledač.

![TOR BROWSER](assets/notext/12.webp)

Prilikom prvog pokretanja, pregledač vam prikazuje stranicu koja vas poziva da se povežete na Tor mrežu. Jednostavno kliknite na dugme "*Connect*" da uspostavite vezu.

![TOR BROWSER](assets/notext/13.webp)

Ako želite da softver automatski povezuje na Tor mrežu tokom vaših budućih korišćenja, označite opciju "*Uvek se automatski poveži*".

![TOR BROWSER](assets/notext/14.webp)

Jednom kada se povežete na Tor mrežu, stići ćete na početnu stranicu.

![TOR BROWSER](assets/notext/15.webp)

Da biste izvršili pretragu na Internetu, jednostavno unesite svoj upit u traku za pretragu i pritisnite taster "*enter*".

![TOR BROWSER](assets/notext/16.webp)

Zatim ćete dobiti rezultate iz svog pretraživača na isti način kao i sa drugim pregledačima.

![TOR BROWSER](assets/notext/17.webp)

Opcija "*Onionize*" na DuckDuckGo omogućava vam da koristite pretraživač putem njegove skrivene usluge na Tor mreži, pristupom njegovom `.onion` Address.

![TOR BROWSER](assets/notext/18.webp)


## Kako konfigurisati Tor Browser?


Na vrhu ekrana vašeg pregledača, pronaći ćete opciju za uvoz vaših favorita. Ovo vam omogućava da automatski integrišete obeleživače iz vašeg starog pregledača u Tor Pregledač.

![TOR BROWSER](assets/notext/19.webp)

Takođe imate opciju da dodate nove obeleživače klikom na ikonu zvezde koja se nalazi u gornjem desnom uglu veb stranice koju posećujete.

![TOR BROWSER](assets/notext/20.webp)

U meniju sa desne strane, pristupate raznim opcijama.

![TOR BROWSER](assets/notext/21.webp)The "*New identity*" button allows you to change your Tor identity. Specifically, this enables you to start a new user session on Tor, meaning changing your IP address and resetting cookies and open sessions.

![TOR BROWSER](assets/notext/22.webp)

Meni "*Bookmarks*" vam omogućava da upravljate svojim obeleživačima.

![TOR BROWSER](assets/notext/23.webp)

"*Istorija*" vam omogućava pristup istoriji pretraživanja ako ste je omogućili u podešavanjima.

![TOR BROWSER](assets/notext/24.webp)

Meni "*Dodaci i teme*" omogućava vam da prilagodite izgled vašeg pregledača ili dodate ekstenzije. Pošto je Tor Browser zasnovan na Mozilla Firefox-u, možete koristiti teme i ekstenzije dostupne za Firefox.

![TOR BROWSER](assets/notext/25.webp)

Konačno, dugme "*Settings*" vam omogućava pristup podešavanjima vašeg pregledača.

![TOR BROWSER](assets/notext/26.webp)

U kartici "*General*" u podešavanjima, postoje razne opcije koje vam omogućavaju da prilagodite korisnički interfejs Tor Browser-a Interface.

![TOR BROWSER](assets/notext/27.webp)

Na kartici "*Home*", možete odabrati da promenite podrazumevanu stranicu koja se prikazuje prilikom otvaranja Tor Browser-a i prilikom otvaranja novih kartica.

![TOR BROWSER](assets/notext/28.webp)

U kartici "*Search*", možete izabrati pretraživač. Tor Browser podrazumevano koristi DuckDuckGo, pretraživač fokusiran na zaštitu privatnosti korisnika, ali možete se odlučiti i za Google ili Startpage, na primer.

![TOR BROWSER](assets/notext/29.webp)

Takođe možete postaviti prečice u svom pretraživaču.

![TOR BROWSER](assets/notext/30.webp)

Na primer, možete ukucati "*@wikipedia*" praćeno vašim pojmom za pretragu, kao što je "*Bitcoin*", u pretraživač.

![TOR BROWSER](assets/notext/31.webp)

Ova funkcija zatim vrši pretragu vašeg pojma direktno na Wikipedia sajtu.

![TOR BROWSER](assets/notext/32.webp)

Možete tako postaviti druge prilagođene prečice za različite sajtove.


Zatim, u kartici "*Privatnost i sigurnost*", pronaći ćete sve postavke vezane za privatnost i sigurnost.

![TOR BROWSER](assets/notext/33.webp)

Imate opciju da zadržite ili obrišete svoju istoriju pretrage.

![TOR BROWSER](assets/notext/34.webp)

Takođe možete upravljati dozvolama za pristup koje dajete različitim veb-sajtovima.

![TOR BROWSER](assets/notext/35.webp)

Za ukupnu sigurnost vašeg pregledača, režimi "*Bezbednije*" i "*Najbezbednije*" omogućavaju vam da prilagodite funkcionalnosti veba i skripte koje izvršavaju sajtovi koje posećujete. Ovo minimizira rizike od iskorišćavanja ranjivosti, ali će takođe uticati na prikaz i interaktivnost sajtova zauzvrat. ![TOR BROWSER](assets/notext/36.webp) Pronaći ćete druge opcije sigurnosti, uključujući blokator opasnog sadržaja i režim samo za HTTPS, koji osigurava da veze sa sajtovima dosledno poštuju ovaj protokol. ![TOR BROWSER](assets/notext/37.webp) Na kraju, u kartici "*Veza*", pronaći ćete sva podešavanja vezana za povezivanje na Tor mrežu. Ovde možete konfigurisati most za pristup Toru iz regiona gde bi njegov pristup mogao biti cenzurisan. ![TOR BROWSER](assets/notext/38.webp) I eto ga, sada ste spremni da pretražujete Internet na bezbedniji i privatniji način! Ako vas tema online privatnosti zanima, takođe preporučujem da otkrijete ovaj drugi vodič o Mullvad VPN:


https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8