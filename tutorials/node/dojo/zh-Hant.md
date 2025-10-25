---
name: 道場
description: 隱私權與自主性的開放原始碼 Bitcoin 節點
---

![cover](assets/cover.webp)



*本教學是根據 [Ashigaru 官方說明文件](https://ashigaru.rs/docs/)，由我接手並加以擴充。我重新編寫了所有章節，以提高清晰度、增加更詳細的說明，以及為初學者提供插圖，使安裝和使用更容易理解。



---

Dojo 是一個開放源碼程式，設計用來作為某些以 Bitcoin core 節點為基礎、以隱私為導向的 Bitcoin 電子錢包的後端伺服器。從歷史上來看，它是為了與 Samourai Wallet 一起工作而開發的，Samourai Wallet 是一個移動 Wallet，提供了先進的隱私功能，如 Whirlpool (CoinJoin)、Ricochet、Stonewall、PayNym...Samourai Wallet 在其開發人員被捕後現已關閉，但其社群繼承者 **Ashigaru Wallet** 已接手，並繼續依賴 Dojo 為希望在使用 Bitcoin 時控制其資料的使用者提供完整的體驗。



![Image](assets/fr/01.webp)



實際上，Dojo 是您的 Wallet 與 Bitcoin 網路之間的閘道。如果沒有 Dojo，輕量級移動 Wallet 就必須查詢第三方伺服器，以獲得您的 UTXO 狀態和歷史記錄，或廣播您的交易。這意味著敏感資料對第三方伺服器的依賴和洩漏（使用的地址、金額、付款頻率等）。有了 Dojo，您就可以自己託管這個伺服器，直接連接到您自己的 Bitcoin 節點。這樣，您所有的投資組合請求都會通過由您控制的基礎設施，沒有中介，加強了您的機密性和主權。



## 設立道場的要求



建立 Dojo 伺服器並不需要超強大的電腦。任何人只要有一台入門級電腦、穩定的網際網路連線，並能夠持續開機（24/7），就可以架設一個可運作的 Dojo。



### 選擇您的機器類型



您可以使用 ：




- 一台筆記型電腦 ；
- 桌上型電腦 ；
- 迷你電腦 (例如 Intel NUC、Lenovo Thincentre Tiny...)。



每種選項都有其優缺點：




- 價格：翻新的迷你電腦或桌上型電腦通常會比全新的筆記型電腦便宜。
- 佔用空間：Mini-PC 佔用較少空間。
- 電源 Supply：筆記型電腦的優勢在於有電池，這表示它不會在斷電時關機，這點與迷你電腦不同。
- 可升級性：閂鎖一般可讓您增加記憶體或輕鬆更換 Hard 磁碟。



如需更多關於選擇設備的資訊，我建議您參加此課程：



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### 推薦設備



沒有必要購買一台新機器。具有以下規格的翻新電腦會比單板電子產品（如 Raspberry Pi）提供更好的效能。



**最低規格：**




- X86-64 架構 (64 位元處理器)。
- 2 GHz 雙核心處理器或更快的速度。
- 最低 8 GB RAM。
- 2 TB 或更多 NVMe SSD（用於儲存 Bitcoin 的 Blockchain，以及必要的索引）。



**建議使用的作業系統： **




- 以 Debian 為基礎的發行版，例如 Ubuntu 24.04 LTS。



**建議設備：**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- 等等。



在其他硬體配置上執行 Dojo 伺服器是完全可能的。但是，為了獲得最佳效能並限制問題發生，我們建議您遵循上述建議。



在本教程中，我將使用一台舊的 ThinkCentre Tiny，配備 Intel Pentium Dual-Core G4400T 處理器、8 GB 記憶體和 2 TB SSD。



## 1 - 安裝 Ubuntu



*如果您希望在已經設定好的裝置上安裝 Dojo，您可以跳過此步驟，直接進入步驟 2.*。



準備好所選的硬體後，就該安裝作業系統了。您幾乎可以使用任何 Debian 發行版，但我建議您選擇 LTS 版本的 Ubuntu，因為它完全符合我們的目的。以下是安裝步驟：



### 1.1. 建立可開機的 USB 金鑰



從一台已經可以使用的電腦 (您平常使用的電腦)，下載 Ubuntu LTS ISO 映像檔 [從官方網站](https://ubuntu.com/download/desktop) (在撰寫本文時為`24.04`，但如果有其他版本，則採用最新版本)。



![Image](assets/fr/02.webp)



將至少 8 GB 的 USB key 插入此電腦，然後用 [Balena Etcher](https://etcher.balena.io/) 等軟體建立可開機的 key。選擇您剛下載的 Ubuntu ISO 映像，選擇 USB key 作為目標裝置，然後開始建立程序（請耐心等待，可能需要幾分鐘）。



![Image](assets/fr/03.webp)



將可開機 USB key 插入已關機的電腦 (您要執行 Dojo 的電腦)。啟動電腦，並立即按下鍵盤上的 **F12** 或 **F10**（視機型而定），以存取開機功能表。然後選擇您的 USB key 作為電腦開機順序中的優先裝置。



![Image](assets/fr/04.webp)



### 1.2. 安裝作業系統



出現 Ubuntu 首頁畫面。選擇「嘗試或安裝 Ubuntu*」。



![Image](assets/fr/05.webp)



然後遵循經典的 Ubuntu 安裝程序：




- 選擇語言。
- 選取鍵盤類型。
- 如果您透過 RJ45 纜線連線，就不需要設定 Wi-Fi。
- 按一下「*安裝 Ubuntu*」，並勾選安裝第三方軟體 (Wi-Fi 驅動程式、多媒體編解碼器等) 的選項。
- 當精靈要求選擇安裝類型時，選擇「*刪除磁碟並安裝 Ubuntu*」。 **警告**：此操作會完全刪除磁碟內容。請仔細檢查您所選擇的磁碟是否符合 Dojo 的 NVMe SSD。
- 建立一個簡單的使用者名稱 (例如 "*loic*")。
- 為機器指定名稱 (例如 "*dojo-node*")。
- 設定強大的密碼，並妥善保管。
- 啟用「*請求我的密碼登入*」選項以加強安全性。
- 指出您的時區，然後按一下「*安裝*」。
- 等待安裝完成。完成後，系統會自動重新啟動。
- 重新啟動電腦時，請移除 USB 安裝金鑰。



有關 Ubuntu 安裝程序的詳細資訊，請參閱我們的專用教學 ：



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. 系統更新



第一次開機後，使用組合鍵 ***Ctrl + Alt + T*** 開啟終端機，執行下列指令更新系統：



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2.外屋安裝



為了讓 Dojo 正常運作，您的系統上必須有某些軟體磚塊。這些磚塊用來管理軟體儲存庫、通訊、歸檔解壓，以及在 Docker 容器內執行 Dojo。所有這些操作都在終端機執行。



### 2.1.準備工作



以下指令會返回您的個人資料夾。在執行一系列安裝之前，這是一個很好的做法。



```bash
cd ~/
```



在安裝任何軟體之前，請確定您電腦上可用軟體的資料庫是最新的。這樣可以避免安裝過時的版本。



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. 安裝公用程式



有幾種工具需要添加到系統中：




- `apt-transport-https`: 可讓您透過 HTTPS 安全地下載封包
- ca-certificates：管理加密連線所需的憑證
- `curl`：從網際網路擷取檔案
- `gnupg-agent`: 用於 GPG 金鑰管理
- software-properties-common`: 提供操作 APT 套件庫的公用程式
- `unzip`: 解壓縮 ZIP 格式的檔案



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



安裝期間，系統可能會要求您確認。按 "*y*「鍵，然後按 」*Enter*"。



![Image](assets/fr/08.webp)



### 2.3. 安裝 Torsocks



Torsocks 可讓某些指令透過 Tor 網路執行，提高通訊的機密性。



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. 安裝 Docker 和 Docker Compose



Dojo 在 Docker 容器內執行。這意味著每個服務都被隔離在獨立的環境中，簡化了維護和安全性。要做到這一點，您需要安裝 Docker 和 Docker Compose 工具，該工具可讓您同時管理多個容器。



#### 新增 Docker 簽署金鑰



Docker 提供自己的數位簽章金鑰。加入它可以驗證下載套件的真實性。



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### 新增官方 Docker 儲存庫



接下來，您需要告訴系統在哪裡可以找到 Docker 官方套件。此指令會在套件管理員設定中加入新的套件庫。



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### 安裝 Docker 和 Docker Compose



現在可以安裝主要的 Docker 元件。



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### 使用者授權



預設情況下，只有以管理員權限執行的指令才能啟動 Docker。為了更方便，我建議將現有使用者加入「*docker*」群組。這樣您就可以使用 Docker，而無需每次都輸入 `sudo`。



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3.單一使用者建立（可選）



如果您想提高系統的安全性，我建議您創建一個獨立的用戶，專門用於運行 Dojo。這種分離限制了風險：如果 Dojo 發生安全問題，它不會直接危及您的主帳戶。



### 3.1. 建立使用者帳號



以下指令會建立一個名為「*dojo*」的新使用者。這個使用者會有一個主目錄 `/home/dojo`，並且可以存取 bash 終端。它也會被加入 sudo 群組，以便執行管理命令。



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2.設定密碼



為此帳戶指定一個強大的密碼非常重要。理想情況下，您應該使用 Bitwarden 之類的密碼管理器來 generate 一個冗長、Hard-to-guess 的密碼組合。



```bash
sudo passwd dojo
```



系統隨後會要求您輸入所選的密碼，然後再確認一次。



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3.授權使用者使用 Docker



若要讓使用者「*dojo*」啟動執行 Dojo 所需的容器，他必須加入 Docker 群組。這可避免在每個指令前加上 `sudo`。



```bash
sudo usermod -aG docker dojo
```



### 3.4.系統重新啟動



為了讓群組變更生效，必須重新啟動機器。



```bash
sudo reboot
```



### 3.5.以新使用者登入



當系統重新啟動時，請使用***dojo***登入帳號和之前定義的密碼登入。之後的所有步驟都必須從這個專用帳號執行。



## 4.下載並檢查 Dojo



在安裝 Dojo 之前，必須確保檔案來自官方開發人員，且未經修改。這一步驟依靠使用 PGP 和哈希值來驗證檔案的真實性和完整性。



### 4.1. 匯入開發者的 PGP 金鑰



透過 Tor 下載開發者的公開金鑰，並將其匯入您的本機密碼匙鏈。此密鑰將被用來驗證與 Dojo 檔案相關的簽章。



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. 下載最新版本的 Dojo



讀取包含 Dojo 原始碼的壓縮檔。在這個範例中，最新的版本是 `1.27.0`：請依據 [官方 GitHub 套件庫中的最新版本](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) 來修改指令。



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3.下載指紋和簽名



開發人員公佈了一個列出存檔數位指紋的檔案，以及一個由他們的 PGP 金鑰簽署的檔案。下載它們以在本機比較您的檔案。



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4.檢查 PGP 簽署



檢查指紋檔案是否已由匯入的金鑰簽署。



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



正確的結果會顯示有效的簽章，其金鑰為 `E53AD419B242822F19E23C6D3033D463D6E544F6`，相關的 Address 為 `dojocoder@pm.me`。可能會出現警告，說明金鑰未經認證：您可以忽略它。



另一方面，如果簽章無效，請立即停止安裝程序，並從頭重新開始。



![Image](assets/fr/17.webp)



### 4.5.檢查存檔完整性



計算下載檔案的 SHA256 指紋，然後開啟指紋檔案，比較兩個數值。



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



如果兩個指紋相同，您可以確定存檔未被修改。如果兩者不同，則無法繼續，並刪除檔案。



![Image](assets/fr/18.webp)



### 4.6.擷取和整理檔案



一旦驗證成功完成，您就可以解壓縮存檔，並準備一個專用於 Dojo 安裝的資料夾。



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7.清理不必要的檔案



刪除不再需要的臨時檔案和存檔，以保持環境清潔。



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5.道場配置



Dojo 是一個後端伺服器，匯集了多項服務，可與您的投資組合互動，並管理您的 Bitcoin 節點。它的設定可能很複雜，但該專案提供了一個簡化的方法，可自動安裝和設定下列元件：




- Dojo (主 API)
- Bitcoin core (完成 Bitcoin 節點)
- BTC-RPC Explorer (web Block explorer)
- Fulcrum Indexer（區塊和交易的快速索引）
- 可在 Tor 網路上使用的 Fulcrum Electrum 伺服器
- 本地網路中可用的 Fulcrum Electrum 伺服器
- 管理憑證



### 5.1. 管理憑證



為了確保存取各種服務的安全性，您需要 generate 幾個獨特的識別碼：




- `bitcoind_rpc_user`
- `bitcoind_rpc_password`
- `mysql_root_password`
- mYSQL_USER
- `mysql_password`
- nODE_API_KEY`
- `node_admin_key`
- node_jwt_secret



這些識別碼**必須是唯一的**（這點非常重要：您不能在多個服務中使用相同的密碼），完全由數字、大寫字母和小寫字母（字母數字）組成，長度約為 40 個字元，以保證高度安全性。我再次強烈建議您使用密碼管理器。



### 5.2.存取設定檔案



Dojo 設定檔位於 `conf/` 資料夾。移動到此目錄：



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3.Bitcoin core 配置



使用 nano 文字編輯器開啟 Bitcoin core 配置檔案：



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



在此檔案中，輸入產生的識別碼：



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ *** 將 `your-ID-here` 和 `your-password-here` 替換為您自己的登入帳號 (使用強大的密碼).***。



您也可以調整 Bitcoin core 使用的快取記憶體大小，以提升效能（如果您有大量可用的 RAM，甚至可以使用更多）：



```
BITCOIND_DB_CACHE=2048
```



若要儲存變更並關閉編輯器 ：




- 按 `Ctrl + X
- 類型 `y`
- 然後按下 "*Enter*"



### 5.4.MySQL 設定



然後開啟 MySQL 資料庫設定：



```bash
nano docker-mysql.conf.tpl
```



請輸入您的登入資訊：



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ *** 將 `your-ID-here` 和 `your-password-here` 替換成您自己的登入帳號 (使用強大、獨特的密碼).***。



以相同方式儲存 (`Ctrl+X`、`y`、"*Enter*")。



![Image](assets/fr/23.webp)



### 5.5.支撐分度器配置



開啟以下檔案：



```bash
nano docker-indexer.conf.tpl
```



新增參數以啟動 Fulcrum 並將其正確整合到 Dojo .NET 中：



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



接下來，根據您的設定，有兩種可能性。如果 Dojo 安裝在一台獨立於您日常電腦的機器上（專用機器、伺服器......），請在您的本地網路中輸入其 IP Address，例如 ：



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



若要找出您電腦的本機 IP Address，請開啟另一個終端機，並輸入下列指令：



```bash
hostname -I
```



第二種可能性：如果 Dojo 是直接在您日常使用的個人電腦上執行，請保留設定檔中的預設值：



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



儲存並退出編輯器 (`Ctrl + X`, `y`, "*Enter*").



### 5.6.節點服務設定



最後，開啟主 Dojo 服務的設定：



```bash
nano docker-node.conf.tpl
```



請輸入您的登入資訊：



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ *** 將 `your-password-here` 替換為您自己的憑證 (使用強大、獨特的密碼)。***



![Image](assets/fr/26.webp)



然後啟動本機索引器：



```
NODE_ACTIVE_INDEXER=local_indexer
```



儲存並退出編輯器 (`Ctrl + X`, `y`, "*Enter*").



### 5.7.登入管理



設定完成後，不需要儲存所有產生的識別碼。唯一絕對必須儲存的是 .NET：



```
NODE_ADMIN_KEY
```



此登錄可讓您稍後登入 Dojo 維護工具。所有其他登入帳號都可以從您的密碼管理員或手寫筆記中移除。如果您將來需要擷取它們，仍可從 Dojo 設定檔中存取。



## 6.道場安裝



在此階段，Dojo 將會在您的機器上安裝並啟動。該操作將啟動多個服務（Bitcoin core、Fulcrum 索引器、Dojo 後端等），並啟動 Blockchain Bitcoin 的完全同步。這可能需要數天時間，視您的硬體和網際網路連線而定。



### 6.1.檢查 Docker 是否正常運作



在開始安裝之前，請確定 Docker 已經運作。執行下列指令：



```bash
docker run hello-world
```



此指令會下載並啟動一個小型測試容器。如果一切運作正常，您應該會看到類似 ：



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



如果沒有顯示此訊息，請先用 .NET Framework 重新開機：



```bash
sudo reboot
```



然後重新登入您的 **dojo** 帳戶，並再次執行測試指令。如果錯誤仍然存在，表示 Docker 未正確安裝。在這種情況下，請返回安裝 Docker 的步驟 `2.4.`，並仔細檢查每個指令。



### 6.2.前往 Dojo 安裝目錄



安裝所需的腳本位於 `my-dojo` 資料夾。移動到此目錄：



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



使用 `ls` 指令檢查 `dojo.sh` 檔案是否存在。這是自動安裝 Dojo 和啟動所有服務的主要腳本。



![Image](assets/fr/29.webp)



### 6.3.開始安裝



執行 .NET Framework 2.0 開始安裝：



```bash
./dojo.sh install
```



按 `y`，然後按「*Enter*」確認安裝。



![Image](assets/fr/30.webp)



這個腳本將 ：




- 下載並啟動必要的 Docker 容器、
- 初始化 Bitcoin core，並開始同步化 Blockchain、
- 啟動 Fulcrum 索引器來追蹤交易和地址、
- 啟動 Dojo 後端及其 API。



您會看到滾動的日誌源源不絕，其中有色彩繽紛的參考資料，例如 `bitcoind`、`soroban`、`nodejs` 或 `fulcrum`。這種捲動表示 Dojo 已經開始運行，並開始執行各種服務。



![Image](assets/fr/31.webp)



### 6.4.退出記錄顯示



日誌會即時出現在您的終端機。當 Dojo 在背景執行時，若要返回命令提示，請輸入 ：



```
Ctrl + C
```



別擔心：停止日誌顯示並不會停止服務。Docker 會繼續在背景執行 Dojo (如果您想要 IBD 繼續，顯然不需要停止電腦)。



### 6.5.瞭解 *初始區塊下載* (IBD)



啟動時，Bitcoin core 必須下載並驗證 2009 年以來的整個 Blockchain。此步驟稱為 ***初始區塊下載* (IBD)**。這是非常重要的，因為它可以讓您的 Dojo 節點獨立驗證每個 Bitcoin 區塊和交易。



此同步的時間長短取決於幾個因素：




- 您的處理器功率和可用的 RAM 記憶體數量、
- 磁碟的速度、
- 您的節點連接的對等體的數量和品質、
- 您的網際網路連線速度。



實際上，這項作業一般需要 ** 2 到 7 天**。在此期間，您可以讓您的機器持續開機。機器開機時間越長，同步化完成的速度就越快。我建議您定期查看 Bitcoin core 日誌，或安裝 Dojo 維護工具（請參閱下一節），以檢查同步狀態。



若要加深您對 IBD 的認識，以及更廣泛而言，對 Bitcoin 節點的運作和作用的認識，我建議您看看這個課程：



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7.同步監控



首次安裝 Dojo 時，您需要等待兩個主要作業完全完成：Blockchain Bitcoin (*IBD*) 的完整下載，以及 Fulcrum 對此 Blockchain 的索引。視您的連線和機器電力而定，這可能需要好幾天的時間。在此期間，您可以監控進度，以確保一切運作順利。



有兩種方法可以監控同步化的狀態：




- 使用 Dojo Maintenance Tool（或 DMT），它很簡單，但在 IBD 期間提供的詳細資訊很少；
- 直接諮詢您機器上的 Dojo 日誌，更具技術性但更精確。



### 7.1.透過 Dojo Maintenance Tool (DMT) 進行檢查



Dojo Maintenance Tool 是一個安全、基於 Web 的 Interface，可讓您監控工廠的狀態，並執行某些操作。這是監控 IBD 進度的最簡單、最方便的方法。在初始同步階段，顯示的資訊可能有限。例如，DMT 不會顯示 Fulcrum 索引的詳細進度。另一方面，一旦同步完成，DMT 將清楚顯示 ：




- Green 上的所有指示燈；
- 每個服務 (節點、索引器、Dojo DB) 的最後一次驗證區塊。



要存取它，您需要知道您的 DMT 的 URL，並 [透過 Tor 瀏覽器] 連線到它(https://www.torproject.org/download/)。要做到這一點，請打開終端機，進入 `/my-dojo` 目錄：



```bash
cd ~/dojo-app/docker/my-dojo
```



然後執行以下指令：



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



然後，您就可以存取透過 Tor 連線到您的 Dojo 的所有相關資訊。我們在此感興趣的是以下 URL：



```
Dojo API and Maintenance Tool =
```



若要從任何網路的任何機器存取 DMT (即使是遠端)，請開啟 Tor 瀏覽器並輸入此 URL，接著輸入 `/admin`。例如，如果您的 URL 是 `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion `，您就需要在 [Tor 瀏覽器](https://www.torproject.org/download/) 欄輸入：



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **請嚴格保密此 Address



接著您會被重定向到認證頁面。DMT 使用您之前產生的 `NODE_ADMIN_KEY` 密碼登入。



![Image](assets/fr/33.webp)



登入後，您可以存取「*Dojo 維護工具*」！在 IBD 期間，您可以在「*Full node*」功能表中看到「*最新區塊*」資訊，讓您知道 Bitcoin 節點目前的狀態。



![Image](assets/fr/34.webp)



記得在 Tor 瀏覽器中將此 Address 加入書籤，方便日後檢索。



一旦您的 Dojo 完全同步，您應該會在 DMT 首頁的所有指標上看到 Green 檢查 ✅。



### 7.2.透過 Dojo 日誌驗證



追蹤 IBD 進度的第二個方法是直接查詢您的機器日誌。這種方式提供了更精確、即時的監控。您可以看到 Bitcoin core 在下載區塊的進度，以及 Fulcrum 如何為這些區塊編制索引。



連接到託管 Dojo 的機器，並打開終端機。所有指令都應從 `my-dojo` 目錄執行。在此資料夾中定位：



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Bitcoin core 日誌



檢視 Bitcoin core 記錄以追蹤 IBD 的進度：



```bash
./dojo.sh logs bitcoind
```



一開始，您會看到區塊標頭的預同步化階段：



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



當這個數字達到 100% 時，Bitcoin core 將開始完整下載 Blockchain。您會看到 IBD 的進度。若要找出目前的區塊高度，請查看 `height=` 所指示的值。您也可以遵循 `progress=` 這個關鍵，它顯示 IBD 進度的百分比。



![Image](assets/fr/36.webp)



與往常一樣，若要關閉記錄並返回命令提示，請使用 `Ctrl + C` 組合。



#### 支點日誌



一旦 Bitcoin core 完成標頭預同步，Fulcrum 就會開始為 Blockchain 編製索引。使用 .NET 查看其日誌：



```bash
./dojo.sh logs fulcrum
```



然後，您會看到在 `height:` 之後顯示的最後索引的區塊高度，以及索引進度百分比。



![Image](assets/fr/37.webp)



### 7.3.Fulcrum 資料庫損毀



Fulcrum 是一款功能特別強大的索引器，但其安裝可能會很複雜，尤其是因為其精密的資料庫管理。如果在初始同步過程中斷電或突然關機，索引器的資料庫可能會損毀。例如，如果您有以下日誌，就可以看到這一點：



```bash
fulcrum | The database has been corrupted etc...
```



**Note:** 這種錯誤應該會在即將發行的 Fulcrum 2.0 中修正。



如果這種情況發生在您身上，對 bitcoind（您的 Bitcoin 節點）沒有影響：它的 IBD 將繼續進行，不受 Fulcrum 的影響。但是，您將無法使用 Fulcrum，直到您刪除其損壞的資料，並從頭重新啟動其同步。下面是它的工作原理：



停止道場：



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



僅刪除 Fulcrum 容器和卷：



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



通常的名稱是 `my-dojo_data-fulcrum`，如果您的情況不是這樣，請調整之前指令所傳回的名稱。



然後重新啟動 Dojo 並從頭重建 Fulcrum：



```bash
./dojo.sh upgrade
```



然後，您可以參考日誌來檢查 Fulcrum 是否正常運作：



```bash
docker logs -f fulcrum
```




## 8.使用 Dojo 維護工具



一旦您的 Bitcoin 結與最 Proof of Work 的經頭同步，且 Blockchain 經由 Fulcrum 100%索引，您就可以開始使用您的道場。



您的 Dojo 提供了廣泛的功能，每個新版本都會定期增強。在我看來，最重要的 2 個功能是 ：




- 可以連接您的 Ashigaru Wallet，使用您自己的節點查詢 Blockchain 資料並廣播您的交易、
- 和 Block explorer，讓您可以存取 Blockchain Bitcoin 的相關資訊，而不會將您的資料暴露給您無法控制的外部實體。



讓我們來看看如何使用它們。


### 8.1.將 Ashigaru 連接到您的道場



將 Ashigaru Wallet 連接到您的 Dojo 非常簡單：在 DMT 上，打開 "*Pairing*"（配對）功能表。會出現一個 QR 代碼，您可以直接使用 Ashigaru 應用程式掃描。



![Image](assets/fr/38.webp)



在 Ashigaru 應用程式中，當您建立或還原 Wallet 後第一次啟動時，您會被重定向到「*設定您的 Dojo 伺服器*」頁面。按下「*掃描 QR*」，然後掃描 DMT 上顯示的 QR 代碼。



![Image](assets/fr/39.webp)



然後按一下「*繼續*」按鈕。



![Image](assets/fr/40.webp)



您現在已連接到您的道場。



![Image](assets/fr/41.webp)



### 8.2.使用 Block explorer



Dojo 會自動安裝一個 Block explorer，[BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer)，直接從您自己的 Bitcoin 節點汲取資料。探索器可讓您透過簡單易懂的 Interface 網路，存取來自 Blockchain 和您的 Mempool 的原始資訊。因此，您可以輕鬆地檢查待決交易的狀態、檢視 Address 的餘額或檢查區塊的組成。



若要存取，只需從瀏覽器擷取 Tor Address。要做到這一點，請執行您用來獲取 DMT 的 Address 的相同命令：



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



您可以透過 Tor 取得所有 Dojo 連線資訊。這裡我們感興趣的是以下的 URL：



```
Block Explorer =
```



如果您已經與 DMT 連線，也可以在連線 JSON 內的「*Pairing*」功能表中找到這個 Address：



![Image](assets/fr/43.webp)



若要從任何網路的任何機器存取您的瀏覽器 (甚至是遠端)，請開啟 [Tor Browser](https://www.torproject.org/download/)，然後輸入您剛擷取的 URL。



⚠️ **請嚴格保密此 Address



這樣您就可以使用自己的 Block explorer。



![Image](assets/fr/44.webp)



*圖片來源：https://ashigaru.rs/.*



若要追蹤交易，只需在右上方的搜尋列輸入 txid。



![Image](assets/fr/45.webp)



*圖片來源：https://ashigaru.rs/.*



若要檢查與 Address 相關的機芯，請以相同方式在搜尋列輸入 Address。



![Image](assets/fr/46.webp)



*圖片來源：https://ashigaru.rs/.*



您也可以在搜尋列中輸入區塊的 Hash 或高度，以顯示詳細資料。



![Image](assets/fr/47.webp)



*圖片來源：https://ashigaru.rs/.*



## 9.道場維護



### 9.1 停止您的道場



切勿突然切斷 Dojo 的電源，因為這可能會損壞某些資料庫，尤其是 Fulcrum 索引器。如果您必須關機，請務必執行 Dojo 的乾淨關機，然後在完成所有程序後，關閉機器：



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 更新您的道場



Dojo 會定期演進，並發布新版本以修復錯誤、提高穩定性和增加功能。因此，[定期檢查更新](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) 並更新您的 Dojo 是非常重要的。此過程類似於初始安裝，但需要您用最新的可用版本替換某些檔案，同時保持您的配置。以下是進行乾淨、安全更新的詳細步驟：



若要找出 Dojo 目前的版本，請執行命令 ：



```bash
./dojo.sh version
```



雖然這一步是可選的，但我建議您先更新您的作業系統。這樣可以降低不相容的風險，並確保 Dojo 使用的相依性是最新的：



```bash
sudo apt-get update
sudo apt-get upgrade
```



進入 Dojo 目錄，停止目前的服務：



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



然後重新啟動您的系統，以獲得清白的記錄：



```bash
sudo reboot
```



Dojo 隨附經數位簽章的檔案。這些 PGP 簽署可確保檔案來自開發者，且未經任何修改。重要的是每次更新 Dojo 時都要檢查它們，就像第一次安裝時一樣。首先透過 Tor 下載開發者的公開金鑰，然後將其匯入 ：



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



回到您的個人目錄：



```bash
cd ~/
```



透過 Tor 從 GitHub 下載最新版本的 Dojo。在這個範例中，是版本 `1.28.0`（在撰寫本文時，這個版本尚未存在：這只是舉例說明）。請記住將檔案和連結 [換成您想要安裝的版本](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases)：



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



同時下載包含 PGP 指紋和簽章的檔案 (再次記住調整指令中的版本)：



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



檢查下載的指紋檔案是否已由開發者的金鑰簽署：



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



正確的結果應該顯示 ：



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



可能會出現金鑰未經認證的警告，但這並不重要。另一方面，如果簽章無效或對應於另一個金鑰，則不再繼續，並重新開始，檢查連結。



然後計算存檔的 SHA256 指紋，並與官方指紋檔案進行比較：



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



如果兩個指紋完全吻合，則表示存檔是正確且完整的。如果兩者不同，請立即刪除檔案，不要繼續。



解壓縮您主目錄中的存檔：



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



然後將內容複製到 Dojo 目錄，覆蓋舊的 .NET 檔案：



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



此操作會保留您位於「~/dojo-app/docker/my-dojo/conf」的組態檔案，但會以更新的版本取代所有其他檔案。



要保持環境清潔，請刪除不必要的檔案 ：



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



回到 Dojo 腳本目錄，執行更新指令：



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



此指令會指示 Docker 以新檔案重建映像，然後自動重新啟動所有服務。在程序結束時，請檢查日誌，確認 Bitcoin core、Fulcrum 和 Dojo 都能正常運作：



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



如果服務啟動時沒有出錯，且日誌顯示區塊正在處理中，則表示您的 Dojo 已更新並可正常運作。