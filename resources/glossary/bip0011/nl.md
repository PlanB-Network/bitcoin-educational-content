---
term: BIP0011
definition: Standaard voor de introductie van M-of-N multisig-transacties op Bitcoin, tegenwoordig bekend als bare-multisig of P2MS.
---

BIP geïntroduceerd door Gavin Andresen in maart 2012 die een standaardmethode voorstelt voor het maken van transacties met meerdere handtekeningen op Bitcoin. Dit voorstel is bedoeld om de veiligheid van bitcoins te verbeteren door meerdere handtekeningen te vereisen om een transactie te valideren. BIP11 introduceert een nieuw type script, genaamd "M-of-N Multisig," waarbij `M` staat voor het minimum aantal vereiste handtekeningen uit `N` potentiële publieke sleutels. Deze standaard gebruikt de `OP_CHECKMULTISIG` opcode, die al bestond in Bitcoin, maar die voorheen niet voldeed aan de standaardisatieregels van de knooppunten. Hoewel dit type script niet meer vaak gebruikt wordt voor echte Multisig wallets, ten gunste van P2SH of P2WSH, blijft het gebruik ervan mogelijk. Het wordt met name gebruikt in meta-protocollen zoals Stamps. Knooppunten kunnen er echter voor kiezen om deze P2MS transacties niet door te geven met de parameter `permitbaremultisig=0`.


> ► *Nu staat deze standaard bekend als "bare-Multisig" of "P2MS".*