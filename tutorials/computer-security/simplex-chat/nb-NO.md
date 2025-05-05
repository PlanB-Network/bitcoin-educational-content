---
name: SimpleX Chat
description: Den første postkassen uten bruker-ID
---
![cover](assets/cover.webp)



SimpleX ble lansert i 2021 og er et gratis direktemeldingsprogram med en radikalt annerledes tilnærming til personvern. I motsetning til WhatsApp, Signal og andre sentraliserte meldingstjenester, skiller SimpleX seg ut med sin brukeradministrasjon: det finnes ingen brukeridentifikatorer, pseudonymer, numre eller synlige offentlige nøkler. Dette totale fraværet av identifikatorer gjør det praktisk talt umulig å korrelere brukere, noe som garanterer et høyt nivå av personvern.



I motsetning til de fleste applikasjoner som krever en konto eller et telefonnummer, lar SimpleX deg starte samtaler ved å dele en lenke eller en kortvarig QR-kode. Hver lenke skaper en unik kryptert kanal, og kontakter kan ikke finne eller kontakte avsenderen på nytt uten en eksplisitt Exchange. Meldingene er kryptert fra ende til annen, og går gjennom relay-servere som sletter dem etter at de er sendt, og som verken ser avsenderen, mottakeren eller nøklene deres.



![Image](assets/fr/01.webp)



Nettverksarkitekturen er helt desentralisert og ikke føderert: Serverne kjenner ikke hverandre, de har ingen global katalog, og de er ikke vertskap for noen brukerprofiler. Og enda bedre: Hver bruker kan utplassere og bruke sin egen relay-server, samtidig som de er kompatible med serverne i det offentlige nettverket.



SimpleX er helt åpen kildekode (klienter, protokoller og servere), og er tilgjengelig på Android, iOS, Linux, Windows og macOS. Den lokale lagringen er kryptert og bærbar, slik at du kan overføre en profil fra én enhet til en annen uten å være avhengig av en sentralisert server.



SimpleX integrerer alle de klassiske funksjonene i meldingsapplikasjoner. Ergonomien er imidlertid mindre smidig enn i WhatsApp eller Signal. Det kan også være mer restriktivt å bruke, spesielt når man legger til kontakter. Etter min mening er SimpleX et relevant alternativ til WhatsApp eller Signal for brukere som prioriterer konfidensialitet, og som av den grunn er villige til å gjøre noen innrømmelser når det gjelder den daglige brukerkomforten.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| **SimpleX**          | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = ende-til-ende-kryptering*



## Installer SimpleX Chat-applikasjonen



SimpleX Chat er tilgjengelig på alle plattformer. Du kan laste ned applikasjonen direkte fra appbutikken på telefonen din:




- [Google Play] (https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store] (https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid] (https://simplex.chat/fdroid/).



På Android er det også mulig å [installere via APK] (https://github.com/simplex-chat/simplex-chat/releases).



I denne veiledningen konsentrerer vi oss om mobilversjonen, men vær oppmerksom på at [desktop-versjoner også er tilgjengelige](https://simplex.chat/downloads/) (MacOS, Linux og Windows). Det er mulig å koble desktop-versjonen til en eksisterende mobil brukerprofil, men for at denne synkroniseringen skal fungere, må begge enhetene være koblet til samme lokale nettverk.



![Image](assets/fr/02.webp)



## Opprett en konto på SimpleX Chat



Når du starter applikasjonen for første gang, klikker du på knappen "*Opprett profil*".



![Image](assets/fr/03.webp)



Velg et brukernavn, som kan være ditt virkelige navn eller et pseudonym, og klikk deretter på "*Opprett*".



![Image](assets/fr/04.webp)



Deretter angir du hvor ofte applikasjonen skal se etter nye meldinger. Hvis telefonens batterilevetid ikke er et problem, velger du "*Instant*" for å motta meldinger i sanntid. Hvis du foretrekker å spare batteri og forhindre at applikasjonen kjører i bakgrunnen, velger du "*Når appen kjører*": Du vil da bare motta meldinger når applikasjonen er åpen. Et mulig kompromiss er å velge en periodisk sjekk hvert 10. minutt.



Når du har gjort ditt valg, klikker du på "*Bruk chat*".



![Image](assets/fr/05.webp)



Du er nå koblet til SimpleX Chat og klar til å begynne å chatte.



![Image](assets/fr/06.webp)



## Sette opp SimpleX Chat



Først og fremst får du tilgang til innstillingene ved å klikke på profilbildet ditt nederst i høyre hjørne, og deretter på "*Settings*".



![Image](assets/fr/07.webp)



Standardinnstillingene passer vanligvis for de fleste brukere. Jeg anbefaler imidlertid at du går til menyen "*Database passphrase & eksport*". Her kan du eksportere SimpleX-kontodatabasen din for sikkerhetskopiering.



Du kan også endre passphrase som brukes til å kryptere denne databasen. Som standard genereres den tilfeldig og lagres lokalt på enheten din. Hvis du foretrekker det, kan du definere din egen passphrase og slette den lokale passphrase-backupen: Du må da angi den manuelt hver gang du åpner programmet, samt når du migrerer til en annen enhet.



**Merk**: Hvis du velger dette alternativet, vil tapet av passphrase føre til permanent tap av alle SimpleX-profiler og -meldinger.



![Image](assets/fr/08.webp)



Jeg anbefaler også at du går til menyen "*Privacy & security*", der du kan aktivere alternativet "*SimpleX Lock*". Dette beskytter tilgangen til applikasjonen med en låskode.



![Image](assets/fr/09.webp)



Til slutt kan du tilpasse SimpleX Chat til dine egne preferanser ved hjelp av menyene "*Notifications*" og "*Appearance*".



![Image](assets/fr/10.webp)



## Send meldinger med SimpleX Chat



Du har to alternativer for å komme i kontakt med en annen person på SimpleX:




- Bruk en lenke til engangsbruk;
- Bruk en gjenbrukbar statisk Address.



En statisk Address gjør at alle som kjenner den, kan kontakte deg på SimpleX. Det er en persistent Address, som kan brukes flere ganger, av forskjellige personer, uten tidsbegrensning. Det er denne vedvarende egenskapen som gjør den mer sårbar for spam. I motsetning til andre meldingsprogrammer er det imidlertid nok å slette SimpleX Address for å stoppe all spam, uten at det påvirker eksisterende samtaler. Address brukes faktisk bare til å opprette den første forbindelsen, og er ikke lenger nødvendig når Exchange er påbegynt.



Engangskoblinger kan derimot bare brukes én gang, av en hvilken som helst bruker. Når en kontakt bruker den, blir koblingen ugyldig. Du må opprette en ny generate for hver nye tilkobling.



### Med statisk Address



Hvis du ønsker å bruke Address, klikker du på profilbildet ditt nederst til venstre på Interface, og velger deretter "*Opprett SimpleX Address*". Klikk deretter på "*Opprett SimpleX Address*" igjen.



![Image](assets/fr/11.webp)



Din gjenbrukbare Address er nå opprettet. Du kan dele den med personer som ønsker å komme i kontakt med deg, enten ved å vise dem QR-koden eller ved å sende dem lenken.



![Image](assets/fr/12.webp)



Klikk på knappen "*Address-innstillinger*". Her kan du konfigurere tillatelsene som er knyttet til din Address. Alternativet "*Del med kontakter*" gjør Address synlig på SimpleX-profilen din. Kontaktene dine vil da kunne se den og videresende den til andre personer som ønsker å kontakte deg.



Alternativet "*Auto-aksept*" aksepterer automatisk innkommende tilkoblinger via din Address. Dette betyr at alle som har din Address vil kunne se profilen din og sende deg en melding, med mindre du aktiverer "*Aksepter inkognito*"-alternativet. Dette skjuler navnet og profilbildet ditt når en ny tilkobling opprettes, og erstatter dem med et tilfeldig pseudonym som er forskjellig for hver samtalepartner.



![Image](assets/fr/13.webp)



### Med gjenbrukbar lenke



Den andre måten å få kontakt med en person på, er å opprette en engangskobling. Dette gjør du ved å klikke på blyantikonet nederst i høyre hjørne av Interface, og deretter velge "*Opprett engangskobling*".



Hvis kontakten din har sendt deg en lenke, klikker du på "*Scan / Lim inn lenke*" for å skanne eller lime den inn.



![Image](assets/fr/14.webp)



SimpleX genererer deretter en engangskobling. Du kan videresende den til kontakten din på hvilken som helst måte: fysisk Exchange, andre meldinger osv.



![Image](assets/fr/15.webp)



Du kan også velge hvilken profil du vil knytte til denne invitasjonslenken. Dette gjør du ved å klikke på profilen din rett under QR-koden. Du vil da kunne velge :




- velg en av de eksisterende profilene dine (vi skal se hvordan du oppretter flere profiler i neste avsnitt);
- eller velg "*Inkognito*"-modus, som skjuler navnet ditt og profilbildet ditt med et tilfeldig generert pseudonym for korrespondenten din.



Her velger jeg "*Inkognito*"-modus.



![Image](assets/fr/16.webp)



Kontakten min brukte lenken. Han aktiverte ikke "*Incognito*"-modusen, og det er derfor jeg ser profilnavnet hans, "*Bob*". På den annen side ser Bob ikke mitt virkelige navn "*Loïc Morel*", men et tilfeldig pseudonym, i dette tilfellet "*RealSynergy*".



![Image](assets/fr/17.webp)



Jeg kan begynne å chatte med en gang, men først vil jeg sjekke at jeg snakker med Bob, og ikke med en ondsinnet person som kan ha snappet opp koblingen eller utført et MITM-angrep.



For å gjøre dette skal vi sjekke sikkerhetskoblingen vår **utenfor applikasjonen**. Dette er viktig, for i tilfelle et MITM-angrep vil den interne verifiseringen bli kompromittert. Så bruk et annet sikkert meldingssystem, eller enda bedre, sjekk kodene personlig.



I chatten klikker du på bildet av Bob og deretter på "*Verifiser sikkerhetskode*". Bob må gjøre det samme på sin side.



![Image](assets/fr/18.webp)



Hvis du jobber eksternt, kan du sammenligne kodene på et annet sikkert meldingssystem (de må være identiske). Eller enda bedre, hvis dere kan møtes ansikt til ansikt, kan du skanne kontaktens QR-kode ved å klikke på "*Scan code*".



![Image](assets/fr/19.webp)



Hvis bekreftelsen er vellykket, vises et skjoldikon med en hake ved siden av kontaktens navn. Dette er din forsikring om at du utveksler med Bob. Hvis bekreftelsen mislykkes, vises meldingen "*Ukorrekt sikkerhetskode!*".



![Image](assets/fr/20.webp)



Du kan nå fritt sende Exchange-meldinger, samtaler og filer til Bob, avhengig av hvilke tillatelser du har angitt for denne samtalen.



## Tilpass SimpleX Chat-profilene dine



En av SimpleX' kraftigste funksjoner er muligheten til å administrere flere helt separate brukerprofiler, som alle er tilgjengelige fra samme lokale konto. På denne måten kan du skille de ulike identitetene dine på en ryddig måte, uten at det kompliserer meldingshåndteringen.



Du kan for eksempel opprette :




- En profil med ditt virkelige navn og et ekte bilde for profesjonelle utvekslinger;
- En profil med ditt virkelige navn og et morsomt bilde for familieutvekslingene dine;
- En profil med et falskt bilde og et pseudonym for dine personlige samtaler;
- En annen pseudonym profil for chatting med fremmede.



Det er det vi skal gjøre her. Jeg begynner med å konfigurere hovedprofilen min, den som er knyttet til min virkelige identitet. Dette gjør jeg ved å klikke på profilbildet mitt nederst i høyre hjørne, og deretter på brukernavnet mitt.



![Image](assets/fr/21.webp)



Deretter klikker jeg på profilbildet mitt for å endre det og legge til et nytt.



![Image](assets/fr/22.webp)



Hvis du vil legge til andre profiler, klikker du på "*Dine chatteprofiler*"-menyen.



![Image](assets/fr/23.webp)



Her ser du alle profilene dine. Klikk på "*Legg til profil*" for å opprette en ny profil.



![Image](assets/fr/24.webp)



Deretter velger du informasjon for den nye profilen din: navn, bilde osv. Her bruker jeg et pseudonym og et annet bilde for å skjule min virkelige identitet i visse utvekslinger.



![Image](assets/fr/25.webp)



Ved å holde fingeren nede på en profil kan du skjule den. Da blir den usynlig i applikasjonen, sammen med alle tilknyttede samtaler. Du kan også velge å "*Mute*" den for å slutte å motta varsler.



![Image](assets/fr/26.webp)



Når du har opprettet profilene dine, kan du administrere dem uavhengig av hverandre. Fra startsiden velger du ganske enkelt den aktive profilen som skal vises.



![Image](assets/fr/27.webp)



Når du oppretter en invitasjonskobling eller statisk Address, kan du nå velge hvilken profil som skal knyttes til den. Hvis jeg for eksempel velger profilen "*Satoshi Nakamoto*" for å generate en kobling og sender den til Alice, vil hun bare se den pseudonyme identiteten min "*Satoshi Nakamoto*", uten å få vite om den virkelige identiteten min "*Loïc Morel*". Hvis jeg derimot gir henne en lenke fra min ekte profil, vil hun ikke ha noen mulighet til å lenke til min pseudonyme profil.



![Image](assets/fr/28.webp)



Gratulerer, du er nå i gang med SimpleX messaging, et utmerket alternativ til WathsApp!



Jeg anbefaler også denne andre opplæringen, der jeg presenterer Threema, et annet interessant alternativ for meldingsapplikasjonen din:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74