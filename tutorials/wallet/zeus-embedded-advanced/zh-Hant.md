---
name: Zeus Embedded - 進階
description: 多節點自我監護 Wallet
---

![Zeus](assets/cover.webp)


## ZEUS Wallet 簡介


ZEUS 是行動版 Bitcoin Wallet 和節點管理應用程式，具備 Bitcoin Lightning Wallet 的完整功能，讓 Bitcoin 支付變得簡單，讓使用者完全掌控財務，並讓更進階的使用者從掌上管理他們的 Lightning 節點。


### ZEUS 適合哪些人使用？

目前 ZEUS 適用於運行 [Lightning Network Daemon (LND)](https://lightning.engineering/) 或 [Core Lightning (CLN)](https://blockstream.com/lightning/) 家庭/企業節點的使用者，並透過 Zeus 遠端管理這些節點。


使用 [BTCPay](https://btcpayserver.org/) 或 [LNBits](https://lnbits.com/) 或 [Alby](https://getalby.com/) (或任何其他 LNDhub 帳戶) 的商家也可以從 ZEUS 連接、使用和管理他們的節點/帳戶。


[從 v0.8 版開始](https://blog.zeusln.com/zeus-v0-8-0-open-beta/)，ZEUS 將開始迎合一般使用者的需求，讓他們只需要簡單的方式，就能透過行動裝置進行快速、便宜的 Bitcoin 付款，ZEUS 內建一個 [內建行動 Lightning 節點](https://docs.zeusln.app/category/embedded-node)，並整合了 [Lightning Service Provider (LSP)](https://docs.zeusln.app/lsp/intro)。


### 重要的 Zeus 資源：


- Zeus 官方網頁 - [https://zeusln.app/](https://zeusln.app/)
- Zeus 文件 - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Zeus Github 儲存庫](https://github.com/ZeusLN/zeus)
- [Zeus Telegram 支援小組](https://t.me/ZeusLN)
- [Zeus on NOSTR](https://iris.to/zeus@zeusln.app)
- [宙斯網誌公告](https://blog.zeusln.com)


### 宙斯特徵

#### 一般功能：


- 自我監護，僅 Bitcoin 和 Lightning Wallet
- 無處理費、無 KYC
- 完全開放原始碼 (APGLv3)
- 支援多個節點/帳號 (您可以管理自己的家庭節點、執行內嵌的 LND 節點、連結到多個 LNDhub 帳號)
- 易於使用的活動選單
- PIN 或 passphrase 加密、隱私模式 - 隱藏您的敏感資料
- 聯絡簿、多主題、多語言


#### 技術特性


- 透過 Tor 連線
- 完全支援 LNURL (付款、提款、授權、頻道)、傳送至 Lightning 位址
- 詳細的照明通道管理、MPP/AMP 支援、Keysend、路由費管理
- Replace-by-fee (RBF)和子女為父母付費 (CPFP) 支援
- NFC 付款和請求、簽署和驗證訊息
- 支援 SegWit 和 Taproot
- 簡單的 Taproot 通道
- 自我監護的閃電地址 (@zeuspay.com)
- 使用 Square 的銷售點 (即將開放 PoS)


### 指南和視訊教學

為了能夠使用 Zeus 並管理 Lightning 渠道、流動性、費用等，最好先閱讀一些關於 Lightning Network 的重要指南。


#### 指南：


- [LND - Lightning Network Daemon 文件](https://docs.lightning.engineering/)
- [CLN - Core Lightning Documentation](https://lightning.readthedocs.io/index.html)
- [Beginners Lightning Guide](https://bitcoiner.guide/lightning/) - by Bitcoin Q&A
- [Lightning 節點管理](https://www.lightningnode.info/) - by openoms
- [Lightning Network與機場的類比](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Managing Lightning Node Liquidity](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Lightning 節點維護](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### BTC Sessions 的視訊教學


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## 如何在行動裝置上開始使用 Zeus LN 嵌入式節點的簡易指南


![Image](assets/en/01.webp)


我將這份指南獻給所有想要在行動裝置上使用自保管節點 Wallet 開始新主權旅程的 Lightning Network (LN) 新使用者。


讓我們考慮一下，您已經通過了所有那些大量的託管 LN 錢包，但您還沒有準備好開始運行 PUBLIC 路由 LN 節點，您只是想以更自我託管的方式在 LN 上堆疊更多的 Sats，並在 LN 上進行定期支付。


Zeus來了，從[在他們的部落格發佈的v0.8.0版本](https://blog.zeusln.com/new-release-zeus-v0-8-0/)開始，現在提供一個嵌入式的LND節點到應用程式中。在此之前，Zeus 是一個遠端節點管理應用程式 + LNDhub 帳戶。但現在......節點就在手機裡！


![Image](assets/en/02.webp)


### 快速回顧 Zeus Node 的主要功能：



- 私人 LND 節點** - 這表示此節點不會透過您的節點做公開路由他人付款。該節點和通道是不公開的（私有的，在公開的 LN 圖表上不可見）。接收和付款將透過您連接的 LSP 對等體進行。請注意：Zeus 嵌入式節點不會進行公開路由！
- 持久 LND 服務** - 使用者可以啟動此功能，讓 LND 服務如同任何一般 LN 節點一樣持續運作。應用程式不必開啟，持久性服務會保持所有通訊在線。
- Neutrino 區塊過濾器** - 區塊同步是使用[區塊過濾器和 Neutrino 協定](https://bitcoinops.org/en/topics/compact-block-filters/)來完成的（沒有給予有關我們用戶的 On-Chain 資金的資訊）。提醒：對於高延遲/慢速的網路連線，這種基於中微子的區塊同步有時候可能會失敗。嘗試切換到靠近 neutrino 的伺服器可以幫助恢復同步。如果沒有這個同步，您的 LND 節點就無法啟動！
- 簡單的 Taproot 頻道** - 當關閉這些頻道時，使用者會產生較少的費用，並獲得更多隱私，因為在檢查他們的 On-Chain 足跡時，他們看起來就像任何其他 Taproot 支出。
- 整合式 LSP** - Olympus 是 Zeus 新的 LSP 節點。使用者可以直接透過 LN 接收 Sats，無需事先設定 LN 頻道。只需建立一個 LN Invoice，並使用 Zeus 0-conf 通道服務從任何其他 LN Wallet 付款即可。在此閱讀更多關於 Zeus LSP 的資訊。LSP 還為我們的用戶提供了更多的隱私，為用戶提供了隱藏其節點公開密碼匙的包裹式發票。
- 連絡人簿** - 您可以手動儲存連絡人或從 NOSTR 匯入，方便傳送款項到您固定的目的地。
- 完全支援 LNURL、LN Address 的傳送與接收** - 現在您可以透過 @zeuspay.com 設定自己的自保管 LN Address。提醒：您也可以在可以使用 LN 認證登入的網站使用 Zeus 進行 LN-auth。是非常方便的。
- 銷售點** - 現在商家用戶可以設置自己的產品項目，並直接從 Zeus 銷售，集成 PoS。目前包含基本需求，但未來將包含擴充功能。
- LND 日誌** - 使用者可以即時讀取 LND 服務日誌，並使用這些日誌來除錯可能發生的問題 (主要是連線不良的問題)
- 自動備份** - LN 節點頻道會自動備份到 Olympus 伺服器上。此自動備份與您的 Wallet seed 節點一起加密（沒有 seed 則完全無用）。使用者也可以手動匯出 SCB（靜態頻道備份），以進行災難復原。


### 如何上線 Zeus LN 節點 (LND 嵌入式)


在本指南中，我只會談到內嵌的 LND 節點，而不會談到使用這個偉大的應用程式的其他方式（遠端節點管理和 LNDhub 帳戶）。關於其他類型的連線，請參考 [Zeus Docs page](https://docs.zeusln.app/category/getting-started)，那裡有很好的說明，不需要寫專門的指南。


#### 步驟 1 - 初始設定


由於 Zeus 是完整的 LND 節點，我會有一些初步的建議：



- 請勿使用舊裝置，以免影響此功能強大的應用程式的使用。尤其是在同步期間，該應用程式可能會大量使用 CPU 和 RAM。如果缺乏這些資源，甚至可能無法使用 Zeus 應用程式。
- 至少使用 Android 11 作為行動作業系統，並盡可能更新。對於 iOS 也是一樣，請嘗試使用更高版本的作業系統。
- 您至少需要 1GB 磁碟空間來儲存資料。隨著時間的推移可能會增加，但有一個功能可以將資料庫壓縮到 MB 級。
- 沒有必要使用 Zeus 與 Tor 或 Orbot 服務。請不要把事情搞得太複雜。在這種情況下，Tor 不會為您提供更多的隱私，而只會使初始同步的情況變得更糟。此外，請小心使用 VPN，並檢查連線至 Neutrino 伺服器的延遲時間。請記住，Neutrino 封鎖過濾器不會洩露或追蹤您的裝置身份，只是提供封鎖服務。LN 的流量也是透過私密通道的 LSP 來傳輸，因此洩漏的資訊非常少，所以沒必要擔心隱私問題。
- 請耐心等待初始同步，可能需要幾分鐘。盡量使用延遲性良好的寬頻網路連線。如果您運行您自己的 Bitcoin 節點，[您可以啟動 neutrino 服務](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) 並將您的 Zeus 連接到您自己的節點，甚至使用內部 LAN，這樣您將擁有最高的速度。


一旦您設定連線類型為「內嵌節點」，應用程式就會開始同步一段時間。耐心等待完成該部分，然後進入主「設定」頁面。


![Image](assets/en/03.webp)


簡單來說，在您開始使用 Zeus 之前，讓我們深入瞭解每個設定部分，並瞭解一些主要功能：


**a - 設定**


此部分包含整個應用程式的一般設定


**1 - 閃電服務供應商 (LSP)**


這裡介紹兩種 LSP 服務：



- _Just in time channels_ - 當您沒有開啟任何頻道或沒有可用的入站流動資金時，如果啟用此服務，它會為您即時開啟一個頻道。如果您不想開啟更多此類通道，則可以禁用此選項。
- _Request channels in advance_ - 您可以在應用程式中直接向奧林帕斯 LSP 購買入站頻道，有多種選項和金額（入站和出站）。


LSP 透過開放支付管道至使用者的節點，協助使用者與 Lightning Network 連結。[Read more about LSP here](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992).ZEUS 整合了一個新的 LSP，稱為 [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581)，所有使用新內嵌節點的使用者都可以使用。


在本節中，預設為 Olympus LSP (https://0conf.lnolymp.us)，但不久之後您也可以設定其他支援此通訊協定的 0conf LSP。


_請記住：_

當您使用包裝好的LN發票與Olympus LSP開通一個通道時，您還可以獲得10萬的入站流動資金！如果您需要直接收到更多的 Sats，這是一個非常好的選擇。

例如：您存入 400k Sats 來開啟 LSP 通道，則 LSP 會朝您的 Zeus 節點開啟容量為 500k Sats 的通道，並將您存入的 400k Sats 推向您這邊。

_「入站流動性」 = 在您的通道中提供更多「空間」來接收。


在未來，我們希望可以有許多其他的 LSP 可以整合到 Zeus 中，並且可以交替使用每個 LSP。新的 LSP 將採用開放式標準來提供這些 0conf 通道，這只是時間問題。


如果您不想「隨時」開啟新頻道，可以停用此選項。


在同一部分中，當 LSP 開啟通往您 Zeus 節點的通道時，您也可以選擇「請求簡單 Taproot 通道」。這些簡易 Taproot 頻道提供更好的 On-Chain 隱私和更低的頻道關閉費用。您不想使用它們的原因只有兩個：



- 它們是新產品，使用它們時 LND 可能仍有 bug。
- 您的交易對手不支援它們。目前，即使是 LND 節點也必須明確選擇加入。


**2 - 付款設定**


此功能可讓您設定自己偏好的付款費用，透過 LN 或 onchain 付款。也提供增加或減少發票逾時的選項。


如果某些 LN 付款失敗，您可以增加費用以尋找更好的路徑。此外，如果您正在進行 onchain tx，您可以設定特定的費用，這樣您的 tx 就不會長時間停留在 Mempool，以防費用過高。


**3 - 發票設定**


本節提供 generate 發票的一些選項：



- 設定要在 Invoice 和 generate 中顯示的標準備忘錄
- 到期時間（以秒為單位），如果您希望 Invoice 在特定時間（更長或更短）內付款
- 包含路由提示 - 提供尋找非公開或私人通道的資訊。這可將付款路由至網路中不公開顯示的節點。路由提示提供收款人私有節點與公開節點之間的部分路由。這個路由提示會包含在接收者所產生的 Invoice 中，並提供給付款者。我建議預設為啟用，否則傳入的付款可能會失敗 (找不到路由)。
- AMP Invoice - Atomic Multi-path Payments 是由 LND 實現的一種新型 Lightning 付款方式，它允許使用 [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) 在沒有特定 Invoice 的情況下接收 Sats。實際上是一種靜態付款代碼。[Read more here](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- 顯示自訂預覽欄位 - 只有在非常特殊的情況下，當您真的想要在預覽中使用自訂欄位時，才使用此選項。[Read more here](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


本節的另一個選項是如何設定您要使用的 onchain Address 類型：SegWit 嵌套、SegWit、Taproot。


![Image](assets/en/04.webp)


按一下上方的滾輪按鈕，就會出現一個彈出畫面，讓您選擇所需的 Address 類型。設定好之後，下次按下 onchain 的接收按鈕時，就會 generate 所選的 Address 類型。您可以隨時變更。


**4 - 頻道設定**


在本節中，您可以預先設定一些開啟頻道的功能，例如



- 確認次數
- 公告頻道 (預設為關閉)，表示將是未公告的頻道
- 簡單的 Taproot 通道
- 顯示頻道購買按鈕


**5 - 隱私權設定**


您可在此找到使用 Zeus 應用程式增加隱私的一些基本設定：



- Block explorer 開啟 tx 詳細資訊 (Mempool.space、blockstream.info 或自訂個人資訊)
- 讀取剪貼簿 - 開啟/關閉切換鍵，如果您想要 Zeus 讀取裝置的剪貼簿
- 潛伏者模式 - 開關切換，如果您想從 Zeus 應用程式中隱藏特定的敏感資訊。當您製作演示或截圖時，這是一個很好的選擇。
- Mempool 費用建議 - 如果要使用 [Mempool.space](https://Mempool.space/) 中的建議費用等級，請啟動此選項。


**6 - 安全**


此部分在開啟應用程式時只有兩個安全保護選項：設定密碼或 PIN。


一旦您設定了開啟應用程式的 PIN 碼，您也可以設定「脅迫 PIN 碼」。這個秘密的額外 PIN 碼只會在您受到威脅的情況下使用。如果您設定了這個 PIN 碼，設定將會全部刪除。所以您最好持續更新您的備份。自動備份預設為開啟，但您也可以在裝置外自行備份。


**7 - 貨幣**


啟用或停用在 Zeus 應用程式使用中顯示法定貨幣換算的選項。目前支援全球 30 多種法定貨幣。


**8 - 語言**


您可以在多種翻譯語言之間切換，並由 Zeus 社群的母語人士審核。


**9 - 顯示**


在本節中，您可以個人化您的 Zeus 顯示，選擇各種顏色主題、預設畫面 (鍵盤或平衡)、顯示您的節點別名、啟動大鍵盤按鈕、顯示更多小數位。


**10 - 銷售點**


這是一項特殊功能，用於啟用/禁用 Zeus 中的集成 PoS 系統。您可以運行獨立的 PoS 系統，也可以與 Square PoS 系統連接。目前支持 PoS 的基本功能，但足以作為一個良好的開始，並可以幫助那些小型商家（酒吧/餐廳、雜貨店）開始以原生的方式接受 BTC。


在此設定中，您可以找到各種選項來設定您的 PoS：



- 確認付款類型：僅 LN、0-conf、1-conf
- 啟用 / 停用操作 PoS 的員工的提示
- 顯示/隱藏鍵盤
- 適用於機票的稅率
- 建立產品和產品類別
- 所有銷售的簡單列表


以下是如何使用 Zeus PoS 的即時示範影片：


**B - 備份 Wallet**


ZEUS 中的嵌入式節點是基於 LND 並使用 [aezeed seed 格式](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md)。這與您在大多數 Bitcoin 錢包中看到的典型 [BIP39 格式](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) 不同，儘管看似相似。Aezeed 包含一些額外的資料，包括 Wallet 的出生日期，這將有助於在恢復過程中更有效地進行重新掃描。


aezeed 金鑰格式應與下列行動錢包相容：Blixt、BlueWallet 和 Breez。請注意，如果您有打開或等待關閉的通道，僅 seed 將不足以恢復您的所有餘額 ！


在 [Zeus Docs 頁面](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery) 瞭解更多關於備份和還原過程的資訊。


電源建議：當您儲存 seed 時，請同時儲存節點的 pubkey！有時候，將它與您的 seed 和 SCB（靜態頻道備份）放在手邊是很好的，以防您需要驗證恢復。


只有當您開啟 LN 通道時，才需要 SCB。如果您只有 onchain 資金，則不需要。


如果您發現經過一段長時間後仍未顯示舊的歷史 txs，請前往 Embedded node - Peers 並停用選項來使用選定的對等者清單 (預設為 btcd.lnolymp.us)。這將會觸發重新啟動，並連線到第一個可用的中微子節點，並有更好的時間回應。或者使用下面提到的其他知名中微子節點。


如果您想查看 LND 節點的更多復原選項，[請閱讀我之前的指南](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html)，您可以在其中找到如何將 Aezeed seed 匯入 Sparrow Wallet 的步驟或其他方法。


**C - 嵌入式節點**


在本節中，我們會找到一些管理整合節點的基本工具：



- _Disaster Recovery_ - LN 頻道的自動和手動備份。請在 Zeus Docs 頁面閱讀更多如何使用此功能。
- _Express Graph Sync_ - Zeus 應用程式會從專用伺服器下載 LN 八卦資料圖，以達到更快更好的同步，並提供最佳的付款路徑。您也可以選擇在啟動時清除先前的圖表資料。
- _Peers_ - 用來管理 neutrino 對等站和 0-conf 對等站。如果您在初始同步時遇到問題，頻道無法上線，那是因為您的裝置與設定的 neutrino 對等體有較高的延遲。請嘗試切換優先對等體清單，或新增您的特定對等體，因為您知道它有更好的同步延遲。知名的 neutrino 伺服器有



 - btcd1.lnolymp.us | btcd2.lnolymp.us - 適用於美國地區
 - sg.lnolymp.us - 適用於亞洲地區
 - btcd-Mainnet.lightning.computer - 適用於美國地區
 - uswest.blixtwallet.com (Seattle) - 適用於美國地區
 - europe.blixtwallet.com (德國) - 適用於歐盟地區
 - asia.blixtwallet.com - 適用於亞洲地區
 - node.eldamar.icu - 適用於美國地區
 - noad.sathoarder.com - 適用於美國地區
 - bb1.breez.technology | bb2.breez.technology - 適用於美國地區
 - neutrino.shock.network - 美國地區



- _LND logs_ - 非常有用的工具，用來除錯您的 LN 節點問題，並以更高的技術層級深入掌控發生了什麼事。
- _進階設定_ - 更多控制 LND 節點使用的工具：



 - _Pathfinding mode_ - bimodal 或 apriori，為您的 LN 付款尋找更好路線的方法，也可以重設先前的路線資訊。請閱讀這些非常好的路徑尋找指南：[尋路](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - 由 Docs Lightning Engineering 和 [LN 付款尋路](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - 由 Voltage 提供。
 - _Persistent LND_ - 如果您希望 LND 服務在後台持續執行，並讓您的節點全天候線上，請啟動此模式。如果您將 Zeus 當作小型商店的 PoS 使用，或是您透過 LN Address 接收到許多 LN 的提示，這會非常有用。
 - _Rescan wallet_ - 此選項會在重新啟動時啟動 Wallet 的所有 onchain txs 的完整掃描。只有在您的 Wallet 遺失某些 tx 的情況下才會啟動。重新掃描任務需要幾分鐘的時間，因此請耐心等待，並經常檢查日誌以瞭解進度的詳細資訊。
 - _Compact Database_ - 如果您的 Zeus 應用程式佔用了大量的裝置空間（請參閱裝置設定中的應用程式詳細資訊），此選項非常有用。如果您使用 Zeus 的活動量很大，我建議您多做此壓縮。一旦您發現 Zeus 應用程式有超過 1-1.5GB 的資料，請執行壓縮。它會重新啟動並需要一些時間，所以請耐心等待。
 - _Delete Neutrino files_ - 這個刪除中微子檔案的選項（需要重新啟動）會大量減少資料儲存的使用。減少資料使用量對電池使用量也有很大的影響，減少電池使用量，特別是當您在持久模式下使用 Zeus 時。


**D - 節點資訊**


在本節中，您將發現更多關於 Zeus 節點狀態的詳細資訊：



- 別名 - 短節點 ID
- 公開金鑰 (Public Key) - 您節點的完整公開金鑰，其他節點必須使用此金鑰才能找到通往您節點的路徑。請記住，這個公開金鑰在一般的 LN Explorer (Mempool、Amboss、1ML 等) 上是看不到的。這個公開金鑰只能透過您所連線的 LN 對等體和頻道取得。
- LN 實作版本
- Zeus 應用程式版本
- Synced to chain (已同步到鏈) 和 Synced to graph status (已同步到圖形狀態) - 非常重要，可顯示節點的正確狀態。如果這兩個狀態沒有顯示「true」，表示您的節點仍在同步或同步上有問題。因此建議查看您的 LND 記錄或再等一會兒。
- 區塊高度和 Hash - 顯示您的節點看到並同步的最後一次區塊和 Hash。


**E - 網路資訊**


本節顯示關於 Lightning Network 一般狀態的更多詳細資訊，這些資訊是從您的圖形同步資料中擷取：可用的公開頻道數、節點數、殭屍頻道數（離線或死亡）、圖形直徑、圖形的平均值和最大值。


此資訊資料可能有助於除錯或僅用於統計。


**F - Lightning Address**


在本節中，使用者可以設定自己的自我保管 LN Address @zeuspay.com。


ZEUS PAY 利用使用者產生的預設影像哈希值、HODL 發票以及 Zaplocker Nostr 驗證方案，讓可能無法全天候線上的使用者，也能收到支付給靜態閃電 Address 的款項。使用者只要在 24 小時內登入他們的 ZEUS 荷里活錢包，就可以領取付款，否則付款會退回給寄件人。


如果您啟動「持續模式」，您的 LN Address 的所有付款都會立即收到。


瞭解 [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) 付款如何運作，以及更多關於 [ZeusPay Fees here](https://docs.zeusln.app/lightning-Address/fees) 的資訊。


**G - Onchain 位址**


在這一節中，您可以參考您產生的上鏈地址，以獲得更好的硬幣控制。


**H - 聯絡人**


Zeus v 0.8.0 中引入了一個新的聯絡人簿，您可以用它快速地向您的朋友和家人發送款項，還可以從 Nostr 匯入您的聯絡人。


只需輸入您的 Nostr npub 或可讀取的 NIP-05 Address，ZEUS 即會查詢 Nostr 中的所有聯絡人。您可從此快速付款給聯絡人，或匯入全部或部分聯絡人至您的本機聯絡人簿。


以下是如何設定和使用 Zeus 聯絡人的簡短影片：


**I - 工具**


在這裡，我們有不同的子區塊，提供更多的工具：



- _Accounts_ - 在此您可以匯入外部帳戶/錢包、Cold 錢包、Hot 錢包，以控制或用作您的 Zeus 節點通道的外部資金來源。此功能仍在實驗階段。
- _Speed up transaction_ - 當您有一個卡住的 tx 進入 Mempool，並想要提高費用時，此功能會很有幫助。您需要提供 tx 詳細資料中的 tx 輸出，並選擇您想要使用的新費用。新費用必須高於之前的費用，並要求您的 onchain Wallet 有更多可用資金。


![Image](assets/en/05.webp)


您必須前往您的待處理 tx 並複製 txid 外點。然後來到這一部分並貼上它，然後選擇您要使用的新費用來提升它。此時會彈出一個新的畫面，其中有推薦的費用，或者您也可以設定一個自訂的費用。記住必須高於先前的費用。


最好在您的 Zeus onchain Wallet 中保留一個 UTXO 與最大 100k 的 Sats，以便在必要時使用它來提升費用。



- _Sign or verify_ - 使用此功能，您可以用 Wallet 金鑰簽署特定訊息。也可以用來驗證訊息，證明訊息來自特定的 Wallet 金鑰。
- _Currency converter_ - 一個簡單的工具，用來計算 BTC 和其他法定貨幣之間的匯率換算。


**J - 商品與支援**


您可在此找到更多關於 Zeus、線上商店、贊助商、社交媒體的資訊和連結。


**K - 求助**


在最後一節中，您可以找到 Zeus 文件頁面、Github 問題（如果您想直接向應用程式開發人員發佈錯誤或請求）、電子郵件支援的連結。



### 步驟 2 - 開始使用 zeus 節點



請記住，Zeus 主要用作 LN Wallet，用於通過 LN 進行簡單快速的支付。當然，它也包含一個 onchain Wallet，但那個應該只用於打開/關閉 LN 通道，而不是用於定期支付咖啡。


請閱讀我的其他指南，關於 [如何使用 Stash 的 3 個層級成為您自己的銀行](https://darth-coin.github.io/beginner/be-your-own-bank-en.html)。


此時使用者有兩種方式開始使用 Zeus：



- 直接透過 LN，使用來自 Olympus LSP 的 0-conf 通道
- 先在 onchain Wallet 存款，然後與您想要的對等人開啟一般的 LN 通道。


#### 方法 A - 使用 Olympus LSP


這是讓新的 LN 用戶加入 Zeus 的簡單直接的方法。它可以是一個完全沒有 Sats 的全新 Bitcoin 用戶，也可以是一個由朋友加入的新用戶，或者是一個剛開始第一次 LN 付款的新商家。


預設情況下，Zeus 會使用它自己的 LSP，即 Olympus。但稍後您也可以切換到其他支援此 0-conf 協定的 LSP 來開啟通道。


只需在您的 Zeus 上建立一個 Invoice（填入金額並點擊 「請求 」按鈕），您就可以直接收到這些 Sats。


您 generate 的 Invoice 將被 [包裹](https://docs.zeusln.app/lsp/wrapped-invoices)，如果您支付了服務相關的費用，您將會看到這些費用。此包裹的 Invoice 包含指向您的 Zeus 節點的路由提示，因此 LSP 可以找到您的新節點，並利用您存入的新資金開啟通道。


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


為了從 LSP 獲得一個 LN 頻道，其中包含您想要第一次收到的資金，這個 Invoice 必須從另一個 LN Wallet 支付，並等待片刻，直到 LSP 朝您的 Zeus 節點開啟頻道，扣除費用，然後將剩餘的付款金額推送到您這邊的頻道。


您只需用另一個閃電 Wallet 支付在 ZEUS 中為您生成的 Invoice，您的通道就會立即打開。[請參考 Zeus LSP 費用](https://docs.zeusln.app/lsp/fees)。


支付通道的另一個好處是零費用路由。這表示在路由付款時，透過 OLYMPUS by ZEUS 的第一跳不會產生路由費用。請注意，超出 OLYMPUS by ZEUS 的跳轉仍會向您收費。


頻道準備就緒後，按一下畫面下方顯示 Zeus 頻道的右側按鈕。


![Image](assets/en/08.webp)


您會看到這樣的頻道，顯示您一方的頻道平衡：


![Image](assets/en/09.webp)


您從這個渠道花費的越多，您擁有的流入流動資金就越多。您從此渠道收到的 Sats 越多，您的入站流動資金空間就越少。


以下是關於 LN 通路如何運作的簡單視覺示範 (由 Rene Pickhardt 所製作)：


此時，考慮到頻道的演示畫面，按一下頻道名稱，您就會看到有關該頻道的詳細資訊。


您與 Olympus 擁有單一頻道，總容量為 490 000 Sats，您一方的餘量為 378k Sats，Olympus 一方為 88k Sats。這表示在同一個頻道中，您最多可以多收到 88k Sats。


如果您需要接收超過 88k Sats（本例中的可用入站流動資金）的資料，比方說另一個 500k Sats，只要用這個數額建立一個新的 LN Invoice，就會觸發一個新的頻道請求給奧林帕斯 LSP。因此，您將獲得第二個通道。


這就是為什麼，為了避免因開多個通道而支付更多的費用，建議首次開啟一個較大的通道，比方說 1-2M Sats。一旦打開，您可以使用本指南中描述的任何外部交換服務，將這些 Sats 的一部分（例如 50%）交換到onchain。


一旦您從該通道換出，比方說換出 50%，並將 Sats 裝回您自己的 Zeus onchain Wallet，您就準備好進入下一個開啟新通道的方法 - 從 onchain 平衡。


#### 方法 B - 使用您的線上餘額


使用此方法，您可以開啟通往任何其他 LN 節點的通道，包括相同的 Olympus LSP。但是，如果您已經與 Olympus 建立了通道，建議您也與其他節點建立通道，以獲得更高的可靠性，而且還可以使用 MPP（多部分付款）。


![Image](assets/en/10.webp)


以上是使用 MPP 支付 LN Invoice 的範例。如您所見，在螢幕底部有「設定」，並會開啟一個下拉頁面，提供您即將付款的詳細資訊。在該畫面中，如果您至少開啟了 2 個頻道，則 MPP 功能預設為開啟。此外，您還可以啟動 AMP（原子多路徑），並設定您想要的特定部分。這是一項強大的功能！


對於 Zeus 這種私人節點，我建議擁有 2-3 個良好的通道 (最多 4-5)、良好的 LSP 和良好的流動性，以滿足您在 LN 上支付或接收 Sats 的所有需求。[請參閱本指南中更多的 LN 節點流動性建議](/nodes/managing-lightning-node-liquidity-en.html)。這裡也有另一個 [關於 LN 流動性的一般指南](https://Bitcoin.design/guide/how-it-works/liquidity/) 來自 Bitcoin 設計團隊。


我知道，選擇合適的對等節點並不是一件容易的事，即使對有經驗的用戶來說也是如此。[所以我會給您一些開始的選擇](https://github.com/ZeusLN/zeus/discussions/2265)，這些是我自己使用 Zeus 測試過的對等節點（我嘗試只連接到 LND 節點，以避免不相容的問題）


這裡也有一份 Zeus 的經憑證的節點對等機構清單。如果您知道好的節點，歡迎將其加入該清單中。


您可以在 Zeus 中開啟頻道，方法是按一下主視圖右下角的頻道圖示，然後按一下右上角的 + 圖示，進入頻道檢視。


![Image](assets/en/11.webp)


如果您想與特定節點開啟頻道，按一下 (A) 上角掃瞄節點 QR nodeID (在 Mempool、Amboss、1ML 上您可以取得該 QR)，所有對等詳細資訊都會被填入。


提醒：


- Zeus 嵌入式節點不使用 Tor 服務！所以請不要嘗試與 Tor 下的節點開啟通道！您對自己造成的傷害比增加隱私更大。Tor 對於 LN 來說並不能提供更多的隱私，反而會增加更多的麻煩。
- 明智地選擇您的對手，最好是優秀的 LSP、優秀的路由節點，而不是可能關閉您的通道且無法提供良好流動性的隨機普通節點。[Here I wrote a dedicated guide](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) about liquidity and example of nodes。


如果您直接點選「Open Channel to Olympus」按鈕，就會填入所需欄位，以開啟 [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581) 的頻道。


與付費的 LSP 渠道不同，您的渠道需要 On-Chain 確認，使用您的 onchain 資金（您可以在打開渠道檢視中從您的 UTXOs 中選擇）；它不會立即打開。請先查詢實際的 Mempool 費用，並根據您想要打開該通道的速度進行相應調整。


在按下開啟頻道的按鈕前，請向下滑動進階選項：


![Image](assets/en/12.webp)


您也需要確定頻道是未公佈的（私人）頻道。預設是關閉已公佈頻道的選項。不建議在 Zeus 內嵌節點啟用此選項，只有在您使用 Zeus 與遠端節點作為公共路由節點時才有用。


與付費 LSP 通道不同，使用此方法開通通道，您將無法從零費用路由中獲益。


完成後，只需按一下「開啟頻道」按鈕，等待礦工確認 tx。一旦通道打開，您就可以隨心所欲地使用通道中的 Sats 進行交易。


請記住，這些通道的所有餘額都在您這邊，所以您不會有流入的流動資金。正如我之前所說，換出或花一些 Sats 購買 LN 以上的東西來「騰出更多空間」接收。


將您的 LN 頻道想像成一杯水。您將水（Sats）倒入一個空杯子（您的通道），直到倒滿。在您喝掉一些水（花掉/換掉）之前，您不能再倒更多的水（LN）。當杯子快空時，使用換入服務倒入更多水 (Sats)。[在此閱讀更多關於外部交換服務的資訊](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html)。


也有其他 LSP 服務為您出售入站通道：LNBig 或 Bitrefill。我認為還有更多類似的服務，但現在記不起來了。


因此，如果您需要一個實際上是空的 LN 通道（從一開始餘額就是 100% 在對方端），以接收比您現有已填滿的通道更多的付款，這可能是一個非常好的選擇。您只需支付特定費用即可開啟這些通道，並獲得大量的入站空間。



## 秘訣


### 入境儲備限額


目前，由於某些 LN 代碼的限制，無法準確收到「Inbound」中顯示的金額。請務必記住，您的發票金額應略低於「頻道本地預留」金額。


![Image](assets/en/13.webp)


如上圖所示，「入站 」顯示我仍可接收 5101 Sats，但事實上此刻不可能接收更多。您可以觀察到，這與「本地預留」的數量相同。


所以請記住，當您開發票收款時，也要看看您的通路流動資金，並從中扣除當地的儲備金，如果您想把應收帳款推到極限的話。


### 給剛開始使用 Zeus node 的新使用者的快速建議：



- 正確掌握您的新通路。


例如，如果您知道一個星期後會收到 100 萬 Sats，請開設一個 200 萬的 Sats 通道，並將其交換到 onchain Wallet 或另一個（臨時）託管 LN 帳戶中，佔您流出流動資金的 50-60%。隨時準備更多的流動資金。一旦您需要更多的流動資金回到您的 Zeus 通道中，您可以將其從託管帳戶中移回。


如果您知道自己每週要傳送 500K Sats，那麼就開啟一個 100 萬 Sats 的頻道。如此一來，您仍有儲備，直到您再次填滿為止。



- 如果您是商家，而且您總是會定期收到比您花費更多的款項，請購買專用的入貨渠道。這是最便宜的方式。您只需支付很少的費用，就能獲得一個「空」的通道。



- 不要開 50-100-300-500k Sats 的無意義的小通道。您會在幾天之內填滿它們，即使您只用它們來做 ZAP。打開更大的頻道和不同的頻道，而不只是一個頻道。


一旦您開啟了一個更大的通道，您可以隨時使用外部潛水交換將 Sats 移動到您的onchain 錢包（包括回到 Zeus onchain）。保持流入和流出流動性之間的平衡是很好的，而且如果您願意的話，您還可以 「重新使用 」這些 Sats 來開啟更多的通道。


### 包裝 Invoice


如果您想在接收時增加更多隱私，可以使用「包裹 Invoice」的方法。提醒：要做到這一點，您需要與 Olympus LSP 建立通道。包裹的發票會 「隱藏 」最終目的地（您的 Zeus 節點），並向付款人顯示您的 LSP 節點為目的地。


若要取得已包裝的 Invoice，請進入主鍵盤畫面，輸入金額並按下 request。將顯示 Invoice 的正常 QR 代碼。現在，點擊右上方的 "X "按鈕，您將被重定向到 Invoice 的更多選項。


![Image](assets/en/14.webp)


現在您必須啟動上方的「啟用 LSP」選項，然後按下「建立 Invoice」按鈕。該選項將創建包裝後的 Invoice，請記住，將會收取少量費用。


### 含路線提示的發票


如果您要管理多個入站頻道的流動性，這是非常有用的功能。實際上，您可以指出要從 Invoice 接收 Sats 的入站通道。


此功能也可用於循環再平衡，當您想要將流動資金從一個填滿的通道移到另一個耗盡的通道時。


如何建立具有路由提示的 Invoice？



- 在主畫面上，向右滑動 LN 抽屜，然後按一下「接收」。
- 在 Invoice 設定中到底部啟動「插入路徑提示」按鈕，然後選擇「自訂」標籤。它會開啟一個畫面，顯示您所有可用的頻道。選擇您想要接收的頻道。
- 填寫所有其他 Invoice 詳細資料、金額、備註等，然後點選「建立 Invoice」。
- 支付該 Invoice 將使 Sats 進入指定通道。


如果您想向自己支付該 Invoice（循環再平衡），當您從同一個 Zeus 節點支付時，在支付畫面中，選擇您想用作發送付款的出站通道（流動性較高的通道）。


### 使用 Keysend 付款


Keysend 是一項被低估的 LN 功能，使用者應該多加使用。


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend)允許 Lightning Network 中的使用者，只要他們的節點有公開頻道，並啟用了 Keysend，就可以直接將付款寄給其他人 ，直接寄到他們的公開金鑰。Keysend 不需要收款人發出 Invoice。


您如何使用 Zeus 做到這一點？


只需掃描或複製目標節點 ID（或使用 Zeus 聯繫人將常規目標節點儲存為聯繫人），然後在 Zeus 主畫面中點擊 「發送 」按鈕。在該畫面中貼上節點 ID 或從連絡人中選擇。


輸入 Sats 的金額、必要的訊息 (是的，您也可以使用它作為 LN 的秘密聊天工具)，然後按一下「傳送」按鈕。完成！


![Image](assets/en/15.webp)


如果您與目標對等機構有直接的通道，則不會涉及任何費用。


如果您與目標對等方沒有直接通道，則 keysend 付款會像正常的 LN Invoice 付款一樣支付費用，路由路徑和其他付款一樣。只是，請記住，它不會留下任何 LN Invoice 的痕跡。


## 銜接


我建議您閱讀後續指南 [Zeus 的進階用法](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html)，裡面有更多的說明和使用案例。


還有...就是這樣！從現在開始，您只需在手機上將 Zeus Node 當作普通的 BTC/LN Wallet 使用即可。UI 非常簡單易用，對任何類型的用戶都很直觀，我想我不需要輸入更多關於如何付款和收款的細節。


總之，以下是比較隱私權圖表 ：


![Image](assets/en/16.webp)