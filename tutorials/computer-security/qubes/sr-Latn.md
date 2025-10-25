---
name: Qubes
description: Razumno siguran operativni sistem.
---

![cover](assets/cover.webp)



Qubes OS je besplatan, open-source operativni sistem dizajniran za korisnike koji bezbednost stavljaju na vrh svojih prioriteta. Njegova posebnost se zasniva na jednostavnoj, ali radikalnoj ideji: umesto da računar posmatra kao celinu, on njegovu upotrebu deli na nezavisne odeljke zvane **_qubes_**.



Svaki qube funkcioniše kao **izolovano virtuelno okruženje**, sa specifičnim nivoom poverenja i funkcijom. Tako da čak i ako je aplikacija kompromitovana, napad ostaje ograničen na taj qube bez uticaja na ostatak sistema.



> Ako ste ozbiljni po pitanju bezbednosti, Qubes OS je najbolji operativni sistem dostupan danas. - **Edward Snowden**.

Međutim, instalacija Qubes OS zahteva više pripreme nego instalacija konvencionalnog operativnog sistema. To podrazumeva proveru određenih hardverskih preduslova, razumevanje osnova virtualizacije i prihvatanje drugačijeg iskustva, gde se svaki svakodnevni zadatak posmatra u smislu separacije. Ali kada se postavi, Qubes OS nudi robustan okvir koji redefiniše način na koji svakodnevno komunicirate sa svojim računarom. U ovom vodiču, objasnićemo kako Qubes OS funkcioniše i kako ga lako instalirati na vaš sistem.



## Kako funkcioniše Qubes OS?



Qubes OS je zasnovan na principu kompartmenalizacije. Umesto korišćenja jednog sistema, oslanja se na **Xen** hipervizor za kreiranje izolovanih virtuelnih mašina, nazvanih qubes. Svaki qube je posvećen određenom zadatku ili nivou poverenja (posao, lično pretraživanje, bankarstvo, itd.). Ova separacija osigurava da bilo kakav kompromis u jednom qube-u ne može da se proširi na druge, delujući kao nekoliko nezavisnih računara unutar jedne mašine.



Korisnik Interface je upravljan centralnom, sigurnom domenom nazvanom **dom0**. Ova domena je potpuno izolovana od Interneta, što je čini srcem sistema. Iako prozore i menije prikazuje dom0, stvarno izvršavanje aplikacija odvija se u njihovim odgovarajućim kockama.



## Različite vrste kocki



Oko dom0 se okreću različite vrste qubes, od kojih svaka ima vrlo specifičnu ulogu.





- **AppVM** se koriste za pokretanje svakodnevnih aplikacija: korisnik tako može odvojiti svoje profesionalne e-mailove od pretraživanja interneta ili bankarskih aktivnosti, pri čemu svako okruženje ostaje potpuno nezavisno od drugih.





- Ove AppVM-ove su same po sebi zasnovane na **TemplateVM-ovima**, koji služe kao centralizovani šabloni za instalaciju i ažuriranje softvera, eliminišući potrebu za upravljanjem svakim kvebom zasebno.



Qubes OS takođe integriše virtuelne mašine specijalizovane za **sistemske usluge**.





- **NetVM** direktno upravlja **mrežnim uređajima** i osigurava vezu s Internetom. Često su povezani s **FirewallVMs**, koji intervenišu da **filtriraju saobraćaj** i ograniče izloženost drugih kocki.





- ServiceVMs igraju sličnu ulogu, na primer u upravljanju USB uređajima, uvek sa istom logikom: izolovati najrizičnije komponente kako bi se smanjila površina napada.



Konačno, za povremene ili rizične zadatke, Qubes OS nudi **DisposableVM**. Ove efemerne kocke se kreiraju u trenutku da **otvore sumnjiv dokument** ili **posete sumnjivu lokaciju**, a zatim potpuno nestaju kada se zatvore, brišući sve tragove i sprečavajući bilo kakav trajni napad.



### Mehanizam sigurnog kopiranja (qrexec)



Razmene između qubes-a zasnovane su na **qrexec-u**, sistemu za komunikaciju između VM-ova dizajniranom za bezbednost. Umesto da qubes-ima dozvoli slobodnu komunikaciju, qrexec nameće **specifične politike**: fajl kopiran iz jednog AppVM-a u drugi, ili tekst prenet putem clipboard-a, uvek prolazi kroz kanal koji sistem nadgleda i validira. Na ovaj način, čak i jednostavan čin kopiranja i lepljenja je kontrolisan kako bi se sprečilo širenje malvera.



### Upravljanje diskom



Qubes OS koristi genijalan sistem za upravljanje skladištem. TemplateVMs sadrže zajedničku softversku bazu, dok AppVMs dodaju samo svoje lične podatke i specifične fajlove. Ovo smanjuje upotrebu diskovnog prostora i olakšava globalna ažuriranja. DisposableVMs, s druge strane, koriste privremene volumene koji potpuno nestaju kada se zatvore. Ovaj model ne samo da garantuje veću sigurnost, već i efikasno upravljanje resursima.



## Zašto izabrati Qubes OS?



Prednosti Qubes OS leže pre svega u njegovom jedinstvenom bezbednosnom modelu. U središtu ovog pristupa je kompartamentalizacija, koja štiti korisnika izolovanjem svakog zadatka u zasebne virtuelne mašine. U praktičnom smislu, zaraženi e-mail ili zlonamerna veb stranica mogu ugroziti samo jedan qube, ostavljajući ostatak sistema i vaše lične podatke potpuno zaštićenim. Ova arhitektura značajno ograničava složene napade koji bi se na konvencionalnom sistemu mogli slobodno širiti.



Qubes OS takođe nudi potpunu transparentnost i kontrolu nad vašim digitalnim okruženjem. Tačno znate koji softver ima pristup kojem resursu, bilo da je to mreža, USB uređaj ili druge osetljive komponente. Sistem integriše napredne bezbednosne funkcije po defaultu, kao što je potpuna enkripcija diska, i olakšava korišćenje usluga za anonimizaciju kao što je Whonix operativni sistem.



https://planb.network/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Umesto da teži stvaranju neprobojnog sistema, Qubes OS se fokusira na otpornost: kapsulira štetu u slučaju kompromitovanja, smanjujući rizik za ostatak sistema. Ovaj pragmatični pristup čini Qubes OS preferiranim izborom za korisnike sa visokim bezbednosnim potrebama, ili koji žele da zadrže maksimalnu kontrolu nad svojim digitalnim životima.



## Instaliranje Qubes OS-a



Pre nego što instalirate Qubes OS, neophodno je da se uverite da vaš hardver ispunjava minimalne zahteve, jer sistem koristi virtualizaciju za izolaciju kjuobova. Glavne komponente koje treba proveriti su :




- **Procesor**: 64-bitni procesor kompatibilan sa hardverskom virtualizacijom (Intel VT-x ili AMD-V).
- RAM: minimum 8 GB je potrebno, ali preporučujemo RAM od 16 GB ili više za istovremeno pokretanje nekoliko qubes.
- **Prostor za skladištenje**: minimum 36 GB, idealno 128 GB na SSD-u za optimalne performanse.



Da biste instalirali Qubes OS, preuzmite zvaničnu ISO sliku sa [zvaničnog sajta](https://www.qubes-os.org/downloads/). Neophodno je proveriti integritet ISO-a koristeći GPG potpise koji su obezbeđeni, kako biste osigurali da fajl nije izmenjen i da je preuzimanje bezbedno.



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Kada se ISO verifikuje, potrebno je kreirati butabilni instalacioni medijum, obično USB stik. Da biste to uradili, preuzmite i instalirajte softver kao što je **Rufus** na Windows-u ili **Etcher** na Windows-u, Linux-u ili macOS-u. Ovi alati vam omogućavaju da kopirate ISO na USB stik tako da bude butabilan.



Pre nego što započnete instalaciju, potrebno je konfigurisati **BIOS ili UEFI** vašeg računara da **omogući virtualizaciju** i dozvoli pokretanje sa USB-a. U zavisnosti od modela vašeg računara, možda će biti potrebno **onemogućiti Secure Boot**, jer Qubes OS možda neće pokrenuti sa ovom opcijom omogućenom.



![0_02](assets/fr/02.webp)



Kada su ovi uslovi ispunjeni, restartujte računar i pristupite BIOS/UEFI tako što ćete odmah pritisnuti **Esc**, **Del**, **F9**, **F10**, **F11** ili **F12** (u zavisnosti od proizvođača). U meniju za pokretanje izaberite USB ključ kao uređaj za pokretanje kako biste pokrenuli instalaciju Qubes OS-a.



**Ekran za pokretanje**


Kada pokrećete sistem sa USB memorije, bićete direktno preusmereni na **GRUB** meni, gde možete izabrati radnju koju želite da izvršite. Koristeći strelice na tastaturi, izaberite "Install Qubes OS" i pritisnite "Enter".



![0_03](assets/fr/03.webp)



**Izbor jezika** :



Kada instalacija počne, prvi korak je da **izaberete jezik** i **regionalnu varijantu** koja odgovara vašoj konfiguraciji. Ovo osigurava da su sistem i opcije instalacije prikazane ispravno na vašem preferiranom jeziku.



![0_04](assets/fr/04.webp)



**Konfiguracija parametara** :



U ovoj fazi, potrebno je da konfigurišete broj Elements pre nego što pokrenete instalaciju na vašem računaru.



![0_05](assets/fr/05.webp)



**Raspored tastature** :



Kliknite na opciju **Keyboard**, zatim izaberite **odgovarajući raspored** za vaš računar. Kada napravite izbor, kliknite na **Terminated** da pređete na sledeći korak.



**Izbor destinacije** :



Odaberite opciju "Installation destination" da biste izabrali disk na koji želite da instalirate Qubes OS. Podrazumevano, particionisanje se odvija automatski, omogućavajući vam da uklonite sve podatke sa diska i instalirate sistem na njega. Međutim, možete izabrati **Customized** ili **Advanced Customization** da biste izvršili prilagođeno particionisanje. Zatim kliknite na "Done". Sistem će vas zamoliti da postavite **password**, koji deluje kao sigurnosni Layer za šifrovanje vaših podataka. Obavezno izaberite složenu i jedinstvenu lozinku.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Izaberite format datuma i vremena** :


Kliknite na opciju Vreme i datum, zatim izaberite vašu geografsku zonu. Takođe možete odabrati željeni format vremena: 24h ili 12h.



![0_08](assets/fr/08.webp)



**Kreiranje korisničkog naloga** :


Kliknite na **Create user** da biste kreirali svoj **prvi nalog**, koji će vam omogućiti prijavljivanje na Qubes OS.



![0_09](assets/fr/09.webp)



**Aktiviraj root nalog** :


Takođe možete **omogućiti root nalog** postavljanjem posebne lozinke za administraciju.



![0_10](assets/fr/10.webp)



Kada su ova podešavanja izvršena, kliknite na **Start installation** da biste započeli proces.



![0_11](assets/fr/11.webp)



Sačekajte **kraj instalacije**, zatim kliknite na **restartuj sistem** da biste završili instalaciju i pokrenuli Qubes OS.



![0_12](assets/fr/12.webp)



**Dodatna konfiguracija** :


Nakon ponovnog pokretanja, Qubes OS vas poziva da finalizirate **podrazumevane šablone i konfiguraciju qubes-a**. Unesite lozinku definisanu za šifrovanje diska.



![0_13](assets/fr/13.webp)



Zatim, počnite izborom **TemplateVM** koji želite da instalirate. Uobičajene opcije uključuju **Debian 12 Xfce**, **Fedora 41 Xfce** i **Whonix 17**, pri čemu se poslednji preporučuje za upotrebe koje zahtevaju **anonimnost i mrežnu sigurnost**. Takođe možete definisati **podrazumevani šablon**, koji će služiti kao osnova za kreiranje novih **AppVMs**.



![0_14](assets/fr/14.webp)



U odeljku **Main configuration** možete odabrati automatsko kreiranje osnovnih sistemskih kjuubova kao što su **sys-net**, **sys-firewall** i **default DisposableVM**. Preporučljivo je omogućiti opciju da **sys-firewall i sys-usb budu disposable**, kako biste ograničili izloženost uređaja i mreže u slučaju kompromitovanja. Takođe možete kreirati podrazumevane **AppVMs**, kao što su **personal**, **work**, **untrusted** i **vault**, kako biste organizovali svoje aktivnosti prema nivou poverenja.



![0_15](assets/fr/15.webp)



Qubes OS takođe vam omogućava da kreirate **kubu posvećenu USB uređajima** (sys-usb) i konfigurišete **Whonix Gateway i Workstation kube** kako biste osigurali svoje komunikacije putem Tor mreže. Za napredne korisnike, sekcija **Napredna konfiguracija** omogućava vam da kreirate **LVM thin pool** za efikasno upravljanje diskovnim prostorom između kuba.



Kada su sve ove opcije konfigurisane, kliknite na **Complete**, zatim na **Finish configuration**. Sačekajte dok sistem primenjuje ova podešavanja. Zatim će vam biti zatraženo da se **prijavite na svoj korisnički nalog**, i vaše Qubes OS okruženje će biti spremno za korišćenje, sigurno i pravilno izolovano za vaše različite aktivnosti.



![0_17](assets/fr/17.webp)



Vaš operativni sistem je sada instaliran i spreman za korišćenje.



![0_18](assets/fr/18.webp)



## Kreiraj qube na svom sistemu



Da biste kreirali qube, proces se upravlja pomoću alata **Qube Manager**, dostupnog iz Start menija. U prozoru alata, jednostavno kliknite na ikonu **Create qube** da biste otvorili novi prozor za konfiguraciju. Prvo, unesite ime za vaš qube, kao što je "perso-web" ili "work", kako biste identifikovali njegovu upotrebu.



Zatim ćete odabrati njegov **Tip**, obično **AppVM** za rutinske zadatke, ili **DisposableVM** za privremenu upotrebu. Ključno je odabrati **Template** na kojem će vaš qube biti baziran, kao što su "fedora-39" ili "debian-12", jer će to obezbediti operativni sistem i softver. Takođe ćete odrediti **NetVM**, što je qube odgovoran za pristup Internetu, podrazumevano **sys-firewall**.



Konačno, nakon podešavanja veličine skladišta i RAM-a ako je potrebno, jednostavnim klikom na **OK** pokrenuće se proces kreiranja. Kada je proces završen, vaš novi qube će biti vidljiv na listi i spreman za korišćenje.



U zaključku, Qubes OS nije običan operativni sistem, već vrhunsko sigurnosno rešenje koje preispituje arhitekturu ličnog računara. Njegov pristup, zasnovan na kompartmenalizaciji i izolaciji putem virtualizacije, nudi neprevaziđenu zaštitu protiv najsloženijih pretnji. Segmentiranjem radnog okruženja u specijalizovane kocke za svaki zadatak, osigurava da se malver ne može proširiti i ugroziti ceo sistem.



Bilo da treba da surfujete internetom bezbedno, zaštitite osetljive informacije ili radite sa različitim nivoima poverenja, Qubes OS pruža otpornu, transparentnu strukturu. Usvajanjem dobrih praksi i potpunim korišćenjem njegovih funkcija, imaćete **digitalnu tvrđavu** prilagođenu modernim pretnjama. Saznajte više o zaštiti vaših podataka i privatnosti.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1