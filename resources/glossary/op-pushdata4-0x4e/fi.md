---
term: OP_PUSHDATA4 (0X4E)

definition: Opcode, joka lisää erittäin suuria määriä dataa pinoon (harvoin käytetty).
---
Mahdollistaa hyvin suuren tietomäärän työntämisen pinoon. Sitä seuraa neljä tavua (little-endian), jotka ilmaisevat työnnettävän datan pituuden (enintään noin 4,3 GB). Tätä op-koodia käytetään hyvin suurten tietojen lisäämiseen skripteihin, vaikka sen käyttö on erittäin harvinaista transaktiokokoa koskevien käytännön rajoitusten vuoksi.
