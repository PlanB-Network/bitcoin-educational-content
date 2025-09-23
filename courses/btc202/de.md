---
name: Einrichten Ihres ersten Bitcoin-Knotens
goal: Verstehen, Installieren, Konfigurieren und Verwenden eines Bitcoin-Knotens
objectives: 


  - Die Rolle und den Zweck eines Bitcoin-Knotens zu verstehen.
  - Die verschiedenen verfügbaren Hardware- und Softwarelösungen zu identifizieren.
  - Installieren und konfigurieren Sie einen Full node (Bitcoin core).
  - Verwenden Sie den Interface Regenschirm und fügen Sie nützliche Anwendungen hinzu.
  - Verbinden Sie einen persönlichen Wallet mit seinem eigenen Knoten.
  - Erkunden Sie die erweiterten Einstellungen und die besten Sicherheitspraktiken.


---
# Werden Sie ein souveräner Bitcoiner



Sie kennen wahrscheinlich das Sprichwort "Nicht Ihre Schlüssel, nicht Ihre Münzen", das zur Selbstverwahrung Ihrer Bitcoins aufruft. Der Besitz Ihrer eigenen Schlüssel ist in der Tat ein wichtiger erster Schritt, aber er reicht nicht aus. Um echte monetäre Souveränität zu erlangen, müssen Sie auch Ihren eigenen Bitcoin-Knoten installieren und verwenden. Dieser Kurs soll Sie durch diesen grundlegenden Schritt auf Ihrer Bitcoin Reise führen!



BTC 202 ist ein zugänglicher Kurs, der Ihnen beibringen soll, wie Sie Ihren eigenen Bitcoin-Knoten spinnen können, auch wenn Sie kein technischer Experte sind. Wir beginnen damit, zu definieren, was ein Bitcoin-Knoten ist, wozu er dient und warum es absolut notwendig ist, selbst einen zu spinnen. Dann führe ich Sie Schritt für Schritt durch die Auswahl Ihrer Hardware, die Installation der notwendigen Software, den Anschluss Ihres Wallet und die ersten möglichen Optimierungen, um ihn weiterzuentwickeln.



Der Betrieb eines Bitcoin-Knotens ist nicht nur eine Option für Experten, er ist eine Notwendigkeit. Es ist ein Resilienz-Tool, das jeder Benutzer verstehen und implementieren muss. Dieser Kurs ist Ihr Startpunkt, um ein souveräner Bitcoiner zu werden!




+++




# Einführung


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Überblick über den Kurs


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Willkommen bei BTC 202, wo Sie lernen werden, wie Sie einen Bitcoin-Knoten einfach und unabhängig installieren, konfigurieren und benutzen können. Aber das ist noch nicht alles: Sie werden auch mehr über den Platz und die Funktion von Knoten im Bitcoin-System erfahren. Der Kurs wechselt zwischen theoretischen Erklärungen und angeleiteter praktischer Anwendung.



### Teil 1 - Einführung



In diesem ersten Teil des Kurses werden wir die grundlegenden Begriffe klären und dann zu genaueren Definitionen übergehen. Was ist ein Knoten? Was sind die Unterschiede zwischen Knoten, Wallet und Miner? Dann lernen Sie etwas über Bitcoin core und die Implementierungen des Protokolls. Das Ziel ist es, dieselbe Sprache zu sprechen, Verwirrung zu vermeiden und eine solide theoretische Grundlage zu schaffen.



### Teil 2 - Ein souveräner Bitcoiner werden



In diesem zweiten Teil werde ich zunächst erklären, warum es wichtig ist, einen eigenen Bitcoin-Knoten zu betreiben. Dann werden wir die verschiedenen Arten von Knoten (vollständig, pruned, SPV...), ihre Funktionsweise und ihre technischen Auswirkungen untersuchen.



Anschließend geben wir Ihnen einen Überblick über die Software, die für den Betrieb eines Bitcoin-Knotens zur Verfügung steht, einschließlich ihrer Vor- und Nachteile. Abschließend geben wir Ihnen einige sehr praktische Empfehlungen für die Auswahl der richtigen Hardware für Ihre Bedürfnisse und Ihr Budget.



Dieser Abschnitt veranschaulicht daher den Weg des souveränen Bitcoiners: Verstehen, warum es notwendig ist, einen Knoten zu betreiben, die Art des Knotens wählen, auf der Grundlage dieser Wahl die Software auswählen und, abhängig von der gewählten Software, die geeignete Hardware bestimmen.



### Teil 3 - Einfache Installation eines Bitcoin-Knotens



Sobald diese Vorbereitungen abgeschlossen sind, ist es an der Zeit, mit Teil 3, der Umbrel gewidmet ist, in die Praxis zu gehen: das Home-Cloud-Betriebssystem, das das Selbsthosten und die Installation eines Bitcoin- und Lightning-Knotens vereinfacht.



Nach einer kurzen Einführung in Umbrel bieten wir ein detailliertes Tutorial, das Sie durch den Installations- und Konfigurationsprozess auf Ihrem eigenen Heimwerker-Rechner führt. Das Ziel dieses Teils ist klar: Ihr werdet euren ersten voll funktionsfähigen und synchronisierten Bitcoin Knoten haben.



### Teil 4 - Anschließen Ihres Wallet an Ihren Knoten



Nachdem Sie nun einen Bitcoin-Knoten eingerichtet haben, ist es an der Zeit, ihn zu benutzen! In diesem Abschnitt erfahren Sie, wie Sie Ihre Wallet-Verwaltungssoftware (wie Sparrow wallet) mit Ihrem eigenen Address-Indexer (Electrs oder Fulcrum) oder direkt mit Bitcoin core verbinden können, damit Sie nicht mehr von öffentlichen Servern abhängig sind.



Wir werden auch die Rolle der Indexer und die verschiedenen Methoden der Verbindung zu Ihrem Knoten (LAN, Tor, Tailscale, etc.) untersuchen. Schließlich, im letzten Kapitel, werden wir die nützlichsten Anwendungen, die auf Umbrel für den alltäglichen Bitcoiner verfügbar sind, besprechen.



### Teil 5 - Fortgeschrittene Konzepte und bewährte Verfahren



In diesem letzten Teil von BTC 202 geht es darum, Ihr Wissen zu vertiefen. Zunächst befassen wir uns mit den besten Praktiken, die Sie bei Ihrem neuen Bitcoin-Knoten anwenden sollten, und mit der Frage, wie Sie ihn auf lange Sicht warten können.



Wir werden uns dann die Zeit nehmen, einige der zuvor im Kurs behandelten Theorien zu wiederholen, einschließlich des Verständnisses des IBD-Prozesses und der Peer-Erkennung im Detail, der Erforschung der Anatomie eines Knotens und schließlich der Verwendung der Datei "Bitcoin.conf" zur Feinabstimmung Ihrer Einstellungen.



### Teil 6 - Letzter Abschnitt



Wie bei allen Plan ₿ Network-Kursen finden Sie im letzten Abschnitt eine Abschlussprüfung, um Ihr Wissen über Bitcoin-Knoten zu testen.



Sind Sie also bereit, Ihren ersten Bitcoin-Knoten einzuschalten? Nehmen Sie Kurs auf Souveränität!



## Was ist ein Bitcoin-Knoten?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Wie von seinem Schöpfer, Satoshi Nakamoto, beschrieben, präsentiert sich Bitcoin als ein elektronisches Peer-to-Peer-Geldsystem. Dieser einfache Satz, der auch der Titel des Weißbuchs ist, enthält viele Hinweise auf das Wesen von Bitcoin:




- Zunächst einmal beschreibt Satoshi Bitcoin als ein "System", d. h. eine zusammenhängende Menge von Hardware- und Softwarekomponenten, die zusammenwirken, um einen bestimmten Dienst zu erbringen oder eine bestimmte Funktion auszuführen;
- Weiter erklärt er, dass dieses System die Verwendung von elektronischem Bargeld ermöglicht, d.h. eine Art immaterielle Währung;
- Schließlich weist er darauf hin, dass dieses System von keiner zentralen Stelle abhängt: Es ist ein "Peer-to-Peer"-System, d. h. die Nutzer selbst sind es, die das System betreiben.



Da Bitcoin ein System ist, muss es zwangsläufig auf Computern betrieben werden. Und da es sich um ein Peer-to-Peer-System handelt, sind die Benutzer selbst für den Betrieb dieser Computer verantwortlich. Was wir einen "Bitcoin-Knoten" nennen, ist genau der Computer, auf dem die Software läuft, die das Bitcoin-Protokoll implementiert (wie Bitcoin core, aber darauf kommen wir später zurück). Dadurch kann Bitcoin ohne eine zentrale Autorität funktionieren: Die Validierung wird auf verteilte Weise von Tausenden unabhängiger Maschinen durchgeführt, die Tausenden von Benutzern gehören.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: Ein Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Es sind genau diese Nutzer, die die Sicherheit von Bitcoin gewährleisten. Wie Eric Voskuil in seinem Buch *Cryptoeconomics* erklärt, beruht die Sicherheit von Bitcoin weder auf Blockchain, noch auf Hashing-Power, noch auf Validierung, Dezentralisierung, Kryptographie, Open Source oder Spieltheorie. Die Sicherheit von Bitcoin hängt in erster Linie von den Individuen ab, die bereit sind, sich einem persönlichen Risiko auszusetzen. Die Dezentralisierung ermöglicht es, dieses Risiko auf eine große Anzahl von Personen zu verteilen, und nur deren Fähigkeit, dem zu widerstehen, gewährleistet die Robustheit des Systems.



Dieses Prinzip ist leicht zu verstehen: Wenn Bitcoin von einem einzigen Knotenpunkt abhängt, der einer einzigen Person gehört, würde die Inhaftierung dieser Person ausreichen, um das Netz abzuschalten, da sie allein alle Risiken trägt. Bei Zehntausenden von Knotenpunkten, die über die ganze Welt verteilt sind, ist das Risiko breit gestreut: Jeder dieser Betreiber müsste neutralisiert werden, um Bitcoin auszuschalten.



![Image](assets/fr/048.webp)



Wir können also mehrere Begriffe unterscheiden und benennen, um die Dinge für den Rest des Kurses zu klären:




- Bitcoin-Währung: die für Transaktionen innerhalb dieses Systems verwendete Rechnungseinheit;
- Das Bitcoin-Netz: die Menge aller verbundenen Knotenpunkte;
- Bitcoin-Knoten: Rechner, auf denen eine Implementierung von Bitcoin läuft;
- Bitcoin-Implementierungen: Software, die das Protokoll in ausführbare Anweisungen umsetzt;
- Bitcoin-Protokoll: das Regelwerk, das den Betrieb des Systems regelt;
- Das Bitcoin-System: die kohärente Kombination all dieser Elements.



### Die Rolle des Bitcoin-Knotens



Die Bitcoin-Knoten bilden zusammen das so genannte Bitcoin-Netz. Sie ermöglichen dem gesamten System einen autonomen Betrieb, ohne Rückgriff auf eine zentrale Behörde oder eine Hierarchie von Servern.



Von Anfang an war Bitcoin so konzipiert, dass jeder Benutzer einen persönlichen Knoten betreiben konnte. Dies gilt auch für die heutige Bitcoin core-Software, die die Funktionen von Wallet und Knoten vereint. Heutzutage wird diese Funktion jedoch oft getrennt: Viele moderne Bitcoin-Geldbörsen sind nur Geldbörsen, die mit externen Knoten verbunden sind (die derselben Person gehören oder nicht).



### Blockchain beibehalten



Die erste Aufgabe eines Knotens besteht darin, eine lokale Kopie des Blockchain zu führen. Um Double-spending auf Bitcoin zu verhindern, ohne eine zentrale Behörde einzuschalten, muss jeder Benutzer prüfen, dass keine Transaktion im System existiert. Die einzige Möglichkeit, dies sicherzustellen, besteht darin, alle auf Bitcoin durchgeführten Transaktionen zu kennen. Aus diesem Grund werden alle Transaktionen mit einem Zeitstempel versehen und in Blöcken gruppiert, und jeder Knoten speichert den gesamten Blockchain.



> Die einzige Möglichkeit, das Nichtvorhandensein einer Transaktion zu bestätigen, besteht darin, sich aller Transaktionen bewusst zu sein.

Nakamoto, S. (2008). *Bitcoin: Ein Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Blockchain ist daher ein sich entwickelndes Register: Jedes Mal, wenn ein neuer Block von einem Miner veröffentlicht wird, prüft der Knoten dessen Gültigkeit, bevor er ihn zu seiner eigenen lokalen Kopie der Kette hinzufügt. Heute (Juli 2025) umfasst die gesamte Blockchain mehr als 675 GB, und diese Größe wächst weiter, da im Durchschnitt alle 10 Minuten ein neuer Block hinzugefügt wird.



![Image](assets/fr/049.webp)



Der Knotenpunkt unterhält auch eine lokale Aufzeichnung aller zu einem bestimmten Zeitpunkt vorhandenen UTXOs, die als **UTXO-Set** bezeichnet wird. Diese Datenbank enthält alle nicht verbrauchten Bitcoin-Fragmente. Wir werden dieses Thema im letzten Teil des Kurses noch einmal ausführlich behandeln.



### Überprüfen und Verteilen von Transaktionen



Die zweite Aufgabe eines Knotens besteht darin, die Überprüfung und Weiterleitung von Transaktionen sicherzustellen. Wenn eine neue Transaktion den Knoten erreicht (entweder über die Wallet-Software oder einen anderen Knoten), prüft er, ob sie mit einer Reihe von Regeln (Konsensregeln und Weiterleitungsregeln) übereinstimmt. Zum Beispiel:




- ausgegebene Bitcoins müssen in seinem UTXO-Set (der Datenbank der nicht ausgegebenen Ausgaben) vorhanden sein;
- die Unterschrift muss gültig sein, und alle Ausgabenbedingungen müssen erfüllt sein (gültiges Skript);
- der Gesamtbetrag der Outputs darf den Gesamtbetrag der Inputs nicht übersteigen, d. h. die Kosten dürfen nicht negativ sein.



![Image](assets/fr/050.webp)



Nach der Validierung wird die Transaktion im Mempool des Knotens gespeichert, einem temporären Speicherplatz, der für unbestätigte Transaktionen reserviert ist, und dann an die anderen Netzwerk-Peers weitergeleitet, mit denen er verbunden ist. Dieser Verteilungs- und Validierungsmechanismus setzt sich von Knoten zu Knoten fort. Auf diese Weise wird die Transaktion über das Bitcoin-Netz verbreitet, und jeder Knoten speichert sie im Mempool, bis sie von einem Miner in einen gültigen Block aufgenommen wird, der dann auf ihre erste Bestätigung hin handelt.



### Kontrolle und Verteilung der Blöcke



Die dritte Aufgabe des Knotens ist die Verwaltung der abgebauten Blöcke. Wenn ein Miner einen neuen Block mit einem gültigen Proof of Work entdeckt, wird er im Netz verbreitet. Die Knoten empfangen ihn, prüfen, ob er allen Protokollregeln entspricht, und integrieren ihn dann in ihre eigene lokale Kopie des Blockchain, wenn er gültig ist. Wie bei Transaktionen werden die neu validierten Blöcke dann an alle mit dem Knoten verbundenen Peers weitergeleitet. Dieser Prozess wird so lange fortgesetzt, bis alle Knoten im Bitcoin-Netz von dem neuen Block Kenntnis haben.



![Image](assets/fr/051.webp)



## Was ist der Unterschied zwischen einem Bogen und einem Wallet?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



Bei der Verwendung des Bitcoin ist es wichtig, zwischen zwei verschiedenen Arten von Software zu unterscheiden: dem Knoten und dem Wallet.



Ein Bitcoin-Knoten ist, wie bereits erwähnt, ein Stück Software, das aktiv am Peer-to-Peer-Netzwerk teilnimmt. Er führt drei Hauptaufgaben aus:




- sicherung des Blockchain,
- validierung und Weiterleitung von Transaktionen,
- blockvalidierung und Relais.



Ein Bitcoin Wallet hingegen ist eine Software, die dazu dient, Ihre privaten Schlüssel zu speichern und zu verwalten. Mit diesen Schlüsseln können Sie Ihre Bitcoins ausgeben, indem Sie die Sperrskripte erfüllen (in der Regel durch eine Signatur). Ein Wallet kann eine Verbindung zu einem (lokalen oder entfernten) Knoten herstellen, um den Status des Blockchain abzufragen und die von ihm erstellten Transaktionen zu übermitteln, aber er ist als solcher kein Teilnehmer des Netzwerks.



In einigen Fällen koexistieren diese beiden Funktionen innerhalb derselben Software, wie im Fall des Bitcoin core, der sowohl als Full node als auch als Wallet dient. Viele gängige Wallet-Programme (Sparrow, BlueWallet usw.) erfordern jedoch eine Verbindung zu einem externen Knoten (ob Ihr eigener oder der eines Drittanbieters), um Transaktionen zu übertragen und den Wallet-Saldo zu ermitteln.



![Image](assets/fr/052.webp)



## Was ist der Unterschied zwischen einem Knoten und einem Miner?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



Die Begriffe "Knoten" und "Miner" werden oft verwechselt. Doch diese beiden Elements erfüllen völlig unterschiedliche Funktionen innerhalb des Systems.



Als Bitcoin im Jahr 2009 von Satoshi Nakamoto ins Leben gerufen wurde, wurde von jedem Nutzer erwartet, dass er sich an dem Netzwerk als Ganzes beteiligt. Daher kombinierte die ursprüngliche Bitcoin-Software mehrere Funktionen auf einmal: Sie fungierte als Wallet, ein Knotenpunkt, und auch als Miner, der neue Blöcke erzeugen konnte. Zu dieser Zeit war der Schwierigkeitsgrad von Mining sehr gering. Alles, was Sie tun mussten, war, die Bitcoin-Software auf Ihrem Computer laufen zu lassen, um Blöcke zu finden und Bitcoins als Belohnung zu erhalten.



Mit der allmählichen Verbreitung von Bitcoin und dem Anstieg der Zahl der Bergleute hat sich die Wettbewerbslandschaft bei Mining jedoch radikal verändert. Heute ist Mining zu einer extrem wettbewerbsintensiven Aktivität geworden, die von industriellen Akteuren mit spezialisierten Infrastrukturen dominiert wird. Die zum Schürfen eines neuen Blocks erforderliche Leistung ist inzwischen so groß, dass es für einen einzelnen Nutzer praktisch unmöglich ist, dies nur mit einem herkömmlichen Computer zu erreichen. Infolgedessen wird Mining heute hauptsächlich von spezialisierten Maschinen, so genannten ASICs (*Application-Specific Integrated Circuits*), betrieben. Diese Chips sind ausschließlich für die Ausführung des doppelten SHA-256, des für Mining verwendeten Algorithmus, auf Bitcoin optimiert.



![Image](assets/fr/053.webp)



Angesichts dieser Entwicklung haben sich die Rollen des Bitcoin-Knotens und des Miner-Knotens deutlich voneinander unterschieden. Wie oben dargestellt, ist die Rolle eines Bitcoin-Knotens rein informativ und validierungsbasiert. Die Rolle des Miner ist eine andere:




- Sie wählt die ausstehenden Transaktionen in der Mempool aus.
- Er erstellt einen Kandidatenblock, der diese Transaktionen integriert.
- Er sucht durch Versuch und Irrtum nach einem gültigen Proof of Work.
- Findet er einen gültigen Beweis, sendet er den Block über seinen Knotenpunkt an die anderen Knotenpunkte.



Ein Miner benötigt einen Bitcoin-Knoten, um mit dem Netz zu interagieren.



Die Rolle des Miner wird manchmal auch von der des Zerhackers unterschieden. Ein Zerhacker ist eine Maschine, deren Aufgabe darin besteht, Hash Vorlagenblöcke, die vom Server eines Pools geliefert werden, nach Hashes zu durchsuchen, die dem für die Anteile definierten Schwierigkeitsziel entsprechen, und nicht dem von Bitcoin. Der Rest des Mining-Prozesses, der die eigentliche Blockkonstruktion, die Transaktionsauswahl oder die Proof-of-Work-Suche nach der Bitcoin-eigenen Schwierigkeit sowie die Verteilung umfasst, wird direkt von den Pools durchgeführt.



![Image](assets/fr/054.webp)



Schließlich gibt es einen wichtigen Unterschied in Bezug auf den wirtschaftlichen Anreiz zwischen dem Miner und dem Knoten. Der Betrieb eines Bitcoin-Knotens bringt keinen direkten finanziellen Vorteil. Auf der anderen Seite bringt die Teilnahme an Mining Belohnungen (Subventionen und Transaktionsgebühren) für jeden gefundenen Block.



In Teil 2 werden wir uns eingehender mit den praktischen und persönlichen Vorteilen der Installation und Nutzung eines Bitcoin-Knotens befassen, die über den rein finanziellen Aspekt hinausgehen.



## Bitcoin core und Protokollimplementierungen


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



Das Bitcoin-Protokoll ist keine Software, sondern ein Satz stillschweigender Regeln, die von den Netzbenutzern gemeinsam genutzt werden. Es definiert Bedingungen für die Gültigkeit von Transaktionen, Mechanismen zur Geldschöpfung, das Blockformat, Proof-of-Work-Bedingungen und viele andere Spezifikationen. Um mit diesem Protokoll zu interagieren, müssen die Benutzer eine Software ausführen, die diese Regeln implementiert: Dies wird als **Implementierung** von Bitcoin bezeichnet.



Eine Implementierung ist daher eine Knotensoftware: ein Programm, das in der Lage ist, eine Schnittstelle zu anderen Rechnern im Bitcoin-Netz herzustellen, Blöcke und Transaktionen herunterzuladen, zu verifizieren, zu speichern und weiterzuleiten sowie Konsens- und Weiterleitungsregeln lokal durchzusetzen. Jede Implementierung ist eine konkrete Interpretation des Protokolls, geschrieben in einer bestimmten Programmiersprache, mit eigener Architektur, Leistung und Ergonomie. Jede Implementierung hat auch ihre eigene Entwicklungsorganisation mit einer eigenen Aufteilung der Verantwortlichkeiten.



Unter diesen Implementierungen dominiert eine bei weitem: **Bitcoin core**.



![Image](assets/fr/055.webp)



### Eine historische Umsetzung, die zum Maßstab geworden ist



Bitcoin core ist die Referenzsoftware für das Bitcoin-Protokoll. Es ist von dem ursprünglichen Code abgeleitet, der von Satoshi Nakamoto 2008-2009 geschrieben wurde, und ist eine direkte Fortsetzung desselben. Ursprünglich bekannt als "*Bitcoin*", dann "*Bitcoin QT*" (aufgrund der Hinzufügung eines grafischen Interface über die Qt-Bibliothek), wurde es 2014 in "*Bitcoin core*" umbenannt, um die Software klar vom Netzwerk zu unterscheiden. Seit Version 0.5 wird es mit zwei Komponenten vertrieben: `Bitcoin-qt` (das grafische Interface) und `bitcoind` (das Kommandozeilen-Interface).



Theoretisch stellt Bitcoin core nicht das Bitcoin-Protokoll dar, sondern ist nur eine Implementierung unter vielen. Es zeichnet sich jedoch durch seine massive Verbreitung, sein Alter, die Robustheit seines Codes und die Strenge seines Entwicklungsprozesses aus. Folglich sind die von Bitcoin core angewandten Regeln in der Praxis de facto die des Bitcoin-Protokolls: Nutzer, Entwickler, Miner und Ökosystemdienste beziehen sich fast ausschließlich auf dieses Protokoll.



### Derzeitige Verteilung der Implementierungen



Nach [im August 2025 von Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (einem bekannten Entwickler im Ökosystem) gesammelten Daten ist die Verteilung der Implementierungen auf die öffentlichen Knoten des Netzwerks wie folgt:




- Bitcoin core**: 87.3% der Knotenpunkte
- Bitcoin Knots**: 12.5
- Andere kumulative Implementierungen**: 0.2% (btcsuite, Bcoin, BTCD...)



![Image](assets/fr/056.webp)



Mit anderen Worten: Etwa 9 von 10 öffentlichen Knoten laufen mit Bitcoin core. Der Rest des Netzes verlässt sich auf eher unbedeutende Clients (obwohl der Anteil von Knots in den letzten Monaten stark zugenommen hat, nicht zuletzt im Zuge der Debatten über die Größenbeschränkung von OP_RETURN). Diese alternativen Implementierungen werden oft von einer einzigen Person oder einem kleinen Team gepflegt.



**Anmerkung:** Bei diesen Zahlen handelt es sich jedoch noch um Schätzungen, da sie in erster Linie auf *hörenden Knoten* beruhen, d. h. auf Knoten, die eingehende Verbindungen annehmen (mit offenem Port 8333). Nicht-abhörende Knoten* sind viel komplexer zu zählen, da es unmöglich ist, sich direkt mit ihnen zu verbinden: Man muss darauf warten, dass die Initiative von ihnen ausgeht, in Form einer ausgehenden Verbindung. Die Website von Luke Dashjr behauptet, auch diese *nicht-hörenden Knoten* zu zählen, aber es ist nach wie vor unmöglich, genaue Daten über sie zu erhalten, und die Aktualisierung dieser Statistiken hinkt zwangsläufig der Realität hinterher.



### Interner Betrieb des Bitcoin core



Bitcoin core ist in C++ geschrieben. Es ist auch ein Open-Source-Projekt, das von einer Gemeinschaft von Entwicklern gepflegt wird, die sich freiwillig engagieren oder von verschiedenen Stellen bezahlt werden (oft von Unternehmen im Ökosystem, die ein persönliches Interesse an der Entwicklung von Core haben). [Der Code wird auf GitHub gehostet (https://github.com/Bitcoin/Bitcoin), und die Entwicklung erfolgt nach einem strengen Schema:




- Mitwirkende** reichen Vorschläge in Form von _Pull Requests_ (PR) ein. Im Prinzip kann jeder eine Änderung vorschlagen, aber sie muss getestet und dokumentiert werden und einen Peer-Review-Prozess durchlaufen.
- Die **Maintainer** haben das Recht, PRs zu genehmigen und zusammenzuführen. Sie sind diejenigen, die die Kohärenz und Stabilität des Projekts garantieren. Im Juli 2025 gibt es fünf von ihnen: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao und Ryan Ofsky.
- Seit Februar 2023 gibt es keinen **Hauptbetreuer** mehr. Diese Rolle hatte zunächst Satoshi Nakamoto beim Start von Bitcoin inne, dann Gavin Andresen nach Nakamotos Weggang Anfang 2011 und schließlich Wladimir J. Van Der Laan von 2014 bis 2023.



![Image](assets/fr/057.webp)



Die Entwicklung von Bitcoin core folgt einer meritokratischen Logik: Neue Mitwirkende werden ermutigt, den Code zu überprüfen und zu testen, bevor sie selbst Änderungen vorschlagen. Entscheidungen beruhen auf technischem Konsens, und größere Änderungen (insbesondere in Bereichen, in denen ein Konsens besteht) erfordern Diskussionen in öffentlichen Kanälen wie Mailinglisten oder PR Review Clubs.



### Andere Bitcoin-Implementierungen



Auch wenn die Verbreitung gering ist, gibt es andere Clients. Der wichtigste ist der von Luke Dashjr entwickelte Bitcoin Knots, ein Fork des Bitcoin core, der zusätzliche Optionen und einen konservativeren Ansatz bei der Entwicklung bietet. Dazu gehören strengere Beschränkungen für Transaktionsformate.



![Image](assets/fr/058.webp)



Wir können auch erwähnen:




- Libbitcoin**: eine modulare C++-Bibliothek, die von Amir Taaki entwickelt und von Eric Voskuil gepflegt wird;
- Bcoin**: eine JavaScript-Implementierung, die nicht mehr aktiv gepflegt wird;
- BTCD/btcsuit**e: eine Implementierung in Go.



Diese Projekte tragen zur Vielfalt des Ökosystems bei, aber ihre Akzeptanz ist nach wie vor sehr begrenzt, so dass es für Bitcoin core schwierig ist, sich unabhängig weiterzuentwickeln.



### Die Macht der Core-Entwickler



Man könnte meinen, dass die Entwickler von Bitcoin core direkte Kontrolle über Bitcoin haben, aber das ist nicht der Fall. Sie können keine Änderung des Protokolls erzwingen. Ihre Aufgabe ist es, Code vorzuschlagen. Es ist Sache jedes Benutzers, über seinen Knoten zu entscheiden, ob er diesen Code verwendet oder nicht.



Das bedeutet, dass eine Änderung in Bitcoin core, die nicht konsensfähig ist, von den Knotenpunkten ignoriert werden kann, indem entweder Bitcoin core nicht aktualisiert wird oder einfach die Implementierung geändert wird. Umgekehrt ist es, wenn eine von den Nutzern gewünschte Funktion im Kernentwicklungsprozess blockiert wird, immer möglich, zu einer anderen Implementierung oder Fork dem Projekt zu wechseln.



Wie wir später in diesem Kurs erörtern werden, sind es die Knotenpunkte (d. h. die Händler), die entsprechend ihrem wirtschaftlichen Gewicht einer Version des Protokolls (und damit der entsprechenden Währung) einen Nutzen verleihen, indem sie Einheiten akzeptieren, die dessen Regeln einhalten. Die wirkliche Macht über Bitcoin liegt also bei diesen Händlern, nicht bei den Entwicklern.




# Werden Sie ein souveräner Bitcoiner


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Warum den eigenen Knoten verdrehen?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



Es gibt eine weit verbreitete Überzeugung, dass der Betrieb eines Bitcoin-Knotens ein rein altruistischer Akt ohne persönlichen Gewinn ist, der ausschließlich im Dienste der Dezentralisierung des Netzwerks steht. Einige betrachten es als eine Art Pflicht für Bitcoiner, das System zu unterstützen und Bitcoin ihre Dankbarkeit zu zeigen.



Wie wir in den vorangegangenen Kapiteln dargelegt haben, bringt das Spinnen eines Knotens in der Tat keinen direkten finanziellen Gewinn. Man könnte also meinen, dass es kein persönliches Interesse daran gibt. Dennoch bringt der Betrieb eines eigenen Knotens viele individuelle Vorteile mit sich. Um Sie davon zu überzeugen, werde ich in diesem Kapitel alle technischen und strategischen Gründe darlegen, warum Sie Ihren eigenen Bitcoin-Knoten installieren und nutzen sollten.



### Vertraulichere Weitergabe von Transaktionen



Wenn die Wallet-Software eine Verbindung zu einem externen Knoten herstellt, überträgt sie ihre Transaktionen an eine Infrastruktur, die nicht unter Ihrer Kontrolle steht. Daraus ergeben sich offensichtliche Überwachungsrisiken: Der Betreiber des entfernten Knotens kann die Einzelheiten Ihrer Transaktionen, einschließlich der Beträge und Häufigkeit, analysieren und sie durch Abgleich bestimmter Metadaten (wie IP-Adressen, Zeiten und Orte) möglicherweise mit Ihrer Identität in Verbindung bringen.



Wie bereits in einem früheren Kapitel erwähnt, kommunizieren Wallets nicht auf magische Weise mit dem Bitcoin-Netzwerk; sie müssen sich mit einem Knotenpunkt verbinden, um Salden abzufragen oder Transaktionen zu übertragen. Wenn Sie nie einen eigenen Knotenpunkt eingerichtet haben, bedeutet dies, dass Ihr Wallet von der Infrastruktur eines Dritten abhängt (in der Regel das Unternehmen, das hinter der Software steht). Dieser Dritte, insbesondere wenn es sich um ein Unternehmen handelt, kann diese Daten beobachten, auswerten oder sogar weitergeben: sei es aus kommerziellen Gründen, aus rechtlichen Gründen oder aufgrund von Piraterie.



![Image](assets/fr/059.webp)



Indem Sie Ihren eigenen Knotenpunkt verwenden, übermitteln Sie Ihre Transaktionen direkt an das Netz und umgehen so die Zwischenhändler. Unter der Voraussetzung, dass Sie Ihren Knoten ordnungsgemäß absichern (worauf wir später noch eingehen werden) oder bestimmte Standards einhalten, werden keine Informationen preisgegeben: Weder Ihre IP Address noch die Details Ihrer Transaktionen laufen durch eine Einheit, die Sie nicht kontrollieren. Dies ist eine Grundvoraussetzung für die Wahrung Ihrer Vertraulichkeit auf Bitcoin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Nicht zensierbare Transaktionen



Aus denselben Gründen wie oben erwähnt ist Wallet-Software, die auf einem Knotenpunkt eines Drittanbieters basiert, anfällig für Zensurrisiken: Der Betreiber des entfernten Knotens kann sich aus verschiedenen Gründen weigern, bestimmte Transaktionen weiterzuleiten. Er kann sie für verdächtig halten oder für unvereinbar mit seiner Politik. Die Transaktion kann auch blockiert werden, wenn sie nicht mit den Weiterleitungsregeln des Knotens übereinstimmt. Schließlich kann der Betreiber gezielt Ihre IP Address anvisieren, um die Übertragung Ihrer Transaktionen zu blockieren.



Umgekehrt sorgen Sie mit Ihrem eigenen Knoten für die Verbreitung Ihrer Transaktionen innerhalb des Peer-to-Peer-Netzwerks. Das bedeutet, dass Sie die volle Kontrolle über die Verbreitung Ihrer Transaktionen behalten, ohne von einem Vermittler abhängig zu sein. Solange die Transaktion mit den Konsens- und Relay-Regeln der mit Ihnen verbundenen Knoten übereinstimmt, wird sie im Netzwerk verbreitet und dann, sofern genügend Gebühren enthalten sind, von einem Miner in einen Block integriert. Ein eigener Knoten garantiert eine neutrale, genehmigungsfreie Bestätigung Ihrer Transaktionen.



### Unabhängige Datenüberprüfung



Ohne einen persönlichen Knotenpunkt sind Sie für den Zugriff auf Informationen wie Ihren Address-Saldo, den Status der Transaktionsbestätigung und die Gültigkeit von Blöcken weiterhin von einer dritten Partei abhängig. Dies setzt ein implizites Vertrauen in die Genauigkeit und Integrität des externen Knotens voraus.



![Image](assets/fr/060.webp)



Wenn Sie einen Full node betreiben, können Sie alle Protokollregeln für jede Transaktion und jeden Block selbst überprüfen. Folglich ist der von Ihrem Wallet angezeigte Saldo nicht die von einem entfernten Server empfangenen Daten, sondern ein lokal aus einer vollständigen Kopie des Blockchain berechnetes Ergebnis, das Block für Block validiert wurde. Dieser Ansatz gibt der Maxime der Bitcoiners volle Bedeutung:



> Vertrauen Sie nicht, überprüfen Sie.

### Bessere Verteilung der Systemsicherheit



Jeder Knoten, der sich dem Netz anschließt, verstärkt die Redundanz und Ausfallsicherheit von Bitcoin. Er erleichtert die Verbreitung von Informationen und ermöglicht es neuen Peers, sich miteinander zu verbinden. Ohne die Knoten wäre das System einfach nicht funktionsfähig.



Wie wir gesehen haben, basiert die Sicherheit von Bitcoin nicht auf Dezentralisierung, Mining oder Kryptographie: Wie bei jedem System hängt sie von Einzelpersonen ab. Genauer gesagt, hängt es von der Fähigkeit der Knotenbetreiber ab, sich dem Zwang zu widersetzen.



Das Besondere an dezentralen Systemen wie Bitcoin ist die Verteilung des Risikos auf alle am Betrieb Beteiligten. Wenn Sie Ihren eigenen Bitcoin-Knoten betreiben, übernehmen Sie einen Teil dieses Risikos, indem Sie für die Sicherheit Ihrer Instanz sorgen; dadurch verringern Sie auch die Risikobelastung für andere Knotenbetreiber.



Es handelt sich also nicht um einen direkten persönlichen Vorteil: Als Betreiber eines Knotens ist man mitverantwortlich für die Sicherheit des Netzes. Es ist vor allem ein kollektiver Nutzen, weil Ihre Beteiligung dazu beiträgt, das Risiko zu verteilen. Im Gegenzug erhöhen Sie Ihre eigene Fähigkeit, Bitcoin zuverlässig zu nutzen.



### Vertiefen Sie Ihr Verständnis für das System



Die Installation eines Full node ist kein trivialer Vorgang. Sie umfasst die Installation der Software, das Verständnis der grundlegenden Funktionsweise, die Überwachung der Synchronisation, die Untersuchung der Protokolle bei Problemen und sogar die Verwendung des Terminals. Dies führt zwangsläufig dazu, dass Sie Ihr Verständnis des Protokolls vertiefen. Dies ist ein indirekter, aber nicht unbedeutender Vorteil.



Die Aneignung dieses Wissens stärkt Ihr Vertrauen in das Werkzeug und kann das Risiko von Fehlern oder Betrug verringern. Auch das Spinnen eines eigenen Knotens ist eine Form des Lernens.



### Auswahl der anzuwendenden Regeln



Ein wichtiger Aspekt, der oft missverstanden wird, ist die Tatsache, dass der Betrieb eines Knotens es Ihnen ermöglicht, die Regeln zu wählen, die Sie lokal anwenden. Es gibt zwei Haupttypen von Regeln:





- Konsensregeln**:



Dies sind die Grundregeln des Bitcoin-Protokolls, die die Integrität des Systems gewährleisten und die Kriterien für die Validierung von Transaktionen und Blöcken festlegen. Jede Transaktion, die diesen Konsensregeln nicht entspricht, kann niemals in einen gültigen Block aufgenommen werden. So wird zum Beispiel eine Transaktion mit einer ungültigen Signatur auf einem ihrer Einträge systematisch ausgeschlossen.



Eine Änderung dieser Regeln ist gleichbedeutend mit einer Änderung des Protokolls und damit der Währung (Hard Fork). Aber auch ohne den Versuch, sie zu ändern, verleiht die einfache Tatsache der strikten Anwendung der bestehenden Regeln eine gewisse Macht: Wenn ein Block gegen die Regeln verstößt, lehnt der Knoten ihn sofort ab.





- Staffelregeln**:



Dabei handelt es sich um Regeln, die für jeden Bitcoin-Knoten spezifisch sind und zu den Konsensregeln hinzugefügt werden, um die Struktur der unbestätigten Transaktionen zu definieren, die im Mempool akzeptiert und an die Peers weitergegeben werden. Jeder Knoten konfiguriert und wendet diese Regeln lokal an, weshalb sie sich von einem Knoten zum anderen unterscheiden können. Sie gelten nur für unbestätigte Transaktionen: Eine Transaktion, die von einem Knoten als "nicht standardmäßig" eingestuft wird, wird nur akzeptiert, wenn sie bereits in einem gültigen Block enthalten ist. Eine Änderung dieser Regeln führt nicht zum Ausschluss des Knotens aus dem Bitcoin-System.



Zum Beispiel ist eine Transaktion ohne Gebühren nach den Konsensregeln vollkommen gültig, wird aber nach der Bitcoin core-Relay-Policy standardmäßig abgelehnt, da der Parameter "minRelayTxFee" auf "0,00001" (in BTC/kB) gesetzt ist. Es ist jedoch möglich, diesen Schwellenwert auf Ihrem eigenen Knoten zu senken, um Transaktionen mit niedrigeren Gebühren weiterzuleiten, oder umgekehrt den Grenzwert z. B. auf 2 Sats/vB zu erhöhen, um die Weiterleitung von Transaktionen mit niedrigen Gebühren zu vermeiden.



Seinen eigenen Knoten zu spinnen bedeutet zu behaupten: "Ich validiere, was ich für gültig halte, nach den Regeln, die ich selbst festgelegt habe "*. Auf diese Weise werden Sie zu einem Akteur in der Steuerung des Systems, der in der Lage ist, eine Entwicklung abzulehnen, die Ihnen inakzeptabel erscheint, oder eine Aktualisierung nach Ihren eigenen Kriterien zu genehmigen.



Wir können also schnell versuchen zu verstehen, wie viel Macht Sie dank Ihres Knotens über die Regeln haben. Und das Ausmaß dieser Macht hängt von der Art der Regel ab.



#### Für Relaisregeln



Was die Weiterleitungsregeln betrifft, so ist der Besitz eines Knotens, unabhängig von seiner wirtschaftlichen Tätigkeit, das Wesentliche. Hier geht es darum, ob Sie zustimmen, bestimmte Arten von Transaktionen weiterzuleiten oder nicht.



Wenn Sie beispielsweise der Meinung sind, dass Transaktionen mit Gebühren von weniger als 1 sat/vB auf Bitcoin akzeptiert werden sollten, können Sie diese Regel auf Ihrem Knoten so anpassen, dass er diese Transaktionen sendet und so ihre Verbreitung im Netz erleichtert, bis ein Miner sie schließlich in einen gültigen Block aufnimmt. Im Wesentlichen geht es also um die Macht über die Verbreitung von Transaktionen: Jeder Knoten hat die Entscheidungsgewalt, da die Zustimmung zur Weiterleitung einer Transaktionsart gleichbedeutend ist mit der Förderung ihrer Akzeptanz im Bitcoin-Netzwerk. Wenn Sie mehrere Knotenpunkte betreiben, haben Sie folglich einen größeren Einfluss auf die Weiterleitungspolitik, da jeder Knotenpunkt seine eigenen Verbindungen und Einflussbereiche im Netz hat.



Wenn ein oder mehrere Knoten mit spezifischen Weiterleitungsregeln konfiguriert sind, bedeutet dies, dass festgelegt wird, welcher Teil des Netzes die Weiterleitung einer bestimmten Art von Transaktion akzeptiert. Die Verbreitung einer Nachricht in einem Peer-to-Peer-Graphen, wie es bei Bitcoin-Transaktionen der Fall ist, folgt der Logik der Perkolationstheorie. Stellen Sie sich jeden Knoten als einen Standort vor, der aktiv (`p` = er leitet weiter) oder inaktiv (`1-p`) sein kann. Sobald der Anteil `p` einen kritischen Schwellenwert (`p_c`) überschreitet, entsteht eine riesige Komponente: Die Transaktion schafft es, das Netzwerk zu durchqueren und hat alle Chancen, einen Miner zu erreichen. In einem Netz wie Bitcoin, in dem jeder Knoten durchschnittlich 8 ausgehende Verbindungen unterhält, wird der `p_c`-Schwellenwert im Allgemeinen auf wenige Prozent festgelegt, sogar noch niedriger, wenn einige Knoten eine sehr große Anzahl von Verbindungen haben.



![Image](assets/fr/061.webp)



Solange `p` unter `p_c` bleibt, bleibt eine Transaktion auf isolierte Taschen beschränkt und erreicht kein Miner. Sobald dieser Schwellenwert überschritten wird, breitet sie sich fast augenblicklich über das gesamte Netz aus.



Letztendlich sind es immer die Miner, die entscheiden, ob eine Transaktion in einen Block aufgenommen wird oder nicht. Die Knotenpunkte greifen jedoch im Vorfeld ein, indem sie die Verteilung der Transaktionen beeinflussen: Sie bestimmen, ob die Miner von einer bestimmten Transaktion Kenntnis erhalten oder nicht. Wenn eine Transaktion nicht an die Miner weitergeleitet wird, ist es für diese natürlich unmöglich, sie in einen Block aufzunehmen.



Das Hinzufügen einiger weiterer Knoten hat daher nur eine marginale Auswirkung, wenn sich das Netzwerk bereits in der Perkolationsphase für eine bestimmte Art von Transaktion befindet, kann sich aber als entscheidend erweisen, wenn sich die Perkolationsschwelle nähert. Der Besitz oder die Beeinflussung mehrerer Knoten, insbesondere wenn sie gut vernetzt sind, kann den Wert von "p" erhöhen oder verringern und damit indirekt die Weiterleitungsregeln steuern, die bestimmen, welche Transaktionen von den Minern gesehen und schließlich akzeptiert werden.



#### Für Konsensregeln



Wenn es um den Einfluss Ihres Knotens auf die Konsensregeln geht, ist vor allem sein wirtschaftliches Gewicht entscheidend. Dies ist ein entscheidendes Konzept: Der Wert einer Währung steht in direktem Zusammenhang mit ihrer Fähigkeit, Exchange zu erleichtern. Wenn ein Gegenstand von niemandem in Exchange für Waren oder Dienstleistungen akzeptiert wird, hat er theoretisch keinen monetären Nutzen. Wenn zum Beispiel kein Händler Kieselsteine als Zahlungsmittel akzeptiert, haben sie keinen Nutzen als Geld. Natürlich bleibt der Nutzen auf individueller Ebene ein subjektiver Begriff, aber in einem bestimmten Gebiet ist es umso wahrscheinlicher, dass dieses Objekt für die in diesem Gebiet lebenden Menschen einen monetären Nutzen hat, je mehr Händler ein Objekt als Zahlungsmittel in Exchange akzeptieren.



Nehmen wir das Beispiel eines Dorfes, in dem viele Händler Gold in Exchange für Waren akzeptieren: Die Chancen stehen gut, dass Gold einen monetären Nutzen für die Dorfbewohner hat. Dies zeigt, dass der Nutzen einer Währung direkt von der Entscheidung der Händler abhängt, sie zu akzeptieren oder abzulehnen.



Dieses Konzept ist entscheidend für das Verständnis der Machtdynamik, die im Bitcoin-System im Spiel ist. Satoshi macht es deutlich: Bitcoin ist ein elektronisches Bargeldsystem; mit anderen Worten, es bietet einen Dienst an, der eine Form von Währung, Bitcoin (oder BTC), anbietet. Wenn die Protokollregeln in einer Weise geändert werden, die nicht rückwärtskompatibel ist (Hard Fork), kommt dies der Schaffung eines neuen Systems und damit einer neuen Währung gleich. Der Erfolg oder Misserfolg dieses Fork hängt dann von der Größe seiner Wirtschaft ab, die wiederum von der Anzahl der Händler bestimmt wird, die diese neue Form der Währung akzeptieren.



![Image](assets/fr/062.webp)



Nehmen wir ein Beispiel: Nehmen wir an, Bitcoin erleidet einen Hard Fork. Dann gäbe es 2 verschiedene Arten von Währungen: BTC-1 (die ursprüngliche, unveränderte Version) und BTC-2 (die neue Währung mit anderen Konsensregeln). Wenn alle Händler, die BTC-1 akzeptiert haben, dies auch weiterhin tun, aber BTC-2 ablehnen, dann wird letztere theoretisch nur einen sehr begrenzten monetären Nutzen haben. Als Nutzer hätte ich kein Interesse daran, BTC-2 zu behalten und zu verwenden, da ich weiß, dass kein Händler es in Exchange für Waren oder Dienstleistungen haben möchte. Wenn sich umgekehrt 50 % der Händler dafür entscheiden, ausschließlich BTC-2 zu akzeptieren, und die restlichen 50 % nur BTC-1 annehmen, dann hat sich der Nutzen von BTC-1 theoretisch halbiert. Ich verwende den Begriff "theoretisch", weil der Nutzen auf individueller Ebene subjektiv bleibt und von einer Vielzahl von Faktoren abhängt (z. B. Gebiet und Konsumgewohnheiten), die im Einzelfall schwer zu erfassen sind.



Auf Bitcoin umfasst die Rolle des "Händlers", verstanden als jede Einheit mit einem gewissen wirtschaftlichen Gewicht, natürlich Unternehmen (physische Geschäfte, Online-Verkaufsseiten, Dienstleister usw.), aber auch Exchange-Plattformen, da sie Bitcoin in Exchange für andere Währungen akzeptieren, und Miner, da sie Bitcoin über Gebühren in Exchange für die Dienstleistung der Aufnahme einer Transaktion in einen Block akzeptieren.



Was die Konsensregeln anbelangt, so können Sie mit Ihrem Knotenpunkt Ihre Wirtschaftstätigkeit auf die eine oder andere Währung ausrichten. Wenn Sie beispielsweise 10 volle Knoten zu Hause haben, aber keine nennenswerten wirtschaftlichen Aktivitäten entfalten, wird Ihr Einfluss während eines Fork fast gleich Null sein. Umgekehrt verleiht ein einziger Knoten, der zur Verwaltung einer Kette von 200 Geschäften verwendet wird, die Bitcoin akzeptieren, ein erhebliches wirtschaftliches Gewicht.



Es kommt also nicht auf die Anzahl der Knotenpunkte an, sondern auf die Bedeutung der von ihnen unterstützten Wirtschaftstätigkeit. Mehr noch: Wenn Ihre wirtschaftliche Aktivität von einem Knoten abhängt, den Sie nicht kontrollieren, entscheidet dessen Eigentümer, welche Währung Sie verwenden, solange Sie mit diesem Knoten verbunden bleiben. Aus diesem Grund ist der Betrieb und die Nutzung eines eigenen Knotens im Rahmen der Systemsteuerung besonders wichtig:



> Nicht dein Knoten, nicht deine Regeln.


## Die verschiedenen Typen von Bitcoin-Knoten


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



Ein Bitcoin-Knoten ist also ein Rechner, auf dem eine Implementierung des Bitcoin-Protokolls läuft. Hinter dieser allgemeinen Definition von Knoten verbergen sich mehrere mögliche Konfigurationen, die nicht alle das gleiche Maß an Autonomie, Ressourcenverbrauch und Nutzen für das Netzwerk bieten. In diesem Kapitel werden wir versuchen, diese Unterschiede zu verstehen, um Ihnen zu helfen, eine Knotenarchitektur zu wählen, die Ihren Anforderungen und Hardwarebeschränkungen entspricht.



### Der vollständige Knoten



Ein Full node ist einfach ein Bitcoin-Knoten, der das gesamte Blockchain aus dem Genesis-Block herunterlädt, jeden Block unabhängig validiert und die Historie des gesamten Blockchain lokal speichert. Dies ist die "normale" Form eines Bitcoin-Knotens, wie sie sich Satoshi Nakamoto vorgestellt hat.



![Image](assets/fr/063.webp)



Der Full node braucht niemandem zu vertrauen, da er alle Informationen im System validiert und kennt. Er ist die Art von Knotenpunkt, die Ihnen die meisten Garantien bietet: Sie wissen, ohne sich auf einen Dritten zu verlassen, ob eine Zahlung gültig ist, ob ein Block gültig ist, ob eine Umstrukturierung rechtmäßig ist und so weiter.



In der Praxis benötigt ein Full node nicht unerhebliche Ressourcen, darunter mehrere hundert Gigabyte für Blockdateien, einen Prozessor, der in der Lage ist, Skripte zu validieren, Arbeitsspeicher für den Mempool und Caches sowie eine stabile Bandbreite. Bei der ersten Synchronisierung (*IBD*) wird die gesamte Historie gelesen und überprüft: Das ist intensiv, geschieht aber nur einmal. Ein Full node nimmt aktiv am Netz teil, leitet Blöcke und Transaktionen weiter und kann eingehende Verbindungen annehmen, um andere Peers zu unterstützen.



Je nach Bedarf können Sie einen Indexer zu Ihrem Full node hinzufügen. Der Bitcoin core bietet die Indexierung von Transaktionen als optionale Funktion (standardmäßig deaktiviert), die für bestimmte Zwecke nützlich sein kann. Allerdings ist kein Address-Indexer enthalten, der von einzelnen Benutzern oft am meisten nachgefragt wird. Um hier Abhilfe zu schaffen, können Sie eine spezielle Software auf Ihrem Knoten installieren, z. B. Electrs oder Fulcrum, um Abfragen zur Überprüfung des Address-Saldos von verbundenen UTXOs zu beschleunigen. Auf die Rolle des Indexers werden wir in einem separaten Kapitel noch einmal genauer eingehen.



### Der pruned-Knoten



Der pruned-Knoten validiert alles wie ein Full node, vom Genesis-Block bis zum Kopf der Kette mit der meisten Arbeit, behält aber **nur den jüngsten Teil der Blockdateien**. Sobald die alten Blöcke überprüft worden sind, werden sie nach und nach gelöscht, um unter einer von Ihnen festgelegten Speicherplatzgrenze zu bleiben. Diese Konfiguration ist ideal, wenn Sie nur begrenzten Speicherplatz zur Verfügung haben: Sie behalten die Unabhängigkeit der Blocküberprüfung, ohne das komplette Blockchain-Archiv zu speichern. Diese Option ist besonders nützlich, wenn Sie Bitcoin core einfach auf Ihrem PC installieren möchten, ohne einen speziellen Rechner zu verwenden.



![Image](assets/fr/064.webp)



Die technischen Implikationen dieser Option sind recht einfach: Der pruned-Knoten ist durchaus in der Lage, Ihre Transaktionen zu übertragen, am Relay teilzunehmen, Blöcke und Transaktionen zu verifizieren und die Kette zu verfolgen. Andererseits kann er nicht als Quelle historischer Daten über seine Grenzen hinaus für andere Anwendungen (z. B. Full Explorers, Indexers, Wallets) dienen. Funktionen, die das Archiv (oder einen globalen Index) benötigen, werden daher nicht verfügbar sein.



In der Praxis können Sie einen pruned-Knoten verwenden, um Wallet-Verwaltungssoftware wie Sparrow wallet anzuschließen. Sie werden jedoch nicht in der Lage sein, Transaktionen auf Ihrem Wallet zu scannen, die vor der Bereinigungsgrenze liegen. Wenn Sie beispielsweise eine Transaktion im Block 901 458 registriert haben, Ihr Knoten aber nur Blöcke ab 905 402 aufwärts speichert (weil die ältesten Blöcke pruned waren), können Sie diese Transaktion nicht scannen. Hätten Sie sie hingegen bereits gescannt, als Ihr Knoten noch diese Blockhöhe hatte, dann würde Ihre Wallet-Verwaltungssoftware die Informationen speichern und den Saldo der entsprechenden UTXOs korrekt anzeigen.



Kurz gesagt, die Wallet-Verfolgung funktioniert problemlos auf einem pruned-Knoten, wenn Sie einen neuen Wallet erstellen, während Ihre Software bereits mit diesem Knoten verbunden ist. Andererseits können Sie auf Schwierigkeiten stoßen, wenn Sie einen alten Wallet wiederherstellen, da vergangene Transaktionen, die nicht mehr vom Knoten aufbewahrt werden, offensichtlich nicht abrufbar sind.



### Der leichte Knoten / SPV



Ein SPV-Knoten (*Simplified Payment Verification*) oder leichtgewichtiger Knoten speichert nur Block-Header, keine Transaktionsdetails, und verlässt sich auf andere vollständige Knoten, um den Beweis zu erhalten, dass eine Transaktion in einem Block ist (Merkle-Beweise über Bäume), für den er den Header hat. Das Konzept der vereinfachten Zahlungsüberprüfung ist nicht neu und wurde von Satoshi Nakamoto selbst in Teil 8 des Weißbuchs vorgeschlagen.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: Ein Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Diese Art von Knoten ist in Bezug auf Speicherplatz und CPU-Nutzung natürlich viel leichter als ein Full node- oder sogar ein pruned-Knoten. Der SPV-Knoten ist daher gut für kleinere Geräte und intermittierende Verbindungen geeignet. In der Tat wird er oft direkt in den Wallet integriert, insbesondere in mobile Software wie die Blockstream App.



Der Nachteil ist das Vertrauen und die Vertraulichkeit: Ein SPV-Client prüft nicht selbst Skripte oder Validierungsrichtlinien; er geht davon aus, dass die Kette mit der meisten Arbeit gültig ist, und ist für Antworten auf einen oder mehrere vollständige Knoten angewiesen. Die Verwendung eines solchen Knotens ist daher eine bessere Option als die Verbindung mit einem Knoten eines Drittanbieters; sie ist jedoch immer noch weniger vorteilhaft als ein Full node- oder sogar ein pruned-Knoten.



![Image](assets/fr/065.webp)



### Welcher Knotenpunkt für welchen Bedarf?





- Mobile / Einsteiger Benutzer



Für einen unerfahrenen Benutzer, der nur einen Wallet auf einer mobilen App hat, ist die Verwendung eines SPV-Knotens sicherlich der beste Weg, um loszulegen. Die Installation ist schnell, erfordert nur wenige Ressourcen, und die Erfahrung ist einfach und flüssig. Das bedeutet, dass Sie bestimmte Informationen selbst verifizieren können und daher weniger auf Knotenpunkte von Drittanbietern angewiesen sind, während Sie gleichzeitig unabhängiger sind, wenn es um die Übertragung von Transaktionen geht.





- PC / fortgeschrittener Benutzer



Ein mittlerer Benutzer mit einem PC kann einen pruned-Knoten installieren, um von fast allen Vorteilen eines Full node zu profitieren, ohne seinen Rechner täglich zu überlasten: vollständige Validierung, moderate Festplattennutzung und einfache Wartung. Es ist eine ideale Lösung, um Ihre Desktop-Wallets zu verbinden und bei der Verteilung Ihrer Transaktionen unabhängig zu bleiben, ohne in eine dedizierte Maschine zu investieren oder Ihren Speicherplatz zu überlasten.





- Souveräner Bitcoiner / Fortgeschrittener



Ein Full node ist nach wie vor die beste Lösung, wenn Sie bei der Nutzung des Bitcoin völlig unabhängig sein und sich später nicht auf fortgeschrittene Anwendungen wie einen Indexer, einen Lightning-Knoten oder sogar einen Block explorer beschränken wollen. Das ist genau das, was wir in diesem Kurs erforschen werden!



## Überblick über die Softwarelösungen


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



Auf der Softwareseite gibt es 2 Hauptmöglichkeiten, einen Bitcoin-Knoten zu betreiben:




- direkt eine Protokollimplementierung wie Bitcoin core (empfohlen) oder Bitcoin Knots installieren,
- oder verwenden Sie eine schlüsselfertige Distribution (oft "_node-in-a-box_" genannt), die eine Bitcoin-Implementierung auf die gleiche Weise integriert, aber auch ein Interface-Verwaltungssystem, einen Anwendungsspeicher und gebrauchsfertige Tools enthält (Lightning, Browser, Indexserver, sogar selbst gehostete Anwendungen außerhalb von Bitcoin...).



Beide Ansätze führen zum gleichen Ziel: einen eigenen Knoten zu haben, aber sie unterscheiden sich in Bezug auf die Interface-Installation und -Nutzung, die Wartung, die Erweiterbarkeit und die Kosten. Das werden wir in diesem Kapitel untersuchen.



### Rohe Bitcoin-Knoten-Implementierungen



Die Installation einer Rohimplementierung bedeutet die direkte Verwendung der Software einer Bitcoin-Protokollimplementierung (wie Core), ohne zusätzliche Software Layer. Sie verwalten die Konfiguration, die Aktualisierungen und die zugehörigen Dienste (Indizierung, API, Lightning, Backups usw.) selbst, je nach Ihren Bedürfnissen.



Das ist der souveränste und flexibelste Ansatz: Sie wissen genau, was läuft, wo die Daten sind und wie alles funktioniert. Auf der anderen Seite wird es komplexer, sobald man über den einfachen Betrieb eines Bitcoin-Knotens hinausgehen will. Wenn es nur darum geht, einen Knoten zu haben, ist die Komplexität vergleichbar mit der eines Node-in-a-Box, oder sogar geringer, da es nur darum geht, Software zu installieren.



#### Bitcoin core (Ultra-Mehrheitskunde)



[Bitcoin core ist der Client des Netzes, der die größte Mehrheit hat (https://bitcoincore.org/). Er lädt den Blockchain herunter, validiert und pflegt ihn, bietet RPC/REST-APIs und kann einen Wallet integrieren. Wenn Sie Standardtools bevorzugen und sich damit wohl fühlen, selbst Dienste hinzuzufügen (wie Electrum-Server, Explorer und LND), sind Sie mit Core besser bedient.



**Vorteile:** Maximale Stabilität, vorhersehbares Verhalten, einfache Erfahrung, einfache Installation und Konfiguration.



**Nachteile:** Sie müssen den Rest des Stacks manuell erstellen, um eine vollständige Anwendungsumgebung zu schaffen, und nicht nur einen Bitcoin-Knoten.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (alternativer Hauptkunde)



[Bitcoin Knots ist ein Fork von Bitcoin core] (https://bitcoinknots.org/), gepflegt von Luke Dashjr. Es ist der wichtigste alternative Client zu Core für die Implementierung des Bitcoin-Protokolls. Er ist vollständig kompatibel mit dem Rest des Netzes (er ist keineswegs ein Hard Fork wie Bitcoin Cash), bietet jedoch zusätzliche Funktionen, einschließlich Optionen für die Weiterleitungspolitik, die in Core fehlen oder standardmäßig strenger angewendet werden, um das zu begrenzen, was manche als Spam ansehen.



Es gibt 2 mögliche Gründe für die Wahl von Knoten statt Kern:




- Techniken**: Unterschiedliche Optionen gegenüber Core, insbesondere in Bezug auf die Relaisverwaltung, indem festgelegt wird, welche Transaktionen von Ihrem Knoten akzeptiert und verbreitet werden.
- Politik**: Einige Leute ziehen es vor, alternative Clients wie Knots aus nicht-technischen Gründen zu verwenden, vor allem um eine Alternative zu Core zu unterstützen und so dessen Monopol zu verringern. Sollte Core jemals kompromittiert werden, wäre es nicht nur nützlich, solide, gut gewartete alternative Clients zu haben, sondern auch zu wissen, wie man sie effektiv einsetzt. Andere nutzen Knots aus Protest, weil sie das Vertrauen in die Core-Entwickler verloren haben oder mit der Mehrheit des Client-Managements nicht einverstanden sind.


https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Ich persönlich empfehle Ihnen, sich für Core zu entscheiden, vor allem um schneller von Sicherheits-Patches zu profitieren. In der Tat werden einige in Knots entdeckte Schwachstellen mit Verzögerung behoben. Ganz allgemein ist der Entwicklungsprozess von Core solide strukturiert und wird von einer großen Zahl von Mitwirkenden unterstützt, während Knots von einer einzigen Person gepflegt wird und eine viel kleinere Gemeinschaft hat. Andererseits verlieren Relay-Regeln heute tendenziell ihre Nützlichkeit, insbesondere wenn sie nur von einem winzigen Teil des Netzwerks angewendet werden (wie bei der Perkolationstheorie).



### Node-in-a-box-Verteilungen



Die _node-in-a-box_ kombiniert Bitcoin core (oder Knots) mit einem vorkonfigurierten Betriebssystem, einem Interface Web und einem App-Store für selbst gehostete Dienste (Lightning, explorers, Electrum Server, Mempool, BTCPay Server, Nextcloud usw.). Mit nur einem Klick können Sie diese verschiedenen Module installieren, aktualisieren und miteinander verbinden.



Es ist eine viel einfachere Lösung für das Starten und Verwalten zahlreicher zusätzlicher Anwendungen im Alltag. Der Nachteil ist, dass im Falle eines Problems (z. B. Docker-Image-Konflikt, fehlerhaftes Update, beschädigte Datenbank) die Fehlersuche sehr komplex werden kann, da man von der Integration der Distribution selbst abhängig ist. Außerdem ist der Community- oder offizielle Support oft kompliziert.



Ein Node-in-a-Box ist also extrem einfach zu bedienen, solange alles richtig funktioniert, aber im Falle eines Fehlers muss man bereit sein, lange zu suchen, auf Hilfe zu warten und sich die Hände schmutzig zu machen.



Die meisten dieser Lösungen sind in zwei Formaten erhältlich:




- Vormontierter Rechner: ein kompletter Computer mit bereits installiertem Betriebssystem. Diese Pay-as-you-go-Rechner müssen lediglich an das Stromnetz angeschlossen und mit dem Internet verbunden werden, um betriebsbereit zu sein. Wenn Ihr Budget es zulässt, hat diese Option den Vorteil, dass sie sehr einfach einzurichten ist, oft vorrangigen Support bietet und zur Finanzierung der Entwicklung beiträgt, da das Geschäftsmodell dieser Unternehmen im Allgemeinen auf dem Verkauf von Hardware basiert.
- DIY: Installieren Sie das Distributions-Betriebssystem auf Ihrem eigenen Rechner (alter PC, NUC, Raspberry Pi, Heimserver...). Dies ist die wirtschaftlichste Lösung, da Sie einen alten Rechner recyceln oder eine Hardware wählen können, die genau Ihren Bedürfnissen und Ihrem Budget entspricht. Es ist auch die flexibelste und am einfachsten zu konfigurierende Option. Diesen Ansatz werden wir im praktischen Teil des Kurses erkunden.



Hier ist ein Überblick über die wichtigsten verfügbaren Node-in-a-Box-Lösungen (im Jahr 2025):



### Umbrel (umbrelOS & Umbrel Home)



[Heute ist Umbrel der Marktführer für Node-in-a-Box-Lösungen (https://umbrel.com/). Sein Erfolg ist größtenteils auf die Einfachheit seiner Installation (als es auf einem einfachen Raspberry Pi gestartet wurde), sein elegantes und intuitives Interface und ein Ökosystem von Anwendungen zurückzuführen, das schnell gewachsen ist und jetzt extrem umfangreich ist.



![Image](assets/fr/067.webp)



Im Jahr 2020 als einfacher Bitcoin-Knoten mit einigen Zusatzanwendungen gestartet, hat sich Umbrel allmählich zu einer vollwertigen, modernen Heim-Cloud entwickelt.



Ich werde hier nicht näher darauf eingehen, wie es funktioniert und welche besonderen Eigenschaften es hat, da wir diese im ersten Kapitel des nächsten Teils genauer untersuchen werden. Für die Zwecke dieses BTC 202-Kurses habe ich mich für UmbrelOS entschieden, das meiner Meinung nach die beste aktuelle Node-in-a-Box-Lösung für Anfänger und Fortgeschrittene ist.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[Start9 bietet StartOS (https://start9.com/) an, ein System für "souveränes Computing": Ziel ist es, dass jeder seinen eigenen privaten Server besitzt und verwaltet, der durch einen Marktplatz für selbst gehostete Anwendungen erweitert wird. Sie können einen Start9-Server kaufen (Server One für $619, Server Pure für $899) oder Ihren eigenen im DIY-Modus auf Ihrem eigenen Rechner zusammenstellen.



Auf der Bitcoin-Seite können Sie mit StartOS einen Full node, einen Lightning-Knoten, BTCPay-Server, Electrs und viele andere Dienste installieren. Die Anziehungskraft von Start9 geht jedoch darüber hinaus: Es bietet die Möglichkeit, verschiedene Software (File Cloud, Messaging, Monitoring) auf einheitliche Weise und mit vollständiger Kontrolle zu entdecken, zu konfigurieren und freizugeben. Das Projekt richtet sich daher an Benutzer, die eine robuste Plattform zum Selbsthosten wünschen, nicht nur einen einfachen Bitcoin-Knoten. Es ist wahrscheinlich das vollständigste Ökosystem nach Umbrel.



![Image](assets/fr/068.webp)



Der Hauptunterschied zu Umbrel liegt im Interface. Umbrel setzt auf eine ausgefeilte Benutzeroberfläche, während Start9 ein einfacheres, funktionelleres Interface bietet. Das Anwendungsökosystem von Start9 ist weniger reichhaltig als das von Umbrel, aber es gleicht dies durch mehrere technische Vorteile aus: Der Zugang zu erweiterten Anwendungseinstellungen ist vereinfacht, während Umbrel schnell restriktiv wird, wenn die gewünschte Option nicht vom Interface bereitgestellt wird. Start9 zeichnet sich auch durch die Verwaltung der Backups aus: Abgesehen von der effizienten Lösung von Umbrel für den LND gibt es im Gegensatz zu Start9 keinen vereinheitlichten Mechanismus. Darüber hinaus bietet es leichter zugängliche Überwachungswerkzeuge und eine verschlüsselte Fernverbindung (`https`), während der lokale Zugang zu Umbrel über `http` erfolgt.



Kurz gesagt, wenn Sie nur die wesentlichen Anwendungen für Bitcoin benötigen, kein besonderes Interesse an Umbrels sehr reichhaltigem Ökosystem haben und der Interface-Benutzer keine Priorität hat, dann ist Start9 die bessere Wahl. Ansonsten ist Umbrel die bessere Wahl.



https://planb.network/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MyNode



[MyNode ist eine Distribution, die sich ausschließlich auf Bitcoin und Lightning konzentriert (https://mynodebtc.com/) und ein Web-Interface, einen Anwendungsmarktplatz und Ein-Klick-Upgrades bietet. Sie können entweder gebrauchsfertige Hardware kaufen (*Modell Zwei* für 549 $ erhältlich) oder MyNode kostenlos auf Ihrem eigenen Rechner installieren. Das Projekt bietet auch eine *Premium*-Version der Software ($94) an, die vorrangigen Support und erweiterte Funktionen umfasst.



![Image](assets/fr/069.webp)



In der Praxis vereint MyNode alle grundlegenden Bausteine, die für den Betrieb eines Full node erforderlich sind, sowie die für Bitcoin-Nutzer wichtigen Anwendungen. Daher ist es eine geeignete Lösung, wenn Sie keine Anwendungen außerhalb des Bitcoin-Ökosystems benötigen, wie z. B. selbst gehostete Anwendungen, die in Start9- und Umbrel-Systemen zu finden sind.



https://planb.network/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz ist ein 100% quelloffenes Projekt](https://docs.raspiblitz.org/) (MIT-Lizenz) für die Montage eines Bitcoin-Knotens und eines Lightning-Knotens auf einem Raspberry Pi. Laden Sie einfach das Image herunter, starten Sie es und folgen Sie dann dem Assistenten, um einen funktionierenden Node-in-a-Box auf Ihrem Raspberry Pi zu haben. Vormontierte Kits sind auch von Drittanbietern erhältlich und kosten in der Regel zwischen $300 und $400, je nach Hardware. RaspiBlitz bietet auch eine Reihe zusätzlicher, einfach zu installierender Anwendungen an.



![Image](assets/fr/070.webp)



Wenn Sie einen Raspberry Pi besitzen, ist dies eine ausgezeichnete Option, da komplette Systeme wie Umbrel für diese Art von Mini-PC immer schwerer werden.



https://planb.network/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo ist ein datenschutzorientiertes Node-in-a-Box-System (https://wiki.ronindojo.io/en/home), das die Bereitstellung von Samurai Dojo und Whirlpool automatisiert, mit einem dedizierten Interface und Plugins, die speziell für das Samurai-Ökosystem entwickelt wurden.



Das Prinzip ist einfach: Wenn Sie Ashigaru Wallet (der Fork-Nachfolger von Samurai Wallet, nachdem seine Entwickler verhaftet wurden) verwenden oder wenn Sie von fortgeschrittenen Datenschutz-Tools profitieren möchten, ist RoninDojo für Sie.



![Image](assets/fr/071.webp)



Das Projekt bot früher eine vorkonfigurierte Maschine namens Tanto an, die aber derzeit nicht verfügbar ist. Möglicherweise wird er zu einem späteren Zeitpunkt wieder angeboten. In der Zwischenzeit ist es möglich, RoninDojo einfach auf einem Rock5B+ oder Rockpro64 zu installieren, oder sogar indirekt auf einem Raspberry Pi.



https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



Eine weitere [Node-in-a-box-Lösung ist Nodl](https://www.nodl.eu/). Wie bei den vorherigen Projekten können Sie entweder die vorkonfigurierte Hardware kaufen (je nach Modell zwischen 599 und 799 €) oder sie selbst im DIY-Modus installieren.



Auf der Softwareseite integriert Nodl Bitcoin core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL, sowie BTC RPC Explorer, alle mit einer integrierten Update-Kette und Open-Source-Code unter der MIT-Lizenz.



![Image](assets/fr/072.webp)



Nachdem Sie die verschiedenen Softwarelösungen untersucht haben, ist es nun an der Zeit, den Rechner auszuwählen, auf dem Ihr Knoten gehostet werden soll!




## Übersicht der Hardware-Lösungen


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Nachdem wir nun alle Möglichkeiten der Software erkundet haben, wollen wir uns auf die für Ihren Knoten erforderliche Hardware konzentrieren. Ich werde Ihnen einige konkrete Ratschläge für die Auswahl Ihrer Komponenten geben, zusammen mit Konfigurationen, die auf verschiedene Budgets zugeschnitten sind. Natürlich handelt es sich hierbei um meine persönliche Meinung und mein Feedback: Es gibt sicherlich noch andere relevante Alternativen als die hier vorgestellten. Außerdem werde ich nicht auf die vormontierten Maschinen eingehen, die von Node-in-a-Box-Projekten angeboten werden und die wir bereits im vorherigen Kapitel behandelt haben. Hier werden wir uns ausschließlich auf DIY-Lösungen konzentrieren.



### Brauchen Sie wirklich eine eigene Maschine?



In den letzten Jahren sind sich Bitcoiner zunehmend eines weit verbreiteten Missverständnisses bewusst geworden, insbesondere mit der Popularisierung von Node-in-a-Box in den frühen 2020er Jahren: Ein Bitcoin-Knoten muss zwangsläufig auf einem ausschließlich für diesen Zweck vorgesehenen Rechner laufen. Dies ist jedoch nicht der Fall. Sie brauchen nicht unbedingt einen speziellen Computer, um einen Bitcoin-Knoten zu betreiben: Bitcoin core kann durchaus auf Ihrem normalen PC laufen. Wenn Sie über genügend Speicherplatz für Blockchain verfügen oder das Pruning aktivieren, können Sie die Kette validieren, Ihren Wallet anschließen und das Programm sogar schließen, wenn Sie es nicht mehr benötigen. Der Vorteil dieses Ansatzes ist beträchtlich: keine Anfangsinvestition und minimale Komplexität.



![Image](assets/fr/074.webp)



Dennoch ist es oft bequemer, einen eigenen Rechner zu verwenden. Er kann kontinuierlich (rund um die Uhr) laufen, ist jederzeit aus der Ferne erreichbar, beansprucht nicht die Ressourcen Ihres Hauptrechners und isoliert vor allem die Anwendungen (eine gute Sicherheitspraxis: Wenn Ihr persönlicher PC ein Problem hat, funktioniert Ihr Knoten weiter und umgekehrt). Die Frage lautet also nicht: "Brauche ich einen eigenen Rechner?", sondern vielmehr: "Brauche ich einen Knoten, der ständig online ist, auf den andere Geräte zugreifen können und der entwicklungsfähig ist?" (Lightning, Indexer, zusätzliche Anwendungen...). Wenn die Antwort "Ja" lautet, wird die Entscheidung für einen separaten Rechner die Dinge viel einfacher machen.



### 3 Beschaffungsmethoden: Recycling, Second-Hand und neu



#### Recycling eines alten PCs



Das ist die wirtschaftlichste Lösung. Die meisten von uns haben einen alten PC mit Dust zu Hause oder bei Freunden und Familie: dies ist die perfekte Gelegenheit, ihn wieder in Betrieb zu nehmen! Um ihn für die Verwendung als Bitcoin-Knoten anzupassen, fügen Sie einfach eine 2-TB-SSD hinzu und ersetzen oder fügen je nach Bedarf RAM-Riegel hinzu, um den Arbeitsspeicher zu erhöhen. Rechnen Sie mit einem Preis zwischen 100 und 200 € für eine voll funktionsfähige Maschine.



Prüfen Sie vor dem Kauf eines Geräts die Anzahl der verfügbaren Festplattensteckplätze, die Art des Anschlusses (M.2 oder SATA), das Format des Arbeitsspeichers (SODIMM oder DIMM) und seine Generation (DDR4 usw.). Sie sollten auch die Gelegenheit nutzen, das Gerät zu reinigen, insbesondere den Lüfter, um eine optimale Leistung zu gewährleisten.



Seien Sie jedoch vorsichtig, wenn Sie einen Laptop verwenden: Der Akku kann mit der Zeit zu einem Problem werden (mehr dazu später in diesem Kapitel).



#### Überholt oder gebraucht



Der Markt ist voll von generalüberholten Business-Mini-PCs wie dem *Lenovo ThinkCentre Tiny*, dem *HP EliteDesk Mini* oder dem *Dell OptiPlex Micro*. Diese Geräte sind solide, kompakt, leise und energieeffizient. Ihr Preis liegt weit unter dem Neupreis, und es ist leicht, Modelle mit i5/i7-Prozessoren der 6. bis 10. Generation und 8 bis 16 GB Arbeitsspeicher zu finden, und das alles zu sehr attraktiven Preisen, die im Allgemeinen zwischen 70 und 200 Euro liegen, je nach Konfiguration. Meiner Meinung nach ist dies wahrscheinlich die beste Option, wenn Sie einen dedizierten Rechner für Ihren Bitcoin-Knoten suchen.



![Image](assets/fr/075.webp)



Es ist auch möglich, gebrauchte PCs und Laptops zu finden, die schon ein paar Jahre alt sind, mit interessanten Konfigurationen und einem hervorragenden Preis-Leistungs-Verhältnis.



**Hinweis:** Geräte aus Firmenflotten, wie z. B. das *ThinkCentre Tiny*, sind oft nur mit einem *DisplayPort* (DP)-Anschluss für den Bildschirm ausgestattet und haben keinen HDMI-Ausgang. Vergessen Sie also nicht, einen Adapter oder ein DP-zu-HDMI-Kabel mitzubringen, falls Sie eines benötigen.



#### Neu kaufen



Wenn Ihr Budget es zulässt, können Sie sich auch für einen neuen Rechner entscheiden. Dies ist eine gute Option, wenn Sie aktuelle Hardware mit guter Leistung haben möchten, insbesondere wenn Sie Umbrel oder Start9 mit zusätzlichen Anwendungen außerhalb des Bitcoin-Ökosystems für das Self-Hosting verwenden möchten.



### Welche Art von Maschine sollte ich wählen?



#### Mini-PC "NUC" / Barebone



Mini-PCs bieten meiner Meinung nach den besten Kompromiss für das Hosting eines Bitcoin-Knotens zu Hause. Sie sind platzsparend, passen leicht in ein Regal, verbrauchen nur wenig Strom und eignen sich für einfache Hardwareänderungen, wie das Hinzufügen von RAM oder den Austausch der SSD.



Ich persönlich bevorzuge den *Lenovo ThinkCentre Tiny*, der auf dem Gebrauchtmarkt (aus Firmenflotten) sehr verbreitet ist; er ist besonders robust und leicht zu modifizieren. Natürlich gibt es auch viele Äquivalente von anderen Herstellern: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*..



![Image](assets/fr/001.webp)



**Highlights:** geringer Platzbedarf, mäßiger Stromverbrauch, geringe Geräuschentwicklung, Skalierbarkeit (je nach Modell) und Zuverlässigkeit.



**Schwächen:** etwas teurer als ein SBC vom Typ Raspberry Pi, kein eingebauter Bildschirm (Fernzugriff oder über externen Monitor), keine Batterie (plötzliches Abschalten bei Stromausfall).



#### Dedizierter Laptop



Er ist eine hervorragende, kostengünstige Alternative zum Mini-PC: Heutzutage kann man gebrauchte oder sogar neue Laptops zu niedrigen Preisen finden, die mit guten Prozessoren, zahlreichen Anschlüssen sowie einem integrierten Bildschirm und einer Tastatur (sehr praktisch für die Erstinstallation) ausgestattet sind. Vor allem aber wirkt der Akku wie eine natürliche USV: Bei einem Stromausfall schaltet sich der Knoten nicht abrupt ab und kann sogar mehrere Stunden lang betriebsbereit bleiben.



![Image](assets/fr/076.webp)



**Highlights:** All-in-One-Lösung, der Akku fungiert als USV (keine Stromausfälle), vereinfachte Installation dank integriertem Display und Tastatur, integrierte Wi-Fi-Karte und eine große Auswahl an Gebraucht- und Neuwarenmärkten (was oft bedeutet, dass Sie Preise aushandeln können).



**Schwächen:** etwas höherer Stromverbrauch als bei einem reinen Mini-PC, allmähliche Abnutzung des Akkus im 24/7-Betrieb mit Kapazitätsverlust, seltene, aber reale Gefahr des Aufblähens des Akkus oder des thermischen Durchgehens mit dem Alter. Es ist vor allem dieser Aspekt, der mich den Mini-PC für die bessere Option als den Laptop halten lässt: die allmähliche Abnutzung des Akkus und die damit verbundenen Risiken.



Wenn Sie sich für diese Lösung entscheiden, empfehle ich Ihnen, den Zustand der Batterie genau im Auge zu behalten, um jegliche Gefahr zu vermeiden. Achten Sie auf übermäßige Hitze, ungewöhnliche Gerüche, Instabilität oder eine verformte Hülle. Im Falle eines Alarms schalten Sie den Computer sofort aus, ziehen Sie den Netzstecker und entsorgen Sie die Batterie in einer speziellen Recyclinganlage.



**Tipp:** Wenn BIOS/UEFI oder das Tool des Herstellers dies zulassen, können Sie eine Lastgrenze (z. B. 60 % oder 80 %) festlegen, um die Lebensdauer der Batterie zu verlängern.



#### Raspberry Pi und andere SBCs: die falsche Idee



In den frühen 2020er Jahren, mit dem Aufkommen der Node-in-a-Box-Software, kam auch der Raspberry Pi-Wahn auf, um einen Bitcoin-Knoten zu betreiben. Die Idee schien attraktiv: preiswert, kompakt und zugänglich.



![Image](assets/fr/073.webp)



In der Praxis kann ein Raspberry Pi ausreichend sein, wenn Ihr Ziel nur darin besteht, einen Bitcoin-Knoten ohne zusätzliche Anwendungen zu betreiben. Sobald Sie jedoch Umbrel, Start9 oder ein umfangreicheres Ökosystem (Block explorer, Address Indexer, Lightning-Knoten, selbst gehostete Anwendungen...) nutzen wollen, stößt der Rechner schnell an seine Grenzen.



Der Raspberry Pi hat eine Reihe von Nachteilen:




- zu schlanke Prozessoren mit einer ARM-Architektur, die manchmal mit bestimmter Software inkompatibel ist oder mehr Handhabung erfordert;
- Gelöteter Arbeitsspeicher, der nicht aufgerüstet werden kann, mit begrenzten Konfigurationen (oft maximal 8 GB);
- externe Boxen für SSDs, die per Kabel angeschlossen werden, häufige Fehlerquellen, die den Kauf einer speziellen Karte für eine stabile SSD erfordern;
- neigung zur schnellen Erwärmung und Schwierigkeiten bei der korrekten Abkühlung;
- sie müssen zusätzliche Hardware kaufen (Gehäuse, Lüfter, SSD-Karte usw.);
- sehr begrenzte Konnektivität.



In der Vergangenheit lag der große Vorteil von SBCs wie dem Raspberry Pi in ihrem Preis: Für ein paar Dutzend Euro konnte man einen dedizierten Rechner bekommen. Heute sind die Preise jedoch stark gestiegen, und wenn man all die notwendige zusätzliche Hardware hinzufügt, nähern sich die Kosten denen der ersten gebrauchten oder generalüberholten x86-Mini-PCs, die meiner Meinung nach viel mehr Vorteile bieten. Aus diesem Grund empfehle ich nicht, sich für einen SBC zu entscheiden.



### Auswahl der Komponenten



#### Festplattenspeicher: SSD obligatorisch, mindestens 2 TB



Technisch ist es möglich, einen Bitcoin-Knoten auf einer Festplatte zu betreiben. Das Problem ist, dass sich alles beträchtlich verlangsamen wird, insbesondere die IBD, die aufgrund der intensiven Nutzung der Festplatte als Cache durch Bitcoin core extrem lang werden wird (insbesondere für das UTXO-Set). Aus diesem Grund rate ich dringend von der Verwendung einer Festplatte ab: Sie stellt einen echten Engpass dar, schränkt die künftige Entwicklung stark ein (z. B. für einen Lightning-Knoten) und kann sogar zu einer Fehlanpassung der Synchronisation mit dem Blockchain-Kopf führen. Außerdem erhöht die ständige Beanspruchung der mechanischen Festplatte das Risiko einer vorzeitigen Abnutzung.



SSDs verändern Ihr Nutzererlebnis radikal: Alles wird schneller und reibungsloser, bei weitaus höherer Zuverlässigkeit. Die Verwendung einer SSD ist daher (fast) obligatorisch für Ihren Knotenpunkt, und Sie werden es nicht bereuen, zumal Modelle mit hoher Kapazität jetzt relativ erschwinglich sind.



![Image](assets/fr/077.webp)



Was die Kapazität angeht, so etablieren sich 2 TB allmählich als das neue vernünftige Minimum. Im Sommer 2025 nähert sich Blockchain bereits 700 GB, und wenn man Umbrel, einen Address-Indexer und einige Anwendungen hinzufügt, wird eine 1-TB-SSD schnell gesättigt sein. Mit 2 TB haben Sie einen komfortablen Spielraum für die kommenden Jahre (grob geschätzt zwischen 5 und 15 Jahren). Sie können sich auch für 4 TB entscheiden, wenn Sie planen, viele Anwendungen auf Umbrel zu nutzen, große Dateien im Self-Hosting zu speichern oder wenn Sie Ihren Speicherplatzbedarf weitgehend voraussehen wollen.



![Image](assets/fr/078.webp)



Was das Format betrifft, so hängt dies von den auf Ihrem Computer verfügbaren Anschlüssen ab; wenn möglich, empfehle ich jedoch die Verwendung einer NVMe M.2 SSD.



#### Speicher (RAM): 8 bis 16 GB



Für Bitcoin core allein (ohne Umbrel-Overlay) empfehlen die Entwickler mindestens 256 MB RAM bei niedrigsten Einstellungen, 512 MB bei Standardeinstellungen und 1 GB für den normalen Gebrauch.



Wenn Sie hingegen ein Node-in-a-Box-System wie Umbrel oder Start9 verwenden, sind die Anforderungen an den Arbeitsspeicher deutlich höher. Die Umbrel-Entwickler empfehlen ein Minimum von 4 GB RAM. Das mag ausreichen, um nur Core laufen zu lassen, aber Sie werden bald an die Grenzen stoßen. Sie empfehlen daher 8 GB, was ich auch als Minimum für eine Grundkonfiguration um Bitcoin (Core, LND, Indexer und ein paar Anwendungen) betrachte. Meiner Erfahrung nach sind 8 GB mit Umbrel und ein paar zusätzlichen Diensten immer noch ein bisschen knapp. Um wirklich komfortabel zu sein und etwas Spielraum zu haben, würde ich 16 GB RAM empfehlen.



#### Prozessor (CPU)



Die Mindestanforderung für einen Umbrel-Knoten ist ein Dual-Core 64-Bit-Prozessor von Intel oder AMD. Wenn Sie zusätzlich zu Bitcoin core einige Anwendungen nutzen wollen, wird ein Quad-Core (oder höher) einen echten Unterschied in Bezug auf die Flüssigkeit machen. So sind beispielsweise i5/i7-Prozessoren der 6. bis 10. Generation auf dem Gebrauchtmarkt eine hervorragende Option.



### Beispiele für konkrete Konfigurationen



Im Folgenden schlage ich drei konkrete Konfigurationen vor, die an unterschiedliche Budgets und Bedürfnisse angepasst sind, mit genauen Modellen, die sie unterstützen. Diese Wahlmöglichkeiten dienen als Beispiele, um die Informationen in diesem Kapitel zu veranschaulichen; Sie sind nicht verpflichtet, genau diese Modelle zu wählen. Da ich den Mini-PC auf lange Sicht für die beste Option halte, werde ich mich bei den drei vorgeschlagenen Konfigurationen auf dieses Format stützen.



*Die unten aufgeführten Preise sind nur Richtwerte und können je nach Region, Anbieter und Zeitraum variieren*



In erster Linie benötigen Sie eine SSD, die groß genug ist, um den Blockchain unterzubringen, und die dennoch genügend Spielraum lässt. SSDs haben eine begrenzte Lebensdauer in Bezug auf die Schreibzyklen und das Gesamtvolumen der geschriebenen Daten. Ein Bitcoin-Knoten belastet die Festplatte beim Schreiben jedoch erheblich. Deshalb empfehle ich nicht die Einsteigermodelle, sondern eine NVMe-SSD, die eine deutlich bessere Leistung bietet.



Als Beispiel habe ich für die Zwecke dieses Kurses das folgende Modell gewählt: *Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*, erhältlich für rund 120 € auf Amazon. Sie können sich auch für andere bekannte Marken wie Crucial, Western Digital oder Kingston entscheiden.



![Image](assets/fr/046.webp)



#### Low-Budget-Konfiguration



Wenn Ihr Budget sehr begrenzt ist (unter 200 €), würde ich Ihnen natürlich raten, nicht in eine spezielle Maschine zu investieren, sondern Bitcoin core direkt auf Ihrem normalen PC zu installieren (im pruned-Modus, wenn Sie nicht genügend Speicherplatz haben).



Ansonsten empfehle ich für ein Einstiegsbudget den *HP EliteDesk 800 G2 Mini*. Ich habe bei Amazon ein generalüberholtes Modell für 96 € gefunden, das mit einem Intel Core i5 Prozessor der 6. Generation und 8 GB RAM ausgestattet ist. Dies ist eine besonders interessante Option für Einsteiger: Dieser Prozessor und diese Menge an Arbeitsspeicher sind mehr als genug, um Core auf Umbrel sowie mehrere Anwendungen gleichzeitig laufen zu lassen, z. B. einen Electrs-Indexer, einen Lightning-Knoten und eine Mempool-Instanz, vorausgesetzt, man weist Core nicht zu viel Cache zu. Darüber hinaus ist es bei dieser Art von Mini-PC einfach, den Arbeitsspeicher auf 16 GB zu erweitern, falls dies erforderlich sein sollte (für einen oder zwei hochwertige Speichersticks müssen Sie ca. 30-40 € zusätzlich bezahlen).



![Image](assets/fr/045.webp)



Fügen Sie dann einfach die SSD zum Budget hinzu. Ausgehend von der Samsung 2TB für 120 € ergeben sich Gesamtkosten von 216 € für ein komplettes, funktionsfähiges Gerät.



#### Medium-Budget-Konfiguration



Wenn Sie über ein durchschnittliches Budget von etwa 300 Euro für den Rechner verfügen, der Ihren Knoten hosten soll, empfehle ich zum Beispiel einen *Lenovo ThinkCentre Tiny*, der mit einem leistungsstarken Prozessor und ausreichend Arbeitsspeicher ausgestattet ist. Ich habe bei Amazon ein generalüberholtes Modell für 180 € gefunden, das mit einem Intel Core i7-Prozessor der 6. Generation und 16 GB RAM ausgestattet ist. Zusammen mit der 2-TB-SSD für 120 Euro belaufen sich die Gesamtkosten auf 300 Euro.



![Image](assets/fr/044.webp)



Mit dieser Maschine haben Sie eine komfortable Konfiguration: ein schnelles IBD und die Möglichkeit, zahlreiche Anwendungen auf Ihrem Umbrel oder Start9 ohne Schwierigkeiten auszuführen. Das ist genau die Konfiguration, die ich für diesen BTC 202 Kurs verwende.



#### High-End-Konfiguration



Mit einem größeren Budget werden die Möglichkeiten deutlich größer. Sie können eine DIY-Konfiguration wählen oder sich sogar für eine vormontierte Maschine entscheiden, die direkt von einem node-in-a-box-Projekt angeboten wird.



Der *ASUS NUC 14 Pro* ist zum Beispiel neu bei Amazon für 540 € erhältlich. Für diesen Preis erhalten Sie einen Intel Core Ultra 5-Prozessor (aktuell und besonders leistungsstark), begleitet von 16 GB DDR5-RAM. Mit einer solchen Konfiguration können Sie eine IBD in Rekordzeit durchführen und anspruchsvolle Anwendungen problemlos installieren.



Dies ist eine äußerst komfortable Konfiguration, sogar ein Overkill, wenn das ursprüngliche Ziel nur darin besteht, einen Bitcoin-Knoten zu betreiben. Wenn Sie hingegen alle Vorteile der auf Umbrel und Start9 verfügbaren selbst gehosteten Anwendungen nutzen wollen, ist diese Leistungsstufe genau richtig für Sie.



![Image](assets/fr/043.webp)



Je nach Verwendungszweck können Sie sich entweder für eine 2-TB-SSD entscheiden, wie bei den anderen Konfigurationen, oder direkt für eine 4-TB-SSD für 260 €, wenn Sie auch persönliche Dateien speichern und Ihre Self-Hosting-Nutzung erweitern möchten. Mit einer 2-TB-SSD betragen die Gesamtkosten der Konfiguration 660 €, während sie mit einer 4-TB-SSD 800 € erreichen.



### Noch ein paar Tipps





- Wenn Sie gebrauchte Geräte kaufen und mit Bitcoins bezahlen möchten, kommen Sie zu einem Treffen in Ihrer Nähe! Wenn Sie sich mit anderen Teilnehmern austauschen, finden Sie mit Sicherheit passende Geräte zu einem guten Preis und tragen gleichzeitig dazu bei, die Kreislaufwirtschaft rund um Bitcoin am Leben zu erhalten. Es ist auch eine Gelegenheit, von den guten Ratschlägen der Gemeinschaft zu profitieren.





- Für die Internetverbindung benötigen Sie natürlich ein RJ45-Ethernet-Kabel, zumindest für die Systeminstallation.





- Einige Umgebungen wie Umbrel erlauben die Verwendung von Wi-Fi, aber die Leistung ist in der Regel schlechter (vor allem, wenn Sie Ihren Lightning-Knoten aus der Ferne verwenden möchten, da dies Auswirkungen haben kann). Wenn Sie sich für Wi-Fi entscheiden, vergewissern Sie sich, dass Ihr Rechner über eine integrierte Karte verfügt oder fügen Sie einen kompatiblen Dongle hinzu.





- Verwenden Sie immer das Original-Netzgerät Supply des Herstellers für Ihr Gerät. Dies ist wichtig, um Schäden an Ihrem Gerät zu vermeiden und die Gefahr eines Brandes zu verhindern.





- Wenn Ihre Maschine nicht über eine eingebaute Batterie verfügt, sollten Sie in einen Wechselrichter investieren, um plötzliche Abschaltungen zu vermeiden.





- Je nach Wert Ihrer Geräte und Ihrer geografischen Lage kann auch ein Blitzschutzsystem sinnvoll sein, entweder direkt an der Schalttafel oder an der verwendeten Steckdosenleiste.





- Denken Sie schließlich daran, die Kühlung Ihres Rechners zu optimieren: Reinigen Sie ihn regelmäßig und stellen Sie ihn an einem kühlen, gut belüfteten und übersichtlichen Ort auf, um eine Überhitzung zu vermeiden, die zu einer Drosselung (freiwillige Begrenzung der Geschwindigkeit Ihres Prozessors) führen könnte.



# Einfache Installation eines Bitcoin-Knotens


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: viel mehr als ein Bitcoin-Knoten


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel ist ein persönliches Server-Betriebssystem, das entwickelt wurde, um Self-Hosting zugänglich zu machen: Sie installieren Umbrel, öffnen einen Browser auf `umbrel.local`, und verwalten alles über einen einfachen Remote-Interface.



Das Projekt machte zunächst die Idee eines Bitcoin- und Lightning-Knotens mit nur einem Klick populär und entwickelte sich dann zu einer echten "Home Cloud": Datei- und Fotospeicherung, Multimedia-Streaming, Netzwerk-Tools, Heimautomatisierung, lokale KI und Hunderte von Apps, die über einen integrierten App Store installiert werden können.



In Umbrel läuft jede Anwendung in einem Docker-Container (Isolierung, atomare Updates, unabhängiger Start/Stop). Der Interface zentralisiert den Zugang zu all diesen Anwendungen und bietet Single Sign-On (mit optionaler 2FA), One-Click-Updates für Betriebssystem und Anwendungen, Live-Überwachung der Maschine (CPU, RAM, Temperatur, Speicher), Verwaltung von Berechtigungen zwischen den Anwendungen und einen Überblick über deren Verbrauch.



Das Ziel von Umbrel ist es daher, Ihnen die Kontrolle und die Vertraulichkeit Ihrer Daten zurückzugeben, ohne auf Cloud-Dienste angewiesen zu sein, und zwar über den einfachen Betrieb eines Bitcoin-Knotens hinaus.



### Umbrel Home vs. UmbrelOS



Umbrel bietet zwei unterschiedliche Ansätze:





- [**Umbrel Home**] (https://umbrel.com/umbrel-home): Dies ist ein gebrauchsfertiger Mini-Server, der speziell für umbrelOS entwickelt und optimiert wurde. Er ist kompakt, leise, Ethernet-verbunden und mit einer NVMe-SSD (bis zu 4 TB optional), 16 GB RAM und einer Quad-Core-CPU ausgestattet. Sie bestellen es, schließen es an und gehen zu `umbrel.local`. Innerhalb von Minuten ist Umbrel einsatzbereit und kann genutzt werden. Das ist die Plug-and-Play-Option.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): Dies ist das Betriebssystem, das Sie selbst auf Ihrer eigenen Hardware installieren können (Mini-PC, NUC, Tower, dedizierter Laptop...). Sie haben denselben Interface und denselben App Store wie bei Umbrel Home.



![Image](assets/fr/080.webp)



In beiden Fällen ist die Benutzererfahrung auf der Softwareseite identisch: browserbasierte Verwaltung, One-Click-Updates, Installation von Anwendungen auf Abruf... Die Do-it-yourself-Lösung ist oft wirtschaftlicher als der Kauf eines Umbrel Home (abhängig von der verwendeten Maschine). Allerdings würde ich nicht unbedingt empfehlen, sich immer für die DIY-Option zu entscheiden, denn **der Kauf eines Umbrel Home trägt direkt zur Finanzierung der Entwicklung des Projekts bei**, da das Geschäftsmodell auf dem Verkauf von Hardware basiert. Und ehrlich gesagt, ist der Preis von 389 € für 2 TB Speicherplatz angesichts der Qualität des angebotenen Geräts sehr angemessen.



![Image](assets/fr/079.webp)



Im nächsten Kapitel werden wir uns damit beschäftigen, wie Sie UmbrelOS DIY auf Ihrem eigenen Rechner installieren können. Sie können diesen BTC 202 Kurs jedoch auf die gleiche Weise verfolgen, wenn Sie sich für ein Umbrel Home entschieden haben.



### Anwendungsfall: vom Bitcoin-Knoten zur Home Cloud



Umbrel kann sehr minimalistisch bleiben und sich ausschließlich auf Bitcoin konzentrieren, oder sich zu einem echten multifunktionalen persönlichen Server entwickeln, je nach Ihren Bedürfnissen. Hier sind die Hauptanwendungen für Umbrel:





- Einfacher Bitcoin-Knoten**: Dies ist die grundlegende Nutzung, auf die sich Umbrel von Anfang an verlassen hat. Du kannst Bitcoin core (oder Knots) laufen lassen, deine Wallets direkt mit deinem Node verbinden, einen Electrum-Server bereitstellen, deinen Mempool Block explorer hosten, um den Blockchain zu sehen, und Gebühren schätzen... Es sind diese Anwendungen, auf die wir uns in diesem Kurs konzentrieren werden.



![Image](assets/fr/082.webp)





- Lightning Network**: Mit Umbrel können Sie auch LND oder Core Lightning, zwei Implementierungen des Lightning Network, einsetzen, um Ihren eigenen Lightning-Knoten zu verwalten. Sie können Kanäle öffnen, Ihre Liquidität verwalten, Zahlungen tätigen, den Ausgleich automatisieren, Dienstleistungen anbieten, einen entfernten Wallet anschließen oder dank der vielen verfügbaren Anwendungen die Vorteile eines erweiterten Interface-Managements nutzen. Wir werden diesen speziellen Anwendungsfall in unserem nächsten LNP 202-Kurs behandeln.



![Image](assets/fr/083.webp)





- Allgemeines Self-Hosting**: mit Nextcloud, Immich, Jellyfin/Plex, DNS-weiten Werbeblockern (Pi-hole/AdGuard), VPNs (WireGuard, Tailscale), Heimautomatisierung (Home Assistant), Backups, Notizverwaltung, Office-Tools, lokale KI (Ollama + Open WebUI)... Umbrel kann Ihr persönlicher Server werden, der es Ihnen ermöglicht, die Kontrolle über Ihre Daten zurückzugewinnen. Sie hosten die Dienste, die Sie täglich nutzen, selbst, mit einer ausgefeilten Benutzererfahrung, die externen Lösungen sehr ähnlich ist, während Sie die volle Kontrolle über Ihre Daten und Ihre Privatsphäre behalten.



Durch die Bereitstellung von Anwendungen in Containern können Sie Umbrel so gestalten, wie Sie es wünschen: Beginnen Sie mit einem einfachen Bitcoin-Knoten und einigen Anwendungen, die mit seinem Ökosystem verbunden sind, installieren Sie dann einen Lightning-Knoten neben Ihrem Bitcoin-Knoten und erweitern Sie Ihre Instanz nach und nach mit den selbst gehosteten Anwendungen, die Sie benötigen.



### Gemeinschaft und gegenseitige Hilfe



Einer der Hauptvorteile von Umbrel gegenüber seinen Konkurrenten ist seine große und sehr aktive Benutzergemeinschaft. Du kannst sie hauptsächlich über [ihren Discord] (https://discord.gg/efNtFzqtdx) und [ihr Online-Forum] (https://community.umbrel.com/) erreichen. Hier finden Sie nicht nur praktische Ratschläge, sondern vor allem auch Lösungen für Probleme und Fehlerbehebungen. Es ist ein großartiger Ort, um anzufangen, Fortschritte zu machen und schließlich anderen Nutzern zu helfen, damit Sie mit Ihrem Coin nicht allein gelassen werden.



![Image](assets/fr/084.webp)



### UmbrelOS-Lizenz



Der Code von Umbrel ist öffentlich zugänglich (Sie können ihn ansehen, Fork, und verändern), aber er steht nicht unter einer echten Open-Source-Lizenz. Tatsächlich wird umbrelOS unter der [*PolyForm Noncommercial 1.0*] Lizenz (https://polyformproject.org/licenses/noncommercial/1.0.0/) vertrieben, obwohl einige zugehörige Entwicklungswerkzeuge unter der MIT-Lizenz verfügbar sind.



Praktisch gesehen können Sie mit umbrelOS so ziemlich alles machen, was Sie wollen, solange es für den persönlichen, nicht-kommerziellen Gebrauch ist: Modifikation, Weitergabe für nicht-kommerzielle Zwecke, Erstellung von Derivaten für Sie selbst oder für nicht-kommerzielle Organisationen, vorausgesetzt, Sie respektieren die rechtlichen Hinweise.



Es ist jedoch verboten, Umbrel oder seine Derivate zu verkaufen (z.B. eine vormontierte Maschine mit vorinstalliertem UmbrelOS), Umbrel-bezogene Dienstleistungen kommerziell anzubieten oder seinen Code in ein Produkt zu integrieren.



Technisch gesehen schränkt diese Lizenz die Installation, das Auditing oder die Anpassung von Umbrel für den persönlichen Gebrauch nicht ein. Rechtlich schützt sie das Projekt gegen unerlaubten Weiterverkauf oder kommerzielles Hosting, insbesondere durch Cloud-Anbieter. Umbrel ist daher nicht quelloffen, obwohl sein Code öffentlich zugänglich bleibt.



Allerdings behält jede Anwendung im Store ihre eigene Lizenz, die häufig Open Source ist.




## Installation eines Full node mit Umbrella


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Nun, da wir alle notwendigen Informationen haben, ist es an der Zeit, sich mit den Details zu befassen. In diesem Tutorial zeigen wir Ihnen, wie Sie einen kompletten Bitcoin Knoten mit UmbrelOS installieren.



### Erforderliche Materialien



Hier verwenden wir das UmbrelOS x86-Image (genauer gesagt, die x86_64-Version). Sie können diese Anleitung auf jedem Rechner Ihrer Wahl durchführen, solange er nicht mit einem Prozessor der ARM-Architektur ausgestattet ist (kein Apple Silicon, Raspberry Pi, etc.). Das bedeutet, dass jeder Computer mit einem Intel- oder AMD-64-Bit-Prozessor ausreicht, solange er die Mindestanforderungen erfüllt, je nachdem, wie Sie Ihren Umbrel verwenden wollen (mindestens ein Dual-Core-Prozessor wird empfohlen).



Wenn Sie sich für einen Raspberry Pi 5 entschieden haben (eine Option, die ich nicht empfehle, wie im vorherigen Abschnitt erwähnt), ist die Installation etwas anders. Sie können dann dieser speziellen Anleitung folgen und zu meinem Kurs zurückkehren, sobald Sie auf der Interface Webseite `http://umbrel.local` sind:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Wie im vorherigen Abschnitt erwähnt, habe ich mich entschieden, dieses Tutorial auf einem kleinen renovierten PC auszuführen, den ich zu einem guten Preis gefunden habe: ein *Lenovo ThinkCentre M900 Tiny*, ausgestattet mit einem Intel Core i7 Prozessor und 16 GB RAM. Dies ist eine sehr komfortable Konfiguration für den Betrieb von Umbrel, insbesondere für einen Bitcoin Knoten. Ich habe mich jedoch für diese Konfiguration entschieden, weil ich später einen Lightning-Knoten und andere anspruchsvollere Anwendungen installieren möchte. Ich habe auch eine 2TB SSD zu meinem ThinkCentre hinzugefügt, um den vollen Blockchain zu behalten und immer noch eine komfortable Marge zu haben. Mit dieser Konfiguration belaufen sich die Gesamtkosten auf 270 €, einschließlich aller Ausgaben.



![Image](assets/fr/001.webp)



Die ThinkCentre Tiny-Reihe von Lenovo hat es mir besonders angetan, denn es sind kompakte, leise und sehr robuste Geräte. Diese Computer sind bei Unternehmen sehr beliebt und daher auf dem Gebrauchtmarkt reichlich vorhanden, wo man interessante Konfigurationen zwischen 70 und 200 Euro finden kann.



Wenn Sie sich, wie ich, für einen PC ohne Monitor entschieden haben, müssen Sie **nur für die Dauer der Installation einen Monitor und eine Tastatur** anschließen. Danach können Sie von einem anderen Computer im selben Netzwerk (oder über andere Methoden, die wir in späteren Kapiteln behandeln werden) auf den PC zugreifen. Sie benötigen außerdem ein RJ45-Ethernet-Kabel, um Ihren Rechner mit dem lokalen Netzwerk zu verbinden, und einen USB-Stick mit mindestens 4 GB, um das Installations-Image zu speichern.



Hier noch einmal die Anforderungen an die Ausrüstung:




- Computer mit x86_64-Prozessor (mindestens Dual-Core, empfohlen Quad-Core);
- RAM-Speicher (mindestens 4 GB, 8 GB oder mehr bei längerer Nutzung empfohlen);
- SSD (empfohlen + 2 TB);
- USB-Stick (+ 4 GB) für die Installation des UmbrelOS-Images;
- Monitor und Tastatur (nur bei der Erstinstallation sinnvoll, wenn der PC nicht damit ausgestattet ist);
- RJ45-Ethernet-Kabel.



### Schritt 1 - Montage des Computers



Je nach der von Ihnen gewählten Hardware müssen Sie zunächst die verschiedenen Komponenten Ihres Computers zusammenbauen. In meinem Fall hatte die ursprüngliche SSD zum Beispiel nur eine Kapazität von 256 GB, also werde ich sie für eine andere Verwendung recyceln und durch eine 2-TB-SSD ersetzen. Wenn Sie auch die RAM-Module ersetzen möchten, ist jetzt der richtige Zeitpunkt dafür.



### Schritt 2: Vorbereiten eines bootfähigen USB-Sticks



Bevor Sie UmbrelOS auf Ihrem Rechner installieren, müssen Sie einen bootfähigen USB-Stick erstellen, der das Betriebssystem enthält. Alle Schritte in Schritt 2 müssen auf Ihrem persönlichen Computer durchgeführt werden (und nicht direkt auf dem Computer, der Ihr Knoten werden soll).





- Laden Sie zunächst die neueste Version von UmbrelOS im USB-Format herunter:



Gehen Sie auf [die offizielle Umbrel-Website, um das ISO-Image herunterzuladen] (https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) für die Installation über einen USB-Stick. Stellen Sie sicher, dass Sie die mit der x86_64-Architektur kompatible Version auswählen (Datei mit dem Namen `umbrelos-amd64-usb-installer.iso`). Das Herunterladen kann einige Zeit dauern, da das Image recht groß ist.



![Image](assets/fr/002.webp)





- Balena Etcher installieren:



Um den bootfähigen USB-Stick zu erstellen, verwenden Sie ein einfaches, plattformübergreifendes Tool namens [Balena Etcher] (https://www.balena.io/etcher/). Laden Sie es herunter und installieren Sie es auf Ihrem Computer.



![Image](assets/fr/003.webp)





- Stecken Sie einen leeren USB-Stick mit mindestens 4 GB ein:



Schließen Sie einen USB-Stick an Ihren Computer an (denjenigen, auf den Sie gerade das UmbrelOS und das Balena Etcher Image heruntergeladen haben). **Warnung: alle Daten auf dem Stick werden gelöscht**. Vergewissere dich, dass er keine wichtigen Dateien enthält.





- Brennen Sie das ISO-Image mit Balena Etcher auf den USB-Stick:



Starten Sie den Balena Etcher und wählen Sie die soeben heruntergeladene ISO-Datei "umbrelos-amd64-usb-installer.iso", indem Sie auf die Schaltfläche "*Flash aus Datei*" klicken. Wählen Sie dann den USB-Stick als Zielgerät und klicken Sie auf "*Flash!*", um mit dem Schreiben zu beginnen.



![Image](assets/fr/004.webp)



Sobald der Vorgang abgeschlossen ist, hast du einen bootfähigen USB-Stick, der UmbrelOS enthält und bereit ist, Umbrel auf deinem Rechner zu installieren.



![Image](assets/fr/005.webp)



### Schritt 3: Booten des Computers von einem USB-Stick



Jetzt, wo Ihr bootfähiger USB-Stick mit UmbrelOS fertig ist, können Sie Ihren Computer damit booten, um die Systeminstallation zu starten. Trennen Sie den USB-Stick von Ihrem Hauptrechner und stecken Sie ihn in das Gerät, auf dem Sie Umbrel und Ihren Bitcoin Knoten installieren möchten.



Wie zu Beginn dieses Kapitels erläutert, benötigen Sie zum Abschluss der Installation ein Anzeigegerät und ein Eingabegerät. Schließen Sie einen Bildschirm über HDMI (oder einen anderen Anschluss, je nach Ihrem PC) und eine Tastatur über USB an Ihren Rechner an. Diese Geräte werden nur für die Installation benötigt; danach brauchen Sie sie nicht mehr, da der Zugriff auf Umbrel von einem anderen Computer aus erfolgt. Schließen Sie diese beiden Geräte an Ihren PC an.



**Tipp:** Wenn Sie keinen peripheren Bildschirm zu Hause haben, können Sie Ihren Fernseher verwenden. Mit seinem HDMI-Eingang (oder einem anderen) kann er als vorübergehender Bildschirm verwendet werden, während Sie das Betriebssystem installieren.



Umbrel benötigt natürlich eine Internetverbindung. Schließen Sie das RJ45-Ethernet-Kabel zwischen Ihrem Gerät und Ihrem Router an.



![Image](assets/fr/006.webp)



Schalten Sie Ihren Rechner ein. In den meisten Fällen sollte er den USB-Stick automatisch erkennen und von ihm booten. Sie sehen dann den UmbrelOS Interface Installationsbildschirm.



Wenn das Gerät auf einem anderen System bootet oder eine Fehlermeldung anzeigt, bedeutet dies wahrscheinlich, dass es nicht automatisch vom USB-Stick bootet. Starten Sie in diesem Fall neu und rufen Sie die BIOS/UEFI-Einstellungen auf (je nach Computerhersteller in der Regel durch Drücken von `DEL`, `F2`, `F12` oder `ESC`). Ändern Sie dann die Bootreihenfolge so, dass der USB-Stick Vorrang hat. Dann starten Sie das Gerät neu, um UmbrelOS zu starten.



### Schritt 4: Installieren Sie UmbrelOS auf Ihrem Computer



Sobald das Gerät vom USB-Stick gebootet hat, werden Sie von der Interface UmbrelOS-Installation begrüßt. In diesem Schritt wird das System direkt auf der internen Festplatte des Hard installiert.



Auf dem nun erscheinenden Bildschirm werden alle vom Computer erkannten internen Speichergeräte aufgelistet. Jeder Datenträger ist mit einer Nummer, einem Namen und einer Speicherkapazität versehen. Suchen Sie den Datenträger, auf dem Sie Umbrel installieren möchten. **Warnung: Alle Dateien auf diesem Laufwerk werden dauerhaft gelöscht.**



![Image](assets/fr/007.webp)



Wenn Sie die richtige Festplatte gefunden haben (in der Regel die mit der größten Kapazität, um den Blockchain aufzunehmen), notieren Sie die ihr zugewiesene Nummer. Wenn die von Ihnen gewählte Platte beispielsweise unter der Nummer "2" erscheint, geben Sie einfach "2" ein und drücken dann die Eingabetaste auf der Tastatur.



![Image](assets/fr/008.webp)



Das Programm formatiert die ausgewählte Festplatte, installiert UmbrelOS und konfiguriert das System automatisch. Dies kann ein paar Minuten dauern. Lassen Sie den Prozess ohne Unterbrechung laufen.



![Image](assets/fr/009.webp)



Wenn die Installation abgeschlossen ist, werden Sie aufgefordert, das Gerät auszuschalten. Drücken Sie eine beliebige Taste, um den Computer auszuschalten.



![Image](assets/fr/010.webp)



Sie können nun den USB-Stick, die Tastatur und den Bildschirm entfernen, da sie für Ihren Umbrel nicht mehr benötigt werden. Alles, was von Ihrem Knoten übrig bleibt, ist der Strom Supply und das RJ45-Ethernet-Kabel.



![Image](assets/fr/011.webp)



Überprüfen Sie vor dem Neustart des Geräts die beiden folgenden Punkte:





- Der USB-Stick ist ausgesteckt**: Wenn er angeschlossen bleibt, kann es sein, dass das System auf ihm statt auf der internen Festplatte neu startet;
- Das Ethernet-Kabel ist eingesteckt**: Das Gerät muss mit Ihrem Router verbunden sein, um zu funktionieren.



Drücken Sie den Einschaltknopf. Das System bootet automatisch von der internen Festplatte, auf der UmbrelOS installiert wurde. Der erste Startvorgang kann etwa **5 Minuten** dauern. Während dieser Zeit initialisiert Umbrel seine Dienste und das Interface.



Öffnen Sie von einem anderen Computer (Ihrem normalen PC), der an das **gleiche lokale Netzwerk** angeschlossen ist, einen Webbrowser (Firefox, Chrome...) und gehen Sie zu:



```
http://umbrel.local
```



Dieses Address wird verwendet, um aus der Ferne auf das grafische Benutzer-Interface von Umbrel zuzugreifen und die Konfiguration zu beginnen.



Wenn der Address `http://umbrel.local` nach mindestens 5 Minuten Wartezeit in Ihrem Browser nicht funktioniert, versuchen Sie es einfach:



```
http://umbrel
```



Wenn das immer noch nicht funktioniert, gib die lokale IP Address deines Umbrel direkt in den Browser ein. Zum Beispiel (ersetzen Sie `42` mit der Nummer Ihres Rechners, auf dem Umbrel im lokalen Netzwerk läuft):



```
http://192.168.1.42
```



Um Ihr Umbrel's IP Address zu identifizieren, gibt es mehrere Methoden, von der einfachsten bis zur fortschrittlichsten:





- Greifen Sie auf die Verwaltung Ihres Routers Interface zu und suchen Sie die IP Address des Umbrel-Geräts im lokalen Netz.





- Verwenden Sie eine Netzwerk-Scan-Software wie Angry IP Scanner, um angeschlossene Geräte zu erkennen und den IP Address von Umbrel zu lokalisieren.



![Image](assets/fr/012.webp)



https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Als letzten Ausweg schließen Sie einen Monitor und eine Tastatur wieder an das Gerät an, melden Sie sich an (Standardanmeldung: `umbrel`, Kennwort: `umbrel`) und geben Sie den folgenden Befehl ein:



```
hostname -I
```



Jetzt sind Sie bereit, Umbrel zu benutzen!



### Schritt 5: Erste Schritte mit Umbrel



Um mit der Konfiguration Ihres Umbrel zu beginnen, klicken Sie auf die Schaltfläche "*Start*".



![Image](assets/fr/013.webp)



#### Ein Konto erstellen



Wählen Sie ein Pseudonym oder geben Sie Ihren Namen ein und legen Sie dann ein sicheres Passwort fest. Seien Sie vorsichtig: Dieses Passwort ist die einzige Barriere, die den Zugang zu Ihrem Umbrel von Ihrem Netzwerk aus schützt (und damit möglicherweise auch zu Ihren Bitcoins, wenn Sie einen Lightning-Knoten auf Umbrel betreiben). Es schützt auch den Fernzugriff über Tor oder VPN, wenn diese Dienste aktiviert sind.



Wählen Sie ein sicheres Passwort und stellen Sie sicher, dass Sie mindestens eine Sicherungskopie aufbewahren (ein Passwortmanager wird empfohlen).



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Sobald Sie Ihr Passwort eingegeben haben, klicken Sie auf die Schaltfläche "*Erstellen*".



![Image](assets/fr/014.webp)



Ihre Umbrel-Konfiguration ist nun abgeschlossen.



![Image](assets/fr/015.webp)



#### Entdeckung von Interface



Der Interface von Umbrel ist ziemlich intuitiv:





- Auf der Startseite können Sie Ihre installierten Anwendungen und Widgets anzeigen.



![Image](assets/fr/016.webp)





- Im "*App Store*" können Sie neue Anwendungen installieren,



![Image](assets/fr/017.webp)





- Das Menü "*Dateien*" zentralisiert alle auf Ihrem Umbrel gespeicherten Dokumente.



![Image](assets/fr/018.webp)





- Über das Menü "*Einstellungen*" können Sie die Einstellungen Ihres Umbrel ändern und auf seine Informationen zugreifen:
    - Aktualisieren Sie Ihr Gerät, starten Sie es neu oder stoppen Sie es;
    - Prüfen Sie den verfügbaren Speicherplatz, die RAM-Auslastung und die Prozessortemperatur;
    - Hintergrundbild ändern;
    - Verwalten Sie den Fernzugriff über Tor, aktivieren Sie Wi-Fi oder 2FA.



![Image](assets/fr/019.webp)



#### Sicherheits- und Verbindungseinstellungen



Zuallererst empfehle ich dringend, die Zwei-Faktor-Authentifizierung (2FA) zu aktivieren. Dies fügt Ihrem Passwort ein zusätzliches Layer an Sicherheit hinzu. Sie ist fast unverzichtbar, wenn Sie Ihren Umbrel zum Speichern persönlicher Dateien, zum Betreiben eines Lightning Nodes oder für andere sensible Aktivitäten nutzen wollen.



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Klicken Sie dazu in den Einstellungen auf das entsprechende Feld.



![Image](assets/fr/020.webp)



Scannen Sie dann den angezeigten QR-Code mit Ihrer Authentifizierungsanwendung. Geben Sie dann den 6-stelligen dynamischen Code in das dafür vorgesehene Feld auf Ihrem Umbrel ein.



Von nun an erfordert jede neue Verbindung zu Ihrem Umbrel sowohl das Passwort als auch den 6-stelligen Code, der von Ihrer Anwendung für die Zwei-Faktor-Authentifizierung (2FA) generiert wird.



![Image](assets/fr/021.webp)



Was den Fernzugriff über Tor angeht, empfehle ich dir, diese Option zu deaktivieren, wenn du sie nicht brauchst, um die Angriffsfläche deines Umbrel zu begrenzen. Standardmäßig kann auf deinen Knoten nur von einem Rechner aus zugegriffen werden, der mit demselben lokalen Netzwerk verbunden ist. Wenn du den Zugang über Tor aktivierst, kannst du dein Umbrel trotzdem von unterwegs aus verwalten.



Wenn du diese Funktion aktivierst, ist es theoretisch möglich, dass jeder Rechner auf der Welt versucht, sich mit deinem Knoten zu verbinden, vorausgesetzt, er kennt den Tor Address. Dein Passwort und 2FA schützen dich aber immer noch.



Wenn du diese Option aktivierst, stelle sicher, dass du die Zwei-Faktor-Authentifizierung (2FA) aktivierst, ein sicheres Passwort verwendest und niemals deine Tor-Verbindung Address offenlegst.



Gib einfach diesen Tor Address in deinen Tor-Browser ein, um von jedem Netzwerk aus auf den Interface von Umbrel zuzugreifen.



![Image](assets/fr/026.webp)



Schließlich können Sie auf dieser Einstellungsseite auch die Wi-Fi-Verbindung aktivieren. Wenn Ihr Rechner, der Umbrel hostet, über eine Wi-Fi-Netzwerkkarte oder einen Wi-Fi-Dongle verfügt, können Sie damit auf das Internet zugreifen, ohne das RJ45-Kabel zu benutzen. Je nach Ihrer Konfiguration kann diese Lösung jedoch die Verbindung verlangsamen, was sich auf die anfängliche Synchronisierung (IBD) und die zukünftige Nutzung des Knotens (z.B. für Lightning-Transaktionen) auswirken kann. Ich persönlich empfehle diese Option nicht, da ein Knoten nicht für den mobilen Einsatz gedacht ist: Auf ihn wird immer aus der Ferne zugegriffen, also können Sie ihn auch eingesteckt lassen.



### Schritt 6: Installation eines Bitcoin-Knotens auf Umbrel



Nachdem UmbrelOS nun korrekt auf Ihrem Rechner installiert und konfiguriert ist, können Sie mit der Installation Ihres Bitcoin Knotens fortfahren. Nichts könnte einfacher sein: Gehen Sie in den App Store, öffnen Sie die Kategorie "*Bitcoin*" und wählen Sie dann die Anwendung "*Bitcoin Node*" (eigentlich Bitcoin core).



![Image](assets/fr/022.webp)



Klicken Sie dann auf die Schaltfläche "*Installieren*".



![Image](assets/fr/023.webp)



Sobald die Installation abgeschlossen ist, startet Ihr Bitcoin-Knoten seinen IBD (*Initial Block Download*): Er lädt alle Transaktionen und Blöcke seit der Gründung von Bitcoin im Jahr 2009 herunter und validiert sie.



![Image](assets/fr/024.webp)



Diese Phase ist besonders zeitaufwendig, da ihre Dauer von mehreren Faktoren abhängt, u. a. von der Menge an RAM, die dem Cache des Knotens zugewiesen ist, der Festplattengeschwindigkeit, der Geschwindigkeit der Internetverbindung und der Prozessorleistung. Die Bandbreite der Dauer ist daher je nach Konfiguration sehr groß. Mit einem Hochleistungs-PC (NVMe-SSD, +32 GB RAM, leistungsstarker Prozessor und gute Internetverbindung) kann IBD in etwa zehn Stunden abgeschlossen werden. Mit einem alten Prozessor, wenig Arbeitsspeicher oder - noch schlimmer - einer mechanischen Hard-Festplatte (von der dringend abgeraten wird) kann sich dieser Vorgang hingegen auf mehrere Wochen ausdehnen.



Mit einem normal ausgestatteten PC (ordentlicher Prozessor, 8 bis 16 GB Arbeitsspeicher und eine SSD) reicht das für etwa 2 bis 7 Tage.



Um IBD etwas zu beschleunigen, können Sie den RAM-Speicher für den Knoten-Cache (der hauptsächlich für das UTXO-Set verwendet wird, auf das wir später im Kurs zurückkommen werden) über den Parameter "dbcache" erhöhen. Bei Umbrel wird diese Änderung in den Knotenparametern auf der Registerkarte "*Optimization*" vorgenommen.



![Image](assets/fr/025.webp)



Standardmäßig ist der Wert des Parameters `dbcache` in Bitcoin core auf 450 MiB, also etwa 472 MB, eingestellt. Wenn Sie diesen Wert erhöhen, können Sie IBD etwas beschleunigen. Ich würde jedoch nicht unbedingt empfehlen, diesen Parameter zu hoch zu setzen: Selbst wenn man ihn auf 4 GiB setzt, wird die Synchronisierung nur um etwa 10 % schneller, und im Falle einer Unterbrechung während IBD kann es zu einem Zeitverlust kommen.



Achten Sie darauf, dass Sie nicht einen zu großen Wert für Ihren Rechner zuweisen. Wenn der für UmbrelOS verfügbare Arbeitsspeicher erschöpft ist, kann Ihr Knoten abrupt anhalten, wodurch die IBD unterbrochen wird und Sie sie manuell neu starten müssen, was zu einem erheblichen Zeitverlust führt.



Um mehr über die Auswirkungen des Parameters `dbcache` auf die anfängliche Synchronisierung zu erfahren, empfehle ich diese Analyse von Jameson Lopp: [*Effects of DBcache Size on Bitcoin Node Sync Speed*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Sobald die IBD Ihres Knotens abgeschlossen ist (100%ige Synchronisierung), haben Sie nun einen voll funktionsfähigen Bitcoin-Knoten. Herzlichen Glückwunsch, Sie sind nun ein integraler Bestandteil des Bitcoin-Netzwerks!



![Image](assets/fr/027.webp)



Im nächsten Teil werden wir uns mit der praktischen Nutzung Ihres neuen Knotens befassen: wie Sie Ihren Wallet mit ihm verbinden und welche Anwendungen Sie installieren sollten, um ein souveräner Bitcoiner zu werden.





# Anschließen Ihres Wallet an Ihren Knoten


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Indexer: Rolle, Betrieb und Lösungen


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Wenn Sie sich bereits vor diesem Kurs mit Bitcoin-Knoten beschäftigt haben, ist Ihnen vielleicht der Begriff "Indexer" begegnet. Dabei handelt es sich um Werkzeuge wie Electrs oder Fulcrum, die zu einem Bitcoin core-Knoten hinzugefügt werden können. Aber was genau ist ihre Rolle? Wie funktionieren sie in der Praxis? Und sollten Sie einen auf Ihrem neuen Bitcoin-Knoten installieren? Das werden wir in diesem Kapitel untersuchen.



### Was ist ein Indexer?



Im Allgemeinen ist ein Indexer ein Programm, das einen Satz von Rohdaten durchsucht, relevante Schlüssel (z. B. Wörter, Bezeichner und Adressen) extrahiert und eine Hilfsdatei, den so genannten "Index", erstellt, in dem sich jeder Schlüssel auf den genauen Ort der Daten im Korpus bezieht. Diese Vorverarbeitungsphase beansprucht CPU-Zeit und benötigt etwas Speicherplatz, aber es entfällt die Notwendigkeit, den gesamten Korpus bei jeder Abfrage der Datenbank zu verarbeiten; eine einfache Abfrage des Indexes führt zu einer fast sofortigen Antwort.



Für den Laien ist es das gleiche Prinzip wie ein Index in einem Buch: Wenn Sie eine bestimmte Information suchen, müssen Sie nicht das ganze Buch lesen, sondern können im Index direkt die Seite finden, auf der die gesuchte Information steht.



In einem Bitcoin-Knoten, wie Bitcoin core, werden Blockchain-Daten in ihrer rohen, chronologischen Form gespeichert. Jeder Block enthält Transaktionen, die wiederum Eingänge und Ausgänge enthalten, ohne eine besondere Klassifizierung nach Address, Kennung oder Wallet. Diese lineare Organisation ist optimal für die Blockvalidierung, aber ungeeignet für gezielte Suchen. Wenn Sie beispielsweise alle Transaktionen finden wollten, die mit einem bestimmten Address in einem nicht indizierten Knoten verknüpft sind, müssten Sie den gesamten Blockchain Block für Block und Transaktion für Transaktion manuell überprüfen. Genau hier kommt der Indexer auf Ihrem Bitcoin-Knoten ins Spiel.



![Image](assets/fr/085.webp)



Ein Indexer ist ein spezialisiertes Softwareprogramm, das diese Masse von Rohdaten (Blockchain, Mempool, UTXO) analysiert und Schlüssel wie Transaktionskennungen, Adressen und Blockhöhen extrahiert. Aus diesen Schlüsseln baut es seinen Index auf, wobei es jeden Schlüssel mit dem genauen Speicherort der Informationen im Knotenpunkt verbindet.



![Image](assets/fr/086.webp)



Die Indizierung ermöglicht es Ihnen, schnell, genau und effizient nach Informationen über Ihren Knoten zu suchen. Wenn Sie z. B. einen Wallet wie Sparrow an Ihren Knoten anschließen, kann dieser fast sofort den Saldo eines Address anzeigen. Konkret fragt er den Indexer mit einer Anfrage wie: "_Welche UTXOs sind mit diesem Skript-Hash verbunden?_" Der Indexer antwortet fast sofort, ohne den gesamten Blockchain neu lesen zu müssen, da diese Daten bereits in seiner Datenbank aufgeführt sind.



### Hat der Bitcoin core einen Indexer?



Ohne die Notwendigkeit zusätzlicher Software bietet Bitcoin core streng genommen keinen vollständigen Address Indexer, der mit Software wie Electrs oder Fulcrum vergleichbar ist. Dennoch enthält es mehrere interne Indizierungsmechanismen sowie optionale Optionen zur Erweiterung seiner Abfragemöglichkeiten. Um die Situation vollständig zu verstehen, müssen wir einen Abstecher in die Geschichte des Projekts machen.



Bis Bitcoin core Version 0.8.0 basierte die Transaktionsvalidierung auf einem globalen Transaktionsindex, der als "txindex" bekannt war. Dieser Index verwies auf alle Blockchain-Transaktionen und ihre Ausgaben. Wenn ein Knoten eine neue Transaktion erhielt, konsultierte er diesen Index, um zu überprüfen, ob die verbrauchten Ausgaben (in Eingaben) tatsächlich existierten und nicht bereits ausgegeben worden waren. daher war "txindex" seinerzeit für die Validierung von Transaktionen unerlässlich.



Dieser Ansatz hatte jedoch seine Grenzen: Er war langsam, kostspielig in Bezug auf die Speicherung und redundant in Bezug auf die Informationen. Um hier Abhilfe zu schaffen, wurde in Version 0.8.0 eine Überarbeitung des Validierungsmodells namens ***Ultraprune*** eingeführt. Anstatt alles in Form von Transaktionsindizes zu speichern, unterhält Bitcoin core eine einfache Datenbank, die ausschließlich UTXOs gewidmet ist, genannt `chainstate` (in der Alltagssprache als "UTXO set" bekannt), und aktualisiert ihre Liste, wenn Ausgaben verbraucht und erstellt werden.



Diese Methode ist viel schneller und speichert nur den aktuellen Zustand des Registers, was den Indexer "txindex" überflüssig macht. Anstatt jedoch den `txindex`-Code zu löschen, haben sich die Entwickler dafür entschieden, diese Funktionalität hinter einem einfachen Parameter (`txindex=1`) zu belassen. Wenn Sie diese Option auf Ihrem Knoten aktivieren, können Sie jede Transaktion von seinem `txid` abfragen.



Entgegen der landläufigen Meinung bietet Bitcoin core keine Address-basierte Indexierung wie Electrs oder Fulcrum. Für diese Entscheidung gibt es mehrere Gründe:





- Die Rolle von Bitcoin core besteht nicht darin, ein komplettes Block explorer zu werden oder eine auf die jeweilige Verwendung zugeschnittene API bereitzustellen. Die Integration eines Address-basierten Index würde eine langfristige Commitment-Wartung erfordern, die über den ursprünglichen Anwendungsbereich der Software hinausgeht.





- Die meisten Anwendungsfälle können bereits auf andere Weise abgedeckt werden. Um beispielsweise den Saldo eines Address zu schätzen, können Sie den Befehl `scantxoutset` verwenden, der den UTXO-Satz direkt abfragt, ohne dass ein vollständiger Index erforderlich ist.





- Jedes Softwareprogramm hat spezifische Anforderungen an das Format oder die Art der zu indizierenden Daten (Address, Hash-Skript, proprietäres Tag usw.). Es ist flexibler und logischer, diese Programme ihre eigenen angepassten Indizes erstellen zu lassen, als eine generische Lösung in Bitcoin core festzulegen.



Bitcoin core verfügt zwar über einen optionalen Transaktionsindexer (`txindex`), ein Überbleibsel seines historischen Betriebs, aber er bietet weder einen Address-Index noch einen direkten Interface für komplexe Suchvorgänge. In einigen Fällen kann es daher sinnvoll sein, einen externen Indexer hinzuzufügen.



### Sollten Sie einen Address-Indexer zu Ihrem Knoten hinzufügen?



Das Hinzufügen eines Address-Indexierers, z. B. von Electrs oder Fulcrum, ist nicht zwingend erforderlich; es hängt von Ihren spezifischen Anforderungen ab.



Wenn Sie einfach nur einen Wallet, wie z. B. Sparrow, mit Ihrem Knoten verbinden möchten, um die Salden einzusehen und Transaktionen zu übertragen, ist dies direkt über den Interface RPC des Bitcoin core möglich, entweder lokal oder aus der Ferne über Tor.



Auf der anderen Seite, um mehr fortgeschrittene Software, wie z. B. mit einem Mempool.Locally, die Installation eines Address Indexer wird für den Raum Block explorer unerlässlich.



Der Indexer benötigt eine gewisse Zeit für die Synchronisierung (weniger als die IBD) und belegt zusätzlichen Speicherplatz. Wenn Ihre SSD nach dem Herunterladen von Blockchain noch genügend freien Speicherplatz hat, können Sie problemlos einen Indexer hinzufügen.



### Welcher Indexer soll gewählt werden?



Zwei Softwareprogramme werden üblicherweise verwendet, um diese Art von Address-Index zu erstellen und zugänglich zu machen: **Electrs** und **Fulcrum**. Diese Tools indizieren die Blockchain nach Script-Hash (Adressen) und schlagen dann ein standardisiertes Interface (das Electrum-Protokoll) vor, mit dem sich zahlreiche Wallets wie Electrum Wallet, Sparrow oder Phoenix verbinden.



![Image](assets/fr/087.webp)



Einfach ausgedrückt ist Electrs recht kompakt: Es indiziert Blockchain schneller und nimmt weniger Speicherplatz in Anspruch, ist aber bei Abfragen etwas weniger leistungsfähig als Fulcrum. Im Gegensatz dazu verbraucht Fulcrum mehr Speicherplatz und braucht länger für die Indizierung, bietet aber eine bessere Abfrageleistung.



Für den individuellen Gebrauch empfehle ich Electrs: Es verbraucht weniger Speicherplatz, wird gut gewartet und ist zwar bei bestimmten Anfragen etwas langsamer als Fulcrum, aber für den täglichen Gebrauch immer noch mehr als ausreichend. Wenn Sie die Zeit und den Speicherplatz haben, können Sie auch Fulcrum ausprobieren, das vor allem bei Geldbörsen mit vielen zu überprüfenden Adressen deutlich besser abschneidet.



Konkret bedeutet dies, dass Electrs im August 2025 etwa 56 GB Speicherplatz benötigt, Fulcrum dagegen etwa 178 GB. Die Wahl Ihres Indexers hängt also auch von Ihrer Speicherkapazität ab:




- Wenn Ihr Festplattenplatz sehr begrenzt ist, müssen Sie sich mit dem Bitcoin core ohne einen externen Address-Indexer begnügen.
- Wenn Sie einen Indexer verwenden möchten, aber dennoch Kapazitätsengpässe haben, entscheiden Sie sich für Electrs.
- Wenn Sie über ausreichend Speicherplatz verfügen, könnte Fulcrum genau das Richtige für Sie sein.



Für den Rest dieses BTC 202-Kurses werde ich Electrs verwenden, aber Sie können einfach mit Fulcrum weitermachen: Die Installationsprozedur ist identisch, ebenso wie die Verbindung des Interface mit dem Wallet, da beide einen Electrum-Server bereitstellen.



### Wie installiere ich einen Indexer auf Umbrel?



Um Electrs (oder Fulcrum) auf Ihrem Umbrel zu installieren, ist das Verfahren einfach: Gehen Sie zum App Store, suchen Sie nach der entsprechenden Anwendung (auf der Registerkarte Bitcoin) und klicken Sie dann auf die Schaltfläche "*Installieren*".



![Image](assets/fr/028.webp)



Sobald die Installation abgeschlossen ist, beginnt Electrs mit einer Synchronisierungsphase (Indizierung), die mehrere Stunden dauern kann.



![Image](assets/fr/029.webp)



Sobald die Synchronisierung abgeschlossen ist, können Sie Ihre Wallet-Software mit Ihrem Electrum-Server verbinden, der auf Umbrel gehostet wird.



## Wie verbinde ich mein Wallet mit meinem Bitcoin-Knoten?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Nun, da Sie einen vollständigen Bitcoin-Knoten haben, ist es an der Zeit, ihn sinnvoll zu nutzen! Im nächsten Kapitel werden wir weitere Verwendungsmöglichkeiten für Ihre Umbrel-Instanz untersuchen. Lassen Sie uns jedoch mit den Grundlagen beginnen: die Anbindung Ihrer Wallet Software, um Informationen von Ihrem eigenen Blockchain zu nutzen und Transaktionen über Ihren eigenen Knoten zu verteilen.



Wie bereits erwähnt, gibt es zwei Hauptverbindungsschnittstellen:




- Direkte Verbindung zum Bitcoin core über RPC;
- Oder verbinden Sie sich mit einem Electrum-Server (Electrs oder Fulcrum).



In diesem Tutorial konzentrieren wir uns auf die Verbindung zu deinem Knoten über Tor, da dies eine einfache und sichere Lösung für Anfänger ist. Ich rate dringend davon ab, den RPC-Port deines Knotens offen zu legen, da eine Fehlkonfiguration ein erhebliches Risiko für die Sicherheit und Vertraulichkeit deiner Daten darstellt. Der größte Nachteil der Kommunikation über Tor ist seine Langsamkeit. Im nächsten Kapitel werden wir eine schnelle und sichere Alternative zu Tor für den Fernzugriff auf Ihren Knoten erkunden: VPN.



Wir verwenden in diesem Kapitel Sparrow als Beispiel, aber das Verfahren ist für alle anderen Wallet-Verwaltungssoftware, die Verbindungen zu Electrum-Servern akzeptiert, gleich. Suchen Sie einfach die entsprechende Einstellung in den Parametern Ihrer Anwendung (normalerweise unter "*Server*", "*Netzwerk*", "*Knoten*"...).



Öffnen Sie auf dem Sparrow die Registerkarte "*Datei*" und gehen Sie in das Menü "Einstellungen".



![Image](assets/fr/030.webp)



Klicken Sie dann auf "*Server*", um die Verbindungsparameter aufzurufen.



![Image](assets/fr/031.webp)



Sie werden dann drei Optionen für die Verknüpfung Ihrer Software mit einem Bitcoin-Knoten entdecken:




- Öffentlicher Server* (gelb): Wenn Sie keinen Bitcoin-Knoten besitzen, verbindet Sie diese Option standardmäßig mit einem öffentlichen Knoten, der Ihnen nicht gehört (normalerweise der eines Unternehmens). Diese Option ist hier nicht relevant, da Sie Ihren eigenen Knoten auf Umbrel haben.
- Bitcoin core* (Green): Diese Option entspricht der Verbindung über Interface RPC, d. h. direkt mit Bitcoin core.
- Private Electrum* (blau): Mit dieser Option können Sie eine Verbindung über den Interface Electrum Server (Electrs oder Fulcrum) Ihres Indexers herstellen.



### Anschluss an Bitcoin core RPC



Wenn Ihr Umbrel-Knoten keinen Indexer hat, müssen Sie diese Option wählen. Auf Sparrow klicken Sie auf "*Bitcoin core*".



![Image](assets/fr/032.webp)



Sie müssen dann mehrere Informationen eingeben, um die Verbindung zu Ihrem Knoten herzustellen. Alle diese Daten können über die Anwendung "*Bitcoin Node*" auf Umbrel abgerufen werden, indem Sie auf die Schaltfläche "*Verbinden*" in der oberen rechten Ecke des Interface klicken.



![Image](assets/fr/033.webp)



Die Registerkarte "*RPC Details*" zeigt alle notwendigen Informationen für die Verbindung an. Wählen Sie eine Verbindung über Tor Address (in `.onion`).



![Image](assets/fr/034.webp)



Geben Sie diese Daten in die entsprechenden Felder des Sparrow wallet ein und klicken Sie dann auf die Schaltfläche "*Test Connection*".



![Image](assets/fr/035.webp)



Wenn die Verbindung erfolgreich ist, erscheinen ein Green-Häkchen und eine Bestätigungsmeldung.



![Image](assets/fr/036.webp)



Das Häkchen unten rechts auf dem Interface Sparrow wallet wird nun zu Green (was eine direkte Verbindung zu Bitcoin core anzeigt).



**Hinweis:** Damit die Verbindung erfolgreich hergestellt werden kann, muss Ihr Knoten zu 100% synchronisiert sein. Wenn dies nicht der Fall ist, warten Sie bitte bis zum Ende des IBD.



### Verbindung zu Electrs



Wenn Ihr Knoten über einen Indexer verfügt, ist es besser, sich mit diesem zu verbinden, als Bitcoin core direkt zu verwenden, da Ihre Abfragen dann schneller verarbeitet werden.



Gehen Sie im Sparrow auf die Registerkarte "*Private Electrum*".



![Image](assets/fr/037.webp)



Sie müssen dann einige Informationen eingeben, um die Verbindung mit Ihrem Indexer herzustellen. Sie finden diese Daten in der Anwendung "*Electrs*" (oder ggf. "*Fulcrum*") auf Umbrel.



Wählen Sie die Registerkarte "*Tor*", um die `.onion`-Verbindung Address zu erhalten. Wenn Sie eine mobile Wallet-Software anschließen möchten, können Sie auch den QR-Code direkt scannen.



![Image](assets/fr/038.webp)



Gib einfach den Tor Address deines Electrum-Servers in das Feld "*URL*" ein und klicke dann auf die Schaltfläche "*Verbindung testen*".



![Image](assets/fr/039.webp)



Wenn die Verbindung erfolgreich ist, werden ein Häkchen und eine Bestätigungsmeldung angezeigt.



![Image](assets/fr/040.webp)



Das Häkchen in der unteren rechten Ecke des Interface Sparrow wallet wird blau (die Farbe, die mit der Verbindung zu einem Electrum-Server verbunden ist).



**Hinweis:** Damit die Verbindung funktioniert, muss Ihr Indexer zu 100 % synchronisiert sein. Wenn dies nicht der Fall ist, warten Sie, bis der Indizierungsprozess abgeschlossen ist.



Jetzt wissen Sie, wie Sie Ihren Wallet an Ihren Bitcoin-Knoten anschließen können! Im nächsten Kapitel werde ich Ihnen einige zusätzliche Anwendungen vorstellen, die auf Umbrel verfügbar sind, die ich besonders schätze und die es Ihnen ermöglichen, Ihre tägliche Nutzung des Bitcoin über Ihren Knoten zu verbessern.




## Übersicht der verfügbaren Anwendungen


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel bietet einen umfangreichen Anwendungsspeicher. Wie Sie sehen werden, gibt es viele Tools im Zusammenhang mit Bitcoin, aber auch eine Vielzahl von Anwendungen in sehr unterschiedlichen Bereichen: Self-Hosting-Lösungen für Dienste und Dateien, Produktivitätsanwendungen, allgemeinere Finanztools, Medienmanagement, Netzwerksicherheit und -verwaltung, Entwicklung, künstliche Intelligenz, soziale Netzwerke und sogar Heimautomatisierung.



In diesem BTC 202-Kurs werden wir uns ausschließlich auf Bitcoin-bezogene Anwendungen konzentrieren. Sie können jedoch auch den Rest des Katalogs nach Tools durchsuchen, die für Sie von Nutzen sein könnten.



Es wäre natürlich unmöglich, hier alle Bitcoin-Anwendungen aufzulisten. In diesem Kapitel möchte ich Ihnen die wichtigsten Werkzeuge vorstellen, die Ihre tägliche Arbeit mit Bitcoin erleichtern und bereichern werden.



### Mempool.space



Wenn es bei der täglichen Arbeit mit Bitcoin ein Werkzeug gibt, das wirklich unverzichtbar ist, dann ist es Block explorer. Ob online zugänglich oder lokal installiert, es wandelt die Rohdaten des Blockchain in ein strukturiertes, klares und leicht zu lesendes Format um. Es verfügt auch über eine Suchmaschine, mit der Benutzer schnell einen bestimmten Block, eine Transaktion oder Address finden können.



Konkret können Sie mit dem Explorer die Gebühren abschätzen, die für die Aufnahme Ihrer Transaktion in einen Block erforderlich sind, dann ihren Fortschritt verfolgen: Sie können herausfinden, ob sie je nach Gebührenmarkt wahrscheinlich in naher Zukunft aufgenommen wird, und schließlich bestätigen, dass sie tatsächlich in einen Block aufgenommen wurde. Es bietet auch die Möglichkeit, Ihre vergangenen Transaktionen zu analysieren und deren Historie einzusehen. Kurz gesagt, es ist das Schweizer Taschenmesser des Bitcoiners.



Wie bereits erwähnt, kann ein Explorer online auf einer Website gehostet oder lokal auf Ihrem Rechner ausgeführt werden. Ein großer Nachteil von Online-Diensten ist, dass sie Ihre Privatsphäre gefährden können. Ohne VPN oder Tor kann der Server, auf dem der Explorer gehostet wird, Ihre IP-Adresse Address mit den von Ihnen angezeigten Transaktionen verknüpfen, was einen idealen Einstiegspunkt für Kettenanalysen darstellen kann.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Darüber hinaus kann Ihr Internetdienstanbieter (ISP) wissen, dass Sie eine bestimmte Transaktion über die Block explorer-Website abrufen. Dies wirft auch eine Vertrauensfrage auf: Sie müssen sich darauf verlassen, dass der Online-Dienst Ihnen genaue Informationen über Ihre Transaktionen liefert, ohne dass Sie deren Wahrheitsgehalt selbst überprüfen können.



Deshalb ist es immer am besten, Ihren eigenen lokalen Block explorer zu verwenden. Auf diese Weise können keine Daten über Ihre Suchaktivitäten nach außen dringen, da alle Abfragen direkt auf einem von Ihnen kontrollierten Rechner verarbeitet werden, ohne das Internet zu durchlaufen. Darüber hinaus stützt sich ein lokaler Explorer auf die Daten Ihres eigenen Bitcoin-Knotens, den Sie selbst nach Ihren eigenen Regeln validiert haben und dem Sie vertrauen können.



Umbrel bietet mehrere Blockexplorer an:




- Mempool.Space
- Bitfeed
- BTC RPC Entdecker



Besonders angetan bin ich von Mempool.Space, das ich auf meinem Knoten installiert habe. Bitte beachten Sie: um die meisten Block-Explorer auf Umbrel zu benutzen, ist ein Address Indexer erforderlich. Sie benötigen also die Anwendung Bitcoin Node (oder Bitcoin Knots), die einen 100% synchronisierten Blockchain hat, sowie einen Indexer wie Electrs oder Fulcrum, der ebenfalls 100% synchronisiert ist.



Sobald die Anwendung installiert ist, öffnen Sie sie einfach, um auf Ihren eigenen Explorer zuzugreifen.



![Image](assets/fr/041.webp)



Um mehr über die Verwendung des Mempool.Space Explorers zu erfahren, empfehle ich dieses umfassende Tutorial:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Blitzknoten



Jetzt, da Sie Ihren eigenen Bitcoin-Knoten haben, können Sie auch Ihren eigenen Lightning-Knoten einrichten, um off-chain-Transaktionen durchzuführen, ohne auf die Infrastruktur eines Dritten angewiesen zu sein.



Umbrel bietet eine Reihe von Anwendungen, die Ihnen helfen, Ihren Lightning-Knoten zum Laufen zu bringen. Sie können bereits zwischen zwei Hauptimplementierungen wählen:




- LND, über die Anwendung *Lightning Node*;
- Core Lightning.



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Sie können Ihren Knoten dann vom Haupt-Interface aus verwalten, oder, für noch mehr Funktionalität und erweiterte Optionen, *Ride The Lightning* oder *ThunderHub* installieren. Diese Tools bieten Ihnen ein viel umfassenderes webbasiertes Interface-Verwaltungssystem für Ihren Knoten.



https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Schließlich empfehle ich die Anwendung *Lightning Network+*, mit der Sie Gleichgesinnte finden können, mit denen Sie Kanäle öffnen können, die sowohl ausgehende als auch eingehende Bargeldtransaktionen ermöglichen.



![Image](assets/fr/089.webp)



Dank Umbrel ist die Verwaltung eines persönlichen Lightning-Knotens stark vereinfacht worden, aber sie ist immer noch relativ komplex. Aus diesem Grund werden wir dieses Thema in einem zukünftigen Kurs, der sich ausschließlich mit dieser Anwendung befasst, näher beleuchten.



### Heckwaage



Eine weitere Anwendung, die ich bei Umbrel besonders mag, ist Tailscale. Dabei handelt es sich um eine VPN-Anwendung, die die Einrichtung sicherer Netzwerke zwischen mehreren Geräten vereinfacht, egal wo auf der Welt sie sich befinden. Im Gegensatz zu herkömmlichen VPNs, die sich auf zentrale Server stützen, nutzt Tailscale das WireGuard-Protokoll, um verschlüsselte End-to-End-Verbindungen zwischen Ihren verschiedenen Geräten herzustellen. Das bedeutet, dass Sie ein funktionierendes VPN in nur wenigen Minuten einrichten können, ohne komplizierte Netzwerkkonfigurationen vornehmen zu müssen.



Bei Umbrel verbindet die Tailscale-Installation Ihren Bitcoin-Knoten mit Ihrem eigenen virtuellen privaten Netzwerk. Einmal konfiguriert, erhält Ihr Knoten eine private Tailscale-IP Address, auf die nur andere Geräte zugreifen können, die mit demselben Tailscale-Netzwerk verbunden sind (wie Computer, Smartphones und Tablets). Diese Verbindung ist Ende-zu-Ende verschlüsselt und läuft nicht durch ein ungeschütztes öffentliches Netzwerk, was die Sicherheit im Vergleich zu einer unverschlüsselten Verbindung deutlich erhöht.



![Image](assets/fr/090.webp)



Konkret bietet Ihnen Tailscale bei der Nutzung Ihres Umbrel mehrere Vorteile:





- Du kannst den Interface Umbrel verwalten oder auf die mit deinem Knoten verbundenen Anwendungen (wie Mempool, Ride The Lightning, ThunderHub...) von überall aus zugreifen, als wärst du im selben lokalen Netzwerk, ohne Ports im Internet freizugeben und ohne durch Tor zu gehen, was sehr langsam ist;





- Sie können sich mit Ihrem Electrum-Server (Electrs oder Fulcrum) oder direkt mit Bitcoin core über Ihr VPN verbinden und dabei Tor umgehen. Dies bietet eine sichere Verbindung, vergleichbar mit der Verwendung von Tor, aber mit viel höherer Geschwindigkeit und geringerer Latenz. Kurz gesagt, Sie behalten die Datenschutz- und Sicherheitsvorteile von Tor, während Sie die Geschwindigkeit einer Clearnet-Verbindung genießen. Für einen On-Chain Wallet mag dieser Gewinn marginal erscheinen, aber wenn Sie planen, später einen eigenen Lightning-Knoten einzurichten, ist der Unterschied beträchtlich. In der Tat ist die Durchführung von Zahlungen über Ihren Knoten unterwegs auf Tor aufgrund der zahlreichen erforderlichen Austauschvorgänge extrem langsam, während es mit Tailscale perfekt funktioniert.





- Sie müssen keine NAT-Regeln konfigurieren, keine Ports öffnen oder einen herkömmlichen VPN-Server einrichten. Sobald die Anwendung auf Umbrel und Ihren Geräten installiert ist, wird das Netzwerk automatisch aufgebaut.



Tailscale on Umbrel ist daher eine sehr interessante Lösung, wenn Sie von überall auf der Welt auf Ihren Knoten zugreifen wollen, und zwar auf eine sichere, leistungsstarke und einfach zu konfigurierende Art und Weise, ohne dabei die Privatsphäre oder die Sicherheit zu opfern.



Um Tailscale auf Ihrem Umbrel zu installieren und zu konfigurieren, lesen Sie dieses Tutorial, Abschnitt 4: "*Tailscale auf Umbrel verwenden*":



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, ein Akronym für "*Notes and Other Stuff Transmitted by Relays*", ist ein offenes, dezentralisiertes Protokoll, mit dem Nachrichten im Internet veröffentlicht und ausgetauscht werden können, ohne von einer zentralen Plattform abhängig zu sein. Jeder Benutzer verfügt über ein Paar kryptografischer Schlüssel: den öffentlichen Schlüssel (`npub`), der als Identifikator dient, und den privaten Schlüssel (`nsec`), der zum Signieren von Nachrichten und zur Gewährleistung ihrer Authentizität verwendet wird.



Die Nachrichten werden über ein Netz unabhängiger Relays übertragen. Diese verteilte Architektur macht Nostr resistent gegen Zensur: kein einzelner Server kontrolliert den Zugang oder die Verteilung, und ein Benutzer kann sich mit so vielen Relais verbinden, wie er möchte.



Dieses Protokoll ist in der Bitcoin-Gemeinschaft sehr beliebt, da Nostr wie Bitcoin Fragen der digitalen Souveränität und Datenkontrolle behandelt. Sein Schöpfer, Fiatjaf, ist ein Entwickler, der im Ökosystem bereits für seine zahlreichen Beiträge bekannt ist.



Mit deinem Umbrel kannst du deine Nutzung von Nostr optimieren. Durch die Installation der ***Nostr Relay***-Anwendung kannst du dein eigenes privates Relay direkt auf deinem Rechner hosten und so sicherstellen, dass alle deine Beiträge und Interaktionen auf Nostr lokal gespeichert werden und nicht durch das Löschen durch öffentliche Relays verloren gehen können.



Die Nostr-Clients ***noStrudel*** oder ***Snort*** sind ebenfalls auf Umbrel verfügbar. Dank dieser Anwendungen können Sie Profile veröffentlichen, lesen, suchen und mit dem Nostr-Ökosystem direkt vom Interface Web auf Ihrem Umbrel interagieren.



Schließlich gibt es noch die ***Nostr Wallet Connect*** App auf Umbrel, die native Lightning-Zahlungen in Nostr ermöglicht. Konkret können Sie Ihren zukünftigen Lightning-Knoten mit Ihren Nostr-Kunden verknüpfen, um Mikrozahlungen, genannt "*zaps*", zu senden, um Inhalte zu belohnen oder auf monetäre Weise zu interagieren, ohne dass Sie einen Drittanbieter-Service in Anspruch nehmen müssen. Diese Zahlungen werden direkt von Ihrem persönlichen Knotenpunkt über Ihre Kanäle gesendet.



Um herauszufinden, wie Sie all diese Anwendungen nutzen können, empfehle ich Ihnen, einen Blick auf diese vollständige Anleitung zu werfen:



https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### BTCPay-Server



BTCPay Server ist ein kostenloser Open-Source-Zahlungsprozessor, der es Ihnen ermöglicht, Zahlungen über Bitcoin und Lightning Network ohne Zwischenhändler zu akzeptieren, während Sie die Gelder selbst verwahren können.



Die Architektur von BTCPay Server basiert auf einem Bitcoin-Knoten und für Lightning auf einer kompatiblen Implementierung (LND, Core Lightning...), was es zu einer der einzigen PoS-Lösungen macht, die vollständig ohne Verwahrung auskommt. Es ist auch die umfassendste Software für Tracking und Buchhaltung.



![Image](assets/fr/091.webp)



Wenn Sie ein Unternehmen besitzen und Bitcoin-Zahlungen direkt über Ihren Umbrel-Knoten akzeptieren möchten, ist die BTCPay Server-Anwendung ideal für Sie. Um mehr über dieses Thema zu erfahren, empfehle ich Ihnen, die folgenden Ressourcen zu konsultieren:





- Der BIZ 101-Kurs zum Einsatz von Bitcoin in Ihrem Unternehmen:



https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- Der POS 305 Kurs zur Nutzung des BTCPay Servers:



https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- Das BTCPay Server-Tutorial:



https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Fortgeschrittene Konzepte und bewährte Verfahren


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Pflege des Regenschirmknotens


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Zum Auftakt dieses letzten Abschnitts und bevor wir uns der fortgeschrittenen Theorie zuwenden, möchte ich in diesem kurzen Kapitel auf die besten Praktiken und konkreten Maßnahmen eingehen, die Sie ergreifen können, sobald Ihr Umbrel-Knoten installiert, synchronisiert und korrekt konfiguriert ist. Wie pflegen Sie ihn täglich?



### Gesunderhaltung der Ausrüstung



Ein zuverlässiger Knoten beginnt mit stabiler Hardware. Stellen Sie sicher, dass das Gerät, in dem Ihr Knoten untergebracht ist, gut belüftet, Dust-frei und in einer trockenen Umgebung installiert ist, fern von Wärme- und Feuchtigkeitsquellen. Vermeiden Sie es, ihn in einen engen Raum zu quetschen und wählen Sie einen gut belüfteten Standort.



Bei Raspberry Pi und Mini-PCs verstopft Dust schließlich die Kühlkörper, wodurch die Temperatur ansteigt und es zu einer Drosselung (freiwillige Begrenzung der Ressourcennutzung) kommt, was wiederum zu einem Rückgang der Effizienz Ihres Knotens führt. Deshalb empfehle ich, den Lufteinlass und den Lüfter regelmäßig zu reinigen, am besten alle paar Monate.



Achten Sie darauf, dass Sie ein hochwertiges Netzgerät Supply verwenden, da eine instabile Spannung zu einer Beschädigung des Systems führen und sogar eine Brandgefahr darstellen kann. Idealerweise sollten Sie das vom Hersteller Ihres Geräts gelieferte Originalnetzteil Supply verwenden. Achten Sie auch auf die Überhitzungsgefahr durch den Joule-Effekt bei Steckdosenleisten: Beachten Sie immer die maximal zulässige Leistung und schließen Sie niemals mehrere Steckdosenleisten in Kaskade an.



Ich empfehle auch, in eine USV zu investieren. Diese schützt Ihren Knoten vor plötzlichen Abschaltungen, ermöglicht Umbrel ein sauberes Herunterfahren im Falle eines Ausfalls und gewährleistet die Kontinuität des Betriebs bei Mikroausfällen oder kurzfristigen Störungen.



Auf der Speicherseite sollten Sie den Fortschritt im Auge behalten: Wenn sich die Festplatte der Sättigung nähert, sollten Sie erwägen, Speicherplatz freizugeben (Deinstallation ungenutzter Anwendungen, Anpassung der Indexer-Einstellungen) oder auf eine größere SSD zu migrieren. Der Nachteil eines vollen Bitcoin-Knotens ist, dass sein Speicherbedarf kontinuierlich steigt, da alle 10 Minuten ein neuer Block erzeugt wird und alte Blöcke nicht gelöscht werden können (es sei denn, der Knoten ist pruned). Ich rate Ihnen daher, beim Kauf Ihrer Hardware eine ausreichend große Kapazität einzuplanen (mindestens 2 TB).



### Update



Node-Updates sind aus drei Gründen wichtig: erstens für die Sicherheit (Patches für Sicherheitslücken, Netzwerkhärtung und DoS-Schutz), zweitens für die Kompatibilität (Änderungen der Relay-Policy, Formatänderungen und Protokoll-Upgrades) und drittens für die Zuverlässigkeit und Leistung (Fehlerbehebungen, Ressourcenverbrauch und andere Verbesserungen). Prüfen Sie also regelmäßig, ob UmbrelOS und Ihre Anwendungen auf dem neuesten Stand sind:





- So aktualisieren Sie das System: Öffnen Sie das Einstellungsmenü und klicken Sie auf die Schaltfläche "*Aktualisierung prüfen*" neben dem Parameter "*UmbrelOS*".



![Image](assets/fr/042.webp)





- So aktualisieren Sie Anwendungen: Rufen Sie den App Store auf. Wenn eine Ihrer Anwendungen aktualisiert werden muss, erscheint in der oberen rechten Ecke des Interface eine Schaltfläche mit einer roten Blase. Klicken Sie einfach darauf und aktualisieren Sie dann jede Anwendung.



Führen Sie diesen Vorgang regelmäßig durch, um Ihr Betriebssystem und Ihre Anwendungen auf dem neuesten Stand zu halten.



### Backups



Wenn du deinen Bitcoin Knoten nur zur Validierung und Verteilung deiner Transaktionen verwendest, deine Wallets aber außerhalb von Umbrel verwaltet werden (z.B. mit einem Hardware Wallet und Sparrow wallet), gibt es nichts, was du direkt in Umbrel sichern musst. In diesem Fall bleibt das wesentliche Backup das der Recovery Phrase und des Descriptor deines externen Wallet, und das gilt unabhängig davon, ob du deinen eigenen Node benutzt oder nicht. Es ändert sich also nichts an Ihrer bisherigen Konfiguration.



Andererseits können je nach den zusätzlichen Anwendungen, die Sie auf Umbrel verwenden, weitere Backups erforderlich sein. Dies ist insbesondere dann der Fall, wenn Sie einen Lightning-Knoten auf Umbrel betreiben. In diesem Fall ist es unbedingt notwendig, das seed, das bei der Installation des Lightning-Knotens mitgeliefert wurde, zu sichern. Zusätzlich zum seed benötigen Sie ein aktuelles ***Static Channel Backup (SCB)***, um Ihren Lightning-Knoten im Falle eines Problems wiederherstellen zu können. Mit SCB können Sie Ihre Gelder wiederherstellen, indem Sie Kanäle zwangsweise schließen. Wenn entweder der seed oder die SCB fehlt, ist es unmöglich, einen Lightning-Knoten wiederherzustellen.



Umbrel bietet auch die Möglichkeit, diese SCB automatisch und dynamisch über Tor auf ihren Servern zu sichern, um sicherzustellen, dass immer eine aktuelle Datei verfügbar ist. In diesem Fall wird nur der seed benötigt, um den Knoten wiederherzustellen.



Wir werden diese Aspekte im nächsten LNP202-Kurs noch einmal im Detail behandeln.



### Sicherheit im Tagesgeschäft



Was die Sicherheit betrifft, verwenden Sie ein langes, eindeutiges und zufälliges Passwort für Interface Umbrel und denken Sie daran, die Zwei-Faktor-Authentifizierung (2FA) zu aktivieren. Bei Anwendungen, die sowohl einen Passwort- als auch einen 2FA-Schutz bieten, aktivieren Sie immer beide und ändern Sie die Standardpasswörter.



Stellen Sie das Dashboard niemals ins Internet, ohne ein sicheres Gateway zu verwenden (z. B. VPN, Tor oder nur lokaler Zugang). Begrenzen Sie die Anzahl der Anwendungen, die Sie installieren, und löschen Sie regelmäßig die Anwendungen, die Sie nicht mehr benötigen, um die Angriffsfläche zu verringern.



Um Ihr Wissen über Computersicherheit im Allgemeinen zu vertiefen, empfehle ich Ihnen, diesen anderen kostenlosen Kurs zu besuchen:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Diagnose und Selbsthilfe



Im Falle eines Fehlers auf Ihrem Umbrel, starten Sie zuerst generate ein Diagnosepaket über die Troubleshooting-Sektion von UmbrelOS oder der betreffenden Anwendung, dann starten Sie die Anwendung sauber neu. Versuchen Sie ggf. auch einen kompletten Neustart des Systems.



Wenn das Problem weiterhin besteht, empfehle ich Ihnen, [der Umbrel-Benutzergemeinschaft auf deren Discord beizutreten] (https://discord.gg/efNtFzqtdx). Beginne mit einer Suche, um herauszufinden, ob jemand bereits auf das gleiche Problem gestoßen ist und eine Lösung gefunden hat. Wenn nicht, kannst du eine Nachricht im Channel "Allgemeine Unterstützung" posten. Du kannst auch [das Umbrel-Forum](https://community.umbrel.com/) benutzen.



In diesen Bereichen können Sie nicht nur Sicherheitsankündigungen und -aktualisierungen verfolgen, sondern auch Fragen stellen und letztlich anderen Benutzern helfen. Oft werden bei diesem Austausch bewährte Verfahren entdeckt.



Mit diesen einfachen Gewohnheiten wird Ihr Umbrel-Knoten stabil, sicher und nützlich bleiben, sowohl für Sie als auch für das Bitcoin Netz.




## IBD und den Peer-Discovery-Prozess verstehen


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Ihr Bitcoin-Knoten wird ohne vorherige Kenntnis der Transaktionshistorie in Betrieb genommen. Zunächst ist er nur ein Computer, auf dem eine Software (Bitcoin core oder ähnlich) läuft. Um ein vollständig synchronisierter und funktionsfähiger Bitcoin-Knoten zu werden, muss er lokal den Zustand des Ledger rekonstruieren, indem er alle Blöcke überprüft, die seit dem Genesis-Block (Block 0, veröffentlicht von Satoshi Nakamoto am 3. Januar 2009) veröffentlicht wurden. Dieser Schritt wird **IBD (_Initial Block Download_)** genannt.



IBD besteht darin, jeden Block und jede Transaktion einzeln herunterzuladen und zu verifizieren, wobei die Konsensregeln angewendet werden, um eine eigene Version des Blockchain zu erstellen. Ziel ist es nicht, einfach eine Kopie ungeprüfter Daten abzurufen, sondern völlig unabhängig zum gleichen Ergebnis zu kommen wie die ehrliche Mehrheit des Netzwerks.



![Image](assets/fr/092.webp)



### IBD-Meilensteine



Die Synchronisierung beginnt mit dem Schritt _**headers-first**_. Ihr Knoten fordert die Folge von Block-Headern von mehreren Peers an und prüft für jeden von ihnen Proof of Work, Schwierigkeitsanpassung, Syntax sowie Timestamp und Versionsnummernregeln. Kurz gesagt, er stellt sicher, dass jeder empfangene Header den Konsensregeln entspricht.



![Image](assets/fr/093.webp)



Zur Erinnerung: Ein Bitcoin-Block besteht aus einem 80-Byte-Header und einer Liste von Transaktionen. Der Fingerabdruck des Blocks wird durch Anwendung eines doppelten SHA-256 Hash auf diesen Header erhalten, der 6 Felder enthält:




- version
- Hash des vorherigen Blocks
- Merkle Root der Transaktionen
- Timestamp (länger als die mittlere Zeit der vorherigen 11 Blöcke)
- schwierigkeitsziel
- Nonce



![Image](assets/fr/094.webp)



Transaktionen werden in eine Merkle Tree übertragen. Dabei handelt es sich um eine Struktur, die eine große Datenmenge (in diesem Fall alle Transaktionen des Blocks) zusammenfasst, indem sie deren Hashes nach und nach zu einer einzigen "Wurzel" aggregiert und so die Zugehörigkeit eines Elements zu der Menge nachweist (und jede Änderung erkennt). Auf diese Weise ändert jede Änderung an einer Transaktion auch die Wurzel des Merkle Tree und damit den Fingerabdruck des Blockkopfes. SegWit hat ein separates zusätzliches Commitment für Cookies (Signaturen) eingeführt, das in der Coinbase platziert wird.



![Image](assets/fr/095.webp)



Dieser _**headers-first**_-Schritt ermöglicht es dem Knoten, den Zweig mit der meisten Arbeit (unabhängig von der Anzahl der Blöcke) zu identifizieren, d. h. den Zweig, auf den sich Bitcoin-Knoten synchronisieren. Sobald dieser Zweig identifiziert ist, lädt der Knoten den Inhalt der Blöcke parallel von mehreren Verbindungen herunter und validiert dann jede Transaktion: Format, Gültigkeit der Skripte (außer `assumevalid=1`), Beträge und das Fehlen von Doppelausgaben. Bei jeder erfolgreichen Prüfung wird der aktuelle Stand der nicht ausgegebenen Münzen (UTXO-Set) in der Datenbank "chainstate/" aktualisiert: ausgegebene Ausgaben werden entfernt, während neue gültige Ausgaben hinzugefügt werden.



Mempool hingegen kommt nur ins Spiel, wenn man sich der Spitze der Kette nähert: Solange der Knoten spät dran ist, hat er keine anstehenden Transaktionen zu speichern.



Sobald die IBD abgeschlossen ist, tritt der Knoten in seine normale Phase ein: Er validiert neue Blöcke, sobald sie veröffentlicht werden, unterhält seinen Mempool mit ausstehenden Transaktionen gemäß seinen Relay-Regeln, leitet Transaktionen und Blöcke weiter und verwaltet etwaige Kettenumstrukturierungen.



### AnnehmenGültig



Bitcoin core enthält einen Mechanismus, der die Zeit bis zur vollen Betriebsbereitschaft eines Knotens verkürzen soll, wobei das Prinzip der autonomen Überprüfung im Wesentlichen beibehalten wird: AssumeValid.



Der Parameter `assumevalid` basiert auf einem vergangenen Referenzblock, dessen Hash in jede Softwareversion integriert ist. Wenn Ihr Knoten während der IBD feststellt, dass sich dieser Block tatsächlich auf dem Zweig mit der meisten Arbeit befindet, kann er die Skriptüberprüfung für alle Transaktionen vor diesem Punkt ignorieren.



Alle anderen Regeln (Blockstruktur, Proof of Work, Größenbeschränkungen, Transaktionsbeträge, UTXOs usw.) werden weiterhin vollständig überprüft. Nur die Berechnung der Skripte vor diesem Referenzblock wird ignoriert. Der Leistungsgewinn ist bei der IBD beträchtlich, da die Überprüfung der Unterschriften einen großen Teil der CPU-Last ausmacht. Nach diesem Referenzblock kehrt die Überprüfung in den normalen Zustand zurück.



Sie können die vollständige Validierung aller Skripte erzwingen, indem Sie diesen Mechanismus deaktivieren, allerdings auf Kosten einer viel längeren IBD, indem Sie den Parameter `assumevalid=0` in der Datei `Bitcoin.conf` verwenden.



### AnnehmenUTXO



ein weiterer vorhandener Parameter ist `assumeutxo`, der jedoch im Gegensatz zu `assumevalid` nicht standardmäßig aktiviert ist. Dieser Mechanismus ermöglicht es der Software, einen Schnappschuss des UTXO-Satzes zusammen mit seinen Metadaten zu laden und ihn vorläufig als Referenzzustand zu betrachten, nachdem überprüft wurde, dass die Header tatsächlich zu dem Blockchain mit der meisten Arbeit führen.



Auf diese Weise wird der Knoten schnell für gängige Zwecke (RPC, Verbindung zu Geldbörsen usw.) einsatzbereit, während er gleichzeitig im Hintergrund die vollständige, geprüfte Rekonstruktion seines eigenen UTXO-Satzes in Angriff nimmt. Sobald diese Phase abgeschlossen ist, wird der anfängliche Schnappschuss durch den lokal rekonstruierten Zustand ersetzt. Dieser Ansatz trennt die schnelle Bereitstellung von Knoten von der vollständigen Überprüfung, ohne letztere zu beeinträchtigen.



### Peer-Erkennung: Wie findet Ihr Knoten das Bitcoin-Netzwerk?



Wenn ein Knoten zum ersten Mal in Betrieb genommen wird, kennt er noch keine Peers. Er muss jedoch andere Bitcoin-Knoten im Internet finden, um Header und dann Blöcke anzufordern, um seinen IBD abzuschließen. Um diese Verbindungen zu initiieren, folgt Bitcoin core einer priorisierten Logik.



![Image](assets/fr/096.webp)



Wenn der Knoten neu gestartet wird, nachdem er bereits benutzt wurde, versucht Core zunächst, die Verbindung zu ausgehenden Gegenstellen wiederherzustellen, die vor dem Herunterfahren registriert wurden, wobei die Informationen in der Datei "anchors.dat" gespeichert sind. Dann konsultiert er sein IP-Address-Buch **`peers.dat`**, in dem die Liste der zuvor angetroffenen Gegenstellen gespeichert ist, um sich erneut mit ihnen zu verbinden. Dies ist einfach eine lokale Datei, die von Core aktualisiert und aufbewahrt wird. Bei einem neuen Knoten, der gerade erst gestartet wurde, sind diese beiden Dateien hingegen leer, da er noch nie mit anderen Bitcoin-Knoten kommuniziert hat.



In diesem Fall fragt die Software _**DNS-Seeds**_ ab. Dabei handelt es sich um [von anerkannten Ökosystementwicklern unterhaltene Server] (https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), die eine Liste von IP-Adressen vermutlich aktiver Knoten zurückgeben. Anhand dieser Adressen kann der neue Knoten seine ersten Verbindungen herstellen und die erforderlichen Daten von der IBD anfordern. Hier ist die Liste der *DNS-Seeds*, die bis heute (August 2025) aktiv sind:




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: "seed.Mainnet.achownodes.xyz"



In den allermeisten Fällen reicht der Schritt *DNS-Seeds* aus, um die ersten Verbindungen mit anderen Knoten herzustellen. Wenn diese Server ausnahmsweise nicht innerhalb von 60 Sekunden antworten, geht der Knoten zu einer anderen Methode über: [eine statische Liste mit über 1.000 Adressen](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) von _Saatknoten_ ist in den Code von Bitcoin core eingebaut und wird regelmäßig aktualisiert. Wenn die ersten beiden Methoden zur Beschaffung von IP-Adressen fehlschlagen, stellt diese letzte Lösung eine erste Verbindung her, von der aus der Knoten dann neue IP-Adressen anfordern kann.



![Image](assets/fr/097.webp)



Als letzten Ausweg können Sie manuell Supply IP-Adressen über die Datei "peers.dat" verwenden, um bestimmte Verbindungen zu erzwingen.



Nach dem Hochfahren diversifiziert der interne Address-Manager die Quellen (separate autonome Netze, Clearnet und Tor sowie verschiedene geografische Gebiete), um das Risiko einer topologischen Isolierung zu verringern. Der Knoten stellt diese ausgehenden Verbindungen her (Verbindungen, die er selbst auswählt und die daher sicherer sind).



Wenn Ihr Knoten an einem offenen Port lauscht (standardmäßig 8333), nimmt er eingehende Verbindungen an. Diese stärken die allgemeine Widerstandsfähigkeit des Netzwerks, indem sie eine Anlaufstelle für neue Knoten bieten, ohne einen besonderen Nutzen für deinen eigenen IBD zu bringen. Wenn dein Knoten auf Tor läuft, bleibt die Logik die gleiche, aber die verwendeten Adressen sind `.onion`-Dienste.




## Anatomie Ihres Bitcoin-Knotens


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Wenn Ihr Knoten seine anfängliche Synchronisierung abgeschlossen hat, speichert er lokal mehrere komplementäre Datensätze, die es ihm ermöglichen, Blöcke und Transaktionen zu validieren, Netzwerk-Peers zu bedienen und unter Beibehaltung seines Zustands schnell neu zu starten. 3 Hauptbausteine sind für einen Knoten unerlässlich:




- gW-402 **Blöcke** auf der Festplatte gespeichert,
- den **UTXO-Satz**, der in einer Schlüssel-Wert-Datenbank verwaltet wird,
- und der **Mempool** wird im RAM gespeichert und periodisch serialisiert.



Darüber hinaus vervollständigen mehrere Hilfsdateien (Peers, Gebührenvoranschläge, Ausschlusslisten, Geldbörsen usw.) das Bild. Lassen Sie uns die Rolle all dieser Dateien entdecken.



### Wo befinden sich die Daten des Knotens tatsächlich?



Bitcoin core speichert seine Daten standardmäßig in einem bestimmten Arbeitsverzeichnis. Unter GNU/Linux befindet sich dieses Verzeichnis normalerweise in `~/.Bitcoin/`, unter Windows in `%APPDATA%\Bitcoin/` und unter macOS in `~/Library/Application Support/Bitcoin/`. Wenn Sie eine Paketlösung verwenden (z. B. innerhalb einer Node-Distribution), kann dieses Verzeichnis an anderer Stelle eingebunden sein, seine Struktur bleibt jedoch gleich. Die wichtigen Unterordner und Dateien, die im Folgenden beschrieben werden, befinden sich weiterhin hier.



![Image](assets/fr/098.webp)



### Die Blöcke



Blockchain ist also eine Sammlung von Blöcken. Ein Full node speichert diese Blöcke als sequentielle Flat Files und unterhält einen parallelen Index zum schnellen Abruf. Bei Bedarf (Reorganisation, Wallet Rescan, Peer-Service) werden diese Daten unverändert wieder eingelesen.



**Hinweis:** Eine Reorganisation oder Resynchronisation ist ein Phänomen, bei dem der Blockchain aufgrund der Existenz konkurrierender Blöcke auf gleicher Höhe eine Änderung seiner Struktur erfährt. Dies geschieht, wenn ein Teil des Blockchain durch eine andere Kette mit einer größeren Menge an angesammelter Arbeit ersetzt wird. Diese Resynchronisationen sind ein natürlicher Teil der Funktionsweise von Bitcoin, bei der verschiedene Schürfer fast gleichzeitig neue Blöcke finden können, wodurch das Bitcoin-Netzwerk in zwei Teile geteilt wird. In solchen Fällen kann sich das Netzwerk vorübergehend in konkurrierende Ketten aufteilen. Wenn eine dieser Ketten mehr Arbeit anhäuft, werden die anderen Ketten von den Knoten aufgegeben, und ihre Blöcke werden als "veraltete Blöcke" oder "verwaiste Blöcke" bezeichnet Dieser Prozess des Ersetzens einer Kette durch eine andere wird als Resynchronisierung bezeichnet.



#### Blk*.dat-Dateien (Rohblockdaten)



Empfangene und validierte Blöcke werden in sequentielle Container mit dem Namen `blkNNNNN.dat` geschrieben, die im Ordner `blocks/` gespeichert werden. Jede Datei wird der Reihe nach gefüllt, bis sie eine maximale Größe von 128 MiB erreicht hat; zu diesem Zeitpunkt öffnet Core die nächste Datei. Darin ist jeder Block im Netzwerkformat serialisiert, wobei ihm ein magischer Bezeichner und eine Länge vorangestellt sind. Diese Organisation ermöglicht ein schnelles Schreiben auf die Festplatte und erleichtert den Blockdienst zur Synchronisierung von Peers.



![Image](assets/fr/099.webp)



Im pruned-Modus speichert der Knoten nur ein aktuelles Fenster dieser Dateien, um den Speicherplatzbedarf zu begrenzen. Er löscht die ältesten "blk*.dat"-Container, sobald das konfigurierte Speicherplatzziel erreicht ist, behält aber genügend Historie bei, um mit der besten bekannten Kette konsistent zu bleiben. Der Index und der UTXO-Satz bleiben normal, so dass die nächsten Transaktionen und Blöcke validiert werden können.



#### Rev*.dat-Dateien (Stornierungsdaten)



Um während einer Reorganisation in der Zeit zurückgehen zu können, speichert Core parallel zu jeder "blk"-Datei eine "revNNNNN.dat"-Datei in "blocks/". Diese Datei enthält die Informationen, die erforderlich sind, um die Auswirkungen eines Blocks auf den UTXO-Satz rückgängig zu machen: für jeden vom Block verbrauchten Ausgang wird der vorherige Zustand des entsprechenden UTXO gespeichert (Menge, Skript, Höhe...). Im Falle eines Blockabbruchs kann der Knoten den vorherigen Zustand schnell wiederherstellen, ohne die gesamte Kette erneut scannen zu müssen.



![Image](assets/fr/100.webp)



#### Blockindex (Blöcke/Index)



Die Suche nach einem Block direkt in den Flat Files wäre zu zeitaufwändig. Core unterhält daher eine LevelDB-Datenbank in `blocks/index/`, die für jeden bekannten Block Metadaten wie Hash, Höhe, Validierungsstatus, `blk`-Datei und Offset auflistet, wo er sich befindet. Wenn ein Peer einen Block anfordert oder wenn eine interne Komponente auf einen bestimmten Block zugreifen muss, ermöglicht dieser Index einen schnellen Zugriff. Ohne diesen Index wären zu viele Operationen erforderlich.



![Image](assets/fr/101.webp)



#### Optionale Indizes (indexes/)



Einige Indizes sind optional und standardmäßig deaktiviert, da sie den Speicherplatzbedarf erhöhen:




- indexes/txindex/`, das wir bereits erwähnt haben, bietet eine Tabelle zur Abbildung von Transaktion → Ort, die es ermöglicht, jede bestätigte Transaktion abzurufen, ohne den Block zu kennen, der sie enthält. Dies ist nützlich für Wallet-Abfragen vom Typ "getrawtransaction", ist aber recht teuer.
- indexes/blockfilter/`, die kompakte Blockfilter (BIP157/158) für Thin Clients enthalten können. Diese Strukturen beschleunigen die clientseitige Überprüfung auf Kosten von zusätzlichem Speicherplatz auf dem Indexer-Knoten.



### UTXO Satz (Kettenzustand)



Das Modell UTXO (*Unspent Transaction Output*) ist die buchhalterische Darstellung von Bitcoin: Jeder nicht ausgegebene Output ist ein verfügbarer "Coin", der als Input für eine zukünftige Transaktion verwendet werden kann.



![Image](assets/fr/102.webp)



Die Gesamtheit all dieser Teile zu einem bestimmten Zeitpunkt T bildet den UTXO-Satz: eine große Liste aller jetzt verfügbaren Teile. Diesen Zustand konsultiert der Knoten, um zu entscheiden, ob eine Transaktion legitime Einheiten ausgibt, die nicht bereits in einer früheren Transaktion verwendet wurden (um Double-spending zu vermeiden).



![Image](assets/fr/103.webp)



Der UTXO-Satz wird im Ordner `chainstate/` als kompakte LevelDB-Datenbank gespeichert. Jeder Teil verbindet einen von der Hash der Transaktion abgeleiteten Schlüssel und den Ausgabeindex mit einem Wert, der Folgendes enthält: den Betrag, die `scriptPubKey`-Sperre, die Höhe des Erstellungsblocks und einen Coinbase-Indikator.



![Image](assets/fr/104.webp)



Der Knoten unterhält einen Speicher-Cache oberhalb von LevelDB, um häufige Lese- und Schreibvorgänge aufzufangen. Mit dem Parameter `dbcache` kann die Größe dieses Caches verändert werden: je größer er ist, desto mehr Speicherzugriffe kommen der IBD und der aktuellen Validierung zugute, allerdings auf Kosten eines höheren RAM-Verbrauchs. Wird ein neuer Block von einem Miner gefunden, löscht der Knoten die von den im Block enthaltenen Transaktionen ausgegebenen (oder verbrauchten) Outputs aus dem UTXO-Satz und fügt die neu erstellten Outputs hinzu.



Theoretisch könnte man eine Transaktion validieren, indem man die Blockhistorie erneut durchsucht, um zu prüfen, ob eine Ausgabe nie getätigt wurde. In der Praxis wäre dies jedoch viel zu zeitaufwändig, da der gesamte Blockchain für jede neue Transaktion gescannt werden müsste. Der Satz UTXO bietet daher die Mindestansicht, die erforderlich ist, um lokal und in angemessener Zeit das Nichtvorhandensein von Double-spending nachzuweisen.



Es sei darauf hingewiesen, dass der UTXO-Satz oft im Mittelpunkt der Bedenken über die Dezentralisierung von Bitcoin steht, da seine Größe natürlich schnell zunimmt. Dies ist zum einen auf den steigenden Preis von Bitcoin zurückzuführen, der die Fragmentierung von Teilen fördert, und zum anderen auf die zunehmende Akzeptanz des Systems: Je mehr Nutzer es gibt, desto größer ist die Nachfrage nach UTXOs.



![Image](assets/fr/105.webp)



Das Wachstum des UTXO-Satzes ergibt sich auch aus der Struktur des einfachen Zahlungsverkehrs auf Bitcoin. Wenn Sie eine Zahlung vornehmen, verbrauchen Sie einen einzigen UTXO als Input und erzeugen 2 neue UTXOs als Output (einen für die Zahlung und den anderen für den Exchange). Schließlich bietet eine Heuristik zur Kettenanalyse, genannt CIOH (*Common Input Ownership Heuristic*), einen weiteren Anreiz, die Konsolidierung von Coin zu vermeiden.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Da ein Teil davon im Arbeitsspeicher gehalten werden muss, um Transaktionen in einer angemessenen Zeit zu überprüfen, kann der UTXO-Satz den Betrieb eines Full node allmählich zu kostspielig machen. Zur Lösung dieses Problems gibt es bereits einige Vorschläge, vor allem [Utreexo] (https://planb.network/resources/glossary/utreexo).



### Der Mempool



Der Mempool ist der lokale Satz gültiger Transaktionen, die empfangen, aber noch nicht bestätigt wurden. Zur Erinnerung: Eine "bestätigte Transaktion" ist eine Transaktion, die in einen gültigen Block aufgenommen wurde. Jeder Knoten verwaltet seinen eigenen Mempool, der sich von dem anderer Knoten im Netzwerk unterscheiden kann, je nachdem:




- die dem Mempool über den Parameter `maxmempool` zugewiesene Größe: ein Knoten mit einem größeren Mempool kann mehr Transaktionen aufnehmen als ein Knoten mit einem kleineren Mempool (es sei denn, letzterer wird leer);
- gW-433-Regeln: Diese sind eine Teilmenge der Relaisregeln des Knotens und definieren die Merkmale, die eine unbestätigte Transaktion erfüllen muss, um in Mempool akzeptiert zu werden;
- perkolation von Transaktionen: Aufgrund verschiedener Faktoren kann eine bestimmte Transaktion bereits an einen Teil des Netzes verteilt worden sein, einen anderen aber noch nicht erreicht haben.



Es ist wichtig zu beachten, dass Knoten-Mempools keinen Konsenswert haben. Bitcoin funktioniert perfekt, auch wenn jeder Knoten einen anderen Mempool hat. Letztendlich sind die maßgeblichen Blöcke immer diejenigen, die dem Blockchain hinzugefügt wurden. Selbst wenn ein Knoten beispielsweise eine bestimmte Transaktion in seinem Mempool (der gemäß den Konsensregeln gültig ist) zunächst ablehnt, ist er verpflichtet, sie zu akzeptieren, wenn sie schließlich in einen Block mit einem gültigen Proof of Work aufgenommen wird. Würde er dies nicht tun und diesen Block ablehnen, obwohl er die Konsensregeln eingehalten hat, würde er einen Hard Fork auslösen, d. h. die Schaffung eines neuen, separaten Bitcoin, in dem er allein wäre.



#### Speicherpolitik und -verwaltung



Wenn eine Transaktion empfangen wird, führt Core eine Reihe von Überprüfungen anhand von Konsensregeln (Syntax, gültige Skripte, keine Doppelausgaben usw.) und Mempool-Regeln durch, bei denen es sich um eine lokale Richtlinie handelt (RBF, Mindestgebührenschwellen, Datenlimit in `OP_RETURN` usw.). Wenn die Transaktion diese Regeln einhält, wird sie gespeichert.



Die Größe des Mempool wird durch den Parameter `maxmempool` in der Datei `Bitcoin.conf` begrenzt (mehr dazu im nächsten Kapitel). Standardmäßig liegt die Grenze bei 300 MB. Wenn er voll ist, erhöht der Knoten dynamisch seine Mindestgebührenschwelle und stößt die am wenigsten profitablen Transaktionen zuerst aus (d.h. er behält Transaktionen zurück, die zuerst abgebaut werden sollten). Transaktionen, die zu alt sind, können auch nach einer konfigurierten Verzögerung verfallen.



#### Mempool Persistenz auf Festplatte



Um den Neustart zu beschleunigen, serialisiert Core regelmäßig den Zustand des Mempool in der Datei `Mempool.dat`, wenn der Knoten heruntergefahren wird. Zusätzlich zum eigentlichen Mempool, der im Speicher verbleibt, speichert Core diese "Mempool.dat"-Datei auf der Festplatte. Wenn der Knoten das nächste Mal gestartet wird, lädt er diesen Schnappschuss neu und löscht alles, was für den aktuellen Blockchain nicht mehr gültig ist.



### Hilfsdateien und Datenbanken



Mehrere andere Dateien auf der gleichen Ebene wie `blocks/`, `chainstate/` und `indexes/` tragen zum ordnungsgemäßen Funktionieren des Systems bei:




- die Datei "peers.dat" enthält ein IP-Address-Buch potenzieller Peers, das durch die anfängliche DNS-Ermittlung, Netzwerkaustausch und manuelle Ergänzungen gespeist wird. Wenn der Knoten startet, kann er auf diese Datei zurückgreifen, um ausgehende Verbindungen herzustellen.
- Beim Ausschalten des Knotens speichert `anchors.dat` die Adressen der abgehenden Teilnehmer, so dass Sie beim nächsten Start schnell wieder versuchen können, sie zu kontaktieren.
- die Datei `banlist.json` enthält lokale Verbote, die vom Betreiber oder vom Knoten beschlossen wurden (wiederholtes ungültiges Verhalten), um den Knoten daran zu hindern, sich erneut zu verbinden oder Verbindungen von diesen bestimmten Peers zu akzeptieren.
- die Datei "fee_estimates.dat" speichert Zeithorizontstatistiken über beobachtete Bestätigungen, die vom Gebührenschätzer verwendet werden, um Gebührensätze vorzuschlagen, die mit den bei der Erstellung einer Transaktion gewählten Verzögerungszielen vereinbar sind.
- gW-446.conf` enthält die Konfigurationsparameter Ihres Knotens. Hier können Sie die Relaisregeln anpassen. Mehr darüber erfahren Sie im nächsten Kapitel.
- die Datei `settings.json` enthält zusätzliche Parameter zu `Bitcoin.conf`.
- debug.log" ist das diagnostische Textprotokoll, das im Falle eines Fehlers zum Verständnis der Knotenaktivitäten verwendet werden kann.
- gW-448.pid` speichert die Prozesskennung zur Laufzeit, so dass andere Anwendungen oder Skripte bitcoind (*Bitcoin daemon*) leicht identifizieren und bei Bedarf mit ihm interagieren können. Sie wird beim Starten des Knotens erstellt und beim Herunterfahren gelöscht.
- `ip_asn.map` ist eine IP → ASN-Zuordnungstabelle (eigenständiges System), die für Bucketing und Peer Diversification (Option `-asmap`) verwendet wird.
- `onion_v3_private_key` speichert den privaten Schlüssel des Tor v3 Dienstes, wenn die Option `-listenonion` aktiviert ist, um einen stabilen onion Address zwischen den Neustarts zu erhalten.
- `i2p_private_key` speichert den privaten I2P-Schlüssel, wenn `-i2psam=` verwendet wird, um ausgehende und möglicherweise eingehende Verbindungen über I2P herzustellen.
- .cookie" enthält einen ephemeren RPC-Authentifizierungs-token (beim Start erstellt, beim Herunterfahren gelöscht), wenn die Cookie-Authentifizierung verwendet wird. Dies kann z. B. für die Verbindung mit Wallet-Software verwendet werden.
- .lock" ist die Datenverzeichnissperre, die verhindert, dass mehrere Instanzen gleichzeitig in dasselbe Datenverzeichnis schreiben.
- `guisettings.ini.bak` ist die automatische Speicherung der GUI-Einstellungen (*Bitcoin Qt*), wenn die Option `-resetguisettings` verwendet wird.



Wie wir in den ersten Teilen dieses BTC 202-Kurses gesehen haben, ist Bitcoin core sowohl Bitcoin Node-Software als auch Wallet. Es ist jedoch nicht unbedingt die Lösung, die ich für die Verwaltung Ihrer Wallets empfehlen würde, da sein Interface grundlegend bleibt und seine Funktionalitäten im Vergleich zu moderner Software wie Sparrow oder Liana begrenzt sind. Core enthält auch Dateien für die Verwaltung Ihrer Geldbörsen:





- `wallets/` ist das Standardverzeichnis, das eine oder mehrere Dateien enthält;
- `wallets/<name>/Wallet.dat` ist die SQLite-Datenbank des Wallet (Schlüssel, Deskriptoren, Transaktions-Metadaten usw.);
- wallets/<name>/Wallet.dat-journal` ist das SQLite-Rollback-Protokoll.



Zusammenfassend lässt sich die Struktur der Bitcoin core-Datei wie folgt beschreiben:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Der Validierungspfad für einen neuen Block



Beim Empfang eines neuen Blocks prüft Ihr Knoten den Proof of Work und ganz allgemein die Einhaltung der Konsensregeln. Wenn alles in Ordnung ist, wendet er die Änderungen Transaktion für Transaktion auf seinen UTXO-Satz an: Er prüft, ob jeder Eintrag bestehende UTXOs mit einem gültigen Skript ausgibt, löscht diese UTXOs und fügt die neuen Ausgänge hinzu. Wenn alles gültig ist, werden die Änderungen an `chainstate/` übergeben.



Parallel dazu werden die Rückgängigmachungsdaten in die Datei `rev*.dat` und die Metadaten in den Index `blocks/index/` geschrieben. Der Block wird dann in die richtige Datei "blk*.dat" serialisiert. Im Falle einer Umstrukturierung liest der Knoten `rev*.dat` in umgekehrter Reihenfolge, um die aufgegebenen Blöcke sauber zu trennen, den UTXO-Satz wiederherzustellen und dann die Blöcke der neuen besten Kette zu verbinden.





## Verstehen von Bitcoin.conf


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



Die Datei "Bitcoin.conf" ist die Hauptkonfigurationsdatei des Interface für den Bitcoin core. Sie ermöglicht es Ihnen, das Verhalten und die Parameter Ihres Knotens anzupassen, ohne den Quellcode neu kompilieren oder Befehlszeilenänderungen vornehmen zu müssen. Konkret handelt es sich um eine einfache Textdatei, die in Schlüssel-Wert-Paaren strukturiert ist, d. h. jede Zeile der Datei verweist auf einen bestimmten Parameter (den Schlüssel) und den zugehörigen Wert, der geändert werden kann, um den Parameter anzupassen.



Netzwerk-, Transaktions-Relay-, Leistungs-, Indexierungs-, Protokollierungs- und RPC-Zugangsparameter können in der Datei "Bitcoin.conf" definiert werden. Diese Konfigurationsdatei ändert jedoch niemals die Konsensregeln des Protokolls: Sie legt nur die lokale Politik des Knotens (Weiterleitungsregeln) fest, die Art und Weise, wie er sich verbindet, indiziert und Dienste bereitstellt.



### Standort und Priorität



Standardmäßig befindet sich die Datei `Bitcoin.conf` im Bitcoin core-Datenverzeichnis. Dies ist das berühmte Verzeichnis, das wir im vorherigen Kapitel erwähnt haben. Allerdings wird diese Datei nicht automatisch von Bitcoin core erstellt, außer in bestimmten Umgebungen, wie z.B. Umbrel. Wenn sie noch nicht existiert, müssen Sie sie selbst erstellen, indem Sie einfach eine Datei mit dem Namen `Bitcoin.conf` erstellen und diese dann in einem Texteditor öffnen, um Ihre Änderungen vorzunehmen.



Die in der Datei `Bitcoin.conf` definierten Parameter können von 2 Ebenen überschrieben werden:




- `settings.json` (dynamisch von Interface-Grafiken oder einigen RPC geschrieben),
- und über Befehlszeilen geänderte Optionen.



Beachten Sie, dass jede Änderung an `Bitcoin.conf` einen Neustart des Knotens erfordert, um wirksam zu werden.



### Format und Struktur



Das Format der `Bitcoin.conf` ist daher sehr einfach: eine Zeile pro Option, in der Form `Option=Wert`. Unnötige Leerzeichen und Leerzeilen werden ignoriert, und Code-Kommentare beginnen mit `#`.



Fast alle booleschen Optionen können mit einem Präfix "no" deaktiviert werden. Zum Beispiel sind `listen=0` und `nolisten=1` je nach Version gleichwertig.



Um die Konfiguration nach Netzen zu unterteilen, können Sie Abschnitte verwenden: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Alternativ können Sie dem Optionsnamen `regtest.maxmempool=100` voranstellen.



### Was Bitcoin.conf tun kann und was nicht



Wie oben erläutert, sind die Konsensregeln in der Datei "Bitcoin.conf" offensichtlich nicht konfigurierbar, da dies einen Hard Fork erzeugen könnte. Auf der anderen Seite sind viele andere Aspekte konfigurierbar. Es gibt 3 nützliche Klassen, die man im Auge behalten sollte:




- Rein lokale Parameter. Diese betreffen nur Ihren Knoten: Cache-Größe (`dbcache`), pruned-Modus (`prune`), optionale Indizes... Sie beeinflussen die Leistung Ihres Rechners, aber nicht die des Netzwerks.
- Weiterleitungs- und Mempool-Richtlinien. Diese entscheiden darüber, was Ihr Knoten vor der Bestätigung akzeptiert, behält und weiterleitet: Mindestgebührenschwelle (`minrelaytxfee`), Mempool Größe und Aufbewahrungszeit (`maxmempool`, `mempoolexpiry`), Transaktionsersatz (RBF)... Diese Regeln sind nicht Teil des Konsens, so dass zwei verschiedene Knoten unterschiedliche Richtlinien haben können und trotzdem vollständig kompatibel sind. Andererseits haben diese Parameter einen Einfluss auf das Bitcoin-Netzwerk (wie im ersten Teil erklärt, insbesondere mit der Perkolationstheorie).
- Netzwerk-Konnektivität. Diese Optionen bestimmen, wie dein Knoten Peers findet, zuhört, ein NAT durchläuft, Tor oder einen Proxy benutzt oder seine Bandbreite begrenzt. Sie formen Ihre Topologie, verändern aber nicht die Weiterleitung von Transaktionen.



Das Verständnis dieser Trennung ist entscheidend: Wenn eine Transaktion nicht den Konsensregeln entspricht, wird Ihr Knoten sie in jedem Fall ablehnen. Aber eine strengere lokale Richtlinie kann sich weigern, eine Transaktion weiterzuleiten, die im Sinne des Konsenses gültig ist.



### Netzwerk und Topologie



Zunächst einmal ist es wichtig, klar zwischen den beiden Arten von Verbindungen zu unterscheiden, die ein Bitcoin-Knoten haben kann:




- Ausgehende Verbindungen, die von unserem Knoten zu einem anderen Knoten initiiert werden;



![Image](assets/fr/106.webp)





- Eingehende Verbindungen, die von einem anderen Knoten zu unserem initiiert werden.



![Image](assets/fr/107.webp)



Diese beiden Verbindungsarten sind durchaus in der Lage, dieselben Daten in beide Richtungen auszutauschen; es geht nicht darum, die Richtung des Datenflusses zu beschränken, sondern nur um den Unterschied im Initiator der Verbindung. Aus der Sicht unseres Knotens gelten ausgehende Verbindungen im Allgemeinen als sicherer, da wir sie initiieren und genau auswählen, zu welchem Knoten wir eine Verbindung herstellen wollen, so dass es unwahrscheinlich ist, dass die Verbindung böswillig ist. Standardmäßig unterhält der Bitcoin core 10 ausgehende Verbindungen (8 "*full-relay*" + 2 "*block-relay-only*").



Ein Full node erhöht den Wert des Netzes, indem er eingehende Verbindungen annimmt. Mit dem Parameter "Listen=1" wird das Abhören auf dem Standard-Port 8333 des betreffenden Netzes aktiviert, so dass diese eingehenden Verbindungen über das Clearnet empfangen werden können. Damit dies funktioniert, muss dieser Port auch auf Ihrem Router geöffnet sein. Ist dies nicht der Fall, funktioniert Ihr Knoten weiterhin nur mit ausgehenden Verbindungen, was keine Auswirkungen auf Ihre persönliche Nutzung des Bitcoin hat. Die Entscheidung, ob Sie eingehende Verbindungen zulassen wollen, liegt bei Ihnen; es gibt keine "beste Wahl"



Wenn du es vorziehst, keinen Port auf deinem Router zu öffnen, aber trotzdem eingehende Verbindungen akzeptierst, kannst du den Parameter `listenonion=1` aktivieren. Damit erreichst du das gleiche Ergebnis, aber nur über das Tor-Netzwerk und nicht über clearnet.



Auf der Netzebene haben wir auch:




- `addnode`: fügt einen freundlichen Peer zur Kontaktaufnahme hinzu (kann mehrfach angegeben werden).
- connect`: schränkt Verbindungen strikt auf den angegebenen Address ein (kann mehrmals angegeben werden). Core stellt keine Verbindung zu einem anderen Knoten her.
- seednode": wird nur zum Ausfüllen des Book-Address verwendet, wenn eine Verbindung zu einem Knoten hergestellt und dann getrennt wird.
- max Connections": legt die globale Obergrenze für eingehende und ausgehende Verbindungen fest. Standardmäßig ist dieser Parameter auf 125 gesetzt, was bedeutet, dass Ihr Knoten nie mehr als 125 Verbindungen akzeptiert.
- maxuploadtarget`: begrenzt die Uploads, um die Bandbreite über ein gleitendes 24-Stunden-Fenster zu begrenzen. Diese Obergrenze beeinträchtigt nicht die Ausbreitung von wichtigen aktuellen Elements.
- `onlynet`: begrenzt ausgehende Verbindungen nur auf ausgewählte Netzwerke (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Wenn du zum Beispiel möchtest, dass sich dein Knoten nur über Tor mit dem Bitcoin-Netzwerk verbindet, kannst du den Parameter `onlynet=onion` aktivieren und eingehende Verbindungen deaktivieren (oder auch nur Verbindungen über Tor zulassen).
- `dnsseed`: erlaubt oder verbietet _DNS-Seeds_, um Peers anzufordern, wenn Ihr lokaler Address-Pool niedrig ist (Voreinstellung: `1`, es sei denn `-connect` oder `-maxconnections=0`).
- `forcednsseed`: erzwingt, dass _DNS-Seeds_ beim Start angefordert werden, auch wenn Sie bereits Adressen auf Lager haben (Voreinstellung: `0`).
- feste Seeds": Erlaubt die Verwendung von *seed-Knoten* (hartkodierte Address-Liste), wenn _DNS-Seeds_ fehlschlagen oder deaktiviert sind (Standard: `1`).
- `dns`: Erlaubt DNS-Auflösungen im Allgemeinen (z.B. für `-addnode`/`-seednode`/`-connect`).



Standardmäßig kommuniziert Ihr Knoten über Clearnet, Tor und I2P. Das bedeutet, dass die Peers, mit denen er sich im Clearnetz verbindet, Ihre öffentliche IP Address sehen können, und Ihr ISP wird wahrscheinlich erkennen können, dass Sie einen Bitcoin-Knoten betreiben (obwohl P2P Transport V2 es für einen ISP schwieriger macht, zu lauschen). Das ist nicht unbedingt ein Problem, aber wenn du ein Durchsickern dieser Informationen vermeiden willst, kannst du deinen Knoten ausschließlich über das Tor-Netzwerk verbinden.



Um vollständig Tor-fähig zu sein, musst du Bitcoin core zwingen, nur dieses Netzwerk zu benutzen und einen versteckten Dienst für eingehende Verbindungen zu erstellen (wenn du sie aktivieren willst). In der `Bitcoin.conf` musst du diese Konfiguration hinzufügen:




- onlynet=onion",
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- proxyrandomize=1",
- listen=1",
- bind=127.0.0.1`,
- upnp=0",
- natpmp=0".



Alle deine P2P-Verbindungen gehen durch Tor. Dein Knoten erhält einen "onion"-Address für eingehende Verbindungen, so dass keine Ports auf dem Router geöffnet werden müssen. Dein ISP sieht nur den Tor-Verkehr, und deine Partner wissen nichts von deiner tatsächlichen öffentlichen IP Address.



Um die DNS-Auflösung im Klartext zu vermeiden, können Sie `dnsseed=0` und `dns=0` zu Ihrer Konfiguration hinzufügen. Sie müssen dann manuell `.onion`-Peers über `seednode=` oder `addnode=` bereitstellen, da die Erkennung neuer Knoten sonst schwierig ist.



Wenn Sie Anfänger sind, würde ich Ihnen natürlich raten, all diese Netzwerkeinstellungen vorerst in Ruhe zu lassen. Die Standardkonfiguration ist oft ausreichend.



### Mempool und Relaispolitik



#### Grundlegende Parameter



Hier sind die grundlegenden Parameter, die Sie in Ihrer "Bitcoin.conf" ändern können und die die Verwaltung Ihres Mempool und die Weiterleitung unbestätigter Transaktionen betreffen:





- `maxmempool=<n>`: Begrenzt die maximale Größe des lokalen Mempool auf `<n>` Megabytes (Standard: `300`). Wenn das Limit erreicht ist, erhöht Ihr Knoten dynamisch seinen effektiven Gebührenschwellenwert und priorisiert die am wenigsten profitablen Transaktionen (basierend auf dem Gebührensatz, nicht auf dem absoluten Wert), um unter dem Limit zu bleiben. Sie können diese Einstellung als Standard belassen. Sie zu erhöhen kann nützlich sein, wenn Sie Mining alleine sind oder wenn Sie einen genaueren Überblick über die Mempool Überlastung erhalten und die Gebührenabschätzung verbessern wollen. Umgekehrt spart eine Verringerung des Wertes RAM und in geringerem Maße auch andere Systemressourcen.





- `mempoolexpiry=<n>`: Maximale Aufbewahrungszeit für unbestätigte Transaktionen in Mempool (in Stunden, Standard: `336`). Nach dieser Zeit werden die Transaktionen entfernt, auch wenn noch Speicherplatz verfügbar ist.





- persistmempool=1": Speichert einen Schnappschuss des Mempool im Stillstand und lädt ihn beim Neustart neu (Standard: `1`). Dies beschleunigt die Wiederherstellung nach einem Neustart und vermeidet die Notwendigkeit, den Zustand über das Netzwerk neu zu lernen.





- `maxorphantx=<n>`: Maximale Anzahl der verwaisten Transaktionen, die beibehalten werden (abhängige Eingaben von UTXOs, die noch nicht im UTXO-Set gesehen wurden, Standardwert: `100`). Bei Überschreitung dieses Schwellenwerts werden die ältesten Transaktionen gelöscht, um ein unkontrolliertes Anwachsen des Cache zu vermeiden.





- blocksonly=1`: Deaktiviert die Annahme und erneute Übermittlung von unbestätigten Transaktionen, die von Peers empfangen wurden (sofern keine besonderen Berechtigungen erteilt wurden). Der Knoten lädt jetzt nur noch Blöcke hoch und macht sie bekannt. Lokal erstellte Transaktionen können weiterhin übertragen werden (um Ihren Knoten mit Ihrer Wallet-Software zu verwenden). Dadurch werden die Bandbreiten- und RAM-Anforderungen erheblich reduziert, wenn auch um den Preis einer geringeren Nützlichkeit für das Relais und einer völligen Unvertrautheit mit dem Mempool.





- `minrelaytxfee=<n>`: Minimaler Gebührensatz (in BTC/kvB), unter dem Transaktionen im Mempool des Knotens nicht akzeptiert und nicht an Peers weitergeleitet werden (Standard: `0.00001` = 1 sat/vB). Je höher dieser Wert ist, desto aggressiver filtert Ihr Knoten kostengünstige Transaktionen.





- `mempoolfullrbf=1`: Akzeptiert RBF-Transaktionen auch ohne ausdrückliche RBF-Signalisierung in der ersetzten Transaktion. Mit dieser "*full-RBF*"-Politik kann eine Transaktion mit einem höheren Gebührensatz eine andere in Mempool ersetzen, wenn die anderen Ersetzungsbedingungen erfüllt sind.



Zur Erinnerung: RBF ist ein Transaktionsmechanismus, der es dem Absender ermöglicht, eine Transaktion durch eine Transaktion mit höheren Gebühren zu ersetzen, um die Bestätigung zu beschleunigen. Wenn eine Transaktion mit einer zu niedrigen Gebühr blockiert bleibt, kann der Absender *Replace-by-fee* verwenden, um die Gebühr zu erhöhen und seine Ersatztransaktion in Mempools und bei Minern zu priorisieren.



#### Erweiterte und spezifische Einstellungen



Hier finden Sie die erweiterten Einstellungen für Mempool und die Relais-Richtlinie. Wenn Sie ein Anfänger sind, sollten Sie diese Einstellungen nicht ändern müssen:





- datacarrier=1`: Erlaubt die Weiterleitung und (bei Mining über den Knoten) die Einbeziehung von Transaktionen mit nicht-finanziellen Daten über einen `OP_RETURN`-Ausgang (Standard: `1`). Wenn Sie diesen Parameter deaktivieren, wird die Fläche für Spam mit nicht-finanziellen Daten geringfügig verkleinert, allerdings um den Preis einer geringeren Kompatibilität mit bestimmten Anwendungen. In jedem Fall müssen Sie vermintes `OP_RETURN` akzeptieren.





- datacarriersize=<n>`: Maximale Größe (in Bytes) des `OP_RETURN`, den der Knoten weiterleitet (Standard: `83`). Eine Verringerung dieses Wertes schränkt die über `OP_RETURN` transportierten Nutzdaten ein. Beachten Sie, dass dieses Limit in einer zukünftigen Version von Bitcoin core standardmäßig entfernt wird.





- bytespersigop=<n>`: Parameter, der Signaturtransaktionen in äquivalente Bytes für die Auswertung des Relay-Limits umwandelt (Standard: `20`). Dies beeinflusst die Akzeptanz von "sigops"-reichen Transaktionen gemäß den lokalen Regeln.





- permitbaremultisig=1": Erlaubt die Weiterleitung von *bare-Multisig* P2MS-Transaktionen (Standard: `1`). Dies ist die älteste Skriptvorlage für die Einrichtung von Multisignaturbedingungen auf einem UTXO (erfunden 2011 von Gavin Andresen).





- whitelistrelay=1": Gewährt eingehenden Peers, die auf der Whitelist stehen, automatisch eine Relay-Erlaubnis (Standard: `1`). Die Transaktionen dieser Peers werden vom Relay akzeptiert, auch wenn sich Ihr Knoten nicht im allgemeinen Relay-Modus befindet.





- whitelistforcerelay=1`: Weist "*forcerelay*"-Erlaubnis für Peers auf der Whitelist mit Standardberechtigungen zu (Standard: `0`). Der Knoten leitet dann ihre Transaktionen weiter, auch wenn sie bereits in Mempool vorhanden sind, und umgeht so die Anti-Redundanz-Mechanismen.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Bindet einen Interface- oder Address-Bereich und weist den entsprechenden Peers feinkörnige Berechtigungen zu: `relay`, `forcerelay`, `Mempool` (Mempool Inhaltsanforderung), `noban`, `download`, `addr`, `bloomfilter`. Dies kann nützlich sein, um vertrauenswürdigen Gegenstellen (wie Gateways, LANs und internen Diensten) eine privilegierte Behandlung zu gewähren.





- peerbloomfilters=1`: Aktivieren Sie die Unterstützung für Bloom-Filter (BIP37), um gefilterte Blöcke/Transaktionen an Thin-Clients zu liefern (Standard: `0`). Warnung: Dies erhöht die Last auf Ihren Ressourcen.





- peerblockfilters=1`: Stellt BIP157 (*Neutrino*) Kompaktfilter für Peers bereit (Standard: `0`).





- `blockreconstructionextratxn=<n>`: Zusätzliche Anzahl von Transaktionen, die im Speicher gehalten werden, um kompakte Blöcke wiederherzustellen (Voreinstellung: `100`). Verbessert den Erfolg von Rekonstruktionen während kompakter Synchronisationen, auf Kosten von etwas Speicher.



Zur Erinnerung: Alle diese Relay-Regeln haben keinen Einfluss auf die Gültigkeit von Transaktionen, die in einem gültigen Block enthalten sind. Sie dienen dazu, Ihren Beitrag zum Relay anzupassen, Ihre Ressourcen zu schützen und Ihren Knoten in eingeschränkten Umgebungen berechenbar zu machen, aber sie erlauben Ihnen niemals, Blöcke abzulehnen, die die Konsensregeln einhalten.



### Geldbörsen



Sie können auch die Art und Weise, wie Ihre Geldbörsen verwaltet werden, in der Datei `Bitcoin.conf` anpassen. Wenn Sie Wallet nicht direkt in Core verwenden, sondern eine externe Verwaltungssoftware wie Sparrow oder Liana, sind diese Parameter von geringer Bedeutung:





- addresstype=<legacy|P2SH-SegWit|bech32|bech32m>`: Legt das Format der Wallet-generierten Adressen für den Empfang fest.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Erzwingt Exchange-Address-Format (Rest einer Eingabe auf eine einzige Zahlung).





- gW-727=<Pfad>`: Lädt einen vorhandenen Wallet beim Start (kann wiederholt werden, um mehrere Geldbörsen zu laden).





- `walletdir=<dir>`: Verzeichnis, das die Wallets enthält (Standard: `<datadir>/wallets` wenn es existiert, sonst `<datadir>`). Dies kann nützlich sein, wenn Sie die Wallets auf einem dedizierten oder verschlüsselten Volume speichern wollen.





- walletbroadcast=1": Sendet automatisch Transaktionen, die von geladenen Geldbörsen erstellt wurden (Standard: `1`). Setzen Sie auf "0", wenn Sie die Übertragung über einen anderen Kanal verwalten möchten.





- walletrbf=1": Aktiviert RBF Opt-in, um RBF bei allen Transaktionen zu signalisieren (Standard: `1`). Ermöglicht es Ihnen, die Gebühren im Falle einer blockierten Transaktion später zu erhöhen.





- `txconfirmtarget=<n>`: Bestätigungsziel für die Transaktion (in Anzahl der Blöcke, Standard: `6`). Die Wallet setzt die Gebühr für die Transaktion automatisch so fest, dass sie innerhalb dieser Anzahl von Blöcken bestätigt wird.





- `paytxfee=<amt>`: Fester Gebührensatz (BTC/kvB), der auf Wallet-Transaktionen angewendet wird. Generell zu vermeiden: adaptive Schätzung über `txconfirmtarget` verwenden.





- fallbackfee=<amt>`: Fallback-Rate (BTC/kvB), die verwendet wird, wenn der Schätzer keine Daten mehr hat (Standardwert: `0.00`). Bei einem Wert von 0 wird das Fallback vollständig deaktiviert.





- mintxfee=<amt>`: Mindestschwellenwert (BTC/kvB), ab dem Wallet Transaktionen erstellt (Standardwert: "0,00001"). Wallet wird sich weigern, eine Transaktion unter diesem Schwellenwert zu erstellen.





- maxtxfee=<amt>`: Absolute Obergrenze der Gesamtgebühren für eine Wallet-Transaktion (Standardwert: 0,10 BTC). Schützt vor abnorm hohen Gebühren, die unnötig Bitcoins zerstören würden.





- teilausgaben vermeiden=1": Wählt UTXOs nach Address-Clustern aus, um Teilausgaben zu vermeiden.





- spendzeroconfchange=1": Erlaubt die Wiederverwendung eines unbestätigten UTXO Exchange als Eintrag in einer neuen Transaktion (Standardwert: `1`).





- consolidatefeerate=<amt>`: Maximaler Satz (BTC/kvB), bei dessen Überschreitung Wallet nicht mehr Inputs hinzufügt als für die Konsolidierung erforderlich. Dies ermöglicht opportunistische Konsolidierungen zu niedrigen Preisen und reduziert die Kosten, wenn die Kosten hoch sind.





- `maxapsfee=<n>`: Budget für zusätzliche Gebühren (BTC, absoluter Wert), die der Wallet zu zahlen bereit ist, um die Option "*Teilausgaben vermeiden*" zu aktivieren.





- `Discardfee=<amt>`: Satz (BTC/kvB), der angibt, inwieweit Sie bereit sind, den Exchange wegzuwerfen, indem Sie ihn zur Gebühr hinzufügen. Ausgaben, die bei diesem Satz mehr als ein Drittel ihres Wertes kosten würden, werden verworfen.





- keypool=<n>`: Größe des vorgenerierten Address-Pools (Standard: `1000`). Zu kleine Werte erhöhen das Risiko einer unvollständigen Wiederherstellung.





- disablewallet=1": Startet Bitcoin core ohne das Subsystem Wallet und deaktiviert die zugehörigen RPCs. Verringert die Angriffsfläche und den Fußabdruck, wenn der Knoten nur zur Validierung/Freigabe verwendet wird.



### Speicherung, Indizierung und Leistung



In der Konfigurationsdatei können Sie auch die Parameter für Ihre Maschine einstellen. Dies kann besonders wichtig sein, wenn Sie über begrenzte Ressourcen oder im Gegenteil über eine große verfügbare Kapazität verfügen:





- datadir=<dir>`: Legt das Hauptdatenverzeichnis des Bitcoin core fest.





- `blocksdir=<dir>`: Entkoppelt den Ort der Blockdateien (`blocks/blk*.dat` und `blocks/rev*.dat`) vom `datadir`. Dies kann nützlich sein, um das Blocks-Archiv auf einem anderen Datenträger zu platzieren, während die Zustandsbasis (`chainstate/`) beispielsweise auf einem schnelleren Medium bleibt.





- `dbcache=<n>`: Weist `<n>` MiB für den Datenbank-Cache (*LevelDB*) zu, der vom Blockindex und `chainstate` verwendet wird (Standard: `450`). Je höher der Wert, desto schneller die IBD und die aktuelle Validierung, allerdings auf Kosten eines höheren RAM-Verbrauchs.





- prune=<n>`: Aktiviert das Pruning von Blockdateien und setzt ein Speicherplatzziel in MiB (Standard: `0` = deaktiviert; `1` = manuelles Pruning über RPC; `>=550` = automatisches Pruning unterhalb des Ziels). Inkompatibel mit `txindex=1`. Der Knoten bleibt ein voll validierender Knoten, kann aber nicht mehr die alte Historie liefern. Diese Option ist besonders nützlich, wenn der Festplattenspeicherplatz begrenzt ist, z. B. bei der Installation eines Knotens auf Ihrem Heimcomputer.





- txindex=1`: Erstellt und pflegt einen globalen Index der bestätigten Transaktionen. Unverzichtbar für bestimmte Abfragen (`getrawtransaction`, nicht Wallet) und für Explorationszwecke, vergrößert aber den Plattenplatzbedarf erheblich. Inkompatibel mit dem pruned-Modus.





- `assumevalid=<hex>`: Gibt einen Block an, von dem angenommen wird, dass er gültig ist, so dass Sie die Skriptprüfungen für seine Vorgänger überspringen können (setzen Sie `0`, um alles zu prüfen). Siehe das vorherige Kapitel für weitere Informationen.





- `reindex=1`: Rekonstruiert Blockindizes und Status (`chainstate`) aus `blk*.dat`-Dateien auf der Festplatte. Baut auch optionale aktive Indizes wieder auf. Dies ist ein zeitaufwändiger Vorgang, um eine beschädigte Datenbank zu reparieren oder schwere Indizes sauber zu aktivieren/deaktivieren.





- reindex-chainstate=1`: Stellt nur den `chainstate` vom aktuellen Blockindex wieder her. Bevorzugt, wenn die Blockdateien in Ordnung sind.





- `blockfilterindex=<Typ>`: Verwaltet Indizes von kompakten Blockfiltern (z.B. `basic`), die von Thin Clients (BIP157/158) und einigen RPCs verwendet werden. Standardmäßig deaktiviert (`0`). Verbraucht zusätzlichen Plattenplatz und Indizierungszeit.





- coinstatsindex=1": Führt einen UTXO-Statistikindex, der mit dem Aufruf "gettxoutsetinfo" betrieben wird. Nützlich für Audits und Metriken, da eine kostspielige Neuberechnung entfällt. Standardmäßig deaktiviert.





- `loadblock=<Datei>`: Importiert beim Start Blöcke aus einer externen Datei `blk*.dat`. Wird verwendet, um den Verlauf aus einer Offline-Quelle (lokale Kopie, externe Medien) vorzuladen, um die Initialisierung zu beschleunigen.





- `par=<n>`: Legt die Anzahl der Skriptüberprüfungs-Threads fest (von `-10` bis `15`, `0` = auto, `<0` = lässt diese Anzahl von Kernen frei). Erlaubt Ihnen, die CPU-Parallelität während der Überprüfung anzupassen. Der Auto-Modus ist in den meisten Fällen geeignet.





- `debuglogfile=<file>`: Gibt den Speicherort des Protokolls `debug.log` an.





- shrinkdebugfile=1`: Verringert die Größe von `debug.log` beim Start (Standard: `1`, wenn `-debug` nicht aktiv ist).





- einstellungen=<Datei>`: Pfad zur dynamischen Einstellungsdatei `settings.json`.



### RPC Zugang und Betriebssicherheit



Schließlich können Sie in der Datei "Bitcoin.conf" auch die Zugriffsparameter für Ihren Knoten konfigurieren. Seien Sie vorsichtig mit diesen Einstellungen, besonders wenn Sie gerade erst anfangen: Vermeiden Sie es, sie zu ändern, ohne die Auswirkungen genau zu verstehen, da dies zu Schwachstellen führen könnte.





- server=1": Aktiviert den JSON-RPC-Server. Unerlässlich, wenn Sie `bitcoind` über `bitcoin-cli` oder eine Anwendung eines Drittanbieters betreiben. Deaktivieren (`0`) auf einem reinen Validierungsknoten, der keine API offenlegt oder bereits einen Electrum-Server verwendet.





- rpcbind=<addr>[:port]`: RPC-Server lauscht Address/Port. Standardmäßig erfolgt das Abhören nur lokal (`127.0.0.1` und `::1`). Dieser Parameter wird ignoriert, wenn `rpcallowip` nicht ebenfalls definiert ist. Verwenden Sie ihn, um Interface explizit einzuschränken.





- rpcport=<Port>`: RPC-Port (Standard: `8332` auf Mainnet, `18332` auf Testnet, `38332` auf bookmark, `18443` auf regtest).





- rpcallowip=<ip|cidr>`: Erlaubt RPC Clients von einer bestimmten IP oder einem Subnetz (kann wiederholt werden). In Verbindung mit `rpcbind` verwenden, um die API nur für ein vertrauenswürdiges Segment (LAN/VPN) freizugeben.





- rpcauth=<USERNAME>:<SALT>$<Hash>`: Empfohlene RPC-Authentifizierungsmethode (Hash-Passwort). Erlaubt mehrere Einträge und vermeidet die Speicherung eines Geheimnisses im Klartext.





- rpccookiefile=<Pfad>`: Pfad zum Authentifizierungs-Cookie (Standard: Datei `.cookie` unter `datadir/`). Dies wird für den lokalen Zugriff desselben Benutzers ohne Verwaltung dauerhafter Passwörter verwendet. Beispielsweise können Sie damit den Liana Wallet mit Ihrem Bitcoin core auf demselben Rechner verbinden.





- rpcuser=<user>` / `rpcpassword=<pw>`: Klassische RPC-Authentifizierung mit Klartext-Passwort. Vermeiden Sie dies zugunsten von `rpcauth` oder einem Cookie.





- rpcthreads=<n>`: Anzahl der Threads, die RPC-Aufrufe bedienen (Standard: `4`). Erhöhen Sie diese Zahl, wenn Sie hohe Aufrufspitzen auf der Seite der Überwachung/des externen Tools haben.





- rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Whitelist der zugelassenen APIs. Reduziert die Angriffsfläche durch Einschränkung der zugänglichen Methoden.





- rpcwhitelistdefault=1|0": Standardverhalten der Whitelist: wenn aktiviert und eine Whitelist verwendet wird, werden nicht gelistete Anrufe abgewiesen. Dies kann auch eine leere Standardmenge erzwingen (keine Anrufe erlaubt), solange nichts explizit aufgeführt ist.





- rest=1": Aktivieren Sie die öffentliche REST-API (standardmäßig deaktiviert). Darf nur in einem vertrauenswürdigen Netzwerk offengelegt werden (gleiche Vorsicht wie bei JSON-RPC).





- `conf=<Datei>`: Gibt, nur auf der Befehlszeile, eine schreibgeschützte Konfigurationsdatei an. Nützlich zum Einfrieren eines Ausführungsprofils (unveränderlich) auf der Ops-Seite.





- `includeconf=<Datei>`: Lädt eine zusätzliche Konfigurationsdatei (Pfad relativ zu `datadir/`). Ermöglicht die Trennung der Rollen: gemeinsame Basis + sensible lokale Überladung.





- gW-769=1` / `daemonwait=1`: Startet `bitcoind` im Hintergrund und wartet mit `daemonwait` auf das Ende der Initialisierung, bevor es übergeben wird. Dies erleichtert die Integration mit Überwachungsprogrammen (systemd, runit).





- `pid=<Datei>`: Speicherort der PID-Datei.





- `sandbox=<log-and-abort|abort>`: Aktiviert experimentelles Syscall-Sandboxing: nur erwartete Syscalls sind erlaubt.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Führt einen Befehl beim Starten oder Herunterfahren aus.





- alertnotify=<cmd>`: Löst bei Empfang eines Alerts einen Befehl aus.





- `blocknotify=<cmd>`: Führt für jeden neuen Block einen Befehl aus.





- `debug=<Kategorie>|1` / `debugexclude=<Kategorie>`: Aktiviert/deaktiviert detaillierte Protokollkategorien (z.B. `net`, `Mempool`, `RPC`, `validation`...).





- logips=1": Protokolliert IP-Adressen.





- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Fügt den Protokollen Quellorte, Threadnamen und genaue Zeitstempel hinzu.





- printtoconsole=1`: Sendet Traces/Debugs an die Konsole (*stdout*).





- help-debug=1": Zeigt die Hilfe zur Debug-Option an und beendet das Programm.





- uacomment=<cmt>`: Fügt einen Kommentar zum Benutzer-Agenten P2P hinzu.



Wir haben nun die meisten Konfigurationsparameter aufgelistet. Diese Datei `Bitcoin.conf` stellt somit das eigentliche Dashboard Ihres Knotens dar: Sie definiert die Netzwerkkonfiguration, die Mempool-Verwaltung, die Festplatten- und Speichernutzung, die Indexierung und die allgemeine Verwaltung. Wenn Sie mehr über diese Datei erfahren und eine auf Ihre Bedürfnisse zugeschnittene Datei erstellen möchten, empfehle ich die Verwendung von [Jameson Lopps Generator] (https://jlopp.github.io/Bitcoin-core-config-generator/).



Wir sind am Ende dieses BTC 202-Kurses angelangt, der Sie nicht nur in die Lage versetzt hat, die Grundlagen zu verstehen, wie Nodes funktionieren und wie sie innerhalb des Systems interagieren, sondern auch Ihren eigenen einzurichten. Sie sind jetzt ein souveräner Bitcoiner, mit Ihrem eigenen Wallet, der Ihre Transaktionen über Ihren eigenen Knoten überträgt. Herzlichen Glückwunsch!



Sie können nun zum letzten Teil des Kurses übergehen, in dem Sie BTC 202 bewerten können, und anschließend Ihr Diplom ablegen, um zu überprüfen, ob Sie alle behandelten Konzepte beherrschen.



Ihnen stehen nun mehrere Optionen offen. Der nächste logische Schritt ist die Einrichtung eines eigenen Lightning-Knotens, der es Ihnen ermöglicht, bei Ihren off-chain-Transaktionen völlig unabhängig zu sein. Dies wird das Thema eines kommenden Kurses sein, der im Herbst 2025 über Plan ₿ Network veröffentlicht wird.



In der Zwischenzeit lade ich Sie ein, die BTC 204-Schulung kennenzulernen, die Sie in die Lage versetzen wird, die Grundsätze des Datenschutzes bei der Nutzung von Bitcoin zu verstehen und zu beherrschen:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Letzter Teil


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Rezensionen und Bewertungen


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Abschlussprüfung


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Schlussfolgerung


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>