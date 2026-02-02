---
name: BitBanana
description: Lightning 節點的行動管理員
---

![cover](assets/cover.webp)



在本教程中，您將學習如何在 Android 上安裝和配置 BitBanana，從您的智能手機控制您的 Lightning 節點。我們將介紹如何將應用程式連接至您現有的基礎設施（Umbrel、RaspiBlitz、myNode 或任何 LND/Core Lightning 節點）、進行 Lightning 付款、遠端管理您的渠道、查看您的路由收入以及備份您的配置。您也將學習到保護您節點存取的最佳安全實務，以及它與 Zeus（一個受歡迎的替代方案）的比較。



## 介紹 BitBanana



BitBanana 是一個開放原始碼的 Android 行動應用程式，可將您的智慧型手機變成一個完整的儀表板，遠端控制您的 Lightning 節點。與在手機上嵌入本地節點的 Lightning 電子錢包不同，BitBanana 採用 100% 遠端控制理念：應用程式不持有任何 satoshi，僅與您現有的基礎設施連接。



該應用程式由 Michael Wünsch 在 MIT 授權下開發，保證完全透明，不收集個人資料，並可驗證可重複的建置。BitBanana 透過標準 URI (「lndconnect://」與「clngrpc://」) 原生支援 LND 與 Core Lightning，大幅簡化初始設定。此應用程式也可辨識 LndHub 和 Nostr Wallet Connect，供沒有個人節點的使用者使用，不過這些模式是以保管方式運作，功能有限。



該介面可讓您完全存取節點的所有關鍵功能：傳送和接收付款 (BOLT11、Lightning Address、LNURL、BOLT12、Keysend)、Lightning 通道管理 (開啟、關閉、費用調整、重新平衡)、進階硬幣控制以及瞭望塔管理。BitBanana 還實現了多個強大的安全層：生物識別鎖定、隱藏模式、緊急 PIN 和原生 Tor 支援以匿名連接。



## 支援的平台與安裝



### 安裝



BitBanana 僅適用於 Android 8.0 或更高版本。該應用程式不存在於 iOS 上，也沒有計劃推出任何版本。這個限制可以從專案的歷史中得到解釋：BitBanana 是 Zap Android 的直接繼承者，最初由 Michael Wünsch 開發，後來他決定以自己的品牌繼續工作。Zap 是一個獨立的應用程式家族 (Zap Android、Zap iOS、Zap Desktop)，由不同的貢獻者以獨立的程式碼基礎開發。BitBanana 目前只追求 Android 分支。



此外，iOS 生態系統對非監護 Lightning 應用程式造成重大的法規與技術限制。2023 年，Apple 以「違反授權」為由拒絕了 Zeus 的更新；2024 年，Phoenix Wallet 面對 Lightning 服務供應商的監管不確定性，離開了美國 App Store。這些障礙解釋了為什麼許多 Lightning 開發人員偏好 Android，因為 Android 為非監護應用程式提供了更開放的政策。



Android 有三種安裝方法：Google Play 商店 (5000+ 安裝、自動更新)、F-Droid (可重複建立、原始碼驗證) 或從 GitHub 手動下載 APK。



![BitBanana](assets/fr/01.webp)



bitbanana.app 官方網站（左）標榜「100% 自行監控，零資料收集」。中央畫面顯示三種下載選項：F-Droid（推薦）、Google Play 和 APK。右邊的畫面顯示付款提醒的通知權限。



應用程式要求的權限：網路 (節點連線)、相機 (QR 碼)、NFC (LNURL)、後台服務 (通知)、生物識別 (安全性) 和 WireGuard VPN。無追蹤器、零資料收集。啟用密碼或生物識別鎖定，確保存取安全。



## 初始設定



### 連接至 LND 節點



要將 BitBanana 連接到您的 LND 節點 (Umbrel、RaspiBlitz、myNode)，請取得包含位址、TLS 憑證和驗證 macaroon 的 `lndconnect` URI 或 QR 代碼。



在本教程中，我們透過 umbrel 使用 LND 節點。如需詳細資訊，請參閱我們的專用教學 ：



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



在 Lightning Node 應用程式上，存取右上方的功能表並選擇「Connect wallet」。



![BitBanana](assets/fr/04.webp)



選擇 **gRPC (Tor)** 以透過 Tor 連線 (建議使用)。QR 代碼和詳細資訊 (Host .onion, Port 10009, Macaroon) 將會顯示。



![BitBanana](assets/fr/02.webp)



在 BitBanana 中，按「CONNECT NODE」，掃描 QR 碼或貼上 URI。授權攝影機存取，然後在確認之前檢查顯示的 .onion 位址。



**Core Lightning** 連線



如果您使用 Core Lightning (CLN) 而不是 LND，流程仍然相同，URI `clngrpc://` 包含相互 TLS 證書。Core Lightning 本機支援 BOLT12 (offers)，可實現 LND 上無法實現的可重複使用的發票和週期性付款。



**無個人節點的連線 (LNbits/hosted)**



如果您沒有 Lightning 節點，BitBanana 可以透過 LndHub（BlueWallet 和 LNbits 使用的通訊協定）或 Nostr Wallet Connect (NWC) 連接到託管服務。請注意：這些模式以託管模式運作 (服務託管您的資金)，功能有限。您將無法管理通道或配置路由費，只能發送和接收 Lightning 付款。



如需 LNbits 或 Nostr Wallet Connect 的詳細資訊，請參閱我們的各種教學：



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## 每日使用



### Interface 主



主螢幕會顯示您的 Lightning 結餘，左上方的功能表可讓您存取下列部分：頻道、路由、簽名/驗證、節點、聯絡人、設定、備份。時鐘圖標（右上角）會開啟交易歷史。底部的 「發送 」和 「接收 」按鈕可讓您發送和接收您的 Satoshis。



![BitBanana](assets/fr/05.webp)



### 閃電和 on-chain 付款



![BitBanana](assets/fr/10.webp)



**傳送付款：** 從主畫面按下「傳送」按鈕。付款畫面（左邊）可讓您將地址或付款資料貼入「Address 或付款資料」欄位，右上方有 QR 掃描器可用來掃描代碼。您也可以選擇儲存在「聯絡人」欄位中的聯絡人，以避免每次都要掃描。



BitBanana 可智能識別所有付款格式：經典的 Lightning 發票（以 `lnbc` 開頭的字符串）、Lightning Address（電子郵件格式，如 `utilisateur@domaine.com`）、用於動態支付的 LNURL-pay 代碼、用於提取資金的 LNURL-withdraw，甚至是直接向 Lightning 公鑰支付的 Keysend 付款，而無需事先開具發票。應用程式會在背景自動執行必要的 LNURL 解析。



發票載入後，BitBanana 會顯示完整的詳細資訊：確實金額、預計路由費、付款說明（如果收款人提供）和發票到期日。確認後，付款會經由您的 Lightning 通道傳送。然後，您可以在交易詳細資料中逐跳檢視路由以及實際支付的費用。



**接收付款：** 按「接收」按鈕。選擇器 (右邊畫面) 可讓您選擇 Lightning (透過您的管道立即付款) 或 On-Chain。對於 Lightning 收款，請輸入所需的金額（以 Satoshis 為單位）（或保留為 0，以建立無固定金額的發票供付款人完成），並加入可選的說明，以顯示在發票上。BitBanana 會立即產生附有 QR 碼的 Lightning 發票以供掃描。您也可以將發票複製成文字，並透過電子郵件傳送。一旦收到付款，推送通知會提醒您，交易會立即顯示在歷史記錄中，並包含所有詳細資訊。



### 通道和路由



![BitBanana](assets/fr/06.webp)



頻道」區段顯示您的傳送/接收能力，並列出具有獨特頭像的頻道。每個通道都會顯示其本地和遠端餘額之間的流動資金分配。輕觸通道可查看全部詳細資訊和操作（關閉、變更路由費）。右上方的三個圓點提供「重新平衡」選項，以重新平衡您的通道流動性。+" 按鈕可開啟一個新通道。



路由部分（中央螢幕）顯示按時段（1D、1W、1M、3M、6M、1Y）的轉寄收入，並提供詳細的轉寄歷史，以優化您的策略。



Sign/Verify (右邊畫面) 可讓您以加密方式簽署/驗證訊息，以證明節點控制權。



### 多節點與參數



![BitBanana](assets/fr/07.webp)



**Manage Nodes**：列出您的節點，按鈕可手動新增、掃瞄 QR 或在節點間切換。特別的是，您可以設定不同類型的連線到相同的節點：LAN、VPN 或 Tor。



**Manage Contacts**：儲存您的 Lightning 聯絡人，以便快速付款。



**設定**：自訂貨幣、語言、頭像。安全與隱私部分：應用程式鎖 (PIN/生物辨識)、隱藏餘額 (隱身模式)、Tor (IP 匿名化)。設定價格傳遞器、區塊探索器、自訂費用估算器。



## 優點與限制



**重點：**




- 完全移動性：從任何地方控制您的 Lightning 節點
- 完整功能：付款 (LNURL、Lightning Address、BOLT 12)、通道管理、硬幣控制、瞭望塔、多節點
- 安全性：PIN 碼/生物辨識、隱藏模式、緊急 PIN 碼、原生 Tor、螢幕截圖封鎖
- 免費、開放原始碼 (MIT)、零佣金、零資料收集



**限制：**




- 需要使用中的 Lightning 節點 (或托管模式中的 LNbits)
- 未規劃 iOS 版本
- 確保手機訪問的安全性至關重要 (macaroon admin = 節點的完整訪問權限)



## 最佳實踐



**安全：**




- 啟動 PIN 碼/生物識別鎖定 (防止未經授權存取節點)
- 設定緊急 PIN 碼 (在受到威脅時刪除敏感資料)
- 絕不分享您的登入 URI 或 macaroon
- 惡劣環境中的隱形模式



**登入：**




- VPN 網狀 (Tailscale、ZeroTier)：速度與安全性的最佳折衷方案
- Tor: 最大保密性，較高延遲
- Clearnet：除非必要，否則避免使用 (IP 暴露、開放埠)



### 備份與還原



最後，還有「備份」功能表，可讓您儲存組態，以便進行電話遷移或重新安裝。



![BitBanana](assets/fr/08.webp)



**重要事項：** 備份不包含 seed 或通道備份 (需在節點上完成)。它包含：節點組態 (位址、憑證、巨集)、標籤、連絡人、參數。Restore 按鈕可讓您匯入現有的備份。儲存前需要確認。



![BitBanana](assets/fr/09.webp)



輸入加密密碼 (右邊畫面)。系統開啟檔案選擇器 (左邊畫面) 以儲存 `BitBananaBackup_2025-XX-XX.dat`。確認「已建立備份」。



**安全性：** 加密儲存備份 (個人雲端、USB、NAS)。切勿共用檔案或密碼。定期測試還原。備份會復原連線，而非資金。



## BitBanana vs Zeus：有何差異？



如果您正在探索管理 Lightning 節點的移動應用程式，您很可能會遇到 Zeus，它是 BitBanana 的熱門替代品。與 BitBanana 不同的是，BitBanana 只專注於遠端控制現有節點，而 Zeus 則採用了更全面的方法，提供兩種操作模式：直接嵌入應用程式的 Lightning 節點（整合 LND 的嵌入式模式）和遠端連接到外部節點，就像 BitBanana 一樣。



這種雙重功能使 Zeus 對希望在沒有任何基礎設施的情況下嘗試使用 Lightning 的初學者特別具有吸引力。嵌入式模式可立即啟動完整的移動節點，而高級用戶可在配置好個人節點後切換到遠端連接。Zeus 也支援 LND 和 Core Lightning 進行遠端連線，例如 BitBanana。



Zeus 的另一大優勢是其跨平台可用性（iOS 和 Android），而 BitBanana 仍然僅基於 Android。Zeus 也結合了 Olympus LSP 基礎架構，方便透過即時管道接收 Lightning 付款、商戶銷售點系統，以及管理流動資金的整合交換功能。



然而，BitBanana 保留了其特有的優勢：更簡單、更流暢的介面、因專注於遠端控制而獲得更好的使用者體驗 (UX)，以及具有上下文解釋的教育方式。Zeus 提供更多功能，但代價是更複雜的介面。此應用程式仍特別適合希望遠距離控制節點的使用者，且不具備監管功能。



若要瞭解關於 Zeus 的更多資訊，請參閱下列教學：



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## 總結



BitBanana 可將您的 Android 智慧型手機變成完整的 Lightning 面板，為節點經營者提供前所未有的行動力。該應用程式涵蓋所有功能：支付（所有格式）、通道管理、硬幣控制、瞭望塔、多節點，並具有增強的安全性（PIN/生物統計、Tor、緊急 PIN）。



BitBanana 完全擁有主權，不會收集任何資料，也不會損害您資金的機密性或控制權。開放原始碼 (MIT) 保證透明度。



## 資源



### 官方文件




- [BitBanana 網站](https://bitbanana.app)
- [完整文件](https://docs.bitbanana.app)
- [GitHub 原始碼](https://github.com/michaelWuensch/BitBanana)



### 安裝




- [Google Play 商店](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)