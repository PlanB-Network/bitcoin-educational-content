---
name: IVPN
description: Postavljanje VPN-a plaćenog bitcoinima
---
![cover](assets/cover.webp)


VPN ("*Virtualna privatna mreža*") je usluga koja uspostavlja sigurnu i šifrovanu vezu između vašeg telefona ili računara i udaljenog servera kojim upravlja VPN provajder.


Tehnički, kada se povezujete na VPN, vaš internet saobraćaj se preusmerava kroz šifrovani tunel do VPN servera. Ovaj proces otežava trećim stranama, kao što su Internet provajderi (ISPs) ili zlonamerni akteri, da presretnu ili pročitaju vaše podatke. VPN server tada deluje kao posrednik koji se povezuje na uslugu koju želite da koristite u vaše ime. On dodeljuje novu IP adresu vašoj vezi, tako što pomaže da sakrijete vašu pravu IP adresu od sajtova koje posećujete. Međutim, suprotno onome što neki online oglasi mogu sugerisati, korišćenje VPN-a ne omogućava vam anonimno pretraživanje interneta, jer zahteva oblik poverenja u VPN provajdera koji može videti sav vaš saobraćaj.

![IVPN](assets/fr/01.webp)

Prednosti korišćenja VPN-a su brojne. Prvo, čuva privatnost vaših online aktivnosti od ISP-ova ili vlada, pod uslovom da VPN provajder ne deli vaše informacije. Drugo, obezbeđuje vaše podatke, posebno kada ste povezani na javne Wi-Fi mreže, koje su podložne MITM (man-in-the-middle) napadima. Treće, sakrivanjem vaše IP adrese, VPN vam omogućava da zaobiđete geografska ograničenja i cenzuru, kako biste pristupili sadržaju koji bi inače bio nedostupan ili blokiran u vašem regionu.


Kao što možete videti, VPN prebacuje rizik posmatranja saobraćaja na VPN provajdera. Stoga, prilikom izbora vašeg VPN provajdera, važno je razmotriti lične podatke potrebne za registraciju. Ako provajder traži informacije kao što su vaš broj telefona, email, podaci o bankovnoj kartici, ili još gore, vašu poštansku adresu, rizik povezivanja vašeg identiteta sa vašim saobraćajem se povećava. U slučaju kompromitovanja provajdera ili pravne zaplene, bilo bi lako povezati vaš saobraćaj sa vašim ličnim podacima. Stoga se preporučuje odabir provajdera koji ne zahteva nikakve lične podatke i prihvata anonimna plaćanja, kao što su bitkoini.


U ovom vodiču predstavljam jednostavno, efikasno i cenovno pristupačno VPN rešenje koje ne zahteva lične informacije za korišćenje.


## Uvod u IVPN


IVPN je VPN usluga dizajnirana posebno za korisnike koji traže oblik privatnosti. Za razliku od popularnih VPN provajdera koji se često promovišu na YouTube-u, IVPN se ističe svojom transparentnošću, sigurnošću i poštovanjem privatnosti.

IVPN-ova politika privatnosti je stroga: nije potrebno unositi lične informacije prilikom registracije. Možete otvoriti nalog bez pružanja email-a, imena ili broja telefona. Za plaćanje, nije potrebno unositi podatke o kreditnoj kartici, jer IVPN prihvata plaćanja u bitkoinima (onchain i Lightning). Štaviše, IVPN tvrdi da ne vodi evidenciju aktivnosti, što znači da, teoretski, vaš internet saobraćaj nije zabeležen od strane kompanije.

IVPN je takođe [potpuno open-source](https://github.com/ivpn), što se tiče njihovog softvera, aplikacija, pa čak i njihove veb stranice, omogućavajući svakome da proveri i pregleda njihov kod. Oni takođe prolaze kroz nezavisne bezbednosne revizije svake godine, čiji su rezultati objavljeni na njihovoj veb stranici.


IVPN isključivo koristi servere koje sami hostuju, čime eliminišu rizike povezane sa korišćenjem usluga trećih strana u oblaku, kao što su AWS, Google Cloud ili Microsoft Azure.


Usluga nudi brojne napredne funkcije, kao što je multi-hop, koji usmerava saobraćaj kroz više servera smeštenih u različitim jurisdikcijama kako bi se poboljšala anonimnost. IVPN takođe integriše blokator tragača i oglasa, i nudi opciju izbora između različitih VPN protokola.


Prirodno, ovaj kvalitet usluge dolazi uz cenu, ali adekvatna cena je često pokazatelj kvaliteta i poštenja. Može signalizirati da kompanija ima poslovni model bez potrebe za prodajom ličnih podataka. IVPN zatim nudi 2 tipa planova: Standard plan, koji omogućava povezivanje do 2 uređaja, i Pro plan, koji omogućava do 7 konekcija i uključuje "*Multi-hop*" protokol koji usmerava vaš saobraćaj kroz više servera.


Za razliku od glavnih VPN provajdera, IVPN funkcioniše po modelu kupovine vremena pristupa usluzi, umesto po modelu pretplate koja se obnavlja. Plaćate u bitcoinima jednom za odabrani period. Na primer, ako kupite godinu dana pristupa, možete koristiti uslugu tokom tog perioda, nakon čega ćete morati da se vratite na IVPN vebsajt da biste kupili više vremena pristupa.


[IVPN cene](https://www.ivpn.net/en/pricing/) su progresivne u zavisnosti od trajanja pristupa koji se kupuje. Ovde su cene za Standard plan:


- 1 nedelja: $2
- 1 mesec: $6
- 1 godina: $60
- 2 godine: $100
- 3 godine: $140


A za Pro plan:


- 1 nedelja: $4
- 1 mesec: $10
- 1 godina: $100
- 2 godine: $160
- 3 godine: $220


## Kako instalirati IVPN na računar?

Preuzmite [najnoviju verziju softvera](https://www.ivpn.net/en/apps-windows/) za vaš operativni sistem, a zatim nastavite sa instalacijom prateći korake u čarobnjaku za instalaciju. ![IVPN](assets/notext/02.webp)

Za korisnike Linux-a, pogledajte uputstva specifična za vašu distribuciju dostupna na [ovoj stranici](https://www.ivpn.net/en/apps-linux/).

![IVPN](assets/notext/03.webp)

Kada je instalacija završena, potrebno je uneti ID vašeg naloga. Videćemo kako ga dobiti u narednim delovima ovog vodiča.

![IVPN](assets/notext/04.webp)

## Kako instalirati IVPN na pametni telefon?


Preuzmite IVPN iz vaše prodavnice aplikacija, bilo da je to [AppStore](https://apps.apple.com/us/app/ivpn-secure-vpn-for-privacy/id1193122683) za iOS korisnike, [Google Play Store](https://play.google.com/store/apps/details?id=net.ivpn.client) za Android, ili [F-Droid](https://f-droid.org/en/packages/net.ivpn.client). Ako koristite Android, takođe imate opciju da preuzmete `.apk` datoteku direktno sa [IVPN sajta](https://www.ivpn.net/en/apps-android/).

![IVPN](assets/notext/05.webp)

Prilikom prve upotrebe aplikacije, bićete odjavljeni. Moraćete da unesete svoj ID naloga da biste aktivirali uslugu.

![IVPN](assets/notext/06.webp)

Sada, pređimo na aktiviranje IVPN-a na vašim uređajima.


## Kako platiti i aktivirati IVPN?


Idite na zvaničnu IVPN veb stranicu [na stranici za plaćanje](https://www.ivpn.net/en/pricing/).

![IVPN](assets/notext/07.webp)

Odaberite plan koji najbolje odgovara vašim potrebama. Za ovaj vodič, odlučićemo se za Standard plan, koji nam omogućava da aktiviramo VPN na našem računaru i pametnom telefonu, na primer.

![IVPN](assets/notext/08.webp)

IVPN će tada kreirati vaš nalog. Ne morate da pružite bilo kakve lične podatke. Samo vaš ID naloga će vam omogućiti da se prijavite. On deluje donekle kao ključ za pristup. Sačuvajte ga na sigurnom mestu kao što je vaš menadžer lozinki, na primer. Takođe možete napraviti papirnu kopiju.

![IVPN](assets/notext/09.webp)

Na istoj stranici, izaberite trajanje vaše pretplate na uslugu.

![IVPN](assets/notext/10.webp)

Zatim izaberite svoj način plaćanja. Što se mene tiče, izvršiću uplatu putem Lightning mreže, tako što ču da kliknem na dugme "*Bitcoin*".

![IVPN](assets/notext/11.webp)

Proverite da li vam sve odgovara, a zatim kliknite na dugme "*Pay with Lightning*".

![IVPN](assets/notext/12.webp)

Lightning faktura će vam biti predstavljena na njihovom BTCPay Serveru. Skenirajte QR kod sa vašim Lightning novčanikom i nastavite sa plaćanjem.

![IVPN](assets/notext/13.webp) 

Kada je faktura plaćena, kliknite na dugme "*Return to IVPN*".

![IVPN](assets/notext/14.webp)

Vaš nalog sada se prikazuje kao "*Aktivan*," i možete videti datum do kojeg važi vaš pristup VPN-u. Nakon tog datuma, biće potrebno da obnovite uplatu.

![IVPN](assets/notext/15.webp)

Da biste aktivirali svoju vezu putem IVPN-a na svom računaru, jednostavno kopirajte svoj ID naloga.

![IVPN](assets/notext/16.webp)

I zalepite ga u softver koji ste prethodno preuzeli.

![IVPN](assets/notext/17.webp)

Zatim kliknite na dugme "*Login*".

![IVPN](assets/notext/18.webp)

Kliknite na kvačicu da aktivirate VPN vezu, i eto, internet saobraćaj vašeg računara je sada šifrovan i preusmeren preko IVPN servera.

![IVPN](assets/notext/19.webp)

Za vaš pametni telefon, postupak je identičan. Zalepite ID vašeg naloga ili skenirajte QR kod povezan sa vašim IVPN nalogom dostupnim na vebsajtu. Zatim, kliknite na oznaku za potvrdu da uspostavite vezu.

![IVPN](assets/notext/20.webp)

## Kako koristiti i konfigurisati IVPN?


U pogledu korišćenja i podešavanja, prilično je jednostavno. Sa glavnog interfejsa, možete aktivirati ili deaktivirati vezu jednostavno korišćenjem oznake za potvrdu.

![IVPN](assets/notext/21.webp)

Takođe imate opciju da pauzirate svoj VPN na određeno vreme.

![IVPN](assets/notext/22.webp)

Klikom na trenutni server, možete izabrati drugi server od dostupnih.

![IVPN](assets/notext/23.webp)

Takođe je moguće aktivirati ili deaktivirati integrisani firewall kao i funkciju protiv praćenja.

![IVPN](assets/notext/24.webp)

Da biste pristupili dodatnim postavkama, kliknite na ikonu postavki.

![IVPN](assets/notext/25.webp)

U kartici "*Account*" pronaći ćete postavke vezane za vaš nalog.

![IVPN](assets/notext/26.webp)

U kartici "*General*", postoji nekoliko podešavanja klijenta. Savetujem vam da označite opcije "*Launch at login*" i "*On launch*" u sekciji "*Autoconnect*" kako biste automatski uspostavili vezu sa VPN-om prilikom pokretanja vašeg računara.

![IVPN](assets/notext/27.webp)

U kartici "*Connection*" pronaći ćete razne opcije vezane za konekciju. Ovde možete promeniti VPN protokol koji se koristi.

![IVPN](assets/notext/28.webp)

Kartica "*IVPN Firewall*" omogućava vam da sistematski aktivirate firewall pri pokretanju računara, osiguravajući da nijedna veza nije uspostavljena van VPN-a.

![IVPN](assets/notext/29.webp)

Kartica "*Split Tunnel*" nudi mogućnost isključivanja određenog softvera iz VPN veze. Aplikacije dodate ovde će nastaviti da rade sa normalnom internet vezom čak i kada je VPN omogućen.

![IVPN](assets/notext/30.webp)

U kartici "*WiFi control*", imate opciju da konfigurišete specifične akcije u skladu sa mrežama na koje ste povezani. Na primer, možete označiti vašu kućnu mrežu kao "*Trusted*" i konfigurisati VPN da se ne aktivira na ovoj mreži, ali da se automatski aktivira na bilo kojoj drugoj WiFi mreži.

![IVPN](assets/notext/31.webp)

U meniju "*AntiTracker*", izaberite profil blokiranja za vaš anti-tracker. Ovo je dizajnirano da blokira oglase, malware i trackere podataka blokiranjem zahteva ka uslugama praćenja dok pretražujete Internet. Ovo poboljšava vašu privatnost sprečavanjem kompanija da prikupljaju i prodaju vaše podatke o pretraživanju. Dostupan je i "*Hardcore Mode*" koji potpuno blokira sve domene u vlasništvu Google-a i Meta-e, kao i sve zavisne usluge.

![IVPN](assets/notext/32.webp)

I eto, sada ste opremljeni da u potpunosti uživate u IVPN-u. Ako takođe želite da poboljšate sigurnost svojih online naloga korišćenjem lokalnog menadžera lozinki, pozivam vas da pogledate naš vodič o KeePass-u, besplatnom i open-source rešenju:


https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Ako ste zainteresovani da otkrijete drugog VPN provajdera sličnog IVPN-u, kako po karakteristikama tako i po ceni, preporučujem da pogledate naš vodič o Mullvad-u:


https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8
