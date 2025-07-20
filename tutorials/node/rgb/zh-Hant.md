---
name: RGB
description: RGB 上的介紹與資產建立
---

![RGB vs Ethereum](assets/0.webp)


## 引言


2009 年 1 月 3 日，Satoshi Nakamoto 發射了第一個 Bitcoin 節點，從那一刻起，新的節點加入，Bitcoin 開始表現得猶如一種新的生命形式，這種生命形式並沒有停止進化，由於其獨特的設計，Bitcoin 已經逐漸成為世界上最安全的網路，Satoshi 非常周全地考慮到了這一點，因為通過經濟誘因，它吸引了通常稱為礦工的用戶投資能源和計算能力，這有助於網路安全。


隨著 Bitcoin 的持續成長和採用，它面臨著可擴展性的問題，Bitcoin 網路允許在大約 10 分鐘的時間內挖出一個有交易的新區塊，假設我們一天有 144 個區塊，每個區塊的最大值為 2700 個交易，Bitcoin 每秒只能允許 4.5 個交易，Satoshi 已經意識到這個限制，我們可以在 2011 年 3 月寄給 Mike Hearn 的電子郵件1 中看到，他在郵件中解釋了我們今天所知的支付管道是如何運作的。微支付快速且安全，無需等待確認。這就是 off-chain 協定的用武之地。


根據 Christian Decker2 的說法，off-chain 通訊協定通常是使用者使用 Blockchain 的資料並進行管理的系統，直到最後一刻才會碰觸到 Blockchain 本身。基於這個概念，Lightning Network 誕生了，這個網路使用 off-chain 通訊協定，讓 Bitcoin 付費幾乎可以瞬間完成，由於並非所有這些操作都會寫在區塊鏈上，因此它允許每秒上千筆交易，並擴大 Bitcoin 的規模。


在 Bitcoin 上的 off-chain 協定領域的研究和開發打開了一個潘多拉盒子，今天我們知道，我們可以以分散的方式實現遠遠超過價值轉移的目標，非營利性的 LNP/BP 標準協會專注於在 Bitcoin 和 Lightning Network 上的 Layer 2 和 3 協定的開發，在這些專案中，RGB 脫穎而出。


## 什麼是 RGB？


RGB 源自 Peter Todd3 對單次使用封條和客戶端驗證的研究，Giacomo Zucco 和社群在 2016-2019 年將其創造為 Bitcoin 和 Lightning Network 的更佳資產通訊協定。這些想法的進一步演進，促使 Maxim Orlovsky 將 RGB 發展為完整的 Smart contract 系統，並自 2019 年起在社群參與下帶領實作。


我們可以將 RGB 定義為一套開放原始碼協定，讓我們能以可擴充和保密的方式執行複雜的智慧型契約。它不是一個特定的網路（如 Bitcoin 或 Lightning）；每個 Smart contract 只是一組 Contract 參與者，這些參與者可以使用不同的通訊管道進行互動（預設為 Lightning Network）。RGB 使用 Bitcoin Blockchain 作為狀態 Commitment 的 Layer，並維護 Smart contract 的程式碼和資料 off-chain，這使得它具有可擴展性，利用 Bitcoin 交易 (和 Script) 作為智慧契約的 Ownership 控制系統；而 Smart contract 的演進則由 off-chain 方案定義，最後需要注意的是，所有東西都是在客戶端進行驗證。


簡單來說，RGB 是一個允許使用者隨時審核 Smart contract、執行它並個別驗證它的系統，而不需要額外的成本，因為它不像 「傳統 」系統那樣使用 Blockchain，複雜的智慧契約系統由 Ethereum 開創，但由於它要求使用者每次操作都要花費大量的汽油，他們從來沒有達到承諾的可擴展性，因此它從來沒有成為被排除在現有金融系統之外的使用者的銀行選擇。


目前，Blockchain 業界提倡智慧型契約的程式碼與資料都必須儲存在 Blockchain，並由網路的每個節點執行，不論規模的過度增加或計算資源的濫用。RGB 所提出的方案更智慧、更有效率，因為它切割了 Blockchain 的範式，將智慧契約與資料從 Blockchain 中分離出來，因此避免了其他平台所見的網路飽和問題，反過來，它也不會強制每個節點執行每個 Contract，而是由相關各方執行，這將機密性提升到前所未有的層級。


![RGB vs Ethereum](assets/1.webp)


## RGB 中的智慧型契約


在 RGB 中，Smart contract 開發者定義了一個方案，指定了 Contract 隨時間演變的規則。該方案是 RGB 中建構智慧契約的標準，在定義發行 Contract 時，發行者和 Wallet 或 Exchange 都必須遵守特定方案，並根據該方案驗證 Contract。只有驗證無誤，各方才能接受請求並處理資產。


RGB 中的 Smart contract 是狀態變更的 Directed Acyclic Graph (DAG)，其中只有圖形的一部分永遠是已知的，其他部分無法存取。RGB 方案是 Smart contract 開始時這個圖形演變的核心規則集。每個 Contract Participant 都可以增加這些規則（如果 Schema 允許的話），而結果圖形就是由這些規則的反覆應用所建立的。


## 可變資產


RGB 中的可替代資產遵循 LNPBP RGB-20 規範4，當定義一個 RGB-20 時，被稱為 "Genesis 資料''的資產資料會透過 Lightning Network 發佈，其中包含使用資產所需的內容。最基本形式的資產不允許二次發行、代幣燒錄、重新命名或替換。


有時候，發行者需要在未來發行更多代用幣，也就是穩定幣，例如 USDT，這可以讓每個代用幣的價值與美元等通貨膨脹貨幣的價值掛鈎。為了達到這個目的，存在更複雜的 RGB-20 方案，除了 Genesis 資料之外，他們還要求發行者生產託付品，這些託付品也會在 Lightning Network 中流通；有了這個資料，我們就可以知道資產的總流通 Supply。這同樣適用於燒毀資產或更改其名稱。


與資產相關的資訊可以是公開或隱私的：如果發行者需要保密，他/她可以選擇不分享代幣的相關資訊，並在絕對隱私的情況下執行操作，但我們也有相反的情況，即發行者和持有人需要整個過程是透明的。這可以透過分享代幣資料來達成。


## RGB-20 程序


燒錄程序會停用代幣，已燒錄的代幣無法再使用。


替換程序發生在代幣被燒毀，並創建相同代幣的新數量時。這有助於減少資產歷史資料的大小，對維持資產速度非常重要。


為了支援有可能燒毀資產而無需更換的使用個案，RGB-20 的子方案只允許燒毀資產。


## 不可替代資產


RGB 中的不可偽造資產遵循 LNPBP RGB-21 規範5，當我們使用 NFT 時，我們也有一個主方案和子方案。這些方案有一個雕刻程序，允許我們按代用幣擁有者的部分附加自訂資料，目前我們在 NFT 中最常見的例子是與代用幣相連的數位藝術。代幣發行者可以透過使用 RGB-21 子方案禁止此資料雕刻。與其他 NFT Blockchain 系統不同，RGB 允許以完全分散且可抵擋審查的方式散佈大型媒體代幣資料，利用稱為 Bifrost 的 Lightning P2P 網路擴充，該網路也用於建立許多其他形式的 RGB 特有 Smart contract 功能。


除了可替代資產和 NFT 之外，RGB 和 Bifrost 還可用於產生其他形式的智慧契約，包括 DEXes、流動資金池、演算法穩定幣等，我們將在未來的文章中加以介紹。


## 來自 RGB 的 NFT vs 來自其他平台的 NFT



- 不需要昂貴的 Blockchain 儲存設備
- 不需要 IPFS，而是使用 Lightning Network 擴充套件 (稱為 Bifrost) (而且是完全端對端加密的)
- 不需要特殊的資料管理解決方案 - Bifrost 再次擔當此角色
- 無需信任網站來維護 NFT 代幣或有關發行資產 / Contract ABI 的資料
- 內建 DRM 加密與 Ownership 管理功能
- 使用 Lightning Network (Bifrost) 備份的基礎架構
- 將內容貨幣化的方法（不僅出售 NFT 本身，還出售內容的存取權，多次出售）


## 結論


自從幾乎 13 年前推出 Bitcoin 以來，我們在這個領域進行了大量的研究和實驗，無論是成功還是失敗，都讓我們對去中心化系統在實際中的行為有了更多的瞭解，是什麼讓它們真正去中心化，又是什麼行為會讓它們傾向於中心化，所有這些都讓我們得出結論，真正的去中心化是一種罕見且難以實現的現象，真正的去中心化只有 Bitcoin 實現了，也正是因為這個原因，我們才會集中精力在 Bitcoin 的基礎上進行建構。


RGB 在 Bitcoin 兔子洞中有自己的兔子洞，當我從它們中掉下來時，我會把我所學到的發佈出來，在下一篇文章中，我們將介紹 LNP 和 RGB 節點以及如何使用它們。



- 1 https://plan99.net/~mike/Satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md


# RGB 節點教學


## 簡介


在本教學中，我們將解釋如何使用 RGB-node 來建立可替代的代幣，以及如何轉移代幣，本文件是以 RGB-node demo 為基礎，不同之處在於本教學使用真實的 Testnet 資料，為此，從現在開始，我們必須建立自己的 Partially Signed Bitcoin Transaction、PSBT。


## 要求


建議使用 Linux 發行版，本教學是使用 Pop!OS 寫成的，它以 Ubuntu 為基礎，您將需要：



- 貨物
- Bitcoin 核心
- 笨蛋


註記: 本教學展示在 Linux 終端執行指令的過程，為了區分使用者所寫的內容和他在終端得到的回應，我們加入了象徵 bash 提示的 $。


您需要安裝一些相依性：


```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```


建立與執行


RGB-node 是一項進行中的工作 (WIP)，因此我們必須將自己定位在特定的 commit (3f3c520c19d84c66d430e76f0fc68c5a66d79c84)，才能正確編譯和使用它，為此我們執行下列指令。


```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```


現在我們編譯它，別忘了使用 --locked 標誌，因為在 clap 的一個版本中引入了一個突破性的變更。


```
$ cargo install --path . --all-features --locked

....
....
Finished release [optimized] target(s) in 2m 14s
Installing /home/user/.cargo/bin/fungibled
Installing /home/user/.cargo/bin/rgb-cli
Installing /home/user/.cargo/bin/rgbd
Installing /home/user/.cargo/bin/stashd
Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```


正如 Rust 編譯器告訴我們的，二進位檔被複製到 $HOME/.cargo/bin 目錄下，如果您的編譯器將二進位檔複製到其他地方，您必須確保 $PATH 中必須包含該目錄。


在已安裝的二進位檔中，我們可以看到三個 daemons 或服務 (以 d 結尾的檔案) 和一個 CLI（指令行 Interface），CLI 可讓我們與主 rgbd daemon 互動。在本教程中，我們要執行兩個節點，因此也需要兩個用戶端，每個用戶端都必須連線到自己的節點，為此我們要建立兩個別名。


```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```


我們可以直接執行別名，或是將它們加入 $HOME/.bashrc 檔案的末尾，然後執行原始碼 $HOME/.bashrc。

前提


RGB-node 不會處理任何與 Wallet 相關的功能，它只是執行 RGB 的特定任務，而這些任務將由外部 Wallet 提供，例如 Bitcoin core。特別是，為了展示具有發行和傳輸功能的基本工作流程，我們將需要：



- RGB-node-0 將與新發行的資產綁定的 issuance_utxo
- A receive_utxo，其中 RGB 節點-1 接收資產
- RGB-node-0 接收資產變更的 change_utxo
- 一個 Partially Signed Bitcoin Transaction (tx.PSBT)，其輸出的公開金鑰會被調整為包含一個 Commitment 到傳輸。


我們將使用 Bitcoin 核心 CLI，我們需要在 Testnet 上執行 bitcoind daemon，這將使我們具有互操作性，最後，我們將能夠向其他遵循本教學的 RGB 使用者發送我們自己的資產。


為了簡單起見，我們會在 ~/.bashrc 檔案的最後加入這個別名。


```
alias bcli="bitcoin-cli -testnet"
```


讓我們列出未支出的輸出交易，並選取兩個，一個是 issuance_utxo，另一個是 change_utxo，至於是哪一個並不重要，重要的是發行者可以控制這兩個 UTXO。


```
$ bcli listunspent
[
{
"txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
"vout": 1,
"address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
"label": "",
"scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
"amount": 0.01703963,
"confirmations": 62432,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
"safe": true
},
{
"txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
"vout": 1,
"address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
"scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
"amount": 0.02877504,
"confirmations": 189184,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
"safe": true
}
]
```


在進一步討論之前，我們需要先談談輸出點，單一交易可以包含多個輸出，輸出點包含 32 位元組的 txid 和 4 位元組的輸出索引號碼 (vout)，以冒號 : 分隔來指代特定的輸出。在我們的 listunspent 輸出中，我們可以找到兩個 UTXO，在每個 UTXO 上我們都可以看到 txid 和 vout，這些就是 out issuance_utxo 和 change_utxo 的輸出點。


receive_utxo 是由接收器控制的 UTXO，在本例中，我們將使用 e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0，這是來自另一個 Wallet 的輸出點。



- issuance_utxo：4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0


我們現在要建立一個部分簽章的交易 (tx.PSBT)，其輸出會被調整為包含轉移的提交，記得把 txid 和 vout 替換成您自己的，目的地 Address 並不重要，它可以是您的，也可以是其他人的，那些 Sats 到哪裡也不重要，重要的是我們使用 issuance_utxo。


```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
"psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
"fee": 0.00000280,
"changepos": 0
}
```


輸出給我們一個 base64 編碼的 PSBT，我們將用它來建立 tx.PSBT。


```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```


讓我們建立一個名為 rgbdata 的新目錄，每個節點的資料目錄都存放在這個目錄中。


```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```


已經位於 $HOME/rgbdata 中，我們在不同的終端啟動每個節點，其中 ~/.cargo/bin 是 RGB 節點安裝後，cargo 複製所有 binaries 的目錄。


```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```


## 發行


要發行資產，我們使用可替代發行子指令執行 rgb0-CLI，然後輸入參數、股票代碼 USDT、名稱「USD Tether」，在分配中我們將使用發行金額和 issuance_utxo，如下所示：


```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```


資產成功發行。使用此資訊進行分享：

資產資訊：


```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"


genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```


我們得到 assetId，我們需要它來轉移資產。


```
$ rgb0-cli fungible list

- name: USD Tether
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
```


## generate blinded UTXO


為了接收新的 USDT，RGB-node-1 需要 generate 與 receive_utxo 對應的 blinded UTXO 來持有資產。


```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```


為了能夠接受與此 UTXO 相關的轉帳，我們需要原始的 receive_utxo 和 blinding_factor。


## 轉移


若要將資產的某個數額轉移到 RGB-node-1 ，我們需要將其傳送至 blinded UTXO，RGB-node-0 需要建立 Consignment 和揭露，並將其提交到 Bitcoin 交易中。然後，我們需要一個 PSBT，我們會修改 PSBT 以包含提交。此外，-i 和 -a 選項允許我們提供一個輸入外點，這個外點將是資產的來源，也是我們接收變更的分配點，我們必須以下列方式 @<change_utxo> 表示。


```
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1

Transfer succeeded, consignments and disclosure are written to "consignment.rgb" and "disclosure.rgb", partially signed witness transaction to "witness.psbt"
Consignment data to share:consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
```


這會寫入三個新檔案，Consignment、disclosure 和包含調整的 PSBT，這個 PSBT 稱為 Witness Transaction，Consignment 會傳送到 RGB-node-1。


## 見證


Witness Transaction 應該被簽署並廣播，為此我們需要將其 base64 編碼回。


```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```


使用 walletprocesspsbt 子指令簽署。


```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
{
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",
"complete": true
}
```


現在敲定並取得六角。


```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="
{
"hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
"complete": true
}
```


## 廣播


使用 sendrawtransaction 子指令進行廣播，使其確認進入 Blockchain。


```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"
8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```


## 接受


若要接受傳入的傳輸，RGB-節點-1 應已收到來自 RGB-node-0 的 Consignment 檔案，並已在產生 UTXO 盲點時產生 receive_utxo 和相對應的 blinding_factor。


```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Asset transfer successfully accepted.
```


我們現在可以透過執行 <receive_utxo> 看到 (在 knownAllocations 欄位中) 新分配的 100 個資產單位：


```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 1
outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
revealedAmount:
value: 100
blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```


由於轉帳時 receive_utxo 是 blinded，付款人 RGB-node-0 沒有關於 100 USDT 被送到何處的資訊，所以 knownAllocations 中沒有顯示該位置。


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```


但您可以看到，RGB-節點-0 無法看到我們用 -a 參數提供給 transfer 指令的 900 項資產變更。要註冊這項變更，RGB-節點-0 需要接受披露。


```
$ rgb0-cli fungible enclose disclosure.rgb

Disclosure data successfully enclosed.
```


如果 RGB-node-0 成功，您可以透過列出資產來查看變更。


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 0
outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
revealedAmount:
value: 900
blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
```


## 結論


如果我們檢查 Block explorer 中已確認的交易，我們不會發現任何與一般交易不同的地方，這要歸功於 RGB 使用單次使用的印章來調整交易，在這篇文章中，我將介紹 RGB 如何運作。


這篇文章可能有 bug，如果您發現了什麼，請讓我知道，以改善本指南，建議和批評也是歡迎的，快樂的黑客！🖖