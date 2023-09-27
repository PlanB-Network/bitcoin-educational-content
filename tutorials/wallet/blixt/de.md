---
name: Blixt

description: LN-Multifunktions-Wallet
---

![Präsentation](assets/1.jpeg)

# Blixt BTC ⚡️ LN Wallet/Node

## Ein leistungsstarker BTC/Lightning-Node in Ihrer Tasche, egal wo Sie sind

Ich möchte Ihnen einen interessanten und gleichzeitig leistungsstarken neuen BTC/LN-Node und mobilen Wallet vorstellen - Blixt. Der Name stammt aus dem Schwedischen und bedeutet "Blitz".

## Wie habe ich dieses kleine Juwel entdeckt?

Ich habe einen Umbrel LND-Node und wollte eine Backup-Lösung haben, um meinen Node im Falle eines SHTF1 schnell wiederherstellen zu können. Also habe ich dieses mobile Wallet gefunden, mit dem sich alle Node-Fonds aus SCB-Backups wiederherstellen lassen. Danach habe ich angefangen, es genauer zu testen und festgestellt, dass ES EIN VOLLSTÄNDIGER NODE IN IHRER EIGENEN TASCHE IST.

Vergessen Sie das nicht, denn das ist sehr wichtig!

> Am Ende dieses Artikels finden Sie einige einfache und schnelle Tutorials, wie Sie es verwenden und sich mit anderen Nodes verbinden können.

Es handelt sich um eine erstaunliche Anwendung für Android und iOS, mit der Sie einen BTC-LND-Node in Ihrer eigenen Tasche betreiben können. Unglaublich, oder? Auf Ihrem eigenen Telefon können Sie in weniger als 10 Minuten einen einsatzbereiten BTC LN-Node haben, mit umfangreichen Funktionen für erfahrene Benutzer, aber auch für neue Benutzer oder solche, die nicht so technikaffin sind, da die Verwendung einfach und nahtlos ist.

Blixt Wallet ist ein Open-Source-Projekt unter der MIT-Lizenz und konzentriert sich auf eine Nische von Benutzern, die mit BTC/LN beginnen möchten, aber nicht die Mittel haben, eine vollständige Maschine zu betreiben, oder einfach einen mobilen Node betreiben möchten.

Links

Hier sind einige Links zu dieser neuen Node/Wallet-App:

> Offizielle Website - mit einer charmanten interaktiven Demo

> GitHub-Repository: Überprüfen Sie den Entwicklungsstand und/oder laden Sie die Quellen herunter
>
> Telegram-Hilfegruppe - Hier können Sie dem Entwickler und der Community direkt Fragen stellen
>
> Download der Android-App Blixt
>
> Download der Testflight-App für iOS
>
> Twitter-Feed mit Demos

![Hauptbild](assets/2.JPEG)

# Hauptfunktionen verfügbar

## Neutrino-Node

Blixt verbindet sich standardmäßig mit dem Blixt-Server, um Blöcke und den Index mit Neutrino (SPV-Modus für vereinfachte Zahlungsverifikation) zu synchronisieren, aber der Benutzer kann sich auch mit seinem eigenen Node verbinden. Es ist erstaunlich, dass die Synchronisierung eines SPV-Nodes in meinem Fall auf Android 11 weniger als 5 Minuten dauert, um das volle Node-Wallet (On-Chain und LN) nutzen zu können.
**Vollständiger nicht verwahrter Knoten**

Der Benutzer kann seine eigenen Kanäle mit einer benutzerfreundlichen Oberfläche verwalten und ausreichend angezeigte Informationen für eine gute Erfahrung erhalten. Im linken oberen Schubladenmenü können Sie zu den Lightning-Kanälen gehen und mit anderen Knoten öffnen, wie Sie möchten. Vergessen Sie nicht, Tor in den Einstellungen zu aktivieren. Dies ist sowohl für die Privatsphäre als auch für den Fall, dass Sie als mobiler Knoten Ihre Internetverbindung / Clearnet-IP häufig ändern, besser, da Ihre Peers gestört werden können. Mit der Tor-Knoten-URI haben Sie immer dieselbe private Kennung, unabhängig von Ihrem Standort / Ihrer IP.

## LND-Knoten sichern / wiederherstellen

Eine leistungsstarke, einfach zu verwaltende und nützliche Funktion ist die Wiederherstellung anderer ausgefallener LND-Knoten mit nur der 24-Wörter-Samenliste und der Datei "channels.backup".

> Hier ist eine Anleitung, wie Sie ausgefallene Umbrel-Knoten in Blixt wiederherstellen können, falls es zu einer Notsituation kommt.

Der Benutzer hat auch die Möglichkeit, die Sicherung der Blixt-Kanäle in Google Drive und / oder im lokalen Speicher auf seinem eigenen Mobilgerät zu speichern (um sie später an einen sicheren Ort außerhalb des Telefons zu verschieben).

Der Wiederherstellungsprozess ist ziemlich einfach: Geben Sie den 24-Wörter-Samen ein, fügen Sie die Sicherungsdatei (zuvor in den Speicher des Mobilgeräts kopiert) hinzu und klicken Sie auf "Wiederherstellen". Es dauert eine Weile, um alle Blöcke für Ihre vergangenen Transaktionen zu synchronisieren und zu scannen. Die Kanäle werden automatisch geschlossen und die Mittel in Ihre Onchain-Brieftasche zurückgeführt (siehe das Schubladenmenü oben links - Onchain).

> Wenn Sie zuvor offene Kanäle mit Ihrem alten Knoten hinter Tor hatten, müssen Sie zuerst die Tor-Option aktivieren (und die Anwendung neu starten) in den Einstellungen des Menüs. Auf diese Weise schlägt der Schließvorgang nicht fehl und/oder die Option zum erzwungenen Schließen wird nicht verwendet.

Vergessen Sie nicht, Ihre LN-Kanäle nach dem Öffnen und/oder Schließen von Kanälen zu sichern. Es dauert nur wenige Sekunden, um sicher zu sein. Später können Sie die Sicherungsdatei an einen sicheren Ort außerhalb Ihres Mobilgeräts verschieben.
Um Ihre Saatgut in einem Wiederherstellungsszenario zu testen, bevor Sie Mittel hinzufügen, verwenden Sie einfach dasselbe 24-Wörter-Saatgut (aezeed) in BlueWallet. Wenn die generierte BTC-Adresse in Blixt dieselbe ist, sind Sie bereit. Sie müssen BlueWallet danach nicht mehr verwenden, Sie können die getestete Brieftasche einfach für die Wiederherstellung löschen.
Integriertes Tor
'Einmal aktiviert, startet die Anwendung hinter dem Tor-Netzwerk neu. Ab diesem Zeitpunkt können Sie in den Einstellungen des Menüs Ihre Knoten-ID mit einer Onion-Adresse sehen, so dass andere Knoten Kanäle zu Ihrem kleinen mobilen Blixt-Knoten öffnen können. Oder sagen wir, Sie haben Ihren eigenen Knoten zu Hause und möchten kleine Kanäle mit Ihrem mobilen Blixt-Knoten haben. Eine perfekte Kombination.

## Dunder LSP - Liquidity Service Provider oder Liquiditätsdienstleister

Eine einfache und fantastische Funktion, die es neuen Benutzern ermöglicht, sofort BTC im Lightning Network zu akzeptieren, ohne Gelder auf die On-Chain-Brieftasche einzuzahlen und dann LN-Kanäle zu öffnen.

Für neue Benutzer ist dies eine großartige Nachricht, da sie angeblich direkt im LN von Null anfangen können. Dazu müssen Sie lediglich eine LN-Rechnung (oder Rechnung) vom Hauptbildschirm aus über die Schaltfläche "Empfangen" erstellen, den Betrag, die Beschreibung usw. eingeben und von einer anderen Brieftasche aus bezahlen. Blixt öffnet einen Kanal von maximal 500k Sats pro empfangener Transaktion. Sie können bei Bedarf mehrere Kanäle öffnen.

Ein interessanter und nützlicher Fall ist folgender: Angenommen, der erste empfangene Betrag beträgt 200k. Blixt öffnet einen Kanal von 500k Sats und hat bereits 200k (abzüglich der Öffnungsgebühren) auf Ihrer Seite. Da Sie jedoch noch 300k "Platz" haben, können Sie weitere empfangen. Daher wird die nächste Zahlung, sagen wir 100k, direkt über diesen Kanal ohne zusätzliche Gebühren erfolgen und Sie haben immer noch 200k Platz für weitere Zahlungen.

Wenn Sie sich jedoch für die dritte Zahlung entscheiden und zum Beispiel 300k empfangen möchten, wird ein weiterer neuer Kanal von 500k erstellt und diese 300k werden auf Ihre Seite geschoben.

Wenn zu viele Anfragen vorliegen, kann der Blixt-Knoten die Kanalkapazität bei der Eröffnung ändern.

## Automatisches Öffnen von Kanälen

In den Einstellungen kann der Benutzer diese Option aktivieren und einen automatisierten Dienst haben, der Kanäle mit den besten Knoten und Routen aus dem verfügbaren Guthaben in der On-Chain-Brieftasche der Blixt-Anwendung öffnet. Dies ist eine vorteilhafte Funktion für neue Benutzer, die nicht wissen, mit welchem Knoten sie einen Kanal öffnen sollen und/oder wie sie einen LN-Kanal öffnen können. Es ist wie ein Autopilot für LN.

> Denken Sie daran: Diese Option wird nur einmal verwendet, wenn Sie Ihre neue Blixt-Brieftasche erstellen, und ist standardmäßig aktiviert. Wenn der neue Benutzer den On-Chain-QR-Code auf dem Hauptbildschirm scannt und seine ersten Sats an diese Adresse einzahlt, öffnet Blixt automatisch einen Kanal mit diesen Sats und dem öffentlichen Blixt-Knoten.

## Eingehende Liquiditätsdienste'

## Funktion für Händler, die mehr eingehende Liquidität benötigen, einfach zu bedienen. Dazu wählen Sie einfach einen der Liquiditätsanbieter aus der Liste aus, zahlen den gewünschten Betrag für den Kanal und geben die ID Ihres Knotens an. Von dort aus wird ein Kanal zu Ihrem Blixt-Knoten geöffnet.

## Kontaktlisten

Nützliche Funktion, wenn Sie eine dauerhafte Liste von Empfängern haben möchten, mit denen Sie die meiste Zeit handeln. Diese Liste kann aus LNURLs, Lightning-Adressen oder zukünftigen statischen Zahlungsinformationen/Rechnungen bestehen. Diese Liste kann derzeit nicht außerhalb der Anwendung gespeichert werden, aber es ist geplant, eine Exportoption zu haben.

## An Lightning-Adresse senden

Sie können an jede LN-Adresse senden, die nicht in Ihrer Kontaktliste steht. Möglicherweise gibt es bald eine Option, eine eigene LN-Adresse vom Typ @blixtwallet.com zu haben.

Unterstützung von LNURL

Sie können LNURL scannen/bezahlen/verbinden, aber derzeit funktioniert dies nicht, wenn LNURL hinter Tor liegt.

## Keysend

Eine sehr leistungsstarke Funktion, die nur wenige mobile Wallets haben. Sie können direkt über einen Kanal Geld senden/überweisen, indem Sie eine Nachricht hinzufügen, wenn nötig. Diese Funktion ist sehr nützlich, um Nachrichten auf dem Amboss.space-Anzeigetafel anzuzeigen (hier ist eine Anleitung zu dieser Amboss-Anzeigetafel).

## Nachrichten signieren

Sehr nützliches Werkzeug zum Signieren von Nachrichten mit Ihrem privaten Schlüssel des Blixt-Knotens, z. B. Authentifizierungsnachrichten und so weiter. Nur sehr wenige mobile Wallets verfügen über diese Funktion, praktisch keine.

## Multi-Kanal-Zahlungen - Multi-Path Payments (MPP)

Nützliche Funktion für LN-Zahlungen, die eine LN-Zahlung in mehrere Teile aufteilt, über mehrere Kanäle hinweg. Dies ist eine gute Möglichkeit, die Liquidität im Netzwerk auszugleichen und die Privatsphäre zu verbessern.

## Lightning-Browser

Eine Reihe von Drittanbieterdiensten mit LN, die in einem einfachen, zugänglichen und benutzerfreundlichen Browser organisiert sind. Dies ist auch eine gute Möglichkeit, Unternehmen zu fördern, die BTC auf LN akzeptieren. Dies ist eine Funktion, die in Zukunft weiterentwickelt wird. Derzeit funktioniert sie nicht hinter Tor, daher erfolgt das Surfen in diesen Anwendungen im Klartext (Clearnet).

## Log-Explorer

Ein leistungsstolles Tool zum Überprüfen der LND-Logs und des Zustands Ihres Knotens im Allgemeinen. Es gibt eine Option zum Speichern der Log-Datei. Es ist sehr nützlich, diese Logs zur Hand zu haben, falls Sie die Hilfe des Entwicklers benötigen, um bestimmte Probleme zu identifizieren.

## Sicherheit

Vous pouvez in den Anwendungseinstellungen die Möglichkeit einstellen, die Anwendung für eine höhere Sicherheit Ihrer Wallet/Node mit einer PIN und/oder Fingerabdruck zu starten.

## On-Chain Wallet

Diese Funktion ist etwas versteckt im linken oberen Menüschubfach. Da sie von einem LN-Benutzer nicht oft verwendet wird, ist sie nicht auf dem Hauptbildschirm sichtbar. Aber das ist nicht schlimm, Sie können es auf einer separaten Wallet haben, auf der Sie Adressen verwalten und das Transaktionsprotokoll anzeigen können, indem Sie beispielsweise Ihren Seed auf Sparrow importieren. Möglicherweise wird Blixt Wallet in Zukunft auch eine Funktion zum Verwalten von UTxO enthalten. Verwenden Sie jedoch NUR diese On-Chain Wallet, um LN-Kanäle zu öffnen oder zu schließen.

"Ostereier"

Ja, in der Blixt-App gibt es einige versteckte Funktionen, kleine Dinge, die die App liebenswert machen und lustige/interessante Aktionen und Antworten auslösen.
Hinweis: Versuchen Sie zweimal auf das Blixt-Logo im Schubfach zu klicken 🙂 Den Rest können Sie selbst entdecken.

# Mini-Leitfaden für typische Anwendungsfälle mit Blixt

A. Öffnen von Kanälen zu Ihrem Blixt-Mini-Node von Ihrem Umbrel-Node aus

## Für Android-Benutzer:

1. Gehen Sie zu den Blixt-Einstellungen - aktivieren Sie Tor - starten Sie die Anwendung neu (schließen Sie sie erzwungenermaßen, wenn sie nicht automatisch neu startet).

2. Warten Sie, bis Blixt hinter Tor geöffnet ist und die neuesten Blöcke synchronisiert.

3. Gehen Sie zu den Einstellungen - klicken Sie auf "Tor Onion Service anzeigen", kopieren Sie es, das ist die URI Ihres Blixt-Nodes.

4a. Gehen Sie zu Ihrer Umbrel RideTheLightning- oder ThunderHub-Anwendung (ich bevorzuge letztere) - fügen Sie einen Peer hinzu und fügen Sie die Onion-Adresse, die Blixt-URI, ein.

4b. Gehen Sie zum Dashboard Ihres Umbrel- oder RTL/TH-Nodes - öffnen Sie einen Kanal und wählen Sie einen bekannten Peer aus der Liste aus, indem Sie Ihre Blixt-Node-ID suchen.

5. Geben Sie die Satoshimenge für den Kanal ein und klicken Sie auf "Öffnen".

6. Warten Sie auf 3 Bestätigungen, um einen neuen Kanal mit Ihrem "Mini-Node" Blixt zu haben.

## Für iOS-Benutzer:

1. Gehen Sie zu den Blixt-Einstellungen - aktivieren Sie Tor - starten Sie die Anwendung neu.

2. Warten Sie, bis Blixt hinter Tor geöffnet ist und die neuesten Blöcke synchronisiert.

3. Gehen Sie zu Ihrem Umbrel-Node, kopieren Sie die Tor-URI oder zeigen Sie den QR-Code an.

4. In der Blixt Wallet gehen Sie zu Einstellungen - Lightning Peers anzeigen - Peer hinzufügen und scannen oder fügen Sie die URI Ihres Umbrel-Nodes ein. Es wird als bekannter Peer hinzugefügt.

5. Gehen Sie zurück zur Thunderhub-App von Umbrel, öffnen Sie das Kanalmenü und wählen Sie einen Peer aus der Dropdown-Liste der vorhandenen Peers aus.

6. Geben Sie alle anderen Details ein, um den Kanal zu öffnen, und klicken Sie auf "Öffnen".

7. Warten Sie auf 3 Bestätigungen, um diesen Kanal zu öffnen, und voilà, Sie haben jetzt mehr eingehende Liquidität auf Ihrer Blixt-Seite.

## B. Öffnen von Kanälen zu einem Umbrel-Knoten

Dieses Mal werden wir einen Kanal VON Ihrem Blixt-Knoten zu Ihrem eigenen Umbrel-Knoten (zum Beispiel) öffnen, um die Verbindung und die Verwendung von Tor zu testen. Später können Sie diesen Kanal ausgleichen, indem Sie die Hälfte oder den gewünschten Betrag auf die Umbrel-Seite schieben. Dies kann auch als "Entlastungsventil" verwendet werden, wenn Ihr Haupt-Umbrel-Knoten mehr Liquidität benötigt.

1. Gehen Sie zu Ihrem Umbrel-Knoten und kopieren Sie die URI Ihres Knotens oder zeigen Sie einfach den QR-Code für die Onion-Adresse an.

2. Gehen Sie zu Blixt - Einstellungen - Lightning-Peers - neuen Peer hinzufügen.

3. Scannen Sie den QR-Code Ihres Umbrel-Knotens oder fügen Sie die Onion-URI ein, und Ihr Umbrel-Knoten wird als Peer hinzugefügt.

4. Gehen Sie zurück zum Hauptbildschirm - oberer linker Schubladenbereich - Lightning-Kanäle.

5. Klicken Sie auf das "+"-Zeichen, um einen neuen Kanal zu öffnen, und fügen Sie die URI ein oder scannen Sie den QR-Code Ihres Umbrel-Knotens. Geben Sie die Anzahl der Sats für den Kanal, die Gebühren ein und klicken Sie auf "Öffnen".

6. Fertig! Der Kanal wird 3 Bestätigungen benötigen, um geöffnet zu werden, und ... Viel Spaß mit Lightning und Ihrem eigenen Umbrel-Knoten.

C. Direkter Empfang von Geldern in der LN-Wallet

Es ist eine einfache und angenehme Erfahrung, Gelder direkt in Ihre frisch eröffnete Blixt-Knoten-Wallet zu erhalten, ohne zuvor Geld einzahlen und manuell Kanäle mit bestimmten Knoten öffnen zu müssen.

1. Sobald Sie die Wallet erstellt und den Seed gesichert haben, gehen Sie zu den Einstellungen und aktivieren Sie die Dunder LSP-Funktion.

2. Gehen Sie zurück zum Hauptbildschirm - klicken Sie auf "Empfangen", geben Sie den Betrag ein (ich habe es mit 200k Sats getestet).

3. Es wird eine LN-Rechnung erstellt, die von einer anderen LN-Wallet bezahlt werden soll.

4. Der Dunder LSP-Service erstellt einen Kanal von maximal 500k Sats und schiebt die von Ihnen gesendeten Gelder (in unserem Fall 200k) auf die Seite Ihres Kanals. So haben Sie einen schönen Kanal zum Senden und Empfangen bereit.
5. Wenn Sie mehr erhalten möchten, werden zukünftige Zahlungen über denselben Kanal empfangen, bis das Maximum von 500k erreicht ist. Wenn es keinen "Platz" mehr gibt, um über denselben Kanal zu empfangen, wird Dunder LSP gemäß demselben Verfahren einen neuen Kanal erstellen.
6. Sichern Sie Ihre geöffneten neuen Kanäle. Immer nach dem Öffnen oder Schließen eines neuen Kanals durchführen. Es ist sehr einfach und schnell und kann viele Probleme vermeiden.

Dies ist ein perfektes Anwendungsszenario für neue kleine Händler, die mit dem Akzeptieren von BTC beginnen möchten.

Wichtige Hinweise

> Bevor Sie Ihre Kanäle hinter Tor verwenden und wenn die Blixt-App lange Zeit geschlossen/nicht synchronisiert war, warten Sie, bis das Synchronisationssymbol oben auf dem Bildschirm verschwindet, und stellen Sie sicher, dass alle Ihre Kanäle aktiv sind. Wenn alles in Ordnung ist, können Sie Ihre Transaktionen durchführen.
>
> Wenn die Kanäle immer noch nicht aktiv sind, fügen Sie die öffentlichen Schlüssel (URIs) Ihrer Peers erneut in den Blixt-Optionen - Show peers hinzu. Sie können auch versuchen, diese Liste zu aktualisieren, wenn das Gossip unter Tor Ihre Peers findet, werden die Kanäle wieder aktiviert. Wenn nicht, fügen Sie sie erneut hinzu, um den Gossip zur Kommunikation zu zwingen.
>
> Aber denken Sie daran: Führen Sie nicht sofort eine Transaktion aus, nachdem Sie die Blixt-App geöffnet haben. Es dauert einen Moment, um zu überprüfen, ob Ihre Kanäle aktiv sind, und es warnt Sie, wenn es einen Fehler in der Zahlungsroute oder einen Liquiditätsmangel auf der Route gibt.
>
> Das Öffnen von LN-Kanälen mit Blixt hat einen Preis, wie jeder andere LN-Knoten, der Kanäle öffnet. Dies hat einen Namen: "commit_fees" (oder Engagementgebühren), die wie eine Reserve zum Schließen der Kanäle dienen, um die Gebühren für die Miner bezahlen zu können. Seien Sie sich also bewusst, dass der Betrag, den Sie in Ihre Blixt-On-Chain-Wallet einzahlen und Kanäle öffnen (unabhängig davon, ob Sie den LSP Dunder verwenden, automatisches Öffnen der Kanäle oder manuelles Öffnen), geringfügig niedriger sein wird als der Gesamtbetrag, mit dem Sie den Kanal geöffnet haben. Aus diesem Grund wird NICHT EMPFOHLEN, sehr kleine Kanäle wie 20-50-100k Sats zu öffnen.
>
> Darüber hinaus fallen für jede LN-Transaktion geringe Netzwerkgebühren an. Dies sind keine Gebühren für Blixt, sondern Kosten, die Ihre Transaktionen durch das Netzwerk sicher und geschützt machen. Sie sind jedoch sehr gering, manchmal sogar in Milli-Sats, oft weniger als 0,5% des Transaktionsbetrags.
> '> Als LN-Knoten wird dringend davon abgeraten, dieselbe Seed auf zwei verschiedenen Geräten zu verwenden. Dieser Vorgang kann NUR durchgeführt werden, wenn Sie sich in einem Wiederherstellungsprozess befinden. Wenn die On-Chain-Wallet aus dem Seed generiert wird, beginnt sie mit der Synchronisierung der vorherigen Transaktionen und Salden. Wenn Sie keine LN.backup Ihrer Kanäle haben, wird der vollständige Wiederherstellungsprozess nicht gestartet. Ja, Sie werden dieselbe On-Chain-Wallet auf beiden Geräten sehen, aber NICHT den LN-Saldo. Und vor allem VERSUCHEN SIE NICHT, dieselben LN-Kanäle auf beiden Geräten wiederherzustellen, da Sie sonst alle Ihre LN-Fonds verlieren würden!>
> Beachten Sie, dass das Schließen von Kanälen Zeit in Anspruch nimmt, bis die Mittel freigegeben werden. So funktioniert LN (um mehr zu erfahren, gehen Sie hierhin). Im Allgemeinen dauert es bei einer kooperativen (normalen) Schließung mindestens 40 Blöcke, bis die Mittel in Ihrer On-Chain-Wallet freigegeben werden. Bei erzwungen geschlossenen Kanälen beträgt dieser Sperrzeitraum manchmal 144 Blöcke oder mehr. Seien Sie also geduldig und machen Sie sich keine Sorgen, die Mittel sind sicher.

## Fazit

Nun, das sind einige der Hauptfunktionen (für eine mobile Wallet ist das viel, oder?) und es werden bald noch mehr hinzukommen.

Die Erfahrung mit dieser LN-Wallet/Node-App ist sehr angenehm und benutzerfreundlich, eine sehr reaktionsfähige App, keine größeren Probleme, nur kleine Dinge, die hinzugefügt werden müssen (aber nicht so wichtig). Es handelt sich immer noch um eine junge App, die unter realen Bedingungen umfangreich getestet werden muss. Also zögern Sie nicht, sie auszuprobieren und dem Entwickler etwaige Probleme mitzuteilen, die behoben oder verbessert werden können.

Vergessen Sie auch nicht, dass es sich um ein Open-Source-Projekt handelt und die Wartung von einem einzigen Entwickler durchgeführt wird, der die gesamte Arbeit leistet! Bitte helfen Sie ihm mit Tests und Feedback und vor allem melden Sie ihm detailliert Probleme oder Verbesserungsvorschläge, die die App benötigt.

Ich hoffe, Sie werden die Verwendung genießen. Persönlich liebe ich sie und sie ist sehr nützlich für mich (hier ist ein Anwendungsfall, in dem diese Wallet ein großartiges Werkzeug ist).

Möge ₿ITCOIN mit dir sein!
