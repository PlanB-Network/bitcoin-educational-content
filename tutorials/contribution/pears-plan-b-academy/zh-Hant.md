---
name: 地圖 ₿ 學院 - Pears App
description: 如何在 Pears 上安裝和使用 Plan ₿ Academy 應用程式？
---

![cover](assets/cover.webp)



您可能知道，Plan ₿ Academy 是專門針對 Bitcoin 的最大教育資料庫，匯集了課程、教學和數以千計以開放授權方式發表的資源。最初，Plan ₿ Academy 是一個網站。但如果您無法再正常存取，例如在審查的情況下，會發生什麼事？



在本教程中，我們將學習如何運行**Plan ₿ Academy**平台，這要歸功於**Pears**，這是一種由**Holepunch**開發，並由**Tether**支援的點對點 (P2P) 技術，是一種真正不可感知的方式。



Pears 是一款軟體，可讓我們在不依賴中央網站的情況下運行 Plan ₿ Academy 平台。在本教程中，我們將在您的電腦上安裝 Pears，以便透過 Pears 存取 Plan ₿ Academy。



Pears 的目標很簡單：讓無需依賴任何集中式基礎架構（無伺服器、無主機、無中介）即可散佈與使用網路應用程式成為可能。換句話說，即使雲端供應商倒閉或某個國家封鎖了某個網域，應用程式仍可在網路的同儕之間繼續運作。正是這種方式讓我們的教育平台 Plan ₿ Academy 可以在全球任何地方存取，沒有單點故障。



---

**TL;DR :**





- 安裝梨 ；





- 執行下列指令啟動 Plan ₿ Academy 應用程式：



```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



---

## 1.安裝梨



### 1.1 什麼是梨？



Pears 是點對點應用程式的運行環境、開發工具和部署平台。這個開放原始碼的工具使得在沒有伺服器或基礎架構的情況下，直接在使用者之間建立、分享和執行軟體成為可能。具體來說，這意味著每個使用者不再將應用程式寄存在中央伺服器上，而是成為一個網路節點，與其他對等者分享部分應用程式和資料。整個系統形成了一個分散式網路，每個實例都相互合作以保持服務的可存取性。



![Image](assets/fr/01.webp)



此方法是以 Holepunch 所開發的一套模組化軟體磚塊為基礎：




- Hypercore**：分散式日誌，可在沒有中央資料庫的情況下保證資料的一致性與安全性。
- Hyperbee**：Hypercore 之上的索引器，用於有效率的資料組織與瀏覽。
- Hyperdrive**：分佈式檔案系統，用於在對等體之間儲存和同步應用程式檔案。
- Hyperswarm** 和 **HyperDHT**：網路層，可在全球範圍內的對等體之間進行發現和連接，無需中央伺服器。
- Secretstream**：E2E 加密通訊協定，可確保兩個對等體之間的交換安全。



透過結合這些元件，Pears 可以建立自主、加密和分散式的應用程式，讓每位使用者都能積極參與網路。這種分散式架構消除了基礎設施成本、審查風險和 SPOF（*單點故障*）。



Pears 由 Holepunch 開發，該公司由 Mathias Buus 和 Paolo Ardoino（Tether 的 CEO 和 Bitfinex 的 CTO）創立，其使命是將點對點邏輯延伸至 Bitcoin 以外。他們的目標是建立「點對點網際網路」，讓每個應用程式都能在沒有授權、沒有伺服器、沒有中間人的情況下運作。Holepunch 背後已有 **Keet**，這是一個完全 P2P 的視訊會議和訊息應用程式。



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*根據您的作業系統，本 Pears 安裝教程分為幾個部分。請直接前往與您的環境相對應的章節，按照適當的指示進行操作： *




- Linux (Debian)** → Part **1.2.**
- 視窗** → 部分 **1.3.**
- macOS** → 部分 **1.4.**




### 1.2 - 如何在 Linux (Debian) 上安裝 Pears？



在 Debian 系統上安裝 Pears 相對簡單，但需要一些先決條件，我們會在本節中詳細說明。



#### 1.2.1.更新系統



首先，最重要的是確保您的系統是最新的。



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



#### 1.2.2 安裝相依性



Pears 依賴許多系統函式庫，包括 Bare JavaScript runtime 使用的 `libatomic1`。使用下列指令安裝：



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



#### 1.2.3 透過 NVM 安裝 Node.js 和 npm



Pears 透過 *npm*（*Node.js* 套件管理程式）發行。雖然 Pears 並不直接依賴 *Node.js* 來運作，但它在安裝時是必要的。在 Linux 上安裝 *Node.js* 的建議方法是 *NVM* (*Node Version Manager*)，它允許您並行管理多個版本的 Node。



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



然後重新載入您的終端機，啟動 *NVM* ：



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



檢查 *NVM* 是否已安裝：



```bash
nvm --version
```



![Image](assets/fr/06.webp)



然後安裝 *Node.js* 的穩定版本 (例如目前的 LTS)：



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



檢查 *Node.js* 和 *npm* 安裝：



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



#### 1.2.4 使用 npm 安裝 Pears



一旦 *npm* 可用，您就可以在系統上全局安裝 Pears CLI。這將允許您從任何目錄執行 `pear` 指令。



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



#### 1.2.5.初始化梨



安裝完成後，只要在終端機執行下列指令即可：



```bash
pear
```



首次啟動時，Pears 會連接到對等網路下載必要的元件。這個過程不需要中央伺服器：檔案直接從其他對等網路取得。



![Image](assets/fr/10.webp)



下載完成後，再次執行指令以檢查是否一切正常：



```bash
pear
```



![Image](assets/fr/11.webp)



如果一切安裝正確，Pears Help 將顯示可用命令清單。



#### 1.2.6.用 Keet 測試梨



若要檢查 Pears 是否完全運作，您可以啟動網路中已有的 P2P 應用程式，例如 Keet，Holepunch 的開放原始碼訊息和視訊會議軟體。



```bash
pear run pear://keet
```



此命令直接從 Pears 網路載入 Keet 應用程式，而不經過中央伺服器。如果 Keet 正確啟動，您的 Pears 安裝就完全正常。



![Image](assets/fr/12.webp)



您的 Linux 系統現在就可以使用 Pears 運行和託管點對點應用程式了。



### 1.3 - 如何在 Windows 上安裝 Pears？



在 Windows 上安裝 Pears 和在 Linux 上一樣簡單，但需要一些特殊工具。



*如果您使用 Linux 並已安裝 Pears，則可直接進入步驟 2



#### 1.3.1.以管理員模式開啟 PowerShell



首先，以管理員權限執行 PowerShell：




- 按一下「開始」功能表；
- 輸入 PowerShell ；
- 用滑鼠右鍵按一下「*Windows PowerShell*」；
- 選擇「*以管理員身分執行*」。



![Image](assets/fr/15.webp)



#### 1.3.2.下載 NVS



Pears 是透過 *npm* (*Node.js* 套件管理程式) 安裝的。在 Windows 上，Holepunch 建議的方法是使用 *NVS* (*Node Version Switcher*)，在這個系統上，*NVS* 比 *NVM* 更穩定。



在 PowerShell 中，執行下列指令以安裝最新版本的 *NVS* ：



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



#### 1.3.3.安裝 Node.js



安裝完成後，重新啟動 PowerShell 並輸入下列指令：



```powershell
nvs
```



您應該會看到可用的 *Node.js* 版本清單。按下鍵盤上的 `a` 鍵，選擇第一個版本。



![Image](assets/fr/17.webp)



*已安裝 Node.js*。



![Image](assets/fr/18.webp)



#### 1.3.4.檢查安裝



確保 *Node.js* 和 *npm* 可被存取：



```powershell
node -v
npm -v
```



這兩個指令都必須傳回版本號碼。



![Image](assets/fr/19.webp)



#### 1.3.5.使用 npm 安裝 Pears



一旦 *Node.js* 和 *npm* 可用，請在系統上全域安裝 **Pears CLI**：



```powershell
npm install -g pear
```



這將會把 `pear` 二進位檔安裝到您的全域 *npm* 目錄中。



![Image](assets/fr/20.webp)



#### 1.3.6.檢查和初始化 Pears



安裝完成後，執行 ：



```powershell
pear
```



首次啟動時，Pears 會自動從點對點網路下載必要的元件。這個過程可能需要一些時間。



![Image](assets/fr/21.webp)



如果一切順利，您應該會看到 CLI Pears 說明畫面，其中列出可用的子指令 (run、seed、info...)。



#### 1.3.7.用 Keet 測試梨



若要檢查 Pears 是否完全運作，您可以啟動網路中已有的 P2P 應用程式，例如 Keet，Holepunch 的開放原始碼訊息和視訊會議軟體。



```bash
pear run pear://keet
```



此命令直接從 Pears 網路載入 Keet 應用程式，而不經過中央伺服器。如果 Keet 正確啟動，您的 Pears 安裝就完全正常。



![Image](assets/fr/22.webp)



您的 Windows 系統現在已準備就緒，可以使用 Pears 執行和託管點對點應用程式。



### 1.4.如何在 macOS 上安裝 Pears？



在 macOS 上安裝 Pears 與在 Linux 上安裝相似，但需要針對 Apple 環境進行一些特定的調整。讓我們一起來發現這些步驟。



*如果您使用 Linux 或 Windows 並已安裝 Pears，則可直接進入步驟 2



#### 1.4.1.檢查系統需求



在安裝之前，請確認系統上已存在 *Xcode Command Line Tools*。此套件提供 _Node.js_ 及其相依性所需的編譯工具。



為此，請使用鍵盤快捷鍵 `Cmd + Space bar` 開啟終端機，然後輸入 `Terminal` 並按下 `Enter` 鍵。然後您就可以在終端機中輸入此指令來啟動安裝：



```bash
xcode-select --install
```



如果工具已安裝在您的系統上，macOS 會通知您。



#### 1.4.2.安裝 NVM



Pears 透過 *npm*（*Node.js* 套件管理程式）發行。雖然 Pears 並不直接依賴 *Node.js* 來運作，但在安裝時必須使用 *Node.js* 。在 macOS 上安裝 *Node.js* 的建議方法是 *NVM* (*Node Version Manager*)，它允許您並行管理多個版本的 Node。



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



然後重新載入您的終端機，啟動 *NVM* ：



```bash
source ~/.zshrc
```



如果您使用 *bash* 而非 *zsh*，請執行 ：



```bash
source ~/.bashrc
```



然後檢查 *NVM* 是否已安裝：



```bash
nvm --version
```



終端機應該會回傳您系統上安裝的 *NVM* 版本。



#### 1.4.3 安裝 Node.js 和 npm



然後安裝 *Node.js* 的穩定版本 (例如目前的 LTS)：



```bash
nvm install --lts
```



安裝完成後，檢查已安裝的版本：



```bash
node -v
npm -v
```



這兩個指令都必須傳回版本號碼。



#### 1.4.4 使用 npm 安裝 Pears



一旦 *npm* 可用，您就可以在系統上全局安裝 Pears CLI。這將允許您從任何目錄執行 `pear` 指令。



```bash
npm install -g pear
```



#### 1.4.5.初始化梨



安裝完成後，只要在終端機執行下列指令即可：



```bash
pear
```



首次啟動時，Pears 會連接到對等網路下載必要的元件。這個過程不需要中央伺服器：檔案直接從其他對等網路取得。



下載完成後，再次執行指令以檢查是否一切正常：



```bash
pear
```



如果一切安裝正確，Pears Help 將顯示可用命令清單。



#### 1.4.6.用 Keet 測試梨



若要檢查 Pears 是否完全運作正常，您可以啟動網路中已有的 P2P 應用程式，例如 Keet，Holepunch 的開放原始碼訊息和視訊會議軟體。



```bash
pear run pear://keet
```



此命令直接從 Pears 網路載入 Keet 應用程式，而不經過中央伺服器。如果 Keet 正確啟動，您的 Pears 安裝就完全正常。



您的 macOS 系統現在已準備就緒，可使用 Pears 執行和託管點對點應用程式。



## 2.如何在梨上使用 Plan ₿ Academy？



一旦安裝並執行 Pears，您就可以透過 P2P 網路直接執行 **Plan ₿ Academy** 平台。只要在您的終端機執行下列指令即可（Linux、Windows 和 macOS 的指令相同）：



```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



![Image](assets/fr/13.webp)



上傳之後，Plan ₿ Academy 將會在您的 Pears 環境中開啟，就像在原始網站中一樣可以隨時使用，但不需要依賴中央伺服器。



![Image](assets/fr/14.webp)