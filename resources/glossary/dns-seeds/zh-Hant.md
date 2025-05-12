---
term: DNS 種子
---

新加入網路的 Bitcoin 節點的初始連線點。這些種子實際上是特定的 DNS 伺服器，它們的 Address 永久嵌入在 Bitcoin 核心程式碼中。當一個新節點啟動時，它會聯絡這些伺服器，以取得一個隨機的 IP 位址清單，這些 IP 位址應該是活躍的 Bitcoin 節點。然後，新節點可以與此清單上的節點建立連線，以取得執行初始區塊下載 (IBD) 所需的資訊，並與累積工作最多的鏈同步。截至 2024 年，以下是 Bitcoin 核心 DNS 種子清單，以及負責其維護的個人 (https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp)：


- seed.Bitcoin.sipa.be：Pieter Wuille；
- dnsseed.bluematt.me：Matt Corallo；
- dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us：Luke Dashjr；
- seed.bitcoinstats.com：Christian Decker；
- seed.Bitcoin.jonasschnelli.ch：Jonas Schnelli；
- seed.btc.petertodd.net：Peter Todd；
- seed.Bitcoin.sprovoost.nl：Sjors Provoost；
- dnsseed.emzy.de：Stephan Oeste；
- seed.Bitcoin.wiz.biz：Jason Maurice；
- seed.Mainnet.achownodes.xyz：Ava Chow.


按照優先順序，DNS 種子是 Bitcoin 節點建立連線的第二種方法。第一種方法是使用節點自己建立的 peers.dat 檔案。如果是新節點，此檔案自然是空的，除非使用者手動修改。


> ► *注意，DNS 種子不應與「seed 節點」混淆，「seed 節點」是建立連線的第三種方式。