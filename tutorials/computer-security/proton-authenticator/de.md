---
name: Proton Authenticator
description: Wie kann ich Proton Authenticator verwenden, um meine Konten mit 2FA zu sichern?
---
![cover](assets/cover.webp)



Die Zwei-Faktor-Authentifizierung (2FA) fügt Ihren Konten eine zusätzliche Sicherheitsbarriere hinzu, indem sie zusätzlich zu Ihrem Passwort einen weiteren Nachweis verlangt, dass nur Sie es besitzen. Durch die Aktivierung von 2FA wird das Risiko eines Hackerangriffs drastisch reduziert, selbst wenn Ihr Passwort durch Phishing oder ein Datenleck kompromittiert wird. Ohne 2FA bräuchte ein Angreifer nur Ihr Passwort, um auf Ihre Konten zuzugreifen; mit 2FA bräuchte er auch Ihren zweiten Faktor, wodurch die meisten Versuche des Kontodiebstahls vereitelt werden.



Es gibt verschiedene Arten von 2FA. SMS-Codes sind besser als gar nichts, bleiben aber anfällig für SIM-Swapping-Angriffe und das Abfangen von Daten. Wir raten davon ab, SMS als primäre 2FA zu verwenden. Authentifizierungsanwendungen (TOTP) generate temporäre Codes lokal auf Ihrem Gerät, wodurch sie viel schwieriger abzufangen sind. Physische Sicherheitsschlüssel bieten die beste Sicherheit, erfordern aber spezielle Hardware.



Proton Authenticator ist ein TOTP-Authentifikator. Er ist die Antwort von Proton auf die Einschränkungen bestehender Anwendungen: viele sind proprietär, enthalten Werbe-Tracker und bieten keine verschlüsselte Datensicherung. Proton Authenticator hebt sich davon ab, indem es eine Open-Source-Anwendung ohne Werbung und Tracker mit einer verschlüsselten End-to-End-Sicherung bietet.



## Einführung von Proton Authenticator



Proton Authenticator ist eine mobile und Desktop-TOTP-Authentifizierungsanwendung, die von Proton entwickelt wurde und für ihre datenschutzfreundlichen Dienste bekannt ist. Wie alle Proton-Produkte ist die Anwendung quelloffen und wurde unabhängigen Sicherheitsprüfungen unterzogen. Sie ist auf allen Plattformen (Android, iOS, Windows, macOS, Linux) kostenlos verfügbar.



Proton Authenticator bietet die folgenden Hauptfunktionen:





- Generierung von **TOTP-Codes** für Ihre 2FA-Konten, kompatibel mit den meisten Websites, die Google Authenticator, Authy usw. verwenden.





- **Optionales verschlüsseltes Cloud-Backup**: Sie können die Anwendung mit Ihrem Proton-Konto verknüpfen, um Ihre Codes mit End-to-End-Verschlüsselung zu sichern und zu synchronisieren. Wenn Sie Ihr Gerät verlieren, schließen Sie einfach ein neues Gerät an, um alle Ihre Codes wiederherzustellen.





- **Synchronisierung mit mehreren Geräten**: Wenn Sie sich in der App bei Proton anmelden, werden Ihre 2FA-Codes automatisch über eine Ende-zu-Ende-Verschlüsselung zwischen mehreren Geräten synchronisiert. Unter iOS ist eine Alternative die Synchronisierung über iCloud.





- **Lokale Sperre durch Passwort oder biometrische Daten**: Die Anwendung bietet eine PIN- und/oder Fingerabdruck-/Gesichts-ID-Sperre. Selbst wenn also jemand physisch auf Ihr entsperrtes Telefon zugreift, kann er Proton Authenticator nicht öffnen.





- **Keine Datenerfassung oder Tracker**: Proton verpflichtet sich, keine persönlichen Daten über die Anwendung zu sammeln. Es gibt keine versteckte Werbung oder Verhaltensanalyse.





- **Einfacher Import/Export**: Eine der Stärken von Proton Authenticator ist der Importassistent für bestehende Konten, der mit anderen Anwendungen (Google Authenticator, Authy, Aegis usw.) kompatibel ist. Bei Bedarf können Sie Ihre Codes auch in eine Datei exportieren.



Kurz gesagt, Proton Authenticator will eine kompromisslose 2FA-Lösung sein: sicher, privat, flexibel.



## Einrichtung



Proton Authenticator ist kostenlos auf allen Plattformen verfügbar. Um die Anwendung herunterzuladen, gehen Sie auf die offizielle Seite: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Offizielle Proton Authenticator Seite mit den Hauptfunktionen der Anwendung und Interface*



Auf dieser Seite finden Sie die Download-Links für alle Betriebssysteme: Android, iOS, Windows, macOS und Linux. Klicken Sie einfach auf das Betriebssystem Ihrer Wahl und folgen Sie den Standard-Installationsschritten.



In diesem Tutorial zeigen wir Ihnen, wie Sie die App auf macOS installieren und konfigurieren. Anschließend sehen wir uns an, wie Sie die App auf iOS installieren und Ihre Codes zwischen den beiden Geräten synchronisieren.



### Installation unter macOS



Sobald Sie die Anwendung heruntergeladen und installiert haben, starten Sie Proton Authenticator. Beim ersten Start führt Sie die Anwendung durch einige erste Konfigurationsbildschirme:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Willkommensbildschirm von Proton Authenticator mit der Meldung "Sicherheit in jedem Code" und der Schaltfläche "Loslegen "*



### Ursprüngliche Einfuhr



Wenn Proton Authenticator feststellt, dass Sie zuvor eine andere 2FA-Anwendung verwendet haben, kann ein Import-Assistent erscheinen. Dieser unterstützt den direkten Import aus bestimmten Anwendungen (Google Authenticator, 2FAS, Authy, Aegis usw.). Alternativ können Sie diesen Schritt auch überspringen und Ihre Konten später manuell hinzufügen.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Importassistent für die Übertragung von Codes aus anderen Authentifizierungsanwendungen*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Kompatible Importanwendungen: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth und Google Authenticator*



### Lokaler Anwendungsschutz



Legen Sie eine Entsperr-PIN fest oder aktivieren Sie die biometrische Entsperrung (Touch ID), falls verfügbar. Dieser Schritt ist wichtig, um zu verhindern, dass jemand, der Ihren Mac verwendet, freien Zugang zu Ihren 2FA-Codes erhält.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Touch ID-Konfigurationsbildschirm mit der Meldung "Schützen Sie Ihre Daten" und der Schaltfläche "Touch ID aktivieren "*



### Optionen für die Synchronisierung



Mit der Anwendung können Sie auch die iCloud-Synchronisierung aktivieren, um Ihre Daten sicher zwischen Ihren Apple-Geräten zu sichern.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*ICloud-Synchronisierungsoption mit der Meldung "Sichern Sie Ihre Daten sicher mit verschlüsselter iCloud-Synchronisierung "*



Sobald diese Schritte abgeschlossen sind, ist Proton Authenticator einsatzbereit.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface main empty Proton Authenticator mit den Optionen "Create a new code" und "Import codes "*



## Hinzufügen eines 2FA-Kontos mit ProtonMail



Wir sehen uns nun an, wie Sie Ihren ersten 2FA-Code hinzufügen, wobei wir ProtonMail als Beispiel verwenden. Diese Methode funktioniert bei allen Diensten, die die Zwei-Faktor-Authentifizierung unterstützen, identisch.



### 2FA auf ProtonMail aktivieren



Zunächst einmal können Sie in unserem Leitfaden zu ProtonMail weitere Informationen nachlesen:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Melden Sie sich bei Ihrem ProtonMail-Konto an und gehen Sie zu den Sicherheitseinstellungen. Suchen Sie nach der Option "Zwei-Faktor-Authentifizierung" und aktivieren Sie sie.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*ProtonMail-Einstellungsseite mit der Option "Authenticator-App" im Abschnitt "Zwei-Faktor-Authentifizierung "*



Klicken Sie auf die Schaltfläche, um den Authentifikator zu aktivieren, und ProtonMail wird Sie auffordern, eine Authentifizierungsanwendung auszuwählen.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*ProtonMail 2FA Konfigurationsfenster mit den Schaltflächen "Abbrechen" und "Weiter "*



ProtonMail zeigt dann einen QR-Code an, den Sie mit Ihrer Authentifizierungsanwendung scannen können.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*ProtonMail QR-Code zum Scannen mit Ihrer Authentifizierungsanwendung, mit der Option "Schlüssel stattdessen manuell eingeben" verfügbar*



Wenn Sie den Schlüssel lieber manuell eingeben möchten, klicken Sie auf "Schlüssel stattdessen manuell eingeben", um den geheimen Schlüssel anzuzeigen.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*Manuelle Eingabe von 2FA-Informationen: Schlüssel, Intervall (30) und Ziffern (6)*



### Scannen Sie den QR-Code mit Proton Authenticator



Klicken Sie in Proton Authenticator auf macOS auf "Neuen Code erstellen". Die Anwendung bietet Ihnen mehrere Optionen: **Scannen Sie einen QR-Code** oder **Geben Sie den Schlüssel manuell ein**.



Verwenden Sie die Kamera Ihres Macs, um den QR-Code zu scannen, der auf dem ProtonMail-Bildschirm angezeigt wird. Sobald Sie den QR-Code gescannt haben, werden Sie zum Konfigurationsbildschirm für den neuen Code weitergeleitet.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Fenster zur Erstellung eines neuen Eintrags mit den Feldern Titel (ProtonMail), Geheimnis, Absender (Proton), Ziffernparameter und Intervall*



Proton Authenticator wird die Informationen automatisch ausfüllen. Sie können den Namen anpassen, wenn Sie möchten, und dann auf "Speichern" klicken.



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*Generierter TOTP-Code für ProtonMail (848 812) mit Anzeige der verbleibenden Zeit*



### Konfiguration validieren



ProtonMail fordert Sie auf, einen von Proton Authenticator generierten 6-stelligen Code einzugeben, um zu bestätigen, dass die 2FA korrekt funktioniert.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*ProtonMail-Validierungsbildschirm mit der Aufforderung zur Eingabe des 6-stelligen Codes (848812)*



Kopieren Sie den Code aus der Anwendung (indem Sie ihn anklicken) und fügen Sie ihn in ProtonMail ein, um die Aktivierung abzuschließen.



Nach der Bestätigung werden Sie von ProtonMail aufgefordert, Ihre Wiederherstellungscodes herunterzuladen. Es ist wichtig, diese sorgfältig zu speichern.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*Bildschirm der ProtonMail-Wiederherstellungscodes mit einer Liste der Rettungscodes und der Schaltfläche "Download "*



### Notfall-Codes



Wenn Sie ein Konto hinzufügen, bewahren Sie die vom Dienst bereitgestellten Wiederherstellungscodes auf. Die meisten Websites bieten statische, einmalig verwendbare Wiederherstellungscodes an, die Sie an einem sicheren Ort aufbewahren können. Bewahren Sie diese Backup-Codes außerhalb von Proton Authenticator auf, damit Sie auf Ihr Konto zugreifen können, wenn Sie den Zugriff auf die 2FA-Anwendung verlieren.



## IOS-Installation und Code-Import



Nachdem Sie Proton Authenticator nun auf macOS eingerichtet haben, möchten Sie es vielleicht auch auf Ihrem iPhone oder iPad verwenden. Hier erfahren Sie, wie Sie Ihre 2FA-Codes auf mehreren Geräten erhalten.



### Laden Sie die Anwendung auf iOS herunter



Gehen Sie zum App Store und suchen Sie nach "Proton Authenticator". Laden Sie die Anwendung herunter und installieren Sie sie auf Ihrem iOS-Gerät.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*Installationsprozess auf iOS: Willkommensbildschirm, Importassistent, Auswahl kompatibler Anwendungen und abschließender Bildschirm "Codes von Proton Authenticator importieren "*



### Methode 1: Export/Import über JSON-Datei



Wenn Sie keine automatische Synchronisierung verwenden (iCloud oder Proton Account), müssen Sie Ihre Codes manuell von Ihrem Mac auf Ihr iPhone übertragen:



**Schritt 1 - Exportieren von macOS** :



Öffnen Sie auf Ihrem Mac Proton Authenticator und gehen Sie zu Einstellungen (Zahnradsymbol). Klicken Sie im Menü auf "Exportieren".



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*Proton Authenticator Einstellungsmenü auf macOS mit sichtbarer Option "Export "*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*Exportfenster mit Dateiname "Proton_Authenticator_backup_2025" und Schaltfläche "Speichern "*



Sichern Sie die JSON-Datei auf Ihrem Mac. Sie können sie per sicherer E-Mail versenden oder in iCloud Drive für den Zugriff von Ihrem iPhone aus speichern.



**Schritt 2 - Importieren auf iOS** :



Installieren Sie auf Ihrem iPhone Proton Authenticator und wählen Sie bei der Konfiguration, Codes zu importieren. Wählen Sie "Proton Authenticator" aus der Liste und importieren Sie die JSON-Datei.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*Importvorgang unter iOS: Lokalisierung der JSON-Datei, Importbestätigung und Konfigurationsbildschirme mit Face ID- und iCloud-Optionen*



### Methode 2: Automatische Synchronisierung



**Über ein Proton-Konto (für die plattformübergreifende Synchronisierung)** :



Wenn Sie noch kein Proton-Konto eingerichtet haben und zwischen verschiedenen Betriebssystemen synchronisieren möchten, werden Sie von der Anwendung aufgefordert, ein Proton-Konto zu erstellen oder zu verbinden.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Bildschirm zur Gerätesynchronisation mit der Aufforderung, ein kostenloses Proton-Konto zu erstellen oder eine Verbindung zu einem bestehenden Konto herzustellen*



**Über iCloud (nur für das Apple-Ökosystem)** :


Wenn Sie nur Apple-Geräte verwenden, können Sie in den Anwendungseinstellungen die iCloud-Synchronisierung wählen. Mit dieser Methode werden Ihre Codes automatisch und sicher zwischen all Ihren Apple-Geräten synchronisiert, ohne dass Sie ein Proton-Konto benötigen.



## Verschlüsselte Sicherung und Wiederherstellung



Eine der wichtigsten Funktionen von Proton Authenticator ist die End-to-End-Sicherung von 2FA-Codes, die sicherstellt, dass Sie bei Verlust oder Wechsel des Geräts nicht noch einmal von vorne anfangen müssen.



### Ende-zu-Ende-Verschlüsselung



Bei der verschlüsselten Cloud-Sicherung mit Proton Authenticator werden Ihre TOTP-Geheimnisse lokal auf Ihrem Gerät verschlüsselt, bevor sie an den Proton-Server gesendet werden. Die Entschlüsselung ist nur durch Sie möglich, auf Ihren Geräten, die mit Ihrem Proton-Konto verbunden sind. Die Proton AG verfügt nicht über den Schlüssel zum Auslesen Ihrer registrierten Codes.



Wenn Sie sich unter iOS für iCloud und nicht für das Proton-Konto entscheiden, werden Ihre Daten nach Apple-Standards verschlüsselt. Bei der lokalen Sicherung auf Android können Sie die Sicherungsdatei mit einem Passwort Ihrer Wahl verschlüsseln.



### Wiederherstellung im Schadensfall



Wenn Ihr Telefon verloren geht, gestohlen wird oder Sie das Mobilteil wechseln:



**Mit aktivierter Proton-Sicherung**: Installieren Sie Proton Authenticator auf dem neuen Gerät. Melden Sie sich bei der Ersteinrichtung mit demselben Proton-Konto an. Sofort wird die Anwendung alle Ihre 2FA-Codes aus dem verschlüsselten Backup synchronisieren und herunterladen.



**Mit iCloud-Backup (iOS)**: Verbinden Sie das neue iPhone/iPad mit der gleichen Apple-ID und stellen Sie sicher, dass der iCloud-Schlüsselbund aktiviert ist. Nach der Installation von Proton Authenticator verbinden Sie sich mit iCloud. Ihre Codes sollten über iCloud synchronisiert und angezeigt werden.



**Keine Cloud-Sicherung**: Sie müssen Ihre Konten manuell importieren. Wenn Sie eine Sicherungsdatei exportiert haben, verwenden Sie die Importfunktion in Proton Authenticator. Im schlimmsten Fall, wenn Sie kein Backup hatten, müssen Sie die Backup-Codes für jeden Dienst verwenden oder den Support kontaktieren.



Mit Proton Authenticator können Sie Ihre Konten jederzeit exportieren, entweder als verschlüsselte Datei oder als QR-Code für mehrere Konten. Diese Optionen geben Ihnen zusätzliche Sicherheit.



## Bewährte Praktiken



Die Verwendung eines 2FA-Authentifikators erhöht Ihre Sicherheit erheblich, doch müssen bestimmte bewährte Verfahren eingehalten werden:



### Speichern Sie Ihre Notfallcodes



Wenn Sie 2FA bei einem Dienst aktivieren, erhalten Sie oft eine Liste mit Wiederherstellungscodes. Bewahren Sie diese nicht auf Ihrem Telefon auf (auf Papier, in einem verschlüsselten Passwortmanager usw.). Im Falle eines Totalverlusts Ihres Authentifikators werden diese statischen Codes Sie retten.



### Verwechseln Sie nicht Ihre Passwörter und 2FA-Codes



Es ist verlockend, einen Passwortmanager zu verwenden, der auch TOTPs speichert. Wenn Sie jedoch das Passwort und den 2FA-Code am selben Ort aufbewahren, schaffen Sie einen einzigen Fehlerpunkt und schwächen die doppelte Authentifizierung. Für maximale Sicherheit empfehlen viele Experten, die beiden Faktoren zu trennen: Passwörter in einem sicheren Manager und 2FA-Codes in einer separaten Anwendung wie Proton Authenticator. Die Verwendung eines integrierten Managers ist jedoch immer noch besser, als gar keine 2FA zu haben.



### Aktivieren Sie mehrere 2FA-Methoden



Idealerweise sollten Sie für Ihre wichtigen Konten mehr als einen zweiten Faktor verwenden. Zögern Sie nicht, einen physischen Sicherheitsschlüssel hinzuzufügen, wenn der Dienst dies zulässt. Weitere Informationen finden Sie in unserem Tutorial über physische Schlüssel von Yubikey:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Halten Sie auch gedruckte Notfallcodes bereit.



### Bleiben Sie diskret und schützen Sie Ihr Gerät



Lassen Sie niemanden Ihr entsperrtes Telefon durchsuchen. Mit Proton Authenticator sind Ihre Codes durch eine PIN/Biometrie geschützt - geben Sie diese PIN nicht preis. Hüten Sie sich auch vor Phishing: Wenn Sie selbst mit 2FA einen Code in Echtzeit an eine betrügerische Website weitergeben, könnte er von einem Angreifer verwendet werden.



### Aktualisierungen und Audits



Proton Authenticator auf dem neuesten Stand zu halten (Updates korrigieren mögliche Fehler). Da der Code offen ist, führt die Gemeinschaft informelle Audits durch, und Proton veröffentlicht die Ergebnisse der formellen Audits.



## Vergleich mit anderen Anwendungen



Wie schneidet Proton Authenticator im Vergleich zu anderen Authentifizierungsanwendungen ab? Hier ist eine vergleichende Zusammenfassung:



**Proton Authenticator**: Open Source, optionales E2EE-verschlüsseltes Cloud-Backup, geräteübergreifende Synchronisierung, lokales Sperren, kein Tracking, verfügbar auf Mobilgeräten und Desktop.



**Google Authenticator**: Proprietär, Sicherung über Google-Konto seit 2023, aber ohne Ende-zu-Ende-Verschlüsselung (Schlüssel können von Google eingesehen werden), Multi-Geräte-Synchronisation ab 2023, standardmäßig keine Anwendungssperre, enthält Google-Tracker.



**Aegis Authenticator**: Open Source, nur lokale Sicherung, keine Cloud-Synchronisierung, Code/biometrische Sperre, kein Tracking, nur Android.



**Authy**: Proprietäres, passwortverschlüsseltes Cloud-Backup, aber geschlossener Code, Multi-Geräte-Synchronisation, PIN-Sperre/Fingerabdruck, sammelt Telefonnummern, Desktop-Anwendung wird im März 2024 eingestellt.



Nachstehend finden Sie unseren Leitfaden zu Authy:



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator ist eine der umfassendsten und sichersten Lösungen auf dem Markt: Open Source, verschlüsselte Synchronisation mit mehreren Geräten, keine kommerziellen Folgeaktivitäten.



## Ressourcen und Unterstützung



### Offizielle Dokumentation




- **Offizielle Website**: [proton.me/authenticator](https://proton.me/authenticator) - Produktpräsentation und Downloads
- **Download-Seite**: [proton.me/de/authenticator/download](https://proton.me/fr/authenticator/download) - Links für alle Betriebssysteme
- **Proton-Unterstützung**: [proton.me/support/zwei-faktoren-authentifizierung-2fa](https://proton.me/support/two-factor-authentication-2fa) - Offizielle 2FA-Aktivierungsanleitung
- **Proton-Blog**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Ankündigung und detaillierte Funktionen



### Quellcode und Transparenz




- **GitHub Proton Authenticator**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Offener Quellcode
- **Sicherheitsprüfungen**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Unabhängige Auditberichte



### Empfohlene Sicherheitstests


Testen Sie nach der Konfiguration Ihre Einrichtung:




- [Have I Been Pwned](https://haveibeenpwned.com/) - Prüfen Sie, ob Ihre Konten kompromittiert wurden
- [2FA-Verzeichnis](https://2fa.directory/) - Liste der Dienste, die 2FA unterstützen



### Gemeinschaften und Diskussionen




- Reddit r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Offizielle Proton-Gemeinschaft
- **Privacy Guides Forum**: [discuss.privacyguides.net](https://discuss.privacyguides.net) - Technische Diskussionen über Datenschutzfragen
- **Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Allgemeine Tipps zum Datenschutz



### Andere




- [Have I Been Pwned](https://haveibeenpwned.com/) - Prüfen Sie, ob Ihre Konten kompromittiert wurden
- [2FA-Verzeichnis](https://2fa.directory/) - Liste der Dienste, die 2FA unterstützen