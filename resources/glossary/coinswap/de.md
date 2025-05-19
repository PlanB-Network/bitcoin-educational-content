---
term: COINSWAP
---

Protokoll für die geheime Übertragung von Ownership zwischen Nutzern. Diese Methode zielt darauf ab, den Besitz von Bitcoins von einer Person auf eine andere zu übertragen und umgekehrt, ohne dass diese Exchange ausdrücklich auf der Blockchain sichtbar sind. Coinwap verwendet intelligente Verträge, um die Übertragung ohne die Notwendigkeit von Vertrauen zwischen den Parteien durchzuführen.


Stellen wir uns ein naives Beispiel (das nicht funktioniert) mit Alice und Bob vor. Alice besitzt 1 BTC, das mit dem privaten Schlüssel $A$ gesichert ist, und Bob besitzt ebenfalls 1 BTC, das mit dem privaten Schlüssel $B$ gesichert ist. Theoretisch könnten sie ihre privaten Schlüssel über einen externen Kommunikationskanal Exchange austauschen, um eine geheime Überweisung durchzuführen. Diese naive Methode birgt jedoch ein hohes Risiko in Bezug auf das Vertrauen. Nichts hindert Alice daran, nach dem Exchange eine Kopie des privaten Schlüssels $A$ zu behalten und sie später zu benutzen, um die Bitcoins zu stehlen, sobald der Schlüssel in Bobs Händen ist. Außerdem gibt es keine Garantie, dass Alice nicht Bobs privaten Schlüssel $B$ erhält und ihren privaten Schlüssel $A$ im Exchange nicht weitergibt. Dieses Exchange beruht also auf einem übermäßigen Vertrauen zwischen den Parteien und ist nicht geeignet, eine sichere, geheime Übertragung von Ownership zu gewährleisten.


Um diese Probleme zu lösen und den Münztausch zwischen Parteien zu ermöglichen, die einander nicht vertrauen, werden wir Smart contract-Systeme verwenden, die den Exchange "atomar" machen. Dies können HTLC (*Hash Time-Locked Contracts*) oder PTLC (*Point Time-Locked Contracts*) sein. Diese beiden Protokolle funktionieren auf ähnliche Weise und verwenden ein Time-Locking-System, das sicherstellt, dass der Exchange entweder erfolgreich abgeschlossen oder vollständig storniert wird, wodurch die Integrität der Gelder beider Parteien geschützt wird. Der Hauptunterschied zwischen HTLC und PTLC besteht darin, dass HTLC Hashes und Preimages zur Sicherung der Transaktion verwendet, während PTLC Adaptor Signatures einsetzt.


In einem Coinswap-Szenario mit einem HTLC oder PTLC zwischen Alice und Bob findet der Exchange auf sichere Weise statt: Entweder ist er erfolgreich und jeder erhält die BTC des anderen, oder er scheitert und jeder behält seine eigenen BTC. Dadurch ist es für beide Parteien unmöglich, zu betrügen oder die BTC der anderen Partei zu stehlen.


Die Verwendung von Adaptor Signatures ist in diesem Zusammenhang besonders interessant, da sie den Verzicht auf traditionelle Skripte ermöglicht (ein Mechanismus, der manchmal als "_scriptless scripts_" bezeichnet wird). Dadurch werden die mit der Exchange verbundenen Kosten reduziert. Ein weiterer großer Vorteil von Adaptor Signatures besteht darin, dass sie nicht die Verwendung eines gemeinsamen Hash für beide Parteien der Transaktion erfordern, wodurch die Notwendigkeit vermieden wird, eine direkte Verbindung zwischen ihnen in bestimmten Arten von Exchange offenzulegen.