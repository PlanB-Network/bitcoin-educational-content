---
term: OP_PUSHDATA2 (0X4D)

definition: Opcode, joka lisää pinoon enintään 65 KB dataa.
---
Mahdollistaa suuren tietomäärän työntämisen pinoon. Sitä seuraa kaksi tavua (little-endian), jotka määrittävät työnnettävän datan pituuden (enintään noin 65 KB). Sitä käytetään isompien tietojen lisäämiseen skripteihin.
