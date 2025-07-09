---
name: Bitcoin Entwicklungsphilosophie
goal: Entwickeln Sie ein tiefes philosophisches Verständnis für die Gestaltungsprinzipien von Bitcoin.
objectives: 

  - Analyse der grundlegenden Kompromisse und Architekturentscheidungen von Bitcoin
  - Lernen Sie, wie Sie vorgeschlagene Änderungen und Neuerungen des Bitcoin-Protokolls bewerten können
  - Synthese von über einem Jahrzehnt Bitcoin-Entwicklungsgeschichte und Debatten in der Gemeinschaft
  - Anwendung eines Rahmens für kritisches Denken bei der Bewertung neuer BIPs


---

# Tiefer Einblick in die Philosophie der Bitcoin-Entwicklung



Die Bitcoin-Entwicklungsphilosophie ist ein Kurs für Bitcoin-Entwickler, die bereits die Grundlagen von Konzepten und Prozessen wie Proof-of-Work, Blockbildung und den Transaktionslebenszyklus verstehen und ein tieferes Verständnis für die Designkompromisse und die Philosophie von Bitcoin erlangen möchten.

Es soll neuen Entwicklern helfen, die wichtigsten Lehren aus mehr als einem Jahrzehnt der Bitcoin-Entwicklung und der öffentlichen Debatte zu ziehen, und ihnen gleichzeitig einen nützlichen Kontext für die Bewertung neuer Ideen (guter und schlechter!) bieten.


### Was ist zu erwarten?


Wie bereits erwähnt, ist dies ein praktischer Leitfaden für Bitcoin-Entwickler. Bitcoin ist jedoch ein breites und komplexes Thema, und wir können hier unmöglich alle Aspekte behandeln. Wir hoffen, mit diesem Kurs die notwendigen Funktionen zu erörtern, um Ihre Entwicklungstätigkeit in Gang zu bringen und Sie in die Lage zu versetzen, das Thema auf eigene Faust weiter zu erforschen.


Es gibt viele Leute, die sich mit Bitcoin befassen; da einige von ihnen gegensätzliche Meinungen haben, finden Sie hier möglicherweise Ressourcen, die widersprüchliche Ideen zum Ausdruck bringen. Wir versuchen jedoch immer, uns an die Fakten zu halten, wo Meinungen keine Rolle spielen.


### Wer hat das geschrieben?


Dieser Kurs basiert auf dem gleichnamigen Buch, dessen Hauptautor Kalle Rosenbaum ist und an dem Linnéa Rosenbaum als Co-Autorin mitgewirkt hat.

Das Buch wurde von [Chaincode Labs] (https://learning.chaincode.com/) in Auftrag gegeben und finanziert, einem Entwicklungszentrum, das Schulungsprogramme für Entwickler anbietet, die etwas über Bitcoin-Entwicklung lernen wollen.


+++



# Einführung

<partId>58c48e9b-e285-4dc6-8952-6cc5140b1313</partId>


## Überblick über den Kurs

<chapterId>28b7256b-9cb0-463e-a82d-d732be86c98c</chapterId>


Willkommen zu diesem Kurs PHI 301 über die Entwicklungsphilosophie von Bitcoin.


Bitcoin ist mehr als nur eine Kryptowährung, es verkörpert eine philosophische Vision über Dezentralisierung, Privatsphäre, Vertrauenslosigkeit und Widerstandsfähigkeit. Dieser Kurs richtet sich speziell an Entwickler, die bereits mit den technischen Grundlagen von Bitcoin vertraut sind und nun ihr Verständnis für die Prinzipien, die dem Design und der Governance von Bitcoin zugrunde liegen, vertiefen möchten.


Während dieses Kurses werden Sie Klarheit über die wesentlichen Werte und Strategien gewinnen, die die Entwicklung von Bitcoin seit über einem Jahrzehnt geleitet haben. Durch die eingehende Untersuchung dieser Themen werden Sie die kritische Perspektive entwickeln, die Sie benötigen, um künftige Entwicklungen mit Zuversicht zu bewerten und zu ihnen beizutragen.


### Die zentralen Werte von Bitcoin


Was macht Bitcoin einzigartig? Dieser Abschnitt enthüllt die grundlegenden Werte, die dem Design von Bitcoin zugrunde liegen. Sie werden **Dezentralisierung** erforschen, der Eckpfeiler, der sicherstellt, dass keine einzelne Einheit das Netzwerk kontrolliert; **Vertrauenslosigkeit**, der Schlüssel zur Beseitigung der Abhängigkeit von Dritten; **Privatsphäre**, die sowohl für die individuelle Freiheit als auch für die Systemintegrität unerlässlich ist; und **unendliches Supply**, die kodierte Garantie der Knappheit, die die wirtschaftliche Identität von Bitcoin prägt. Die Beherrschung dieser Konzepte wird es Ihnen ermöglichen, die Stärken und Schwächen von Bitcoin vollständig zu erfassen.


### Bitcoin Verwaltung


Das Navigieren in der komplexen Governance-Landschaft von Bitcoin erfordert mehr als nur technisches Fachwissen, sondern auch ein Verständnis des einzigartigen Ansatzes von Bitcoin für Konsens und Entscheidungsfindung. In diesem Abschnitt werden Sie in die Mechanismen und Philosophien hinter kritischen Prozessen wie Protokoll-Upgrades, die Notwendigkeit des kontradiktorischen Denkens, die Stärke der Open-Source-Zusammenarbeit, die ständigen Herausforderungen der Skalierung und die nuancierten Strategien, die erforderlich sind, wenn die Dinge unweigerlich schief gehen, eintauchen. Mit diesem Wissen sind Sie nicht nur in der Lage, sich zu beteiligen, sondern die Zukunft von Bitcoin effektiv und verantwortungsvoll zu gestalten.


Sind Sie bereit, den nächsten Schritt auf Ihrer Bitcoin-Reise zu tun? Lassen Sie uns beginnen!


***N.B.**: Wenn Sie während des Kurses auf unbekannte Begriffe im Zusammenhang mit Bitcoin stoßen, schlagen Sie bitte im [Glossar] (https://planb.network/resources/glossary) nach, um Definitionen zu finden.*




# Bitcoin Zentrale Werte

<partId>2d6c683b-54c8-5465-b2ca-4e96a6828834</partId>


## Dezentralisierung

<chapterId>9397c84b-0038-5d0e-88d5-11767ce8182d</chapterId>




Hier wird analysiert, was Dezentralisierung ist und warum sie für das Funktionieren von Bitcoin unerlässlich ist. Wir unterscheiden zwischen dem

die Dezentralisierung der Miner und die der Full Nodes und diskutieren, was sie für die Zensurresistenz, eine der zentralen Eigenschaften von Bitcoin, leisten.


Die Diskussion verlagert sich dann auf das Verständnis der Neutralität - oder der Erlaubnislosigkeit gegenüber Nutzern, Minern und Entwicklern - die eine notwendige Eigenschaft jedes dezentralen Systems ist. Schließlich gehen wir darauf ein, wie schwierig es sein kann, ein dezentralisiertes System wie Bitcoin zu verstehen, und stellen einige mentale Modelle vor, die Ihnen helfen könnten, es zu verstehen.


Ein System ohne eine zentrale Kontrollstelle wird als *dezentralisiert* bezeichnet. Bitcoin wurde entwickelt, um einen zentralen Kontrollpunkt zu vermeiden, oder genauer gesagt einen *zentralisierten Punkt der Zensur*.


Dezentralisierung ist ein Mittel, um *Zensurresistenz* zu erreichen.


Es gibt zwei wichtige Aspekte der Dezentralisierung in Bitcoin: Dezentralisierung in Miner und Dezentralisierung in Full node.


Miner Dezentralisierung bezieht sich auf die Tatsache, dass die Transaktionsverarbeitung nicht von einer zentralen Instanz durchgeführt oder koordiniert wird. Full node Dezentralisierung bezieht sich auf die Tatsache, dass die Validierung der Blöcke, d. h. der von den Minern ausgegebenen Daten, am Rande des Netzwerks erfolgt, letztlich durch die Nutzer, und nicht durch einige wenige vertrauenswürdige Behörden.


![](assets/decentralization-banner.webp)


### Miner Dezentralisierung



Vor Bitcoin gab es bereits Versuche, digitale Währungen zu schaffen, aber die meisten davon scheiterten an mangelnder Dezentralisierung der Verwaltung und am Widerstand gegen Zensur.


Miner Dezentralisierung in Bitcoin bedeutet, dass die *Bestellung von Transaktionen* nicht von einer einzelnen Einheit oder einer festen Gruppe von Einheiten durchgeführt wird. Sie wird kollektiv von allen Akteuren durchgeführt, die sich daran beteiligen wollen; dieses Kollektiv der Miner ist eine dynamische Gruppe von Nutzern. Jeder kann nach Belieben beitreten oder austreten. Diese Eigenschaft macht Bitcoin zensurresistent.


Wäre Bitcoin zentralisiert, wäre es anfällig für diejenigen, die es zensieren wollen, wie etwa Regierungen. Es würde das gleiche Schicksal erleiden wie frühere Versuche, digitales Geld zu schaffen. In der Einleitung [eines Papiers] (https://www.blockstream.com/sidechains.pdf) mit dem Titel "Enabling Blockchain Innovations with Pegged Sidechains" (Ermöglichung von Blockchain-Innovationen mit verankerten Sidechains) erklären die Autoren, wie frühe Versionen von digitalem Geld nicht für eine gegnerische Umgebung ausgerüstet waren (siehe auch das Kapitel über gegnerisches Denken im nächsten Teil).


David Chaum führte 1983 digitales Bargeld als Forschungsthema ein, und zwar in einer Umgebung mit einem zentralen Server, dem man vertraut, um Double-spending zu verhindern. Um das von dieser zentralen vertrauenswürdigen Partei ausgehende Risiko für die Privatsphäre des Einzelnen zu mindern und die Fungibilität zu erzwingen, führte Chaum die Blindsignatur ein, mit der er ein kryptografisches Mittel zur Verhinderung der Verknüpfung der Signaturen des zentralen Servers (die Münzen darstellen) bereitstellte, während der zentrale Server weiterhin die Möglichkeit hatte, Doppelausgaben zu verhindern.

Das Erfordernis eines zentralen Servers wurde zur Achillesferse des digitalen Bargelds [Gri99]. Es ist zwar möglich, diese Schwachstelle zu beseitigen, indem die Signatur des zentralen Servers durch eine Schwellensignatur mehrerer Unterzeichner ersetzt wird, doch ist es für die Überprüfbarkeit wichtig, dass die Unterzeichner eindeutig und identifizierbar sind. Das System bleibt dennoch anfällig für Fehler, da jeder Unterzeichner einzeln ausfallen oder zum Ausfall gebracht werden kann.


Es wurde deutlich, dass die Verwendung eines zentralen Servers für die Bestellung von Transaktionen aufgrund des hohen Zensurrisikos keine praktikable Option ist. Selbst wenn man den zentralen Server durch einen Zusammenschluss einer festen Anzahl von n Servern ersetzen würde, von denen mindestens m einer Bestellung zustimmen müssen, gäbe es immer noch Schwierigkeiten. Das Problem würde sich in der Tat dahin verlagern, dass sich die Nutzer auf diese n Server einigen müssten und auch darauf, wie bösartige Server durch gute ersetzt werden könnten, ohne sich auf eine zentrale Behörde zu verlassen.


Lassen Sie uns darüber nachdenken, was passieren könnte, wenn Bitcoin zensierbar wäre. Der Zensor könnte die Nutzer dazu zwingen, sich zu identifizieren, zu erklären, woher ihr Geld kommt oder was sie damit kaufen, bevor sie ihre Transaktionen in das Blockchain einspeisen.


Der fehlende Widerstand gegen die Zensur würde es dem Zensor außerdem ermöglichen, die Benutzer zu zwingen, neue Systemregeln zu übernehmen. Zum Beispiel könnten sie eine Änderung durchsetzen, die es ihnen erlaubt, das Geld Supply aufzublähen und sich dadurch zu bereichern. In einem solchen Fall hätte ein Benutzer, der Blöcke verifiziert, drei Möglichkeiten, mit den neuen Regeln umzugehen:



- Annehmen: Akzeptieren Sie die Änderungen und übernehmen Sie sie in ihre Full node.
- Ablehnen: Verweigern Sie die Annahme der Änderungen; dies führt dazu, dass der Benutzer ein System hat, das keine Transaktionen mehr verarbeitet, da die Sperren des Zensors nun vom Full node des Benutzers als ungültig betrachtet werden.
- Umzug: Ernennung eines neuen zentralen Kontrollpunkts; alle Nutzer müssen herausfinden, wie sie sich koordinieren und sich dann auf den neuen zentralen Kontrollpunkt einigen können.


Wenn sie Erfolg haben, werden die gleichen Probleme höchstwahrscheinlich irgendwann in der Zukunft wieder auftauchen, wenn man bedenkt, dass das System genauso zensierbar geblieben ist wie zuvor.


Keine dieser Optionen ist für den Nutzer von Vorteil.


Der Widerstand gegen Zensur durch Dezentralisierung ist das, was Bitcoin von anderen Geldsystemen unterscheidet, aber es ist aufgrund des *Double-spending-Problems* nicht leicht zu bewerkstelligen. Dies ist das Problem, dass niemand dieselbe Münze zweimal ausgeben kann, ein Problem, von dem viele Leute dachten, es sei unmöglich, es dezentral zu lösen. Satoshi Nakamoto schreibt in seinem [Bitcoin Whitepaper] (https://planb.network/Bitcoin.pdf) darüber, wie das Double-spending Problem gelöst werden kann:


> In diesem Papier schlagen wir eine Lösung für das Double-spending-Problem vor, bei der ein verteilter Peer-to-Peer Timestamp-Server für den generate-Rechnungsnachweis der chronologischen Reihenfolge von Transaktionen verwendet wird.


Hier verwendet er den seltsam klingenden Ausdruck "verteilter Timestamp-Server von Peer-to-Peer". Das Schlüsselwort ist hier *verteilt*, was in diesem Zusammenhang bedeutet, dass es keinen zentralen Kontrollpunkt gibt. Nakamoto fährt dann fort zu erklären, wie Proof-of-Work die Lösung ist.

Doch niemand erklärt es besser als

[Gregory Maxwell auf Reddit] (https://www.reddit.com/r/Bitcoin/comments/ddddfl/question_on_the_vulnerability_of_bitcoin/f2g9e7b/), wo er auf jemanden antwortet, der vorschlägt, die Hash-Leistung der Miner zu begrenzen, um potenzielle 51%-Angriffe zu vermeiden:


> Ein dezentrales System wie Bitcoin verwendet eine öffentliche Wahl. Aber man kann in einem dezentralen System nicht einfach eine Abstimmung von "Menschen" durchführen, denn das würde eine zentralisierte Partei erfordern, um Menschen zur Stimmabgabe zu ermächtigen. Stattdessen verwendet Bitcoin eine Abstimmung der Rechenleistung, da es möglich ist, die Rechenleistung ohne die Hilfe einer zentralen Stelle zu verifizieren
dritte Partei.


Der Beitrag erklärt, wie das dezentrale Bitcoin-Netzwerk durch den Einsatz von Proof-of-Work eine Einigung über die Transaktionsreihenfolge erzielen kann.


Er schließt mit der Aussage, dass der 51%ige Angriff nicht besonders besorgniserregend ist, verglichen mit den Leuten, die sich nicht um die Dezentralisierungseigenschaften von Bitcoin kümmern oder sie nicht verstehen:


> Ein weitaus größeres Risiko für Bitcoin besteht darin, dass die Öffentlichkeit, die es verwendet, es nicht versteht, sich nicht darum kümmert und die Dezentralisierungseigenschaften nicht schützt, die es gegenüber zentralisierten Alternativen überhaupt erst wertvoll machen.

Die Schlussfolgerung ist eine wichtige. Wenn die Menschen die Dezentralisierung von Bitcoin, die stellvertretend für seine Zensurresistenz steht, nicht schützen, könnte Bitcoin Opfer von zentralisierenden Kräften werden, bis es so zentralisiert ist, dass Zensur eine Sache wird. Dann ist das meiste, wenn nicht sogar alles, von seinem Wert weg. Dies bringt uns zum nächsten Abschnitt über die Dezentralisierung von Full node.


### Full node Dezentralisierung



In den obigen Abschnitten haben wir hauptsächlich über die Dezentralisierung von Miner gesprochen und darüber, wie die Zentralisierung von Minern eine Zensur ermöglichen kann. Aber es gibt auch einen anderen Aspekt der Dezentralisierung, nämlich *Full node Dezentralisierung*.


Die Bedeutung der Dezentralisierung des Full node hängt mit der Vertrauenslosigkeit zusammen. Nehmen wir an, ein Nutzer stellt den Betrieb seines eigenen Full node ein, z. B. weil die Betriebskosten zu stark gestiegen sind. In diesem Fall muss er auf andere Weise mit dem Bitcoin-Netz interagieren, möglicherweise durch die Verwendung von Web-Wallets oder leichtgewichtigen Wallets, was ein gewisses Maß an Vertrauen in die Anbieter dieser Dienste erfordert.


Der Benutzer setzt die Konsensregeln des Netzes nicht mehr direkt durch, sondern vertraut darauf, dass jemand anderes dies tut. Nehmen wir nun an, dass die meisten Benutzer die Durchsetzung des Konsenses an eine vertrauenswürdige Instanz delegieren. In diesem Fall kann das Netzwerk schnell in die Zentralisierung abgleiten, und die Netzwerkregeln können von böswilligen Akteuren geändert werden.


In [a

Bitcoin Magazine article] (https://bitcoinmagazine.com/technical/decentralist-perspective-Bitcoin-might-need-small-blocks-1442090446) interviewt Aaron van Wirdum Bitcoin-Entwickler über ihre Ansichten zur Dezentralisierung und die Risiken, die mit der Erhöhung der maximalen Blockgröße von Bitcoin verbunden sind. Diese Diskussion war ein Hot-Thema während der Ära 2014-2017, als viele Leute über die Erhöhung der Blockgrößengrenze diskutierten, um einen höheren Transaktionsdurchsatz zu ermöglichen.


Ein starkes Argument gegen eine Erhöhung der Blockgröße ist, dass dadurch die Kosten für die Verifizierung steigen. Wenn die Verifizierungskosten steigen, wird dies einige Nutzer dazu bringen, ihre vollen Knoten nicht mehr zu betreiben. Dies wiederum wird dazu führen, dass mehr Menschen das System nicht in einer Trustless Weise nutzen können.


Pieter Wuille wird in dem Artikel zitiert, wo er die Risiken der Zentralisierung von Full node erläutert:


> Wenn viele Unternehmen einen Full node betreiben, bedeutet dies, dass sie alle davon überzeugt werden müssen, einen anderen Regelsatz zu implementieren. Mit anderen Worten: Die Dezentralisierung der Blockvalidierung ist es, die den Konsensregeln ihr Gewicht verleiht.
> Aber wenn die Full node-Zahl sehr niedrig ist, weil zum Beispiel alle dieselben Web-Wallets, Börsen und SPV oder mobilen Wallets verwenden, könnte eine Regulierung Realität werden. Und wenn die Behörden die Konsensregeln regulieren können, bedeutet das, dass sie alles ändern können, was Bitcoin zu Bitcoin macht. Sogar die Grenze von 21 Millionen Bitcoin.

Da haben Sie es. Bitcoin-Nutzer sollten ihre eigenen vollständigen Knoten betreiben, um Regulierungsbehörden und große Unternehmen von dem Versuch abzuhalten, die Konsensregeln zu ändern.


### Neutralität



Bitcoin ist neutral, oder erlaubnisfrei, wie man es gerne nennt. Das bedeutet, dass es dem Bitcoin egal ist, wer Sie sind oder wofür Sie es verwenden.


Bitcoin ist neutral, und das ist auch gut so, denn nur so kann es funktionieren. Wenn es von einer Organisation kontrolliert würde, wäre es nur ein weiterer virtueller Objekttyp und ich hätte keinerlei Interesse daran


Solange Sie sich an die Regeln halten, können Sie es nach Belieben verwenden, ohne jemanden um Erlaubnis zu fragen. Dies schließt *Mining*, *Transaktion* und *Erstellung von Protokollen und Diensten* auf der Grundlage von Bitcoin ein:



- Wenn *Mining* ein genehmigter Prozess wäre, bräuchten wir eine zentrale Behörde, die auswählt, wer schürfen darf. Dies würde höchstwahrscheinlich dazu führen, dass Bergleute legale Verträge unterzeichnen müssten, in denen sie zustimmen würden

transaktionen nach den Launen der zentralen Behörde zu zensieren, was den Zweck von Mining von vornherein zunichte macht.



- Wenn Personen, die in Bitcoin *transagieren*, persönliche Informationen angeben, erklären müssten, wofür ihre Transaktionen gedacht sind, oder anderweitig nachweisen müssten, dass sie es wert sind, Transaktionen durchzuführen, bräuchten wir auch eine zentrale Stelle, die Benutzer oder Transaktionen genehmigt. Auch dies würde zu Zensur und Ausgrenzung führen.



- Wenn Entwickler um die Erlaubnis bitten müssten, Protokolle *auf Bitcoin aufzubauen*, würden nur die Protokolle entwickelt werden, die vom zentralen Ausschuss für die Erteilung von Entwicklergenehmigungen zugelassen sind. Dies würde aufgrund des Eingreifens der Regierung unweigerlich alle Protokolle, die die Privatsphäre schützen, und alle Versuche zur Verbesserung der Dezentralisierung ausschließen.


Auf allen Ebenen wird der Versuch, Beschränkungen für die Nutzung von Bitcoin aufzuerlegen, Bitcoin so sehr schaden, dass es seinen Wertvorstellungen nicht mehr gerecht wird.


Pieter Wuille https://Bitcoin.stackexchange.com/a/92055/69518[beantwortet eine Frage zu Stack Exchange] über die Beziehung zwischen Blockchain und normalen Datenbanken. Er erklärt, wie die Genehmigungsfreiheit durch die Verwendung von Proof-of-Work in Kombination mit wirtschaftlichen Anreizen erreicht werden kann.


Er schließt ab:


> Die Verwendung von Trustless-Konsensalgorithmen wie PoW bietet etwas, das Ihnen keine andere Konstruktion bietet (erlaubnisfreie Teilnahme, d. h. es gibt keine festgelegte Gruppe von Teilnehmern, die Ihre Änderungen zensieren kann). Die Verwendung von Trustless-Konsensalgorithmen wie PoW bietet etwas, das jedoch mit hohen Kosten verbunden ist, und seine wirtschaftlichen Annahmen machen es so gut wie nur für Systeme nützlich, die ihre eigene Kryptowährung definieren.
> Wahrscheinlich gibt es auf der ganzen Welt nur einen oder ein paar wenige gebrauchte Exemplare davon.

Er erklärt, dass das System, um Genehmigungsfreiheit zu erreichen, höchstwahrscheinlich eine eigene Währung benötigt, wodurch "die Anwendungsfälle auf Kryptowährungen beschränkt werden". Der Grund dafür ist, dass die erlaubnisfreie Teilnahme, oder Mining, wirtschaftliche Anreize erfordert, die in das System selbst eingebaut sind.


### Dezentralisierung begreifen



Ein überzeugender Aspekt von Bitcoin ist, wie Hard zu begreifen ist, dass niemand es kontrolliert. Es gibt keine Ausschüsse oder Führungskräfte in Bitcoin. Gregory Maxwell, wiederum [auf dem Bitcoin subreddit] (https://www.reddit.com/r/Bitcoin/comments/s82t2n/comment/htdte7w/?utm_source=share&utm_medium=web2x&context=3), vergleicht dies auf faszinierende Weise mit der englischen Sprache:


> Vielen Menschen fällt es schwer, autonome Systeme zu verstehen. In ihrem Leben gibt es viele Dinge wie die englische Sprache - aber die Menschen nehmen sie einfach als selbstverständlich hin und betrachten sie nicht einmal als Systeme. Sie stecken in einer zentralisierten Denkweise fest, in der alles, was sie für ein "Ding" halten, eine Autorität hat, die es kontrolliert.
>

> Bitcoin konzentriert sich auf nichts. Verschiedene Personen, die Bitcoin übernommen haben, haben sich aus freien Stücken entschieden, dafür zu werben, und wie sie das tun, ist ihre eigene Sache. Autoritätsfixierte Menschen mögen diese Aktivitäten sehen und glauben, dass es sich um eine Operation der Bitcoin-Behörde handelt, aber eine solche Behörde existiert nicht.


Die Art und Weise, wie Bitcoin durch Dezentralisierung funktioniert, ähnelt der außergewöhnlichen kollektiven Intelligenz, die bei vielen Arten in der Natur zu finden ist. Die Informatikerin Radhika Nagpal spricht in einem [Ted-Talk] (https://www.ted.com/talks/radhika_nagpal_what_intelligent_machines_can_learn_from_a_school_of_fish) über das kollektive Verhalten von Fischschwärmen und wie Wissenschaftler versuchen, es mit Robotern nachzuahmen.


> Zweitens, und das finde ich immer noch am bemerkenswertesten, wissen wir, dass es keine Anführer gibt, die diesen Fischschwarm überwachen. Stattdessen entsteht dieses unglaubliche kollektive Verhalten allein durch die Interaktionen zwischen den einzelnen Fischen.
> Irgendwie gibt es zwischen benachbarten Fischen diese Wechselwirkungen oder Spielregeln, die dafür sorgen, dass alles klappt.

Sie weist darauf hin, dass viele natürliche oder künstliche Systeme ohne Führer funktionieren können und dies auch tun, und dass sie mächtig und widerstandsfähig sind. Jeder Einzelne interagiert nur mit seiner unmittelbaren Umgebung, aber zusammen bilden sie etwas Gewaltiges.


![](assets/fishschool.webp)

*Fischschwärme haben keine Anführer*


Was auch immer Sie über Bitcoin denken, seine dezentrale Natur macht es schwer zu kontrollieren. Bitcoin existiert, und Sie können nichts dagegen tun. Es ist etwas, das man studieren sollte, nicht debattieren.


### Schlussfolgerung zur Dezentralisierung


Wir unterscheiden zwischen Full node Dezentralisierung und Mining Dezentralisierung. Mining Dezentralisierung ist ein Mittel, um Zensurresistenz zu erreichen, während Full node Dezentralisierung dafür sorgt, dass die Konsensregeln des Netzwerks Hard ohne breite Unterstützung unter den Nutzern nicht verändert werden.


Die dezentralisierte Natur von Bitcoin ermöglicht Neutralität gegenüber Entwicklern, Nutzern und Minern. Jeder kann sich beteiligen, ohne um Erlaubnis zu fragen.


Dezentrale Systeme können Hard sein, aber es gibt einige mentale Modelle, die helfen können, zum Beispiel die englische Sprache oder Fischschwärme.


## Vertrauensunwürdigkeit

<chapterId>0506ba61-16a3-543c-95fa-3f3e2dd64121</chapterId>



![](assets/trustlessness-banner.webp)


In diesem Kapitel wird das Konzept der Vertrauenslosigkeit analysiert, was es aus Sicht der Informatik bedeutet und warum Bitcoin Trustless sein muss, um sein Wertversprechen zu behalten.

Dann sprechen wir darüber, was es bedeutet, Bitcoin auf eine Art und Weise zu verwenden, die Trustless entspricht, und welche Art von Garantien Ihnen ein Full node geben kann und welche nicht.

Im letzten Abschnitt befassen wir uns mit der realen Interaktion zwischen Bitcoin und tatsächlicher Software oder Benutzern und der Notwendigkeit, Kompromisse zwischen Bequemlichkeit und Vertrauenswürdigkeit einzugehen, um überhaupt etwas zu erreichen.


Die Leute sagen oft Dinge wie "Bitcoin ist großartig, weil es Trustless ist".


Was versteht man unter Trustless? Pieter Wuille erklärt diesen weit verbreiteten Begriff auf [Stack Exchange] (https://Bitcoin.stackexchange.com/a/45674/69518):


> Das Vertrauen, von dem wir in "Trustless" sprechen, ist ein abstrakter technischer Begriff. Ein verteiltes System wird als Trustless bezeichnet, wenn es keine vertrauenswürdigen Parteien benötigt, um korrekt zu funktionieren.

Kurz gesagt, das Wort *Trustless* bezieht sich auf eine Eigenschaft des Bitcoin-Protokolls, wonach es logischerweise ohne "vertrauenswürdige Parteien" funktionieren kann. Dies unterscheidet sich von dem Vertrauen, das Sie zwangsläufig in die Software oder Hardware setzen müssen, die Sie betreiben. Auf den letztgenannten Aspekt des Vertrauens wird im weiteren Verlauf dieses Kapitels näher eingegangen.


In zentralisierten Systemen verlassen wir uns auf den Ruf eines zentralen Akteurs, um sicherzustellen, dass er sich um die Sicherheit kümmert oder im Falle von Problemen zurückrudert, sowie auf das Rechtssystem, um Verstöße zu sanktionieren. Diese Vertrauensanforderungen sind in pseudonymen dezentralen Systemen problematisch - es gibt keine Möglichkeit des Rückgriffs, so dass es eigentlich kein Vertrauen geben kann. In der Einleitung zu [dem Bitcoin Whitepaper] (https://Bitcoin.org/Bitcoin.pdf) beschreibt Satoshi Nakamoto dieses Problem:


> Der Internethandel stützt sich fast ausschließlich auf Finanzinstitute, die bei der Abwicklung elektronischer Zahlungen als vertrauenswürdige Dritte fungieren.
> Obwohl das System für die meisten Transaktionen gut genug funktioniert, leidet es immer noch unter den inhärenten Schwächen des vertrauensbasierten Modells.  Völlig unumkehrbare Transaktionen sind nicht wirklich möglich, da die Finanzinstitute nicht umhin können, Streitigkeiten zu schlichten. Die Kosten für die Schlichtung erhöhen die Transaktionskosten, begrenzen die praktische Mindestgröße von Transaktionen und verhindern die Möglichkeit, kleine Gelegenheitsgeschäfte zu tätigen.
> Mit der Möglichkeit einer Rückabwicklung wächst das Bedürfnis nach Vertrauen. Die Händler müssen ihren Kunden gegenüber vorsichtig sein und sie um mehr Informationen bitten, als sie eigentlich bräuchten.  Ein gewisser Prozentsatz an Betrug wird als unvermeidlich hingenommen. Diese Kosten und Zahlungsunsicherheiten können durch die Verwendung von physischem Geld vermieden werden, aber es gibt keinen Mechanismus, um Zahlungen über einen Kommunikationskanal ohne eine vertrauenswürdige Partei durchzuführen

Es scheint, dass wir kein dezentrales System haben können, das auf Vertrauen basiert, und deshalb ist Vertrauenslosigkeit in Bitcoin wichtig.


Um Bitcoin auf Trustless-Art zu nutzen, müssen Sie einen vollständig validierenden Bitcoin-Knoten betreiben. Nur dann können Sie überprüfen, ob die Blöcke, die Sie von anderen erhalten, den Konsensregeln entsprechen, z. B. ob der Zeitplan für die Ausgabe von Münzen eingehalten wird und ob keine Doppelausgaben auf dem Blockchain erfolgen. Wenn Sie keinen Full node betreiben, lagern Sie die Verifizierung von Bitcoin-Blöcken an jemand anderen aus und vertrauen darauf, dass dieser Ihnen die Wahrheit sagt, was bedeutet, dass Sie Bitcoin nicht vertrauensvoll nutzen.


David Harding hat [einen Artikel auf der Bitcoin.org-Website] (https://Bitcoin.org/en/Bitcoin-core/features/validation) verfasst, in dem er erklärt, wie der Betrieb eines Full node - oder die vertrauenslose Nutzung von Bitcoin - Ihnen tatsächlich hilft:


> Die Währung Bitcoin funktioniert nur, wenn Menschen Bitcoins in Exchange für andere wertvolle Dinge akzeptieren. Das bedeutet, dass es die Menschen sind, die Bitcoins akzeptieren, die ihnen Wert verleihen und die entscheiden, wie Bitcoin funktionieren soll.
>

> Wenn Sie Bitcoins akzeptieren, sind Sie befugt, die Regeln von Bitcoin durchzusetzen, z. B. die Konfiszierung der Bitcoins einer Person zu verhindern, ohne Zugang zu den privaten Schlüsseln dieser Person zu haben.
>

> Leider lagern viele Nutzer ihre Durchsetzungsmacht aus. Dies lässt die Dezentralisierung von Bitcoin in einem geschwächten Zustand zurück, in dem eine Handvoll Miner sich mit einer Handvoll Banken und kostenlosen Diensten zusammentun kann, um die Regeln von Bitcoin für all jene nicht verifizierenden Nutzer zu ändern, die ihre Macht ausgelagert haben.
>

> Im Gegensatz zu anderen Geldbörsen setzt Bitcoin Core die Regeln durch. Wenn also die Miner und Banken die Regeln für ihre nicht verifizierenden Benutzer ändern, können diese Benutzer keine voll validierten Bitcoin Core Benutzer wie Sie bezahlen.


Er sagt, dass ein Full node Ihnen hilft, jeden Aspekt des Blockchain zu überprüfen, ohne jemand anderem zu vertrauen, um sicherzustellen, dass die Münzen, die Sie von anderen erhalten, echt sind. Das ist großartig, aber es gibt eine wichtige Sache, bei der Ihnen ein Full node nicht helfen kann: Er kann keine Doppelausgaben durch Kettenumschreibungen verhindern:


> Beachten Sie, dass zwar alle Programme - einschließlich Bitcoin Core - anfällig für Kettenumschreibungen sind, Bitcoin jedoch einen Schutzmechanismus bietet: Je mehr Bestätigungen Ihre Transaktionen haben, desto sicherer sind Sie. Es gibt keine bekannte dezentralisierte Verteidigung, die besser ist als diese.

Unabhängig davon, wie fortschrittlich Ihre Software ist, müssen Sie darauf vertrauen, dass die Blöcke mit Ihren Münzen nicht umgeschrieben werden. Wie Harding betont, können Sie jedoch eine Reihe von Bestätigungen abwarten, nach denen Sie die Wahrscheinlichkeit einer Umschreibung der Kette für gering genug halten, um sie zu akzeptieren.


Die Anreize für die Verwendung von Bitcoin auf eine Trustless Art und Weise stehen im Einklang mit dem Bedarf des Systems an Full node Dezentralisierung. Je mehr Menschen ihre eigenen vollständigen Knoten verwenden, desto stärker ist die Dezentralisierung von Full node und damit auch der Schutz von Bitcoin vor böswilligen Änderungen des Protokolls. Wie im Abschnitt über die Dezentralisierung von Full node erläutert, entscheiden sich die Benutzer jedoch leider oft für vertrauenswürdige Dienste, da sie einen unvermeidlichen Kompromiss zwischen Vertrauenslosigkeit und Bequemlichkeit eingehen müssen.


Die Vertrauenslosigkeit von Bitcoin ist aus einer Systemperspektive absolut zwingend erforderlich. Im Jahr 2018 sprach Matt Corallo [über Vertrauenslosigkeit] (https://btctranscripts.com/baltic-honeybadger/2018/trustlessness-scalability-and-directions-in-security-models/) auf der Baltic Honeybadger-Konferenz in Riga.


![video](https://youtu.be/66ZoGUAnY9s?t=4019)


Die Quintessenz dieses Vortrags ist, dass man keine Trustless-Systeme auf einem vertrauenswürdigen System aufbauen kann, aber man kann vertrauenswürdige Systeme - z. B. ein aufsichtsrechtliches Wallet - auf einem Trustless-System aufbauen.



![width=50%](assets/trust.webp)


Ein Trustless Basis Layer ermöglicht verschiedene Kompromisse auf höheren Ebenen


Dieses Sicherheitsmodell ermöglicht es dem Systementwickler, Kompromisse zu schließen

die für sie sinnvoll sind, ohne diese Kompromisse anderen aufzudrängen.


### Nicht vertrauen, überprüfen



Der Bitcoin funktioniert zwar zuverlässig, aber Sie müssen Ihrer Software und Hardware trotzdem bis zu einem gewissen Grad vertrauen. Das liegt daran, dass Ihre Software oder Hardware möglicherweise nicht so programmiert ist, dass sie das tut, was auf der Verpackung angegeben ist. Zum Beispiel:



- Die CPU könnte böswillig so konzipiert sein, dass sie kryptografische Operationen mit privaten Schlüsseln erkennt und die Daten des privaten Schlüssels preisgibt.
- Der Zufallszahlengenerator des Betriebssystems ist möglicherweise nicht so zufällig, wie er behauptet.
- Bitcoin Core könnte einen Code eingeschleust haben, der Ihre privaten Schlüssel an einen bösen Akteur sendet.


Sie müssen also nicht nur einen Full node einsetzen, sondern auch sicherstellen, dass Sie das ausführen, was Sie vorhaben. Reddit-Benutzer brianddk [schrieb einen Artikel] (https://www.reddit.com/r/Bitcoin/comments/smj1ep/bitcoin_v220_and_guix_stronger_defense_against/) über die verschiedenen Vertrauensstufen, die Sie bei der Überprüfung Ihrer Software wählen können. Im Abschnitt "Trusting the builders" spricht er über reproduzierbare Builds:


> Reproduzierbare Builds sind eine Möglichkeit, Software so zu gestalten, dass viele Entwickler aus der Gemeinschaft die Software erstellen und sicherstellen können, dass das endgültige Installationsprogramm identisch ist mit dem, was andere Entwickler erstellen. Bei einem sehr öffentlichen, reproduzierbaren Projekt wie Bitcoin muss keinem einzelnen Entwickler vollständig vertraut werden. Viele Entwickler können alle den Build durchführen und bestätigen, dass sie dieselbe Datei erstellt haben, die der ursprüngliche Ersteller digital signiert hat.

Der Artikel definiert 5 Stufen des Vertrauens: Vertrauen in die Website, die Entwickler, den Compiler, den Kernel und die Hardware.


Um das Thema der reproduzierbaren Builds weiter zu vertiefen, hielt Carl Dong [einen Vortrag über Guix] (https://btctranscripts.com/breaking-Bitcoin/2019/Bitcoin-build-system/), in dem er erklärte, warum es problematisch sein kann, dem Betriebssystem, den Bibliotheken und den Compilern zu vertrauen, und wie man dies mit einem System namens Guix beheben kann, das heute von Bitcoin Core verwendet wird.


> Was können wir also dagegen tun, dass unsere Toolchain eine Reihe von vertrauenswürdigen Binärdateien enthält, die reproduzierbar bösartig sind? Wir müssen mehr als nur reproduzierbar sein. Wir müssen bootstrap-fähig sein. Wir können nicht so viele binäre Tools haben, die wir von externen, von anderen Organisationen kontrollierten Servern herunterladen und ihnen vertrauen müssen.
>

> Wir sollten wissen, wie diese Tools erstellt werden und wie wir sie genau nachbauen können, vorzugsweise aus einer viel kleineren Menge vertrauenswürdiger Binärdateien. Wir müssen die Anzahl der vertrauenswürdigen Binärdateien so weit wie möglich reduzieren und einen leicht überprüfbaren Pfad von diesen Toolchains zu den Tools haben, die wir für die Erstellung von Bitcoin verwenden. So können wir die Überprüfung maximieren und das Vertrauen minimieren.

Dann erklärt er, wie Guix uns erlaubt, nur einer minimalen Binärdatei von 357 Bytes zu vertrauen, die verifiziert und vollständig verstanden werden kann, wenn man weiß, wie man die Anweisungen interpretiert. Das ist ziemlich bemerkenswert: Man verifiziert, dass die 357-Byte-Binärdatei das tut, was sie tun soll, verwendet sie dann, um das vollständige Build-System aus dem Quellcode zu erstellen, und erhält am Ende eine Bitcoin-Core-Binärdatei, die eine exakte Kopie des Builds eines anderen sein sollte.


Es gibt ein Mantra, dem viele Bitcoiner folgen und das vieles von dem oben Gesagten gut wiedergibt:


> Vertrauen Sie nicht, überprüfen Sie.

Dies spielt auf die Phrase "[trust, but verify](https://en.wikipedia.org/wiki/Trust,_but_verify)" an, die der ehemalige US-Präsident Ronald Reagan im Zusammenhang mit der nuklearen Abrüstung verwendete. die [Bitcoiners](https://twitter.com/Truthcoin/status/1491415722123153408?s=20&t=ZyROxZxlBppdRpuuzsiF5w) haben ihn umgedreht, um die Ablehnung von Vertrauen und die Wichtigkeit der Durchführung eines Full node zu betonen.


Es liegt an den Benutzern zu entscheiden, inwieweit sie die von ihnen verwendete Software und die empfangenen Blockchain-Daten überprüfen wollen. Wie bei so vielen anderen Dingen im Bitcoin gibt es einen Kompromiss zwischen Bequemlichkeit und Vertrauenswürdigkeit. Es ist fast immer bequemer, einen verwahrten Wallet zu verwenden, als Bitcoin Core auf der eigenen Hardware laufen zu lassen. Da die Bitcoin-Software jedoch immer ausgereifter wird und die Benutzeroberflächen immer besser werden, sollte sie mit der Zeit immer besser in der Lage sein, Benutzer zu unterstützen, die bereit sind, auf Vertrauenslosigkeit hinzuarbeiten. Da die Benutzer im Laufe der Zeit mehr Wissen erwerben, sollten sie auch in der Lage sein, das Vertrauen allmählich aus der Gleichung zu entfernen.


Einige Benutzer denken kontraproduktiv und überprüfen die meisten Aspekte der von ihnen verwendeten Software. Infolgedessen reduzieren sie den Bedarf an Vertrauen auf das absolute Minimum, da sie nur ihrer Computerhardware und ihrem Betriebssystem vertrauen müssen. Auf diese Weise helfen sie auch Menschen, die ihre Hardware nicht so gründlich überprüfen, indem sie ihre Stimme in der Öffentlichkeit erheben, um vor Problemen zu warnen, die sie finden könnten. Ein gutes Beispiel dafür ist ein [Ereignis aus dem Jahr 2018] (https://bitcoincore.org/en/2018/09/20/notice/), als jemand einen Fehler entdeckte, der es Minern ermöglichte, eine Ausgabe zweimal in derselben Transaktion auszugeben:


> CVE-2018-17144, dessen Behebung am 18. September in den Bitcoin Core-Versionen 0.16.3 und 0.17.0rc4 veröffentlicht wurde, beinhaltet sowohl eine Denial-of-Service-Komponente als auch eine kritische Inflationsschwachstelle. Ursprünglich wurde das Problem mehreren Entwicklern, die an Bitcoin Core arbeiten, sowie Projekten, die andere Kryptowährungen unterstützen, einschließlich ABC und Unlimited, am 17. September als reiner Denial-of-Service-Fehler gemeldet, wir haben jedoch schnell festgestellt, dass es sich auch um eine Inflationsschwachstelle mit derselben Ursache und Behebung handelt.

Hier meldete eine anonyme Person ein Problem, das sich als viel schlimmer herausstellte, als der Berichterstatter dachte. Dies unterstreicht die Tatsache, dass Personen, die den Code überprüfen, oft Sicherheitslücken melden, anstatt sie auszunutzen. Dies ist für diejenigen von Vorteil, die nicht in der Lage sind, alles selbst zu überprüfen.


Die Nutzer sollten sich jedoch nicht darauf verlassen, dass andere sie schützen, sondern sich selbst vergewissern, wann immer und was immer sie können; so bleibt man so souverän wie möglich, und so gedeiht Bitcoin. Je mehr Augen auf die Software gerichtet sind, desto unwahrscheinlicher ist es, dass sich bösartiger Code und Sicherheitslücken einschleichen.


### Schlussfolgerung über Vertrauenslosigkeit



Das Bitcoin-Protokoll ist Trustless, weil es den Benutzern erlaubt, damit zu interagieren, ohne einer dritten Partei zu vertrauen. In der Praxis sind die meisten Menschen jedoch nicht in der Lage, den gesamten Stapel von Software und Hardware, auf dem Bitcoin ausgeführt wird, zu überprüfen. Qualifizierte Personen, die Software oder Hardware überprüfen, können andere, weniger qualifizierte Personen warnen, wenn sie bösartigen Code oder Fehler finden.


Ohne Vertrauenswürdigkeit kann es keine Dezentralisierung geben, denn Vertrauen setzt zwangsläufig eine zentrale Autorität voraus. Man kann ein vertrauenswürdiges System auf einem Trustless-System aufbauen, aber man kann kein Trustless-System auf einem vertrauenswürdigen System aufbauen.


## Datenschutz

<chapterId>1b960afe-0008-589b-b2f4-007d60d264c6</chapterId>



![](assets/privacy-banner.webp)


In diesem Kapitel geht es darum, wie Sie Ihre privaten Finanzdaten für sich behalten können. Es wird erklärt, was Privatsphäre im Zusammenhang mit Bitcoin bedeutet, warum sie wichtig ist und was es bedeutet, wenn man sagt, dass Bitcoin pseudonym ist. Es wird auch untersucht, wie private Daten durchsickern können, sowohl On-Chain als auch off-chain.


Dann wird darauf eingegangen, dass Bitcoins fungibel sein sollten, d. h. gegen andere Bitcoins austauschbar, und wie Fungibilität und Datenschutz Hand in Hand gehen. Schließlich stellt das Kapitel einige Maßnahmen vor, die Sie ergreifen können, um Ihre Privatsphäre und die anderer zu verbessern.


Bitcoin kann als ein pseudonymes System beschrieben werden, bei dem die Benutzer mehrere Pseudonyme in Form von öffentlichen Schlüsseln haben. Auf den ersten Blick sieht dies wie ein ziemlich guter Weg aus, um die Nutzer vor einer Identifizierung zu schützen, aber es ist in der Tat sehr einfach, private Finanzinformationen unbeabsichtigt preiszugeben.


### Was bedeutet Privatsphäre?



Datenschutz kann in verschiedenen Kontexten unterschiedliche Dinge bedeuten. In Bitcoin bedeutet es im Allgemeinen, dass die Nutzer ihre finanziellen Informationen nicht an andere weitergeben müssen, es sei denn, sie tun dies freiwillig.


Es gibt viele Möglichkeiten, wie Sie Ihre privaten Informationen an andere weitergeben können, mit oder ohne es zu wissen. Daten können entweder aus dem öffentlichen Blockchain oder durch andere Mittel durchsickern, zum Beispiel wenn böswillige Akteure Ihre Internetkommunikation abfangen.


### Warum ist der Datenschutz wichtig?


Es mag offensichtlich erscheinen, warum die Privatsphäre in Bitcoin wichtig ist, aber es gibt einige Aspekte, an die man vielleicht nicht sofort denkt. [Im Bitcoin-Talkforum (https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908) führt Gregory Maxwell eine Reihe von guten Gründen an, warum seiner Meinung nach die Privatsphäre wichtig ist. Dazu gehören der freie Markt, die Sicherheit und die Menschenwürde:


> Der Schutz der finanziellen Privatsphäre ist ein wesentliches Kriterium für das effiziente Funktionieren eines freien Marktes: Wenn Sie ein Unternehmen führen, können Sie keine wirksamen Preise festlegen, wenn Ihre Lieferanten und Kunden gegen Ihren Willen alle Ihre Transaktionen einsehen können.
> Sie können nicht effektiv konkurrieren, wenn Ihre Konkurrenz Ihre Verkäufe verfolgt.  Bei Ihren privaten Geschäften geht Ihr Informationsvorsprung verloren, wenn Sie keinen Datenschutz für Ihre Konten haben: Wenn Sie Ihren Vermieter in Bitcoin bezahlen, ohne dass ein ausreichender Datenschutz gewährleistet ist, sieht Ihr Vermieter, wann Sie eine Gehaltserhöhung erhalten haben und kann mehr Miete von Ihnen verlangen.
>

> Finanzielle Privatsphäre ist für die persönliche Sicherheit von entscheidender Bedeutung: Wenn Diebe Ihre Ausgaben, Ihr Einkommen und Ihr Vermögen sehen können, können sie diese Informationen nutzen, um Sie anzusprechen und auszunutzen. Ohne Datenschutz haben böswillige Parteien mehr Möglichkeiten, Ihre Identität zu stehlen, Ihnen große Einkäufe vor der Haustür wegzuschnappen oder sich als Unternehmen auszugeben, mit denen Sie Geschäfte machen... sie können genau sagen, wie viel sie von Ihnen erpressen wollen.
>

> Finanzielle Privatsphäre ist für die Menschenwürde unerlässlich: Niemand möchte, dass die rotzfreche Barista im Café oder die neugierigen Nachbarn Kommentare zu seinem Einkommen oder seinen Ausgabengewohnheiten abgeben. Niemand möchte, dass seine babyverrückten Schwiegereltern ihn fragen, warum er Verhütungsmittel (oder Sexspielzeug) kauft. Ihr Arbeitgeber hat nicht zu wissen, an welche Kirche Sie spenden. Nur in einer vollkommen aufgeklärten, diskriminierungsfreien Welt, in der niemand eine unangemessene Autorität über einen anderen hat, könnten wir unsere Würde bewahren und unsere rechtmäßigen Geschäfte frei und ohne Selbstzensur tätigen, wenn wir keine Privatsphäre haben.

Maxwell geht auch auf die Fungibilität ein, die später in diesem Kapitel erörtert wird, sowie darauf, dass Privatsphäre und Strafverfolgung keine Gegensätze sind.


### Pseudonymität


Wir haben oben erwähnt, dass Bitcoin pseudonym ist und dass die Pseudonyme öffentliche Schlüssel sind. In den Medien hört man oft, dass Bitcoin anonym ist, was nicht korrekt ist. Es gibt einen Unterschied zwischen Anonymität und Pseudonymität.


Andrew Poelstra [erklärt in einem Bitcoin Stack Exchange Beitrag] (https://Bitcoin.stackexchange.com/a/29473/69518), wie Anonymität bei Transaktionen aussehen würde:


> Völlige Anonymität, d. h., wenn Sie Geld ausgeben, gibt es keinen Hinweis darauf, woher es kommt oder wohin es geht, ist theoretisch möglich, wenn Sie die kryptografische Technik der Null-Wissens-Beweise verwenden.

Der Unterschied scheint darin zu bestehen, dass man bei einer pseudonymen Form des Geldes Zahlungen zwischen Pseudonymen zurückverfolgen kann, während dies bei einer anonymen Form des Geldes nicht möglich ist. Da Bitcoin-Zahlungen zwischen Pseudonymen nachvollziehbar sind, handelt es sich nicht um ein anonymes System.


Wir haben auch gesagt, dass die Pseudonyme öffentliche Schlüssel sind, aber eigentlich sind es Adressen, die von öffentlichen Schlüsseln abgeleitet sind. Warum verwenden wir Adressen als Pseudonyme und nicht etwas anderes, z. B. einen beschreibenden Namen wie "watchme1984"? Dies wurde [gut erklärt] (https://Bitcoin.stackexchange.com/a/25175/69518) von Benutzer Tim S., auch auf Bitcoin Stack Exchange:


> Damit die Idee von Bitcoin funktioniert, müssen Sie Münzen haben, die nur vom Besitzer eines bestimmten privaten Schlüssels ausgegeben werden können. Das bedeutet, dass alles, an das Sie senden, in irgendeiner Weise an einen öffentlichen Schlüssel gebunden sein muss.
>

> Die Verwendung beliebiger Pseudonyme (z. B. Benutzernamen) würde bedeuten, dass man das Pseudonym irgendwie mit einem öffentlichen Schlüssel verknüpfen müsste, um die Verschlüsselung mit öffentlichen/privaten Schlüsseln zu ermöglichen. Dies würde die Möglichkeit der sicheren Offline-Erstellung von Adressen/Pseudonymen zunichte machen (z. B. müssten Sie, bevor jemand Geld an den Benutzernamen "tdumidu" senden könnte, im Blockchain bekannt geben, dass "tdumidu" dem öffentlichen Schlüssel "a1c..." gehört, und eine Gebühr erheben, damit andere einen Grund haben, dies bekannt zu geben), die Anonymität verringern (indem Sie dazu ermutigt werden, Pseudonyme wiederzuverwenden) und die Größe des Blockchain unnötig aufblähen. Es würde auch ein falsches Gefühl der Sicherheit erzeugen, dass man an den sendet, für den man sich hält (wenn ich den Namen "Linus Torvalds" nehme, bevor er es tut, dann ist es meiner, und die Leute könnten Geld senden, weil sie denken, sie bezahlen den Schöpfer von Linux, nicht mich).

Durch die Verwendung von Adressen oder öffentlichen Schlüsseln erreichen wir wichtige Ziele, wie z. B. die Beseitigung der Notwendigkeit, ein Pseudonym vorher irgendwie zu registrieren, die Verringerung der Anreize für die Wiederverwendung von Pseudonymen, die Vermeidung der Aufblähung von Blockchain und die Erschwernis, sich für andere Personen auszugeben.


### Blockchain Datenschutz



Der Blockchain-Datenschutz bezieht sich auf die Informationen, die Sie bei Transaktionen auf der Blockchain preisgeben. Er gilt für alle Transaktionen, sowohl für die, die Sie senden, als auch für die, die Sie empfangen.


Satoshi Nakamoto macht sich in Abschnitt 7 seines [Bitcoin Whitepaper] (https://Bitcoin.org/Bitcoin.pdf) Gedanken über On-Chain Privatsphäre:


> Als zusätzliche Firewall sollte für jede Transaktion ein neues Schlüsselpaar verwendet werden, um zu verhindern, dass sie mit einem gemeinsamen Eigentümer verknüpft werden. Ein gewisses Maß an Verknüpfung ist bei Transaktionen mit mehreren Eingängen unvermeidlich, da diese zwangsläufig erkennen lassen, dass ihre Eingänge demselben Eigentümer gehörten. Das Risiko besteht darin, dass, wenn der Eigentümer eines Schlüssels offengelegt wird, die Verknüpfung andere Transaktionen aufdecken könnte, die demselben Eigentümer gehörten.

Das Papier fasst die Hauptprobleme des Blockchain-Datenschutzes zusammen, nämlich Address-Wiederverwendung und Address-Clustering. Ersteres ist selbsterklärend, letzteres bezieht sich auf die Möglichkeit, mit einem gewissen Grad an Sicherheit zu entscheiden, dass eine Reihe verschiedener Adressen demselben Benutzer gehört.


![](assets/address-reuse-clustering.webp)


Typische Lecks in der Privatsphäre beim Blockchain


Chris Belcher [schrieb sehr detailliert](https://en.Bitcoin.it/Privacy#Blockchain_attacks_on_privacy) über die verschiedenen Arten von Lecks in der Privatsphäre, die auf dem Bitcoin Blockchain auftreten können. Wir empfehlen Ihnen, zumindest die ersten paar Unterabschnitte unter "Blockchain-Angriffe auf die Privatsphäre" zu lesen


Das Ergebnis ist, dass der Datenschutz in Bitcoin nicht perfekt ist. Es erfordert einen erheblichen Aufwand, um private Transaktionen durchzuführen. Die meisten Menschen sind nicht bereit, für den Datenschutz so weit zu gehen. Es scheint einen klaren Kompromiss zwischen Privatsphäre und Benutzerfreundlichkeit zu geben.


Ein weiterer wichtiger Aspekt der Privatsphäre ist, dass die Maßnahmen, die Sie zum Schutz Ihrer eigenen Privatsphäre ergreifen, sich auch auf andere Nutzer auswirken. Wenn Sie mit Ihrer eigenen Privatsphäre schlampig umgehen, kann dies auch die Privatsphäre anderer Menschen beeinträchtigen. Gregory Maxwell erklärt dies sehr anschaulich in der gleichen Bitcoin Talk-Diskussion [die wir oben verlinkt haben] (https://bitcointalk.org/index.php?topic=334316.msg3589252#msg3589252), und schließt mit einem Beispiel ab:


> Das funktioniert tatsächlich auch in der Praxis... Ein netter Whitehat-Hacker im IRC spielte mit dem Knacken von Brainwallet herum und stieß auf eine Phrase mit ~250 BTC darin.  Wir konnten den Besitzer allein anhand des Address identifizieren, weil er von einem Bitcoin-Dienst bezahlt wurde, der Adressen wiederverwendet, und er konnte ihn überreden, die Kontaktinformationen des Benutzers preiszugeben. Er bekam den Nutzer tatsächlich ans Telefon, er war schockiert und verwirrt - aber dankbar, dass er seine Münzen nicht los war.  Das war ein glückliches Ende. (Dies ist bei weitem nicht das einzige Beispiel dafür, aber eines der lustigeren).

In diesem Fall ist dank des menschenfreundlichen Hackers alles gut gegangen, aber verlassen Sie sich beim nächsten Mal nicht darauf.


### Nicht-Blockchain-Datenschutz


Das Blockchain ist zwar eine berüchtigte Quelle für Datenlecks, aber es gibt auch viele andere Lecks, die nicht das Blockchain verwenden, einige davon heimtückischer als andere. Diese reichen von Key-Loggern bis zur Analyse des Netzwerkverkehrs. Um sich über einige dieser Methoden zu informieren, lesen Sie bitte noch einmal [Chris Belchers Artikel] (https://en.Bitcoin.it/Privacy#Non-blockchain_attacks_on_privacy), insbesondere den Abschnitt "Non-Blockchain attacks on privacy".


Neben einer Fülle von Angriffen erwähnt Belcher die Möglichkeit, dass jemand Ihre Internetverbindung ausspäht, z. B. Ihr Internetanbieter:


> Wenn der Angreifer sieht, dass eine Transaktion oder ein Block von Ihrem Knoten ausgeht, die bzw. der zuvor nicht eingegeben wurde, kann er mit ziemlicher Sicherheit wissen, dass die Transaktion von Ihnen durchgeführt oder der Block von Ihnen geschürft wurde. Da es sich um Internetverbindungen handelt, kann der Angreifer die IP Address mit den entdeckten Bitcoin-Informationen in Verbindung bringen.

Zu den offensichtlichsten Lecks in der Privatsphäre gehören jedoch die Börsen. Aufgrund von Gesetzen, die in der Regel als KYC (Know Your Customer) und AML (Anti-Money Laundering) bezeichnet werden und in den Ländern gelten, in denen sie tätig sind, müssen Börsen und damit verbundene Unternehmen oft persönliche Daten über ihre Nutzer sammeln und große Datenbanken darüber anlegen, welche Nutzer welche Bitcoins besitzen. Diese Datenbanken sind ideale Honigtöpfe für böse Regierungen und Kriminelle, die immer auf der Suche nach neuen Opfern sind. Es gibt tatsächlich Märkte für diese Art von Daten, auf denen Hacker

daten an den Meistbietenden zu verkaufen.


Erschwerend kommt hinzu, dass die Unternehmen, die diese Datenbanken verwalten, oft nur wenig Erfahrung mit dem Schutz von Finanzdaten haben, denn viele von ihnen sind junge Start-ups, und wir wissen mit Sicherheit, dass es bereits zu mehreren Lecks gekommen ist. Ein paar Beispiele sind

[Das indische Unternehmen MobiQwik] (https://bitcoinmagazine.com/business/probably-the-largest-kyc-data-leak-in-history-demonstrates-the-importance-of-Bitcoin-privacy) und [HubSpot] (https://bitcoinmagazine.com/business/hubspot-security-breach-leaks-Bitcoin-users-data).


Auch hier ist der Schutz der Daten gegen diese Vielzahl von Angriffen Hard, und es ist wahrscheinlich, dass Sie nicht in der Lage sein werden, dies vollständig zu tun. Sie müssen sich für den Kompromiss zwischen Komfort und Datenschutz entscheiden, der für Sie am besten geeignet ist.


### Fungibilität


Fungibilität bedeutet im Zusammenhang mit Währungen, dass eine Münze gegen jede andere Münze der gleichen Währung austauschbar ist. Das ist lustig

das Wort wurde weiter oben in diesem Kapitel kurz angesprochen.


In dem dort besprochenen Artikel stellte Gregory Maxwell [fest] (https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908):


> Finanzielle Privatsphäre ist ein wesentliches Element der Fungibilität in Bitcoin: Wenn man eine Münze sinnvoll von einer anderen unterscheiden kann, dann ist ihre Fungibilität schwach. Wenn unsere Fungibilität in der Praxis zu schwach ist, können wir nicht dezentralisiert sein: Wenn jemand Wichtiges eine Liste gestohlener Münzen ankündigt, von denen er keine Münzen akzeptiert, müssen Sie die Münzen, die Sie akzeptieren, sorgfältig mit dieser Liste vergleichen und diejenigen zurückgeben, die nicht funktionieren.  Jeder muss die von verschiedenen Behörden herausgegebenen schwarzen Listen überprüfen, denn in dieser Welt wollen wir alle nicht mit schlechten Münzen dastehen. Dies erhöht die Reibung und die Transaktionskosten und macht Bitcoin als Geld weniger wertvoll.

Hier spricht er über die Gefahren, die sich aus einem Mangel an Fungibilität ergeben. Nehmen wir an, Sie haben einen UTXO. Die Geschichte dieses UTXO kann normalerweise über mehrere Sprünge zurückverfolgt werden und erstreckt sich auf eine Vielzahl früherer Ausgaben. Wenn einer dieser Ausgänge in illegale, unerwünschte oder verdächtige Aktivitäten verwickelt war, könnten einige potenzielle Empfänger Ihrer Münze diese ablehnen. Wenn Sie davon ausgehen, dass Ihre Zahlungsempfänger Ihre Münzen anhand einer zentralen "Whitelist" oder "Blacklist" überprüfen, werden Sie vielleicht auch die Münzen, die Sie erhalten, überprüfen, um auf der sicheren Seite zu sein. Das Ergebnis ist, dass eine schlechte Fungibilität eine noch schlechtere Fungibilität unterstützt.


Adam Back und Matt Corallo [hielten einen Vortrag über Fungibilität] (https://btctranscripts.com/scalingbitcoin/milan-2016/fungibility-overview/) auf der Scaling Bitcoin in Mailand im Jahr 2016. Sie dachten in dieselbe Richtung:


> Sie brauchen Fungibilität, damit Bitcoin funktioniert. Wenn man Münzen erhält und sie nicht ausgeben kann, dann beginnt man zu zweifeln, ob man sie ausgeben kann. Wenn es Zweifel an den erhaltenen Münzen gibt, dann werden die Leute zu den Taint-Diensten gehen und prüfen, ob diese Münzen gesegnet sind, und dann werden die Leute den Handel verweigern. Dies führt dazu, dass Bitcoin von einem dezentralisierten, erlaubnisfreien System in ein zentralisiertes, erlaubnispflichtiges System umgewandelt wird, bei dem man einen "Schuldschein" von den Anbietern der schwarzen Liste erhält.

Es scheint, dass Privatsphäre und Fungibilität Hand in Hand gehen. Die Fungibilität wird geschwächt, wenn die Privatsphäre schwach ist, da z. B. Münzen von unerwünschten Personen auf eine schwarze Liste gesetzt werden können. Auf die gleiche Weise wird die Privatsphäre geschwächt, wenn die Fungibilität schwach ist: Wenn es eine schwarze Liste gibt, müssen Sie die Anbieter der schwarzen Liste fragen, welche Münzen Sie annehmen wollen, und dabei möglicherweise Ihre IP Address, Ihre E-Mail Address und andere sensible Informationen preisgeben. Diese beiden Merkmale sind so eng miteinander verwoben, dass es Hard ist, über eines von ihnen isoliert zu sprechen.


### Maßnahmen zum Schutz der Privatsphäre



Es wurden verschiedene Techniken entwickelt, um sich vor dem Verlust der Privatsphäre zu schützen. Zu den naheliegendsten gehört, wie bereits von Nakamoto erwähnt, die Verwendung eindeutiger

adressen für jede Transaktion, aber es gibt noch einige andere. Wir werden Ihnen nicht beibringen, wie Sie ein Datenschutz-Ninja werden. Bitcoin Q+A hat jedoch eine [Kurzzusammenfassung von Technologien zur Verbesserung des Datenschutzes] (https://bitcoiner.guide/privacytips/), die in gewisser Weise danach geordnet ist, wie Hard sie zu implementieren ist. Wenn Sie sie lesen, werden Sie feststellen, dass der Bitcoin-Datenschutz oft mit Dingen außerhalb von Bitcoin zu tun hat. Zum Beispiel sollte man nicht mit seinen Bitcoins prahlen und Tor und VPN benutzen.


In dem Beitrag werden auch einige Maßnahmen aufgeführt, die in direktem Zusammenhang mit Bitcoin stehen:


- Full node: Wenn Sie keinen eigenen Full node verwenden, werden Sie viele Informationen über Ihren Wallet an Server im Internet weitergeben. Der Betrieb eines Full node ist ein guter erster Schritt.
- Lightning Network: Es gibt mehrere Protokolle, die auf Bitcoin aufbauen, z. B. Lightning Network und Liquid von Blockstream Sidechain.
- CoinJoin: Eine Möglichkeit für mehrere Personen, ihre Transaktionen zu einer einzigen zusammenzufassen, wodurch eine Kettenanalyse erschwert wird.


In [einem Vortrag] (https://btctranscripts.com/breaking-Bitcoin/2019/breaking-Bitcoin-privacy/) auf der Konferenz Breaking Bitcoin gab Chris Belcher ein interessantes praktisches Beispiel dafür, wie der Datenschutz verbessert wurde:


> Sie waren ein Bitcoin Kasino. Online-Glücksspiel ist in den USA nicht erlaubt. Alle Kunden von Coinbase, die direkt auf Bustabit einzahlten, mussten ihre Konten schließen lassen, weil Coinbase dies überwachte. Bustabit hat ein paar Dinge getan. Sie haben etwas getan, das Wechselgeldvermeidung genannt wird, wo man durchgeht und sieht, ob man eine Transaktion konstruieren kann, die keine Wechselgeldausgabe hat. Dies spart Miner Gebühren und behindert auch die Analyse.
>

> Außerdem importierten sie ihre stark genutzten, wiederverwendeten Einzahlungsadressen in joinmarket. Zu diesem Zeitpunkt wurden die Kunden von coinbase.com nie gesperrt. Es scheint, dass der Überwachungsdienst von Coinbase danach nicht mehr in der Lage war, die Analyse durchzuführen, so dass es möglich ist, diese Algorithmen zu brechen.

Er erwähnte dieses Beispiel unter anderem auch auf der [Datenschutzseite] (https://en.Bitcoin.it/Privacy) des Bitcoin-Wikis.


Es ist zu beachten, dass ein besserer Schutz der Privatsphäre erreicht werden kann, wenn Systeme auf Bitcoin aufgesetzt werden, wie es bei Lightning Network der Fall ist:


![image](assets/privacy.webp)


Schichten über dem Bitcoin können die Privatsphäre verbessern


Im letzten Beitrag haben wir festgestellt, dass das Bedürfnis nach Vertrauen nur mit zusätzlichen Schichten zunehmen kann, aber das scheint bei der Privatsphäre nicht der Fall zu sein, die durch zusätzliche Schichten beliebig verbessert oder verschlechtert werden kann. Warum ist das so? Jeder Layer, der auf Bitcoin aufgesetzt wird, muss, wie im Absatz "Layered Scaling" im zukünftigen Kapitel "Scaling" erläutert, gelegentlich On-Chain-Transaktionen verwenden, sonst wäre er nicht "auf Bitcoin". Schichten, die die Privatsphäre verbessern, versuchen im Allgemeinen, den Basis-Layer so wenig wie möglich zu verwenden, um die Menge der preisgegebenen Informationen zu minimieren.


Die oben genannten Möglichkeiten sind eher technischer Natur, um Ihre Privatsphäre zu verbessern. Aber es gibt noch andere Möglichkeiten. Zu Beginn dieses Kapitels haben wir gesagt, dass Bitcoin ein pseudonymes System ist. Das bedeutet, dass die Benutzer von Bitcoin nicht durch ihren richtigen Namen oder andere persönliche Daten bekannt sind, sondern durch ihre öffentlichen Schlüssel. Ein öffentlicher Schlüssel ist ein Pseudonym für einen Benutzer, und ein Benutzer kann mehrere Pseudonyme haben. In einer idealen Welt ist Ihre persönliche Identität von Ihren Bitcoin-Pseudonymen entkoppelt. Leider lässt diese Entkopplung aufgrund der in diesem Kapitel beschriebenen Probleme mit der Privatsphäre im Laufe der Zeit nach.


Um das Risiko der Offenlegung Ihrer persönlichen Daten zu verringern, sollten Sie sie gar nicht erst herausgeben oder sie an zentralisierte Dienste weitergeben, die große Datenbanken aufbauen, die undicht werden können. Ein Artikel von Bitcoin Q+A [erklärt KYC] (https://bitcoiner.guide/nokyconly/) und die damit verbundenen Gefahren. Er schlägt auch einige Schritte vor, die Sie unternehmen können, um Ihre Situation zu verbessern:


> Zum Glück gibt es einige Möglichkeiten, Bitcoin ohne KYC-Quellen zu kaufen. Dies sind alle P2P (Peer-to-Peer)-Börsen, bei denen Sie direkt mit einer anderen Person und nicht mit einer zentralisierten dritten Partei handeln. Leider verkaufen einige von ihnen neben Bitcoin auch andere Münzen, so dass wir Sie dringend bitten, vorsichtig zu sein.

Der Artikel schlägt vor, Börsen, die KYC/AML verlangen, zu vermeiden und stattdessen privat zu handeln oder dezentrale Börsen wie [bisq] (https://bisq.network/) zu nutzen.


https://planb.network/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04

Ausführlichere Informationen über Gegenmaßnahmen finden Sie in dem bereits erwähnten [Wiki-Artikel zum Datenschutz] (https://en.Bitcoin.it/wiki/Privacy#Methods_for_improving_privacy_.28non-Blockchain.29), beginnend mit "Methods for improving privacy (non-Blockchain)".


### Schlussfolgerung zum Datenschutz



Datenschutz ist sehr wichtig, aber Hard zu erreichen. Es gibt kein Patentrezept für den Datenschutz.


Um einen angemessenen Schutz der Privatsphäre in Bitcoin zu erreichen, müssen Sie aktive Maßnahmen ergreifen, die zum Teil kostspielig und zeitaufwändig sind.


## Endliche Supply

<chapterId>af125ba2-ef98-5905-8895-41a538fe5ea5</chapterId>



![](assets/finitesupply-banner.webp)


Dieses Kapitel befasst sich mit dem Bitcoin Supply-Limit von 21 Millionen BTC, oder wie viel ist es eigentlich? Wir sprechen darüber, wie dieses Limit durchgesetzt wird und was man tun kann, um zu überprüfen, ob es eingehalten wird. Außerdem werfen wir einen Blick in die Kristallkugel und erörtern die Dynamik, die ins Spiel kommen wird, wenn der Block reward von subventionsbasiert auf gebührenbasiert umgestellt wird.


Das bekannte endliche Supply von 21 Millionen BTC wird als eine grundlegende Eigenschaft von Bitcoin angesehen. Aber ist sie wirklich in Stein gemeißelt?


Schauen wir uns zunächst an, was die aktuellen Konsensregeln über Supply von Bitcoin sagen und wie viel davon tatsächlich nutzbar sein wird. Pieter Wuille schrieb einen Artikel darüber [über den Stapel Exchange] (https://Bitcoin.stackexchange.com/a/38998/69518), in dem er zählte, wie viele Bitcoins es geben würde, sobald alle Münzen abgebaut sind:


> Wenn Sie alle diese Zahlen zusammenzählen, erhalten Sie 20999999.9769 BTC.

Aber aus einer Reihe von Gründen - wie frühe Probleme mit Coinbase-Transaktionen, Miner, die versehentlich weniger als erlaubt einfordern, und Verlust von privaten Schlüsseln - wird diese Obergrenze nie erreicht werden. Wuille schlussfolgert:


> Damit verbleiben 20999817.31308491 BTC (wenn man alles bis zum Block 528333 berücksichtigt)

Allerdings sind verschiedene Wallets verloren gegangen oder gestohlen worden, Transaktionen wurden an den falschen Address gesendet, Leute haben vergessen, dass sie Bitcoin besitzen. Die Gesamtsumme dieser Vorfälle kann durchaus in die Millionen gehen. Die Leute haben versucht, die bekannten Verluste zusammenzurechnen [hier] (https://bitcointalk.org/index.php?topic=7253.0).


Dies lässt uns mit: ??? BTC.


Wir können also sicher sein, dass der Bitcoin Supply höchstens 20999817.31308491 BTC sein wird. Alle verlorenen oder nicht nachweislich verbrannten Münzen werden diese Zahl verringern, aber wir wissen nicht, um wie viel. Das Interessante daran ist, dass es keine Rolle spielt, oder besser gesagt, es spielt eine positive Rolle für Bitcoin-Inhaber,

[wie erklärt] (https://bitcointalk.org/index.php?topic=198.msg1647#msg1647) von Satoshi Nakamoto:


> Verlorene Münzen machen die Münzen aller anderen nur etwas mehr wert.  Betrachten Sie es als eine Spende an alle.

Das endliche Supply wird schrumpfen, was zumindest theoretisch zu einer Preisdeflation führen sollte.


Wichtiger als die genaue Anzahl der im Umlauf befindlichen Münzen ist die Art und Weise, wie das Supply-Limit ohne eine zentrale Behörde durchgesetzt wird. Alias chytrik bringt es auf [Stack Exchange] (https://Bitcoin.stackexchange.com/a/106830/69518) gut auf den Punkt:


> Die Antwort ist also, dass man nicht darauf vertrauen muss, dass jemand den Supply nicht erhöht. Man muss nur einen Code ausführen, der überprüft, dass dies nicht der Fall ist.

Selbst wenn einige Vollknoten sich der dunklen Seite zuwenden und beschließen, Blöcke mit höherwertigen Coinbase-Transaktionen zu akzeptieren, werden alle übrigen Vollknoten sie einfach vernachlässigen und ihre Geschäfte wie gewohnt weiterführen. Einige Full Nodes können, absichtlich oder unabsichtlich, bösartige Software einsetzen, doch das Kollektiv wird den Blockchain zuverlässig sichern. Sie können sich also dafür entscheiden, dem System zu vertrauen, ohne jemandem vertrauen zu müssen.


### Blocksubvention und Transaktionsgebühren



Ein Block reward setzt sich aus der Blocksubvention und den Transaktionsgebühren zusammen. Der Block reward muss die Sicherheitskosten des Bitcoin decken. Wir können mit Sicherheit sagen, dass unter den heutigen Bedingungen in Bezug auf die Blocksubvention, die Transaktionsgebühren, den Bitcoin-Preis, die Mempool-Größe, die Hash-Macht, den Grad der Dezentralisierung usw. die Anreize für jeden Spieler, sich an die Regeln zu halten, hoch genug sind, um ein sicheres Geldsystem zu erhalten.


Was passiert, wenn die Blocksubvention gegen Null geht? Der Einfachheit halber gehen wir davon aus, dass sie tatsächlich gleich Null ist. An diesem Punkt werden die Sicherheitskosten des Systems nur noch durch Transaktionsgebühren gedeckt. Was die Zukunft für uns bereithält, wenn dies geschieht, können wir nicht wissen. Die Unsicherheitsfaktoren sind zahlreich und wir müssen uns mit Spekulationen begnügen. Der Beitrag von Paul Sztorc zu diesem Thema [in seinem Truthcoin-Blog] (https://www.truthcoin.info/blog/security-budget/) besteht größtenteils aus Spekulationen, aber er hat zumindest einen soliden Punkt (bitte beachten Sie, dass M2, auf das sich Sztorc bezieht, ein Maß für ein Fiatgeld Supply ist):


> Während beide in denselben "Sicherheitshaushalt" einfließen, sind der Blockzuschuss und die txn-Gebühren völlig unterschiedlich. Sie sind so unterschiedlich wie die "Gesamtgewinne von VISA im Jahr 2017" und der "Gesamtanstieg von M2 im Jahr 2017".

Heute sind es die Inhaber, die für die Sicherheit zahlen (über die Geldinflation). Morgen werden die Geldausgeber an der Reihe sein, diese Last irgendwie zu schultern, wie unten dargestellt.


![image](assets/finitesupply.webp)


Im Laufe der Zeit wird sich die Last der Sicherheitskosten von den Besitzern zu den Ausgebern verlagern


Wenn Transaktionsgebühren die Hauptmotivation für Mining sind, verschieben sich die Anreize. Vor allem, wenn der Mempool eines Miner nicht genügend Transaktionsgebühren enthält, könnte es für diesen Miner profitabler werden, die Geschichte von Bitcoin umzuschreiben, anstatt sie zu erweitern. Bitcoin Optech hat einen speziellen [Abschnitt über dieses Verhalten] (https://bitcoinops.org/en/topics/fee-sniping/), genannt *fee sniping*, geschrieben von David Harding:


> Das "Fee Sniping" ist ein Problem, das auftreten kann, wenn die Subventionierung von Bitcoin weiter abnimmt und die Transaktionsgebühren beginnen, die Blockbelohnungen von Bitcoin zu dominieren. Wenn Transaktionsgebühren alles sind, was zählt, dann hat ein Miner mit `x` Prozent der Hash-Rate eine `x` Prozent Chance auf Mining im nächsten Block, so dass der erwartete Wert von ehrlichem Mining `x` Prozent des [besten feerate set of transactions](https://bitcoinops.org/en/newsletters/2021/06/02/#candidate-set-based-csb-block-template-construction) in ihrem Mempool ist.
>

> Alternativ könnte ein Miner auf unehrliche Weise versuchen, den vorherigen Block plus einen völlig neuen Block zu minen, um die Kette zu verlängern. Dieses Verhalten wird als "fee sniping" bezeichnet, und die Chance des unehrlichen Miner, dabei erfolgreich zu sein, wenn jeder andere Miner ehrlich ist, ist `(x/(1-x))^2`. Auch wenn die Erfolgswahrscheinlichkeit beim Fee Sniping insgesamt geringer ist als beim ehrlichen Mining, könnte der Versuch des unehrlichen Mining die profitablere Wahl sein, wenn für die Transaktionen im vorherigen Block wesentlich höhere Fee Rates gezahlt wurden als für die Transaktionen, die sich derzeit im Mempool befinden - eine kleine Chance auf einen großen Betrag kann mehr wert sein als eine große Chance auf einen kleinen Betrag.

Ein Wermutstropfen für unsere Hoffnungen für die Zukunft ist die Tatsache, dass, wenn Miner anfangen, Gebühren zu erheben, dies andere dazu anregen wird, dasselbe zu tun, so dass noch weniger ehrliche Miner übrig bleiben. Dies könnte die Gesamtsicherheit von Bitcoin stark beeinträchtigen. Harding führt einige mögliche Gegenmaßnahmen auf, wie z. B. die Verwendung von Transaktionszeitsperren, um einzuschränken, wo im Blockchain die Transaktion erscheinen kann.


Wenn also der Konsens über die Endlichkeit von Supply bestehen bleibt, wird die Blocksubvention - dank [BIP42] (https://github.com/Bitcoin/bips/blob/master/bip-0042.mediawiki), das einen sehr langfristigen Inflationsfehler behoben hat - um das Jahr 2140 herum auf Null sinken. Werden die Transaktionsgebühren danach noch ausreichen, um das Netz zu sichern?


Das ist unmöglich zu sagen, aber wir wissen ein paar Dinge:


- Ein Jahrhundert ist aus Sicht von Bitcoin eine *lange* Zeit. Wenn es noch existiert, wird es sich wahrscheinlich enorm weiterentwickelt haben.
- Wenn eine überwältigende wirtschaftliche Mehrheit es für notwendig erachtet, die Regeln zu ändern und beispielsweise eine ständige jährliche Geldwertinflation von 0,1 % oder 1 % einzuführen, wird das Supply von Bitcoin nicht mehr endlich sein.
- Bei einem Null-Block-Zuschuss und einem leeren oder fast leeren Mempool können die Dinge aufgrund von Gebührenerhöhungen wackelig werden.


Da der Übergang zu einem gebührenpflichtigen Block reward so weit in der Zukunft liegt, wäre es vielleicht klug, keine voreiligen Schlüsse zu ziehen und zu versuchen, die potenziellen Probleme zu lösen, solange wir es noch können. Peter Todd ist zum Beispiel der Meinung, dass die Gefahr besteht, dass das Sicherheitsbudget von Bitcoin in Zukunft nicht ausreichen wird, und plädiert daher für eine kleine ständige Inflation in Bitcoin. Er ist jedoch auch der Meinung, dass es keine gute Idee ist, ein solches Thema zum jetzigen Zeitpunkt zu diskutieren, wie [er im Podcast What Bitcoin Did] (https://www.whatbitcoindid.com/podcast/peter-todd-on-the-essence-of-Bitcoin) sagte:


> Aber das ist ein Risiko, das 10 oder 20 Jahre in der Zukunft liegt. Das ist eine sehr lange Zeit. Und wer zum Teufel weiß bis dahin, wie hoch die Risiken sind?

Vielleicht können wir uns Bitcoin als etwas Organisches vorstellen. Stellen Sie sich eine kleine, langsam wachsende Eichenpflanze vor. Stellen Sie sich auch vor, dass Sie noch nie in Ihrem Leben einen ausgewachsenen Baum gesehen haben. Wäre es dann nicht klug, Ihre Kontrollbedürfnisse zu zügeln, anstatt im Voraus alle Regeln dafür aufzustellen, wie sich diese Pflanze entwickeln und wachsen darf?


### Schlussfolgerung zum endlichen Supply



Ob die Bitcoin Supply über 21 Millionen hinauswachsen werden, können wir heute nicht sagen, und das ist wahrscheinlich nicht so schlimm. Es ist wichtig, dafür zu sorgen, dass das Sicherheitsbudget hoch genug bleibt, aber nicht dringend. Lassen Sie uns diese Diskussion in 10-50 Jahren führen, wenn wir mehr wissen. Wenn sie dann noch relevant ist.


# Bitcoin Gouvernanz

<partId>411bf53f-af4b-50f1-b71b-e40fe3ff64b7</partId>


## Aktualisieren von

<chapterId>3ffa84d1-adfa-5fbc-9b13-384ea783fcdd</chapterId>



![](assets/upgrading-banner.webp)


Eine sichere Aufrüstung von Bitcoin kann äußerst schwierig sein. Manche Änderungen brauchen mehrere Jahre, um eingeführt zu werden. In diesem Kapitel lernen wir das gängige Vokabular rund um die Aufrüstung von Bitcoin kennen und untersuchen einige Beispiele für historische Aufrüstungen des Protokolls sowie die Erkenntnisse, die wir daraus gewonnen haben. Schließlich sprechen wir über Kettensplits und die damit verbundenen Risiken und Kosten.


Um sich auf dieses Kapitel einzustimmen, sollten Sie [David Hardings Beitrag über Harmonie und Zwietracht] lesen (https://bitcointalk.org/dec/p1.html):


> Bitcoin Experten sprechen oft von Konsens, dessen Bedeutung abstrakt und Hard schwer zu fassen ist. Aber das Wort Konsens hat sich aus dem lateinischen Wort concentus entwickelt, "ein gemeinsames Singen in Harmonie", also sollten wir nicht von Bitcoin Konsens, sondern von Bitcoin Harmonie sprechen.
>

> Harmonie ist das, was Bitcoin funktionieren lässt. Tausende von vollwertigen Knoten arbeiten unabhängig voneinander, um die Gültigkeit der empfangenen Transaktionen zu überprüfen, wodurch eine harmonische Vereinbarung über den Zustand des Bitcoin Ledger entsteht, ohne dass ein Knotenbetreiber einem anderen vertrauen muss. Es ist vergleichbar mit einem Chor, in dem jedes Mitglied das gleiche Lied zur gleichen Zeit singt, um etwas viel Schöneres zu schaffen, als es jeder von ihnen allein schaffen könnte.
>

> Das Ergebnis der Bitcoin-Harmonie ist ein System, in dem Bitcoins nicht nur vor kleinen Dieben sicher sind (vorausgesetzt, Sie bewahren Ihre Schlüssel sicher auf), sondern auch vor endloser Inflation, massenhafter oder gezielter Konfiszierung oder einfach vor dem bürokratischen Morast, der das herkömmliche Finanzsystem ausmacht.

In diesem Kapitel wird erörtert, wie Bitcoin verbessert werden kann, ohne Zwietracht zu säen. In Harmonie zu bleiben, d. h. den Konsens aufrechtzuerhalten, ist in der Tat eine der größten Herausforderungen bei der Entwicklung von Bitcoin. Es gibt viele Nuancen bei den Aktualisierungsmechanismen, die man am besten versteht, wenn man die tatsächlichen Fälle früherer Aktualisierungen studiert. Aus diesem Grund liegt der Schwerpunkt des Kapitels auf historischen Beispielen, und es beginnt mit einigen nützlichen Vokabeln.


### Vokabeln



Laut Wikipedia bezeichnet [Vorwärtskompatibilität] (https://en.wikipedia.org/wiki/Forward_compatibility) den Zustand, in dem eine alte Software Daten verarbeiten kann, die von neuerer Software erstellt wurden, und dabei die Teile ignoriert, die sie nicht versteht:


Eine Norm unterstützt die Vorwärtskompatibilität, wenn ein Produkt, das mit früheren Versionen übereinstimmt, Eingaben, die für spätere Versionen der Norm entwickelt wurden, "elegant" verarbeiten kann und neue Teile, die es nicht versteht, ignoriert.


Umgekehrt bedeutet [Abwärtskompatibilität] (https://en.wikipedia.org/wiki/Backward_compatibility), dass Daten aus einer alten Software auch in neueren Programmen verwendet werden können. Eine Änderung wird als vollständig kompatibel bezeichnet, wenn sie sowohl vorwärts- als auch rückwärtskompatibel ist.


Eine Änderung der Bitcoin-Konsensregeln wird als *Soft Fork* bezeichnet, wenn sie vollständig kompatibel ist. Dies ist die gebräuchlichste Art, Bitcoin zu aktualisieren, und zwar aus einer Reihe von Gründen, auf die wir im weiteren Verlauf dieses Kapitels eingehen werden. Wenn eine Änderung der Bitcoin-Konsensregeln zwar abwärtskompatibel, aber nicht vorwärtskompatibel ist, wird sie als *Hard Fork* bezeichnet.


Für einen technischen Überblick über Soft-Forks und Hard-Forks lesen Sie bitte [Kapitel 11 von Grokking Bitcoin] (https://rosenbaum.se/book/grokking-Bitcoin-11.html). Dort werden diese Begriffe erklärt und auch die Upgrade-Mechanismen erläutert. Es ist empfehlenswert, wenn auch nicht unbedingt notwendig, sich damit vertraut zu machen, bevor Sie weiter lesen.


### Historische Upgrades



Der Bitcoin ist heute nicht mehr derselbe wie damals, als der Block Genesis geschaffen wurde. Im Laufe der Jahre wurden mehrere Upgrades vorgenommen. Im Jahr 2018 sprach Eric Lombrozo [auf der Breaking-Bitcoin-Konferenz] (https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) über die verschiedenen Upgrading-Mechanismen von Bitcoin und wies darauf hin, wie sehr sie sich im Laufe der Zeit entwickelt haben. Er erklärte sogar, wie Satoshi Nakamoto einst Bitcoin durch einen Hard Fork aufwertete:


> Es gab tatsächlich eine Hard-Fork in Bitcoin, die Satoshi so gemacht hat, dass wir es niemals so machen würden - es ist eine ziemlich schlechte Art, es zu machen. Wenn du dir die Git-Commit-Beschreibung hier ansiehst [[757f076](https://github.com/Bitcoin/Bitcoin/commit/757f0769d8360ea043f469f3a35f6ec204740446)], sagt er etwas über reverted makefile.unix wx-config Version 0.3.6. Das stimmt. Das ist alles, was er sagt. Es gibt keinen Hinweis darauf, dass es überhaupt eine bahnbrechende Änderung gibt. Er hat sie im Grunde darin versteckt. Er hat auch [auf bitcointalk] (https://bitcointalk.org/index.php?topic=626.msg6451#msg6451) gepostet und gesagt, bitte aktualisieren Sie so schnell wie möglich auf 0.3.6. Wir haben einen Implementierungsfehler behoben, durch den es möglich ist, dass gefälschte Transaktionen als akzeptiert angezeigt werden können. Akzeptieren Sie keine Bitcoin-Zahlungen, bis Sie auf 0.3.6 aktualisiert haben. Wenn Sie nicht sofort upgraden können, wäre es am besten, wenn Sie Ihren Bitcoin-Knoten abschalten, bis Sie es tun. Und obendrein, ich weiß nicht, warum er sich dazu entschlossen hat, dies auch noch zu tun, hat er beschlossen, einige Optimierungen in denselben Code einzufügen. Einen Fehler beheben und einige Optimierungen hinzufügen.

Er weist darauf hin, dass dieser Hard Fork absichtlich oder unabsichtlich Möglichkeiten für zukünftige Soft Forks geschaffen hat, nämlich die Skript-Operatoren (Opcodes) OP_NOP1-OP_NOP10. Wir werden diese Codeänderung in cve-2010-5141 genauer untersuchen. Diese Opcodes wurden bisher für zwei Soft-Forks verwendet:


- [BIP65](https://github.com/Bitcoin/bips/blob/master/bip-0065.mediawiki) (OP_CHECKLOCKTIMEVERIFY)
- [BIP113](https://github.com/Bitcoin/bips/blob/master/bip-0112.mediawiki) (OP_SEQUENCEVERIFY).


Lombrozo gibt auch einen Überblick darüber, wie sich die Aufrüstungsmechanismen im Laufe der Jahre, bis 2017, entwickelt haben. Seitdem wurde nur ein weiteres großes Upgrade, Taproot, eingeführt. Der lange und etwas chaotische Prozess, der zu seiner Aktivierung führte, hat uns geholfen, weitere Einblicke in die Aufrüstungsmechanismen von Bitcoin zu gewinnen.


#### SegWit Aufrüstung



Während alle Upgrades, die SegWit vorausgingen, mehr oder weniger schmerzlos waren, war dieses anders. Als der SegWit-Aktivierungscode im Oktober 2016 veröffentlicht wurde, schien es unter den Bitcoin-Nutzern eine überwältigende Unterstützung dafür zu geben, aber aus irgendeinem Grund signalisierten die Miner keine Unterstützung für dieses Upgrade, was die Aktivierung ohne Aussicht auf eine Lösung verzögerte.


Aaron van Wirdum beschreibt diesen gewundenen Weg in seinem Bitcoin Magazinartikel [The Long Road To SegWit] (https://bitcoinmagazine.com/technical/the-long-road-to-SegWit-how-bitcoins-biggest-protocol-upgrade-became-reality). Er beginnt damit, zu erklären, was SegWit ist und wie es in die Debatte über die Blockgröße eingreift. Van Wirdum skizziert dann die Ereignisse, die zu seiner endgültigen Aktivierung führten. Im Mittelpunkt dieses Prozesses stand ein Upgrade-Mechanismus namens *Benutzeraktiviertes Soft Fork*, kurz UASF, der vom Benutzer Shaolinfry vorgeschlagen wurde:


> Shaolinfry schlug eine Alternative vor: ein benutzeraktiviertes Soft Fork (UASF). Anstelle der Hash-Stromaktivierung würde ein nutzeraktiviertes Soft Fork eine "Flaggentagsaktivierung" haben, bei der die Knoten zu einem vorbestimmten Zeitpunkt in der Zukunft mit der Durchsetzung beginnen Solange eine solche UASF von einer wirtschaftlichen Mehrheit durchgesetzt wird, sollte dies eine Mehrheit der Miner dazu zwingen, die Soft Fork zu befolgen (oder zu aktivieren).

Unter anderem zitiert er Shaolinfrys E-Mail an die Bitcoin-dev Mailingliste. Bei dieser Gelegenheit argumentierte Shaolinfry [gegen Miner aktivierte Soft Forks] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-February/013643.html) und listete eine Reihe von Problemen mit ihnen auf:


> Erstens muss man sich darauf verlassen können, dass die Hash-Leistung nach der Aktivierung validiert wird.  Der BIP66 Soft Fork war ein Fall, bei dem 95 % des Hashrate Bereitschaft signalisierten, aber in Wirklichkeit etwa die Hälfte die aktualisierten Regeln nicht validierte und versehentlich auf einen ungültigen Block schürfte.
>

> Zweitens hat die Miner-Signalisierung ein natürliches Vetorecht, das es einem kleinen Prozentsatz von Hashrate ermöglicht, die Knotenaktivierung des Upgrades für alle zu blockieren. Bisher haben Soft-Forks die Vorteile der relativ zentralisierten Mining-Landschaft genutzt, in der es relativ wenige Mining-Pools gibt, die gültige Blöcke bauen; wenn wir uns in Richtung einer stärkeren Dezentralisierung von Hashrate bewegen, ist es wahrscheinlich, dass wir mehr und mehr unter "Upgrade-Trägheit" leiden werden, die die meisten Upgrades verhindern wird.

Shaolinfry machte auch auf eine häufige Fehlinterpretation der Miner-Signalisierung aufmerksam: Die Leute dachten im Allgemeinen, dass es sich dabei um ein Mittel handelte, mit dem Bergleute über Protokoll-Upgrades entscheiden konnten, und nicht um eine Aktion, die bei der Koordinierung von Upgrades half. Aufgrund dieses Missverständnisses fühlten sich die Miner möglicherweise auch verpflichtet, ihre Meinung zu einem bestimmten Soft Fork öffentlich zu verkünden, als ob dies dem Vorschlag Gewicht verleihen würde.


Der UASF-Vorschlag ist, kurz gesagt, ein "Flaggentag", an dem die Nodes beginnen, bestimmte neue Regeln durchzusetzen. Auf diese Weise müssen die Miner keine kollektive Anstrengung unternehmen, um das Upgrade zu koordinieren, sondern *können* die Aktivierung früher als am Flaggentag auslösen, wenn genügend Blöcke ihre Unterstützung signalisieren:


> Mein Vorschlag ist, das Beste aus beiden Welten zu kombinieren. Da ein vom Nutzer aktivierter Soft Fork eine relativ lange Vorlaufzeit vor der Aktivierung benötigt, können wir ihn mit BIP9 kombinieren, um die Option einer schnelleren, mit der Leistung koordinierten Hash-Aktivierung oder einer Aktivierung am Flaggentag zu bieten, je nachdem, was früher eintritt.
> In beiden Fällen können wir die Warnsysteme in BIP9 nutzen. Die Änderung ist relativ einfach: Es wird ein Parameter für die Aktivierungszeit hinzugefügt, der den BIP9-Zustand vor Ablauf der BIP9-Bereitstellungszeitspanne in den Zustand LOCKED_IN überführt.

Diese Idee stieß auf großes Interesse, schien aber keine annähernd einstimmige Unterstützung zu finden, was zu Bedenken hinsichtlich einer möglichen Kettenspaltung führte. Der Artikel von Aaron van Wirdum erklärt, wie dies schließlich dank [BIP91] (https://github.com/Bitcoin/bips/blob/master/bip-0091.mediawiki), verfasst von James Hilliard, gelöst wurde:


> Hilliard schlug eine etwas komplexe, aber clevere Lösung vor, die alles kompatibel machen würde: Getrennte Zeugenaktivierung, wie vom Bitcoin Kernentwicklungsteam vorgeschlagen, das BIP148 UASF und der Aktivierungsmechanismus des New Yorker Abkommens. Sein BIP91 könnte Bitcoin ganz erhalten - zumindest während der Aktivierung von SegWit.

Es gab einige kompliziertere Faktoren (z. B. das so genannte "New Yorker Abkommen"), die bei diesem BIP berücksichtigt werden mussten. Wir empfehlen Ihnen, den Artikel von Van Wirdum vollständig zu lesen, um mehr über die vielen interessanten Details dieser Geschichte zu erfahren.


#### Post-SegWit-Diskussion


Nach dem Einsatz von SegWit kam eine Diskussion über die Einsatzmechanismen auf. Wie Eric Lombrozo in [seinem Vortrag auf der Konferenz Breaking Bitcoin] (https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) und Shaolinfry feststellten, ist ein Miner aktivierter Soft Fork nicht der ideale Upgrade-Mechanismus:


> Irgendwann werden wir dem Bitcoin-Protokoll wahrscheinlich weitere Funktionen hinzufügen wollen. Dies ist eine große philosophische Frage, die wir uns stellen. Machen wir ein UASF für die nächste Version? Wie wäre es mit einem hybriden Ansatz? Miner, das von sich aus aktiviert wurde, ist ausgeschlossen. bip9 werden wir nicht mehr verwenden.

Im Januar 2020 schickte Matt Corallo [eine E-Mail](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2020-January/017547.html) an die Bitcoin-dev-Mailingliste, die eine Diskussion über zukünftige Soft Fork-Bereitstellungsmechanismen in Gang setzte. Er listete fünf Ziele auf, die seiner Meinung nach für ein Upgrade unerlässlich sind. David Harding [fasst sie in einem Bitcoin Optech Newsletter](https://bitcoinops.org/en/newsletters/2020/01/15/#discussion-of-Soft-Fork-activation-mechanisms) wie folgt zusammen:


> Die Möglichkeit des Abbruchs, wenn ein ernsthafter Einwand gegen die vorgeschlagenen Änderungen der Konsensregeln auftaucht. Die Zuweisung einer ausreichenden Zeitspanne nach der Veröffentlichung der aktualisierten Software, um sicherzustellen, dass die meisten Wirtschaftsknoten aufgerüstet werden, um diese Regeln durchzusetzen. Die Erwartung, dass die Hash-Rate des Netzes vor und nach der Änderung sowie während der Übergangsphase in etwa gleich sein wird. Die Erstellung von Blöcken, die nach den neuen Regeln ungültig sind und zu falschen Bestätigungen in nicht aufgerüsteten Knoten und SPV-Clients führen könnten, soll so weit wie möglich verhindert werden. Die Sicherheit, dass die Abbruchmechanismen nicht von Griefern oder Partisanen missbraucht werden können, um ein allgemein gewünschtes Upgrade ohne bekannte Probleme zu verhindern

Was Corallo vorschlägt, ist eine Kombination aus einem Miner aktivierten Soft Fork und einem nutzeraktivierten Soft Fork:


> Eine Aktivierungsmethode, die den richtigen Präzedenzfall schafft und die oben genannten Ziele angemessen berücksichtigt, wäre also eine etwas konkretere Lösung:
>

> 1) eine Standard-BIP-9-Einführung mit einem Zeithorizont von einem Jahr für
aktivierung mit 95% Miner Bereitschaft, +

> 2) falls keine Aktivierung innerhalb eines Jahres erfolgt, eine sechsmonatige
ruhephase, in der die Gemeinschaft analysieren und diskutieren kann

die Gründe für die Nichtaktivierung und, +

> 3) Falls es sinnvoll ist, würde ein einfacher Befehlszeilen-/Bitcoin.conf-Parameter, der seit der ursprünglichen Bereitstellungsversion unterstützt wird, es den Benutzern ermöglichen, sich für eine BIP-8-Bereitstellung mit einem 24-monatigen Zeithorizont für die Aktivierung des Flaggentags zu entscheiden (sowie für eine neue Bitcoin-Kernversion, die das Flag universell aktiviert).
>

> Dies bietet einen sehr langen Zeithorizont für eine stärkere Standardaktivierung und stellt gleichzeitig sicher, dass die Ziele von Nr. 5 erreicht werden, selbst wenn in diesen Fällen der Zeithorizont erheblich verlängert werden muss, um die Ziele von Nr. 3 zu erreichen. Die Entwicklung von Bitcoin ist kein Wettlauf. Wenn es sein muss, stellen wir mit einer Wartezeit von 42 Monaten sicher, dass wir keinen negativen Präzedenzfall schaffen, den wir im weiteren Verlauf der Entwicklung von Bitcoin bedauern werden.

#### Taproot Upgrade - Schnellversuch



Als Taproot im Oktober 2020 einsatzbereit war, d. h. alle technischen Details rund um die Konsensregeln implementiert waren und eine breite Zustimmung in der Gemeinschaft gefunden hatten, begannen die Diskussionen darüber, wie es tatsächlich eingesetzt werden sollte. Diese Diskussionen verliefen bis zu diesem Zeitpunkt ziemlich unauffällig.


Es wurden zahlreiche Vorschläge für Aktivierungsmechanismen gemacht, und David Harding

[zusammengefasst auf dem Bitcoin Wiki] (https://en.Bitcoin.it/wiki/Taproot_activation_proposals). In seinem Artikel erläuterte er einige Eigenschaften von BIP8, an dem zu diesem Zeitpunkt einige Änderungen vorgenommen wurden, um es flexibler zu machen.


> Zum Zeitpunkt der Erstellung dieses Dokuments wurde [BIP8] (https://github.com/Bitcoin/bips/blob/master/bip-0008.mediawiki) auf der Grundlage der im Jahr 2017 gewonnenen Erkenntnisse ausgearbeitet. Eine bemerkenswerte Änderung im Anschluss an die BIPs 9+148 besteht darin, dass die erzwungene Aktivierung nun auf der Blockhöhe und nicht mehr auf der vergangenen mittleren Zeit basiert; eine zweite bemerkenswerte Änderung besteht darin, dass die erzwungene Aktivierung ein boolescher Parameter ist, der ausgewählt wird, wenn die Aktivierungsparameter eines Soft Fork entweder für die Ersteinrichtung festgelegt oder bei einer späteren Einrichtung aktualisiert werden.

BIP8 ohne erzwungene Aktivierung ist der Version [BIP9](https://github.com/Bitcoin/bips/blob/master/bip-0009.mediawiki) mit Zeitüberschreitung und Verzögerung sehr ähnlich, mit dem einzigen signifikanten Unterschied, dass BIP8 Blockhöhen verwendet, während BIP9 die mittlere vergangene Zeit verwendet. Bei dieser Einstellung kann der Versuch scheitern (er kann aber später erneut versucht werden).


BIP8 mit erzwungener Aktivierung schließt mit einer obligatorischen Signalisierungsperiode ab, in der alle Blöcke, die in Übereinstimmung mit den Regeln produziert wurden, die Bereitschaft für den Soft Fork in einer Weise signalisieren müssen, die die Aktivierung in einer früheren Bereitstellung desselben Soft Fork mit nicht-obligatorischer Aktivierung auslösen wird. Mit anderen Worten: Wenn Knotenversion x ohne erzwungene Aktivierung freigegeben wird und später Version y freigegeben wird, die die Miner erfolgreich dazu zwingt, innerhalb desselben Zeitraums mit der Signalisierung der Bereitschaft zu beginnen, werden beide Versionen gleichzeitig mit der Durchsetzung der neuen Konsensregeln beginnen.


Diese Flexibilität des überarbeiteten BIP8-Vorschlags macht es möglich, einige andere Ideen so auszudrücken, wie sie unter Verwendung von BIP8 aussehen würden. Damit steht ein gemeinsamer Faktor zur Verfügung, mit dem viele verschiedene Vorschläge kategorisiert werden können.


Von diesem Zeitpunkt an wurden die Diskussionen sehr hitzig, vor allem darüber, ob `lockinontimeout` `true` (wie bei einem vom Benutzer aktivierten Soft Fork, von Harding als "BIP8 mit erzwungener Aktivierung" bezeichnet) oder `false` (wie bei einem Miner aktivierten Soft Fork, von Harding als "BIP8 ohne erzwungene Aktivierung" bezeichnet) sein sollte.


Unter den aufgelisteten Vorschlägen war einer mit "Mal sehen, was passiert" überschrieben. Aus irgendeinem Grund wurde dieser Vorschlag erst sieben Monate später aufgegriffen.


In diesen sieben Monaten ging die Diskussion weiter, und es schien, als könne kein breiter Konsens darüber erzielt werden, welcher Bereitstellungsmechanismus verwendet werden sollte. Es gab hauptsächlich zwei Lager: eines, das `lockinontimeout=true` bevorzugte (die UASF-Leute), und das andere, das `lockinontimeout=false` bevorzugte (die "Versuchen Sie es und wenn es fehlschlägt, überdenken Sie es"-Leute). Da es keine überwältigende Unterstützung für eine dieser Optionen gab, drehte sich die Debatte im Kreis, ohne dass es einen Fortschritt zu geben schien. Einige dieser Diskussionen wurden im IRC geführt, in einem Kanal namens ##Taproot-activation, aber [am 5. März 2021] (https://gnusha.org/Taproot-activation/2021-03-05.log) änderte sich etwas:


```
06:42 < harding> roconnor: is somebody proposing BIP8(3m, false)?  I mentioned that the other day but I didn't see any responses.
[...]
06:43 < willcl_ark_> Amusingly, I was just thinking to myself that, vs this, the SegWit activation was actually pretty straightforward: simply a LOT=false and if it fails a UASF.
06:43 < maybehuman> it's funny, "let's see what happens" (i.e. false, 3m) was a poular choice right at the beginning of this channel iirc
06:44 < roconnor> harding: I think I am.  I don't know how much that is worth.  Mostly I think it would be a widely acceptable configuration based on my understanding of everyone's concerns.
06:44 < willcl_ark_> maybehuman: becuase everybody actually wants this, even miners reckoned they could upgrade in about two weeks (or at least f2pool said that)
06:44 < roconnor> harding: BIP8(3m,false) with an extended lockin-period.
06:45 < harding> roconnor: oh, good.  It's been my favorite option since I first summarized the options on the wiki like seven months ago.
06:45 <@michaelfolkson> UASF wouldn't release (true,3m) but yeah Core could release (false, 3m)
06:45 < willcl_ark_> harding: It certainly seems like a good approach to me. _if_ that fails, then you can try an understand why, without wasting too much time
```


Der Ansatz "Mal sehen, was passiert" schien endlich in den Köpfen der Menschen anzukommen. Dieses Verfahren wurde später wegen seiner kurzen Signalisierungszeit als "Speedy Trial" bezeichnet. David Harding erklärt diese Idee der breiten Öffentlichkeit in einem

[E-Mail an die Bitcoin-dev Mailingliste](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-March/018583.html):

> Die frühere Version dieses Vorschlags wurde vor über 200 Tagen dokumentiert, und der zugrundeliegende Code von Taproot wurde vor über 140 Tagen in Bitcoin Core integriert. Wenn wir den Schnellversuch zu dem Zeitpunkt gestartet hätten, als Taproot integriert wurde (was etwas unrealistisch ist), wären wir entweder weniger als zwei Monate davon entfernt gewesen, Taproot zu haben, oder wir wären vor über einem Monat zum nächsten Aktivierungsversuch übergegangen.
>

> Stattdessen haben wir lange debattiert und scheinen einer meiner Meinung nach allgemein akzeptablen Lösung nicht näher gekommen zu sein als zu dem Zeitpunkt, als die Mailingliste vor über einem Jahr begann, Aktivierungspläne für die Zeit nach SegWit zu diskutieren. Ich denke, dass Speedy Trial ein Weg ist, um generate schnelle Fortschritte zu erzielen, die entweder die Debatte beenden (für den Moment, wenn die Aktivierung erfolgreich ist) oder uns einige tatsächliche Daten liefern, auf die wir uns bei zukünftigen Taproot Aktivierungsvorschlägen stützen können.

Dieser Bereitstellungsmechanismus wurde im Laufe von zwei Monaten verfeinert und dann in [Bitcoin Core Version 0.21.1](https://github.com/Bitcoin/Bitcoin/blob/master/doc/release-notes/release-notes-0.21.1.md#Taproot-Soft-Fork) veröffentlicht. Die Miner begannen schnell, dieses Upgrade zu signalisieren, indem sie den Bereitstellungsstatus auf "LOCKED_IN" setzten, und nach einer Gnadenfrist wurden die Taproot-Regeln Mitte November 2021 in Block [709632] (https://Mempool.space/block/0000000000000000000687bca986194dc2c1f949318629b44bb54ec0a94d8244) aktiviert.


#### Künftige Einführungsmechanismen


In Anbetracht der Probleme mit den jüngsten Abspaltungen von Soft, SegWit und Taproot, ist nicht klar, wie die nächste Aktualisierung eingesetzt werden soll. Speedy Trial wurde für die Einführung von Taproot verwendet, aber nur, um die Kluft zwischen der UASF und der MASF zu überbrücken, und nicht, weil es sich als der beste bekannte Einführungsmechanismus erwiesen hat.


### Risiken


Bei der Aktivierung eines Fork, sei es Hard oder Soft, Miner aktiviert oder benutzeraktiviert, besteht die Gefahr eines lang anhaltenden Kettensplits. Ein Split, der länger als ein paar Blöcke andauert, kann der Stimmung rund um Bitcoin sowie seinem Preis schweren Schaden zufügen. Vor allem aber würde es große Verwirrung darüber stiften, was Bitcoin ist. Ist Bitcoin diese Kette oder jene Kette?


Das Risiko bei einem vom Benutzer aktivierten Soft Fork besteht darin, dass die neuen Regeln auch dann aktiviert werden, wenn die Mehrheit der Hash Macht sie nicht unterstützt. Dieses Szenario würde zu einer lang anhaltenden Kettenspaltung führen, die so lange andauern würde, bis die Mehrheit der Hash-Macht die neuen Regeln annimmt. Vor allem Hard könnte einen Anreiz bieten, auf die neue Kette zu wechseln, wenn sie nach dem Split auf der alten Kette bereits Blöcke geschürft haben, da sie durch den Wechsel des Zweigs ihre eigenen Blockbelohnungen aufgeben würden. Es lohnt sich jedoch, eine bemerkenswerte Episode zu erwähnen: Im März 2013 kam es aufgrund eines unbeabsichtigten Hard Fork zu einem lang anhaltenden Split, und entgegen diesem Anreiz beschlossen zwei große Mining-Pools, ihren Zweig des Splits aufzugeben, um den Konsens wiederherzustellen.


Andererseits ist das Risiko bei einem Miner aktivierten Soft Fork eine Folge der Tatsache, dass Miner ein falsches Signal geben können, was bedeutet, dass der tatsächliche Anteil der Hash-Leistung, der die Änderung unterstützt, kleiner sein könnte als es aussieht. Wenn die tatsächliche Unterstützung nicht die Mehrheit der Hash-Power ausmacht, würden wir wahrscheinlich eine lang anhaltende Kettenspaltung ähnlich der im vorherigen Absatz beschriebenen erleben. Dieses oder zumindest ein ähnliches Problem ist in der Realität bei der Einführung von BIP66 aufgetreten, aber es wurde innerhalb von etwa 6 Blöcken gelöst.


#### Kosten einer Aufteilung



Jimmy Song [sprach über die Kosten, die mit Hard-Gabeln verbunden sind] (https://btctranscripts.com/breaking-Bitcoin/2017/socialized-costs-of-Hard-forks/) bei Breaking Bitcoin in Paris, aber vieles von dem, was er sagte, gilt auch für einen Kettensplit aufgrund eines gescheiterten Soft Fork. Er sprach von *negativen externen Effekten* und definierte sie als den Preis, den jemand anderes für Ihre eigenen Handlungen zahlen muss:


> Das klassische Beispiel für eine negative Externalität ist eine Fabrik. Vielleicht handelt es sich um eine Ölraffinerie, die ein Gut produziert, das gut für die Wirtschaft ist, aber sie produziert auch etwas, das eine negative Externalität darstellt, wie die Umweltverschmutzung. Das ist nicht nur etwas, wofür jeder bezahlen muss, um es zu beseitigen, oder worunter er leiden muss. Es gibt auch Auswirkungen zweiter und dritter Ordnung, wie z. B. mehr Verkehr in Richtung der Fabrik, weil mehr Arbeiter dorthin fahren müssen. Es könnte auch sein, dass Sie die Tierwelt in der Umgebung gefährden. Es ist nicht so, dass jeder für die negativen externen Effekte zahlen muss, sondern es könnten bestimmte Personen sein, wie z. B. Menschen, die zuvor die Straße benutzt haben, oder Tiere, die sich in der Nähe der Fabrik aufhielten, und auch sie zahlen für die Kosten der Fabrik.

Im Zusammenhang mit Bitcoin veranschaulicht er negative externe Effekte anhand von Bitcoin Cash (bcash), einem Hard Fork von Bitcoin, das kurz vor dieser Konferenz im Jahr 2017 geschaffen wurde. Er kategorisiert die negativen externen Effekte eines Hard Fork in einmalige Kosten und dauerhafte Kosten.


Unter den vielen Beispielen für einmalige Kosten nennt er die Kosten, die bei Börsen entstehen:


> Wir haben also eine Reihe von Börsen, und sie hatten eine Menge einmaliger Kosten zu tragen. Das erste, was passierte, war, dass Einzahlungen und Abhebungen bei diesen Börsen für ein oder zwei Tage gestoppt werden mussten, weil sie nicht wussten, was passieren würde. Viele dieser Börsen mussten auf den Cold-Speicher zurückgreifen, weil ihre Nutzer bcash verlangten. Das ist Teil ihrer treuhänderischen Pflicht, sie müssen das tun. Sie müssen auch die neue Software prüfen. Das ist etwas, was wir bei itbit tun mussten. Wir wollen bcash ausgeben - wie machen wir das? Müssen wir electron cash herunterladen? Ist es mit Malware infiziert? Wir müssen es prüfen. Wir hatten etwa 10 Tage Zeit, um herauszufinden, ob das in Ordnung ist oder nicht. Und dann müssen Sie entscheiden, ob wir nur eine einmalige Abhebung zulassen oder ob wir diese neue Münze auflisten wollen Für einen Exchange ist es nicht einfach, eine neue Münze aufzulisten - es gibt alle möglichen neuen Verfahren für Cold Lagerung, Unterzeichnung, Einzahlungen, Abhebungen. Oder man könnte einfach eine einmalige Aktion durchführen, bei der man ihnen irgendwann ihr Bargeld gibt und dann nie wieder daran denkt. Aber auch das hat seine Probleme. Und schließlich, egal wie man es macht, Abhebungen oder Auflistungen - man wird eine neue Infrastruktur brauchen, um mit diesem token in irgendeiner Weise zu arbeiten, selbst wenn es eine einmalige Abhebung ist. Sie brauchen eine Möglichkeit, diese Token an Ihre Nutzer weiterzugeben. Auch hier gilt: Kurzfristig. Richtig? Dafür ist keine Zeit, es muss schnell gehen.

Er listet auch die einmaligen Kosten auf, die Händlern, Zahlungsabwicklern, Wallets, Minern und Nutzern entstehen, sowie einige der dauerhaften Kosten, zum Beispiel der Verlust der Privatsphäre und ein höheres Risiko von Reorgs.


Wenn es zu einer Aufspaltung kommt und die Kette mit den allgemeinsten Regeln stärker wird als die Kette mit den strengeren Regeln, kommt es zu einer Reorganisation. Dies hat schwerwiegende Auswirkungen auf alle Transaktionen, die in dem ausgelöschten Zweig durchgeführt werden. Aus diesen Gründen ist es sehr wichtig, Kettenaufspaltungen immer zu vermeiden.


### Schlussfolgerung zum Upgrading


Bitcoin wächst und entwickelt sich mit der Zeit weiter. Im Laufe der Jahre wurden verschiedene Upgrade-Mechanismen eingesetzt, und die Lernkurve ist steil. Es werden immer ausgefeiltere und robustere Methoden erfunden, da wir mehr darüber erfahren, wie das Netz reagiert.


Um Bitcoin in Harmonie zu halten, haben sich Soft-Gabelungen als der richtige Weg erwiesen, aber die große Frage ist immer noch nicht vollständig beantwortet: Wie können wir Soft-Gabelungen sicher einsetzen, ohne Zwietracht zu verursachen?


## Gegensätzliches Denken

<chapterId>d4982f3d-4694-51cc-99be-28f54b03a2a2</chapterId>


![](assets/adversarialthinking-banner.webp)


Dieses Kapitel befasst sich mit *adversarischem Denken*, einer Denkweise, die sich darauf konzentriert, was schief gehen könnte und wie Gegner handeln könnten. Wir beginnen mit der Erörterung der Sicherheitsannahmen und des Sicherheitsmodells von Bitcoin und erklären dann, wie normale Benutzer ihre Selbstsouveränität und die Full node Dezentralisierung von Bitcoin verbessern können, indem sie kontraproduktiv denken. Dann schauen wir uns einige tatsächliche Bedrohungen für Bitcoin sowie die Denkweise des Gegners an. Schließlich sprechen wir über das *Axiom des Widerstands*, das Ihnen helfen kann zu verstehen, warum die Leute überhaupt an Bitcoin arbeiten.


Wenn man über die Sicherheit verschiedener Systeme diskutiert, ist es wichtig, die Sicherheitsannahmen zu verstehen. Eine typische Sicherheitsannahme in Bitcoin ist "das diskrete Logarithmusproblem ist Hard zu lösen", was einfach ausgedrückt bedeutet, dass es praktisch unmöglich ist, einen privaten Schlüssel zu finden, der einem bestimmten öffentlichen Schlüssel entspricht. Eine weitere ziemlich starke Sicherheitsannahme ist, dass die Mehrheit der Hashpower des Netzes ehrlich ist, d. h. dass sie sich an die Regeln hält. Wenn sich diese Annahmen als falsch erweisen, dann ist Bitcoin in Schwierigkeiten.


Im Jahr 2015 hielt Andrew Poelstra [einen Vortrag] (https://btctranscripts.com/scalingbitcoin/hong-kong-2015/security-assumptions/) auf der Scaling Bitcoin-Konferenz in Hongkong, in dem er die Sicherheitsannahmen von Bitcoin analysierte. Er beginnt mit der Feststellung, dass viele Systeme Gegner bis zu einem gewissen Grad außer Acht lassen; so ist es beispielsweise wirklich Hard, ein Gebäude gegen alle Arten von Angriffen zu schützen. Stattdessen akzeptieren wir im Allgemeinen die Möglichkeit, dass jemand das Gebäude niederbrennt, und verhindern dieses und andere gegnerische Verhaltensweisen bis zu einem gewissen Grad durch Strafverfolgung usw.


Siehe die Analogie des Gebäudes von Greg Maxwell:


![](https://youtu.be/Gs9lJTRZCDc?t=2799)


Aber online sind die Dinge anders:


> Im Internet ist das jedoch nicht der Fall. Wir haben pseudonymes und anonymes Verhalten, jeder kann sich mit jedem verbinden und das System schädigen. Wenn es möglich ist, das System zu schädigen, dann werden sie es tun. Wir können nicht davon ausgehen, dass sie sichtbar sein werden und dass sie erwischt werden.

Die Folge ist, dass alle bekannten Schwachstellen in Bitcoin irgendwie behoben werden müssen, sonst werden sie ausgenutzt. Schließlich ist Bitcoin der größte Honigtopf der Welt.


Poelstra führt weiter aus, dass es sich bei Bitcoin um ein neuartiges System handelt, das nebulöser ist als beispielsweise ein Unterschriftsprotokoll, das sehr klare Sicherheitsvoraussetzungen hat.


In seinem persönlichen Blog geht der Software-Ingenieur Jameson Lopp auf dieses Thema ein (https://blog.lopp.net/bitcoins-security-model-a-deep-dive/):


> In Wirklichkeit wurde und wird das Bitcoin-Protokoll ohne eine formell definierte Spezifikation oder ein Sicherheitsmodell entwickelt. Das Beste, was wir tun können, ist, die Anreize und das Verhalten der Akteure innerhalb des Systems zu untersuchen, um es besser zu verstehen und zu beschreiben.

Wir haben also ein System, das in der Praxis zu funktionieren scheint, dessen Sicherheit wir aber nicht formell beweisen können. Ein Beweis ist wahrscheinlich nicht möglich aufgrund von

die Komplexität des Systems selbst.


### Nicht nur für Bitcoin-Experten



Die Bedeutung des kontradiktorischen Denkens erstreckt sich bis zu einem gewissen Grad auch auf alltägliche Bitcoin-Nutzer, nicht nur auf Hardcore-Bitcoin-Entwickler und Experten. Ragnar Lifthasir erwähnt in einem [Tweetstorm] (https://bitcoinwords.github.io/tweetstorm-on-adversarial-thinking), wie vereinfachende Erzählungen über Bitcoin - zum Beispiel "nur HODL" - Bitcoin selbst herabsetzen können, und schließt mit den Worten


> Um Bitcoin und uns selbst stärker zu machen, müssen wir wie die Software-Ingenieure denken, die zu Bitcoin beitragen. Sie führen Peer Reviews durch und suchen gnadenlos nach Fehlern. Auf ihren technischen Veranstaltungen sprechen sie über alle Möglichkeiten, wie ein Vorschlag scheitern kann. Sie denken kontraproduktiv. Sie sind konservativ

Er bezeichnet diese vereinfachenden Erzählungen als Monomanien. Mit dieser Definition will er sagen, dass man, wenn man sich auf eine einzige Sache konzentriert - z. B. "nur HODL" -, Gefahr läuft, die wohl wichtigeren Dinge zu übersehen, wie z. B. sein Bitcoin sicher zu halten oder sein Bestes zu tun, um Bitcoin in einer Trustless Weise zu nutzen.


### Bedrohungen



Es gibt eine Menge bekannter Schwachstellen in Bitcoin, und viele davon werden aktiv ausgenutzt. Um einen Eindruck davon zu bekommen, werfen Sie einen Blick auf die [Schwachstellen-Seite] (https://en.Bitcoin.it/wiki/Weaknesses) im Bitcoin-Wiki. Dort wird eine Vielzahl von Problemen erwähnt, wie z. B

Wallet Diebstahl und Denial-of-Service-Angriffe:


> Wenn ein Angreifer versucht, das Netzwerk mit von ihm kontrollierten Clients zu füllen, ist es sehr wahrscheinlich, dass Sie sich nur mit Angreiferknoten verbinden. Obwohl Bitcoin niemals eine Zählung von Knoten für irgendetwas verwendet, kann die vollständige Isolierung eines Knotens vom ehrlichen Netzwerk bei der Ausführung anderer Angriffe hilfreich sein.

Diese Art des Angriffs wird als *Sybil-Angriff* bezeichnet und tritt immer dann auf, wenn ein einziges Unternehmen mehrere Knoten in einem Netzwerk kontrolliert und diese benutzt, um als mehrere Unternehmen aufzutreten.


Wie in dem Zitat auch erwähnt wird, ist der Sybil-Angriff im Bitcoin-Netz nicht wirksam, da es keine Abstimmung über Knoten oder andere zählbare Einheiten gibt, sondern über die Rechenleistung. Nichtsdestotrotz macht diese flache Struktur das System anfällig für andere Angriffe. Auf der Bitcoin-Wiki-Seite werden auch andere mögliche Angriffe beschrieben, z. B. das Verstecken von Informationen (oft als *Eclipse-Angriff* bezeichnet), und die Art und Weise, wie Bitcoin Core einige heuristische Gegenmaßnahmen gegen solche Angriffe implementiert.


Dies sind Beispiele für reale Bedrohungen, die es zu bekämpfen gilt.


### Einfaches Sabotagefeld


![](assets/sabotage-manual.webp)


Auszug aus dem Simple Sabotage Field Manual


Um die Denkweise des Gegners besser zu verstehen, könnte es hilfreich sein, einen Einblick in seine Arbeitsweise zu bekommen. Eine US-Regierungsbehörde namens Office of Strategic Services, die während des Zweiten Weltkriegs tätig war und unter anderem Spionage, Sabotage und Propaganda betreiben sollte, erstellte ein [Handbuch] (https://www.gutenberg.org/ebooks/26184) für ihr Personal, in dem beschrieben wurde, wie man den Feind richtig sabotiert. Es trug den Titel "Simple Sabotage Field Manual" und enthielt konkrete Tipps, wie man den Feind infiltriert, um ihm das Leben schwer zu machen (Hard). Die Tipps reichten vom Niederbrennen von Lagerhallen bis hin zur Abnutzung von Bohrern, um den Feind zu schwächen

effizienz.


Zum Beispiel gibt es einen Abschnitt darüber, wie ein Infiltrator Organisationen stören kann. Es ist nicht Hard zu sehen, wie solche Taktiken eingesetzt werden könnten, um den Bitcoin Entwicklungsprozess, an dem sich jeder beteiligen kann, ins Visier zu nehmen. Ein engagierter Angreifer kann den Fortschritt durch endlose Bedenken zu irrelevanten Themen abwürgen, um präzise Formulierungen feilschen und versuchen, Diskussionen zu wiederholen, die bereits umfassend behandelt wurden. Der Angreifer kann auch eine Trollarmee anheuern, um seine eigene Effektivität zu vervielfachen; wir können dies einen sozialen Sybil-Angriff nennen. Mit einem sozialen Sybil-Angriff können sie den Anschein erwecken, dass es mehr Widerstand gegen eine vorgeschlagene Änderung gibt, als es tatsächlich der Fall ist.


Dies verdeutlicht, dass ein entschlossener Staat alles in seiner Macht stehende tun kann und wird, um den Feind zu vernichten, einschließlich seiner Zerschlagung von innen heraus. Da Bitcoin eine Form von Geld ist, die mit etablierten Fiat-Währungen konkurriert, ist es wahrscheinlich, dass Staaten Bitcoin als Feind betrachten.


### Axiom des Widerstands


Eric Voskuil [schreibt auf seiner Cryptoeconomics-Wiki-Seite] (https://github.com/libbitcoin/libbitcoin-system/wiki/Axiom-of-Resistance) über das, was er das "Axiom des Widerstands" nennt:


> Mit anderen Worten: Es wird davon ausgegangen, dass es möglich ist, dass sich ein System der staatlichen Kontrolle entzieht. Dies wird nicht als Tatsache akzeptiert, sondern aufgrund empirischer Untersuchungen des Verhaltens ähnlicher Systeme als vernünftige Annahme angesehen, auf die sich das System stützen kann.
>

> Wer das Axiom des Widerstands nicht akzeptiert, betrachtet ein völlig anderes System als Bitcoin. Wenn man davon ausgeht, dass es für ein System nicht möglich ist, staatlichen Kontrollen zu widerstehen, machen Schlussfolgerungen im Kontext von Bitcoin keinen Sinn - so wie Schlussfolgerungen in der sphärischen Geometrie der euklidischen Geometrie widersprechen. Wie kann Bitcoin ohne das Axiom erlaubnisfrei oder zensurresistent sein? Der Widerspruch führt zu offensichtlichen Fehlern, wenn man versucht, den Konflikt zu rationalisieren.


Im Wesentlichen will er damit sagen, dass ein Versuch nur dann sinnvoll ist, wenn man annimmt, dass es möglich ist, ein System zu schaffen, das die Staaten nicht kontrollieren können.


Das bedeutet, dass Sie für die Arbeit an Bitcoin das Axiom des Widerstands akzeptieren sollten, da Sie sonst Ihre Zeit besser mit anderen Projekten verbringen sollten. Die Anerkennung dieses Axioms hilft Ihnen, Ihre Entwicklungsanstrengungen auf die wirklichen Probleme zu konzentrieren: die Codierung von Gegnern auf staatlicher Ebene. Mit anderen Worten: Denken Sie gegnerisch.


### Schlussfolgerung zum kontradiktorischen Denken



Ein dezentralisiertes System kann keine Rechenschaftspflicht außerhalb des Systems selbst haben, daher muss Bitcoin bösartiges Verhalten rigoroser verhindern als traditionelle Systeme. Bösartiges Denken ist in einem solchen System unabdingbar.


Um Bitcoin sicher zu halten, muss man seine Feinde und deren Anreize kennen. Die meisten Bedrohungen scheinen sich auf die Nationalstaaten zu beschränken, die durch Besteuerung und Gelddrucken über enorme wirtschaftliche Macht verfügen. Sie werden ihre Gelddruckprivilegien wahrscheinlich nicht so leicht aufgeben.


## Offene Quelle

<chapterId>427a160c-f893-5b2c-afba-7b24e71ba899</chapterId>



![](assets/opensource-banner.webp)


Bitcoin wurde mit Open-Source-Software entwickelt. In diesem Kapitel analysieren wir, was das bedeutet, wie die Wartung der Software funktioniert und wie Open-Source-Software im Bitcoin eine erlaubnisfreie Entwicklung ermöglicht. Wir tauchen ein in die *Auswahlkryptographie*, die sich mit der Auswahl und Verwendung von Bibliotheken in kryptographischen Systemen beschäftigt. Das Kapitel enthält einen Abschnitt über den Überprüfungsprozess von Bitcoin, gefolgt von einem weiteren über die Art und Weise, wie Bitcoin-Entwickler finanziert werden. Im letzten Abschnitt geht es darum, wie die Open-Source-Kultur von Bitcoin von außen betrachtet wirklich seltsam aussehen kann, und warum diese vermeintliche Seltsamkeit in Wirklichkeit ein Zeichen für gute Gesundheit ist.


Die meisten Bitcoin-Programme, insbesondere Bitcoin Core, sind Open Source. Das bedeutet, dass der Quellcode der Software der Allgemeinheit zur Einsichtnahme, zum Basteln, zur Veränderung und zur Weitergabe zur Verfügung gestellt wird. Die Definition von Open Source unter [](https://opensource.org/osd) beinhaltet unter anderem die folgenden wichtigen Punkte:


> Freie Weiterverbreitung: Die Lizenz darf niemanden daran hindern, die Software als Bestandteil einer Gesamt-Software-Distribution, die Programme aus verschiedenen Quellen enthält, zu verkaufen oder weiterzugeben. Die Lizenz darf keine Lizenzgebühr oder sonstige Gebühr für einen solchen Verkauf verlangen.
>

> Quellcode: Das Programm muss den Quellcode enthalten und die Weitergabe sowohl in Quellcode- als auch in kompilierter Form ermöglichen. Wird ein Produkt in irgendeiner Form nicht mit dem Quellcode vertrieben, muss es eine gut publizierte Möglichkeit geben, den Quellcode für nicht mehr als angemessene Reproduktionskosten zu erhalten, vorzugsweise durch kostenloses Herunterladen über das Internet. Der Quellcode muss die bevorzugte Form sein, in der ein Programmierer das Programm ändern würde. Absichtlich verschleierter Quellcode ist nicht zulässig. Zwischenformen wie die Ausgabe eines Präprozessors oder Übersetzers sind nicht zulässig.
>

> Abgeleitete Werke: Die Lizenz muss Modifikationen und abgeleitete Werke zulassen und deren Weitergabe unter denselben Bedingungen erlauben wie die Lizenz der Originalsoftware.

Bitcoin Core hält sich an diese Definition, indem es unter der [MIT-Lizenz] (https://github.com/Bitcoin/Bitcoin/blob/master/COPYING) verbreitet wird:


```
The MIT License (MIT)

Copyright (c) 2009-2022 The Bitcoin Core developers
Copyright (c) 2009-2022 Bitcoin Developers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
```


Wie im Kapitel "Don't Trust, Verify" erwähnt, ist es wichtig, dass die Benutzer überprüfen können, ob die Bitcoin-Software, die sie ausführen, "wie beworben" funktioniert. Dazu müssen sie uneingeschränkten Zugriff auf den Quellcode der Software haben, die sie überprüfen wollen.


In den nächsten Abschnitten werden wir uns mit einigen anderen interessanten Aspekten von Open-Source-Software in Bitcoin befassen.


### Wartung der Software



Der Quellcode von Bitcoin Core wird in einem Git-Repository verwaltet, das auf [GitHub] (https://github.com/Bitcoin/Bitcoin) gehostet wird. Jeder kann dieses Repository klonen, ohne um Erlaubnis zu fragen, und es dann lokal prüfen, erstellen oder ändern. Das bedeutet, dass es viele Tausende von Kopien des Repositorys gibt, die über den gesamten Globus verteilt sind. Dies sind alles Kopien desselben Repositorys. Was also macht dieses spezielle GitHub Bitcoin Core Repository so besonders? Technisch gesehen ist es überhaupt nichts Besonderes, aber gesellschaftlich ist es zum Mittelpunkt der Bitcoin-Entwicklung geworden.


Der Bitcoin- und Sicherheitsexperte Jameson Lopp erklärt dies sehr gut in einem [Blogbeitrag] (https://blog.lopp.net/who-controls-Bitcoin-core-/) mit dem Titel "Who Controls Bitcoin Core?":


> Bitcoin Core ist eher ein Brennpunkt für die Entwicklung des Bitcoin-Protokolls als ein Punkt der Befehls- und Kontrollfunktion. Wenn er aus irgendeinem Grund nicht mehr existieren würde, würde ein neuer Brennpunkt entstehen - die technische Kommunikationsplattform, auf der er basiert (derzeit das GitHub-Repository), ist eher eine Frage der Bequemlichkeit als eine der Definition/Projektintegrität. Tatsächlich haben wir bereits erlebt, dass der Entwicklungsschwerpunkt von Bitcoin die Plattform und sogar den Namen wechselt!

Er fährt fort zu erklären, wie die Software von Bitcoin Core gewartet und gegen bösartige Codeänderungen gesichert wird. Die allgemeinen Erkenntnisse aus diesem vollständigen Artikel werden ganz am Ende zusammengefasst:


> Keiner kontrolliert Bitcoin.
>

> Niemand kontrolliert den Schwerpunkt der Entwicklung von Bitcoin.

Der Entwickler von Bitcoin Core, Eric Lombrozo, spricht in seinem [Medium-Beitrag] (https://medium.com/@elombrozo/the-Bitcoin-core-merge-process-74687a09d81d) mit dem Titel "The Bitcoin Core Merge Process" weiter über den Entwicklungsprozess:


> Jeder kann Fork, das Repository der Codebasis, verwenden und beliebige Änderungen an seinem eigenen Repository vornehmen. Sie können einen Client aus ihrem eigenen Repository erstellen und diesen stattdessen ausführen, wenn sie wollen. Sie können auch Binär-Builds erstellen, die andere Leute ausführen können.
>

> Wenn jemand eine Änderung, die er in seinem eigenen Repository vorgenommen hat, in Bitcoin Core einbringen möchte, kann er einen Pull Request einreichen. Nach dem Einreichen kann jeder die Änderungen überprüfen und kommentieren, unabhängig davon, ob er Zugriff auf Bitcoin Core selbst hat oder nicht.

Es sollte beachtet werden, dass es sehr lange dauern kann, bis Pull Requests von den Maintainern in das Repository eingebunden werden, und das ist normalerweise auf einen Mangel an Review zurückzuführen, der oft auf einen Mangel an *Reviewern* zurückzuführen ist.


Lombrozo geht auch auf den Prozess ein, der mit Konsensänderungen einhergeht, aber das würde den Rahmen dieses Kapitels sprengen. Weitere Informationen darüber, wie das Bitcoin-Protokoll aktualisiert wird, finden Sie im vorangegangenen Kapitel "Aktualisierung".


### Genehmigungsfreie Entwicklung



Wir haben festgelegt, dass jeder Code für Bitcoin Core schreiben kann, ohne um Erlaubnis zu fragen, aber nicht unbedingt in das Haupt-Git-Repository eingebunden werden muss. Dies betrifft jede Änderung, von der Änderung der Farbschemata der grafischen Benutzer-Interface über die Art und Weise, wie Peer-to-Peer-Nachrichten formatiert werden, bis hin zu den Konsensregeln, d. h. dem Satz von Regeln, die einen gültigen Blockchain definieren.


Wahrscheinlich ebenso wichtig ist, dass es den Benutzern freisteht, Systeme auf der Grundlage von Bitcoin zu entwickeln, ohne um Erlaubnis zu fragen. Wir haben zahllose erfolgreiche Softwareprojekte gesehen, die auf Bitcoin aufgebaut wurden, wie z. B:



- Lightning Network: Ein Zahlungsnetz, das eine schnelle Zahlung von sehr kleinen Beträgen ermöglicht. Es erfordert sehr wenige On-Chain Bitcoin Transaktionen. Es gibt verschiedene interoperable Implementierungen, wie [Core Lightning](https://github.com/ElementsProject/lightning), [LND](https://github.com/lightningnetwork/LND), [Eclair](https://github.com/ACINQ/eclair) und [Lightning Dev Kit](https://github.com/lightningdevkit).
- CoinJoin: Mehrere Parteien arbeiten zusammen, um ihre Zahlungen in einer einzigen Transaktion zusammenzufassen, um Address Clustering zu erschweren. Es gibt verschiedene Implementierungen.
- Sidechains: Dieses System kann eine Münze auf dem Blockchain des Bitcoin sperren, um sie auf einem anderen Blockchain freizugeben. Dadurch können Bitcoins auf eine andere Blockchain, nämlich eine Sidechain, verschoben werden, um die auf dieser Sidechain verfügbaren Funktionen zu nutzen. Beispiele hierfür sind [Blockstreams Elements] (https://github.com/ElementsProject/Elements).
- OpenTimestamps: Ermöglicht es Ihnen, [Timestamp ein Dokument](https://opentimestamps.org/) auf Bitcoins Blockchain auf eine private Weise zu speichern. Sie können dann diese Timestamp verwenden, um zu beweisen, dass ein Dokument vor einem bestimmten Zeitpunkt existiert haben muss.


Ohne die genehmigungsfreie Entwicklung wären viele dieser Projekte nicht möglich gewesen. Wie im Kapitel über die Neutralität dargelegt, würden nur die Protokolle entwickelt werden, die vom zentralen Ausschuss für die Erteilung von Genehmigungen an Entwickler zugelassen sind, wenn Entwickler um eine Genehmigung für die Erstellung von Protokollen auf der Grundlage von Bitcoin bitten müssten.


Es ist üblich, dass Systeme wie die oben genannten selbst als Open-Source-Software lizenziert werden, was es wiederum anderen ermöglicht, ihren Code beizutragen, wiederzuverwenden oder zu überprüfen, ohne um Erlaubnis zu fragen. Open Source ist zum Goldstandard der Bitcoin-Softwarelizenzierung geworden.


### Pseudonyme Entwicklung



Die Tatsache, dass Sie für die Entwicklung von Bitcoin-Software nicht um Erlaubnis fragen müssen, bietet eine interessante und wichtige Option: Sie können Code schreiben und veröffentlichen, in Bitcoin Core oder jedem anderen Open-Source-Projekt, ohne Ihre Identität preiszugeben.


Viele Entwickler wählen diese Option, indem sie unter einem Pseudonym arbeiten und versuchen, es von ihrer wahren Identität zu trennen. Die Gründe dafür können von Entwickler zu Entwickler unterschiedlich sein. Ein pseudonymer Benutzer ist ZmnSCPxj. Neben anderen Projekten trägt er zu Bitcoin Core und Core Lightning bei, eine von mehreren Implementierungen von Lightning Network. [Er schreibt](https://zmnscpxj.github.io/about.html) auf seiner Webseite:


> Ich bin ZmnSCPxj, eine zufällig generierte Internetperson. Meine Pronomen sind er/sie/sie.
>

> Ich verstehe, dass die Menschen instinktiv meine Identität wissen wollen. Ich denke jedoch, dass meine Identität weitgehend immateriell ist, und ziehe es vor, nach meiner Arbeit beurteilt zu werden.
>

> Wenn Sie sich fragen, ob Sie spenden sollen oder nicht, und wenn Sie sich fragen, wie hoch meine Lebenshaltungskosten oder mein Einkommen sind, dann verstehen Sie bitte, dass Sie mir genau genommen nach dem Nutzen spenden sollten, den Sie in meinen
artikel und meine Arbeit an Bitcoin und Lightning Network.


In seinem Fall ist der Grund für die Verwendung eines Pseudonyms nach seinen Verdiensten zu beurteilen und nicht danach, wer die Person(en) hinter dem Pseudonym ist/sind. Interessanterweise verriet er in einem [Artikel auf CoinDesk] (https://www.coindesk.com/markets/2020/06/29/many-Bitcoin-developers-are-choosing-to-use-pseudonyms-for-good-reason/), dass das Pseudonym aus einem anderen Grund geschaffen wurde.


> Mein ursprünglicher Grund [für die Verwendung eines Pseudonyms] war einfach, dass ich mir Sorgen machte, einen großen Fehler zu begehen; daher war ZmnSCPxj ursprünglich als Wegwerf-Pseudonym gedacht, das in einem solchen Fall aufgegeben werden kann. Es scheint jedoch einen überwiegend positiven Ruf zu haben, so dass ich es beibehalten habe

Die Verwendung eines Pseudonyms ermöglicht es Ihnen in der Tat, freier zu sprechen, ohne Ihren persönlichen Ruf zu gefährden, wenn Sie etwas Dummes sagen oder einen großen Fehler machen. Wie sich herausstellte, wurde sein Pseudonym sehr angesehen und im Jahr 2019 [erhielt er sogar einen Entwicklungszuschuss] (https://twitter.com/spiralbtc/status/1204815615678177280), was an sich schon ein Beweis für die erlaubnisfreie Natur von Bitcoin ist.


Das wohl bekannteste Pseudonym in Bitcoin ist Satoshi Nakamoto. Es ist unklar, warum er sich für ein Pseudonym entschied, aber im Nachhinein betrachtet war es wahrscheinlich aus mehreren Gründen eine gute Entscheidung:


- Da viele Leute spekulieren, dass Nakamoto eine Menge Bitcoin besitzt, ist es für seine finanzielle und persönliche Sicherheit unerlässlich, dass seine Identität unbekannt bleibt.
- Da seine Identität unbekannt ist, gibt es keine Möglichkeit, jemanden strafrechtlich zu verfolgen, was verschiedenen Regierungsbehörden eine Hard Zeit gibt.
- Es gibt keine Autoritätsperson, zu der man aufschauen kann, was Bitcoin leistungsorientierter und erpressungsresistenter macht.


Beachten Sie, dass diese Punkte nicht nur für Satoshi Nakamoto gelten, sondern in unterschiedlichem Maße für jeden, der in Bitcoin arbeitet oder bedeutende Mengen der Währung besitzt.


### Auswahl Kryptographie


Open-Source-Entwickler nutzen oft Open-Source-Bibliotheken, die von anderen entwickelt wurden. Dies ist ein natürlicher und großartiger Teil eines gesunden Ökosystems. Aber bei Bitcoin-Software geht es um echtes Geld, und deshalb müssen Entwickler besonders vorsichtig sein, wenn sie die Bibliotheken von Drittanbietern auswählen, von denen sie abhängig sein sollen.


In einem philosophischen [Vortrag über Kryptographie] (https://btctranscripts.com/greg-maxwell/2015-04-29-gmaxwell-Bitcoin-selection-cryptography/) will Gregory Maxwell den Begriff "Kryptographie" neu definieren, den er für zu eng hält. Er erklärt, dass im Grunde *Information frei sein will*, und begründet seine Definition von Kryptographie damit:


> Kryptografie ist die Kunst und Wissenschaft, die wir einsetzen, um die grundlegende Natur der Information zu bekämpfen, sie unserem politischen und moralischen Willen anzupassen und sie gegen alle Zufälle und Bemühungen, sich ihr zu widersetzen, für menschliche Zwecke einzusetzen.

Anschließend führt er den Begriff *Selektionskryptografie* ein, der als die Kunst der Auswahl kryptografischer Werkzeuge bezeichnet wird, und erklärt, warum dies ein wichtiger Teil der Kryptografie ist. Es geht darum, wie man kryptografische Bibliotheken, Werkzeuge und Praktiken auswählt, oder wie er sagt "das Kryptosystem der Auswahl von Kryptosystemen".


Anhand konkreter Beispiele zeigt er, wie die Auswahl von Kryptographie leicht schief gehen kann, und schlägt eine Liste von Fragen vor, die Sie sich stellen können, wenn Sie sie praktizieren. Im Folgenden finden Sie eine gekürzte Fassung dieser Liste:


- Ist die Software für Ihre Zwecke geeignet?
- Werden die kryptografischen Überlegungen ernst genommen?
- Wie sieht das Überprüfungsverfahren aus? Gibt es eines?
- Welche Erfahrungen haben die Autoren gemacht?
- Ist die Software dokumentiert?
- Ist die Software portabel?
- Ist die Software getestet?
- Verwendet die Software bewährte Verfahren?


Dies ist zwar nicht der ultimative Leitfaden für den Erfolg, aber es kann sehr hilfreich sein, diese Punkte bei der Auswahl von Kryptographie durchzugehen.


Aufgrund der von Maxwell erwähnten Probleme versucht Bitcoin Core wirklich Hard, [seine Abhängigkeit von Bibliotheken von Drittanbietern zu minimieren] (https://github.com/Bitcoin/Bitcoin/blob/master/doc/dependencies.md). Natürlich kann man nicht alle externen Abhängigkeiten beseitigen, sonst müsste man alles selbst schreiben, von der Schriftdarstellung bis zur Implementierung von Systemaufrufen.


### Überprüfung



Dieser Abschnitt heißt "Überprüfung" und nicht "Codeüberprüfung", weil die Sicherheit von Bitcoin stark von der Überprüfung auf mehreren Ebenen abhängt, nicht nur vom Quellcode. Außerdem erfordern verschiedene Ideen eine Überprüfung auf verschiedenen Ebenen: eine Änderung der Konsensregel würde eine tiefere Überprüfung auf mehreren Ebenen erfordern als eine Änderung des Farbschemas oder eine Tippfehlerbehebung.


Auf dem Weg zur endgültigen Verabschiedung durchläuft eine Idee in der Regel mehrere Phasen der Diskussion und Überprüfung. Einige dieser Phasen sind im Folgenden aufgeführt:



- Eine Idee wird auf der Bitcoin-dev-Mailingliste veröffentlicht
- Die Idee wird in einem Bitcoin Verbesserungsvorschlag (BIP) formalisiert
- Die BIP wird in einem Pull Request (PR) an Bitcoin Core implementiert
- Mechanismen für den Einsatz werden diskutiert
- Einige konkurrierende Bereitstellungsmechanismen sind in Pull Requests zu Bitcoin Core implementiert
- Pull-Requests werden mit dem Master-Zweig zusammengeführt
- Die Nutzer entscheiden, ob sie die Software nutzen wollen oder nicht


In jeder dieser Phasen prüfen Personen mit unterschiedlichen Standpunkten und Hintergründen die verfügbaren Informationen, sei es der Quellcode, ein BIP oder nur eine lose beschriebene Idee. Die Phasen werden in der Regel nicht streng von oben nach unten durchgeführt, sondern es können mehrere Phasen gleichzeitig stattfinden, und manchmal wird zwischen ihnen hin und her gewechselt. Auch können verschiedene Personen während verschiedener Phasen Feedback geben.


Einer der fleißigsten Code-Reviewer bei Bitcoin Core ist Jon Atack. Er schrieb [einen Blogbeitrag] (https://jonatack.github.io/articles/how-to-review-pull-requests-in-Bitcoin-core) darüber, wie man Pull Requests in Bitcoin Core überprüft. Er betont, dass ein guter Code-Reviewer sich darauf konzentriert, wie er am besten einen Mehrwert schaffen kann.


> Als Neuling sollte man versuchen, mit Freundlichkeit und Bescheidenheit einen Beitrag zu leisten und dabei so viel wie möglich zu lernen.
>

> Eine gute Herangehensweise ist es, sich nicht mit sich selbst zu beschäftigen, sondern mit der Frage: "Wie kann ich am besten dienen?"

Er unterstreicht die Tatsache, dass die Überprüfung ein wirklich einschränkender Faktor in Bitcoin Core ist. Viele gute Ideen bleiben in einem Schwebezustand stecken, in dem keine Überprüfung stattfindet. Er weist darauf hin, dass die Überprüfung nicht nur für Bitcoin von Vorteil ist, sondern auch eine großartige Möglichkeit darstellt, etwas über die Software zu lernen und ihr gleichzeitig einen Mehrwert zu verleihen. Als Faustregel empfiehlt Atack, 5-15 PRs zu prüfen, bevor Sie selbst einen PR machen. Auch hier sollten Sie sich darauf konzentrieren, wie Sie der Gemeinschaft am besten dienen können, und nicht darauf, wie Sie Ihren eigenen Code einbinden können. Darüber hinaus betont er, wie wichtig es ist, die Überprüfung auf der richtigen Ebene durchzuführen: Ist jetzt die Zeit für Fehler und Tippfehler, oder braucht der Entwickler eher eine konzeptionell orientierte Überprüfung? Jon Attack fügt hinzu:


> Eine nützliche erste Frage zu Beginn einer Überprüfung kann lauten: "Was wird hier zum jetzigen Zeitpunkt am meisten gebraucht?" Die Beantwortung dieser Frage erfordert Erfahrung und einen umfassenden Kontext, aber sie ist eine nützliche Frage, um zu entscheiden, wie Sie in kürzester Zeit den größten Nutzen erzielen können.

Die zweite Hälfte des Beitrags besteht aus einigen nützlichen praktischen technischen Anleitungen, wie die Überprüfung tatsächlich durchgeführt wird, und enthält Links zu wichtigen Dokumentationen für die weitere Lektüre.


Die Bitcoin Core-Entwicklerin und Code-Reviewerin Gloria Zhao hat [einen Artikel] (https://github.com/glozow/Bitcoin-notes/blob/master/review-checklist.md) geschrieben, der Fragen enthält, die sie sich normalerweise während einer Überprüfung stellt. Sie gibt auch an, was sie für eine gute Überprüfung hält:


> Ich persönlich denke, eine gute Rezension ist eine, bei der ich mir eine Menge gezielter Fragen über die PR gestellt habe und mit den Antworten zufrieden war
zu ihnen. [...] Natürlich beginne ich mit konzeptionellen Fragen, dann mit Fragen zum Ansatz und schließlich mit Fragen zur Implementierung. Im Allgemeinen halte ich persönlich es für nutzlos, Kommentare zur C++-Syntax auf einem PR-Entwurf zu hinterlassen, und würde es als unhöflich empfinden, zu "macht das Sinn" zurückzukehren, nachdem der Autor mehr als 20 meiner Vorschläge zur Codeorganisation beantwortet hat.


Ihre Idee, dass sich eine gute Überprüfung auf das konzentrieren sollte, was zu einem bestimmten Zeitpunkt am dringendsten benötigt wird, deckt sich gut mit Jon Atacks Ratschlägen. Sie

schlägt eine Liste von Fragen vor, die Sie sich auf verschiedenen Ebenen des Überprüfungsprozesses stellen können, betont aber, dass diese Liste in keiner Weise erschöpfend ist und auch kein einfaches Rezept darstellt. Die Liste wird mit Beispielen aus der Praxis von GitHub illustriert.


### Finanzierung



Viele Leute arbeiten an der Bitcoin Open-Source-Entwicklung, entweder für Bitcoin Core oder für andere Projekte. Viele tun dies in ihrer Freizeit, ohne dafür eine Vergütung zu erhalten, aber einige Entwickler werden auch dafür bezahlt.


Unternehmen, Einzelpersonen und Organisationen, die ein Interesse am anhaltenden Erfolg von Bitcoin haben, können den Entwicklern Geld spenden, entweder direkt oder über Organisationen, die das Geld wiederum an einzelne Entwickler weitergeben. Es gibt auch eine Reihe von Unternehmen, die sich auf Bitcoin konzentrieren und qualifizierte Entwickler einstellen, damit diese Vollzeit an Bitcoin arbeiten können.


### Kulturschock



Man hat manchmal den Eindruck, dass es unter den Bitcoin-Entwicklern viele interne Streitereien und endlose hitzige Debatten gibt und dass sie nicht in der Lage sind, Entscheidungen zu treffen.


So wurde beispielsweise der Taproot-Einführungsmechanismus über einen langen Zeitraum hinweg diskutiert, in dem sich zwei "Lager" bildeten. Das eine wollte die Aufrüstung "scheitern" lassen, wenn die Bergleute nach einem bestimmten Zeitpunkt nicht mit überwältigender Mehrheit für die neuen Regeln gestimmt hatten, während das andere die Regeln nach diesem Zeitpunkt auf jeden Fall durchsetzen wollte. Michael Folkson fasst die Argumente der beiden Lager in einer [email](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-February/018380.html) an die Bitcoin-dev Mailingliste zusammen.


Die Debatte dauerte scheinbar ewig, und es war wirklich nicht abzusehen, dass sich in absehbarer Zeit ein Konsens in dieser Frage bilden würde. Das hat die Leute frustriert, und infolgedessen hat sich die Hitze verschärft. Gregory Maxwell (als Benutzer nullc) befürchtete [auf Reddit] (https://www.reddit.com/r/Bitcoin/comments/hrlpnc/technical_taproot_why_activate/fyqbn8s/?utm_source=share&utm_medium=web2x&context=3), dass die langwierigen Diskussionen das Upgrade weniger sicher machen würden:


> Zum jetzigen Zeitpunkt führt zusätzliches Warten nicht zu mehr Überprüfung und Gewissheit. Stattdessen wird durch die zusätzliche Verzögerung die Trägheit aufgeweicht und das Risiko möglicherweise etwas erhöht, da die Leute beginnen, Details zu vergessen, die Arbeit an der nachgelagerten Nutzung (wie die Unterstützung von Wallet) zu verzögern und nicht so viel zusätzlichen Überprüfungsaufwand zu investieren, wie sie es tun würden, wenn sie sich auf den Zeitrahmen für die Aktivierung verlassen könnten.

Schließlich wurde dieser Streit dank eines neuen Vorschlags von David Harding und Russel O'Connor mit dem Namen Speedy Trial beigelegt, der eine vergleichsweise kürzere Signalisierungszeit für Bergleute vorsah, um die Aktivierung von Taproot festzulegen oder schnell zu scheitern. Wenn sie es innerhalb dieses Zeitfensters aktivierten, würde Taproot etwa 6 Monate später bereitgestellt werden.


Jemand, der mit dem Entwicklungsprozess von Bitcoin nicht vertraut ist, würde wahrscheinlich denken, dass diese hitzigen Debatten furchtbar schlecht und sogar giftig aussehen. Es gibt mindestens zwei Faktoren, die sie in den Augen einiger Leute schlecht aussehen lassen:



- Im Vergleich zu Closed-Source-Unternehmen finden alle Debatten offen und unbearbeitet statt. Ein Softwareunternehmen wie Google würde seine Mitarbeiter niemals öffentlich über vorgeschlagene Funktionen diskutieren lassen, sondern höchstens eine Erklärung über die Haltung des Unternehmens zu diesem Thema veröffentlichen. Dies lässt die Unternehmen im Vergleich zu Bitcoin harmonischer erscheinen.
- Da Bitcoin genehmigungsfrei ist, kann jeder seine Meinung äußern. Das ist ein grundlegender Unterschied zu einem Closed-Source-Unternehmen, das nur eine Handvoll Leute mit einer Meinung hat, normalerweise Gleichgesinnte. Die Fülle an Meinungen, die innerhalb von Bitcoin geäußert werden, ist einfach überwältigend im Vergleich zu z.B. PayPal.


Die meisten Bitcoin-Entwickler würden argumentieren, dass diese Offenheit ein gutes und gesundes Umfeld schafft und dass sie sogar notwendig ist, um das beste Ergebnis zu erzielen.


Wie im Kapitel Bedrohung angedeutet, kann der zweite Punkt sehr vorteilhaft sein, hat aber auch eine Kehrseite. Ein Angreifer könnte Hinhaltetaktiken anwenden, wie sie im [Simple Sabotage Field Manual] (https://www.gutenberg.org/ebooks/26184) beschrieben sind, um den Entscheidungsfindungs- und Entwicklungsprozess zu verzerren.


Da Bitcoin Geld ist und Bitcoin Core unermessliche Mengen an Geld sichert, sollte man die Sicherheit in diesem Zusammenhang nicht auf die leichte Schulter nehmen. Aus diesem Grund haben erfahrene Bitcoin Core

die Entwickler könnten sehr Hard-lastig erscheinen, was in der Regel auch gerechtfertigt ist. In der Tat wird eine Funktion mit einer schwachen Begründung dahinter nicht akzeptiert werden. Das Gleiche würde passieren, wenn es die

reproduzierbare Builds zu erstellen, neue Abhängigkeiten hinzuzufügen oder wenn der Code nicht den [Best Practices] von Bitcoin folgte (https://github.com/Bitcoin/Bitcoin/blob/master/doc/developer-notes.md).


Neue (und alte) Entwickler können dadurch frustriert werden. Aber, wie bei Open-Source-Software üblich, können Sie jederzeit Fork das Repository, mergen, was Sie wollen, um Ihre eigene Fork, und bauen und führen Sie Ihre eigene Binärdatei.


### Fazit zu Open Source


Bitcoin Core und die meiste andere Bitcoin-Software ist Open Source, was bedeutet, dass es jedem freisteht, die Software nach Belieben zu verteilen, zu verändern und zu nutzen. Das Bitcoin Core-Repository auf GitHub ist derzeit der zentrale Punkt der Bitcoin-Entwicklung, aber dieser Status kann sich ändern, wenn die Menschen beginnen, den Betreuern oder der Website selbst zu misstrauen.


Open Source ermöglicht eine erlaubnisfreie Entwicklung in und auf Bitcoin. Ob Sie nun Code schreiben, Code überprüfen oder Protokolle erstellen - Open Source ermöglicht Ihnen dies, ob Sie pseudonom sind oder nicht.


Der Entwicklungsprozess rund um Bitcoin ist radikal offen, was dazu führen kann, dass Bitcoin wie ein toxischer und ineffizienter Ort aussieht, aber genau das macht Bitcoin widerstandsfähig gegen böswillige Akteure.


## Skalierung

<chapterId>bb3f3924-202c-5cdd-b2e9-e0c1cab0e48e</chapterId>



![](assets/scaling-banner.webp)



In diesem Kapitel untersuchen wir, ob Bitcoin skalierbar ist oder nicht. Wir beginnen damit, dass wir uns ansehen, wie die Menschen in der Vergangenheit über Skalierung nachgedacht haben. Anschließend werden im größten Teil dieses Kapitels verschiedene Ansätze zur Skalierung von Bitcoin erläutert, insbesondere die vertikale, horizontale, nach innen gerichtete und schichtweise Skalierung. Auf jede Beschreibung folgen Überlegungen darüber, ob der Ansatz das Wertversprechen von Bitcoin beeinträchtigt.


Im Bitcoin-Bereich wird das Wort "Skalierung" von verschiedenen Leuten unterschiedlich definiert. Einige verstehen darunter die Erhöhung der Blockchain-Transaktionskapazität, andere glauben, dass es gleichbedeutend mit einer effizienteren Nutzung des Blockchain ist, und wieder andere sehen es als die Entwicklung von Systemen auf der Grundlage des Bitcoin.


Im Zusammenhang mit Bitcoin und für die Zwecke dieses Buches definieren wir Skalierung als *Erhöhung der Nutzungskapazität von Bitcoin ohne Beeinträchtigung seiner Zensurresistenz*. Diese Definition umfasst mehrere Aspekte

zum Beispiel die Art der Änderungen:


- Weniger Bytes für Transaktionsinputs verwenden
- Verbesserung der Leistung der Unterschriftenprüfung
- Weniger Bandbreitenverbrauch im Peer-to-Peer-Netzwerk
- Batching von Transaktionen
- Mehrschichtige Architektur


Wir werden uns in Kürze mit den verschiedenen Ansätzen zur Skalierung befassen, doch zunächst ein kurzer Überblick über die Geschichte von Bitcoin im Zusammenhang mit der Skalierung.


### Geschichte der Skalierung



Die Skalierung ist seit der Genesis von Bitcoin ein zentraler Punkt der Diskussion. Der allererste Satz der [allerersten E-Mail] (https://www.metzdowd.com/pipermail/cryptography/2008-November/014814.html) als Reaktion auf die Ankündigung des Bitcoin-Whitepapers durch Satoshi auf der Kryptographie-Mailingliste handelte tatsächlich von Skalierung:


> Satoshi Nakamoto schrieb:
>

> "Ich habe an einem neuen elektronischen Bargeldsystem gearbeitet, das vollständig auf Peer-to-Peer-Basis arbeitet, ohne vertrauenswürdige Dritte.  Das Papier ist unter http://www.Bitcoin.org/Bitcoin.pdf verfügbar
>

> Wir brauchen ein solches System sehr, sehr dringend, aber so wie ich Ihren Vorschlag verstehe, scheint er nicht die erforderliche Größe zu haben.

Das Gespräch an sich ist vielleicht nicht sehr interessant oder genau, aber es zeigt, dass die Skalierung von Anfang an ein Anliegen war.


Die Diskussionen über die Skalierung erreichten ihren Höhepunkt um 2015-2017, als viele verschiedene Ideen darüber kursierten, ob und wie die maximale Blockgröße erhöht werden sollte. Dabei handelte es sich um eine eher uninteressante Diskussion über die Änderung eines Parameters im Quellcode, eine Änderung, die keine grundlegende Lösung brachte, sondern das Problem der Skalierung weiter in die Zukunft verschob und technische Schulden aufbaute.


Im Jahr 2015 fand in Montreal eine Konferenz mit dem Titel [Scaling Bitcoin] (https://scalingbitcoin.org/) statt, mit einer Folgekonferenz sechs Monate später in Hongkong und danach an einer Reihe anderer Orte auf der ganzen Welt. Im Mittelpunkt stand die Frage, wie Address skaliert werden kann. Viele Bitcoin-Entwickler und andere Enthusiasten kamen auf diesen Konferenzen zusammen, um verschiedene Skalierungsfragen und -vorschläge zu diskutieren. Die meisten dieser Diskussionen drehten sich nicht um die Erhöhung der Blockgröße, sondern um eher langfristige Lösungen.


Nach der Konferenz in Hongkong im Dezember 2015 fasste Gregory Maxwell [seinen Standpunkt] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-December/011865.html) zu vielen der diskutierten Themen zusammen und begann mit einer allgemeinen Skalierungsphilosophie:


> Mit der verfügbaren Technologie gibt es grundlegende Kompromisse zwischen Größe und Dezentralisierung. Wenn das System zu kostspielig ist, werden die Menschen gezwungen sein, Dritten zu vertrauen, anstatt die Regeln des Systems unabhängig durchzusetzen. Wenn der Ressourcenverbrauch von Bitcoin Blockchain im Vergleich zur verfügbaren Technologie zu groß ist, verliert Bitcoin seine Wettbewerbsvorteile gegenüber den alten Systemen, weil die Validierung zu kostspielig ist (und viele Nutzer ausschließt), wodurch das Vertrauen in das System zurückgedrängt wird.  Wenn die Kapazität zu gering und unsere Transaktionsmethoden zu ineffizient sind, wird der Zugang zur Kette zur Beilegung von Streitigkeiten zu kostspielig sein, was wiederum das Vertrauen in das System zurückdrängt.

Er spricht über den Zielkonflikt zwischen Durchsatz und Dezentralisierung. Wenn Sie größere Blöcke zulassen, werden Sie einige Leute aus dem Netzwerk verdrängen, weil sie nicht mehr die Ressourcen haben, um die Blöcke zu validieren. Wenn der Zugang zu den Blöcken jedoch teurer wird, können es sich weniger Leute leisten, sie als Streitbeilegungsmechanismus zu nutzen. In beiden Fällen werden die Nutzer zu vertrauenswürdigen Diensten gedrängt.


Er fährt fort mit einer Zusammenfassung der vielen auf der Konferenz vorgestellten Ansätze zur Skalierung. Dazu gehören rechnerisch effizientere Signaturüberprüfungen, *segregierte Zeugen* einschließlich einer Änderung der Blockgrößenbegrenzung, ein platzsparenderer Mechanismus zur Blockweitergabe und der Aufbau von Protokollen auf Bitcoin in Schichten. Viele dieser

ansätze wurden inzwischen umgesetzt.


### Ansätze zur Skalierung



Wie bereits angedeutet, muss es bei der Skalierung von Bitcoin nicht unbedingt darum gehen, die Blockgröße oder andere Grenzen zu erhöhen. Wir gehen nun einige allgemeine Ansätze zur Skalierung durch, von denen einige nicht unter dem im vorherigen Abschnitt erwähnten Kompromiss zwischen Durchsatz und Dezentralisierung leiden.


#### Vertikale Skalierung



Vertikale Skalierung ist der Prozess der Erhöhung der Rechenressourcen der Maschinen, die Daten verarbeiten. Im Zusammenhang mit Bitcoin wären dies die Vollknoten, d. h. die Maschinen, die Blockchain im Namen ihrer Nutzer validieren.


Die am häufigsten diskutierte Technik für die vertikale Skalierung in Bitcoin ist die Anhebung der Blockgrößengrenze. Dies würde bedeuten, dass einige Vollknoten ihre Hardware aufrüsten müssten, um mit den steigenden Rechenanforderungen Schritt zu halten. Der Nachteil ist, dass dies auf Kosten der Zentralisierung geschieht.


Neben den negativen Auswirkungen auf die Dezentralisierung von Full node könnte sich die vertikale Skalierung auch auf weniger offensichtliche Weise negativ auf die Dezentralisierung und Sicherheit von Bitcoin auswirken. Schauen wir uns einmal an, wie Miner arbeiten "sollten". Angenommen, ein Miner schürft einen Block der Höhe 7 und veröffentlicht diesen Block im Bitcoin-Netzwerk. Es wird einige Zeit dauern, bis dieser Block eine breite Akzeptanz findet, was hauptsächlich auf zwei Faktoren zurückzuführen ist:


- Die Übertragung des Blocks zwischen den Peers nimmt aufgrund von Bandbreitenbeschränkungen Zeit in Anspruch.
- Die Validierung des Blocks braucht Zeit.


Während Block 7 durch das Netzwerk propagiert wird, befinden sich viele Miner immer noch auf Mining auf Höhe von Block 6, weil sie Block 7 noch nicht erhalten und validiert haben. Wenn einer dieser Schürfer während dieser Zeit einen neuen Block auf Höhe 7 findet, gibt es zwei konkurrierende Blöcke auf dieser Höhe. Es kann nur einen Block in Höhe 7 (oder einer anderen Höhe) geben, was bedeutet, dass einer der beiden Kandidaten veraltet sein muss.


Kurz gesagt, veraltete Blöcke treten auf, weil jeder Block Zeit braucht, um sich zu verbreiten, und je länger die Verbreitung dauert, desto höher ist die Wahrscheinlichkeit veralteter Blöcke.


Angenommen, die Begrenzung der Blockgröße wird aufgehoben und die durchschnittliche Blockgröße nimmt erheblich zu. Die Blöcke würden sich dann aufgrund von Bandbreitenbeschränkungen und Überprüfungszeiten langsamer über das Netz verbreiten. Eine längere Übertragungszeit erhöht auch die Wahrscheinlichkeit, dass Blöcke veraltet sind.


Bergleute mögen es nicht, wenn ihre Blöcke blockiert werden, weil sie dann ihre Block reward verlieren, also tun sie alles, um dies zu vermeiden

szenario. Zu den Maßnahmen, die sie ergreifen können, gehören:



- Aufschieben der Validierung eines eingehenden Blocks, auch bekannt als *validationless Mining*. Miner können einfach den Proof-of-Work des Block-Headers überprüfen und darauf aufbauen, während sie in der Zwischenzeit den vollständigen Block herunterladen und validieren.
- Anschluss an einen Mining pool mit größerer Bandbreite und Konnektivität.


Der Mining ohne Validierung untergräbt die Dezentralisierung des Full node weiter, da der Miner zumindest vorübergehend auf eingehende Blöcke vertraut. Auch die Sicherheit wird in gewissem Maße beeinträchtigt, da ein Teil der Rechenleistung des Netzwerks potenziell auf einem ungültigen Blockchain aufbaut, anstatt auf der stärksten und gültigen Kette.


Der zweite Punkt wirkt sich negativ auf die Dezentralisierung von Miner aus, da die Pools mit der besten Netzwerkanbindung und Bandbreite in der Regel auch die größten sind, was dazu führt, dass sich die Miner auf einige wenige große Pools konzentrieren.


#### Horizontale Skalierung



Die horizontale Skalierung bezieht sich auf Techniken, bei denen die Arbeitslast auf mehrere Rechner aufgeteilt wird. Dies ist zwar ein weit verbreiteter Skalierungsansatz bei beliebten Websites und Datenbanken, aber in Bitcoin ist dies nicht so einfach möglich.


Viele Leute bezeichnen diesen Bitcoin-Skalierungsansatz als *sharding*. Im Grunde besteht er darin, dass jeder Full node nur einen Teil des Blockchain verifiziert. Peter Todd hat sich viele Gedanken über das Konzept des Sharding gemacht. Er hat einen [Blog-Beitrag] (https://petertodd.org/2015/why-scaling-Bitcoin-with-sharding-is-very-Hard) geschrieben, in dem er Sharding in allgemeiner Form erklärt und auch seine eigene Idee namens *Treechains* vorstellt. Der Artikel ist schwierig zu lesen, aber Todd macht einige Punkte, die recht gut verdaulich sind:


> In Scherbensystemen funktioniert die "Full node-Verteidigung" nicht, zumindest nicht direkt. Der springende Punkt ist, dass nicht jeder alle Daten hat, also muss man entscheiden, was passiert, wenn sie nicht verfügbar sind.

Dann stellt er verschiedene Ideen vor, wie man das Sharding oder die horizontale Skalierung angehen kann. Gegen Ende des Beitrags kommt er zum Schluss:


> Es gibt allerdings ein großes Problem: Heiliger Bimbam, das ist im Vergleich zu Bitcoin sehr komplex! Selbst die "Kinder"-Version von Sharding - mein Linearisierungsschema anstelle von zk-SNARKS - ist wahrscheinlich ein oder zwei Größenordnungen komplexer als die Verwendung des Bitcoin-Protokolls im Moment, und dennoch scheint ein großer Teil der Unternehmen in diesem Bereich die Hände hochzuwerfen und stattdessen zentralisierte API-Anbieter zu verwenden. Es wird nicht einfach sein, das oben Genannte tatsächlich zu implementieren und es in die Hände der Endnutzer zu bekommen.
>

> Andererseits ist die Dezentralisierung nicht billig: Die Verwendung von PayPal ist um eine oder zwei Größenordnungen einfacher als das Bitcoin-Protokoll.

Die Schlussfolgerung, die er zieht, ist, dass Sharding technisch möglich sein *könnte*, aber es würde den Preis einer enormen Komplexität mit sich bringen. Angesichts der Tatsache, dass viele Nutzer Bitcoin bereits zu komplex finden und stattdessen lieber zentralisierte Dienste nutzen, wird es Hard sein, sie davon zu überzeugen, etwas noch Komplexeres zu nutzen.


#### Interne Skalierung



Während sich die horizontale und vertikale Skalierung in zentralisierten Systemen wie Datenbanken und Webservern in der Vergangenheit bewährt hat, scheinen sie für ein dezentrales Netzwerk wie Bitcoin aufgrund ihrer zentralisierenden Wirkung nicht geeignet zu sein.


Ein Ansatz, der viel zu wenig gewürdigt wird, ist das, was wir als *inward scaling* bezeichnen können, was übersetzt so viel bedeutet wie "mit weniger mehr erreichen". Es bezieht sich auf die kontinuierliche Arbeit vieler Entwickler, die bereits vorhandenen Algorithmen zu optimieren, so dass wir innerhalb der bestehenden Grenzen des Systems mehr erreichen können.


Die Verbesserungen, die durch die Skalierung nach innen erreicht wurden, sind, gelinde gesagt, beeindruckend. Um Ihnen eine allgemeine Vorstellung von den Verbesserungen im Laufe der Jahre zu geben, hat Jameson Lopp [Benchmark-Tests] (https://blog.lopp.net/Bitcoin-core-performance-evolution/) zur Blockchain-Synchronisierung durchgeführt und dabei viele verschiedene Versionen von Bitcoin Core bis zurück zu Version 0.8 verglichen.


![](assets/Bitcoin-Core-Sync-Performance-1.webp)


Leistung beim anfänglichen Herunterladen von Blöcken bei verschiedenen Versionen von Bitcoin Core. Auf der Y-Achse ist die synchronisierte Blockhöhe und auf der X-Achse die Zeit, die für die Synchronisierung mit dieser Höhe benötigt wurde


Die verschiedenen Zeilen stehen für unterschiedliche Versionen von Bitcoin Core. Die Linie ganz links ist die neueste, d. h. Version 0.22, die im September 2021 veröffentlicht wurde und 396 Minuten für die vollständige Synchronisierung benötigte. Die ganz rechte Linie ist die Version 0.8 vom November 2013, die 3452 Minuten benötigte. Die gesamte - etwa 10-fache - Verbesserung ist auf die Skalierung nach innen zurückzuführen.


Die Verbesserungen können entweder als Platzeinsparung (RAM, Festplatte, Bandbreite usw.) oder als Einsparung von Rechenleistung kategorisiert werden. Beide Kategorien tragen zu den Verbesserungen im obigen Diagramm bei.


Ein gutes Beispiel für eine rechnerische Verbesserung findet sich in der Bibliothek [libsecp256k1](https://github.com/Bitcoin-core/secp256k1), die unter anderem die kryptografischen Primitive implementiert, die zur Erstellung und Überprüfung digitaler Signaturen benötigt werden. Pieter Wuille ist einer der Mitwirkenden an dieser Bibliothek und er hat einen [Twitter-Thread](https://twitter.com/pwuille/status/1450471673321381896) geschrieben, in dem er die Leistungsverbesserungen aufzeigt, die durch verschiedene Pull-Requests erreicht wurden.


![](assets/libsecp256k1speedups.webp)


Leistung der Unterschriftenprüfung im Laufe der Zeit, mit Markierung der wichtigsten Pull Requests auf der Zeitachse


Das Diagramm zeigt den Trend für zwei verschiedene 64-Bit-CPU-Typen, nämlich ARM und x86. Der Leistungsunterschied ist darauf zurückzuführen, dass die x86-Architektur mehr spezialisierte Befehle bietet als die ARM-Architektur, die weniger und allgemeinere Befehle hat. Der allgemeine Trend ist jedoch für beide Architekturen derselbe. Beachten Sie, dass die Y-Achse logarithmisch ist, was die Verbesserungen weniger beeindruckend erscheinen lässt, als sie tatsächlich sind.


Es gibt auch mehrere gute Beispiele für platzsparende Verbesserungen, die zur Leistungssteigerung beigetragen haben. In einer

[Medium-Blogpost] (https://murchandamus.medium.com/2-of-3-Multisig-inputs-using-Pay-to-Taproot-d5faf2312ba3) über den Beitrag von Taproot zur Platzersparnis vergleicht Benutzer Murch, wie viel Blockspeicherplatz eine 2-von-3-Schwellenwert-Signatur benötigen würde, wobei er Taproot auf verschiedene Arten verwendet und es überhaupt nicht einsetzt.


![](assets/murch-taproot.webp)


Platzersparnis für verschiedene Ausgabentypen, Taproot und ältere Versionen.


Ein 2-von-3 Multisig mit nativem SegWit würde insgesamt 104,5+43 vB = 147,5 vB benötigen, während die platzsparendste Verwendung von Taproot im Standardfall nur 57,5+43 vB = 100,5 vB erfordern würde. Im schlimmsten Fall und in seltenen Fällen, z. B. wenn ein Standardunterzeichner aus irgendeinem Grund nicht verfügbar ist, würde Taproot 107,5+43 vB = 150,5 vB benötigen. Sie müssen nicht alle Details verstehen, aber dies sollte Ihnen eine Vorstellung davon vermitteln, wie Entwickler über Platzeinsparungen denken - jedes kleine Byte zählt.


Abgesehen von der Skalierung nach innen in der Bitcoin-Software gibt es einige Möglichkeiten, wie die Nutzer ebenfalls zur Skalierung nach innen beitragen können. Sie können ihre Transaktionen intelligenter gestalten, um Transaktionsgebühren zu sparen und gleichzeitig ihren Fußabdruck auf Full node Anforderungen zu verringern. Zwei häufig genutzte Techniken zur Erreichung dieses Ziels sind das Transaktions-Batching und die Ausgabekonsolidierung.


Die Idee beim Transaktions-Batching ist, mehrere Zahlungen in einer einzigen Transaktion zusammenzufassen, anstatt eine Transaktion pro Zahlung durchzuführen. Dadurch können Sie eine Menge Gebühren sparen und gleichzeitig die Belastung des Blockraums verringern.


![](assets/tx-batching.webp)


Bei der Bündelung von Transaktionen werden mehrere Zahlungen zu einer einzigen Transaktion zusammengefasst, um Gebühren zu sparen.


Unter Output-Konsolidierung versteht man das Ausnutzen von Zeiten mit geringer Nachfrage nach Blockspace, um mehrere Outputs zu einem einzigen Output zusammenzufassen. Dadurch können Sie später, wenn Sie eine Zahlung leisten müssen, während die Nachfrage nach Blockspace hoch ist, Ihre Gebührenkosten senken.


![](assets/utxo-consolidation.webp)


Ausgabekonsolidierung: Verschmelzen Sie Ihre Münzen zu einer großen Münze, wenn die Gebühren niedrig sind, um später Gebühren zu sparen.


Es mag nicht offensichtlich sein, wie die Konsolidierung des Outputs zur Skalierung nach innen beiträgt. Immerhin wird die Gesamtmenge der Blockchain-Daten durch diese Methode sogar leicht erhöht. Nichtsdestotrotz schrumpft der UTXO-Satz, d. h. die Datenbank, die festhält, wem welche Münzen gehören, weil man mehr UTXOs ausgibt als man schafft. Dies entlastet die vollen Knotenpunkte bei der Pflege ihrer UTXO-Sets.


Leider können diese beiden Techniken der *UTXO-Verwaltung* für Ihre eigene Privatsphäre oder die Ihrer Zahlungsempfänger von Nachteil sein. Bei der Bündelung weiß jeder Empfänger, dass alle gebündelten Ausgaben von Ihnen an andere Empfänger gehen (außer vielleicht die Änderung). Im Fall der UTXO-Konsolidierung werden Sie offenlegen, dass die von Ihnen konsolidierten Nachrichten zur gleichen Wallet gehören. Sie müssen also möglicherweise einen Kompromiss zwischen Kosteneffizienz und Datenschutz eingehen.


#### Gestufte Skalierung



Der wirkungsvollste Ansatz zur Skalierung ist wahrscheinlich die Schichtung. Die allgemeine Idee hinter der Schichtung ist, dass ein Protokoll Zahlungen zwischen Nutzern abwickeln kann, ohne dass dem Blockchain weitere Transaktionen hinzugefügt werden.


Ein mehrstufiges Protokoll beginnt damit, dass sich zwei oder mehr Personen auf eine Starttransaktion einigen, die auf den Blockchain übertragen wird, wie in der folgenden Abbildung dargestellt.


![](assets/scaling-layer.webp)

Ein typisches Layer 2-Protokoll auf der Grundlage von Bitcoin, Layer 1.


Die Art und Weise, wie diese Starttransaktion erstellt wird, ist bei den verschiedenen Protokollen unterschiedlich, aber ein gemeinsames Thema ist, dass die Teilnehmer eine unsignierte Starttransaktion und eine Reihe von vorsignierten Bestrafungstransaktionen erstellen, die die Ausgabe der Starttransaktion auf verschiedene Weise verwenden. Anschließend wird die Starttransaktion vollständig signiert und im Blockchain veröffentlicht, und die Bestrafungstransaktionen können vollständig signiert und veröffentlicht werden, um eine sich falsch verhaltende Partei zu bestrafen. Dies schafft Anreize für die Teilnehmer, ihre Versprechen einzuhalten, so dass das Protokoll auf eine Trustless Weise funktionieren kann.


Sobald die Starttransaktion auf dem Blockchain läuft, kann das Protokoll tun, was es tun soll. Zum Beispiel könnte es superschnelle Zahlungen zwischen Teilnehmern durchführen, einige Techniken zur Verbesserung der Privatsphäre implementieren oder fortgeschrittene Skripte verwenden, die vom Bitcoin nicht unterstützt werden.


Wir werden nicht im Detail darauf eingehen, wie bestimmte Protokolle funktionieren, aber wie Sie in der vorherigen Abbildung sehen können, wird der Blockchain während des Lebenszyklus des Protokolls nur selten verwendet. Die ganze pikante Action passiert *off-chain*. Wir haben gesehen, dass dies ein Gewinn für den Datenschutz sein kann, wenn es richtig gemacht wird, aber es kann auch ein Vorteil für die Skalierbarkeit sein.


In einem [Reddit-Beitrag] (https://www.reddit.com/r/Bitcoin/comments/438hx0/a_trip_to_the_moon_requires_a_rocket_with/) mit dem Titel "Eine Reise zum Mond erfordert eine Rakete mit mehreren Stufen, sonst frisst die Raketengleichung dein Mittagessen... alle im Clownsauto-Stil in ein Trebuchet zu packen und auf den Erfolg zu hoffen, ist nicht möglich", erklärt Gregory Maxwell, warum die Schichtung unsere beste Chance ist, Bitcoin um Größenordnungen zu vergrößern.


Er beginnt damit, dass er betont, dass es ein Irrtum ist, Visa oder Mastercard als Hauptkonkurrenten von Bitcoin zu betrachten, und betont, dass die Erhöhung der maximalen Blockgröße ein schlechter Ansatz ist, um dieser Konkurrenz zu begegnen. Dann spricht er darüber, wie man durch den Einsatz von Schichten einen echten Unterschied machen kann:


> Heißt das also, dass Bitcoin als Zahlungstechnologie nicht der große Gewinner sein kann? Nein. Aber um die Art von Kapazität zu erreichen, die erforderlich ist, um den Zahlungsbedarf der Welt zu decken, müssen wir intelligenter arbeiten.
>

> Von Anfang an war Bitcoin so konzipiert, dass es durch seine intelligente Vertragsabwicklung Schichten auf sichere Weise einbezieht (glauben Sie, das wurde nur eingebaut, damit die Leute über bedeutungslose "DAOs" philosophieren können?) In der Tat werden wir das Bitcoin-System als einen hochgradig zugänglichen und absolut vertrauenswürdigen Roboterrichter verwenden und die meisten unserer Geschäfte außerhalb des Gerichtssaals abwickeln - aber so, dass wir, wenn etwas schief geht, alle Beweise und etablierten Vereinbarungen haben, so dass wir darauf vertrauen können, dass das Robotergericht es in Ordnung bringen wird. (Geek-Sidebar: Wenn dies unmöglich erscheint, lesen Sie diesen alten Beitrag über Transaktions-Cut-Through)
>

> Dies ist gerade wegen der Kerneigenschaften von Bitcoin möglich. Ein zensierbares oder reversibles Basissystem ist nicht sehr geeignet, um darauf eine leistungsfähige obere Layer-Transaktionsverarbeitung aufzubauen... und wenn der zugrunde liegende Vermögenswert nicht solide ist, hat es wenig Sinn, überhaupt mit ihm zu handeln.

Die Analogie mit der Richterin veranschaulicht sehr gut, wie die Schichtung funktioniert: Diese Richterin muss unbestechlich sein und darf nie ihre Meinung ändern, sonst funktionieren die Schichten über Bitcoins Basis Layer nicht zuverlässig.


Er fährt fort, indem er einen Punkt über zentralisierte Dienste anspricht. Es ist in der Regel kein Problem, einem zentralen Server mit trivialen Mengen von Bitcoin zu vertrauen, um Dinge zu erledigen: Das ist auch geschichtete Skalierung.


Viele Jahre sind vergangen, seit Maxwell den obigen Artikel geschrieben hat, und seine Worte sind immer noch richtig. Der Erfolg des Lightning Network beweist, dass die Schichtung in der Tat ein Weg nach vorne ist, um den Nutzen des Bitcoin zu erhöhen.



### Schlussfolgerung zur Skalierung



Wir haben verschiedene Möglichkeiten erörtert, wie man Bitcoin skalieren und die Nutzungskapazität von Bitcoin erhöhen kann. Die Skalierung ist seit den Anfängen von Bitcoin ein Thema.


Wir wissen heute, dass Bitcoin nicht vertikal ("größere Hardware kaufen") oder horizontal ("nur Teile der Daten überprüfen") skalierbar ist, sondern eher nach innen ("mit weniger mehr erreichen") und in Schichten ("Protokolle auf Bitcoin aufbauen").


## Wenn die Kacke am Dampfen ist

<chapterId>fe39c13c-310f-51fd-84ff-6b92dd01c9e7</chapterId>



![](assets/shtf-banner.webp)

Bitcoin wird von Menschen gebaut. Menschen schreiben die Software, und Menschen führen diese Software dann aus. Wenn eine Sicherheitslücke oder ein schwerwiegender Fehler entdeckt wird - gibt es da wirklich einen Unterschied zwischen diesen beiden? - wird sie immer von Menschen entdeckt, von Menschen aus Fleisch und Blut. Dieses Kapitel befasst sich mit der Frage, was Menschen tun, tun sollten und nicht tun sollten, wenn die Kacke am Dampfen ist. Im ersten Abschnitt wird der Begriff *responsible disclosure* erklärt, der sich darauf bezieht, wie jemand, der eine Schwachstelle entdeckt, verantwortungsbewusst handeln kann, um den Schaden zu minimieren. Der Rest des Kapitels nimmt Sie mit auf einen Rundgang durch einige der schwerwiegendsten Sicherheitslücken, die im Laufe der Jahre entdeckt wurden, und wie Entwickler, Miner und Benutzer mit ihnen umgingen. Die Dinge waren in der frühen Kindheit von Bitcoin nicht so rigoros wie sie es heute sind.


### Verantwortungsvolle Offenlegung



Stellen Sie sich vor, Sie entdecken einen Fehler in Bitcoin Core, einen Fehler, der es jedem ermöglicht, einen Bitcoin Core-Knoten aus der Ferne herunterzufahren, indem er einige speziell gestaltete Netzwerknachrichten verwendet. Stellen Sie sich vor, Sie sind nicht bösartig und möchten, dass dieses Problem nicht ausgenutzt wird. Was tun Sie dann? Wenn Sie darüber schweigen, wird wahrscheinlich jemand anderes das Problem entdecken, und Sie können nicht sicher sein, dass diese Person nicht bösartig ist.


Wenn ein Sicherheitsproblem entdeckt wird, sollte die Person, die es entdeckt, _responsible disclosure_ anwenden, ein Begriff, der unter Bitcoin-Entwicklern häufig verwendet wird. Der Begriff ist [erklärt auf Wikipedia] (https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure):


> Die Entwickler von Hardware und Software benötigen oft Zeit und Ressourcen, um ihre Fehler zu beheben. Oft sind es ethische Hacker, die diese Fehler finden
schwachstellen. Hacker und Computer-Sicherheitswissenschaftler sind der Meinung, dass es ihre soziale Verantwortung ist, die Öffentlichkeit auf Schwachstellen aufmerksam zu machen. Das Verstecken von Problemen könnte ein Gefühl falscher Sicherheit hervorrufen. Um dies zu vermeiden, stimmen sich die beteiligten Parteien ab und vereinbaren einen angemessenen Zeitraum für die Behebung der Sicherheitslücke. Je nach den potenziellen Auswirkungen der Schwachstelle, der voraussichtlichen Zeit, die für die Entwicklung und Anwendung einer Notlösung oder eines Workarounds benötigt wird, und anderen Faktoren kann dieser Zeitraum zwischen einigen Tagen und mehreren Monaten variieren.


Das heißt, wenn Sie ein Sicherheitsproblem finden, sollten Sie dies dem für das System zuständigen Team melden. Aber was bedeutet das im Zusammenhang mit Bitcoin? Niemand kontrolliert Bitcoin, aber es gibt derzeit einen zentralen Punkt für die Entwicklung von Bitcoin, nämlich das [Bitcoin Core Github Repository] (https://github.com/Bitcoin/Bitcoin). Die Betreuer dieses Repositorys sind für den darin enthaltenen Code verantwortlich, aber sie sind nicht für das System als Ganzes verantwortlich - das ist niemand. Nichtsdestotrotz ist es die beste Praxis, eine E-Mail an security@bitcoincore.org zu schicken.


In einem [E-Mail-Thread] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/015002.html) mit dem Titel "Responsible disclosure of bugs" (Verantwortungsvolle Offenlegung von Fehlern) aus dem Jahr 2017 versuchte Anthony Towns zusammenzufassen, was seiner Meinung nach die derzeit besten Praktiken sind. Er hatte Beiträge aus mehreren Quellen und von verschiedenen Personen gesammelt, um seine Ansicht zu diesem Thema zu untermauern.




- Schwachstellen sollten über security at bitcoincore.org gemeldet werden
- Ein kritisches Problem (das sofort ausgenutzt werden kann oder bereits ausgenutzt wird und großen Schaden anrichtet) wird wie folgt behandelt:
  - einen so schnell wie möglich veröffentlichten Patch
  - umfassende Benachrichtigung über die Notwendigkeit eines Upgrades (oder der Deaktivierung betroffener Systeme)
  - minimale Offenlegung des eigentlichen Problems, um Angriffe zu verzögern
- Eine unkritische Schwachstelle (weil sie nur schwer oder mit hohem Aufwand auszunutzen ist) wird durch die folgenden Maßnahmen behoben:
  - patch und Überprüfung im Rahmen des normalen Entwicklungsprozesses
  - rückport einer Korrektur oder eines Workarounds von der Master-Version in die aktuell veröffentlichte Version
- Die Entwickler versuchen sicherzustellen, dass die Veröffentlichung des Fixes die Art der Schwachstelle nicht verrät, indem sie erfahrenen Entwicklern, die nicht über die Schwachstelle informiert wurden, den vorgeschlagenen Fix zur Verfügung stellen, ihnen mitteilen, dass er eine Schwachstelle behebt, und sie bitten, die Schwachstelle zu identifizieren.
- Die Entwickler können anderen Bitcoin-Implementierungen empfehlen, Schwachstellen zu beheben, bevor die Lösung veröffentlicht und weit verbreitet wird, wenn sie dies tun können, ohne die Schwachstelle zu offenbaren; z. B. wenn die Lösung erhebliche Leistungsvorteile hat, die ihre Einbeziehung rechtfertigen würden.
- Bevor eine Schwachstelle bekannt wird, empfehlen die Entwickler befreundeten Altcoin-Entwicklern in der Regel, dass sie sich um die Behebung kümmern sollten. Dies geschieht jedoch erst, nachdem die Korrekturen im Bitcoin-Netzwerk weit verbreitet sind.
- Die Entwickler werden im Allgemeinen keine Altcoin-Entwickler benachrichtigen, die sich feindselig verhalten haben (z. B. Sicherheitslücken nutzen, um andere anzugreifen, oder die Embargos verletzen).
- Die Entwickler von Bitcoin werden keine Details zu den Sicherheitslücken veröffentlichen, bis >80 % der Bitcoin-Knoten die Korrekturen implementiert haben. Die Entdecker von Schwachstellen werden ermutigt und aufgefordert, dieselbe Politik zu verfolgen. [1] [6]


Diese Liste zeigt, wie vorsichtig man sein muss, wenn man Patches für Bitcoin veröffentlicht, da der Patch selbst die Sicherheitslücke verraten könnte. Der vierte Aufzählungspunkt ist besonders interessant, da er erklärt, wie man testen kann, ob ein Patch gut genug getarnt wurde. Wenn nämlich ein paar wirklich erfahrene Entwickler die Schwachstelle nicht erkennen können, obwohl sie wissen, dass der Patch eine Schwachstelle behebt, wird es für andere wahrscheinlich wirklich Hard sein, sie zu entdecken.


In dem Thread, der zu dieser E-Mail führte, wurde diskutiert, ob, wann und wie Schwachstellen in Altcoins und anderen Implementierungen von Bitcoin offengelegt werden sollten. Hier gibt es keine klare Antwort. "Den Guten zu helfen" scheint das Vernünftigste zu sein, aber wer entscheidet, wer das ist und wo zieht man die Grenze? Bryan Bishop [argumentierte](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014983.html), dass es eine moralische Pflicht sei, Altcoins und sogar Scamcoins dabei zu helfen, sich gegen Sicherheitslücken zu verteidigen:


> Es reicht nicht aus, Bitcoin und seine Benutzer vor aktiven Bedrohungen zu schützen, sondern es besteht eine allgemeinere Verantwortung, alle Arten von Benutzern und verschiedene Software vor vielen Arten von Bedrohungen in jeglicher Form zu schützen, selbst wenn die Leute dumme und unsichere Software verwenden, die Sie persönlich nicht betreuen oder zu der Sie nicht beitragen oder für die Sie eintreten. Der Umgang mit dem Wissen um eine Sicherheitslücke ist eine heikle Angelegenheit, und Sie könnten Erkenntnisse erhalten, die schwerwiegendere direkte oder indirekte Auswirkungen haben als ursprünglich beschrieben.

Der obigen E-Mail von Town ging auch ein [Beitrag] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014977.html) von Gregory Maxwell voraus, in dem er argumentierte, dass Sicherheitslücken schwerwiegender sein könnten, als sie erscheinen:


> Ich habe mehrfach erlebt, wie sich ein Hard-Problem als trivial herausstellte, wenn man den richtigen Trick fand, oder wie sich ein kleines Dos-Problem als weitaus schwerwiegender erwies.
>

> Einfache Leistungsfehler, die geschickt eingesetzt werden, können potenziell dazu verwendet werden, das Netzwerk aufzuteilen - Miner A und Exchange B gehen in eine Partition, alle anderen in eine andere... und verdoppeln.
>

> Und so weiter.  Ich stimme zwar absolut zu, dass verschiedene Dinge unterschiedlich gehandhabt werden sollten und können, aber es ist nicht immer so eindeutig. Es ist ratsam, Dinge als schwerwiegender zu behandeln, als man sie kennt.

Selbst wenn also eine Sicherheitslücke scheinbar Hard ausgenutzt werden kann, ist es am besten, davon auszugehen, dass sie leicht ausnutzbar ist und Sie nur noch nicht herausgefunden haben, wie.


Er erwähnt auch, dass "es nicht ganz richtig ist, diesen Thread als Offenlegung zu bezeichnen, denn es geht hier nicht um Offenlegung. Offenlegung ist, wenn man den Verkäufer informiert.  In diesem Thread geht es um die Veröffentlichung, und das hat ganz andere Auswirkungen. Veröffentlichung ist, wenn man sicher ist, dass man es den potenziellen Angreifern gesagt hat". Diese letzte Bemerkung zur Unterscheidung zwischen Offenlegung und Veröffentlichung ist sehr wichtig. Der einfache Teil ist die verantwortungsvolle Offenlegung; der Hard-Teil ist die vernünftige Veröffentlichung.


### Die traumatische Kindheit von Bitcoin



Bitcoin war ursprünglich ein Ein-Mann-Projekt (zumindest lässt das Pseudonym seines Schöpfers darauf schließen), und Bitcoin hatte anfangs wenig bis gar keinen Wert. Daher wurden Schwachstellen und Fehlerbehebungen nicht so rigoros gehandhabt wie heute.


Das Bitcoin-Wiki enthält eine [Liste der gemeinsamen Schwachstellen und Gefährdungen](https://en.Bitcoin.it/wiki/Common_Vulnerabilities_and_Exposures) (CVEs), die Bitcoin durchlaufen hat. Dieser Abschnitt stellt ein kleines Exposé einiger Sicherheitsprobleme und Vorfälle aus den ersten Jahren von Bitcoin dar. Wir werden nicht auf alle eingehen, aber wir haben einige ausgewählt, die wir besonders interessant finden.


#### 2010-07-28: Die Münzen anderer ausgeben (CVE-2010-5141)



Am 28. Juli 2010 entdeckte eine pseudonyme Person namens ArtForz einen Fehler in Version 0.3.4, der es jedem ermöglichte, Münzen von jedem anderen zu nehmen. ArtForz meldete dies *verantwortlich* an Satoshi Nakamoto und an einen anderen Bitcoin-Entwickler namens Gavin Andresen.


Das Problem war, dass der Skriptoperator `OP_RETURN` die Programmausführung einfach beenden würde. Wenn also der scriptPubKey `<pubkey> OP_CHECKSIG` und scriptSig `OP_1 OP_RETURN` wäre, würde der Teil des Programms im scriptPubKey niemals ausgeführt werden. Das Einzige, was passieren würde, wäre, dass `1` auf den Stack gelegt würde und dann würde `OP_RETURN` das Programm beenden. Jeder Wert ungleich Null oben auf dem Stack, nachdem das Programm ausgeführt wurde, bedeutet, dass die Ausgabebedingung erfüllt ist. Da das oberste Stackelement `1` nicht Null ist, wäre die Ausgabe in Ordnung.


Dies war der Code für die Behandlung von `OP_RETURN`:


```
case OP_RETURN:
{
pc = pend;
}
break;
```

Der Effekt von `pc = pend;` war, dass der Rest des Programms übersprungen wurde, was bedeutete, dass jedes sperrende Skript in scriptPubKey ignoriert wurde. Die Korrektur bestand darin, die Bedeutung von `OP_RETURN` so zu ändern, dass es stattdessen sofort fehlschlug.


```
case OP_RETURN:
{
return false;
}
break;
```


Satoshi nahm diese Änderung lokal vor und erstellte daraus eine ausführbare Binärdatei mit der Version 0.3.5. Dann postete er im Bitcointalk-Forum `*** ALERT \*** Upgrade to 0.3.5 ASAP` und forderte die Nutzer auf, diese Binärversion von ihm zu installieren, ohne den Quellcode dafür zu präsentieren:


> Bitte aktualisieren Sie so schnell wie möglich auf 0.3.5!  Wir haben einen Implementierungsfehler behoben, bei dem es möglich war, dass gefälschte Transaktionen akzeptiert werden konnten.  Akzeptieren Sie keine Bitcoin-Transaktionen als Zahlung, bis Sie auf Version 0.3.5 aktualisiert haben!

Die ursprüngliche Nachricht wurde später bearbeitet und ist nicht mehr in ihrer vollständigen Form verfügbar. Der obige Ausschnitt stammt aus einer [Zitatantwort] (https://bitcointalk.org/index.php?topic=626.msg6458#msg6458). Einige Benutzer probierten das Binary von Satoshi aus, stießen aber auf Probleme damit. Kurze Zeit später schrieb [Satoshi](https://bitcointalk.org/index.php?topic=626.msg6469#msg6469):


> Ich hatte noch keine Zeit, das SVN zu aktualisieren.  Warten Sie auf 0.3.6, ich baue es jetzt.  Sie können Ihren Knoten in der Zwischenzeit herunterfahren.

Und 35 Minuten später schrieb [er](https://bitcointalk.org/index.php?topic=626.msg6480#msg6480):


> SVN ist mit Version 0.3.6 aktualisiert.
>

> Ich lade jetzt einen Windows-Build von 0.3.6 auf Sourceforge hoch, dann werde ich einen Linux-Build erstellen.

Zu diesem Zeitpunkt schien er auch den ursprünglichen Beitrag aktualisiert zu haben, um 0.3.6 anstelle von 0.3.5 zu erwähnen:


> Bitte aktualisieren Sie so schnell wie möglich auf 0.3.6!  Wir haben einen Implementierungsfehler behoben, bei dem es möglich war, dass gefälschte Transaktionen als akzeptiert angezeigt werden konnten.  Akzeptieren Sie keine Bitcoin-Transaktionen als Zahlung, bis Sie auf Version 0.3.6 aktualisiert haben!
>

> Wenn Sie nicht sofort auf 0.3.6 aktualisieren können, ist es am besten, den Bitcoin-Knoten bis dahin abzuschalten.
>

> Ebenfalls in 0.3.6, schnelleres Hashing:
> - midstate-Cache-Optimierung dank tcatm
> - Crypto++ ASM SHA-256 dank BlackEye
> Insgesamt 2,4x schnellere Generierung.
>

> Herunterladen:
>

> http://sourceforge.net/projects/Bitcoin/files/Bitcoin/Bitcoin-0.3.6/
>

> Windows- und Linux-Benutzer: Wenn Sie 0.3.5 haben, müssen Sie trotzdem auf 0.3.6 aktualisieren.

Beachten Sie den Unterschied in der Charakterisierung des Problems in der ersten Meldung: "könnte als akzeptiert angezeigt werden" gegenüber "könnte akzeptiert werden". Vielleicht hat Satoshi den Schweregrad des Fehlers in seiner Mitteilung heruntergespielt, um nicht zu viel Aufmerksamkeit auf das eigentliche Problem zu lenken. Wie auch immer, die Leute haben auf 0.3.6 aktualisiert und es hat wie erwartet funktioniert. Dieses spezielle Problem wurde erstaunlicherweise ohne Verluste von Bitcoin gelöst.


In der Meldung zu Satoshi wurden auch einige Leistungsoptimierungen für Mining beschrieben. Es ist unklar, warum dies in einer kritischen Sicherheitsbehebung enthalten war, es ist möglich, dass der Zweck war, das wirkliche Problem zu verschleiern. Es scheint jedoch wahrscheinlicher, dass er einfach das veröffentlicht hat, was sich auf dem Entwicklungszweig des Subversion-Repositorys befand, mit der hinzugefügten Sicherheitsbehebung.


Damals gab es noch nicht annähernd so viele Nutzer wie heute, und der Wert von Bitcoin ging gegen Null. Würde diese Fehlerbehebung heute stattfinden, würde man sie aus mehreren Gründen als komplette Scheißshow bezeichnen:



- Satoshi hat eine reine Binärversion von 0.3.5 veröffentlicht, die die Korrektur enthält. Es wurde kein Patch oder Code zur Verfügung gestellt, vielleicht als Maßnahme, um das Problem zu verschleiern.
- 0.3,5 [hat nicht einmal funktioniert] (https://bitcointalk.org/index.php?topic=626.msg6455#msg6455).
- Der Fix in 0.3.6 war eigentlich ein Hard Fork.


Ein weiterer strittiger Punkt ist, ob es gut oder schlecht ist, dass die Benutzer aufgefordert wurden, ihre Knoten abzuschalten. Das wäre heute nicht mehr möglich, aber damals verfolgten viele Benutzer aktiv die Foren, um Updates zu erhalten, und waren in der Regel auf dem Laufenden. In Anbetracht der Tatsache, dass es möglich war, dies zu tun, wäre es vielleicht eine sinnvolle Maßnahme gewesen.


#### 2010-08-15 Kombinierter Ausgabeüberlauf (CVE-2010-5139)



Mitte August 2010 hat der Bitcointalk-Forumsnutzer jgarzik, alias Jeff Garzik,

[entdeckte, dass](https://bitcointalk.org/index.php?topic=822.msg9474#msg9474) eine bestimmte Transaktion in Blockhöhe 74638 zwei Ausgaben mit ungewöhnlich hohem Wert hatte:


```
"out" : [
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0xB7A73EB128D7EA3D388DB12418302A1CBAD5E890 OP_EQUALVERIFY OP_CHECKSIG"
},
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0x151275508C66F89DEC2C5F43B6F9CBE0B5C4722C OP_EQUALVERIFY OP_CHECKSIG"
}
]
```


> Der "Wert aus" in diesem Block #74638 ist ziemlich seltsam:
>

> 92233720368.54277039 BTC?  Ist das UINT64_MAX, frage ich mich?

Vermutlich gab es einen Fehler, der dazu führte, dass die Summe der beiden int64-Ausgänge (nicht uint64, wie Garzik vermutete) zu einem negativen Wert -0,00997538 BTC überlief. Unabhängig von der Summe der Eingänge wäre die "Summe" der Ausgänge kleiner, so dass diese Transaktion nach dem damaligen Code in Ordnung war.


In diesem Fall war der Fehler durch einen tatsächlichen Exploit aufgedeckt und veröffentlicht worden. Eine unglückliche Folge davon war, dass etwa 2x92 Milliarden Bitcoin erschaffen wurden, was das Geld Supply von etwa 3,7 Millionen Münzen, das zu dieser Zeit existierte, stark verwässerte.


In einem verwandten Thread hat [Satoshi gepostet](https://bitcointalk.org/index.php?topic=823.msg9531#msg9531), dass er es begrüßen würde, wenn die Leute mit Mining aufhören würden (oder mit dem *Generieren*, wie sie es damals nannten):


> Es würde helfen, wenn die Leute aufhören würden, zu generieren.  Wir werden wahrscheinlich einen neuen Zweig um den aktuellen herum machen müssen, und je weniger generate man hat, desto schneller wird das gehen.
>

> Ein erster Patch wird in SVN rev 132 sein.  Er ist noch nicht hochgeladen.  Ich schiebe zuerst einige andere Änderungen aus dem Weg, dann werde ich den Patch dafür hochladen.

Sein Plan war es, einen Soft Fork zu machen, um Transaktionen wie die hier diskutierte ungültig zu machen und damit die Blöcke (insbesondere Block 74638), die solche Transaktionen enthielten, ungültig zu machen. Weniger als eine Stunde später übertrug er einen [Patch in Revision 132](https://sourceforge.net/p/Bitcoin/code/132/) in das Subversion-Repository und [postete im Forum](https://bitcointalk.org/index.php?topic=823.msg9548#msg9548), in dem er beschrieb, was seiner Meinung nach die Benutzer tun sollten:


> Der Patch wurde in SVN rev 132 hochgeladen!
>

> Für den Moment, empfohlene Schritte:
> 1) Abschalten.
> 2) Laden Sie die blk-Dateien von knightmb herunter.  (ersetzen Sie Ihre blk0001.dat und blkindex.dat Dateien)
> 3) Upgrade.
> 4) Es sollte mit weniger als 74000 Blöcken beginnen. Lassen Sie ihn den Rest erneut herunterladen.
>

> Wenn Sie die Dateien von knightmb nicht verwenden wollen, können Sie einfach Ihre blk*.dat-Dateien löschen, aber das wird das Netzwerk stark belasten, wenn jeder den gesamten Blockindex auf einmal herunterlädt.
>

> Ich werde in Kürze Veröffentlichungen erstellen.

Er wollte, dass die Leute Blockdaten von einem bestimmten Benutzer, nämlich knightmb, herunterladen, der seinen Blockchain so veröffentlicht hatte, wie er auf seiner Festplatte erschien, nämlich die Dateien blkXXXX.dat und blkindex.dat. Der Grund dafür, die Blockchain-Daten auf diese Weise herunterzuladen, anstatt sie von Grund auf zu synchronisieren, bestand darin, Engpässe bei der Netzwerkbandbreite zu verringern.


Dabei gab es eine große Einschränkung: Die Daten, die die Benutzer von knightmb herunterluden, wurden beim Start nicht von der Bitcoin-Software überprüft (https://Bitcoin.stackexchange.com/a/113682/69518). Die Datei blkindex.dat enthielt den UTXO-Satz, und die Software akzeptierte alle Daten darin, als ob sie sie bereits verifiziert hätte. knightmb hätte die Daten manipulieren können, um sich selbst oder jemand anderem einige Bitcoins zu geben.


Auch hier schienen die Leute mitzumachen, und die Aufhebung des ungültigen Blocks und seiner Nachfolger war erfolgreich. Die Schürfer begannen mit der Arbeit an einem neuen Nachfolger für Block [74637] (https://Mempool.space/block/0000000000606865e679308edf079991764d88e8122ca9250aef5386962b6e84), und laut Timestamp des Blocks erschien ein Nachfolger um 23:53 UTC, etwa sechs Stunden nach der Entdeckung des Problems. Am folgenden Tag, dem 16. August, um 08:10 Uhr, hatte die neue Kette die alte Kette um Block 74689 überholt, so dass sich alle nicht aktualisierten Knoten neu organisierten, um der neuen Kette zu folgen. Dies ist die umfangreichste Reorganisation - 52 Blöcke - in der Geschichte von Bitcoin.


Verglichen mit dem OP_RETURN-Problem wurde dieses Problem etwas sauberer gehandhabt:


- Keine Veröffentlichung eines reinen Binärpatches
- Die freigegebene Software funktionierte wie vorgesehen
- Nein Hard Fork


Auch bei dieser Ausgabe wurden die Benutzer aufgefordert, Mining zu stoppen. Wir können darüber diskutieren, ob dies eine gute Idee ist oder nicht, aber stellen Sie sich vor, Sie sind ein Miner und Sie sind davon überzeugt, dass alle Blöcke über dem schlechten Block schließlich in einer tiefen Reorganisation ausgelöscht werden: Warum sollten Sie Ressourcen auf Mining-verdammte Blöcke verschwenden?


Sie könnten auch denken, dass es ein wenig seltsam ist, wie von Nakamoto vorgeschlagen, den Blockchain, einschließlich des UTXO-Satzes, von einem beliebigen Hard-Laufwerk herunterzuladen. Wenn das so ist, haben Sie Recht: Das ist verdächtig. Aber unter den gegebenen Umständen war diese Notfallmaßnahme vernünftig.


Es gibt einen wichtigen Unterschied zwischen diesem Fall und dem vorherigen OP_RETURN-Fall: Dieses Problem wurde in freier Wildbahn ausgenutzt, so dass eine Behebung unkomplizierter erfolgen konnte. Im Fall von OP_RETURN mussten sie die Behebung verschleiern und öffentliche Erklärungen abgeben, aus denen nicht direkt hervorging, worin das Problem bestand.


#### 2013-03-11 DB-Sperren Problem 0.7.2 - 0.8.0 (CVE-2013-3220)



Ein sehr interessantes und pädagogisch wertvolles Problem tauchte im März 2013 auf. Es stellte sich heraus, dass sich der Blockchain (obwohl im folgenden Zitat das Wort "Fork" verwendet wird) nach Block 225429 geteilt hatte. Über die Einzelheiten dieses Vorfalls wurde [in BIP50] berichtet (https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki). In der Zusammenfassung heißt es:


> Ein Block mit einer größeren Anzahl von Transaktionsinputs als zuvor gesehen wurde gemined und verbreitet. Bitcoin 0.8-Knoten waren in der Lage, damit umzugehen, aber einige Pre-0.8-Bitcoin-Knoten lehnten ihn ab, was zu einem unerwarteten Fork des Blockchain führte. Die Pre-0.8-inkompatible Kette (von nun an die 0.8-Kette) verfügte zu diesem Zeitpunkt über etwa 60 % der Mining Hash-Leistung, wodurch sichergestellt wurde, dass sich der Split nicht automatisch auflöste (wie es der Fall gewesen wäre, wenn die Pre-0.8-Kette die 0.8-Kette an Gesamtarbeit überholt hätte, was die 0.8-Knoten gezwungen hätte, sich auf die Pre-0.8-Kette umzustellen).
>

> Um die kanonische Kette so schnell wie möglich wiederherzustellen, haben BTCGuild und Slush ihre Bitcoin 0,8-Knoten auf 0,7 herabgestuft, damit ihre Pools auch den größeren Block ablehnen würden. Dadurch wurde die Mehrheit der Hashpower auf die Kette ohne den größeren Block gelegt, was schließlich dazu führte, dass sich die 0,8-Knoten zur Kette vor 0,8 umorganisierten.

Das schnelle Handeln der Mining-Pools BTCGuild und Slush war in dieser Notlage von entscheidender Bedeutung. Sie waren in der Lage, die Mehrheit der Hash-Power auf den Vor-0.8-Zweig des Splits umzuleiten und so zur Wiederherstellung des Konsenses beizutragen. Dies gab den Entwicklern die Zeit, eine nachhaltige Lösung zu finden.


Sehr interessant an diesem Problem ist auch, dass die Version 0.7.2 mit sich selbst inkompatibel war, wie es auch bei früheren Versionen der Fall war. Dies wird im [Abschnitt über die Ursache von BIP50] (https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki#root-cause) erklärt:


> Mit der unzureichend hohen BDB-Sperrkonfiguration war sie implizit zu einer Netzwerk-Konsensregel geworden, die die Gültigkeit von Blöcken bestimmt (wenn auch eine
inkonsistente und unsichere Regel, da die Verwendung der Sperre von Knoten zu Knoten variieren kann).


Kurz gesagt, das Problem besteht darin, dass die Anzahl der Datenbanksperren, die die Bitcoin Core-Software zur Verifizierung eines Blocks benötigt, nicht deterministisch ist. Ein Knoten könnte X Sperren benötigen, während ein anderer Knoten X+1 Sperren benötigt. Die Knoten haben auch eine Grenze, wie viele Sperren Bitcoin aufnehmen kann. Wenn die Anzahl der benötigten Sperren den Grenzwert überschreitet, wird der Block als ungültig betrachtet. Wenn also X+1 das Limit überschreitet, aber nicht X, dann teilen die beiden Knoten den Blockchain auf und sind sich nicht einig, welcher Zweig gültig ist.


Abgesehen von den Sofortmaßnahmen, die von den beiden Pools zur Wiederherstellung des Konsenses ergriffen wurden, bestand die gewählte Lösung darin



- begrenzung der Blöcke in Bezug auf die Größe und die benötigten Sperren in Version 0.8.1
- alte Versionen (0.7.2 und einige ältere) mit denselben neuen Regeln patchen und die globale Sperrgrenze erhöhen.


Mit Ausnahme der im zweiten Aufzählungspunkt genannten Erhöhung des Limits für globale Sperren wurden diese Regeln vorübergehend für einen bestimmten Zeitraum eingeführt. Es war geplant, diese Beschränkungen aufzuheben, sobald die meisten Knoten aufgerüstet haben.


Diese Soft Fork verringerte das Risiko eines Scheiterns des Konsenses drastisch, und einige Monate später, am 15. Mai, wurden die vorübergehenden Regeln im gesamten Netz gemeinsam deaktiviert. Es sei darauf hingewiesen, dass es sich bei dieser Deaktivierung in Wirklichkeit um eine Hard Fork handelte, die jedoch nicht umstritten war. Außerdem wurde sie zusammen mit der vorangegangenen Soft Fork veröffentlicht, so dass diejenigen, die die geforkte Soft-Software einsetzten, sehr wohl wussten, dass ihr eine Hard Fork folgen würde. Daher blieb die große Mehrheit der Knoten im Konsens, als der Hard Fork aktiviert wurde. Unglücklicherweise gingen jedoch einige Knoten, die nicht aktualisiert hatten, bei diesem Prozess verloren.


Man könnte sich fragen, ob dies heute noch machbar wäre. Die Mining-Landschaft ist heute komplexer, und je nach Hash-Macht auf beiden Seiten der Spaltung könnte es Hard sein, einen Patch wie den in BIP50 schnell genug auszurollen. Es wäre wahrscheinlich Hard, Bergleute auf dem "falschen" Zweig davon zu überzeugen, auf ihre Blockbelohnungen zu verzichten.


#### BIP66



Das BIP66 ist interessant, weil es die Bedeutung von hervorhebt:



- gute Auswahl Kryptographie
- verantwortungsvolle Offenlegung
- einsatz ohne Offenlegung der Schwachstelle
- Mining auf überprüften Blöcken


BIP66 war ein Vorschlag zur Verschärfung der Regeln für Signaturkodierungen in Bitcoin Script. Die [Motivation] (https://github.com/Bitcoin/bips/blob/master/bip-0066.mediawiki#motivation) bestand darin, Signaturen mit anderer Software oder anderen Bibliotheken als OpenSSL und sogar neueren Versionen von OpenSSL analysieren zu können. OpenSSL ist eine Bibliothek für allgemeine Kryptographie, die Bitcoin Core zu dieser Zeit verwendete.


Das BIP wurde am 4. Juli 2015 aktiviert. Das BIP66 behebt jedoch auch ein viel schwerwiegenderes Problem, das in dem BIP nicht erwähnt wird.


##### Die Verwundbarkeit



Die vollständige Offenlegung dieses Themas wurde am 28. Juli 2015 von Pieter Wuille in einem

[E-Mail an die Bitcoin-dev Mailingliste](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-July/009697.html):


> Hallo zusammen,
>

> Ich möchte auf eine Sicherheitslücke hinweisen, die ich im September 2014 entdeckt habe und die nicht mehr ausnutzbar war, als BIP66 Anfang dieses Monats die 95 %-Schwelle erreichte.
>

> Kurze Beschreibung:
>

> Eine speziell angefertigte Transaktion könnte den Blockchain zwischen den Knoten gegabelt haben:
>

> - verwendung von OpenSSL auf 32-Bit-Systemen und auf 64-Bit-Windows-Systemen
> - verwendung von OpenSSL auf Nicht-Windows-64-Bit-Systemen (Linux, OSX, ...)
> - verwendung einiger Nicht-OpenSSL-Codebasen zum Parsen von Signaturen

In der E-Mail werden weitere Einzelheiten darüber dargelegt, wie das Problem entdeckt wurde und was genau die Ursache dafür war. Am Ende legt er eine Zeitleiste der Ereignisse vor, und wir werden hier einige der wichtigsten wiedergeben. Einige von ihnen wurden, wie die obige Abbildung zeigt, bereits beschrieben.


![](assets/bip66-timeline-1.webp)


Zeitleiste der Ereignisse rund um das BIP66. Die schwarz markierten Punkte wurden bereits erläutert.


##### Vor der Entdeckung



Ohne dass irgendjemand von diesem Problem wusste, hätte es durch das inzwischen in die Breite gezogene BIP62 gelöst werden können, bei dem es sich um einen Vorschlag zur Verringerung der Möglichkeiten der Verfälschung von Transaktionen handelte. Zu den vorgeschlagenen Änderungen im BIP62 gehörte eine Verschärfung der Konsensregeln für die Kodierung von Signaturen, die sogenannte "strenge DER-Kodierung". Pieter Wuille schlug im Juli 2014 einige Änderungen am BIP vor, mit denen das Problem gelöst worden wäre:


> 2014-Jul-18: Um die Bitcoin-Signaturkodierungsregeln nicht von OpenSSLs spezifischem Parser abhängig zu machen, habe ich den BIP62-Vorschlag dahingehend geändert, dass seine strenge DER-Signaturanforderung auch für Transaktionen der Version 1 gilt. Zu dieser Zeit wurden keine Nicht-DER-Signaturen mehr in Blöcken verarbeitet, daher wurde angenommen, dass dies keine Auswirkungen haben würde. Siehe https://github.com/Bitcoin/bips/pull/90 und http://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2014-July/006299.html. Zu diesem Zeitpunkt war dies nicht bekannt, aber wenn es umgesetzt worden wäre, hätte dies die Schwachstelle behoben.

Aufgrund des Umfangs dieses BIP, das wesentlich mehr als nur "strenge DER-Kodierung" abdeckte, wurde es ständig geändert und kam nie zum Einsatz. Das BIP wurde später zurückgezogen, weil Segregated Witness, BIP141, die Fehlbarkeit von Transaktionen auf eine andere und vollständigere Weise löste.


##### Nach der Entdeckung



OpenSSL veröffentlichte neue Versionen seiner Software mit Patches, die das Problem gelöst hätten, wenn sie von Anfang an in Bitcoin verwendet worden wären. Die Verwendung einer neuen Version von OpenSSL nur in einer neuen Version von Bitcoin Core würde das Problem jedoch verschlimmern. Gregory Maxwell erklärt dies in einem anderen [E-Mail-Thread] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-January/007097.html) im Januar 2015:


> Während es für die meisten Anwendungen im Allgemeinen akzeptabel ist, einige Unterschriften eifrig abzulehnen, ist Bitcoin ein Konsenssystem, bei dem alle Teilnehmer im Allgemeinen über die genaue Gültigkeit oder Ungültigkeit der Eingabedaten einig sein müssen.  In gewissem Sinne ist die Konsistenz wichtiger als die "Korrektheit".
> [...]
> Die obigen Patches beheben jedoch nur ein Symptom des allgemeinen Problems: das Verlassen auf Software, die nicht für die Verwendung im Konsens entwickelt oder vertrieben wird (insbesondere OpenSSL), um konsensnormatives Verhalten zu erreichen.  Daher schlage ich als schrittweise Verbesserung eine gezielte Soft-Fork vor, um bald eine strikte DER-Konformität zu erzwingen, unter Verwendung einer Teilmenge von BIP62.

Er weist darauf hin, dass die Verwendung von Code, der nicht für die Verwendung in Konsenssystemen vorgesehen ist, ernsthafte Risiken birgt, und schlägt vor, dass Bitcoin eine strenge DER-Kodierung implementiert. Dies ist ein sehr deutliches Beispiel für die Bedeutung einer guten Auswahl von Kryptographie.


Diese Ereignisse könnten den Eindruck erwecken, dass Gregory Maxwell von der Sicherheitslücke wusste, die Pieter Wuille später veröffentlichte, aber helfen wollte, eine als Vorsichtsmaßnahme getarnte Lösung einzuschleusen, ohne zu viel Aufmerksamkeit auf das eigentliche Problem zu lenken. Das könnte so sein, ist aber reine Spekulation.


Dann wurde, wie von Maxwell vorgeschlagen, BIP66 als Untermenge von BIP62 geschaffen, die nur eine strikte DER-Kodierung vorsah. Dieses BIP wurde offenbar weitgehend akzeptiert und im Juli eingeführt, obwohl es ironischerweise zu zwei Aufspaltungen von Blockchain aufgrund des *validierungslosen Mining* kam. Diese Abspaltungen werden im nächsten Abschnitt erörtert.


![](assets/bip66-timeline-2.webp)


Eine wichtige Erkenntnis daraus ist, dass BIPs mehr oder weniger *atomar* sein sollten, d. h. sie sollten vollständig genug sein, um etwas Nützliches zu bieten oder ein bestimmtes Problem zu lösen, aber klein genug, um eine breite Unterstützung durch die Benutzer zu ermöglichen. Je mehr man in ein BIP packt, desto geringer ist die Chance auf Akzeptanz.


##### Spaltungen aufgrund von validierungsfreien Mining



Leider war die Geschichte von BIP66 damit noch nicht zu Ende. Als BIP66 aktiviert wurde, stellte sich heraus, dass es ziemlich chaotisch war, weil einige Miner die Blöcke, die sie zu erweitern versuchten, nicht verifiziert haben. Dies wird als validierungsloser Mining oder SPV-Mining (wie in Simplified Payment Verification) bezeichnet. Eine Warnmeldung wurde an Bitcoin-Knoten mit einem Link zu [einer Webseite, die das Problem beschreibt] (https://Bitcoin.org/en/alert/2015-07-04-spv-Mining) versandt:


> Am frühen Morgen des 4. Juli 2015 wurde die Schwelle von 950/1000 (95 %) erreicht. Kurz darauf schürfte ein kleiner Miner (Teil der nicht aufgerüsteten 5 %) einen ungültigen Block - ein zu erwartender Vorfall. Leider stellte sich heraus, dass etwa die Hälfte der Hash-Rate des Netzwerks Mining war, ohne die Blöcke vollständig zu validieren (SPV Mining genannt), und neue Blöcke auf diesem ungültigen Block aufbaute.

Auf der Warnseite wurden die Benutzer angewiesen, 30 zusätzliche Bestätigungen abzuwarten, falls sie ältere Versionen von Bitcoin Core verwenden.


Der oben erwähnte Split trat am 04.07.2015 um 02:10 UTC nach der Blockhöhe [363730] (https://Mempool.space/block/000000000000000006a320d752b46b532ec0f3f815c5dae467aff5715a6e579e) auf. Dieses Problem wurde um 03:50 Uhr desselben Tages behoben, nachdem 6 ungültige Blöcke abgebaut worden waren. Leider trat dasselbe Problem am nächsten Tag, d. h. am 2015-07-05 um 21:50 Uhr, erneut auf, aber dieses Mal dauerte der ungültige Zweig nur 3 Blöcke.


![](assets/bip66-timeline-3.webp)

Die Ereignisse, die zu BIP66, seinem Einsatz und den Folgen führten, sind eine sehr gute Fallstudie dafür, wie vorsichtig Bitcoin-Entwickler sein müssen. Ein paar wichtige Erkenntnisse aus BIP66:



- Das Gleichgewicht zwischen Offenheit und dem Verschweigen einer Schwachstelle ist heikel.
- Die Bereitstellung von Korrekturen für nicht veröffentlichte Schwachstellen ist ein schwieriges Unterfangen.
- Der Konsens lautet Hard.
- Software, die nicht für Konsenssysteme bestimmt ist, ist generell riskant.
- BIPs sollten eher atomar sein.


### Fazit zu When Shit Hits The Fan



Bitcoin hat Bugs. Personen, die Fehler entdecken, sollten diese verantwortungsbewusst an die Bitcoin-Entwickler weitergeben, damit diese den Fehler beheben können, ohne ihn öffentlich zu machen. Im Idealfall kann die Fehlerbehebung als Leistungsverbesserung oder eine andere Verschleierung getarnt werden.


Wir haben uns einige der schwerwiegenderen Probleme angesehen, die im Laufe der Jahre aufgetaucht sind, und wie sie behandelt wurden. Einige wurden durch Exploits öffentlich entdeckt, während andere verantwortungsbewusst offengelegt wurden und behoben werden konnten, bevor böswillige Akteure die Chance hatten, sie auszunutzen.


## Fragen zur Diskussion

<chapterId>91462ca7-f09c-55da-a5b9-3e211de31da5</chapterId>


Diese Diskussionsfragen sind nicht nur eine Wiederholung des Inhalts von "Bitcoin Entwicklungsphilosophie", sondern sollen Sie dazu anregen, weiter zu recherchieren, also stellen Sie sicher, dass Sie sich auf die Suche machen.


Sie können die Tiefe Ihres Verständnisses testen, indem Sie einen [Mini-Essay] (https://www.youtube.com/watch?v=N4YjXJVzoZY) von 100-300 Wörtern schreiben, indem Sie ein Thema aus diesem Fragenpool wählen. Wenn Sie eine Rückmeldung zu Ihrer Arbeit wünschen, können Sie sie an mini-essay@planb.network schicken. Wir werden sie gerne überprüfen.


#### Dezentralisierung



- Die Dezentralisierung ist Hard. Warum machen wir uns all diese Mühe, damit es funktioniert? Könnten wir uns für einen hybriden Ansatz entscheiden, bei dem einige Teile zentralisiert sind und andere nicht?
- Führt die Dezentralisierung das Problem der doppelten Ausgaben ein, oder erfordert das Problem der doppelten Ausgaben die Dezentralisierung? Wie hat die Satoshi das Problem der doppelten Ausgaben gelöst?
- In welchen Aspekten ist Bitcoin immer noch am anfälligsten für Zensur, und warum ist Zensur so eine schlechte Sache? Gibt es Argumente, die für eine Zensur sprechen?
- Es wird angegeben, dass Bitcoin genehmigungsfrei ist. Gibt es noch andere Zahlungsmittel, die Sie als erlaubnisfrei ansehen könnten?



#### Vertrauensunwürdigkeit




- Vertrauenslosigkeit ist oft ein Spektrum, nicht binär. Welche Aspekte von Bitcoin sind eher Trustless, und welche beinhalten typischerweise ein höheres Maß an Vertrauen? Können sie abgemildert werden?
- Sie möchten einen Full node ausführen, um alle Transaktionen vollständig validieren zu können. Sie laden Bitcoin Core von https://Bitcoin.org/en/download herunter. Wohin haben Sie Ihr Vertrauen gesetzt, und wo sind Sie vollständig Trustless?
- Kann man ein Trustless-System auf ein bewährtes System aufbauen?



#### Datenschutz




- Welches sind einige wichtige Vorteile, die ein Nutzer hat, wenn er bei der Interaktion mit Bitcoin seine Privatsphäre wahrt? Was sind einige altruistische Vorteile für das Netz?
- Wie wirkt sich die Wiederverwendung von Adressen auf Ihre Privatsphäre aus?
- Bitcoin verwendet ein UTXO-Modell, während einige alternative Kryptowährungen ein Kontomodell verwenden. Welche Auswirkungen hat diese Entscheidung auf die Privatsphäre?



#### Endlicher Supply




- Welches Verhältnis besteht zwischen dem endlichen Bitcoin und der Münzausgabe des Supply durch den Coinbase Transaction? Welches Verhältnis besteht zwischen der Münzausgabe und dem Sicherheitsbudget, und wie stehen sie im Widerspruch zueinander?
- Welche Parameter hätte Satoshi ändern können, um Bitcoins Supply-Obergrenze zu ändern? Was würde sich ändern, wenn er beschlossen hätte, den Supply auf 1 Million zu begrenzen? Wie wäre es mit 1 Billion?
- Warum plädieren einige Leute für eine Erhöhung von Bitcoin Supply? Glauben Sie, dass dies geschehen wird?


#### Aktualisieren von



- Was ist Speedy Trial und warum war es notwendig, Taproot zu aktivieren?
- Warum brauchen wir einen so hohen Prozentsatz an Minern, um eine Softfork aufzurüsten? Warum ist der Schwellenwert nicht einfach 51%?



#### Gegensätzliches Denken




- Was ist ein Sybil-Angriff, und warum ist ein dezentrales Netzwerk so anfällig dafür?
- Warum ist es wichtig, dass alle Akteure im Bitcoin-Netzwerk - und nicht nur die Entwickler - kontraproduktiv denken?



#### Offene Quelle




- Nur eine Handvoll Betreuer hat die notwendigen GitHub-Berechtigungen, um Code in das [Bitcoin Core](https://github.com/Bitcoin/Bitcoin) Repository einzubringen. Steht das nicht im Widerspruch zu einem erlaubnisfreien Netzwerk?
- Ist der Open-Source-Entwicklungsprozess anfällig für einen Sybil-Angriff? Wenn ja, wie würden Sie dem begegnen?
- Welche Vor- und Nachteile hat es, sich auf Open-Source-Bibliotheken von Drittanbietern zu verlassen, und welchen Ansatz verfolgt Bitcoin Core?
- Inwiefern brauchen wir eine Überprüfung, die über die reine Codeüberprüfung hinausgeht? Wie lässt sich bestimmen, wie viel Überprüfung genug ist?
- Wie stellen wir sicher, dass immer genügend Leute mit Fachwissen an Bitcoin arbeiten? Was geschieht, wenn dies nicht der Fall ist, und wie können wir ihre Integrität und ihre Absichten einschätzen?



#### Skalierung




- Es wird argumentiert, dass Sharding Skalierungsvorteile auf Kosten der Komplexität bietet. Warum sollten wir technologische Verbesserungen annehmen oder nicht, nur weil sie schwer zu verstehen sind, selbst wenn sie technologisch sinnvoll erscheinen?
- Was sind einige Beispiele für Methoden der inneren Skalierung, die in Bitcoin eingeführt wurden?
- Warum ist die vertikale Skalierung in einem dezentralen System viel schwieriger? Wie sieht es mit der horizontalen Skalierung aus?
- Wir scheinen nicht einmal annähernd einen Konsens darüber zu haben, wie wir die ganze Welt in Bitcoin einbinden können. Hätte Satoshi nicht zumindest einen Weg dorthin finden müssen, bevor Mining den ersten Block im Jahr 2009 einleitet?
- Wie würden Sie jede der folgenden Techniken einordnen (vertikal, horizontal, nach innen oder keine Skalierungstechnik): Sharding, Erhöhung der Blockgröße, SegWit, SPV-Knoten, zentralisierte Börsen, Lightning Network, Verringerung der Blockintervalle, Taproot, Sidechains



# Letzter Abschnitt


<partId>4b6ff4ef-b9ea-4c48-b05f-62d41a38fbbb</partId>


## Rezensionen und Bewertungen


<chapterId>d334a837-df46-4989-9cad-8d8779147dbe</chapterId>


<isCourseReview>true</isCourseReview>

## Schlussfolgerung


<chapterId>b77ed55c-b13a-430b-a212-37aab527b9e7</chapterId>


<isCourseConclusion>true</isCourseConclusion>