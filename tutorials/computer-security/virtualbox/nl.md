---
name: VirtualBox
description: VirtualBox installeren op Windows 11 en je eerste VM maken
---
![cover](assets/cover.webp)



___



*Deze zelfstudie is gebaseerd op originele inhoud van Florian Burnel gepubliceerd op [IT-Connect](https://www.it-connect.fr/). Licentie [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Er kunnen wijzigingen zijn aangebracht in de oorspronkelijke tekst.*



___




## I. Presentatie



In deze tutorial leren we hoe je VirtualBox installeert op Windows 11 om virtuele machines te maken, of het nu gaat om Windows 10, Windows 11, Windows Server of een Linux-distributie (Debian, Ubuntu, Kali Linux, enz.).



Deze inleidende tutorial over VirtualBox helpt je op weg met deze open source virtualisatieoplossing, ontwikkeld door Oracle, die volledig gratis is. Later zullen andere tutorials online worden gezet om dieper op het onderwerp in te gaan.



Als het gaat om het virtualiseren van een werkstation, voor testdoeleinden als onderdeel van een project of tijdens je IT-studie, is VirtualBox duidelijk een goede oplossing. Het is ook een alternatief voor andere oplossingen zoals Hyper-V, dat is geïntegreerd in Windows 10 en Windows 11 (en Windows Server), en VMware Workstation (tegen betaling) / VMware Workstation Player (gratis voor persoonlijk gebruik).



Mijn configuratie: **een Windows 11 werkstation waarop ik VirtualBox ga installeren**, maar je kunt VirtualBox zowel op Windows 10 (of een oudere versie) als op Linux installeren. Wat virtuele machines betreft, ondersteunt VirtualBox een groot aantal systemen, waaronder Windows (bijv. Windows 10, Windows 11, Windows Server 2022, enz.), Linux (Debian, Rocky Linux, Ubuntu, Fedora, enz.), BSD (PfSense) en macOS.



## II. VirtualBox voor Windows 11 downloaden



Om VirtualBox te downloaden voor installatie op een Windows machine, is er maar één goede Address: de [officiële VirtualBox website](https://www.virtualbox.org/wiki/Downloads) in de "**Downloads**" sectie. Klik gewoon op "Windows hosts" om te beginnen met het downloaden van deze executable, die iets meer dan 100 MB groot is.



![Image](assets/fr/025.webp)



## III. VirtualBox installeren op Windows 11



### A. VirtualBox installeren



Het installeren van VirtualBox** is eenvoudig en het proces is hetzelfde voor alle versies van Windows. Start eerst de VirtualBox executable die je net hebt gedownload en klik dan op "**Next**".



![Image](assets/fr/026.webp)



Deze installatie is aanpasbaar, maar ik raad je aan om alle functies te installeren: wat het geval is met de standaard selectie. In de afbeelding hieronder zie je verschillende Elements, waaronder:





- VirtualBox USB-ondersteuning** om VirtualBox USB-apparaten te laten ondersteunen
- VirtualBox Bridged Network** om netwerkondersteuning in "Bridge"-modus te integreren (de virtuele machine kan rechtstreeks verbinding maken met uw lokale netwerk)
- VirtualBox Host-Only Network** om netwerkondersteuning te integreren in de "Host-Only" modus (de virtuele machine kan alleen communiceren met uw Windows 11 fysieke host en andere virtuele machines in deze modus)



Klik op "**Volgende**" om verder te gaan.



![Image](assets/fr/001.webp)



Klik op "**Ja**", en houd er rekening mee dat **het netwerk op uw Windows 11-machine even onderbroken wordt**, terwijl VirtualBox netwerkaanpassingen uitvoert om verschillende netwerktypes te ondersteunen, inclusief Bridge-modus.



![Image](assets/fr/002.webp)



Zodra je hebt bevestigd, start de installatie... En er verschijnt een melding "**Wilt u deze apparaatsoftware installeren? Vink de optie "**Always trust software from Oracle Corporation**" aan en klik op "**Install**". VirtualBox moet nu verschillende stuurprogramma's op uw computer installeren.



![Image](assets/fr/003.webp)



De installatie is nu voltooid! Vink de optie "**Start Oracle VM VirtualBox 6.1.34 na installatie**" aan en klik op "**Klik**" om de software te starten.



![Image](assets/fr/004.webp)



### B. Het uitbreidingspakket toevoegen



Nog steeds op de officiële VirtualBox site (zie vorige link), kun je een officieel uitbreidingspakket downloaden, toegankelijk onder de "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" sectie door te klikken op de "**Alle ondersteunde platformen**" link. Met dit pakket kun je extra functionaliteiten toevoegen aan VirtualBox: het is niet verplicht om het toe te voegen, maar het kan nuttig zijn! Het bevat bijvoorbeeld ondersteuning voor USB 3.0 in VM's, webcamondersteuning en schijfversleuteling.



Open VirtualBox, klik op "**Bestand**" en vervolgens op "**Instellingen**" in het menu.



![Image](assets/fr/005.webp)



Klik op "**Extensions**" aan de linkerkant (1), dan op de "**+**" knop aan de rechterkant (2) om **het VirtualBox** uitbreidingspakket te laden dat je net hebt gedownload (3).



![Image](assets/fr/006.webp)



Bevestig door op de knop "**Installatie**" te klikken.



![Image](assets/fr/007.webp)



Klik op "**OK**": het officiële uitbreidingspakket is nu geïnstalleerd op uw VirtualBox-instantie!



![Image](assets/fr/008.webp)



Laten we verder gaan met het maken van onze eerste virtuele machine.



## IV. Uw eerste VirtualBox VM maken



Om een nieuwe virtuele machine aan te maken in VirtualBox, klik je gewoon op de "**New**" knop om de VM creatie wizard te starten. Aangezien dit de eerste keer is dat je VirtualBox opstart, wil ik je wat meer details geven over Interface en de andere knoppen.





- Instellingen**: algemene VirtualBox-configuratie (standaard VM-map, updatebeheer, taal, NAT-netwerken, extensies, enz.)
- Importeren**: een virtueel apparaat importeren in OVF-formaat
- Exporteren**: een bestaande virtuele machine in OVF-indeling exporteren om een virtueel apparaat te maken
- Toevoegen**: een bestaande virtuele machine toevoegen aan uw VirtualBox-inventaris, in standaard VirtualBox-formaat (.vbox) of XML-formaat



Aan de linkerkant geeft het gedeelte "**Tools**" toegang tot **geavanceerde functies, met name voor het beheren van het virtuele netwerk, maar ook voor het beheren van VM-opslag**. Onder het item "**Tools**" worden later uw virtuele machines toegevoegd.



![Image](assets/fr/009.webp)



### A. VM-aanmaakproces



**Ter herinnering, VirtualBox ondersteunt een groot aantal besturingssystemen, waaronder Windows, Linux en BSD. In dit voorbeeld ga ik een virtuele machine voor Windows 11 maken. Er moeten verschillende velden worden ingevuld:





- Naam**: naam van de virtuele machine (dit is de naam die zal worden weergegeven in VirtualBox)
- Machinemap**: waar de virtuele machine moet worden opgeslagen, wetende dat op deze locatie een submap met de naam van de VM zal worden aangemaakt
- Type**: het type besturingssysteem, afhankelijk van welk besturingssysteem je wilt installeren
- Version**: de versie van het systeem dat je wilt installeren, in dit geval Windows 11, dus "**Windows11_64**"



Klik op "**Volgende**" om verder te gaan.



![Image](assets/fr/010.webp)



Afhankelijk van het besturingssysteem dat je in de vorige stap hebt geselecteerd, doet **VirtualBox aanbevelingen over de resources die aan de virtuele machine moeten worden toegewezen**. Hier hebben we het over het RAM-geheugen dat u wilt toewijzen aan de VM. Laten we uitgaan van 4 GB, omdat dit inderdaad wordt aanbevolen voor Windows 11, maar als je een tekort aan resources hebt, kun je in plaats daarvan 2 GB opgeven. **Doorgaan



**Noot**: de middelen die aan de virtuele machine zijn toegewezen, kunnen later worden gewijzigd.



![Image](assets/fr/011.webp)



Wat de virtuele Hard schijf betreft, beginnen we vanaf nul, dus we moeten "**Create virtual Hard disk now**" kiezen, zodat de VM opslagruimte heeft om het besturingssysteem te installeren en gegevens op te slaan. Klik op "**Create**".



![Image](assets/fr/012.webp)



VirtualBox ondersteunt drie verschillende formaten voor virtuele Hard schijven, wat een groot verschil is met andere oplossingen zoals VMware en Hyper-V. Je kunt kiezen uit drie formaten:





- VDI**, de officiële VirtualBox-indeling
- VHD**, de officiële Hyper-V-indeling, hoewel de nieuwe VHDX-indeling tegenwoordig vaker wordt gebruikt
- VMDX** is de officiële VMware-indeling voor zowel VMware Workstation als VMware ESXi



Om een virtuele machine te maken die alleen op deze VirtualBox-instantie wordt gebruikt, kiest u "**VDI**". Aan de andere kant, als de virtuele Hard schijf op een later tijdstip aan een Hyper-V host wordt gekoppeld, kan het een goed idee zijn om te beginnen met het VHD-formaat om te voorkomen dat deze moet worden geconverteerd. Klik op "**Next**".



![Image](assets/fr/013.webp)



**De virtuele schijf kan dynamisch zijn of een vaste grootte hebben**. Als het dynamisch is, zal het bestand dat **de virtuele schijf representeert (hier een .vdi-bestand) groeien als er gegevens naar de schijf worden geschreven** totdat het zijn maximale grootte bereikt, maar het zal niet krimpen als er gegevens worden verwijderd. Als het daarentegen een vaste grootte heeft, wordt **de totale opslagruimte onmiddellijk toegewezen (en dus gereserveerd)**, wat iets hogere prestaties mogelijk maakt, maar langer duurt wanneer de virtuele schijf voor het eerst wordt aangemaakt.



Persoonlijk vind ik voor virtuele testmachines met VirtualBox de modus "**Dynamisch toegewezen**" voldoende.



![Image](assets/fr/014.webp)



**De volgende stap is het specificeren van de grootte van de virtuele schijf**, waarbij je in gedachten moet houden dat de schijf standaard wordt opgeslagen in de VM-map (dit kan in dit stadium worden gewijzigd). Ik heb een grootte van 64 GB aangegeven om te voldoen aan de vereisten van Windows 11, maar ook hier kan een kleinere grootte worden toegewezen. Klik op "**Create**" om de VM te maken!



![Image](assets/fr/015.webp)



Op dit punt bevindt de VM zich in onze inventaris, is deze geconfigureerd, maar is het besturingssysteem nog niet geïnstalleerd. We moeten de configuratie van de VM afronden voordat we deze opstarten.



### B. Een ISO-image toewijzen aan een VirtualBox VM



Om Windows 11, of elk ander systeem, te installeren, hebben we installatiebronnen nodig. In de meeste gevallen gebruiken we een schijfimage in ISO-indeling om een besturingssysteem te installeren. **Het is noodzakelijk om de Windows 11 ISO-image in het virtuele dvd-station van onze VM te laden



Klik op de VM in de VirtualBox-inventaris (1) en vervolgens op de knop "**Configuratie**" (2), die toegang geeft tot de algemene configuratie van deze virtuele machine. Dit menu wordt gebruikt om resources te beheren (bijv. RAM verhogen, CPU configureren, enz.). Klik op "**Storage**" aan de linkerkant (3), op de DVD-drive waar staat "**Empty**" voor het moment (4), klik dan op het DVD-vormige pictogram (5) en "**Choose a disk file**".



![Image](assets/fr/016.webp)



Selecteer de ISO-image van het besturingssysteem dat je wilt installeren en klik op OK. Dit is wat ik krijg:



![Image](assets/fr/017.webp)



Blijf in het gedeelte "**Configuratie**" van de VM, ik moet nog een paar dingen uitleggen.



### C. VM-netwerkverbinding



Ga naar de sectie "**Netwerk**" aan de linkerkant. In dit onderdeel kun je het netwerk van de virtuele machine beheren: het aantal virtuele netwerkinterfaces (maximaal 4 per VM), MAC Address en de netwerktoegangsmodus (NAT, bridge access, intern netwerk, enz.). **Als je wilt dat je virtuele machine toegang heeft tot het internet, selecteer dan "NAT" of "Bridge Access"**, maar deze tweede modus vereist dat er een DHCP-server actief is op je netwerk, of je moet handmatig een IP Address configureren.



Opmerking: ik zal in een apart artikel dieper ingaan op het netwerkgedeelte.



![Image](assets/fr/018.webp)



### D. Het aantal virtuele processors



Net als een fysieke computer heeft een virtuele machine RAM, een Hard schijf en een processor nodig om te functioneren. Toen we de VM aanmaakten, is het je misschien opgevallen dat de processorconfiguratie niet in de wizard was opgenomen. Deze kan echter op elk moment worden geconfigureerd via het tabblad "**Systeem**" en vervolgens "**Processor**", waar je het aantal virtuele processors kunt kiezen.



Opmerking: de optie "**Enable VT-x/AMD-v nested**" is vereist voor geneste virtualisatie.



In mijn geval heeft de virtuele machine 2 virtuele processors:



![Image](assets/fr/019.webp)



**Aarzel niet om de andere secties van het configuratiemenu te bekijken.



### E. Eerste boot en installatie van het besturingssysteem



Om een virtuele machine te starten, selecteer je deze in de inventaris en klik je op de knop "**Start**". Er wordt een tweede venster geopend met een visueel overzicht van de VM.



![Image](assets/fr/020.webp)



Au, ik krijg een vervelende foutmelding en mijn virtuele machine wil niet opstarten! De foutmelding is "Inloggen mislukt voor virtuele machine..." met de volgende details:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



In feite is dit normaal omdat **de virtualisatiefunctie niet is ingeschakeld op mijn computer**! Om dit probleem te verhelpen, moet je je computer herstarten om toegang te krijgen tot het BIOS en virtualisatie in te schakelen.



![Image](assets/fr/021.webp)



Zonder te wachten start ik mijn computer opnieuw op en **druk op de "SUPPR"-toets om toegang te krijgen tot het BIOS** (de toets kan per machine verschillen en kan bijvoorbeeld F2 zijn) van mijn ASUS-moederbord. Om virtualisatie te activeren, moet in mijn geval "SVM Mode" zijn ingeschakeld. Ook hier kan de naam van moederbord tot moederbord en van fabrikant tot fabrikant verschillen. Zoek naar een functie die verwijst naar **AMD-V** (voor een AMD CPU) of **Intel VT-x** (voor een Intel CPU).



![Image](assets/fr/022.webp)



Zodra dit is gebeurd, sla je de wijziging op en start je de fysieke machine opnieuw op... Deze keer kan **VirtualBox de virtuele machine** starten en de Windows ISO-image laden om het besturingssysteem te installeren! 🙂



![Image](assets/fr/023.webp)



Op onze Windows 11 fysieke host, waar VirtualBox is geïnstalleerd, kunnen we zien dat de Windows 11 virtuele machine map verschillende bestanden bevat.





- Het VBOX**-bestand (in XML-indeling) dat overeenkomt met de VM-configuratie (RAM, CPU, enz.)
- Het VBOX-PREV** bestand is een back-up van de vorige configuratie
- Het VDI**-bestand komt overeen met de virtuele Hard schijf in dynamische modus, dus het is momenteel slechts 13 GB groot, terwijl de maximale grootte 64 GB is
- Het NVRAM**-bestand bevat de BIOS-status van de virtuele machine, wat overeenkomt met het niet-vluchtige geheugen van een fysieke machine



![Image](assets/fr/024.webp)



## V. Conclusie



**VirtualBox werkt nu op onze Windows 11 fysieke machine! Nu hoeven we er alleen nog maar gebruik van te maken en virtuele machines te maken!** Ik kom in een ander artikel terug op het installeren van Windows 11 in een VirtualBox VM. Voor Windows 10, Windows Server of een Linux-distributie (Ubuntu, Debian, enz.), laat je gewoon leiden!