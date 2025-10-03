---
name: Mempool
description: Erkunden Sie das gesamte Bitcoin-Ökosystem.
---

![cover](assets/cover.webp)



Das Bitcoin-Protokoll ist ein pseudonymes, dezentralisiertes Netz, das für Konsultationen offen ist. Die Mitglieder (Knoten), d. h. Computer mit einer Instanz der Bitcoin-Software, haben uneingeschränkten Zugang zu allen auf Bitcoin veröffentlichten Daten. In den Anfangsjahren von Bitcoin war das Protokoll jedoch nicht so allgemein zugänglich wie heute.


In den Anfängen von Bitcoin war es notwendig, einen Bitcoin-Knoten zu betreiben, um auf die entsprechenden Tools (bitcoin-cli) zuzugreifen, mit denen das Netz über die Befehlszeilen abgefragt werden konnte.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Daher wurden Projekte ins Leben gerufen, um die Bitcoin-Gemeinschaft zu erweitern und sie für alle zugänglich zu machen, die keinen Knoten besitzen und/oder nicht über die erforderlichen technischen Kenntnisse verfügen.



In diesem Tutorial werden wir uns das **Mempool.space** Projekt, seine Funktionen und die Auswirkungen auf das Bitcoin Ökosystem ansehen.



## Was ist Mempool.space?



**Mempool.space** ist ein Open-Source-Explorer, der nützliche Informationen über Transaktionen, Transaktionsgebühren, Blöcke und Miner in den verschiedenen Bitcoin-Protokollnetzwerken liefert. Er wurde 2020 eingeführt und bietet eine deutliche Verbesserung der Benutzerfreundlichkeit durch repräsentative Grafiken, sanfte Animationen und übersichtliche Schnittstellen.



Um das Projekt zu verstehen, ist ein Mempool (Speicherpool) ein virtueller Raum, in dem alle Transaktionen, die im Bitcoin-Netz auf ihre Bestätigung warten, gespeichert werden. Ein Mempool ist wie ein "Warteraum", in dem Bitcoin-Transaktionen auf ihre Bestätigung warten. Jeder Computer im Netz (Knoten) hat seinen eigenen Warteraum, was erklärt, warum nicht alle Transaktionen für alle gleichzeitig sichtbar sind.



Die wichtigste Auswirkung der Plattform im Bitcoin-Ökosystem besteht darin, dass sie Ihnen den Zugriff auf die vielfältigen Informationen in den Speicherbereichen der meisten Bitcoin-Knoten ermöglicht, ohne dass Sie einen ausführen müssen. Mempool.space ist ein Repository für die Anzeige und Suche von Bitcoin-Protokollnetzwerken.



Die zunehmende Verbreitung im Ökosystem und die Tatsache, dass Mempool.space Open Source ist, haben dazu geführt, dass es in immer mehr persönliche Hosting-Systeme integriert wird. Sie können jetzt Ihre eigene Instanz von Mempool.space direkt auf Ihrem persönlichen Knoten haben. Sehen Sie sich unser Tutorial zur Konfiguration von Mempool.space auf Ihrem Umbrel-Knoten an.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Die Grundlagen von Mempool.space



Wie bereits erwähnt, ist [Mempool.space] (https://Mempool.space) ein Bitcoin-Protokoll-Explorer, mit dem Sie Ihre Transaktionen und deren Ausbreitung im gewählten Bitcoin-Netzwerk in Echtzeit von einem grafischen Interface aus überwachen können.



Mempool.space unterstützt viele Bitcoin-Protokollnetze.


In der Menüleiste finden Sie die folgenden Netzwerke:




- **Mainnet**: Das wichtigste Bitcoin-Netz, in dem echte Bitcoin-Transaktionen stattfinden.
- **Signet**: Ein Testnetz, das digitale Signaturen zur Validierung von Blöcken verwendet, ohne die vom Hauptnetz benötigten Ressourcen zu benötigen.
- **Testnet 3**: Ein risikofreies Test- und Entwicklungsnetz auf Basis des Bitcoin-Protokolls.
- **Testnet 4**: Die neue Version von Testnet 3 bringt mehr Stabilität und neue Konsensregeln in die Testumgebung.



![reseaux](assets/fr/01.webp)



Auf der Startseite, links in Green, sehen Sie die möglichen zukünftigen Blöcke (Gruppen von Transaktionen), die bereit sind, validiert und in das Bitcoin-Netzwerk integriert (abgebaut) zu werden. Im Durchschnitt wird alle zehn Minuten ein Block abgebaut: Bewahren Sie diese Information auf, denn sie wird sich später in unserer Entwicklung als nützlich erweisen.


In violett auf der rechten Seite finden Sie die zuletzt auf Bitcoin abgebauten Blöcke, wobei die Nummer des letzten abgebauten Blocks die aktuelle Höhe des Netzwerks darstellt.



![blocs](assets/fr/02.webp)



Der Abschnitt **Transaktionsgebühren** ist ein Schätzer für Transaktionsgebühren. Je höher die Gebühren für Ihre Transaktion sind, desto wahrscheinlicher ist es, dass Ihre Transaktion dem nächsten Block hinzugefügt wird, der zum Mining bereit ist.


Die Transaktionsgebühren stellen die Kosten dar, die ein Miner von Ihnen verlangt, um Ihre Transaktion in einen Kandidatenblock für Mining einzufügen. Sie werden durch ein Verhältnis von sat/vB (Satoshi/Virtual Bytes) definiert, das die Anzahl der Satoshis angibt, die Sie für den Platz bezahlen, den Ihre Transaktion in dem Kandidatenblock einnehmen wird.



⚠️ WICHTIG: Im Falle einer Mempool-Sättigung priorisieren die Miner Transaktionen mit dem besten Satoshi/vByte-Verhältnis. Je schwerer (größer) Ihre Transaktion ist, desto mehr Satoshis braucht sie, um schnell aufgenommen zu werden.



![fees-visualizer](assets/fr/03.webp)



Der Bereich **Mempool Goggles** ermöglicht es Ihnen, den von einer Transaktion belegten Raum zu visualisieren.



![mempool](assets/fr/04.webp)



Aufgrund der Schwierigkeit des Proof of Work, das die Schürfer bereitstellen müssen, um ihren Blockkandidaten in die Kette der geschürften Blöcke aufzunehmen, wird etwa alle zehn Minuten ein Block geschürft. Diese Schwierigkeit ändert sich alle **2016 Blöcke**, was etwa **2 Wochen** entspricht. Sie können die Entwicklung dieser Schwierigkeit hier sehen.



![difficulty](assets/fr/05.webp)



Die Aufnahme eines neuen Blocks in die Hauptkette berechtigt den Miner des validierten Blocks zu einer Belohnung, die sich aus einem festen Anteil (der alle 210.000 Blöcke** halbiert wird, was während der Halbierungen etwa 4 Jahren** entspricht) und Transaktionsgebühren zusammensetzt.



![halving](assets/fr/06.webp)



## Zugang zu Ihren Transaktionsdetails



In der Mempool.space-Suchleiste können Sie Ihren Bitcoin Address oder Ihren transaction ID eingeben, um mehr über Ihre Geschichte zu erfahren.



![search](assets/fr/07.webp)



Auf der Seite mit den Transaktionsdetails finden Sie allgemeine Informationen zu Ihrer Transaktion:




- **Status**: Bestätigt, wenn zu einem Block hinzugefügt, unbestätigt, wenn in einem Mempool wartend.
- **Transaktionsgebühren**.
- **Geschätzte Ankunftszeit (ETA)**: Die ungefähre Zeit, die es dauert, bis Ihre Transaktion zu einem Block hinzugefügt wird. Sie wird nach dem Verhältnis berechnet, das die mit dieser Transaktion verbundenen Gebühren ausmacht.



![general-txinfo](assets/fr/08.webp)



Der Abschnitt **Flow** zeigt ein Diagramm der Komponenten Ihrer Transaktion.



Inputs (vorherige UTXO), die für Ihre Transaktion verwendet werden, und Outputs, die den Empfängern das Recht geben, die Bitcoins aus jedem Output zu verwenden, indem sie die für ihre Ausgaben erforderliche Unterschrift vorlegen.



![flow](assets/fr/09.webp)



Weitere Einzelheiten zu den verwendeten Adressen finden Sie im Abschnitt **Eingänge und Ausgänge**.



![address](assets/fr/10.webp)



Entdecken Sie die verschiedenen Bitcoin-Transaktionsschemata, um Ihre Vertraulichkeit zu verbessern.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Beschleunigen Sie Ihre Transaktionen



Im Bitcoin-Ökosystem ist der Aspekt der Transaktionsvalidierung durch Miner untrennbar mit den Transaktionsgebühren verbunden, die mit dieser Transaktion verbunden sind. Miner bevorzugen Transaktionen mit einem höheren Gebührenverhältnis (Satoshis/vBytes), was die Gültigkeit Ihrer Transaktion beeinträchtigen könnte, wenn Sie keine angemessenen, von Minern akzeptierten Gebühren zahlen. Ihre Transaktion würde in Mempool stecken bleiben, während sie auf einen Block wartet, der ihr Gebührenverhältnis akzeptiert.



Zum Glück gibt es im Bitcoin-Netz zwei Methoden, um die Bestätigung Ihrer Transaktion zu beschleunigen.





- **RBF** - Ersetzung durch Gebühr: Eine Methode, die es Ihnen ermöglicht, dieselben Einträge wie bei der Transaktion mit niedriger Gebühr auszugeben, aber dieses Mal durch Erhöhung der Transaktionsgebühr, um die Validierung zu beschleunigen. Ihre neue Transaktion wird schneller validiert und in einen Block aufgenommen, wodurch die Transaktion mit niedriger Gebühr ungültig wird.



Sie können mit Portfolios, die diesen Mechanismus akzeptieren, eine Gebührenersatzaktion durchführen. Siehe zum Beispiel unseren Artikel über das Portfolio Blue Wallet.



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent: Ein Ansatz, der sich an RBF anlehnt, aber auf der Seite des Empfängers. Wenn die Transaktion, bei der Sie der Empfänger sind, in einem Mempool blockiert wird, haben Sie die Möglichkeit, die Outputs (UTXOs) dieser Transaktion auszugeben, obwohl sie noch nicht bestätigt wurde, indem Sie dieser neuen Transaktion mehr Gebühren zuweisen, so dass die durchschnittlichen Gebühren - der Transaktion, bei der Sie der Empfänger sind, und der initiierten Transaktion - die Miner dazu veranlassen, beide Transaktionen in einen Block aufzunehmen.



⚠️ Die erste Transaktion muss in einem Block enthalten sein, damit die zweite Transaktion bestätigt werden kann.



Wenn Ihnen all diese Begriffe etwas zu technisch erscheinen, empfehle ich Ihnen, [unser Glossar](https://planb.network/resources/glossary) zu konsultieren, das Definitionen aller Fachbegriffe im Zusammenhang mit Bitcoin und seinem Ökosystem enthält.



Zusätzlich zu diesen Methoden ermöglicht Mempool.space dank seiner Verbindungen zu mehr als 80 % der Miner im Bitcoin-Netzwerk auch die Beschleunigung jeder Ihrer **unbestätigten** Transaktionen, selbst derjenigen, die RBF nicht aktivieren, indem Sie den Minern in Exchange eine Gegenleistung dafür zahlen, dass sie Ihre kostengünstige Transaktion in den nächsten Block einfügen, der zum Mining bereit ist.



Klicken Sie auf der Seite mit den Transaktionsdetails auf die Schaltfläche **Beschleunigen**, und fahren Sie dann fort, Ihre Gegenpartei an die Miner zu bezahlen.



![accelerate-section](assets/fr/11.webp)


## Minderjährige



Ein Miner bezieht sich auf eine Person, die eine Mine verwaltet, d. h. einen Computer, der am Mining-Prozess beteiligt ist, der aus der Teilnahme an Proof-of-Work besteht. Der Miner fasst die ausstehenden Transaktionen in seinem Mempool zu einem Kandidatenblock zusammen. Er sucht dann nach einem gültigen Hash, der kleiner oder gleich dem Zielwert ist, für den Header dieses Blocks, indem er die verschiedenen Nonces modifiziert. Findet er eine gültige Hash, sendet er seinen Block an das Bitcoin-Netzwerk und kassiert die damit verbundene finanzielle Belohnung, die sich aus der Blocksubvention (Schaffung neuer Bitcoins ex nihilo) und der Transaktionsgebühr zusammensetzt.



https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

miner sind wie "Validierer", die Transaktionen überprüfen und zu Blöcken zusammenfassen. Um dem Bitcoin-Netzwerk einen neuen Block hinzuzufügen, müssen sie ein komplexes mathematisches Rätsel lösen (das Proof-of-Work). Der erste Miner, der das Rätsel löst, gewinnt eine Bitcoin-Belohnung (Blockzuschuss + Gebühren für die im Block enthaltenen Transaktionen).



Der Schwierigkeitsgrad dieses Proof of Work wird überwacht, so dass Sie die Entwicklung der für Miner erforderlichen Rechenleistung visualisieren können. Sie finden in den folgenden Abschnitten:





- Eine Schätzung der Gesamtbelohnungen, die von Bergleuten während der letzten Schwierigkeitsanpassung erzielt wurden, sowie Schätzungen für die nächste Halving der Blockvergabe, die alle 210.000 Blöcke (ca. 04 Jahre) erfolgt.



![rewards](assets/fr/12.webp)



Diese Schwierigkeit wird alle 2016 Blöcke (etwa zwei Wochen) angepasst. Sie ist umgekehrt proportional zu der durchschnittlichen Zeit, die die Bergleute für Miner alle 2016 Blöcke benötigen.


Wenn der durchschnittliche Zeitaufwand der Miner weniger als 10 Minuten beträgt, steigt die Schwierigkeit, was beweist, dass es für die Miner einfacher war, Miner-Blöcke zu validieren. Umgekehrt nimmt die Schwierigkeit ab, wenn der durchschnittliche Zeitaufwand größer als 10 Minuten ist.



![mining-pool](assets/fr/13.webp)





- Gruppen von Bergleuten: In Anbetracht der damit verbundenen Schwierigkeiten arbeitet eine Gruppe von Minern zusammen, um die Proof of Work auf Bitcoin zu finden, und zwar in einem sogenannten **Pool**. Wenn ein Block von der Gruppe geschürft wird, wird die erhaltene Belohnung entsprechend dem Prozentsatz des Erfolgs bei der Suche nach einer Teillösung für jeden Miner, d. h. dem Beitrag an Rechenleistung bei der Suche nach Proof-of-Work, oder entsprechend der im Rahmen der Zusammenarbeit vereinbarten Vergütungsmethode verteilt.





![mining](assets/fr/14.webp)



## Lightning Network Infrastruktur



Mempool bietet nicht nur Informationen über die Netzinfrastruktur von Bitcoin (Hauptkette). Es integriert auch Visualisierungs- und Erkundungstools für das Lightning-Overlay von Bitcoin.



Im Abschnitt **Lightning** können Sie alle bestehenden Verbindungen zwischen Lightning-Knoten anzeigen.



![network-stats](assets/fr/15.webp)



Dieser Interface enthält Informationen über :





- Lightning Network-Statistiken.



![distribution](assets/fr/16.webp)




⚠️ **WICHTIG**: Die Kapazität eines Zahlungskanals gibt den maximalen Betrag an, den ein Knoten während einer Lightning-Transaktion an einen anderen Knoten senden kann.





- Die Blitzknoten werden je nach Internetdienstanbieter (Hosting-Dienst) und optional je nach Kapazität des Zahlungskanals zugewiesen.



![distribution](assets/fr/17.webp)





- Die Geschichte der Gesamtkapazität des Lightning Network.


Hier finden Sie auch eine Rangliste dieser Knotenpunkte nach der Kapazität ihrer Zahlungskanäle.



![ranking](assets/fr/18.webp)



## Mehr Grafiken



Mempool.space ist die ideale Plattform, um die Interaktion mit Bitcoin-Protokollnetzen zu genießen. Die Diagramme liefern nicht nur visuelle Daten, die Ihnen helfen zu entscheiden, wann Sie Transaktionen durchführen sollten, sondern auch präzise Parameter, die es Ihnen ermöglichen, die Stärke und den Zustand des Bitcoin-Netzes und der zugehörigen Lightning-Infrastrukturen in Echtzeit zu visualisieren.



Im Bereich **Grafik** können Sie wichtige Daten über das Bitcoin-Netz einsehen:




- Entwicklung der Mempool-Größe: Sie können beobachten, wie die Größe des Mempool schwankt, was auf Zeiten mit hoher oder niedriger Aktivität im Netz hinweisen kann.



![graphs](assets/fr/19.webp)






- Die Entwicklung von Transaktionen und Transaktionsgebühren im gewählten Netzwerk: Indem Sie die Schwankungen bei den Transaktionen pro Sekunde verfolgen, können Sie Zeiten der Überlastung oder geringen Aktivität vorhersehen und Ihre Transaktionsgebühren optimieren. Diese Grafik gibt Ihnen einen Überblick über die Kapazität des Netzwerks, das Transaktionsvolumen zu bewältigen.



![graphs](assets/fr/20.webp)



Jetzt, wo Sie das Ende Ihrer Reise auf Mempool.space erreicht haben, können Sie Ihr eigener Entdecker werden und Ihre Transaktionen in Echtzeit verfolgen. Nachfolgend finden Sie unseren Artikel über den Bitcoin **Public Pool** Entdecker.



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1