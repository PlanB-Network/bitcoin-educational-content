---
term: CHAIN CODE
---

Im Kontext der hierarchischen deterministischen (HD) Ableitung von Bitcoin-Wallets ist der Chain Code ein 256-Bit kryptografischer Salt-Wert, der verwendet wird, um Kind-Schlüssel aus einem Elternschlüssel zu generieren, entsprechend dem BIP32-Standard. Der Chain Code wird in Kombination mit dem Elternschlüssel und dem Index des Kindes verwendet, um deterministisch ein neues Paar von Schlüsseln (privater Schlüssel und öffentlicher Schlüssel) zu generieren, ohne den Elternschlüssel oder andere abgeleitete Kind-Schlüssel preiszugeben.

Daher gibt es für jedes Paar von Schlüsseln einen einzigartigen Chain Code. Der Chain Code wird entweder durch Hashing des Wallet-Seeds und Übernahme der rechten Hälfte der Bits erhalten. In diesem Fall wird er als Master Chain Code bezeichnet, der mit dem Master-Privatschlüssel verbunden ist. Alternativ kann er durch Hashing eines Elternschlüssels mit seinem Eltern-Chain Code und einem Index erhalten werden, wobei dann die rechten Bits behalten werden. Dies wird dann als Kind-Chain Code bezeichnet.

Ohne Kenntnis des mit jedem Elternpaar verbundenen Chain Codes ist es unmöglich, Schlüssel abzuleiten. Er führt pseudozufällige Daten in den Ableitungsprozess ein, um sicherzustellen, dass die Erzeugung kryptografischer Schlüssel für Angreifer unvorhersehbar bleibt, während sie für den Wallet-Inhaber deterministisch ist.

> ► *Auf Englisch wird ein "code de chaîne" als "chain code" bezeichnet, und ein "code de chaîne maître" als "master chain code".*