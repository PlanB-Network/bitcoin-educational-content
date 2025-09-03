---
name: Nmap
description: Savladajte Nmap za mapiranje mreže i skeniranje ranjivosti
---

![cover](assets/cover.webp)



*Ovaj vodič je zasnovan na originalnom sadržaju Mickaela Dorignyja objavljenom na [IT-Connect](https://www.it-connect.fr/). Licenca [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Izmene su napravljene u originalnom tekstu.*



___



Dobrodošli u ovaj uvodni vodič za Nmap, dizajniran za svakoga ko želi da ovlada ovim moćnim alatom za skeniranje mreža. Cilj je da vam se pruže osnovna znanja koja su vam potrebna za efikasno korišćenje Nmap-a na dnevnoj bazi.



Nmap je svestran alat, koji široko koriste IT, mrežni i sajber bezbednosni profesionalci za dijagnostiku, otkrivanje mreža i bezbednosne provere. Ovaj vodič je namenjen onima koji su novi u ovim oblastima i žele da nauče osnove Nmap-a. Preporučuje se osnovno znanje o administraciji sistema i mreža.



Naučićete osnove Nmap-a, kako da izvršavate skeniranje portova, identifikujete aktivne hostove na mreži, detektujete verzije servisa i operativne sisteme, izvršavate skeniranje ranjivosti i još mnogo toga. Svaki deo uključuje detaljna objašnjenja i praktične primere koji će vam pomoći da savladate korišćenje Nmap-a u različitim kontekstima.



Do kraja ovog vodiča, imaćete solidno razumevanje Nmap-a i moći ćete ga efikasno koristiti za poboljšanje sigurnosti i upravljanja vašim mrežama. Uživajte u čitanju.



## 1 - Uvod u Nmap: Šta je Nmap?



### I. Prezentacija



U ovom prvom delu, pogledaćemo alat za skeniranje mreže Nmap. Pogledaćemo ključni Elements koji treba da znate o ovom alatu i kako generalno funkcioniše. Ovo će nam pomoći da bolje razumemo ostatak tutorijala.



### II. Uvođenje alata Nmap



Nmap, za _Network Mapper_, je besplatan, open-source alat koji se koristi za **otkrivanje mreža, mapiranje i bezbednosne provere**. Takođe se može koristiti za druge zadatke kao što su **inventarizacija mreže, dijagnostika ili nadzor**.



Može odrediti da li su hostovi na ciljanoj mreži aktivni i dostupni, koji mrežni servisi su izloženi, koje verzije i tehnologije se koriste, i druge korisne informacije za analizu. Nmap se može koristiti za skeniranje jedne usluge na određenoj mašini, ili preko velikih delova mreže, sve do celog Interneta.



Snage Nmap-a su mnoge:





- Snažan i fleksibilan**: Nmap može skenirati velike mreže i koristiti napredne tehnike detekcije. Podržava UDP, TCP, ICMP, IPv4 i IPv6, i može izvršavati detekciju verzija, skeniranje ranjivosti ili interakcije specifične za protokole. Njegova arhitektura je modularna, zahvaljujući posebno NSE (Nmap Scripting Engine) skriptama, koje ćemo kasnije razmotriti u ovom vodiču.
- Jednostavnost korišćenja**: zvanična dokumentacija je obilna i najvišeg kvaliteta. Dostupni su i brojni resursi zajednice koji će vam pomoći da počnete.
- Popularnost i dugovečnost**: Nmap je referenca u svojoj oblasti od 1998. godine. Trenutna verzija, u vreme ovog ažuriranja, je 7.95. Iako postoje drugi alati za specifične zadatke, Nmap ostaje neophodan za mapiranje i analizu mreža.



**Nmap u bioskopu**



Nmap je jedan od retkih sigurnosnih alata koji je stekao izvesnu notornost među širom javnošću. Pojavljuje se u filmu _Matrix Reloaded_, u emblematičnoj sceni gde ga Trinity koristi za hakovanje sistema:



![nmap-image](assets/fr/01.webp)



matrix: Reloaded scena sa Nmap-om



On se takođe pojavljuje u drugim kinematografskim delima.



**Povratne informacije



Kao sistem administrator, a zatim revizor sajber bezbednosti i pentester, **koristim Nmap gotovo svakodnevno** i **redovno ga preporučujem** sistem administratorima koji žele da ojačaju svoje upravljanje mrežama i poboljšaju svoje dijagnostičke sposobnosti.



### III. Operacija na visokom nivou



Nmap je dostupan za Linux, Windows i macOS. Uglavnom je napisan u C, C++ i Lua (za NSE skripte). Uglavnom se koristi na komandnoj liniji, iako su dostupni i grafički interfejsi kao što je Zenmap. Međutim, snažno vam savetujemo da počnete sa komandnom linijom kako biste bolje razumeli kako funkcioniše.



Jednostavan primer:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Ova komanda će biti detaljno objašnjena kasnije. U ovom vodiču, koristićemo Nmap na Linuxu, ali njegova upotreba je slična i na drugim sistemima. Na Windowsu, Nmap se oslanja na biblioteku **Npcap** (koja zamenjuje sada zastareli WinPcap) za hvatanje i ubrizgavanje mrežnih paketa.



Nmap se koristi kao konvencionalni binarni fajl, kao što su `ls` ili `ip`. Neke napredne funkcije mogu zahtevati povišena prava, jer alat ponekad manipuliše paketima na nekonvencionalne načine kako bi izazvao specifične reakcije na ciljanim sistemima (posebno za detekciju servisa ili ranjivosti).



### IV. Uticaji korišćenja Nmap-a



Pre nego što koristite Nmap, važno je biti svestan njegovog potencijalnog uticaja na mreže i sisteme:





- Može poslati **hiljade ili čak milione paketa** u kratkom vremenskom periodu, što može zasićiti određene mrežne infrastrukture.
- Može generate **malformed ili non-standard** pakete, verovatno da poremeti određenu opremu (posebno industrijske sisteme).
- Može proizvesti **ponašanje slično napadu**, što može pokrenuti upozorenja u sigurnosnim sistemima (vatrozidi, IDS/IPS, itd.).



Generalno govoreći, **Nmap je veoma pričljiv alat**, jer generiše mnogo saobraćaja kako bi izvukao što više informacija. Stoga je preporučljivo potpuno razumeti kako funkcioniše pre nego što se koristi u osetljivim ili produkcionim okruženjima.



### V. Zaključak



Ovaj odeljak uvodi Nmap i njegove glavne karakteristike. Videli smo da je to esencijalni, moćni i fleksibilni alat za mapiranje mreže. Takođe smo razgovarali o tome kako funkcioniše i koje mere predostrožnosti treba preduzeti prilikom njegove upotrebe, kako bismo postavili scenu za naredne delove tutorijala.



## 2 - Zašto koristiti Nmap?



### I. Prezentacija



U ovom odeljku ćemo pogledati glavne upotrebe alata za skeniranje mreže Nmap. Videćemo da je to alat koji se široko koristi u mnogim kontekstima i profesijama, i da je imati ga u svom alatu i znati kako ga savladati definitivno korisna veština.



### II. Korišćenje Nmap-a za dijagnostiku i nadzor



Nmap se može koristiti za dijagnostiku mreže i, šire gledano, za nadgledanje. Na isti način na koji se ping može koristiti za utvrđivanje da li dva hosta komuniciraju, Nmap se može koristiti za brzo utvrđivanje da li je host aktivan ili da li određena usluga funkcioniše. Zahvaljujući [Nmap-u](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap"), možemo dobiti precizne podatke o vremenu odziva hosta, putanji koju paketi prelaze, odgovoru koji daje određena usluga, itd.



Sledeća komanda i rezultat mogu se koristiti, na primer, da se brzo utvrdi da li je veb server na hostu **192.168.1.18** aktivan i ispravno odgovara:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Koristi Nmap za preuzimanje statusa web servisa sa udaljenog servera.*



Dakle, korišćenje Nmap-a ide dalje od čuvenog "ping testa" tokom faza debagovanja ili dijagnostike. Videćemo kasnije da postoji nekoliko metoda koje Nmap koristi da identifikuje koja usluga sluša na datom portu, uključujući i njenu verziju.



### III. Korišćenje Nmap-a za mapiranje mreže



Kao _Network Mapper_, mapiranje mreže je glavni cilj ovog alata. Može se koristiti unutar lokalne mreže, ili preko više mreža, podmreža i VLAN-ova, da bi se naveli svi dostupni hostovi i servisi. Nmap čini ovaj zadatak mnogo bržim i efikasnijim od bilo koje ručne metode.



Na primer, sledeća komanda se može koristiti za brzo identifikovanje aktivnih hostova na mreži **192.168.1.0/24**:



```
nmap -sn 192.168.1.0/24
```



*Napomena: opcija `-sP` je zastarela i zamenjena je sa `-sn`.*



![nmap-image](assets/fr/03.webp)



*Korišćenje Nmap-a za otkrivanje dostupnih hostova na mreži*



Videćemo kasnije da postoji nekoliko metoda koje Nmap koristi da utvrdi da li se host može smatrati "aktivnim", čak i ako a priori ne izlaže nikakve usluge.



### IV. Korišćenje Nmap-a za evaluaciju politike filtriranja



Nmap ima prednost što je činjeničan: njegovi rezultati omogućavaju uspostavljanje konkretnih nalaza, za razliku od bilo kog dokumenta o arhitekturi ili politike filtriranja. To je ključni alat za procenu efikasnosti kompartmenalizacije informacionog sistema, jer vam omogućava da **proverite da li se politika filtriranja zaista primenjuje**.



U korporativnoj mreži, najbolja praksa nalaže da sistemi budu segmentirani prema svojoj ulozi, kritičnosti ili lokaciji. Pravila filtriranja (često implementirana putem vatrozida) moraju ograničiti komunikaciju između zona. Ali ove konfiguracije su često složene i sklone greškama.



Dakle, da biste potvrdili da je politika poštovana, ništa ne nadmašuje konkretan test. Na primer, možete proveriti da li osetljive administrativne usluge (SSH, WinRM, MSSQL, MySQL, itd.) nisu dostupne iz korisničke zone.



Korišćenje **Nmap-a za testiranje politike filtriranja** treba da bude sistematsko pre nego što se takva politika uvede u produkciju. Nažalost, ova provera se često zanemaruje.



Iz mog iskustva, mnoge greške u konfiguraciji ostaju neprimećene u odsustvu testova validacije. Jednostavna greška u IP opsegu ili previd u pravilima može ostaviti navodno izolovanu zonu ranjivom.



### V. Korišćenje Nmap-a za bezbednosni audit i penetraciono testiranje



Nmap ima **mnoge korisne funkcije za procenu bezbednosti**, testiranje penetracije (pentests), i nažalost takođe za napadače.



Funkcije otkrivanja mreže su ključne za napadača, koji treba da razume topologiju mreže nakon početnog kompromitovanja. Ali Nmap nudi mnogo više od toga: integriše skriptni mehanizam, **od kojih su mnogi posvećeni otkrivanju ranjivosti**.



Na primer, ova komanda se može koristiti za proveru da li FTP servis dozvoljava anonimnu konekciju, bez potrebe za ručnim povezivanjem:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Korišćenje NSE skripte za proveru anonimne FTP autentifikacije putem Nmap-a.*



Nmap otkrivanje ranjivosti je jedan od prvih koraka u reviziji ili testu penetracije. Omogućava vam brzo prepoznavanje određenih slabih tačaka i optimizaciju vaših analiza.



Ali pazite: **alatke za skeniranje ranjivosti imaju svoja ograničenja**. Nmap pokriva samo deo pretnji i ne garantuje da je sistem bezbedan ako se ne otkriju problemi. Stoga je neophodno **razumeti kako korišćeni skripti funkcionišu** i ne oslanjati se isključivo na njihov sud.



### VI. Zaključak



Videli smo da savladavanje Nmap-a može pokriti širok spektar slučajeva upotrebe, od dijagnostike i nadgledanja do mapiranja, evaluacije sigurnosnih politika i skeniranja ranjivosti. U sledećem delu, preći ćemo na suštinu i instalirati Nmap.




## 3 - Instaliranje i konfigurisanje Nmap-a



### I. Prezentacija



U ovom odeljku ćemo naučiti kako instalirati alat za mrežno skeniranje Nmap na Linux i Windows operativne sisteme. Na kraju ovog odeljka, imaćemo sve što nam je potrebno da počnemo koristiti Nmap za buduće module. Na kraju, videćemo koje privilegije može zahtevati kada se koristi i zašto.



### II. Instaliranje Nmap-a na Linux-u



Nmap je prvobitno dizajniran da radi na GNU/Linux operativnim sistemima. Kao rezultat toga, i zahvaljujući svojoj dugovečnosti i popularnosti, naći ćete ga u svim zvaničnim repozitorijumima glavnih Unix distribucija. U ovom uputstvu, koristiću operativni sistem zasnovan na Debian-u [Kali Linux](https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Ali možete ga koristiti na potpuno isti način sa klasičnim Debian-om, CentOS-om, Red Hat-om ili bilo kojim drugim!



Pod Debianom, da biste proverili da li je Nmap prisutan u vašim trenutnim repozitorijumima, možete koristiti sledeću komandu:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



Odgovor ovde jasno ukazuje da paket "nmap" postoji u repozitorijumima (ovde, onima Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). Od sada, možete instalirati Nmap putem uobičajenih komandi za instalaciju, ništa razoružavajuće za sada 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Da bismo proverili da je Nmap ispravno instaliran, prikazaćemo njegovu verziju:



```
nmap --version
```



Evo očekivanog rezultata:



![nmap-image](assets/fr/05.webp)



rezultat prikazivanja trenutne verzije Nmap._



Imajte na umu prisustvo biblioteke "libpcap" (_Packet Capture Library_) i njene verzije u ovom prikazu. Takođe korišćena od strane Wireshark-a, "libpcap" koristi Nmap za kreiranje i manipulaciju paketima i osluškivanje mrežnog saobraćaja.



### III Installing Nmap on Windows



Da biste instalirali na Windows operativni sistem, počnite preuzimanjem binarne datoteke sa zvaničnog sajta (i ni jednog drugog!):





- Stranica za preuzimanje Nmap-a na zvaničnom sajtu: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




Zatim ćete morati preuzeti binarni fajl nazvan `nmap-<VERSION>-setup.exe`:



![nmap-image](assets/fr/06.webp)



stranica za preuzimanje instalacionog binarnog fajla nmap za Windows



Kada imate ovaj binarni fajl na vašem sistemu, jednostavno ga pokrenite da instalirate Nmap. Ovo je jednostavna instalacija i možete ostaviti sve opcije kao podrazumevane.



Moj refleks je da odznačim polje "zenmap (GUI Frontend)". Ovo je grafički Interface za Nmap koji ne koristim i neće biti pokriven u ovom vodiču, ali slobodno ga isprobajte kada savladate Nmap alatku za komandnu liniju!



![nmap-image](assets/fr/07.webp)



opciono isključivanje Zenmap-a prilikom instalacije Nmap-a na Windows-u



Na kraju instalacije Nmap-a, predlaže se druga instalacija: ona biblioteke "Npcap":



![nmap-image](assets/fr/08.webp)



instalacija biblioteke "Npcap" prilikom instalacije Nmap-a na Windows-u



Ovo je biblioteka na kojoj se Nmap oslanja za upravljanje mrežnim komunikacijama, tj. za kreiranje, slanje i primanje mrežnih paketa. Verovatno ste već naišli na ovu biblioteku ako koristite Wireshark na Windows-u, pošto je i on koristi i zahteva instalaciju.



Kao i kod Linux-a, možete potvrditi da je Nmap instaliran otvaranjem Command Prompt-a ili [Powershell] terminala (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") i unosom sledeće komande:



```
nmap --version
```



Evo očekivanog rezultata:



![nmap-image](assets/fr/09.webp)



rezultat prikazivanja trenutne verzije Nmap._



Nmap je sada instaliran na Windows. Možete ga koristiti na potpuno isti način kao na Linuxu, prateći ovaj vodič.



### IV. Lokalni privilegiji potrebni za korišćenje Nmap-a



Ali uzgred, kada koristite Nmap, **da li je neophodno imati povišene lokalne privilegije na sistemu?** Odgovor je: **zavisi**.



U svom vrlo osnovnom obliku, tj. bez preteranog korišćenja njegovih opcija, Nmap ne zahteva nužno privilegovana prava. Međutim, uskoro ćete shvatiti da je bolje koristiti Nmap u privilegovanom kontekstu ("root" pod Linux-om, "administrator" ili ekvivalent pod Windows-om) kako biste mogli da ga koristite u punom potencijalu, uz rizik dobijanja poruke o grešci poput ove:



![nmap-image](assets/fr/10.webp)



poruka o grešci pod Linuxom kada Nmap opcije zahtevaju root prava._



Bilo na Linuxu ili Windowsu, postoji mnogo slučajeva kada će Nmap tražiti privilegovan pristup. Glavni razlozi su sledeći (neiscrpna lista):





- Kreiranje "sirovih" mrežnih paketa**: Nmap je sposoban za širok spektar metoda skeniranja, uključujući naprednu manipulaciju i kreiranje paketa. Ovo je slučaj, na primer, kada želimo da izvršimo TCP SYN skeniranja, koja ne poštuju klasični _Three-way handshake_ TCP razmene. Da bi to uradio, Nmap mora koristiti funkcije koje nisu nativne za operativne sisteme, koji znaju samo kako da poštuju dobre prakse u mrežnim komunikacijama (poziva se na biblioteke "Npcap" i "libcap" koje su gore pomenute). Zbog toga što Nmap ne radi stvari na "standardni" način, u stanju je da zaključi određene informacije o operativnim sistemima, servisima i određenim ranjivostima.





- Slušajte mrežni saobraćaj**: neke od Nmap opcija zahtevaju da sluša mrežu kako bi dobio određene informacije. Ova akcija se smatra osetljivom na operativnim sistemima, jer takođe omogućava slušanje komunikacija drugih aplikacija na sistemu. Baš kao i Wireshark, Nmap zahteva specifične privilegije za ovo, koje je lakše dobiti direktnim pristupom privilegovanoj sesiji.





- Slušanje na privilegovanim portovima**: na operativnim sistemima, portovi od 0 do 1024 (TCP kao i UDP) se smatraju privilegovanim, tj. oni su na neki način rezervisani za vrlo specifične upotrebe i stoga zaštićeni. Iako je ovo donekle zastareo razlog danas, i dalje je potrebno imati određene privilegije za slušanje na ovim portovima, što Nmap možda mora da uradi u zavisnosti od toga kako će se koristiti.





- Slanje UDP paketa:** Slično tome, slušanje mrežne aplikacije na UDP portovima (protokol bez stanja) zahteva privilegovana prava na operativnim sistemima. Privilegovana sesija će stoga biti potrebna ako želite da izvršite UDP skeniranje, za koje će Nmap morati da sluša odgovor kako bi analizirao odgovore na svoja skeniranja.




Da budemo precizniji, moguće je, barem na Linuxu, pokrenuti Nmap sa svim njegovim funkcijama i opcijama bez potrebe da budete root. Ovo se postiže dodeljivanjem pravih _sposobnosti_ binarnoj datoteci. Međutim, ovo zahteva naprednu manipulaciju i možda nije tako praktično kao pokretanje Nmap-a direktno sa privilegijama. Takođe, ovaj pristup je manje uobičajen i može predstavljati sigurnosne probleme ako nije pravilno konfigurisan.



Međutim, ovo je malo odstupanje od našeg Nmap tutorijala, pa ćemo to za sada izostaviti.



Za ostatak ovog vodiča, pretpostavite da se Nmap uvek pokreće kao "root" (iz ljuske kao "root" ili putem "sudo" komande), ili u administratorskom terminalu pod Windows-om, čak i ako to nije naznačeno. U suprotnom, možete iskusiti suptilne, ali primetne razlike u odnosu na vodič.



### V. Zaključak



To je to! Nmap je sada instaliran na našem operativnom sistemu i spreman za korišćenje, bez potrebe za daljom konfiguracijom. Ovaj deo zaključuje uvod i prezentaciju Nmap-a. Nadam se da vam je probudio interesovanje i da ste željni da počnete sa vežbanjem.



Na ozbiljniju notu, sada imamo bolju ideju o tome šta je Nmap alat za mapiranje i koja su njegova najčešća upotreba, kao i njegova ograničenja. Idemo dalje!




## 4 - TCP i UDP skeniranje portova sa Nmap



### I. Prezentacija



U ovom odeljku ćemo naučiti kako da izvršimo naše prve skeniranje portova koristeći alat za mrežno skeniranje Nmap. Videćemo kako da ga koristimo za sastavljanje liste mrežnih servisa izloženih na hostu, bilo da koristimo TCP ili UDP protokole.



Od sada, zapamtite da skenirate samo hostove u kontrolisanom okruženju za koje imate eksplicitnu autorizaciju.





- Kao podsetnik: [Krivični zakonik: Poglavlje III: Napadi na sisteme za automatsku obradu podataka](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Ako nemate nijedno pri ruci**, preporučujem sledeća besplatna rešenja, koja su upravo ono što vam treba!





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Platforma za obuku hakovanja, Hack The Box konstantno pruža ranjive sisteme koje možete napadati kako vam odgovara. Dostupno je nekoliko stotina sistema, ali obnovljeni skup od 20 mašina se nudi besplatno tokom cele godine, sa pristupom putem OpenVPN VPN-a.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: Ova platforma nudi brojne namerno ranjive sisteme za preuzimanje, koji se mogu koristiti putem VirtualBox-a (takođe besplatno rešenje) ili na druge načine. Kada se preuzmu, nije potreban VPN - sve je lokalno.




Takođe, slobodno **kreirajte virtuelnu mašinu** na vašem omiljenom operativnom sistemu i instalirajte razne servise na njoj kao testne mete. Prednost ovde je što ćete takođe moći da vidite šta se dešava na serverskoj strani tokom skeniranja, posebno sa Wireshark-om, i da imate kontrolu nad lokalnim firewall-om kada budemo radili naprednije testove.



Hajde da budemo praktični!



### II. Skeniranje TCP portova hosta putem Nmap-a



#### A. Prvo TCP skeniranje portova sa Nmap-om



Sada ćemo izvršiti naše prve skeniranja putem Nmap-a. Naš cilj je jednostavan: želimo saznati koje usluge su izložene od strane web servera koji smo upravo postavili, kako bismo videli da li postoji nešto neočekivano, kao što je administrativna usluga koja ne bi trebala biti dostupna, ili izloženost porta aplikacije za koju smo mislili da je povučena iz upotrebe.



U mom primeru, host koji treba skenirati ima IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Evo mogućeg rezultata. Vidimo klasičan Nmap povratak sa puno informacija:



![nmap-image](assets/fr/11.webp)



rezultati jednostavnog TCP skeniranja izvedenog pomoću Nmap._



Brzim pregledom ovog rezultata, razumemo da su portovi TCP/22 i TCP/80 dostupni na ovom hostu.



Podrazumevano, i ako mu ne kažete drugačije, Nmap će skenirati samo TCP portove.



#### B. Razumevanje rezultata jednostavnog Nmap skeniranja



Hajde da odemo korak dalje, međutim, da bismo razumeli ovaj izlaz: svaki red je važan, prvo da bismo znali šta je upravo urađeno, a drugo da bismo pravilno protumačili same rezultate skeniranja.



Prva linija je u suštini podsetnik na verziju skeniranja i datum (korisno za evidentiranje i arhiviranje na kraju!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



Druga linija prikazuje početak rezultata skeniranja za host "debian.home (192.168.1.19)". Ove informacije će biti korisne kada počnemo skenirati više hostova istovremeno:



```
Nmap scan report for debian.home (192.168.1.19)
```



Treći red nam govori da je dotični host "Up", tj. aktivan:



```
Host is up (0.00022s latency).
```



Konačno, Nmap nas obaveštava da 998 TCP portova identifikovanih kao zatvoreni nisu prikazani u:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Ovo nam štedi skoro 1.000 linija izlaza koji izgledaju kao:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Hvala njemu što nas je poštedeo ovoga!



Zašto 998 "zatvorenih" portova? Dodavanje 2 otvorena porta čini 1000, a to je broj portova koje će Nmap skenirati u svojoj podrazumevanoj konfiguraciji, a ne 65535 postojećih TCP portova! Videćemo kasnije da je ovo potpuno i lako prilagodljivo. Ali ako ciljani host ima servis koji sluša na prilično egzotičnom portu, ovo "podrazumevano" skeniranje ga neće otkriti.



Prateći ove informacije, nalazimo ono što je najzanimljivije: tabelu organizovanu prema tri kolone "PORT - STATE - SERVICE":





- Prva kolona "PORT" jednostavno označava ciljani port/protokol, i ovde je važno pogledati da li je to TCP port (`<port>/tcp`) ili UDP (`<port>/udp`).





- Kolona "STATE" označava status mrežne usluge otkrivene na ovom portu i određene od strane Nmap-a na osnovu dobijenog odgovora. Ovo može biti "open", "closed", "filtered" ili "unknown". Kasnije ćemo videti kako Nmap razlikuje ova različita stanja.





- Kolona "SERVICE" označava uslugu izloženu na dotičnom portu. Imajte na umu, međutim, da ovde nismo koristili opcije aktivnog otkrivanja usluga. Nmap se oslanja na lokalnu referencu između porta/protokola i navodno dodeljene usluge: datoteku "/etc/services"




Ako pogledate datoteku "/etc/services" na Linux sistemu, pronaći ćete vezu "port/protokol - usluga" sličnu onoj koju prikazuje Nmap:



![nmap-image](assets/fr/12.webp)



izvlači sadržaj datoteke "/etc/services" pod Linuxom._



Važno je razumeti da, za sada, Nmap nije izvršio nikakvo aktivno otkrivanje servisa. Na primer, ne bi bio u mogućnosti da identifikuje SSH servis iza TCP/80 porta da je to bio slučaj. Otuda važnost poznavanja kako koristiti prave opcije - uskoro dolazi!



Znati kako interpretirati izlaz Nmap-a je važan deo savladavanja ovog alata. Dobra vest je da će ovaj izlaz uglavnom biti isti, bez obzira na opcije koje koristite.



#### C. Ispod haube: analiza mreže pomoću Wireshark-a



Ako pažljivo pogledate šta se dešava na mreži Interface hosta koji skenira server, ili na samom serveru, Nmap-ove akcije će biti mnogo jasnije. To je ono što ćemo ovde uraditi.



Ono što vam ovde mogu pokazati je samo deo onoga što je vidljivo u Wireshark-u. Ako želite da idete dalje, slobodno sami izvršite mrežno snimanje tokom skeniranja, a zatim pregledajte ono što je snimljeno.



U ovom testu, moj skenirajući host (192.168.1.18) i moj ciljni host (192.168.1.19) su na istoj lokalnoj mreži.



Nmap započinje proverom da li je ciljni host aktivan na lokalnoj mreži slanjem ARP zahteva. Ako primi odgovor, zna da je host aktivan i započinje skeniranje mreže:



![nmap-image](assets/fr/13.webp)



_ARP zahtev izdat od strane Nmap-a da utvrdi da li je ciljni host prisutan na lokalnoj mreži._



Ako je host koji treba skenirati na udaljenoj mreži, Nmap započinje slanjem ping zahteva i pokušava da dosegne neke od najčešće izloženih portova (TCP/80, TCP/443):



![nmap-image](assets/fr/14.webp)



ping zahtev izdat od strane Nmap-a da se utvrdi da li je ciljni host dostupan na udaljenoj mreži



Ako dobije odgovor na bilo koji od ovih testova, smatra da je cilj aktivan.



Kada Nmap utvrdi da je njegova meta aktivna, pokušaće da razreši njen naziv domena sa DNS serverom konfigurisanim na mrežnoj kartici:



![nmap-image](assets/fr/15.webp)



rezolucija dNS na cilj skeniranja Nmap



Sada kada je Nmap identifikovao svoju metu i zna da je aktivna, započinje svoj TCP port skeniranje:



![nmap-image](assets/fr/16.webp)



prenos tCP SYN paketa i prijem RST/ACK tokom Nmap skeniranja



Da bi to uradio, na svakom TCP portu u svom podrazumevanom opsegu, **poslaće TCP SYN pakete i čekati odgovor**. Na gornjem snimku ekrana, prima TCP RST/ACK pakete od skeniranog servera, što znači "idi dalje, ovde nema ničega" - drugim rečima, ovi portovi su zatvoreni. Kao što smo videli u rezultatu, ovo će biti slučaj za većinu skeniranih portova. Sa dva izuzetka:



![nmap-image](assets/fr/17.webp)



odgovor na TCP SYN paket poslat na port 22, aktivan na cilju skeniranja



Na snimku ekrana iznad, vidimo TCP SYN/ACK paket poslat od strane ciljnog hosta**. Port je aktivan i izlaže uslugu. Nmap potvrđuje prijem odgovora, zatim prekida vezu (TCP RST/ACK). **Ovako je znao da je port TCP/22 aktivan**.



Videli smo ovde da Nmap poštuje "Three Way Handshake" prilikom skeniranja TCP mreže. Iz razloga performansi, moguće je tražiti od njega da ne odgovara na povratak servera, čime se štedi nekoliko hiljada paketa prilikom skeniranja velike mreže. Ali ćemo pogledati ove opcije i optimizacije kasnije u tutorijalu.



Sada imamo bolju ideju o tome kako izvršiti TCP skeniranje i šta se zapravo dešava kada se ono obavlja. Takođe smo videli da, po default-u, Nmap izvršava TCP skeniranje portova na ograničenom broju portova.



### III. Skeniranje UDP portova pomoću Nmap-a



#### A. Prvo UDP skeniranje porta sa Nmap



Sada da vidimo kako da skeniramo UDP portove hosta. Kao što smo videli, Nmap će po defaultu uvek skenirati TCP portove. Ovo može značiti propuštanje mnogo informacija ako nismo svesni toga.



Kao podsetnik, za potrebe ovog testa, moj skenirajući host (192.168.1.18) i moj ciljni host (192.168.1.19) su na istoj lokalnoj mreži.



```
nmap -sU 192.168.1.19
```



Ovde, povratna vrednost ima isti format kao za TCP skeniranje, ali aktivne usluge prikazane su u formatu `<port>/UDP`, kako je traženo!



![nmap-image](assets/fr/18.webp)



rezultat jednostavnog UDP skeniranja izvedenog pomoću Nmap._



Opcija "-sU" se koristi da se Nmap-u kaže da želite raditi na UDP, umesto na TCP što je podrazumevano.



Usput, verovatno ćete primetiti da Nmap zahteva "root" prava za UDP skeniranja, kao što je ranije pomenuto u tutorijalu.



napomena: Od najnovijih verzija Nmap-a, uvek se preporučuje pokretanje UDP skeniranja sa administratorskim privilegijama kako bi se osigurali pouzdani rezultati, jer neke funkcije zahtevaju sirovi pristup mrežnim soketima._



UDP skeniranja mogu trajati veoma dugo (1100 sekundi za skeniranje 1000 portova u mom primeru), zbog odsustva "Three Way Handshake" u UDP-u, što znači da će Nmap čekati povratnu informaciju za svaki poslati UDP paket, i odrediće da je port "zatvoren" samo ako nema povratne informacije nakon određenog vremena (timeout). Ovaj odgovor od skeniranih hostova nije sistematičan i često je ograničen u smislu broja odgovora po sekundi, kako bi se izbegli određeni napadi amplifikacije. Ovo je u suprotnosti sa TCP-om, gde postoji trenutni odgovor od skeniranog hosta, bilo da je port otvoren ili zatvoren. Kasnije ćemo videti kako da ovo optimizujemo.



Druga poteškoća sa UDP je **da servisi ne odgovaraju uvek na dolazne pakete**, jednostavno zato što to nije uvek neophodno i to je princip UDP-a. Kada je to slučaj, i kada se ne primi ICMP "port unreachable", servis je označen kao "open|filtered" od strane Nmap-a, kao što je prikazano na gornjem snimku ekrana.



#### B. Ispod haube: analiza mreže putem Wireshark-a



Kao i kod našeg TCP skeniranja, hajde da detaljnije pogledamo šta se dešava na mrežnom nivou tokom UDP skeniranja koristeći Wireshark analizu. Nmap-ovo ponašanje u određivanju da li je host aktivan je isto.



Jedina stvarna razlika prilikom skeniranja UDP-a je ta što Nmap neće čekati na "Three Way Handshake", budući da ovaj mehanizam ne postoji u UDP-u (protokol bez stanja):



![nmap-image](assets/fr/19.webp)



Prenos uDP paketa i prijem ICMP (port nedostupan) tokom Nmap skeniranja



Možemo videti na gornjem snimku ekrana da će Nmap poslati veliki broj UDP paketa, i primiti za većinu njih ICMP paket "Destination unreachable (Port unreachable)" kao odgovor. Ovo je normalno, jer je to odgovarajući odgovor definisan od strane [RFC 1122](https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") kada je UDP port nedostupan:



![nmap-image](assets/fr/20.webp)



izvod iz RFC 1122._



Hajde da detaljnije pogledamo ovaj Wireshark snimak, koji prikazuje **tri moguća scenarija** u UDP:



![nmap-image](assets/fr/21.webp)



snimanje mreže tokom UDP skeniranja na različitim portovima pomoću Nmap._



Tri slučaja su sledeća:





- Prvi Exchange se sastoji od paketa br. 3, 4 i 8, 9. Nmap šalje UDP pakete na klasični SNMP port i stoga **unapred konstruiše pakete u skladu sa protokolom**. Zatim dobija odgovor od servera (paketi br. 8 i 9). Rezultat: Nmap je primio odgovor, usluga je "otvorena".





- Drugi Exchange se sastoji od paketa 6 i 7. Nmap šalje "prazan" UDP paket (bez strukture protokola) na port UDP/165, i prima ICMP paket kao odgovor: "Destination unreachable (Port unreachable)". Rezultat: Nmap je primio (negativan) odgovor, host je aktivan, ali usluga koju je pokušao da dosegne nije operativna na ovom portu, koji će biti označen kao "zatvoren".





- Poslednji Exchange se sastoji od paketa br. 12: Nmap šalje "prazan" UDP paket na port UDP/1235. Nema odgovora, čak ni eksplicitnog odbijanja od skeniranog hosta. Rezultat: Nmap označava port kao "open|filtered", jer nije u mogućnosti da utvrdi da li je to zbog prisustva firewall-a, koji je konfigurisan da ne odgovara, ili zbog aktivne UDP usluge koja ionako ne vraća odgovor (nije obavezno u UDP).




Evo rezultata prikazanog od strane Nmap-a nakon ova tri slučaja:



![nmap-image](assets/fr/22.webp)



mogući rezultati UDP skeniranja izvedenog putem Nmap._



Sada imamo bolju ideju o tome kako izvršiti UDP skeniranje i šta se zapravo dešava kada se ono izvrši. Do sada smo koristili Nmap na vrlo jednostavan način, bez stvarnog odlučivanja koje portove skenirati, ali to će se uskoro promeniti!



### IV. Fino podešavanje skeniranja portova sa Nmap-om



#### A. Podsetnik podrazumevanog ponašanja Nmap-a



Kao što smo videli, Nmap sam bira broj i portove za skeniranje ako ne navedete nikakve opcije. Ovo je "podrazumevana" konfiguracija koju Nmap koristi kada mu ne kažete tačno šta da radi. Ove podrazumevane opcije su dizajnirane da daju ideju o glavnim izloženim portovima, pri čemu se biraju prema učestalosti izloženosti (najčešći ili najfrekventniji portovi) umesto po numeričkom redu (port 1, 2, 3, itd.) i takođe da izbegnu pokretanje skeniranja svih 65535 mogućih portova ako ne navedete odgovarajuće opcije, što bi bilo predugo i preopširno za "podrazumevani" slučaj upotrebe.



**Kako se biraju ovi portovi?



1000 portova skeniranih u podrazumevanom režimu biraju se prema učestalosti pojavljivanja. Ove statistike održava Nmap i ažuriraju se na isti način kao i sam binarni fajl i njegovi skripti (moduli). Možete sami pogledati ove statistike u datoteci "/usr/shares/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



izvučeno iz datoteke "/usr/shares/nmap/nmap-services"._



Ovde, u trećoj koloni, vidimo nešto što izgleda kao verovatnoće (između 0 i 1) ili procentualna distribucija. Ovo je učestalost pojavljivanja svakog para port/protokol. Možemo videti da najpoznatiji portovi (FTP, SSH, TELNET i SMTP u ovom izvodu) imaju mnogo veću vrednost od ostalih.



#### B. Precizno odredite ciljne portove za Nmap skeniranje



Međutim, u stvarnom svetu, možda ćemo morati da skeniramo samo određeni port, ili nekoliko portova, ili određeni opseg portova. Nmap olakšava upravo to, na jedinstven način za oba UDP i TCP skeniranja.



**Skeniraj određeni port putem Nmap-a**



Ako želimo da skeniramo jedan port, a ne 1000, možemo specificirati ovaj port putem Nmap opcije "-p" ili "--port":



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Kao rezultat toga, skeniranje će prirodno biti mnogo brže i Nmap će emitovati samo pakete potrebne da se otkrije da li je host aktivan, a zatim da li je navedeni port dostupan. Ovo štedi vreme ako samo želite brzo da proverite da li je veb servis na vašem sajtu za prikazivanje i dalje dostupan.



**Skeniraj više portova pomoću Nmap-a**



Na isti način, možemo navesti nekoliko portova za Nmap, koristeći istu opciju i spajajući navedene portove zarezom:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Bez obzira na redosled, Nmap će proveriti sve ove portove, i to samo one na ciljanom hostu. Primetićete u Nmap-ovom izlazu da nam **izričito govori sve portove i njihov status**, čak i ako su "zatvoreni". Za razliku od podrazumevanog ponašanja, gde bi ovaj kompletan izlaz zauzeo previše prostora:



![nmap-image](assets/fr/24.webp)



*Rezultat Nmap TCP skeniranja na naznačenim portovima.*



**Skeniraj opseg portova



Ako je broj portova koje želite skenirati prevelik, možete ih navesti po opsegu, na primer:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Naravno, možete kombinovati i uklapati kako vam odgovara, na primer:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**Skeniranje TCP i UDP portova



Takođe možete istovremeno izvršiti UDP i TCP skeniranja na odabranim portovima:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



Primetićete u ovom poslednjem primeru prisustvo "U:" za označavanje UDP porta i "T:" za označavanje TCP porta. Evo mogućeg izlaza ovog tipa skeniranja:



![nmap-image](assets/fr/25.webp)



*Rezultat TCP i UDP skeniranja portova pomoću Nmap-a.*



Sada je to zanimljiv način da prilagodite svoje skeniranje!



**Skeniraj sve portove



Konačno, moguće je specificirati mnogo veće ili manje opsege za Nmap. Videli smo da podrazumevana lista koju bira Nmap sadrži 1000 portova. Takođe možemo tražiti 100 najčešćih portova, ili 200 najčešćih, koristeći opciju "--top-ports":



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Konačno, možemo ga zamoliti da skenira sve moguće portove (svih 65535), koristeći oznaku "-p-":



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Ovo drugo će potrajati duže, posebno sa UDP, ali ćete biti sigurni da nećete propustiti nijedan otvoreni port.



*Napomena: Opcija "-p-" je preporučeni metod za skeniranje svih TCP portova. Za UDP skeniranja, preporučuje se ograničavanje broja portova zbog performansi, jer kompletna skeniranja svih UDP portova mogu trajati veoma dugo.*



Kasnije u vodiču, videćemo kako da optimizujemo brzinu Nmap skeniranja da odgovara našim potrebama, što će biti posebno korisno za skeniranja na svim TCP i UDP portovima.



### V. Zaključak



U ovom odeljku konačno smo dobili praktičnu vežbu, tako da sada znamo **kako koristiti Nmap na osnovni način za skeniranje TCP i UDP portova hosta**. Takođe smo detaljno pogledali šta se dešava na mrežnom nivou i **kako Nmap određuje da li je TCP ili UDP port aktivan ili ne**. Na kraju, znamo kako precizno odabrati portove koje želimo skenirati i **šta Nmap-ove podrazumevane opcije zapravo rade**. U nastavku ćemo ponovo koristiti ovo znanje i primeniti ga na skeniranje cele mreže, uključujući globalno mapiranje i otkrivanje mreže.




## 5 - Mapiranje i otkrivanje mreže pomoću Nmap-a



### I. Prezentacija



U ovom odeljku ćemo naučiti kako koristiti alat za mrežno skeniranje Nmap za mapiranje vaše mreže. Videćemo koliko može biti efikasan u ovom zadatku, kroz njegove različite opcije. Na kraju, pogledaćemo različite načine specificiranja ciljeva naših skeniranja za Nmap.



Posebno ćemo koristiti ono što smo naučili u prethodnom odeljku o tome kako Nmap određuje da li je host aktivan i dostupan.



Kao što je pomenuto u uvodu u Nmap, ovo je Mrežni Mapper. Kao takav, to je savršen alat za sastavljanje liste dostupnih hostova na mreži, bilo lokalnoj ili udaljenoj.



**Povratak autora:**



Zapravo, kao revizor sajber bezbednosti i pentester, sistematski koristim Nmap prilikom sprovođenja internih penetracionih testova kako bih saznao gde se nalazim, ko su moji susedi na lokalnoj mreži i koje su druge mreže dostupne, kao i sistemi koji se na njima nalaze. Moj cilj je jednostavan: mapirati mrežu, odrediti veličinu informacionog sistema i, posebno, skicirati njegovu površinu napada.



Mapiranje mreže može biti korisno i u kontekstu dijagnostike mreže, nadzora, mapiranja resursa (da li ste zaista sigurni da se vaš IS sastoji isključivo od onoga što je u Active Directory ili u vašem GLPI/OCS Inventaru? Takođe se može koristiti za detekciju prisustva Shadow IT-a u vašem informacionom sistemu.



### II. Korišćenje Nmap-a za skeniranje opsega mreže



#### A. Otkrivanje mreže pomoću Nmap skeniranja



Sada bismo želeli da pređemo na viši nivo i analiziramo celu našu lokalnu mrežu. Ništa nije jednostavnije: sve što treba da uradimo je da ponovo upotrebimo komande koje smo videli u prethodnom odeljku, ali da navedemo CIDR umesto jednostavnog IP Address.



CIDR (**Classless Inter Domain Routing**) je "klasična" notacija za specificiranje opsega mreže i njenog obima (koristeći masku). Na primer, "192.168.0.0/24" je "prevođenje" decimalne notacije maske "255.255.255.0".



Da bismo koristili Nmap sa specificiranim CIDR-om, možemo ga koristiti na sledeći način:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



Takođe je moguće, kao sa portovima u prethodnom odeljku, navesti više hostova, više mreža ili opseg:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Evo primer rezultata koje bismo mogli dobiti prilikom pokretanja skeniranja na mreži:



![nmap-image](assets/fr/26.webp)



rezultati Nmap skeniranja za mapiranje nekoliko mreža



Posebno, vidimo nekoliko aktivnih domaćina, a svaki odeljak domaćina počinje linijom poput ove:



```
Nmap scan report for <name> (<IP>)
```



Ovo nam omogućava da jasno vidimo na kojeg se domaćina odnose sledeći rezultati. Poslednji red je takođe važan:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Znamo da je, na skeniranim mrežama, Nmap otkrio 5 aktivnih hostova.



#### B. Ispod haube: analiza mreže putem Wiresharka



Sada ćemo detaljnije pogledati šta se dešava na mrežnom nivou tokom otkrivanja mreže koje se izvodi putem Nmap-a.



Kao što smo videli u prethodnom odeljku, Nmap će po defaultu koristiti ARP protokol za detekciju prisustva hostova na lokalnoj mreži:



![nmap-image](assets/fr/27.webp)



ARH paketi uhvaćeni prilikom skeniranja lokalne mreže koristeći Nmap i njegove podrazumevane opcije



Tako je u stanju da detektuje praktično sve hostove na lokalnoj mreži, jer odgovor na ARP zahtev generalno pružaju svi aktivni hostovi na mreži i ne deluje sumnjivo ni na koji način.



Za udaljene mreže, Nmap koristi kombinaciju tehnika:



![nmap-image](assets/fr/28.webp)



iCMP i TCP paketi uhvaćeni prilikom skeniranja udaljene mreže koristeći Nmap i njegove podrazumevane opcije



Da budemo precizniji, Nmap koristi ICMP echo paket (klasičan slučaj pingovanja) i ICMP Timestamp paket, koji se obično koristi za izračunavanje vremena prenosa paketa. Nada se da će dobiti odgovor od hostova na udaljenim mrežama.



Ali postoji više od toga. Možete videti u Wireshark snimku iznad da se **TCP SYN** paketi sistematski šalju na TCP/443 portove svakog potencijalnog hosta na mrežama koje treba skenirati, kao i **TCP ACK** paketi na TCP/80 portu.



**Zašto slati TCP pakete na portove kao deo otkrivanja mreže?**



Slanje SYN paketa na dati port omogućava Nmap-u da **odredi da li servis osluškuje na tom portu**. Ako domaćin odgovori na SYN paket sa SYN/ACK paketom, to ukazuje da je aktivan i da servis osluškuje na tom portu. Nmap stoga pokušava svoju sreću na ovom servisu, **čak i ako nije dobijen odgovor na ping**.



Slanje ACK paketa na dati port omogućava Nmap-u da **utvrdi da li je firewall prisutan na tom hostu**. Ako host odgovori na ACK paket sa RST (Reset) paketom, to ukazuje da je firewall verovatno prisutan na tom hostu i da blokira neželjeni saobraćaj. Host na taj način odaje svoje prisustvo na mreži, čak i ako nije odgovorio na druge zahteve.



Međutim, važno je napomenuti da detekcija vatrozida korišćenjem ove tehnike možda neće biti potpuno pouzdana u svim slučajevima. Neki hostovi mogu generate RST odgovore iz razloga koji nisu povezani sa prisustvom vatrozida, kao što su specifična konfiguracija servisa ili operativnog sistema. Pored toga, moderni vatrozidi mogu biti konfigurisani da ne odgovaraju na pokušaje otkrivanja ovog tipa.



Sada smo prešli dug put i možemo izvršiti osnovno otkrivanje mreže. Sada ćemo pogledati još nekoliko opcija koje će nam omogućiti veću kontrolu nad ponašanjem Nmap-a.



### III. Otkrivanje mreže bez skeniranja portova pomoću Nmap-a



Kao što ste možda primetili, po defaultu Nmap **izvodi skeniranje portova nakon otkrivanja aktivnog hosta**, što dodaje veliku količinu paketa i čekanje na odgovore našem skeniranju. Ako imate 5 hostova na vašoj mreži, Nmap će pokušati da proveri status oko 5,000 portova, što će potrajati duže.



Međutim, moguće je koristiti Nmap opcije za izvođenje **samo otkrivanja aktivnih hostova** na mreži, bez otkrivanja njihovih servisa.



Ako želimo da saznamo samo koji hostovi su dostupni, bez informacija o uslugama i portovima koje izlažu, možemo koristiti opciju "-sn" da izvršimo **samo skeniranje koristeći ICMP Echo (ping) i ARP zahteve**. Drugim rečima, potpuno onemogućiti skeniranje portova:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Evo rezultata Nmap otkrivanja mreže izvedenog bez skeniranja portova:



![nmap-image](assets/fr/29.webp)



Rezultat otkrivanja mreže bez skeniranja portova pomoću Nmap-a.



Već smo pomenuli moguće ograničenja korišćenja ICMP-a samog za otkrivanje hostova (za udaljene mreže). Zato Nmap takođe koristi nekoliko trikova koji mogu otkriti prisustvo vatrozida ili specifične usluge na hostovima. Uz pomoć opcija, možemo ponovo koristiti ove trikove, pa čak ih i proširiti, bez potrebe da ponovo započinjemo kompletno skeniranje portova svakog otkrivenog hosta.



Da bismo to uradili, koristićemo opcije "-PS" (TCP SYN) i "-PA" (TCP ACK), koje će nam omogućiti da navedemo portove koje želimo da pridružimo kao deo našeg otkrivanja hostova, kao i opciju "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Ovo skeniranje već osigurava da je otkrivanje hosta malo potpunije nego sa podrazumevanim opcijama.



Počinjemo da dobijamo prilično sveobuhvatne komande, koristeći više opcija. Ovo je zato što znamo kako Nmap funkcioniše i ograničenja njegovih "podrazumevanih" opcija, koje ponekad mogu da nas navedu da gubimo vreme ili propustimo važne Elements. To je cela poenta uzimanja vremena da ga savladamo!



Da detaljno opišemo opcije naše poslednje narudžbine:





- "`-sn`: onemogućava skeniranje portova za svaki aktivni host otkriven pomoću Nmap-a.





- "`-PP`: omogućava ICMP echo (ping skeniranje) za otkrivanje hostova.





- "`-PS <PORT>`": pošalji TCP SYN paket na naznačeni port(ove) kako bi detektovao bilo koju aktivnu uslugu koja odaje prisustvo hosta koji nije odgovorio na ping.





- "`-PA <PORT>`": pošalji TCP ACK paket na navedene portove da otkriješ bilo koji aktivni firewall koji odaje prisustvo hosta koji nije odgovorio na ping.




U gornjem primeru, navodim portove koje smatram najčešće izloženim u mojim Nmap kontekstima za opciju "-PS". Ovi različiti portovi će zatim biti testirani na svakom hostu, ne da bismo videli da li je servis koji hostuju zaista aktivan, već da bismo videli da li nam to omogućava da otkrijemo host koji nije odgovorio na naš ICMP Echo dok je još uvek aktivan (putem odgovora sa servisa ili firewall-a hosta).



Evo šta se može videti u mrežnom snimanju napravljenom u vreme takvog skeniranja, u ovom slučaju izvod na jednom ciljanom hostu:



![nmap-image](assets/fr/30.webp)



paketi poslati od strane Nmap-a tokom naprednog otkrivanja mreže, bez skeniranja portova



Pronalazimo naše TCP SYN pakete, naš TCP ACK na portu TCP/80 i naš ICMP echo. Nmap će izvršiti sve ove testove za svaki host koji je cilj naše mrežne pretrage.



### IV. Korišćenje fajla sa resursima za ciljanje pomoću Nmap-a



Navođenje ciljeva može se brzo pokazati složenim u stvarnim informacionim sistemima, koji ponekad mogu biti sastavljeni od desetina ili stotina mreža, podmreža i VLAN-ova. Zbog toga je lakše koristiti datoteku kao izvor za Nmap nego ih navoditi jedan po jedan u komandnoj liniji.



Za početak, kreirajte jednostavnu datoteku koja sadrži jedan unos po liniji:



![nmap-image](assets/fr/31.webp)



datoteka koja sadrži jednu metu (host ili mrežu) po liniji



Dalje, možemo koristiti sve do sada viđene Nmap opcije i navesti opciju "-iL <path/file>":



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap će zatim uključiti u svoje skeniranje sve ciljeve sadržane u našoj datoteci.



Ako želite biti sigurni da će svi vaši ciljevi biti uzeti u obzir, možete koristiti opciju "-sL -n". Nmap će tada samo interpretirati CIDR-ove i hostove u datoteci i prikazati ih vama, bez slanja bilo kakvih paketa preko mreže:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Ovo osigurava da je lista hostova za skeniranje tačna.



Jedan poslednji važan savet koji bih želeo da podelim sa vama tiče se **isključenja hosta ili mreže kao dela skeniranja**. Ova potreba za isključenjem hosta može biti neophodna u nekoliko slučajeva, posebno ako želimo da budemo sigurni da **osetljiva komponenta informacionog sistema nije poremećena ili ometena našim skeniranjem**.



Česti primeri takvih potreba su kada kompanija poseduje industrijsku (PLC) ili medicinsku opremu. Takva oprema je ponekad loše dizajnirana i uopšte nije namenjena za primanje loše formatiranih paketa, ili prevelikog broja istih. Iz očiglednih razloga dostupnosti ili poslovnog/ljudskog rizika, poželjno je isključiti ih iz testiranja.



Da bismo isključili IP adrese ili mreže iz našeg skeniranja, možemo koristiti Nmap opciju "--exclude", na primer:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



U ovom primeru, skeniram mrežu "192.168.1.0/24" ali isključujem host "192.168.1.140" koji se tamo nalazi. Nmap neće poslati pakete ovom hostu. Još jedan primer sa isključenjem podmreže:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



Slično tome, skeniram veliku mrežu "10.0.0.0/16", ali mreža "10.0.100.0/24" neće biti skenirana. Ponovo, preporučujem korišćenje opcije "-sL -n" da biste dobili vrlo jasan pregled koji hostovi će biti skenirani, a koji će biti isključeni iz skeniranja, posebno ako radite u osetljivom kontekstu.



### V. Otkrivanje mreže i skeniranje portova



Sada možemo kombinovati ono što smo naučili u ovom delu sa onim što smo naučili u prethodnom delu o opcijama skeniranja portova. Podrazumevano, videli smo da Nmap skenira 1000 najčešćih portova na svakom aktivnom hostu koji otkrije. Videli smo kako da sprečimo ovo ponašanje ako ga ne želimo, ali možemo ga u potpunosti kontrolisati, pa čak i proširiti ako to odgovara našim potrebama.



Na primer, sledeća komanda će proveriti prisustvo servisa koji sluša na portu TCP/22 na svakom skeniranom hostu:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap će prvo izvršiti otkrivanje mreže kako bi naveo aktivne hostove, i za svaki od njih, proveriće da li je prisutan servis na portu TCP/22.



Na isti način, možemo izvršiti kompletno skeniranje svih TCP portova na svakom hostu otkrivenom na mreži "192.168.0.0/24", isključujući host "192.168.0.4" na primer:



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Slobodno kombinujte sve opcije koje smo do sada naučili kako biste ih prilagodili svojim potrebama.



### VI. Zaključak



U ovom odeljku smo videli kako koristiti Nmap za mapiranje mreže koristeći razne opcije. Sada imamo precizno razumevanje ciljeva naših skeniranja, kao i ponašanja Nmap-ovog skeniranja portova i metode otkrivanja hostova. I što je najvažnije, znamo koje su Nmap-ove podrazumevane postavke i ograničenja, i kako koristiti njegove glavne opcije za dalji napredak.



U sledećem odeljku ćemo pogledati mehanizme i opcije za otkrivanje verzija servisa i operativnih sistema koje je skenirao Nmap.




## 6 - Otkrivanje verzija servisa i operativnog sistema pomoću Nmap-a



### I. Prezentacija



U ovom odeljku ćemo naučiti kako koristiti Nmap za otkrivanje i precizno detektovanje verzija servisa i operativnih sistema koje koriste skenirani hostovi. Detaljno ćemo pogledati kako Nmap obavlja ovaj zadatak, kao i ograničenja alata kako bismo bolje razumeli i interpretirali njegove rezultate.



Kao što smo videli u prethodnim delovima ovog tutorijala, podrazumevano, Nmap neće proveravati koji servis je izložen na portovima koje skenira i smatra otvorenim. Dakle, ako slušate web servis na portu TCP/22, Nmap će nastaviti da ga prijavljuje kao otvoren, ali kao `SSH` servis. Ovo je zato što koristi [bazu podataka](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) lokalnu za vaš sistem da bi pronašao vezu između porta/protokola i imena servisa (datoteka `/etc/services/`).



U većini slučajeva, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) će vam pružiti tačne informacije, jer je retko u produkcionom okruženju pronaći takve slučajeve. Međutim, preostali slučajevi će biti situacije gde je klasična usluga ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, itd.) izložena na neklasičnom portu (npr. 2022 za SSH uslugu), u kom slučaju Nmap neće pronaći podudaranje u svojoj lokalnoj bazi podataka, ili ono koje ne odgovara stvarnosti, i propustićete važne informacije.



Srećom, Nmap nudi veoma precizne opcije i mehanizme za otkrivanje koje tačno usluge se mogu skrivati iza otvorenog porta. Čak ima bazu podataka upita i potpisa za identifikaciju tačnih tehnologija i verzija. Pored usluga, Nmap može identifikovati i korišćenu tehnologiju i njenu verziju.



To ćemo razmatrati u ovom odeljku.



### II. Kako otkriti tehnologiju ili verziju



#### A. Podsetnik kako identifikovati tehnologiju ili verziju



Identifying a technology and a version involves retrieving the name of the service, CMS, application or software listening on the targeted port. For example, a web page is managed by a CMS (`WordPress`), run by a web service (`Apache`, IIS, Nginx) and hosted by a server (Linux or Windows). But how do you know which web service is running?



Klasična metodologija za pronalaženje ovih informacija je _banner grabbing_, koja se jednostavno sastoji od lociranja mesta gde usluga u pitanju prikazuje ove informacije i čitanja podataka. Vrlo često, u svojoj podrazumevanoj konfiguraciji ili obradi, usluge prikazuju svoje ime, pa čak i verziju kao prvi odgovor nakon povezivanja.



![nmap-image](assets/fr/32.webp)



prikaži verziju čim se TCP veza uspostavi od strane FTP servisa



Ovde vidimo da jednostavna TCP konekcija sa ovom uslugom putem `telnet` rezultira TCP paketom koji sadrži njenu tehnologiju i verziju.



Jednom kada ste stekli ideju o vrsti usluge s kojom imate posla, možete takođe poslati specifične komande ili zahteve toj usluzi kako biste iz nje izvukli informacije. Ovi zahtevi/komande mogu se takođe slati nasumično (bez sigurnosti da su odgovarajuće za tu vrstu usluge), u nadi da će jedan od njih izazvati odgovor od strane usluge u pitanju.



U drugim, naprednijim slučajevima, potrebno je poslati specifične pakete kako bi se izazvala reakcija, kao što je greška, koja će pružiti detaljne informacije o verziji ili korišćenoj tehnologiji.



Kao što možete zamisliti, Nmap će koristiti sve ove tehnike kako bi pokušao identifikovati tačan tip usluge hostovane na portu, kao i ime njene tehnologije i verziju.



#### B. Razumevanje Nmap sondi i podudaranja



Da bi izvršio sve ove provere na svakom skeniranom portu, Nmap koristi lokalnu bazu podataka koja se često ažurira (baš kao i binarni fajl ili njegovi moduli). Ovo je tekstualni fajl od nekoliko hiljada linija: `/usr/share/nmap/nmap-service-probes`.



Ova datoteka se sastoji od brojnih unosa, svi organizovani oko dva glavna smernice:





- `Probe`: ovo je definicija paketa koji će Nmap poslati u pokušaju da izazove reakciju od servisa koji treba identifikovati. Zamislite to kao slepi pokušaj poput _Hello? Guten Tag? Hello? Um... Buenos Dias možda?_. Čim ciljani servis primi probe koji razume (tj. govori ispravan protokol), odgovoriće Nmap-u, koji će tada imati potvrdu o tipu servisa.





- Podudaranje": ovo su regularni izrazi koje Nmap primenjuje na dobijeni odgovor. Ako slanje HTTP GET zahteva izazove odgovor od servisa, primeniće desetine regularnih izraza na taj odgovor kako bi identifikovao prisustvo, na primer, reči `Apache`, `Nginx`, `Microsoft IIS`, itd.




Postoji još nekoliko direktiva za specifične slučajeve, ali glavne za razumevanje kako Nmap funkcioniše i prilagođavanje njegove upotrebe su ove. Da bi ovaj teorijski deo bio konkretniji, evo primera:



![nmap-image](assets/fr/33.webp)



primer sonde u Nmap-ovoj datoteci `/usr/share/nmap/nmap-service-probes`



U prvom redu ovog primera, vidimo lako razumljiv Probe nazvan `GetRequest`. Ovo je TCP paket koji sadrži prazan HTTP GET zahtev ka korenu web servisa koristeći HTTP/1.0, praćen linijskim razmakom i praznim redom.



Linija `ports` govori Nmap-u za koji port da pošalje ovu sondu. Ovo vam omogućava da prioritizujete testove i uštedite vreme.



Konačno, imamo dva primera `match`. Prvi, na primer, kategorizovaće skenirani veb servis kao `ajp13` ako regularni izraz sadržan u ovoj liniji odgovara primljenom odgovoru servisa.



Da bismo vam pomogli da razumete kako Probes mogu izgledati, evo liste nekih od Probes koje ćete pronaći u ovoj datoteci (ima ih ukupno 188 u trenutku pisanja ovog vodiča).



![nmap-image](assets/fr/34.webp)



primer nekoliko Probes koje koristi Nmap i koje se nalaze u datoteci `/usr/share/nmap/nmap-service-probes`._



Prva dva (nazvana `NULL` i `GenericLines`) su ovde od posebnog interesa, jer jednostavno šalju prazan TCP paket ili onaj koji sadrži prelazak u novi red. Serverske usluge često se najavljuju tačno čim se uspostavi veza, bez ikakve specifične akcije, komande ili zahteva od klijenta.



Evo slučaja nešto složenijeg _podudaranja_:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



Tačna regularna ekspresija je sadržana ovde između `m|` i `|`, što deli svaku regularnu ekspresiju u ovom fajlu. Molimo vas da odvojite vreme da pročitate ceo ovaj primer. Primetićete selekciju u regularnoj ekspresiji: `([\d.]+)`, koja se koristi za izolaciju verzije. Ovaj primer takođe definiše druge Elements kao što su naziv proizvoda `p/nginx/`, dobijena verzija `v/$1/` i CPE sa verzijom `cpe:/a:igor_sysoev:nginx:$1/`.



CPE (Common Platform Enumeration) je standardizovani sistem notacije koji se koristi za identifikaciju i opisivanje softvera i hardvera. Ovaj format omogućava efikasnije upravljanje ranjivostima i sigurnosnim konfiguracijama, i pre svega jedinstven način njihovog predstavljanja, bez obzira na proizvod o kojem je reč. Evo dva primera CPE: `cpe:/o:microsoft:windows_8.1:r1` i `cpe:/a:apache:http_server:2.4.35`



Ovde jasno identifikujemo njihove tipove `o` za OS, `a` za aplikaciju, dobavljača, proizvod i verzije.



Dakle, u slučaju _poklapanja_ sa jednim od ovih regularnih izraza, dobićemo ne samo ime usluge, već i njenu verziju i tačan CPE, što olakšava pronalaženje CVE-ova koji utiču na ovu verziju. Ove informacije ćete pronaći u standardnom izlazu Nmap-a, i videćete da su veoma korisne za druge svrhe koje ćemo pokriti u nekoliko narednih sekcija.



Tačna sintaksa _matches_ i, generalnije, direktiva u datoteci `/usr/share/nmap/nmap-service-probes` se tu ne završava, i može izgledati prilično složeno ako niste navikli da manipulišete Nmap-om i njegovim rezultatima. Međutim, trebali biste barem imati na umu njegovo postojanje i opštu funkciju, što će vam kasnije biti korisno kada budete želeli da razumete ili otklonite grešku u rezultatu, prilagodite skeniranje ili čak doprinesete razvoju Nmap-a.



### III. Korišćenje Nmap-a za detekciju verzija



Sada ćemo koristiti sve ove složene mehanike _Probe_ i _Match_ putem jednostavne opcije: `-sV`. Ovo jednostavno govori Nmap-u: pokušaj da saznaš tačno koje usluge i verzije portova si postavio kao otvorene.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Evo kompletnog primera rezultata takve komande:



![nmap-image](assets/fr/35.webp)



rezultati Nmap-ove detekcije verzija aplikacija izloženih na mreži



Ovde možemo videti da je Nmap uspeo da identifikuje sve verzije mrežnih servisa koje ovaj cilj izlaže, i prikazuje ove informacije u novoj koloni `VERSION`. Moguće je videti prilično precizne informacije, čak do operativnog sistema, ako su te informacije deo pronađenog potpisa.



Da bismo detaljno razumeli šta se dešava tokom skeniranja ranjivosti, možemo koristiti opciju `--version-trace`. Ovo će obezbediti prikaz u režimu otklanjanja grešaka, prikazujući _Probe_ koji je doveo do detekcije:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Kao rezultat toga, imaćemo mnogo informacija za pregled. Pokušajte da identifikujete linije koje počinju sa `Service scan Hard match`. Zatim ćete videti linije poput ovih:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Možemo jasno videti koji su _Probes_ korišćeni za detekciju tehnologije i verzije (u ovom slučaju `NULL` i `GetRequest` _Probes_), kao i informacije koje su dobijene.



### IV. Ovladavanje testovima i tačnost detekcije



Sada ćemo se vratiti na direktivu u datoteci `/usr/share/nmap/nmap-service-probes` koju ranije nismo pogledali:



![nmap-image](assets/fr/36.webp)



ispituje direktivu `rarity` u datoteci `/usr/share/nmap/nmap-service-probes`._



Ova direktiva se koristi za označavanje retkosti (tj. prioriteta/verovatnoće) povezane sa _Probe_. Ova notacija od 1 do 9 omogućava vam da kontrolišete potpunost analize koju obavlja Nmap prilikom slanja _Probes_. U Nmap-ovom sistemu "notacije", retkost od 1 pruža informacije u velikoj većini slučajeva, dok retkost od 8 ili 9 predstavlja veoma poseban slučaj, specifičan za konfiguraciju ili uslugu koja je retko prisutna.



Da budem jasniji, u podrazumevanom slučaju, Nmap će poslati svakom servisu koji treba identifikovati _Probes_ koji imaju retkost od 1 do 7. Da biste dobili bolju predstavu o distribuciji _Probes_ po _retkosti_, evo njihovog broja:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Možda izgleda kontraintuitivno, ima više `rarity` 8 i 9 nego ostalih. To je upravo zato što su rarity 1 Probes generički i rade u većini slučajeva, bez obzira na uslugu (setite se `NULL` Probe koja jednostavno šalje prazan TCP paket). Dok su složeniji Probes gotovo jedinstveni po usluzi.



Ako želimo ručno upravljati sondama koje želimo koristiti u našem skeniranju verzija, možemo koristiti opciju `--version-intensity`. Evo dva primera:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Da završimo ovu temu, evo primera _Probe_ 9 i 8:



![nmap-image](assets/fr/37.webp)



primeri Probe na retkosti 8 i 9 u datoteci `/usr/share/nmap/nmap-service-probes`._



Ove dve _Probes_ detektuju Quake1 i Quake2 servere (video igra). Zanimljivo za nostalgičnu stranu, ali verovatno neće biti od velike koristi u svakodnevnom životu.



U zavisnosti od vaših potreba za preciznošću ili brzinom, zapamtite da ovaj princip `rarity` postoji i može uticati na rezultat.



### V. Korišćenje Nmap-a za detekciju operativnih sistema



Sada ćemo pogledati kako Nmap može pomoći u detekciji operativnih sistema hostova skeniranih i detektovanih na mreži. Da biste to uradili, koristite Nmap opciju `-O` (za `OS Scan`).



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Evo primera rezultata. Ovde nam Nmap kaže da je verovatno u pitanju Linux OS, i nudi nam razne statistike u vezi sa njegovom tačnom verzijom.



![nmap-image](assets/fr/38.webp)



otkrivanje verovatnoće identifikacije operativnog sistema pomoću Nmap-a



Da bi to postigao, Nmap će koristiti mnoštvo tehnika koje funkcionišu na vrlo sličan način kao _Probes_ i _Matches_ za detekciju tehnologije i verzije. Glavna razlika je u tome što će Nmap koristiti prilično "niskonivojske" parametre ICMP, TCP, UDP i drugih protokola. Evo dva primera testa za detekciju operativnog sistema Microsoft Windows 11:



![nmap-image](assets/fr/39.webp)



primeri testova koje izvodi Nmap za detekciju Windows 11 OS-a



Hajde da se suočimo s tim, ovi testovi su veoma teški za tumačenje, i nećemo pokušavati da ih razumemo u dubini u kontekstu uvodnog Nmap tutorijala. Ako želite da dublje istražite ovu temu, fajl koji sadrži ove informacije je `/usr/share/nmap/nmap-os-db`.



Međutim, morate biti svesni da je detekcija OS-a više verovatnoća koju utvrđuje Nmap nego sigurnost.



### VI. Zaključak



U ovom odeljku smo naučili kako da koristimo Nmap opcije za detekciju tehnologija, verzija i operativnih sistema skeniranih hostova i servisa. Sada imamo dobro razumevanje kako Nmap prikuplja ove informacije na daljinu. Takođe smo pregledali opcije za upravljanje detaljnošću i tačnošću testiranja, kao i ograničenja alata u vezi sa ovim temama.



U sledećem odeljku ćemo naučiti kako da koristimo Nmap-ove NSE skripte za izvođenje bezbednosne analize našeg informacionog sistema. Odvojite vreme da ponovo pročitate poslednje odeljke ako je potrebno, i ne oklevajte da vežbate i sami istražite unutrašnjost alata kako biste bolje savladali ono što smo do sada naučili.




## 7 - Analiza bezbednosti: otkrivanje ranjivosti



### I. Prezentacija



U ovom odeljku ćemo naučiti kako koristiti alat za mrežno skeniranje Nmap za otkrivanje i analizu ranjivosti na ciljevima naših skeniranja. Konkretno, pogledaćemo razne opcije dostupne za izvršenje ovog zadatka i proučiti granice mogućnosti alata kako bismo bolje razumeli i interpretirali njegove rezultate.



U ovom prvom delu, pogledaćemo skener ranjivosti Nmap-a i videti kako koristiti osnovne opcije za detekciju ranjivosti. U narednim delovima, detaljnije ćemo razmotriti kako ova funkcija radi i kako se može prilagoditi.



### II. Korišćenje Nmap-a za otkrivanje ranjivosti



Sada želimo koristiti Nmap mrežni skener za otkrivanje ranjivosti u uslugama i sistemima našeg informacionog sistema. To znači da će, pored otkrivanja aktivnih hostova, nabrajanja izloženih usluga i detekcije verzija i tehnologija, Nmap tražiti ranjivosti.



Da bi to postigao, Nmap se oslanja na NSE (_Nmap Scripting Engine_) skripte, koje se mogu posmatrati kao moduli koji omogućavaju granularni pristup testiranju.



Sa pravim opcijama, zamolićemo Nmap da koristi svoje različite NSE skripte na svakoj otkrivenoj usluzi, omogućavajući nam da otkrijemo:





- Greške u konfiguraciji ;





- Dodatna i naprednija verzija i otkrića OS-a ;





- Poznate ranjivosti (CVE-ovi) ;





- Slabi identifikatori ;





- Karakteristika Elements infekcije zlonamernim softverom ;





- Mogućnosti uskraćivanja usluge ;





- Itd.




Kao što možete videti, NSE skripte značajno proširuju mogućnosti Nmap-a u smislu mrežnih operacija koje može da izvrši. I to za obavljanje daleko naprednijih zadataka nego ikada pre. Dobra vest je da se, kao i obično, ove funkcije mogu koristiti jednostavno putem opcije i u podrazumevanom kontekstu. Ovo ćemo videti sledeće.



### III. Primer skeniranja ranjivosti



NSE skripte se mogu koristiti kada se koristi Nmap za skeniranje jednog porta na hostu, svih servisa na tom hostu ili svih servisa detektovanih na nekoliko mreža. Stoga možemo koristiti opcije koje ćemo videti u svim kontekstima koje smo do sada proučili.



Da bismo omogućili skeniranje ranjivosti putem Nmap skeniranja, potrebno je koristiti opciju `-sC`:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Zapamtite da će Nmap po defaultu, ako ne navedete ništa, skenirati samo 1000 najčešćih portova. Neće detektovati ranjivosti na egzotičnijim portovima koje vaši ciljevi mogu izložiti.



Pre nego što upotrebite ovu funkcionalnost na produkcionom informacionom sistemu, pozivam vas da nastavite sa čitanjem tutorijala. U narednim odeljcima ćemo pogledati kako bolje kontrolisati uticaj i tipove testova koji će biti izvršeni.



Ponovnim korišćenjem onoga što smo ranije naučili, možemo, na primer, biti sveobuhvatniji i skenirati sve TCP portove cilja:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Evo rezultata Nmap skeniranja korišćenjem NSE skripti:



![nmap-image](assets/fr/40.webp)



primer rezultata skeniranja ranjivosti na hostu putem Nmap-a._



Ovde vidimo prikaz dodatnih informacija od interesa u kontekstu analize ranjivosti:





- FTP usluga može se pristupiti anonimno i nije zaštićena autentifikacijom. NSE skripta zadužena za ovu verifikaciju nam to govori, pa čak prikazuje deo strukture stabla FTP usluge. Ovde vidimo da imamo pristup `C` direktorijumu Windows sistema!





- NSE skripta zadužena za napredno preuzimanje web servisa prikazuje naslov stranice, dajući nam bolju predstavu o tome šta web servis hostuje.





- Takođe imamo mini analizu konfiguracije SMB servisa (skripte `smb2-time`, `smb-security-mode` i `smb2-security-mode`). Informacije su prikazane malo drugačije, nakon rezultata mrežnog skeniranja, kako bi bile lakše za čitanje. Konkretno, ove informacije ukazuju na odsustvo SMB Exchange potpisa. Ova slabost u konfiguraciji omogućava da cilj bude korišćen u SMB Relay napadu, značajnom sigurnosnom propustu koji se često eksploatiše u testovima upada/cyber-napada.




Naravno, ovo je samo jedan primer. Nmap ima NSE skripte za mnoge servise, ciljajući širok spektar ranjivosti. Detaljnije ćemo razmotriti ove mogućnosti u narednom odeljku.



Da zaključimo ovaj uvod u skeniranje ranjivosti, evo kompletne komande za otkrivanje mreže, skeniranje TCP portova, detekciju verzija i ranjivosti:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Evo komande koja počinje da liči na realističnije slučajeve upotrebe Nmap-a!



### IV. Razumevanje ograničenja Nmap-a u skeniranju ranjivosti



Da budemo jasni: Nmap nije sposoban da izvrši kompletan penetracioni test vašeg informacionog sistema, niti da simulira operaciju Crvenog tima. Ima nekoliko ograničenja kojih morate biti svesni kako ne biste imali lažan osećaj sigurnosti:





- Ograničeno pokrivanje**: iako su Nmap-ovi NSE skripti moćni, njihovo pokrivanje testova može biti ograničeno u poređenju sa drugim specijalizovanim alatima za otkrivanje ranjivosti. Neke ranjivosti možda neće biti pokrivene dostupnim NSE skriptama, kao što su ranjivosti Active Directory-ja, izloženost osetljivih podataka ili napredniji slučajevi ranjivih web aplikacija.





- Složenost ranjivosti**: određene vrste ranjivosti mogu biti teške za otkrivanje korišćenjem NSE skripti zbog njihove složenosti. Na primer, ranjivosti koje zahtevaju složenu interakciju sa udaljenim servisom možda neće biti efikasno otkrivene pomoću Nmap-a (kao u slučaju prekomernih dozvola u deljenju fajlova ili greške u kontroli dozvola u veb aplikaciji).





- Pasivno otkrivanje**: Nmap se prvenstveno fokusira na aktivne skeniranja za otkrivanje ranjivosti, što znači da možda neće efikasno otkriti potencijalne ranjivosti bez uspostavljanja aktivne veze sa ciljnim hostovima. Ranjivosti koje se ne manifestuju tokom aktivnog skeniranja stoga mogu biti propuštene (kao u slučaju ubacivanja koda u veb aplikaciju).





- Zavisnost od ažuriranja**: Nmap-ova [baza podataka](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) NSE skripti se konstantno razvija, ali može doći do kašnjenja između otkrivanja nove ranjivosti i dodavanja odgovarajuće skripte u Nmap. Kao rezultat toga, Nmap možda neće uvek biti ažuriran sa najnovijim ranjivostima.





- Lažno pozitivni i lažno negativni rezultati**: kao i sa svakim sigurnosnim alatom, Nmap-ovi NSE skripti mogu proizvesti lažno pozitivne (lažna upozorenja o ranjivostima) ili lažno negativne rezultate (prave ranjivosti koje nisu otkrivene). Ovo je nešto što treba imati na umu prilikom analize Nmap rezultata.




Dakle, važno je razumeti šta Nmap radi, a šta ne radi, kao i znati kako interpretirati njegove rezultate. Konkretno, videli smo kroz ovaj vodič da podrazumevane opcije mogu dovesti do propuštanja važnih Elements koje se mogu otkriti pažljivom upotrebom.



Bilo da ste administrator mrežnog sistema, inženjer bezbednosti ili čak CISO, korišćenje Nmap-a vam daje pregled bezbednosnog statusa informacionog sistema. Ovo je važan prvi korak u obezbeđivanju sistema, koji IT tim može redovno sprovoditi. Međutim, to ne bi trebalo da zameni intervenciju i savete [stručnjaka za sajber bezbednost](https://www.it-connect.fr/cours-tutoriels/securite-informatique/), koji će moći da otkriju slabosti daleko sveobuhvatnije nego Nmap.



### V. Zaključak



U ovom prvom delu Modula 3, predstavili smo skeniranje ranjivosti putem Nmap-a. Sada znamo kako koristiti glavnu opciju za obavljanje ovog zadatka, ali takođe znamo i ograničenja vežbe. U sledećem delu, detaljnije ćemo razmotriti ovu funkcionalnost, koristeći NSE skripte da desetostruko povećamo moć Nmap-a.



## 8 - Korišćenje NSE skripti u Nmap-u



### I. Prezentacija



U ovom odeljku ćemo detaljno razmotriti NSE (_Nmap Scripting Engine_) skripte. Posebno ćemo pogledati zašto su one jedna od velikih prednosti ovog alata, kako funkcionišu i kako pregledati i koristiti mnoge postojeće skripte.



Ovaj deo se nadovezuje na prethodni tutorijal, u kojem smo naučili kako da koristimo Nmap-ove funkcije za skeniranje ranjivosti na osnovni način. Sada ćemo detaljnije pogledati kako [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) funkcioniše u tom pogledu, kako bismo ponovo mogli da izvršimo preciznija i kontrolisanija skeniranja.



### II. Koncept Nmap NSE skripti



Nmap-ovi NSE skripti omogućavaju vam da proširite njegove mogućnosti na veoma fleksibilan način. Oni su napisani u LUA-i, skriptnom jeziku koji je lakši za rukovanje i pristup od C ili C# jezika koje koristi Nmap. Prednost korišćenja LUA skripte sa Nmap-om umesto samostalnog alata je što nam omogućava da iskoristimo brzinu izvršavanja i standardne funkcije Nmap-a (otkrivanje hosta, porta i verzije, itd.).



Ovi skripti su organizovani po kategorijama, a jedan skript može pripadati više od jedne kategorije:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Tehnički, kategorije kojima skripta pripada su direktno naznačene u njenom kodu.



![nmap-image](assets/fr/41.webp)



kategorije skripti nSE `ftp-anon`._



Ovaj primer prikazuje deo koda NSE skripte `ftp-anon.nse`, čije izvršavanje smo videli u prethodnom odeljku.



### III. Navedi postojeće NSE skripte



Podrazumevano, NSE skripte za Nmap nalaze se u direktorijumu `/usr/share/nmap/scripts/`, bez specifične strukture stabla ili hijerarhije. Evo pregleda sadržaja ovog direktorijuma:



![nmap-image](assets/fr/42.webp)



izvlači sadržaj direktorijuma `/usr/share/nmap/scripts/` koji sadrži NSE skripte._



Ovaj direktorijum sadrži preko 5.000 NSE skripti. U većini slučajeva, prvi deo imena skripte sadrži protokol ili kategoriju kojoj pripada. Ovo nam omogućava da sortiramo listu, na primer, ako želimo da navedemo sve skripte koje ciljaju FTP servis:



![nmap-image](assets/fr/43.webp)



lista NSE Nmap skripti sa imenima koja počinju sa `ftp-`.



Nmap zapravo ne nudi opciju za pregledavanje i listanje svojih NSE skripti; možete koristiti komandu `--script-help` praćenu imenom kategorije ili reči:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Međutim, izlaz će biti naziv svakog skripta i njegov opis, što nije optimalno ako pretraga donese nekoliko desetina skripti:



![nmap-image](assets/fr/44.webp)



rezultat korišćenja Nmap komande `--script-help`



Po mom mišljenju, najefikasnija metoda je korišćenje klasičnih Linux komandi u direktorijumu `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Slobodno pregledajte kod modula koji vam se dopadaju, kako biste bolje razumeli kako funkcioniše NSE skripta.



### IV. Korišćenje Nmap-ovih NSE skripti



Sada ćemo naučiti kako da izvršimo skeniranje ranjivosti pažljivim odabirom NSE skripti koje nas zanimaju.



#### A. Izaberite skripte po kategoriji



Za početak, možemo izabrati da izvršimo sve skripte koje pripadaju određenoj kategoriji. Moramo naznačiti ovu kategoriju ili ove kategorije Nmap-u sa argumentom `--script <category>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Ova prva komanda je ekvivalent komandi `nmap -sC`. Podrazumevano, Nmap će izabrati skripte iz kategorije `default`, ali to je samo radi argumentacije. Sledeća komanda, na primer, koristiće sve skripte iz kategorije `discovery`:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Kao što smo videli, neke kategorije nam omogućavaju da brzo identifikujemo šta povezani NSE skripti rade (`discovery`, `vuln`, `exploit`), dok druge definišu nivo rizika, detekcije ili stabilnosti izvršenog testa. Ako smo u osetljivom kontekstu i nemamo dobar uvid u različite akcije koje izvodi naš izbor skripti, možemo odlučiti da kombinujemo izbore kako bismo odabrali samo one skripte koji su u kategorijama `discovery` i `safe`:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Ako apsolutno i eksplicitno želite da isključite skripte iz kategorija `dos` i `intrusive`, možete koristiti sledeću notaciju:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Imajte na umu da će navođenje uslova isključenja kao gore rezultirati korišćenjem svih drugih kategorija koje nisu eksplicitno isključene. Da bismo bili pravedniji, mogli bismo navesti, na primer:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Evo nekoliko primera kako rukovati NSE skriptama po kategorijama, posebno kada koristite Nmap za analizu ranjivosti u stvarnim kontekstima.



#### B. Izaberite skripte kao jedinicu



Takođe možemo izabrati da izvršimo jedan specifičan test tokom analize, test koji odgovara NSE skripti. Da bismo to uradili, potrebno je da navedemo ime skripte u parametru `-script <name>`. Uzimajući za primer skriptu `ftp-anon.nse`:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Zatim imamo veoma precizan rezultat:



![nmap-image](assets/fr/45.webp)



rezultat korišćenja NSE skripte `ftp-anon` na FTP portu putem Nmap._



Vidimo rezultat pokretanja skripte `ftp-anon` na portu 21, i ni na jednom drugom portu, jer smo naveli opciju `-p 21`. Takođe smo mogli izvršiti osnovno skeniranje portova, pokrećući NSE skriptu `ftp-anon` samo na otkrivenim FTP servisima:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Dakle, Nmap bi takođe izvršio ovaj test anonimne konekcije ako bi pronašao FTP servis na drugom portu.



Za kratak opis onoga što NSE skripta radi, možete koristiti opciju `--script-help` pomenutu iznad:



![nmap-image](assets/fr/46.webp)



pomozi prikaz rezultata za NSE skriptu `sshv1`._



Ukratko, još jednom možemo ponovo koristiti sve opcije otkrivanja mreže, usluge, verzije i tehnologije koje smo koristili do sada!



#### C. Upravljanje argumentima skripte



Tokom korišćenja Nmap-a, naići ćete na određene NSE skripte koje zahtevaju ulazne argumente kako bi ispravno funkcionisale. Sada ćemo pogledati kako proslediti argumente ovim skriptama putem Nmap opcija.



Kao primer, uzmimo skriptu `ssh-brute`, koja vam omogućava da izvršite brute force napad na SSH servis.



Klasičan napad grube sile sastoji se od testiranja nekoliko lozinki (ponekad miliona) u pokušaju da se autentifikuje na određeni nalog. Pokušavajući toliko lozinki, napadač se kladi na verovatnoću da je korisnik koristio slabu lozinku koja se nalazi u rečniku lozinki korišćenom za napad.



Ovaj skript ima opcije "default", koje možemo prilagoditi našem kontekstu. U kontekstu ovog napada, na primer, možemo obezbediti Nmap-u listu korisnika i rečnik lozinki koji će se koristiti. Koliko ja znam, nije moguće lako navesti argumente potrebne za skript, tako da je najpouzdaniji način posetiti zvaničnu Nmap veb stranicu. Direktan link do dokumentacije za NSE skript može se dobiti kao odgovor na opciju `--script-help`:



![nmap-image](assets/fr/47.webp)



rezultat prikazivanja pomoći za NSE skriptu `ssh-brute` sa linkom na nmap.org.



Klikom na označeni link, dolazimo na ovu web stranicu sajta [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



spisak argumenata koji se mogu proslediti Nmap-ovom `ssh-brute` NSE skriptu



Ovde imamo jasan pregled argumenata koji se mogu koristiti, pri čemu su glavni u našem kontekstu `passdb` (fajl koji sadrži listu lozinki) i `userdb` (fajl koji sadrži listu korisnika). Dokumentacija ovde se odnosi na interne Nmap biblioteke, jer su ovi mehanizmi za brute force i pridružene opcije zajednički kako bi se koristili uniformno kroz nekoliko skripti (`ssh-brute`, `mysql-brute`, `mssql-brute`, itd.) i stoga će imati manje-više iste argumente:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Kao što možete videti u ovoj poslednjoj komandi, možemo navesti potrebne argumente za Nmap skriptu koristeći opciju `--scripts-args key=value,key=value`. Evo mogućeg rezultata Nmap izlaza prilikom izvođenja SSH brute force napada putem `ssh-brute` NSE skripte:



![nmap-image](assets/fr/49.webp)



rezultat izvršenja SSH bruteforce napada putem Nmap._



Kao što možete videti, informacije generisane od strane NSE skripti su prefiksirane sa `NSE: [ime skripte]` u interaktivnom izlazu (izlaz terminala), što olakšava pronalaženje. Unutar uobičajenog prikaza rezultata Nmap-a, jednostavno imamo rezime koji ukazuje na to da li su otkriveni slabi identifikatori (uključujući lozinke, zapamtite).



Da bismo stvari podigli na viši nivo, i da vas podsetimo da se sve ovo može koristiti pored svih opcija koje smo već razmotrili, evo komande koja će otkriti mrežu `10.10.10.0/24`, skenirati 2000 najčešćih TCP portova i pokrenuti pretragu anonimnog pristupa na FTP servisima i kampanju brutalne sile na SSH servisima:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Ovo je samo jedan primer mnogih dostupnih skripti i njihovih opcija. Ali sada imamo bolju predstavu o tome kako se nositi sa NSE skriptama, da li zahtevaju argumente i kako proslediti te argumente Nmap-u.



### V. Zaključak



U ovom odeljku smo naučili kako da koristimo Nmap-ove NSE skripte za obavljanje različitih zadataka. Pozivam vas da odvojite vreme da istražite različite kategorije skripti i same skripte, kako biste videli koliko testova mogu automatizovati.



Već nekoliko sekcija akumuliramo više ili manje napredne opcije otkrivanja, skeniranja i enumeracije. Do sada bi trebalo da ste svesni da Nmap-ov izlaz i prikaz rezultata postaju prilično opsežni, ponekad čak i previše opširni za naš terminal. U sledećem delu, naučićemo kako da ovladamo ovim izlazom, posebno tako što ćemo ga čuvati u fajlovima u različitim formatima.






## 9 - Upravljanje izlaznim podacima Nmap-a




### I. Prezentacija



U ovom odeljku ćemo pogledati izlaz koji proizvodi Nmap, a posebno različite opcije za formatiranje ovog izlaza. Videćemo da Nmap može proizvesti nekoliko formata izlaza kako bi odgovarao različitim potrebama, i da je i ovo jedna od velikih snaga ovog alata.



Podrazumevano, Nmap nudi detaljan prikaz rezultata skeniranja i testova koje obavlja. Ovo uključuje skenirane hostove i servise, one koji su detektovani kao dostupni, specifikacije otvorenih portova, njihov status i verziju. Pored toga, detalji NSE skripti su takođe dostupni u izlazu terminala. Međutim, ovaj izlaz može brzo postati obiman, čak i uz jasno formatiranje informacija, što može otežati pronalaženje preciznih informacija u rezultatima.



### II. Ovladavanje Nmap izlaznim formatima



#### A. Sačuvaj rezultate skeniranja u tekstualnoj datoteci



Da bi stvari bile lakše, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) omogućava vrlo jednostavno čuvanje svog izlaza u tekstualnu datoteku. Ovo može biti korisno za arhiviranje, poređenje sa drugim testovima, ali i za pregled ovog izlaza pomoću specijalizovanih alata za obradu teksta ili skript jezika, kao što su Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed, itd. Da bismo sačuvali standardni izlaz Nmap-a u tekstualnu datoteku, možemo koristiti opciju `-oN <filename>` (slovo "N" u "normal"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Nema iznenađenja, jer će Nmap prikazati svoj uobičajeni standardni izlaz u našem terminalu, ali i u navedenoj datoteci.



#### B. generate Nmap izlaz u sažetom formatu



Postoji i drugi izlazni format u stilu "text" koji može lako da interpretira čovek: format "greppable".



Ovaj format je kreiran da pruži "sažeti" prikaz izlaza Nmap-a, strukturisan na takav način da olakša njegovo procesiranje alatima kao što je `grep`. Pogledajmo primer ovog tipa izlaza:



![nmap-image](assets/fr/50.webp)



nmap mreža skeniranje i izlaz u "greppable" formatu._



Ovde sam izvršio otkrivanje mreže, kao i skeniranje portova i analizu tehnologija i verzija na /24 mreži, a zatim sam sačuvao izlaz u datoteci u formatu "greppable". Na kraju dobijem datoteku koja sadrži 2 linije po aktivnom hostu:





- Prva linija mi govori da je taj i taj host _Up_;





- Druga linija mi govori koji portovi su skenirani, njihov status i informacije o tehnologiji i verziji dobijene u veoma specifičnom formatu: `<port>/<status/<protocol>//<service>//<version>/,`




Ovo formatiranje sa fiksnim delimiterom omogućava brzo procesiranje pomoću alata za obradu teksta kao što su `grep`, ili skriptni i programski jezici. Sledeća komanda, na primer, omogućava mi da lako dobijem informacije o hostu `10.10.10.5` u slučaju velikog skeniranja koje je izvršio Nmap, čiji bi izlaz bio težak za pregledavanje:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Suprotno tome, takođe mogu lako navesti sve hostove koji imaju otvoren port 21, jer su portovi i IP na istoj liniji:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Da bismo dobili takav izlaz u generate, potrebno je koristiti opciju `-oG <filename>.gnmap` (slovo "G" u "grep"). Po navici, koristim ekstenziju `.gnmap` za takvu datoteku, ali slobodno koristite koju god želite:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Ovaj format se može koristiti za različite svrhe i posebno je koristan za brzo skriptovanje/sortiranje. Ipak, teži da bude napušten u korist formata koji ćemo sledeće razmatrati.



napomena: `-oG` format pogodan za pretragu je zvanično zastareo od Nmap verzije 7.90. I dalje se može koristiti radi kompatibilnosti. I dalje se može koristiti za potrebe kompatibilnosti, ali se preporučuje korišćenje XML ili normalnog formata za bilo koji razvoj ili automatizovano parsiranje._



#### C. XML format za Nmap izlaz



Poslednji format koji vredi pomenuti u ovom vodiču je XML. Za razliku od prethodna dva formata, ovaj nije dizajniran da ga čitaju ljudi, već drugi alati ili skripte.



XML (_eXtensible Markup Language_) je jezik za označavanje koji se koristi za skladištenje i prenos podataka, nudeći hijerarhijsku strukturu putem prilagođenih oznaka.



U okviru Nmap-a, XML format se koristi za generate detaljne izveštaje o izvršenim skeniranjima, uključujući informacije o hostovima, portovima i otkrivenim ranjivostima, kao i dodatne informacije koje nisu prikazane u standardnom Nmap izlazu.



Da bismo generate dobili izlaznu datoteku u XML formatu, potrebno je koristiti opciju `-oX` ("O" od "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Rezultat je standardni izlaz Nmap-a u vašem terminalu, kao i datoteka u XML formatu u vašem trenutnom direktorijumu.



Naravno, XML format nije dizajniran da ga čitaju i interpretiraju ljudi. Ipak, ako želite da radite skriptovanje ili automatizovanu analizu na ovom formatu Nmap izlaza, i dalje morate imati ideju o korišćenim oznakama i strukturi. Na primer, evo dela sadržaja XML fajla kreiranog od strane Nmap-a, koji prikazuje rezultate skeniranja za 1 host:



![nmap-image](assets/fr/51.webp)



Nažalost, ne mogu da generišem ili prikažem XML zapise direktno. Međutim, mogu da vam opišem strukturu XML zapisa za jedan host tokom Nmap skeniranja.

```xml
<host>
  <status state="up" reason="syn-ack" reason_ttl="0"/>
  <address addr="192.168.1.1" addrtype="ipv4"/>
  <hostnames>
    <hostname name="example-host" type="user"/>
  </hostnames>
  <ports>
    <port protocol="tcp" portid="80">
      <state state="open" reason="syn-ack" reason_ttl="0"/>
      <service name="http" method="table" conf="3"/>
    </port>
    <!-- Više portova može biti navedeno ovde -->
  </ports>
  <os>
    <osmatch name="Linux 3.2 - 4.9" accuracy="98">
      <osclass type="general purpose" vendor="Linux" osfamily="Linux" osgen="3.X" accuracy="98"/>
    </osmatch>
  </os>
  <uptime seconds="3600" lastboot="Fri Oct  6 12:00:00 2023"/>
  <distance value="1"/>
  <tcpsequence index="263" difficulty="Good luck!" values="12345,67890,13579,24680,11223"/>
  <ipidsequence class="Randomized"/>
  <tcptssequence class="1000"/>
</host>
```

Ovaj primer prikazuje osnovne elemente kao što su status hosta, adresa, portovi, operativni sistem i drugi relevantni podaci.



Ovde ima mnogo informacija, a posebno nas zanimaju dve otvorene luke:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Razumemo da će ovaj format olakšati automatsko parsiranje rezultata, jer je svaki deo informacija uredno raspoređen u posvećenu, imenovanu oznaku ili atribut. Konkretno, pronalazimo deo informacija na koji ranije nismo naišli: CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Ukratko smo pomenuli CPE u odeljku 2 modula 2, a ove informacije se određuju u podudaranjima tokom detekcije verzije. Nmap koristi svoje mehanizme za detekciju usluga, tehnologije i verzije kako bi pronašao povezani CPE.



Ovo nam omogućava da ponovo koristimo ove informacije sa bazama podataka i aplikacijama koje ih koriste. Posebno mislim na NVD bazu podataka, koja referencira CVE-ove. Za svaki CVE, ona sadrži CPE-ove pogođene ranjivošću. Evo primera CVE-a koji se odnosi na `a:microsoft:internet_information_services:7.5` iz NVD baze podataka:



![nmap-image](assets/fr/52.webp)



prisustvo CPE u detaljima CVE u NVD bazi podataka



Sada imamo bolje razumevanje prednosti ovog formata, koji nudi veoma jasnu strukturu informacija i sadrži sve podatke prikupljene ili obrađene od strane Nmap-a.



Kao refleks, sistematski čuvam svoje Nmap skeniranja u sva tri formata odjednom. Ovo je omogućeno opcijom `-oA <name>` ("A" za "All"), koja će kreirati `<name>.nmap` fajl, `<name>.xml` fajl i `<name>.gnmap` fajl. Na ovaj način sam siguran da mi ništa neće nedostajati kada trebam ponovo pregledati rezultate.



Sa ova tri formata, trebalo bi da imate sve što vam je potrebno za čuvanje i eventualnu obradu rezultata Nmap-a na automatizovan način. Ponovo ćemo koristiti XML format u sledećem odeljku, kada budemo gledali korišćenje Nmap-a sa drugim sigurnosnim alatima.



#### III. Generisanje HTML izveštaja iz Nmap skeniranja



XML format nudi mnoge mogućnosti, ne najmanje važno to što može poslužiti kao osnova za generisanje izveštaja u HTML formatu, koji će biti vizuelno prijatniji za pregledavanje.



Da bismo transformisali Nmap datoteku u XML formatu u veb stranicu, koristićemo alatku `xsltproc`, koju ćemo prvo morati instalirati:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Jednom kada je ovaj alat instaliran, jednostavno mu dostavite XML datoteku koja treba da se konvertuje i naziv HTML izveštaja koji treba da se generiše:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Kao rezultat, imaćemo celu našu skeniranu verziju lepo strukturiranu, čak i sa nekoliko boja i klikabilnim linkovima u sadržaju!



![nmap-image](assets/fr/53.webp)



izvod iz Nmap izveštaja skeniranja u HTML formatu generisanog pomoću xsltproc._



Uopšteno govoreći, XML datoteka koju sačuva Nmap sadrži referencu na drugu datoteku u XSL formatu:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



Konverzija u HTML je stoga funkcija koju omogućava i olakšava Nmap, pri čemu je `xsltproc` uobičajen i priznat alat za obavljanje ovog zadatka (koji ne dolazi iz Nmap alata).



XSLT (_Extensible Stylesheet Language Transformations_) je podskup XSL-a koji omogućava da se XML podaci prikažu na veb stranici i "transformišu", paralelno sa XSL stilovima, u čitljive, formatirane informacije u HTML formatu.



izvor: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



Nivo informacija u izveštaju je ekvivalentan onom u Nmap-ovom XML formatu i viši od onog u standardnom terminalskom izlazu (_interaktivni izlaz_).



### IV. Upravljanje nivoom detaljnosti Nmap-a



Sada ćemo pogledati nekoliko opcija za Debugger Nmap ili za praćenje njegovog napretka.



Prva opcija koju treba da pomenemo je opcija `-v`, koja povećava obimnost informacija koje Nmap prikazuje. Evo primera:



![nmap-image](assets/fr/54.webp)



nmap-ov detaljan izlaz koristeći opciju `-v`._



Na skeniranju koje cilja mnoge hostove i portove, izlaz u terminalu postaje teško iskoristiv zbog količine prikazanih informacija. Iz tog razloga, ova opcija bi trebalo da se koristi u kombinaciji sa prethodno viđenim opcijama, koje vam omogućavaju da sačuvate standardni izlaz Nmap-a u fajl. Informacije vezane za upotrebu detaljnosti neće biti uključene u ovaj izlazni fajl. Kao što možete videti iz gornjeg primera, ova detaljnost vam omogućava da jasno i direktno pratite Nmap-ove akcije i otkrića. Za duže skeniranje gde prikaz podataka može biti spor, ovo izbegava da budete slepi za trenutne aktivnosti Nmap-a i omogućava vam da znate da stvari napreduju i kojim tempom. Da biste povećali detaljnost za još jedan nivo, možete koristiti opciju `-vv`.



Da biste dodatno pratili aktivnost Nmap-a tokom skeniranja, možete koristiti opciju `--packet-trace`. Sa opcijom `-v`, dobijamo živi log svih otvorenih portova koje je Nmap otkrio, dok sa ovom opcijom dobijamo log liniju za svaki paket poslat na port. Ovo prirodno proizvodi veoma opširan izlaz, ali omogućava detaljno praćenje aktivnosti Nmap-a, evo primera:



![nmap-image](assets/fr/55.webp)



detaljno praćenje aktivnosti Nmap-a putem `--packet-trace`._



Opet, ove informacije neće biti zabeležene u izlaznoj datoteci koju proizvodi Nmap ako se koriste opcije `-oN`, `-oG`, `-oX` ili `-oA`.



Konačno, Nmap takođe nudi dve opcije za debagovanje: `-d` i `-dd`. Ove opcije se ponašaju slično kao opcija za verbosnost `-v`, ali dodaju dodatne tehničke informacije, kao što je rezime tehničkih parametara na početku skeniranja:



![nmap-image](assets/fr/56.webp)



opcije tempiranja su prikazane u Nmap-ovom debug prikazu



U narednih nekoliko odeljaka, pogledaćemo koje su opcije "Vremena" i zašto ih vredi poznavati.



Konačno, ako želite samo osnovni, sintetički pregled napretka Nmap skeniranja, možete koristiti opciju `--stats-every 5s`. "5s" ovde znači 5 sekundi i može se modifikovati prema vašim potrebama. Ovo je učestalost kojom ćemo primati povratne informacije od Nmap-a o njegovom napretku:



![nmap-image](assets/fr/57.webp)



informacije prikazane opcijom Nmap-a `--stats-every`



Posebno, možemo dobiti procenat napretka, kao i indikaciju faze u kojoj se nalazi: faza otkrivanja hosta putem [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), faza otkrivanja izloženih TCP portova, itd. Ove informacije se takođe mogu dobiti u izlazu terminala pritiskom na "Enter" tokom skeniranja.



Međutim, Nmap nije baš dobar u proceni koliko će zadatak trajati, ne samo zato što unapred ne zna koliko će hostova i servisa morati da skenira.



### V. Zaključak



U ovom odeljku smo pogledali nekoliko opcija za čuvanje rezultata Nmap skeniranja u različitim formatima datoteka. Ovo će biti veoma korisno, jer u realnim kontekstima, rezultati skeniranja mogu zauzeti stotine ili čak hiljade linija! Takođe smo videli kako povećati nivo detaljnosti Nmap-a za potrebe debagovanja ili za dobijanje izveštaja o napretku skeniranja.



XML format će biti posebno koristan u sledećem delu, gde ćemo pogledati nekoliko alata koji mogu raditi sa Nmap rezultatima.




## 10 - Korišćenje Nmap-a sa drugim sigurnosnim alatima



### I. Prezentacija



U ovom odeljku ćemo pogledati neke od klasičnih upotreba Nmap-a sa drugim besplatnim i open source sigurnosnim alatima. Konkretno, iskoristićemo ono što smo naučili u prethodnim odeljcima da dodatno poboljšamo snagu i efikasnost Nmap-a.



Mogućnost čuvanja rezultata Nmap skeniranja u XML formatu čini podatke kompatibilnim sa mnoštvom drugih alata. Kako skoro svi današnji programski i skriptni jezici imaju biblioteke sposobne za parsiranje XML-a, ovo znatno olakšava obradu tih podataka. Brojni alati, posebno oni usmereni ka ofanzivnoj bezbednosti, imaju funkcije za obradu XML formata koji generiše Nmap. Hajde da pogledamo bliže.



Pomenuću nekoliko ofanzivnih alata bez detaljnog objašnjavanja kako se koriste ili kako funkcionišu. Pretpostaviću da je čitalac upoznat sa njihovom osnovnom upotrebom i da su već operativni. Ovaj deo će biti od posebnog interesa za [cybersecurity] profesionalce (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), ljude na obuci ili one koji su odlučili da se dublje posvete ovoj temi.



### II. Uvoz rezultata Nmap-a u Metasploit



Prvi alat koji ćemo pogledati za ponovno korišćenje Nmap podataka u ofanzivnoj bezbednosti i istraživanju ranjivosti je Metasploit.



Metasploit je okvir za eksploataciju i napade. To je besplatno rešenje i prepoznat alat koji sadrži veliki broj modula napisanih u Ruby ili Python jeziku. Ovi moduli omogućavaju eksploataciju ranjivosti, izvođenje napada, generisanje backdoor-a, upravljanje povratnim pozivima (C&C ili funkcije komunikacije i kontrole) i sve to da se koristi na ujednačen način.



Posebno, ovaj dobro poznati i široko korišćeni operativni okvir može raditi sa postgreSQL [bazom podataka](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) u kojoj su smešteni hostovi, portovi, servisi, informacije o autentifikaciji i još mnogo toga.





- Zvanična dokumentacija za Metasploit: [https://docs.metasploit.com/](https://docs.metasploit.com/)




Ovo je mesto gde Nmap i njegov izlaz dolaze do izražaja, jer se XML format Nmap izlaza može lako uvesti u Metasploit bazu podataka kako bi se popunila baza podataka domaćina i usluga, koje se zatim mogu brzo označiti kao mete za ovaj ili onaj napad.



Jednom kada se nađem u svom Metasploit interaktivnom shell-u, počinjem kreiranjem radnog prostora, vrste prostora specifičnog za moje današnje okruženje:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Kada je moj radni prostor kreiran, potrebno je da potvrdimo da je komunikacija sa bazom podataka operativna:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Konačno, možemo koristiti Metasploit komandu `db_import` da uvezemo naš Nmap sken u XML formatu:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Evo rezultata izvršavanja svih ovih komandi:



![nmap-image](assets/fr/58.webp)



uvezi Nmap skeniranje u XML formatu u Metasploit bazu podataka



Ovde možete videti da je svaki host uvezen, zajedno sa svojim uslugama. Ovi podaci se zatim mogu prikazati putem komande `services` ili `services -p <port>` za određenu uslugu:



![nmap-image](assets/fr/59.webp)



lista usluga uvezenih iz XML datoteke u Metasploit bazu podataka



Konačno, možemo brzo i lako ponovo koristiti ove podatke u modulu zahvaljujući opciji `-R`, koja će "konvertovati" listu usluga dobijenih kao ulaz za direktivu `RHOSTS`, koja se koristi za specificiranje ciljeva napada koji će se izvršiti. Evo primera sa modulom `ssh_login`, koji vam omogućava da izvršite brute force napad na [SSH] usluge (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



koristite opciju `services -R` da uvezete usluge navedene kao meta napada



Ovo je samo mali primer šta se može uraditi sa Nmap podacima u Metasploit-u, ali vam daje malu ideju o tome koliko brzo i lako ove informacije mogu biti ponovo korišćene kao deo penetracionog testa, skeniranja ranjivosti ili sajber napada. Takođe je vredno pomenuti da se Nmap može pokrenuti direktno iz Metasploit-a kako bi se rezultati uvezli u bazu podataka (komanda `db_nmap`), još jedna zanimljiva tema za pokrivanje!



### III. Korišćenje Nmap-a sa Aquatone web skenerom



Drugi alat koji bih želeo da predstavim u ovom delu o ponovnoj upotrebi Nmap rezultata za ofanzivnu sigurnost i analizu ranjivosti je Aquatone.



Aquatone je veb skener dizajniran za efikasno istraživanje veb aplikacija na mreži. Nudi napredne funkcije za otkrivanje veb servisa, identifikaciju pod-domena, analizu portova i otisak prsta veb aplikacija. Sve je predstavljeno jasno i sažeto u HTML, JSON i tekstualnim izveštajima za laku analizu veb bezbednosti.



Kao i Metasploit, Aquatone može direktno obraditi Nmap-ov XML format i koristiti ga kao metu za skeniranje. Konkretno, može izdvojiti samo hostove i usluge od interesa (web usluge) iz svih podataka koje Nmap izveštaj može sadržati.





- Link alata: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




Da biste koristili Nmap-ov XML izlaz sa Aquatone-om, jednostavno pošaljite XML datoteku u pipe koji će biti konzumiran od strane Aquatone-a. Evo primera:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Gde Aquatone obično izvodi otkrivanje portova na hostovima kako bi pronašao web usluge, u ovom kontekstu će se oslanjati isključivo na rezultate Nmap-a, koji je već izvršio ovu operaciju, čime se štedi vreme:



![nmap-image](assets/fr/61.webp)



korišćenje Nmap rezultata u XML formatu sa `aquatone`._



Za vašu informaciju, ovde je izvod iz izveštaja koji je proizveo Aquatone:



![nmap-image](assets/fr/62.webp)



primer `aquatone` izveštaja



Lično, često koristim Aquatone da brzo dobijem pregled tipova veb-sajtova prisutnih na mreži, posebno zahvaljujući njegovoj funkciji snimanja ekrana.



Ovde ponovo, posedovanje kompletnog Nmap izveštaja u XML formatu štedi vreme i olakšava ponovno korišćenje u drugom alatu.



### IV. Zaključak



Ova dva primera jasno pokazuju da Nmap-ov XML format olakšava drugim alatima korišćenje njegovih rezultata, jer je to strukturiran, jednostavan za korišćenje format podataka. Postoji mnogo drugih alata sposobnih za obradu ovih rezultata, kao što su alati za automatsko izveštavanje, grafičke reprezentacije ili složeniji, vlasnički skeneri ranjivosti.



Naravno, možete takođe razviti sopstvene skripte i alate u Python-u, [PowerShell-u](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) ili bilo kom drugom jeziku sa XML bibliotekom za parsiranje kako biste manipulisali i ponovo koristili podatke rezultata Nmap-a kako vam odgovara.



Ovaj odeljak nas dovodi do kraja modula tutorijala o naprednijem korišćenju Nmap-a, posebno za skeniranje ranjivosti putem NSE skripti.



Sledeći deo tutorijala će se fokusirati, između ostalog, na dodatne, tehnički zahtevnije najbolje prakse i savete o specifičnim skeniranjima koja Nmap može da izvrši. Takođe ćemo pogledati opcije za optimizaciju performansi skeniranja, koje su posebno korisne prilikom skeniranja velikih mreža.




## 11 - Poboljšanje performansi skeniranja mreže



### I. Prezentacija



U ovom poglavlju ćemo naučiti kako optimizovati brzinu mrežnih skeniranja pomoću Nmap-a korišćenjem različitih specifičnih opcija. Konkretno, saznaćemo više o unutrašnjem funkcionisanju Nmap-a, od upravljanja _timeout_-om do unapred sačuvanih konfiguracija alata.



Sada kada smo dobro pogledali karakteristike Nmap-a, hajde da se uhvatimo u koštac sa zveri i njenom snagom. Ako ste ikada koristili alat na velikim mrežama, verovatno ste primetili da neka skeniranja mogu potrajati dugo, uprkos snazi alata. I to sa dobrim razlogom: jednostavna `nmap` komanda sa nekoliko opcija može generate milione paketa ciljajući stotine hiljada potencijalnih sistema i usluga.



Štaviše, neke konfiguracije mrežne opreme mogu namerno nametnuti sporiju brzinu (broj paketa po sekundi), uz rizik odbijanja vaših paketa ili zabrane vašeg IP Address iz sigurnosnih razloga.



U zavisnosti od konteksta, može biti korisno pokušati optimizovati sve ovo, kao što ćemo videti u ovom poglavlju.



U svakom slučaju, možete proveriti podrazumevane vrednosti parametara koje ćemo razmotriti, kao i da li su opcije koje ćete koristiti ispravno uzete u obzir, putem Nmap debaga (opcija `-d` viđena u prethodnom poglavlju):



![nmap-image](assets/fr/63.webp)



pregledajte opcije vremenskog određivanja putem Nmap-ove opcije `-d`._



### II. Upravljanje brzinom Nmap skeniranja



#### A. Upravljanje paralelizacijom



Podrazumevano, Nmap koristi paralelizaciju u svojim skeniranjima kako bi ih optimizovao, a svi parametri koje koristi mogu se modifikovati putem različitih opcija. Međutim, slučajevi u kojima je zaista potrebno modifikovati ove parametre su prilično retki, tako da ih nećemo detaljno razmatrati u ovom vodiču:





- `--min-hostgroup/max-hostgroup <size>`: veličina paralelnih grupa za skeniranje hostova.





- `--min-parallelism/max-parallelism <numprobes>`: paralelizacija Probes.





- `--scan-delay/--max-scan-delay <time>`: podešava kašnjenje između sondi.




Samo znajte da oni postoje i da se mogu koristiti.



#### B. Upravljanje brojem paketa po sekundi



Podrazumevano, Nmap sam podešava broj paketa po sekundi koje šalje u skladu sa odgovorom mreže. Ali moguće je primorati ovo podešavanje definisanjem visoke i/ili minimalne vrednosti koje treba pratiti u smislu broja paketa po sekundi. Ovo podešavanje se vrši korišćenjem opcija `--min-rate <broj>` i `--max-rate <broj>` gde `broj` predstavlja broj paketa po sekundi. Primer:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Ove opcije vam omogućavaju da prilagodite brzinu skeniranja prema vašim specifičnim potrebama, bilo da ubrzate proces ili ograničite korišćeni protok. Drugi slučaj (ograničavanje brzine skeniranja) je onaj koji će vas najverovatnije dovesti do ovih opcija, naročito ako iskusite kašnjenje mreže prilikom korišćenja Nmap-a (što je prilično retko).



### III. Upravljanje prekidima veze i istekom vremena



Još jedan parametar s kojim se možemo igrati kako bismo optimizovali brzinu Nmap skeniranja (ili garantovali veću tačnost) odnosi se na _timeout_ i _retry_.



Za _timeouts_, ovo je **timeout bez odgovora** nakon kojeg će Nmap prestati čekati odgovor i smatrati uslugu ili host nedostupnim. Za _retry_, ovo je **broj uzastopnih pokušaja operacije** koje će Nmap izvršiti pre nego što pređe dalje.



Kao i kod paralelizacije, upravljanje _timeout_-om i _retry_-jem može se primeniti na faze otkrivanja hosta ili usluge:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: određuje vreme povratnog putovanja Exchange. Opet, ovaj parametar se zapravo izračunava i prilagođava u hodu tokom skeniranja. Malo je verovatno da ćete ga morati koristiti, jer Nmap izračunava ovo vreme u hodu prema reakciji mreže.





- `--max-retries <number>`: ograničava broj ponovnih slanja paketa tokom skeniranja portova. Podrazumevano, Nmap može ići do 10 ponovnih pokušaja za jednu uslugu, posebno ako pronađe kašnjenja ili gubitke na mrežnom nivou, ali u većini slučajeva se izvrši samo jedan.





- `--host-timeout <time>`: specificira maksimalno vreme koje će Nmap provesti na hostu za sve njegove operacije, uključujući skeniranje portova, detekciju servisa i bilo koje druge operacije vezane za taj host. Ako ovaj vremenski interval bude prekoračen bez ikakvog odgovora ili **završetka operacija**, Nmap će napustiti taj host bez prikazivanja bilo kakvih rezultata u vezi sa njim i preći na sledeći na svojoj listi. Ovo vam omogućava da kontrolišete maksimalno vreme koje Nmap provodi na datom hostu, izbegavajući zaglavljivanje na tvrdoglavim hostovima i optimizujući ukupno vreme skeniranja.




U mom svakodnevnom radu koristim opcije `--max-retries` i `--host-timeout` da optimizujem svoje skeniranje:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Ovi parametri nude dodatnu fleksibilnost za prilagođavanje ponašanja skeniranja specifičnim potrebama i uslovima mreže. Međutim, morate biti svesni njihovih implikacija u smislu opterećenja na skenirane hostove i potencijalnog gubitka tačnosti.



### IV. Korišćenje pripremljenih konfiguracija



Različite opcije koje smo videli u ovom poglavlju mogu se koristiti pojedinačno ili kao deo unapred pripremljenih konfiguracija koje nudi Nmap. Opcija koja omogućava korišćenje ovih _templates_ (šablona konfiguracija) je `-T <broj>` ili `-T <ime>`. Postoji 5 nivoa _templates_ koji se mogu koristiti:



```
-T<0-5>: Set timing template (higher is faster)
```



Podrazumevano, Nmap koristi _template_ 3 (_normal_), što je generalno dovoljno.



Što se mene tiče, uglavnom radim u kontekstima gde moram biti prilično brz (dok ostajem što potpuniji) i često koristim opciju `-T4`.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Evo šta nam pokazuje informacije o otklanjanju grešaka za ovo skeniranje:



![nmap-image](assets/fr/64.webp)



korišćenje `-T4` podešavanja tokom Nmap skeniranja



### V. Zaključak



U ovom poglavlju smo razmotrili različite tehnike i opcije koje možete koristiti za upravljanje snagom, agresivnošću i performansama Nmap-a. Ove opcije su posebno korisne prilikom skeniranja velikih mreža, a ređe za svrhe prikrivenosti.



U sledećem poglavlju, pogledaćemo nekoliko najboljih praksi za korišćenje Nmap-a i osiguranje njegove bezbednosti.




## 12 - Bezbednost podataka i poverljivost prilikom korišćenja Nmap-a



### I. Prezentacija



U ovom poglavlju ćemo razmotriti niz dobrih praksi koje treba usvojiti u vezi sa sigurnošću i, pre svega, poverljivošću podataka koje proizvodi, obrađuje i skladišti Nmap.



Korišćenje Nmap-a unutar informacionog sistema može brzo biti kategorizovano kao ofanzivna akcija. Shodno tome, potrebno je preduzeti niz mera predostrožnosti kako bi se delovalo u okviru zakonskog okvira, uz garantovanje bezbednosti ciljanih meta, prikupljenih podataka i sistema korišćenog za skeniranje.



### II. Dobijanje odgovarajućih ovlašćenja



Pre nego što skenirate mrežu ili sistem, uverite se da ste dobili odgovarajuće dozvole. Skeniranje sistema na ranjivosti (`NSE skripte`) bez dozvole može biti nezakonito i može imati pravne posledice, posebno ako bezbednost informacionog sistema nije deo vaših zvaničnih dužnosti.





- Kao podsetnik: [Krivični zakonik: Poglavlje III: Napadi na sisteme za automatsku obradu podataka](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Zaštita osetljivih podataka



Rezultati koje proizvodi Nmap mogu se smatrati osetljivim, posebno kada sadrže informacije o slabostima u informacionom sistemu koje bi napadač mogao iskoristiti. Ali i kada se odnose na sisteme koji nisu dostupni svima (npr. osetljivi, industrijski, zdravstveni ili [rezervni] informacioni sistemi (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



Takođe smo videli da, u zavisnosti od korišćenih NSE skripti, NSE rezultati skeniranja [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) mogu takođe sadržati identifikatore.



Dakle, zlonamerna osoba koja uspe da pristupi ovim rezultatima skeniranja imaće pri ruci mapu informacionog sistema i bogatstvo tehničkih informacija, bez da je sama sprovela ove radnje, uz rizik da bude otkrivena.



Stoga je važno voditi računa da se ne prikupljaju ili skladište osetljive informacije na neprimeren način prilikom korišćenja Nmap-a, uključujući, ali ne ograničavajući se na sledeće:





- Šifrovanje izlaznih podataka: ako treba da skladištite ili prenosite rezultate vaših Nmap skeniranja, obavezno ih šifrujte kako biste zaštitili poverljivost podataka. Ovo će sprečiti neovlašćeno presretanje osetljivih informacija. Idealno, podaci bi trebalo da budu šifrovani čim napuste sistem korišćen za izvođenje skeniranja (ZIP arhiva šifrovana jakom lozinkom je veoma dobar početak).





- Postavite kontrole pristupa: osigurajte da samo ovlašćene osobe imaju pristup rezultatima vaših Nmap skeniranja gde će biti pohranjeni. Postavite odgovarajuće kontrole pristupa kako biste zaštitili osetljive informacije od neovlašćenog pristupa.





- Budnost pri rukovanju podacima: kada prenosite, kopirate ili obrađujete skenirane podatke, pobrinite se da bezbednost podataka bude pod strogom kontrolom. To znači: nemojte ih ostavljati u `Download` direktorijumu radne stanice povezane na Internet, nemojte ih puštati da prolaze kroz vašu internu HTTP datoteku Exchange aplikaciju, nemojte ostavljati Notepad otvoren bez zaključavanja radne stanice tokom pauze za ručak, itd.




### IV. Upravljanje agresivnim skeniranjima



Kao što smo videli tokom ovog tutorijala, Nmap može biti veoma detaljan na mrežnom nivou. Takođe može slati pakete koji nisu pravilno formatirani i koji ne poštuju striktno strukturu protokola u mrežnim okvirima i paketima koje generiše. Sve ove akcije mogu imati uticaj na određene sisteme i servise, ponekad do tačke izazivanja kvara ili zasićenja sistemskih i mrežnih resursa.



Da biste izbegli bilo kakve incidente, potrebno je da savladate ponašanje Nmap-a i znate kako da ga prilagodite kontekstu u kojem se koristi, pomoću različitih opcija o kojima se raspravlja u ovom vodiču. Nećemo nužno koristiti Nmap na isti način na informacionom sistemu koji sadrži industrijski [hardver](https://www.it-connect.fr/actualites/actu-materiel/) kao u korisničkoj mreži sastavljenoj od Windows sistema zaštićenih lokalnim firewall-om ili u jezgru mreže.



Nadamo se da su vas razne lekcije u ovom vodiču naučile kako da ovladate i analizirate ponašanje Nmap-a, ali najbolji način za učenje je kroz praksu. Zato se pobrinite da budete upoznati sa opcijama Nmap-a koje ćete koristiti.



### V. Zaštita sistema skeniranja



U prvom poglavlju smo videli da u većini slučajeva Nmap treba pokrenuti kao `root` ili lokalni administrator. To je zato što obavlja mrežne operacije, ponekad na prilično niskom nivou, putem mrežnih biblioteka, koje zahtevaju visoke i rizične dozvole sa stanovišta stabilnosti sistema ili poverljivosti drugih aplikacija.



Kao rezultat toga, Nmap se može smatrati osetljivom komponentom sistema na kojem je instaliran. Obavezno koristite najnoviju verziju Nmap-a, jer starije verzije mogu sadržati poznate sigurnosne ranjivosti. Korišćenjem ažurirane verzije možete minimizirati rizike povezane sa korišćenjem alata.



Ako ste odlučili da koristite Nmap ne putem sesije kao `root`, već dodeljivanjem specifičnih privilegija privilegovanom korisniku tako da ima sve što mu je potrebno za korišćenje Nmap-a (`sudo` ili _capabilities_), budite svesni da se Nmap može koristiti kao deo potpune eskalacije privilegija:



![nmap-image](assets/fr/65.webp)



povišenje privilegija Nmap putem `sudo`._



Ovde koristim Nmap komandu preko `sudo`, ali ovo mi omogućava da dobijem interaktivnu ljusku kao `root` na sistemu, što nije bio originalni cilj.



Takođe je veoma nepreporučljivo instalirati Nmap na sistemima koji nisu dizajnirani za obavljanje mrežnih skeniranja. Mislim posebno na servere ili radne stanice. S jedne strane, ovo bi dodalo potencijalni vektor za eskalaciju privilegija, ali pre svega bi napadaču omogućilo lak pristup ofanzivnom alatu.



Konačno, bezbednost sistema korišćenog za skeniranje mora biti osigurana šire, kako sam sistem ne bi postao vektor za upad ili curenje informacija. Kao administrator sistema, bolje je koristiti posvećen sistem, idealno sa ograničenim životnim vekom, nego sopstvenu radnu stanicu.



### VI. Zaključak



U zaključku, uverite se da ste pravilno savladali Nmap pre nego što ga koristite u stvarnim ili produkcionim uslovima, i budite oprezni prilikom obrade i upravljanja njegovim rezultatima. Bilo bi šteta izazvati štetu, procuriti podatke ili olakšati kompromitaciju, kada je početni pristup usmeren na poboljšanje bezbednosti vaše kompanije.



## 13 - Port skeniranja putem TCP-a: SYN, Connect i FIN



### I. Prezentacija



U ovom poglavlju i sledećem, detaljnije ćemo pogledati različite tipove TCP skeniranja dostupne u Nmap-u, počevši od najčešće korišćenih: SYN, Connect i FIN skeniranja.



Kao što ste možda primetili, Nmap nudi nekoliko opcija za TCP skeniranje:



![nmap-image](assets/fr/66.webp)



tehnike skeniranja dostupne u Nmap._



Ideja ovde je da objasnimo neke od ovih metoda, kako bismo vam pomogli da razumete njihove razlike, prednosti i ograničenja. Videćete da, u zavisnosti od konteksta ili onoga što želite da saznate, bolje je odlučiti se za jednu ili drugu opciju.



### II. TCP SYN skeniranje ili "Half Open skeniranje



Prva vrsta TCP skeniranja koju ćemo pogledati je `TCP SYN Scan`, takođe poznata kao `Half Open Scan`. Ako se sećate mrežnih skeniranja koja smo radili nakon naših prvih skeniranja portova, ovo je vrsta skeniranja koju podrazumevano koristi [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) kada se pokreće sa root pravima.



Prevod će vam pomoći da razumete kako ovaj sken funkcioniše. Zapravo, TCP SYN sken će poslati TCP SYN paket ka svakom ciljanom portu, što je prvi paket koji klijent šalje (onaj koji zahteva uspostavljanje veze) kao deo čuvenog _Three way handshake_ TCP. Normalno, ako je port otvoren na ciljanom serveru, sa servisom koji radi iza njega, server će poslati nazad TCP SYN/ACK paket da potvrdi klijentov SYN i inicijalizuje TCP vezu. Ovaj odgovor ima oblik TCP paketa sa SYN i ACK zastavicama postavljenim na 1, omogućavajući nam da potvrdimo da je port otvoren i vodi ka servisu.



S druge strane, ako je port zatvoren, server će nam poslati `TCP` paket sa RST i ACK zastavicama postavljenim na 1 kako bi prekinuo zahtev za povezivanje, tako da ćemo znati da se čini da nijedna usluga nije aktivna iza ovog porta:



![nmap-image](assets/fr/67.webp)



dijagram ponašanja tCP SYN skeniranja za otvorene i zatvorene portove



Da bih dobio konkretniji uvid u `TCP SYN Scan`, izvršio sam skeniranje porta TCP/80 na hostu koji je imao aktivan web server na ovom portu. Pokretanjem mrežnog skeniranja sa Wireshark-om, možemo videti sledeći tok (izvor skeniranja: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



snimanje mreže tokom TCP SYN skeniranja za otvoreni port



Na prvoj liniji vidimo da izvor skeniranja šalje TCP paket hostu `10.10.10.203` na port TCP/80. U ovom TCP paketu, SYN zastavica je postavljena na 1 kako bi označila da je ovo zahtev za inicijalizaciju TCP veze.



Zatim, na drugoj liniji, vidimo da cilj odgovara sa `TCP SYN/ACK`, što znači da prihvata inicijalizaciju veze i stoga da prima tokove na portu TCP/80. Možemo stoga zaključiti da je port TCP/80 otvoren i da je veb server prisutan na skeniranom serveru.



Naš domaćin zatim šalje nazad RST paket kako bi zatvorio vezu, omogućavajući skeniranom domaćinu da ne održava otvorenu TCP vezu čekajući odgovor. U slučaju skeniranja na mnogim portovima, ne zatvaranje TCP veza moglo bi dovesti do uskraćivanja usluge, zasićujući broj veza koje čekaju odgovor koje server može održavati (pogledajte [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



U Wireshark-u, moći ćete da vidite status TCP zastavica za svaki test koji izvršimo. Ovo će pokazati da li je paket SYN, SYN/ACK, ACK, itd. paket:



![nmap-image](assets/fr/69.webp)



pogledajte TCP zastavice paketa u Wireshark-u (ovde TCP SYN)



Suprotno tome, pokrenuo sam isti test između dve mašine, ali ovog puta skenirao TCP/81 port na kojem nijedna usluga nije aktivna (izvor skeniranja: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



snimanje mreže tokom TCP SYN skeniranja za zatvoren port



Skenirani host vraća `TCP RST/ACK` kao odgovor na moj `TCP SYN` kada port nije otvoren.



Kao što je pomenuto, kada pokrećete Nmap iz privilegovanog terminala, TCP SYN skeniranje je podrazumevani režim i može se forsirati putem opcije `-sS` (`scan SYN`):



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




`TCP SYN Scan` je najčešće korišćen sken zbog brzine. S druge strane, neuspeh klijenta da završi _Three Way Handshake_ (tj. ne slanje ACK nakon serverovog SYN/ACK) može izgledati sumnjivo ako se previše puta primeti na serveru ili sa istog izvora na mreži. Zaista, normalno ponašanje klijenta nakon primanja TCP SYN/ACK paketa kao odgovor na TCP SYN je da pošalje `acknowledgement` (ACK) i zatim započne Exchange.



Ipak, omogućava nešto brže skeniranje, jer se ne trudi da šalje ACK za svaki pozitivan odgovor. Prednost SYN skeniranja je njegova brzina, jer se šalje samo jedan paket po portu koji se skenira, na račun veće šanse za detekciju.



Pored toga, TCP SYN skeniranje može otkriti da li je port filtriran (zaštićen) od strane vatrozida. Naime, vatrozid ispred ciljnog hosta može se otkriti po načinu na koji se ponaša kada primi TCP SYN paket na port koji treba da štiti. Jednostavno neće odgovoriti. Međutim, kao što smo videli, u oba slučaja (otvoren ili zatvoren port), postoji odgovor od hosta. Ovo treće ponašanje će otkriti prisustvo vatrozida između skeniranog hosta i mašine koja vrši skeniranje. Evo rezultata koji Nmap može vratiti kada je skenirani port filtriran od strane vatrozida:



![nmap-image](assets/fr/71.webp)



nmap prikaz prilikom skeniranja filtriranog porta



Kada izvršimo hvatanje mreže u vreme skeniranja, možemo zapravo videti da nema odgovora:



![nmap-image](assets/fr/72.webp)



snimanje mreže tokom TCP SYN skeniranja za port filtriran od strane vatrozida



Razlika između zatvorenog porta i filtriranog porta je sledeća: filtrirani port je port zaštićen firewall-om, dok je zatvoreni port port na kojem ne radi nijedna usluga i koji stoga nije u mogućnosti da obradi naše TCP pakete. Neke vrste TCP skeniranja, kao što je TCP SYN skeniranje, mogu otkriti da li je port filtriran, dok druge vrste skeniranja to ne mogu.



### III. TCP Connect scan ili Full Open scan



Drugi tip TCP skeniranja je `TCP Connect scan`, takođe poznat kao _Full Open Scan_. Radi na isti način kao i TCP SYN skeniranje, ali ovaj put vraća `TCP ACK` nakon pozitivnog odgovora sa servera (SYN/ACK). Zato se zove `Full Open`, jer je veza potpuno otvorena i inicirana na svakom portu otvorenom tokom skeniranja, čime se poštuje TCP _Three Way Handshake_:



![nmap-image](assets/fr/73.webp)



dijagram ponašanja tCP Connect skeniranja za otvorene i zatvorene portove



Evo šta se može videti prilikom prolaska kroz mrežu tokom `TCP Connect skeniranja` usmerenog na otvoreni port:



![nmap-image](assets/fr/74.webp)



mreža njuškanje tokom TCP Connect skeniranja za otvoreni port



Možemo videti da je prvi TCP paket poslat kao `TCP SYN` od strane klijenta, a server će zatim odgovoriti sa `TCP SYN/ACK`, što ukazuje da je port otvoren i da hostuje aktivnu uslugu. Da bi simulirao legitimnog klijenta do kraja, Nmap će zatim poslati `TCP ACK` nazad serveru. Suprotno tome, kada se skenira zatvoren port:



![nmap-image](assets/fr/75.webp)



snimanje mreže tokom TCP Connect skeniranja za zatvoreni port



Imajte na umu da je odgovor servera na naš `SYN` paket ponovo `TCP RST/ACK` paket, tako da možemo zaključiti da je port zatvoren i da na njemu ne rade nikakve usluge.



Kada koristite Nmap, opcija `-sT` (`scan Connect`) se koristi za izvođenje TCP Connect skeniranja. Imajte na umu da kada se Nmap koristi iz neprivilegovane sesije, ovo je podrazumevani režim TCP skeniranja:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



`TCP Connect Scan` simulira legitimniji zahtev za povezivanje, sa ponašanjem koje najviše podseća na ponašanje lambda klijenta, pa je teže uočiti skeniranje na smanjenom broju portova. Međutim, sporiji je, jer potpuno inicijalizuje svaku TCP konekciju na otvorenim portovima skenirane mašine.



Nmap skeniranje 10.000 portova će i dalje biti lako otkriveno ako su instalirane usluge za otkrivanje i zaštitu od mrežnih upada (IDS, IPS, EDR). Kada napadač želi da ostane neprimetan, obično će se fokusirati na mali broj strateški odabranih portova, kao što su 445 (SMB) ili 80 (HTTP), koji su često otvoreni na serverima i predstavljaju uobičajene ranjivosti.



Pošto TCP Connect Scan očekuje odgovor u oba slučaja, može takođe detektovati prisustvo firewall-a koji možda filtrira portove na ciljnom hostu.



### IV. TCP FIN scan ili "Stealth Scan



`TCP FIN Scan`, takođe poznat kao _Stealth Scan_, koristi ponašanje klijenta koji završava TCP konekciju da detektuje otvoren port.



U TCP-u, kraj sesije znači slanje TCP paketa sa FIN zastavicom postavljenom na 1. U normalnom Exchange, server prekida svu komunikaciju sa klijentom (bez odgovora). Ako server nema aktivnu TCP vezu sa klijentom, poslaće `RST/ACK`. Stoga možemo razlikovati otvorene i zatvorene portove slanjem `TCP FIN` paketa na skup portova:



![nmap-image](assets/fr/76.webp)



dijagram ponašanja tCP FIN skeniranja za otvorene i zatvorene portove



Ponovo sam snimio mrežu tokom _Stealth skeniranja_ i ovo je ono što vidite kada je skenirani port otvoren:



![nmap-image](assets/fr/77.webp)



snimanje mreže tokom TCP FIN skeniranja za otvoreni port



Možemo videti da klijent šalje jedan ili dva paketa da prekine TCP vezu i da server ne odgovara. On jednostavno prihvata kraj veze i prestaje sa komunikacijom.



Evo šta sada vidimo kada skeniramo zatvoren port:



![nmap-image](assets/fr/78.webp)



snimanje mreže tokom TCP FIN skeniranja za zatvoreni port



Vidimo da server šalje nazad paket `TCP RST/ACK`, tako da postoji razlika u ponašanju između otvorenog i zatvorenog porta, i možemo da navedemo otvorene portove na serveru slanjem TCP FIN paketa. Koristeći Nmap, opcija `-sF` (`scan FIN`) se koristi za izvođenje TCP FIN skeniranja:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Scan ne radi na Windows hostovima, jer OS obično ignoriše TCP FIN pakete kada su poslati na portove koji nisu otvoreni. Dakle, ako pokrenete TCP FIN Scan na Windows hostu, steći ćete utisak da su svi portovi zatvoreni.



Zato je važno biti upoznat sa nekoliko metoda skeniranja i razumeti razliku između njih.



Pošto u oba slučaja TCP FIN neće čekati odgovor, neće moći da detektuje prisustvo vatrozida između ciljnog hosta i izvora skeniranja.



Evo primera TCP FIN skeniranja rezultata Nmap-a:



![nmap-image](assets/fr/79.webp)



rezultati TCP FIN skeniranja pomoću Nmap._



Zapravo, neodgovaranje hosta na datom portu može značiti da je port filtriran, ali takođe da je otvoren i aktivan.



Ovo skeniranje se naziva "stealth", jer ne generate mnogo saobraćaja i generalno ne izaziva logovanje u ciljnim sistemima. Može se koristiti za diskretno otkrivanje portova na mreži bez podizanja alarma. Međutim, kao što je gore pomenuto, njegova efikasnost može varirati u zavisnosti od ciljnog sistema, kao i njegova diskrecija u zavisnosti od konfiguracije sigurnosne opreme.



### V. Zaključak



Toliko o prvom od dva poglavlja o različitim tipovima TCP skeniranja koje nudi Nmap! U sledećem poglavlju ćemo pogledati XMAS, Null i ACK TCP tipove skeniranja, koji rade na različite načine kako bi otkrili otvorene portove na hostu.





## 14 - Skeniranje portova putem TCP-a: XMAS, Null i ACK



### I. Prezentacija



U ovom odeljku nastavićemo da istražujemo različite metode TCP skeniranja koje nudi Nmap. Ovde ćemo pogledati `XMAS`, `Null` i `ACK` metode, koje koriste TCP-specifične funkcije za dobijanje informacija o portovima i uslugama otvorenim na datoj meti.



### II. TCP XMAS skeniranje



XMAS Scan TCP je pomalo neobičan jer uopšte ne simulira normalno ponašanje korisnika ili mašine na mreži. Zapravo, XMAS Scan će poslati TCP pakete sa zastavicama `URG` (Urgent), `PSH` (Push) i `FIN` (Finish) postavljenim na 1, kako bi zaobišao određene firewall-ove ili mehanizme filtriranja.



Ime XMAS dolazi od činjenice da je neobično videti ove zastavice uključene. Kada su sve tri zastavice istovremeno postavljene u TCP paketu, izgleda kao osvetljena jelka:



![nmap-image](assets/fr/80.webp)



tCP zastavice korišćene u XMAS skeniranju



Bez ulaska u detalje o ulozi ovih zastavica ovde, važno je znati da kada se šalje paket sa ove tri zastavice omogućene, aktivna usluga iza ciljanog porta neće vratiti nijedan paket. S druge strane, ako je port zatvoren, dobićemo TCP RST/ACK paket. Sada ćemo moći da razlikujemo ponašanje otvorenog i zatvorenog porta prilikom listanja portova na mašini:



![nmap-image](assets/fr/81.webp)



dijagram ponašanja tCP XMAS skeniranja za otvorene i zatvorene portove



I dalje prateći istu logiku, mrežno skeniranje na portu TCP/80 hosta sa aktivnim web serverom pokazuje sledeće ponašanje prilikom detekcije otvorenog porta (izvor skeniranja `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



snimanje mreže tokom TCP XMAS skeniranja za otvoreni port



Možemo videti da izvor skeniranja šalje dva TCP XMAS paketa (sa zastavicama `FIN`, `PSH` i `URG` postavljenim na 1) ka hostu `10.10.10.203` i da nema povratne informacije od cilja, što ukazuje da je port otvoren. Suprotno tome, kada se izvrši `TCP XMAS Scan` na zatvorenom portu, primećuje se sledeći rezultat:



![nmap-image](assets/fr/83.webp)



snimanje mreže tokom TCP XMAS skeniranja za zatvoren port



Odgovor na naš TCP paket je zatim `TCP RST/ACK`, što ukazuje da je port zatvoren. Da biste koristili ovu tehniku sa Nmap-om, opcija `-sX` (`scan XMAS`) vam omogućava da izvršite TCP XMAS skeniranje:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



Važno je napomenuti da TCP XMAS skeniranje nije u stanju da detektuje vatrozide koji mogu biti između mete i mašine za skeniranje, za razliku od nekih drugih tipova skeniranja kao što su TCP SYN ili Connect. Zaista, aktivni vatrozid između dva domaćina će osigurati da se ne vrati TCP odgovor ako je ciljani port filtriran (tj. zaštićen vatrozidom). U slučaju neodgovaranja, stoga je nemoguće znati da li je port zaštićen vatrozidom ili otvoren i aktivan. Takođe treba biti svestan da, kao i kod TCP FIN skeniranja, određene aplikacije ili operativni sistemi kao što je Windows mogu iskriviti rezultate ovog tipa skeniranja.



napomena: podrška za XMAS/FIN/NULL skeniranja na novijim verzijama Windows-a ostaje ograničena, i rezultati mogu biti nedosledni na ovoj vrsti cilja. (Ažuriranje 2025)_



### III. TCP Null scan



Nasuprot TCP XMAS skeniranju, TCP Null skeniranje će poslati TCP skenirajuće pakete sa svim zastavicama postavljenim na 0. Ovo je takođe ponašanje koje nikada neće biti pronađeno u normalnom Exchange između mašina, jer slanje TCP paketa bez zastavice nije specificirano u RFC-u koji opisuje TCP protokol. Zbog toga se može lakše detektovati.



Kao i TCP XMAS skeniranje, ovo skeniranje može ometati određene firewall-ove ili module za filtriranje, omogućavajući paketima da prođu:



![nmap-image](assets/fr/84.webp)



dijagram ponašanja tCP Null skeniranja za otvorene i zatvorene portove



Evo šta se može videti na mreži tokom TCP Null skeniranja na otvorenom portu:



![nmap-image](assets/fr/85.webp)



snimanje mreže tokom TCP Null skeniranja za otvoreni port



Mašina za skeniranje šalje paket bez zastavice (`[<None>]` u Wiresharku) bez ikakvog odgovora od servera. Suprotno tome, kada je ciljni port zatvoren:



![nmap-image](assets/fr/86.webp)



snimanje mreže tokom TCP Null skeniranja za zatvoren port



Da biste izvršili TCP Null skeniranje pomoću Nmap-a, jednostavno koristite opciju `-sN` (`scan Null`):



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Pošto je odgovor kada je port otvoren i kada je firewall aktivan (nema povratne informacije servera u oba slučaja) identičan, TCP Null skeniranje nije u mogućnosti da otkrije prisustvo firewalla. Štaviše, firewall čak može falsifikovati rezultat sugerišući da je port otvoren, jer ne odgovara na TCP pakete bez zastavica, iako je port filtriran. Ovo je važna informacija koju treba imati na umu kada se koriste skeniranja koja nisu u stanju da razlikuju između otvorenog i filtriranog (zaštićenog firewallom) porta, kao što su `TCP Null`, `XMAS` ili `FIN` skeniranja, kako bi se ostalo dosledno u interpretaciji dobijenih rezultata.



### IV. TCP ACK skeniranje



TCP ACK skeniranje se koristi za otkrivanje prisustva firewall-a na ciljanom hostu ili između cilja i izvora skeniranja.



Za razliku od drugih skeniranja, TCP ACK skeniranje ne pokušava da identifikuje koji portovi su otvoreni na hostu, već da li je aktivan sistem filtriranja, odgovarajući za svaki port sa `filtered` ili `unfiltered`. Neka TCP skeniranja, kao što su `TCP SYN` ili `TCP Connect`, mogu raditi oba istovremeno, dok druga, kao što su `TCP FIN` ili `TCP XMAS`, uopšte ne mogu odrediti prisustvo filtriranja. Zato TCP ACK skeniranje može biti korisno:



![nmap-image](assets/fr/87.webp)



dijagram ponašanja tCP ACK skeniranja za filtrirane i nefiltrirane portove



Koristićemo Nmap opciju `-sA` da izvršimo ovu vrstu skeniranja. Evo rezultata TCP ACK skeniranja ako je port filtriran, tj. blokiran i zaštićen firewall-om:



![nmap-image](assets/fr/88.webp)



prikaz nmap tokom TCP ACK skeniranja._



Primer rezultata za host sa firewall-om i bez njega. Nmap vraća `filtered` na portovima TCP/80 i TCP/81 hosta `10.10.10.203`. Na mrežnoj analizi putem Wireshark-a, ponašanje je sledeće:



![nmap-image](assets/fr/89.webp)



snimanje mreže tokom TCP ACK skeniranja za port koji nije filtriran od strane vatrozida



Ciljna mašina ne vraća ništa ako je prisutan firewall.



Da biste pokrenuli ovo skeniranje sa Nmap-om, koristite opciju `-sA` (`scan ACK`):



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Zaključak



Razmotrili smo tri različite metode skeniranja putem TCP-a pored već predstavljenih. Ove različite metode treba koristiti u vrlo specifičnim uslovima i kontekstima, naročito u kontekstu penetracionih testova ili operacija Crvenog tima, tokom kojih su prisutne ideje diskrecije.



## 15 - Nmap CheatSheet - Sažetak komandi iz tutorijala



### I. Prezentacija



Evo kratkog pregleda mnogih Nmap komandi i slučajeva upotrebe, kako biste ih brzo pronašli i ponovo koristili u svakodnevnoj upotrebi.



### II. Nmap: CheatSheet IT-Connect



Evo varalica sa komandama koje su predstavljene. Ova stranica olakšava pronalaženje najčešćih upotreba Nmap-a.





- Skeniranje portova




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Otkrivanje aktivnih hostova




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



napomena: Opcija `-sP` je zastarela već nekoliko godina i treba je zameniti sa `-sn`. (Ažuriranje 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Detekcija verzije




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- NSE skripte: traženje ranjivosti




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Upravljanje izlazom Nmap-a




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Optimizacija performansi




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- TCP tipovi skeniranja




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Nadam se da ćeš ove komande smatrati korisnim. Ne zaboravi da prilagodiš cilj svojih skeniranja svom kontekstu i da se pozoveš na zvaničnu dokumentaciju kako bi u potpunosti savladao testove koji se izvode.



### III. Zaključak



Nmap vodič je sada završen. Sada imate osnove koje su vam potrebne za korišćenje ovog sveobuhvatnog i moćnog alata. Snažno vam savetujemo da vežbate u kontrolisanim okruženjima (Hack The Box, VulnHub, virtuelne mašine) pre nego što ga koristite u produkciji.



Mnogo toga ostaje da se istraži o unutrašnjem funkcionisanju alata i naprednim funkcijama. Međutim, ovladavanje komandama i konceptima predstavljenim ovde omogućiće vam da koristite Nmap sa samopouzdanjem i relevantnošću.