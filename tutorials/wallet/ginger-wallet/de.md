---
name: Ginger Wallet
description: Open-Source, selbstverwaltete Bitcoin wallet Software, fork von Wasabi Wallet, Integration von Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet ist ein quelloffenes, nicht-verwahrendes Bitcoin-Portfolio, das sich auf Vertraulichkeit und Datenschutz konzentriert. Es entstand als fork aus Wasabi Wallet (nach Version 2.0.7.2 - MIT-Lizenz).



Ginger Wallet behält die technische Architektur von Wasabi bei, fügt aber ein paar spezifische Funktionen hinzu. Laut der [Ginger Wallet-Dokumentation] (https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet) legt Wasabi den Schwerpunkt auf **Autonomie und Kontrolle**, während Ginger den Schwerpunkt auf **Benutzerfreundlichkeit, Sicherheit und ein vereinfachtes Erlebnis** legt, wodurch es auch für diejenigen zugänglich wird, die mit technischen Aspekten weniger vertraut sind.



Ginger Wallet ist eine wallet-Software nur für Computer (keine mobile Anwendung).



## Was ist Coinjoin?



Der **coinjoin** ist eine spezielle Bitcoin-Transaktionsstruktur, die mehrere Teilnehmer in einer einzigen gemeinsamen Transaktion zusammenführt. Dieser Mechanismus vermischt die Eingaben verschiedener Nutzer in einer gemeinsamen Transaktion, was die Rückverfolgung von Geldern extrem erschwert - wenn nicht sogar oft unmöglich macht, wenn es richtig gemacht wird. Dadurch wird es für einen außenstehenden Beobachter fast unmöglich, die Herkunft und den Bestimmungsort der beteiligten Bitcoins mit Sicherheit zu identifizieren, anders als bei herkömmlichen Bitcoin-Transaktionen.



Für Sie als Nutzer hilft coinjoin, Ihre Vertraulichkeit zu wahren. Wenn Sie beispielsweise eine Spende von 10.000 sats auf einer Bitcoin-Adresse erhalten, kann der Absender diese Gelder zurückverfolgen und in einigen Fällen darauf schließen, dass Sie eine größere Menge an Bitcoins besitzen, oder Ihre Aktivitäten beobachten. Wenn Sie nach dieser Spende von 10.000 sats einen Coinjoin durchführen, unterbrechen Sie die Rückverfolgbarkeit: Der Absender kann aus dieser Zahlung keine Informationen mehr über Sie ableiten.



Das Chaumian Coinjoin bietet ein hohes Maß an Sicherheit, da die Gelder jederzeit unter der alleinigen Kontrolle des Nutzers bleiben. Auch die Betreiber der koordinierenden Server können die Bitcoins der Teilnehmer unter keinen Umständen abzweigen. Weder die Nutzer noch die Koordinatoren müssen sich gegenseitig vertrauen: Jeder behält die Kontrolle über seine privaten Schlüssel und ist allein befugt, Transaktionen zu validieren. Kein Dritter kann sich also während eines Coinjoin Ihre Bitcoins aneignen oder eine direkte Verbindung zwischen Ihren Ein- und Ausgaben herstellen.



Um mehr über coinjoin zu erfahren, besuchen Sie den Kurs BTC 204 der Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

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



Ginger weist Sie von Anfang an auf die Kosten hin, die mit dem Coinjoin-Prozess verbunden sind.



![screen](assets/fr/07.webp)



Drücken Sie dann **Start** und dann **Neu**, um ein neues Portfolio zu erstellen.



![screen](assets/fr/08.webp)



Speichern und bestätigen Sie anschließend Ihre seedphrase.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Für zusätzliche Sicherheit bietet der Ginger Wallet die Möglichkeit, einen passphrase hinzuzufügen.



![screen](assets/fr/11.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Diese passphrase wird, sobald sie hinzugefügt wurde, jedes Mal angefordert, wenn Sie versuchen, auf Ihr Portfolio zuzugreifen.



![screen](assets/fr/12.webp)



Ginger aktiviert automatisch die Standardeinstellung **Coinjoin**, wenn Sie Ihr Portfolio erstellen. Sie werden darüber informiert und können die Einstellung dann an Ihre Bedürfnisse anpassen.



![screen](assets/fr/13.webp)




### Allgemeine Einstellungen



Sobald Sie Ihr erstes Portfolio erstellt haben, werden Sie zur Ginger Wallet-Schnittstelle weitergeleitet.



![screen](assets/fr/14.webp)



Aktivieren Sie den **Diskretmodus**, wenn Sie die Salden in Ihren Geldbörsen verbergen möchten.



![screen](assets/fr/15.webp)



Sie können mehrere Portfolios auf Ginger Wallet erstellen. Klicken Sie einfach auf **Portfolio hinzufügen**.



![screen](assets/fr/16.webp)



Ginger unterstützt die Verwendung von Hardware-Portfolios über die Standard-Bitcoin-Core-Schnittstelle, obwohl eine direkte Integration von oder zu einem Hardware-Portfolio noch nicht verfügbar ist.



Zu den kompatiblen Hardware-Portfolios gehören (aber nicht nur) :




- Blockstrom Jade
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



Auf dieser Registerkarte können Sie die Ausführung von Bitcoin Knots beim Start der Anwendung aktivieren, Ihr Netz (Main/RegTest) und Ihren Tarifanbieter (Mempool Space/Blockstream info/Full Node) auswählen usw.



![screen](assets/fr/20.webp)





- Sicherheitsmerkmale**



Auf der Registerkarte Sicherheit kannst du die Zwei-Faktor-Authentifizierung aktivieren, Tor aktivieren oder deaktivieren und sogar deaktivieren, sobald die Ginger-Anwendung geschlossen wird.



![screen](assets/fr/21.webp)



**NB** :




- Stellen Sie für die Zwei-Faktor-Authentifizierung sicher, dass Ihre Authentifizierungsanwendung das SHA256-Protokoll und 8-stellige Codes unterstützt. Das Ginger Wallet erfordert einen 8-stelligen 2FA-Code, um die Sicherheit zu erhöhen. Dieses längere Format macht es viel schwieriger, den Code zu erraten oder zu kompromittieren, und bietet einen besseren Schutz vor unbefugtem Zugriff.
- Standardmäßig wird der gesamte Netzwerkverkehr von Ginger durch Tor geleitet, so dass eine manuelle Konfiguration nicht notwendig ist. Wenn Tor bereits auf deinem System aktiv ist, wird Ginger ihm automatisch Priorität geben.



Aber wenn du Tor in den Einstellungen deaktivierst, bleibt deine Privatsphäre im Allgemeinen erhalten, außer in zwei Situationen:




- bei einem Coinjoin könnte der Koordinator Ihre Ein- und Ausgänge mit Ihrer IP-Adresse verknüpfen;
- wenn Sie eine Transaktion übermitteln, könnte ein böswilliger Knoten, mit dem Sie sich verbinden, Ihre Transaktion mit Ihrer IP-Adresse in Verbindung bringen.



Vergessen Sie nicht, jedes Mal **Fertig** (in der unteren rechten Ecke) zu drücken, um Ihre Einstellungen zu speichern. Einige Einstellungen erfordern einen Neustart des Ginger Wallet, um wirksam zu werden.



Darüber hinaus können Sie mit der Suchleiste oben in den Portfolios nach jedem beliebigen Parameter usw. suchen und darauf zugreifen.



![screen](assets/fr/22.webp)




### Konfiguration des Portfolios



In der Anwendung können mehrere Portfolios angelegt werden, so dass jedes Portfolio nach Ihren Bedürfnissen konfiguriert werden kann. Klicken Sie dazu auf die **drei Punkte** vor dem Portfolionamen, dann auf **Portfolioeinstellungen**.



![screen](assets/fr/23.webp)



Wie Sie sehen, können Sie neben dem wallet-Parameter auch Ihre UTXOs (Liste der Token, die Sie besitzen), Statistiken und wallet-Informationen (z. B. den erweiterten öffentlichen Schlüssel) einsehen.



Um zu unserer Portfoliokonfiguration zurückzukehren, klicken Sie auf Portfolioparameter und Sie werden zu den folgenden Registerkarten weitergeleitet:




- Allgemein** (hier können Sie den Namen des Portfolios ändern) ;



![screen](assets/fr/24.webp)





- Coinjoin** (hier können Sie die Coinjoin-Einstellungen für diesen wallet anpassen) ;



![screen](assets/fr/25.webp)





- Tools** (hier können Sie Ihr seedphrase überprüfen, Ihr Portfolio erneut synchronisieren oder es löschen).



![screen](assets/fr/26.webp)




## Bitcoins erhalten



![video](https://youtu.be/cqv35wBDWMQ)



Um Bitcoins in Ihrem wallet auf Ginger Wallet zu erhalten:




- drücken Sie **Empfangen** ;



![screen](assets/fr/27.webp)





- Geben Sie den Namen der Quelle ein, mit der Sie die Adresse verknüpfen möchten. Dies ist eine Kennzeichnung, um Ihre Zahlungen zu verfolgen. Dies hat keine on-chain-Implikationen; es handelt sich lediglich um Rückverfolgbarkeitsinformationen, die lokal in Ihrer Anwendung gespeichert werden;



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- klicken Sie auf den kleinen Pfeil links neben **Erstellen**, um Ihr Adressformat auszuwählen (**SegWit** /**Taproot**), und klicken Sie dann auf **Erstellen**, um generate eine Adresse und einen QR-Code zu erstellen.



![screen](assets/fr/29.webp)



Diese Adresse oder dieser QR-Code wird von Ihrem Absender verwendet, um Ihnen Bitcoins zu senden.



![screen](assets/fr/30.webp)




## Bitcoins senden




![video](https://youtu.be/2nf5aAimfhg)



Um dies zu tun:




- Drücken Sie die Taste **Senden**;
- geben Sie die Adresse des Empfängers, den zu versendenden Betrag und ein Etikett ein;
- prüfen Sie die Transaktionsübersicht und bestätigen Sie den Versand.



![screen](assets/fr/31.webp)




## Bitcoins ausgeben



Es ist einfach, Bitcoin mit Ginger Wallet zu kaufen und zu verkaufen. In nur wenigen Schritten können Sie Ihre Bitcoins ausgeben.



### Bitcoins kaufen



![video](https://youtu.be/lEqTBzm5MEA)



Ginger Wallet-Nutzer können Bitcoins kaufen.





- Drücken Sie die Taste **Kaufen**. Diese Taste bleibt auch dann sichtbar, wenn das wallet leer ist.



![screen](assets/fr/32.webp)





- Wählen Sie Ihr Land oder sogar Ihr Bundesland (in einigen Regionen, wie z. B. Kanada), bevor Sie mit dem Bitcoin-Kauf fortfahren. Wenn Sie zum ersten Mal auf die Funktion **Kaufen** klicken, müssen Sie auch Ihre Region angeben.



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



In der oberen rechten Ecke des Bildschirms, die mit **Alle** gekennzeichnet ist, können Sie die Angebote nach Zahlungsart filtern. Die von Ihnen gewählte Zahlungsmethode ist standardmäßig eingestellt, kann aber jederzeit geändert werden.



![screen](assets/fr/36.webp)



Wenn Sie ein passendes Angebot finden, klicken Sie auf die Schaltfläche **Annehmen**, um mit dem Kauf fortzufahren. Sie werden dann zur Seite des Verkäufers weitergeleitet, wo Sie die Transaktion abschließen können.



### Bitcoins verkaufen



Ginger Wallet-Nutzer können Bitcoin verkaufen. Die Schaltfläche **Verkaufen** ist nur sichtbar, wenn im Portfolio Mittel vorhanden sind.





- Klicken Sie auf **Verkaufen**.



![screen](assets/fr/37.webp)





- Wie bei der Option **Kaufen** müssen Sie bei der ersten Nutzung der Verkaufsfunktion Ihr Land auswählen, bevor Sie mit dem Bitcoin-Verkauf fortfahren können.





- Als Nächstes müssen Sie die Menge an Bitcoins eingeben, die Sie verkaufen möchten. Sie können diesen Betrag in BTC oder in einer Fiat-Währung wie dem US-Dollar (USD) eingeben.





- Sobald Sie dies getan haben, wird eine Liste der verfügbaren Angebote angezeigt. Wählen Sie ein für Sie passendes Angebot aus und klicken Sie auf **Annehmen**, um fortzufahren.





- Nun müssen Sie die Transaktion abschließen:
 - Sobald Sie ein Angebot angenommen haben, werden Sie auf die Seite des Anbieters weitergeleitet;
 - Folgen Sie den Anweisungen auf der Anbieterseite;
 - Zu einem bestimmten Zeitpunkt erhalten Sie eine Empfängeradresse und den genauen Betrag, den Sie senden sollen;
 - Kehren Sie dann zu Ginger Wallet zurück, um den Prozess fortzusetzen;
 - Sobald Sie wieder im Ginger Wallet sind, erscheint ein Dialogfeld, in dem Sie auf **Senden** klicken können.



Dadurch wird der Bildschirm **Senden** geöffnet, in dem die Adresse des Empfängers und der Betrag bereits ausgefüllt sind. Sie können auch die Schaltfläche **Senden** auf dem Startbildschirm verwenden. Obwohl Sie die Transaktion manuell senden können, empfehlen wir Ihnen, sie über das Dialogfeld auszuführen, um den Prozess zu optimieren.



## Herstellung eines Coinjoin auf Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Schützen Sie die Vertraulichkeit Ihrer Bitcoins mit **Coinjoin**, das direkt in den Ginger Wallet integriert ist. Der wallet verwendet **WabiSabi**, ein chaumianisches Coinjoin-Protokoll, das entwickelt wurde, um leichter zugängliche und effiziente Coinjoins zu ermöglichen.



Es liegt an Ihnen, die Coinjoin-Strategie (automatisch oder manuell) zu wählen, die Ihnen am besten passt.



Ginger Coinjoin ist sofort nach dem Download einsatzbereit (keine weiteren Schritte erforderlich). Ginger Coinjoin läuft automatisch im Hintergrund, um Ihre Privatsphäre bei jeder Transaktion zu schützen. In der Praxis erscheint der Coinjoin-Player immer dann, wenn Sie ein Guthaben haben, das anonymisiert werden kann.



Das manuelle Starten von Coinjoin ist ein Ein-Klick-Vorgang. Starten Sie die Runde und warten Sie darauf, dass die Coinjoin-Transaktion erstellt und bestätigt wird. Sie werden den Anonymisierungswert in der Schnittstelle sehen.



Es können mehrere Mischungen durchgeführt werden, bis der gewünschte Grad an Anonymität erreicht ist. Sie können auch bestimmte Teile aus dem Mix ausschließen.



Standardmäßig verwendet Ginger seinen eigenen Koordinator mit allen vorkonfigurierten Parametern und garantierten Gebühren. Bei Coinjoins von Token im Wert von mehr als 0,03 BTC fällt zusätzlich zur mining-Gebühr eine Koordinatorgebühr von 0,3 % an. Einträge von 0,03 BTC oder weniger sowie Remixe sind von den Koordinatorgebühren befreit, auch nach einer einzigen Transaktion. Daher ermöglicht eine Zahlung mit Coinjoin-Geldern sowohl dem Sender als auch dem Empfänger, ihre Coins zu remixen, ohne dass Koordinatorgebühren anfallen.



Ginger bevorzugt Coinjoins mit mehr Teilnehmern gegenüber kleineren, schnelleren Runden. Größere Coinjoins bieten mehr Anonymität, geringere Kosten und eine größere Effizienz des Blockraums.




## Sicherheit und bewährte Praktiken



Der Wunsch nach Dezentralisierung und die Wahrung der Privatsphäre erfordern die Anwendung mehrerer bewährter Verfahren:




- Bewahren Sie Ihren seedphrase immer an einem sicheren Ort auf, wenn er nicht online ist;
- Wenn Sie Ihren Computer verlieren oder einen unbefugten Zugriff vermuten, erstellen Sie sofort ein neues wallet. Übertragen Sie Ihre Gelder in dieses neue Portfolio und löschen Sie das alte;
- Verwenden Sie für jeden Empfang eine andere Adresse, um die Wiederholung von Adressen zu vermeiden;
- Laden Sie Ihre Portfolio-Anwendungen immer ausschließlich von dem offiziellen GitHub-Konto oder der offiziellen Website herunter.



Jetzt sind Sie mit der Anwendung Ginger Wallet vertraut, mit der Sie Ihre Bitcoins senden, empfangen und ausgeben können.



Wenn Sie diese Anleitung nützlich fanden, hinterlassen Sie mir bitte einen grünen Daumen. Bitte teilen Sie diesen Artikel über Ihre Social-Media-Plattformen. Ich danke Ihnen vielmals!



Ich schlage auch vor, dass Sie sich diese Anleitung ansehen, wie Sie die Computeranwendung Liana verwenden, um Bitcoins zu senden und zu empfangen und einen automatisierten Nachlassplan umzusetzen.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04