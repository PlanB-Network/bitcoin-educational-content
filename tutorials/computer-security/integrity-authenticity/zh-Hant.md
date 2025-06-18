---
name: GnuPG
description: 如何驗證軟體的完整性和真實性？
---
![cover](assets/cover.webp)


下載軟體時，確保其未經修改且確實來自官方來源是非常重要的。對於與 Bitcoin 相關的軟體尤其如此，例如 Wallet 軟體，可讓您確保金鑰的安全性，以存取您的資金。在本教程中，我們將介紹如何在安裝軟體之前驗證其完整性和真實性。我們將以 Sparrow Wallet 為例，這是比特幣玩家最喜歡的 Wallet 軟體，但對於任何其他軟體，操作步驟都是一樣的。


驗證完整性包括將下載檔案的數位指紋 (即 Hash) 與官方開發人員提供的指紋進行比較，以確保檔案未被修改。如果兩者相符，就表示檔案與原始檔案完全相同，並未被攻擊者破壞或修改。


另一方面，驗證真實性可確保檔案確實來自官方開發人員，而非冒名者。這是透過驗證數位簽章來完成的。此簽章可證明軟體是以合法開發者的私人金鑰簽章。


如果未執行這些檢查，就有安裝包含修改程式碼的惡意軟體的風險。這些程式碼可能會竊取個人金鑰等資訊，或是阻止存取您的檔案。這類型的攻擊相當常見，尤其是在開放原始碼軟體的情況下，偽造版本可能被散佈。


為了執行此驗證，我們將使用兩個工具：散列函式驗證完整性，以及實作 PGP 通訊協定的開放原始碼工具 GnuPG 來驗證真實性。


## 先決條件


如果您使用的是**Linux**，GPG 已預先安裝在大多數發行版本上。如果沒有，您可以使用下列指令安裝：


```bash
sudo apt install gnupg
```


對於 **macOS**，如果您尚未安裝 Homebrew 套件管理程式，請使用下列指令安裝：


```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```


```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```


然後使用此指令安裝 GPG：


```bash
brew install gnupg
```

對於 **Windows **，如果您沒有 GPG，可以安裝 [Gpg4win](https://www.gpg4win.org/) 軟體。

![GnuPG](assets/notext/01.webp)


## 下載文件


首先，我們需要各種文件。訪問 [Sparrow Wallet 在 "*Download*" 部分的官方網站](https://sparrowwallet.com/download/)。如果您希望驗證其他軟體，請前往該軟體的網站。


![GnuPG](assets/notext/02.webp)


您也可以前往 [該專案的 GitHub 儲存庫](https://github.com/sparrowwallet/sparrow/releases)。


![GnuPG](assets/notext/03.webp)


下載與您作業系統相對應的軟體安裝程式。


![GnuPG](assets/notext/04.webp)


您也需要檔案的 Hash，通常稱為「*SHA256SUMS*」或「*MANIFEST*」。


![GnuPG](assets/notext/05.webp)


同時下載檔案的 PGP 簽署。這是 `.asc` 格式的文件。


![GnuPG](assets/notext/06.webp)


確保將所有這些檔案放置在同一個資料夾中，以便執行下列步驟。


最後，您需要開發人員的公開金鑰，我們將用它來驗證 PGP 簽署。這個金鑰通常可以在軟體的網站、專案的 GitHub 儲存庫、有時在開發者的社群媒體，或是 Keybase 之類的專門網站找到。以 Sparrow Wallet 為例，您可以在 [Keybase](https://keybase.io/craigraw) 上找到開發者 Craig Raw 的公開金鑰。若要直接從終端下載，請執行指令：


```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```


![GnuPG](assets/notext/07.webp)


## 驗證簽名


驗證簽章的過程在**Windows**、**macOS**和**Linux**上都是一樣的。一般而言，您已在上一步匯入公開金鑰，但如果尚未匯入，請使用下列指令匯入：


```bash
gpg --import [key path]
```


以開發者公開金鑰檔案的位置取代 `[金鑰路徑]`。


![GnuPG](assets/notext/08.webp)


使用下列指令驗證簽章：


```bash
gpg --verify [file.asc]
```


將 `[file.asc]` 改為簽章檔案的路徑。在 Sparrow 的情況下，此檔案在版本 2.0.0 時稱為 "*sparrow-2.0.0-manifest.txt.asc*"。


![GnuPG](assets/notext/09.webp)


如果簽章有效，GPG 會向您指出。然後您就可以進入下一步，因為這確認了檔案的真實性。


![GnuPG](assets/notext/10.webp)


## 驗證 Hash

既然已確認軟體的真實性，也就有必要驗證其完整性。我們會比較軟體的 Hash 與開發者提供的 Hash。如果兩者相符，則保證軟體程式碼未被竄改。


在**Windows**上，開啟終端機並執行下列指令：


```bash
CertUtil -hashfile [file path] SHA256 | findstr /v "hash"
```


以安裝程式的位置取代 `[檔案路徑]`。


![GnuPG](assets/notext/11.webp)


終端將傳回下載軟體的 Hash。


![GnuPG](assets/notext/12.webp)


請注意，對於某些軟體，可能需要使用不同於 SHA256 的 Hash 函式。在這種情況下，只需在指令中取代 Hash 函式的名稱即可。


然後將結果與檔案 "*sparrow-2.0.0-manifest.txt*" 中的相應值進行比較。


![GnuPG](assets/notext/13.webp)


在我的案例中，我們看到兩個哈希值完全符合。


在 **macOS** 和 **Linux** 上，Hash 驗證程序是自動執行的。不需要像在 Windows 上一樣，手動檢查兩個哈希值之間的匹配。


只要在**macOS**上執行此指令即可：


```bash
shasum --check [file name] --ignore-missing
```


以安裝程式的名稱取代 `[檔案名稱]`。例如，對於 Sparrow Wallet：


```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```


如果哈希值匹配，您應該會看到以下輸出：


```bash
Sparrow-2.0.0.dmg: OK
```


在**Linux**上，指令類似：


```bash
sha256sum --check [file name] --ignore-missing
```


如果哈希值匹配，您應該會看到以下輸出：


```bash
sparrow_2.0.0-1_amd64.deb: OK
```


現在您可以放心，您所下載的軟體是正確且完整的。您可以繼續在您的電腦上安裝。


如果您覺得本教學對您有幫助，請在下方豎起大拇指。歡迎在您的社交網路分享這篇文章。非常感謝您！


我也建議您看看 VeraCrypt 的其他教學，這是一款可以加密和解密儲存裝置的軟體。


https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5