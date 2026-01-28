---
term: Multi-path payments (MPP)
definition: Lightning-techniek die een betaling opsplitst in verschillende delen die via verschillende routes worden gerouteerd.
---

Een algemene term voor alle betalingstechnieken op Lightning die het mogelijk maken om een transactie op te splitsen in verschillende kleinere delen en via verschillende routes te routeren. Met andere woorden, elke betalingsfractie neemt een ander knooppuntpad. Dit maakt het mogelijk om liquiditeitsbeperkingen op een enkel kanaal in de route te omzeilen.


Betalingen via meerdere paden bieden ook kleine voordelen op het gebied van vertrouwelijkheid, omdat het moeilijker wordt voor een waarnemer om elk betalingsfragment te koppelen aan de hele transactie. In de basisversie delen alle fragmenten echter hetzelfde geheim voor HTLC's, waardoor de transactie traceerbaar kan zijn als een waarnemer op meerdere routes aanwezig is. Bovendien is het geheim, omdat het uniek is voor alle fragmenten van de betaling, niet atomair. Dit betekent dat sommige delen van de betaling succesvol kunnen worden uitgevoerd, terwijl andere kunnen mislukken. Deze nadelen worden verholpen met "Atomic Multi-Path Payment".