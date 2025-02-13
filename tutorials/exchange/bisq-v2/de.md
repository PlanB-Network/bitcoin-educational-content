---
name: Bisq 2
description: Vollständige Anleitung zur Verwendung von Bisq 2 und zum P2P-Tausch von Bitcoins
---
![cover](assets/cover.webp)

## Einführung

KYC-freie Peer-to-Peer-Börsen (P2P) sind für die Wahrung der Vertraulichkeit und der finanziellen Autonomie der Nutzer unerlässlich. Sie ermöglichen direkte Transaktionen zwischen Einzelpersonen, ohne dass eine Identitätsprüfung erforderlich ist, was für diejenigen, die Wert auf ihre Privatsphäre legen, entscheidend ist. Für ein tieferes Verständnis der theoretischen Konzepte schauen Sie sich den Kurs BTC204 an:

https://planb.network/courses/btc204
### Was ist Bisq 2?

Bisq 2 ist die neue Version der beliebten dezentralen Bisq-Börse, die im Jahr 2024 eingeführt wurde. Im Gegensatz zu seinem Vorgänger wurde Bisq 2 entwickelt, um mehrere Austauschprotokolle zu unterstützen und den Nutzern mehr Flexibilität zu bieten.

**Die wichtigsten neuen Funktionen:**


- Unterstützung für mehrere private Netzwerke (Tor, I2P)
- Mehrere Identitäten für mehr Vertraulichkeit
- REST API für Handelsroboter
- Unterstützung für mehrere Portfoliotypen
- Rollensystem mit Pfandpflicht in BSQ

Dieser Leitfaden konzentriert sich ausschließlich auf "Bisq Easy", das einzige derzeit verfügbare Protokoll. Bisq Easy wurde speziell für neue Bitcoin-Nutzer entwickelt. Mit diesem Protokoll können Nutzer Bitcoins gegen Fiat-Währungen auf einer dezentralen Peer-to-Peer-Plattform kaufen und verkaufen. Die Transaktionen sind auf den Gegenwert von 600 USD (mit einem Mindestbetrag von 6 USD) begrenzt, und die Sicherheit des Austauschs hängt von der Reputation der BTC-Verkäufer ab. Bisq Easy erhebt keine Handelsgebühren und verlangt keine Sicherheitsleistung. Es wird erwartet, dass Bisq Easy Bisq 1 für Bargeldtransaktionen unter 600 USD (oder dem Gegenwert) ablösen wird.

**Hauptmerkmale:**


- Plattformübergreifende Desktop-Anwendung
- Mehrere Austauschprotokolle verfügbar
- Dezentrales P2P-Netzwerk
- Fokus auf Vertraulichkeit (keine KYC, Nutzung von Tor)
- Nicht-Pflegschaft (Sie behalten die Kontrolle über Ihr Geld)
- Offene Quelle (AGPL)

### Unterschiede zu Bisq 1

**Für Käufer:**


- Keine Kaution erforderlich
- Keine Handelsgebühren
- Keine Schürfgebühren
- Sicherheit aufgrund der Reputation des Anbieters
- Niedrigere Handelslimits (entspricht 600 USD)

**Für Verkäufer:**


- Keine Kaution erforderlich
- Aufbau eines guten Rufs
- Möglichkeit der Verbrennung von BSQ oder der Schaffung von BSQ-Anleihen
- Potenziell höhere Verkaufsprämie (10-15% über dem Markt)

**Wichtiger Hinweis:** Sobald das Bisq Multisig-Protokoll in Bisq 2 implementiert ist, kann die alte Version von Bisq auslaufen. Bisq 1 wird jedoch weiterhin als Verwaltungstool für das Bisq CAD und für BSQ-BTC-Börsen verwendet.

### Austauschprozess


- Der Ersteller des Angebots legt die Bedingungen für den Austausch fest
- Sobald sich die Händler auf die Bedingungen (Zahlungsmethode und Preis) geeinigt haben, beginnt der Austausch
- Der Verkäufer schickt seine Bankdaten an den Käufer, und der Käufer schickt seine Bitcoin-Adresse an den Verkäufer
- Der Käufer zahlt in bar und benachrichtigt den Verkäufer
- Sobald die Zahlung eingegangen ist, sendet der Verkäufer die Bitcoins an die Adresse des Käufers
- Der Austausch ist abgeschlossen, wenn der Käufer die Bitcoins erhält

### Wichtige Regeln


- Vor dem Austausch von Zahlungsdaten kann der Austausch ohne Angabe von Gründen storniert werden
- Nach dem Austausch von Informationen kann die Nichteinhaltung von Verpflichtungen zur Verbannung führen
- Verwenden Sie bei Banküberweisungen **niemals die Begriffe "Bisq" oder "Bitcoin "** im Verwendungszweck (dies könnte dazu führen, dass die Gelder eingefroren werden oder sogar das Bankkonto des Empfängers oder des Zahlers gesperrt wird)
- Die Händler müssen sich mindestens einmal am Tag einloggen, um den Prozess zu verfolgen
- Im Falle eines Problems können die Unternehmer die Dienste eines Vermittlers in Anspruch nehmen

## Installation und Konfiguration

### 1. Herunterladen und Überprüfen von Bisq 2

![Téléchargement de Bisq 2](assets/fr/01.webp)


- Gehen Sie zu [bisq.network](https://bisq.network/downloads/)
- Laden Sie die Ihrem Betriebssystem entsprechende Version von Bisq 2 herunter (scrollen Sie auf der Seite nach unten)
- Überprüfen Sie die Authentizität der heruntergeladenen Datei (dringend empfohlen). Eine ausführliche Anleitung zur Überprüfung der Signatur finden Sie im folgenden Tutorial:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
### 2. Installation entsprechend Ihrem System

Bitte befolgen Sie die für Ihr Betriebssystem geeigneten Installationsschritte. Sollten Sie während der Installation auf Schwierigkeiten stoßen, können Sie die ausführliche Anleitung im [offiziellen Bisq-Wiki](https://bisq.wiki/Downloading_and_installing) einsehen.

### 3. Erste Inbetriebnahme


- Starten Sie Bisq 2 und akzeptieren Sie die Nutzungsbedingungen

![Conditions d'utilisation](assets/fr/01.webp)


- Erstellen Sie ein neues Profil, indem Sie einen Namen und einen Avatar wählen

![Création du profil](assets/fr/02.webp)


- Sie werden dann zum Haupt-Dashboard der Anwendung weitergeleitet, wo Sie Bisq Easy starten können, um Ihre ersten Bitcoins zu kaufen oder zu verkaufen

![Page d'accueil de Bisq 2](assets/fr/03.webp)

### 4. Einrichten von Zahlungsmitteln


- Rufen Sie den Bereich Zahlungskonten über das Hauptmenü auf

![Liste des comptes de paiement](assets/fr/04.webp)


- Fügen Sie eine neue Zahlungsmethode hinzu, indem Sie die erforderlichen Informationen ausfüllen

![Création d'un nouveau compte de paiement](assets/fr/05.webp)

Die Vorkonfiguration von Zahlungsmethoden ist optional, wird aber empfohlen, um beim Handel Zeit zu sparen. Sie können Ihre Zahlungsmethoden auch direkt während eines Handels konfigurieren, indem Sie sich an Ihren Börsenpartner wenden.

### 5. Sicherheit des Kontos

**Datensicherung:**

Im Gegensatz zu Bisq 1 ist in Bisq 2 derzeit keine Bitcoin-Wallet integriert: Transaktionen werden daher über Ihre eigenen externen Wallets abgewickelt. Dennoch empfehlen wir Ihnen, regelmäßig ein Backup Ihres Bisq 2 Datenordners zu erstellen. Um Ihren Datenordner zu finden, konsultieren Sie das [offizielle Bisq-Wiki] (https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).

**Identitätsmanagement:**

Mit Bisq 2 können Sie mehrere Identitäten anlegen. Jede Identität kann für verschiedene Arten von Transaktionen verwendet werden. Ihre Identitäten werden im Datenordner gespeichert.

## Kaufen und Verkaufen von Bitcoins

### Wie man Bitcoins kauft

**Option 1: Nutzen Sie ein bestehendes Angebot**


- Wählen Sie auf dem Hauptbildschirm "Bisq Easy", den Reiter "Erste Schritte" und klicken Sie dann auf "Handelsassistent starten"

![Lancer trade wizard](assets/fr/06.webp)


- Wählen Sie "Bitcoin kaufen" und wählen Sie Ihre Währung

![Sélection achat Bitcoin](assets/fr/07.webp)

![Choix de la devise](assets/fr/08.webp)


- Richten Sie Ihre bevorzugten Zahlungsmethoden ein (SEPA, Revolut, etc.)

![Configuration méthodes de paiement](assets/fr/09.webp)


- An diesem Punkt haben Sie entweder eine Liste von Angeboten, die Ihren vorherigen Kriterien entsprechen, oder Sie müssen zum "Offerbook" gehen

![Liste des offres](assets/fr/10.webp)


- Im zweiten Fall können Sie die Angebote über die Schaltflächen oben rechts auf der Oberfläche anzeigen und filtern

![Filtres des offres](assets/fr/11.webp)


- Sobald Sie Ihr Angebot ausgewählt haben, müssen Sie nur noch Ihre Zahlungsmethode wählen und die Zusammenfassung des Geschäfts bestätigen

![Choix modalités de paiement](assets/fr/12.webp)

![Configuration du trade](assets/fr/13.webp)

![Récapitulatif du trade](assets/fr/14.webp)

**Option 2: Erstellen Sie Ihr eigenes Angebot**


- Wählen Sie "Bisq Easy" und dann "Angebotsbuch"
- Wählen Sie Ihr Handelspaar (z.B. BTC/EUR)
- Klicken Sie auf "Angebot erstellen
- Folgen Sie dem Assistenten zur Angebotserstellung: Definieren Sie den Betrag (Festbetrag oder Spanne)

![Configuration du montant](assets/fr/20.webp)


- Wählen Sie akzeptierte Zahlungsarten

![Sélection méthodes de paiement](assets/fr/21.webp)


  - Prüfen Sie die Zusammenfassung und veröffentlichen Sie das Angebot

![Récapitulatif et publication](assets/fr/22.webp)

Sobald der Austausch eingeleitet wurde:


- Senden Sie Ihre Bitcoin-Adresse oder Lightning-Rechnung an den Verkäufer

![Envoi adresse Bitcoin](assets/fr/15.webp)


- Erhalt der Bankverbindung des Verkäufers

![Réception coordonnées bancaires](assets/fr/16.webp)

![Détails coordonnées bancaires](assets/fr/17.webp)


- Nehmen Sie die Zahlung vor (ohne "Bisq" oder "Bitcoin" zu erwähnen)
- Benachrichtigung des Verkäufers über Ihre Zahlung

![Notification paiement](assets/fr/18.webp)


- Warten Sie auf die Bitcoins

![Attente réception](assets/fr/19.webp)

### Wie kann man Bitcoins verkaufen?

Der Verkaufsprozess auf Bisq 2 folgt einer ähnlichen Logik wie der Kaufprozess, mit denselben Hauptschritten, aber in umgekehrter Reihenfolge. Sie können entweder ein eigenes Verkaufsangebot erstellen oder auf ein bestehendes Kaufangebot reagieren. Im Folgenden finden Sie eine Übersicht über die verschiedenen Optionen und Phasen des Prozesses:

**Option 1: Erstellen eines Verkaufsangebots**


- Wählen Sie "Bisq Easy" und dann "Angebotsbuch"
- Klicken Sie auf "Angebot erstellen" und wählen Sie "Bitcoin verkaufen"
- Konfigurieren Sie Ihr Angebot:
 - Währung auswählen (EUR, USD, etc.)
 - Wählen Sie die akzeptierten Zahlungsarten
 - Legen Sie den Betrag fest (zwischen 6 und 600 USD Gegenwert)
 - Legen Sie Ihren Preis fest (Festpreis oder % des Marktes)
- Details prüfen und das Angebot veröffentlichen

**Option 2: Ein bestehendes Angebot wahrnehmen**


- Angebote auf der Registerkarte "Angebotsbuch" durchsuchen
- Filter nach Währung und Zahlungsmethode
- Wählen Sie ein Angebot, das zu Ihnen passt
- Details prüfen und das Angebot annehmen

**Verkaufsprozess:**

Sobald der Austausch eingeleitet wurde:


   - Senden Sie Ihre Bankverbindung an den Käufer
   - Warten Sie auf die Bitcoin-Adresse des Käufers
   - Prüfen Sie, ob die Adresse gültig ist

Nach der Zahlungsbenachrichtigung:


   - Prüfen Sie, ob die Zahlung auf Ihrem Konto eingegangen ist
   - Bestätigen Sie, dass der Betrag und die Details übereinstimmen
   - Senden Sie Bitcoins an die angegebene Adresse
   - Markieren Sie die Transaktion als abgeschlossen

Fertigstellung :


   - Warten Sie auf die Bestätigung des Käufers
   - Feedback zur Transaktion hinterlassen
   - Bauen Sie Ihren Ruf für zukünftige Verkäufe auf

**Wichtiger Hinweis:** Als Verkäufer müssen Sie besonders auf das Risiko von Rückbuchungen achten. Bevorzugen Sie sichere Zahlungsmethoden und überprüfen Sie immer, ob die Zahlung eingegangen ist, bevor Sie Bitcoins versenden.

## Bewährte Praktiken und Sicherheit

### Sicherheitstipps

**Für Käufer:**


- Beginnen Sie mit kleinen Mengen
- Prüfen Sie die Reputation des Verkäufers (Mindestpunktzahl 30.000)
- Verwenden Sie nur die vorgeschlagenen Zahlungsarten
- Prüfen Sie, ob der Verkäufer aktiv ist, bevor Sie die Zahlung senden
- Verwenden Sie nur die im Austausch-Chat angegebene Bankverbindung
- Kommunizieren Sie niemals außerhalb der Bisq 2 Plattform
- Zahlungsnachweis aufbewahren
- Senden Sie niemals sensible Informationen

**Für Verkäufer:**


- Seien Sie vorsichtig mit neuen Konten
- Vermeiden Sie Zahlungsmethoden, die anfällig für Rückbuchungen sind (PayPal, Venmo)
- Prüfen Sie, ob die Kontodaten mit denen des Käufers übereinstimmen
- Kommunikation auf Chat beschränken Bisq 2
- Im Zweifelsfall eine Mediation einleiten

### Aufbau eines guten Rufs (für Vertriebsmitarbeiter)

Um Ihren Ruf als Verkäufer auf Bisq zu verbessern, sollten Sie regelmäßig Transaktionen durchführen und eine professionelle Kommunikation mit Käufern pflegen. Reagieren Sie schnell auf Käuferanfragen, um eine positive Erfahrung zu gewährleisten. Sie können auch eine BSQ-Anleihe erstellen, um Ihr Engagement für die Plattform zu zeigen. Diese Maßnahmen schaffen Vertrauen und ziehen mehr Käufer an.

### Streitbeilegung


- Kontaktieren Sie Ihren Gesprächspartner per Chat
- Eröffnen Sie gegebenenfalls einen Streitfall
- Alle geforderten Nachweise vorlegen
- Befolgen Sie die Anweisungen des Vermittlers

### Datenschutz :


- Keine Registrierung oder zentralisierte Identitätsüberprüfung erforderlich
- Alle Verbindungen laufen über das Tor-Netzwerk (und bald auch über I2P)
- Kein zentraler Server zur Datenspeicherung
- Die Transaktionsdetails sind nur für die beteiligten Parteien lesbar

### Schutz vor Zensur :


- Vollständig verteiltes P2P-Netzwerk
- Das Tor-Netzwerk (und bald auch I2P) nutzen, um sich gegen Zensur zu wehren
- Open-Source-Projekt, das von einer DAO verwaltet wird, ohne zentrale Rechtspersönlichkeit

## Vorteile und Nachteile

### Vorteile von Bisq 2


- Maximale Vertraulichkeit**: Kein KYC, Verwendung von Tor
- Dezentralisierung**: Kein zentraler Server
- Sicherheit**: Quelloffener, nicht verschlüsselter Code
- Intuitive Benutzeroberfläche**: Einfacher als Bisq 1
- Flexibilität**: Mehrere Austauschprotokolle

### Nachteile von Bisq 2


- Begrenzte Liquidität** (im Moment) :
 - Neues Protokoll in der Anlaufphase
 - Wenige Verkaufsangebote verfügbar
 - Möglicherweise lange Wartezeiten, um einen Käufer zu finden
- Handelslimits**: Maximal 600 USD pro Transaktion (mit Bisq easy)
- Nur Desktop**: Keine mobile Anwendung

## Künftige Protokolle

Obwohl Bisq Easy derzeit das einzige verfügbare Protokoll ist, befinden sich mehrere andere Protokolle für Bisq 2 in der Entwicklung:


- Bisq Lightning**: Austauschprotokoll auf der Grundlage eines Treuhandsystems, das die Kryptographie der Mehrparteienberechnung im Lightning-Netzwerk nutzt.
- Bisq MuSig**: Migration des Hauptprotokolls von Bisq 1 auf Bisq 2, unter Verwendung eines 2-on-2-Multisig mit Sicherheitseinlagen.
- BSQ-Tauschgeschäfte**: Sofortige atomare Tauschgeschäfte zwischen BSQ und BTC.
- Liquid Swaps**: Austausch von Vermögenswerten im Liquid-Netzwerk (USDT, BTC-L) über atomare Swaps.
- Monero Swaps**: Atomare Tauschgeschäfte zwischen Bitcoin und Monero.
- Flüssiges MuSig**: Version des Multisig-Protokolls mit L-BTC für niedrigere Kosten und größere Vertraulichkeit.
- Submarine Swaps**: Tauschgeschäfte zwischen Bitcoin im Lightning-Netzwerk und Bitcoin auf der Kette.
- Stablecoin-Swaps**: Atomare Tauschgeschäfte zwischen Bitcoin und USD-Stablecoins.
- Multisig-Optionen**: Erstellung von P2P-Put- und Call-Optionen mit BTC-Blockierung in einer On-Chain-Multisig-Transaktion.
- Offene Multisig-Kontrakte**: Ermöglicht die Erstellung individueller bedingter Kontrakte unter Verwendung eines 2-on-3-Multisig-Systems mit Arbitrage.

Diese Protokolle befinden sich derzeit in der Entwicklung und werden schrittweise in Bisq 2 integriert, um den Nutzern mehr Flexibilität für ihre spezifischen Anforderungen zu bieten.

## Nützliche Ressourcen


- Offizielle Website: [bisq.network](https://bisq.network)
- Dokumentation: [Bisq Wiki](https://bisq.wiki)
- Unterstützung: [Forum Bisq](https://bisq.community)
- Quellcode: [GitHub](https://github.com/bisq-network)