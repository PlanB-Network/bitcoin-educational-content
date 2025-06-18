---
term: MEHRWEGE-ZAHLUNGEN (MPP)
---

Ein allgemeiner Begriff für alle Zahlungstechniken auf Lightning, die es ermöglichen, eine Transaktion in mehrere kleinere Teile aufzuteilen und über verschiedene Routen zu leiten. Mit anderen Worten: Jede Zahlungsfraktion nimmt einen anderen Knotenpfad. Auf diese Weise können Liquiditätsbeschränkungen für einen einzelnen Kanal auf der Route umgangen werden.


Zahlungen auf mehreren Wegen bieten auch leichte Vorteile in Bezug auf die Vertraulichkeit, da es für einen Beobachter schwieriger wird, jedes Zahlungsfragment mit der gesamten Transaktion zu verknüpfen. In der Grundversion teilen sich jedoch alle Fragmente das gleiche Geheimnis für HTLCs, was die Transaktion nachvollziehbar machen kann, wenn ein Beobachter auf mehreren Wegen anwesend ist. Da das Geheimnis für alle Teile der Zahlung eindeutig ist, ist es außerdem nicht atomar. Das bedeutet, dass einige Teile der Zahlung erfolgreich ausgeführt werden können, während andere fehlschlagen können. Diese Nachteile werden mit "Atomic Multi-Path Payment" behoben.