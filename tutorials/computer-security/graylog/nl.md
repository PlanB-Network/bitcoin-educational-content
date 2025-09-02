---
name: Graylog
description: Centraliseer en analyseer je logs eenvoudig
---
![cover](assets/cover.webp)



___



*Deze zelfstudie is gebaseerd op originele inhoud van Florian BURNEL gepubliceerd op [IT-Connect](https://www.it-connect.fr/). Licentie [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Er kunnen wijzigingen zijn aangebracht in de oorspronkelijke tekst.*



___



## Graylog implementeren op Debian 12



### I. Presentatie



Graylog is een open source "log sink" oplossing ontworpen om logs van je machines en netwerkapparaten te centraliseren, op te slaan en in realtime te analyseren. In deze tutorial leren we hoe je de gratis versie van Graylog installeert op een Debian 12 machine!



Binnen een informatiesysteem genereert elke **server**, of die nu **Linux** of **Windows** draait, en elk **netwerkapparaat** (switch, router, firewall, etc...) **zijn eigen logs**, die lokaal worden opgeslagen. Met logs die lokaal op elke machine zijn opgeslagen, is eventanalyse en correlatie erg moeilijk... Dit is waar **Graylog** om de hoek komt kijken. Het zal fungeren als een **log sink**, wat betekent dat **alle machines hun logs** zullen sturen (via syslog, bijvoorbeeld). Graylog zal dan **deze logs opslaan en indexeren**, terwijl je globale zoekopdrachten kunt uitvoeren en waarschuwingen kunt aanmaken.



Graylog is een analyse- en monitoringtool die het makkelijker maakt om verdacht gedrag en verschillende problemen (stabiliteit, prestaties, enz.) te identificeren.




![Image](assets/fr/034.webp)



**Opmerking: de gratis versie, **Graylog Open**, is geen SIEM zoals Wazuh dat is, vooral omdat het echte inbraakdetectiefuncties mist.



### II. Vereisten



De **stack Graylog** is gebaseerd op **verschillende componenten** die we moeten installeren en configureren. Hier installeren we alle componenten op dezelfde server, maar het is mogelijk om clusters te maken op basis van meerdere nodes en de rollen te verdelen over meerdere servers. Voor deze tutorial installeren we **Graylog 6.1**, de meest recente versie tot nu toe.





- MongoDB 7**, de huidige aanbevolen versie voor Graylog (minimaal 5.0.7, maximaal 7.x)
- OpenSearch**, een open source Fork van Elasticsearch gemaakt door Amazon (minimaal 1.1.x, maximaal 2.15.x)
- OpenJDK 17**



De **Graylog server** draait op **Debian 12**, maar installatie is mogelijk op andere distributies, ook via Docker. De virtuele machine is uitgerust met **8 GB RAM** en **256 GB schijfruimte**, om genoeg bronnen te hebben voor alle componenten (anders kan dit een significante invloed hebben op de prestaties). Ik geef dit echter als een ruwe richtlijn, omdat **de grootte van de Graylog-architectuur afhangt van de hoeveelheid informatie die moet worden verwerkt**. Graylog kan 30 MB of 300 MB gegevens per dag verwerken, maar ook 300 GB gegevens per dag... Het is een **schaalbare oplossing** die **terabytes aan logs** kan verwerken (zie [deze pagina](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Bron: Graylog



Voordat u begint met de configuratie, moet u een statische IP Address toewijzen aan de Graylog-machine en de laatste updates installeren. Zorg ervoor dat u de tijdzone van de lokale machine instelt en een NTP-server definieert voor datum- en tijdsynchronisatie. Dit is het commando dat u moet uitvoeren:



```
sudo timedatectl set-timezone Europe/Paris
```



**Note: **OpenSearch installeren is optioneel** als je in plaats daarvan **Graylog Data Node** gebruikt.



### III Stapsgewijze installatie van Graylog



Laten we beginnen met het bijwerken van de pakketcache en het installeren van de gereedschappen die we nodig hebben voor wat komen gaat.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. MongoDB installeren



Als dat klaar is, beginnen we met de installatie van MongoDB. Download de GPG-sleutel die overeenkomt met de MongoDB-repository:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Voeg vervolgens de MongoDB 6 repository toe aan de Debian 12 machine:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Vervolgens werken we de pakketcache bij en proberen we MongoDB te installeren:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



MongoDB kan niet worden geïnstalleerd omdat een afhankelijkheid ontbreekt: **libssl1.1**. We moeten dit pakket handmatig installeren voordat we verder kunnen gaan, omdat Debian 12 het niet in de repositories heeft.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



We gaan het DEB-pakket genaamd "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (laatste versie) downloaden met de opdracht **wget** en vervolgens installeren met de opdracht **dpkg**. Dit levert de volgende twee commando's op:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Start de MongoDB-installatie opnieuw op:



```
sudo apt-get install -y mongodb-org
```



Start vervolgens de MongoDB-service opnieuw op en schakel deze in om automatisch te starten wanneer de Debian-server wordt gestart.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Nu MongoDB geïnstalleerd is, kunnen we verder gaan met de installatie van de volgende component.



#### B. OpenSearch installeren



Laten we verder gaan met het installeren van OpenSearch op de server. Het volgende commando voegt de signature key toe voor OpenSearch packages:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Voeg dan de OpenSearch-repository toe zodat we het pakket daarna kunnen downloaden met **apt**:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Werk je pakketcache bij:



```
sudo apt-get update
```



Installeer vervolgens OpenSearch** en zorg ervoor dat **het standaardwachtwoord voor het beheerdersaccount** van uw instantie is ingesteld. Hier is het wachtwoord "**IT-Connect2024!**", maar vervang deze waarde door een sterk wachtwoord. **Vermijd zwakke wachtwoorden** zoals "**P@ssword123**" en gebruik ten minste **8 tekens** met ten minste één teken van elk type (kleine letters, hoofdletters, cijfers en speciale tekens), anders verschijnt er een foutmelding aan het einde van de installatie. **Dit is een vereiste sinds OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Wees geduldig tijdens de installatie...



Als je klaar bent, neem dan even de tijd om de minimale configuratie uit te voeren. Open het configuratiebestand in YAML-formaat:



```
sudo nano /etc/opensearch/opensearch.yml
```



Stel de volgende opties in wanneer het bestand is geopend:



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



Deze OpenSearch configuratie is ontworpen om een enkele node in te stellen. Hier volgt wat uitleg over de verschillende parameters die we gebruiken:





- cluster.name: graylog**: Deze parameter benoemt het OpenSearch-cluster met de naam "**graylog**".
- node.name: ${HOSTNAME}**: de knooppuntnaam wordt dynamisch ingesteld om overeen te komen met die van de lokale Linux machine. Zelfs als we maar één knooppunt hebben, is het belangrijk om het de juiste naam te geven.
- path.data: /var/lib/opensearch**: dit pad specificeert waar OpenSearch zijn gegevens opslaat op de lokale machine, in dit geval in "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: dit pad definieert waar OpenSearch logbestanden worden opgeslagen, hier in "**/var/log/opensearch**".
- discovery.type: single-node**: deze parameter configureert OpenSearch om met een enkele node te werken, vandaar de keuze voor de optie "**single-node**".
- network.host: 127.0.0.1**: deze configuratie zorgt ervoor dat OpenSearch alleen luistert op zijn Interface local loop, wat voldoende is aangezien het op dezelfde server staat als Graylog.
- action.auto_create_index: false**: door het automatisch maken van indexen uit te schakelen, zal OpenSearch niet automatisch een index maken wanneer een document wordt verzonden zonder een bestaande index.
- plugins.security.disabled: true**: deze optie deactiveert de OpenSearch beveiligingsplugin, wat betekent dat er geen authenticatie, toegangsbeheer of communicatie-encryptie zal zijn. Deze instelling bespaart tijd bij het instellen van Graylog, maar moet vermeden worden in productie (zie [deze pagina](https://opensearch.org/docs/1.0/security-plugin/index/)).



Sommige opties zijn al aanwezig, dus je hoeft alleen maar de "#" te verwijderen om ze te activeren en vervolgens je waarde aan te geven. Als je een optie niet kunt vinden, kun je deze direct aan het einde van het bestand declareren.



![Image](assets/fr/023.webp)



Sla dit bestand op en sluit het.



#### C. Java (JVM) configureren



Je moet de Java Virtual Machine die door OpenSearch wordt gebruikt configureren om de hoeveelheid geheugen die deze service kan gebruiken aan te passen. Bewerk het volgende configuratiebestand:



```
sudo nano /etc/opensearch/jvm.options
```



Met de hier gebruikte configuratie zal **OpenSearch starten met 4 GB toegewezen geheugen en kan groeien tot 4 GB**, dus er zal geen geheugenvariatie zijn tijdens het gebruik. Hier houdt de configuratie rekening met het feit dat de virtuele machine in totaal **8 GB RAM** heeft. Beide parameters moeten dezelfde waarde hebben. Dit betekent dat de regels:



```
-Xms1g
-Xmx1g
```



Met deze regels:



```
-Xms4g
-Xmx4g
```



Hier is een afbeelding van de modificatie die moet worden aangebracht:



![Image](assets/fr/022.webp)



Sluit dit bestand nadat je het hebt opgeslagen.



Daarnaast moeten we de configuratie van de "**max_map_count**" parameter in de Linux kernel controleren. Deze bepaalt de limiet van het aantal geheugengebieden dat per proces in kaart wordt gebracht, om aan de behoeften van onze applicatie te voldoen. **OpenSearch**, net als Elasticsearch**, raadt aan om deze waarde in te stellen op "262144" om fouten in het geheugenbeheer te voorkomen.



In principe is de waarde op een vers geïnstalleerde Debian 12 machine al correct. Maar laten we het controleren. Voer dit commando uit:



```
cat /proc/sys/vm/max_map_count
```



Als je een andere waarde krijgt dan "**262144**", voer dan het volgende commando uit, anders is het niet nodig.



```
sudo sysctl -w vm.max_map_count=262144
```



Schakel ten slotte OpenSearch autostart in en start de bijbehorende service.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Als je de systeemstatus weergeeft, zou je een Java-proces met 4 GB RAM moeten zien.



```
top
```



![Image](assets/fr/029.webp)



Volgende stap: de langverwachte installatie van Graylog!



#### D. Graylog installeren



Om **Graylog 6.1** in de laatste versie te installeren, voert u de volgende 4 opdrachten uit om **Graylog Server** te downloaden en te installeren**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Als dit gedaan is, moeten we enkele wijzigingen aanbrengen in de configuratie van Graylog voordat we het proberen te starten.



Laten we beginnen met het configureren van deze twee opties:





- password_secret**: deze parameter wordt gebruikt om een sleutel te definiëren die door Graylog wordt gebruikt om de opslag van gebruikerswachtwoorden te beveiligen (in de geest van een salting-sleutel). Deze sleutel moet **uniek** en **willekeurig** zijn.
- root_password_sha2**: Deze parameter komt overeen met het standaard beheerderswachtwoord in Graylog. Het wordt opgeslagen als een Hash SHA-256.



We beginnen met het genereren van een sleutel van 96 tekens voor de **password_secret** parameter:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Kopieer de geretourneerde waarde en open dan het Graylog configuratiebestand:



```
sudo nano /etc/graylog/server/server.conf
```



Plak de sleutel in de **password_secret** parameter, zoals dit:



![Image](assets/fr/027.webp)



Sla het bestand op en sluit het.



Vervolgens moet je het wachtwoord instellen voor het "**admin**" account dat standaard is aangemaakt. In het configuratiebestand moet de Hash van het wachtwoord worden opgeslagen, wat betekent dat het moet worden berekend. Het onderstaande voorbeeld geeft de Hash van het wachtwoord "**LogsWells@**": pas de waarde aan aan je eigen wachtwoord.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Kopieer de verkregen waarde als uitvoer (zonder het streepje aan het einde van de regel).



Open het Graylog configuratiebestand opnieuw:



```
sudo nano /etc/graylog/server/server.conf
```



Plak de waarde in de **root_password_sha2** optie als volgt:



![Image](assets/fr/026.webp)



Stel in het configuratiebestand de optie "**http_bind_address**" in. Geef "**0.0.0.0:9000**" op, zodat Graylog's Interface web kan worden benaderd op poort **9000**, via elke server IP Address.



![Image](assets/fr/024.webp)



Stel dan de "**elasticsearch_hosts**" optie in op `http://127.0.0.1:9200` om onze lokale OpenSearch instantie aan te geven. Dit is nodig omdat we geen **Graylog Data Node** gebruiken. En zonder deze optie is het niet mogelijk om verder te gaan...



![Image](assets/fr/025.webp)



Sla het bestand op en sluit het.



Dit commando activeert Graylog zodat het automatisch start bij de volgende boot, en start onmiddellijk de Graylog server.



```
sudo systemctl enable --now graylog-server
```



Als dit gedaan is, probeer dan verbinding te maken met Graylog vanuit een browser. Voer het IP Address (of de naam) en poort 9000 van de server in.



**Ter informatie:**



Nog niet zo lang geleden verscheen er een verificatievenster zoals hieronder wanneer je voor het eerst inlogde op Graylog. Je moest je login "**admin**" en je wachtwoord invoeren. En dan werd je onaangenaam verrast door het feit dat de verbinding niet werkte.



![Image](assets/fr/031.webp)



Het was nodig om terug te gaan naar de opdrachtregel op de Graylog server en de logs te raadplegen. We konden toen zien dat **voor de eerste verbinding**, het nodig is om **een tijdelijk wachtwoord** te gebruiken, gespecificeerd in de logs.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Vervolgens moest je opnieuw proberen verbinding te maken met de gebruiker "**admin**" en het tijdelijke wachtwoord, en hiermee kon je inloggen!



**Dit is niet langer het geval. Je hoeft alleen maar in te loggen met je beheerdersaccount en het wachtwoord dat is ingesteld op de opdrachtregel



![Image](assets/fr/033.webp)



**Welkom op Graylog's Interface!



![Image](assets/fr/019.webp)



#### E. Graylog: een nieuwe beheerdersaccount aanmaken



In plaats van de door Graylog aangemaakte beheerdersaccount te gebruiken, kunt u uw eigen persoonlijke beheerdersaccount aanmaken. Klik op het menu "**Systeem**" en vervolgens op "**Gebruikers en teams**" om op de knop "**Gebruiker aanmaken**" te klikken. Vul vervolgens het formulier in en wijs de beheerdersrol toe aan uw account.



![Image](assets/fr/020.webp)



Een gepersonaliseerde account kan extra informatie bevatten, zoals voor- en achternaam en e-mail Address, in tegenstelling tot een native admin account. Bovendien zorgt dit voor een betere traceerbaarheid wanneer elke persoon met een account op naam werkt.



## Logboeken naar Graylog sturen met rsyslog



### I. Presentatie



In dit tweede deel leren we hoe we een Linux machine kunnen configureren om zijn logs naar een Graylog server te sturen. Hiervoor installeren en configureren we Rsyslog op het systeem.



### II. Graylog configureren om Linux logs te ontvangen



We beginnen met het configureren van Graylog. Er zijn drie stappen om te voltooien:





- Het maken van een **Invoer** om een ingang te maken waarmee Linux machines **Syslog logs kunnen versturen via UDP**.
- Het aanmaken van een nieuwe **Index** voor het opslaan en **indexeren van alle Linux logs**.
- Aanmaken van een **Stream** om **de door Graylog ontvangen logs door te sturen** naar de nieuwe Linux Index.



#### A. Een invoer voor Syslog aanmaken



Log in op Graylog Interface, klik op "**System**" in het menu en dan op "**Inputs**". Selecteer in de vervolgkeuzelijst "**Syslog UDP**" en klik vervolgens op de knop "**Nieuwe invoer starten**". Het is ook mogelijk om een TCP Syslog Input aan te maken, maar hiervoor is het gebruik van een TLS-certificaat nodig: een pluspunt voor de veiligheid, maar niet behandeld in dit artikel.



![Image](assets/fr/001.webp)



Er verschijnt een wizard op het scherm. Begin met deze Input een naam te geven, bijvoorbeeld "**Graylog_UDP_Rsyslog_Linux**" en kies een poort. Standaard is de poort "**514**", maar je kunt deze aanpassen. Hier is poort "**12514**" geselecteerd.



![Image](assets/fr/016.webp)



Je kunt ook de optie "**Volledig bericht opslaan**" aanvinken om het volledige logbericht in Graylog op te slaan. Klik op "**Invoer starten**".



![Image](assets/fr/017.webp)



De nieuwe ingang is aangemaakt en is nu actief. Graylog kan nu Syslog logs ontvangen op poort 12514/UDP, maar we zijn nog niet klaar met het configureren van de applicatie.



![Image](assets/fr/018.webp)


**Notitie: een enkele Input kan gebruikt worden om logs van meerdere Linux machines op te slaan.



#### B. Een nieuwe Linux-index maken



We moeten een index aanmaken in Graylog om logs van Linux-machines op te slaan. Een **index** in Graylog is een opslagstructuur die de ontvangen logs bevat, d.w.z. de ontvangen berichten. Graylog gebruikt OpenSearch als opslagmotor en berichten worden geïndexeerd om snel en efficiënt zoeken mogelijk te maken.



Klik in Graylog op "**Systeem**" in het menu en vervolgens op "**Indices**". Op de nieuwe pagina die verschijnt, klik je op "**Create index set**".



![Image](assets/fr/005.webp)



Geef deze index een naam, bijvoorbeeld "**Linux Index**", voeg een beschrijving en een voorvoegsel toe voordat je bevestigt. Hier zullen we **alle Linux logs opslaan in deze index**. Het is ook mogelijk om specifieke indexen aan te maken om alleen bepaalde logs op te slaan (alleen [SSH] logs (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), Web service logs, enz.)



![Image](assets/fr/006.webp)



Nu moeten we een nieuwe stream maken om berichten naar deze index te routeren.



#### C. Een stream maken



Om een nieuwe stream aan te maken, klik je op "**Streams**" in het hoofdmenu van Graylog. Klik dan rechts op de knop "**Stream aanmaken**". In het venster dat verschijnt, geef je de stream een naam, bijvoorbeeld "**Linux Stream**" en kies je de index "**Linux Index**" voor het veld "**Index Set**". Bevestig je keuze.



**Opmerking: berichten die overeenkomen met deze stroom worden ook opgenomen in de "**Standaardstroom**", tenzij je de optie "**Verwijder matches uit 'Standaardstroom'**" aanvinkt.



![Image](assets/fr/002.webp)



Klik dan in je stoominstellingen op de knop "**Regel voor stream toevoegen**" om een nieuwe regel voor het routeren van berichten toe te voegen. Als je dit venster niet kunt vinden, klik dan op "**Streams**" in het menu, klik dan op de regel die overeenkomt met je stream op "**Meer**" en vervolgens op "**Regels beheren**".



Kies het type "**match input**" en selecteer de eerder aangemaakte **Rsyslog-invoer in UDP**. Bevestig met de knop "**Create Rule**". Alle berichten naar onze nieuwe ingang worden nu naar de Index voor Linux gestuurd.



![Image](assets/fr/003.webp)



Uw nieuwe Stream zou in de lijst moeten verschijnen en het zou in de status "**Running**" moeten staan. De bandbreedte van het bericht toont "**0 msg/s**", omdat we op dit moment geen logs naar de Rsyslog UDP ingang sturen. Om de logs van een stream te bekijken, klik je gewoon op de naam.



![Image](assets/fr/004.webp)



**Alles is klaar aan de Graylog kant**. De volgende stap is het configureren van de Linux machine.



### III. Rsyslog installeren en configureren op Linux



Log in op de Linux machine, lokaal of op afstand, en gebruik een gebruikersaccount met rechten om de rechten te verhogen (via sudo). Gebruik anders direct de "root" account.



#### A. Het pakket Rsyslog installeren



Begin met het bijwerken van de pakketcache en installeer het pakket met de naam "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Controleer dan de status van de service. In de meeste gevallen is deze al actief.



```
sudo systemctl status rsyslog
```



#### B. Rsyslog configureren



Rsyslog heeft hier een hoofdconfiguratiebestand:



```
/etc/rsyslog.conf
```



Daarnaast wordt de map "**/etc/rsyslog.d/**" gebruikt om aanvullende configuratiebestanden voor RSyslog op te slaan. In het hoofdconfiguratiebestand staat een Include-richtlijn om alle "**.conf**"-bestanden in deze map te importeren. Dit maakt het mogelijk om extra bestanden te hebben voor het configureren van Rsyslog zonder het hoofdbestand aan te passen.



In deze map moet je nummers gebruiken om de laadvolgorde te definiëren, omdat bestanden in alfabetische volgorde worden geladen. Door een numeriek voorvoegsel toe te voegen kun je de prioriteit tussen verschillende configuratiebestanden beheren. Hier hebben we maar één extra bestand, dus dat is geen probleem.



In deze map maken we een bestand aan met de naam "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



Voeg in dit bestand deze regel in:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Dit is hoe je deze regel moet interpreteren:





- `*.*`: betekent dat alle Syslog-logs van de Linux-machine naar Graylog worden gestuurd.
- `@`: geeft aan dat het transport in UDP wordt uitgevoerd. Je moet "**@@**" opgeven om over te schakelen naar TCP.
- `192.168.10.220:12514`: geeft de Address van de Graylog-server aan en de poort waarop de logs worden verzonden (komt overeen met de Invoer).
- `RSYSLOG_SyslogProtocol23Format`: komt overeen met het formaat van de berichten die naar Graylog worden verzonden.



Als je klaar bent, sla je het bestand op en herstart je Rsyslog.



```
sudo systemctl restart rsyslog.service
```



Na deze actie zouden de eerste berichten op je Graylog server moeten aankomen!



### IV. Linux logs weergeven in Graylog



Vanuit Graylog kun je klikken op "**Streams**" en je nieuwe stream selecteren om gerelateerde berichten te bekijken. Je kunt ook klikken op "**Zoeken**" en je Steam selecteren om een zoekopdracht te starten.



Hier zijn enkele belangrijke kenmerken van de Interface:



**1** - Selecteer de periode waarvoor berichten moeten worden weergegeven. Standaard worden berichten van de laatste 5 minuten weergegeven.



**2** - Selecteer de stream(s) die moet(en) worden weergegeven.



**3** - Automatisch vernieuwen van de berichtenlijst inschakelen (bijvoorbeeld elke 5 seconden). Anders is het statisch en moet je het handmatig verversen.



**4** - Klik op het vergrootglas om de zoekopdracht te starten na het wijzigen van de periode, stream of filter.



**5** - Invoerbalk om je zoekfilters op te geven. Hier geef ik "**source:srv-docker**" op om alleen de logs weer te geven van de nieuwe machine waarop ik zojuist Rsyslog heb ingesteld.



Logs worden verzonden door de Linux machine:



![Image](assets/fr/015.webp)



### V. Een SSH-verbindingsfout identificeren



De kracht van Graylog ligt in de mogelijkheid om logs te indexeren en zoekopdrachten uit te voeren op basis van verschillende criteria: bronmachine, Timestamp, berichtinhoud, enzovoort. We zouden kunnen zoeken naar mislukte SSH-verbindingen.



Probeer vanaf een machine op afstand (bijvoorbeeld de Graylog server) verbinding te maken met je Linux server waarop je zojuist Rsyslog hebt geconfigureerd. Bijvoorbeeld:



```
ssh [email protected]
```



Voer dan opzettelijk een onjuiste **gebruikersnaam** en **wachtwoord** in, om **generate verbindingsfouten** te veroorzaken. In het "**/var/log/auth.log**" bestand, zal dit generate logboek boodschappen geven zoals de volgende:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Je zou deze berichten op Graylog moeten vinden.



Gebruik in Graylog het volgende zoekfilter om alleen overeenkomende berichten weer te geven:



```
message:Failed password AND application_name:sshd
```



Als je meerdere servers hebt en de logboeken van een specifieke server wilt analyseren, geef dan de naam van die server op als aanvulling:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Hier is een overzicht van het resultaat op een machine waar ik verschillende verbindingsfouten heb gegenereerd, op verschillende tijden van de dag:



![Image](assets/fr/009.webp)



Niet succesvolle verbindingspogingen worden gemaakt vanaf de machine met IP Address "**192.168.10.199**". Als je meer wilt weten over de activiteit van deze host, kun je **zoeken naar dit IP Address**. Graylog zal alle logs uitvoeren waar naar dit IP Address wordt verwezen, op alle hosts (waarvoor het versturen van logs is geconfigureerd).



In dit geval kan het te gebruiken filter:



```
message:"192.168.10.199"
```



We krijgen aanvullende resultaten (niet verrassend, omdat we niet filteren op de SSH-toepassing):



![Image](assets/fr/008.webp)



### VI. Conclusie



Door deze tutorial te volgen, zou je een Linux machine moeten kunnen configureren om zijn logs naar een Graylog server te sturen. Op deze manier kun je de logs van je Linux hosts centraliseren in je log sink!



Om nog verder te gaan, kun je overwegen dashboards en waarschuwingen te maken om een melding te ontvangen wanneer er een afwijking wordt gedetecteerd.



![Image](assets/fr/007.webp)