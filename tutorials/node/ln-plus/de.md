---
name: Lightning Network+
description: Erhalten Sie kostenlose eingehende Liquidität mit kooperativen Eröffnungen auf Ihrem Lightning-Knoten
---

![cover](assets/cover.webp)



## Einführung



[LN+ (Lightning Network Plus)] (https://lightningnetwork.plus/) ist eine Gemeinschaftsplattform, die die Zusammenarbeit zwischen Lightning Network-Knotenbetreibern erleichtern soll. Ihr Hauptziel ist es, die Konnektivität, Liquidität und Dezentralisierung des Lightning-Netzwerks zu verbessern, ohne dass zentralisierte Vermittler benötigt werden.



Dieses Tutorial wird sich auf den **"Swaps "**-Dienst konzentrieren, der heute die am meisten genutzte und strukturierende Funktion von LN+ ist. Die anderen von der Plattform angebotenen Dienste werden ebenfalls vorgestellt.



## LN+ Übersicht



### Was ist Lightning Network Plus?



Lightning Network Plus (LN+) ist eine Gemeinschaftsplattform für Lightning-Knotenbetreiber, die direkt und freiwillig zusammenarbeiten möchten. Sie zielt darauf ab, die Schaffung nützlicher, ausgewogener und nachhaltiger Lightning-Kanäle zu erleichtern und gleichzeitig die Notwendigkeit zentralisierter Lösungen oder aufgezwungener Knotenpunkte zu vermeiden.



LN+ basiert auf einem Grundprinzip: Peer-to-Peer-Zusammenarbeit, die auf Transparenz, Gegenseitigkeit und Reputation beruht.



### LN+ Dienstleistungen auf einen Blick



LN+ bietet mehrere Dienste zur Verbesserung der Topologie und Liquidität des Lightning-Netzes, darunter :





- Swaps**: wechselseitige Öffnung von Kanälen zwischen Betreibern (Hauptdienst).
- Ringe**: kreisförmige Kanalöffnungen zwischen mehreren Teilnehmern.
- Vertrauensbasierte Swaps**: Varianten, die sich stärker auf das Vertrauen und die Vergangenheit der Teilnehmer stützen.
- Soziale Funktionen**: Profile, Kommentare und Reputationssystem.



Im weiteren Verlauf dieses Tutorials konzentrieren wir uns ausschließlich auf den Dienst **Swaps**, der im Mittelpunkt der derzeitigen Nutzung von LN+ steht.



## LN+ "Swaps"-Dienst



### Definition eines LN+ Swaps



Ein LN+ **Swap** ist eine freiwillige Vereinbarung zwischen zwei Betreibern von Lightning-Knotenpunkten zur gegenseitigen Öffnung von Lightning-Kanälen mit gleicher (oder vorher vereinbarter) Kapazität. Im Gegensatz zu einer herkömmlichen einseitigen Kanalöffnung basiert der Swap auf **expliziter Gegenseitigkeit**.



In der Praxis :





- Sie öffnen einen Kanal zum Knoten Ihres Partners.
- Ihr Partner öffnet einen Kanal zu Ihrem Knotenpunkt.
- Beide Parteien binden eine ähnliche Menge an on-chain-Bitcoins.



### Welchen Zweck haben Swaps für Knotenbetreiber?



Der Swaps-Dienst befasst sich mit mehreren zentralen Problemen, mit denen Lightning-Betreiber konfrontiert sind:





- Verbesserte Konnektivität**: Schaffung von nützlichen bidirektionalen Kanälen, sobald sie geöffnet werden.
- Besseres Liquiditätsmanagement**: Jede Partei hat sowohl eingehende als auch ausgehende Kapazitäten.
- Geringeres Risiko von unnötigen Kanälen**: Der Partner wird ermutigt, den Kanal offen zu halten.
- Stärkere Dezentralisierung**: direkte Verbindungen zwischen den Betreibern, ohne vorgeschriebene Knotenpunkte.



### Für welche Knotenprofile sind Swaps sinnvoll?



Swaps sind besonders nützlich für :





- Neue Knotenpunkte, die ihre Routingfähigkeit schnell verbessern wollen.
- Vermittler, die die Dichte ihrer Kanalkurve erhöhen möchten.
- Routing-orientierte Knotenpunkte, die ihre Topologie optimieren wollen.



## Verbinden Sie Ihren Lightning-Knoten mit dem LN+



### Technische Anforderungen



Bevor Sie beginnen, benötigen Sie :





- Ein funktionierender Lightning-Knoten (LND, Core Lightning oder Eclair).
- Zugriff auf die Verwaltungsschnittstelle Ihres Knotens.
- Ausreichende on-chain-Kapazität zur Öffnung der Kanäle.



Rufen Sie die Website [Lightning Network](https://lightningnetwork.plus/) Plus auf und klicken Sie auf die Schaltfläche "Anmelden" oben rechts auf der Benutzeroberfläche.



![capture](assets/fr/03.webp)



### Authentifizierung durch Nachrichtensignatur



Um sich zu authentifizieren, müssen Sie die bereitgestellte Nachricht mit dem privaten Schlüssel Ihres Lightning-Knotens signieren. Mit ThunderHub ist dieser Vorgang sehr einfach.



Beginnen Sie damit, die vom LN+ angezeigte Meldung zu kopieren.



![capture](assets/fr/04.webp)



Gehen Sie im ThunderHub auf die Registerkarte "Tools" und klicken Sie dann auf die Schaltfläche "Signieren" im Abschnitt "Nachrichten".



![capture](assets/fr/05.webp)



Fügen Sie die von LN+ bereitgestellte Authentifizierungsnachricht ein und klicken Sie dann auf "Unterschreiben".



![capture](assets/fr/06.webp)



ThunderHub signiert diese Nachricht dann mit dem privaten Schlüssel Ihres Knotens. Kopieren Sie die generierte Signatur.



![capture](assets/fr/07.webp)



Fügen Sie diese Unterschrift in das entsprechende Feld auf der LN+ Website ein und klicken Sie dann auf "Anmelden".



![capture](assets/fr/08.webp)



Sie sind nun mit Ihrem Lightning-Knoten mit LN+ verbunden. Dieser Vorgang ermöglicht es LN+, zu überprüfen, ob Sie der rechtmäßige Eigentümer des Knotens sind, den Sie auf ihrer Plattform angeben.



![capture](assets/fr/09.webp)



Wenn Sie möchten, können Sie Ihr LN+-Profil personalisieren, z. B. durch Hinzufügen einer kurzen Biografie.



## An einem bestehenden Swap teilnehmen



### Zugang zu Tauschangeboten



Um an Ihrer ersten Kanalöffnung teilzunehmen, gehen Sie zum Menü `Swaps` oben auf der Schnittstelle. Hier finden Sie alle derzeit verfügbaren Swaps, abhängig von den Eigenschaften Ihres Knotens.



![capture](assets/fr/10.webp)



### Bedingungen für die Zuschussfähigkeit



Um einem bestehenden Tauschangebot beizutreten, wählen Sie einfach die entsprechende Anzeige aus und registrieren sich. LN+ erlaubt es dem Ersteller des Tauschangebots jedoch, bestimmte **Zulassungsbedingungen** festzulegen, wie z. B. :





- eine Mindestanzahl von bereits geöffneten Programmen;
- minimale Gesamtknotenkapazität ;
- bestimmte Arten von Verbindungen akzeptiert.



### Neueste Knotenpunkte



Daher kann es vor allem in der Anfangsphase der Nutzung vorkommen, dass **wenige oder keine Angebote** für Ihren Knoten verfügbar sind. Dies ist eine übliche Situation für neue oder noch nicht angeschlossene Knotenpunkte.



In meinem Fall erfüllte trotz der Existenz einiger offener Kanäle keines der Angebote die erforderlichen Kriterien.



## Erstellen Sie Ihr eigenes Tauschangebot



### Wann sollten Sie Ihren eigenen Swap einrichten?



Wenn kein bestehendes Angebot verfügbar ist, ist die Erstellung eines eigenen Swaps oft die beste Lösung. Außerdem behalten Sie so die Kontrolle über die Parameter des Swaps.



### Konfiguration austauschen



Klicken Sie auf **Start Liquidity Swap**, und konfigurieren Sie dann Ihre Angebotsparameter:





- wählen Sie die Gesamtzahl der Teilnehmer (3, 4 oder 5);
- geben die Kapazität der zu öffnenden Kanäle an;
- den Verpflichtungszeitraum festlegen, in dem sich die Teilnehmer verpflichten, ihre Kanäle nicht zu schließen;
- etwaige Beschränkungen für die Teilnehmer angeben (Mindestanzahl der Kanäle, Mindestgesamtkapazität, Art der akzeptierten Verbindung).



![capture](assets/fr/11.webp)



### Veröffentlichung und Erwartungen der Teilnehmer



Sobald Sie alle Parameter eingegeben haben, klicken Sie auf **Liquidity Swap starten**, um Ihr Angebot zu veröffentlichen. Jetzt müssen Sie nur noch darauf warten, dass sich andere Betreiber anmelden.



![capture](assets/fr/12.webp)



## Abschluss eines Swaps



### Effektive Kanalöffnung



Da nun alle Tauschpositionen besetzt sind, kann jeder Teilnehmer auf seiner LN+-Schnittstelle sehen, zu welchem Knoten er einen Lightning-Kanal öffnen muss.



![capture](assets/fr/13.webp)



Öffnen Sie auf Ihrer Seite den Kanal unter Verwendung der von LN+ bereitgestellten Node-ID und unter Beachtung der angegebenen Menge. Dieser Vorgang kann über ThunderHub, einen anderen Lightning-Knotenmanager oder direkt über die Basisschnittstelle Ihres Knotens durchgeführt werden.



![capture](assets/fr/14.webp)



Sobald der Kanal geöffnet ist, erscheint er im Bereich der wartenden Kanäle.



![capture](assets/fr/15.webp)



### Bestätigung in LN+



Kehren Sie dann zu LN+ zurück, um zu bestätigen, dass Sie die Kanalöffnung eingeleitet haben, indem Sie auf die Schaltfläche "Kanalöffnung gestartet" klicken.



![capture](assets/fr/16.webp)



### Ende des Swaps



Wenn alle Teilnehmer die Kanäle, zu denen sie sich verpflichtet haben, geöffnet haben, gilt der Swap als abgeschlossen.



## Reputation und gute Kommunikationspraktiken



### Das LN+ Reputationssystem



LN+ enthält ein Reputationssystem, das auf den von den Teilnehmern am Ende von Swaps hinterlassenen Meinungen basiert. Diese Meinungen sind öffentlich und haben einen direkten Einfluss auf die Fähigkeit eines Betreibers, an zukünftigen Swaps teilzunehmen oder solche zu erstellen.



![capture](assets/fr/17.webp)



### Empfohlene bewährte Verfahren



Um einen guten Ruf zu wahren und den reibungslosen Ablauf von Swaps zu gewährleisten, wird empfohlen, :





- die Fristen für die Öffnung der Kanäle einhalten;
- im Falle eines Problems oder einer Verzögerung schnell zu kommunizieren;
- nutzen Sie den Kommentarbereich, um sich mit anderen Teilnehmern auszutauschen;
- einen Kanal nicht vor Ablauf des Verpflichtungszeitraums zu schließen.




![capture](assets/fr/18.webp)



### Warum Reputation für LN+ von zentraler Bedeutung ist



LN+ basiert auf einem Modell der freiwilligen Zusammenarbeit, ohne starke technische Zwänge. Die Reputation ist daher der Hauptanreiz für die Gewährleistung der Zuverlässigkeit und Vertrauenswürdigkeit der Teilnehmer.



## Andere LN+ Dienstleistungen



Zusätzlich zu Swaps bietet LN+ weitere Dienste, die die Konnektivität und Koordination zwischen den Betreibern von Lightning-Knoten verbessern sollen. Ringe** ermöglichen es mehreren Teilnehmern, eine Schleife von Kanalöffnungen zu bilden und so die Redundanz der Routing-Pfade und die Dichte des Lightning-Graphen zu verstärken. Vertrauensbasierte Swaps** basieren auf ähnlichen Prinzipien wie klassische Swaps, bieten aber Teilnehmern, die bereits einen guten Ruf auf der Plattform haben, mehr Flexibilität.



LN+ integriert auch soziale Funktionen wie öffentliche Knotenprofile, Tauschkommentare und ein Reputationssystem. Bei diesen Tools handelt es sich nicht um technische Dienste an sich, sondern sie spielen eine zentrale Rolle für das reibungslose Funktionieren der Plattform und erleichtern die Kommunikation, die Koordinierung und das Vertrauen zwischen den Betreibern.



## Schlussfolgerung



Der Swaps-Service von LN+ ist ein effektives Werkzeug zur Verbesserung der Konnektivität, Liquidität und Dezentralisierung im Lightning-Netzwerk. Durch die Förderung gegenseitiger, koordinierter Kanalöffnungen ermöglicht LN+ Knotenbetreibern, ihre Topologie zu stärken und gleichzeitig eine verantwortungsvolle, dezentrale Zusammenarbeit zu fördern.