---
term: OP_SUCCESS
definition: Opcodes gereserveerd in Tapscript die automatisch succes aangeven, gebruikt voor toekomstige soft forks.
---

De `OP_SUCCESS` vertegenwoordigen een reeks opcodes die in het verleden uitgeschakeld waren en nu gereserveerd zijn voor toekomstig gebruik in Tapscript. Hun uiteindelijke doel is om updates en uitbreidingen van de scripttaal te vergemakkelijken, door de introductie van nieuwe functionaliteiten via Soft forks mogelijk te maken. Wanneer een van deze opcodes voorkomt in een script, geeft dit aan dat dat deel van het script automatisch is geslaagd, ongeacht de aanwezige gegevens of condities. Dit betekent dat het script doorgaat met de uitvoering zonder te falen, onafhankelijk van de voorgaande bewerkingen.


Dus, wanneer een nieuwe opcode wordt toegevoegd aan een `OP_SUCCESS`, vertegenwoordigt dit noodzakelijkerwijs de toevoeging van een meer beperkende regel dan de vorige. Geüpdatete knooppunten kunnen dan de naleving van deze regel verifiëren, en knooppunten die niet zijn geüpdatet zullen de geassocieerde transacties en de blokken die ze bevatten niet weigeren, omdat de `OP_SUCCESS` dat deel van het script valideert. Daarom is er geen Hard Fork.


Ter vergelijking, de `OP_NOP` (*No Operation*) dienen ook als plaatshouders in het script, maar ze hebben geen effect op de uitvoering van het script. Wanneer een `OP_NOP` wordt tegengekomen, gaat het script gewoon verder zonder de toestand van de stack of de voortgang van het script te veranderen. Het belangrijkste verschil zit dus in hun invloed op de uitvoering: `OP_SUCCESS` garandeert een succesvolle doorgang door dat deel van het script, terwijl `OP_NOP` neutraal is en geen invloed heeft op de stack of de voortgang van het script. Deze opcodes worden aangeduid met `OP_SUCCESSN` waarbij `N` een getal is dat wordt gebruikt om de `OP_SUCCESS` te onderscheiden.