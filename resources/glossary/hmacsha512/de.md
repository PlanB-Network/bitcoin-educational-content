---
term: HMAC-SHA512
---

`HMAC-SHA512` steht für "Hash-based Message Authentication Code - Secure Hash Algorithm 512". Es handelt sich um einen kryptografischen Algorithmus, der verwendet wird, um die Integrität und Authentizität von Nachrichten zu überprüfen, die zwischen zwei Parteien ausgetauscht werden. Er kombiniert die kryptografische Hash-Funktion `SHA512` mit einem gemeinsamen Geheimschlüssel, um für jede Nachricht einen einzigartigen Message Authentication Code (MAC) zu generieren.

Im Kontext von Bitcoin wird die natürliche Verwendung von `HMAC-SHA512` leicht abgeleitet. Dieser Algorithmus wird im deterministischen und hierarchischen Ableitungsprozess des kryptografischen Schlüsselbaums einer Wallet verwendet. `HMAC-SHA512` wird insbesondere eingesetzt, um vom Seed zum Master-Schlüssel zu gelangen und dann bei jeder Ableitung von einem Elternpaar zu Kindpaaren. Dieser Algorithmus findet sich auch in einem anderen Ableitungsalgorithmus namens `PBKDF2`, der verwendet wird, um von der Wiederherstellungsphrase und Passphrase zum Seed zu gelangen.