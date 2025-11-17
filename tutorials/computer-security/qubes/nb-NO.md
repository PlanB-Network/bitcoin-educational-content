---
name: Qubes
description: Et rimelig sikkert operativsystem.
---

![cover](assets/cover.webp)



Qubes OS er et gratis operativsystem med åpen kildekode som er utviklet for brukere som setter sikkerhet øverst på prioriteringslisten. Dets særegenhet er basert på en enkel, men radikal idé: I stedet for å betrakte datamaskinen som en helhet, deler det bruken av den inn i uavhengige avdelinger kalt **_qubes_**.



Hver qube fungerer som et **isolert virtuelt miljø**, med et bestemt tillitsnivå og en bestemt funksjon. Så selv om en applikasjon blir kompromittert, forblir angrepet begrenset til den aktuelle quben uten å påvirke resten av systemet.



> Hvis du er opptatt av sikkerhet, er Qubes OS det beste operativsystemet som finnes på markedet i dag. - **Edward Snowden**.

Installasjonen av Qubes OS krever imidlertid mer forberedelser enn installering av et vanlig operativsystem. Det innebærer å sjekke visse maskinvareforutsetninger, forstå det grunnleggende om virtualisering og akseptere en annerledes opplevelse, der alle daglige oppgaver tenkes i form av separasjon. Men når Qubes OS først er på plass, tilbyr det et robust rammeverk som omdefinerer måten du samhandler med datamaskinen på i det daglige. I denne veiledningen forklarer vi hvordan Qubes OS fungerer, og hvordan du enkelt installerer det på systemet ditt.



## Hvordan fungerer Qubes OS?



Qubes OS er basert på prinsippet om oppdeling. I stedet for å bruke ett enkelt system, baserer det seg på hypervisoren **Xen** for å opprette isolerte virtuelle maskiner, kalt qubes. Hver qube er dedikert til en bestemt oppgave eller et bestemt tillitsnivå (arbeid, personlig surfing, banktjenester osv.). Denne separasjonen sikrer at eventuelle kompromitteringer i én qube ikke kan spre seg til de andre, slik at de fungerer som flere uavhengige datamaskiner i én og samme maskin.



Bruker Interface administreres av et sentralt, sikkert domene kalt **dom0**. Dette domenet er fullstendig isolert fra Internett, noe som gjør det til systemets hjerte. Selv om vinduer og menyer vises av dom0, foregår den faktiske kjøringen av applikasjoner i deres respektive qubes.



## De forskjellige typene av qubes



Rundt dom0 kretser ulike typer kuber, hver med en helt spesifikk rolle å spille.





- **AppVM** brukes til å kjøre hverdagsapplikasjoner: Brukeren kan dermed skille mellom profesjonell e-post og nettsurfing eller bankaktiviteter, og hvert miljø forblir helt uavhengig av de andre.





- Disse AppVM-ene er i seg selv basert på **TemplateVM-er**, som fungerer som sentraliserte maler for installasjon og oppdatering av programvare, noe som eliminerer behovet for å administrere hver qube separat.



Qubes OS integrerer også virtuelle maskiner som er spesialisert på **systemtjenester**.





- En **NetVM** administrerer **nettverksenheter** direkte og sørger for tilkobling til Internett. De er ofte forbundet med **BrannmurVM-er**, som griper inn for å **filtrere trafikk** og begrense eksponeringen av andre qubes.





- ServiceVM-er spiller en lignende rolle, for eksempel i håndteringen av USB-enheter, alltid med samme logikk: isoler de mest risikofylte komponentene for å redusere angrepsflaten.



Til slutt, for sporadiske eller risikofylte oppgaver, tilbyr Qubes OS **DisposableVM**. Disse kortvarige qubene opprettes i farten for å **åpne et mistenkelig dokument** eller **besøke et tvilsomt nettsted**, og forsvinner deretter helt når de lukkes, slik at alle spor slettes og vedvarende angrep forhindres.



### Den sikre kopieringsmekanismen (qrexec)



Utvekslingen mellom qubene er basert på **qrexec**, et sikkerhetssystem for kommunikasjon mellom VM-er. I stedet for å la qubes kommunisere fritt, innfører qrexec **spesifikke retningslinjer**: En fil som kopieres fra en AppVM til en annen, eller tekst som overføres via utklippstavlen, går alltid gjennom en kanal som overvåkes og valideres av systemet. På denne måten blir selv den enkle handlingen å kopiere og lime inn kontrollert for å forhindre spredning av skadelig programvare.



### Diskadministrasjon



Qubes OS bruker et genialt system for lagringsadministrasjon. TemplateVM-er inneholder den felles programvarebasen, mens AppVM-er bare legger til egne personlige data og spesifikke filer. Dette reduserer bruken av diskplass og forenkler globale oppdateringer. DisposableVM-er bruker derimot midlertidige volumer som forsvinner helt når de lukkes. Denne modellen garanterer ikke bare større sikkerhet, men også effektiv ressursforvaltning.



## Hvorfor velge Qubes OS?



Fordelene med Qubes OS ligger først og fremst i den unike sikkerhetsmodellen. Kjernen i denne tilnærmingen er kompartmentalisering, som beskytter brukeren ved å isolere hver oppgave i separate virtuelle maskiner. I praksis kan en infisert e-post eller et ondsinnet nettsted bare kompromittere én enkelt Qubes-maskin, mens resten av systemet og personopplysningene dine er fullt beskyttet. Denne arkitekturen begrenser i betydelig grad komplekse angrep som på et konvensjonelt system kan forplante seg fritt.



Qubes OS gir også full åpenhet og kontroll over det digitale miljøet ditt. Du vet nøyaktig hvilken programvare som har tilgang til hvilke ressurser, enten det er nettverket, en USB-enhet eller andre sensitive komponenter. Systemet integrerer avanserte sikkerhetsfunksjoner som standard, for eksempel full diskkryptering, og gjør det enklere å bruke anonymiseringstjenester som Whonix-operativsystemet.



https://planb.academy/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

I stedet for å skape et ugjennomtrengelig system, fokuserer Qubes OS på robusthet: Det kapsler inn skadene i tilfelle kompromittering, noe som reduserer risikoen for resten av systemet. Denne pragmatiske tilnærmingen gjør Qubes OS til et foretrukket valg for brukere med høye sikkerhetsbehov, eller som ønsker å beholde maksimal kontroll over sine digitale liv.



## Installere Qubes OS



Før du installerer Qubes OS, er det viktig å sikre at maskinvaren din oppfyller minimumskravene, siden systemet er avhengig av virtualisering for å isolere Qubes. De viktigste komponentene som må sjekkes er :




- **Proessoren**: En 64-biters prosessor som er kompatibel med maskinvarevirtualisering (Intel VT-x eller AMD-V).
- RAM: minimum 8 GB er påkrevd, men vi anbefaler RAM på 16 GB eller mer for å kunne kjøre flere qubes samtidig.
- **Lagringsplass**: minst 36 GB, helst 128 GB på en SSD-enhet for optimal ytelse.



For å installere Qubes OS, last ned det offisielle ISO-bildet fra Qubes OS [offisielt nettsted] (https://www.qubes-os.org/downloads/). Det er viktig å kontrollere ISO-filens integritet ved hjelp av GPG-signaturene som følger med, for å sikre at filen ikke er manipulert og at nedlastingen er sikker.



https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Når ISO-filen er verifisert, må du opprette et oppstartbart installasjonsmedium, vanligvis en USB-pinne. Dette gjør du ved å laste ned og installere programvare som **Rufus** på Windows eller **Etcher** på Windows, Linux eller macOS. Med disse verktøyene kan du kopiere ISO-filen til USB-pinnen slik at den blir oppstartbar.



Før du starter installasjonen, må du konfigurere datamaskinens **BIOS eller UEFI** til å **aktivere virtualisering** og tillate oppstart fra USB. Avhengig av maskinmodell kan det være nødvendig å **deaktivere Secure Boot**, ettersom Qubes OS kanskje ikke starter opp med dette alternativet aktivert.



![0_02](assets/fr/02.webp)



Når disse betingelsene er oppfylt, starter du datamaskinen på nytt og åpner BIOS/UEFI ved å trykke **Esc**, **Del**, **F9**, **F10**, **F11** eller **F12** (avhengig av produsent). I oppstartsmenyen velger du USB-nøkkelen som oppstartsenhet for å starte Qubes OS-installasjonen.



**Startskjermbilde**


Når du starter opp fra USB-minnepinnen, kommer du direkte til **GRUB**-menyen, der du kan velge hvilken handling som skal utføres. Bruk piltastene på tastaturet til å velge "Install Qubes OS", og trykk på "Enter".



![0_03](assets/fr/03.webp)



**Valg av språk** :



Når installasjonen starter, er det første trinnet å **velge språk** og **regional variant** som passer for din konfigurasjon. Dette sikrer at systemet og installasjonsalternativene vises riktig på det språket du foretrekker.



![0_04](assets/fr/04.webp)



**Parameterkonfigurasjon** :



På dette stadiet må du konfigurere en rekke Elements før du starter installasjonen på maskinen din.



![0_05](assets/fr/05.webp)



**Tastaturoppsett** :



Klikk på alternativet **Tastatur**, og velg deretter den **tilpassede layouten** for datamaskinen din. Når du har gjort ditt valg, klikker du på **Terminated** for å gå videre til neste trinn.



**Valg av destinasjon** :



Velg alternativet "Installasjonsdestinasjon" for å velge disken du ønsker å installere Qubes OS på. Som standard skjer partisjoneringen automatisk, slik at du kan fjerne alle data fra disken og installere systemet på den. Du kan imidlertid velge **Customized** eller **Advanced Customization** for å utføre en tilpasset partisjonering. Klikk deretter på "Done". Systemet vil be deg om å angi et **passord**, som fungerer som en sikkerhets-Layer for å kryptere dataene dine. Sørg for å velge et komplekst og unikt passord.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Velg dato- og tidsformat** :


Klikk på Tid og dato, og velg deretter din geografiske sone. Du kan også velge ønsket tidsformat: 24 timer eller 12 timer.



![0_08](assets/fr/08.webp)



**Opprettelse av brukerkonto** :


Klikk på **Opprett bruker** for å opprette din **første konto**, som vil gjøre det mulig for deg å logge inn på Qubes OS.



![0_09](assets/fr/09.webp)



**Aktiver root-konto** :


Du kan også **aktivere root-kontoen** ved å angi et eget passord for administrasjon.



![0_10](assets/fr/10.webp)



Når disse innstillingene er gjort, klikker du på **Start installasjon** for å starte prosessen.



![0_11](assets/fr/11.webp)



Vent til **slutt på installasjonen**, og klikk deretter på **start systemet på nytt** for å fullføre installasjonen og starte Qubes OS.



![0_12](assets/fr/12.webp)



**Ytterligere konfigurasjon** :


Etter omstart ber Qubes OS deg om å fullføre **standardmalene og qubes-konfigurasjonen**. Skriv inn passordet som er definert for å kryptere disken.



![0_13](assets/fr/13.webp)



Deretter begynner du med å velge hvilken **TemplateVM** du ønsker å installere. Vanlige alternativer er **Debian 12 Xfce**, **Fedora 41 Xfce** og **Whonix 17**, der sistnevnte anbefales for bruk som krever **anonymitet og nettverkssikkerhet**. Du kan også definere en **standardmal**, som vil fungere som grunnlag for opprettelsen av nye **AppVM-er**.



![0_14](assets/fr/14.webp)



I delen **Hovedkonfigurasjon** kan du velge å automatisk opprette viktige systemkonfigurasjoner som **sys-net**, **sys-brannmur** og **standard DisposableVM**. Det anbefales å aktivere alternativet for å gjøre **sys-brannmur og sys-usb disponible**, for å begrense eksponeringen av enheter og nettverk i tilfelle kompromittering. Du kan også opprette standard **AppVM-er**, for eksempel **personlig**, **arbeid**, **ikke-betrodd** og **hvelv**, for å organisere aktivitetene dine i henhold til deres tillitsnivå.



![0_15](assets/fr/15.webp)



Med Qubes OS kan du også opprette en **qube dedikert til USB-enheter** (sys-usb) og konfigurere **Whonix Gateway- og Workstation-quber** for å sikre kommunikasjonen din via Tor-nettverket. For avanserte brukere kan du i delen **Avansert konfigurasjon** opprette et **LVM thin pool** for å administrere diskplass mellom qubes på en effektiv måte.



Når alle disse alternativene er konfigurert, klikker du på **Fullfør** og deretter på **Fullfør konfigurasjon**. Vent mens systemet bruker disse innstillingene. Du vil deretter bli bedt om å **logge inn på brukerkontoen din**, og Qubes OS-miljøet ditt vil være klart til bruk, sikkert og riktig isolert for de ulike aktivitetene dine.



![0_17](assets/fr/17.webp)



Operativsystemet er nå installert og klart til bruk.



![0_18](assets/fr/18.webp)



## Opprett en qube på systemet ditt



For å opprette en qube styres prosessen av verktøyet **Qube Manager**, som er tilgjengelig fra Start-menyen. I verktøyvinduet klikker du ganske enkelt på ikonet **Create qube** for å åpne et nytt konfigurasjonsvindu. Først skriver du inn et navn på quben, for eksempel "perso-web" eller "work", for å identifisere bruken av den.



Deretter velger du **Type**, vanligvis **AppVM** for rutinemessige oppgaver, eller **DisposableVM** for midlertidig bruk. Det er viktig å velge **Template** som quben skal baseres på, for eksempel "fedora-39" eller "debian-12", ettersom det er denne som inneholder operativsystemet og programvaren. Du skal også utpeke **NetVM**, som er den quben som er ansvarlig for Internett-tilgang, som standard **sys-brannmur**.



Til slutt, etter at du har justert lagringsstørrelse og RAM om nødvendig, klikker du bare på **OK** for å starte opprettelsesprosessen. Når prosessen er fullført, vil den nye qube-en din være synlig i listen og klar til bruk.



Qubes OS er altså ikke noe vanlig operativsystem, men en banebrytende sikkerhetsløsning som tenker nytt om PC-arkitekturen. Tilnærmingen, som er basert på oppdeling og isolering gjennom virtualisering, gir uovertruffen beskyttelse mot de mest sofistikerte truslene. Ved å segmentere arbeidsmiljøet i spesialiserte områder for hver enkelt oppgave, sikrer det at skadelig programvare ikke kan spre seg og sette hele systemet i fare.



Enten du trenger å surfe sikkert på nettet, beskytte sensitiv informasjon eller jobbe med ulike tillitsnivåer, tilbyr Qubes OS et robust og transparent rammeverk. Ved å ta i bruk god praksis og utnytte funksjonene fullt ut, får du en **digital festning** som er tilpasset moderne trusler. Finn ut mer om hvordan du beskytter data og personvern.



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1