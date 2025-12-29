---
name: SwapMarket
description: Bitcoin und Lightning Swap Services Aggregator
---

![cover](assets/cover.webp)



Der Transfer von Geldern zwischen Bitcoin on-chain und Lightning Network erfordert in der Regel entweder die manuelle Öffnung von Lightning-Kanälen (technisch und kostspielig) oder die Nutzung zentralisierter Swap-Plattformen mit KYC. SwapMarket bietet eine Alternative: vertrauenslose atomare Swaps über wettbewerbsfähige Anbieter, ohne KYC.



Innovation: Obwohl die Anbieter Vermittler sind, garantieren HTLC (*Hash Time Locked Contracts*) mathematisch, dass Ihre Mittel unter Ihrer Kontrolle bleiben. Der Zusammenschluss mehrerer Anbieter (Boltz, ZEUS Swaps, Eldamar, Middle Way) schafft Preiswettbewerb. Interface web open-source selbst-hostbar.



## Was ist SwapMarket?



SwapMarket ist ein Open-Source-Aggregator, der 2024 eingeführt wurde und als Vergleicher von Bitcoin/Lightning-Swap-Anbietern fungiert. Der Nutzer vergleicht sofort die Konditionen (Gebühren, Liquidität, Limits) und wählt den optimalen Anbieter aus.



### Technische Architektur



**Frontend clientseitig**: 100% clientseitige Anwendung (fork Boltz Web App) gehostet auf GitHub Pages. Code läuft im Browser ohne Backend-Server. Verlauf wird lokal gespeichert (Cookies/Cache). Öffentlicher und überprüfbarer Quellcode.



**Provider-Ermittlung** : Hardcodierte Liste in `src/configs/mainnet.ts`. Neue Anbieter können per Pull Request oder E-Mail hinzugefügt werden.



**Unabhängige Backends**: Jeder Anbieter betreibt sein eigenes Boltz-Backend. Die Schnittstelle fragt die APIs in Echtzeit ab, um Angebote sofort zu vergleichen.



**HTLC Atomare Swaps**: Hash Time Locked Contracts garantieren Atomarität: entweder wird der Swap ausgeführt, oder jede Partei erhält ihr Geld zurück. Das Kontrahentenrisiko wird mathematisch eliminiert.



### Philosophie



SwapMarket reduziert die Zentralisierung durch die Schaffung von Wettbewerb zwischen Anbietern für Gebühren und Liquidität. Keine KYC, Open-Source-Code, der selbst gehostet werden kann, Vervielfältigung unabhängiger Betreiber zur Vermeidung von Single Points of Failure.



## Hauptmerkmale



### Anbieter-Marktplatz



Die Schnittstelle zeigt alle aktiven Anbieter an: Name des Anbieters, angewandte Gebühren (prozentual und/oder fest), verfügbare Mindest-/Höchstbeträge und unterstützte Swap-Typen. Die Anwendung fragt direkt die APIs der einzelnen in der Konfigurationsdatei angegebenen Anbieter ab, um die Kurse in Echtzeit abzurufen. Der Wettbewerb zwischen den Anbietern garantiert optimale Zinssätze, die im Allgemeinen bei 0,5 % für Standard-Swaps liegen.



### Bidirektionale Swaps



**Swap-in (on-chain → Lightning)**: Konvertieren Sie on-chain BTCs in Lightning-Satoshis. Anwendungsfall: Betreiben Sie einen mobilen wallet Lightning, erhalten Sie eingehende Kapazität auf einem Knoten oder haben Sie sofortige Liquidität.



**Swap-out (Lightning → on-chain)**: Konvertiert Lightning-Satoshis in on-chain BTC. Anwendungsfall: Leeren eines wallet Lightning in den kalten Speicher oder Ausgleich der Liquidität zwischen den Schichten.



### Sicherheit und Wiederherstellung



**Trustless-Atomtausch**: HTLCs garantieren, dass entweder der Tausch in vollem Umfang abgeschlossen wird oder jede Partei ihren Einsatz zurückerhält. Das Kontrahentenrisiko wird mathematisch eliminiert.



**Rückzahlungsmechanismus**: Jeder Swap ist mit einer Zeitsperre versehen. Wenn der Swap scheitert, werden die Gelder automatisch nach Ablauf der Zeit zurückerstattet. Der Nutzer behält immer die Möglichkeit, seine Bitcoins zurückzufordern.



**Wiederherstellungsschlüssel**: Mit SwapMarket können Sie Wiederherstellungsschlüssel für laufende Swaps exportieren. Im Falle eines Problems können diese Schlüssel verwendet werden, um einen Swap von einem beliebigen Gerät aus abzuschließen oder abzubrechen.



## Installation und Zugang



### Interface Web



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



Die Anwendung wird unter `http://localhost:3000` zugänglich sein. Das Self-Hosting garantiert die vollständige Kontrolle über die Schnittstelle, eliminiert das Risiko der Zensur der offiziellen Domain und ermöglicht die Überprüfung des Quellcodes vor der Ausführung.



### Erstmalige Konfiguration



**Wallet Lightning**: Vergewissern Sie sich, dass Sie einen betriebsbereiten wallet Lightning (Phoenix, Zeus, BlueWallet usw.) haben. Für Swap-Ins werden Sie generate eine Lightning-Rechnung erhalten. Für Swap-outs zahlen Sie eine Lightning-Rechnung.



**Wallet on-chain**: Für Swap-Ins benötigen Sie einen wallet Bitcoin on-chain, um Geld zu senden. Für Swap-outs bereiten Sie eine Bitcoin-Empfangsadresse vor.



**Optionale Konfiguration**: SwapMarket speichert den Tauschverlauf und die Präferenzen in Browser-Cookies. Keine Kontoerstellung erforderlich.



## Zugriff auf Einstellungen und Rettungsschlüssel



Bevor Sie Ihre ersten Swaps vornehmen, empfehlen wir Ihnen dringend, Ihren **Rescue Key** herunterzuladen. Mit diesem Notfallschlüssel können Sie Ihr Guthaben im Falle eines technischen Problems oder des Verlusts des Zugangs zu Ihrem Gerät wiederherstellen.



### Zugangsparameter



Klicken Sie auf der SwapMarket-Hauptseite auf das Zahnradsymbol (⚙️) oben rechts auf der Oberfläche neben dem Tauschformular.



![Accès aux paramètres](assets/fr/01.webp)



### Seite Einstellungen



Die Seite Einstellungen wird geöffnet, auf der mehrere Konfigurationsoptionen angezeigt werden:





- Denominierung**: Wahlweise BTC oder sats
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



### Auswechseln: Blitz → Bitcoin



Dieses erste Beispiel zeigt, wie man Lightning-Satoschis in on-chain-Bitcoins umwandelt.



**Schritt 1: Konfiguration austauschen



Wählen Sie auf der Hauptseite das Tauschformular aus:




- LIGHTNING** (oberes Feld): Geben Sie den Betrag ein, den Sie in sats Lightning senden möchten (Beispiel: 30.000 sats)
- BITCOIN** (unteres Feld): Der Betrag, den Sie erhalten, wird automatisch nach Abzug der Gebühren angezeigt (Beispiel: 29.320 sats)



Fügen Sie in das untere Feld Ihre **Empfangs-Bitcoin-Adresse** ein, an die Sie das Geld überweisen möchten. Prüfen Sie diese Adresse sorgfältig.



Der Standardanbieter ist in der Regel Boltz Exchange. Die Netz- und Anbietergebühren werden deutlich angezeigt.



![Configuration swap-out](assets/fr/03.webp)



**Schritt 2: Auswahl des Anbieters**



Klicken Sie auf das Dropdown-Menü des Anbieters (Standard: "Boltz Exchange"), um alle verfügbaren Liquiditätsanbieter anzuzeigen.



Es öffnet sich ein modales Fenster, in dem eine Vergleichstabelle angezeigt wird:




- Status**: Green-Anzeige, wenn der Anbieter aktiv ist
- Alias**: Name des Anbieters (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Gebühr**: Vom Anbieter erhobene Gebühren (im Allgemeinen zwischen 0,49 % und 0,5 %)
- Max Swap**: Maximal akzeptierter Betrag für einen Swap



Vergleichen Sie Gebühren und Höchstbeträge und wählen Sie dann den Anbieter Ihrer Wahl.



**Bitte beachten**: Die Schnittstelle zur Anbieterauswahl zeigt nicht die **Mindestbeträge** für jeden Anbieter an. Diese Information erscheint nur in der Schnittstelle zur Swap-Erstellung, nachdem ein Anbieter ausgewählt wurde. Die Mindest- und Höchstbeträge können von Anbieter zu Anbieter variieren und sich im Laufe der Zeit ändern. **Wenn der Betrag, den Sie tauschen möchten, außerhalb der Grenzen eines Anbieters liegt, können Sie einen anderen Anbieter wählen, der für Ihre Transaktion besser geeignet ist.



![Sélection du provider](assets/fr/04.webp)



**Schritt 3: Swap-Erstellung und Blitzzahlung**



Klicken Sie auf die gelbe Schaltfläche **"ATOMIC SWAP ERSTELLEN "**. SwapMarket wird generate eine **Lightning-Rechnung** (BOLT11) erstellen, die Sie mit Ihrem wallet Lightning bezahlen können.



Die Seite zeigt an:




- Swap-ID**: Eindeutige Swap-Kennung (Beispiel: J4ymFIMVR6Hm)
- Status**: "swap.created" (Swap erstellt, wartet auf Zahlung)
- QR-Code**: Scannen Sie ihn mit Ihrem wallet Lightning
- Invoice Lightning**: Zeichenfolge, die mit "lnbc" beginnt (Beispiel: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Bezahlen Sie diese Rechnung mit Ihrem wallet Lightning (Phoenix, Zeus, BlueWallet, etc.). Der genaue zu zahlende Betrag wird angezeigt (Beispiel: 30.000 sats).



![Paiement Lightning](assets/fr/05.webp)



**Schritt 4: Bestätigung und Annahme**



Sobald die Lightning-Zahlung bestätigt wurde, erhält SwapMarket sofort Ihre Zahlung und der Anbieter sendet die Bitcoin-Transaktion an Ihre Adresse.



Der Status ändert sich in **"Rechnung.beglichen "** (Rechnung bezahlt), und es wird eine Bestätigungsmeldung angezeigt.



Ihre on-chain-Bitcoins sind verfügbar, sobald die Transaktion bestätigt wurde (in der Regel ein paar Minuten bis ein paar Stunden, je nach den vom Anbieter gewählten mining-Gebühren).



![Confirmation swap-out](assets/fr/06.webp)



Sie können auf **"OPEN CLAIM TRANSACTION "** klicken, um die Bitcoin-Transaktion in einem Blockchain-Browser anzuzeigen.



### Einwechseln: Bitcoin → Lightning



Dieses zweite Beispiel zeigt, wie man on-chain Bitcoins in Lightning-Satoshis umwandelt.



**Schritt 1: Konfiguration austauschen



Wählen Sie auf der Hauptseite das Tauschformular aus:




- BITCOIN** (oberes Feld): Geben Sie den Betrag ein, den Sie in sats Bitcoin senden möchten (Beispiel: 63.400 sats)
- LIGHTNING** (unteres Feld): Der Betrag, den Sie erhalten, wird automatisch nach Abzug der Gebühren angezeigt (Beispiel: 62 884 sats)



Fügen Sie in das untere Feld eine Lightning**-Rechnung (BOLT11) ein, die von Ihrem wallet Lightning erstellt wurde, oder verwenden Sie Ihre LNURL-Adresse, wenn Ihr wallet dies unterstützt.



![Configuration swap-in](assets/fr/07.webp)



**Schritt 2: Prüfung des Rettungsschlüssels**



Nachdem Sie auf **"ATOMIC SWAP ERSTELLEN "** geklickt haben, erscheint ein modales Fenster, in dem Sie aufgefordert werden, Ihren Rescue Key zu bestätigen.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rettungsschlüssel**: Da Sie Ihren Rettungsschlüssel bereits bei der Erstkonfiguration hochgeladen haben (siehe vorheriger Abschnitt), klicken Sie auf die Schaltfläche **"VERIFY EXISTING KEY "**, um den von Ihnen gespeicherten Schlüssel zu importieren.



Wählen Sie die zuvor heruntergeladene Rescue Key-Datei aus. Nach erfolgreicher Überprüfung wechselt die Schnittstelle automatisch zum nächsten Schritt.



**Schritt 3: Bitcoin** Hinterlegungsadresse



SwapMarket generiert jetzt eine **einzigartige Bitcoin-Adresse**, die den mit Ihrer Lightning-Rechnung verknüpften HTLC-Vertrag enthält.



Die Seite zeigt an:




- Swap-ID**: Eindeutige Kennung (Beispiel: 1kGmB6JyGqU4)
- Status**: "Rechnung.eingestellt" (Rechnung eingestellt, wartet auf Zahlung Bitcoin)
- QR-Code**: Bitcoin-Depot-Adresse
- Bitcoin**-Adresse: Beginnt normalerweise mit "bc1p..." (Beispiel: bc1p5mvtwxapjkds...9d4n9f)
- Warnung in gelb** : "Stellen Sie sicher, dass Ihre Transaktion innerhalb von ~24 Stunden nach der Erstellung dieses Swaps bestätigt wird!"



Dieser Zeitraum von ~24 Stunden ist der **Timeout** des HTLC-Vertrags. Wenn Ihre Bitcoin-Transaktion nicht innerhalb dieses Zeitrahmens bestätigt wird, schlägt der Swap fehl und Sie müssen Ihren Rescue Key verwenden, um Ihr Geld zurückzuerhalten.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Sie können die Adresse kopieren, indem Sie auf die Schaltfläche **"ADRESSE "** klicken, oder den QR-Code direkt von Ihrem wallet on-chain scannen.



**Schritt 4: Bitcoins senden**



Senden Sie von Ihrem wallet Bitcoin on-chain **genau** den angegebenen Betrag (z.B. 63.400 sats) an die generierte Adresse.



**Wichtig**: Verwenden Sie angemessene mining-Gebühren, um eine schnelle Bestätigung zu gewährleisten. Wenn die Gebühr zu niedrig ist und die Transaktion über den Timeout (~24h) hinaus im Mempool verbleibt, wird der Swap fehlschlagen.



Sobald die Transaktion gesendet wurde, erkennt SwapMarket, dass sie sich im Mempool befindet und zeigt an:




- Status** : "Transaktion.mempool
- Meldung**: "Transaktion ist im Mempool - Warte auf Bestätigung, um den Swap abzuschließen"



![Transaction en mempool](assets/fr/10.webp)



**Schritt 5: Bestätigung und Blitzempfang



Sobald die Bitcoin-Transaktion ihre erste Bestätigung erhält, bezahlt der Anbieter automatisch Ihre Lightning-Rechnung. Sie erhalten die Satoshis sofort auf Ihrem wallet Lightning.



Der Status ändert sich zu **"Transaktion.Anspruch.ausstehend "**, dann wird eine Bestätigungsmeldung angezeigt:



![Confirmation swap-in](assets/fr/11.webp)



Ihre Lightning-Satoshis sind sofort in Ihrem wallet verfügbar.



## Vorteile und Grenzen



### Vorteile



**Tarifwettbewerb**: Durch die Zusammenlegung von Anbietern entsteht ein natürlicher Wettbewerb, der die Gebühren nach unten zieht (0,49 % bis 0,5 %).



**Vertraulichkeit**: Keine KYC, 100% clientseitige Schnittstelle (keine Übertragung persönlicher Daten), Tor-Browser kompatibel.



**Nicht sorgeberechtigt**: HTLC garantieren mathematisch die alleinige Kontrolle über Ihr Geld. Entweder der Swap gelingt, oder Sie erhalten Ihre Bitcoins zurück.



**Open-Source-Self-Hosting**: überprüfbarer öffentlicher Code, der lokal eingesetzt werden kann, um möglichst unempfindlich gegen Zensur zu sein.



### Beschränkungen



**Begrenzte Liquidität**: Begrenzte Anzahl von aktiven Anbietern (Boltz, Eldamar, MiddleWay je nach Zeitraum). Die Höchstbeträge können begrenzt sein.



**Ablaufzeit**: Zeitüberschreitung von 24h bis 48h. Wenn die on-chain-Transaktion nicht vor Ablauf bestätigt wird, ist eine manuelle Wiederherstellung erforderlich.



**Interface-Zentralisierung**: Obwohl die offizielle Schnittstelle selbst gehostet werden kann, wird sie auf GitHub Pages gehostet. Wenn GitHub das Repo zensiert, wird der Zugriff über swapmarket.github.io blockiert (Lösung: Selbst-Hosting).



**on-chain-Spuren**: HTLC-Skripte sind potenziell durch fortgeschrittene Blockchain-Analyse identifizierbar.



## Bewährte Praktiken



### Sichere Konfiguration



**Laden Sie Ihren Rescue Key herunter**: Laden Sie vor Ihren ersten Swaps Ihren Rescue Key aus den Einstellungen herunter (siehe entsprechender Abschnitt oben). Dieser einmalige Schlüssel gilt für alle zukünftigen Swaps und ermöglicht es Ihnen, Ihr Guthaben im Falle eines Problems wiederherzustellen.



**Tor-Browser verwenden**: Für maximale Vertraulichkeit greifen Sie auf SwapMarket über den Tor-Browser zu, um Ihre IP-Adresse zu verbergen.



**Erwägen Sie Selbst-Hosting**: Für technische Benutzer, die ihre eigene SwapMarket-Instanz betreiben, entfällt die Abhängigkeit von der offiziellen GitHub Pages-Domäne.



### Optimierung der Auslagerung



**Behalten Sie den Mempool im Auge**: Überprüfen Sie mempool.space vor einem Swap-In. Wählen Sie Zeiten mit geringer Aktivität, um die mining-Kosten zu minimieren.



**Überprüfen Sie die Adressen**: Prüfen Sie bei der Auslagerung Ihre Empfangsadresse genauestens. Verwenden Sie "Kopieren und Einfügen" und überprüfen Sie die ersten 5 und die letzten 5 Zeichen.



**Testen Sie mit kleinen Mengen**: Beginnen Sie mit dem erlaubten Minimum (25.000 bis 50.000 sats). Erhöhen Sie die Menge schrittweise, sobald Sie das Verfahren beherrschen.



**Dokumentieren Sie Ihre Swaps**: Notieren Sie sich für jeden Swap die ID, die Einlösungsadresse und das Ablaufdatum. Diese Informationen erleichtern die Rückverfolgung und Wiederherstellung im Falle eines technischen Problems.



### Strategie für die Nutzung



**Balancieren Sie Ihren Cashflow**: Nutzen Sie SwapMarket, um Ihre Aufteilung zwischen on-chain (Sparen, langfristige Sicherheit) und Lightning (tägliche Ausgaben, sofortige Zahlungen) entsprechend Ihren tatsächlichen Bedürfnissen anzupassen.



**Berechnen Sie die Rentabilität**: Vergleichen Sie bei dauerhaftem Lightning-Liquiditätsbedarf die kumulierten Kosten wiederholter Swaps mit denen der direkten Eröffnung eines Lightning-Kanals. SwapMarket eignet sich hervorragend für einmalige Anpassungen, nicht unbedingt für große regelmäßige Ströme.



## SwapMarket vs. Boltz: Was ist der Unterschied?



### Boltz: Technik vs. Dienstleistung



**Boltz ist die Open-Source-Technologie** (`boltz-backend` auf GitHub), die atomare Tauschvorgänge über HTLC zwischen Bitcoin, Lightning und Liquid implementiert.



**Kritischer Punkt**: Alle SwapMarket-Anbieter (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) setzen ihre eigene Instanz des Boltz-Backends ein. Die zugrunde liegende Technologie ist daher identisch. Eine Schwachstelle im Boltz-Backend würde potenziell alle Anbieter betreffen, aber der Open-Source-Charakter des Systems ermöglicht eine Überprüfung durch die Gemeinschaft.



**Boltz Exchange** ist ein einzelner Dienst, der vom Boltz-Team betrieben wird, während **SwapMarket** mehrere Anbieter zusammenbringt, die alle die Boltz-Technologie nutzen und so ein wettbewerbsfähiges Preisumfeld schaffen.



Weitere Einzelheiten finden Sie in unseren Anleitungen zu Boltz und Zeus Swap:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Wesentliche Unterschiede



| Aspekt       | Boltz Exchange       | SwapMarket                           |
| ------------ | -------------------- | ------------------------------------ |
| Art           | Einzigartiger Dienst | Multi-Provider-Aggregator             |
| Anbieter      | Nur Boltz            | Boltz, ZEUS, Eldamar, Middle Way     |
| Wettbewerb    | Feste Gebühren       | Freier Wettbewerb                    |
| Schnittstelle | boltz.exchange       | swapmarket.github.io (selbst hostbar) |
| Sicherheit    | Non-custodial (HTLC) | Non-custodial (HTLC)                 |

**SwapMarket-Vorteile**: Preiswettbewerb, Diversifizierung der Backend-Instanzen, Echtzeitvergleich.



**Technologische Alternativen** (nicht SwapMarket-kompatibel): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Diese Lösungen verwenden ihre eigenen Implementierungen von Submarine Swaps.



**Empfehlung**: Verwenden Sie der Einfachheit halber Boltz Exchange oder SwapMarket, um die Kosten durch Wettbewerb zu optimieren. Beide sind in Bezug auf die Sicherheit gleichwertig (HTLC ohne Freiheitsentzug).



## Schlussfolgerung



SwapMarket erleichtert Bitcoin/Lightning-Tauschgeschäfte, indem es mehrere Anbieter in einer einzigen Schnittstelle zusammenfasst. Die HTLC-Architektur garantiert die Nicht-Kustodialität von Swaps, das Fehlen von KYC wahrt die Vertraulichkeit und der selbst-hostbare Open-Source-Code stärkt die Resistenz gegen Zensur.



Der Wettbewerb zwischen den Anbietern verbessert die Kurse und vervielfacht die Liquiditätsquellen. Um die Verwaltung auf zwei Ebenen zu optimieren (on-chain-Einsparungen, Blitzkosten), ist SwapMarket ein praktisches Instrument, das die Finanzhoheit und die Vertraulichkeit bewahrt.



## Ressourcen



### Offizielle Dokumentation




- [SwapMarket - Webanwendung](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Technische Dokumentation](https://docs.boltz.exchange/)
- [Leitfaden zur Selbstverwaltung](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Verwandte Projekte




- [Boltz Exchange](https://boltz.exchange) - Original-Atomtauschbörse
- [ZEUS Swaps](https://zeusln.com) - Anbieter von Blitztauschbörsen