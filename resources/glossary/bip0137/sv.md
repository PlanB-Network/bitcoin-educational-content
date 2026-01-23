---
term: BIP0137
definition: Standardiserat format för att signera meddelanden med en privat Bitcoin-nyckel för att bevisa ägarskap av en adress.
---

Föreslår ett standardiserat format för att signera meddelanden med privata Bitcoin-nycklar och deras tillhörande adresser, för att bevisa Ownership för en Address. Denna BIP syftar till att lösa tvetydigheten relaterad till de olika typerna av Bitcoin-adresser (P2PKH, P2SH, P2WPKH ...) vid signering av ett meddelande. Den introducerar en metod för att uttryckligen särskilja dessa Address-format genom signaturer. Dessa signaturer är användbara för olika tillämpningar som t.ex. bevis på medel, revision och andra användningar som kräver autentisering av en Address via dess privata nyckel. BIP322 har sedan dess introducerat ett nytt signaturformat som gör det möjligt att utöka denna standard och generalisera den för alla typer av skript.