---
name: Nunchuk
description: Wallet mobil für alle geeignet
---
![cover](assets/cover.webp)



## Ein leistungsstarker Wallet


Nunchuk kam Ende 2020 mit einer klaren Philosophie auf den Markt: Multi-Signatur soll zum Standard werden. Es wurde daher so konzipiert, dass es sehr fortschrittliche Funktionen ausführen kann, wobei die wertvolle Entscheidung getroffen wurde, das Design direkt auf Bitcoin Core aufzubauen, der Referenzsoftware für das Bitcoin-Ökosystem.



Nach mehr als 4 Jahren der Entwicklung und Nutzung ist es nun bereit, in großem Umfang ausprobiert zu werden. Wenn Sie ein Anfänger sind und mit dem Nunchuk nicht vertraut sind, wird Ihnen diese Anleitung helfen, die ersten Schritte zu machen und diese Software zu entdecken, deren fortgeschrittene Funktionen Sie kennenlernen können, nachdem Sie den ersten Schlag überwunden haben. Die Anleitung selbst richtet sich an fortgeschrittene Benutzer, die über die notwendigen Fähigkeiten verfügen, um alle Schritte zu befolgen, aber sie kann für jeden eine Inspiration sein, um herauszufinden, wie man seine Fähigkeiten verbessern kann. Wir werden mit der mobilen Version beginnen, und dieser Hinweis ist notwendig, da Nunchuk die Software auch für den Computer hat.



## Herunterladen


Der erste Schritt ist definitiv die Entscheidung, wo Sie die App herunterladen können. Gehen Sie auf die [offizielle Website] (https://nunchuk.io/), wo Sie einige Dokumentationen (nicht viel, aber ein Anfang), die Präsentation der Funktionen und am Ende der Seite alle Download-Links finden.



📌 In diesem Tutorial zeige ich euch, wie ihr Software Wallet aus dem Github-Repository herunterladet und wie ihr die Version vor der Installation auf eurem Handy überprüft. **Die folgende Prozedur kann nur von deinem Computer aus durchgeführt werden, daher empfehle ich dir, all diese Schritte von deinem Desktop oder Laptop aus zu machen und - nach allen Überprüfungen - die `.apk` Datei auf dein Handy zu übertragen.**



![image](assets/en/01.webp)



Wenn Ihre Kenntnisse noch nicht sehr weit fortgeschritten sind, können Sie die `.apk` aus den offiziellen Stores herunterladen und direkt zum Konfigurationsteil dieses Tutorials übergehen. Wenn Sie hingegen den Sprung wagen wollen, folgen Sie Schritt für Schritt weiter.



Klicken Sie also von Ihrem Desktop-Computer aus auf _Besuchen Sie unser Open-Source-Repository_



Der Link führt Sie zu Nunchuks Github-Seite, wo Sie eine Reihe von Repos finden. Wir konzentrieren uns auf das _nunchuk-android_ Repository



![image](assets/en/02.webp)



Auf dem nächsten Bildschirm suchen Sie rechts den Abschnitt _Releases_ und wählen _Latest_



![image](assets/en/03.webp)



Laden Sie unter _Assets_ die Version (in diesem Beispiel 1.67.apk) herunter, zusammen mit der SHA256SUMS-Datei und SHA256SUMS.asc.



![image](assets/en/04.webp)



Um den GPG-Schlüssel des Entwicklers zu finden, gehen Sie zurück zum Abschnitt _Releases_ des Repositorys und suchen Sie nach 1.9.53 (oder früher), die den Link zum Erhalt und Download des _GPG-Schlüssels_ enthält



![image](assets/en/05.webp)



Wir werden die Überprüfung mit einem praktischen Tool von Sparrow wallet durchführen, das ein eigenes Fenster für diesen Zweck hat und PGP-Signaturen und SHA256-Manifeste unterstützt.



Starten Sie dann Sparrow und wählen Sie im Menü _Tools_ die Option _Download überprüfen_.



![image](assets/en/06.webp)



In dem sich öffnenden Fenster finden Sie Felder zum "Ausfüllen": Wählen Sie die Schaltfläche _Browse_ auf der rechten Seite und wählen Sie für jedes Feld die entsprechenden Dateien aus, die Sie gerade von Github heruntergeladen haben. Wenn Sie alle Schritte abgeschlossen haben, sieht das Fenster wie folgt aus, mit Green Häkchen und Hash Bestätigung des Manifests.



![image](assets/en/07.webp)


**Anmerkung: Der Screenshot stammt von einem Windows-PC. Die gleiche Vorgehensweise kann für jedes Betriebssystem auf Ihrem Computer verwendet werden, Sie müssen nur Sparrow wallet installiert haben. Und verifiziert!**



Sie können den Leitfaden zu Sparrow wallet finden, um diesen Software Wallet herunterzuladen


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Sie können dann die "apk"-Datei von Ihrem Computer auf Ihr Handy übertragen



![image](assets/en/08.webp)



und installieren Sie Nunchuk



![image](assets/en/09.webp)



Bevor du Nunchuk auf deinem Handy startest, öffne Orbot und setze den Neuling in die Liste der Apps, die unter Tor geroutet werden sollen.



![image](assets/en/11.webp)



Starten Sie nun Nunchuk. Für Projektfunktionen - die nicht Gegenstand dieses Tutorials sind - wird Nunchuk Sie nach dem Öffnen auffordern, sich über eine E-Mail oder ein Google-Profil anzumelden. Solange Sie nicht vorhaben, die Vorteile der erweiterten Pläne von Nunchuk Inc. zu nutzen, **vermeiden Sie die Anmeldung** und wählen Sie die Option _Als Gast fortfahren_.



![image](assets/en/12.webp)



## Einstellungen


Nunchuk präsentiert sich mit einem _Home_-Fenster, in dem man seine Bedienphilosophie leicht nachvollziehen kann und auf die wir gleich noch näher eingehen werden.



Unten finden Sie die Menüs, und als ersten Schritt wählen Sie _Profil_, um auf die Einstellungen zuzugreifen.



![image](assets/en/10.webp)



Wählen Sie dann _Anzeigeeinstellungen_ und ignorieren Sie weiterhin die Aufforderung, ein Konto zu erstellen.



![image](assets/en/14.webp)



Auf dem unten stehenden Bildschirm können Sie überprüfen, ob Wallet online ist und Sie Ihren Server verbinden können. Beachten Sie dabei die Anweisungen auf dem Link, der durch Klicken auf _diese Anleitung_ angeboten wird.



![image](assets/en/15.webp)



Speichern Sie die Einstellungen mit dem Befehl _Netzwerkeinstellungen speichern_, kehren Sie zum Menü _Profil_ zurück und wählen Sie _Sicherheitseinstellungen_.



![image](assets/en/16.webp)



In diesem Menü legen Sie fest, wie das Öffnen der App geschützt werden soll. Um unerwünschten Zugriff zu verhindern, können Sie Nunchuk mit der Biometrie des Telefons schützen und/oder eine Sicherheits-PIN hinzufügen.



![image](assets/en/17.webp)



Werfen Sie auch einen Blick auf das Menü _About_, das Sie immer im Fenster _Profil_ finden



![image](assets/en/18.webp)



die es Ihnen ermöglicht, die Version der App zu überprüfen oder bei Bedarf die Entwickler zu kontaktieren.



![image](assets/en/19.webp)



## Schlüsselerzeugung und Wallet


Wie aus der Philosophie von Nunchuk leicht zu erraten ist, ist die Software als nützliches Werkzeug für die Verwaltung von Geldbörsen mit mehreren Signaturen gedacht. Um diese Funktion auszuführen, ermöglicht Nunchuk die Erstellung von Wallet, indem es sie von den Schlüsseln trennt, die zum Anordnen digitaler Signaturen benötigt werden.



Die ideale Funktionsweise des Nunchuk beinhaltet die Erstellung von Geldbörsen, die nur beobachtet werden können, abhängig von Tasten, die "Colds" sein können



Auf den vorherigen Bildschirmen haben Sie vielleicht bemerkt, dass es unten ein Menü namens _Tasten_ gibt. Wenn Sie das Nunchuk gerade heruntergeladen haben, sehen Sie sowohl in _Home_ als auch in _Tasten_ eine große Schaltfläche, die Sie einlädt, eine Taste hinzuzufügen: _Taste hinzufügen_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**So funktioniert das Nunchuk:** Zuerst importieren Sie den generate, dann erstellen Sie den Wallet und konfigurieren ihn so, dass er die Schlüssel auswählt, die zum Entsperren der darauf gespeicherten Gelder berechtigen.



Auch beim Wallet singlesig erstellen Sie zuerst den Schlüssel und erst dann den Wallet. Und genau das werden wir jetzt tun. Wir beginnen mit einem Wallet singlesig, um das Eis zu brechen und die Funktionen des Nunchuk zu entdecken.



Klicken Sie auf _Schlüssel hinzufügen_



![image](assets/en/22.webp)



Nunchuk zeigt eine Reihe von unterstützten Signaturgeräten an, aber um zu beginnen, wählen Sie _Software_.



![image](assets/en/23.webp)



Nunchuk wird generate ein Mnemonic, das auf dem Gerät gespeichert wird. Sie müssen dann die Reihenfolge der Wörter für die Sicherung aufschreiben, die besten Umgebungsbedingungen schaffen und sicherstellen, dass Sie die Zeit haben, es gut und leise zu tun. Die Software zeigt das Mnemonic nur einmal an, unabhängig davon, ob Sie es jetzt oder später anzeigen lassen wollen, also wählen Sie _Jetzt erstellen und sichern_.



![image](assets/en/24.webp)



Das Nunchuk erzeugt Mnemonic-Sätze mit 24 Wörtern, die sofort auf dem nächsten Bildschirm erscheinen



![image](assets/en/25.webp)



und führte dann eine kurze Überprüfung durch, bei der Sie aufgefordert wurden, das richtige Wort aus 3 Möglichkeiten auszuwählen, das der Nummer in der Mnemonic-Sequenz entspricht.


Wenn Sie das Mnemonic richtig geschrieben haben, wird die Schaltfläche _Fortfahren_ aktiviert. Drücken Sie sie, um fortzufahren.



![image](assets/en/26.webp)



Benennen Sie Ihren Schlüssel und drücken Sie _Fortfahren_.



![image](assets/en/27.webp)



Am Ende dieser Schritte werden Sie gefragt, ob Sie einen [passphrase](https://planb.network/en/resources/glossary/passphrase-bip39) zu Ihrem Mnemonic-Satz hinzufügen möchten. Wenn Sie nicht wissen, wie man passphrase benutzt, wie man es sichert oder wie es funktioniert, empfehle ich Ihnen, _Ich brauche keine Passphrase_ zu wählen.



![image](assets/en/28.webp)



Der Schlüssel ist nun erstellt und wird Ihnen im Menü angezeigt:




- Mit _Key Spec_ wird der Master-Fingerprint angezeigt
- Sie haben Einstellungen, die drei Punkte oben rechts, wo Sie den Schlüssel löschen oder eine Nachricht signieren können
- Neben dem Namen des Schlüssels finden Sie ein Federsymbol, auf das Sie klicken können, um den Namen des Schlüssels zu bearbeiten, z. B. um Ihre Schlüssel in Zukunft zu ordnen.
- Als letzten Befehl können Sie den Gesundheitszustand des Schlüssels überprüfen: Durch Drücken von _Run health check_ können Sie die App überprüfen lassen, ob ein Schlüssel kompromittiert ist.



Wenn Sie fertig sind, klicken Sie auf _Done_



![image](assets/en/29.webp)



Im Menü _Tasten_ sehen Sie Ihre erste Taste erscheinen.



![image](assets/en/30.webp)



Im Menü _Home_ erscheint die Option zum Erstellen von Wallet. Klicken Sie auf _Neue Brieftasche erstellen_.



![image](assets/en/31.webp)



Nunchuk zeigt Ihnen eine Reihe von Möglichkeiten, die größtenteils mit den Dienstleistungen des Unternehmens zu tun haben, die nicht Gegenstand dieses Tutorials sind.



In diesem Leitfaden werden wir eine _Hot Wallet und eine _Benutzerdefinierte Brieftasche_ erstellen, indem wir die Details erläutern.


Beginnen wir mit _Custom wallet_.



![image](assets/en/32.webp)



Die App fordert Sie auf einfache Weise auf, dieses neue Wallet zu benennen und das Skript für die Adressen auszuwählen. Für das Lernprogramm habe ich die Standardeinstellung _Native segwit_ gewählt. Wenn Sie fertig sind, wählen Sie _Fortfahren_



![image](assets/en/33.webp)



In der Konfiguration des Wallet werden Sie aufgefordert, einzustellen, mit welchem Schlüssel die Mittel dieses Wallet aufgeschlossen werden sollen. Sollte es mehrere Schlüssel geben, wird eine Liste angezeigt, aus der Sie wählen können. Da wir im Moment nur einen Schlüssel erstellt haben, setzen wir ein Häkchen bei diesem Schlüssel. In der unteren rechten Ecke können Sie sehen, wie Nunchuk Sie auffordert, Ihre zukünftigen Wallet-Mehrfachsignaturen einzurichten, wodurch sich die Anzahl der _erforderlichen Schlüssel_ erhöht.



![image](assets/en/34.webp)



Da wir eine Einzelsig erstellen, lassen wir `1` stehen und klicken auf _Weiter_.



Zuletzt wird ein Verifizierungsbildschirm angezeigt, auf dem Sie die Funktionen des Wallet überprüfen können:




- der Name
- die "1/1 Multisig"-Stufe, wie Nunchuk die Wallet-Single-Stufe nennt
- den Skripttyp, "Native SegWit"
- den Schlüssel "Keys" mit seinem Fingerabdruck und seinem Ableitungspfad



Wenn Sie zufrieden sind, drücken Sie auf _Brieftasche erstellen_



![image](assets/en/35.webp)



Wallet wurde erstellt und Sie können die [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) Datei als Backup herunterladen. Um zum Hauptmenü zurückzukehren, klicken Sie auf den Pfeil in der oberen linken Ecke.



![image](assets/en/36.webp)



Sie befinden sich in _Home_, wo Sie das neu erstellte Wallet sehen, das den Kontostand und den Status der Verbindung anzeigt. Wenn Sie auf die blaue Fläche klicken, können Sie auf die Hauptfunktionen von Wallet zugreifen.



![image](assets/en/37.webp)





- Über das Linsensymbol in der oberen rechten Ecke können Sie eine Transaktionssuche durchführen;
- gW-35-Konfiguration anzeigen" ermöglicht den Zugriff auf das Konfigurationsmenü, in dem Sie den Namen des Wallet bearbeiten und die erweiterten Optionen oben rechts aktivieren können (von denen Sie keine Bildschirmfotos erhalten können). Hier können Sie die Wallet-Konfiguration exportieren, Beschriftungen vornehmen, Tasten ersetzen, die [Lückengrenze] (https://planb.network/en/resources/glossary/gap-limit) ändern und mehr.



## Transaktionen mit Nunchuk



Auszeichnungen _Empfangen_



![image](assets/en/38.webp)



Die App ist so programmiert, dass sie den QR-Code des Address anzeigt oder den scriptPubKey kopiert/teilt, um Onchain-Gelder zu erhalten.



![image](assets/en/39.webp)



Auf diesem ersten Address kam ein UTXO an,



![image](assets/en/40.webp)



aber wir klicken trotzdem auf _Empfangen_, um eine weitere zu erhalten.



![image](assets/en/41.webp)



Sie sollen herausfinden, dass Nunchuk Ihnen diese neue Address als _unbenutzte Adresse_ meldet, Ihnen aber auch anzeigt, dass Sie _benutzte Adressen_ und deren Anzahl haben.



### Ausgabentransaktion mit Münzkontrolle



Wenn auch dieses zweite UTXO eingetroffen ist, kehren Sie zum Hauptbildschirm des Wallet zurück, um den Status der beiden eingehenden Transaktionen zu überprüfen, und klicken Sie vor allem auf die Option _Münzen anzeigen_



![image](assets/en/42.webp)



wo Ihnen die einzelnen UTXOs angezeigt werden. Hier können Sie sich einen bestimmten Betrag anzeigen lassen, indem Sie auf den kleinen Pfeil neben dem Betrag klicken



![image](assets/en/43.webp)



und überprüfen Sie, wann es angekommen ist, die Beschreibung, Block UTXO, so dass es nicht ausgegeben wird und mehr.



![image](assets/en/44.webp)



Wenn du aber zum Menü _Münzen_ zurückgehst, indem du auf den Pfeil in der oberen rechten Ecke klickst, kannst du "Münzkontrolle" einschalten, um deine UTXOs kontrollierter auszugeben.



Im folgenden Beispiel habe ich UTXO von 21.000 Sats ausgewählt und dann auf das Symbol in der unteren linken Ecke geklickt.



![image](assets/en/45.webp)



Nunchuk öffnet automatisch das Fenster _Neue Transaktion_, um diesen UTXO auszugeben. In der Ausgabetransaktion müssen Sie zunächst den Betrag manuell eingeben oder _Alles senden_ wählen, um das gesamte Münzkontrollguthaben zu senden, ohne Reste zu erzeugen. Sobald der Betrag festgelegt ist, wählen Sie _Fortfahren_



![image](assets/en/46.webp)



Jetzt zeigt Nunchuk an, wo der Address eingefügt werden muss, auf den diese Gelder überwiesen werden sollen, und gibt eine Beschreibung an, um die Transaktion abzuschließen.



![image](assets/en/47.webp)



Wenn Sie _Transaktion erstellen_ wählen, wird die automatische Gebühren- und Transaktionsverwaltung an die App delegiert. Ich empfehle, _Benutzerdefinierte Transaktion_ für mehr Kontrolle zu wählen.



In diesem neuen Bildschirm ist es wichtig, Folgendes auszuwählen




- _Gebühr vom Sendebetrag abziehen_, um zu verhindern, dass die Gebühren von einem anderen UTXO in Wallet gezahlt werden, der sie ausgibt und einen Restbetrag erzeugt (was ein vermeidbarer Verlust an Privatsphäre ist);
- und legen Sie die Gebühren nach der Überprüfung im Explorer manuell fest.



Wenn Sie alle diese Schritte durchgeführt haben, klicken Sie auf _Fortfahren_



![image](assets/en/48.webp)



Der nächste Bildschirm ist die vollständige Zusammenfassung der Transaktion. Wenn alles in Ordnung ist, bestätigen Sie, indem Sie _Bestätigen und Transaktion erstellen_ wählen.



![image](assets/en/49.webp)



Mit _Ausstehende Unterschriften_ macht Nunchuk Sie darauf aufmerksam, dass die Transaktion auf Ihre Unterschrift zur Genehmigung der Ausgabe wartet, die Sie durch Klicken auf _Unterschreiben_ anbringen.



![image](assets/en/50.webp)



Der Befehl _Broadcast_ erscheint unten, um die abgeschlossene und signierte Transaktion zu verbreiten.



![image](assets/en/51.webp)



### Ausgabentransaktion aus dem Menü _Senden_



Während wir auf der Hauptseite von Wallet sehen, wie die Transaktion ausgeführt wird und auf die Bestätigung wartet, verwenden wir das Menü _Senden_, um eine tägliche Ausgabe zu simulieren.



![image](assets/en/52.webp)



Wenn Sie auf _Senden_ klicken, wird der Bildschirm für das Senden der Transaktion angezeigt, der mit dem soeben gezeigten Bildschirm identisch ist, jedoch ohne die Münzkontrolle zu durchlaufen.



Auch in diesem zweiten Beispiel habe ich mich für _Benutzerdefinierte Transaktion_ entschieden und den gesamten Betrag gesendet, aber ich hätte ihn auch manuell einstellen können. Sobald Sie sich für einen Betrag entschieden haben, drücken Sie auf _Fortfahren_.



![image](assets/en/53.webp)



Dann entscheiden Sie immer, ob die Gebühren von der betreffenden UTXO abgezogen werden (in diesem Beispiel ist die Wahl erzwungen, weil es nur eine gibt), passen Sie die Gebühren manuell an die aktuelle Situation in Mempool an und drücken Sie _Fortfahren_.



![image](assets/en/54.webp)



Wenn das Übersichtsbild zufriedenstellend ist, wählen Sie _Bestätigen und Transaktion anlegen_.



![image](assets/en/55.webp)



Unterschreiben Sie die Transaktion mit _Sign_



![image](assets/en/56.webp)



und verbreiten sie im Netz.



![image](assets/en/57.webp)



Wallet befindet sich an diesem Punkt mit einem Saldo von Null und einer Aktualisierung der Historie.



![image](assets/en/58.webp)



## Schaffung eines "Hot Wallet"



Um nichts aus der Anfangsphase von Nunchuk mobile auszulassen, wollen wir sehen, wie die App "Hot Wallet" erstellt



Im _Home_ Menü des Nunchuk, wo die Liste der Geldbörsen erscheint, klicken Sie auf das "+" in der oberen rechten Ecke.



![image](assets/en/59.webp)



Wählen Sie _Hot wallet_ aus den Optionen



![image](assets/en/60.webp)



Nunchuk gibt auf der Präsentationsseite einige Ratschläge zum Umgang mit Hot-Geldbörsen. Wählen Sie _Fortfahren_, um fortzufahren.



![image](assets/en/61.webp)



Nach ein paar Augenblicken ist das Wallet erstellt und erscheint in der Liste in bräunlicher Farbe. Dies ist die Farbe, mit der das Nunchuk Sie darauf hinweist, dass Sie das Wallet noch nicht gesichert haben.



![image](assets/en/62.webp)



Klicken Sie auf den Namen des Wallet, um auf seine Konfigurationen zuzugreifen, und Sie werden möglicherweise eine Aufforderung sehen, den Mnemonic-Satz sofort zu sichern.



![image](assets/en/63.webp)



Die Prozedur ist dieselbe, die wir schon einmal gesehen haben, also werden wir sie nicht noch einmal wiederholen. Sobald dies geschehen ist, wird Nunchuk Sie zu der entsprechenden Schlüsselseite führen, die Sie als diejenige bearbeiten können, die Sie mit dem _Custom_ Verfahren erstellt haben.



![image](assets/en/64.webp)



Versuchen Sie auch _Run health check_



![image](assets/en/65.webp)



oder um zu sehen, wie Sie alle Ihre Geldbörsen in der _Home_ der App anzeigen können.



![image](assets/en/66.webp)



## Im Hinterkopf behalten, um unabhängig zu bleiben


Genauso wie es eine Reihenfolge für die Erstellung gibt, d. h. zuerst die Schlüssel und dann den Wallet zu erzeugen, müssen Sie die umgekehrte Reihenfolge für das Löschen dieser Elemente aus Ihrer Anwendung einhalten.



Wenn Sie einen der Schlüssel löschen müssen, sollten Sie zuerst Wallet oder die Geldbörsen löschen, die einen der Signaturschlüssel für Transaktionen verwenden: Löschen Sie zuerst die Geldbörsen und erst dann die Schlüssel. Wenn Sie diese Reihenfolge nicht einhalten, können Sie den Schlüssel nicht entfernen.



Jetzt, wo Sie wissen, wie Sie mit dem Nunchuk anfangen, können Sie sich weiter mit dieser App beschäftigen und ihre Geheimnisse entdecken. In diesem Tutorial haben wir nur die ersten Schritte unternommen, aber es gibt anspruchsvollere Anwendungen und fortgeschrittene Bedürfnisse, die Sie mit dem Software Wallet erfüllen können.