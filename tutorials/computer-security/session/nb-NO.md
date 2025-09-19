---
name: Session
description: Send krypterte meldinger, ikke metadata
---
![cover](assets/cover.webp)



Session er et kryptert meldingsprogram som ble opprettet i 2020, og som er utviklet for å tilby et høyere konfidensialitetsnivå enn tradisjonelle meldinger. Det ble først utviklet av *Oxen Privacy Tech Foundation*, deretter av *Session Technology Foundation*.



Session har noen interessante tekniske funksjoner: ende-til-ende-kryptering av meldinger, et desentralisert nettverk som er organisert for å garantere tilgjengelighet og redundans, og Tor-inspirert løkruting. I motsetning til WathsApp eller Signal, som krever et telefonnummer for registrering, ber Session ikke om noen personlig informasjon (ikke noe nummer, ingen e-post, bare et par kryptografiske nøkler).



Med Session kan du sende meldinger, filer, talemeldinger, lydanrop og grupper på opptil 100 medlemmer (og fellesskap utover det), samtidig som du minimerer lekkasjer av metadata.



![Image](assets/fr/01.webp)



Session er først og fremst rettet mot brukere som setter konfidensialitet i høysetet. Denne meldingstjenesten representerer et seriøst alternativ til WhatsApp, med en arkitektur som er utformet for å tåle moderne overvåkingsmodeller.



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
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = ende-til-ende-kryptering*



## Installer Session-applikasjonen



Session er tilgjengelig på alle plattformer. Du kan laste ned applikasjonen direkte fra applikasjonsbutikken på telefonen din:




- [Google Play] (https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store] (https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid] (https://fdroid.getsession.org/).



På Android er det også mulig å [installere via APK] (https://github.com/session-foundation/session-android/releases).



I denne veiledningen konsentrerer vi oss om mobilversjonen, men vær oppmerksom på at [datamaskinversjoner også er tilgjengelige](https://getsession.org/download) (MacOS, Linux og Windows). Senere skal vi se på hvordan du synkroniserer en konto på tvers av flere enheter.



## Opprett en konto på Session



Ved første oppstart klikker du på "*Opprett konto*".



![Image](assets/fr/02.webp)



Velg et visningsnavn for profilen din. Dette kan være et pseudonym eller ditt virkelige navn.



![Image](assets/fr/03.webp)



Deretter må du velge mellom to moduser for varslingshåndtering:





- Hurtigmodus (**Firebase Cloud Messaging/Apple Push Notification Service**): gjør at du kan motta meldingsvarsler i tilnærmet sanntid, takket være varslingstjenestene som leveres av Google eller Apple (avhengig av systemet ditt). For at dette skal fungere, overføres din IP Address og en unik varslings-ID til Google eller Apple, og Session-konto-ID-en er også registrert hos en STF-server (via Tor). Denne modusen innebærer (riktignok minimal) eksponering av metadata, men kompromitterer ikke meldingsinnhold eller kontakter, og gjør det ikke mulig å spore din faktiske aktivitet. Denne modusen er derfor mer effektiv når det gjelder responstid, men er avhengig av en sentralisert infrastruktur og er litt mindre effektiv når det gjelder konfidensialitet.





- Langsom modus (**bakgrunnspolling**): Session-applikasjonen forblir aktiv i bakgrunnen og polling nettverket med jevne mellomrom etter nye meldinger. Denne tilnærmingen garanterer større konfidensialitet enn den første, ettersom ingen data overføres til tredjepartsservere; verken Google, Apple eller STF-servere mottar noen informasjon. På den annen side har denne modusen to ulemper: Varsler kan bli forsinket (opptil flere minutter), og energiforbruket er generelt høyere på grunn av applikasjonsaktivitet i bakgrunnen.



![Image](assets/fr/04.webp)



Du er nå koblet til Session-applikasjonen og kan begynne å utveksle meldinger.



![Image](assets/fr/05.webp)



## Lagre øktkontoen din



Det første du må gjøre før du begynner å bruke Session, er å lagre kontoen din slik at du kan gjenopprette den hvis du mister enheten din. Dette gjør du ved å klikke på knappen "*Fortsett*" ved siden av "*Lagre gjenopprettingspassordet*".



![Image](assets/fr/06.webp)



Session vil da vise en Mnemonic-frase. Kopier den nøye og oppbevar den på et sikkert sted. Denne frasen gir deg full tilgang til Session-kontoen din, så det er viktig at du ikke avslører den. Du trenger den for å få tilgang til kontoen din på en annen enhet, spesielt hvis du mister eller bytter ut den nåværende telefonen.



![Image](assets/fr/07.webp)



Denne frasen fungerer på samme måte som Mnemonic-frasene som brukes i Bitcoin-porteføljer. Jeg anbefaler derfor at du leser denne andre veiledningen, der jeg forklarer de beste fremgangsmåtene for å lagre en Mnemonic-frase:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Vær oppmerksom på dette**: I motsetning til Mnemonic-fraser som brukes i Bitcoin-mapper, må du i Session **absolutt lagre hvert ord i sin helhet**. De fire første bokstavene er ikke nok!



## Sette opp Session-applikasjonen



For å få tilgang til applikasjonsinnstillingene klikker du på profilbildet ditt øverst til venstre i Interface. Her kan du legge til et profilbilde.



![Image](assets/fr/08.webp)



I "*Privacy*"-menyen kan du aktivere eller deaktivere ulike funksjoner (vær oppmerksom på at noen av dem kan avsløre din IP Address). Jeg anbefaler også å aktivere alternativet "*Lock App*", som krever autentisering for å få tilgang til applikasjonen.



![Image](assets/fr/09.webp)



I menyen "*Notification*" kan du velge mellom "*Fast Mode*" og "*Slow Mode*" (se tidligere deler av veiledningen). Du kan også tilpasse varslene slik at de passer til dine preferanser.



![Image](assets/fr/10.webp)



Til slutt kan du gå til menyen "*Utseende*" for å tilpasse Interface til din smak. I menyen "*Recovery Password*" kan du hente frem Mnemonic-frasen din hvis du ønsker å ta en ny sikkerhetskopi.



![Image](assets/fr/11.webp)



## Sende meldinger med Session



For å kontakte andre personer, klikk på "*+*"-knappen på hjemmesiden.



![Image](assets/fr/12.webp)



Flere alternativer er tilgjengelige. Hvis du ønsker å opprette eller bli medlem av en gruppe, velger du "*Opprett gruppe*" eller "*Bli medlem av fellesskap*".



![Image](assets/fr/13.webp)



Hvis du vil at noen skal legge deg til som kontakt, kan du få dem til å skanne økt-ID-en din som en QR-kode.



![Image](assets/fr/14.webp)



Hvis du vil sende innloggingen din eksternt, klikker du på "*Inviter en venn*". Deretter kan du kopiere økt-ID-en din og sende den via en annen kommunikasjonskanal. Du kan også hente denne informasjonen ved å klikke på profilbildet ditt på startsiden.



![Image](assets/fr/15.webp)



Hvis du har en annen persons økt-ID og ønsker å legge den til, klikker du på "*Ny melding*".



![Image](assets/fr/16.webp)



Deretter kan du lime inn identifikatoren i tekst, eller skanne den direkte hvis du har den som en QR-kode.



![Image](assets/fr/17.webp)



Send deretter en første melding til denne personen.



![Image](assets/fr/18.webp)



Så snart personen godtar forespørselen din, vil du se brukernavnet deres vises, og du vil kunne chatte fritt med dem.



![Image](assets/fr/19.webp)



## Synkroniser skrivebordsprogramvare



For å synkronisere kontoen din på datamaskinen din, må du installere programvaren. [Last den ned fra det offisielle nettstedet](https://getsession.org/download). Jeg anbefaler deg å sjekke ektheten og integriteten før du installerer den.



![Image](assets/fr/20.webp)



Ved første oppstart klikker du på "*Jeg har en konto*".



![Image](assets/fr/21.webp)



Skriv inn Mnemonic-frasen din, og sørg for å la det være et mellomrom mellom hvert ord.



![Image](assets/fr/22.webp)



Du kan nå få tilgang til samtalene dine fra datamaskinen din.



![Image](assets/fr/23.webp)



Gratulerer, du har nå fått taket på Session messaging, et utmerket alternativ til WathsApp!



Jeg anbefaler også denne andre opplæringen, der jeg presenterer Threema, et annet interessant alternativ for meldingsapplikasjonen din:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74