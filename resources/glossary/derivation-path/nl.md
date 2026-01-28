---
term: Afleidingspad
definition: Reeks indexen die het afleidingspad beschrijven van kind-sleutels vanaf de mastersleutel in een HD-wallet.
---

In de context van Hierarchical Deterministic (HD) wallets verwijst een afleidingspad naar de reeks indexen die gebruikt worden om kindsleutels af te leiden van een hoofdsleutel. Dit pad wordt beschreven in BIP32 en identificeert de boomstructuur voor het afleiden van kindsleutels. Een afleidingspad wordt weergegeven door een reeks indexen gescheiden door schuine strepen en begint altijd met de hoofdsleutel (aangeduid als `m/`). Een typisch pad is bijvoorbeeld `m/84'/0'/0'/0/0`. Elk afleidingsniveau wordt geassocieerd met een specifieke diepte:


- `m /` geeft de private hoofdsleutel aan. Het is uniek voor een Wallet en kan geen broers of zussen hebben op dezelfde diepte. De hoofdsleutel wordt direct van de seed afgeleid;
- `m / purpose' /` geeft het afleidingsdoel aan dat helpt om de gevolgde standaard te identificeren. Dit veld wordt beschreven in BIP43. Bijvoorbeeld, als de Wallet voldoet aan de BIP84 standaard (SegWit V0), dan zou de index `84'` zijn;
- `m / doel' / Coin-type' /` geeft het type cryptocurrency aan. Dit maakt een duidelijk onderscheid mogelijk tussen branches die gewijd zijn aan de ene cryptocurrency en branches die gewijd zijn aan een andere in een Wallet met meerdere GW's. De index gewijd aan Bitcoin is `0'`;
- `m / doel' / Coin-type' / account' /` geeft het rekeningnummer aan. Deze diepte maakt het gemakkelijk om een Wallet te onderscheiden en te organiseren in verschillende accounts. Deze accounts zijn genummerd vanaf `0'`. Uitgebreide sleutels (`xpub`, `xprv`...) worden op dit diepteniveau gevonden;
- `m / purpose' / Coin-type' / account' / change /` geeft het pad aan. Elk account zoals gedefinieerd op diepte 3 heeft twee paden op diepte 4: een externe keten en een interne keten (ook wel "verandering" genoemd). De externe keten leidt adressen af die bedoeld zijn om publiekelijk te worden gedeeld, dat wil zeggen, de adressen die ons worden aangeboden wanneer we op "ontvangen" klikken in onze Wallet software. De interne keten leidt adressen af die niet bedoeld zijn om publiekelijk uitgewisseld te worden, voornamelijk wijzigingsadressen. De externe keten wordt geïdentificeerd met de index `0` en de interne keten met de index `1`. Je zult merken dat we vanaf deze diepte niet langer een verharde afleiding uitvoeren, maar een normale afleiding (er is geen apostrof). Het is dankzij dit mechanisme dat we in staat zijn om alle child public keys af te leiden van hun `xpub`;



- `m / doel' / Coin-type' / rekening' / wijziging / Address-index` geeft eenvoudig het nummer van de ontvangende Address en zijn sleutelpaar aan, om het te onderscheiden van zijn broers en zussen op dezelfde diepte op dezelfde tak. Bijvoorbeeld, de eerste afgeleide Address heeft de index `0`, de tweede Address heeft de index `1`, enzovoort...


Als mijn ontvangende Address bijvoorbeeld het afleidingspad `m / 86' / 0' / 0' / 0 / 5` heeft, dan kunnen we de volgende informatie afleiden:


- `86'` geeft aan dat we de afleidingsnorm van BIP86 (Taproot / SegWit V1) volgen;
- `0'` geeft aan dat het een Bitcoin Address is;
- `0'` geeft aan dat we op de eerste rekening van de Wallet zijn;
- `0` geeft aan dat het een externe Address is;
- `5` geeft aan dat het de zesde externe Address van deze rekening is.


