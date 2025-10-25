---
name: Lipa for Business
description: Bitcoin und Lightning-Zahlungslösungen für Händler
---

![cover](assets/cover.webp)



Händler sind nun zunehmend daran interessiert, Bitcoin-Zahlungen über Lightning Network zu akzeptieren. Im Gegensatz zu herkömmlichen Kreditkartenzahlungen, die mit hohen Gebühren und langen Abwicklungszeiten verbunden sind, erfolgen Lightning-Transaktionen praktisch sofort, unterliegen keinen Rückbuchungen und wahren die Vertraulichkeit der Kunden.



Damit ein Unternehmen Bitcoin problemlos einführen kann, muss die Zahlungslösung mit einer intuitiven Interface-Kasse einfach bleiben, Mehrbenutzerfunktionen bieten und idealerweise eine automatische Umrechnung in die Landeswährung ermöglichen, um die Volatilität zu mindern.



**Lipa for Business** ist die perfekte Antwort auf diese Bedürfnisse. Es handelt sich um eine Schweizer Lösung, die von der Lightning Payment Services AG entwickelt wurde, um Händlern die Möglichkeit zu geben, Bitcoin Lightning-Zahlungen einfach und effizient zu akzeptieren, ohne dass sie dabei an ihre Kunden gebunden sind.



*Hinweis: Die in diesem Tutorial verwendeten Screenshots stammen von der offiziellen Lipa for Business-Website (lipa.swiss/de/for-business) und werden zu Schulungszwecken verwendet*



## Einführung von Lipa for Business



Lipa for Business ist eine mobile Anwendung, die wie eine Bitcoin- und Lightning-Kasse funktioniert. Sie bietet ein rationalisiertes Interface, um Zahlungen in Sats einzuziehen, und integriert professionelle Funktionen: Zugang für Mitarbeiter, Buchhaltungsexporte, Web-Dashboard, alles ohne jemals in den Besitz Ihrer Gelder zu gelangen.



### Wesentliche Merkmale



**Sofortige Lightning-Zahlungen**: Bitcoin Lightning-Rechnungen werden in Sekundenschnelle erstellt und gewährleisten praktisch sofortige Transaktionen ohne zwischengeschaltete Banken. Die Gebühren sind niedrig und transparent im Vergleich zu herkömmlichen Lösungen.



**Interface POS intuitiv**: Die App bietet eine übersichtliche Interface-Kasse, die für die einfache Verwendung im Laden konzipiert ist. Geben Sie den Betrag in der lokalen Währung ein, und die App zeigt sofort den Betrag in BTC und einen Zahlungs-QR-Code an. Kompatibel mit allen auf dem Markt befindlichen Lightning-Wallets.



**Verwaltung mehrerer Angestellter**: Alle Mitarbeiter können die Anwendung zur Auszahlung nutzen, ohne Zugriff auf die Gelder zu haben. Der Eigentümer behält die volle Kontrolle, während die Cloud-Synchronisation sicherstellt, dass keine Transaktion verloren geht. Jeder Mitarbeiter erhält einen separaten Zugang über eine QR-Code-Einladung.



**Automatische Umrechnung in CHF**: Für Schweizer Händler bietet Lipa eine sofortige Umrechnung der Umsätze in Schweizer Franken auf dem Bankkonto. Diese Option ist optional: Sie können die Zahlungen in Bitcoin behalten (kostenlos) oder sie für 0,98% Kommission in CHF/EUR umwandeln.



**Web-Dashboard**: Interface-Administrationspanel, das über dashboard.lipa.swiss zugänglich ist und es Ihnen ermöglicht, alle Transaktionen anzuzeigen, nach Zeitraum oder Mitarbeiter zu filtern und Buchhaltungsdaten im CSV-Format zu exportieren. Das Dashboard kann auch verwendet werden, um generate Web-Rechnungen mit QR-Codes direkt von Interface aus zu erstellen.



## Ein Konto erstellen



⚠️ **Wichtig** : Die Installation der Anwendung erfordert einen Wohnsitz in der Schweiz. Diese geografische Einschränkung gilt aus Gründen der Einhaltung gesetzlicher Vorschriften.



Um Lipa for Business zu nutzen, müssen Sie zunächst ein spezielles Händlerkonto einrichten:





- Gehen Sie auf lipa.swiss/for-business und laden Sie die Anwendung für Ihre Plattform herunter (Android oder iOS)
- Installieren Sie "lipa Wallet for business" von Google Play oder dem App Store
- Beim ersten Start geben Sie Ihre Unternehmensdaten ein: Firmenname, Kontakt-E-Mail, Telefon und Address
- Die E-Mail ist die wichtigste Kennung für den Zugriff auf das Web-Dashboard



Sobald das Formular eingereicht wurde, erstellt Lipa Ihren Händlerbereich. Vor der endgültigen Aktivierung kann eine kurze manuelle Prüfung durchgeführt werden (vereinfachtes KYC-Verfahren). Die Aktivierung erfolgt in der Regel innerhalb von 24 Stunden, aber die Zeiten können variieren.



**Wichtig**: Für die Einlösung von Bitcoin ist keine Bankverbindung erforderlich. Die Bankverbindung ist nur erforderlich, wenn Sie sich für die automatische Umrechnung in CHF entscheiden.



## Einbau und Interface



**Mobile Anwendung**: Verfügbar für Android/iOS-Smartphones und -Tablets. Interface wurde für die Verwendung am Point of Sale entwickelt, mit leicht lesbarem Elements und auf das Notwendige beschränkten Interaktionen. Eine Schaltfläche "Eine Zahlung einlösen" ermöglicht den Zugriff auf den Betragseingabebildschirm.



**Technische Anforderungen**: Stabile Internetverbindung erforderlich (mindestens 3G), um Blitzzahlungen in Echtzeit zu verarbeiten.



**Web-Dashboard**: Kostenloses Dashboard, zugänglich über dashboard.lipa.swiss. Sichere E-Mail-Verbindung (magischer Link ohne Passwort). Interface zeigt alle Ihre Transaktionen mit allen Details an: Datum, BTC-/Fiat-Betrag, Exchange-Kurs, Mitarbeiter, etc. CSV-Export für die Integration in die Buchhaltung.



![Dashboard Lipa Business](assets/fr/02.webp)



Das Dashboard kann auch verwendet werden, um generate Web-Rechnungen mit QR-Codes direkt von Interface zu erstellen:



![Génération factures web](assets/fr/03.webp)



**Mehrere Terminals**: Native Unterstützung für mehrere Terminals innerhalb eines Unternehmens. Fügen Sie neue Geräte hinzu, indem Sie Mitarbeiter per QR-Code-Einladung einladen. Jedes Terminal ist mit demselben Händler Wallet verbunden, wobei die Rückverfolgbarkeit nach Kassierer beibehalten wird.



## Eine Zahlung annehmen



Das Inkassoverfahren ist ähnlich wie bei einer herkömmlichen Transaktion:



![Processus de paiement Lipa](assets/fr/01.webp)





- Betrag eingeben**: Geben Sie auf dem Zahlungsbildschirm den Betrag in der Landeswährung (CHF oder EUR) ein. Beispiel: für einen Kaffee zu 4,50 CHF geben Sie 4,50 ein
- Invoice-Generierung** : Die Anwendung rechnet den Betrag sofort in Satoshis zum aktuellen Kurs um und generiert einen Lightning Invoice in Form eines QR-Codes
- Kundenzahlung** : Der Kunde scannt den QR-Code mit seinem Wallet Lightning und validiert die Zahlung
- Bestätigung** : Die Zahlung wird innerhalb von Sekunden bestätigt, mit visueller Anzeige des Erfolgs



## Professionelle Werkzeuge



**Geschichte und Statistik**: Jede Zahlung wird mit allen Details erfasst. Das Dashboard bietet eine Übersicht mit Filtern nach Zeitraum oder Mitarbeiter, vergleichbar mit einem klassischen Kassensystem.



**Buchhaltungsexporte**: Datenexport im CSV/Excel-Format mit allen notwendigen Informationen (Exchange Satz, transaction ID) zur Integration in Ihre Buchhaltungssoftware.



**Mitarbeiterverwaltung**: Hinzufügen/Entfernen von autorisierten Benutzern über das Dashboard. Jeder Mitarbeiter erhält einen eigenen Zugang mit Transaktionsnachweis. Entzug jederzeit möglich.



**Backup**: Nicht verpfändetes Händlerkonto mit 24-Wort-Wiederherstellungsphrase zur sicheren Aufbewahrung. Nur der Inhaber des Haupt-Wallet sollte dieses Backup verwalten - Mitarbeiter haben keinen Zugriff darauf.



## Automatische CHF-Umrechnung



**Verfügbarkeit**: Der Service ist für Schweizer Händler mit Zahlung in CHF verfügbar (EUR je nach Verfügbarkeit).



**Konfiguration**: Wahlmöglichkeit zwischen Empfang in Bitcoin (kostenlos) oder Umrechnung in Fiat über Finanzpartner. Bei Konvertierung in CHF ist eine IBAN für Überweisungen anzugeben.



**Gebühren**: 0.98% Provision auf umgewandelte Beträge (im Vergleich zu 0% für Zahlungen in BTC). Keine anderen versteckten Gebühren oder Abonnements.



**Wie es funktioniert** : Der erhaltene Betrag wird sofort zum Marktpreis verkauft und auf Ihr Bankkonto überwiesen. Die Überweisung erfolgt gemäß den üblichen Bankfristen Ihrer Bank.



**Flexibilität**: Option jederzeit in den Parametern umkehrbar. Ermöglicht es Ihnen, im Modus "Fiat-Konvertierung" zu testen und dann zu 100% BTC zu wechseln, sobald Sie sich wohl fühlen.



## Sicherheit und Vertraulichkeit



**Nicht sorgeberechtigt**: Sie behalten die ständige Kontrolle über die erhaltenen Gelder. Während der Konfiguration wird ein privates/öffentliches Schlüsselpaar generiert (daher die 24-Wort-Phrase). Lipa speichert Ihre privaten Schlüssel nicht.



**Mitarbeitersicherheit**: Mitarbeiter können nur Rechnungen erstellen, aber keine Gelder ausgeben. Im Falle eines Terminalproblems bleiben Ihre Gelder sicher und Sie können den Zugang sperren.



**Kundenvertraulichkeit**: pseudonyme Blitzzahlungen ohne personenbezogene Daten. Im Gegensatz zu Kartenzahlungen, die über zentralisierte Netzwerke laufen.



**Authentifizierung**: Dashboard zugänglich über Magic Link E-Mail. Mobile Anwendung geschützt durch PIN oder biometrische Daten.



## Empfohlene Anwendungsfälle





- Gastronomie**: Bars, Restaurants, Cafés, die Aufschläge in Bitcoin mit Trinkgeldmanagement akzeptieren
- Einzelhandel**: Lebensmittelgeschäfte, Bäckereien zur Ausweitung der Zahlungsmöglichkeiten ohne feste Gebühren
- Nomadische Verkäufer**: Imbisswagen, Märkte, Festivals mit nur einem Smartphone
- Veranstaltungen** : Temporäre Stände mit gebrauchsfertigen Lösungen
- Dienstleistungen**: Berater, Handwerker für einmalige Abrechnung in Bitcoin



## Vorteile und Grenzen



### Vorteile




- Einfaches Interface, keine technischen Kenntnisse erforderlich
- Freiheitsentziehende Lösung mit vollständiger Kontrolle über die Mittel
- Verwaltung mehrerer Mitarbeiter mit Rückverfolgbarkeit
- Buchhaltungsexport und Web-Dashboard inklusive
- Automatische CHF-Umrechnungsoption für Schweizer Händler
- Transparente Gebühren: 0% Bitcoin, 0,98% Fiat-Umrechnung
- Positionierung als innovatives Unternehmen im Bitcoin-Ökosystem
- Schutz vor Inflation und Währungsabwertung
- Zensurresistentes, dezentralisiertes Zahlungssystem



### Grenzwerte




- Nur Blitzschutz (kein Bitcoin On-Chain)
- Fiat-Umrüstung derzeit auf die Schweiz beschränkt
- Erfordert, dass die Kunden einen kompatiblen Wallet Lightning haben
- Statische QR-Codes derzeit nicht verfügbar
- Internetverbindung für alle Transaktionen erforderlich



## Schlussfolgerung



Lipa for Business ist als Komplettlösung für die Annahme von Bitcoin in Geschäften positioniert. Es wird keine teure Infrastruktur benötigt (ein einfaches Smartphone reicht aus), die Kosten sind niedrig und fix und die Integration in bestehende Prozesse ist einfach.



Sein nicht-vertraulicher, datenschutzfreundlicher Charakter, kombiniert mit professionellen Management-Tools, macht es zu einer attraktiven Wahl für Händler, die Bitcoin einführen und dabei Einfachheit und Sicherheit beibehalten wollen.



## Ressourcen





- [Lipa for Business offizielle Website](https://lipa.swiss/en/for-business)
- [Dashboard web](https://dashboard.lipa.swiss)
- [Lipa Support for Business](https://help.lipa.swiss/business)
- [Lipa General Support](https://help.lipa.swiss/Wallet)
- [LinkedIn Lipa] (https://www.linkedin.com/company/getlipa)
- [Twitter @lipa_btc](https://twitter.com/lipa_btc)