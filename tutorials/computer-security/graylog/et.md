---
name: Graylog
description: Tsentraliseerige ja analüüsige oma logisid hõlpsasti
---
![cover](assets/cover.webp)



___



*See õpetus põhineb Florian BURNELi originaalsel sisul, mis on avaldatud [IT-Connect](https://www.it-connect.fr/). Litsents [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Originaaltekstis võib olla tehtud muudatusi.*



___



## Graylogi kasutuselevõtt Debian 12 peal



### I. Esitlus



Graylog on avatud lähtekoodiga lahendus, mis on loodud masinate ja võrguseadmete logide tsentraliseerimiseks, salvestamiseks ja reaalajas analüüsimiseks. Selles õpetuses õpime, kuidas paigaldada Graylogi tasuta versiooni Debian 12 masinale!



Infosüsteemis genereerib iga **server**, olgu see siis **Linux** või **Windows**, ja iga **võrguseade** (kommutaator, ruuter, tulemüür jne...) **oma logisid**, mis salvestatakse lokaalselt. Kuna logid salvestatakse lokaalselt igas masinas, on sündmuste analüüs ja korrelatsioon väga keeruline... Siinkohal tuleb mängu **Graylog**. See toimib **logi neeldajana**, mis tähendab, et **kõik millised masinad saadavad talle oma logid** (näiteks syslogi kaudu). Graylog **salvestab ja indekseerib need logid**, võimaldades samal ajal teha globaalseid otsinguid ja luua hoiatusi.



Graylog on analüüsi- ja jälgimisvahend, mis lihtsustab kahtlase käitumise ja erinevate probleemide (stabiilsus, jõudlus jne) tuvastamist.




![Image](assets/fr/034.webp)



**Märkus: tasuta versioon **Graylog Open** ei ole SIEM nagu Wazuh, eriti kuna sellel puuduvad tõelised sissetungi tuvastamise funktsioonid.



### II. Eeltingimused



**stack Graylog** põhineb **mitmetel komponentidel**, mida me peame paigaldama ja konfigureerima. Siinkohal paigaldame kõik komponendid samasse serverisse, kuid on võimalik luua mitme sõlme baasil klastreid ja jaotada rollid mitme serveri vahel. Selle õpetuse jaoks paigaldame **Graylog 6.1**, mis on seni kõige uuem versioon.





- MongoDB 7**, praegune soovituslik versioon Graylogi jaoks (minimaalselt 5.0.7, maksimaalselt 7.x)
- OpenSearch**, Amazoni loodud avatud lähtekoodiga Fork Elasticsearchist (minimaalselt 1.1.x, maksimaalselt 2.15.x)
- OpenJDK 17**



**Graylogi server** töötab **Debian 12** peal, kuid paigaldamine on võimalik ka teistesse distributsioonidesse, sealhulgas Dockeri kaudu. Virtuaalmasinal on **8 GB RAM** ja **256 GB kettaruumi**, et kõigi komponentide jaoks oleks piisavalt ressursse (vastasel juhul võib see oluliselt mõjutada jõudlust). Ma annan selle siiski ligikaudse suunisena, sest **graylogi arhitektuuri suurus sõltub töödeldava teabe hulgast**. Graylog võib töödelda 30 MB või 300 MB andmeid päevas, aga ka 300 GB andmeid päevas... Tegemist on **skaalutava lahendusega**, mis suudab töödelda **terabaite logisid** (vt [see lehekülg](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Allikas: Graylog



Enne seadistamise alustamist määrake Graylogi masinale staatiline IP Address ja installige viimased uuendused. Seadistage kindlasti kohaliku masina ajavöönd ja määrake NTP-server kuupäeva ja kellaaja sünkroniseerimiseks. Siin on käsk, mida tuleb käivitada:



```
sudo timedatectl set-timezone Europe/Paris
```



**Märkus: **OpenSearchi paigaldamine on vabatahtlik**, kui kasutate selle asemel **Graylogi andmesõlme**.



### III Graylogi samm-sammuline paigaldamine



Alustame pakettide vahemälu uuendamisest ja järgnevaks vajaminevate tööriistade paigaldamisest.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. MongoDB paigaldamine



Kui see on tehtud, alustame MongoDB installimist. Laadige alla MongoDB repositooriumile vastav GPG võti:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Seejärel lisage MongoDB 6 repositoorium Debian 12 masinasse:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Järgmisena uuendame pakettide vahemälu ja üritame paigaldada MongoDB:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



MongoDB-d ei saa paigaldada, sest puudub sõltuvus: **libssl1.1**. Me peame selle paketi käsitsi paigaldama, enne kui saame jätkata, sest Debian 12 repositooriumides seda ei ole.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Laenutame DEB-paketi nimega "**libssl1.1_1.1.1.1f-1ubuntu2.23_amd64.deb**" (uusim versioon) käsuga **wget**, seejärel paigaldame selle käsuga **dpkg**. See annab järgmised kaks käsku:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Käivitage MongoDB paigaldus uuesti:



```
sudo apt-get install -y mongodb-org
```



Seejärel taaskäivitage MongoDB teenus ja lubage sellel automaatselt käivituda, kui Debian server käivitatakse.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Kui MongoDB on paigaldatud, võime liikuda edasi järgmise komponendi paigaldamise juurde.



#### B. OpenSearchi paigaldamine



Liigume edasi OpenSearchi paigaldamise juurde serverisse. Järgmine käsk lisab OpenSearchi pakettide allkirjastamise võtme:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Seejärel lisage OpenSearchi repositoorium, et saaksime seejärel paketi **apt** abil alla laadida:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Uuendage oma paketi vahemälu:



```
sudo apt-get update
```



Seejärel **installige OpenSearch**, hoolitsedes selle eest, et **määrata oma instantsi administraatori** konto jaoks vaikimisi parool. Siin on parool "**IT-Connect2024!**", kuid asendage see väärtus tugeva parooliga. **Vältige nõrku paroole** nagu "**P@ssword123**" ja kasutage vähemalt **8 tähemärki**, kus on vähemalt üks märk igast tüübist (väike- ja suurtähtedega, numbri- ja erimärgiga), vastasel juhul tekib paigaldamise lõpus viga. **See on eeltingimus alates OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Palun olge paigaldamise ajal kannatlik...



Kui olete lõpetanud, võtke hetkeks aega, et teostada minimaalne konfiguratsioon. Avage konfiguratsioonifail YAML-vormingus:



```
sudo nano /etc/opensearch/opensearch.yml
```



Kui fail on avatud, seadistage järgmised valikud:



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



See OpenSearchi konfiguratsioon on mõeldud ühe sõlme seadistamiseks. Siin on mõned selgitused erinevate parameetrite kohta, mida me kasutame:





- cluster.name: graylog**: see parameeter annab OpenSearchi klastrile nime "**graylog**".
- node.name: ${HOSTNAME}**: sõlme nimi määratakse dünaamiliselt, et see vastaks kohaliku Linuxi masina nimele. Isegi kui meil on ainult üks sõlmpunkt, on oluline, et see saaks õige nime.
- path.data: /var/lib/opensearch**: see tee määrab, kus OpenSearch salvestab oma andmeid kohalikul masinal, antud juhul "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: see tee määrab, kuhu OpenSearchi logifailid salvestatakse, siin "**/var/log/opensearch**".
- discovery.type: single-node**: see parameeter määrab, et OpenSearch töötaks ühe sõlmega, seega valitakse valik "**single-node**".
- network.host: 127.0.0.1**: see konfiguratsioon tagab, et OpenSearch kuulab ainult oma Interface kohalikku silmust, mis on piisav, kuna see on samas serveris kui Graylog.
- action.auto_create_index: false**: automaatse indeksi loomise keelamisega ei loo OpenSearch automaatselt indeksit, kui dokument saadetakse ilma olemasoleva indeksita.
- plugins.security.disabled: true**: see valik lülitab OpenSearchi turvaplugina välja, mis tähendab, et autentimist, juurdepääsu haldamist ja kommunikatsiooni krüpteerimist ei toimu. See seade säästab aega Graylogi seadistamisel, kuid seda tuleks vältida tootmises (vt [see lehekülg](https://opensearch.org/docs/1.0/security-plugin/index/)).



Mõned valikud on juba olemas, seega peate nende aktiveerimiseks lihtsalt eemaldama "#" ja seejärel märkima oma väärtuse. Kui te ei leia valikut, võite selle deklareerida otse faili lõpus.



![Image](assets/fr/023.webp)



Salvestage ja sulgege see fail.



#### C. Java seadistamine (JVM)



Te peate konfigureerima OpenSearchi kasutatava Java virtuaalmasina, et kohandada selle teenuse kasutatava mälu hulka. Redigeerige järgmist konfiguratsioonifaili:



```
sudo nano /etc/opensearch/jvm.options
```



Siin kasutatava konfiguratsiooni puhul **OpenSearch alustab 4 GB eraldatud mäluga ja võib kasvada kuni 4 GB**, nii et mälu ei muutu töö ajal. Siinkohal võetakse konfiguratsioonis arvesse asjaolu, et virtuaalmasinal on kokku **8 GB RAM**. Mõlemad parameetrid peavad olema sama väärtusega. See tähendab, et asendatakse read:



```
-Xms1g
-Xmx1g
```



Nende ridadega:



```
-Xms4g
-Xmx4g
```



Siin on pilt muudatusest, mis tuleb teha:



![Image](assets/fr/022.webp)



Sulgege see fail pärast salvestamist.



Lisaks peame kontrollima Linuxi tuuma parameetri "**max_map_count**" konfiguratsiooni. See määratleb protsessi kohta kaardistatud mälupiirkondade piiri, et rahuldada meie rakenduse vajadusi. **OpenSearch**, nagu ka Elasticsearch**, soovitab selle väärtuse seadmiseks "262144", et vältida mäluhaldusvigu.



Põhimõtteliselt on värskelt installeeritud Debian 12 masina väärtus juba õige. Aga kontrollime. Käivita see käsk:



```
cat /proc/sys/vm/max_map_count
```



Kui sa saad muu väärtuse kui "**262144**", käivitage järgmine käsk, vastasel juhul ei ole see vajalik.



```
sudo sysctl -w vm.max_map_count=262144
```



Lõpuks lubage OpenSearchi automaatne käivitamine ja käivitage sellega seotud teenus.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Kui te kuvate oma süsteemi olekut, peaksite nägema Java-protsessi, millel on 4 GB RAM-i.



```
top
```



![Image](assets/fr/029.webp)



Järgmine samm: kauaoodatud Graylogi paigaldamine!



#### D. Graylogi paigaldamine



Graylog 6.1** uusima versiooni **installeerimiseks käivitage järgmised 4 käsku, et **laadige alla ja installige Graylog Server**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Kui see on tehtud, peame enne käivitamist tegema mõned muudatused Graylogi konfiguratsioonis.



Alustame nende kahe valiku konfigureerimisest:





- password_secret**: seda parameetrit kasutatakse võtme määratlemiseks, mida Graylog kasutab kasutajate paroolide salvestamise turvamiseks (soolamisvõtme vaimus). See võti peab olema **unikaalne** ja **juhuslik**.
- root_password_sha2**: see parameeter vastab vaikimisi administraatori paroolile Graylogis. See on salvestatud Hash SHA-256 kujul.



Alustame 96-kohalise võtme genereerimisega parameetri **password_secret** jaoks:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Kopeerige tagastatud väärtus, seejärel avage Graylogi konfiguratsioonifail:



```
sudo nano /etc/graylog/server/server.conf
```



Sisestage võti parameetrisse **password_secret** järgmiselt:



![Image](assets/fr/027.webp)



Salvestage ja sulgege fail.



Järgmisena tuleb määrata vaikimisi loodud konto "**admin**" parool. Konfigureerimisfailis tuleb salvestada parooli Hash, mis tähendab, et see tuleb arvutada. Allpool toodud näites on esitatud parooli "**LogsWells@**" Hash: kohandage see väärtus oma parooliga.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Kopeeri saadud väärtus väljundiks (ilma sidekriipsuta rea lõpus).



Avage uuesti Graylogi konfiguratsioonifail:



```
sudo nano /etc/graylog/server/server.conf
```



Sisestage väärtus **root_password_sha2** valikusse järgmiselt:



![Image](assets/fr/026.webp)



Kui olete konfiguratsioonifailis, seadistage valik "**http_bind_address**". Määrake "**0.0.0.0:9000**", nii et Graylogi Interface veebi saab kasutada pordi **9000** kaudu mis tahes serveri IP Address kaudu.



![Image](assets/fr/024.webp)



Seejärel määra "**elasticsearch_hosts**" valikuks `http://127.0.0.1:9200`, et deklareerida meie kohalik OpenSearchi instants. See on vajalik, kuna me ei kasuta **Graylogi andmesõlme**. Ja ilma selle valikuta ei ole võimalik edasi minna...



![Image](assets/fr/025.webp)



Salvestage ja sulgege fail.



See käsk aktiveerib Graylogi, nii et see käivitub automaatselt järgmisel käivitamisel, ja käivitab kohe Graylogi serveri.



```
sudo systemctl enable --now graylog-server
```



Kui see on tehtud, proovige Graylogiga brauserist ühendust võtta. Sisestage serveri IP Address (või nimi) ja port 9000.



**Teavitamiseks:**



Mitte väga kaua aega tagasi ilmus Graylogi sisselogimisel alljärgnevale aknale sarnane autentimisaken, kui sa esimest korda Graylogi sisse logisid. Sa pidid sisestama oma kasutajanime "**admin**" ja parooli. Ja siis avastasite ebameeldivalt, et ühendus ei tööta.



![Image](assets/fr/031.webp)



Oli vaja minna tagasi Graylogi serveri käsureale ja vaadata logisid. Siis nägime, et **Esimeseks ühenduseks** on vaja **kasutada ajutist salasõna**, mis on määratud logides.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Seejärel pidite uuesti proovima ühendust kasutaja "**admin**" ja ajutise parooliga, mis võimaldas teil sisse logida!



**See ei ole enam nii. Kõik, mida peate tegema, on sisse logida oma admin-kontoga ja käsureal konfigureeritud parooliga



![Image](assets/fr/033.webp)



**Tervitan teid Graylogi Interface-sse!



![Image](assets/fr/019.webp)



#### E. Graylog: uue administraatori konto loomine



Selle asemel, et kasutada Graylogi poolt loodud administraatori kontot, saate luua oma isikliku administraatori konto. Klõpsake menüüs "**Süsteem**", seejärel "**Kasutajad ja meeskonnad**", et vajutada nupule "**Loo kasutaja**". Seejärel täitke vorm ja määrake oma kontole administraatori roll.



![Image](assets/fr/020.webp)



Isikupärastatud konto võib sisaldada lisateavet, näiteks ees- ja perekonnanime ning e-posti Address, erinevalt algupärasest administraatorikontost. Veelgi enam, see tagab parema jälgitavuse, kui iga isik töötab nimelise kontoga.



## Logide saatmine graylogi rsyslogi abil



### I. Esitlus



Selles teises osas õpime, kuidas konfigureerida Linuxi masinat saatma oma logisid Graylogi serverisse. Selleks paigaldame ja konfigureerime süsteemi Rsyslogi.



### II. Graylogi konfigureerimine Linuxi logide vastuvõtmiseks



Alustame Graylogi konfigureerimisest. Selleks on kolm sammu:





- **Sisendi** loomine, et luua sisenemispunkt, mis võimaldab Linuxi masinatel **saata Syslogi logisid UDP** kaudu.
- Uue **indeksi** loomine, et salvestada ja **indekseerida kõiki Linuxi logisid**.
- **Stream** loomine, et **suunata** Graylogi poolt saadud logid uude Linuxi indeksisse.



#### A. Syslogi sisendi loomine



Logige sisse Graylog Interface-sse, klõpsake menüüs "**Süsteem**" ja seejärel "**Sisendid**". Valige rippmenüüst "**Syslog UDP**", seejärel klõpsake nupul "**Launch new input**". Võimalik on luua ka TCP Syslog Input, kuid selleks on vaja kasutada TLS-sertifikaati: see on turvalisuse huvides kasulik, kuid seda ei käsitleta käesolevas artiklis.



![Image](assets/fr/001.webp)



Ekraanile ilmub nõustaja. Alustage, andes sellele sisendile nime, näiteks "**Graylog_UDP_Rsyslog_Linux**", ja valige port. Vaikimisi on port "**514**", kuid seda saab kohandada. Siin on valitud port "**12514**".



![Image](assets/fr/016.webp)



Samuti saate märkida valiku "**Täieliku sõnumi salvestamine**", et salvestada kogu logisõnum Graylogi. Klõpsake nuppu "**Launch Input**".



![Image](assets/fr/017.webp)



Uus sisend on loodud ja on nüüd aktiivne. Graylog saab nüüd vastu võtta Syslogi logisid portil 12514/UDP, kuid me ei ole veel rakenduse konfigureerimist lõpetanud.



![Image](assets/fr/018.webp)


**Märkus: ühte sisendit saab kasutada mitme Linuxi masina logide salvestamiseks.



#### B. Uue Linuxi indeksi loomine



Meil on vaja luua Graylogi indeks, et salvestada Linuxi masinate logisid. Graylogi **indeks** on salvestusstruktuur, mis sisaldab saadud logisid, st vastuvõetud sõnumeid. Graylog kasutab salvestusmootorina OpenSearch'i ja sõnumid indekseeritakse, et võimaldada kiiret ja tõhusat otsingut.



Klõpsake Graylogi menüüs "**Süsteem**" ja seejärel "**Indeksid**". Avaneval uuel lehel klõpsake nupule "**Loo indeksikomplekt**".



![Image](assets/fr/005.webp)



Nimetage see indeks, näiteks "**Linux Index**", lisage enne kinnitamist kirjeldus ja eesliide. Siin **salvestame kõik Linuxi logid sellesse indeksisse**. Samuti on võimalik luua spetsiifilisi indekseid, et salvestada ainult teatud logisid (ainult [SSH] logid (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), veebiteenuste logid jne).



![Image](assets/fr/006.webp)



Nüüd peame looma uue voo, et suunata sõnumeid sellesse indeksisse.



#### C. Loo oja



Uue voo loomiseks klõpsake Graylogi peamenüüs "**Streams**". Seejärel klõpsake paremal nupul "**Loo voog**". Ilmuvas aknas nimetage voog, näiteks "**Linux Stream**", ja valige väljal "**Index Set**" indeks "**Linux Index**". Kinnitage oma valik.



**Hoiatus: Sellele voole vastavad sõnumid lisatakse ka "**Eelduvoog**", kui te ei vali valikut "**Eemalda vasted 'Vaikimisi voost'**".



![Image](assets/fr/002.webp)



Seejärel klõpsake oma aurusätetes nupule "**Lisa voogureegel**", et lisada uus sõnumite suunamise reegel. Kui te ei leia seda akent, klõpsake menüüs "**Streams**", seejärel klõpsake oma voole vastaval real "**More**" ja seejärel "**Manage Rules**".



Valige tüüp "**vastav sisend**" ja valige eelnevalt loodud **Rsyslogi sisend UDP**. Kinnitage nupuga "**Loo reegel**". Kõik sõnumid meie uuele sisendile saadetakse nüüd Linuxi jaoks mõeldud indeksisse.



![Image](assets/fr/003.webp)



Teie uus voog peaks ilmuma loendisse ja see peaks olema olekus "**Toimiv**". Sõnumi ribalaius näitab "**0 msg/s**", kuna me ei saada praegu ühtegi logi Rsyslogi UDP-sisendisse. Voo logide vaatamiseks klõpsake lihtsalt selle nimele.



![Image](assets/fr/004.webp)



**Kõik on Graylogi poolel valmis**. Järgmine samm on Linuxi masina konfigureerimine.



### III. Rsyslogi paigaldamine ja seadistamine Linuxis



Logige Linuxi masinasse sisse, kas lokaalselt või eemalt, ja kasutage kasutajakontot, millel on õigused oma õiguste tõstmiseks (sudo abil). Vastasel juhul kasutage otse kontot "root".



#### A. Rsyslogi paketi paigaldamine



Alusta pakettide vahemälu uuendamisest ja paketi "**rsyslog**" paigaldamisest.



```
sudo apt-get update
sudo apt-get install rsyslog
```



Seejärel kontrollige teenuse staatust. Enamasti on see juba käivitatud.



```
sudo systemctl status rsyslog
```



#### B. Rsyslogi konfigureerimine



Rsyslogi peamine konfiguratsioonifail asub siin:



```
/etc/rsyslog.conf
```



Lisaks sellele kasutatakse kataloogi "**/etc/rsyslog.d/**" Rsyslogi täiendavate konfiguratsioonifailide salvestamiseks. Põhikonfiguratsioonifailis on olemas direktiiv Include, et importida kõik selles kataloogis asuvad "**.conf**" failid. See võimaldab Rsyslogi konfigureerimiseks täiendavaid faile ilma põhifaili muutmata.



Selles kataloogis tuleb laadimisjärjekorra määramiseks kasutada numbreid, sest failid laaditakse tähestikulises järjekorras. Numbrilise eesliite lisamine võimaldab teil hallata prioriteetsust mitme konfiguratsioonifaili vahel. Siin on meil ainult üks lisafail, nii et see ei ole probleemiks.



Selles kataloogis loome faili nimega "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



Sisestage sellesse faili järgmine rida:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Seda rida tuleb tõlgendada järgmiselt:





- `*.*`: tähendab, et saadab kõik Syslogi logid Linuxi masinast Graylogi.
- `@`: näitab, et transport toimub UDP-s. TCP-le üleminekuks tuleb märkida "**@@**".
- `192.168.10.220:12514`: näitab Graylogi serveri Address ja port, millele logid saadetakse (vastab sisendile).
- `RSYSLOG_SyslogProtocol23Format`: vastab Graylogile saadetavate sõnumite vormingule.



Kui olete valmis, salvestage fail ja käivitage Rsyslog uuesti.



```
sudo systemctl restart rsyslog.service
```



Pärast seda toimingut peaksid esimesed sõnumid jõudma teie Graylogi serverisse!



### IV. Linuxi logide kuvamine Graylogis



Graylogis saate klõpsata "**Streams**" ja valida oma uue voo, et vaadata sellega seotud sõnumeid. Teise võimalusena võite klõpsata "**Haigus**" ja valida oma Steami ning käivitada otsingu.



Järgnevalt on esitatud Interface mõned peamised omadused:



**1** - Valige ajavahemik, mille kohta teateid kuvatakse. Vaikimisi kuvatakse viimase 5 minuti sõnumid.



**2** - Valige kuvatav(ad) voog(id).



**3** - Lubage sõnumite loendi automaatne värskendamine (näiteks iga 5 sekundi järel). Vastasel juhul on see staatiline ja te peate seda käsitsi värskendama.



**4** - klõpsake suurendusklaasil, et käivitada otsing pärast perioodi, voo või filtri muutmist.



**5** - sisestusriba otsingufiltrite määramiseks. Siin annan "**source:srv\-docker**", et kuvada ainult selle uue masina logisid, millel ma just seadistasin Rsyslogi.



Logid saadab Linuxi masin:



![Image](assets/fr/015.webp)



### V. SSH-ühenduse tõrke tuvastamine



Graylogi tugevus seisneb tema võimekuses indekseerida logisid ja võimaldada otsinguid erinevate kriteeriumide alusel: lähtemasin, Timestamp, sõnumite sisu jne.... Me võiksime otsida ebaõnnestunud SSH-ühenduste tuvastamist.



Proovige kaugemast masinast (näiteks Graylogi serverist) luua ühendus oma Linuxi serveriga, millel te just konfigureerisite Rsyslogi. Näiteks:



```
ssh [email protected]
```



Seejärel sisestage tahtlikult vale **kasutajanimi** ja **salasõna**, et **generate ühendusvigu** tekitada. Failis "**/var/log/auth.log**" tekitab see generate logiteateid, mis sarnanevad järgmistele:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Need sõnumid peaksite leidma Graylogist.



Graylogis kasutage järgmist otsingufiltrit, et kuvada ainult sobivaid sõnumeid:



```
message:Failed password AND application_name:sshd
```



Kui teil on mitu serverit ja soovite analüüsida konkreetse serveri logisid, siis määrake lisaks selle nimi:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Siin on ülevaade tulemusest masinas, kus ma tekitasin mitu ühenduseviga erinevatel kellaaegadel:



![Image](assets/fr/009.webp)



Ebaõnnestunud ühenduskatsed tehakse masinast, mille IP Address on "**192.168.10.199**". Kui soovite selle host'i aktiivsuse kohta rohkem teada saada, saate **otsida seda IP Address**. Graylog väljastab kõik logid, kus sellele IP Address-le viidatakse, kõikidel hostidel (mille jaoks logide saatmine on konfigureeritud).



Sellisel juhul võib kasutatav filter olla:



```
message:"192.168.10.199"
```



Saame täiendavaid tulemusi (mis ei ole üllatav, sest me ei filtreeri SSH-rakendust):



![Image](assets/fr/008.webp)



### VI. Kokkuvõte



Seda õpetust järgides peaksite olema võimeline seadistama Linuxi masinat nii, et see saadaks oma logisid Graylogi serverisse. Nii saate oma Linuxi hostide logid tsentraliseerida oma logi valamusse!



Kui soovite veelgi kaugemale minna, kaaluge näidikute ja hoiatuste loomist, et saada teateid anomaalia tuvastamise korral.



![Image](assets/fr/007.webp)