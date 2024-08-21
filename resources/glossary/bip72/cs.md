---
term: BIP72
---

Doplnění BIP70 a BIP71 definováním rozšíření Bitcoin URI (BIP21) o další parametr `r`. Tento parametr umožňuje zahrnout odkaz na bezpečnou platební žádost podepsanou SSL certifikátem obchodníka. Když klient klikne na toto rozšířené URI, jeho peněženka kontaktuje server obchodníka s žádostí o platební údaje. Tyto údaje jsou automaticky vyplněny v rozhraní transakce peněženky a klient může být informován, že platí majiteli domény odpovídající podepisujícímu certifikátu (například "pandul.fr"). Jelikož je toto vylepšení svázáno s BIP70, nikdy nebylo široce přijato.