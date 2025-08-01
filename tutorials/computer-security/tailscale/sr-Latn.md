---
name: Tailscale
description: Napredni Tailscale vodič
---
![cover](assets/cover.webp)



## 1. Uvod



Tailscale je VPN nove generacije koji stvara šifrovanu mesh mrežu između vaših uređaja. Omogućava vam povezivanje udaljenih mašina kao da su na istoj lokalnoj mreži, bez složene konfiguracije ili otvaranja portova.



Za samostalno hostovanje, Tailscale dodeljuje svakom uređaju fiksnu privatnu IP adresu u virtuelnoj mreži, omogućavajući stabilan pristup vašim uslugama čak i kada se vaša javna IP adresa promeni. To znači da možete upravljati svojim serverima na daljinu, bez direktnog izlaganja vaših usluga Internetu.



**Glavne aplikacije:**




- Upravljajte ličnim serverom spolja
- Upravljajte Umbrel/Lightning čvorovima brže nego Tor
- Siguran pristup Raspberry Pi ili NAS-u
- Povežite se sa svojim uslugama putem SSH ili HTTP bez složene mrežne konfiguracije



Ovaj pristup fokusiran na jednostavnost omogućava korisnicima koji sami hostuju da pristupe svojim uslugama sigurno, izbegavajući zamke tradicionalnih VPN-ova.



## 2. Kako Tailscale funkcioniše



Za razliku od tradicionalnih VPN-ova, koji sav saobraćaj usmeravaju kroz centralni server, Tailscale stvara mrežu u kojoj uređaji komuniciraju direktno jedni s drugima. Centralni server samo upravlja autentifikacijom i distribucijom ključeva, bez uvida u korisničke podatke.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Slika 1: Tradicionalni VPN sa arhitekturom hub-and-spoke gde sav saobraćaj prolazi kroz centralni server*



Na osnovu WireGuard-a, svaki uređaj generiše sopstvene kriptografske ključeve. Koordinacioni server distribuira javne ključeve čvorovima, koji zatim uspostavljaju end-to-end enkriptovane tunele direktno između sebe. Da bi prošao kroz firewall-ove, Tailscale koristi NAT traversal i, kao poslednju opciju, DERP relaye koji održavaju enkripciju.



![VPN maillé (mesh)](assets/fr/02.webp)


*Slika 2: Tailscale mesh mreža gde uređaji direktno komuniciraju jedni sa drugima*



Sve komunikacije su šifrovane pomoću WireGuard-a. Tailscale vidi samo metapodatke (veze) ali nikada sadržaj razmena. Za veću suverenost, Headscale omogućava da server za koordinaciju bude samostalno hostovan.



**Sigurnost i poverljivost:** Zahvaljujući WireGuard-u, sve komunikacije na Tailscale-u su šifrovane od kraja do kraja. Tailscale ne može čitati vaš saobraćaj - samo vaši uređaji imaju potrebne privatne ključeve. Servis vidi samo metapodatke: IP adrese, imena uređaja, vremenske oznake povezivanja i peer-to-peer dnevnike povezivanja (bez sadržaja).



Međutim, ova arhitektura zavisi od Tailscale Inc. za koordinaciju mreže. Da bi se eliminisala ova zavisnost, Headscale nudi open-source alternativu koja vam omogućava da sami hostujete kontrolni server dok koristite zvanične Tailscale klijente, čime se garantuje potpuni suverenitet nad vašom mrežnom infrastrukturom, uz cenu tehnički složenije konfiguracije.



**Za detaljno objašnjenje unutrašnjeg funkcionisanja Tailscale-a, uključujući upravljanje kontrolnom ravni, NAT prolaz i DERP releje, preporučujemo odličan članak [Kako Tailscale funkcioniše](https://tailscale.com/blog/how-tailscale-works) na zvaničnom blogu. Ovaj članak detaljno objašnjava tehničke koncepte koji čine Tailscale tako moćnim.



## 3. Instaliranje Tailscale



Tailscale radi na **većini uobičajenih** operativnih sistema (Windows, macOS, Linux, iOS, Android). Instalacija je opisana kao "brza i jednostavna" na svim platformama. Počnimo tako što ćemo pogledati interfejs i kako kreirati nalog, a zatim preći na procedure instalacije za različita okruženja.



### 3.1 Kreiranje Tailscale naloga



Idite na [https://tailscale.com/](https://tailscale.com/) i kliknite na dugme "Get Started" u gornjem desnom uglu stranice.




![Page d'accueil Tailscale](assets/fr/03.webp)


*Početna stranica Tailscale-a objašnjava koncept i nudi besplatan početak*



Da biste koristili Tailscale, prvo morate kreirati nalog putem provajdera identiteta:



![Page de connexion Tailscale](assets/fr/04.webp)


*Izbor provajdera identiteta za povezivanje sa Tailscale (Google, Microsoft, GitHub, Apple, itd.)*



Nakon prijavljivanja, Tailscale će vas pitati za neke informacije o vašoj nameravanoj upotrebi:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Obrazac za bolje razumevanje vaše upotrebe (lične ili profesionalne)*



Kada kreirate svoj nalog, možete instalirati Tailscale na svoje uređaje:



![Ajout du premier appareil](assets/fr/07.webp)


*Tailscale vam omogućava da instalirate aplikaciju na različite sisteme*



### 3.2 Instalacija na različitim platformama





- **Na Windows i macOS:** Jednostavno preuzmite grafičku aplikaciju sa zvanične Tailscale veb stranice i instalirajte je (.msi datoteka na Windowsu, .dmg datoteka na Macu). Nakon instalacije, aplikacija pokreće grafički interfjes koji vam omogućava da se povežete (putem pregledača) sa vašim Tailscale nalogom kako biste autentifikovali uređaj.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*Povežite MacBook sa tailnetom*



![Connexion réussie](assets/fr/09.webp)


*Potvrda da je uređaj povezan na Tailscale* mrežu





- **Na Linuxu (Debian, Ubuntu, itd.):** Imate nekoliko opcija. Najjednostavnija metoda je pokretanje zvaničnog instalacionog skripta: na primer, na Debian/Ubuntu :



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Ovaj skript će dodati zvanični Tailscale repozitorijum i instalirati paket. Takođe možete [ručno dodati APT repozitorijum](https://pkgs.tailscale.com) ili koristiti regularne Snap ili apt pakete. Kada se instalira, daemon `tailscaled` će raditi u pozadini. Zatim ćete morati **autentifikovati čvor** (pogledajte Interface CLI vs web ispod). Na drugim distribucijama (Fedora, Arch...), paket je takođe dostupan putem standardnih repozitorijuma ili univerzalnog instalacionog skripta. Za server bez grafičkog interfejsa, koristite CLI: na primer `sudo tailscale up --auth-key <key>` ako koristite unapred generisani ključ za autentifikaciju, ili jednostavno `tailscale up` za interaktivni login (koji će obezbediti URL koji treba posetiti da biste autentifikovali uređaj).





- **Na sistemima zasnovanim na ARM-u (Raspberry Pi, itd.):** Generalno koristimo Linux, tako da je isti pristup kao gore (skripta ili paket). Imajte na umu da Tailscale podržava ARM32/ARM64 arhitekturu bez ikakvih problema. Mnogi korisnici instaliraju Tailscale na Raspberry Pi OS putem apt-a ili na laganim distribucijama (DietPi, itd.) kako bi pristupili svom Pi uređaju svuda.





- **Na iOS i Android:** Tailscale pruža **zvanične** mobilne aplikacije. Jednostavno instalirajte *Tailscale* sa [App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) ili [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).



![Installation sur iPhone](assets/fr/11.webp)


*Koraci za instalaciju Tailscale na iPhone: dobrodošli, privatnost, obaveštenja, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Poveži se na tailnet, izaberi nalog i potvrdi na iPhone-u*



Kada je aplikacija instalirana, pri prvom pokretanju će vas tražiti da se autentifikujete putem odabranog provajdera (Google, Apple ID, Microsoft, itd., u zavisnosti od toga šta koristite za Tailscale) - to je isti postupak kao na drugim platformama, obično preusmeravanje na OAuth veb stranicu. Nakon toga, mobilna aplikacija kreira VPN (na iOS-u ćete morati da prihvatite dodatak za VPN konfiguraciju). Aplikacija zatim može raditi u pozadini, omogućavajući vam pristup vašem tailnet-u sa bilo kog mesta. *Napomena:* na mobilnom uređaju možete imati **samo jedan aktivan VPN u isto vreme** - zato se pobrinite da nemate drugi VPN povezan u isto vreme, jer Tailscale neće moći da uspostavi svoju vezu. Na Androidu, možete postaviti poseban radni profil ako želite da izolujete određene upotrebe (npr. profil sa aktivnim Tailscale-om za određenu aplikaciju).



### 3.3 Dodavanje više uređaja i validacija



Kada je vaš prvi uređaj povezan, Tailscale vas poziva da dodate druge uređaje na vašu mrežu:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interfejs prikazuje prvi povezan uređaj i čeka druge uređaje*



Kada dodate nekoliko uređaja, možete proveriti da li mogu međusobno komunicirati:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Potvrda da uređaji mogu međusobno komunicirati putem pinga*



Tailscale zatim predlaže dodatne konfiguracije kako bi poboljšao vaše iskustvo:



![Suggestions de configuration](assets/fr/14.webp)


*Predlozi za postavljanje DNS-a, deljenje uređaja i upravljanje pristupom*



### 3.4 Administrativna kontrolna tabla



Konzola za administraciju veba omogućava vam da pregledate i upravljate svim vašim povezanim uređajima:



![Tableau de bord des machines](assets/fr/15.webp)


*Lista povezanih uređaja sa njihovim karakteristikama i statusom*



**Interface Web vs Interface CLI:** Tailscale nudi dva komplementarna načina interakcije sa mrežom: **Interfejs web administraciju** i **klijenta komandne linije (CLI)**.





- **Interface Web (Admin Console)** : dostupno na [https://login.tailscale.com](https://login.tailscale.com), ova web konzola je centralna kontrolna tabla za vašu Tailscale mrežu. Prikazuje sve uređaje (*Machines*), njihov online/offline status, njihove Tailscale IP adrese i više. Ovde možete **upravljati uređajima** (preimenovati, isteći ključeve, autorizovati rute, onemogućiti čvor), **upravljati korisnicima** (u organizacionom kontekstu) i definisati sigurnosna pravila (ACLs). Takođe, ovde konfigurišete globalne opcije kao što su MagicDNS, oznake ili auth ključevi (unapred generisani auth ključevi za automatsko dodavanje uređaja). Interface web je veoma koristan za dobijanje pregleda i primenu promena koje će biti propagirane putem koordinacionog servera na sve čvorove. *Primer:* Aktiviranje **subnet rute** ili **exit čvora** se vrši jednim klikom u konzoli, kada se čvor u pitanju najavi kao takav.





- **Interfejs komandne linije (CLI):** Komanda `tailscale` je dostupna u CLI na svakom uređaju gde je Tailscale instaliran. Ovaj CLI vam omogućava da sve radite lokalno: povežete se (`tailscale up`), proverite status (`tailscale status` da vidite koji su vršnjaci povezani), otklonite greške (`tailscale ping <ip>`), i tako dalje. Neke funkcije su čak **ekskluzivne za CLI** ili naprednije, na primer:





  - `tailscale up --advertise-routes=192.168.0.0/24` da oglašava rutu podmreže,
  - `tailscale up --advertise-exit-node` da predložite vašu mašinu kao izlazni čvor,
  - `tailscale set --accept-routes=true` (ili `--exit-node=<IP>`) da konzumirate rutu ili koristite izlazni čvor,
  - `tailscale ip -4` da prikaže Tailscale IP uređaja,
  - `tailscale lock/unlock` (ako koristite *tailnet-lock*, napredna sigurnosna funkcija),
  - ili `tailscale file send <node>` da koristite **Taildrop** (prenos fajlova između uređaja).


CLI je veoma koristan na serverima bez grafičkog interfejsa i za skriptovanje određenih radnji. **Razlike u korišćenju:** Većina osnovnih konfiguracija može se izvršiti ili putem Web-a ili putem CLI. Na primer, dodavanje uređaja se vrši ili putem konzole, ili pokretanjem `tailscale up` na uređaju i validacijom putem web-a. Slično, preimenovanje uređaja može se izvršiti putem konzole ili sa `tailscale set --hostname`. **Ukratko**, web konzola je idealna za globalnu administraciju mreže (posebno sa više mašina/korisnika), dok je CLI zgodan za preciznu kontrolu nad određenom mašinom, automatizovane skripte, ili korišćenje na sistemu bez GUI.



## 4. Korišćenje Tailscale na Umbrel-u



Umbrel je popularna platforma za samostalno hostovanje (posebno korišćena za Bitcoin/Lightning čvorove i druge samostalno hostovane usluge, putem svoje prodavnice aplikacija). Da biste instalirali i konfigurisali Umbrel, preporučujemo da pratite naš posvećeni vodič:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Korišćenje Umbrel-a i Tailscale-a zajedno je posebno zanimljiv slučaj upotrebe, jer Umbrel nativno integriše lako implementirajući Tailscale modul. Evo kako se Tailscale integriše sa Umbrel-om i šta donosi:



### 4.1 Instalacija i konfiguracija Umbrel-a





- **Instaliranje Tailscale na Umbrel:** Umbrel ima zvaničnu Tailscale aplikaciju u svojoj prodavnici aplikacija. Instalacija ne može biti jednostavnija:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Stranica aplikacije Tailscale u Umbrel App Store-u*



Sa Interface Web Umbrel, otvorite App Store, potražite **Tailscale** i kliknite na *Install*. Nekoliko sekundi kasnije, aplikacija je instalirana na Umbrel. Kada je otvorite, Umbrel prikazuje stranicu koja vam omogućava da povežete vaš čvor sa Tailscale.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Ekran za povezivanje Tailscale u Umbrelovom interfejsu*



Samo **kliknite na "Log in"**, što će vas preusmeriti na Tailscale stranicu za autentifikaciju:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Povežite se sa Tailscale-om putem provajdera identiteta*



Možete se autentifikovati putem vašeg Tailscale naloga (Google/GitHub/itd.) ili uneti vaš email. Obično, na Umbrel-u, interfejs traži da posetite [https://login.tailscale.com](https://login.tailscale.com) i prijavite se - ovo autentifikuje Umbrel Tailscale aplikaciju.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Potvrda da je Umbrel uređaj povezan na Tailscale mrežu*



Jednom kada završite, vaš Umbrel je "u" vašoj Tailscale mreži i pojavljuje se na vašoj konzoli sa imenom (npr. *umbrel*). Zatim možete kliknuti na IP adresu vaših uređaja da ga kopirate, preuzmete IPv6 Address ili vaš MagicDNS povezan sa vašim uređajem.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Administratorska konzola Tailscale-a prikazuje nekoliko povezanih uređaja, uključujući Umbrel*




### 4.2 Daljinski pristup Umbrel uslugama



Jednom kada je Umbrel povezan sa Tailscale, **možete pristupiti Umbrel interfejsu i aplikacijama koje rade na njemu, sa bilo kog mesta, kao da ste na lokalnoj mreži**. Ovo je jedna od glavnih prednosti u odnosu na Tor.



Pristup je izuzetno jednostavan: umesto korišćenja `umbrel.local` (što funkcioniše samo na vašoj lokalnoj mreži), koristite Tailscale IP adresu vašeg Umbrela (`http://100.x.y.z`) direktno sa bilo kog uređaja povezanog na vaš tailnet. Ovo funkcioniše bez obzira na to gde se nalazite ili koju internet konekciju koristite (4G, javni Wi-Fi, korporativna mreža).



**Primeri aplikacija hostovanih na Umbrel-u dostupnih putem Tailscale-a:**





- **Interface main Umbrel**: Pristupite svojoj Umbrel kontrolnoj tabli jednostavno tako što ćete uneti `http://100.x.y.z` u vaš pretraživač
- **Bitcoin čvor**: Upravljajte svojim Bitcoin čvorom bez kašnjenja, pregledajte sinhronizaciju i statistiku
- **Lightning čvor**: Koristite ThunderHub, RTL ili druge Lightning interfejse za upravljanje sa trenutnom odzivnošću
- **Mempool**: Pogledaj Bitcoin transakcije i Mempool bez Tor kašnjenja
- **noStrudel**: Pristupite vašim Nostr uslugama hostovanim na Umbrel



**Povežite spoljne novčanike sa vašim Bitcoin ili lightning čvorovima putem Tailscale :**



Tailscale takođe omogućava vašim Bitcoin i Lightning novčanicima instaliranim na drugim uređajima da se direktno povežu sa vašim Umbrel čvorom:





- **Sparrow wallet (Bitcoin)**: Ovaj eksterni Bitcoin novčanik može se direktno povezati sa vašim Umbrel Electrum serverom koristeći Tailscale IP adresu:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Konfigurisanje privatnog Electrum servera u Sparrow novčaniku koristeći Umbrelov Tailscale IP adresu*



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Lista alias-a za Electrum server u Sparrow sa Umbrel Tailscale IP adresom*



Pročitajte naš kompletan vodič za konfiguraciju Sparrow novčanika sa vašim Bitcoin čvorom:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- **Zeus (Lightning)**: Ovaj mobilni Lightning novčanik može se povezati sa vašim Lightning čvorom na Umbrel-u. Umesto da podešavate endpoint kao .onion, jednostavno postavite Tailscale IP adresu vašeg Umbrel uređaja i Lightning API port. Veza će biti trenutna u poređenju sa Tor-om.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Konfigurisanje Zeusa za povezivanje sa Lightning čvorom preko Tailscale* IP adrese



Da biste konfigurisali Zeus sa vašim Lightning čvorom, pogledajte naš detaljni vodič :



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Da biste saznali više o Lightning mređi i kako funkcioniše na Umbrel-u, posetite :



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Prednosti u odnosu na Tor



Umbrel nativno nudi daljinski pristup putem Tor-a (pružanjem `.onion` adresa za svoje web usluge). Iako Tor ima prednost u pogledu poverljivosti (anonimnosti) i ne zahteva registraciju, mnogi korisnici smatraju da je **Tor spor i nestabilan** za svakodnevnu upotrebu (stranice se sporo učitavaju, dolazi do isteka vremena, itd.) - *"Umbrel preko Tor-a je tako spor "* neki se žale.



Tailscale nudi generalno **bržu, nisko-latentnu** vezu, jer saobraćaj prolazi direktno (ili putem brzog releja) umesto da se prebacuje kroz 3 Tor čvora. Štaviše, Tailscale pruža iskustvo "lokalne mreže": koriste se privatni IP-ovi, a aplikacije se mogu direktno mapirati (npr. SMB mrežni disk na \100.x.y.z).



To je rečeno, Tor ima prednost decentralizacije i "out of the box" na Umbrel-u, dok Tailscale podrazumeva poverenje trećoj strani (ili hosting headscale-a). Tor je takođe koristan za pristup bez klijenta (iz bilo kog Tor pretraživača, možete pristupiti Umbrel UI, dok Tailscale zahteva instaliran klijent na uređaju koji pristupa).



**Ukratko**, za interaktivnu upotrebu (Lightning novčanici, česti web interfejsi), Tailscale nudi značajnu udobnost i brzinu u poređenju sa Tor-om, uz cenu blage spoljne zavisnosti. Mnogi ljudi biraju da koriste *oba*: Tailscale na dnevnoj bazi, a Tor kao rezervu ili za deljenje pristupa sa nekim bez pozivanja u njihov VPN.



### 4.4 Bezbednost



Korišćenjem Tailscale-a sa Umbrel-om, izbegavate izlaganje Umbrel-a internetu. Umbrel čvor je dostupan samo vašim drugim autentifikovanim uređajima u tailnet-u, što značajno smanjuje površinu napada (nema otvorenih portova za strance, nema rizika od napada na web servis putem interneta).



Komunikacije su šifrovane (WireGuard) pored bilo koje šifrovanja koje vaši servisi već koriste (npr. čak je i interni HTTP u tunelu). I dalje možete primeniti Tailscale ACL-ove kako biste, na primer, sprečili određeni tailnet uređaj da pristupi Umbrelu ako želite da podelite mrežu. Umbrel sam po sebi ne vidi razliku - misli da služi lokalno.



---

Da zaključimo ovaj deo, integracija Tailscale-a na Umbrel zahteva samo nekoliko klikova i **značajno poboljšava pristupačnost** vašeg samohostovanog čvora. Moći ćete da upravljate Umbrel-om i njegovim uslugama sa bilo kog mesta, sigurno i efikasno, baš kao da ste kod kuće. Ovo je posebno korisno rešenje za aplikacije u realnom vremenu (Lightning) koje pate od Tor latencije, ili generalno za bilo koji samohost koji traži jednostavnu privatnu vezu. Sve to bez izlaganja ijednog **porta** na vašem uređaju, i bez komplikovane mrežne konfiguracije.



## 5. Napredno upravljanje i slučajevi upotrebe



### 5.1 Tailscale napredne funkcije



**Upravljanje mrežom:** Administratorska konzola (login.tailscale.com) omogućava vam upravljanje uređajima, pregled veza i konfiguraciju pravila pristupa.



**MagicDNS:** Automatski rešava imena uređaja (npr. `raspberrypi.tailnet.ts.net`) kako bi se izbeglo pamćenje IP adresa.



**ACL i kontrola pristupa:** Precizno definišite ko može pristupiti čemu u vašoj mreži putem JSON pravila, idealno za izolaciju određenih uređaja ili ograničavanje pristupa specifičnim uslugama.



**Deljenje uređaja** omogućava vam da pozovete nekoga da pristupi određenoj mašini bez davanja pristupa celoj vašoj mreži.



**Subnet Router:** Tailscale mašina može delovati kao prolaz za čitav podmrežni segment, omogućavajući pristup uređajima koji nisu na Tailscale mreži (IoT, štampači, itd.) putem jedne konfigurisane mašine.



**Izlazni čvor:** Koristite mašinu kao internet prolaz da izađete sa njenom IP adresom. Korisno za javni Wi-Fi ili za zaobilaženje geografskih ograničenja.



**Taildrop:** Sigurna alternativa za AirDrop, omogućava vam prenos fajlova između vaših Tailscale uređaja, bez obzira na njihovu platformu ili lokaciju. Za razliku od AirDrop-a, koji je ograničen na Apple ekosistem i fizičku blizinu, Taildrop radi između svih vaših uređaja (Windows, Mac, Linux, Android, iOS), čak i ako su u različitim zemljama. Fajlovi se prenose direktno između uređaja sa end-to-end enkripcijom, bez prolaska kroz centralni server. Koristite komandnu liniju `tailscale file cp` ili grafičku aplikaciju u zavisnosti od vašeg sistema.



### 5.2 Poređenje sa drugim rešenjima



**Vs OpenVPN:** Tailscale je mnogo jednostavniji za konfiguraciju (nema portova za otvaranje, nema upravljanja sertifikatima) ali uključuje zavisnost od usluge treće strane. OpenVPN je potpuno kontrolabilan, ali zahteva više stručnosti.



**Kao direktni konkurent, ZeroTier** radi na nivou 2 (Ethernet), omogućavajući broadcast/multicast, dok Tailscale radi na nivou 3 (IP). ZeroTier nudi veću fleksibilnost mreže, dok Tailscale favorizuje jednostavnost korišćenja.



**Vs Tor:** Tor nudi anonimnost koju Tailscale ne pruža, ali je mnogo sporiji. Tor je decentralizovan i ne zahteva nalog, dok je Tailscale brži i nudi iskustvo slično LAN mreži.



**Vs WireGuard priručnik:** Tailscale automatizuje sve upravljanje ključevima i vezama koje čist WireGuard zahteva da ručno rukujete. To je u suštini WireGuard + pojednostavljeno upravljanje nivoem 3.



U zaključku, Tailscale se pozicionira kao moderno rešenje usmereno na jednostavnost, idealno za ličnu upotrebu i male timove. Za puriste potpune kontrole, Headscale nudi alternativu sa sopstvenim hostingom.



## 6. Zaključak



**Prednosti Tailscale-a:** Tailscale nudi nekoliko prednosti za samostalno hostovanje:





- **Jednostavnost i performanse** - Brza instalacija na svim platformama bez složene mrežne konfiguracije. Saobraćaj prati najdirektniji put između vaših mašina (P2P mesh), uz performanse WireGuard protokola i bez centralnog servera koji bi ograničio protok.
- **Sigurnost i fleksibilnost** - end-to-end enkripcija, smanjena površina napada i napredne funkcije (ACL, SSO/MFA autentifikacija). Radi čak i iza NAT-ova ili u pokretu, sa podmrežnim ruterima i izlaznim čvorovima kako bi se mreža prilagodila vašim potrebama.



**Ograničenja:** Takođe imajte na umu:





- **Eksterna zavisnost** - U svojoj standardnoj verziji, usluga se oslanja na infrastrukturu Tailscale Inc. Ova zavisnost se može zaobići putem Headscale (alternativa za samostalno hostovanje).
- **Ostala ograničenja** - Delimično zatvoren izvorni kod, ograničenja besplatne verzije za određene napredne upotrebe, nema podrške za Layer 2 (broadcast/multicast), i potreba za pristupom internetu za uspostavljanje veza.



**Tailscale je idealan za individualne self-hostove i male timove, programere kojima je potreban pristup raspršenim resursima, početnike u korišćenju VPN-a i mobilne korisnike. Za kompanije kojima je potrebna potpuna kontrola, druga rešenja kao što su Headscale ili direktno WireGuard mogu biti pogodnija**.



**Istražite Headscale za potpuno samostalno hostovanje, API i DevOps integracije (Terraform), ili alternative kao što su Innernet (slično, ali potpuno samostalno hostovano) i Netmaker.**



Tailscale je ključni alat za samostalno hostovanje, zahvaljujući svojoj jednostavnosti i efikasnosti, čineći vašu privatnu infrastrukturu dostupnom kao da je u oblaku, dok zadržavate kontrolu kod kuće.



## 7. Korisni resursi



### Zvanična dokumentacija





- **Tailscale Documentation Center**: [docs.tailscale.com](https://docs.tailscale.com) - Kompletna dokumentacija na engleskom jeziku, vodiči za instalaciju, tutorijali i tehničke reference.
- **Kako Tailscale funkcioniše**: [Kako Tailscale funkcioniše](https://tailscale.com/blog/how-tailscale-works) - Detaljan članak koji objašnjava unutrašnje funkcionisanje Tailscale-a.
- **Changelog**: [tailscale.com/changelog](https://tailscale.com/changelog) - Praćenje ažuriranja i novih funkcija.



### Praktični vodiči





- **Homelab** tutorijali: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Specifični vodiči za samostalno hostovanje.
- **Konfigurisanje izlaznog čvora** : [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Detaljan vodič za konfigurisanje izlaznih čvorova.
- **Koristite Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Prenosite fajlove između Tailscale uređaja.



### Poređenja





- **Tailscale vs. other solutions**: [tailscale.com/compare](https://tailscale.com/compare) - Detaljna poređenja sa drugim VPN i mrežnim rešenjima (ZeroTier, OpenVPN, itd.).



### Zajednica





- **Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Diskusije, pitanja i povratne informacije.
- **GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Izvorni kod za korisnike, mesto gde možete pratiti razvoj i prijaviti probleme.
- **Discord**: [discord.gg/tailscale](https://discord.gg/tailscale) - Zajednica korisnika i programera.



Tailscale redovno pruža novi sadržaj i funkcije. Pogledajte njihov [zvanični blog](https://tailscale.com/blog/) za najnovije vesti i studije slučaja.
