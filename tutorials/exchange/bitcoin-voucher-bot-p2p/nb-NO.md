---
name: BitcoinVoucherBot P2P
description: Hvordan kjøpe og selge Bitcoin P2P med BitcoinVoucherBot
---

![image](assets/cover.webp)



Vi hører fortsatt om BitcoinVoucherBot, en Telegram-bot opprettet for å kjøpe Bitcoin uten [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) via SEPA-bankoverføring. Dessverre er BitcoinVoucherBot i sin sentraliserte form fra og med november 2025 ikke lenger tilgjengelig som en tjeneste uten KYC.



I denne guiden vil vi se på hvordan den nye implementeringen fungerer som gjør det mulig for brukere å kjøpe og selge Bitcoin direkte på den nye P2P (Peer-To-Peer)-markedsplassen, så ingen KYC. For å motvirke nye restriksjoner som i økende grad truer digital frihet og personvern, skapte utviklerne denne utvidelsen, noe som gir brukerne muligheten til å kjøpe og selge Bitcoin med en høy grad av anonymitet gjennom P2P (Peer-To-Peer). La oss sammen se hvordan denne nye utvekslingsmetoden fungerer.



For å bruke tjenesten må du foreta overføringer via Lightning Network. Sørg derfor for at du har en wallet som støtter denne protokollen og lar deg bruke en "LNURL" eller "Lightning Address" til å motta og sende penger.



Blant de støttede lommebøkene kan vi finne:





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Custodial)
- [Wallet av Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Forvaring med bytte til ikke-forvaring)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



Eller enhver wallet som har en "Lightning Address" og genererer en Bolt11-faktura. lommebøker som generate en Bolt12-faktura støttes ikke for øyeblikket. For mer informasjon, se definisjonen av [Bolt](https://planb.academy/resources/glossary/bolt).



I denne veiledningen vil vi bruke Wallet of Satoshi, siden den er enkel å bruke umiddelbart.



**Forsiktighetsregler**: Wallet of Satoshi er populær blant nybegynnere, men er depotbasert, med begrenset kontroll over midler; bruk den bare midlertidig, og overfør umiddelbart til en ikke-depotbasert for full suverenitet. Fra og med oktober 2025 inkluderer den en stabil selvforvaltende modus over hele verden på iOS/Android (oppdater appen), med autonome private nøkler, veksling mellom moduser, egendefinerte Lightning-adresser og seed 12-ord backup. Det er imidlertid fortsatt en midlertidig løsning frem til konsolidering, og wallet ikke-frihetsberøvende moden for langsiktig administrasjon foretrekkes.



Veldig bra! Nå kan vi begynne reisen vår, som vil veilede deg trinn for trinn i hvordan du oppretter kontoen din, håndterer kjøps- og salgskamper og bruker det begrensede området ditt.



## Wallet og innrullering



Hvis du ikke allerede har det installert på smarttelefonen din, kan du først laste ned Wallet of Satoshi.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Hvis du aldri har brukt Wallet of Satoshi før og ønsker å forstå hvordan det fungerer, foreslår jeg at du følger denne veiledningen, slik at du kan aktivere det på riktig måte og sikkerhetskopiere det på en trygg måte.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Nå som wallet er klar, kan du begynne å sende en liten mengde sats. Husk at for å fullføre registreringen på P2P-plattformen (Peer-To-Peer), må du sende 1000 sats som et kontrolltiltak: Dette er for å skape en barriere mot eventuelle angrep av typen fantommatch (svindel), og forhindre at noen registrerer seg uten spamfilter.



![image](assets/it/02.webp)



Vi kan nå åpne P2P (Peer-To-Peer)-plattformen for å fortsette med registreringen. Du kan logge inn fra stasjonære PC-er eller nettlesere på smarttelefoner, via Telegram BitcoinVoucherBot eller via .onion-lenker for å gi et enda større nivå av personvern.



hvis du velger å bruke Tor .onion-lenken, anbefaler jeg også "Tor Browser". Hvis du ikke kjenner til den ennå, kan du lese mer om den på denne lenken:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Nå velger du hvordan du vil nå plattformen.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Nettleser Smarttelefon](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Du blir omdirigert til hovedsiden.



trykk på "Get Starter" for å komme i gang med en gang



![image](assets/it/03.webp)



På neste skjermbilde må du velge et passord og skrive det inn (boks A), og deretter gjenta det (boks B). Jeg anbefaler at du umiddelbart lagrer dette passordet på et sikkerhetskopimedium, for eksempel på en sikker digital enhet som "Bitwarden":



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

eller lagre passordet ditt på et papirmedium (**advarsel**: dette er ikke en god løsning, men det er greit hvis det er ment som en midlertidig løsning).



Kryss av i bekreftelsesboksen der du oppgir at du ikke er en robot (boks C). Merk: Ikke aktiver RSA-kryptering med mindre du vet nøyaktig hva det er og hvordan det fungerer. Du trenger ikke å gjøre noe på dette stadiet. Klikk på "Generate Avatar" ("Generer avatar") (boks D).



![image](assets/it/04.webp)



Nå må du betale 1000 sats for å fullføre registreringen.



1. Begynn fra toppen, og se først din tilfeldig genererte og ekstremt viktige "Avatar ID" Lagre den nøye, akkurat som jeg rådet deg til å gjøre med passordet.


2. Du må deretter angi "Lightning Address" i feltet nedenfor. Dette vil gjøre det mulig for deg å motta betalinger hvis du kjøper Bitcoin, eller få refusjoner. Hvis du bruker Wallet eller Satoshi, vil du kunne kopiere din Address ved å klikke på motta.


3. Kryss av i bekreftelsesboksen der du bekrefter at du ikke er en robot.


4. Betal 1000 sats for å få tilgang til det begrensede området ditt. Hvis du ikke kan ramme den inn, kan du klikke på den med musen (på PC) eller trykke på den med fingeren (på nettleser/Telegram smarttelefoner) for å kopiere adressen som du må lime inn i Wallet of Satoshi og fullføre fakturabetalingen.



![image](assets/it/05.webp)



Dette er din LNURL Address.



![image](assets/it/06.webp)



Gratulerer!!! Du har opprettet din Avatar permanent, og du kan se sammendraget her. Nok en gang anbefaler jeg at du er nøye med å lagre både avataren og passordet ditt, slik jeg har foreslått tidligere.



Klikk på "I've saved my credentials, continue" (oversatt som: "Jeg har lagret legitimasjonen min, fortsett")



![image](assets/it/07.webp)



Du er nå i hjertet av plattformen, hvor du kan se alle handelskampene med deres detaljer. For en tydeligere visning, nedenfor vil du se bildene som ligger i nettstedet fra stasjonære datamaskiner.





- "Type" ("Type") definerer om det er et "salg" ("sell") eller et "kjøp" ("buy")
- "Amount" ("Beløp"): angir hvor mange sats brukeren selger hvis matchen er av typen "Sell", eller hvor mange Bitcoin brukeren er villig til å kjøpe hvis matchen er av typen "Buy".
- "BTC-pris med margin" ("BTC-pris med margin"): viser prisen som tar hensyn til marginen som brukes over den merkede verdien.
- "Margin" ("Margin") er den prosentandelen som legges til markedsprisen. Med et minustegn (-) får du en rabatt på markedsprisen, med et plusstegn (+) legges det til en premie på markedsprisen.
- "Method" ("Metode") angir hvilken metode brukeren foretrekker å bli betalt med.
- "Creator" er den unike avataren som brukeren bruker på plattformen.
- "Rep" (Reputation) Brukerens omdømme varierer fra -5 upålitelig til +5 ekstremt pålitelig.
- "Status" ("Status"): Angir statusen til kampen. I skjermbildet i eksempelet ser alle treffene ut til å være "Open" ("Åpne").
- "Expiration" ("Utløp"): viser hvor lang tid det er igjen før kampen utløper og avbrytes hvis ingen har valgt den.



![image](assets/it/08.webp)



Klikk på avataren din øverst til høyre for å få tilgang til profilen din.



![image](assets/it/09.webp)



Her kan du se Avatar-navnet ditt, bruker-ID, opprettelsesdato og omdømme, som vil reflektere positivt eller negativt på oppførselen din i forhandlinger.



![image](assets/it/10.webp)



I Innstillinger-delen kan du se "Lightning Address", som du oppga under registreringen, og endre den om nødvendig. Du har også muligheten til å opprette en offentlig nøkkel, som du som nevnt bare bør sette opp hvis du har de nødvendige ferdighetene. Den brukes til å kryptere meldingene du utveksler med motparten din direkte fra datamaskinen din.



Telegram-varslingsfunksjonen anbefales på det sterkeste. Ved å aktivere den vises en QR-kode som du kan ramme inn med Telegram-appen: på denne måten vil du motta varsler i sanntid om alle handlinger relatert til kampene dine, direkte i bot-chatten på Telegram.



![image](assets/it/11.webp)



Til slutt finner du henvisningsdelen, med inntektene som genereres av brukerne du har invitert. Herfra kan du bruke knappen for å dele lenken eller QR-koden din, og litt lenger ned kan du se en liste over treff for å spore omdømmet ditt sammen med den tilsvarende poengsummen.



![image](assets/it/12.webp)



## Opprett en bestilling for å kjøpe Bitcoin



Gå inn på Marketplace: fra hovednavigasjonslinjen, klikk på vognsymbolet "Marketplace" ("Marketplace") for å åpne ordreboken. start deretter en ny ordre: trykk på "Ny ordre" -knappen ("Ny ordre") for å starte prosessen.



![image](assets/it/13.webp)





- Angi bestillingsdetaljer:
- Velg alternativet "Kjøp Bitcoin"("Buy Bitcoin").
- Angi hvor mye sats du vil ha.
- Definer prismarginen (mellom -20 % og +20 % av markedsverdien).
- Velg betalingsmetode (Instant SEPA osv.).
- Angir foretrukket valuta.
- Bekreft bestilling: Klikk på "Opprett bestilling" ("Bekreft bestilling") for å gå videre til arkiveringsfasen.



![image](assets/it/14.webp)



Depositum kreves: Et depositum på 10 % av totalbeløpet, pluss et servicegebyr, kreves for å aktivere bestillingen.




- Innskuddsbetaling: Når bestillingen opprettes, genererer systemet automatisk en lynfaktura. Depositumet er kun midlertidig og refunderes når bestillingen er fullført.
- Hovedfunksjoner:
- Depositum: 10 % av bestillingsverdien.
- Serviceavgift: kostnad for bruk av plattformen.
- Tidsbegrensning: Du har 5 minutter på deg til å gjennomføre betalingen, ellers utløper transaksjonen.



![image](assets/it/15.webp)



Etter vellykket betaling vil ordren vises i boken og være synlig for alle brukere, som kan velge og akseptere den. For å opprette en salgsordre trenger du bare å klikke på "Selg Bitcoin" ("Sell Bitcoin"), angi mengden satoshi du ønsker å selge, angi marginen, velge betalingsmetode og valuta, og deretter fortsette med innbetalingen på 10 % som et depositum. Når du er ferdig, vil kampen din være synlig i listen.



![image](assets/it/16.webp)



## Slik aksepterer du en bestilling



1. Selgere kan se en liste over alle tilgjengelige bestillinger i boken.


2. Sjekk detaljene: Hver bestilling viser informasjon som f.eks:




  - Mengde av Bitcoin,
  - Margin på pris,
  - Betalingsmåte,
  - Brukeromdømme.



![image](assets/it/17.webp)



3. Klikk på bestillingen for å åpne hele arket med all informasjon.


4. Trykk på "Sell Bitcoin" ("Selg Bitcoin") for å godta forslaget.



![image](assets/it/18.webp)



## Depositum kreves av selger



Når bestillingen er akseptert, genererer systemet en faktura for betaling. Innskuddet inkluderer:



- Det totale beløpet for bestillingen,



- servicekommisjonen.



Innskuddet må betales innen den fastsatte fristen, ellers vil transaksjonen ikke bli bekreftet.



![image](assets/it/19.webp)



## Sende betalingsinstruksjoner



Etter at innskuddet er gjort, vil transaksjonen vises i selgerens personlige dashbord, som må oppgi detaljene til kjøperen for å fullføre betalingen i fiat-valuta.



1. Selgeren viser den aktive transaksjonen i panelet sitt.


2. Klikk på "Send betalingsinstruksjoner"


3. Legg inn all nødvendig informasjon for fiat-betalingen (IBAN, mottaker, adresse, årsak til betaling osv.).


4. Klikk på "Send Message" ("Send melding") for å overføre dataene til kjøperen.



![image](assets/it/20.webp)



## Betalingsprosedyre



Kjøperen mottar en melding i chatten på plattformen med alle nødvendige data for å utføre betalingen i fiat-valuta:




- Bankopplysninger: IBAN med navn og adresse til selgerens kontohaver.
- Nøyaktig beløp: eksakt fiat-beløp som skal overføres.
- Årsak/beskrivelse: tekst som skal inkluderes i transaksjonen.
- Tidsfrist: Frist for å fullføre betalingen.



Overføringen skjer utenfor P2P-systemet og må gjøres gjennom ens bankinstitusjon.



⚠️ **Viktig merknad:** bekreftelse på plattformen skal først gjøres etter at du faktisk har ordnet overføringen eller fiat-betalingen via banken din.



![image](assets/it/21.webp)



## Bekreftelse av betaling fiat



Dette trinnet er avgjørende for kjøperen og bør først utføres etter at man har kontrollert at betalingen faktisk er sendt.



1. Mottaksdata: Kjøperen har mottatt betalingsinstruksjoner fra selgeren.


2. Betalingsutførelse: fiat-overføring ordnes fra ens bankkonto.


3. Verifisering: Kontroller at operasjonen ble behandlet på riktig måte.


4. Bekreft på plattformen: Klikk på "Bekreft fiat-betaling"("Confirm fiat payment") på handelssiden.


Knappen "Confirm Payment fiat" vises i transaksjonsdelen og skal bare brukes etter at du har bekreftet at betalingen faktisk er sendt.



![image](assets/it/22.webp)



Det siste trinnet i prosessen er at selgeren bekrefter mottak av fiat-betalingen, og deretter frigjøres satssene til kjøperen.



![image](assets/it/23.webp)



## Konklusjon



I håp om at denne opplæringen vil hjelpe deg å bruke en ny metode for å handle Bitcoins eller til og med bare kjøpe dem, enten for din egen butikk av verdi eller for å begynne å bringe daglige betalinger til liv. Likevel er det fortsatt en dør å utforske for å takle det som er i ferd med å skje i vår digitale verden.



Løkken som drives av organene som kontrollerer oss strammes, for å føde et stadig mer kontrollert internett. Ved å kjøpe P2P vil du holde kjøpene dine i total anonymitet, uten å etterlate spor og ingen oppfølgingsreaksjoner fra tredjeparter.