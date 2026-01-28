---
term: Tweak
definition: Skalärvärde som läggs till en offentlig nyckel för att ändra den samtidigt som dess användbarhet med den ursprungliga privata nyckeln bibehålls.
---

Att "tweaka" en publik nyckel inom kryptografi innebär att den modifieras med hjälp av ett additivt värde som kallas "tweak", så att den fortfarande kan användas med kännedom om både den ursprungliga privata nyckeln och tweaken. Tekniskt sett är en tweak ett skalärt värde som läggs till den ursprungliga publika nyckeln. Om $P$ är den publika nyckeln och $t$ är tweaken, blir den tweakade publika nyckeln :


$$
P' = P + tG
$$


Där $G$ är generatorn för den elliptiska kurva som används. Denna operation producerar en ny publik nyckel som härrör från originalet, samtidigt som den behåller vissa kryptografiska egenskaper som gör att den kan användas. Den här metoden används t.ex. för Taproot-adresser (P2TR) för att göra det möjligt att spendera antingen genom att presentera en Schnorr-signatur på traditionellt sätt eller genom att uppfylla ett av villkoren i en Merkle Tree, även kallad "MAST".