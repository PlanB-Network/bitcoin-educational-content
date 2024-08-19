---
term: ORPHAN
---

Theoretisch bezieht sich ein Waisenblock (orphan block) auf einen gültigen Block, den ein Knotenpunkt empfangen hat, ohne dass der Elternblock, also der vorherige in der Kette, bereits erworben wurde. Obwohl gültig, bleibt dieser Block lokal isoliert als Waise.

In der allgemeinen Verwendung bezieht sich der Begriff "Waisenblock" jedoch oft auf einen Block ohne Kind: einen gültigen Block, der aber nicht in der Haupt-Bitcoin-Kette behalten wird. Dies tritt auf, wenn zwei Miner innerhalb einer kurzen Zeitspanne einen gültigen Block auf der gleichen Kettenhöhe finden und im Netzwerk verbreiten. Knotenpunkte wählen letztendlich nur einen Block zur Aufnahme in die Kette aus, basierend auf dem Prinzip der Kette mit der meisten angesammelten Arbeit, wodurch der andere zum "Waisen" wird.

![](../../dictionnaire/assets/9.png)

> ► *Persönlich bevorzuge ich den Begriff "Waisenblock", um über einen Block ohne Elternteil zu sprechen, und den Begriff "veralteter Block" (stale block), um auf einen Block zu verweisen, der kein Kind hat. Ich finde dies logischer und verständlicher, obwohl eine Mehrheit der Bitcoiner diese Verwendung nicht folgt.*