---
term: Invoice lightning
definition: Lightning-betalingsverzoek dat alle informatie bevat die nodig is om de transactie te voltooien.
---

Lightning betalingsverzoek gegenereerd door de ontvanger, met alle informatie die nodig is om de transactie te voltooien.


Een Invoice Lightning bevat de bestemming van de betaling in de vorm van de openbare sleutel van het ontvangende knooppunt, maar ook een `LN` prefix, het bedrag, een tijd tot de vervaldatum, de Hash van het geheim dat wordt gebruikt in HTLC's en andere metadata, waarvan sommige optioneel zijn, zoals routeringsopties. Deze facturen worden gedefinieerd door de BOLT11 standaard. Eenmaal betaald, kan een Invoice Lightning niet hergebruikt worden.


