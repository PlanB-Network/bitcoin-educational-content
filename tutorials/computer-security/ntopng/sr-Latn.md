---
name: Ntopng
description: Nadgledajte vašu mrežu pomoću ntopng
---
![cover](assets/cover.webp)



___



*Ovaj vodič je zasnovan na originalnom sadržaju Floriana Duchemina objavljenom na [IT-Connect](https://www.it-connect.fr/). Licenca [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Moguće je da su napravljene izmene u originalnom tekstu.*



___



## I. Prezentacija



**Bilo da je u pitanju provera fluidnosti mreže, dobijanje jasne slike o korišćenju ili statistika performansi, praćenje protoka mreže je važan deo mreže preduzeća**. Pomaže u predviđanju promena infrastrukture i osigurava kvalitet korišćenja za korisnike (takođe poznat kao QoE za *Quality of Experience*, za razliku od QoS).



Da biste to uradili, dostupne su mnoge tehnike i softver/protokoli. Na primer, Netflow, koji je razvio Cisco, može se koristiti za preuzimanje statistike IP tokova sa Interface, ali je njegova upotreba ograničena na kompatibilnu opremu.



Zato ću u ovom vodiču predstaviti **Ntop** i pokazati vam kako da ga koristite u vašoj infrastrukturi za praćenje korišćenja mreže.



Ntop je softver otvorenog koda koji se može instalirati na bilo koji Linux računar. Besplatan je i može prikupljati sledeće podatke:





- Iskorišćenost propusnog opsega
- Glavni kupci
- Glavne destinacije
- Protokoli korišćeni
- Aplikacije korišćene
- Portovi korišćeni
- Itd.



Sada preimenovan u **Ntopng (Nova Generacija)**, nudi mnoge osnovne funkcije besplatno. Dostupna je i komercijalna verzija, koja omogućava izvoz konfigurisanih upozorenja u softver tipa SIEM, ili filtriranje saobraćaja sa pravilima definisanim direktno iz sonde.



## II. Preduslovi



Instalacija Ntop sonde razlikuje se u zavisnosti od opreme i okruženja. Dakle, ovde vam neću dati vodič korak po korak, već ću izložiti razne mogućnosti.



### A. Način rada na brodu



Ako imate pfSense, OPNSense ili Endian firewall u produkciji, ili čak Linux radnu stanicu sa NFTables, dobre vesti! Možete direktno instalirati Ntopng i početi pratiti vaše interfejse.



Prednost ove tehnike je što ne zahteva dodatni hardver. S druge strane, povećava iskorišćenost resursa, pa se pobrinite da imate adekvatan hardver ili VM odgovarajuće veličine (minimum 2 jezgra i 2BG RAM-a).



### B. TAP / SPAN režim



**Tap** je **mrežni uređaj koji duplicira saobraćaj koji prolazi kroz njega i šalje ga na drugi uređaj.** Prednost ovog uređaja je što ne zahteva nikakve izmene postojeće infrastrukture i može se postaviti bilo gde za nadgledanje određenih delova mreže, ili između centralnog sviča i ivicnog rutera za analizu saobraćaja ka/od Interneta.



Veliki nedostatak ove vrste opreme je njena cena. U današnjim Gigabit mrežama, pasivni tap ne može pravilno da uhvati mrežni saobraćaj, tako da vam je potreban aktivni uređaj koji košta oko 200 € (minimum).



**SPAN** mod, takođe poznat kao **port mirroring**, koristi se od strane sviča za prosleđivanje saobraćaja sa jednog porta na drugi. Ovo je daleko moj omiljeni metod, jer je jednostavan za postavljanje i, kao tap, omogućava vam da nadgledate deo mreže ili celu mrežu po želji. Međutim, postoje dva nedostatka: svič mora integrisati ovu funkciju, i njegova upotreba može povećati opterećenje procesora na sviču.



### C. Režim rutera



Savršeno je moguće montirati ruter pod Linuxom i instalirati ntopng na njega. Jedini nedostatak ove metode je što će modifikovati vašu mrežu, bilo njeno interno adresiranje, ili adresiranje između vašeg "pravog" rutera i onog koji dodajete.



Napomena: za čitaoce članka [Create a Wifi router with Raspberry Pi and RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) potpuno je moguće instalirati ntopng na vaš Rpi kako biste dobili tačne statistike!



### D. Bridge mode



Zanimljiva alternativa je korišćenje **Linux mašine u bridge režimu.** Postavljena između dva uređaja, omogućava da se sav saobraćaj presretne bez potrebe za intervencijom u konfiguraciji infrastrukture ili njene opreme. Kako stara mašina može obaviti posao, trošak ove metode može biti privlačan. Imajte na umu da, da bi bilo optimalno, uređaj treba da ima tri mrežne kartice, dve u bridge režimu, jednu za pristup Interface i SSH. Moguće je koristiti samo dve kartice, ali tada će i saobraćaj administracije uređaja biti presretnut...



Dakle, **koristiću ovaj poslednji režim**. Iz praktičnih razloga, koristiću virtuelne mašine za demonstraciju, ali metoda ostaje ista za korišćenje na fizičkim mašinama.



## III. Priprema sonde sa Interface mostom



Za sondu biram mašinu sa **Debian 11** u minimalnoj instalaciji.



Prvi korak, uvek isti, ažuriraj:



```
apt-get update && apt-get upgrade
```



Zatim instalirajte paket **bridge-utils**, koji će nam omogućiti da kreiramo naš most:



```
apt-get install bridge-utils
```



Jednom kada je instaliran, prva stvar koju treba primetiti je trenutno ime naših mrežnih kartica. Pod Debian-om, ovo ime može imati nekoliko oblika, i biće nam potrebno za konfiguraciju.



Jednostavna komanda **ip add** će vratiti izlaz sa ovim informacijama:



![Image](assets/fr/016.webp)



Ovde vidim 3 interfejsa:





- Lo**: ovo je loopback Interface; to je virtuelni Interface koji "loopuje" preko opreme. U suštini, ovaj Interface, čiji je Address 127.0.0.1 (iako će bilo koji Address u 127.0.0.0/8 poslužiti, jer je ovaj opseg rezervisan za ovu svrhu) se koristi za kontaktiranje same opreme. Ako ste instalirali web sajt na svojoj radnoj stanici (koristeći WAMPP, na primer), verovatno ste koristili "*localhost*" Address u nekom trenutku da prikažete sajt hostovan na vašoj sopstvenoj mašini. Ovo ime hosta je povezano sa Address 127.0.0.1 i stoga sa Interface loopback.
- ens33**: ovo je moj prvi Interface, koji je ovde dobio Address od mog DHCP-a
- ens36**: moj drugi Interface



Sada kada imam sve informacije, mogu da izmenim datoteku */etc/network/interfaces* kako bih kreirao svoj bridge. Evo kako trenutno izgleda (može se razlikovati):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



Prvi deo se odnosi na moj loopback Interface, koji neću dirati, a zatim sledi Interface ens33. Izmene uključuju dodavanje mog drugog Interface (ens36) i konfigurisanje bridge-a sa ova dva interfejsa:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



Evo nekoliko objašnjenja ovih prvih promena:





- auto *Interface***: će automatski "pokrenuti" Interface pri pokretanju sistema
- iface *Interface* inet manual**: da koristite Interface bez bilo koje IP Address. Kao ključna reč "static" za definisanje statičke IP Address ili "dhcp" za korišćenje dinamičkog adresiranja



Izmene se nastavljaju:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



Evo ponovo nekoliko objašnjenja:





- iface br0 inet static**: here I've defined my Interface bridge (*br0*) with a static Address.
- Address, netmask, gateway**: informacije o adresiranju ploče
- bridge_ports**: interfejsi koji će biti uključeni u bridge
- bridge_stp**: protokol Spanning Tree se koristi prilikom međusobnog povezivanja svičeva kako bi se detektovale redundantne veze i izbegle petlje. Pošto most može biti umetnut između dve mrežne putanje, može biti izvor petlje, stoga postoji mogućnost omogućavanja ovog protokola. Ne treba mi ovde, pa ga onemogućavam.



Sačuvaj promene i restartuj mrežu:



```
systemctl restart networking
```



Da biste proverili promene, ponovo prikažite rezultat komande **ip** add:



![Image](assets/fr/021.webp)


Možete jasno videti **moj novi Interface "*br0*" sa IP Address koji sam mu dodelio.** Usput, možete takođe videti da su moja dva fizička interfejsa zaista "UP", ali nemaju IP Address.



## IV. Instaliranje NtopNG



Sada kada naša sonda može da njuši saobraćaj između moje mreže i rutera, sve što preostaje je da instaliramo ntopng. Da bismo to uradili, prvo izmenite datoteku */etc/apt/sources.list* i dodajte **contrib** na kraj svake linije koja počinje sa **deb** ili **deb-src**.



Podrazumevano, izvori paketa sadrže samo pakete usklađene sa DFSG (*Debian Free Software Guidelines*), označene ključnom reči **main**. Takođe možete dodati ove izvore:





- contrib**: paketi koji sadrže softver usklađen sa DFSG, ali koriste zavisnosti koje nisu deo **main** grane
- non-free**: sadrži pakete koji nisu u skladu sa DFSG-om



Primer linije u /etc/apt/sources.list:



```
deb http://deb.debian.org/debian/ bullseye main
```



Dakle, samo ću dodati reč **contrib** u ovakve redove.



Ostatak koraka je naveden na [NtopNG] sajtu (https://packages.ntop.org/apt/) gde, za Debian 11, treba da dodate Ntop izvore za buduću instalaciju. Ovo dodavanje je automatizovano korišćenjem:



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Zatim dolazi stvarna faza instalacije:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



Prva komanda briše keš apt upravljača paketa. Druga će ažurirati listu paketa, a treća će instalirati NtopNG.



Nakon instalacije, **NtopNG softver je direktno dostupan na portu 3000 Debian mašine**. Tako da je za mene to `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



NtopNG početna stranica



Podrazumevani login i lozinka su prikazani, tako da sve što treba da uradite je da ih unesete!



## V. Korišćenje NtopNG



Kada se prvi put prijavite, prva stvar koju će vam biti zatraženo da uradite je da promenite podrazumevanu administratorsku lozinku i jezik. Nažalost, francuski nije jedan od njih.



Zatim stižete na kontrolnu tablu:



![Image](assets/fr/023.webp)



NtopNG kontrolna tabla



Nemoj se navići na ovo! Ako primetiš žuti okvir na vrhu ekrana, videćeš rečenicu: "*Licence expires in 04:57*". Po defaultu, instalacija pokreće probnu verziju pune verzije NtopNG, ali na (veoma) ograničeno vreme. Kada se ovaj "odbrojavanje" završi, aktivira se *community* verzija i kontrolna tabla se menja:



![Image](assets/fr/024.webp)



Nova NtopNG zajednica kontrolna tabla



Prva stvar koju treba uraditi je **proveriti da li ispravan Interface sluša**. U gornjem levom uglu, padajuća lista dostupnih interfejsa omogućava vam da izaberete Interface koji nas ovde zanima: br0



![Image](assets/fr/025.webp)



Interface izbor



Novi prozor prikazuje "Top Flaw Talkers", tj. uređaje koji najviše komuniciraju. Ovde imam samo dve stanice koje se pojavljuju:



![Image](assets/fr/026.webp)



**Izvorišni hostovi se pojavljuju sa leve strane, odredišta sa desne strane** Ovo vam omogućava da vizualizujete korišćenje ukupne širine pojasa od strane svakog hosta i da dobijete celokupan pregled mrežnog saobraćaja. To nije loše, ali možemo ići dalje...



Ako kliknem na "*Hosts*", na primer, dobijam grafikon koji prikazuje potrošnju energije za slanje i primanje svakog hosta na mojoj mreži. Ovde, na primer, mogu da vidim da 192.168.1.37 sam čini 80% mog saobraćaja:



![Image](assets/fr/027.webp)



Ako kliknem na IP Address hosta o kojem je reč, preusmeren sam na stranicu sa rezimeom:



![Image](assets/fr/028.webp)



Mogu da vidim, na primer, da je to VMWare mašina (prepoznajući YES mog MAC Address), da se zove DESKTOP-GHEBGV1 (tako da je sigurno Windows host) I imam **statistiku o primljenim i poslatim paketima, kao i količinu podataka**.



Primetićete i novi meni na vrhu ovog rezimea. Predlažem da kliknete na "**Aplikacije**" da vidite šta uzrokuje toliki saobraćaj:



![Image](assets/fr/017.webp)


Ha, izgleda da imamo odgovor! Na grafiku sa leve strane, **vidimo da 76.6% njegovog saobraćaja dolazi sa ... Windows Update**, tako da ovaj host preuzima ažuriranja!



NtopNG koristi tehnologiju zvanu DPI za *Deep Packet Inspection*, omogućavajući mu da kategorizuje svaki mrežni tok i definiše aplikaciju (ili porodicu aplikacija) koja stoji iza njega.



Da demonstriram, pokrećem YouTube video na svom hostu:



![Image](assets/fr/018.webp)



**Saobraćaj je odmah prepoznat i kategorizovan!



Napomena: iz očiglednih razloga, ovakva vrsta softvera može izazvati probleme sa privatnošću, pa budite pažljivi da ga koristite pod pravim uslovima. Takođe imajte na umu da je moguće **anonimizirati rezultate**, opcija se može pronaći u **Podešavanja > Preferencije > Razno** i zove se "**Mask Host IP Address**".



## VI. Detekcije i upozorenja



NtopNG je takođe sposoban da izdaje bezbednosna upozorenja na određenim feedovima. Ona se mogu pronaći u meniju **Alerts**, na levom baneru. Ovde, na primer, imam ukupno 2851 upozorenje, podeljeno u različite stepene ozbiljnosti: Notice, Warning i Error.



![Image](assets/fr/019.webp)



Hajde da pogledamo upozorenja visoke kritičnosti, imam ih 17!



Klikom na ovu figuru prikazuju se detalji upozorenja. Ovde nema ničeg alarmantnog, to je lažno pozitivno, preuzimanje ažuriranja je kategorizovano kao prenos binarnih fajlova u HTTP strimu, što zaista može značiti napad.



![Image](assets/fr/020.webp)



Međutim, pošto koristim besplatnu verziju, ne mogu da isključim domene ili hostove koji su izvor upozorenja, tako da ćete morati da ih pratite kako ne biste propustili nešto mnogo zabrinjavajuće. NtopNG će generate upozorenja u slučaju:





- Preuzimanje binarne datoteke putem HTTP-a
- Sumnjiv DNS saobraćaj
- Korišćenje nestandardnog porta
- Detekcija SQL injekcije
- Cross-Site Scripting (XSS)
- Itd.



## VII. Zaključak



U ovom vodiču, videli smo **kako postaviti sondu sa NtopNG** što nam omogućava da **analiziramo naš mrežni saobraćaj** kako bismo vizualizovali upotrebu protokola i zauzeće svakog hosta, ali i detektovali sumnjiv saobraćaj.



Nažalost, ne mogu pokriti sve funkcije i mogućnosti u ovom članku, ali slobodno istražite!



Ovo rešenje se može implementirati na trajnoj osnovi unutar infrastrukture preduzeća. NtopNG takođe može izvoziti rezultate u InfluxDB bazu podataka, omogućavajući vam da kreirate sopstvene kontrolne table pomoću alata treće strane kao što je Graphana.