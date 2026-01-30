---
term: Wallet import format (WIF)
definition: Base58Check-kodningsmetod för en privat Bitcoin-nyckel för att underlätta import eller export mellan plånböcker.
---

En metod för att koda en privat Bitcoin-nyckel på ett sätt som gör att den lättare kan importeras eller exporteras mellan olika plånböcker. WIF är baserad på `Base58Check`-kodning, som innehåller information om versionen, komprimeringen av motsvarande offentliga nyckel och en kontrollsumma för feldetektering vid skrivning. En privat WIF-nyckel börjar med tecknen `5` för okomprimerade nycklar, eller `K` och `L` för komprimerade nycklar, och innehåller alla de tecken som krävs för att rekonstruera den ursprungliga privata nyckeln. WIF-formatet ger ett standardiserat sätt att överföra en privat nyckel mellan olika Wallet-program.