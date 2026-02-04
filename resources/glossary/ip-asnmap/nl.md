---
term: IP_ASN.MAP
definition: Bitcoin Core-bestand dat IP-adressen koppelt aan ASN's om netwerkverbindingen te diversifiëren.
---

Bestand gebruikt in Bitcoin core om de ASMAP op te slaan, die de "bucketing" (d.w.z. groepering) van IP adressen verbetert door te vertrouwen op Autonome Systeem Nummers (ASN). In plaats van het groeperen van uitgaande verbindingen door IP netwerk prefixen (/16), maakt dit bestand het mogelijk om verbindingen te diversifiëren door een IP adresseringsmap te maken naar ASN's, die unieke identificaties zijn voor elk netwerk op het Internet. Het idee is om de veiligheid en topologie van het Bitcoin netwerk te verbeteren door verbindingen te diversifiëren om bescherming te bieden tegen bepaalde aanvallen (met name de Erebus aanval).