---
name: BIP-39 Passphrase Trezor
description: Hvordan legger jeg til en passphrase i Trezor-porteføljen min?
---
![cover](assets/cover.webp)



En passphrase BIP39 er et valgfritt passord som, kombinert med Mnemonic-frasen, gir en ekstra Layer av sikkerhet for deterministiske og hierarkiske Bitcoin-porteføljer. I denne veiledningen vil vi sammen finne ut hvordan du setter opp en passphrase på din sikre Bitcoin Wallet på en Trezor (Safe 3, Safe 5 og Model One).



![Image](assets/fr/01.webp)



Hvis du ikke er kjent med passphrase-konseptet, hvordan det fungerer og hvilke konsekvenser det har for din Bitcoin Wallet, anbefaler jeg på det sterkeste at du leser denne andre teoretiske artikkelen der jeg forklarer alt (dette er veldig viktig, ettersom bruk av en passphrase uten å forstå hvordan den fungerer kan sette bitcoinsene dine i fare) :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase på Trezor håndteres på klassisk måte hvis du har valgt BIP39-standarden under konfigurasjonen (noe jeg anbefaler hvis du ikke trenger *Multi-share Backup*). Det spesielle med Trezor er at du enten kan taste inn passphrase direkte på Hardware Wallet, eller via datamaskinens tastatur ved hjelp av Trezor Suite-programvaren. Det andre alternativet er betydelig mindre sikkert, ettersom datamaskinen har en mye større angrepsflate enn Hardware Wallet. Det kan imidlertid være raskere å skrive en kompleks passphrase på et vanlig tastatur enn på Hardware Wallet, noe som kan oppmuntre til bruk av sterke passordfraser. Derfor er det alltid bedre å bruke en passphrase, selv om den må tastes inn, enn å ikke bruke en i det hele tatt. Det er imidlertid viktig å være oppmerksom på den økte risikoen for numeriske angrep som dette innebærer.



Disse alternativene er ikke tilgjengelige på alle Trezor-kompatible porteføljeforvaltningsprogrammer. For Model One kan passphrase for eksempel legges inn via tastaturet på Sparrow Wallet. For modellene Model T, Safe 3 og Safe 5 må du enten bruke Trezor Suite eller legge inn passphrase direkte på Hardware Wallet, ettersom muligheten til å legge inn passphrase via Sparrow ble deaktivert av HWI for noen år siden.



![Image](assets/fr/02.webp)



I Trezor Suite har du to forskjellige måter å administrere passphrase-etterspørsel på. Du kan aktivere alternativet "*passphrase*" i fanen "*Enhet*". Hvis dette er aktivert, vil Trezor Suite og all annen programvare for porteføljeforvaltning systematisk be deg om å angi passphrase hver gang du starter opp. Hvis du foretrekker en mer diskret tilnærming til bruk av passphrase, kan du beholde innstillingen på "*Standard*". I så fall må du manuelt gå inn i menyen til Hardware Wallet øverst i venstre hjørne og klikke på "*+ passphrase*"-knappen hver gang du starter den.



Før du starter denne veiledningen, må du forsikre deg om at du allerede har initialisert Trezor og generert Mnemonic-frasen din. Hvis du ikke har gjort det, og Trezor er ny, følger du den modellspesifikke veiledningen som er tilgjengelig på Plan ₿ Network. Når du har fullført dette trinnet, kan du gå tilbake til denne veiledningen.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Legge til en passphrase til en Safe 3 eller Safe 5



Når du har opprettet din Wallet, lagret din Mnemonic og angitt en PIN-kode, kommer du til Trezor Suite-startmenyen. Øverst i venstre hjørne vises et vindu som inviterer deg til å aktivere passphrase BIP39.



![Image](assets/fr/03.webp)



Hvis dette vinduet ikke vises, må du aktivere alternativet "*passphrase*" manuelt i innstillingsfanen "*Device*".



![Image](assets/fr/04.webp)



I dette vinduet blir du bedt om å oppgi din passphrase. Velg en sterk passphrase og ta umiddelbart en fysisk sikkerhetskopi, på et medium som papir eller metall. I dette eksempelet har jeg valgt passphrase: `fH3&kL@9mP#2sD5qR!82`. Dette er et eksempel, men jeg anbefaler at du velger en litt lengre passphrase. Mellom 30 og 40 tegn vil være ideelt (som et godt passord).



du bør selvfølgelig aldri dele din passphrase på Internett, slik jeg gjør i denne veiledningen. Dette eksemplet Wallet vil bare bli brukt på Testnet og vil bli slettet ved slutten av veiledningen



For mer spesifikke anbefalinger om valg av passphrase, vil jeg igjen invitere deg til å lese denne andre artikkelen:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Hvis du vil legge inn passphrase via tastaturet på datamaskinen, skriver du den inn i feltet, og klikker deretter på "*Access passphrase Wallet*".



![Image](assets/fr/05.webp)



Hardware Wallet vil da vise passphrase. Kontroller at den stemmer overens med den fysiske sikkerhetskopien (papir eller metall) før du klikker på skjermen for å fortsette.



![Image](assets/fr/06.webp)



Dette gir deg tilgang til den passphrase-beskyttede porteføljen din.



![Image](assets/fr/07.webp)



Hvis du foretrekker å øke sikkerheten ved å legge inn passphrase kun på Trezor, klikker du på "*Enter passphrase on Trezor*" når du blir bedt om det.



![Image](assets/fr/08.webp)



Et T9-tastatur vises på Trezor, slik at du kan taste inn passphrase. Når du er ferdig med inntastingen, klikker du på Green-krysset for å bruke passphrase på Wallet.



![Image](assets/fr/09.webp)



Du vil da ha tilgang til din sikre passphrase Wallet.



![Image](assets/fr/10.webp)



For å bruke Sparrow Wallet er fremgangsmåten den samme, men for modellene T, Safe 3 og Safe 5 må passphrase tastes inn på Hardware Wallet og ikke via tastaturet på datamaskinen.



Når Sparrow Wallet krever tilgang til Trezor, og passphrase ikke har blitt brukt siden forrige oppstart, må du taste den inn ved hjelp av T9-tastaturet.



![Image](assets/fr/11.webp)



## Legge til en passphrase til en Model One



På Model One er bruken av en passphrase BIP39 nesten uunnværlig. Ettersom denne enheten ikke har et Secure Element, er det relativt enkelt å hente ut sensitiv informasjon. Den er derfor ikke motstandsdyktig mot fysiske angrep. Ettersom passphrase ikke beholdes på enheten etter at den er slått av, kan bruk av en sterk (ikke-bruteable) passphrase imidlertid beskytte deg mot de fleste kjente fysiske angrep på denne modellen.



På Model One er det ikke mulig å taste inn passphrase direkte på Hardware Wallet. Du må taste den inn via tastaturet på datamaskinen.



Når du har opprettet din Wallet, lagret din Mnemonic og angitt en PIN-kode, kommer du til Trezor Suite-startmenyen. Øverst i venstre hjørne vises et vindu som inviterer deg til å aktivere passphrase BIP39.



![Image](assets/fr/12.webp)



Hvis dette vinduet ikke vises, må du aktivere alternativet "*passphrase*" i fanen "*Device*" i innstillingene.



![Image](assets/fr/13.webp)



I dette vinduet blir du bedt om å oppgi din passphrase. Velg en sterk passphrase og ta umiddelbart en fysisk sikkerhetskopi, på et medium som papir eller metall. I dette eksempelet har jeg valgt passphrase: `fH3&kL@9mP#2sD5qR!82`. Dette er bare et eksempel, men jeg anbefaler at du velger en litt lengre passphrase. Mellom 30 og 40 tegn vil være ideelt (som et godt passord).



For mer spesifikke anbefalinger om valg av passphrase, vil jeg igjen invitere deg til å lese denne andre artikkelen:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Skriv inn din passphrase i det angitte feltet, og klikk deretter på knappen "*Access passphrase Wallet*".



![Image](assets/fr/14.webp)



Hardware Wallet vil vise din passphrase. Kontroller at den stemmer overens med den fysiske sikkerhetskopien (papir eller metall), og klikk deretter på høyre knapp for å fortsette.



![Image](assets/fr/15.webp)



Dette tar deg til den passphrase-beskyttede porteføljen din.



![Image](assets/fr/16.webp)



For å bruke Sparrow Wallet deretter, er prosedyren den samme. Hver gang Sparrow krever tilgang til din Hardware Wallet, og passphrase ikke har blitt lagt inn siden enheten sist ble startet opp, må du legge den inn.



![Image](assets/fr/17.webp)



Gratulerer, du er nå i gang med å bruke passphrase BIP39 på Trezor maskinvare-lommebøker. Hvis du vil ta Wallet-sikkerheten et skritt videre, kan du ta en titt på denne veiledningen om Trezors *Multi-share*-sikkerhetskopieringssystemer (*Shamirs hemmelige delingsordning*):



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Hvis du fant denne opplæringen nyttig, ville jeg være takknemlig hvis du legger igjen en Green-tommel nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Tusen takk skal du ha!