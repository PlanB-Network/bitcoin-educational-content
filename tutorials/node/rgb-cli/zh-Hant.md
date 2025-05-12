---
name: RGB CLI
description: 如何在 RGB 上建立和 Exchange 智慧型契約？
---
![cover](assets/cover.webp)


在本教學中，我們將使用 LNP/BP 協會所建立的命令列工具 `RGB`，一步一步地撰寫 Contract。目的是展示如何安裝和操作 CLI、編譯 Schema、匯入 Interface 和 Interface Implementation，然後發出 RGB 資產。我們還會瞭解底層邏輯，包括編譯和狀態驗證。本教學結束時，您應該可以重現流程並建立自己的 RGB 契約。


## RGB 協定提醒


RGB 是運行在 Bitcoin 之上的協定，模擬 Smart contract 的功能和數位資產管理，而不會使其所依據的 Blockchain 負荷過重。與傳統的 On-Chain 智慧型契約（例如 Ethereum 上的契約）不同，RGB 依賴「*Client-side Validation*」系統：大部分的資料和狀態歷史都是由相關參與者專屬交換和儲存，而 Bitcoin Blockchain 只承載小型的加密承諾（透過 *Tapret* 或 *Opret* 等機制）。因此，在 RGB 通訊協定中，Bitcoin Blockchain 只扮演時間戳記伺服器和 Double-spending 保護系統的角色。


RGB Contract 的結構類似進化狀態機。它從 Genesis 開始，Genesis 根據嚴格類型化和編譯的 Schema 定義初始狀態（例如描述 Supply、報價器或其他元資料）。之後會應用狀態轉換（State Transitions），必要時還會應用狀態延伸（State Extensions），以修改或延伸此狀態。無論是轉移可替代資產 (RGB20) 或建立獨特資產 (RGB21)，每一個作業都涉及 * 單一使用封條*。這些封條可將 Bitcoin UTXOs 連結至 off-chain 狀態，並防止重複支出，同時確保保密性與可擴充性。


若要進一步瞭解 RGB 協定的運作方式，我建議您參加這個全面的訓練課程：


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

RGB 的內部邏輯是以 Rust 函式庫為基礎，身為開發者的您可以將這些函式庫匯入您的專案中，以管理 *Client-side Validation* 的部分。此外，LNP/BP 團隊正在開發其他語言的綁定，但尚未定案。此外，Bitfinex 等其他實體也在開發自己的整合堆疊，但我們會在另一篇教學中談到這些。就目前而言，`RGB` CLI 是官方參考，即使它仍然相對未經完善。


## 安裝和展示 RGB CLI 工具


主指令簡稱為「RGB」。它的設計讓人聯想到 `git`，有一組子指令用來操作契約、呼叫契約、發行資產等等。Bitcoin Wallet 目前尚未整合，但會在即將推出的版本 (0.11) 中整合。這個下一個版本將能讓使用者直接從 `RGB`創建和管理他們的錢包 (透過描述符)，包括 PSBT 的產生、與外部硬體 (例如 Hardware Wallet) 的相容性以進行簽章，以及與 Sparrow 等軟體的互通性。這將簡化整個資產發行和轉移方案。


### 透過貨運安裝


我們在 Rust 中安裝了 .NET 工具：


```bash
cargo install rgb-contracts --all-features
```


(注意：crate 名為 `RGB-contracts`，安裝的指令將命名為 `RGB`。如果已存在名為 `RGB` 的 crate，可能會有衝突，因此才會有這個名稱)


安裝過程中會編譯大量的相依性（例如指令解析、Electrum 整合、零知識證明管理等）。


安裝完成後，.NET 會自動啟動：


```bash
rgb
```


執行 `RGB`（不含參數）會顯示可用的子指令清單，例如 `interfaces`, `Schema`, `import`, `export`, `issue`, `Invoice`, `transfer` 等。您可以變更本機儲存目錄 (存放所有日誌、示意圖和實作的 Stash)、選擇網路 (Testnet、Mainnet) 或設定您的 Electrum 伺服器。


![RGB-CLI](assets/fr/01.webp)


### 控制的第一次概述


執行下列指令時，您會看到預設已整合了一個 `RGB20` Interface：


```bash
rgb interfaces
```


如果未整合此 Interface，請克隆 .NET Framework：


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


編譯它：


```bash
cargo run
```


然後匯入您選擇的 Interface：


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-CLI](assets/fr/02.webp)


但是，我們被告知目前還沒有 Schema 匯入軟體中。Stash 中也沒有 Contract。若要查看，請執行命令 ：


```bash
rgb schemata
```


然後，您可以複製儲存庫以擷取某些示意圖：


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-CLI](assets/fr/03.webp)


此儲存庫在其 `src/` 目錄中包含數個 Rust 檔案 (例如 `nia.rs`)，這些檔案定義模式 (NIA 代表 "*Non Inflatable Asset*「，UDA 代表 」*Unique Digital Asset*"，等等)。若要編譯，您可以執行 ：


```bash
cd rgb-schemata
cargo run
```


這會產生數個與已編譯示意圖相對應的「.RGB」和「.rgba」檔案。例如，您會找到 `NonInflatableAsset.RGB`。


### 匯入 Schema 和 Interface Implementation


現在您可以將原理圖匯入 `RGB` 中：


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-CLI](assets/fr/04.webp)


這會將它加入本機的 Stash。如果我們執行以下指令，就會發現 Schema 現在出現了：


```bash
rgb schemata
```


## 創建 Contract（發行）


有兩種方法可以建立新資產：




- 我們可以使用 Rust 中的腳本或程式碼，透過填充 Schema 欄位 (Global State、自有國家等) 來建立 Contract，並產生 `.RGB` 或 `.rgba` 檔案；
- 或直接使用 `issue` 子指令，並使用 YAML (或 TOML) 檔描述 token 的屬性。


您可以在 Rust 中的「examples」資料夾中找到範例，說明您如何建立「ContractBuilder」、填入「Global State」（資產名稱、股票代號、Supply、日期等）、定義 Owned State（指派給哪個 UTXO），然後將所有這些編譯成 *Contract Consignment*，您就可以匯出、驗證並匯入 Stash。


另一種方法是手動編輯 YAML 檔案，自訂 `ticker`、`name`、`Supply` 等。假設檔案名稱為 `RGB20-demo.yaml`。您可以指定 ：




- `spec`：股票代號、名稱、精確度 ；
- `條款'：一個用於法律通知的欄位 ；
- `issuedSupply` : 已發行的代幣數量 ；
- `assignments`: 表示 Single-Use Seal (*Seal Definition*) 和已解鎖的數量。


以下是要建立的 YAML 檔案範例：


```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```


![RGB-CLI](assets/fr/05.webp)


然後只要執行指令 ：


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-CLI](assets/fr/06.webp)


在我的情況中，唯一的 Schema 識別碼 (需用單引號括起）是 `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` 而且我沒有輸入任何發行商。所以我的訂單是 ：


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


如果您不知道 Schema ID，請執行命令 ：


```bash
rgb schemata
```


CLI 回覆說已經發出新的 Contract 並加入 Stash。如果我們鍵入以下指令，就會發現現在又多了一個 Contract，與剛發出的 Contract 對應：


```bash
rgb contracts
```


![RGB-CLI](assets/fr/07.webp)


接著，下一個指令會顯示全局狀態 (名稱、股票、Supply...) 和 Owned 狀態清單，也就是分配 (例如，在 UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1` 中定義的 100 萬個 `PBN` 代幣)。


```bash
rgb state '<ContractId>'
```


![RGB-CLI](assets/fr/08.webp)


## 匯出、匯入及驗證


若要與其他使用者分享 Contract，可從 Stash 匯出到 .NET 檔案：


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-CLI](assets/fr/09.webp)


您可以將 `myContractPBN.RGB` 檔案傳給其他使用者，他可以使用命令 ：


```bash
rgb import myContractPBN.rgb
```


匯入時，如果是簡單的 *Contract Consignment*，我們會收到「`Importing Consignment RGB`」訊息。如果是較大的 *State Transition Consignment*，指令會有所不同 (`RGB接受`)。


為了確保有效性，您也可以使用本機驗證功能。例如，您可以執行 ：


```bash
rgb validate myContract.rgb
```


### Stash 的使用、驗證和顯示


提醒一下，Stash 是模式、介面、實作和契約 (Genesis + 轉換) 的本地庫存。每次執行「匯入」，都會新增一個元素到 Stash。這個 Stash 可以用命令 ：


```bash
rgb dump
```


![RGB-CLI](assets/fr/10.webp)


這將 generate 一個資料夾，其中包含整個 Stash 的詳細資訊。


## 轉移和 PSBT


若要執行轉移，您需要操作本機 Bitcoin Wallet 來管理「Tapret」或「Opret」承諾。


### generate 和 Invoice


在大多數情況下，Contract 的參與者 (例如 Alice 和 Bob) 之間的互動是透過產生 Invoice 來進行的。如果 Alice 想要 Bob 執行某些事情 (代幣轉移、重新發行、DAO 中的動作等)，Alice 就會建立一個 Invoice 詳細說明她對 Bob 的指示。因此我們有 ：




- Alice** （Invoice 的發行人） ；
- 鮑勃**（接收並執行 Invoice）。


與其他生態系統不同，RGB Invoice 並不局限於付款的概念。它可以嵌入與 Contract 相關聯的任何請求：撤銷金鑰、投票、在 NFT 上建立雕刻 (*engraving*) 等。相應的操作可以在 Contract Interface 中描述。相應的操作可在 Contract Interface 中描述。


以下指令會產生 RGB Invoice：


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


與 ：




- `$Contract`：Contract 識別碼 (*ContractId*) ；
- `$Interface`：要使用的 Interface (例如 `RGB20`)；
- `$ACTION`：在 Interface 中指定的操作名稱 (對於簡單的可替代代幣轉移，可以是 "Transfer")。如果 Interface 已經提供預設動作，您不需要在此再次輸入；
- `$STATE`：要轉移的狀態資料（例如，如果轉移的是可替代代幣，則是代幣的數量）；
- `$Seal`：受益人（Alice）的 Single-Use Seal，即對 UTXO 的明確引用。Bob 將使用此資訊建立 Witness Transaction，而相對應的輸出就會屬於 Alice (以 *blinded UTXO* 或未加密的形式)。


例如，使用下列指令


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI 與 generate 和 Invoice 相似：


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


它可以透過任何管道 (文字、QR code 等) 傳送給 Bob。


### 進行轉移


若要從此 Invoice ：




- 鮑勃（在他的 Stash 中持有代幣）有一個 Bitcoin Wallet。他需要準備一個 Bitcoin 交易（以 PSBT 的形式，例如 `tx.PSBT`），花掉所需的 RGB 代幣所在的 UTXO，再加上一個 UTXO 作為貨幣 (Exchange) ；
- Bob 執行下列指令：


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- 這會產生一個 `Consignment.RGB` 檔案，其中包含 ：
 - 轉換歷史向 Alice 證明代用幣是真的；
 - 將代幣轉移到 Alice 的 Single-Use Seal 的新轉換；
 - A Witness Transaction（無符號）。
- Bob 將此`Consignment.RGB`檔傳送給 Alice (透過電子郵件、分享伺服器或 RGB-RPC 通訊協定、Storm 等)；
- Alice 接收 `Consignment.RGB` 並在自己的 Stash 中接受它：


```bash
alice$ rgb accept consignment.rgb
```




- CLI 會檢查轉換的有效性，並將其加入 Alice 的 Stash。如果無效，指令會失敗，並帶有詳細的錯誤訊息。否則，它會成功，並報告樣本交易尚未在 Bitcoin 網路上廣播（Bob 正在等待 Alice 的 Green 指示燈）；
- 為了確認，`accept` 指令會傳回一個簽章 (*payslip*)，Alice 可以將這個簽章傳送給 Bob，向他顯示她已經確認了 *Consignment* ；
- 鮑勃就可以簽署並發佈 (`--publish`)他的 Bitcoin 交易：


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- 此交易一經 On-Chain 確認，資產的 Ownership 即視為轉移給 Alice。Alice 的 Wallet 監控交易的 Mining，看到新的 Owned State 出現在其 Stash 中。


您現在知道如何發行和轉移 RGB Contract。如果您覺得這篇教學有用，請在下方寫上 Green 的拇指，我會非常感激。請隨時在您的社交網絡上分享這篇文章。非常感謝


我也推薦這份教學，其中我介紹了如何啟動一個 RGB 相容的 Lightning 節點到 Exchange 代幣，幾乎是瞬間完成：


https://planb.network/tutorials/node/others/rln-ffc02528-329b-4e16-bd83-873d0299feea