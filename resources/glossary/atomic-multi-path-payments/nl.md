---
term: ATOMAIRE MEERPADENBETALINGEN
---

Verbeterde versie van MPP (*Multi-Path Payments*) waarbij elk betalingsfragment een apart deelgeheim heeft, zodat de transactie atomisch wordt afgewikkeld, d.w.z. volledig of helemaal niet.


MPP's zijn betalingstechnieken op Lightning die het mogelijk maken om een transactie op te splitsen in verschillende kleinere delen en via verschillende routes te routeren. Met andere woorden, elke betalingsfractie neemt een ander knooppuntpad. Dit omzeilt liquiditeitsbeperkingen op een enkel kanaal in de route. In basis-MPP's deelt elke betalingsfractie hetzelfde geheim, en dus dezelfde Hash in HTLC's. Dit kan de transactie traceerbaar maken als de transactie niet kan worden getraceerd. Dit kan de transactie traceerbaar maken als een waarnemer op meerdere routes aanwezig is, omdat hij al deze identieke geheimen aan elkaar kan koppelen. Bovendien is het geheim, omdat het uniek is voor alle delen van de betaling, niet atomair. Dit betekent dat sommige delen van de betaling succesvol kunnen worden uitgevoerd, terwijl andere kunnen mislukken.


In AMP worden voor elke fractie unieke deelgeheimen gebruikt. Als alle fragmenten ontvangen zijn, kan de ontvanger hiermee het oorspronkelijke algemene geheim reconstrueren en de volledige betaling opeisen. Deze methode maakt gedeeltelijke vereffening van de betaling onmogelijk, omdat het bezit van alle deelgeheimen nodig is om de volledige betaling te ontsluiten. Dit zorgt ervoor dat de betaling volledig succesvol of volledig onsuccesvol (d.w.z. atomair) is. AMP verbetert ook de vertrouwelijkheid, omdat er geen zichtbare links meer zijn tussen verschillende routes.


Een voordeel van AMP's is dat ze zelfs werken als alleen de ontvanger en verzender deze methode hebben geïmplementeerd. Intermediaire knooppunten verwerken deze betalingen als conventionele transacties met HTLC's, zich er niet van bewust dat ze fracties van een grotere betaling verwerken.