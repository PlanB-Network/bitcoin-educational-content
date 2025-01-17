---
term: HMAC-SHA512

---
hMAC-SHA512" steht für "Hash-based Message Authentication Code - Secure Hash Algorithm 512". Es handelt sich um einen kryptographischen Algorithmus zur Überprüfung der Integrität und Authentizität von Nachrichten, die zwischen zwei Parteien ausgetauscht werden. Er kombiniert die kryptografische Hash-Funktion `SHA512` mit einem gemeinsamen geheimen Schlüssel, um einen eindeutigen Message Authentication Code (MAC) für jede Nachricht zu erzeugen.

Im Zusammenhang mit Bitcoin ist die natürliche Verwendung von "HMAC-SHA512" leicht abgeleitet. Dieser Algorithmus wird für den deterministischen und hierarchischen Ableitungsprozess des kryptografischen Schlüsselbaums einer Geldbörse verwendet. insbesondere wird "Hmac-SHA512" verwendet, um vom Seed-Schlüssel zum Master-Schlüssel zu gelangen und dann für jede Ableitung von einem Elternpaar zu Kindpaaren. Dieser Algorithmus ist auch in einem anderen Ableitungsalgorithmus namens "PBKDF2" enthalten, der verwendet wird, um von der Wiederherstellungsphrase und der Passphrase zum Seed zu gelangen.