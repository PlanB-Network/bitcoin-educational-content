---
name: Jade DIY
description: Verwandeln Sie eine 15-Dollar-Entwicklungsplatine in eine voll funktionsfähige Bitcoin-Hardware wallet
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Einsteigerbau


**Zielgruppe:** Neugierige Bauherren mit wenig bis gar keiner Erfahrung mit eingebetteten Systemen.


**Dauer:** 2 Stunden (flexibel)


**Ergebnisse:** Am Ende des Kurses werden die Studierenden:



- Erkennen Sie das Sicherheitsmodell von DIY-Hardware-Wallets im Vergleich zu kommerziellen Geräten.
- Bauen Sie ein Mikrocontroller-basiertes Signiergerät zusammen.
- Flashen Sie Open-Source-Firmware und überprüfen Sie die Build-Prüfsumme.
- Eine mainnet-Transaktion mit ihrem neuen Gerät unterzeichnen und übertragen.


---

## Abstrakt


In diesem zweistündigen Workshop lernen Anfänger, einen funktionsfähigen Bitcoin-Hardware-wallet zu bauen, indem sie Open-Source-Jade-Firmware auf ein 15-Dollar-LilyGO T-Display-Board flashen. Die Teilnehmer verwandeln generische Entwicklungshardware in ein Signiergerät, das mit kommerziellen Geldbörsen für 150 $ vergleichbar ist, und lernen die Sicherheitsgrundlagen durch praktische Erfahrung und nicht nur durch Theorie.


### Philosophie


Beim Bau eines eigenen Signiergeräts geht es nicht nur darum, Geld zu sparen, sondern auch darum, die Technologie zu verstehen, die Ihr Bitcoin schützt. Dieser Workshop setzt auf "Sicherheit durch Verständnis" statt auf Blackbox-Vertrauen. Durch die Beschaffung von Komponenten, das Flashen von Open-Source-Firmware und die eigene Erzeugung von Entropie verringern die Teilnehmer das Risiko in der Lieferkette und lernen gleichzeitig, Sicherheitsansprüche kritisch zu bewerten. Das Ziel ist informierte Autonomie: Die Teilnehmer sollen sowohl die Möglichkeiten als auch die Grenzen ihres selbstgebauten Geräts im Vergleich zu gehärteten kommerziellen Alternativen verstehen.


---

## Konzept Fibel (15 min)


### Was ist Selbstverwahrung und warum ist sie wichtig?


Bitcoin wurde geschaffen, um die Notwendigkeit vertrauenswürdiger Dritter wie Banken und Unternehmen aus unserem Geldsystem zu entfernen. Anstelle von Vertrauen nutzt Bitcoin Mathematik, Physik und Kryptographie, um jedem die Macht zu geben, sein Geld zu besitzen und zu kontrollieren, ohne die Erlaubnis von jemandem zu benötigen.


Die Art und Weise, wie dies funktioniert, ist, dass bitcoin auf einem globalen digitalen Hauptbuch existiert, das Blockchain genannt wird, auch bekannt als die bitcoin timechain, die ein öffentliches und transparentes Hauptbuch ist, das von Computern geführt wird, anstatt eines zentralisierten Hauptbuchs wie ein Bankkonto.


Um Bitcoin von einem Ort zum anderen zu transferieren, müssen Sie die Transaktion mit einem so genannten privaten Schlüssel signieren. Stellen Sie sich das so vor, als würden Sie einen Tresor mit einem Passwort aufschließen und die Bitcoin in den Tresor einer anderen Person verschieben. Bitcoin gibt Ihnen die Macht, die Schlüssel zu diesem Tresor selbst zu halten, anstatt sich auf eine Bank zu verlassen, die Ihr Geld für Sie bewegt.


Mit großer Macht geht große Verantwortung einher. Wenn Sie Ihre Schlüssel verlieren, ist Ihr Geld für immer weg. Auf diese Weise können Sie sich die Schlüssel zum Tresorraum wie das Geld selbst vorstellen. Schlüssel sind zwar nicht dasselbe wie Bitcoin, aber sie sind der Mechanismus, um Ihr Geld zu bewegen, und daher extrem wichtig zu schützen. Aus diesem Grund sagen wir "nicht Ihre Schlüssel, nicht Ihre Münzen".


Der Begriff Self-Custody mag verwirrend klingen, aber er bedeutet nichts anderes, als dass Sie Ihre eigenen privaten Schlüssel besitzen und Ihre eigenen Bitcoins kontrollieren. Wenn Sie diesen Schlüssel nicht besitzen, vertrauen Sie darauf, dass jemand anderes ihn für Sie verwahrt. Wenn Ihre Bitcoin in einem börsengehandelten Fonds oder an einer Börse (Mt. Gox, FTX, Coinbase, Binance usw.) liegen, besitzen Sie keine Bitcoin, sondern einen Anspruch auf Bitcoin. Dies birgt alle möglichen Risiken, z. B. dass Börsen gehackt werden und Sie Ihre Bitcoin verlieren oder dass Unternehmen Ihr Geld verleihen und Ihnen nur einen Bruchteil als Reserve überlassen. Außerdem hätten vertrauenswürdige Dritte die volle Kontrolle über Ihr Geld und könnten Abhebungen beschränken oder einfrieren.


![image](assets/fr/01.webp)


Mit der Selbstverwahrung nehmen Sie das Vertrauen aus der Gleichung heraus. Niemand kann Ihre Gelder einfrieren oder eine Transaktion verweigern, Sie können Geld über Grenzen hinweg an jeden und zu jeder Zeit senden, und Sie brauchen kein Bankkonto, keinen Ausweis und keine Genehmigung von jemandem. Niemand kann Sie aufhalten, zensieren oder bestehlen, was die volle Macht von Bitcoin als Freiheitsgeld freisetzt. Deshalb sagen wir, dass Sie mit bitcoin Ihre eigene Bank sein können.


Bitcoin wurde geschaffen, um das Problem der Manipulation von Vertrauen und Geld zu lösen, ein Ausstieg aus unserem derzeitigen System, aber der Ausstieg funktioniert nur, wenn man die Schlüssel nimmt. Aus diesem Grund ist die Selbstverwahrung so wichtig.


### Was ist ein Wallet?


Der Begriff wallet ist eine etwas falsche Bezeichnung und kann daher verwirrend sein. Ja, es stimmt, dass ein Bitcoin-wallet, wie ein physischer wallet, Wert speichert. Der Hauptunterschied besteht jedoch darin, dass Bitcoin-Geldbörsen keine Bitcoins speichern.


Bitcoin existiert nur als Ledger-Eintrag in der öffentlichen Blockchain oder in den metaphorischen Tresoren im Cyberspace. Denken Sie daran, um Bitcoin zu verschieben, müssen Sie Ihre Schlüssel verwenden, um den Tresor zu öffnen und die Münzen an einen anderen Ort zu verschieben, die privaten Schlüssel sind das, was verwendet wird, um Bitcoin auszugeben. Wenn Sie eine Transaktion mit Ihrem wallet durchführen, verwenden Sie eigentlich nur Ihre Schlüssel, um die Transaktion zu unterzeichnen. Auf diese Weise zeigen Sie, dass Sie das Geld besitzen und das Recht haben, diese Münzen auszugeben.


Bitcoin-Geldbörsen speichern eigentlich nur Ihre privaten Schlüssel, daher wäre es genauer, sie als Schlüsselbund zu bezeichnen.


### Hot vs. Cold Geldbörsen


Ein Hot wallet ist eine Software-App auf Ihrem Telefon oder Computer. Sie ist mit dem Internet verbunden, so dass sie einfacher zu bedienen ist und Transaktionen schneller unterzeichnet werden können, aber das bedeutet auch, dass sie anfälliger für Hacker, Malware und Phishing ist. Es wird als "heiß" bezeichnet, weil es mit dem Internet verbunden ist, an die Steckdose angeschlossen und eingeschaltet ist. Ein Beispiel wäre ein Telefon wallet oder ein Browser wallet.


Ein kaltes wallet oder Hardware-wallet hingegen ist ein Gerät, das Ihren Schlüssel offline erstellt und speichert. Dies verhindert, dass jemand Ihr Geld hacken kann, und ist viel sicherer für langfristige Ersparnisse. Allerdings ist es ein Gerät, das zum Unterschreiben jeder Transaktion benötigt wird und weniger bequem sein kann.


### Hardware Wallet Bedrohungsmodell


Hardware-Geldbörsen existieren, um ein grundlegendes Problem zu lösen: Wie signiert man Bitcoin-Transaktionen, ohne seine privaten Schlüssel einem mit dem Internet verbundenen Computer auszusetzen, der durch Malware oder Angreifer aus der Ferne kompromittiert werden könnte? Das zentrale Bedrohungsmodell geht davon aus, dass Ihr alltäglicher Laptop oder Ihr Telefon potenziell feindlich ist. Ein Hardware-wallet schafft eine isolierte Umgebung, in der die privaten Schlüssel das Gerät nie verlassen, und die Transaktionssignierung erfolgt in einem secure element oder einem Mikrocontroller, der nur die Signatur zurück an den Host-Computer übermittelt, nicht aber den Schlüssel selbst. Selbst wenn Ihr Computer vollständig kompromittiert ist, kann ein Angreifer Ihr Bitcoin nicht stehlen, ohne physischen Zugriff auf das Gerät und Ihre PIN.


Allerdings bergen Hardware-Geldbörsen ihre eigenen Gefahren. Sie müssen darauf vertrauen, dass der Hersteller keine Hintertüren eingebaut hat, dass die Lieferkette nicht manipuliert wurde und dass die Zufallszahlengenerierung wirklich zufällig ist. Physische Angreifer könnten Schlüssel durch Seitenkanalangriffe oder Chipmanipulationen extrahieren, und jemand mit vorübergehendem Zugang könnte Ihr Gerät verändern. Der Aufbau Ihrer eigenen wallet-Hardware hilft Ihnen, diese Kompromisse zu verstehen - Sie treffen Entscheidungen über sichere Elemente im Vergleich zu Allzweck-Mikrocontrollern, über die Verifizierung von Transaktionen auf einem Display und über den Schutz vor Fern- und physischen Bedrohungen. Das Ziel ist nicht die perfekte Sicherheit, sondern zu verstehen, gegen welche Bedrohungen Sie sich schützen und welche bestehen bleiben.


### Wichtige Konzepte



- Entropie und seed-Sätze:** Ihr wallet ist nur so sicher wie die Zufälligkeit, die es hervorbringt. Wir mischen den Zufallszahlengenerator des Geräts mit menschenfreundlichen Tricks wie Würfelwürfen, wandeln diese Entropie in einen [BIP39-Satz] mit 12 oder 24 Wörtern um (https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) und verlassen den Raum mit einer schriftlichen oder metallenen Sicherung, der Sie vertrauen.
- Seed-Phrase-Hygiene:** Behandeln Sie die seed wie Generalschlüssel zu Ihren Ersparnissen. Geben Sie den Satz niemals in ein Telefon oder einen Computer ein - Keylogger, Screenshots und Cloud-Backups können ihn für immer ausspähen. Bewahren Sie den Satz offline auf, speichern Sie ihn an einem Ort, auf den nur Sie Zugriff haben, und üben Sie, ihn laut vorzulesen, bevor Sie gehen.
- Sicheres Element + Mikrocontroller:** Stellen Sie sich das secure element als den Tresor und den Mikrocontroller als das Hirn vor. Das secure element bewacht die privaten Schlüssel und ist fälschungssicher, während der Mikrocontroller den Bildschirm, die Tasten und die Firmware-Logik steuert. Beachten Sie, dass die Hardware-Geldbörsen, die wir heute bauen, keinen secure element haben. Das bedeutet nicht, dass sie unsicher sind, sondern nur, dass sie eine Schutzstufe weniger haben.
- Vertrauen in die Firmware:** Die Firmware ist das unsichtbare Betriebssystem des wallet. Laden Sie immer von gekennzeichneten Versionen herunter, überprüfen Sie den veröffentlichten Hash und machen Sie sich bewusst, dass reproduzierbare Builds es mehreren Personen ermöglichen, den gleichen Code zu kompilieren und zu genau der gleichen Binärdatei zu gelangen. Wenn die Prüfsumme nicht übereinstimmt, unterschreiben Sie nicht.


---

## Was bauen wir?


Wir nehmen generische Hardware, das LilyGo T-Display, und flashen die Jade SDK-Firmware darauf. Das [Jade Plus](https://blockstream.com/jade/jade-plus/) ist ein Open-Source-wallet, das normalerweise 150 $ kostet:


![image](assets/fr/02.webp)


Heute werden wir stattdessen ihre Firmware auf eine 15-Dollar-Hardware flashen.


### Was man kaufen sollte


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB mit Gehäuse, Modell K164)** - [Bestellen Sie direkt bei LilyGO](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) für etwa $15. Dieses ESP32-Board bietet das Display, die Tasten und die USB-Schnittstelle, die das Jade Plus von Blockstream widerspiegeln. Das ESP32-Board enthält auch Wi-Fi- und Bluetooth-Funkgeräte; wir liefern Firmware, die sie deaktiviert, aber sie bilden Ihr Bedrohungsmodell, da bösartiger Code sie wieder einschalten könnte.
- USB-C-Kabel** - Bringen Sie ein datenfähiges Kabel mit, damit Sie Firmware flashen und das Board direkt von Ihrem Laptop aus mit Strom versorgen können (für den Unterricht völlig ausreichend).


### Warum sollten Sie Ihren eigenen Hardware Wallet bauen?



- Sparen Sie rund 135 Dollar gegenüber dem Kauf eines handelsüblichen Geräts.
- Erhöhen Sie den Komfort mit flashender Firmware, sicheren Elementen und wallet-Hygiene.
- Richten Sie zusätzliche Signiergeräte ein, um die Einsparungen auf mehrere Geldbörsen zu verteilen.
- Reduzieren Sie das Risiko in der Lieferkette, indem Sie alle Komponenten selbst beschaffen und montieren.
- Denken Sie an das Mantra von Lopp: Souveränität und Bequemlichkeit stehen immer im Widerspruch zueinander.


## Physikalische Einrichtung


### Bereiten Sie Ihren Fall vor


Sie haben zwei Möglichkeiten, Ihr LilyGO T-Display Board unterzubringen: ein 3D-gedrucktes Gehäuse oder das offizielle LilyGO-Gehäuse. Das gedruckte Gehäuse können Sie bei [dieses Modell](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure) finden und drucken lassen. Es bietet eine leichte und anpassbare Hülle für Ihr Gerät.


![image](assets/fr/04.webp)


Alternativ können Sie auch das offizielle LilyGO-Gehäuse verwenden, das eine etwas andere Passform und Verarbeitung aufweist und einen robusteren Schutz sowie ein poliertes Aussehen bietet.


![image](assets/fr/05.webp)


Beachten Sie, dass sich das gedruckte und das offizielle Gehäuse in Design und Montage leicht unterscheiden. Unabhängig davon, welche Option Sie wählen, stellen Sie sicher, dass die Platine richtig im Gehäuse sitzt, um lose Verbindungen oder Schäden zu vermeiden.


### Prüfen Sie den Vorstand


Bevor Sie fortfahren, untersuchen Sie Ihre LilyGO T-Display-Platine sorgfältig auf sichtbare Defekte oder Verschmutzungen. Prüfen Sie, ob das Display, die Tasten und der USB-C-Anschluss sauber und frei von Staub oder Lötspritzern sind. Gehen Sie vorsichtig mit der Platine um und achten Sie auf elektrostatische Entladung (ESD), indem Sie sich erden oder ein ESD-Armband verwenden, um Schäden an empfindlichen Komponenten zu vermeiden.


### Anschließen an Ihren Laptop


Verbinden Sie die LilyGO-Platine über ein datenfähiges USB-C-Kabel mit Ihrem Laptop. Diese Verbindung liefert Strom und ermöglicht es Ihnen, die Firmware zu flashen.


Beim Hochfahren wird der folgende Bildschirm eingeblendet:


![image](assets/fr/06.webp)



Nach dem Einschalten zeigt der LilyGO einen Farbtestbildschirm an, der durch die einzelnen Farben geht. Dies bestätigt, dass das Display und die Platine korrekt funktionieren, bevor die Firmware geflasht wird.


Sobald der Farbtest abgeschlossen ist, wechselt der Bildschirm in einen Standardzustand, der anzeigt, dass das Board für die nächsten Schritte im Bauprozess bereit ist.


![image](assets/fr/07.webp)


## Der einfache Weg oder der Hard Weg


Es gibt zwei Hauptansätze für das Flashen Ihrer wallet-Firmware: den einfachen und den schwierigen Weg. Der einfache Weg verwendet vorkonfigurierte Tools oder webbasierte Flashers, die die Firmware mit minimalen Eingaben automatisch auf Ihr Gerät laden. Diese Methode ist ideal für Anfänger, die einen schnellen Erfolg erzielen oder die Komplexität von Debugging und Befehlszeileninteraktionen vermeiden möchten. Sie vereinfacht den Prozess und beschleunigt die Inbetriebnahme, so dass sie auch für Einsteiger in die Embedded-Entwicklung oder Hardware-Wallets geeignet ist.


Der harte Weg hingegen beinhaltet die manuelle Verwendung von Befehlszeilentools zum Flashen der Firmware. Bei diesem Ansatz müssen Firmware-Signaturen und Prüfsummen verifiziert werden, um die Authentizität und Integrität sicherzustellen, was Ihnen ein tieferes Verständnis des Flash-Prozesses und der Interaktion zwischen Firmware und Hardware ermöglicht. Dies erfordert zwar mehr Aufwand und Vertrautheit mit Terminalbefehlen, bietet aber mehr Kontrolle, Transparenz und Vertrauen in die Sicherheit Ihres Geräts.


Jede Methode hat ihre Nachteile: Der einfache Weg opfert ein gewisses Maß an Vertrauen und Verständnis für Geschwindigkeit und Bequemlichkeit, während der schwierige Weg mehr Zeit und technisches Geschick erfordert, aber mit Flexibilität und einem besseren Verständnis der zugrunde liegenden Technologie belohnt. Die Ausbilder sollten die Schüler dazu ermutigen, den Weg zu wählen, der ihrem Wohlbefinden und ihrer Neugierde am besten entspricht, um sowohl das Vertrauen als auch die Entdeckungsfreude zu fördern.


## Der einfache Weg


Der einfachste Weg, einen ESP32 zu flashen



- Besuchen Sie das offizielle Blockstream Github: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Sie können die Quelldatei herunterladen und die Website lokal ausführen, aber GitHub hostet sie bereits unter [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub stellt HTML, CSS, JavaScript usw. direkt in Ihrem Browser bereit, sodass Sie das Gerät flashen können, ohne Entwickler-Tools zu installieren.


![image](assets/fr/09.webp)



- Öffnen Sie das Dropdown-Menü (es ist wahrscheinlich auf "M5Stack Core2" voreingestellt) und wählen Sie Ihr Entwicklungsboard aus - für diese Klasse wählen Sie "LILYGO T-Display".


![image](assets/fr/10.webp)



- Wenn Sie auf blinken klicken, wird dies angezeigt. Um zu wissen, welches Gerät der LILYGO ist, ziehen Sie den Lilygo ab und stecken Sie ihn wieder ein. Der COM-Port, an dem der Lilygo angeschlossen ist, wird angezeigt und verschwindet wieder. Klicken Sie auf den COM-Port, an den die Jade angeschlossen ist


![image](assets/fr/11.webp)



- Es sollte ein Fortschrittsbalken angezeigt werden, und wenn er fertig ist, können Sie ihn einrichten


## Aufstellen des Jade Wallet


Sobald die Firmware erfolgreich geflasht wurde, ist Ihr LilyGO T-Display nun ein voll funktionsfähiges Jade-Hardware-wallet. Dieser Abschnitt führt Sie durch den anfänglichen Einrichtungsprozess, von der Erstellung Ihrer seed Phrase bis zur Verbindung des Geräts mit der wallet Software wie Sparrow oder der Blockstream Green Mobile App.


### Erstes Booten und Geräte-Setup



- Schalten Sie das Gerät ein:** Wenn der LilyGO noch über USB-C mit Ihrem Laptop verbunden ist, sollte die Jade-Firmware automatisch starten. Sie sehen das Jade-Logo auf dem Display erscheinen.



- Aufrufen des Einrichtungsmodus:** Das Gerät zeigt Ihnen ein Startmenü an. Verwenden Sie die beiden physischen Tasten auf der Platine, um zu navigieren:
 - Linke Taste:** Nach oben/zurück bewegen
 - Rechte Taste:** Nach unten/vorwärts bewegen
 - Beide Tasten gleichzeitig:** Auswählen/Bestätigen



- Wählen Sie "Setup":** Navigieren Sie zu der Option "Setup" und drücken Sie beide Tasten zur Bestätigung. Das Gerät führt Sie durch den anfänglichen Konfigurationsprozess.


### Erstellen Ihres Wallet



- Wählen Sie "Einrichtung beginnen":** Das Gerät wird Sie auffordern, mit der Erstellung des wallet zu beginnen. Bestätigen Sie Ihre Auswahl.



- Wählen Sie "Neues Wallet erstellen":** Es werden Ihnen zwei Optionen angeboten:
 - Neue Wallet erstellen:** Erzeugt einen neuen seed-Satz (wählen Sie diesen für den Workshop)
 - Wallet wiederherstellen:** Wiederherstellung eines vorhandenen wallet aus einem seed-Satz (für fortgeschrittene Benutzer)



- Wählen Sie "Neues Wallet erstellen" und bestätigen Sie.



- Entropie generieren:** Das Gerät verwendet seinen Zufallszahlengenerator, um kryptografische Entropie zu erzeugen. Dieser Vorgang dauert einige Sekunden, da das Gerät Zufallszahlen aus mehreren Quellen sammelt.


### Aufzeichnung Ihrer Seed Phrase



- Schreiben Sie Ihren seed-Satz auf:** Das Gerät zeigt nun einen BIP39 seed-Satz mit 12 Wörtern an, ein Wort nach dem anderen. Dies ist der wichtigste Schritt des gesamten Prozesses.


**Wichtige Sicherheitspraktiken:**


- Schreiben Sie jedes Wort deutlich auf Papier (verwenden Sie die mitgelieferten seed-Satzkarten, falls vorhanden)
- Überprüfen Sie jedes Wort, während Sie es schreiben
- Fotografieren Sie den seed-Satz niemals mit Ihrem Handy
- Geben Sie die Wörter niemals in einen Computer oder ein Telefon ein
- Behalten Sie Ihren seed-Satz für sich - teilen Sie Ihren Bildschirm nicht und zeigen Sie ihn nicht anderen



- Überprüfen Sie Ihren seed-Satz:** Nachdem Sie alle 12 Wörter aufgeschrieben haben, fordert das Gerät Sie auf, mehrere Wörter des Satzes zu bestätigen, um sicherzustellen, dass Sie sie richtig aufgenommen haben. Verwenden Sie die Tasten, um das richtige Wort für jede Aufforderung auszuwählen.


**Pro-Tipp:** Bevor Sie weitermachen, üben Sie, sich Ihren seed-Satz laut vorzulesen (leise, so dass andere Sie nicht hören können). Auf diese Weise können Sie eventuelle Schreibfehler oder Unklarheiten erkennen.


### Verbindung Methode



- Verbindungsart wählen:** Die Jade-Firmware unterstützt zwei Verbindungsmethoden:
 - USB:** Kabelgebundene Verbindung über USB-C-Kabel (für diesen Workshop empfohlen)
 - Bluetooth:** Drahtlose Verbindung zu mobilen Geräten



- Wählen Sie vorerst **USB**, da dies die einfachste Option für Desktop-wallet-Software ist und keine drahtlosen Angriffsvektoren einführt.



- Gerätebezeichnung:** Der Jade zeigt eine eindeutige Kennung wie "Connect Jade A7D924" an. Diese Kennung hilft Ihnen bei der Unterscheidung zwischen mehreren Hardware-Geldbörsen, wenn Sie mehr als eine bauen. Notieren Sie sich diese Kennung, falls gewünscht.


### Verbindung zur Wallet-Software


Sie haben nun zwei Hauptoptionen für die Verbindung mit Ihrer neu erstellten Hardware wallet: die Blockstream Green Mobile App (für den Einsatz unterwegs) oder Sparrow Wallet (für den Einsatz auf dem Desktop mit erweiterten Funktionen). In diesem Workshop werden wir uns auf Sparrow Wallet konzentrieren, da es einen besseren Einblick in die technischen Details von Bitcoin-Transaktionen bietet.


#### Option 1: Blockstream Green Mobile App (Schnellstart)


Wenn Sie Ihr Gerät schnell mit einem mobilen Gerät testen möchten:



- Laden Sie die **Blockstream Green** App aus dem App Store (iOS) oder Google Play (Android) herunter
- Öffnen Sie die App und wählen Sie "Hardware Wallet verbinden"
- Wählen Sie "Jade" aus der Liste der unterstützten Geräte
- Schließen Sie Ihren Jade mit einem USB-C-auf-USB-C-Kabel an Ihr Telefon an (oder mit einem USB-C-auf-Lightning-Adapter für iPhone 15+)
- Folgen Sie den Anweisungen auf dem Bildschirm, um eine Verbindung herzustellen und Ihr erstes wallet zu erstellen


**Hinweis zu Liquid:** Die Blockstream Green-App unterstützt sowohl Bitcoin als auch Liquid (eine Bitcoin-Sidechain). Wenn Sie Liquid-Funktionen verwenden, werden Sie möglicherweise aufgefordert, den "Master Blinding Key" zu exportieren - dadurch kann die App Transaktionsbeträge im Liquid-Netzwerk sehen, die ansonsten vertraulich sind. Für diesen Workshop können Sie die Liquid-Funktionen auslassen und sich auf Standard-Bitcoin-Transaktionen konzentrieren.


#### Option 2: Sparrow Wallet (empfohlen für Werkstatt)


Sparrow Wallet ist eine leistungsstarke Desktop-Anwendung, die Ihnen eine genaue Kontrolle über Ihre Bitcoin-Transaktionen ermöglicht und nahtlos mit Ihrer Jade Hardware wallet verbunden werden kann.


**Installation:**



- Laden Sie Sparrow Wallet von der offiziellen Website herunter: [sparrowwallet.com](https://sparrowwallet.com)
- Überprüfen Sie die Download-Signatur (Einzelheiten finden Sie in der Sparrow-Dokumentation)
- Installieren und starten Sie die Anwendung


**Verbinden Sie Ihre Jade mit Sparrow:**



- Gehen Sie in Sparrow auf **Datei → Neue Wallet**
- Geben Sie Ihrem wallet einen Namen (z. B. "Mein Jade Wallet")
- Klicken Sie auf **Verbundener Hardware Wallet**
- Das Sparrow sollte Ihr angeschlossenes Jade-Gerät automatisch erkennen
- Wenn Sie dazu aufgefordert werden, bestätigen Sie die Verbindung auf dem Jade-Display durch Drücken beider Tasten
- Wählen Sie den gewünschten Skripttyp:
 - Native Segwit (P2WPKH):** Empfohlen für Anfänger - niedrigste Gebühren, größtmögliche Kompatibilität mit modernen Wallets
 - Nested Segwit (P2SH-P2WPKH):** Für die Kompatibilität mit älteren Diensten
 - Taproot (P2TR):** Am fortschrittlichsten, bietet den besten Datenschutz und die niedrigsten Gebühren, erfordert jedoch eine hochmoderne wallet-Unterstützung
- Klicken Sie auf **Schlüsselspeicher importieren**, um die Verbindung herzustellen


**Konfiguration der Serververbindung von Sparrow:**


Bevor Sie Ihren Kontostand einsehen oder Transaktionen übertragen können, muss Sparrow eine Verbindung zu einem Bitcoin-Knoten herstellen, um Blockchain-Daten abzurufen. Sie haben mehrere Optionen, die jeweils unterschiedliche Kompromisse zwischen Bequemlichkeit, Datenschutz und Vertrauen beinhalten:



- Öffentliches Electrum Server (am einfachsten, am wenigsten privat):** Stellt eine Verbindung zu einem öffentlichen Server her, der von einer dritten Partei betrieben wird. Schnell einzurichten, aber der Server kann die Adressen Ihres wallet sehen und sie möglicherweise mit Ihrer IP-Adresse verknüpfen. Gut für Tests im Testnetz.
 - In Sparrow gehen Sie zu **Tools → Einstellungen → Server**
 - Wählen Sie **Öffentlicher Server** und wählen Sie einen Server aus der Liste
 - Klicken Sie auf **Verbindung testen**, um zu überprüfen



- Bitcoin Core oder Knots Node (am meisten privat, am meisten Arbeit):** Betreiben Sie Ihren eigenen vollständigen Bitcoin Node. Dies ist der Goldstandard für Privatsphäre und Verifizierung, da Sie jede Transaktion selbst validieren und nicht dem Server eines anderen vertrauen. Es erfordert jedoch das Herunterladen der gesamten Blockchain (~600 GB) und die Synchronisierung Ihres Knotens.
 - Installieren und Synchronisieren von Bitcoin Core oder Knots
 - In Sparrow gehen Sie zu **Tools → Einstellungen → Server**
 - Wählen Sie **Bitcoin Core oder Knots** und geben Sie die Verbindungsdaten Ihres Knotens ein



- Privates Electrum Server (gutes Gleichgewicht):** Hosten Sie Ihren eigenen Electrum-Server (wie Fulcrum oder Electrs), der mit Ihrem Bitcoin Core- oder Knots-Knoten verbunden ist. Bietet volle Privatsphäre, ohne dass Sie Sparrow auf demselben Rechner wie Ihren Knoten ausführen müssen.
 - Richten Sie einen Electrum-Server ein, der auf Ihren Bitcoin Core- oder Knots-Knoten verweist
 - Gehen Sie im Sparrow zu **Tools → Einstellungen → Server**
 - Wählen Sie **Private Electrum** und geben Sie die URL Ihres Servers ein


Für diesen Workshop ist die Verwendung eines **öffentlichen Electrum Server** für Testnetz-Transaktionen vollkommen ausreichend. In einer Produktionsumgebung mit echtem Geld sollten Sie einen eigenen Knotenpunkt oder einen vertrauenswürdigen privaten Server für maximalen Datenschutz in Betracht ziehen.


#### Option 3: Blockstream Green Desktop App (Schnellstart)


Blockstream Green ist die Software, mit der die Einrichtung von JadeDIY abgeschlossen wird und die mit der Desktop-Version geliefert werden muss



- Holen Sie sich die offizielle Blockstream-Anwendung - dies ist der Link dazu auf der Website des Unternehmens. Wenn Sie dort sind, klicken Sie auf [Jetzt herunterladen](https://blockstream.com/app/).


![image](assets/fr/12.webp)



- Je nachdem, wo Sie Ihre Downloads ablegen, befindet sich die Datei höchstwahrscheinlich in Ihrem Downloads-Ordner. Schauen Sie dort nach und doppelklicken Sie auf die ausführbare Datei, um die Software zu installieren.


![image](assets/fr/13.webp)



- Möglicherweise müssen Sie Administratorrechte vergeben, um das Installationsprogramm auszuführen. Danach öffnet sich ein Fenster, das wie das folgende Bild aussieht - klicken Sie auf **Weiter**.


![image](assets/fr/14.webp)



- Wählen Sie aus, wo die installierte Anwendung gespeichert werden soll (an einem Ort mit Ihren anderen Programmen oder an einem leicht zu findenden Ort), und klicken Sie dann auf **Weiter**.


![image](assets/fr/15.webp)



- Das Installationsprogramm fragt nach einem Verknüpfungsnamen. Geben Sie einen Namen ein oder behalten Sie den Standardnamen bei und klicken Sie dann auf **Weiter**.


![image](assets/fr/16.webp)



- Wenn Sie eine Desktop-Verknüpfung wünschen, markieren Sie das Kästchen; andernfalls klicken Sie auf **Weiter**.


![image](assets/fr/17.webp)



- Klicken Sie abschließend auf **Installieren** und warten Sie ein paar Minuten, bis die Installation abgeschlossen ist.


![image](assets/fr/18.webp)



- Der Fortschrittsbalken sollte sich bis zum Ende füllen.


![image](assets/fr/19.webp)



- Nach Abschluss des Vorgangs wird eine neue Seite angezeigt - klicken Sie auf **Finish**.


![image](assets/fr/20.webp)



- Suchen Sie Ihre neu installierte Blockstream-Anwendung (Beispiel im Startmenü von Windows 11).


![image](assets/fr/21.webp)



- Sobald Sie es gefunden haben, klicken Sie zum Starten darauf - ein Startbildschirm sollte erscheinen.


### Überprüfen Ihrer Einrichtung


Sobald Sie mit Sparrow (oder einer anderen wallet-Anwendung) verbunden sind:



- Überprüfen Sie Ihre Adressen:** Das Sparrow zeigt Empfangsadressen an, die von Ihrem seed-Satz abgeleitet sind. Sie können eine Adresse auf Ihrem Jade-Gerät überprüfen, indem Sie in Sparrow auf die Registerkarte "Empfangen" gehen und auf "Address anzeigen" klicken - die Adresse sollte sowohl auf Ihrem Computerbildschirm als auch auf dem Jade-Display erscheinen.



- Generieren Sie eine Empfangsadresse:** Klicken Sie in Sparrow auf die Registerkarte **Empfangen** und kopieren Sie Ihre erste Bitcoin-Empfangsadresse.



- Bereit für Transaktionen:** Ihre Hardware wallet ist nun vollständig konfiguriert und bereit, Bitcoin-Transaktionen zu empfangen und zu unterzeichnen. Fahren Sie mit dem nächsten Abschnitt fort, um das Signieren einer Testnetz-Transaktion zu üben.



---

### Checkliste für die Schnelleinrichtung



- Jade-Firmware bootet erfolgreich
- Neuer wallet mit 12-Wort-seed-Satz erstellt
- Saatgutsatz deutlich aufgeschrieben und überprüft
- USB-Verbindungsmodus ausgewählt
- Wallet-Software (Sparrow) installiert und angeschlossen
- Serververbindung konfiguriert (öffentlicher Electrum für mainnet)
- Erste Empfangsadresse generiert und im Gerät verifiziert



---

**MIT-Lizenz**


**Copyright (c) 2025 Das Bitcoin Netzwerk NYC**


Hiermit wird jeder Person, die eine Kopie dieser Software und der zugehörigen Dokumentationsdateien (die "Software") erwirbt, kostenlos die Erlaubnis erteilt, uneingeschränkt mit der Software zu handeln, einschließlich und ohne Einschränkung der Rechte, Kopien der Software zu verwenden, zu kopieren, zu modifizieren, zusammenzuführen, zu veröffentlichen, zu vertreiben, zu unterlizenzieren und/oder zu verkaufen, und Personen, denen die Software zur Verfügung gestellt wird, dies zu gestatten, vorbehaltlich der folgenden Bedingungen:


Der obige Copyright-Hinweis und dieser Genehmigungshinweis müssen in allen Kopien oder wesentlichen Teilen der Software enthalten sein.


DIE SOFTWARE WIRD OHNE MÄNGELGEWÄHR UND OHNE JEGLICHE AUSDRÜCKLICHE ODER STILLSCHWEIGENDE GARANTIE ZUR VERFÜGUNG GESTELLT, EINSCHLIESSLICH, ABER NICHT BESCHRÄNKT AUF DIE GARANTIE DER MARKTGÄNGIGKEIT, DER EIGNUNG FÜR EINEN BESTIMMTEN ZWECK UND DER NICHTVERLETZUNG VON RECHTEN. UNTER KEINEN UMSTÄNDEN SIND DIE AUTOREN ODER URHEBERRECHTSINHABER HAFTBAR FÜR JEGLICHE ANSPRÜCHE, SCHÄDEN ODER ANDERE HAFTUNGEN, SEI ES IM RAHMEN EINES VERTRAGS, EINER UNERLAUBTEN HANDLUNG ODER ANDERWEITIG, DIE SICH AUS DER SOFTWARE ODER DER NUTZUNG ODER DEM SONSTIGEN UMGANG MIT DER SOFTWARE ERGEBEN ODER DAMIT ZUSAMMENHÄNGEN.


---