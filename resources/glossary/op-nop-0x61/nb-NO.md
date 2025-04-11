---
term: OP_NOP (0X61)

---
Gir ingen effekt på stakken eller skriptets tilstand. Den utfører ingen bevegelser, kontroller eller modifikasjoner. Den gjør rett og slett ingenting, med mindre noe annet er bestemt via en soft fork. Siden Satoshi Nakamoto modifiserte dem i 2010, har `OP_NOP`-kommandoene (`OP_NOP1` (`0XB0`) til `OP_NOP10` (`0XB9`)) blitt brukt til å legge til nye opkoder i form av en soft fork.

Dermed har `OP_NOP2` (`0XB1`) og `OP_NOP3` (`0XB2`) allerede blitt brukt til å implementere henholdsvis `OP_CHECKLOCKTIMEVERIFY` og `OP_CHECKSEQUENCEVERIFY`. De brukes i kombinasjon med `OP_DROP` for å fjerne de tilhørende temporale verdiene fra stakken, slik at skriptets kjøring kan fortsette, uansett om noden er oppdatert eller ikke. Med `OP_NOP`-kommandoene kan man derfor sette inn et avbruddspunkt i et skript for å sjekke om det finnes flere betingelser som allerede eksisterer, eller som kan bli lagt til med fremtidige soft forks. Siden Tapscript har bruken av `OP_NOP` blitt erstattet av den mer effektive `OP_SUCCESS`.