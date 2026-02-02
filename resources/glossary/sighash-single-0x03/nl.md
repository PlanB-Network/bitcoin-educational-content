---
term: SIGHASH_SINGLE (0X03)
definition: SigHash-vlag die elke ondertekende input koppelt aan de bijbehorende output op dezelfde index.
---

Type SigHash Flag gebruikt in Bitcoin transactiehandtekeningen om aan te geven dat de handtekening geldt voor alle ingangen van de transactie en slechts voor één uitgang, die overeenkomt met de index van dezelfde ondertekende ingang. Dus, elke input ondertekend met `SIGHASH_SINGLE` is specifiek gekoppeld aan een bepaalde output. De andere uitgangen worden niet vastgelegd door de handtekening en kunnen dus later gewijzigd worden. Dit type handtekening is handig bij complexe transacties, waarbij deelnemers bepaalde inputs aan specifieke outputs willen koppelen, terwijl er flexibiliteit overblijft voor de andere outputs van de transactie.