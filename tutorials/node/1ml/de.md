---
name: 1ML
description: Erfahren Sie, wie Sie den 1ML-Explorer verwenden können, um das Lightning-Netzwerk von Bitcoin zu verstehen und zu analysieren.
---
![cover](assets/cover.webp)



## Einführung



Lightning Network ist eine schnelle, kostengünstige Zahlungslösung, die auf Bitcoin aufbaut und sofortige, sichere Transaktionen ermöglicht. Die Beobachtung dieses Netzes ist wichtig, um zu verstehen, wie es funktioniert, seine Topologie und den Zustand der Knoten, aus denen es besteht. Ein Lightning-Explorer wie 1ML dient zur Visualisierung der öffentlichen Daten des Netzes, einschließlich aktiver Knoten, offener Kanäle und verfügbarer Kapazitäten, und bietet Nutzern, Entwicklern und Knotenbetreibern einen wertvollen Überblick.



## Zugang zu 1ML und Verstehen der Homepage



Um auf 1ML zuzugreifen, öffnen Sie einfach Ihren Webbrowser und geben Sie [https://1ml.com](https://1ml.com) ein. Dadurch gelangen Sie auf die Homepage, die als globales Dashboard des Lightning Network dient.



![capture](assets/fr/03.webp)



Auf dieser Seite werden oben auf dem Bildschirm mehrere wichtige Statistiken angezeigt, darunter :





- Die **Gesamtzahl der aktiven Knoten** im Netz, d. h. der Computer, die am Senden und Empfangen von Blitzzahlungen beteiligt sind.
- Die **Anzahl der offenen Kanäle**, die den Verbindungen zwischen diesen Knotenpunkten entsprechen und Geldtransfers ermöglichen.
- Die **gesamte Netzwerkkapazität**, ausgedrückt in Bitcoin (BTC), die die Summe der Kapazitäten aller öffentlichen Kanäle angibt.



Diese Zahlen werden regelmäßig aktualisiert, um den aktuellen Stand des Netzes widerzuspiegeln. Sie vermitteln einen Eindruck von dessen Größe, Wachstum und Robustheit.



![capture](assets/fr/04.webp)



Gleich darunter bietet die Seite Listen mit Ranglisten:





- Die **am meisten verbundenen Knoten**, die die meisten offenen Kanäle zu anderen Knoten haben.
- Die **höchsten Kapazitäten** auf den Knoten, die angeben, welche Knoten die größten Mengen übertragen können.
- Die wichtigsten Kanäle in Bezug auf die Kapazität.



Mit Hilfe von Filtern lassen sich diese Listen auch nach geografischem Standort oder anderen Kriterien verfeinern.



Diese Seite ist ein idealer Ausgangspunkt, um Lightning Network zu erkunden und seine allgemeine Topologie zu verstehen.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Erkundung von Blitzknoten



Um einen Knoten auf 1ML zu suchen, verwenden Sie zunächst die Suchleiste oben auf der Seite. Sie können die **Knoten-ID** eingeben, d. h. den eindeutigen Bezeichner des Knotens, oder seinen **Alias**, der einen leichter zu merkenden Namen darstellt.



Sobald die Suche abgeschlossen ist, klicken Sie auf den entsprechenden Knoten, um dessen Detailseite aufzurufen.



![capture](assets/fr/07.webp)



Auf dieser Seite werden mehrere wichtige Informationen angezeigt:





- Knoten-ID**: Diese eindeutige Kennung ist eine lange Zeichenkette, mit der der Knoten im gesamten Netz genau identifiziert werden kann.



![capture](assets/fr/08.webp)





- Alias**: Dies ist der Name, den der Eigentümer des Knotens gewählt hat, um ihn öffentlich darzustellen.



![capture](assets/fr/09.webp)





- Die **Anzahl der Kanäle** gibt an, wie viele Verbindungen der Knoten mit anderen Knoten geöffnet hat, während die **Gesamtkapazität** die Summe der in diesen Kanälen verfügbaren Bitcoins darstellt. Ein Knoten mit einer großen Anzahl von Kanälen und einer hohen Kapazität ist im Allgemeinen gut vernetzt und in der Lage, große Geldbeträge schnell über das Netzwerk zu transferieren.



![capture](assets/fr/10.webp)





- Die **Uptime** oder Verfügbarkeit gibt an, wie lange ein Knoten aktiv und online erreichbar war, was seine Zuverlässigkeit widerspiegelt. Das **Alter** des Knotens gibt andererseits an, wie lange er bereits im Netz präsent ist, was seine Stabilität und Erfahrung innerhalb von Lightning Network widerspiegelt.



![capture](assets/fr/11.webp)



Diese Daten helfen Ihnen, die Bedeutung und Zuverlässigkeit eines Knotens in Lightning Network zu verstehen. Beispielsweise ist ein Knoten mit einer großen Anzahl von Kanälen, hoher Kapazität und hoher Betriebszeit oft ein wichtiger Akteur im Netz.



## Erkundung von Blitzkanälen



### Was ist ein Lightning-Kanal?



Ein Lightning-Kanal ist eine direkte Verbindung zwischen zwei Netzwerkknoten. Er ermöglicht es diesen beiden Knoten, sofortige, kostengünstige Zahlungen auszutauschen, ohne für jede Transaktion die Bitcoin-Hauptkette zu durchlaufen. Kanäle sind die Grundlage, die Lightning Network schnell und skalierbar macht.



### Kanalinformationen auf 1ML lesen



Auf 1ML hat jeder Kanal eine eigene Seite oder ein Beschreibungsblatt mit einer Reihe wichtiger Daten:



Von der Seite eines Knotens aus können Sie auf eine Liste der Kanäle zugreifen. Wenn Sie auf einen Kanal klicken, zeigt 1ML eine spezielle Seite mit mehreren wichtigen Informationen an.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



Die wichtigsten sichtbaren Daten sind folgende:





- Partnerknoten**: Jeder Kanal verbindet zwei Knoten. 1ML zeigt beide Identifikatoren und ihre jeweiligen Aliasnamen an.



![capture](assets/fr/14.webp)





- Kanalkapazität**: Dies ist die Gesamtmenge an Bitcoins, die in diesem Kanal gesperrt ist. Diese Kapazität stellt die Höchstgrenze der Zahlungen dar, die über diesen Kanal laufen können.



![capture](assets/fr/15.webp)





- Kanalalter**: gibt an, wie lange der Kanal bereits offen ist. Ein alter Kanal ist oft ein Zeichen für eine stabile Beziehung zwischen zwei Knoten.



![capture](assets/fr/16.webp)



### Grenzen der Sichtbarkeit des Kanals



Es ist wichtig zu verstehen, dass 1ML nur **einen Teil** von Lightning Network anzeigt. Der Explorer zeigt nur **öffentliche Kanäle**, d. h. solche, die im Netz bekannt gegeben wurden. Private Kanäle, die oft aus Gründen der Vertraulichkeit oder Strategie verwendet werden, sind nicht sichtbar. Darüber hinaus zeigt 1ML weder die genaue Verteilung der Mittel auf jeder Seite eines Kanals noch die getätigten Zahlungen oder die zu einem bestimmten Zeitpunkt tatsächlich verfügbare Liquidität an. Die angezeigten Informationen können daher zur Analyse der **allgemeinen Struktur des Netzwerks** verwendet werden, nicht aber zur Analyse der tatsächlichen finanziellen Aktivitäten oder des detaillierten Liquiditätsstatus.



## Lightning Network nach Standort erkunden



### Knotenpunkte nach Land und Region



1ML ermöglicht es Ihnen, Lightning Network nach einer **geografischen Aufschlüsselung** zu erkunden. Von der Startseite aus oder über spezielle Abschnitte ist es möglich, Knoten nach Land oder Region anzuzeigen. Diese Funktion basiert auf den von den Knotenbetreibern angegebenen Standortinformationen.


In der Navigationsleiste finden Sie den Link **Location**. Auf der Seite sind die Knotenpunkte nach Kontinent, Land und Stadt gruppiert.



![capture](assets/fr/17.webp)



Wenn Sie ein Land auswählen, zeigt 1ML eine Liste der zugehörigen Knoten an, zusammen mit aggregierten Statistiken wie der Anzahl der Knoten und der sichtbaren Gesamtkapazität für dieses geografische Gebiet.



#### Was dies über die lokale Adoption aussagt





- Technologieübernahme**: Eine große Anzahl von Knoten in einer Region deutet darauf hin, dass Bitcoin-Nutzer, Unternehmen oder Dienste Lightning Network aktiv übernehmen. Dies zeugt von technologischer Reife und der Bereitschaft, die Vorteile von Lightning (schnelle Transaktionen, niedrigere Kosten) zu nutzen.
- Wirtschaftliches Ökosystem** : Das dichte Vorhandensein von Knotenpunkten kann auch ein Zeichen für ein lokales Wirtschaftsgefüge um Bitcoin sein: Händler, die Lightning akzeptieren, Start-ups, die Tools entwickeln, Gemeinschaftsveranstaltungen usw.
- Sicherheit und Ausfallsicherheit**: Die vielfältige geografische Verteilung erhöht die Ausfallsicherheit des Netzes bei lokalen Ausfällen oder Einschränkungen. Je weiter die Knoten verstreut sind, desto dezentraler und schwieriger zu zensieren ist das Netz.
- Politische Maßnahmen und Vorschriften**: In einigen Ländern kann die Einführung dank eines günstigen Rechtsrahmens oder einer proaktiven Gemeinschaft schneller erfolgen. Umgekehrt wird in Gebieten mit strengen oder feindlichen Vorschriften die Zahl der Knotenpunkte geringer sein.



#### Grenzen der geografischen Daten



Bedenken Sie jedoch, dass die Geolokalisierung von Lightning-Knotenpunkten ihre Grenzen hat und mit Verzerrungen verbunden ist:





- Ungefährer IP-Standort**: 1ML verwendet im Allgemeinen die öffentliche IP-Adresse von Knoten, um deren Standort zu schätzen. Diese Methode kann jedoch durch die Verwendung von VPNs, Cloud-Servern (AWS, Google Cloud) oder Hosting in anderen Ländern als dem tatsächlichen Wohnsitz des Knotenbesitzers verzerrt werden.
- Virtuelle Knotenpunkte**: Einige Betreiber hosten ihre Knoten aus Gründen der Zuverlässigkeit und Verfügbarkeit auf entfernten Servern, was einen falschen Eindruck vom physischen Standort vermitteln kann.
- Mobilität der Benutzer**: Der Betreiber eines Knotens kann den Standort wechseln, seine Infrastruktur verlagern oder mehrere Knoten in verschiedenen Regionen einrichten, was das Auslesen der Daten erschwert.
- Unsichtbarkeit von privaten Knoten**: Einige Knoten veröffentlichen ihre IP-Adresse nicht oder verwenden Methoden, um ihren Standort zu verbergen, was eine Geolokalisierung unmöglich macht.



## 1ML konkrete Anwendungsfälle



### Verständnis der Netzwerktopologie



1ML ermöglicht es Ihnen, die **allgemeine Struktur von Lightning Network** zu visualisieren. Durch die Beobachtung der Verbindungen zwischen den Knoten, der Anzahl der Kanäle und der Gesamtkapazität ist es möglich zu verstehen, wie das Netzwerk organisiert ist, welche Knoten eine zentrale Rolle spielen und wie Zahlungsströme theoretisch zirkulieren können.



Dieses Verständnis ist unerlässlich, wenn wir verstehen wollen, wie der Lightning Network funktioniert, und zwar nicht nur für die Verwendung im Portfolio.



### Identifizieren Sie wichtige Knotenpunkte



Dank der von 1ML angebotenen Rankings (am meisten verbundene Knoten, höchste Kapazität, Alter) ist es möglich, die Knoten zu identifizieren, die einen wichtigen Platz im Netzwerk einnehmen. Diese Knoten dienen oft als wichtige Gateways für Lightning-Zahlungen.



![capture](assets/fr/18.webp)



### Überprüfung der öffentlichen Sichtbarkeit eines Knotens



Als Knotenbetreiber können Sie mit 1ML überprüfen, ob Ihr Knoten auf Lightning Network **öffentlich beworben** wird. Wenn ein Knoten auf 1ML erscheint, bedeutet dies, dass er für andere Knoten sichtbar und zugänglich ist, um öffentliche Kanäle zu öffnen.


Dies kann bei der Diagnose von Sichtbarkeits- oder Konnektivitätsproblemen hilfreich sein.



### Beobachtung der Entwicklung von Lightning Network im Laufe der Zeit



Durch den Vergleich globaler Statistiken über verschiedene Zeiträume ermöglicht 1ML die Beobachtung der Entwicklung von Lightning Network: Zunahme oder Abnahme der Anzahl der Knotenpunkte, Schwankungen der Gesamtkapazität oder Veränderungen der geografischen Verteilung.


Diese Beobachtungen bieten eine interessante Perspektive auf das Wachstum, den Reifegrad und die Trends von Lightning Network.



## 1ML-Best Practices und Einschränkungen



### Öffentliche Daten ≠ vollständige Realität



1ML basiert ausschließlich auf den **öffentlich bekannt gegebenen** Daten zu Lightning Network. Das bedeutet, dass das Tool nur einen Teil der Realität abbildet. Viele Kanäle können privat sein, einige Knotenpunkte werden möglicherweise nicht bekannt gegeben, und die tatsächlich in den Kanälen verfügbare Liquidität ist nicht sichtbar. Es ist daher wichtig, 1ML als globales Analysewerkzeug zu verwenden, nicht als umfassende Darstellung des Netzwerks.



### Datenschutz und Blitzschutz



Lightning Network wurde mit einem starken Fokus auf **Zahlungsschutz** entwickelt. Einzelne Transaktionen sind auf 1ML nicht sichtbar, und die exakten Kontostände sind nicht öffentlich. Diese Einschränkung ist kein Fehler des Explorers, sondern ein grundlegendes Merkmal von Lightning Network, das die Privatsphäre der Nutzer schützen soll.



### Ziehen Sie keine voreiligen Schlüsse



Ein Knoten mit hoher Kapazität oder vielen Kanälen ist nicht unbedingt in allen Fällen "zuverlässiger" oder "effizienter". Ebenso bedeutet ein vorübergehender Rückgang der Gesamtnetzkapazität nicht unbedingt ein strukturelles Problem. Zahlen sollten immer im Nachhinein interpretiert und in einen Kontext gestellt werden.



### Komplementarität mit anderen Instrumenten



1ML ist ein hervorragender Ausgangspunkt für die Erkundung von Lightning Network, aber es wird am besten in Verbindung mit anderen Tools wie Lightning-Portfolios, Knotenverwaltungsschnittstellen und anderen Erkundungsprogrammen verwendet. Dieser Ansatz bietet einen vollständigeren und differenzierteren Blick auf das Netzwerk.



## 1ML-Verbindungsoption (erweiterte Funktionalität)



1ML bietet eine auf der Website sichtbare Option **Anmelden / Konto erstellen**, die jedoch **nicht erforderlich** ist, um Lightning Network-Daten anzuzeigen. Alle bisher in dieser Anleitung besprochenen Funktionen sind **ohne Konto** verfügbar.



Die Verbindung richtet sich in erster Linie an **Lightning-Knotenbetreiber**. Sie ermöglicht es insbesondere, einen Knoten mit einem 1ML-Konto zu verknüpfen, um bestimmte öffentliche Informationen wie die Präsentation des Knotens, Kontaktlinks und andere Metadaten zu verwalten. Diese Funktion soll die Sichtbarkeit und Identifizierung eines Knotens innerhalb des Explorers verbessern.



Es ist wichtig zu beachten, dass 1ML **keine Verwahrungsdienstleistung** ist. Die Einrichtung eines Kontos gibt keinen Zugang zu Geldern, Kanälen oder Zahlungen eines Knotens. Es dient lediglich der Interaktion mit dem Explorer in deklarativer und informativer Hinsicht.



Im Zusammenhang mit dem Erlernen oder Entdecken der Lightning Network kann diese Option daher als **optional** betrachtet werden und ist fortgeschrittenen Nutzern vorbehalten.



## Schlussfolgerung



1ML ist ein wertvolles Instrument zur Beobachtung und zum Verständnis von Lightning Network anhand seiner öffentlichen Daten. Es ermöglicht Ihnen, die Struktur des Netzwerks zu erkunden, Knoten und Kanäle zu analysieren und die allgemeine Entwicklung der Lightning Network-Übernahme im Laufe der Zeit zu verfolgen. Ohne die Notwendigkeit eines Kontos oder der Handhabung von Geldmitteln bietet 1ML einen zugänglichen Zugang für jeden, der sein Verständnis der Funktionsweise von Lightning vertiefen möchte.


Wenn Sie sich eingehender mit dem Lightning Network beschäftigen möchten, empfehle ich Ihnen den vollständigen Kurs Einführung in den Lightning Network:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb