---
name: Ledger U2F & FIDO2
description: Verbessern Sie Ihre Online-Sicherheit mit Ledger
---
![cover](assets/cover.webp)



Ledger-Geräte sind Hardware-Geldbörsen, die ursprünglich zur Sicherung eines Bitcoin Wallet entwickelt wurden, aber sie bieten auch erweiterte Optionen für eine starke Authentifizierung im Internet. Dank ihrer Kompatibilität mit den Protokollen **U2F** und **FIDO2** ermöglichen sie Ihnen, den Zugang zu Ihren Online-Konten zu sichern, indem sie einen zweiten Authentifizierungsfaktor einrichten.



Das U2F-Protokoll (Universal 2nd Factor) wurde 2014 von Google und Yubico eingeführt und anschließend von der FIDO Alliance standardisiert. Es ermöglicht das Hinzufügen eines zweiten physischen Authentifizierungsfaktors (2FA) beim Einloggen. Einmal aktiviert, müssen Nutzer zusätzlich zum klassischen Passwort jeden Versuch, sich mit ihrem Konto zu verbinden, durch Drücken einer Taste auf ihrem Ledger bestätigen. In diesem Zusammenhang funktioniert das Ledger ähnlich wie ein Yubikey. U2F ist in der Tat eine Unterkomponente des FIDO2-Standards, die diesen umfasst und gleichzeitig erhebliche Verbesserungen mit sich bringt, darunter native Unterstützung für moderne Browser und größere Flexibilität bei der Verwaltung von Authentifizierungsschlüsseln.



Diese Methoden basieren auf asymmetrischer Kryptografie: Es werden keine geheimen Daten übertragen, was Phishing- oder Abhörangriffe unwirksam macht. U2F und FIDO2 werden inzwischen von vielen Online-Diensten unterstützt.



In diesem Tutorial zeigen wir Ihnen, wie Sie U2F und FIDO2 für die Zwei-Faktor-Authentifizierung mit Ihrem Ledger aktivieren.



**Hinweis:** U2F und FIDO2 werden von allen Ledger-Geräten unterstützt, die mit aktueller Firmware ausgestattet sind: ab Version 2.1.0 für den Nano X und Nano S classic und ab Version 1.1.0 für den Nano S Plus. Die Modelle Stax und Flex sind nativ kompatibel.



## Installieren Sie die Anwendung Ledger Security Key



Wenn Sie ein Ledger-Gerät verwenden, wissen Sie wahrscheinlich, dass die Firmware allein nicht alle Funktionen enthält, die für die Verwaltung von Krypto-Geldbörsen erforderlich sind. Um zum Beispiel ein Bitcoin Wallet zu verwenden, müssen Sie die Anwendung "*Bitcoin*" installieren. Auch für die Verwaltung von MFA-Schlüsseln müssen Sie die Anwendung "*Security Key*" installieren.



Bevor Sie beginnen, stellen Sie sicher, dass Sie Ihren Bitcoin Wallet auf Ihrem Ledger eingerichtet haben. Es ist wichtig, Ihren Mnemonic korrekt zu speichern, da die für 2FA verwendeten Schlüssel von diesem Mnemonic abgeleitet werden. Wenn Ihr Ledger verloren geht oder beschädigt wird, können Sie den Zugang zu Ihren Schlüsseln wiederherstellen, indem Sie Ihre Mnemonic-Phrase auf einem anderen Ledger-Gerät eingeben (im Moment werden FIDO2-Kennungen im "*passwortlosen*" Modus noch nicht von Ledgers unterstützt, daher gibt es keine residenten Kennungen).



Schließen Sie Ihr Ledger an Ihren Computer an und entsperren Sie es.



![Image](assets/fr/01.webp)



Um die Anwendung zu installieren, öffnen Sie die Software [Ledger Live] (https://www.Ledger.com/Ledger-live) und gehen Sie dann zur Registerkarte "*Mein Ledger*". Suchen Sie die Anwendung "*Sicherheitsschlüssel*" und installieren Sie sie auf Ihrem Gerät.



![Image](assets/fr/02.webp)



Die Anwendung "*Sicherheitsschlüssel*" sollte nun neben den anderen auf Ihrem Ledger installierten Anwendungen erscheinen.



![Image](assets/fr/03.webp)



Klicken Sie auf die Anwendung, um sie für die nächsten Schritte des Lernprogramms geöffnet zu lassen.



![Image](assets/fr/04.webp)



## Verwenden Sie U2F/FIDO2 für 2FA mit einem Ledger



Greifen Sie auf das Konto zu, das Sie mit der Zwei-Faktor-Authentifizierung sichern möchten. Ich werde zum Beispiel ein Bitwarden-Konto verwenden. Sie finden die 2FA-Option in der Regel in den Einstellungen des Dienstes unter den Registerkarten "*Authentifizierung*", "*Sicherheit*", "*Anmeldung*" oder "*Passwort*".



![Image](assets/fr/05.webp)



Wählen Sie im Abschnitt für die Zwei-Faktor-Authentifizierung die Option "*Passkey*" (der Begriff kann je nach Website variieren).



![Image](assets/fr/06.webp)



Oft werden Sie aufgefordert, Ihr aktuelles Passwort zu bestätigen.



![Image](assets/fr/07.webp)



Geben Sie Ihrem Sicherheitsschlüssel einen Namen, damit Sie ihn leicht wiedererkennen, und klicken Sie dann auf "*Schlüssel lesen*".



![Image](assets/fr/08.webp)



Ihre Kontodaten werden auf dem Display des Ledger angezeigt. Drücken Sie zur Bestätigung die Taste "*Registrieren*" (oder beide Tasten gleichzeitig, je nach Modell).



![Image](assets/fr/09.webp)



Der Zugangsschlüssel wurde erfolgreich registriert.



![Image](assets/fr/10.webp)



Registrieren Sie diesen Sicherheitsschlüssel.



![Image](assets/fr/11.webp)



Wenn Sie sich jetzt bei Ihrem Konto anmelden, werden Sie zusätzlich zu Ihrem üblichen Passwort aufgefordert, Ihr Ledger zu verbinden.



![Image](assets/fr/12.webp)



Sie können dann die Taste "*Anmelden*" auf dem Display Ihres Ledger drücken, um die Authentifizierung zu bestätigen (oder beide Tasten gleichzeitig, je nach Modell).



![Image](assets/fr/13.webp)



Der Vorteil der Verwendung eines Hardware Wallet Ledger für die Zwei-Faktor-Authentifizierung ist, dass Sie Ihre Schlüssel dank des Mnemonic-Satzes leicht wiederherstellen können. Zusätzlich zu dieser grundlegenden Sicherung können Sie auch einen Notfallcode verwenden, der von jedem Dienst bereitgestellt wird, bei dem Sie 2FA aktiviert haben. Mit diesem Notfallcode können Sie sich mit Ihrem Konto verbinden, wenn Sie Ihren Sicherheitsschlüssel verlieren. Er ersetzt also die 2FA für eine Verbindung, falls erforderlich.



Bei Bitwarden beispielsweise können Sie diesen Code aufrufen, indem Sie auf "*Recovery-Code anzeigen*" klicken.



![Image](assets/fr/14.webp)



Ich empfehle Ihnen, diesen Code an einem anderen Ort als Ihr Hauptpasswort aufzubewahren, um zu verhindern, dass sie zusammen gestohlen werden. Wenn Ihr Passwort beispielsweise in einem Passwort-Manager gespeichert ist, bewahren Sie Ihren 2FA-Notfallcode separat auf Papier auf.



Dieser Ansatz bietet Ihnen zwei Sicherungsebenen für den Fall, dass Ihr Ledger für die 2FA-Authentifizierung verloren geht: eine erste Sicherung unter Verwendung des Mnemonic-Satzes für alle Ihre Konten und eine zweite kontospezifische Sicherung unter Verwendung der Notfallcodes. Es ist jedoch wichtig, **die Rolle des Mnemonic nicht mit der des Notfallcodes** zu verwechseln:




- Die 12- oder 24-Wort-Mnemonic-Phrase gibt Ihnen nicht nur Zugang zu den Schlüsseln, die für 2FA auf all Ihren Konten verwendet werden, sondern auch zu Ihren Bitcoins, die mit Ihrem Ledger gesichert sind;
- Der Notfallcode ermöglicht es Ihnen, die 2FA-Anfrage nur auf dem betreffenden Konto (in diesem Beispiel nur auf Bitwarden) vorübergehend zu umgehen.



Herzlichen Glückwunsch, jetzt können Sie Ihren Ledger für MFA verwenden! Wenn Sie diese Anleitung nützlich fanden, wäre ich Ihnen sehr dankbar, wenn Sie unten einen Green-Daumen hinterlassen würden. Sie können diese Anleitung auch gerne in Ihren sozialen Netzwerken teilen. Herzlichen Dank dafür!



Ich empfehle auch dieses andere Tutorial, in dem wir uns eine andere Lösung für die U2F- und FIDO2-Authentifizierung ansehen:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e