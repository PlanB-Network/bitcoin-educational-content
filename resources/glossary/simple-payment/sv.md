---
term: Enkel betalning
definition: Transaktionsmodell med 2 utgångar, vanligtvis en betalning och växel.
---

Transaktionsmönster (eller modell) som används i kedjeanalys och som kännetecknas av att en eller flera UTXO förbrukas som insatsvaror och 2 UTXO produceras som utdata. Denna modell kommer därför att se ut så här:





Denna enkla betalningsmodell indikerar att vi sannolikt befinner oss i en sändnings- eller betalningstransaktion. Användaren har förbrukat sin egen UTXO i inputs för att i outputs tillfredsställa en betalning UTXO och en förändring UTXO (förändring som returneras till samma användare). Vi vet därför att den observerade användaren sannolikt inte längre är i besittning av en av de två UTXO:erna i utdata (betalningen), men att de fortfarande är i besittning av den andra UTXO (förändringen).