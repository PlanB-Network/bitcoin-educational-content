---
name: DietPi
description: Lichtgewicht besturingssysteem geoptimaliseerd voor onderpresterende machines. Met een voorkeur voor zelf-hosting
---

![cover](assets/cover.webp)



In niet-technische kringen zijn merken als `Odroid`, `Raspberry Pi`, `Orange Pi` of `Radxa` weinig bekend. Maar je hoeft alleen maar in technische kringen te kijken om te ontdekken dat **SBC** computers - gebouwd op een enkel moederbord, vaak microscopisch klein vergeleken met algemeen gebruikte computers - onmisbaar zijn geworden als ondersteuning voor elk persoonlijk project.



Dit zijn computers die in veel verschillende modellen worden geproduceerd. Ze hosten bij voorkeur Linux-distributies, vaak aangepast om soepel te draaien op deze ondergemotoriseerde machines.



**DietPi is geen uitzondering**: het is een Debian-gebaseerd besturingssysteem, geoptimaliseerd om zo licht mogelijk te zijn en zelfs de minst presterende `SBC` erg snel te maken. Overgeschakeld van Debian12 Bookworm naar Debian13 Trixie net toen deze tutorial werd geschreven, ondersteunt het nu ook open source `RISC-V` processor-gebaseerde SBCs. DietPi is een aangename ontdekking die verdere studie verdient.



## Sterke punten



Dit is niet het "gebruikelijke duplicaat" van Debian voor kleine Raspberry-achtige borden. DietPi is dat wel:




- Geoptimaliseerd voor snelheid en lichtheid**: een [vergelijking met andere Debian distributies voor SBC](https://dietpi.com/blog/?p=888), DietPi is lichter in alles. Het DietPi ISO image weegt minder dan 1 GB, veruit het kleinste onder de distributies die gewijd zijn aan oudere modellen van Raspberry of Orange PI (bijvoorbeeld). De vraag naar RAM- en CPU-bronnen is erg laag, zodat het altijd het beste uit boards haalt, zelfs oudere.
- Ingebouwde automatiseringen en installateurs**: Een reeks speciale commando's helpt gebruikers systeembronnen te controleren en taken te automatiseren om programma's te installeren en te starten, versies bij te werken, back-ups te maken en alle logs te controleren.
- Een sterke, experimenteer-georiënteerde gemeenschap**: [tutorials](https://dietpi.com/forum/c/community-tutorials/8) en projecten van de DietPi community, zijn ideaal om inspiratie op te doen voor software die je met één klik kunt installeren, dankzij DietPi.



**Het was nog nooit zo makkelijk om alles uit je SBC te halen**.



## Automatiseringen voor zelf hosten


Wil je experimenteren met je eigen server om geavanceerde netwerkoplossingen te draaien, of tools om je Bitcoin expertise te ontwikkelen? DietPi kan de oplossing zijn die je zoekt. Hoewel veel mensen weten hoe ze hun eigen infrastructuur moeten beheren en perfect geconfigureerde en beveiligde servers moeten draaien, is DietPi een geschikte stap voor diegenen die vanaf nul willen beginnen.



In plaats van het handmatig uitvoeren van alle complexe taken die zo'n taak vereist, stelt DietPi u in staat om ze te bouwen met een `wizard` en een eigen opdrachtregel. Hier kunt u experimenteren met uw eigen persoonlijke cloud, _smart home_ apparaatbeheer, geautomatiseerde back-ups en crontab, maar ook met meer geavanceerde oplossingen.



![img](assets/en/01.webp)



## Installatie



### Downloaden



DietPi biedt een ontelbare set ISO-images om het besturingssysteem op veel verschillende apparaten te branden. Sommige worden alleen ondersteund: de ISO voor Raspberry PI5 wordt bijvoorbeeld nog getest, maar je kunt zeker een vinden die geschikt is voor jouw bord.



Voor deze handleiding koos ik ervoor om het op een thin client te installeren, dus ging de keuze naar _PC/VM_ en vervolgens naar _Native PC_. Er zijn twee ISO images voor deze apparaten, die verschillen in de generatie van de bootloader. De machine die in de tutorial wordt gebruikt is vrij oud, dus de keuze viel op de _BIOS/CSM_ versie. Als je een nieuwere machine hebt, kan de juiste versie de `UEFI` zijn.



![img](assets/en/02.webp)



Je komt op de pagina met de `image of the installer`, de `sha256` en de `Signatures`.



![img](assets/en/03.webp)



Maak een map aan in de `home` van je dagelijkse computer, zodat je de benodigde bestanden kunt downloaden met `wget`.



![img](assets/en/04.webp)



De publieke sleutel van de ontwikkelaar vereiste een minimum aan onderzoek, maar je kunt hem vinden op deze link: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Controleer de inhoud van de map met `ls -la` en importeer de MichaIng sleutel in je sleutelring met `gpg --import`.



### Verificatie en flash



Tot slot het gedeelte dat ik het meest aanbeveel: controleer de authenticiteit van het besturingssysteem dat je hebt gedownload en dat je op het punt staat te installeren op je SBC.



![img](assets/en/06.webp)



Als je ook het `Goede handtekening` resultaat hebt en dezelfde Hash controle met het sha256sum commando, kun je doorgaan met het flashen van de ISO naar een USB stick. Gebruik hiervoor apps zoals Whale Etcher.



![img](assets/en/07.webp)



## DietPi installatie



![img](assets/en/09.webp)



Breng de flash drive over naar het apparaat dat DietPi gaat hosten en begin met de installatie van het lime Green besturingssysteem. In deze oefening gebruiken we een thin client met 16 GB RAM, een 128 GB SSD voor het besturingssysteem en een tweede 1 TB dataschijf. De installatie duurde minder dan 30 minuten, maar als je bijvoorbeeld een Raspberry gebruikt, kunnen de bronnen minder zijn en langer duren. Je krijgt de voortgang te zien tijdens de installatie.



![img](assets/en/08.webp)



Omdat DietPi ontworpen is voor Raspberries en dergelijke, is de ware aard van de installatie de zogenaamde `headless` installatie, zonder grafische omgeving en met native `shsh' toegang. In de handleiding zie je in plaats daarvan een grafische omgeving, LXDE om precies te zijn.



Tijdens deze stap wordt u ook gevraagd om te kiezen welke webbrowser u standaard wilt gebruiken, tussen Chromium en Firefox. Beide werken goed; er zijn geen specifieke contra-indicaties voor een van beide, behalve uw persoonlijke voorkeur.



Tegen het einde kan het installatieprogramma je vragen of je al programma's wilt installeren, maar hier **raad ik je aan om niets vooraf te laden**. Je moet weten dat na deze stap om veiligheidsredenen wordt gevraagd om de standaard wachtwoorden van de twee gebruikers te wijzigen. Het belangrijkste is dat je het `Global Software Password (GSP)`** moet instellen, waarmee je op een gecontroleerde manier toegang krijgt tot de verschillende software. **Als je software downloadt tijdens de installatie van het OS, zonder het `GSP` in te stellen, zullen ze vrijwel ontoegankelijk blijven**. Je zult ze moeten verwijderen en opnieuw installeren nadat je het `Global Software Password` hebt ingesteld: dus **zet er niets in om dubbel werk te voorkomen**. (Het ongemak is waarschijnlijk, niet 100% zeker).



De installatie eindigt met een verzoek om DietPi-Survey te activeren, een geautomatiseerde gegevensverzamelingsdienst die wordt gebruikt om de ontwikkeling van het besturingssysteem te ondersteunen. Volgens de website wordt de gegevensverzameling geactiveerd wanneer je software downloadt van de automatisering die DietPi biedt, of wanneer je een upgrade uitvoert naar de volgende versie. Iedereen heeft de optie om in (_Opt IN_) of uit (_Opt OUT_) te stappen.



![img](assets/en/23.webp)



Na voltooiing van de installatie en de daaropvolgende herstart, verschijnt DietPi op het scherm zoals je het instelt. Voor de tutorial koos ik, zoals gezegd, de `LXDE` grafische omgeving. Op het bureaublad vond ik de snelkoppeling om `htop` te starten en de terminal te openen.



![img](assets/en/10.webp)



### "Gereedschap" van besturingssysteem



Vergeet de meeste programma's die je gebruikt op je Linux-distributie - DietPi is zo geoptimaliseerd dat je er al heel wat hebt weggelaten. In principe zou je veel commando's handmatig moeten installeren, maar als je het gewoon uitprobeert, weersta dan de verleiding en probeer de automatiseringen van DietPi uit.



Het is zeker de terminal die het eerste nuttige hulpmiddel is om aan de slag te gaan met je nieuwe besturingssysteem, en het opent automatisch elke keer dat je het aanzet.



![img](assets/en/11.webp)



Op het terminalscherm vind je een reeks commando's voorafgegaan door `dietpi-` die de [tools](https://dietpi.com/docs/dietpi_tools/) van dit besturingssysteem voorstellen:




- `dietpi-launcher`: voor toegang tot het besturingssysteem, bestandsbeheer, enz
- `dietpi-Software`: dit is het hulpprogramma waarmee je alle software kunt installeren die al beschikbaar is in de suite
- `dietpi-config`: om toegang te krijgen tot systeemconfiguraties, zelfs de meest geavanceerde.



![img](assets/en/14.webp)



### Back-up



Het maken van een back-up van een server is een routine die de systeembeheerder vanaf de eerste opstart moet voorzien.



Met DietPi is er het `dietpi-Backup` commando, waarvan ik je aanraad om het te verkennen om de ideale oplossing te vinden: het stelt je in staat om een regelmatige back-up in te stellen, incrementeel of niet, afhankelijk van de gebruikte applicaties, en alle opties om de routine aan te passen.



![img](assets/en/22.webp)



Selecteer de bestemming van de back-up, bijvoorbeeld een andere schijf, door `dietpi-Drive_Manager` te starten om de bestemmingsschijf te koppelen en te gebruiken voor deze functie.



## Configuratie



Zelf hosten is een aan te raden ervaring voor iedereen, of je nu nieuwsgierig bent of gewoon enthousiast. Het opzetten en configureren van een server brengt echter een aantal niet onaanzienlijke technologische uitdagingen met zich mee. Dit is waar **de eenvoud van DietPi** om de hoek komt kijken, zodat je in een paar eenvoudige stappen een systeem kunt configureren dat aan je behoeften voldoet.



![img](assets/en/24.webp)



Basis- en geavanceerde instellingen, allemaal binnen handbereik in de ene Interface die beschikbaar is met de opdracht:



``dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-software


```