---
name: OPNsense
description: Kako da instaliram i konfigurišem OPNsense firewall?
---
![cover](assets/cover.webp)



___



*Ovaj vodič je zasnovan na originalnom sadržaju autora Florian BURNEL objavljenom na [IT-Connect](https://www.it-connect.fr/). Licenca [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Moguće je da su napravljene izmene u originalnom tekstu.*



___



## I. Prezentacija



U ovom vodiču ćemo pogledati OPNsense open source firewall. Pogledaćemo njegove glavne karakteristike, preduslove i kako instalirati ovo rešenje zasnovano na FreeBSD.



Pre nego što počnete, trebalo bi da znate da su **OPNsense i pfSense oba open source firewall-ovi** zasnovani na FreeBSD-u. Možemo reći da je pfSense na neki način stariji brat OPNsense-a, jer je potonji Fork kreiran 2015. godine. Na kraju, važno je napomenuti da je od 2017. godine, **OPNsense prešao na HardenedBSD umesto FreeBSD-a**. HardenedBSD je unapređena verzija FreeBSD-a, sa naprednim bezbednosnim funkcijama.



OPNsense se ističe po svom modernijem korisničkom Interface i **češćem ritmu ažuriranja**. Zaista, raspored ažuriranja OPNsense uključuje dva glavna izdanja godišnje, koja se ažuriraju otprilike svake dve nedelje (što rezultira manjim izdanjima). Ova praksa je veoma zanimljiva u poređenju sa pfSense, ako pogledamo zajedničke verzije ovih rešenja.



![Image](assets/fr/050.webp)



## II. OPNsense features



OPNsense je operativni sistem dizajniran da deluje kao firewall i ruter, iako su njegove funkcije brojne i mogu se proširiti instaliranjem dodatnih paketa. Pogodan za proizvodnu upotrebu, uglavnom se koristi za mrežnu sigurnost i upravljanje protokom.



### A. Glavne karakteristike



Evo su neke od ključnih karakteristika OPNsense-a:





- Firewall i NAT**: OPNsense pruža naprednu funkcionalnost stateful firewall-a sa stateful filtriranjem, kao i mogućnosti prevođenja mreže Address (NAT).





- DNS/DHCP**: OPNsense može biti konfigurisan da upravlja DNS i DHCP uslugama na mreži. Može delovati kao DHCP server, ali se takođe može koristiti kao DNS resolver za uređaje na lokalnoj mreži. Dnsmasq je takođe integrisan po defaultu.





- VPN**: OPNsense podržava nekoliko VPN protokola, uključujući IPsec, OpenVPN i WireGuard, omogućavajući sigurne veze za daljinski pristup mobilnim radnim stanicama ili međusobno povezivanje lokacija.





- Web proxy**: OPNsense uključuje web proxy za kontrolu i filtriranje pristupa Internetu. Takođe se može koristiti za filtriranje sadržaja i upravljanje pristupom mreži.





- Upravljanje propusnim opsegom (QoS)**: OPNsense nudi funkcije upravljanja kvalitetom usluge (QoS) za prioritizaciju mrežnog saobraćaja i bolje upravljanje mrežnim propusnim opsegom.





- Captive portal**: ova funkcija vam omogućava upravljanje korisničkim pristupom mreži putem stranice za autentifikaciju (lokalna baza, vaučeri, itd.). To je funkcija koja se često koristi za javne Wi-Fi mreže.





- IDS/IPS**: OPNsense integriše Suricata kako bi ponudio funkcije detekcije i prevencije upada (IDS/IPS) za zaštitu mreže od napada.





- Visoka dostupnost (CARP)**: OPNsense podržava CARP (*Common Address Redundancy Protocol*) za visoku dostupnost između više OPNsense firewall-ova, osiguravajući da usluga ostane aktivna čak i u slučaju kvara hardvera.





- Izveštavanje i nadgledanje**: OPNsense pruža alate za izveštavanje i nadgledanje u realnom vremenu kako bi se pratila performansa mreže (sa NetFlow) i otkrili potencijalni problemi, zahvaljujući kreiranju logova. Ovo uključuje grafike. Monit alat je integrisan u OPNsense i omogućava nadzor samog firewall-a.



### B. Dodatni paketi



Ovo je samo pregled funkcija koje nudi OPNsense. Pored toga, **katalog paketa** dostupan iz OPNsense administracije Interface omogućava vam da **obogatite firewall dodatnim funkcionalnostima**. To uključuje ACME klijent, Wazuh agent, NTP Chrony servis i Caddy kao obrnuti proxy.



![Image](assets/fr/051.webp)



## III. OPNsense preduslovi



Prvo, morate odlučiti gde ćete instalirati OPNsense. Postoji nekoliko mogućih rešenja, uključujući instalaciju na:





- Hiper-računar kao virtuelna mašina, bilo da je to Hyper-V, Proxmox, VMware ESXi, itd.
- Mašina kao *bare-metal* sistem. Ovo bi mogao biti mini PC koji deluje kao firewall.



Takođe možete kupiti **OPNsense uređaj za montažu u rack** putem naše online prodavnice.



Morate uzeti u obzir hardverske resurse potrebne za pokretanje OPNsense-a. Ovo je detaljno opisano na [ovoj stranici dokumentacije](https://docs.opnsense.org/manual/hardware.html).



**Minimalni i preporučeni resursi za proizvodnju:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Konačno, **vaši zahtevi za resursima zavise pre svega od broja veza koje treba upravljati**, a samim tim i od **vaših zahteva za propusnim opsegom**. Pored toga, potrebno je **imati na umu usluge koje će biti aktivirane i korišćene** (proxy, detekcija upada, itd...) jer mogu biti zahtevne za CPU i/ili RAM.



Trebaće vam i OPNsense instalaciona ISO slika, koju možete preuzeti sa [zvaničnog sajta](https://opnsense.org/download/). Za instalaciju na VM, izaberite opciju "**dvd**" kao tip slike da biste dobili ISO sliku (i uradite šta želite sa njom...). Za instalaciju putem USB ključa za pokretanje, izaberite opciju "**vga**" da biste dobili "**.img**" fajl.



![Image](assets/fr/048.webp)



Trebaće vam i računar za administraciju i testiranje OPNsense.



## IV. Konfiguracija cilja



Naš cilj je da





- Kreirajte internu virtuelnu mrežu (192.168.10.0/24 - LAN)**, koja može pristupiti Internetu preko OPNsense firewall-a. Za proizvodnu upotrebu, ovo može biti vaša lokalna mreža, kablovska i/ili Wi-Fi.
- Aktivirajte i konfigurišite NAT** tako da VM-ovi u internom virtuelnom mrežnom okruženju mogu pristupiti Internetu
- Aktivirajte i konfigurišite DHCP server na OPNsense** da distribuira IP konfiguraciju budućim mašinama povezanim na internu virtuelnu mrežu.
- Konfigurišite firewall** da dozvoli samo odlazne LAN ka WAN tokove u HTTP (80) i HTTPS (443).
- Konfigurišite firewall** da dozvoli virtuelnom LAN-u korišćenje OPNsense kao DNS resolver (53).



Ako koristite Hyper-V platformu, ovo će vam dati sledeću reprezentaciju:



![Image](assets/fr/033.webp)



## V. Instaliranje OPNsense firewall-a



### A. Priprema USB ključa za pokretanje



Prvi korak je priprema instalacionog medija: **bootabilni USB ključ sa OPNsense**. Ovo je naravno opcionalno ako radite u virtuelnom okruženju, ali u svakom slučaju morate preuzeti OPNsense instalacionu ISO sliku.



Nakon preuzimanja, dobijate **arhivu koja sadrži sliku u ".img"** formatu. Možete **napraviti USB stik za pokretanje** pomoću raznih aplikacija, uključujući **balenaEtcher**: izuzetno jednostavan za korišćenje. Štaviše, aplikacija će prepoznati sliku u arhivi, tako da je ne morate prethodno dekompresovati.





- [Preuzmi balenaEtcher](https://etcher.balena.io/)



Kada je aplikacija instalirana, izaberite svoju sliku, svoj USB ključ i zatim kliknite na "Flash! Sačekajte trenutak.



![Image](assets/fr/049.webp)



Sada ste spremni za instalaciju.



### B. Instaliranje OPNsense sistema



Pokrenite mašinu na kojoj je OPNsense. Trebalo bi da vidite stranicu dobrodošlice sličnu onoj ispod. Na nekoliko sekundi, ekran prikazan će biti vidljiv u prozoru. Pustite da proces teče svojim tokom...



![Image](assets/fr/019.webp)



OPNsense slika je učitana na mašinu, tako da se sistem može pristupiti u "**live**" režimu, tj. privremeno smešten u memoriju.



![Image](assets/fr/025.webp)



Zatim ćete doći do Interface sličnog onom ispod. Prijavite se sa prijavom "**installer**" i lozinkom "**opnsense**". Imajte na umu da je tastatura trenutno **QWERTY**. U ovom trenutku, **započećemo proces instalacije OPNsense-a**.



![Image](assets/fr/026.webp)



Na ekranu se pojavljuje novi čarobnjak. Prvi korak je da izaberete raspored tastature koji odgovara vašoj konfiguraciji. Za AZERTY tastaturu, izaberite opciju "**French (accent keys)**" sa liste, zatim dvaput kliknite**.



![Image](assets/fr/027.webp)



Drugi korak je odabir zadatka koji će se izvršiti. Ovde ćemo izvršiti instalaciju koristeći **ZFS datotečni sistem**. Postavite se na liniju "**Install (ZFS)**" i potvrdite sa **Enter**.



![Image](assets/fr/028.webp)



U trećem koraku, izaberite "**stripe**" jer je naša mašina opremljena sa **samo jednim diskom**: nije moguće obezbediti redundanciju za zaštitu skladišta firewall-a i njegovih podataka. Ovo je posebno važno prilikom instalacije na fizičku mašinu kako bi se zaštitilo od hardverskog kvara diska, putem RAID principa.



![Image](assets/fr/029.webp)



U četvrtom koraku, jednostavno pritisnite **Enter** da potvrdite.



![Image](assets/fr/030.webp)



Konačno, potvrdite odabirom "**YES**" i zatim pritisnite taster **Enter**.



![Image](assets/fr/031.webp)



Sada ćete morati da sačekate dok se OPNsense instalira... Ovaj proces traje oko 5 minuta.



![Image](assets/fr/032.webp)



Kada je instalacija završena, možemo promeniti lozinku za "**root**" pre ponovnog pokretanja. Izaberite "**Root Password**", pritisnite **Enter** i unesite lozinku "**root**" dva puta.



![Image](assets/fr/020.webp)



Konačno, izaberite "**Complete Install**" i pritisnite **Enter**. Iskoristite ovu priliku da **izbacite disk iz DVD drajva VM-a**. U postavkama VM-a, možete takođe postaviti da prvi boot bude sa diska.



![Image](assets/fr/021.webp)



Virtuelna mašina će se ponovo pokrenuti i učitati OPNsense sistem sa diska, pošto smo ga upravo instalirali. Prijavite se sa "root" nalogom u konzoli, i vašom novom lozinkom (inače, podrazumevana lozinka je "**opnsense**").



### D. Povezivanje mrežnih interfejsa



Ekran prikazan ispod će se pojaviti. Izaberite "**1**" i pritisnite **Enter** da povežete mrežne kartice mašine sa OPNsense interfejsima.



![Image](assets/fr/022.webp)



Prvo, čarobnjak vas pita da konfigurišete agregaciju linkova i VLAN-ove. Navedite "**n**" da odbijete, i svaki put potvrdite vaš odgovor sa **Enter**. Zatim, treba da dodelite dva interfejsa "**hn0**" i "**hn1**" za **WAN** i **LAN**. U principu, "**hn0**" odgovara WAN-u, a drugi Interface LAN-u.



Evo kako funkcioniše:



![Image](assets/fr/023.webp)



Sada imamo:





- Interface **LAN** povezan sa mrežnom karticom "**hn1**" i sa podrazumevanom IP adresom OPNsense Address, tj. **192.168.1.1/24**.
- Interface **WAN** povezan sa mrežnom karticom "**hn0**" i sa IP Address dobijenom putem **DHCP** na lokalnoj mreži (zahvaljujući našem eksternom virtuelnom prekidaču).



Podrazumevano, administracija OPNsense Interface je dostupna samo sa LAN Interface, iz očiglednih bezbednosnih razloga. Stoga se morate povezati na Interface LAN firewall-a da biste izvršili administraciju. Ako to nije moguće, možete privremeno upravljati OPNsense sa WAN-a. Ovo podrazumeva onemogućavanje funkcije firewall-a.



Da biste to uradili, prebacite se na režim ljuske putem opcije "**8**" i pokrenite sledeću komandu:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Pristup OPNsense Interface sistemu za upravljanje



OPNsense Administration Interface može se pristupiti putem HTTPS-a, koristeći IP Address LAN-a** Interface (ili WAN-a). Vaš pretraživač će vas odvesti na stranicu za prijavu. Prijavite se sa "root" nalogom i lozinkom koju ste ranije odabrali.



![Image](assets/fr/034.webp)



Sačekajte nekoliko sekundi... Bićete upitani da pratite čarobnjaka za osnovnu konfiguraciju. Kliknite "**Next**" da nastavite.



![Image](assets/fr/036.webp)



Prvi korak je da definišete ime hosta, ime domena, izaberete jezik i definišete DNS server(e) koji će se koristiti za razrešavanje imena. Zadržavanje opcije "**Enable Resolver**" će omogućiti da se firewall koristi kao DNS resolver, što će biti korisno za mašine u našoj virtuelnoj LAN mreži.



![Image](assets/fr/037.webp)



Pređite na sledeći korak. Čarobnjak vam daje opciju **definisanja NTP servera za sinhronizaciju datuma i vremena**, iako su već podrazumevano konfigurisani serveri. Pored toga, neophodno je izabrati vremensku zonu koja odgovara vašoj geografskoj lokaciji (osim ako nemate posebne zahteve).



![Image](assets/fr/038.webp)



Zatim dolazi važan korak: **konfigurisanje Interface WAN**. Trenutno je konfigurisano u DHCP i ostaće u ovom režimu konfiguracije, osim ako ne želite da postavite statički IP Address.



![Image](assets/fr/039.webp)



Još uvek na stranici za konfiguraciju Interface WAN, potrebno je da poništite opciju "**Block access to private networks via WAN**" ako mreža na WAN strani koristi privatne adrese. Ovo će verovatno biti slučaj ako vodite laboratoriju, i tako može sprečiti vaš pristup Internetu.



![Image](assets/fr/040.webp)



Dalje, možete **definisati "root"** lozinku, ali ovo je opcionalno jer smo to već uradili.



![Image](assets/fr/041.webp)



Nastavite do kraja da biste pokrenuli ponovno učitavanje konfiguracije. Ako treba da nastavite sa preuzimanjem kontrole putem WAN-a, ponovo pokrenite gornju komandu kada se ovaj proces završi.



![Image](assets/fr/042.webp)



To je sve što treba da se uradi!



![Image](assets/fr/035.webp)



### E. DHCP konfiguracija



Naš cilj je koristiti OPNsense DHCP server za distribuciju IP adresa na virtuelnoj LAN mreži. Da bismo to uradili, potrebno je pristupiti ovoj lokaciji u meniju:



```
Services > ISC DHCPv4 > [LAN]
```



**Kao što možete videti, DHCP je već podrazumevano omogućen na LAN-u ** Ako niste zainteresovani za ovu uslugu, trebalo bi da je onemogućite. Iako je već omogućen i želimo da ga koristimo, važno je pregledati njegovu konfiguraciju.



Ako je potrebno, možete promeniti opseg IP adresa koje će biti distribuirane: **192.168.10.10** do **192.168.10.245**, u zavisnosti od trenutnih podešavanja.



![Image](assets/fr/046.webp)



Takođe možemo videti da su polja "**DNS servers**", "**Gateway**", "**Domain name**", itd., prazna po defaultu. U stvari, postoji automatsko nasleđivanje određenih opcija i podrazumevanih vrednosti za ova različita polja. Na primer, za DNS server će biti distribuiran IP Address LAN-a Interface, omogućavajući korišćenje OPNsense firewall-a kao DNS resolvera.



Sačuvaj konfiguraciju nakon što napraviš bilo kakve izmene, ako je potrebno.



![Image](assets/fr/047.webp)



Da biste testirali DHCP server, potrebno je da povežete mašinu na LAN mrežu vašeg firewall-a.



Ova mašina mora dobiti IP Address od OPNsense DHCP servera, i naša mašina mora imati pristup mreži. Pristup internetu mora raditi. Imajte na umu da ako ste onemogućili funkciju vatrozida za pristup OPNsense sa WAN-a, ovo će onemogućiti NAT, sprečavajući vas da pristupite Webu.



**Napomena**: trenutno izdate DHCP zakupnine su vidljive iz OPNsense administracije Interface. Da biste to uradili, idite na sledeću lokaciju: **Services > ISC DHCPv4 > Leases**.



![Image](assets/fr/045.webp)



### F. Konfigurisanje NAT i firewall pravila



Dobra vest je da sada možemo pristupiti OPNsense administraciji Interface sa LAN-a.



```
https://192.168.1.10
```



Nakon prijavljivanja na OPNsense, hajde da istražimo NAT konfiguraciju. Idite na ovu lokaciju: **Firewall > NAT > Outbound**. Ovde možete birati između automatskog (podrazumevano) i ručnog kreiranja izlaznih NAT pravila.



Izaberite automatski režim putem opcije "**Automatsko generisanje odlaznih NAT pravila**" i kliknite na "**Sačuvaj**" (u principu, ova konfiguracija je već aktivna). U automatskom režimu, OPNsense sam kreira NAT pravilo za svaku od vaših mreža.



![Image](assets/fr/043.webp)



Za sada, svi računari povezani na virtuelni LAN "**192.168.10.0/24**" mogu pristupiti Internetu bez ograničenja. Međutim, naš cilj je ograničiti pristup WAN-u na HTTP i HTTPS protokole, kao i DNS na Interface LAN-u firewall-a.



Dakle, treba da kreiramo pravila za firewall... Pregledajte meni na sledeći način: **Firewall > Rules > LAN**.



**Podrazumevano, postoje dva pravila za autorizaciju celokupnog odlaznog LAN saobraćaja, u IPv4 i IPv6**. Deaktivirajte ova dva pravila klikom na strelicu Green krajnje levo, na početku svake linije.



Zatim kreirajte tri nova pravila za autorizaciju **LAN mreže** (tj. "**LAN net**") da:





- pristupite svim destinacijama koristeći **HTTP**.
- pristupite svim destinacijama pomoću **HTTPS**.
- zahtevaj **OPNsense** na njegovom **Interface LAN** (tj. "**LAN Address**"), putem **DNS protokola** (ovo podrazumeva korišćenje firewall-a kao DNS), u suprotnom autorizuj svoj DNS resolver putem njegovog IP-a Address.



Ovo daje sledeći rezultat:



![Image](assets/fr/044.webp)



Sve što preostaje je da kliknete na "**Primeni izmene**" kako biste prebacili nova pravila vatrozida u produkciju. **Imajte na umu da će svi tokovi koji nisu eksplicitno autorizovani biti blokirani po defaultu.



LAN mašina može pristupiti Internetu, koristeći HTTP i HTTPS. Svi ostali protokoli će biti blokirani.



![Image](assets/fr/018.webp)



## IV. Zaključak



Prateći ovaj vodič, moći ćete da instalirate OPNsense i odmah počnete sa radom. OPNsense nudi širok spektar funkcija za efikasno obezbeđivanje i upravljanje mrežnim saobraćajem, i pogodan je za upotrebu u profesionalnim okruženjima.



Ova instalacija je samo početak: slobodno istražite menije i konfigurišite druge funkcije kako biste prilagodili OPNsense svojim potrebama.