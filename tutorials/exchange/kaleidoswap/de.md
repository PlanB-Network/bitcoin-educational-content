---
name: KaleidoSwap
description: Fortgeschrittener Leitfaden für den RGB-Asset-Handel auf Lightning Network mit KaleidoSwap
---

![cover](assets/cover.webp)


KaleidoSwap ist eine anspruchsvolle Open-Source-Desktop-Anwendung, die die Lücke zwischen dem RGB-Protokoll und Lightning Network schließt. Sie dient als umfassende Schnittstelle für die Verwaltung von RGB-Lightning-Knoten, die Interaktion mit RGB-Lightning-Service-Providern (LSPs) über die LSPS1-Spezifikation und die Durchführung von atomaren Swaps von RGB-Assets.


Als nicht-verwahrende Lösung gibt KaleidoSwap den Nutzern die Möglichkeit, die volle Kontrolle über ihre Schlüssel und Daten zu behalten. Durch die Nutzung des Client-seitigen Validierungsparadigmas von RGB ermöglicht es private und skalierbare Smart Contracts auf der Grundlage von Bitcoin. Dieses Tutorial taucht in die fortgeschrittenen Funktionen von KaleidoSwap ein und führt Sie durch die Feinheiten der "farbigen" UTXO-Verwaltung, der Channel-Liquidität für bestimmte Vermögenswerte und des Taker-Maker-Handelsmodells, um sicherzustellen, dass Sie dieses leistungsstarke dezentrale Austauschprotokoll vollständig nutzen können.


## Einrichtung


KaleidoSwap bietet vorgefertigte Binärdateien für die wichtigsten Betriebssysteme, aber für fortgeschrittene Benutzer stellt die Erstellung aus dem Quellcode sicher, dass Sie den neuesten Code mit Ihren spezifischen Konfigurationen verwenden.


### Binärdateien herunterladen


Sie können die neueste Version für Ihr Betriebssystem von der [offiziellen Website](https://kaleidoswap.com/) oder der [GitHub-Releases-Seite](https://github.com/kaleidoswap/desktop-app/releases) herunterladen.


### Installationsmethoden


1.  **Windows**: Laden Sie das Installationsprogramm `.exe` herunter und führen Sie es aus.

2.  **macOS**: Laden Sie die `.dmg`-Datei herunter, öffnen Sie sie und ziehen Sie KaleidoSwap in Ihren Anwendungsordner.

3.  **Linux**: Laden Sie die `.AppImage` oder `.deb` Datei herunter und installieren/führen Sie sie aus.



## Optionen für die Knoteneinrichtung


Wenn Sie KaleidoSwap zum ersten Mal starten, wird Ihnen der **Verbindungsbildschirm** angezeigt. Dies ist der erste Schritt zur Konfiguration Ihrer Umgebung.


![Node Selection Screen](assets/en/01.webp)


Sie müssen wählen, wie Sie sich mit dem RGB Lightning Network verbinden. Diese Wahl wirkt sich auf Ihr Maß an Kontrolle und Privatsphäre aus.


### Option 1: Lokaler Knoten (empfohlen für Selbstverwahrung)


**Für vollständige Kontrolle und Privatsphäre** führen Sie einen Knoten direkt auf Ihrem Rechner aus, siehe die Vorteile unten:


- Selbstbestimmtes Leben**: Sie haben die Schlüssel in der Hand. Keine dritte Partei kann Ihr Geld einfrieren oder Ihre Transaktionen zensieren.
- Datenschutz**: Ihre Daten bleiben auf Ihrem Gerät.
- Unabhängigkeit**: Keine Abhängigkeit von externen Dienstleistern.


Wenn Sie **Lokaler Knoten** wählen, gelangen Sie zum Einrichtungsbildschirm, wo Sie einen neuen wallet erstellen oder einen bestehenden wiederherstellen können.


![Local Node Setup Screen](assets/en/02.webp)


### Option 2: Entfernter Knotenpunkt


Verbinden Sie sich mit einem entfernten RGB Lightning Node (selbst gehostet auf einem VPS oder bei einem gehosteten Anbieter).


- Vorteile**: Kein lokaler Ressourcenverbrauch, 24/7 Verfügbarkeit.
- Nachteil**: Erfordert Vertrauen in den Host oder die Verwaltung eines entfernten Servers.


![Remote Node Setup Screen](assets/en/03.webp)


**Wir empfehlen dringend, einen eigenen Knoten zu betreiben - entweder lokal (Option 1) oder durch Selbsthosten eines entfernten Knotens -, um die zensurresistenten Eigenschaften von Bitcoin und RGB vollständig zu nutzen.


## Erstellen eines Wallet


KaleidoSwap verwaltet sowohl Bitcoin- als auch RGB-Guthaben. Der wallet-Erstellungsprozess initialisiert einen Schlüsselspeicher, der Ihre on-chain-Gelder und Ihre Lightning-Channel-Status sichert.


Hier ist der genaue Ablauf:

1. Öffnen Sie KaleidoSwap und wählen Sie **Lokaler Knoten**.

2. Klicken Sie auf **Neue Wallet erstellen**.

3. **Konto einrichten**: Geben Sie einen **Kontonamen** ein und wählen Sie das **Netzwerk** (z. B. Bitcoin Mainnet, Testnet, Signet).

4. **Erweiterte Konfiguration** (optional): Wenn Sie ein Power-User sind, können Sie benutzerdefinierte RPC-Endpunkte, Indexer-URLs oder Proxy-Einstellungen unter "Erweiterte Einstellungen" konfigurieren.

5. Klicken Sie auf **Fortfahren**.

6. **Passwort**: Legen Sie ein starkes Passwort fest, um Ihre wallet-Datei lokal zu verschlüsseln.

7. **Wiederherstellungsphrase**: Schreiben Sie Ihren seed-Satz auf und bewahren Sie ihn sicher auf.


    - Kritisch**: Dieser Satz wird benötigt, um Ihre on-chain-Gelder und Ihre Knotenidentität wiederherzustellen.
    - Warnung**: **Der Status von Lightning-Kanälen kann nicht vollständig vom seed allein wiederhergestellt werden**. Sie müssen auch statische Kanalsicherungen (SCB) führen, um in Kanälen gesperrte Mittel wiederherzustellen.


![Wallet Creation Screen](assets/en/04.webp)



## Übersicht über das Dashboard


Sobald Ihr wallet erstellt ist, werden Sie zum **Dashboard** weitergeleitet.


![KaleidoSwap Dashboard](assets/en/05.webp)


hinweis: Der obige Screenshot zeigt ein wallet, das bereits finanziert wurde und aktive Kanäle hat. Ein frisches wallet zeigt einen Nullsaldo und keine aktiven Kanäle, bis Sie es finanzieren


## Finanzierung Ihres Wallet


Um mit RGB-Guthaben zu arbeiten, müssen Sie Ihr wallet finanzieren. KaleidoSwap unterstützt die Einzahlung sowohl von Bitcoin- als auch von RGB-Guthaben über on-chain-Transaktionen oder den Lightning Network.


### Hinterlegung von Bitcoin


1. Klicken Sie im Menü Schnellzugriff auf **Einzahlung**.

2. Wählen Sie **BTC** aus der Liste der Vermögenswerte.


![Select BTC Asset](assets/en/06.webp)


3. Wählen Sie Ihre Einzahlungsmethode: **On-Chain** oder **Lightning**.


![BTC Deposit Options](assets/en/07.webp)



- In der Kette**: Scannen Sie den QR-Code oder kopieren Sie die Adresse, um den Bitcoin von einem anderen wallet zu senden.
- Lightning**: Erstellen Sie eine Rechnung über den gewünschten Betrag.


![BTC On-chain Deposit](assets/en/08.webp)


### Hinterlegung von RGB Assets & farbigen UTXOs


Um RGB-Vermögenswerte (wie USDT) zu erhalten, müssen bestimmte UTXOs verfügbar sein, um "gefärbt" (einem Vermögenswert zugewiesen) zu werden.


1. Klicken Sie auf **Einzahlung** und wählen Sie das RGB-Asset (z. B. USDT). **Wichtig**: Wenn dies das **erste Mal** ist, dass Ihr Knoten diesen speziellen Vermögenswert empfängt, **lassen Sie das Feld Asset-ID leer**. Die Eingabe einer ID für einen unbekannten Vermögenswert führt dazu, dass der Knoten eine Fehlermeldung ausgibt, da er ihn noch nicht kennt.

2. Wählen Sie **On-Chain** oder **Lightning**.


![USDT Deposit Options](assets/en/09.webp)


#### On-Chain-Empfangsmodi: Zeuge vs. Geblendet


Beim Empfang von RGB-Assets on-chain stehen Ihnen zwei Datenschutzmodi zur Verfügung:



- Geblendeter Empfang (empfohlen für den Datenschutz)**: Sie stellen dem Absender einen "blinded" UTXO zur Verfügung. Sie bitten den Absender, Assets an einen bestehenden UTXO zu senden, der Ihnen gehört, aber Sie verschleiern die tatsächliche UTXO-Kennung. Dies bietet einen besseren Schutz der Privatsphäre.
- Zeuge empfangen**: Sie geben eine Standard-Bitcoin-Adresse an. Sie bitten den Absender, einen *neuen* UTXO für Sie zu erstellen, indem er die Anlagen an diese Adresse sendet. Auf diese Weise können die RGB-Assets direkt mit dem neuen UTXO verbunden werden, der durch die Transaktion erstellt wurde.


#### Blitzeinlage


Für Blitzeinzahlungen reichen Sie einfach generate eine Rechnung ein. Der RGB Vermögenswert wird über Ihre offenen Kanäle an Sie weitergeleitet.


![USDT Lightning Invoice](assets/en/10.webp)



## Öffnen von Kanälen mit RGB-Assets


Um RGB-Vermögenswerte über den Lightning Network zu leiten, benötigen Sie einen Kanal mit ausreichender Liquidität und Vermögensverteilung. Der einfachste Weg für den Einstieg ist der **Kauf eines Kanals** von einem LSP (Lightning Service Provider).


### Kauf eines Channels von Kaleido LSP


1. Gehen Sie auf die Registerkarte **Kanäle**. Sie sehen die Optionen "Kanal öffnen" (manuell) oder "Kanal kaufen" (LSP).

2. Klicken Sie auf **Kanal kaufen**.


![Channels Dashboard](assets/en/11.webp)


3. **Verbinden mit LSP**: Die App stellt eine Verbindung mit dem Standard-LSP von Kaleido her. Dieser Anbieter bietet eingehende Liquidität und unterstützt RGB Asset-Routing.


![Connect to LSP](assets/en/12.webp)


4. **Kanal konfigurieren**:


    - Kapazität**: Wählen Sie die Gesamtkapazität Bitcoin für den Kanal.
    - RGB-Zuweisung**: Wählen Sie das RGB-Asset (z. B. USDT), das Sie empfangen oder senden können möchten. Der LSP stellt sicher, dass der Kanal für die Unterstützung dieses Assets konfiguriert ist.


![Configure Channel](assets/en/13.webp)



    - RGB-Zuweisung**: Wählen Sie das RGB-Asset (z. B. USDT), das Sie empfangen oder senden können möchten. Der LSP stellt sicher, dass der Kanal für die Unterstützung dieses Assets konfiguriert ist.


![RGB Allocation](assets/en/14.webp)


5.  **Zahlung**: Sie müssen eine Gebühr an den LSP für die Öffnung des Kanals und die Bereitstellung von Liquidität zahlen. Sie können mit **Lightning** oder **On-chain** Bitcoin bezahlen. Die Zahlung kann von Ihrem internen KaleidoSwap wallet oder einem externen wallet aus erfolgen.


![Complete Payment](assets/en/15.webp)


6. Sobald die Zahlung bestätigt ist, leitet der LSP die Transaktion zur Öffnung des Kanals ein. Sie erhalten den Bildschirm **Auftrag abgeschlossen**.


![Order Completed](assets/en/16.webp)


7. Nach der Bestätigung auf der Blockchain ist Ihr Kanal aktiv und bereit für RGB-Überweisungen.



## Handel: Taker-Maker-Modell


Die Handelsmaschine von KaleidoSwap arbeitet nach dem **Taker-Maker-Modell**. Sie können Vermögenswerte manuell mit einem Peer tauschen oder einen Market Maker (LSP) nutzen.


### Tausch mit einem Market Maker (LSP)


Dies ist die häufigste Art des Handels. Sie fungieren als **Taker** und führen Aufträge gegen die vom LSP (**Maker**) bereitgestellte Liquidität aus.


1. Navigieren Sie zur Registerkarte **Handel** und wählen Sie **Market Maker**.

2. **Betrag eingeben**: Geben Sie den Betrag von Bitcoin ein, den Sie senden möchten (oder den Vermögenswert, den Sie erhalten möchten). Die Schnittstelle wird den geschätzten Wechselkurs und die Gebühren anzeigen.


![Market Maker Swap](assets/en/17.webp)


3. **Bestätigen Sie den Tausch**: Überprüfen Sie die Details, einschließlich des Wechselkurses und des genauen Betrags, den Sie erhalten werden. Klicken Sie auf **Bestätigen Sie den Tausch**.


![Confirm Swap](assets/en/18.webp)


4. **Verarbeitung**: Der Swap wird atomar auf dem Lightning Network ausgeführt. Sie sehen einen Statusbildschirm, der anzeigt, dass der Swap noch nicht abgeschlossen ist.


![Swap Pending](assets/en/19.webp)


5. **Erfolg**: Sobald die HTLCs abgewickelt sind, ist der Swap abgeschlossen, und die Vermögenswerte befinden sich in Ihrem Kanal.


![Swap Success](assets/en/20.webp)



## Entwickler API


Für Entwickler, die auf KaleidoSwap aufbauen, stellt die Anwendung einen API zur Verfügung, der unterstützt:



- RGB LSPS1**: Für automatisierte Liquiditätsdienste.
- Swap API**: Für programmatischen Handel und Market Making.
- WebSocket**: Für Echtzeit-Marktdaten-Abonnements.


Die vollständigen Endpunkte und Spezifikationen finden Sie in der [API Dokumentation](https://docs.kaleidoswap.com/api/introduction).


## Schlussfolgerung


Mit KaleidoSwap können Sie die Privatsphäre und Skalierbarkeit von RGB-Assets auf dem Lightning Network nutzen. Wenn Sie Colored UTXOs und die Zuweisung von Kanal-Assets verstehen, können Sie dieses leistungsstarke dezentrale Austauschprotokoll vollständig nutzen.