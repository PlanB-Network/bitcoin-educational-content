---
termi: HWI
---

Lyhenne sanoista "*Hardware Wallet Interface*" eli laitteistolompakon rajapinta. Se on standardoitu rajapinta, joka helpottaa integraatiota ja vuorovaikutusta Bitcoin-lompakon hallintasovellusten ja laitteistolompakoiden välillä. Erityisesti HWI on sekä Python-kirjasto että komentorivityökalu. Se helpottaa näiden komponenttien välistä kommunikaatiota käyttämällä PSBT:itä (Partially Signed Bitcoin Transactions) ja mahdollisesti Descriptoreita (output script descriptors). Tämä rajapinta kehitettiin alun perin Bitcoin Corea varten, ja sen jälkeen siitä tuli standardi, jota useimmat lompakkosovellukset käyttävät.