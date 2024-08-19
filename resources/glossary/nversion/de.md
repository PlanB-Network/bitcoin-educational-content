---
term: NVERSION
---

Das `nVersion`-Feld in einer Bitcoin-Transaktion wird verwendet, um die Version des verwendeten Transaktionsformats anzugeben. Es ermöglicht dem Netzwerk, zwischen verschiedenen Entwicklungsstufen des Transaktionsformats im Laufe der Zeit zu unterscheiden und die entsprechenden Regeln anzuwenden. Dieses Feld hat keinen Einfluss auf die Konsensregeln. Das bedeutet, dass jeder diesem Feld zugewiesene Wert nicht dazu führt, dass die Transaktion für ungültig erklärt wird. Allerdings hat das `nVersion`-Feld Standardisierungsregeln, die derzeit nur die Werte `1` und `2` akzeptieren. Bislang ist dieses Feld nur für die Aktivierung des `nSequence`-Feldes nützlich.