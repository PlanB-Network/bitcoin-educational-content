---
term: BIP72

---
Doplňuje BIP70 a BIP71 definováním rozšíření Bitcoin URI (BIP21) o další parametr `r`. Tento parametr umožňuje zahrnout odkaz na zabezpečený požadavek na platbu podepsaný certifikátem SSL obchodníka. Když klient klikne na tento rozšířený URI, jeho peněženka kontaktuje server obchodníka a požádá o platební údaje. Tyto údaje se automaticky vyplní v transakčním rozhraní peněženky a klient může být informován, že platí vlastníkovi domény odpovídající podpisovému certifikátu (například "pandul.fr"). Vzhledem k tomu, že toto vylepšení je spojeno s BIP70, nebylo nikdy široce přijato.