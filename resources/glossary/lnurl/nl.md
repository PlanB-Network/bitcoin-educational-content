---
term: LNURL
definition: Protocol dat Lightning-interacties vereenvoudigt via bech32-gecodeerde URL's.
---

Communicatieprotocol dat een reeks functies specificeert die zijn ontworpen om interacties tussen Lightning-knooppunten en klanten en toepassingen van derden te vereenvoudigen. Dit protocol is gebaseerd op HTTP en maakt het mogelijk om links aan te maken voor verschillende operaties, zoals een betalingsverzoek, een opnameverzoek of andere functionaliteiten die de gebruikerservaring verbeteren. Elke LNURL is een URL gecodeerd in bech32 met het voorvoegsel `lnurl`, die bij het scannen een reeks automatische acties op de Lightning Wallet activeert.


Met LNURL-Withdraw (LUD-03) kun je bijvoorbeeld geld opnemen van een dienst door een QR-code te scannen, zonder dat je handmatig generate en Invoice hoeft te gebruiken. Of met LNURL-auth (LUD-04) kun je verbinding maken met online diensten met behulp van een privésleutel op je Lightning Wallet in plaats van een wachtwoord.