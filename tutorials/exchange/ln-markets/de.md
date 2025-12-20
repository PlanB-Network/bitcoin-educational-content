---
name: LN Markets
description: Bitcoin Handelsplattform auf Lightning Network
---

![cover](assets/cover.webp)



LN Markets ist die erste wirklich Lightning-native Bitcoin-Handelsplattform, die es Ihnen ermöglicht, gehebelte Bitcoin-Derivate direkt von Ihrem wallet-Lightning aus zu handeln, ohne KYC, mit sofortiger Abrechnung und minimaler Verwahrung. Die 2020 eingeführte Plattform beseitigt die Reibungen traditioneller Börsen: keine Identitätsüberprüfung, keine blockierten Einlagen, kein Warten auf Blockchain-Bestätigungen. Ihr wallet Lightning wird zu Ihrem Handelskonto.



## Was ist LN Markets?



LN Markets bietet **Futures** (unbefristete Verträge mit einer Hebelwirkung von bis zu 100×) und **Optionen** (Call/Put mit einem auf die gezahlte Prämie begrenzten Risiko). Die Plattform fungiert als Liquiditätsaggregationsschicht, die mehrere Handelsplätze konsolidiert, um eine optimale Zero-Slippage-Ausführung zu gewährleisten. Ihre Gelder sind nur für die exakte Dauer Ihrer aktiven Positionen gebunden, nicht für Tage oder Wochen wie bei einem herkömmlichen Depotkonto.



### Verfügbare Handelsprodukte



**Futures (unbefristete Verträge)**



Perpetual-Kontrakte sind Futures ohne Verfallsdatum, die es Ihnen ermöglichen, mit Hebelwirkung auf die Bitcoin-Preisentwicklung zu spekulieren. LN Markets bietet zwei Margin-Management-Modi:



**Isolierter Modus**: Jede Position hat ihre eigene Marge. Nur die Mittel, die dieser spezifischen Position zugewiesen wurden, sind einem Risiko ausgesetzt. Wenn die Position den Liquidationspreis erreicht, wird **nur diese Position liquidiert**, Ihre anderen Positionen und Ihr Restguthaben sind davon nicht betroffen. Ideal für die strikte Begrenzung des Risikos pro Handel.



**Cross-Modus (Cross Margin)** : Die Marge wird auf alle Ihre offenen Positionen aufgeteilt. Ihr gesamter Kontostand dient als Sicherheit für alle Ihre Positionen. Wenn eine Position ausfällt, greift das System auf Ihr gesamtes verfügbares Guthaben zurück, um eine Liquidation zu vermeiden. **Risiko**: Wenn Ihr Gesamtguthaben erschöpft ist, können alle Ihre Positionen gleichzeitig liquidiert werden. Nur für erfahrene Händler empfohlen, die ihre Kapitaleffizienz maximieren wollen.



**Positionsmanagement** :





- Long-Position**: Sie wetten auf den Anstieg von BTC/USD. Wenn der Preis steigt, gewinnen Sie; wenn er fällt, verlieren Sie. **Beispiel**: Bitcoin steht bei 100.000 $, Sie eröffnen eine Long-Position mit 10.000 sats und 10× Hebelwirkung. Wenn Bitcoin auf $105.000 (+5%) steigt, gewinnt Ihre Position 50% (5% × 10), d.h. ~5.000 sats Gewinn. Wenn Bitcoin auf 95.000 $ fällt (-5%), verlieren Sie 50%, d.h. einen Verlust von ~5.000 sats.





- Short-Position**: Sie wetten darauf, dass BTC/USD fällt. Wenn der Kurs fällt, gewinnen Sie; wenn er steigt, verlieren Sie. **Beispiel**: Bitcoin steht bei 100.000 $, Sie eröffnen eine Short-Position mit 10.000 sats und 10× Hebelwirkung. Wenn Bitcoin auf $95.000 (-5%) fällt, gewinnen Sie 50%, d.h. ~5.000 sats. Steigt Bitcoin auf 105.000 $ (+5%), verlieren Sie 50%.



Die Hebelwirkung (bis zum 100-fachen) verstärkt Gewinne und Verluste proportional. Ein **Funding Rate**-Mechanismus (periodische Gebühren alle 8 Stunden) gleicht Long- und Short-Positionen aus. Sie können bis zu 100 Futures-Positionen gleichzeitig verwalten.



**Optionen**



Eine Option ist wie ein **Lotterieschein mit Verfallsdatum**. Sie zahlen eine Prämie, um auf die Richtung des Bitcoin-Kurses zu wetten. **Großer Vorteil**: Sie können nie mehr als die gezahlte Prämie verlieren, keine Liquidation möglich.





- Call-Option (bullische Wette)**: Sie wetten darauf, dass Bitcoin vor Ablauf der Frist über den Basispreis steigen wird. Sie gewinnen, wenn der Preis steigt, und verlieren nur die Prämie, wenn der Preis fällt.





- Put-Option (bärische Wette)**: Sie wetten, dass Bitcoin unter den Basispreis fallen wird. Sie gewinnen, wenn der Preis fällt, und verlieren nur die Prämie, wenn der Preis steigt.





- Straddle (Volatilitätswette)**: Sie kaufen einen Call UND einen Put gleichzeitig. Sie gewinnen, wenn Bitcoin eine große Bewegung in irgendeine Richtung macht, Sie verlieren beide Prämien, wenn der Preis stabil bleibt.



Limit: 50 gleichzeitige Positionen. Ideal für den Einstieg in den gehebelten Handel ohne Angst vor Liquidation.



**sats ↔ sUSD**: Konvertieren Sie Ihre Satoshis sofort in synthetische Dollar (sUSD), um sich vor der Volatilität zu schützen, oder umgekehrt, um das Bitcoin-Engagement wiederherzustellen.



## Plattformzugang und Kontoerstellung



### Weiter zu LN Markets



Gehen Sie zu [lnmarkets.com](https://lnmarkets.com) und klicken Sie auf "App öffnen".



![Page d'accueil LN Markets](assets/fr/01.webp)



### Ihr Konto erstellen



Auf dem Begrüßungsbildschirm werden mehrere Verbindungsmethoden angeboten:



![Méthodes de connexion](assets/fr/02.webp)



**Optionen verfügbar** :


1. **Registrieren Sie sich mit einem Lightning wallet** (empfohlen): LNURL-Authentifizierung mit Phoenix, Breez, Zeus oder BlueWallet


2. **Registrieren Sie sich mit E-Mail**: klassisches Konto (schränkt die Lightning-Erfahrung ein)


3. **Alby** oder **Ledger**: Browser-Erweiterungen



### Verbindung über Lightning (LNURL-auth)



Klicken Sie auf "Registrieren mit einem Lightning wallet". Scannen Sie den QR-Code mit Ihrem wallet Lightning:



![QR code LNURL-auth](assets/fr/03.webp)



Ihr wallet unterzeichnet automatisch eine kryptografische Anfrage und Ihr Konto wird sofort erstellt, ohne E-Mail oder Passwort. Starke Sicherheit und absolute Anonymität.



### Erstmalige Konfiguration



![Configuration post-connexion](assets/fr/04.webp)



**Verfügbare Parameter** :




- Benutzername**: personalisieren Sie Ihren Benutzernamen
- Automatische Abhebungen**: Aktivieren Sie automatische Abhebungen auf Ihr wallet nach Handelsschluss
- Zwei-Faktor-Authentifizierung**: verbesserte Sicherheit mit 2FA
- Dokumentation**: Zugang zu offiziellen Ressourcen



## Interface-Tour



Die Oberfläche des LN Markets ist in mehrere Abschnitte unterteilt, die über das Seitenmenü zugänglich sind:



### Dashboard



![Dashboard](assets/fr/06.webp)



Zeigt Ihre Performance nach Produkttyp (Futures Cross, Futures Isolated, Optionen) mit P&L, gehandelten Volumina und Ihrem persönlichen Address Lightning (z.B. `pivi@lnmarkets.com`).



### Profil



![Profil trader](assets/fr/07.webp)



Detaillierte Statistiken: Anzahl der Trades, Händlertyp (SCALPER, etc.), mittlere Positionsdauer, Long/Short-Aufteilung, Gewinnrate, Durchschnittswerte (Menge, Margin, Leverage) und progressive Gebührenstruktur je nach Volumen.



### Berufe



![Historique des trades](assets/fr/08.webp)



Die Registerkarte "Trades" zeigt eine vollständige Historie Ihrer Positionen mit allen wichtigen Metriken: Erstellungsdatum, Richtung (Long/Short), Positionsgröße (Menge), zugesagte Marge, Einstiegs- und Ausstiegskurs, realisierter Gewinn/Verlust (P&L) und Handelsgebühren. Sie können nach Produkttyp (Futures/Optionen) filtern und Ihre Daten für externe Analysen oder Buchhaltung exportieren.



### Einstellungen



![Paramètres de la plateforme](assets/fr/05.webp)



Die Registerkarte Einstellungen bietet zwei Registerkarten: **Konto** und **Interface**.



*registerkarte *Konto**:



Kontoverwaltung mit bearbeitbaren Feldern :




- Benutzername**: Ändern Sie Ihren Benutzernamen (z.B. "pivi") mit der Schaltfläche "Aktualisieren"
- E-Mail**: Ihre E-Mail-Adresse hinzufügen/bearbeiten
- Einzahlungs-Bitcoin-Adresse**: die Bitcoin-Adresse, die Sie für die Einzahlung von on-chain-Geldern verwenden können.



**Drei Konfigurationsschaltflächen** :




- In Bestenlisten** erscheinen: Wählen Sie, ob Sie in öffentlichen Bestenlisten erscheinen wollen oder nicht
- Taproot-Adressen verwenden**: Bitcoin-Adressen verwenden Taproot für on-chain-Einzahlungen/Abhebungen
- Automatische Abhebungen aktivieren**: Aktivieren Sie automatische Abhebungen auf Ihren wallet Lightning nach Abschluss des Geschäfts



**Kontomigration**: Abschnitt, in dem Sie Ihr Lightning-Konto auf die klassische E-Mail/Passwort-Authentifizierung umstellen können.



**Session Verwaltung**: schaltfläche "Sitzung und lokale Daten löschen", um die Verbindung zu trennen und die lokalen Browserdaten zu löschen.



*registerkarte *Interface**:



Passen Sie das Benutzererlebnis mit sieben Umschaltern an:




- Auftragsbestätigung überspringen**: Deaktivieren des Bestätigungsmodals vor der Handelsausführung (schneller Handel)
- Tooltips anzeigen**: Tooltips anzeigen, wenn der Mauszeiger über Elemente bewegt wird
- Privater Modus (maskiert sensible Daten)**: maskiert Beträge und sensible Daten in der Schnittstelle (Datenschutzmodus)
- Netto-PL im Profil anzeigen**: Nettogewinn/-verlust in Ihrem öffentlichen Profil anzeigen
- Einheitensymbole** verwenden: Anzeige von Symbolen für Währungseinheiten (sats, $)
- Tonbenachrichtigungen aktivieren**: Aktivieren Sie Tonbenachrichtigungen für Handelsereignisse
- Desktop-Benachrichtigungen aktivieren**: Desktop-Benachrichtigungen des Betriebssystems aktivieren



### Wallet



![Wallet](assets/fr/09.webp)



Bitcoin und synthetische USD-Salden mit der Historie von Einzahlungen, Abhebungen, Querüberweisungen, Swaps, Finanzierungen und on chain-Adressverwaltung.



### API



![API V3](assets/fr/10.webp)



LN Markets bietet ein komplettes API REST (V2 und V3), um Ihren Handel über Skripte oder Bots vollständig zu automatisieren. Sie können API-Schlüssel mit anpassbaren Berechtigungen (schreibgeschützt, Handel, Abhebungen) direkt über die Schnittstelle erstellen. Offizielle TypeScript und Python SDKs sind für eine einfache Integration verfügbar. Die vollständige API V3 Dokumentation ist unter [api.lnmarkets.com/v3](https://api.lnmarkets.com/v3) verfügbar.



## Erste Einzahlung von Geldern



Klicken Sie auf "Einzahlung". Drei Methoden sind verfügbar:



![Modal de dépôt](assets/fr/11.webp)



1. **LNURL**: Scannen Sie den QR-Code mit Ihrem wallet Lightning


2. **Invoice**: Geben Sie einen Betrag ein und scannen Sie die Lightning-Rechnung


3. **On-Chain**: Betriebshof Bitcoin on chain



## Handel in der Praxis



### Trade Futures Long: Wetten auf den Aufwärtstrend



Klicken Sie auf dem Dashboard auf "Futures" und dann auf "Isoliert". Klicken Sie auf **"Kaufen "**, um eine Long-Position zu eröffnen.



![Interface Futures Long](assets/fr/12.webp)



Klicken Sie auf das Symbol **Rechner** neben der Schaltfläche "Kaufen", um den Positionsrechner anzuzeigen:



![Calculateur de position Long](assets/fr/13.webp)



**Konkretes Beispiel** :




- Menge**: $100 (Positionsgröße)
- Handelsspanne**: 12.336 sats (gebundene Marge)
- Hebelwirkung**: 7.73× (jede Veränderung von 1% BTC = 7,73% auf Ihr Kapital)
- Einstiegspreis** : $104,863.5
- Liquidation**: 92.852 $ (kritischer automatischer Liquidationspreis)
- Ausstiegspreis**: 110.000 $ (für die Gewinnberechnung)
- PL** : 4.492 sats (Gewinn bei Ausstieg zu 110.000 $)



**Szenarien** :




- Anstieg +4,9%** ($110.000) : +4.492 sats Gewinn (+36,4%)
- Neutral** ($104.863) : -185 sats (nur Gebühren)
- Rückgang um -11,5%** (92.852 $): vollständige Liquidation (-100%)



Klicken Sie auf die Schaltfläche "Kaufen", um den Handel zu bestätigen. **Zwei mögliche Fälle** :





- Wenn Sie über ausreichend Liquidität** auf Ihrem Konto verfügen: Es wird direkt ein Bestätigungsfenster angezeigt (siehe Abbildung unten). Klicken Sie auf "Ja", um den Handel sofort auszuführen.



![Confirmation trade Long](assets/fr/14.webp)





- Wenn Sie nicht genug Bargeld** haben: Stattdessen wird ein Lightning-QR-Code angezeigt. Scannen Sie ihn mit Ihrem wallet Lightning, um die erforderliche Marge zu zahlen. Der Handel wird nach Zahlungseingang automatisch eröffnet



### Trade Futures Short: Wetten auf den Abwärtstrend



Klicken Sie auf **"Verkaufen "**, um eine Short-Position zu eröffnen (Sie gewinnen, wenn der Preis fällt). Öffnen Sie den Taschenrechner mit dem Taschenrechner-Symbol, um Ihre Position einzurichten:



![Calculateur de position Short](assets/fr/15.webp)



Klicken Sie zur Bestätigung auf "Verkaufen". Für den Long sind **zwei Fälle möglich**:





- Wenn Sie über genügend Bargeld verfügen**: Direktbestätigungsmodus, klicken Sie auf "Ja"
- Wenn Sie nicht genug Bargeld** haben: Es wird ein Lightning-QR-Code angezeigt (Bild unten). Scannen Sie ihn mit Ihrem wallet Lightning, um die erforderliche Marge zu zahlen:



![Paiement Lightning pour Short](assets/fr/16.webp)



Sobald die Lightning-Zahlung eingegangen ist, wird Ihre Short-Position automatisch eröffnet. Sie können sie dann über die Handelsoberfläche verwalten.



#### Schließen einer Position



Um Ihre Position (Long oder Short) zu schließen, klicken Sie auf das **kleine Kreuz in der rechten unteren Ecke** der Verwaltungsoberfläche:



![Interface de clôture](assets/fr/17.webp)



Es wird ein Bestätigungsdialog angezeigt, um den Abschluss des Geschäfts zu bestätigen:



![Confirmation clôture](assets/fr/18.webp)



Das Modal zeigt Ihre aktuelle GuV (Gewinn oder Verlust) an. Klicken Sie zum Schließen auf "Ja". Der Saldo wird sofort über Lightning zu Ihrem Wallet addiert (Gewinn) oder von ihm abgezogen (Verlust).



### Handelsoptionen Call: bedingtes Kaufrecht



Optionen bieten ein auf die gezahlte Prämie begrenztes **Risiko**, wobei keine Liquidation möglich ist. Ein Call gibt Ihnen das Recht (nicht die Pflicht), Bitcoin vor dem Verfall zum Ausübungspreis zu kaufen. Im Gegensatz zu Futures können Sie nie mehr als die investierte Prämie verlieren.



Klicken Sie auf dem Dashboard auf "Optionen" und wählen Sie dann die Registerkarte "Anruf".



![Interface Options Call](assets/fr/19.webp)



Konfigurieren Sie Ihren Handel mit den folgenden Parametern:




- Menge**: $100 (Umfang Ihres Vertrags)
- Verfallsdatum** : 2025-11-15 (Verfallsdatum)
- Strike**: 96.000 $ (Zielpreis)



Die anderen Felder werden automatisch berechnet:




- Marge**: 1.045 sats (zu zahlende Prämie, Ihre Investition)
- Breakeven**: 96.923 $ (Preis, um Ihren Einsatz zurückzugewinnen)
- Delta**: 40 (Bitcoin Preisempfindlichkeit)



**Wie berechnet man seinen Gewinn?**



Ihr Gewinn hängt vom Bitcoin-Kurs bei Ablauf ab. Formel: **(BTC-Preis - Strike) × Contract-Größe - gezahlte Prämie**.



**konkrete Beispiele** :





- Bitcoin zu $96.000** (aktueller Kurs) : Innerer Wert = $0. **Verlust: -1.045 sats** (Sie verlieren die Prämie)





- Bitcoin zu 97.000 $**: Innerer Wert = (97.000 - 96.000) × 0,00105 BTC = 1,05 $. Umgerechnet in sats ≈ 2,175 sats. **Gewinn: 2,175 - 1,045 = +1,130 sats** (+108% Gewinn)





- Bitcoin zu $98.000**: innerer Wert = $2.000 ≈ 3.224 sats. **Gewinn: +2.179 sats** (+208% Gewinn)





- Bitcoin zu $100.000**: innerer Wert = $4.000 ≈ 5.263 sats. **Gewinn: +4.218 sats** (+403% Gewinn)





- Bitcoin unter $96.000**: Option verfällt wertlos. **Beschränkter Verlust: -1.045 sats**, keine Verwertung möglich



Klicken Sie auf "Call kaufen". Es erscheint ein Bestätigungsdialogfeld:



![Confirmation Call option](assets/fr/20.webp)



Klicken Sie zur Bestätigung erneut auf "Buy Call". Die Option erscheint in "Laufende Optionen". Bei Fälligkeit berechnet LN Markets automatisch den inneren Wert und passt Ihren Gewinn/Verlust an.



**Hinweis zu Verkaufsoptionen** : Die Funktionsweise ist identisch mit der einer Kaufoption, aber in umgekehrter Reihenfolge. Bei einem Put setzen Sie darauf, dass der Bitcoin-Preis **sinkt**. Wenn der Bitcoin unter Ihren Basispreis fällt, gewinnen Sie; wenn er darüber bleibt, verlieren Sie nur die gezahlte Prämie. Die Berechnung der Gewinne folgt der gleichen Logik: **(Strike - BTC-Preis) × Contract-Größe - gezahlte Prämie**.



### Entnahme aus dem Blitzfonds



Klicken Sie auf "Zurückziehen":



![Modal de retrait](assets/fr/21.webp)



**Methoden** : LNURL, Invoice, Lightning Address, On-Chain.



**Invoice-Verfahren** :


1. Generieren Sie eine Lightning-Rechnung von Ihrem wallet


2. Kopieren Sie die Rechnung (beginnt mit `lnbc...`)


3. Fügen Sie sie in das Feld LN Markets ein


4. Rücknahme bestätigen


5. Ihr wallet wird in 1-3 Sekunden gutgeschrieben



Keine Blitzabhebungsgebühren, nur minimale Weiterleitungsgebühren (<0,1% in der Praxis).



## Risiken und bewährte Verfahren



**Hauptrisiken** :




- Totale Liquidation**: Eine hohe Hebelwirkung kann innerhalb von Minuten 100% der Marge aufzehren
- Experimenteller Dienst**: Alpha-Phase, technologische Unsicherheiten
- Kontrahentenrisiko**: Plattform bleibt einziger Kontrahent



**Best practices** :



1. **Kapitalmanagement**: Wählen Sie eine auf Ihr Profil zugeschnittene Risikomanagementstrategie. Beispiel: Setzen Sie 5 % Ihres Gesamtvermögens für den gehebelten Handel ein und riskieren Sie maximal 1 % dieses Kapitals pro Handel (z. B.: 1 BTC Vermögen → 5 Mio. sats für den Handel → 50k sats maximales Risiko pro Position)



2. **Systematischer Stop-Loss**: Konfigurieren Sie Stop-Losses, um Ihre Verluste pro Handel zu begrenzen. Bei einer 1%-Risiko-Regel stellen beispielsweise selbst 10 aufeinanderfolgende Verlustgeschäfte nur 10% Ihres Handelskapitals dar



3. **Starten Sie klein**: Testen Sie zunächst mit einigen tausend Satelliten, um die Mechanismen zu verstehen, bevor Sie Ihre Kapitalmanagementstrategie anwenden



4. **Regelmäßige Gewinnentnahme**: Sichern Sie Ihre Gewinne auf Ihrem Haupt-wallet und lassen Sie nur das aktive Handelskapital auf der Plattform



5. **Achten Sie auf die Hebelwirkung**: Vermeiden Sie eine Hebelwirkung von mehr als dem 20-fachen, es sei denn, Sie sind sich der Liquidationsrisiken voll bewusst



**Kosten**: keine Blitzeinzahlungs- und -auszahlungsgebühren, Spread ~0,1% pro Handel (je nach Volumen bis 0,06%).



## Vorteile und Grenzen



**Vorteile** :




- Non-custodial (Gesamtkontrolle ohne Handelszeiten)
- KYC-frei (Anonymität über Lightning/Nostr)
- Sofortige Abrechnungen (Einzahlungen/Abhebungen in Sekunden)
- Ausführung zum Nulltarif mit Liquiditätsaggregation
- API öffentlich und Nostr Unterstützung



**Einschränkungen** :




- Service alpha (mögliche Entwicklungen)
- Geringere Liquidität als Binance/Deribit
- Verboten für US-Bürger



## Schlussfolgerung



LN Markets verkörpert eine bedeutende Weiterentwicklung des Bitcoin-Handels, indem Lightning Network nativ integriert wird, um den Benutzern die Kontrolle zurückzugeben. Für versierte Bitcoiner, die spekulieren möchten, ohne ihre Souveränität zu kompromittieren, ist es eine einzigartige Alternative zu traditionellen zentralisierten Börsen.



Die Plattform entwickelt sich weiter mit linearen USDT-Futures und dem nicht-vertraulichen Handel über Discreet Log Contracts (DLC), die derzeit entwickelt werden. Durch die Anwendung guter Risikomanagement-Praktiken (kleine Beträge, Stop-Loss, regelmäßige Abhebungen) wird LN Markets zu einem leistungsstarken Werkzeug, um Bitcoin Leverage verantwortungsvoll zu erkunden.



Fangen Sie klein an, testen Sie mit ein paar tausend Satelliten und erkunden Sie nach und nach diese neue Lightning Network-Grenze. Viel Spaß beim souveränen Handel ⚡️!



## Ressourcen





- [LN Markets offizielle Website](https://lnmarkets.com)
- [Dokumentation](https://docs.lnmarkets.com)