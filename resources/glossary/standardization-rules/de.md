---
term: STANDARDISIERUNGSREGELN

---
Standardisierungsregeln werden von jedem Bitcoin-Knoten zusätzlich zu den Konsensregeln individuell festgelegt, um die Struktur der unbestätigten Transaktionen zu definieren, die er in seinen Mempool aufnimmt und an seine Peers sendet. Diese Regeln werden also lokal von jedem Knoten konfiguriert und ausgeführt und können von einem Knoten zum anderen variieren. Sie gelten ausschließlich für unbestätigte Transaktionen. Daher akzeptiert ein Knoten eine Transaktion, die er als nicht standardisiert betrachtet, nur, wenn sie bereits in einem gültigen Block enthalten ist.

Es ist anzumerken, dass die Mehrheit der Nodes die Standardkonfigurationen, wie sie in Bitcoin Core festgelegt sind, beibehält, wodurch eine Einheitlichkeit der Standardisierungsregeln im gesamten Netzwerk geschaffen wird. Eine Transaktion, die zwar mit den Konsensregeln übereinstimmt, sich aber nicht an diese Standardisierungsregeln hält, wird es schwer haben, im gesamten Netzwerk verbreitet zu werden. Sie kann jedoch immer noch in einen gültigen Block aufgenommen werden, wenn sie einen Miner erreicht. In der Praxis werden diese Transaktionen, die als "Nicht-Standard" bezeichnet werden, oft direkt an einen Miner durch externe Mittel außerhalb des Bitcoin Peer-to-Peer-Netzwerks übermittelt. Dies ist oft die einzige Möglichkeit, diese Art von Transaktionen zu bestätigen.

Zum Beispiel ist eine Transaktion, die keine Gebühren zuweist, sowohl nach den Konsensregeln gültig als auch nicht standardmäßig, weil die Standardrichtlinie von Bitcoin Core für den Parameter "minRelayTxFee" "0,00001" (in BTC/kB) ist.

> ► *Der Begriff "mempool rules" wird manchmal auch für die Standardisierungsregeln verwendet