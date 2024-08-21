---
termi: OP_PUSHDATA4 (0X4E)
---

Mahdollistaa erittäin suuren määrän datan siirtämisen pinoon. Sitä seuraa neljä tavua (little-endian), jotka ilmoittavat työntöön tulevan datan pituuden (jopa noin 4,3 GB asti). Tätä operaatiokoodia käytetään erittäin suurten datamäärien sisällyttämiseen skripteihin, vaikkakin sen käyttö on äärimmäisen harvinaista käytännön rajoitusten vuoksi siirtokoon suhteen.