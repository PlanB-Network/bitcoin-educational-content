---
name: Canaan Avalon Mini 3
description: Konfigurera din ASIC Avalon för solomining eller Miner pooling
---

![cover](assets/cover.webp)



I den här handledningen tittar vi på hur du ställer in Canaan Avalon Mini 3, för enkel hemanvändning av Miner.



Fram till nu har ASIC-maskiner (*Application Specific Integrated Circuit*) som är särskilt utformade för att utföra en viss uppgift - i det här fallet Hash-beräkning (SHA-256) för Miner av Bitcoin - varit särskilt olämpliga för hushållsbruk. Det störande bullret, värmen som alstras och behovet av att anpassa elinstallationen för att klara av den enorma kraften i dessa enheter hindrade de flesta av oss från att delta.



Idag har Canaan, en av de ledande tillverkarna av ASIC-maskiner, bestämt sig för att ta sig an marknaden för privatpersoner som vill ha Miner hemma, genom att erbjuda ett sortiment av produkter som är relativt tysta och mycket enkla att installera (plug & play).



Dessa enheter marknadsförs antingen som en extra värmare, som i fallet med **Avalon Nano 3S (140W)**, eller som en miniradiator med en effekt på **800W**, som i fallet med **Avalon Mini 3**.



https://planb.network/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Observera att prisskillnaden mot traditionella värmare med motsvarande effekt i de allra flesta fall inte gör det möjligt för dig att göra en ekonomisk vinst. De satoshis som genereras av Mining:s verksamhet kommer aldrig att kompensera för denna prisskillnad, såvida du inte har tillgång till gratis (överskott) eller mycket billig el.



Enligt min mening bör dessa enheter ses mer som ett enkelt sätt att Miner hemma för dem som vill göra det av personliga skäl: *få icke-KYC Satss / spela "lotteriet" genom att solominera / delta i Hashrate decentralisering etc..*. samtidigt som man drar nytta ** som en bonus** av den värme som genereras för att värma sitt rum på vintern. Men inte som ett sätt att spara pengar i de flesta fall åtminstone (västländer).



## Unboxing och funktioner



### Avalon Nano 3S



Låt oss först se vad som finns i Avalon Mini 3-lådan.



![image](assets/fr/24.webp)



När du öppnar lådan ligger bruksanvisningen rakt framför dig, men ännu viktigare är att WIFI-mottagarmodulen är dold under det runda vita klistermärket till vänster om bruksanvisningen. Du kommer att behöva den senare.



![image](assets/fr/25.webp)



Under skumblocket finns enheten, och när den tagits ur lådan finns strömmen Supply-enheten.



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## Starta och ansluta till det lokala nätverket



När du har packat upp din Avalon Mini 3, placera den i ett relativt öppet utrymme, om möjligt, så att värmen kan cirkulera ordentligt. Börja sedan med att sätta in den lilla WIFI-mottagarmodulen i USB-porten på enhetens undersida, koppla in strömmen Supply och se till att strömbrytaren är i läge "1".



![image](assets/fr/28.webp)



När dessa steg har slutförts tänds enhetens LED-display och visar symbolen "Bluetooth", vilket indikerar att den är redo att anslutas till ditt lokala nätverk via Avalon Family-applikationen.



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



För att göra detta, gå till din mobilapplikationsbutik, sök efter och ladda ner **Avalon Family**-applikationen.



![image](assets/fr/11.webp)


När du har installerat programmet öppnar du det genom att klicka på "Skip" i det övre högra hörnet, sedan på knappen "Add" och slutligen på "Search". Se till att du har Bluetooth aktiverat på din smartphone, så att detektering av enheten går smidigt.



![image](assets/fr/12.webp)


När enheten har upptäckts av programmet klickar du på den och väljer "Connect". Du kommer då till en skärm där du kan ange dina WIFI-anslutningsuppgifter.


![image](assets/fr/13.webp)


När du är ansluten till ditt lokala nätverk visar Mini 3 information som IP Address, tid, Hashrate och strömförsörjning.



Nedan följer en sammanfattande tabell över Mini 3:s allmänna tekniska specifikationer:



| Caractéristique                                      | Valeur                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consommation électrique                              | 800 W                                                     |
| Bruit                                                | 35-55 dB                                                  |
| Température de l'air en sortie                       | 60-70°C (sous température ambiante 25°C)                  |
| Exigences de température ambiante pour l'utilisation | -5° C - 40°C                                              |
| Plage d'entrée de l'appareil                         | 110V-240V AC 50/60Hz                                      |
| Taille de la machine                                 | Longueur: 760 mm / Profondeur: 104 mm / Hauteur: 214.5 mm |
| Poids de la machine                                  |  8.35 kg                                                  |

## Anslutning till en Mining pool



**Den här delen är gemensam för Nano 3s och Mini 3 eftersom processerna är helt identiska **



Oavsett om vi vill "solominera" eller Miner "poola", måste vi ansluta till en Mining pool. Faktum är att vår enhet inte är något annat än en Hash-tillverkare utan någon medvetenhet om Bitcoin-nätverket. Genom att ansluta den till en pool får den tillgång till Bitcoin-nätverket och kan ta emot blockmallar att arbeta med.



### Använda applikationen för att ansluta till en Mining pool



I Avalon Family-applikationen väljer du enheten enligt bilden nedan. Du kommer då automatiskt att bli ombedd att ändra maskinens administratörslösenord. Klicka på "OK" om du vill göra det, eller på "Avbryt" om du vill behålla standardlösenordet "admin".


![image](assets/fr/16.webp)


Välj sedan "Settings", sedan "Pool Config" och ange parametrarna för de 3 begärda poolerna.


Poolerna #2 och #3 kommer att fungera som säkerhetskopior om en av dem skulle gå sönder, så att din Miner inte fungerar i onödan. Som standard kommer Hashrate att pekas till pool #1



I vårt fall väljer vi:




- 1 - Allmän pool,
- 2 - CkPool,
- 3 - Ocean.



![image](assets/fr/17.webp)



Mer information om hur du ansluter till en Mining pool finns i dessa handledningar :



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.network/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Sammanfattningsvis behöver vi





- poolen Address, vanligtvis **stratum+tcp://xxxxxxxx:port**.





- namnet på "arbetaren" som består av *din Bitcoin Address* och det *pseudo* du väljer för din enhet, de 2 åtskilda av en *punkt*, till exempel:**bc1qxxxxxxxxxxxxxxx.MonAvalonNano3S**





- lösenordet, som vanligtvis alltid är "**x**"



När poolinformationen har matats in klickar du på "Spara".



![image](assets/fr/18.webp)


Starta om enheten enligt anvisningarna och vänta några minuter tills din Hashrate är riktad mot önskad pool (#1).



### Använda webbläsaren för att ansluta till en Mining pool



Du kan också ansluta till en Mining pool och, mer allmänt, komma åt enhetens Interface-hanteringssystem via din favoritwebbläsare.



För att göra detta skriver du in IP Address för den enhet som visas på skärmen nedan i webbläsarens sökfält, i vårt exempel **192.168.144.6**



![image](assets/fr/15.webp)



Följande sida visas, där du ombeds att öppna Avalon Family-applikationen och skanna QR-koden som visas med applikationen.



![image](assets/fr/20.webp)



Öppna programmet och klicka på de 3 strecken längst upp till höger och sedan på scan. Skanna webbläsarens QR-kod, ange sedan programmets administratörslösenord och klicka på OK.



![image](assets/fr/21.webp)



Här är du på webbsidan som låter dig interagera med din Avalon. Det är mer av en instrumentpanel för att visa maskinens mätvärden än ett sätt att konfigurera den.



Men poolinställningarna kan fortfarande nås på detta sätt, genom att klicka på **"Pool Config"** i det nedre högra hörnet.



![image](assets/fr/22.webp)



På samma sätt som med mobilapplikationen kan du ange dina poolparametrar här.



![image](assets/fr/23.webp)



## Styr din enhet via Avalon Family-appen



Vi har nu anslutit vår Miner till vårt lokala nätverk och riktat vår Hashrate mot Minings-pooler. Låt oss nu upptäcka de viktigaste funktionerna i vår maskin genom Avalon Family-applikationen.



I huvudmenyn för Avalon-familjens applikation klickar du på ikonen som motsvarar Avalon Mini 3. Du kommer då direkt till menyn för hantering av driftlägen.



3 alternativ finns tillgängliga: "Värme"-läge, "Mining"-läge eller "Natt"-läge.





- I läget "Heater" har du 2 effektnivåer "Eco" eller "Super".


"Eco"-nivån motsvarar en värmeeffekt på 500 W för en Hashrate på ca 25 Th/s och 40 dB för ljudnivån.


Nivån "Super" motsvarar en uteffekt på 650 W vid ca 30Th/s och 45 dB. I detta läge kan du ställa in en maximal omgivningstemperatur över vilken enheten slutar att fungera.



![image](assets/fr/36.webp)




- I "Mining"-läget arbetar enheten med maximal hastighet, utan möjlighet att ställa in en måltemperatur (förutom den inbyggda överhettningsgränsen, förstås). Syftet är att få ut mesta möjliga av Miner:s prestanda. Här närmar sig uteffekten 800 W vid cirka 37,5 Th/s och en ljudnivå på 50-55 dB.



![image](assets/fr/37.webp)


I "Night"-läget körs din Mini 3 med lägsta möjliga hastighet och minimalt med buller. 400 W, 20 Th/s och ca 33 dB.



Även här kan du ställa in en måltemperatur över vilken enheten går in i inaktivt läge och stoppar Miner. Om temperaturen sjunker startar enheten om och återupptar uppvärmningen och Miner. I det här läget är displayens LED-lampor avstängda som standard, men du kan välja att slå på dem vid behov för att lysa upp rummet i mörkret, som en nattlampa (se bilden nedan).



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



Slutligen kan du leka med din Avalons LED-lampor via menyn "Display". Du kan välja att bläddra igenom relevant driftinformation, välja att visa tiden eller till och med en anpassad (pixlad) bild.



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



Precis som med Avalon Nano 3S kan du i menyn "Settings" ändra administratörslösenordet, poolinställningarna, kontrollera filterobstruktion (finns på undersidan av enheten), kontakta support eller visa enhetsloggar.



![image](assets/fr/42.webp)



Återigen kan filtret i botten av enheten rengöras med en dammsugare, ju mer regelbundet desto bättre.



Vi har kommit till slutet av denna handledning, som har lärt oss hur vi ansluter vår Avalon Mini 3 till vårt lokala nätverk, hur vi riktar vår Hashrate mot Mining-pooler och hur vi navigerar genom alternativ och inställningar med Avalon Family-applikationen.



Om du vill veta mer kan du ta en titt på vår handledning om den mindre versionen av Avalon: Nano 3S.



https://planb.network/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6