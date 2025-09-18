---
name: Elementary OS
description: Den ideelle erstatningen for Windows og MacOS
---

![cover](assets/cover.webp)



Elementary OS er et Ubuntu-basert operativsystem som er utviklet for å være enkelt, raskt og stabilt for mange dagligdagse bruksområder. Det representerer et balansert Linux-alternativ til MacOS og Windows. Det flytende, intuitive og oversiktlige grafiske Interface gjør det enkelt å lære, selv for nybegynnere. Det fokuserer også på ergonomi, sikkerhet og ytelse.



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

## Hvorfor velge Elementary OS





- **Enkelhet og brukervennlighet**: Elementary OS' grafiske Interface ligger midt mellom MacOs og Windows. Dette gjør det lett å ta i bruk, selv for uerfarne brukere.





- **Sikkerhet**: I likhet med de fleste Linux-distribusjoner har Elementary OS et høyt sikkerhetsnivå. Regelmessige oppdateringer, rettighetsstyring og fraværet av vanlige virus gjør det til et pålitelig system.





- **Hastighet**: Elementary OS er en lettvektsdistribusjon. Den krever få ressurser, noe som gjør den rask og egnet for datamaskiner med beskjedne konfigurasjoner.





- **Gratis**: Systemet er helt gratis. Når du laster det ned, kan du imidlertid gi en donasjon for å støtte utviklerne.





- **Aktivt fellesskap**: Fellesskapet rundt Elementary OS er mangfoldig og lydhørt. Hvis du støter på problemer, kan du enkelt finne hjelp i forumet eller på sosiale nettverk.



## Installasjon og konfigurasjon


### Forutsetninger for maskinvare



Før du starter installasjonen, må du forsikre deg om at du har følgende utstyr:





- En **USB-nøkkel** på minst 12 GB
- **RAM-minne** på minst 4 GB
- En **Hard-disk på 20 GB** eller mer for komfortabel bruk



## Last ned ISO-bilde



Gå til operativsystemets offisielle nettside [elementary] (https://elementary.io/) og velg et beløp til støtte for prosjektet. Dette trinnet er valgfritt.


Hvis du ønsker å laste ned ISO-bildet gratis, skriver du inn 0 i feltet **"Annet"** og starter nedlastingen av systemets ISO-bilde.



![0_01](assets/fr/01.webp)



## Opprette en oppstartbar USB-nøkkel



Når du har lastet ned ISO-bildet, må du gjøre det oppstartbart på en USB-nøkkel for å fortsette med installasjonen.



Last ned programvare som [Balena Etcher] (https://etcher.balena.io/) eller et lignende verktøy, og start deretter programvaren.


Velg det tidligere nedlastede **Elementary OS** ISO-bildet, og angi USB-nøkkelen som mål.



Klikk på **flash**-knappen for å starte prosessen, og vent til prosessen er fullført før du tar ut USB-nøkkelen.



![0_02](assets/fr/02.webp)



## Nøkkeloppstart og BIOS-tilgang



Slå av datamaskinen du ønsker å installere Elementary OS på, og koble deretter til USB-nøkkelen.


Når datamaskinen starter, går du inn i BIOS (`ESC`, `F9` eller `F11` avhengig av merke) og velger USB-nøkkelen som oppstartsenhet, og trykker deretter på `Enter` for å starte oppstartsprosessen.



## Installere Elementary OS



Installasjonen starter automatisk hvis USB-nøkkelen er riktig konfigurert.



### Valg av språk



Velg språket du ønsker å installere systemet på. Du kan også velge en regional variant.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



### Tastaturoppsett



Velg det oppsettet som passer til tastaturet ditt. Det finnes et felt der du kan kontrollere at tastene produserer de riktige tegnene.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)



### Testmodus



Elementary OS lar deg teste systemet før du installerer det. I denne modusen kan du utforske Interface uten å endre noe på Hard-disken.



### Starter installasjonen





- Klikk på **"Slett disk og installer"** for å installere direkte på hele disken.
- Klikk på **"Tilpasset installasjon"** hvis du ønsker å administrere partisjonene manuelt.



![0_07](assets/fr/07.webp)



### Valg av plate



Velg disken som Elementary OS skal installeres på, og klikk deretter på Fortsett-knappen.



![0_08](assets/fr/08.webp)



### Diskkryptering



Et alternativ lar deg kryptere disken for å **sikre dataene dine**. Du må angi et sterkt passord for å aktivere denne beskyttelsen. Det er imidlertid valgfritt.



![0_09](assets/fr/09.webp)



![0_10](assets/fr/10.webp)



### Starter installasjonen



Før du starter installasjonen, kan du godkjenne automatisk installasjon av ekstra maskinvaredrivere, avhengig av maskinens kompatibilitet.





- Klikk på "Slett og installer" for å starte installasjonen.
- Vent til prosessen er fullført.



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



### Start på nytt



Når du er ferdig, klikker du på **enter**-knappen for å starte på nytt, og deretter fjerner du USB-nøkkelen på et passende tidspunkt for å unngå at installasjonen starter på nytt.



![0_13](assets/fr/13.webp)



## Konfigurasjon etter installasjon



Etter omstart er det nødvendig med noen få ekstra trinn.



![0_14](assets/fr/14.webp)



### Valg av språk



Bekreft eller endre systemspråket ved pålogging.



![0_15](assets/fr/15.webp)



### Tastaturoppsett



Kontroller at tastaturoppsettet er det du ønsker.



![0_16](assets/fr/05.webp)



### Opprette en brukerkonto



Knytt en brukerkonto til operativsystemet ved å definere et brukernavn og deretter sikre tilgangen til dataene dine med et alfanumerisk passord på minst 20 tegn og symboler.



![0_17](assets/fr/17.webp)



### Første tilkobling



Når du logger på for første gang, lar Elementary OS deg tilpasse miljøet ditt med noen få grunnleggende innstillinger.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



## Oppdatering av systemet



Før langvarig bruk er det viktig å oppdatere systemet med de nyeste oppdateringene.


### Alternativ 1: Oppdatering via Interface-grafikk



Gå inn i **AppCenter** og klikk på oppdateringsikonet øverst i høyre hjørne. Vent til oppdateringene vises på listen, og klikk deretter på **"Oppdater alle"** for å starte installasjonen.



![0_20](assets/fr/20.webp)



![0_21](assets/fr/21.webp)



### Alternativ 2: Oppdatering via terminal



Du kan også utføre oppdateringen fra kommandolinjen via terminalen: et anbefalt alternativ på grunn av nøyaktigheten.



```shell
sudo apt update
```



```shell
sudo apt full-upgrade
```



For de første oppdateringene krever operativsystemet brukerpassordet ditt og bekreftelse for å oppdatere programvarepakker, selv i Elementary-kjernen.



## Konfigurasjon av arbeidsmiljøet



Elementary OS inneholder bare de viktigste verktøyene. For å tilpasse miljøet til dine behov, spesielt hvis du er en utvikler, anbefaler vi at du installerer flere verktøy.





- Du kan legge til nyttige avhengigheter med følgende kommando (tilpasses dine behov):



```shell
sudo apt update && sudo apt install -y git python3 python3-pip build-essential wget curl zsh make snapd && sudo snap install code --classic
```



Denne kommandoen installerer **Git**, **Python 3**, **pip**, **kompilatorverktøy**, **wget**, **curl**, **zsh**, **make**, **snapd** og **vscode** for å forberede et grunnleggende utviklingsmiljø.



Elementary OS er nå oppe og kjører på maskinen din. Filosofien om enkelhet, letthet og eleganse gjør det til et utmerket valg for både personlig og profesjonell bruk. Du får et stabilt, flytende og oversiktlig system som er klart til å tilpasses etter dine preferanser. Enten det gjelder utvikling, kontorbruk eller daglig surfing, er alt på plass for å skape et effektivt, intuitivt og behagelig arbeidsmiljø. Ta også en titt på veiledningen vår om Fedora, en like enkel, robust og modulær Linux-distribusjon.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0