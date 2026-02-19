---
name: Blitz Wallet
description: Die einfachste Bitcoin-Wallet.
---

![cover](assets/cover.webp)

Die Benutzererfahrung ist einer der entscheidenden Faktoren bei der Wahl einer Bitcoin-Wallet. In diesem Tutorial stellen wir Ihnen Blitz Wallet vor, eine Wallet, die Einfachheit in den Mittelpunkt ihres Ansatzes stellt: Dank der Integration des **Spark**-Protokolls bietet Ihnen Blitz eine der einfachsten und umfassendsten Bitcoin-Wallets auf dem Markt, mit sofortigen Zahlungen und ohne technischen Verwaltungsaufwand.

## Was ist Blitz Wallet?

Blitz Wallet ist eine **self-custodial** und **open source** Bitcoin-Wallet, die auf Ihre Souveränität sowie eine flüssige und intuitive Benutzererfahrung setzt.

[Blitz Wallet](https://blitz-wallet.com/) ist eine mobile Anwendung, die für Android (Play Store) und iOS (App Store) verfügbar ist.

Im Gegensatz zu herkömmlichen Lightning-Wallets, die die Verwaltung von Zahlungskanälen und eingehender Liquidität erfordern, setzt Blitz Wallet auf das **Spark-Protokoll**, um diese technischen Komplexitäten zu beseitigen. Das Ergebnis: sofortige Zahlungen ab dem ersten empfangenen Satoshi, ohne jegliche vorherige Konfiguration. Das Ziel von Blitz ist es, Bitcoin-Zahlungen so einfach wie eine herkömmliche Zahlungs-App zu gestalten, ohne jemals die Self-Custody Ihrer Mittel zu gefährden.

Blitz Wallet unterstützt außerdem **lesbare Adressen** im Format `benutzer@domain.com` (über LNURL), wodurch Bitcoin so einfach wie eine E-Mail versendet werden kann, ohne bei jeder Transaktion lange Invoices oder QR codes handhaben zu müssen.

## Das Spark-Protokoll verstehen

Bevor wir zur Praxis übergehen, ist es hilfreich, die Technologie zu verstehen, die Blitz Wallet unter der Haube antreibt: das **Spark-Protokoll**.

### Was ist Spark?

Spark ist ein open source Layer-Protokoll, das auf Bitcoin aufbaut und vom Team von Lightspark entwickelt wurde. Es ermöglicht sofortige Transaktionen zu geringen Kosten, wobei die Self-Custody Ihrer Bitcoins gewahrt bleibt.

Im Gegensatz zum Lightning Network, das auf **Zahlungskanälen** zwischen zwei Parteien basiert, verwendet Spark eine Technologie namens **Statechain** (Zustandskette). Das grundlegende Prinzip ist folgendes: Anstatt die Bitcoins bei jeder Transaktion auf der Blockchain zu bewegen, überträgt Spark das **Ausgaberecht** von einem Benutzer auf einen anderen, ohne on-chain-Bewegung.

### Wie funktioniert es?

Um Spark intuitiv zu verstehen, stellen wir uns vor, dass das Ausgeben eines Bitcoins auf Spark das Vervollständigen eines Puzzles aus zwei Teilen erfordert:
- Ein Teil wird vom Benutzer gehalten (zum Beispiel Alice).
- Das andere Teil wird von einer Gruppe von Betreibern gehalten, die als **Spark Entity (SE)** bezeichnet wird.

Nur die Kombination der beiden passenden Teile ermöglicht es, die Bitcoins auszugeben.

Wenn Alice ihre Bitcoins an Bob senden möchte, passiert Folgendes: Ein neues Puzzle wird gemeinsam zwischen Bob und der SE erstellt. Das Puzzle behält die gleiche Form, aber die Teile, aus denen es besteht, ändern sich. Von nun an passt Bobs Teil zu dem der SE. Alices altes Teil wird unbrauchbar, da die SE ihr entsprechendes Teil zerstört hat. Das Eigentum an den Bitcoins hat den Besitzer gewechselt, **ohne eine einzige Transaktion auf der Blockchain**.

Bob kann anschließend denselben Prozess wiederholen, um diese Bitcoins an Carol zu senden, und so weiter. Jeder Transfer funktioniert durch den Austausch der Puzzleteile, nicht durch eine on-chain-Bewegung von Mitteln.

### Warum ist es sicher?

Eine berechtigte Frage stellt sich: Was passiert, wenn die SE ihr altes Teil nicht wirklich zerstört?

Die Spark Entity ist keine einzelne Einheit: Es ist eine Gruppe unabhängiger Betreiber. Das Teil der SE wird nie von einem einzigen Betreiber gehalten. Der Austausch des Puzzles erfordert die Zusammenarbeit mehrerer Betreiber. Es genügt, dass **ein einziger Betreiber ehrlich ist**, um bei einem Transfer die Reaktivierung eines alten Puzzles zu verhindern. Kein einzelner Betreiber kann heimlich ein altes aktives Puzzle aufbewahren oder es später neu erstellen.

Darüber hinaus verfügt Spark über einen Mechanismus zur einseitigen Entnahme: Sie können Ihre Bitcoins jederzeit on-chain zurückholen, ohne die Zusammenarbeit der SE. Dieser Sicherheitsmechanismus ist ein fester Bestandteil der Spark-Architektur und garantiert, dass Sie niemals vom Netzwerk abhängig sind, um auf Ihre Mittel zuzugreifen.

### Spark vs. Lightning Network

Spark und Lightning stehen nicht im Wettbewerb: Sie sind **komplementär**. Blitz Wallet integriert beide, sodass Sie die Vorteile beider nutzen können.

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **Technologie**               | Statechains (Zustandsketten) | Zahlungskanäle        |
| **Kanalverwaltung**           | Nicht erforderlich           | Erforderlich          |
| **Eingehende Liquidität**     | Nicht erforderlich           | Erforderlich          |
| **Sofortige Transaktionen**   | Ja                           | Ja                    |
| **Self-custody**              | Ja                           | Ja                    |
| **Lightning-Kompatibilität**  | Ja (über atomic swaps)       | Nativ                 |

Das Lightning Network bleibt ein hervorragendes Protokoll für sofortige Zahlungen, aber es bringt technische Einschränkungen mit sich (Kanalverwaltung, eingehende Liquidität, Online-Node...), die Anfänger abschrecken können. Spark beseitigt diese Einschränkungen und bleibt dabei mit Lightning kompatibel.

## Installation und Konfiguration

In diesem Tutorial basieren wir auf der Android-Version von Blitz Wallet, aber alle unten vorgestellten Prozesse gelten ebenso für iOS.

![installation](assets/fr/01.webp)

Da Blitz Wallet eine Self-Custody-Wallet ist, haben Sie die Wahl zwischen **einer neuen Wallet erstellen** oder **eine Wiederherstellungsphrase importieren** (12 oder 24 Wörter) einer bestehenden Wallet.

Hier entscheiden wir uns für die Erstellung einer neuen Wallet. Im Folgenden finden Sie unsere Empfehlungen zur Sicherung Ihrer Wiederherstellungsphrase:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **WICHTIG**: Diese 12 oder 24 Wiederherstellungswörter sind **der einzige Zugangsschlüssel zu Ihren Bitcoins**. Blitz ist eine self-custodial Wallet: Weder Blitz noch Spark haben Zugang zu Ihrer Wiederherstellungsphrase oder Ihren Mitteln. Wenn Sie diese Wörter verlieren, verlieren Sie unwiderruflich den Zugang zu Ihren Bitcoins. Teilen Sie sie mit niemandem: Jeder, der sie besitzt, kann Ihre Bitcoins ausgeben.

Erstellen Sie anschließend einen **PIN-Code**, um den Zugang zu Ihrer Wallet zu sichern.

![setup-wallet](assets/fr/02.webp)

## Erste Schritte mit Blitz

Transaktionen mit Blitz durchzuführen ist intuitiver als bei den meisten anderen Bitcoin-Wallets. Die Benutzeroberfläche ist minimalistisch und konzentriert sich auf drei Hauptaktionen: Senden, Scannen und Empfangen.

### Bitcoins empfangen

Um Bitcoins auf Ihrer Blitz-Wallet zu empfangen, klicken Sie auf das Symbol **"Pfeil nach unten"** (↓), geben Sie den Betrag in Satoshis ein, den Sie empfangen möchten, fügen Sie eine optionale Beschreibung hinzu, und die Wallet generiert eine Rechnung (Invoice), die Sie an Ihren Absender weitergeben können.

⚠️ **HINWEIS**: Der Satoshi (oder "Sat") ist die kleinste Einheit von Bitcoin: **1 Bitcoin = 100 000 000 Satoshis**.

Eine der Besonderheiten von Blitz Wallet ist die Unterstützung mehrerer Netzwerke und Protokolle des Bitcoin-Ökosystems:

- **Lightning Network**: Eine der Zusatzschichten von Bitcoin, die sofortige Mikrozahlungen mit sehr geringen Gebühren ermöglicht. Ideal für kleine alltägliche Beträge.

- **Bitcoin (on-chain)**: Die Haupt-Blockchain des Bitcoin-Protokolls, geeignet für Transaktionen mit größeren Beträgen, bei denen maximale Sicherheit und Endgültigkeit Priorität haben.

- **Liquid Network**: Eine Sidechain (parallele Kette) von Bitcoin, entwickelt von Blockstream, die schnelle und vertrauliche Transaktionen mit Liquid Bitcoin (L-BTC) ermöglicht.

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Standardmäßig generiert Blitz eine Lightning-Rechnung, aber Sie können das Netzwerk wählen, auf dem Sie Ihre Satoshis empfangen möchten, indem Sie auf die Schaltfläche **"Choose format"** (Format wählen) klicken.

![receive-sats](assets/fr/03.webp)

### Kontakte erstellen

Blitz Wallet vereinfacht das wiederkehrende Senden von Bitcoins dank seines Kontaktsystems.

Im Menü **Contacts** können Sie Blitz-Benutzernamen oder Lightning-Adressen (LNURL) speichern, mit denen Sie häufig interagieren.

So können Sie Satoshis an diese Adressen mit wenigen Klicks senden, ohne jedes Mal einen QR code scannen oder manuell eine Adresse eingeben zu müssen.

### Bitcoins senden

Neben den klassischen Methoden zum Senden von Bitcoin (QR code scannen, manuelle Adresseingabe) bietet Blitz mehrere praktische Optionen:

- **Aus einem Bild** (*From Image*): Importieren Sie einen QR code aus Ihrer Fotogalerie.
- **Aus der Zwischenablage** (*From Clipboard*): Fügen Sie eine zuvor kopierte Adresse oder Rechnung ein.
- **Manuelle Eingabe** (*Manual Input*): Geben Sie direkt eine Bitcoin-Adresse, eine Lightning-Rechnung oder eine lesbare Adresse ein (zum Beispiel `benutzer@walletofsatoshi.com`).
- **Aus Ihren Kontakten**: Wählen Sie einen vorgespeicherten Empfänger, um mit wenigen Klicks zu senden.

Im Menü **Wallet** klicken Sie auf die Schaltfläche **"Pfeil nach oben"** (↑), wählen Sie Ihre Sendemethode, geben Sie den zu sendenden Betrag ein, fügen Sie eine Beschreibung hinzu und bestätigen Sie die Transaktion.

Der Mindestbetrag für eine Sendung beträgt derzeit **1 000 Satoshis**.

![send-bitcoin](assets/fr/05.webp)

## Der Blitz-Store

Über den reinen Bitcoin-Transfer hinaus integriert Blitz Wallet einen Store, in dem Sie Ihre Bitcoins ausgeben können, um digitale Dienste direkt aus der Anwendung heraus zu kaufen.

Klicken Sie im Hauptmenü auf den Reiter **Store**, um den Store aufzurufen. Dort finden Sie auch einen Zugang zur Plattform **Bitrefill**, mit der Sie Geschenkkarten bei Tausenden von Händlern weltweit direkt mit Bitcoin kaufen können.

- **Künstliche Intelligenz**: Greifen Sie auf die neuesten generativen KI-Modelle (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) zu und bezahlen Sie Ihre Credits direkt in Satoshis. Verschiedene Tarife stehen je nach Bedarf zur Verfügung (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **Anonyme SMS**: Senden und empfangen Sie SMS weltweit, ohne Ihre persönliche Telefonnummer preiszugeben. Der Dienst wird in Satoshis pro gesendeter Nachricht abgerechnet.

![sms-credit](assets/fr/07.webp)

- **WireGuard VPN**: Schützen Sie Ihre Online-Privatsphäre mit einem WireGuard-VPN-Abonnement (wöchentlich, monatlich oder vierteljährlich), zahlbar in Bitcoin direkt über den Blitz-Store. Sie müssen lediglich die WireGuard-Client-App auf Ihrem Gerät herunterladen, um den Dienst zu nutzen.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet hinter den Kulissen: weiterführende Details

Hinter der Benutzerfreundlichkeit von Blitz Wallet verbirgt sich eine durchdachte technische Architektur, die mehrere Schichten des Bitcoin-Ökosystems kombiniert.

### Die Verteilung Ihres Guthabens

Blitz Wallet verwaltet Ihr Guthaben transparent, indem es Ihre Mittel je nach Bedarf auf die verschiedenen Protokolle verteilt. Wenn Ihr Guthaben unter 500 000 Satoshis liegt, nutzt Blitz das **Liquid Network** und atomare Tauschvorgänge (*atomic swaps*), um Ihnen ein flüssiges Erlebnis zu bieten und Transaktionen über das Lightning Network auch mit kleinen Beträgen zu ermöglichen.

Dieser Ansatz gewährleistet einen einfachen Einstieg für neue Benutzer, ohne dass sie die zugrunde liegenden Mechanismen verstehen müssen. Sie können die Verteilung Ihres Guthabens auf die verschiedenen Schichten im Menü **Einstellungen > Balance Info** einsehen.

![balance](assets/fr/09.webp)

### Der Lightning-Modus (optional)

Standardmäßig nutzt Blitz Wallet das Liquid Network und das Spark-Protokoll, um Ihnen ein flüssiges Erlebnis ohne technische Konfiguration zu bieten. Dennoch gibt Ihnen Blitz die Möglichkeit, den **Lightning-Modus** zu aktivieren, der automatisch einen Zahlungskanal öffnet, sobald Sie ein Guthaben von **500 000 Satoshis** (0,005 BTC) erreichen.

Um den Lightning-Modus zu aktivieren, gehen Sie in die **Einstellungen** und klicken Sie dann im Abschnitt **Technische Einstellungen** auf die Option **Node Info**.

![enable-lightning](assets/fr/10.webp)

Dank des Spark-Protokolls ist diese Aktivierung **optional**: Spark ermöglicht bereits Lightning-kompatible Zahlungen, ohne einen Kanal öffnen oder eingehende Liquidität verwalten zu müssen. Der native Lightning-Modus bleibt für fortgeschrittene Benutzer nützlich, die über ihren eigenen in die Anwendung integrierten Lightning-Node verfügen möchten.

### Point of Sale (PoS)

Blitz Wallet verfügt über eine **Point-of-Sale**-Funktion, die es Händlern ermöglicht, Bitcoin-Zahlungen direkt über die Anwendung zu akzeptieren.

Im Menü **Einstellungen > Point-of-sale** können Sie konfigurieren:

- Die eindeutige Kennung Ihres Geschäfts
- Die lokale Fiat-Währung, in der Preise angezeigt werden sollen
- Die Anweisungen für Ihre Mitarbeiter
- Die Trinkgeld-Option für Ihre Kunden

Ihre Kunden müssen lediglich den generierten QR code scannen, um ihre Bitcoin-Zahlung sofort durchzuführen.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Für die Erstellung dieses Tutorials verwendete Quellen:
- Blog von [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
