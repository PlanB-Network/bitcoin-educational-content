---
name: OPNsense
description: Hoe installeer en configureer ik een OPNsense firewall?
---
![cover](assets/cover.webp)



___



*Deze zelfstudie is gebaseerd op originele inhoud van Florian BURNEL gepubliceerd op [IT-Connect](https://www.it-connect.fr/). Licentie [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Er kunnen wijzigingen zijn aangebracht in de oorspronkelijke tekst.*



___



## I. Presentatie



In deze tutorial bekijken we de OPNsense open source firewall. We bekijken de belangrijkste functies, de vereisten en hoe je deze op FreeBSD gebaseerde oplossing installeert.



Voordat je begint, moet je weten dat **OPNsense en pfSense beide open source firewalls** zijn, gebaseerd op FreeBSD. We kunnen zeggen dat pfSense een soort grote broer van OPNsense is, aangezien de laatste een Fork is die in 2015 is gemaakt. Tot slot is het belangrijk om op te merken dat **OPNsense sinds 2017 is overgeschakeld op HardenedBSD in plaats van FreeBSD**. HardenedBSD is een verbeterde versie van FreeBSD, met geavanceerde beveiligingsfuncties



OPNsense onderscheidt zich door zijn modernere gebruikers-Interface en **frequentere updatefrequentie**. Het updateprogramma van OPNsense bevat namelijk twee grote releases per jaar, die ongeveer elke twee weken worden bijgewerkt (wat resulteert in kleine releases). Deze opvolging is erg interessant in vergelijking met pfSense, als we kijken naar de community versies van deze oplossingen.



![Image](assets/fr/050.webp)



## II. OPNsense functies



OPNsense is een besturingssysteem dat is ontworpen om te fungeren als een firewall en router, hoewel de mogelijkheden talrijk zijn en kunnen worden uitgebreid door extra pakketten te installeren. Het is geschikt voor productiegebruik en wordt voornamelijk gebruikt voor netwerkbeveiliging en flow management.



### A. Belangrijkste kenmerken



Hier zijn enkele van de belangrijkste functies van OPNsense:





- Firewall en NAT**: OPNsense biedt geavanceerde stateful firewall functionaliteit met stateful filtering, evenals network Address translation (NAT) mogelijkheden.





- DNS/DHCP**: OPNsense kan geconfigureerd worden om DNS en DHCP diensten op het netwerk te beheren. Het kan fungeren als een DHCP server, maar kan ook gebruikt worden als een DNS resolver voor machines op het lokale netwerk. Dnsmasq is ook standaard geïntegreerd.





- VPN**: OPNsense ondersteunt verschillende VPN-protocollen, waaronder IPsec, OpenVPN en WireGuard, waardoor veilige verbindingen mogelijk zijn voor externe toegang tot mobiele werkstations of interconnectie tussen locaties.





- Web proxy**: OPNsense bevat een webproxy om de internettoegang te controleren en te filteren. Deze kan ook worden gebruikt om inhoud te filteren en netwerktoegang te beheren.





- Bandbreedtebeheer (QoS)**: OPNsense biedt Quality of Service (QoS)-beheerfuncties om voorrang te geven aan netwerkverkeer en de bandbreedte van het netwerk beter te beheren.





- Captive portal**: met deze functie kun je de toegang van gebruikers tot het netwerk beheren via een verificatiepagina (lokale basis, vouchers, enz.). Het is een functie die vaak wordt gebruikt voor openbare Wi-Fi-netwerken.





- IDS/IPS**: OPNsense integreert Suricata om intrusion detection en prevention (IDS/IPS) functies te bieden om het netwerk tegen aanvallen te beschermen.





- Hoge beschikbaarheid (CARP)**: OPNsense ondersteunt CARP (*Common Address Redundancy Protocol*) voor hoge beschikbaarheid tussen meerdere OPNsense firewalls, zodat de service actief blijft, zelfs als de hardware uitvalt.





- Rapportage en monitoring**: OPNsense biedt realtime rapportage- en bewakingstools om de netwerkprestaties te volgen (met NetFlow) en potentiële problemen op te sporen, dankzij de aanmaak van logs. Dit omvat ook grafieken. De Monit tool is geïntegreerd in OPNsense en maakt toezicht op de firewall zelf mogelijk.



### B. Extra pakketten



Dit is slechts een overzicht van de functies die OPNsense biedt. Bovendien kunt u met de **pakketcatalogus** die toegankelijk is via de OPNsense administratie Interface de firewall verrijken met extra functionaliteiten**. Deze omvatten een ACME client, een Wazuh agent, de NTP Chrony service en Caddy als reverse proxy.



![Image](assets/fr/051.webp)



## III. OPNsense voorwaarden



Allereerst moet je beslissen waar je OPNsense gaat installeren. Er zijn verschillende mogelijke oplossingen, waaronder installatie op:





- Een hypervisor als virtuele machine, of het nu Hyper-V, Proxmox, VMware ESXi, enz. is.
- Een machine als een *baar-metaal* systeem. Dit kan een mini PC zijn die als firewall fungeert.



U kunt ook **een OPNsense rack-mountable appliance** kopen via onze online winkel.



U moet rekening houden met de hardware middelen die nodig zijn om OPNsense te draaien. Dit wordt beschreven op [deze documentatiepagina] (https://docs.opnsense.org/manual/hardware.html).



**Minimale en aanbevolen middelen voor productie:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Tenslotte **zijn de benodigde bronnen vooral afhankelijk van het aantal te beheren verbindingen**, en dus van de benodigde bandbreedte**. Daarnaast moet je **rekening houden met de services die worden geactiveerd en gebruikt** (proxy, inbraakdetectie, etc...) omdat ze veel CPU en/of RAM kunnen gebruiken.



Je hebt ook het OPNsense installatie ISO image nodig, dat je kunt downloaden van [de officiële website](https://opnsense.org/download/). Voor installatie op een VM, selecteer "**dvd**" als het type image om een ISO image te verkrijgen (en doe ermee wat je wilt...). Voor installatie via een opstartbare USB-sleutel selecteert u de optie "**vga**" om een "**.img**"-bestand te verkrijgen.



![Image](assets/fr/048.webp)



U hebt ook een computer nodig voor OPNsense administratie en testen.



## IV. Doelconfiguratie



Ons doel is om





- Maak een intern virtueel netwerk aan (192.168.10.0/24 - LAN)**, dat toegang heeft tot het internet via de OPNsense firewall. Voor productiegebruik kan dit uw lokale netwerk, kabel en/of Wi-Fi zijn.
- NAT** activeren en configureren zodat VM's in het interne virtuele netwerk toegang hebben tot internet
- Activeer en configureer de DHCP-server op OPNsense** om een IP-configuratie te distribueren naar toekomstige machines die op het interne virtuele netwerk zijn aangesloten
- Configureer de firewall** om alleen uitgaande LAN naar WAN stromen in HTTP (80) en HTTPS (443) toe te staan.
- Configureer de firewall** zodat het virtuele LAN OPNsense kan gebruiken als DNS-resolver (53).



Als je het Hyper-V-platform gebruikt, krijg je de volgende weergave:



![Image](assets/fr/033.webp)



## V. De OPNsense firewall installeren



### A. De opstartbare USB-sleutel voorbereiden



De eerste stap is het voorbereiden van het installatiemedium: **de opstartbare USB-sleutel met OPNsense**. Dit is natuurlijk optioneel als je in een virtuele omgeving werkt, maar in ieder geval moet je het OPNsense installatie ISO image downloaden.



Na het downloaden krijg je **een archief met een image in ".img"** formaat. Je kunt **een opstartbare USB-stick** maken met verschillende applicaties, waaronder **balenaEtcher**: ultra-simpel in gebruik. Bovendien herkent de applicatie het image in het archief, zodat je het niet van tevoren hoeft uit te pakken.





- [Download balenaEtcher](https://etcher.balena.io/)



Zodra de toepassing is geïnstalleerd, selecteert u uw afbeelding en uw USB-sleutel en klikt u op "Flash! Wacht even.



![Image](assets/fr/049.webp)



Nu ben je klaar om te installeren.



### B. Het OPNsense systeem installeren



Start de machine op waarop OPNsense draait. Je zou een welkomstpagina moeten zien zoals hieronder. Gedurende enkele seconden zal het getoonde scherm zichtbaar zijn in het venster. Laat het proces zijn werk doen...



![Image](assets/fr/019.webp)



De OPNsense image wordt op de machine geladen, zodat het systeem kan worden benaderd in "**live**" modus, d.w.z. tijdelijk opgeslagen in het geheugen.



![Image](assets/fr/025.webp)



Dan kom je bij een Interface zoals hieronder. Log in met login "**installer**" en wachtwoord "**opnsense**". Houd er rekening mee dat het toetsenbord op dit moment **QWERTY** is. Op dit punt zullen we **beginnen met het OPNsense installatieproces**.



![Image](assets/fr/026.webp)



Er verschijnt een nieuwe wizard op het scherm. De eerste stap is het selecteren van de toetsenbordindeling die overeenkomt met je configuratie. Selecteer voor een AZERTY-toetsenbord de optie "**Frans (accenttoetsen)**" uit de lijst en dubbelklik vervolgens**.



![Image](assets/fr/027.webp)



De tweede stap is het selecteren van de taak die uitgevoerd moet worden. Hier gaan we een installatie uitvoeren met het **ZFS bestandssysteem**. Plaats jezelf op de regel "**Install (ZFS)**" en bevestig met **Enter**.



![Image](assets/fr/028.webp)



Selecteer in de derde stap "**stripe**" omdat onze machine is uitgerust met **slechts één schijf**: er is geen redundantie mogelijk om de firewall-opslag en zijn gegevens te beveiligen. Dit is vooral relevant bij installatie op een fysieke machine om te beschermen tegen hardwarefouten van een schijf, via het RAID-principe.



![Image](assets/fr/029.webp)



Druk in de vierde stap gewoon op **Enter** om te bevestigen.



![Image](assets/fr/030.webp)



Bevestig ten slotte door "**YES**" te selecteren en op de **Enter** toets te drukken.



![Image](assets/fr/031.webp)



Nu moet je wachten terwijl OPNsense wordt geïnstalleerd... Dit proces duurt ongeveer 5 minuten.



![Image](assets/fr/032.webp)



Zodra de installatie is voltooid, kunnen we het wachtwoord "**root**" wijzigen voordat we opnieuw opstarten. Selecteer "**Root Password**", druk op **Enter** en voer het wachtwoord "**root**" twee keer in.



![Image](assets/fr/020.webp)



Selecteer ten slotte "**Complete Install**" en druk op **Enter**. Maak van de gelegenheid gebruik om de schijf uit het DVD-station van de VM te werpen**. In de VM-instellingen kun je ook instellen dat de eerste keer wordt opgestart op schijf.



![Image](assets/fr/021.webp)



De virtuele machine zal opnieuw opstarten en het OPNsense systeem laden vanaf schijf, aangezien we het net geïnstalleerd hebben. Log in met de "root" account in de console en je nieuwe wachtwoord (anders is het standaard wachtwoord "**opnsense**").



### D. Netwerkinterfaces koppelen



Het onderstaande scherm verschijnt. Selecteer "**1**" en druk op **Enter** om de netwerkkaarten van de machine te associëren met de OPNsense interfaces.



![Image](assets/fr/022.webp)



Eerst vraagt de wizard u om verbindingsaggregatie en VLAN's te configureren. Geef "**n**" op om te weigeren en bevestig uw antwoord telkens met **Enter**. Vervolgens moet u de twee interfaces "**hn0**" en "**hn1**" toewijzen aan het **WAN** en **LAN**. In principe komt "**hn0**" overeen met het WAN en de andere Interface met het LAN.



Zo werkt het:



![Image](assets/fr/023.webp)



We hebben nu:





- Het Interface **LAN** is gekoppeld aan de "**hn1**" netwerkkaart en aan het OPNsense standaard IP Address, d.w.z. **192.168.1.1/24**.
- De Interface **WAN** is verbonden met de "**hn0**" netwerkkaart en met een IP Address opgehaald via **DHCP** op het lokale netwerk (dankzij onze externe virtuele switch).



Standaard is de OPNsense administratie Interface alleen toegankelijk vanaf de LAN Interface, om voor de hand liggende veiligheidsredenen. U moet dus verbinding maken met de LAN Interface van de firewall om het beheer uit te voeren. Als dit niet mogelijk is, kunt u OPNsense tijdelijk vanaf het WAN beheren. Hiervoor moet u de firewallfunctie uitschakelen.



Schakel hiervoor over naar shellmodus via de optie "**8**" en voer het volgende commando uit:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Toegang tot het OPNsense Interface beheersysteem



De OPNsense Administratie Interface is toegankelijk via HTTPS, via het IP Address van de LAN** Interface (of het WAN). Uw browser brengt u naar een inlogpagina. Log in met het "root" account en wachtwoord dat je eerder hebt gekozen.



![Image](assets/fr/034.webp)



Wacht een paar seconden... U wordt gevraagd een wizard te volgen om de basisconfiguratie uit te voeren. Klik op "**Next**" om verder te gaan.



![Image](assets/fr/036.webp)



De eerste stap is het definiëren van de hostnaam, de domeinnaam, het kiezen van de taal en het definiëren van de DNS server(s) die gebruikt moeten worden voor naamresolutie. Door de optie "**Enable Resolver**" aan te houden, kan de firewall worden gebruikt als DNS-resolver, wat handig is voor de machines in ons virtuele LAN.



![Image](assets/fr/037.webp)



Ga verder naar de volgende stap. De wizard geeft je de optie om **een NTP-server te definiëren voor datum- en tijdsynchronisatie**, hoewel er standaard al servers zijn geconfigureerd. Daarnaast is het essentieel om de tijdzone te kiezen die overeenkomt met je geografische locatie (tenzij je speciale vereisten hebt).



![Image](assets/fr/038.webp)



Dan volgt een belangrijke stap: **Het configureren van het Interface WAN**. Op dit moment is het geconfigureerd in DHCP en het zal in deze configuratiemodus blijven, tenzij je een statische IP Address wilt instellen.



![Image](assets/fr/039.webp)



Nog steeds op de Interface WAN configuratiepagina, moet je de optie "**Blokkeer toegang tot privé netwerken via WAN**" uitvinken als het netwerk aan de WAN kant privé adressering gebruikt. Dit zal waarschijnlijk het geval zijn als je een Lab draait, waardoor je mogelijk geen toegang hebt tot het internet.



![Image](assets/fr/040.webp)



Vervolgens kunt u **een "root"** wachtwoord definiëren, maar dit is optioneel omdat we dit al gedaan hebben.



![Image](assets/fr/041.webp)



Ga door tot het einde om de configuratie opnieuw te laden. Als je de controle via het WAN moet blijven overnemen, start dan het bovenstaande commando opnieuw zodra dit proces is voltooid.



![Image](assets/fr/042.webp)



Dat is alles!



![Image](assets/fr/035.webp)



### E. DHCP-configuratie



Ons doel is om de OPNsense DHCP server te gebruiken om IP adressen te verdelen over het virtuele LAN. Om dit te doen, moeten we naar deze menulocatie gaan:



```
Services > ISC DHCPv4 > [LAN]
```



**Zoals je kunt zien, is DHCP al standaard ingeschakeld op het LAN ** Als je niet geïnteresseerd bent in deze service, moet je het uitschakelen. Hoewel het al is ingeschakeld en we het willen gebruiken, is het belangrijk om de configuratie te controleren.



Indien nodig kunt u het bereik van IP-adressen die moeten worden gedistribueerd wijzigen: **192.168.10.10** tot **192.168.10.245**, afhankelijk van de huidige instellingen.



![Image](assets/fr/046.webp)



We kunnen ook zien dat de velden "**DNS servers**", "**Gateway**", "**Domeinnaam**", enz. standaard leeg zijn. In feite is er een automatische overerving van bepaalde opties en standaardwaarden voor deze verschillende velden. Bijvoorbeeld, voor de DNS server zal het IP Address van het Interface LAN verdeeld worden, waardoor de OPNsense firewall als DNS resolver gebruikt kan worden.



Sla de configuratie op nadat u wijzigingen hebt aangebracht, indien nodig.



![Image](assets/fr/047.webp)



Om de DHCP-server te testen, moet je een machine aansluiten op het LAN-netwerk van je firewall.



Deze machine moet een IP Address krijgen van de OPNsense DHCP server en onze machine moet toegang hebben tot het netwerk. Internettoegang moet werken. Houd er rekening mee dat als u de firewall-functie hebt uitgeschakeld om OPNsense vanaf het WAN te benaderen, dit de NAT uitschakelt, waardoor u geen toegang tot het web krijgt.



**Noot**: de huidige DHCP leases zijn zichtbaar via de OPNsense administratie Interface. Ga hiervoor naar de volgende locatie: **Services > ISC DHCPv4 > Leases**.



![Image](assets/fr/045.webp)



### F. NAT en firewallregels configureren



Het goede nieuws is dat we nu toegang hebben tot de OPNsense administratie Interface vanaf het LAN.



```
https://192.168.1.10
```



Laten we na het inloggen op OPNsense de NAT-configuratie ontdekken. Ga naar deze locatie: **Firewall > NAT > Outbound**. Hier kunt u kiezen tussen automatisch (standaard) en handmatig aanmaken van uitgaande NAT regels.



Kies de automatische modus via de optie "**Automatic generation of outgoing NAT rules**" en klik op "**Save**" (in principe is deze configuratie al actief). In automatische modus maakt OPNsense zelf een NAT regel aan voor elk van uw netwerken.



![Image](assets/fr/043.webp)



Op dit moment hebben alle computers die verbonden zijn met het virtuele LAN "**192.168.10.0/24**" onbeperkt toegang tot het internet. Ons doel is echter om de toegang tot het WAN te beperken tot HTTP en HTTPS protocollen en DNS op het Interface LAN van de firewall.



Dus moeten we firewallregels maken... Blader als volgt door het menu: **Firewall > Regels > LAN**.



**Standaard zijn er twee regels om al het uitgaande LAN verkeer te autoriseren, in IPv4 en IPv6**. Deactiveer deze twee regels door te klikken op de Green pijl uiterst links, aan het begin van elke regel.



Maak vervolgens drie nieuwe regels aan om het **LAN netwerk** (d.w.z. "**LAN net**") te autoriseren voor:





- toegang tot alle bestemmingen met **HTTP**.
- toegang tot alle bestemmingen met **HTTPS**.
- vraag **OPNsense** aan op zijn **Interface LAN** (d.w.z. "**LAN Address**"), via het **DNS-protocol** (dit impliceert dat de firewall als DNS wordt gebruikt), anders machtig je DNS-resolver via zijn IP Address.



Dit geeft het volgende resultaat:



![Image](assets/fr/044.webp)



Je hoeft alleen nog maar te klikken op "**Wijzigingen toepassen**" om de nieuwe firewallregels over te zetten naar productie. **Houd er rekening mee dat alle stromen die niet expliciet zijn geautoriseerd standaard worden geblokkeerd



De LAN-machine heeft toegang tot het internet met HTTP en HTTPS. Alle andere protocollen worden geblokkeerd.



![Image](assets/fr/018.webp)



## IV. Conclusie



Als je deze handleiding volgt, kun je OPNsense installeren en meteen aan de slag gaan. OPNsense biedt een groot aantal functies om je netwerkverkeer efficiënt te beveiligen en te beheren, en is geschikt voor gebruik in professionele omgevingen.



Deze installatie is nog maar het begin: voel je vrij om de menu's te verkennen en andere functies te configureren om OPNsense aan te passen aan jouw behoeften.