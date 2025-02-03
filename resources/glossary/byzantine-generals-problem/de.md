---
term: PROBLEM DER BYZANTINISCHEN GENERÄLE

---
Das Problem wurde erstmals von Leslie Lamport, Robert Shostak und Marshall Pease in der Fachzeitschrift *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"] (https://lamport.azurewebsites.net/pubs/byz.pdf) im Juli 1982 formuliert. Es wird heute verwendet, um die Herausforderungen in Bezug auf die Entscheidungsfindung zu veranschaulichen, wenn ein verteiltes System keinem Akteur vertrauen kann.

In dieser Metapher lagert eine Gruppe byzantinischer Generäle mit ihren jeweiligen Armeen um eine Stadt, die sie angreifen oder belagern wollen. Die Generäle sind geografisch voneinander getrennt und müssen über Boten kommunizieren, um ihre Strategie zu koordinieren. Ob sie angreifen oder sich zurückziehen, spielt keine Rolle, solange alle Generäle einen Konsens finden.

Daher können wir die folgenden Anforderungen berücksichtigen:


- Jeder General muss eine Entscheidung treffen: Angriff oder Rückzug (ja oder nein);
- Eine einmal getroffene Entscheidung kann nicht mehr geändert werden;
- Alle Generäle müssen sich auf dieselbe Entscheidung einigen und diese synchron ausführen.

Darüber hinaus kann ein General mit einem anderen nur über Nachrichten kommunizieren, die von einem Kurier übermittelt werden und die verzögert, zerstört, verändert werden oder verloren gehen können. Und selbst wenn eine Nachricht erfolgreich zugestellt wird, können sich ein oder mehrere Generäle (aus welchen Gründen auch immer) dazu entschließen, das aufgebaute Vertrauen zu missbrauchen und eine gefälschte Nachricht zu senden, um Chaos zu stiften.

Überträgt man das Dilemma auf den Kontext der Bitcoin-Blockchain, so stellt jeder General einen Knoten im Netzwerk dar, der einen Konsens über den Zustand des Systems erreichen muss. Mit anderen Worten: Die Mehrheit der Teilnehmer eines verteilten Netzwerks muss sich einig sein und die gleiche Aktion ausführen, um einen Totalausfall zu vermeiden. Die einzige Möglichkeit, einen Konsens in dieser Art von verteiltem System zu erreichen, besteht darin, dass mindestens 2/3 der Netzwerkknoten zuverlässig und ehrlich sind. Wenn also die Mehrheit des Netzes beschließt, böswillig zu handeln, ist das System verwundbar.

> dieses Dilemma wird manchmal auch als "Problem der zuverlässigen Übertragung" bezeichnet