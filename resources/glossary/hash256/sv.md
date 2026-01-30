---
term: HASH256
definition: Funktion som applicerar SHA256 två gånger i följd, används i olika Bitcoin-applikationer.
---

Kryptografisk funktion som används för olika applikationer på Bitcoin. Det innebär att SHA256-funktionen tillämpas två gånger på indata. Meddelandet passerar genom SHA256 en gång och resultatet av denna operation används som indata för en andra passage genom SHA256. Utdata från denna funktion är därför 256 bitar.


$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$$