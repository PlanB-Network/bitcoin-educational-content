---
term: BIP

---
Akronym für "Bitcoin Improvement Proposal" (Bitcoin-Verbesserungsvorschlag) Ein Bitcoin Improvement Proposal (BIP) ist ein formaler Prozess für das Vorschlagen und Dokumentieren von Verbesserungen und Änderungen am Bitcoin-Protokoll und seinen Standards. Da Bitcoin keine zentrale Instanz hat, die über Aktualisierungen entscheidet, erlauben BIPs der Community, Verbesserungen in einer strukturierten und transparenten Weise vorzuschlagen, zu diskutieren und zu implementieren. Jedes BIP beschreibt detailliert die Ziele der vorgeschlagenen Verbesserung, die Begründungen, mögliche Auswirkungen auf die Kompatibilität sowie die Vor- und Nachteile. BIPs können von jedem Mitglied der Community geschrieben werden, müssen aber von anderen Entwicklern und den Editoren, die die Bitcoin Core GitHub Datenbank pflegen, genehmigt werden: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun, und Ruben Somsen. Es ist jedoch wichtig zu verstehen, dass die Rolle dieser Personen bei der Bearbeitung von BIPs nicht bedeutet, dass sie Bitcoin kontrollieren. Wenn jemand eine Verbesserung vorschlägt, die innerhalb des formalen BIP-Rahmens nicht akzeptiert wird, kann er sie immer noch direkt der Bitcoin-Gemeinschaft vorlegen oder sogar eine Abspaltung mit seiner Änderung erstellen. Der Vorteil des BIP-Prozesses liegt in seiner Formalität und Zentralisierung, die eine Debatte erleichtern, um eine Spaltung unter den Bitcoin-Nutzern zu vermeiden, und die versuchen, Aktualisierungen in einer einvernehmlichen Weise zu implementieren. Letztendlich ist es das Prinzip der wirtschaftlichen Mehrheit, das die Machtdynamik innerhalb des Protokolls bestimmt.

Die BIPs werden in drei Hauptkategorien eingeteilt:


- Standards Track BIPs*: Betrifft Änderungen, die sich direkt auf Bitcoin-Implementierungen auswirken, wie z.B. Transaktions- und Blockvalidierungsregeln;
- Informationelle BIPs*: Sie enthalten Informationen oder Empfehlungen, ohne direkte Änderungen am Protokoll vorzuschlagen;
- BIPs* verarbeiten: Beschreiben Sie Änderungen in den Verfahren rund um Bitcoin, wie z. B. Governance-Prozesse.

Standard- und Informations-BIPs werden auch nach "Schicht" klassifiziert:


- Konsens-Schicht*: BIPs in dieser Schicht betreffen die Konsensregeln von Bitcoin, wie z.B. Änderungen an den Block- oder Transaktionsvalidierungsregeln. Diese Vorschläge können entweder Soft Forks (rückwärtskompatible Änderungen) oder Hard Forks (nicht rückwärtskompatible Änderungen) sein. Zum Beispiel gehören die BIPs für SegWit und Taproot zu dieser Kategorie;
- Peer-Dienste*: Diese Schicht befasst sich mit dem Betrieb des Bitcoin-Knotennetzwerks, d.h. damit, wie die Knoten einander im Internet finden und miteinander kommunizieren.
- API/RPC*: Die BIPs dieser Schicht betreffen die Anwendungsprogrammierschnittstellen (API) und Remote Procedure Calls (RPC), die es Bitcoin-Software ermöglichen, mit den Knoten zu interagieren;
- Anwendungsschicht*: Diese Schicht bezieht sich auf Anwendungen, die auf Bitcoin aufsetzen. Die BIPs in dieser Kategorie befassen sich typischerweise mit Änderungen auf der Ebene der Bitcoin-Wallet-Standards.

Der Prozess der Einreichung eines BIP beginnt mit der Konzeptualisierung und Diskussion der Idee auf der *Bitcoin-dev* Mailingliste. Wenn die Idee vielversprechend ist, entwirft der Autor ein BIP, das einem bestimmten Format folgt, und reicht es über einen Pull Request im Core-Repository auf GitHub ein. Die Redakteure überprüfen diesen Vorschlag, um sicherzustellen, dass er alle Kriterien erfüllt. Das BIP muss technisch durchführbar sein, dem Protokoll nützen, die geforderte Formatierung einhalten und mit der Philosophie von Bitcoin übereinstimmen. Wenn das BIP diese Bedingungen erfüllt, wird es offiziell in das GitHub-Repository der BIPs integriert. Dann wird ihm eine Nummer zugewiesen. Diese Nummer wird in der Regel vom Redakteur, oft Luke Dashjr, festgelegt und logisch vergeben: BIPs, die sich mit ähnlichen Themen befassen, erhalten oft fortlaufende Nummern.

Im Laufe ihres Lebenszyklus durchlaufen BIPs dann verschiedene Status. Der aktuelle Status wird in der Kopfzeile eines jeden BIP angegeben:


- Entwurf: Der Vorschlag befindet sich noch in der Entwurfs- und Diskussionsphase;
- Vorgeschlagen: Das BIP wird als vollständig angesehen und kann von der Gemeinschaft geprüft werden;
- Aufgeschoben: Die BIP wird vom Champion oder einem Redakteur auf einen späteren Zeitpunkt verschoben;
- Abgelehnt: Ein BIP wird als abgelehnt eingestuft, wenn es 3 Jahre lang keine Aktivität gezeigt hat. Sein Verfasser kann es zu einem späteren Zeitpunkt wieder aufnehmen, wodurch es in den Entwurfsstatus zurückkehren kann;
- Zurückgezogen: Die BIP wurde von ihrem Verfasser zurückgezogen;
- Endgültig: Das BIP wird von Bitcoin akzeptiert und weitgehend umgesetzt;
- Aktiv: Dieser Status wird nur für Prozess-BIPs vergeben, sobald ein bestimmter Konsens erreicht ist;
- Ersetzt / überholt: Die BIP ist nicht mehr anwendbar oder wurde durch einen neueren Vorschlag ersetzt, der sie überflüssig macht.

![](../../dictionnaire/assets/25.webp)

> bIP ist die Abkürzung für "Bitcoin Improvement Proposal" (Bitcoin Verbesserungsvorschlag). Im Französischen kann es mit "Proposition d'amélioration de Bitcoin" übersetzt werden. Die meisten französischen Texte verwenden jedoch das Akronym "BIP" direkt als allgemeines Substantiv, manchmal feminin, manchmal maskulin