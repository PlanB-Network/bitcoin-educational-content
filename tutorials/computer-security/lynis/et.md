---
name: Lynis
description: Linuxi masina turvaauditi teostamine Lynisiga
---
![cover](assets/cover.webp)



___



*See õpetus põhineb Fares CHELLOUGi originaalsel sisul, mis on avaldatud [IT-Connect](https://www.it-connect.fr/). Litsents [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Originaaltekstis võib olla tehtud muudatusi.*



___



## I. Esitlus



**Selles õpetuses õpime, kuidas teha Linuxi masina turvaauditit Lynise abil! Neile, kes ei tea **Lynis't,** on väike käsurea utiliit, mis analüüsib teie serveri konfiguratsiooni ja annab soovitusi **masinate turvalisuse parandamiseks**



Lynis on avatud lähtekoodiga tööriist CISOFY-lt, mis on spetsialiseerunud **süsteemi auditeerimisele ja karastamisele**. Kui soovite teha edusamme Linuxi ja populaarsete teenuste (SSH, Apache2 jne) karastamisel, siis Lynis on teie liitlane! Lynis mitte ainult ei ütle teile, mis on valesti, vaid annab ka soovitusi, mis suunavad teid õigesse suunda (ja säästavad aega).



**Lynis** töötab enamiku Linuxi distributsioonidega, sealhulgas: *lynis** töötab järgmiste süsteemidega: *Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis on suunatud Linuxi / UNIXi kasutajatele, kuid on ka **macOS** ühilduv. Väga kiire installeerimine, pakettide tasemel ei ole sõltuvushaldust.



Seda kasutatakse mitmesugustel eesmärkidel:





- Ohutusauditid
- Vastavustestimine (PCI, HIPAA ja SOX)
- Karmimad süsteemikonfiguratsioonid
- Haavatavuse tuvastamine



Tööriista kasutavad laialdaselt paljud kasutajad, sealhulgas süsteemiadministraatorid, IT-audiitorid ja pentestrid. Analüüside tegemiseks põhineb tööriist sellistel standarditel nagu **CIS Benchmark, NIST, NSA, OpenSCAP** ja **Debian, Gentoo, Red Hat** ametlikel soovitustel.



Projekt on saadaval aadressil Address **Github**:





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Lae Lynis alla CISOFY-st](https://cisofy.com/lynis/#download)



Selles samm-sammult õpetuses kavatsen **kasutada VPS-i, millel töötab Debian 12** ja keskendun SSH osale, kuna soovin kontrollida selle konfiguratsiooni ja parandada seda.



## II. Allalaadimine ja paigaldamine



Lynise allalaadimiseks ja installimiseks on mitu võimalust. Valige allolevast nimekirjast see, mida te eelistate.



### A. Paigaldamine Debiani repositooriumidest



See paigaldusrežiim võimaldab teil kasutada käsku **lynis** ükskõik kust süsteemis, erinevalt installeerimisest lähtekohast, kus te peate asuma kataloogis.



Ühendage oma serveriga SSH kaudu ja sisestage Lynise installimiseks järgmised käsud:



```
sudo apt-get update
sudo apt-get install lynis -y
```



See on see, mida sa saad:



![Image](assets/fr/024.webp)



### B. Laadige alla ametlikust veebisaidist



Seda saab alla laadida ka Cisofy veebisaidilt:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



See on see, mida sa saad:



![Image](assets/fr/032.webp)



Järgmisena pakime arhiivi lahti, kasutades järgmist käsku:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



See on see, mida sa saad:



![Image](assets/fr/020.webp)



Liigume kausta **lynis**:



```
cd lynis
```



Uuendusi saame kontrollida järgmise käsuga:



```
./lynis update info
```



See on see, mida sa saad:



![Image](assets/fr/023.webp)



### C. Lae alla GitHubist



Laenutame **Lynise** ametlikust GitHubi repositooriumist, kasutades järgmist käsku (*git* peab olema teie masinas olemas):



```
git clone https://github.com/CISOfy/lynis.git
```



See on see, mida sa saad:



![Image](assets/fr/060.webp)



## III. Lynise kasutamine



Lynis on meie masinas olemas, nii et õppigem seda kasutama!



### A. Peamised juhtimisseadmed ja valikud



Kättesaadavate käskude kuvamiseks sisestage lihtsalt järgmine käsk:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe:
./lynis
```



See on see, mida sa saad:



![Image](assets/fr/039.webp)



Lisaks on teil järgmised võimalused:



![Image](assets/fr/040.webp)



Kõigi olemasolevate käskude kuvamiseks sisestage järgmine käsk:



```
sudo lynis show
```



See on see, mida sa saad:



![Image](assets/fr/022.webp)



Kui soovite kuvada kõiki valikuid, peate sisestama:



```
sudo lynis show options
```



See on see, mida sa saad:



![Image](assets/fr/021.webp)



Selle artikli ülejäänud osas õpime, kuidas teatud võimalusi kasutada.



### B. Süsteemiauditi läbiviimine



Me palume **Lynisel** auditeerida meie süsteemi, tuues välja, mis on õigesti konfigureeritud ja mida võiks parandada. Selleks sisestage järgmine käsk:



```
sudo lynis audit system
# ou
./lynis audit system
```



Vaikimisi, kui te ei ole selle käsu käivitamisel sisse logitud root'ina, käivitub tööriist hetkel sisselogitud kasutaja õigustega. Mõned testid ei käivitata selles kontekstis:



![Image](assets/fr/052.webp)



Siin on testid, mida selles režiimis ei tehta:



![Image](assets/fr/051.webp)



Kui käsk on täidetud, algab analüüs. Lihtsalt oodake hetk.



Auditi lõpus saate selle (näeme, et **Lynis** on õigesti tuvastanud **Debian 12** süsteemi ja kasutab analüüsiks **Debian plugin**):



![Image](assets/fr/017.webp)



Järgnevalt loetleb Lynis punktid, mis vastavad kõigele, mida ta on meie süsteemis kontrollinud. See on korraldatud kategooriate kaupa, nagu me näeme. Samuti tasub märkida, et soovituste esiletõstmiseks kasutatakse värvikoodi:





- Punane** kriitilise Elements või parimate tavade mittejärgimise korral (näiteks puuduv pakett), st teie server ei järgi seda punkti
- Kollane** soovituste või soovituse osalise täitmise puhul (ütleme, et selle värviga esile tõstetud punkti täitmine on plussiks (mitteprioriteetne))
- Green** punktide puhul, kus teie serveri konfiguratsioon on vastavuses
- Valge**, kui see on neutraalne



Siin näeme, et Lynis soovitab paigaldada **fail2ban**:



![Image](assets/fr/057.webp)



Jaotises "**Boot ja teenused**" näeme, et teenuste kaitset *systemd* kaudu võiks parandada. Positiivne on see, et Grub2 on olemas ja probleeme õiguste osas ei ole:



![Image](assets/fr/029.webp)



Seejärel on teil jaotised "**Kernel**" ja "**Mälu ja protsessid**":



![Image](assets/fr/037.webp)



Järgmisena tuleb jaotis "**Kasutajad, rühmad ja autentimine**". Tööriist teavitab meid hoiatusest kataloogi "**/etc/sudoers.d**" õiguste kohta. Hetkel ei tea me rohkem, kuid analüüsi lõpus saame näha, milline on soovitus.



![Image](assets/fr/049.webp)



Siin on, mida leiate jaotistest "**Koored", "Failisüsteemid" ja "USB-seadmed "**. Muuhulgas näeme, et on olemas ettepanekud mount-punktide kohta ja et USB-seadmed on sellel masinal praegu lubatud.



![Image](assets/fr/048.webp)



Järgnevalt jaotised: "Siin on märgitud, et pakette, mida enam ei kasutata, võib kustutada ja et puudub utiliit, mis suudaks automaatseid uuendusi hallata.



![Image](assets/fr/058.webp)



Näeme, et tulemüür on aktiveeritud (ja jah, seal on iptables!). Lisaks näeme, et ta on leidnud kasutamata reeglid ja et Apache'i veebiserver on paigaldatud.



![Image](assets/fr/055.webp)



Sellele järgneb veebiserveri enda analüüs, kuna teenus on tuvastatud.



Näeme, et ta on leidnud **Nginxi** konfiguratsioonifailid ja et SSL/TLS osa puhul on **ciphers** konfigureeritud protokolliga, mis oleks ebaturvaline. Teisest küljest on Lynise sõnul logihaldus korrektne.



![Image](assets/fr/038.webp)



SSH teenus on minu VPS serveris olemas. Selle konfiguratsiooni analüüsib Lynis. Tuleb öelda, et SSH turvalisust saab kergesti parandada! Me tuleme selle valdkonna juurde üksikasjalikult tagasi, kui oleme saanud soovitused.



![Image](assets/fr/026.webp)



Siin on jaotised **"SNMP tugi", "Andmebaasid", "PHP", "Squid tugi", "LDAP teenused", "Logimine ja failid "**.



Logihalduse kohta on üks väga oluline soovitus: on tungivalt soovitatav, et te ei hoiaks logisid ainult lokaalselt oma masinas. Kui masin oleks ründaja poolt rikutud, siis on tõenäoline, et ta üritaks oma jäljed kustutada... Seega tuleb logid externaliseerida.



![Image](assets/fr/050.webp)



Siin on meil haavatavate teenuste, kontohalduse, plaaniliste ülesannete ja NTP sünkroniseerimise audit. bänneri ja identifitseerimise osas on märgitud, et tase on madal: see on arusaadav, kui kuvatakse süsteemi versiooni, annab see potentsiaalsele ründajale märku. See on vaikimisi seadistus.



Oleks huvitav aktiveerida **auditd**, et saada logisid **ekspertiisi** korral. **NTP** on samuti kontrollitud, sest logide tõhusaks otsimiseks on soovitav, et süsteemid oleksid õigel ajal, mis lihtsustab otsingut.



![Image](assets/fr/036.webp)



Seejärel vaatleb Lynis krüptograafilist Elements, virtualiseerimist, konteinereid ja turva raamistikke. Mõned lõigud on tühjad, sest puudub vastavus analüüsitava masinaga. Küll aga näeme, et mul on kaks aegunud SSL-sertifikaati ja ma ei ole **SELinux** aktiveerinud.



![Image](assets/fr/027.webp)



Ka siin on arenguruumi: puudub viirusetõrje ja pahavara skanner ning meil on soovitusi failiõiguste kohta.



![Image](assets/fr/028.webp)



Järgnevalt keskendub Lynis Linuxi kerneli konfigureerimise (sealhulgas IPv4 virna reeglite) ning Linuxi masina "Home" kataloogide haldamise karmistamisele.



![Image](assets/fr/035.webp)



Oleme jõudnud analüüsi lõppu... See viimane punkt näitab, et meil oleks kõik, mida ClamAVi olemasolu selles masinas võiks tuua.



![Image](assets/fr/030.webp)



## IV. Soovitused



Pärast auditit on aeg lugeda ja analüüsida soovitusi. Siinkohal saame soovitused ja selgitused iga Lynise poolt läbi viidud testi kohta.



Võtame näiteks SSH soovitused. **Ja iga soovituse kohta leiate soovitatud parameetri ja lingi, mis selgitab turvapunkti **See on teie otsustada, sõltuvalt teie kontekstist ja kasutamisest.



Vaatame mõned näited soovitustest, mis kajastavad otseselt kogu auditi käigus esile toodud punkte...



### A. Näited soovituste kohta





- Nagu me varem nägime, on NTP oluline logide ajatemplimiseks:



![Image](assets/fr/043.webp)





- Lynis soovitab paigaldada ka paketi **apt-listbugs**, et saada teavet kriitiliste vigade kohta pakettide paigaldamise ajal **apt.** kaudu



![Image](assets/fr/041.webp)





- Tööriist soovitab paigaldada **needrestart, et näha**, millised protsessid kasutavad raamatukogu vana versiooni ja vajavad taaskäivitamist.



![Image](assets/fr/054.webp)





- Selles soovituses soovitatakse paigaldada **fail2ban**, et automaatselt blokeerida hostid, mis ei suuda autentimist teostada (eelkõige brute force).



![Image](assets/fr/044.webp)





- Süsteemi teenuste karastamiseks soovitab ta käivitada sinise käsu iga teenuse jaoks meie masinas.



![Image](assets/fr/056.webp)





- Ta soovitab määrata kõigile kaitstud kontode paroolidele aegumiskuupäevad.



![Image](assets/fr/031.webp)





- Selles soovituses soovitatakse määrata parooli vanuse miinimum- ja maksimumväärtused. Muu hulgas tagab see, et paroole vahetatakse regulaarselt.



![Image](assets/fr/042.webp)





- Soovitame kasutada eraldi partitsioone, et piirata kettaruumiprobleemide mõju ühel partitsioonil.



![Image](assets/fr/047.webp)





- Selles soovituses soovitatakse andmete lekkimise vältimiseks USB-mäluseadmete ja firewire'i keelamine



![Image](assets/fr/033.webp)





- Selle soovituse täitmiseks installige ja seadistage lihtsalt näiteks **unnatended-upgrade**.



![Image](assets/fr/053.webp)



### B. Soovitatavate pakettide paigaldamine



Süsteemi konfiguratsiooni parandamiseks paigaldame masinasse mõned paketid: mõned neist on Lynise poolt soovitatud, mõned soovitan mina isiklikult.



Teil on hea alus, mille alusel töötada, kui te kulutate veidi aega nende seadistamisele. Selleks vaadake IT-Connecti veebisaiti, muid veebiartikleid ja tööriistade dokumentatsiooni.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Mõned andmed paigaldatud pakettide kohta:





- Clamav** on viirusetõrje.
- unattend-upgrades** võimaldab teil hallata oma uuendusi automaatselt ja isegi taaskäivitada masinat või automaatselt puhastada vanu pakette, see on täielikult konfigureeritav.
- rkhunter** on rootkitide vastane programm, mis skaneerib teie failisüsteemi.
- Fail2ban** tugineb teie logifailidele vastavalt sellele, mida annate talle lugeda, ja töötab koos **iptablesiga**, et keelata näiteks IP-aadressid, mis üritavad teie serverit SSH-süsteemis "brute force'i" kasutada.



### C. Soovitused SSH jaoks



Vaatame SSH soovitusi. Need on loetletud allpool. Ärge muretsege, me selgitame kohe, kuidas konfiguratsiooni parandada.



![Image](assets/fr/034.webp)



Vaatame lähemalt minu praegust **SSH** konfiguratsiooni:**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



Allpool soovitatud konfiguratsiooni saab veel optimeerida, kuid see annab teile hea aluse. *Pange tähele, et ma olen eemaldanud mitmeid kommentaare parema loetavuse huvides*.



Me:





- Muuda SSH-ühenduse port (unusta vaikimisi 22)
- Suurendada logide sõnastatuse taset **INFO-lt VERBOSE-le**
- Määra **LoginGraceTime** väärtuseks **2 minutit**



Kui kahe minuti jooksul ei sisestata ühenduse andmeid, ühendus katkestatakse.





- Aktiveeri **strictModes**



Määrab, kas "sshd" peaks enne ühenduse kinnitamist kontrollima kasutaja failide režiimi ja omanikku ning kasutaja kodukataloogi. See on tavaliselt soovitav, sest mõnikord jätavad algajad kogemata oma kataloogi või failid täielikult kõigile ligipääsetavaks. Vaikimisi on "yes".





- Määra **MaxAuthtries** väärtuseks 3



See näitab ebaõnnestunud autentimiskatsete arvu enne side sulgemist.





- Määra **MaxSessions** väärtuseks 2



See tähistab maksimaalset samaaegsete seansside arvu.





- Avaliku võtme autentimise lubamine



```
PubkeyAuthentication yes
```





- Säilitada parooliga autentimine:



```
PasswordAuthentication yes
```



Keelata tühjad paroolid ja **Kerberos** autentimine, samuti **direct root autentimine**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Veenduge, et teil on "**PermitRootLogin no", kui see on võrdne "yes", siis on see "absoluutne paha "**.





- Keelata TCP-ühenduse ümbersuunamine



```
AllowTcpForwarding no
```



Näitab, kas TCP ümbersuunamised on lubatud, vaikimisi on "jah". Pange tähele: TCP ümbersuunamiste keelamine ei suurenda turvalisust, kui kasutajatel on juurdepääs shell'ile, kuna nad saavad endiselt oma ümbersuunamisvahendeid seadistada.





- Keelata X11 ümbersuunamine



```
X11Forwarding no
```



Näitab, kas X11 ümbersuunamisi aktsepteeritakse, vaikimisi on "ei". Pange tähele: isegi kui X11 ümbersuunamised on keelatud, ei suurenda see turvalisust, kuna kasutajad saavad endiselt oma ümbersuunajad seadistada. X11 ümbersuunamine lülitatakse automaatselt välja, kui on valitud **UseLogin**.





- Määrake kliendi ja sshd vahelise suhtluse aegumistähtaeg



```
ClientAliveInterval  300
```



Määratleb ajaülevaate sekundites, mille järel, kui kliendilt ei ole andmeid saadud, saadab sshd teenus sõnumi, milles palub kliendilt vastust. Vaikimisi on see valik seatud väärtusele "0", mis tähendab, et neid sõnumeid kliendile ei saadeta. Ainult SSH-protokolli 2. versioon toetab seda valikut.



```
ClientAliveCountMax 0
```



Vastavalt [sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html) dokumentatsioonile (*man page*) tähendab see valik järgmist: "Seadistab **sshd** jaoks ilma kliendi vastuseta saadetavate ooteaegade arvu (vt eespool). Kui see künnis saavutatakse, kui oote sõnumid on saadetud, katkestab **sshd** kliendi ühenduse ja lõpetab seansi. Oluline on märkida, et need ootelesõnumid erinevad oluliselt **KeepAlive**-variandist (allpool). Ühenduse hoidmise sõnumid saadetakse läbi krüpteeritud tunneli ja seetõttu ei ole need võltsitavad. **KeepAlive** abil lubatud TCP-tasandi ühenduse hoidmine on võltsitav. Ühenduse hoidmise mehhanism on huvitav siis, kui klient või server peab teadma, kas ühendus on tühikäigul."





- Vältida teabe avalikustamist, lülitades välja **motd, banner, lastlog**



```
PrintMotd no
```



Määrab, kas sshd peaks näitama faili "/etc/motd" sisu, kui kasutaja logib sisse interaktiivses režiimis. Mõnes süsteemis võib selle sisu kuvada ka shell /etc/profile või sarnase faili kaudu. Vaikeväärtus on "yes".



```
Banner none
```



Tasub märkida, et mõnes jurisdiktsioonis võib sõnumi saatmine enne autentimist olla õiguskaitse eelduseks. Määratud faili sisu edastatakse kaugkasutajale enne ühenduse autoriseerimist. See valik tuleb konfigureerida, sest vaikimisi ei kuvata sõnumit.



Piltides annab see:



![Image](assets/fr/019.webp)



### D. Auditi tulemus



Lõpuks, ärme unusta kontrollida **Lynise auditi skoori**! Näeme, et **Minu Hardening score on 63** ja et aruande faili saab vaadata aadressil "**/var/log/lynis-report.dat**". Samuti on olemas fail "**/var/log/lynis.log**".



**Teisisõnu, mida kõrgem tulemus, seda parem! Seetõttu peate töötama oma konfiguratsiooni kallal, et saavutada võimalikult kõrge skoor, võimaldades samal ajal oma masina ja hostitud teenuste normaalset toimimist (mis tähendab funktsionaalsete testide läbiviimist).



![Image](assets/fr/046.webp)



Vaatame tulemusi minu teisel serveril, kus ma veetsin veidi rohkem aega karastamisele! Seega on normaalne, et tulemus on kõrgem (**76**).



![Image](assets/fr/045.webp)



## V. Lynis automatiseeritud planeerimine



**Lynis** pakub ka võimalust käivitada oma kontrolle plaanilise ülesande kaudu. Tegelikult on olemas valik **"--cronjob "**, mis käivitab kõik Lynise'i testid ilma valideerimise või kasutaja tegevuseta. Seejärel saate väga lihtsalt luua skripti, mis käivitab **Lynis** ja paneb väljundi ajamärgistatud faili, kus on kõnealuse serveri nimi. Siin on selline fail, mille võid panna */etc/cron.daily* kausta:



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



Muutuja **"AUDITOR_NAME "** on lihtsalt muutuja, mille me määrame **"--auditori "** valikuga **Lynis**, et see nimi kuvataks aruandes:



![Image](assets/fr/059.webp)



Me loome ka mõned kontekstilised muutujad, mis aitavad meil end paremini organiseerida, näiteks hostinimi ja kuupäev, mille järgi me raportile nime anname ja seda ajaliselt tembeldame, ning tee kausta juurde, kuhu me tahame oma aruanded panna.



## VI. Kokkuvõte



Lynis on väga praktiline tööriist, mis aitab teil säästa aega ja olla tõhusam, kui soovite rohkem teada Linuxi serveri konfiguratsiooni seisust, eriti turvalisuse osas. Kuid ärge unustage, et iga muudatus tuleb enne tootmises rakendamist testida, võttes arvesse teie enda kasutust ja konteksti.



Tõenäoliselt ei kasuta sa sama konfiguratsiooni võrgule avatud VPS-i puhul, kus sul on vaja ainult ühte SSH ühendust (sest sa oled ainus inimene, kes ühendab), erinevalt **bastionist** või **schedulerist**, mis vajavad mitmekordset **SSH.** ühendust



Kui olete saanud konfiguratsiooni, mis sobib teile karastamise mõttes, on soovitav võtta kasutusele automatiseerimisvahend, et te ei peaks ülesandeid käsitsi uuesti tegema, sest see oleks aeganõudev ja vigadega seotud. Näiteks võite kasutada **: Puppet, Chef, Ansible jne...**



Ärge unustage enne rakendamist oma meeskonnaga suhtlemist: te peate andma neile aru, miks te neid muudatusi teete, mitte lihtsalt ütlema neile, et te neid teete. Lõppkokkuvõttes on eesmärk anda edasi häid tavasid ja see suurendab teie eduvõimalusi.



Lõpuks saate võrrelda **Lynist** ka teiste vahenditega, mida on mitmeid. Kui soovite liikuda tsentraliseeritud haldamise suunas, jäädes samas avatud lähtekoodiga, siis soovitan [Wazuh] tööriista (https://wazuh.com/).



**See õpetus on lõppenud, lõbutsege koos Lynisega!