---
term: Invoice LIGHTNING
---

Lynbetalingsforespørsel generert av mottakeren, som inneholder all informasjon som trengs for å fullføre transaksjonen.


En Invoice Lightning inneholder betalingsdestinasjonen i form av mottakernodens offentlige nøkkel, men også et LN-prefiks, beløpet, en utløpstid, Hash for hemmeligheten som brukes i HTLC-er, og andre metadata, hvorav noen er valgfrie, for eksempel rutingsalternativer. Disse fakturaene er definert av BOLT11-standarden. Når en Invoice Lightning er betalt, kan den ikke brukes på nytt.


> på fransk kan vi oversette "Invoice" med "facture", men vi bruker vanligvis det engelske begrepet også på fransk