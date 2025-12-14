---
term: BIP0044
---

Een voorstel voor verbetering dat een standaard hiërarchische afleidingsstructuur introduceert voor HD-wallets. BIP44 bouwt voort op de principes van BIP32 voor sleutelafleiding en op BIP43 voor het gebruik van het veld "doel". Het introduceert een afleidingsstructuur met vijf niveaus: `m / doel' / munttype' / rekening' / wijziging / adres_index`. Hier zijn de details van elke diepte:


- `m /` geeft de master private sleutel aan. Het is uniek voor een Wallet en kan geen broers of zussen hebben op dezelfde diepte. De hoofdsleutel is direct afgeleid van de seed van de Wallet;
- `m / purpose' /` geeft het afleidingsdoel aan dat helpt bij het identificeren van de gevolgde standaard. Dit veld wordt beschreven in BIP43. Bijvoorbeeld, als de Wallet de BIP84 (SegWit V0) standaard volgt, dan zou de index `84'` zijn;
- `m / doel' / Coin-type' /` geeft het type cryptocurrency aan. Dit maakt een duidelijk onderscheid mogelijk tussen takken die gewijd zijn aan de ene cryptocurrency en takken die gewijd zijn aan een andere cryptocurrency in een Wallet met meerdere Coin. De index gewijd aan Bitcoin is `0'`;
- `m / doel' / Coin-type' / rekening' /` geeft het rekeningnummer aan. Met deze diepte kan een Wallet gemakkelijk worden onderscheiden en georganiseerd in verschillende accounts. Deze accounts zijn genummerd vanaf `0'`. Uitgebreide sleutels (`xpub`, `xprv`...) worden op deze diepte gevonden;
- `m / purpose' / Coin-type' / account' / change /` geeft de keten aan. Elk account zoals gedefinieerd in diepte 3 heeft twee ketens op diepte 4: een externe keten en een interne keten (ook wel "verandering" genoemd). De externe keten leidt adressen af die bedoeld zijn om publiekelijk te communiceren, d.w.z. de adressen die ons worden aangeboden wanneer we op "ontvangen" klikken in onze Wallet software. De interne keten leidt adressen af die niet bedoeld zijn om publiekelijk uitgewisseld te worden, d.w.z. voornamelijk wijzigingsadressen. De externe keten wordt geïdentificeerd met de index `0` en de interne keten met de index `1`. Je zult merken dat we vanaf deze diepte niet langer een verharde afleiding uitvoeren, maar een normale afleiding (er is geen apostrof). Dankzij dit mechanisme zijn we in staat om alle child public keys af te leiden van hun `xpub`;
- `m / doel' / Coin-type' / rekening' / wijziging / Address-index` geeft eenvoudig het nummer van de ontvangende Address en zijn sleutelpaar aan, om het te onderscheiden van zijn broers en zussen op dezelfde diepte op dezelfde tak. Bijvoorbeeld, de eerste afgeleide Address heeft de index `0`, de tweede Address heeft de index `1`, enzovoort...

Als mijn ontvangende Address bijvoorbeeld het afleidingspad `m / 86' / 0' / 0' / 0 / 5` heeft, dan kunnen we de volgende informatie afleiden:


- `86'` geeft aan dat we de afleidingsstandaard van BIP86 (Taproot of SegWitV1) volgen;
- `0'` geeft aan dat het een Bitcoin Address is;
- `0'` geeft aan dat we op de eerste rekening van de Wallet zijn;
- `0` geeft aan dat het een externe Address is;
- `5` geeft aan dat het de zesde externe Address van deze rekening is.