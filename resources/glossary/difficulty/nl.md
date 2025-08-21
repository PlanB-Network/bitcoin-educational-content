---
term: MOEILIJKHEIDSGRAAD
---

Een instelbare parameter die de complexiteit van de Proof of Work bepaalt die nodig is om een nieuw blok toe te voegen aan de Blockchain en de bijbehorende beloning te verdienen. Deze moeilijkheid wordt weergegeven door het moeilijkheidsdoel, een 256-bits waarde die de bovengrens bepaalt waaraan de Hash van de blokkop moet voldoen om als geldig beschouwd te worden. Het doel is dat de Hash, bereikt door een dubbele uitvoering van SHA256 (SHA256d), kleiner is dan of gelijk is aan dit doel. Om deze Hash te bereiken, manipuleren miners de `Nonce` in de block header. De moeilijkheidsgraad wordt elke 2016 blokken aangepast, of ongeveer elke twee weken, om de gemiddelde tijd voor het aanmaken van een blok op ongeveer 10 minuten te houden.