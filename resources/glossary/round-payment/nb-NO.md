---
term: RUND BETALING

---
En intern heuristikk for kjedeanalyse på Bitcoin som muliggjør en hypotese om arten av utgangene til en transaksjon basert på runde beløp. Generelt, når man står overfor et enkelt betalingsmønster (1 inngang og 2 utganger), hvis en av utgangene bruker et rundt beløp, så representerer den betalingen. Ved eliminering, hvis den ene utgangen representerer betalingen, representerer den andre endringen. Det kan derfor tolkes som at det er sannsynlig at brukeren som legger inn transaksjonen, fortsatt har den utgangen som er identifisert som endringen.

Det er verdt å merke seg at denne heuristikken ikke alltid er anvendelig, siden de fleste betalinger fortsatt gjøres i fiat-valutaenheter. Når en forhandler i Frankrike aksepterer bitcoin, viser de vanligvis ikke stabile priser i sats. De vil heller velge en konvertering mellom prisen i euro og beløpet i bitcoins som skal betales gjennom POS (som for eksempel BTCPay Server). Derfor bør det ikke være et rundt tall i transaksjonsutgangen. En analytiker kan likevel forsøke å gjøre denne konverteringen ved å ta hensyn til valutakursen som gjaldt da transaksjonen ble sendt ut i nettverket. Hvis bitcoin en dag blir den foretrukne regningsenheten på børsene våre, kan denne heuristikken bli enda mer nyttig for analyser.

![](../../dictionnaire/assets/11.webp)