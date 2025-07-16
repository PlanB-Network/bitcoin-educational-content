---
name: Pi-Hole
description: Blokator oglasa za celu vašu mrežu
---
![cover](assets/cover.webp)



___



*Ovaj vodič je zasnovan na originalnom sadržaju Floriana Duchemina objavljenom na [IT-Connect](https://www.it-connect.fr/). Licenca [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Moguće je da su napravljene izmene u originalnom tekstu.*



___



## I. Prezentacija



Svi smo to uradili čim pokrenemo naš omiljeni pregledač: instaliramo **adblocker** (blokator reklama). Međutim, kada koristimo TV pregledač ili Android uređaj, itd... Malo je teže pronaći nešto što radi. A ako ima više od jednog uređaja u kući, pa, morate ponoviti operaciju za svaki pregledač!



U ovom vodiču, rešićemo jednostavan problem**: obezbediti blokator oglasa za sve mašine na našoj mreži i upravljati njime centralno.**



Da bismo to uradili, koristićemo alat razvijen za ovu svrhu: **Pi-Hole**



Pi-Hole je DNS sinkhole. Koristiće DNS zahteve koje prave vaši uređaji da validira ili odbije saobraćaj, čime vas štiti od adresa i domena za koje se zna da distribuiraju reklame, malver i slično.



DNS označava Domain Name System. Dakle, šta je domen? Pa, "it-connect.fr" je samo jedan primer. Ime domena je jedinstveni identifikator za jedan ili više resursa, obično kojim upravlja jedan entitet.



Naziv mašine plus naziv domena naziva se FQDN za *Fully Qualified Domain Name*. Omogućava vam da dođete do određene mašine samo "pozivanjem" iste. Na primer, kada ukucate "www.trucmachin.com", zapravo pozivate mašinu "www", koja pripada domenu "trucmachin.com".



Osim što naši računari ne razumeju ljudski jezik, sve što razumeju je binarno, pa im je potreban IP Address, što je ekvivalent telefonskog broja, da bi došli do vebsajta.



Dakle, svaki put kada unesete ime veb-sajta u svoj pregledač ili kliknete na link, vaš računar prvo pita DNS server za IP Address koji odgovara tom imenu.



**Pi-Hole će zatim pregledati ove zahteve (ima ih na stotine svakog dana!) i automatski blokirati one za koje je poznato da hostuju reklame ili čak zlonamerne datoteke



## II. Instaliranje Pi-Hole



Sa imenom kao što je Pi-Hole, mogli biste s pravom pretpostaviti da vam je potreban Raspberry-Pi... Ali to nije sasvim tačno. **Pi-Hole se može instalirati na bilo koji Linux računar (Debian, Fedora, Rocky, Ubuntu, itd.)



S druge strane, morate imati na umu da **ovaj uređaj mora raditi 24 sata dnevno iz jednostavnog razloga: nema DNS-a, nema Interneta!** Raspberry je stoga dobra ideja, jer troši gotovo nimalo energije.



Da biste instalirali, jednostavno se povežite na vašu Linux mašinu putem SSH-a i unesite sledeću komandu kao "*root*":



```
curl -sSL https://install.pi-hole.net | bash
```



> **Napomena**: u normalnim okolnostima, nije preporučljivo "hakovati" skriptu bez prethodnog poznavanja njene funkcije. Ako niste sigurni, idite na stranicu putem pretraživača ili preuzmite sadržaj kao datoteku.
>


> **Napomena: na minimalnim verzijama Debian 11, Curl nije instaliran, tako da ga morate ručno instalirati pomoću komande **apt-get install curl** pre nego što unesete gornju komandu.

Kada se skripta pokrene, izvršiće se niz testova, a sama instalacija će se pobrinuti sama za sebe:



![Image](assets/fr/019.webp)



Instaliranje Pi-Hole



Kada je instalacija završena, bićete preusmereni na ovaj ekran:



![Image](assets/fr/020.webp)



Pi-Hole početni ekran



> **Napomena**: ako koristite DHCP na vašem računaru, dobićete upozorenje o tome. Naravno, za pravilnu upotrebu, snažno preporučujemo da dodelite fiksnu IP adresu vašem računaru.

Nakon ovog ekrana, dobićete nekoliko informativnih poruka, a zatim ćete biti preusmereni na čarobnjak za konfiguraciju, koji će vas prvo pitati kojem DNS serveru će Pi-Hole prosleđivati zahteve. Ja sam izabrao Quad9, koji ima povelju o privatnosti korisnika.



![Image](assets/fr/021.webp)



DNS selekcija - Pi-Hole



> **Napomena: ako ste u kompaniji, verovatno je vaš trenutni DNS server kontroler domena Active Directory. Ali ne brinite, kasnije možete navesti uslovni preusmerivač za domen po vašem izboru. Obično ćete moći da preusmerite bilo koji zahtev koji se tiče vašeg lokalnog domena na vaš DNS server.

Primetićete da neki izbori uključuju opciju DNSSEC. U suštini, DNS protokol nije siguran (nije dizajniran sa tim na umu u to vreme). DNSSEC rešava ovaj problem dodavanjem Layer sigurnosti kroz enkripciju i potpisivanje razmena, kao što je objašnjeno u odgovarajućem članku: [DNS Security](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Bilo koji blokator oglasa oslanja se na jednu ili više lista da bi obavio svoj posao. Pi-Hole dolazi sa jednom listom kao standardnom, pa je izaberite i dodajte više kasnije.



![Image](assets/fr/022.webp)



Dođe pitanje o Interface webu, njegova instalacija je opcionalna, jer alat ima sopstvenu komandnu liniju za upravljanje i vizualizaciju. Ali ovaj Interface je prilično prijatan i dobro urađen, pa preporučujem da ga instalirate u isto vreme:



![Image](assets/fr/023.webp)



Ako instalirate Pi-Hole na mašinu koja već ima Web server, možete odgovoriti sa "ne" na sledeće pitanje. Imajte na umu, međutim, da su PHP i nekoliko modula potrebni da bi ovo radilo. U suprotnom, **lighttpd će biti instaliran sa svim potrebnim modulima**.



![Image](assets/fr/024.webp)



Zatim ćete biti upitani da li želite da beležite DNS zahteve. **Ako želite da sačuvate istoriju, postavite ovo na da; u suprotnom, postavite na ne, ali izgubićete deo funkcionalnosti** (pogledajte sledeći ekran).



![Image](assets/fr/025.webp)



Za svoju Interface mrežu, Pi-Hole koristi sopstvenu funkciju pod nazivom FTLDNS, koja obezbeđuje API i generiše statistiku iz DNS zahteva. Ova funkcija može uključivati "privatni" režim koji maskira tražene domene, korisnike iza zahteva, ili oboje. Korisno je ako želite da vršite monitoring bez narušavanja privatnosti ljudi, ili jednostavno ako želite da se pridržavate relevantnih propisa u slučaju korišćenja na javnoj mreži.



![Image](assets/fr/026.webp)



Izbor privatnog načina života



Kada se odgovori na ovo poslednje pitanje, skripta će uraditi ono što treba: preuzeti GitHub repozitorijume i konfigurisati Pi-Hole. Na kraju instalacije, prikazaće se ekran sažetka sa važnim informacijama:



![Image](assets/fr/027.webp)



Ekran rezimea instalacije



Zapiši lozinku za web Interface i informacije o mreži. Sada je vreme da konfigurišemo DHCP uslugu na našoj trenutnoj lokaciji.



## III. DHCP konfiguracija



Da bi funkcionisao, Pi-Hole treba da "rešava" DNS zahteve od klijenata, tako da oni moraju znati da je to onaj kome ih treba poslati. Postoji nekoliko načina da se to uradi:





- Izmenite DNS postavke na vašem DHCP serveru (npr. vaš Box)
- Onemogući ovaj server i koristi onaj koji obezbeđuje Pi-Hole
- Ručno modifikujte svaki uređaj da koristi Pi-Hole kao DNS



Lično biram prvo rešenje. Verovatno **imate DHCP server tamo gde ste** (obično vaš uređaj). Dakle, nema potrebe da se zamarate.



Kako postoji veliki broj mogućnosti, između različitih kutija operatera (o kojima ne znam sve) i onih koji imaju svoj ruter, neću pružiti snimak ekrana za ove izmene. U svakom slučaju, potrebno je otići na DHCP postavke i izmeniti "DNS" parametar kako biste uključili IP Address vašeg Pi-Hole-a.



Jednom kada je ovo urađeno, ako su neki uređaji bili uključeni ranije, zadržaće stare postavke, pa ćete morati ponovo pokrenuti zahtev za konfiguraciju.



Na Windows radnim stanicama, sa komandnom linijom :



```
ipconfig /renew
```



Na Linux radnoj stanici :



```
dhclient
```



Za sve ostale uređaje, moraju se isključiti i ponovo uključiti.



Dakle, treba da dobiju prave parametre, da provere:



```
ipconfig /all
```



U DNS polju, trebalo bi da imate Address vašeg Pi-Hole, u mom slučaju 192.168.1.42 :



![Image](assets/fr/029.webp)



## IV. Korišćenje Interface web Pi-Hole



Da bi se olakšala administracija, **Pi-Hole** koristi dobro dizajniran Interface web Interface. Korisnički je prilagođen i pristupačan, omogućava vam da:





- Prikaži broj zahteva, blokiranih zahteva, itd. u realnom vremenu.
- Upravljajte svojom Belom i Crnom listom
- Dodajte statičke unose, alias-e, itd.
- Dodaj liste
- I mnoge druge funkcije!



Što se mene tiče, dodaću listu za blokiranje. Kao što je gore pomenuto, samo jedna lista je bila instalirana u isto vreme kad i Soft. Postoji mnogo lista za reklamne sajtove, ali je najbolje izabrati bar jednu specifičnu za zemlju u kojoj živite. Jedna od najpoznatijih lista je **EasyList**, a jedna od njih je specifična za Francusku: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



Da biste ga dodali, prvo se povežite na Interface admin: **http://<ip_du_PiHole>/admin**



Lozinka administratora je već generisana (pogledajte snimak ekrana na kraju instalacije), tako da je sve što treba da uradite da je unesete kako biste pristupili Interface :



![Image](assets/fr/030.webp)



Interface iz Pi-Hole



Možemo videti, na primer, da su dva korisnika povezana na Pi-Hole, da je obradio 442 zahteva i da je 8 od njih blokirano. Ovi grafici mogu biti dobar izvor informacija, posebno u profesionalnom kontekstu.



Da biste dodali našu listu, idite na menije "**Group Management**" i "**Adlists**":



![Image](assets/fr/031.webp)



Možemo videti našu prvu listu "**StevenBlack**", da bismo dodali našu, kopirajte link koji sam vam dao iznad i ubacite ga u polje "**Address**", za opis, biram da stavim ime liste:



![Image](assets/fr/032.webp)



Dodavanje liste u Pi-Hole



Sve što preostaje je da kliknete na "**Add**" da biste ga dodali. Da bismo ga aktivirali, potrebno je da izvršimo dodatni korak kako bismo "upozorili" Pi-Hole da preuzme ovu listu. Da bismo to uradili:





- Ili koristite ugrađenu komandnu liniju
- Ili Interface web



Lično sam izabrao drugi, jer ako ste pažljivo pogledali, link ka PHP skripti koja vrši ažuriranje je direktno na stranici na kojoj se nalazimo (reč "online"). Dakle, sve što treba da uradite je da kliknete na njega, što će vas odvesti na stranicu sa samo jednom opcijom:



![Image](assets/fr/033.webp)



Stranica će prikazati rezultat skripte kada bude završena, što znači da je lista uzeta u obzir (osim ako se ne prikaže poruka o grešci, naravno).



Kao što je najavljeno na početku ovog tutorijala, Pi-Hole vam takođe omogućava da **blokirate domene za koje se zna da distribuiraju malver. Da biste ojačali ovu funkciju, predlažem da dodate i redovno ažuriranu listu domena koju distribuira Abuse.ch**, što će značajno ojačati sigurnost vaše mreže, dostupnu na [ovom Address](https://urlhaus.abuse.ch/downloads/hostfile/).



Naravno, možete dodati bilo koje liste za koje smatrate da su relevantne, ili ručno upravljati svojom crnom listom putem menija crne liste.



## V. Pi-Hole testovi



Sada kada je sve na svom mestu, sve što treba da uradiš je da testiraš rešenje kako bi se uverio da radi ispravno.



Na primer, pokušaću da pristupim domenu *http://admin.gentbcn.org/* koji se nalazi na listi Abuse.ch jer je poznato da hostuje malver:



![Image](assets/fr/034.webp)



Očigledno, negde sam blokiran. Da bismo se uverili da je Pi-Hole obavio posao, možemo proveriti dnevnik upita u Interface veb "Query Log" da vidimo da li je blokada sa liste:



![Image](assets/fr/035.webp)



## VI. Zaključak



U ovom vodiču, pokazali smo vam kako da postavite DNS server koji ne samo da eliminiše većinu reklama radi vašeg komfora pri pretraživanju, već takođe dodaje **Layer nivo sigurnosti blokiranjem domena koji šire phishing i malware**.



Sve besplatno i ekonomično ako se instalira na Raspberry-Pi (u smislu potrošnje energije).