---
name: Breez Point of Sales

description: Anleitung zum Starten der Bitcoin-Akzeptanz mit Breez POS
---

![cover](assets/cover.jpeg)

# Breez Point of Sales

_Dieser Text stammt von der Breez-Dokumentationswebsite: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_

## Was ist Breez POS?

**Breez** ist eine umfassende, nicht verwahrende Lightning-App. Lassen Sie uns das genauer betrachten:

- **Lightning** ist ein Bitcoin-Zahlungsnetzwerk, das die Transaktionszeiten von Minuten auf Millisekunden und die Transaktionsgebühren von mehreren Dollar auf wenige Cent reduziert. Lightning verwandelt Bitcoin von digitalem Gold in digitale Währung und bewahrt dabei alle Vorteile, die Bitcoin großartig machen.
- **Nicht verwahrend** bedeutet, dass Breez nicht im Besitz des Geldes der Benutzer ist. Viele Lightning-Apps nehmen das Geld ihrer Benutzer in Besitz. Sie sind im Grunde genommen Bitcoin-Banken. Mit einer nicht verwahrenden App wie Breez sind alle Benutzer ihre eigenen Banken.
- **Umfassend** bedeutet, dass Breez fast alle technischen Vorgänge automatisch und im Hintergrund erledigt. Dinge wie Kanalerstellung, eingehende Liquidität und Routing bleiben unter der Haube. (Aber Breez ist auch Open Source, sodass Interessierte die Technologie überprüfen können!)

**Breez POS** steht für unseren Kassenmodus. Mit anderen Worten, Breez funktioniert wie eine digitale Registrierkasse für Unternehmen und Händler, die Lightning-Zahlungen akzeptieren möchten (zusätzlich zu seinem "Standard"-Modus, der wie die digitale Version eines Lederportemonnaies für Bitcoin und einem Podcast-Player der nächsten Generation ist). Schauen wir uns nun an, wie Sie Breez als Lightning-Kasse für Ihr Unternehmen einrichten können.

## Wie starten Sie mit Breez?

1. Der erste Schritt besteht darin, die App herunterzuladen. Sie ist für Android und iOS verfügbar (installieren Sie TestFlight und klicken Sie auf den Link von Ihrem Gerät).
2. Breez kann sich automatisch auf Google Drive, iCloud oder jedem WebDav-Server sichern.
   > Beachten Sie, dass jedes Gerät seinen eigenen Lightning-Knoten ausführt. Sie können den POS-Modus auf beliebig vielen Geräten ausführen, aber die Guthaben bleiben getrennt.
3. Öffnen Sie die App und klicken Sie auf das Symbol oben links, um den Point-of-Sale-Modus zu finden.

## Einrichten des POS

1. Klicken Sie auf das Symbol oben links und dann auf Point of Sale > POS-Einstellungen.

### Das Manager-Passwort

In den POS-Einstellungen haben Sie die Möglichkeit, ein Manager-Passwort zu erstellen. Das Manager-Passwort verhindert, dass ausgehende Zahlungen von der Breez-App ohne Autorisierung gesendet werden können. Das Verkaufspersonal kann nur Zahlungen vom Gerät erhalten. Beachten Sie, dass Sie bei Verwendung dieser Option möglicherweise auch den Zugriff auf das Backup von Breez verhindern möchten. Daher wird die Verwendung eines externen WebDav-Kontos (z. B. Nextcloud) für diesen Anwendungsfall empfohlen.

### Die Artikel-Liste

Die Artikel-Liste ist ein Katalog von zum Verkauf stehenden Artikeln und deren Preisen. Es gibt zwei Möglichkeiten, Artikel zur Liste hinzuzufügen:

- Um Artikel einzeln einzugeben, klicken Sie auf "Artikel" oben in der Hauptansicht des POS und dann auf das "+"-Symbol unten rechts. Hier können Sie den Namen eines einzelnen Artikels, den Preis (angezeigt in der Währung Ihrer Wahl) und die SKU (eine eindeutige interne Kennung für diesen Artikeltyp; optional) eingeben.
- Um mehrere Artikel auf einmal einzugeben, klicken Sie auf das Taschenrechner-Symbol oben links, dann auf Point of Sale > Einstellungen > POS-Einstellungen und klicken Sie dann auf die drei Punkte rechts neben der Artikelliste und anschließend auf Importieren aus CSV. Dadurch können Sie eine CSV-Datei importieren, die Sie im Voraus vorbereitet haben und die die Namen, Preise und SKUs Ihrer Artikel enthält.

### Fiat-Anzeige

Breez sendet und empfängt nur Bitcoin und für die meisten Transaktionen auf Lightning, die in der Regel kleinere Beträge sind, wird die Summe normalerweise in Satoshis angezeigt, auch bekannt als Sats (1 BTC = 100.000.000 Sats). Viele Händler finden es jedoch praktisch, den Wert des Kaufs in der lokalen Fiat-Währung anzeigen zu können (und Kunden mitzuteilen).

In der Hauptansicht des POS ist die aktuell angezeigte Währung auf der rechten Seite sichtbar (Standard ist SAT). Es gibt auch eine Dropdown-Liste mit anderen verfügbaren Währungen zur Anzeige. Um Währungen zu dieser Dropdown-Liste hinzuzufügen oder zu entfernen, klicken Sie auf Point of Sale > Einstellungen > Fiat-Währungen. Überprüfen Sie dann einfach die Währungen, die Sie in Ihrem Dropdown-Menü haben möchten, und deaktivieren Sie diejenigen, die Sie nicht anzeigen möchten.

Die angezeigten Werte stammen von yadio, einer angesehenen Quelle für Wechselkursdaten, und sie werden in nahezu Echtzeit aktualisiert. Aber denken Sie daran: Der tatsächliche Zahlungsvorgang erfolgt immer in Bitcoin, unabhängig von der angezeigten Währung.

### Bestellung aufladen

Um die Bestellung zusammenzustellen, fügen Sie entweder Artikel aus der Artikelliste hinzu oder geben Sie einfach einen Betrag über die Tastatur ein. Klicken Sie dann oben in der Hauptansicht des POS auf "Aufladen". Sie sehen dann einen QR-Code, den der Kunde mit seiner Lightning-App scannen kann, den Sie direkt von einer anderen App auf Ihrem Gerät teilen können oder den Sie bei Bedarf kopieren und einfügen können.

Beim Scannen dieses Codes oder beim Klicken auf die geteilte/eingefügte Rechnung sieht der Kunde die Rechnung in seiner Lightning-App und hat die Möglichkeit, sie sofort zu bezahlen und die Transaktion abzuschließen.

Sobald Sie in der Breez-App auf dem Gerät des Händlers die Animation "Zahlung genehmigt!" sehen, können Sie auf das Druckersymbol klicken, um einen Beleg für den Kunden zu erstellen. Um einen Belegdrucker in Android zu verwenden, versuchen Sie es mit diesem Treiber. Beachten Sie, dass Sie auch vergangene Transaktionen über den Transaktionsbildschirm drucken können.

### Verkaufsbericht

Um einen täglichen/wöchentlichen/monatlichen Bericht über Ihre Verkäufe (für Buchhaltungszwecke oder andere) anzuzeigen, klicken Sie auf das Symbol oben links und dann auf Transaktionen. Klicken Sie auf das Berichtssymbol, um den Bericht anzuzeigen, und auf das Kalendersymbol, um den ausgewählten Datumsbereich zu ändern.

### Exportieren von Transaktionen

Um eine Liste der in Breez erhaltenen Zahlungen anzuzeigen, klicken Sie auf das Symbol oben links und dann auf Transaktionen. Klicken Sie auf die drei Punkte oben rechts und dann auf Exportieren, um eine Liste der eingehenden Zahlungen im CSV-Format zu exportieren. Um die Liste auf einen bestimmten Zeitraum zu beschränken, klicken Sie auf das Kalendersymbol, um einen Datumsbereich festzulegen.

### Belege drucken

Um einen Verkaufsbeleg zu drucken, klicken Sie auf das Drucksymbol oben rechts im Zahlungsbestätigungsfenster. Alternativ klicken Sie auf das Symbol oben links und dann auf Transaktionen. Suchen Sie den zu druckenden Verkauf, öffnen Sie ihn und klicken Sie auf das Drucksymbol oben rechts.

> Hinweis: Verwenden Sie diesen Treiber, um auf einem tragbaren 58mm/80mm Bluetooth/USB-Thermodrucker zu drucken.

## Ich möchte mehr erfahren

- Für weitere Informationen zu Lightning und Breez besuchen Sie unseren [Blog](https://breez.technology/blog).
- Für weitere technische Tipps, wie Sie das Beste aus der App herausholen und gängige Operationen durchführen können, werfen Sie einen Blick in unsere [Dokumentation](https://breez.technology/documentation).
- Wenn Sie steckenbleiben und die Antwort in keiner unserer Hilfsliteraturen finden können, finden Sie uns auf [Telegram](https://t.me/breez_labs) oder senden Sie uns eine [E-Mail](mailto:support@breez.technology).
- Wenn Sie einige Demonstrationsvideos des Breez POS-Modus in Aktion sehen möchten, hier ist ein großartiges kurzes Video [hier](https://www.youtube.com/watch?v=xxxx) und hier ist ein längeres, detaillierteres Video [hier](https://www.youtube.com/watch?v=xxxx).
