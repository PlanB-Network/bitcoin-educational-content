---
term: BIP137

---
Navrhuje standardizovaný formát pro podepisování zpráv pomocí soukromých klíčů Bitcoin a přidružených adres, aby bylo možné prokázat vlastnictví adresy. Cílem tohoto BIP je vyřešit nejednoznačnost související s různými typy bitcoinových adres (P2PKH, P2SH, P2WPKH...) při podepisování zprávy. Zavádí metodu explicitního rozlišování těchto formátů adres prostřednictvím podpisů. Tyto podpisy jsou užitečné pro různé aplikace, jako je důkaz prostředků, audit a další použití vyžadující ověření adresy prostřednictvím jejího soukromého klíče. BIP322 od té doby zavedl nový formát podpisu, který umožňuje rozšíření tohoto standardu a jeho zobecnění pro jakýkoli typ skriptu.