---
name: Dođo
description: Otvoreni Bitcoin čvor za privatnost i autonomiju
---

![cover](assets/cover.webp)



*Ovaj vodič je zasnovan na [zvaničnoj Ashigaru dokumentaciji](https://ashigaru.rs/docs/), koju sam preuzeo i proširio. Prepisao sam sve delove radi poboljšanja jasnoće, dodao dodatna detaljna objašnjenja, kao i ilustracije za početnike, kako bi instalacija i korišćenje bili lakši za razumevanje.*



---

Dojo je program otvorenog koda dizajniran da deluje kao backend server za određene privatno orijentisane Bitcoin novčanike, zasnovane na Bitcoin core čvoru. Istorijski gledano, razvijen je da radi sa Samourai Wallet, mobilnim Wallet koji je nudio napredne funkcije privatnosti kao što su Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym... Samourai Wallet je sada ugašen nakon hapšenja njegovih programera, ali njegov naslednik iz zajednice, **Ashigaru Wallet**, je preuzeo i nastavlja da se oslanja na Dojo kako bi ponudio kompletno iskustvo za korisnike koji žele da zadrže kontrolu nad svojim podacima prilikom korišćenja Bitcoin.



![Image](assets/fr/01.webp)



U praktičnom smislu, Dojo deluje kao prolaz između vašeg Wallet i Bitcoin mreže. Bez Dojo-a, lagani mobilni Wallet bi morao da upitava servere trećih strana kako bi dobio status vaših UTXO-a i vašu istoriju, ili da emituje vaše transakcije. Ovo podrazumeva zavisnost i curenje osetljivih podataka ka serveru treće strane (korišćene adrese, iznosi, učestalost plaćanja, itd.). Sa Dojo-om, vi sami hostujete ovaj server, direktno povezan sa vašim sopstvenim Bitcoin čvorom. Na ovaj način, svi zahtevi vašeg portfolija prolaze kroz infrastrukturu koju vi kontrolišete, bez posrednika, jačajući vašu poverljivost i suverenitet.



## Zahtevi za postavljanje Dojo-a



Postavljanje Dojo servera ne zahteva ultra-moćan računar. Svako sa osnovnim računarom, stabilnom internet vezom i mogućnošću da ga ostavi uključenog neprekidno (24/7) može postaviti funkcionalan Dojo.



### Izaberite tip mašine



Možete koristiti :




- laptop ;
- desktop računar ;
- mini-PC (npr. Intel NUC, Lenovo Thincentre Tiny...).



Svaka opcija ima svoje prednosti i nedostatke:




- Cena: obnovljeni mini-PC ili desktop često će biti jeftiniji od novog laptopa.
- Otisak: mini-PC zauzima manje prostora.
- Power Supply: laptop ima prednost baterije, što znači da se neće isključiti u slučaju nestanka struje, za razliku od mini-PC-ja.
- Mogućnost nadogradnje: barbones obično omogućavaju dodavanje memorije ili lako zamenu Hard diska.



Za više informacija o odabiru vaše opreme, preporučujem da pohađate ovaj kurs:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Preporučena oprema



Nema potrebe da kupujete novu mašinu. Refurbished računar sa specifikacijama ispod će pružiti mnogo bolje performanse od jednokanalne elektronike (kao što je Raspberry Pi).



**Minimalne specifikacije:**




- X86-64 arhitektura (64-bitni procesor).
- Dvojezgarni procesor od 2 GHz ili brži.
- 8 GB RAM minimum.
- 2 TB ili više NVMe SSD (za skladištenje Blockchain ili Bitcoin i potrebnih indeksa).



**Preporučeni operativni sistem: **




- Distribucija zasnovana na Debianu, kao što je Ubuntu 24.04 LTS.



**Preporučena oprema:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- itd.



Savršeno je moguće pokrenuti Dojo server na drugim hardverskim konfiguracijama. Međutim, da biste postigli najbolji učinak i ograničili probleme, savetujemo vam da pratite gore navedene preporuke.



U ovom vodiču, koristiću stari ThinkCentre Tiny sa Intel Pentium Dual-Core G4400T procesorom, 8 GB RAM i 2 TB SSD.



## 1 - Instaliranje Ubuntu-a



*Ako želite da instalirate Dojo na uređaj koji je već konfigurisan, možete preskočiti ovaj korak i preći direktno na korak 2.*



Nakon što ste pripremili odabrani hardver, vreme je da instalirate operativni sistem. Možete koristiti gotovo bilo koju Debian distribuciju, ali preporučujem da se odlučite za LTS verziju Ubuntu-a, jer je savršeno prilagođena našim potrebama. Evo koraka koje treba pratiti:



### 1.1. kreirajte USB ključ za pokretanje



Sa već funkcionalnog računara (vaša uobičajena mašina), preuzmite Ubuntu LTS ISO sliku [sa zvaničnog sajta](https://ubuntu.com/download/desktop) (`24.04` u trenutku pisanja, ali uzmite najnoviju ako je dostupna).



![Image](assets/fr/02.webp)



Umetnite USB ključ od najmanje 8 GB u ovaj računar, zatim kreirajte bootabilni ključ koristeći softver kao što je [Balena Etcher](https://etcher.balena.io/). Izaberite Ubuntu ISO sliku koju ste upravo preuzeli, odaberite USB ključ kao ciljni uređaj, zatim pokrenite proces kreiranja (budite strpljivi, može potrajati nekoliko minuta).



![Image](assets/fr/03.webp)



Ubacite USB ključ sa mogućnošću pokretanja u isključen računar (onaj na kojem želite pokrenuti Dojo). Pokrenite mašinu i odmah pritisnite **F12** ili **F10** na tastaturi (u zavisnosti od modela) da biste pristupili meniju za pokretanje. Zatim izaberite vaš USB ključ kao prioritetni uređaj u redosledu pokretanja računara.



![Image](assets/fr/04.webp)



### 1.2. instaliraj operativni sistem



Na ekranu se pojavljuje početni ekran Ubuntu-a. Izaberite "Try or Install Ubuntu*".



![Image](assets/fr/05.webp)



Zatim pratite klasičan proces instalacije Ubuntua:




- Izaberite jezik.
- Izaberite tip tastature.
- Ako ste povezani putem RJ45 kabla, nema potrebe za konfigurisanjem Wi-Fi-ja.
- Kliknite na "*Install Ubuntu*" i označite opciju za instalaciju softvera treće strane (Wi-Fi drajveri, multimedijalni kodeci, itd.).
- Kada čarobnjak zatraži vrstu instalacije, izaberite "*Erase disk and install Ubuntu*". **Upozorenje**: ova operacija će potpuno obrisati sadržaj diska. Pažljivo proverite da li disk koji ste izabrali odgovara NVMe SSD-u namenjenom za Dojo.
- Kreirajte jednostavno korisničko ime (npr. "*loic*").
- Dodelite ime mašini (npr. "*dojo-node*").
- Postavite jaku lozinku i čuvajte je na sigurnom.
- Omogući opciju "*Zatraži moju lozinku za prijavu*" da pojačaš sigurnost.
- Naznačite svoju vremensku zonu, zatim kliknite na "*Install*".
- Sačekajte da se instalacija završi. Kada se završi, sistem će se automatski restartovati.
- Uklonite USB instalacioni ključ prilikom ponovnog pokretanja računara.



Za više detalja o procesu instalacije Ubuntu-a, pogledajte naš posvećeni vodič :



https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. ažuriranje sistema



Nakon prvog pokretanja, otvorite terminal koristeći kombinaciju tastera ***Ctrl + Alt + T*** i pokrenite sledeće komande za ažuriranje sistema:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Instalacija pomoćne zgrade



Da bi Dojo pravilno radio, određene softverske komponente moraju biti prisutne na vašem sistemu. One se koriste za upravljanje softverskim repozitorijumima, komunikaciju, dekompresiju arhiva i izvršavanje Dojo-a unutar Docker kontejnera. Sve ove operacije se izvode u terminalu.



### 2.1. Priprema



Sledeća komanda vas vraća u vaš lični folder. Ovo je dobra praksa pre pokretanja serije instalacija.



```bash
cd ~/
```



Pre nego što instalirate bilo koji softver, uverite se da je baza podataka dostupnog softvera na vašem računaru ažurirana. Ovo sprečava instaliranje zastarelih verzija.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. instaliraj uslužne programe



Nekoliko alata treba dodati u sistem:




- `apt-transport-https`: omogućava vam da preuzimate pakete sigurno putem HTTPS-a
- `ca-certificates`: upravlja sertifikatima potrebnim za šifrovane veze
- `curl`: za preuzimanje datoteka s interneta
- `gnupg-agent`: za upravljanje GPG ključevima
- software-properties-common`: pruža alate za manipulaciju APT repozitorijumima
- `unzip`: otvara datoteke u ZIP formatu



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Tokom instalacije, sistem može tražiti vašu potvrdu. Pritisnite taster "*y*", zatim pritisnite "*Enter*".



![Image](assets/fr/08.webp)



### 2.3. instaliraj Torsocks



Torsocks omogućava izvršavanje određenih komandi putem Tor mreže, poboljšavajući poverljivost komunikacija.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. instaliraj Docker i Docker Compose



Dojo radi unutar Docker kontejnera. To znači da je svaka usluga izolovana u nezavisnom okruženju, što pojednostavljuje održavanje i bezbednost. Da biste to uradili, potrebno je da instalirate Docker i alat Docker Compose, koji vam omogućava upravljanje sa nekoliko kontejnera istovremeno.



#### Dodajte Docker potpisni ključ



Docker obezbeđuje sopstveni ključ za digitalni potpis. Dodavanje ključa verifikuje autentičnost preuzetih paketa.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Službeni Docker repozitorijum dodat



Zatim, treba da kažete sistemu gde da pronađe zvanične Docker pakete. Ova komanda dodaje novi repozitorijum u konfiguraciju vašeg menadžera paketa.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Instaliranje Dockera i Docker Compose



Glavne Docker komponente sada mogu biti instalirane.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Autorizacija korisnika



Podrazumevano, samo komande izvršene sa administratorskim pravima mogu pokrenuti Docker. Radi veće pogodnosti, preporučujem dodavanje vašeg trenutnog korisnika u grupu "*docker*". Ovo vam omogućava da koristite Docker bez potrebe da svaki put kucate `sudo`.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Kreiranje jednog korisnika (opciono)



Ako želite poboljšati sigurnost vašeg sistema, preporučujem da kreirate zasebnog korisnika isključivo za pokretanje Dojo-a. Ovo razdvajanje ograničava rizike: ako dođe do sigurnosnog problema u Dojo-u, to neće direktno ugroziti vaš glavni nalog.



### 3.1. kreiranje korisničkog naloga



Sledeća komanda kreira novog korisnika po imenu "*dojo*". Ovaj korisnik će imati početni direktorijum `/home/dojo` i pristup bash terminalu. Takođe će biti dodat u sudo grupu kako bi omogućio izvršavanje administratorskih komandi.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Postavljanje lozinke



Važno je dodeliti jaku lozinku ovom nalogu. Idealno bi bilo da koristite menadžer lozinki kao što je Bitwarden za generate dugu, Hard-za-pogađanje kombinaciju.



```bash
sudo passwd dojo
```



Sistem će vas zatim zamoliti da unesete izabranu lozinku, a zatim je potvrdite po drugi put.



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Autorizuj korisnika da koristi Docker



Da bi se korisniku "*dojo*" omogućilo pokretanje kontejnera potrebnih za rad Dojo-a, mora biti dodat u Docker grupu. Ovo izbegava potrebu da se svaki komanda prethodi sa `sudo`.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Ponovno pokretanje sistema



Da bi promene u grupi stupile na snagu, mašina mora biti restartovana.



```bash
sudo reboot
```



### 3.5. Prijava sa novim korisnikom



Kada se sistem ponovo pokrene, prijavite se sa ***dojo*** nalogom i lozinkom koju ste ranije definisali. Svi naredni koraci moraju se izvršiti sa ovog posvećenog naloga.



## 4. Preuzmi i proveri Dojo



Pre nego što instalirate Dojo, neophodno je da se uverite da su fajlovi došli od zvaničnog developera i da nisu modifikovani. Ovaj korak se oslanja na korišćenje PGP-a i heševa za verifikaciju autentičnosti i integriteta fajlova.



### 4.1. uvezite PGP ključ programera



Preuzmite javni ključ programera putem Tor-a i uvezite ga u svoj lokalni ključni lanac. Ovaj ključ će se koristiti za verifikaciju potpisa povezanih sa Dojo datotekama.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. preuzmi najnoviju verziju Dojo



Preuzmite komprimovanu arhivu koja sadrži Dojo izvorni kod. U ovom primeru, najnovija verzija je `1.27.0`: modifikujte komandu u skladu sa [najnovijom verzijom ovde na zvaničnom GitHub repozitorijumu](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Preuzmi otiske prstiju i potpis



Programeri objavljuju datoteku koja sadrži digitalne otiske arhiva, kao i datoteku potpisanu njihovim PGP ključem. Preuzmite ih kako biste lokalno uporedili vaše datoteke.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Proveri PGP potpis



Proverite da je datoteka otiska prsta potpisana uvezenim ključem.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Tačan rezultat prikazuje važeći potpis sa ključem `E53AD419B242822F19E23C6D3033D463D6E544F6` i povezanim Address `dojocoder@pm.me`. Može se pojaviti upozorenje da ključ nije sertifikovan: možete ga ignorisati.



Ako je, s druge strane, potpis nevažeći, odmah zaustavite proces instalacije i počnite ponovo od početka.



![Image](assets/fr/17.webp)



### 4.5. Proveri integritet arhive



Izračunajte SHA256 otisak preuzetog fajla, zatim otvorite fajl sa otiskom da uporedite dve vrednosti.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Ako su dva otiska prsta identična, možete biti sigurni da arhiva nije modifikovana. Ako su različiti, nemojte dalje i obrišite fajlove.



![Image](assets/fr/18.webp)



### 4.6. Ekstraktuj i organizuj fajlove



Kada je verifikacija uspešno završena, možete raspakovati arhivu i pripremiti folder posvećen instalaciji Dojo-a.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Očistite nepotrebne fajlove



Izbrišite privremene datoteke i arhive koje više nisu potrebne kako biste održali čistoću vašeg okruženja.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Konfiguracija dođoa



Dojo je serverska aplikacija koja objedinjuje nekoliko usluga za interakciju sa vašim portfoliom i upravljanje vašim Bitcoin čvorom. Njegova konfiguracija može biti složena, ali projekat nudi pojednostavljeni metod koji automatski instalira i konfiguriše sledeće komponente:




- Dojo (main API)
- Bitcoin core (kompletan Bitcoin čvor)
- BTC-RPC Explorer (web Block explorer)
- Fulcrum Indekser (brzo indeksiranje blokova i transakcija)
- Fulcrum Electrum Server dostupan na Tor mreži
- Fulcrum Electrum Server dostupan na lokalnoj mreži
- Administratorski akreditivi



### 5.1. administratorski akreditivi



Da biste osigurali pristup raznim uslugama, potrebno je generate nekoliko jedinstvenih identifikatora:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_PASSWORD`
- mYSQL_USER
- `MYSQL_PASSWORD`
- nODE_API_KEY`
- `NODE_ADMIN_KEY`
- `NODE_JWT_SECRET`



Ovi identifikatori **moraju biti jedinstveni** (ovo je veoma važno: ne smete koristiti istu lozinku za više usluga), sastavljeni isključivo od brojeva, velikih i malih slova (alfanumerički), i treba da budu dugi oko 40 karaktera kako bi se garantovao visok nivo sigurnosti. Još jednom, toplo preporučujem korišćenje menadžera lozinki.



### 5.2. Pristupite konfiguracionim fajlovima



Datoteke konfiguracije Dojo nalaze se u fascikli `conf/`. Pređite u ovaj direktorijum:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Bitcoin core konfiguracija



Otvorite konfiguracionu datoteku Bitcoin core pomoću nano uređivača teksta:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



U ovu datoteku unesite generisane identifikatore:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Zamenite `your-ID-here` i `your-password-here` sa vašim sopstvenim prijavama (sa jakom lozinkom).***



Takođe možete prilagoditi veličinu keš memorije koju koristi Bitcoin core kako biste poboljšali performanse (možete koristiti i više ako imate puno dostupnog RAM-a):



```
BITCOIND_DB_CACHE=2048
```



Da biste sačuvali izmene i zatvorili uređivač :




- pritisnite `Ctrl + X
- ukucaj `y`
- zatim pritisnite "*Enter*"



### 5.4. MySQL konfiguracija



Zatim otvorite konfiguraciju MySQL baze podataka:



```bash
nano docker-mysql.conf.tpl
```



Molimo unesite svoje podatke za prijavu:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Zamenite `your-ID-here` i `your-password-here` sa vašim sopstvenim podacima za prijavu (sa jakim, jedinstvenim lozinkama).***



Sačuvaj na isti način (`Ctrl + X`, `y`, "*Enter*").



![Image](assets/fr/23.webp)



### 5.5. Konfiguracija Fulcrum indeksatora



Otvorite sledeću datoteku:



```bash
nano docker-indexer.conf.tpl
```



Dodajte parametre za aktivaciju Fulcrum-a i pravilno ga integrišite u Dojo:



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Dalje, postoje 2 mogućnosti, u zavisnosti od vaše konfiguracije. Ako je Dojo instaliran na mašini koja je odvojena od vašeg svakodnevnog računara (na posebnoj mašini, serveru...), unesite njegov IP Address u vašu lokalnu mrežu, na primer :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Da biste saznali lokalni IP Address vaše mašine, otvorite drugi terminal i unesite sledeću komandu:



```bash
hostname -I
```



Druga mogućnost: ako se Dojo pokreće direktno na vašem svakodnevnom ličnom računaru, zadržite podrazumevanu vrednost koja je već prisutna u konfiguracionoj datoteci :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Sačuvaj i izađi iz uređivača (`Ctrl + X`, `y`, "*Enter*").



### 5.6. Konfiguracija usluge čvora



Konačno, otvorite konfiguraciju glavne Dojo usluge:



```bash
nano docker-node.conf.tpl
```



Molimo unesite svoje podatke za prijavu:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Zamenite `your-password-here` sa vašim sopstvenim akreditivima (sa jakim, jedinstvenim lozinkama).***



![Image](assets/fr/26.webp)



Zatim aktivirajte lokalni indeksator:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Sačuvaj i izađi iz uređivača (`Ctrl + X`, `y`, "*Enter*").



### 5.7. Upravljanje prijavama



Kada je konfiguracija završena, nije neophodno sačuvati sve generisane identifikatore. Jedini koji apsolutno mora biti sačuvan je :



```
NODE_ADMIN_KEY
```



Ova prijava će vam omogućiti da se kasnije prijavite u alat za održavanje Dojo-a. Sve druge prijave mogu biti uklonjene iz vašeg menadžera lozinki ili ručno pisanih beleški. One ostaju dostupne iz Dojo konfiguracionih fajlova ukoliko ih budete trebali u budućnosti.



## 6. Instalacija Dojo-a



U ovoj fazi, Dojo će biti instaliran i pokrenut na vašem računaru. Operacija će pokrenuti nekoliko servisa (Bitcoin core, Fulcrum indeksator, Dojo backend, itd.) i inicirati punu sinhronizaciju Blockchain Bitcoin. Ovo može potrajati nekoliko dana, u zavisnosti od vašeg hardvera i internet konekcije.



### 6.1. Proverite da Docker radi ispravno



Pre nego što započnete instalaciju, uverite se da je Docker operativan. Pokrenite sledeću komandu:



```bash
docker run hello-world
```



Ova komanda preuzima i pokreće mali testni kontejner. Ako sve funkcioniše ispravno, trebalo bi da vidite poruku sličnu:



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Ako se ova poruka ne prikazuje, počnite ponovnim pokretanjem vašeg računara sa:



```bash
sudo reboot
```



Zatim se ponovo prijavite na svoj **dojo** nalog i ponovo pokrenite test komandu. Ako greška i dalje postoji, Docker nije pravilno instaliran. U tom slučaju, vratite se na korak `2.4.` o instalaciji Dockera i pažljivo proverite svaku komandu.



### 6.2. Idite u direktorijum za instalaciju Dojo-a



Skripte potrebne za instalaciju nalaze se u fascikli `my-dojo`. Pređite u ovaj direktorijum:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Koristite komandu `ls` da proverite da li je prisutan fajl `dojo.sh`. Ovo je glavni skript koji automatizuje instalaciju Dojo-a i pokretanje svih njegovih servisa.



![Image](assets/fr/29.webp)



### 6.3. Pokreni instalaciju



Pokrenite instalaciju pokretanjem :



```bash
./dojo.sh install
```



Potvrdite instalaciju pritiskom na `y` i zatim "*Enter*".



![Image](assets/fr/30.webp)



Ovaj skript će :




- preuzmite i pokrenite potrebne Docker kontejnere,
- inicijalizuj Bitcoin core i započni sinhronizaciju Blockchain,
- pokreni Fulcrum indeksator da prati transakcije i adrese,
- aktiviraj Dojo backend i njegove API-je.



Videćete stalan tok logova koji se pomeraju, sa šarenim referencama kao što su `bitcoind`, `soroban`, `nodejs` ili `fulcrum`. Ovo pomeranje ukazuje da je Dojo pokrenut i da počinje sa izvršavanjem različitih servisa.



![Image](assets/fr/31.webp)



### 6.4. Prikaz izlaznog dnevnika



Logovi se pojavljuju u realnom vremenu u vašem terminalu. Da biste se vratili na komandnu liniju dok Dojo radi u pozadini, otkucajte :



```
Ctrl + C
```



Ne brini: zaustavljanje prikaza logova ne zaustavlja servise. Docker nastavlja da pokreće Dojo u pozadini (očigledno ne treba da zaustaviš računar ako želiš da IBD nastavi).



### 6.5. Razumevanje *Initial Block Download* (IBD)



Na pokretanju, Bitcoin core mora preuzeti i verifikovati ceo Blockchain od 2009. Ovaj korak se zove ***Initial Block Download* (IBD)**. To je neophodno, jer omogućava vašem Dojo čvoru da nezavisno verifikuje svaki Bitcoin blok i transakciju.



Trajanje ove sinhronizacije zavisi od nekoliko faktora:




- snaga vašeg procesora i količina dostupne RAM memorije,
- brzina vašeg diska,
- broj i kvalitet vršnjaka na koje se vaš čvor povezuje,
- brzina vaše Internet veze.



U praksi, ova operacija obično traje između **2 i 7 dana**. Tokom ovog perioda, možete ostaviti vašu mašinu da radi neprekidno. Što duže mašina radi, brže će se sinhronizacija završiti. Savetujem vam da redovno proveravate status sinhronizacije konsultujući Bitcoin core logove, ili koristeći Dojo alat za održavanje nakon instalacije (pogledajte sledeći odeljak).



Da biste produbili svoje znanje o IBD-u i, generalno, o radu i ulozi vašeg Bitcoin čvora, preporučujem da pogledate ovaj kurs:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Praćenje sinhronizacije



Kada prvi put instalirate Dojo, potrebno je da sačekate da se dve glavne operacije u potpunosti završe: kompletno preuzimanje Blockchain Bitcoin (*IBD*) i indeksiranje ovog Blockchain od strane Fulcrum-a. U zavisnosti od vaše konekcije i snage mašine, ovo može potrajati nekoliko dana. Tokom ovog vremena, možete pratiti napredak procesa kako biste bili sigurni da sve teče glatko.



Postoje dva načina za praćenje statusa sinhronizacije:




- korišćenje alata za održavanje Dojo (ili DMT), koji je jednostavan, ali pruža malo detalja tokom IBD;
- direktna konsultacija Dojo logova na vašem računaru, tehnički zahtevnija ali mnogo preciznija.



### 7.1. Proveri putem Dojo Maintenance Tool (DMT)



Alat za održavanje Dojo je siguran, web-baziran Interface koji vam omogućava da pratite status vaše fabrike i izvršavate određene operacije. To je najlakši i najpristupačniji način za praćenje napretka IBD-a. Tokom početne faze sinhronizacije, prikazane informacije mogu biti ograničene. Na primer, DMT ne prikazuje detaljan napredak Fulcrum indeksiranja. S druge strane, kada je sinhronizacija završena, DMT će jasno prikazati :




- sva svetla na Green;
- poslednji validirani blok za svaku uslugu (Node, Indexer, Dojo DB).



Da biste mu pristupili, potrebno je da znate URL vašeg DMT-a i da se povežete sa njim [preko Tor pretraživača](https://www.torproject.org/download/). Da biste to uradili, otvorite terminal i idite u direktorijum `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Zatim pokrenite sledeću komandu:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Tada ćete imati pristup svim informacijama koje se odnose na povezivanje sa vašim Dojo putem Tor-a. URL koji nas ovde zanima je sledeći:



```
Dojo API and Maintenance Tool =
```



Da biste pristupili DMT sa bilo kog uređaja na bilo kojoj mreži (čak i daljinski), otvorite Tor Browser i unesite ovaj URL praćen sa `/admin`. Na primer, ako je vaš URL `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, potrebno je da unesete u traku [Tor Browser](https://www.torproject.org/download/):



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Molimo vas da ovaj Address zadržite strogo poverljivo**



Bićete preusmereni na stranicu za autentifikaciju. DMT se prijavljuje koristeći lozinku `NODE_ADMIN_KEY` koju ste ranije generisali.



![Image](assets/fr/33.webp)



Jednom kada se prijavite, možete pristupiti *Dojo Maintenance Tool*! Tokom IBD, možete videti informacije o "*Latest Block*" u meniju "*Full node*", što vam omogućava da saznate trenutni status vašeg Bitcoin čvora.



![Image](assets/fr/34.webp)



Zapamti da obeležiš ovaj Address u Tor Browser-u za lakše pronalaženje kasnije.



Kada je vaš Dojo potpuno sinhronizovan, trebalo bi da vidite Green oznaku ✅ na svim indikatorima na DMT početnoj stranici.



### 7.2. Verifikacija putem Dojo logova



Drugi način praćenja napretka vašeg IBD-a je direktno konsultovanje logova mašine. Ovaj pristup nudi mnogo preciznije, praćenje u realnom vremenu. Možete videti kako Bitcoin core napreduje u preuzimanju blokova i kako ih Fulcrum indeksira.



Povežite se sa mašinom na kojoj se nalazi vaš Dojo i otvorite terminal. Sve komande treba izvršiti iz direktorijuma `my-dojo`. Pozicionirajte se u ovom folderu:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Bitcoin core dnevnici



Pregledajte dnevnike Bitcoin core da biste pratili napredak IBD-a:



```bash
./dojo.sh logs bitcoind
```



Na početku, videćete fazu pred-sinhronizacije zaglavlja blokova:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Kada ova cifra dostigne 100%, Bitcoin core će započeti kompletno preuzimanje Blockchain. Videćete napredak IBD-a. Da biste saznali trenutnu visinu bloka, pogledajte vrednost označenu sa `height=`. Takođe možete pratiti ključ `progress=`, koji pokazuje procenat napretka IBD-a.



![Image](assets/fr/36.webp)



Kao i uvek, da biste zatvorili logove i vratili se na komandnu liniju, koristite kombinaciju `Ctrl + C`.



#### Fulcrum dnevnici



Jednom kada Bitcoin core završi predsinhronizaciju zaglavlja, Fulcrum počinje indeksiranje Blockchain kako napreduje. Pogledajte njegove dnevnike sa :



```bash
./dojo.sh logs fulcrum
```



Videćete visinu poslednjeg indeksiranog bloka, naznačenu posle `height:`, kao i procenat napretka indeksiranja.



![Image](assets/fr/37.webp)



### 7.3. Korupcija baze podataka Fulcrum



Fulcrum je posebno moćan indeksator, ali njegova instalacija može biti složena, ne samo zbog delikatnog upravljanja bazom podataka. U slučaju nestanka struje ili naglog gašenja mašine tokom početne sinhronizacije, baza podataka indeksatora može biti oštećena. To možete videti, na primer, ako imate sledeće logove:



```bash
fulcrum | The database has been corrupted etc...
```



**Napomena:** Ova vrsta greške bi trebala biti ispravljena sa nadolazećim izdanjem Fulcrum 2.0.



Ako vam se ovo dogodi, nema uticaja na bitcoind (vaš Bitcoin čvor): njegov IBD će nastaviti da napreduje nezavisno od Fulcruma. Međutim, nećete moći da koristite Fulcrum dok ne obrišete njegove oštećene podatke i ponovo pokrenete sinhronizaciju od početka. Evo kako to funkcioniše:



Stop Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Izbriši samo Fulcrum kontejner i volumen:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Obično je ime `my-dojo_data-fulcrum`, ako to nije slučaj kod vas, prilagodite ime koje je vraćeno prethodnom komandom.



Zatim ponovo pokrenite Dojo i izgradite Fulcrum iz početka:



```bash
./dojo.sh upgrade
```



Zatim možete proveriti da Fulcrum ispravno radi konsultovanjem logova:



```bash
docker logs -f fulcrum
```




## 8. Korišćenje alata za održavanje Dojo-a



Kada je vaš Bitcoin čvor sinhronizovan sa warp glavom sa najviše Proof of Work, i Blockchain je 100% indeksiran od strane Fulcrum-a, možete početi koristiti vaš Dojo.



Vaš Dojo nudi širok spektar funkcija, koje se redovno unapređuju sa svakom novom verzijom. Po mom mišljenju, 2 najvažnije su :




- mogućnost povezivanja vašeg Ashigaru Wallet za korišćenje sopstvenog čvora za konsultovanje Blockchain podataka i emitovanje vaših transakcija,
- i Block explorer, koji vam omogućava pristup informacijama o Blockchain Bitcoin bez izlaganja vaših podataka eksternoj instanci koju ne kontrolišete.



Hajde da saznamo kako ih koristiti.


### 8.1. Povežite Ashigaru sa svojim Dojoom



Povezivanje vašeg Ashigaru Wallet sa vašim Dojo-om je veoma jednostavno: kada ste na vašem DMT-u, otvorite meni "*Pairing*". Pojaviće se QR kod, koji možete direktno skenirati pomoću Ashigaru aplikacije.



![Image](assets/fr/38.webp)



U aplikaciji Ashigaru, prvi put kada je pokrenete nakon kreiranja ili vraćanja vašeg Wallet, bićete preusmereni na stranicu "*Konfiguriši svoj Dojo server*". Pritisnite "*Skeniraj QR*", zatim skenirajte QR kod prikazan na vašem DMT.



![Image](assets/fr/39.webp)



Zatim kliknite na dugme "*Continue*".



![Image](assets/fr/40.webp)



Sada ste povezani sa svojim Dojo-om.



![Image](assets/fr/41.webp)



### 8.2. Korišćenje Block explorer



Dojo automatski instalira Block explorer, [BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer), koji direktno koristi podatke sa vašeg sopstvenog Bitcoin čvora. Explorer vam omogućava pristup sirovim informacijama sa Blockchain i vašeg Mempool kroz lako razumljiv Interface web. Tako možete, na primer, proveriti status transakcije na čekanju, videti stanje Address ili lako ispitati sastav bloka.



Da biste mu pristupili, jednostavno preuzmite Tor Address iz svog pregledača. Da biste to učinili, pokrenite istu komandu koju ste koristili za dobijanje Address vašeg DMT:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Imaćete pristup svim informacijama o vašoj Dojo vezi putem Tor-a. URL koji nas ovde zanima je sledeći:



```
Block Explorer =
```



Ako ste već povezani sa svojim DMT-om, možete pronaći ovaj Address u meniju "*Pairing*", unutar JSON-a za povezivanje:



![Image](assets/fr/43.webp)



Da biste pristupili svom pregledaču sa bilo kog računara na bilo kojoj mreži (čak i daljinski), otvorite [Tor Browser](https://www.torproject.org/download/) i unesite URL koji ste upravo dobili.



⚠️ **Molimo vas da ovaj Address zadržite strogo poverljivim



Tada ćete imati pristup svom Block explorer.



![Image](assets/fr/44.webp)



*Image credit: https://ashigaru.rs/.*



Da biste pratili transakciju, jednostavno unesite njen txid u traku za pretragu u gornjem desnom uglu.



![Image](assets/fr/45.webp)



*Image credit: https://ashigaru.rs/.*



Da biste proverili kretanja povezana sa Address, postupite na isti način unosom Address u traku za pretragu.



![Image](assets/fr/46.webp)



*Image credit: https://ashigaru.rs/.*



Takođe možete uneti Hash ili visinu bloka u traku za pretragu da biste prikazali detalje.



![Image](assets/fr/47.webp)



*Image credit: https://ashigaru.rs/.*



## 9. Održavanje dođoa



### 9.1 Zaustavi svoj Dojo



Nikada nemojte naglo isključiti napajanje vašem Dojo-u, jer to može oštetiti određene baze podataka, posebno Fulcrum indeksator. Ako ipak morate da ga isključite, uvek prvo izvršite čisto gašenje Dojo-a, a zatim, kada su svi postupci završeni, isključite i mašinu:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Ažurirajte svoj Dojo



Dojo se redovno razvija i nove verzije se objavljuju kako bi se ispravile greške, poboljšala stabilnost i dodale nove funkcije. Stoga je važno [redovno proveravati ažuriranja](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) i ažurirati vaš Dojo. Proces je sličan početnoj instalaciji, ali zahteva zamenu određenih fajlova sa najnovijom dostupnom verzijom, uz zadržavanje vaše konfiguracije. Ovde su detaljni koraci koje treba pratiti za čisto i sigurno ažuriranje:



Da biste saznali trenutnu verziju vašeg Dojo-a, pokrenite komandu :



```bash
./dojo.sh version
```



Iako je ovaj korak opcionalan, preporučujem da počnete ažuriranjem vašeg OS-a. Ovo smanjuje rizik od nekompatibilnosti i osigurava da su zavisnosti koje koristi Dojo ažurirane:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Idite u Dojo direktorijum i zaustavite trenutne servise:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Zatim ponovo pokrenite svoj sistem da biste dobili čistu početnu tačku:



```bash
sudo reboot
```



Dojo dolazi sa digitalno potpisanim fajlovima. Ovi PGP potpisi osiguravaju da fajlovi potiču od programera i da nisu izmenjeni na bilo koji način. Važno je proveriti ih svaki put kada ažurirate Dojo, baš kao što ste to uradili kada ste ga prvi put instalirali. Počnite preuzimanjem javnog ključa programera putem Tor-a, zatim ga uvezite :



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Vratite se u svoj lični direktorijum:



```bash
cd ~/
```



Preuzmite najnoviju verziju Dojo sa GitHub-a putem Tor-a. U ovom primeru, to je verzija `1.28.0` (koja još ne postoji u trenutku pisanja: ovo je samo primer). Zapamtite da zamenite datoteku i link [sa verzijom koju želite da instalirate](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Takođe preuzmite datoteku koja sadrži PGP otiske prstiju i potpis (ponovo, zapamtite da prilagodite verziju u komandi):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Proverite da je preuzeta datoteka otiska prsta potpisana ključem programera:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Tačan rezultat treba da prikaže :



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Može se pojaviti upozorenje da ključ nije sertifikovan, ali to nije važno. S druge strane, ako je potpis nevažeći ili odgovara drugom ključu, nemojte nastavljati dalje i počnite ispočetka, proveravajući linkove.



Zatim izračunajte SHA256 otisak arhive i uporedite ga sa zvaničnim fajlom otiska:



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Ako se dva otiska prstiju savršeno podudaraju, arhiva je originalna i netaknuta. Ako se razlikuju, odmah obrišite fajlove i nemojte nastaviti.



Raspakujte arhivu u vašem home direktorijumu:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Zatim kopirajte sadržaj u Dojo direktorijum, prepisujući stari :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Ova operacija čuva vaše konfiguracione fajlove locirane u `~/dojo-app/docker/my-dojo/conf`, ali zamenjuje sve ostale fajlove sa ažuriranim verzijama.



Da biste održali svoju okolinu čistom, obrišite nepotrebne fajlove :



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Vratite se u direktorijum skripti Dojo i pokrenite komandu za ažuriranje:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Ova komanda upućuje Docker da ponovo izgradi slike sa novim fajlovima, a zatim automatski restartuje sve servise. Na kraju procesa, proverite logove kako biste se uverili da Bitcoin core, Fulcrum i Dojo rade ispravno:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Ako se usluge pokrenu bez greške i dnevnici prikazuju da se blokovi obrađuju, vaš Dojo je sada ažuriran i operativan.