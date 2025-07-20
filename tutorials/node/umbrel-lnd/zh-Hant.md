---
name: Umbrel LND
description: 在 Umbrel 上安裝和設定 Lightning Network Daemon (LND) 的進階教學
---
![cover](assets/cover.webp)




## 簡介



本進階教學將帶您逐步完成在您的 Umbrel 節點上安裝、配置和使用 Lightning Node (LND) 應用程式。您將學習如何開啟頻道、管理您的流動資金，以及將您的節點與行動應用程式同步。



## 1.先決條件：正常運作的 Bitcoin Umbrel 節點



在部署 Lightning 之前，您需要在 Umbrel 上有一個完全運作的 Bitcoin 節點。這包括安裝 Umbrel（在 Raspberry Pi、NAS 或其他機器上），並完全同步 Blockchain Bitcoin。



若要安裝 Umbrel 並設定您的 Bitcoin 節點，建議您遵循我們的專用教學 ：



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

請確定您的 Bitcoin 節點是最新且運作正常，因為 Lightning Network 的所有 off-chain 交易都仰賴它。



## 2.Lightning Network 簡介



Lightning Network 是第二個 Layer 通訊協定，目的是在主 Blockchain 以外進行 Bitcoin 交易，以加快交易速度並降低交易成本。



具體而言，Lightning 使用節點間的付款通道網路：兩位使用者透過攔截 On-Chain BTC (初始交易) 來開啟通道，然後可在此通道內立即進行 Exchange 付款。這些 off-chain 交易不會記錄在 Blockchain 上，因此速度極快，成本幾乎為零。



付款可以通過多個渠道（感謝中介節點）到達網絡上的任何收款人，實現幾乎無限制規模的即時交易。因此，Lightning 可提供非常快速、低成本的交易，是日常支付或微型交易的理想選擇，同時可減輕 Blockchain Bitcoin 的負擔。



為了運作，Lightning 節點必須永久連接至網路，並與其他 Lightning 節點互動。目前有多種軟體實作（LND、Core Lightning、Eclair 等），這些軟體都能彼此相容。Umbrel 使用 LND (Lightning Network Daemon) 作為其官方 Lightning 節點應用程式的一部分。本教程主要介紹 LND。



如需 Lightning Network 的完整理論介紹，我們建議您參加我們的專門課程 ：



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

本課程將讓您徹底了解 Lightning Network 的基本概念，然後再進行 LND 節點的練習。



## 3.為什麼要自行託管 LND？



與託管或半託管解決方案相比，在 Umbrel 上操作您自己的 Lightning 節點 (LND) 可讓您對您的資金和渠道擁有完全的主權。



### Lightning 解決方案的比較 ：



**Solutions custodiales (ex: Wallet of Satoshi)** ：




- 您的 Lightning 比特幣由可信賴的第三方管理
- 易於使用，無複雜技術
- 營運商持有您的資金，並可追蹤您的交易
- 您犧牲了控制權和機密性



**非商品消費組合（如 Phoenix、Breez）** ：




- 使用者保留他們的私人金鑰，因此 Ownership 他們的 BTC
- 沒有完整的節點管理 - 應用程式在後台管理通道
- 簡約與主權之間的妥協
- 流動資金依賴供應商基礎設施
- 技術限制 (一部智慧型手機無法為其他手機路由付款)



**Self-hosted LND 節點 (Umbrel)** ：




- 最大主權：您的 On-Chain 和 off-chain BTC 完全由您控制
- 沒有第三方參與開通渠道或管理您的付款
- 提高保密性（您的通路和交易只有您和您的直接同行知道）
- 使用自由： 連接您自己的服務和錢包
- 可為他人進行路由交易（微額費用報酬）
- 增加技術責任（維護、流動資金管理、備份）



簡而言之，自行託管 LND 可讓您擁有最大的控制權，但需要更多的技術能力。這是便利性與主權之間的權衡。



## 4.逐步教學



### 4.1 在 Umbrel 上安裝和配置 Lightning Node 應用程式



一旦您的 Umbrel 節點 (Bitcoin) 已同步化，請遵循下列步驟 ：



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



從 Interface Umbrel 的「App Store」部分安裝 Lightning Node 應用程式。



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) 會以應用程式的形式部署在您的 Umbrel 上。當您第一次開啟它時，您會看到警告訊息，告知您「閃電」是一項實驗性技術。



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



您可以選擇建立新節點或從備份/seed 還原一個節點。第一次安裝時，請選擇建立新節點。Lightning Node 應用程式會 generate 一個 24 個字的 Mnemonic 詞組 (您的 seed Lightning)：請仔細寫下來 (最好是離線寫在紙上)，因為必要時會用它來還原您的 Lightning 資金。



**註：在最近版本的 Umbrel 上，安裝 Lightning 應用程式會提供這個 24 字的 seed（Bitcoin Umbrel 節點本身並不提供）。



![Interface principale de Lightning Node](assets/fr/04.webp)



初始化之後，您會存取 Lightning Node 的主 Interface。



![Paramètres de l'application](assets/fr/05.webp)



在應用程式設定中，您會發現許多重要的選項：




   - 諮詢您的節點 ID (您節點的唯一識別碼)
   - 連接外部 Wallet（連接 Wallet）
   - 檢視密語
   - 存取進階設定
   - 恢復通道
   - 下載頻道備份檔案
   - 啟用自動備份
   - 設定透過 Tor 備份 (Backup over Tor)



這些選項對於您的 Lightning 節點的安全和管理非常重要。請務必啟動自動備份，並妥善保管您的密語。



**有用的資源：**




- [Umbrel社群](https://community.umbrel.com) - 供使用者分享有關 Umbrel 及其生態系統的問題與解決方案的討論區


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Umbrel 上 Lightning Node 應用程式功能說明
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - 官方 LND 文件

### 4.2 開啟 Lightning 通道



一旦 LND 建立並運行，您就可以開啟第一個 Lightning 頻道。要尋找優質節點連接：



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/)是一個探索器，用來尋找可靠的節點來開啟通道。



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



例如，[ACINQ 節點](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) 是一個公認的節點，具有極佳的可用性和流動性統計。



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



本教學中，我們將與 [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca)開啟一個頻道。連線所需的資訊 (pubkey@ip:port) 已在他們的 Amboss 頁面上提供。



若要開啟通道 ：



![Bouton d'ouverture de canal](assets/fr/09.webp)



在 Lightning Node 首頁，按一下「+ OPEN CHANNEL」按鈕



![Configuration du canal](assets/fr/10.webp)



在頻道設定頁面中 ：




   - 貼上從 Amboss 複製的節點 ID (格式：pubkey@ip:port)
   - 定義頻道容量的大小 (某些節點如 ACINQ 有最小值，例如 400k Sats)
   - 必要時調整開戶交易費用



![Canal en cours d'ouverture](assets/fr/11.webp)



交易傳送完成後，頻道會在首頁顯示為「開啟」。等待 On-Chain 交易確認。



![Détails du canal](assets/fr/12.webp)



按一下頻道以檢視其詳細資訊：




   - 現況
   - 總容量
   - 流動資金明細（流入/流出）
   - 遠端節點的公開金鑰
   - 以及其他技術資訊



### 使用 Lightning Network+ 取得流入的流動資金



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ 可在 Umbrel App Store 中使用，讓您更輕鬆地獲得來源現金。



![Interface principale de LN+](assets/fr/14.webp)



主 Interface 提供三個重要選項：




- "流動資金交換：探索可用的交換要約
- "Open For Me」： 篩選您符合資格的交換項目
- 「至文件」：存取文件



![Message d'erreur LN+](assets/fr/15.webp)



注意：如果您尚未開啟頻道，點選「為我開啟」時會看到此錯誤訊息。



![Liste des swaps disponibles](assets/fr/16.webp)



流動資金交換」頁面顯示網路上所有可用的交換報價。



![Swaps éligibles](assets/fr/17.webp)



"Open For Me（為我開啟）」僅篩選您的節點符合所需條件的交換。



![Détails d'un swap](assets/fr/18.webp)



交換詳細資料範例 ：




- 五角形配置（5 名參與者）
- 每個通道的容量為 300k Sats
- 先決條件：至少 10 個開放通道，總容量為 1M Sats
- 有空位：4/5



### 4.3 與行動應用程式同步 (Zeus)



若要遠端 (智慧型手機) 控制您的 Lightning 節點，您可以使用 Zeus (iOS/Android 上的開放原始碼應用程式)。



**Zeus 配置與 Umbrel :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



確定您的 Umbrel 節點可以存取 (預設是透過 Tor)。


在 Interface Umbrel 中，開啟 Lightning Node 應用程式，然後按一下箭頭所示的「連接 Wallet」按鈕。



![Page de connexion avec QR code](assets/fr/20.webp)



此時會出現一個 QR 碼，包含 lndconnect 格式的 LND 存取資料。此 QR 代碼的資訊特別密集，因此請不要猶豫將其放大以方便閱讀。



![Configuration initiale de Zeus](assets/fr/21.webp)



在您的手機上 ：




   - 開啟宙斯
   - 在首頁點選「進階設定」，連接您自己的 Lightning 節點
   - 在參數中，選擇 「建立或連接 Wallet」。



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



在宙斯：




   - 選擇「LND (REST)」作為連線類型
   - 您可以掃描 QR 代碼（推薦方法）或手動輸入資訊。(不要猶豫放大 Umbrel QR 代碼，因為它非常密集）
   - 重要： 如果您的 Umbrel 只能透過 Tor（預設）存取，請啟動「使用 Tor」選項
   - 儲存設定



您的 Zeus 現在已連接到您的 Umbrel 節點，並允許您進行 Lightning 付款、檢視您的頻道、餘額等，同時保持完全自我管理。



**進階連線選項：**



預設情況下，Zeus ↔ Umbrel 連線是透過 Tor。若要更快速的連線，有兩種選擇：



**Lightning Node Connect (LNC)** ：




   - Lightning Labs 的加密連接機制
   - 在 Umbrel 上安裝 Lightning Terminal 應用程式 (包含 LNC 存取權限)
   - generate Lightning Terminal 中的連接 QR 碼 (連接 → 透過 LNC 連接 Zeus)
   - 掃描至 Zeus（選擇「LNC」作為連線類型）



**VPN Tailscale**：




   - 易於設定的網狀 VPN
   - 在 Umbrel (App Store) 和手機上安裝 Tailscale
   - 透過 Tailscale 私人 IP 連接 Zeus，而非 Tor Address



這些選項並非必須使用，Tor + Zeus 解決方案在大多數情況下都運作良好。



> **有用的資源：**
> - [Zeus Documentation - Umbrel Connection](https://community.umbrel.com/t/zeus-LN-mobile/7619) - 連接 Zeus 與 Umbrel 的官方指南
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Zeus 開放原始碼專案
> - [Umbrel Community - Connecting Zeus via Tailscale](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - 使用 Tailscale 將 Zeus 連接到 Umbrel 的指南

## 5.安全與最佳實務



管理自我託管的 Lightning 節點需要特別注意安全性。



### 節點的備份與安全性



**重要的備份類型**



您的 Lightning Umbrel 節點需要兩種類型的備份：



**seed句子 (24字)**




- 收回 On-Chain 資金
- 重新製作 Wallet 閃電的必要條件
- 用於超安全儲存（離線、紙上）



**Static Channel Backup (SCB)** 檔案




- 包含 Lightning 通道資訊
- 當發生碰撞時，允許強制關閉通道
- 重要：** 切勿手動儲存 `channel.db` 檔案 (有被懲處的風險)



**手動備份程序



若要手動儲存頻道 ：


1.存取 Lightning 節點功能表 (「+ Open Channel」旁邊的三點「⋮」)


2.下載頻道備份檔案


3.每次修改通道後，匯出新的 SCB


4.安全儲存 SCB（加密媒體、異地複本）



**Umbrel** 自動備份系統



Umbrel 具有精密的自動備份系統，可確保 ：



*資料保護：*




- 傳輸前的用戶端加密
- 透過 Tor 網路傳送
- 隨機填寫補充的資料
- 裝置唯一的加密金鑰



*強化安全性：*




- 狀態變更時立即備份
- 以隨機間隔進行「誘餌」備份
- 隱藏備份大小變更
- 保護時間分析



*修復過程：*




- 識別碼和鑰匙來自您的 seed Umbrel
- 僅使用 Mnemonic 語句即可進行完全修復
- 自動復原最新備份
- 還原頻道設定和資料



### 碰撞修復



如果您的節點遺失（硬體故障、SD 卡損毀） ：




- 重新安裝雨傘
- 在 Lightning 應用程式中輸入您的 24 字 seed
- 還原時匯入 SCB 檔案



LND 會聯繫您舊頻道的每個合作夥伴，關閉這些頻道，並收回您應佔的 On-Chain 資金。這些頻道將被永久關閉（如有必要可重新開啟）。



### 可用性與詐欺保護



理想情況下，儘可能經常將您的結留在線上。如果長期不在線




- 惡意的對等端可能試圖廣播舊的頻道狀態
- 閃電」規定「抗議期」（LND 約為 2 週）
- 如果您要長時間離開，請設定 Watchtower



**Watchtower 配置：**




- 在 LND 進階設定中，新增受信任 Watchtower 伺服器的 URL
- 您可以使用公共服務或安裝自己的 Watchtower




若要瞭解有關設定和使用 watchtowers 的更多資訊，建議您參閱我們的專用教學 ：



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### 其他最佳實踐





- 軟體更新：** 保持 Umbrel 和 LND 為最新版本 (安全修復)
- 硬體保護：** 使用穩定的系統 (Raspberry Pi 搭配 SSD、迷你電腦) 和 UPS
- 網路安全：** 保留預設 Tor 設定，變更 Umbrel 管理員密碼 (預設："moneyprintergobrrr")
- 加密：** 盡可能啟用磁碟加密



## 6.其他工具



Umbrel 的 Lightning Node 應用程式提供管理頻道的基本功能，但第三方工具也提供進階功能。



### 雷霆集線器



Interface 可透過 Umbrel App Store 安裝的現代網路型 Lightning 節點管理系統。



**特性：**




- 通道的即時可視化（容量、餘量）
- 整合式再平衡工具
- 支援多路徑計費 (MPP)
- QR 代碼生成 LNURL
- 交易管理 On-Chain



ThunderHub 是監控作用中的路由節點和執行簡單再平衡的理想選擇。



### Ride The Lightning (RTL)



Interface 網頁相容於數種 Lightning 實作 (LND、Core Lightning、Eclair)。



**重點：**




- 多節點管理
- 情境相關儀表板
- 支援潛艇交換 (Lightning Loop)
- 雙重認證
- 匯出/匯入通道備份



RTL 是一把完整的 「瑞士軍刀」，可以用更專業的方式管理 Lightning 節點。



### 其他有用的工具





- Lightning Shell** ：透過瀏覽器使用命令列 (lncli)
- BTC RPC Explorer & Mempool** ：監控 Blockchain
- LNmetrics & Torq**：路由效能分析
- Amboss 與 1ML**：節點的「社交」管理（別名、聯絡人、網路分析）



這些工具只需透過 Umbrel App Store 按幾下即可安裝，不需要任何複雜的設定。



**其他工具資源：**




- [ThunderHub.io - 功能](https://thunderhub.io) - ThunderHub 功能概述
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - RTL 文件
- [David Kaspar - 透過 ThunderHub 進行再平衡](https://blog.davidkaspar.com) - 再平衡實用指南
- [Guide "Managing Lightning Nodes"](https://github.com/openoms/lightning-node-management) - 電源使用者的進階文件



## 總結



在 Umbrel 上運行自己的 LND 節點是邁向金融主權的重要一步。雖然它需要比保管解決方案更多的技術參與，但在控制、保密和積極參與 Lightning Network 方面的好處是相當可觀的。



按照本指南，您現在應該可以安裝 LND、開啟頻道、管理您的流動資金以及遠端存取您的節點。隨著您對生態系統的熟悉，您可以隨意逐步探索進階功能和其他工具。



請記住，您的資金安全取決於您的保障措施和做法。在投入大筆資金之前，請花時間瞭解各個方面。
