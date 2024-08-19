---
term: HASHCASH
---

HashCash ist ein Proof-of-Work-System, das 1997 von Adam Back entwickelt wurde, um Spam und DoS-Angriffe zu bekämpfen. Es basiert auf dem Prinzip, dass ein Absender eine Rechenaufgabe erfüllen muss (speziell das Finden einer partiellen Kollision bei einer kryptografischen Hashfunktion), um seine Arbeit zu beweisen. Diese Aufgabe ist für den Absender in Bezug auf Zeit und Energie kostspielig, aber das Überprüfen des Ergebnisses durch den Empfänger ist schnell und einfach. Dieses Protokoll hat sich insbesondere im Kampf gegen Spam in E-Mail-Kommunikationen als besonders geeignet erwiesen, da es für legitime Nutzer minimal belastend ist, während es für Spammer ein signifikantes Hindernis darstellt. Tatsächlich erfordert das Senden einer einzelnen E-Mail einige Sekunden Rechenzeit, aber diese Operation millionenfach zu replizieren, wird in Bezug auf Energie und Zeit extrem kostspielig, was oft das wirtschaftliche Interesse von Spam-Kampagnen, ob zu Marketingzwecken oder bösartig, zunichte macht. Zudem ermöglicht es die Wahrung der Anonymität des Absenders.

HashCash wurde schnell von Cypherpunks adoptiert, die ein anonymes elektronisches Währungssystem ohne Zwischenhändler entwickeln wollten. Tatsächlich führte Adam Backs Innovation erstmals das Konzept der Knappheit in der digitalen Welt ein. Das Konzept des Proof of Work findet sich dann in mehreren elektronischen Währungssystemen, die Bitcoin vorausgingen, einschließlich:
* b-money von Wei Dai, veröffentlicht im Jahr 1998;
* R-POW von Hal Finney, veröffentlicht im Jahr 2004;
* BitGold von Nick Szabo, veröffentlicht im Jahr 2005.

Das Prinzip von HashCash findet sich auch im Bitcoin-Protokoll, wo es als Schutzmechanismus gegen Sybil-Angriffe verwendet wird.