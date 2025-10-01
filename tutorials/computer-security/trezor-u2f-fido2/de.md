---
name: "Trezor U2F & FIDO2"
description: Verstärken Sie Ihre Online-Sicherheit mit Trezor
---
![cover](assets/cover.webp)



Trezor-Geräte sind Hardware-Geldbörsen, die ursprünglich für die Sicherung eines Bitcoin Wallet entwickelt wurden, aber auch erweiterte Optionen für eine starke Authentifizierung im Internet bieten. Dank ihrer Kompatibilität mit den Protokollen **U2F** und **FIDO2** ermöglichen sie es Ihnen, den Zugang zu Ihren Online-Konten zu sichern, ohne sich ausschließlich auf Passwörter zu verlassen.



Das U2F-Protokoll (*Universal 2nd Factor*) wurde 2014 von Google und Yubico eingeführt und anschließend von der FIDO Alliance standardisiert. Es ermöglicht das Hinzufügen eines zweiten physischen Authentifizierungsfaktors (2FA) beim Einloggen. Einmal aktiviert, müssen Nutzer zusätzlich zum klassischen Passwort jeden Versuch, sich mit ihrem Konto zu verbinden, durch Drücken einer Taste auf ihrem Trezor bestätigen. In diesem Zusammenhang funktioniert der Trezor ähnlich wie ein Yubikey.



Diese Methode basiert auf asymmetrischer Kryptografie: Es werden keine geheimen Daten übertragen, so dass Phishing- oder Abhörangriffe unwirksam sind. U2F wird inzwischen von vielen Online-Diensten unterstützt.



Zusätzlich zu U2F, das die Zwei-Faktor-Authentifizierung ermöglicht, unterstützen die Trezors auch FIDO2 (*Fast IDentity Online 2.0*), eine Weiterentwicklung von U2F. Dabei handelt es sich um ein standardisiertes Authentifizierungsprotokoll aus dem Jahr 2018, das die Logik von U2F erweitert und darauf abzielt, Passwörter vollständig zu ersetzen. Es basiert auf zwei Komponenten: *WebAuthn* (Browserseite) und *CTAP2* (physische Schlüsselseite). FIDO2 ermöglicht eine "passwortlose" Authentifizierung: Die Benutzer identifizieren sich ausschließlich über ihr Trezor-Gerät, das als einzigartiger kryptografischer Token fungiert, ohne ein zusätzliches Passwort. Dieses Protokoll ist jetzt mit einer Reihe von Online-Diensten kompatibel, insbesondere mit denen, die auf Unternehmen ausgerichtet sind.



Neben der "passwortlosen" Funktionalität ermöglicht FIDO2 auch eine Zwei-Faktor-Authentifizierung, ähnlich wie U2F.



FIDO2 führt auch das Konzept der residenten Berechtigungsnachweise ein, d. h. Identifikatoren, die direkt im Trezor gespeichert sind und sowohl den privaten Schlüssel, der die Verbindung ermöglicht, als auch die Identifikationsdaten des Benutzers enthalten. Dieser Mechanismus ermöglicht eine wirklich passwortfreie Authentifizierung: einfach den Trezor einstecken und den Zugang bestätigen, ohne eine ID oder ein Passwort einzugeben. Im Gegensatz dazu speichern nicht-ortsgebundene Anmeldeinformationen, die eher konventionell sind, nur den privaten Schlüssel im Gerät; die Benutzer-ID bleibt auf der Serverseite gespeichert und muss daher bei jeder Verbindung eingegeben werden. Wir werden uns später ansehen, wie man sie mit dem Trezor speichert.



In diesem Tutorial erfahren Sie, wie Sie U2F oder FIDO2 für die Zwei-Faktor-Authentifizierung aktivieren und wie Sie FIDO2 so konfigurieren, dass Sie ohne Passwort direkt mit Ihrem Trezor auf Ihre Konten zugreifen können.



**Hinweis:** U2F ist mit allen Trezor-Modellen kompatibel, aber FIDO2 wird nur von den Modellen Safe 3, Safe 5 und Model T unterstützt, nicht aber vom Model One.



## Verwendung von U2F/FIDO2 für 2FA auf einem Trezor



Bevor Sie beginnen, stellen Sie sicher, dass Sie Ihr Bitcoin Wallet auf Ihrem Trezor eingerichtet haben. Es ist wichtig, Ihr Mnemonic korrekt zu speichern, da die für U2F und FIDO2 bei der Zwei-Faktor-Authentifizierung verwendeten Schlüssel von diesem Mnemonic abgeleitet werden. Wenn Ihr Trezor verloren geht oder beschädigt wird, können Sie den Zugang zu Ihren Schlüsseln wiederherstellen, indem Sie Ihre Mnemonic-Phrase auf einem anderen Trezor-Gerät eingeben (beachten Sie, dass für FIDO2-Anmeldeinformationen im "*passwortlosen*" Modus seed allein nicht ausreicht, wie wir in den nächsten Abschnitten sehen werden).



Schließen Sie Ihr Trezor an Ihren Computer an und entsperren Sie es.



![Image](assets/fr/01.webp)



Greifen Sie auf das Konto zu, das Sie mit der Zwei-Faktor-Authentifizierung sichern möchten. Ich werde zum Beispiel ein Bitwarden-Konto verwenden. Sie finden die 2FA-Option in der Regel in den Einstellungen des Dienstes unter den Registerkarten "*Authentifizierung*", "*Sicherheit*", "*Anmeldung*" oder "*Passwort*".



![Image](assets/fr/02.webp)



Wählen Sie im Abschnitt für die Zwei-Faktor-Authentifizierung die Option "*Passkey*" (der Begriff kann je nach Website variieren).



![Image](assets/fr/03.webp)



Oft werden Sie aufgefordert, Ihr aktuelles Passwort zu bestätigen.



![Image](assets/fr/04.webp)



Geben Sie Ihrem Sicherheitsschlüssel einen Namen, damit Sie ihn leicht wiedererkennen, und klicken Sie dann auf "*Schlüssel lesen*".



![Image](assets/fr/05.webp)



Ihre Kontodaten werden auf dem Bildschirm des Trezor angezeigt. Berühren Sie den Bildschirm oder drücken Sie die Taste zur Bestätigung. Sie werden auch aufgefordert, Ihren PIN-Code zu bestätigen.



![Image](assets/fr/06.webp)



Registrieren Sie diesen Sicherheitsschlüssel.



![Image](assets/fr/07.webp)



Von nun an werden Sie, wenn Sie sich mit Ihrem Konto verbinden wollen, zusätzlich zu Ihrem üblichen Passwort aufgefordert, Ihren Trezor zu verbinden.



![Image](assets/fr/08.webp)



Sie können dann auf den Bildschirm Ihres Trezor drücken, um die Authentifizierung zu bestätigen.



![Image](assets/fr/09.webp)



Der Vorteil der Verwendung eines Hardware Wallet Trezor für die Zwei-Faktor-Authentifizierung ist, dass Sie Ihre Schlüssel dank der Mnemonic Phrase leicht wiederherstellen können. Zusätzlich zu dieser grundlegenden Sicherung können Sie auch einen Notfallcode verwenden, der von jedem Dienst bereitgestellt wird, bei dem Sie 2FA aktiviert haben. Dieser Notfallcode ermöglicht es Ihnen, sich mit Ihrem Konto zu verbinden, wenn Sie Ihren Sicherheitsschlüssel verlieren. Er ersetzt also die 2FA für eine Verbindung, falls erforderlich.



Bei Bitwarden beispielsweise können Sie diesen Code aufrufen, indem Sie auf "*Recovery-Code anzeigen*" klicken.



![Image](assets/fr/10.webp)



Ich empfehle Ihnen, diesen Code an einem anderen Ort als Ihr Hauptpasswort aufzubewahren, um zu verhindern, dass sie zusammen gestohlen werden. Wenn Ihr Passwort beispielsweise in einem Passwort-Manager gespeichert ist, bewahren Sie Ihren 2FA-Notfallcode separat auf Papier auf.



Dieser Ansatz bietet Ihnen zwei Sicherungsebenen für den Fall, dass Sie Ihren Trezor für die 2FA-Authentifizierung verlieren: eine erste Sicherung mit der Mnemonic-Phrase für alle Ihre Konten und eine zweite, die für jedes Konto spezifisch ist, mit den Notfallcodes. Es ist jedoch wichtig, **die Rolle des Mnemonic nicht mit der des Notfallcodes** zu verwechseln:




- Die 12- oder 24-Wörter-Mnemonic-Phrase gibt Ihnen nicht nur Zugang zu den Schlüsseln, die für 2FA auf allen Ihren Konten verwendet werden, sondern auch zu Ihren Bitcoins, die mit Ihrem Trezor gesichert sind;
- Der Notfallcode ermöglicht es Ihnen, die 2FA-Anfrage nur auf dem betreffenden Konto (in diesem Beispiel nur auf Bitwarden) vorübergehend zu umgehen.



## Verwendung von FIDO2 auf einem Trezor



Neben der Zwei-Faktor-Authentifizierung ermöglicht FIDO2 auch eine "passwortlose" Authentifizierung, d. h. ohne dass Sie bei der Anmeldung auf einer Website ein Passwort eingeben müssen. Verbinden Sie einfach Ihren Trezor mit Ihrem Computer, um auf diese Weise auf Ihr sicheres Konto zuzugreifen. Hier erfahren Sie, wie Sie diese Funktion konfigurieren.



Bevor Sie beginnen, stellen Sie sicher, dass Sie Ihr Bitcoin Wallet auf Ihrem Trezor eingerichtet haben. Es ist wichtig, den Mnemonic zu speichern, da die FIDO2 "*passwortlos*"-Kennungen mit Ihrem seed verschlüsselt werden (wie Sie diese Kennungen richtig speichern, erfahren Sie im nächsten Abschnitt).



Schließen Sie den Trezor an Ihren Computer an und entsperren Sie ihn.



![Image](assets/fr/01.webp)



Greifen Sie im Modus "*passwortlos*" auf das Konto zu, das Sie sichern möchten. Ich werde ein Bitwarden-Konto als Beispiel verwenden. Diese Option finden Sie in der Regel in den Einstellungen des Dienstes, oft unter einer Registerkarte "*Authentifizierung*", "*Sicherheit*" oder "*Kennwort*".



Bei Bitwarden zum Beispiel finden Sie die Option unter dem Reiter "*Hauptpasswort*". Klicken Sie auf "*Einschalten*", um die Authentifizierung über FIDO2 zu aktivieren.



![Image](assets/fr/11.webp)



Sie werden oft aufgefordert, Ihr Passwort zu bestätigen.



![Image](assets/fr/12.webp)



Ihre Kontodaten werden auf dem Bildschirm des Trezor angezeigt. Berühren Sie den Bildschirm oder drücken Sie die Taste zur Bestätigung. Sie müssen auch Ihren PIN-Code bestätigen.



![Image](assets/fr/13.webp)



Fügen Sie auf der Website einen Namen hinzu, um sich Ihren Sicherheitsschlüssel zu merken, und klicken Sie dann auf "*Einschalten*".



![Image](assets/fr/14.webp)



Sie werden dann aufgefordert, sich zu identifizieren, um zu überprüfen, ob der Schlüssel richtig funktioniert.



![Image](assets/fr/15.webp)



Von nun an ist es nicht mehr notwendig, beim Einloggen in Ihr Konto Ihre E-Mail Address oder Ihr Login einzugeben. Klicken Sie einfach auf die Schaltfläche, um sich mit einem physischen Schlüssel auf dem Anmeldeformular zu authentifizieren.



![Image](assets/fr/16.webp)



Bestätigen Sie die Verbindung zu Ihrem Trezor durch Eingabe Ihrer Hardware Wallet-PIN.



![Image](assets/fr/17.webp)



Sie werden mit Ihrem Konto verbunden, ohne dass Sie Ihr Passwort eingeben müssen.



![Image](assets/fr/18.webp)



**Bitte beachten Sie, dass das Hauptpasswort für Ihr Online-Konto für die Anmeldung weiterhin gültig ist, auch wenn Sie die "*passwortlose*" Authentifizierung über FIDO2 auf Ihrem Trezor aktivieren**



## Speichern Sie Ihre FIDO2-Anmeldedaten (Anmeldedaten Anwohner)



Wenn Sie FIDO2 oder U2F für die Zwei-Faktor-Authentifizierung verwenden, d. h. um sich bei Konten anzumelden, für die zusätzlich zur 2FA-Validierung über Ihren Trezor ein Passwort erforderlich ist, kann der Mnemonic-Satz allein den Zugriff auf Ihre Schlüssel wiederherstellen. Wenn Sie jedoch FIDO2 im "*passwortlosen*" Modus verwenden, wie im vorherigen Abschnitt beschrieben, müssen Sie zusätzlich zur Sicherung Ihres Mnemonic-Satzes, der diese Daten verschlüsselt, eine Kopie Ihrer FIDO-Anmeldedaten erstellen.



Dazu benötigen Sie einen Computer, auf dem Python installiert ist. Öffnen Sie ein Terminal und führen Sie den folgenden Befehl aus, um die erforderliche Trezor-Software zu installieren:



```shell
pip3 install --upgrade trezor
```



Schließen Sie Ihren Trezor über USB an den Computer an und entsperren Sie ihn mit Ihrem PIN-Code.



![Image](assets/fr/01.webp)



Um die Liste der auf dem Trezor gespeicherten FIDO2-Kennungen abzurufen, führen Sie den folgenden Befehl aus:



```shell
trezorctl fido credentials list
```



Bestätigen Sie den Export auf Ihrem Trezor.



![Image](assets/fr/19.webp)



Ihre FIDO2-Anmeldeinformationen werden auf Ihrem Terminal angezeigt. Für mein Bitwarden-Konto habe ich zum Beispiel diese Informationen erhalten:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Kopieren und speichern Sie alle diese Informationen in einer Textdatei. Diese Sicherung birgt kein nennenswertes Risiko, außer dass sie zeigt, dass Sie diese Dienste mit FIDO2 nutzen. Die "*Credential ID*" wird mit dem seed Ihres Wallet verschlüsselt, was bedeutet, dass ein Angreifer, der diese Sicherung erhält, nicht in der Lage wäre, eine Verbindung zu Ihren Konten herzustellen, sondern nur feststellen könnte, dass Sie diese Konten nutzen. Um diese IDs zu entschlüsseln, benötigen Sie den seed in Ihrem Wallet.



Sie können daher mehrere Kopien dieser Textdatei erstellen und sie an verschiedenen Orten speichern, z. B. lokal auf Ihrem Computer, bei einem Filehosting-Dienst und auf externen Medien wie einem USB-Stick. Beachten Sie jedoch, dass diese Sicherung nicht automatisch aktualisiert wird. Sie müssen sie also jedes Mal erneuern, wenn Sie eine neue "*passwortlose*" Verbindung mit Ihrem Trezor herstellen.



Nehmen wir an, Sie haben Ihren Trezor kaputt gemacht. Um Ihre FIDO2-Anmeldeinformationen wiederherzustellen, müssen Sie zunächst Ihren Wallet mit Ihrer Mnemonic-Phrase auf einem neuen FIDO2-kompatiblen Trezor-Gerät wiederherstellen.



Sobald die Wiederherstellung abgeschlossen ist, führen Sie den folgenden Befehl in Ihrem Terminal aus, um Ihre FIDO2-Kennungen auf das neue Gerät zu importieren:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Ersetzen Sie einfach `<CREDENTIAL_ID>` durch einen Ihrer Bezeichner. In meinem Fall würde dies zum Beispiel zu:



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Ihr Trezor wird Sie auffordern, Ihre FIDO2-Kennung zu importieren. Bestätigen Sie durch Drücken auf dem Bildschirm.



![Image](assets/fr/20.webp)



Ihr FIDO2-Login ist nun auf Ihrem Trezor betriebsbereit. Wiederholen Sie diesen Vorgang für jeden Ihrer Identifikatoren.



Herzlichen Glückwunsch, jetzt kannst du deine Trezor mit U2F und FIDO2 verwenden! Wenn du diese Anleitung nützlich fandest, wäre ich dir sehr dankbar, wenn du unten einen Green-Daumen hinterlassen würdest. Du kannst diese Anleitung auch gerne in deinen sozialen Netzwerken teilen. Herzlichen Dank!



Ich empfehle auch dieses andere Tutorial, in dem wir uns eine andere Lösung für die U2F- und FIDO2-Authentifizierung ansehen:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e