---
term: RBF (REPLACE-BY-FEE)

---
En transaksjonsmekanisme som gjør det mulig for avsenderen å erstatte en transaksjon med en annen ved å betale høyere gebyrer, for å fremskynde bekreftelsen. Hvis en transaksjon med for lave gebyrer blir sittende fast, kan avsenderen bruke *Replace-By-Fee* til å øke gebyrene og prioritere erstatningstransaksjonen i mempoolene.

RBF gjelder så lenge transaksjonen befinner seg i mempoolene; når den først er i en blokk, kan den ikke lenger erstattes. Ved første sending må transaksjonen angi at den er tilgjengelig for erstatning ved å justere verdien `nSequence` til et tall som er mindre enn `0xfffffffffe`. Dette kalles et RBF-"flagg". Denne innstillingen signaliserer at det er mulig å oppdatere transaksjonen etter at den har blitt sendt ut, noe som gjør det mulig med en RBF. Noen ganger er det imidlertid mulig å erstatte en transaksjon som ikke har signalisert RBF. Noder som bruker konfigurasjonsparameteren `mempoolfullrbf=1`, godtar denne erstatningen selv om RBF ikke ble signalisert i utgangspunktet.

I motsetning til CPFP (*Child Pays For Parent*), der mottakeren kan handle for å fremskynde transaksjonen, lar RBF (*Replace-By-Fee*) avsenderen ta initiativ til å fremskynde sin egen transaksjon ved å øke gebyrene.