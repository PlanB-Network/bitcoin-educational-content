---
term: Node
definition: Computer waarop een Bitcoin-client draait en die deelneemt aan het netwerk door een kopie van de blockchain bij te houden.
---

In het Bitcoin netwerk is een knooppunt (of "node" in het Engels) een computer waarop een Bitcoin protocolclient draait (zoals bijvoorbeeld Bitcoin core). Het neemt deel aan het netwerk door een kopie van Blockchain te onderhouden, transacties en nieuwe blokken door te geven en te verifiëren, en optioneel door deel te nemen aan het Mining proces. De som van alle Bitcoin knooppunten vertegenwoordigt het Bitcoin netwerk zelf.


Er zijn verschillende soorten knooppunten in Bitcoin, waaronder volledige knooppunten en lichte knooppunten. Full nodes bewaren een complete kopie van Blockchain, verifiëren alle transacties en blokken volgens de consensusregels en nemen actief deel aan de verspreiding van transacties en blokken over het netwerk. Aan de andere kant houden light nodes, of SPV (*Simple Payment Verification*) nodes, alleen de headers van blokken bij en vertrouwen op full nodes voor het verkrijgen van transactie-informatie.


> ► *Sommigen maken ook onderscheid tussen zogenaamde "pruned nodes" ("pruned node" in het Engels). Dit zijn volledige knooppunten, die alle blokken van het Genesis blok downloaden en verifiëren, maar alleen de meest recente blokken in het geheugen bewaren.*