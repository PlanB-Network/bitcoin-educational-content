---
name: Bitcoin Keeper
description: Bitcoin mobile wallet für Sicherheit und multi-sig
---

![cover](assets/cover.webp)



Die sichere Verwaltung von Bitcoins stellt eine große Herausforderung für jeden Inhaber dar, der sich bewusst ist, dass die finanzielle Souveränität auf dem Spiel steht. Zwischen der Einfachheit eines mobilen wallet und der Robustheit einer multi-sig-Lösung kann die technische Lücke für viele Nutzer entmutigend erscheinen. Bitcoin Keeper ist genau an dieser Schnittstelle positioniert und bietet einen progressiven Ansatz für die Sicherheit, der die Nutzer bei ihrer Entwicklung begleitet.



Bitcoin Keeper ist eine Open-Source-Mobilanwendung, die ausschließlich für Bitcoin bestimmt ist und vom BitHyve-Team entwickelt wurde. Ihr Ziel ist es, fortschrittliches Portfoliomanagement zugänglich zu machen, insbesondere Multisignatur-Konfigurationen, und gleichzeitig eine intuitive Schnittstelle für Anfänger zu erhalten. Die Anwendung trägt den Slogan "Secure today, Plan for tomorrow" und spiegelt damit die Philosophie der langfristigen Unterstützung wider.



Im Gegensatz zu generalistischen Geldbörsen, die mehrere Kryptowährungen verwalten, konzentriert sich Bitcoin Keeper ausschließlich auf Bitcoin. Dieser ausschließliche Bitcoin-Ansatz reduziert die potenzielle Angriffsfläche und vereinfacht die Benutzererfahrung erheblich. Die Anwendung zeichnet sich auch durch ihre native Integration der am weitesten verbreiteten Hardware-Wallets und ihre erweiterten UTXO-Verwaltungsfunktionen aus.



## Was ist Bitcoin Keeper?



### Philosophie und Ziele



Bitcoin Keeper wurde entwickelt, um die spezifischen Bedürfnisse von Bitcoinern zu erfüllen, die die volle Kontrolle über ihre privaten Schlüssel behalten wollen. Das Projekt umfasst die grundlegenden Prinzipien von Bitcoin: offener und überprüfbarer Quellcode, Respekt für die Privatsphäre und die Souveränität der Nutzer. Für die Nutzung der Anwendung ist keine Registrierung oder Angabe persönlicher Daten erforderlich, und sie kann für Signiervorgänge sogar offline ausgeführt werden.



Zentrales Ziel ist es, ein flexibles, zukunftssicheres Werkzeug für die Aufbewahrung von BTC über mehrere Jahre und sogar mehrere Generationen hinweg anzubieten, und zwar dank der Vererbungsfunktionalitäten. Die Anwendung ermöglicht es den Nutzern, einfach mit einem mobilen wallet zu beginnen und sich dann schrittweise zu sichereren Lösungen mit mehreren Unterschriften zu entwickeln.



### Anwendungsarchitektur



Bitcoin Keeper organisiert die Fondsverwaltung nach zwei unterschiedlichen Konzepten. Das **Hot Wallet** ist ein einfaches wallet mit einem Schlüssel, das auf dem Telefon aufbewahrt wird und für alltägliche Ausgaben und kleinere Beträge gedacht ist. Tresore** sind Tresore mit mehreren Unterschriften (Multi-Key), die mehrere Schlüssel benötigen, um eine Ausgabe zu autorisieren, und für die langfristige sichere Aufbewahrung konzipiert sind.



### Hauptmerkmale



Bitcoin Keeper unterstützt fast alle auf dem Markt befindlichen Hardware-Geldbörsen: Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport und Coinkite's Tapsigner. Die Integration erfolgt je nach Gerät über unterschiedliche Methoden: QR-Code-Scannen, NFC-Verbindung oder Datei-Import.



Die Anwendung bietet außerdem eine erweiterte UTXO-Verwaltung mit Transaktionskennzeichnung, Münzkontrolle zur manuellen Auswahl von Eingängen beim Senden und PSBT-Formatunterstützung für teilweise signierte Transaktionen.



## Installation und Erstkonfiguration



Bitcoin Keeper ist kostenlos für Android über den Google Play Store und für iOS über den App Store erhältlich. Der angegebene Herausgeber ist BitHyve. Vergewissern Sie sich vor der Installation, dass Ihr Gerät frei von Malware und auf dem neuesten Stand ist und nicht gerootet oder jailbroken ist.



Beim ersten Start fordert die Anwendung Sie auf, einen Sicherheits-PIN-Code zu erstellen. Dieser Code schützt den Zugang zu Ihrem wallet und verschlüsselt sensible Daten lokal. Wählen Sie einen starken Code und merken Sie ihn sich. Sie können dann die biometrische Authentifizierung (Fingerabdruck oder Face ID) für eine schnellere Entsperrung aktivieren.



![Installation et configuration du PIN](assets/fr/01.webp)



Die Anwendung präsentiert dann mehrere Einführungsbildschirme, die ihre drei Säulen erklären: wallet-Erstellung zum Senden und Empfangen von Bitcoins, Schlüsselverwaltung mit Hardware-wallet-Kompatibilität und Erbschaftsplanung zur Weitergabe von Bitcoins. Klicken Sie auf "Get Started" und wählen Sie dann "Start New", um eine neue Konfiguration zu erstellen.



![Écrans d'introduction](assets/fr/02.webp)



## Entdeckung der Schnittstelle



Die Oberfläche von Bitcoin Keeper ist in vier Hauptregisterkarten unterteilt, die über die untere Navigationsleiste zugänglich sind:



![Les quatre onglets de l'application](assets/fr/03.webp)



Die Registerkarte **Wallets** zeigt Ihre Wallets und deren Guthaben an. Hier haben Sie Zugriff auf Ihre Wallets, um Bitcoins zu senden und zu empfangen. Die Tags "Hot Wallet" und "Single-Key" oder "Multi-Key" ermöglichen es Ihnen, den Typ jedes wallet schnell zu identifizieren.



Die Registerkarte **Schlüssel** zentralisiert die Verwaltung Ihrer Signaturschlüssel. Hier finden Sie sowohl den von der Anwendung generierten mobilen Schlüssel als auch alle von Hardware-Wallets importierten Schlüssel. Hier können Sie auch neue Signaturgeräte hinzufügen.



Die Registerkarte **Concierge** bietet Unterstützungsdienste: Stellen Sie Fragen an das Support-Team und stellen Sie eine Verbindung zu Bitcoin-Beratern her, um persönliche Unterstützung zu erhalten.



Die Registerkarte **Mehr** (Weitere Optionen) ermöglicht den Zugriff auf Einstellungen wie persönliche Serververbindung, Schlüsselsicherung, Vererbungsdokumente, Anzeigeeinstellungen und wallet-Verwaltung.



## Verbindung zu Ihrem eigenen Server



Um Ihre Vertraulichkeit zu stärken, können Sie mit Bitcoin Keeper die Anwendung mit Ihrem eigenen Electrum-Server verbinden, anstatt die standardmäßigen öffentlichen Server zu verwenden.



![Configuration du serveur Electrum](assets/fr/04.webp)



Blättern Sie auf der Registerkarte "Mehr" nach unten, um die Servereinstellungen zu finden. Klicken Sie auf "Server hinzufügen", um eine neue Verbindung zu konfigurieren. Sie können zwischen "Public Server" (vorkonfigurierte öffentliche Server) und "Private Electrum" (Ihr eigener Server) wählen.



Für einen privaten Server geben Sie die URL (z. B. umbrel.local für einen Umbrel-Knoten) und die Portnummer (normalerweise 50001) ein. Aktivieren Sie SSL, wenn Ihr Server dies unterstützt. Sie können auch einen Konfigurations-QR-Code scannen. Sobald Sie die Parameter eingegeben haben, klicken Sie auf "Mit Server verbinden".



Wenn Sie noch keinen eigenen Bitcoin-Knoten haben, schauen Sie sich unsere Anleitung zum Umbrel an, eine einfache und kostengünstige Möglichkeit, Ihren eigenen Knoten zu spinnen:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Bitcoins erhalten



Wählen Sie auf der Registerkarte Geldbörsen das wallet aus, von dem Sie Geld erhalten möchten, indem Sie es drücken. Auf dem wallet-Bildschirm werden der Kontostand und drei Aktionsschaltflächen angezeigt: Bitcoin senden, Bitcoin empfangen und Alle Münzen anzeigen.



![Réception de bitcoins](assets/fr/05.webp)



Drücken Sie "Bitcoin empfangen". Bitcoin Keeper generiert eine neue Empfangsadresse im Bech32-Format (beginnend mit bc1...), zusammen mit dem QR-Code. Sie können dieser Adresse ein Etikett hinzufügen, um die Quelle des Geldes zu identifizieren. Geben Sie die Adresse an den Absender weiter, indem Sie den QR-Code anzeigen oder die Textadresse kopieren.



Die Anwendung generiert automatisch eine neue Adresse für jeden Empfang, so dass Ihre Privatsphäre gewahrt bleibt. Verwenden Sie "Neue Address abrufen", um bei Bedarf eine leere Adresse zu erhalten.



## UTXO-Verwaltung



Bitcoin Keeper bietet eine vollständige Übersicht über die UTXO (nicht ausgegebene Transaktionsausgaben), aus denen sich Ihr Saldo zusammensetzt. Drücken Sie auf einem wallet-Bildschirm auf "Alle Münzen anzeigen", um den Eckenmanager aufzurufen.



![Gestion des UTXO](assets/fr/06.webp)



Auf dem Bildschirm "Münzen verwalten" wird jede UTXO einzeln mit ihrem Betrag und ihrer Bezeichnung aufgelistet. Diese Ansicht ermöglicht es Ihnen, die Herkunft Ihrer Münzen zu verfolgen und sie zu organisieren. Über "Zum Senden auswählen" können Sie bestimmte UTXOs auswählen, um sie mit der Münzkontrolle zu versenden und so die Vermischung von Münzen unterschiedlicher Herkunft zu vermeiden.



## Bitcoins senden



Zum Senden wählen Sie das Quellportfolio aus und drücken auf "Bitcoin senden". Geben Sie die Zieladresse ein (eingefügt oder per QR-Code gescannt) und fügen Sie optional ein Etikett hinzu, um den Empfänger zu identifizieren.



![Envoi de bitcoins](assets/fr/07.webp)



Auf dem nächsten Bildschirm können Sie den zu überweisenden Betrag eingeben. Die Schnittstelle zeigt Ihr verfügbares Guthaben und die Umrechnung in eine Fiat-Währung an. Wählen Sie die Aufladepriorität: Niedrig (Economy, ~60 Minuten), Mittel oder Hoch (Priorität). Die geschätzten Kosten in sats/vbyte werden in Echtzeit angezeigt. Drücken Sie "Senden", um fortzufahren.



![Confirmation et envoi](assets/fr/08.webp)



Ein Übersichtsbildschirm zeigt alle Details an: wallet-Quelle, Zieladresse, Transaktionspriorität, Netzgebühren, gesendeter Betrag und Gesamtbetrag. Bitte überprüfen Sie diese Informationen sorgfältig, da Bitcoin-Transaktionen nicht umkehrbar sind. Drücken Sie "Bestätigen & Senden", um die Transaktion zu senden.



Es erscheint eine Bestätigung "Senden erfolgreich" mit der vollständigen Zusammenfassung. Die Transaktion ist in der Historie "Letzte Transaktionen" mit ihrer Bezeichnung sichtbar.



## Speichern Sie Ihre Schlüssel



Das Sichern Ihres Wiederherstellungsschlüssels ist ein wichtiger Schritt. Gehen Sie auf der Registerkarte "Mehr" zum Abschnitt "Sicherung und Wiederherstellung" und klicken Sie auf "Wiederherstellungsschlüssel".



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



Auf dem Bildschirm wird der Status Ihrer Sicherungen angezeigt. Um Ihre Sicherung zu überprüfen, fordert die Anwendung Sie auf, ein bestimmtes Wort in Ihrer Phrase zu bestätigen (z. B. das 7. Wort). Durch diese Überprüfung wird sichergestellt, dass Sie Ihre Wiederherstellungsphrase korrekt aufgeschrieben haben.



In den "Einstellungen für den Wiederherstellungsschlüssel" können Sie über "Wiederherstellungsschlüssel anzeigen" Ihre vollständige Phrase und den Fingerabdruck des Unterzeichners Ihres Schlüssels sehen. Bewahren Sie Ihre 12-Wort-Phrase auf Papier an einem sicheren Ort auf, der vor Feuchtigkeit und Feuer geschützt ist. Speichern Sie ihn niemals auf einem angeschlossenen Gerät.



## Hinzufügen eines externen Schlüssels (wallet-Hardware)



Einer der größten Vorteile von Bitcoin Keeper ist die Integration von Hardware-Geldbörsen. Drücken Sie auf der Registerkarte "Schlüssel" auf "Schlüssel hinzufügen", um eine neue Signatureinheit hinzuzufügen.



![Ajout d'une clé hardware](assets/fr/10.webp)



Wählen Sie "Schlüssel von einer Hardware hinzufügen", um einen Hardware-wallet anzuschließen. Die Anwendung unterstützt eine breite Palette von Geräten: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner, und Specter Solutions.



### Tapsigner-Konfiguration



Der Tapsigner ist eine NFC-Karte von Coinkite, die besonders für den mobilen Einsatz geeignet ist. Wenn Sie mehr erfahren möchten, haben wir ein spezielles Tutorial:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Um den Tapsigner hinzuzufügen, wählen Sie ihn aus der Liste der Hardware-Geldbörsen aus.



![Configuration du Tapsigner](assets/fr/11.webp)



Geben Sie zunächst den 6- bis 32-stelligen PIN-Code ein, der auf der Rückseite Ihrer Karte aufgedruckt ist (Standardeinstellung bei neuen Karten), oder Ihre PIN, wenn diese bereits konfiguriert ist. Drücken Sie auf "Fortfahren" und halten Sie Ihr Tapsigner nahe an die Rückseite Ihres Telefons, wenn "Bereit zum Scannen" angezeigt wird. Die NFC-Kommunikation importiert automatisch den öffentlichen Schlüssel. Sie können dann eine Beschreibung hinzufügen (z. B. "Métro Card"), um diesen Schlüssel zu identifizieren.



## Erstellen eines Multisig-Portfolios



Sobald Sie Ihre Schlüssel eingerichtet haben, können Sie einen wallet mit mehreren Unterschriften erstellen, der mehrere Geräte kombiniert. Klicken Sie auf der Registerkarte "Geldbörsen" auf "Wallet hinzufügen".



![Création d'un nouveau wallet](assets/fr/12.webp)



Sie haben drei Optionen: "Wallet erstellen" für ein neues Portfolio, "Wallet importieren", um ein vorhandenes wallet wiederherzustellen, oder "Wallet gemeinsam nutzen" für einen gemeinsamen Tresor. Wählen Sie "Wallet erstellen" und dann "Bitcoin Wallet".



![Sélection du type de wallet](assets/fr/13.webp)



Der nächste Bildschirm bietet verschiedene Konfigurationen an: "Einzeltaste", "2 von 3 Mehrfachtasten" oder "3 von 5 Mehrfachtasten". Für ein benutzerdefiniertes multi-sig drücken Sie auf "Benutzerdefinierte Einstellung wählen". Wählen Sie z. B. "1 von 2": Eine einzelne Unterschrift ist von zwei möglichen Tasten erforderlich.



Wählen Sie dann die Schlüssel aus, aus denen Ihr Tresor bestehen soll. In unserem Beispiel kombinieren wir den "Mobile Key" (Telefonsoftwareschlüssel) mit dem "TAPSIGNER" (Metro Card). Diese Konfiguration bietet Redundanz: Wenn einer der Schlüssel unzugänglich wird, können Sie Ihr Geld immer mit dem anderen ausgeben.



![Finalisation du wallet multisig](assets/fr/14.webp)



Geben Sie Ihrem wallet einen Namen (z. B. "Test PlanB"), fügen Sie eine optionale Beschreibung hinzu und überprüfen Sie die ausgewählten Tasten. Drücken Sie auf "Erstellen Sie Ihr Wallet". Eine Bestätigungsmeldung "Wallet erfolgreich erstellt" erscheint und erinnert Sie daran, die wallet-Wiederherstellungsdatei zu speichern.



Ihr neuer multisig wallet erscheint nun in der Registerkarte Brieftaschen mit dem Tag "Multischlüssel" und der Angabe "1 von 2".



### Konfigurationsdatei speichern



**Im Gegensatz zu einem einfachen wallet, bei dem die Wiederherstellungsphrase ausreicht, um den Zugang wiederherzustellen, ist für einen wallet Multisig auch die Konfigurationsdatei erforderlich, in der die Struktur des Safes beschrieben wird (welche Schlüssel teilnehmen, wie viele Signaturen erforderlich sind). Ohne diese Datei können Sie Ihren wallet auch mit allen Wiederherstellungsphrasen nicht wiederherstellen.



![Export du fichier de configuration](assets/fr/15.webp)



Um diese Datei zu exportieren, wählen Sie auf der Registerkarte "Brieftaschen" Ihren wallet multisig aus und drücken dann auf das Symbol "Einstellungen" (Zahnrad) in der oberen rechten Ecke. Klicken Sie unter "Wallet-Einstellungen" auf "Wallet-Konfigurationsdatei". Es stehen mehrere Exportoptionen zur Verfügung:





- PDF exportieren**: erzeugt ein PDF-Dokument mit allen wallet-Informationen
- QR** anzeigen: zeigt einen scannbaren QR-Code an, um die Konfiguration auf ein anderes Gerät zu importieren
- Airdrop / Dateiexport**: exportiert die Datei über die Freigabeoptionen Ihres Telefons
- NFC**: Freigabe über NFC mit einem kompatiblen Gerät



Bewahren Sie diese Konfigurationsdatei getrennt von Ihren Wiederherstellungsphrasen auf, am besten auf einem verschlüsselten oder gedruckten Medium. Wenn Sie Ihr Telefon verlieren, können Sie mit dieser Datei und den Wiederherstellungsphrasen für jeden beteiligten Schlüssel Ihr wallet multisig auf dem Bitcoin Keeper oder einer anderen kompatiblen Software wiederherstellen.



## Bewährte Praktiken



### Organisation des Fonds



Strukturieren Sie Ihre Bitcoins entsprechend ihrer Verwendung: ein heißer wallet Single-Key für laufende Ausgaben mit begrenzten Beträgen und ein oder mehrere Vaults Multi-Key für langfristige Ersparnisse. Systematisches UTXO-Tagging hilft Ihnen dabei, den Überblick darüber zu behalten, woher Ihre Gelder stammen. Dies ist besonders nützlich für die Verwaltung der Vertraulichkeit und die Vermeidung der Vermischung von Münzen unterschiedlicher Herkunft.



Schützen Sie Ihr Telefon: Aktivieren Sie die biometrische Sperre, führen Sie regelmäßig Systemaktualisierungen durch und achten Sie auf die installierten Anwendungen. Und halten Sie Bitcoin Keeper mit Sicherheits-Patches auf dem neuesten Stand.



### Backup-Sicherheit



Bewahren Sie mindestens zwei Kopien jedes Wiederherstellungssatzes auf Papier an geografisch getrennten Orten auf. Bei großen Beträgen sollten Sie graviertes, katastrophenfestes Metall in Betracht ziehen. Bewahren Sie diese Phrasen niemals auf einem mit dem Internet verbundenen Gerät auf, und fotografieren Sie sie nicht.



Für multi-sig Tresore speichern Sie auch die Konfigurationsdatei (Wallet Recovery File), die die teilnehmenden öffentlichen Schlüssel und die Tresorstruktur enthält. Mit dieser Datei und den Schlüsselwiederherstellungsphrasen kann wallet mit jeder kompatiblen Software wie Sparrow oder Specter wiederhergestellt werden.



## Vorteile und Grenzen



### Höhepunkte





- Ausschließlich Bitcoin-Anwendung reduziert Komplexität und Risiko
- Native Integration von Multisig Vaults mit schrittweiser Anleitung
- Erweiterte wallet-Hardwareunterstützung (Tapsigner, Coldcard, Ledger, Jade, etc.)
- Erweiterte Verwaltung von UTXO und Münzkontrolle
- Kann mit einem persönlichen Electrum-Server verbunden werden
- Offener, überprüfbarer Quellcode



### Zu berücksichtigende Zwänge





- Interface hauptsächlich auf Englisch
- Einige Premium-Funktionen (Cloud Backup, Assisted Server) erfordern ein Upgrade
- Die Multisig-Konfiguration erfordert eine anfängliche Schulung



## Schlussfolgerung



Bitcoin Keeper zeichnet sich als skalierbare Lösung für die Verwaltung Ihrer Bitcoins aus. Sein progressiver Ansatz, vom einfachen Hot-wallet bis hin zu Multi-Signatur-Vaults, bedeutet, dass die Sicherheit aufgerüstet werden kann, wenn sich die Anforderungen ändern. Die Fähigkeit, Hardware-Wallets wie Tapsigner einfach zu integrieren, ebnet den Weg für robuste Konfigurationen ohne übermäßige Komplexität.



Die ausschließliche Ausrichtung auf Bitcoin, der offene Quellcode und die Achtung der Privatsphäre machen es zu einer Wahl, die mit den Kernwerten des Bitcoin-Ökosystems übereinstimmt.



Dieses Tutorial behandelt die wesentlichen Funktionen von Bitcoin Keeper in der kostenlosen Version. Die Anwendung bietet auch Premium-Funktionen (Cloud Backup, Assisted Server Backup, Canary Wallets), die Gegenstand eines eigenen Tutorials sein werden. In einem der nächsten Leitfäden werden wir auch die Funktion "Erbschaftsplanung" erkunden, mit der Sie die Übertragung Ihrer Bitcoins an Ihre Angehörigen vorbereiten können, dank der in die Anwendung integrierten erweiterten Tresore und Begleitdokumente.



## Ressourcen





- Offizielle Website: [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Hilfe-Center: [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Quellcode: [github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)