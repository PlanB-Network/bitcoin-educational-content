---
name: Specter Desktop
description: Verwalten Sie Ihre Multi-Signatur-Bitcoin-Portfolios in völliger Souveränität mit Ihrem eigenen Knotenpunkt
---

![cover](assets/cover.webp)



Specter Desktop ist eine Open-Source-Anwendung (MIT-Lizenz), die von Cryptoadvance seit 2019 entwickelt wird und die Verwaltung von Bitcoin-Wallets mit Ihren Hardware-Wallets (Ledger, Trezor, Coldcard, BitBox02, Passport usw.) und Ihrer eigenen Bitcoin-Infrastruktur (Bitcoin Core Node oder Electrum Server) erleichtert. Die Anwendung zeichnet sich besonders bei Konfigurationen mit mehreren Signaturen aus und ermöglicht es Ihnen, große Summen zu sichern, indem Sie die Signierleistung auf mehrere unabhängige Hardware-Wallets verteilen.



**In diesem Lernprogramm lernen Sie, wie man:**




- Installieren und konfigurieren Sie Specter Desktop auf Ihrem Computer (Windows, macOS oder Linux)
- Verbinden Sie Specter mit einem Electrum-Server (in diesem Beispiel wird Umbrel verwendet)
- Erstellen eines einfachen wallet mit wallet-Hardware (Coldcard)
- Bitcoins mit voller Souveränität empfangen und versenden
- Einrichten eines 2-on-3-Multisignatur-wallet mit mehreren Hardware-Geldbörsen
- Specter auf einem Umbrel-Server installieren (Bonus für Fortgeschrittene)



Alle Ihre Transaktionen werden lokal über Ihre eigene Infrastruktur validiert, ohne dass Informationen an externe Server übertragen werden, wodurch Ihre Vertraulichkeit und finanzielle Souveränität gewährleistet sind. Überprüfen Sie Transaktionen immer auf Ihrem wallet-Hardware-Bildschirm, bevor Sie unterschreiben.



## Herunterladen und Installieren



Besuchen Sie die offizielle Specter Desktop Website, um die Anwendung herunterzuladen.



![Page d'accueil Specter](assets/fr/01.webp)



Wählen Sie auf der Download-Seite die Version aus, die Ihrem Betriebssystem entspricht: macOS, Windows oder Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Nach dem Herunterladen installieren Sie die Anwendung gemäß den üblichen Anweisungen Ihres Betriebssystems. Unter macOS ziehen Sie das Symbol in Programme. Unter Windows führen Sie das Installationsprogramm aus. Unter Linux folgen Sie den Anweisungen des Pakets.



## Erstmalige Konfiguration



Beim ersten Start von Specter Desktop werden Sie aufgefordert, den Verbindungstyp zu wählen. Sie können eine Verbindung zu einem Electrum-Server oder zu Ihrem eigenen Bitcoin-Kernknoten herstellen.



![Choix du type de connexion](assets/fr/03.webp)



In diesem Beispiel verwenden wir eine Verbindung zu einem Electrum-Server, der auf Umbrel läuft.



Weitere Informationen finden Sie in unserem Tutorial zu Umbrel:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Diese Option bietet eine schnellere Synchronisierung als Bitcoin Core. Wenn Sie dies bevorzugen, können Sie "Bitcoin Core" wählen und die Verbindung zu Ihrem lokalen Knoten konfigurieren. Die folgenden Schritte bleiben unabhängig von Ihrer Wahl die gleichen.



Wählen Sie "Electrum Connection" und dann "Enter my own", um Ihren eigenen Electrum-Server zu konfigurieren.



![Configuration Electrum](assets/fr/04.webp)



Geben Sie die Adresse Ihres Electrum-Servers ein. In unserem Fall mit Umbrel wird die Adresse `umbrel.local` mit Port `50001` sein. Klicken Sie auf "Verbinden", um die Verbindung herzustellen.



Sobald die Verbindung hergestellt ist, erscheint der Willkommensbildschirm mit einer Checkliste, die Ihnen den Einstieg erleichtert. Sie müssen nun Ihre Hardware-Geldbörsen hinzufügen.



![Écran d'accueil](assets/fr/05.webp)



## Hinzufügen von wallet-Hardware



Klicken Sie im linken Menü auf "Gerät hinzufügen", um Ihre wallet-Hardware hinzuzufügen.



Specter Desktop unterstützt zahlreiche Hardware-Geldbörsen: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault, und viele andere.



Wenn Sie mehr erfahren möchten, schauen Sie sich unsere wallet-Tutorials zur Hardware an.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Wählen Sie Ihre wallet-Hardware. In diesem Beispiel verwenden wir eine Coldcard MK4.



Nachfolgend finden Sie unsere Anleitung für diese wallet-Hardware:



https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Für eine Coldcard müssen Sie die öffentlichen Schlüssel von der wallet-Hardware entweder über eine USB-Verbindung oder eine microSD-Karte exportieren.



![Import des clés du Coldcard](assets/fr/07.webp)



Folgen Sie den angezeigten Anweisungen, um die Schlüssel von Ihrer Coldcard zu exportieren. Geben Sie Ihrer wallet-Hardware einen Namen (hier "MK4 Tuto"). Sobald die Schlüssel importiert wurden, können Sie ein wallet mit einem einzigen Schlüssel erstellen oder andere Hardware-Geldbörsen für ein wallet mit mehreren Signaturen hinzufügen.



![Dispositif ajouté](assets/fr/08.webp)



## Erstellung eines Portfolios



Nachdem Sie Ihre wallet-Hardware hinzugefügt haben, klicken Sie auf "Create single key wallet" (Einzelschlüssel wallet erstellen), um einen wallet mit Einzelsignatur zu erstellen.



Geben Sie Ihrem Portfolio einen Namen (z. B. "Wallet für tuto") und wählen Sie den Adresstyp. Wählen Sie "Segwit", um native bech32-Adressen zu verwenden, die die Transaktionskosten optimieren.



![Configuration du portefeuille](assets/fr/09.webp)



Sobald Ihr Portfolio erstellt wurde, bietet Specter an, eine Backup-PDF-Datei zu speichern, die alle öffentlichen Informationen enthält, die zur Wiederherstellung Ihres Portfolios benötigt werden (Deskriptoren, erweiterte öffentliche Schlüssel). Diese Datei enthält nicht Ihre privaten Schlüssel.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Bitcoins erhalten



Um Bitcoins zu empfangen, wählen Sie Ihr wallet im linken Menü aus und klicken Sie dann auf die Registerkarte "Empfangen".



Specter erstellt automatisch eine neue Empfangsadresse mit einem QR-Code.



![Génération d'une adresse de réception](assets/fr/11.webp)



Sie können die Adresse kopieren oder den QR-Code scannen. Überprüfen Sie die Adresse immer auf dem Bildschirm Ihres wallet, bevor Sie sie an jemanden weitergeben.



## Historie und Adressen anzeigen



Sobald Sie Bitcoins erhalten haben, können Sie Ihre Transaktionen auf der Registerkarte "Transaktionen" einsehen.



![Historique des transactions](assets/fr/12.webp)



Auf der Registerkarte "Adressen" können Sie alle von Ihrem Portfolio generierten Adressen mit ihrem Nutzungsstatus und den zugehörigen Beträgen einsehen.



![Liste des adresses](assets/fr/13.webp)



## Bitcoins senden



Um Bitcoins zu versenden, klicken Sie auf die Registerkarte "Senden". Geben Sie die Adresse des Empfängers und den zu sendenden Betrag ein und aktivieren Sie die erweiterten Optionen, wenn Sie die UTXOs (Münzkontrolle) manuell auswählen möchten.



![Création d'une transaction](assets/fr/14.webp)



Klicken Sie auf "Create Unsigned Transaction", um die Transaktion zu erstellen. Specter fordert Sie dann auf, die Transaktion mit Ihrer wallet Hardware zu signieren.



![Signature de la transaction](assets/fr/15.webp)



Wenn Sie eine Coldcard verwenden, haben Sie die Wahl zwischen der Unterzeichnung über USB oder über die microSD-Karte (Air-Gapped). Bestätigen Sie die Transaktion auf dem Hardware-Bildschirm Ihres wallet und überprüfen Sie sorgfältig die Zieladresse und den Betrag.



Sobald die Transaktion unterzeichnet ist, können Sie sie im Bitcoin-Netz verbreiten.



![Options de diffusion](assets/fr/16.webp)



Klicken Sie auf "Transaktion senden", um die Transaktion zu senden. Specter bestätigt, dass Ihre Transaktion gesendet wurde, und Sie können ihren Status auf der Registerkarte "Transaktionen" verfolgen.



![Diffusion de la transaction](assets/fr/17.webp)



## Erstellung und Verwendung eines Portfolios mit mehreren Unterschriften



Einer der größten Vorteile von Specter Desktop ist seine Fähigkeit, die Verwaltung von Portfolios mit mehreren Unterschriften zu vereinfachen. Ein Multisig wallet erfordert mehrere Signaturen, um eine Transaktion zu autorisieren, und eliminiert so den Single Point of Failure. Eine 2-on-3-Konfiguration erfordert zum Beispiel zwei Unterschriften von drei separaten Hardware-Wallets, um eine Ausgabe zu bestätigen.



Um ein Multisig wallet zu erstellen, fügen Sie zunächst alle signierenden Hardware-Geldbörsen über "Gerät hinzufügen" hinzu. In diesem Beispiel werden wir drei verschiedene Hardware-Geldbörsen verwenden: eine Coldcard MK4 (bereits zuvor hinzugefügt), einen Passport und einen Ledger. Diese Diversifizierung der Hersteller erhöht die Sicherheit, da die Abhängigkeit von einer einzigen Lieferkette oder Firmware vermieden wird.



Hier sind die Links zu den Ledger- und Passport-Tutorials:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Fügen Sie den Passport hinzu, indem Sie die wallet-Hardware benennen (z. B. "Passport multi") und ihre Schlüssel per microSD-Karte oder QR-Code importieren. Klicken Sie dann auf "Weiter", um fortzufahren.



![Ajout du Passport](assets/fr/23.webp)



Fügen Sie dann das Ledger hinzu, indem Sie es über USB anschließen und die Anwendung Bitcoin auf der wallet-Hardware öffnen. Benennen Sie es (z. B. "ledger multi") und klicken Sie auf "Get via USB" und dann auf "Continue", um seine öffentlichen Schlüssel zu importieren.



![Ajout du Ledger](assets/fr/24.webp)



Sobald Sie Ihre drei Hardware-Wallets in Specter registriert haben, klicken Sie auf "wallet hinzufügen" und wählen Sie die Option "Mehrfachsignatur", um einen wallet mit Mehrfachsignatur zu erstellen.



![Choix du type de wallet](assets/fr/25.webp)



Wählen Sie die drei Hardware-Geldbörsen aus, die Sie in Ihr Multisignatur-Quorum aufnehmen möchten: MK4 Tuto, Passport multi und Ledger multi. Klicken Sie auf "Weiter", um mit dem nächsten Schritt fortzufahren.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Wählen Sie Ihre Multi-Signatur-Konfiguration. Wählen Sie "Segwit" als Adresstyp, um von optimierten Gebühren zu profitieren. Mit dem Parameter "Erforderliche Signaturen zur Autorisierung von Transaktionen (m von 3)" können Sie den Schwellenwert festlegen: Für eine 2-on-3-Konfiguration sind 2 Signaturen erforderlich. Jede wallet-Hardware zeigt ihren entsprechenden Multisig-Schlüssel an. Klicken Sie auf "wallet erstellen", um die Erstellung abzuschließen.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Ihr "Multi tuto"-Multisignatur-Portfolio ist nun erstellt. Specter empfiehlt Ihnen sofort, die Sicherungs-PDF-Datei mit der Portfolio-Beschreibung zu speichern. Klicken Sie auf "Save Backup PDF", um diese wichtige Datei herunterzuladen.



![Wallet multisig créé](assets/fr/28.webp)



Mit Specter können Sie auch wallet-Informationen über einen QR-Code oder eine Datei an jede Ihrer Hardware-Geldbörsen exportieren. Dadurch können bestimmte Hardware-Geldbörsen (wie Coldcard oder Passport) die Multisig-Konfiguration direkt in ihrem Speicher speichern.



Für Passport entsperren Sie Ihr Gerät und gehen dann zu "Konto verwalten" > "Wallet verbinden" > "Specter" > "Multisig" > "QR-Code" und scannen dann den von Specter generierten QR-Code. Ihr Passport wird Sie dann auffordern, eine Empfangsadresse von Ihrem wallet zu scannen, um die Multisig-Konfiguration zu bestätigen.



Für das MK4 schließen Sie es an Ihren PC an und entsperren es. Klicken Sie dann auf "MK4 Tuto-Datei speichern" und speichern Sie die Datei auf Ihrem MK4. Wenn Sie das nächste Mal Ihre wallet-Hardware signieren, wird das MK4 diese Datei verwenden, um die Konfiguration der Multisig zu beenden.



![Export vers les hardware wallets](assets/fr/29.webp)



Zu Ihrer Information: Sie können jederzeit über die Registerkarte "Einstellungen" Ihres Portfolios und dann "Export" auf die Sicherungskopien zugreifen:



![Accès au backup PDF](assets/fr/30.webp)



Die alltägliche Nutzung ist ähnlich wie bei einem einfachen wallet: Sie empfangen generate-Adressen wie gewohnt. Um Bitcoins zu versenden, gehen Sie auf die Registerkarte "Senden", geben Sie die Adresse des Empfängers und den Betrag ein und klicken Sie dann auf "Unsignierte Transaktion erstellen".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter erstellt einen PSBT (Partially Signed Bitcoin Transaction) und zeigt "Acquired 0 of 2 signatures" an. Sie müssen nun mit mindestens zwei Ihrer drei Hardware-Geldbörsen unterschreiben. Klicken Sie auf die erste wallet-Hardware (z. B. "MK4 Tuto"), um mit Ihrer Coldcard zu unterschreiben, dann auf die zweite (z. B. "Passport multi"), um die zweite erforderliche Signatur zu erhalten.



![Signature de la transaction](assets/fr/32.webp)



Sobald Sie die beiden erforderlichen Unterschriften erhalten haben (die Schnittstelle zeigt "Acquired 2 of 2 signatures" und "Transaction is ready to send" an), klicken Sie auf "Send Transaction", um die Transaktion im Bitcoin-Netzwerk zu übertragen.



![Transaction prête à être diffusée](assets/fr/33.webp)



Dieser Ansatz mit mehreren Unterschriften eignet sich besonders gut für Unternehmen (mehrere Manager müssen Ausgaben genehmigen), Familien (Schutz eines Mehrgenerationen-Erbes) oder Einzelpersonen, die große Summen verwalten (geografische Verteilung von Hardware-Wallets, um lokalen Katastrophen zu widerstehen).



### Die entscheidende Bedeutung von Mehrfachsignatur-Backups



**Bitte beachten Sie**: Die Sicherung eines Multisig-Portfolios unterscheidet sich grundlegend von der Sicherung eines einzelnen Portfolios. Ihre Wiederherstellungsphrasen (seed-Phrasen) allein reichen nicht aus, um ein Multisig-Portfolio wiederherzustellen. Sie müssen auch den **output descriptor** (output descriptor) sichern, der die Konfigurationsinformationen für Ihr Multisig-Portfolio enthält.



Der output descriptor enthält wichtige Daten: die erweiterten öffentlichen Schlüssel (xpubs) jedes Mitunterzeichners, die Signaturschwelle (2 auf 3 in unserem Beispiel), die Art des verwendeten Skripts (natives, verschachteltes oder altes Segwit) und die Umgehungspfade für jede wallet-Hardware. Ohne diesen Deskriptor können Sie Ihren wallet nicht wiederherstellen oder auf Ihre Bitcoins zugreifen, selbst wenn Sie zwei Ihrer drei Wiederherstellungsphrasen haben. Der Deskriptor teilt Ihrer Software mit, wie die öffentlichen Schlüssel zu den generate- und Bitcoin-Adressen, die Ihrem Guthaben entsprechen, kombiniert werden können.



Specter Desktop erzeugt automatisch eine Sicherungs-PDF-Datei, wenn Sie Ihr Multisig-Portfolio erstellen. Diese PDF-Datei enthält den vollständigen Deskriptor, die Fingerabdrücke jeder wallet-Hardware und alle für die Wiederherstellung erforderlichen öffentlichen Informationen. **Diese Datei enthält nicht Ihre privaten Schlüssel** und erlaubt es Ihnen daher nicht, Ihre Bitcoins auszugeben, aber sie erlaubt es jedem, der darauf zugreift, Ihre komplette Transaktionshistorie und Ihren Kontostand zu sehen.



Um Ihre Multisignatur-Konfiguration korrekt zu sichern, gehen Sie folgendermaßen vor: Klicken Sie nach der Erstellung Ihres Portfolios auf die Registerkarte "Einstellungen", dann auf "Export" und wählen Sie "Backup-PDF speichern". Erstellen Sie mehrere Kopien dieser PDF-Datei: Drucken Sie mindestens zwei Kopien auf Papier aus und behalten Sie außerdem eine verschlüsselte digitale Kopie. Speichern Sie eine Kopie der PDF-Datei mit jedem Ihrer Wiederherstellungssätze an geografisch getrennten Orten.



Gravieren Sie Ihre Wiederherstellungsphrasen auf feuerfeste und wasserdichte Metallplatten, um ihre Langlebigkeit zu garantieren. Unterschätzen Sie niemals die Bedeutung dieser Sicherungen: Wenn Sie den Ordner `~/.specter` auf Ihrem Computer verlieren UND eine Ihrer Hardware-Geldbörsen ohne eine Deskriptor-Sicherung verlieren, sind alle Ihre Gelder unwiederbringlich verloren, selbst bei einer 2-on-3-Konfiguration. Die Mehrfachsignatur-Redundanz schützt vor dem Verlust von wallet-Hardware, aber nur, wenn Sie den Deskriptor Ihres wallet korrekt gesichert haben.



## Vorteile und Einschränkungen von Specter Desktop



**Vorteile**: Optimale Vertraulichkeit mit vollständiger lokaler Validierung ohne Server von Drittanbietern. Multisignatur-Flexibilität für erweiterte Konfigurationen (Unternehmen, Familie, Einzelperson). Umfassende wallet-Hardwareunterstützung mit voller Interoperabilität (USB und Air-Gapped).



**Einschränkungen**: Erheblicher Lernaufwand für fortgeschrittene Bitcoin-Konzepte (UTXOs, Deskriptoren, Ableitungspfade).



## Bewährte Praktiken



Überprüfen Sie immer die Adressen und Beträge auf Ihrem Hardware-wallet-Bildschirm vor der Validierung, um sich vor Malware zu schützen.



Bewahren Sie PDF-Backups getrennt von Ihrem Saatgut auf. Diese öffentlichen Deskriptoren können in einem Banktresor oder einer verschlüsselten Cloud gespeichert werden, was die Wiederherstellung erleichtert, ohne Ihre privaten Schlüssel preiszugeben.



Testen Sie die Wiederherstellung mit token-Beträgen, bevor Sie Ihre Portfolios mit großen Fonds verwenden. Erstellen, testen, löschen und wiederherstellen, um Ihre Verfahren zu validieren.



Halten Sie Specter und Ihre Firmware auf dem neuesten Stand. Verteilen Sie Ihre Mitunterzeichner mit mehreren Unterschriften geografisch (zu Hause, im Büro oder in der Nähe), um lokalen Katastrophen zu widerstehen. Verwenden Sie beschreibende Etiketten, um Buchhaltung und Steuererklärungen zu erleichtern.



## Bonus: Installation auf einem Bitcoin-Server (Umbrel, RaspiBlitz, Start9)



Wenn Sie bereits einen Bitcoin-Server wie Umbrel, RaspiBlitz, MyNode oder Start9 besitzen, können Sie Specter Desktop direkt aus deren Application Store installieren. Dieser Ansatz bietet mehrere wesentliche Vorteile: Die Anwendung konfiguriert sich automatisch mit Ihrem lokalen Bitcoin Core-Knoten, sie bleibt rund um die Uhr über eine Weboberfläche von jedem Gerät in Ihrem Netzwerk aus zugänglich, und Sie können sogar sicher über Tor aus der Ferne darauf zugreifen. Ihre gesamte Bitcoin-Infrastruktur ist auf einem einzigen dedizierten Server zentralisiert, was die Verwaltung vereinfacht und Ihre Souveränität stärkt.



### Installation über den Umbrel App Store



Gehen Sie von Ihrer Umbrel-Oberfläche aus zum App Store und suchen Sie nach Specter Desktop. Klicken Sie auf "Installieren", um die Installation zu starten.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Sobald die Installation abgeschlossen ist, öffnen Sie Specter Desktop auf Ihrem Umbrel. Auf dem Willkommensbildschirm werden Sie aufgefordert, Ihre Verbindungsart zu wählen. Wenn Sie Specter auf Ihrem Umbrel verwenden, klicken Sie auf "Einstellungen aktualisieren", um die Verbindung zu konfigurieren.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Wählen Sie "Remote Specter USB-Verbindung", um die Verwendung von USB-Hardware-Geldbörsen zu ermöglichen, die an Ihren lokalen Computer angeschlossen sind, während Sie Specter auf dem entfernten Umbrel-Server verwenden.



![Configuration Remote Specter USB](assets/fr/20.webp)



Befolgen Sie die angezeigten Anweisungen zur Konfiguration der HWI-Bridge. Sie müssen auf die Bridge-Einstellungen des Geräts zugreifen und die Domäne `http://umbrel.local:25441` zur Whitelist hinzufügen. Klicken Sie auf "Aktualisieren", um die Konfiguration zu speichern.



![HWI Bridge Settings](assets/fr/21.webp)



Wenn Sie Ihre USB-Hardware-Geldbörsen auch von Ihrem lokalen Computer aus nutzen möchten, laden Sie die Specter Desktop-Anwendung auf Ihren Computer herunter und stellen Sie sie auf "Ja, ich führe Specter aus der Ferne aus". Klicken Sie auf "Speichern", um die Konfiguration abzuschließen.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Schlussfolgerung



Specter Desktop demokratisiert fortgeschrittene Bitcoin-Konfigurationen und macht Multisignatur zugänglich, ohne Ihre Souveränität oder Vertraulichkeit zu opfern. Für Benutzer, die erhebliche Geldbeträge verwalten, verwandelt es institutionelle Praktiken in Lösungen, die von Privatpersonen eingesetzt werden können.



Obwohl die Anwendung eine anfängliche Investition in die Infrastruktur und das Lernen erfordert, bietet sie vollständige Souveränität: Kontrolle über die Validierungsinfrastruktur, physisches Eigentum an den Schlüsseln und Transaktionen frei von der Überwachung durch Dritte. Ganz gleich, ob Sie als Einzelperson Ihre Ersparnisse sichern, als Familie ein Mehrgenerationen-Schließfach einrichten oder als Unternehmen den Cashflow verwalten, Specter Desktop ist das Referenzwerkzeug, um maximale Sicherheit und absolute Souveränität miteinander zu vereinbaren.



## Ressourcen



### Offizielle Dokumentation




- [Specter Desktop offizielle Website](https://specter.solutions/desktop/)
- [GitHub-Quellcode](https://github.com/cryptoadvance/specter-desktop)
- [Vollständige Dokumentation] (https://docs.specter.solutions/)



### Gemeinschaft und Unterstützung




- [Telegram Specter Community Group] (https://t.me/spectersupport)
- [Reddit Diskussionsforum](https://reddit.com/r/specterdesktop/)
- [GitHub Fehlerberichte] (https://github.com/cryptoadvance/specter-desktop/issues)