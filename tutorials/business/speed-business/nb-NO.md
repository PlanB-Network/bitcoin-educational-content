---
name: Hastighet Wallet - PoS
description: Integrer enkelt Bitcoin- og stablecoin-betalinger i virksomheten din
---
![cover](assets/cover.webp)



Den verdensomspennende adopsjonen av Bitcoin er basert på konkrete brukstilfeller i hverdagen. Bruken av Bitcoin i umiddelbare kommersielle transaksjoner over hele verden forsterker denne adopsjonen hos både store institusjoner og små bedrifter. I denne veiledningen tar vi en titt på Speed Business, en enhetlig betalingsplattform som gjør det mulig for bedriften din å ta imot Bitcoin-betalinger via Lightning.



![btc-session](https://www.youtube.com/watch?v=ywUNZ_sxr0Q)



## Kom i gang med Speed Business



[Speed Business] (https://www.tryspeed.com/) er en plattform utviklet av [Speed Wallet] (https://www.speed.app/) som gjør det mulig for alle selgere å integrere umiddelbare, rimelige Bitcoin- og stablecoin-betalinger.



Speed har et bredt spekter av funksjoner for å dekke de økonomiske aspektene ved virksomheten din. Du finner:





- Konfigurasjon for nettbetaling**: Motta betalinger fra kundene dine uansett hvor de befinner seg, takket være nettstedet ditt.





- Betalinger på stedet**: Ideell for butikker og virksomheter som tar imot kontanter i butikken.





- Uttak**: Ta ut eiendelene dine uten problemer og bruk bitcoins til å betale tilbake kunder og lønninger.





- Tilkobling til andre plattformer**: Bruker du eksterne verktøy for å administrere betalingene dine? Speed gir deg muligheten til å koble dem til plattformen, slik at du får et alt-i-ett-økosystem som gjenspeiler virksomheten din.



Opprett kontoen din på [Speed] (https://app.tryspeed.com/register/), så begynner vi å sette opp betalinger for bedriften din.



![account-creation](assets/fr/01.webp)



Gi informasjon til Speed Wallet, slik at han kan hjelpe deg med å forenkle plattformen i henhold til din erfaring med Bitcoin og Lightning Network



![onboard](assets/fr/02.webp)



Speed leveres med et programvareutviklingskit som lar deg tilpasse integrasjonen, og en utvidelse for standard integrasjon.



I denne veiledningen skal vi jobbe med en standard integrasjon ved hjelp av utvidelsen fra Speed.



For å gjøre opplevelsen enklere, tilbyr Speed en testmodus som lar deg prøve ut de ulike funksjonene uten å måtte bekymre deg for hvordan de påvirker butikkadministrasjonen.



![test-data](assets/fr/03.webp)



Du kan teste alle aspektene som dekkes i denne opplæringen, ved hjelp av testmodus.



Når du deaktiverer testmodus, må du konfigurere uttaksporteføljen din.



![configure-wallet](assets/fr/04.webp)



Hvis du ennå ikke eier en Bitcoin og/eller Lightning Wallet, anbefaler vi at du tar en titt på våre [mobile lommebøker] veiledninger (https://planb.network/tutorials/wallet).



https://planb.network/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

⚠️ **VIKTIG**: Når du konfigurerer porteføljen din, bør du velge typen **BTC (On-Chain)** når du mottar store beløp, i størrelsesorden tusenvis av euro, for å sikre pålitelig bekreftelse på Bitcoin, og typen **LN Address** når du ønsker å motta øyeblikkelige mikrobetalinger i virksomheten din.



![setup-wallet](assets/fr/05.webp)



Bekreft deretter at porteføljen din er lagt til ved hjelp av bekreftelses-e-posten som Speed sender.



![verfication](assets/fr/06.webp)



Definer minsteuttaket og minimumssaldoen som du ikke kan ta ut midlene dine under.



![payout](assets/fr/07.webp)



## Legg til produktene dine



I delen **Produkter** legger du til katalogen over produktene du selger i butikken din.



![product-creation](assets/fr/08.webp)



Trykk på **Neste** for å fortsette å definere produktet og dets funksjoner.



![product-details](assets/fr/09.webp)



Deretter definerer du produktets salgspris.



![product-price](assets/fr/10.webp)



Disse produktene gjør det mulig for deg å bruke generate-betalingslenker slik at kundene dine kan betale for dem.



## Mottak av betalinger



Speed Wallet gir deg muligheten til å bruke flere metoder for å motta betalinger på nett eller på stedet i virksomheten din.



I menyen **Motta betalinger > Betalinger** finner du historikken over mottatte betalinger og deres status (betalt, utløpt, ubetalt, kansellert).



![payments](assets/fr/11.webp)





- Betalingslenker ligger i alternativet **Kassekoblinger** og lar deg sette opp unike betalingssider for produktene dine.



![checkout-link](assets/fr/12.webp)



Avhengig av behovene dine kan du konfigurere og tilpasse betalingssiden til å motta betalinger på et bestemt beløp.



![configure-checkout](assets/fr/13.webp)



![finalize-checkout](assets/fr/14.webp)



Du finner listen over betalingslenker du har satt opp i kontoen din i menyen **Betalingslenker**.





- Fakturaer: Med Speed kan du sende generate-tilbud og fakturaer til kundene dine.



![invoices](assets/fr/16.webp)



Velg en kunde du allerede har registrert, eller opprett enkelt din egen.



Når du angir valutaen, får du tilgang til listen over produkter som er konfigurert i den aktuelle valutaen.



Du kan sende denne Invoice i PDF-format, via e-post, eller generate en QR-kodelink til skanning (ideelt for butikker som samler inn på stedet), slik at kunden kan betale Invoice.



![configure-invoice](assets/fr/17.webp)






- I menyen **Betalingsadresser** kan du sette opp en Lyn-Address som du kan motta flere betalinger av varierende størrelse til.



![addresses](assets/fr/19.webp)



⚠️ Du kan legge til og bruke andre domenenavn enn Speed sine. Vi anbefaler imidlertid at du bruker standardkonfigurasjonen for første gang, slik at du kan dra nytte av all ekspertisen til Speed Business' tekniske support.





- Den **En QR**: Ideell for betaling på stedet. Opprett en QR-kode som er knyttet til bedriften din, slik at kundene kan betale for produktene dine.



![one-qr](assets/fr/20.webp)



## Utfør betalinger fra Speed



Speed business samler ikke bare inn betalinger for virksomheten din, det er en portefølje som lar deg administrere hele den økonomiske siden av virksomheten din uten problemer.



I menyen **Send betalinger** finner du alle alternativene speed har å tilby for pengeoverføringer.





- Øyeblikkelige betalinger**: Med Instant Send-alternativet kan du sende bitcoins sikkert og umiddelbart fra selgerkontoen din.





- generate uttakslenker** som gjør det mulig for partnere og leverandører å få tilgang til betalingen på et senere tidspunkt uten at du trenger å være til stede på nettet.



I alternativet **Utbetalingslenker** oppretter du en ny uttakslenke og konfigurerer den ved å definere valuta, beløp og et passord for å sikre mottakerens transaksjon.



![withdrawal-links](assets/fr/21.webp)



⚠️Les uttakslenker kan bare brukes én gang, og vi anbefaler på det sterkeste at du angir et unikt passord for hver lenke, ellers kan hvem som helst som er i besittelse av lenken, ta ut beløpet som er angitt på uttakslenken.





- Utbetalinger**: I menyen Utbetalinger kan du starte uttak fra Speed Business-saldoen din til din personlige Wallet.



![payouts](assets/fr/22.webp)





- Rabatter**: Oppmuntre stamkundene dine ved å sette opp rabattalternativer for å opptjene bonuser.



![cashbacks](assets/fr/23.webp)



## Explorer Speed Business



Speed Business er en plattform med flere valutaer som lar deg holde separate porteføljer i ett og samme system.



I **Saldoer**-alternativet finner du saldoen i Bitcoin-, USDT- og USDC-porteføljene dine.



![balance](assets/fr/24.webp)



I likhet med Speed Wallet, i **Swap**-menyen, lar Speed Business deg Exchange valutaer mellom de forskjellige valutaporteføljene dine (BTC, USDT, USDC) for så lite som Sats 20 000 (rundt $ 20 til gjeldende kurs).



![swap](assets/fr/25.webp)



I **Transfer**-menyen kan du kommunisere med andre forhandlere og enkelt overføre bitcoins ved hjelp av deres Speed ID.



![transferts](assets/fr/26.webp)



I menyen **Kunder** kan du lagre og se listen over kundene dine (enkeltpersoner eller selskaper).



![customers](assets/fr/27.webp)



Tjen belønninger ved å delta i Speeds partnerprogram.



I menyen **Partnere** kan du invitere selgere til å etablere virksomheten sin på Speed business og tjene passiv inntekt.



![partners](assets/fr/28.webp)



## Integrer Speed i bedriftens nettsted



Speed Business har et utviklingskit som lar deg integrere betalingsløsningen på ditt eget nettsted.



I **Utviklere**-menyen oppretter du offentlige og private nøkler for å bruke Speed Wallet API-metoder.



Finn den komplette [dokumentasjonen] (https://apidocs.tryspeed.com/reference/introduction) for bedre integrering av Speed Business.



![developers](assets/fr/29.webp)



## Tilpass virksomheten din



I menyen **Innstillinger** kan du konfigurere forhandlerprofilen og bedriftsinformasjonen din.



I delen **Forretningsinnstillinger**:





- Rediger opplysningene om kjøpmannskontoen din, for eksempel navn, sted og tidssone.





- Sjekk hvilke tillatelser som er aktivert (motta betaling, sende Bitcoin, Exchange, overføre, ta ut) på kontoen din i menyen **Kontostatus**.





- Definer uttakslommebøkene dine i menyen **Payout Wallets**, og konfigurer dem i menyen **Payout Scheduling**.





- Definer de grafiske retningslinjene for virksomheten din, og tilpass betalingssider, e-post, QR-koder og fakturaer etter eget ønske i menyen **Branding**.





- Konfigurer betalingsmetoder i aksepterte valutaer i menyen **Betalingsmetode**.



![payment-method](assets/fr/30.webp)



⚠️ Toleransen tilsvarer den prosentvise reduksjonen du aksepterer på Invoice-beløpet for at en betaling skal anses som gyldig. Hvis kunden må betale USD 100 og toleransen din er 1 %, vil enhver betaling på USD 99 validere Invoice-beløpet på USD 100.





Du har fått en god forståelse av Speed, integrerer Bitcoin i virksomheten din og utvikler din lokale sirkulære økonomi basert på Bitcoin. Hvis du synes denne veiledningen var nyttig, er vi sikre på at du vil like vår sveitsiske Bitcoin Pay-veiledning like godt.



https://planb.network/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

