---
term: UMSTRUKTURIERUNG

---
Bezieht sich auf ein Phänomen, bei dem die Blockchain aufgrund der Existenz konkurrierender Blöcke auf gleicher Höhe eine Änderung ihrer Struktur erfährt. Dies geschieht, wenn ein Teil der Blockchain durch eine andere Kette ersetzt wird, die eine größere Menge an angesammelter Arbeit aufweist.

Diese Umstrukturierungen sind Teil der natürlichen Funktionsweise von Bitcoin, bei der verschiedene Miner fast gleichzeitig neue Blöcke finden können, wodurch das Bitcoin-Netzwerk in zwei Teile gespalten wird. In solchen Fällen kann sich das Netzwerk vorübergehend in konkurrierende Ketten aufspalten. Wenn eine dieser Ketten mehr Arbeit anhäuft, werden die anderen Ketten von den Knoten aufgegeben, und ihre Blöcke werden zu so genannten "veralteten Blöcken" oder "verwaisten Blöcken" Dieser Prozess des Ersetzens einer Kette durch eine andere ist eine Reorganisation.

![](../../dictionnaire/assets/9.webp)

Umstrukturierungen können verschiedene Folgen haben. Erstens, wenn ein Nutzer eine Transaktion in einem Block bestätigt hat, der sich als aufgegeben herausstellt, aber diese Transaktion nicht in der letztendlich gültigen Kette auftaucht, dann wird seine Transaktion wieder unbestätigt. Aus diesem Grund wird empfohlen, immer mindestens 6 Bestätigungen abzuwarten, um eine Transaktion als wirklich unveränderlich zu betrachten. Nach 6 Blöcken sind Umstrukturierungen so unwahrscheinlich, dass die Chance, dass sie auftreten, als praktisch null angesehen werden kann.

Außerdem bedeuten Umstrukturierungen auf globaler Systemebene eine Verschwendung der Rechenleistung der Miner. Wenn es zu einer Aufspaltung kommt, werden einige Schürfer auf Kette "A" sein und andere auf Kette "B". Wenn die Kette "B" während einer Reorganisation aufgegeben wird, dann ist die gesamte von den Minern auf dieser Kette eingesetzte Rechenleistung per Definition verschwendet. Wenn es zu viele Umstrukturierungen im Bitcoin-Netzwerk gibt, wird die Gesamtsicherheit des Netzwerks verringert. Dies ist einer der Gründe, warum eine Erhöhung der Blockgröße oder eine Verringerung des Intervalls zwischen den einzelnen Blöcken (10 Minuten) gefährlich sein kann.

> einige Bitcoiner bevorzugen den Begriff "orphan block" für einen abgelaufenen Block. Im allgemeinen Sprachgebrauch wird ein "Reorg" auch für eine "Reorganisation" verwendet Der Begriff "Reorganisation" ist ein Anglizismus. Genauer wäre es, von einer "Resynchronisierung" zu sprechen