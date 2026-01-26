---
name: Zeus Swap
description: Nicht-vertrauenswürdiger Exchange-Dienst zwischen On-Chain und Lightning Network Bitcoins
---

![cover](assets/cover.webp)



Das Bitcoin-Ökosystem weist eine Dualität auf: Das Hauptnetz (On-Chain) bietet maximale Sicherheit, während Lightning Network sofortige Transaktionen ermöglicht. Diese Zwei-Layer-Architektur stellt eine praktische Herausforderung dar: Wie können Gelder zwischen diesen beiden Schichten ohne zentrale Vermittler effizient übertragen werden?



Das Problem ist konkret: Sie erhalten eine Lightning-Zahlung, möchten sie aber in Cold-Lagerung aufbewahren, oder umgekehrt, Sie haben On-Chain-Bitcoins, benötigen aber Lightning-Liquidität. Traditionelle Lösungen beinhalten das manuelle Öffnen/Schließen von Lightning-Kanälen (kostspielig und technisch) oder zentralisierte Plattformen, die KYC erfordern.



Zeus Swap löst dieses Problem mit einem automatisierten, nicht-verwahrenden Exchange-Dienst. Er wurde von Zeus LSP entwickelt und ermöglicht es Ihnen, On-Chain-Bitcoins bidirektional in Lightning-Satoshis zu konvertieren, ohne Ihr Geld einem Vermittler anzuvertrauen. Der Prozess verwendet atomare Verträge (HTLC), die garantieren, dass der Exchange entweder abgeschlossen oder abgebrochen wird.



Die Innovation liegt in der Einfachheit: nur ein paar Klicks für ein Exchange, das Ihre finanzielle Souveränität bewahrt und keine Registrierung oder KYC erfordert.



## Was ist Zeus Swap?



Zeus Swap ist ein von Zeus LSP entwickelter Exchange-Liquiditätsdienst, der atomare Swaps zwischen dem Bitcoin-Hauptnetz und Lightning Network ermöglicht. Es handelt sich um eine technische Infrastruktur, die Submarine-Swaps und Reverse-Swaps nutzt, um die Zwei-Wege-Konvertierung zwischen On-Chain-BTC und Lightning-Satoshis zu erleichtern und gleichzeitig den nicht-kustodialen Charakter des Vorgangs zu bewahren.



### Technische Architektur



Zeus Swap verwendet die quelloffene Bitcoin/Lightning-Atomtausch-Technologie von Boltz. Das Protokoll verwendet Hash Time Locked Contracts (HTLC): Verträge, die Gelder mit zwei Freigabebedingungen (Enthüllung eines kryptografischen Geheimnisses oder Zeitablauf) sperren.



Bei einem U-Boot-Swap (On-Chain → Lightning) sendet der Nutzer Bitcoins an einen Address, der den Hash eines Lightning Invoice enthält. Zeus LSP schaltet diese Mittel nur frei, indem es den entsprechenden Invoice bezahlt und das Vorabbild offenlegt, das die Bitcoins automatisch freigibt. Dieser Mechanismus garantiert Atomarität.



Bei einem umgekehrten Swap (Lightning → On-Chain) bezahlt der Nutzer einen Lightning Invoice von Zeus LSP, wodurch ein Vorabbild sichtbar wird, das die Freigabe einer vorbereiteten Bitcoin-Transaktion an den Ziel-Address ermöglicht.



Weitere Einzelheiten zur Funktionsweise des Lightning Network finden Sie in unserem speziellen Kurs:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Das Geschäftsmodell



Zeus LSP fungiert als Market Maker, der die Liquidität von On-Chain und Lightning aufrechterhält, um Swaps zu honorieren. Für Swaps erhebt Zeus eine variable Gebühr (in der Regel 0,1 % bis 0,5 % je nach Richtung und Bedingungen) zuzüglich der Bitcoin-Gebühr für Mining, die vor der Validierung transparent angezeigt wird.



Als Lightning Service Provider optimiert Zeus die Kosten dank seiner Expertise in der bedarfsgerechten Öffnung von Kanälen, effizientem Routing und maßgeschneiderten Liquiditätslösungen.



### Integration



Zeus Wallet integriert den Dienst nativ und ermöglicht den Austausch, ohne Interface Bitcoin/Lightning zu verlassen. Damit entfällt die Reibung des Kopierens und Einfügens zwischen Anwendungen.



Das unabhängige Interface-Web bleibt für alle Geldbörsen zugänglich, was eine maximale Flexibilität bei der Nutzung garantiert.



## Hauptmerkmale



### Bidirektionale Swaps



Zeus Swap bietet zwei Arten von Exchange an:



**U-Boot-Tausch (On-Chain → Lightning)**: Einspeisung von Lightning-Liquidität aus Ihren Bitcoin-Reserven, nützlich für die Versorgung eines mobilen Wallet- oder Lightning-Knotens ohne manuelles Öffnen von Kanälen.



**Reverse Swaps (Lightning → On-Chain)**: Umwandlung von Lightning-Satoshis in On-Chain-Bitcoins für die langfristige Lagerung, um kostspielige Kanalschließungen zu vermeiden.



### Benutzeroberflächen



**Interface web** (swaps.zeuslsp.com): vereinfachtes Verfahren ohne Registrierung, geführter Prozess mit Echtzeitanzeige von Gebühren und Status.



**Zeus Wallet-Integration**: direkter Austausch aus der Anwendung, automatische Verwaltung von Rechnungen und Adressen, Vermeidung von Bearbeitungsfehlern.



### Sicherheit und Wiederherstellung



Jeder Swap erzeugt einen einzigartigen Contract mit unveränderlichen Parametern: Hash Lightning, Timeout, Erstattung Address. Im Falle eines Ausfalls automatische Wiederherstellung über den Address bereitgestellt, unabhängig von Zeus LSP.



**Zeus Swaps Rescue Key**: Während eines On-Chain → Lightning Swaps erzeugt Zeus automatisch einen universellen Wiederherstellungsschlüssel, der die alten individuellen Erstattungsdateien ersetzt. Dieser einzigartige Schlüssel funktioniert auf jedem Gerät und für alle mit ihm erstellten Swaps. Es ist wichtig, diesen Schlüssel herunterzuladen und an einem sicheren Ort zu speichern, damit Sie Ihre Gelder im Falle eines Swap-Fehlers wiederherstellen können.



### Optimierung des Netzes



Zeus Swap passt die Verfallszeiten und Mining-Gebühren automatisch an die Netzbedingungen an. Zeus-Benutzer profitieren von erweiterten Optionen: Wahl des LSP, angepasste Verzögerungen, Kompatibilität mit anderen Diensten (Boltz).



## Installation und Nutzung



### Zugriffsmethoden



**Interface web** (swaps.zeuslsp.com): universelle Lösung, kompatibel mit allen Geldbörsen, keine Installation erforderlich, ideal für den gelegentlichen Gebrauch.



**Zeus-App** (iOS/Android): integrierte Erfahrung, die Wallet und Swaps kombiniert, geeignet für regelmäßige Nutzer.



In unserem Zeus-Tutorial erfahren Sie mehr über diesen kompletten Wallet :



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Web-Konfiguration



**On-Chain → Lightning**: Der Prozess beginnt mit der Konfiguration des Swaps auf dem Interface Web Zeus Swap. Der Benutzer kann den Pfeil zwischen den Feldern On-Chain und Lightning verwenden, um die Richtung des Swaps umzukehren.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: Betragswahl (Sats 50.000 → Sats 49.648 nach Gebühren) mit transparenter Anzeige der Netzentgelte (Sats 302) und des Zeus-Dienstes (Sats 50).*



Während des Vorgangs bietet Zeus Ihnen an, den Universal Recovery Key herunterzuladen:



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Download-Dialog für den Zeus Swaps Rescue Key - ein Universalschlüssel, der die alten individuellen Erstattungsdateien ersetzt*



Wenn Sie bereits einen Schlüssel haben, können Sie ihn mit Zeus überprüfen:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface zur Überprüfung der Gültigkeit eines vorhandenen Zeus Swaps Rescue Key*



Nach der Konfiguration erzeugt Zeus das Bitcoin-Depot Address und zeigt die Anweisungen an:



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Seite für den Tauschabschluss: QR-Code und Bitcoin Address für den Versand von 50.000 Satss, mit Erinnerung an das 24-Stunden-Verfallsdatum*



Der Swap wartet dann auf die Bestätigung durch Bitcoin:



![Attente de confirmation](assets/fr/05.webp)



*Status "Transaktion in Mempool" - Warten auf die Bestätigung von Bitcoin, um den Tausch abzuschließen*



Nach der Bestätigung wird der Tausch automatisch abgeschlossen:



![Swap réussi](assets/fr/06.webp)



*Bestätigung des Erfolgs: 49.648 Sats erhalten auf Lightning nach Abzug der Netz- und Servicegebühren*



### Verwendung der Zeus-App



**Lightning → On-Chain**: Die Zeus-Anwendung bietet eine integrierte Erfahrung für Reverse Swaps (Lightning bis Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Zeus-Hauptbildschirm mit den Bilanzen von Lightning (69.851 Sats) und On-Chain (38.018 Sats), Zugriff auf Swaps über das Seitenmenü*



![Configuration du swap reverse](assets/fr/08.webp)



*Erstellung eines Interface Reverse Swap: 50.000 Sats Lightning → 49.220 Sats On-Chain, wobei Netzgebühren (530 Sats) und Service (250 Sats) deutlich angezeigt werden. Benutzer können entweder manuell einen Bitcoin eingeben, der Address empfängt, oder einen generate automatisch vom Wallet Zeus über die Schaltfläche "generate On-Chain Address"



![Finalisation du swap mobile](assets/fr/09.webp)



*Abschlussbildschirme: Lightning Invoice Zahlungsbildschirm mit "PAY THIS Invoice", Bestätigung der erfolgreichen Lightning-Zahlung in 9,96 Sekunden und Saldenliste mit den 49.162 Sats, die auf eine Bestätigung warten*



### Überwachung und Sicherheit



Jeder Swap hat eine eindeutige Kennung mit Echtzeit-Verfolgung. Vollständige Fortschrittsanzeige, automatische Warnungen bei Ablauf der Frist. Automatische Ladeempfehlungen je nach Netzbedingungen.



## Vorteile und Grenzen



### Vorteile





- Einfachheit**: Austausch mit ein paar Klicks im Vergleich zur manuellen Kanalmanipulation
- Non-custodial**: keine KYC, kein Konto, Gelder werden nie einer dritten Partei anvertraut
- Transparenz**: Gebühren werden vor der Validierung explizit angezeigt (0,1 % bis 0,5 % + Mindestbetrag je nach Nutzertests - aktuelle Gebühren bei jedem Swap überprüfen)
- Mobile Integration**: native Erfahrung in Zeus Wallet



### Beschränkungen





- Verfallszeiten**: maximal 24-48h, Ausfall, wenn Bitcoin nicht rechtzeitig bestätigt wird
- Betragsgrenzen**: mindestens 25.000 Sats, Zeus LSP Liquidität variabel je nach Konditionen
- Verfolgt On-Chain**: HTLC-Skripte, die möglicherweise durch die Blockchain-Analyse identifiziert werden können
- Bestätigung erforderlich**: mindestens 10 Minuten für Bitcoin-Validierung



## Bewährte Praktiken



### Zeitplan und Kosten





- Beobachten Sie Mempool.space in Zeiten mit geringer Überlastung
- Bevorzugen Sie Wochenenden und verkehrsschwache Zeiten, um die Mining-Kosten zu senken
- Rentabilitätsberechnung: kleine Beträge vs. direkte Kanalöffnung



### Sicherheit





- Prüfen Sie die Bitcoin-Adressen sorgfältig (Kopieren und Einfügen empfohlen)
- Sichern Sie den Zeus Swaps Rescue Key**: Laden Sie den Wiederherstellungsschlüssel herunter und bewahren Sie ihn an einem sicheren Ort auf
- Dokument: Contract ID, Erstattung Address, Verfallsdatum
- Verwenden Sie die entsprechenden Mining-Gebühren für die rechtzeitige Bestätigung



### Strategie für die Nutzung





- Balance On-Chain/Blitzliquidität für Ihre Bedürfnisse
- Zeus Swap für einmalige Anpassungen, Direktkanäle für dauerhaften Bedarf



## Vergleich mit anderen Swap-Diensten



### Zeus Swap gegen Boltz Exchange



Zeus Swap nutzt die Backend-Technologie von Boltz, bietet aber einige entscheidende Verbesserungen:



**Zeus Swap Vorteile** :




- Interface unified**: native Integration in Zeus Wallet vs Interface Webtechnik Boltz
- WebSocket API**: Aktualisierungen in Echtzeit gegenüber manueller Abfrage
- Automatisierte Verwaltung**: automatische Rechnungsstellung und Address-Verwaltung
- Mobile Unterstützung**: Optimierung nur für Smartphones vs. Desktop
- Swagger-Dokumentation**: vollständige REST-API für Entwickler



**Boltz bleibt vorteilhaft** für völlige Unabhängigkeit und die Verwendung mit jedem Bitcoin/Lightning-Setup.



Zeus Swap verwandelt die bewährte Boltz-Technologie in ein Mainstream-Nutzererlebnis, vergleichbar mit dem Unterschied zwischen einem Rohprotokoll und einer benutzerfreundlichen Anwendung.



### Zeus Swap gegen Phoenix/Breez (integrierte Swaps)



Phoenix und Breez integrieren transparente Swap-Funktionen, die die technische Komplexität vor dem Endnutzer verbergen. Phoenix verwendet ein automatisches Swap-in/Swap-out-System, bei dem der Benutzer nicht explizit zwischen Bitcoin-Ebenen unterscheidet: Er "sendet an einen Bitcoin Address" und die Anwendung führt den Swap im Hintergrund durch.



Dieser ultra-vereinfachte Ansatz ist perfekt für Anfänger geeignet, schränkt aber das Verständnis und die Kontrolle der Vorgänge ein. Zeus Swap verfolgt eine pädagogischere Philosophie: Die Nutzer verstehen, dass sie zwischen zwei verschiedenen Ebenen wechseln und entwickeln allmählich ein Verständnis für das Ökosystem der zwei Layer Bitcoin.



## Detaillierter Vergleich der Gebühren und Grenzwerte (2024)



⚠️ **Warnung**: Die Gebühren können im Laufe der Zeit je nach Marktbedingungen und Service-Updates variieren. Überprüfen Sie immer die im Interface angezeigten Gebühren, bevor Sie einen Swap validieren.




| Service | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Mindestbetrag |
| ------------- | ----------------------- | --------------------- | --------------- |
| **Zeus Swap** | ~0.1% + Mining-Gebühren | 0.5% + Mining-Gebühren | 25.000 Sats |
| **Boltz** | 0.2% + Mining-Gebühren | 0.5% + Mining-Gebühren | 50.000 Sats |
| **Phoenix** | Nur Mining-Gebühren | 0.4% fix | 10.000 Sats |
| **Breez** | 0.25% + Netzwerkgebühren | 0.5% + Mining-Gebühren | 50.000 Sats |

Zeus Swap bietet ein ausgewogenes Verhältnis zwischen Benutzerfreundlichkeit und technischer Kontrolle: zugänglicher als Boltz, flexibler als Phoenix/Breez, mit einem strikten, nicht disziplinarischen Ansatz.



## Schlussfolgerung



Zeus Swap stellt eine bedeutende Innovation im Bitcoin-Ökosystem dar und löst auf elegante Weise die Herausforderung der Interoperabilität zwischen dem Hauptnetz und Lightning Network. Durch die Kombination der kryptografischen Robustheit atomarer Swaps mit einer zugänglichen Benutzererfahrung demokratisiert dieser Dienst die Bitcoin-Dual-Layer-Verwaltung, ohne die Grundsätze der Finanzsouveränität zu gefährden.



Die nicht-verwahrende Architektur von Zeus Swap, die von der bewährten Boltz-Technologie übernommen wurde, stellt sicher, dass Ihre Mittel während des gesamten Swap-Prozesses unter Ihrer alleinigen Kontrolle bleiben. Dieser Ansatz respektiert den Geist von Bitcoin und bietet gleichzeitig die Benutzerfreundlichkeit, die für eine breite Akzeptanz erforderlich ist. Preistransparenz und das Fehlen von KYC-Prozessen verstärken dieses einzigartige Wertversprechen.



Für den modernen Bitcoin-Nutzer ist Zeus Swap ein strategisches Instrument zur Optimierung der bedarfsgerechten Verteilung von Liquidität: On-Chain sichere Aufbewahrung für langfristige Einsparungen, Blitzverfügbarkeit für tägliche Ausgaben und Mikrotransaktionen. Diese Flexibilität verwandelt das Bitcoin-Management von einer technischen Einschränkung in einen Wettbewerbsvorteil.



Die künftige Entwicklung von Zeus Swap, unterstützt durch das erfahrene Zeus LSP-Team und die Open-Source-Gemeinschaft von Boltz, verspricht weitere Verbesserungen in Bezug auf Kosten, Verarbeitungszeiten und Benutzerfreundlichkeit. Dieser Dienst ist Teil des allgemeinen Trends zur Reifung der Bitcoin-Infrastruktur, bei der die technische Raffinesse für den Endnutzer transparent wird.



## Ressourcen



### Offizielle Dokumentation




- [Zeus Swap - Webportal](https://swaps.zeuslsp.com)
- [Zeus Wallet - Mobile Anwendung](https://zeusln.app)
- [Blog Zeus - Ankündigungen und Anleitungen](https://blog.zeusln.com)
- [Technische Dokumentation Zeus](https://docs.zeusln.app)



### Gemeinschaft und Unterstützung




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegramm Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)