---
term: CHAUMIAN CoinJoin
---

Ett CoinJoin-protokoll som använder David Chaums blinda signaturer och Tor för kommunikation mellan deltagare och koordinatorns server. Målet med ett Chaumian CoinJoin är att säkerställa att deltagarna vet att koordinatorn inte kan stjäla bitcoins eller länka samman in- och utgångar.


För att uppnå detta skickar användarna sin input och en kryptografiskt blinded-mottagande Address till koordinatorn. Denna Address, en gång unblinded, är avsedd att ta emot bitcoins som en utgång från CoinJoin. Samordnaren signerar dessa tokens och returnerar dem till användarna. Användarna återansluter sedan anonymt till samordnarens server med en ny Tor-identitet och avslöjar sina utdataadresser i klartext för transaktionskonstruktionen. Koordinatorn kan verifiera att alla dessa mottagningsadresser kommer från legitima användare, eftersom han tidigare har signerat deras blinded-version med sin privata nyckel. Han kan dock inte associera en specifik utgående Address med en given ingående användare. Därför finns det ingen länk mellan inmatningarna och utmatningarna, inte ens ur koordinatorns perspektiv. När transaktionen har skapats av koordinatorn skickar han tillbaka den till deltagarna som signerar den för att låsa upp sina inmatningar, efter att ha verifierat att deras utmatningar verkligen ingår i transaktionen. Deltagarna skickar signaturen till samordnaren. När alla signaturer har samlats in kan koordinatorn sända ut CoinJoin-transaktionen i Bitcoin-nätverket.


![](../../dictionnaire/assets/38.webp)


Denna metod säkerställer att koordinatorn varken kan äventyra deltagarnas anonymitet eller stjäla bitcoins under hela CoinJoin-processen.


Det är svårt att med säkerhet avgöra vem som först introducerade idén om CoinJoin på Bitcoin, och vem som hade idén att använda David Chaums blinda signaturer i detta sammanhang. Man tror ofta att Gregory Maxwell var den första som diskuterade det i [ett meddelande på BitcoinTalk 2013](https://bitcointalk.org/index.php?topic=279249.0):


> *"Genom att använda Chaum blinda signaturer: Användare ansluter och tillhandahåller inmatningar (och byter adresser) samt en kryptografiskt blinded-version av Address som de vill skicka sina privata mynt till; servern signerar tokens och returnerar dem. Användarna återansluter anonymt, avmaskerar sina utdataadresser och returnerar dem till servern. Servern kan se att alla utdata har signerats av honom och att alla utdata därför kommer från giltiga deltagare. Senare återansluter människor och signerar."*

Maxwell, G. (2013, 22 augusti). *CoinJoin: Bitcoin integritet för den verkliga världen*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

Det finns dock andra tidigare omnämnanden, både för Chaums signaturer i samband med blandning och för coinjoins. [I juni 2011 presenterade Duncan Townsend på BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) en mixer som använder Chaums signaturer på ett sätt som liknar moderna chaumianska coinjoins. I samma tråd finns det [ett meddelande från hashcoin som svar till Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) för att förbättra hans mixer. Detta meddelande presenterar exakt vad som närmast liknar coinjoins. Ett liknande system nämns också i [ett meddelande från Alex Mizrahi 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), när han var rådgivare till skaparna av Tenebrix. Själva termen "CoinJoin" skulle inte ha uppfunnits av Greg Maxwell, men den skulle komma från en idé av Peter Todd.