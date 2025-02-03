---
term: BIP137

---
Foreslår et standardisert format for signering av meldinger med private Bitcoin-nøkler og tilhørende adresser, for å bevise eierskap av en adresse. Denne BIP-en har som mål å løse tvetydigheten knyttet til de ulike typene Bitcoin-adresser (P2PKH, P2SH, P2WPKH ...) ved signering av en melding. Den introduserer en metode for å eksplisitt skille mellom disse adresseformatene gjennom signaturer. Disse signaturene er nyttige for ulike bruksområder, for eksempel bevis på midler, revisjon og andre bruksområder som krever autentisering av en adresse via dens private nøkkel. BIP322 har siden introdusert et nytt signaturformat som gjør det mulig å utvide denne standarden og generalisere den for alle typer skript.