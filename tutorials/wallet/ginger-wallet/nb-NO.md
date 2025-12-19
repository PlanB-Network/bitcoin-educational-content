---
name: Ginger Wallet
description: Bitcoin wallet-programvare med åpen kildekode, fork fra Wasabi Wallet, integrering av Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet er en åpen kildekode-portefølje med fokus på konfidensialitet og personvern. Den startet som fork fra Wasabi Wallet (etter versjon 2.0.7.2 - MIT-lisens).



Ginger Wallet beholder Wasabis tekniske arkitektur, men legger til noen få spesifikke funksjoner. Ifølge [Ginger Wallet-dokumentasjonen](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet) legger Wasabi vekt på **autonomi og kontroll**, mens Ginger fokuserer på **brukervennlighet, sikkerhet og en forenklet opplevelse**, noe som gjør den tilgjengelig for dem som er mindre kjent med tekniske aspekter.



Ginger Wallet er wallet-programvare kun for datamaskiner (ingen mobilapplikasjon).



## Hva er Coinjoin?



**coinjoin** er en spesiell Bitcoin-transaksjonsstruktur som samler flere deltakere i én enkelt samarbeidstransaksjon. Denne mekanismen blander oppføringene til forskjellige brukere i en felles transaksjon, noe som gjør det ekstremt vanskelig - om ikke umulig, hvis det gjøres på riktig måte - å spore midler. Som et resultat blir det nesten umulig for en utenforstående observatør å identifisere opprinnelsen og destinasjonen til de involverte bitcoinsene med sikkerhet, i motsetning til i konvensjonelle Bitcoin-transaksjoner.



For deg som bruker bidrar coinjoin til å bevare konfidensialiteten din. Hvis du for eksempel mottar en donasjon på 10 000 sats på en Bitcoin-adresse, kan avsenderen spore disse midlene og, i noen tilfeller, utlede at du har en større mengde bitcoins, eller observere aktivitetene dine. Ved å foreta en coinjoin etter denne donasjonen på 10 000 sats, bryter du sporbarheten: Avsenderen vil ikke lenger kunne utlede noen informasjon om deg fra denne betalingen.



Chaumian coinjoin tilbyr et høyt sikkerhetsnivå, ettersom midlene til enhver tid er under brukerens eksklusive kontroll. Selv operatørene av de koordinerende serverne kan ikke under noen omstendigheter omdirigere deltakernes bitcoins. Hverken brukere eller koordinatorer trenger å stole på hverandre: Hver av dem beholder kontrollen over sine private nøkler, og er alene autorisert til å validere transaksjoner. Ingen tredjepart kan derfor tilegne seg bitcoinsene dine under en coinjoin, eller etablere en direkte kobling mellom dine input og output.



Hvis du vil lære mer om coinjoin, kan du sjekke ut Plan ₿ Academy's BTC 204-kurs :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Installer Ginger Wallet



For å installere Ginger Wallet, besøk nettstedet [Ginger Wallet](https://gingerwallet.io).



Trykk på **Last ned** for å laste ned den riktige versjonen for din datamaskin (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Et annet alternativ er å gå til prosjektets [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) for å laste det ned.



![screen](assets/fr/04.webp)



Kjør deretter installasjonsprogrammet.



![screen](assets/fr/05.webp)




## Parameterinnstillinger



### Foreløpige konfigurasjoner



Åpne Ginger Wallet, velg ønsket språk.



![screen](assets/fr/06.webp)



Helt fra starten av minner Ginger deg på kostnadene som er forbundet med coinjoin-prosessen.



![screen](assets/fr/07.webp)



Trykk deretter på **Start** og deretter på **Ny** for å opprette en ny portefølje.



![screen](assets/fr/08.webp)



Lagre og bekreft deretter seedphrase.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



For ekstra sikkerhet gir Ginger Wallet deg muligheten til å legge til en passphrase.



![screen](assets/fr/11.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Når denne passphrase-en er lagt til, blir du bedt om å oppgi den hver gang du prøver å få tilgang til porteføljen din.



![screen](assets/fr/12.webp)



Ginger aktiverer automatisk standardinnstillingen **Coinjoin** når du oppretter porteføljen din. Du blir informert om dette og kan deretter tilpasse innstillingen slik at den passer dine behov.



![screen](assets/fr/13.webp)




### Generelle innstillinger



Når du har opprettet din første portefølje, kommer du til Ginger Wallet-grensesnittet.



![screen](assets/fr/14.webp)



Aktiver **Diskret modus** hvis du ønsker å skjule saldoen i lommebøkene dine.



![screen](assets/fr/15.webp)



Du kan opprette flere porteføljer på Ginger Wallet. Bare klikk på **Legg til en portefølje**.



![screen](assets/fr/16.webp)



Ginger støtter bruk av maskinvareporteføljer via standard Bitcoin Core-grensesnittet, selv om direkte integrering fra eller til en maskinvareportefølje ennå ikke er tilgjengelig.



Kompatibel maskinvareportefølje inkluderer (men er ikke begrenset til) :




- Blockstream Jade
- Coldcard MK4
- Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor modell T
- Trezor Safe 3
- osv.



Klikk nå på **Innstillinger**.



![screen](assets/fr/17.webp)



Disse innstillingene gjelder for applikasjonen generelt, og konfigurasjonene du gjør der, vil gjelde for alle porteføljer.



I **Innstillinger** har du fanene :





- Generelt**



![screen](assets/fr/18.webp)





- Utseende



I denne fanen kan du blant annet endre språk, valuta og visningsenhet for gebyr (BTC/Satoshi).



![screen](assets/fr/19.webp)





- Bitcoin**



I denne fanen kan du aktivere Bitcoin Knots til å kjøre ved oppstart av programmet, velge nettverk (Main/RegTest) og leverandør av ladetakst (Mempool Space/Blockstream info/Full Node), osv.



![screen](assets/fr/20.webp)





- Sikkerhetsfunksjoner



I Sikkerhet-fanen kan du aktivere tofaktorautentisering, aktivere eller deaktivere Tor og til og med deaktivere det når Ginger-applikasjonen er lukket.



![screen](assets/fr/21.webp)



**NB** :




- For tofaktorautentisering må du sørge for at autentiseringsprogrammet ditt støtter SHA256-protokollen og 8-sifrede koder. Ginger Wallet krever en 8-sifret 2FA-kode for å forbedre sikkerheten. Dette lengre formatet gjør koden mye vanskeligere å gjette eller kompromittere, noe som gir bedre beskyttelse mot uautorisert tilgang.
- Som standard går all nettverkstrafikk i Ginger gjennom Tor, noe som eliminerer behovet for manuell konfigurasjon. Hvis Tor allerede er aktivt på systemet ditt, vil Ginger automatisk gi det prioritet.



Men når du deaktiverer Tor i innstillingene, er personvernet ditt i utgangspunktet ivaretatt, bortsett fra i to situasjoner:




- under en Coinjoin, kan koordinatoren koble inn- og utdataene dine til IP-adressen din;
- når du sender en transaksjon, kan en ondsinnet node som du kobler deg til, knytte transaksjonen til din IP.



Ikke glem å trykke på **Done** (nederst i høyre hjørne) hver gang for å lagre innstillingene. Noen innstillinger krever at Ginger Wallet startes på nytt for å tre i kraft.



I tillegg kan du bruke søkefeltet øverst i porteføljene til å søke etter og få tilgang til alle parametere osv.



![screen](assets/fr/22.webp)




### Konfigurasjon av porteføljen



Det er mulig å opprette flere porteføljer i programmet, slik at hver portefølje kan konfigureres etter dine behov. Dette gjør du ved å klikke på de **tre prikkene** foran porteføljenavnet og deretter på **Porteføljeinnstillinger**.



![screen](assets/fr/23.webp)



Som du kan se, vil du i tillegg til wallet-parameteren kunne se UTXO-ene dine (listen over tokens du eier), statistikk og wallet-informasjon (for eksempel den utvidede offentlige nøkkelen).



Når du klikker på porteføljeparametere for å gå tilbake til porteføljekonfigurasjonen, kommer du til følgende faner:




- Generelt** (hvor du kan endre porteføljenavnet) ;



![screen](assets/fr/24.webp)





- Coinjoin** (hvor du kan tilpasse coinjoin-innstillingene for denne wallet) ;



![screen](assets/fr/25.webp)





- Verktøy** (der du kan sjekke seedphrase, synkronisere porteføljen din på nytt eller slette den).



![screen](assets/fr/26.webp)




## Motta bitcoins



![video](https://youtu.be/cqv35wBDWMQ)



For å motta bitcoins i din wallet på Ginger Wallet:




- trykk **Mottak** ;



![screen](assets/fr/27.webp)





- Skriv inn navnet på kilden som du ønsker å knytte adressen til. Dette er en merking for å holde oversikt over betalingene dine. Dette har ingen on-chain-implikasjoner; det er ganske enkelt sporbarhetsinformasjon som lagres lokalt i applikasjonen din;



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- klikk på den lille pilen til venstre for **Generate** for å velge adresseformat (**SegWit** /**Taproot**), og klikk deretter på **Generate** for å generate en adresse og QR-kode.



![screen](assets/fr/29.webp)



Denne adressen eller QR-koden vil bli brukt av avsenderen til å sende deg bitcoins.



![screen](assets/fr/30.webp)




## Send bitcoins




![video](https://youtu.be/2nf5aAimfhg)



For å gjøre dette :




- Trykk på **Send**-knappen;
- skriv inn mottakerens adresse, beløpet som skal sendes og en etikett;
- sjekk transaksjonsoversikten og bekreft at du vil sende.



![screen](assets/fr/31.webp)




## Bruk bitcoins



Det er enkelt å kjøpe og selge Bitcoin med Ginger Wallet. På bare noen få trinn kan du bruke bitcoinsene dine.



### Kjøp bitcoins



![video](https://youtu.be/lEqTBzm5MEA)



Ginger Wallet-brukere kan kjøpe bitcoins.





- Trykk på **Buy**-knappen. Denne knappen forblir synlig selv om wallet er tom.



![screen](assets/fr/32.webp)





- Velg ditt land, eller til og med din stat (i noen regioner, for eksempel Canada), før du fortsetter med et bitcoin-kjøp. Når du klikker på **Kjøp**-funksjonen for første gang, må du faktisk også spesifisere regionen din.



![screen](assets/fr/33.webp)



Trykk på **Fortsett** for å gå videre i kjøpsprosessen.





- Skriv deretter inn hvor mange bitcoins du ønsker å kjøpe i det dedikerte feltet. Du kan også velge transaksjonsvaluta.



![screen](assets/fr/34.webp)



Hver valuta har en minimums- og maksimumsgrense for kjøp. For eksempel er maksimumsgrensen i USD 30 000 USD.



Hvis du allerede har foretatt et kjøp, kan du se transaksjonshistorikken din ved å klikke på knappen **Tidligere bestillinger**. En liste over tidligere transaksjoner og deres status vises.





- Velg det tilbudet som passer best for deg.



Nå ser du en liste over alle tilgjengelige tilbud. For hvert tilbud har du :




 - leverandørnavn (1) ;
 - antall bitcoins som tilsvarer det tidligere angitte beløpet, betalingsmåten og kjøpsgebyret (2) ;
 - knappen **Accept** (3).



![screen](assets/fr/35.webp)



Gebyrene som er angitt i tilbudet, utgjør ikke en ekstra kostnad. De er allerede inkludert i det totale beløpet for tilbudet.



Øverst til høyre på skjermen, merket **Alle**, kan du filtrere tilbud etter betalingsmåte. Betalingsmåten du har valgt, er angitt som standard, men kan endres når som helst.



![screen](assets/fr/36.webp)



Hvis du finner et passende tilbud, klikker du på **Aksepter**-knappen for å gå videre med kjøpet. Du vil da bli omdirigert til selgerens side, hvor du kan fullføre transaksjonen.



### Selge bitcoins



Brukere av Ginger Wallet kan selge Bitcoin. Knappen **Sell** er bare synlig når det er tilgjengelige midler i porteføljen.





- Klikk på **Selg**.



![screen](assets/fr/37.webp)





- I likhet med **Buy**-alternativet må du velge land når du bruker salgsfunksjonen for første gang, før du kan gå videre med et bitcoinsalg.





- Deretter må du angi hvor mange Bitcoins du ønsker å selge. Du kan angi dette beløpet i BTC eller i en fiat-valuta, for eksempel amerikanske dollar (USD).





- Når du har gjort dette, vil du se en liste over tilgjengelige tilbud. Velg et tilbud som passer deg, og klikk deretter på **Aksepter** for å fortsette.





- Nå må du fullføre transaksjonen:
 - Når du har akseptert et tilbud, blir du sendt videre til leverandørens side;
 - Følg instruksjonene på leverandørsiden ;
 - På et tidspunkt vil du motta en mottakeradresse og det nøyaktige beløpet du skal sende;
 - Gå deretter tilbake til Ginger Wallet for å fortsette prosessen;
 - Når du er tilbake i Ginger Wallet, vises en dialogboks der du kan fortsette ved å klikke på **Send**.



Dette åpner **Send**-skjermbildet med mottakerens adresse og beløp forhåndsutfylt. Du kan også bruke **Send**-knappen på startskjermen. Selv om du kan sende transaksjonen manuelt, anbefaler vi at du fullfører den via dialogboksen for å optimalisere prosessen.



## Lage en coinjoin på Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Beskytt konfidensialiteten til bitcoinsene dine med **Coinjoin**, som er integrert direkte i Ginger Wallet. wallet bruker **WabiSabi**, en Chaumian coinjoin-protokoll som er utviklet for å legge til rette for mer tilgjengelige og effektive coinjoins.



Det er opp til deg å velge den coinjoin-strategien (automatisk eller manuell) som passer deg best.



Ginger Coinjoin er klar til bruk så snart du laster den ned (ingen ekstra trinn kreves). Ginger Coinjoin kjører automatisk i bakgrunnen for å beskytte personvernet ditt ved hver transaksjon. I praksis vil Coinjoin-spilleren dukke opp når du har en saldo som kan anonymiseres.



Når det gjelder manuell oppstart av coinjoin, er det en operasjon med ett klikk. Start runden og vent på at coinjoin-transaksjonen skal bygges og bekreftes. Du vil se anonymiseringspoengene i grensesnittet.



Du kan mikse flere ganger til ønsket nivå av anonymitet er nådd. Du kan også ekskludere visse deler fra miksen.



Som standard bruker Ginger sin egen koordinator med alle forhåndskonfigurerte parametere og garanterte avgifter. Coinjoins av tokens verdt mer enn 0,03 BTC påløper et koordinatorgebyr på 0,3% i tillegg til mining gebyret. Innføringer på 0,03 BTC eller mindre, samt remixer, er unntatt fra koordinatorgebyrer, selv etter en enkelt transaksjon. En betaling med Coinjoin-midler gjør det derfor mulig for både avsender og mottaker å remixe myntene sine uten å pådra seg koordinatoravgifter.



Ginger foretrekker coinjoins med flere deltakere fremfor mindre, raskere runder. Større coinjoins gir mer anonymitet, lavere kostnader og mer effektiv bruk av blokkplass.




## Sikkerhet og beste praksis



Ønsket om desentralisering og ivaretakelse av personvernet krever at man tar i bruk flere beste praksiser:




- seedphrase må alltid oppbevares på et trygt sted utenfor nettet;
- Hvis du mister datamaskinen din eller mistenker uautorisert tilgang, må du opprette en ny wallet umiddelbart. Overfør midlene dine til denne nye porteføljen og slett den gamle;
- Bruk en annen adresse for hvert mottak for å unngå gjenbruk av adresser;
- Last alltid ned porteføljeapplikasjonene dine utelukkende fra den offisielle GitHub-kontoen eller det offisielle nettstedet.



Nå er du kjent med hvordan du bruker Ginger Wallet-applikasjonen til å sende, motta og bruke bitcoins.



Hvis du fant denne opplæringen nyttig, vennligst la meg en grønn tommel nedenfor. Del gjerne denne artikkelen via dine sosiale medieplattformer. Tusen takk skal du ha!



Jeg foreslår også at du sjekker ut denne veiledningen om hvordan du bruker dataprogrammet Liana til å sende og motta bitcoins, samt implementere en automatisert eiendomsplan.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04