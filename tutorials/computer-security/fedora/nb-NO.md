---
name: Fedora
description: Linux-distribusjonen som gir deg et gratis, komplett og sikkert arbeidsområde.
---


![cover](assets/cover.webp)





Fedora er et gratis Linux-basert operativsystem med åpen kildekode som ble lansert i 2003, utviklet av **Fedora Project**-fellesskapet og støttet av **Red Hat Linux**. Det er kjent for sin stabilitet, gode ytelse og brukervennlighet, noe som gjør det til et utmerket valg for både nybegynnere og avanserte brukere. Systemet kjører på de fleste moderne prosessorarkitekturer, noe som gjør det enkelt å installere på praktisk talt alle datamaskiner. Fedora er også tilgjengelig i flere forhåndskonfigurerte utgaver, kalt "Fedora Spins" eller "Fedora Editions", som er utviklet for spesifikke behov (videospill, astronomi, utvikling...).



## Fedora Linux-arkitektur



Som du har lest tidligere, er Fedora et gratis operativsystem basert på Linux-kjernen. Linux-kjernen er den delen av operativsystemet som kommuniserer med maskinvaren og administrerer systemressurser som minne og prosessorkraft.



Fedora Linux inneholder en rekke programvareverktøy og applikasjoner som er nødvendige for å kjøre operativsystemet på toppen av Linux-kjernen. Fedoras modulære arkitektur betyr at det i hovedsak består av en samling enkeltkomponenter som enkelt kan legges til, fjernes eller byttes ut etter behov. På denne måten kan du forme operativsystemet slik at det kun bruker de ressursene du trenger.



Fedora inkluderer også et skrivebordsmiljø, som er Interface der brukerne utfører oppgaver og får tilgang til applikasjoner. Fedoras standard skrivebordsmiljø er GNOME, et brukervennlig, brukervennlig og svært tilpasningsdyktig skrivebordsmiljø.



## Hvorfor velge Fedora?



Blant de mange tilgjengelige Linux-distribusjonene skiller Fedora seg spesielt ut for:





- Modularitet**: Fedora er kompatibel med ulike prosessorarkitekturer, og kan installeres på de fleste datamaskiner, selv de med lite strøm, slik at den passer perfekt til dine behov.





- En enkel, intuitiv Interface**: Fedora kombinerer en moderne grafisk Interface med en kraftig kommandolinje-Interface, noe som gjør den enkel å bruke for alle profiler.





- Kjernestabilitet**: Fedora er basert på Red Hat og er kjent for sine pålitelige oppdateringer, spesielt kjerneoppdateringer, som utføres uten større feil takket være gratis bidrag fra et stort fellesskap.





- Rask og enkel installasjon**: Med en image-størrelse på bare 3 GB er installasjonen rask og enkel, selv på maskiner med begrensede ressurser.



## Fedora-utgaver



Fedora tilbyr utgaver som passer til dine behov, avhengig av profil og bruk. Du finner hovedsakelig:





- Fedora Workstation**: Denne utgaven er ideell for personlig og/eller profesjonell bruk på datamaskinene dine, og er installert med generiske verktøy som nettlesere, en kontorpakke (tekstredigeringsprogrammer) og programvare for medieavspilling.





- Fedora Server**: Denne utgaven er dedikert til serveradministrasjon. Fedora Server inneholder en rekke verktøy som hjelper deg med å distribuere og administrere servere i din egen skala.





- Fedora CoreOS**: Vil du enkelt kjøre og distribuere skyapplikasjoner? Fedora CoreOS er utgaven som gir deg verktøyene du trenger for å lage og administrere avbildninger med for eksempel Docker og Kubernets.



I denne veiledningen skal vi ta hånd om Fedora Workstation-utgaven. Prosessene som beskrives nedenfor, er imidlertid de samme for de andre utgavene.



## Installere og konfigurere Fedora Workstation



Installasjon av Fedora Workstation krever følgende maskinvarekonfigurasjon:




- En USB-nøkkel på minst **8 GB** for å starte operativsystemet.
- Minst **40 GB ledig plass** på datamaskinens Hard-disk.
- 4 GB RAM** for en jevn opplevelse.



### Last ned Fedora Workstation



Du kan laste ned [Fedora Workstation]-utgaven (https://fedoraproject.org/fr/workstation/download) fra Fedora-prosjektets offisielle nettsted. Velg deretter den versjonen som passer til din prosessorarkitektur (32-bit - 64-bit) og klikk på **Last ned**-ikonet.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Opprett en oppstartbar USB-nøkkel



For å installere Fedora må du lage en oppstartbar USB-nøkkel ved hjelp av programvare som [Balena Etcher] (https://etcher.balena.io/).



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Når du er ferdig med å installere Balena Etcher, åpner du programmet og velger det nedlastede Fedora Workspace ISO-bildet. Velg USB-nøkkelen din som destinasjonsmedium, og klikk på **Flash**-knappen for å begynne å lage den oppstartbare nøkkelen.



![boot](assets/fr/05.webp)


### Installere Fedora



Når du er ferdig med å starte opp USB-nøkkelen, slår du av datamaskinen.


Slå på datamaskinen, og åpne BIOS under oppstart ved å trykke på `F2`, `F12` eller `ESC`, avhengig av hvilken datamaskin du bruker.



I oppstartsalternativene velger du USB-nøkkelen som primær oppstartsenhet. Når du bekrefter dette valget, vil datamaskinen starte på nytt og automatisk starte Fedora-installasjonsprogrammet** som ligger på USB-nøkkelen.



Når datamaskinen har startet fra USB-minnepinnen, vises **GRUB-skjermbildet**.



På dette stadiet har du følgende alternativer:




- Test media**: Med dette alternativet kan du kontrollere integriteten til USB-minnepinnen og sikre at alle avhengighetene som kreves for en korrekt installasjon, er til stede. Dette er et valgfritt trinn, men anbefales hvis du er i tvil om USB-pinnen.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Start Fedora**: Dette starter Fedora i "live"-modus, uten installasjon.



På Fedora-skrivebordet (live-modus) klikker du på **Installer Fedora** (eller Installer på Hard-disk) for å starte installasjonsprosessen. Du kan velge å installere senere og teste Fedora uten å måtte installere den.



![install-live](assets/fr/08.webp)



Det første trinnet er å velge Fedoras **installasjonsspråk** og **tastaturoppsett**



![language](assets/fr/10.webp)





- Velge installasjonsdiskett:



Velg Hard-disken som du vil installere Fedora på.



Hvis disken er tom, vil Fedora automatisk bruke all tilgjengelig plass. Ellers kan du tilpasse partisjoneringen (manuelt eller automatisk).



![disk](assets/fr/11.webp)





- Kryptering:



På dette stadiet foreslår Fedora at du krypterer disken din for å legge til en ekstra Layer av sikkerhet. Dette sikrer at dataene dine bare kan leses av Fedora-systemet ditt.



![chiffrement](assets/fr/12.webp)



Før du starter installasjonen, viser Fedora en oppsummering av valgene dine. Bekreft og klikk på installasjonsknappen for å starte Fedora-installasjonen.



![resume](assets/fr/13.webp)



Under installasjonen kopierer Fedora filer og konfigurerer systemet. Når du er ferdig, starter datamaskinen automatisk på nytt.



![installation](assets/fr/14.webp)



### Grunnleggende konfigurasjon


Ved første gangs bruk må du foreta noen få innstillinger:




- Endre systemspråket hvis det er nødvendig.



![language](assets/fr/15.webp)





- Velg et tastaturoppsett som passer dine preferanser.



![keyboard](assets/fr/16.webp)





- Velg tidssone ved å skrive inn navnet på byen din i søkefeltet, og klikk deretter på det tilhørende forslaget.



![timezone](assets/fr/17.webp)





 - Aktiver eller deaktiver tilgang til posisjonen din for applikasjoner som trenger det, samt automatisk sending av feilrapporter.



![location](assets/fr/18.webp)





- Bestem deg for om du vil aktivere tredjeparts programvarelagre.



![logs](assets/fr/19.webp)





- Skriv inn ditt fulle navn og definer et brukernavn for kontoen din.



![name](assets/fr/20.webp)





- Opprett et sikkert passord for økten din: så langt som mulig (minst 20 tegn), så tilfeldig som mulig og med en rekke tegn (små og store bokstaver, tall og symboler). Husk å lagre passordet ditt.



![mdp](assets/fr/21.webp)



Når alle disse trinnene er fullført, kan du starte Fedora og begynne å bruke det umiddelbart, uten ytterligere omstart.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Når installasjonen er fullført, kan du bruke Interface-hjemmet med noen få forhåndsinstallerte verktøy.



![install-now](assets/fr/09.webp)



## Oppdag de grunnleggende oppgavene



### Surfe på Internett


Fedoras standard nettleser er **Firefox**. Den er enkel å bruke og passer for de fleste behov.


Hvis du foretrekker en annen nettleser, kan du installere den fra **programvarebehandleren** eller via **terminalen**.


### Tekstbehandling


Fedora inkluderer **LibreOffice**-kontorpakken som standard, som tilbyr flere nyttige verktøy:




- Writer** for tekstbehandling.
- Calc** for regneark.
- Impress** for å lage presentasjoner.


## Installere applikasjoner


For å installere nye programmer kan du bruke Fedoras **programvarebehandling** (kalt _Software_), som gjør installasjonen enkel og visuell.  Det er imidlertid ofte raskere og mer nøyaktig å bruke **terminalen**.



Før du installerer programvare, må du alltid huske å oppdatere **repositoriene** for å sikre at du har tilgang til de nyeste tilgjengelige versjonene.



Bruk deretter følgende kommando for å starte installasjonen av det ønskede programmet:


sudo dnf install programvare_navn`


## Oppdatering av operativsystemet


Etter installasjonen er det viktig å oppdatere Fedora for å dra nytte av de nyeste sikkerhetsoppdateringene og programvareoppdateringene.


### Alternativ 1: Via Interface-grafikk




- Åpne Fedora **Settings**, og gå deretter til **System**-delen.
- Klikk på **Programvareoppdatering**.
- Start nedlastingen av oppdateringer, og vent til prosessen er fullført.



Det kan være nødvendig med en **omstart** etter at oppdateringene er installert.


### Alternativ 2: Via terminal




- Åpne en terminal og start med å oppdatere **repositoriene** for å sikre at du har de nyeste versjonene av:



```shell
sudo dnf check-update
```





- Deretter oppdaterer du all installert programvare med følgende kommando:



```shell
sudo dnf upgrade
```



Nå er Fedora-systemet ditt oppdatert og klart til bruk for alle dine daglige oppgaver. Oppdag vår veiledning om Linux Mint, en annen Linux-distribusjon, og hvordan du setter opp et sunt og sikkert miljø for dine Bitcoin-transaksjoner.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5