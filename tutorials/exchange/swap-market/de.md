---
name: SwapMarket
description: Bitcoin und Lightning Swap Services Aggregator
---

![cover](assets/cover.webp)



Der Transfer von Geldern zwischen Bitcoin On-Chain und Lightning Network erfordert im Allgemeinen entweder die manuelle Öffnung von Lightning-Kanälen (technisch und kostspielig) oder die Nutzung zentralisierter Swap-Plattformen mit KYC. SwapMarket bietet eine Alternative: Trustless-Atom-Swaps über wettbewerbsfähige Anbieter, ohne KYC.



Innovation: Obwohl die Anbieter Vermittler sind, garantieren HTLC (*Hash Time Locked Contracts*) mathematisch, dass Ihre Mittel unter Ihrer Kontrolle bleiben. Der Zusammenschluss mehrerer Anbieter (Boltz, ZEUS Swaps, Eldamar, Middle Way) schafft Preiswettbewerb. Interface web open-source selbst-hostbar.



## Was ist SwapMarket?



SwapMarket ist ein Open-Source-Aggregator, der 2024 eingeführt wurde und als Vergleichsrechner für Bitcoin/Lightning-Swap-Anbieter fungiert. Der Nutzer vergleicht sofort die Konditionen (Gebühren, Liquidität, Limits) und wählt den optimalen Anbieter aus.



### Technische Architektur



**Frontend clientseitig**: 100% clientseitige Anwendung (Fork Boltz Web App) gehostet auf GitHub Pages. Code läuft im Browser ohne Backend-Server. Verlauf wird lokal gespeichert (Cookies/Cache). Öffentlicher und überprüfbarer Quellcode.



**Provider-Ermittlung** : Hard-kodierte Liste in `src/configs/Mainnet.ts`. Neue Anbieter werden per Pull Request oder E-Mail hinzugefügt.



**Unabhängige Backends**: Jeder Anbieter betreibt sein eigenes Boltz-Backend. Interface fragt die APIs in Echtzeit ab, um Angebote sofort zu vergleichen.



**HTLC Atomare Swaps**: Hash Time Locked Contracts garantieren Atomarität: entweder wird der Swap ausgeführt, oder jede Partei erhält ihr Geld zurück. Das Kontrahentenrisiko wird mathematisch eliminiert.



### Philosophie



SwapMarket reduziert die Zentralisierung durch die Schaffung von Wettbewerb zwischen Anbietern für Gebühren und Liquidität. Keine KYC, Open-Source-Code, der selbst gehostet werden kann, Vervielfältigung unabhängiger Betreiber zur Vermeidung von Single Points of Failure.



## Hauptmerkmale



### Anbieter-Marktplatz



Interface zeigt alle aktiven Anbieter an: Name des Anbieters, angewandte Gebühren (prozentual und/oder fest), verfügbare Mindest-/Höchstbeträge und unterstützte Swap-Typen. Die Anwendung fragt direkt die APIs jedes in der Konfigurationsdatei angegebenen Anbieters ab, um Kurse in Echtzeit zu erhalten. Der Wettbewerb zwischen den Anbietern garantiert optimale Zinssätze, die im Allgemeinen bei 0,5 % für Standard-Swaps liegen.



### Bidirektionale Swaps



**Swap-in (On-Chain → Lightning)**: Konvertieren Sie On-Chain BTCs in Lightning-Satoshis. Anwendungsfall: Betreiben Sie einen mobilen Wallet Lightning, erhalten Sie eingehende Kapazität auf einem Knoten oder haben Sie sofortige Liquidität.



**Swap-out (Lightning → On-Chain)**: Umwandlung von Lightning-Satoshis in On-Chain BTC. Anwendungsfall: Auslagerung von Wallet-Lightning in Cold-Speicher oder Umschichtung von Liquidität zwischen Schichten.



### Sicherheit und Wiederherstellung



**Trustless Atomtausch: HTLC garantiert, dass entweder der Exchange vollständig erfüllt wird oder jede Partei ihren Einsatz zurückerhält. Das Kontrahentenrisiko wird mathematisch eliminiert.



**Rückzahlungsmechanismus**: Jeder Swap hat ein Verfallsdatum (TIMELOCK). Wenn der Swap scheitert, werden die Gelder nach Ablauf automatisch zurückerstattet. Der Nutzer behält immer die Möglichkeit, seine Bitcoins zurückzufordern.



**Wiederherstellungsschlüssel**: Mit SwapMarket können Sie Wiederherstellungsschlüssel für laufende Swaps exportieren. Im Falle eines Problems können diese Schlüssel verwendet werden, um einen Swap von einem beliebigen Gerät aus abzuschließen oder abzubrechen.



## Installation und Zugang



### Interface web



SwapMarket erfordert keine Installation. Der Zugang erfolgt über den Browser, indem Sie https://swapmarket.github.io besuchen. Für maximale Vertraulichkeit verwenden Sie Brave, Firefox mit Anti-Tracking-Erweiterungen oder LibreWolf. Für die Anonymität im Netz wird der Tor-Browser empfohlen.



Keine Registrierung, E-Mail oder Identitätsprüfung erforderlich.



### Selbst-Hosting (optional)



Für technische Benutzer, die keine Abhängigkeit von der offiziellen GitHub Pages-Domäne wünschen, kann SwapMarket lokal ausgeführt werden:



**Via npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Via Docker** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



Die Anwendung wird unter `http://localhost:3000` zugänglich sein. Das Self-Hosting garantiert die vollständige Kontrolle über Interface, eliminiert das Risiko der Zensur der offiziellen Domäne und ermöglicht die Überprüfung des Quellcodes vor der Ausführung.



### Erstmalige Konfiguration



**Wallet Lightning**: Vergewissern Sie sich, dass Sie einen betriebsbereiten Wallet Lightning haben (Phoenix, Zeus, BlueWallet usw.). Für Swap-Ins erhalten Sie generate und Lightning Invoice. Für Swap-outs zahlen Sie einen Lightning Invoice.



**Wallet On-Chain**: Für Swap-Ins benötigen Sie einen Wallet Bitcoin On-Chain, um Geld zu senden. Für Swap-Outs bereiten Sie einen Bitcoin vor, der Address erhält.



**Optionale Konfiguration**: SwapMarket speichert den Tauschverlauf und die Präferenzen in Browser-Cookies. Keine Kontoerstellung erforderlich.



## Zugriff auf Einstellungen und Rettungsschlüssel



Bevor Sie Ihre ersten Swaps vornehmen, empfehlen wir Ihnen dringend, Ihren **Rescue Key** herunterzuladen. Mit diesem Notfallschlüssel können Sie Ihr Guthaben im Falle eines technischen Problems oder des Verlusts des Zugangs zu Ihrem Gerät wiederherstellen.



### Zugangsparameter



Klicken Sie auf der SwapMarket-Hauptseite auf das Zahnradsymbol (⚙️) oben rechts auf der Interface, neben dem Tauschformular.



![Accès aux paramètres](assets/fr/01.webp)



### Seite Einstellungen



Die Seite Einstellungen wird geöffnet, auf der mehrere Konfigurationsoptionen angezeigt werden:





- Denominierung**: Wahl zwischen BTC oder Sats
- Dezimaltrennzeichen**: Dezimaltrennzeichen (, oder .)
- Audio-/Browser-Benachrichtigungen**: Audio- und Browser-Benachrichtigungen
- Rettungsschlüssel** : Download des Wiederherstellungsschlüssels
- Protokolle**: Protokolle anzeigen, herunterladen oder löschen



![Page Settings](assets/fr/02.webp)



### Rettungsschlüssel herunterladen



Klicken Sie auf die Schaltfläche **Download** neben "Rettungsschlüssel".



**Wichtige Punkte** :




- Der Rescue Key ist ein **Notfallschlüssel**, der für alle Ihre zukünftigen Swaps funktioniert
- Bewahren Sie diesen Schlüssel an einem **sicheren und dauerhaften** Ort auf (Passwortmanager, digitaler Safe)
- Im Falle eines Swap-Problems (Zeitüberschreitung, technisches Versagen) können Sie mit diesem Schlüssel Ihr Guthaben wiederherstellen



## Schritt für Schritt einen Swap erstellen



### Auswechseln: Lightning → Bitcoin



Dieses erste Beispiel zeigt, wie man Lightning-Satoschis in On-Chain-Bitcoins umwandelt.



**Schritt 1: Konfiguration austauschen



Wählen Sie auf der Hauptseite das Tauschformular aus:




- LIGHTNING** (oberes Feld): Geben Sie den Betrag ein, den Sie in Sats Lightning senden möchten (Beispiel: 30.000 Sats)
- Bitcoin** (unteres Feld): Der Betrag, den Sie erhalten, wird automatisch nach Abzug der Gebühren angezeigt (Beispiel: Sats 29.320)



Fügen Sie in das untere Feld Ihren **Empfangs-Bitcoin-Address** ein, an den Sie das Geld überweisen möchten. Prüfen Sie diese Address sorgfältig.



Der Standardanbieter ist in der Regel Boltz Exchange. Die Netzgebühren und die Gebühren des Anbieters werden deutlich angezeigt.



![Configuration swap-out](assets/fr/03.webp)



**Schritt 2: Auswahl des Anbieters**



Klicken Sie auf das Dropdown-Menü des Anbieters (Standard: "Boltz Exchange"), um alle verfügbaren Liquiditätsanbieter anzuzeigen.



Es öffnet sich ein modales Fenster, in dem eine Vergleichstabelle angezeigt wird:




- Status**: Green Anzeige, ob der Anbieter aktiv ist
- Alias**: Name des Anbieters (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Gebühr**: Vom Anbieter erhobene Gebühren (im Allgemeinen zwischen 0,49 % und 0,5 %)
- Max Swap**: Maximal akzeptierter Betrag für einen Swap



Vergleichen Sie Gebühren und Höchstbeträge und wählen Sie dann den Anbieter Ihrer Wahl.



**Bitte beachten**: In der Interface zur Anbieterauswahl werden die **Mindestbeträge** für die einzelnen Anbieter nicht angezeigt. Diese Information erscheint erst in der Interface zur Swap-Erstellung, nachdem ein Anbieter ausgewählt wurde. Mindest- und Höchstbeträge können von Anbieter zu Anbieter variieren und sich im Laufe der Zeit ändern. **Wenn der Betrag, den Sie tauschen möchten, außerhalb der Grenzen eines Anbieters liegt, können Sie einen anderen Anbieter wählen, der für Ihre Transaktion besser geeignet ist.



![Sélection du provider](assets/fr/04.webp)



**Schritt 3: Swap-Erstellung und Blitzzahlung**



Klicken Sie auf die gelbe Schaltfläche **"ATOMIC SWAP ERSTELLEN "**. SwapMarket wird generate ein **Lightning Invoice** (BOLT11) für Sie von Ihrem Wallet Lightning zu bezahlen.



Die Seite zeigt an:




- Swap-ID**: Eindeutige Swap-Kennung (Beispiel: J4ymFIMVR6Hm)
- Status**: "swap.created" (Swap erstellt, wartet auf Zahlung)
- QR-Code**: Scannen Sie ihn mit Ihrem Wallet Lightning
- Invoice Lightning**: Zeichenfolge, die mit "lnbc" beginnt (Beispiel: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Bezahlen Sie diesen Invoice von Ihrem Wallet Lightning (Phoenix, Zeus, BlueWallet, etc.). Der genaue zu zahlende Betrag wird angezeigt (Beispiel: 30.000 Sats).



![Paiement Lightning](assets/fr/05.webp)



**Schritt 4: Bestätigung und Annahme**



Sobald die Lightning-Zahlung bestätigt wurde, erhält SwapMarket sofort Ihre Zahlung und der Anbieter sendet die Bitcoin-Transaktion an Ihr Address.



Der Status wechselt zu **"Invoice.settled "** (Invoice bezahlt), und es erscheint eine Bestätigungsmeldung.



Ihre On-Chain-Bitcoins sind verfügbar, sobald die Transaktion bestätigt wurde (in der Regel innerhalb weniger Minuten bis zu einigen Stunden, je nach den vom Anbieter gewählten Mining-Gebühren).



![Confirmation swap-out](assets/fr/06.webp)



Sie können auf **"OPEN CLAIM TRANSACTION "** klicken, um die Bitcoin-Transaktion in einem Blockchain-Explorer anzuzeigen.



### Einwechseln: Bitcoin → Lightning



Dieses zweite Beispiel zeigt, wie man On-Chain-Bitcoins in Lightning-Satoshis umwandelt.



**Schritt 1: Konfiguration austauschen



Wählen Sie auf der Hauptseite das Tauschformular aus:




- Bitcoin** (oberes Feld): Geben Sie den Betrag ein, den Sie in Sats Bitcoin senden möchten (Beispiel: 63.400 Sats)
- LIGHTNING** (unteres Feld): Der Betrag, den Sie erhalten, wird automatisch nach Abzug der Gebühren angezeigt (Beispiel: 62 884 Sats)



Fügen Sie in das untere Feld einen Lightning** Invoice (BOLT11) ein, der von Ihrem Wallet Lightning erzeugt wurde, oder verwenden Sie Ihren LNURL Address, wenn Ihr Wallet dies unterstützt.



![Configuration swap-in](assets/fr/07.webp)



**Schritt 2: Prüfung des Rettungsschlüssels**



Nachdem Sie auf **"ATOMIC SWAP ERSTELLEN "** geklickt haben, erscheint ein modales Fenster, in dem Sie aufgefordert werden, Ihren Rescue Key zu bestätigen.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rettungsschlüssel**: Da Sie Ihren Rettungsschlüssel bereits bei der Erstkonfiguration hochgeladen haben (siehe vorheriger Abschnitt), klicken Sie auf die Schaltfläche **"VERIFY EXISTING KEY "**, um den gespeicherten Schlüssel zu importieren.



Wählen Sie die zuvor heruntergeladene Rescue Key-Datei aus. Nach erfolgreicher Überprüfung fährt das Interface automatisch mit dem nächsten Schritt fort.



**Schritt 3: Bitcoin** Hinterlegung Address



SwapMarket generiert jetzt einen **einzigartigen Bitcoin Address**, der den HTLC Contract enthält, der mit Ihrem Lightning Invoice verbunden ist.



Die Seite zeigt an:




- Swap-ID**: Eindeutige Kennung (Beispiel: 1kGmB6JyGqU4)
- Status** : "Invoice.set" (Invoice gesetzt, wartet auf Zahlung Bitcoin)
- QR-Code**: Bitcoin Betriebshof Address
- Bitcoin** Address: Beginnt normalerweise mit "bc1p..." (Beispiel: bc1p5mvtwxapjkds...9d4n9f)
- Warnung in gelb** : "Stellen Sie sicher, dass Ihre Transaktion innerhalb von ~24 Stunden nach der Erstellung dieses Swaps bestätigt wird!"



Dieser Zeitraum von ~24 Stunden ist der **Timeout** des HTLC Contract. Wenn Ihre Bitcoin-Transaktion nicht innerhalb dieses Zeitrahmens bestätigt wird, schlägt der Swap fehl und Sie müssen Ihren Rescue Key verwenden, um Ihr Geld zurückzuerhalten.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Sie können den Address kopieren, indem Sie auf die Schaltfläche **"Address"** klicken, oder den QR-Code direkt von Ihrem Wallet On-Chain scannen.



**Schritt 4: Bitcoins senden**



Senden Sie von Ihrem Wallet Bitcoin On-Chain **genau** den angegebenen Betrag (z. B. 63.400 Sats) an den erzeugten Address.



**Wichtig**: Verwenden Sie angemessene Mining-Gebühren, um eine schnelle Bestätigung zu gewährleisten. Ist die Gebühr zu niedrig und verbleibt die Transaktion über den Timeout (~24h) hinaus in Mempool, schlägt der Swap fehl.



Sobald die Transaktion gesendet wurde, erkennt SwapMarket, dass es sich um Mempool handelt und zeigt :




- Status** : "Transaktion.Mempool"
- Meldung**: "Transaktion ist in Mempool - Warte auf Bestätigung, um den Tausch abzuschließen"



![Transaction en mempool](assets/fr/10.webp)



**Schritt 5: Bestätigung und Blitzempfang**



Sobald die Bitcoin-Transaktion ihre erste Bestätigung erhält, zahlt der Anbieter automatisch Ihren Lightning Invoice aus. Sie erhalten die Satoshis sofort auf Ihrem Wallet Lightning.



Der Status ändert sich zu **"Transaktion.Anspruch.ausstehend "**, dann wird eine Bestätigungsmeldung angezeigt:



![Confirmation swap-in](assets/fr/11.webp)



Ihre Lightning-Satoshis sind sofort in Ihrem Wallet verfügbar.



## Vorteile und Grenzen



### Vorteile



**Tarifwettbewerb**: Durch die Zusammenlegung von Anbietern entsteht ein natürlicher Wettbewerb, der die Gebühren nach unten zieht (0,49 % bis 0,5 %).



**Vertraulichkeit**: Kein KYC, Interface 100% clientseitig (keine Übertragung von persönlichen Daten), Tor-Browser kompatibel.



**Nicht sorgeberechtigt**: HTLC garantieren mathematisch die alleinige Kontrolle über Ihr Geld. Entweder der Tausch ist erfolgreich, oder Sie erhalten Ihre Bitcoins zurück.



**Open-Source-Self-Hosting**: überprüfbarer öffentlicher Code, der lokal eingesetzt werden kann, um möglichst unempfindlich gegen Zensur zu sein.



### Beschränkungen



**Begrenzte Liquidität**: Begrenzte Anzahl von aktiven Anbietern (Boltz, Eldamar, MiddleWay je nach Zeitraum). Die Höchstbeträge können begrenzt sein.



**Ablaufzeit**: Zeitüberschreitung von 24h bis 48h. Wenn die On-Chain-Transaktion nicht vor Ablauf bestätigt wird, ist eine manuelle Wiederherstellung erforderlich.



**Interface Zentralisierung**: Obwohl es selbst gehostet werden kann, wird das offizielle Interface auf GitHub Pages gehostet. Wenn GitHub das Repo zensiert, wird der Zugriff über swapmarket.github.io blockiert (Lösung: Selbst-Hosting).



**On-Chain-Spuren**: HTLC-Skripte sind potenziell durch eine erweiterte Blockchain-Analyse identifizierbar.



## Bewährte Praktiken



### Sichere Konfiguration



**Laden Sie Ihren Rescue Key herunter**: Laden Sie vor Ihren ersten Swaps Ihren Rescue Key aus den Einstellungen herunter (siehe entsprechender Abschnitt oben). Dieser einmalige Schlüssel gilt für alle zukünftigen Swaps und ermöglicht es Ihnen, Ihr Guthaben im Falle eines Problems wiederherzustellen.



**Tor-Browser verwenden**: Für maximale Vertraulichkeit greifen Sie auf SwapMarket über den Tor-Browser zu, um Ihre IP Address zu verbergen.



**Erwägen Sie Selbst-Hosting**: Für technische Benutzer, die ihre eigene SwapMarket-Instanz betreiben, entfällt die Abhängigkeit von der offiziellen GitHub Pages-Domäne.



### Optimierung der Auslagerung



**Beobachten Sie Mempool**: Prüfen Sie Mempool.space vor einer Auslagerung. Wählen Sie Zeiten mit geringer Aktivität, um die Mining-Kosten zu minimieren.



**Überprüfen Sie die Adressen**: Prüfen Sie bei einem Tausch die empfangene Address-Adresse genauestens. Verwenden Sie Kopieren und Einfügen und überprüfen Sie die ersten 5 und die letzten 5 Zeichen.



**Testen Sie mit kleinen Mengen**: Beginnen Sie mit der kleinstmöglichen Menge (25.000 bis 50.000 Sats). Erhöhen Sie die Menge allmählich, wenn Sie das Verfahren beherrschen.



**Dokumentieren Sie Ihre Swaps**: Notieren Sie sich für jeden Swap die ID, die Rückzahlung Address und das Verfallsdatum. Diese Informationen erleichtern die Rückverfolgung und Wiederherstellung im Falle eines technischen Problems.



### Strategie für die Nutzung



**Balancieren Sie Ihren Cashflow**: Verwenden Sie SwapMarket, um Ihre Aufteilung zwischen On-Chain (Ersparnisse, langfristige Sicherheit) und Lightning (tägliche Ausgaben, sofortige Zahlungen) entsprechend Ihren tatsächlichen Bedürfnissen anzupassen.



**Berechnen Sie die Rentabilität**: Vergleichen Sie bei dauerhaftem Lightning-Liquiditätsbedarf die kumulierten Kosten wiederholter Swaps mit der direkten Eröffnung eines Lightning-Kanals. SwapMarket eignet sich hervorragend für einmalige Anpassungen, nicht unbedingt für große regelmäßige Ströme.



## SwapMarket vs. Boltz: Was ist der Unterschied?



### Boltz: Technik vs. Dienstleistung



**Boltz ist die Open-Source-Technologie** (`boltz-backend` auf GitHub), die atomare Tauschvorgänge über HTLC zwischen Bitcoin, Lightning und Liquid implementiert.



**Kritischer Punkt**: Alle SwapMarket-Anbieter (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) setzen ihre eigene Instanz des Boltz-Backends ein. Die zugrunde liegende Technologie ist daher identisch. Eine Schwachstelle im Boltz-Backend würde potenziell alle Anbieter betreffen, aber der Open-Source-Charakter des Systems ermöglicht eine Überprüfung durch die Gemeinschaft.



**Boltz Exchange** ist ein einzelner Dienst, der vom Boltz-Team betrieben wird, während **SwapMarket** mehrere Anbieter zusammenbringt, die alle die Boltz-Technologie nutzen und so ein wettbewerbsfähiges Preisumfeld schaffen.



Weitere Einzelheiten finden Sie in unseren Anleitungen zu Boltz und Zeus Swap:



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Wesentliche Unterschiede



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**SwapMarket-Vorteile**: Preiswettbewerb, Diversifizierung der Backend-Instanzen, Echtzeitvergleich.



**Technologische Alternativen** (nicht SwapMarket-kompatibel): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Diese Lösungen verwenden ihre eigenen Implementierungen von Submarine Swaps.



**Empfehlung**: Verwenden Sie der Einfachheit halber Boltz Exchange oder SwapMarket, um die Kosten durch Wettbewerb zu optimieren. Beide sind in Bezug auf die Sicherheit gleichwertig (HTLC ohne Freiheitsentzug).



## Schlussfolgerung



SwapMarket erleichtert den Bitcoin/Lightning-Austausch, indem es mehrere Anbieter zu einem einzigen Interface zusammenfasst. Die HTLC-Architektur garantiert die Nicht-Kustodialität von Swaps, das Fehlen von KYC bewahrt die Vertraulichkeit und der selbst-hostbare Open-Source-Code stärkt den Widerstand gegen Zensur.



Der Wettbewerb zwischen den Anbietern verbessert die Preise und vervielfältigt die Liquiditätsquellen. Um die Verwaltung von zwei Layer zu optimieren (On-Chain Einsparungen, Blitzkosten), ist SwapMarket ein praktisches Instrument, das die Finanzhoheit und die Vertraulichkeit bewahrt.



## Ressourcen



### Offizielle Dokumentation




- [SwapMarket - Webanwendung](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Technische Dokumentation] (https://docs.boltz.Exchange/)
- [Leitfaden zur Selbstverwaltung](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Verwandte Projekte




- [Boltz Exchange](https://boltz.Exchange) - Original-Atomtauschdienst
- [ZEUS Swaps](https://zeusln.com) - Anbieter von Blitz-Swaps