---
name: VirtualBox
description: Installer VirtualBox på Windows 11 og opprett din første VM
---
![cover](assets/cover.webp)



___



*Denne veiledningen er basert på originalt innhold av Florian Burnel publisert på [IT-Connect](https://www.it-connect.fr/). Lisens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Det kan ha blitt gjort endringer i den opprinnelige teksten



___




## I. Presentasjon



I denne veiledningen lærer vi hvordan du installerer VirtualBox på Windows 11 for å opprette virtuelle maskiner, enten det er for å kjøre Windows 10, Windows 11, Windows Server eller en Linux-distribusjon (Debian, Ubuntu, Kali Linux osv.).



Denne introduksjonsveiledningen til VirtualBox vil hjelpe deg å komme i gang med denne åpen kildekode-virtualiseringsløsningen som er utviklet av Oracle, og som er helt gratis. Senere vil det bli lagt ut andre veiledninger på nettet for å ta deg dypere inn i emnet.



Når det gjelder virtualisering av en arbeidsstasjon, enten det er for testformål som en del av et prosjekt eller i løpet av IT-studiene, er VirtualBox helt klart en god løsning. Det er også et alternativ til andre løsninger som Hyper-V, som er integrert i Windows 10 og Windows 11 (samt Windows Server), og VMware Workstation (mot betaling) / VMware Workstation Player (gratis for personlig bruk).



Min konfigurasjon: **en Windows 11-arbeidsstasjon der jeg skal installere VirtualBox**, men du kan installere VirtualBox på Windows 10 (eller en eldre versjon), så vel som på Linux. Når det gjelder virtuelle maskiner, støtter VirtualBox et bredt spekter av systemer, inkludert Windows (f.eks. Windows 10, Windows 11, Windows Server 2022 osv.), Linux (Debian, Rocky Linux, Ubuntu, Fedora osv.), BSD (PfSense) og macOS.



## II. Last ned VirtualBox for Windows 11



For å laste ned VirtualBox for installasjon på en Windows-maskin, finnes det bare én god Address: [official VirtualBox website] (https://www.virtualbox.org/wiki/Downloads) i "**Downloads**"-delen. Bare klikk på "Windows hosts" for å starte nedlastingen av denne kjørbare filen, som er litt over 100 MB stor.



![Image](assets/fr/025.webp)



## III. Installere VirtualBox på Windows 11



### A. Installere VirtualBox



Det er enkelt å installere VirtualBox**, og prosessen er den samme for alle Windows-versjoner. Start med å starte den kjørbare filen for VirtualBox som du nettopp har lastet ned, og klikk deretter på "**Neste**".



![Image](assets/fr/026.webp)



Denne installasjonen kan tilpasses, men jeg anbefaler at du installerer alle funksjonene: som er tilfelle med standardvalget. På bildet nedenfor kan du se forskjellige Elements, inkludert :





- VirtualBox USB-støtte** for å aktivere VirtualBox til å støtte USB-enheter
- VirtualBox Bridged Network** for å integrere nettverksstøtte i "Bridge"-modus (den virtuelle maskinen kan koble seg direkte til ditt lokale nettverk)
- VirtualBox Host-Only Network** for å integrere nettverksstøtte i "Host-Only"-modus (den virtuelle maskinen kan bare kommunisere med den fysiske Windows 11-verten og andre virtuelle maskiner i denne modusen)



Klikk på "**Neste**" for å fortsette.



![Image](assets/fr/001.webp)



Klikk på "**Yes**", og vær oppmerksom på at **nettverket vil bli avbrutt et øyeblikk på Windows 11-maskinen**, mens VirtualBox utfører nettverksendringer for å støtte ulike nettverkstyper, inkludert Bridge-modus.



![Image](assets/fr/002.webp)



Når du har bekreftet, starter installasjonen... En melding "**Vil du installere denne enhetsprogramvaren?"** vises. Kryss av for "**Stoler alltid på programvare fra Oracle Corporation**" og klikk på "**Installer**". VirtualBox trenger faktisk å installere flere drivere på datamaskinen din.



![Image](assets/fr/003.webp)



Installasjonen er nå fullført! Merk av for "**Start Oracle VM VirtualBox 6.1.34 etter installasjon**" og klikk på "**Klikk**" for å starte programvaren.



![Image](assets/fr/004.webp)



### B. Legg til utvidelsespakken



På det offisielle VirtualBox-nettstedet (se forrige lenke) kan du fortsatt laste ned en offisiell utvidelsespakke, tilgjengelig under "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" -delen ved å klikke på lenken "**Alle støttede plattformer**". Denne pakken gjør det mulig å legge til flere funksjoner i VirtualBox: det er ikke obligatorisk å legge den til, men den kan være nyttig! Den inkluderer for eksempel støtte for USB 3.0 i virtuelle maskiner, støtte for webkamera og diskkryptering.



Åpne VirtualBox, klikk på "**File**" og deretter på "**Settings**" i menyen.



![Image](assets/fr/005.webp)



Klikk på "**Extensions**" til venstre (1), og deretter på "**+**"-knappen til høyre (2) for å **laste inn VirtualBox**-utvidelsespakken du nettopp har lastet ned (3).



![Image](assets/fr/006.webp)



Bekreft ved å klikke på knappen "**Installasjon**".



![Image](assets/fr/007.webp)



Klikk på "**OK**": Den offisielle utvidelsespakken er nå installert på VirtualBox-forekomsten din!



![Image](assets/fr/008.webp)



La oss gå videre til opprettelsen av vår første virtuelle maskin.



## IV. Opprette din første VirtualBox VM



For å opprette en ny virtuell maskin i VirtualBox klikker du ganske enkelt på knappen "**Ny**" for å starte veiviseren for oppretting av VM. Siden dette er første gang du starter VirtualBox, vil jeg gjerne gi deg noen flere detaljer om Interface og de andre knappene.





- Innstillinger**: generell VirtualBox-konfigurasjon (standard VM-mappe, oppdateringshåndtering, språk, NAT-nettverk, utvidelser osv.)
- Import**: importer en virtuell appliance i OVF-format
- Eksporter**: eksporter en eksisterende virtuell maskin i OVF-format for å opprette en virtuell appliance
- Legg til**: legg til en eksisterende virtuell maskin i VirtualBox-inventaret, i standard VirtualBox-format (.vbox) eller XML-format



Til venstre gir delen "**Tools**" tilgang til **avanserte funksjoner, særlig for å administrere det virtuelle nettverket, men også for å administrere VM-lagring**. Under "**Verktøy**" legges de virtuelle maskinene dine til senere.



![Image](assets/fr/009.webp)



### A. Prosess for opprettelse av VM



**Som en påminnelse: VirtualBox støtter en rekke operativsystemer, inkludert Windows, Linux og BSD. I dette eksemplet skal jeg opprette en virtuell maskin for Windows 11. Flere felt må fylles ut:





- Navn**: navnet på den virtuelle maskinen (dette er navnet som vises i VirtualBox)
- Maskinmappe**: hvor den virtuelle maskinen skal lagres, vel vitende om at en undermappe med VM-navnet vil bli opprettet på denne plasseringen
- Type**: typen operativsystem, avhengig av hvilket operativsystem du ønsker å installere
- Version**: versjonen av systemet du ønsker å installere, i dette tilfellet Windows 11, altså "**Windows11_64**"



Klikk på "**Neste**" for å fortsette.



![Image](assets/fr/010.webp)



Avhengig av operativsystemet du valgte i forrige trinn, kommer **VirtualBox med anbefalinger om hvilke ressurser som skal allokeres til den virtuelle maskinen**. Her snakker vi om RAM-minnet du ønsker å allokere til VM-en. La oss anta 4 GB, fordi dette faktisk er anbefalt for Windows 11, men hvis du har lite ressurser, kan du angi 2 GB i stedet. **Fortsett



**Merk**: Ressursene som er allokert til den virtuelle maskinen, kan endres senere.



![Image](assets/fr/011.webp)



Når det gjelder den virtuelle Hard-disken, starter vi fra bunnen av, så vi må velge "**Opprett virtuell Hard-disk nå**" slik at den virtuelle VM-en har lagringsplass til å installere operativsystemet og lagre data. Klikk på "**Opprett**".



![Image](assets/fr/012.webp)



VirtualBox støtter tre ulike formater for virtuelle Hard-disker, noe som er en stor forskjell sammenlignet med andre løsninger som VMware og Hyper-V. Det er tre formater å velge mellom:





- VDI**, det offisielle VirtualBox-formatet
- VHD**, som er det offisielle Hyper-V-formatet, selv om det nye VHDX-formatet brukes oftere i disse dager
- VMDX** er det offisielle VMware-formatet for både VMware Workstation og VMware ESXi



Hvis du vil opprette en virtuell maskin som bare skal brukes på denne VirtualBox-forekomsten, velger du "**VDI**". Hvis den virtuelle Hard-disken derimot skal kobles til en Hyper-V-vert på et senere tidspunkt, kan det være en god idé å starte med VHD-formatet for å unngå å måtte konvertere den. Klikk på "**Neste**".



![Image](assets/fr/013.webp)



**Den virtuelle disken kan ha enten dynamisk eller fast størrelse**. Når den er dynamisk, vil filen som representerer **den virtuelle disken (her en .vdi-fil) vokse etter hvert som data skrives til disken** til den når sin maksimale størrelse, men den krymper ikke hvis data slettes. Når den derimot har fast størrelse, blir **den totale lagringsplassen allokert umiddelbart (og dermed reservert)**, noe som gir litt høyere ytelse, men som tar lengre tid når den virtuelle disken først opprettes.



Personlig anser jeg "**Dynamisk allokert**"-modusen som tilstrekkelig for å teste virtuelle maskiner med VirtualBox.



![Image](assets/fr/014.webp)



**Neste trinn er å angi størrelsen på den virtuelle disken**, og husk at disken som standard vil bli lagret i VM-katalogen (dette kan endres på dette stadiet). Jeg har angitt en størrelse på 64 GB for å oppfylle kravene i Windows 11, men også her kan du velge en mindre størrelse. Klikk på "**Create**" for å opprette VM-en!



![Image](assets/fr/015.webp)



På dette tidspunktet er den virtuelle maskinen i lageret vårt, den er konfigurert, men operativsystemet er ikke installert. Vi må fullføre konfigurasjonen av den virtuelle maskinen før vi starter den opp.



### B. Tilordne et ISO-bilde til en VirtualBox VM



For å installere Windows 11, eller et hvilket som helst annet system, trenger vi installasjonskilder. I de fleste tilfeller bruker vi et diskbilde i ISO-format for å installere et operativsystem. **Det er nødvendig å laste inn ISO-bildet av Windows 11 i den virtuelle DVD-stasjonen i den virtuelle VM-en



Klikk på den virtuelle maskinen i VirtualBox-inventaret (1), og klikk deretter på knappen "**Configuration**" (2), som gir tilgang til den generelle konfigurasjonen av denne virtuelle maskinen. Denne menyen brukes til å administrere ressurser (f.eks. øke RAM, konfigurere CPU osv.). Klikk på "**Storage**" til venstre (3), på DVD-stasjonen der det står "**Empty**" for øyeblikket (4), og klikk deretter på det DVD-formede ikonet (5) og "**Choose a disk file**".



![Image](assets/fr/016.webp)



Velg ISO-bildet av operativsystemet du vil installere, og klikk deretter på OK. Dette er hva jeg får opp:



![Image](assets/fr/017.webp)



Bli i "**Konfigurasjon**"-delen av VM-en, jeg har fortsatt et par ting å forklare.



### C. VM-nettverkstilkobling



Gå til "**Nettverk**"-seksjonen til venstre. Her kan du administrere den virtuelle maskinens nettverk: antall virtuelle nettverksgrensesnitt (opptil 4 per VM), MAC Address og nettverkstilgangsmodus (NAT, brotilgang, internt nettverk osv.). **Hvis du vil at den virtuelle maskinen skal ha tilgang til Internett, velger du "NAT" eller "Bridge Access"**, men denne andre modusen krever at en DHCP-server er aktiv på nettverket ditt, ellers må du konfigurere en IP Address manuelt.



Merk: Jeg kommer tilbake til nettverksdelen i mer detalj i en egen artikkel.



![Image](assets/fr/018.webp)



### D. Antall virtuelle prosessorer



I likhet med en fysisk datamaskin trenger en virtuell maskin RAM, en Hard-disk og en prosessor for å fungere. Da vi opprettet den virtuelle maskinen, la du kanskje merke til at veiviseren ikke inkluderte prosessorkonfigurasjonen. Denne kan imidlertid konfigureres når som helst via fanen "**System**" og deretter "**Processor**", der du kan velge antall virtuelle prosessorer.



Merk: Alternativet "**Enable VT-x/AMD-v nested**" er påkrevd for nestet virtualisering.



I mitt tilfelle har den virtuelle maskinen to virtuelle prosessorer:



![Image](assets/fr/019.webp)



**Nøl ikke med å ta en titt på de andre delene av konfigurasjonsmenyen.



### E. Første oppstart og OS-installasjon



For å starte en virtuell maskin velger du den i inventarlisten og klikker på "**Start**"-knappen. Et nytt vindu åpnes, som gir en visuell oversikt over den virtuelle maskinen.



![Image](assets/fr/020.webp)



Ouch, jeg får en stygg feil, og den virtuelle maskinen min vil ikke starte! Feilen er "Innlogging mislyktes for virtuell maskin ..." med følgende detaljer:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



Dette er faktisk normalt fordi **virtualiseringsfunksjonen ikke er aktivert på min datamaskin**! For å løse dette problemet må du starte datamaskinen på nytt for å få tilgang til BIOS og aktivere virtualisering.



![Image](assets/fr/021.webp)



Uten å vente starter jeg datamaskinen på nytt og **trykker på "SUPPR"-tasten for å få tilgang til BIOS** (tasten kan variere avhengig av maskinen, og kan for eksempel være F2) på ASUS-hovedkortet mitt. For å aktivere virtualisering må "SVM Mode" være aktivert i mitt tilfelle. Også her kan navnet endres fra ett hovedkort til et annet, fra en produsent til en annen. Se etter en funksjon som refererer til **AMD-V** (for en AMD CPU) eller **Intel VT-x** (for en Intel CPU).



![Image](assets/fr/022.webp)



Når dette er gjort, lagrer du endringen og starter den fysiske maskinen på nytt ... Denne gangen kan **VirtualBox starte den virtuelle maskinen** og laste inn Windows ISO-bildet for å installere operativsystemet 🙂 🙂 ..



![Image](assets/fr/023.webp)



På vår fysiske Windows 11-vert, der VirtualBox er installert, kan vi se at mappen for den virtuelle Windows 11-maskinen inneholder ulike filer.





- VBOX**-filen (i XML-format) som tilsvarer VM-konfigurasjonen (RAM, CPU osv.)
- VBOX-PREV**-filen er en sikkerhetskopi av den forrige konfigurasjonen
- VDI**-filen tilsvarer den virtuelle Hard-disken i dynamisk modus, så den er for øyeblikket bare 13 GB, mens den maksimale størrelsen er 64 GB
- NVRAM**-filen inneholder BIOS-tilstanden til den virtuelle maskinen, noe som tilsvarer det ikke-flyktige minnet til en fysisk maskin



![Image](assets/fr/024.webp)



## V. Konklusjon



**VirtualBox er nå oppe og går på vår fysiske Windows 11-maskin! Nå gjenstår det bare å dra nytte av det og opprette virtuelle maskiner** Jeg kommer tilbake til installering av Windows 11 i en VirtualBox VM i en annen artikkel. For Windows 10, Windows Server eller en Linux-distribusjon (Ubuntu, Debian osv.) er det bare å la oss veilede deg!