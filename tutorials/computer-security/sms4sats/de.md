---
name: SMS4Sats
description: Anonymes Empfangen und Senden von SMS durch Bezahlung in Bitcoin Lightning
---

![cover](assets/cover.webp)



Die SMS-Verifizierung ist für viele Online-Dienste ein Muss geworden. Ob es darum geht, ein Konto auf einer Plattform zu erstellen, eine Registrierung zu validieren oder eine Identität zu bestätigen, Websites verlangen fast systematisch eine Telefonnummer. Diese weit verbreitete Praxis stellt ein großes Problem für alle dar, die ihre Privatsphäre schützen wollen: Ihre persönliche Nummer wird zu einer dauerhaften Kennung, die Ihre verschiedenen digitalen Aktivitäten mit Ihrer wirklichen Identität verknüpft und unerwünschten Werbeanrufen Tür und Tor öffnet.



**SMS4Sats** reagiert auf dieses Problem, indem es temporäre Telefonnummern für den Empfang und Versand von SMS-Nachrichten anbietet. Der Dienst zeichnet sich durch sein registrierungsfreies Modell und die ausschließliche Bitcoin-Zahlung über Lightning Network aus. Für ein paar Satoshis erhalten Sie eine Einwegnummer, mit der Sie eine Registrierung bestätigen können, ohne jemals Ihre persönliche Nummer preiszugeben.



Diese Anleitung führt Sie durch die drei SMS4Sats-Funktionen: Empfang einer Bestätigungs-SMS, anonymer SMS-Versand und Anmietung einer temporären Nummer für mehrere Stunden.



## Was ist SMS4Sats?



SMS4Sats ist ein Online-Dienst, der unter [sms4sats.com](https://sms4sats.com) zugänglich ist und die anonyme Verwaltung von SMS gegen Bezahlung in Bitcoin Lightning ermöglicht. Der Dienst bietet drei verschiedene Funktionen: den Empfang von einmaligen Verifizierungscodes, den Versand von SMS an beliebige Nummern und die Anmietung von temporären Nummern für mehrere Stunden.



### Philosophie und Betriebsmodell



Das Projekt ist so konzipiert, dass maximale Vertraulichkeit und finanzielle Souveränität gewährleistet sind. Da keine Kontoerstellung erforderlich ist und nur Bitcoin Lightning-Zahlungen akzeptiert werden, entfällt bei SMS4Sats vollständig die Notwendigkeit, persönliche Daten anzugeben. Keine E-Mail-Adresse, keine Kreditkarte, keine persönlichen Informationen sind erforderlich. Nur die Lightning-Zahlung ist erforderlich, um auf die Dienste zuzugreifen.



Der Dienst unterstützt über 400 Websites und Anwendungen in rund 120 Ländern und deckt damit die meisten gängigen Überprüfungsanforderungen ab. Diese umfassende geografische Abdeckung ermöglicht die Validierung von Registrierungen auf einer Vielzahl von Plattformen, von sozialen Netzwerken bis hin zu Messaging-Diensten.



### Bedingtes Zahlungsmodell



SMS4Sats verwendet für seine SMS-Empfangsfunktionalität bedingte Blitzrechnungen (hodl invoices). Dieser Mechanismus stellt sicher, dass Sie nur belastet werden, wenn die SMS tatsächlich empfangen wird. Wenn innerhalb der zugewiesenen Zeit (maximal 20 Minuten) keine Nachricht ankommt, wird die Zahlung automatisch storniert und die Satoshis werden an Ihren wallet zurückgegeben. Diese Garantie gilt nicht für die Sende- und Mietfunktionen, die nicht erstattungsfähig sind.



## Die drei SMS4Sats-Merkmale



Die Oberfläche von SMS4Sats ist in drei Registerkarten unterteilt, die drei verschiedenen Verwendungszwecken entsprechen: **RECEIVE**, um Verifizierungscodes zu empfangen, **SEND**, um anonyme SMS zu senden, und **RENT**, um eine temporäre Nummer zu mieten.



### Empfangen einer SMS



Die Hauptfunktion ermöglicht es Ihnen, eine temporäre Nummer zu erhalten, um einen einmaligen Verifizierungscode zu bekommen. Sobald der Code empfangen und verwendet wurde, wird die Nummer dauerhaft deaktiviert.



### Eine SMS senden



Mit dieser Funktion können Sie eine SMS an eine beliebige Telefonnummer senden, ohne Ihre Identität preiszugeben. Der Empfänger erhält die Nachricht von einer anonymen Nummer.



### Eine Nummer mieten



Für Benutzer, die mehrere SMS-Nachrichten auf einer einzigen Nummer empfangen müssen, bietet SMS4Sats eine zeitlich begrenzte Mietoption an. Mit dieser Option können Sie während des Mietzeitraums mehrere Nachrichten empfangen und versenden.



**Hinweis zu den Preisen** : Die in dieser Anleitung angegebenen Preise sind Richtpreise. Sie variieren je nach Land der Nummer, dem Zieldienst und der aktuellen Nachfrage. Eine SMS an Telegram Frankreich kann zum Beispiel je nach Bedingungen zwischen 1.500 und 5.000 Satoshis kosten. Prüfen Sie immer den genauen Betrag der Blitzrechnung, bevor Sie zahlen.



## Erhalten Sie eine Bestätigungs-SMS



Schauen wir uns im Detail an, wie man SMS4Sats verwendet, um einen Verifizierungscode zu erhalten, veranschaulicht durch die Einrichtung eines Telegram-Kontos.



### Schritt 1: Land und Dienst auswählen



Gehen Sie zu [sms4sats.com](https://sms4sats.com) und bleiben Sie auf der Registerkarte **RECEIVE**. Wählen Sie das Land der gewünschten Nummer aus dem Dropdown-Menü. Wenn der Zieldienst Ihres Abonnements aufgeführt ist, wählen Sie ihn aus, um die Empfangschancen zu optimieren.



![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)



In diesem Beispiel wählen wir Frankreich als Land und Telegram als Zieldienst. Klicken Sie auf **NEXT**, um mit dem nächsten Schritt fortzufahren.



### Schritt 2: Bezahlen Sie die Lightning-Rechnung



Eine Blitzrechnung wird in Form eines QR-Codes angezeigt. Der Betrag variiert je nach Land und ausgewähltem Dienst. Scannen Sie den QR-Code mit Ihrem Lightning wallet oder kopieren Sie die Rechnung, um manuell zu bezahlen.



![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)



Beachten Sie die wichtige Meldung: "Kein SMS-Code = Keine Zahlung". Wenn Sie keine SMS erhalten, wird Ihre Zahlung automatisch storniert und innerhalb von maximal 20 Minuten zurückerstattet.



### Schritt 3: Ermitteln der vorläufigen Nummer



Sobald die Zahlung bestätigt wurde, wird die temporäre Telefonnummer sofort angezeigt. Ein Zähler zeigt die verbleibende Zeit bis zum Erhalt der SMS an.



![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)



Kopieren Sie diese Nummer (hier +33 7 74 70 09 66), um sie für den Dienst zu verwenden, für den Sie sich anmelden möchten.



### Schritt 4: Verwenden Sie die Nummer des Zieldienstes



Geben Sie die vorläufige Nummer in der Anwendung oder auf der Website ein, auf der Sie Ihr Konto erstellen. In unserem Beispiel Telegram geben Sie die Nummer ein, bestätigen sie und warten auf den Verifizierungscode.



![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)



Der Prozess ist identisch mit der herkömmlichen Registrierung: Sie geben die Nummer ein, Telegram sendet einen Verifizierungscode per SMS, und dann schließen Sie die Kontoerstellung ab.



### Schritt 5: Abrufen des Verifizierungscodes



Kehren Sie zur SMS4Sats-Schnittstelle zurück. Sobald die SMS eingegangen ist, wird der Aktivierungscode automatisch angezeigt. Klicken Sie auf **CODE KOPIEREN**, um ihn einfach zu kopieren.



![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)



Geben Sie diesen Code beim Zieldienst ein, um Ihre Anmeldung abzuschließen. Die temporäre Nummer wird dann dauerhaft deaktiviert.



## Senden Sie eine anonyme SMS



Mit SMS4Sats können Sie auch SMS-Nachrichten an beliebige Nummern senden, ohne Ihre Identität preiszugeben.



### Schritt 1: Verfassen der Nachricht



Klicken Sie auf die Registerkarte **SENDEN**. Geben Sie die Zielrufnummer mit ihrer internationalen Vorwahl ein und schreiben Sie Ihre Nachricht (maximal 1600 Zeichen).



![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)



Klicken Sie auf **NEXT**, um mit der Zahlung fortzufahren.



### Schritt 2: Bezahlen und senden



Bezahlen Sie die angezeigte Lightning-Rechnung. Sobald die Zahlung bestätigt wurde, wird die SMS sofort an den Empfänger gesendet.



![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)



Es wird ein Bestätigungscode angezeigt, um zu bestätigen, dass die Nachricht gesendet wurde. Der Empfänger wird die SMS von einer anonymen Nummer erhalten.



## Vorübergehend eine Nummer mieten



Für Anwendungen, die mehrere SMS-Nachrichten auf derselben Nummer erfordern, können Sie mit der Funktion RENT eine Nummer für mehrere Stunden mieten.



### Konfiguration der Vermietung



Klicken Sie auf die Registerkarte **RENT**. Wählen Sie Land und Dauer.



![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)



**Wichtige Hinweise:**




- Die Preise variieren je nach Land und Dauer des Aufenthalts
- Mieten sind nicht erstattungsfähig**, im Gegensatz zu einmaligen SMS-Nachrichten
- Gemietete Nummern funktionieren im Allgemeinen nicht mit Telegram
- Diese Option eignet sich für das Abonnement mehrerer Dienste nacheinander



Nachdem Sie auf **NEXT** geklickt und die Lightning-Rechnung bezahlt haben, erhalten Sie eine Nummer, die Sie für die Dauer des Mietzeitraums nutzen können, um SMS-Nachrichten zu empfangen und zu versenden.



## Vorteile und Grenzen



### Höhepunkte



**Keine persönlichen Daten erforderlich**: Das Modell der Nichtregistrierung garantiert, dass keine persönlichen Daten erhoben werden.



**Drei zusätzliche Funktionen**: Empfangen, Senden und Mieten decken die meisten Bedürfnisse ab.



**Zahlung nur in Bitcoin** : Lightning Network erlaubt sofortige und pseudonyme Transaktionen.



**Automatische Erstattung**: Beim Empfang von SMS-Nachrichten garantiert das hodl-Rechnungssystem, dass Sie nur bezahlen, wenn die SMS ankommt.



### Zu berücksichtigende Zwänge



**Relative Sicherheit des SMS-Kanals**: SMS-Codes sind keine zuverlässige Authentifizierungsmethode und sollten nicht für sensible Konten verwendet werden.



**Variable Kompatibilität**: Viele Websites erkennen und blockieren virtuelle Nummern. Es können mehrere Versuche erforderlich sein.



**Nicht wiederverwendbare Nummern**: Nach einmaligem Gebrauch wird die Nummer recycelt und kann nicht wiederverwendet werden.



**Nicht erstattungsfähige Mietangebote**: Anders als bei einmaligen SMS-Nachrichten gibt es bei Mietnachrichten keine Geld-zurück-Garantie.



## Bewährte Praktiken



### Verwende Tor für mehr Privatsphäre



SMS4Sats ist über [Tor](sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion) erreichbar. Mit dieser Konfiguration wird Ihre IP-Adresse beim Zugriff auf den Dienst verschleiert.



### Kritische Konten meiden



Verwenden Sie niemals eine Wegwerfnummer für Ihre wichtigen Konten (Bank, Haupt-E-Mail). Wenn diese Plattformen verlangen, dass Sie Ihre Nummer zu einem späteren Zeitpunkt erneut validieren, verlieren Sie den Zugang zu dem Konto.



### Trennen Sie Ihre digitalen Identitäten



Für pseudonyme Konten kombinieren Sie die temporäre Nummer mit einer Wegwerf-E-Mail-Adresse und einem Browser, den Sie normalerweise nicht benutzen.



### Wählen Sie eine solide 2FA



Sobald Ihr Konto erstellt ist, aktivieren Sie stärkere Authentifizierungslösungen: TOTP-Anwendung (Aegis, Ente Auth) oder FIDO2 physischer Sicherheitsschlüssel.



## Schlussfolgerung



SMS4Sats ist eine Komplettlösung für die Verwaltung vertraulicher SMS. Ob Sie einen Verifizierungscode erhalten, eine anonyme Nachricht senden oder eine temporäre Nummer mieten möchten, der Dienst erfüllt dank der Bezahlung in Bitcoin Lightning eine breite Palette von Vertraulichkeitsanforderungen.



Beachten Sie jedoch seine Grenzen: Der Dienst garantiert keine absolute Anonymität und ist nicht für sensible oder langfristige Konten geeignet. Bei kluger Nutzung und im Bewusstsein seiner Grenzen ist SMS4Sats ein praktisches Instrument, um die Kontrolle über Ihre Telefonkommunikation zurückzugewinnen.



## Ressourcen





- [SMS4Sats offizielle Website](https://sms4sats.com)
- [Service FAQ](https://sms4sats.com/faq)
- [Tor-Adresse](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)