---
term: REORGANISATION
---

Bezieht sich auf ein Phänomen, bei dem die Blockchain aufgrund des Vorhandenseins von konkurrierenden Blöcken auf der gleichen Höhe eine Modifikation ihrer Struktur durchläuft. Dies tritt auf, wenn ein Teil der Blockchain durch eine andere Kette ersetzt wird, die eine größere Menge an gesammelter Arbeit aufweist.

Diese Reorganisationen sind Teil der natürlichen Funktionsweise von Bitcoin, wo verschiedene Miner fast gleichzeitig neue Blöcke finden können, wodurch das Bitcoin-Netzwerk vorübergehend in zwei geteilt wird. In solchen Fällen kann das Netzwerk vorübergehend in konkurrierende Ketten aufgeteilt werden. Letztendlich, wenn eine dieser Ketten mehr Arbeit ansammelt, werden die anderen Ketten von den Knoten aufgegeben, und ihre Blöcke werden zu dem, was als "veraltete Blöcke" oder "Waisenblöcke" bezeichnet wird. Dieser Prozess des Ersetzens einer Kette durch eine andere ist die Reorganisation.

![](../../dictionnaire/assets/9.png)

Reorganisationen können verschiedene Konsequenzen haben. Zunächst, wenn eine Transaktion eines Benutzers in einem Block bestätigt wurde, der sich als aufgegeben herausstellt, aber diese Transaktion nicht in der letztendlich gültigen Kette erscheint, dann wird ihre Transaktion wieder unbestätigt. Deshalb wird empfohlen, immer auf mindestens 6 Bestätigungen zu warten, um eine Transaktion als wahrhaft unveränderlich zu betrachten. Nach 6 Blöcken Tiefe sind Reorganisationen so unwahrscheinlich, dass die Chance ihres Auftretens praktisch als null betrachtet werden kann.

Darüber hinaus implizieren Reorganisationen auf der globalen Systemebene eine Verschwendung der Rechenleistung der Miner. Tatsächlich, wenn eine Aufteilung auftritt, werden einige Miner auf Kette `A` und andere auf Kette `B` sein. Wenn Kette `B` während einer Reorganisation letztendlich aufgegeben wird, dann ist die gesamte von den Minern auf dieser Kette eingesetzte Rechenleistung per Definition verschwendet. Wenn es zu viele Reorganisationen im Bitcoin-Netzwerk gibt, wird dadurch die Gesamtsicherheit desselben reduziert. Dies ist teilweise der Grund, warum eine Erhöhung der Blockgröße oder eine Verringerung des Intervalls zwischen den Blöcken (10 Minuten) gefährlich sein kann.

> ► *Einige Bitcoiner bevorzugen den Begriff "Waisenblock", um sich auf einen abgelaufenen Block zu beziehen. Außerdem wird im allgemeinen Sprachgebrauch ein "Reorg" verwendet, um sich auf eine "Reorganisation" zu beziehen. Der Begriff "Reorganisation" ist ein Anglizismus. Um genauer zu sein, könnte man von einer "Resynchronisation" sprechen.*