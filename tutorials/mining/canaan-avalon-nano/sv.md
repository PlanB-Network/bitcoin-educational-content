---
name: Canaan Avalon Nano 3S
description: Konfigurera din ASIC Avalon för solomining eller Miner pooling
---

![cover](assets/cover.webp)



I den här handledningen tittar vi på hur du ställer in Canaan Avalon Nano 3S, för enkel hemanvändning av Miner.



Fram till nu har ASIC-maskiner (*Application Specific Integrated Circuit*) som är särskilt utformade för att utföra en viss uppgift - i det här fallet Hash-beräkning (SHA-256) för Miner av Bitcoin - varit särskilt olämpliga för hushållsbruk. Det störande bullret, värmen som alstras och behovet av att anpassa elinstallationen för att klara av den enorma kraften i dessa enheter hindrade de flesta av oss från att delta.



Idag har Canaan, en av de ledande tillverkarna av ASIC-maskiner, bestämt sig för att ta sig an marknaden för privatpersoner som vill ha Miner hemma, genom att erbjuda ett sortiment av produkter som är relativt tysta och mycket enkla att installera (plug & play).



Dessa enheter marknadsförs antingen som en extra värmare, som i fallet med **Avalon Nano 3S (140W)**, eller som en miniradiator med en effekt på **800W**, som i fallet med **Avalon Mini 3**.



https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Observera att prisskillnaden mot traditionella värmare med motsvarande effekt i de allra flesta fall inte gör det möjligt för dig att göra en ekonomisk vinst. De satoshis som genereras av Mining:s verksamhet kommer aldrig att kompensera för denna prisskillnad, såvida du inte har tillgång till gratis (överskott) eller mycket billig el.



Enligt min mening bör dessa enheter ses mer som ett enkelt sätt att Miner hemma för dem som vill göra det av personliga skäl: *få icke-KYC Satss / spela "lotteriet" genom att solominera / delta i Hashrate decentralisering etc..*. samtidigt som man drar nytta ** som en bonus** av den värme som genereras för att värma sitt rum på vintern. Men inte som ett sätt att spara pengar i de flesta fall åtminstone (västländer).



## Unboxing och funktioner



Låt oss först se vad som finns i Avalon Nano 3S-lådan.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



När du har öppnat lådan hittar du en kartonghylsa som innehåller en WIFI-mottagare som, som vi kommer att se senare, måste anslutas till enhetens USB-port för att den ska kunna ansluta till ditt lokala nätverk. Dessutom ingår bruksanvisningen och ett metallstift för att återställa enheten till fabriksinställningarna om det behövs.



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



När allt väl är ur lådan är det här vad som finns till hands: själva maskinen naturligtvis, användarhandboken, WIFI-mottagaren, den tidigare nämnda metallspetsen och enhetens ström Supply. Det medföljande kreditkortet är inte värt att nämna enligt vår mening.



![image](assets/fr/05.webp)



Nedan följer en tabell som sammanfattar de allmänna tekniska specifikationerna för Nano 3S :



| Caractéristique                                      | Valeur                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Taux de hachage                                      | 6 Th/s +- 5%                                            |
| Consommation d'énergie                               | 140 W                                                   |
| Bruit                                                | 30 - 40 dB                                              |
| Plage de température de sortie d'air                 | 60-70°C (sous température ambiante 25°C)                |
| Exigences de température ambiante pour l'utilisation | de -5 à 30°C                                            |
| Plage d'entrée de l'appareil                         | 28V 5A continu                                          |
| Plage d'entrée de l'adaptateur                       | 110-240V AC 50/60Hz                                     |
| Taille de la machine                                 | Longueur: 205 mm /  Largeur: 115 mm / Hauteur:  58.5 mm |
| Poids de la machine                                  | 0.86 kg                                                 |

## Starta och ansluta till det lokala nätverket



När du har packat upp din Avalon Nano 3 S, placera den om möjligt i ett relativt öppet utrymme så att värmen kan cirkulera. Börja sedan med att sätta in den lilla WIFI-mottagarmodulen enligt bilden nedan:



![image](assets/fr/06.webp)


Anslut sedan strömmen Supply:s USB-C-kontakt till enhetens USB-C-port för att driva den.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



Enheten startar upp och Avalon Nano-logotypen visas på skärmen, följt av en "mobiltelefon"-logotyp med orden "Please Configure the Network With Avalon Family App".



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



För att göra detta, gå till din mobilapplikationsbutik, sök efter och ladda ner **Avalon Family**-applikationen.



![image](assets/fr/11.webp)


När du har installerat programmet öppnar du det genom att klicka på "Skip" i det övre högra hörnet, sedan på knappen "Add" och slutligen på "Search". Se till att du har Bluetooth aktiverat på din smartphone, så att detektering av enheten går smidigt.



![image](assets/fr/12.webp)


När enheten har upptäckts av programmet klickar du på den och väljer "Connect". Du kommer då till en skärm där du kan ange dina WIFI-anslutningsuppgifter.


![image](assets/fr/13.webp)


När enheten är ansluten till ditt lokala nätverk ser skärmen ut så här:



![image](assets/fr/14.webp)



Den visar en "fiktiv" Hashrate, eftersom ingen pool ännu har konfigurerats, och enhetens tid, datum, ström och IP Address - mycket användbart om du vill komma åt enhetens Interface via en PC och webbläsare (mer om detta senare).



![image](assets/fr/15.webp)




## Anslutning till en Mining pool



**Den här delen är gemensam för Nano 3s och Mini 3, eftersom processerna är helt identiska**.



Oavsett om vi vill "solominera" eller Miner "poola" kommer vi att behöva ansluta till en Mining pool. Faktum är att vår enhet inte är något annat än en Hash-tillverkare utan någon medvetenhet om Bitcoin-nätverket. Genom att ansluta den till en pool får den tillgång till Bitcoin-nätverket och kan ta emot blockmallar att arbeta med.



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



I Avalon-familjens applikation klickar du på ikonen som motsvarar Avalon Nano 3S.


visas sedan 3 menyer: "Arbetsläge", "Ljusreglering" och "Inställningar". Klicka först på "Arbetsläge". Du kommer då att erbjudas 3 strömlägen för din maskin.



**Low**: ger dig cirka 3 Th/s Hashrate för 70 W strömförbrukning


**Medium**: ger dig ca 4,5 Th/s Hashrate för 100 W strömförbrukning


**Hög**: ger dig cirka 6 Th/s Hashrate vid maximal förbrukning på 140 W



![image](assets/fr/31.webp)


Låt oss ta ett steg tillbaka och utforska menyn "Light Control". Detta är en rent kosmetisk funktion. Det finns en mängd olika alternativ för att variera färg, intensitet, värme, stänga av enhetens LED-lampor på natten etc... Det är lätt att ta reda på själv.



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



Den sista menyn som är tillgänglig för oss är menyn "Inställningar" som vi redan har sett för att ansluta till våra Mining-pooler. Här kan du hantera dina pooler, ändra enhetens administratörslösenord och observera olika mätvärden, t.ex. garantins utgångsdatum, filtrets renhet eller hur du kontaktar support i händelse av fel.



![image](assets/fr/35.webp)


För underhåll och för att hålla filtret så rent som möjligt rekommenderar vi att du använder en dammsugare och regelbundet dammsuger luftintagen och luftutsläppen för att förhindra igensättning.



Vi har kommit till slutet av den här handledningen, som har lärt oss hur vi ansluter vår Avalon Nano 3 S till vårt lokala nätverk, hur vi pekar vår Hashrate mot Mining-pooler och hur vi navigerar genom alternativ och inställningar med Avalon Family-applikationen.



För att få reda på mer, ta en titt på vår handledning om den överlägsna versionen av Avalon: Mini 3.



https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7