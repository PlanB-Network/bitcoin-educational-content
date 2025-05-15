---
name: Lightning Network Daemon (Linux)
description: 在 Linux 上安裝和執行 Lightning Network Daemon
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network 是 Bitcoin 的第二個 Layer，使其能以閃電的尺寸出現，這特別要歸功於它所提供的交易速度和低成本。



在本教程中，我們將在 Linux 機器 (Ubuntu 24.04 發行版) 上安裝 Lightning Network Daemon 實作。



## 什麼是 Lightning Network Daemon？



Lightning Network Daemon 是 Lightning Network 的完整 Go 實作。它由 Lightning Labs 創建，可讓您在機器上執行 Lightning 節點的完整實例。


換句話說，有了這個實作，您就可以 ：





- 與 Lightning Network** 互動：您可以使用命令列直接從您的機器終端建立 Lightning 投資組合、管理付款管道和路由等。
- 連結遠端 Bitcoin 節點或您自己的 Bitcoin 核心實例**：LND 可讓您連結一個 Bitcoin 實例，並將其作為您的後端。要使用此實作，您不需要在您的機器上執行 Bitcoin Core 實作。




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## 為什麼要擁有自己的 Lightning 節點？


Lightning 是 Bitcoin 的覆蓋層，可優化傳輸流程並降低交易成本。



透過轉換您的 Lightning 節點，您獲得了主權和自主權。您可以掌控自己的資金，所以請記住：



「不是你的鑰匙，也不是你的比特幣」



從這個意義上說，運行 Lightning 節點可以從以下幾方面增加資料的安全性和完整性：





- 完全控制**：管理您自己的付款管道，成為您自己的銀行，成為您資產的主人。
- 保密性**：交易時無需依賴第三方保護您的隱私。
- 學習與自主**：感謝 `lncli` 指令，您可以從您的終端應用自己，更好地了解 Lightning 的底層過程。
- 權力下放**：在強化和分散 Bitcoin / Lightning Network 方面發揮積極作用。



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


要在我們的機器上執行 LND 實作的實例，您有兩個選擇。我們可以在自己的機器上設定環境在本機執行，或是從 Docker 容器安裝 LND。在此，我們將專注於第一個選項，並在稍後的教學中瞭解如何使用 Docker。


## 從原始碼安裝 LND



### 先決條件


由於 LND 是用 Go 寫成的，您需要確定您的 Linux 機器上有 GoLang 環境和必要的相依性。





- 硬體需求：**


為了獲得流暢、無縫的體驗，您的電腦需要有必要的容量來執行 LND Lightning 節點。



您將需要 ：


1. **8 GB RAM** 可提供最佳流暢性、


2. **多核心處理器 (四核心或更多)**，以有效管理您節點的動作、


3. ** 至少 5GB 磁碟空間**用於修剪節點模式，1TB 用於執行 Bitcoin Core (如果使用遠端節點，則可選)





- 安裝有用的依賴項目：**


以下指令可讓您在機器上安裝執行 LND 所需的工具。其中，您需要安裝 `Git`，一個版本管理工具，以及 `make`，可以從原始碼執行並建構 LND 實作。



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- 在您的 Linux 機器上安裝 GoLang**



截至本教學日期，LND 需要 Go*** 1.23.6 版本才能安裝。



如果您已經安裝了先前的版本，請移除它以安裝新的 Go。


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Go** 環境組態


在您的 `~/.bashrc` 檔案中，初始化下列環境變數，將 Go 加入您的 Linux 系統。



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- 檢查安裝** (法文)


```bash
go version
```



![go-version](assets/fr/03.webp)


### 克隆 LND GitHub 套件庫



使用 git 在您的機器上取得 LND 原始碼的本機複本


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### 建立與安裝



先前已安裝的 `make` 工具可讓您從 LND 原始碼建立可執行檔，並進行安裝。



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



在您的機器上安裝 LND



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- 檢查您的安裝** (法語)



為了確保一切順利，執行這個指令應該可以得到您目前執行的 LND 版本。



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- 維護與升級



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **重要**：LND 更新可能需要較新版本的 Go，因此請務必更新您的系統，以避免安裝時發生相依性問題。


### 設定 Lightning Network Daemon



Lightning LND 節點的設定與 Bitcoin 相似，都是在包含您節點所有參數的設定檔中進行。要做到這一點，您可以在機器的根目錄創建一個隱藏資料夾 `.LND`，然後在這個資料夾中創建您的配置文件 `LND.conf`。



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





在設定檔中，您可以設定 LND 節點。



```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```



## 瞭解您的組態



重要的是，您必須瞭解正確完整安裝 LND 節點所需的最低配置。



根據 `~/.LND/LND.conf` 檔案的內容，以下是欄位的詳細資訊：





- noseedbackup**：允許您選擇是否要 LND 對您的投資組合執行自動備份。  將此屬性設定為「0」可讓您手動將還原資訊儲存到個人選擇的安全位置。





- debuglevel**：允許您定義在動作期間發生錯誤時，錯誤和記錄的詳細程度。





- Bitcoin.active**：指示 LND 作為 Bitcoin 節點運作，並與 Bitcoin 網路互動。





- Bitcoin.Mainnet**：指定 LND 連接到 Bitcoin 的主網路 (Mainnet)，您可以為 Bitcoin Signet 和 Bitcoin Regtest 網路分別設定值 `bitcoind.signet` 和 `bitcoind.regtest





- Bitcoin.node**：指定 LND 應該連接的 Bitcoin 節點類型。





- Bitcoin.rpcuser** 和 **Bitcoin.rpcpassword** ：代表。


分別連接至 Bitcoin 節點的登入 (使用者、密碼)





- bitcoind.zmqpubrawblock** 和 **bitcoind.zmqpubrawtx**：分別定義 ZeroMQ 端點以接收 Bitcoin 網路上新區塊和交易的通知。




## 使用 LND 檢查您的安裝



您可能會想要確認程序是否成功，並與 Lightning Network 同步，以保持您的節點資訊最新。



若要啟動 LND 實作並取得您節點的相關資訊，只需輸入命令 ：


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## 在 LND 上執行動作



安裝完成並通過檢查後，您就可以開始使用了。


以下是讓您開始使用的基本指令。



### 建立投資組合


您的 「閃電 」投資組合是任何管理資金行動的第一步。



⚠️ **重要**：仔細記下您的 24 字 **seed 詞組**。如果發生問題，您需要它來收回您的資金。



同時儲存您的 Wallet 密碼，以便在重新啟動 LND 節點時，可以使用 `lncli unlock` 指令解除鎖定。



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### 檢查您的餘額



直接從終端機查詢您的帳戶：



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### 有關您節點的資訊



使用下面的指令找出您節點上的頻道。



```bash
lncli listchannels
```



您也可以取得與您連線的節點清單。



```bash
lncli listpeers
```



### 通路管理



Lightning 通道可讓您與 Lightning Network 上的另一個節點**直接、逐對連線。在此通道中，您可以自由使用 Exchange Satoshis，最高可達通道的容量。



### 連接至節點



如果您想積極參與並從 Lightning 的強大功能中獲益，連接其他 Lightning 節點是最基本的動作。



要連接到對等體（Lightning 節點），您需要三項資訊：




- 節點的公開金鑰**：這是節點在 Bitcoin 網路中的唯一識別碼；
- IP** ：安裝節點的機器 IP；
- PORT** ：  機器上允許與此節點通訊的開放埠。



您可以在 [amboss](https://amboss.space/) 上找到要連線的節點，這是一個列出 Lightning 節點資訊的平台。



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




請確保連線至**可靠的節點**，以維護您自己系統的完整性。以下是一些選擇正確連線的建議。





- 地理多樣化**：連接不同區域的節點。





- 信譽**：選擇可用性良好的節點。





- 容量**：選擇流通性好的結。





- 收費**：支票路由費用。


### 開通付款管道


若要開啟付款通道，請確定您已**連線**至對等節點，然後定義您希望攔截在此通道中的**容量**（薩托希數量）。



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### 建立閃電 Invoice



Lightning Invoice 代表一串字符，表示您希望在 Lightning Wallet 中接收 Satoshis。


使用自己的節點創建 Lightning 發票，可以保護您的資料（地理和個人），並讓您對資金管理擁有 100% 的自主權。



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### 支付閃電 Invoice



```bash
lncli payinvoice <FACTURE>
```


### 關閉通道



有兩種方法可以關閉目前節點上的活動頻道。





- 合作關閉**：這表示您的節點希望退出付款通道，確保正在進行的任務已完成，並備份資料以避免資金遺失。


```
lncli closechannel <ID_CANAL>
```




- 強制關閉**：⚠️ 盡可能避免，此動作會中斷您付款通道中正在進行的程序，並增加資金損失的風險。


```
lncli closechannel --force <ID_CANAL>
```


## LND 節點的最佳實作與安全性。


使用 Bitcoin/ Lightning 節點時，安全是最重要的。以下幾點可加強安裝的安全性：





- 將您的 `seed phrase` 保存在安全的離線位置。





- 定期備份 `~/.LND/channel.backup` 檔案：每次在您的節點上開啟新頻道 (或關閉舊頻道)，這個檔案都會儲存您的頻道狀態。


⚠️ 在資料遺失或節點故障的情況下，允許您還原通道並恢復支付通道中被凍結的資金



您可以使用以下指令指定此檔案的備份路徑，以還原您的資金：


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- 確保您已儲存 Lightning Wallet 的還原字詞和密碼。
- 保持您的系統為最新版本。



## 目前的故障排除


### 常見問題




- bitcoind 連線錯誤** ：檢查您的 RPC 登入詳細資料
- 同步受阻** ：檢查您的網際網路連線
- 權限錯誤**：檢查資料夾`~/.LND`的權限




那麼，您已經走到了本教程的最後。如果您想了解更多關於 Lightning 的資訊，我們提供了這個入門課程，讓您更了解 Lightning Network 背後的概念和實務。




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb