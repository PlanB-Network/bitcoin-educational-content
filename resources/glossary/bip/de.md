---
term: BIP
---

Akronym für "Bitcoin Improvement Proposal" (Vorschlag zur Verbesserung von Bitcoin). Ein Bitcoin Improvement Proposal (BIP) ist ein formaler Prozess zur Vorschlagung und Dokumentation von Verbesserungen und Änderungen am Bitcoin-Protokoll und seinen Standards. Da Bitcoin keine zentrale Entität hat, die über Updates entscheidet, ermöglichen BIPs der Gemeinschaft, Verbesserungen auf strukturierte und transparente Weise vorzuschlagen, zu diskutieren und umzusetzen. Jedes BIP beschreibt die Ziele der vorgeschlagenen Verbesserung, die Begründungen, potenzielle Auswirkungen auf die Kompatibilität sowie die Vor- und Nachteile. BIPs können von jedem Mitglied der Gemeinschaft geschrieben werden, müssen aber von anderen Entwicklern und den Editoren, die die Bitcoin Core GitHub-Datenbank pflegen: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun und Ruben Somsen, genehmigt werden. Es ist jedoch wichtig zu verstehen, dass die Rolle dieser Personen bei der Bearbeitung von BIPs nicht bedeutet, dass sie Bitcoin kontrollieren. Wenn jemand eine Verbesserung vorschlägt, die innerhalb des formalen BIP-Rahmens nicht akzeptiert wird, kann sie dennoch direkt der Bitcoin-Gemeinschaft präsentiert oder sogar ein Fork einschließlich ihrer Modifikation erstellt werden. Der Vorteil des BIP-Prozesses liegt in seiner Formalität und Zentralisierung, die die Debatte erleichtern, um eine Spaltung unter den Bitcoin-Nutzern zu vermeiden, und suchen, Updates auf konsensuelle Weise zu implementieren. Letztendlich ist es das Prinzip der wirtschaftlichen Mehrheit, das die Machtverhältnisse innerhalb des Protokolls bestimmt.

BIPs werden in drei Hauptkategorien eingeteilt:
* *Standards Track BIPs*: Betreffen Modifikationen, die Bitcoin-Implementierungen direkt beeinflussen, wie Transaktions- und Blockvalidierungsregeln;
* *Informational BIPs*: Bieten Informationen oder Empfehlungen, ohne direkte Änderungen am Protokoll vorzuschlagen;
* *Process BIPs*: Beschreiben Änderungen in den Verfahren rund um Bitcoin, wie Governance-Prozesse.

Standards Track und Informational BIPs werden auch nach "Layer" klassifiziert:
* *Consensus Layer*: BIPs in dieser Schicht betreffen die Konsensregeln von Bitcoin, wie Modifikationen an den Block- oder Transaktionsvalidierungsregeln. Diese Vorschläge können entweder Soft Forks (rückwärtskompatible Modifikationen) oder Hard Forks (nicht rückwärtskompatible Modifikationen) sein. Zum Beispiel gehören die BIPs für SegWit und Taproot zu dieser Kategorie;
* *Peer Services*: Diese Schicht betrifft den Betrieb des Bitcoin-Node-Netzwerks, das heißt, wie Knoten im Internet einander finden und miteinander kommunizieren.
* *API/RPC*: Die BIPs dieser Schicht betreffen die Application Programming Interfaces (API) und Remote Procedure Calls (RPC), die es Bitcoin-Software ermöglichen, mit Knoten zu interagieren;
* *Applications Layer*: Diese Schicht bezieht sich auf Anwendungen, die auf Bitcoin aufbauen. Die BIPs in dieser Kategorie befassen sich typischerweise mit Modifikationen auf der Ebene der Bitcoin-Wallet-Standards.

Der Prozess der Einreichung eines BIP beginnt mit der Konzeptualisierung und Diskussion der Idee auf der *Bitcoin-dev* Mailingliste. Wenn die Idee vielversprechend ist, entwirft der Autor ein BIP nach einem spezifischen Format und reicht es über einen Pull Request im Core GitHub-Repository ein. Die Editoren überprüfen diesen Vorschlag, um zu verifizieren, dass er alle Kriterien erfüllt. Das BIP muss technisch machbar, vorteilhaft für das Protokoll sein, das erforderliche Format einhalten und im Einklang mit der Philosophie von Bitcoin stehen. Wenn das BIP diese Bedingungen erfüllt, wird es offiziell in das GitHub-Repository der BIPs integriert. Es wird dann eine Nummer zugewiesen. Diese Nummer wird in der Regel vom Editor, oft Luke Dashjr, entschieden und logisch zugewiesen: BIPs, die sich mit ähnlichen Themen befassen, erhalten oft aufeinanderfolgende Nummern.

BIPs durchlaufen dann verschiedene Status im Laufe ihres Lebenszyklus. Der aktuelle Status wird im Kopf jeder BIP angegeben:
* Entwurf: Der Vorschlag befindet sich noch in der Entwurfs- und Diskussionsphase;
* Vorgeschlagen: Der BIP gilt als vollständig und bereit zur Überprüfung durch die Gemeinschaft;
* Zurückgestellt: Der BIP wird durch den Champion oder einen Redakteur für später auf Eis gelegt;
* Abgelehnt: Ein BIP wird als abgelehnt klassifiziert, wenn es 3 Jahre lang keine Aktivität gezeigt hat. Sein Autor kann sich später entscheiden, es wieder aufzunehmen, was es ermöglichen würde, in den Entwurfsstatus zurückzukehren;
* Zurückgezogen: Der BIP wurde von seinem Autor zurückgezogen;
* Final: Der BIP wird akzeptiert und weitgehend auf Bitcoin implementiert;
* Aktiv: Nur für Prozess-BIPs wird dieser Status zugewiesen, sobald ein bestimmter Konsens erreicht ist;
* Ersetzt / Veraltet: Der BIP ist nicht länger anwendbar oder wurde durch einen neueren Vorschlag ersetzt, der ihn unnötig macht.

![](../../dictionnaire/assets/25.png)

> ► *BIP ist das Akronym für "Bitcoin Improvement Proposal". Im Deutschen könnte es als "Vorschlag zur Verbesserung von Bitcoin" übersetzt werden. Allerdings verwenden die meisten deutschen Texte direkt das Akronym "BIP" als ein gemeinsames Substantiv, manchmal weiblich, manchmal männlich.*