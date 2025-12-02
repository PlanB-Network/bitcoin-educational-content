---
name: Public Pool
description: Introduksjon til Public Pool
---

![signup](assets/cover.webp)

**Public Pool** er ikke bare et hvilket som helst basseng; det er det som også er kjent som en **Solo Pool**. Hvis din [miner](https://planb.academy/resources/glossary/miner) lykkes i å mine en blokk, så samler du inn hele blokkbelønningen, som ikke deles med andre deltakere i bassenget eller med bassenget selv.

**Public Pool** tilbyr kun en **blokkmal** for din miner slik at den kan utføre sin oppgave uten at du trenger å ha en **Bitcoin node** og programvaren som kommuniserer med din miner. Siden du ikke samler din databehandlingskraft med den til andre deltakere, er sjansene dine for å lykkes med å mine en blokk åpenbart veldig lave, noe som ligner litt på et lotterisystem, der noen ganger en heldig person vinner jackpotten.

![signup](assets/1.webp)

På **Dashboardet** til **Public Pool**, har du fortsatt noen statistikker som bassengets **Totale Hashrate** samt en fordeling av de forskjellige typene minere som er koblet til bassenget.

![signup](assets/2.webp)

I de første linjene kan vi se **Bitaxe** med 1323 **Bitaxe** koblet til for en total på 649TH/s. **Bitaxe** er et **Open source** prosjekt som tillater enkel gjenbruk av en chip fra en **[ASIC](https://planb.academy/resources/glossary/asic)** som **Antminer S19** på et **opensource** elektronisk kort for å lage en liten miner på 0.5TH/s for 15W. Dette er mineren vi vil bruke som et eksempel for denne opplæringen.

## Legge til en **Worker** 👷‍♂️

![signup](assets/cover.webp)

Øverst på siden kan du kopiere bassengadressen **stratum+tcp://public-pool.io:21496**.

Deretter, for **bruker**-feltet, skriv inn en **Bitcoin**-adresse som du eier.

Hvis du har flere minere, kan du skrive inn samme adresse for alle sammen slik at deres **hashrates** kombineres og vises som en enkelt miner. Du kan også skille dem ved å legge til et distinkt navn til hver. For å gjøre dette, legg ganske enkelt til **.workername** etter **Bitcoin**-adressen.

Til slutt, for **passord**-feltet, bruk **‘x’**.

Eksempel: Hvis din **Bitcoin**-adresse er **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’** og du ønsker å navngi din miner **« Brrrr »**, så ville du skrive inn følgende informasjon i din miners grensesnitt:

- **URL**: stratum+tcp://public-pool.io:21496
- **BRUKER**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Passord**: **‘x’**
Hvis din miner er en **Bitaxe**, er feltene litt forskjellige, men informasjonen forblir den samme:
- **URL**: public-pool.io (her trenger du å fjerne delen i begynnelsen **‘stratum+tcp://’** og delen på slutten **‘:21496’** som vil bli rapportert i portfeltet)
- **Port**: 21496
- **Bruker**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Passord**: **‘x’**

![signup](assets/3.webp)
Noen få minutter etter at du starter med mining, vil du kunne se dataene dine på **Public Pool**-nettstedet ved å søke etter adressen din.

## Dashboard

![signup](assets/4.webp)

Når du er koblet til **Public Pool**, kan du få tilgang til **Dashboardet** ditt ved å søke med **Bitcoin**-adressen du oppga i **Bruker**-feltet. I vårt tilfelle her, er det **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’**.

På **Dashboardet** vises forskjellig informasjon både om dataene dine og om nettverket.

![signup](assets/5.webp)

Du har **Network Hash Rate** som tilsvarer den totale arbeidskraften til **Bitcoin**-nettverket.

**Network Difficulty** indikerer vanskelighetsgraden som må nås for å validere en blokk.

Og **Your Best Difficulty** er den høyeste vanskelighetsgraden du har nådd. Hvis du, ved en tilfeldighet 🍀, når nettverksvanskeligheten, så vinner du hele blokkbelønningen... etter 100 blokker. Du må vente 100 blokker før du kan bruke dem.

Du har også **Block Height** som er nummeret på den siste blokken som ble minet, samt dens vekt uttrykt i WU, maksimumet er 4,000,000.

Nedenfor kan du se alle statistikkene for hver av enhetene dine individuelt hvis du har gitt dem et distinkt navn ved å legge til **.name** bak **Bitcoin**-adressen din i **Bruker**-feltet.