---
name: Jade

description: Anleitung zur Einrichtung Ihres JADE-Geräts
---

![Bild](assets/cover.webp)

## Tutorial-Video

![Video](https://www.youtube.com/watch?v=_U1jsTeqbTw)
Blockstream Jade - Mobile Bitcoin Hardware Wallet VOLLSTÄNDIGE ANLEITUNG von BTCsession

## Vollständige Schreibanleitung

![Bild](assets/cover2.webp)

### Voraussetzungen

1. Laden Sie die neueste Version von Blockstream Green herunter.

2. Installieren Sie diesen Treiber, um sicherzustellen, dass Jade von Ihrem Computer erkannt wird.

### Desktop-Einrichtung

![Vollständige Anleitung](https://youtu.be/0fPVzsyL360)

Öffnen Sie Blockstream Green und klicken Sie dann auf das Blockstream-Logo unter Geräte.

![Bild](assets/1.webp)

Schließen Sie Jade mit dem mitgelieferten USB-Kabel an Ihren Desktop an.

> Hinweis: Wenn Jade von Ihrem Computer nicht erkannt wird, laden Sie den Treiber aus der Anleitung hier herunter.

Sobald Jade in Green angezeigt wird, aktualisieren Sie Jade, indem Sie auf "Nach Updates suchen" klicken und die neueste Firmware-Version auswählen. Verwenden Sie das Scrollrad oder den Schalter an Jade, um die Aktualisierung zu bestätigen und fortzufahren. Stellen Sie sicher, dass Jade weiterhin die Schaltfläche "Initialisieren" anzeigt, andernfalls müssen Sie warten, bis Sie Jade eingerichtet haben, um ein Upgrade durchzuführen. Verwenden Sie die Zurück-Taste, um zu diesem Bildschirm zu gelangen, falls erforderlich.

![Bild](assets/2.webp)

Nachdem Sie die Firmware von Jade aktualisiert haben, wählen Sie "Jade einrichten" für die Netzwerk- und Sicherheitsrichtlinie, die Sie verwenden möchten.

> Tipp: Die Sicherheitsrichtlinie wird unter "Typ" auf dem Anmeldebildschirm angezeigt. Wenn Sie sich nicht sicher sind, ob Sie Singlesig oder Multisig Shield auswählen sollen, lesen Sie bitte unsere Anleitung hier. (https://help.blockstream.com/hc/en-us/articles/4403642609433)

![Bild](assets/3.webp)

Wählen Sie als Nächstes "Neue Brieftasche erstellen" und wählen Sie 12 Wörter aus, um Ihre Wiederherstellungsphrase zu generieren. Durch Klicken auf "Erweitert" haben Sie die Möglichkeit, eine 12- oder 24-Wörter-Wiederherstellungsphrase zu wählen.

![Bild](assets/4.webp)

Notieren Sie die Wiederherstellungsphrase offline auf Papier (oder verwenden Sie ein dediziertes Backup-Gerät für Wiederherstellungsphrasen für zusätzliche Sicherheit). Verwenden Sie dann das Rad oder den Schalter oben auf Ihrem Jade, um Ihre Wiederherstellungsphrase zu überprüfen. Dieser Schritt stellt sicher, dass Sie sie korrekt aufgeschrieben haben.

![Bild](assets/5.webp)

Legen Sie eine sechsstellige PIN fest und bestätigen Sie diese. Diese wird verwendet, um Blockstream Jade jedes Mal zu entsperren, wenn Sie sich in Ihre Brieftasche einloggen.

![Bild](assets/6.webp)

Wählen Sie nun einfach "Zur Brieftasche gehen" in der Green-Desktop-App aus, und Sie sehen Ihre Brieftasche in Blockstream Green geöffnet. Blockstream Jade zeigt auch an, dass es bereit ist! Sie können jetzt Ihre Jade verwenden, um Bitcoin-Transaktionen zu senden und zu empfangen.

![Bild](assets/7.webp)

Nachdem Sie Ihre Brieftasche verwendet haben, trennen Sie Blockstream Jade von Ihrem Gerät. Wenn Sie das nächste Mal die Brieftasche auf Blockstream Jade verwenden möchten, schließen Sie einfach Ihr Gerät wieder an und folgen Sie den Anweisungen.

Quelle: https://help.blockstream.com/hc/en-us/articles/17478506300825

### Anhang A - Überprüfen der Green Wallet-Download-Datei

Die Überprüfung des Downloads bedeutet, zu überprüfen, ob die heruntergeladene Datei seit der Veröffentlichung durch den Entwickler nicht verändert wurde.
Wir tun dies, indem wir überprüfen, ob die Signatur (die mit dem privaten Schlüssel des Entwicklers erstellt wurde) zusammen mit der heruntergeladenen Datei und dem öffentlichen Schlüssel des Entwicklers ein TRUE-Ergebnis liefern, wenn sie durch die Funktion gpg –verify geleitet werden. Ich zeige Ihnen als Nächstes, wie das geht. Wenn Sie den Hintergrund dazu lernen möchten, habe ich hier eine Anleitung und hier eine weitere.

Zuerst erhalten wir den Signaturschlüssel:

Für Linux öffnen Sie das Terminal und führen Sie diesen Befehl aus (Sie sollten den Text einfach kopieren und einfügen und die Anführungszeichen einschließen):

```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```

Für Mac machen Sie dasselbe, außer dass Sie zuerst GPG Suite herunterladen und installieren müssen.

Für Windows machen Sie dasselbe, außer dass Sie zuerst GPG4Win herunterladen und installieren müssen.

Sie erhalten eine Ausgabe, die besagt, dass der öffentliche Schlüssel importiert wurde.

![image](assets/9.webp)

Dieses Bild hat ein leeres alt-Attribut; der Dateiname lautet image-3-1024x162.webp

Als Nächstes müssen wir die Datei mit dem Hash der Software erhalten. Sie wird auf der GitHub-Seite von Blockstream gespeichert. Gehen Sie zuerst zu ihrer Info-Seite hier und klicken Sie auf den Link für "desktop". Sie gelangen zur neuesten Release-Seite auf GitHub und dort sehen Sie einen Link zur Datei SHA256SUMS.asc, die ein Textdokument mit dem veröffentlichten Hash von Blockstreams Programm enthält, das wir heruntergeladen haben.

![image](assets/10.webp)

GitHub:

![image](assets/11.webp)

Es ist nicht notwendig, aber nach dem Speichern auf der Festplatte habe ich "SHA256SUMS.asc" in "SHA256.txt" umbenannt, um die Datei auf dem Mac mit dem Texteditor einfacher öffnen zu können. Dies war der Inhalt der Datei:

![image](assets/12.webp)

Der Text, den wir suchen, befindet sich oben. Abhängig von der heruntergeladenen Datei gibt es eine entsprechende Hash-Ausgabe, die wir später vergleichen werden.

Der untere Teil des Dokuments enthält die Signatur, die auf die oben genannte Nachricht gemacht wurde - es handelt sich um eine Zwei-in-Eins-Datei.

Die Reihenfolge spielt keine Rolle, aber bevor wir den Hash überprüfen, werden wir überprüfen, ob die Hash-Nachricht echt ist (d.h. nicht manipuliert wurde).

Öffnen Sie das Terminal. Sie müssen sich im richtigen Verzeichnis befinden, in dem die Datei SHA256SUMS.asc heruntergeladen wurde. Wenn Sie sie beispielsweise in das Verzeichnis "Downloads" heruntergeladen haben, ändern Sie für Linux und Mac in das Verzeichnis wie folgt (Groß- und Kleinschreibung beachten):

```bash
cd Downloads
```

Natürlich müssen Sie nach diesen Befehlen die Eingabetaste drücken. Für Windows öffnen Sie CMD (Eingabeaufforderung) und geben Sie dasselbe ein (obwohl die Groß- und Kleinschreibung hier keine Rolle spielt).

Für Windows und Mac müssen Sie zuvor GPG4Win bzw. GPG Suite heruntergeladen haben, wie zuvor beschrieben. Für Linux wird gpg mit dem Betriebssystem geliefert. Geben Sie diesen Befehl in Terminal (oder CMD für Windows) ein:

```bash
gpg --verify SHA256SUMS.asc
```

Die genaue Schreibweise des Dateinamens (in Rot) kann sich je nach Tag, an dem Sie die Datei abrufen, unterscheiden. Stellen Sie sicher, dass der Befehl mit dem heruntergeladenen Dateinamen übereinstimmt. Sie sollten diese Ausgabe erhalten und die Warnung über die vertrauenswürdige Signatur ignorieren - das bedeutet nur, dass Sie dem Computer noch nicht manuell mitgeteilt haben, dass Sie dem zuvor importierten öffentlichen Schlüssel vertrauen.

![image](assets/13.webp)

Dieses Bild hat ein leeres alt-Attribut; der Dateiname lautet image-4-1024x165.webp
Dieses Ergebnis bestätigt, dass die Signatur gültig ist, und wir sind zuversichtlich, dass der private Schlüssel von "info@greenaddress.it" die Daten (den Hash-Bericht) signiert hat.

Jetzt sollten wir unsere heruntergeladene Zip-Datei hashen und das Ergebnis mit dem veröffentlichten vergleichen. Beachten Sie, dass in der Datei SHA256SUMS.asc ein Text steht, der "Hash: SHA512" sagt, was mich verwirrt, da die Datei eindeutig SHA256-Ausgaben enthält, daher werde ich das ignorieren.

Für Mac und Linux öffnen Sie das Terminal, navigieren Sie zum Speicherort der heruntergeladenen Zip-Datei (wahrscheinlich müssen Sie erneut "cd Downloads" eingeben, es sei denn, Sie haben das Terminal seitdem nicht geschlossen). Übrigens können Sie immer überprüfen, in welchem Verzeichnis Sie sich befinden, indem Sie PWD ("print working directory") eingeben, und wenn dies alles fremd ist, ist es nützlich, ein kurzes YouTube-Video anzusehen, indem Sie nach "how to navigate the Linux/Mac/Windows file system" suchen.

Um die Datei zu hashen, geben Sie Folgendes ein:

```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```

Sie sollten überprüfen, wie Ihre Datei genau heißt, und den obigen blauen Text bei Bedarf ändern.

Sie erhalten eine Ausgabe wie diese (Ihre wird sich unterscheiden, wenn die Datei von meiner abweicht):

![image](assets/14.webp)

Vergleichen Sie als Nächstes visuell die Hash-Ausgabe mit dem, was in der Datei SHA256SUMS.asc steht. Wenn sie übereinstimmen, dann –> ERFOLG! Herzlichen Glückwunsch.

Quelle: https://armantheparman.com/jade/

### Verwendung in Sparrow

Wenn Sie bereits wissen, wie man Sparrow verwendet, ist es wie immer:

> Hinweis: Der Vorgang ist derselbe wie bei Specter, zum Beispiel

Laden Sie Sparrow über den hier bereitgestellten Link herunter.

![image](assets/14.5.webp)

Klicken Sie auf Weiter, um den Einrichtungsassistenten zu starten und mehr über die verschiedenen Verbindungsoptionen zu erfahren.

![image](assets/15.webp)

Wählen Sie Ihren gewünschten Server aus und wählen Sie dann Neue Wallet erstellen.

![image](assets/16.webp)

Geben Sie einen Namen für Ihre Wallet ein und klicken Sie auf Wallet erstellen.

![image](assets/17.webp)

Wählen Sie Ihre gewünschten Richtlinien- und Skripttypen aus und wählen Sie dann Verbundene Hardware Wallet.

> Hinweis: Wenn Sie Blockstream Jade zuvor als Singlesig-Wallet mit Blockstream Green verwendet haben und Ihre Transaktionen in Sparrow anzeigen möchten, stellen Sie sicher, dass der Skripttyp mit dem Kontotyp übereinstimmt, der Ihre Guthaben in Green enthält. Die Ableitungspfad muss ebenfalls übereinstimmen.

![image](assets/18.webp)

Schließen Sie Ihren Blockstream Jade an und klicken Sie auf Scannen. Sie werden dann aufgefordert, Ihre PIN auf Jade einzugeben.

> Tipp: Stellen Sie sicher, dass die Blockstream Green-App nicht geöffnet ist, bevor Sie Ihre Jade anschließen. Wenn Green geöffnet ist, kann dies zu Problemen führen, wenn Ihre Jade in Sparrow erkannt wird.

![image](assets/19.webp)

Wählen Sie Importieren Sie den Keystore, um den öffentlichen Schlüssel des Standardkontos zu importieren, oder wählen Sie den Pfeil, um manuell den Ableitungspfad auszuwählen, den Sie verwenden möchten.

![image](assets/20.webp)

Nachdem der gewünschte Schlüssel importiert wurde, klicken Sie auf Übernehmen.

![image](assets/21.webp)

Sie haben Ihre Wallet jetzt erfolgreich eingerichtet und können mit Sparrow und Blockstream Jade Bitcoin empfangen, speichern und ausgeben.

> Hinweis: Wenn Sie Jade zuvor mit Blockstream Green als Multisig Shield-Wallet verwendet haben, sollten Sie nicht erwarten, dass Ihre neue Sparrow-Wallet den gleichen Kontostand anzeigt - dies sind unterschiedliche Wallets. Um wieder auf Ihre Multisig Shield-Wallet zuzugreifen, schließen Sie Ihre Jade einfach wieder an Blockstream Green an.

![image](assets/22.webp)
Quelle: https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-

### grüne App

Wenn Sie lieber eine mobile Anleitung haben möchten, können Sie sie mit Blockstream Green verwenden.

- Wie man Blockstream Jade mit Green einrichtet | Blockstream Jade - https://youtu.be/7aacxnc6DHg

- Wie man Bitcoin in eine Jade-Wallet empfängt | Blockstream Jade - https://youtu.be/CVtcDdiPqLA
