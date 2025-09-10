---
name: Coin Control
description: Machen Sie sich mit Coin Control vertraut, einem wichtigen Werkzeug zum Schutz Ihrer Privatsphäre bei Bitcoin
---
![cover](assets/cover.webp)


*Dieses Tutorial wurde aus [einer Lektion von Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/) importiert.*



## Einführung



Die Solidität des Bitcoin-Protokolls wird durch einfache Schlüsselkonzepte gewährleistet. Unter diesen sticht die Transparenz hervor: Alle Bitcoin-Transaktionen sind öffentlich und für jeden leicht überprüfbar. Obwohl dieses Merkmal ein Meilenstein des Protokolls ist, da es Betrug verhindert und die Echtheit der Gelder gewährleistet, kann es auch eine Herausforderung für die Vertraulichkeit darstellen. **Haben Sie sich gefragt, ob so viel Transparenz Ihre Privatsphäre beeinträchtigen kann?**



Das sollten Sie. Es ist zwar recht einfach, Satoshi ohne KPC zu sammeln, aber Ihre Privatsphäre ist gerade in der Ausgabenphase am meisten gefährdet.



### Was passiert, wenn Sie einen UTXO ausgeben?



Die Ausgabe von Bitcoin ist nicht einfach die Übertragung eines Wertes auf jemand anderen.



Indem Sie einen Ihrer UTXOs verbrauchen, müssen Sie die Bedingungen für die Transparenz des Protokolls erfüllen, da Sie verpflichtet sind, nachzuweisen, dass Sie diese Mittel besitzen. Sie machen sich also verantwortlich für :




- ihren öffentlichen Schlüssel preisgeben;
- eine digitale Signatur zu erstellen.



Der Zeitpunkt der Ausgabe ist daher der kritischste: **Die Ausgabe von Bitcoin ist ein Akt, der bewusst und mit so viel Kontrolle wie möglich erfolgen muss**.



## Coin Kontrolle



Im Bitcoin-Protokoll gibt es Begriffe wie _Konto_ oder _Geldeinheiten_ nicht. Das Konzept von UTXO wird in dem folgenden Kurs, den ich sehr empfehle, hervorragend erklärt:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Mit Bitcoin akkumulieren Sie kleine oder große Rechnungseinheiten, die in Satoshi gemessen werden und durch "unverbrauchte Transaktionsausgaben", die **UTXO**, auch "Münzen" genannt, repräsentiert werden, und die Sie später ausgeben. Wenn Sie UTXOs verwenden, um eine Transaktion zu erstellen, werden sie vollständig zerstört und andere UTXOs werden an ihrer Stelle erstellt.



Software-Geldbörsen werden entwickelt, um diese Wahl automatisch zu treffen, indem sie "zufällig" ausgewählte Münzen verwenden und bestimmte vom Protokoll vorgesehene Algorithmen anwenden. Das einzige Kriterium, das diese Algorithmen erfüllen müssen, ist die Deckung des für die Ausgaben benötigten Betrags.



Sie können UTXOs unterschiedlichen Alters mischen oder die neuesten oder "ältesten" Ausgaben bevorzugen, je nach dem von den Entwicklern gewählten Algorithmus. Die besten Software-Geldbörsen, auch planen, den Benutzer mit einer wichtigen Wahl zu verlassen.



Die "Coin-Steuerung", die auch als "Coin-Auswahl" bezeichnet wird, ist eine Funktion einiger Software-Geldbörsen, mit der Sie **manuell UTXOs auswählen können, die Sie ausgeben möchten, wenn Sie Ihre Transaktion erstellen**.



Angenommen, wir haben einen Wallet mit 3 UTXOs von 21.000, 42.000 bzw. 63.000 Satoshi.



![img](assets/en/01.webp)



Wenn man 24.000 Sats ausgeben muss und die automatische Auswahl einem Algorithmus überlässt, könnte ein guter Software Wallet sich dafür entscheiden, UTXO 1 + UTXO 2 zu kombinieren, um die 24k Sats und Miner Gebühren zu bezahlen, wodurch ein Restbetrag entsteht, der in einen internen Address des Start-Wallet zurückfließt.



![img](assets/en/02.webp)



Nach der Transaktion lässt sich die neue Situation in Wallet, die nur die UTXOs berücksichtigt, wie folgt zusammenfassen.



![img](assets/en/03.webp)



Mit der richtigen Software und Ihrem Bewusstsein hätten Sie jedoch eine andere, in mancher Hinsicht richtigere Wahl treffen können. Zum Beispiel, indem Sie nur den UTXO2 (ab 42.000 Sats) auswählen.



![img](assets/en/04.webp)



Mit einer Endsituation in Ihrem Wallet, auf dem Niveau von UTXO, sieht das anders aus als vorher.



![img](assets/en/05.webp)



## Warum manuelles Coin Control?



![img](assets/en/06.webp)



In den beiden obigen Beispielen ist der Saldo tatsächlich derselbe: 108.280 Sats. Nachdem wir 24.000 Sats ausgegeben haben, würden wir ohne manuelle Auswahl 2 UTXO in Wallet haben; mit der manuellen Kontrolle von Coin haben wir insgesamt 3.



Die Frage, die wir uns stellen könnten, lautet: **Warum all das tun?** Es gibt, oder könnte es geben, verschiedene Gründe, warum wir `UTXO1` nicht verwendet haben, **und sie alle bilden die Grundlage dafür, warum es beim Ausgeben eine gute Praxis ist, die manuelle Coin-Control zu aktivieren**.



Die Auswahl von UTXOs ermöglicht es Ihnen, einige Aspekte gegenüber anderen zu bevorzugen. Die Wahl hängt wirklich von den Zielen ab, die Sie erreichen wollen.



### Datenschutz



Einer der Hauptvorteile der manuellen Coin-Kontrolle ist eine **größere Privatsphäre für den Geldgeber**. Nehmen wir immer unser Beispiel: die Ausgabe von 24.000 Satoshi _ohne manuelle Coin Auswahl_. Da Blockchain von Bitcoin ein öffentlicher Datensatz ist, kann ein außenstehender Beobachter ohne den Schatten eines Zweifels erklären, dass die Eingänge `UTXO1 von 21.000 Sats` und `UTXO2 von 42.000 Sats`, sowie der Rest, der `UTXO5 von 38.280 Sats` **alle drei zu demselben Nutzer gehören**.



Durch die manuelle Auswahl von "UTO2" bleibt dagegen "UTO1" vollständig reserviert und wartet im UTXO-Set darauf, zu einem geeigneteren Zeitpunkt ausgegeben zu werden.



Der "UTXO1" könnte aus einer KYC-Quelle stammen, z. B. aus einer in Exchange erhaltenen Zahlung für Waren und Dienstleistungen, während die anderen UTXOs dies nicht tun. Die Vermischung eines UTXO-KYC mit anderen, die vertraulicher sind, gefährdet die Anonymität von Nicht-KYC-Geldern.



**KYC-Mittel würden unweigerlich zur Rückverfolgung der Identität des Zahlenden führen. Wenn es deine Wallet wäre, würdest du wollen, dass ein externer Beobachter deine Identität mit solcher absoluten Gewissheit nachvollziehen kann?**



Versuchen Sie also zu bedenken, dass Geldbörsen, die z. B. eine manuelle Auswahl von UTXOs implementieren, eine **Trennung von einem oder mehreren UTXOs** ermöglichen, eine Funktion, die in solchen Situationen genutzt werden kann.



Obwohl ich davon überzeugt bin, dass KYC-Gelder in einem separaten Wallet aufbewahrt werden sollten als in einem Bitcoin, der ohne KYC gekauft wurde, ist in diesem Fall die Trennung einiger Ihrer Adressen eine wichtige Hilfe, die Sie sich zunutze machen könnten, indem Sie lernen, Ihre Ausgaben manuell auszuwählen.



### Sparen von Gebühren



Die Auswahl der richtigen UTXO zur Tätigung einer Ausgabe **ermöglicht eine Gebührenoptimierung**. Wiederum ausgehend von unserem ursprünglichen Beispiel hat Software Wallet zwei UTXOs ausgewählt, um die zu tätigenden Ausgaben zu decken. Zwei UTXOs bedeuten zwei Unterschriften, die dem Netz vorgelegt werden müssen. Daraus folgt, dass die Transaktion ein größeres "Gewicht" in Form von vBytes hat.



Mit der manuellen Steuerung des Coin können Sie dagegen nur einen Betrag auswählen, der für die Deckung ausreicht, und so Gebühren sparen, indem Sie das "Gewicht" der Transaktion verringern.



In Zeiten, in denen die Gebühren hoch sind, Sie aber gezwungen sind, Bitcoin On-Chain auszugeben (z. B. um einen Lightning Network-Kanal zu eröffnen), erweist sich die Coin-Kontrolle als der richtige wirtschaftliche Anreiz, auf den Sie zurückgreifen sollten.



### Aggregation der Überreste



Wenn Sie eine Zahlung vornehmen und Bitcoin On-Chain verwenden, wird die Möglichkeit, Wechselgeld zu erhalten, fast immer zu einer Gewissheit. Jeder Restbetrag stellt selbst einen kleinen Verlust an Privatsphäre dar, da er dem Netz (und insbesondere dem Empfänger der Zahlung) einen Address von Ihnen offenbart, der mit Ihrer Quelleingabe in Verbindung gebracht werden kann.



In Anbetracht der Tatsache, dass die besten Wallet HDs generate spezielle Adressen für die Reste, können Sie leicht erkennen und "trennen" alle Reste der verschiedenen Transaktionen gemacht; wenn sie einen bestimmten Betrag erreicht haben, können Sie sie manuell auswählen und konsolidieren sie, oder wechseln Sie zu Lightning Network (meine bevorzugte Methode) und verarbeiten sie so, um die Privatsphäre verloren in Ausgaben wieder.



### Ausgaben aus einem Cold Wallet



Das Cold Wallet ist ein Instrument, mit dem man vernünftigerweise ein gutes Maß an Sicherheit erlangen kann, um einen beliebigen Geldbetrag für einen langen Zeitraum zur Seite zu legen. Es können jedoch unvorhergesehene Ereignisse eintreten, so dass die Notwendigkeit entsteht, auf die Ersparnisse zuzugreifen und einige unerwartete Ausgaben zu tätigen.



Ich weiß nicht, wie viele meinen Ansatz teilen können, aber mein Rat ist, **nie die Ausgaben direkt von Cold Wallet, um zu vermeiden, erhalten die Änderung zwischen den Adressen der gleichen**. Lernen Sie, die UTXOs, die zur Deckung der Ausgabe benötigt werden, manuell auszuwählen, sie auf einen Wallet Hot zu übertragen und Ihre Transaktion von letzterem aus vorzubereiten. Eventuelles Wechselgeld können Sie dann an einen Cold Wallet Address zurückschicken (wenn der Betrag ausreicht), für andere Ausgaben verwenden oder wie soeben gesehen abtrennen.



## Praktische Präsentation


Nach der technischen Einführung des "Warum" sehen wir uns an, wie die manuelle Steuerung des Coin in der Praxis mit verschiedener Software, Desktop und Mobile, umgesetzt werden kann. Wir werden immer dasselbe Wallet BIP39 verwenden, das in jedes der ausgewählten Tools importiert wird, um Ihnen die kleinen Unterschiede zwischen ihnen zu zeigen.



## Wallet Schreibtisch



### Sparrow



Wenn Sie Sparrow verwenden, öffnen Sie Ihren Wallet und wählen Sie _UTXOs_ aus dem Menü auf der linken Seite. Es wird eine Liste aller UTXOs angezeigt, die mit Ihrem Wallet verbunden sind.



Klicken Sie einfach mit der Maus auf einen der Befehle und wählen Sie dann _Ausgewählte senden_. Sparrow zeigt Ihnen auch die Gesamtsumme an, die Sie nach der Auswahl ausgeben können, direkt neben dem Befehl. Grafisch zeigt Ihnen Sparrow den ausgewählten UTXO durch blaue Markierung an.



![img](assets/en/07.webp)



Sie können auch mehr als einen auswählen. Verwenden Sie die Taste _CTRL_, um nicht benachbarte UTXOs in der Liste auszuwählen.



![img](assets/en/08.webp)



Nach der manuellen Auswahl von UTXO können Sie mit der Erstellung der Transaktion beginnen, und Sparrow zeigt Ihnen grafisch, wie sie aufgebaut ist.



![img](assets/en/09.webp)



#### Abtrennung von UTXO



Das Trennen von Geldern bedeutet, dass sie im Wallet "gesperrt" werden, damit sie nicht als Input für eine Transaktion verwendet werden können. Sparrow ermöglicht diese Funktion, auf die man immer über das Menü _UTXOs_ zugreift: Sie platzieren die Maus über dem zu "sperrenden" UTXO und klicken die rechte Maustaste. Unter den Funktionen dieses Verfahrens erscheint _Freeze UTXO_. Auf diese Weise können Sie Coins mit Sparrow-Geldbörsen trennen.



![img](assets/en/29.webp)



### Elektrum



Wenn Ihr Wallet-Desktop Electrum ist, sollten Sie wissen, dass Sie UTXOs entweder aus dem Menü _Adressen_ oder aus dem Menü _Münzen_ manuell auswählen können. In beiden Menüs erfolgt die Auswahl, indem Sie mit der Maus auf den gewünschten UTXO zeigen und nach einem Rechtsklick _Add to Coin control_ wählen.



![img](assets/en/10.webp)



Auch mit dieser Software können Sie mehr als einen UTXO auswählen, indem Sie die Taste _CTRL_ auf Ihrer Tastatur drücken, wenn sie nicht nebeneinander liegen.



![img](assets/en/11.webp)



Electrum zeigt Ihnen die Auswahl grafisch an, indem es die ausgewählten UTXOs in Green hervorhebt, während am unteren Rand ein Balken in derselben Farbe erscheint, der die verfügbare Balance nach der Coin-Kontrolle anzeigt.



![img](assets/en/12.webp)



Sobald Sie die Ausgabe(n) ausgewählt haben, können Sie Ihre Transaktion wie gewohnt über das Menü _Senden_ erstellen.



#### Abtrennung von UTXO



Electrum bietet diese Funktion, indem Sie auf das Menü _Coins_, wo Sie gehen, um eine bestimmte UTXO und dann wählen Sie _Freeze_ mit einem Rechtsklick. Sie können "einfrieren" die Address auch ohne Mittel aus dem Menü _Adressen_, oder die "Coin", um es nicht ausgeben.



![img](assets/en/28.webp)



### Nunchuk



Mit Nunchuk können Sie UTXOs manuell aus dem Hauptmenü auswählen, sobald es geöffnet ist. Starten Sie Nunchuk und klicken Sie auf _Münzen anzeigen_.



![img](assets/en/13.webp)



Es öffnet sich das Fenster mit allen UTXOs in Ihrem Wallet, aus dem Sie einen oder mehrere auswählen können, indem Sie das Häkchen neben dem jeweiligen Betrag aktivieren. Nachdem Sie Ihre Auswahl getroffen haben, fahren Sie mit _Transaktion erstellen_ fort.



![img](assets/en/14.webp)



Danach können Sie den Ziel-Address eingeben und den Betrag und die Gebühren festlegen.



![img](assets/en/15.webp)



#### Abtrennung von UTXO



Der Vollständigkeit halber sei erwähnt, dass Nunchuk unter anderem auch die Möglichkeit bietet, eine (oder mehrere) UTXOs zu trennen, und zwar auf zwei verschiedene Arten. Rufen Sie das Menü _Münzen anzeigen_ auf und wählen Sie manuell aus der Liste der Münzen. Klicken Sie dann auf das Menü _Mehr_ unten rechts: Es erscheint eine Liste mit Optionen, aus der Sie _Münzen sperren_ wählen können.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Sie können auch in das für UTXO reservierte Feld klicken, um das Fenster _Münzdetails_ aufzurufen. Hier erscheint in der oberen rechten Ecke der Befehl zum Sperren/Entsperren des betreffenden UTXO.



![img](assets/en/41.webp)



### Blockstream App



Blockstream App desktop, früher bekannt als Green, ermöglicht Ihnen die Auswahl von Coin, wenn Sie bereits mit der Erstellung der Transaktion begonnen haben. Öffnen Sie also Ihren Wallet und klicken Sie auf _Senden_.



![img](assets/en/16.webp)



Fügen Sie den Ziel-Address in das entsprechende Feld ein und wählen Sie dann _Manuelle Coin-Auswahl_.



![img](assets/en/17.webp)



Es öffnet sich ein Fenster, in dem Sie eine oder mehrere UTXO-Münzen auswählen können. Im folgenden Beispiel haben wir zwei Münzen ausgewählt. Bestätigen Sie anschließend Ihre Wahl, indem Sie auf _Coin Auswahl bestätigen_ klicken.



![img](assets/en/18.webp)



Legen Sie den Betrag und die Gebühren fest und fahren Sie dann ganz normal mit Ihrer Transaktion fort.



![img](assets/en/19.webp)



⚠️ N.B. Im Menü _Coins_ von Green gibt es _Lock_/_Unlock_ Punkte, die auf die Möglichkeit der Trennung von UTXO hinweisen. Diese Funktion ist nur in so genannten Multisig-Konten aktiviert; sie wird auch nur aktiviert, wenn man UTXO mit einem sehr geringen Betrag auswählt, der nahe an der Schwelle von "Dust" liegt.



## Wallet mobil



Es können auch Geldbörsen von Mobiltelefonen gewählt werden, die eine manuelle Auswahl von UTXOs ermöglichen. Betrachten wir Blue Wallet als erstes Beispiel.



### Blau Wallet



Wenn Sie ein Benutzer dieses Wallet sind, öffnen Sie es und klicken Sie auf , um die Kontrollbildschirme für eine Ihrer Geldbörsen aufzurufen. Um auf das Coin-Kontrollhandbuch zuzugreifen, müssen Sie die Ausgabenphase eingeben und dann auf _Senden_ klicken.



![img](assets/en/21.webp)



Wählen Sie auf dem nächsten Bildschirm die Menüs aus, die durch die drei Punkte in der oberen rechten Ecke gekennzeichnet sind. Es öffnet sich ein Dropdown-Fenster mit einer Reihe von Befehlen. Wählen Sie den letzten Befehl: _Münzkontrolle_.



![img](assets/en/22.webp)



An dieser Stelle zeigt das blaue Wallet alle Ihre UTXOs an. Zusätzlich zu den Beträgen werden sie grafisch durch verschiedene Farben unterschieden.



![img](assets/en/27.webp)



Wählen Sie das UTXO aus und wählen Sie dann _Münze verwenden_.



![img](assets/en/23.webp)



Das blaue Wallet bringt Sie zurück zum Fenster _Senden_, um mit der Erstellung der Transaktion fortzufahren. Passen Sie den Betrag und die Gebühren an, und wählen Sie dann _Weiter_.



![img](assets/en/24.webp)



An diesem Punkt können Sie die Transaktion wie üblich beenden.



#### Abtrennung eines UTXO



Mit dem blauen Wallet können Sie auch UTXOs aussortieren, so dass sie nicht mehr ausgegeben werden können - keine schlechte Funktion für einen Wallet von einem mobilen Gerät aus. Sie rufen die Coin-Steuerung mit dem soeben erläuterten Verfahren auf und wählen nach der Auswahl des UTXO die Option _Freeze_ anstelle von _Use Coin_.



![img](assets/en/26.webp)



### Nunchuk



Die mobile Version des Nunchuk bietet dem Benutzer auch die Möglichkeit, den Coin zu steuern. Wenn Sie diese App auf dem Handy verwenden, öffnen Sie sie und gehen Sie zum Menü _Wallet_. Wählen Sie dort _Münzen anzeigen_.



![img](assets/en/30.webp)



Klicken Sie in dem Fenster, in dem die Liste der UTXOs erscheint, auf _Auswählen_.



![img](assets/en/38.webp)



Neben jedem UTXO erscheint eine Auswahlfunktion. Wie in der Desktop-Version erfolgt die manuelle Auswahl auf dem Nunchuk mobile durch Ankreuzen des kleinen Quadrats neben der Menge. Der Bildschirm zeigt die Anzahl der ausgewählten UTXOs und die verfügbare Gesamtmenge an. Wenn Sie fertig sind, klicken Sie auf das ₿-Symbol in der unteren linken Ecke, das den Befehl zum Starten der Transaktion gibt.



![img](assets/en/31.webp)



Nun können Sie die Transaktion abschließen, indem Sie den Betrag auswählen und auf _Fortfahren_ klicken.



![img](assets/en/32.webp)



Fahren Sie wie gewohnt fort und fügen Sie einen Ziel-Address und eine Beschreibung ein und passen Sie die Gebühreneinstellungen an.



#### Abtrennung von UTXO



Sie können UTXOs auch mit dem mobilen Nunchuk aussondern. Rufen Sie das Fenster mit der Münzliste auf und wählen Sie den Pfeil neben dem UTXO, den Sie trennen möchten.



![img](assets/en/42.webp)



Sie sehen das Feld _Münzdetails_, in dem Sie _Diese Münze sperren_ auswählen können.



![img](assets/en/43.webp)



### Bitcoin Keeper



Der Bitcoin Keeper ist der letzte Wallet, den wir in diesem Leitfaden sehen werden. Wir sehen seine Funktionalität bei der Coin-Kontrolle mit einer Wallet-Einzelunterschrift, obwohl eine solche Verwendung nicht der Zweck dieser speziellen Anwendung ist. Nachdem Sie Keeper auf Ihrem Telefon eingerichtet haben, starten Sie es und öffnen Sie ein Wallet, das etwas Geld enthält. Klicken Sie in der Mitte des Hauptbildschirms auf _Alle Münzen anzeigen_.



![img](assets/en/34.webp)



Keeper zeigt eine Übersicht über die UTXOs. Um den Auswahlbildschirm aufzurufen, klicken Sie auf _Select To Send_.



![img](assets/en/35.webp)



Sie können Münzen auswählen, indem Sie sie abhaken, indem Sie auf den entsprechenden Befehl klicken. Wenn Sie fertig sind, klicken Sie auf _Senden_.



![img](assets/en/36.webp)



Bitcoin Keeper führt Sie direkt zum Menü _Senden_, wo Sie die Transaktion mit den ausgewählten UTXOs erstellen können.



![img](assets/en/37.webp)



## Hardware Wallet



Jede der in diesem Leitfaden vorgestellten Software-Geldbörsen kann die einzige Interface für eine Ihrer Hardware-Geldbörsen sein. Das bedeutet, dass die Coin-Steuerung für das Offline-Signiergerät mit den bisher gesehenen Schritten durchgeführt wird.



### Allgemeine Empfehlungen



Die Coin-Kontrolle ist eine sehr effektive Methode zur Auswahl Ihrer Transaktionsinputs. Die manuelle Auswahl ist sogar noch effizienter, wenn Sie beim Kauf/Empfang Ihrer Mittel die Quelle Ihrer Satoshis gut gekennzeichnet haben. Wenn Sie diese Technik gut erlernen wollen, empfehle ich Ihnen das folgende Tutorial:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Wir haben bereits über die "Trennung von Resten" gesprochen. Wenn Sie Reste für die spätere Verarbeitung sperren und die Privatsphäre wiederherstellen wollen (Tausch auf Layer 2), müssen Sie darauf achten, sie jedes Mal zu "etikettieren", wenn Sie einen erhalten. Von den bisher vorgestellten Software-Geldbörsen färbt nur Electrum UTXO-Reste grafisch ein, um sie auf einen Blick sichtbar zu machen. Andere, wie Sparrow, zeigen Ihnen die Kette im Ableitungspfad des einzelnen UTXO (`m/84'/0'/0'/1/11`).



Um diese Technik effektiv anzuwenden, denken Sie daran, dem Wechselgeld, das Sie erhalten, immer eine Beschreibung hinzuzufügen: Die Person, an die Sie Ihr Geld geschickt haben (eine Zahlung, ein Tutorium oder etwas anderes), kennt den Address, der mit dem Wechselgeld verbunden ist, und weiß, dass es Ihnen gehört, da es aus einer gemeinsamen Transaktion stammt!