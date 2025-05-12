---
name: 尾巴

description: 在 USB 鑰匙上安裝 Tails
---

![image](assets/cover.webp)


可攜式失憶作業系統，保護您不受監控和審查。


## 為何要有安裝了 Tails 的 USB 鑰匙？


Tails (https://tails.boum.org/) 是讓您隨時擁有安全電腦的最簡單方法，它不會在您使用的電腦上留下任何痕跡。


要使用 Tails，請關閉您可以存取的電腦 (在父母家、朋友家、網咖...) 並使用 Tails USB 密鑰啟動電腦，而非 Windows、macOS 或 Linux。


之後，您將擁有一個獨立於一般作業系統的工作空間和通訊環境，而且絕對不會使用 Hard 磁碟機。


Tails 從不寫入 Hard 磁碟機，只使用電腦的 RAM 來運作。當 Tails 關機時，這個記憶體就會被完全刪除，從而消除所有可能的痕跡。


## 一些具體使用案例


為了讓您具體瞭解 Tails 隨身攜帶 USB 隨身碟的好處，以下是 Agora256 團隊編輯的一份非詳盡的小清單：



- 以不受審查的匿名方式連線至網際網路和 Tor，在不留痕跡的情況下瀏覽網站；
- 從可疑網站開啟 PDF；
- 使用 Electrum Wallet 測試您的 Bitcoin 私密金鑰備份；
- 使用辦公室套件 (LibreOffice) 並在不屬於您的電腦上工作；
- 在 Linux 環境中踏出第一步，學習如何離開 Microsoft 和 Apple 的世界。


## 如何信任 Tails？


使用軟體總是有信任的因素，但不一定要盲目。像 Tails 這樣的工具必須努力提供使用者值得信任的方法。對 Tails 而言，這意味著



- 公開原始碼：https://gitlab.tails.boum.org/；
- 一個以知名專案為基礎的專案：Tor 和 Debian；
- 可驗證和可重複的下載；
- 不同個人和組織的建議。


## 安裝與使用指南


本安裝指南的目的是引導您完成安裝的每個步驟。我們不會比官方指南更多地描述需要採取的行動，但我們會在給您提示和訣竅的同時為您指出正確的方向。


基於實際經驗的原因，這些提示將集中在 macOS 和 Linux 平台上。

🛠️

在開始此程序之前，請確定您有一個讀取速度至少為 150 MB/s、容量至少為 8 GB 的 USB 密鑰，最好是 USB 3.0。


先決條件：



- 1 個 USB 密鑰，僅適用於 Tails，容量至少為 8 GB
- 使用 Linux、macOS 或 Windows 連接至網際網路的電腦
- 約一小時的空閒時間，視您的網際網路連線速度而定，包括 ½ 小時的安裝時間 (1.3 GB 檔案下載)


## 步驟 1：從電腦下載 Tails


![image](assets/1.webp)


🔗 **官方尾巴部分:** https://tails.boum.org/install/linux/index.fr.html#download


下載副檔名為 .img 的安裝檔案可能需要一些時間，這取決於您的網際網路下載速度，因此請提前計劃。在現代高效的連線下，下載時間不會超過 5 分鐘。


將檔案儲存至已知資料夾，例如「下載」，因為下一步將需要此資料夾。


## 步驟 2：驗證您的下載


![image](assets/2.webp)


🔗 **官方尾巴部分:** https://tails.boum.org/install/linux/index.fr.html#verify


驗證下載可確保它是由 Tails 開發人員所發行，並且在下載過程中沒有被損壞或截取。


您可以使用 PGP 手動驗證剛剛下載的檔案是否是預期的檔案，但如果沒有進階知識，此驗證提供的安全性等級與下載頁面上的 JavaScript 驗證相同，但卻複雜得多且容易出錯。


若要驗證檔案，請使用官方部分提供的「選擇您的下載...」按鈕！


## 步驟 3：在 USB 隨身碟上安裝 Tails


![image](assets/3.webp)


🔗 **官方尾巴部分：**



- Linux:** https://tails.boum.org/install/linux/index.fr.html#install
- macOS:** https://tails.boum.org/install/mac/index.fr.html#etcher 和 https://tails.boum.org/install/mac/index.fr.html#install


在 USB key 上安裝 Tails 這一步驟是整份指南中最困難的，尤其是如果您從未執行過這一步驟。最重要的一點是在官方部分選擇適合您作業系統的正確步驟：Linux 或 macOS。


一旦按照建議安裝並準備好工具，就可以將擴展名為 .img 的檔案複製到您的密鑰 (清除所有現有資料)，使其成為可獨立「開機」的檔案。


祝您好運！第 4 步見。


## 步驟 4：重新啟動 Tails USB 密鑰


![image](assets/4.webp)


🔗 **官方尾巴部分:** https://tails.boum.org/install/linux/index.en.html#restart


是時候使用您的新 USB 隨身碟啟動您的電腦了。將它插入其中一個 USB 連接埠，然後重新啟動！


**注意💡：大多數電腦不會自動從 Tails USB 隨身碟開機，但您可以按下開機功能表鍵，以顯示可能從哪些裝置開機的清單。


若要確定您應該按下哪個按鍵，才能確保開機功能表允許您選擇 USB 隨身碟，而不是您常用的 Hard 磁碟機，以下是一份按製造商列出的非完整清單：


| Manufacturer | Key              |
| ------------ | ---------------- |
| Acer         | F12, F9, F2, Esc |
| Apple        | Option           |
| Asus         | Esc              |
| Clevo        | F7               |
| Dell         | F12              |
| Fujitsu      | F12, Esc         |
| HP           | F9               |
| Huawei       | F12              |
| Intel        | F10              |
| Lenovo       | F12              |
| MSI          | F11              |
| Samsung      | Esc, F12, F2     |
| Sony         | F11, Esc, F10    |
| Toshiba      | F12              |
| others...    | F12, Esc         |

選取 USB 隨身碟後，您應該會看到這個新的開機畫面，這是非常好的現象，讓電腦繼續開機...


![image](assets/5.webp)


## 步驟 5： 歡迎來到 Tails！


![image](assets/6.webp)


🔗 **官方尾巴部分:** https://tails.boum.org/install/linux/index.en.html#tails


開機載入程式和載入畫面出現一兩分鐘後會出現歡迎畫面。


![image](assets/7.webp)


在歡迎畫面中，在 Language & Region（語言與區域）部分選擇您的語言和鍵盤配置。按一下 Start Tails。


![image](assets/8.webp)


如果您的電腦未連線至網路，請參考官方的 Tails 說明，協助您在沒有 Wi-Fi 的情況下連線至網路 (「測試您的 Wi-Fi」一節)。


連線到本機網路後，就會出現 Tor 連線精靈，幫助您連線到 Tor 網路。


![image](assets/9.webp)


您可以開始匿名瀏覽，探索 Tails 包含的選項和軟體。盡情享受吧！您有許多出錯的空間，因為 USB 隨身碟上沒有任何修改...下次重新啟動時，您會忘記所有的經驗！


## 在未來的指南中...


當您在自己的 Tails USB 隨身碟上多做一些實驗後，我們會在另一篇文章中探討其他更進階的主題，例如：



- 使用 ** 最新版本的 Tails** 更新金鑰；
- 設定並使用 ** 持久性儲存 **；
- 安裝 ** 附加軟體**。


在此之前，如果您有任何問題，請隨時與 Agora256 社群分享。我們一起學習，明天會比今天更好！