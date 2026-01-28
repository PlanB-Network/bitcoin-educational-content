---
term: PRNG
definition: Algoritm som genererar sekvenser av nästan slumpmässiga tal från ett frö (seed).
---

Förkortning för "Pseudoslumptalsgenerator". GNPA är en klass av algoritmer som används för att generate-sekvenser av ungefärliga slumptal, med utgångspunkt från ett initialt tillstånd som kallas seed (seed). Inom kryptografi används GNPA för att generate-nycklar, initialiseringsvektorer och andra Elements som kräver slumpmässighet. En bra GNPA måste ha egenskaper som enhetlighet i utdata, oförutsägbarhet och motståndskraft mot prediktiva attacker. Till skillnad från riktiga slumptalsgeneratorer är GNPA deterministiska och reproducerbara. På Bitcoin kan GNPA:er användas i programvara för portföljhantering eller i hårdvaruplånböcker, för att på generate återskapa den återvinningsfras som ligger till grund för deterministiska och hierarkiska portföljer.