---
term: Transaktionsvittne
definition: SegWit-komponent som innehåller signaturer och offentliga nycklar som krävs för att låsa upp bitcoins i en transaktion.
---

Avser en komponent i Bitcoin-transaktioner som flyttades med SegWit Soft Fork till Address frågan om transaktionens formbarhet. Vittnet innehåller de signaturer och publika nycklar som krävs för att låsa upp de bitcoins som spenderats i en transaktion. I Legacy-transaktioner representerade vittnet summan av `scriptSig` från alla ingångar. I SegWit-transaktioner representerar vittnet summan av `scriptWitness` för varje inmatning, och denna del av transaktionen flyttas nu till en separat Merkle Tree inom blocket.


Före SegWit kunde signaturer ändras något utan att ogiltigförklaras innan en transaktion bekräftades, vilket ändrade transaktionsidentifieraren. Detta gjorde det svårt att bygga olika protokoll, eftersom en obekräftad transaktion kunde se sin identifierare ändras. Genom att separera vittnena gör SegWit att transaktioner inte kan göras om, eftersom en ändring av signaturerna inte längre påverkar transaktionsidentifieraren (txid), utan endast vittnesidentifieraren (WTXID). Förutom att lösa problemet med manipulerbarhet gör denna separation det möjligt att öka kapaciteten för varje block.


