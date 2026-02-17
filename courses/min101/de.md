---
name: Einführung in Bitcoin mining
goal: Bitcoin mining und proof-of-work von Grund auf verstehen
objectives: 


  - Verstehen Sie proof-of-work und seine Rolle in Bitcoin.
  - Analysieren Sie den Mechanismus zur Anpassung der Schwierigkeit.
  - Sie müssen wissen, was die technischen Begriffe im Zusammenhang mit mining bedeuten.
  - Beschreiben Sie die Schritte, die zum Bau eines Bitcoin-Blocks und seiner Komponenten gehören.
  - Ermittlung der wichtigsten Entwicklungen in der mining-Industrie.


---

# Entdecken Sie die Grundlagen von Bitcoin mining



Wer den proof of work versteht, versteht auch, wie der Bitcoin funktioniert. Ohne diese Erfindung und ihre geniale Anwendung hätte es Bitcoin einfach nicht geben können. Dieser Kurs vermittelt Ihnen die gesamte mining-Theorie, die Sie für Ihre Bitcoin-Reise benötigen.



MIN 101 richtet sich in erster Linie an Anfänger, da es alle Konzepte von Grund auf erklärt. Wenn Sie jedoch bereits über ein mittleres Wissensniveau verfügen, können Sie in diesem Kurs Ihr Verständnis festigen, einige ungefähre Annahmen korrigieren und Details erkunden, die in den gängigen Erklärungen oft fehlen.



Am Ende dieses Kurses werden Sie in der Lage sein, die Funktionsweise von proof-of-work auf einfache und rigorose Weise zu erklären. MIN 101 ist auch ein idealer Einstieg in alle anderen fortgeschrittenen Kurse, die sich mit Bitcoin, mining und Plan ₿ Academy befassen, egal ob theoretisch oder praktisch.



+++


# Einführung


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Überblick über den Kurs


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



Willkommen zum MIN 101-Kurs, in dem Sie die grundlegenden theoretischen Konzepte von mining und Proof-of-Work innerhalb des Bitcoin-Systems entdecken werden. Dieser Kurs ist der erste Schritt auf Ihrer bitcoiner Reise, um zu verstehen, wie mining funktioniert. Sobald Sie ihn abgeschlossen haben, können Sie zu fortgeschritteneren Theoriekursen übergehen oder selbst zum Bitcoin-Miner werden!



In diesem MIN-101-Kurs werden wir nicht noch einmal die grundlegenden Konzepte von Bitcoin durchgehen, sondern direkt zum Kern der Sache kommen: mining. Wenn Sie noch nie etwas von Bitcoin gehört haben oder wenn Ihnen die Grundlagen noch nicht ganz klar sind, empfehle ich Ihnen dringend, mit unserem Einführungskurs BTC 101 zu beginnen. Sobald Sie sich diese Grundlagen angeeignet haben, können Sie MIN 101 mit Zuversicht in Angriff nehmen:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Teil 1 - Einführung



Wir beginnen diesen Kurs mit einem optionalen ersten Kapitel, in dem ich eine sehr vereinfachte Erklärung von mining gebe, um Ihnen ein klares mentales Bild zu vermitteln, bevor wir uns mit den technischen Mechanismen befassen.



Es geht hier nicht darum, Ihnen alle technischen Details zu vermitteln (die kommen später im Kurs), sondern Ihnen einen roten Faden zu geben. Sobald dieses Gerüst steht, wird sich jedes fortgeschrittenere Konzept, das später eingeführt wird, ganz natürlich in diese Struktur einfügen.



### Teil 2 - Wie proof of work funktioniert



Nach der Einführung ist Teil 2 die technische Grundlage des Schulungsprogramms. Sein Ziel ist es, Schritt für Schritt zu erklären, wie Bitcoin gültige Blöcke erzeugt. Wir beginnen mit der Entdeckung der Struktur eines Blocks, bevor wir auf den proof-of-work-Mechanismus eingehen: die Rolle des Ziels, der Nonce und der Hash-Funktion. Schließlich werden wir sehen, wie Bitcoin dank des Mechanismus zur Anpassung der Schwierigkeit eine stabile Blockproduktionsrate trotz Schwankungen in der Hash-Leistung aufrechterhalten kann. Am Ende dieses Abschnitts werden Sie die grundlegenden Prinzipien von Bitcoin's proof-of-work vollständig verstanden haben.



### Teil 3 - Das Anreizsystem Bitcoin mining



Im dritten Teil werden wir uns ansehen, warum Miner ermutigt werden, sich ehrlich an mining zu beteiligen. Wir werden das Prinzip der Blockbelohnung, ihre Zusammensetzung und Berechnungsmethode, ihre Entwicklung im Laufe der Zeit durch Halvings und die besondere Rolle der Coinbase-Transaktion im Detail erläutern.



### Teil 4 - Die Bitcoin-mining-Industrie



Im vierten Teil wird der mining in seine betriebliche Realität zurückversetzt. Er zeichnet die Entwicklung der mining-Maschinen nach, von den Anfängen des Bitcoin bis zum modernen ASIC, um die aktuellen Hardwarebeschränkungen zu verstehen. Wir schauen uns auch die Grundlagen der mining-Pools an, um zu verstehen, wie es den Minern gelingt, die Varianz ihrer Einnahmen zu verringern.



### Teil 5 - Letzter Abschnitt



Im letzten Teil des Kurses können Sie Ihre mining-Kenntnisse in Form eines Diploms überprüfen.



Ziel dieses MIN 101-Kurses ist es daher, Ihnen ein klares, strukturiertes und nachhaltiges Verständnis von Bitcoin mining zu vermitteln, sowohl technisch als auch wirtschaftlich.



Sind Sie bereit, Bitcoin mining zu entdecken? Fangen wir an!




## Bitcoin mining leicht gemacht


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Bevor ich zu einer detaillierten und technischeren Erklärung von Bitcoin mining übergehe, möchte ich Ihnen einen Überblick über das Prinzip geben, das bewusst einfach und schematisch gehalten ist. Wenn Sie bereits über ein gewisses Grundwissen verfügen, können Sie im nächsten Kapitel, nach Beantwortung der Quizfragen, direkt zum Kern der Sache vordringen. Dieses Kapitel richtet sich vor allem an Anfänger, um Ihnen einen sanften Einstieg zu ermöglichen.



Stellen Sie sich Bitcoin wie ein großes öffentliches Notizbuch vor, das von allen genutzt wird und in dem wir aufschreiben, wer wem Bitcoins geschickt hat. Dieses Notizbuch wird Blockchain genannt. Sie kann nicht von nur einer Person geführt werden, sonst müsste man ihr vertrauen. Stattdessen funktioniert Bitcoin kollektiv: Tausende von Computern verifizieren und pflegen dieselbe Version dieses Notizbuchs.



![Image](assets/fr/049.webp)



Wenn Sie in Bitcoin eine Zahlung vornehmen, legen Sie eine Transaktion an. Diese Transaktion wird nicht sofort dem Notebook hinzugefügt. Sie wird zunächst an das Netzwerk gesendet und wartet dann darauf, in das nächste Transaktionspaket integriert zu werden. Dieses Paket wird als Block bezeichnet.



![Image](assets/fr/050.webp)



Ein Block ist einfach eine Reihe von Transaktionen, die in Gruppen zusammengefasst sind. Wenn ein Block fertig ist, reicht es nicht aus, ihn zu veröffentlichen. Man muss dem Netzwerk beweisen, dass der Block es wert ist, in den Pool aufgenommen zu werden. An dieser Stelle kommt mining ins Spiel.



Mining ist die Arbeit der Validierung eines Blocks durch den Verbrauch von Energie. Akteure, die Miner genannt werden, verwenden spezielle Computer. Diese Maschinen verbrauchen Strom, um in einer Schleife eine sehr große Anzahl von Tests durchzuführen, bis sie einen Beweis finden, den das Netz akzeptiert. Wenn ein Miner diesen Beweis findet, gilt sein Block als gültig.



Sobald der Block validiert wurde, wird er an das Netz gesendet. Die anderen Knoten prüfen schnell, ob er den Regeln entspricht, und fügen ihn dann der Reihe der vorherigen Blöcke hinzu. Deshalb nennt man sie auch "Blockchain": Jeder neue Block kommt nach den anderen, in sequentieller Reihenfolge, und diese Kette wächst nach und nach.



![Image](assets/fr/051.webp)



Zusammenfassend lässt sich sagen, dass die Transaktionen zunächst erstellt werden. Dann werden sie in einem Block zusammengefasst. Dann validiert ein Miner diesen Block, indem er Strom verbraucht. Schließlich wird dieser Block der Blockchain hinzugefügt, und die darin enthaltenen Transaktionen werden bestätigt.



Wenn Bergleute Strom verbrauchen, dann nicht, weil sie Freiwillige sind. Sie tun es, weil es eine Belohnung gibt. Wenn ein Miner einen Block validiert, erhält er zwei Arten von Einkommen. Zum einen erhält er neu geschaffene Bitcoins. Zum anderen kassiert er die Gebühren, die von den Nutzern für die im Block enthaltenen Transaktionen gezahlt wurden. Mit anderen Worten: Der Miner wird sowohl durch die programmierte Ausgabe von Geld als auch durch die von einem Markt festgelegten Transaktionsgebühren entschädigt.



In diesem Stadium wird Ihnen absichtlich ein sehr einfacher Einblick in mining gewährt. Es wird noch nicht erklärt, wie der Block im Detail aufgebaut ist, oder wie genau der Beweis funktioniert, nach dem die Miner suchen, oder wie Bitcoin ein gleichmäßiges Tempo hält, oder wie die Belohnung genau berechnet wird, oder wie sie eingefordert wird. Das ist okay, das ist alles, was wir im Rest dieses MIN 101 Kurses sehen werden!



Das Ziel dieses Kapitels war einfach, Ihnen eine klare gedankliche Struktur zu geben: Transaktionen → Blöcke → mining → Blockchain → Belohnung. Behalten Sie diese Gedankenkette im Kopf. Im weiteren Verlauf des Kurses wird jedes Kapitel eine Schicht technischer Details zu einem dieser Elemente hinzufügen, bis Sie nicht nur verstehen, was vor sich geht, sondern auch wie und warum es zuverlässig, in großem Maßstab, ohne Chef und ohne Vertrauen funktioniert.



# Wie funktioniert proof of work?


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## Der Bitcoin-Transaktionspfad


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



Um zu verstehen, was es mit Bitcoin mining auf sich hat, müssen wir zunächst den Weg einer typischen Bitcoin-Transaktion verfolgen. Das wird Ihnen genau zeigen, wo der Block ins Spiel kommt und warum er das Herzstück des Systems ist. Genau das möchte ich Ihnen in diesem ersten Kapitel zeigen.



In Bitcoin ist eine Transaktion eine Datenstruktur, die das Eigentum an Bitcoins von einem Nutzer auf einen anderen überträgt. Konkret verbraucht sie "Ausgaben" aus vergangenen Transaktionen (sogenannte UTXO), die als "Eingaben" bezeichnet werden, und erstellt dann neue "Ausgaben", die festlegen, wem diese Bitcoins nun gehören und unter welchen Bedingungen sie später ausgegeben werden können.



![Image](assets/fr/001.webp)



Ein wichtiger Punkt bei Bitcoin ist die Ausgabeberechtigung. Bitcoin befinden sich nicht auf einem Konto, wie etwa Ihr Geld auf der Bank, sondern sind durch Ausgabenbedingungen gesperrt. Wenn ein wallet einen UTXO als Eingabe verwenden will, muss er kryptografisch nachweisen, dass er das Recht hat, ihn zu entsperren. Dieser Nachweis erfolgt häufig in Form einer digitalen Signatur generated eines privaten Schlüssels. Aus diesem Grund bestehen Bitcoiner darauf, ihre privaten Schlüssel zu sichern: Sie sind es, die den Zugang zu ihren Bitcoins freischalten und es ihnen folglich ermöglichen, sie auszugeben.



![Image](assets/fr/002.webp)



Die digitale Signatur in Bitcoin spielt zwei wichtige Rollen:




- Ausgabe genehmigen: Dies beweist, dass der Benutzer den privaten Schlüssel besitzt, der von der UTXO-Ausgabebedingung erwartet wird;
- Integritätsschutz: verbindet die Autorisierung mit den genauen Details der Transaktion (Empfänger, Beträge, Gebühren usw.). Wenn jemand die Transaktion nachträglich verändert, ist die Signatur nicht mehr gültig.



Sobald die Transaktion korrekt aufgebaut und vom Bitcoin wallet des Benutzers signiert wurde, muss sie im Bitcoin-Netz übertragen werden.



### Die Rolle des Bitcoin-Knotens bei der Verteilung



Bitcoin ist ein Peer-to-Peer-Netzwerk: Es gibt keinen zentralen Server, der alle Transaktionen empfängt und verarbeitet. Diese Rolle wird von den Knotenpunkten gemeinsam wahrgenommen. Ein Bitcoin-Knoten ist ein Stück Software (z. B. Bitcoin Core), das mit anderen Knoten im Bitcoin-Netzwerk verbunden ist und dessen Hauptaufgabe darin besteht, Transaktionen und Blöcke zu überprüfen, zu speichern und weiterzuleiten.



Wenn Sie eine Transaktion von einem wallet senden, leitet der wallet sie an einen Knoten weiter (Ihren eigenen oder den eines Dienstes). Dieser Knoten prüft zunächst, ob die Transaktion verschiedenen Regeln entspricht, wie z. B.:




- unterschriften gültig sind;
- die Eingaben beziehen sich auf bestehende UTXO (d. h. existierende Bitcoins);
- diese UTXO nicht bereits anderweitig ausgegeben worden sind;
- die Menge der Outputs ist kleiner oder gleich der Menge der Inputs (Bitcoins werden nicht aus dem Nichts geschaffen);
- usw.



Wenn die Transaktion all diese Prüfungen bestanden hat, gibt der Knoten sie an die anderen Knoten des Netzes weiter, mit denen er verbunden ist. Diese wiederum prüfen die Transaktion und leiten sie weiter, und so weiter. Innerhalb weniger Sekunden wird die Transaktion verbreitet und ist dem gesamten oder zumindest einem großen Teil des Bitcoin-Netzes bekannt.



![Image](assets/fr/003.webp)



### Der mempool: das Wartezimmer für Transaktionen



Zwischen dem Moment, in dem eine Transaktion gesendet wird, und dem Moment, in dem sie in einem Block bestätigt wird, muss sie warten. Dieser Wartebereich wird **mempool** genannt (Zusammenziehung von `memory` und `pool`). Ein Mempool ist also ein temporärer Speicherplatz für gültige, aber noch unbestätigte Transaktionen.



Wichtiger Punkt: Es gibt keinen einzigen Mempool, sondern nur Mempools. Jeder Knoten verwaltet seinen eigenen Mempool mit seinen eigenen lokalen Beschränkungen. Das bedeutet, dass zwei Knoten zu einem bestimmten Zeitpunkt leicht unterschiedliche Mempool-Inhalte haben können (je nachdem, was sie erhalten, was sie abgelehnt oder was sie gelöscht haben).



![Image](assets/fr/004.webp)



In diesem Stadium weiß das Netzwerk von der Transaktion, hat sie verifiziert und hält sie im Speicher, bis sie bestätigt wird. Die Bestätigung dieser Transaktion erfolgt jedoch erst, wenn ein Miner sie in einen Block einfügt und dieser Block vom Netzwerk akzeptiert wird.



### Blockchain: ein öffentliches Zeitstempelregister



Da es sich bei Bitcoin um eine immaterielle Währung handelt, muss ein Problem gelöst werden: die Vermeidung von Doppelausgaben ohne eine zentrale Behörde. Wenn zwei Transaktionen versuchen, denselben UTXO auszugeben, müssen alle in der Lage sein, sich auf einen einzigen, kohärenten Zustand zu einigen. Satoshi Nakamoto fasst dieses Problem mit diesem berühmten Satz zusammen:



> Die einzige Möglichkeit, das Nichtvorhandensein einer Transaktion zu bestätigen, besteht darin, sich aller Transaktionen bewusst zu sein.

Mit anderen Worten: Um zu wissen, dass ein Bitcoin noch nicht ausgegeben wurde, braucht man eine gemeinsame Aufzeichnung der bisherigen Ausgaben.



Dies ist die Rolle der Blockchain: ein öffentliches Register, das die Geschichte der Transaktionen enthält. Aber anstatt jede Transaktion zu schreiben, sobald sie stattfindet, fasst Bitcoin sie in Blöcken zusammen. Jeder Block fungiert als Verlaufsseite, und das System funktioniert somit wie ein Zeitstempel-Server: Es ordnet die Transaktionen im Laufe der Zeit auf nachprüfbare Weise.



Dieses Register kann dank eines einfachen Prinzips nicht überschrieben werden: Jeder Block enthält den kryptografischen Fingerabdruck (Hash) des vorherigen Blocks. Die Blöcke sind also miteinander verknüpft: Wenn Sie einen Block aus der Vergangenheit ändern, ändert sich sein Hash, wodurch die Verknüpfung mit dem nächsten Block unterbrochen wird, was wiederum die Verknüpfung mit dem übernächsten Block unterbricht, und so weiter. Diese Kette von Abhängigkeiten gibt der "*Blockchain*" ihren Namen.



![Image](assets/fr/005.webp)



Wenn wir diese Grundprinzipien von Bitcoin verstanden haben, können wir das Ziel eines Miners konkreter beschreiben: einen neuen Block zu erstellen, der die bestehende Kette erweitert, indem er ausstehende Transaktionen einträgt, und dann zu versuchen, ihn gültig zu machen (dies ist der berühmte "proof of work", den wir in einem späteren Kapitel untersuchen werden). Doch zunächst wollen wir im nächsten Kapitel gemeinsam herausfinden, wie ein Kandidatenblock konstruiert wird.



## Bau eines Bitcoin-Blocks


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Sie haben nun verstanden, wie eine Bitcoin-Transaktion funktioniert und welche Rolle die Blockchain spielt. Bevor wir uns jedoch genauer ansehen, wie proof-of-work funktioniert, gibt es noch einen wesentlichen Schritt, den der Miner ausführen muss: die Konstruktion eines Kandidatenblocks. Lassen Sie uns gemeinsam herausfinden, was ein Kandidatenblock ist und wie der Miner ihn konstruiert, bevor wir uns auf die Suche nach einem gültigen Beweis machen.



### Der Kandidatenblock



Miner müssen ihre Blöcke selbst erstellen, bevor sie versuchen, sie abzubauen. Jeder Miner wiederum konstruiert aus den in seinem Mempool anstehenden Transaktionen einen so genannten Kandidatenblock. Der Aufbau eines Kandidatenblocks besteht also aus folgenden Schritten:




- auswählen, welche Transaktionen aufgenommen werden sollen;
- diese Vorgänge in einer Weise zu organisieren, die mit den Bitcoin-Vorschriften vereinbar ist;
- die in der Kopfzeile des Blocks gespeicherten Metadaten erzeugen.



Die Auswahl der Transaktionen folgt einer einfachen wirtschaftlichen Logik: Ein Block hat eine durch das Bitcoin-Protokoll begrenzte Kapazität, so dass der Schürfer versucht, den Ertrag für diesen Platz zu maximieren. Er wählt vorrangig die Transaktionen aus, die im Verhältnis zu dem Platz, den sie im Block einnehmen, die höchsten Gebühren bieten (dies wird als "Gebührensatz" bezeichnet und in sats/vB ausgedrückt). Auf die Einzelheiten der Gebühren wird später eingegangen; erinnern Sie sich einfach an die Idee der Sortierung nach Flächeneffizienz.



Ein Bitcoin-Block besteht also aus zwei Hauptteilen:




- eine Liste von Transaktionen;
- einen Blockkopf, der gewissermaßen als Ausweis für den Block dient.



![Image](assets/fr/006.webp)



Der Header ist von wesentlicher Bedeutung, da er als Grundlage für proof-of-work verwendet wird: Bei Bitcoin wird nicht direkt ein ganzer Block gemined, sondern nur der Header eines Blocks, der die Informationen zusammenfasst, die für die Verknüpfung des Blocks mit der Kette und die Übertragung seines Inhalts erforderlich sind. Damit der Header alle Transaktionen repräsentieren kann, verwendet Bitcoin ein kryptografisches Werkzeug: den Merkle-Baum.



### Der Merkle-Baum: Zusammenfassung einer großen Menge von Transaktionen



Es wäre unmöglich, alle Transaktionen im Header aufzulisten: Ein Block kann Tausende von Transaktionen enthalten, während der Header eine feste Größe hat (80 Byte). Die Lösung besteht daher darin, einen eindeutigen Hash zu berechnen, der von allen Transaktionen des Blocks abhängt: dies ist die Merkle-Wurzel.



Das Prinzip ist wie folgt:




- wird der kryptografische Fingerabdruck (Hash) jeder Transaktion berechnet;
- diese Hashes werden gepaart, verkettet und dann erneut gehasht, um eine neue Schicht von Hashes zu bilden;
- dieser Vorgang wird so lange wiederholt, bis ein einziger endgültiger Hashwert erhalten wird: die Merkle-Wurzel.



![Image](assets/fr/007.webp)



Ändert sich also eine einzelne Transaktion, und sei es auch nur um ein einziges Bit, so führt dies zu einer Änderung des Fingerabdrucks, die sich auf die Merkle-Root überträgt. Diese Wurzel ist im Block-Header enthalten. Die Änderung einer vergangenen Transaktion bedeutet also eine Änderung des Block-Headers, in dem sie enthalten ist, und damit des Block-Footprints und der Verknüpfung mit nachfolgenden Blöcken.



Seit SegWit haben wir die Signaturen vom Rest getrennt. In Wirklichkeit gibt es also 2 Merkle-Bäume, die in jedem Block enthalten sind. Diese Trennung hat Auswirkungen auf die Art und Weise, wie wir die Größe eines Blocks zählen, und auf bestimmte kryptografische Verpflichtungen, aber der Grundgedanke bleibt derselbe: Der Header muss auf kompakte Weise den gesamten Inhalt des Blocks bestätigen.



### Blockkopf



Der Blockkopf ist 80 Bytes lang und enthält genau 6 Felder. Diese sechs Elemente werden bei der Suche nach einem proof of work gehasht (siehe nächstes Kapitel):





- Die Version (`Version`): Sie gibt an, an welche Regeln oder Aktualisierungssignale sich der Block hält. Sie dient als Mechanismus zur Aufrechterhaltung der Protokollkompatibilität und der Weiterentwicklung.




- Hash des vorherigen Blocks (`previousblockhash`): Dies ist der Hash des Headers des vorherigen Blocks. Dadurch werden die Blöcke miteinander verbunden. Ohne dieses Feld würden wir unabhängige Blöcke haben. Indem wir den Hash des Headers des vorherigen Blocks einschließen, erhalten wir eine Kette, in der jeder neue Block auf dem vorherigen aufbaut.





- Merkle-Wurzel (`merkleroot`): Dies ist der Fingerabdruck aller Transaktionen im Block (über den Merkle-Baum). Sie verbindet den Header mit dem Inhalt: Wenn der Miner die Auswahl oder die Reihenfolge der Transaktionen ändert, ändert sich die Wurzel.





- Zeitstempel: Dies ist ein vom Miner gewählter Zeitstempel (Unix-Zeit) (mit Gültigkeitseinschränkungen), der angeben muss, wann der Block geschürft wurde. Er muss nicht auf die Sekunde genau sein, aber er muss bestimmte Bedingungen erfüllen, um für das Netzwerk akzeptabel zu sein.





- Kodiertes Schwierigkeitsziel (`nbits`): Dieses Feld kodiert das aktuelle Schwierigkeitsziel. Wir werden im Kapitel über den Schwierigkeitsgrad mehr ins Detail gehen, aber denken Sie daran, dass dieser Parameter Teil der Kopfzeile ist.





- Nonce (nicht einmal): Dies ist ein Wert, den der Bergmann frei ändern kann. Er dient als einstellbare Variable während proof-of-work. Ich werde seine Rolle im nächsten Kapitel näher erläutern, aber es ist wichtig zu verstehen, dass die Nonce Teil des Block-Headers ist und dazu dient, aufeinanderfolgende Versuche zu ermöglichen.



Zur besseren Veranschaulichung hier ein Beispiel für einen Block-Header im Hexadezimalformat (80 Byte):



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



Hier ist eine Aufschlüsselung nach Feldern:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



Dieser vom Miner konstruierte Kandidatenblock-Header bildet die Grundlage für seine Arbeit. Bei der Suche nach einem gültigen proof-of-work wird nicht die gesamte Liste der Transaktionen direkt in einer Schleife gehasht, sondern dieser 80-Byte-Block, der alles enthält, was erforderlich ist, um den Block mit der Vergangenheit zu verknüpfen und seinen Inhalt zu übertragen, und der auch die Parameter enthält, die für den mining-Mechanismus erforderlich sind, den wir im nächsten Kapitel untersuchen werden.



## Der Hash, das Ziel und die Nonce


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



In den vorangegangenen Kapiteln haben Sie den Weg einer Bitcoin-Transaktion verfolgt: Sie wurde von einem wallet erstellt und signiert, von Knoten weitergeleitet, in Mempools gespeichert und dann bestätigt, wenn ein Miner sie in einen vom Netzwerk akzeptierten Block einfügt. Aber wir haben noch nicht gesehen, wie ein Schürfer seinen Block zur Blockchain hinzufügen kann. Was ist der Prozess hinter mining?



Das Verständnis des mining-Prozesses ist ziemlich einfach. Es läuft auf drei Konzepte hinaus, die Hand in Hand gehen: eine Hash-Funktion, ein Zielwert und eine Variable, die der Miner ändern kann. Werfen wir einen Blick darauf, wie das alles funktioniert.



### Die Hash-Funktion



Eine Hash-Funktion ist ein Werkzeug, das eine Nachricht als Eingabe nimmt und eine Ausgabe fester Größe erzeugt, die "*Fingerprint*" oder "*Hash*" genannt wird.



![Image](assets/fr/010.webp)



Die Hash-Funktion ist für Computersysteme interessant, weil sie bestimmte Eigenschaften hat:





- Ändert man ein einziges Bit der Eingabe, ändert sich der resultierende Ausgabe-Hash völlig und unvorhersehbar;



![Image](assets/fr/011.webp)





- Es ist unmöglich, vom Ausgang zum Eingang zu gelangen: Die Funktion ist irreversibel;



![Image](assets/fr/012.webp)





- Es ist unmöglich, zwei verschiedene Nachrichten zu finden, die genau den gleichen Hash ergeben.



![Image](assets/fr/013.webp)



Die in Bitcoin für mining verwendete Hash-Funktion ist "SHA256", die zweimal hintereinander angewendet wird. Dies wird als doppeltes SHA256 oder "SHA256d" bezeichnet. Durch diese doppelte Hashfunktion wird der Fingerabdruck des Blocks erzeugt.



```text
hash = SHA256(SHA256(message))
```



In unserem Fall entspricht die "Nachricht" dem Blockkopf, den Sie im vorigen Kapitel gesehen haben. Zur Erinnerung: Der Header ist eine kleine Struktur, die alles im Block zusammenfasst.



![Image](assets/fr/014.webp)



### Arbeitsnachweis: Finden eines Hashwerts, der kleiner als das Ziel ist



Proof-of-Work wird oft als Lösung für ein komplexes Problem beschrieben. In Wirklichkeit handelt es sich weniger um ein Problem als um eine Trial-and-Error-Suche: Der Miner muss eine Version des Headers finden, deren Hashwert (nach Durchlaufen der Hashfunktion "SHA256d") eine einfache Bedingung erfüllt: Er muss kleiner sein als ein bestimmter Zielwert.



Diese Bedingung wird wie folgt formuliert:




- der Hash des Blockkopfes wird mit einer Hash-Funktion berechnet;
- interpretieren wir diesen Hash als eine Zahl;
- damit der Block gültig ist, muss diese Zahl kleiner oder gleich einem Wert namens "*Schwierigkeitsziel*" sein.



Mit anderen Worten, ein Block ist gültig, wenn:



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



Das Ziel ist eine 256-Bit-Zahl. Da der von `SHA256d` erzeugte Hash ebenfalls 256 Bit beträgt, können sie als zwei Zahlen verglichen werden. Je niedriger die Zielvorgabe ist, desto schwieriger ist die Bedingung, da es weniger mögliche Ergebnisse unterhalb dieser Schwelle gibt. Umgekehrt ist die Bedingung umso leichter zu erfüllen, je höher die Zielvorgabe ist, und umso einfacher wird es, einen Block zu minen. In späteren Kapiteln werden wir uns genauer ansehen, wie dieses Ziel bestimmt wird.



In diesem System ist die Hash-Funktion interessant. Denken Sie daran, dass es einfach ist, die Ausgabe aus der Eingabe zu berechnen, aber unmöglich, eine Eingabe zu finden, wenn man nur die Ausgabe der Funktion kennt. Bei mining wird von den Schürfern nicht verlangt, einen genauen Hashwert zu finden, sondern einen Hashwert, der unter einem Zielwert liegt. Die einzige Möglichkeit, dies zu erreichen, besteht darin, eine sehr große Anzahl von Versuchen zu unternehmen, bis ein bestimmter Header ihres Kandidatenblocks, wenn er gehasht wird, einen Hash-Wert ergibt, der kleiner als dieser Zielwert ist.



Sobald das Ziel ausreichend niedrig ist, wird dieser Prozess kostspielig. Der Miner berechnet den Hash des Headers seines Kandidatenblocks, überprüft das Ergebnis und ändert, falls die Bedingung nicht erfüllt ist, den Header und wiederholt die Berechnung. Diese Schleife wird so lange wiederholt, bis ein gültiger Header gefunden wird. Wenn der Hash des Headers schließlich die Bedingung erfüllt, ist das proof of work etabliert, der Block gilt als gültig und kann im Bitcoin-Netzwerk verbreitet werden, damit die Knoten ihn zu ihrer Blockchain hinzufügen. Der siegreiche Miner erhält dann die zugehörige Belohnung (auf deren Zusammensetzung wir später eingehen), während sich alle Miner sofort auf die Suche nach einem neuen, gültigen Header für den nächsten Block machen.



Der grundlegende Vorteil dieses Mechanismus liegt in seiner Asymmetrie. Die Herstellung eines proof of work ist für Miner kostspielig, da sie eine große Anzahl von Hash-Berechnungen erfordert. Für die Verifizierer, d. h. die Netzwerkknoten, ist die Verifizierung hingegen äußerst einfach: Sie müssen lediglich den vom Miner gelieferten Block-Header hashen und überprüfen, ob der resultierende Hash tatsächlich niedriger ist als das Ziel. Das Auffinden eines Beweises erfordert daher viel Arbeit und Ressourcen, während die Überprüfung seiner Gültigkeit schnell und kostengünstig ist. Genau diese Eigenschaft ist es, die ein effizientes proof-of-work-System ausmacht.



### Die Nonce



Eine praktische Frage bleibt: Wenn der vom Miner konstruierte Header des Kandidatenblocks keinen gültigen Hash ergibt, wie kann der Miner es dann erneut versuchen? Er muss etwas im Header ändern, um einen anderen Hash zu erhalten. Genau das ist die Aufgabe der Nonce.



Erinnern Sie sich an die erste Eigenschaft einer Hash-Funktion: Die Änderung eines einzigen Bits der Eingabe reicht aus, um einen völlig anderen und unvorhersehbaren Ausgabe-Hash zu erzeugen. Jede Hash-Berechnung gleicht daher einer Zufallsziehung.



![Image](assets/fr/016.webp)



Um sein Glück erneut zu versuchen, muss der Miner nicht den gesamten Header seines Kandidatenblocks ändern, sondern nur einen winzigen Teil davon, denn schon ein einziges anderes Bit führt zu einem völlig neuen Hash, der möglicherweise gültig ist, wenn er kleiner ist als der Zielwert.



Genau aus diesem Grund enthält der Blockkopf ein Nonce. Das Nonce ist ein 32-Bit-Wert, der einmal verwendet und dann ersetzt wird. In der Praxis kann ein Miner für ein und denselben Kandidatenblock etwa 4,29 Milliarden mögliche Werte testen (von "0" bis "2^32 - 1"). Jede Variation des Nonce-Wertes verändert den Block-Header und folglich auch den Hash-Wert, der nach Anwendung der SHA256d-Hash-Funktion erzeugt wird.



Das mining-Verfahren ist sehr einfach:




- erstellt der Miner einen Kandidatenblock (Transaktionen + Header);
- berechnet dann den Hash des `SHA256d(header)`;
- ist das Ergebnis größer als das Ziel, wird der Nonce geändert;
- beginnt wieder;
- usw.



![Image](assets/fr/017.webp)



Tatsächlich ist die Nonce nicht das einzige Feld, das geändert werden kann. Jede Änderung innerhalb der Transaktionen eines Blocks führt zu einer Änderung der Wurzel des Merkle-Baums und damit zu einer Änderung der Kopfzeile des Blocks. Mit der heutigen Rechenleistung ist es relativ schnell möglich, die 4,29 Milliarden möglichen Werte der Nonce durchzugehen. Aus diesem Grund gibt es ein weiteres Feld, das allgemein als "*extra-nonce*" bezeichnet wird und die Möglichkeiten der Header-Variation weiter vervielfacht. Wir werden auf diesen Mechanismus in einem späteren Kapitel noch einmal genauer eingehen.



### Was ist der Sinn von proof of work?



Wir nennen es "Beweis", weil das Ergebnis sofort überprüfbar ist: Sobald ein Block erzeugt wurde, kann jeder Knoten in einem Bruchteil einer Sekunde überprüfen, ob der kryptografische Hash seines Headers tatsächlich unter dem erforderlichen Zielwert liegt. Wir nennen es "Arbeit", weil das Erreichen dieses Hashwerts eine Vielzahl von Versuchen und damit echte Kosten in Form von Berechnungen und Energie erfordert.



Im Weißbuch Bitcoin führt Satoshi Nakamoto zwei Vorteile für den Einsatz eines proof-of-work-Systems in Bitcoin an:





- Seal der Wirtschaftsgeschichte:**



Sobald die Rechenlast verbraucht ist, ist der Block gesperrt: Seine Änderung würde eine Neuberechnung des proof of work dieses Blocks erfordern. Und da die Blöcke aneinandergereiht sind, würde die Änderung eines alten Blocks auch bedeuten, dass alle nachfolgenden Blöcke neu berechnet werden müssten, um dann die laufende Arbeit der ehrlichen Kette einzuholen und zu übertreffen.



Mit anderen Worten: Das proof-of-work dient als Rückgrat des Zeitstempelsystems, so dass es mit zunehmender Anzahl der Blöcke immer kostspieliger wird, die Vergangenheit zu fälschen. Wenn ein neuer Block geschürft wird, wird die vom proof of work bereitgestellte Sicherheit gleichzeitig und einheitlich auf alle vorhandenen UTXO angewendet. Mit jedem hinzugefügten Block akkumuliert jedes UTXO somit eine zusätzliche Menge an Sicherheit vom Proof-of-Work.





- Definition der Mehrheitsregel (Konsens) und Neutralisierung von Sybil:**



Proof-of-Work ermöglicht es auch Bitcoin, einen Konsens zu erreichen, ohne sich auf die Abstimmungsregel "eine ID = eine Stimme" zu verlassen, die durch die massive Schaffung von Identitäten (IPs, Knoten, Schlüssel...) leicht verfälscht werden könnte.



Bei Bitcoin ist die "*Mehrheit*" nicht die größte Anzahl von Teilnehmern, sondern die **Kette, die die meiste Arbeit anhäuft**. Wie Satoshi es ausdrückt, ist dies ein "eine CPU = eine Stimme"-Prinzip, d. h. eine Abstimmung, die nach der tatsächlichen Rechenleistung gewichtet wird, die zur Erzeugung gültiger Blöcke aufgewendet wird. Der Einsatz von Tausenden von Knotenpunkten bringt also an sich keinen Vorteil gegenüber Bitcoin. Ohne zusätzliche Rechenleistung werden keine Arbeitsnachweise mehr akkumuliert, und der Sybil-Angriff wird nutzlos, während die Entscheidungsregel objektiv bleibt und keine Identifizierung der Teilnehmer erfordert.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System.*](https://bitcoin.org/bitcoin.pdf)



Die Grundsätze im Zusammenhang mit der Nützlichkeit und den Befugnissen von Minderjährigen sind ein sehr komplexes Thema, auf das ich in diesem Kurs nicht näher eingehen werde. Wir werden dieses Thema jedoch in zukünftigen MIN 201-Schulungen vertieft behandeln.



Im Moment kann man die Funktionsweise von mining wie folgt zusammenfassen: Die Miner erstellen einen Kandidatenblock mit den in den Mempools anhängigen Transaktionen und suchen dann nach einem Hash des Headers (über `SHA256d`), der kleiner oder gleich einem Zielwert ist. Sie erreichen dies, indem sie Nonces durch Versuch und Irrtum testen.



Im nächsten Kapitel werden wir einen kurzen geschichtlichen Abstecher zum proof-of-work-Prinzip machen, um seinen Hintergrund zu verstehen, und uns dann ansehen, wie das Schwierigkeitsziel durch das System bestimmt wird.



## Die Geschichte von proof of work


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



Proof-of-work wurde nicht für Bitcoin erfunden. Satoshi Nakamoto griff mehrere ältere Ideen auf, die bereits in verschiedenen Kontexten erforscht worden waren, und fügte sie zusammen.



### HashBargeld



In den späten 1990er Jahren wurde das Problem des E-Mail-Spams immer größer. Wenn der Versand einer E-Mail fast nichts kostet, kann ein Spammer Millionen von Nachrichten versenden. Wenn aber jede Nachricht einen geringen Rechenaufwand erfordert, bleibt der Versand einer einzigen legitimen Nachricht für einen normalen Benutzer einfach, während der Versand von Millionen von Nachrichten sehr teuer wird.



Dies ist das Ziel von Hashcash, das 1997 von Adam Back vorgeschlagen wurde und als Erfindung des proof-of-work-Prinzips gilt. Das Prinzip von Hashcash ist dem von mining sehr ähnlich: Es wird ein Hash erzeugt, der eine Bedingung erfüllt (eine bestimmte Anzahl von Nullen am Anfang des Hashes). Der Beweis ist dann der Nachricht beigefügt und kann vom Empfänger sehr schnell überprüft werden. Wenn eine E-Mail empfangen wird, die diesen Beweis nicht enthält, kann sie sofort als Spam betrachtet und daher gefiltert werden. Die Spammer sind dann gezwungen, eine beträchtliche Menge an Energie aufzubringen, um Millionen von Nachrichten zu versenden, was die Rentabilität dieser Art von Operationen, ob zu Marketingzwecken oder in betrügerischer Absicht, drastisch reduziert (oder sogar ganz zunichte macht).



Heutzutage wird Hashcash nicht mehr für E-Mails verwendet. Die Spam-Filterung basiert heute weitgehend auf zentralisierten Systemen. Der Vorteil von Hashcash gegenüber aktuellen Lösungen liegt darin, dass es keine zentrale Filterung benötigt: Jeder kann die Parameter nach seinen eigenen Kriterien anpassen. Es erfordert auch keine Identifizierung, da eine Hash-Suche anonym durchgeführt werden kann. Vor allem stützt es sich nicht auf ein Reputationssystem, das dazu neigt, subjektive Formen der Filterung einzuführen.



Bei Hashcash ging es nicht um die Schaffung von Geld. Es ging darum, eine leicht automatisierbare digitale Handlung mit Grenzkosten zu belegen.



![Image](assets/fr/008.webp)



### Bit Gold



In den späten 1990er und frühen 2000er Jahren erforschte Nick Szabo die Idee der digitalen Knappheit auf der Grundlage des proof of work. Sein konzeptionelles Projekt mit dem Namen Bit Gold sieht die Schaffung von Werteinheiten durch die Lösung eines kostspieligen proof of work und die anschließende Aufzeichnung dieser Beweise in einem Register vor, um eine Form des Eigentums zu schaffen.



Bit Gold hat zwar nicht zu einem System wie Bitcoin geführt, aber es enthält mehrere wichtige Erkenntnisse: die Idee, dass Berechnungen Knappheit erzeugen können, und die Idee, Elemente mit einem Zeitstempel zu versehen, um eine Geschichte zu erstellen, die nur schwer umgeschrieben werden kann.



### RPOW



Im Jahr 2004 schlug die Hal Finney RPOW (*Reusable Proofs of Work*) vor. Die Idee war, Arbeitsnachweise zu erstellen, die dann ausgetauscht und nicht nur verbraucht werden können. RPOW zielte darauf ab, digitale token auf der Grundlage von proof of work zu erstellen, mit einem System zur Überprüfung und Übertragung dieser token, ohne sie zu duplizieren. Auch RPOW löste das Problem einer völlig dezentralen Registrierung nicht zufriedenstellend, wie es Bitcoin später tun sollte, aber es bleibt einer der großen Vorläufer von Bitcoin.



![Image](assets/fr/009.webp)



Hashcash, Bit Gold und RPOW verwenden proof-of-work, um Kosten aufzuerlegen und eine Form der Knappheit zu schaffen. Bitcoin greift diesen Mechanismus auf, gibt ihm aber eine zentrale und kollektive Rolle: proof-of-work wird nicht nur verwendet, um etwas zu erschaffen, sondern auch, um zu entscheiden, wer das Recht hat, die nächste Seite des Registers (den nächsten Block) zu schreiben, und um dieses Register kostspielig zu fälschen.



## Anpassen des Schwierigkeitsziels


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



In den vorangegangenen Kapiteln haben Sie das Herzstück von proof-of-work kennengelernt: Schürfer hacken den Header ihres Kandidatenblocks mit `SHA256d`, und der Block wird nur dann als gültig angesehen, wenn der resultierende Hashwert numerisch kleiner oder gleich einem Referenzwert, dem sogenannten Zielwert, ist. Bleibt die Frage: Woher kommt dieser Zielwert, und wie stellt das System sicher, dass er im Laufe der Zeit konstant bleibt?



Bitcoin strebt eine durchschnittliche Rate von einem gefundenen Block alle 10 Minuten an. Natürlich ist dieses Tempo nicht auf die Sekunde genau garantiert. In der Praxis werden einige Blöcke einige Sekunden nach dem vorherigen gefunden, während andere erst nach mehr als einer Stunde gefunden werden. Entscheidend ist hier der Durchschnitt über einen ausreichend langen Zeitraum.



![Image](assets/fr/019.webp)



Diese Variabilität ergibt sich aus der probabilistischen Natur von mining: Jeder Hash ist ein unabhängiger Versuch mit einer konstanten Wahrscheinlichkeit (unter der Annahme, dass das Ziel unverändert bleibt), ein Ergebnis unterhalb des Ziels zu erzielen. Es kann daher mit einer Lotterie mit kontinuierlicher Ziehung verglichen werden: Je mehr Hashes die Miner pro Sekunde durchführen, desto kürzer ist die erwartete Verzögerung bis zum Auftauchen eines gültigen Blocks, ohne jedoch jemals die Zufälligkeit von einer Ziehung zur nächsten zu beseitigen.



### Warum sollte man 10 Minuten zwischen den Blöcken einplanen?



Obwohl es dafür keine Beweise gibt, hat Satoshi Nakamoto sicherlich 10 Minuten als praktischen Kompromiss zwischen Effizienz und Sicherheit gewählt. Ein kürzeres Intervall würde zu häufigeren Bestätigungen führen, aber auch zu mehr vorübergehenden Netzaufspaltungen. Um diesen Punkt zu verstehen, müssen wir auf die Art und Weise zurückgehen, wie sich ein Block verbreitet.



Wenn ein Miner einen gültigen Block findet, verteilt er ihn sofort an seine Peers. Die Knoten, die ihn erhalten, prüfen seine Gültigkeit (Transaktionen, proof of work, Konsensregeln usw.) und leiten ihn dann weiter. Diese Weitergabe dauert eine gewisse Zeit, die durch die Internet-Latenzzeit, die Bandbreite und die Fähigkeit der einzelnen Knoten, den Block zu überprüfen, begrenzt ist.



![Image](assets/fr/020.webp)



Wenn während dieser Diffusionsverzögerung ein anderer Miner ebenfalls einen gültigen Block in derselben Höhe entdeckt, kann es zu einer vorübergehenden Spaltung des Netzes kommen: Ein Teil der Knoten und Miner verlässt sich auf Block A, der andere auf Block B. Dies ist eine vorübergehende Teilung des Netzes.



![Image](assets/fr/021.webp)



Diese Spaltungen sind nicht katastrophal. Der Nakamoto-Konsens sagt voraus, dass sich auf lange Sicht nur ein Zweig durchsetzen wird: derjenige, der die meiste Arbeit anhäuft. Sobald zum Beispiel ein neuer Block über Block A geschürft wird, synchronisiert sich das gesamte Netzwerk auf diesen Zweig und gibt Block B auf, der dann zu einem "*stale block*" wird, der in der Alltagssprache manchmal fälschlicherweise als "*orphan block*" bezeichnet wird.



![Image](assets/fr/022.webp)



Andererseits haben sie ihren Preis: einige Minuten lang arbeitet ein Teil der Miner an einem Zweig, der dann aufgegeben wird. Diese Arbeit ist dann unter dem Gesichtspunkt der Gesamtsicherheit vergeudet, da sie nicht zur endgültigen Kette beigetragen hat. Je kürzer das Intervall zwischen den einzelnen Blöcken ist, desto größer ist die Wahrscheinlichkeit solcher Aufspaltungen, da die Propagationszeit einen größeren Teil der Zeit zwischen den einzelnen Blöcken ausmacht.



Das 10-Minuten-Intervall lässt in der Regel genügend Zeit, damit sich der Siegerblock weit verbreiten kann, bevor ein konkurrierender Block auf gleicher Höhe gefunden wird. Dies ist ein Kompromiss, der Splits begrenzt, die Verschwendung von Rechenleistung reduziert und dem Netzwerk hilft, auf globaler Ebene synchron zu bleiben.



### Verstehen von hashrate



*"Hashrate*" bezieht sich auf die Menge an Hash-Berechnungen, die pro Sekunde durchgeführt werden, unabhängig davon, ob sie von einem einzelnen Miner, einer Gruppe von Minern oder allen Minern in Bitcoin durchgeführt werden. Sie wird in "H/s" (Hashes pro Sekunde) ausgedrückt, mit Vielfachen wie "TH/s" (Terahashes pro Sekunde) oder "EH/s" (Exahashes pro Sekunde). Dies gibt die Anzahl der Versuche an, die Miner pro Sekunde unternehmen können, um einen Hash zu erhalten, der niedriger ist als der Zielwert.



Wenn das Ziel fest bleibt, dann:




- jeder Versuch hat eine feste Erfolgswahrscheinlichkeit;
- mehr Versuche pro Sekunde erhöhen die Wahrscheinlichkeit, dass ein Gewinnversuch schnell erscheint


Mit anderen Worten: Wenn das Bitcoin-Netz von morgen seine Rechenleistung verdoppelt, indem es doppelt so viele mining-Rechner anschließt, würden die Blöcke ohne einen Korrekturmechanismus im Durchschnitt doppelt so schnell gefunden werden. Das Ziel muss daher angepasst werden, um die hashrate-Schwankungen auszugleichen.



### Anpassen des Schwierigkeitsziels



Bitcoin löst dieses Problem mit einem periodischen Zielanpassungsmechanismus, der die Schwierigkeit von mining anpasst. Das Prinzip ist wie folgt: Alle 2016 Blöcke (etwa alle 2 Wochen) berechnet jeder Knoten das Schwierigkeitsziel neu, indem er beobachtet, wie viel Zeit tatsächlich für die Produktion dieser 2016 Blöcke benötigt wurde.



Ziel dieses Mechanismus ist es, die durchschnittliche Produktionszeit eines Blocks auf etwa 10 Minuten zu reduzieren, während sich der Gesamt-hashrate des Netzes ständig ändert, weil Maschinen abgeschaltet werden oder im Gegenteil neue Maschinen hinzukommen.



![Image](assets/fr/023.webp)



Die Berechnung basiert auf der beobachteten Zeit für den verstrichenen Zeitraum:




- wenn die letzten Blöcke von 2016 zu schnell gefunden wurden, bedeutet dies, dass hashrate in diesem Zeitraum gestiegen ist; Bitcoin erschwert dann die Bedingung, indem es das Ziel für den nächsten Zeitraum senkt;
- wenn die Blöcke von 2016 zu langsam gefunden wurden, bedeutet dies, dass hashrate abgenommen hat; Bitcoin lindert den Zustand, indem es das Ziel erhöht.



Die Formel lautet wie folgt:



```txt
Tn = To * (Ta / Tt)
```



Mit:




- tn": neues Ziel
- bis": altes Ziel
- ta": Verstrichene Echtzeit für die letzten 2016 Blöcke
- tt": Zielzeit (in Sekunden)



Mit einer Zielzeit von zwei Wochen, d.h. `Tt = 1.209.600` Sekunden:



```txt
Tn = To * (Ta / 1 209 600)
```



Um zu verstehen, wie man die Schwierigkeit von Bitcoin mining anpassen kann, hier ein Beispiel mit fiktiven Werten:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


Mit:



- **Zu = 18.045.755.102**`: Altes Ziel, d. h. der Referenzwert vor der Anpassung.
- **ta = 1.000.000 Sekunden**`: Zeit, die tatsächlich für die Produktion der letzten 2016 Blöcke aufgewendet wurde. Da diese Zeit geringer ist als die Zielzeit, hat das Netzwerk zu schnell abgebaut.
- **1.209.600 Sekunden**`: Zielzeit, die 10 Minuten pro Block für 2016 Blöcke entspricht und als Referenz für die Anpassung verwendet wird.
- **tn = 14.918.779.020**`: Neues Ziel nach Schwierigkeitsanpassung berechnet.



Hier ist das neue Ziel niedriger als das alte, was bedeutet, dass mining härter wird, um die Blockproduktion im nächsten Zeitraum zu verlangsamen.


*Die Zielwerte in diesem Beispiel sind zu Lehrzwecken vereinfacht und skaliert; das tatsächliche Ziel, das in Bitcoin verwendet wird, ist eine 256-Bit-Ganzzahl in einer ganz anderen Größenordnung.*



Diese Berechnung wird lokal von jedem Knoten auf der Grundlage der in den Blöcken eingegebenen Zeitstempel durchgeführt. Da alle Knoten dieselben Regeln anwenden, kommen sie zu demselben Ergebnis, und das neue Ziel wird zur gemeinsamen Referenz für die nächsten Blöcke 2016.



Es gibt ein wichtiges Detail, das bei dieser Anpassung zu beachten ist: **Sie ist begrenzt**. Bitcoin begrenzt die Variation der Schwierigkeit pro Periode, um zu abrupte Änderungen zu vermeiden, die das System blockieren könnten. Die tatsächliche Zeit, die berücksichtigt wird, muss innerhalb eines Bereichs bleiben, der dem Faktor 4 entspricht (mindestens ein Viertel des alten Ziels, höchstens das Vierfache des alten Ziels). Dies verhindert eine extreme Neuausrichtung, wenn die Zeitstempel sehr untypisch oder manipuliert sind.



### Darstellung der Ziele



Im Blockkopf erscheint das Ziel nicht in seiner vollen 256-Bit-Form, da dies zu viel Platz beanspruchen würde. Stattdessen kodiert das 32-Bit-Feld "nBits" das Ziel in einem kompakten Format, vergleichbar mit der wissenschaftlichen Notation zur Basis 256: ein Exponent (1 Byte) und ein Koeffizient (3 Byte). Das vollständige Ziel wird dann aus diesen beiden Werten rekonstruiert. Wir werden hier nicht ins Detail gehen, da das Thema relativ komplex ist und nichts zum Verständnis von mining beiträgt. Es sei nur daran erinnert, dass das Ziel nicht in roher Form im Blockkopf gespeichert ist, sondern in kompakter Form.



Mit diesem letzten Kapitel von Teil I haben wir uns einen Überblick darüber verschafft, wie proof-of-work in Bitcoin funktioniert: Der Miner erstellt einen Kandidatenblock, indem er Transaktionen aus seinem Mempool auswählt, den Kandidatenblock-Header berechnet, ihn hasht, den resultierenden Hash mit dem Periodenziel vergleicht und dann erneut beginnt, indem er die Nonce ändert, bis er einen gültigen Hash erhält. Schließlich berechnet das Netzwerk alle 2016 Blöcke ein neues Ziel, um trotz der ständigen Schwankungen von hashrate eine durchschnittliche Zeit von etwa 10 Minuten pro Block zu erhalten.




# Das Bitcoin mining Anreizsystem


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Wie Sie sich vorstellen können, ist Bitcoin mining keine altruistische Tätigkeit. Miner haben reale Kosten: Strom für den Betrieb ihrer mining-Computer, den Kauf von Spezialgeräten, Lohnkosten für die Wartung, manchmal auch für Räumlichkeiten und Kühlsysteme. Damit das Bitcoin-System funktioniert, müssen die privaten Interessen der Miner mit den kollektiven Interessen des Netzwerks in Einklang gebracht werden. Genau das ist die Aufgabe der mining-Belohnung. Sie ermutigt die Miner, in proof of work zu investieren, gültige Transaktionen einzubeziehen und die Regeln des Protokolls zu respektieren, anstatt zu versuchen, es zu korrumpieren.



Diese Logik basiert auf der Spieltheorie: Das Protokoll macht Ehrlichkeit rational. Ein Miner verdient Geld, wenn er einen gültigen Block produziert, der von den Knoten akzeptiert wird. Versucht er hingegen zu betrügen, wird sein Block von den Knoten abgelehnt, und er erhält nichts. Da die Produktion eines Blocks mit Kosten verbunden ist, stellt ein zurückgewiesener Block einen direkten Verlust dar. In einem wettbewerbsintensiven Umfeld, in dem Tausende von Spielern gleichzeitig nach einem gültigen Block suchen, besteht die profitabelste Strategie daher meist darin, sich strikt an die Regeln zu halten und sein Einkommen auf ehrliche Weise zu maximieren.



Um dies zu erreichen, sieht das Bitcoin-Protokoll vor, dass der Miner, der einen gültigen Block findet, das Recht erhält, eine bestimmte Transaktion in den Block aufzunehmen, wofür er eine bestimmte Summe von BTC erhält. Dies wird als **Blockbelohnung** bezeichnet. In diesem ersten Kapitel dieses Abschnitts geht es darum, zu verstehen, woraus er besteht und wie er ermittelt wird. Später werden wir sehen, wie sich der Teil der Geldschöpfung im Laufe der Zeit entwickelt (mit Halvings) und wie er tatsächlich technisch eingezogen wird (über die Coinbase-Transaktion).



### Woraus besteht die Blockprämie?



In den vorangegangenen Kapiteln haben wir gesehen, wie Miner es schaffen, einen gültigen Block zu finden. Sobald ein Miner einen Header gefunden hat, dessen Hash kleiner ist als der Zielwert, wird sein Blockkandidat als gültig angesehen. Er kann ihn dann an das gesamte Bitcoin-Netzwerk weitergeben. Der Block wird dem Rest der Blockchain hinzugefügt, wodurch die darin enthaltenen Transaktionen bestätigt werden.



Genau dieses Ereignis (das tatsächliche Hinzufügen des Blocks zur Blockchain) ist der Auslöser für die Auszahlung einer Belohnung an den erfolgreichen Miner. Diese Belohnung setzt sich aus zwei verschiedenen Elementen zusammen, die addiert werden:




- blocksubvention**;
- transaktionsgebühren**.



![Image](assets/fr/024.webp)



Schauen wir uns einmal an, was diese beiden Teile der Belohnung bedeuten.



### Blockzuschuss



Die Blocksubvention entspricht dem monetären Erstellungsanteil der Belohnung. Wenn ein Miner einen gültigen Block erzeugt, ermächtigt ihn das Protokoll, eine bestimmte Anzahl neuer Bitcoins zu erzeugen und sie sich selbst als Belohnung zuzuteilen. Diese Bitcoins werden ex nihilo geschaffen. Sie haben vorher nicht existiert.



Die Menge der neu geschaffenen Bitcoins ist jedoch keineswegs willkürlich. Sie ist durch die Regeln des Bitcoin-Protokolls genau festgelegt und für alle Miner identisch. Wir werden uns diesen Mechanismus im nächsten Kapitel genauer ansehen, denn die Subvention ist kein fester Wert auf unbestimmte Zeit: Sie wird in regelmäßigen Abständen nach einem genauen Zeitplan aufgeteilt. Für den Moment sollten Sie sich das einfach merken:




- der Blockzuschuss ist eine der beiden Komponenten der Blockprämie;
- er ist begrenzt und wird vom Protokoll bestimmt, nicht vom Miner (auch wenn der Miner technisch gesehen weniger als den Höchstbetrag anfordern kann);
- es erzeugt Bitcoins aus dem Nichts.



Diese Subvention spielt im Rahmen des Bitcoin-Protokolls zwei Hauptrollen. Die erste besteht darin, Spieler zur Teilnahme an mining zu ermutigen. In den ersten Jahren von Bitcoin (und manchmal noch heute) waren die Transaktionsgebühren sehr niedrig. Die Subvention hat daher eine ausreichende Entschädigung garantiert, um Miner anzuziehen und ein gewisses Maß an Sicherheit für das System zu gewährleisten.



Die zweite Rolle bezieht sich auf die Verteilung der Währung. Bei jeder neuen Währung stellt sich die Frage, wie die Geldeinheiten gerecht an die Bevölkerung verteilt werden können. Die Blocksubvention bietet eine Antwort auf dieses Problem. Durch die Schaffung von Bitcoins über mining ermöglicht sie deren anfängliche Verteilung auf offene und neutrale Weise: Jeder kann sie erhalten, sofern er an mining teilnimmt, ohne dass eine vorherige Genehmigung oder Identifizierung erforderlich ist.



Da diese Bitcoins jedoch aus dem Nichts geschaffen werden, ist ihr Wert nicht ohne Grundlage. Indem die Subvention die im Umlauf befindliche Geldmenge erhöht, verwässert sie mechanisch den Wert der vorhandenen Bitcoins. Sie führt also eine Form der Geldinflation ein. Wir werden jedoch im nächsten Kapitel sehen, dass diese Subvention allmählich verschwinden wird und die Inflation schließlich aufhört.



![Image](assets/fr/025.webp)



### Transaktionsgebühren



Die zweite Komponente der Blockbelohnung hängt mit der Systemnutzung zusammen: Wenn ein Nutzer eine Transaktion durchführt, möchte er, dass diese bestätigt wird. Der Platz in den Blöcken ist jedoch begrenzt, und Blöcke erscheinen im Durchschnitt nur etwa alle 10 Minuten. Blockraum ist daher eine knappe Ressource. Wenn die Nachfrage das Angebot übersteigt, steigt der Preis: Das ist der Markt für Transaktionsgebühren. Jeder Schürfer, dem es gelingt, einen gültigen Block zu erzeugen, erhält das Recht, die vollen Transaktionsgebühren für alle Transaktionen, die er in seinen Block aufgenommen hat, auf eigene Rechnung einzuziehen.



Man kann es sich wie ein Auktionssystem vorstellen: Für jede Transaktion wird ein Gebührenbetrag vorgeschlagen, und die Miner geben denjenigen den Vorrang, die ihr Einkommen maximieren, wobei der Platz begrenzt ist. Dieser Mechanismus sorgt für eine natürliche Angleichung der Interessen:




- eilige Nutzer zahlen mehr, um schnell aufgenommen zu werden;
- miner werden ermutigt, Transaktionen einzubeziehen, die die höchsten Gebühren für den Blockraum zahlen.
- das Netz vermeidet Spam, da die Veröffentlichung einer Transaktion mit Kosten verbunden ist.



#### Wie werden die Transaktionsgebühren berechnet?



Entgegen der landläufigen Meinung sind Gebühren kein Output bei einer Bitcoin-Transaktion. Vielmehr gibt eine Transaktion Inputs aus und erzeugt Outputs. Die Inputs stellen die Quelle der verwendeten Bitcoins dar, während die Outputs das Ziel der Zahlungen darstellen. Die Transaktionsgebühren sind einfach **die Differenz zwischen den gesamten Inputs und den gesamten Outputs**.



Mit anderen Worten: Die Bitcoin-Inputs des Nutzers, die ihm gehören, erzeugen Outputs für die Empfänger, geben aber nicht den vollen Betrag wieder, den die Inputs verbraucht haben. Die Differenz zwischen diesen beiden Beträgen stellt die Transaktionsgebühren dar, die der Miner einnehmen kann.



Nehmen wir ein Beispiel. Eine Transaktion verbraucht zwei Inputs, einen von `100.000 sats` und den anderen von `150.000 sats`, und erzeugt drei Outputs von `35.000 sats`, `42.000 sats` und `170.000 sats`.



![Image](assets/fr/027.webp)



Die Summe der Inputs beträgt also 250.000 sats", während die Summe der Outputs 247.000 sats" beträgt. Dies bedeutet, dass 3.000 sats in Inputs verbraucht wurden, ohne in Outputs wiederhergestellt zu werden: Dieser Betrag entspricht den durch diese Transaktion vorgeschlagenen Gebühren.



![Image](assets/fr/028.webp)



Wenn ein Miner diese Transaktion in einen gültigen Block aufnimmt, hat er das Recht, diese "3.000 sats" zusätzlich zu den Gebühren aller anderen im Block enthaltenen Transaktionen zu erhalten. Es gibt jedoch keine direkte on-chain-Verbindung zwischen der Transaktion, die die Gebühr zahlt, und den sats, die der Miner tatsächlich einnimmt. Technisch gesehen werden die "3.000 sats" an Gebühren vernichtet, und im Gegenzug erhält der Miner das Recht, denselben Betrag für sich selbst wiederherzustellen.



#### Die Gebührenquote



Ein Block ist nicht durch die Anzahl der Transaktionen begrenzt, sondern durch seine Gesamtkapazität (heute in der Praxis durch das Gewicht des Blocks). Einige Transaktionen benötigen mehr Platz als andere: Eine Transaktion mit vielen Eingaben und Ausgaben ist größer als eine einfache Transaktion mit einer einzigen Eingabe und zwei Ausgaben. Auch die verwendeten Skripte beeinflussen die Größe.



![Image](assets/fr/026.webp)



Zwei Transaktionen können daher in absoluten Zahlen den gleichen Betrag an Gebühren zahlen, sind aber aus Sicht des Miners wirtschaftlich nicht gleichwertig. Wenn eine Transaktion doppelt so groß ist, kostet sie auch doppelt so viel Platz im Block. Da der Platz knapp ist, versucht der Schürfer, seine Einnahmen pro Platzeinheit zu maximieren.



Aus diesem Grund wird in der Praxis die Wettbewerbsfähigkeit einer Transaktion durch ein Gebührenverhältnis ausgedrückt, das üblicherweise in "sats/vB" (satoshi pro virtuellem Byte) angegeben wird. Die Berechnung dieses Verhältnisses ist ganz einfach:



```text
fee rate = fee / weight (in vB)
```



Wenn wir zum Beispiel ein Geschäft mit einem Gewicht von 141 vB haben und 1.974 sats an Gebühren zuweisen, wird es einen Gebührensatz von 14 sats/vB haben.



```text
1 974 / 141 ≈ 14 sats/vB
```



Dieses Verhältnis erklärt die wirtschaftlichen Entscheidungen der Miner: Bei fester Kapazität maximiert die Aufnahme von Transaktionen mit hohen Kosten die Gesamtgebühren des Blocks und damit die Vergütung des Miners. Es erklärt auch, warum kostengünstige Transaktionen lange Zeit in der Warteschlange der Mempools verbleiben: Sie konkurrieren mit anderen Transaktionen, die mehr pro Platzeinheit zahlen.



### Schutz des Netzes vor Spam



Gebühren dienen auch der operativen Sicherheit: Sie führen Kosten für die Vervielfältigung von Transaktionen ein. Wäre die Veröffentlichung einer Transaktion kostenlos, wäre es ein Leichtes, das Netz mit nutzlosen Transaktionen zu überschwemmen und die Mempools zu sättigen, was die Belastung der Knoten erhöhen würde.



In der Praxis wenden die Knoten lokale Weiterleitungsrichtlinien (Mempool-Regeln) an und legen oft eine Mindestgebührenschwelle fest, unter der sie eine Transaktion nicht weiterleiten (standardmäßig `0,1 sat/vB` in Bitcoin Core über `minRelayTxFee`). Eine Transaktion kann im strengen Sinne der Konsensregeln gültig sein, aber von den meisten Knoten nicht weitergeleitet werden, wenn ihre Gebühren zu niedrig sind. Das hat zur Folge, dass sie nicht zirkuliert, die Miner nicht erreicht und eine sehr geringe Chance hat, bestätigt zu werden.



An dieser Stelle haben Sie das Wesentliche der Blockbelohnung verstanden: Sie entspricht der Entschädigung für den siegreichen Miner und besteht aus zwei verschiedenen Elementen. Einerseits aus einer Blocksubvention, die durch die Regeln des Protokolls festgelegt ist und durch die ex nihilo neue Bitcoins geschaffen werden. Zum anderen aus den Gebühren für Transaktionen, die in dem geminten Block enthalten sind.



Im nächsten Kapitel werden wir uns eingehender mit der Blocksubvention befassen, um zu verstehen, wie sie genau berechnet wird und wie sie sich im Laufe der Zeit gemäß den Regeln des Bitcoin-Protokolls entwickelt.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



Im vorigen Kapitel haben wir gesehen, dass Miner, die einen gültigen Block erzeugen, eine Belohnung erhalten, die sich aus den Gebühren für die im Block enthaltenen Transaktionen und einer Blocksubvention zusammensetzt. Wir haben jedoch noch nicht erklärt, wie die Höhe dieser Subvention bestimmt wird. Der Mechanismus, der diesen Wert festlegt und weiterentwickelt, wird als ***Halving*** bezeichnet.



### Was bedeutet Halbierung?



Halving ist ein in das Bitcoin-Protokoll programmiertes Ereignis, das die Blocksubvention halbiert, d. h. die maximale Menge an neuen Bitcoins, die der siegreiche Miner mit jedem Block erzeugen darf. Es wirkt sich nicht auf die Transaktionsgebühren aus: Die Gebühren bestehen unabhängig und werden weiterhin durch die Nutzeraktivität und den Wettbewerb um den Blockraum bestimmt.



Bei der Einführung von Bitcoin im Jahr 2009 wurde die Blocksubvention auf 50 BTC für jeden geförderten Block festgelegt. Seitdem wurde diese Subvention bei jeder Halbierung mehrmals halbiert.



![Image](assets/fr/029.webp)



Halving wird nicht durch ein Datum, sondern durch die Blockhöhe ausgelöst. Es wird **alle 210.000 Blöcke** ausgeführt. Da Bitcoin ein durchschnittliches Intervall von etwa 10 Minuten pro Block anstrebt, entsprechen 210.000 Blöcke etwa vier Jahren.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Wenn wir also `n` die Anzahl der bereits erfolgten Halbierungen beachten, kann die Blocksubvention in BTC wie folgt berechnet werden:



```text
subsidy(n) = 50 / 2^n
```



### Vergangene Halbierungen



Hier finden Sie eine Übersichtstabelle über die bereits erfolgten Halbierungen mit Angabe der Blockhöhe, des Datums und der nach dem Ereignis geltenden neuen Blocksubvention:



| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### Wann und wie endet der Zuschuss?



Halving wird wiederholt, solange der Zuschuss in der Mindesteinheit des Systems ausgedrückt werden kann: satoshi.



```text
1 BTC = 100 000 000 sats
```



Wenn die Subvention halbiert wird, erreichen wir schließlich Bruchteile eines Bitcoins, die so klein sind, dass sie weniger als 1 satoshi ausmachen. An diesem Punkt ist es nicht mehr möglich, eine halbe Einheit satoshi zu erzeugen. Die Geldschöpfung durch die Blocksubvention wird eingestellt, und die Miner werden ausschließlich durch Transaktionsgebühren entschädigt. Von diesem Zeitpunkt an sind alle Bitcoins im Umlauf, und es ist nicht mehr möglich, neue Einheiten zu produzieren.



Das endgültige Ende der Blocksubventionen wird bei der Blockstufe 6.930.000 eintreten, d.h. bei der 33. und letzten Halbierung. Dieses Ereignis wird um das Jahr 2140 erwartet, obwohl es unmöglich ist, ein genaues Datum zu nennen, da es von der tatsächlichen Geschwindigkeit abhängt, mit der bis dahin Blöcke gefunden werden.



Da die Blocksubvention einer geometrischen Folge mit einem Verhältnis von 1/2 bei jeder Halbierung folgt, war die Geldschöpfung in den Anfangstagen von Bitcoin extrem hoch und nimmt dann sehr schnell ab. Bei der 7. Halbierung werden bereits über 99 % der Bitcoins in Umlauf gebracht worden sein. Es wird erwartet, dass die 99 %-Schwelle zwischen 2032 und 2036 überschritten wird. Das bedeutet, dass es dann über 100 Jahre dauern wird, um das letzte verbleibende 1 % der Bitcoins abzubauen. Während die Geldinflation bei der Einführung von Bitcoin sehr hoch war, um eine weite Verbreitung der Währung zu ermöglichen, ist sie jetzt sehr niedrig und wird weiter sinken, bis sie das Niveau einer echten Hartwährung erreicht, deren Umlaufmenge nicht mehr steigen kann.



![Image](assets/fr/030.webp)



### Warum wird es niemals 21 Millionen BTC geben?



Die maximale Geldmenge von Bitcoin wird oft mit 21 Millionen BTC angegeben. Dies ist ein guter Näherungswert für das Verständnis der Geldpolitik, aber aus rein technischer Sicht wird die Gesamtmenge niemals genau 21.000.000 Bitcoins erreichen.



Der Hauptgrund ist mechanisch. Durch aufeinanderfolgende Halbierungen fällt die Blocksubvention schließlich unter den Mindestwert von 1 sat, was die Ausgabe vor Erreichen der exakten theoretischen Gesamtzahl beendet. Aufgrund dieser Mindestgranularität und der Rundungsregeln liegt die Gesamtzahl der durch die Subvention geschaffenen Bitcoins bei etwas weniger als 21 Millionen.



Darüber hinaus können auch geringfügige protokollbedingte Abweichungen zu dieser Entwicklung beitragen. So kann es in seltenen Fällen vorkommen, dass einige Miner nicht ihre volle Subvention in Anspruch genommen haben, wodurch sich die Menge der tatsächlich ausgegebenen Bitcoins definitiv verringert. Erwähnenswert ist auch der Genesis-Block, der von Satoshi am 3. Januar 2009 erzeugt wurde und dessen erzeugte Bitcoins nicht Teil des UTXO set sind, sowie bestimmte historische Ereignisse im Zusammenhang mit Fehlern, wie z. B. doppelte Coinbase-Transaktionskennungen.



Schließlich müssen auch alle Bitcoins berücksichtigt werden, die vernichtet oder gesperrt wurden:




- bitcoins in unlösbare Skripte gesperrt;
- die absichtlich durch "OP_RETURN"-Skripte zerstört wurden;
- oder Verlust von privaten Schlüsseln auf Anwendungsebene.



Theoretisch ist der Vorrat von Bitcoin daher auf 21 Millionen begrenzt. In der Praxis werden jedoch nie 21 Millionen Bitcoins im Umlauf sein.



## Die Coinbase-Transaktion


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



In den vorangegangenen Kapiteln haben wir zwei wichtige Punkte vorgestellt. Zum einen erhält der Miner, dem es gelingt, einen gültigen Block zu erzeugen und zu verbreiten, eine Belohnung. Zum anderen haben wir gesehen, dass sich diese Belohnung aus zwei verschiedenen Elementen zusammensetzt:




- eine Blocksubvention (ex nihilo geschaffene Bitcoins, deren Höchstbetrag vom Protokoll festgelegt und über Halvings schrittweise reduziert wird);
- alle Transaktionsgebühren, die von Nutzern gezahlt wurden, deren Transaktionen in den Block aufgenommen wurden.



Eine Frage bleibt jedoch offen: Durch welchen Mechanismus erhält der Miner diese Belohnung in Bitcoin? Genau das ist die Aufgabe einer bestimmten Transaktion, die als "Coinbase" bezeichnet wird.



### So funktioniert die Coinbase-Transaktion



Wie wir im ersten Teil des Kurses gesehen haben, enthält jeder Bitcoin-Block eine Liste von ausstehenden Transaktionen, die er bestätigen wird. Die allererste dieser Transaktionen ist immer die Coinbase-Transaktion. Sie ermöglicht es dem siegreichen Miner, seine Belohnung zu erhalten.



![Image](assets/fr/031.webp)



Auf den ersten Blick sieht sie wie eine klassische Bitcoin-Transaktion aus: Sie hat eine TXID, Ausgaben und ist im Merkle-Baum des Blocks enthalten. Sie unterscheidet sich jedoch in einem wichtigen Punkt: Sie gibt keine bestehenden UTXO aus.



Bei einer klassischen Bitcoin-Transaktion verweisen die "Inputs" auf frühere, nicht ausgegebene Outputs (UTXO), die den Inputwert liefern. Die Ausgänge verteilen diesen Wert dann an neue UTXO mit neuen Ausgabebedingungen weiter. Mit anderen Worten: Um Bitcoins zu versenden, müssen Sie sie bereits besitzen. Die Coinbase-Transaktion hingegen verbraucht keine Bitcoins als Input: Sie erzeugt Bitcoins als Output direkt aus dem Nichts.



Es ist genau dieser Mechanismus, der es ermöglicht, neue Bitcoins über die Blocksubvention in Umlauf zu bringen und dem Miner die Gebühren für die im Block enthaltenen Transaktionen gutzuschreiben. Die Coinbase-Transaktion kann sich nicht auf einen real existierenden UTXO beziehen (tatsächlich bezieht sie sich auf einen fiktiven UTXO), da ihre Rolle gerade darin besteht, einen Teil des Wertes (die Subvention) zu schaffen und den anderen Teil (die Gebühren) zurückzuerhalten, ohne sie von einer früheren Transaktion zu erhalten. Damit das gesamte System kohärent bleibt, muss der Teil, der den Gebühren entspricht, genau der Summe der Bitcoins entsprechen, die als Inputs verbraucht, aber nicht als Outputs in den anderen Transaktionen des Blocks wiederhergestellt wurden.



![Image](assets/fr/032.webp)



Diese Transaktion ist nicht optional. Ein Block, der keine Coinbase-Transaktion enthält, ist ungültig und wird von den Netzwerkknoten systematisch abgelehnt.



⚠️ Bitte beachten Sie: Der Begriff "*coinbase*" hat nichts mit der gleichnamigen Tauschplattform zu tun. In Bitcoin bezieht sich "*coinbase*" historisch gesehen auf die Transaktion, die den Block Reward erzeugt. Das Unternehmen hat diesen Begriff einfach für seinen Namen übernommen.



Die coinbase-Transaktion erfüllt eigentlich mehrere Funktionen gleichzeitig:




- Die erste ist die, die wir gerade beschrieben haben: Sie weist dem Miner die Belohnung zu, die ihm für die Erzeugung eines gültigen Blocks zusteht.
- Seine zweite, eher technische Rolle besteht darin, die kryptografische Verpflichtung mit den Zeugen (Signaturen) der SegWit-Transaktionen im Block zu verankern.
- Eine dritte Rolle, die diesmal nicht direkt mit dem Protokoll zusammenhängt, sondern mit der modernen Industrialisierung von mining, besteht darin, dass die Coinbase jetzt häufig zur Verankerung beliebiger technischer Daten verwendet wird. Diese Daten stehen in der Regel im Zusammenhang mit dem Betrieb von mining-Pools und deren interner Organisation.



Damit Sie diese verschiedenen Verwendungszwecke besser verstehen können, werden wir uns nun die Struktur der Coinbase-Transaktion genauer ansehen.



### Die Grundstruktur der Coinbase-Transaktion



Eine Coinbase-Transaktion muss genau eine Eingabe enthalten. Der Einfachheit halber sagen wir manchmal, dass sie keine Eingabe hat, weil diese Eingabe kein reales UTXO ausgibt. In Wirklichkeit gibt es eine Eingabe mit einer referenzierten Quelle, die aber absichtlich auf ein nicht existierendes UTXO verweist.



Wie wir bereits gesehen haben, muss jede Bitcoin-Transaktion UTXO als Eingabe verbrauchen, um gültige Ausgaben zu erzeugen. In der Bitcoin-Transaktion erfolgt dieser Verbrauch in Form eines Verweises auf einen vorhandenen UTXO als Eingabe. Diese Referenzierung erfolgt einfach durch die Angabe der Kennung der vorherigen Transaktion (derjenigen, in der die UTXO erstellt wurde) sowie ihres Indexes unter den Ausgaben dieser Transaktion. Konkret wird ein UTXO durch einen Hash (die vorherige TXID) und einen Index definiert.



Im Fall der Coinbase-Transaktion muss die Eingabe jedoch zwangsläufig auf diesen speziellen gefälschten UTXO mit einer TXID voller Nullen verweisen, die keiner echten TXID entspricht, anstatt auf einen real existierenden UTXO zu verweisen:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Unmittelbar danach folgt der falsche Index:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



Im grundlegenden Bitcoin-Protokoll, wie in Satoshi Nakamoto beschrieben, ist diese falsche Eingabe die einzige Einschränkung, die der Coinbase-Transaktion auferlegt wird.



Wie jeder UTXO, auf den in der Eingabe einer Transaktion verwiesen wird, ist er mit einem "ScriptSig"-Feld verbunden. Bei einer herkömmlichen Transaktion enthält dieses "ScriptSig"-Feld die Elemente, die erforderlich sind, um den "ScriptPubKey" zu erfüllen und somit den ausgegebenen UTXO zu entsperren. Im besonderen Fall von coinbase ist das Feld "ScriptSig" jedoch völlig frei, da das UTXO, auf das verwiesen wird, absichtlich fiktiv ist. Miner können daher beliebige Daten eingeben. Wir werden uns später ansehen, wie diese Freiheit genutzt wird.


Zusätzlich zu diesem falschen Eingang gibt es einen oder mehrere ganz normale Ausgänge, die es dem Miner ermöglichen, die Bitcoins von der Belohnung auf einer seiner Bitcoin-Adressen abzuholen. Bei diesen Ausgängen handelt es sich um UTXO, die durch einen "ScriptPubKey" gesperrt sind (z. B. ein Skript, das auf eine vom Miner oder dem Pool kontrollierte Adresse zeigt). Die einzige Besonderheit liegt hier in der Regel für die Berechnung ihres Wertes: Die Gesamtsumme der Outputs der Coinbase darf niemals die maximal zulässige Subvention übersteigen, zu der die Blockgebühren hinzukommen.



Historisch gesehen lässt sich die Coinbase-Transaktion also auf dieses einfache Schema reduzieren: eine gefälschte Eingabe, die auf einen nicht existierenden UTXO verweist, und eine oder mehrere Ausgaben, die dazu dienen, die Blockbelohnung an den siegreichen Miner zu verteilen. Heute ist die Coinbase jedoch nicht mehr auf diese Verteilungsfunktion beschränkt. Ihre besondere Position im Block und die große Flexibilität ihrer Struktur haben zu neuen Anwendungen geführt, sowohl im Protokoll selbst als auch in mining-Pool-Verwaltungsmechanismen.



### Andere Verwendungen von coinbase



Im Laufe der Zeit hat sich die Coinbase-Transaktion zu einem besonders praktischen Einfügepunkt für die Integration einer Vielzahl von Informationen entwickelt, die für mining und für die Blockstruktur selbst nützlich sind. Werfen wir einen Blick auf sie, um die Gesamtorganisation von coinbase besser zu verstehen.



#### Der BIP-34



BIP-34 ist ein fork Soft, der im März 2013 eingeführt wurde, beginnend mit Block 227.930, mit dem Version 2 der Bitcoin-Blöcke eingeführt wurde. Diese neue Version erfordert, dass jeder Block in der `scriptSig` der coinbase-Transaktion die Höhe des zu erstellenden Blocks enthält.



Zum einen verdeutlicht diese Entwicklung die Art und Weise, in der das Netzwerk die Blockstruktur und die Konsensregeln weiterentwickeln will. Zum anderen stellt sie die Einzigartigkeit jedes Blocks und jeder Coinbase-Transaktion sicher.



Somit ist das `scriptSig` von coinbase nicht völlig frei. Seit der Aktivierung von BIP-34 ist sie einfach gezwungen, mit der Höhe des Blocks zu beginnen, in dem diese coinbase-Transaktion enthalten ist.



![Image](assets/fr/035.webp)



#### Das Extra-Nonce



Wie wir in den ersten Kapiteln dieses Kurses gesehen haben, verfügt der Miner über ein 32-Bit-Nonce-Feld im Block-Header, das er durch Versuch und Irrtum modifiziert, um einen Hash zu finden, der kleiner oder gleich dem Zielwert ist. Dieser 32-Bit-Raum erlaubt bereits eine sehr große Anzahl von Kombinationen, die untersucht werden können, aber wenn der mining-Schwierigkeitsgrad hoch ist, kann dieser Bereich in relativ kurzer Zeit vollständig ausgeschöpft werden, so dass möglicherweise keine Kombination gefunden wird, die einen gültigen Hash ergibt. Wenn alle möglichen Werte des `nonce` erfolglos getestet wurden, muss der Miner dann ein anderes Element ändern, um den Block-Header zu ändern und eine neue Reihe von Versuchen zu starten.



Da die Coinbase-Transaktion über die "ScriptSig" ihrer Eingabe ein freies Feld anbietet, besteht die Lösung zur Erweiterung des Nonce-Raums darin, einen Teil dieser "ScriptSig" auszunutzen. Dies wird im Allgemeinen als "extra-nonce" bezeichnet. Durch Änderung der Extra-Nonce ändert der Miner die "ScriptSig" von Coinbase, d. h. den Transaktionsbezeichner, dann die Merkle-Wurzel des Blocks und schließlich den Block-Header selbst. Auf diese Weise erhält er einen neuen Suchraum von Hashes, den er erkunden kann, ohne die anderen Komponenten seines Kandidatenblocks ändern zu müssen.



![Image](assets/fr/036.webp)



#### Identifizierung von Pools und Minern



Heute ist ein sehr großer Teil des weltweiten hashrate in mining-Pools organisiert. In diesen Strukturen schließen sich einzelne Bergleute zusammen, um ihre Arbeit zu bündeln und die Streuung ihrer Einnahmen zu verringern.



Aus betrieblichen Gründen nutzen mining-Pools auch das freie Feld der coinbase-Eingabe `scriptSig`, um verschiedene Informationen einzufügen. Diese variieren von Pool zu Pool und von Netzwerkprotokoll zu Netzwerkprotokoll, umfassen aber im Allgemeinen eine eindeutige Kennung (oft eine zusätzliche Nonce, die in mehrere Unterteile unterteilt ist), die jedem Schürfer zugewiesen wird, um doppelte Arbeit innerhalb des Pools zu vermeiden. In der Regel wird ein Pool-Identifikations-Tag hinzugefügt, das für die öffentliche Zuordnung gefundener Blöcke, mining-Statistiken und andere Verfolgungszwecke verwendet wird.



![Image](assets/fr/037.webp)



#### Das Engagement von SegWit



Seit der SegWit soft fork im Jahr 2017 aktiviert wurde, wurden die Zeugen-Daten (d. h. im Allgemeinen die Signaturen) von den Transaktions-Stammdaten getrennt, um insbesondere das Problem der Verfälschbarkeit von Bitcoin-Transaktionen zu beheben. Diese Trennung führt daher ein neues Element ein, das im Block übertragen werden muss.



Zu diesem Zweck werden die Zeugen in einem anderen Merkle-Baum zusammengefasst, dessen Wurzel dann über eine OP_RETURN-Ausgabe an die Coinbase-Transaktion übergeben wird.



![Image](assets/fr/038.webp)



Ich werde in diesem Kurs nicht näher auf diesen Mechanismus eingehen, da er den Rahmen dieses Artikels sprengen würde, aber denken Sie daran, dass seit der Einführung von SegWit die coinbase-Transaktion als Vehikel dient, um im Block einen Fingerabdruck zu verankern, der alle SegWit-Zeugen zusammenfasst. Die Zeugen werden in einem unabhängigen Merkle-Baum abgelegt, die Wurzel dieses Baums wird in eine Ausgabe der coinbase-Transaktion geschrieben, und diese coinbase-Transaktion selbst wird zusammen mit allen anderen Transaktionen in den Haupt-Merkle-Baum aufgenommen, dessen Wurzel im Blockkopf erscheint. Auf diese Weise werden die Zeugen, die getrennt von den Haupttransaktionsdaten gespeichert werden, weiterhin in den Block-Header übernommen.



![Image](assets/fr/039.webp)



#### Beliebige Meldungen



Da die `scriptSig` das freie Einfügen beliebiger, vom Miner gewählter Informationen erlaubt, haben einige die Gelegenheit genutzt, um eher persönliche als technische Nachrichten hinzuzufügen. Der berühmteste Fall ist natürlich Satoshi Nakamoto mit seiner inzwischen ikonischen Nachricht:



> The Times 03/Jan/2009 Kanzler am Rande der zweiten Rettungsaktion für Banken

Diese Nachricht, die im Genesis-Block (dem allerersten Block von Bitcoin) enthalten ist, ist in der `scriptSig` der Coinbase-Transaktion tatsächlich hexadezimal kodiert:



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### Die Fälligkeitsfrist


Sobald der Block abgebaut und verteilt wurde, erscheint die Coinbase-Transaktion wie jede andere Transaktion auf der Blockchain. Sie erzeugt UTXO für den siegreichen Schürfer und ermöglicht es ihm, seine Belohnung zu erhalten. Diese UTXO können jedoch nicht sofort ausgegeben werden: Sie unterliegen einer Fälligkeitsfrist. Diese Fälligkeit ist auf 100 Blöcke nach dem Block festgelegt, der die Coinbase enthält. Konkret bedeutet dies, dass die Coinbase-Transaktion insgesamt 101 Bestätigungen erhalten muss, damit der siegreiche Schürfer seinen Output ausgeben kann.


![Image](assets/fr/040.webp)


Das Ziel dieser Regel ist es, die Auswirkungen von Kettenumstellungen auf die Wirtschaft zu begrenzen. Wie wir in den vorherigen Kapiteln gesehen haben, kann es vorkommen, dass auf derselben Höhe zwei verschiedene gültige Blöcke fast gleichzeitig von verschiedenen Minern gefunden werden. Für einen kurzen Moment kann sich das Netzwerk spalten: Einige Knoten erhalten zuerst Block A, während andere zuerst Block B sehen. Dann, im Laufe der folgenden Blöcke, sammelt einer der beiden Zweige mehr Arbeit an und wird zum Referenzzweig. Der andere Zweig wird aufgegeben und seine Blöcke werden obsolet. Die darin enthaltenen Transaktionen können dann theoretisch in die Mempools zurückkehren und auf ihre Bestätigung warten.



In der Praxis kommt dies nur selten vor, da der Gebührenmarkt häufig dazu führt, dass fast dieselben Transaktionen in zwei konkurrierenden Blöcken in derselben Höhe erscheinen. Dies ist einer der Gründe, warum eine Bitcoin-Transaktion nach sechs Bestätigungen gemeinhin als unveränderlich angesehen wird: Umstrukturierungen von mehr als sechs Blöcken sind so unwahrscheinlich, dass sie vernünftigerweise als unmöglich angesehen werden können.



![Image](assets/fr/041.webp)



Das Problem bei diesen Umstrukturierungen im Falle der Coinbase-Transaktion ist, dass es sich nicht um eine gewöhnliche Transaktion handelt. Es werden brandneue Bitcoins in den Umlauf gebracht. Wenn die Blockbelohnung sofort ausgegeben werden könnte, könnte eine problematische Kaskadensituation entstehen:




- ein Miner gibt Bitcoins von einer Coinbase aus,
- diese Bitcoins in der Wirtschaft zirkulieren,
- dann wurde der ursprüngliche Block im Zuge einer Umstrukturierung endgültig aufgegeben.



Die im Umlauf befindlichen Bitcoins hätten dann in der endgültigen Kette nie existiert, und eine Reihe von Transaktionen, die zum Zeitpunkt der Ausgabe gültig waren, wären im Nachhinein ungültig geworden.



Die Laufzeit ist so lang, dass dieses Szenario unrealistisch ist. Eine Umstrukturierung von 101 Blöcken wird in der Praxis als unmöglich angesehen (auch wenn die Wahrscheinlichkeit dafür verschwindend gering ist). Wir wissen nicht genau, warum Satoshi einen so hohen Wert für die Laufzeit gewählt hat, aber es ist wahrscheinlich, dass er so gewählt wurde, dass der Mechanismus auch im Falle größerer Netzstörungen funktionsfähig bleibt.



Diese Regel verhindert, dass neu geschaffenes Geld mit Blockprämie in Umlauf kommt, bevor der Block, in dem es sich befindet, sicher unter einer großen Menge an angesammelter Arbeit begraben wurde.



---

Wir sind nun am Ende unserer Erklärung der Funktionsweise von Bitcoin mining angelangt. Sie sollten jetzt ein klares Bild von den grundlegenden Mechanismen haben.



Im letzten Teil des Kurses werden wir zu konkreteren Aspekten zurückkehren, um Ihnen zu zeigen, wie Bitcoin mining in der realen Welt umgesetzt wird: seine Industrialisierung, die verwendeten Maschinen, die Gruppierung der Spieler usw. Ziel ist es, Ihnen einen Gesamtüberblick über Bitcoin mining zu geben, sowohl aus der theoretischen und protokollarischen Perspektive, die wir soeben gesehen haben, als auch aus der praktischen und operativen Seite.



# Die Bitcoin mining-Industrie


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## Die Entwicklung der mining-Maschinen


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



In den ersten Tagen von Bitcoin war mining keine industrielle Tätigkeit. Es war Teil der Bitcoin-Software, die auf einem PC gestartet wurde, oft aus Neugierde, manchmal zur Unterstützung des Netzwerks und in zweiter Linie, um Bitcoins zu erhalten, die damals praktisch keinen Marktwert hatten.



Im Laufe der Jahre hat sich diese Tätigkeit gewandelt: Die Maschinen haben sich verändert, der Schwierigkeitsgrad ist explodiert, und mining hat sich zu einer eigenständigen Industrie entwickelt. Werfen wir einen Blick auf die operativen Aspekte von Bitcoin mining.



### Erste Schritte: mining mit einer CPU



Im Jahr 2009 und in den Anfangsjahren wurde mining hauptsächlich mit der CPU eines herkömmlichen Computers ausgeführt. Bitcoin war damals nur ein einfaches Stück Software, das als wallet, als Knotenpunkt und als Miner diente. Es genügte, die Software des Satoshi Nakamoto auf dem eigenen Computer zu starten, um am mining-Prozess teilzunehmen und in vielen Fällen Blöcke zu finden.



Eine CPU kann alles, aber sie ist nicht für alles optimiert. Sie führt sehr allgemeine Anweisungen mit komplexer Logik aus. Für eine Aufgabe wie das wiederholte Hashing von Block-Headern ist sie nicht das ideale Werkzeug, aber beim Start des Netzes ist der Schwierigkeitsgrad so niedrig, dass es mehr als genug ist, um Blöcke zu finden.



Dieser Zeitraum ist wichtig, weil er uns an einen wichtigen Punkt erinnert: proof of work hängt nicht von einer bestimmten Kategorie von Geräten ab. Was zählt, ist die Fähigkeit, Hashes schneller als andere zu berechnen, und das zu einem bestimmten Preis. Sobald ein technischer Vorteil auftritt, wird er automatisch in einen wirtschaftlichen Vorteil umgewandelt. Absolut gesehen ist es aber auch heute noch möglich, mit einer herkömmlichen CPU zu versuchen, Bitcoin-Blöcke zu finden. Diesen Ansatz verfolgt zum Beispiel das Projekt NerdMiner. Die Chancen, einen Block zu finden, sind praktisch gleich Null, aber es besteht immer noch eine infinitesimale Wahrscheinlichkeit.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Umstieg auf GPUs



Schon bald erkannten die Miner, dass der Engpass nicht in der Leistung lag, sondern in der Fähigkeit, eine große Anzahl ähnlicher Operationen parallel durchzuführen. Dies war genau das, was Grafikprozessoren (GPUs) tun konnten. Ursprünglich war ein Grafikprozessor dafür konzipiert, dieselben Operationen mit großen Datenmengen durchzuführen. Diese Architektur eignete sich perfekt für eine Aufgabe wie das wiederholte Hashing: Anstelle einiger weniger hochflexibler Kerne verfügte man über Hunderte, später Tausende von Einheiten, die dieselben Befehle gleichzeitig ausführen konnten.



Bei vergleichbarem Stromverbrauch kann ein Grafikprozessor weitaus mehr Hashes pro Sekunde erzeugen als eine CPU. Zur gleichen Zeit hatte der Bitcoin einen Wechselkurs gegenüber dem Dollar, sein Wert stieg, und es entstanden Tauschplattformen. Von da an begann sich das Wesen von mining zu verändern. Es ging nicht mehr nur um die Teilnahme, sondern um das Geldverdienen. Dedizierte Konfigurationen tauchten auf: Maschinen, die um mehrere Grafikkarten herum gebaut wurden, manchmal ohne Bildschirm, mit einem minimalen System und spezialisierter Software, deren einziger Zweck das Mining war.



Zu diesem Zeitpunkt begann die Schwierigkeit von mining zu explodieren. Zwischen Mitte 2010 und Mitte 2011 stieg er sogar um das 1.000-fache an. Mechanisch gesehen beginnt die Spezialisierung, genau wie bei den frühen Formen der Industrialisierung, und gewöhnliche Nutzer, die sich damit begnügen, die Bitcoin-Software auf ihren PCs laufen zu lassen, haben nur noch eine sehr geringe Chance, einen gültigen Block zu finden.



![Image](assets/fr/044.webp)



*Quelle: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



Zwischen der GPU-Ära und der modernen ASIC-Ära gab es eine Zwischenphase: die Verwendung von FPGAs. Ein FPGA ist ein reprogrammierbares Bauteil: es kann so konfiguriert werden, dass es direkt eine Logikschaltung für eine bestimmte Berechnung implementiert, in diesem Fall SHA256d. Die Idee war, sich noch weiter von der Allzweck-Hardware (CPU/GPU) zu entfernen, um die Energieeffizienz zu steigern. Doch schon bald sollten die Verbesserungen, die virtuell auf FPGAs erzielt wurden, auch physisch auf die Chips selbst angewendet werden: das ist die Ankunft von ASIC.



### Die Ankunft von ASIC



Die letzte Stufe der Spezialisierung der mining-Hardware war das Erscheinen der ASIC (*anwendungsspezifische integrierte Schaltkreise*). Ein ASIC ist ein Chip, der für eine einzige Aufgabe entwickelt wurde. Im Fall von Bitcoin mining ist diese Aufgabe genau die Ausführung von `SHA256d` mit maximaler Geschwindigkeit und mit optimaler Energieeffizienz. Im Gegensatz zu einer GPU wird ein ASIC nicht für Spiele, 3D-Rendering oder KI verwendet. Er dient dem Hashing, und das ist auch schon alles.



![Image](assets/fr/045.webp)



*ASIC S21 XP hergestellt von Bitmain*



Diese Spezialisierung hat zwei wesentliche Konsequenzen:




- Der erste ist ein Sprung in Leistung und Effizienz. Bei Geräten einer vergleichbaren Generation erzeugt ein ASIC weitaus mehr Hashes pro Sekunde als ein Grafikprozessor und verbraucht dabei weniger Strom. Der Mining mit einem Grafikprozessor war schnell nicht mehr wettbewerbsfähig: Obwohl er technisch funktionierte, überstiegen die Stromkosten in den meisten Fällen bei weitem die erwarteten Einnahmen;
- Der zweite Grund ist eine Änderung des Modells: Die Investitionen wurden hauptsächlich auf Hardware für den industriellen Einsatz umgestellt. Bei Mining geht es nun darum, Maschinen zu kaufen, die für diesen Zweck entwickelt wurden, sie kontinuierlich mit Strom zu versorgen, zu kühlen, zu warten und ihre Überalterung aufzufangen. Denn ein ASIC ist wirtschaftlich nicht ewig haltbar: Wenn eine neue, leistungsfähigere Generation auf den Markt kommt, werden die alten Maschinen immer unrentabler, selbst wenn sie noch funktionsfähig sind.



Von diesem Zeitpunkt an geht es nicht mehr nur um ein Hobby. Wir sprechen über einen Sektor, in dem die Wettbewerbsfähigkeit von einer Gleichung abhängt:




- kosten für Strom;
- kosten für Ausrüstung und Abschreibung;
- fähigkeit zur Kühlung und zum Betrieb in großem Maßstab;
- verfügbarkeit und Zuverlässigkeit der Maschinen;
- geschwindigkeit der Kommunikation;
- usw.



### Mining Bauernhöfe



Eine isolierte Maschine kann Bergbau betreiben, aber durch die Gruppierung von Hunderten und später Tausenden von ASIC an einem einzigen Standort können wir die Fixkosten teilen, die Logistik optimieren und uns dem Modell eines spezialisierten Rechenzentrums annähern.



Eine mining-Farm ist in ihrer einfachsten Form ein Gebäude (oder eine Reihe von Containern), die mit ASIC gefüllt sind und rund um die Uhr laufen. Die Herausforderung besteht nun darin, stabile Betriebsbedingungen aufrechtzuerhalten:




- große Mengen an preiswerter, stabiler elektrischer Energie liefern;
- wärmemanagement, um Drosselung zu vermeiden, da die Energiedichte beträchtlich ist;
- staub filtern, Feuchtigkeit kontrollieren, reinigen;
- echtzeit-Überwachung der Maschinenleistung (Temperaturen, Hardwarefehler, hashrate-Abstürze usw.).



![Image](assets/fr/043.webp)



*Eines der sieben Gebäude für Bitcoin mining am Standort Rockdale von Riot Platforms in der Nähe von Austin, Texas. Dieses Gebäude ist speziell der Immersion gewidmet mining*



Mining wird nun von industriellen Akteuren vorangetrieben, von denen einige börsennotiert sind und sehr große Farmen bauen und betreiben. Dazu gehören MARA Holdings (Nasdaq: `MARA`) und Riot Platforms (Nasdaq: `RIOT`).



![Image](assets/fr/042.webp)



Auch ohne auf die Details der Rentabilitätsmodelle einzugehen, ist es wichtig zu verstehen, warum mining diese Form angenommen hat. Proof-of-Work ist ein Wettbewerbsmechanismus: Die Wahrscheinlichkeit, einen Block zu finden und damit Geld zu verdienen, ist proportional zu dem Anteil an hashrate, den man einsetzt. Daraus ergibt sich ein ständiger Druck, die Rechenleistung zu erhöhen, die Kosten pro Recheneinheit zu senken und Verluste zu begrenzen. Infolgedessen werden Umgebungen, die billigeren Strom, ein für die Kühlung günstiges Klima oder eine reichhaltige Energieinfrastruktur bieten, natürlich immer attraktiver.



Mining Bitcoin hat sich also von einer Tätigkeit, die in ihren Anfängen für jedermann zugänglich war, zu einer Tätigkeit entwickelt, die von spezialisierter Ausrüstung und professionellen Verfahren beherrscht wird. Dies ändert jedoch nichts an den Regeln des Protokolls. Theoretisch kann jeder mit jeder Maschine schürfen. Aber in der Praxis hat der Schwierigkeitsgrad und die Effizienz von ASIC dazu geführt, dass das heimische mining in den meisten Fällen nicht mehr wettbewerbsfähig ist.



Natürlich gibt es immer noch Situationen, in denen ein mining für Sie interessant sein kann, z. B. wenn Sie von sehr billigem Strom profitieren oder wenn Sie die von Ihrem Miner erzeugte Wärme generated nutzen, um Ihr Haus im Winter zu heizen. Aber in jedem Fall müssen Sie eine Maschine kaufen, die mit einem ASIC-Chip ausgestattet ist. Und da Ihre mining-Leistung im Vergleich zum Bitcoin-Netz extrem klein bleibt, müssen Sie einen Weg finden, um die Varianz Ihres Einkommens zu verringern: Genau das ist die Aufgabe der mining-Pools, die wir im nächsten Kapitel besprechen werden.



Wenn Sie mining-Lösungen mit Wärmerückgewinnung für zu Hause erforschen möchten, finden Sie hier Anleitungen zu verschiedenen Werkzeugen, sowohl gebrauchsfertig als auch zum Selbstbau:



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Gruppierung in mining-Pools


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining Bitcoin ist mit laufenden und unvermeidlichen Kosten verbunden, zu denen vor allem der Stromverbrauch der Maschinen gehört. Diese Kosten fallen unabhängig von den Ergebnissen an, auch wenn die Einnahmen aus mining naturgemäß selten und zufällig sind. Die Entdeckung eines Blocks hängt ausschließlich vom Anteil des Miners an hashrate ab, was die Erträge umso unvorhersehbarer macht, je kleiner dieser Anteil ist. Es ist genau dieses praktische Problem, das schnell zur weit verbreiteten Nutzung von mining-Pools führte. In diesem letzten Kapitel des MIN 101-Kurses biete ich eine Einführung in die Prinzipien und den Betrieb von mining-Pools in Bitcoin.



### Was ist ein mining-Pool?



Ein mining-Pool ist eine Organisation (oft ein Online-Dienst), die die Rechenleistung vieler unabhängiger Miner bündelt, um die Häufigkeit zu erhöhen, mit der ihre Gruppe Blöcke findet. Wenn der Pool einen Block findet, wird die Blockbelohnung unter den Teilnehmern nach internen Poolregeln verteilt (die im Kurs MIN 201 behandelt werden, da sie für MIN 101 zu komplex sind).



Die Teilnehmer an einem mining-Pool werden dann oft als "Hashers" und nicht als "Miners" bezeichnet, da sie nicht mehr die gesamte mining-Arbeit ausführen, sondern lediglich die Daten hacken, die ihnen vom Pool übermittelt werden.



Achten Sie darauf, dass Sie den mining-Pool nicht mit der mining-Farm verwechseln. Dies sind zwei unterschiedliche Konzepte. Wie wir im vorherigen Kapitel gesehen haben, ist eine Farm ein physischer Standort, an dem eine einzige Einheit zahlreiche mining-Maschinen betreibt. Ein Pool hingegen ist vor allem eine virtuelle Gruppierung: Tausende von Maschinen, die oft geografisch verstreut sind, arbeiten unter einer gemeinsamen Koordination. Eine Farm kann jedoch an einem Pool teilnehmen und tut dies auch häufig.



![Image](assets/fr/048.webp)



### Verringerung der Einkommensabweichung



Warum also einem Pool beitreten? Ganz einfach, weil das Ergebnis der mining-Aktivität probabilistisch ist: Bei jedem Hash-Versuch besteht eine sehr geringe Chance, dass er das Schwierigkeitsziel erreicht und somit einen gültigen Block erzeugt.



Auf lange Sicht sollte Ihr durchschnittlicher Verdienst proportional zu Ihrem Anteil am gesamten hashrate sein. Dieser Grundsatz ergibt sich direkt aus den Gesetzen der Wahrscheinlichkeit: Jede Hash-Berechnung stellt eine unabhängige Zufallsziehung dar, und nach dem Gesetz der großen Zahlen konvergiert die Häufigkeit, mit der Sie Blöcke entdecken, mathematisch gesehen zu Ihrem Anteil an den gesamten hashrate des Netzwerks. Kurz- bis mittelfristig kann Ihr tatsächlicher Verdienst jedoch äußerst unregelmäßig ausfallen. Diese Diskrepanz zwischen dem theoretischen Durchschnitt und der zufälligen Realität nennen wir in der Mathematik **Varianz**.



Hier ein einfaches Beispiel, um das Prinzip zu veranschaulichen:




- Das Bitcoin-Netz produziert durchschnittlich 144 Blöcke pro Tag (etwa ein Block alle 10 Minuten);
- Wenn Sie `0,0001 %` der gesamten hashrate haben, ist Ihre Erwartung `144 × 0,000001`, oder `0,000144` Block/Tag;
- Mit anderen Worten: Sie sollten im Durchschnitt alle 1/0,000144 Tage einen Block finden, d. h. alle 6.944 Tage, also etwa 19 Jahre.



Dieser Wert entspricht jedoch nur einer mathematischen Erwartung: Die Verteilung der Entdeckungszeiten folgt einem Zufallsgesetz, so dass es in der Praxis durchaus möglich ist, auch über einen sehr langen Zeitraum hinweg keinen einzigen Block zu entdecken. Man kann Pech haben und sehr lange nichts finden, während man gleichzeitig wiederkehrende Kosten (Strom, Wartung, Abschreibung der Geräte...) bezahlt.



Der mining-Pool ändert die Art dieses Problems: Durch die Kombination von hashrate findet der Pool häufiger Blöcke. Jeder Teilnehmer erklärt sich dann bereit, nur einen Bruchteil jedes gefundenen Blocks zu erhalten, dafür aber viel häufiger. Es handelt sich um eine Umwandlung von einem stark schwankenden, weit gestreuten Einkommen in ein regelmäßigeres Einkommen, wobei die Kosten für die Aufteilung der Belohnungen und die Zahlung von Servicegebühren anfallen.



### Warum sinkt die Varianz, wenn man Gruppen zusammenfasst?



Je höher die Rechenleistung, desto höher die erwartete Häufigkeit der gefundenen Blöcke. Noch wichtiger ist, dass die beobachteten Ergebnisse umso näher am statistischen Durchschnitt über einen bestimmten Zeitraum liegen, je häufiger die Ereignisse auftreten.



Als Einzelkämpfer kann ein Kleinschürfer jahrelang ohne einen einzigen Block auskommen, dann eines Tages eine große Auszahlung erhalten und dann nichts mehr. In einem Pool gilt immer noch dieselbe Wahrscheinlichkeitsrealität, aber sie wird auf kollektiver Ebene geglättet: Der Pool findet häufiger Blöcke, und die Umverteilung wandelt diese Ereignisse in regelmäßigere Auszahlungen für jeden Teilnehmer um. **Der mining-Pool verkauft daher Vorhersagbarkeit für die mining-Aktivität.



### Historische Denkmäler



Wie wir im vorangegangenen Kapitel gesehen haben, konnte mining zu Beginn mit einem herkömmlichen Computer allein bewältigt werden, da der Schwierigkeitsgrad sehr niedrig war. Aber als das globale hashrate explodierte (GPU, dann ASIC), wurde das Solo-mining für die meisten Teilnehmer zu einem sehr zeitaufwändigen Glücksspiel.



Die ersten Pools wurden genau als Reaktion auf diese neue Realität gegründet. Braiins Pool (ehemals Slush Pool / Bitcoin.cz) ist der erste Bitcoin-mining-Pool: Er hat seinen ersten Block am 16. Dezember 2010 geschürft. Der Erfolg dieses ersten mining-Pools war rasant, da er in nur wenigen Tagen fast 3,5 % des weltweiten hashrate eroberte.



![Image](assets/fr/047.webp)



Auf der technischen Seite wurden Pools dann um spezielle Kommunikationsprotokolle zwischen dem Pool und den Minern herum strukturiert (z.B. Stratum, dann Stratum V2), um die verteilte Arbeit effizient zu orchestrieren. In unserem Kurs MIN 201 werden wir uns diese Konzepte genauer ansehen.



### Die moderne Situation



Zum Zeitpunkt der Abfassung dieses Artikels (Anfang 2026) liegt der globale Bitcoin hashrate bei einer Größenordnung von zetta-hash pro Sekunde (= 1.000 EH/s = 1.000.000.000.000.000.000.000 Hashes pro Sekunde), und fast alle gefundenen Blöcke stammen aus mining-Pools.



Hier ist eine Rangliste der wichtigsten mining-Pools und ihres jeweiligen Anteils an hashrate. Diese Rangliste wird sich wahrscheinlich noch ändern, wenn Sie diesen Kurs lesen. Für aktuelle Daten besuchen Sie bitte [mempool.space](https://mempool.space/graphs/mining/pools).



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Quelle [mempool.space](https://mempool.space/graphs/mining/pools), Einmonatsdaten, 16. Dezember 2025 bis 16. Januar 2025.*



In einem Kurs für Fortgeschrittene werden wir uns eingehender mit der internen Funktionsweise der Pools befassen (Anteile, Netzwerkprotokolle, Zahlungsmethoden ...), denn hier kommen die Details ins Spiel, die sowohl die Rentabilität des Miners als auch die möglichen Auswirkungen auf Bitcoin bestimmen.



---

Wir sind nun am Ende von MIN 101 angelangt. Vielen Dank, dass Sie den Kurs bis zum Ende durchgearbeitet haben. Wenn Sie Ihre im Laufe des Kurses erworbenen Fähigkeiten bewerten möchten, erwartet Sie im nächsten Abschnitt eine Abschlussprüfung.



Mit dem soeben erworbenen Grundwissen können Sie nun auf Plan ₿ Academy weiterführende Kurse zu mining belegen, sei es in der Theorie, wie dieser, oder in der Praxis, damit auch Sie an Bitcoin mining teilnehmen können!



# Letzter Teil


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Rezensionen und Bewertungen


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Abschlussprüfung


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Schlussfolgerung


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>