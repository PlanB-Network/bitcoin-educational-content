---
term: CoinJoin
---

CoinJoin är en teknik som används för att bryta spårbarheten för bitcoins. Den bygger på en samarbetstransaktion med en specifik struktur med samma namn: CoinJoin-transaktionen. CoinJoin-transaktioner bidrar till att förbättra integritetsskyddet för Bitcoin-användare genom att göra det svårare för externa observatörer att analysera transaktioner. Denna struktur gör det möjligt att blanda flera mynt i en enda transaktion, vilket gör det svårt att fastställa länkarna mellan in- och utdataadresser.


CoinJoin fungerar generellt på följande sätt: olika användare som vill blanda sätter in ett belopp som input i en transaktion. Dessa inputs kommer att komma ut som olika outputs av samma belopp. I slutet av transaktionen är det omöjligt att avgöra vilken utgång som tillhör vilken användare. Det finns tekniskt sett ingen länk mellan inmatningarna och utmatningarna i CoinJoin-transaktionen. Länken mellan varje användare och varje UTXO är bruten, på samma sätt som varje mynts historia är det.


![](../../dictionnaire/assets/4.webp)


För att möjliggöra CoinJoin utan att någon användare förlorar kontrollen över sina medel när som helst, konstrueras transaktionen först av en koordinator och överförs sedan till varje användare. Var och en signerar sedan transaktionen på sin sida efter att ha verifierat att den passar dem, och sedan läggs alla signaturer till transaktionen. Om en användare eller koordinatorn försöker stjäla andras pengar genom att ändra utdata från CoinJoin-transaktionen, blir signaturerna ogiltiga och transaktionen avvisas av noderna. När registreringen av deltagarnas utdata görs med hjälp av Chaums blinda signaturer för att undvika kopplingen till indata kallas detta för "Chaumian CoinJoin".


Denna mekanism ökar transaktionernas konfidentialitet utan att kräva ändringar i Bitcoin-protokollet. Specifika implementeringar av CoinJoin, såsom Whirlpool, JoinMarket eller Wabisabi, erbjuder lösningar för att underlätta samordningsprocessen mellan deltagarna och förbättra effektiviteten i CoinJoin-transaktionen. Här är ett exempel på en CoinJoin-transaktion:


```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```


Det är svårt att med säkerhet avgöra vem som först introducerade idén om CoinJoin på Bitcoin, och vem som hade idén att använda David Chaums blinda signaturer i detta sammanhang. Man tror ofta att Gregory Maxwell var den första som diskuterade det i [ett meddelande på BitcoinTalk 2013](https://bitcointalk.org/index.php?topic=279249.0):

Använda Chaum blinda signaturer: Användare ansluter och tillhandahåller inmatningar (och byter adresser) samt en kryptografiskt blinded-version av Address som de vill skicka sina privata mynt till; servern signerar tokens och returnerar dem. Användarna återansluter anonymt, avmaskerar sina utdataadresser och skickar tillbaka dem till servern. Servern kan se att alla utdata har signerats av den och att alla utdata följaktligen kommer från giltiga deltagare. Senare återansluter människor och signerar.

Maxwell, G. (2013, 22 augusti). *CoinJoin: Bitcoin integritet för den verkliga världen*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0


Det finns dock tidigare omnämnanden, både för Chaum-signaturer i samband med blandning och för coinjoins. [I juni 2011 presenterar Duncan Townsend på BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) en mixer som använder Chaum-signaturer på ett sätt som liknar moderna Chaumian coinjoins. I samma tråd finns det [ett meddelande från hashcoin som svar till Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) för att förbättra hans mixer. Detta meddelande presenterar vad som närmast liknar coinjoins. Ett liknande system nämns också i [ett meddelande från Alex Mizrahi 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), när han var rådgivare till skaparna av Tenebrix. Själva termen "CoinJoin" uppfanns inte av Greg Maxwell, utan kom från en idé av Peter Todd.


> ► *Termen "CoinJoin" har ingen fransk översättning. Vissa bitcoiners använder också termerna "mix", "mixing" eller "mixage" för att hänvisa till CoinJoin-transaktionen. Mixning är snarare den process som används i hjärtat av CoinJoin. Det är också viktigt att inte förväxla mixning genom coinjoins med mixning genom en central aktör som tar bitcoins i besittning under processen. Detta har inget att göra med CoinJoin där användaren inte förlorar kontrollen över sina bitcoins under processen.*