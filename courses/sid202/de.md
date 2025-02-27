---
name: Bauen mit Elementen und Liquid Network
goal: Lernen Sie, die Open-Source-Blockchain-Plattform Elements und ihre wichtigsten Funktionen zu nutzen und damit zu entwickeln
objectives: 

  - Verstehen Sie die grundlegenden Konzepte der Elements-Blockchain-Plattform und der Liquid-Sidechains.
  - Lernen Sie, wie man Elements-Knoten für Standalone- und Sidechain-Konfigurationen einrichtet und betreibt.
  - Sammeln Sie praktische Erfahrungen mit der föderierten Blocksignierung und dem föderierten 2-Way Peg.
  - Einrichtung und Verwaltung von sicheren, effizienten Blockchain-Umgebungen für reale Anwendungsfälle.

---
# Bauen Sie auf Flüssigkeit und Elemente

Entdecken Sie die fortgeschrittenen Funktionen und Möglichkeiten von Liquid und Elements und lernen Sie, wie Sie diese Tools effektiv nutzen können, um Ihre Entwicklungsprojekte zu verbessern. Diese Schulung bietet eine umfassende theoretische und praktische Grundlage, die es Ihnen ermöglicht, Funktionen wie Confidential Transactions, Issued Assets und Federated Block Signing zu beherrschen.

Liquid, das auf dem Elements-Framework basiert, wurde entwickelt, um den Datenschutz, die Skalierbarkeit und die Funktionalität von finanziellen und technischen Lösungen zu verbessern. In diesem Kurs werden Sie praktische Erfahrungen mit der Ausgabe und Verwaltung von Vermögenswerten, dem Federated 2-Way Peg und der Verwendung von Tools wie elementsd und elements-cli sammeln, die Sie in die Lage versetzen, innovative, auf Ihre Bedürfnisse zugeschnittene Lösungen zu erstellen.

Dieser Kurs ist auf Entwickler aller Erfahrungsstufen zugeschnitten. Anfänger und fortgeschrittene Benutzer finden verständliche Erklärungen und praktische Beispiele, während fortgeschrittene Benutzer tiefer in technische Details und weniger bekannte Funktionen von Liquid und Elements eintauchen können.

Machen Sie mit, um Ihre Fähigkeiten zu verbessern, das volle Potenzial von Liquid und Elements auszuschöpfen und wirkungsvolle Werkzeuge für die Zukunft der Liquid-Innovation zu entwickeln.

+++
# Einführung

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## Kurse Einführung

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

![Video](https://youtu.be/gkQfnwYLyI0?si=H6cIPhgZaSAwHaHI)

Ziel der Elements Academy ist es, die Schlüsselkonzepte von Elements, der Open-Source-Plattform, auf der Liquid aufbaut, vorzustellen und zu erklären. Am Ende des Kurses sollten Sie die wichtigsten Funktionen von Elements, wie z. B. Confidential Transactions und Issued Assets, und die mit dem Betrieb von Elements Core verbundenen Prozesse gut verstehen.

Jeder Abschnitt besteht aus Lektionen mit erklärendem Text und einem Video, das mit einem Quiz endet. Die Anzahl der Fragen bezieht sich auf den Umfang des vorangegangenen Themas. Abschnitt 10 fasst den Kursinhalt zusammen und endet mit einem größeren Quiz.

Alle Fragen, Bitten um zusätzliche Informationen oder Rückfragen zu den Quizantworten können an Ihren Lehrer James Dorfman gerichtet werden.

## Elemente Übersicht

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

![Video](https://youtu.be/ns-JLGdkNig?si=fmWye_boRSvVF1Bt)

Elements ist eine quelloffene, Sidechain-fähige Blockchain-Plattform, die Zugang zu leistungsstarken Funktionen bietet, die von Mitgliedern der Community entwickelt wurden, wie etwa vertrauliche Transaktionen und ausgegebene Vermögenswerte.

Elements ist im Kern ein Protokoll, das die Konsensbildung über den Transaktionsverlauf und die Regeln für die Übertragung und Erstellung von Vermögenswerten ermöglicht, die in einem verteilten Blockchain-Ledger gespeichert sind.

Weitere Hintergrundinformationen zu Elements finden Sie auf der Website des Elements-Projekts (https://elementsproject.org/), im offiziellen Liquid-Blog (https://blog.liquid.net/) und im Entwicklerportal (https://liquid.net/devs).

### Elemente

Elements wurde 2015 eingeführt und reduziert die internen Entwicklungs- und Forschungskosten. Es nutzt die neueste Blockchain-Technologie und eröffnet viele neue Anwendungsfälle für die Implementierung. Eine auf Elements basierende Blockchain kann entweder als eigenständige Blockchain betrieben oder an eine andere gekoppelt und als Sidechain betrieben werden. Wenn Elements als Sidechain betrieben wird, können Vermögenswerte nachweislich zwischen verschiedenen Blockchains übertragen werden.

Es basiert auf der Bitcoin-Codebasis und erweitert diese, sodass Entwickler, die mit der Bitcoin-API vertraut sind, schnell und kostengünstig funktionierende Blockchains erstellen und Proof-of-Concept-Projekte testen können. Da Elements auf der Bitcoin-Codebasis aufgebaut ist, kann es auch als Testumgebung für Änderungen am Bitcoin-Protokoll selbst dienen.

Im Folgenden werden einige der wichtigsten Funktionen von Elements aufgeführt.

#### Vertrauliche Transaktionen

Standardmäßig werden alle Adressen in Elements mit Confidential Transactions geblindet. Bei der Verblendung werden der Betrag und die Art des zu übertragenden Vermögenswerts kryptografisch für alle verborgen, außer für die Teilnehmer und diejenigen, denen sie den Verblendungsschlüssel mitteilen möchten.

#### Ausgegebene Vermögenswerte

Mit Issued Assets on Elements können mehrere Arten von Assets ausgegeben und zwischen Netzwerkteilnehmern übertragen werden. Ein emittierter Vermögenswert profitiert auch von vertraulichen Transaktionen und kann von jedem, der das entsprechende Reissue-Token besitzt, neu ausgegeben oder zerstört werden.

#### Föderierter 2-Wege-Wirbel

Elements ist eine Allzweck-Blockchain-Plattform, die auch an eine bestehende Blockchain (wie Bitcoin) "angekoppelt" werden kann, um den Transfer von Vermögenswerten von einer Kette zur anderen zu ermöglichen. Die Implementierung von Elements als Sidechain ermöglicht es, einige der inhärenten Eigenschaften der Hauptkette zu umgehen und gleichzeitig ein hohes Maß an Sicherheit beizubehalten, das durch auf der Hauptkette gesicherte Vermögenswerte gewährleistet wird.

#### Signierte Blöcke

Elements verwendet eine starke Föderation von Unterzeichnern, die so genannten Block Signers, die Blöcke zuverlässig und zeitnah unterzeichnen und erstellen. Dadurch entfällt die Transaktionslatenz des PoW-Mining-Prozesses, der aufgrund seiner zufälligen Poisson-Verteilung einer großen Blockzeitvarianz unterliegt. Mit dem föderierten Blocksignierungsprozess wird eine zuverlässige Blockerstellung erreicht, ohne dass eine dritte Vertrauensperson oder ein auf einem Algorithmus basierender Mining-Prozess erforderlich ist.

Elements fügt all diese Funktionen auf der Bitcoin Core Codebasis hinzu, erweitert die Fähigkeiten des Mainchain-Protokolls und ermöglicht neue Geschäftsanwendungen, wenn es als Sidechain oder als eigenständige Blockchain-Lösung eingesetzt wird.

# Element

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## Wie Elemente funktionieren

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

![Video](https://youtu.be/v0lzmfH81AY?si=V-xDWfmDLKyBcdPs)

Elements bietet eine technische Lösung für die Probleme, mit denen Blockchain-Nutzer täglich konfrontiert sind: Transaktionslatenz, mangelnde Privatsphäre und das Risiko der Fungibilität.

Elements überwindet diese Probleme durch den Einsatz von Federated Block Signing und Confidential Transactions.

Im Gegensatz zum Bitcoin-Netzwerk ist der Prozess der Blocksignierung bei Elements nicht auf Dynamic Membership Multiparty Signatures (DMMS) und Proof of Work (PoW) angewiesen. Stattdessen verwendet Elements eine starke Föderation von Unterzeichnern, die so genannten Blocksignierer, die Blöcke zuverlässig und zeitnah signieren und erstellen können. Dadurch entfällt die Transaktionslatenz des PoW-Mining-Prozesses, der aufgrund seiner zufälligen Poisson-Verteilung einer großen Blockzeitvarianz unterliegt. Der föderierte Blocksignierungsprozess ermöglicht eine zuverlässige Blockerstellung, ohne dass eine dritte Partei als vertrauenswürdig eingestuft werden muss.

Elements kann als Sidechain zu einer anderen Blockchain, wie Bitcoin, oder als eigenständige Blockchain ohne Abhängigkeiten von anderen Netzwerken laufen.

Wenn sie als Sidechain verwendet wird, enthält die Strong Federation auch Mitglieder, die den sicheren und kontrollierten Transfer von Vermögenswerten zwischen einer Hauptkette und einer Elements-Sidechain ermöglichen. Die kontrollierte Übertragung von Vermögenswerten wird als Federated 2-Way Peg bezeichnet und die Mitglieder, die die Rolle der Vermögensübertragung übernehmen, werden Watchmen genannt.

Die Prozesse, die beim Betrieb eines Elements-Netzwerks ablaufen, und die Rollen der Netzwerkteilnehmer sind wichtig, um zu verstehen, wie Elements funktioniert.

Unabhängig davon, ob sie als Sidechain oder als eigenständige Blockchain implementiert ist, nutzt Elements starke Verbände von Blocksignierern, um Blöcke zu erzeugen.

### Starke Föderationen

Elements verwendet ein Konsensmodell, das erstmals von Blockstream vorgeschlagen wurde und Strong Federations genannt wird. Eine Strong Federation benötigt keinen Proof of Work (PoW) und verlässt sich stattdessen auf die kollektiven Handlungen einer Gruppe von gegenseitig misstrauenden Teilnehmern, den sogenannten Functionaries.

Die Rollen, die ein Funktionär in einer starken Föderation erfüllen kann, sind: Blocksignierer und Wächter. Blocksignierer sind erforderlich, wenn Sie Elemente entweder im Sidechain- oder im Standalone-Blockchain-Modus betreiben, während Wächter nur in einem Sidechain-Setup erforderlich sind.

Die Aktionen, die ein Mitglied einer starken Föderation durchführen kann, sind auf zwei verschiedene Rollen aufgeteilt, um die Sicherheit zu erhöhen und den Schaden zu begrenzen, den ein Angreifer anrichten kann.

Durch die Kombination der Rollen dieser Teilnehmer kann Elements sowohl eine schnelle Blockerstellung (schnellere und endgültige Transaktionsbestätigung) als auch gesicherte, übertragbare Vermögenswerte (gebundene Vermögenswerte, die direkt mit einer anderen Blockchain verbunden werden können) bieten.

Sie können das Whitepaper über starke Föderationen hier lesen: https://blockstream.com/strong-federations.pdf

### Unterzeichner blockieren

Eine Blockchain wie die von Bitcoin wird erweitert, wenn jeder, der Teil einer dynamischen Gruppe von Blocksignierern ist, die Kette erweitert, indem er den Nachweis für die geleistete Arbeit erbringt. Die dynamische Natur der Gruppe führt zu den Latenzproblemen, die solchen Systemen eigen sind.

Durch die Verwendung eines festen Unterzeichnersatzes ersetzt ein föderiertes Modell den dynamischen Satz durch einen bekannten Satz mit mehreren Unterschriften. Durch die Verringerung der Anzahl der Teilnehmer, die für die Erweiterung der Blockchain erforderlich sind, wird die Geschwindigkeit und Skalierbarkeit des Systems erhöht, während die Validierung durch alle Parteien die Integrität des Transaktionsverlaufs gewährleistet.

Die föderierte Blocksignierung besteht aus mehreren Phasen:


- Schritt 1 - Die Blocksignierer schlagen allen anderen teilnehmenden Blocksignierern Kandidatenblöcke in einer Runde vor.
- Schritt 2 - Jeder Blocksignierer signalisiert seine Absicht, indem er sich im Voraus verpflichtet, den gegebenen Kandidatenblock zu signieren.
- Schritt 3 - Wenn der vorgegebene Schwellenwert für die Vorab-Zusage erreicht ist, unterzeichnet jeder Blocksignierer den Block.
- Schritt 4 - Wenn der Schwellenwert für die Unterschrift (der sich von dem in Schritt 3 unterscheiden kann) erreicht ist, wird der Block akzeptiert und an das Netzwerk gesendet. Die Strong Federation hat einen Konsens über den letzten Transaktionsblock erreicht.
- Schritt 5 - Der nächste Block wird dann vom nächsten Blocksignierer in der Runde vorgeschlagen und der Vorgang wiederholt sich.

Da die Blockgenerierung einer Strong Federation nicht probabilistisch ist und auf einer festen Anzahl von Unterzeichnern basiert, kommt es nie zu einer Reorganisation mehrerer Blöcke. Dies ermöglicht eine erhebliche Verringerung der Wartezeit bei der Bestätigung von Transaktionen. Außerdem entfällt der Anreiz, aus Profitgründen zu schürfen (d. h. die Block-Belohnungen), und wird durch einen Anreiz zur produktiven Teilnahme an einem Netzwerk ersetzt, bei dem alle Teilnehmer das gleiche Ziel verfolgen: sicherzustellen, dass das Netzwerk weiterhin in einer Weise funktioniert, die für alle von Vorteil ist. Dies geschieht ohne die Einführung einer einzigen Schwachstelle oder höherer Vertrauensanforderungen.

### Elemente als Sidechain - Watchmen und der föderierte 2-Way Peg

Wenn sie als Sidechain betrieben wird, haben einige Mitglieder der Strong Federation eine zusätzliche Rolle zu erfüllen, nämlich die der Watchmen. Wächter sind für den Transfer von Vermögenswerten in und aus einer Elements-Sidechain verantwortlich, Prozesse, die als "Peg-In" und "Peg-Out" bekannt sind.

Damit eine Sidechain vertrauenswürdig funktioniert, muss sie es den Teilnehmern ermöglichen, zu überprüfen, ob die Lieferung von Vermögenswerten kontrolliert und nachprüfbar ist. Eine Elements-Sidechain verwendet einen 2-Way Federated Peg, um den Zwei-Wege-Transfer von Vermögenswerten in und aus einer Elements-Blockchain zu ermöglichen. Dies erfüllt die Anforderungen der nachweisbaren Ausgabe und des Transfers zwischen den Blockchains.

Die Federated-2-Way-Peg-Funktion ermöglicht es, dass ein Vermögenswert mit anderen Blockchains interoperabel ist und den nativen Vermögenswert einer anderen Blockchain repräsentiert. Indem Sie Ihre Blockchain an eine andere ankoppeln, können Sie die Fähigkeiten der Mainchain erweitern und einige ihrer inhärenten Einschränkungen überwinden.

Auf hohem Niveau finden Übertragungen in die Sidechain statt, wenn jemand Vermögenswerte der Mainchain an eine Adresse sendet, die von einer Watchmen-Wallet mit mehreren Signaturen kontrolliert wird. Dadurch werden die Vermögenswerte auf der Mainchain effektiv eingefroren. Watchmen validiert dann die Transaktion und gibt die gleiche Menge des zugehörigen Vermögenswerts auf der Sidechain frei. Die freigegebenen Vermögenswerte werden an eine Sidechain-Wallet gesendet, die den Anspruch auf die ursprünglichen Mainchain-Vermögenswerte nachweisen kann. Durch diesen Vorgang werden Vermögenswerte von der Hauptkette auf die Sidechain übertragen.

Um Vermögenswerte zurück auf die Mainchain zu übertragen, führt ein Nutzer eine spezielle Peg-out-Transaktion auf der Sidechain durch. Diese Transaktion wird von Watchmen überprüft, die dann eine Transaktionsausgabe aus der von ihnen kontrollierten Multi-Signatur-Wallet auf der Mainchain signieren. Eine bestimmte Anzahl von Teilnehmern des Verbunds muss unterschreiben, bevor die Transaktion auf der Hauptkette gültig wird. Wenn die Watchmen einen Vermögenswert an die Mainchain zurücksenden, vernichten sie auch den entsprechenden Betrag auf der Sidechain, wodurch die Vermögenswerte effektiv zwischen den Blockchains übertragen werden.

## Einrichten und Ausführen von Elementen

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

![Video](https://youtu.be/Frr_OjTEPAM?si=iq5XonJyQk8S5OAu)

Da Elements auf der Bitcoin-Codebasis basiert, sind die Komponenten, aus denen ein funktionierendes Netzwerk besteht, sehr ähnlich.

Die Elements-Knoten-Software selbst heißt `elementsd` und läuft als Daemon auf dem Rechner eines Benutzers. Ein Daemon (oder Dienst in Windows) ist ein Programm, das im Hintergrund läuft, ohne die direkte Kontrolle eines angemeldeten Benutzers zu benötigen.

Hinweis: In diesem Dokument beziehen wir uns immer auf elementsd als die Daemon-Version, aber alles kann auch mit elements-qt gemacht werden, vorausgesetzt, die Server-Option ist aktiviert.

Der Elements-Daemon verbindet sich mit anderen Knoten im Netzwerk, um Transaktions- und Blockdaten auszutauschen und seine lokale Kopie der Blockchain des Netzwerks zu validieren und zu erweitern.

Die Elements-Software besteht auch aus einem Client-Programm namens `elements-cli`, mit dem Sie über die Befehlszeile RPC-Befehle (Remote Procedure Call) an elementsd senden können. Damit kann man zum Beispiel den Kontostand einer Geldbörse abfragen, Transaktions- oder Blockdaten einsehen oder eine Transaktion übertragen. Dieses Setup sollte jedem bekannt sein, der die Bitcoin-Äquivalente bitcoind und bitcoin-cli verwendet hat.

Da ein Elements-Knoten durch Übergabe von Parametern beim Start oder über eine Konfigurationsdatei konfiguriert werden kann, ist es möglich, mehr als eine Instanz auf demselben Rechner laufen zu lassen. Dies ist nützlich für Test- und Entwicklungszwecke, da Sie Ihr eigenes lokales Netzwerk auf einem einzigen Rechner einrichten können, wobei jeder Elements-Knoten seine eigene Kopie der Blockchain-Daten hat, seinen eigenen Pool unbestätigter gültiger Transaktionen verwaltet und RPC-Anfragen auf verschiedenen Ports abhört.

### Das Elements Code Repository und die Gemeinschaft

Elements ist ein Open-Source-Projekt, dessen Quellcode im Elements GitHub-Repository unter https://github.com/ElementsProject/elements zu finden ist. Das Repository enthält den Quellcode für die Programme elementsd und elements-cli sowie unterstützende Installations- und Build-Tools, eine Reihe von Tests und eine anleitende Dokumentation.

Ergänzend zum Code-Repository gibt es auch die Website https://elementsproject.org, eine auf die Community ausgerichtete Ressource mit Erklärungen zu Elements, seiner Funktionsweise und einem umfassenden Tutorial. Das Tutorial konzentriert sich auf das Erlernen von Elements anhand von Kommandozeilenbeispielen und zeigt Ihnen, wie Sie einfache Desktop- und Webanwendungen darauf aufbauen können. Die Website listet auch beliebte Diskussionsforen der Elements-Community auf und wird selbst auf GitHub gehostet, so dass Beiträge der Community zum Inhalt der Website geleistet werden können.

Um Elements auf Ihrem Rechner auszuführen, müssen Sie zunächst den Quellcode klonen (d. h. eine Kopie davon herunterladen), alle Abhängigkeiten des Codes installieren und schließlich die ausführbaren Dateien für den Daemon und den Client erstellen. Die Elements-Software ist dann bereit, konfiguriert und ausgeführt zu werden.

## Konfigurieren von Knoten und Netzwerken

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

Konfigurationseinstellungen können beim Start an einen Elements-Knoten übergeben werden, um die Art und Weise zu ändern, wie er läuft, Daten validiert, sich mit anderen Knoten verbindet und seine Blockchain-Daten initialisiert.

Die Einstellungen werden entweder aus der angegebenen Datei `elements.conf` geladen oder als Parameter über die Kommandozeile übergeben.

Einige Dinge können mit diesen Parametern geändert werden:


- Der Name des Standardvermögenswertes, der in einer eigenständigen Blockchain-Implementierung verwendet wird.
- Die Nummer des ursprünglich erstellten Assets.
- Der Vermögenswert, der für die Zahlung von Transaktionsgebühren im Netz zu verwenden ist.
- Der Speicherort der Blockchain-Datendateien.
- Die RPC-Zugangsdaten, die zur Verbindung mit einem Bitcoin-Knoten verwendet werden.
- Der zu erfüllende Schwellenwert "n von m" und die gültigen öffentlichen Schlüssel, die Blöcke signieren können.
- Das Skript, das zufriedenstellend sein muss, um Vermögenswerte in und aus einer Sidechain zu transferieren.
- Ob eine Verbindung zu einem Bitcoin-Knoten als Sidechain hergestellt werden soll oder nicht.

Viele von ihnen sind Teil der Konsensregeln des Netzwerks, daher ist es wichtig, dass sie beim Start auf alle Knoten angewendet werden. Einige können nach der Initialisierung einer Kette geändert werden, aber einige müssen nach der Initialisierung einer Kette festgelegt werden.

Die Verwendung von Parametern wird im weiteren Verlauf des Kurses behandelt, wenn sie sich auf die einzelnen Abschnitte beziehen.

### Grundlegende Operationen über die Befehlszeile

In diesem Kurs werden Beispiele gezeigt, die das Programm `elements-cli` verwenden, um RPC-Aufrufe an einen oder mehrere Elements-Knoten zu tätigen. Dies geschieht von einer Terminalsitzung aus, und um die Befehle kürzer zu machen, wird ein "Alias" verwendet. Nach dieser Konvention sehen Sie etwas wie die folgenden Befehle:

```bash
e1-dae
e1-cli getnewaddress
```

Die Zeichen "e1-dae" und "e1-cli" sind eigentlich eine typografische Abkürzung, die die Funktion "Alias" des Terminals nutzt. Die "e1-dae" und "e1-cli" werden tatsächlich ersetzt, wenn der Befehl ausgeführt wird und der Befehl, der ausgeführt wird, wird ähnlich sein:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

Was wir oben sehen, ist ein Aufruf zum Starten des Elements-Daemons und ein Aufruf der elements-cli-Programme, die sich im Verzeichnis `$HOME/elements/src` befinden, sowie ein Wert für den Parameter `datadir`. Der Parameter `datadir` erlaubt es uns, dem Daemon und den Client-Instanzen mitzuteilen, wo sie ihre Konfigurationsdateien finden und, im Falle des Daemons, wo sie ihre Kopie der Blockchain speichern sollen. Da sie sich eine Konfigurationsdatei teilen, kann der Client RPC-Aufrufe an den Daemon tätigen.

Durch erneutes Ausführen des obigen Befehls, aber mit einem anderen `datadir`-Wert, können wir mehr als eine Instanz von Elements starten, jede mit ihrer eigenen Kopie der Blockchain und der Konfigurationseinstellungen. Gemäß dieser Konvention werden wir im Kurs die Alias `e2-dae` und `e2-cli` verwenden, um auf ein anderes datadir-Verzeichnis als das von e1 zu verweisen. Das obige Beispiel für unsere zweite "e2"-Instanz würde also lauten:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

Damit können wir alle Arten von Operationen durchführen, wie z. B. die Abwicklung von Transaktionen zwischen Knoten, die Ausgabe von Vermögenswerten und die Überprüfung der Verwendung von Blinding bei vertraulichen Transaktionen zwischen verschiedenen Knoten im selben Netzwerk.

# Element verwenden Praktischer Anwendungsfall

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Vertrauliche Transaktionen

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

![Video](https://youtu.be/-by2xBtXQeE?si=7bLo_geGn3qh7MXN)

In diesem Abschnitt erfahren Sie, wie Sie die Funktion "Vertrauliche Transaktionen" von Elements nutzen können.

Alle Adressen in Elements sind standardmäßig durch vertrauliche Transaktionen verblindet, bei denen Betrag und Art der übertragenen Vermögenswerte nur für die Teilnehmer der Transaktion (und diejenigen, denen sie den Verblendungsschlüssel offenlegen wollen) sichtbar sind, während gleichzeitig kryptografisch garantiert wird, dass nicht mehr Münzen ausgegeben werden können als verfügbar sind.

### Vertrauliche Adressen und vertrauliche Vorgänge

Wenn Sie eine neue Adresse in Elements mit dem Befehl `getnewaddress` erstellen, wird sie standardmäßig als vertrauliche Adresse angelegt.

Um die Vertraulichkeit von Transaktionen zu demonstrieren, wird e2 sich selbst Geld senden und dann versuchen, die Transaktion von e1 einzusehen. Damit wird die Vertraulichkeit von Transaktionen in Elements demonstriert.

Jede neue Adresse, die von einem Elements-Knoten erzeugt wird, ist standardmäßig vertraulich. Wir können dies demonstrieren, indem wir e2 dazu bringen, eine neue Adresse zu erzeugen.

```
e2-cli getnewaddress
```

Beachten Sie, dass die Adresse mit e1 beginnt. Dadurch wird sie als vertrauliche Adresse identifiziert. Eine genauere Untersuchung der Adresse mit dem Befehl getaddressinfo zeigt weitere Details der Adresse.

```
e2-cli getaddressinfo <address>
```

Sie können sehen, dass es eine Eigenschaft confidential_key gibt, die uns sagt, dass es sich um eine vertrauliche Adresse handelt.

Der confidential_key ist der öffentliche Verblendungsschlüssel, der der vertraulichen Adresse selbst hinzugefügt wird. Dies ist der Grund, warum eine vertrauliche Adresse so lang ist.

Sie hat auch eine zugehörige nicht vertrauliche Adresse. Wenn Sie reguläre, nicht vertrauliche Transaktionen innerhalb von Elements verwenden möchten, sollten die Anlagen an diese Adresse und nicht an die Adresse mit dem Präfix lq1 gesendet werden.

Wir können nun e2 veranlassen, Geldbeträge an die von ihm generierte Adresse zu senden. Dies wird später zeigen, dass e1, da er keine der handelnden Parteien ist, nicht in der Lage sein wird, die Details der Transaktion einzusehen.

```
e2-cli sendtoaddress <address>
```

Notieren Sie die Transaktions-ID. Bestätigen Sie die Transaktion.

```
e2-cli -generate 101
```

Betrachtet man die Transaktion, bei der e2 einige Gelder an sich selbst geschickt hat, aus der Perspektive von e2 selbst.

```
e2-cli gettransaction <txid>
```

Wenn Sie in den Transaktionsdetails nach oben blättern, können Sie sehen, dass e2 die gesendeten und empfangenen Beträge sowie die getätigten Vermögenswerte anzeigen kann. Sie können auch die Eigenschaften amountblinder und assetblinder sehen, die dazu dienen, die Details vor anderen, nicht an der Transaktion beteiligten Knoten zu verbergen.

Um die Details der gleichen Transaktion von e1 zu überprüfen, müssen wir zuerst die Rohdaten der Transaktion erhalten.

```
e1-cli getrawtransaction <txid>
```

Diese gibt die Rohdaten der Transaktion zurück. Wenn Sie sich den Abschnitt vout ansehen, können Sie feststellen, dass es drei Instanzen gibt. Bei den ersten beiden Instanzen handelt es sich um den Eingangs- und den Änderungsbetrag, bei der dritten um die Transaktionsgebühr. Von diesen drei Beträgen ist die Gebühr der einzige, bei dem Sie einen Wert sehen können, da die Gebühr selbst in Elements immer unverblendet ist.

### Blinding Keys

Die ersten beiden Voutenabschnitte zeigen "geblendete Spannen" der Wertbeträge und die Verpflichtungsdaten, die als Nachweis für den tatsächlichen Betrag und die Art des getätigten Vermögenswerts dienen.

Selbst wenn wir den privaten Schlüssel von e2 in die Brieftasche von e1 importieren würden, könnte sie die Beträge und die Art der getätigten Transaktionen nicht sehen, da sie den von e2 verwendeten Blinding Key nicht kennt. Wir beweisen dies, indem wir den privaten Schlüssel von e2s Wallet in die von e1 importieren. Zunächst müssen wir den Schlüssel von e2 exportieren

```
e2-cli dumpprivkey <address>
```

Dann importieren Sie es in e1.

```
e1-cli importprivkey <privkey>
```

Jetzt können wir beweisen, dass e1 die Werte immer noch nicht sehen kann.

```
e1-cli gettransaction <txid>
```

In der Tat wird als Sendeleistung 0 angezeigt, obwohl sie eigentlich 1 war.

Um den tatsächlichen, nicht verblendeten Wert sehen zu können, benötigen wir den Verblendungsschlüssel. Zu diesem Zweck exportieren wir zunächst den Verblendungsschlüssel aus e2.

```
e2-cli dumpblindingkey <address>
```

Dann importieren Sie es in e1.

```
e1-cli importblindingkey <address> <blinding key>
```

Wenn wir nun die Transaktionsdetails von e1 erhalten.

```
e1-cli gettransaction <txid>
```

Es zeigt, dass wir mit dem importierten Verblendungsschlüssel nun den tatsächlichen Wert von 1 innerhalb der Transaktion sehen können.

In diesem Abschnitt haben wir gesehen, dass die Verwendung eines Verblendungsschlüssels den Betrag und die Art der Vermögenswerte in einer Transaktion verbirgt und dass wir diese Werte durch den Import des richtigen Verblendungsschlüssels aufdecken können. In der Praxis kann ein Verblendungsschlüssel z. B. an einen Wirtschaftsprüfer weitergegeben werden, wenn die Beträge und Arten von Vermögenswerten einer Partei überprüft werden sollen. Die Funktion "Vertrauliche Transaktionen" von Elements ermöglicht auch die Durchführung von "Bereichsnachweisen". Mit Hilfe von Bereichsnachweisen kann nachgewiesen werden, dass ein Vermögenswert innerhalb eines bestimmten Bereichs gehalten wird, ohne dass der tatsächliche Betrag offengelegt werden muss.

Wir haben auch gesehen, dass vertrauliche Transaktionen optional sind, aber standardmäßig aktiviert werden, wenn eine neue Adresse erstellt wird.

Das war's für diese Lektion; viel Glück beim Quiz und bis zum nächsten Mal!

## Ausgegebene Vermögenswerte

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

![Video](https://youtu.be/XnY4WZUNSs4?si=dG8I5OoSh_0EBdvL)

In diesem Abschnitt erfahren Sie, wie Sie die Funktion Ausgegebene Assets in Elements verwenden können.

Ausgegebene Vermögenswerte ermöglichen die Ausgabe mehrerer Arten von Vermögenswerten und deren Übertragung zwischen den Teilnehmern des Elements-Netzwerks. Jeder Knoten im Netzwerk kann seine eigenen Vermögenswerte ausgeben. Emissionen können fungibles Eigentum an jedem beliebigen Vermögenswert darstellen, einschließlich Gutscheinen, Coupons, Währungen, Einlagen, Anleihen, Aktien usw. Issued Assets öffnet die Tür für den Aufbau von vertrauenslosen Börsen, Optionen und anderen fortschrittlichen intelligenten Verträgen mit selbst ausgegebenen Assets.

Ein ausgegebener Vermögenswert profitiert auch von vertraulichen Transaktionen und kann von jedem, der den zugehörigen Token besitzt, erneut ausgegeben werden.

Der erste Schritt ist, dass wir Zugang zu zwei Elements-Knoten benötigen, die wir e1 und e2 nennen. Die Blockchains der Knoten wurden zurückgesetzt und das Standardvermögen zwischen ihnen aufgeteilt.

Die beiden Knoten befinden sich im selben lokalen Netzwerk, sind miteinander verbunden und teilen daher dieselben Transaktionen in ihrem Transaktions-Mempool und identische Blockchains. Obwohl sie auf demselben Rechner laufen, ist es erwähnenswert, dass sie nicht dieselben Blockchain-Dateien verwenden. Jeder Knoten verwaltet seine eigene lokale Kopie der Blockchain, die dieselbe Transaktionshistorie enthält, da sie sich im Konsens befinden und sich an dieselben Protokollregeln halten wie jeder andere.

Beginnen wir mit der Überprüfung der Sicht jedes Knotens auf die im Netz vorhandenen Emissionen von Vermögenswerten.

Dies geschieht mit dem Befehl listissuances.

```
e1-cli listissuances
e2-cli listissuances
```

Wie Sie sehen können, zeigen beide Knoten die gleiche Emissionshistorie. Sie zeigen beide einen Vermögenswert an, die Erstausgabe von 21 Millionen Bitcoin, die bei der Initialisierung der Kette erstellt wurden. Sie können die Hex-Id des Vermögenswerts in den Ergebnissen der Ausführung des obigen Befehls sehen und auch die Bezeichnung, die dem Vermögenswert zugewiesen wurde, nämlich "Bitcoin".

Es ist erwähnenswert, dass das Standard-Asset bei der Initialisierung der Kette immer mit einem Label versehen wird. Wenn Sie Ihre eigenen Assets ausgeben, können Sie ihnen selbst Labels zuweisen, was wir in Kürze tun werden. Bevor wir das tun können, müssen wir unser eigenes Asset ausgeben.

Wir werden e1 das neue Asset ausgeben lassen. Dies geschieht mit dem Befehl issueasset.

```
e1-cli issueasset 100 1 false
```

issueasset" nimmt 3 Parameter an.

Die Menge des neu auszugebenden Vermögenswerts, wir haben 100 verwendet. Die Menge der zu erstellenden Token (Token werden für die Neuausgabe von Beträgen eines Vermögenswerts verwendet), wovon wir 1 gewählt haben. Der letzte Parameter teilt Elements mit, ob die Ausgabe des Vermögenswerts verblindet oder unverblindet erfolgen soll. Wir verwenden "unblinded", da wir die Emissionsbeträge von e2 in einer Minute sehen wollen, also geben wir "false" ein.

Wenn Sie den Befehl ausführen, erhalten Sie Daten über die Ausgabe. Dazu gehören die Transaktions-ID, von der Sie eine Kopie für die spätere Verwendung erstellen können, der eindeutige Hex-Wert des Vermögenswerts und der eindeutige Hex-Wert des Tokens des Vermögenswerts.

Erzeugen Sie einen Block zur Bestätigung der Ausgabetransaktion.

```
e1-cli -generate 1
```

Führen Sie den Befehl "Listissuances" für e1 erneut aus.

```
e1-cli listissuances
```

Das zeigt uns, dass e1 jetzt 2 Emissionen kennt, die ursprüngliche Emission von Bitcoin und unser neu ausgegebenes Asset, von dem wir 100 Stück sehen können. Beachten Sie den hexadezimalen Wert des neuen Vermögenswerts und dass es keine zugehörige Vermögenswertbezeichnung gibt, wie bei der Bitcoin-Emission.

Überprüfen Sie erneut die Liste der bekannten Ausgaben von e2.

```
e2-cli listissuances
```

Das zeigt uns, dass e2 nichts von der Ausgabe von Vermögenswerten durch e1 weiß. Er kann nur die ursprüngliche Ausgabe von Bitcoin sehen, die er bereits sehen konnte.

Der Grund dafür ist, dass e2 die Adresse, an die die neue Anlage gesendet wurde, als sie von e1 ausgestellt wurde, nicht kennt und nicht beobachtet.

Auch wenn e2 die Emission selbst nicht sehen kann, könnte e1 e2 einen Teil des Vermögenswertes schicken. Der neue Vermögenswert würde dann als verfügbares Guthaben in der Brieftasche von e2 auftauchen, auch wenn dieser die ursprüngliche Emission nicht kennt.

Damit e2 die tatsächliche Ausgabe (und damit den ausgegebenen Betrag) sehen kann, müssen wir die Adresse in e2 als überwachte Adresse hinzufügen.

Dazu müssen wir die Adresse herausfinden, an die der Vermögenswert gesendet wurde. Dazu verwenden wir die Transaktions-ID, die wir zuvor kopiert haben, und lassen e1 die Details dieser Transaktion abrufen, damit wir die richtige Adresse herausfinden können, die wir der Überwachungsliste von e2 hinzufügen können.

```
e1-cli gettransaction <the-issuance-transaction-id>
```

Wenn Sie nach dem Hexadezimalwert der Transaktionsdaten nach oben blättern, sehen Sie die Adresse, die 100 unserer neuen Anlagegüter erhalten hat, gekennzeichnet durch ihren Hexadezimalwert.

Nehmen Sie die Adresse und kopieren Sie sie, damit wir sie in e2 importieren können.

Nun wollen wir diese Adresse in e2 importieren. Dazu verwenden wir den Befehl importaddress.

```
e2-cli importaddress <the-issued-to-address>
```

Überprüfen wir nun die Liste der e2-Emissionen.

```
e2-cli listissuances
```

Sie können sehen, dass unser neu ausgegebener Vermögenswert nun in der Liste enthalten ist. Der e2-Knoten ist auch in der Lage, den Betrag des ausgegebenen Vermögenswerts sowie den Betrag des zugehörigen Tokens zu ermitteln, da es sich um eine unverblindete Ausgabe handelt. Um die Zuordnung von Asset-IDs zu Namen in Elements zu aktivieren, stoppen Sie zunächst Elements.

```
e1-cli stop
```

Starten Sie ihn dann mit einem zusätzlichen Parameter neu, der das Hexadezimalzeichen eines Assets der angegebenen Bezeichnung zuordnet. Dies ermöglicht es dem Knoten, Daten über das Asset in einem besser lesbaren Format anzuzeigen. Wenn Sie möchten, können Sie diesen Parameter am Ende der elements.conf hinzufügen, dann müssen Sie das Argument nicht bei jedem Start des Daemon hinzufügen. Zum Beispiel:

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

Wir werden hier jedoch die Argumentationsmethode verwenden.

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

Erneute Abfrage des Knotens nach einer Liste der Ausgaben.

```
e1-cli listissuances
```

Das zeigt uns, dass die Zuordnung des Hexadezimalwerts des Assets zu seiner Bezeichnung funktioniert. Prüfen Sie erneut die Liste der Ausgaben des Knotens e2.

```
e2-cli listissuances
```

Sie sehen, dass der Knoten e2 keinen Zugriff auf diese Beschriftung hat, da Beschriftungen nur für den Knoten verfügbar sind, der sie festgelegt hat. In der Tat können wir demselben Asset-Hex auf e2 ein anderes Label zuweisen als auf e1. Halten Sie zunächst den Knoten e2 an.

```
e2-cli stop
```

Neustart mit einem anderen Etikett, das dem Hexadezimalwert unseres neuen Assets zugewiesen wurde.

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

Auflistung der Ausgaben von e2.

```
e2-cli listissuances
```

Asset-Kennzeichnungen sind für jeden Knoten lokal, nur das Feld des Assets wird von anderen Knoten im Netzwerk erkannt.

Die Zuordnung von Label zu Asset-Sechseck ist bei der Durchführung von Aktionen wie Transaktionen und Geldbörsenabfragen nützlich, da sie eine Kurzform für den Verweis auf ein Asset bietet. Wenn wir zum Beispiel einen Teil unseres neuen Guthabens (einen Betrag von 10) von e1 nach e2 schicken wollen, ohne das Label zu verwenden.

Zunächst benötigen wir eine Adresse, an die wir das Asset senden können.

```
e2-cli getnewaddress
```

Verwenden Sie dann den Befehl sendtoaddress.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

Bestätigen Sie die Transaktion, indem Sie einen Block erzeugen.

```
generate 1
```

Überprüfung des Vermögenswerts wurde auf e2 empfangen.

```
e2-cli getwalletinfo
```

Wir können sehen, dass die Anlage tatsächlich erhalten wurde.

Beachten Sie, dass e2 das Hexadezimalzeichen der empfangenen Kühlstelle zuordnet und sie mit ihrer eigenen Bezeichnung anzeigt. Eine einfachere Möglichkeit, dasselbe zu tun, wäre die Verwendung des Asset-Labels von e1 beim Senden.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

Hinter den Kulissen ordnet Elements die lokalen Bezeichnungen den Hex-Werten zu, um die Verwendung der ausgegebenen Assets zu vereinfachen.

In diesem Abschnitt haben wir gesehen, wie man Vermögenswerte ausgibt und kennzeichnet. Im nächsten Abschnitt werden wir uns mit der Neuausgabe und der Vernichtung von Beträgen eines ausgegebenen Vermögenswerts befassen.

## Neuausgabe von Vermögenswerten

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

![Video](https://youtu.be/5em79YHtYk0?si=rhponm6Hw9AB6RJp)

In diesem Abschnitt erfahren Sie, wie Sie mehr von einem bereits ausgegebenen Vermögenswert ausgeben können und wie Sie eine bestimmte Menge eines ausgegebenen Vermögenswerts vernichten können.

Die Notwendigkeit, einen Vermögenswert neu auszugeben (mehr zu schaffen) oder eine Menge des Vermögenswerts zu vernichten, tritt wahrscheinlich auf, wenn der Vermögenswert etwas repräsentiert, das keinen festen Vorrat hat. Dies könnte z. B. bei Vermögenswerten der Fall sein, die Gold in einem Tresor darstellen; wenn Goldeinheiten in den Tresor ein- und ausgehen, muss der Vermögenswert, der den Vorrat des Tresors darstellt, entsprechend nach oben oder unten angepasst werden.

Die erneute Ausgabe einer Menge eines Vermögenswerts erfordert den Besitz des zugehörigen Tokens, der zusammen mit dem Vermögenswert bei seiner ursprünglichen Ausgabe erstellt wurde.

Bei der Erstellung weiterer Vermögenswerte spielt es keine Rolle, welcher Knoten den Vermögenswert ursprünglich ausgegeben hat, solange der Knoten, der eine Menge eines Vermögenswerts neu ausgibt, im Besitz des so genannten Neuausgabetokens des Vermögenswerts ist. Wir werden uns ansehen, wie man das Wiederausgabetoken anfänglich erstellt, wie man es verwendet, um eine Menge eines Vermögenswerts neu auszugeben, und wie man das Wiederausgabetoken auf andere Knoten überträgt, so dass diese ebenfalls die Erlaubnis haben, den Vermögenswert neu auszugeben.

Wir benötigen Zugang zu zwei Elements-Knoten, die wir e1 und e2 nennen. Die Blockchains der Knoten wurden zurückgesetzt und das Standardvermögen zwischen ihnen aufgeteilt.

Wir lassen e1 eine Menge von 100 Stück eines neuen Vermögenswerts ausgeben und 1 Token für die Neuausgabe desselben Vermögenswerts erstellen. Zur Vereinfachung des Beispiels wird die Ausgabe als "unblinded" angelegt. Lassen Sie uns also fortfahren und den Vermögenswert und das zugehörige Reissuance-Token ausgeben.

```
e1-cli issueasset 100 1 false
```

Notieren Sie sich die ID des Vermögenswerts und auch die des (neu auszugebenden) Tokens.

Da wir später weitere Vermögenswerte aus e2 ausgeben werden, müssen wir uns die Transaktions-ID notieren, mit der der Vermögenswert ausgegeben wurde, und diese verwenden, um die Adresse zu importieren, an die der Vermögenswert gesendet wurde.

Bestätigen Sie die Transaktion.

```
e1-cli -generate 1
```

Mit dem Befehl gettransaction können wir nun die Details der Transaktion überprüfen:

```
e1-cli gettransaction <txid>
```

Wenn Sie über das Hexfeld der Transaktionsdaten hinaus blättern, sehen Sie, dass e1 bei der Transaktion 1 Wiederausgabetoken und 100 des zugehörigen Vermögenswerts erhalten hat.

Machen Sie eine Kopie der Adresse, damit wir sie in e2 importieren können.

Und jetzt importiere ich die Adresse in die e2-Brieftasche.

```
e2-cli importaddress <address>
```

Wir können nun feststellen, dass sowohl e1 als auch e2 von der Ausgabe von Vermögenswerten wissen.

```
e1-cli listissuances
e2-cli listissuances
```

Gegenwärtig besitzt e1 einen Teil des Vermögenswerts und 1 Wiederausgabemarke, e2 jedoch nicht.

```
e1-cli getwalletinfo
```

Beachten Sie auch, dass e1 weniger von dem Standard-Asset hat als zuvor, weil es einen kleinen Betrag zur Deckung der Transaktionsgebühren gezahlt hat. Dieser Betrag wird von e1 eingezogen, wenn der erstellte Block mehr als 100 Blöcke tief fällig wird.

```
e2-cli getwalletinfo
```

Da e1 im Besitz des Reissue-Tokens ist, kann es mehr davon ausgeben. Dies geschieht mit dem Befehl reissueasset. Lassen wir e1 weitere 100 Stück des Vermögenswerts neu ausgeben.

```
e1-cli reissueasset <asset-id> 100
```

Die Überprüfung der Neuausstellung hat funktioniert.

```
e1-cli getwalletinfo
```

Sie sehen, dass e1 nun wie erwartet 200 des Vermögenswertes hält.

Da e2 nicht über einen Betrag des Wiederausgabetokens verfügt, erhalten sie eine Fehlermeldung, wenn sie versuchen, den Vermögenswert wieder auszugeben.

```
e2-cli reissueasset <asset-id> 100
```

Beachten Sie die Fehlermeldung.

Mit dem Befehl listissuances können wir die Details der Neuausgabe von e1 einsehen.

```
e1-cli listissuances
```

Beachten Sie das Kennzeichen "is_reissuance".

Wenn wir nun e2 einen Betrag des Reissue-Tokens schicken, können sie selbst einen Betrag des Assets neu ausgeben. Zunächst benötigen wir eine Adresse, an die wir den Token senden können. Es ist erwähnenswert, dass der Reissuance-Token beim Senden und Anzeigen von Salden genauso behandelt wird wie jeder andere Vermögenswert innerhalb von elements und dass er wie jeder andere Vermögenswert auch in kleinere Stückelungen zerlegt werden kann, so dass wir nicht den 1 Reissuance-Token an e2 senden müssen, damit dieser den Vermögenswert neu ausgeben kann. Jede Stückelung ist ausreichend. Generierung einer Adresse für e2 zum Empfang des Reissue-Tokens.

```
e2-cli getnewaddress
```

Senden Sie dann einen Teil der RIT von e1 nach e2.

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Bestätigen Sie die Transaktion.

```
e1-cli -generate 1
```

Wir können jetzt sehen, dass e2 die 0,1 hält, die ihm gesendet wurde.

```
e2-cli getwalletinfo
```

Das bedeutet, dass e2 jetzt mehr von dem Vermögenswert ausgeben kann, der mit dem RIT verbunden ist, den es in seiner Brieftasche hat. Wir lassen e2 500 Stück des Vermögenswerts neu ausgeben.

```
e2-cli reissueasset <asset-id> 500
```

Überprüfen Sie das Ergebnis der Neuausstellung.

```
e2-cli getwalletinfo
```

Sie sehen, dass e2 nun den neu ausgegebenen Betrag in seiner Brieftasche hat und dass der RIT selbst bei der Neuausgabe von Vermögenswerten nicht verbraucht wird.

Die Zerstörung einer Menge eines Vermögenswerts ist etwas, das jeder tun kann, der mindestens die zu zerstörende Menge besitzt, und wird nicht durch das Wiederausgabesymbol geregelt.

```
e2-cli destroyamount <asset-id>
e2-cli getwalletinfo
```

In diesem Abschnitt haben wir gesehen, wie man einen Vermögenswert ausgibt und wie man den Reissuance-Token nutzt, der optional als Teil der Vermögenswertausgabe erstellt wird. Wir haben auch gesehen, dass die Übertragung eines Reissuance-Tokens genauso einfach ist wie die Übertragung eines anderen Vermögenswerts und dass der Besitz einer beliebigen Menge eines Reissuance-Tokens dem Inhaber das Recht gibt, weitere Exemplare des zugehörigen Vermögenswerts auszugeben. Daher ist es sehr wichtig zu kontrollieren, wer in Ihrem Netzwerk Zugang zu Reissuance-Tokens hat. Wir haben auch gesehen, wie eine Menge eines Vermögenswerts zerstört werden kann und dass dieser Prozess nicht durch den Besitz des Reissuance-Tokens kontrolliert wird.

# Element Föderation

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## Unterschriftssperre

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

![Video](https://youtu.be/kxWX91fCnus?si=KItm_Am3_RrBcLBN)

Elements unterstützt ein föderiertes Unterzeichnungsmodell, mit dem Sie die Anzahl der Mitglieder der Strong Federation festlegen können, die einen vorgeschlagenen Block unterzeichnen müssen, um einen gültigen Block zu erzeugen.

Bisher haben wir zur Vereinfachung des Beispiels Blöcke mit dem Befehl "Generate" erstellt, der nicht die Anforderung einer Mehrfachsignatur erfüllen musste, damit die erstellten Blöcke vom Netz als gültig akzeptiert werden.

Wir werden unsere Knoten so einrichten, dass die Erstellung von 2-of-2-Multisig-Blöcken erforderlich ist. Dies wird mit dem signblockscript-Parameter eingerichtet, der der Konfigurationsdatei hinzugefügt oder dem Knoten beim Starten übergeben werden kann. Um eine Kette mit diesem Parameter zu initialisieren, müssen wir zunächst das Skript erstellen, aus dem sie besteht.

Dazu verwenden wir einige vorhandene Knoten, speichern die von ihnen ausgegebenen Daten und löschen dann die Kette, damit wir sie mit unserem Parameter signblockscript neu starten können. Dies ist notwendig, da das Skript Teil der Konsensregeln des Netzwerks ist und bei der Initialisierung der Kette festgelegt werden muss. Es kann nicht zu einem späteren Zeitpunkt zu einer bereits bestehenden Kette hinzugefügt werden.

Wir benötigen Zugang zu zwei Elements-Knoten, die wir e1 und e2 nennen. Die Blockchains der Knoten wurden zurückgesetzt und das Standardvermögen zwischen ihnen aufgeteilt.

Stellen Sie sicher, dass der Parameter con_max_block_sig_size in Ihrer Datei elements.conf auf einen hohen Wert gesetzt ist, da sonst die Blocksignierung später in diesem Abschnitt fehlschlägt. Für dieses Lernprogramm haben wir con_max_block_sig_size=2000 eingestellt.

Da wir unsere Blockchain zurücksetzen und die mit e1 und e2 verknüpften Wallets löschen werden, müssen wir eine Kopie der Adressen, öffentlichen und privaten Schlüssel machen, die wir zur Erstellung des Blocksignaturskripts verwenden, damit wir sie später wieder verwenden können.

Zunächst muss jeder der künftigen Blocksignaturknoten eine neue Adresse erzeugen, von der Sie eine Kopie erstellen müssen.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Dann müssen wir die öffentlichen Schlüssel aus den Adressen extrahieren und sie für die spätere Verwendung aufbewahren.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Dann extrahieren wir die privaten Schlüssel, die wir später wieder importieren, damit die Knoten die Blöcke signieren können, nachdem wir unsere Blockchain und Wallet-Daten neu initialisiert haben.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Nun müssen wir ein neues Skript mit 2 von 2 Multisignaturanforderungen erstellen. Dazu verwenden wir den Befehl createmultisig und übergeben als ersten Parameter den Wert 2 sowie zwei öffentliche Schlüssel. Es sind diese Schlüssel, deren Besitz später bei der Erstellung des Blocks nachgewiesen werden muss.

Jeder der beiden Knoten, e1 oder e2, könnte die Multisig erzeugen.

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

Damit haben wir unser Redeskript, das Sie zur späteren Verwendung kopieren können.

Nun müssen wir die bestehenden Blockchain- und Wallet-Daten löschen, damit wir mit dem neuen signblockscript als Teil der Konsensregeln der Kette neu beginnen können. Aus diesem Grund mussten wir zuvor eine Kopie einiger Daten erstellen, z. B. der privaten Schlüssel, die in der neuen Kette zum Signieren von Blöcken verwendet werden. Dies müssen Sie tun, bevor Sie fortfahren.

Nachdem wir unsere bestehenden Brieftaschen- und Kettendaten gelöscht haben, können wir nun unsere Knoten starten und sie mit dem Parameter signblockscript eine neue Kette initialisieren lassen. Geben wir -evbparams=dynafed:0::: ein, um die dynafed-Aktivierung zu deaktivieren, da wir diese erweiterte Funktion für dieses Beispiel nicht benötigen.

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

Jetzt müssen wir die privaten Schlüssel importieren, die wir zuvor gespeichert haben, damit unsere Knoten alle vorgeschlagenen Blöcke signieren und vervollständigen können.

```
e1-cli importprivkey <e1-priv-key>
e2-cli importprivkey <e2-priv-key>
```

Die Verwendung des generate-Befehls sollte nun fehlschlagen, da er die erforderlichen Regeln für die Blocksignierung nicht erfüllt, die nun von unseren Knoten durchgesetzt werden.

```
e1-cli -generate 1
```

Um einen neuen Block vorzuschlagen, kann jeder Knoten den Befehl getnewblockhex aufrufen. Dieser gibt das Hexadezimalzeichen eines neuen Blocks zurück, der signiert werden muss, bevor er von einem Knoten in unserem Netzwerk akzeptiert wird.

```
e1-cli getnewblockhex
```

Denken Sie daran, dass der Befehl nur einen vorgeschlagenen Block erstellt, nicht aber einen generiert.

Um dies zu bestätigen, können wir sehen, dass es derzeit keine Blöcke in unserer Blockchain gibt.

```
e1-cli getblockcount
```

Wenn wir versuchen, das Blockhex zu übermitteln, ohne es vorher zu signieren.

```
e1-cli submitblock <block-hex>
```

Wir erhalten eine Meldung, dass der Blockproof ungültig ist. Dies liegt daran, dass er noch nicht von 2 der erforderlichen 2 Parteien unterzeichnet wurde.

Bringen wir also e1 dazu, den vorgeschlagenen Block zu unterzeichnen.

```
e1-cli signblock <block-hex>
```

Lassen Sie e2 das Feld unterschreiben.

```
e2-cli signblock <block-hex>
```

Beachten Sie, dass e2 die von e1 erzeugte Ausgabe, die den vorgeschlagenen Block signiert, nicht signiert. Beide signieren den vorgeschlagenen Block Hex unabhängig von den Ergebnissen des jeweils anderen.

Nun müssen wir die Blocksignaturen von e1 und e2 kombinieren. Jeder der beiden Knoten kann dies tun, er braucht nur das signierte Blockhex des anderen Knotens.

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

Wie Sie sehen, gibt der Befehl combineblocksigs das Hexadezimalsymbol des signierten Blocks sowie den Status "complete" aus, der besagt, dass das Hexadezimalsymbol des Blocks zum Übertragen bereit ist.

Nun können beide Knoten das fertige Blockhex übermitteln. Wir lassen e1 das tun.

```
e1-cli submitblock <combined-signed-hex>
```

Überprüfung, ob die Übermittlung gültig war.

```
e1-cli getblockcount
e2-cli getblockcount
```

Sie können sehen, dass sowohl e1 als auch e2 den Block als gültig akzeptiert haben und ihn an die Spitze ihrer lokalen Kopien der Blockchain gesetzt haben.

Um den Prozess zusammenzufassen. In diesem Abschnitt haben wir:


- Vorgeschlagen wird ein Block.
- Jeder Knotenpunkt hat es unterschrieben.
- Kombinieren Sie die Unterschriften.
- Es wurde geprüft, ob die Signaturen gültig sind und den Schwellenwert der Kette für die Wiederbeschriftung erfüllen.
- Der Block wurde eingereicht.

Jeder Knoten im Netzwerk validierte den Block und fügte ihn zu seiner lokalen Kopie der Blockchain hinzu.

### Block SIgning

Obwohl der Prozess auf den ersten Blick komplex erscheint, ist die Reihenfolge der Blocksignierung in Elements immer gleich und die Ersteinrichtung muss nur einmal durchgeführt werden:

1. Ersteinrichtung (einmalig durchgeführt)

2. Unter Verwendung der öffentlichen Schlüssel der föderierten Blocksignierer wird eine Multisignaturadresse namens "signblockscript" erstellt.

3. Das daraus resultierende Redeem-Skript wird zum Starten einer neuen Blockchain verwendet.

4. Blockproduktion (laufend)

5. Vorgeschlagene Blöcke werden erstellt und zur Unterzeichnung ausgetauscht.

Sobald eine bestimmte Anzahl von Unterzeichnern den vorgeschlagenen Block unterzeichnet hat, wird er kombiniert und an das Netz übermittelt. Wenn er die Kriterien des "Signblockscript" der Kette erfüllt, akzeptieren die Knoten ihn als gültigen Block.

## Element als Seitenkette

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

![Video](https://youtu.be/egYzj4N8CB8?si=v7_-IXsjHPE-ARDe)

Elements ist eine Open-Source-Blockchain-Plattform für allgemeine Zwecke, die auch an eine bestehende Blockchain wie Bitcoin "angekoppelt" werden kann. Wenn Elements an eine andere Blockchain gekoppelt ist, wird es als "Sidechain" bezeichnet. Sidechains ermöglichen den wechselseitigen Transfer von Vermögenswerten von einer Kette zur anderen. Die Implementierung von Elements als Sidechain ermöglicht es, einige der inhärenten Einschränkungen der Mainchain zu umgehen und gleichzeitig ein hohes Maß an Sicherheit beizubehalten, das die auf der Mainchain gesicherten Vermögenswerte bieten.

Während eine Sidechain die Mainchain und ihre Transaktionshistorie kennt, hat die Mainchain keine Kenntnis von der Sidechain und benötigt auch keine für ihren Betrieb. Dadurch können Sidechains ohne Einschränkungen oder Verzögerungen, die mit Vorschlägen zur Verbesserung des Mainchain-Protokolls verbunden sind, Innovationen einführen. Anstatt zu versuchen, das Hauptprotokoll direkt zu ändern, ermöglicht die Erweiterung des Hauptprotokolls, dass die Mainchain selbst sicher und spezialisiert bleibt und den reibungslosen Betrieb der Sidechain unterstützt.

Durch die Erweiterung der Funktionalität von Bitcoin und die Ausnutzung der zugrundeliegenden Sicherheit ist eine Elements-basierte Sidechain in der Lage, neue Funktionen bereitzustellen, die den Nutzern der Mainchain bisher nicht zur Verfügung standen. Ein Beispiel für eine Elements-basierte Sidechain im Produktionseinsatz ist das Liquid Network.

Um eine Elements-Blockchain als Sidechain zu initialisieren, müssen wir den Skriptparameter federated peg verwenden. Dieser Parameter kann in der Konfigurationsdatei eines Knotens festgelegt oder beim Start übergeben werden.

Das föderierte Peg-Skript legt fest, welche Mitglieder der starken Föderation Peg-In- und Peg-Out-Funktionen ausführen können. Diese Funktionäre werden als "Wächter" bezeichnet, da sie die Mainchain und die Sidechain auf gültige Peg-In- und Peg-Out-Transaktionen überwachen und diese, falls gültig, ausführen. Ausbuchen" bedeutet, gebundene Vermögenswerte aus der Sidechain in die Mainchain zu verschieben, und "Einbuchen" bedeutet, gebundene Vermögenswerte aus der Mainchain in die Sidechain zu verschieben. Wenn wir "in die Sidechain verschieben" sagen, meinen wir eigentlich, dass die Gelder in einer Multi-Signatur-Adresse auf der Mainchain gesperrt werden und ein entsprechender Betrag des Vermögenswertes auf der Elements-Sidechain erstellt wird. Wenn wir "aus der Sidechain auslagern" sagen, meinen wir damit, dass Vermögenswerte auf der Elements-Sidechain vernichtet werden und der entsprechende Betrag aus den gesperrten Mitteln auf der Mainchain freigegeben wird. Die Erlaubnis, die Peg-In- und Peg-Out-Funktionen auszuführen, erfordert, dass die Funktionäre das Eigentum an den öffentlichen Schlüsseln nachweisen, die im föderierten Peg-Skript verwendet werden. Dies geschieht durch die Verwendung der entsprechenden privaten Schlüssel.

Um ein föderiertes Peg-Skript zu erstellen, müssen wir daher zunächst für jeden unserer Knoten einen öffentlichen Schlüssel erzeugen. Außerdem müssen wir die zugehörigen privaten Schlüssel für die spätere Verwendung speichern, da wir alle bestehenden Kettendaten löschen und eine neue Kette mit dem federated peg script initialisieren müssen. Der Grund dafür ist, dass das federated peg-Skript Teil der Konsensregeln einer Sidechain ist und nicht zu einem späteren Zeitpunkt auf eine bestehende, nicht gepeggte Blockchain angewendet werden kann.

Lassen Sie uns also für jeden unserer Knoten eine Adresse generieren, die relevanten Daten für die spätere Verwendung speichern und das federated peg-Skript generieren, das wir später zur Initialisierung unserer Sidechain verwenden werden.

Zunächst muss jeder unserer Knoten, die als Wächter in unserem Netz fungieren werden, eine neue Adresse generieren.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Dann validieren wir die Adresse, um die öffentlichen Schlüssel zu erhalten.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Und rufen Sie dann die mit jeder Adresse verbundenen privaten Schlüssel ab.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Speichern Sie die privaten und öffentlichen Schlüssel zur späteren Verwendung.

Jetzt müssen wir die bestehenden Blockchain- und Wallet-Daten löschen, da wir eine neue Chain mit einem federated peg-Skript initialisieren werden. Sie können dies jetzt tun. Vergessen Sie nicht, den Bitcoin-Daemon zu starten, den wir zum Einbinden benötigen.

Jetzt können wir eine neue Kette mit einem föderierten Peg-Skript initialisieren, das mit den öffentlichen Schlüsseln erstellt wurde, die wir zuvor gespeichert haben. Die Zahlen, die wir eingeben und die unsere öffentlichen Schlüssel umgeben, definieren und begrenzen die Anzahl der verwendeten Schlüssel und den Schlüsselbesitz, der nachgewiesen werden muss, um in unsere Sidechain ein- und aus ihr auszusteigen.

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

Jetzt importieren wir die privaten Schlüssel, die wir zuvor gespeichert haben, damit unsere Knoten später signieren und die Übertragung von Vermögenswerten zwischen Ketten abschließen können und die Anforderungen des federated peg script erfüllen.

```
e1-cli importprivkey <priv-key-1>
e2-cli importprivkey <priv-key-1>
```

Wir müssen nun einige Blöcke auf beiden Ketten reifen lassen. Die Reifung von Blöcken ist eine Voraussetzung für den Peg-Prozess, da sie vor Blockumstrukturierungen auf der Mainchain schützt, die zu einer Aufblähung des Angebots an gebundenen Vermögenswerten auf der Sidechain führen.

Um diesen Abschnitt auf den Verbundpflock zu konzentrieren, werden wir Blöcke ohne das Blocksignierungsmodell generieren, das wir im letzten Abschnitt betrachtet haben, und wir kehren zur Verwendung des Befehls "generate" zurück, um neue Blöcke zu erstellen.

```
b-cli generate 101
e1-cli generate 1
```

Wir brauchen jetzt nicht unbedingt Blöcke für Elemente zu erzeugen. Aber lassen Sie uns trotzdem einen generieren. Das ist eine gute Praxis, um mögliche Inkonsistenzen zu vermeiden.

Jetzt ist unsere Kette bereit zum Einhängen. Zum Einhängen müssen wir mit dem Befehl getpeginaddress eine spezielle Art von Adresse erzeugen. Beachten Sie, dass die Zeitspanne zwischen der Erzeugung einer Peg-in-Adresse mit getpeginaddress und ihrer Beanspruchung mit claimpegin so gering wie möglich gehalten werden sollte. Peg-in-Adressen sind nicht dauerhaft haltbar und sollten nicht wiederverwendet werden.

```
e1-cli getpeginaddress
```

Sie können sehen, dass der Befehl eine neue Mainchain-Adresse sowie ein neues Skript erstellt, das befriedigt werden muss, um die eingezahlten Gelder einzufordern. Die Mainchain-Adresse ist eine "Pay-to-Script-Hash"-Adresse, die von Funktionären verwendet wird, die im Elements-Netzwerk die Rolle des Wächters übernehmen.

Wie getnewaddress fügt auch getpeginaddress der Wallet des aufrufenden Knotens ein neues Geheimnis hinzu, so dass es wichtig ist, eine Sicherung der Wallet-Datei in den Prozess der Knotenverwaltung einzubeziehen.

Wir werden nun einige Bitcoin von der Mainchain an die Sidechain senden. Unsere Mainchain-Regressionstest-Wallet enthält bereits einige Gelder.

```
b-cli getwalletinfo
```

Wir können sehen, dass die Brieftasche 50 Bitcoin enthält. Wir werden eine Bitcoin von der Mainchain an die Sidechain senden. Wir müssen das Geld an die Mainchain-Adresse senden, die unser Knoten zuvor generiert hat.

```
b-cli sendtoaddress <e1-pegin-address>
```

Wir müssen die ID dieser Transaktion aufbewahren, da wir sie später für den Nachweis der Finanzierung benötigen.

Wir können nun sehen, dass der Kontostand der Mainchain um den Betrag, den wir gesendet haben, plus einen zusätzlichen kleinen Betrag zur Deckung der Transaktionsgebühren, gesunken ist.

```
b-cli getwalletinfo
```

Wir müssen die Transaktion erneut reifen lassen.

```
b-cli generate 101
```

Damit unser Elements-Knoten die Peg-In-Gelder beanspruchen kann, müssen wir den "Beweis" erbringen, dass die Peg-In-Transaktion durchgeführt wurde. Der kryptografische Beweis verwendet die ID der Finanzierungstransaktion, um den Merkel-Pfad zu berechnen, und beweist, dass die Transaktion in einem bestätigten Block vorhanden ist.

```
b-cli gettxoutproof '["<tx-id>"]'
```

Wir benötigen auch die Rohdaten der Transaktionen.

```
b-cli getrawtransaction <tx-id>
```

Mit dem Nachweis und den Rohdaten für die Peg-In-Transaktion kann unser Element-Knoten nun die Peg-In-Transaktion unter Verwendung der Rohtransaktion und des Transaktionsnachweises geltend machen.

```
e1-cli claimpegin <raw> <proof>
```

Beachten Sie, dass es ein optionales drittes Argument gibt, das wir an claimpegin hätten übergeben können. Dieser dritte Parameter kann verwendet werden, um die Sidechain-Adresse anzugeben, an die die geforderten Gelder gesendet werden sollen. In unserem Beispiel war dies nicht erforderlich, da wir den Befehl von demselben Knoten aus aufgerufen haben, dem die Adresse gehört, an die die geforderten Gelder gehen.

Überprüfung des Saldos von e1.

```
e1-cli getwalletinfo
```

Generierung eines Blocks zur Bestätigung des Anspruchs.

```
e1-cli generate 1
```

Überprüfung des Saldos von e1.

```
e1-cli getwalletinfo
```

Wir können sehen, dass die Einsteckung erfolgreich beantragt wurde.

Bei der Auszahlung ist der Prozess ähnlich. Es wird eine Adresse generiert, Geldmittel werden an diese Adresse gesendet und die Geldmittel werden freigegeben, wenn die Transaktion gültig ist. Wir werden nicht den gesamten Peg-Out-Prozess behandeln, da er Arbeiten auf der Mainchain beinhaltet, die den Rahmen dieses Kurses sprengen würden. Die Schritte in Bezug auf die Elemente-Ereignisse sind, dass eine Adresse auf der Mainchain generiert wird.

```
b-cli getnewaddress
```

Mit dem Befehl sendtomainchain werden Gelder von einem Elements-Knoten an die Mainchain-Adresse gesendet.

```
e1-cli sendtomainchain <new-address> 1
```

Generierung eines Blocks zur Bestätigung der Transaktion.

```
e1-cli generate 1
```

Prüfen Sie das Guthaben in der Brieftasche des Knotens.

```
e1-cli getwalletinfo
```

Und sehen Sie, dass der Saldo gesunken ist.

In diesem Abschnitt haben wir gesehen, wie das geht:


- Erzeugen Sie ein Skript für den Verbundpflock.
- Initialisieren Sie eine neue Kette, die das Skript als Netzkonsensparameterregel verwendet.
- Senden Sie Geld von der Mainchain zur Sidechain.
- Beanspruchen Sie die Mittel innerhalb der Elements-Sidechain.
- Verstehen Sie, wie das Zurücksenden von Geldern an die Mainchain gestartet wird.

### FederatedPegScript

Damit Elements als Sidechain funktionieren kann, muss der Genesis-Block in seiner Blockchain mit einem `fedpegscript` erstellt werden. Dies geschieht durch die Übergabe des Parameters "Fedpegscript" beim Starten des Knotens. Das Skript ist dann Teil der Konsensregeln der Elements-Blockchain und ermöglicht die Validierung und Bearbeitung von Peg-In- und Peg-Out-Anfragen.

Das "fedpegscript" besteht aus öffentlichen Schlüsseln, die von denjenigen kontrolliert werden, die berechtigt sind, die Pflockaktionen durchzuführen. Das folgende Beispiel zeigt das Format eines 2-von-2-Multisignatur-Fedpegscript:

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

Hinweis: Die Zeichen außerhalb der öffentlichen Schlüssel sind Begrenzer, die den öffentlichen Schlüssel und die Anforderungen an "n von m" angeben. Die Vorlage für ein 1-of-1-Fedpegscript wäre zum Beispiel "5121<öffentlicher Schlüssel 1>51ae".

### Einstecken

Bevor ein Peg-In von einer Elements-Sidechain akzeptiert werden kann, muss es ausreichend Bestätigungen auf der Mainchain geben. Dies ist notwendig, um eine Inflation des Angebots des gebundenen Vermögenswerts auf der Elements-Sidechain zu vermeiden, die durch eine Umstrukturierung der Mainchain verursacht werden könnte.

Kurze Umstrukturierungen der Spitze der Bitcoin-Blockchain werden als Teil des normalen Betriebs des Proof of Work (PoW) Konsensmechanismus erwartet. Daher akzeptiert Elements ein Peg-In nur dann als gültig, wenn es eine ausreichende Tiefe innerhalb der Bitcoin-Blockchain hat. Dies dient dazu, zu verhindern, dass Elements denselben Peg-In mehr als einmal annimmt.

### Peg-Out

Ein Peg-Out findet statt, wenn ein Elements-Knoten den Befehl `sendtomainchain` aufruft, der als Eingabe eine Mainchain-Adresse (das Peg-Out-Ziel) sowie den Betrag des verpfändeten Vermögenswerts, der `entnommen` werden soll, erhält. Dadurch wird eine Ausgliederungstransaktion auf der Sidechain erzeugt. Sobald die Funktionäre, die als Watchmen fungieren, feststellen, dass die Peg-Out-Transaktion auf der Sidechain bestätigt wurde, kümmern sie sich um die tatsächliche Freigabe des Vermögenswerts auf der Mainchain an das Peg-Out-Ziel, wie wir in früheren Abschnitten des Kurses gelernt haben.

## Elemente als eigenständige Blockchain

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

![Video](https://youtu.be/u-3rV7DGtD0?si=G1__H0Uelf4sTUDM)

Bislang haben wir uns angesehen, wie Elements als Sidechain betrieben werden kann. Es kann jedoch auch als eigenständige Blockchain-Lösung mit einem eigenen Standard-Asset betrieben werden. In diesem Fall behält eine Elements-Blockchain alle Funktionen einer Sidechain-Implementierung bei, wie z. B. vertrauliche Transaktionen und ausgegebene Vermögenswerte, benötigt aber kein Peg-in oder Peg-out, um Standard-Asset-Beträge aus dem Umlauf hinzuzufügen oder zu entfernen.

In diesem Abschnitt werden wir:

Initialisieren Sie eine neue Elements-Blockchain mit einem Standard-Asset namens "newasset".

Geben Sie an, dass 1.000.000 `Newasset` zusammen mit 2 Wiederausgabemarken dafür erstellt werden sollen.

Beanspruchen Sie alle "Newasset"-Münzen, die jeder ausgeben kann.

Beanspruchen Sie alle Wiederausgabemarken für "newasset", die jeder ausgeben kann.

Senden Sie den Vermögenswert und sein Re-Issuance-Token an die Brieftasche eines anderen Knotens.

Mehr 'newasset' von beiden Knotenpunkten ausgeben.

Um ein Elements-Netzwerk für den Betrieb als eigenständige Blockchain zu initialisieren, muss jeder Knoten mit einigen grundlegenden Parametern gestartet werden. Sie werden verwendet, um dem Knoten mitzuteilen, dass er nicht versuchen soll, Peg-Ins von einer anderen Blockchain zu validieren, den Namen des Standard-Assets des Netzwerks und die Menge des Standard-Assets und des zugehörigen Reissue-Tokens zu erstellen.

Wir starten nun eine neue Kette mit diesen Parametern auf unseren beiden verbundenen Elements-Knoten. Wir nennen das Standard-Asset "newasset" und geben eine Million davon und zwei "newasset"-Wiederausgabemarken aus.

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

Beachten Sie, dass die hier verwendeten Beträge die kleinste Stückelung sind, die das Netzwerk akzeptieren kann, so dass die zweihundert Millionen Neuausgabemünzen tatsächlich zwei ganzen Münzen entsprechen. Das Gleiche gilt für die Stückelung der ersten kostenlosen Münzen.

Prüfen Sie den aktuellen Kontostand unserer Knoten.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Wir können sehen, dass die Initialisierung korrekt funktioniert hat.

Da die anfängliche Ausgabe von Vermögenswerten als "jeder kann sie ausgeben" angelegt wird, wird e1 sie alle beanspruchen, so dass wir e2 den Zugang zu ihnen entziehen können.

```
e1-cli getnewaddress
e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

Beachten Sie, dass wir "newasset" nicht als zu versendendes Wirtschaftsgut angeben müssen, da es bereits das Standardwirtschaftsgut und damit auch das Standardwirtschaftsgut für die Zahlung der Netzgebühren ist.

Innerhalb von Elements können Sie mehrere Asset-Typen an dieselbe Adresse senden. Wir können also die Adresse, die wir gerade für den Empfang des Standard-Assets generiert haben, wiederverwenden und sie als Zieladresse für die neu ausgegebenen Token verwenden.

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Bestätigen Sie die Transaktionen.

```
e1-cli generate 101
```

Wir überprüfen jetzt, ob e1 der einzige Inhaber des Vermögenswerts und des Tokens für die Neuausgabe ist.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Wie wir sehen können, ist das tatsächlich der Fall.

Jetzt schicken wir einen Teil des "newasset" an e2, der derzeit einen Saldo von Null hat.

```
e2-cli getnewaddress
e1-cli sendtoaddress <e2-address> 500 "" "" false
```

Beachten Sie, dass wir den Typ des zu sendenden Assets nicht angeben mussten, da "newasset" als Standard-Asset des Netzes erstellt wurde

Lassen Sie uns auch einige der Neuausgabemarken für "newasset" an e2 senden.

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Bestätigen Sie die Transaktionen.

```
e1-cli generate 101
```

Wir können überprüfen, ob die Geldbörsen entsprechend aktualisiert wurden.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Nun werden wir einige der Standard-Assets von e1 neu ausgeben. Beachten Sie, dass die Möglichkeit dazu durch den Startparameter initialreissuancetokens aktiviert wird. Wenn er weggelassen oder auf Null gesetzt wird, führt dies zu einem Standard-Asset, das zu einem späteren Zeitpunkt nicht mehr neu ausgegeben werden kann.

```
e1-cli reissueasset newasset 100
```

Wir konnten die Bezeichnung "newasset" verwenden, anstatt den hexadezimalen Wert anzugeben, da eine Elementkette immer ihre Standardanlage bezeichnet.

Überprüfung, ob die Neuausgabe der Standardanlage funktioniert hat:

```
e1-cli generate 101
e1-cli getwalletinfo
```

Wir werden nun beweisen, dass e2, da es einige der Token für die Neuausgabe von "newasset" besitzt, auch den Standardwert neu ausgeben kann.

```
e2-cli reissueasset newasset 100
```

Überprüfung, ob die Neuausgabe der Standardanlage durch e2 funktioniert hat.

```
e2-cli generate 101
e2-cli getwalletinfo
```

In diesem Abschnitt haben wir Elements als eigenständige Blockchain eingerichtet und überprüft, ob die Grundfunktionen wie erwartet funktionieren.

Wir haben Startparameter verwendet, um:

Initialisieren Sie eine neue Elements-Blockchain mit einem Standard-Asset namens "newasset".

Geben Sie die Menge des Standard-Assets an, das bei der Initialisierung der Kette erstellt werden soll.

Erstellen Sie einige Neuausgabemarken für den Standardwert und geben Sie mehr von dem Standardwert von beiden Knotenpunkten aus.

In unserem eigenständigen Blockchain Elements Netzwerk funktionieren alle anderen Transaktionen auf die gleiche Weise wie in den Beispielen, die in den Hauptabschnitten des Kurses behandelt werden, aber sie verwenden "newasset" anstelle von "Bitcoin" als Standard- und Gebührenwert.

### Parameter für den Knotenstart und die Ketteninitialisierung

Um einen Elements-Knoten als eigenständige Blockchain zu betreiben, müssen ein paar Parameter zusammen verwendet werden. Wir werden uns jetzt jeden einzelnen ansehen und herausfinden, was sie bewirken.

#### validatepegin=0

Da eine eigenständige Blockchain keine Peg-In- oder Peg-Out-Transaktionen validieren muss, müssen wir diese Prüfungen deaktivieren. Mit dieser Einstellung müssen Sie die Bitcoin-Client-Software nicht ausführen oder eine Kopie der Bitcoin-Blockchain speichern, da das Elements-Netzwerk unabhängig arbeitet.

#### defaultpeggedassetname

Hier können Sie den Namen des Standard-Assets angeben, das bei der Initialisierung der Blockchain erstellt wird.

#### initiale Freimünzen

Die Anzahl (im Äquivalent der Bitcoin-Einheit Satoshi) des zu erstellenden Standard-Assets.

#### erstausgabescheine

Die Anzahl (im Äquivalent der Bitcoin-Einheit Satoshi) der neu zu erstellenden Token für den Standardwert. Ohne diese Angabe wäre es nicht möglich, mehr von dem Standard-Asset zu erstellen. Wenn es nicht möglich sein soll, mehr von dem Standard-Asset zu erstellen, kann dies auf Null gesetzt oder weggelassen werden.

Mit diesen Parametern würde der gemeinsame Start eines Knotens etwa so aussehen:

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### Grundlegende Operationen

Der Parameter "defaultpeggedassetname" weist dem Standard-Asset eine Bezeichnung zu. Ohne diese Einstellung wird das Standard-Asset automatisch "Bitcoin" genannt. In früheren Abschnitten mussten wir, wenn wir Assets, die wir selbst ausgestellt hatten, an einen anderen Knoten schickten, entweder das Asset-Hex oder das lokal angewendete Asset-Label angeben, um Elements mitzuteilen, welches Asset wir senden wollten. Da `defaultpeggedassetname` für alle Knoten gilt, brauchen wir es nicht zu benennen, wenn wir es senden, auch wenn sein Name nicht `bitcoin` ist. Jede Funktion, die vorher standardmäßig `Bitcoin` gesendet hat, wird nun das senden, was Sie als Standard-Assetname gewählt haben.

Es ist also ganz einfach, 10 der neuen Standardwerte an eine Adresse zu senden:

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

Wenn Sie den Knoten mit einem Wert für "Initialreissuancetokens" versehen haben, der größer als Null ist, können Sie auch mehr von dem Standard-Asset neu ausgeben, was nicht möglich ist, wenn Sie Elements als Sidechain ausführen.

Dazu muss jeder Knoten, der einen mit dem Standard-Asset verbundenen Token-Betrag besitzt, nur einen Befehl in der Form ausgeben:

```
e1-cli reissueasset <default asset name> <amount>
```

Mit den oben genannten Parametern können Sie Elements als eigenständige Blockchain mit eigenem Standard-Asset betreiben, entkoppelt von Bitcoin und anderen Blockchains.

## Schlussfolgerung

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

![Video](https://youtu.be/CTMdamTZBBM?si=16LBcXvN4pBfC7lr)

In diesem Kurs haben wir gelernt, dass Elements ein Open-Source-Netzwerkprotokoll ist, das als Sidechain zu einer anderen Blockchain oder als eigenständige Blockchain-Lösung implementiert werden kann.

Wir haben gesehen, dass der Quellcode und die Website für Elements (https://github.com/ElementsProject/elements) auf GitHub gehostet werden und dass es Community-Diskussionsforen wie Build On L2 (https://community.liquid.net/c/developers/) oder das Liquid Developers Telegram (https://t.me/liquid_devel) gibt, die genutzt werden können, um mehr über die Bereitstellung und Entwicklung von Anwendungen auf Elements und Liquid zu erfahren. Wichtige Funktionen wie Confidential Transactions und Issued Assets wurden ebenso behandelt wie die Art und Weise, wie Mitglieder einer Strong Federation eine föderierte Blocksignierung und den 2-Way-Peg-Mechanismus ermöglichen.

Der nächste Schritt besteht darin, sich selbst mit einem kumulativen Quiz herauszufordern, das alle vorangegangenen Abschnitte abdeckt, und dann Ihre Elements-Reise zu beginnen... viel Glück!

# Schlussfolgerung

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## Rezensionen und Bewertungen

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Schlussfolgerung

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

Herzlichen Glückwunsch zum Abschluss dieses Kurses!

Wir freuen uns sehr, dass Sie diesen Meilenstein auf Ihrer Lernreise erfolgreich erreicht haben. Durch Ihren Einsatz und Ihr Engagement haben Sie wertvolle Kenntnisse und Fähigkeiten erworben, die Ihnen in Ihrer beruflichen Entwicklung von großem Nutzen sein werden.