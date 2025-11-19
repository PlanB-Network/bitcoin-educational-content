---
name: LNP2PBot
description: Vollständige Anleitung zu LNP2PBot und P2P-Bitcoin-Handel
---
![cover](assets/cover.webp)

## Einführung

KYC-freie Peer-to-Peer-Börsen (P2P) sind für die Wahrung der Vertraulichkeit und der finanziellen Autonomie der Nutzer unerlässlich. Sie ermöglichen direkte Transaktionen zwischen Einzelpersonen, ohne dass eine Identitätsprüfung erforderlich ist, was für diejenigen, die Wert auf ihre Privatsphäre legen, entscheidend ist. Für ein tieferes Verständnis der theoretischen Konzepte schauen Sie sich den Kurs BTC204 an:

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Der Kauf und Verkauf von Bitcoin über Peer-to-Peer (P2P) ist eine der privatesten Methoden, Bitcoins zu erwerben oder zu veräußern. LNP2PBot ist ein Open-Source-Telegram-Bot, der P2P-Börsen auf dem Lightning-Netzwerk erleichtert und schnelle, kostengünstige und KYC-freie Transaktionen ermöglicht.

### Warum Lnp2pbot verwenden?


- Keine KYC erforderlich
- Schnelle Transaktionen über das Lightning Network
- Geringe Kosten
- Einfache Schnittstelle über Telegram, eine beliebte Messaging-Anwendung, die von überall auf der Welt zugänglich ist
- Integriertes Reputationssystem
- Automatisches Treuhandkonto für sicheren Handel
- Unterstützung mehrerer Währungen
- Aktive und wachsende Gemeinschaft

### Voraussetzungen

Um Lnp2pbot zu verwenden, benötigen Sie :

1. Lightning Network Geldbörse (Breez, Phoenix oder Blixt empfohlen)

2. Telegram-Anwendung installiert (https://telegram.org/)

3. Ein Telegram-Konto mit einem bestimmten Benutzernamen

## Installation und Konfiguration

### 1. Konfigurieren Ihrer Lightning-Geldbörse

Installieren Sie zunächst eine kompatible Lightning-Geldbörse. Hier sind unsere detaillierten Empfehlungen:

**Empfehlenswerte Portfolios**


- [Breez](https://breez.technology):
  - Ausgezeichnet für Anfänger
  - Intuitive, moderne Schnittstelle
  - Nicht-Pflegschaft (Sie behalten die Kontrolle über Ihr Geld)
  - Perfekt kompatibel mit Lnp2pbot
  - Verfügbar für iOS und Android

Unten finden Sie den Link zur Anleitung für diese Brieftasche:

https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

- [Phoenix](https://phoenix.acinq.co) :
  - Einfach und zuverlässig
  - Automatische Kanalkonfiguration
  - Native Unterstützung für BOLT11-Rechnungen
  - Hervorragend geeignet für alltägliche Transaktionen
  - Verfügbar für iOS und Android

Unten finden Sie den Link zur Anleitung für diese Brieftasche:

https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

- [Blixt](https://blixtwallet.github.io) :
  - Eher technisch, aber sehr vollständig
  - Erweiterte Konfigurationsoptionen
  - Perfekt für erfahrene Benutzer
  - Offene Quelle
  - Verfügbar für Android

Unten finden Sie den Link zur Anleitung für diese Brieftasche:

https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

**Wichtige Hinweise zu anderen Portfolios**

⚠️ **Wichtig**: Stellen Sie vor dem Verkauf von Sats sicher, dass Ihr Portfolio "Hold"-Rechnungen unterstützt, die vom Bot als Treuhandsystem verwendet werden.


- **Geldbörse von Satoshi**: Funktioniert gut für den Empfang von Sats, kann aber Verzögerungen bei der Aktualisierung des Guthabens haben, wenn ein Verkauf abgebrochen wird.
- **Muun**: Nicht empfehlenswert, da Zahlungen aufgrund der Beschränkung der Bot-Routing-Gebühren (maximal 0,2 %) fehlschlagen können.
- **Aqua**: Funktioniert für den Empfang von Satelliten, kann aber im Falle eines Verkaufsstopps lange Verzögerungen (bis zu 48 Stunden) bei der Aktualisierung des Kontostands haben.

💡 **Tipp**: Für eine optimale Erfahrung sollten Sie sich für die empfohlenen Portfolios entscheiden (Breez, Phoenix oder Blixt).

⚠️ **Wichtig**: Vergessen Sie nicht, Ihre Wiederherstellungsphrasen an einem sicheren Ort zu speichern.

### 2. Erste Schritte mit Lnp2pbot

1. Klicken Sie auf diesen Link, um auf den Bot zuzugreifen: [@lnp2pBot](https://t.me/lnp2pbot)

2. Telegram wird automatisch geöffnet

3. Klicken Sie auf "Start" oder senden Sie den Befehl "/start"

4. Der Bot wird Sie auffordern, einen Benutzernamen zu erstellen, wenn Sie noch keinen haben

5. Der Bot wird Sie durch die anfängliche Konfiguration führen

### 3. Werden Sie Mitglied der Gemeinschaft


- Treten Sie dem Hauptkanal bei: [@p2plightning](https://t.me/p2plightning)
- Unterstützung: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)

## Kaufen und Verkaufen von Bitcoins

Es gibt zwei Möglichkeiten, Bitcoins auf Lnp2pbot zu tauschen:

1. Durchsuchen Sie bestehende Angebote auf dem Markt und reagieren Sie darauf

2. Erstellen Sie Ihr eigenes Angebot zum Kauf oder Verkauf

In diesem Leitfaden wird ausführlich erläutert, wie :


- Bitcoins aus einem bestehenden Angebot kaufen
- Verkaufen Sie Bitcoins, indem Sie Ihr eigenes Angebot erstellen

### Wie man Bitcoins kauft

**1. Ein Angebot suchen und auswählen**

![Sélection d'une offre de vente](assets/fr/01.webp)

Durchsuchen Sie die Angebote in [@p2plightning] (https://t.me/p2plightning) und klicken Sie auf die Schaltfläche "Satoshis kaufen" unter der Anzeige, die Sie interessiert.

**2. Angebot und Betrag validieren**

![Validation de l'offre](assets/fr/02.webp)

1. Zurück zum Bot-Chat

2. Bestätigen Sie Ihre Wahl des Angebots

3. Geben Sie den Betrag in Fiat-Währung ein, den Sie kaufen möchten

4. Der Bot wird Sie auffordern, eine Blitzrechnung über den Betrag in Satoshis zu erstellen

**3. Kontaktieren Sie den Verkäufer**

![Mise en relation](assets/fr/03.webp)

Sobald die Rechnung verschickt wurde, setzt sich der Bot mit dem Verkäufer in Verbindung.

**4. Kommunikation mit dem Verkäufer**

![Chat privé](assets/fr/04.webp)

Klicken Sie auf den Nickname des Verkäufers, um einen privaten Chat-Kanal zu öffnen, in dem Sie Einzelheiten zur Zahlung in Fiat austauschen können.

**5. Bestätigung der Zahlung**

![Confirmation du paiement](assets/fr/05.webp)

Nachdem Sie die Fiat-Zahlung vorgenommen haben, verwenden Sie den Befehl `/fiatsent` im Bot-Chat. Sobald die Transaktion abgeschlossen ist, können Sie den Verkäufer bewerten und die Transaktion wird geschlossen.

### Wie man Bitcoins verkauft

**1. Erstellen Sie ein Verkaufsangebot**

![Création d'une offre de vente](assets/fr/06.webp)

Um ein Verkaufsangebot zu erstellen, verwenden Sie einfach den Befehl :

`Verkaufen`

Der Bot wird Sie dann Schritt für Schritt anleiten:

1. Wählen Sie Ihre Währung

2. Geben Sie die Anzahl der zu verkaufenden Satoshis an

3. Für den Preis haben Sie zwei Möglichkeiten:


   - Festsetzung eines Festpreises für die Menge der Satoshis
   - Verwendung des Marktpreises mit der Möglichkeit der Anwendung eines Aufschlags (positiv oder negativ)

💡 **Tipp**: Mit dem Aufschlag können Sie Ihren Preis im Verhältnis zum Marktpreis anpassen. Ein Aufschlag von -1 % bedeutet zum Beispiel, dass Sie für 1 % weniger als den Marktpreis verkaufen.

**2. Bestätigung der Auftragserstellung**

![Confirmation de l'ordre de vente](assets/fr/07.webp)

Sobald der Auftrag erstellt wurde, erhalten Sie eine Bestätigung mit der Möglichkeit, den Auftrag mit dem Befehl "Stornieren" zu stornieren.

**3. Verkäufe managen**

![Prise de l'ordre par un acheteur](assets/fr/08.webp)


- Wenn ein Käufer auf Ihr Angebot antwortet, erhalten Sie eine Benachrichtigung mit einem QR-Code und einer Rechnung, die Sie bezahlen müssen.
- Überprüfen Sie das Profil und den Ruf des Käufers.

![Mise en relation avec l'acheteur](assets/fr/09.webp)


- Klicken Sie auf den Nickname des Käufers, um einen privaten Diskussionskanal zu öffnen.
- Übermittlung der Fiat-Zahlungsdaten an den Käufer.
- Warten Sie auf die Bestätigung der Fiat-Zahlung durch den Käufer.
- Überprüfen Sie, ob die Zahlung auf Ihrem Konto eingegangen ist.

![Confirmation de la fin de l'ordre](assets/fr/10.webp)


- Bestätigen Sie die Transaktion mit `/release` und schließen Sie die Bestellung ab. Sie haben dann die Möglichkeit, den Käufer zu bewerten.

## Bewährte Praktiken und Sicherheit

### Tipps zur Sicherheit


- Beginnen Sie mit kleinen Mengen
- Prüfen Sie immer den Ruf der Nutzer
- Verwenden Sie nur die vorgeschlagenen Zahlungsarten
- Alle Mitteilungen im Bot-Chat halten
- Geben Sie niemals sensible Informationen weiter

### Reputationssystem


- Jeder Nutzer hat einen Reputationswert
- Erfolgreiche Transaktionen erhöhen Ihren Punktestand
- Wählen Sie Nutzer mit einem guten Ruf
- Melden Sie jedes verdächtige Verhalten den Moderatoren

### Beilegung von Streitigkeiten

1. Wenn Probleme auftreten, bleiben Sie ruhig und professionell

2. Verwenden Sie den Befehl "/dispute", um ein Ticket zu öffnen

3. Erbringen Sie alle erforderlichen Nachweise

4. Auf einen Moderator warten

## Vergleich mit anderen Lösungen

Lnp2pbot hat mehrere Vor- und Nachteile gegenüber anderen P2P-Tauschlösungen wie Peach, Bisq, HodlHodl und Robosat:

### Vorteile von Lnp2pbot


- **Keine KYC erforderlich**: Im Gegensatz zu anderen Plattformen ist bei Lnp2pbot keine Identitätsprüfung erforderlich, so dass die Vertraulichkeit der Nutzer gewahrt bleibt.
- **Schnelle Transaktionen**: Dank des Lightning-Netzwerks erfolgen Transaktionen fast sofort.
- **Niedrige Gebühren**: Die Transaktionskosten sind niedriger als bei traditionellen Börsen.
- **Mobile Verfügbarkeit**: LNP2PBot ist über Telegram zugänglich und kann somit einfach auf mobilen Geräten genutzt werden.
- **Einfach zu bedienen**: Die intuitive Benutzeroberfläche von Lnp2pbot ist auch für weniger erfahrene Benutzer leicht zu bedienen.

### Nachteile von Lnp2pbot


- **Telegram-Abhängigkeit**: Die Verwendung von Lnp2pbot erfordert ein Telegram-Konto, das nicht für alle Benutzer geeignet ist.
- **Weniger Liquidität**: Im Vergleich zu etablierteren Plattformen wie Bisq kann die Liquidität geringer sein.

Im Vergleich dazu bieten Lösungen wie Bisq eine größere Liquidität und eine Desktop-Schnittstelle, können aber höhere Gebühren und längere Transaktionszeiten mit sich bringen. HodlHodl und Robosat bieten ebenfalls einen KYC-freien Handel an, jedoch mit unterschiedlichen Gebührenstrukturen und Schnittstellen.

## Nützliche Ressourcen


- Offizielle Website: https://lnp2pbot.com/
- Dokumentation: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Unterstützung: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)