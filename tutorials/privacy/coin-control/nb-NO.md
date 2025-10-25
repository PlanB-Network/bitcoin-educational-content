---
name: Coin Control
description: Bli kjent med Coin Control, et nøkkelverktøy for å beskytte personvernet ditt på Bitcoin
---
![cover](assets/cover.webp)


*Denne veiledningen er importert fra [en leksjon av Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*



## Innledning



Soliditeten til Bitcoin-protokollen sikres av enkle grunnleggende konsepter. Blant disse skiller åpenhet seg ut: alle Bitcoin-transaksjoner er offentlige og lett verifiserbare av hvem som helst. Selv om denne egenskapen er en hjørnestein i protokollen, fordi den forhindrer svindel og sikrer midlenes ekthet, kan den også representere en utfordring for konfidensialitet. **Har du noen gang lurt på om så mye åpenhet kan svekke ditt personvern?**



Det bør du gjøre. Selv om det er ganske enkelt å samle Satoshi non-kyc, er personvernet ditt mest utsatt i utgiftsfasen.



### Hva skjer når du bruker en UTXO



Å bruke Bitcoin er ikke bare å overføre verdier til noen andre.



Ved å forbruke en av UTXO-ene dine, må du faktisk oppfylle vilkårene som er pålagt for protokollgjennomsiktighet, fordi du har en forpliktelse til å bevise at du eier disse midlene. Du gjør deg derfor ansvarlig for :




- avsløre din offentlige nøkkel;
- produsere en digital signatur.



Tidspunktet for bruk er derfor det mest kritiske: ** Å bruke Bitcoin er en handling som skal gjøres bevisst og med så mye kontroll som mulig**.



## Coin Kontroll



I Bitcoin-protokollen finnes ikke elementer som _konto_ eller _pengeenheter_. Konseptet UTXO forklares på en utmerket måte i følgende kurs, som jeg anbefaler på det varmeste:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Med Bitcoin er det du akkumulerer og senere bruker, små eller store regningsenheter målt i Satoshi, representert ved "ubrukte transaksjonsutganger", **UTXO**, også kalt "mynter". Når du bruker UTXO-er til å opprette en transaksjon, blir de fullstendig ødelagt, og andre UTXO-er opprettes i stedet.



Programvarelommebøker er utviklet for å gjøre dette valget automatisk, ved hjelp av "tilfeldig" utvalgte mynter, ved å ta i bruk visse algoritmer gitt av protokollen. Det eneste kriteriet som disse algoritmene oppfyller, er å dekke beløpet som trengs for å bruke.



De kan blande UTXO-er av ulik alder, eller favorisere å bruke de nyeste eller "eldste", avhengig av algoritmen som er valgt av utviklerne. De beste Software Wallets planlegger også å gi brukeren et viktig valg.



`Coin Control`manual, som du også kan finne referert til som `Coin Selection`, er en funksjon i noen Software Wallets som lar deg **manuelt velge UTXOer som skal brukes når du bygger transaksjonen**.



Anta at vi har en Wallet med tre UTXO-er på henholdsvis 21 000, 42 000 og 63 000 Satoshi.



![img](assets/en/01.webp)



Hvis du må bruke 24 000 Sats og la en algoritme gjøre det automatiske valget, kan en god Software Wallet velge å kombinere UTXO 1 + UTXO 2 for å betale avgiftene på 24 000 Sats og Miner, noe som skaper en rest som går tilbake til en intern Address i start-Wallet.



![img](assets/en/02.webp)



Etter transaksjonen kan den nye situasjonen i Wallet, som kun teller UTXO-er, oppsummeres som følger.



![img](assets/en/03.webp)



Med riktig programvare og bevissthet kunne du imidlertid ha gjort et annet, og på noen måter riktigere valg. For eksempel ved å velge bare UTXO2 (fra 42 000 Sats).



![img](assets/en/04.webp)



Med en sluttsituasjon i Wallet, på nivå med UTXO, ser det annerledes ut enn før.



![img](assets/en/05.webp)



## Hvorfor manuell coin control?



![img](assets/en/06.webp)



I de to eksemplene ovenfor er saldoen faktisk den samme - 108 280 Sats. Etter å ha brukt 24 000 Sats, ville vi uten manuelt valg hatt 2 UTXO i Wallet; med manuell kontroll av Coin har vi 3 totalt.



Spørsmålet vi kunne stille oss er følgende: **hvorfor gjøre alt dette?** Det finnes, eller kan finnes, flere grunner til at vi ikke brukte `UTXO1` **og alle disse ligger til grunn for hvorfor—i forbruksfasen—å aktivere manuell coin control er en god praksis å følge**.



Ved å velge UTXO-er kan du favorisere noen aspekter fremfor andre. Valget avhenger av hvilke mål du ønsker å oppnå.



### Personvern



En av de viktigste fordelene med manuell Coin-kontroll er **større personvern for den som bruker pengene**. La oss alltid ta eksemplet vårt: bruk av 24 000 Satoshi _uten manuelt Coin-valg_. Siden Blockchain av Bitcoin er et offentlig register, kan en utenforstående observatør uten skyggen av tvil erklære at inngangene `UTXO1 på 21 000 Sats` og `UTXO2 på 42 000 Sats`, samt resten, `UTXO5 fra 38 280 Sats` **alle tre tilhører samme bruker**.



Ved å velge `UTXO2` manuelt, derimot, forblir `UTXO1` fullstendig reservert, og blir liggende i UTXO-settet og vente på å bli brukt på et mer passende tidspunkt.



UTXO1 kan komme fra en KYC-kilde, for eksempel en betaling mottatt i Exchange for varer og tjenester, mens de andre UTXO-ene ikke gjør det. Hvis man blander en UTXO-kyc med andre som er mer konfidensielle, går det ut over anonymiteten til ikke-kyc-midler.



**KYC-midler ville uunngåelig føre til å spore betaleren tilbake til identiteten. Hvis det var din lommebok, ville du ønsket at en ekstern observatør kunne spore identiteten din med en så absolutt sikkerhet?**



Prøv da å tenke på at lommebøker som implementerer manuelt valg av UTXO-er, for eksempel, tillater **segregering av en eller flere UTXO-er**, en funksjon som skal brukes når slike situasjoner oppstår.



Selv om jeg er overbevist om at KYC-midler bør oppbevares i en separat Wallet enn Bitcoin kjøpt uten kyc, hvis dette er ditt tilfelle, er segregering av noen av adressene dine en viktig hjelp, som du kan dra nytte av ved å lære å manuelt velge utgiftsinngangene dine.



### Sparer på avgifter



Ved å velge riktig UTXO til å foreta en utgift, **muliggjøres avgiftsoptimalisering**. Med utgangspunkt i vårt første eksempel valgte Software Wallet to UTXO-er for å dekke utgiften som skulle gjøres. To UTXO-er innebærer to signaturer som skal vises til nettverket. Det følger at transaksjonen har en større "vekt" i form av vBytes.



Med den manuelle kontrollen Coin kan du derimot bare velge en som er tilstrekkelig til å dekke beløpet, noe som sparer gebyrer ved å redusere "vekten" på transaksjonen.



I tider der avgiftene er høye, men du er tvunget til å bruke Bitcoin On-Chain (f.eks. for å åpne en Lightning Network-kanal), er det Coin-kontrollen som viser seg å være det riktige økonomiske insentivet å benytte seg av.



### Aggregering av levningene



Når du foretar en betaling og bruker Bitcoin On-Chain, blir muligheten for å motta vekslepenger nesten alltid en visshet. Hver rest er i seg selv et lite tap av personvern, ettersom det avslører for nettverket (og spesielt for mottakeren av betalingen) en Address av deg som kan knyttes til kildeinngangen din.



Tatt i betraktning at de beste Wallet HDs generate spesielle adresser for restene, kan du enkelt gjenkjenne dem og "segregere" alle restene av de forskjellige transaksjonene som er gjort; når de har nådd et visst beløp, kan du velge dem manuelt og konsolidere dem, eller bytte til Lightning Network (min foretrukne metode) og behandle dem for å gjenvinne personvernet som er tapt i utgiftene.



### Utgifter fra en Cold Wallet



Cold Wallet er et instrument som man med rimelighet kan oppnå en god grad av sikkerhet, for å lagre et hvilket som helst beløp for å holde til side i en lang periode. Imidlertid kan uforutsette hendelser skje, så behovet oppstår for å få en hånd på besparelser og møte noen uventede utgifter.



Jeg vet ikke hvor mange som kan dele min tilnærming, men mitt råd er å ** aldri gjøre utgiftene direkte fra Cold Wallet, for å unngå å motta endringen mellom adressene til det samme **. Lær deg å manuelt velge UTXO-er som trengs for å dekke utgiften, overføre dem til en Wallet Hot og forberede transaksjonen din fra sistnevnte. Eventuelle endringer kan du sende tilbake til en Cold Wallet Address (hvis beløpet er tilstrekkelig), bruke det til andre utgifter, eller fortsatt segregere det som vi nettopp har sett.



## Praktisk presentasjon


Etter den tekniske introduksjonen av `hvorfor`, la oss se hvordan du kan bruke Coin manuell kontroll i praksis med forskjellig programvare, stasjonær og mobil. Vi vil alltid bruke den samme Wallet BIP39, importert til hvert av de valgte verktøyene, for å vise deg de små forskjellene mellom dem.



## Wallet Skrivebord



### Sparrow



Hvis du bruker Sparrow, åpner du Wallet og velger _UTXOs_ fra menyen til venstre. Du vil se en liste over alle UTXO-er som er knyttet til din Wallet.



Bare klikk med musen på en av dem, og velg deretter _Send Selected_. Sparrow viser også summen som er tilgjengelig for bruk etter valget, rett ved siden av kommandoen. Grafisk viser Sparrow den valgte UTXO ved å utheve den i blått.



![img](assets/en/07.webp)



Du kan også velge mer enn én. Bruk _CTRL_-tasten for å velge UTXO-er som ikke ligger ved siden av hverandre i listen.



![img](assets/en/08.webp)



Etter at du har valgt UTXO manuelt, kan du begynne å bygge transaksjonen, og Sparrow vil vise deg grafisk hvordan den er sammensatt.



![img](assets/en/09.webp)



#### Segregering av UTXO



Segregering av midler betyr å "låse" dem i Wallet slik at de ikke kan brukes som input til en transaksjon. Sparrow tillater denne funksjonaliteten, som alltid er tilgjengelig fra _UTXOs_-menyen: du plasserer musen over UTXO som skal "låses" og klikker på høyre museknapp. Blant funksjonene i denne prosedyren vises _Freeze UTXO_. Slik vil du kunne segregere mynter med Sparrow lommebøker.



![img](assets/en/29.webp)



### Elektrum



Hvis Wallet-skrivebordet ditt er Electrum, bør du vite at du kan velge UTXO-er manuelt enten fra _Addresses_-menyen eller fra _Coins_-menyen. I begge menyene gjøres valget ved å peke med musen på ønsket UTXO og velge _Add to Coin control_ etter å ha høyreklikket.



![img](assets/en/10.webp)



Selv med denne programvaren kan du velge mer enn én UTXO ved hjelp av _CTRL_-tasten på tastaturet hvis de ikke ligger ved siden av hverandre.



![img](assets/en/11.webp)



Grafisk vil Electrum vise deg valget ved å utheve de valgte UTXO-ene i Green, mens en søyle vises nederst, uthevet i samme farge, som viser den tilgjengelige balansen etter Coin-kontrollen.



![img](assets/en/12.webp)



Når du har valgt utdata, eller utdataene, kan du bygge opp transaksjonen slik du vanligvis gjør fra _Send_-menyen.



#### Segregering av UTXO



Electrum tilbyr denne funksjonaliteten ved å gå til _Coins_-menyen, hvor du velger en bestemt UTXO og deretter velger _Freeze_ med et høyreklikk. Du kan "fryse" Address selv uten midler fra _Addresses_-menyen, eller "Coin" for ikke å bruke den.



![img](assets/en/28.webp)



### Nunchuk



Med Nunchuk kan du velge UTXO-er manuelt fra hovedmenyen når den er åpen. Start Nunchuk og klikk på _Vis mynter_.



![img](assets/en/13.webp)



Dette åpner vinduet som inneholder alle UTXO-ene i Wallet, der du kan velge en eller flere ved å aktivere haken ved siden av hvert beløp. Når du har valgt, fortsetter du med _Create transaction_.



![img](assets/en/14.webp)



Deretter kan du angi destinasjonen Address og angi beløp og gebyrer.



![img](assets/en/15.webp)



#### Segregering av UTXO



For fullstendighetens skyld tillater Nunchuk også blant sine funksjoner å segregere en (eller flere) UTXO-er, og det kan gjøres på to forskjellige måter. Åpne menyen _Vis mynter_ og velg manuelt fra listen over mynter. Klikk deretter på _More_-menyen nederst til høyre: en liste over alternativer vises, hvorfra du kan velge _Lock coins_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Du kan også klikke på plassen som er reservert for UTXO, for å få tilgang til vinduet _Coin details_. Her vises kommandoen for å låse/låse opp den aktuelle UTXO i øvre høyre hjørne.



![img](assets/en/41.webp)



### Blockstream-appen



Blockstream App desktop, tidligere kjent som Green, lar deg velge Coin når du allerede har begynt å bygge transaksjonen. Åpne derfor Wallet og klikk på _Send_.



![img](assets/en/16.webp)



Lim inn destinasjonen Address i det aktuelle feltet, og velg deretter _Manual Coin selection_.



![img](assets/en/17.webp)



Dette åpner vinduet der du kan velge én eller flere UTXO-mynter. I eksempelet nedenfor har vi valgt to mynter. Deretter bekrefter du valget ved å klikke på _Confirm Coin Selection_.



![img](assets/en/18.webp)



Angi beløp og gebyrer, og fortsett deretter som normalt med transaksjonen.



![img](assets/en/19.webp)



⚠️ N.B. I _Coins_-menyen til Green er det _Lock_ / _Unlock_-elementer som antyder muligheten for å segregere UTXO. Denne funksjonen er bare aktivert i såkalte Multisig-kontoer; den aktiveres også bare ved å velge UTXO av svært lite beløp, nær terskelen til `Dust`.



## Wallet mobil



Lommebøker kan også velges fra mobilen, som gjør det mulig å velge UTXO-er manuelt. La oss se Blue Wallet som det første eksemplet.



### Blå Wallet



Hvis du er bruker av denne Wallet, åpner du den og klikker for å gå til kontrollskjermbildene knyttet til en av lommebøkene dine. For å få tilgang til kontrollmanualen for Coin må du gå inn i utgiftsfasen og deretter klikke på _Send_.



![img](assets/en/21.webp)



På neste skjermbilde velger du menyene som indikeres av de tre prikkene i øvre høyre hjørne. Et rullegardinvindu åpnes med en rekke kommandoer. Velg den siste: _Coin Control_.



![img](assets/en/22.webp)



På dette punktet viser Blue Wallet alle UTXO-ene dine. I tillegg til beløpene er de grafisk differensiert med forskjellige farger.



![img](assets/en/27.webp)



Velg UTXO for å velge, og velg deretter _Use Coin_.



![img](assets/en/23.webp)



Blå Wallet tar deg tilbake til _Send_-vinduet for å fortsette å bygge opp transaksjonen. Juster beløpet og gebyrene, og velg deretter _Neste_.



![img](assets/en/24.webp)



På dette tidspunktet kan du avslutte transaksjonen, slik du vanligvis gjør.



#### Segregering av en UTXO



Blue Wallet lar deg også segregere UTXO-er, slik at de ikke er tilgjengelige for bruk, noe som ikke er en dårlig funksjon for en Wallet fra en mobil enhet. Du åpner Coin-kontrollen med prosedyren som nettopp ble forklart, og etter at du har valgt UTXO, velger du _Freeze_ i stedet for _Use Coin_.



![img](assets/en/26.webp)



### Nunchuk



Mobilversjonen av Nunchuk gir også brukeren muligheten til å kontrollere Coin. Hvis du bruker denne appen fra mobilen, åpner du den og går til _Wallet_-menyen. Derfra velger du _Vis mynter_.



![img](assets/en/30.webp)



Klikk på _Velg_ i vinduet der listen over UTXO-er vises.



![img](assets/en/38.webp)



En valgfunksjon vises ved siden av hver UTXO. Som i PC-versjonen gjøres manuelle valg på Nunchuk mobile ved å krysse av i den lille firkanten ved siden av beløpet. Skjermen viser antall UTXO-er som er valgt, og det totale beløpet som er tilgjengelig. Når du er ferdig, klikker du på ₿-symbolet i nedre venstre hjørne, som er kommandoen for å starte oppbyggingen av transaksjonen.



![img](assets/en/31.webp)



Nå kan du fullføre transaksjonen ved å velge beløp og klikke på _Continue_.



![img](assets/en/32.webp)



Fortsett som vanlig ved å lime inn en destinasjon Address, en beskrivelse og tilpasse gebyrinnstillingene.



#### Segregering av UTXO



Du kan også segregere UTXO-er med mobil Nunchuk. Åpne det dedikerte myntlistevinduet, og velg pilen ved siden av UTXO du vil segregere.



![img](assets/en/42.webp)



Du vil se en plass reservert for _Coin details_, der du kan velge _Lock this coin_.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper er den siste Wallet vi vil se i denne veiledningen. Vi ser funksjonaliteten brukt på Coin-kontroll med en Wallet single-sig, selv om en slik bruk ikke er formålet med akkurat denne appen. Etter at du har konfigurert Keeper på telefonen din, starter du den og åpner en Wallet som inneholder noen midler. I midten av hovedskjermen klikker du på _Vis alle mynter_.



![img](assets/en/34.webp)



Keeper viser en oversikt over UTXO-ene. Klikk på _Velg å sende_ for å få tilgang til valgskjermen.



![img](assets/en/35.webp)



Du kan velge mynter ved å krysse av for dem ved å klikke på den aktuelle kommandoen. Når du er ferdig, klikker du på _Send_.



![img](assets/en/36.webp)



Bitcoin Keeper tar deg direkte til _Send_-menyen, der du kan bygge transaksjonen med de valgte UTXO-ene.



![img](assets/en/37.webp)



## Hardware Wallet



Hver av programvarelommebøkene i denne veiledningen kan være den eneste Interface til en av maskinvarelommebøkene dine. Det betyr at Coin-kontrollen for frakoblet signeringsenhet utføres med trinnene som er sett så langt.



### Generelle anbefalinger



Coin-kontroll er en svært effektiv metode for å velge transaksjonsinnganger. Manuell utvelgelse er enda mer effektiv hvis du har merket kilden til Satoshiene dine godt når du kjøper/mottar midler. Hvis du ønsker å lære denne teknikken godt, anbefaler jeg følgende veiledning:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Vi har tidligere snakket om `segregering av rester`. Hvis du vil låse restene for senere behandling og gjenvinne personvernet (bytte på Layer 2), må du passe på å `merke` dem hver gang du mottar en. Av Software Wallets som er sett så langt, er det bare Electrum som farger UTXO-restene grafisk for å gjøre dem synlige på et øyeblikk. Andre, som Sparrow, viser deg kjeden i avledningsveien til den enkelte UTXO (`m/84'/0'/0'/0'/1/11`).



For å bruke denne teknikken effektivt, husk å alltid legge til en beskrivelse på endringen du mottar: personen du sendte pengene dine til (en betaling, en veiledning eller annet), kjenner Address knyttet til endringen og vet at den tilhører deg, siden den kommer fra transaksjonen dere gjorde sammen!