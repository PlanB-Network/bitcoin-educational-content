---
name: Ashigaru
description: Der fork von Samourai Wallet zum Sichern, Verwalten und Mischen Ihrer Bitcoins
---

![cover](assets/cover.webp)



Ashigaru ist eine Bitcoin-Mobile-wallet-Anwendung, die an das Samourai-Wallet-Projekt anschließt, allerdings in einer neuen Form. Diese Software entstand in einem besonderen Kontext: Im April 2024 wurden die Gründer von Samourai Wallet von den amerikanischen Behörden verhaftet, und ihre Server wurden beschlagnahmt. Die Samurai-Anwendung selbst blieb zwar nutzbar, wird aber derzeit nicht mehr gepflegt. Ashigaru ist eine kostenlose fork-Version von Samurai Wallet, die von einem anonymen Team gepflegt wird, um die Kontinuität der Samurai-Funktionalität zu gewährleisten und die ursprüngliche Philosophie zu bewahren: die Verteidigung der Privatsphäre und der Souveränität der Bitcoin-Nutzer.



Ashigaru übernimmt viel von der DNA von Samourai: eine ähnliche Schnittstelle, ein offensichtlich selbstverwaltender Ansatz, Open Source und ein Schwerpunkt auf Privatsphäre. Der Code wird unter der GNU GPLv3 Lizenz vertrieben, die sicherstellt, dass jeder die Software prüfen, verändern oder weitergeben kann.



Die Ashigaru-Anwendung enthält eine Reihe von fortschrittlichen Tools für die Vertraulichkeit und Verwaltung Ihrer UTXOs:




- Whirlpool**, ein auf Zerolink basierendes Coinjoin-Protokoll, das es Ihnen ermöglicht, die deterministischen Verbindungen zwischen Transaktionsein- und -ausgängen zu unterbrechen, ohne die Hoheit über Ihr Geld zu verlieren.
- PayNym**, das wiederverwendbare Zahlungscodes (BIP47) implementiert, die jetzt über ein "*Pepehash*"-Avatarsystem dargestellt werden.
- Ricochet**, eine Funktion, die Zwischensprünge zu Transaktionen hinzufügt, um deren Rückverfolgung zu erschweren.
- Und natürlich ***Coin Control*** zum präzisen Auswählen, Einfrieren und Beschriften Ihrer UTXOs.
- Batch Spending***, um Kosten zu senken, indem mehrere Zahlungen in einer einzigen Transaktion zusammengefasst werden.
- Der **Stealth Mode**, der die Anwendung auf Ihrem Mobiltelefon hinter einer Attrappe versteckt, um bei einer physischen Inspektion Ihres Telefons unbemerkt zu bleiben.
- Erweiterte Ausgabentools zur Optimierung Ihrer Vertraulichkeit (payjoin, stonewall...).
- Ein optimiertes Wiederherstellungssystem mit der Passphrase BIP39.
- Ein System zur automatischen Optimierung der Auswahl von Transaktionsgebühren.



![Image](assets/fr/01.webp)



Ashigaru richtet sich daher an Nutzer, die sich der Problematik der Rückverfolgbarkeit von Transaktionen auf Bitcoin bewusst sind. Egal, ob Sie ein datenschutzbewusster Nutzer, ein erfahrener Bitcoiner, der sich der Selbstkontrolle verschrieben hat, oder eine Person sind, die den Risiken einer verstärkten Überwachung ausgesetzt ist, diese wallet-Anwendung bietet Ihnen die Werkzeuge, die Sie benötigen, um die Kontrolle über Ihre Aktivitäten auf Bitcoin wiederzuerlangen.



Ashigaru ist in einer mobilen Version über seine App verfügbar, die wir in diesem Tutorial erkunden werden. Aber es kann auch auf dem PC mit ***Ashigaru Terminal*** verwendet werden, das wir in einem späteren Tutorial vorstellen werden.



![Image](assets/fr/02.webp)



In diesem Tutorial möchte ich Sie in die grundlegende Nutzung von Ashigaru einführen: Installation, Verbindung zum Dojo, Backup, Empfang und Versand von Bitcoins. Fortgeschrittene Tools werden in anderen speziellen Tutorials vorgestellt.



## 1. Voraussetzungen für Ashigaru



Die Anwendung benötigt ein paar Voraussetzungen, um richtig zu funktionieren. Zunächst einmal handelt es sich nicht um eine Anwendung, die in klassischen Geschäften wie dem Google Play Store oder App Store erhältlich ist. Sie lässt sich nur manuell auf deinem Handy installieren, und zwar über die Datei "apk", die du über das Tor-Netzwerk herunterladen kannst. Wenn du also ein iPhone verwendest, wird diese Methode nicht funktionieren: Du brauchst ein Android-Gerät.



Um die `.apk` Datei über Tor herunterzuladen, brauchst du einen Browser, der auf `.onion` Seiten zugreifen kann. Am einfachsten ist es, die Tor-Browser-Anwendung auf deinem Handy zu installieren, die im [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) oder direkt [über die `.apk`](https://www.torproject.org/download/#android) erhältlich ist.



![Image](assets/fr/03.webp)



Die meisten neueren Smartphones blockieren standardmäßig die Installation von Anwendungen aus unbekannten Quellen. Sie müssen diese Option für Tor Browser in den Einstellungen Ihres Geräts vorübergehend aktivieren, um die Installation zu ermöglichen. Sobald die Anwendung installiert ist, sollten Sie diese Funktion deaktivieren, um die Sicherheit Ihres Telefons zu erhöhen.



Eine weitere wesentliche Voraussetzung für die Nutzung von Ashigaru ist ein Bitcoin Dojo-Knoten. Aus Gründen der Sicherheit und Souveränität unterhält das Ashigaru-Team keinen zentralen Server, um Ihre Anwendung zu verbinden. Sie müssen also Ihre eigene Dojo-Instanz betreiben oder eine Verbindung zu einer vertrauenswürdigen Instanz herstellen.



Das Dojo ermöglicht es Ihrer Ashigaru-Anwendung, Blockchain-Informationen abzurufen, Ihr Adressguthaben einzusehen und Ihre Transaktionen im Bitcoin-Netzwerk zu übertragen.



Um mehr über Dojo zu erfahren und zu lernen, wie man es installiert, lade ich Sie ein, diesem speziellen Tutorial zu folgen:



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Wenn Sie es sich wirklich nicht leisten können, Ihr eigenes Dojo zu betreiben, können Sie unter [dojobay.pw](https://www.dojobay.pw/mainnet/) Leute finden, die bereit sind, ihre Instanz kostenlos zu teilen. Dies kann eine vorübergehende Lösung sein, aber langfristig empfehle ich Ihnen, Ihr eigenes Dojo zu verwenden, um Ihre Souveränität und Vertraulichkeit zu gewährleisten.



## 2. Überprüfen und installieren Sie die Ashigaru-Anwendung



### 2.1. Laden Sie die Ashigaru-Anwendung herunter



Öffne auf deinem Handy den Tor-Browser und gehe zu [der offiziellen Ashigaru-Website](https://ashigaru.rs/download/), im Bereich "Downloads". Klicke dann auf die Schaltfläche "Download für Android", um die Installationsdatei herunterzuladen.



![Image](assets/fr/04.webp)



Bevor wir die Anwendung auf Ihrem Gerät installieren, überprüfen wir ihre Authentizität und Integrität. Dies ist ein sehr wichtiger Schritt, vor allem wenn Sie eine Anwendung direkt aus einer "apk"-Datei installieren.



### 2.2. Ashigaru-Anwendung prüfen



Gehen Sie zurück zur [offiziellen Ashigaru-Website](https://ashigaru.rs/download/) in den Abschnitt `Download` und kopieren Sie die Nachricht, die unter dem Titel `SHA-256 Hash der APK-Datei` angezeigt wird. Kopieren Sie den gesamten Block, von `BEGIN PGP SIGNED MESSAGE` bis `END PGP SIGNATURE`.



![Image](assets/fr/05.webp)



Öffne auf deinem Handy einen neuen Tab im Tor-Browser und gehe zu [dem Keybase-Verifizierungstool](https://keybase.io/verify). Füge die soeben kopierte Nachricht in das dafür vorgesehene Feld ein und klicke dann auf die Schaltfläche "Überprüfen".



![Image](assets/fr/06.webp)



Wenn die Signatur echt ist, zeigt Keybase eine Meldung an, die bestätigt, dass die Datei von den Ashigaru-Entwicklern signiert wurde. Sie können auch auf das von Keybase angezeigte Profil `ashigarudev` klicken und überprüfen, ob der Fingerabdruck des Schlüssels genau mit : `A138 06B1 FA2A 676B`.



Wenn jedoch in diesem Stadium ein Fehler erscheint, bedeutet dies, dass die Signatur ungültig ist. In diesem Fall **installieren Sie die APK** nicht. Beginnen Sie noch einmal von vorne, oder bitten Sie die Community um Hilfe, bevor Sie fortfahren.



![Image](assets/fr/07.webp)



Keybase hat Ihnen den Hash der Anwendung zur Verfügung gestellt. Wir werden nun überprüfen, ob der Hash der heruntergeladenen .apk-Datei mit dem von Keybase verifizierten Hash übereinstimmt. Gehen Sie dazu auf [HASH DATEI ONLINE](https://hash-file.online/).



![Image](assets/fr/08.webp)



Klicken Sie auf die Schaltfläche `BROWSE...` und wählen Sie die in Schritt 2.1 heruntergeladene `.apk`-Datei aus.


Wählen Sie dann die Hash-Funktion `SHA-256`, und klicken Sie auf `CALCULATE HASH`, um den Hash-Wert Ihrer Datei zu berechnen.



![Image](assets/fr/09.webp)



Auf der Website wird der Hash Ihrer `.apk`-Datei angezeigt. Vergleichen Sie ihn mit dem Hash, den Sie auf Keybase.io überprüft haben. Wenn die beiden Hashes identisch sind, war die Authentizitäts- und Integritätsprüfung erfolgreich. Sie können nun mit der Installation der Anwendung fortfahren.



![Image](assets/fr/10.webp)



### 2.3. Installieren Sie die Ashigaru-Anwendung



Um die Anwendung zu installieren, öffnen Sie den Dateimanager Ihres Telefons und gehen Sie zum Ordner "Downloads". Klicken Sie dann auf die "apk"-Datei, die Sie gerade überprüft haben, und bestätigen Sie die Installation, wenn Sie dazu aufgefordert werden.



![Image](assets/fr/11.webp)



Ashigaru ist jetzt auf Ihrem Handy installiert.



## 3. Initialisieren Sie die Anwendung und erstellen Sie ein Bitcoin-Portfolio



Wenn Sie die Anwendung zum ersten Mal starten, wählen Sie "MAINNET".



![Image](assets/fr/12.webp)



Klicken Sie dann auf `Get Started`.



![Image](assets/fr/13.webp)



Wir werden nun ein neues Bitcoin-Portfolio erstellen. Drücken Sie die Schaltfläche "Neues wallet erstellen".



![Image](assets/fr/14.webp)



### 3.1. ein Bitcoin-Portfolio erstellen



Ashigaru benötigt ein passphrase BIP39. Wählen Sie Ihren passphrase und geben Sie ihn in die entsprechenden Felder ein. Er muss so lang und zufällig wie möglich sein, um einem Brute-Force-Angriff zu widerstehen.



Machen Sie sofort ein physisches Backup von diesem passphrase. Dies ist ein sehr wichtiger Schritt: Wenn Sie Ihr Telefon verlieren, **wenn Sie dieses passphrase nicht mehr haben, werden Sie nicht mehr in der Lage sein, auf Ihre Bitcoins** zuzugreifen, die in Ihrem Ashigaru wallet gespeichert sind. Dasselbe passphrase wird auch zur Verschlüsselung der wallet Wiederherstellungsdatei verwendet.



Wenn Sie nicht wissen, was ein passphrase ist, oder nicht ganz verstehen, wie es funktioniert, empfehle ich Ihnen dringend, diese zusätzliche Anleitung zu lesen. Das ist wichtig, denn das passphrase ist ein kritisches Element Ihrer Sicherheit: Wenn Sie seine Verwendung falsch verstehen, kann das zum dauerhaften Verlust Ihrer Mittel führen.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Sobald Sie Ihr passphrase eingegeben haben, klicken Sie auf "Weiter".



![Image](assets/fr/15.webp)



Wählen Sie dann einen PIN-Code. Dieser Code wird zum Entsperren Ihres Ashigaru wallet verwendet und schützt ihn vor unbefugtem physischen Zugriff. Er ist nicht an der kryptografischen Ableitung Ihrer wallet-Schlüssel beteiligt. Das bedeutet, dass jeder, der Ihre mnemonische Phrase und passphrase kennt, auch ohne Kenntnis des PIN-Codes in der Lage ist, wieder Zugang zu Ihren Bitcoins zu erhalten.



Entscheiden Sie sich für einen langen, zufälligen PIN-Code. Denken Sie daran, eine Sicherungskopie an einem anderen Ort als Ihr Telefon aufzubewahren, um zu verhindern, dass beide gleichzeitig kompromittiert werden.



![Image](assets/fr/16.webp)



Sobald der PIN-Code erstellt wurde, zeigt Ashigaru die mnemonische Phrase Ihres wallet an. Warnung: Diese Phrase, kombiniert mit Ihrem passphrase, gibt Ihnen vollen Zugriff auf Ihre Bitcoins. Jeder, der diese Phrase besitzt, kann sich in den Besitz Ihrer Gelder bringen, selbst wenn er keinen Zugang zu Ihrem Telefon hat. Diese 12-Wort-Sequenz kann verwendet werden, um Ihr wallet im Falle von Verlust, Diebstahl oder Bruch Ihres Telefons wiederherzustellen. Es ist daher wichtig, sie mit äußerster Sorgfalt auf einem physischen Medium (Papier oder Metall) zu speichern.



Speichern Sie diesen Satz niemals in digitaler Form, sonst riskieren Sie, dass Ihr Geld gestohlen wird. Je nach Ihrer Sicherheitsstrategie können Sie mehrere physische Kopien erstellen, aber teilen Sie sie niemals. Behalten Sie die Wörter in ihrer genauen Reihenfolge bei und achten Sie darauf, dass sie nummeriert sind.



Und schließlich sollten Sie die Mnemonik und den passphrase nie am selben Ort aufbewahren. Wenn beide gleichzeitig kompromittiert würden, könnte ein Angreifer Zugang zu Ihrem wallet erhalten.



![Image](assets/fr/17.webp)



Wenn Sie mehr darüber erfahren möchten, wie Sie Ihre mnemonische Phrase sichern können, lesen Sie bitte diesen ergänzenden Leitfaden:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru bittet Sie dann, Ihr passphrase erneut zu bestätigen. Nutzen Sie diese Gelegenheit, um zu überprüfen, ob Ihr physisches Backup korrekt ist.



![Image](assets/fr/18.webp)



### 3.2. ein Dojo anschließen



Als Nächstes folgt der Schritt der Verbindung mit Ihrem Dojo. Wie in der Einführung erläutert, muss Ashigaru mit einem Dojo verbunden sein, um mit dem Bitcoin-Netzwerk zu interagieren.



Loggen Sie sich in das "Maintenance Tool" Ihres Dojos ein und öffnen Sie das Menü "PAIRING".



![Image](assets/fr/19.webp)



Drücken Sie auf Ashigaru die Taste "QR scannen" und scannen Sie dann den von Ihrem DMT angezeigten QR-Code für die Verbindung. Klicken Sie dann zur Bestätigung auf "Fortfahren".



![Image](assets/fr/20.webp)



Geben Sie Ihren PIN-Code ein, um das wallet zu entsperren. Dadurch gelangen Sie auf die Synchronisierungsseite. Es ist normal, dass zu diesem Zeitpunkt *PayNym*-Fehler angezeigt werden, da das wallet neu ist. Klicken Sie einfach auf `Fortfahren`.



![Image](assets/fr/21.webp)



Sie werden dann zur Startseite Ihres Portfolios weitergeleitet.



![Image](assets/fr/22.webp)



Bevor Sie weitermachen, empfehle ich Ihnen, eine Testwiederherstellung durchzuführen, während die wallet noch keine Bitcoin enthält. So können Sie überprüfen, ob Ihre Backups auf Papier richtig funktionieren. Um herauszufinden, wie das geht, folgen Sie dieser Anleitung:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Einrichten der Ashigaru-Anwendung



Um zu den Anwendungseinstellungen zu gelangen, klicken Sie auf das Bild Ihres *PayNym* in der oberen linken Ecke und wählen Sie dann "Einstellungen".



![Image](assets/fr/23.webp)



Hier finden Sie mehrere Optionen, mit denen Sie die Funktionsweise von Ashigaru an Ihre Bedürfnisse anpassen können. Ich empfehle Ihnen jedoch dringend, gleich zu Beginn 2 wichtige Parameter zu aktivieren.



Öffnen Sie zunächst das Menü "Sicherheit" > "Tarnmodus" und aktivieren Sie dann diese Funktion, wenn Sie sie benötigen. Sie verbirgt die Ashigaru-Anwendung hinter dem Namen, dem Logo und der Oberfläche einer normalen Anwendung, die auf Ihrem Telefon installiert ist. Damit soll verhindert werden, dass jemand Ashigaru bei einer physischen Inspektion Ihres Telefons identifiziert.



![Image](assets/fr/24.webp)



Jede angebotene gefälschte Anwendung hat eine bestimmte Methode, um die echte Ashigaru-Oberfläche freizuschalten. Wenn Sie zum Beispiel den Taschenrechner auswählen, verschwindet die Ashigaru-Anwendung von Ihrem Startbildschirm und wird durch einen gefälschten Taschenrechner ersetzt. Wenn Sie diesen öffnen, sehen Sie eine klassische, funktionierende Taschenrechneroberfläche, aber um auf Ashigaru zuzugreifen, müssen Sie nur fünfmal schnell auf das Symbol "=" tippen.



Der zweite wichtige Parameter, der aktiviert werden muss, ist [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Diese Option ermöglicht es Ihnen, die Kosten einer Transaktion zu erhöhen, wenn sie in den Mempools stecken bleibt, weil die Kosten zu niedrig sind. Sie können sie über das Menü `Transaktionen > Ausgeben mit RBF` aktivieren.



![Image](assets/fr/25.webp)



Tipp: Sie können die Anzeigeeinheit Ihres Portfolios von `BTC` auf `sat` ändern, indem Sie einfach auf den auf der Startseite angezeigten Gesamtsaldo klicken.



## 5. Bitcoins auf Ashigaru erhalten



Jetzt, wo Ihr Portfolio betriebsbereit ist, können Sie Satss empfangen. Drücken Sie dazu die Schaltfläche "+" unten rechts auf der Benutzeroberfläche und dann die grüne Schaltfläche "Empfangen".



![Image](assets/fr/26.webp)



Ashigaru zeigt Ihnen dann die erste unbenutzte Empfängeradresse in Ihrem wallet an, um die Wiederverwendung von Adressen zu verhindern (die Wiederverwendung von Adressen ist eine sehr schlechte Praxis für Ihre Privatsphäre). Sie können diese Adresse dann an die Person oder den Dienst weiterleiten, der Ihnen Bitcoins senden muss.



![Image](assets/fr/27.webp)



Sobald die Transaktion im Netz verbreitet wurde, wird sie automatisch auf der Startseite der Anwendung angezeigt.



![Image](assets/fr/28.webp)



## 6. Bitcoins mit Ashigaru versenden



Jetzt, wo Sie Bitcoins in Ihrem Ashigaru wallet haben, können Sie sie auch verschicken. Drücken Sie dazu die "+"-Taste unten rechts und wählen Sie dann die rote "Senden"-Taste.



![Image](assets/fr/29.webp)



Wählen Sie dann das Konto aus, von dem Sie die Ausgabe tätigen möchten. Im Moment haben wir uns noch nicht mit dem Postmix-Konto beschäftigt, das für Coinjoins reserviert ist und das wir in einem späteren Tutorial behandeln werden. Wir werden also Geld vom Haupteinlagenkonto senden.



![Image](assets/fr/30.webp)



Geben Sie Ihre Transaktionsdetails ein: den zu sendenden Betrag und die Bitcoin-Adresse des Empfängers.



![Image](assets/fr/31.webp)



Wenn Sie auf die drei kleinen Punkte in der oberen rechten Ecke und dann auf "Nicht ausgegebene Ausgaben anzeigen" klicken, können Sie auch genau auswählen, welche UTXOs Sie ausgeben möchten, um Ihre Privatsphäre zu schützen.



![Image](assets/fr/32.webp)



Wenn Sie alle Angaben gemacht haben, klicken Sie auf den weißen Pfeil am unteren Rand der Benutzeroberfläche, um fortzufahren.



Sie gelangen dann auf eine Übersichtsseite mit allen Details zu Ihrer Transaktion. Es werden mehrere wichtige Elemente angezeigt:




- Überprüfen Sie im Block "Ziel" ein letztes Mal, ob die Empfängeradresse und der gesendete Betrag korrekt sind;
- Im Block `Gebühren` können Sie den von Ashigaru automatisch gewählten Gebührensatz einsehen und gegebenenfalls ändern, indem Sie auf `VERWALTEN` klicken;
- Der "Transaction"-Block gibt die Art der Transaktion an, die Sie durchführen wollen. Hier geht es um eine einfache Transaktion, aber Ashigaru unterstützt auch andere Arten von datenschutzoptimierten Transaktionen, die wir in einem späteren Tutorial ausführlich behandeln werden;
- Der rote "Transaktionsalarm"-Block warnt Sie, wenn Ihre Transaktion Muster aufweist, die von den Kettenanalysetools erkannt werden können und die Ihre Privatsphäre gefährden könnten. Wenn Sie darauf klicken, können Sie sich die Details ansehen. In meinem Fall zeigt mir Ashigaru zum Beispiel an, dass der gesendete Betrag rund ist (3000 sats), so dass ich ableiten kann, welcher Ausgang den Ausgaben und welcher dem Austausch entspricht. Um mehr über diese Heuristik der Kettenanalyse zu erfahren, lade ich Sie ein, meine BTC 204-Schulung auf der Plan ₿ Academy zu besuchen;
- Schließlich können Sie Ihre Transaktion mit einem Etikett versehen, um ihren Zweck zu dokumentieren.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Sobald Sie alle Informationen überprüft haben, verwenden Sie den grünen Pfeil, um die Bitcoins zu senden. Halten Sie den Pfeil gedrückt und ziehen Sie ihn dann nach rechts, um den Upload zu bestätigen.



![Image](assets/fr/33.webp)



Ihre Transaktion wurde im Bitcoin-Netz übertragen.



![Image](assets/fr/34.webp)



## 7. Wiederherstellung des Ashigaru wallet



Die Wiederherstellung eines Ashigaru wallet unterscheidet sich geringfügig von der eines klassischen Bitcoin wallet, da die Anwendung die gleichen Methoden wie der Samurai Wallet verwendet. Wenn Sie den Zugriff auf Ihren wallet verlieren (sei es, weil Sie Ihre PIN vergessen, ihn deinstalliert oder Ihr Telefon verloren haben), gibt es mehrere Möglichkeiten, Ihre Bitcoins wiederherzustellen.



Wenn Sie noch Zugang zu Ihrem Telefon haben oder eine Sicherungskopie dieser Datei erstellt haben, ist die einfachste Methode die Verwendung der Sicherungsdatei `ashigaru.txt`. Diese Datei enthält alle Informationen, die du brauchst, um dein Portfolio auf einer neuen Instanz von Ashigaru (oder auf Sparrow Wallet) wiederherzustellen, aber sie ist mit dem passphrase verschlüsselt, den du in Schritt 3.1 dieses Tutorials definiert hast. Sie müssen also sowohl die Datei `ashigaru.txt` als auch Ihren passphrase haben, um diese Methode anwenden zu können.



Mit diesen beiden Elementen können Sie z. B. Ihr Portfolio auf Sparrow Wallet wiederherstellen.



![Image](assets/fr/35.webp)



Wenn Sie keinen Zugriff auf die Datei `ashigaru.txt` haben, können Sie trotzdem mit Ihrer passphrase-Mnemonik den Zugriff auf Ihre Fonds wiederherstellen, so wie Sie es für jedes andere Bitcoin-Portfolio tun würden. Ich empfehle, dass Sie diese Wiederherstellung entweder auf einer neuen Ashigaru-Instanz oder direkt auf Sparrow Wallet durchführen, um die Umgehungspfade von Whirlpool wiederherzustellen, wenn Sie diese verwendet haben. Alternativ können Sie diese Informationen auch in jede andere BIP39-kompatible Software importieren, indem Sie die Ableitungspfade manuell eingeben.



Weitere Informationen zu diesem Verfahren finden Sie in der vollständigen Anleitung, die ich zur Wiederherstellung eines Wallet Samurai wallet geschrieben habe. Da Ashigaru ein fork ist, ist das Verfahren identisch:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Wie Sie sehen, ist die passphrase unabhängig von der von Ihnen verwendeten Wiederherstellungsmethode unverzichtbar. Stellen Sie also sicher, dass Sie ihn sorgfältig sichern. Je nach Ihrer Sicherheitsstrategie können Sie auch mehrere Kopien erstellen.



## 8. Anwendung aktualisieren



Um die Ashigaru-App zu aktualisieren, müssen Sie, da Sie sie über eine "apk"-Datei und nicht wie eine normale App über den Play Store installiert haben, die neue "apk"-Datei herunterladen, die der aktualisierten Version entspricht, und sie dann manuell installieren.



Wiederholen Sie die in Abschnitt 2 dieser Anleitung beschriebenen Schritte, mit dem Unterschied, dass Ihr Android-Telefon Ihnen die Option "Aktualisieren" und nicht "Installieren" anbieten sollte, wenn Sie auf die "apk"-Datei klicken, um die Installation zu starten**.



![Image](assets/fr/41.webp)



Dies ist ein sehr wichtiger Punkt: Wenn Android `Install` statt `Update` anzeigt, installieren Sie wahrscheinlich eine betrügerische Version. Brechen Sie in diesem Fall den Installationsvorgang sofort ab.



Wie bei der Erstinstallation überprüfen Sie bitte die Authentizität und Integrität der "apk"-Datei, bevor Sie mit dem Update fortfahren.



Um herauszufinden, wann eine neue Version verfügbar ist, schauen Sie von Zeit zu Zeit auf der offiziellen Ashigaru-Website nach. Seien Sie versichert, dass Ashigaru eine stabile, ausgereifte Anwendung ist, die von Samourai Wallet geerbt wurde, und dass Updates im Vergleich zu jüngerer Software relativ selten sind.



## 9. Spenden Sie für das Ashigaru-Projekt



Ashigaru ist ein Open-Source-Projekt. Wenn Sie die Entwicklung unterstützen möchten, können Sie direkt aus der Anwendung heraus über PayNym eine Spende tätigen.



Klicken Sie dazu auf Ihren PayNym oben rechts auf der Benutzeroberfläche und wählen Sie dann Ihren Zahlungscode, der mit "PM..." beginnt.



![Image](assets/fr/36.webp)



Drücken Sie dann die "+"-Taste unten rechts auf dem Bildschirm.



![Image](assets/fr/37.webp)



Wählen Sie als Empfänger "Ashigaru Open Source Project".



![Image](assets/fr/38.webp)



Klicken Sie auf die Schaltfläche "VERBINDEN", um den BIP47-Kommunikationskanal einzurichten (mehr über dieses Protokoll erfahren Sie in der folgenden Anleitung).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Sobald die Transaktion der Benachrichtigung bestätigt wurde, können Sie Ihre Spenden an das Projekt senden, indem Sie auf den kleinen weißen Pfeil in der oberen rechten Ecke der Benutzeroberfläche klicken.



![Image](assets/fr/40.webp)



Sie wissen nun, wie Sie die grundlegenden Funktionen der Ashigaru-Anwendung nutzen können. In zukünftigen Tutorials werden wir uns ansehen, wie Sie die Vorteile der erweiterten Ausgabentransaktionen nutzen können, sowie Whirlpool, die von Samurai Wallet geerbte Coinjoin-Implementierung.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
