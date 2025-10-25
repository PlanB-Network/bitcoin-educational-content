---
name: Umbrel
description: 發現並安裝 Umbrel - 您的 Bitcoin 節點和主伺服器
---

![cover](assets/cover.webp)



## 簡介



### 什麼是 Bitcoin 節點？



Bitcoin 節點是透過執行 Bitcoin 核心軟體或替代用戶端而參與 Bitcoin 網路的電腦。它的作用對於網路的運作和安全性至關重要：





- Blockchain 儲存：維護完整、最新的 Blockchain Bitcoin 副本
- 交易驗證：根據協定規則驗證每筆交易和區塊
- 資訊傳播：與其他節點分享新的交易和區塊
- 建立共識：有助於網路規則的應用



運行您自己的 Bitcoin 節點是邁向金融主權的重要一步，可提供多項關鍵優勢：





- **保密性**：分享您的交易，不會向第三方透露您的資訊
- 抵抗審查：沒有人可以阻止您使用 Bitcoin
- 獨立驗證：無需信任其他人的節點來驗證您的交易
- 建立共識：協助應用 Bitcoin 網路規則
- 網路支援：成為網路分配與分散的積極參與者



### Umbrel：運行 Bitcoin 節點的簡單解決方案



Umbrel 是一套開放原始碼作業系統，可簡化 Bitcoin 節點的安裝與管理。它也能將您的電腦轉換成個人專屬的家庭伺服器，讓您輕鬆架設.NET伺服器：





- 完整的 Bitcoin 節點
- Bitcoin 基本應用 (Electrs, Mempool.space)
- 其他個人服務 (雲端儲存、串流、VPN 等)



Umbrel 以其優雅且直覺的 Interface 使用者 Interface，讓所有人都能使用自助式託管服務，同時保留對您資料的完全控制。



## Umbrel 安裝選項



Umbrel 提供兩種使用其解決方案的主要方式：交鑰匙選項 (Umbrel Home) 和免費開放原始碼版本 (UmbrelOS)。



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home：交鑰匙解決方案



Umbrel Home 是預先設定的家庭伺服器，專為最佳體驗而設計。這個多合一硬體解決方案包括



**硬體功能**




- 針對自託管最佳化的高效能處理器
- 預先安裝高速 SSD 儲存裝置
- 安靜的冷卻系統
- 精巧、優雅的設計
- 整合式 USB 與乙太網路埠



**獨家優惠**




- 隨插即用安裝：插上電源即可使用
- 專人協助的優質支援
- 保證自動更新
- 整合式移轉精靈
- 完整硬體保固
- 全面支援所有功能



**價格**：399 歐元（價格可能因季節而異）



### UmbrelOS: 開放原始碼版本



UmbrelOS 是 Umbrel 作業系統的免費開放原始碼版本。這個靈活的解決方案可讓您使用自己的硬體，同時受惠於 Umbrel 的基本功能。



**福利**




- 完全免費
- 開放、可驗證的原始碼
- 選擇的自由
- 進階客製化選項



**支援的平台**




- Raspberry Pi 5：受歡迎且經濟實惠的解決方案
- X86 系統：適用於標準 PC 或伺服器
- 虛擬機器：用於測試或在現有基礎架構上使用



**限制條件**




- 僅提供社區支援
- 部分進階功能保留給 Umbrel Home
- 更具技術性的初始配置
- 效能取決於所選擇的硬體



此版本非常適合 .NET 使用：




- 技術使用者
- 已經擁有相容設備的人
- 想要學習和實驗的人
- 希望對專案有所貢獻的開發人員



官方安裝連結 ：




- [在 Raspberry Pi 5 上安裝](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [在 x86 系統上安裝 (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [虛擬機器安裝](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



在本教程中，我們將專注於在 Raspberry Pi 5 上安裝 UmbrelOS，但其他平台的基本原則仍然類似。



## 在 Raspberry Pi 5 上安裝 Umbrel OS



### 所需元件



安裝時，您需要 ：





- Raspberry Pi 5 (4 GB 或 8 GB RAM)
- 正式的 Raspberry Pi 電源 Supply（對穩定性至關重要）
- MicroSD 卡（至少 32 GB）
- microSD 讀卡機
- 用於資料儲存的外接式 SSD
- 乙太網路線
- 連接 SSD 的 USB 傳輸線



### 安裝步驟



**下載 UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- 請造訪 [官方網站](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- 下載最新版本的 UmbrelOS for Raspberry Pi 5



**Balena Etcher** 安裝



![Téléchargement Balena Etcher](assets/fr/02.webp)




- 下載並安裝 [Balena Etcher](https://www.balena.io/etcher/) 到您的電腦上



**準備 microSD** 卡



![Insertion carte microSD](assets/fr/03.webp)




- 將 microSD 卡插入電腦的讀卡機



** 影像閃爍**



![Flashage UmbrelOS](assets/fr/04.webp)




- 啟動 Balena Etcher
- 選擇下載的 UmbrelOS 映像檔
- 選擇您的 microSD 卡為目的地
- 按一下「Flash!」，等待程序完成
- 安全地彈出記憶卡



**microSD 卡安裝**



![Installation microSD](assets/fr/05.webp)




- 將 microSD 卡插入您的 Raspberry Pi 5



**週邊連接**



![Connexion périphériques](assets/fr/06.webp)




- 將外接式固態硬碟連接至可用的 USB 連接埠
- 連接 Pi 和路由器之間的乙太網路線



**開啟電源**



![Démarrage du Pi](assets/fr/07.webp)




- 連接 Raspberry Pi 官方電源 Supply
- 等待幾分鐘讓系統啟動



**First access**



![Accès interface web](assets/fr/08.webp)




- 在連線至相同網路的裝置上，開啟瀏覽器
- 進入 Umbrel 的 Interface 網站：`http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



如果 `umbrel.local` 無法運作，您需要在區域網路中找到 Raspberry Pi 的 IP Address。您可以 ：




- 請參閱路由器的 Interface
- 使用 nmap 等網路掃描器
- 在電腦的終端機使用 `arp -a` 指令



## 踏上 Umbrel 的第一步



一旦您的 Umbrel 已啟動，並可透過瀏覽器存取，請依照下列步驟開始使用：



### 初始設定



**Create your account**



![Création compte](assets/fr/10.webp)




- 選擇使用者名稱
- 設定安全密碼
- 您需要這些憑證才能存取您的 Umbrel



**帳戶確認**



![Confirmation compte](assets/fr/11.webp)




- 按一下「下一步」以存取您的儀表板



**發現 Interface**



![Interface Umbrel](assets/fr/12.webp)




- 存取 Umbrel App Store
- 探索眾多可用的應用程式
- 讓我們先安裝 Bitcoin 的基本應用程式



### 安裝 Bitcoin 應用程式



**Bitcoin 節點**



![Bitcoin Node](assets/fr/13.webp)




- 安裝的第一個應用程式
- 下載並檢查整個 Blockchain Bitcoin



**選舉人**



![Installation Electrs](assets/fr/14.webp)




- 連接 Bitcoin 電子錢包的 Electrum 伺服器
- 與您的 Bitcoin 節點同步



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Blockchain 的 Interface 顯示器
- 即時追蹤交易和區塊



## 使用 Mempool.space 追蹤交易



Mempool.space 是一個開放原始碼的 Blockchain 探索器，提供 Bitcoin 網路的即時視覺化。它可讓您追蹤交易，並瞭解交易如何在網路上傳播。



### 瞭解 Mempool 和確認



Mempool」（記憶體池）就像一個虛擬的等候室，所有未經確認的 Bitcoin 交易在納入區塊之前，都會先存放在這裡。以下是交易的處理過程：



1. **廣播**：當您傳送交易時，會先在 Bitcoin 網路上廣播


2. **Waiting in Mempool**：等待 Miner 根據成本選取


3. **第一次確認**：未成年人將其包含在區塊中 (第一次確認)


4. **附加確認**：在包含您交易的區塊之後開採的每個新區塊都會增加一個確認



建議的確認次數取決於 ：




- 對於小額：1-2 次確認即可
- 對於大筆款項：一般認為 6 次確認非常安全



### 從 Mempool.space 探索 Interface



1. **首頁**可讓您概覽 Bitcoin 網路：




   - 最近開採的區塊
   - 不同優先順序的成本預算
   - Mempool 的現況



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **搜尋交易**：若要追蹤特定交易，請將其識別碼 (txid) 貼入頁面頂端的搜尋列。



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### 分析交易詳細資料



一旦找到您的交易，Mempool.space 會為您提供完整的分析：



1. **Essential information** ：




   - 狀態（確認與否）
   - 已付費用 (單位：Sats/vB)
   - 預計確認時間



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **交易結構** ：




   - 輸入和輸出的視覺表示
   - 涉及地址的詳細清單
   - 轉讓金額



3. ** 技術資料** ：




   - 交易重量
   - 虛擬尺寸
   - 使用的格式和版本
   - 其他特定元資料



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### 在 Umbrel 上使用 Mempool.space 的優勢



1. **保密性**：您的請求會經過您自己的節點


2. **獨立**：無需依賴第三方服務


3. **Reliability**：即使在公共瀏覽器當機時也能存取資料



使用此應用程式，您可以有效監控您的交易，瞭解費用如何影響確認速度，並進一步瞭解 Bitcoin 網路的運作方式。



## 將 Wallet Bitcoin 連接到您的節點



### 電子組態



**本地連接**



![Connexion locale](assets/fr/18.webp)




- 用於您的區域網路
- 設定更快速簡便



**透過 Tor 進行遠端連線**



![Connexion Tor](assets/fr/19.webp)




- 要從任何地方存取您的節點
- 更安全、更隱私



### 與 Sparrow Wallet 連線



**存取參數**



![Paramètres Sparrow](assets/fr/20.webp)




- 開放式麻雀 Wallet
- 移至偏好設定 > 伺服器
- 按一下「修改現有連線」。



**連線類型的選擇**



Sparrow 提供三種連接模式：



**公共伺服器**




- 連線至公共伺服器 (例如 blockstream.info、Mempool.space)
- 簡單但隱私性較低



***Bitcoin Core***




- 直接連線至 Bitcoin 節點
- 私人但速度較慢



***私人電子琴***




- 連接至您的 Electrs 伺服器
- 結合保密性與效能



**選民**配置



使用我們之前看到的 Electrs 應用程式中顯示的資訊選擇您的連線類型：



在這兩種情況下，請不要勾選「使用 SSL」和「使用代理」選項。



**本地連接**


主機：umbrel.local


連接埠號：50001



**遠端連線 (Tor)**


主機 : [your-Address-onion]


連接埠號：50001



如果您要在本機網路之外存取您的節點，Tor 連線是必要的。



![Configuration connexion](assets/fr/21.webp)


如需 Sparrow Wallet 軟體的詳細資訊，我們有完整的教學：


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## 總結



您的 Umbrel 現在可以使用了。您可積極參與 Bitcoin 網路，同時保留對資料的完全控制。歡迎探索 Umbrel App Store 中的許多其他應用程式，以擴充您的家庭伺服器功能。



## 有用資源



### 官方文件




- [Umbrel官方網站](https://umbrel.com)
- [Umbrel 文件](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)



### Bitcoin 應用程式




- [Bitcoin Core](https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sparrow Wallet](https://sparrowwallet.com)



### 社區




- [論壇雨傘](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter Umbrel](https://twitter.com/umbrel)