---
name: Voltz
description: Alt-i-ett Lightning wallet for virksomheten din.
---

![cover](assets/cover.webp)



Ideen til Voltz-plattformen kom fra en gruppe bitcoinere som ønsket å tilby sin egen bitcoin wallet-tjeneste. Resultatet ble en komplett infrastruktur for å ta imot bitcoin i detaljhandelen. I denne veiledningen tar vi deg med på en omvisning i Voltz og mulighetene plattformen tilbyr for bitcoin-integrasjon.



## Kom i gang med Voltz



I tillegg til å være en depotbasert Lightning wallet som lar deg sende, motta og betale daglig, er Voltz en komplett plattform som tilbyr en rekke utvidelser for å integrere bitcoin som et salgssted eller en markedsplass i virksomheten din.



Gå til [Voltz]-plattformen (https://www.lnvoltz.xyz/en) og opprett en konto ved å klikke på "Prøv nå"-knappen.



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ Det er viktig å angi et sterkt alfanumerisk passord for å øke sjansene dine mot brute-force-angrep, og sjekk at du faktisk er på det offisielle Voltz-nettstedet for å fylle inn påloggingsinformasjonen din for å beskytte deg mot phishing.



Voltz-grensesnittet er svært likt grensesnittet til LnBits-plattformen.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz er faktisk bygget på en LnBits-server. Ta en titt på veiledningen vår for å lære hvordan du monterer dine egne LnBits-servere og bygger løsningene dine på dem.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

Plattformen lar deg administrere flere porteføljer på en effektiv måte. Når du registrerer deg, har du som standard automatisk en Lightning-portefølje. Du kan imidlertid legge til andre porteføljer.



![wallets](assets/fr/03.webp)



### Bærbarhet



Voltz er ikke begrenset til et webgrensesnitt: I delen **Mobile Access** kan du koble din aktive Voltz wallet til applikasjoner som Zeus eller Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

For å gjøre dette må du installere og aktivere **LndHub**-utvidelsen på plattformen.



![lndhub](assets/fr/04.webp)



Velg din aktive Voltz-portefølje, og avhengig av hvilke rettigheter du ønsker å gi, skanner du den aktuelle QR-koden.




- QR-koden for fakturaer gir deg kun mulighet til å lese porteføljehistorikken din og generate nye fakturaer.
- Med QR-koden for administratorer kan du se historikk, generate-fakturaer og også betale lynfakturaer.



![qrs](assets/fr/05.webp)



I denne veiledningen kobler vi Voltz wallet til Blue Wallet-applikasjonen.



![connect](assets/fr/06.webp)



Når porteføljen vår er koblet til, vil alle handlinger som utføres synkroniseres mellom Blue Wallet og Voltz. Når du for eksempel generate en faktura på Blue Wallet, har du også en historikk på Voltz.



![sync](assets/fr/07.webp)



I delen **Porteføljekonfigurasjon** finner du minimale parametere som tilpasning av porteføljenavnet og valutaen du ønsker å motta betalingene dine i.



![config](assets/fr/08.webp)



### Utvidelser



En av de spesielle egenskapene til Voltz-plattformen er dens modularitet, slik at du kan aktivere de utvidelsene du trenger. Listen over utvidelser finner du i menyen **Utvidelser**.



![extensions](assets/fr/09.webp)



Blant disse utvidelsene er TPoS, en kasseterminal som du kan bruke til å føre varelager og samle inn betalinger fra kundene dine.



![tpos](assets/fr/10.webp)



Fra Point of Sale-terminalen kan du :




- Få en nettside du kan dele med kunder og samarbeidspartnere;
- Administrer produktbeholdningen;
- Generer Lightning-fakturaer;
- Kontant betaling via Bolt-kort.



Utvidelsen er tilgjengelig som en gratisversjon og som en betalingsversjon med mer avanserte funksjoner. For å opprette en POS-terminal klikker du på **Åpne**-knappen under logoen for utvidelsen, og deretter klikker du på **Nytt POS**.



![new_tpos](assets/fr/11.webp)



Definer navnet på utsalgsstedet ditt, og koble deretter Voltz wallet til terminalen for å samle inn betalinger. Du kan aktivere drikkepenger ved å krysse av i boksen **Aktivér drikkepenger**. Aktiver også alternativet for fakturautskrift hvis du ønsker å skrive ut kvitteringer til kundene dine (denne funksjonaliteten er fortsatt under utvikling, så det kan forekomme feil).



Salgsterminalen inkluderer også skattekonfigurasjon når du ønsker å bruke ditt lands skatt direkte på produktene dine.



![tpos](assets/fr/12.webp)



Når POS-terminalen er opprettet, kan du legge til forhåndskonfigurerte produkter og tjenester for å sikre en smidig betalings- og regnskapsopplevelse for deg og kundene dine.



![product](assets/fr/13.webp)



Opprett produktene dine ved å definere navn, legge til et bilde og angi en salgspris.  Du kan kategorisere produktene dine for enklere sporing. Du kan legge til avgifter direkte på et bestemt produkt. Hvis produktet ikke har noen avgift, vil avgiften som er konfigurert ved opprettelsen av salgsterminalen, automatisk bli lagt til.



![products](assets/fr/14.webp)



Du kan importere produktlisten din automatisk fra et JSON-format ved å klikke på **Importer/Eksporter**-knappen.



![exports](assets/fr/15.webp)



Få tilgang til kasseområdet via lenken ved å klikke på ikonet **Ny fane**, eller del POS-plattformen din via QR-kode med kundene dine ved å klikke på ikonet **QR-kode**.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



Kundene dine kan se katalogen din og foreta betalingen fra dette grensesnittet.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



I gruppen av tilgjengelige utvidelser finner du også verktøy som **Invoice** og **Payment Link**, som lar deg generate-fakturaer med spesifikke produkter for å samle inn isolerte betalinger uten å gå gjennom POS-terminalen.



## Hold oversikt over betalingene dine



I menyen **Payments** gir Voltz deg en oversikt over betalinger til de ulike porteføljene dine.


Du kan spore betalingene dine ved å :




- Status.
- Etiketten: for eksempel **TPOS** for betaling på utsalgsstedet og **lnhub** via mobiltilkoblingen i Zeus- og Blue Wallet-lommebøker.
- Samlingsporteføljen.
- Summen av inngående og utgående betalinger.
- En veldefinert periode.



![payments](assets/fr/22.webp)



## Flere alternativer



Voltz er også en infrastruktur som du kan bygge dine egne løsninger på. I delen **Utvidelser** finner du en guide til hvordan du utvikler dine egne utvidelser innenfor Voltz' og LnBits' økosystem.



![build](assets/fr/23.webp)



Hvis du ønsker å utvikle løsninger utenfor økosystemet, men likevel bruke infrastrukturen deres, finner du i delen **URL for node** API-nøkler og dokumentasjonsinformasjon med et eksempel på hva du kan gjøre med disse dataene.



Du kan opprette Lightning-fakturaer fra applikasjonene dine ved hjelp av Voltz wallet, betale Lightning-fakturaer, dekode og verifisere fakturaer.



![keys](assets/fr/24.webp)



Du har nå en god forståelse av Voltz. Hvis du likte denne opplæringen, er vi sikre på at du vil lære mer om de beste metodene og verktøyene for å integrere bitcoin i virksomheten din med kurset vårt: Bitcoin for bedrifter.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a