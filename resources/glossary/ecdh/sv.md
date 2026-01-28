---
term: ECDH
definition: Nyckelutbytesmetod som använder elliptiska kurvor för att generera en delad hemlighet utan att utbyta privata nycklar.
---

Metod för kryptografisk nyckel Exchange som bygger på principerna för Diffie-Hellman-nyckeln Exchange, men som använder elliptiska kurvor för att ge en hög säkerhetsnivå med mindre nyckelstorlekar. Detta protokoll gör det möjligt för två parter att generate en delad hemlighet med hjälp av sina offentliga och privata nyckelpar, utan att någonsin behöva Exchange de privata nycklarna själva. Den delade hemligheten kan sedan användas för att kryptera efterföljande kommunikation. Denna algoritm återfinns ibland i förslag för att förbättra Bitcoin, särskilt BIP47 eller BIP352 för att härleda nya mottagaradresser från en statisk identifierare.