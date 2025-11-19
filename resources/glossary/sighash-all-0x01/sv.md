---
term: SIGHASH_ALL (0X01)
---

Typ av SigHash Flagga som används i Bitcoin-transaktionssignaturer för att ange att signaturen gäller för alla komponenter i transaktionen. Genom att använda `SIGHASH_ALL` täcker undertecknaren alla ingångar och alla utgångar. Detta innebär att varken inmatningar eller utmatningar kan modifieras efter signaturen utan att den ogiltigförklaras. Denna typ av SigHash-flagga är den vanligaste i Bitcoin-transaktioner, eftersom den säkerställer fullständig slutgiltighet och integritet för transaktionen.