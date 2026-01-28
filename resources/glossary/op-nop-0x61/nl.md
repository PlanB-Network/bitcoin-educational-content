---
term: OP_NOP (0X61)
definition: Opcode die geen effect heeft, gebruikt als invoegpunt voor toekomstige soft forks.
---

Heeft geen effect op de stack of de status van het script. Het voert geen bewegingen, controles of wijzigingen uit. Het doet gewoon niets, tenzij anders besloten wordt via een Soft Fork. Inderdaad, sinds hun aanpassing door Satoshi Nakamoto in 2010, worden de `OP_NOP` commando's (`OP_NOP1` (`0XB0`) tot `OP_NOP10` (`0XB9`)) gebruikt om nieuwe opcodes toe te voegen in de vorm van een Soft Fork.


Zo zijn `OP_NOP2` (`0XB1`) en `OP_NOP3` (`0XB2`) al gebruikt om respectievelijk `OP_CHECKLOCKTIMEVERIFY` en `OP_CHECKSEQUENCEVERIFY` te implementeren. Ze worden gebruikt in combinatie met `OP_DROP` om de geassocieerde tijdelijke waarden van de stack te verwijderen, waardoor de uitvoering van het script door kan gaan, of het knooppunt nu up-to-date is of niet. De `OP_NOP` commando's maken het dus mogelijk om een onderbrekingspunt in een script in te voegen om te controleren op aanvullende voorwaarden die al bestaan of toegevoegd kunnen worden met toekomstige Soft forks. Sinds Tapscript is het gebruik van `OP_NOP` vervangen door het efficiëntere `OP_SUCCESS`.