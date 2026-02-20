---
term: Svårighetsmål
definition: 256-bitars numeriskt värde som bestämmer acceptansgränsen för hashning av blockhuvuden.
---

Svårighetsfaktorn, även känd som svårighetsmålet, är en parameter som används i konsensusmekanismen av Proof of Work (Proof of Work, PoW) på Bitcoin. Målet representerar ett numeriskt värde som avgör hur svårt det är för miners att lösa ett specifikt kryptografiskt problem, kallat Proof of Work, när de skapar ett nytt block på Blockchain.


Svårighetsmålet är ett justerbart 256-bitars (64 byte) tal som bestämmer en acceptansgräns för hashning av blockheaders. Med andra ord, för att ett block ska vara giltigt måste Hash i dess header med `SHA256d` (dubbel `SHA256`) vara numeriskt lägre eller lika med svårighetsmålet. Proof of Work består av att modifiera fältet `Nonce` i blockhuvudet eller Coinbase Transaction tills den resulterande Hash är lägre än målvärdet.


Detta mål justeras varje 2016 block (ungefär varannan vecka), under en händelse som kallas "justering" Svårighetsfaktorn räknas om baserat på den tid det tog att bryta de föregående 2016 blocken. Om den totala tiden är mindre än två veckor ökar svårighetsgraden genom att målet justeras nedåt. Om den totala tiden är mer än två veckor minskar svårighetsgraden genom att justera målet uppåt. Målet är att upprätthålla en genomsnittlig Mining-tid på 10 minuter per block. Denna tid mellan varje block hjälper till att förhindra uppdelningar av Bitcoin-nätverket, vilket resulterar i slöseri med datorkraft. Svårighetsmålet finns i varje blockhuvud, inom fältet `nBits`. Eftersom detta fält är reducerat till 32 bitar och målet faktiskt är 256 bitar, komprimeras målet till ett mindre exakt vetenskapligt format.





> ► *Svårighetsmålet kallas ibland också för "svårighetsfaktorn"* I förlängningen kan den refereras till med sin kodning i blockrubrikerna med termen "nBits"