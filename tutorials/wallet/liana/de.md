---
name: Liana
description: Einrichten und Benutzen einer Brieftasche auf Liana
---
![cover](assets/cover.webp)

In diesem Tutorial erklären wir Ihnen Schritt für Schritt, wie Sie die Liana-Anwendung auf einem Computer nutzen können. Unter anderem erfahren Sie, wie Sie einen automatisierten Nachfolgeplan einrichten, Bitcoins in normalen Situationen empfangen und versenden und nach einer bestimmten Zeit Geld aus einem bestehenden Portfolio abrufen können.

Im Januar 2025 waren die mit Liana kompatiblen Hardware-Geldbörsen folgende: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.

Wenn Sie Guthaben aus einer bestehenden Liana-Brieftasche wiederherstellen möchten, lesen Sie die Präsentation unten und gehen Sie direkt zum Abschnitt "Bitcoins wiederherstellen".

## Einführung in die Liana-Software

Liana ist ein Open-Source-Softwarepaket für die Erstellung und Verwaltung fortschrittlicher Portfolios, insbesondere als Teil eines automatisierten Vererbungssystems oder eines robusten Sicherungsmechanismus. Das Projekt wird seit 2022 von Wizardsardine entwickelt, einem von Kévin Loaec und Antoine Poinsot mitgegründeten Unternehmen. Auf der offiziellen Website wird Liana als "ein einfaches Portfolio für die persönliche Archivierung mit Wiederherstellungs- und Vererbungsfunktionen" vorgestellt. Die Software läuft auf Computern - Linux, MacOS, Windows - und ihr (offener) Quellcode ist [auf GitHub] verfügbar (https://github.com/wizardsardine/liana).

Liana baut auf der Programmierbarkeit von Bitcoin auf, um eine fortschrittliche Geldbörse zu schaffen. Insbesondere nutzt es die Vorteile von Zeitsperren (*Timelocks*), die es erlauben, Geldmittel erst nach Ablauf einer bestimmten Zeitspanne auszugeben, und die bei der Rückgewinnung von Bitcoins eine Rolle spielen. Eine Liana-Brieftasche besteht also aus mehreren Ausgabepfaden:


- Ein Hauptausgabenpfad, der immer verfügbar ist;
- Mindestens ein Wiederherstellungspfad, der nach einer bestimmten Zeit zugänglich wird.

Das nachstehende Diagramm veranschaulicht die Funktionsweise eines Portfolios mit zwei Ausgabenpfaden:

![Schéma explicatif](assets/fr/01.webp)

Mit diesem Vorgang können Sie verschiedene Konfigurationen einrichten, darunter :


- Ein Nachfolgeplan (oder Erbschaftsplan), der es den Erben ermöglicht, im Falle des Todes des Nutzers Gelder zurückzuerhalten. Für weitere Informationen zu diesem Thema empfehlen wir die Lektüre von [Teil 4] (https://planb.network/courses/btc102/233c88d3-2e8e-5eba-ac06-efe67a209038) des Kurses BTC102.
- Ein verstärktes Backup mit Wiederherstellungszeit, das dem Nutzer die Möglichkeit gibt, sein Portemonnaie zu benutzen, ohne dass er die entsprechende geheime Phrase aufbewahren und riskieren muss, dass sie gestohlen wird, z. B. bei einem Einbruch.
- Ein Sicherheitsnetz für Menschen, die mit Bitcoin anfangen: Sie verwalten ihre eigene Wallet, und ihr "Vormund" (z. B. ein Verwandter) behält sich das Recht vor, ihre Gelder nach einer bestimmten Zeit zurückzuholen.
- Ein Mehrparteien-Signatursystem (*multisig*) mit reduzierten Anforderungen im Laufe der Zeit, um das Verschwinden eines oder mehrerer Teilnehmer, z. B. der Partner eines Unternehmens, zu bewältigen.

Die große Stärke von Liana ist die Einführung einer standardisierten Methode, die die Wiedererlangung von Geldern im Falle des Verlustes des Hauptschlüssels, der für laufende Ausgaben verwendet wird, garantiert. Dies stellt eine große Innovation für die saubere Aufbewahrung von Geldern dar, die mit Risiken behaftet ist, vor allem, wenn man sich nicht gut mit dem Thema auskennt. Liana könnte daher selbst die risikoscheuesten Nutzer dazu ermutigen, ihre Gelder nicht mehr bei einem Verwahrer (z. B. einer Börsenplattform) zu verwahren, sondern das Eigentum an ihrem Geld zurückzugewinnen, ganz im Sinne des Cypherpunk-Ethos von Bitcoin.

Natürlich hat Liana auch seine Nachteile. Der erste ist, dass Sie Ihr Wallet regelmäßig aktualisieren müssen, indem Sie eine Transaktion auf der Bitcoin-Blockchain durchführen. Dies kann mühsam (je nachdem, wie oft Sie die Software verwenden) und kostspielig (je nach Höhe der Gebühren) sein, aber es ist der Preis, den Sie für zusätzliche Sicherheit zahlen.

Ein zweiter negativer Punkt kann die Vertraulichkeit sein. Wenn Sie eine andere Person in die Konfiguration einbeziehen, ist diese Person in alle Ihre Adressen eingeweiht und kann somit Ihre Aktivitäten überwachen. Dies ist jedoch kein Problem, wenn Sie sich für ein verstärktes Backup oder für eine Nachfolgeregelung entscheiden, bei der Ihr Erbe keine unmittelbare Kenntnis von den Details des Portfolios hat.

## Vorbereitung

In diesem Tutorial werden wir einen Nachfolgeplan aufstellen. Wir verwenden :


- Ein Ledger Nano S Plus, für die täglichen Ausgaben;

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

- Eine Blockstream Jade, die zur Einziehung von Geldern verwendet wird;

https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3

- Zwei Speichermedien (USB-Sticks) zum Speichern des Portfolio-Deskriptors;
- Ein Nachfolgebrief, der Anweisungen für die Einziehung der Gelder enthält;
- Ein nummerierter, versiegelter Beutel, um sicherzustellen, dass das Rückgewinnungsgerät (die Jade) nicht verwendet wurde.

## Installation und Konfiguration

Besuchen Sie die offizielle Wizardsardine-Website und laden Sie Liana unter https://wizardsardine.com/liana/ herunter. Sie können auch die neueste Version [aus dem GitHub-Repository] (https://github.com/wizardsardine/liana/releases) herunterladen, wo Sie die Authentizität der Software überprüfen können. Die in diesem Lernprogramm verwendete Version ist 0.9.

![Télécharger Liana](assets/fr/02.webp)

Um herauszufinden, wie Sie die Authentizität und Integrität von Software vor der Installation manuell überprüfen können, empfehlen wir Ihnen diese Anleitung:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Installieren Sie die Software auf Ihrem Rechner und starten Sie sie. Wählen Sie die Option "*Erstelle eine neue Liana-Brieftasche*", um Ihre Brieftasche zu konfigurieren.

![Accueil Liana](assets/fr/03.webp)

Wählen Sie Ihren Portfoliotyp. Wenn Sie ein erweitertes Backup mit Wiederherstellungszeit einrichten möchten, können Sie die Option "*Build your own*" wählen und sich für das Standardschema entscheiden. Dies funktioniert ähnlich, nur dass Sie den Satz zur Wiederherstellung der Hardware-Brieftasche nicht beibehalten müssen.

Wir ignorieren hier den Fall der *Expanding multisig*, die eine komplexere Konfiguration einrichtet.

Für die Zwecke dieses Tutorials werden wir einfache Vererbung verwenden.

![Choisir type de portefeuille](assets/fr/04.webp)

Es folgt eine kurze Erklärung.

![Rapide explication](assets/fr/05.webp)

Sobald Sie die Erklärung gelesen haben, können Sie die Schlüssel für Ihre Liana-Geldbörse einrichten. Dies ist ein entscheidender Schritt, da er die Ausgabemerkmale Ihres Kontos bestimmt.

![Configurer clés](assets/fr/06.webp)

Im Menü "Erweiterte Einstellungen" können Sie zunächst den "Deskriptortyp" festlegen, d. h. die Art und Weise, wie der Vertrag auf der Kette geschrieben wird. Sie können zwischen zwei Typen wählen: P2WSH (SegWit) oder Taproot. In beiden Fällen ist die Semantik der Ausgabebedingungen die gleiche. Während P2WSH den Vertrag leichter verständlich macht, ist Taproot insofern überlegen, als dass ungenutzte Bedingungen ausgeblendet werden und beim Abruf Kosten gespart werden.

Diese Auswahl ist optional: Im Zweifelsfall belassen Sie die Standardoption (P2WSH im Falle von Version 0.9, aber das kann sich noch ändern).

![Choisir le type de descripteur](assets/fr/07.webp)

Als nächstes konfigurieren Sie Ihren Primärschlüssel (*Primärschlüssel*). Dieser Schlüssel (oder besser gesagt, dieser Satz von Schlüsseln) wird für die aktuelle Ausgabe von Mitteln verwendet, die keinen zeitlichen Bedingungen unterliegt. Wenn Sie auf "*Setzen*" klicken, können Sie das entsprechende *Zeichengerät* auswählen. In unserem Fall haben wir die Ledger Nano S Plus Hardware Wallet gewählt.

Erlauben Sie die Freigabe des erweiterten öffentlichen Schlüssels des Geräts. Geben Sie diesem Schlüssel einen aussagekräftigen Namen (in diesem Fall "Nano S+"). Beachten Sie, dass alle auf dem Gerät installierten Anwendungen weiterhin normal funktionieren.

![Configurer clé principale](assets/fr/08.webp)

Legen Sie dann die Rückzahlungsverzögerung fest, d. h. die Zeit, nach der die Mittel durch den *Erbschaftsschlüssel* ausgegeben werden können. Diese Verzögerung wird in Blöcken definiert, wobei zwischen den einzelnen Blöcken ein Abstand von durchschnittlich 10 Minuten liegt. Sie kann zwischen 10 Minuten (1 Block) und etwa 15 Monaten (65.535 Blöcke) liegen. Diese Obergrenze ist eine Beschränkung des Bitcoin-Protokolls, da die Sperrzeit mit 16 Bit kodiert ist.

Wenn keine besonderen Umstände vorliegen, sollten Sie sich für die längste Vorlaufzeit entscheiden: 15 Monate oder 65.535 Blöcke. So sparen Sie Kosten. Wir empfehlen Ihnen jedoch, die Aktualisierung (wie im Abschnitt "Aktualisierung des Portfolios" beschrieben) einmal im Jahr, immer zur gleichen Jahreszeit, durchzuführen, um diese Praxis zu "ritualisieren" und nicht zu vergessen.

Hier haben wir eine Wiederherstellungszeit von einer Stunde (6 Blöcke) festgelegt, um unsere Tests durchzuführen.

![Configurer temps de verrouillage](assets/fr/09.webp)

Richten Sie schließlich Ihren Nachlassschlüssel ein. Dieser Schlüssel (oder besser gesagt, eine Reihe von Schlüsseln) wird verwendet, um im Falle Ihres Verschwindens Gelder wiederzuerlangen. Klicken Sie auf "*Einstellen*", wählen Sie das Signiergerät und bestätigen Sie die Freigabe des erweiterten öffentlichen Schlüssels auf diesem Gerät.

Für dieses Lernprogramm haben wir Jade gewählt. Geben Sie dem Schlüssel einen aussagekräftigen Namen (hier "Jade"). Wie beim ersten Gerät funktionieren auch hier die herkömmlichen Konten weiter.

![Configurer clé de succession](assets/fr/10.webp)

Überprüfen Sie, ob alles in Ordnung ist, und klicken Sie auf "*Fortfahren*", um Ihre Auswahl zu bestätigen.

![Confirmer clés](assets/fr/11.webp)

Der nächste Schritt besteht darin, Ihre Portfoliobeschreibung zu speichern. Dies ist die Information, die Sie benötigen, um die Mittel auf Ihrem Konto zu finden. Im Gegensatz zur Eselsbrücke können Sie mit dem Deskriptor keine Gelder ausgeben, so dass seine Offenlegung nur ein Problem für die Vertraulichkeit darstellt (die Person kennt alle Ihre Transaktionen).

Speichern Sie zwei Kopien der Beschreibung auf elektronischen Datenträgern, z. B. auf einem USB-Stick. Achten Sie darauf, dass Sie auch zwei Kopien auf Papier ausdrucken, damit Sie im Falle einer Beschädigung der elektronischen Medien darauf zugreifen können. Jede Sicherung muss mit einer Signatureinheit verbunden sein.

![Sauvegarder descripteur](assets/fr/12.webp)

Unser Deskriptor (der am Ende des Tutorials analysiert wird) lautet wie folgt:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Der letzte Schritt der anfänglichen Portfoliokonfiguration besteht darin, den Deskriptor in jedem der Hardwareportfolios zu überprüfen, die als Signaturgeräte dienen.

![Enregistrer descripteur](assets/fr/13.webp)

Führen Sie dasselbe für jedes signierende Gerät durch. Sie müssen überprüfen und bestätigen, dass der Deskriptor zu jedem Hardware-Portfolio hinzugefügt wurde.

![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)

Ihre Wallet-Informationen sind nun registriert, und Sie müssen nur noch konfigurieren, wie Sie sich mit dem Bitcoin-Netzwerk verbinden wollen. Sie können entweder Ihren eigenen Knoten (lokal oder remote) oder die Infrastruktur von WizardSardine nutzen. In letzterem Fall müssen Sie eine E-Mail-Adresse mit Ihrer Wallet verknüpfen, über die Sie den Deskriptor abrufen können. WizardSardine hat dann Zugriff auf alle Ihre Transaktionen. Die erste Option wird daher empfohlen.

![Sélectionner connexion réseau](assets/fr/15.webp)

Wir haben uns entschieden, unseren eigenen Knoten zu verwenden. Sie können einen vorhandenen Knoten verwenden oder einen *pruned node* auf Ihrem Rechner installieren. Wenn Sie keinen Zugang zu einem anderen Knoten haben, installieren Sie Ihren eigenen Knoten auf Ihrem Rechner, was einige Zeit dauern sollte (in der Größenordnung von mehreren Tagen).

![Choisir type de nœud](assets/fr/16.webp)

Für dieses Tutorial haben wir einen bestehenden (öffentlichen) Electrum-Server verwendet. Aber seien Sie vorsichtig! Er hatte Zugriff auf alle unsere Aktivitäten mit der Liana-Brieftasche. Verwenden Sie also Ihren eigenen Knotenpunkt, wenn Sie Ihre Privatsphäre schützen wollen.

![Connexion serveur Electrum public](assets/fr/17.webp)

Sobald die Konfiguration des Knotens abgeschlossen ist, sollte sich der Hauptbildschirm öffnen und Ihre frisch erstellte Liana-Brieftasche anzeigen.

Nutzen Sie die Gelegenheit, das Rückgewinnungsgerät an einem sicheren Ort aufzubewahren. Es sollte an einem strategischen Ort aufbewahrt werden, damit es im Falle Ihres Todes von Ihren Erben gefunden werden kann.

Für zusätzliche Sicherheit können Sie die zur Wiederherstellung verwendeten Komponenten in einen versiegelten Beutel (*Sicherheitsbeutel*) geben und die Seriennummer irgendwo notieren. So ist sichergestellt, dass niemand darauf Zugriff hat und Ihr Gerät gültig bleibt.

In unserem Beispiel haben wir die folgenden Elemente zusammengestellt:


- Blockstream Jade als Signatureinheit für den Nachlass;
- Ein USB-Kabel zum Anschließen und Aufladen des Geräts;
- Eine Sicherheitskopie des Satzes auf Papier für den Fall einer Fehlfunktion oder Beschädigung des Geräts (der Datenträger kann auch aus Metall bestehen und somit vor Witterungseinflüssen geschützt sein, wie dies z. B. bei Cryptosteel-Kapseln der Fall ist);
- Der USB-Stick, der den Portfolio-Deskriptor enthält;
- Ein Papier-Backup des Deskriptors für den Fall einer Fehlfunktion oder Beschädigung des USB-Sticks (dieses Backup wurde hier nicht fotografiert);
- Ein Nachfolgeschreiben, in dem die Schritte beschrieben werden, die zur Rückforderung der Gelder unternommen werden sollen.

![Éléments de récupération](assets/fr/18.webp)

Und wir haben diese Gegenstände versiegelt!

![Sachet scellé récupération](assets/fr/19.webp)

## Erhalt von Geldern

Auf dem Hauptbildschirm von Liana werden Ihr Saldo und die mit Ihrem Portfolio verbundenen Transaktionen (vergangene und aktuelle) angezeigt. In unserem Fall ist der Saldo Null, was normal ist.

![Écran principal](assets/fr/20.webp)

Um Geld zu erhalten, gehen Sie auf die Registerkarte "*Empfang*" und klicken Sie auf "*Adresse generieren*". Auf Ihrem Bildschirm sollte eine neue Adresse erscheinen. Sie ist länger als bei herkömmlichen Portfolios: Es handelt sich um eine Adresse, die mit einem eigenständigen Vertrag (P2WSH oder Taproot) verbunden ist.

![Générer nouvelle adresse](assets/fr/21.webp)

Sie müssen diese Adresse auf Ihrem Hardware-Portfolio verifizieren, indem Sie auf "*Auf Hardware-Gerät verifizieren*" klicken.

![Vérifier adresse portefeuille matériel](assets/fr/22.webp)

Sobald das Geld gesendet wurde, erscheint die Transaktion auf dem Hauptbildschirm (zuerst als unbestätigt, dann als bestätigt). Für diesen Test haben wir 50.000 Satoshis (etwas mehr als 50 $ zum Zeitpunkt der Überweisung) gesendet. Es versteht sich von selbst, dass der in Ihrem Fall überwiesene Betrag aufgrund der Transaktionsgebühren um eine Größenordnung höher sein muss als dieser Wert.

![Vérifier solde](assets/fr/23.webp)

Sie können den Verfallsstatus Ihres Guthabens überprüfen, indem Sie auf die Registerkarte "*Münzen*" gehen. Diese Registerkarte zeigt Ihnen die verschiedenen Münzen (UTXO) in Ihrer Geldbörse an. Hier können wir sehen, dass die 50.000 Satoshis Münze, die durch unsere Transaktion erstellt wurde, am selben Tag (in einer Stunde) abläuft.

![Obtenir informations pièce](assets/fr/24.webp)

Um das in Bitcoin verwendete UTXO-Darstellungsmodell besser zu verstehen, können Sie den ersten Teil des von Loïc Morel geschriebenen Kurses über Vertraulichkeit in Bitcoin lesen:

https://planb.network/courses/btc204
## Laufende Ausgaben

Laufende Ausgaben sind der Normalfall für die Nutzung von Liana. Das Versenden von Bitcoins mit dem Master Key funktioniert wie bei allen klassischen Bitcoin-Wallets wie Electrum oder Sparrow.

Um eine Gebühr zu erheben, gehen Sie auf die Registerkarte "*Senden*" und geben Sie die wichtigsten Informationen ein: die BTC-Adresse des Empfängers, den zu sendenden Betrag und den gewünschten Gebührensatz. Sie können auch eine (lokal gespeicherte) Beschreibung hinzufügen, damit Sie es sich bequem machen können. In unserem Beispiel haben wir 10.000 Satoshis an einen bestimmten Bob geschickt, mit einer Gebühr von 4 Sat/ov, oder $0,67 zum Zeitpunkt der Transaktion.

Liana bietet auch eine "Münzkontrolle": Sie geben an, welche Münze (UTXO) Sie ausgeben möchten. Hier haben wir uns für die zuvor erstellte 50.000-Satoschis-Münze entschieden.

![Envoyer fonds clé principale](assets/fr/25.webp)

Unterschreiben Sie dann die Transaktion mit Ihrem Signaturgerät, das mit dem Hauptschlüssel verbunden ist, indem Sie auf "*Sign*" klicken. Sie müssen die Transaktion auf Ihrer Hardware-Wallet verifizieren und bestätigen. Hier haben wir den Nano S Plus zum Signieren der Transaktion verwendet.

![Signer transaction clé principale](assets/fr/26.webp)

Zum Schluss senden Sie die Transaktion über das Netzwerk, indem Sie auf "*Broadcast*" klicken. Beachten Sie, dass das Senden von Geldmitteln die Wiederherstellungszeit für verwendete Münzen zurücksetzt.

![Diffuser transaction clé principale](assets/fr/27.webp)

Die Transaktion wird auf dem Hauptbildschirm angezeigt und Ihr Saldo wird aktualisiert.

![Solde après dépense](assets/fr/28.webp)

## Aktualisierung des Portfolios

Wie oben erläutert, erfordert die Liana-Brieftasche, dass Sie Ihr Guthaben regelmäßig aktualisieren, indem Sie eine Transaktion auf der Blockchain durchführen. Wenn Sie dies nicht tun, kann Ihr Guthaben von Ihrem Erben (oder von Ihrem zweiten Gerät im Falle eines erweiterten Backups) wiederhergestellt werden. Diese Situation ist nicht extrem gefährlich, aber sie untergräbt den Zweck der Einrichtung dieses Mechanismus: die Kontrolle über Ihre Bitcoins zu behalten, ohne auf eine vertrauenswürdige dritte Partei zurückgreifen zu müssen, während Sie von einem Sicherheitsnetz profitieren.

Bevor Ihr Guthaben (oder ein Teil davon) abläuft und durch den Wiederherstellungsschlüssel ausgegeben werden kann, wird eine Warnung angezeigt. Sie weist darauf hin, dass Ihr "Wiederherstellungspfad" (*Wiederherstellungspfad*) bald verfügbar sein wird. Angesichts der Kürze unserer Wiederherstellungszeit (eine Stunde) wird diese Meldung in unserem Fall direkt angezeigt.

![Avertissement chemin récupération](assets/fr/29.webp)

Wenn die Frist abläuft, erscheint eine Schaltfläche, die Sie auffordert, die betreffenden Mittel zu aktualisieren.

![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)

Um Ihre Münzen zu aktualisieren, gehen Sie auf die Registerkarte "*Münzen*" und klicken Sie auf "*Münze aktualisieren*" in dem entsprechenden Münzfeld. Wenn Sie mehrere Münzen haben, sollten Sie sie aus Gründen der Vertraulichkeit einzeln und in relativ kurzen Abständen aktualisieren. Um die Kosten niedrig zu halten, können Sie Ihre Gelder konsolidieren, indem Sie das gesamte Portfolio an eine neue Empfangsadresse senden, was jedoch Ihre Vertraulichkeit beeinträchtigt.

![Actualiser pièce](assets/fr/31.webp)

Geben Sie den gewünschten Gebührensatz für die Transaktion an. Da es sich um eine Überweisung an Sie selbst handelt, können Sie einen relativ niedrigen Gebührensatz festlegen, vor allem, wenn Sie die Überweisung einige Tage vor Ablauf der Frist vornehmen.

![Transfert à soi-même](assets/fr/32.webp)

Die Transaktion (mit der Bezeichnung "*Selbstüberweisung*") wird nur auf der Registerkarte "*Transaktionen*" angezeigt.

![Transactions après auto-transfert](assets/fr/33.webp)

Einmal bestätigt, ist Ihre Münze sicher! Sie können bis zum nächsten Verfallsdatum beruhigt sein.

## Bitcoin-Erholung

Wenn Sie Gelder aus dem Liana-Portfolio wiederherstellen wollen, können Sie sich in zwei Situationen befinden. Sie können Zugang zu dem Computer haben, auf dem die Software installiert ist. In diesem Fall müssen Sie sie nur öffnen (was im Falle des erweiterten Backup-Modells geschieht). Es kann aber auch sein, dass Sie keinen Zugang zu diesem Computer haben, dann fangen wir hier ganz von vorne an. Beachten Sie, dass das Wiederherstellungsverfahren in beiden Fällen das gleiche ist.

Um loszulegen, laden Sie Liana von [der offiziellen Wizardsardine-Website] (https://wizardsardine.com/liana/) oder von [dem GitHub-Repository] (https://github.com/wizardsardine/liana/releases) herunter, wo Sie die Echtheit der Software überprüfen können. Installieren Sie die Software und führen Sie sie aus. Die in unserem Fall verwendete Version ist 0.9, daher kann sich das Erscheinungsbild geändert haben. Wählen Sie auf dem Willkommensbildschirm die Option "Add an existing Liana wallet".

![Ajouter portefeuille existant](assets/fr/34.webp)

Konfigurieren Sie, wie Sie sich mit dem Netzwerk verbinden wollen. Sie können entweder Ihren eigenen Knoten (lokal oder remote) oder die Infrastruktur von WizardSardine nutzen. Im letzteren Fall benötigen Sie die vom Portfolioersteller verwendete E-Mail-Adresse, damit die Fonds automatisch gefunden werden können. Wenn Sie diese Informationen nicht haben, wählen Sie die erste Option.

![Sélectionner connexion réseau](assets/fr/35.webp)

Wenn Sie Ihren eigenen Knoten verwenden, importieren Sie den Portfolio-Deskriptor. Dabei handelt es sich um eine technische Beschreibung des Kontos, die es Ihnen ermöglicht, die darin enthaltenen Mittel abzurufen. In unserem Fall handelt es sich um die folgenden Informationen:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

![Importer descripteur](assets/fr/36.webp)

Liana fordert Sie dann auf, eine mnemonische Phrase einzugeben. Wenn Sie ein funktionierendes Signaturgerät (Hardware-Geldbörse) haben, können Sie diesen Teil überspringen. Wenn Ihr Gerät fehlt oder beschädigt ist, Sie aber die entsprechenden 12 oder 24 Wörter haben, können Sie diese Option trotzdem nutzen. Um auf Nummer sicher zu gehen (wenn die wiederherzustellende Menge hoch ist), empfehlen wir Ihnen dennoch, sich eine neue Hardware-Geldbörse zu besorgen und die Mnemonik zu verwenden, um die Schlüssel darauf wiederherzustellen.

In unserem Fall verwenden wir die Blockstream Jade Hardware Wallet als Wiederherstellungsgerät und entscheiden uns, diesen Schritt zu überspringen ("*Skip*").

![Passer phrase mnémotechnique](assets/fr/37.webp)

Prüfen und speichern Sie den Deskriptor in Ihrem Signaturgerät, indem Sie ihn auf dem Bildschirm auswählen. Wenn Ihre Hardware-Geldbörse nicht angezeigt wird, überprüfen Sie, ob sie angeschlossen und entsperrt ist. Prüfen und bestätigen Sie, dass diese Informationen zu Ihrem Gerät hinzugefügt wurden.

![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)

Konfigurieren Sie Ihren Knoten. Sie können einen vorhandenen Knoten verwenden oder einen *pruned node* auf Ihrem Rechner installieren. In unserem Fall haben wir einen bestehenden Knoten verwendet.

![Choisir type de nœud](assets/fr/39.webp)

Für dieses Tutorial haben wir einen öffentlichen Electrum-Server verwendet. Dieser hatte jedoch Zugriff auf alle unsere Aktivitäten mit der Liana-Brieftasche. Wenn Sie Ihre Privatsphäre schützen wollen, sollten Sie besser Ihren eigenen Node verwenden.

![Connexion serveur Electrum public](assets/fr/17.webp)

Sobald Sie Ihren Knotenpunkt eingerichtet haben, gelangen Sie zum Hauptbildschirm der Brieftasche, wo Sie den Kontostand und frühere Transaktionen, die mit dem Konto verknüpft sind, einsehen können. Sie können auch sehen, ob Gelder abgerufen werden können. Hier sehen wir, dass eine Münze abgerufen werden kann.

![Accueil Liana récupération](assets/fr/40.webp)

Um die Mittel im Portfolio wiederherzustellen, gehen Sie zu den Einstellungen ("*Einstellungen*") unten links und klicken Sie auf "*Wiederherstellung*".

![Récupération dans paramètres](assets/fr/41.webp)

Geben Sie den Coin in der Wallet aus, indem Sie das entsprechende Feld ankreuzen. Geben Sie die BTC-Adresse an, an die Sie das Geld senden möchten, sowie die Transaktionsgebühr. Klicken Sie dann auf "*Weiter*".

![Récupération des pièces](assets/fr/42.webp)

Signieren Sie die Transaktion, indem Sie auf "*Sign*" klicken und die Transaktion in Ihrer Hardware-Wallet validieren.

![Signer transaction clé de récupération](assets/fr/43.webp)

Dann senden Sie es über das Netzwerk, indem Sie auf "*Broadcast*" klicken.

![Diffuser transaction clé de récupération](assets/fr/44.webp)

Die Transaktion sollte auf dem Hauptbildschirm erscheinen. Sobald dies bestätigt ist, ist die Wiederherstellung abgeschlossen!

![Écran principal après récupération](assets/fr/45.webp)

## Videos

Wenn Sie mehr über Liana erfahren möchten, finden Sie hier einige Videos, die Ihnen eine bessere Vorstellung von der Funktionsweise vermitteln. Hier ist eine Video-Präsentation von Liana mit Kévin Loaec und Antoine Poinsot:

![Vidéo de présentation avec Kévin Loaec et Antoine Poinsot](https://youtu.be/siuLmQo1lM8)

Und hier ist eine Anleitung zur Verwendung von Liana, mit Antoine Poinsot:

![Vidéo-tutoriel avec Antoine Poinsot](https://youtu.be/JrG4WMVPZDQ)

Die dort gezeigten Manipulationen ähneln denen, die in diesem Lernprogramm vorgestellt werden.

## Bonus: Deskriptoranalyse

Der Deskriptor ist eine vom Menschen lesbare Zeichenkette, die eine Reihe von Adressen erschöpfend beschreibt. Er fasst eine Reihe wesentlicher Informationen zusammen, um die Teile (UTXO) eines erweiterten Portfolios abzurufen. Die Art und Weise, wie der Deskriptor geschrieben wird, basiert auf [Miniscript syntax] (https://bitbox.swiss/blog/understanding-bitcoin-miniscript-part-2/), der von Andrew Poelstra, Pieter Wuille und Sanket Kanjalkar im Jahr 2019 entwickelten Skriptsprache.

Um besser zu verstehen, warum diese Zeichenkette wichtig ist, lassen Sie uns den Deskriptor in unserem Beispiel analysieren, der lautet :

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Diesem Deskriptor können die folgenden Informationen entnommen werden:


- wsh" (kurz für *witness script hash*): Dies ist die Art der erstellten Transaktionsausgabe. Hätten wir uns für Taproot entschieden, wäre der Bezeichner "tr" gewesen.
- oder_d": Dies ist ein logischer Operator, der angibt, dass *eine der beiden folgenden* Bedingungen erfüllt sein muss, damit die Ausgabe akzeptiert wird (das "d" steht für eine bestimmte Syntax).
- pk" (kurz für *öffentlicher Schlüssel*): Dieser Operator prüft eine gegebene Signatur gegen den folgenden öffentlichen Schlüssel und gibt die Antwort als Booleschen Wert (TRUE oder FALSE) aus.
- `[3689a8e7/48'/0'/0'/2']`: Dieses Element enthält den *Fingerprint* des Hauptschlüssels für die Haupt-Hardware-Wallet (in diesem Fall der Nano S Plus) und den Ableitungspfad zum verknüpften erweiterten privaten Schlüssel (von dem alle anderen privaten Schlüssel abgeleitet werden).
- `xpub6FKY ... WQa`: Dies ist der erweiterte öffentliche Schlüssel, der mit dem Haupt-Hardware-Portfolio (hier der Nano S Plus) verknüpft ist
- `/<0;1>/*`: Dies sind die Ableitungspfade für den Erhalt einfacher Schlüssel und Adressen: `0` für den Empfang, `1` für interne Operationen (*Änderung*), mit einem "Platzhalter" (`*`), der die sequentielle Ableitung mehrerer Adressen auf konfigurierbare Weise ermöglicht, ähnlich dem "Gap-Limit"-Management klassischer Portfolio-Software.
- und_v": Dies ist ein logischer Operator, der angibt, dass *die folgenden zwei* Bedingungen erfüllt sein müssen, damit die Ausgabe akzeptiert wird (das `_v` weist auf eine bestimmte Syntax hin).
- `v:pkh` (kurz für *verify: public key hash*): Dieser Operator verifiziert eine gegebene Signatur und einen öffentlichen Schlüssel gegen den folgenden Hash des öffentlichen Schlüssels (*hash*). Dies ist im Wesentlichen die gleiche Prüfung wie bei P2PKH- und P2WPKH-Skripten.
- `[42e629dd/48'/0'/0'/2']`: Dies ist das gleiche Element wie oben (bestehend aus der Spur und dem Ableitungspfad), außer dass die Spur des Hauptschlüssels des Hardware-Wiederherstellungsportfolios (in diesem Fall die Jade) angegeben wird.
- `xpub6DpQ ... WQd": Dies ist der erweiterte öffentliche Schlüssel, der mit der Hardware-Wiederherstellungs-Brieftasche (hier die Jade) verknüpft ist.
- `older(6)` : Dieser Operator prüft, ob die erstellte Transaktionsausgabe ein Alter von mehr als 6 Blöcken haben muss, um ausgegeben werden zu können.

Das letzte Datenelement (`8alrve5h`) ist die Prüfsumme des Deskriptors und entspricht der Portfolio-Kennung.

Die von diesem Portfolio erstellten Skripte haben die folgende Form:

```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```

Da die Sicherheit Ihrer Bitcoin-Wallet auch davon abhängt, dass Sie verstehen, wie sie funktioniert, schlage ich vor, dass Sie die Mechanismen von deterministischen und hierarchischen Wallets in diesem kostenlosen Trainingskurs auf Plan ₿ Network eingehend studieren:

https://planb.network/courses/cyp201