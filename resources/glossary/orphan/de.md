---
term: ORPHAN

---
Theoretisch handelt es sich bei einem verwaisten Block um einen gültigen Block, der von einem Knoten empfangen wurde, der den übergeordneten Block, d. h. den vorherigen in der Kette, noch nicht erworben hat. Obwohl dieser Block gültig ist, bleibt er lokal als Waise isoliert.

Im allgemeinen Sprachgebrauch bezieht sich der Begriff "verwaister Block" jedoch oft auf einen Block ohne Kind: ein gültiger Block, der jedoch nicht in der Haupt-Bitcoin-Kette verbleibt. Dies geschieht, wenn zwei Miner innerhalb eines kurzen Zeitraums einen gültigen Block auf der gleichen Kettenhöhe finden und ihn über das Netzwerk verbreiten. Die Knoten wählen schließlich nur einen Block aus, der in die Kette aufgenommen wird, basierend auf dem Prinzip der Kette mit der meisten angesammelten Arbeit, wodurch der andere "verwaist" wird

![](../../dictionnaire/assets/9.webp)

> ich persönlich bevorzuge den Begriff "verwaister Block" für einen Block ohne Elternteil und den Begriff "veralteter Block" für einen Block, der kein Kind hat. Ich finde dies logischer und verständlicher, auch wenn die Mehrheit der Bitcoiner dieser Verwendung nicht folgt.*