---
term: Kontrollsumma
definition: Beräknat värde för att verifiera dataintegritet, som används i adresser och återställningsfraser.
---

Kontrollsumman är ett värde som beräknas från en uppsättning data och som används för att verifiera integriteten och giltigheten hos dessa data under överföring eller lagring. Checksummealgoritmer är utformade för att upptäcka oavsiktliga fel eller oavsiktliga ändringar av data, t.ex. överföringsfel eller filkorruption. Det finns olika typer av checksummealgoritmer, t.ex. paritetskontroller, modulära checksummor, kryptografiska Hash-funktioner eller BCH-koder (*Bose, Ray-Chaudhuri och Hocquenghem*).


På Bitcoin används kontrollsummor på applikationsnivå för att säkerställa integriteten hos mottagande adresser. En kontrollsumma beräknas från nyttolasten i en användares Address och läggs sedan till i Address för att upptäcka eventuella fel i dess inmatning. En kontrollsumma finns också i återställningsfraser (mnemonics).


