---
term: RESYNCHRONISATION
---

Bezieht sich auf ein Phänomen, bei dem die Blockchain eine Modifikation ihrer Struktur durchläuft, aufgrund der Existenz von konkurrierenden Blöcken auf der gleichen Höhe. Dies tritt auf, wenn ein Teil der Blockchain durch eine andere Kette mit einer größeren Menge an akkumulierter Arbeit ersetzt wird.

Diese Resynchronisationen sind Teil der natürlichen Funktionsweise von Bitcoin, wo verschiedene Miner fast gleichzeitig neue Blöcke finden können, wodurch das Bitcoin-Netzwerk vorübergehend in zwei geteilt wird. In solchen Fällen kann das Netzwerk vorübergehend in konkurrierende Ketten aufgeteilt werden. Letztendlich, wenn eine dieser Ketten mehr Arbeit akkumuliert, werden die anderen Ketten von den Knoten aufgegeben, und ihre Blöcke werden als "veraltete Blöcke" oder "Waisenblöcke" bezeichnet. Dieser Prozess des Ersetzens einer Kette durch eine andere ist Resynchronisation.

![](../../dictionnaire/assets/9.png)

Resynchronisationen können verschiedene Konsequenzen haben. Zuerst, wenn eine Transaktion eines Benutzers in einem Block bestätigt wurde, der sich als aufgegeben herausstellt, aber diese Transaktion nicht in der letztendlich gültigen Kette gefunden wird, dann wird ihre Transaktion wieder unbestätigt. Deshalb wird empfohlen, immer auf mindestens 6 Bestätigungen zu warten, um eine Transaktion als wahrhaft unveränderlich zu betrachten. Nach 6 Blöcken Tiefe sind Resynchronisationen so unwahrscheinlich, dass die Chance ihres Auftretens praktisch null betrachtet werden kann.

Weiterhin, auf der globalen Systemebene, implizieren Resynchronisationen eine Verschwendung der Rechenleistung der Miner. Tatsächlich, wenn eine Aufteilung auftritt, werden einige Miner auf Kette `A` sein, und andere auf Kette `B`. Wenn Kette `B` während einer Resynchronisation letztendlich aufgegeben wird, dann ist die gesamte von den Minern auf dieser Kette eingesetzte Rechenleistung, per Definition, verschwendet. Wenn es zu viele Resynchronisationen im Bitcoin-Netzwerk gibt, wird daher die Gesamtsicherheit des Netzwerks reduziert. Dies ist teilweise der Grund, warum eine Erhöhung der Blockgröße oder eine Reduzierung des Intervalls zwischen den Blöcken (10 Minuten) gefährlich sein kann.

> ► *Einige Bitcoiner bevorzugen den Begriff "Waisenblock" für einen abgelaufenen Block. Auch wenn es ein Anglizismus ist, wird im allgemeinen Sprachgebrauch oft eine "Reorganisation" oder ein "Reorg" gegenüber einer "Resynchronisation" bevorzugt.*