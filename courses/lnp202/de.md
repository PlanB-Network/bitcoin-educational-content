---
name: Einrichten Ihres ersten Lightning-Knotens
goal: Verstehen, Installieren, Konfigurieren und Verwenden eines Lightning-Knotens
objectives: 


  - Die Rolle und den Zweck eines Lightning-Knotens zu verstehen.
  - Identifizieren Sie die verschiedenen verfügbaren Softwarelösungen.
  - Installieren und konfigurieren Sie einen Lightning-Knoten (LND).
  - Verbinden Sie ein Aufwandskonto.
  - Kennen Sie die Risiken bei der Verwendung eines Lightning-Knotens.


---

# Ihr erster Schritt zur Autonomie bei Lightning



Sie haben bereits Ihren ersten sats erworben, Ihre Eigenmittel gesichert und einen Bitcoin-Knoten eingesetzt, um bei der Nutzung von on-chain souverän zu sein. Der nächste Schritt besteht darin, die gleiche Autonomie auf Lightning zu erlangen: Genau das ist das Ziel dieses Kurses.



LNP202 richtet sich an fortgeschrittene Benutzer und führt Sie Schritt für Schritt durch die Einrichtung Ihres ersten Lightning-Knotens, ohne dass Sie über fortgeschrittene technische Kenntnisse verfügen müssen.



Sie lernen, wie Sie LND auf Umbrel installieren, Ihre Kanäle öffnen und verwalten, Ihren Knotenpunkt überwachen und ein mobiles wallet anschließen, so dass Sie eine Erfahrung genießen können, die mit der eines verwahrten wallet vergleichbar ist, während Sie die volle Kontrolle über Ihre Mittel behalten.



+++


# Einführung


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Überblick über den Kurs


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202 ist ein praxisorientierter Kurs, der darauf abzielt, Sie durch den Betrieb Ihres eigenen Knotens mit Lightning unabhängig zu machen. Das Ziel ist einfach: Beginnen Sie mit einem bereits vorhandenen Bitcoin-Knoten, richten Sie LND auf Umbrel ein, sichern Sie ihn ordnungsgemäß, öffnen und verwalten Sie Ihre ersten Kanäle, und nutzen Sie dann Ihren Knoten täglich von einem mobilen wallet aus. Dieser Kurs setzt voraus, dass Sie bereits BTC 202 besucht haben, da ich davon ausgehe, dass Ihr Bitcoin-Knoten auf Umbrel eingerichtet und synchronisiert ist. Wir werden hier nicht noch einmal darauf eingehen, wie man einen Bitcoin-Knoten einrichtet.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Für ein besseres Verständnis der internen Mechanik von Lightning ist der Kurs LNP 201 ebenfalls sehr zu empfehlen, obwohl er keine Voraussetzung für diesen Kurs ist:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Im ersten Teil dieses LNP202-Kurses werfen wir einen Blick darauf, was ein Lightning-Knoten wirklich ist, wie er sich von einem einfachen wallet unterscheidet und warum der Betrieb eines persönlichen Knotens die einzige Möglichkeit ist, Lightning zu nutzen, ohne Ihren sats an eine vertrauenswürdige Drittpartei zu delegieren. Dieser Abschnitt schließt mit einer strategischen Entscheidung: Welche Lösung ist die richtige für Sie, von den einfachsten Ansätzen bis hin zum klassischen Lightning-Knoten, den wir in diesem Kurs implementieren werden.



In Teil 2 des Kurses werden Sie LND auf Umbrel installieren und dann die Elemente einrichten, die die kostspieligsten Fehler verhindern: eine realistische Backup-Strategie und Schutz vor Betrug durch einen Watchtower. Sobald diese Grundlagen vorhanden sind, werden Sie Ihren ersten Kanal eröffnen, damit Sie mit Ihrer eigenen Infrastruktur auf Lightning zahlen können.



Sie sehen also: In diesem LNP202-Kurs werden wir einen Lightning-Knoten im Plug-and-Play-Modus über Umbrel einrichten und nicht über die klassische Kommandozeile, um ihn für fortgeschrittene Benutzer geeignet zu machen. Wenn Sie eine Befehlszeilen-Installation bevorzugen, empfehle ich Ihnen, dem unten stehenden Tutorial zu folgen. Weitere, fortgeschrittenere, kommandozeilenorientierte Lightning-Kurse sind ebenfalls in Vorbereitung.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Teil 3 führt Sie dann von einem funktionierenden Knoten zu einem, den Sie zu kontrollieren wissen. Sie beginnen mit der Bestimmung des Betreiberprofils Ihres Lightning-Knotens (Verbraucher, Händler oder Router) und setzen sich dann mit einer kompletten Management-Software auseinander, um Ihre Kanäle zu verfolgen und Ihre Topologie sauber zu steuern. Schließlich werden Sie sich mit einem sehr wichtigen Punkt von Lightning befassen: wie Sie eingehende Liquidität erhalten, sei es über bezahlte oder kooperative Lösungen.



In Teil 4 geht es um den täglichen Gebrauch. Sie werden eine Verbindung zwischen Ihrem Knotenpunkt und einem mobilen Kunden herstellen, damit Sie einfach von Ihrem Smartphone aus bezahlen und abkassieren können, ohne die Selbstverwahrung aufzugeben. Wir werden zunächst einen Netzwerkansatz über *Tailscale* und dann einen Protokollansatz über *Nostr Wallet Connect* mit ihren jeweiligen Vorteilen und Nachteilen betrachten. Der Kurs endet mit einem abschließenden Kapitel, das Ihnen die richtigen Gewohnheiten vermittelt, um Ihre Selbstbehauptung aufrechtzuerhalten, sowohl in operativer als auch in pädagogischer Hinsicht.



Wenn Sie diesen LNP202-Kurs in der richtigen Reihenfolge absolvieren, werden Sie am Ende eine vollständige Konfiguration für Ihren Lightning-Knoten haben, die für den täglichen Gebrauch geeignet ist und die Sie vor allem im Griff haben.




## Verstehen von Blitznodeen


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Bevor Sie Ihren eigenen Knoten in Betrieb nehmen, wird in diesem Kapitel kurz die grundlegende Theorie von Lightning Network erläutert. Es ist in der Tat wichtig, die damit verbundenen Mechanismen zu verstehen, da Sie dadurch in die Lage versetzt werden, Risiken zu erkennen und bewährte Verfahren zu deren Begrenzung anzuwenden. Ich werde hier jedoch nicht ins Detail gehen, da dies nicht das Hauptziel dieses Kurses ist. Wenn Sie tiefer in das Thema einsteigen möchten, empfehle ich Ihnen den Kurs LNP 201 von Fanis Michalakis, der eine Referenz auf diesem Gebiet ist:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Was ist ein Lightning-Knoten?



Gehen wir zurück zu den Grundlagen: Bevor wir definieren, was ein Knoten ist, müssen wir verstehen, was Lightning Network ist. Es ist ein Top-Layer-Protokoll, das auf Bitcoin aufbaut und entwickelt wurde, um Offchain-BTC-Transaktionen zu ermöglichen, die schnell (mit nahezu sofortiger Finalität) und im Allgemeinen kostengünstig sind. "Offchain" bedeutet, dass Transaktionen, die auf Lightning durchgeführt werden, nicht auf der Haupt-Bitcoin-Blockchain erscheinen sollen. Lightning ist auch eine teilweise Antwort auf die zunehmende Nutzung von Bitcoin und auf die Überlastung der Onchain, die Bedenken hinsichtlich der Skalierbarkeit des Systems aufkommen lässt.



Um zu funktionieren, stützt sich Lightning auf die Öffnung von Zahlungskanälen zwischen Teilnehmern, innerhalb derer Transaktionen fast sofort und oft mit minimalen Gebühren durchgeführt werden können, ohne dass sie einzeln auf der Bitcoin-Blockchain registriert werden müssen. Diese Kanäle können für eine sehr lange Zeit offen bleiben und erfordern nur dann Onchain-Transaktionen, wenn sie geöffnet und geschlossen werden.



Ein Lightning-Knoten ist ein Teilnehmer im Lightning-Netzwerk, der Kanäle öffnet und Zahlungen mit anderen Knoten durchführt. Konkret handelt es sich bei einem Lightning-Knoten um ein Stück Software, das auf einem Computer läuft und das Lightning Network-Protokoll implementiert. Beispiele hierfür sind LND, Core Lightning oder Eclair. Die Hauptaufgabe dieser Software besteht darin,:




- eine Verbindung zu einem Bitcoin-Knoten herstellen, um Informationen aus der Hauptblockchain zu erhalten;
- bidirektionale Zahlungskanäle mit anderen Knotenpunkten erstellen und verwalten;
- nachrichten mit dem gesamten Lightning-Netzwerk austauschen.



![Image](assets/fr/001.webp)



### Node vs. Lightning Wallet: ein wichtiger Unterschied



Auf Bitcoin (onchain) bezieht sich "*wallet*" auf die Software, die Ihre privaten Schlüssel verwaltet, Ihr Guthaben aus Ihren UTXO berechnet und Ihre Transaktionen aufbaut. Dieser wallet kann auf Ihrem eigenen Bitcoin-Knoten oder auf dem eines anderen beruhen, aber heute sind die Rolle des Knotens und die des Onchain-wallet klar getrennt.



Bei Lightning ist es schwieriger, diese Art von Vokabular wiederzuverwenden, ohne Verwirrung zu stiften. Der Begriff "*Lightning wallet*" ist ziemlich vage, denn in Wirklichkeit gibt es so etwas wie einen wirklich eigenständigen Lightning wallet nicht, es sei denn, er basiert auf einem Knoten. Daher sind nur zwei Situationen möglich:



- Ein echter Lightning-Knoten (d. h. ohne Verwahrung): Die Software, die Sie verwenden (z. B. eine mobile App wie Phoenix oder eine LND-Instanz auf Umbrel), führt tatsächlich einen Knoten aus, und Sie besitzen tatsächlich die Schlüssel, um Ihre Bitcoins abzurufen. In diesem Fall ist Ihr "*Lightning wallet*" in Wirklichkeit nur eine Benutzeroberfläche auf einem Lightning-Knoten, egal ob eingebettet oder entfernt.



- Sie nutzen einen Verwahrungsdienst: Sie verwenden eine Anwendung, die Ihnen einen Saldo in sats auf Lightning anzeigt, aber im Hintergrund befinden sich die Mittel auf dem Knoten eines Anbieters (z. B. Wallet of Satoshi). Sie haben weder die Schlüssel noch die Kontrolle über die Kanäle. Ihr Guthaben ist lediglich ein Buchungseintrag in der Datenbank des Unternehmens. Es ist vergleichbar mit dem Hinterlegen Ihrer Bitcoins auf einer Börsenplattform, mit allen damit verbundenen Risiken. In diesem Fall ist Ihr "*Lightning wallet*" lediglich ein Zugang zu einem Konto, das von einem Betreiber verwaltet wird, der seinerseits einen echten Lightning-Knoten betreibt.



Bei Lightning gibt es also kein Dazwischen: Entweder Sie haben einen Knoten (selbst einen eingebetteten) und sind somit selbst verantwortlich oder Sie haben keinen, so dass Ihr sats im Besitz eines Unternehmens ist. Aber wie wir in den folgenden Kapiteln sehen werden, sind diese beiden Verwendungszwecke manchmal schwer zu unterscheiden. Phoenix ist beispielsweise eine mobile Anwendung, in die ein echter Lightning-Knoten eingebettet ist, was dem Benutzer jedoch nicht unbedingt bewusst ist, da die gesamte Komplexität seiner Funktionsweise fast vollständig verborgen ist.



### Eine Erinnerung an die Funktionsweise des Lightning Network



In diesem Abschnitt werde ich Ihnen kurz erläutern, wie Lightning funktioniert. Wenn Sie eine ausführlichere Darstellung der theoretischen Konzepte wünschen, sollten Sie sich den Kurs LNP 201 ansehen.



#### Zahlungskanäle: öffnen, aktualisieren und schließen



Das Herzstück des Lightning-Netzwerks basiert auf bidirektionalen Zahlungskanälen. Ein Kanal kann geöffnet (d. h. erstellt), bei Lightning-Transaktionen aktualisiert und schließlich geschlossen werden. Aus der Sicht der Onchain ist ein Kanal nichts anderes als ein 2/2-Multisignatur-Ausgang.



![Image](assets/fr/002.webp)



Aus der Sicht von Lightning handelt es sich um einen Zahlungskanal, bei dem die Liquidität zwischen den beiden Teilnehmern aufgeteilt wird.



![Image](assets/fr/003.webp)





- Eröffnung eines Kanals:**



Zwei Nodes beschließen, einen Channel zu eröffnen. Einer von ihnen überweist Bitcoins in einer Onchain-Transaktion namens *Finanzierungstransaktion*. Diese Transaktion erzeugt eine Ausgabe, die auf einem 2-von-2-Multisignatur-Skript basiert, was bedeutet, dass die Ausgabe dieser Mittel auf Bitcoin die Unterschrift beider Knoten im Kanal erfordert. Vor der Ausgabe dieser Transaktion bittet die Partei, die die Mittel bereitstellt, die andere Partei um die Unterzeichnung einer *Abhebungstransaktion*, die nicht onchain ausgegeben wird, es ihr aber ermöglicht, ihre Mittel im Falle eines Problems zurückzuerhalten.



![Image](assets/fr/004.webp)





- Commitment-Transaktionen:**



Der Zustand des Kanals (d. h. die Verteilung von sats zwischen A und B) wird durch einen *commitment transaction* dargestellt, der beiden Knoten bekannt ist, aber nicht sofort auf der Blockchain übertragen wird. Diese Transaktion beschreibt, wie die Gelder des Kanals auf der Blockchain entsprechend den auf Lightning getätigten Zahlungen umverteilt werden.



Bei jeder Blitzzahlung unterzeichnen die beiden Knoten einen neuen Status, der den vorherigen ersetzt. Der alte Status wird dank eines Widerrufsschlüssel-Mechanismus widerrufen: Wenn einer der Teilnehmer versucht, einen alten Status zu übertragen, kann der andere den vollen Betrag als Strafe zurückfordern.



Der wichtige Gedanke hierbei ist, dass es immer eine signierte Bitcoin-Transaktion gibt, die nicht auf der Kette übertragen wird und die es den Knoten ermöglicht, die sats der anderen entsprechend den auf Lightning Network geleisteten Zahlungen neu zu verteilen.



![Image](assets/fr/005.webp)





- Kanalschließung:**



Ein Kanal kann sauber über eine kooperative Schließung geschlossen werden, wenn sich beide Parteien über den Endzustand des Kanals einig sind, oder einseitig (eine erzwungene Schließung), wenn einer der Teilnehmer nicht mehr kooperiert oder nicht mehr erreichbar ist. In allen Fällen erfolgt die Schließung in Form einer Onchain-Transaktion, bei der der 2/2-Ausgang ausgegeben und die Mittel entsprechend dem letzten gültigen Zustand des Kanals unter den Teilnehmern verteilt werden.



![Image](assets/fr/006.webp)



Lightning funktioniert somit als sekundäre Schicht, die auf Bitcoin verankert ist: Nur bestimmte Ereignisse (das Öffnen und Schließen von Kanälen) erscheinen auf der Hauptblockchain. Zwischenzeitliche Zahlungen bleiben außerhalb der Blockchain.



Bevor wir weitermachen, möchte ich Ihnen zwei wichtige Konzepte für die Verwaltung eines Lightning-Kanals vorstellen:




- Liquidity*: die auf einer Seite des Kanals verfügbare Menge an sats;
- Die *Kapazität*: Sie ist der Gesamtbetrag, der im 2/2-Multisig-Ausgang gesperrt ist, d. h. die Summe der Liquidität auf beiden Seiten des Kanals.



#### Ein Netzwerk von Kanälen und Liquidität



Ein Kanal ist nicht nur für Zahlungen zwischen zwei Knoten gedacht: Er ist Teil eines globalen Netzwerks miteinander verbundener Kanäle. Ihr Knoten kann Zahlungen für andere Nutzer über seine eigenen Kanäle weiterleiten, und Sie können sats an einen Lightning-Knoten senden, mit dem Sie keinen direkten Kanal haben, solange ein gültiger Pfad zwischen Ihren beiden Knoten gefunden werden kann.



Jeder Knoten kennt über das Gossip-Protokoll eine Karte dieses Netzes: welche Kanäle existieren, welche Knoten durch einen bidirektionalen Kanal verbunden sind und welche Kapazitäten veröffentlicht werden. Um eine Zahlung an einen Empfänger ohne direkten Kanal zu senden, berechnet Ihr Knoten eine Route, die aus mehreren Sprüngen besteht: Ihr Knoten → Knoten X → Knoten Y → Empfängernodeen. Bei jedem Schritt durchläuft die Zahlung einen Kanal, der in der Richtung der Zahlung über ausreichende Liquidität verfügen muss.



![Image](assets/fr/007.webp)



Die Liquidität eines Kanals ist daher nicht symmetrisch: eine Seite kann stark belastet sein, während die andere fast leer ist. Die Verwaltung dieser Liquidität, d. h. zu wissen, wo sich die sats befinden und in welche Richtung sie fließen können, ist einer der wichtigsten Aspekte beim Betrieb eines Lightning-Knotens. In den folgenden praktischen Kapiteln werden wir uns damit näher befassen.



#### HTLC: Zahlung transportieren, ohne ausgeraubt zu werden



Damit Zahlungen über Zwischennodeen laufen können, ohne dass Vertrauen erforderlich ist, verwendet Lightning intelligente Verträge namens *HTLC* (*Hashed Time-Locked Contracts*). Vereinfacht ausgedrückt, macht ein HTLC die Überweisung von Geldern von der Offenlegung eines Geheimnisses abhängig und enthält eine Zeitbeschränkung, um den Absender im Falle eines Transaktionsausfalls zu schützen. Jede Zahlung ist daher von der Vorlage eines Vorabbildes abhängig (ein Geheimnis, dessen Hash einem vereinbarten Wert entspricht). Wenn der Endempfänger dieses Vorabbild vorlegt, kann er die Gelder einfordern, was wiederum jedem zwischengeschalteten Knoten ermöglicht, seine eigenen Gelder zurückzuerhalten.



![Image](assets/fr/008.webp)



Ich erspare Ihnen die technischen Details der Funktionsweise des HTLC, da sie für die Zwecke dieses Kurses nicht wesentlich sind. Eine ausführliche Erklärung finden Sie im Theoriekurs LNP 201. Denken Sie einfach daran, dass HTLC einen atomaren Austausch ermöglichen: Entweder wird der Transfer abgeschlossen und niemand wird bei der Weiterleitung geschädigt, oder er scheitert und jeder Teilnehmer erhält sein ursprüngliches Geld zurück. Dazwischen gibt es kein Dazwischen.



### Die wichtigsten Lightning-Knoten-Implementierungen



Wie bei Bitcoin gibt es auch für das Lightning-Protokoll mehrere Implementierungen. Eine Reihe unabhängiger Teams entwickeln ihre eigenen Versionen, die alle interoperabel sind, da sie sich an dieselben Spezifikationen (die BOLTs) halten. Hier sind die wichtigsten Implementierungen, die heute verwendet werden.



#### LND (*Lightning Network Daemon*)



LND ist eine vollständige Implementierung des Lightning-Protokolls, geschrieben in Go und entwickelt von Lightning Labs.



![Image](assets/fr/009.webp)



#### Kernblitz (*CLN*)



Core Lightning (früher *C-Lightning*) ist die von Blockstream entwickelte Implementierung. Sie ist in C geschrieben, mit einigen Komponenten in Rust.



![Image](assets/fr/010.webp)



#### Eclair



Eclair ist eine in Scala geschriebene Implementierung, die von dem französischen Unternehmen ACINQ entwickelt wurde. ACINQ betreibt mit Eclair einen der wichtigsten Routing-Knoten im Lightning-Netz und nutzt diese Implementierung als Softwarebasis für eigene Produkte wie die Anwendung Phoenix.



![Image](assets/fr/011.webp)



#### LDK (*Lightning Development Kit*)



LDK (*Lightning Development Kit*) ist ein Rust Entwicklungskit, das von Spiral (Block, ex-Square) gepflegt wird. Es ist kein gebrauchsfertiger daemon wie LND oder CLN, sondern eine Bibliothek für Entwickler, die Lightning direkt in ihre Anwendungen integrieren möchten.



![Image](assets/fr/012.webp)



In diesem LNP202-Kurs werden wir uns hauptsächlich auf LND konzentrieren: die Implementierung, die am häufigsten in schlüsselfertigen Lösungen für Privatkunden verwendet wird, wie Umbrel.



So viel zu dieser kurzen Erinnerung an die Funktionsweise von Lightning. Noch einmal: Wenn es Konzepte gibt, die Sie nicht verstehen, oder wenn Sie etwas tiefer einsteigen möchten, bevor Sie sie in die Praxis umsetzen, ist der Kurs von Fanis Michalakis die unverzichtbare Referenz zu diesem Thema:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Warum einen eigenen Lightning-Knoten betreiben?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Die Antwort auf diese Frage ist recht einfach, da sie rhetorisch ist: Ohne einen eigenen Knotenpunkt nutzt man Lightning nicht mehr wirklich, sondern nur noch die Illusion von Lightning über die Infrastruktur eines Unternehmens.



Die Verwendung eines Lightning-Custodial-wallet bedeutet, dass die Bitcoins technisch gesehen dem Unternehmen gehören, das den Knoten betreibt. Sie sind nicht im Besitz der privaten Schlüssel und haben keine Kontrolle über die Kanäle. Ihr wallet-Guthaben ist nur eine Zeile in der Datenbank eines Dienstanbieters. Diese Situation ist für Anfänger sicherlich sehr bequem, und die Benutzererfahrung ist oft fließend, aber die grundlegende Frage ist: Was ist der Vorteil der Verwendung von Bitcoin und Lightning, wenn man am Ende genau die Aspekte aufgibt, die sie von traditionellen Währungen und Banken unterscheiden?



Die beiden wichtigsten Wertversprechen von Bitcoin sind monetäre Souveränität (keine Abhängigkeit von einer zentralen Behörde für die Ausgabe und Verwahrung) und Zensurresistenz (keine Möglichkeit für Dritte, Zahlungen zu verhindern oder zu filtern). Ein Verwahrungssystem auf Lightning steht diesen beiden Zielen entgegen: Sie können die interne Geldmenge der Plattform nicht überprüfen, und ein Betreiber, der alle Gelder und alle Kanäle hält, kann Ihre Zahlungen per Definition zensieren, verzögern, priorisieren oder blockieren. Unter diesen Bedingungen können wir uns berechtigterweise fragen, **welchen Sinn die Verwendung von Bitcoin über Lightning hat, wenn sie die gleichen Muster von Vertrauen und Abhängigkeit reproduziert wie bei traditionellen staatlichen Währungssystemen**.



> Erforderlich ist ein elektronisches Zahlungssystem, das auf kryptografischen Beweisen statt auf Vertrauen beruht und es zwei beliebigen Parteien ermöglicht, direkt miteinander zu handeln, ohne dass eine vertrauenswürdige dritte Partei erforderlich ist.
*Satoshi Nakamoto, Bitcoin Weißbuch


Abgesehen von der Philosophie sind die konkreten Nachteile für Sie wie folgt. Erstens haben Sie keine Möglichkeit zu überprüfen, ob das Unternehmen tatsächlich die Bitcoins besitzt, die den angezeigten Guthaben entsprechen. Es kann mit Bruchteilen von Reserven arbeiten, gehackt werden, in Konkurs gehen oder einfach verschwinden. In diesem Fall sind Sie nur ein weiterer Gläubiger ohne echte Garantie, dass Sie Ihr Geld zurückbekommen.



Zweitens ist das Unternehmen regulatorischen Risiken ausgesetzt: einstweilige Verfügungen, Einfrieren von Geldern, Aufforderungen zur Sperrung von Nutzern oder Transaktionen, verstärkte Überwachung oder sogar ein völliges Verbot von Aktivitäten in bestimmten Ländern. Jede Einschränkung, die auf dem Dienstleister lastet, wirkt sich mechanisch auf Sie aus.



Was die Vertraulichkeit betrifft, ist die Situation nicht besser. Ein Verwahrer sieht alle Ihre Bewegungen: Beträge, Häufigkeit, Empfänger, Guthaben, Ausgabegewohnheiten. In Kombination mit den von der Anwendung bereitgestellten Informationen und möglicherweise der zugrundeliegenden Kettenanalyse auf Bitcoin können diese Informationen ein sehr genaues Profil Ihrer finanziellen Aktivitäten ergeben. Auch dies ist weit entfernt von dem Ziel von Bitcoin, die finanzielle Überwachung zu reduzieren.



Die gute Nachricht ist, dass der Betrieb eines eigenen Lightning-Knotens heute nicht mehr nur technischen Experten vorbehalten ist, wie es vielleicht in den späten 2010er Jahren der Fall war. Für Privatanwender gibt es relativ einfache Lösungen, die wir im nächsten Kapitel ausführlich erläutern.




## Die Wahl der richtigen Lösung für die jeweilige Aufgabe


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



Heutzutage ist es möglich, eine Benutzererfahrung zu haben, die der eines wallet mit Blitzgewahrsam sehr nahe kommt, während man in Selbstgewahrsam bleibt. Dieses Kapitel soll Ihnen helfen, den für Ihr Profil am besten geeigneten Weg zu wählen.



### Option 1: Lightning nicht direkt verwenden



Die erste Lösung besteht einfach darin, Lightning nicht nativ zu nutzen, sondern einen Bitcoin oder Liquid wallet zu verwenden, der Atomic Swaps einbindet. Beispielsweise nutzen Aqua- oder Bull Bitcoin Wallet-Anwendungen diese Methode, indem sie es Ihnen ermöglichen, Lightning-Rechnungen zu bezahlen, ohne selbst einen Lightning-Knoten zu betreiben, und dabei in Eigenverantwortung zu bleiben.



Das Prinzip ist einfach: Ihre Gelder verbleiben im Bitcoin, entweder im on-chain oder im Liquid, und Sie greifen über einen wallet darauf zu, wo Sie die Schlüssel auf herkömmliche Weise aufbewahren. Wenn Sie eine Lightning-Rechnung scannen, leitet Ihr wallet eine Transaktion (on-chain oder Liquid) an einen atomaren Tauschdienst ein. Dieser Dienst wickelt dann die Lightning-Zahlung über seinen eigenen Knoten ab, wobei er die Bitcoins verwendet, die Sie on-chain oder über Liquid bereitgestellt haben. Dadurch müssen Sie selbst keine Lightning-Kanäle verwalten und können dennoch Lightning-Rechnungen nahtlos begleichen.



![Image](assets/fr/013.webp)



Der große Vorteil dieses Ansatzes im Vergleich zu einem konventionellen Lightning-verwahrten wallet besteht darin, dass Sie jederzeit zu 100 % im Besitz Ihrer Gelder bleiben. Die Bitcoins befinden sich in Ihrer Onchain oder Liquid wallet, mit Ihrer eigenen mnemonischen Phrase. Selbst während des Swaps bleiben Sie im Besitz Ihrer Gelder, denn der Swap ist atomar. Er beruht auf einem kryptografischen Mechanismus, der sicherstellt, dass es nur zwei mögliche Ergebnisse gibt: Entweder der Swap gelingt vollständig, oder er scheitert und der Dienst kann sich Ihre Gelder nicht aneignen.



Die meisten Portfolios, die diese Art von Funktionalität anbieten, stützen sich auf [Boltz](https://boltz.exchange/) für den technischen Teil des Swaps.



Diese Lösung bietet auch interessante Vorteile in Bezug auf die Vertraulichkeit, insbesondere in Verbindung mit dem Liquid. Für einen Anfänger ist es auch sehr einfach einzurichten und zu speichern: eine klassische mnemonische Phrase, keine Kanäle, keine Liquidität zum Ausgleichen...



Andererseits hat dieser Ansatz auch seine Grenzen. Erstens ist sie nicht unanfechtbar: Sie sind von der Verfügbarkeit und dem guten Willen des Swap-Dienstes abhängig. Wenn dieser Ihr Konto nicht mehr bearbeiten will oder seinen Betrieb einstellt, können Sie keine Blitzrechnungen mehr über ihn bezahlen. Hinzu kommen die nicht unerheblichen Gebühren: Sie zahlen sowohl die Onchain- oder Liquid-Transaktionsgebühren als auch die Swap-Service-Provision. Wenn die Onchain-Gebühren stark ansteigen, kann es sehr teuer werden, Lightning zu nutzen.



Für den gelegentlichen Gebrauch ist es also noch akzeptabel, aber für einen sehr aktiven Lightning-Nutzer ist es besser, die Dinge mit einem echten Lightning-Knoten zu erledigen.



### Option 2: Eingebaute Lightning-Knoten



Die zweite Kategorie von Lösungen basiert auf Lightning-Knoten, die direkt in eine mobile Anwendung eingebettet sind. Phoenix Wallet war der Vorreiter dieses Modells und gilt nach wie vor als Maßstab. Heute bieten andere Projekte vergleichbare Ansätze, wie Zeus (im eingebetteten Modus) oder BitKit.



Die Idee ist einfach: Die Anwendung führt tatsächlich einen Lightning-Knoten aus, aber alle komplexen Vorgänge werden automatisch im Hintergrund abgewickelt. Sie haben eine "*Lightning wallet*"-Schnittstelle mit einer mnemonischen Phrase für die Sicherung, Sie sehen einen Saldo und bezahlen Rechnungen, aber Sie verwalten keine Kanäle, Liquidität oder die meisten Parameter.



![Image](assets/fr/014.webp)



Diese Lösungen sind immer selbstverwahrend. Die Schlüssel, die die Mittel kontrollieren, sind generated und auf Ihrem Telefon gespeichert, und die Sicherung erfolgt über einen seed oder einen gleichwertigen Mechanismus. Sie haben nicht einfach nur ein Konto bei einem Dienstanbieter, sondern Sie besitzen Bitcoins, die in Kanälen gesperrt sind, die Ihnen gehören und nicht gestohlen werden können.



Die Vorteile der LN-On-Board-Knoten sind zahlreich:




- extrem einfach zu installieren und zu verwenden;
- benutzererfahrung, die der eines verwahrten Lightning wallet nahe kommt, aber mit Selbstverwahrung;
- keine manuelle Verwaltung von Kanälen oder Liquidität;
- relativ einfache Sicherung.



Aber diese eingebetteten wallet haben auch erhebliche Einschränkungen. Erstens hat der Betreiber des Dienstes (z. B. ACINQ im Fall von Phoenix) einen ziemlich detaillierten Einblick in die Datenströme, die Ihren Knoten durchlaufen: Mengen, Häufigkeit, Empfänger, auch wenn sich dies sicherlich verbessern wird, insbesondere mit der schrittweisen Einführung von *Trampolin-Knoten*. Zweitens sind Sie in hohem Maße von diesem Betreiber als Ihrem wichtigsten Lightning-Peer abhängig. Wenn der ACINQ-Knoten nicht mehr verfügbar ist (im Fall von Phoenix), wenn das Unternehmen unter regulatorischen Druck gerät oder sein Geschäftsmodell ändert, kann Ihr Nutzererlebnis stark beeinträchtigt oder sogar gefährdet werden.



Schließlich hat diese Einfachheit ihren Preis. Eingebettete LN-Knotendienste erheben in der Regel spezifische Gebühren für Einzahlungen, Abhebungen oder bestimmte Kanalverwaltungsvorgänge. Meiner Meinung nach ist dieses Modell im Hinblick auf den angebotenen Dienst sinnvoll, aber bei intensiver Nutzung kann es sehr viel teurer sein als ein gut verwalteter herkömmlicher Lightning-Knoten.



### Option 3: der klassische Lightning-Knoten



Die dritte Lösung, auf die wir in diesem LNP202-Kurs näher eingehen werden, ist der Betrieb eines herkömmlichen Lightning-Knotens auf einem dedizierten Server oder Gerät.



Mit "klassisch" meine ich, dass Sie selbst eine Lightning-Implementierung (z. B. LND) auf Ihrem eigenen Bitcoin-Knoten installieren und konfigurieren. Sie wählen Ihre Peers aus, öffnen Ihre Kanäle, verwalten Ihre ein- und ausgehende Liquidität und legen Ihre Routing-Gebührenrichtlinien fest.



In Bezug auf die Souveränität ist das die beste Lösung. Sie sind nicht mehr von einem bestimmten Unternehmen für Ihre Kanäle oder Zahlungen abhängig: Wenn ein Peer Sie zensiert oder einen Kanal schließt, können Sie einen anderen mit einem anderen Knotenpunkt öffnen. Wenn ein Dienst verschwindet, bleiben Ihre sats in den Kanälen, die Sie kontrollieren, und Sie können sie onchain zurückführen. Sie können auch Ihre langfristigen Kosten optimieren: Sobald Ihre Kanäle richtig dimensioniert und verwaltet sind, können die Gesamtkosten für Zahlungen sehr niedrig werden.



Was die Vertraulichkeit betrifft, so unterliegen Sie natürlich den Beschränkungen des Lightning-Modells, aber Sie geben nicht Ihr gesamtes Geschäft an einen einzigen Betreiber ab.



Im Gegensatz dazu ist die Einrichtung eines klassischen Lightning-Knotens deutlich komplexer: Sie müssen ihn installieren, konfigurieren, warten, Updates überwachen, die Logik von Kanälen und Gebührenrichtlinien verstehen, Kanäle und Cashflow verwalten und so weiter. Eine Fehlkonfiguration, ein schlampiges Backup oder eine nachlässige Verwaltung können leichter zum Verlust von sats führen. Der Knoten muss außerdem kontinuierlich laufen.



Genau diesen Weg schlage ich Ihnen in diesem Kurs vor und begleite Sie bei jedem Schritt, um Risiken zu begrenzen und Ihr Vorgehen zu strukturieren.



### Welche Lösung für welches Benutzerprofil?



Um die richtige Lösung für Ihr Lightning-Benutzerprofil auszuwählen, müssen Sie zwei Faktoren berücksichtigen: die Häufigkeit der Nutzung von Lightning und Ihre Bereitschaft zur technischen Verwaltung.



Wenn Sie nur gelegentlich Lightning-Zahlungen tätigen, aber dennoch von Zeit zu Zeit LN-Rechnungen von Ihrem Telefon aus begleichen möchten, ohne die Selbstverwahrung aufzugeben, ist ein Bitcoin oder Liquid wallet mit Swap-Funktion wahrscheinlich die beste Option. Sie behalten das Eigentum an Ihren Geldern, verwalten keine Knotenpunkte und nehmen im Gegenzug für die Einfachheit etwas höhere Gebühren in Kauf.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Wenn Sie Lightning ziemlich regelmäßig nutzen und die Vorteile eines echten Knotens nutzen möchten, aber keine Zeit für die Verwaltung von Kanälen, Gebühren oder Infrastruktur aufwenden wollen, ist ein mobiler eingebetteter Lightning-Knoten eine gute Lösung. Sie behalten die Kontrolle über Ihre Gelder, die UX bleibt sehr zugänglich und die ganze Komplexität wird ausgeblendet, allerdings zum Preis einer deutlichen Abhängigkeit von einem Betreiber.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Wenn Sie ein mittlerer oder fortgeschrittener Nutzer sind, der bereit ist, Zeit in das Verständnis und die Verwaltung seiner Infrastruktur zu investieren, und die maximale Kontrolle über seine Kanäle, Liquidität und Kosten haben möchte, ist ein klassischer serverbasierter Lightning-Knoten der richtige Weg. Es ist die anspruchsvollste Lösung, aber auch diejenige, die am besten mit der Idee der Souveränität von Bitcoin übereinstimmt.




# Erstellen Ihres ersten Lightning-Knotens


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## Installation von LND mit Umbrel


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Nachdem wir nun die Grundlagen von Lightning und die verfügbaren Lösungen besprochen haben, ist es an der Zeit, zur Sache zu kommen. Zur Teilnahme an diesem Kurs benötigen Sie einen Bitcoin-Knoten, der mit Umbrel synchronisiert ist. Dieser Schulungskurs LNP202 ist eine Fortsetzung von BTC 202; wenn Sie noch keinen Bitcoin-Knoten haben, sollten Sie diesen anderen Schulungskurs besuchen, bevor Sie hierher zurückkehren, sobald Ihr Knoten synchronisiert wurde. Ich empfehle Ihnen dringend, ihn zu konsultieren, da ich nicht im Detail auf seine Funktionsweise, Konfiguration und Sicherheitsmaßnahmen eingehen werde.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

In diesem ersten Kapitel sehen wir uns an, wie Sie LND auf Ihrem Umbrel installieren. Die Funktionsweise des Umbrel macht diesen Schritt sehr einfach, da Sie nur eine Anwendung installieren müssen.



Öffnen Sie auf der Startseite den "App Store" am unteren Rand der Benutzeroberfläche.



![Image](assets/fr/015.webp)



Geben Sie in der Suchleiste "Lightning Node" ein und klicken Sie dann auf die Anwendung.



![Image](assets/fr/016.webp)



Klicken Sie dann auf die Schaltfläche `Installieren`, um die Installation zu starten.



![Image](assets/fr/017.webp)



Klicken Sie auf der Startseite auf die Anwendung, um sie zu öffnen, und wählen Sie dann "Einen neuen Knoten einrichten".



![Image](assets/fr/018.webp)



Sie erhalten eine Eselsbrücke mit 24 Wörtern. Bewahren Sie sie an einem sicheren Ort auf. Im nächsten Kapitel werden wir uns genauer ansehen, wie Sie den Zugang zu Ihrem Lightning-Knoten wiederherstellen können (dies ist ein viel komplexerer Prozess als bei einem einfachen Bitcoin wallet), aber denken Sie daran, dass diese Phrase eine entscheidende Rolle spielt und mit äußerster Sorgfalt aufbewahrt werden muss.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Speichern Sie diese Phrase auf dieselbe Weise wie eine herkömmliche mnemotechnische Phrase: auf einem physischen Medium (Papier oder Metall), das an einem sicheren Ort aufbewahrt wird, und klicken Sie dann auf die Schaltfläche "NEXT".



![Image](assets/fr/019.webp)



Geben Sie dann die Wörter Ihres Satzes ein, um zu überprüfen, ob Sie sie richtig aufgeschrieben haben.



![Image](assets/fr/020.webp)



Eine Warnmeldung erinnert Sie daran, dass es sich bei der Anwendung um eine Betaversion handelt und dass Lightning Network eine experimentelle Technologie bleibt. Es versteht sich von selbst, dass Sie niemals Beträge auf Ihren Lightning-Knoten übertragen sollten, die Sie nicht zu verlieren bereit sind.



Sie gelangen dann zur Hauptschnittstelle Ihres Lightning-Knotens. Auf der linken Seite finden Sie Ihren Bitcoin onchain wallet, der auf Ihrem Knoten gehostet wird. Dies ist der generated aus der 24-Wort-Phrase, die Sie gerade gespeichert haben.



In der Mitte finden Sie Ihren Lightning wallet. Es repräsentiert Ihr ausgehendes Bargeld, d. h. die Bitcoins, die Sie in Ihren Lightning-Kanälen besitzen.



Auf der rechten Seite sehen Sie einige wichtige Informationen über Ihren Knoten:




- Die Anzahl der Verbindungen und offenen Kanäle;
- Ihr gesamter ausgehender Cashflow, d. h. das, was Sie theoretisch für Lightning ausgeben können;
- Ihre gesamte eingehende Liquidität, d. h. das, was Sie theoretisch über Lightning erhalten können.



![Image](assets/fr/021.webp)



Beginnen wir mit der Anpassung unseres Knotens. Klicken Sie auf die drei kleinen Punkte oben rechts in der Benutzeroberfläche und dann auf "Erweiterte Einstellungen". Im Untermenü "Personalisierung" können Sie einen öffentlichen Namen für Ihren Knoten festlegen (vermeiden Sie es, Ihren echten Namen zu verwenden) und seine Farbe wählen.



![Image](assets/fr/046.webp)



Klicken Sie dann auf die grüne Schaltfläche "SPEICHERN UND NEU STARTEN", um Ihren Knoten neu zu starten und die Änderungen zu übernehmen.



Ihr Lightning-Knoten ist nun bereit, seine ersten Kanäle für Zahlungen zu öffnen. Aber zuerst wollen wir einen Blick darauf werfen, wie Sie Ihren sats schützen können!



## Speichern des Lightning-Knotens


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Bevor Sie Ihren ersten sats an Ihren Knoten senden, ist es wichtig zu verstehen, wie das Backup funktioniert und welche Risiken damit verbunden sind. Im Gegensatz zu einem einfachen Bitcoin-Onchain-Portfolio ist die Sicherung eines Lightning-Knotens ziemlich komplex: Die falsche Strategie kann zum dauerhaften Verlust Ihrer Gelder führen. In diesem Kapitel werden wir uns ansehen, was wirklich gesichert werden muss und wie Umbrel diesen Prozess mit LND handhabt.



In diesem Kurs werden wir die Implementierung LND (*Lightning Network Daemon*) verwenden. Obwohl die Prinzipien bei den anderen Implementierungen ähnlich sind, sind die Wiederherstellungsdateien und -verfahren, über die ich sprechen werde, spezifisch für LND.



### Was sollte ich auf einem Lightning-Knoten speichern?



Bei einem Blitznodeen reicht es nicht aus, den seed zu retten und zu hoffen, dass sich alles wieder normalisiert. Mehrere Elemente spielen unterschiedliche Rollen, daher ist es wichtig, zwischen ihnen zu unterscheiden.



#### Der seed (*hüstel*)



Wenn Sie den LND initialisieren, erhalten Sie einen seed mit 24 Wörtern. Dies ist ein LND-spezifisches Format namens "*aezeed*". Es handelt sich nicht um ein klassisches seed BIP39, obwohl es einem solchen sehr ähnlich sieht. Aus diesem seed leitet LND die privaten Schlüssel Ihrer Onchain-wallet ab, die mit dem Lightning-Knoten verbunden sind, d. h. die Adressen, an die Sie Bitcoins empfangen oder an die Sie Bitcoins nach Kanalschließungen zurückgeben können.



![Image](assets/fr/019.webp)



Dieser seed kann daher verwendet werden, um den mit Ihrem Knoten verbundenen Onchain-wallet wiederherzustellen und um Gelder abzurufen, die bereits onchain zurückgeführt wurden (z. B. nach einer Kanalschließung). Andererseits reicht der seed allein nicht aus, um Ihre noch offenen Lightning-Kanäle wiederherzustellen, da er nicht die erforderlichen Informationen über den Status Ihrer Kanäle enthält.



#### Die Kanaldatenbank (`channel.db`)



LND speichert den detaillierten Status Ihrer Kanäle in einer Datenbank namens "channel.db". Diese Datenbank enthält:




- die Liste Ihrer offenen Kanäle;
- ihre Gleichaltrigen und deren Kennungen;
- die letzten commitment transaction für jeden Kanal (die aufeinanderfolgenden Zustände, die festlegen, wem was in dem Kanal gehört, und die es ermöglichen, Onchain-Gelder im Falle eines Problems wiederherzustellen);
- die Informationen, die benötigt werden, um einen Peer zu bestrafen, der versucht, eine alte Meldung zu senden.



Das Problem mit dieser Datenbank ist, dass sie sich ständig ändert: Jede Zahlung, jedes Routing, jedes Öffnen oder Schließen eines Kanals verändert ihren Inhalt. Aus diesem Grund ist ein herkömmliches Backup (z.B. eine regelmäßige Kopie Ihrer `channel.db`) gefährlich. Wenn Sie eine zu alte Version der `channel.db` wiederherstellen und den Knoten mit diesem veralteten Zustand wieder aufbauen, könnten Ihre Peers der Meinung sein, dass Sie einen alten Kanalzustand senden. In diesem Fall sieht das Protokoll eine Strafe vor: Ihr Peer kann den gesamten Betrag des Kanals zurückfordern, als ob Sie versucht hätten zu betrügen.



In der Praxis ist `channel.db` also kein Sicherungsmedium im eigentlichen Sinne. Sie ist der lebende Zustand Ihres Knotens. Die einzige Situation, in der es sinnvoll ist, sie zur Wiederherstellung Ihres Knotens zu verwenden, ist, wenn Sie diese Datenbank direkt von einem Rechner wiederherstellen, der gerade ausgefallen ist (z. B. von einer noch lesbaren Festplatte). In diesem Fall stellen Sie den letzten Stand wieder her und können LND auf einem anderen Rechner auf der Grundlage dieser Datenbank neu starten, in der Gewissheit, dass dieser Stand so aktuell wie möglich ist, da der alte Rechner nicht mehr läuft. Eine weitere Situation, in der diese Methode als relevante Sicherung dienen kann, ist eine Konfiguration mit zwei Festplatten und einer dynamischen, permanenten Kopie von einer auf die andere. Diese Art der Einrichtung ist jedoch komplexer zu implementieren.



Regelmäßige Kopien von `channel.db` zu machen und sie als Sicherungskopien zu speichern, um sie später wiederherzustellen, ist jedoch eine sehr schlechte Idee: An dem Tag, an dem Sie sie benutzen, laufen Sie Gefahr, sich selbst zu bestrafen und alle Ihre sats zu verlieren.



#### Statische Kanalsicherung (SCB)



Um eine Notfallwiederherstellung zu ermöglichen, hat LND den Mechanismus *Static Channel Backup* (SCB) eingeführt. Dabei handelt es sich um eine spezielle Datei, die oft `channel.backup` genannt wird und statische Informationen über Ihre Kanäle enthält: wer Ihre Peers sind, wie man sie kontaktiert und was Ihre Kanäle sind.



Diese Datei enthält keinen detaillierten Kanalstatus oder Aktualisierungsverlauf. Sie ermöglicht es Ihnen nicht, Kanäle in genau dem Zustand wieder zu öffnen, in dem sie sich befunden haben, und auch nicht, diesen Lightning-Knoten weiter zu betreiben. Vielmehr dient sie als Ankerpunkt, um Ihre Peers zu bitten, Ihnen dabei zu helfen, alle Ihre Kanäle sauber zu schließen und so Ihren sats onchain zu erhalten, auf Schlüsseln, die Sie dank des seed abrufen können. Im Gegensatz zur Datei `channel.db`, die bei jeder Zahlung oder Weiterleitung geändert wird, wird die SCB-Datei nur aktualisiert, wenn ein Kanal geöffnet oder geschlossen wird.



Bei der Wiederherstellung über SCB ist der Prozess wie folgt:




- Sie stellen Ihr seed wieder her (*gezehrt*), wodurch Ihr mit dem Blitznodeen verbundenes Onchain-wallet wiederhergestellt wird;
- Sie übermitteln LND Ihre letzte SCB;
- LND verwendet den SCB, um die Liste Ihrer Peers und der Kanäle, die Sie mit ihnen haben, zu finden;
- Es kontaktiert jeden Peer, teilt ihm mit, dass Sie einen Datenverlust erlitten haben, und bittet ihn, Ihren Kanal mit ihm zu schließen, damit Sie Ihren Onchain-Anteil wiederherstellen können.



Die Idee ist, dass Ihre Peers, wenn sie bemerken, dass Sie einen Datenverlust melden, ihr letztes commitment transaction senden und den Force Channel schließen. Sobald diese Transaktionen bestätigt wurden, erscheinen Ihre Gelder wieder in Ihrem Onchain-Portfolio (verbunden mit dem seed).



Dieser Wiederherstellungsmechanismus ist jedoch nicht perfekt. Erstens wird Ihr Lightning-Knoten nicht wirklich wiederhergestellt, da alle Kanäle geschlossen werden. Sie müssen dann einen neuen Lightning-Knoten von Grund auf neu erstellen. Zweitens garantiert es keine 100-prozentige Wiederherstellung, obwohl es die Chancen auf eine Wiederherstellung Ihrer Onchain-Guthaben im Falle eines Problems erheblich erhöht. Dieses Wiederherstellungsprotokoll hängt nämlich von der Kooperation und der Verfügbarkeit Ihrer Peers ab: Wenn einer von ihnen offline ist, seine eigenen Daten verloren hat oder sich weigert, zu kooperieren, können Ihre Gelder blockiert bleiben oder sogar dauerhaft verloren gehen. Deshalb ist es wichtig, dass Sie auf Ihrem Lightning-Knoten keine Kanäle mit unerreichbaren Peers über längere Zeiträume offen halten. Wenn Sie zu diesem Zeitpunkt einen Datenverlust erleiden und der Peer unerreichbar bleibt, ist eine Wiederherstellung über SCB unmöglich, und Ihre Gelder bleiben verloren, bis der Peer wieder online ist (vielleicht für immer).



Zusammenfassend lässt sich sagen, dass eine gute Lightning-Backup-Strategie auf LND auf drei Säulen ruht:




- Ihr seed (*geezeed*), für die Onchain-Schicht;
- Zuverlässige automatische SCB-Sicherung;
- Gutes Kanalmanagement durch die Auswahl zuverlässiger Peers und die präventive Schließung derjenigen, die oft nicht erreichbar sind.



### Wie verwaltet Umbrel die Sicherung Ihres LND-Knotens?



Umbrel bietet einen vereinfachten Sicherungsmechanismus für den LND-Knoten, der genau auf der SCB basiert. Die Idee ist, Ihnen die Mühe zu ersparen, diese Datei selbst zu manipulieren, eine Sicherungskopie davon zu erstellen und den Prozess so weit wie möglich zu automatisieren.



Wenn Sie Ihren Knoten auf Umbrel erstellen, erhalten Sie einen seed, der eine doppelte Rolle spielt:




- wird Ihr Bitcoin in der Kette wallet abgeleitet, die mit Ihrem Lightning-Knoten verbunden ist;
- er wird verwendet, um eine Backup-Kennung und einen Verschlüsselungsschlüssel abzuleiten, die für Remote-SCB-Backups verwendet werden.



Dank dieses Mechanismus erstellt Umbrel automatisch eine verschlüsselte Sicherungskopie Ihrer SCB und speichert sie über Tor auf seinen Servern. Die SCB wird dank eines von Ihrem seed abgeleiteten Schlüssels verschlüsselt gespeichert. Im Falle eines Datenverlustes musst du also nur einen Bitcoin und einen Lightning-Knoten auf dem Umbrel auf demselben oder einem anderen Rechner neu erstellen und dann deinen seed eingeben. Sie können dann den neuesten SCB-Status von den Umbrel-Servern abrufen, ihn entschlüsseln und den Prozess der Wiederherstellung Ihrer Gelder beginnen.



Diese Sicherungen werden von Ihrem Knotenpunkt lokal verschlüsselt, bevor sie gesendet werden, wodurch die Vertraulichkeit Ihrer Daten gewährleistet wird: Umbrel kann den Inhalt der SCB nicht lesen. Die Übertragung erfolgt über Tor, wodurch verhindert wird, dass Ihre IP-Adresse aufgedeckt wird. Darüber hinaus fügt Ihr Umbrel dem Datenverkehr Rauschen hinzu (zufällige Auffüllungen und falsche Backups, die in unregelmäßigen Abständen gesendet werden), um zu verhindern, dass der Server genau feststellen kann, wann Sie einen Kanal öffnen oder schließen.



Der Hauptvorteil dieser Methode ist, dass sie die Sicherung Ihres Lightning-Knotens erheblich vereinfacht: Sie müssen Ihren seed nur einmal während der Knoteninitialisierung sichern. Dies birgt zwar ein gewisses Risiko, da es sich nur um eine Sicherung der SCB handelt, aber für angemessene Beträge ist es ein akzeptabler Kompromiss.



### Bewährte Praktiken zur Begrenzung des Verlustrisikos



Selbst bei der Sicherung von Umbrel kann das Risiko eines Verlusts von sats durch einige einfache, bewährte Verfahren erheblich verringert werden:





- Überwachen Sie die Verfügbarkeit Ihrer Kollegen:



Wenn ein wichtiger Kanal häufig mit einem unerreichbaren oder instabilen Peer verbunden ist, ist es sicherer, ihn sauber zu schließen, solange Ihr Knoten noch funktioniert. Eine präventive kooperative oder erzwungene Schließung beseitigt eine potenzielle Problemquelle im Falle einer SCB-Wiederherstellung.





- Vermeiden Sie es, zu viel Liquidität auf unbekannte Gleichaltrige zu konzentrieren:



Je größer der Kanal ist, den ein Peer mit Ihnen hat, desto wichtiger ist es, dass er zuverlässig ist. Wählen Sie seriöse, gut vernetzte und aktive Knoten, damit eine künftige Wiederherstellung über SCB reibungslos ablaufen kann.





- Ergänzen Sie Umbrel durch lokale Backups:



Zusätzlich zur automatischen Sicherung des Umbrel können Sie auch eine verschlüsselte Kopie Ihrer SCB-Datei (`channel.backup`) auf einem externen Medium aufbewahren und diese regelmäßig aktualisieren. Idealerweise sollten Sie sie jedes Mal erneuern, wenn Sie einen Kanal öffnen oder schließen. Auf diese Weise haben Sie eine Backup-Lösung für den Fall, dass der automatische Backup-Dienst des Umbrel aus irgendeinem Grund nicht mehr verfügbar ist.





- Der richtige Umgang mit Ihrem seed



Ihr seed Umbrel stellt nicht nur Ihren Onchain-wallet wieder her, sondern leitet auch den Verschlüsselungsschlüssel für Backups ab. Ein Angreifer, der Zugriff darauf hat, könnte daher eine Wiederherstellung starten und Ihr Geld auf seinen eigenen wallet übertragen, ohne überhaupt physischen Zugang zu Ihrem Knoten zu haben.



Wenn Sie also Ihren Knoten wiederherstellen müssen, aber nicht mehr über Ihr seed verfügen, können Sie nichts mehr wiederherstellen: Ihr gesamtes sats ist verloren. Es ist daher sehr wichtig, dass Sie Ihr seed mit äußerster Sorgfalt und nur auf physischen Medien (Papier oder Metall) speichern und an einem sicheren Ort aufbewahren. Weitere Informationen zur Verwaltung eines seed finden Sie in dieser Anleitung:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Wie speichere ich meinen Lightning-Knoten auf Umbrel?



Nachdem Sie nun verstanden haben, wie die Theorie funktioniert, lassen Sie uns zur Sache kommen. Klicken Sie in Ihrer Lightning Node-Anwendung (die eigentlich LND heißt) auf die drei kleinen Punkte in der oberen rechten Ecke.



![Image](assets/fr/022.webp)



Für die Sicherung sind hier drei Elemente von Interesse:




- Vergewissern Sie sich, dass die Option `Automatische Backups` aktiviert ist. Dadurch wird Ihre verschlüsselte SCB automatisch an die Server von Umbrel gesendet.
- Sie können dann wählen, ob Sie über Tor oder Clearnet senden wollen, indem Sie die Option `Backup over Tor` wählen. Wie in den vorangegangenen Abschnitten erläutert, empfehle ich Ihnen dringend, Tor zu verwenden, um Ihre Vertraulichkeit zu wahren.
- Schließlich gibt es eine Schaltfläche "Kanal-Backup-Datei herunterladen", mit der Sie eine "Kanal-Backup-Datei", d. h. einen verschlüsselten Schnappschuss Ihrer SCB, auf Ihren Computer herunterladen können. So können Sie von Zeit zu Zeit zusätzlich zu den automatisch an die Umbrel-Server gesendeten Sicherungen weitere lokale Sicherungen erstellen.



Jetzt wissen Sie, wie Sie das sats Ihres Lightning-Knotens vor Datenverlust schützen können. Im nächsten Kapitel werden wir uns ansehen, wie Sie Ihren Knoten vor Betrugsversuchen schützen können.




## Watchtower: Rolle und Aufbau


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



In Lightning basiert jeder Kanal auf einer Abfolge von aufeinanderfolgenden Zuständen, die durch unveröffentlichte commitment transaction dargestellt werden. Bei jeder Lightning-Zahlung oder -Weiterleitung bilden die beiden Teilnehmer des Kanals ein neues Paar von commitment transaction, das die aktuelle Verteilung der Mittel im Kanal widerspiegelt. Alte commitment transaction werden obsolet.



Wenn eine der Parteien einen veralteten Status veröffentlicht, hat die andere Partei das Recht, dies zu sanktionieren und den vollen Betrag des Kanals zurückzufordern. In diesem Kapitel werfen wir einen kurzen Blick darauf, wie dieser Mechanismus funktioniert, und erklären dann, wie man einen ***Wachturm*** einrichtet: ein System, das Ihren Lightning-Knoten vor möglichen Betrugsversuchen schützt.



### Verstehen, wie Wachtürme funktionieren


Zu jedem Zeitpunkt verfügt jede Partei im Kanal über eine commitment transaction, die es ihr ermöglichen würde, den Kanal zu schließen und ihren Anteil an den Geldern zurückzuerhalten, wenn sie veröffentlicht würde. Dieser Vorgang wird als *erzwungene Schließung* bezeichnet. Wenn sie jedoch versuchen würden, einen älteren commitment transaction zu veröffentlichen, der einem früheren Zustand des Kanals entspricht, in dem er mehr sats besaß, würde diese Transaktion als Betrugsversuch betrachtet werden. In diesem Fall kann die Gegenpartei den mit diesem älteren Zustand verbundenen Sperrschlüssel verwenden, um den vollen Betrag des Kanals wiederzuerlangen, während der Betrüger vorübergehend durch die Zeitsperre blockiert wird.


Dieses System bedeutet, dass die Veröffentlichung eines alten Zustands, d. h. ein Betrugsversuch, sehr riskant ist: Wenn die andere Partei diese Transaktion im Mempool oder auf der Blockchain sieht, bevor die Zeitsperre abläuft, kann sie den Widerrufsschlüssel verwenden und das gesamte Geld zurückerhalten. **Daher hängt die Sicherheit Ihres Lightning-Kanals von Ihrer Fähigkeit ab, einen Betrugsversuch innerhalb des durch die Zeitsperre auferlegten Zeitfensters zu erkennen**.



#### Warum sind Wachtürme notwendig?



Der Sanktionsmechanismus funktioniert nur, wenn der Geschädigte dazu in der Lage ist:




- jeden neuen Bitcoin-Block überwachen, um festzustellen, ob ein Kanal commitment transaction veröffentlicht worden ist;
- feststellen, ob diese Transaktion dem letzten gültigen Zustand oder einem widerrufenen Zustand entspricht;
- im Falle eines widerrufenen Status die rechtmäßige Transaktion rechtzeitig zu verbreiten und den Widerrufsschlüssel zu verwenden, um alle Mittel vor Ablauf der Zeitsperre wiederzuerlangen.



![Image](assets/fr/023.webp)



Im Idealfall ist Ihr Lightning-Knoten rund um die Uhr online, synchronisiert und überwacht kontinuierlich die Blockchain. Aus diesem Grund kann er im Alleingang einen Betrugsversuch erkennen und reagieren. In der Praxis kann ein persönlicher Lightning-Knoten jedoch ausfallen, insbesondere im Falle eines längeren Stromausfalls oder eines Ausfalls der Internetverbindung.



Genau während dieser Ausfallzeiten wird das Risiko real: Wenn ein unehrlicher Peer einen alten Status veröffentlicht, während Ihr Knoten offline ist, und die Zeitsperre abläuft, ohne dass Sie reagieren, wird der Betrug wirksam. Sie verlieren einen Teil oder Ihr gesamtes Guthaben in diesem Kanal.



Um dieses Risiko zu verringern, wurden Watchtower eingeführt. Ein Watchtower ist ein externer Dienst, der die Blockchain in Ihrem Namen überwacht, indem er nach der möglichen Veröffentlichung eines alten Status auf einem Ihrer Kanäle scannt und, falls erforderlich, automatisch die Straftransaktion in Ihrem Namen sendet. Selbst wenn Ihr Lightning-Knoten über einen längeren Zeitraum offline ist, kann der Watchtower Ihre Gelder schützen, indem er alle Betrugsversuche überwacht und die entsprechende Strafe verhängt, sobald er einen solchen entdeckt.



#### Wie ein Wachturm funktioniert



Ein Wachturm ist so konzipiert, dass er so wenig Informationen wie möglich über Ihre Kanäle erfährt und gleichzeitig die Möglichkeit hat, im Falle eines Problems zu handeln:




- Für jeden neuen Kanalstatus mit einem Peer bereitet Ihr Knoten im Voraus eine potenzielle Straftransaktion vor. Im Falle eines Betrugs durch den Peer würde diese Transaktion es Ihnen ermöglichen, alle Gelder im Kanal zurückzuholen;
- Ihr Knoten verschlüsselt dann diese Straf-Transaktion mit der TXID des entsprechenden commitment transaction (diejenige, die verwendet würde, wenn der Betrüger einen Betrugsversuch unternehmen würde). Solange keine Schließung stattfindet, kann der Wachturm diese Transaktion nicht entschlüsseln, da er die TXID der betrügerischen Transaktion nicht vollständig kennt;
- Ihr Knoten sendet dem Wachturm ein Paket, das die verschlüsselte Straftransaktion und die Hälfte der TXID der potenziellen Betrugstransaktion enthält.



Da die an den Wachturm übermittelte TXID unvollständig ist, kann er die Rechtstransaktion nicht entschlüsseln. Er kann jedoch die Blockchain auf eine TXID überwachen, die mit dem Teil übereinstimmt, der ihm gehört. Findet er eine solche Transaktion, versucht er, die vollständige TXID dieser Transaktion zu verwenden, um Ihre Straftransaktion zu entschlüsseln. Gelingt die Entschlüsselung, weiß es, dass es sich um einen Betrugsversuch handelt, und veröffentlicht sofort die Straftransaktion für Sie.



![Image](assets/fr/024.webp)



Der Wachturm hat also keinen Einblick in die Details Ihrer Kanäle: weder die Identität Ihrer Peers, noch die Salden, noch die Struktur der Transaktionen. Er sieht nur verschlüsselte Pakete. Die einzige Information, die er ableiten kann, ist die Aktualisierungsrate Ihrer Kanäle, da er für jeden neuen Status ein Paket erhält, dessen Inhalt er aber nicht kennen kann. Im Falle eines Betrugs wird er sicherlich die Kanalinformationen durch Entschlüsselung der Straftransaktion herausfinden, aber zumindest wird Ihr sats gerettet werden.



Dieser Mechanismus beruht auf einem Kompromiss: Sie übertragen dem Wachturm die Fähigkeit, eine vorab signierte Strafzahlung zu veröffentlichen, aber diese Transaktion bleibt für den Wachturm völlig undurchsichtig, bis ein Betrug stattfindet. Der Wachturm kann weder die Empfänger ändern noch die Gelder umleiten, da er nur über eine bereits unterzeichnete Transaktion verfügt, deren Ergebnisse zu Ihren Gunsten eingefroren wurden. Er kann auch nicht die Details eines Kanals in einer legitimen erzwungenen oder kooperativen Schließung kennen, da die TXIDs nicht übereinstimmen. Andererseits bleibt der Watchtower eine minimal vertrauenswürdige dritte Partei: Sie müssen sich darauf verlassen, dass er online ist und Ihre Rechtstransaktion ordnungsgemäß übermittelt, wenn Sie sie benötigen.



#### Ein Wachturm werden



Theoretisch kann jeder Lightning-Knoten als Wachturm für andere Knoten fungieren (wenn sie dieselbe Implementierung verwenden, z. B. LND), während er selbst von anderen Knoten geschützt wird, die diese Rolle für ihn übernehmen. In den folgenden praktischen Abschnitten werde ich Ihnen zeigen, wie Sie diesen einfachen Mechanismus auf Ihrem LND unter Umbrel einrichten können.


Eine interessante Strategie könnte daher darin bestehen, mit vertrauenswürdigen Bitcoiner-Freunden zu vereinbaren, gegenseitig als Wächter zu fungieren. Sie überwachen deren Kanäle, und sie überwachen Ihre.



### Finden Sie einen altruistischen Wachturm



Wenn Sie niemanden in Ihrer Umgebung kennen, der einen Wachturmdienst anbieten kann, gibt es eine Reihe von uneigennützigen öffentlichen Wachtürmen, an die Sie sich anschließen können. In diesem LNP202-Kurs schlage ich zum Beispiel vor, dass Sie sich mit dem Wachtturmdienst verbinden, der gemeinsam von LN+ und Voltage angeboten wird und ein Wachtturm für LND ist.


Hier finden Sie die Anmeldedaten:



- Über Tor:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Über clearnet:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Als Dankeschön für die Bereitstellung dieses kostenlosen Wachtturm-Dienstes [können Sie über Lightning eine Spende tätigen](https://lightningnetwork.plus/donation).


Da wir nun einen altruistischen Wachturmdienst verwenden, wollen wir sehen, wie wir ihn auf unserem LND-Knoten unter Umbrel konfigurieren.


### Errichtung eines Wachturms


Klicken Sie in der Anwendung "Lightning Node" auf die drei Punkte oben rechts auf der Oberfläche und wählen Sie dann "Erweiterte Einstellungen".


![Image](assets/fr/025.webp)


Gehen Sie dann in das Menü "Watchtower".


![Image](assets/fr/026.webp)



Aktivieren Sie die Option "Watchtower Client" und klicken Sie dann auf die Schaltfläche "NODE SPEICHERN UND NEU STARTEN". Warten Sie auf den Neustart von LND.


![Image](assets/fr/027.webp)


Sobald der Neustart abgeschlossen ist, kehren Sie zum gleichen Menü zurück und geben die ID des altruistischen Wachturms Ihrer Wahl in das dafür vorgesehene Feld ein. Klicken Sie dann zur Bestätigung auf die Schaltfläche "ADD". Sie können auch den Parameter `Watchtower Client Sweep Fee Rate` anpassen: dies ist der Gebührensatz, den Sie bereit sind, für eine mögliche, vom Wachturm übertragene Gerechtigkeitstransaktion zu zahlen. Es besteht keine Notwendigkeit, einen zu hohen Satz zu wählen, aber Sie sollten auch einen zu niedrigen Satz vermeiden, da sonst das Rechtsgeschäft nicht rechtzeitig bestätigt wird.


Starten Sie Ihren Knoten neu, indem Sie auf die Schaltfläche `SAVE AND RESTART NODE` klicken, um diese Änderungen zu übernehmen.


![Image](assets/fr/028.webp)



Wenn Sie zu diesem Menü zurückkehren, werden Sie sehen, dass Ihr Blitznodeen jetzt durch den gerade hinzugefügten Wachturm geschützt ist.



![Image](assets/fr/029.webp)



Ein altruistischer Wachturm ist in der Regel ausreichend, vor allem, wenn Sie keine großen Geldbeträge auf Ihren Blitznodeen setzen und wenn Sie Ihren Knoten gut verwalten (lassen Sie ihn nicht zu lange aus). Für noch mehr Sicherheit können Sie auch mehrere hinzufügen, indem Sie den gleichen Prozess wiederholen.



## Eröffnen Sie Ihren ersten Lightning-Kanal


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Wenn Sie es bis hierher geschafft haben, wissen Sie bereits, dass ein Lightning-Knoten ohne Kanal ein bisschen wie ein leeres wallet ist: Er existiert, aber er ist nutzlos. Um Zahlungen senden oder empfangen zu können, muss Ihr Knoten mit mindestens einem anderen Knoten im Lightning-Netzwerk über einen Kanal verbunden sein. In Zukunft empfehlen wir aus Gründen der Ausfallsicherheit und der Routing-Effizienz dringend, mehrere Kanäle zu eröffnen. In den folgenden Kapiteln werden wir uns auch damit befassen, wie Sie Ihre liquiden Mittel verwalten, Ihre Kanaltopologie optimieren und fortschrittlichere Tools als die grundlegende LND-Schnittstelle auf Umbrel verwenden können.



In diesem Einführungskapitel geht es jedoch lediglich darum, zu verstehen, wie man einen guten Lightning-Peer auswählt, wo man die Informationen findet, die man für die Auswahl seiner Peers benötigt, und schließlich, wie man seinen ersten Kanal über die grundlegende LND-Schnittstelle öffnet.



### Wie wählt man einen guten Lightning-Peer aus?



Wenn Sie einen Kanal eröffnen, müssen Sie einen Peer auswählen: einen anderen Lightning-Knoten, mit dem Ihr Knoten über einen Kanal direkt verbunden sein wird. Die Wahl des Peers ist wichtig, da sie einen direkten Einfluss auf den Kanal hat:




- die Leichtigkeit, mit der Ihre Zahlungen ihren Weg finden;
- die Zuverlässigkeit Ihrer Kanäle im Laufe der Zeit;
- ihre Routingkosten.



Es gibt keine perfekte Übereinstimmung für alle, aber es gibt eine Reihe von zuverlässigen Kriterien, um gute Kandidaten zu identifizieren.



#### 1. Konnektivität der Knoten



Ein guter Peer ist ein Knoten, der gut mit dem Lightning-Netzwerk verbunden ist. Das bedeutet nicht nur, dass er eine große Anzahl von Kanälen hat (obwohl dies ein Indikator sein kann), sondern vor allem, dass er mit anderen zuverlässigen Knoten verbunden ist und eine ausreichend zentrale Position im Netzwerkgraphen einnimmt.



Ein gut angebundener Knotenpunkt erhöht Ihre Chancen, eine effiziente Route zu den meisten Zahlungszielen zu finden. Außerdem wird dadurch die Anzahl der benötigten Zwischennodeen reduziert, was die Kosten niedrig hält.



Umgekehrt können Sie Ihre Möglichkeiten einschränken, wenn Sie Ihren ersten Kanal für einen isolierten oder schwach angebundenen Knotenpunkt öffnen: Sie können diesen Peer zwar bezahlen, aber es wird viel schwieriger sein, den Rest des Netzes zu bezahlen.



#### 2. Kapitalisierung und Kanalkapazität



Ein guter Peer ist auch ein ausreichend kapitalisierter Knoten. Dies zeigt sich an seiner gesamten Kanalkapazität (die Summe der sats, die allen seinen Kanälen zugewiesen sind) und seiner durchschnittlichen Kanalkapazität (es ist oft besser, nur wenige gut kapitalisierte Kanäle zu haben als viele kleine).



Ein Knoten mit lächerlicher Kapazität oder dessen Kanäle alle winzig klein sind, wird nicht in der Lage sein, Zahlungen mit großen Beträgen weiterzuleiten, was für Sie zu Routing-Fehlern führt.



#### 3. Spesenpolitik



Jeder Knoten legt seine eigenen Weiterleitungsgebühren fest (Grundgebühr und Gebührensatz). Ein guter Peer wird keine exorbitanten Gebühren für strategische Kanäle verlangen. Für einen ersten Kanal ist es am besten, einen Knoten mit eher moderaten Gebühren zu wählen, um Ihre eigenen Zahlungen nicht zu behindern.



Denken Sie daran, dass auch Ihre eigenen Routing-Gebühren Einfluss darauf haben, wie andere Sie als Peer wahrnehmen: Ein Knotenpunkt, der seine Gebühren ständig ändert oder absurde Kosten auferlegt, wird selten geschätzt.



#### 4. Stabilität und Dienstalter



Die Stabilität der Peers ist ein sehr wichtiges Kriterium. Ein guter Knoten hat eine hohe Betriebszeit (er ist sehr selten offline), er hält seine Kanäle für eine lange Zeit offen und er öffnet/schließt nicht ständig Kanäle ohne Grund.



Alte und noch aktive Kanäle sind ein gutes Signal: Sie deuten darauf hin, dass die Beziehung für den Peer profitabel ist, dass der Knotenpunkt weiß, wie er sein Kapital verwalten kann, und dass er nicht jederzeit geschlossen wird, so dass Sie nicht ständig Onchain-Gebühren für das Schließen und Wiedereröffnen zahlen müssen.



Umgekehrt kann ein Peer, der oft offline ist oder Kanäle schnell schließt, eine Quelle von Problemen für Sie und von zusätzlichen Kosten für die Eröffnung neuer Kanäle sein.



Auch mit diesen Kriterien werden Sie nicht gleich beim ersten Mal eine perfekte Wahl treffen. Das ist normal: Die wahre Qualität eines Peers zeigt sich erst bei seiner Verwendung. Deshalb ist es wichtig, dass:




- überwachung der Kanalaktivität (geroutetes Volumen, Verfügbarkeit usw.);
- kanäle schließen, die keinen Zweck erfüllen oder deren Teilnehmer zu oft offline sind;
- ihr Kapital im Laufe der Zeit in bessere Peers umschichten.



Dabei geht es nicht darum, jeden Tag Kanäle zu öffnen und zu schließen (was mit hohen Onchain-Kosten verbunden wäre), sondern darum, die Topologie allmählich so zu entwickeln, dass sich eine Reihe zuverlässiger, gut angebundener Peers ergibt, die Ihren Anforderungen entsprechen.



### Wie kann ich einen Peer finden?



Um diese Kriterien anzuwenden, benötigen Sie Tools, die das Lightning-Netzwerk sichtbar machen. Es gibt mehrere Explorer und Dienste, die dies ermöglichen. Zu den bekanntesten Lightning-Explorern gehören [1ML](https://1ml.com/) und [Amboss](https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

Hier empfehle ich Ihnen jedoch [das Lightning-Terminal-Tool von Lightning Labs](https://terminal.lightning.engineering/), das eine (zugegebenermaßen auf teilweise subjektiven Kriterien basierende) Rangliste der Lightning-Knoten erstellt, die für die Eröffnung eines Kanals als besonders relevant erachtet werden.



![Image](assets/fr/030.webp)



Das Problem mit den sehr großen Lightning-Knoten an der Spitze dieses Rankings ist, dass die meisten keine Channel-Eröffnungen unter sehr hohen Beträgen akzeptieren. Viele wenden auch strenge Peer-Management-Richtlinien an, was dazu führen kann, dass Ihr Kanal geschlossen wird. Andererseits haben diese Knoten angesichts der Anzahl ihrer Verbindungen im Allgemeinen keinen Bedarf an eingehender Liquidität.



Ich würde Ihnen daher raten, sich in der Rangliste nach unten vorzuarbeiten, um einen Knoten zu finden, der gut verbunden, zuverlässig und zentral genug im Netzgraphen ist, ohne übermäßig groß zu sein. Hier habe ich zum Beispiel den Knoten Lightning auf stacker.news identifiziert, der sehr gut verbunden ist, eine hohe Kapazität hat und eine zentrale Position im Netzwerkgraphen einnimmt.



![Image](assets/fr/031.webp)



Ein weiterer interessanter Ansatz besteht darin, einen Kanal zu einem Knotenpunkt zu öffnen, der Liquidität benötigt, z. B. ein Ihnen bekannter Händler, ein Verein oder eine Gemeinschaft. Diese Strategie hat drei Vorteile:




- Da das gewählte Unternehmen Liquiditätszuflüsse benötigt, hat es logischerweise weniger Anreize, Ihren Kanal ohne Grund zu schließen;
- Seine wirtschaftliche Tätigkeit erhöht die Chancen auf eine Weiterleitung über diesen Kanal und damit auf die Erhebung bestimmter Gebühren;
- Sie tun dem Ökosystem einen Gefallen und leisten einen wertvollen Beitrag für andere Bitcoiner.



Sobald du einen relevanten Knoten identifiziert hast, kannst du seine Knoten-ID abrufen. Dabei handelt es sich einfach um eine Verkettung des öffentlichen Schlüssels des Knotens, eines "@"-Trennzeichens, seiner IP- oder Tor-Adresse und des verwendeten Ports. Diese ID ist leicht über das Profil des Knotens in jedem Lightning-Explorer zugänglich.



### Öffnen Sie Ihren ersten Kanal über LND



Nun, da wir den Knoten identifiziert haben, mit dem wir unseren ersten Kanal öffnen wollen, müssen wir sats mit ihm verbinden. Dazu müssen Sie den Bitcoin in die Kette wallet einspeisen, die mit Ihrem LND verbunden ist.



Suchen Sie auf der LND-Hauptschnittstelle Ihren "Bitcoin Wallet" und klicken Sie dann auf die Schaltfläche "Einzahlen". Eine Onchain-Empfangsadresse ist dann generated: Senden Sie sats dorthin. Der Betrag, den Sie überweisen müssen, hängt von der Kapazität ab, die Sie Ihrem ersten Kanal zuweisen möchten, aber bedenken Sie, dass Sie etwas mehr als die angestrebte Kapazität senden müssen. Wenn Sie z. B. einen Kanal mit 500.000 sats eröffnen wollen, senden Sie nicht genau 500.000 sats, sondern einen höheren Betrag.



![Image](assets/fr/032.webp)



Sobald die Transaktion übertragen wurde, erscheint sie in der Schnittstelle. Warten Sie auf die Bestätigung, bevor Sie den Kanal öffnen. Sie sehen einen grünen Pfeil neben dem Vorgang, wenn er bestätigt wurde.



![Image](assets/fr/033.webp)



Scrollen Sie nach unten zur Hauptschnittstelle und klicken Sie dann auf "+ OPEN CHANNEL".



![Image](assets/fr/034.webp)



Geben Sie die "Node ID" des Knotens ein, mit dem Sie einen Kanal eröffnen möchten, geben Sie den Betrag an, den Sie festschreiben möchten, und passen Sie dann die Gebühr für die Eröffnungstransaktion entsprechend dem Stand des Onchain-Gebührenmarktes an. Vergewissern Sie sich natürlich vorher, dass Sie genügend Geld in Ihrem LND Onchain-Portfolio haben.



Wenn alle Parameter eingestellt sind, klicken Sie auf die Schaltfläche "KANAL ÖFFNEN".



![Image](assets/fr/035.webp)



Warten Sie darauf, dass die Eröffnungstransaktion auf der Kette bestätigt wird. Ihr erster Kanal ist nun offiziell in Betrieb: Herzlichen Glückwunsch!



Sie sehen, dass sich im Moment 100 % der Liquidität des Kanals auf meiner Seite befindet: Das ist normal, denn ich bin derjenige, der den Kanal eröffnet hat. Wenn sich Zahlungen und Routing weiterentwickeln, wird sich diese Verteilung ändern, aber die Gesamtkapazität des Kanals wird immer gleich bleiben.



![Image](assets/fr/036.webp)



Jetzt, da Sie einen Kanal haben, können Sie Ihre ersten Lightning-Zahlungen vornehmen, vorausgesetzt, der ausgewählte Knoten ist ordnungsgemäß mit dem Netzwerk verbunden. Natürlich werden wir uns in späteren Kapiteln ansehen, wie Sie eine bequemere Methode zum Bezahlen von Lightning-Rechnungen über Ihr Mobiltelefon einrichten können. Aber jetzt wollen wir erst einmal versuchen, eine erste Zahlung direkt von LND an Umbrel zu tätigen.



Klicken Sie dazu im Abschnitt "Lightning Wallet" auf die Schaltfläche "Senden" und fügen Sie dann die Rechnung ein, die Sie einstellen möchten.



![Image](assets/fr/037.webp)



Der Rechnungsbetrag wird angezeigt. Bestätigen Sie die Zahlung, indem Sie auf die Schaltfläche "SENDEN" klicken.



![Image](assets/fr/038.webp)



Wenn eine gültige Route gefunden wird, sollte Ihre erste Blitzzahlung erfolgreich sein.



![Image](assets/fr/039.webp)



Wenn wir uns nun die Verteilung der Liquidität im Kanal ansehen, sehen wir, dass mein Peer jetzt 5.002 sats auf seiner Seite hat. Dies entspricht den 5.000 sats der Zahlung, die ich gerade getätigt habe und die er an den Knoten des Empfängers weitergeleitet hat. Die zusätzlichen 2 sats entsprechen den von mir gezahlten Weiterleitungsgebühren, da der Empfänger genau 5.000 sats erhalten hat.



![Image](assets/fr/040.webp)



Um die Zuverlässigkeit unserer Zahlungen zu verbessern, wird es natürlich notwendig sein, andere Kanäle zu öffnen. Je nach Zielsetzung müssen wir auch einen Weg finden, um eingehende Liquidität zur Verfügung zu stellen, damit wir Zahlungen auf Lightning erhalten können. Dies wird das Thema des nächsten Abschnitts sein.



# Verwalten Ihres Lightning-Knotens


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Definieren Sie Ihr Knotenbetreiberprofil


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Nachdem Ihr Lightning-Knoten eingerichtet und in Betrieb ist, müssen Sie im nächsten Schritt Ihr Händlerprofil festlegen. Dies ist eine wichtige Entscheidung, da sie Ihre Kanalöffnungsstrategie, die Art der von Ihnen bevorzugten Peers und die Art und Weise, wie Sie Liquidität verwalten, bestimmt.



Damit dies bei Lightning funktioniert, brauchen Sie Liquidität in der richtigen Richtung. Die ausgehende Liquidität entspricht Ihrer Zahlungsfähigkeit (sats auf Ihrer Seite der Kanäle verfügbar). Eingehende Liquidität entspricht Ihrer Fähigkeit, zu empfangen (sats auf der Seite Ihrer Partner). Mit anderen Worten, Ihr Profil läuft auf eine einfache Frage hinaus: Verlassen Ihre sats Ihren Knotenpunkt die meiste Zeit über, oder gehen sie in ihn hinein?



### Der Verbraucher



Dies ist das Profil der großen Mehrheit der Nutzer. Sie nutzen Ihren Node, um Lightning-Zahlungen vorzunehmen: um Waren und Dienstleistungen zu kaufen, Rechnungen zu bezahlen, Trinkgelder zu versenden - kurzum, um Lightning als schnelles Zahlungsmittel zu nutzen. Auf der anderen Seite erhalten Sie wenig oder nur geringfügig von Lightning, zum Beispiel ein paar Spenden, Erstattungen zwischen Freunden oder ein paar Mikrozahlungen.



Dieses Profil ist am einfachsten zu handhaben, denn Ihr Hauptbedürfnis ist es, zahlen zu können. In der Praxis bedeutet dies, dass Sie ausgehende Liquidität benötigen. Sobald Sie einen oder mehrere Kanäle in der richtigen Größe zu stabilen, gut vernetzten Knotenpunkten geöffnet haben, werden Ihre ausgehenden Zahlungen mechanisch Liquidität auf die andere Seite Ihrer Kanäle bringen. Genau diese Bewegung schafft natürlich eine angemessene Menge an eingehender Liquidität. Selbst wenn Sie nicht regelmäßig Geld erhalten möchten, können Sie daher von Zeit zu Zeit Geld erhalten, ohne eine komplexe Strategie zu entwickeln. Sie müssen sich also keine Sorgen um Ihre eingehende Liquidität machen.



In diesem LNP202-Kurs werden wir uns auf dieses "Verbraucher"-Knotenbetreiberprofil konzentrieren, da es dasjenige ist, das fast allen Bitcoin-Nutzern auf Lightning entspricht.



### Der Einzelhändler



Der Händler ist in gewisser Weise das Gegenteil des Verbrauchers. Hier besteht das Hauptziel nicht darin, zu zahlen, sondern zu kassieren. Ein Unternehmen, ein Dienstleistungsanbieter, ein Online-Shop oder eine Verkaufsstelle, die Lightning akzeptiert, wird viele eingehende Zahlungen erhalten und relativ wenige ausgehende Zahlungen von diesem Knotenpunkt aus tätigen.



Dieses Profil ist anspruchsvoller, da eine verweigerte Blitzzahlung potenziell einen verlorenen Verkauf bedeutet. Die Priorität liegt daher bei der eingehenden Liquidität. Wenn Ihr Knotenpunkt nicht über genügend eingehende Liquidität verfügt, werden die Zahlungen Ihrer Kunden scheitern, selbst wenn sie das Geld haben, einfach weil es keinen Weg gibt, die Liquidität auf dem richtigen Weg zu Ihnen zu bringen.



Die größte Herausforderung für den Händler ergibt sich auch aus der natürlichen Entwicklung der Kanäle. Wenn Sie nur empfangen, werden sich Ihre Kanäle allmählich auf Ihrer Seite füllen. Sie brauchen also Mechanismen, um Ihre eingehende Liquidität zu erhalten und zu erneuern.



Es gibt jedoch auch einen einfacheren Fall: das gemischte Verbraucher-/Händlerprofil. Wenn Sie über Lightning sammeln, aber auch über Lightning ausgeben (Geschäftsausgaben, Zahlungen an Lieferanten oder sogar private Ausgaben), dann erzeugen Ihre Zahlungsausgänge auf natürliche Weise wieder Zahlungseingänge. Die Verwaltung wird reibungsloser, da sich die Zahlungsströme gegenseitig ausgleichen, und Sie müssen weniger auf künstliche Mechanismen zurückgreifen, die nur dazu dienen, die Liquidität der Eingänge wiederherzustellen.



### Der Router



Der Router ist ein spezielles Profil. Er nutzt seinen Lightning-Knoten nicht, um zu zahlen oder zu kassieren, sondern um die Zahlungen anderer Personen weiterzuleiten und Gebühren einzuziehen. Das Ziel ist es, eine nützliche, zuverlässige und wirtschaftlich wettbewerbsfähige Route innerhalb des Lightning-Graphen zu sein.



Um ehrlich zu sein, ist ein Router auf Lightning ein komplexeres Geschäft, als es aussieht, und Rentabilität ist schwer zu erreichen. Zunächst einmal ist das Öffnen und Schließen von Kanälen mit hohen Onchain-Kosten verbunden. Um effizient zu routen, müssen Sie oft Ihre Topologie anpassen, testen, leistungsschwache Kanäle schließen, neue eröffnen und Ihre Liquidität regelmäßig neu ausbalancieren. Zweitens ist der Wettbewerb hart: Große, etablierte Knotenpunkte erobern naturgemäß einen großen Teil des Datenverkehrs, und es ist schwierig, Fuß zu fassen, ohne erhebliches Kapital in gut dimensionierten Kanälen zu binden.



Außerdem gibt es hohe betriebliche Anforderungen. Ein Routing-Knoten muss extrem stabil sein, überwacht, ordnungsgemäß gesichert und rigoros verwaltet werden. Sie müssen die Leistung der Kanäle überwachen, Ihre Gebührenpolitik anpassen, eine ausgewogene Liquidität aufrechterhalten, Peers verwalten und technische Probleme schnell lösen. Dieses Maß an Engagement kann als technisches Hobby oder als Beitrag zur Infrastruktur interessant sein, aber wenn Ihr Ziel einfach darin besteht, Lightning auf souveräne Weise zu nutzen, ist der Einstieg in das Routing, um Geld zu verdienen, selten relevant. Deshalb wird in diesem LNP202-Kurs dieses Profil nicht vertieft.



### Verschaffen Sie sich einen klaren Überblick, bevor Sie weitermachen



Wenn Sie dem Profil eines Verbrauchers entsprechen, wird Ihre Priorität darin bestehen, zuverlässig und mit einfacher Verwaltung bezahlen zu können. Wenn Sie ein Händler sind, wird Ihre Priorität darin bestehen, dass Sie ohne Probleme Geld einnehmen können, was eine Strategie zur Beschaffung von Liquidität nach innen voraussetzt. Wenn Sie das Routing in Betracht ziehen, müssen Sie es als eine anspruchsvolle, wirtschaftlich unsichere und zeitaufwändige Tätigkeit betrachten.



Wenn Sie dieses Profil jetzt definieren, vermeiden Sie eine klassische Falle: die Anwendung einer Kanalstrategie, die für einen Händler oder Router konzipiert ist, obwohl Sie einfach nur ein Nutzer sind, der bezahlen möchte.



## Verwendung eines Lightning-Knotenmanagers


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



Im vorherigen Teil dieses LNP202-Schulungskurses haben wir die Basisschnittstelle der Anwendung "Lightning Node" auf dem Umbrel verwendet. Diese Schnittstelle reicht für die wichtigsten Vorgänge aus (Überprüfung von Salden, Anzeige der Bargeldverteilung, Öffnen und Schließen von Kanälen), ist aber absichtlich sehr vereinfacht. Diese Einfachheit schränkt die verfügbaren Optionen ein und bietet keinen Zugang zu vielen der erweiterten Funktionen Ihres LND-Knotens. Aus diesem Grund werden wir jetzt eine andere, umfassendere Lightning-Knotenverwaltungssoftware verwenden.



Diese zusätzliche Software wird einfach eine ergänzende Verwaltungsschnittstelle für Ihren Knoten sein. Das bedeutet, dass Sie die "Lightning Node"-Schnittstelle weiterhin parallel verwenden können, und sogar mehrere verschiedene, wenn Sie dies wünschen. Es handelt sich dabei lediglich um verschiedene Möglichkeiten, mit demselben Lightning-Knoten zu interagieren.



Zu den bekanntesten Softwareprogrammen gehören:




- [Alby Hub](https://albyhub.com/);
- [Ride The Lightning](https://www.ridethelightning.info/);
- [ThunderHub](https://thunderhub.io/).



Alle drei sind gute Lösungen. Wenn Sie möchten, können Sie alle drei mit Ihrem Knotenpunkt testen, bevor Sie sich für diejenige entscheiden, die Ihnen am besten gefällt. Ich persönlich verwende ThunderHub aus Gewohnheit und weil es mir vollständiger erscheint als die anderen. Dies ist das Tool, das ich in dieser Schulung vorstellen werde, aber Sie können auch eine der beiden anderen Alternativen wählen. Für jedes dieser Programme gibt es eine eigene Anleitung auf Plan ₿ Academy.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### ThunderHub installieren



Diese Programme können alle ganz einfach über den Umbrel App Store installiert werden. Wie gesagt, wir verwenden hier ThunderHub, aber wenn Sie später ein anderes Programm testen möchten, ist die Vorgehensweise ähnlich.



![Image](assets/fr/041.webp)



Umbrel bietet Ihnen ein Standardpasswort für den Zugang zu ThunderHub. Kopieren Sie es: Sie werden es sofort brauchen. Denken Sie auch daran, es in Ihrem Passwort-Manager zu speichern, da Sie bei jedem Öffnen der Software danach gefragt werden.



![Image](assets/fr/042.webp)



Klicken Sie auf "Anmelden" und fügen Sie das von Umbrel bereitgestellte Passwort ein, um sich anzumelden.



![Image](assets/fr/043.webp)



Sie gelangen dann zur ThunderHub-Startseite, auf der die wichtigsten Informationen zu Ihrem Lightning-Knoten angezeigt werden.



![Image](assets/fr/044.webp)



Für den Anfang empfehle ich Ihnen, die Zwei-Faktor-Authentifizierung (2FA) zu aktivieren. Klicken Sie in den Einstellungen einfach auf "Aktivieren" neben "2FA aktivieren" und folgen Sie dann dem üblichen Verfahren.



![Image](assets/fr/045.webp)



### ThunderHub verwenden



ThunderHub ist relativ leicht zu erlernen. Alle Menüs sind über die linke Spalte der Benutzeroberfläche zugänglich. Zusammenfassend lässt sich sagen, was die einzelnen Menüs bewirken:




- startseite: Knotenübersicht, Bilanzen und Schnellaktionen;
- dashboard: anpassbares Dashboard mit Widgets und Metriken;
- peers: Anzeige und Verwaltung von Verbindungen zu anderen Lightning-Knoten;
- kanäle": vollständige Verwaltung der Kanäle (Liquidität, Gebühren, Schließung usw.);
- rebalance": ein Instrument zur Wiederherstellung des Gleichgewichts von Kanälen durch Rundzahlungen;
- transaktionen: Verlauf der gesendeten und empfangenen Blitzzahlungen;
- forwards": Routing-Statistiken und Kosten generated von Ihrem Knoten;
- kette": Bitcoin Onchain-Portfolio (UTXOs und Transaktionen);
- gW-201-Integration zur Überwachung und Sicherung;
- tools": erweiterte Tools (Backups, Berichte, Makronen, Signaturen usw.);
- tauschen: Blitz-/Onchain-Swaps über Boltz;
- statistiken: Gesamtstatistiken und Leistung Ihres Lightning-Knotens.



Mit diesen Funktionen verfügen Sie über alle Werkzeuge, die Sie benötigen, um Ihren Lightning-Knoten effizient zu verwalten. Es ist nicht notwendig, jede Option sofort im Detail zu beherrschen: Wir werden sie im Laufe dieses Kurses nach und nach erforschen. Wenn Sie sich jedoch eingehender mit der Software befassen möchten, schauen Sie sich unser ThunderHub-Tutorial an:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Das Menü, das uns hier am meisten interessiert, ist "Channels". Es bietet einen detaillierten Überblick über alle Kanäle in Ihrem Knoten mit ihrer Liquiditätsverteilung. Insbesondere können Sie unter "Open" sehen, welche Kanäle offen sind, unter "Pending", welche darauf warten, geöffnet oder geschlossen zu werden, und unter "Closed", welche bereits geschlossen sind.



![Image](assets/fr/047.webp)



Für einen bestimmten Kanal können Sie auf den Namen oder die Kanal-ID des Peers klicken, um dessen Amboss-Seite zu öffnen und weitere Informationen zu erhalten. Sie können auch auf das Bleistiftsymbol klicken, um die Parameter des Kanals zu ändern, einschließlich der Gebührenrichtlinie, die für diesen Kanal gilt, wenn Ihr Knoten Zahlungen an den Knoten Ihres Peers weiterleitet.



![Image](assets/fr/048.webp)



Wenn Sie Ihren Lightning-Knoten hauptsächlich als "Verbraucher" verwenden, brauchen Sie diese Gebühren nicht zu ändern: Sie können die Standardwerte beibehalten. Wenn Sie hingegen besser verstehen möchten, wie Routing-Gebühren in Lightning funktionieren, empfehle ich Ihnen die Schulung LNP 201 und insbesondere Kapitel 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Wenn Sie auf das kleine Kreuz neben einem Peer klicken, können Sie die Schließung eines Kanals veranlassen. Wenn Sie z.B. feststellen, dass ein Peer regelmäßig inaktiv ist, kann es sinnvoll sein, diesen Kanal zu schließen, um Ihr Kapital einem zuverlässigeren Peer zuzuweisen.



Sie haben dann zwei Möglichkeiten. Die erste, und immer vorzuziehende, ist die kooperative Schließung. Indem Sie diese Aktion bestätigen, bittet Ihr Knoten Ihren Peer, den Kanal gemeinsam zu schließen. Wenn er zustimmt, können Sie die Onchain-Schließungstransaktion übertragen und Ihren Anteil an den Mitteln zurückerhalten. Die Vorteile dieser Methode liegen darin, dass Sie die Onchain-Gebühren für die Transaktion wählen und somit unnötige Kosten vermeiden und dass die Gelder schneller und ohne Zeitsperre zurückerhalten werden.



![Image](assets/fr/049.webp)



Die zweite Option ist die erzwungene Schließung. In diesem Fall fragen Sie nicht nach dem Einverständnis der Gegenstelle und senden direkt den letzten commitment transaction in Ihrem Besitz. Ich würde diese Methode nicht empfehlen, es sei denn, sie ist der letzte Ausweg, z. B. wenn die Gegenstelle systematisch kooperative Abschlüsse verweigert oder nicht mehr antwortet. Die erzwungene Schließung hat zwei große Nachteile: Die Gebühren sind oft sehr hoch, da sie im Voraus festgelegt wurden, um einen Anstieg der Onchain-Gebühren vorwegzunehmen, und es gibt eine Verzögerung bei der Rückerstattung der Gelder, da sie durch eine Zeitsperre blockiert sind. Diese Zeitsperre gibt Ihrem Peer die Zeit, im Falle eines Betrugsversuchs zu reagieren (was hier natürlich nicht der Fall ist, aber Sie müssen trotzdem warten).



![Image](assets/fr/050.webp)



Um einen neuen Kanal zu eröffnen, gehen Sie auf das Menü "Home" und klicken Sie auf "Kanal eröffnen" im Abschnitt "Liquidity". Sie können dann die ID des gewählten Knotens, die Kanalkapazität, die gewünschte Lightning-Routing-Gebühr und die Onchain-Gebühr für die Eröffnungstransaktion eingeben.



![Image](assets/fr/051.webp)



Dies sind die wichtigsten Aktionen, die Sie mit ThunderHub durchführen müssen. Im weiteren Verlauf dieses LNP202-Kurses werden wir weitere Funktionen kennenlernen.



## Beschaffung von Liquidität


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Wie Sie sehen, ist es nicht besonders kompliziert, ausgehende Liquidität zu haben, um Zahlungen mit Lightning zu tätigen. Öffnen Sie einfach auf eigene Initiative Kanäle zu anderen Knotenpunkten und beginnen Sie, sats zu senden. Auf der anderen Seite ist es komplizierter, eingehende Liquidität zu haben, um Zahlungen auf Lightning zu erhalten, da Sie entweder andere Knoten benötigen, um Kanäle zu Ihnen zu öffnen, oder Sie müssen die Liquidität selbst bewegen, indem Sie Zahlungen leisten.



Wenn Sie ein "Verbraucher"-Profil wählen, müssen Sie sich in der Regel keine Gedanken über eingehende Liquidität machen. Ihre Nutzung des Lightning-Knotens wird überwiegend zahlungsorientiert sein und nicht auf Cash-in ausgerichtet. Indem Sie einfach ein paar Lightning-Zahlungen tätigen, werden Sie im Laufe der Zeit auf natürliche Weise Liquiditätszuflüsse erzeugen.



Wenn Sie hingegen ein "Händler"-Profil haben, ist die Situation umgekehrt: Sie werden hauptsächlich Zahlungen einholen und nur wenige davon leisten. Sie können sich also nicht nur auf Ihre eigenen Zahlungen verlassen, um Liquidität zu erhalten. Es ist daher erforderlich, dass andere Lightning-Knotenpunkte Kanäle zu Ihnen öffnen. Doch wie kann dies erreicht werden? Wie bringt man andere Betreiber dazu, Kapital für einen zu binden? Genau das werden wir in diesem Kapitel untersuchen.



### Kauf von eingehender Liquidität



Wie zu erwarten, ist es am effektivsten, jemanden zum Handeln zu bewegen, indem man ihn bezahlt. Für eingehende Liquidität zu Ihrem Lightning-Knotenpunkt gilt genau dasselbe Prinzip. Der einfachste Weg, Kanäle zu Ihrem Knotenpunkt zu bekommen, ist, für den Service und die damit verbundene Kapitalbindung zu bezahlen.



Wenn Sie ein Unternehmen oder ein Einzelhändler sind, bedeutet dieser Ansatz, dass Sie schnell zuverlässige Kanäle erhalten, um Zahlungen von Ihren Kunden ohne Reibungsverluste einzuziehen.



Es gibt viele Möglichkeiten, Inbound-Liquidität zu kaufen. Ich persönlich verwende und empfehle die Plattform [Magma](https://magma.amboss.tech/) von Amboss. Sie ist sehr einfach zu bedienen, die Eröffnung eines Kanals geht schnell und die Preise sind im Allgemeinen angemessen. Magma funktioniert wie ein Marktplatz mit Anbietern und Nachfragern, aber Version 2 hat die Erfahrung stark vereinfacht: Erstellen Sie einfach eine Anfrage, zahlen Sie den Preis per Lightning, und Magma gleicht sie automatisch mit dem besten verfügbaren Angebot ab. Nach sechs Onchain-Bestätigungen ist Ihr Kanal mit eingehender Liquidität einsatzbereit. Und so funktioniert es:



Gehen Sie auf [die Magma-Website](https://magma.amboss.tech/buy), in den Abschnitt "Kanäle kaufen".



![Image](assets/fr/052.webp)



Wenn Sie möchten, können Sie ein Konto einrichten, um Ihre Einkäufe zu verfolgen, dies ist jedoch nicht zwingend erforderlich. Wenn Sie kein Konto einrichten, stellt Magma Ihnen lediglich eine Sitzungsnummer zur Verfügung, mit der Sie Ihre Einkäufe zu einem späteren Zeitpunkt abrufen können.



Sobald Sie auf der Website sind, geben Sie die erforderlichen Informationen für den Kauf von Liquidität ein. Wählen Sie "Einmalig" für einen einmaligen Kauf und geben Sie dann den Betrag ein, den Sie für eingehende Liquidität zu zahlen bereit sind. Je höher der gezahlte Betrag ist, desto größer ist die Kapazität des Kanals, der für Ihren Knotenpunkt geöffnet wird. Unten sehen Sie eine Schätzung der Kapazität des Kanals: Dies ist ein Näherungswert, da der endgültige Betrag vom besten von Magma gefundenen Angebot abhängt, das manchmal höher und manchmal niedriger ist.



![Image](assets/fr/053.webp)



Geben Sie dann Ihre Knoten-ID ein. Sie finden sie z. B. im Menü "Knoten-ID" der Anwendung "Lightning Node" auf Umbrel.



![Image](assets/fr/054.webp)



Wenn Sie alle Angaben gemacht haben, klicken Sie auf die Schaltfläche "Bestellung prüfen und öffnen".



![Image](assets/fr/055.webp)



Wenn Sie kein Konto erstellt haben, erhalten Sie von Magma einen Sitzungsschlüssel und eine Sicherungsdatei. Bewahren Sie diese beiden Elemente an einem sicheren Ort auf, da sie es Ihnen ermöglichen, die Bestellung zu einem späteren Zeitpunkt abzurufen oder ihren Status zu verfolgen, falls ein Problem auftritt. Sobald Sie die Datei gespeichert haben, klicken Sie auf die Schaltfläche "Mit Lightning bezahlen".



![Image](assets/fr/056.webp)



Magma generate stellt dann eine Blitzrechnung über den von Ihnen gewählten Betrag aus. Diese müssen Sie bezahlen. Wenn Sie bereits Kanäle auf Ihrem Lightning-Knoten haben, können Sie direkt von dort aus bezahlen oder ein anderes externes Lightning-wallet verwenden.



![Image](assets/fr/057.webp)



Sobald die Zahlung erfolgt ist, wird die Transaktion in der Magma-Schnittstelle als bearbeitet angezeigt.



![Image](assets/fr/058.webp)



Nach ein paar Minuten wird die Anfrage bearbeitet: Ein Kanal mit sats wird für Ihren Lightning-Knoten geöffnet. Sobald die Eröffnungstransaktion onchain bestätigt wurde, haben Sie Zugang zu der entsprechenden eingehenden Liquidität.



![Image](assets/fr/059.webp)



Magma ist auch direkt in ThunderHub integriert. Scrollen Sie auf der Registerkarte "Home" nach unten zum Abschnitt "Liquidity" und klicken Sie auf "Buy Inbound Liquidity". Sie müssen nur noch den gewünschten Betrag eingeben und bestätigen. Sie brauchen keine Rechnungen manuell zu bezahlen, da ThunderHub automatisch die Zahlung von Ihrem Knotenpunkt übernimmt.



![Image](assets/fr/060.webp)



Für Sie als Händler ist diese Art von Dienst besonders geeignet, da er Ihnen ermöglicht, schnell eine große Menge an eingehender Liquidität von zuverlässigen Knotenpunkten zu erhalten, was garantiert, dass Ihre Kunden Sie ohne Schwierigkeiten bezahlen können. Wenn Sie hingegen eine Privatperson sind oder nicht für eingehende Liquidität bezahlen möchten, gibt es auch kostenlose Lösungen. Schauen wir uns das mal an.



### Kooperative eingehende Liquidität



Wenn Sie kein Händler sind, aber dennoch Liquidität benötigen (z. B. um Ihren Node beim Start vorzubereiten, während Sie auf einige Zahlungen warten), müssen Sie nicht unbedingt dafür bezahlen. Eine von mir bevorzugte Lösung ist die Zusammenarbeit mit anderen Knotenbetreibern, die ebenfalls eingehende Liquidität benötigen, um gegenseitig Lightning-Kanäle zu öffnen. Auf diese Weise erhalten Sie durch die Eröffnung eines Kanals ausgehende Liquidität und gleichzeitig eingehende Liquidität, und das kostenlos (abzüglich der Onchain-Gebühren für die Eröffnung).



Sie können dies natürlich auch direkt mit anderen Bitcoinern vereinbaren. Es gibt jedoch eine Plattform, die sich dieser Art von Kreisöffnungen widmet: [Lightning Network +](https://lightningnetwork.plus/). Das Prinzip besteht darin, nicht zwei Kanäle zwischen denselben Personen zu öffnen, sondern zirkuläre Eröffnungen mit mindestens drei oder sogar mehr Teilnehmern einzurichten.



Nehmen wir ein Beispiel, um zu verstehen, wie Lightning Network+ funktioniert:




- Ein Knotenbetreiber namens "A" veröffentlicht eine Ankündigung, in der er erklärt, dass er mit zwei anderen Personen einen 1-Millionen-sats-Kanal eröffnen möchte;
- Die Anzeige bleibt aktiv, bis weitere Teilnehmer hinzugefügt werden;
- Später schließen sich zwei Betreiber, "B" und "C", der Ankündigung des Knotens "A" an. Das Dreieck ist nun vollständig, und die Eröffnungsphase kann beginnen.
- Knoten `A` öffnet einen Kanal zu Knoten `B`;
- Knoten "B" öffnet einen Kanal zu Knoten "C";
- Knoten "C" öffnet einen Kanal zu Knoten "A".



Am Ende des Vorgangs verfügt jeder Knoten über 1 Million sats an ausgehender und 1 Million sats an eingehender Liquidität. Dieses System kann auf vier oder fünf Teilnehmer erweitert werden.



Natürlich gibt es keinen technischen Mechanismus, der garantiert, dass ein Teilnehmer den Kanal, zu dessen Einrichtung er sich verpflichtet hat, auch tatsächlich öffnet. Aus diesem Grund hat die Plattform ein Reputationssystem eingerichtet, das auf positiven Bewertungen basiert, wenn die Betreiber ihre Verpflichtungen einhalten. Und im schlimmsten Fall, wenn Sie auf jemanden treffen, der nicht kooperiert, haben Sie kein Geld verloren: Sie haben lediglich eine Gelegenheit für eingehende Liquidität verpasst.



Diese Lösung eignet sich besonders für ein "Verbraucher"-Profil, da sie es Ihnen ermöglicht, kostenlos eingehende Liquidität zu erhalten, während Sie Ihren Knotenpunkt mit anderen kleinen Betreibern verbinden. Für Händler hingegen ist dieser Ansatz in der Regel nicht relevant: Für jeden Sat an eingehender Liquidität muss ein Sat an ausgehender Liquidität blockiert werden, und Ihr großer Bedarf an eingehender Liquidität würde dann zu viel Kapital binden.



Um Lightning Network+ zu nutzen, haben Sie zwei Möglichkeiten: Entweder Sie verwenden die in Umbrel integrierte Anwendung oder Sie nutzen die klassische Website und erstellen ein Konto, indem Sie sich von Ihrem Knoten aus anmelden. Ich empfehle Letzteres, da die integrierte Anwendung nicht den vollen Umfang der verfügbaren Funktionen bietet.



Rufen Sie die Website [Lightning Network +](https://lightningnetwork.plus/) auf und klicken Sie auf die Schaltfläche "Anmelden" oben rechts auf der Benutzeroberfläche.



![Image](assets/fr/061.webp)



Um sich zu authentifizieren, müssen Sie die bereitgestellte Nachricht mit dem privaten Schlüssel Ihres Lightning-Knotens signieren. Mit ThunderHub ist dieser Vorgang sehr einfach. Kopieren Sie zunächst die von LN+ angezeigte Nachricht.



![Image](assets/fr/062.webp)



Gehen Sie in ThunderHub auf die Registerkarte "Tools" und klicken Sie dann auf die Schaltfläche "Signieren" im Abschnitt "Nachrichten".



![Image](assets/fr/063.webp)



Fügen Sie die von LN+ bereitgestellte Authentifizierungsnachricht ein, und klicken Sie auf "Unterschreiben".



![Image](assets/fr/064.webp)



ThunderHub signiert diese Nachricht dann mit dem privaten Schlüssel Ihres Knotens. Kopieren Sie die generated-Signatur.



![Image](assets/fr/065.webp)



Fügen Sie diese Unterschrift in das entsprechende Feld auf der LN+ Website ein und klicken Sie dann auf "Anmelden".



![Image](assets/fr/066.webp)



Sie sind nun mit Ihrem Lightning-Knoten mit LN+ verbunden. Dieser Vorgang ermöglicht es LN+, zu überprüfen, ob Sie der rechtmäßige Eigentümer des Knotens sind, den Sie auf ihrer Plattform beanspruchen.



![Image](assets/fr/067.webp)



Wenn Sie möchten, können Sie Ihr LN+-Profil personalisieren, z. B. durch Hinzufügen einer kurzen Biografie.



Um an Ihrer ersten kreisförmigen Kanalöffnung teilzunehmen, gehen Sie zum Menü "Swaps" am oberen Rand der Benutzeroberfläche. Hier finden Sie alle derzeit verfügbaren Swaps, abhängig von den Eigenschaften Ihres Knotens.



![Image](assets/fr/068.webp)



Um einem bestehenden Swap-Angebot beizutreten, klicken Sie einfach auf das Angebot und registrieren Sie sich. Bei LN+ kann der Ersteller eines Swap-Angebots den Teilnehmern jedoch bestimmte Bedingungen auferlegen, z. B. eine Mindestanzahl von Kanälen oder eine Mindestgesamtkapazität des Knotens. Es ist daher möglich, dass insbesondere in den ersten Tagen nur wenige Angebote für Ihren Knoten verfügbar sind. In meinem Fall waren trotz einiger bereits geöffneter Kanäle keine Angebote für meinen Knotenpunkt verfügbar. Also habe ich einen eigenen Swap eingerichtet, und Sie können dasselbe tun, wenn Sie sich in der gleichen Situation befinden.



Klicken Sie auf "Start Liquidity Swap", und geben Sie dann Ihre Angebotsparameter ein:




- Wählen Sie die Gesamtzahl der Teilnehmer (3, 4 oder 5);
- Geben Sie die Anzahl der zu öffnenden Kanäle an (vergewissern Sie sich, dass Sie mindestens diese Anzahl in Ihrem wallet auf der Kette haben);
- Definieren Sie die offene Zeit des Kanals. Dies ist der Zeitraum, in dem die Teilnehmer vereinbaren, sie nicht zu schließen;
- Auf der rechten Seite können Sie Einschränkungen für die Teilnehmer festlegen: Mindestanzahl der Kanäle, Mindestgesamtkapazität und Art der akzeptierten Verbindung.



Wenn alle Parameter eingestellt sind, klicken Sie auf die Schaltfläche "Liquidity Swap starten".



![Image](assets/fr/069.webp)



Ihr Tauschangebot wurde nun erstellt. Jetzt müssen Sie nur noch darauf warten, dass sich andere Knotenbetreiber anmelden. Wenn Ihre Bedingungen nicht zu restriktiv sind, sollte dies nicht allzu lange dauern. Denken Sie daran, den Status Ihres Swaps in den folgenden Stunden oder Tagen zu überwachen.



![Image](assets/fr/070.webp)



Alle Tauschplätze sind besetzt: Wir gehen nun zur Phase der Kanalöffnung über. Jeder Teilnehmer kann über seine LN+-Schnittstelle sehen, zu welchem Knoten er einen Lightning-Kanal öffnen muss.



![Image](assets/fr/084.webp)



Öffnen Sie auf Ihrer Seite den Kanal unter Verwendung der von LN+ gelieferten Node-ID und unter Beachtung der angegebenen Menge. Wie wir in den vorangegangenen Kapiteln gesehen haben, können Sie dies entweder über ThunderHub, mit einem anderen Lightning-Node-Manager oder direkt über die grundlegende Lightning-Node-Anwendungsschnittstelle tun.



![Image](assets/fr/085.webp)



Sobald die Eröffnung erfolgt ist, erscheint sie in der Rubrik der wartenden Kanäle. In meinem Fall handelt es sich um den Kanal mit dem Knoten "Plebian_fr".



![Image](assets/fr/086.webp)



Sie können dann zum LN+ zurückkehren, um zu bestätigen, dass Sie die Kanalöffnung eingeleitet haben. Klicken Sie einfach auf die Schaltfläche "Kanalöffnung gestartet".



![Image](assets/fr/087.webp)



Wenn alle anderen Teilnehmer ebenfalls den Kanal geöffnet haben, zu dem sie sich verpflichtet haben, denken Sie daran, ihnen eine positive Bewertung zu hinterlassen.



![Image](assets/fr/088.webp)



Im Falle von Schwierigkeiten oder Verzögerungen können Sie sich über den Kommentarbereich am Ende der Seite direkt an Ihre Kollegen wenden.



![Image](assets/fr/089.webp)



Einige Teilnehmer möchten vielleicht von Anfang an ein Gleichgewicht zwischen den Kreisläufen herstellen, indem sie eine Zahlung an sich selbst leisten. Dies gewährleistet eine ausgewogene Verteilung der Barmittel in jedem Kanal. Wenn Sie in einem "Verbraucher"-Profil sind, ist dies nicht unbedingt erforderlich, aber Sie können diesen Ausgleich entweder selbst vornehmen, wenn Sie es wünschen, oder Ihre Kanalgebühren vorübergehend auf Null setzen, um es für den Peer, der dies tun möchte, einfacher zu machen. Manchmal möchte es niemand tun.



![Image](assets/fr/090.webp)




# Entfesseln Sie das Potenzial Ihres Lightning-Knotens


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Anschluss eines mobilen wallet über Tailscale


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



Das war's. Sie haben jetzt einen gut angeschlossenen Lightning-Knoten, der sowohl über eingehende als auch ausgehende Liquidität verfügt. Jetzt können Sie Ihren Lightning-Knoten im echten Leben nutzen. Bis jetzt haben wir immer Schnittstellen direkt auf Umbrel verwendet, entweder die Anwendung "Lightning Node" oder die Schnittstelle "ThunderHub". Diese Tools funktionieren für das Senden und Empfangen von Zahlungen, sind aber eindeutig nicht für alltägliche Lightning-Zahlungen optimiert. Die Schnittstelle ist für die Verwendung auf einem Computer konzipiert, was auf einem Smartphone unpraktisch ist, und erfordert außerdem eine Verbindung mit demselben Netzwerk, um ordnungsgemäß zu funktionieren (obwohl es technisch möglich ist, sich aus der Ferne über Tor zu verbinden).



Was wir als Bitcoiner in der Praxis suchen, ist eine klassische Lightning-wallet-Schnittstelle auf einem Smartphone: die Möglichkeit, Rechnungen per QR-Code zu scannen, und eine einfache Schnittstelle zum Bezahlen und Auszahlen von sats. Genau das werden wir in diesem und im nächsten Kapitel implementieren. Die allgemeine Idee ist, eine mobile Lightning wallet-Anwendung auf Ihrem Smartphone zu haben, die von überall aus genutzt werden kann (nicht nur in Ihrem lokalen Netzwerk), die aber im Hintergrund auf Ihren eigenen Lightning-Knoten zurückgreift, um Zahlungen zu senden und zu empfangen.



### Welche Lösungen gibt es für die Anbindung eines mobilen Kunden?



Heutzutage gibt es mehrere Möglichkeiten, dies zu tun, sowohl in Bezug auf die mobile Anwendung als auch auf die Art der Verbindung zwischen Ihrem Knoten und dieser Anwendung. Die drei wichtigsten Verbindungsarten sind:




- über ***Tor***;
- über VPN ***Tailscale***;
- über ***Nostr Wallet Connect***.



Vor einigen Jahren habe ich eine Verbindung über ***Tor*** hergestellt, aber ich habe schnell damit aufgehört: Die Zahl der Ausfälle und die Verzögerungen bei der Kommunikation waren viel zu groß. In der Theorie funktioniert es, aber in der Praxis war die Benutzererfahrung katastrophal. Ich würde daher von diesem Ansatz abraten.



Die Alternative, die ich dann gewählt habe, war die Verwendung eines ***Tailscale*** VPN, um die Kommunikation zwischen der mobilen Anwendung und dem Knoten sicherzustellen. Diese Lösung funktioniert sehr gut: Selbst in Mobilfunknetzen mit geringem Durchsatz werden meine Zahlungen immer problemlos abgewickelt. Diese Methode werde ich in diesem Kapitel zuerst mit der Zeus-Anwendung vorstellen.



Im nächsten Kapitel werden wir uns eine andere, neuere Lösung ansehen, die ebenfalls sehr gut funktioniert: ***Nostr Wallet Connect***. Dieses Mal werden wir die Alby Go-Anwendung verwenden, um Ihnen eine Alternative vorzustellen, obwohl Zeus auch mit NWC kompatibel ist, wenn Sie dies wünschen.



### Installieren und Konfigurieren des Tailscale



Für diese erste Methode benötigen wir Tailscale. Dabei handelt es sich um eine VPN-Lösung auf der Grundlage von WireGuard, die es Ihnen ermöglicht, über das Internet verteilte Geräte sicher zu verbinden und dabei automatisch Verschlüsselung, Authentifizierung und NAT-Traversal zu verwalten. Einfach ausgedrückt, ist es so, als wären alle Ihre Geräte mit demselben LAN wie Ihr Router verbunden, obwohl sie sich überall im Internet befinden könnten.



Um es zu benutzen, müssen Sie zunächst ein Konto erstellen. Rufen Sie die Tailscale-Website auf und klicken Sie auf die Schaltfläche "Get Started" (Starten).



![Image](assets/fr/071.webp)



Wählen Sie dann einen Identitätsanbieter für Ihr Tailscale-Konto. Ich persönlich habe mich mit einem meiner GitHub-Konten angemeldet.



![Image](assets/fr/072.webp)



Sobald Sie sich angemeldet haben, werden Ihnen einige Fragen zu Ihrer Nutzung gestellt. Beantworten Sie diese kurz, um fortzufahren.



![Image](assets/fr/073.webp)



Tailscale bietet dann an, einen Client auf Ihrem Rechner zu installieren. Daran sind wir im Moment nicht interessiert: Gehen Sie direkt zu Umbrel und installieren Sie die Tailscale-Anwendung aus dem App Store.



![Image](assets/fr/074.webp)



Wenn sich die Anwendung öffnet, klicken Sie auf "Anmelden" und folgen dann dem Authentifizierungsprozess, wobei Sie die gleiche Methode wie bei der Erstellung Ihres Kontos verwenden.



![Image](assets/fr/075.webp)



Klicken Sie zur Bestätigung auf "Verbinden". Ihr Umbrel ist nun mit Ihrem VPN-Netzwerk verbunden.



![Image](assets/fr/076.webp)



Laden Sie dann die Tailscale-Anwendung auf Ihr Smartphone herunter und melden Sie sich mit demselben Konto an. Bitte beachten Sie: Auf Android ist es nicht möglich, zwei VPNs gleichzeitig zu verwenden. Damit Tailscale funktioniert, müssen Sie alle anderen aktiven VPNs deaktivieren. Außerdem müssen Sie jedes Mal, wenn Sie Ihren Lightning-Knoten über Zeus verwenden möchten, das Tailscale-VPN aktivieren, da die Verbindung sonst nicht hergestellt werden kann.



![Image](assets/fr/077.webp)



Am Tailscale-Standort können Sie nun, da mindestens zwei Clients angeschlossen sind, auf die Verwaltungskonsole mit einer Liste aller mit dem Netzwerk verbundenen Geräte und deren Tailscale-IP-Adressen zugreifen.



![Image](assets/fr/078.webp)



### Zeus verbinden



Installieren Sie die Zeus-Anwendung auf Ihrem Telefon. Wenn sie sich öffnet, wählen Sie "Erweiterte Einstellungen" und dann "wallet erstellen oder verbinden".



![Image](assets/fr/079.webp)



Wählen Sie im Abschnitt "Wallet-Schnittstelle" die Option "LND (REST)". Geben Sie dann die Tailscale-Adresse Ihres Umbrel ein, die Sie über Ihr Tailscale-Dashboard oder direkt in der Tailscale-Anwendung auf dem Umbrel finden können. Für den Port geben Sie "8080" ein.



![Image](assets/fr/080.webp)



Zeus bittet Sie dann, einen "Macaroon" anzugeben. Dabei handelt es sich um eine Berechtigung token, mit der Sie genau festlegen können, welche Rechte einer Anwendung (in diesem Fall Zeus) für die Interaktion mit Ihrem Lightning-Knoten gewährt werden. Es ist möglich, generate einen Macaroon aus ThunderHub, im Menü "Tools", Untermenü "Bäckerei", zu erstellen, aber für diesen Zweck ist es am einfachsten, ihn direkt aus der Anwendung "Lightning Node" abzurufen.



Klicken Sie auf die drei kleinen Punkte oben rechts auf der Oberfläche, dann auf "Wallet verbinden". Wählen Sie "REST (Lokales Netzwerk)". Sie können dann einen Makaron mit den entsprechenden Rechten kopieren.



![Image](assets/fr/081.webp)



Fügen Sie sie in das entsprechende Feld in Zeus ein und klicken Sie dann auf die Schaltfläche "WALLET CONFIG SPEICHERN".



![Image](assets/fr/082.webp)



Sie können jetzt über die Zeus-App auf Ihren Lightning-Knoten zugreifen. Das bedeutet, dass Sie generate-Rechnungen direkt auf Ihrem Lightning-Knoten von Ihrem Smartphone aus empfangen und auch Lightning-Rechnungen bezahlen können, wo immer Sie sind.



![Image](assets/fr/083.webp)



Tipp: Tailscale ist nicht darauf beschränkt, Ihren Lightning-Knoten aus der Ferne zu verwenden. Es ermöglicht Ihnen den Zugriff auf alle Tools Ihres Umbrel von anderer Software aus, sogar aus der Ferne. Du kannst zum Beispiel die Tailscale IP-Adresse deines Umbrel verwenden, um deinen Bitcoin Knoten (über Electrs oder Fulcrum) mit Sparrow Wallet zu verbinden, ohne durch Tor zu gehen. Auch hier wird die Langsamkeit von Tor vermieden. Installiere einfach den Tailscale Client auf deinem Computer und verbinde ihn mit deinem Netzwerk.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

Im nächsten Kapitel werden wir uns eine andere, ebenso effektive Möglichkeit ansehen, einen mobilen Client mit Ihrem Lightning-Knoten zu verbinden: Nostr Wallet Connect. Wir werden eine andere Anwendung als Zeus verwenden (obwohl Zeus auch mit NWC kompatibel ist), nämlich Alby Go.



## Anschluss eines mobilen wallet über NWC


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Wenn Sie von der Tailscale-Verbindung nicht überzeugt sind oder wenn Ihnen die Verwaltung eines dualen VPNs zu mühsam erscheint, schlägt dieses Kapitel eine andere Möglichkeit vor, einen entfernten mobilen Client zu verwenden, um sats über Ihren Lightning-Knoten zu bezahlen und zu empfangen: ***Nostr Wallet Connect***.



Für dieses Beispiel verwenden wir die mobile Anwendung Alby Go, die sehr gut gestaltet und besonders leicht zu erlernen ist. Sie können aber auch Zeus oder jede andere NWC-kompatible mobile Anwendung verwenden. Eine Liste kompatibler Anwendungen finden Sie auf [dem `awesome-nwc` GitHub-Repository](https://github.com/getAlby/awesome-nwc).



### Wie funktioniert Nostr Wallet Connect?



Nostr Wallet Connect ist ein standardisiertes Protokoll, das es einer Anwendung oder Website ermöglicht, Aktionen auf einem entfernten Lightning-Knoten auszulösen, ohne eine direkte Netzwerkverbindung zu diesem Knoten herzustellen (kein API LND ausgesetzt, kein VPN, kein `.onion`-Dienst...). NWC definiert, wie eine Anwendung eine Absicht formuliert (z.B. `pay_intece`) und das Ergebnis erhält.



Es funktioniert ganz einfach. Sie initialisieren eine Sitzung durch Scannen eines QR-Codes oder über einen Deeplink `nostr+walletconnect:`. Dieser String enthält die Sitzungsparameter und ein Autorisierungsgeheimnis. Wenn die Anwendung dann bezahlen will, serialisiert sie die Anfrage, verschlüsselt sie und veröffentlicht sie als Ereignis auf einem Nostr-Relay. Der Knoten liest das Ereignis auf dem Relais, entschlüsselt es, überprüft, ob der Autor für diese Sitzung autorisiert ist, führt die Zahlung aus und gibt dann eine verschlüsselte Antwort zurück (Erfolg mit Vorabbild oder Fehler). Das Relais fungiert nur als Transportvermittler: Es kann den Inhalt nicht lesen, aber es kann den Zeitpunkt und die Häufigkeit der Anfragen beobachten.



Im Vergleich zu einer Verbindung über Tailscale oder Tor besteht der Hauptvorteil von NWC darin, dass Ihr Knoten nicht direkt von außen erreichbar ist. Dies vereinfacht die mobile Nutzung erheblich: Ihr Knoten muss keine eingehenden Verbindungen annehmen, er muss nur in der Lage sein, mit einem Relais zu kommunizieren. Andererseits führen Sie eine funktionale Abhängigkeit von Nostr-Relais ein: Wenn sie nicht verfügbar sind, verschlechtert sich das Erlebnis. Auch wenn die Nachrichten verschlüsselt sind, kann das Relais ein gewisses Maß an Aktivitätsmetadaten beobachten.



Der Unterschied in den Sicherheitsmodellen ist ebenfalls wichtig. Mit Tailscale oder Tor erhältst du direkten Zugang zu deinem Knoten (über API oder LND), der durch hochsensible Geheimnisse geschützt ist. Das ist mächtig, weil man alles verwalten kann, aber es ist auch eine Angriffsfläche auf einer niedrigeren Ebene. Mit NWC ist der Zugang eher anwendungsbezogen: Du delegierst eine Sitzung token, die nur bestimmte Aktionen autorisiert.



### Installieren Sie Alby Hub auf Ihrem Lightning-Knoten



Früher gab es im Umbrel App Store eine Anwendung, die speziell für NWC-Verbindungen gedacht war, aber leider ist diese nicht mehr verfügbar. Sie müssen nun Alby Hub verwenden, um diese Art von Verbindung herzustellen. Installieren Sie dazu zunächst die Alby Hub-Anwendung direkt aus dem Store.



![Image](assets/fr/091.webp)



Überspringen Sie beim Öffnen die Einführungsbildschirme und klicken Sie dann auf die Schaltfläche `Get Started (LND)`. Es ist wichtig, darauf zu achten, dass in Klammern `LND` und nicht `LDK` steht. Wenn "LND" angezeigt wird, bedeutet dies, dass Alby Hub Ihren vorhandenen Lightning-Knoten korrekt erkannt hat und sich selbst als Schnittstelle für ihn konfiguriert. Wird hingegen `LDK` angezeigt, bedeutet dies, dass Alby Hub Ihren Knoten nicht erkannt hat und im Begriff ist, einen neuen Knoten zu erstellen, was hier nicht das Ziel ist.



![Image](assets/fr/092.webp)



Sie werden dann aufgefordert, ein Alby-Konto einzurichten. Für die auf den NWC beschränkte Nutzung ist dies nicht erforderlich, aber Sie können dies tun, wenn Sie die spezifischen Dienste von Alby in Anspruch nehmen möchten. Wenn nicht, klicken Sie auf `Vielleicht später`, um fortzufahren.



![Image](assets/fr/093.webp)



Wählen Sie dann ein sicheres, eindeutiges Passwort. Damit wird der Zugang zu Alby Hub auf Ihrem Knoten geschützt. Denken Sie daran, es in Ihrem Passwort-Manager zu speichern.



![Image](assets/fr/094.webp)



Dies bringt Sie zur Alby Hub-Schnittstelle. Sie brauchen nicht den gesamten Konfigurationsprozess zu durchlaufen, es sei denn, Sie wollen es als Hauptmanager Ihres Lightning-Knotens verwenden. Wie wir bereits gesehen haben, kann Alby Hub tatsächlich die Verwendung von ThunderHub für die Verwaltung Ihres Knotens ersetzen. Wenn Sie mehr über die Optionen von Alby Hub erfahren möchten, schauen Sie sich unser spezielles Tutorial an:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Gehen Sie zum Menü `Verbindungen`.



![Image](assets/fr/095.webp)



Hier sehen Sie alle Anwendungen, die sich über NWC mit Ihrem Lightning-Knoten verbinden können. Dazu gehört Zeus, das bereits im vorherigen Kapitel erwähnt wurde. Hier werden wir Alby Go verwenden. Klicken Sie auf Alby Go und dann auf die Schaltfläche "Mit Alby Go verbinden", um den Verbindungsvorgang zu starten.



![Image](assets/fr/096.webp)



### Installieren und Anschließen des Alby Go



Installieren Sie auf Ihrem Smartphone die Anwendung Alby Go:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



In Alby Hub konfigurieren Sie die Rechte, die Sie der Anwendung Alby Go auf Ihrem Lightning-Knoten gewähren möchten. Sie können z. B. Ausgabenlimits pro Zeitraum oder ein Ablaufdatum für den NWC-Link festlegen oder die vollständige Kontrolle überlassen. Sobald Sie die Parameter festgelegt haben, klicken Sie auf die Schaltfläche "Weiter".



![Image](assets/fr/097.webp)



Alby Hub sendet dann einen QR-Code an generate, um die NWC-Verbindung zwischen Ihrem Lightning-Knoten und Alby Go herzustellen.



![Image](assets/fr/098.webp)



Klicken Sie in der Anwendung Alby Go beim ersten Öffnen auf "Wallet verbinden" und scannen Sie dann den vom Alby Hub bereitgestellten QR-Code.



![Image](assets/fr/099.webp)



Wählen Sie einen Namen, um dieses wallet zu identifizieren. Sie haben jetzt Fernzugriff auf Ihren Lightning-Knoten über Alby Go. Sie können generate Rechnungen an sats auf Ihrem Knoten empfangen, oder Lightning-Rechnungen direkt mit ihm einstellen.



![Image](assets/fr/100.webp)



Ich habe zum Beispiel 1543 sats von der Schnittstelle Alby Go gesendet.



![Image](assets/fr/101.webp)



Wenn ich die Basisschnittstelle meines Lightning-Knotens auf Umbrel aufrufe, kann ich sehen, dass diese Zahlung tatsächlich von meinem Knoten getätigt wurde.



![Image](assets/fr/102.webp)



Jetzt wissen Sie, wie Sie Ihren Lightning-Knoten von überall aus nutzen können.



## Lang anhaltende Autonomie mit Lightning


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Wir sind nun am Ende dieses LNP202-Praxiskurses angelangt. Sie verfügen nun über die Grundlagen, die Sie benötigen, um Lightning Network souverän zu nutzen: Sie verstehen die wirkliche Rolle eines Knotens, die Kompromisse verschiedener Ansätze und Sie haben eine LND-Instanz auf Umbrel mit einer konsistenten Sicherungs- und Schutzstrategie eingerichtet. Sie haben auch Ihre ersten Kanäle eröffnet und gelernt, wie man Liquidität verwaltet, um Ihre Zahlungen täglich zuverlässig zu machen.



Aus betrieblicher Sicht sollte Ihr Knoten jetzt in einen Wartungsrhythmus übergehen. Das Wichtigste ist, ihn zu überwachen (Betriebszeit, Synchronisierung, Channel-Status, Zahlungsausfälle usw.), die von Umbrel angebotenen Updates anzuwenden, wenn stabile Versionen verfügbar sind, und regelmäßig zu überprüfen, ob Ihre Backups und die Watchtower-Konfiguration noch aktiv sind.



Bei den Kanälen sollten Sie pragmatisch vorgehen: Behalten Sie die Kanäle, die für Sie nützlich sind, schließen Sie diejenigen, die dauerhaft inaktiv sind oder mit instabilen Partnern verbunden sind, und schichten Sie Ihr Kapital allmählich in eine robustere Topologie um.



**Einer der häufigsten Fehler in dieser Phase ist die Zuweisung von zu viel Kapital für Ihren Lightning-Knoten. Bedenken Sie, dass Ihr Lightning-Knoten weit weniger sicher ist als ein Hardware-wallet und dass die Verfügbarkeit der für Ihre Kanäle bereitgestellten Mittel von Sicherungsmechanismen abhängt, die nach wie vor unvollkommen sind. Es ist daher sehr wichtig, dass Sie sich auf vernünftige Beträge beschränken, deren Verlust Sie sich im Falle eines Problems leisten können, und dass Sie den Großteil Ihres sats immer auf einem Onchain-Hardware-wallet halten.



Was die Tools betrifft, empfehle ich Ihnen, neugierig zu bleiben und auf neue Entwicklungen zu achten. In dieser Schulung haben wir mehrere von ihnen kennengelernt, sei es für die Verwaltung Ihres Knotens, seine Konnektivität oder die Fernnutzung für Zahlungen. Lightning ist jedoch ein besonders dynamischer Bereich. Jedes Jahr tauchen neue und relevante Tools auf, und viele neue Anwendungen erscheinen auch auf Umbrel. Wenn Sie sich über diese neuen Entwicklungen auf dem Laufenden halten, können Sie vielleicht noch leistungsfähigere oder praktischere Lösungen entdecken als die in diesem Kurs vorgestellten.



Was die Ausbildung anbelangt, so empfehle ich Ihnen dringend, den Theoriekurs LNP 201 von Fanis Michalakis zu besuchen, der sich mit der Bedienung des Lightning Network befasst. Er wird Ihnen helfen, die in diesem LNP202-Kurs durchgeführten Manipulationen besser zu verstehen, und Ihnen mehr Sicherheit bei der täglichen Verwaltung Ihres Knotens geben.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

In einer anderen Richtung, aber genauso wichtig für Ihre Bitcoin-Reise, empfehle ich auch Ludovic Lars' ausgezeichneten Kurs über die Geschichte der Entstehung von Bitcoin.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Aber bevor Sie weitermachen, können Sie eine Bewertung dieses LNP202-Kurses schreiben und natürlich das Diplom ablegen, um zu bestätigen, dass Sie den gesamten Inhalt verstanden haben.



# Letzter Teil


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Rezensionen und Bewertungen


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Abschlussprüfung


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Schlussfolgerung


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>