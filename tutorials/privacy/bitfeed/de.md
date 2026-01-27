---
name: Bitfeed
description: Erkunden Sie die Hauptprotokollkette von Bitcoin.
---

![cover](assets/cover.webp)



Bitfeed ist eine Plattform zur Visualisierung der Onchain-Schicht des Bitcoin-Protokolls. Sie wurde von einem der Mitwirkenden am Mempool.space-Projekt initiiert und zeichnet sich vor allem durch ihr minimalistisches Erscheinungsbild und ihre Benutzerfreundlichkeit aus.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

In diesem Tutorial werden wir einen Blick auf dieses Tool werfen, mit dem Sie alle Transaktionen und Blöcke im Netzwerk untersuchen können.



## Erste Schritte mit Bitfeed



Bitfeed ist eine Plattform, die sich auf drei Hauptpunkte konzentriert:





- Blockchain-Konsultation**,
- Transaktionssuche**,
- Visualisierung des Mempools**.



### Beratung in der Blockchain



Auf der Bitfeed-Startseite finden Sie hauptsächlich :





- Die Suchleiste: Dieser Bereich ist der Einstiegspunkt für Blockchain-Abfragen. Hier können Sie nach einem bestimmten Block anhand seiner Nummer oder seines Hashes suchen. Sie können auch nach bestimmten Transaktionen und Bitcoin-Adressen suchen, um bestimmte Transaktionsinformationen im Netzwerk zu überprüfen.



![searchBar](assets/fr/01.webp)



In der oberen linken Ecke sehen Sie den aktuellen Bitcoin-Kurs, geschätzt in US-Dollar (USD).



![price](assets/fr/02.webp)



In der rechten Seitenleiste befindet sich das Plattformmenü. Von diesem Menü aus können Sie die Plattformoberfläche nach Ihren Wünschen anpassen, Elemente hinzufügen oder entfernen und die Anzeigefilter anpassen. Zum Beispiel können Sie die Größe jedes Blocks nach Wert oder nach Gewicht in virtuellen Bytes (vBytes) anzeigen.



![menu](assets/fr/03.webp)



In der Mitte der Seite befindet sich der zuletzt geminte Block mit einer Übersicht über alle Transaktionen, die in diesem Block enthalten sind. Dieser Abschnitt enthält Informationen über den Zeitstempel, die Gesamtzahl der an dem Block beteiligten Bitcoins, die Größe des Blocks in Bytes, die Anzahl der Transaktionen und das durchschnittliche Transaktionskostenverhältnis pro virtuellem Byte im Block.



![block](assets/fr/04.webp)



Sie können den Verlauf des Kanals zurückverfolgen, indem Sie in der Suchleiste nach einem bestimmten Block suchen und ihn nach Ihren Kriterien anzeigen.



Wir möchten zum Beispiel die Transaktionen im Block "879488" anzeigen.



![bloc](assets/fr/05.webp)



Die erste Transaktion dieses Blocks ist die **coinbase**-Transaktion, die es dem Schürfer dieses Blocks ermöglicht, die mining-Belohnung zu verdienen, die erst nach 100 geschürften Blöcken ausgegeben werden kann und sich aus den darin enthaltenen Transaktionsgebühren und dem Block Grant zusammensetzt. Diese Transaktion ist diejenige, die die Ausgabe neuer Bitcoins im System ermöglicht.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f

Standardmäßig werden die Transaktionen in einem Block nach zwei Kriterien dargestellt:




- Die Größe, die zwischen dem Wert und dem Gewicht (vBytes) variieren kann;
- Die Farbe kann je nach Alter und dem Verhältnis der Transaktionsgebühren pro virtuellem Byte variieren.



![options](assets/fr/07.webp)



Daraus können wir schließen, dass alle Transaktionen, die im selben Block enthalten sind, die gleiche Anzahl an Bestätigungen in der Blockchain haben. Die größten Würfel stellen die Transaktionen dar, die den höchsten Betrag an Bitcoins enthalten.



Diese Interpretation wird auch durch die Menüoption **"Info "** bestätigt, die uns über die Übersetzung der Farbe und Größe der Transaktionen des Blocks informiert.



![infos](assets/fr/08.webp)



Sie können die Transaktionen eines Blocks auch nach virtuellen Bytes und Gebührenverhältnis anzeigen. Diese Ansicht kann sich von der vorherigen unterscheiden, da der Bitcoin-Wert, der in einer Transaktion enthalten ist, nicht deren Größe definiert.



![visualisation](assets/fr/09.webp)



### Anzeigen von Transaktionen



Sie können über die Suchleiste nach einer Transaktion anhand ihrer Kennung suchen. Sie können auch auf einen Würfel klicken, um die Informationen zu dieser Transaktion anzuzeigen.



In unserem Fall nehmen wir die Transaktion, die den größten Platz im Block "879488" belegt.



![biggest](assets/fr/10.webp)



Sie werden sehen, dass diese Transaktion "42.989" hat, was die Differenz zwischen dem letzten Block, der abgebaut wird, und unserem gewählten Block darstellt. Diese Bestätigungen tragen dazu bei, die Sicherheit des Bitcoin-Netzwerks zu stärken, denn um diese Transaktion böswillig zu verändern, müssten Angreifer über die gleiche Rechenleistung verfügen, um die gesamte Hauptblockkette neu zu schreiben.



Die Größe dieser Transaktion beträgt 57.088 vByte, was vor allem auf die große Anzahl von UTXOs zurückzuführen ist, die bei ihrer Erstellung verwendet wurden (842 Einträge). Überraschenderweise ist der angewandte Gebührensatz relativ niedrig (nur 4 sats/vByte), verglichen mit dem Gesamtdurchschnitt der Blöcke von 5,82 sats/vByte.



Die Transaktion, die den meisten Platz beansprucht, ist also nicht unbedingt die Transaktion mit dem höchsten Transaktionskostenverhältnis.



![transaction](assets/fr/11.webp)



Wenn Sie der Skala im Menü **Info** folgen, ist die Transaktion mit dem höchsten Transaktionskostenverhältnis lila. Dies ist die Transaktion [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) mit einem Transaktionskostenverhältnis von `147,49 sats/vBytes`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Mempool-Visualisierung



Der Mempool ist der virtuelle Ort, an dem Bitcoin-Transaktionen, die darauf warten, in einen Block aufgenommen zu werden, gruppiert werden. Bitfeed ermöglicht die Abfrage des [mempool](https://planb.academy/resources/glossary/mempool) von mehreren Bitcoin Minern und bietet damit eine breite Palette von Transaktionsverfolgung.



![mempool](assets/fr/13.webp)



In diesem Bereich können Sie alle gültigen und noch unbestätigten Transaktionen auf der Hauptkette des Bitcoin-Netzwerks verfolgen.



![unconfirmed](assets/fr/14.webp)



Sie haben nun einen Leitfaden für die Nutzung der Bitfeed-Plattform zur Analyse von Blöcken und Transaktionen, um die auf der Hauptkette des Bitcoin-Netzwerks verfügbaren Informationen zu visualisieren und gleichzeitig von einer minimalistischen, einfach zu bedienenden Schnittstelle zu profitieren. Wenn Ihnen dieses Tutorial gefallen hat, empfehlen wir Ihnen, den nächsten Schritt zu machen: Entdecken Sie Lightning Network über das Amboss-Projekt.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017