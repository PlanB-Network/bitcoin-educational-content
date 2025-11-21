---
term: ATOMÆRE BETALINGER MED FLERE VEIER
---

Forbedret versjon av MPP (*Multi-Path Payments*), der hvert betalingsfragment har en egen partiell hemmelighet, noe som sikrer at transaksjonen gjøres opp atomisk, dvs. i sin helhet eller ikke i det hele tatt.


MPP-er er betalingsteknikker i Lightning som gjør det mulig å dele opp en transaksjon i flere mindre deler og rute den via ulike ruter. Med andre ord tar hver betalingsfraksjon en annen nodebane. På denne måten omgår man likviditetsbegrensninger på én enkelt kanal i ruten. I grunnleggende MPP-er deler hver betalingsfraksjon den samme hemmeligheten, og derfor den samme Hash i HTLC-er. Dette kan gjøre transaksjonen sporbar hvis en observatør er til stede på flere ruter, ettersom han kan koble alle disse identiske hemmelighetene sammen. Fordi hemmeligheten er unik for alle deler av betalingen, er den heller ikke atomisk. Det betyr at noen deler av betalingen kan bli utført med suksess, mens andre kan mislykkes.


I AMP brukes unike delhemmeligheter for hver fraksjon. Når alle fragmentene er mottatt, kan mottakeren rekonstruere den opprinnelige generelle hemmeligheten og kreve full betaling. Denne metoden gjør det umulig å gjøre opp betalingen delvis, ettersom det kreves at man er i besittelse av alle delhemmelighetene for å låse opp hele betalingen. Dette sikrer at betalingen er helt vellykket eller helt mislykket (dvs. atomisk). AMP forbedrer også konfidensialiteten, ettersom det ikke lenger finnes noen synlige koblinger mellom ulike ruter.


En fordel med AMP er at de fungerer selv om bare mottakeren og avsenderen har implementert denne metoden. Mellomliggende noder behandler disse betalingene som konvensjonelle transaksjoner ved hjelp av HTLC-er, uten å være klar over at de behandler deler av en større betaling.