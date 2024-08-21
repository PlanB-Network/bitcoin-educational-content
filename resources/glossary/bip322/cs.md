---
term: BIP322
---

Navrhuje nový standard, který má nahradit BIP137 pro podepisování zpráv pomocí soukromých klíčů Bitcoinu a přidružených adres, aby se dokázalo vlastnictví adresy. Tyto podpisy jsou užitečné pro různé aplikace, jako je důkaz finančních prostředků, auditování a další použití vyžadující ověření adresy prostřednictvím jejího soukromého klíče. Ve srovnání s BIP137 rozšiřuje BIP322 standard podepisování zpráv za hranice tradičních adres pomocí přístupu založeného na skriptech. Umožňuje softwaru peněženky podepsat zprávu pro jakýkoli skript, který by mohli odemknout k vynaložení bitcoinů. K tomu používá metodu podepisování textu vytvořením podpisu pro virtuální Bitcoinovou transakci. Pro tradiční adresy P2PKH zůstává BIP322 kompatibilní s tradičním formátem podpisu.