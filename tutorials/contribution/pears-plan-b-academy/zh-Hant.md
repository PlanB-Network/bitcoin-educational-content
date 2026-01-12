---
name: Plan ₿ Academy - Pears App
description: 如何在 Pears 上安裝和使用 Plan ₿ Academy 應用程式？
---

![cover](assets/cover.webp)


您可能已經知道 Plan ₿ Academy 是專門用於 Bitcoin 的最大教育資料庫，匯集了課程、教學和數以千計的開放源碼資源。最初，Plan ₿ Academy 是一個網站。但如果您無法再正常存取，例如在審查的情況下，會發生什麼事？


在本教程中，我們將學習如何使用**Pears**以真正可抵抗審查的方式執行**Plan ₿ Academy**平台，**Pears**是由**Holepunch**開發、**Tether**支援的點對點 (P2P) 技術。


Pears 是一款軟體，讓我們可以不依賴集中式網站來執行 Plan ₿ Academy 平台。在本教程中，我們將在您的電腦上安裝 Pears，以便透過 Pears 存取 Plan ₿ Academy。


Pears 的目標很簡單：讓發佈和使用網路應用程式成為可能，而無需依賴任何集中式基礎架構 (無伺服器、無主機、無中介)。換句話說，即使雲端供應商關閉或某個國家封鎖某個網域，應用程式仍可繼續存在於網路的同儕之間。這種方式讓我們的教育平台 Plan ₿ Academy 可以在全球範圍內存取，沒有單點故障。


---

**TL;DR:**



- 安裝梨；



- 執行下列指令啟動 Plan ₿ Academy 應用程式：


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1.梨是什麼？


Pears 是點對點應用程式的運行環境、開發工具和部署平台。這個開放原始碼的工具讓您可以在沒有伺服器或基礎架構的情況下，直接在使用者之間建立、分享及執行軟體。在實際應用上，這表示每個使用者不再是將應用程式寄存在中央伺服器上，而是成為網路中的一個節點：他們與其他對等使用者分享部分應用程式和資料。整個系統形成了一個分散式網路，其中每個實例相互合作以保持服務的可存取性。


![Image](assets/fr/01.webp)


此方法以 Holepunch 所開發的一套模組化軟體元件為基礎：



- Hypercore**：分散式日誌，可確保資料的一致性與安全性，無需中央資料庫。
- Hyperbee**：建置在 Hypercore 之上的索引，可讓資料有效率地組織與查詢。
- Hyperdrive**：分佈式檔案系統，用於在對等體之間儲存和同步應用程式檔案。
- Hyperswarm** 和 **HyperDHT**：網路層，無需中央伺服器即可在全球範圍內進行對等體發現與連線。
- Secretstream**：端對端加密通訊協定，可確保對等體之間的通訊安全。


透過結合這些元件，Pears 可建立自主、加密和分散式的應用程式，讓每位使用者都能積極參與網路。這種分散式架構消除了基礎設施成本、審查風險和 SPOF（*單點故障*）。


Pears 由 Holepunch 開發，該公司由 Mathias Buus 和 Paolo Ardoino（Tether 的 CEO 和 Bitfinex 的 CTO）創立，其使命是將點對點邏輯延伸至 Bitcoin 以外。他們的目標是建立「*對等互聯網*」，讓每個應用程式都能在沒有允許、沒有伺服器、沒有中間人的情況下運作。Holepunch 背後已有 **Keet**，這是一個完全 P2P 的視訊會議和訊息應用程式。


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*根據您的作業系統，本 Pears 安裝教程分為多個部分。請直接前往與您的環境相對應的章節，按照適當的指示進行操作： *



- Linux (Debian)** → 第 **2 節**
- 視窗** → 第 **3 節**
- macOS** → 第 **4 節**


## 2.如何在 Linux (Debian) 上安裝 Pears？


在 Debian 上安裝 Pears 相對簡單，但需要一些先決條件，我們將在本節中詳細說明。


### 2.1.更新系統


在做任何其他事情之前，確保您的系統是最新版本是很重要的。


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2.安裝相依性


Pears 依賴一些系統函式庫，包括 Bare JavaScript runtime 引擎使用的 `libatomic1`。使用下列指令安裝：


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3.透過 NVM 安裝 Node.js 和 npm


Pears 透過 *npm*（*Node.js* 套件管理程式）發行。雖然 Pears 並不直接依賴 *Node.js* 執行，但在安裝時需要使用 *Node.js* 。在 Linux 上安裝 *Node.js* 的建議方式是透過 *NVM* (*Node Version Manager*)，它允許您同時管理多個版本的 Node。


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


然後，重新載入您的終端機，啟動 *NVM*：


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


檢查 *NVM* 是否已正確安裝：


```bash
nvm --version
```


![Image](assets/fr/06.webp)


接下來，安裝 *Node.js* 的穩定版本 (例如目前的 LTS 版本)：


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


確認 *Node.js* 和 *npm* 已正確安裝：


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4.使用 npm 安裝 Pears


一旦 *npm* 可用，您就可以在系統上全局安裝 Pears CLI。這可讓您從任何目錄執行 `pear` 指令。


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5.初始化梨


安裝完成後，只要在終端機執行下列指令即可：


```bash
pear
```


首次啟動時，Pears 會連接到對等網路下載必要的元件。這個過程不依賴任何中央伺服器 - 檔案會直接從其他對等網路擷取。


![Image](assets/fr/10.webp)


下載完成後，再次執行指令確認一切正常：


```bash
pear
```


![Image](assets/fr/11.webp)


如果一切安裝正確，Pears 的說明功能表就會顯示可用的指令清單。


### 2.6.用 Keet 測試梨


要驗證 Pears 是否完全運作正常，您可以啟動網路中現有的 P2P 應用程式，例如 Keet，這是由 Holepunch 開發的開放原始碼訊息和視訊會議軟體。


```bash
pear run pear://keet
```


此命令直接從 Pears 網路載入 Keet 應用程式，而不使用中央伺服器。如果 Keet 能正確啟動，就表示您的 Pears 安裝已完全正常。


![Image](assets/fr/12.webp)


您的 Linux 系統現在就可以使用 Pears 運行和託管點對點應用程式了。


## 3.如何在 Windows 上安裝 Pears


在 Windows 上安裝 Pears 和在 Linux 上一樣簡單，但需要一些特定的工具。


*如果您使用 Linux 且已安裝 Pears，您可以直接跳到 **步驟 5**.* 。


### 3.1.以管理員身份開啟 PowerShell


首先，以管理員權限啟動 PowerShell：



- 按一下「開始」功能表；
- 輸入「PowerShell」；
- 用滑鼠右鍵按一下「*Windows PowerShell*」；
- 選擇「*以管理員身分執行*」。


![Image](assets/fr/15.webp)


### 3.2.下載 NVS


Pears 是透過 *npm* (*Node.js* 套件管理程式) 安裝的。在 Windows 上，Holepunch 建議的方法是使用 *NVS* (*Node Version Switcher*)，在這個系統上，*NVS* 比 *NVM* 更穩定。


在 PowerShell 中，執行下列指令以安裝最新版本的 *NVS*：


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3.安裝 Node.js


安裝完成後，重新啟動 PowerShell，然後輸入下列指令：


```powershell
nvs
```


您應該會看到可用的 *Node.js* 版本清單。按下鍵盤上的 `a` 鍵，選擇第一個版本。


![Image](assets/fr/17.webp)


*Node.js* 已安裝。


![Image](assets/fr/18.webp)


### 3.4.驗證安裝


確保 *Node.js* 和 *npm* 可被存取：


```powershell
node -v
npm -v
```


這兩個指令都應該會回傳版本號碼。


![Image](assets/fr/19.webp)


### 3.5.使用 npm 安裝 Pears


一旦 *Node.js* 和 *npm* 可用，請在系統上全域安裝 **Pears CLI**：


```powershell
npm install -g pear
```


這會將 `pear` 二進位檔安裝在您的全域 *npm* 目錄中。


![Image](assets/fr/20.webp)


### 3.6.驗證和初始化 Pears


安裝完成後，執行：


```powershell
pear
```


首次啟動時，Pears 會自動從點對點網路下載所需的元件。這個過程可能需要一些時間。


![Image](assets/fr/21.webp)


如果一切順利，您應該可以看到 Pears CLI 的說明功能表，以及可用的子指令清單 (run、seed、info...)。


### 3.7.用 Keet 測試梨


要驗證 Pears 是否完全運作，您可以啟動網路中現有的 P2P 應用程式，例如 Keet - 由 Holepunch 開發的開放原始碼訊息和視訊會議軟體。


```bash
pear run pear://keet
```


此命令直接從 Pears 網路載入 Keet 應用程式，而不使用任何中央伺服器。如果 Keet 成功啟動，表示您的 Pears 安裝已完全正常。


![Image](assets/fr/22.webp)


您的 Windows 系統現在已準備就緒，可以使用 Pears 執行和託管點對點應用程式。


## 4.如何在 macOS 上安裝 Pears


在 macOS 上安裝 Pears 與 Linux 相似，但需要針對 Apple 環境進行一些特定的調整。讓我們一起完成這些步驟。


*如果您使用 Linux 或 Windows 並已安裝 Pears，您可以直接跳到 **步驟 5***.*


### 4.1.檢查系統先決條件


安裝前，請確認您的系統已安裝 *Xcode Command Line Tools*。此套件為 *Node.js* 及其相依性提供必要的建立工具。


為此，請使用快捷鍵 `Cmd + 空格鍵`開啟終端機，輸入 `終端機`，然後按下 `Enter`。然後，在終端機執行以下指令進行安裝：


```bash
xcode-select --install
```


如果工具已安裝在您的系統上，macOS 會通知您。


### 4.2.安裝 NVM


Pears 透過 *npm*（*Node.js* 套件管理程式）發行。雖然 Pears 並不直接依賴 *Node.js* 來運作，但在安裝時需要使用 *Node.js* 。在 macOS 上安裝 *Node.js* 的建議方法是 *NVM* (*Node Version Manager*)，它允許你同時管理多個 Node 版本。


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


然後重新載入您的終端機，啟動 *NVM*：


```bash
source ~/.zshrc
```


如果您使用 *bash* 而非 *zsh*，請執行：


```bash
source ~/.bashrc
```


接下來，檢查 *NVM* 是否安裝正確：


```bash
nvm --version
```


您的終端機應該會顯示已安裝的 *NVM* 版本。


### 4.3.安裝 Node.js 和 npm


接下來，安裝 *Node.js* 的穩定版本 (例如目前的 LTS 版本)：


```bash
nvm install --lts
```


安裝完成後，請驗證安裝的版本：


```bash
node -v
npm -v
```


這兩個指令都應該會回傳一個版本號碼。


### 4.4.使用 npm 安裝 Pears


一旦 *npm* 可用，您就可以在系統上全局安裝 Pears CLI。這將允許您從任何目錄執行 `pear` 指令。


```bash
npm install -g pear
```


### 4.5.初始化梨


安裝完成後，只要在終端機執行下列指令即可：


```bash
pear
```


首次啟動時，Pears 會連接到對等網路來下載必要的元件。這個過程不需要任何中央伺服器 - 檔案會直接從其他對等網路擷取。


下載完成後，重新執行指令以驗證一切正常：


```bash
pear
```


如果一切安裝正確，Pears 的說明功能表就會顯示可用的指令清單。


### 4.6.用 Keet 測試梨


要驗證 Pears 是否完全運作，您可以啟動網路中已有的 P2P 應用程式，例如 Keet，這是 Holepunch 的開放原始碼訊息和視訊會議軟體。


```bash
pear run pear://keet
```


此命令直接從 Pears 網路載入 Keet 應用程式，而不使用中央伺服器。如果 Keet 成功啟動，表示您的 Pears 安裝已完全運作。


您的 macOS 系統現在已準備就緒，可以使用 Pears 執行和託管點對點應用程式。


## 5.如何在梨上使用 Plan ₿ 學院


安裝並執行 Pears 後，您可以透過 P2P 網路直接啟動 **Plan ₿ Academy** 平台。只需在您的終端機執行以下指令 (相同指令適用於 Linux、Windows 及 macOS)：


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


載入完成後，Plan ₿ Academy 將會在您的 Pears 環境中開啟，就像原始網站一樣可隨時使用 - 但不需依賴中央伺服器。


![Image](assets/fr/14.webp)


## 6.如何進行種子計劃 ₿學院對梨的研究


在 Pears 網路中，*seed* 一個應用程式意味著從您自己的機器將它重新分配給其他對等機。實際上，當您 seed Plan ₿ Academy 時，您的電腦就會成為一個資料來源，讓其他使用者可以下載應用程式，而不需要仰賴中央伺服器。


這個機制強化了我們的應用程式在 Pears 網路上的彈性和抗檢查能力。seed 應用程式的對等人越多，它的可用性和分散性就越高，即使某些原始節點離線也沒問題。


若要協助分發 Plan ₿ Academy，只需執行下列指令：


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


只要此指令保持作用中，您的裝置就會參與分發應用程式的檔案。如果您關閉終端機，分享程序就會停止。


若要在重新啟動後繼續播種，您可以在背景執行指令或建立系統服務 - 例如 Linux 上的 systemd 服務、macOS 上的 LaunchAgent 或 Windows 上的排程工作。這些方法可確保 Plan ₿ Academy 應用程式在系統啟動時自動恢復播種。


感謝您為 Pears 上的「Plan ₿學院」分散式散佈做出貢獻，並協助 Bitcoin 教育成為真正的抗檢查教育！