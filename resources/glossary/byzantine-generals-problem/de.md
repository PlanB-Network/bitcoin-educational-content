---
term: BYZANTINE GENERALS PROBLEM
---

Das Problem wurde erstmals von Leslie Lamport, Robert Shostak und Marshall Pease in der Fachzeitschrift *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["Das Byzantinische Generäle Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) im Juli 1982 formuliert. Es wird heute verwendet, um die Herausforderungen in Bezug auf Entscheidungsfindung zu veranschaulichen, wenn ein verteiltes System keinem Akteur vertrauen kann.

In dieser Metapher sind eine Gruppe byzantinischer Generäle und ihre jeweiligen Armeen um eine Stadt herum gelagert, die sie angreifen oder belagern möchten. Die Generäle sind geografisch voneinander getrennt und müssen über Boten kommunizieren, um ihre Strategie zu koordinieren. Ob sie angreifen oder sich zurückziehen, spielt keine Rolle, solange alle Generäle einen Konsens erreichen.

Daher können wir die folgenden Anforderungen betrachten:
* Jeder General muss eine Entscheidung treffen: angreifen oder zurückziehen (ja oder nein);
* Sobald die Entscheidung getroffen ist, kann sie nicht geändert werden;
* Alle Generäle müssen der gleichen Entscheidung zustimmen und sie synchron ausführen.

Darüber hinaus kann ein General nur über Nachrichten kommunizieren, die von einem Kurier übermittelt werden, die verzögert, zerstört, verändert oder verloren gehen können. Und selbst wenn eine Nachricht erfolgreich zugestellt wird, können ein oder mehrere Generäle aus irgendeinem Grund beschließen, das etablierte Vertrauen zu verraten und eine betrügerische Nachricht zu senden, was Chaos verursacht.

Wenn man das Dilemma auf den Kontext der Bitcoin-Blockchain anwendet, repräsentiert jeder General einen Knoten im Netzwerk, der einen Konsens über den Zustand des Systems erreichen muss. Mit anderen Worten, die Mehrheit der Teilnehmer in einem verteilten Netzwerk muss zustimmen und die gleiche Aktion ausführen, um einen totalen Ausfall zu vermeiden. Der einzige Weg, einen Konsens in diesem Typ von verteiltem System zu erreichen, ist, mindestens 2/3 der Netzwerkknoten zuverlässig und ehrlich zu haben. Daher ist das System anfällig, wenn die Mehrheit des Netzwerks beschließt, bösartig zu handeln.

> ► *Dieses Dilemma wird manchmal auch als "Das Problem des zuverlässigen Rundfunks" bezeichnet.*