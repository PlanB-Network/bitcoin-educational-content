---
term: Offer
definition: Herbruikbare statische QR-codes voor het ontvangen van meerdere betalingen op Lightning (BOLT12).
---

In BOLT12 zijn *aanbiedingen* statische QR-codes voor het doen van meerdere betalingen op Lightning Network. In tegenstelling tot conventionele facturen kunnen *aanbiedingen* worden hergebruikt. Ze kunnen worden gebruikt om meerdere generate en Invoice aanvragen te doen. Wanneer een gebruiker een QR-code scant die een *aanbieding* bevat, stuurt hij een bericht met een verzoek voor een nieuwe Invoice naar het bijbehorende Lightning-knooppunt. Het knooppunt antwoordt met een Invoice die de betaler kan gebruiken. De *aanbiedingen* bieden dus een unieke identificatie voor het ontvangen van meerdere betalingen van verschillende gebruikers op Lightning.