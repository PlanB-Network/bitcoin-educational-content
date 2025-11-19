---
name: Zeus Embedded
description: Slik bruker du Lightning Zeus Embedded Wallet
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS er i utgangspunktet en mobilapplikasjon for fjernstyring av lynnoder, slik at du kan kontrollere noden din som er installert på en ekstern server


Men applikasjonen har også en "Embedded node".



**Det er denne siden av applikasjonen vi skal utforske i denne veiledningen. Dette gjør det mulig for hvem som helst å ha sin egen lynnode på mobilen, uten behov for en dedikert server, på samme måte som ACINQ tilbyr sin utrolige Wallet lightning Phoenix.**



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*Lightning er et nettverk som opererer parallelt med Bitcoin, noe som gjør det mulig å veksle bitcoins uten å systematisk måtte gjennomføre On-Chain-transaksjoner. Resultatet er nesten øyeblikkelige transaksjoner, uten behov for å vente i 10 minutter på at en blokk skal valideres. Dette er spesielt nyttig når man skal betale en kjøpmann i den fysiske verden. I tillegg gir Lightning et bemerkelsesverdig nivå av **konfidensialitet** som Bitcoin-nettverket ikke har fra naturens side*.



** Zeus "Integrated"** er rettet mot Bitcoin-brukere som ønsker å maksimere sitt privatliv og autonomi.


Kort sagt, det er **potensielt** Wallet-mobilen til cypherpunks drømmer. Selv om den fortsatt er i sin spede begynnelse (alfaversjon) og har noen få bugs, er funksjonene legio, og det er ingen tvil om at den vil glede de mest uredde blant oss, som ønsker maksimal kontroll og valgfrihet.



På den annen side tror jeg ikke det for øyeblikket er egnet for nybegynnere som ikke er kjent med Bitcoin og bare vil ha en enkel måte å sende / motta satoshis på. Dette kan imidlertid endre seg i fremtiden, ettersom en forvaringsfunksjon via Cashu (chaumian Ecash)-protokollen er under implementering for nybegynnere...



## Installer applikasjonen



Gå til [prosjektets nettsted] (https://zeusln.com/) for å laste ned applikasjonen for smarttelefonens operativsystem:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Opprettelse av portefølje



Når programmet har startet, klikker du på "Quick Start"-knappen for å begynne å opprette Wallet.



![image](assets/fr/03.webp)





Deretter vises en rekke initialiseringsskjermbilder. Vent noen øyeblikk, og vent deretter noen minutter til noden er 100 % synkronisert via Neutrino.



Dette kan ta noen minutter. For informasjon nøytrino er en måte for mobile lommebøker å få tilgang til Blockchain Bitcoin-informasjon, uten å måtte kjøre en Full node.



![image](assets/fr/04.webp)





Etter noen få øyeblikk er du klar til å gå.



![image](assets/fr/05.webp)




## Oppsett av applikasjon



Klar, vel, ikke helt, for det sier seg selv at en Zeus-bruker som er navnet verdig, navigerer sin Wallet med klasse og stil. Så vi må endre avataren hans.



Klikk på avataren din øverst i høyre hjørne av skjermen:



![image](assets/fr/06.webp)





Klikk på tannhjulet og deretter på plusstegnet "+" :



![image](assets/fr/07.webp)





Velg det vakreste bildet av Zevs som skal representere denne Wallet, og klikk på "CHOOSE PICTURE" nederst på skjermen, og gå deretter tilbake ved å klikke på pilen øverst til høyre.



![image](assets/fr/08.webp)





Til slutt gir du Wallet et kallenavn og klikker på "SAVE Wallet CONFIG" for at endringen skal tre i kraft. Til slutt klikker du på tilbakepilen øverst i venstre hjørne for å gå tilbake til startskjermen.



![image](assets/fr/09.webp)





Denne gangen kan vi virkelig komme i gang.



![image](assets/fr/10.webp)



### Biometri



For å beskytte tilgangen til Wallet kan du legge til en PIN-kode/passord og aktivere biometri.



Dette gjør du ved å gå til Wallet-hovedmenyen ved å klikke på de horisontale strekene øverst til venstre.



![image](assets/fr/11.webp)





Velg "Innstillinger", deretter "Sikkerhet" og til slutt "Angi/endre PIN-kode".



![image](assets/fr/12.webp)





Opprett PIN-koden din, bekreft den og aktiver biometri ved å trykke på den tilhørende "Biometri"-knappen.  Gå tilbake til hovedmenyen ved hjelp av pilen øverst til venstre.



![image](assets/fr/13.webp)




### Lagre Mnemonic frase



Når du er tilbake i hovedmenyen, klikker du på "Sikkerhetskopier Wallet", og deretter leser du advarselsteksten som informerer deg om at det å miste de 24 ordene du er i ferd med å motta, er det samme som å miste tilgangen til pengene dine, og at alle som har disse ordene i tillegg til deg, kan få tilgang til pengene dine. Gi dem aldri til noen.



Velg "I UNDERSTAND" nederst på skjermen. Klikk deretter på hvert av de 24 ordene for å få dem opp, og noter dem nøye.



Du kan skrive den på papir, eller kanskje, for ekstra sikkerhet, gravere den på rustfritt stål for å beskytte den mot brann, oversvømmelse eller kollaps. Valget av medium for Mnemonic avhenger av sikkerhetsstrategien din, men hvis du bruker Zeus som en utgiftsportefølje som inneholder moderate beløp, bør papir være tilstrekkelig.



For mer informasjon om hvordan du lagrer og administrerer Mnemonic-frasen din, anbefaler jeg på det sterkeste å følge denne andre veiledningen, spesielt hvis du er nybegynner:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



Når du er ferdig, klikker du på "I'VE BACKUP MY 24 WORDS" nederst på skjermen, og vi er tilbake på startskjermen, klare til å motta våre første bitcoins.




## Alternativ 1 - Motta On-Chain bitcoins og åpne en Lightning-kanal



**Zeus Embedded** er først og fremst utviklet som en innebygd lynnode, men den kan også brukes som en Wallet On-Chain.



For å motta On-Chain bitcoins, klikk på "On-Chain"-knappen og deretter på "Motta".


Til slutt skanner du QR-koden eller kopierer Bitcoin Address for å sette inn penger.



![image](assets/fr/15.webp)





Når midlene er bekreftet og kreditert til din Wallet, kan du bruke dem til å åpne en **Lightning-kanal**. Lightning-kanalen din er din inngangsport til Lightning Network, slik at du kan Exchange bitcoins på en mye mer konfidensiell og rask måte.





- For å gjøre det, klikk på "FLYTT On-Chain MIDLER TIL LIGHTNING"



På neste skjermbilde blir du bedt om å åpne en kanal i samarbeid med **"Olympus by Zeus"**, LSP (Lightning Service Provider) favorisert av Wallet.


I denne veiledningen velger vi dette alternativet for enkelhets skyld, men det er fullt mulig å åpne kanaler med en hvilken som helst node i nettverket.


Det er til og med mulig å åpne flere kanaler i én og samme transaksjon ved å velge "OPEN ADDITIONAL CHANNEL". *Men dette skal vi se nærmere på i en "avansert" versjon av **Zeus Embedded**-veiledningen.*





- Velg deretter beløpet du ønsker å bruke på denne kanalen. I vårt tilfelle vil alle On-Chain-midlene våre bli brukt, så vi aktiverer knappen "Bruk alle mulige midler".





- Til slutt velger du "OPEN CHANNEL"-knappen nederst på skjermen.



![image](assets/fr/16.webp)





I løpet av få sekunder er kanalen etablert, og vi er klare til å foreta våre første Lyn-transaksjoner. På startskjermen kan vi se en liten klokke ved siden av Wallet-saldoen vår. Dette er fordi vi fortsatt må vente på tre On-Chain-bekreftelser før kanalen virkelig er funksjonell.



![image](assets/fr/17.webp)





Etter de tre bekreftelsene ser vi at saldoen vår nå er kreditert Lightning-innlegget.



![image](assets/fr/18.webp)



En liten detalj: Når vi klikker på menyen nederst på skjermen for å se statusen til lynkanalene våre, ser vi at en liten del av saldoen vår ikke er tilgjengelig for bruk: Vi kan bare bruke 208253 satoshier i stedet for de 210370 vi faktisk har. Dette er normalt, ettersom det er spesifikt for lynprotokollen.



Til slutt bør det bemerkes at vår partner Olympus forbeholder seg retten til å stenge kanalen etter eget skjønn, for eksempel hvis den ikke blir brukt. For å sikre at kanalen vår opprettholdes, må vi betale LSP (Lightning Service Provider), som vi vil se i neste avsnitt, gjennom den andre måten å åpne en kanal på.





## Send bitcoins via Lightning



Nå som vi har fått kanalen vår i gang, la oss se hvordan vi kan bruke den til å betale en Invoice (Invoice) lyn.



Dette gjør du ved å klikke på "Lightning"-knappen og deretter på "Send".



![image](assets/fr/19.webp)





På neste skjermbilde kopierer du Invoice inn i det dedikerte feltet, eller skanner det ved å klikke på ikonet øverst til høyre. Til slutt skyver du "Slide to Pay"-knappen til høyre for å betale.



![image](assets/fr/20.webp)






Vent noen sekunder, så er Invoice betalt, og satoshiene dine har reist med lysets hastighet.



![image](assets/fr/21.webp)





Med Zeus kan du deretter legge til en seddel for å denominere betalingen, eller se ruten satoshiene dine tok før de nådde destinasjonen (og avgiftene som ble tatt ut av alle mellomliggende noder). Dette er den typen funksjonalitet vi elsker med Wallet.



![image](assets/fr/22.webp)



Merk at i motsetning til en Wallet som [Phoenix]([Plan ₿ Academy - Phoenix](https://planb.academy/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), blir ruten med Zeus beregnet lokalt og ikke delegert til en tredjepart (ACINQ i Phoenix' tilfelle). Så du er den eneste som kjenner mottakeren av betalingen. Vi taper litt effektivitet (betalinger tar litt lenger tid å gjennomføre, men vi vinner mye når det gjelder personvern).





Ved å klikke på den lille pilen nederst på startskjermen kan du også se betalingshistorikken vår. Her ser vi i Green de 212 121 Sats som ble mottatt for On-Chain, deretter i rødt henholdsvis de 211 756 Sats som ble brukt til å åpne kanalen vår, og deretter de 121 212 satoshiene som ble brukt til å betale for Invoice-lynet vårt.



![image](assets/fr/23.webp)





## Alternativ 2 - Motta bitcoins direkte på Lightning



I stedet for å åpne en kanal manuelt, som vi nettopp har sett, er det mulig å motta penger direkte via Lightning, selv uten en allerede eksisterende kanal, ved hjelp av Olympus, Zeus LSP.




- Dette gjør du ved å klikke på "Lightning"-knappen på startskjermen og deretter på "Receive".
- Velg deretter beløpet du ønsker å motta i "Beløp"-boksen, og klikk på "Opprett Invoice"-knappen nederst på skjermen.



![image](assets/fr/24.webp)





Det neste skjermbildet viser Invoice som skal betales for å motta satoshiene. Vi får beskjed om at LSP-en vil holde tilbake 10 000 Sats hvis betalingen skjer via Lightning. Vi får se senere hvordan disse kanalåpningsgebyrene er begrunnet.



Betal Invoice eller få noen andre til å betale det, så åpnes kanalen automatisk, men med fradrag av de 10 000 Sats som avtalt.



![image](assets/fr/25.webp)





Vi er nå i spissen for 2 lynkanaler, hvis status kan kontrolleres ved å klikke på knappen som indikeres av den hvite pilen nederst på startskjermen.



Vi kan se at i motsetning til kanalen som åpnes fra On-Chain-skalaen vår, viser den som åpnes direkte via lynet, ingen advarsel.


Ettersom du har betalt for å sette opp denne kanalen, forplikter Lightning Service Provider (LSP) seg til å vedlikeholde kanalen i 3 måneder, og tilbyr deg "innkommende likviditet". På den nederste kanalen kan du se at mottakskapasiteten er 96383 satoshier. LSP har derfor bundet opp kapital slik at du kan motta betalinger direkte etter at kanalen er åpnet.



De 10 000 Satoshi som betales i avgifter dekker altså: kostnadene ved å åpne kanalen (Bitcoin On-Chain transaksjon, garantien for å vedlikeholde kanalen i tre måneder og kapitalbinding).



![image](assets/fr/26.webp)





Gratulerer, du er nå klar til å bruke Zeus Embedded, det mobile belysningssystemet Wallet med de mest avanserte funksjonene på markedet.





Hvis du vil vite mer om den tekniske driften av Lightning Network, kan du finne Fanis Michalakis' utmerkede gratis opplæring i Plan ₿ Academy:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb