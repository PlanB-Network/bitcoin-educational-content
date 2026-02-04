---
term: Gepruunde node
definition: Full node die oude geverifieerde blokken verwijdert om opslagruimte te besparen.
---

Een pruned node, in het Engels "pruned Node", is een Full node die het snoeien van de Blockchain uitvoert. Dit houdt in het geleidelijk verwijderen van de oudste blokken, nadat deze naar behoren zijn geverifieerd, om alleen de meest recente blokken te behouden. De retentie limiet wordt gespecificeerd in het `Bitcoin.conf` bestand via de `prune=n` parameter, waar `n` de maximale grootte is die de blokken innemen in megabytes (MB). Als `0` achter deze parameter staat, dan is snoeien uitgeschakeld en bewaart het knooppunt de Blockchain in zijn geheel.


pruned knooppunten worden soms beschouwd als andere typen knooppunten dan volledige knooppunten. Het gebruik van een pruned knooppunt kan vooral interessant zijn voor gebruikers met beperkte opslagcapaciteit. Op dit moment moet een Full node bijna 600 GB hebben om Blockchain op te slaan. Een pruned node kan de benodigde opslag beperken tot 550 MB. Hoewel het minder schijfruimte gebruikt, behoudt een pruned knooppunt een verificatie- en validatieniveau dat vergelijkbaar is met dat van een Full node. Daarom bieden pruned knooppunten meer vertrouwen. pruned knooppunten bieden hun gebruikers daarom meer vertrouwen in vergelijking met lichte knooppunten (SPV).