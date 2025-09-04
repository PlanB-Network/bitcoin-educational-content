---
name: Debian
description: En Linux-distribusjon som er kjent for sin stabilitet, robusthet og kompatibilitet.
---

![cover](assets/cover.webp)



Debian er en fri GNU/Linux-distribusjon som er kjent for sin robusthet og pålitelighet. Linux-kjernen og alle pakkene er grundig testet for å sikre bunnsolid stabilitet og et høyt sikkerhetsnivå. Debian er egnet for både servere og arbeidsstasjoner, og tilbyr en brukervennlig opplevelse og en stor katalog med programvare. Enten du er ute etter et sikkert system for daglig bruk eller et produksjonsmiljø, er Debian det riktige valget.



## Hvorfor velge Debian?





- Gratis og åpen**: Debian er helt åpen kildekode, noe som garanterer åpenhet og ingen lisensavgifter.
- Stabilitet og sikkerhet**: Hver utgivelse gjennomgår en grundig testprosess, noe som gjør Debian til en av de mest pålitelige og sikre distribusjonene på markedet.
- Aktivt fellesskap**: Et stort fellesskap og omfattende dokumentasjon er tilgjengelig for å støtte deg når du trenger det.
- Lett og skalerbar**: Du kan installere Debian på maskiner med beskjedne ressurser og samtidig opprettholde god ytelse.
- Omfattende programvarekatalog**: over 50 000 offisielle pakker er tilgjengelige via repositoriene.



## Velg en Interface-grafikk



Debian tilbyr flere skrivebordsmiljøer som passer til dine behov:





- GNOME**: moderne, intuitiv Interface, ideell for nybegynnere. Den tilbyr en flytende, brukervennlig grafisk meny for tilgang til programmer.
- XFCE**: lett og rask, perfekt for mindre kraftige maskiner.
- KDE Plasma**: svært tilpasningsdyktig, med et Windows-lignende utseende.
- Cinnamon**: enkel, elegant Interface, inspirert av Windows.
- LXDE / LXQt**: ultralett, egnet for eldre datamaskiner.
- MATE**: enkel og klassisk, nær det gamle GNOME.



💡 For en komfortabel og grepsvennlig opplevelse anbefales **GNOME** på det sterkeste.



## Installere og konfigurere Debian


### Krav til maskinvare



Før du starter installasjonen, må du forsikre deg om at du har følgende utstyr:





- USB-nøkkel**: minimum 8 GB for å lagre det oppstartbare ISO-bildet.
- Tilfeldig tilgangsminne (RAM)**: 4 GB for problemfri installasjon og drift.
- Diskplass**: minst 15 GB ledig plass til systemet og oppdateringer.



### Last ned



Valget av Debian-image avhenger av prosessorarkitekturen din:





- AMD64**: Last ned "live hybrid"-utgaven fra [download]-listen (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: hent DVD-bildet fra det offisielle [Debian]-nettstedet (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- Andre arkitekturer**: Finn ISO-en som tilsvarer din arkitektur [her] (https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Opprette en oppstartbar USB-nøkkel



Når du har lastet ned det aktuelle ISO-bildet, kan du fortsette med å opprette installasjonsmediet:




- Last ned Balena Etcher** fra [offisiell nettside] (https://etcher.balena.io/), hent deretter binærfilen til systemet ditt og installer den.



![etcher](assets/fr/02.webp)





- Start Etcher**: åpne programvaren og velg det tidligere nedlastede Debian ISO-bildet.
- Velg USB-nøkkel**: Angi nøkkelen din (8 GB+) som mål.
- Start flash**: klikk på **Flash!** og vent til prosessen er fullført.



![flash](assets/fr/03.webp)



USB-nøkkelen din er nå klar til å begynne å installere Debian.



## Installere Debian på systemet ditt



### Oppstart fra USB-nøkkel



Slik starter du installasjonen fra USB-nøkkelen:




- Slå datamaskinen helt av**.
- Start på nytt** og få tilgang til BIOS/UEFI ved å trykke på `ESC`, `F2`, `F11` (eller den dedikerte tasten avhengig av merke).
- I oppstartsmenyen **velger du USB-nøkkelen** som oppstartsenhet.
- Bekreft** med Enter-tasten for å starte Debian-imaget: Dette tar deg til installeringsprogrammets velkomstskjerm.



### Starter installasjonen



Startskjerm:



![starting](assets/fr/04.webp)



Når du starter opp fra USB-minnepinnen, tilbyr Debians velkomstskjerm flere alternativer:




- Live System**: starter Debian uten å installere det, ideelt for testing av miljøet.
- Start Installer**: starter installasjonen direkte på Hard-disken.
- Advanced Install Options**: gir deg tilgang til tilpassede installasjonsmodi.



For å utforske Debian i live-modus velger du **Live System** og bekrefter med **Enter**. Du kan deretter starte installasjonen ved å klikke på **Install Debian** i live-miljøet.



![system](assets/fr/05.webp)





- Valg av språk** (valgfritt)



Velg hovedspråket for Debian-systemet ditt fra listen, og klikk deretter på OK.



![language](assets/fr/06.webp)





- Tidssone** (GMT)



Velg din geografiske sone for å stille inn dato og klokkeslett automatisk.



![timezone](assets/fr/07.webp)





- Tastaturoppsett



Velg språk og layout for tastaturet. Bruk det innebygde testfeltet til å kontrollere at hver tast produserer det forventede tegnet.



![keyboard](assets/fr/08.webp)



### Diskpartisjonering





- Slett disk**: Hvis du har en egen partisjon, vil dette alternativet slette alt innholdet på denne.
- Manuell partisjonering**: Velg dette alternativet for å opprette, endre størrelse på eller slette partisjoner etter behov.



![disk](assets/fr/09.webp)





- Opprette en brukerkonto



Skriv inn ditt fulle navn, kontonavn og et sterkt passord for å sikre at økten din er sikker.



![user](assets/fr/10.webp)





- Sammendrag av parametere**



En oversikt over valgene dine vises: Kryss av for hvert element, og gå tilbake for å endre om nødvendig.



![settings](assets/fr/11.webp)





- Starter installasjonen



Klikk på **Install** for å begynne å kopiere filer og konfigurere systemet, og vent deretter til prosessen er fullført.



![install](assets/fr/12.webp)





- Start på nytt**



Når installasjonen er fullført, starter du datamaskinen på nytt for å bruke alle konfigurasjoner og få tilgang til ditt nye Debian-system.



![restart](assets/fr/13.webp)



Ved oppstart skriver du inn brukernavn og passord for å få tilgang til systemet.



![login](assets/fr/14.webp)



## Oppdatering av systemet



Før du begynner å bruke systemet ditt, er det viktig å oppdatere det. På den måten kan du dra nytte av de nyeste programvareoppdateringene, oppdaterte repositories og i noen tilfeller sikkerhetsoppdateringer for selve operativsystemet.



### Alternativ 1: Oppdatering via grafisk Interface (GNOME)



Hvis du har installert Debian med GNOME-skrivebordsmiljøet, kan du utføre oppdateringer grafisk. For å gjøre dette åpner du **Programvare**, og går deretter til fanen **Oppdateringer**. Klikk deretter på **Start på nytt og oppdater** for å starte prosessen.



### Alternativ 2: Oppdatering via terminal (anbefalt)



Denne metoden gir mer fullstendig kontroll. Den lar deg oppdatere repositorier, programvarepakker og, om nødvendig, kjernen.




- Åpne terminalen ved hjelp av snarveien `Ctrl + Alt + T`.
- Oppdater listen over tilgjengelige pakker med følgende kommando:



```shell
sudo apt update
```



Skriv inn passordet ditt når du blir bedt om det (merk at ingen tegn vises mens du skriver - dette er normalt).





- Slik installerer du tilgjengelige oppdateringer:



```shell
sudo apt full-upgrade
```



## Oppdag de grunnleggende oppgavene



### Surfe på Internett



Standard nettleser på Debian er **Firefox**. Hvis du foretrekker en annen nettleser, kan du installere en annen, forutsatt at den er tilgjengelig i Debian-arkivene (for eksempel Chromium, Brave...).



### Tekstbehandling



**LibreOffice**-pakken er installert som standard på Debian.





- For å skrive dokumenter bruker du **LibreOffice Writer**, som tilsvarer Microsoft Word.
- For regneark fungerer **LibreOffice Calc** som et alternativ til Excel.
- Til slutt kan du lage presentasjoner med **LibreOffice Impress**, akkurat som med PowerPoint.



## Installere applikasjoner



Det er to måter å installere programmer på i Debian:



### Grafisk metode:



Du kan bruke **programvareadministratoren** (tilgjengelig via den grafiske Interface) for å enkelt søke etter og installere programmer.



### Kommandolinjemetode:



Hvis applikasjonen du leter etter ikke vises i den grafiske Interface, eller hvis du foretrekker terminalen, kan du bruke følgende kommando:



```shell
sudo apt install <name>
```



Erstatt `<name>` med pakkenavnet. For eksempel, for å installere `curl`:



```shell
sudo apt install curl
```



### Installere en manuelt nedlastet pakke:



Hvis du har lastet ned en `.deb`-fil (Debian-pakke), kan du installere den med følgende kommando:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

Debian-systemet ditt er nå installert og klart til bruk for dine daglige oppgaver.


Takket være **GNOME**-skrivebordsmiljøet har du tilgang til et bredt spekter av programmer via en brukervennlig grafisk Interface, som er ideell for både nybegynnere og avanserte brukere.



Det er også mulig å bytte skrivebordsmiljø (f.eks. til XFCE, KDE osv.) uten å måtte installere Debian på nytt. For å gjøre dette bruker du ganske enkelt terminalen og installerer det nye miljøet du ønsker.



Hvis du vil lære mer om Debian, og mer generelt om GNU/Linux-distribusjoner, anbefaler jeg at du leser dette kurset:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1