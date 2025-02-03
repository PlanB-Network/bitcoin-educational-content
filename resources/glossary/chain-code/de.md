---
term: CHAIN CODE

---
Im Zusammenhang mit der hierarchisch-deterministischen (HD) Ableitung von Bitcoin-Wallets ist der Kettencode ein kryptografischer 256-Bit-Salzwert, der gemäß dem BIP32-Standard verwendet wird, um aus einem Elternschlüssel Kindschlüssel zu generieren. Der Kettencode wird in Kombination mit dem Elternschlüssel und dem Index des Kindes verwendet, um auf deterministische Weise ein neues Schlüsselpaar (privater Schlüssel und öffentlicher Schlüssel) zu erzeugen, ohne den Elternschlüssel oder andere abgeleitete Kindschlüssel preiszugeben.

Daher gibt es für jedes Schlüsselpaar einen eindeutigen Kettencode. Der Kettencode wird entweder durch Hashing des Seed der Brieftasche und die rechte Hälfte der Bits ermittelt. In diesem Fall handelt es sich um einen Hauptkettencode, der mit dem privaten Hauptschlüssel verknüpft ist. Alternativ kann er auch durch Hashing eines übergeordneten Schlüssels mit seinem übergeordneten Kettencode und einem Index ermittelt werden, wobei die rechten Bits beibehalten werden. In diesem Fall spricht man von einem Child-Chain-Code.

Es ist unmöglich, Schlüssel abzuleiten, ohne den Kettencode zu kennen, der mit jedem Elternpaar verbunden ist. Es führt Pseudo-Zufallsdaten in den Ableitungsprozess ein, um sicherzustellen, dass die Generierung kryptografischer Schlüssel für Angreifer unvorhersehbar bleibt, während sie für den Inhaber der Brieftasche deterministisch ist.

> ► *Im Englischen wird ein "code de chaîne" als "chain code" und ein "code de chaîne maître" als "master chain code" bezeichnet.*