---
name: Lynis
description: Izvršite bezbednosnu proveru Linux mašine pomoću Lynis-a
---
![cover](assets/cover.webp)



___



*Ovaj vodič je zasnovan na originalnom sadržaju autora Fares CHELLOUG objavljenom na [IT-Connect](https://www.it-connect.fr/). Licenca [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Moguće je da su napravljene izmene u originalnom tekstu.*



___



## I. Prezentacija



**U ovom vodiču ćemo naučiti kako da izvršimo bezbednosnu proveru na Linux mašini koristeći Lynis! Za one koji ne znaju **Lynis,** to je mali alat za komandnu liniju koji će analizirati konfiguraciju vašeg servera i dati preporuke za **poboljšanje bezbednosti vaše mašine.**



Lynis je alat otvorenog koda od CISOFY, kompanije specijalizovane za **reviziju sistema i očvršćavanje**. Ako želite da napredujete u očvršćavanju Linux-a i popularnih servisa (SSH, Apache2, itd.), Lynis je vaš saveznik! Lynis ne samo da vam govori šta nije u redu, već pruža i preporuke kako bi vas usmerio na pravi put (i uštedeo vam vreme).



**Lynis** radi sa većinom Linux distribucija, uključujući: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis je namenjen korisnicima Linux / UNIX sistema, ali je takođe kompatibilan sa **macOS**. Veoma brzo se instalira, bez upravljanja zavisnostima na nivou paketa.



Koristi se za razne svrhe:





- Bezbednosne provere
- Testiranje usklađenosti (PCI, HIPAA i SOX)
- Složenije konfiguracije sistema
- Otkrivanje ranjivosti



Alat se široko koristi od strane različitih korisnika, uključujući sistemske administratore, IT revizore i pentestere. Za analize, alat se zasniva na standardima kao što su **CIS Benchmark, NIST, NSA, OpenSCAP** i na zvaničnim preporukama od **Debian, Gentoo, Red Hat**.



Projekat je dostupan na ovom Address na **Github** :





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Preuzmite Lynis sa CISOFY](https://cisofy.com/lynis/#download)



U ovom vodiču korak po korak, koristiću **VPS sa Debian 12** i fokusiraću se na deo sa SSH, jer bih želeo da proverim njegovu konfiguraciju i unapredim je.



## II. Preuzimanje i instalacija



Postoji nekoliko načina za preuzimanje i instalaciju Lynis-a. Izaberite onaj koji vam najviše odgovara sa liste ispod.



### A. Instalacija iz Debian repozitorijuma



Ovaj način instalacije omogućava vam da koristite komandu **lynis** sa bilo kog mesta u sistemu, za razliku od instalacije iz izvornog koda, gde morate biti locirani u direktorijumu.



Povežite se sa svojim serverom putem SSH i unesite sledeće komande da instalirate Lynis :



```
sudo apt-get update
sudo apt-get install lynis -y
```



Ovo je ono što dobijaš:



![Image](assets/fr/024.webp)



### B. Preuzmite sa zvanične veb stranice



Takođe ga možete preuzeti sa vebsajta Cisofy:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Ovo je ono što dobijaš:



![Image](assets/fr/032.webp)



Dalje, raspakovaćemo arhivu koristeći sledeću komandu:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Ovo je ono što dobijaš:



![Image](assets/fr/020.webp)



Hajde da pređemo u fasciklu **lynis**:



```
cd lynis
```



Možemo proveriti ažuriranja sledećom komandom:



```
./lynis update info
```



Ovo je ono što dobijaš:



![Image](assets/fr/023.webp)



### C. Preuzmi sa GitHuba



Preuzećemo **Lynis** iz zvaničnog GitHub repozitorijuma, koristeći sledeću komandu (*git* mora biti prisutan na vašem računaru):



```
git clone https://github.com/CISOfy/lynis.git
```



Ovo je ono što dobijaš:



![Image](assets/fr/060.webp)



## III. Korišćenje Lynis



Lynis je prisutan na našoj mašini, pa hajde da naučimo kako da ga koristimo!



### A. Glavne kontrole i opcije



Da biste prikazali dostupne komande, jednostavno unesite sledeću komandu:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe :
./lynis
```



Ovo je ono što dobijaš:



![Image](assets/fr/039.webp)



I takođe dobijaš sledeće opcije:



![Image](assets/fr/040.webp)



Da biste prikazali sve dostupne komande, unesite sledeću komandu:



```
sudo lynis show
```



Ovo je ono što dobijaš:



![Image](assets/fr/022.webp)



Ako želite prikazati sve opcije, morate uneti :



```
sudo lynis show options
```



Ovo je ono što dobiješ:



![Image](assets/fr/021.webp)



U ostatku ovog članka, naučićemo kako koristiti određene opcije.



### B. Izvođenje sistemske revizije



Tražićemo od **Lynis**-a da izvrši reviziju našeg sistema, ističući šta je ispravno konfigurisano i šta bi moglo biti poboljšano. Da biste to uradili, unesite sledeću komandu:



```
sudo lynis audit system
# ou
./lynis audit system
```



Podrazumevano, ako niste prijavljeni kao root kada pokrenete ovu komandu, alat će se pokrenuti sa privilegijama trenutno prijavljenog korisnika. Neki testovi neće biti pokrenuti u ovom kontekstu:



![Image](assets/fr/052.webp)



Evo testova koji neće biti izvedeni u ovom režimu:



![Image](assets/fr/051.webp)



Jednom kada je komanda izvršena, analiza počinje. Samo sačekajte trenutak.



Na kraju revizije, dobijate ovo (možemo videti da je **Lynis** ispravno identifikovao sistem **Debian 12** i koristiće **Debian plugin** za analizu):



![Image](assets/fr/017.webp)



Dalje, Lynis će navesti skup tačaka koje odgovaraju svemu što je proverio na našem sistemu. Ovo je organizovano po kategorijama, kao što ćemo videti. Takođe je vredno napomenuti da se koristi kod boja za isticanje preporuka:





- Crveno** za kritične Elements ili nepoštovanje najboljih praksi (na primer, nedostaje paket), tj. vaš server ne poštuje ovu tačku
- Žuto** za sugestije ili delimičnu usklađenost sa preporukom (recimo da je plus ispuniti tačku istaknutu ovom bojom (neprioritetno))
- Green** za tačke gde je konfiguracija vašeg servera usklađena
- Bela**, kada je neutralna



Ovde možemo videti da Lynis preporučuje instalaciju **fail2ban**:



![Image](assets/fr/057.webp)



U odeljku "**Boot and services**" vidimo da bi zaštita servisa putem *systemd*-a mogla biti poboljšana. S pozitivne strane, Grub2 je prisutan i nema problema sa dozvolama na :



![Image](assets/fr/029.webp)



Zatim imate odeljke "**Kernel**" i "**Memory and Processes**":



![Image](assets/fr/037.webp)



Dalje, odeljak "**Korisnici, Grupe i Autentifikacija**". Alat nas obaveštava o upozorenju na dozvole direktorijuma "**/etc/sudoers.d**". Za sada ne znamo više, ali ćemo moći da vidimo koja je preporuka na kraju analize.



![Image](assets/fr/049.webp)



Evo šta možete pronaći u odeljcima "**Shells", "Files Systems", and "USB Devices "**. Između ostalog, možemo videti da postoje predlozi za tačke montiranja i da su USB uređaji trenutno dozvoljeni na ovoj mašini.



![Image](assets/fr/048.webp)



Dalje, odeljci: "**Name services", "Ports and packages", "Networking".** Ovde se navodi da paketi koji se više ne koriste mogu biti uklonjeni i da ne postoji alat sposoban za upravljanje automatskim ažuriranjima.



![Image](assets/fr/058.webp)



Možemo videti da je firewall aktiviran (i da, tu je iptables!). Pored toga, možemo videti da je pronašao neiskorišćena pravila i da je instaliran Apache web server.



![Image](assets/fr/055.webp)



Ovo prati analiza samog veb servera, pošto je usluga identifikovana.



Možemo videti da je pronašao **Nginx** konfiguracione fajlove, i da su za SSL/TLS deo, **šifre** konfigurisane korišćenjem protokola koji bi bio nesiguran. S druge strane, prema Lynis-u, upravljanje logovima je ispravno.



![Image](assets/fr/038.webp)



SSH usluga je prisutna na mom VPS serveru. Njenu konfiguraciju analizira Lynis. Treba reći da se sigurnost SSH-a može lako poboljšati! Vratit ćemo se na ovo područje detaljno kada dobijemo preporuke.



![Image](assets/fr/026.webp)



Evo sekcija **"SNMP Support", "Databases", "PHP", "Squid Support", "LDAP Services", "Logging and files "**.



Postoji jedan zaista važan predlog u vezi sa upravljanjem logovima: snažno se preporučuje da ne čuvate logove samo lokalno na vašem računaru. Ako bi napadač kompromitovao računar, verovatno bi pokušao da izbriše svoje tragove... Zato treba da eksternalizujemo logove.



![Image](assets/fr/050.webp)



Ovde imamo reviziju ranjivih usluga, upravljanja nalozima, zakazanih zadataka i NTP sinhronizacije. naznačeno je da je nivo nizak na delu za baner i identifikaciju: ovo je razumljivo, ako prikažete verziju sistema, to daje naznaku potencijalnom napadaču. Ovo je podrazumevana postavka.



Bilo bi zanimljivo aktivirati **auditd** kako bismo imali logove u slučaju **forenzičke** analize. Takođe se proverava i **NTP**, jer je za efikasno pretraživanje logova poželjno da sistemi budu tačno podešeni, što pojednostavljuje pretragu.



![Image](assets/fr/036.webp)



Lynis zatim gleda na kriptografski Elements, virtualizaciju, kontejnere i sigurnosne okvire. Neki delovi su prazni jer nema podudarnosti sa analiziranom mašinom. Međutim, možemo videti da imam dva istekla SSL sertifikata i da nisam aktivirao **SELinux**.



![Image](assets/fr/027.webp)



Ovde takođe ima prostora za poboljšanje: nema anti-virusnog ili anti-malware skenera, a imamo i predloge za dozvole datoteka.



![Image](assets/fr/028.webp)



Dalje, Lynis se fokusira na pooštravanje konfiguracije Linux kernela (uključujući pravila za IPv4 stog), kao i na upravljanje "Home" direktorijumima Linux mašine.



![Image](assets/fr/035.webp)



Došli smo do kraja analize... Ova poslednja tačka pokazuje da bismo imali sve da dobijemo instaliranjem ClamAV-a na ovu mašinu.



![Image](assets/fr/030.webp)



## IV. Preporuke



Nakon revizije, vreme je da pročitate i analizirate preporuke. Ovde dobijamo preporuke i objašnjenja za svaki od testova koje je sproveo Lynis.



Uzmimo za primer preporuke za SSH. **Za svaki predlog, pronaći ćete preporučeni parametar i link koji će objasniti bezbednosnu tačku** Na vama je da odlučite, u zavisnosti od vašeg konteksta i upotrebe.



Hajde da pogledamo nekoliko primera preporuka koje direktno odražavaju tačke istaknute tokom revizije...



### A. Primeri preporuka





- Kao što smo ranije videli, NTP je važan za vremensko označavanje logova:



![Image](assets/fr/043.webp)





- Lynis takođe predlaže instaliranje paketa **apt-listbugs** kako biste dobili informacije o kritičnim greškama tokom instalacije paketa putem **apt.**



![Image](assets/fr/041.webp)





- Alat predlaže da instaliramo **needrestart da bismo mogli** videti koji procesi koriste staru verziju biblioteke i treba ih restartovati.



![Image](assets/fr/054.webp)





- Ovaj predlog predlaže instalaciju **fail2ban** kako bi se automatski blokirali hostovi koji ne uspevaju da se autentifikuju (posebno brute force napadi).



![Image](assets/fr/044.webp)





- Da bismo očvrsnuli sistemske usluge, preporučuje da pokrenemo plavu komandu za svaku uslugu na našem računaru.



![Image](assets/fr/056.webp)





- Predlaže postavljanje datuma isteka za sve zaštićene lozinke naloga.



![Image](assets/fr/031.webp)





- Ovaj predlog predlaže postavljanje minimalnih i maksimalnih vrednosti za starost lozinke. Između ostalog, ovo će osigurati da se lozinke redovno menjaju.



![Image](assets/fr/042.webp)





- Preporučujemo korišćenje zasebnih particija, kako biste ograničili uticaj problema sa prostorom na disku na jednu particiju.



![Image](assets/fr/047.webp)





- Ova preporuka sugeriše onemogućavanje USB skladišta i firewire-a kako bi se sprečilo curenje podataka.



![Image](assets/fr/033.webp)





- Da biste ispunili ovu preporuku, jednostavno instalirajte i konfigurišite **unnatended-upgrade**, na primer.



![Image](assets/fr/053.webp)



### B. Instaliranje preporučenih paketa



Da bismo poboljšali konfiguraciju sistema, instaliraćemo neke pakete na mašinu: neke koje preporučuje Lynis, a neke koje lično preporučujem.



Imaćete dobru osnovu za rad, sve dok odvojite malo vremena za njihovu konfiguraciju. Da biste to učinili, pogledajte IT-Connect sajt, druge članke na Webu i dokumentaciju alata.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Neke informacije o instaliranim paketima :





- Clamav** je antivirus.
- unattend-upgrades** će vam omogućiti da automatski upravljate svojim ažuriranjima i čak restartujete mašinu ili automatski očistite stare pakete, potpuno je podesiv.
- rkhunter** je anti-rootkit koji skenira vaš fajl sistem.
- Fail2ban** će se oslanjati na vaše log fajlove prema onome što mu date da pročita i radiće sa **iptables**, na primer da zabrani IP adrese koje pokušavaju da "brute force-uju" vaš server preko SSH.



### C. Preporuke za SSH



Hajde da pogledamo preporuke za SSH. One su navedene ispod. Ne brinite, odmah ćemo objasniti kako poboljšati konfiguraciju.



![Image](assets/fr/034.webp)



Hajde da detaljnije pogledamo moju trenutnu **SSH** konfiguraciju u :**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



Konfiguracija predložena u nastavku još uvek može biti optimizovana, ali vam daje dobru osnovu. *Imajte na umu da sam uklonio određeni broj komentara radi bolje čitljivosti*.



Mi ćemo :





- Promenite port za SSH konekciju (zaboravite podrazumevani 22)
- Povećajte nivo detaljnosti logova, sa **INFO na VERBOSE**
- Postavite **LoginGraceTime** na **2 minuta**



Ako se informacije o povezivanju ne unesu u roku od dva minuta, veza se prekida.





- Aktiviraj **strictModes**



Navodi da li "sshd" treba da proveri režime i vlasnika korisničkih fajlova, kao i korisnički matični direktorijum pre nego što validira konekciju. Ovo je obično poželjno, jer ponekad početnici slučajno ostave svoj direktorijum ili fajlove potpuno dostupne svima. Podrazumevana vrednost je "yes".





- Postavite **MaxAuthtries** na 3



Ovo predstavlja broj neuspelih pokušaja autentifikacije pre nego što se komunikacija prekine.





- Postavite **MaxSessions** na 2



Ovo predstavlja maksimalan broj istovremenih sesija.





- Omogući autentifikaciju javnim ključem



```
PubkeyAuthentication yes
```





- Zadrži autentifikaciju lozinkom :



```
PasswordAuthentication yes
```



Zabraniti prazne lozinke i **Kerberos** autentifikaciju, kao i **direktnu root autentifikaciju**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Uverite se da imate "**PermitRootLogin no", ako je jednako "yes", to je "apsolutno zlo "**.





- Zabraniti preusmeravanje TCP konekcije



```
AllowTcpForwarding no
```



Ukazuje da li su TCP preusmerenja dozvoljena, sa "da" kao podrazumevanim podešavanjem. Molimo obratite pažnju: onemogućavanje TCP preusmerenja ne poboljšava bezbednost ako korisnici imaju pristup ljusci, jer i dalje mogu postaviti sopstvene alate za preusmeravanje.





- Zabraniti X11 preusmeravanje



```
X11Forwarding no
```



Ukazuje da li su X11 preusmerenja prihvaćena, sa "ne" kao podrazumevanim podešavanjem. Molimo obratite pažnju: čak i ako su X11 preusmerenja onemogućena, to ne povećava sigurnost, jer korisnici i dalje mogu postaviti sopstvene preusmerivače. X11 preusmerenje je automatski onemogućeno ako je odabrano **UseLogin**.





- Podesite vreme čekanja komunikacije između klijenta i sshd



```
ClientAliveInterval  300
```



Definiše vremensko ograničenje u sekundama, nakon kojeg, ako podaci nisu primljeni od klijenta, sshd servis šalje poruku zahtevajući odgovor od klijenta. Podrazumevano, ova opcija je postavljena na "0", što znači da ove poruke nisu poslate klijentu. Samo verzija 2 SSH protokola podržava ovu opciju.



```
ClientAliveCountMax 0
```



Prema [dokumentaciji (*man stranici*) za sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html), ovo je značenje ove opcije: "Postavlja broj poruka zadržavanja (vidi gore) koje treba poslati bez odgovora od klijenta za **sshd**. Ako se ovaj prag dostigne dok su poruke zadržavanja poslate, **sshd** prekida vezu sa klijentom i završava sesiju. Važno je napomenuti da su ove poruke zadržavanja veoma različite od opcije **KeepAlive** (ispod). Poruke zadržavanja veze se šalju kroz šifrovani tunel, i stoga nisu falsifikovane. Zadržavanje veze na TCP nivou omogućeno opcijom **KeepAlive** je falsifikovano. Mehanizam zadržavanja veze je od interesa kada klijent ili server treba da zna da li je veza neaktivna."





- Sprečite otkrivanje informacija onemogućavanjem **motd, banner, lastlog**



```
PrintMotd no
```



Određuje da li sshd treba da prikaže sadržaj datoteke "/etc/motd" kada se korisnik prijavi u interaktivnom režimu. Na nekim sistemima, ovaj sadržaj može takođe biti prikazan od strane ljuske, putem /etc/profile ili slične datoteke. Podrazumevana vrednost je "yes".



```
Banner none
```



Vredi napomenuti da je u nekim jurisdikcijama slanje poruke pre autentifikacije možda preduslov za pravnu zaštitu. Sadržaj specificirane datoteke se prenosi udaljenom korisniku pre nego što se odobri autorizacija veze. Ova opcija treba da bude konfigurisana, jer po defaultu nijedna poruka neće biti prikazana.



Na slikama, ovo daje :



![Image](assets/fr/019.webp)



### D. Rezultat revizije



Konačno, ne zaboravimo da proverimo **Lynis audit score**! Vidimo da je **moj Hardening score 63** i da se izveštaj može pogledati u "**/var/log/lynis-report.dat**". Tu je i fajl "**/var/log/lynis.log**".



**Drugim rečima, što je viši rezultat, to bolje! Stoga treba da radite na svojoj konfiguraciji kako biste postigli najviši mogući rezultat, dok omogućavate vašoj mašini i hostovanim uslugama da funkcionišu normalno (što znači sprovođenje funkcionalnih testova).



![Image](assets/fr/046.webp)



Hajde da pogledamo rezultate na mom drugom serveru, gde sam proveo malo više vremena na učvršćivanju! Tako da je normalno da je rezultat viši (**76**).



![Image](assets/fr/045.webp)



## V. Lynis automatizovano planiranje



**Lynis** takođe nudi opciju pokretanja provera putem zakazanog zadatka. U stvari, postoji opcija **"--cronjob "**, koja će pokrenuti sve Lynis testove bez potrebe za validacijom ili akcijom korisnika. Zatim možete vrlo jednostavno kreirati skriptu koja će pokrenuti **Lynis** i staviti izlaz u fajl sa vremenskom oznakom i imenom odgovarajućeg servera. Evo fajla ovog tipa koji možete staviti u folder */etc/cron.daily*:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



Promenljiva **"AUDITOR_NAME "** je jednostavno promenljiva koju ćemo postaviti u opciji **"--auditor "** alata **Lynis** kako bi se ovo ime prikazalo u izveštaju:



![Image](assets/fr/059.webp)



Takođe ćemo kreirati nekoliko kontekstualnih promenljivih koje će nam pomoći da se bolje organizujemo, kao što su ime hosta i datum za imenovanje izveštaja i vremensko obeležavanje, kao i putanja do foldera u koji želimo da stavimo naše izveštaje.



## VI. Zaključak



Lynis je veoma praktičan alat koji će vam pomoći da uštedite vreme i budete efikasniji kada želite da saznate više o stanju konfiguracije Linux servera, posebno u smislu bezbednosti. Međutim, ne zaboravite da svaka izmena mora biti testirana pre nego što se primeni u produkciji, uzimajući u obzir vašu sopstvenu upotrebu i kontekst.



Verovatno nećete primeniti istu konfiguraciju za VPS izložen mreži, gde vam je potrebna samo jedna SSH veza (jer ste vi jedina osoba koja se povezuje), za razliku od **bastiona** ili **planera** koji će morati da umnože **SSH.** konekcije.



Kada imate konfiguraciju koja vam odgovara u smislu očvršćavanja, preporučljivo je usvojiti alat za automatizaciju kako ne biste morali ponovo ručno obavljati zadatke, jer bi to bilo dugotrajno i sklono greškama. Na primer, možete koristiti **: Puppet, Chef, Ansible, itd...**



Ne zaboravite da komunicirate sa svojim timovima pre implementacije: potrebno je da im objasnite zašto pravite ove promene, a ne samo da im kažete da ih pravite. Na kraju, cilj će biti da prenesete dobre prakse, i to će povećati vaše šanse za uspeh.



Konačno, možete uporediti **Lynis** sa drugim alatima, kojih ima nekoliko. Ako želite preći na centralizovano upravljanje, a da ostanete open source, preporučujem alat [Wazuh] (https://wazuh.com/).



**Ovaj vodič je završen, zabavite se sa Lynis!