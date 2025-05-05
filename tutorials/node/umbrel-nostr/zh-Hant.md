---
name: Umbrel Nostr
description: 在 Umbrel 上設定和使用 Nostr 應用程式
---

![cover](assets/cover.webp)



## 先決條件：安裝 Umbrel



Umbrel 是一個開放原始碼平台，可讓您輕鬆地在個人伺服器上託管 Bitcoin 應用程式和其他服務。這是一個多合一的解決方案，可大幅簡化 Bitcoin 節點和分散式應用程式的自我託管。



請確認您已依照我們的安裝指南安裝 Umbrel：



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Nostr 簡介



**Nostr** 是專為社交網路設計的開放式分散網路協定。其名稱代表 _"Notes and Other Stuff Transmitted by Relays"_。它允許任何人發佈訊息（筆記），以 JSON 事件的方式管理，並透過中繼伺服器而非中央平台來傳播。每個使用者都擁有一對加密金鑰 (私鑰/公鑰)，可作為識別碼：公鑰 (npub) 可識別使用者，私鑰 (nsec) 則可簽署訊息。由於這種分散式架構，**Nostr 提供了抗檢查**和極大的靈活性：您可以使用多個用戶端，並連接到任意多個中繼器，而無需依賴單一伺服器。



簡而言之，Nostr 是一種分散式通訊協定，**客戶端**（使用者應用程式）透過**中繼器**（伺服器）傳送和接收事件。自 2023 年以來，此通訊協定因其分散性和資料主權的價值，特別受到 Bitcoin 社群的歡迎。



**注意：** 要使用 Nostr，您需要您的私人密碼匙 (由 Nostr 客戶端或透過專用擴充套件產生)。 **切勿分享您的私人密碼匙**，因為這會允許任何人冒充您。請將它保存在安全的地方，並使用安全的金鑰管理工具（請參閱下面的提示）。



## Nostr 的 Umbrel 應用程式



Umbrel 提供一個整合應用程式的生態系統，讓您在個人節點上充分利用 Nostr 的優勢。我們將詳細介紹主要 Nostr 相關應用程式的使用： **Nostr Relay**、**noStrudel**、**Snort** 和 **Nostr Wallet Connect**。每個應用程式都能滿足特定需求：_Nostr Relay_ 是**私人中繼伺服器**，_noStrudel_ 和 _Snort_ 是**Nostr 客戶端** (閱讀/出版筆記的介面)，而 _Nostr Wallet Connect_ 則是將您的**Lightning 作品集**連結至 Nostr 的工具。



### Nostr 中繼 - 您在 Umbrel 上的私人中繼



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** 是 Umbrel 的官方應用程式，用於在您的節點上運行您**自己的 Nostr 中繼**。主要目的是擁有一個**私人且可靠的中繼，以**即時備份您所有的Nostr**活動。換句話說，透過在公共中繼之外使用這個個人中繼，您可以確保所有的筆記、訊息和反應都會被複製回家，避免受到審查或資料遺失。



**安裝：** 從 Umbrel App Store (類別 _Social_)，安裝 _Nostr Relay_。啟動後，應用程式會在背景執行 (docker 服務)。



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



您會透過 Umbrel 看到其 Interface 網頁：它提供基本資訊，最重要的是您中繼的 URL (右上方)，您需要複製以供進一步使用。同步按鈕 (地球圖示) 也是可用的。



**要利用您的 Umbrel 繼電器 ：



**在您的用戶端應用程式 (例如 iOS 上的 Damus、Android 上的 Amethyst、Umbrel 上的 Snort 或 noStrudel 等) 中，加入您先前複製的私有中繼的 URL。預設情況下，Umbrel 中繼監聽埠為 **4848**。如果您在本機網路存取，會得到類似以下的 URL：`ws://umbrel.local:4848`（或使用 Umbrel 的本機 IP）。



如果您使用 Tailscale (請參閱下文)，您甚至可以使用 MagicDNS DNS 別名 (通常是 `umbrel` 或自動產生的名稱) 從任何地方存取，總是使用 4848 連接埠。



如果您偏好 Tor，請取得 Umbrel 的 .onion Address，並透過 Tor 相容的瀏覽器或用戶端與連接埠 4848 搭配使用（請參閱 Tor 章節）。



將 URL 加入 Nostr 用戶端的中繼設定後，連接到此中繼。您應該會在用戶端中看到 Umbrel 中繼已經連線（通常以 Green 點或類似的標誌表示）。



**同步歷史記錄 (選用)**：在 Umbrel 上 _Nostr Relay_ 的 Interface 網頁中，按一下 **globe** 🌐 圖示 (在頁面頂端)。這個動作會強制您的 Umbrel Relay 連線到您的其他 Relay（在您的客戶端中設定的那些 Relay），以**匯入您舊有的公開**活動。這表示您過去透過公開中繼發表或閱讀的筆記，也會下載並儲存在您的私人中繼上。請等待同步化進行。



**照常使用Nostr：** 從現在開始，您在Nostr上執行的任何新活動（發佈的筆記、反應、加密的私人訊息等）都會照常轉發到公共中繼**，同時也會轉發到您的Umbrel中繼**。如果您的 Nostr 客戶端設定正確，它會將每個事件傳送至所有中繼站 (包括您的中繼站)。您的私人中繼將作為實時備份。即使在暫時斷線的情況下，您的客戶也能夠透過此中繼稍後重新同步遺失的資料。



在後台，Umbrel 的 _Nostr Relay_ 是基於開放原始碼的 **nostr-rs-relay**專案 (Rust 通訊協定實作)。它支援整個 Nostr 通訊協定和許多標準 NIP (NIP-01、02、03、09、11、12、15、16、20、22、26、28、33 等)，保證與客戶的最大相容性。



### noStrudel - 適用於探索者的 Nostr 客戶端



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel**是面向強大用戶的 Nostr 網路用戶端，非常適合詳細瞭解和探索 Nostr 網路。它是一種沙箱，用來檢查事件和中繼，以及實驗通訊協定的進階功能。Interface 是英文版本，技術性相對較高，適合對 Nostr 內部運作感到好奇的資深使用者使用。



**安裝：** 從 Umbrel App Store (類別 _Social_)安裝 _noStrudel_。啟動後，可透過瀏覽器在 Umbrel 的 Address (例如 `http://umbrel.local` 或透過其 .onion/Tailscale 進行存取，請參閱外部存取部分)。



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**設定繼電器：** 開啟 noStrudel 時，您會在右上角看到「設定繼電器」按鈕。按一下即可設定您的繼電器。



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



在此頁面中，貼上之前複製的 Umbrel 中繼 URL。您也可以新增應用程式預設的其他中繼。設定好中繼後，點選左下方的「登入」繼續。



![Options de connexion dans noStrudel](assets/fr/06.webp)



**連線：** noStrudel 提供您多種連線選項。在我們的例子中，我們將選擇 「私鑰」，並貼入您先前產生的 Nostr 私鑰。如果您還沒有金鑰，您可以安裝 [Nostr Connect] 擴充套件 (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) 來建立和/或儲存您的 Nostr 金鑰，從而更安全地與各種 Nostr 應用程式通訊。



![Interface principale de noStrudel](assets/fr/07.webp)



連線後，您可以使用 noStrudel 透過 Nostr 分享您的筆記。Interface 可讓您存取 ：





- 完整的 Nostr 面板，包含備註時間線、通知、訊息、個人資料搜尋
- 中繼管理與連線狀態
- 檢查事件及其 JSON 內容的進階工具
- 時間軸篩選器和 PIN 碼的設定選項



**Tip:** 在 _noStrudel_ 上，您可以設定 _timeline filterters_ 或測試不同的 _NIPs (Nostr Implementation Possibilities)_。例如，檢查對 NIP-05 (分散式識別碼) 或更多最新功能的支援。這使得 _noStrudel_ 成為在受控環境中進行實驗的絕佳工具。



### Snort - Umbrel 上的現代 Nostr 客戶



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** 是 Umbrel 上的另一款 Nostr 網頁用戶端，提供現代、快速、簡潔的 **Interface** 與分散式社群網路互動。與以強大使用者為目標的 noStrudel 不同，_Snort_ 的目標是在不犧牲功能的前提下簡化使用。它以 React 建構，提供整潔的使用者介面，讓人聯想到經典的社群網路，適合日常使用。



**安裝：** 從 Umbrel App Store（類別 _Social_）安裝 _Snort_。



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



開啟 Snort 時，您會看到左下角有一個「註冊」按鈕。



![Options de connexion dans Snort](assets/fr/10.webp)



您可以選擇註冊或連線到現有帳號（這就是本教學所要做的）。



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort 提供多種連接方法。您可以使用先前安裝的 Nostr Connect 延伸或其他可用的方法。連線後，您就可以充分使用應用程式。



來自 _Snort_ 的 Interface 提供 ：





- ** 帖子/討論/全局** 顯示可在您的筆記、線程討論或全局饋送之間導覽
- 用於 **通知**、**訊息** (DM)、**搜尋**、**個人資料**等的標籤。
- **+** 或 _Write_ 按鈕可發佈新筆記
- 管理**訂閱（以下）**和**清單**
- 繼電器管理功能表可新增/移除繼電器，並追蹤其可用性



**建議的中繼設定：** 若要新增 Umbrel 中繼，請前往設定 - 中繼。在 Snort 的中繼列表中輸入您的中繼 URL (`ws://umbrel:4848`或其他 URL，視您的設定而定)。如此一來，Snort 除了在公開中繼上發佈您的筆記外，也會在私人中繼上發佈您的筆記。



### Nostr Wallet Connect - 將您的 Lightning Wallet 連接到 Nostr



**Nostr Wallet Connect (NWC)** 是一個應用程式，可將您的 Umbrel (Lightning)** 節點連接到相容的 Nostr 應用程式，以進行 Lightning 付款 (例如，發送 _zaps_ ，那些「喜歡」內容的微額付款)。在本教程中，我們將介紹如何將 noStrudel 連接到您的 Lightning 節點，以便直接從 Interface 進行付款。



**安裝與設定：**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



從 Umbrel 上的 Alby 商店安裝 _Nostr Wallet Connect_。



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



在 noStrudel 中，按一下右上角的個人資料，然後按一下「管理」按鈕。



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



按一下「閃電」，然後按一下「連接 Wallet」。



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



在可用的連接選項中，選擇「Umbrel」。



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



按一下「連線」，就會自動轉到您的 Umbrel Nostr Wallet 連線階段。



![Page de configuration des autorisations NWC](assets/fr/17.webp)



在 Nostr Wallet Connect 頁面上，您可以 ：




   - 定義您的最高預算
   - 驗證授權
   - 設定連線的到期時間


按一下「連線」以完成。



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



您會重定向到 noStrudel，並收到確認訊息：您現在可以從 Wallet/LND 節點斬殺整個世界！



感謝 NWC，您透過 Nostr 進行的**Lightning 付款**（斬獲獎勵帖、_Value for Value_ 付款等）都從**您自己的節點**開始。您不再需要每次都透過外部服務或手機掃瞄 QR 來進行交易。使用者體驗大幅提升，同時仍保持_非保管_和隱私友好。



如果您想知道如何在 Umbrel 上建立自己的 Lightning 節點，我建議您參閱這份其他全面的教學：



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## 進階組態與安全性



在進階層級一起使用 Umbrel 和 Nostr 需要特別注意**安全性**和**連線性**。以下是一些如何保護您的配置並在任何地方以最佳方式存取配置的提示。



### 安全的外部存取：Tor 和 Tailscale



基於安全考量，您的 Umbrel 預設只能在本機網路存取 (並透過 Tor)。若要離家與 Nostr 互動，您有兩個首選的解決方案： **Tor**（透過洋蔥網路匿名存取）和**Tailscale**（私人 VPN 網路）。





- 透過 Tor 存取：** Umbrel 自動為其 Interface 網路和應用程式配置**Tor 服務 (.onion)**。這表示您可以在任何地方使用 Tor 瀏覽器存取 Interface Umbrel (包括 _noStrudel_ 或 _Snort_)，而不會暴露您的公開 IP。_Tor 是用來從您的區域網路以外存取您的 Umbrel 服務，而不會讓您的裝置暴露在網際網路上 ([在您的系統上設定 Tor - 指南 - Umbrel 社群](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww))。_ 若要使用此選項，請前往 Umbrel 設定，並擷取您的 Umbrel 的 .onion URL (或掃描提供的 QR code)。在 Tor 瀏覽器上，存取此 .onion Address：您將會得到與本機相同的 Interface。然後您就可以像在家中一樣使用您的 Nostr 應用程式。


**Nostr relay via Tor:** 如果您希望您的 Nostr relay 可以讓您的客戶（或授權的朋友）透過 Tor 連線，這是可以做到的。Umbrel 並沒有直接提供中繼的 .onion Address，但由於它是在 4848 連接埠上執行，您可以使用 .onion Address：





    - 使用 UI Umbrel 的 .onion Address，並設定您的用戶端透過此 Interface 連線（對 WebSocket 來說並不可行）、





    - 或***將 4848 連接埠開放為獨立的洋蔥服務。這需要在 Umbrel 上設定 Tor (僅適用於熟悉 SSH 的進階使用者)。另外，也可以考慮在其他伺服器上建立 Tor tunnel**，重定向到 Umbrel：然而，對於個人使用而言，使用 Tailscale 是最簡單的方法。





- 透過 Tailscale 存取：** [Tailscale](https://tailscale.com/) 是網狀 VPN 解決方案，可在您的裝置與 Umbrel 之間建立虛擬私人網路。其優點是：它的工作方式就像您在區域網路上一樣，不過是透過網際網路，經過加密且不需要複雜的設定。 **Tailscale 會為您的 Umbrel 指定固定 IP 和私人網域名稱，不論其網路位置為何 ([Tailscale|Umbrel應用程式商店](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard))**。實際上，一旦您在 Umbrel 上安裝了 Tailscale (從 Umbrel App Store，類別 _Networking_) ***和***您的裝置 (行動裝置、電腦...)，您就可以透過 Address 如`100.x.y.z` (Tailscale IP) 或名稱如`umbrel.tailnet123.ts.net`到達 Umbrel。


對 Nostr_來說，Tailscale 是非常有用的：您的手機如果有啟動 Tailscale，就可以連接到 `ws://umbrel:4848` (感謝 MagicDNS) 或直接連接到 Tailscale IP 和連接埠 4848 來使用中繼。像 Damus 或 Amethyst 之類的用戶端將會看到你的 Umbrel，就像它在同一個本地網路中一樣。 **祕訣：** 在 Tailscale 啟用 **MagicDNS** 選項，以使用主機名稱 `umbrel` 代替記憶 IP。這可確保即使您在移動中，也能順暢地連線到您的中繼站([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past))。


更重要的是，Tailscale 可以讓您透過簡單的瀏覽器，使用私人 IP 或指定的網域名稱，存取 Interface Umbrel (也就是 _noStrudel/Snort_ 網路用戶端)。不需要 Tor 瀏覽器，而且資料傳輸速度通常比透過 Tor 網路更好。




**注意：Tor 和 Tailscale 並非互相排斥。您可以為了匿名存取或特定服務而保持 Tor 啟動，並因為 Tailscale 的簡易性而在日常使用。在這兩種情況下，您都不需要在路由器上開啟連接埠，這可以加強安全性。



### 保護您的 Nostr 中繼 (建議實作)



如果您在 Umbrel 上託管 Nostr relay，尤其是在進階的情況下，請務必應用一些良好的實務：





- 隱私或受限制的中繼：**預設情況下，您的 Umbrel 中繼是隱私的（不公開宣佈），如果您只透過 Tailscale 或您的區域網路存取，陌生人將無法存取。 ** 保持連結機密 ** 請勿在公開的 Nostr 網路上廣播，除非您想自願接待其他使用者，這是另一個問題 (節制、頻寬等)。對於個人使用，我們建議只限您自己存取，必要時也只限幾位可信賴的親朋好友存取。





- 白名單/認證**：nostr-rs-relay 實作支援 **NIP-42** 認證機制，以及公開金鑰白名單。透過啟用這些選項，您可以限制您的 relay，讓它 ** 只接受由特定金鑰 (您的) 簽署的事件**，或客戶端必須經過驗證才能發佈。設定這些選項需要在 Umbrel 中編輯 relay 的 `config.toml` 配置檔 (透過 Docker 容器中的 SSH) 。這樣，即使有人發現您的中繼，如果他們不在清單上，就無法在那裡發佈任何東西。





- 更新和維護：** 保持您的 Umbrel 和 _Nostr Relay_ 應用程式為最新版本。更新可能包括性能改進（如更好的垃圾郵件處理）和安全修復。在 Umbrel 上，請定期到 App Store 檢查 _Nostr Relay_ 的更新，並在必要時應用這些更新。





- 監控與限制：** 密切注意中繼器的使用情況。nostr-rs-relay提供可設定的**速率和儲存限制**（配置中的 「限制」，例如每秒事件數量、最大事件大小、舊事件清除......）。對於私人使用，您可能不需要碰這些，但請注意這些參數是存在的，如果您需要的話（[nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)）。





- 確保 Nostr 金鑰的安全：** 這一點已經提到，但它是至關重要的：永遠不要在您不完全信任的 Interface 中輸入您的 Nostr 私密金鑰。取而代之，使用瀏覽器擴充套件或外部裝置（例如獨立電話上的 Nostr _signers_）來簽署敏感的動作。在 Umbrel 上，您的網路用戶端如 _Snort_ 和 _noStrudel_ 可以透過 NIP-07 在不知道您的密匙的情況下工作。利用這個機會，結合舒適與安全。




按照這些提示，您的 Umbrel 節點與 Nostr 的整合將同時具有強大的**和**安全性。您將擁有一個完整的環境：一個用於 Lightning 付款的 Bitcoin 節點、一個用於資料主權的私有 Nostr 中繼，以及用於瀏覽這個新的分散式社交網路的高效能 Nostr 網頁用戶端。享受與 Umbrel 一起探索 Nostr 的樂趣！