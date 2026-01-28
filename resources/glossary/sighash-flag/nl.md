---
term: Sighash flag
definition: Parameter die bepaalt welke componenten van een transactie door de handtekening worden gedekt.
---

Een parameter in een Bitcoin transactie die bepaalt welke onderdelen van een transactie (inputs en outputs) gedekt worden door de bijbehorende handtekening, waardoor ze onveranderbaar worden. De SigHash Flag is een byte die aan de digitale handtekening van elke ingang wordt toegevoegd. Daarom heeft de keuze van de SigHash Flag direct invloed op welke delen van de transactie bevroren worden door de handtekening en welke achteraf nog gewijzigd kunnen worden. Dit mechanisme zorgt ervoor dat handtekeningen transactiegegevens nauwkeurig en veilig vastleggen volgens de bedoeling van de ondertekenaar. Er zijn drie belangrijke SigHash Flags:



- `SIGHASH_ALL` (`0x01`): De handtekening is van toepassing op alle in- en uitgangen van de transactie, waardoor ze volledig worden vergrendeld;



- `SIGHASH_NONE` (`0x02`): De handtekening geldt voor alle ingangen maar niet voor de uitgangen, waardoor de uitgangen na de handtekening kunnen worden gewijzigd;



- `SIGHASH_SINGLE` (`0x03`): De handtekening omvat alle ingangen en slechts één uitgang die overeenkomt met de index van de ondertekende ingang.


Naast deze drie SigHash Flags kan de modifier `SIGHASH_ANYONECANPAY` (`0x80`) gecombineerd worden met elk van de voorgaande types. Wanneer deze modifier wordt gebruikt, wordt slechts een deel van de invoer ondertekend, waarbij de rest kan worden gewijzigd. Hier zijn de bestaande combinaties met de modifier:



- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): De handtekening is van toepassing op een enkele invoer en dekt alle uitgangen van de transactie;



- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): De handtekening heeft betrekking op een enkele invoer, zonder zich vast te leggen op een uitvoer;



- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): De handtekening is van toepassing op een enkele invoer en alleen op de uitvoer die dezelfde index heeft als deze invoer.


> ► *Een synoniem dat soms gebruikt wordt voor "SigHash" is "Signature Hash Types".*