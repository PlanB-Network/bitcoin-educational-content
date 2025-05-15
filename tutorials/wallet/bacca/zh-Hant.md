---
name: 巴卡
description: 在沒有 Ledger Live 軟體的情況下設定 Ledger
---
![cover](assets/cover.webp)


如果你使用的是Ledger，你可能已經發現你必須通過Ledger Live軟件，至少在初始設備配置時，要檢查它的真實性，並在上面安裝Bitcoin應用程序。然而，在這一配置之後，許多比特幣玩家更喜歡使用專門的 Bitcoin Wallet 管理軟件，如 Sparrow 或 Liana，而不是 Ledger Live。雖然 Ledger 生產的硬體錢包非常優秀，能快速包含最新的 Bitcoin 功能，但他們的軟體不一定能適應比特幣玩家的特殊需求。事實上，Ledger Live 包含許多專為替代幣設計的功能，而專門用於 Bitcoin Wallet 管理的選項卻很有限。但 Sparrow 和 Liana（目前）的問題是，它們不允許您在 Ledger 上安裝 Bitcoin 應用程式。


若要繞過在 Ledger 初期設定時使用 Ledger Live 的需要，您可以使用 Bacca 工具，（或稱「Ledger 安裝程式」）。此軟體可讓您安裝和更新 Bitcoin 應用程式、驗證 Ledger 的真實性，甚至稍後更新裝置的韌體。Bacca 是由 Chaincode Labs 的 Bitcoin Core 開發人員、[Revault 和 Liana](https://wizardsardine.com/) 的共同創辦人 Antoine Poinsot (Darosior) 和 Pythcoiner 所創造。


在本教程中，我將教您如何使用此工具，讓您可以永遠不用 Ledger Live 軟體，也能享受 Ledger 裝置的樂趣。它適用於所有裝置：Nano S Classic、Nano S Plus、Nano X、Flex 和 Stax。


---
*請注意，此工具相當新，其開發人員說明它仍處於**測試階段。他們建議僅將此工具用於測試目的，而非用於承載真正 Bitcoin Wallet 的裝置，儘管這是可能的。在這方面，我建議您遵循此工具開發人員的建議，這些建議已在 [其 GitHub 儲存庫的 README](https://github.com/darosior/ledger_installer).* 中註明。


---
## 先決條件


在電腦上，您需要兩個工具來使用 Bacca：




- Git ；
- Rust.


如果您已經安裝，則可以跳過此步驟。


**Linux:**


在 Linux 發行版本中，Git 通常已預先安裝。要檢查系統上是否已安裝 Git，可以在終端機中輸入以下命令 ：


```bash
git --version
```


如果您的系統上沒有安裝 Git，以下是在 Debian ：


```bash
sudo apt install git
```


最後，要安裝 Rust 開發環境，請使用 ：


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


**視窗：**


要安裝 Git，請前往 [該專案的官方網站](https://git-scm.com/)。下載軟體，並依照安裝說明進行。


![BACCA](assets/fr/01.webp)


以相同方式從 [官方網站](https://www.Rust-lang.org/tools/install) 安裝 Rust。


![BACCA](assets/fr/02.webp)


**MacOS:**


如果您的系統尚未安裝 Git，請開啟終端機，執行下列指令來安裝：


```bash
git --version
```


如果您的系統上未安裝 Git，則會開啟一個視窗，讓您安裝包含 Git 的 Xcode。只需按照螢幕上的指示繼續安裝即可。


若要安裝 Rust，請執行下列指令：


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


## 巴卡安裝


開啟終端機，進入要儲存軟體的資料夾，然後執行下列指令：


```bash
git clone https://github.com/darosior/ledger_installer.git
```


導覽到軟體目錄：


```bash
cd ledger_installer
```


然後使用 Cargo 來編譯專案並執行 Bacca GUI：


```bash
cargo run -p ledger_manager_gui
```


現在您可以存取軟體 Interface。


![BACCA](assets/fr/03.webp)


## 設定 Ledger


在您開始之前，如果您的 Ledger 是新的，請確認您已設定 PIN 碼並儲存復原短語。這些初始步驟不需要 Ledger Live。只要透過 USB 傳輸線連接 Ledger 供電即可。如果您不確定如何進行這兩個步驟，您可以參考您機型的特定教學開頭：


https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## 使用 Bacca


將您的 Ledger 連接到電腦，並使用您設定的 PIN 碼解鎖。Bacca 應該會自動偵測到您的 Ledger。


![BACCA](assets/fr/04.webp)


若要確認您 Ledger 的真實性，請按一下「*檢查*」按鈕。您需要在 Ledger 裝置上授權連線才能繼續。


![BACCA](assets/fr/05.webp)


Bacca 隨後會通知您 Ledger 是否為真品。如果不是正品，則表示裝置已遭破解或為仿冒品。在這種情況下，請立即停止使用。


![BACCA](assets/fr/06.webp)


在「*Apps*」功能表中，您可以查詢 Ledger 上已安裝的應用程式清單。


![BACCA](assets/fr/07.webp)


若要安裝 Bitcoin 應用程式，請按一下「*安裝*」，然後授權安裝在您的 Ledger 上。


![BACCA](assets/fr/08.webp)


應用程式安裝良好。


![BACCA](assets/fr/09.webp)


如果您沒有安裝最新版本的 Bitcoin 應用程式，Bacca 會顯示「*更新*」按鈕，而不是「*最新*」指示。只需按一下此按鈕即可更新應用程式。


![BACCA](assets/fr/10.webp)


現在，您的 Ledger 已經正確設定為最新版本的 Bitcoin 應用程式，您就可以在 Sparrow 或 Liana 等管理軟體上匯入並使用您的 Wallet，而無需透過 Ledger Live！


如果您認為本教學有用，請在下方留下 Green 拇指。歡迎在您的社交網路分享這篇文章。非常感謝


我也建議您看看這篇 GnuPG 的教學，其中說明了如何在安裝軟體之前檢查軟體的完整性與真實性。這是很重要的做法，尤其是在安裝 Wallet 管理軟體，例如 Liana 或 Sparrow ：


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc