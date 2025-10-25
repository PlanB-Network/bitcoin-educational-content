---
name: RoninDojo v2
description: 在 Raspberry Pi 上安裝 RoninDojo v2 Bitcoin 節點
---
![cover RoninDojo v2](assets/cover.webp)


**警告:** 在 Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被扣押之後，RoninDojo 的某些功能（例如 Whirlpool）已不再運作。不過，這些工具有可能在未來幾週內以不同方式恢復或重新啟動。此外，由於 RoninDojo 的程式碼託管在 Samourai 的 GitLab 上，而 GitLab 也被查封，因此目前無法從遠端下載程式碼。RoninDojo 團隊可能正在努力重新發布程式碼。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

> 使用 Bitcoin 時要注意隱私。

在之前的教學中，我們已經介紹了安裝和使用 RoninDojo v1 的步驟。然而，在過去的一年中，RoninDojo 團隊推出了他們的實作版本 2，這標誌著該軟體架構的一個重要轉折點。事實上，他們捨棄了 Linux Manjaro 發行版，改用 Debian。因此，他們不再提供在 Raspberry Pi 上自動安裝的預先設定映像檔。但仍有一種手動安裝的方法。我就是用這個方法來安裝我自己的節點，從那時起，RoninDojo v2 在我的 Raspberry Pi 4 上運作得非常好。因此，我現在提供一個新的教學，說明如何在 Raspberry Pi 上手動安裝 RoninDojo v2。

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0

## 目錄：


- RoninDojo 是什麼？
- 安裝 RoninDojo v2 應該選擇何種硬體？
- 如何組裝 Raspberry Pi 4？
- 如何在 Raspberry Pi 4 上安裝 RoninDojo v2？
- 如何使用您的 RoninDojo v2 節點？


## RoninDojo 是什麼？

Dojo 最初是完整的 Bitcoin 節點實作，以 Bitcoin Core 為基礎，由 Samourai Wallet 團隊開發。此解決方案可安裝在任何設備上。與其他 Core 實作不同，Dojo 經過特別優化，可與 Samourai Wallet 的 Android 應用環境整合。至於 RoninDojo，它是專為方便安裝和管理 Dojo 以及其他各種輔助工具而設計的實用程式。簡而言之，RoninDojo 在簡化安裝與管理的同時，整合了許多其他工具，豐富了 Dojo 的基本實作。


Ronin 也提供 [一個稱為 "*Tanto*" 的 node-in-box 解決方案](https://ronindojo.io/en/products)，這個裝置已經在其團隊組裝的系統上安裝了 RoninDojo。Tanto 是一種付費選項，對於那些希望避免技術複雜性的人來說可能會很有趣。但由於 RoninDojo 的原始碼是開放的，因此也可以將它部署在您自己的硬體上。這個選擇更經濟，但需要一些額外的操作，我們將在本教學中介紹。

RoninDojo 是一個 Dojo，因此它可以輕鬆地將 Whirlpool CLI 整合到您的 Bitcoin 節點中，以提供最佳的 CoinJoin 體驗。有了 Whirlpool CLI，您就可以每天 24 小時、每週 7 天不間斷地重新混合您的比特幣，而無需您的個人電腦保持開機狀態。


除了 Whirlpool CLI 之外，RoninDojo 還包含各種工具來增強您的 Dojo 功能。其中，Boltzmann 計算器可分析您交易的隱私等級，Electrum 伺服器可讓您的 Bitcoin 錢包與您的節點連線，而 Mempool 伺服器可讓您在本機檢視您的交易，而不會洩漏資訊。


與 Umbrel 等其他節點解決方案相比，RoninDojo 明顯專注於 On-Chain 解決方案和隱私權工具。與 Umbrel 不同，RoninDojo 不支援建立 Lightning 節點，也不支援整合更多通用伺服器應用程式。雖然 RoninDojo 提供的多功能工具比 Umbrel 少，但它擁有管理 On-Chain 活動的所有基本功能。


如果您不需要 Umbrel 提供的通用功能或與 Lightning Network 相關的功能，而且您正在尋找一個簡單、穩定且具備 Whirlpool 或 Mempool 等基本工具的節點，RoninDojo 可能是理想的解決方案。Umbrel 趨向於成為一個迷你多工作業伺服器，以 Lightning Network 和多功能為導向，而 RoninDojo 則與 Samourai Wallet 的理念一致，著重於使用者隱私的基本工具。


現在我們已經概述了 RoninDojo，讓我們一起看看如何設定這個節點。


## 安裝 RoninDojo v2 應選擇何種硬體？

RoninDojo 提供了在 [RockPro64](https://ronindojo.io/en/download) 上自動安裝其軟體的映像。但是，我們的教程著重於在 Raspberry Pi 4 上的手動安裝步驟。雖然最近推出了 Raspberry Pi 5，理論上本教學應該與這款新機型相容，但我還沒有機會親自測試，也沒有發現來自社區的任何回饋。一旦我購買到 Pi 5 和相容的元件，我就會更新本教學，讓您了解最新情況。在此期間，我建議優先使用 Pi 4，因為它在我的節點上運作得非常好。

就我而言，我在配備 8 GB 記憶體的 Raspberry Pi 上執行 RoninDojo。雖然有些社群成員已成功讓它在只有 4 GB 記憶體的裝置上運作，但我自己還沒有測試過這種配置。由於價格相差不大，選擇 8 GB RAM 版本似乎是明智之舉。如果您打算將您的 Raspberry Pi 改作其他用途，這也會很有用。

值得注意的是，RoninDojo 團隊經常報告與機殼和 SSD 轉接器相關的問題。我自己也面臨這些問題。 **因此，強烈建議避免使用為您節點的 SSD 配備 USB 纜線的機殼。**反之，請選擇專為您的 Raspberry Pi 設計的儲存擴充卡：


![storage expansion card RPI4](assets/notext/1.webp)


若要儲存 Bitcoin Blockchain，您需要與您所選擇的儲存擴充卡相容的固態硬碟。目前（2024 年 2 月），我們正處於過渡階段。預計再過幾個月，1 TB 的磁碟將不再足以容納 Blockchain 不斷成長的大小，尤其是考慮到您計畫整合到節點中的各種應用程式。因此，有些人建議投資 2 TB SSD，以便長期安心使用。然而，隨著 SSD 價格逐年下降的趨勢，有些人則建議選擇 1 TB 的硬碟，這樣的硬碟應該足夠使用一到兩年，他們認為等到硬碟過時時，2 TB 機型的成本很可能已經下降。因此，選擇取決於您的個人喜好。如果您打算將RoninDojo使用一段相當長的時間，並且希望避免在未來幾年內發生任何技術上的問題，那麼選擇2 TB的SSD似乎是最謹慎的做法，因為它能提供您一個舒適的未來空間。


此外，您還需要各種小型元件：


- 配備風扇的機殼，可放置 Raspberry Pi 和儲存擴充卡。包括 SSD 擴充卡和相容外殼的套件可在網上購買；
- Raspberry Pi 的電源線；
- 一張至少 16 GB 的 micro SD 卡（雖然 8 GB 在技術上已經足夠，但 8 GB 和 16 GB 卡之間的價格差異通常微不足道）；
- 用於網路連接的 RJ45 乙太網路線。


![node material](assets/notext/2.webp)


## 如何組裝 Raspberry Pi 4？

節點的組裝會因所選擇的硬體，特別是外殼類型而有所不同。不過，在組裝時，要遵循的一般步驟大綱大致上仍是相似的。

先將 SSD 安裝在儲存擴充卡上，並小心鎖緊背面的兩顆鎖緊螺絲。


![assembly1](assets/notext/3.webp)


然後將 Raspberry Pi 連接到擴充卡上。


![assembly2](assets/notext/4.webp)


此外，將風扇連接至 Raspberry Pi。


![assembly3](assets/notext/5.webp)


連接各種元件，注意使用正確的針腳，並參閱您的機殼手冊。機殼製造商通常會提供影片教學，協助您組裝。在我的案例中，我有一張配備開關按鈕的額外擴充卡。這不是製作 Bitcoin 節點的必要條件。我主要使用它來提供電源按鈕。


如果您和我一樣，擁有配備開關按鈕的擴充卡，請不要忘記安裝小型的「自動開機」跳線。這將允許您的節點在電源開啟後立即自動啟動。這項功能在停電時特別有用，因為它可以讓您的節點自行重新啟動，而不需要您手動介入。


![assembly4](assets/notext/6.webp)


在將所有硬體插入機殼之前，請務必先將 Raspberry Pi、儲存擴充卡和風扇通電，檢查它們是否正常運作。


![assembly5](assets/notext/7.webp)


最後，將 Raspberry Pi 安裝在機殼中。請注意，稍後的步驟需要將 micro SD 卡插入 Raspberry Pi 的適當連接埠。如果您的機殼上有開口，讓您無需打開機殼即可插入 SD 卡 (如照片中我的機殼)，您現在就可以關上機殼。但是，如果您的機殼沒有直接連接 micro SD 連接埠，您就需要等到準備好 micro SD 卡插入後再完成組裝。


![assembly6](assets/notext/8.webp)


## 如何在 Raspberry Pi 4 上安裝 RoninDojo v2？


### 步驟 1：準備可開機 micro SD

組裝好硬體後，下一步就是安裝 RoninDojo。為此，我們將從您的電腦準備一張可開機的 micro SD 卡，將適當的磁碟映像燒錄到該卡上。

您需要使用 _**Raspberry Pi Imager**_ 軟體，此軟體的設計是為了方便下載、設定和寫入作業系統到 micro SD 卡上，以便與 Raspberry Pi 搭配使用。首先在您的個人電腦上安裝此軟體：


- 適用於 Ubuntu/Debian: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- 適用於 Windows： https://downloads.raspberrypi.org/imager/imager_latest.exe
- 適用於 Mac： https://downloads.raspberrypi.org/imager/imager_latest.dmg


軟體安裝完成後，打開軟體，將 micro SD 卡插入個人電腦。從 Raspberry Pi Imager Interface，選擇 `CHOOSE OS`：


![choose OS](assets/notext/9.webp)


接下來，進入「Raspberry Pi OS (其他)」功能表：


![choose OS others](assets/notext/10.webp)


選擇名為 `Raspberry Pi OS (Legacy, 64-bit) Lite` 的作業系統，其大小為 `0.3GB`：


![choose OS Legacy Lite](assets/notext/11.webp)


選擇作業系統後，您會被重新導向到 Raspberry Pi Imager 的主選單。按一下「選擇儲存空間」：


![choose storage](assets/notext/12.webp)


選擇您的 micro SD 卡：


![choose micro sd](assets/notext/13.webp)


選擇作業系統及 micro SD 卡後，按一下「下一步」：


![choose next](assets/notext/14.webp)


將會出現一個新視窗。選擇「編輯設定」：


![edit settings](assets/notext/15.webp)


在此視窗中，移至 `GENERAL` 標籤，並進行下列設定 (這些設定對於它的運作非常重要)：


- 啟用該選項，並指定 `RoninDojo` 為主機名稱；
- 啟用「設定使用者名稱和密碼」，輸入 `pi` 作為使用者名稱，選擇密碼，並記下這些資訊，因為以後還需要用到。這些憑證是臨時的，之後會被刪除；
- 停用「設定 Wi-Fi」；
- 啟用 `Set locale settings` 並選擇您的時區以及與您電腦相對應的鍵盤類型；


![general settings](assets/notext/16.webp)


在「服務」索引標籤中，按一下「啟用 SSH」方塊，然後選擇「使用密碼驗證」：


![services settings](assets/notext/17.webp)


此外，請確保在 `OPTIONS` 標籤中，已停用遠距偵測：


![options settings](assets/notext/18.webp)


按一下「儲存」：


![settings save](assets/notext/19.webp)

按一下「是」以確認，開始建立可開機的 micro SD 卡：

![settings yes](assets/notext/20.webp)


會有一則訊息通知您，micro SD 卡上的所有資料將被刪除。按一下「是」以確認開始處理：


![overwrite micro SD](assets/notext/21.webp)


等待軟體完成 micro SD 卡的準備：


![writing micro SD](assets/notext/22.webp)


當顯示程序結束的訊息出現時，您可以從電腦移除 micro SD 卡：


![writing micro SD completed](assets/notext/23.webp)


### 步驟 2：完成節點組裝

現在您可以將 micro SD 卡插入 Raspberry Pi 的適當連接埠。


![micro SD](assets/notext/24.webp)


然後使用乙太網路線將 Raspberry Pi 連接到路由器。最後，連接電源線並按下電源按鈕 (如果您的設定包含電源按鈕)，即可開啟您的節點。


### 步驟 3：與節點建立 SSH 連線

首先，必須找到您節點的 IP Address。您可以選擇使用 _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ 或 _[Angry IP Scanner](https://angryip.org/)_ 等工具，或檢查路由器的管理 Interface。IP Address 的格式應該是 `192.168.1.??`。 **對於下列所有指令，請將 `[IP]` 換成您節點的實際 IP Address，** (移除括號)。


啟動終端機。


若要移除已與節點 IP Address 相關聯的可能金鑰，請執行指令：

`ssh-keygen -R [IP]`。


此指令之後的錯誤並不嚴重，它只是表示該 key 不存在於您的已知主機清單中 (這很有可能)。例如，如果您節點的 IP 是 `192.168.1.40`，命令就變成了：`ssh-keygen -R 192.168.1.40`。


接下來，執行指令與您的節點建立 SSH 連線：

`ssh pi@[IP]`。

將會出現一則關於主機真實性的訊息： `The authenticity of host '[IP]' can't be established.` 這表示由於缺乏已知的公開金鑰，您嘗試連線的裝置的真實性無法驗證。第一次透過 SSH 連線到新主機時，總是會出現此訊息。您必須回應 `yes` 以將其公開金鑰新增到您的本機目錄，如此一來，日後 SSH 連線到此節點時，就不會再出現此警告訊息。因此，請輸入 `yes` 並按下 `enter` 以驗證。

接下來會要求您輸入密碼，也就是之前在步驟 1 中設定為臨時的密碼。用 `enter` 驗證。接著您就可以透過 SSH 連線到您的節點。


總而言之，以下是要執行的指令：


- `ssh-keygen -R [IP]``
- `ssh pi@[IP]`
- 是
- 輸入臨時密碼並驗證。


### 步驟 4：更新與準備

現在您已透過 SSH 連線至節點。在您的終端機上，命令提示應該是pi@RoninDojo:~$`。開始時，請使用下列指令更新可用套件清單，並為現有套件安裝更新：

`sudo apt update && sudo apt upgrade -y``


更新完成後，繼續使用指令安裝 *Git* 和 *Dialog*：

`sudo apt install git dialog -y`


接下來，執行以下步驟克隆 _RoninOS_ Git 套件庫的「master」分支：

`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS``


使用指令執行指令碼 `customize-image.sh`：

`cd /opt/RoninOS/ && sudo ./customize-image.sh``


**重要的是讓腳本不中斷地執行，並耐心等待其程序**結束，大約需要 10 分鐘。當「設定完成」訊息出現時，您就可以進入下一步。


### 步驟 5：啟動 RoninOS

使用命令啟動 RoninOS：

`sudo systemctl start ronin-setup` 啟動。


使用命令顯示日誌檔案的行數：

`tail -f /home/ronindojo/.logs/setup.logs`.


在此階段，**重要的是讓 RoninOS 啟動，並等待它**完成執行。這需要大約 40 分鐘。當出現`所有 RoninDojo 功能安裝完成！`時，您可以繼續到步驟 6。


### 步驟 6：存取 RoninUI 並變更憑證

完成安裝後，若要透過瀏覽器連線到您的節點，請確保您的個人電腦與您的節點連線到相同的區域網路。如果您的個人電腦正在使用 VPN，請暫時關閉 VPN。若要在瀏覽器中存取節點 Interface，請在 URL 列中輸入：


- 直接輸入您節點的 IP Address，例如 `192.168.1.??`；
- 或者，輸入 `ronindojo.local`。


進入 RoninUI 首頁後，系統會提示您開始安裝。为此，请单击 「开始 」按钮。


![lets start](assets/notext/25.webp)


在此階段，RoninUI 向您提供您的 `root` 密碼。必須妥善保管。您可以選擇在紙張上進行實體備份，或將其保存在 [密碼管理器](https://planb.network/courses/99c46148-7080-4915-a7e0-9df0e145cd47/0b3c69b2-522c-56c8-9fb8-1562bd55930f)。


![root password](assets/notext/26.webp)


儲存「root」密碼後，勾選「我已備份 Root 使用者憑證」方塊，然後按一下「繼續」繼續。


![confirm root password](assets/notext/27.webp)


下一步涉及创建用户密码，该密码将用于访问 RoninUI Web Interface 和与您的节点建立 SSH 会话。選擇一個強大的密碼，並確保將其安全保存。在单击 "Finish"（完成）验证之前，您需要输入该密码两次。至於使用者名稱，建議保留預設選項 `ronindojo`。如果您決定更改，請記住相應調整以下步驟中的命令。


![user credentials](assets/notext/28.webp)


完成這些動作後，請等待您的節點初始化。然後，您將存取 RoninUI Web Interface。您幾乎已經完成整個過程，只剩下幾個小步驟！

![Ronin UI](assets/notext/29.webp)


### 步驟 7：移除臨時憑證

在您的個人電腦上開啟新的終端，並使用下列指令與您的節點建立 SSH 連線：

`SSH ronindojo@[IP]`


例如，如果您節點的 IP Address 是 `192.168.1.40`，則適當的指令將會是：

`SSH ronindojo@192.168.1.40`


如果您在上一步中變更了使用者名稱，用另一個使用者名稱取代預設使用者名稱 (`ronindojo`)，請務必在指令中使用這個新名稱。例如，如果您選擇 `planb` 作為使用者名稱，且 IP Address 為 `192.168.1.40`，則輸入的指令將會是：

`SSH planb@192.168.1.40`

您會被要求輸入使用者密碼。輸入後按 `enter` 鍵確認。然後，您將存取 RoninCLI Interface。使用鍵盤上的方向鍵導航到 `Exit RoninDojo` 選項，然後按下`enter`以選取。

![RoninCLI](assets/notext/30.webp)


此時，您已進入節點的終端機，出現類似以下的指令提示：`ronindojo@RoninDojo:~$`。若要移除在設定可開機 micro SD 卡時建立的臨時使用者，請輸入下列指令並按下 `enter`：

`sudo deluser --remove-home pi`


系統會提示您確認使用者密碼。輸入密碼，然後按 `enter` 鍵確認。等待操作完成，然後使用 `exit` 指令離開終端機。


恭喜您！您的 RoninDojo v2 節點現在已設定完成，可以開始使用。它將開始其 IBD（*初始區塊下載*），繼續從 Genesis 區塊下載和驗證 Bitcoin Blockchain。此步驟涉及檢索 2009 年 1 月 3 日以來的所有 Bitcoin 交易，需要一些時間。一旦 Blockchain 完全下載完成，索引器將繼續壓縮資料庫。IBD 的持續時間會有很大差異。此程序完成後，您的 RoninDojo 節點將完全運作。


**如果您使用本教學從舊版 RoninDojo v1 節點**遷移到新版，同時保留相同的 SSD，您的節點應該會自動偵測並重複使用磁碟上的現有資料，讓您不必再次執行 IBD。在這種情況下，您只需等待節點重新同步最新的區塊。


### 步驟 8：「veth 修正」

如果您在 Raspberry Pi 上使用 RoninDojo v2 時遇到 bug，即在順利安裝之後，您的節點突然無法透過 SSH 連線，但在簡單重新啟動之後又恢復正常，那麼您需要遵循此步驟 8。這個常見的 bug 可以使用社群開發的解決方案："_veth fix_"輕鬆修復。這個小修正可以永久解決突然斷線的問題。以下是應用方法。


在您的個人電腦上開啟新的終端，並使用下列指令與您的節點建立 SSH 連線：

`SSH ronindojo@[IP]`


舉例來說，如果您的節點 IP Address 是 `192.168.1.40`，適當的指令應該是：

`SSH ronindojo@192.168.1.40`


系統會提示您輸入使用者密碼。輸入後按 `enter` 鍵確認。然後，您將存取 RoninCLI Interface。使用鍵盤的箭頭瀏覽到 `Exit RoninDojo` 選項，然後按下`enter`以選取。


此時，您已進入節點的終端機，出現類似以下的指令提示：`ronindojo@RoninDojo:~$`。若要套用 **veth** 修正，請鍵入下列指令，然後按 `enter`：

`sudo nano /etc/dhcpcd.conf``


再次確認您的密碼，然後按下 `enter`。


您會看到 `dhcpcd.conf` 檔案。您需要複製下列文字，確保包含星號，並將其加入檔案底部：

拒絕介面 veth*`


若要執行此動作，請使用鍵盤上的向下箭頭移至檔案底部，然後按一下滑鼠右鍵，將文字貼到獨立的一行上。


新增文字後，按下 `ctrl X` 開始退出，接著按下 `ctrl Y` 確認儲存變更，然後按下 `enter` 完成並返回指令提示。為確保修改已正確套用，請使用適當的指令重新開啟 `dhcpcd.conf` 檔案。


若要完成修復程式的應用，請執行下列步驟重新啟動您的節點：

`sudo reboot now` (重新啟動)


此時，您可以關閉終端機。等待 RoninDojo 重新啟動所需的時間，之後您應該可以透過瀏覽器的圖形 Interface 重新連線。這個過程應該可以解決遇到的錯誤。


## 如何使用您的 RoninDojo v2 節點？


### 將您的 Wallet 軟體連接到 Electrs

您新安裝和同步的節點的第一個用途是向 Bitcoin 網路廣播您的交易。您可能會想要將您的各種錢包連接到您的節點，以便保密地廣播您的交易。您可以透過 Electrum Rust 伺服器 (electrs) 來進行。此應用程式通常已預先安裝在您的 RoninDojo 節點上。如果沒有，您可以透過 RoninCLI Interface 在`應用程式 > 管理應用程式 > 安裝 Electrum 伺服器`中手動安裝。


若要取得 Electrum 伺服器的 Tor Address，請從 RoninUI 網頁 Interface，前往：

配對 > Electrum 伺服器 > 立即配對

![Pairing](assets/notext/31.webp)

![Electrs](assets/notext/32.webp)

然後，您需要在 Wallet 軟體中輸入以 `.onion` 結尾的 `Hostname` Address，並附上連接埠 `50001`。![hostname](assets/notext/33.webp)

例如，在 Sparrow Wallet 上，只要移至標籤即可：

檔案 > 偏好設定 > 伺服器 > 私人電子琴


![Sparrow](assets/notext/34.webp)


### 連接 Wallet 軟體至 Samourai Dojo

作為使用 Electrs 的替代方案，Dojo 允許您直接將兼容的 Software Wallet 連接到 RoninDojo 節點。Samourai Wallet 和 Sentinel 等錢包提供此功能。


要建立連接，您只需掃描 Dojo 的 QR 代碼。要通過 RoninUI 存取此 QR 碼，請導航至：

配對 > Samourai 道場 > 現在配對

![Samourai Dojo](assets/notext/35.webp)

要將您的 Samourai Wallet 連接到您的 Dojo，只需在安裝應用程式時掃描此 QR 代碼即可：


![Samourai Wallet connection](assets/notext/36.webp)


如果您在設定Ronin Dojo之前已經擁有Samourai Wallet，在還原您的Wallet之前，必須先備份您的Wallet，卸載後再重新安裝Samourai Wallet應用程式。啟動重新安裝的應用程式後，您將可選擇連線至新的道場。 **請小心，如果執行不正確，此過程會有損失您的 bitcoins 的風險！** 請確認您的檔案中有 Samourai Wallet 的備份，並透過 `設定 > 疑難排解 > passphrase` 驗證您的 passphrase 的有效性。備份您的復原短語和 passphrase 的可讀性也很重要。若要更精確地進行此操作，建議遵循此詳細教學：[https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).


### 使用自己的 Mempool.空間 Block explorer

Block explorer 將來自 Bitcoin Blockchain 的原始資訊轉換成結構化、易讀的格式。透過 *Mempool.space* 等工具，可以分析交易、搜尋特定位址，甚至即時查詢網路 mempool 的平均費率。


然而，使用線上區塊探索者會對您的隱私造成風險，並涉及對第三方所提供資料的信任。事實上，不經過自己的節點而使用這些服務，您可能會在不經意間洩露您的交易資訊，而且必須仰賴網站擁有者所提供資訊的準確性。

為了降低這些風險，建議您透過 Tor 網路使用自己的 *Mempool.space* 實體，直接託管在您的節點上。此解決方案可確保您的隱私權及資料的自主性。

為此，請先從 RoninUI 安裝 *Mempool Space Visualizer*。在網頁 Interface 上，移至「儀表板」標籤，然後按一下「Mempool Space」下方的「管理」：

儀表板 > Mempool 空間 > 管理

![Manage mempool](assets/notext/37.webp)

然後按一下「安裝 Mempool Visualizer」按鈕：

![install mempool](assets/notext/38.webp)

確認您的使用者密碼：

![password mempool](assets/notext/39.webp)

等待安裝完成，然後再按一下「管理」按鈕：

![Mempool Manage](assets/notext/40.webp)

您將獲得一個 `.onion` 連結，以透過 Tor 網路存取您自己的 *Mempool.space* 實例。

![Mempool link](assets/notext/41.webp)

我建議您將此連結儲存於 Tor 瀏覽器的我的最愛，或將其加入智慧型手機上的 Tor 瀏覽器應用程式，以便隨時隨地輕鬆安全地存取。如果您還沒有 Tor 瀏覽器，可以在這裡下載：[https://www.torproject.org/download/](https://www.torproject.org/download/)

![Mempool Tor](assets/notext/42.webp)


### 使用 Whirlpool 混合您的比特幣

您的 RoninDojo 節點也整合了 _WhirlpoolCLI_ 和 _WhirlpoolGUI_，前者是命令列 Interface，可讓 Whirlpool 錢幣接合自動化；後者則是圖形化 Interface，旨在與 _WhirlpoolCLI_ 互動。


透過 Whirlpool 執行 CoinJoin 時，所使用的應用程式必須處於啟動狀態才能執行混音。這個條件對於希望達到高層級不混音的人來說可能會造成限制。事實上，託管整合 Whirlpool 應用程式的裝置必須持續開啟。這表示若要一天 24 小時參與混音，您的電腦或智慧型手機必須持續開啟 Samourai 或 Sparrow。解決這個限制的方法是在一直開啟的機器上使用 _WhirlpoolCLI_，例如 Bitcoin 節點，讓您的硬幣可以不間斷地混音，而不需要開啟另一個裝置。


詳細的教學正在準備中，將一步一步引導您完成 Samourai Wallet 和 RoninDojo v2 從 A 到 Z 的共同接合過程。


若要深入瞭解 CoinJoin 及其在 Bitcoin 上的使用，我也邀請您參閱這篇文章：了解並在 Bitcoin 上使用 CoinJoin，我在這篇文章中詳細介紹了有關這項技術的所有知識。




### 使用 Whirlpool 統計工具 (WST)


使用 Whirlpool 執行共同接合之後，精確評估混合 UTXOs 所達到的隱私等級是非常有用的。為此，您可以使用 Python 工具 *Whirlpool Stat Tool*。此工具可讓您測量 UTXOs 的前瞻性和回溯性得分，同時分析它們在資料池中的擴散率。


為了加深您對這些指數計算機制的瞭解，我建議您閱讀這篇文章：REMIX - Whirlpool，詳細說明這些指數的運作。


https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



若要存取 WST 工具，請前往 RoninCLI。為此，請在個人電腦上開啟終端機，並使用下列指令與您的節點建立 SSH 連線：

`SSH ronindojo@[IP]`


例如，如果您節點的 IP Address 是 `192.168.1.40`，則適當的指令是

`SSH ronindojo@192.168.1.40`


如果您在步驟 6 中變更了使用者名稱，用另一個使用者名稱取代預設使用者名稱 (`ronindojo`)，請務必在指令中使用這個新名稱。例如，如果您選擇 `planb` 作為您的使用者名稱，而 IP Address 是 `192.168.1.40`，則輸入的指令將會是：

`SSH planb@192.168.1.40`


您會被要求輸入使用者密碼。輸入後按 `enter` 鍵確認。然後，您將存取 RoninCLI Interface。使用鍵盤上的箭頭鍵瀏覽到 `Samourai Toolkit` 功能表，然後按下 `enter` 鍵選取：


![Samourai Toolkit](assets/notext/43.webp)


然後選擇「Whirlpool Stat Tool」：


![WST](assets/notext/44.webp)


初始化 WST 後，工具將進行自動安裝。在此步驟中請稍候。使用說明將會捲動顯示。安裝完成後，按任意鍵進入 WST 終端：


![WST commands](assets/notext/45.webp)


將會顯示以下指令提示：

`wst#/tmp>``


如果您希望退出 Interface 並返回 RoninCLI 功能表，只需輸入即可：

退出


首先，必須設定代理使用 Tor，以確保從 OXT 擷取資料時的機密性。輸入指令：

`socks5 127.0.0.1:9050`


隨後，繼續下載包含您的交易的池資訊：

下載 0001

將 `0001` 改為您感興趣的池的面額代碼。WST 上的面額代碼如下：


- Pool 0.5 bitcoins: `05`
- Pool 0.05 bitcoins: `005`
- Pool 0.01 bitcoins: `001`
- Pool 0.001 bitcoins: `0001`


下載完成後，在此指令中將 `0001` 改為您的資料池代碼，即可載入資料：載入 0001


![WST loading](assets/notext/46.webp)


等待載入完成，這可能需要幾分鐘。資料載入完成後，若要知道硬幣的未設定分數，請執行 `score` 指令，後面跟上您的 txid（不含括號）：

得分 [txid]`


![WST score](assets/notext/47.webp)


WST 接著會顯示回溯分數 (_Backward-looking metrics_)，接著會顯示前瞻分數 (_Forward-looking metrics_)。除了暫停評分之外，WST 也會顯示您的交易相對於其暫停評分在交易池中的擴散率。


**請注意，硬幣的前瞻性分數應從初始組合的 txid 開始計算，而不是從最近的組合開始計算。反之，UTXO 的回溯分數則是從上一個週期的 txid 開始計算。**


### 使用波爾茲曼計算機

Boltzmann 計算器是分析 Bitcoin 交易的工具，提供測量其熵水平以及其他先進指標的能力。這些資料可提供交易隱私權的量化評估，並協助找出潛在的瑕疵。此工具已整合至您的 RoninDojo 節點，讓您可以輕鬆存取和使用。


在詳細介紹 Boltzmann 計算機的使用步驟之前，必須先瞭解這些指標的含義、計算方法及其效用。雖然這些指標適用於任何 Bitcoin 交易，但對於評估 CoinJoin 交易的品質特別有用。


**軟件計算的第一個指標**是可能組合的總數，在工具中的 `nb combinations` 下顯示。根據所涉及的 UTXOs 值，該指標量化了輸入與輸出之間的關聯方式的數量。換句話說，它決定了交易可以 generate 進行的可信解釋的數量。例如，根據 Whirlpool 5x5 模型構成的 CoinJoin 會出現 `1496` 種可能的組合：

![combinations](assets/notext/50.webp)

資料來源：KYCP


**計算的第二個指標**是交易的熵，用`Entropy`來指定。當一筆交易有許多可能的組合時，參考它的熵通常更有意义。其定義為可能組合數的二進位對數。以下是使用的公式：


- $E$：交易的熵；
- $C$：交易的可能組合數。

$$E = \log_2(C)$$


在數學中，二進制對數（基 2 對數）對應於將 2 提升到幂的逆運算。換句話說，$x$ 的二進制對數就是為了得到 $x$ 而必須將 2 提升到的指數。因此，這個指標是以位元來表示的。讓我們以計算根據 Whirlpool 5x5 模型結構的 CoinJoin 交易的熵為例，如前所述，該交易提供的可能組合數為 `1496`：

$$ C = 1496 $$

$$ E = \log_2(1496) $$

$$ E \approx 10.5469 \text{ bits}$$


因此，這筆 CoinJoin 交易的熵值為 10.5469 位元，非常令人滿意。此值越高，交易可接受的不同解釋就越多，從而提高其隱私度。


讓我們以一個較傳統的交易為例，它有一個輸入和兩個輸出：[1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://Mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)

對於這個交易，唯一可能的解釋是：`(inp 0) > (Outp 0 ; Outp 1)`。因此，它的熵建立在 `0`：

$$ C = 1 $$

$$ E = \log_2(1) $$

$$ E \approx 0 \text{ bits}$$

**波爾茲曼計算機提供的第三個指標**名為「Wallet 效率」。這個指標透過與相同設定下的最佳交易比較，來評估交易的效率。這讓我們討論最大熵的概念，它對應於特定交易結構理論上可以達到的最高熵。因此，對於 Whirlpool 5x5 CoinJoin 結構，最大熵設定為「10.5469」。然後，將這個最大熵與所分析交易的實際熵相對照來計算交易的效率。使用的公式如下：


- $ER$: 交易的實際熵，以位元表示；
- $EM$：給定交易結構的最大可能熵，也是以位元為單位；
- $Ef$：交易效率，以位元為單位。

$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$

$$Ef = 0 \text{ bits}$$


此指標也以百分比表示，其計算公式如下：


- $CR$：實際可能的組合數；
- $CM$：具有相同結構的最大可能組合數；
- $Ef$：以百分比表示的效率。

$$Ef = \frac{CR}{CM}$$

$$Ef = \frac{1496}{1496}$$

$$Ef = 100\%$$


因此，「100%」的效率表示交易根據其結構，將隱私的潛力發揮到最大。


**第四個指標**，熵密度，或稱「熵密度」，提供了一個相對於交易的每個輸入或輸出的熵的角度。這個指標對於評估和比較不同規模的交易效率非常有用。要計算它，只要將交易的總熵除以所涉及的輸入和輸出總數即可。以 Whirlpool 5x5 CoinJoin 為例：


- $ED$: 以位元表示的熵密度；
- $E$：交易的熵，以位元表示；
- $T$：交易中輸入和輸出的總數。

$$T = 5 + 5 = 10$$

$$ED = \frac{E}{T}$$

$$ED = \frac{10.5469}{10}$$

$$ED = 1.054 \text{ bits}$$

**波爾茲曼計算機提供的第五個資訊**是輸入和輸出之間的匹配概率表。此表透過「波爾兹曼分數」顯示特定輸入連接至特定輸出的概率。以 Whirlpool CoinJoin 為例，概率表會突出顯示每個輸入和輸出之間的連接機率，提供交易中關聯的模糊性或可預測性的定量測量：


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


在這裡，很明顯每個輸入都有同等機會與任何輸出相關聯，這加強了交易的模糊性和機密性。但是，在只有單一輸入和兩個輸出的簡單交易中，情況就不同了：


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

在這裡，我們可以看到每個輸出來自輸入 0 的機率是 100%。因此，較低的機率會稀釋輸入和輸出之間的直接關聯，從而轉換成更高的機密性。


**** 提供的第六項資訊是確定性連結的數量，並輔以這些連結的比率。這個指標揭示了在分析的交易中，有多少輸入和輸出之間的連結是不容置疑的，具有 100% 的可能性。反過來，比率則可顯示這些確定性連結在交易總連結中所佔的比重。


舉例來說，Whirlpool 型 CoinJoin 交易沒有任何確定性連結，因此顯示的指標和比率都是 0%。另一方面，在我們檢視的第二筆交易（有一個輸入和兩個輸出）中，指標設定為 2，比率達到 100%。因此，由於輸入和輸出之間沒有直接且無可爭議的連結，因此指標為零表示保密性極佳。


**如何在 RoninDojo 上存取 Boltzmann 計算機？**

若要存取 *Boltzmann Calculator* 工具，請前往 RoninCLI。為此，請在個人電腦上開啟終端機，並使用下列指令與您的節點建立 SSH 連線：`SSH ronindojo@[IP]``


舉例來說，如果您節點的 IP Address 是 `192.168.1.40`，則適當的指令將會是：

`SSH ronindojo@192.168.1.40`


如果您在步驟 6 中變更使用者名稱，以另一個使用者名稱取代預設使用者名稱 (`ronindojo`)，請務必在指令中使用這個新名稱。例如，如果您選擇 `planb` 作為您的使用者名稱，而 IP Address 是 `192.168.1.40`，則輸入的指令將會是：

`SSH planb@192.168.1.40`


您會被要求輸入使用者密碼。輸入後按`enter`鍵確認。然後，您將存取 RoninCLI Interface。使用鍵盤上的箭頭導覽到 `Samourai Toolkit` 功能表，然後按`enter`選取：


![Samourai Toolkit](assets/notext/43.webp)


然後選擇 `Boltzmann Calculator`：


![boltzmann](assets/notext/49.webp)


您將到達軟體的首頁：


![boltzmann home](assets/notext/51.webp)


輸入您要研究的交易的 txid，然後按`enter`鍵：


![boltzmann txid](assets/notext/52.webp)


然後計算器會為您提供我們之前討論過的所有指標：


![boltzmann result](assets/notext/53.webp)


### RoninDojo v2 的其他功能

您的 RoninDojo 節點整合了其他各種功能。尤其是，您有能力掃描特定資訊，將其納入考量。例如，有時候您的 Samourai Wallet 連接到 RoninDojo 時，可能不會顯示您實際持有的比特幣。如果餘額顯示為 0，而您確定在這台 Wallet 中擁有比特幣，有幾種原因可以解釋這種情況，例如衍生路徑中的錯誤。但其中一個原因也可能是您的節點沒有正確監控您的地址。要解決這個問題，您可以使用 _xpub tool_ 確保您的節點確實跟隨您的 `xpub`。要透過 RoninUI 存取此工具，請遵循下列路徑：

維護 > XPUB 工具


輸入造成問題的 `xpub` 並按一下 `Check` 按鈕以驗證這些資訊：

![xpub tool](assets/notext/54.webp)

確保所有交易都已正確列出。驗證所使用的衍生類型是否與您的 Wallet 吻合也很重要。如果不是這樣，請按一下 `Retype`，然後根據您的需求從 `BIP44`、`BIP49` 或 `BIP84`中選擇。

除了這個工具之外，RoninUI 的「維護」標籤還包含許多其他有用的功能：


- 交易工具：可檢查指定交易的詳細資料；
- Address 工具：允許確認您的道場追蹤指定的 Address；
- 重新掃描區塊：強制您的節點對指定的區塊範圍執行新的掃描。


Push Tx" 選項卡是 RoninUI 另一項有趣的功能，可在 Bitcoin 網路上廣播已簽署的交易。交易必須以十六進位形式輸入。


關於 RoninUI 面板上的其他可用標籤：


- `Apps`：託管 Whirlpool 應用程式，未來一定會用來整合新的應用程式；
- `日誌`：提供即時存取軟體事件日誌的功能；
- 系統資訊」：提供您節點的一般資訊，例如 CPU 溫度、儲存空間使用率或 RAM 資料。您也可以找到 `Reboot` 和 `Shut down` 選項來重新啟動或關閉您的節點；
- `設定`：允許您變更使用者密碼。


就是這樣！感謝您跟隨本教學到最後。如果您喜歡，我鼓勵您在社交媒體上分享。此外，如果您有機會，請考慮以捐款的方式來支持那些為我們的社群提供這些免費開放原始碼軟體的開發人員：[https://donate.ronindojo.io/](https://donate.ronindojo.io/).若要加深您對 RoninDojo 的認識，並發掘更多資源，我強烈建議您參考以下提及的外部資源連結。


**外部資源：**


- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/introducing-boltzmann-85930984a159](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)
