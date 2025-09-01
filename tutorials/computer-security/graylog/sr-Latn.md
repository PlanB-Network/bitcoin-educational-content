---
name: Graylog
description: Centralizujte i analizirajte svoje logove lako
---
![cover](assets/cover.webp)



___



*Ovaj vodič je zasnovan na originalnom sadržaju Floriana BURNEL-a objavljenom na [IT-Connect](https://www.it-connect.fr/). Licenca [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Moguće je da su napravljene izmene u originalnom tekstu.*



___



## Implementacija Graylog-a na Debian 12



### I. Prezentacija



Graylog je open source rešenje "log sink" dizajnirano za centralizaciju, skladištenje i analizu logova sa vaših mašina i mrežnih uređaja u realnom vremenu. U ovom vodiču ćemo naučiti kako da instaliramo besplatnu verziju Graylog-a na Debian 12 mašini!



U okviru informacionog sistema, svaki **server**, bilo da radi na **Linux**-u ili **Windows**-u, i svaki **mrežni uređaj** (switch, ruter, firewall, itd...) **generiše sopstvene logove**, koji se čuvaju lokalno. Sa logovima koji su čuvani lokalno na svakoj mašini, analiza i korelacija događaja je veoma teška... Tu dolazi **Graylog**. On će delovati kao **log sink**, što znači da će mu **sve vaše mašine slati svoje logove** (putem syslog-a, na primer). Graylog će zatim **čuvati i indeksirati te logove**, omogućavajući vam da izvršavate globalne pretrage i kreirate upozorenja.



Graylog je alat za analizu i nadzor koji olakšava identifikaciju sumnjivog ponašanja i raznih problema (stabilnost, performanse, itd.).




![Image](assets/fr/034.webp)



**Napomena: besplatna verzija, **Graylog Open**, nije SIEM kao što je Wazuh, posebno jer joj nedostaju stvarne funkcije detekcije upada.



### II. Preduslovi



**Stack Graylog** zasnovan je na **nekoliko komponenti** koje ćemo morati instalirati i konfigurisati. Ovde ćemo instalirati sve komponente na istom serveru, ali je moguće kreirati klastere zasnovane na nekoliko čvorova i raspodeliti uloge na više servera. Za potrebe ovog vodiča, instaliraćemo **Graylog 6.1**, najnoviju verziju do danas.





- MongoDB 7**, trenutna preporučena verzija za Graylog (minimalno 5.0.7, maksimalno 7.x)
- OpenSearch**, otvoreni izvor Fork Elasticsearch kreiran od strane Amazona (minimalno 1.1.x, maksimalno 2.15.x)
- OpenJDK 17**



**Graylog server** radi na **Debian 12**, ali je instalacija moguća i na drugim distribucijama, uključujući putem Dockera. Virtuelna mašina je opremljena sa **8 GB RAM-a** i **256 GB prostora na disku**, kako bi imala dovoljno resursa za sve komponente (inače ovo može značajno uticati na performanse). Međutim, ovo dajem kao okvirni vodič, jer **veličina Graylog arhitekture zavisi od količine informacija koje se obrađuju**. Graylog može obraditi 30 MB ili 300 MB podataka dnevno, kao i 300 GB podataka dnevno... To je **skalabilno rešenje** sposobno za rukovanje **terabajtima logova** (pogledajte [ovu stranicu](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Izvor: Graylog



Pre nego što započnete konfiguraciju, dodelite statičku IP adresu Address Graylog mašini i instalirajte najnovija ažuriranja. Obavezno postavite vremensku zonu lokalne mašine i definišite NTP server za sinhronizaciju datuma i vremena. Evo komande koju treba pokrenuti:



```
sudo timedatectl set-timezone Europe/Paris
```



**Napomena: **Instalacija OpenSearch-a je opcionalna** ako koristite **Graylog Data Node** umesto toga.



### III Korak-po-korak instalacija Graylog-a



Hajde da počnemo ažuriranjem keša paketa i instaliranjem alata koji su nam potrebni za ono što sledi.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. Instaliranje MongoDB



Kada to bude završeno, počećemo sa instalacijom MongoDB-a. Preuzmite GPG ključ koji odgovara MongoDB repozitorijumu:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Zatim dodajte MongoDB 6 repozitorijum na Debian 12 mašinu:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Zatim ćemo ažurirati keš paketa i pokušati instalirati MongoDB:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



MongoDB ne može biti instaliran jer nedostaje zavisnost: **libssl1.1**. Moraćemo da instaliramo ovaj paket ručno pre nego što možemo nastaviti, jer Debian 12 ga nema u svojim repozitorijumima.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Preuzećemo DEB paket pod nazivom "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (najnovija verzija) pomoću komande **wget**, a zatim ćemo ga instalirati pomoću komande **dpkg**. Ovo proizvodi sledeće dve komande:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Ponovo pokreni instalaciju MongoDB-a:



```
sudo apt-get install -y mongodb-org
```



Zatim ponovo pokrenite MongoDB servis i omogućite mu da se automatski pokreće kada se Debian server pokrene.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Sa instaliranim MongoDB-om, možemo preći na instalaciju sledeće komponente.



#### B. Instaliranje OpenSearch



Hajde da pređemo na instalaciju OpenSearch-a na serveru. Sledeća komanda dodaje ključ potpisa za OpenSearch pakete:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Zatim dodajte OpenSearch repozitorijum kako bismo kasnije mogli preuzeti paket pomoću **apt**:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Ažurirajte keš paketa:



```
sudo apt-get update
```



Zatim **instalirajte OpenSearch**, vodeći računa da **definišete podrazumevanu lozinku za Admin nalog vaše instance**. Ovde je lozinka "**IT-Connect2024!**", ali zamenite ovu vrednost jakom lozinkom. **Izbegavajte slabe lozinke** poput "**P@ssword123**" i koristite najmanje **8 karaktera** sa barem jednim karakterom svake vrste (malo slovo, veliko slovo, broj i specijalni karakter), inače će doći do greške na kraju instalacije. **Ovo je preduslov od OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Molimo vas da budete strpljivi tokom instalacije...



Kada završite, odvojite trenutak da izvršite minimalnu konfiguraciju. Otvorite konfiguracionu datoteku u YAML formatu:



```
sudo nano /etc/opensearch/opensearch.yml
```



Kada je datoteka otvorena, postavite sledeće opcije:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



Ova OpenSearch konfiguracija je dizajnirana za postavljanje jednog čvora. Evo nekih objašnjenja različitih parametara koje koristimo:





- cluster.name: graylog**: ovaj parametar imenuje OpenSearch klaster sa imenom "**graylog**".
- node.name: ${HOSTNAME}**: ime čvora se dinamički postavlja da odgovara onom lokalne Linux mašine. Čak i ako imamo samo jedan čvor, važno je pravilno ga imenovati.
- path.data: /var/lib/opensearch**: ova putanja specificira gde OpenSearch čuva svoje podatke na lokalnom računaru, u ovom slučaju u "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: ova putanja definiše gde su OpenSearch log fajlovi sačuvani, ovde u "**/var/log/opensearch**".
- discovery.type: single-node**: ovaj parametar konfiguriše OpenSearch da radi sa jednim čvorom, stoga izbor opcije "**single-node**".
- network.host: 127.0.0.1**: ova konfiguracija osigurava da OpenSearch sluša samo na svojoj Interface lokalnoj petlji, što je dovoljno jer se nalazi na istom serveru kao i Graylog.
- action.auto_create_index: false**: onemogućavanjem automatskog kreiranja indeksa, OpenSearch neće automatski kreirati indeks kada se dokument pošalje bez postojećeg indeksa.
- plugins.security.disabled: true**: ova opcija deaktivira OpenSearch sigurnosni dodatak, što znači da neće biti autentifikacije, upravljanja pristupom ili enkripcije komunikacije. Ovo podešavanje štedi vreme prilikom postavljanja Graylog-a, ali treba ga izbegavati u produkciji (pogledajte [ovu stranicu](https://opensearch.org/docs/1.0/security-plugin/index/)).



Neke opcije su već prisutne, tako da jednostavno treba da uklonite "#" da biste ih aktivirali, a zatim navedite svoju vrednost. Ako ne možete pronaći opciju, možete je direktno navesti na kraju datoteke.



![Image](assets/fr/023.webp)



Sačuvaj i zatvori ovu datoteku.



#### C. Konfiguriši Java (JVM)



Morate konfigurisati Java Virtual Machine koju koristi OpenSearch kako biste prilagodili količinu memorije koju ova usluga može koristiti. Izmenite sledeću konfiguracionu datoteku:



```
sudo nano /etc/opensearch/jvm.options
```



Sa konfiguracijom implementiranom ovde, **OpenSearch će početi sa 4 GB dodeljene memorije i može rasti do 4 GB**, tako da neće biti varijacija memorije tokom rada. Ovde konfiguracija uzima u obzir činjenicu da virtuelna mašina ima ukupno **8 GB RAM-a**. Oba parametra moraju imati istu vrednost. To znači zamenu linija:



```
-Xms1g
-Xmx1g
```



Sa ovim linijama:



```
-Xms4g
-Xmx4g
```



Ovde je slika izmene koja treba da se izvrši:



![Image](assets/fr/022.webp)



Zatvori ovu datoteku nakon što je sačuvaš.



Pored toga, treba da proverimo konfiguraciju parametra "**max_map_count**" u Linux kernelu. On definiše limit memorijskih oblasti mapiranih po procesu, kako bi se zadovoljile potrebe naše aplikacije. **OpenSearch**, kao i **Elasticsearch**, preporučuje postavljanje ove vrednosti na "262144" kako bi se izbegle greške u upravljanju memorijom.



U principu, na sveže instaliranoj Debian 12 mašini, vrednost je već ispravna. Ali hajde da proverimo. Pokreni ovu komandu:



```
cat /proc/sys/vm/max_map_count
```



Ako dobijete vrednost drugačiju od "**262144**", pokrenite sledeću komandu, u suprotnom nije potrebno.



```
sudo sysctl -w vm.max_map_count=262144
```



Konačno, omogućite automatsko pokretanje OpenSearch-a i pokrenite povezanu uslugu.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Ako prikažeš status sistema, trebalo bi da vidiš Java proces sa 4 GB RAM-a.



```
top
```



![Image](assets/fr/029.webp)



Sledeći korak: dugo očekivana instalacija Graylog-a!



#### D. Instaliranje Graylog



Da biste **instalirali Graylog 6.1** u njegovoj najnovijoj verziji, pokrenite sledeće 4 komande za **preuzimanje i instalaciju Graylog Servera**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Kada se ovo završi, potrebno je napraviti neke izmene u Graylog konfiguraciji pre nego što pokušamo da ga pokrenemo.



Hajde da počnemo sa konfigurisanjem ove dve opcije:





- password_secret**: ovaj parametar se koristi za definisanje ključa koji Graylog koristi za osiguranje skladištenja korisničkih lozinki (u duhu salting ključa). Ovaj ključ mora biti **jedinstven** i **nasumičan**.
- root_password_sha2**: ovaj parametar odgovara podrazumevanom administratorskom lozinkom u Graylog-u. Skladišti se kao Hash SHA-256.



Počećemo generisanjem ključa od 96 karaktera za parametar **password_secret**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Kopirajte vraćenu vrednost, zatim otvorite Graylog konfiguracionu datoteku:



```
sudo nano /etc/graylog/server/server.conf
```



Zalepite ključ u parametar **password_secret**, ovako:



![Image](assets/fr/027.webp)



Sačuvaj i zatvori datoteku.



Zatim, treba da postavite lozinku za nalog "**admin**" koji je podrazumevano kreiran. U konfiguracionoj datoteci, Hash lozinke mora biti sačuvan, što znači da mora biti izračunat. Primer ispod daje Hash lozinke "**LogsWells@**": prilagodite vrednost svojoj lozinci.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Kopirajte vrednost dobijenu kao izlaz (bez crtice na kraju reda).



Ponovo otvorite konfiguracionu datoteku Graylog-a:



```
sudo nano /etc/graylog/server/server.conf
```



Zalepite vrednost u opciju **root_password_sha2** ovako:



![Image](assets/fr/026.webp)



Dok ste u konfiguracionoj datoteci, postavite opciju "**http_bind_address**". Navedite "**0.0.0.0:9000**" kako bi se Graylog-ov Interface web mogao pristupiti na portu **9000**, putem bilo koje IP adrese servera Address.



![Image](assets/fr/024.webp)



Zatim postavite opciju "**elasticsearch_hosts**" na `http://127.0.0.1:9200` da biste deklarisali našu lokalnu OpenSearch instancu. Ovo je neophodno, jer ne koristimo **Graylog Data Node**. I bez ove opcije, neće biti moguće ići dalje...



![Image](assets/fr/025.webp)



Sačuvaj i zatvori datoteku.



Ova komanda aktivira Graylog tako da se automatski pokreće pri sledećem podizanju sistema i odmah pokreće Graylog server.



```
sudo systemctl enable --now graylog-server
```



Jednom kada je ovo završeno, pokušajte da se povežete sa Graylog-om iz pregledača. Unesite IP servera Address (ili ime) i port 9000.



**Za vašu informaciju:**



Ne tako davno, prozor za autentifikaciju sličan onom ispod pojavio bi se kada se prvi put prijavite na Graylog. Morali ste uneti svoj login "**admin**" i svoju lozinku. A onda biste bili neprijatno iznenađeni kada biste otkrili da veza ne radi.



![Image](assets/fr/031.webp)



Bilo je potrebno vratiti se na komandnu liniju na Graylog serveru i konsultovati logove. Tada smo mogli videti da je **za prvu konekciju** neophodno **koristiti privremenu lozinku**, navedenu u logovima.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Zatim ste morali ponovo pokušati povezivanje sa korisnikom "**admin**" i privremenom lozinkom, i to vam je omogućilo prijavu!



**Ovo više nije slučaj. Sve što treba da uradite je da se prijavite sa svojim administratorskim nalogom i lozinkom konfigurisanom na komandnoj liniji



![Image](assets/fr/033.webp)



**Dobrodošli u Graylogov Interface!



![Image](assets/fr/019.webp)



#### E. Graylog: kreiraj novi administratorski nalog



Umesto da koristite administratorski nalog koji je nativno kreirao Graylog, možete kreirati svoj lični administratorski nalog. Kliknite na meni "**System**", zatim na "**Users and Teams**" i kliknite na dugme "**Create user**". Zatim popunite formular i dodelite administratorsku ulogu svom nalogu.



![Image](assets/fr/020.webp)



Personalizovani nalog može sadržati dodatne informacije, kao što su ime i prezime i e-mail Address, za razliku od nativnog administratorskog naloga. Štaviše, ovo osigurava bolju sledljivost kada svaka osoba radi sa imenovanim nalogom.



## Pošalji logove u Graylog sa rsyslog



### I. Prezentacija



U ovom drugom delu, naučićemo kako da konfigurišemo Linux mašinu da šalje svoje logove na Graylog server. Da bismo to uradili, instaliraćemo i konfigurisati Rsyslog na sistemu.



### II. Konfigurisanje Graylog-a za primanje Linux logova



Počećemo sa konfigurisanjem Graylog-a. Postoje tri koraka koja treba završiti:





- Kreiranje **Input-a** za kreiranje ulazne tačke koja omogućava Linux mašinama da **šalju Syslog logove putem UDP-a**.
- Kreiranje novog **Indeksa** za čuvanje i **indeksiranje svih Linux logova**.
- Kreiranje **Stream-a** za **usmeravanje** logova primljenih od strane Graylog-a ka novom Linux Index-u.



#### A. Kreiraj Ulaz za Syslog



Prijavite se na Graylog Interface, kliknite na "**System**" u meniju, a zatim na "**Inputs**". U padajućoj listi, izaberite "**Syslog UDP**" i zatim kliknite na dugme označeno sa "**Launch new input**". Takođe je moguće kreirati TCP Syslog Input, ali to zahteva korišćenje TLS sertifikata: prednost za sigurnost, ali nije pokriveno u ovom članku.



![Image](assets/fr/001.webp)



Čarobnjak će se pojaviti na ekranu. Počnite tako što ćete ovom Unosu dati ime, na primer "**Graylog_UDP_Rsyslog_Linux**" i izaberite port. Podrazumevano, port je "**514**", ali ga možete prilagoditi. Ovde je izabran port "**12514**".



![Image](assets/fr/016.webp)



Možete takođe označiti opciju "**Store full message**" da biste sačuvali celu poruku dnevnika u Graylog-u. Kliknite na "**Launch Input**".



![Image](assets/fr/017.webp)



Novi Input je kreiran i sada je aktivan. Graylog sada može primati Syslog logove na portu 12514/UDP, ali još nismo završili sa konfigurisanjem aplikacije.



![Image](assets/fr/018.webp)


**Napomena: jedan unos može se koristiti za čuvanje logova sa nekoliko Linux mašina.



#### B. Kreiraj novi Linux indeks



Moramo kreirati Indeks u Graylog-u za čuvanje logova sa Linux mašina. **Indeks** u Graylog-u je struktura skladištenja koja sadrži primljene logove, tj. primljene poruke. Graylog koristi OpenSearch kao svoj skladišni mehanizam, a poruke su indeksirane kako bi omogućile brze i efikasne pretrage.



Iz Graylog-a, kliknite na "**System**" u meniju, zatim na "**Indices**". Na novoj stranici koja se pojavi, kliknite na "**Create index set**".



![Image](assets/fr/005.webp)



Imenujte ovaj indeks, na primer "**Linux Indeks**", dodajte opis i prefiks, pre nego što potvrdite. Ovde ćemo **skladištiti sve Linux logove u ovom indeksu**. Takođe je moguće kreirati specifične indekse za skladištenje samo određenih logova (samo [SSH] logovi (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), logovi Web servisa, itd.).



![Image](assets/fr/006.webp)



Sada treba da kreiramo novi tok za usmeravanje poruka ka ovom indeksu.



#### C. Kreiraj Stream



Da biste kreirali novi stream, kliknite na "**Streams**" u glavnom meniju Graylog-a. Zatim kliknite na dugme "**Create stream**" sa desne strane. U prozoru koji se pojavi, imenujte stream, na primer "**Linux Stream**" i izaberite indeks "**Linux Index**" za polje pod nazivom "**Index Set**". Potvrdite vaš izbor.



**Napomena: poruke koje odgovaraju ovom toku će takođe biti uključene u "**Podrazumevani tok**", osim ako ne označite opciju "**Ukloni podudaranja iz 'Podrazumevanog toka'**".



![Image](assets/fr/002.webp)



Zatim, u podešavanjima za steam, kliknite na dugme "**Add stream rule**" da biste dodali novo pravilo za usmeravanje poruka. Ako ne možete pronaći ovaj prozor, kliknite na "**Streams**" u meniju, zatim na liniji koja odgovara vašem stream-u, kliknite na "**More**" pa "**Manage Rules**".



Izaberite tip "**match input**" i odaberite prethodno kreirani **Rsyslog input u UDP**. Potvrdite sa dugmetom "**Create Rule**". Sve poruke ka našem novom Input-u će sada biti poslate na Index za Linux.



![Image](assets/fr/003.webp)



Vaš novi Stream treba da se pojavi na listi i treba da bude u stanju "**Running**". Širina opsega poruka pokazuje "**0 msg/s**", jer trenutno ne šaljemo nikakve logove na Rsyslog UDP ulaz. Da biste videli logove stream-a, jednostavno kliknite na njegovo ime.



![Image](assets/fr/004.webp)



**Sve je spremno na Graylog strani**. Sledeći korak je konfiguracija Linux mašine.



### III. Instaliranje i konfiguracija Rsyslog na Linux-u



Prijavite se na Linux mašinu, bilo lokalno ili daljinski, i koristite korisnički nalog sa dozvolama za povećanje privilegija (putem sudo). U suprotnom, koristite direktno "root" nalog.



#### A. Instaliranje paketa Rsyslog



Počnite ažuriranjem keša paketa i instaliranjem paketa pod nazivom "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Zatim proverite status usluge. U većini slučajeva, već je pokrenuta.



```
sudo systemctl status rsyslog
```



#### B. Konfigurisanje Rsyslog



Rsyslog ima glavnu konfiguracionu datoteku koja se nalazi ovde:



```
/etc/rsyslog.conf
```



Pored toga, direktorijum "**/etc/rsyslog.d/**" se koristi za čuvanje dodatnih konfiguracionih fajlova za Rsyslog. U glavnom konfiguracionom fajlu postoji Include direktiva za uvoz svih "**.conf**" fajlova koji se nalaze u ovom direktorijumu. Ovo omogućava da se dodaju dodatni fajlovi za konfiguraciju Rsyslog-a bez izmene glavnog fajla.



U ovom direktorijumu morate koristiti brojeve za definisanje reda učitavanja, jer se fajlovi učitavaju abecednim redom. Dodavanje numeričkog prefiksa omogućava vam da upravljate prioritetom između nekoliko konfiguracionih fajlova. Ovde imamo samo jedan dodatni fajl, tako da to nije problem.



U ovom direktorijumu, kreiraćemo fajl pod nazivom "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



U ovu datoteku umetnite ovu liniju:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Evo kako da protumačite ovu liniju:





- `*.*`: znači poslati sve Syslog logove sa Linux mašine na Graylog.
- `@`: označava da se transport obavlja putem UDP-a. Morate navesti "**@@**" da biste prešli na TCP.
- `192.168.10.220:12514`: označava Address Graylog servera i port na koji se šalju logovi (koji odgovara Input-u).
- `RSYSLOG_SyslogProtocol23Format`: odgovara formatu poruka koje se šalju na Graylog.



Kada završite, sačuvajte datoteku i ponovo pokrenite Rsyslog.



```
sudo systemctl restart rsyslog.service
```



Nakon ove akcije, prve poruke bi trebalo da stignu na vaš Graylog server!



### IV. Prikazivanje Linux logova u Graylog



Iz Graylog-a, možete kliknuti na "**Streams**" i odabrati vaš novi stream da biste videli povezane poruke. Alternativno, kliknite na "**Search**" i odaberite vaš Steam i pokrenite pretragu.



Evo su neke ključne karakteristike Interface:



**1** - Izaberite period za koji će se prikazati poruke. Podrazumevano se prikazuju poruke iz poslednjih 5 minuta.



**2** - Izaberite tok(ove) koji će biti prikazan(i).



**3** - Omogući automatsko osvežavanje liste poruka (na primer, svakih 5 sekundi). U suprotnom, lista je statična i moraćeš da je osvežavaš ručno.



**4** - Kliknite na lupu da pokrenete pretragu nakon izmene perioda, toka ili filtera.



**5** - Unosna traka za određivanje filtera pretrage. Ovde navodim "**source:srv\-docker**" da prikažem samo logove nove mašine na kojoj sam upravo postavio Rsyslog.



Logove šalje Linux mašina:



![Image](assets/fr/015.webp)



### V. Identifikacija neuspeha SSH konekcije



Snaga Grayloga leži u njegovoj sposobnosti da indeksira logove i omogući pretrage prema različitim kriterijumima: izvorna mašina, Timestamp, sadržaj poruke, itd... Mogli bismo tražiti da identifikujemo neuspele SSH konekcije.



Sa udaljene mašine (na primer, Graylog servera), pokušajte da se povežete na vaš Linux server na kojem ste upravo konfigurisali Rsyslog. Na primer:



```
ssh [email protected]
```



Zatim namerno unesite netačno **korisničko ime** i **lozinku**, kako biste izazvali **generate greške povezivanja**. U datoteci "**/var/log/auth.log**", ovo će generate zabeležiti poruke slične sledećem:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Trebalo bi da pronađeš ove poruke na Graylog-u.



Na Graylog-u, koristite sledeći filter pretrage da prikažete samo odgovarajuće poruke:



```
message:Failed password AND application_name:sshd
```



Ako imate nekoliko servera i želite da analizirate logove određenog servera, navedite njegovo ime dodatno:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Evo pregleda rezultata na mašini gde sam generisao nekoliko grešaka u vezi, u različito doba dana:



![Image](assets/fr/009.webp)



Neuspešni pokušaji povezivanja dolaze sa mašine sa IP Address "**192.168.10.199**". Ako želite da saznate više o aktivnosti ovog hosta, možete **pretražiti ovaj IP Address**. Graylog će prikazati sve logove gde se ovaj IP Address pominje, na svim hostovima (za koje je podešeno slanje logova).



U ovom slučaju, filter koji treba koristiti može biti:



```
message:"192.168.10.199"
```



Dobijamo dodatne rezultate (nije iznenađujuće, s obzirom da ne filtriramo na SSH aplikaciji):



![Image](assets/fr/008.webp)



### VI. Zaključak



Prateći ovaj vodič, trebalo bi da budete u mogućnosti da konfigurišete Linux mašinu da šalje svoje logove na Graylog server. Na ovaj način, moći ćete da centralizujete logove vaših Linux hostova u vašem log skladištu!



Da biste otišli još dalje, razmislite o kreiranju kontrolnih tabli i upozorenja kako biste primali obaveštenja kada se otkrije anomalija.



![Image](assets/fr/007.webp)