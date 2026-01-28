---
term: Transaktion (tx)
definition: Operation registrerad på blockchain som överför äganderätten till bitcoins från en eller flera inputs till en eller flera outputs.
---

I samband med Bitcoin är en transaktion (förkortad som "TX") en operation som registreras på Blockchain som överför Ownership av bitcoins från en eller flera ingångar till en eller flera utgångar. Varje transaktion förbrukar outnyttjade transaktionsutgångar (UTXO) som ingångar, vilka är utgångar från tidigare transaktioner, och skapar nya UTXO som utgångar, vilka kan användas som ingångar i framtida transaktioner.


Varje input innehåller en referens till en befintlig output tillsammans med ett signaturskript (`scriptSig`) som uppfyller de utgiftsvillkor (`scriptPubKey`) som fastställts av den output som den refererar till. Det är detta som gör att bitcoins kan låsas upp. Utgångarna definierar nya utgiftsvillkor (`scriptPubKey`) för de överförda bitcoins, ofta i form av en publik nyckel eller en Address som bitcoins nu är associerade till.