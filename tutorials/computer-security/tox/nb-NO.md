---
name: Tox
description: Åpne opp for samtaler uten mellomledd på den desentraliserte Tox-protokollen
---
![cover](assets/cover.webp)



Ende-til-ende-kryptering er en tjeneste som tilbys av mange meldingsapper som WhatsApp og Telegram. Kryptering her betyr at før meldingen sendes av avsenderen, er den sikret med en kryptografisk lås som bare mottakeren har nøkkelen til. I dag skal vi oppdage en helt desentralisert, ende-til-ende-kryptert meldingsapplikasjon, basert på prinsipper som ligner på Blockchain, for å tilby sikker, ende-til-ende-kryptert kommunikasjon uten mellomledd: Tox Chat.



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
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = ende-til-ende-kryptering*



## Hva er Tox?



Tox er en gratis (åpen kildekode), desentralisert kommunikasjonsprotokoll som bruker *Networking and Cryptography Library* (NaCl)-teknologi og kombinasjoner av krypteringsalgoritmer for å garantere brukernes sikkerhet og konfidensialitet. Med Tox kan du Exchange-tekstmeldinger, foreta lyd- og videosamtaler, dele filer og dele skjermen med venner på en sikker, desentralisert måte og uten mellomledd.



Teknologien som Tox-protokollen bruker, ligner på peer-to-peer-nettverk som for eksempel blokkjeder, noe som favoriserer desentralisering av protokollens infrastruktur. I motsetning til sosiale nettverk og ende-til-ende-krypterte meldingsapplikasjoner, er Tox Chat-applikasjonen bygget på en desentralisert protokoll som ikke har noen sentral server. Alle brukere kommuniserer i et mellommannsfritt, sensurresistent peer-to-peer-nettverk. For å kommunisere identifiseres hver bruker ved hjelp av en unik ID (ToxID) som er avledet fra hans eller hennes offentlige nøkkel, som lagres i en distribuert Hash-tabell.



## Bli med i Tox



Du kan bruke Tox-protokollen via en direktemeldingsklient som du kan laste ned fra [Tox Chat-nettstedet] (https://tox.chat).



![download](assets/fr/01.webp)



Avhengig av operativsystemet ditt kan du laste ned og installere en Tox-klient som samsvarer med:





- aTox: [aTox](https://github.com/evilcorpltd/aTox), en Tox-klient skrevet i Kotlin som kun er tilgjengelig på Android



![aTox](assets/fr/02.webp)





- qTox: En Tox-klient fra [åpen kildekode] (https://github.com/TokTok/qTox) basert på Qt Framework (C++) tilgjengelig på Windows, Linux, MacOs.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic) er en Tox-klient skrevet i C og kjører på systemer med kommandolinjegrensesnitt.



![Toxic](assets/fr/04.webp)



I denne veiledningen bruker vi qTox-klienter på Windows og aTox til å kommunisere.



## Kom i gang med qTox



Når du har lastet ned, installerer du Tox-klienten og oppretter profilen din.



![qTox-acount](assets/fr/05.webp)



Gratulerer, du har nettopp blitt medlem av Tox-protokollen. I qTox-programvaren finner du profilinformasjonen din ved å klikke på brukernavnet ditt.



![profil](assets/fr/06.webp)



Her finner du blant annet Tox-ID-en din, som du kan lagre som en QR-kode og dele med folk som ønsker å komme i kontakt med deg.



Eksporter Tox-profilfilfilen slik at du har en sikkerhetskopi av profilen og kontaktinformasjonen din som du kan bruke til å gjenopprette den. Klikk på knappen **Eksporter**, og velg deretter banen til sikkerhetskopifilen.



![export](assets/fr/07.webp)



Fra **More**-menyen kan du legge til venner, importere kontakter og administrere venneforespørsler du mottar.



![friends](assets/fr/08.webp)



Du kan for eksempel nå meg via denne Tox-ID-en: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Når venneforespørselen er sendt, må mottakeren godta eller avvise forespørselen din før du kan kontakte vedkommende.



![request](assets/fr/09.webp)



Tox-klienten inneholder alle alternativene som tilbys av direktemeldingsprogrammer:





- Videosamtaler





- Taleanrop





- Fildeling





- emojis



![chat](assets/fr/10.webp)



### Peer-to-peer-grupper



Tox-klientene dine gjør det også mulig for deg å kommunisere med en gruppe mennesker på en helt desentralisert måte: disse kalles konferanser. I menyen **Grupper** kan du opprette en ny konferanse eller se listen over invitasjoner til konferanser du har mottatt.



![conferences](assets/fr/11.webp)



Når konferansen er opprettet, kan du invitere vennene dine til å delta i konferansen på Tox-klienten din. Høyreklikk på brukernavnet til vennen du ønsker å invitere, i listen over venner. Klikk på alternativet **Inviter til konferanse**, og velg deretter konferansenavnet du har opprettet. Du kan også invitere en venn ved å opprette en konferanse implisitt med alternativet **Opprett en ny konferanse**.



⚠️ Tox-klienter er fortsatt under utvikling, så du kan støte på feil når du samhandler med programvaren. Konferanse- og videosamtalefunksjoner er ennå ikke tilgjengelige på Tox Android-klienten (aTox).



![invite](assets/fr/12.webp)



### Filoverføringer



I menyen **Filoverføringer** finner du en oversikt over filene du har sendt og filene du har mottatt fra kontaktene dine.



![files](assets/fr/13.webp)



Du kan også tilpasse konfigurasjonene for fildeling for hver diskusjon du har. Høyreklikk på mottakerens brukernavn og velg "Vis flere detaljer".



![details](assets/fr/14.webp)



Fra Interface-detaljer kan du administrere autorisasjonene du gir til mottakeren for:





- Automatisk aksept av konferanseinvitasjoner.





- Automatisk filaksept.





- Sikkerhetskopieringsstier for diskusjonsfilene dine.



![permissions](assets/fr/15.webp)



### Flere parametere



I menyen **Innstillinger** kan du tilpasse innstillingene for Tox-klienten din.





- I delen **Generelt** kan du endre det grunnleggende språket i Tox-klienten, definere stiene for sikkerhetskopiering av filer og den maksimale filstørrelsen som skal aksepteres automatisk.



![general](assets/fr/16.webp)





- I delen **Interface-bruker** kan du endre skrifttyper og størrelser på meldingene dine. Du kan også endre temaet for Tox-klienten.



![ui](assets/fr/17.webp)





- I **Privacy**-fanen kan du definere kortvarige meldinger ved å fjerne merket i boksen "Keep chat history". Du kan også endre Nospam-koden din når du merker at du blir spammet av venneforespørsler ved å klikke på "generate random NoSpam code"-knappen.



![privacy](assets/fr/18.webp)



### Hva garanterer konfidensialitet på Tox?



Tox-protokollen bruker Distributed Hash Table til å opprette et nettverk av desentraliserte noder. Hver Tox-klient er en del av DHT-nettverket og lagrer informasjon om andre noder. I Tox' tilfelle lagrer DHT IP-adresser som verdier knyttet til offentlige Tox-nøkler (Tox ID). Dette gjør det enkelt å søke etter en Tox Client-enhet uten å måtte spørre en sentral server.



Tenk deg at du skriver til brukeren vår `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F`, som vi kaller **bruker B**. Tox-klienten din vil finne denne identifikatoren i Hash Distributed-tabellen og hente den tilknyttede IP Address. Når IP Address er funnet, oppretter Tox-klienten en direkte, kryptert kommunikasjonskanal med maskinen til **bruker B**, eller bruker andre noder som reléer for å nå **bruker B**. Krypteringsalgoritmer sørger for at det uansett kommunikasjonskanal bare er **bruker B** som kan lese innholdet i meldingen din.



Hvis du har hatt glede av å oppdage Tox og har forstått hvordan det er nyttig for å styrke personvernet ditt, kan du gjerne gi denne veiledningen en tommel opp. Vi anbefaler også vår veiledning om Simple Login, et verktøy som lar deg motta og sende e-post anonymt.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41