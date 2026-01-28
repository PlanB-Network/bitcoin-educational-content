---
term: Macaroon
definition: Autentiseringsmekanism som används på Lightning för att säkra åtkomst till fjärrtjänster.
---

En autentiseringsmekanism som är utformad för att säkra åtkomst till tjänster i distribuerade system. Macaroons används framför allt på Lightning för att autentisera användare när de får tillgång till delegerade tjänster. Med en Lightning-nod är det till exempel möjligt att generate en macaroon som auktoriserar utförandet av transaktioner från din smartphone via din fjärrnod. Till skillnad från cookies har macaroons fördelen att de valideras kryptografiskt av utfärdaren eller delegeras för verifiering.