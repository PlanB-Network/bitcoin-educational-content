---
term: BIP0072
definition: Utökning av Bitcoin-URIer med en parameter för säkra betalningsbegäranden enligt BIP70. Blev aldrig allmänt antaget.
---

Kompletterar BIP70 och BIP71 genom att definiera utvidgningen av Bitcoin URI (BIP21) med en ytterligare parameter `r`. Denna parameter gör det möjligt att inkludera en länk till en säker betalningsbegäran som signerats av handlarens SSL-certifikat. När en kund klickar på denna utökade URI kontaktar deras Wallet handlarens server för att begära betalningsinformation. Dessa uppgifter fylls automatiskt i Wallet:s transaktion Interface, och kunden kan informeras om att de betalar domänägaren som motsvarar signeringscertifikatet (till exempel "pandul.fr"). Eftersom den här förbättringen ingår i BIP70 har den aldrig fått någon större spridning.