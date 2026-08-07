---
term: BTCPay Server

definition: Åpen kildekode-betalingsprosessor som lar deg akseptere bitcoin-betalinger uten mellomledd.
---

⚠️ **Kritisk sikkerhetsvarsel (7. august 2026):** en kritisk sårbarhet som rammer BTCPay Server utnyttes aktivt og kan føre til tap av midler. Oppdater instansen din til **versjon 2.4.2** umiddelbart via `Admin Dashboard > Server > Maintenance > Update`, og kontroller deretter at bunnteksten viser `2.4.2`. Hvis du ikke kan oppdatere med én gang, må du slå av BTCPay Server. Når du har oppdatert, må du også fornye macaroons og `macaroons.db` fullstendig, fornye autentiseringsstrengene til eventuelle andre Lightning-backender fullstendig, og hvis du har generert en varm on-chain-lommebok inne i BTCPay Server, må du flytte midlene og opprette lommeboken på nytt. Integratorer bør i tillegg oppdatere NBXplorer til versjon 2.6.10. Kilde: [Utgivelsesnotater for BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b
BTCPay Server er en betalingsprosessor med åpen kildekode som gjør det mulig for selgere og brukere å akseptere Bitcoin-betalinger uten å være avhengig av en tredjepart for transaksjonsbehandling. BTCPay Server ble lansert i 2017 og tilbyr en Bitcoin-betalingsintegrasjonsløsning for e-handelsnettsteder, med avanserte funksjoner som støtte for maskinvarelommebøker, fakturerings- og regnskapsverktøy, samt kompatibilitet med Lightning Network. Utviklingen ble initiert av Nicolas Dorier, som svar på handlingene til Bitpay, som ifølge ham hadde villedet sine brukere ved å presse dem mot å ta i bruk SegWit2x, som selskapet feilaktig anså som den "sanne" Bitcoin. Denne motstanden ble oppsummert i en nå berømt tweet fra Nicolas Dorier i august 2017:

> "_Dette er løgn, min tillit til deg er brutt, jeg vil gjøre deg foreldet_".
