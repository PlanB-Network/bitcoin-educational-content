---
term: Offer
definition: Återanvändbara statiska QR-koder för att ta emot flera betalningar på Lightning (BOLT12).
---

I BOLT12 är *offers* statiska QR-koder för att göra flera betalningar på Lightning Network. Till skillnad från konventionella fakturor kan *offers* återanvändas. De kan användas för att generate flera Invoice-förfrågningar. När en användare skannar en QR-kod som innehåller ett *erbjudande* skickas ett meddelande med en begäran om en ny Invoice till den associerade Lightning-noden. Noden svarar med en Invoice som betalaren kan använda. *erbjudandena* ger alltså en unik identifierare för att ta emot flera betalningar från olika användare på Lightning.