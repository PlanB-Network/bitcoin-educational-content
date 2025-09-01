---
name: Lynis
description: Een beveiligingsaudit van een Linux-machine uitvoeren met Lynis
---
![cover](assets/cover.webp)



___



*Deze zelfstudie is gebaseerd op originele inhoud van Fares CHELLOUG gepubliceerd op [IT-Connect](https://www.it-connect.fr/). Licentie [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Er kunnen wijzigingen zijn aangebracht in de oorspronkelijke tekst.*



___



## I. Presentatie



**In deze tutorial leren we hoe we een beveiligingsaudit kunnen uitvoeren op een Linux machine met behulp van Lynis! Voor degenen die **Lynis,** niet kennen, het is een klein commandoregel hulpprogramma dat de configuratie van je server analyseert en aanbevelingen doet om **de beveiliging van je machine te verbeteren.**



Lynis is een open source tool van CISOFY, een bedrijf gespecialiseerd in **systeem auditing en hardening**. Als je vooruitgang wilt boeken in het hardenen van Linux en populaire services (SSH, Apache2, etc.), dan is Lynis je bondgenoot! Lynis vertelt je niet alleen wat er fout gaat, maar geeft ook aanbevelingen om je in de juiste richting te sturen (en tijd te besparen).



**Lynis** werkt met de meeste Linux distributies, inclusief: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis is gericht op Linux / UNIX gebruikers, maar is ook **macOS** compatibel. Zeer snel te installeren, er is geen afhankelijkheidsbeheer op pakketniveau.



Het wordt voor verschillende doeleinden gebruikt:





- Veiligheidsaudits
- Compliance testen (PCI, HIPAA en SOX)
- Robuustere systeemconfiguraties
- Kwetsbaarheidsdetectie



De tool wordt veel gebruikt door een breed scala aan gebruikers, waaronder systeembeheerders, IT-auditors en pentesters. Voor analyses is de tool gebaseerd op standaarden zoals **CIS Benchmark, NIST, NSA, OpenSCAP** en op officiële aanbevelingen van **Debian, Gentoo, Red Hat**.



Het project is beschikbaar op deze Address op **Github**:





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Lynis downloaden van CISOFY](https://cisofy.com/lynis/#download)



In deze stap-voor-stap tutorial ga ik **een VPS gebruiken die Debian 12** draait en ik ga me concentreren op het SSH gedeelte, omdat ik de configuratie ervan wil controleren en verbeteren.



## II. Downloaden en installeren



Er zijn verschillende manieren om Lynis te downloaden en te installeren. Kies uit de onderstaande lijst de manier die jouw voorkeur heeft.



### A. Installatie vanuit Debian-repositories



Met deze installatiemodus kunt u het **lynis** commando overal op het systeem gebruiken, in tegenstelling tot installatie vanaf de broncode, waar u zich in de directory moet bevinden.



Maak verbinding met je server via SSH en voer de volgende commando's in om Lynis te installeren:



```
sudo apt-get update
sudo apt-get install lynis -y
```



Dit is wat je krijgt:



![Image](assets/fr/024.webp)



### B. Downloaden van de officiële website



Je kunt het ook downloaden van de Cisofy website:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Dit is wat je krijgt:



![Image](assets/fr/032.webp)



Vervolgens pakken we het archief uit met het volgende commando:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Dit is wat je krijgt:



![Image](assets/fr/020.webp)



Laten we naar de **lynis** map gaan:



```
cd lynis
```



We kunnen controleren op updates met het volgende commando:



```
./lynis update info
```



Dit is wat je krijgt:



![Image](assets/fr/023.webp)



### C. Downloaden van GitHub



We downloaden **Lynis** van de officiële GitHub repository met het volgende commando (*git* moet aanwezig zijn op je machine):



```
git clone https://github.com/CISOfy/lynis.git
```



Dit is wat je krijgt:



![Image](assets/fr/060.webp)



## III. Lynis gebruiken



Lynis is aanwezig op onze machine, dus laten we leren hoe we het kunnen gebruiken!



### A. Belangrijkste bedieningselementen en opties



Voer het volgende commando in om de beschikbare commando's weer te geven:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe:
./lynis
```



Dit is wat je krijgt:



![Image](assets/fr/039.webp)



En je krijgt ook de volgende opties:



![Image](assets/fr/040.webp)



Voer het volgende commando in om alle beschikbare commando's weer te geven:



```
sudo lynis show
```



Dit is wat je krijgt:



![Image](assets/fr/022.webp)



Als u alle opties wilt weergeven, moet u invoeren:



```
sudo lynis show options
```



Dit is wat je krijgt:



![Image](assets/fr/021.webp)



In de rest van dit artikel leren we hoe we bepaalde opties kunnen gebruiken.



### B. De systeemaudit uitvoeren



We gaan **Lynis** vragen om ons systeem door te lichten, om aan te geven wat correct geconfigureerd is en wat verbeterd kan worden. Voer hiervoor het volgende commando in:



```
sudo lynis audit system
# ou
./lynis audit system
```



Als je niet als root bent ingelogd wanneer je dit commando uitvoert, draait het gereedschap standaard met de rechten van de gebruiker die op dat moment is ingelogd. Sommige testen worden in deze context niet uitgevoerd:



![Image](assets/fr/052.webp)



Hier zijn de tests die in deze modus niet worden uitgevoerd:



![Image](assets/fr/051.webp)



Zodra het commando is uitgevoerd, begint de analyse. Wacht gewoon even.



Aan het einde van de audit krijg je dit (we kunnen zien dat **Lynis** het **Debian 12** systeem correct heeft geïdentificeerd en de **Debian plugin** zal gebruiken voor de analyse):



![Image](assets/fr/017.webp)



Vervolgens geeft Lynis een lijst met punten die overeenkomen met alles wat hij in ons systeem heeft gecontroleerd. Dit is georganiseerd per categorie, zoals we zullen zien. Het is ook de moeite waard om op te merken dat er een kleurcode wordt gebruikt om aanbevelingen te markeren:





- Rood** voor kritieke Elements of best practices die niet worden gerespecteerd (bijvoorbeeld een ontbrekend pakket), d.w.z. uw server respecteert dit punt niet
- Geel** voor suggesties of gedeeltelijke naleving van de aanbeveling (laten we zeggen dat het een plus is om te voldoen aan een punt dat met deze kleur is gemarkeerd (niet-prioriteit))
- Green** voor punten waar uw serverconfiguratie aan voldoet
- Wit**, indien neutraal



Hier zien we dat Lynis aanbeveelt om **fail2ban** te installeren:



![Image](assets/fr/057.webp)



In de sectie "**Boot en services**" zien we dat de servicebescherming via *systemd* verbeterd zou kunnen worden. Aan de positieve kant, Grub2 is aanwezig en er zijn geen problemen met permissies op:



![Image](assets/fr/029.webp)



Dan heb je de secties "**Kernel**" en "**Memory en Processen**":



![Image](assets/fr/037.webp)



Vervolgens de sectie "**Users, Groepen en Authenticatie**". De tool informeert ons over een waarschuwing met betrekking tot de permissies van de map "**/etc/sudoers.d**". Op dit moment weten we niet meer, maar we zullen aan het einde van de analyse kunnen zien wat de aanbeveling is.



![Image](assets/fr/049.webp)



Dit is wat je kunt vinden in de secties "**Shells", "Bestandssystemen" en "USB-apparaten"**. We kunnen onder andere zien dat er suggesties zijn voor koppelpunten en dat USB-apparaten momenteel zijn toegestaan op deze machine.



![Image](assets/fr/048.webp)



Vervolgens de secties: "**Naam services", "Poorten en pakketten", "Netwerken".** Hier wordt aangegeven dat pakketten die niet langer in gebruik zijn kunnen worden verwijderd en dat er geen hulpprogramma is dat automatische updates kan beheren.



![Image](assets/fr/058.webp)



We kunnen zien dat er een firewall geactiveerd is (en ja, er is iptables!). Daarnaast kunnen we zien dat er ongebruikte regels zijn gevonden en dat er een Apache webserver is geïnstalleerd.



![Image](assets/fr/055.webp)



Dit wordt gevolgd door een analyse van de webserver zelf, aangezien de dienst is geïdentificeerd.



We kunnen zien dat het **Nginx** configuratiebestanden heeft gevonden en dat voor het SSL/TLS gedeelte de **ciphers** zijn geconfigureerd met het gebruik van een protocol dat onveilig zou zijn. Aan de andere kant is volgens Lynis het logbeheer correct.



![Image](assets/fr/038.webp)



De SSH-service is aanwezig op mijn VPS-server. De configuratie wordt geanalyseerd door Lynis. Het moet gezegd worden dat de beveiliging van SSH gemakkelijk verbeterd kan worden! We zullen hier in detail op terugkomen zodra we de aanbevelingen hebben verkregen.



![Image](assets/fr/026.webp)



Hier zijn de secties **"SNMP-ondersteuning", "Databases", "PHP", "Squid-ondersteuning", "LDAP-services", "Loggen en bestanden"**.



Er is één heel belangrijke suggestie over logbeheer: het wordt sterk aangeraden om logs niet alleen lokaal op je machine op te slaan. Als de machine corrupt zou zijn door een aanvaller, is het waarschijnlijk dat hij zijn sporen zou proberen te wissen... Dus we moeten de logs externaliseren.



![Image](assets/fr/050.webp)



Hier hebben we de audit van kwetsbare services, accountbeheer, geplande taken en NTP-synchronisatie.Er wordt aangegeven dat het niveau laag is op het banner- en identificatiegedeelte: dit is begrijpelijk, als je de systeemversie weergeeft, geeft dit een indicatie aan een potentiële aanvaller. Dit is de standaardinstelling.



Het zou interessant zijn om **auditd** te activeren om logs te hebben in het geval van **forensische** analyse. De **NTP** wordt ook gecontroleerd, want om logs efficiënt te doorzoeken, is het beter om systemen op tijd te hebben, wat het zoeken vereenvoudigt.



![Image](assets/fr/036.webp)



Lynis kijkt vervolgens naar cryptografische Elements, virtualisatie, containers en beveiligingsframeworks. Sommige secties zijn leeg omdat er geen overeenkomst is met de geanalyseerde machine. We kunnen echter zien dat ik twee verlopen SSL-certificaten heb en dat ik **SELinux** niet heb geactiveerd.



![Image](assets/fr/027.webp)



Ook hier is ruimte voor verbetering: er is geen antivirus- of antimalwarescanner en we hebben suggesties voor bestandsrechten.



![Image](assets/fr/028.webp)



Vervolgens richt Lynis zich op het aanscherpen van de Linux kernel configuratie (inclusief regels voor de IPv4 stack) en het beheer van de "Home" mappen van de Linux machine.



![Image](assets/fr/035.webp)



We zijn aan het einde van de analyse gekomen... Dit laatste punt laat zien dat we er alle baat bij hebben om ClamAV op deze machine te hebben.



![Image](assets/fr/030.webp)



## IV. Aanbevelingen



Na de audit is het tijd om de aanbevelingen te lezen en te analyseren. Hier krijgen we de aanbevelingen en uitleg voor elk van de tests die Lynis heeft uitgevoerd.



Neem bijvoorbeeld de SSH-aanbevelingen. **Voor elke suggestie vind je de aanbevolen parameter en een link die het beveiligingspunt uitlegt ** Het is aan jou om te beslissen, afhankelijk van je context en gebruik.



Laten we eens kijken naar een paar voorbeelden van aanbevelingen die een directe echo zijn van de punten die tijdens de controle naar voren kwamen...



### A. Voorbeelden van aanbevelingen





- Zoals we eerder zagen, is NTP belangrijk voor het tijdstempelen van logs:



![Image](assets/fr/043.webp)





- Lynis stelt ook voor om het pakket **apt-listbugs** te installeren om informatie te krijgen over kritieke bugs tijdens de installatie van pakketten via **apt.**



![Image](assets/fr/041.webp)





- De tool stelt voor dat we **needrestart installeren om** te kunnen zien welke processen een oude versie van de bibliotheek gebruiken en opnieuw opgestart moeten worden.



![Image](assets/fr/054.webp)





- Deze suggestie stelt voor om **fail2ban** te installeren om automatisch hosts te blokkeren die er niet in slagen zich te authenticeren (met name brute kracht).



![Image](assets/fr/044.webp)





- Om de systeemservices te harden, raadt hij aan om het blauwe commando uit te voeren voor elke service op onze machine.



![Image](assets/fr/056.webp)





- Hij stelt voor om vervaldatums in te stellen voor alle beveiligde accountwachtwoorden.



![Image](assets/fr/031.webp)





- Deze suggestie stelt voor om minimum- en maximumwaarden in te stellen voor de leeftijd van een wachtwoord. Dit zorgt er onder andere voor dat wachtwoorden regelmatig worden veranderd.



![Image](assets/fr/042.webp)





- We raden aan om aparte partities te gebruiken om de impact van schijfruimteproblemen op één partitie te beperken.



![Image](assets/fr/047.webp)





- Deze aanbeveling stelt voor om USB-opslag en firewire uit te schakelen om het lekken van gegevens te voorkomen



![Image](assets/fr/033.webp)





- Om aan deze aanbeveling te voldoen, installeer en configureer je bijvoorbeeld **unnatended-upgrade**.



![Image](assets/fr/053.webp)



### B. Aanbevolen pakketten installeren



Om de systeemconfiguratie te verbeteren, gaan we enkele pakketten op de machine installeren: enkele aanbevolen door Lynis, enkele die ik persoonlijk aanbeveel.



Je hebt een goede basis om mee te werken, zolang je maar wat tijd besteedt aan het configureren ervan. Raadpleeg hiervoor de IT-Connect site, andere artikelen op het web en de documentatie van de tools.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Informatie over de geïnstalleerde pakketten:





- Clamav** is een antivirus.
- unattend-upgrades** stelt je in staat om je updates automatisch te beheren en zelfs de machine opnieuw op te starten of oude pakketten automatisch te verwijderen, het is volledig configureerbaar.
- rkhunter** is een anti-rootkit die je bestandssysteem scant.
- Fail2ban** baseert zich op je logbestanden volgens wat je het geeft om te lezen en het werkt met **iptables**, bijvoorbeeld om IP-adressen te bannen die je server proberen te "brute-forcen" in SSH.



### C. Aanbevelingen voor SSH



Laten we eens kijken naar de SSH-aanbevelingen. Ze staan hieronder. Maak je geen zorgen, we zullen meteen uitleggen hoe je de configuratie kunt verbeteren.



![Image](assets/fr/034.webp)



Laten we eens kijken naar mijn huidige **SSH** configuratie in:**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



De hieronder voorgestelde configuratie kan nog worden geoptimaliseerd, maar geeft je een goede basis. *Merk op dat ik een aantal opmerkingen heb verwijderd voor een betere leesbaarheid*.



We zullen:





- Wijzig de SSH-verbindingspoort (vergeet de standaard 22)
- Verhoog het verbositeitsniveau van logs, van **INFO naar VERBOSE**
- Stel **LoginGraceTime** in op **2 minuten**



Als er binnen twee minuten geen verbindingsinformatie wordt ingevoerd, wordt de verbinding verbroken.





- Activeer **strictModes**



Geeft aan of "sshd" de modi en de eigenaar van de bestanden van de gebruiker en de thuismap van de gebruiker moet controleren voordat een verbinding wordt gevalideerd. Dit is normaal gesproken wenselijk, omdat nieuwelingen soms per ongeluk hun map of bestanden volledig toegankelijk laten voor iedereen. De standaardinstelling is "yes".





- Stel **MaxAutries** in op 3



Dit is het aantal mislukte authenticatiepogingen voordat de communicatie wordt afgesloten.





- Stel **MaxSessions** in op 2



Dit is het maximum aantal gelijktijdige sessies.





- Authenticatie met openbare sleutel inschakelen



```
PubkeyAuthentication yes
```





- Wachtwoordverificatie behouden:



```
PasswordAuthentication yes
```



Verbied lege wachtwoorden en **Kerberos** authenticatie, evenals **directe root authenticatie**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Zorg ervoor dat je "**PermitRootLogin no" hebt, als het gelijk is aan "yes", is het "absolute evil"**.





- TCP-verbindingsomleiding verbieden



```
AllowTcpForwarding no
```



Geeft aan of TCP-omleidingen zijn toegestaan, met "yes" als standaardinstelling. Let op: het uitschakelen van TCP redirects verhoogt de veiligheid niet als gebruikers toegang hebben tot een commandoregel, omdat ze nog steeds hun eigen omleidingshulpmiddelen kunnen instellen.





- X11-omleiding verbieden



```
X11Forwarding no
```



Geeft aan of X11-omleidingen worden geaccepteerd, met "no" als standaardinstelling. Let op: zelfs als X11-omleidingen zijn uitgeschakeld, verhoogt dit de veiligheid niet, omdat gebruikers nog steeds hun eigen omleidingen kunnen instellen. X11-omleidingen worden automatisch uitgeschakeld als **UseLogin** is geselecteerd.





- De time-out voor communicatie tussen de client en sshd instellen



```
ClientAliveInterval  300
```



Definieert een time-out in seconden waarna, als er geen gegevens worden ontvangen van de client, de sshd service een bericht stuurt met het verzoek om een antwoord van de client. Standaard is deze optie ingesteld op "0", wat betekent dat deze berichten niet naar de client worden gestuurd. Alleen versie 2 van het SSH-protocol ondersteunt deze optie.



```
ClientAliveCountMax 0
```



Volgens de [documentatie (*manpagina*) voor sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html), is dit wat deze optie betekent: "Stelt het aantal hold-berichten (zie hierboven) in dat moet worden verzonden zonder antwoord van de client voor **sshd**. Als deze drempel wordt bereikt terwijl de hold-berichten zijn verzonden, verbreekt **sshd** de verbinding met de client en wordt de sessie beëindigd. Het is belangrijk op te merken dat deze hold-berichten sterk verschillen van de **KeepAlive** optie (hieronder). Verbindingswachtberichten worden door de versleutelde tunnel gestuurd en zijn daarom niet te vervalsen. TCP-level connection hold ingeschakeld door **KeepAlive** is vervalsbaar. Het verbindingsstopmechanisme is van belang als de client of server moet weten of de verbinding inactief is."





- Voorkom openbaarmaking van informatie door **motd, banner, lastlog** uit te schakelen



```
PrintMotd no
```



Geeft aan of sshd de inhoud van het bestand "/etc/motd" moet weergeven als een gebruiker zich aanmeldt in interactieve modus. Op sommige systemen kan deze inhoud ook door de shell worden weergegeven, via /etc/profile of een soortgelijk bestand. De standaardwaarde is "yes".



```
Banner none
```



Het is de moeite waard om op te merken dat in sommige rechtsgebieden het verzenden van een bericht voorafgaand aan de authenticatie een voorwaarde kan zijn voor wettelijke bescherming. De inhoud van het gespecificeerde bestand wordt naar de gebruiker op afstand gestuurd voordat er verbindingstoestemming wordt gegeven. Deze optie moet geconfigureerd worden, omdat er standaard geen bericht wordt weergegeven.



In afbeeldingen geeft dit:



![Image](assets/fr/019.webp)



### D. Auditscore



Laten we tot slot niet vergeten om de **Lynis audit score** te controleren! We zien dat **mijn Hardening score 63** is en dat het rapportbestand kan worden bekeken in "**/var/log/lynis-report.dat**". Er is ook het bestand "**/var/log/lynis.log**".



**Met andere woorden, hoe hoger de score, hoe beter! Daarom moet je aan je configuratie werken om de hoogst mogelijke score te behalen, terwijl je machine en gehoste services normaal kunnen functioneren (wat betekent dat je functionele tests moet uitvoeren).



![Image](assets/fr/046.webp)



Laten we eens kijken naar de resultaten op mijn tweede server, waar ik iets meer tijd heb besteed aan hardening! Het is dus normaal dat de score hoger is (**76**).



![Image](assets/fr/045.webp)



## V. Lynis geautomatiseerde planning



**Lynis** biedt ook de optie om zijn controles uit te voeren via een geplande taak. Er is in feite de optie **"--cronjob"**, die alle Lynis-tests uitvoert zonder dat validatie of actie van de gebruiker nodig is. Je kunt dan heel eenvoudig een script maken dat **Lynis** uitvoert en de uitvoer in een bestand met tijdstempel zet met de naam van de server in kwestie. Hier is een bestand van dit type dat je in de map */etc/cron.daily* kunt plaatsen:



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



De variabele **"AUDITOR_NAME"** is gewoon een variabele die we instellen in de optie **"--auditor"** van **Lynis** zodat deze naam in het rapport wordt weergegeven:



![Image](assets/fr/059.webp)



We gaan ook een paar contextuele variabelen maken die ons zullen helpen onszelf beter te organiseren, zoals de hostnaam en datum voor het benoemen van het rapport en de tijdstempel, en het pad naar de map waarin we onze rapporten willen plaatsen.



## VI. Conclusie



Lynis is een zeer praktisch hulpmiddel waarmee je tijd kunt besparen en efficiënter kunt werken als je meer wilt weten over de configuratie van een Linux-server, met name op het gebied van beveiliging. Vergeet echter niet dat elke wijziging moet worden getest voordat deze in productie wordt toegepast, rekening houdend met je eigen gebruik en context.



Je gaat waarschijnlijk niet dezelfde configuratie toepassen op een VPS die is blootgesteld aan het net, waar je maar één SSH-verbinding nodig hebt (omdat jij de enige persoon bent die verbinding maakt), in tegenstelling tot een **bastion** of **scheduler** die meerdere **SSH.** verbindingen nodig hebben



Als je eenmaal een configuratie hebt die bij je past op het gebied van hardening, is het aan te raden om een automatiseringstool te gebruiken zodat je de taken niet handmatig opnieuw hoeft te doen, omdat dit tijdrovend en foutgevoelig zou zijn. Je kunt bijvoorbeeld ** gebruiken: Puppet, Chef, Ansible, enz...**



Vergeet niet om vóór de implementatie met je teams te communiceren: je moet ze laten begrijpen waarom je deze veranderingen doorvoert, niet alleen vertellen dat je ze doorvoert. Uiteindelijk is het de bedoeling om goede praktijken door te geven en dit zal je kansen op succes vergroten.



Tenslotte kun je **Lynis** ook vergelijken met andere tools, waarvan er verschillende zijn. Als je naar gecentraliseerd beheer wilt gaan en toch open source wilt blijven, raad ik de tool [Wazuh] aan (https://wazuh.com/).



**Deze les is afgelopen, veel plezier met Lynis!