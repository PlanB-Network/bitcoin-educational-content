---
name: Robosats

description: Anleitung zur Verwendung von Robosats
---

![cover](assets/cover.jpeg)

# Robosats

RoboSats (https://learn.robosats.com/) ist eine einfache Möglichkeit, Bitcoin gegen nationale Währungen privat auszutauschen. Es vereinfacht das Peer-to-Peer-Erlebnis und verwendet Lightning-Hold-Rechnungen, um die Verwahrung und Vertrauensanforderungen zu minimieren.

![video](https://youtu.be/XW_wzRz_BDI)

## Anleitung

> Diese Anleitung stammt von Bitcoin Q&A (https://bitcoiner.guide/robosats/). Alle Credits gehen an ihn, unterstützen Sie ihn dort (https://bitcoiner.guide/contribute); BitcoinQ&A ist auch ein Bitcoin-Mentor. Kontaktieren Sie ihn für Mentoring!

![image](assets/0.png)

RoboSats - Ein einfacher und privater Lightning-basierter P2P-Austausch

## Bevor Sie beginnen

### Dinge, die Sie wissen müssen

| Jargon         | Definition                                                                                                                                                                                                                                   |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Roboter        | Ihre automatisch generierte private Handelsidentität. Verwenden Sie denselben Roboter nicht mehr als einmal, da dies Ihre Privatsphäre beeinträchtigen kann.                                                                                 |
| Token          | Eine Zeichenfolge zufälliger Zeichen, die verwendet wird, um Ihren einzigartigen Roboter zu generieren.                                                                                                                                      |
| Maker          | Ein Benutzer, der ein Angebot zum Kauf oder Verkauf von Bitcoin erstellt.                                                                                                                                                                    |
| Taker          | Ein Benutzer, der das Angebot eines anderen Benutzers zum Kauf oder Verkauf von Bitcoin annimmt.                                                                                                                                             |
| Bond           | Eine Menge an Bitcoin, die von beiden Parteien als Versprechen, fair zu spielen und ihren Teil des Handels abzuschließen, gesperrt wird. Bonds betragen in der Regel 3% des Gesamthandelsbetrags und werden von Hodl-Rechnungen unterstützt. |
| Handels-Escrow | Vom Verkäufer verwendet, um den Handelsbetrag in Bitcoin zu halten, wiederum unter Verwendung von Hodl-Rechnungen.                                                                                                                           |
| Gebühren       | RoboSats berechnet 0,2% des Handelsbetrags, der zwischen Maker und Taker aufgeteilt wird. Der Taker zahlt 0,175% und der Maker zahlt 0,025%.                                                                                                 |

## Dinge, die Sie haben müssen

### Eine Lightning Wallet

RoboSats ist Lightning-nativ, daher benötigen Sie eine Lightning Wallet, um den Bond zu finanzieren und die gekauften Sats als Käufer zu erhalten. Sie sollten bei der Auswahl Ihrer Wallet vorsichtig sein, da nicht alle mit der Technologie, die RoboSats verwendet, kompatibel sind.

Wenn Sie einen eigenen Node betreiben, ist Zeus mit Abstand die beste Option. Wenn Sie keinen eigenen Node haben, empfehle ich Phoenix, eine plattformübergreifende mobile Wallet mit einfacher Einrichtung und Zugang zu Lightning. Phoenix wurde bei der Erstellung dieser Anleitung verwendet.

### Einige Bitcoin

Käufer und Verkäufer müssen vor jedem Handel einen Bond finanzieren. Dies ist in der Regel ein sehr geringer Betrag (~3% des Handelsbetrags), ist aber dennoch eine Voraussetzung.

Verwenden Sie RoboSats, um Ihre ersten Sats zu kaufen? Warum lassen Sie sich nicht von einem Freund den winzigen Betrag leihen, der zum Starten erforderlich ist!? Wenn Sie alleine unterwegs sind, gibt es hier einige andere großartige Möglichkeiten, um einige noKYC-Sats zu erhalten, um loszulegen.

### Zugang zu RoboSats

Natürlich müssen Sie Zugang zu RoboSats haben! Es gibt vier Hauptwege, dies zu tun:

1. Über den Tor-Browser (empfohlen!)
2. Über einen regulären Webbrowser (nicht empfohlen!)
3. Über die Android APK
4. Ihr eigener Client

Wenn Sie neu beim Tor-Browser sind, erfahren Sie mehr und laden Sie ihn [hier](https://www.torproject.org/download/) herunter.
Eine kurze Notiz für iOS-Benutzer, die über ihre Telefone auf RoboSats über Tor zugreifen möchten. 'Onion Browser' ist nicht der Tor-Browser. Verwenden Sie stattdessen Orbot + Safari und Orbot + DuckDuckGo.

## Bitcoin kaufen

Die folgenden Schritte wurden im Mai 2023 mit Version 0.5.0 durchgeführt und über den Tor-Browser aufgerufen. Die Schritte sollten für Benutzer, die über die Android APK auf RoboSats zugreifen, identisch sein.

Zum Zeitpunkt des Schreibens befindet sich RoboSats noch in der aktiven Entwicklung, daher kann sich die Benutzeroberfläche in Zukunft etwas ändern, aber die grundlegenden Schritte, um den Handel abzuschließen, sollten weitgehend unverändert bleiben.

> Wenn Sie RoboSats zum ersten Mal laden, gelangen Sie zu dieser Startseite. Klicken Sie auf Start.

![image](assets/2.png)

Generieren Sie Ihren Token und speichern Sie ihn an einem sicheren Ort, z. B. in einer verschlüsselten Notiz-App oder einem Passwort-Manager. Dieser Token kann verwendet werden, um Ihre vorübergehende Roboter-ID wiederherzustellen, falls Ihr Browser oder Ihre App während eines Handels geschlossen wird.

![image](assets/3.png)

Begrüßen Sie Ihre neue Roboteridentität und klicken Sie dann auf Weiter.

![image](assets/4.png)

Klicken Sie auf Angebote, um das Orderbuch zu durchsuchen. Oben auf der Seite können Sie dann nach Ihren Vorlieben filtern. Beachten Sie unbedingt die Bond-Prozentsätze und den Aufschlag auf den durchschnittlichen Wechselkurs.

- Wählen Sie Kaufen
- Wählen Sie Ihre Währung
- Wählen Sie Ihre Zahlungsmethode(n)

![image](assets/5.png)

> Klicken Sie auf das Angebot, das Sie annehmen möchten. Geben Sie den Betrag (in Ihrer gewählten Fiat-Währung) ein, den Sie vom Verkäufer kaufen möchten, überprüfen Sie abschließend die Details und klicken Sie auf Bestellung aufgeben.

Wenn der Verkäufer nicht online ist (erkennbar an einem roten Punkt auf seinem Profilbild), erhalten Sie eine Warnung, dass der Handel länger als üblich dauern könnte. Wenn Sie fortfahren und der Verkäufer nicht rechtzeitig vorgeht, erhalten Sie 50% des Bond-Betrags als Entschädigung für Ihre verschwendete Zeit.

![image](assets/6.png)

Als nächstes müssen Sie Ihre Handelsbindung durch Zahlung der Rechnung auf dem Bildschirm sperren. Dies ist eine Reservierungsrechnung, die in Ihrer Brieftasche eingefroren wird. Sie wird nur berechnet, wenn Sie Ihre Seite des Handels nicht abschließen.

![image](assets/7.png)

Scannen Sie im Lightning Wallet den QR-Code und zahlen Sie die Rechnung.

![image](assets/8.png)

Generieren Sie anschließend in Ihrem Lightning Wallet eine Rechnung für den angezeigten Betrag und fügen Sie sie in das vorgesehene Feld ein.

![image](assets/9.png)

Warten Sie, bis der Verkäufer seinen Handelsbetrag sperrt. Wenn dies geschieht, wechselt RoboSats automatisch zum nächsten Schritt, bei dem das Chat-Fenster geöffnet wird. Sagen Sie Hallo und fragen Sie den Verkäufer nach seinen Fiat-Zahlungsinformationen. Sobald diese bereitgestellt wurden, senden Sie die Zahlung über die gewählte Methode und bestätigen Sie dies in RoboSats. Alle Chats in RoboSats sind PGP-verschlüsselt, was bedeutet, dass nur Sie und Ihr Handelspartner die Nachrichten lesen können.

![image](assets/10.png)

Sobald der Verkäufer den Zahlungseingang bestätigt, gibt RoboSats automatisch die Zahlung frei, indem die zuvor bereitgestellte Rechnung verwendet wird.

![image](assets/11.png)

Wenn die Rechnung bezahlt ist, ist der Handel abgeschlossen und Ihre Bindung wird aufgehoben. Sie sehen dann eine Handelszusammenfassung.

![image](assets/12.png)

Überprüfen Sie Ihr Lightning Wallet, um zu bestätigen, dass die Sats angekommen sind.

![image](assets/13.png)

## Zusätzliche Funktionen

Neben dem offensichtlichen Kauf und Verkauf von Bitcoin hat RoboSats noch einige andere Funktionen, die Sie kennen sollten.

Robot Garage
Möchten Sie mehrere Trades gleichzeitig haben, aber nicht dieselbe Identität teilen? Kein Problem! Klicken Sie auf die Registerkarte "Roboter", generieren Sie einen zusätzlichen Roboter und erstellen oder nehmen Sie Ihre nächste Bestellung entgegen.

![image](assets/14.png)

### Bestellungen erstellen

Neben dem Annehmen eines Angebots von jemand anderem können Sie auch Ihr eigenes erstellen und auf einen anderen Roboter warten.

- Öffnen Sie die Seite "Erstellen".
- Geben Sie an, ob Ihre Bestellung Bitcoin kaufen oder verkaufen soll.
- Geben Sie den Betrag und die Währung ein, mit der Sie kaufen/verkaufen möchten.
- Geben Sie die Zahlungsmethode(n) ein, die Sie verwenden möchten.
- Geben Sie den Prozentsatz des "Premiums über dem Marktpreis" ein, den Sie akzeptieren möchten. Beachten Sie, dass dies auch eine negative Zahl sein kann, um einen Rabatt gegenüber dem aktuellen Marktpreis anzubieten.
- Klicken Sie auf "Bestellung erstellen".
- Bezahlen Sie die Lightning-Rechnung, um Ihre Maker-Bond zu sperren.
- Ihre Bestellung ist jetzt aktiv. Lehnen Sie sich zurück und warten Sie, bis jemand sie annimmt.

![image](assets/15.png)

### On-Chain-Auszahlungen

RoboSats konzentriert sich auf Lightning, aber Käufer haben die Möglichkeit, ihre Sats an eine On-Chain-Bitcoin-Adresse zu erhalten. Käufer können diese Option auswählen, nachdem sie ihre Bond gesperrt haben. Nach der Auswahl von On-Chain erhält der Käufer eine Übersicht über die Gebühren. Die zusätzlichen Gebühren für diesen Service umfassen:

- Eine Swap-Gebühr, die von RoboSats erhoben wird - Diese Gebühr ist dynamisch und variiert je nach Auslastung des Bitcoin-Netzwerks.
- Eine Mining-Gebühr für die Auszahlungstransaktion - Diese kann vom Käufer konfiguriert werden.

![image](assets/16.png)

### P2P-Swaps

RoboSats ermöglicht es Benutzern, Sats in ihre Lightning Wallet zu tauschen oder auszutauschen. Klicken Sie einfach auf die Schaltfläche "Swap" oben auf der Angebotsseite, um die aktuellen Swap-Angebote anzuzeigen.

Als Käufer eines "Swap In"-Angebots senden Sie On-Chain-Bitcoin an den Peer und erhalten Sats zurück, abzüglich der beworbenen Gebühren und/oder Aufschläge, in Ihre Lightning Wallet. Als Käufer eines "Swap Out"-Angebots senden Sie Sats über Lightning und erhalten Bitcoin, abzüglich eventueller Gebühren und/oder Aufschläge, an Ihre On-Chain-Adresse. Benutzer von Samourai oder Sparrow Wallet können auch die Stowaway-Funktion nutzen, um einen Swap abzuschließen.

RoboSats-Swap-Angebote können auch alternative Bitcoin-Pegelungen wie RBTC, LBTC und WBTC umfassen. Wenn Sie mit diesen Token interagieren, sollten Sie äußerst vorsichtig sein, da sie alle verschiedene Kompromisse mit sich bringen. Gepflegter Bitcoin ist nicht Bitcoin!

![image](assets/17.png)

### Führen Sie Ihren eigenen RoboSats-Client aus

Umbrel-, Citadel- und Start9-Node-Betreiber können ihren eigenen RoboSats-Client direkt auf ihrem Node installieren. Die Vorteile dabei sind:

- Dramatisch schnellere Ladezeiten.
- Sicherer: Sie kontrollieren, welche RoboSats-Client-App Sie ausführen.
- Greifen Sie sicher von jedem Browser/Gerät auf RoboSats zu. Wenn Sie sich in Ihrem lokalen Netzwerk befinden oder VPN verwenden, müssen Sie TOR nicht verwenden: Ihr Node-Backend übernimmt die Torifizierung, die für die Anonymisierung erforderlich ist.
- Ermöglicht die Kontrolle darüber, mit welchem P2P-Marktkoordinator Sie sich verbinden (Standardmäßig robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)

![image](assets/18.png)

## FAQ

### Kann ich betrogen werden?

Als Käufer können Sie im Falle, dass Sie das für Ihren Teil des Handels erforderliche Fiat-Geld gesendet haben, der Verkäufer jedoch die Sats nicht freigibt, einen Streit eröffnen. Wenn Sie während dieses Streitprozesses den RoboSats-Schiedsrichtern nachweisen können, dass Sie das Fiat-Geld gesendet haben, werden die hinterlegten Gelder des Verkäufers und ihre Handelsbindung an Sie freigegeben. Wie kann ich einen Handel stornieren?

Sie können einen Handel stornieren, nachdem Sie Ihre Bindung hinterlegt haben, indem Sie auf die Schaltfläche "Gemeinsame Stornierung" im Handelsmenü klicken. Wenn Ihr Handelspartner mit der Stornierung einverstanden ist, fallen keine Gebühren an. Wenn Ihr Handelspartner jedoch den Handel abschließen möchte und Sie trotzdem stornieren, verlieren Sie Ihre Handelsbindung.

### Arbeitet RoboSats mit der Zahlungsmethode 'X'?

Es gibt keine Einschränkungen bei den Zahlungsmethoden in RoboSats. Wenn Sie keine Angebote in Ihrer gewünschten Methode sehen, erstellen Sie Ihr eigenes Angebot damit!

![image](assets/19.png)

### Was erfährt RoboSats über mich, wenn ich es benutze?

Wenn Sie RoboSats über Tor oder die Android-App verwenden, erfährt es überhaupt nichts! Erfahren Sie hier mehr.

- Tor schützt Ihre Netzwerk-Privatsphäre.
- PGP-Verschlüsselung hält Ihren Handelschat privat.
- Keine Konten bedeuten einen Roboter pro Handel. Das bedeutet, dass RoboSats mehrere Trades nicht einer einzigen Entität zuordnen kann.

Es gibt jedoch einige Einschränkungen! Lightning ist als Sender ziemlich privat, aber nicht als Empfänger. Wenn Sie an Ihren eigenen Lightning-Knoten empfangen, wird Ihre Knoten-ID in Ihren Rechnungen geteilt. Diese Knoten-ID gibt jedem, der davon Kenntnis hat, einen Ausgangspunkt, um Ihre On-Chain-Aktivitäten zu verknüpfen. Dies gilt auch, wenn ein Benutzer seinen Handel über eine On-Chain-Auszahlung erhalten möchte.

Um dies zu mildern, können Benutzer eine Lösung wie eine Proxy Wallet für Lightning oder Coinjoin für On-Chain verwenden.

### Föderation

Derzeit gibt es einen einzigen RoboSats-Koordinator, der vom RoboSats-Entwicklerteam betrieben wird. Im Bitcoin-Netzwerk macht jede Form der Zentralisierung einen einfacheren Angriffspunkt für Regierungen oder Regulierungsbehörden dar, die möglicherweise nicht wohlwollend auf einen bestimmten Dienst schauen.

Da RoboSats ein Open-Source-Projekt ist, könnte jeder den Code nehmen und seinen eigenen Koordinator betreiben. Obwohl dies das Risiko von einem einzelnen Ziel etwas dezentralisiert, fragmentiert es auch einen bereits dünnen Liquiditätsmarkt.

Das RoboSats-Team ist sich dessen bewusst und arbeitet an einem föderierten Modell. Als Endbenutzer sollte sich der Handelsfluss, wie oben gezeigt, dadurch nicht wesentlich ändern, es wird jedoch zusätzliche Ansichten oder Bildschirme geben, um verschiedene Koordinatoren hinzuzufügen oder zu entfernen, die entstehen.

ENDE des Leitfadens
https://bitcoiner.guide/robosats/
