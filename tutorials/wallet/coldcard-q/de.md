---
name: COLDCARD Q
description: Einrichten und Verwenden einer COLDCARD Q
---
![cover](assets/cover.webp)

Eine Hardware-Wallet ist ein elektronisches Gerät zur Verwaltung und Sicherung der privaten Schlüssel einer Bitcoin-Wallet. Im Gegensatz zu Software-Wallets (oder Hot Wallets), die auf Universalmaschinen installiert sind, die oft mit dem Internet verbunden sind, ermöglichen Hardware-Wallets eine physische Isolierung der privaten Schlüssel, was das Risiko von Piraterie und Diebstahl verringert.

Das Hauptziel einer Hardware-Wallet ist es, die Funktionalität des Geräts so weit wie möglich zu reduzieren, um die Angriffsfläche zu minimieren. Weniger Angriffsfläche bedeutet auch weniger potenzielle Angriffsvektoren, d. h. weniger Schwachstellen im System, die Angreifer ausnutzen könnten, um an Bitcoins zu gelangen.

Es ist ratsam, eine Hardware-Brieftasche zu verwenden, um Ihre Bitcoins zu sichern, vor allem, wenn Sie große Mengen besitzen, entweder in absoluten Werten oder als Anteil an Ihrem Gesamtvermögen.

Hardware-Wallets werden in Verbindung mit einer Wallet-Management-Software auf einem Computer oder Smartphone verwendet. Letztere verwaltet die Erstellung von Transaktionen, aber die kryptografische Signatur, die erforderlich ist, um diese Transaktionen gültig zu machen, wird ausschließlich in der Hardware-Wallet durchgeführt. Dies bedeutet, dass die privaten Schlüssel niemals einer potenziell anfälligen Umgebung ausgesetzt sind.

Hardware-Wallets bieten einen doppelten Schutz für den Benutzer: Einerseits sichern sie Ihre Bitcoins gegen Angriffe aus der Ferne, indem sie die privaten Schlüssel offline halten, und andererseits bieten sie im Allgemeinen einen größeren physischen Widerstand gegen Versuche, die Schlüssel zu extrahieren. Und genau nach diesen 2 Sicherheitskriterien können wir die verschiedenen Modelle auf dem Markt beurteilen und klassifizieren.

In diesem Lernprogramm möchte ich Ihnen eine solche Lösung vorstellen: die **COLDCARD Q**.

---
Da die COLDCARD Q eine Vielzahl von Funktionen bietet, schlage ich vor, ihre Verwendung in 2 Tutorials aufzuteilen. In diesem ersten Tutorial werden wir uns mit der Erstkonfiguration und den Grundfunktionen des Geräts befassen. In einem zweiten Tutorial werden wir uns dann ansehen, wie Sie alle erweiterten Optionen Ihrer COLDCARD nutzen können.

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
---
## Einführung der COLDCARD Q

Die COLDCARD Q ist eine reine Bitcoin-Hardware-Wallet, die vom kanadischen Unternehmen Coinkite entwickelt wurde, das für seine früheren MK-Modelle bekannt ist. Die Q ist ihr bisher fortschrittlichstes Produkt und wird als die ultimative Bitcoin-Hardware-Wallet positioniert.

Hardwaretechnisch ist die COLDCARD Q mit allen Funktionen ausgestattet, die für ein optimales Nutzererlebnis erforderlich sind:


- Ein großes LCD-Display vereinfacht die Navigation und Bedienung;
- Eine vollständige QWERTY-Tastatur;
- Integrierte Kamera zum Scannen von QR-Codes;
- Zwei microSD-Kartensteckplätze ;
- Eine vollständig isolierte Stromversorgungsoption über drei AAA-Batterien (nicht im Lieferumfang enthalten) oder über ein USB-C-Kabel;
- Zwei Secure Elements von zwei verschiedenen Herstellern für zusätzliche Sicherheit;
- Die Fähigkeit, über NFC zu kommunizieren.

Meiner Meinung nach hat die COLDCARD Q nur zwei Nachteile. Erstens ist sie wegen ihrer vielen Funktionen ziemlich sperrig, denn sie ist fast 13 cm lang und 8 cm breit, also fast so groß wie ein kleines Smartphone. Außerdem ist es wegen des Batteriefachs ziemlich dick. Wenn Sie auf der Suche nach einer kleineren, mobileren Hardware-Geldbörse sind, ist das viel kompaktere MK4 vielleicht die bessere Wahl. Der zweite Nachteil ist natürlich der Preis des Geräts, der auf der offiziellen Website mit **$239,99** angegeben ist, d.h. $72 mehr als das MK4, womit das Q in direktem Wettbewerb mit Premium-Hardware-Geldbörsen wie dem Ledger Flex oder dem Passport von Foundation steht.

![CCQ](assets/fr/001.webp)

Auf der Softwareseite ist die COLDCARD Q genauso gut ausgestattet wie die anderen Geräte von Coinkite und verfügt über eine Vielzahl fortschrittlicher Funktionen:


- Würfeln Sie, um Ihre eigene Genesungsphrase zu generieren;
- PIN-Code ;
- Countdown bis zur endgültigen PIN-Sperre ;
- BIP39 Passphrase ;
- Endgültige Sperr-PIN ;
- Countdown für die Verbindung ;
- SeedXOR;
- BIP85...

Kurz gesagt, die COLDCARD Q bietet ein besseres Benutzererlebnis als die MK4 und ist ideal für fortgeschrittene Benutzer, die eine größere Benutzerfreundlichkeit wünschen.

Die COLDCARD Q ist zum Verkauf [auf der offiziellen Coinkite-Website] (https://store.coinkite.com/store/coldcard) erhältlich. Sie kann auch bei einem Händler erworben werden.

## Vorbereiten des Tutorials

Wenn Sie Ihre COLDCARD erhalten haben, sollten Sie zunächst die Verpackung prüfen, um sicherzustellen, dass sie nicht geöffnet wurde. Wenn die Verpackung beschädigt ist, kann dies ein Hinweis darauf sein, dass die Hardware-Geldbörse beschädigt wurde und möglicherweise nicht echt ist.

![CCQ](assets/fr/002.webp)

Wenn Sie die Schachtel öffnen, sollten Sie die folgenden Gegenstände finden:


- Die COLDCARD Q befindet sich in einem versiegelten Beutel;
- Eine Karte, auf der Sie Ihre Eselsbrücke notieren können.

![CCQ](assets/fr/003.webp)

Vergewissern Sie sich, dass der Beutel nicht entsiegelt oder beschädigt wurde. Überprüfen Sie auch, ob die Nummer auf dem Beutel mit der Nummer auf dem Papier im Beutel übereinstimmt. Bewahren Sie diese Nummer für spätere Zwecke auf.

![CCQ](assets/fr/004.webp)

Wenn Sie Ihre COLDCARD mit Strom versorgen möchten, ohne sie an einen Computer anzuschließen (Luftspalt), legen Sie drei AAA-Batterien in die Rückseite des Geräts ein. Alternativ können Sie es über ein USB-C-Kabel mit Ihrem Computer verbinden.

![CCQ](assets/fr/005.webp)

Für dieses Tutorial benötigen Sie außerdem Sparrow Wallet, um Ihre Bitcoin-Brieftasche auf Ihrem Computer zu verwalten. Laden Sie [Sparrow Wallet] (https://sparrowwallet.com/download/) von der offiziellen Website herunter. Ich empfehle Ihnen dringend, sowohl die Authentizität (mit GnuPG) als auch die Integrität (per Hash) zu überprüfen, bevor Sie mit der Installation fortfahren. Wenn Sie nicht wissen, wie man das macht, folgen Sie dieser Anleitung:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
## Auswahl des PIN-Codes

Sie können nun Ihre COLDCARD einschalten, indem Sie auf die Taste in der linken oberen Ecke drücken.

![CCQ](assets/fr/006.webp)

Drücken Sie die Taste "*ENTER*", um die Nutzungsbedingungen zu akzeptieren.

![CCQ](assets/fr/007.webp)

Ihre COLDCARD Q zeigt dann oben auf dem Bildschirm eine Nummer an. Vergewissern Sie sich, dass diese Nummer mit der Nummer auf der versiegelten Tüte und auf dem Stück Plastik in der Tüte übereinstimmt. Dadurch wird sichergestellt, dass Ihr Paket zwischen dem Zeitpunkt, an dem es von Coinkite verpackt wurde, und dem Zeitpunkt, an dem Sie es öffnen, nicht geöffnet wurde. Drücken Sie "*ENTER*", um fortzufahren.

![CCQ](assets/fr/008.webp)

Navigieren Sie zum Menü "*PIN-Code wählen*" und bestätigen Sie mit der Taste "*ENTER*".

![CCQ](assets/fr/009.webp)

Dieser PIN-Code wird zum Entsperren Ihrer COLDCARD verwendet. Er ist daher ein Schutz gegen unbefugten physischen Zugriff. Dieser PIN-Code ist nicht an der Ableitung der kryptografischen Schlüssel Ihrer Brieftasche beteiligt. Selbst wenn Sie keinen Zugang zu diesem PIN-Code haben, können Sie also mit Ihrer mnemonischen Phrase wieder Zugang zu Ihren Bitcoins erhalten.

COLDCARD-PIN-Codes bestehen aus zwei Teilen: einem Präfix und einem Suffix, die jeweils zwischen 2 und 6 Ziffern enthalten können, also insgesamt 4 bis 12 Ziffern. Wenn Sie Ihre COLDCARD entsperren, müssen Sie zunächst das Präfix eingeben, woraufhin Ihnen das Gerät 2 Wörter anzeigt. Geben Sie dann das Suffix ein. Diese beiden Wörter werden Ihnen während dieses Konfigurationsschritts mitgeteilt und sollten sorgfältig gespeichert werden, da Sie sie jedes Mal benötigen, wenn Sie Ihre COLDCARD entsperren. Wenn die beiden Wörter, die beim Entsperren angezeigt werden, mit denen übereinstimmen, die Sie bei der Konfiguration gespeichert haben, bestätigt dies, dass Ihr Gerät seit der letzten Verwendung nicht kompromittiert wurde.

Klicken Sie erneut auf "*PIN wählen*"

![CCQ](assets/fr/010.webp)

Bestätigen Sie, dass Sie die Warnhinweise gelesen haben.

![CCQ](assets/fr/011.webp)

Sie wählen nun Ihren PIN-Code aus. Wir empfehlen einen langen, zufälligen PIN-Code. Achten Sie darauf, dass Sie diesen Code an einem anderen Ort als Ihre COLDCARD aufbewahren. Sie können die in Ihrem Paket enthaltene Karte verwenden, um diesen Code zu notieren.

Geben Sie das Präfix Ihrer Wahl ein und drücken Sie dann die Taste "*ENTER*", um den ersten Teil des PIN-Codes zu bestätigen.

![CCQ](assets/fr/012.webp)

Die beiden Anti-Phishing-Wörter werden dann auf Ihrem Bildschirm angezeigt. Bewahren Sie sie sorgfältig auf, damit Sie sie später wiederfinden. Sie können die in Ihrem Paket enthaltene Karte verwenden, um sie aufzuschreiben.

![CCQ](assets/fr/013.webp)

Geben Sie dann den zweiten Teil Ihres PIN-Codes ein und drücken Sie "*ENTER*".

![CCQ](assets/fr/014.webp)

Bestätigen Sie Ihre PIN, indem Sie sie ein zweites Mal eingeben und darauf achten, dass die beiden Anti-Phishing-Wörter mit denen übereinstimmen, die Sie zuvor gespeichert haben.

![CCQ](assets/fr/015.webp)

Denken Sie von nun an daran, jedes Mal, wenn Sie Ihre COLDCARD entsperren, die Gültigkeit der beiden Anti-Phishing-Wörter zu überprüfen, die auf dem Bildschirm erscheinen, nachdem Sie Ihren PIN-Code-Präfix eingegeben haben.

## Aktualisierung der Firmware

Wenn Sie Ihr Gerät zum ersten Mal benutzen, ist es wichtig, dass Sie die Firmware überprüfen und aktualisieren. Rufen Sie dazu das Menü "*Erweitert/Tools*" auf.

![CCQ](assets/fr/016.webp)

**Wichtig:** Wenn Sie planen, Ihre Firmware zu aktualisieren und dies nicht das erste Mal ist, dass Sie COLDCARD verwenden (d. h. Sie haben bereits eine Brieftasche auf COLDCARD erstellt), stellen Sie sicher, dass Sie Ihre mnemonische Phrase haben und dass sie funktioniert (sowie die optionale Passphrase, falls zutreffend). Dies ist wichtig, um zu vermeiden, dass Ihre Bitcoins im Falle eines Problems während der Geräteaktualisierung verloren gehen.

Wählen Sie "*Firmware aktualisieren*".

![CCQ](assets/fr/017.webp)

Wählen Sie "*Version anzeigen*".

![CCQ](assets/fr/018.webp)

Sie können die aktuelle Firmware-Version Ihrer COLDCARD überprüfen. In meinem Fall lautet die Version zum Beispiel "*1.2.3Q*".

![CCQ](assets/fr/019.webp)

Prüfen Sie [auf der offiziellen COLDCARD-Website] (https://coldcard.com/downloads), ob eine neuere Version verfügbar ist. Klicken Sie auf "*Download*", um die neue Firmware herunterzuladen.

![CCQ](assets/fr/020.webp)

An dieser Stelle empfehlen wir dringend, die Integrität und Authentizität der heruntergeladenen Firmware zu überprüfen. Laden Sie dazu [das Dokument mit den von den Entwicklern signierten Hashes aller Versionen] (https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt) herunter, überprüfen Sie die Signatur mit [dem öffentlichen Schlüssel des Entwicklers] (https://keybase.io/dochex) und stellen Sie sicher, dass der im signierten Dokument angegebene Hash mit dem der von der Website heruntergeladenen Firmware übereinstimmt. Wenn alles korrekt ist, können Sie mit der Aktualisierung fortfahren.

Wenn Sie mit diesem Überprüfungsprozess nicht vertraut sind, empfehle ich Ihnen, diese Anleitung zu lesen:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Nehmen Sie eine microSD-Karte und übertragen Sie die Firmware-Datei (Dokument in `.dfu`) auf diese Karte. Stecken Sie die microSD-Karte in einen der Anschlüsse Ihrer COLDCARD.

![CCQ](assets/fr/021.webp)

Wählen Sie dann im Menü für die Firmware-Aktualisierung "*Von MicroSD*".

![CCQ](assets/fr/022.webp)

Wählen Sie die entsprechende Datei für die Firmware aus.

![CCQ](assets/fr/023.webp)

Bestätigen Sie Ihre Auswahl durch Drücken der Taste "*ENTER*".

![CCQ](assets/fr/024.webp)

Bitte warten Sie, während die Firmware aktualisiert wird.

![CCQ](assets/fr/025.webp)

Sobald die Aktualisierung abgeschlossen ist, geben Sie Ihren PIN-Code ein, um das Gerät zu entsperren.

![CCQ](assets/fr/026.webp)

Ihre Firmware ist jetzt auf dem neuesten Stand.

## COLDCARD Q-Parameter

Wenn Sie möchten, können Sie die Einstellungen Ihrer COLDCARD über das Menü "*Einstellungen*" aufrufen.

![CCQ](assets/fr/027.webp)

In diesem Menü finden Sie verschiedene Anpassungsoptionen, wie z. B. die Einstellung der Bildschirmhelligkeit oder die Auswahl der Standardmaßeinheit.

![CCQ](assets/fr/028.webp)

Im nächsten Tutorial werden wir uns mit weiteren erweiterten Einstellungen beschäftigen:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
## Erstellen einer Bitcoin-Brieftasche

Jetzt ist es an der Zeit, eine neue Bitcoin-Brieftasche zu erstellen! Dazu müssen Sie eine mnemonische Phrase erstellen. Auf Coldcard haben Sie drei Möglichkeiten, diese Phrase zu erstellen:


- Verwenden Sie nur den internen Zufallszahlengenerator (TRNG);
- Verwenden Sie eine Kombination aus TRNG und Würfeln, um Entropie hinzuzufügen;
- Verwenden Sie nur Würfelwürfe.

**Anfängern und fortgeschrittenen Nutzern empfehlen wir, nur den internen Zufallszahlengenerator der COLDCARD zu verwenden**

Ich empfehle die Option "nur Würfel" nicht, da eine schlechte Ausführung zu einem Satz mit unzureichender Entropie führen kann, was die Sicherheit Ihrer Geldbörse gefährdet.

Die beste Option ist jedoch sicherlich die zweite, bei der die Verwendung von TRNG mit einer externen Entropiequelle kombiniert wird. Diese Methode garantiert eine Mindestentropie, die der von TRNG allein entspricht, und fügt eine zusätzliche Sicherheitsebene für den Fall eines möglichen Ausfalls des internen Generators (freiwillig oder nicht) hinzu. Wenn Sie sich für diese Option entscheiden, bei der TRNG und Würfeln kombiniert werden, profitieren Sie von einer größeren Kontrolle über die Generierung des Satzes, ohne die Risiken im Falle einer schlechten Ausführung Ihrerseits zu erhöhen.

Klicken Sie auf "*New Seed Words*".

![CCQ](assets/fr/029.webp)

Sie können die Länge Ihres Satzes wählen. Ich empfehle Ihnen, sich für einen Satz mit 12 Wörtern zu entscheiden, da er weniger komplex zu handhaben ist und nicht weniger Portfolio-Sicherheit bietet als ein Satz mit 24 Wörtern.

![CCQ](assets/fr/030.webp)

Die COLDCARD zeigt dann die von TRNG erzeugte Wiederherstellungsphrase an. Wenn Sie zusätzliche externe Entropie hinzufügen möchten, drücken Sie die Taste "*4*".

![CCQ](assets/fr/031.webp)

Dies führt Sie zu einer Seite, auf der Sie durch Würfeln Entropie hinzufügen können. Machen Sie so viele Würfe wie möglich (ein Minimum von 50 wird empfohlen, aber weniger ist nicht schlimm, da Sie bereits von der Entropie des TRNG profitieren), und notieren Sie die Ergebnisse mit den Tasten "*1*" bis "*6*". Wenn Sie fertig sind, drücken Sie "*ENTER*" zur Bestätigung.

![CCQ](assets/fr/032.webp)

Es wird eine neue mnemonische Phrase angezeigt, die auf der Entropie basiert, die Sie soeben angegeben haben, sowie auf der des TRNG.

**Warnung: Diese Phrase gibt Ihnen vollen, uneingeschränkten Zugriff auf alle Ihre Bitcoins**. Jeder, der im Besitz dieser Phrase ist, kann Ihr Geld stehlen, auch ohne physischen Zugriff auf Ihre COLDCARD. Die 12-Wort-Phrase stellt den Zugang zu Ihren Bitcoins im Falle von Verlust, Diebstahl oder Bruch Ihrer COLDCARD wieder her. Es ist daher sehr wichtig, dass Sie sie sorgfältig aufbewahren und an einem sicheren Ort aufbewahren.

Sie können ihn auf den mit Ihrer COLDCARD gelieferten Karton schreiben, oder für zusätzliche Sicherheit empfehle ich Ihnen, ihn auf einen Träger aus Edelstahl zu gravieren, um ihn vor Feuer, Überschwemmung oder Einsturz zu schützen. Speichern Sie sie auf keinen Fall auf einem digitalen Medium, sonst könnten Sie Ihre Bitcoins verlieren.

Schreiben Sie die auf dem Bildschirm angezeigten Wörter auf einen physischen Datenträger Ihrer Wahl. Je nach Ihrer Sicherheitsstrategie können Sie mehrere vollständige physische Kopien des Satzes anfertigen (aber vor allem dürfen Sie ihn nicht aufspalten). Achten Sie darauf, dass die Wörter nummeriert sind und in der richtigen Reihenfolge stehen.

Natürlich dürfen Sie **diese Worte** niemals im Internet weitergeben, anders als in diesem Tutorium. Dieses Musterportfolio wird nur im Testnet verwendet und am Ende des Tutoriums gelöscht.

Nachdem Sie die Wörter aufgeschrieben haben, drücken Sie "*ENTER*".

![CCQ](assets/fr/033.webp)

Um sicherzugehen, dass Sie Ihre Phrase korrekt gespeichert haben, fordert das System Sie auf, bestimmte Wörter zu bestätigen. Wählen Sie auf dem Tastenfeld die Nummer aus, die dem jeweiligen Wort entspricht.

![CCQ](assets/fr/034.webp)

Ihre Brieftasche ist nun erstellt! In der oberen rechten Ecke des Bildschirms sehen Sie den Fingerabdruck Ihres privaten Hauptschlüssels. Drücken Sie "*ENTER*".

![CCQ](assets/fr/035.webp)

Sie haben nun Zugriff auf das Hauptmenü Ihrer COLDCARD.

![CCQ](assets/fr/036.webp)

## Einrichten eines neuen Portfolios auf Sparrow

Es gibt mehrere Möglichkeiten, die Kommunikation zwischen der Sparrow Wallet-Software und Ihrer COLDCARD herzustellen. Die einfachste ist die Verwendung eines USB-C-Kabels. Standardmäßig sind auf Ihrer COLDCARD jedoch die Kabel- und NFC-Kommunikation deaktiviert. Um sie wieder zu aktivieren, navigieren Sie zu "*Einstellungen*", dann zu "*Hardware ein/aus*" und aktivieren Sie die gewünschte Kommunikationsoption.

![CCQ](assets/fr/037.webp)

Wenn Sie es vorziehen, Ihre COLDCARD völlig von Ihrem Computer zu isolieren, können Sie sich für eine indirekte "Air-Gap"-Kommunikation entscheiden, indem Sie QR-Codes oder eine microSD-Karte verwenden. Dies ist die Methode, die wir in diesem Tutorial verwenden werden.

Gehen Sie zu "*Erweitert/Tools*".

![CCQ](assets/fr/038.webp)

Wählen Sie "*Geldbörse exportieren*".

![CCQ](assets/fr/039.webp)

Wählen Sie dann "*Sparrow Wallet*".

![CCQ](assets/fr/040.webp)

Drücken Sie "*ENTER*", um die Konfigurationsdatei zu erstellen.

![CCQ](assets/fr/041.webp)

Wählen Sie dann aus, wie Sie diese Datei an Sparrow senden möchten. In diesem Beispiel habe ich eine microSD-Karte in den Steckplatz "*A*" eingelegt, also wähle ich die Schaltfläche "*1*". Sie können die Informationen auch als QR-Code auf Ihrem COLDCARD-Bildschirm anzeigen, indem Sie die Taste "*QR*" drücken und diesen QR-Code mit der Webcam Ihres Computers scannen.

![CCQ](assets/fr/042.webp)

Starten Sie Sparrow Wallet und überspringen Sie die Einführungsseiten, um zum Hauptbildschirm zu gelangen. Vergewissern Sie sich, dass Sie korrekt mit einem Knoten verbunden sind, indem Sie den Schalter unten rechts auf dem Bildschirm überprüfen.

![CCQ](assets/fr/043.webp)

Es wird dringend empfohlen, dass Sie Ihren eigenen Bitcoin-Knoten verwenden. Für dieses Tutorial verwende ich einen öffentlichen Knoten (gelb), da ich mich im Testnetz befinde, aber für den produktiven Einsatz ist es am besten, Bitcoin Core lokal (grün) oder einen Electrum-Server auf einem entfernten Knoten (blau) zu verwenden.

Öffnen Sie das Menü "*Datei*" und wählen Sie "*Neue Brieftasche*".

![CCQ](assets/fr/044.webp)

Benennen Sie Ihr Wallet und klicken Sie auf "*Create Wallet*".

![CCQ](assets/fr/045.webp)

Wählen Sie im Dropdown-Menü "*Skripttyp*" den Skripttyp, der Ihre Bitcoins sichern soll.

![CCQ](assets/fr/046.webp)

Klicken Sie auf "*Airgapped Hardware Wallet*".

![CCQ](assets/fr/047.webp)

Klicken Sie unter der Registerkarte "*Coldcard*" auf "*Scannen...*", wenn Sie den auf Ihrer COLDCARD angezeigten QR-Code scannen möchten, oder auf "*Datei importieren...*", um die Datei von der microSD-Karte zu importieren (dies ist die `.json`-Datei).

![CCQ](assets/fr/048.webp)

Prüfen Sie nach dem Import, ob der auf Sparrow angezeigte "*Master Fingerprint*" mit dem auf Ihrer COLDCARD angezeigten übereinstimmt. Bestätigen Sie die Erstellung, indem Sie auf "*Übernehmen*" klicken.

![CCQ](assets/fr/049.webp)

Richten Sie ein starkes Passwort ein, um den Zugang zu Ihrer Sparrow-Geldbörse zu sichern. Dieses Passwort schützt Ihre öffentlichen Schlüssel, Adressen, Tags und den Transaktionsverlauf vor unbefugtem Zugriff.

Es ist eine gute Idee, dieses Passwort zu speichern, damit Sie es nicht vergessen (z. B. in einem Passwort-Manager).

![CCQ](assets/fr/050.webp)

Ihre Geldbörse ist jetzt auf Sparrow Wallet eingerichtet.

![CCQ](assets/fr/051.webp)

Bevor Sie Ihre ersten Bitcoins in Ihrer Brieftasche erhalten, **empfehle ich Ihnen dringend, einen leeren Wiederherstellungstest** durchzuführen. Notieren Sie sich einige Referenzinformationen, wie z. B. Ihre xpub, und setzen Sie dann Ihre COLDCARD Q zurück, während die Wallet noch leer ist. Versuchen Sie dann, Ihre Brieftasche auf der COLDCARD wiederherzustellen, indem Sie Ihre Papier-Backups verwenden. Überprüfen Sie, ob die nach der Wiederherstellung erstellte xpub mit der ursprünglich notierten übereinstimmt. Wenn dies der Fall ist, können Sie sicher sein, dass Ihre Papier-Backups zuverlässig sind.

Um mehr darüber zu erfahren, wie man einen Wiederherstellungstest durchführt, empfehle ich Ihnen, diesen anderen Lehrgang zu lesen:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Bitcoins erhalten

Um Ihre ersten Bitcoins zu erhalten, schalten Sie zunächst Ihre COLDCARD ein und entsperren sie.

![CCQ](assets/fr/052.webp)

Klicken Sie auf Sparrow Wallet auf die Registerkarte "*Empfangen*".

![CCQ](assets/fr/053.webp)

Bevor Sie die von Sparrow Wallet vorgeschlagene Adresse verwenden, überprüfen Sie sie auf Ihrem COLDCARD-Bildschirm. Auf diese Weise können Sie sich vergewissern, dass die von Sparrow angezeigte Adresse nicht gefälscht ist und dass die Hardware-Wallet tatsächlich über den privaten Schlüssel verfügt, der benötigt wird, um die mit dieser Adresse gesicherten Bitcoins später auszugeben. Dies hilft Ihnen, verschiedene Arten von Angriffen zu vermeiden.

Um diese Prüfung durchzuführen, klicken Sie auf das Menü "*Address Explorer*" auf der COLDCARD.

![CCQ](assets/fr/054.webp)

Wählen Sie die Art des Skripts, das Sie auf Sparrow verwenden. In meinem Fall ist es Segwit P2WPKH. Ich klicke es an.

![CCQ](assets/fr/055.webp)

Sie können dann Ihre verschiedenen abgeleiteten Adressen der Reihe nach sehen.

![CCQ](assets/fr/056.webp)

Prüfen Sie mit Sparrow, ob die Adresse übereinstimmt. In meinem Fall ist die Adresse mit dem Ableitungspfad `m/84'/1'/0'/0/0` tatsächlich `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr` sowohl bei Sparrow als auch bei COLDCARD.

![CCQ](assets/fr/057.webp)

Eine andere Möglichkeit, den Besitz dieser Adresse zu überprüfen, besteht darin, den QR-Code direkt von Ihrer COLDCARD in Sparrow zu scannen. Wählen Sie auf dem Startbildschirm Ihrer COLDCARD "*Beliebigen QR-Code scannen*". Sie können auch die Taste "*QR*" auf der Tastatur verwenden.

![CCQ](assets/fr/058.webp)

Scannen Sie den QR-Code der Adresse, die auf Sparrow Wallet angezeigt wird.

![CCQ](assets/fr/059.webp)

Vergewissern Sie sich, dass die auf Ihrer COLDCARD angezeigte Adresse mit der auf Sparrow angezeigten Adresse übereinstimmt. Drücken Sie dann die Taste "*1*".

![CCQ](assets/fr/060.webp)

Die Adresse ist damit erfolgreich bestätigt.

![CCQ](assets/fr/061.webp)

Sie können jetzt ein "*Label*" hinzufügen, um die Quelle der Bitcoins zu beschreiben, die mit dieser Adresse gesichert werden. Dies ist eine gute Praxis, die es Ihnen ermöglicht, Ihre UTXOs besser zu verwalten.

![CCQ](assets/fr/062.webp)

Für weitere Informationen zum Thema Etikettierung empfehle ich auch diesen anderen Lehrgang:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52
Sie können dann diese Adresse verwenden, um Bitcoins zu erhalten.

![CCQ](assets/fr/063.webp)

## Bitcoins senden

Jetzt, wo Sie Ihre ersten Sats in Ihrer COLDCARD-gesicherten Geldbörse erhalten haben, können Sie sie auch ausgeben!

Beginnen Sie wie immer mit dem Einschalten und Entsperren Ihrer COLDCARD Q, öffnen Sie dann Sparrow Wallet und navigieren Sie zur Registerkarte "*Senden*", um eine neue Transaktion vorzubereiten.

![CCQ](assets/fr/064.webp)

Wenn Sie "Münzkontrolle" wünschen, d.h. gezielt auswählen möchten, welche UTXOs in der Transaktion verbraucht werden sollen, gehen Sie auf die Registerkarte "*UTXOs*". Wählen Sie die UTXOs aus, die Sie ausgeben möchten, und klicken Sie dann auf "*Ausgewählte senden*". Sie werden zum gleichen Bildschirm auf der Registerkarte "*Senden*" zurückgeleitet, aber mit den bereits für die Transaktion ausgewählten UTXOs.

![CCQ](assets/fr/065.webp)

Geben Sie die Zieladresse ein. Sie können auch mehrere Adressen eingeben, indem Sie auf die Schaltfläche "*+ Hinzufügen*" klicken.

![CCQ](assets/fr/066.webp)

Notieren Sie ein "*Etikett*", um sich den Zweck dieser Ausgabe zu merken.

![CCQ](assets/fr/067.webp)

Wählen Sie den Betrag, der an diese Adresse geschickt werden soll.

![CCQ](assets/fr/068.webp)

Passen Sie den Gebührensatz für Ihr Geschäft an den aktuellen Markt an.

![CCQ](assets/fr/069.webp)

Vergewissern Sie sich, dass alle Ihre Transaktionsparameter korrekt sind, und klicken Sie dann auf "*Transaktion erstellen*".

![CCQ](assets/fr/070.webp)

Wenn alles zu Ihrer Zufriedenheit ist, klicken Sie auf "*Transaktion zur Unterzeichnung abschließen*".

![CCQ](assets/fr/071.webp)

Sobald Sie Ihre Transaktion in Sparrow erstellt haben, ist es an der Zeit, sie mit Ihrer COLDCARD zu signieren. Um die PSBT (unsignierte Transaktion) an Ihr Gerät zu übertragen, haben Sie mehrere Möglichkeiten. Wenn die kabelgebundene Datenübertragung aktiviert ist, können Sie die Transaktion direkt über eine USB-C-Verbindung senden, so wie Sie es mit jeder anderen Hardware-Wallet tun würden. In diesem Fall müssten Sie bei Sparrow auf die Schaltfläche "*Sign*" in der unteren rechten Ecke klicken. In meinem Beispiel ist diese Schaltfläche blockiert, weil die COLDCARD nicht per Kabel angeschlossen ist.

![CCQ](assets/fr/072.webp)

Wenn Sie es vorziehen, eine "Air-Gap"-Verbindung ohne direkten Kontakt zwischen der Hardware-Geldbörse und Ihrem Computer aufrechtzuerhalten, haben Sie 2 Möglichkeiten. Die erste und komplexere ist die Verwendung einer microSD-Karte. Legen Sie die microSD-Karte in Ihren Computer ein, zeichnen Sie die Transaktion über die Schaltfläche "*Transaktion speichern*" auf Sparrow auf und übertragen Sie diese Karte dann auf einen Anschluss an Ihrer COLDCARD.

![CCQ](assets/fr/073.webp)

Rufen Sie dann das Menü "*Unterschriftsreif*" auf.

![CCQ](assets/fr/074.webp)

Überprüfen Sie die Transaktionsdetails auf Ihrer COLDCARD, einschließlich der Empfängeradresse, des gesendeten Betrags und der Transaktionsgebühr.

![CCQ](assets/fr/075.webp)

Wenn alles korrekt ist, drücken Sie die Taste "*ENTER*", um die Transaktion zu unterzeichnen.

![CCQ](assets/fr/076.webp)

Legen Sie dann die microSD-Karte wieder in Ihren Computer ein und klicken Sie bei Sparrow auf "*Transaktion laden*", um die signierte Transaktion von der microSD-Karte zu laden. Sie können dann eine letzte Überprüfung durchführen, bevor Sie sie in das Bitcoin-Netzwerk hochladen.

![CCQ](assets/fr/077.webp)

Die zweite Methode zum Signieren mit Ihrer COLDCARD in Air-Gap, die viel einfacher ist als die microSD-Methode, ist das Scannen des PSBT direkt über die Kamera des Geräts. Wählen Sie auf Sparrow "*QR anzeigen*".

![CCQ](assets/fr/078.webp)

Wählen Sie auf der COLDCARD "*Beliebigen QR-Code scannen*". Sie können auch die Taste "*QR*" auf der Tastatur verwenden.

![CCQ](assets/fr/079.webp)

Verwenden Sie die Kamera der COLDCARD, um den auf Sparrow angezeigten QR-Code zu scannen.

![CCQ](assets/fr/080.webp)

Die Details der Transaktion werden zur Überprüfung erneut angezeigt. Drücken Sie "*ENTER*", um zu unterschreiben, wenn alles zu Ihrer Zufriedenheit ist.

![CCQ](assets/fr/081.webp)

Ihre COLDCARD zeigt dann die signierte Transaktion als QR-Code an. Verwenden Sie die Webcam Ihres Computers, um diesen QR-Code zu scannen, indem Sie "*Scan QR*" auf Sparrow auswählen.

![CCQ](assets/fr/082.webp)

Ihre signierte Transaktion ist nun auf Sparrow sichtbar. Prüfen Sie ein letztes Mal, ob alles korrekt ist, und klicken Sie dann auf "*Broadcast Transaction*", um die Transaktion im Bitcoin-Netzwerk zu übertragen.

![CCQ](assets/fr/083.webp)

Sie können Ihre Transaktion auf der Registerkarte "*Transaktionen*" von Sparrow Wallet verfolgen.

![CCQ](assets/fr/084.webp)

Herzlichen Glückwunsch, Sie sind nun mit der grundlegenden Nutzung von COLDCARD Q mit Sparrow Wallet vertraut!

Wenn Sie diese Anleitung nützlich fanden, wäre ich Ihnen sehr dankbar, wenn Sie unten einen grünen Daumen hinterlassen würden. Bitte teilen Sie dieses Tutorial auch in Ihren sozialen Netzwerken. Herzlichen Dank!

Ich empfehle Ihnen auch, einen Blick auf dieses andere Tutorial zu werfen, in dem wir die erweiterten Optionen der COLDCARD Q besprechen:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0