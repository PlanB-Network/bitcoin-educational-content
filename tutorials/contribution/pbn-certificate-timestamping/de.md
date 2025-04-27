---
name: Zeitstempelung von Plan ₿ Netzwerkzertifikaten und -diplomen
description: Verstehen, wie das Plan ₿ Netzwerk verifizierbare Nachweise für Ihr Zertifikat und Diplome ausstellt
---

![cover](assets/cover.webp)

Wenn Sie dies lesen, besteht eine hohe Wahrscheinlichkeit, dass Sie entweder ein Bitcoin-Zertifikat oder ein Abschlussdiplom für einen der Kurse erhalten haben, die Sie im Plan B Netzwerk absolviert haben, also herzlichen Glückwunsch zu dieser Leistung!

In diesem Tutorial werden wir sehen, wie das Plan B Netzwerk verifizierbare Nachweise für Ihr Bitcoin-Zertifikat oder jedes Diplom über den Abschluss eines Kurses ausstellt. Im zweiten Teil werden wir sehen, wie man die Authentizität dieser Nachweise überprüft.

# Plan B Netzwerk Nachweisverfahren

Im Plan ₿ Netzwerk bieten wir Ihnen ein Zertifikat und Diplome an, die kryptografisch von uns signiert und auf der Timechain (d.h. der Bitcoin-Blockchain) zeitgestempelt sind. Um dies zu erreichen, mussten wir ein Nachweisverfahren entwickeln, das auf 2 kryptografischen Operationen basiert:

1. Eine GPG-Signatur auf einer Textdatei, die Ihre Leistungen zusammenfasst
2. Das Zeitstempeln dieser signierten Datei über [opentimestamps](https://opentimestamps.org/).

Grundsätzlich ermöglicht Ihnen die erste Operation zu überprüfen, wer das Zertifikat (oder Diplom) ausgestellt hat, während die zweite Operation Ihnen ermöglicht zu überprüfen, wann es ausgestellt wurde.
Wir glauben, dass dieses einfache Nachweisverfahren es uns ermöglicht, Zertifikate und Diplome mit unbestreitbaren Nachweisen auszustellen, die jeder selbst überprüfen kann.

![image](./assets/proof-mechanism.webp)

Beachten Sie, dass dank dieses Nachweisverfahrens jeder Versuch, auch das kleinste Detail Ihres Zertifikats oder Diploms zu ändern, einen völlig anderen sha256-Hash der signierten Datei erzeugen würde, was sofort eine Manipulation aufdecken würde, da die Signatur und die Zeitstempelung nicht mehr gültig wären. Darüber hinaus würde eine einfache Überprüfung der Signatur den Betrug aufdecken, falls jemand versucht, böswillig einige Zertifikate oder Diplome im Namen des Plan B Netzwerks zu fälschen.

## Wie funktioniert die GPG-Signatur?

Die GPG-Signatur wird mit der Verwendung einer Open-Source-Software namens GNU Private Guard erhalten. Diese Software ermöglicht es jedem, private Schlüssel zu erstellen, Signaturen zu signieren und zu überprüfen sowie Dateien zu verschlüsseln und zu entschlüsseln. Für den Umfang dieses Tutorials wissen Sie, dass das Plan B Netzwerk GPG verwendet, um seinen privaten/öffentlichen Schlüssel zu erstellen und jedes Bitcoin-Zertifikat oder Diplom über den Abschluss eines Kurses zu signieren.

Andererseits kann jemand, der die Authentizität einer signierten Datei überprüfen möchte, GPG verwenden, um den öffentlichen Schlüssel des Ausstellers zu importieren und zu überprüfen. Im zweiten Teil des Tutorials werden wir sehen, wie man dies mit einem Terminal macht.

Für diejenigen, die neugierig sind und mehr über diese fantastische Software erfahren möchten, können Sie sich auf ["Das GNU Privacy Handbuch"](https://www.gnupg.org/gph/en/manual/x135.html) beziehen.

## Wie funktioniert das Zeitstempeln?

Jeder kann OpenTimestamps verwenden, um eine Datei zu zeitstempeln und einen verifizierbaren Nachweis der Existenz der Datei zu erhalten. Mit anderen Worten, es bietet Ihnen keinen Nachweis darüber, wann die Datei erstellt wurde, sondern einen Nachweis der Existenz nicht später als zu einem bestimmten Zeitpunkt.
OpenTimestamps kann diesen Dienst kostenlos anbieten dank einer hoch effizienten Methode, solche Nachweise in der Bitcoin Blockchain zu speichern. Es verwendet den sha256-Hash der Datei als eindeutigen Identifikator Ihrer Datei und baut einen Merkle-Baum mit anderen Hashes von eingereichten Dateien anderer Benutzer und verankert nur den Hash der Merkle-Baum-Struktur in einer OpReturn-Transaktion.
Sobald diese Transaktion in einem Block enthalten ist, kann jeder mit der ursprünglichen Datei und der `.ots`-Datei, die damit verbunden ist, die Echtheit der Zeitstempelung überprüfen. Im zweiten Teil des Tutorials werden wir sehen, wie man Ihr Bitcoin-Zertifikat oder jedes Abschlusszeugnis eines Kurses mit einem Terminal und mit einer grafischen Oberfläche über die Website von OpenTimestamps überprüft.
# Wie man ein Plan B Network Zertifikat oder Diplom überprüft

## Schritt 1. Laden Sie Ihr Zertifikat oder Diplom herunter

Loggen Sie sich in Ihr persönliches PBN-Dashboard ein.

![image](./assets/login.webp)

Gehen Sie zur Seite "Credentials", indem Sie im Menü auf der linken Seite klicken, und wählen Sie Ihre Prüfungssitzung oder Ihr Abschlusszeugnis aus.

![image](./assets/credential.webp)

Laden Sie die Zip-Datei herunter.

![image](./assets/download.webp)

Extrahieren Sie den Inhalt, indem Sie mit der rechten Maustaste auf die `.zip`-Datei klicken und "Extrahieren" auswählen. Sie finden drei verschiedene Dateien darin:

- Signierte Textdatei (z.B. zertifikat.txt)
- Open Timestamp (OTS) Datei (z.B. zertifikat.txt.ots)
- PDF-Zertifikat (z.B. zertifikat.pdf)

## Schritt 2: Überprüfung der Signatur der Textdatei

Öffnen Sie zunächst ein Terminal im Ordner, in dem sich die Dateien befinden (Rechtsklick auf das Fenster des Ordners und klicken Sie auf "Im Terminal öffnen"). Befolgen Sie dann die folgenden Anweisungen

1. Importieren Sie den öffentlichen PGP-Schlüssel des Plan ₿ Netzwerks mit dem folgenden Befehl:

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

Wenn der PGP-Schlüssel erfolgreich importiert wurde, sollten Sie eine Nachricht wie die folgende sehen

```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

HINWEIS: Wenn Sie sehen, dass 1 Schlüssel verarbeitet und 0 importiert wurde, haben Sie wahrscheinlich denselben Schlüssel zuvor bereits importiert, und das ist in Ordnung.

2. Überprüfen Sie die Signatur des Zertifikats oder Diploms mit folgendem Befehl:

```bash
gpg --verify certificate.txt
```

Dieser Befehl sollte Ihnen Details über die Signatur zeigen, einschließlich:

- Wer es signiert hat (Plan ₿ Netzwerk)
- Wann es signiert wurde
- Ob die Signatur gültig ist

Dies ist ein Beispiel für das Ergebnis:

```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```

Wenn Sie eine Nachricht wie "BAD signature" sehen, bedeutet das, dass die Datei manipuliert wurde.

## Schritt 3: Überprüfung des Open Timestamp

### Überprüfung über eine grafische Oberfläche

1. Besuchen Sie die OpenTimestamps-Website: https://opentimestamps.org/
2. Klicken Sie auf den Tab "Stamp & Verify".
3. Ziehen Sie die OTS-Datei (z.B. `certificate.txt.ots`) in den dafür vorgesehenen Bereich.
4. Ziehen Sie die zeitgestempelte Datei (z.B. `certificate.txt`) in den dafür vorgesehenen Bereich.
5. Die Website wird den Open Timestamp automatisch überprüfen und das Ergebnis anzeigen.

Wenn Sie eine Nachricht wie die folgende sehen, ist Ihr Zeitstempel gültig:
![cover](assets/opentimestamp_wegui_verified.webp)
### CLI-Methode

HINWEIS: Dieses Verfahren **erfordert einen lokalen Bitcoin-Knoten, der läuft**

1. Installieren Sie den OpenTimestamps-Client aus dem offiziellen Repository: https://github.com/opentimestamps/opentimestamps-client, indem Sie den folgenden Befehl ausführen:

```
pip install opentimestamps-client
```

2. Navigieren Sie in das Verzeichnis, das die extrahierten Zertifikatsdateien enthält.

3. Führen Sie den folgenden Befehl aus, um den Open Timestamp zu überprüfen:

```
ots verify certificate.txt.ots
```

Dieser Befehl wird:

- Den Zeitstempel gegen die Blockchain von Bitcoin prüfen
- Ihnen zeigen, wann genau die Datei mit einem Zeitstempel versehen wurde
- Die Authentizität des Zeitstempels bestätigen

### Endergebnisse

Beachten Sie, dass die Überprüfung erfolgreich ist, wenn **beide** Nachrichten angezeigt werden:

1. Die GPG-Signatur wird als **"Gute Signatur von Plan ₿ Network"** gemeldet
2. Die OpenTimestamps-Überprüfung zeigt einen spezifischen Bitcoin-Blockzeitstempel und berichtet **"Erfolg! Bitcoin-Block [Blockhöhe] bezeugt, dass Daten bereits am [Zeitstempel] existierten"**

Jetzt, da Sie wissen, wie das Plan B Network einen verifizierbaren Nachweis für jedes Bitcoin-Zertifikat und Diplom über den Abschluss eines Kurses ausstellt, können Sie leicht die Integrität davon überprüfen.