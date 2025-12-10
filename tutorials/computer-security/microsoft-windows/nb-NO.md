---
name: Windows 11
description: Automatisk installasjon av Microsoft Windows 11 via konfigurasjonsfil
---
![cover](assets/cover.webp)


I denne veiledningen lærer vi hvordan du installerer Windows 11 automatisk ved hjelp av en annen metode enn den vanlige Windows-installasjonsprosessen.


## Last ned!


Det første du trenger er en installasjonsfil. Det tryggeste og mest pålitelige stedet å laste den ned er direkte fra Microsofts offisielle nettsted.


Bare gå til lenken nedenfor og følg instruksjonene for å laste ned [Windows 11 ISO-fil] (https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


Når du er på nedlastingssiden, blar du ned til delen for nedlasting av ISO-filen.


![Image](assets/en/01.webp)


og velg riktig versjon.


![Image](assets/en/03.webp)


Når du har valgt Windows 11, klikker du på Bekreft-knappen.


Det kan ta noen sekunder å behandle forespørselen, og deretter vil du se følgende side:


![Image](assets/en/04.webp)


Etter at du har bekreftet forespørselen, må du velge ønsket språk.


![Image](assets/en/05.webp)


Etter at du har valgt språk og klikket på Bekreft-knappen, vil forespørselen bli behandlet. Dette trinnet kan ta noen sekunder.


Når forespørselen er behandlet, vil du se en side med en nedlastingslenke til .iso-filen. Klikk på 64-biters nedlastingsknappen for å starte nedlastingen.


Filstørrelsen er ca. 5,5 GB, og den genererte lenken vil være gyldig i 24 timer.


## Automatisering!


På dette stadiet må vi gjøre endringer i standardinstallasjonen av Windows. I denne fasen, ved hjelp av Unattended install, bestemmer vi hvilke elementer som skal installeres, uten at brukeren trenger å gjøre noe i etterkant. I denne metoden brukes faktisk en XML-fil til å konfigurere installasjonstrinnene og tjenestene som installeres i Windows. Bruken av Unattended.xml-filen skaper med andre ord en automatisert prosess under installasjonen, slik at det ikke er nødvendig å velge flere alternativer, og man unngår de kjedelige trinnene som vanligvis kreves under installasjonen. Denne metoden er en uvanlig, men standard metode som har blitt introdusert av Microsoft. Du finner mer informasjon på [Microsofts offisielle nettsted] (https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


Det finnes forskjellige verktøy tilgjengelig på internett for å generere filer uten tilsyn. Noen av dem er online, mens andre er offline. Et av de elektroniske verktøyene for å lage denne filen er [dette nettstedet] (https://schneegans.de/windows/unattend-generator). Etter å ha åpnet den, blir vi presentert med følgende side:


![Image](assets/en/06.webp)


Som nevnt øverst på siden, kan denne metoden brukes til å installere Windows 10 og 11. I det første trinnet velger vi Windows-språket. Hvis vi trenger å legge til et annet eller til og med et tredje språk i listen over Windows-skjerm- og tastaturspråk, kan vi bruke boksen nedenfor:


![Image](assets/en/07.webp)


I neste trinn velger vi ønsket plassering.


![Image](assets/en/08.webp)


På dette stadiet kan vi også spesifisere prosessorarkitekturen for datamaskinen. I dette trinnet kan vi gjøre det:

1. Bestem om du vil ignorere sikkerhetsfunksjoner i Windows, for eksempel TPM og Secure Boot. Secure Boot-funksjonen sørger for at hvis noen av de sentrale Windows-filene blir tuklet med under oppstartsprosessen, oppdages problemet, og kjøringen av dem forhindres. Denne funksjonen bidrar også til å beskytte systemet mot å installere skadelige oppdateringer i Windows. På enkelte datamaskiner, spesielt eldre modeller, er det uunngåelig å aktivere muligheten til å omgå disse funksjonene. Det anbefales imidlertid generelt å beholde funksjoner som Secure Boot aktivert.

2. Ignorer kravet om internettforbindelse for å fullføre prosessen. Dette er nyttig i situasjoner der en kablet LAN-tilkobling ikke er tilgjengelig, fordi det trådløse kortet i de fleste tilfeller ikke gjenkjennes under Windows-installasjonen, og Internett-tilgang via kabel er nødvendig. Hvis du aktiverer dette alternativet, løser du problemer knyttet til dette trinnet.


I neste trinn kan vi velge et navn på datamaskinen.


![Image](assets/en/09.webp)


Vi kan også la Windows velge et navn for systemet. I dette trinnet kan vi velge type Windows, enten komprimert eller ukomprimert, eller la Windows bestemme hvilken versjon som passer ut fra datamaskinens spesifikasjoner. Tidssonen kan også angis på dette trinnet.


Neste trinn omfatter partisjonsinnstillinger:


![Image](assets/en/10.webp)


På dette stadiet kan vi spesifisere partisjonstypen for installasjon av Windows, samt de nødvendige innstillingene for installasjon av Windows Recovery Environment. Ved å velge det første alternativet utsettes partisjonsvalg og partisjonering til tidspunktet for Windows-installasjonen, og under installasjonen vil disse spørsmålene bli stilt akkurat som i den normale installasjonsmetoden.


I dette trinnet velger vi hvilken versjon av Windows som skal installeres:


![Image](assets/en/11.webp)


Hvis en produktnøkkel er tilgjengelig, kan den også legges inn på dette stadiet.


Neste trinn innebærer å konfigurere Windows-påloggingskontoen:


![Image](assets/en/12.webp)


## Kontomøter


På dette stadiet


1. Vi kan definere et navn og et passord for administratorkontoen. Det er også mulig å opprette flere bruker- eller administratorkontoer.

2. Her angir vi hvilken konto du skal logge inn på første gang du installerer Windows. De ulike alternativene for denne delen er vist i bildet.

3. Hvis du ikke vil at det skal opprettes noen kontoer, sletter du alle kontoer og velger dette alternativet. I dette tilfellet vil du automatisk bli logget inn på Windows-administratorkontoen etter Windows-installasjonen.


Neste trinn innebærer å konfigurere innstillinger for passord og vertsfil:


![Image](assets/en/13.webp)


På dette stadiet bestemmer vi om passordene skal ha en utløpsperiode. I tillegg inneholder denne delen sikkerhetsinnstillinger knyttet til mislykkede påloggingsforsøk, som kan aktiveres eller deaktiveres basert på dine behov.


Nederst i denne delen finnes det innstillinger for filvisning. Ingen av disse alternativene er tilgjengelige under en standard Windows-installasjon, og må konfigureres etter installasjonen. Med metoden for uovervåket installasjon er disse innstillingene derimot lett tilgjengelige.


Neste trinn innebærer å konfigurere sikkerhetsinnstillingene i Windows:


![Image](assets/en/14.webp)


## Sikkerhetsinnstillinger


På dette stadiet


1. Windows Defender kan aktiveres eller deaktiveres. Denne funksjonen fungerer som en sikkerhetsprogramvare i Windows og bidrar til å forhindre kjøring av skadelige filer, visse nettverksangrep og mer.

2. Automatiske Windows-oppdateringer kan deaktiveres. Dette er en av de vanligste utfordringene Windows-brukere står overfor!

3. Denne delen gjør det mulig å aktivere eller deaktivere UAC (User Account Control). Denne funksjonen hindrer mistenkelige programmer i å kjøre med utvidede lese- og skrivetillatelser.

4. Denne funksjonen brukes av Windows til å oppdage potensielt skadelig programvare.

5. Aktiver eller deaktiver støtte for lange baner i Windows-programmer, for eksempel PowerShell og andre.

6. Aktiver eller deaktiver Eksternt skrivebord for ekstern tilgang til systemet.


Avhengig av hvilken Windows-versjon som brukes, kan det hende at noen av disse funksjonene ikke støttes.


Neste trinn innebærer konfigurering av ikonene:


![Image](assets/en/15.webp)


I denne delen:


1. Skrivebordsikoner er listet opp, og de kan legges til eller fjernes etter behov.

2. Startmenyikonene er listet opp, og de kan også legges til eller fjernes etter behov.

3. Denne delen gjør det mulig å konfigurere om virtualiseringsrelaterte verktøy skal installeres eller ikke. Dette alternativet er spesifikt for Windows 11 og gjelder ikke for Windows 10.


Neste trinn innebærer å konfigurere Wi-Fi-innstillinger:


![Image](assets/en/16.webp)


I denne delen kan du konfigurere innstillinger for Wi-Fi-nettverk. Som nevnt tidligere, blir Wi-Fi-kortet i de fleste tilfeller ikke gjenkjent under Windows-installasjonen, så det er vanligvis ikke mulig å koble til under installasjonen. Ved å konfigurere denne delen kan systemet imidlertid koble seg til Internett hvis det trådløse kortet oppdages.


Neste trinn innebærer en viktig innstilling:


![Image](assets/en/17.webp)


I denne delen angir vi om informasjon om systemproblemer skal sendes til Microsoft eller ikke.


Neste trinn innebærer konfigurering av standardapplikasjoner:


![Image](assets/en/18.webp)


## Standard aktivering/deaktivering av programvare


I denne delen kan vi velge applikasjoner som vi ikke ønsker å installere som standard. Vi kan for eksempel velge å ikke installere Cortana eller Copilot.


Neste trinn omfatter sikkerhetsinnstillinger knyttet til kjøring av applikasjoner:


![Image](assets/en/19.webp)


Ved å bruke WDAC-innstillinger kan kjøring av visse programmer forhindres.


Til slutt, etter å ha brukt de ønskede innstillingene, kan den genererte XML-filen lastes ned:


![Image](assets/en/20.webp)


Ved å klikke på Download XML File lastes autounattend.xml-filen ned. For å bruke denne filen er det bare å montere den nedlastede ISO-filen på en USB-stasjon, plassere autounattend.xml-filen i rotkatalogen og deretter fortsette med Windows-installasjonen.


Et av verktøyene som er tilgjengelige for å lage en oppstartbar USB-stasjon er Rufus. Rufus kan lage en oppstartbar Windows-installasjons flash-stasjon, med en gitt Windows-installasjons ISO-fil. Det er raskt og enkelt, du kan laste det ned [her] (https://rufus.ie/en/#download)


![Image](assets/en/21.webp)


I denne programvaren, etter å ha valgt ønsket USB-stasjon og riktig ISO-fil, klikker vi på Start.


![Image](assets/en/22.webp)


På dette stadiet deaktiverer vi alle alternativene, da aktivering av dem kan føre til konflikter når du bruker den genererte Unattend-filen. Etter at filene er kopiert til USB-stasjonen, plasserer vi filen autounattend.xml i rotkatalogen:


![Image](assets/en/23.webp)


Nå er USB-stasjonen klar til å brukes til å installere Windows automatisk, og installasjonen kan startes ved hjelp av denne stasjonen.


## ISO-redigering


Hvis du trenger å installere Windows på en virtuell maskin, kan du bruke programvare for å opprette og redigere ISO-filer. En slik programvare er AnyBurn. Etter at du har hentet ut innholdet i ISO-filen som er lastet ned fra Microsofts nettsted, plasserer du filen autounattend.xml i rotkatalogen. Deretter bruker du AnyBurn til å opprette en ny ISO-fil med det oppdaterte innholdet.


AnyBurn er en multifunksjonell programvare for arbeid med ISO-filer. Den tilbyr forskjellige funksjoner for håndtering av ISO-filer, hvorav en av dem er å lage oppstartbare ISO-bilder; [her] (https://www.anyburn.com/download.php) er den opprinnelige nettsiden.


På hovedsiden til programvaren velger du "Opprett bilde fra fil/mappe":


![Image](assets/en/24.webp)


På neste side velger du alle filene som er hentet ut fra ISO-en sammen med filen autounattend.xml.


![Image](assets/en/25.webp)


I dette trinnet konfigurerer vi innstillingene for å gjøre ISO-filen oppstartbar:


![Image](assets/en/26.webp)


På dette stadiet må banen til bootfix.bin-filen angis for å gjøre ISO-en oppstartbar. Denne filen ligger i roten av ISO-en, i oppstartsmappen. Det anbefales også å aktivere både ISO9660- og UDF-alternativene i Egenskaper-delen.


![Image](assets/en/27.webp)


Etter dette trinnet, klikker du på Neste for å opprette ISO-filen. Denne filen kan brukes i virtualiseringsprogramvare som Oracle VirtualBox. Nedenfor finner du en veiledning om VirtualBox:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65