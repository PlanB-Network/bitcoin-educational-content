---
name: Proton Drive
description: Implementierung von Backups
---
![cover](assets/cover.webp)

Heutzutage ist es entscheidend, eine Strategie zu etablieren, um die Zugänglichkeit, Sicherheit und das Backup Ihrer persönlichen Dateien, wie Ihre persönlichen Dokumente, Fotos oder wichtige Projekte, zu gewährleisten. Der Verlust dieser Daten kann katastrophal sein.

Um diese Probleme zu verhindern, rate ich dazu, mehrere Backups Ihrer Dateien auf verschiedenen Medien zu pflegen. Eine in der Informatik häufig verwendete Strategie ist die "3-2-1"-Backup-Strategie, die den Schutz Ihrer Dateien sicherstellt:
- **3** Kopien Ihrer Dateien;
- Gespeichert auf mindestens **2** verschiedenen Arten von Medien;
- Mit mindestens **1** Kopie außerhalb des Standorts.

Mit anderen Worten, es ist ratsam, Ihre Dateien an 3 verschiedenen Orten zu speichern, unter Verwendung verschiedener Arten von Medien, wie Ihrem Computer, einer externen Festplatte, einem USB-Stick oder einem Online-Speicherdienst. Und schließlich bedeutet eine außerhalb des Standorts aufbewahrte Kopie, dass Sie ein Backup außerhalb Ihres Hauses oder Geschäfts haben sollten. Dieser letzte Punkt hilft, den Totalverlust Ihrer Dateien im Falle lokaler Katastrophen wie Brände oder Überschwemmungen zu vermeiden. Eine externe Kopie, weit entfernt von Ihrem Zuhause oder Geschäft, stellt sicher, dass Ihre Daten unabhängig von lokalen Risiken überleben.

Um die Implementierung der 3-2-1-Backup-Strategie zu erleichtern, können Sie einen Online-Speicherdienst nutzen. Diese Lösungen, gemeinhin als "Cloud" bezeichnet, bieten zusätzlichen Schutz, indem sie Ihre Daten auf sicheren Servern speichern, die von jedem Gerät aus zugänglich sind. Der Begriff "Cloud" bezieht sich einfach auf die Speicherung von Daten auf externen Servern.

Viele Menschen nutzen die Speicherlösungen großer digitaler Unternehmen: Google Drive, Microsoft OneDrive oder Apple iCloud.
![PROTON DRIVE](assets/notext/01.webp)
Diese Lösungen sind bequem für den täglichen Gebrauch und gewährleisten die Zugänglichkeit Ihrer Daten, aber sie gewährleisten nicht die Vertraulichkeit. In diesem Tutorial schlage ich vor, eine andere Lösung zu entdecken, die genauso einfach zu verwenden ist wie die Speicherwerkzeuge von Big Tech, aber mit zusätzlichen Maßnahmen zum Schutz Ihrer Privatsphäre. Diese Lösung ist Proton Drive, das Online-Speicherwerkzeug der Schweizer Firma Proton. Wir werden auch sehen, wie man eine 3-2-1-Strategie, die für den täglichen Gebrauch geeignet ist, leicht umsetzen kann.

## Einführung in Proton Drive
Proton Drive ist eine interessante Lösung für Online-Speicher, weil es Benutzerfreundlichkeit mit Sicherheit für Ihre Dateien verbindet. Im Gegensatz zu traditionellen Cloud-Diensten von Technologiegiganten implementiert Proton Drive Maßnahmen zum Schutz Ihrer Privatsphäre. Es gewährleistet eine Ende-zu-Ende-Verschlüsselung für alle Ihre Dateien, was bedeutet, dass selbst die Teams von Proton keinen Zugriff auf Ihre Daten haben. Darüber hinaus ist Proton Drive Open-Source, was unabhängigen Experten erlaubt, den Code der Software frei zu prüfen.
![PROTON DRIVE](assets/notext/02.webp)
Das Geschäftsmodell von Proton basiert auf einem Abonnement-System, was beruhigend ist, da es darauf hindeutet, dass das Unternehmen finanziert wird, ohne notwendigerweise die Daten seiner Nutzer auszubeuten. In diesem Tutorial werde ich erklären, wie man die kostenlose Version von Proton Drive verwendet, aber es gibt auch mehrere Abonnementstufen, die mehr Funktionen bieten. Dieses Geschäftsmodell ist einem kostenlosen System im Stil von Big Tech vorzuziehen, bei dem man sich fragen könnte, ob unsere persönlichen Daten zum Profit genutzt werden. Dies scheint bei Proton nicht der Fall zu sein.

Proton Drive bietet viel mehr als einfache Speicheroptionen; es ermöglicht auch das Teilen, Bearbeiten und gemeinsame Arbeiten an Dokumenten online mit Bearbeitungswerkzeugen, ähnlich wie die Software-Suite von Google.
Bezüglich der [Preisgestaltung](https://proton.me/pricing) bietet die kostenlose Version bis zu 5 GB Speicherplatz und umfasst wesentliche Funktionen. Um die Kapazitäten auf 200 GB Speicherplatz zu erweitern, ist ein spezifisches Abonnement für Proton Drive für 4 € pro Monat verfügbar. Das Proton Unlimited-Paket bietet andererseits für 10 € pro Monat einen Speicherplatz von bis zu 500 GB auf Proton Drive, zusätzlich zu allen bezahlten Diensten von Proton, wie dem VPN und dem Passwortmanager, sowie zusätzlichen Vorteilen bei kostenlosen Tools (E-Mail und Kalender). ![PROTON DRIVE](assets/notext/03.webp)
## Wie erstellt man ein Proton-Konto?

Wenn Sie noch kein Proton-Konto haben, müssen Sie eines erstellen. Ich verweise Sie auf unser Proton Mail-Tutorial, in dem wir detailliert erklären, wie Sie ein kostenloses Proton-Konto erstellen und einrichten:

https://planb.network/tutorials/others/general/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
![PROTON DRIVE](assets/notext/04.webp)
## Wie richtet man Proton Drive ein?

Sobald Sie in Ihrem Proton-Mail eingeloggt sind, klicken Sie oben links auf dem Bildschirm auf das Symbol mit den vier kleinen Quadraten.
![PROTON DRIVE](assets/notext/05.webp)
Dann klicken Sie auf "*Drive*".
![PROTON DRIVE](assets/notext/06.webp)
Sie befinden sich jetzt auf Ihrem Proton Drive.
![PROTON DRIVE](assets/notext/07.webp)
## Wie verwendet man Proton Drive?
Um Dateien zu Ihrem Proton Drive hinzuzufügen, wenn Sie ausschließlich die Webversion verwenden (die Nutzung der lokalen Version besprechen wir später), müssen Sie Ihre Dokumente einfach per Drag-and-Drop direkt in die Schnittstelle ziehen. ![PROTON DRIVE](assets/notext/08.webp) Anschließend finden Sie Ihr Dokument auf der Startseite. ![PROTON DRIVE](assets/notext/09.webp) Um einen neuen Eintrag hinzuzufügen, klicken Sie auf den Button "*Neu*" oben links auf dem Bildschirm. ![PROTON DRIVE](assets/notext/10.webp) Die Funktion "*Datei hochladen*" öffnet Ihren lokalen Dateiexplorer, sodass Sie neue Dokumente zu Proton Drive hinzufügen können, genau wie Sie es durch Ziehen und Ablegen tun würden. ![PROTON DRIVE](assets/notext/11.webp) "*Ordner hochladen*" ermöglicht es Ihnen, einen ganzen Ordner zu importieren. ![PROTON DRIVE](assets/notext/12.webp) "*Neuer Ordner*" ermöglicht es Ihnen, einen Ordner zu erstellen, um Ihre Dokumente auf Proton Drive besser zu organisieren. ![PROTON DRIVE](assets/notext/13.webp) Klicken Sie auf diese Option, weisen Sie Ihrem Ordner einen Namen zu. ![PROTON DRIVE](assets/notext/14.webp) Dann finden Sie ihn direkt auf der Startseite von Proton Drive. ![PROTON DRIVE](assets/notext/15.webp) Schließlich ermöglicht Ihnen "*Neues Dokument*", direkt in Proton Drive ein neues Textdokument zu erstellen. ![PROTON DRIVE](assets/notext/16.webp) Wenn Sie darauf klicken, öffnet sich ein neues leeres Dokument. ![PROTON DRIVE](assets/notext/17.webp) Sie können darauf schreiben und es bearbeiten. ![PROTON DRIVE](assets/notext/18.webp) Wenn Sie auf den Button "*Teilen*" oben rechts klicken, können Sie das Dokument teilen. ![PROTON DRIVE](assets/notext/19.webp) Sie müssen nur die E-Mail des Mitwirkenden eingeben, dem Sie Zugriff auf das Dokument geben möchten, entweder im Nur-Lese-Modus oder mit Bearbeitungsrechten. ![PROTON DRIVE](assets/notext/20.webp) Wenn Sie zu Ihrem Proton Drive zurückkehren, können Sie sehen, dass das Dokument erfolgreich gespeichert wurde. ![PROTON DRIVE](assets/notext/21.webp) Im Tab "*Geteilt*" finden Sie die Dokumente, die Sie mit anderen geteilt haben. ![PROTON DRIVE](assets/notext/22.webp) Und im Tab "*Mit mir geteilt*" können Sie die Dokumente sehen, die andere mit Ihnen geteilt haben. ![PROTON DRIVE](assets/notext/23.webp) Schließlich können Sie im Tab "*Papierkorb*" Ihre kürzlich gelöschten Dokumente finden. ![PROTON DRIVE](assets/notext/24.webp) Die meisten Einstellungen für Ihr Proton Drive sind in Ihr Proton-Konto integriert. Für detaillierte Anweisungen zur Einrichtung Ihres Kontos lade ich Sie ein, dieses Tutorial zu konsultieren:
https://planb.network/tutorials/others/general/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Wie installiert man die Proton Drive Software?
Proton Drive bietet auch eine Software, die die Synchronisierung Ihrer lokalen Dateien mit Ihrem Online-Speicherplatz ermöglicht. Diese Funktion erleichtert und automatisiert die Implementierung unserer 3-2-1-Backup-Strategie. Mit der Proton Drive Software erhalten Sie 2 synchronisierte Kopien Ihrer Dateien: eine auf Ihrem Computer und die andere auf den Servern von Proton, was die Kriterien von 2 Medientypen und Offsite-Backup erfüllt. Sie müssen lediglich eine dritte Kopie erstellen, die wir später einrichten werden.
Um die Software zu nutzen, klicken Sie auf den Tab "*Computer*" in Ihrem Proton Drive-Konto und wählen Sie den Button, der Ihrem Betriebssystem entspricht, um mit dem Download fortzufahren.
Sobald Sie es installiert haben, müssen Sie sich anmelden, um Ihr Konto freizuschalten, und dann auf "*Anmelden*" klicken.
![PROTON DRIVE](assets/notext/25.webp)
Wählen Sie die lokalen Dateien aus, die Sie mit Ihrem Proton Drive synchronisieren möchten.
![PROTON DRIVE](assets/notext/26.webp)
Zum Beispiel habe ich nur den Ordner "*Proton Backup*" ausgewählt. Klicken Sie dann auf die Schaltfläche "*Weiter*".
![PROTON DRIVE](assets/notext/27.webp)
Sie gelangen dann zur Softwareoberfläche, die ähnlich wie die Webanwendung ist.
![PROTON DRIVE](assets/notext/28.webp)
Von nun an haben Sie lokal auf Ihrem Computer einen Ordner mit dem Titel "*Proton Drive*", der alle Ihre auf Proton online gespeicherten Dokumente sammelt. Wenn Sie eine Datei von Ihrem Computer zu diesem Ordner hinzufügen, finden Sie sie automatisch auf der Startseite der Proton Drive Webanwendung und umgekehrt. Für die Ordner, die Sie während der Softwareinstallation zur Synchronisierung ausgewählt haben, können Sie sie auch online finden, indem Sie im Proton Drive zur Sektion "*Computer*" gehen und dann Ihren Computer auswählen.
![PROTON DRIVE](assets/notext/29.webp)
So werden alle Ihre Dateien sowohl lokal auf Ihrem Gerät als auch auf den Online-Servern von Proton Drive gesichert und synchronisiert.

## Wie erstellt man ein Backup von Proton Drive?

Wenn Sie den vorherigen Schritten gefolgt sind, haben Sie jetzt zwei unterschiedliche Backup-Speicherorte für Ihre wichtigen Dateien. Um unsere 3-2-1-Backup-Strategie zu vervollständigen, müssen wir eine dritte Kopie hinzufügen.
Ich schlage vor, dieses zusätzliche Backup auf einem externen Medium durchzuführen, wie zum Beispiel einer externen Festplatte oder einem USB-Stick. Abhängig von der Intensität Ihrer Nutzung legen Sie eine angemessene Backup-Aktualisierungsfrequenz fest (wöchentlich, monatlich, halbjährlich...). Bei jedem gewählten Intervall müssen Sie die Gesamtheit Ihres Proton Drive herunterladen, um die Daten auf dem gewählten externen Medium zu sichern. Auf diese Weise behalten Sie selbst im Falle des Diebstahls Ihres Computers und der gleichzeitigen Zerstörung der Proton-Server dank der Kopie auf dem USB-Stick sicheren Zugang zu Ihren Dateien.

Gehen Sie dazu zu Ihrem Proton Drive.
![PROTON DRIVE](assets/notext/31.webp)
Wählen Sie alle Ihre Dateien aus.
![PROTON DRIVE](assets/notext/32.webp)
Klicken Sie dann auf den kleinen Pfeil, um sie herunterzuladen.
![PROTON DRIVE](assets/notext/33.webp)
Wir wiederholen dann den Vorgang mit unseren Dateien, die von unserem Computer synchronisiert wurden.
![PROTON DRIVE](assets/notext/34.webp)
Sie finden dann .zip-Dateien in Ihren Downloads. Verbinden Sie einfach das externe Medium Ihrer Wahl mit Ihrem Computer und übertragen Sie dann diese Dateien darauf.
![PROTON DRIVE](assets/notext/35.webp)
Wenn Sie befürchten, dass dieser USB-Stick gestohlen werden könnte, erwägen Sie, ihn mit Software wie VeraCrypt zu verschlüsseln (wir werden bald ein Tutorial zu dieser Software machen).

Herzlichen Glückwunsch, Sie haben jetzt eine sehr robuste 3-2-1-Backup-Strategie, die es Ihnen ermöglicht, das Risiko, den Zugang zu Ihren persönlichen Dokumenten zu verlieren, drastisch zu reduzieren, egal unter welchen Umständen. Indem Sie Proton Drive für Ihre Online-Backups wählen, profitieren Sie auch von einer Ende-zu-Ende-Verschlüsselung, die den Schutz Ihrer Privatsphäre garantiert.

Um mehr darüber zu erfahren, wie Sie Ihre Online-Präsenz sichern und Hacking vermeiden können, empfehle ich auch, unser detailliertes Tutorial zum Passwortmanager Bitwarden zu konsultieren:

https://planb.network/tutorials/others/general/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9