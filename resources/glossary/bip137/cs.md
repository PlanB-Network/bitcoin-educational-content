---
term: BIP137
---

Navrhuje standardizovaný formát pro podepisování zpráv s privátními klíči Bitcoinu a jejich přidruženými adresami, aby se dokázalo vlastnictví adresy. Tento BIP si klade za cíl vyřešit nejednoznačnost související s různými typy Bitcoinových adres (P2PKH, P2SH, P2WPKH...) při podepisování zprávy. Zavádí metodu pro explicitní rozlišení těchto formátů adres prostřednictvím podpisů. Tyto podpisy jsou užitečné pro různé aplikace, jako je důkaz finančních prostředků, audit a další použití vyžadující ověření adresy prostřednictvím jejího privátního klíče. BIP322 od té doby představil nový formát podpisu, který umožňuje rozšíření tohoto standardu a jeho zobecnění pro jakýkoli typ skriptu.