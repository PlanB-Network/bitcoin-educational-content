---
term: Covenant
definition: Mechanisme dat voorwaarden oplegt aan de manier waarop een bitcoin in toekomstige transacties kan worden uitgegeven.
---

Een mechanisme dat het mogelijk maakt om specifieke voorwaarden op te leggen over hoe een bepaald stuk geld kan worden uitgegeven, ook in toekomstige transacties. Naast de voorwaarden die gewoonlijk door de scripttaal op een UTXO worden toegestaan, dwingt het convenant aanvullende beperkingen af op hoe deze Bitcoin in volgende transacties kan worden uitgegeven. Technisch gezien ontstaat een convenant wanneer de `scriptPubKey` van een UTXO beperkingen definieert op de `scriptPubKey` van de uitvoer van een transactie die deze UTXO uitgeeft. Door de reikwijdte van het script uit te breiden, zouden convenanten talrijke ontwikkelingen op Bitcoin mogelijk maken, zoals de bilaterale verankering van drivechains, de implementatie van vaults, of de verbetering van overlay systemen zoals Lightning. Convenantvoorstellen worden gedifferentieerd op basis van drie criteria:


- Hun bereik;
- Hun uitvoering;
- Hun recursiviteit.


Er zijn veel voorstellen die het gebruik van convenanten op Bitcoin mogelijk maken. De verst gevorderde in het implementatieproces zijn: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO) en `OP_VAULT`. Andere voorstellen zijn: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, enz.


Om het concept van een convenant beter te begrijpen, kun je de volgende analogie bekijken: stel je een kluis voor met 500€ in kleine biljetten. Als het je lukt om deze kluis te openen met de juiste sleutel, dan ben je vrij om dit geld te gebruiken zoals je wilt. Dit is de normale situatie met Bitcoin. Stel je nu voor dat dezelfde kluis geen 500€ aan bankbiljetten bevat, maar maaltijdcheques van gelijke waarde. Als je erin slaagt deze kluis te openen, kun je dit bedrag gebruiken. Je vrijheid om geld uit te geven is echter beperkt, omdat je deze bonnen alleen kunt gebruiken om in bepaalde restaurants te betalen. Er is dus een eerste voorwaarde om dit geld te kunnen uitgeven, namelijk de kluis te openen met de juiste sleutel. Maar er is ook een extra voorwaarde met betrekking tot het toekomstige gebruik van dit bedrag: het moet uitsluitend worden uitgegeven in partnerrestaurants, en niet vrij. Dit systeem van beperkingen op toekomstige transacties wordt een convenant genoemd.


