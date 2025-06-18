---
name: Trezor Modell Eins
description: Einrichten und Verwenden des Hardware Wallet Model One
---
![cover](assets/cover.webp)



*Bildnachweis: [Trezor.io](https://trezor.io/)*



Das Trezor Model One ist das allererste Hardware Wallet, das 2014 von SatoshiLabs auf den Markt gebracht wurde. Nach mehr als zehn Jahren ist es immer noch eine interessante Wahl, insbesondere für Nutzer, die ein Hardware Wallet suchen, das sowohl technisch als auch preislich erschwinglich ist. Auf der offiziellen Trezor-Website wird er für 49 € angeboten. Es ist eine der einzigen Hardware-Geldbörsen in dieser Preisklasse. Sie liegt in der Mitte zwischen den Einsteigergeräten für rund 20 Euro, wie dem Tapsigner, die oft keinen Bildschirm haben, und den Geräten der mittleren Preisklasse für rund 80 Euro, wie dem Ledger Nano S Plus oder dem Trezor Safe 3.



Das Model One verfügt über ein 0,96 Zoll großes monochromes OLED-Display und zwei physische Tasten. Es arbeitet ohne Batterie und nutzt nur einen Micro-USB-Anschluss für Strom und Daten Exchange.



![Image](assets/fr/01.webp)



Der größte Nachteil des Model One ist das Fehlen eines Secure Elements, was es anfällig für eine Vielzahl von physischen Angriffen macht, von denen einige relativ einfach auszuführen sind. Diese Angriffe können die Analyse von Hilfskanälen umfassen, um die Geräte-PIN zu ermitteln, oder fortschrittlichere Techniken, um das verschlüsselte seed zu extrahieren, um es später zu erzwingen. Beachten Sie, dass diese Angriffe physischen Zugriff auf das Gerät erfordern. Diese Anfälligkeit kann jedoch durch die Verwendung eines soliden passphrase BIP39 erheblich verringert werden. Wenn Sie sich für dieses Hardware Wallet entscheiden, rate ich Ihnen dringend, ein passphrase zu konfigurieren.



Das Model One bietet zwei wichtige Vorteile:




- Es basiert auf einer vollständig quelloffenen Architektur. Im Gegensatz zu neueren Modellen mit Secure Element sind alle Hardware- und Softwarekomponenten des Model One auditierbar;
- Es ist mit einem Bildschirm ausgestattet. Meines Wissens ist dies das einzige Hardware Wallet auf dem Markt in dieser Preisklasse mit einem Bildschirm. Dies ist ein sehr wichtiges Merkmal, da es die Überprüfung von signierten Informationen und Empfangsadressen ermöglicht und damit viele digitale Angriffe verhindert.



Das Trezor Model One kann daher eine gute Wahl für Anfänger und fortgeschrittene Nutzer mit begrenztem Budget sein. Es ist jedoch wichtig, sich seiner Einschränkungen in Bezug auf den physischen Schutz bewusst zu sein, da es kein Secure Element gibt. Wenn Ihr Budget begrenzt ist, ist dies eine gute Option, aber wenn Sie es sich leisten können, sich für ein höherwertiges Modell zu entscheiden, wie z. B. das Trezor Safe 3 für 79 €, ist es vorzuziehen, da es ein Secure Element enthält.



## Auspacken des Trezor Model One



Wenn Sie Ihr Model One erhalten, vergewissern Sie sich, dass die Verpackung und der Seal unversehrt sind, um sicherzustellen, dass das Paket nicht geöffnet wurde. Eine Softwareüberprüfung der Authentizität und Integrität des Geräts wird auch bei der späteren Einrichtung durchgeführt.



Inhalt der Box: :




- Das Trezor Model One;
- Karton zum Aufzeichnen Ihres Mnemonic-Satzes, Aufkleber und Anweisungen;
- USB-A auf Mikro-USB-Kabel.



![Image](assets/fr/02.webp)



Die Navigation auf dem Gerät ist sehr einfach:




- Klicken Sie mit der rechten Maustaste, um zu bestätigen und mit den nächsten Schritten fortzufahren;
- Verwenden Sie die linke Taste, um zurückzugehen.



## Voraussetzungen



In diesem Tutorial zeige ich Ihnen, wie Sie das Trezor Model One mit der [Sparrow Wallet Portfolio Management Software] (https://sparrowwallet.com/download/) verwenden können. Wenn Sie diese Software noch nicht installiert haben, sollten Sie dies jetzt tun. Wenn Sie Hilfe benötigen, haben wir auch eine detaillierte Anleitung zur Konfiguration von Sparrow Wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Außerdem benötigen Sie die Trezor Suite Software, um das Model One zu konfigurieren, seine Echtheit zu überprüfen und die Firmware zu installieren. Wir werden diese Software nur zu diesem Zweck verwenden, und danach wird sie nur noch für Firmware-Updates benötigt. Für die tägliche Verwaltung des Wallet werden wir ausschließlich Sparrow Wallet verwenden, da es für Bitcoin optimiert und auch für Anfänger leicht zu bedienen ist (Sparrow unterstützt nur Bitcoin, keine Altcoins).



[Trezor Suite von der offiziellen Website herunterladen](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Bei diesen beiden Programmen empfehle ich Ihnen dringend, sowohl ihre Authentizität (mit GnuPG) als auch ihre Integrität (über Hash) zu überprüfen, bevor Sie sie auf Ihrem Rechner installieren. Wenn Sie nicht wissen, wie man das macht, können Sie diese andere Anleitung befolgen:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Starten des Trezor Model One



Schließen Sie Ihr Model One an Ihren Computer an, auf dem die Trezor Suite und Sparrow Wallet bereits installiert sind.



![Image](assets/fr/04.webp)



Öffnen Sie die Trezor Suite und klicken Sie auf "*Meinen Trezor einrichten*".



![Image](assets/fr/05.webp)



Wählen Sie "*Nur-Bitcoin-Firmware*" und klicken Sie dann auf "*Nur-Bitcoin installieren*".



![Image](assets/fr/06.webp)



Die Trezor Suite wird dann die Firmware auf Ihrem Model One installieren. Bitte warten Sie während der Installation.



![Image](assets/fr/07.webp)



Klicken Sie auf "*Fortfahren*".



![Image](assets/fr/08.webp)



## Erstellung eines Bitcoin-Portfolios



Klicken Sie in der Trezor Suite auf die Schaltfläche "*Neues Wallet erstellen*".



![Image](assets/fr/09.webp)



Akzeptieren Sie die Nutzungsbedingungen für die Hardware Wallet.



![Image](assets/fr/10.webp)



Klicken Sie in Trezor Suite auf "*Sicherung fortsetzen*".



![Image](assets/fr/11.webp)



Die Software enthält Anweisungen zur Verwaltung Ihres Mnemonic-Satzes.



Mit diesem Mnemonic haben Sie vollen, uneingeschränkten Zugriff auf alle Ihre Bitcoins. Jeder, der im Besitz dieses Satzes ist, kann Ihr Geld stehlen, auch ohne physischen Zugang zu Ihrem Trezor Model One.



Die 24-Wort-Phrase stellt den Zugang zu Ihren Bitcoins wieder her, falls Ihr Hardware Wallet verloren geht, gestohlen wird oder kaputt geht. Es ist daher sehr wichtig, sie sorgfältig zu speichern und an einem sicheren Ort aufzubewahren.



Sie können die Gravur auf dem mitgelieferten Karton anbringen. Für zusätzliche Sicherheit empfehle ich, die Gravur auf einem Edelstahlsockel anzubringen, um sie vor Feuer, Überschwemmung oder Einsturz zu schützen.



Bestätigen Sie die Anweisungen und klicken Sie dann auf die Schaltfläche "*Wallet-Sicherung erstellen*".



![Image](assets/fr/12.webp)



Das Model One erstellt Ihren Mnemonic-Satz mithilfe seines Zufallszahlengenerators. Vergewissern Sie sich, dass Sie während dieses Vorgangs nicht beobachtet werden. Schreiben Sie die auf dem Bildschirm angezeigten Wörter auf einen Datenträger Ihrer Wahl. Je nach Ihrer Sicherheitsstrategie können Sie mehrere vollständige physische Kopien des Satzes anfertigen (aber vor allem dürfen Sie ihn nicht teilen). Achten Sie darauf, dass die Wörter nummeriert sind und in der richtigen Reihenfolge stehen.



***Natürlich dürfen Sie diese Worte niemals im Internet weitergeben, wie ich es in diesem Tutorial tue. Dieses Beispiel Wallet wird nur auf dem Testnet verwendet und wird am Ende des Tutorials gelöscht werden



Für weitere Informationen über die richtige Art und Weise, Ihre Mnemonic Phrase zu speichern und zu verwalten, empfehle ich Ihnen diesen anderen Lehrgang, besonders wenn Sie ein Anfänger sind:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Um mit den nächsten Wörtern fortzufahren, klicken Sie mit der rechten Maustaste. Wenn Sie alle Wörter aufgeschrieben haben, klicken Sie erneut auf die rechte Taste, um zum nächsten Schritt zu gelangen.



![Image](assets/fr/13.webp)



Ihr Hardware Wallet zeigt Ihnen wieder alle Ihre Wörter an. Überprüfen Sie, ob Sie sie alle aufgeschrieben haben.



![Image](assets/fr/14.webp)



## Einstellen des PIN-Codes



Als Nächstes kommt der Schritt des PIN-Codes. Mit dem PIN-Code wird Ihr Trezor entsperrt. Er bietet also Schutz vor unbefugtem physischen Zugriff. Dieser PIN-Code ist nicht an der Ableitung der kryptografischen Schlüssel Ihres Wallet beteiligt. Selbst wenn Sie keinen Zugang zum PIN-Code haben, können Sie mit Ihrem 12-Wörter-Mnemonic-Satz wieder Zugang zu Ihren Bitcoins erhalten.



Klicken Sie in der Trezor Suite auf "*Weiter zur PIN*" und dann auf die Schaltfläche "*PIN festlegen*".



![Image](assets/fr/15.webp)



Bestätigen Sie auf dem Model One.



![Image](assets/fr/16.webp)



Wir empfehlen, einen möglichst zufälligen PIN-Code zu wählen. Speichern Sie diesen Code an einem anderen Ort als den, an dem Ihr Trezor gespeichert ist (z. B. in einem Passwortmanager). Sie können einen PIN-Code mit einer Länge zwischen 8 und 50 Ziffern festlegen. Ich empfehle Ihnen, den PIN-Code so lang wie möglich zu wählen, um die Sicherheit zu erhöhen.



Der PIN-Code muss in der Trezor Suite auf Ihrem Computer eingegeben werden, indem Sie auf die Punkte klicken, die den Ziffern entsprechen, je nach der auf dem Trezor Model One angezeigten Tastaturkonfiguration.



Diese spezielle PIN-Eingabemethode ist jedes Mal erforderlich, wenn Sie Ihr Trezor Model One entsperren, sei es über die Trezor Suite oder den Sparrow Wallet.



![Image](assets/fr/17.webp)



Klicken Sie anschließend auf die Schaltfläche "*PIN eingeben*".



![Image](assets/fr/18.webp)



Geben Sie Ihre PIN zur Bestätigung erneut ein.



![Image](assets/fr/19.webp)



Klicken Sie in Trezor Suite auf die Schaltfläche "*Einrichtung abschließen*".



![Image](assets/fr/20.webp)



Die Konfiguration Ihres Model One ist nun abgeschlossen. Wenn Sie möchten, können Sie den Namen und die Startseite Ihres Hardware Wallet ändern.



![Image](assets/fr/21.webp)



Wir werden die Trezor Suite Software nicht mehr benötigen, außer um regelmäßige Firmware-Updates auf Ihrem Hardware Wallet durchzuführen, oder wenn Sie einen Wiederherstellungstest durchführen möchten. Wir werden nun Sparrow zur Verwaltung des Portfolios verwenden, da diese Software perfekt für die ausschließliche Verwendung des Bitcoin geeignet ist.



## Einrichten des Portfolios auf Sparrow Wallet



Beginnen Sie mit dem Herunterladen und der Installation von Sparrow Wallet [von der offiziellen Website] (https://sparrowwallet.com/) auf Ihrem Computer, falls Sie dies nicht bereits getan haben.



Wenn Sie Sparrow Wallet geöffnet haben, vergewissern Sie sich, dass die Software mit einem Bitcoin-Knoten verbunden ist, was durch das Häkchen in der unteren rechten Ecke von Interface angezeigt wird. Wenn Sie Probleme mit der Verbindung von Sparrow haben, empfehle ich Ihnen, den Anfang dieses Tutorials zu lesen:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klicken Sie auf die Registerkarte "*Datei*" und dann auf "*Neues Wallet*".



![Image](assets/fr/22.webp)



Geben Sie Ihrem Portfolio einen Namen und klicken Sie dann auf "*Wallet erstellen*".



![Image](assets/fr/23.webp)



Wählen Sie im Dropdown-Menü "*Skripttyp*" den Skripttyp aus, der zur Sicherung Ihrer Bitcoins verwendet werden soll. Ich empfehle "*Taproot*" oder, falls dies nicht möglich ist, "*Native SegWit*".



![Image](assets/fr/24.webp)



Klicken Sie auf die Schaltfläche "*Verbundenes Hardware Wallet*". Ihr Model One muss natürlich mit dem Computer verbunden sein.



![Image](assets/fr/25.webp)



Klicken Sie auf die Schaltfläche "*Scan*". Ihr Model One sollte erscheinen.



Wenn Sie Ihr Model One an einen Computer mit geöffnetem Sparrow Wallet anschließen, werden Sie aufgefordert, ein passphrase BIP39 in Sparrow einzugeben. Diese erweiterte Option wird in einem späteren Tutorial behandelt. Im Moment können Sie einfach "*passphrase ausschalten*" wählen, um zu verhindern, dass Ihr Trezor Sie bei jedem Start auffordert, ein passphrase einzugeben.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Klicken Sie auf "*Import Keystore*".



![Image](assets/fr/27.webp)



Sie können nun die Details Ihres Wallet sehen, einschließlich des erweiterten öffentlichen Schlüssels Ihres ersten Kontos. Klicken Sie auf die Schaltfläche "*Apply*", um die Erstellung des Wallet abzuschließen.



![Image](assets/fr/28.webp)



Wählen Sie ein sicheres Passwort, um den Zugang zum Sparrow Wallet zu schützen. Dieses Passwort gewährleistet einen sicheren Zugriff auf Ihre Sparrow Wallet-Daten und schützt Ihre öffentlichen Schlüssel, Adressen, Etiketten und Transaktionshistorie vor unbefugtem Zugriff.



Ich empfehle Ihnen, dieses Passwort in einem Passwort-Manager zu speichern, damit Sie es nicht vergessen.



![Image](assets/fr/29.webp)



Und jetzt ist Ihr Portfolio in Sparrow Wallet importiert worden!



![Image](assets/fr/30.webp)



Bevor Sie Ihre ersten Bitcoins in Ihrem Wallet erhalten, **empfehle ich Ihnen dringend, einen Leertest** durchzuführen. Schreiben Sie einige Referenzinformationen auf, z. B. Ihr xpub, und setzen Sie dann Ihren Trezor Model One zurück, während der Wallet noch leer ist. Versuchen Sie dann, Ihr Wallet auf dem Trezor mit Hilfe Ihrer Papier-Backups wiederherzustellen. Überprüfen Sie, ob das nach der Wiederherstellung erzeugte xpub mit dem ursprünglich notierten übereinstimmt. Wenn dies der Fall ist, können Sie sicher sein, dass Ihre Papier-Backups zuverlässig sind.



Um mehr darüber zu erfahren, wie man einen Wiederherstellungstest durchführt, empfehle ich Ihnen, diesen anderen Lehrgang zu lesen:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Wie kann man mit dem Trezor Model One Bitcoins empfangen?



Klicken Sie auf Sparrow auf die Registerkarte "*Empfangen*".



![Image](assets/fr/31.webp)



Bevor Sie den von Sparrow Wallet vorgeschlagenen Address verwenden, überprüfen Sie ihn auf dem Bildschirm Ihres Trezor. Auf diese Weise können Sie sich vergewissern, dass der auf Sparrow angezeigte Address nicht gefälscht ist und dass der Hardware Wallet tatsächlich den privaten Schlüssel enthält, der für die anschließende Ausgabe der mit diesem Address gesicherten Bitcoins erforderlich ist. Dies hilft Ihnen, mehrere Arten von Angriffen zu vermeiden.



Um diese Prüfung durchzuführen, klicken Sie auf die Schaltfläche "*Address anzeigen*".



![Image](assets/fr/32.webp)



Überprüfen Sie, ob der auf Ihrem Trezor angezeigte Address mit dem auf dem Sparrow Wallet übereinstimmt. Es ist auch ratsam, diese Überprüfung kurz vor der Übermittlung Ihres Address an den Absender durchzuführen, um sicher zu sein, dass er gültig ist. Sie können die rechte Taste zur Bestätigung drücken.



![Image](assets/fr/33.webp)



Sie können auch ein "*Label*" hinzufügen, um die Quelle der Bitcoins zu beschreiben, die mit diesem Address gesichert werden sollen. Dies ist eine gute Praxis, die es Ihnen ermöglicht, Ihre UTXOs besser zu verwalten.



![Image](assets/fr/34.webp)



Sie können dann dieses Address verwenden, um Bitcoins zu erhalten.



![Image](assets/fr/35.webp)



## Wie versendet man Bitcoins mit dem Trezor Model One?



Jetzt, wo du deine ersten Satss in deinem Model One-gesicherten Wallet erhalten hast, kannst du sie auch ausgeben! Schließen Sie Ihren Trezor an Ihren Computer an, starten Sie Sparrow Wallet und gehen Sie dann auf die Registerkarte "*Senden*", um eine neue Transaktion zu erstellen.



![Image](assets/fr/36.webp)



Wenn Sie *Münzkontrolle* wünschen, d.h. gezielt auswählen möchten, welche UTXOs in der Transaktion verbraucht werden sollen, gehen Sie auf die Registerkarte "*UTXOs*". Wählen Sie die UTXOs aus, die Sie ausgeben möchten, und klicken Sie dann auf "*Ausgewählte senden*". Sie werden zum gleichen Bildschirm auf der Registerkarte "*Senden*" zurückgeleitet, aber mit den bereits für die Transaktion ausgewählten UTXOs.



![Image](assets/fr/37.webp)



Geben Sie den Ziel-Address ein. Sie können auch mehrere Adressen eingeben, indem Sie auf die Schaltfläche "*+ Hinzufügen*" klicken.



![Image](assets/fr/38.webp)



Notieren Sie ein "*Etikett*", um sich den Zweck dieser Ausgabe zu merken.



![Image](assets/fr/39.webp)



Wählen Sie den Betrag, der an diesen Address gesendet werden soll.



![Image](assets/fr/40.webp)



Passen Sie den Gebührensatz für Ihre Transaktion an den aktuellen Markt an. Sie können zum Beispiel [Mempool.space] (https://Mempool.space/) verwenden, um einen geeigneten Gebührensatz zu wählen.



Vergewissern Sie sich, dass alle Ihre Transaktionsparameter korrekt sind, und klicken Sie dann auf "*Transaktion erstellen*".



![Image](assets/fr/41.webp)



Wenn alles zu Ihrer Zufriedenheit ist, klicken Sie auf "*Transaktion zur Unterzeichnung abschließen*".



![Image](assets/fr/42.webp)



Klicken Sie auf "*Unterschreiben*".



![Image](assets/fr/43.webp)



Klicken Sie auf "*Unterschreiben*" neben Ihrem Trezor Model One.



![Image](assets/fr/44.webp)



Überprüfen Sie die Transaktionsparameter auf Ihrem Hardware Wallet-Bildschirm, einschließlich des empfangenden Address des Empfängers, den gesendeten Betrag und die Gebühr. Sobald die Transaktion auf dem Trezor überprüft wurde, klicken Sie mit der rechten Maustaste, um sie zu signieren.



![Image](assets/fr/45.webp)



Ihre Transaktion ist nun signiert. Prüfen Sie ein letztes Mal, ob alles in Ordnung ist, und klicken Sie dann auf "*Transaktion übertragen*", um sie im Bitcoin-Netz zu übertragen.



![Image](assets/fr/46.webp)



Sie finden es auf der Registerkarte "*Transaktionen*" von Sparrow Wallet.



![Image](assets/fr/47.webp)



Herzlichen Glückwunsch, Sie sind nun mit der grundlegenden Verwendung des Trezor Model One mit Sparrow Wallet vertraut! Um noch einen Schritt weiter zu gehen, empfehle ich Ihnen diese umfassende Anleitung zur Verwendung eines Hardware Wallet Trezor mit einem passphrase BIP39, um Ihre Sicherheit zu verstärken:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Wenn Sie diese Anleitung nützlich fanden, wäre ich Ihnen dankbar, wenn Sie unten einen Green-Daumen hinterlassen würden. Sie können diesen Artikel auch gerne in Ihren sozialen Netzwerken teilen. Ich danke Ihnen sehr!