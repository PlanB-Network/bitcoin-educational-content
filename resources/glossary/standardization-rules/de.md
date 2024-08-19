---
term: STANDARDISIERUNGSREGELN
---

Standardisierungsregeln werden individuell von jedem Bitcoin-Knoten zusätzlich zu den Konsensregeln angenommen, um die Struktur von unbestätigten Transaktionen zu definieren, die er in seinen Mempool aufnimmt und an seine Peers weiterleitet. Diese Regeln werden also lokal von jedem Knoten konfiguriert und ausgeführt und können von einem Knoten zum anderen variieren. Sie gelten ausschließlich für unbestätigte Transaktionen. Daher wird ein Knoten eine Transaktion nur dann akzeptieren, wenn er sie als nicht-standardmäßig ansieht, falls sie bereits in einem gültigen Block enthalten ist.

Es wird darauf hingewiesen, dass die Mehrheit der Knoten die Standardkonfigurationen beibehält, wie sie in Bitcoin Core festgelegt sind, wodurch eine Einheitlichkeit der Standardisierungsregeln im Netzwerk geschaffen wird. Eine Transaktion, die zwar den Konsensregeln entspricht, aber nicht diesen Standardisierungsregeln folgt, wird Schwierigkeiten haben, im Netzwerk verbreitet zu werden. Sie kann jedoch immer noch in einem gültigen Block enthalten sein, wenn sie einen Miner erreicht. In der Praxis werden diese Transaktionen, die als "nicht-standardmäßig" bezeichnet werden, oft direkt über externe Mittel außerhalb des Bitcoin Peer-to-Peer-Netzwerks an einen Miner übermittelt. Dies ist oft der einzige Weg, um diese Art von Transaktion zu bestätigen.

Zum Beispiel ist eine Transaktion, die keine Gebühren zuweist, sowohl nach den Konsensregeln gültig als auch nicht-standardmäßig, da die Standardrichtlinie von Bitcoin Core für den Parameter `minRelayTxFee` `0.00001` (in BTC/kB) beträgt.

> ► *Der Begriff "Mempool-Regeln" wird manchmal auch verwendet, um sich auf die Standardisierungsregeln zu beziehen.*