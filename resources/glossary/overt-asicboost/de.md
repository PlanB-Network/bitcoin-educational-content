---
term: OVERT ASICBOOST

---
Die offene und transparente Version von AsicBoost. AsicBoost ist eine algorithmische Optimierungstechnik, die beim Bitcoin-Mining verwendet wird. Miner, die die Overt-Version verwenden, manipulieren das Feld "nVersion" des Kandidatenblocks und verwenden diese Änderung als zusätzlichen Nonce. Diese Methode lässt das eigentliche "Nonce"-Feld des Blocks bei jedem Hashing-Versuch unverändert, wodurch die für jeden SHA256 benötigten Berechnungen reduziert werden, da einige Daten zwischen den Versuchen gleich bleiben. Diese Version ist öffentlich auffindbar und verbirgt ihre Änderungen nicht vor dem Rest des Netzes, anders als die verdeckte Version von AsicBoost.