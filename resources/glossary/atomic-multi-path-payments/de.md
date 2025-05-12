---
term: ATOMARE MEHRWEGZAHLUNGEN
---

Verbesserte Version von MPP (*Multi-Path Payments*), bei der jedes Zahlungsfragment ein eigenes Teilgeheimnis hat, um sicherzustellen, dass die Transaktion atomar abgewickelt wird, d. h. vollständig oder gar nicht.


MPPs sind Zahlungstechniken auf Lightning, die es ermöglichen, eine Transaktion in mehrere kleinere Teile zu zerlegen und über verschiedene Routen zu leiten. Mit anderen Worten: Jeder Zahlungsanteil nimmt einen anderen Knotenpunktpfad. Auf diese Weise werden Liquiditätsbeschränkungen auf einem einzigen Kanal auf der Route umgangen. Bei einfachen MPP teilen sich die einzelnen Zahlungsteile dasselbe Geheimnis und daher denselben Hash in HTLC. Dies kann die Transaktion nachvollziehbar machen, wenn ein Beobachter auf mehreren Routen anwesend ist, da er alle diese identischen Geheimnisse miteinander verknüpfen kann. Da das Geheimnis für alle Teile der Zahlung eindeutig ist, ist es außerdem nicht atomar. Das bedeutet, dass einige Teile der Zahlung erfolgreich ausgeführt werden können, während andere fehlschlagen können.


Bei AMP werden für jeden Bruchteil eindeutige Teilgeheimnisse verwendet. Sobald alle Fragmente eingegangen sind, ermöglichen sie es dem Empfänger, das ursprüngliche allgemeine Geheimnis zu rekonstruieren und die volle Zahlung zu fordern. Diese Methode macht eine teilweise Abwicklung der Zahlung unmöglich, da der Besitz aller Teilgeheimnisse erforderlich ist, um die vollständige Zahlung zu entschlüsseln. Dadurch wird sichergestellt, dass die Zahlung entweder vollständig erfolgreich oder vollständig erfolglos ist (d. h. atomar). AMP verbessert auch die Vertraulichkeit, da es keine sichtbaren Verbindungen zwischen verschiedenen Routen mehr gibt.


Ein Vorteil der AMPs ist, dass sie auch dann funktionieren, wenn nur der Empfänger und der Sender diese Methode implementiert haben. Zwischengeschaltete Knoten verarbeiten diese Zahlungen als herkömmliche Transaktionen mit HTLCs, ohne zu wissen, dass sie Bruchteile einer größeren Zahlung verarbeiten.