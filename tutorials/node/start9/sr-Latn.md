---
name: Start9

description: Uputstvo za postavljanje privatnog servera Start9

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Evo video tutorijala od Southern Bitcoiner-a, video vodič koji vam pokazuje kako da postavite i koristite Start9 / StartOS lični server, i kako da pokrenete bitcoin čvor.*


## 1️⃣ Uvod


### Šta je tačno Start9?


Start9 je kompanija osnovana 2020. godine, najpoznatija po razvoju [**StartOS-a,**](https://github.com/Start9Labs/start-os) operativnog sistema zasnovanog na Linuxu, dizajniranog za lične servere. Omogućava korisnicima lako samostalno hostovanje širokog spektra softverskih usluga—kao što su Bitcoin i Lightning čvorovi, aplikacije za razmenu poruka ili menadžeri lozinki, uz zadržavanje potpune kontrole nad svojim podacima i eliminisanje oslanjanja na centralizovane tehnološke platforme. StartOS sadrži korisnički prijatan interfejs zasnovan na pregledaču, kuriranu Tržnicu za instaliranje usluga i ugrađene alate za privatnost kao što su Tor integracija i sistemska HTTPS enkripcija. Start9 takođe pruža hardverske uređaje sa unapred instaliranim OS-om, iako se softver može instalirati na kompatibilan hardver ili virtuelne mašine (VM-ove).


### Koje opcije su dostupne?


Start9 nudi opcije za unapred izgrađene i DIY implementacije. [**Server One**](https://store.start9.com/collections/servers/products/server-one) i [**Server Pure**](https://store.start9.com/collections/servers/products/server-pure) su zvanični hardverski uređaji sa komponentama visokih performansi: Server One koristi procesor **AMD Ryzen 7 5825U** sa konfigurisanim RAM-om (16GB–64GB) i skladištem (2TB–4TB NVMe SSD), dok je Server Pure opremljen sa **Intel i7-10710U**, takođe nudi opcije za konfigurisanje RAM-a i skladišta. Obe opcije uključuju **doživotnu tehničku podršku** kada se kupe direktno od Start9. Za korisnike koji preferiraju fleksibilnost, StartOS se može besplatno instalirati na širok spektar postojećeg hardvera, uključujući laptopove, desktop računare, mini PC-jeve i računare sa jednim pločama, ili unutar VM-ova.


![image](assets/en/01.webp)


### Koje su razlike u odnosu na Umbrel?


StartOS i Umbrel pojednostavljuju instalaciju usluga koje sami hostujete, ali se razlikuju po arhitekturi i funkcijama. Umbrel funkcioniše kao aplikacioni sloj na Debian/Ubuntu sistemima ili VM-ovima, dok je Start9 posvećen operativni sistem koji zahteva direktnu instalaciju na hardver ili VM. Umbrel ima uglađen, macOS-inspirisan interfejs, dok Start9 daje prioritet funkcionalnom, minimalnom dizajnu. Umbrel nudi veći [izbor aplikacija](https://apps.umbrel.com/), dok [Start9 Marketplace](https://marketplace.start9.com/) nadoknađuje naprednim tehničkim mogućnostima. Start9 pojednostavljuje pristup naprednim podešavanjima putem validiranih UI formi, smanjujući potrebu za interakcijom sa komandnom linijom. Takođe se ističe u upravljanju bekapovima sa jednim klikom za enkriptovane sistemske bekapove, što je funkcija koju Umbrel nema nativno. StartOS pruža ugrađene alate za nadgledanje i primenjuje HTTPS enkripciju za pristup lokalnoj mreži, poboljšavajući sigurnost. Umbrel koristi neenkriptovani HTTP lokalno, iako obe platforme podržavaju siguran daljinski pristup putem Tor-a. Umbrel je pogodan za korisnike koji daju prioritet bogatom ekosistemu aplikacija i uglađenom UI. Start9 je snažan izbor za one koji cene sigurnost, mogućnost konfiguracije, pouzdanost bekapa i napredno upravljanje uslugama bez potrebe za ekspertizom u komandnoj liniji. Da biste saznali više o Umbrel-u i razlikama u odnosu na Start9, posetite ovaj kurs:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ DIY Prerequisites: Minimum & Recommended Specs


Za osnovnu upotrebu sa minimalnim uslugama, **minimalne specifikacije** su: **1 vCPU jezgro (2.0GHz+ boost), 4GB RAM, 64GB skladište**, i Ethernet port. Ipak, preporučujem da idete daleko iznad toga, posebno ako pokrećete Bitcoin Node. Lično, počeo sam sa 1TB i brzo ostao bez prostora. Bolje ciljati na **najmanje 2TB skladišta**, zajedno sa **četvorojezgarnim CPU-om (2.5GHz+)** i **8GB+ RAM-a**. To čini ogromnu razliku u performansama i dugovečnosti. Ako želite da se dublje upustite, ovde je aktuelna zajednička tema o [Hardveru sposobnom za pokretanje StartOS-a](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Preuzimanje i Flashovanje Firmware-a


Da biste započeli postavljanje, koristite poseban računar da posetite [Start9 website](https://start9.com/), i idite na odeljak sa dokumentacijom klikom na `DOCS`. Odatle pristupite `Flashing Guides` da pronađete odgovarajuću verziju StartOS-a. Dostupne su dve opcije:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Ovaj vodič pokriva opciju `x86/ARM`.


Najnovija verzija OS-a može se preuzeti sa [Github stranice za izdanje](https://github.com/Start9Labs/start-os/releases/latest). Verzije [Pre-release](https://github.com/Start9Labs/start-os/releases) su takođe dostupne za korisnike koji žele da testiraju nove funkcije. Na dnu stranice, pod `Assets`, preuzmite `x86_64` ili `x86_64-nonfree.iso`. Slika `x86_64-nonfree.iso` sadrži ne-slobodan (zatvorenog koda) softver potreban za Server One i većinu DIY hardvera, posebno za podršku grafičkih i mrežnih uređaja.


Preporučuje se verifikacija integriteta fajla proverom njegovog SHA256 heša u poređenju sa onim navedenim na GitHub-u. Za Linux, može se koristiti komanda `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso`, dok su drugi operativni sistemi pokriveni u dokumentaciji.


Nakon preuzimanja i verifikacije StartOS slike, potrebno je da se ona prebaci na USB drajv. `BalenaEtcher` je preporučeni softver za ovaj zadatak. To je besplatan, open-source alat za pisanje OS slika na USB drajvove i SD kartice, dostupan za Windows, macOS i Linux. Preuzmite odgovarajuću verziju sa zvanične [Balena Etcher veb stranice](https://www.balena.io/etcher/) i pokrenite instalacioni program. Povežite ciljni USB drajv ili SD karticu, otvorite Balena Etcher i kliknite na `Flash from file` da biste izabrali preuzetu OS sliku. Etcher će automatski detektovati povezane drajvove; izaberite tačan cilj ako je prisutno više njih. Kliknite na `Flash!` da biste započeli pisanje slike. Etcher automatski validira proces pisanja po završetku. Kada se završi, bezbedno uklonite drajv i koristite ga za pokretanje uređaja.


![image](assets/en/19.webp)


## 4️⃣ Inicijalno podešavanje


Za početno podešavanje, pogledajte Start9 [dokumentaciju](https://docs.start9.com/0.3.5.x/) stranicu pod `USER MANUAL` zatim `Getting Started - Initial Setup`. Ovaj zvanični vodič treba konsultovati za najnovije informacije.


Predstavljene su dve opcije:



- Počni iznova
- Opcije oporavka


Za novu instalaciju servera, izaberite `Start Fresh`. Prvo, povežite server na napajanje i Ethernet kabl. Osigurajte da je računar korišćen za podešavanje na istoj lokalnoj mreži. Izvadite novoflešovani USB drajv iz računara i ubacite ga u server.


Možete kontrolisati server na daljinu sa bilo kog računara na istoj mreži. Otvorite veb pregledač i idite na `http://start.local`.


**Napomena**: Ako dođe do problema sa povezivanjem na ovu adresu, često je uzrok neuspeh kućnih mreža da razreše `.local` imena domena. Problem se može rešiti direktnim pristupom serveru putem njegove IP adrese. IP se može pronaći prijavljivanjem u administratorski interfejs rutera (obično na `192.168.1.1` ili sličnoj adresi), i pronalaženjem uređaja na listi DHCP klijenata ili mapi mreže. Zatim, unesite punu IP adresu (npr. `http://192.168.1.105`) u pregledač. Ovo zaobilazi DNS razrešavanje. Ako problemi i dalje postoje, pogledajte [stranicu sa uobičajenim problemima](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) ili [kontaktirajte njihovu podršku.](https://start9.com/contact/)


Na ekranu bi trebalo da se pojavi StartOS podešavanje. Kliknite na `Start Fresh` da započnete podešavanje novog servera.


![image](assets/en/03.webp)


Sledeći korak je da izaberete skladišni disk na kojem će StartOS podaci biti pohranjeni.


![image](assets/en/04.webp)


Postavite jaku `Password` za server. Zabeležite je kako je savetovao Start9, zatim kliknite na `FINISH`.


![image](assets/en/05.webp)


Ekran će pokazati da se StartOS inicijalizuje i postavlja server. Sledeći korak je `Download address info` jer je adresa `start.local` samo za potrebe postavljanja i neće raditi nakon toga.


![image](assets/en/06.webp)


Datoteka konfiguracije sadrži dve kritične adrese za pristup: jednu za `lokalnu mrežu (LAN)` i drugu za siguran pristup putem `Tor`. Obe adrese treba sačuvati u sigurnom menadžeru lozinki. Sledeći korak je da `Verujete svom Root CA`. Otvorite novu karticu u pregledaču i pratite uputstva da biste verovali Root CA i prijavili se. Root CA sertifikat se takođe može preuzeti klikom na `Preuzmi sertifikat` u preuzetoj datoteci.


## 5️⃣ Verujte svom Root CA


Nakon preuzimanja sertifikata, serverov `Root CA` mora biti pouzdan od strane operativnog sistema. Kliknite na `View Instructions` i pronađite smernice za određeni OS.


![image](assets/en/07.webp)


Za Linux sistem koriste se sledeće komande. Prvo, otvorite Terminal i instalirajte potrebne pakete:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Idite do direktorijuma gde je sertifikat preuzet, obično `~/Downloads`. Izvršite ove komande da dodate sertifikat u skladište poverenja operativnog sistema. Pređite u folder za preuzimanja sa `cd ~/Downloads`. Kreirajte potreban direktorijum sa `sudo mkdir -p /usr/share/ca-certificates/start9`. Kopirajte fajl sertifikata, zamenjujući `your-filename.crt` stvarnim imenom fajla, koristeći `sudo cp "your-filename.crt" /usr/share/ca-certificates/start9/`. Registrujte sertifikat trajno dodavanjem njegove putanje u sistemsku konfiguraciju sa `sudo bash -c "echo 'start9/your-filename.crt' >> /etc/ca-certificates.conf"`. Na kraju, obnovite skladište poverenja sa `sudo update-ca-certificates`. Ključno je koristiti stvarno ime fajla sertifikata i proveriti sve putanje pre izvršavanja ovih komandi. Ovaj proces uspostavlja trajno poverenje za HTTPS konekcije Start9 servera.


Uspešna instalacija biće naznačena izlazom koji kaže `1 added`. Većina aplikacija će tada moći da se poveže sigurno putem `https`. Ako koristite Firefox, potreban je dodatni [završni korak](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff). Za Chrome ili Brave, potreban je drugačiji [završni korak](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome) kako bi se konfigurisao pregledač da poštuje Root CA. Testirajte vezu osvežavanjem stranice. Ako problem i dalje postoji, zatvorite i ponovo otvorite pregledač pre nego što ponovo posetite stranicu.


![image](assets/en/08.webp)


## 6️⃣ Početak sa StartOS-om


Sada bi trebalo da bude moguće prijaviti se koristeći sigurnu HTTPS vezu. Unesite `Password` za pristup `Welcome Screen`.


![image](assets/en/09.webp)


Ovaj ekran pruža korisne prečice za početak. Leva bočna traka sadrži glavne stavke menija za navigaciju.


## 7️⃣ Sistem


Kartica Sistemi u StartOS-u omogućava pristup osnovnim funkcijama sistema za upravljanje ličnim serverom. Nudi alate za održavanje sistema, sigurnost, dijagnostiku i konfiguraciju bez potrebe za poznavanjem komandne linije.


Deo `Backups` omogućava kreiranje potpunih rezervnih kopija sistema, uključujući usluge, konfiguracije i podatke, koje se kasnije mogu vratiti. Ovo je neophodno za oporavak od katastrofa ili migraciju na novi hardver. Rezervne kopije mogu se čuvati na eksternim diskovima i šifrovane su pomoću glavne lozinke.


Odeljak `Manage` u kartici Systems omogućava kontrolu nad ključnim funkcijama sistema. Korisnici mogu ručno proveriti i primeniti StartOS ažuriranja, održavajući kontrolu nad procesom ažuriranja sistema. Moguće je instalirati prilagođene ili usluge trećih strana koje nisu dostupne na zvaničnom tržištu. Ako server nije povezan putem Ethernet-a, Wi-Fi postavke se mogu konfigurisati iz ovog odeljka. Napredni korisnici mogu omogućiti SSH pristup za upravljanje sistemom na nivou terminala.


![image](assets/en/10.webp)


Odeljak `Insights` pruža praćenje performansi i zdravlja servera u realnom vremenu, prikazujući korišćenje CPU-a, RAM-a i diska putem grafika. Takođe prikazuje temperaturu sistema, što je korisno za uređaje poput Raspberry Pi koji nemaju aktivno hlađenje. Metrički podaci o vremenu rada i prosečnom opterećenju pomažu u proceni stabilnosti sistema, a dostupni su i živi logovi za rešavanje problema sa servisom ili sistemom.


Odeljak `Support` nudi pristup ugrađenim FAQ-ovima, zvaničnoj dokumentaciji i kanalima podrške zajednice. Dnevnici za otklanjanje grešaka mogu se preuzeti iz ovog odeljka kako bi se podelili sa Start9 podrškom za brže rešavanje problema.


![image](assets/en/11.webp)


## 8️⃣ Marketplace


`Marketplace` se koristi za otkrivanje, instalaciju i upravljanje uslugama na ličnom serveru. Omogućava pristup softveru kao što su Bitcoin Core, BTCPay Server i electrs. StartOS podržava više marketa, uključujući zvanični Start9 Registry i registre koje vodi zajednica. Ovi se mogu dodati klikom na `CHANGE` i prebacivanjem na `Community Registry`, što omogućava pristup širem spektru usluga.


![image](assets/en/12.webp)


## 9️⃣ Instaliranje Bitcoin Full Node-a


Instaliranje Bitcoin full node na StartOS pruža punu suverenost nad Bitcoin iskustvom. Omogućava validaciju transakcija i poboljšava privatnost i sigurnost uklanjanjem oslanjanja na spoljne usluge koje mogu beležiti aktivnosti. Dobija se potpuna kontrola nad transakcijama, omogućavajući njihovo direktno emitovanje na mrežu. Podrazumevana opcija je `Bitcoin Core`, koja se nativno integriše sa StartOS-om i omogućava povezivanje sa novčanicima kao što su Specter, Sparrow, ili Electrum za postavku samostalnog čuvanja. Alternativa, `Bitcoin Knots`, je takođe dostupna putem Community Registry.


Da biste instalirali Bitcoin Core, idite na Marketplace. Pod podrazumevanim registrom, pronađite i instalirajte Bitcoin Core uslugu. Nakon instalacije, pojaviće se `Needs Config` prompt, koji zahteva da se podešavanja završe pre nego što usluga može da radi. Ovo se obično dešava nakon ažuriranja ili svežih instalacija i zahteva pregled `RPC settings`. Nastavite sa podrazumevanom konfiguracijom i kliknite na `Save`.


![image](assets/en/13.webp)


Kada se potpuno sinhronizuje, vaš čvor može služiti kao privatni backend za novčanike poput Sparrow, pružajući poboljšanu privatnost i validaciju transakcija. Međutim, za korisnike koji čuvaju značajne iznose, ključno je razumeti sigurnosne kompromise ove direktne veze. Kada se wallet direktno poveže sa Bitcoin Core, može izložiti osetljive podatke, jer Bitcoin Core čuva javne ključeve (xpubs) i wallet bilanse nešifrovane na host mašini. Kompromitovani sistem mogao bi omogućiti napadaču da otkrije vaša sredstva i cilja vas.


Da biste ublažili ovaj rizik i postigli robusniji sigurnosni model, možete postaviti privatni Electrum Server. Ovaj server deluje kao posrednik, indeksirajući blokčejn bez skladištenja bilo kakvih informacija specifičnih za wallet. Povezivanjem vašeg wallet sa sopstvenim Electrum serverom umesto direktno sa Bitcoin Core, sprečavate wallet da pristupi osetljivim podacima čvora.


![image](assets/en/14.webp)


## 🔟 Postavite electrs


`electrs` (Electrum Rust Server) je brz, efikasan indeksator koji se povezuje na vaš Bitcoin Core čvor i omogućava novčanicima kompatibilnim sa Electrum da u realnom vremenu pretražuju istoriju transakcija i stanja. Pokretanjem electrs na StartOS-u, eliminišete oslanjanje na treće strane Electrum servere, značajno poboljšavajući privatnost i sigurnost—vaši wallet upiti idu direktno na vaš samostalno hostovani čvor.


Da biste ga postavili, prvo instalirajte electrs servis iz StartOS Marketplace-a. Sistem će zahtevati da Bitcoin Core bude potpuno sinhronizovan pre nego što nastavite. Nakon instalacije, potvrdite `Needs Config` postavke sa preporučenim podrazumevanim vrednostima i electrs počinje indeksiranje blockchain-a, što može potrajati do jednog dana u zavisnosti od vašeg hardvera.


![image](assets/en/15.webp)


Kada završite, možete povezati novčanike kao što su Sparrow ili Specter. Uspešna veza omogućava vašem wallet da se sinhronizuje direktno sa vašim čvorom, pružajući sigurno, privatno i samostalno hostovano Bitcoin iskustvo.


## 1️⃣1️⃣ Poveži Sparrow Wallet


Da biste povezali `Sparrow Wallet` sa vašim StartOS čvorom koristeći electrs implementaciju, prvo se uverite da je Bitcoin Core potpuno sinhronizovan i da je electrs instaliran i pokrenut. Otvorite Sparrow Wallet na vašem uređaju i idite na `File` -> `Settings` -> `Server`. Zatim izaberite `Private Electrum Server`. U polje za URL unesite `Tor hostname` i `Port` za electrs, koje možete pronaći u StartOS pod `Services` -> `electrs` -> `Properties` (obično se završava sa `.onion:50001`).


![image](assets/en/16.webp)


Zatim omogućite Tor potvrđivanjem opcije `Use Proxy`, postavljanjem adrese proxy-a na `127.0.0.1` i porta na `9050`. Kliknite na `Test Connection` i sačekajte nekoliko trenutaka. Uspešna konekcija će prikazati poruku potvrde kao što je `Connected to electrs`. Kada se verifikuje, zatvorite podešavanja i nastavite sa kreiranjem ili obnavljanjem vašeg wallet. Ova konfiguracija osigurava da vaš wallet upite šalje vašem sopstvenom čvoru putem electrs-a, pružajući potpunu privatnost i rad bez poverenja.


![image](assets/en/17.webp)


## 🎯 Zaključak


StartOS by Start9 je platforma prilagođena korisnicima, fokusirana na privatnost, dizajnirana za samostalno hostovanje esencijalnih servisa kao što su Bitcoin i Lightning čvorovi, novčanici i lične aplikacije. Eliminira potrebu za veštinama rada u komandnoj liniji nudeći čist grafički interfejs, automatske bekape, praćenje zdravlja i siguran pristup preko Tor-a, što ga čini idealnim za netehničke korisnike. Njegova modularna arhitektura podržava besprekornu integraciju sa alatima kao što su electrs ili Sparrow, dajući vam potpunu kontrolu nad vašim finansijskim i digitalnim suverenitetom. Sa snažnim fokusom na transparentnost, lokalnu kontrolu i proširivost, StartOS osnažuje korisnike da povrate vlasništvo od centralizovanih platformi i pokrenu sopstvenu privatnu, otpornu infrastrukturu.