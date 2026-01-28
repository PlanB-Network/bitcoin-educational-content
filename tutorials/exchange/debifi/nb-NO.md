---
name: Debifi
description: Få et lån uten frihetsberøvelse garantert av Bitcoin.
---

![cover](assets/cover.webp)




## Innledning



I århundrer har tradisjonelle lån gjort det mulig å finansiere mange prosjekter. Men det er fortsatt tregt, kostbart og lite inkluderende, særlig for dem som ikke har tilgang til en solid bankinfrastruktur.



Fremveksten av Bitcoin-protokollen innledet en ny finansiell æra, og den førte med seg en rekke utfordringer. En av disse utfordringene var hvordan man skulle skaffe likviditet uten å bli tvunget til å selge Bitcoin, og dermed miste eksponeringen mot vekstpotensialet



Resultatet er **Debifi**, en plattform som posisjonerer seg som et moderne alternativ til bankene. Målet er klart: å gjøre kreditt så enkelt og gjennomsiktig som mulig, ved å kombinere fordelene ved det tradisjonelle finanssystemet med friheten som Bitcoin tilbyr. Navnet Debifi gjenspeiler denne visjonen: ***Decentralized Bitcoin Finance***, en sammentrekning som illustrerer møtet mellom desentralisert finans og Bitcoin-innovasjon.



Debifi er en Bitcoin-støttet utlånsplattform uten depot, noe som betyr at du beholder kontrollen over dine private nøkler. Den lar brukerne frigjøre likviditet i bytte mot låste bitcoins som sikkerhet. I motsetning til tradisjonelle banklån bruker Debifi et sperresystem med flere signaturer (3 av 4) og aksepterer ikke rehypothecation av sikkerhet, noe som garanterer større sikkerhet og gjennomsiktighet.



I praksis betyr dette at verken Debifi eller den enkelte långiver kan bruke dine BTC uten at tre parter (du, långiveren og en betrodd tredjepart) er enige om det. Dette gjør systemet sikrere: Hvis du låner på Debifi, beholder du eierskapet til dine Bitcoin til lånet er tilbakebetalt i sin helhet.



## Fordeler med Debifi



Med Debifi får du Bitcoin-støttede lån som er overpantsatt og sikret med on-chain. Pengene dine er trygge med lommebøker med flere signaturer, 2FA og total kontroll over dine Bitcoin - du holder nøklene dine, du holder myntene dine. Lån i en rekke stablecoins eller fiat-alternativer, til konkurransedyktige priser og global likviditet.



Her er en rask sammenligning mellom et Debifi-lån og et tradisjonelt banklån:


| Characteristics        | Loan via Debifi                                                        | Traditional Bank Loan                                                       |
| ---------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Accessibility          | ✔️ Open to any Bitcoin holder (even without banking history)           | ❌ Often limited to clients with physical collateral and strong records      |
| Speed of approval      | ✔️ Funds available within minutes or hours                             | ❌ Lengthy process (days or weeks)                                           |
| Required guarantees    | ✔️ Bitcoin used as the sole collateral                                 | ❌ Physical guarantees (property, land, stable income)                       |
| Asset control          | ✔️ You keep exposure to Bitcoin and its upside potential               | ❌ No connection between the loan and your financial assets                  |
| Geographic flexibility | ✔️ Available everywhere (no banking jurisdiction constraints)          | ❌ Restricted to the bank’s jurisdiction                                     |
| Main risk              | ❌ Liquidation risk if BTC price drops too sharply                      | ❌ Risk of asset seizure or negative impact on credit score                  |

Før jeg viser deg steg for steg hvordan du låner på Debifi, er det noen ting jeg mener du bør vite.




## Definisjoner





- Etableringsgebyr** er en engangsavgift som påløper ved innvilgelse av lån og beregnes som en prosentandel av lånebeløpet. Disse gebyrene dekker administrative, operasjonelle og forvaltningsmessige kostnader.





- Sikkerhet** er en eiendel du setter inn for å sikre et lån. I Debifis tilfelle er sikkerheten Bitcoin (BTC), som låntakeren deponerer i Multisig 3/4 escrow.





- Multisig escrow (3/4)**-systemet er en sikker innskuddsmekanisme der en låntakers bitcoins plasseres på en adresse med flere signaturer. Nærmere bestemt har fire (4) parter hver sin nøkkel (låntaker, långiver, Debifi, uavhengig tredjepart). For å flytte midler kreves minst 3 av 4 signaturer.





- En stablecoin** er en kryptovaluta hvis verdi er knyttet til en stabil eiendel (f.eks. amerikanske dollar), noe som gjør at man unngår volatiliteten til Bitcoin. For eksempel er 1 USDC alltid verdt ~ 1 USD, ettersom den er støttet av fiat-reserver.





- Belåningsgraden (Loan-to-Value (LTV)** for et lån avgjør hvor mye penger du kan låne som sikkerhet for Bitcoin. LTV-forhold = Lånebeløp / sikkerhetsbeløp * 100. For eksempel betyr en LTV på 50 % at verdien av lånet tilsvarer 50 % av verdien av den deponerte Bitcoin.




BTC Sessions videoopplæring :



![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)



## Kom i gang med Debifi



For å komme i gang med Debifi trenger du noen forutsetninger.


### Forutsetninger



Før du kan låne fra Debifi, må du sørge for at du har med deg følgende ting:





- Bitcoin wallet: hvor du oppbevarer BTC (ideelt sett ikke-depot, f.eks. Hardware Wallet eller en betrodd mobil wallet). Det er fra denne wallet at du sender Bitcoin-sikkerheten til Debifi og mottar sikkerheten tilbake.



Du kan bruke Aqua, en Bitcoin og Liquid wallet som også støtter USDT stablecoin-administrasjon på ulike nettverk. Eller COLDCARD (Mk4 eller Q), som for øyeblikket er den eneste maskinvaren som støttes av Debifi.



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3



- KYC (*Know Your Customer*): Avhengig av hvilket lånetilbud som er valgt, kan det være nødvendig med en identitetskontroll. På Debifi angir hvert tilbud om KYC er påkrevd eller ikke. Så forbered deg deretter. KYC utføres av pålitelige tredjepartsleverandører som Sumsub.



![image](assets/fr/03.webp)





- Applikasjon for tofaktorautentisering: Debifi krever en Authenticator-kode for alle viktige handlinger. Det er et ekstra sikkerhetslag. I denne veiledningen bruker vi Google Authenticator. Alternativt kan du bruke andre etter eget ønske.



https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc



- Debifis nettsted og mobilapplikasjon: Debifi er både et nettsted og en mobilapplikasjon, og de to fungerer sammen. Mobilappen blir en wallet, som lagrer den private nøkkelen din og administrerer signeringen av kontrakter. I tillegg må du bruke nettstedet til å inngå kontrakter (en stor Interface gir deg en generell oversikt over lånekontrakter og deres detaljer).





- Debifis mobilapp (iOS/Android) er nødvendig for å ta opp lån. Du må laste ned appen, opprette en konto og "linke" enheten din (registrere enheten til kontoen din). Debifi-appen støtter tofaktorautentisering (2FA), og uten smarttelefon kan du ikke bekrefte transaksjoner på Debifi.



### Opprett en konto



Besøk [Debifis offisielle nettsted](https://debifi.com/app).



![image](assets/fr/04.webp)



Installer applikasjonen i henhold til hvilken type smarttelefon du har, og åpne den.



![image](assets/fr/05.webp)



![image](assets/fr/06.webp)



Når du er inne i programmet, klikker du på menyen **Innstillinger**.



![image](assets/fr/07.webp)



Klikk deretter på **Logg inn eller opprett konto** for å opprette en konto med e-postadressen din.



![image](assets/fr/08.webp)



![image](assets/fr/09.webp)



![image](assets/fr/10.webp)



Du vil motta en bekreftelseskode på e-post. Kopier og lim inn denne koden i applikasjonen. Åpne deretter Debifi-applikasjonen på smarttelefonen din og logg inn.



![image](assets/fr/11.webp)



### Sikre kontoen din



For sikkerhets skyld vil Debifi be deg om å følge tre trinn.



![image](assets/fr/12.webp)





- Først må du angi en sterk PIN-kode for å få tilgang til applikasjonen din senere.



![image](assets/fr/13.webp)





- Deretter konfigurerer du tofaktorautentisering (2FA) for å knytte enheten din til kontoen din ved hjelp av 2FA-koden.



![image](assets/fr/14.webp)





- Til slutt må du lagre de 12 ordene i den private nøkkelen din ved å skrive den ned på et pålitelig medium og oppbevare den på et trygt sted. Denne fasen er avgjørende for å gjenopprette kontoen din og administrere pengene dine.



![image](assets/fr/15.webp)





- For ekstra sikkerhet kan du til og med legge til en passphrase.



![image](assets/fr/16.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Vær oppmerksom på at det kun er den registrerte smarttelefonen din som kan åpne kontoen din (et ekstra sikkerhetstiltak).



Når du har fullført disse trinnene, klikker du på menyen **Tilbud** for å se de tilgjengelige lånetilbudene. Når du klikker på et tilbud, blir du videresendt til Debifis nettsider.



![image](assets/fr/17.webp)



### Gå inn på nettstedet og utforsk lånetilbudene



Når enheten din er tilkoblet, går du til [Debifis nettsted](https://debifi.com/). Logg inn for å etablere en sikker forbindelse mellom Debifis mobilapplikasjon og nettplattformen. Dette gjør det enklere for deg å samhandle med tilgjengelige lånetilbud (en tydelig oversikt over detaljene i hvert tilbud) og administrere kontoen din.



![image](assets/fr/18.webp)



![image](assets/fr/19.webp)



![image](assets/fr/20.webp)



![image](assets/fr/21.webp)




Videoveiledning om hvordan du logger inn med kontoen din på plattformen :



![video](https://youtu.be/cUwCfTKDAOo)



## Lånesøknad



Plattformen setter deg i kontakt med likviditet av institusjonell kvalitet og tilbyr en rekke alternativer som passer dine behov. Bla gjennom for å finne ut hva som er tilgjengelig. Du har også fleksibilitet til å justere låneparametrene i henhold til din individuelle risikotoleranse og økonomiske situasjon.



![image](assets/fr/22.webp)



De fiat-valutaene Debifi tilbyr for øyeblikket, kan ses på plattformen.



![image](assets/fr/23.webp)



### Tydelige og fleksible kontraktsklausuler



Debifi baserer seg på transparente og fleksible lånevilkår for å imøtekomme behovene til begge parter (långiver og låntaker). Viktige klausuler inkluderer :



#### Belåningsgrad i forhold til verdi (LTV)


Bitcoin-lånetransjer er vanligvis tre (3) i antall:





- Konservative lån (30-40 % belåningsgrad), som tilsvarer et lavrisikolån, er ideelle for å maksimere sikkerheten mot prisvolatilitet i Bitcoin;





- Balansert (50 % belåningsgrad) ;





- Aggressive (70 % belåningsgrad), som gir større likviditet, men som innebærer en svært høy risiko for likvidasjon i nedgangstider. Aktiv overvåking av markedsforholdene i Bitcoin er et must ved valg av denne transjen.



#### Rentesatser



Rentesettingen avhenger generelt av den valgte belåningsgraden, lånets løpetid, volatiliteten i sikkerheten og plattformspesifikke risikovurderinger. Rentene er faste i hele lånets løpetid.



#### Fleksibilitet i lånets løpetid og tilbakebetaling



Tilbakebetalingsplanene er fleksible og tilpasset låntakerens behov. Lånene kan tilbakebetales helt eller delvis når som helst uten ekstra gebyrer, forutsatt at kravene til sikkerhet fortsatt er oppfylt. I løpet av lånets løpetid betales rentene med jevne mellomrom, mens hovedstolen gjøres opp ved forfall.



#### Likvidasjonsrettigheter (Margin calls)



På grunn av Bitcoins volatilitet har lånene en klart definert policy for margin call. En margin call oppstår når belåningsgraden stiger på grunn av en nedgang i sikkerhetsverdien. Debifi varsler låntakeren via e-post og appen, slik at de kan legge til sikkerhet eller tilbakebetale deler av lånet.


75 % belåningsgrad - første varsel

80 % belåningsgrad - andre varsel

85 % belåningsgrad - siste varsel

90 % belåningsgrad - Sikkerheten er realisert



### Lansering av låneprosessen



Klikk på et lånetilbud som passer dine behov for å se funksjonene i det.



![image](assets/fr/24.webp)



Du kan se :


1. Navn på utlånsinstitusjon ;


2. Lånebeløpet varierer;


3. At du vil motta midlene i USDC Ethereum ;


4. Lånets løpetid, rentesats og belåningsgrad;


5. KYC er påkrevd for dette tilbudet;


6. Det nøyaktige beløpet du trenger, må oppgis (beløpet må ligge innenfor beløpsgrensen, se punkt 2);


7. Ethereum USDC-adressen som skal brukes til å motta pengene, må oppgis.



Når du er fornøyd med tilbudet og har fylt ut den nødvendige informasjonen, klikker du på "Contract-forespørsel".



![image](assets/fr/25.webp)



Gå tilbake til mobilapplikasjonen for "**Gi offentlig nøkkel**".



![image](assets/fr/26.webp)



Trykk på '' **Lever ut offentlig nøkkel** '', og velg deretter kilden til den offentlige nøkkelen. Långiveren må også oppgi en offentlig nøkkel.



![image](assets/fr/27.webp)



![image](assets/fr/28.webp)



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Neste trinn er å signere kontrakten. Fortsatt i mobilapplikasjonen trykker du på '' **Signer Contract** ''



![image](assets/fr/31.webp)



![image](assets/fr/32.webp)



Når du er ferdig med å signere kontrakten, oppretter Debifi automatisk en unik multisignatur Bitcoin-adresse (escrow 3-sur-4) for kontrakten din. Så lenge bitcoinsene dine er i escrow, kan de ikke brukes andre steder.



### Innskudd av garantien og mottak av pengene dine



Det siste trinnet er å deponere Bitcoin-sikkerheten din i multisignatur-sperresystemet. Debifi viser deg escrow-adressen (B) og mengden BTC (A) som skal sendes som (sikkerhet + provisjon).



![image](assets/fr/33.webp)



Du vil også motta dette varselet i mobilapplikasjonen din.



![image](assets/fr/34.webp)



Så snart innskuddet ditt er bekreftet, vil långiveren utbetale lånebeløpet til den mottakeradressen du har oppgitt, slik at transaksjonen fullføres og du får tilgang til de midlene du trenger.



Du vil da motta et varsel fra Debifi, der du blir bedt om å betale lånegebyrene eller provisjonene for å få status på lånet ditt.



Når kontrakten er opprettet, trekkes lånegebyrene automatisk fra sikkerheten som låntakeren har deponert på sperret adresse med flere signaturer.



Alt du trenger å gjøre er å signere en transaksjon som gjør at Debifi kan trekke sin provisjon fra garantien. Långiveren din må på sin side også signere transaksjonen for gebyrfradrag, ellers vil ikke Debifi kunne motta provisjonen sin.



![image](assets/fr/35.webp)



De gjeldende utlånsgebyrene er 1,5-2 %, avhengig av kontraktens løpetid. Plattformen krever kun provisjon i Bitcoin.



## Sporing av lån



Når lånet er aktivt, kan du følge med på kontrakten i sanntid. I grensesnittet finner du:



- Lånebeløp og gjenværende løpetid.
- Gjeldende LTV (Loan-to-Value), som stiger når prisen på BTC synker og verdien av sikkerheten din faller.




Låntakere blir varslet når sikkerhetsverdien synker, og denne informasjonen vises også på kontraktsoppsummeringssiden. For å gjenopprette den opprinnelige belåningsgraden må låntakeren enten



- stille ytterligere sikkerhet;
- tilbakebetale hele eller deler av gjelden.




Ved en eventuell økning i prisen på pantesikkerheten beholder låntakeren eventuelle kursgevinster på pantesikkerheten. Han skylder kun lånebeløpet, som er forhåndsbestemt og uavhengig av Bitcoin-prisen.




## Tilbakebetaling og gjenvinning av sikkerhetsstillelse



Ved utløpet av den avtalte løpetiden (eller tidligere, hvis du ønsker det) må du betale tilbake lånet.


I Debifi :





- Gå til kontrakten din og klikk på **Foreta en tilbakebetaling**. Angi det totale beløpet som skal betales (hovedstol + renter).





- Send stablecoins fra din wallet til långiverens adresse, og bekreft tilbakebetalingen på plattformen ved å kopiere **ID** for tilbakebetalingstransaksjonen inn i den dedikerte fanen. Dette gjør det enklere for Debifi å utføre sine kontroller.



Når betalingen er bekreftet av långiver (og av deg), vil Debifi be deg om å **refundere**. Din Bitcoin-sikkerhet frigjøres, og du kan returnere den fra sperringen til din egen wallet.  Ikke glem å samle inn alle dine Bitcoins.



Så snart du mottar bitcoinsene dine, endres lånekontrakten til **Contract fullført**.



Vi gratulerer! Du har fullført prosessen.




## Beste praksis og sikkerhet



Uansett hvilke mål du har eller hva som motiverer deg - finansiering av et prosjekt, kjøp av eiendom, kjøp av bitcoins osv. - bør du utvise stor forsiktighet før du tar opp et lån med Bitcoin som sikkerhet. Ta deg tid til å vurdere beslutningen nøye, ettersom Bitcoin fortsatt er en ustabil eiendel. **Et kraftig prisfall kan føre til tvangslikvidasjon av bitcoinsene dine



Overvåk forholdet mellom lån og sikkerhet (LTV). Sett opp varsler (BTC-pris, LTV) hvis mulig. Ikke la belåningsgraden nærme seg 90 %. Hvis du er i tvil, kan du øke sikkerheten eller tilbakebetale tidlig.



Kontroller nøklene dine. Oppbevar BTC i en sikker wallet (ideelt sett maskinvare eller en anerkjent wallet). Ikke angi en PIN-kode knyttet til en viktig dato i livet ditt, og del aldri gjenopprettingsfrasen din. På Debifi generate du din private nøkkel i applikasjonen - Debifi kjenner den ikke.



Begynn i det små om mulig. Ved ditt første lån bør du teste et beskjedent beløp for å gjøre deg kjent med prosessen.



Bruk kun Debifis offisielle nettsider for å holde deg oppdatert på nyheter fra Debifi, og unngå ukjente lenker eller phishing-lenker.  Oppdater applikasjonen, beskytt smarttelefonen din med en PIN-kode, og velg en kompatibel Hardware Wallet.



Alternativt, hvis du er en långiver, vil denne opplæringsvideoen veilede deg gjennom bruk av Debifi-plattformen. Fra å velge låntakere som er interessert i tilbudet ditt, til å levere offentlige nøkler, signere avtaler, overføre stablecoins og mer.



![video](https://youtu.be/g8iLxwI4xT0)



Nå vet du hvordan du bruker Debifis plattform for å få lån.



Jeg anbefaler at du tar dette kurset, som tar en grundig titt på Bitcoin, Stablecoins og deres bidrag til suverenitet.



https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46