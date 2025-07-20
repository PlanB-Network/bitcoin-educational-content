---
name: Misty Breez
description: Den bukløse Lightning Wallet.
---

![misty-breez-cover](assets/cover.webp)



Misty Breez er en Lightning selvholdende Wallet utviklet av Breez basert på deres Software Development Kit og **Liquid**-nettverket utviklet av BlockStream.


Den kommer med en helt ny tilnærming til drift uten en Lightning-node: en potensiell **GAME CHANGER** i Bitcoin-overføringer mellom nettverk.


I denne veiledningen beskriver vi hvordan denne porteføljen fungerer og gir deg en fullstendig oversikt.



## Hvordan fungerer Misty Breez?



Misty Breez er en implementering uten Lightning node som backend. Den er utviklet på grunnlag av Breez SDK og Liquid.



Liquid er en parallell Layer til Bitcoin-nettverket, og tilbyr betydelige forbedringer i hastighet og transaksjonskostnader. Denne Layer gjør det mulig for Misty Breez å droppe en Lightning-node og i stedet bruke tredjeparts Exchange-tjenester som **Boltz** for å sikre interoperabilitet mellom Liquid Network og Lightning Network. Ikke hastverk, vi kommer tilbake til dette.



La oss starte eventyret vårt med Misty Breez Wallet.



## Kom i gang med Misty Breez



Misty Breez-mobilappen er tilgjengelig på offisielle nedlastingsplattformer som Google Play Store (på Android) og Apple Store (på iOS). Du kan også bli omdirigert til riktig app fra det offisielle [Misty Breez]-nettstedet (https://breez.technology/misty/).



⚠️ Pass på at du ikke forveksler Misty Breez med Breez Wallet.



⚠️ **VIKTIG**: For sikkerheten til bitcoinsene dine er det viktig å laste ned applikasjonen fra offisielle plattformer for å sikre dens autentisitet.



![download-misty-breez](assets/fr/01.webp)



I denne veiledningen tar vi utgangspunkt i en Android-enhet. Likevel gjelder alle trinnene og de spesifikke funksjonene som beskrives i denne delen, også for iOS.



Ved installasjon gir Misty Breez deg muligheten til å opprette en ny Wallet eller gjenopprette en gammel Lightning Wallet som du har gjenopprettingsord for.


I denne veiledningen velger vi å opprette en ny portefølje.



⚠️Misty Breez er for tiden i utviklingsfasen, så vi anbefaler deg å starte med rimelige beløp.



![create-wallet](assets/fr/02.webp)


### Lagre gjenopprettingsordene dine :


Noe av det første du bør gjøre når du oppretter en ny portefølje, er å sikkerhetskopiere de 12 recovery-ordene dine.


Her er noen tips om hvordan du tar sikkerhetskopi av backupfrasen din.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

For å sikkerhetskopiere frasene dine velger du menyen **Innstillinger > Sikkerhet** og deretter alternativet **Sjekk sikkerhetskopifrasen din**.



![backup](assets/fr/03.webp)


For ekstra sikkerhet kan du også **opprette en PIN-kode** for å autentisere tilgangen til Wallet.




Finn din lokale valuta blant de mange valutaene som aksepteres av Misty Breez. Konfigurer valutaen din i menyen **Innstillinger > Fiat-valutaer**, og velg deretter den eller de valutaene du ønsker.



![devises](assets/fr/04.webp)



### Gjør dine første transaksjoner


Hvis du allerede er kjent med Breez-porteføljen, vil du ikke bli avskrekket av Misty Breez' intuitive Interface.



På menyen **Balanse** i Interface klikker du på alternativet **Mottak** for å opprette fakturaer for å motta bitcoins på Wallet.



⚠️ Misty Breez vil be deg om å aktivere varsler for applikasjonen i telefonens innstillinger for å gi deg rett til en Lightning Address.



Med Misty Breez kan du :




- Motta bitcoins på Lightning Network fra **100 satoshis** opp til **25 000 000 satoshis**.
- Motta bitcoins på Bitcoin-hovednettverket fra **25 000 satoshis**.



![transactions](assets/fr/05.webp)



Det er her magien med Misty Breez begynner.


I motsetning til Breez Wallet, som gir deg en Lightning-node og ber deg om å dekke kostnadene ved å åpne og lukke betalingskanaler selv, ber Misty Breez deg ikke om å gjøre noe som helst. Som nevnt tidligere fungerer Misty Breez ikke engang på grunnlag av en Lightning-node.



La oss ta en nærmere titt bak kulissene.



I virkeligheten eier du en Liquid-portefølje som er knyttet til Misty Breez-porteføljen din. Logisk sett vil du håndtere L-BTC (Liquid Bitcoin) til faste kurser knyttet til tredjeparts ubåt-satoshi-konverteringstjenester som vil gjøre deg i stand til å samhandle med Lightning Network.



Når du mottar en betaling på din Misty Breez Wallet, sender avsenderen deg satoshier som vil gå gjennom en konverteringstjeneste som Boltz (for tiden brukt av Misty Breez), for å konvertere satoshiene som sendes til L-BTC som vil bli mottatt på din Misty Breez Wallet (tilknyttet Liquid Wallet).


Her er et forenklet diagram over prosessen bak kulissene.



![lnswap-in](assets/fr/06.webp)



Klikk på Interface i menyen **Saldo**, klikk på alternativet **Send** for å betale en Lyn-Invoice.


Sett inn Lightning Invoice, mottakerens Lightning Address eller bare skann QR-koden på Invoice for å utføre betalingen.



![send-bitcoins](assets/fr/07.webp)



Bak kulissene aktiverer du Liquid Wallet tilknyttet Misty Breez Wallet for å konvertere tilsvarende L-BTC til satoshier via Boltz, og deretter overfører du disse satoshiene til mottakerens Lightning Wallet (som finnes på Lightning Network).



![send-bitcoin-bts](assets/fr/08.webp)



Denne funksjonen i Misty Breez' infrastruktur gjør det mulig for brukere å utføre transaksjoner selv når Misty Breez er frakoblet.



For de mer erfarne finnes det også en meny **Preferences > Developers** som gir deg litt mer informasjon om :




- Versjonen av Breez Software Development Kit.
- Den offentlige nøkkelen til Misty Breez Wallet.
- Låntakeren, den unike identifikatoren som er utledet fra den primære offentlige nøkkelen.
- Porteføljebalansen din.
- Tips Liquid, for å sende små mengder L-BTC.
- Bitcoin-tipset, for sending av små mengder Bitcoin.



Du kan også utføre visse handlinger, for eksempel synkronisere med Liquid Network, sikkerhetskopiere nøklene dine, dele aktivitetsloggen din og velge å skanne Liquid Network på nytt.



![dev-mode](assets/fr/09.webp)


Vi gratulerer! Du har nå en god forståelse av Misty Breez-porteføljen og dens bidrag til Bitcoin-nettverkstransaksjoner. Hvis du har funnet denne veiledningen nyttig, vennligst gi oss en Green-tommel. Vi vil bli glade for å høre fra deg.



For å gå videre, anbefaler jeg også at du oppdager vår veiledning om Aqua Wallet, som fungerer på samme måte som Misty Breez :



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125