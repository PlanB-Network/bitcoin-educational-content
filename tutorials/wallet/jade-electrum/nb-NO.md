---
name: Jade - Electrum
description: Slik bruker du Jade eller Jade Plus med Electrum (stasjonær)
---

![cover](assets/cover.webp)



_Denne veiledningen er hentet fra en [Bitcoin Workshops-leksjon](https://officinebitcoin.it/lezioni/jadeele/index.html)_



Opplæringen er laget med Jade Classic, men operasjonene er også gyldige for de som har Jade Plus.



Etter at du har initialisert Jade, kan du begynne å bruke den og - for å gjøre det - velge en wallet-skjerm.



Jade er en enhet som kan brukes sammen med flere wallet-apper, eller companion-apper som Blockstream spesifiserer dem på nettstedet sitt.



I denne veiledningen vil du se trinnene for bruk av Electrum Wallet, via USB-kabeltilkobling.



## Overføring av offentlig nøkkel



Ta og slå på din initialiserte Jade. Så snart du slår den på, ser den slik ut:




![img](assets/en/32.webp)



Hvis du velger _Unlock Jade_, får du opp en meny der du må velge hvordan du kobler enheten din til Companion-appen.



Med Electrum kan du bare koble Jade til via USB, så velg denne metoden.



Start Electrum, som vil åpne og foreslå som standardalternativ å åpne den sist brukte wallet.



Hvis dette er første gang du kobler Jade til Electrum, velger du _Create New Wallet_ og deretter _Finish_.



![img](assets/en/34.webp)



Navn wallet.



![img](assets/en/35.webp)



Velg Standard Wallet.



![img](assets/en/36.webp)



Når du velger keystore, er det viktig å velge _Bruk en maskinvareenhet_.



![img](assets/en/37.webp)



Electrum starter skanning etter maskinvareenheten.



![img](assets/en/38.webp)



Når du kobler USB til datamaskinen (som allerede er koblet til Jade på USB C-siden), vises wallet-maskinvaren i låsemodus. Jade låses opp ved å taste inn den sekssifrede PIN-koden som ble angitt under oppsettet.




![img](assets/en/39.webp)



Ulåst maskinvareenhet, Electrum oppdager Jade. Fortsett ved å klikke på _Neste_.



![img](assets/en/40.webp)



På dette tidspunktet ber Electrum deg om å angi policyskriptet: Velg _Native Segwit_.



![img](assets/en/41.webp)



Fasen med overføring av offentlig nøkkel fra wallet fra Jade til visning av Electrum begynner.



Når eksporten av den offentlige nøkkelen er fullført, er prosessen ferdig.



Watch-only er klar og Electrum varsler om fullføring med følgende skjermbilde.



![img](assets/en/42.webp)



wallet er faktisk opprettet, og du kan begynne å utforske den: Du kan se _adressene_, _lommebokinformasjonen_, og - viktigst av alt - du kan se i nedre høyre hjørne indikasjonen på at det er Blockstreams enhet. Den grønne prikken ved siden av Blockstream-logoen indikerer at enheten er slått på og riktig koblet til det lokale nettverket.



![img](assets/en/43.webp)



## Mottak og bruk av transaksjoner



Fra _Receive_-menyen i Electrum, generate en `scriptPubKey` (adresse) for å motta midler. Begynn alltid med et lite beløp og gjør en mottak+bruk-test.



![img](assets/en/44.webp)



Når du har mottatt satellitter, kan du sjekke at de har kommet inn i _History_-menyen.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Når transaksjonen er bekreftet, kan du bruke denne UTXO og fullføre testen.



Utgiften innebærer å bruke Jade til å signere.



Gå til _Send_-menyen i Electrum, lim inn en scriptPubKey, og sjekk den godt.



![img](assets/en/47.webp)



Når du er ferdig, trykker du på _Pay_.



Transaksjonsvinduet åpnes, og her er det viktig å angi de riktige transaksjonsgebyrene. Når du er ferdig med alle innstillingene, klikker du på _Forhåndsvisning_ nederst i høyre hjørne.



![img](assets/en/48.webp)



Transaksjonsvinduet viser noen viktige detaljer, først og fremst status: `Unsignert`.



På dette stadiet kan du også se kommandoen _Sign_, som du må klikke på for å sette på signaturen med Jade.



![img](assets/en/49.webp)



Nå begynner en kommunikasjonsfase mellom displayet wallet og maskinvareenheten, der Electrum varsler deg om å følge instruksjonene på maskinvareenheten, som er slått på og klar til å signere.



![img](assets/en/50.webp)



**Først bør du imidlertid verifisere det du signerer: Alle parametrene for transaksjonen du nettopp har satt opp, vises også på Jade**, og du kan verifisere dem alle.



![img](assets/en/51.webp)



For å fortsette må du alltid plassere markøren på pilen "→" som fører til neste trinn, og aldri på "X", med mindre du vil avslutte operasjonen uten å fullføre den.



Bekreftelsesdelen avsluttes med at gebyret vises. På dette tidspunktet er bekreftelsen det samme som å skrive under.



![img](assets/en/52.webp)



Jade behandler operasjonen i et kort øyeblikk, og når den er ferdig, går den tilbake til startmenyen.



![img](assets/en/53.webp)



På Electrum kan du se statusen til transaksjonen, som har endret seg fra `Unsigned` til `Signed`, og nå er det mulig for deg å videreformidle den ved å klikke på _Broadcast_.



![img](assets/en/54.webp)



wallet, som er testet på denne måten, kan brukes til å ta imot UTXO beregnet på sikker lagring.



![img](assets/en/55.webp)



Denne veiledningen er et eksempel på hvordan du bruker Jade, tilkoblet via USB, til en wallet watch-only. Electrum er et klassisk eksempel, men du foretrekker kanskje annen wallet-programvare. Jade eksporterer den offentlige nøkkelen til mange andre lommebøker: finn lignende funksjoner som du leser om i denne veiledningen, for å veilede deg og finne ut hvordan du kan bruke den i din favoritt companio-app.