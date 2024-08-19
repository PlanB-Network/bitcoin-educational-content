---
term: OVERT ASICBOOST
---

Die offene und transparente Version von AsicBoost. AsicBoost ist eine algorithmische Optimierungstechnik, die beim Bitcoin-Mining verwendet wird. Miner, die die Overt-Version verwenden, manipulieren das `nVersion`-Feld des Kandidatenblocks und nutzen diese Modifikation als zusätzlichen Nonce. Diese Methode lässt das eigentliche `Nonce`-Feld des Blocks bei jedem Hashing-Versuch unverändert, wodurch die Berechnungen für jedes SHA256 reduziert werden, indem einige Daten zwischen den Versuchen gleich gehalten werden. Diese Version ist öffentlich erkennbar und verbirgt ihre Modifikationen nicht vor dem Rest des Netzwerks, im Gegensatz zur Covert-Version von AsicBoost.