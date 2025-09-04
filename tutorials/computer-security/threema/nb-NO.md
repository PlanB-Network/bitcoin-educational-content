---
name: Threema
description: Sikker, anonym direktemeldinger
---
![cover](assets/cover.webp)



Threema ble grunnlagt i 2012 i Sveits og er en direktemeldingsapp som er utviklet for å garantere personvern og sikkerhet. I motsetning til WhatsApp, Telegram eller Signal krever Threema ikke telefonnummer eller e-post Address for å opprette en konto. Hver bruker har en unik identifikator, noe som muliggjør fullstendig anonym registrering.



På den tekniske siden er kommunikasjonen over Threema kryptert fra ende til ende. Mobilapplikasjonskoden har vært åpen kildekode siden 2020, men serverinfrastrukturen er fortsatt proprietær og sentralisert. Serverne er utelukkende plassert i Sveits (et land som er kjent for sitt juridiske rammeverk for databeskyttelse).



![Image](assets/fr/01.webp)



Threema har grunnleggende klienter for Android og iOS. Det finnes også en nettapplikasjon, samt programvare for Windows, Linux og macOS. For å bruke dem må du imidlertid først registrere deg på en mobil enhet.



Threema-applikasjonen er ikke gratis. Den fungerer etter en engangsmodell: 5,99 euro for å bruke appen resten av livet (eller 4,99 euro hvis du kjøper den direkte). For å virkelig kunne bruke Threema anonymt, må betalingen også være anonym. Derfor kan du kjøpe en aktiveringsnøkkel i bitcoins eller kontanter på "*Threema Shop*" for å aktivere Android-versjonen. På iOS må kjøpet derimot gå gjennom App Store, på grunn av Apples restriksjoner på inntektsgenerering fra apper.



Det finnes også en egen forretningsversjon kalt "*Threema Work*". I denne veiledningen konsentrerer vi oss om hjemmeversjonen.



| Applikasjon          | E2EE 1:1       | E2EE grupper   | Anonym registrering | Åpen kildekode klient-lisens | Åpen kildekode server-lisens | Desentralisert server    | Opprettelsesår    |
| -------------------- | -------------- | -------------- | ------------------- | ---------------------------- | ---------------------------- | ------------------------ | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                            | ❌                            | ❌                        | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                            | ❌                            | ❌                        | 2011              |
| Facebook Messenger   | ✅              | 🟡 (valgfri)   | ❌                   | ❌                            | ❌                            | ❌                        | 2011              |
| Telegram             | 🟡 (valgfri)   | ❌              | 🟡                  | ✅                            | ❌                            | ❌                        | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                            | ❌                            | ❌                        | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                            | ✅                            | ❌                        | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                            | ❌                            | ❌                        | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                            | ✅                            | 🟡 (føderert)           | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                            | N/A                          | 🟡 (via e-post)         | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                            | ✅                            | 🟡 (føderert)           | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                            | ✅                            | ✅                        | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                            | ✅                            | ✅                        | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                            | ❌                            | 🟡(ingen katalog)      | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                            | N/A                          | ✅                        | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                            | N/A                          | ✅                        | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                            | N/A                          | ✅                        | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                            | N/A                          | ✅                        | 2013              |

*E2EE = ende-til-ende-kryptering*



## Installer Threema-applikasjonen



Threema er tilgjengelig på alle plattformer. Du kan laste ned applikasjonen direkte fra appbutikken på telefonen din:




- [Google Play] (https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold] (https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery] (https://appgallery.huawei.com/#/app/C103713829);
- [App Store] (https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



På Android er det også mulig å [installere via APK] (https://shop.threema.ch/en/download).



Det finnes også [datamaskinversjoner] (https://threema.ch/download) (MacOS, Linux og Windows). Denne veiledningen viser deg hvordan du synkroniserer dem.



## Kjøp Threema-lisens



Når du har installert applikasjonen, hvis du har gått direkte gjennom en appbutikk, har du allerede betalt for lisensen og bør ha umiddelbar tilgang til den. Hvis du gikk gjennom F-Droid eller APK, må du nå kjøpe en lisens på det offisielle nettstedet.



[Gå til "*Threema Shop*" (https://shop.threema.ch/) og klikk på "*Buy Threema for Android*"-knappen.



![Image](assets/fr/02.webp)



Velg antall lisenser du ønsker å kjøpe (bare én hvis det bare er til deg), velg valuta, og velg leveringsmetode for lisensen. Du kan velge å motta lisensen via e-post, eller direkte på nettstedet hvis du ønsker å være anonym. Klikk deretter på "*Fortsett til betaling*".



![Image](assets/fr/03.webp)



Velg betalingsmetode. I mitt tilfelle kommer jeg til å betale med bitcoins, noe jeg også anbefaler deg å gjøre, ettersom det lar deg forbli anonym (forutsatt at du bruker Bitcoin på riktig måte) og er mye mer praktisk enn en ekstern kontantbetaling. Klikk deretter på "*Neste*".



![Image](assets/fr/04.webp)



Hvis du ikke trenger en Invoice, klikker du på "*Neste*" igjen uten å oppgi noen personlige opplysninger.



Bekreft deretter kjøpet ved å klikke på "*Bekreft betaling*".



![Image](assets/fr/05.webp)



Deretter må du sende det angitte beløpet til Bitcoin Address (dessverre støttes ikke Lightning ennå). Når transaksjonen er bekreftet på Blockchain, klikker du på "*Lukk*" ved siden av Invoice.



Du vil da få tilgang til lisensnøkkelen din. Merk: Hvis du ikke har oppgitt en e-post Address, vil denne nøkkelen bare vises her. Husk å lagre URL-adressen til siden, slik at du kan få tilgang til den senere ved behov.



![Image](assets/fr/06.webp)



## Opprett en konto på Threema



Nå som du har lisensnøkkelen din, kan du endelig starte programmet. Hvis du ikke har kjøpt Threema via en applikasjonsbutikk, blir du ved første oppstart bedt om å skrive inn lisensnøkkelen du har kjøpt på nettstedet.



![Image](assets/fr/07.webp)



Klikk deretter på knappen "*Sett opp nå*".



![Image](assets/fr/08.webp)



Beveg fingeren over skjermen for å generate en kilde til entropi, som trengs for å lage din "*Threema ID*".



![Image](assets/fr/09.webp)



Din "*Threema ID*" vil da vises. Den gjør det mulig for deg å kontakte andre brukere. Klikk på "*Neste*".



![Image](assets/fr/10.webp)



Velg et passord. Det gjør at du kan gjenopprette tilgangen til kontoen din hvis det skulle bli nødvendig. Lag passordet så langt og tilfeldig som mulig, og oppbevar en sikker kopi av det, for eksempel i en passordbehandler.



![Image](assets/fr/11.webp)



Deretter velger du et brukernavn, som kan være enten ditt virkelige navn eller et pseudonym.



![Image](assets/fr/12.webp)



Du kan da koble Threema-ID-en din til telefonnummeret ditt. Dette gjør det enklere for deg å søke i kontaktene dine, men hvis du bruker Threema, er det også for å bevare anonymiteten din, så det er best å ikke koble den. Klikk på "*Neste*".



![Image](assets/fr/13.webp)



Når du har fullført dette trinnet, klikker du på "*Finish*".



![Image](assets/fr/14.webp)



Du er nå koblet til Threema og kan begynne å kommunisere.



![Image](assets/fr/15.webp)



## Sett opp Threema



Først går du til innstillingene ved å klikke på de tre små prikkene øverst i høyre hjørne, og deretter velger du "*Settings*".



![Image](assets/fr/16.webp)



I "*Privacy*"-fanen finner du flere alternativer som du kan tilpasse til dine behov:




- Synkronisere kontaktene på telefonen din ;
- Mottar meldinger fra ukjente personer;
- Skriveindikator under dataregistrering ;
- Melding om mottak av meldinger...



![Image](assets/fr/17.webp)



Under fanen "*Security*" anbefaler jeg at du aktiverer alternativet "*Locking mechanism*" for å beskytte tilgangen til applikasjonen. Det anbefales også å aktivere passphrase for å sikre lokale sikkerhetskopier.



![Image](assets/fr/18.webp)



Utforsk gjerne de andre delene av innstillingene for å tilpasse applikasjonen til dine preferanser.



![Image](assets/fr/19.webp)



## Sikkerhetskopiering av Threema-kontoen din



Før du begynner å utveksle meldinger, er det viktig å planlegge en måte å gjenopprette kontoen din på, spesielt hvis telefonen endres eller mistes. Dette gjør du ved å klikke på de tre prikkene øverst til høyre på Interface, og deretter gå til menyen "*Backups*".



![Image](assets/fr/20.webp)



Her finner du to alternativer for sikkerhetskopiering av dataene dine:




- "*Threema Safe*";
- "*Data Backup*".



"Threema Safe* lagrer all kontoinformasjonen din, bortsett fra samtalene dine, på Threemas servere. Disse dataene er kryptert med passordet du valgte da du opprettet kontoen din, slik at Threema ikke har tilgang til dem. Sikkerhetskopier tas automatisk og regelmessig.



Med "*Threema Safe*" trenger du bare å oppgi "*Threema ID*" og passordet ditt for å gjenopprette kontoen din på en ny enhet. Hvis en av disse to opplysningene mangler, vil det være umulig å gjenopprette kontoen din.



Med dette alternativet kan du bare hente frem ID, profil, kontakter, grupper og visse innstillinger, men **ikke samtalehistorikken**.



For å aktivere "*Threema Safe*", merker du bare av for alternativet i menyen "*Backups*".



![Image](assets/fr/21.webp)



Hvis du også ønsker å sikkerhetskopiere og gjenopprette samtalehistorikken din, må du bruke alternativet "*Data Backup*". Dette genererer en fullstendig sikkerhetskopi av kontoen din, lagret lokalt på telefonen din. Du må overføre denne sikkerhetskopien til den nye enheten din og bruke passordet ditt (og eventuelt passphrase) for å gjenopprette hele kontoen din.



Siden denne sikkerhetskopien bare er lokal, må den regelmessig kopieres til eksterne medier. Hvis ikke vil det være umulig å gjenopprette enheten hvis den går tapt. Denne metoden egner seg derfor best til en planlagt overføring fra én enhet til en annen, og ikke til nødsituasjoner.



Merk: "*Data Backup*" fungerer bare hvis du bruker det samme operativsystemet. Du kan for eksempel ikke bruke den til å migrere fra en Samsung til en iPhone.



## Tilpass Threema-profilen din



Klikk på profilbildet ditt øverst i venstre hjørne av Interface, og velg deretter "*Min profil*".



![Image](assets/fr/22.webp)



Her kan du tilpasse profilen din: legge til et bilde, velge hvem som kan se den, eller se Threema-påloggingen din.



![Image](assets/fr/23.webp)



## Synkroniser PC-programvare



Hvis du vil ha tilgang til samtalene dine på PC-en din, kan du synkronisere Threema-kontoen din med den dedikerte programvaren. Last ned programvaren for operativsystemet ditt [fra det offisielle nettstedet] (https://threema.ch/en/download).



![Image](assets/fr/24.webp)



Klikk på de tre prikkene øverst til høyre på telefonen, og åpne deretter menyen "*Threema 2.0 for Desktop*".



![Image](assets/fr/25.webp)



Klikk på "*Add device*", og bruk deretter telefonen til å skanne QR-koden som vises av programvaren på datamaskinen.



![Image](assets/fr/26.webp)



For å bekrefte synkroniseringen klikker du på emoji-gruppen som vises i programvaren.



![Image](assets/fr/27.webp)



Logg inn med passordet ditt på datamaskinen din.



![Image](assets/fr/28.webp)



I tillegg til mobilapplikasjonen kan du nå få tilgang til Threema-kontoen din direkte fra datamaskinen din.



![Image](assets/fr/29.webp)



## Sende meldinger med Threema



Nå som alt er riktig konfigurert, kan du begynne å kommunisere. Klikk på knappen "*Start chat*".



![Image](assets/fr/30.webp)



Velg "*Ny kontakt*".



![Image](assets/fr/31.webp)



Skriv inn eller skann korrespondentens "*Threema ID*".



![Image](assets/fr/32.webp)



Klikk på meldingsikonet.



![Image](assets/fr/33.webp)



Send en første melding til korrespondenten din.



![Image](assets/fr/34.webp)



Når korrespondenten din svarer, opprettes forbindelsen, og du kan se navnet og profilbildet hans eller hennes. Deretter kan du sende Exchange-meldinger, multimediefiler og til og med ringe.



![Image](assets/fr/35.webp)



Gratulerer, du er nå i gang med å bruke Threema messaging, et flott alternativ til WathsApp! Hvis du synes denne veiledningen var nyttig, vil jeg være veldig takknemlig hvis du legger igjen en Green-tommel nedenfor. Del gjerne denne veiledningen på dine sosiale nettverk. Tusen takk skal du ha!



Jeg anbefaler også denne andre veiledningen, der jeg introduserer deg for Proton Mail, et mye mer personvernvennlig alternativ til Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2