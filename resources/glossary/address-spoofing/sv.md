---
term: Address spoofing
definition: En attack där en illvillig aktör skapar en adress som starkt liknar offerets adress för att lura dem och omdirigera deras betalningar.
---

Attack där en illasinnad aktör skapar en Address (eller annan betalningsidentifierare) som är mycket lik offrets. Syftet är att lura användaren att kopiera denna felaktiga Address under en transaktion, vilket resulterar i att bitcoins skickas till angriparen istället för den avsedda destinationen.



Angriparen utnyttjar användarens brådska för att kopiera fel Address om han genomför transaktionen utan att kontrollera dess riktighet. För att genomföra denna attack gör angriparen i allmänhet betalningar med små summor till offrets Wallet för att integrera den falska Address i sin transaktionshistorik. Denna attack tenderar att användas med altcoins, där det är vanligt att återanvända samma mottagningsadresser, till skillnad från Bitcoin, där användningen av tomma adresser för varje transaktion är en mer utbredd praxis. Bitcoin-användare är dock inte immuna mot denna attack.



En annan metod för att presentera en felaktig adress för offret är användningen av bedräglig programvara för plånbokshantering som imiterar legitim programvara, eller ändring av adressen när en maskin har komprometterats, mellan det ögonblick då den kopieras och det då transaktionen konstrueras. Detta kallas ibland '"*address swapping*"'.



För att skydda dig mot dessa olika angreppsmetoder är det viktigt att kontrollera flera tecken i Address, särskilt dess kontrollsumma (i slutet), på skärmen på signeringsenheten innan du signerar transaktionen.



Denna attack kallas ibland även '"*address poisoning*"'.