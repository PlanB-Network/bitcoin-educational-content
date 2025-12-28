---
name: BitcoinVoucherBot P2P
description: Wie man Bitcoin P2P mit BitcoinVoucherBot kauft und verkauft
---

![image](assets/cover.webp)



Wir hören immer noch von BitcoinVoucherBot, einem Telegram-Bot, der geschaffen wurde, um Bitcoin ohne [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) per SEPA-Überweisung zu kaufen. Leider ist der BitcoinVoucherBot in seiner zentralisierten Form ab November 2025 nicht mehr als Dienst ohne KYC verfügbar.



In diesem Leitfaden werden wir uns ansehen, wie die neue Implementierung funktioniert, die es Nutzern ermöglicht, Bitcoin direkt auf dem neuen P2P (Peer-To-Peer)-Marktplatz zu kaufen und zu verkaufen, also ohne KYC. Um neuen Beschränkungen entgegenzuwirken, die zunehmend die digitale Freiheit und Privatsphäre bedrohen, haben die Entwickler diese Erweiterung geschaffen, die es den Nutzern ermöglicht, Bitcoin mit einem hohen Maß an Anonymität über P2P (Peer-To-Peer) zu kaufen und zu verkaufen. Schauen wir uns gemeinsam an, wie diese neue Austauschmethode funktioniert.



Um den Dienst zu nutzen, müssen Sie Überweisungen über Lightning Network tätigen. Vergewissern Sie sich also, dass Sie einen wallet haben, der dieses Protokoll unterstützt und es Ihnen ermöglicht, eine "LNURL" oder einen "Lightning Address" zu verwenden, um Gelder zu empfangen und zu senden.



Unter den unterstützten Geldbörsen finden wir:





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Pflegedienst)
- [Wallet von Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Verwahrer mit Tausch gegen Nicht-Verwahrer)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



Oder jeder wallet, der einen "Lightning Address" hat und eine Bolt11-Rechnung erzeugt. Geldbörsen, die generate eine Bolt12-Rechnung erzeugen, werden derzeit nicht unterstützt. Für weitere Informationen siehe die Definition von [Bolt] (https://planb.academy/resources/glossary/bolt).



Für dieses Lernprogramm werden wir Wallet of Satoshi verwenden, da es leicht zu benutzen ist.



**Vorsicht**: Wallet of Satoshi ist zwar bei Anfängern beliebt, aber ein Depot mit begrenzter Kontrolle über die Gelder; verwenden Sie es nur vorübergehend und wechseln Sie sofort zu einem Nicht-Depot, um volle Souveränität zu erhalten. Ab Oktober 2025 umfasst es einen stabilen Selbstverwahrungsmodus weltweit auf iOS/Android (aktualisieren Sie die App), mit autonomen privaten Schlüsseln, Wechsel zwischen den Modi, benutzerdefinierten Lightning-Adressen und seed 12-Wort-Backup. Es bleibt jedoch eine Zwischenlösung bis zur Konsolidierung, wobei für die langfristige Verwaltung wallet ohne Verwahrung vorzuziehen ist.



Sehr gut! Jetzt können wir mit unserer Reise beginnen, die Sie Schritt für Schritt durch die Erstellung Ihres Kontos, die Verwaltung von Kauf- und Verkaufsspielen und die Nutzung Ihres geschützten Bereichs führen wird.



## Wallet und Immatrikulation



Wenn Sie es noch nicht auf Ihrem Smartphone installiert haben, laden Sie zunächst Wallet of Satoshi herunter.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Wenn Sie Wallet of Satoshi noch nie benutzt haben und verstehen wollen, wie es funktioniert, empfehle ich Ihnen, diese Anleitung zu befolgen, damit Sie es richtig aktivieren und sicher sichern können.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Jetzt, wo Ihr wallet fertig ist, können Sie anfangen, eine kleine Menge sats zu senden. Denken Sie daran, dass Sie, um Ihre P2P (Peer-to-Peer)-Plattformregistrierung abzuschließen, 1000 sats als Kontrollmaßnahme senden müssen: Dies dient dazu, eine Barriere gegen Angriffe vom Typ "Phantomspiel" (Betrug) zu schaffen und zu verhindern, dass sich jemand ohne Spamfilter anmeldet.



![image](assets/it/02.webp)



Wir können nun die P2P (Peer-To-Peer)-Plattform öffnen, um mit der Registrierung fortzufahren. Sie können sich von Desktop-PCs oder Browsern auf Smartphones, über den Telegram BitcoinVoucherBot oder über .onion-Links anmelden, um ein noch höheres Maß an Privatsphäre zu gewährleisten.



wenn du dich für den Tor.onion-Link entscheidest, empfehle ich auch "Tor Browser". Wenn du es noch nicht kennst, kannst du unter diesem Link mehr darüber erfahren:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Wählen Sie nun aus, wie Sie die Plattform erreichen wollen.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Browser Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Sie werden dann zur Hauptseite weitergeleitet.



drücken Sie auf "Get Starter", um sofort loszulegen



![image](assets/it/03.webp)



Auf dem nächsten Bildschirm müssen Sie ein Kennwort auswählen und eingeben (Feld A) und dann wiederholen (Feld B). Ich empfehle Ihnen, dieses Passwort sofort auf einem Sicherungsmedium zu speichern, z. B. auf einem sicheren digitalen Gerät wie dem "Bitwarden":



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

oder speichern Sie Ihr Passwort auf einem Papiermedium (**Warnung**: dies ist keine gute Lösung, aber für eine vorübergehende Lösung durchaus geeignet).



Aktivieren Sie das Kontrollkästchen, in dem Sie angeben, dass Sie kein Roboter sind (Feld C). Bitte beachten Sie: Aktivieren Sie die RSA-Verschlüsselung nur, wenn Sie genau wissen, was sie ist und wie sie funktioniert. Sie müssen zu diesem Zeitpunkt noch nichts tun. Klicken Sie auf "Avatar generieren" (Feld D).



![image](assets/it/04.webp)



Nun müssen Sie die 1000 sats bezahlen, um die Anmeldung abzuschließen.



1. Fangen Sie oben an und sehen Sie zuerst Ihre zufällig generierte und äußerst wichtige "Avatar-ID" Speichern Sie sie sorgfältig, so wie ich es Ihnen für das Passwort geraten habe.


2. Sie müssen dann Ihren "Lightning Address" in das Feld unten eingeben. Dies ermöglicht Ihnen, Zahlungen zu erhalten, wenn Sie Bitcoin kaufen, oder Erstattungen zu erhalten. Wenn Sie Wallet oder Satoshi verwenden, können Sie Ihren Address kopieren, indem Sie auf "Erhalten" klicken.


3. Markieren Sie das Kontrollkästchen, in dem Sie angeben, dass Sie kein Roboter sind.


4. Bezahlen Sie 1000 sats, um Zugang zu Ihrem geschützten Bereich zu erhalten. Wenn Sie es nicht einrahmen können, klicken Sie mit der Maus darauf (auf dem PC) oder tippen Sie mit dem Finger darauf (auf Browser/Telegram-Smartphones), um die Adresse zu kopieren, die Sie in Wallet of Satoshi einfügen und die Rechnungszahlung abschließen müssen.



![image](assets/it/05.webp)



Dies ist Ihre LNURL Address.



![image](assets/it/06.webp)



Herzlichen Glückwunsch!!! Sie haben Ihren Avatar dauerhaft erstellt und können die Zusammenfassung hier einsehen. Ich empfehle Ihnen noch einmal, sowohl Ihren Avatar als auch Ihr Passwort sorgfältig zu speichern, wie ich es bereits vorgeschlagen habe.



Klicken Sie auf "I've saved my credentials, continue" (übersetzt: "Ich habe meine Anmeldedaten gespeichert, fahren Sie fort")



![image](assets/it/07.webp)



Sie befinden sich nun im Herzen der Plattform, wo Sie alle Handelsspiele mit ihren Details sehen können. Für eine bessere Übersicht sehen Sie unten die Bilder, die auf der Website von Desktop-Computern zu sehen sind.





- "Typ" ("Type") definiert, ob es sich um einen "Verkauf" ("Sell") oder einen "Kauf" handelt
- "Betrag" ("Amount"): gibt an, wie viele sats der Nutzer verkauft, wenn es sich um eine Übereinstimmung des Typs "Sell" handelt, oder wie viele Bitcoin der Nutzer zu kaufen bereit ist, wenn es sich um eine Übereinstimmung des Typs "Buy" handelt.
- "BTC-Preis mit Marge" ("BTC Price with Margin"): zeigt den Preis unter Berücksichtigung der Marge, die über dem markierten Wert liegt.
- "Marge" ("Margin") ist der Prozentsatz, der auf den Marktpreis angewandt wird. Bei einem Minuszeichen (-) erhalten Sie einen Abschlag auf den Marktpreis, bei einem Pluszeichen (+) wird ein Aufschlag auf den Marktpreis vorgenommen.
- "Methode" ("Method") gibt an, mit welcher Methode der Nutzer bezahlt werden möchte.
- "Creator" ist der einzigartige Avatar, den der Nutzer auf der Plattform verwendet.
- "Rep" (Reputation) Die Reputationsstufe des Nutzers reicht von -5 unzuverlässig bis +5 extrem zuverlässig.
- "Status" ("Status"): gibt den Status der Übereinstimmung an. Im Beispiel-Screenshot scheinen alle Übereinstimmungen "Offen" ("Open") zu sein.
- "Ablauf" ("Expiration"): zeigt an, wie viel Zeit noch verbleibt, bevor das Spiel abläuft und abgebrochen wird, wenn es von niemandem gewählt wurde.



![image](assets/it/08.webp)



Klicken Sie oben rechts auf Ihren Avatar, um Ihr Profil aufzurufen.



![image](assets/it/09.webp)



Hier sehen Sie Ihren Avatarnamen, Ihre Benutzer-ID, das Erstellungsdatum und Ihren Ruf, der sich positiv oder negativ auf Ihr Verhalten in Verhandlungen auswirkt.



![image](assets/it/10.webp)



Im Abschnitt Einstellungen können Sie Ihre "Lightning Address", die Sie bei der Registrierung eingegeben haben, einsehen und gegebenenfalls ändern. Sie haben auch die Möglichkeit, einen öffentlichen Schlüssel zu erstellen, der, wie bereits erwähnt, nur dann eingerichtet werden sollte, wenn Sie über die entsprechenden Kenntnisse verfügen. Er wird verwendet, um die Nachrichten zu verschlüsseln, die Sie direkt von Ihrem Computer aus mit Ihrem Gesprächspartner austauschen werden.



Die Telegram-Benachrichtigungsfunktion ist sehr empfehlenswert. Wenn Sie sie aktivieren, erscheint ein QR-Code, den Sie mit der Telegram-App einrahmen können: Auf diese Weise erhalten Sie Echtzeit-Benachrichtigungen über alle Aktionen im Zusammenhang mit Ihren Spielen, direkt im Bot-Chat auf Telegram.



![image](assets/it/11.webp)



Schließlich finden Sie Ihren Empfehlungsbereich mit den Einnahmen, die durch die von Ihnen eingeladenen Nutzer erzielt werden. Von hier aus können Sie die Schaltfläche verwenden, um Ihren Link oder QR-Code zu teilen, und etwas weiter unten können Sie eine Liste von Übereinstimmungen einsehen, um Ihr Ansehen zusammen mit der entsprechenden Punktzahl zu verfolgen.



![image](assets/it/12.webp)



## Einen Auftrag zum Kauf von Bitcoin erstellen



Betreten Sie den Marktplatz: Klicken Sie in der Hauptnavigationsleiste auf das Einkaufswagen-Symbol "Marktplatz" ("Marketplace"), um das Bestellbuch zu öffnen. Starten Sie dann eine neue Bestellung: Drücken Sie die Schaltfläche "Neue Bestellung" ("New Order"), um den Vorgang zu starten.



![image](assets/it/13.webp)





- Bestelldaten einstellen:
- Wählen Sie die Option "Bitcoin kaufen" ("Bitcoin kaufen").
- Geben Sie die gewünschte Menge an sats ein.
- Definieren Sie die Preisspanne (zwischen -20% und +20% vom Marktwert).
- Wählen Sie die Zahlungsmethode (Instant SEPA, etc.).
- Gibt die bevorzugte Währung an.
- Auftrag bestätigen: Klicken Sie auf "Auftrag erstellen" ("Auftrag bestätigen"), um mit der Einreichung fortzufahren.



![image](assets/it/14.webp)



Anzahlung erforderlich: Zur Aktivierung der Bestellung ist eine Anzahlung in Höhe von 10 % des Gesamtbetrags zuzüglich einer Bearbeitungsgebühr erforderlich.




- Kautionszahlung: Bei der Erstellung des Auftrags erstellt das System automatisch eine Blitzrechnung. Die Anzahlung ist nur vorübergehend und wird zurückerstattet, wenn der Auftrag abgeschlossen ist.
- Hauptmerkmale:
- Kaution: 10% des Auftragswertes.
- Servicegebühr: Kosten für die Nutzung der Plattform.
- Zeitlimit: Sie haben 5 Minuten Zeit, um die Zahlung vorzunehmen, sonst verfällt die Transaktion.



![image](assets/it/15.webp)



Nach erfolgreicher Zahlung erscheint der Auftrag im Buch und ist für alle Nutzer sichtbar, die ihn auswählen und annehmen können. Um einen Verkaufsauftrag zu erstellen, brauchen Sie nur auf "Bitcoin verkaufen" zu klicken, die Menge an satoshi, die Sie verkaufen möchten, einzugeben, die Marge festzulegen, die Zahlungsmethode und die Währung auszuwählen und dann mit der 10%igen Anzahlung als Sicherheitsleistung fortzufahren. Sobald dies geschehen ist, wird Ihr Match in der Liste angezeigt.



![image](assets/it/16.webp)



## So nehmen Sie eine Bestellung an



1. Verkäufer können eine Liste aller verfügbaren Aufträge im Buch sehen.


2. Prüfen Sie die Details: Jede Bestellung enthält Informationen wie:




  - Menge von Bitcoin,
  - Marge auf den Preis,
  - Zahlungsmethode,
  - Ruf der Benutzer.



![image](assets/it/17.webp)



3. Klicken Sie auf den Auftrag, um das vollständige Blatt mit allen Informationen zu öffnen.


4. Drücken Sie auf "Bitcoin verkaufen" ("Sell Bitcoin"), um das Angebot anzunehmen.



![image](assets/it/18.webp)



## Kaution vom Verkäufer verlangt



Wenn der Auftrag angenommen wird, erstellt das System eine Rechnung zur Zahlung. Die Kaution umfasst:



- Der Gesamtbetrag der Bestellung,



- die Dienstleistungskommission.



Die Zahlung der Kaution muss innerhalb der festgelegten Frist erfolgen, andernfalls wird die Transaktion nicht bestätigt.



![image](assets/it/19.webp)



## Übermittlung von Zahlungsanweisungen



Nach der Einzahlung erscheint die Transaktion im persönlichen Dashboard des Verkäufers, der die Details an den Käufer weitergeben muss, um die Zahlung in Fiat-Währung abzuschließen.



1. Der Verkäufer zeigt die aktive Transaktion in seinem Panel an.


2. Klicken Sie auf "Zahlungsanweisungen einreichen"


3. Geben Sie alle erforderlichen Informationen für die Fiat-Zahlung ein (IBAN, Empfänger, Adresse, Grund der Zahlung usw.).


4. Klicken Sie auf "Nachricht senden"("Send Message"), um die Daten an den Käufer zu übermitteln.



![image](assets/it/20.webp)



## Zahlungsverfahren



Der Käufer erhält im Chat der Plattform eine Nachricht mit allen notwendigen Daten, um die Zahlung in Fiat-Währung vorzunehmen:




- Bankverbindung: IBAN mit Name und Anschrift des Kontoinhabers des Verkäufers.
- Genauer Betrag: genauer Fiat-Betrag, der überwiesen werden soll.
- Ursache/Beschreibung: Text, der in die Transaktion aufgenommen werden muss.
- Frist: Frist, bis zu der die Zahlung erfolgen muss.



Die Überweisung findet außerhalb des P2P-Systems statt und muss über das eigene Bankinstitut abgewickelt werden.



⚠️ **Wichtiger Hinweis:** Die Bestätigung auf der Plattform sollte erst dann erfolgen, wenn Sie die Überweisung oder Fiat-Zahlung über Ihre Bank tatsächlich veranlasst haben.



![image](assets/it/21.webp)



## Bestätigung der Zahlung fiat



Dieser Schritt ist für den Käufer von entscheidender Bedeutung und sollte erst durchgeführt werden, nachdem er sich vergewissert hat, dass die Zahlung tatsächlich erfolgt ist.



1. Empfangsdaten: Der Käufer hat die Zahlungsanweisungen des Verkäufers erhalten.


2. Zahlungsabwicklung: Die Überweisung erfolgt vom eigenen Bankkonto.


3. Verifizierung: Überprüfung, ob der Vorgang korrekt ausgeführt wurde.


4. Bestätigung auf der Plattform: Klicken Sie auf der Handelsseite auf "Confirm fiat payment" ("Bestätigen Sie die Fiat-Zahlung").


Die Schaltfläche "Confirm Payment fiat" (Zahlung bestätigen) wird im Transaktionsbereich angezeigt und sollte erst verwendet werden, nachdem überprüft wurde, ob die Zahlung tatsächlich gesendet wurde.



![image](assets/it/22.webp)



Im letzten Schritt bestätigt der Verkäufer den Erhalt der Zahlung in Fiat, woraufhin die Satze an den Käufer freigegeben werden.



![image](assets/it/23.webp)



## Schlussfolgerung



In der Hoffnung, dass dieses Tutorial Ihnen dabei hilft, eine neue Methode zu nutzen, um Bitcoins zu handeln oder auch nur zu kaufen, entweder für Ihren eigenen Wertespeicher oder um tägliche Zahlungen ins Leben zu rufen. Dennoch bleibt es eine Tür, die es zu erforschen gilt, um mit dem umzugehen, was in unserer digitalen Welt passieren wird.



Die Schlinge, die uns die Kontrollorgane um den Hals legen, zieht sich immer enger, um ein zunehmend kontrolliertes Internet zu schaffen. Wenn Sie P2P kaufen, bleiben Ihre Einkäufe völlig anonym, hinterlassen keine Spuren und werden nicht von Dritten verfolgt.