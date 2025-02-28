---
term: NVERSION

---
Das Feld "nVersion" in einer Bitcoin-Transaktion wird verwendet, um die Version des verwendeten Transaktionsformats anzugeben. Es ermöglicht dem Netzwerk, zwischen verschiedenen Entwicklungen des Transaktionsformats im Laufe der Zeit zu unterscheiden und die entsprechenden Regeln anzuwenden. Dieses Feld hat keinen Einfluss auf die Konsensregeln. Das bedeutet, dass ein diesem Feld zugewiesener Wert nicht dazu führt, dass die Transaktion ungültig wird. Für das Feld "nVersion" gelten jedoch Standardisierungsregeln, die derzeit nur die Werte "1" und "2" akzeptieren. Im Moment ist dieses Feld nur für die Aktivierung des Feldes "nSequence" nützlich.