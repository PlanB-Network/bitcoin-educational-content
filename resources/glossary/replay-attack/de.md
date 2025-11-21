---
term: ANGRIFF WIEDERHOLEN
---

Im Zusammenhang mit Bitcoin liegt ein Replay-Angriff vor, wenn eine gültige Transaktion auf einem Blockchain böswillig auf einem anderen Blockchain reproduziert wird, der die gleiche Transaktionshistorie hat. Mit anderen Worten, eine auf einem Kanal übertragene Transaktion kann auf einem anderen Kanal ohne die Zustimmung des Absenders der ersten Transaktion reproduziert werden.


Nehmen wir das Beispiel eines hypothetischen Hard Fork von Bitcoin, genannt "*BitcoinBis*". Wenn Sie eine Zahlung in Bitcoins leisten, um ein Baguette von einem Bäcker auf dem realen Blockchain Bitcoin zu kaufen, könnte derselbe Bäcker diese legitime Transaktion auf *BitcoinBis* wiederholen, um denselben Betrag in Kryptowährungen auf diesem Fork zu erhalten, ohne dass Sie etwas dafür tun müssten.


Diese Art des Angriffs kann nur bei Blockchain-Verzweigungen mit 2 unabhängigen Ketten, die über einen längeren Zeitraum bestehen, auftreten. Typischerweise wäre dies der Fall bei Hard Fork. Damit ein Replay-Angriff möglich ist, müssen die beiden Blockchains eine gemeinsame Geschichte haben, und die duplizierte Transaktion muss als Input UTXOs verwenden, die aus früheren Transaktionen stammen, die vor der Aufspaltung der beiden Ketten stattfanden, oder aus früheren Transaktionen, die selbst bereits in einem früheren Replay-Angriff wiedergegeben wurden.


Im Allgemeinen besteht ein Replay-Angriff in der Datenverarbeitung darin, dass gültige Daten abgefangen und wiederverwendet werden, um ein System durch Wiederholung der ursprünglichen Übertragung zu täuschen. Dies kann manchmal zu einem Identitätsdiebstahl in einem Netzwerk führen.


> ► *Im Falle eines Replay-Angriffs auf eine Bitcoin-Transaktion wird dies manchmal einfach als "Replay-Transaktion" bezeichnet. "*