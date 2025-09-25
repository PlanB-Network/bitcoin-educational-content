---
name: RoninDojo v2
description: Instaliranje vašeg RoninDojo v2 Bitcoin čvora na Raspberry Pi
---
![cover RoninDojo v2](assets/cover.webp)


**UPOZORENJE:** Nakon hapšenja osnivača Samourai novčanika i zaplene njihovih servera 24. aprila, određene funkcije RoninDojo-a, kao što je Whirlpool, više nisu operativne. Međutim, moguće je da bi ovi alati mogli biti ponovo uspostavljeni ili pokrenuti na drugačiji način u narednim nedeljama. Dodatno, pošto je RoninDojo kod bio hostovan na Samourai-evom GitLab-u, koji je takođe zaplenjen, trenutno nije moguće preuzeti kod sa interneta. Timovi RoninDojo-a verovatno rade na ponovnom objavljivanju koda.*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo korišćenje ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

> Koristite Bitcoin uz očuvanje privatnosti.

U prethodnom vodiču, već smo objasnili postupak instalacije i korišćenja RoninDojo v1. Međutim, tokom protekle godine, timovi RoninDojo su lansirali verziju 2 svoje implementacije, što je označilo značajnu prekretnicu u arhitekturi softvera. Naime, prešli su sa Linux Manjaro distribucije na Debian. Shodno tome, više ne nude unapred konfigurisan imidž za automatsku instalaciju na Raspberry Pi. Ali i dalje postoji metoda za ručnu instalaciju. Ovo je ono što sam koristio za svoj čvor, i od tada, RoninDojo v2 radi odlično na mom Raspberry Pi 4. Stoga nudim novi vodič o tome kako ručno instalirati RoninDojo v2 na Raspberry Pi.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0

## Sadržaj:


- Šta je RoninDojo?
- Koji hardver odabrati za instalaciju RoninDojo v2?
- Kako sastaviti Raspberry Pi 4?
- Kako instalirati RoninDojo v2 na Raspberry Pi 4?
- Kako koristiti svoj RoninDojo v2 čvor?


## Šta je RoninDojo?

Dojo je u početku potpuna implementacija Bitcoin čvora, zasnovana na Bitcoin Core-u, i razvijena od strane Samourai Wallet timova. Ovo rešenje može biti instalirano na bilo koju opremu. Za razliku od drugih Core implementacija, Dojo je specifično optimizovan za integraciju sa Android aplikacionim okruženjem Samourai novčanik. Što se tiče RoninDojo, to je alat dizajniran da olakša instalaciju i upravljanje Dojo-om, kao i raznim drugim komplementarnim alatima. Ukratko, RoninDojo obogaćuje osnovnu implementaciju Dojo-a integracijom mnoštva dodatnih alata, dok pojednostavljuje njegovu instalaciju i upravljanje.


Ronin takođe nudi [rešenje "node-in-box", pod nazivom "*Tanto*"](https://ronindojo.io/en/products), uređaj sa već instaliranim RoninDojo sistemom koji je sastavila njihova ekipa. Tanto je plaćena opcija, koja može biti zanimljiva za one koji žele da izbegnu tehničke komplikacije. Ali pošto je izvorni kod RoninDojo-a otvoren, moguće ga je instalirati i na sopstvenom hardveru. Ova alternativa, ekonomičnija, ipak zahteva dodatne manipulacije, koje ćemo pokriti u ovom vodiču.

RoninDojo je Dojo, tako da omogućava laku integraciju Whirlpool CLI u vaš Bitcoin čvor kako bi se obezbedilo najbolje moguće CoinJoin iskustvo. Sa Whirlpool CLI, postaje moguće kontinuirano mešati vaše bitkoine, 24 sata dnevno, 7 dana u nedelji, bez potrebe da vaš lični računar ostane uključen.


Iza Whirlpool CLI, RoninDojo uključuje razne alate za poboljšanje funkcionalnosti vašeg Dojo-a. Među njima, Boltzmann kalkulator analizira nivo privatnosti vaših transakcija, Electrum server omogućava povezivanje vaših Bitcoin novčanika sa vašim čvorom, a Mempool server omogućava vam da lokalno pregledate vaše transakcije, bez curenja informacija.


U poređenju sa drugim node rešenjima kao što je Umbrel, RoninDojo je jasno fokusiran na [On-Chain](https://planb.network/resources/glossary/onchain) rešenja i alate za privatnost. Za razliku od Umbrel-a, RoninDojo ne podržava postavljanje Lightning node-a niti integraciju opštijih server aplikacija. Iako RoninDojo nudi manje svestranih alata od Umbrel-a, ima sve osnovne funkcionalnosti za upravljanje vašim On-Chain aktivnostima.


Ako vam nisu potrebne generalističke funkcionalnosti ili one povezane sa Lightning mrežom koje nudi Umbrel, a tražite jednostavan, stabilan čvor sa osnovnim alatima kao što su Whirlpool ili Mempool, RoninDojo bi mogao biti idealno rešenje. Dok Umbrel teži da postane mini server za više zadataka orijentisan ka Lightning mreži i svestranosti, RoninDojo, u skladu sa filozofijom Samourai novčanika, fokusira se na osnovne alate za privatnost korisnika.


Sada kada smo predstavili RoninDojo, hajde da zajedno vidimo kako da postavimo ovaj čvor.


## Koji hardver odabrati za instalaciju RoninDojo v2?

RoninDojo nudi sliku za automatsku instalaciju svog softvera na [RockPro64](https://ronindojo.io/en/download). Međutim, naš vodič se fokusira na ručnu proceduru instalacije na Raspberry Pi 4. Iako je Raspberry Pi 5 nedavno lansiran, i ovaj vodič bi teoretski trebao biti kompatibilan sa ovim novim modelom, još uvek nisam imao priliku da ga lično testiram, niti sam pronašao povratne informacije iz zajednice. Čim nabavim Pi 5 i kompatibilne komponente, ažuriraću ovaj vodič kako bih vas obavestio. U međuvremenu, preporučujem da se prioritet da Pi 4, jer savršeno radi za moj čvor.

Što se mene tiče, pokrećem RoninDojo na Raspberry Pi opremljenim sa 8 GB RAM-a. Iako su neki članovi zajednice uspeli da ga pokrenu na uređajima sa samo 4 GB RAM-a, nisam lično testirao ovu konfiguraciju. S obzirom na malu razliku u ceni, čini se mudrim odlučiti se za verziju sa 8 GB RAM-a. Ovo bi takođe moglo biti korisno ako planirate da svoj Raspberry Pi iskoristite za druge svrhe u budućnosti.

Važno je napomenuti da su timovi RoninDojo prijavili česte probleme vezane za kućište i SSD adapter. I sam sam se suočio sa tim problemima. **Stoga se snažno preporučuje izbegavanje kućišta opremljenih USB kablom za SSD vašeg čvora.** Umesto toga, preferirajte karticu za proširenje skladišta posebno dizajniranu za vaš Raspberry Pi:


![storage expansion card RPI4](assets/notext/1.webp)


Da biste uskladištili Bitcoin Blockchain, biće vam potreban SSD kompatibilan sa karticom za proširenje skladišta koju ste odabrali. Trenutno (februar 2024), nalazimo se u fazi tranzicije. Očekuje se da, za nekoliko meseci, diskovi od 1 TB više neće biti dovoljni da sadrže rastuću veličinu Blockchain-a, posebno uzimajući u obzir razne aplikacije koje planirate da integrišete u svoj čvor. Neki stoga preporučuju ulaganje u SSD od 2 TB za duševni mir na duže staze. Međutim, s obzirom na trend opadanja cena SSD-ova iz godine u godinu, drugi predlažu da se zadovoljite diskom od 1 TB, koji bi trebao biti dovoljan za jednu ili dve godine, uz argument da će, do trenutka kada postane zastareo, cena modela od 2 TB verovatno pasti. Izbor stoga zavisi od vaših ličnih preferencija. Ako planirate da zadržite svoj RoninDojo na duži vremenski period i želite da izbegnete bilo kakvo tehničko rukovanje u narednim godinama, opcija SSD-a od 2 TB čini se najrazboritijom, jer vam nudi komfornu marginu za budućnost.


Pored toga, biće vam potrebne razne male komponente:


- Kućište opremljeno ventilatorom za smeštaj vašeg Raspberry Pi i vaše kartice za proširenje skladišta. Kompleti koji uključuju i SSD karticu za proširenje i kompatibilno kućište dostupni su online;
- Kabl za napajanje za vaš Raspberry Pi;
- Micro SD kartica od najmanje 16 GB (iako bi 8 GB tehnički moglo biti dovoljno, razlika u ceni između 8 i 16 GB kartica je često zanemarljiva);
- RJ45 Ethernet kabl za mrežnu vezu.


![node material](assets/notext/2.webp)


## Kako sastaviti Raspberry Pi 4?

Sklapanje vašeg čvora će se razlikovati u zavisnosti od odabranog hardvera, posebno tipa kućišta. Međutim, opšti pregled koraka koje treba pratiti ostaje uglavnom sličan u sklapanju.

Počnite instaliranjem vašeg SSD-a na karticu za proširenje skladišta, pazeći da osigurate dva zavrtanja za zaključavanje na zadnjoj strani.


![assembly1](assets/notext/3.webp)


Zatim pričvrstite svoj Raspberry Pi na ekspanzionu karticu.


![assembly2](assets/notext/4.webp)


Takođe, pričvrstite ventilator na Raspberry Pi.


![assembly3](assets/notext/5.webp)


Povežite različite komponente, pazeći da koristite ispravne pinove, pozivajući se na priručnik vašeg kućišta. Proizvođači kućišta često nude video tutorijale kako bi vam pomogli u sklapanju. U mom slučaju, imam dodatnu ekspanzionu karticu opremljenu dugmetom za uključivanje/isključivanje. Ovo nije neophodno za pravljenje Bitcoin čvora. Uglavnom je koristim da bih imao dugme za napajanje.


Ako, kao i ja, imate proširenu karticu opremljenu dugmetom za uključivanje/isključivanje, ne zaboravite da instalirate mali džamper "Auto Power On". Ovo će omogućiti vašem čvoru da se automatski pokrene čim se uključi napajanje. Ova funkcija je posebno korisna u slučaju nestanka struje, jer omogućava vašem čvoru da se ponovo pokrene samostalno, bez vaše ručne intervencije.


![assembly4](assets/notext/6.webp)


Pre nego što umetnete sav hardver u kućište, važno je proveriti ispravno funkcionisanje vašeg Raspberry Pi-ja, kartice za proširenje memorije i ventilatora tako što ćete ih uključiti.


![assembly5](assets/notext/7.webp)


Na kraju, instalirajte vaš Raspberry Pi u njegovo kućište. Imajte na umu da će kasniji korak zahtevati dodavanje micro SD kartice u odgovarajući port na Raspberry Pi-ju. Ako vaše kućište ima otvor koji omogućava umetanje SD kartice bez otvaranja (kao što je slučaj sa mojim prikazanim na fotografiji), možete sada zatvoriti kućište. Međutim, ako vaše kućište nema direktan pristup micro SD portu, moraćete da sačekate dok ne pripremite micro SD karticu za umetanje pre nego što završite sklapanje.


![assembly6](assets/notext/8.webp)


## Kako instalirati RoninDojo v2 na Raspberry Pi 4?


### Korak 1: Pripremi microSD karticu za pokretanje

Nakon sastavljanja vašeg hardvera, sledeći korak je instalacija RoninDojo. Za ovo ćemo pripremiti butabilnu micro SD karticu sa vašeg računara, tako što ćemo na nju snimiti odgovarajuću sliku diska.

Trebaće vam softver _**Raspberry Pi Imager**_, dizajniran da olakša preuzimanje, konfigurisanje i upisivanje operativnih sistema na micro SD karticu za korišćenje sa Raspberry Pi-jem. Počnite instaliranjem ovog softvera na vaš lični računar:


- Za Ubuntu/Debian: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Za Windows: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Za Mac: https://downloads.raspberrypi.org/imager/imager_latest.dmg


Jednom kada je softver instaliran, otvorite ga i ubacite vašu micro SD karticu u lični računar. Iz Raspberry Pi Imager interfejsa, izaberite `CHOOSE OS`:


![choose OS](assets/notext/9.webp)


Zatim idite na meni `Raspberry Pi OS (other)`:


![choose OS others](assets/notext/10.webp)


Odaberite operativni sistem pod nazivom `Raspberry Pi OS (Legacy, 64-bit) Lite`, koji je veličine `0.3 GB`:


![choose OS Legacy Lite](assets/notext/11.webp)


Nakon odabira operativnog sistema, bićete preusmereni na glavni meni Raspberry Pi Imager-a. Kliknite na `CHOOSE STORAGE`:


![choose storage](assets/notext/12.webp)


Izaberite svoju micro SD karticu:


![choose micro sd](assets/notext/13.webp)


Nakon što izaberete operativni sistem i micro SD karticu, kliknite na `NEXT`:


![choose next](assets/notext/14.webp)


Pojaviće se novi prozor. Izaberite `EDIT CONFIGURATION`:


![edit settings](assets/notext/15.webp)


U ovom prozoru idite na karticu `GENERAL` i napravite sledeća podešavanja (koja su veoma važna da bi radilo):


- Omogući opciju i dodeli `RoninDojo` kao ime hosta;
- Omogući `Set username and password`, u prevodu `Postavi korisničko ime i lozinku`, unesi `pi` kao korisničko ime, izaberi lozinku i zabeleži ove informacije, jer će biti potrebne kasnije. Ovi kredencijali su privremeni i biće obrisani nakon toga;
- Onemogući `Configure Wi-Fi`;
- Omogući `Set locale settings` i izaberi svoju vremensku zonu kao i tip tastature koji odgovara tvom računaru;


![general settings](assets/notext/16.webp)


U kartici USLUGE kliknite na polje `Enable SSH` i izaberite `Use a password for authentication`:


![services settings](assets/notext/17.webp)


Takođe, osigurajte da je u kartici `OPTIONS` telemetrija onemogućena:


![options settings](assets/notext/18.webp)


Kliknite na `SAVE`:


![settings save](assets/notext/19.webp)

Potvrdite klikom na `YES` za početak kreiranja bootabilne micro SD kartice:

![settings yes](assets/notext/20.webp)


Poruka će vas obavestiti da će svi podaci na micro SD kartici biti obrisani. Potvrdite klikom na `YES` da biste započeli proces:


![overwrite micro SD](assets/notext/21.webp)


Sačekajte dok softver ne završi pripremu vaše micro SD kartice:


![writing micro SD](assets/notext/22.webp)


Kada se pojavi poruka koja označava kraj procesa, možete ukloniti micro SD karticu iz vašeg računara:


![writing micro SD completed](assets/notext/23.webp)


### Korak 2: Završite sklapanje čvora

Sada možete umetnuti micro SD karticu u odgovarajući port vašeg Raspberry Pi-ja.


![micro SD](assets/notext/24.webp)


Zatim povežite svoj Raspberry Pi sa ruterom koristeći Ethernet kabl. Na kraju, uključite svoj čvor povezivanjem kabla za napajanje i pritiskom na dugme za napajanje (ako vaša postavka uključuje jedno).


### Korak 3: Uspostavite SSH vezu sa čvorom

Prvo, potrebno je pronaći IP adresu vašeg čvora. Imate opciju da koristite alat kao što je _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ ili _[Angry IP Scanner](https://angryip.org/)_, ili proverite administratorski interfejs vašeg rutera.. IP adresa treba da bude u formi `192.168.1.??`. **Za sve naredne komande, zamenite `[IP]` sa stvarnom IP adresom vašeg čvora**, (uklanjajući zagrade).


Pokreni terminal.


Da biste uklonili mogući ključ koji je već povezan sa IP adresom vašeg čvora, izvršite komandu:

`ssh-keygen -R [IP]`.


Greška nakon ove komande nije ozbiljna; to jednostavno znači da ključ ne postoji u vašoj listi poznatih hostova (što je prilično verovatno). Na primer, ako je IP vaše čvorne tačke `192.168.1.40`, komanda postaje: `ssh-keygen -R 192.168.1.40`.


Zatim uspostavite SSH vezu sa svojim čvorom izvršavanjem komande:

`ssh pi@[IP]`.

Pojaviće se poruka u vezi sa autentičnošću hosta: `The authenticity of host '[IP]' can't be established.` Ovo ukazuje da autentičnost uređaja sa kojim pokušavate da se povežete ne može biti verifikovana zbog nedostatka poznatog javnog ključa. Kada se prvi put povezujete putem SSH-ja na novog hosta, ova poruka će se uvek pojaviti. Morate odgovoriti sa `yes` da biste dodali njegov javni ključ u vaš lokalni direktorijum, što će sprečiti da se ova poruka upozorenja pojavljuje tokom budućih SSH konekcija na ovaj čvor. Dakle, otkucajte `yes` i pritisnite `enter` da biste potvrdili.

Bićete zatim upitani da unesete svoju lozinku, onu koja je prethodno postavljena kao privremena u koraku 1. Potvrdite sa `enter`. Zatim ćete biti povezani sa svojim čvorom putem SSH-a.


Ukratko, evo komandi za izvršavanje:


- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `yes`
- Unesite privremenu lozinku i potvrdite.


### Korak 4: Ažuriranje i priprema

Sada ste povezani sa svojim čvorom putem SSH sesije. Na vašem terminalu, komandna linija bi trebala biti: `pi@RoninDojo:~ $`. Za početak, ažurirajte listu dostupnih paketa i instalirajte ažuriranja za postojeće pakete sledećom komandom:

`sudo apt update && sudo apt upgrade -y`


Kada se ažuriranja završe, nastavite sa instalacijom *Git* i *Dialog* koristeći komandu:

`sudo apt install git dialog -y`


Zatim, klonirajte granu `master` Git repozitorijuma _RoninOS_ izvršavanjem:

`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`


Pokreni skriptu `customize-image.sh` sa komandom:

`cd /opt/RoninOS/ && sudo ./customize-image.sh`


**Važno je pustiti skriptu da radi bez prekida i strpljivo čekati kraj njenog procesa**, što traje oko 10 minuta. Kada se pojavi poruka `Setup is complete`, možete preći na sledeći korak.


### Korak 5: Pokretanje RoninOS-a

Pokrenite RoninOS komandom:

`sudo systemctl start ronin-setup`


Za prikaz linija log fajla koristi komandu:
`tail -f /home/ronindojo/.logs/setup.logs`


U ovoj fazi, **važno je pustiti RoninOS da se pokrene i sačekati da završi sa radom.** Ovo traje oko 40 minuta. Kada se pojavi `All RoninDojo feature installations complete!`, možete preći na korak 6.


### Korak 6: Pristupanje RoninUI i promena kredencijala

Nakon završetka instalacije, da biste se povezali sa svojim čvorom putem pregledača, osigurajte da je vaš lični računar povezan na istu lokalnu mrežu kao i vaš čvor. Ako koristite VPN na svom računaru, privremeno ga onemogućite. Da biste pristupili interfjesu čvoru u svom pregledaču, unesite u URL traku:


- Direktno IP adresu vašeg čvora, na primer, `192.168.1.??`;
- Ili, otkucajte `ronindojo.local`.


Jednom kada se nađete na početnoj stranici RoninUI, bićete pozvani da započnete podešavanje. Da biste to učinili, kliknite na dugme `Let's start`.


![lets start](assets/notext/25.webp)


U ovoj fazi, RoninUI vam prikazuje vašu `root` lozinku. Važno je da je čuvate na sigurnom. Možete se odlučiti za fizičku kopiju, na papiru, ili je sačuvati u [menadžeru lozinki](https://planb.network/courses/99c46148-7080-4915-a7e0-9df0e145cd47/0b3c69b2-522c-56c8-9fb8-1562bd55930f).


![root password](assets/notext/26.webp)


Nakon što sačuvate lozinku `root`, označite polje `I have backed up Root user credentials` i kliknite na `Continue` da nastavite.


![confirm root password](assets/notext/27.webp)


Sledeći korak uključuje kreiranje korisničke lozinke, koja će se koristiti i za pristup RoninUI web interfejsu i za uspostavljanje SSH sesija sa vašim čvorom. Izaberite jaku lozinku i obavezno je sačuvajte na sigurnom mestu. Biće potrebno da unesete ovu lozinku dva puta pre nego što kliknete na `Finish` za potvrdu. Što se tiče korisničkog imena, preporučuje se da zadržite podrazumevani izbor, `ronindojo`. Ako odlučite da ga promenite, zapamtite da u skladu s tim prilagodite komande u narednim koracima.


![user credentials](assets/notext/28.webp)


Kada se ove radnje završe, sačekajte da se vaš čvor inicijalizuje. Zatim ćete pristupiti RoninUI web interfejsu. Skoro ste na kraju procesa, ostalo je još samo nekoliko malih koraka!

![Ronin UI](assets/notext/29.webp)


### Korak 7: Uklonite privremene kredencijale

Otvorite novi terminal na svom ličnom računaru i uspostavite SSH vezu sa svojim čvorom koristeći sledeću komandu:

`SSH ronindojo@[IP]`


Ako je, na primer, IP adresa vašeg čvora `192.168.1.40`, odgovarajuća komanda će biti:

`SSH ronindojo@192.168.1.40`


Ako ste promenili svoje korisničko ime tokom prethodnog koraka, zamenjujući podrazumevano korisničko ime (`ronindojo`) sa drugim, obavezno koristite ovo novo ime u komandi. Na primer, ako ste izabrali `planb` kao korisničko ime i IP adresa je `192.168.1.40`, komanda koju treba uneti će biti:

`SSH planb@192.168.1.40`

Bićete zamoljeni da unesete korisničku lozinku. Unesite je i zatim pritisnite `enter` da biste potvrdili. Zatim ćete pristupiti RoninCLI interfejsu. Koristite strelice na tastaturi da biste se pomerili do opcije `Exit RoninDojo` i pritisnite `enter` da biste je izabrali.

![RoninCLI](assets/notext/30.webp)


U ovom trenutku, nalazite se u terminalu vašeg čvora, sa komandnom linijom sličnom ovoj: `ronindojo@RoninDojo:~ $`. Da biste uklonili privremenog korisnika kreiranog tokom konfiguracije butabilne micro SD kartice, unesite sledeću komandu i pritisnite `enter`:

`sudo deluser --remove-home pi`


Bićete upitani da potvrdite svoju korisničku lozinku. Unesite je i potvrdite pritiskom na `enter`. Sačekajte da se operacija završi, zatim koristite komandu `exit` da napustite terminal.


Čestitamo! Vaš RoninDojo v2 čvor je sada konfigurisan i spreman za korišćenje. Počeće svoj IBD (*Initial Block Download*), nastavljajući sa preuzimanjem i verifikacijom Bitcoin blockchain-a od Genesis bloka. Ovaj korak uključuje preuzimanje svih Bitcoin transakcija napravljenih od 3. januara 2009. godine i može potrajati neko vreme. Kada se blockchain u potpunosti preuzme, indeksator će nastaviti sa kompresovanjem baze podataka. Trajanje IBD-a može značajno varirati. Vaš RoninDojo čvor će biti potpuno operativan kada se ovaj proces završi.


**Ako prelazite sa starog RoninDojo v1 čvora** na ovu novu verziju uz pomoć ovog vodiča, a pritom zadržavate isti SSD, vaš čvor bi automatski trebalo da detektuje i ponovo iskoristi postojeće podatke na disku, čime ćete biti pošteđeni potrebe za ponovnim izvođenjem IBD-a. U tom slučaju, samo ćete morati da sačekate da se vaš čvor ponovo sinhronizuje sa najnovijim blokovima.


### Korak 8: "veth fix"

Ako naiđete na grešku sa vašim RoninDojo v2 na Raspberry Pi, gde nakon jednostavne instalacije vaš čvor iznenada postane nedostupan putem SSH-a, ali se oporavi nakon jednostavnog ponovnog pokretanja, potrebno je da pratite ovaj korak 8. Ova uobičajena greška može se lako popraviti rešenjem koje je razvila zajednica: "_veth fix_". Ova manja korekcija trajno rešava nagle prekide veze. Evo kako da je primenite.


Otvorite novi terminal na vašem ličnom računaru i uspostavite SSH vezu sa vašim čvorom koristeći sledeću komandu:

`SSH ronindojo@[IP]`


Ako je, na primer, IP adresavašeg čvora `192.168.1.40`, odgovarajuća komanda bi bila:

`SSH ronindojo@192.168.1.40`


Bićete upitani da unesete korisničku lozinku. Unesite je i pritisnite `enter` da biste potvrdili. Zatim ćete pristupiti RoninCLI interfejsu. Koristite strelice na tastaturi da biste se pomerili do opcije `Exit RoninDojo` i pritisnite `enter` da biste je izabrali.


U ovom trenutku, nalazite se na terminalu vašeg čvora, sa komandnom linijom sličnom: `ronindojo@RoninDojo:~ $`. Da biste primenili **veth** popravku, ukucajte sledeću komandu i pritisnite `enter`:

`sudo nano /etc/dhcpcd.conf`


Ponovo potvrdite svoju lozinku i pritisnite `enter`.


Stići ćete do datoteke `dhcpcd.conf`. Potrebno je da kopirate sledeći tekst, uključujući zvezdicu, i dodate ga na dno datoteke:

`denyinterfaces veth*`


Da biste to uradili, pomerite se na dno fajla koristeći strelicu nadole na tastaturi, zatim koristite desni klik miša da nalepite tekst na nezavisnu liniju.


Nakon dodavanja teksta, pritisnite `ctrl X` da započnete izlazak, zatim `ctrl Y` da potvrdite čuvanje izmena, i pritisnite `enter` da finalizirate i vratite se na komandnu liniju. Da biste osigurali da je izmena ispravno primenjena, ponovo otvorite `dhcpcd.conf` fajl koristeći odgovarajuću komandu.


Da biste dovršili primenu popravke, ponovo pokrenite svoj čvor izvršavanjem:

`sudo reboot now`


U ovom trenutku, možete zatvoriti svoj terminal. Dozvolite potrebno vreme da se vaš RoninDojo ponovo pokrene, nakon čega bi trebalo da se ponovo povežete putem grafičkog interfejsa u vašem pregledaču. Ovaj proces bi trebalo da reši naiđeni problem.


## Kako koristiti svoj RoninDojo v2 čvor?


### Povezivanje vašeg softverskog novčanika sa Electrs

Prva upotreba vašeg sveže instaliranog i sinhronizovanog čvora biće emitovanje vaših transakcija na Bitcoin mrežu. Verovatno ćete želeti da povežete vaše različite novčanike sa vašim čvorom kako biste emitovali vaše transakcije poverljivo. To možete učiniti putem Electrum Rust Servera (electrs). Ova aplikacija je obično unapred instalirana na vašem RoninDojo čvoru. Ako nije, možete je ručno instalirati putem RoninCLI interfejsa u `Applications > Manage Applications > Install Electrum Server`.


Da biste dobili Tor adresu vašeg Electrum Servera, sa RoninUI web interfejsom, idite na:

`Pairing > Electrum server > Pair now`

![Pairing](assets/notext/31.webp)

![Electrs](assets/notext/32.webp)

Trebaće da unesete `Hostname` adresu koja se završava sa `.onion` iz vašeg softverskog novčanika, zajedno sa portom `50001`. ![hostname](assets/notext/33.webp)

Na primer, za Sparrow novčanika, jednostavno idite na karticu:

`File > Preferences > Server > Private Electrum`


![Sparrow](assets/notext/34.webp)


### Povezivanje vašeg softverskog novčanika sa Samourai Dojo

Kao alternativu korišćenju Electrs-a, Dojo omogućava da povežete vaš kompatibilni softverski novčanik direktno na vaš RoninDojo čvor. Novčanici kao što su Samourai novčanik i Sentinel nude ovu funkcionalnost.


Da biste uspostavili vezu, samo ćete trebati skenirati QR kod vašeg Dojo-a. Da biste pristupili ovom QR kodu putem RoninUI, idite na:

`Pairing > Samourai Dojo > Pair now`

![Samourai Dojo](assets/notext/35.webp)

Da biste povezali svoj Samourai novčanik sa svojim Dojo-om, jednostavno skenirajte ovaj QR kod tokom instalacije aplikacije:


![Samourai Wallet connection](assets/notext/36.webp)


Ako ste već imali Samourai novčanik pre nego što ste postavili svoj Ronin Dojo, potrebno je da napravite rezervnu kopiju svog novčanika, deinstalirate i zatim ponovo instalirate Samourai novčanik aplikaciju, pre nego što obnovite svoj novčanik. Kada pokrenete ponovo instaliranu aplikaciju, imaćete opciju da se povežete sa novim Dojo-om. **Budite oprezni, ovaj proces nosi rizik od gubitka vaših bitcoina ako nije pravilno izvršen!** Uverite se da imate rezervnu kopiju svog Samourai novčanika u svojim fajlovima i proverite validnost svog passphrase-a putem `Settings > Troubleshoot > passphrase`. Takođe je važno da imate čitljivu rezervnu kopiju svoje fraze za oporavak i svog passphrase. Za više preciznosti u ovoj operaciji, preporučuje se da pratite ovaj detaljni vodič: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).


### Korišćenje sopstvenog Mempool.space blok-istraživača

Block explorer (istraživač blokova) transformiše sirove informacije iz Bitcoin blockchain-a u strukturirani i lako čitljiv format. Sa alatima kao što je *Mempool.space*, moguće je analizirati transakcije, pretraživati specifične adrese ili čak konsultovati prosečne stope naknada mempool-ova mreže u realnom vremenu.


Međutim, korišćenje online blok istraživača predstavlja rizike za vašu privatnost i uključuje poverenje u podatke koje pružaju treće strane. Zaista, korišćenjem ovih usluga bez prolaska kroz sopstveni čvor, mogli biste nenamerno otkriti informacije o vašim transakcijama i morate se osloniti na tačnost informacija koje pruža vlasnik sajta.

Da biste ublažili ove rizike, preporučuje se korišćenje sopstvene instance *Mempool.space* putem Tor mreže, direktno hostovane na vašem čvoru. Ovo rešenje osigurava očuvanje vaše privatnosti i autonomiju vaših podataka.

Da biste to uradili, počnite instaliranjem *Mempool Space Visualizer* iz RoninUI. Na web interfejsu, idite na karticu `Dashboard` i kliknite na `Manage` ispod `Mempool Space`:

`Dashboard > Mempool Space > Manage`

![Manage mempool](assets/notext/37.webp)

Zatim kliknite na dugme `Install Mempool visualizer`:

![install mempool](assets/notext/38.webp)

Potvrdite lozinku korisnika:

![password mempool](assets/notext/39.webp)

Sačekajte da se instalacija završi, a zatim ponovo kliknite na dugme `Manage`:

![Mempool Manage](assets/notext/40.webp)

Dobićete `.onion` link za pristup vašoj instanci *Mempool.space* putem Tor mreže.

![Mempool link](assets/notext/41.webp)

Preporučujem vam da sačuvate ovaj link u svojim omiljenim stranicama na Tor pretraživaču ili da ga dodate u Tor Browser aplikaciju na svom pametnom telefonu za lak i siguran pristup sa bilo kog mesta. Ako još uvek nemate Tor pretraživač, možete ga preuzeti ovde: [https://www.torproject.org/download/](https://www.torproject.org/download/)

![Mempool Tor](assets/notext/42.webp)


### Korišćenje Whirlpool-a za mešanje vaših bitkoina

Vaš RoninDojo čvor takođe integriše _WhirlpoolCLI_, komandno-linijski interfejs koji omogućava automatizaciju Whirlpool coinjoin-a, i _WhirlpoolGUI_, grafički interfejs dizajniran za interakciju sa _WhirlpoolCLI_.


Izvođenje CoinJoin-a putem Whirlpool-a zahteva da aplikacija koja se koristi bude aktivna za izvođenje remiksa. Ovaj uslov može biti restriktivan za one koji žele postići visoke nivoe anonseta. Naime, uređaj koji hostuje aplikaciju koja integriše Whirlpool mora ostati uključen neprekidno. To znači da, kako biste učestvovali u remiksima 24 sata dnevno, vaš računar ili pametni telefon mora ostati uključen sa Samourai ili Sparrow aplikacijom otvorenom neprekidno. Rešenje za ovo ograničenje je korišćenje _WhirlpoolCLI_ na mašini koja je uvek uključena, kao što je Bitcoin čvor, omogućavajući vašim novčićima da se remiksuju bez prekida, i bez potrebe da drugi uređaj ostane uključen.


Detaljno uputstvo je u pripremi kako bi vas korak po korak vodilo kroz proces coinjoining-a sa Samourai novčanikom i RoninDojo v2, od A do Š.


Za dublje razumevanje CoinJoin-a i njegove upotrebe na Bitcoin-u, takođe vas pozivam da pogledate ovaj drugi članak: Razumevanje i korišćenje CoinJoin na Bitcoin-u, gde detaljno opisujem sve što treba da znate o ovoj tehnici.




### Korišćenje Whirlpool Stat Alata (WST)


Nakon obavljanja coinjoin-a sa Whirlpool-om, korisno je precizno proceniti nivo privatnosti postignut za vaše mešane UTXO-e. Da biste to uradili, možete koristiti Python alat *Whirlpool Stat Tool*. Ovaj alat vam omogućava da izmerite i prospektivne i retrospektivne rezultate svojih UTXO-a, dok analizirate njihovu stopu širenja u pool-u.


Da biste produbili svoje razumevanje mehanizama izračunavanja ovih anonseta, preporučujem čitanje članka: REMIX - Whirlpool, koji detaljno opisuje funkcionisanje ovih pokazatelja.


https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



Da biste pristupili WST alatu, idite na RoninCLI. Da biste to učinili, otvorite terminal na svom ličnom računaru i uspostavite SSH vezu sa svojim čvorom koristeći sledeću komandu:

`SSH ronindojo@[IP]`


Ako je, na primer, IP adresa vašeg čvora `192.168.1.40`, odgovarajuća komanda bi bila:

`SSH ronindojo@192.168.1.40`


Ako ste promenili svoje korisničko ime tokom koraka 6, zamenjujući podrazumevano korisničko ime (`ronindojo`) sa drugim, obavezno koristite ovo novo ime u komandi. Na primer, ako ste izabrali `planb` kao svoje korisničko ime i IP adresa je `192.168.1.40`, komanda koju treba uneti bi bila:

`SSH planb@192.168.1.40`


Bićete zamoljeni da unesete korisničku lozinku. Unesite je i pritisnite `enter` da biste potvrdili. Zatim ćete pristupiti RoninCLI interfejsu. Koristite strelice na tastaturi da biste se kretali do menija `Samourai Toolkit` i pritisnite `enter` da biste ga odabrali:


![Samourai Toolkit](assets/notext/43.webp)


Zatim izaberite `Whirlpool Stat Tool`:


![WST](assets/notext/44.webp)


Po pokretanju WST-a, alat će nastaviti sa automatskom instalacijom. Sačekajte tokom ovog koraka. Uputstva za korišćenje će se prikazati. Kada je instalacija završena, pritisnite bilo koji taster da pristupite WST terminalu:


![WST commands](assets/notext/45.webp)


Sledeći komandni prompt će biti prikazan:

`wst#/tmp>`


Ako želite da izađete iz ovog interfejsa i vratite se u RoninCLI meni, jednostavno unesite:

`quit`


Prvo, potrebno je konfigurisati proxy za korišćenje Tor-a, kako bi se obezbedila poverljivost prilikom izvlačenja podataka iz OXT. Unesite komandu:

`socks5 127.0.0.1:9050`


Nakon toga, nastavite sa preuzimanjem informacija o poolu koje sadrže vašu transakciju:

`download 0001`

Zamenite `0001` sa kodom denominacije bazena koji vas interesuje. Kodovi denominacija su sledeći na WST:


- Pool 0.5 bitcoina: `05`
- Bazen 0.05 bitkoina: `005`
- Bazen 0.01 bitkoina: `001`
- Bazen 0.001 bitkoina: `0001`


Nakon preuzimanja, učitajte podatke zamenom `0001` sa kodom vašeg bazena u ovoj komandi: `load 0001`


![WST loading](assets/notext/46.webp)


Sačekajte da se učitavanje završi, što može potrajati nekoliko minuta. Kada se podaci učitaju, da biste saznali anonset rezultate vašeg novčića, izvršite komandu `score` praćenu vašim txid (bez zagrada):

`rezultat [txid]`


![WST score](assets/notext/47.webp)


WST će zatim prikazati retrospektivni skor (_Backward-looking metrics_), praćen prospektivnim skorom (_Forward-looking metrics_). Pored anonset skorova, WST će takođe naznačiti stopu difuzije vaše transakcije unutar bazena, u odnosu na njen anonset.


**Važno je napomenuti da se očekivani rezultat vašeg novčića treba izračunati iz txid vaše početne mešavine, a ne iz vaše najnovije mešavine. Suprotno tome, retrospektivni rezultat UTXO se izračunava iz txid poslednjeg ciklusa.**


### Korišćenje Boltzmann kalkulatora

Boltzmann kalkulator je alat za analizu Bitcoin transakcije, koji nudi mogućnost merenja nivoa entropije među ostalim naprednim metrikama. Ovi podaci pružaju kvantifikovanu procenu privatnosti transakcije i pomažu u identifikaciji potencijalnih nedostataka. Ovaj alat je već integrisan u vaš RoninDojo čvor, što ga čini lakim za pristup i korišćenje.


Pre nego što detaljno opišemo proceduru korišćenja Boltzmann kalkulatora, važno je razumeti značenje ovih indikatora, metodu njihovog izračunavanja i njihovu korisnost. Iako su primenljivi na bilo koju Bitcoin transakciju, ovi indikatori su posebno korisni za procenu kvaliteta CoinJoin transakcije.


**Prvi indikator** koji softver izračunava je ukupan broj mogućih kombinacija, označen pod `nb combinations` u alatu. Na osnovu vrednosti uključenih UTXO-a, ovaj indikator kvantifikuje broj načina na koje se ulazi mogu povezati sa izlazima. Drugim rečima, određuje broj mogućih interpretacija koje transakcija može generisati. Na primer, CoinJoin strukturiran prema Whirlpool modelu 5x5 prikazuje `1496` mogućih kombinacija:

![combinations](assets/notext/50.webp)

Kredit: KYCP


**Drugi indikator** koji se izračunava je entropija transakcije, označena kao `Entropy`. Kada transakcija ima veliki broj mogućih kombinacija, često je relevantnije pozvati se na njenu entropiju. Ovo se definiše kao binarni logaritam broja mogućih kombinacija. Evo formule koja se koristi:


- $E$: entropija transakcije;
- $C$: broj mogućih kombinacija za transakciju.

$$E = \log_2(C)$$


U matematici, binarni logaritam (logaritam sa bazom 2) odgovara inverznoj operaciji podizanja broja 2 na određenu potenciju. Drugim rečima, binarni logaritam od $x$ je eksponent na koji 2 mora biti podignut da bi se dobilo $x$. Stoga se ovaj pokazatelj izražava u bitovima. Uzmimo primer izračunavanja entropije za CoinJoin transakciju strukturiranu prema Whirlpool 5x5 modelu, koji, kao što je ranije pomenuto, nudi broj mogućih kombinacija od `1496`:

$$ C = 1496 $$

$$ E = \log_2(1496) $$

$$ E \approx 10.5469 \text{ bits}$$


Dakle, ova transakcija CoinJoin prikazuje entropiju od 10.5469 bita, što se smatra veoma zadovoljavajućim. Što je ova vrednost viša, to transakcija dopušta više različitih interpretacija, čime se poboljšava njen nivo privatnosti.


Hajde da uzmemo dodatni primer sa konvencionalnijom transakcijom, koja sadrži jedan ulaz i dva izlaza: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://Mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)

U slučaju ove transakcije, jedina moguća interpretacija je: `(inp 0) > (Outp 0 ; Outp 1)`. Shodno tome, njena entropija je utvrđena na `0`:

$$ C = 1 $$

$$ E = \log_2(1) $$

$$ E \approx 0 \text{ bits}$$

**Treći indikator** koji pruža Boltzmann kalkulator naziva se `Efikasnost novčanika`, ili na engleskom `Wallet Efficiency`. Ovaj indikator procenjuje efikasnost transakcije poredeći je sa optimalnom transakcijom koja se može zamisliti u identičnom okruženju. Ovo nas vodi do diskusije o konceptu maksimalne entropije, koja odgovara najvećoj entropiji koju određena struktura transakcije teoretski može postići. Dakle, za Whirlpool 5x5 CoinJoin strukturu, maksimalna entropija je postavljena na `10.5469`. Efikasnost transakcije se zatim izračunava suočavanjem ove maksimalne entropije sa stvarnom entropijom analizirane transakcije. Formula koja se koristi je sledeća:


- $ER$: stvarna entropija transakcije, izražena u bitovima;
- $EM$: maksimalna moguća entropija za datu strukturu transakcije, takođe u bitovima;
- $Ef$: efikasnost transakcije, u bitovima.

$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$

$$Ef = 0 \text{ bita}$$


Ovaj indikator je takođe izražen kao procenat, njegova formula je zatim:


- $CR$: broj stvarno mogućih kombinacija;
- $CM$: maksimalan broj mogućih kombinacija sa istom strukturom;
- $Ef$: efikasnost izražena kao procenat.

$$Ef = \frac{CR}{CM}$$

$$Ef = \frac{1496}{1496}$$

$$Ef = 100\%$$


Efikasnost od `100%` tako ukazuje da transakcija maksimizira svoj potencijal za privatnost na osnovu svoje strukture.


**Četvrti indikator**, gustina entropije, ili `Entropy Density`, nudi perspektivu o entropiji u odnosu na svaki ulaz ili izlaz transakcije. Ovaj indikator je koristan za procenu i poređenje efikasnosti transakcija različitih veličina. Da biste ga izračunali, jednostavno podelite ukupnu entropiju transakcije sa ukupnim brojem uključenih ulaza i izlaza. Uzimajući primer Whirlpool 5x5 CoinJoin:


- $ED$: gustina entropije izražena u bitovima;
- $E$: entropija transakcije izražena u bitovima;
- $T$: ukupan broj ulaza i izlaza u transakciji.

$$T = 5 + 5 = 10$$

$$ED = \frac{E}{T}$$

$$ED = \frac{10.5469}{10}$$

$$ED = 1.054 \text{ bits}$$

**Peti podatak** koji pruža Boltzmann kalkulator je tabela verovatnoća podudaranja između ulaza i izlaza. Ova tabela pokazuje, kroz `Boltzmann score`, verovatnoću da je određeni ulaz povezan sa datim izlazom. Uzimajući primer Whirlpool CoinJoin, tabela verovatnoća bi istakla šanse povezivanja između svakog ulaza i izlaza, pružajući kvantitativnu meru nejasnoće ili predvidljivosti asocijacija u transakciji:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Ovde je jasno da svaki ulaz ima jednake šanse da bude povezan sa bilo kojim izlazom, što pojačava nejasnoću i poverljivost transakcije. Međutim, u slučaju jednostavne transakcije sa jednim ulazom i dva izlaza, situacija je drugačija:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Ovde vidimo da je verovatnoća da svaki izlaz dolazi iz ulaza 0 100%. Niža verovatnoća se stoga prevodi u veću poverljivost, razblažujući direktne veze između ulaza i izlaza.


**Šesti deo informacija** koji je obezbeđen je broj determinističkih veza, dopunjen odnosom ovih veza. Ovaj indikator otkriva koliko je veza između ulaza i izlaza u analiziranoj transakciji neosporno, sa 100% verovatnoćom. Odnos, zauzvrat, nudi perspektivu o težini ovih determinističkih veza unutar ukupnih veza transakcije.


Na primer, transakcija tipa Whirlpool-CoinJoin ne prikazuje determinističke veze, i stoga pokazuje indikator i odnos od 0%. S druge strane, u našoj drugoj ispitanoj transakciji (sa jednim ulazom i dva izlaza), indikator je postavljen na 2, a odnos dostiže 100%. Dakle, nulti indikator signalizira odličnu poverljivost zahvaljujući odsustvu direktnih i neospornih veza između ulaza i izlaza.


**Kako pristupiti Boltzmann kalkulatoru na RoninDojo?**

Da biste pristupili alatu *Boltzmann Calculator*, idite na RoninCLI. Da biste to uradili, otvorite terminal na vašem ličnom računaru i uspostavite SSH vezu sa vašim čvorom koristeći sledeću komandu: `SSH ronindojo@[IP]`


Ako je, na primer, IP adresa vašeg čvora `192.168.1.40`, odgovarajuća komanda bi bila:

`SSH ronindojo@192.168.1.40`


Ako ste promenili svoje korisničko ime tokom koraka 6, zamenjujući podrazumevano korisničko ime (`ronindojo`) sa drugim, obavezno koristite ovo novo ime u komandi. Na primer, ako ste izabrali `planb` kao svoje korisničko ime i IP adresa je `192.168.1.40`, komanda koju treba uneti bi bila:

`SSH planb@192.168.1.40`


Bićete zamoljeni da unesete korisničku lozinku. Unesite je i zatim pritisnite `enter` da biste potvrdili. Zatim ćete pristupiti RoninCLI interfejsu. Koristite strelice na tastaturi da biste se pomerili do menija `Samourai Toolkit` i pritisnite `enter` da biste ga izabrali:


![Samourai Toolkit](assets/notext/43.webp)


Zatim izaberite `Boltzmann Calculator`:


![boltzmann](assets/notext/49.webp)


Stići ćete na početnu stranicu softvera:


![boltzmann home](assets/notext/51.webp)


Unesite txid transakcije koju želite proučiti i pritisnite taster `enter`:


![boltzmann txid](assets/notext/52.webp)


Kalkulator vam zatim pruža sve indikatore o kojima smo prethodno razgovarali:


![boltzmann result](assets/notext/53.webp)


### Ostale funkcije vašeg RoninDojo v2

Vaš RoninDojo čvor integriše razne druge funkcije. Konkretno, imate mogućnost skeniranja specifičnih informacija kako biste ih uzeli u obzir. Na primer, ponekad vaš Samourai novčanik, povezan sa RoninDojo, možda neće prikazivati bitkoine koje zapravo posedujete. Ako saldo pokazuje 0 dok ste sigurni da imate bitkoine u ovom novčaniku, nekoliko razloga može objasniti ovu situaciju, kao što je greška u putanjama derivacije. Ali jedan od uzroka može biti i to što vaš čvor ne prati pravilno vaše adrese. Da biste rešili ovaj problem, možete se uveriti da vaš čvor zaista prati vaš `xpub` koristeći _xpub alat_. Da biste pristupili ovom alatu putem RoninUI, pratite putanju:

`Maintenance > XPUB Tool`


Unesite `xpub` koji izaziva problem i kliknite na dugme `Check` da biste proverili ove informacije:

![xpub tool](assets/notext/54.webp)

Osigurajte da su sve transakcije pravilno navedene. Takođe je važno proveriti da li tip derivacije koji se koristi odgovara onom na vašem novčaniku. Ako to nije slučaj, kliknite na `Retype`, zatim izaberite između `BIP44`, `BIP49` ili `BIP84` prema vašim potrebama.

Pored ovog alata, kartica `Maintenance` u RoninUI je puna drugih korisnih funkcija:


- *Alat za transakcije*: Omogućava pregled detalja date transakcije;
- *Alat za adrese*: Omogućava potvrdu praćenja date adrese od strane vašeg Dojo-a;
- *Ponovno skeniraj blokove*: Prisiljava vaš čvor da izvrši novo skeniranje određenog raspona blokova.


Kartica `Push Tx` je još jedna zanimljiva funkcija RoninUI, koja omogućava emitovanje potpisane transakcije na Bitcoin mreži. Transakcija mora biti uneta u heksadecimalnom obliku.


Što se tiče ostalih kartica dostupnih na vašoj RoninUI kontrolnoj tabli:


- `Apps`: Hostuje Whirlpool aplikaciju i sigurno će se koristiti za integraciju novih aplikacija u budućnosti;
- `Logs`: Nudi pristup logvima događaja vašeg softvera u realnom vremenu;
- `System Info`: Pruža opšte informacije o vašem čvoru, kao što su temperatura CPU-a, iskorišćenost prostora za skladištenje ili podaci o RAM-u. Takođe ćete pronaći opcije `Reboot` i `Shut down` za ponovno pokretanje ili isključivanje vašeg čvora;
- `Settings`: Omogućava vam da promenite korisničku lozinku.


Eto! Hvala što ste pratili ovaj vodič do kraja. Ako vam se dopao, ohrabrujem vas da ga podelite na društvenim mrežama. Štaviše, ako imate priliku, razmislite o podršci programerima koji omogućavaju da ovaj besplatni i open-source softver bude dostupan našoj zajednici donacijom: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). Da biste produbili svoje znanje o RoninDojo i otkrili više resursa, toplo preporučujem da konsultujete linkove ka spoljnim resursima pomenutim u nastavku.


**Spoljni resursi:**


- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/introducing-boltzmann-85930984a159](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)

