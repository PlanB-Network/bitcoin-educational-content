---
term: Hashcash
definition: Proof-of-work-system designat av Adam Back 1997, en föregångare till Bitcoin-brytningsmekanismen.
---

HashCash är ett Proof-of-Work-system som designades av Adam Back 1997 för att bekämpa spam och DoS-attacker. Det bygger på principen att en avsändare måste utföra en beräkningsuppgift (specifikt att hitta en partiell kollision på en kryptografisk Hash-funktion) för att bevisa sitt arbete. Denna uppgift är kostsam i form av tid och energi för avsändaren, men det är snabbt och enkelt för mottagaren att verifiera resultatet. Detta protokoll har visat sig vara särskilt lämpligt för att bekämpa skräppost i e-postkommunikation, eftersom det är minimalt betungande för legitima användare samtidigt som det utgör ett betydande hinder för skräppostare. Att skicka ett enda e-postmeddelande kräver visserligen några sekunders beräkning, men att upprepa denna operation miljontals gånger blir extremt kostsamt i termer av energi och tid, vilket ofta omintetgör det ekonomiska intresset för spamkampanjer, oavsett om de är i marknadsföringssyfte eller skadliga. Dessutom gör den det möjligt att bevara avsändarens anonymitet.


HashCash anammades snabbt av cypherpunks som ville utveckla ett anonymt elektroniskt valutasystem utan mellanhänder. Adam Backs innovation introducerade faktiskt begreppet knapphet i den digitala världen för första gången. Konceptet Proof of Work återfinns sedan i flera elektroniska valutasystem som föregick Bitcoin, bland annat:


- b-money av Wei Dai publicerad 1998;
- R-POW av Hal Finney utgiven 2004;
- BitGold av Nick Szabo publicerad 2005.


HashCash-principen återfinns också i Bitcoin-protokollet, där den används som en skyddsmekanism mot Sybil-attacker.