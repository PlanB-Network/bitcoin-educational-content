---
name: SMS4Sats
description: Motta og send SMS anonymt ved å betale i Bitcoin Lightning
---

![cover](assets/cover.webp)



SMS-bekreftelse har blitt et must for mange nettbaserte tjenester. Enten det er for å opprette en konto på en plattform, validere en registrering eller bekrefte en identitet, krever nettsteder nesten systematisk et telefonnummer. Denne utbredte praksisen utgjør et stort problem for alle som ønsker å bevare personvernet sitt: Personnummeret ditt blir en permanent identifikator som knytter de ulike digitale aktivitetene dine til din virkelige identitet og åpner døren for uønskede kommersielle henvendelser.



**SMS4Sats** løser dette problemet ved å tilby midlertidige telefonnumre for mottak og sending av SMS-meldinger. Tjenesten skiller seg ut med sin modell uten registrering og eksklusive Bitcoin-betaling via Lightning Network. For noen få satoshier får du et engangsnummer som gjør at du kan validere en registrering uten å oppgi personnummeret ditt.



Denne veiledningen guider deg gjennom de tre SMS4Sats-funksjonene: motta en bekreftelses-SMS, sende en anonym SMS og leie et midlertidig nummer i flere timer.



## Hva er SMS4Sats?



SMS4Sats er en nettbasert tjeneste tilgjengelig på [sms4sats.com](https://sms4sats.com), som muliggjør anonym SMS-håndtering via betaling i Bitcoin Lightning. Tjenesten tilbyr tre forskjellige funksjoner: mottak av verifiseringskoder til engangsbruk, sending av SMS til et hvilket som helst nummer og leie av midlertidige numre i flere timer.



### Filosofi og driftsmodell



Prosjektet er utformet for å sikre maksimal konfidensialitet og økonomisk suverenitet. Ved å ikke kreve opprettelse av konto og kun akseptere Bitcoin Lightning-betalinger, eliminerer SMS4Sats fullstendig behovet for å oppgi personopplysninger. Ingen e-postadresse, ingen kredittkort, ingen personlig informasjon er nødvendig. Kun Lightning-betaling kreves for å få tilgang til tjenestene.



Tjenesten støtter over 400 nettsteder og applikasjoner i rundt 120 land, noe som dekker de fleste vanlige verifiseringsbehov. Denne omfattende geografiske dekningen gjør det mulig å validere registreringer på en rekke ulike plattformer, fra sosiale nettverk til meldingstjenester.



### Betinget betalingsmodell



SMS4Sats bruker betingede lynfakturaer (hodl-fakturaer) for SMS-mottaksfunksjonaliteten. Denne mekanismen sikrer at du kun blir belastet hvis SMS-en faktisk blir mottatt. Hvis ingen melding ankommer innen den tildelte tiden (maksimalt 20 minutter), blir betalingen automatisk kansellert, og satoshiene returneres til din wallet. Denne garantien gjelder ikke for sende- og leiefunksjoner, som ikke kan refunderes.



## De tre SMS4Sats-funksjonene



SMS4Sats-grensesnittet er organisert rundt tre faner som tilsvarer tre forskjellige bruksområder: **RECEIVE** for å motta bekreftelseskoder, **SEND** for å sende anonyme SMS, og **RENT** for å leie et midlertidig nummer.



### Motta en SMS



Hovedfunksjonen lar deg få et midlertidig nummer for å motta en unik bekreftelseskode. Når koden er mottatt og brukt, deaktiveres nummeret permanent.



### Send en SMS



Med denne funksjonen kan du sende en SMS til et hvilket som helst telefonnummer uten å avsløre identiteten din. Mottakeren vil motta meldingen fra et anonymt nummer.



### Lei et skuespill



For brukere som har behov for å motta flere SMS-meldinger på ett enkelt nummer, tilbyr SMS4Sats et midlertidig leiealternativ. Dette alternativet lar deg motta og sende flere meldinger i løpet av leieperioden.



**Merknad om priser** : Prisene som vises i denne veiledningen er veiledende. De varierer avhengig av hvilket land nummeret kommer fra, hvilken tjeneste som er målet, og den aktuelle etterspørselen. For eksempel kan en SMS til Telegram Frankrike koste mellom 1 500 og 5 000 satoshis, avhengig av forholdene. Sjekk alltid det nøyaktige beløpet på lynfakturaen før du betaler.



## Motta en bekreftelses-SMS



La oss se nærmere på hvordan du bruker SMS4Sats til å motta en bekreftelseskode, illustrert ved opprettelsen av en Telegram-konto.



### Trinn 1: Velg land og tjeneste



Gå til [sms4sats.com](https://sms4sats.com) og hold deg på **RECEIVE**-fanen. Velg landet til ønsket nummer fra rullegardinmenyen. Hvis måltjenesten for abonnementet ditt er oppført, velger du den for å optimalisere sjansene for mottak.



![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)



I dette eksempelet velger vi Frankrike som land og Telegram som måltjeneste. Klikk på **NEXT** for å gå videre til neste trinn.



### Trinn 2: Betal lynfakturaen



En lynfaktura vises i form av en QR-kode. Beløpet varierer avhengig av hvilket land og hvilken tjeneste du har valgt. Skann QR-koden med Lightning wallet, eller kopier fakturaen for å betale manuelt.



![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)



Legg merke til den viktige meldingen: "Ingen SMS-kode = ingen betaling". Hvis du ikke mottar en SMS, blir betalingen automatisk kansellert og refundert innen maksimalt 20 minutter.



### Trinn 3: Få det midlertidige nummeret



Når betalingen er bekreftet, vises det midlertidige telefonnummeret umiddelbart. En teller viser hvor lang tid det er igjen til du mottar SMS-en.



![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)



Kopier dette nummeret (her +33 7 74 70 09 66) for å bruke det på den tjenesten du ønsker å registrere deg for.



### Trinn 4: Bruk nummeret på måltjenesten



Skriv inn det midlertidige nummeret i applikasjonen eller på nettstedet der du oppretter kontoen din. I vårt Telegram-eksempel skriver du inn nummeret, bekrefter det og venter på bekreftelseskoden.



![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)



Prosessen er identisk med konvensjonell registrering: du skriver inn nummeret, Telegram sender en bekreftelseskode via SMS, og deretter fullfører du kontoopprettelsen.



### Trinn 5: Hent bekreftelseskoden



Gå tilbake til SMS4Sats-grensesnittet. Så snart SMS-en er mottatt, vises aktiveringskoden automatisk. Klikk på **KOPIER KODE** for å kopiere den enkelt.



![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)



Tast inn denne koden på måltjenesten for å fullføre registreringen. Det midlertidige nummeret deaktiveres deretter permanent.



## Send en anonym SMS



SMS4Sats lar deg også sende SMS-meldinger til et hvilket som helst nummer uten å avsløre identiteten din.



### Trinn 1: Skrive meldingen



Klikk på fanen **SEND**. Skriv inn destinasjonstelefonnummeret med internasjonal kode, og skriv meldingen din (maks. 1600 tegn).



![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)



Klikk på **NESTE** for å gå videre til betaling.



### Trinn 2: Betal og send



Betal lynfakturaen som vises. Når betalingen er bekreftet, sendes SMS-en umiddelbart til mottakeren.



![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)



En bekreftelseskode vises for å bekrefte at meldingen er sendt. Mottakeren vil motta SMS-en fra et anonymt nummer.



## Lei et midlertidig nummer



For bruk som krever flere SMS-meldinger på samme nummer, kan du med RENT-funksjonen leie et nummer i flere timer.



### Konfigurasjon for utleie



Klikk på fanen **RENT**. Velg land og varighet.



![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)



**Viktige punkter å merke seg:**




- Prisene varierer avhengig av land og oppholdets lengde
- Leie kan ikke refunderes**, i motsetning til SMS-meldinger for engangsbruk
- Leide numre fungerer vanligvis ikke med Telegram
- Dette alternativet er egnet for å abonnere på flere tjenester etter hverandre



Når du har klikket på **NESTE** og betalt lynfakturaen, får du et nummer som du kan bruke så lenge leieperioden varer til å motta og sende SMS-meldinger.



## Fordeler og begrensninger



### Høydepunkter



**Ingen personopplysninger kreves**: Modellen uten registrering garanterer at ingen personopplysninger samles inn.



**Tre tilleggsfunksjoner**: Motta, sende og leie dekker de fleste behov.



**Kun betaling i Bitcoin** : Lightning Network tillater umiddelbare og pseudonyme transaksjoner.



**Automatisk tilbakebetaling**: Når du mottar SMS-meldinger, garanterer hodl-fakturasystemet at du bare betaler hvis SMS-en kommer frem.



### Begrensninger å ta hensyn til



**Relativ SMS-kanalsikkerhet**: SMS-koder er ikke en robust autentiseringsmetode og bør ikke brukes til sensitive kontoer.



**Variabel kompatibilitet**: Mange nettsteder oppdager og blokkerer virtuelle numre. Flere forsøk kan være nødvendig.



**Nummer som ikke kan gjenbrukes**: Etter engangsbruk resirkuleres nummeret og kan ikke gjenvinnes.



**Ikke-refunderbar leie**: I motsetning til engangs-SMS-meldinger, kommer ikke leie med en pengene-tilbake-garanti.



## Beste praksis



### Bruk Tor for mer personvern



SMS4Sats er tilgjengelig via [Tor](sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion). Denne konfigurasjonen maskerer IP-adressen din når du får tilgang til tjenesten.



### Unngå kritiske kontoer



Bruk aldri et engangsnummer til viktige kontoer (bank, hoved-e-post). Hvis disse plattformene krever at du validerer nummeret ditt på nytt på et senere tidspunkt, vil du miste tilgangen til kontoen.



### Skill de digitale identitetene dine



For pseudonyme kontoer kan du kombinere det midlertidige nummeret med en engangs-e-postadresse og en nettleser som er isolert fra det du vanligvis bruker.



### Velg en robust 2FA



Når kontoen din er opprettet, aktiverer du sterkere autentiseringsløsninger: TOTP-applikasjon (Aegis, Ente Auth) eller fysisk sikkerhetsnøkkel FIDO2.



## Konklusjon



SMS4Sats er en komplett løsning for konfidensiell SMS-håndtering. Enten du ønsker å motta en bekreftelseskode, sende en anonym melding eller leie et midlertidig nummer, oppfyller tjenesten et bredt spekter av konfidensialitetsbehov, takket være betaling i Bitcoin Lightning.



Vær imidlertid oppmerksom på begrensningene: Tjenesten garanterer ikke absolutt anonymitet, og egner seg ikke for sensitive eller langvarige kontoer. Brukt med omtanke og med en bevissthet om begrensningene, er SMS4Sats et praktisk verktøy for å gjenvinne kontrollen over telefonkommunikasjonen din.



## Ressurser





- [SMS4Sats offisielle nettsted](https://sms4sats.com)
- [Ofte stilte spørsmål om tjenesten](https://sms4sats.com/faq)
- [Tor-adresse](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)