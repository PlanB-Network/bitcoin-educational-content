---
term: Overt ASICBoost
definition: Transparent version av AsicBoost som manipulerar nVersion-fältet för att optimera mining.
---

Den öppna och transparenta versionen av AsicBoost. AsicBoost är en algoritmisk optimeringsteknik som används i Bitcoin Mining. Miners som använder Overt-versionen manipulerar `nVersion`-fältet i kandidatblocket och använder denna modifiering som en ytterligare Nonce. Denna metod lämnar det faktiska `Nonce`-fältet i blocket oförändrat under varje hashningsförsök, vilket minskar de beräkningar som krävs för varje SHA256, genom att hålla vissa data desamma mellan försöken. Den här versionen kan upptäckas offentligt och döljer inte sina ändringar från resten av nätverket, till skillnad från den hemliga versionen av AsicBoost.