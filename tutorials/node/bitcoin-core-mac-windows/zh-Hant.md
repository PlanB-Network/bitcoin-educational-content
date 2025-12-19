---
name: "Bitcoin Core (macOS & Windows)"
description: 在 Mac 或 Windows 上安裝 Bitcoin Core
---

![cover](assets/cover.webp)

在一般電腦上安裝 Bitcoin Core 是可以做到的，但並不理想。如果您不介意讓電腦全天候開著，那麼這樣就可以了。如果您需要關閉電腦，每次重新開機等待軟體同步就會變得很煩。


這些說明適用於 Mac 或 Windows 使用者。Linux 使用者很可能不需要我的協助，但 Linux 的使用說明與 Mac 非常相似。


## 開始清潔


理想情況下，您希望使用一台沒有惡意軟體的乾淨電腦。即使您使用的是 Hardware Wallet，惡意軟體也可能會騙走您的硬幣。


您可以將舊電腦擦乾淨，然後用作專用的 Bitcoin 電腦，或是購買專用的電腦/筆記型電腦。


## Hard 硬碟機


Bitcoin Core 會佔用您硬碟機上約 400 GB 的資料，而且還會持續增加。您可以使用內接式硬碟機，但也可以附加外接式 Hard 硬碟機。我會說明這兩種選項。理想情況下，您應該使用固態硬碟機。如果您有一台舊電腦，它內部可能沒有這種硬碟機。只要買一個 1 或 2 TB 的外接式固態硬碟機就可以了。一般的硬碟機也許能用，但最終可能會出問題，而且速度會慢很多。


![image](assets/fr/01.webp)


## 下載 Bitcoin Core


前往 Bitcoin.org（請確保您沒有前往 Bitcoin.com，那是 Roger Ver 所擁有的垃圾幣網站，騙人購買 Bitcoin Cash 而非 Bitcoin）。


到達那裡之後，奇怪的是，在哪裡取得軟體並不明顯。進入資源功能表，按一下「Bitcoin Core」，如下圖所示：


![image](assets/fr/02.webp)


這將帶您進入下載頁面：


![image](assets/fr/03.webp)


按一下「下載 Bitcoin Core」橘色按鈕：


![image](assets/fr/04.webp)


有多個選項可供選擇，視您的電腦而定。前兩個與本指南相關；在左邊欄上選擇 Windows 或 Mac。點選後會開始下載，很可能會下載到您的下載目錄。


## 驗證下載（第一部分）


您需要包含不同版本的哈希值的文件。此檔案曾在 Bitcoin.org 的下載頁面，但現在已移至 bitcoincore.org/en/download：


![image](assets/fr/05.webp)


您需要 SHA256 二進位雜湊檔案。此檔案包含 Bitcoin Core 各種下載套件的 SHA256 切細值。


接下來，我們需要 Hash Bitcoin Core 下載，並與檔案中所說的 Hash 應有的內容比較。然後我們就知道下載的內容和 bitcoincore.org 所預期的完全相同。


再次導覽到 Downloads 目錄，並執行此指令 (將 X 改為 Full node Bitcoin 下載檔案的正確名稱)：


```bash
shasum -a 256 XXXXXXXXXXXX # <--- FOR MAC
certutil -hashfile XXXXXXXXXXX SHA256 # <--- FOR WINDOWS
```


您將獲得 Hash 輸出。記下它，並與 SHA256SUMS 檔案中的 Hash 進行比較。


如果輸出完全相同，那麼您已經驗證沒有任何位元的資料被竄改過...幾乎是這樣。我們仍然需要確定 SHA256SUMS 檔案不是惡意的。


若要進行下一步，我們必須在電腦上安裝 gpg。


要做到這一點，請參閱我的 SHA256/gpg 指南，並滾動到 「下載 gpg 」部分的一半左右，然後尋找您的作業系統的副標題。然後再回到這裡。


## 取得公開金鑰


回到下載頁面，取得 SHA256 Hash 簽章檔案


![image](assets/fr/06.webp)


按一下並將檔案儲存到磁碟，最好是下載目錄。


此檔案包含不同人士對 SHA256SUMS 檔案的簽章。


我們需要首席開發人員 Wladimir J. van der Laan 的公開金鑰在我們電腦的鑰匙圈上。他的公開金鑰 ID 是

1 - 01ea 5486 de18 a882 d4c2 6845 90c8 019e 36c2 e964


將該文字複製到下列指令中：


```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```


在任何時候，您都可以使用此指令查看電腦的鑰匙圈中有哪些鑰匙：


```bash
gpg --list-keys
```


## 驗證下載（第二部分）


我們擁有公開金鑰，因此現在可以驗證 SHA256SUMS 檔案，其中包含 Bitcoin Core 下載的雜湊值，以及這些雜湊值的簽章。


再次開啟 Terminal 或 CMD，並確認已進入 Downloads 目錄。從那裡執行此指令：


```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```


第一個列出的檔案是簽章檔案的確切拼法。第二個列出的檔案應該是包含哈希值的文字檔案的確切拼法。兩個檔案應該在同一個目錄中，而且您需要在檔案的目錄中，否則，您必須輸入每個檔案的完整路徑。


這是您應該得到的輸出


![image](assets/fr/07.webp)


您可以忽略警告訊息 - 它只是在提醒您，您還沒有在密鑰部分與 Wladimir 會面，並親自詢問他的公開密鑰是什麼，然後告訴您的電腦要完全信任這個密鑰。


如果您收到此訊息，現在您知道 SHA256SUMS.asc 檔案在 Wladimir 簽署後未被篡改。


## 安裝 Bitcoin 核心


您應該不需要安裝程式的詳細說明。


![image](assets/fr/08.webp)


## 運行 Bitcoin 核心


在 Mac 上，您可能會收到警告（Apple 仍然反對 Bitcoin）


![image](assets/fr/09.webp)


按一下確定，然後開啟系統偏好設定


![image](assets/fr/10.webp)


按一下安全性與隱私權圖示：


![image](assets/fr/11.webp)


然後按一下「無論如何開啟」：


![image](assets/fr/12.webp)


錯誤會再次出现，但這次您可以使用「開啟」按鈕。按一下。


![image](assets/fr/13.webp)


Bitcoin Core 應該會載入，您會看到一些選項：


![image](assets/fr/14.webp)


在這裡您可以選擇使用預設路徑來下載 Blockchain，或是選擇您的外接式磁碟機。如果您要使用內接磁碟機，我建議您不要改變預設路徑，這樣會讓您在安裝其他軟體與 Bitcoin Core 溝通時更容易設定。


您可以選擇執行修剪過的節點，它可以節省空間，但會限制您的節點。無論如何，您反正都要下載整個 Blockchain 並進行驗證，所以如果您有足夠的空間，請保留下載的內容，如果可以避免的話，就不要修剪。


確認後，Blockchain 將開始下載。這需要很多天。


![image](assets/fr/15.webp)


如果您願意，可以關閉電腦再回來下載，不會造成任何損害。
