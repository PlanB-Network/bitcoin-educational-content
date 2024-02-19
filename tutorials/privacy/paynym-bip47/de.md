---
name: BIP47 - PayNym

description:: Wie PayNym funktioniert
---

> "Es ist zu groß", sagten sie alle, und der Truthahn, der mit Sporen geboren wurde und sich für einen Kaiser hielt, blähte sich wie ein Schiff mit vollen Segeln auf und ging mit großer Wut und roten Augen direkt auf ihn zu. Das arme Entlein wusste nicht, ob es stehen bleiben oder weitergehen sollte: Es war sehr traurig, von allen Enten im Hof verspottet zu werden.

![BIP47, das hässliche Entlein Illustration](assets/1.webp)

Eine der größten Herausforderungen im Bitcoin-Protokoll ist die Wiederverwendung von Adressen. Die Transparenz und die Verteilung des Netzwerks machen diese Praxis gefährlich für die Privatsphäre des Benutzers. Um Probleme damit zu vermeiden, wird empfohlen, für jede neue eingehende Zahlung an eine Brieftasche eine neue leere Empfangsadresse zu verwenden, was in einigen Fällen kompliziert sein kann.

Dieser Kompromiss ist so alt wie das White Paper. Satoshi hat uns bereits in seinem Ende 2008 veröffentlichten Werk vor diesem Risiko gewarnt:

> "Als zusätzliche Firewall könnte für jede Transaktion ein neues Schlüsselpaar verwendet werden, um sie nicht mit einem gemeinsamen Eigentümer zu verbinden."

Es gibt viele Lösungen, um mehrere Zahlungen zu empfangen, ohne die Adresse wiederzuverwenden. Jede Lösung hat ihre eigenen Kompromisse und Nachteile. Eine dieser Lösungen ist BIP47, ein Vorschlag von Justus Ranvier, der 2015 veröffentlicht wurde und es ermöglicht, wiederverwendbare Zahlungscodes zu generieren. Das Ziel ist es, mehrere Transaktionen an dieselbe Person durchzuführen, ohne dabei die Adresse wiederzuverwenden.

Anfangs wurde dieser Vorschlag von einem Teil der Community verachtet und wurde nie zu Bitcoin Core hinzugefügt. Einige Softwareprogramme haben sich jedoch dafür entschieden, ihn auf eigene Faust zu implementieren. So hat [Samourai Wallet](https://samouraiwallet.com/) seine eigene Implementierung von BIP47 entwickelt: PayNym. Heute ist diese Implementierung natürlich auf Samourai Wallet für Smartphones verfügbar, aber auch auf [Sparrow Wallet](https://sparrowwallet.com/) für PCs.

Im Laufe der Zeit hat Samourai neue Funktionen entwickelt, die direkt mit PayNym verbunden sind. Es gibt jetzt ein ganzes Ökosystem von Tools, die auf PayNym und BIP47 basieren und die Privatsphäre des Benutzers optimieren.
In diesem Artikel erfahren Sie das Prinzip von BIP47 und PayNym, die Mechanismen dieser Protokolle und die daraus resultierenden praktischen Anwendungen. Ich werde nur auf die erste Version von BIP47 eingehen, die derzeit für PayNym verwendet wird, aber die Versionen 2, 3 und 4 funktionieren praktisch auf die gleiche Weise.

> Der einzige wesentliche Unterschied liegt in der Benachrichtigungstransaktion. Version 1 verwendet eine einfache Adresse mit OP_RETURN für die Benachrichtigung, Version 2 verwendet ein Multisig-Skript (Bloom-Multisig) mit OP_RETURN und Version 3 und 4 verwenden einfach ein Multisig-Skript (Cfilter-Multisig). Die in diesem Artikel behandelten Mechanismen, insbesondere die untersuchten kryptographischen Methoden, sind daher auf alle vier Versionen anwendbar. Die PayNym-Implementierung in der Samourai Wallet und Sparrow verwendet derzeit die erste Version von BIP47.

## Inhaltsverzeichnis:

1- Das Problem der Adresswiederverwendung.

2- Prinzipien von BIP47 und PayNym.

3- Tutorials: Verwendung von PayNym.

- Erstellen einer BIP47-Transaktion mit der Samourai Wallet.

- Erstellen einer BIP47-Transaktion mit der Sparrow Wallet.

4- Die Mechanismen von BIP47.

- Der wiederverwendbare Zahlungscode.
- Die kryptographische Methode: Der Diffie-Hellman-Schlüsselaustausch auf elliptischen Kurven (ECDH).

- Die Benachrichtigungstransaktion.
- Erstellen der Benachrichtigungstransaktion.
- Empfang der Benachrichtigungstransaktion.
- Die BIP47-Zahlungstransaktion.
- Empfang der BIP47-Zahlung und Ableitung des privaten Schlüssels.
- Rückerstattung der BIP47-Zahlung.

5- Abgeleitete Verwendungen von PayNym.

6- Meine persönliche Meinung zu BIP47.

## Das Problem der Adresswiederverwendung.

Eine Empfangsadresse wird verwendet, um Bitcoins zu empfangen. Sie wird aus einem öffentlichen Schlüssel generiert, indem er gehasht und einem spezifischen Format unterzogen wird. Dadurch wird eine neue Ausgabebeschränkung für eine Münze erstellt, um den Eigentümer zu ändern.

> Um mehr über die Generierung einer Empfangsadresse zu erfahren, empfehle ich Ihnen, den letzten Teil dieses Artikels zu lesen: Das Bitcoin-Wallet - Auszug aus dem eBook "Demokratisiertes Bitcoin 2" [ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).

Darüber hinaus haben Sie sicherlich schon von einem erfahrenen Bitcoin-Benutzer gehört, dass Empfangsadressen nur einmal verwendet werden sollten und dass Sie daher für jede neue eingehende Zahlung in Ihre Brieftasche eine neue Adresse generieren sollten. Aber warum?
Grundsätzlich gefährdet die Wiederverwendung von Adressen Ihre Gelder nicht direkt. Die Verwendung von Kryptographie auf elliptischen Kurven ermöglicht es, dem Netzwerk nachzuweisen, dass Sie im Besitz eines privaten Schlüssels sind, ohne diesen Schlüssel preiszugeben. Sie können also mehrere verschiedene UTXOs auf derselben Adresse sperren und zu verschiedenen Zeitpunkten ausgeben. Wenn Sie den privaten Schlüssel, der mit dieser Adresse verbunden ist, nicht preisgeben, kann niemand auf Ihre Gelder zugreifen. Das Problem bei der Wiederverwendung von Adressen betrifft eher die Privatsphäre.

Wie bereits eingeführt, ermöglichen die Transparenz und die dezentrale Natur des Bitcoin-Netzwerks jedem Benutzer, der Zugriff auf einen Knoten hat, die Beobachtung der Transaktionen des Zahlungssystems. Dadurch kann er die verschiedenen Guthaben der Adressen sehen. Satoshi Nakamoto erwähnte die Möglichkeit, neue Schlüsselpaare und damit neue Adressen für jede eingehende Zahlung an eine Brieftasche zu generieren. Das Ziel wäre, eine zusätzliche Firewall zu haben, falls eine Verbindung zwischen der Identität des Benutzers und einem seiner Schlüsselpaare hergestellt wird.

Heutzutage ist die Verwendung von leeren Adressen aufgrund von Chain-Analyseunternehmen und der Entwicklung von KYC keine zusätzliche Firewall mehr, sondern eine Verpflichtung für jeden, der sich um seine Privatsphäre kümmert.

Die Suche nach Privatsphäre ist kein Komfort oder Fantasie eines maximalistischen Bitcoiners. Es handelt sich um einen spezifischen Parameter, der direkt Ihre persönliche Sicherheit und die Sicherung Ihrer Gelder betrifft. Um Ihnen das zu verdeutlichen, hier ein sehr konkretes Beispiel:

- Bob kauft Bitcoin im DCA (Dollar-Cost-Averaging)-Verfahren, d.h. er erwirbt regelmäßig eine kleine Menge Bitcoin, um den Einstiegspreis zu glätten. Bob sendet die gekauften Gelder systematisch an dieselbe Empfangsadresse. Er kauft jede Woche 0,01 Bitcoin und sendet sie an diese Adresse. Nach zwei Jahren hat Bob einen ganzen Bitcoin auf dieser Adresse angesammelt.

- Der Bäcker an der Ecke akzeptiert Bitcoin-Zahlungen. Bob ist glücklich, Bitcoin ausgeben zu können, und geht, um sein Baguette in Satoshis zu kaufen. Um zu bezahlen, verwendet er die mit seiner Adresse gesperrten Gelder. Sein Bäcker weiß nun, dass er einen Bitcoin besitzt. Dieser hohe Betrag könnte Neider anziehen, und Bob könnte potenziell einem physischen Angriff ausgesetzt sein.

Die Wiederverwendung von Adressen ermöglicht es einem Beobachter, eine unbestreitbare Verbindung zwischen Ihren verschiedenen UTXOs und manchmal zwischen Ihrer Identität und Ihrer gesamten Brieftasche herzustellen.
Aus diesem Grund generieren die meisten Bitcoin Wallet-Software automatisch eine neue Empfangsadresse, wenn Sie auf die Schaltfläche "Empfangen" klicken. Für den durchschnittlichen Benutzer ist es daher kein großes Problem, sich daran zu gewöhnen, leere Adressen zu verwenden. Für einen Online-Shop, eine Börse oder eine Spendenkampagne kann diese Einschränkung jedoch schnell untragbar werden.
Es gibt viele Lösungen für diese Organisationen. Jede von ihnen hat ihre Vor- und Nachteile, aber bisher und wie wir später sehen werden, unterscheidet sich BIP47 wirklich von den anderen.

Dieses Problem der Adresswiederverwendung ist bei Bitcoin keineswegs unbedeutend. Wie Sie auf dem untenstehenden Diagramm von der Website [oxt.me](http://oxt.me/) sehen können, beträgt die Gesamt-Wiederverwendungsrate von Bitcoin-Adressen derzeit 52%:
Diagramm von OXT.me zur Entwicklung der Gesamt-Wiederverwendungsrate von Adressen im Bitcoin-Netzwerk.

![image](assets/2.webp)

Kredit: https://oxt.me/charts

Der Großteil dieser Wiederverwendungen stammt von Börsen, die aus Effizienz- und Bequemlichkeitsgründen dieselbe Adresse mehrmals verwenden. BIP47 wäre bisher die beste Lösung, um dieses Phänomen bei Börsen einzudämmen. Dadurch könnte die Gesamt-Wiederverwendungsrate von Adressen gesenkt werden, ohne dabei zu viele Reibungsverluste für diese Einrichtungen zu verursachen.

Diese globale Maßnahme im gesamten Netzwerk ist in diesem Fall besonders sinnvoll. Die Adresswiederverwendung ist nicht nur ein Problem für die Person, die diese Praxis durchführt, sondern auch für alle Personen, die Transaktionen mit dieser Person durchführen. Der Verlust der Privatsphäre bei Bitcoin wirkt wie ein Virus und verbreitet sich von Benutzer zu Benutzer. Die Untersuchung einer globalen Maßnahme für alle Transaktionen im Netzwerk ermöglicht es uns, das Ausmaß dieses Phänomens zu erkennen.

## Prinzipien von BIP47 und PayNym.

BIP47 zielt darauf ab, eine einfache Möglichkeit zu bieten, mehrere Zahlungen zu erhalten, ohne die Adresse wiederzuverwenden. Es basiert auf der Verwendung eines wiederverwendbaren Zahlungscodes.

Auf diese Weise können mehrere Sender mehrere Zahlungen an einen einzigen wiederverwendbaren Zahlungscode eines anderen Benutzers senden, ohne dass der Empfänger für jede neue Transaktion eine neue leere Adresse übermitteln muss.

Ein Benutzer kann dann seinen Zahlungscode frei kommunizieren (in sozialen Netzwerken, auf seiner Website...) ohne das Risiko eines Verlusts der Privatsphäre, im Gegensatz zu einer herkömmlichen Empfangsadresse oder einem öffentlichen Schlüssel.
Um einen Austausch durchzuführen, müssen beide Benutzer über eine Bitcoin-Wallet mit einer Implementierung des BIP47 verfügen, wie z.B. PayNym auf Samourai Wallet oder Sparrow Wallet. Die Verknüpfung der Zahlungscodes der beiden Benutzer ermöglicht die Einrichtung eines geheimen Kanals zwischen ihnen. Um diesen Kanal ordnungsgemäß einzurichten, muss der Absender eine Transaktion auf der Bitcoin-Blockchain durchführen: die Benachrichtigungstransaktion (dazu komme ich später).

Die Verknüpfung der Zahlungscodes der beiden Benutzer erzeugt gemeinsame Geheimnisse, die wiederum eine große Anzahl von eindeutigen Bitcoin-Empfangsadressen generieren (genau 2^32). Daher wird die Zahlung mit BIP47 tatsächlich nicht an den Zahlungscode gesendet, sondern an ganz normale Adressen, die aus den Zahlungscodes der Beteiligten abgeleitet werden.

Der Zahlungscode fungiert also als virtuelle Kennung, die aus dem Wallet-Samen abgeleitet wird. In der HD-Wallet-Derivationsstruktur befindet sich der Zahlungscode in Tiefe 3, auf der Wallet-Kontoebene.

![image](assets/3.webp)

Sein Ableitungszweck wird mit 47' (0x8000002F) in Bezug auf das BIP47 gekennzeichnet. Ein Ableitungspfad für einen wiederverwendbaren Zahlungscode wäre zum Beispiel:

> m/47'/0'/0'/

Damit Sie sich vorstellen können, wie ein Zahlungscode aussieht, hier ist meiner:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Dieser kann auch als QR-Code codiert werden, um die Kommunikation zu erleichtern:

![image](assets/4.webp)

Was die PayNym Bots betrifft, diese Roboter, die man auf Twitter sieht, sind sie einfach visuelle Darstellungen Ihres Zahlungscodes, die von Samourai Wallet erstellt werden. Sie werden durch eine Hash-Funktion erzeugt, was sie nahezu einzigartig macht. Hier ist meiner mit seiner Kennung:

> +throbbingpond8B1

![image](assets/5.webp)

Diese Bots haben keine echte technische Verwendung. Stattdessen erleichtern sie die Interaktion zwischen den Benutzern, indem sie eine virtuelle visuelle Identität schaffen.

Für den Benutzer ist der Prozess einer BIP47-Zahlung mit der PayNym-Implementierung äußerst einfach. Stellen wir uns vor, Alice möchte Zahlungen an Bob senden:

1. Bob verbreitet seinen QR-Code oder direkt seinen wiederverwendbaren Zahlungscode. Er kann ihn auf seiner Website, in verschiedenen öffentlichen sozialen Netzwerken oder über andere Kommunikationsmittel an Alice senden.
2. Alice öffnet ihre Software Samourai oder Sparrow und scannt oder fügt den Zahlungscode von Bob ein.
3. Alice verbindet ihren PayNym mit dem von Bob ("Follow" auf Englisch). Dieser Vorgang findet außerhalb der Blockchain statt und ist vollständig kostenlos.

4. Alice verbindet ihren PayNym mit dem von Bob ("Connect" auf Englisch). Dieser Vorgang findet "on chain" statt. Alice muss die Transaktionsgebühren sowie eine feste Gebühr von 15.000 Sats für den Service auf Samourai bezahlen. Die Servicegebühren werden auf Sparrow angeboten. Dieser Schritt wird als Benachrichtigungstransaktion bezeichnet.

5. Sobald die Benachrichtigungstransaktion bestätigt ist, kann Alice eine BIP47-Zahlungstransaktion an Bob erstellen. Ihre Brieftasche generiert automatisch eine neue leere Empfangsadresse, für die nur Bob den privaten Schlüssel besitzt.

Die Durchführung der Benachrichtigungstransaktion, d.h. die Verbindung ihres PayNym, ist ein obligatorischer erster Schritt, um BIP47-Zahlungen durchzuführen. Sobald dieser Schritt jedoch abgeschlossen ist, kann der Absender mehrere Zahlungen an den Empfänger (genau 2^32) durchführen, ohne erneut eine Benachrichtigungstransaktion durchführen zu müssen.

Sie haben gesehen, dass es zwei verschiedene Operationen gibt, um PayNyms miteinander zu verbinden: verbinden und folgen. Die Verbindungsoperation ("connecter") entspricht der Benachrichtigungstransaktion von BIP47, die einfach eine Bitcoin-Transaktion mit bestimmten Informationen ist, die über einen OP_RETURN-Ausgang übermittelt werden. Sie hilft dabei, eine verschlüsselte Kommunikation zwischen den beiden Benutzern herzustellen, um die erforderlichen gemeinsamen Geheimnisse zur Generierung neuer leerer Empfangsadressen zu erzeugen.

Die Verknüpfungsoperation ("follow" oder "relier") hingegen ermöglicht eine Verbindung auf Soroban, einem auf Tor basierenden verschlüsselten Kommunikationsprotokoll, das speziell von den Samourai-Teams entwickelt wurde.

Zusammenfassend:

- Das Verbinden von zwei PayNyms ("follow") ist völlig kostenlos. Dies hilft bei der Herstellung von verschlüsselten "off chain" -Kommunikationen, insbesondere zur Verwendung von Samourai-Kollaborationstransaktionstools (Stowaway oder StonewallX2). Diese Operation ist spezifisch für PayNym. Sie wird nicht im BIP47 beschrieben.

- Das Verbinden von zwei PayNyms ist kostenpflichtig. Dies beinhaltet die Durchführung der Benachrichtigungstransaktion, um die Verbindung herzustellen. Die Kosten umfassen mögliche Servicegebühren, Transaktionsmining-Gebühren und 546 Sats, die an die Empfangsbenachrichtigungsadresse des Empfängers gesendet werden, um ihn über die Öffnung des Tunnels zu informieren. Diese Operation ist mit BIP47 verbunden. Sobald sie durchgeführt wurde, kann der Absender mehrere BIP47-Zahlungen an den Empfänger durchführen.

Um zwei PayNyms verbinden zu können, müssen sie bereits miteinander verknüpft sein.

## Tutorials: Verwendung von PayNym.

Jetzt, da wir die Theorie gesehen haben, wollen wir uns die Praxis gemeinsam ansehen. Die Idee der folgenden Tutorials ist es, meinen PayNym in meiner Sparrow-Wallet mit meinem PayNym in meiner Samourai-Wallet zu verbinden. Das erste Tutorial zeigt Ihnen, wie Sie eine Transaktion mit dem wiederverwendbaren Zahlungscode von Samourai zu Sparrow durchführen können, und das zweite Tutorial beschreibt den gleichen Mechanismus von Sparrow zu Samourai.

> Ich habe diese Tutorials im Testnetzwerk durchgeführt. Es handelt sich nicht um echte Bitcoins.

### Erstellen einer BIP47-Transaktion mit Samourai Wallet.

Um zu beginnen, benötigen Sie natürlich die Samourai Wallet-App. Sie können sie direkt aus dem Google Play Store herunterladen oder mit der APK-Datei, die auf der offiziellen Samourai-Website verfügbar ist.

Nachdem die Wallet initialisiert wurde, falls Sie dies noch nicht getan haben, fordern Sie Ihren PayNym an, indem Sie auf das Pluszeichen (+) unten rechts und dann auf "PayNym" klicken.

Der erste Schritt, um eine BIP47-Zahlung durchzuführen, besteht darin, den wiederverwendbaren Zahlungscode unseres Empfängers abzurufen. Anschließend können wir uns damit verbinden und uns dann verbinden:

![video](assets/6.mp4)

Sobald die Benachrichtigungstransaktion bestätigt ist, kann ich mehrere Zahlungen an meinen Empfänger senden. Jede Transaktion erfolgt automatisch mit einer neuen leeren Adresse, für die der Empfänger die Schlüssel besitzt. Dieser muss nichts tun, alles wird von meiner Seite aus berechnet.

So führen Sie eine BIP47-Transaktion in der Samourai Wallet durch:

![video](assets/7.mp4)

### Erstellen einer BIP47-Transaktion mit Sparrow Wallet.

Genauso wie bei Samourai benötigen Sie natürlich die Sparrow-Software. Diese ist auf Computern verfügbar. Sie können sie von ihrer [offiziellen Website](https://sparrowwallet.com/) herunterladen.

Stellen Sie sicher, dass Sie die Signatur des Entwicklers und die Integrität der heruntergeladenen Software überprüfen, bevor Sie sie auf Ihrem Gerät installieren.

Erstellen Sie eine Wallet und fordern Sie Ihren PayNym an, indem Sie auf "Show PayNym" im Menü "Tool" in der oberen Leiste klicken:

![image](assets/8.webp)

Anschließend müssen Sie Ihren PayNym mit dem des Empfängers verbinden und verbinden. Geben Sie dazu seinen wiederverwendbaren Zahlungscode in das Fenster "Find Contact" ein, folgen Sie ihm und führen Sie dann die Benachrichtigungstransaktion durch, indem Sie auf "Link Contact" klicken:

![image](assets/9.webp)

Sobald die Benachrichtigungstransaktion bestätigt ist, können Zahlungen an den wiederverwendbaren Zahlungscode gesendet werden. Hier ist, wie es funktioniert:

![video](assets/10.mp4)

Jetzt, da wir den praktischen Aspekt der PayNym-Implementierung von BIP47 untersucht haben, wollen wir uns ansehen, wie all diese Mechanismen funktionieren und welche kryptographischen Methoden verwendet werden.

## Die Mechanismen von BIP47.

Um die Mechanismen von BIP47 zu untersuchen, ist es wichtig, die Struktur der hierarchischen deterministischen Wallet (HD), die Mechanismen zur Ableitung von Kinderschlüsselpaaren und die Prinzipien der elliptischen Kurvenkryptographie zu verstehen. Glücklicherweise finden Sie auf meinem Blog alle Informationen, die für das Verständnis dieses Teils erforderlich sind:

- [Verständnis der Ableitungspfade einer Bitcoin Wallet](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-bitcoin)

- [Die Bitcoin Wallet - Auszug aus dem eBook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2)

### Der wiederverwendbare Zahlungscode.

Wie in Teil zwei dieses Papiers erklärt, befindet sich der wiederverwendbare Zahlungscode in Tiefe drei der HD-Wallet. Er ist letztendlich in seiner Platzierung, Struktur und Funktion etwas vergleichbar mit einem xpub.

Hier sind die verschiedenen Teile, aus denen ein 80-Byte-Zahlungscode besteht:

- Byte 0: Die Version. Wenn die erste Version von BIP47 verwendet wird, ist dieses Byte gleich 0x01.

- Byte 1: Das Bitfeld. Dieser Raum ist reserviert, um zusätzliche Informationen für spezifische Verwendungen bereitzustellen. Wenn nur PayNym verwendet wird, ist dieses Byte gleich 0x00.

- Byte 2: Die Parität von y. Dieses Byte gibt 0x02 oder 0x03 an, abhängig von der Parität (gerade oder ungerade Anzahl) des Werts der y-Koordinate unseres öffentlichen Schlüssels. Für weitere Informationen zu dieser Praxis lesen Sie bitte Schritt 1 des Abschnitts "Adressableitung" in diesem Artikel.

- Von Byte 3 bis Byte 34: Der Wert von x. Diese Bytes geben die x-Koordinate unseres öffentlichen Schlüssels an. Die Konkatenation von x und der Parität von y ergibt unseren komprimierten öffentlichen Schlüssel.

- Von Byte 35 bis Byte 66: Der Kettencode. Dieser Raum ist für den mit dem oben genannten öffentlichen Schlüssel verbundenen Kettencode reserviert.

- Von Byte 67 bis Byte 79: Die Polsterung. Dieser Raum ist für mögliche zukünftige Entwicklungen reserviert. Für Version 1 füllen wir ihn einfach mit Nullen auf, um die Daten auf 80 Bytes, die Größe einer OP_RETURN-Ausgabe, aufzufüllen.

Hier ist die hexadezimale Darstellung meines wiederverwendbaren Zahlungscodes aus dem vorherigen Abschnitt, mit den Farben, die den oben genannten Bytes entsprechen:
Anschließend muss auch das Byte des Präfixes "P" hinzugefügt werden, um auf den ersten Blick zu erkennen, dass es sich um einen Zahlungscode handelt. Dieses Byte ist 0x47.

Schließlich berechnen wir die Prüfsumme dieses Zahlungscodes mit HASH256, d.h. einem doppelten Hash mit der SHA256-Funktion. Wir nehmen die ersten vier Bytes dieses Hashes und fügen sie am Ende hinzu (in rosa).

Der Zahlungscode ist bereit und muss nur noch in Base 58 umgewandelt werden:

Wie Sie sehen können, ähnelt diese Konstruktion stark der Struktur eines erweiterten öffentlichen Schlüssels vom Typ "xpub".

Während dieses Prozesses, der zu unserem Zahlungscode führt, haben wir einen komprimierten öffentlichen Schlüssel und einen Kettencode verwendet. Diese beiden Elemente sind das Ergebnis einer deterministischen und hierarchischen Ableitung von der Wallet-Saat, indem wir dem folgenden Ableitungspfad folgen: m/47'/0'/0'/
Konkret wird der öffentliche Schlüssel und der Kettencode des wiederverwendbaren Zahlungscodes berechnet, indem der Hauptprivatschlüssel aus dem Seed abgeleitet wird und dann ein Tochterpaar mit dem Index 47 + 2^31 (verstärkte Ableitung) abgeleitet wird. Anschließend werden zwei weitere Tochterpaare mit dem Index 2^31 (verstärkte Ableitung) abgeleitet.

> Wenn Sie mehr über die Ableitung von Tochter-Schlüsselpaaren in einer deterministischen hierarchischen Bitcoin-Brieftasche erfahren möchten, empfehle ich Ihnen, CRYPTO301 zu machen.

### Die kryptographische Methode: der Diffie-Hellman-Schlüsselaustausch auf elliptischen Kurven (ECDH).

Die kryptographische Methode, die dem BIP47 zugrunde liegt, ist ECDH (Elliptic-Curve Diffie-Hellman = Diffie-Hellman-Schlüsselaustausch auf elliptischen Kurven). Dieses Protokoll ist eine Variante des klassischen Diffie-Hellman-Schlüsselaustauschs.

Diffie-Hellman ist ein Schlüsselaustauschprotokoll, das 1976 vorgestellt wurde und es zwei Personen ermöglicht, aus zwei Schlüsselpaaren (öffentliche und private Schlüssel) ein gemeinsames Geheimnis zu bestimmen, indem sie über einen unsicheren Kommunikationskanal kommunizieren.

![image](assets/11.webp)

Dieses gemeinsame Geheimnis (der rote Schlüssel) kann dann für andere Aufgaben verwendet werden. Typischerweise kann dieses gemeinsame Geheimnis verwendet werden, um eine Kommunikation in einem unsicheren Netzwerk zu verschlüsseln und zu entschlüsseln:

![image](assets/12.webp)

Um diesen Austausch erfolgreich durchzuführen, verwendet Diffie-Hellman modulare Arithmetik, um das gemeinsame Geheimnis zu berechnen. Hier ist eine vereinfachte Erklärung, wie es funktioniert:

- Alice und Bob einigen sich auf eine gemeinsame Farbe, hier Gelb. Diese Farbe ist allen bekannt. Es ist eine öffentliche Information.

- Alice wählt eine geheime Farbe, hier Rot. Sie mischt die beiden Farben und erhält Orange.

- Bob wählt eine geheime Farbe, hier Entenblau. Er mischt die beiden Farben und erhält Himmelblau.

- Alice und Bob können die erhaltenen Farben austauschen: Orange und Himmelblau. Dieser Austausch kann über ein unsicheres Netzwerk erfolgen und von Angreifern beobachtet werden.

- Alice mischt die von Bob erhaltenen Himmelblaue Farbe mit ihrer geheimen Farbe (Rot). Sie erhält Braun.

- Bob mischt die von Alice erhaltenen Orange Farbe mit seiner geheimen Farbe (Entenblau). Er erhält dieselbe braune Farbe.

![image](assets/13.webp)

> Kredit: Ursprüngliche Idee: A.J. Han Vinck, Vektorversion: Flugaal, Übersetzung: Dereckson, Public domain, via Wikimedia Commons. https://commons.wikimedia.org/wiki/File:Diffie-Hellman_Key_Exchange_(fr).svg

In dieser Vereinfachung repräsentiert die braune Farbe das Geheimnis, das zwischen Alice und Bob geteilt wird. Man muss sich vorstellen, dass es für den Angreifer in Wirklichkeit unmöglich ist, die orangefarbene und hellblaue Farbe zu trennen, um die geheimen Farben von Alice oder Bob wiederherzustellen.

Nun betrachten wir seine tatsächliche Funktionsweise. Auf den ersten Blick scheint Diffie-Hellman schwer zu verstehen zu sein. In Wirklichkeit ist das Funktionsprinzip jedoch fast kinderleicht. Bevor ich Ihnen die Mechanismen im Detail erkläre, möchte ich Ihnen kurz zwei mathematische Konzepte in Erinnerung rufen, die wir benötigen werden (und die übrigens auch in vielen anderen kryptographischen Methoden verwendet werden).

1. Eine Primzahl ist eine natürliche Zahl, die nur zwei Teiler hat: 1 und sich selbst. Zum Beispiel ist die Zahl 7 eine Primzahl, da sie nur durch 1 und 7 (sich selbst) teilbar ist. Die Zahl 8 hingegen ist keine Primzahl, da sie durch 1, 2, 4 und 8 teilbar ist. Sie hat also nicht nur zwei, sondern vier ganze und positive Teiler.

2. Das "Modulo" (notiert als "mod" oder "%") ist eine mathematische Operation, bei der zwischen zwei ganzen Zahlen der Rest der euklidischen Division der ersten Zahl durch die zweite Zahl zurückgegeben wird. Zum Beispiel ist 16 mod 5 gleich 1.

Der Diffie-Hellman-Schlüsselaustausch zwischen Alice und Bob funktioniert wie folgt:

- Alice und Bob wählen zwei gemeinsame Zahlen: p und g. p ist eine Primzahl. Je größer diese Zahl p ist, desto sicherer wird Diffie-Hellman sein. g ist eine primitive Wurzel von p. Diese beiden Zahlen können unverschlüsselt über ein unsicheres Netzwerk kommuniziert werden, sie entsprechen der gelben Farbe in der obigen Vereinfachung. Alice und Bob müssen einfach genau die gleichen Werte für p und g haben.

- Nachdem die Parameter festgelegt wurden, wählen Alice und Bob jeweils eine geheime Zufallszahl. Die von Alice erhaltene Zufallszahl wird als a bezeichnet (entspricht der roten Farbe) und die von Bob erhaltene Zufallszahl wird als b bezeichnet (entspricht der türkisblauen Farbe). Diese beiden Zahlen müssen geheim bleiben.

- Anstatt diese Zahlen a und b auszutauschen, berechnet jede Partei A (großgeschrieben) und B (großgeschrieben) wie folgt:

> A ist gleich g hoch a modulo p:
> A = g^a % p

> B ist gleich g hoch b modulo p:
> B = g^b % p

- Diese Zahlen A (entspricht der orangefarbenen Farbe) und B (entspricht der hellblauen Farbe) werden zwischen den beiden Parteien ausgetauscht. Der Austausch kann unverschlüsselt über ein unsicheres Netzwerk erfolgen.

- Alice, die nun B kennt, berechnet den Wert von z wie folgt:

> z ist gleich B hoch a modulo p:
> z = B^a % p

- Zur Erinnerung, B = g^b % p. Daher haben wir:

  > z = B^a % p
  > z = (g^b)^a % p
  >
  > Gemäß den Rechenregeln für Potenzen:
  >
  > (x^n)^m = x^nm
  >
  > Daher haben wir:
  >
  > z = g^ba % p

- Bob, der nun über A informiert ist, wird auch den Wert von z berechnen:
  > z ist gleich A hoch b modulo p:
  >
  > z = A^b % p
  >
  > Daher haben wir:
  >
  > z = (g^a)^b % p
  > z = g^ab % p
  > z = g^ba % p

Dank der Distributivität des Modulo-Operators finden Alice und Bob genau den gleichen Wert für z. Diese Zahl repräsentiert ihr gemeinsames Geheimnis, das Äquivalent zur Farbe Braun in der vorherigen Veranschaulichung. Sie können dieses gemeinsame Geheimnis verwenden, um eine Kommunikation zwischen ihnen auf einem unsicheren Netzwerk zu verschlüsseln.

![Schema der technischen Funktionsweise von Diffie-Hellman](assets/14.webp)

Ein Angreifer, der im Besitz von p, g, A und B ist, wird nicht in der Lage sein, a, b oder z zu berechnen. Eine solche Operation würde einer Umkehrung der Exponentiation entsprechen. Diese Berechnung ist unmöglich, außer man versucht alle Möglichkeiten einzeln auszuprobieren, da wir in einem endlichen Körper arbeiten. Dies würde bedeuten, das diskrete Logarithmusproblem zu lösen, also das Inverse der Exponentialfunktion in einer endlichen zyklischen Gruppe zu berechnen.

Solange wir also ausreichend große Werte für a, b und p wählen, ist Diffie-Hellman sicher. Typischerweise ist mit Parametern von 2.048 Bits (eine Zahl mit 600 Dezimalstellen) das Testen aller Möglichkeiten für a und b utopisch. Mit solchen Größenordnungen gilt der Algorithmus als sicher.

Genau hier liegt jedoch der Hauptnachteil des Diffie-Hellman-Protokolls. Um sicher zu sein, muss der Algorithmus große Zahlen verwenden. Daher bevorzugen wir heute den Einsatz des ECDH-Algorithmus, einer Variante von Diffie-Hellman, der eine algebraische Kurve verwendet, genauer gesagt eine elliptische Kurve. Dadurch können wir mit viel kleineren Zahlen arbeiten und dennoch ein gleichwertiges Maß an Sicherheit gewährleisten, was wiederum die Ressourcen für Berechnung und Speicherung reduziert.

Das allgemeine Prinzip des Algorithmus bleibt gleich. Anstelle einer zufälligen Zahl a und einer aus a berechneten Zahl A mit modularer Exponentiation verwenden wir jedoch ein Schlüsselpaar, das auf einer elliptischen Kurve etabliert ist. Anstelle der Distributivität des Modulo-Operators verwenden wir hier das Gruppenrecht auf elliptischen Kurven, genauer gesagt die Assoziativität dieses Gesetzes.
Wenn Sie keine Kenntnisse über die Funktionsweise von privaten und öffentlichen Schlüsseln auf einer elliptischen Kurve haben, erkläre ich Ihnen die Grundlagen dieser Methode in den ersten sechs Teilen dieses Artikels.

Zusammenfassend ist ein privater Schlüssel eine zufällige Zahl zwischen 1 und n-1 (wobei n die Ordnung der Kurve ist), und ein öffentlicher Schlüssel ist ein eindeutiger Punkt auf der Kurve, der durch Addition und Verdoppelung von Punkten vom Generatorpunkt aus bestimmt wird:

> K = k·G

Dabei ist K der öffentliche Schlüssel, k der private Schlüssel und G der Generatorpunkt.

Eine Eigenschaft dieses Schlüsselpaares ist, dass es sehr einfach ist, K zu bestimmen, wenn man k und G kennt, aber es ist heute unmöglich, k zu bestimmen, wenn man K und G kennt. Es handelt sich um eine Einwegfunktion.

Mit anderen Worten, man kann den öffentlichen Schlüssel leicht berechnen, wenn man den privaten Schlüssel kennt, aber es ist unmöglich, den privaten Schlüssel zu berechnen, wenn man den öffentlichen Schlüssel kennt. Diese Sicherheit beruht erneut auf der Unmöglichkeit der Berechnung des diskreten Logarithmus.

Wir werden diese Eigenschaft nutzen, um unseren Diffie-Hellman-Algorithmus anzupassen. Der Arbeitsmechanismus von ECDH ist wie folgt:

- Alice und Bob einigen sich auf eine kryptographisch sichere elliptische Kurve und deren Parameter. Diese Informationen sind öffentlich.

- Alice generiert eine zufällige Zahl ka, die ihr privater Schlüssel sein wird. Dieser private Schlüssel muss geheim bleiben. Sie bestimmt ihren öffentlichen Schlüssel Ka durch Addition und Verdoppelung von Punkten auf der gewählten elliptischen Kurve.

> Ka = ka·G

- Bob generiert ebenfalls eine zufällige Zahl kb, die sein privater Schlüssel sein wird. Er berechnet den zugehörigen öffentlichen Schlüssel Kb.

> Kb = kb·G

- Alice und Bob tauschen ihre öffentlichen Schlüssel Ka und Kb über ein unsicheres öffentliches Netzwerk aus.

- Alice berechnet einen Punkt (x,y) auf der Kurve, indem sie ihren privaten Schlüssel ka auf den öffentlichen Schlüssel von Bob Kb anwendet.

> (x,y) = ka·Kb

- Bob berechnet einen Punkt (x,y) auf der Kurve, indem er seinen privaten Schlüssel kb auf den öffentlichen Schlüssel von Alice Ka anwendet.

> (x,y) = kb·Ka

- Alice und Bob erhalten den gleichen Punkt auf der elliptischen Kurve. Das gemeinsame Geheimnis wird die x-Koordinate dieses Punktes sein.

Sie erhalten das gleiche gemeinsame Geheimnis, weil:

> (x,y) = ka·Kb = ka·kb·G = kb·ka·G = kb·Ka

Ein potenzieller Angreifer, der das unsichere öffentliche Netzwerk beobachtet, kann nur die öffentlichen Schlüssel von Alice und Bob sowie die Parameter der gewählten Kurve erhalten. Wie zuvor erklärt, reichen diese beiden Informationen allein nicht aus, um die privaten Schlüssel zu bestimmen, und daher kann der Angreifer nicht auf das Geheimnis zugreifen.
ECDH ist ein Algorithmus, der den Austausch von Schlüsseln ermöglicht. Es wird oft zusammen mit anderen kryptographischen Methoden verwendet, um ein Protokoll zu definieren. Zum Beispiel wird ECDH im Herzen von TLS (Transport Layer Security) verwendet, einem Verschlüsselungs- und Authentifizierungsprotokoll, das für die Transportebene des Internets verwendet wird. TLS verwendet ECDHE für den Schlüsselaustausch, eine Variante von ECDH, bei der die Schlüssel ephemeral sind, um anhaltende Vertraulichkeit zu gewährleisten. Neben ECDHE verwendet TLS auch einen Authentifizierungsalgorithmus wie ECDSA, einen Verschlüsselungsalgorithmus wie AES und eine Hash-Funktion wie SHA256.

TLS definiert unter anderem das "s" in "https" sowie das kleine Schlosssymbol, das Sie oben links in Ihrem Webbrowser sehen, um eine verschlüsselte Kommunikation zu gewährleisten. Sie verwenden also ECDH, während Sie diesen Artikel lesen, und verwenden es wahrscheinlich täglich, ohne es zu bemerken.

### Die Benachrichtigungstransaktion.

Wie wir im vorherigen Abschnitt gesehen haben, ist ECDH eine Variante des Diffie-Hellman-Austauschs, bei dem Schlüsselpaare auf einer elliptischen Kurve erstellt werden. Das passt gut, denn wir haben viele Schlüsselpaare in unseren Bitcoin-Hierarchical-Deterministic-Wallets!

Die Idee besteht darin, die Schlüsselpaare der hierarchischen deterministischen Bitcoin-Wallets beider Parteien zu verwenden, um gemeinsame und ephemere Geheimnisse zwischen ihnen herzustellen. Im BIP47 wird daher stattdessen ECDHE (Elliptic Curve Diffie-Hellman Ephemeral) verwendet.

ECDHE wird im BIP47 zunächst verwendet, um den Zahlungscode vom Absender an den Empfänger zu übertragen. Dies ist die berühmte Benachrichtigungstransaktion. Damit BIP47 verwendet werden kann, müssen beide Parteien (der Absender, der Zahlungen sendet, und der Empfänger, der Zahlungen empfängt) den Zahlungscode der anderen Partei kennen. Dies ist erforderlich, um die ephemeren öffentlichen Schlüssel abzuleiten und somit dedizierte Empfangsadressen zu erstellen.

Vor diesem Austausch kennt der Absender logischerweise bereits den Zahlungscode des Empfängers, da er ihn off-chain erhalten hat, zum Beispiel auf seiner Website oder in sozialen Netzwerken. Der Empfänger kennt jedoch möglicherweise nicht den Zahlungscode des Absenders. Es muss ihm also übermittelt werden, sonst kann er seine ephemeren Schlüssel nicht ableiten und somit nicht wissen, wo sich seine Bitcoins befinden und seine Mittel nicht freigeben. Man könnte es ihm off-chain übermitteln, mit einem anderen Kommunikationssystem, aber das würde ein Problem bei der Wiederherstellung der Wallet aus dem Seed darstellen.
Tatsächliche Übersetzung:
Wie bereits erwähnt, werden BIP47-Adressen nicht aus dem Empfänger-Samen abgeleitet (sonst könnte man direkt eine seiner xpubs verwenden), sondern sie werden durch eine Berechnung unter Verwendung der beiden Zahlungscodes erstellt: dem des Empfängers und dem des Absenders. Daher muss der Empfänger, wenn er seine Brieftasche verliert und versucht, sie mit seinem Samen wiederherzustellen, zwangsläufig alle Zahlungscodes der Personen haben, die ihm Bitcoins über BIP47 geschickt haben.

Es wäre also möglich, BIP47 ohne diese Benachrichtigungstransaktion zu verwenden, aber jeder Benutzer müsste eine Sicherungskopie der Zahlungscodes seiner Kontakte erstellen. Diese Situation bleibt jedoch unverwaltbar, solange es keine einfache und robuste Möglichkeit gibt, diese Sicherungskopien zu erstellen, zu speichern und aktuell zu halten. Die Benachrichtigungstransaktion ist daher im aktuellen Zustand der Dinge nahezu obligatorisch.

Neben der Sicherung der Zahlungscodes spielt diese Transaktion auch eine Benachrichtigungsrolle für den Empfänger. Sie informiert den Client darüber, dass ein Tunnel geöffnet wurde.

Bevor ich Ihnen die technische Funktionsweise der Benachrichtigungstransaktion im Detail erkläre, möchte ich Ihnen etwas über das Datenschutzmodell erzählen. Tatsächlich rechtfertigt das BIP47-Modell bestimmte Vorsichtsmaßnahmen bei der Erstellung dieser ersten Transaktion.

Der Zahlungscode selbst stellt kein direktes Datenschutzrisiko dar. Im Gegensatz zum herkömmlichen Bitcoin-Modell, das es ermöglicht, den Informationsfluss zwischen der Benutzeridentität und den Transaktionen zu unterbrechen, insbesondere durch die Verwendung anonymer öffentlicher Schlüssel, kann der Zahlungscode direkt mit einer Identität verknüpft werden. Dies ist natürlich keine Verpflichtung, aber diese Verbindung ist nicht gefährlich.

Der Zahlungscode leitet die Adressen, die zum Empfangen von BIP47-Zahlungen verwendet werden, nicht direkt ab. Stattdessen werden die Adressen durch die Anwendung von ECDHE auf die Kinderschlüssel der Zahlungscodes beider Parteien erhalten.

Ein einzelner Zahlungscode stellt daher kein direktes Datenschutzrisiko dar, da nur die Benachrichtigungsadresse daraus abgeleitet wird. Es können einige Informationen daraus abgeleitet werden, aber normalerweise kann man nicht wissen, mit wem Sie Transaktionen durchführen.

Es ist daher wichtig, eine strikte Trennung zwischen den Zahlungscodes der Benutzer aufrechtzuerhalten. Zu diesem Zweck ist der anfängliche Kommunikationsschritt des Codes ein kritischer Moment für die Zahlungsdatenschutz und dennoch für das ordnungsgemäße Funktionieren des Protokolls erforderlich. Wenn einer der beiden Zahlungscodes öffentlich abgerufen werden kann (z. B. auf einer Website), darf der zweite Code, d. h. der des Absenders, nicht mit dem ersten in Verbindung gebracht werden.

Nehmen wir zum Beispiel an, ich möchte eine Spende mit BIP47 an eine friedliche Protestbewegung in Kanada machen:

- Diese Organisation hat ihren Zahlungscode direkt auf ihrer Website oder in ihren sozialen Netzwerken veröffentlicht.
- Dieser Code ist also mit der Bewegung verbunden.

- Ich hole mir diesen Zahlungscode.

- Bevor ich ihnen eine Transaktion senden kann, muss ich sicherstellen, dass sie von meinem persönlichen Zahlungscode wissen, der auch mit meiner Identität verbunden ist, da ich ihn zum Empfangen von Transaktionen aus meinen sozialen Netzwerken verwende.

Wie kann ich ihn ihnen übermitteln? Wenn ich ihn mit einem herkömmlichen Kommunikationsmittel sende, besteht die Gefahr, dass die Informationen durchsickern und ich als Person, die friedliche Bewegungen unterstützt, erfasst werde.

Die Benachrichtigungstransaktion ist sicherlich nicht die einzige Lösung, um den Zahlungscode des Absenders geheim zu übermitteln, erfüllt jedoch derzeit perfekt diese Rolle, indem sie mehrere Sicherheitsebenen anwendet.

Im folgenden Schema stellen die roten Linien den Zeitpunkt dar, an dem der Informationsfluss unterbrochen werden muss, und die schwarzen Pfeile stellen die eindeutigen Verbindungen dar, die von einem externen Beobachter hergestellt werden können:

![Schema des Modells für die Vertraulichkeit des wiederverwendbaren Zahlungscodes](assets/15.webp)

In der Realität ist es für das klassische Bitcoin-Vertraulichkeitsmodell oft schwierig, den Informationsfluss zwischen dem Schlüsselpaar und dem Benutzer vollständig zu unterbrechen, insbesondere bei Ferntransaktionen. Zum Beispiel muss der Empfänger einer Spendenkampagne eine Adresse oder einen öffentlichen Schlüssel auf seiner Website oder in seinen sozialen Netzwerken offenlegen. Die ordnungsgemäße Verwendung von BIP47, d.h. mit der Benachrichtigungstransaktion, löst dieses Problem durch ECDHE und die Verschlüsselungsschicht, die wir untersuchen werden.

Natürlich wird das klassische Bitcoin-Vertraulichkeitsmodell immer noch auf der Ebene der ephemeren öffentlichen Schlüssel beobachtet, die aus der Verknüpfung der beiden Zahlungscodes abgeleitet werden. Die beiden Modelle sind voneinander abhängig. Ich möchte hier nur darauf hinweisen, dass im Gegensatz zur herkömmlichen Verwendung eines öffentlichen Schlüssels zum Empfangen von Bitcoins der Zahlungscode mit einer Identität verknüpft sein kann, da die Information "Bob führt eine Transaktion mit Alice durch" zu einem anderen Zeitpunkt unterbrochen wird. Der Zahlungscode wird verwendet, um Zahlungsadressen zu generieren, aber allein durch Beobachtung der Blockchain ist es unmöglich, eine BIP47-Zahlungstransaktion mit den verwendeten Zahlungscodes zu verknüpfen.

### Aufbau der Benachrichtigungstransaktion.

Lassen Sie uns nun sehen, wie diese Benachrichtigungstransaktion funktioniert. Stellen wir uns vor, Alice möchte mit BIP47 Geld an Bob senden. In meinem Beispiel handelt Alice als Absenderin und Bob als Empfänger. Letzterer hat seinen Zahlungscode auf seiner Website veröffentlicht. Alice kennt also bereits Bobs Zahlungscode.

1. Alice berechnet ein gemeinsames Geheimnis mit ECDH:

- Sie wählt ein Schlüsselpaar aus ihrer HD-Wallet aus, das sich auf einem anderen Zweig als ihr Zahlungscode befindet. Achten Sie darauf, dass dieses Paar nicht leicht mit Alice' Benachrichtigungsadresse oder ihrer Identität in Verbindung gebracht werden kann (siehe vorheriger Abschnitt).
- Alice wählt den privaten Schlüssel dieses Paares aus. Wir nennen ihn "a" (Kleinbuchstabe).

> a

- Alice erhält den öffentlichen Schlüssel, der mit Bobs Benachrichtigungsadresse verknüpft ist. Dieser Schlüssel ist das erste abgeleitete Kind des Zahlungscodes von Bob (Index 0). Wir nennen diesen öffentlichen Schlüssel "B" (Großbuchstabe). Der mit diesem öffentlichen Schlüssel verbundene private Schlüssel wird "b" (Kleinbuchstabe) genannt. "B" wird durch Addition und Verdoppelung von Punkten auf der elliptischen Kurve von "G" (dem Generatorpunkt) mit "b" (dem privaten Schlüssel) bestimmt.

> B = b·G

- Alice berechnet einen geheimen Punkt "S" (Großbuchstabe) auf der elliptischen Kurve, indem sie ihren privaten Schlüssel "a" auf den öffentlichen Schlüssel von Bob "B" anwendet.

> S = a·B

- Alice berechnet den Verblindungsfaktor "f", der verwendet wird, um ihren Zahlungscode zu verschlüsseln. Dazu generiert sie eine pseudozufällige Zahl mit der HMAC-SHA512-Funktion. Als zweiten Eingabewert verwendet sie einen Wert, den nur Bob wiederfinden kann: (x), die Abszisse des zuvor berechneten geheimen Punktes. Der erste Eingabewert ist (o), die in dieser Transaktion verbrauchte UTXO (Outpoint).

> f = HMAC-SHA512(o, x)

2. Alice konvertiert ihren persönlichen Zahlungscode in Binärformat.

3. Sie verwendet diesen Verblindungsfaktor als Schlüssel, um eine symmetrische Verschlüsselung auf die Nutzlast ihres Zahlungscodes anzuwenden. Der verwendete Verschlüsselungsalgorithmus ist ein einfaches XOR. Die durchgeführte Operation ist vergleichbar mit dem Vernam-Chiffre, auch bekannt als "One-Time Pad":

- Alice teilt zuerst ihren Verblindungsfaktor in zwei Teile auf: Die ersten 32 Bytes werden "f1" genannt und die letzten 32 Bytes werden "f2" genannt. Es gilt also:

> f = f1 || f2

- Alice berechnet getrennt den verschlüsselten Wert (x') der Abszisse des öffentlichen Schlüssels (x) ihres Zahlungscodes und den verschlüsselten Wert (c') ihres Kettencodes (c). "f1" und "f2" fungieren jeweils als Verschlüsselungsschlüssel. Die verwendete Operation ist das XOR (exklusives Oder).

> x' = x XOR f1
>
> c>' = c XOR f2

- Alice ersetzt die echten Werte der x-Koordinate des öffentlichen Schlüssels und des Chaincodes (c) in ihrem Zahlungscode durch die verschlüsselten Werte (x') und (c').

Bevor wir die technische Beschreibung dieser Benachrichtigungstransaktion fortsetzen, wollen wir uns einen Moment mit der XOR-Operation befassen. XOR ist ein bitweiser logischer Operator, der auf der Booleschen Algebra basiert. Aus zwei bitweisen Operanden liefert er 1, wenn die Bits gleicher Rangordnung unterschiedlich sind, und er liefert 0, wenn die Bits gleicher Rangordnung gleich sind. Hier ist die Wahrheitstabelle für XOR in Abhängigkeit von den Werten der Operanden D und E:

| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Beispiel:

> 0110 XOR 1110 = 1000

Oder:

> 010011 XOR 110110 = 100101

Bei der Verwendung von ECDH ist die Verwendung von XOR als Verschlüsselungsschicht besonders kohärent. Durch diesen Operator ist die Verschlüsselung symmetrisch. Dadurch kann der Empfänger den Zahlungscode mit demselben Schlüssel entschlüsseln, der zur Verschlüsselung verwendet wurde. Der Verschlüsselungs- und Entschlüsselungsschlüssel wird aus dem gemeinsamen Geheimnis durch ECDH berechnet.

Diese Symmetrie wird durch die Eigenschaften der Kommutativität und Assoziativität des XOR-Operators ermöglicht:

- Weitere Eigenschaften:
  -> D ⊕ D = 0
  -> D ⊕ 0 = D

- Kommutativität:
  D ⊕ E = E ⊕ D

- Assoziativität:
  D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z

- Symmetrie:
  Wenn: D ⊕ E = L
  Dann: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E
  -> D ⊕ L = E
  Dann ähnelt diese Verschlüsselungsmethode sehr dem Vernam-Chiffre (One-Time Pad), dem einzigen bekannten Verschlüsselungsalgorithmus, der eine bedingungslose (oder absolute) Sicherheit bietet. Damit das Vernam-Chiffre diese Eigenschaft aufweist, muss der Verschlüsselungsschlüssel perfekt zufällig sein, die gleiche Länge wie die Nachricht haben und nur einmal verwendet werden. Bei der hier verwendeten Verschlüsselungsmethode für BIP47 ist der Schlüssel tatsächlich die gleiche Länge wie die Nachricht, der Verblindungsfaktor hat genau die gleiche Länge wie die Verkettung der Abszisse des öffentlichen Schlüssels mit dem Kettencode der Zahlung. Dieser Verschlüsselungsschlüssel wird tatsächlich nur einmal verwendet. Allerdings stammt dieser Schlüssel nicht aus einem perfekten Zufall, da er ein HMAC ist. Er ist eher pseudozufällig. Es handelt sich also nicht um ein Vernam-Chiffre, aber die Methode kommt ihm nahe.
  Kehren wir zu unserem Aufbau der Benachrichtigungstransaktion zurück:

4. Alice hat jetzt ihren Zahlungscode mit einer verschlüsselten Nutzlast. Sie wird eine Transaktion erstellen und verbreiten, die ihren öffentlichen Schlüssel "A" als Eingabe, eine Ausgabe an die Benachrichtigungsadresse von Bob und eine OP_RETURN-Ausgabe enthält, die ihren Zahlungscode mit der verschlüsselten Nutzlast enthält. Diese Transaktion ist die Benachrichtigungstransaktion.

OP_RETURN ist ein Opcode, also ein Skript, mit dem eine Bitcoin-Transaktionsausgabe als ungültig markiert werden kann. Heutzutage wird es verwendet, um Informationen in der Bitcoin-Blockchain zu verbreiten oder zu verankern. Es können bis zu 80 Bytes an Daten gespeichert werden, die in die Blockchain geschrieben und somit von allen anderen Benutzern sichtbar sind.

Wie wir in dem vorherigen Abschnitt gesehen haben, wird Diffie-Hellman verwendet, um ein gemeinsames Geheimnis zwischen zwei Benutzern zu generieren, die über ein unsicheres Netzwerk kommunizieren, das potenziell von Angreifern beobachtet wird. Im BIP47 wird ECDH verwendet, um über das Bitcoin-Netzwerk zu kommunizieren, das naturgemäß ein transparentes Kommunikationsnetzwerk ist und von vielen Angreifern beobachtet wird. Das durch den Diffie-Hellman-Schlüsselaustausch auf der elliptischen Kurve berechnete gemeinsame Geheimnis wird dann verwendet, um die geheime Information zu verschlüsseln, die übertragen werden soll: den Zahlungscode des Absenders (Alice).

Hier ist ein Diagramm aus dem BIP47, das das gerade Beschriebene veranschaulicht:

![Diagramm: Alice sendet ihren verschleierten Zahlungscode an Bobs Benachrichtigungsadresse](assets/16.webp)

Quelle: Wiederverwendbare Zahlungscodes für hierarchisch deterministische Geldbörsen, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Wenn wir dieses Diagramm mit dem übereinstimmen lassen, was ich Ihnen zuvor beschrieben habe:

- "Wallet Priv-Key" auf Alice's Seite entspricht: a.

- "Child Pub-Key 0" auf Bob's Seite entspricht: B.
- "Notification Shared Secret" entspricht: f.
- "Masked Payment Code" entspricht dem verschleierten Zahlungscode, d.h. mit verschlüsselten Nutzdaten: x' und c'.

- "Notification Transaction" ist die Transaktion, die den OP_RETURN enthält.

Ich fasse die Schritte zusammen, die wir gerade besprochen haben, um eine Benachrichtigungstransaktion durchzuführen:

- Alice erhält den Zahlungscode und die Benachrichtigungsadresse von Bob.

- Alice wählt eine UTXO aus ihrem HD-Wallet mit dem entsprechenden Schlüsselpaar aus.

- Sie berechnet einen geheimen Punkt auf der elliptischen Kurve mit Hilfe von ECDH.

- Sie verwendet diesen geheimen Punkt, um einen HMAC zu berechnen, der der Verblindungsfaktor ist.

- Sie verwendet diesen Verblindungsfaktor, um die Nutzdaten ihres persönlichen Zahlungscodes zu verschlüsseln.

- Sie verwendet eine OP_RETURN-Transaktionsausgabe, um den verschleierten Zahlungscode an Bob zu übertragen.

Um das Funktionieren genauer zu verstehen, insbesondere die Verwendung von OP_RETURN, betrachten wir gemeinsam eine echte Benachrichtigungstransaktion. Ich habe eine solche Transaktion im Testnet durchgeführt, die Sie hier finden können:

https://mempool.space/fr/testnet/tx/0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e

TXID:

> 0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e

![BIP47-Benachrichtigungstransaktion](assets/17.webp)

Quelle: https://blockstream.info/

Beim Betrachten dieser Transaktion können wir bereits sehen, dass sie eine einzige Eingabe und 4 Ausgaben hat:

- Die erste Ausgabe ist OP_RETURN, die meinen verschleierten Zahlungscode enthält.

- Die zweite Ausgabe von 546 Sats zeigt auf die Benachrichtigungsadresse meines Empfängers.

- Die dritte Ausgabe von 15.000 Sats sind die Servicegebühren, da ich Samourai Wallet für den Aufbau dieser Transaktion verwendet habe.

- Die vierte Ausgabe von zwei Millionen Sats ist der Wechselbetrag, d.h. der verbleibende Unterschied meines Eingangs, der zu einer anderen meiner Adressen zurückkehrt.

Am interessantesten ist natürlich die Ausgabe 0, die OP_RETURN verwendet. Schauen wir uns genauer an, was sie enthält:

![OP_RETURN-Ausgabe der Benachrichtigungstransaktion BIP47](assets/18.webp)

Quelle: https://blockstream.info/

Dort entdecken wir das Skript der Ausgabe in hexadezimaler Form:

> 6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000

In diesem Skript können wir mehrere Teile analysieren:
6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000>

OP-Codes:
6a4c

Ein Byte, das die Größe der Nutzlast angibt (80 Bytes):
50

Die Metadaten meines Klartext-Zahlungscodes:
010002

Die verschlüsselte x-Koordinate des öffentlichen Schlüssels meines Zahlungscodes:
b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164

Der verschlüsselte Kettencode meines Zahlungscodes:
927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d8

Polsterung, um auf 80 Bytes zu kommen:
00000000000000000000000000

Unter den OP-Codes können wir 0x6a erkennen, was OP_RETURN und 0x4c, was OP_PUSHDATA1 bedeutet. Das nächste Byte nach diesem OP-Code gibt die Größe der folgenden Nutzlast an. Es ist 0x50, also 80 Bytes.

Dann kommt der Zahlungscode mit der verschlüsselten Nutzlast.

Hier ist mein Klartext-Zahlungscode, der in dieser Transaktion verwendet wird:

In Base58:
PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU

In Base16 (HEX):
4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db

Wenn man meinen Klartext-Zahlungscode mit dem OP_RETURN vergleicht, kann man sehen, dass die HRP (in Braun) und die Prüfsumme (in Rosa) nicht übertragen werden. Das ist normal, diese Informationen sind für Menschen bestimmt.
Dann kann man (in grün) die Version (0x01), das Bitfeld (0x00) und die Parität des öffentlichen Schlüssels (0x02) erkennen. Am Ende des Zahlungscodes befinden sich leere Bytes in Schwarz (0x00), die zur Auffüllung auf insgesamt 80 Bytes dienen. Alle diese Metadaten werden im Klartext übertragen (nicht verschlüsselt).
Schließlich kann man sehen, dass die Abszisse des öffentlichen Schlüssels (in Blau) und der Chain-Code (in Rot) verschlüsselt wurden. Dies bildet die Nutzlast des Zahlungscodes.

### Empfang der Transaktionsbenachrichtigung.

Nun, da Alice die Transaktionsbenachrichtigung an Bob gesendet hat, schauen wir uns an, wie er sie interpretiert.

Zur Erinnerung: Bob muss zwingend auf den Zahlungscode von Alice zugreifen können. Ohne diese Information, wie wir im nächsten Abschnitt sehen werden, kann er die von Alice erstellten Schlüsselpaare nicht ableiten und somit nicht auf ihre mit BIP47 erhaltenen Bitcoins zugreifen. Derzeit ist die Nutzlast des Zahlungscodes von Alice verschlüsselt. Schauen wir uns gemeinsam an, wie Bob sie entschlüsselt.

1. Bob überwacht Transaktionen, die Ausgaben mit seiner Benachrichtigungsadresse erstellen.

2. Wenn eine Transaktion eine Ausgabe an seine Benachrichtigungsadresse hat, analysiert Bob sie, um zu sehen, ob sie eine OP_RETURN-Ausgabe enthält, die dem BIP47-Standard entspricht.

3. Wenn das erste Byte der Nutzlast des OP_RETURN 0x01 ist, beginnt Bob mit der Suche nach einem möglichen gemeinsamen Geheimnis mit ECDH:

- Bob wählt den öffentlichen Schlüssel als Eingabe der Transaktion aus. Das heißt, den öffentlichen Schlüssel von Alice namens "A" mit:

> A = a·G

- Bob wählt den privaten Schlüssel "b" aus, der mit seiner persönlichen Benachrichtigungsadresse verknüpft ist:

> b

- Bob berechnet den geheimen Punkt "S" (gemeinsames Geheimnis ECDH) auf der elliptischen Kurve durch Addition und Verdoppelung von Punkten, indem er seinen privaten Schlüssel "b" auf den öffentlichen Schlüssel von Alice "A" anwendet:

> S = b·A

- Bob bestimmt den Verblindungsfaktor "f", der es ermöglicht, die Nutzlast des Zahlungscodes von Alice zu entschlüsseln. Auf die gleiche Weise, wie Alice es zuvor berechnet hatte, findet Bob "f", indem er HMAC-SHA512 auf (x) den x-Wert des geheimen Punktes "S" und auf (o) die in dieser Transaktionsbenachrichtigung verbrauchte UTXO anwendet:

> f = HMAC-SHA512(o, x)

4. Bob interpretiert die Daten des OP_RETURN in der Transaktionsbenachrichtigung als Zahlungscode. Er entschlüsselt einfach die Nutzlast dieses potenziellen Zahlungscodes mithilfe des Verblindungsfaktors "f":

- Bob teilt den blinden Faktor "f" in zwei Teile auf: Die ersten 32 Bytes von "f" werden zu "f1" und die letzten 32 Bytes zu "f2".
- Bob entschlüsselt den verschlüsselten Abszissenwert (x') des öffentlichen Schlüssels des Zahlungscodes von Alice:

> x = x' XOR f1

- Bob entschlüsselt den verschlüsselten Kettencode (c') des Zahlungscodes von Alice:

> c = c' XOR f2

5. Bob überprüft, ob der Wert des öffentlichen Schlüssels des Zahlungscodes von Alice zur Gruppe secp256k1 gehört. Wenn dies der Fall ist, interpretiert er dies als gültigen Zahlungscode. Andernfalls ignoriert er diese Transaktion.

Jetzt, da Bob den Zahlungscode von Alice kennt, kann sie ihm bis zu 2^32 Zahlungen senden, ohne jemals wieder eine Benachrichtigungstransaktion dieser Art durchführen zu müssen.

Warum funktioniert das? Wie kann Bob den gleichen blinden Faktor wie Alice bestimmen und somit ihren Zahlungscode entschlüsseln? Lassen Sie uns die Aktion von ECDH genauer untersuchen, wie sie gerade beschrieben wurde.

Zunächst haben wir es mit einer symmetrischen Verschlüsselung zu tun. Das bedeutet, dass der Verschlüsselungsschlüssel und der Entschlüsselungsschlüssel denselben Wert haben. Dieser Schlüssel in der Benachrichtigungstransaktion ist der blinde Faktor (f = f1 || f2). Alice und Bob müssen also den gleichen Wert für f erhalten, ohne ihn direkt zu übertragen, da ein Angreifer ihn stehlen und die geheime Information entschlüsseln könnte.

Dieser blinde Faktor wird erhalten, indem HMAC-SHA512 auf zwei Werte angewendet wird: die Abszisse eines geheimen Punktes und die verbrauchte UTXO am Eingang der Transaktion. Bob muss also über diese beiden Informationen verfügen, um die Nutzlast des Zahlungscodes von Alice zu entschlüsseln.

Für die Eingabe-UTXO kann Bob es einfach beobachten, indem er die Benachrichtigungstransaktion betrachtet. Für den geheimen Punkt muss Bob ECDH verwenden.

Wie in dem Abschnitt über Diffie-Hellman gesehen, können Alice und Bob einfach durch Austausch ihrer jeweiligen öffentlichen Schlüssel und geheimes Anwenden ihrer privaten Schlüssel auf den öffentlichen Schlüssel des anderen einen bestimmten geheimen Punkt auf der elliptischen Kurve finden. Die Benachrichtigungstransaktion stützt sich auf diesen Mechanismus:

> Bob's Schlüsselpaar:
>
> B = b·G
>
> Alice's Schlüsselpaar:
>
> A = a·G
>
> Für einen geheimen Punkt S (x,y):
>
> S = a·B = a·b·G = b·a·G = b·A

![Schema zur Generierung eines gemeinsamen Geheimnisses mit ECDHE](assets/19.webp)
Jetzt, da Bob den Zahlungscode von Alice kennt, wird er in der Lage sein, ihre BIP47-Zahlungen zu erkennen und die empfangenen Bitcoins zu entschlüsseln, indem er die entsprechenden privaten Schlüssel ableitet.
![Bob interpretiert die Benachrichtigungstransaktion von Alice](assets/20.webp)

Quelle: Wiederverwendbare Zahlungscodes für hierarchisch deterministische Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Wenn wir dieses Schema mit dem vergleichen, was ich Ihnen zuvor beschrieben habe:

- "Wallet Pub-Key" auf Alice's Seite entspricht: A.

- "Child Priv-Key 0" auf Bob's Seite entspricht: b.

- "Notification Shared Secret" entspricht: f.

- "Masked Payment Code" entspricht dem verschleierten Zahlungscode von Alice, d.h. mit verschlüsseltem Payload: x' und c'.

- "Notification Transaction" ist die Transaktion, die den OP_RETURN enthält.

Ich fasse die Schritte zusammen, die wir gerade gemeinsam gesehen haben, um eine Benachrichtigungstransaktion zu empfangen und zu interpretieren:

- Bob überwacht die Transaktionsausgänge an seine Benachrichtigungsadresse.

- Wenn er eine entdeckt, ruft er die Informationen aus dem OP_RETURN ab.

- Bob wählt den öffentlichen Schlüssel als Eingabe aus und berechnet einen geheimen Punkt mit ECDH.

- Er verwendet diesen geheimen Punkt, um einen HMAC zu berechnen, der als Blindfaktor dient.

- Er verwendet diesen Blindfaktor, um den Payload des Zahlungscodes von Alice im OP_RETURN zu entschlüsseln.

### Die BIP47-Zahlungstransaktion.

Lassen Sie uns nun gemeinsam den Zahlungsprozess mit BIP47 betrachten. Um den aktuellen Stand der Dinge in Erinnerung zu rufen:

- Alice kennt den Zahlungscode von Bob, den sie einfach von seiner Website abgerufen hat.

- Bob kennt den Zahlungscode von Alice dank der Benachrichtigungstransaktion.

- Alice wird eine erste Zahlung an Bob durchführen. Sie kann weitere Zahlungen auf die gleiche Weise durchführen.

Bevor ich Ihnen diesen Prozess erkläre, denke ich, es ist wichtig, daran zu erinnern, an welchen Indizes wir derzeit arbeiten:

Der Ableitungspfad eines Zahlungscodes wird wie folgt beschrieben: m/47'/0'/0'/.

Der nächste Tiefenindex verteilt die Indizes wie folgt:

- Das erste normale Kindpaar (nicht verstärkt) wird verwendet, um die Benachrichtigungsadresse zu generieren, über die wir im vorherigen Teil gesprochen haben: m/47'/0'/0'/0/.

- Normale Kindschlüsselpaare werden innerhalb von ECDH verwendet, um BIP47-Zahlungsempfangsadressen zu generieren, wie wir in diesem Teil sehen werden: m/47'/0'/0'/ von 0 bis 2 147 483 647/.

- Verstärkte Kindschlüsselpaare sind ephemere Zahlungscodes: m/47'/0'/0'/ von 0' bis 2 147 483 647'/.
  Jedes Mal, wenn Alice eine Zahlung an Bob senden möchte, generiert sie eine neue eindeutige leere Adresse mithilfe des ECDH-Protokolls:

* Alice wählt den ersten abgeleiteten privaten Schlüssel aus ihrem persönlichen wiederverwendbaren Zahlungscode aus:

> a

- Alice wählt den ersten unbenutzten öffentlichen Schlüssel aus, der aus Bobs Zahlungscode abgeleitet wird. Diesen öffentlichen Schlüssel nennen wir "B". Er ist mit dem privaten Schlüssel "b" verbunden, von dem nur Bob Kenntnis hat.

> B = b·G

- Alice berechnet einen geheimen Punkt "S" auf der elliptischen Kurve, indem sie ihren privaten Schlüssel "a" auf Bobs öffentlichen Schlüssel "B" anwendet, indem sie Punkte addiert und verdoppelt:

> S = a·B

- Aus diesem geheimen Punkt berechnet Alice das gemeinsame Geheimnis "s" (kleingeschrieben). Dazu wählt sie die x-Koordinate des geheimen Punktes "S" aus, die sie "Sx" nennt, und gibt diesen Wert in die SHA256-Hashfunktion ein.

> s = SHA256(Sx)

Vertraue nicht, überprüfe! Wenn Sie die Grundprinzipien einer Hashfunktion verstehen möchten, finden Sie in diesem Artikel weitere Informationen. Und wenn Sie dem NIST nicht vertrauen (zu Recht) und den genauen Ablauf von SHA256 verstehen möchten, erkläre ich Ihnen alles in diesem Artikel auf Französisch.

- Alice verwendet dieses gemeinsame Geheimnis "s", um eine Bitcoin-Empfangsadresse zu berechnen. Zunächst überprüft sie, ob "s" im Bereich der Kurve secp256k1 enthalten ist. Wenn dies nicht der Fall ist, erhöht sie den Index des öffentlichen Schlüssels von Bob, um ein anderes gemeinsames Geheimnis abzuleiten.

- Anschließend berechnet sie einen öffentlichen Schlüssel "K0", indem sie die Punkte "B" und "s·G" auf der elliptischen Kurve addiert. Mit anderen Worten, Alice addiert den aus Bobs Zahlungscode abgeleiteten öffentlichen Schlüssel "B" mit einem anderen Punkt, der auf der elliptischen Kurve durch Addition und Verdopplung von Punkten mit dem gemeinsamen Geheimnis "s" vom Kurvengenerator secp256k1 "G" berechnet wird. Dieser neue Punkt repräsentiert einen öffentlichen Schlüssel, den wir "K0" nennen:

> K0 = B + s·G

- Mit diesem öffentlichen Schlüssel "K0" kann Alice eine leere Empfangsadresse auf standardmäßige Weise ableiten (z. B. SegWit V0 in Bech32).

Sobald Alice diese Empfangsadresse "K0" von Bob hat, kann sie eine herkömmliche Bitcoin-Transaktion erstellen, indem sie eine UTXO aus einem anderen Zweig ihrer HD-Brieftasche auswählt und an die Adresse "K0" von Bob ausgibt.

![Alice sendet Bitcoins mit BIP47 an Bob](assets/21.webp)

Quelle: Wiederverwendbare Zahlungscodes für hierarchisch deterministische Brieftaschen, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
Wenn wir dieses Schema mit dem vergleichen, was ich Ihnen zuvor beschrieben habe:

- "Child Priv-Key" auf der Seite von Alice entspricht: a.

- "Child Pub-Key 0" auf der Seite von Bob entspricht: B.

- "Payment Secret 0" entspricht: s.

- "Payment Pub-Key 0" entspricht: K0.

Ich fasse die Schritte zusammen, die wir gerade gemeinsam gesehen haben, um eine BIP47-Zahlung zu senden:

- Alice wählt den ersten abgeleiteten Kind-Privatschlüssel aus ihrem persönlichen Zahlungscode aus.

- Sie berechnet einen geheimen Punkt auf der elliptischen Kurve mit ECDH aus dem ersten unbenutzten abgeleiteten Kind-Publikumsschlüssel aus Bobs Zahlungscode.

- Sie verwendet diesen geheimen Punkt, um ein gemeinsames Geheimnis mit SHA256 zu berechnen.

- Sie verwendet dieses gemeinsame Geheimnis, um einen neuen geheimen Punkt auf der elliptischen Kurve zu berechnen.

- Sie addiert diesen neuen geheimen Punkt zum öffentlichen Schlüssel von Bob.

- Sie erhält einen neuen ephemeren öffentlichen Schlüssel, für den nur Bob den zugehörigen privaten Schlüssel besitzt.

- Alice kann eine normale Transaktion an Bob mit der abgeleiteten ephemeren Empfangsadresse senden.

Wenn sie eine zweite Zahlung durchführen möchte, wiederholt sie die oben genannten Schritte, außer dass sie den zweiten abgeleiteten öffentlichen Schlüssel aus Bobs Zahlungscode auswählt. Das bedeutet, den nächsten unbenutzten Schlüssel. Sie hat dann eine zweite Empfangsadresse, die zu Bob gehört, "K1".

![Alice leitet drei BIP47-Empfangsadressen an Bob ab](assets/22.webp)

Credit: Wiederverwendbare Zahlungscodes für hierarchisch deterministische Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Sie kann so weitermachen und bis zu 2^32 leere Adressen ableiten, die Bob gehören.

Aus Sicht eines Außenstehenden, der die Bitcoin-Blockchain beobachtet, ist es theoretisch unmöglich, eine BIP47-Zahlung von einer normalen Zahlung zu unterscheiden. Hier ist ein Beispiel für eine BIP47-Zahlungstransaktion im Testnetzwerk:

https://blockstream.info/testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

TXID:

> 94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

Es sieht aus wie eine normale Transaktion mit einer verbrauchten Eingabe, einer Zahlungsausgabe von 210.000 Sats und einer Änderung:

![Bitcoin-Zahlungstransaktion mit BIP47](assets/23.webp)

Credit: https://blockstream.info/

### Empfang der BIP47-Zahlung und Ableitung des privaten Schlüssels.

Alice hat gerade ihre erste Zahlung an eine leere BIP47-Adresse von Bob getätigt. Lassen Sie uns nun gemeinsam sehen, wie Bob diese Zahlung erhält. Wir werden auch sehen, warum Alice keinen Zugriff auf den privaten Schlüssel der Adresse hat, den sie gerade generiert hat, und wie Bob diesen Schlüssel findet, um die Bitcoins auszugeben, die er gerade erhalten hat.
Sobald Bob die Benachrichtigungstransaktion von Alice erhält, leitet er den BIP47-öffentlichen Schlüssel "K0" ab, noch bevor sie eine Zahlung dorthin gesendet hat. Er überwacht also jede Zahlung an die zugehörige Adresse. Tatsächlich leitet er sofort mehrere Adressen ab, die er überwacht (K0, K1, K2, K3...). So leitet er den öffentlichen Schlüssel "K0" ab:

- Bob wählt den ersten abgeleiteten Kind-Privatschlüssel aus seinem Zahlungscode aus. Dieser private Schlüssel wird "b" genannt. Er ist mit dem öffentlichen Schlüssel "B" verbunden, mit dem Alice in dem vorherigen Schritt ihre Berechnungen durchgeführt hat:

> b

- Bob wählt den ersten abgeleiteten öffentlichen Schlüssel von Alice aus ihrem Zahlungscode aus. Dieser Schlüssel wird "A" genannt. Er ist mit dem privaten Schlüssel "a" verbunden, mit dem Alice ihre Berechnungen durchgeführt hat und von dem nur Alice Kenntnis hat. Bob kann diesen Prozess durchführen, da er den Zahlungscode von Alice kennt, der ihm zusammen mit der Benachrichtigungstransaktion übermittelt wurde.

> A = a·G

- Bob berechnet den geheimen Punkt "S", indem er Addition und Verdoppelung von Punkten auf der elliptischen Kurve anwendet und seinen privaten Schlüssel "b" auf den öffentlichen Schlüssel von Alice "A" anwendet. Hier verwenden wir ECDH, um sicherzustellen, dass dieser Punkt "S" für Bob und Alice gleich ist.

> S = b·A

- Auf die gleiche Weise wie Alice isoliert Bob die Abszisse dieses Punktes "S". Wir haben diesen Wert "Sx" genannt. Er gibt diesen Wert in die SHA256-Funktion ein, um das gemeinsame Geheimnis "s" zu finden (kleingeschrieben).

> s = SHA256(Sx)

- Auf die gleiche Weise wie Alice berechnet Bob den Punkt "s·G" auf der elliptischen Kurve. Dann addiert er diesen geheimen Punkt mit seinem öffentlichen Schlüssel "B". Er erhält einen neuen Punkt auf der elliptischen Kurve, den er als öffentlichen Schlüssel "K0" interpretiert:

> K0 = B + s·G

Sobald Bob diesen öffentlichen Schlüssel "K0" hat, kann er den zugehörigen privaten Schlüssel ableiten, um seine Bitcoins ausgeben zu können. Er ist der einzige, der diese Zahl generieren kann.

- Bob addiert seinen abgeleiteten Kind-Privatschlüssel "b" zu seinem persönlichen Zahlungscode. Nur er kann den Wert von "b" erhalten. Dann addiert er "b" mit dem gemeinsamen Geheimnis "s", um k0, den privaten Schlüssel von K0, zu erhalten:

> k0 = b + s
> Dank des Gruppenrechts der elliptischen Kurve erhält Bob genau den privaten Schlüssel, der dem von Alice verwendeten öffentlichen Schlüssel entspricht. Wir haben also:
> K0 = k0·G

![Bob generiert seine BIP47-Empfangsadressen](assets/24.webp)

Credit: Wiederverwendbare Zahlungscodes für hierarchisch deterministische Geldbörsen, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Wenn wir dieses Schema mit dem vergleichen, was ich Ihnen zuvor beschrieben habe:

- "Child Priv-Key 0" auf Bobs Seite entspricht: b.

- "Child Pub-Key 0" auf Alice' Seite entspricht: A.

- "Payment Secret 0" entspricht: s.

- "Payment Pub-Key 0" entspricht: K0.

- "Payment Priv-Key 0" entspricht: k0.

Ich fasse die Schritte zusammen, die wir gerade gemeinsam durchgegangen sind, um eine BIP47-Zahlung zu empfangen und den entsprechenden privaten Schlüssel zu berechnen:

- Bob wählt den ersten abgeleiteten privaten Schlüssel aus seinem persönlichen Zahlungscode aus.

- Er berechnet einen geheimen Punkt auf der elliptischen Kurve durch ECDH aus dem ersten abgeleiteten öffentlichen Schlüssel aus Alice' Kettencode.

- Er verwendet diesen geheimen Punkt, um ein mit SHA256 gemeinsam genutztes Geheimnis zu berechnen.

- Er verwendet dieses gemeinsam genutzte Geheimnis, um einen neuen geheimen Punkt auf der elliptischen Kurve zu berechnen.

- Er addiert diesen neuen geheimen Punkt zu seinem persönlichen öffentlichen Schlüssel.

- Er erhält einen neuen ephemeren öffentlichen Schlüssel, an den Alice ihre erste Zahlung senden wird.

- Bob berechnet den privaten Schlüssel, der diesem ephemeren öffentlichen Schlüssel zugeordnet ist, indem er seinen abgeleiteten privaten Schlüssel aus seinem Zahlungscode und das gemeinsam genutzte Geheimnis addiert.

Da Alice nicht "b", Bobs privaten Schlüssel, erhalten kann, ist sie nicht in der Lage, k0, den privaten Schlüssel, der der BIP47-Empfangsadresse von Bob zugeordnet ist, zu bestimmen.

Schematisch können wir die Berechnung des gemeinsam genutzten Geheimnisses "S" wie folgt darstellen:

![Berechnung des gemeinsam genutzten Geheimnisses mit ECDHE](assets/25.webp)

Nachdem das gemeinsam genutzte Geheimnis mit ECDH gefunden wurde, berechnen Alice und Bob den BIP47-Zahlungsöffentlichen Schlüssel "K0", und Bob berechnet auch den zugehörigen privaten Schlüssel "k0":

![Ableitung der BIP47-Empfangsadresse aus dem gemeinsam genutzten Geheimnis](assets/26.webp)

### Rückerstattung der BIP47-Zahlung.

Da Bob den wiederverwendbaren Zahlungscode von Alice kennt, hat er bereits alle erforderlichen Informationen, um ihr eine Rückerstattung zu senden. Er muss Alice nicht kontaktieren, um nach irgendwelchen Informationen zu fragen. Er muss sie lediglich mit einer Benachrichtigungstransaktion informieren, insbesondere damit sie ihre BIP47-Adressen mit ihrem Seed wiederherstellen kann, und er kann ihr bis zu 2^32 Zahlungen senden.
Bob kann Alice dann auf die gleiche Weise zurückerstatten, wie sie ihm Zahlungen geschickt hat. Die Rollen kehren sich um:

![Bob erstattet Alice mit BIP47](assets/27.webp)

Quelle: Wiederverwendbare Zahlungscodes für hierarchisch deterministische Geldbörsen, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Sie kennen nun alle Feinheiten dieser großartigen Lösung namens BIP47.

## Abgeleitete Verwendungen von PayNym.

Die Implementierung von BIP47 in der Samourai Wallet hat zu PayNym geführt, Identifikatoren, die aus den Zahlungscodes der Benutzer berechnet werden. Heute geht ihre Nützlichkeit weit über die Verwendung von BIP47 hinaus.

Das Samourai-Team entwickelt allmählich ein ganzes Ökosystem von Werkzeugen und Diensten rund um den Benutzer-PayNym. Dazu gehören natürlich alle Ausgabewerkzeuge, die die Benutzerprivatsphäre optimieren, indem sie einer Transaktion Entropie hinzufügen und somit plausible Leugnung ermöglichen.

Die gemeinsame Nutzung von Soroban, dem auf Tor basierenden verschlüsselten Kommunikationsnetzwerk, und PayNym hat die Benutzererfahrung bei der Erstellung von gemeinsamen Transaktionen erheblich verbessert, während ein gutes Sicherheitsniveau beibehalten wurde. Auf diese Weise können Stowaway (PayJoin) und StonewallX2-Transaktionen leicht durchgeführt werden, ohne die vielen nicht signierten Transaktionen manuell austauschen zu müssen, die für die Durchführung einer solchen gemeinsamen Transaktion erforderlich sind.

Im Gegensatz zur Verwendung von BIP47 müssen bei diesen gemeinsamen Transaktionen keine Benachrichtigungstransaktionen durchgeführt werden. Es reicht aus, die PayNym zu verknüpfen, um diese Werkzeuge zu verwenden. Es ist nicht erforderlich, sie zu verbinden.

Wenn Sie mehr über gemeinsame Transaktionen und im Allgemeinen über alle Ausgabewerkzeuge der Samourai Wallet erfahren möchten, können Sie den Abschnitt "Ausgabewerkzeuge" in diesem Artikel lesen. Dort finden Sie eine technische Erklärung und eine detaillierte Anleitung für jedes Werkzeug.

Neben diesen gemeinsamen Transaktionen wurde kürzlich beobachtet, dass das Samourai-Team an einem mit PayNym verbundenen Authentifizierungsprotokoll arbeitet: Auth47. Dieses Tool ist bereits implementiert und ermöglicht beispielsweise die Authentifizierung über einen PayNym auf einer Website, die diese Methode akzeptiert. In Zukunft denke ich, dass Auth47 über diese Möglichkeit der Web-Authentifizierung hinaus in ein umfassenderes Projekt rund um das BIP47/PayNym/Samourai-Ökosystem integriert wird. Möglicherweise wird dieses Protokoll verwendet, um die Benutzererfahrung der Samourai Wallet weiter zu optimieren, insbesondere bei der Verwendung von Ausgabewerkzeugen. Es bleibt abzuwarten...

## Meine persönliche Meinung zu BIP47.

Natürlich ist der Hauptnachteil von BIP47 die Transaktionsbenachrichtigung. Der Benutzer muss Gebühren für das Mining dieser Transaktion bezahlen, was für einige lästig sein kann. Auf der anderen Seite ist das Argument des "Spams" in der Bitcoin-Blockchain absolut unannehmbar. Jeder, der die Gebühren für seine Transaktion bezahlt, sollte in der Lage sein, sie in das Register einzutragen, unabhängig von ihrem Zweck. Das Gegenteil zu behaupten, bedeutet, sich für Zensur auszusprechen.
Es ist möglich, dass in Zukunft kostengünstigere Lösungen gefunden werden, um den Zahlungscode des Absenders an den Empfänger zu übermitteln und dieser ihn sicher zu speichern. Aber im Moment ist die Transaktionsbenachrichtigung die Lösung mit den wenigsten Kompromissen.

Dieser Nachteil ist vernachlässigbar, wenn man alle Vorteile von BIP47 betrachtet. Unter allen bestehenden Vorschlägen zur Lösung dieses Problems der Adresswiederverwendung scheint es mir die beste Lösung zu sein.

Wie bereits erklärt, stammen die meisten Adresswiederverwendungen von Börsen. BIP47 ist die einzige vernünftige Lösung, die dieses Problem tatsächlich an der Quelle lösen kann. Jeder Vorschlag, die Anzahl der Adresswiederverwendungen zu reduzieren, sollte diesen Aspekt berücksichtigen und die Lösung an die Hauptursache des Problems anpassen.

In Bezug auf die Verwendung ist das BIP47-Zahlungsverfahren trotz seiner komplexen Mechanismen kinderleicht. Wiederverwendbare Zahlungscodes können daher auch von unerfahrenen Benutzern problemlos übernommen werden.

In Bezug auf die Privatsphäre ist BIP47 sehr interessant. Wie bereits in dem Abschnitt über die Transaktionsbenachrichtigung erklärt, enthüllt der Zahlungscode keine Informationen über abgeleitete temporäre Adressen. Dadurch wird der Informationsfluss zwischen der Bitcoin-Transaktion und der Empfänger-ID unterbrochen, im Gegensatz zur herkömmlichen Verwendung einer Empfangsadresse.

Und vor allem funktioniert die PayNym-Implementierung von BIP47! Sie ist seit 2016 in der Samourai Wallet verfügbar und seit Anfang dieses Jahres in der Sparrow Wallet. Es handelt sich nicht um ein wissenschaftliches Projekt, sondern um eine gestern getestete und heute voll funktionsfähige Lösung.

Hoffentlich werden diese wiederverwendbaren Zahlungscodes in Zukunft von den Akteuren im Ökosystem übernommen, in Wallet-Software implementiert und von Bitcoin-Nutzern verwendet.

Jede wirklich positive Lösung für die Benutzerprivatsphäre muss diskutiert, vorangetrieben und verteidigt werden, damit Bitcoin nicht zum Spielplatz von Unternehmen wird und zum Überwachungsinstrument der Regierungen wird.
Er dachte daran, wie er überall verfolgt und beleidigt worden war, und jetzt hörte er alle sagen, dass er der schönste aller schönen Vögel sei! Selbst der Holunder neigte seine Zweige zu ihm hin und die Sonne strahlte ein so warmes und wohltuendes Licht aus! Da blähten sich seine Federn auf, sein schlanker Hals richtete sich auf und er rief aus vollem Herzen: "Wie konnte ich so viel Glück träumen, als ich nur eine hässliche kleine Ente war?"

## Weitere Informationen:

- Verstehen und Verwenden von CoinJoin auf Bitcoin.

- Verstehen der Derivationspfade einer Bitcoin-Wallet.

- Installation und Verwendung des Bitcoin-Knotens RoninDojo.

### Externe Ressourcen und Dank:

Vielen Dank an LaurentMT und Théo Pantamis für die vielen Konzepte, die sie mir erklärt haben und die ich in diesem Artikel verwendet habe. Ich hoffe, ich konnte sie genau wiedergeben.

Vielen Dank an Fanis Michalakis für das Korrekturlesen dieses Textes und seine fachlichen Ratschläge.

- https://bitcoiner.guide/paynym/
- https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols
