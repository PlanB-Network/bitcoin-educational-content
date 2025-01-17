---
term: RESYNCHRONISATION

---
Bezieht sich auf ein Phänomen, bei dem die Blockchain aufgrund der Existenz konkurrierender Blöcke auf gleicher Höhe eine Änderung ihrer Struktur erfährt. Dies geschieht, wenn ein Teil der Blockchain durch eine andere Kette mit einer größeren Menge an angesammelter Arbeit ersetzt wird.

Diese Resynchronisationen sind Teil der natürlichen Funktionsweise von Bitcoin, bei der verschiedene Miner fast gleichzeitig neue Blöcke finden können, wodurch das Bitcoin-Netzwerk in zwei Teile gespalten wird. In solchen Fällen kann sich das Netzwerk vorübergehend in konkurrierende Ketten aufspalten. Wenn eine dieser Ketten mehr Arbeit anhäuft, werden die anderen Ketten von den Knoten aufgegeben, und ihre Blöcke werden zu so genannten "veralteten Blöcken" oder "verwaisten Blöcken" Dieser Prozess des Ersetzens einer Kette durch eine andere ist die Resynchronisierung.

![](../../dictionnaire/assets/9.webp)

Resynchronisierungen können verschiedene Folgen haben. Erstens, wenn ein Nutzer eine Transaktion in einem Block bestätigt hat, der sich als abgebrochen herausstellt, aber diese Transaktion nicht in der letztendlich gültigen Kette gefunden wird, dann wird seine Transaktion wieder unbestätigt. Aus diesem Grund wird empfohlen, immer mindestens 6 Bestätigungen abzuwarten, um eine Transaktion als wirklich unveränderlich zu betrachten. Nach 6 Blöcken sind Neusynchronisierungen so unwahrscheinlich, dass die Chance, dass sie auftreten, als praktisch null angesehen werden kann.

Außerdem bedeuten Resynchronisationen auf globaler Systemebene eine Verschwendung der Rechenleistung der Miner. Wenn es zu einer Aufspaltung kommt, befinden sich einige Miner auf Kette "A" und andere auf Kette "B". Wenn die Kette "B" während einer Neusynchronisierung aufgegeben wird, ist die gesamte von den Schürfern auf dieser Kette eingesetzte Rechenleistung per Definition verschwendet. Wenn es zu viele Resynchronisationen im Bitcoin-Netzwerk gibt, wird die Gesamtsicherheit des Netzwerks daher verringert. Dies ist einer der Gründe, warum eine Erhöhung der Blockgröße oder eine Verringerung des Intervalls zwischen den einzelnen Blöcken (10 Minuten) gefährlich sein kann.

> einige Bitcoiner bevorzugen den Begriff "orphan block", um einen abgelaufenen Block zu bezeichnen. Auch wenn es sich um einen Anglizismus handelt, wird im allgemeinen Sprachgebrauch eine "Reorganisation" oder "Reorg" oft der "Resynchronisation" vorgezogen