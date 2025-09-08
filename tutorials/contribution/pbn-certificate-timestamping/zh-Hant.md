---
name: Plan ₿ Network 文憑時間戳
description: 瞭解 Plan ₿ Network 如何為您的證書和文憑簽發可驗證的證明
---

![cover](assets/cover.webp)


如果您正在閱讀這篇文章，您很有可能已收到₿-CERT 測試證書或您在 planb.network 上所參加課程的結業證書，恭喜您的成就！


在本教程中，我們將發現 Plan ₿ Network 如何為您的₿-CERT 測試證書或任何有關課程完成的文憑簽發可驗證的證明。然後，在第二部分中，我們將描述如何驗證這些證明的真實性。


# Plan ₿ Network 驗證機制


在 Plan ₿ Network，我們以加密方式簽署證書和文憑，並透過依賴兩種加密運算的證明機制，使用時間鏈 (即 Bitcoin Blockchain)，為證書和文憑加上時間戳記：


1.綜合您的成就的文字檔上的 GPG 簽署

2.透過 [opentimestamps](https://opentimestamps.org/)，為同一個已簽署檔案加上時間戳記。


第一個作業可讓您確認證書（或文憑）的簽發者，第二個作業可讓您驗證證書的簽發日期。

我們相信，這個簡單的證明機制讓我們有能力簽發任何人都能獨立驗證的證書和文憑，並提供不可推翻的證據。


![image](./assets/proof-mechanism.webp)


有了這個證明機制，任何試圖篡改證書或畢業證書的行為，即使是最微小的細節，都會導致已簽署檔案的 SHA-256 Hash 完全不同，立即揭露任何篡改行為，因為簽章和 Timestamp 都不再有效。此外，如果有人試圖以 Plan ₿ Network 的名義惡意偽造證書或文憑，只要簡單地驗證簽章，就能揭穿詐欺行為。


## GPG 簽署如何運作？


GPG 簽署是使用稱為 GNU Privacy Guard 的開放原始碼軟體產生的。此軟體可讓使用者輕鬆建立私人金鑰、簽署和驗證簽章，以及加密和解密檔案。就本教程而言，必須注意的是 Plan ₿ Network 使用 GPG 來建立它的私密金鑰/公開金鑰，並簽署所有₿-CERT 證書和課程結業證書。


另一方面，如果有人想要驗證已簽署檔案的真實性，他們可以使用 GPG 匯入簽發者的公開金鑰並進行驗證。


對於那些好奇並想要了解更多關於這個神奇軟體的人，您可以參考[「GNU 隱私權手冊」](https://www.gnupg.org/gph/en/manual/x135.html)


## 時間戳記如何運作？


任何人都可以使用 OpenTimestamps 來 Timestamp 檔案，並取得其存在的可驗證證明。換句話說，它不會提供檔案建立時間的證明，而是證明檔案存在的時間不會晚於特定時間。

OpenTimestamps 利用高效率的方法在 Bitcoin Blockchain 中儲存證明，免費提供這項服務。它採用 SHA-256 Hash 演算法為您的檔案建立獨特的識別碼，並使用其他使用者所提交檔案的哈希值來建構 Merkle Tree。只有 Merkle Tree 結構中的 Hash 被錨定在 OP_RETURN 交易中，確保以安全且精簡的方式驗證檔案的存在。

一旦這個交易進入一個區塊，任何擁有初始文件和與之相關的`.ots`文件的人都可以驗證時間戳的真實性。在教學的第二部分，我們將看如何在 OpenTimestamps 的網站上，透過模板和圖形 Interface 來驗證您的 Bitcoin 證書或任何課程結業文憑。


# 如何驗證 Plan ₿ Network ₿-CERT 證書或文憑


## 步驟 1.下載您的證書或文憑


登入 planb.network 上的個人/學生儀表板。


![image](./assets/login.webp)


點選左側功能表進入「證書」，選擇您的考試課程或您的文憑。


![image](./assets/credential.webp)


下載壓縮檔。


![image](./assets/download.webp)


在`.zip`檔案上按一下滑鼠右鍵，然後選擇「解壓縮」，即可將內容解壓縮出來。您會發現三個不同的檔案：



- 已簽署的文字檔 (例如：certificate.txt)
- 開放 Timestamp (OTS) 檔案 (例如：certificate.txt.ots)
- PDF 證書 (例如：certificate.pdf)


## 步驟 2：如何驗證文字檔的簽章？


首先，前往您解壓縮檔案的資料夾，並開啟終端機（在資料夾視窗上按滑鼠右鍵，然後按「在終端機中開啟」）。然後按以下指示操作。


1.使用下列指令匯入 Plan ₿ Network 公開 PGP 金鑰：


```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```


如果成功匯入 PGP 金鑰，您應該會看到類似以下的訊息


```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```


注意：如果您看到 1 個金鑰已被處理，而 0 個金鑰已被匯入，很可能表示您之前已經匯入相同的金鑰，這完全沒有問題。


2.使用下列指令驗證證書或文憑的簽章：


```bash
gpg --verify certificate.txt
```


此指令會顯示簽章的詳細資訊，包括



- 誰簽署 (Plan ₿ Network)
- 簽署時
- 簽名是否有效


這是結果的範例：


```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```


如果您看到類似「BAD signature」的訊息，表示檔案已被竄改。


## 步驟 3：驗證開啟的 Timestamp


### 透過圖形 GW 進行驗證-24


1.請造訪 OpenTimestamps 網站：https://opentimestamps.org/

2.按一下「戳記與驗證」標籤。

3.將 OTS 檔案 (例如 `certificate.txt.ots`) 拖放到指定區域。

4.拖放有時間戳記的檔案 (例如 `certificate.txt`) 到指定區域。

5.網站會自動驗證開啟的 Timestamp 並顯示結果。


如果您看到類似以下的訊息，表示 Timestamp 有效：


![cover](assets/opentimestamp_wegui_verified.webp)


### CLI 方法


注意：此程序 ** 將需要一個執行中的本機 Bitcoin 節點**


1.執行下列指令，從官方 [repository](https://github.com/opentimestamps/opentimestamps-client) 安裝 OpenTimestamps 用戶端：


```
pip install opentimestamps-client
```


2.導覽到包含已解壓縮憑證檔案的目錄。


3.執行下列指令驗證開啟的 Timestamp：


```
ots verify certificate.txt.ots
```


此指令將會



- 根據 Bitcoin 的 Blockchain 檢查 Timestamp
- 準確顯示檔案的時間戳記
- 確認 Timestamp 的真實性


### 最終結果


如果顯示下列兩項訊息，驗證即為成功：


1.GPG 簽署報告為 **「來自 Plan ₿ Network 的良好簽章 」**。

2.OpenTimestamps 驗證顯示特定的 Bitcoin 區塊 Timestamp，並報告 **"成功！Bitcoin 區塊 [blockheight] 證明資料存在於 [Timestamp]"**


現在您知道 Plan ₿ Network 如何為任何₿-CERT 憑證和文憑發出可驗證的證明，您可以輕鬆地驗證其完整性。
