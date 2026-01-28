---
term: Network-adjusted time (NAT)
definition: Schatting van de universele tijd op basis van de mediaan van de klokken van de netwerknodes.
---

Schatting van de universele tijd gebaseerd op de klokken van de netwerkknooppunten. Elk knooppunt berekent zijn NAT door de mediaan te nemen van de tijdverschillen tussen zijn lokale klok (UTC) en die van de knooppunten waarmee het verbonden is, en vervolgens zijn lokale klok op te tellen bij de mediaan van deze verschillen, tot een maximum van 70 minuten. De voor het netwerk gecorrigeerde tijd is dus een mediaan van de knooppunttijden die door elk knooppunt lokaal zijn berekend. Dit referentiekader wordt vervolgens gebruikt om de geldigheid van de bloktijdstempels te controleren. Een blok wordt alleen geaccepteerd door een knooppunt als de Timestamp tussen de MTP (mediane tijd van de laatste 11 gemijnde blokken) en de NAT plus 2 uur ligt:


```text
MTP < Valid Timestamp < (NAT + 2h)
```