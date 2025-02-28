---
term: COINJOIN

---
Coinjoin er en teknikk som brukes til å bryte sporbarheten til bitcoins. Den baserer seg på en samarbeidstransaksjon med en spesifikk struktur med samme navn: coinjoin-transaksjonen. Coinjoin-transaksjoner bidrar til å forbedre personvernet til Bitcoin-brukere ved å gjøre det vanskeligere for eksterne observatører å analysere transaksjoner. Denne strukturen gjør det mulig å blande flere mynter i én enkelt transaksjon, noe som gjør det vanskelig å fastslå koblingene mellom inngangs- og utgangsadresser.

Coinjoin fungerer generelt på følgende måte: Ulike brukere som ønsker å blande seg, setter inn et beløp som input i en transaksjon. Disse inndataene vil komme ut som forskjellige utdata av samme beløp. Ved slutten av transaksjonen er det umulig å avgjøre hvilken utgang som tilhører hvilken bruker. Det er teknisk sett ingen kobling mellom input og output i coinjoin-transaksjonen. Koblingen mellom hver bruker og hver UTXO er brutt, på samme måte som historikken til hver mynt er det.

![](../../dictionnaire/assets/4.webp)

For å muliggjøre coinjoin uten at noen brukere mister kontrollen over midlene sine, blir transaksjonen først konstruert av en koordinator og deretter overført til hver bruker. Deretter signerer hver enkelt transaksjonen på sin side etter å ha verifisert at den passer dem, og deretter legges alle signaturene til transaksjonen. Hvis en bruker eller koordinatoren forsøker å stjele andres penger ved å endre utdataene fra coinjoin-transaksjonen, vil signaturene være ugyldige, og transaksjonen vil bli avvist av nodene. Når registreringen av deltakernes output gjøres ved hjelp av Chaums blindsignaturer for å unngå koblingen til input, kalles dette "Chaumian coinjoin".

Denne mekanismen øker konfidensialiteten til transaksjonene uten å kreve endringer i Bitcoin-protokollen. Spesifikke implementeringer av coinjoin, som Whirlpool, JoinMarket eller Wabisabi, tilbyr løsninger for å forenkle koordineringsprosessen mellom deltakerne og forbedre effektiviteten til coinjoin-transaksjonen. Her er et eksempel på en coinjoin-transaksjon:

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

Det er vanskelig å fastslå med sikkerhet hvem som først introduserte ideen om coinjoin på Bitcoin, og hvem som hadde ideen om å bruke David Chaums blindsignaturer i denne sammenhengen. Det antas ofte at Gregory Maxwell var den første til å diskutere det i [en melding på BitcoinTalk i 2013] (https://bitcointalk.org/index.php?topic=279249.0):

Ved hjelp av blinde Chaum-signaturer: Brukerne kobler seg til og oppgir inndata (og endrer adresser) samt en kryptografisk blindet versjon av adressen de ønsker å sende de private myntene sine til. Brukerne kobler seg anonymt til igjen, avmaskerer utdataadressene sine og sender dem tilbake til serveren. Serveren kan se at alle utdataene er signert av den, og at alle utdataene dermed kommer fra gyldige deltakere. Senere kobler folk seg til igjen og signerer.

Maxwell, G. (2013, 22. august). *CoinJoin: Bitcoin-personvern for den virkelige verden*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

Det finnes imidlertid tidligere omtaler, både for Chaum-signaturer i forbindelse med miksing og for coinjoins. [I juni 2011 presenterer Duncan Townsend på BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) en mikser som bruker Chaum-signaturer på en måte som er ganske lik moderne Chaumian coinjoins. I den samme tråden er det [en melding fra hashcoin som svar til Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) for å forbedre mikseren hans. Denne meldingen presenterer det som ligner mest på coinjoins. Et lignende system nevnes også i [en melding fra Alex Mizrahi i 2012] (https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), mens han var rådgiver for skaperne av Tenebrix. Selve begrepet "coinjoin" ble ikke oppfunnet av Greg Maxwell, men kom fra en idé av Peter Todd.

> begrepet "coinjoin" har ingen fransk oversettelse. Noen bitcoinere bruker også begrepene "mix", "mixing" eller "mixage" for å referere til coinjoin-transaksjonen. Mixing er snarere prosessen som brukes i hjertet av coinjoin. Det er også viktig å ikke forveksle miksing gjennom coinjoins med miksing gjennom en sentral aktør som tar bitcoinsene i besittelse under prosessen. Dette har ingenting å gjøre med coinjoin, der brukeren ikke mister kontrollen over bitcoinsene sine i løpet av prosessen