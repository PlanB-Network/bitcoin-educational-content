---
name: Qubes
description: Een redelijk veilig besturingssysteem.
---

![cover](assets/cover.webp)



Qubes OS is een vrij, open-source besturingssysteem ontworpen voor gebruikers die veiligheid hoog in het vaandel hebben staan. De bijzonderheid is gebaseerd op een eenvoudig maar radicaal idee: in plaats van de computer als een geheel te beschouwen, verdeelt het het gebruik ervan in onafhankelijke compartimenten genaamd **_qubes_**.



Elke qube functioneert als een **geïsoleerde virtuele omgeving**, met een specifiek vertrouwensniveau en functie. Dus zelfs als een applicatie gecompromitteerd is, blijft de aanval beperkt tot de qube zonder de rest van het systeem te beïnvloeden.



> Als je beveiliging serieus neemt, is Qubes OS het beste besturingssysteem dat momenteel beschikbaar is. - **Edward Snowden**.

Het installeren van Qubes OS vereist echter meer voorbereiding dan het installeren van een conventioneel besturingssysteem. Je moet bepaalde hardwarevereisten controleren, de basisprincipes van virtualisatie begrijpen en een andere ervaring accepteren, waarbij elke dagelijkse taak wordt gezien in termen van scheiding. Maar eenmaal geïnstalleerd biedt Qubes OS een robuust raamwerk dat de manier waarop je dagelijks met je computer omgaat herdefinieert. In deze tutorial leggen we uit hoe Qubes OS werkt en hoe je het eenvoudig op je systeem kunt installeren.



## Hoe werkt Qubes OS?



Qubes OS is gebaseerd op het principe van compartimentering. In plaats van een enkel systeem te gebruiken, vertrouwt het op de **Xen** hypervisor om geïsoleerde virtuele machines te maken, qubes genaamd. Elke qube is gewijd aan een specifieke taak of vertrouwensniveau (werk, persoonlijk browsen, bankieren, etc.). Deze scheiding zorgt ervoor dat een compromis in één qube zich niet kan verspreiden naar de andere qube's, die fungeren als verschillende onafhankelijke computers binnen één enkele machine.



Gebruiker Interface wordt beheerd door een centraal, beveiligd domein genaamd **dom0**. Dit domein is volledig geïsoleerd van het Internet, waardoor het het hart van het systeem is. Hoewel vensters en menu's worden weergegeven door dom0, vindt de daadwerkelijke uitvoering van applicaties plaats in hun respectievelijke qubes.



## De verschillende soorten qubes



Rond dom0 draaien verschillende soorten qubes, elk met een heel specifieke rol.





- De **AppVM** worden gebruikt om alledaagse applicaties te draaien: de gebruiker kan dus zijn professionele e-mails scheiden van zijn webbrowsing of bankactiviteiten, waarbij elke omgeving volledig onafhankelijk blijft van de andere.





- Deze AppVM's zijn zelf gebaseerd op **TemplateVM's**, die dienen als gecentraliseerde sjablonen voor het installeren en updaten van software, waardoor het niet meer nodig is om elke qube apart te beheren.



Qubes OS integreert ook virtuele machines die gespecialiseerd zijn in **systeemdiensten**.





- De **NetVM** beheert direct de **netwerkapparaten** en zorgt voor verbinding met het internet. Ze worden vaak geassocieerd met **FirewallVM's**, die ingrijpen om **verkeer** te filteren en de blootstelling van andere qubes te beperken.





- ServiceVM's spelen een vergelijkbare rol, bijvoorbeeld in USB-apparaatbeheer, altijd met dezelfde logica: isoleer de meest risicovolle componenten om het aanvalsoppervlak te verkleinen.



Voor incidentele of risicovolle taken biedt Qubes OS **DisposableVM**. Deze efemere qubes worden on the fly aangemaakt om **een verdacht document** te openen of **een dubieuze site** te bezoeken, en verdwijnen volledig wanneer ze worden gesloten, waardoor alle sporen worden gewist en een aanhoudende aanval wordt voorkomen.



### Het veilige kopieermechanisme (qrexec)



Uitwisselingen tussen qubes zijn gebaseerd op **qrexec**, een inter-VM communicatiesysteem ontworpen voor beveiliging. In plaats van qubes vrij te laten communiceren, legt qrexec **specifiek beleid** op: een bestand dat van de ene AppVM naar de andere wordt gekopieerd, of tekst die via het klembord wordt overgebracht, gaat altijd door een kanaal dat door het systeem wordt bewaakt en gevalideerd. Op deze manier wordt zelfs het kopiëren en plakken gecontroleerd om de verspreiding van malware te voorkomen.



### Schijfbeheer



Qubes OS gebruikt een ingenieus systeem voor opslagbeheer. TemplateVM's bevatten de gemeenschappelijke softwarebasis, terwijl AppVM's alleen hun persoonlijke gegevens en specifieke bestanden toevoegen. Dit vermindert het gebruik van schijfruimte en vergemakkelijkt globale updates. DisposableVM's gebruiken daarentegen tijdelijke volumes die volledig verdwijnen wanneer ze gesloten worden. Dit model garandeert niet alleen een betere beveiliging, maar ook een efficiënt beheer van bronnen.



## Waarom kiezen voor Qubes OS?



De voordelen van Qubes OS liggen vooral in het unieke beveiligingsmodel. De kern van deze aanpak is compartimentering, die de gebruiker beschermt door elke taak te isoleren in aparte virtuele machines. Praktisch gezien kan een geïnfecteerde e-mail of kwaadaardige website slechts een enkele qube compromitteren, waardoor de rest van het systeem en uw persoonlijke gegevens volledig beschermd blijven. Deze architectuur beperkt complexe aanvallen aanzienlijk die zich op een conventioneel systeem vrij zouden kunnen verspreiden.



Qubes OS biedt ook volledige transparantie en controle over uw digitale omgeving. Je weet precies welke software toegang heeft tot welke bron, of dat nu het netwerk, een USB-apparaat of andere gevoelige onderdelen zijn. Het systeem integreert standaard geavanceerde beveiligingsfuncties, zoals volledige schijfversleuteling, en faciliteert het gebruik van anonimiseringsdiensten zoals het Whonix besturingssysteem.



https://planb.network/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

In plaats van te streven naar een ondoordringbaar systeem, richt Qubes OS zich op veerkracht: het kapselt schade in het geval van compromittering, waardoor het risico voor de rest van het systeem wordt beperkt. Door deze pragmatische aanpak is Qubes OS de keuze bij uitstek voor gebruikers met hoge beveiligingsbehoeften of die maximale controle over hun digitale leven willen behouden.



## Qubes OS installeren



Voordat je Qubes OS installeert, is het essentieel om ervoor te zorgen dat je hardware voldoet aan de minimale vereisten, omdat het systeem vertrouwt op virtualisatie om qubes te isoleren. De belangrijkste onderdelen om te controleren zijn :




- De **processor**: Een 64-bits processor die compatibel is met hardwarevirtualisatie (Intel VT-x of AMD-V).
- RAM: minimaal 8 GB is vereist, maar we raden 16 GB RAM of meer aan om meerdere qubes tegelijk te draaien.
- **Opslagruimte**: minimaal 36 GB, idealiter 128 GB op een SSD voor optimale prestaties.



Om Qubes OS te installeren, download je het officiële ISO-image van de Qubes OS [officiële site](https://www.qubes-os.org/downloads/). Het is essentieel om de integriteit van de ISO te controleren met behulp van de bijgeleverde GPG-handtekeningen om er zeker van te zijn dat er niet met het bestand geknoeid is en dat de download veilig is.



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Zodra de ISO is geverifieerd, moet je een opstartbaar installatiemedium maken, meestal een USB-stick. Om dit te doen, download en installeer je software zoals **Rufus** op Windows of **Etcher** op Windows, Linux of macOS. Met deze tools kun je de ISO naar de USB-stick kopiëren zodat deze opstartbaar is.



Voordat u met de installatie begint, moet u het **BIOS of UEFI** van uw computer configureren om **virtualisatie** in te schakelen en opstarten vanaf USB toe te staan. Afhankelijk van uw machinemodel, kan het nodig zijn om **Secure Boot** uit te schakelen, omdat Qubes OS mogelijk niet opstart met deze optie ingeschakeld.



![0_02](assets/fr/02.webp)



Zodra aan deze voorwaarden is voldaan, start u de computer opnieuw op en opent u het BIOS/UEFI door onmiddellijk op **Esc**, **Del**, **F9**, **F10**, **F11** of **F12** (afhankelijk van de fabrikant) te drukken. Selecteer in het opstartmenu de USB-sleutel als opstartapparaat om de Qubes OS-installatie te starten.



**Opstartscherm**


Bij het opstarten vanaf de USB-stick kom je direct in het **GRUB** menu, waar je de uit te voeren actie kunt kiezen. Selecteer "Install Qubes OS" met de pijltjestoetsen op je toetsenbord en druk op "Enter".



![0_03](assets/fr/03.webp)



**Taalkeuze** :



Wanneer de installatie start, is de eerste stap om **de taal** en **regionale variant** te kiezen die geschikt zijn voor jouw configuratie. Dit zorgt ervoor dat het systeem en de installatieopties correct worden weergegeven in de taal van je voorkeur.



![0_04](assets/fr/04.webp)



**Parameterconfiguratie** :



In dit stadium moet je een aantal Elements configureren voordat je de installatie op je machine start.



![0_05](assets/fr/05.webp)



**Keyboard layout** :



Klik op de optie **Keyboard** en selecteer vervolgens de **passende lay-out** voor uw computer. Als u uw keuze hebt gemaakt, klikt u op **Gebroken** om naar de volgende stap te gaan.



**Kies bestemming** :



Selecteer de optie "Installatiebestemming" om de schijf te kiezen waarop je Qubes OS wilt installeren. Standaard vindt de partitionering automatisch plaats, zodat u alle gegevens van de schijf kunt verwijderen en het systeem erop kunt installeren. Je kunt echter kiezen voor **Aangepast** of **Uitgebreid aanpassen** om een aangepaste partitionering uit te voeren. Klik vervolgens op "Gereed". Het systeem zal je vragen om een **wachtwoord** in te stellen, dat fungeert als een Layer beveiliging om je gegevens te versleutelen. Zorg ervoor dat je een complex en uniek wachtwoord kiest.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Selecteer datum- en tijdformaat** :


Klik op de optie Tijd en datum en selecteer vervolgens je geografische zone. Je kunt ook de tijdnotatie van je voorkeur kiezen: 24u of 12u.



![0_08](assets/fr/08.webp)



**Gebruikersaccount aanmaken** :


Klik op **Gebruiker aanmaken** om uw **eerste account** aan te maken, waarmee u kunt inloggen op Qubes OS.



![0_09](assets/fr/09.webp)



**Activeer root account** :


U kunt ook **de root-account** inschakelen door een apart wachtwoord in te stellen voor beheer.



![0_10](assets/fr/10.webp)



Zodra deze instellingen zijn gemaakt, klik je op **Start installatie** om het proces te starten.



![0_11](assets/fr/11.webp)



Wacht tot het **einde van de installatie** en klik dan op **herstart systeem** om de installatie af te ronden en Qubes OS te starten.



![0_12](assets/fr/12.webp)



**Aanvullende configuratie** :


Na het herstarten vraagt Qubes OS om de **standaard sjablonen en qubes configuratie** af te ronden. Voer het wachtwoord in dat is gedefinieerd om de schijf te coderen.



![0_13](assets/fr/13.webp)



Selecteer vervolgens de **TemplateVM** die u wilt installeren. Veel voorkomende opties zijn **Debian 12 Xfce**, **Fedora 41 Xfce** en **Whonix 17**, waarbij de laatste wordt aanbevolen voor gebruik dat **anonimiteit en netwerkbeveiliging** vereist. Je kunt ook de **standaard sjabloon** definiëren, die zal dienen als basis voor het maken van nieuwe **AppVM's**.



![0_14](assets/fr/14.webp)



In de sectie **Main configuration** kun je ervoor kiezen om automatisch essentiële systeemqubes aan te maken zoals **sys-net**, **sys-firewall** en **default DisposableVM**. Het is aan te raden om de optie **sys-firewall en sys-usb disposable** aan te zetten, om de blootstelling van het apparaat en het netwerk te beperken in het geval van een compromis. Je kunt ook standaard **AppVM's** aanmaken, zoals **personal**, **work**, **untrusted** en **vault**, om je activiteiten te organiseren op basis van hun vertrouwensniveau.



![0_15](assets/fr/15.webp)



Met Qubes OS kun je ook een **qube speciaal voor USB-apparaten** (sys-usb) maken en **Whonix Gateway en Workstation qubes** configureren om je communicatie via het Tor-netwerk te beveiligen. Voor gevorderde gebruikers kun je in het **Geavanceerde configuratie** gedeelte een **LVM thin pool** aanmaken om schijfruimte tussen qubes efficiënt te beheren.



Zodra al deze opties zijn geconfigureerd, klikt u op **Voltooien** en vervolgens op **Configuratie voltooien**. Wacht terwijl het systeem deze instellingen toepast. U wordt dan gevraagd om **in te loggen op uw gebruikersaccount** en uw Qubes OS-omgeving is klaar voor gebruik, veilig en goed geïsoleerd voor uw verschillende activiteiten.



![0_17](assets/fr/17.webp)



Je besturingssysteem is nu geïnstalleerd en klaar voor gebruik.



![0_18](assets/fr/18.webp)



## Maak een qube aan op uw systeem



Om een qube te maken, wordt het proces beheerd door het hulpprogramma **Qube Manager**, dat toegankelijk is vanuit het menu Start. Klik in het toolvenster op het pictogram **Kwbe maken** om een nieuw configuratievenster te openen. Voer eerst een naam in voor uw qube, zoals "perso-web" of "werk", om het gebruik ervan te identificeren.



Vervolgens selecteer je het **Type**, meestal **AppVM** voor routinetaken, of **DisposableVM** voor tijdelijk gebruik. Het is cruciaal om de **Template** te kiezen waarop je qube gebaseerd zal zijn, zoals "fedora-39" of "debian-12", aangezien dit het besturingssysteem en de software zal leveren. Je wijst ook de **NetVM** aan, de qube die verantwoordelijk is voor de internettoegang, standaard **sys-firewall**.



Tot slot, na het aanpassen van de opslaggrootte en RAM indien nodig, zal een eenvoudige klik op **OK** het creatieproces starten. Zodra het proces is voltooid, is je nieuwe qube zichtbaar in de lijst en klaar voor gebruik.



Kortom, Qubes OS is geen gewoon besturingssysteem, maar een geavanceerde beveiligingsoplossing die de architectuur van de pc heroverweegt. De aanpak, gebaseerd op compartimentering en isolatie door middel van virtualisatie, biedt ongeëvenaarde bescherming tegen de meest geavanceerde bedreigingen. Door de werkomgeving te segmenteren in gespecialiseerde qubes voor elke taak, zorgt het ervoor dat malware zich niet kan verspreiden en het hele systeem in gevaar kan brengen.



Of je nu veilig op het web moet surfen, gevoelige informatie moet beschermen of met verschillende vertrouwensniveaus moet werken, Qubes OS biedt een veerkrachtig, transparant raamwerk. Door goede praktijken toe te passen en optimaal gebruik te maken van de functies, beschikt u over een **digitaal fort** dat is aangepast aan moderne bedreigingen. Meer informatie over de bescherming van uw gegevens en privacy.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1