---
name: PureOS
description: Linux-distribusjonen som gir deg kontroll over ditt digitale liv.
---

![cover](assets/cover.webp)



Beskyttelse av personopplysninger i den digitale tidsalderen er en topp prioritet for alle Internett-brukere. Bedrifter, organisasjoner og til og med operativsystemer er nyttige informasjonskilder for å definere profilen og livsstilen din. Å velge riktig operativsystem er det første steget mot å styrke personvernet ditt på nettet. I denne veiledningen tar vi en titt på PureOS, en Linux-distribusjon med fokus på personvern.



https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## Kom i gang med PureOS



PureOS er et Debian-basert operativsystem utviklet av Purism. PureOS passer både for IT-profesjonelle og brukere som er ute etter en enkel og brukervennlig distribusjon. Det er unikt ved at det er *fri programvare*, og fokuserer på beskyttelse av brukernes personopplysninger ved å sette opp et rammeverk basert på personvernet, friheten, sikkerheten og stabiliteten som Debian tilbyr.



### Hvorfor velge PureOS?





- Enkel, intuitiv Interface**: GNOME tilbyr et oversiktlig Interface-skrivebord som er designet for å være enkelt å bruke, selv for folk som ikke er komfortable med kommandolinjen.





- Gratis**: Som de fleste Linux-distribusjoner er PureOS helt gratis å bruke. Et månedlig abonnement er imidlertid tilgjengelig for å støtte utviklere.





- Sikkerhet og stabilitet**: PureOS' arkitektur og driftsmodus gjør det til en svært sikker distribusjon som garanterer databeskyttelse og systemstabilitet.





- Dokumentasjon og et aktivt fellesskap**: PureOS har tydelig, tilgjengelig dokumentasjon og et engasjert, lydhørt fellesskap, noe som gjør det enkelt å løse problemer og lære systemet trinn for trinn.



## Installasjon og konfigurasjon



Installering og konfigurering av PureOS på datamaskinen din krever følgende minimalistiske funksjoner:




- En USB-nøkkel på minst 8 GB for å flashe systemet.
- 4 GB RAM.
- 30 GB ledig plass på Hard-disken.



Gå til [PureOS offisielle nettsted] (https://pureos.net/) og last deretter ned ISO-bildet av operativsystemet i henhold til maskinens arkitektur.



For å starte PureOS-installasjonen må du opprette en oppstartbar USB-nøkkel ved hjelp av flash-programvare som [Balena Etcher] (https://www.balena.io/etcher).



I løpet av tre enkle trinn får du en USB-pinne med PureOS-operativsystemet.





- Koble til USB-nøkkelen og kjør den nedlastede Balena-programvaren.
- Velg deretter PureOS ISO-bildet
- Velg USB-nøkkelen som utdataenhet, klikk deretter på **Flash**-knappen og vent til prosessen er ferdig.



![0_01](assets/fr/01.webp)



Når USB-nøkkelen er startet opp, starter du datamaskinen du ønsker å installere PureOS på, på nytt.



Når du starter opp, åpner du BIOS ved å trykke på tastene `ESC`, `F9` eller `F11`, avhengig av hvilken maskin du har. Velg USB-nøkkelen som oppstartsenhet, og trykk deretter på `ENTER` for å bekrefte.



### Oppstartsskjerm



PureOS tilbyr flere alternativer for å starte opp operativsystemet. Velg alternativet **Test or Install PureOS** for å starte installasjonen av operativsystemet.



![0_02](assets/fr/02.webp)



Angi hvilket språk og tastaturoppsett du vil bruke på datamaskinen.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



Tillat eller nekt tilgang til din **geografiske plassering** til applikasjoner for personlige anbefalinger basert på området ditt.



![0_05](assets/fr/05.webp)



Du kan koble deg til din eksisterende **NextCloud**-konto for å hente data knyttet til kontorpakken du bruker på et annet system.



![0_06](assets/fr/06.webp)



Du får en veiledning, men du kan lukke vinduet hvis du ønsker å hoppe over dette trinnet.



![0_08](assets/fr/08.webp)



### Starter installasjonen



Klikk på **Activities**-menyen og utforsk programmene og verktøyene som er forhåndsinstallert på systemet. Klikk på **Install PureOS** for å starte installasjonen



![0_09](assets/fr/09.webp)



Still inn systemspråket og tastaturoppsettet etter behov, og konfigurer deretter Hard-diskpartisjoneringsmodus.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



Du har to alternativer for partisjonering av Hard-disken:




- Slett disk**: For en fullstendig installasjon av PureOS, slettes alle eksisterende data på Hard-disken.



![0_14](assets/fr/14.webp)





- Manuell partisjonering** for å lage dine egne partiturer



⚠️ Når du oppretter partisjoner for operativsystemet manuelt, må du sørge for at du tildeler en partisjon på minst 2 GB til PureOS-drift og deretter en annen partisjon til data.



![0_15](assets/fr/15.webp)



Aktiver **diskkryptering** hvis du ønsker å sikre dataene dine. Skriv inn et sterkt, komplekst passord.



Knytt en bruker til operativsystemet ved å definere et brukernavn og et alfanumerisk passord på minst 20 tegn for å styrke datasikkerheten.



![0_16](assets/fr/16.webp)



Gå gjennom innstillingene du har gjort, og endre dem om nødvendig.



![0_17](assets/fr/17.webp)



Klikk på **Installer** og deretter på **Installer nå** for å bekrefte at PureOS er installert på datamaskinen din.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



Når installasjonen er fullført, merker du av i boksen **Start på nytt nå** for å starte datamaskinen på nytt, og bekrefter deretter:




- Språket.
- Tastaturoppsett.
- NextCloud-kontoen din (valgfritt).



![0_25](assets/fr/25.webp)



## Oppdateringer



Før du begynner å bruke PureOS, er det viktig å oppdatere systemet ditt. Da får du tilgang til de nyeste funksjonene og sikkerhetsoppdateringene, og du sikrer bedre stabilitet.





- Oppdatering via Interface-grafikk**:


Åpne **Programvare**, og gå deretter til fanen **Oppdateringer**. Tilgjengelige oppdateringer vises automatisk. Klikk på **Last ned** og deretter på **Installer** når nedlastingen er fullført.





- Oppdater via terminal**:


Åpne terminalen, og skriv inn følgende kommando for å oppdatere listen over tilgjengelige pakker:



```shell
sudo apt update
```



Skriv inn passordet ditt og bekreft. Installer deretter oppdateringene med:



```shell
sudo apt full-upgrade
```



## PureOS for utvikling



PureOS inneholder som standard ikke alle verktøyene som trengs for utvikling.


Du kan installere dem raskt med følgende kommando:



```shell
sudo apt install build-essential git curl
```



Dette vil installere kompileringsverktøyene **Git** og **Curl**, som er nyttige i de fleste utviklingsmiljøer.



## PureOS-miljø



PureOS skiller seg ut med sin innovative tilnærming til ekte konvergens: Ett enkelt operativsystem sikrer jevn og sømløs drift på tvers av en rekke enheter, inkludert bærbare datamaskiner, nettbrett, mini-PC-er og smarttelefoner.



PureOS-applikasjoner er utviklet for å være tilpasningsdyktige: De tilpasser seg automatisk til skjermstørrelse og inndatamodus (berøring eller tastatur/mus). GNOME-nettleseren tilpasser for eksempel Interface dynamisk for å gi en optimal opplevelse på både mobile og stasjonære enheter.



PureOS inneholder også kontorpakken **LibreOffice**, som inkluderer:





- Writer**: en komplett tekstbehandler for oppretting og redigering av dokumenter.
- Calc**: et kraftig regnearkprogram for håndtering av data og beregninger.
- Impress**: et verktøy for å lage profesjonelle presentasjoner.



Med denne gratispakken kan du jobbe effektivt uten å være avhengig av proprietær programvare.



PureOS tilbyr et enhetlig, sikkert og fleksibelt miljø, basert på en 100 % åpen kildekodedistribusjon som garanterer total kontroll og streng respekt for personvernet. Den ekte konvergensen gjør det mulig å lage applikasjoner som er kompatible med ulike typer enheter, for eksempel datamaskiner, nettbrett og smarttelefoner, uten behov for komplekse tilpasninger.



PureOS har innebygd tilgang til viktige verktøy, robuste pakkebehandlere og et rikt økosystem med åpen kildekode, og forenkler utvikling, testing og distribusjon av applikasjoner i et sikkert miljø. Den stabile arkitekturen og Commitment til konfidensialitet gjør den til en pålitelig plattform for en rekke bruksområder, inkludert Blockchain-utvikling, rask prototyping eller produksjonsmiljøer.



Oppdag kurset vårt om hvordan du kan styrke sikkerheten og beskytte det digitale personvernet ditt.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1