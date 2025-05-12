---
name: Mullvad VPN
description: Postavljanje VPN-a plaćenog bitcoinima
---
![cover](assets/cover.webp)


VPN ("*Virtualna Privatna Mreža*") je usluga koja uspostavlja sigurnu i šifrovanu vezu između vašeg telefona ili računara i udaljenog servera kojim upravlja VPN provajder.


Tehnički, kada se povezujete na VPN, vaš internet saobraćaj se preusmerava kroz šifrovani tunel do VPN servera. Ovaj proces otežava trećim stranama, kao što su Internet provajderi (ISP) ili zlonamerni akteri, da presretnu ili pročitaju vaše podatke. VPN server tada deluje kao posrednik koji se povezuje na uslugu koju želite da koristite u vaše ime. Dodeljuje novu IP Address vašoj vezi, što pomaže da sakrijete vašu pravu IP Address od sajtova koje posećujete. Međutim, suprotno onome što neki online oglasi mogu sugerisati, korišćenje VPN-a ne omogućava vam anonimno pretraživanje interneta, jer zahteva nivo poverenja u VPN provajdera koji može videti sav vaš saobraćaj.

![MULLVAD VPN](assets/fr/01.webp)

Prednosti korišćenja VPN-a su brojne. Prvo, čuva privatnost vaših online aktivnosti od ISP-ova ili vlada, pod uslovom da VPN provajder ne deli vaše informacije. Drugo, obezbeđuje vaše podatke, posebno kada ste povezani na javne Wi-Fi mreže, koje su podložne MITM ("**man-in-the-middle**") napadima. Treće, sakrivanjem vašeg IP Address, VPN vam omogućava da zaobiđete geografska ograničenja i cenzuru, kako biste pristupili sadržaju koji bi inače bio nedostupan ili blokiran u vašem regionu.


Kao što možete videti, VPN prebacuje rizik posmatranja saobraćaja na VPN provajdera. Stoga, prilikom izbora vašeg VPN provajdera, važno je razmotriti lične podatke potrebne za registraciju. Ako provajder traži informacije kao što su vaš broj telefona, email Address, podaci o bankovnoj kartici, ili još gore, vaša poštanska Address, rizik povezivanja vašeg identiteta sa vašim saobraćajem se povećava. U slučaju kompromitovanja provajdera ili pravnog zaplene, bilo bi lako povezati vaš saobraćaj sa vašim ličnim podacima. Stoga se preporučuje da izaberete provajdera koji ne zahteva nikakve lične informacije i prihvata anonimna plaćanja, kao što su bitkoini.


U ovom vodiču predstaviću jednostavno, efikasno i cenovno pristupačno VPN rešenje koje ne zahteva lične informacije za korišćenje.


## Uvod u Mullvad VPN

Mullvad VPN je švedska usluga koja se izdvaja po svojoj Commitment prema privatnosti korisnika. Za razliku od glavnih VPN provajdera, Mullvad ne zahteva lične podatke prilikom prijave. Nema potrebe da navedete email Address, broj telefona ili ime; umesto toga, Mullvad vam dodeljuje anoniman broj naloga koji se koristi za plaćanje i pristup usluzi. Pored toga, Mullvad tvrdi da ne vodi evidenciju aktivnosti koje prolaze kroz njihove servere.

![MULLVAD VPN](assets/notext/02.webp)

Za plaćanje nije nužno potrebno pružiti informacije o kreditnoj kartici, jer Mullvad prihvata Bitcoin uplate (samo onchain na njihovoj zvaničnoj stranici, ali postoji nezvanična metoda za plaćanje putem Lightning-a). Takođe prihvataju gotovinske uplate putem pošte.


Mullvad VPN se takođe ističe svojom transparentnošću i sigurnošću. Njihov softver je otvorenog koda, a redovno prolaze nezavisne sigurnosne revizije kako bi procenili svoje aplikacije i infrastrukturu, čiji su rezultati [objavljeni na njihovom sajtu](https://mullvad.net/fr/blog/tag/audits). Kompanija iza Mullvada je smeštena u Švedskoj, zemlji poznatoj po strogim zakonima o privatnosti. Oni isključivo koriste servere koje sami hostuju, čime eliminišu rizike povezane sa korišćenjem usluga trećih strana u oblaku, kao što su hiperskeleri AWS, Google Cloud ili Microsoft Azure.


Što se tiče funkcija, Mullvad nudi sve što se očekuje od dobrog VPN klijenta, uključujući prekidač koji štiti vaš saobraćaj ako se VPN prekine, opciju da onemogućite VPN za određene aplikacije i mogućnost usmeravanja vašeg saobraćaja kroz više VPN servera.


Prirodno, ovaj kvalitet usluge dolazi uz cenu, ali fer cena je često pokazatelj kvaliteta i poštenja. Može signalizirati da kompanija ima poslovni model bez potrebe da prodaje vaše lične podatke trećim stranama. Mullvad VPN nudi fiksnu cenu od 5 evra mesečno, koja se može koristiti na do 5 različitih uređaja.

![MULLVAD VPN](assets/notext/03.webp)

Za razliku od glavnih VPN provajdera, Mullvad ima model kupovine vremena pristupa usluzi umesto ponavljajuće, automatske pretplate. Jednostavno izvršite jednokratnu uplatu u bitkoinima za odabrano trajanje. Na primer, ako kupite godinu dana pristupa, možete koristiti uslugu tokom tog perioda, nakon čega morate ponovo posetiti Mullvadov sajt da obnovite vreme pristupa.

U poređenju sa IVPN, još jednim visokokvalitetnim VPN provajderom, Mullvad je nešto ekonomičniji. Na primer, čak i kada se odlučite za trogodišnju kupovinu sa IVPN, mesečni trošak iznosi oko €5.40. Međutim, IVPN nudi neke dodatne usluge i takođe ima jeftiniji plan od Mullvad-ovog (Standard plan), ali je ovo ograničeno na samo 2 uređaja i isključuje "multi-hop" protokol.

Takođe sam sproveo neke neformalne testove brzine kako bih uporedio IVPN i Mullvad. Iako je IVPN pokazao blagu superiornost u pogledu performansi, brzine kod Mullvada su i dalje bile veoma zadovoljavajuće. U poređenju sa glavnim VPN provajderima, IVPN i Mullvad su se pokazali kao najmanje jednako efikasni, ako ne i superiorniji u nekim slučajevima.


## Kako instalirati Mullvad VPN na računar?


Posetite [zvaničnu Mullvad veb stranicu](https://mullvad.net/en/download/) i kliknite na meni "*Downloads*".

![MULLVAD VPN](assets/notext/04.webp)

Za korisnike Windows-a ili macOS-a, preuzmite softver direktno sa sajta i pratite uputstva koja pruža čarobnjak za instalaciju kako biste završili instalaciju.

![MULLVAD VPN](assets/notext/05.webp)

Za korisnike Linux-a, uputstva specifična za vašu distribuciju možete pronaći u odeljku ["*Linux*"](https://mullvad.net/en/download/vpn/linux).

![MULLVAD VPN](assets/notext/06.webp)

Kada je instalacija završena, potrebno je uneti ID vašeg naloga. Videćemo kako da ga dobijete u narednim delovima ovog vodiča.


## Kako instalirati Mullvad VPN na pametni telefon?


Preuzmite Mullvad VPN iz svoje prodavnice aplikacija, bilo da je to [AppStore](https://apps.apple.com/us/app/mullvad-vpn/id1488466513) za iOS korisnike, [Google Play Store](https://play.google.com/store/apps/details?id=net.mullvad.mullvadvpn) za Android, ili [F-Droid](https://f-droid.org/packages/net.mullvad.mullvadvpn/). Ako koristite Android, takođe imate opciju da preuzmete `.apk` datoteku direktno sa [Mullvad sajta](https://mullvad.net/en/download/vpn/android).

![MULLVAD VPN](assets/notext/07.webp)

Prilikom prve upotrebe aplikacije, bićete odjavljeni. Moraćete da unesete svoj ID naloga da biste aktivirali uslugu.

![MULLVAD VPN](assets/notext/08.webp)

Sada, pređimo na aktiviranje Mullvad-a na vašim uređajima.


## Kako platiti i aktivirati Mullvad VPN?


Idite na [zvaničnu Mullvad veb stranicu](https://mullvad.net/) i kliknite na dugme "*Get Started*".

![MULLVAD VPN](assets/notext/09.webp)

Kliknite na dugme "*generate account number*".

![MULLVAD VPN](assets/notext/10.webp)Mullvad will then create your account. You do not need to provide any personal information. It is only your account number that will allow you to log in. It acts somewhat like an access key. Save it in a safe place like your password manager, for example. You can also make a paper copy.

![MULLVAD VPN](assets/notext/11.webp)

Zatim kliknite na dugme "*Dodaj vreme na svoj nalog*".

![MULLVAD VPN](assets/notext/12.webp)

Zatim ćete stići na stranicu za prijavu na vaš nalog. Unesite broj vašeg naloga i zatim kliknite na dugme "*Log in*".

![MULLVAD VPN](assets/notext/13.webp)

Izaberite svoj način plaćanja. Preporučujem plaćanje u bitkoinima, jer ćete imati koristi od popusta od 10%, što smanjuje cenu na €4.50 mesečno. Ako više volite da platite putem Lightning-a, obezbediću alternativni metod u sledećem delu.

![MULLVAD VPN](assets/notext/14.webp)

Kliknite na dugme "*Create a one-time payment Address*".

![MULLVAD VPN](assets/notext/15.webp)

Zatim platite sa svojim Bitcoin Wallet iznos naveden primljenom Address koji vam je dat.

![MULLVAD VPN](assets/notext/16.webp)

Može potrajati nekoliko minuta pre nego što sajt detektuje vašu uplatu, nakon što je transakcija potvrđena. Kada Mullvad detektuje uplatu, trajanje vaše pretplate će se pojaviti u gornjem levom uglu stranice, umesto oznake "*Nema preostalog vremena*".

![MULLVAD VPN](assets/notext/17.webp)

Zatim možete uneti broj svog naloga u softver da aktivirate VPN.

![MULLVAD VPN](assets/notext/18.webp)

Da biste aktivirali VPN na svojoj mobilnoj aplikaciji, proces je potpuno isti. Samo trebate uneti broj svog naloga.

![MULLVAD VPN](assets/notext/19.webp)

## Kako platiti Mullvad VPN pomoću Lightning-a?


Kao što ste razumeli, Mullvad još uvek ne prihvata uplate putem Lightning Network. Međutim, zahvaljujući preporuci od [Lounès](https://x.com/louneskmt), otkrio sam neformalnu uslugu koja vam omogućava da zaobiđete ovo ograničenje. Ova usluga, dostupna na [vpn.sovereign.engineering](https://vpn.sovereign.engineering/), prihvata vaše uplate putem Lightning-a i zauzvrat vam pruža važeći plan za Mullvad.

![MULLVAD VPN](assets/notext/20.webp)

Imate 2 različite opcije na ovom sajtu: možete verovati menadžeru sajta i direktno uneti broj svog naloga, zatim kliknuti na "*Log in*" kako bi vaš Mullvad paket bio automatski validiran. Ili, možete kliknuti na dugme "*Heck yeah!*" da kupite Voucher u Lightning-u, koji zatim možete koristiti na zvaničnom Mullvad sajtu da dobijete svoj paket. ![MULLVAD VPN](assets/notext/21.webp) U oba slučaja, bićete upitani da izaberete trajanje vašeg paketa. Možete birati između 6 meseci i 1 godine. ![MULLVAD VPN](assets/notext/22.webp) Zatim kliknite na dugme "*Top-up with Lightning*". ![MULLVAD VPN](assets/notext/23.webp) Da biste finalizirali kupovinu, platite Invoice sa vašim Lightning Wallet. ![MULLVAD VPN](assets/notext/24.webp) Ako ste se odlučili za kupovinu Vouchera, na Mullvad sajtu, izaberite "*Voucher*" među dostupnim metodama plaćanja na vašem nalogu. Zatim, unesite broj Vouchera koji ste dobili sa vpn.sovereign.engineering sajta u predviđeno polje. ![MULLVAD VPN](assets/notext/25.webp) ## Kako koristiti i konfigurisati Mullvad VPN?


Sada kada imate aktivan nalog i uneli ste broj naloga u Mullvad softver ili aplikaciju, možete u potpunosti uživati u uslugama vašeg VPN-a. ![MULLVAD VPN](assets/notext/26.webp) Da biste se isključili sa VPN-a, jednostavno kliknite na dugme "*Disconnect*". ![MULLVAD VPN](assets/notext/27.webp) Mala crvena strelica pored dugmeta "*Disconnect*" omogućava vam da promenite servere bez promene trenutne lokacije. ![MULLVAD VPN](assets/notext/28.webp) Ako želite da promenite grad za vaš VPN server, kliknite na "*Switch location*" da biste izabrali novu lokaciju. ![MULLVAD VPN](assets/notext/29.webp) Na vrhu ekrana videćete nadimak vašeg uređaja kao i preostalo trajanje vašeg paketa. ![MULLVAD VPN](assets/notext/30.webp) Klikom na ikonu malog čoveka, pristupićete detaljnim informacijama o vašem nalogu. ![MULLVAD VPN](assets/notext/31.webp) Da biste pristupili podešavanjima, kliknite na zupčanik. ![MULLVAD VPN](assets/notext/32.webp) U meniju "*User Interface settings*", možete prilagoditi podešavanja vašeg softvera, uključujući jezik Interface i njegovo ponašanje na vašem sistemu. ![MULLVAD VPN](assets/notext/33.webp) U meniju "*VPN settings*", pronaći ćete opcije vezane za vaš VPN. Preporučujem da omogućite opcije "*Launch app on start-up*" i "*Auto-connect*" kako bi se vaša VPN konekcija automatski pokrenula kada se vaša mašina pokrene.

![MULLVAD VPN](assets/notext/34.webp) In the "*DNS content blockers*" submenu, you have the option to filter and block DNS requests to malicious, advertising, or unwanted websites.

![MULLVAD VPN](assets/notext/35.webp)

Konačno, meni "*Split tunneling*" omogućava vam da odaberete specifične aplikacije na vašem računaru za koje internet saobraćaj neće biti usmeren kroz VPN.

![MULLVAD VPN](assets/notext/36.webp)

Da biste dobili pregled svog Mullvad naloga i upravljali raznim povezanim uređajima, možete kliknuti na meni "*Devices*" na vebsajtu.

![MULLVAD VPN](assets/notext/37.webp)

I eto ga, sada ste spremni da u potpunosti uživate u Mullvad VPN-u. Ako ste zainteresovani da otkrijete drugog VPN provajdera sličnog Mullvadu, kako po funkcijama tako i po ceni, preporučujem da pogledate naš vodič o IVPN-u:


https://planb.network/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68