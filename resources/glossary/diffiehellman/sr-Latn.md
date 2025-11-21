---
term: DIFFIE-HELLMAN
---

Kriptografski metod koji omogućava dvema stranama da generate podele tajnu preko nesigurnog komunikacionog kanala. Ova tajna se zatim može koristiti za šifrovanje komunikacije između dve strane. Diffie-Hellman koristi modularnu aritmetiku tako da, čak i ako napadač može da posmatra razmene, ne može da zaključi deljenu tajnu bez rešavanja teškog matematičkog problema: diskretnog logaritma. U Bitcoin, varijanta DH nazvana ECDH koja koristi eliptičnu krivu se ponekad koristi, posebno za statičke Address protokole kao što su Silent Payments ili BIP47.