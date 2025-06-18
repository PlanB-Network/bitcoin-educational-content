---
name: RoninDojo

description: 安裝和使用您的 RoninDojo Bitcoin 節點。
---
***警告:**在 Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被扣押之後，RoninDojo 的某些功能（例如 Whirlpool）已不再運作。不過，這些工具有可能在未來幾週內以不同方式恢復或重新啟動。此外，由於 RoninDojo 的程式碼託管在 Samourai 的 GitLab 上，而 GitLab 也被查封，因此目前無法從遠端下載程式碼。RoninDojo 團隊可能正在努力重新發布程式碼。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


本教學專門用於安裝 RoninDojo v1。要利用最新的改進和功能，我強烈建議您參考我們的教程，專門用於在您的 Raspberry Pi 上直接安裝 RoninDojo v2：___________________________________________________。

https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

要真正參與 Bitcoin 網路，運行和使用自己的節點是不可或缺的。雖然運行 Bitcoin 節點不會為使用者帶來任何經濟上的好處，但卻能讓使用者保護自己的隱私、獨立行事，並控制自己對網路的信任。


在本文中，我們將詳細介紹 RoninDojo，這是運行您自己的 Bitcoin 節點的絕佳解決方案。


### 目錄：



- RoninDojo 是什麼？
- 選擇何種硬體？
- 如何安裝 RoninDojo？
- 如何使用 RoninDojo？
- 總結


如果您不熟悉 Bitcoin 節點的運作方式及其作用，我建議您先閱讀這篇文章：Bitcoin 節點 - 第 1/2 部分：技術概念。


![Samourai](assets/1.webp)


## RoninDojo 是什麼？


Dojo 是由 Samourai Wallet 團隊開發的完整 Bitcoin 節點伺服器。您可以在任何機器上自由安裝。


RoninDojo 是 Dojo 和其他各種工具的安裝助手和管理工具。RoninDojo 以 Dojo 的原始實作為基礎，並加入許多其他工具，同時也讓安裝和管理變得更容易。


他們也提供「隨插即用」的硬體，RoninDojo Tanto，將 RoninDojo 預先安裝在其團隊組裝的機器上。Tanto 是付費的解決方案，適合不想弄髒手的人使用。


RoninDojo 的程式碼是開放原始碼，因此也可以將此解決方案安裝在您自己的硬體上。此方案具有成本效益，但需要多一些操作，這就是我們在本文中要做的。


RoninDojo 是一個 Dojo，因此它可以輕鬆地將 Whirlpool CLI 整合到您的 Bitcoin 節點中，讓您擁有最佳的 CoinJoin 體驗。有了 Whirlpool CLI，您不僅可以讓您的比特幣全天候混音，而不需要開著您的個人電腦，而且還可以大大提高您的隱私。


RoninDojo 整合了許多依賴於您的 Dojo 的其他工具，例如 Boltzmann 計算器（可決定交易的隱私等級）、Electrum 伺服器（可將您的不同 Bitcoin 荷包連接至您的節點）或 Mempool 伺服器（可私下觀察您的交易）。

與我在本文中向您介紹的另一個節點解決方案（如 Umbrel）相比，RoninDojo 深深專注於優化使用者隱私的「on chain」解決方案和工具。因此，RoninDojo 不允許與 Lightning Network 互動。

與 Umbrel 相比，RoninDojo 提供的工具較少，但 Ronin 上幾個比特幣玩家必備的功能卻非常穩定。


因此，如果您不需要 Umbrel 伺服器的所有功能，只想要一個簡單穩定的節點，加上一些必要的工具，例如 Whirlpool 或 Mempool，那麼 RoninDojo 對您來說可能是一個很好的解決方案。


在我看來，Umbrel 的開發重點主要放在 Lightning Network 和多功能工具上。它仍然是 Bitcoin 節點，但目標是讓它成為多工作業的迷你伺服器。相較之下，RoninDojo 的開發重心更貼近 Samourai Wallet 的團隊，並著重於比特币玩家必備的工具，讓 Bitcoin 上的隱私權完全獨立並有最佳化的管理。


請注意，設定 RoninDojo 節點比設定 Umbrel 節點稍微複雜一些。


現在我們已經可以描繪 RoninDojo 的圖像，讓我們一起看看如何設定這個節點。


## 選擇何種硬體？


要選擇託管和執行 RoninDojo 的機器，您有幾個選項。


如前所述，最簡單的選擇是訂購 Tanto，這是專為此目的設計的隨插即用機器。若要訂購，請按這裡：[link](https://shop.ronindojo.io/product-category/nodes/).


由於 RoninDojo 團隊製作開放源代碼，因此也可以在其他機器上實現 RoninDojo。您可以在此頁面找到最新版本的安裝精靈：[連結](https://ronindojo.io/en/downloads.html)，而最新版本的程式碼則在此頁面：[link](https://code.samourai.io/ronindojo/RoninDojo).


就我個人而言，我將它安裝在 Raspberry Pi 4 8GB 上，一切運作完美。


但請注意，RoninDojo 團隊表示機殼與 SSD 轉接器經常會發生問題。因此，我們不建議您使用附有連接線的機殼來安裝機器的SSD。反之，最好使用專為您主機板設計的儲存擴充卡，例如這款：Raspberry Pi 4 儲存擴充卡。


以下是如何設定您自己的 RoninDojo 節點的範例：



- 一台 Raspberry Pi 4。
- 有風扇的機殼。
- 相容的儲存擴充卡。
- 一條電源線。
- 16GB 或以上的工業級 micro SD 卡。
- 1 TB 或更大的 SSD。
- RJ45 乙太網路線，建議使用 8 類。


## 如何安裝 RoninDojo？


### 步驟 1：準備可開機的 micro SD 卡。


組裝好機器後，您就可以開始安裝 RoninDojo。為此，首先將適當的磁碟映像燒錄到可開機的 micro SD 卡上。


將您的 micro SD 卡插入個人電腦，然後到 RoninDojo 官方網站下載 RoninOS 磁碟映像檔：https://ronindojo.io/en/downloads.html。


下載與您硬體相對應的磁碟映像檔。在我的情況下，我下載了 "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ" 映像：


![Download RoninOS disk image](assets/2.webp)


下載映像後，請使用相應的 .SHA256 檔案驗證其完整性。我將在本文中詳細說明如何執行：如何在 Windows 上驗證 Bitcoin 軟體的完整性？


驗證 RoninOS 完整性的具體說明也可在此頁面上找到：https://wiki.ronindojo.io/en/extras/verify。


若要將此影像燒錄到 micro SD 卡上，您可以使用 Balena Etcher 等軟體，您可以在此處下載：https://www.balena.io/etcher/。


若要執行此動作，請在 Etcher 中選擇映像檔，然後將其快閃到 micro SD 卡上：


![Burn disk image with Etcher](assets/3.webp)


操作完成後，您可以將可開機 micro SD 卡插入 Raspberry Pi 並開機。


### 步驟 2：配置 RoninOS。


RoninOS 是您的 RoninDojo 節點的作業系統。它是 Linux 發行版 Manjaro 的修改版本。啟動您的機器並等上幾分鐘之後，您就可以開始配置。


若要遠端連線，您需要找到 RoninDojo 機器的 IP Address。要做到這一點，您可以，例如，連接到您的互聯網盒子的管理面板，或者您也可以下載軟件，如 https://angryip.org/，掃描您的本地網絡，找到機器的 IP。


一旦找到 IP，您就可以使用 SSH 從連接至相同區域網路的另一台電腦控制您的機器。


從執行 macOS 或 Linux 的電腦，只要開啟終端機即可。從執行 Windows 的電腦，您可以使用 Putty 之類的專門工具，或直接使用 Windows PowerShell。


開啟終端機後，輸入下列指令：

```
ssh root@192.168.?.?
```


只需用之前找到的 RoninDojo 的 IP 取代兩個問號即可。

秘訣：在 Shell 中，按一下滑鼠右鍵即可貼上項目。


接下來，您將到達 Manjaro 控制面板。使用箭頭在下拉清單中變更目標，選擇正確的鍵盤配置。


![Manjaro Keyboard Configuration](assets/4.webp)


為您的會話選擇使用者名稱和密碼。使用強密碼並做安全備份。您可以選擇在安裝時使用弱密碼，之後透過「複製貼入」到 RoninUI 來輕鬆變更密碼。這將允許您使用非常強大的密碼，而無需在安裝 Manjaro 時花太多時間手動輸入。


![Manjaro Username Configuration](assets/5.webp)


接下來，還會要求您選擇 root 密碼。對於 root 密碼，請直接輸入強密碼。您將無法從 RoninUI 修改它。此外，請記住安全備份此 root 密碼。


然後輸入您的位置和時區。


![Manjaro Time Zone Configuration](assets/6.webp)


![Manjaro Location Configuration](assets/7.webp)


接下來，選擇主機名稱。


![Manjaro Hostname Configuration](assets/8.webp)


最後，驗證 Manjaro 設定資訊並確認。


![Verification of ManjaroOS Configuration Information](assets/9.webp)


### 步驟 3：下載 RoninDojo。


RoninOS 的初始配置將會完成。一旦完成，如上面的截圖所示，機器將重新啟動。等待片刻，然後輸入以下命令重新連接到您的 RoninDojo 機器：

```
ssh username@192.168.?.?
```


只需用您之前選擇的使用者名稱取代「使用者名稱」，然後用您 RoninDojo 的 IP 取代問號即可。


然後輸入您的使用者密碼。


在終端機中，它會看起來像這樣：


![SSH Connection to RoninOS](assets/10.webp)


現在您已連接到您的機器，該機器目前只有 RoninOS。現在您需要在上面安裝 RoninDojo。


輸入以下指令下載最新版本的 RoninDojo：

```
git clone https://code.samourai.io/ronindojo/RoninDojo
```


下載速度會很快。在終端機，您會看到這個：


![Cloning RoninDojo](assets/11.webp)


等待下載完成，然後安裝並使用下列指令存取 RoninDojo 使用者 Interface：

```
~/RoninDojo/ronin
```


系統會要求您輸入使用者密碼：


![Bitcoin Node Password Verification](assets/12.webp)


此命令僅在您首次訪問 RoninDojo 時需要。之後，若要透過 SSH 存取 RoninCLI，您只需輸入 [SSH username@192.168.???] 指令，將「使用者名稱」改為您的使用者名稱，並輸入您節點的 IP Address。系統會提示您輸入使用者密碼。


接下來，您會看到這個華麗的動畫：


![RoninCLI launch animation](assets/13.webp)


然後，您最終會到達 RoninDojo CLI 使用者 Interface。


### 步驟 4：安裝 RoninDojo。


從主功能表，使用鍵盤上的方向鍵導航至「系統」功能表。按下 Enter 鍵確認您的選擇。


![RoninCLI navigation menu to System](assets/14.webp)


然後前往「系統設定與安裝」功能表。


![RoninCLI navigation menu to RoninDojo system installation](assets/15.webp)


最後，使用空格鍵勾選「系統設定」和「安裝 RoninDojo」，然後選擇「接受」開始安裝。


![RoninDojo installation confirmation](assets/16.webp)


讓安裝安靜地進行。就我而言，大約花了 2 小時。在安裝過程中，請開啟您的終端機。


偶爾檢查您的終端機，因為在安裝的某些階段會要求您按鍵，例如這裡：


![RoninDojo installation in progress](assets/17.webp)


安裝結束時，您會看到不同的容器開始運作：


![Node container startup](assets/18.webp)


然後您的節點會重新啟動。再次連線到 RoninCLI 進行下一步。


![Bitcoin node restart](assets/19.webp)


### 步驟 5：下載 Proof-of-Work 鏈，並存取 RoninUI。


安裝完成後，您的節點會開始下載 Bitcoin Proof-of-Work 鏈。這稱為初始區塊下載 (IBD)。通常需要 2 到 14 天，視您的網際網路連線和裝置而定。


您可以透過存取 RoninUI 網頁 Interface 來追蹤鏈的下載進度。


若要從本機網路存取，請在瀏覽器的 Address 欄輸入下列內容：



- 直接輸入您機器的 IP Address (192.168.?.?)
- 或輸入： ronindojo.local


如果您正在使用 VPN，請記得停用 VPN。


### 可能的轉折


如果您無法從瀏覽器連線至 RoninUI，請從透過 SSH 連線至節點的終端檢查應用程式是否正常運作。按照之前的步驟連接至主功能表：



- 類型：SSH username@192.168.??? 用您的憑證取代。



- 輸入您的使用者密碼。


進入主功能表後，前往 **RoninUI > 重新啟動**


如果應用程式重新啟動正常，則是瀏覽器的連線有問題。檢查您是否使用 VPN，並確認您與節點連線至相同的網路。


如果重新啟動產生錯誤，請嘗試更新作業系統，然後再重新安裝 RoninUI。更新作業系統： **系統 > 軟體更新 > 更新作業系統**


更新和重新啟動完成後，請透過 SSH 重新連接到您的節點，並重新安裝 RoninUI： **RoninUI > 重新安裝**


再次下載 RoninUI 後，嘗試透過瀏覽器連接 RoninUI。


**Tip:** 如果您不小心退出 RoninCLI，並發現自己在 Manjaro 終端，只需輸入「ronin」指令，即可直接返回 RoninCLI 的主選單。


### 網路登入


您也可以使用 Tor 從任何網路登入 RoninUI 網路 Interface。要做到這一點，請從 RoninCLI 擷取 RoninUI 的 Tor Address：**憑證 > Ronin UI**


擷取以 .onion 結尾的 Tor Address，然後在 Tor 瀏覽器中輸入此 Address，登入 Ronin UI。請小心不要洩漏您的各種憑證，因為它們是敏感資訊。


![RoninUI web login interface](assets/20.webp)


登入後，系統會要求您輸入使用者密碼。這與您透過 SSH 登入時使用的密碼相同。


![RoninUI web interface management panel](assets/21.webp)


我們可以在這裡看到 IBD（初始區塊下載）的進度。請耐心等待，您正在檢索自 2009 年 1 月 3 日以來在 Bitcoin 上進行的所有交易。


下載整個 Blockchain 之後，索引器會壓縮資料庫。此操作大約需要 12 小時。您也可以在 RoninUI 上的 "Indexer "下追蹤其進度。


之後您的 RoninDojo 節點就可以完全運作了：


![Indexer synchronized at 100% functional node](assets/22.webp)


如果您想要將使用者密碼變更為更強的密碼，現在就可以從「設定」標籤中進行變更。在 RoninDojo 上，沒有額外的安全 Layer，因此我建議選擇一個真正強大的密碼，並注意其備份。


## 如何使用 RoninDojo？


下載並壓縮鏈後，您就可以開始享受新 RoninDojo 節點提供的服務。讓我們看看如何使用它們。


### 將 Wallet 軟體連接到電器。


您新安裝和同步化節點的第一個效用，就是將您的交易廣播到 Bitcoin 網路。因此，您很可能要將您不同的 Wallet 管理軟體連接到它。


您可以使用 Electrum Rust Server (electrs)。該應用程式通常已預先安裝在您的 RoninDojo 節點上。如果沒有，您可以從 RoninCLI Interface 手動安裝。


只需前往 **應用程式 > 管理應用程式 > 安裝 Electrum 伺服器**


若要取得 Electrum 伺服器的 Tor Address，請從 RoninCLI 功能表前往：

**Credentials > Electrs**


您只需在 Wallet 軟體中輸入 .onion 連結。例如，在 Sparrow Wallet 中，移至選項卡：

**檔案 > 偏好設定 > 伺服器**


在伺服器類型中，選擇 `Private Electrum`，然後在對應的欄位中輸入您的 Electrum 伺服器的 Tor Address。最後，點選「測試連線」來測試並儲存您的連線。


![Sparrow Wallet connection interface to an electrs](assets/23.webp)


### 連接 Wallet 軟體至 Samourai Dojo。


您也可以使用 Samourai Dojo 將相容的 Software Wallet 連接到 RoninDojo 節點，而不是使用 Electrs。例如，Samourai Wallet 提供此選項。


要做到這一點，只需掃描您的 Dojo 的連接 QR 代碼。要從 RoninUI 訪問，請點擊 「儀表板 」標籤，然後點擊 Dojo 方塊中的 「管理 」按鈕。然後，您就可以看到 Dojo 和 BTC-RPC Explorer 的連線 QR 代碼。若要顯示它們，請按一下「顯示值」。


![Retrieving the connection QR code to Dojo](assets/24.webp)


要將 Samourai Wallet 連接到您的 Dojo，您需要在安裝應用程式時掃描此 QR 代碼：


![Connecting to Dojo from the Samourai Wallet application](assets/25.webp)


### 使用您自己的 Mempool Explorer。


作為 Bitcoiners 的必備工具，探索者允許您檢查 Bitcoin 鏈的各種資訊。例如，使用 Mempool，您可以即時查看其他用戶收取的費用，以便相應調整您的費用。您也可以檢查您的交易的確認狀態或查看 Address 的餘額。


這些探索者工具可能會讓您暴露於隱私風險中，並需要您信任第三方的資料庫。當您使用此線上工具而不經過自己的節點時：



- 您有洩露 Wallet 資訊的風險。



- 您信任他們主持的 Proof-of-Work 連鎖網站上的網站管理員。


為了避免這些風險，您可以透過 Tor 網路在您的節點上使用自己的 Mempool 實例。使用此解決方案，您不僅可以在使用服務時保護自己的隱私，而且由於您查詢自己的資料庫，因此也不再需要信任供應商。


為此，請先從 RoninCLI 安裝 Mempool Space Visualizer：


**應用程式 > 管理應用程式 > 安裝 Mempool Space Visualizer**


安裝完成後，擷取連結至您的 Mempool。Tor Address 將允許您從任何網路存取。同樣地，我們透過 RoninCLI 擷取此連結：


**Credentials > Mempool**


![Retrieve Tor Mempool address](assets/26.webp)


只需在 Tor 瀏覽器中輸入您的 Mempool Tor Address，即可根據您自己的資料享受您自己的 Mempool 實例。我建議您將此 Tor Address 加入收藏夾，以便更快速地存取。您也可以在桌面上建立捷徑。


![Mempool Space interface](assets/27.webp)


如果您還沒有 Tor 瀏覽器，可以在這裡下載： https://www.torproject.org/download/


您也可以透過智慧型手機安裝 Tor 瀏覽器，並輸入相同的 Address 來存取。從任何地方，您都可以使用自己的節點檢視 Bitcoin 連鎖的狀態。


### 使用 Whirlpool CLI。


您的 RoninDojo 節點也包含 WhirlpoolCLI，這是一個遠端命令列 Interface，用於自動化 Whirlpool 混合。


當您使用 Whirlpool 實作執行 CoinJoin 時，您使用的應用程式必須保持開啟，才能執行混音和混音。對於想要擁有高安裝集的使用者來說，這個過程可能會很乏味，因為使用 Whirlpool 執行應用程式的裝置必須持續保持開啟狀態。實際上，這表示如果您想讓您的 UTXOs 進行全天候混音，您就需要讓您的個人電腦或手機持續開啟應用程式。


解決這個限制的方法之一，是在 Bitcoin 節點等需要持續開機的機器上使用 WhirlpoolCLI。如此一來，我們的 UTXO 就能全天候進行混音，而無需讓 Bitcoin 節點以外的其他機器持續運作。

WhirlpoolCLI 與 WhirlpoolGUI 一起使用，WhirlpoolGUI 是一個圖形化的 Interface ，安裝在個人電腦上，方便管理 Coinjoins。我將在這篇文章中詳細解釋如何設定 Whirlpool CLI 與您自己的道場：[link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).


若要瞭解更多關於 CoinJoin 的一般資訊，我在這篇文章中會一一說明：[link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).


### 使用 Whirlpool 統計工具。


使用 Whirlpool 執行 CoinJoins 後，您可能想知道混合 UTXOs 的實際隱私程度。Whirlpool 統計工具可讓您輕鬆完成此工作。使用此工具，您可以計算混合 UTXOs 的前瞻性得分和後瞻性得分。若要瞭解更多關於計算這些 Anon Sets 及其運作方式的資訊，我建議您閱讀這一部分：[link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).


該工具已預先安裝在您的 RoninDojo 上。目前，它只能從 RoninCLI 使用。若要從主功能表啟動，請前往：

**三浦里工具包 > Whirlpool 統計工具**


使用說明將會出現。完成後，按任意鍵進入命令列：


![Whirlpool Stats Tool software home](assets/28.webp)


終端機將顯示：

**wst#/tmp>**


若要離開 Interface 並返回 RoninCLI 功能表，只需輸入指令即可：

```
quit
```


首先，我們將在 Tor 上設定代理，以便在完全隱私的情況下擷取 OXT 資料。輸入指令：

```
socks5 127.0.0.1:9050
```


然後從包含您的交易的資料池中下載資料：

```
download 0001
```


**註：** 將 `0001` 改為您感興趣的池面值代碼。


WST 上的面額代碼如下：



- Pool 0.5 bitcoins: 05
- 池 0.05 比特幣: 005
- 池 0.01 比特幣: 001
- Pool 0.001 bitcoins: 0001


![Downloading data from pool 0001 from OXT](assets/29.webp)


下載資料後，使用指令載入：

```
load 0001
```


**註：** 將 `0001` 改為您感興趣的池面值代碼。


![Loading data from pool 0001](assets/30.webp)

讓載入過程進行，可能需要幾分鐘。載入資料後，輸入 score 指令，然後輸入您的 txid（交易識別碼），以取得其 Anon Sets：

```
score TXID
```


**Note:** 將 `txid` 改為您的交易識別碼。


![Printing the prospective and retrospective scores of the given TXID](assets/31.webp)


WST 接著會顯示回溯分數 (Backward-looking metrics) ，接著會顯示前瞻分數 (Forward-looking metrics)。除了 Anon Set 的分數之外，WST 還會根據 Anon Set 提供您的輸出在池中的擴散率。


請注意，您的 UTXO 的前瞻性分數是根據您初始組合的 txid 計算，而不是根據您最後一次組合的 txid 計算。相反，UTXO 的回溯分數是根據上一個週期的 txid 來計算的。


再次重申，如果您不瞭解 Anon Sets 的這些概念，我建議您閱讀我在 CoinJoin 文章中的這一部分，在這部分中我用圖表詳細解釋了一切：[https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)


### 使用 Boltzmann 計算機。


Boltzmann 計算器是一種工具，可讓您輕鬆計算 Bitcoin 交易的各種進階指標，包括其熵值。所有這些資料可讓您量化交易的隱私等級，並偵測任何潛在錯誤。此工具已預先安裝在您的 RoninDojo 節點上。


若要從 RoninCLI 存取，請透過 SSH 連線，然後進入選單：

**Samourai Toolkit > Boltzmann 計算機**


在解釋如何在 RoninDojo 上使用之前，我會先解釋這些指標所代表的意義、計算方式以及用途。


這些指標可用於任何 Bitcoin 交易，但對於研究 CoinJoin 交易的品質尤其有趣。


1.本軟體計算的第一個指標是可能的組合數。它在計算機上註明為 "nb combinations"。根據 UTXOs 的值，這個指標代表從輸入到輸出的可能映射數量。


**註：** 如果您不熟悉「UTXO」一詞，我建議您閱讀這篇短文：


> Bitcoin 交易的機制：UTXO、輸入和輸出。

換句話說，此指標代表特定交易的可能詮釋數量。例如，一個 Whirlpool 5x5 CoinJoin 結構的可能組合數等於 1496：


![Schema of a Coinjoin transaction on kycp.org](assets/32.webp)


資料來源：KYCP


2.第二個計算指標是交易的熵。由於交易的可能組合數可能非常多，因此可以選擇使用熵來代替。熵表示可能組合數的二進位對數。其計算公式如下



- E： 交易的熵。
- C：交易的可能組合數。


**E = log2(C)**


在數學中，二進位對數 (以 2 為底) 是 2 的幂函數的逆函數。換句話說，x 的二進位對數是為了得到 x 值而必須將數 2 提升到的幂。


因此：


**E = log2(C)**


**C = 2^E**


此指標以位元表示。例如，以下是 Whirlpool 5x5 CoinJoin 交易的熵的計算，前面提到的可能組合數等於 1496：


**C = 1496**


**E = log2(1496)**


**E = 10.5469 位元**


因此，這筆 CoinJoin 交易的熵值為 10.5469 位元，非常好。


此指標越高，表示對交易的不同詮釋越多，因此交易的機密性也越高。


讓我們再舉一個例子。下面是一個有一個輸入和兩個輸出的 「經典 」交易：


![Bitcoin transaction schema on oxt.me](assets/34.webp)


信用：OXT


這項交易只有一種可能的解釋：


**[(inp 0) > (Outp 0 ; Outp 1)]**


所以它的熵會等於 0：


**C = 1**,

**E = log2(C)**、

**E = 0**


3.Boltzmann 計算器返回的第三個指標是 Tx 的效率，稱為「Wallet 效率」。此指標可將輸入的交易與相同配置下的最佳交易進行比較。


現在我們將介紹最大熵的概念，它代表特定交易結構可達到的最高熵。例如，一個 Whirlpool 5x5 CoinJoin 結構的最大熵為 10.5469。效率指標將此最大熵與輸入交易的實際熵進行比較。其計算公式如下



- ER：以位元表示的實際熵。
- EM：以位元表示相同結構的最大熵。
- Ef：以位元表示的效率。


**Ef = ER - EM**


**Ef = 10.5469 - 10.5469**


**Ef = 0 位元**


此指標也以百分比表示，因此公式變成：



- CR：可能組合的實際數量。
- CM：結構相同的最大可能組合數。
- Ef：以百分比表示的效率。


**Ef = CR/CM**


**Ef = 1496/1496**


**Ef = 100%**


效率為 100% 表示此交易相對於其結構而言，具有最高的隱私性。


4.第四個計算指標是熵密度。它讓我們可以將熵與每個輸入或輸出相關聯。此指標可用於比較不同規模的交易之間的效率。


其計算方法非常簡單：將交易的熵除以輸入和輸出的數量。例如，對於一個 Whirlpool 5x5 CoinJoin，我們會有：


ED：以位元表示的熵密度。

E： 交易熵，以位元表示。

T： 交易中輸入和輸出的總數。


T = 5 + 5 = 10

ED = E / T

ED = 10.5469 / 10

ED = 1.054 位元


Boltzmann 計算器提供的第五項資訊是輸入和輸出之間連結的概率表。這個表格簡單地提供了特定輸入對應特定輸出的概率（玻爾兹曼分數）。


如果我們以 Whirlpool CoinJoin 為例，概率表會是這樣：


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


在這裡，我們可以看到每個輸入與每個輸出連結的機率相等。


但是，如果我們以有一個輸入和兩個輸出的交易為例，它會是這樣的：


| Input | Output 0 | Output 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

在這個範例中，我們可以看到每個輸出來自輸入 0 的概率是 100%。


此機率越低，機密性就越高。


6.計算的第六項資訊是確定性連結的數量。還會提供確定性連結的比率。這個指標會強調特定交易的輸入和輸出之間的連結數量，這些連結的機率為 100%，也就是說它們是不可否認的。


比率表示交易中確定性連結的數量與連結總數的比較。


例如，CoinJoin Whirlpool 交易的輸入和輸出之間沒有確定的連結。指標將為零，比率也將為 0%。


但是，對於所研究的第二筆交易（1 筆輸入和 2 筆輸出），指標是 2，比率是 100%。


因此，如果此指標為零，則表示保密性良好。


現在我們已經研究了這些指標，讓我們看看如何使用此軟體計算它們。從 RoninCLI，進入功能表：

**Samourai Toolkit > Boltzmann 計算機**


![Boltzmann Calculator software homepage](assets/35.webp)


軟體啟動後，輸入您要研究的 transaction ID。您可以一次輸入多筆交易，方法是用逗號分隔，然後按 Enter：


![Enter a TXID to study on Boltzmann Calculator](assets/36.webp)


然後，計算機將返回我們之前看到的所有指標：


![Printing of Boltzmann Calculator data for this TXID](assets/37.webp)


鍵入命令 "Quit" 離開軟體，回到 RoninCLI 功能表。


若要進一步瞭解 Boltzmann 計算器，我建議您閱讀這些文章：



- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159



- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf


### 連接 Bisq。


Bisq 是一個點對點的 Exchange 平台，可讓您買賣比特幣。它與在 Tor 上執行的桌面軟體搭配使用，讓您無需提供身份即可 Exchange 比特幣。

Bisq 透過 2/2 多重簽章系統保障點對點交換的安全。您可以將此軟體與您自己的 RoninDojo 節點一起使用，以最佳化您交換的隱私，並信任您自己節點的 Blockchain 所提供的資料。


若要下載 Bisq 軟體，請至其官方網站：https://bisq.network/。


若要開始使用軟體，建議閱讀此頁： https://bisq.network/getting-started/


要從您的 RoninDojo 擷取連線連結，您需要透過 SSH 連線至 RoninCLI。然後前往功能表：

**應用程式 > 管理應用程式**


輸入密碼，然後用空格鍵勾選方塊：

**[ ] 啟用 Bisq 連線**


確認您的選擇。讓您的節點安裝，然後從以下網址擷取 Tor V3 Address：

**Credentials > bitcoind**


複製「Bitcoin daemon」下的 Address。


您也可以從 RoninUI Interface 擷取您的 bitcoind Tor V3 Address，只要點選「儀表板」上「Bitcoin Core」方格中的「Manage」即可：


![Retrieve TorV3 Bitcoin Daemon address on RoninUI](assets/38.webp)


若要從 Bisq 連接您的節點，請移至功能表：

**設定 > 網路資訊**


![Access the node connection interface from the Bisq software](assets/39.webp)


按一下「使用自訂 Bitcoin 核心節點」的氣泡。然後在指定的方塊中輸入您的 Bitcoin TorV3 Address，帶有".onion「，但不帶 」http://"。


![Box to enter the TorV3 address of your node in the Bisq software](assets/40.webp)


重新啟動 Bisq 軟體。您的節點現在已連接至 Bisq。


### 其他功能。


您的 RoninDojo 節點還包括其他基本功能。您有能力掃描特定資訊，以確保將其納入考量。


例如，有時您的 Wallet 連接到您的 RoninDojo 可能找不到屬於您的比特幣。儘管您確定在這個 Wallet 中擁有 Bitcoin，但餘額還是 0。有很多可能的原因需要考慮，包括衍生路徑中的錯誤，其中也有可能是您的節點沒有觀察到您的地址。


要解決這個問題，您可以使用「xpub 工具」檢查您的節點是否正在追蹤您的 xpub。要從 RoninUI 存取，請前往功能表：

**維護 > XPUB 工具**


輸入有問題的 xpub，然後按一下「檢查」以驗證此資訊。


![XPUB Tool from RoninUI](assets/41.webp)


如果您的 xpub 被節點追蹤，您會看到這個出現：


![XPUB Tool result showing successful analysis](assets/42.webp)


檢查所有交易是否正確顯示。此外，驗證衍生類型是否與您的 Wallet 匹配。在這裡，我們可以看到節點將此 xpub 視為 BIP44 派生。如果此衍生類型與您的 Wallet 不匹配，請按一下「Retype」按鈕，然後根據您的選擇選擇 BIP44/BIP49/BIP84：


![Change the derivation type of the studied xpub from RoninUI](assets/43.webp)


如果您的 xpub 沒有被節點追蹤，您會看到這個畫面邀請您匯入：


![Import an xpub with XPUB Tool on RoninUI](assets/44.webp)


您也可以使用其他維護工具：



- 交易工具：可讓您觀察特定交易的詳細資訊。
- Address 工具：可讓您確認特定的 Address 是否被您的 Dojo 追蹤。
- 重新掃描區塊：強制您的節點重新掃描選取的區塊範圍。


您還可以在 RoninUI 上找到 "Push Tx "工具。它允許您向 Bitcoin 網路廣播已簽署的交易。它必須以十六進位格式輸入：


![Tool for broadcasting a signed transaction from RoninUI](assets/45.webp)


## 結論：


我們已經看過如何安裝和開始使用 RoninDojo 這個很棒的工具。它是運行您自己的 Bitcoin 節點的絕佳選擇。它是一個穩定的解決方案，整合了所有比特幣玩家必備的工具，並保持更新。


如果使用終端機不會讓您害怕，而且您不需要與 Lightning Network 相關的工具，那麼 RoninDojo 可能會吸引您。


如果可以，請考慮捐贈給為您免費製作這些開放源碼軟體的開發者： https://donate.ronindojo.io/


若要進一步瞭解 RoninDojo，我建議您查看以下外部資源中的連結。


### 進一步閱讀：



- 了解並使用 Bitcoin 上的 CoinJoin。
- Hash 功能 - 節錄自電子書 Bitcoin Démocratisé 1.
- 有關 Bitcoin passphrase 的一切資訊。


### 外部資源：



- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/