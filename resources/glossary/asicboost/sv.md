---
term: Asicboost
definition: En algoritmisk optimering som möjliggör en ökning av gruvdriftseffektiviteten med cirka 20% genom att återanvända en del av hasch-beräkningarna mellan flera försök.
---

ASICBOOST är en algoritmisk optimeringsmetod som uppfanns 2016 och som är utformad för att öka effektiviteten i Bitcoin Mining med cirka 20% genom att minska mängden beräkningar som behövs för varje Hash-försök av rubriken. Denna teknik utnyttjar en funktion i SHA256 Hash-funktionen, som används för Mining, som delar upp data i block innan de bearbetas. ASICBOOST behåller ett av dessa block oförändrat över flera hashningsförsök, vilket gör att Miner bara behöver göra en del av arbetet för detta block över flera försök. Denna datadelning gör det möjligt att återanvända resultat från tidigare beräkningar och därmed minska det totala antalet beräkningar som krävs för att hitta en giltig Hash.


ASICBOOST kan användas i två former: Overt ASICBOOST och Covert ASICBOOST. Overt ASICBOOST-formen är synlig för alla, eftersom den innebär att blockets `nVersion`-fält används som en Nonce, och inte ändrar den verkliga `Nonce`. Covert-formen försöker dölja dessa modifieringar genom att använda Merkle-träd. Denna andra metod har dock blivit mindre effektiv sedan introduktionen av SegWit på grund av den andra Merkle Tree, vilket ökar antalet beräkningar som krävs för att använda den.


Sammanfattningsvis gör ASICBOOST att gruvarbetare inte behöver utföra en fullständig SHA256 för alla hashförsök, eftersom en del av resultatet förblir oförändrat, vilket påskyndar gruvarbetarnas arbete.