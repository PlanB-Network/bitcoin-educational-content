---
term: 初始區塊下載 (IBD)
---

指節點從 Genesis 區塊下載和驗證 Blockchain，並與 Bitcoin 網路中其他節點同步的過程。啟動新的 Full node 時必須執行 IBD。在初始同步開始時，節點沒有先前交易的資訊。因此，它會從網路中的其他節點下載每個區塊，驗證其有效性，然後將其加入本地版本的 Blockchain。值得注意的是，由於 Blockchain 和 UTXO 集的大小不斷增加，IBD 可能會變得冗長且資源密集。其執行速度取決於託管該節點的電腦的運算能力、其 RAM 容量、儲存裝置的速度以及頻寬。為了讓您有個概念，如果您有強大的網際網路連線，而且節點寄存在最新款的 MacBook 上，並有充足的記憶體，IBD 只需要幾個小時。相反，如果您使用的是 Raspberry Pi 之類的微型電腦，IBD 可能需要一個星期或更長的時間。


> ► *在法語中，一般接受直接指 IBD。有時使用的翻譯是 "synchronisation initiale「，或 」téléchargement initial des blocs"。