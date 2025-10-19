---
name: Ingwer Wallet
description: Open-Source, selbstverwaltete Bitcoin Wallet Software, Fork von Wasabi Wallet, Integration von Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet ist ein quelloffenes, nicht-verwahrendes Bitcoin-Portfolio mit Schwerpunkt auf Vertraulichkeit und Datenschutz. Es entstand als Fork aus Wasabi Wallet (nach Version 2.0.7.2 - MIT-Lizenz).



Ginger Wallet behält die technische Architektur von Wasabi bei, fügt aber ein paar spezifische Funktionen hinzu. Laut der [Ginger Wallet-Dokumentation] (https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet) legt Wasabi den Schwerpunkt auf **Autonomie und Kontrolle**, während Ginger sich auf **Benutzerfreundlichkeit, Sicherheit und ein vereinfachtes Erlebnis** konzentriert, um es auch für diejenigen zugänglich zu machen, die mit technischen Aspekten weniger vertraut sind.



Ginger Wallet ist eine Wallet-Software nur für Computer (keine mobile Anwendung).



## Was ist CoinJoin?



CoinJoin** ist eine besondere Art der Bitcoin-Transaktionsstruktur, die mehrere Teilnehmer in einer einzigen gemeinsamen Transaktion zusammenführt. Bei diesem Mechanismus werden die Eingaben verschiedener Nutzer in einer gemeinsamen Transaktion vermischt, was die Rückverfolgung von Geldern extrem erschwert - wenn nicht sogar oft unmöglich macht, wenn es richtig gemacht wird. Dadurch wird es für einen außenstehenden Beobachter fast unmöglich, die Herkunft und den Bestimmungsort der beteiligten Bitcoins mit Sicherheit zu bestimmen, anders als bei herkömmlichen Bitcoin-Transaktionen.



Für Sie, den Nutzer, trägt CoinJoin zur Wahrung Ihrer Vertraulichkeit bei. Wenn Sie zum Beispiel eine Spende von 10.000 Sats auf einem Bitcoin Address erhalten, kann der Absender diese Gelder zurückverfolgen und in einigen Fällen ableiten, dass Sie eine größere Menge an Bitcoins besitzen, oder Ihre Aktivitäten beobachten. Wenn Sie nach dieser Spende von 10.000 Sats eine CoinJoin machen, unterbrechen Sie die Rückverfolgbarkeit: Der Absender kann aus dieser Zahlung keine Informationen mehr über Sie ableiten.



Das Chaumian CoinJoin bietet ein hohes Maß an Sicherheit, da die Gelder jederzeit unter der alleinigen Kontrolle des Nutzers bleiben. Selbst die Betreiber der koordinierenden Server können die Bitcoins der Teilnehmer unter keinen Umständen abzweigen. Weder Nutzer noch Koordinatoren müssen sich gegenseitig vertrauen: Jeder behält die Kontrolle über seine privaten Schlüssel und ist allein berechtigt, Transaktionen zu validieren. Daher kann sich kein Dritter während einer CoinJoin Ihre Bitcoins aneignen oder eine direkte Verbindung zwischen Ihren Eingaben und Ausgaben herstellen.



Um mehr über CoinJoin zu erfahren, besuchen Sie den Kurs BTC 204 der Plan ₿ Academy:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Ginger Wallet installieren



Um Ginger Wallet zu installieren, besuchen Sie die Website [Ginger Wallet] (https://gingerwallet.io).



Drücken Sie **Download**, um die richtige Version für Ihren Computer (Windows / MacOs / Linux) herunterzuladen.



![screen](assets/fr/03.webp)



Eine andere Möglichkeit ist, das Projekt auf [GitHub] (https://github.com/GingerPrivacy/GingerWallet/releases) herunterzuladen.



![screen](assets/fr/04.webp)



Führen Sie dann das Installationsprogramm aus.



![screen](assets/fr/05.webp)




## Parameter-Einstellungen



### Vorläufige Konfigurationen



Öffnen Sie Ginger Wallet, wählen Sie Ihre bevorzugte Sprache.



![screen](assets/fr/06.webp)



Ginger erinnert Sie von Anfang an an die Kosten, die mit dem CoinJoin-Verfahren verbunden sind.



![screen](assets/fr/07.webp)



Drücken Sie dann **Start** und dann **Neu**, um ein neues Portfolio zu erstellen.



![screen](assets/fr/08.webp)



Speichern und bestätigen Sie anschließend Ihre seedphrase.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Für zusätzliche Sicherheit bietet der Ginger Wallet die Möglichkeit, einen passphrase hinzuzufügen.



![screen](assets/fr/11.webp)



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Diese passphrase wird, sobald sie hinzugefügt wurde, jedes Mal angefordert, wenn Sie versuchen, auf Ihr Portfolio zuzugreifen.



![screen](assets/fr/12.webp)



Ginger aktiviert automatisch die Standardeinstellung **CoinJoin**, wenn Sie Ihr Portfolio erstellen. Sie werden darüber informiert und können die Einstellung dann an Ihre Bedürfnisse anpassen.



![screen](assets/fr/13.webp)




### Allgemeine Einstellungen



Sobald Sie Ihr erstes Portfolio erstellt haben, werden Sie zu Gingers Interface Wallet weitergeleitet.



![screen](assets/fr/14.webp)



Aktivieren Sie den **Diskretmodus**, wenn Sie die Salden in Ihren Geldbörsen verbergen möchten.



![screen](assets/fr/15.webp)



Sie können mehrere Portfolios auf der Ginger Wallet erstellen. Klicken Sie einfach auf **Portfolio hinzufügen**.



![screen](assets/fr/16.webp)



Ginger unterstützt die Verwendung von Hardware-Portfolios über den Bitcoin core-Standard Interface, obwohl eine direkte Integration von oder zu einem Hardware-Portfolio noch nicht verfügbar ist.



Zu den kompatiblen Hardware-Portfolios gehören (aber nicht nur) :




- BLOCKSTREAM Jade
- Coldcard MK4
- Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Modell T
- Trezor Safe 3
- usw.



Klicken Sie nun auf **Einstellungen**.



![screen](assets/fr/17.webp)



Diese Einstellungen beziehen sich auf die Anwendung im Allgemeinen, und die dort vorgenommenen Konfigurationen gelten für alle Portfolios.



Unter **Einstellungen** finden Sie die Registerkarten :





- Allgemein**



![screen](assets/fr/18.webp)





- Erscheinungsbild



Auf dieser Registerkarte können Sie unter anderem die Sprache, die Währung und die Gebührenanzeigeeinheit (BTC/Satoshi) ändern.



![screen](assets/fr/19.webp)





- Bitcoin**



Auf dieser Registerkarte können Sie die Ausführung von Bitcoin Knots beim Start der Anwendung aktivieren, Ihr Netz (Main/RegTest) und Ihren Tarifanbieter (Mempool Space/BLOCKSTREAM info/Full node) auswählen usw.



![screen](assets/fr/20.webp)





- Sicherheitsmerkmale**



Auf der Registerkarte Sicherheit kannst du die Zwei-Faktor-Authentifizierung aktivieren, Tor aktivieren oder deaktivieren und sogar deaktivieren, sobald die Ginger-Anwendung geschlossen wird.



![screen](assets/fr/21.webp)



**NB** :




- Stellen Sie für die Zwei-Faktor-Authentifizierung sicher, dass Ihre Authentifizierungsanwendung das SHA256-Protokoll und 8-stellige Codes unterstützt. Der Ginger Wallet erfordert einen 8-stelligen 2FA-Code für erhöhte Sicherheit. Dieses längere Format macht es viel schwieriger, den Code zu erraten oder zu kompromittieren, und bietet einen besseren Schutz vor unbefugtem Zugriff.
- Standardmäßig wird der gesamte Netzwerkverkehr von Ginger durch Tor geleitet, so dass eine manuelle Konfiguration nicht notwendig ist. Wenn Tor bereits auf deinem System aktiv ist, wird Ginger ihm automatisch Priorität geben.



Aber wenn du Tor in den Einstellungen deaktivierst, bleibt deine Privatsphäre im Allgemeinen erhalten, außer in zwei Situationen:




- während eines CoinJoin könnte der Koordinator Ihre Ein- und Ausgänge mit Ihrem IP Address verbinden;
- wenn Sie eine Transaktion übermitteln, könnte ein böswilliger Knoten, mit dem Sie sich verbinden, Ihre Transaktion mit Ihrer IP-Adresse in Verbindung bringen.



Vergessen Sie nicht, jedes Mal **Fertig** (unten rechts im Coin) zu drücken, um Ihre Einstellungen zu speichern. Einige Einstellungen erfordern einen Neustart des Ginger Wallet, um wirksam zu werden.



Darüber hinaus können Sie mit der Suchleiste oben in den Portfolios nach jedem beliebigen Parameter usw. suchen und darauf zugreifen.



![screen](assets/fr/22.webp)




### Konfiguration des Portfolios



In der Anwendung können mehrere Portfolios angelegt werden, so dass jedes Portfolio nach Ihren Bedürfnissen konfiguriert werden kann. Klicken Sie dazu auf die **drei Punkte** vor dem Portfolionamen, dann auf **Portfolioeinstellungen**.



![screen](assets/fr/23.webp)



Wie Sie sehen, können Sie neben dem Wallet-Parameter auch Ihre UTXOs (Liste der Token, die Sie besitzen), Statistiken und Wallet-Informationen (z. B. den erweiterten öffentlichen Schlüssel) einsehen.



Um zu unserer Portfoliokonfiguration zurückzukehren, klicken Sie auf Portfolioparameter und Sie werden zu den folgenden Registerkarten weitergeleitet:




- Allgemein** (hier können Sie den Namen des Portfolios ändern) ;



![screen](assets/fr/24.webp)





- CoinJoin** (hier können Sie die CoinJoin-Einstellungen dieses Portfolios anpassen) ;



![screen](assets/fr/25.webp)





- Tools** (hier können Sie Ihre seedphrase überprüfen, Ihr Portfolio erneut synchronisieren oder es löschen).



![screen](assets/fr/26.webp)




## Bitcoins erhalten



Um Bitcoins in Ihrem Wallet auf Ginger Wallet zu erhalten:




- drücken Sie **Empfangen** ;



![screen](assets/fr/27.webp)





- Geben Sie den Namen der Quelle ein, der Sie das Address zuordnen möchten. Dies ist eine Kennzeichnung, um Ihre Zahlungen zu verfolgen. Dies hat keine Auswirkungen auf On-Chain; es handelt sich lediglich um Rückverfolgbarkeitsinformationen, die lokal in Ihrer Anwendung gespeichert werden;



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- klicken Sie auf den kleinen Pfeil links neben **generate**, um Ihr Address-Format (**SegWit** /**Taproot**) auszuwählen, und klicken Sie dann auf **generate**, um generate, Address und QR-Code auszuwählen.



![screen](assets/fr/29.webp)



Dieser Address oder QR-Code wird von Ihrem Absender verwendet, um Ihnen Bitcoins zu senden.



![screen](assets/fr/30.webp)




## Bitcoins senden



Video-Tutorial, wie man über Ginger Wallet sendet.



![Vidéo](https://youtu.be/2nf5aAimfhg)



Um dies zu tun:




- Drücken Sie die Taste **Senden**;
- geben Sie die Address des Empfängers, den zu sendenden Betrag und ein Etikett ein;
- überprüfen Sie die Transaktionsübersicht und bestätigen Sie den Versand.



![screen](assets/fr/31.webp)




## Bitcoins ausgeben



Es ist einfach, Bitcoin mit Ginger Wallet zu kaufen und zu verkaufen. In nur wenigen Schritten können Sie Ihre Bitcoins ausgeben.



### Bitcoins kaufen



Ginger Wallet-Nutzer können Bitcoins kaufen.





- Drücken Sie die Taste **Kaufen**. Diese Taste bleibt auch dann sichtbar, wenn das Wallet leer ist.



![screen](assets/fr/32.webp)





- Wählen Sie Ihr Land oder sogar Ihr Bundesland (in einigen Regionen, wie z. B. Kanada), bevor Sie mit dem Kauf des Bitcoin fortfahren. Wenn Sie zum ersten Mal auf die Funktion **Kaufen** klicken, müssen Sie auch Ihre Region angeben.



![screen](assets/fr/33.webp)



Drücken Sie **Fortfahren**, um den Kaufvorgang fortzusetzen.





- Geben Sie dann den Betrag an Bitcoins, den Sie kaufen möchten, in das entsprechende Feld ein. Sie können auch die Transaktionswährung wählen.



![screen](assets/fr/34.webp)



Für jede Währung gibt es ein Mindest- und ein Höchstlimit für den Kauf. In USD beträgt die Obergrenze zum Beispiel 30.000 $.



Wenn Sie bereits einen Kauf getätigt haben, können Sie Ihren Transaktionsverlauf einsehen, indem Sie auf die Schaltfläche **Vorherige Bestellungen** klicken. Es wird eine Liste der vergangenen Transaktionen und deren Status angezeigt.





- Wählen Sie das für Sie passende Angebot.



Hier sehen Sie eine Liste aller verfügbaren Angebote. Für jedes Angebot haben Sie :




 - name des Lieferanten (1) ;
 - die Anzahl der Bitcoins, die dem zuvor eingegebenen Betrag entspricht, die Zahlungsmethode und die Kaufgebühr (2) ;
 - die Schaltfläche **Akzeptieren** (3).



![screen](assets/fr/35.webp)



Die im Angebot angegebenen Gebühren stellen keine zusätzlichen Kosten dar. Sie sind bereits im Gesamtbetrag des Angebots enthalten.



In der rechten oberen Hälfte des Bildschirms mit der Bezeichnung **Alle** können Sie die Angebote nach Zahlungsart filtern. Die von Ihnen gewählte Zahlungsmethode ist standardmäßig eingestellt, kann aber jederzeit geändert werden.



![screen](assets/fr/36.webp)



Wenn Sie ein passendes Angebot finden, klicken Sie auf die Schaltfläche **Annehmen**, um mit dem Kauf fortzufahren. Sie werden dann zur Seite des Verkäufers weitergeleitet, wo Sie die Transaktion abschließen können.



### Bitcoins verkaufen



Ginger Wallet-Nutzer können Bitcoin verkaufen. Die Schaltfläche **Verkaufen** ist nur sichtbar, wenn Mittel im Portfolio vorhanden sind.





- Klicken Sie auf **Verkaufen**.



![screen](assets/fr/37.webp)





- Wie bei der Option **Kaufen** müssen Sie bei der erstmaligen Verwendung der Funktion Verkaufen Ihr Land auswählen, bevor Sie mit dem Verkauf eines Bitcoin fortfahren können.





- Als Nächstes müssen Sie die Menge an Bitcoins eingeben, die Sie verkaufen möchten. Sie können diesen Betrag in BTC oder in einer Fiat-Währung wie dem US-Dollar (USD) eingeben.





- Sobald Sie dies getan haben, wird eine Liste der verfügbaren Angebote angezeigt. Wählen Sie ein für Sie passendes Angebot aus und klicken Sie auf **Annehmen**, um fortzufahren.





- Nun müssen Sie die Transaktion abschließen:
 - Sobald Sie ein Angebot angenommen haben, werden Sie auf die Seite des Anbieters weitergeleitet;
 - Folgen Sie den Anweisungen auf der Anbieterseite;
 - Irgendwann erhalten Sie eine Empfänger-Address und den genauen Betrag, den Sie senden müssen;
 - Kehren Sie dann zu Ginger Wallet zurück, um den Vorgang fortzusetzen;
 - Sobald Sie wieder in Ginger Wallet sind, erscheint ein Dialogfeld, in dem Sie auf **Senden** klicken können.



Dadurch wird der Bildschirm **Senden** geöffnet, in dem der Address des Empfängers und der Betrag vorausgefüllt sind. Sie können auch die Schaltfläche **Senden** auf dem Startbildschirm verwenden. Obwohl Sie die Transaktion manuell senden können, empfehlen wir Ihnen, sie über das Dialogfeld auszuführen, um den Prozess zu optimieren.



## Machen Sie einen CoinJoin auf Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Schützen Sie die Vertraulichkeit Ihrer Bitcoins mit **CoinJoin**, das direkt in den Ginger Wallet integriert ist. Der Wallet verwendet **WABISABI**, ein Chaumian CoinJoin Protokoll, das entwickelt wurde, um leichter zugängliche und effiziente Coinjoins zu ermöglichen.



Es liegt an Ihnen, die CoinJoin-Strategie (automatisch oder manuell) zu wählen, die Ihnen am besten passt.



Ginger CoinJoin ist sofort nach dem Herunterladen einsatzbereit (keine weiteren Schritte erforderlich). Ginger CoinJoin läuft automatisch im Hintergrund, um Ihre Privatsphäre bei jeder Transaktion zu schützen. In der Praxis wird das CoinJoin-Lesegerät immer dann angezeigt, wenn Sie einen Saldo haben, der anonymisiert werden kann.



Die manuelle Inbetriebnahme des CoinJoin ist ein Ein-Klick-Vorgang. Starten Sie die Runde und warten Sie darauf, dass die CoinJoin-Transaktion erstellt und bestätigt wird. Sie werden das Anonymisierungsergebnis in Interface sehen.



Es können mehrere Mischungen durchgeführt werden, bis der gewünschte Grad an Anonymität erreicht ist. Sie können auch bestimmte Teile aus dem Mix ausschließen.



Standardmäßig verwendet Ginger seinen eigenen Koordinator mit allen vorkonfigurierten Parametern und garantierten Gebühren. Bei Coinjoins von Token im Wert von mehr als 0,03 BTC fällt zusätzlich zur Mining-Gebühr eine Koordinatorgebühr von 0,3 % an. Einträge von 0,03 BTC oder weniger sowie Remixes sind von Koordinatorgebühren befreit, selbst nach einer einzigen Transaktion. Daher können bei einer Zahlung mit CoinJoin-Geldern sowohl der Sender als auch der Empfänger ihre Münzen neu mischen, ohne dass Koordinatorgebühren anfallen.



Ginger bevorzugt Coinjoins mit mehr Teilnehmern gegenüber kleineren, schnelleren Runden. Größere Coinjoins bieten mehr Anonymität, niedrigere Kosten und eine größere Effizienz des BLOCK-Platzes.




## Sicherheit und bewährte Praktiken



Der Wunsch nach Dezentralisierung und die Wahrung der Privatsphäre erfordern die Anwendung mehrerer bewährter Verfahren:




- Bewahren Sie Ihr seedphrase immer an einem sicheren Ort auf, wenn Sie nicht online sind;
- Wenn Sie Ihren Computer verlieren oder einen unbefugten Zugriff vermuten, erstellen Sie sofort ein neues Wallet. Übertragen Sie Ihre Gelder in dieses neue Portfolio und löschen Sie das alte;
- Verwenden Sie für jeden Empfang einen anderen Address, um die Wiederverwendung von Adressen zu vermeiden;
- Laden Sie Ihre Portfolio-Anwendungen immer ausschließlich von dem offiziellen GitHub-Konto oder der offiziellen Website herunter.



Jetzt sind Sie mit der Verwendung der Ginger Wallet-Anwendung zum Senden, Empfangen und Ausgeben Ihrer Bitcoins vertraut.



Wenn Sie dieses Tutorial nützlich fanden, hinterlassen Sie mir bitte einen Green Daumen unten. Bitte zögern Sie nicht, diesen Artikel über Ihre Social-Media-Plattformen zu teilen. Herzlichen Dank!



Ich schlage auch vor, dass Sie sich dieses Tutorial ansehen, in dem erklärt wird, wie man die Computeranwendung Liana verwendet, um Bitcoins zu senden und zu empfangen und einen automatisierten Nachlassplan umzusetzen.



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04