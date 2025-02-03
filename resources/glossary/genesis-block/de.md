---
term: GENESIS-BLOCK

---
Der Genesis Block ist der erste Block des Bitcoin-Systems. Er steht für den konkreten Start von Bitcoin. Der Genesis Block wurde von dem anonymen Gründer von Bitcoin, Satoshi Nakamoto, am 3. Januar 2009 erstellt. Sein Hash lautet:

```text
000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

Dieser Block enthält nur eine coinbase-Transaktion, die 50 Bitcoins als Belohnung für den Miner (in diesem Fall Satoshi Nakamoto selbst) erzeugt. Dieser Block enthält eine in die coinbase-Transaktion eingebettete Nachricht:

```text
The Times 03/Jan/2009 Chancellor on brink of second bailout for banks
```

Dieses Zitat ist ein Verweis auf einen Artikel der Zeitung *The Times*. Die Nachricht wird als Kritik am traditionellen Finanzsystem und seinen Exzessen interpretiert, die teilweise die Schaffung von Bitcoin als monetäre Alternative motivierten.

Da er den allerersten Block der Bitcoin-Blockchain verkörpert, hat der Genesis-Block natürlich kein Feld, das den Hash des vorherigen Blocks enthält (weil es keinen gibt). Außerdem sind die 50 Bitcoins, die in diesem Block als Belohnung generiert werden, auf Protokollebene nicht auszahlbar.