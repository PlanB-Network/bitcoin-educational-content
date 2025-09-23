---
name: Cryptomator
description: 在雲端加密您的檔案
---
![cover](assets/cover.webp)



___



*本教學是根據 Florian BURNEL 發表於 [IT-Connect](https://www.it-connect.fr/) 的原始內容。原始碼授權類型 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有變更。*



___



## I.簡報



在本教程中，我們將使用 Cryptomator 應用程式來加密儲存於雲端的資料，不論是 Microsoft OneDrive、Google Drive、Dropbox、Box 甚至 iCloud。



為您儲存在 Drive 等線上儲存解決方案上的資料加密，是保護您的檔案和隱私的最佳方式。有了加密功能，即使資料儲存在美國或全球其他國家的伺服器上，也只有您才能解密並讀取資料。



在本範例中，將使用配備 OneDrive 的 Windows 11 22H2 機器，但在其他版本的 Windows 和其他儲存服務上，步驟是相同的。您只需安裝同步用戶端，並添加您的帳戶。這將使 Cryptomator 能夠在儲存庫中儲存資料。



![Image](assets/fr/020.webp)



Cryptomator 是其他應用程式的替代方案，特別是另一篇文章中介紹的 Picocrypt，它看起來不同，但使用起來同樣簡單。Cryptomator 也是**開放原始碼**、符合 RGPD 規範，並會使用 AES-256 位元加密演算法**加密資料**。相比之下，Picocrypt 則依賴速度更快的 XChaCha20 演算法 (也是 256 位元)。



https://planb.network/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

Cryptomator 應用程式適用於 **Windows** (exe / msi)、**Linux**、**macOS**，也適用於 **Android** 和 **iOS**。順便說一下，除了 Android 應用程式需要付費 (14.99 歐元) 之外，所有應用程式都是免費的。



在您的電腦上，**Cryptomator 會建立一個資料夾，並在其中建立一個保險庫**。在保險庫內（可儲存在您的 OneDrive、Google Drive 或類似的儲存空間），您的資料將會被加密。因此，如果您將所有資料儲存在 Drive 儲存空間託管的保險箱中，這些資料將受到保護（因為已加密）。



**註**：本文以線上儲存服務為例，但 Cryptomator 可用於加密本機磁碟、外接式磁碟甚至 NAS 上的資料。事實上，沒有任何限制。



## II.安裝 Cryptomator



若要開始使用，您需要**下載**並**安裝**Cryptomator**。下載完成後，只需按幾下即可完成安裝。與 [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/)一樣，Cryptomator 將依賴 WinFsp 在您的 Windows 機器上**掛載虛擬磁碟機。





- [從官方網站下載 Cryptomator](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III.在 Windows 上使用 Cryptomator



### A.建立新的保險箱



若要建立新保險箱，請按一下「**新增**」按鈕，然後選擇「**新保險箱...**」。此機器上的現有保險箱和已知保險箱就會出現在 Interface 的左側。*在機器 A 上建立的保險箱可以在機器 B 上打開和修改，只要機器 B 配備 Cryptomator（且知道加密金鑰）。*



![Image](assets/fr/015.webp)



首先為儲存庫命名，例如「**IT-Connect**」。這會在我的 OneDrive 中建立一個名為「**IT-Connect**」的目錄。



![Image](assets/fr/011.webp)



在下一步中，Cryptomator 可能會**偵測您機器上存在的「Drive」**：Google Drive、OneDrive、Dropbox 等....。以便您直接選擇提供者。我在兩台不同的 Windows 11 機器上試過，有好幾個 Drive，都沒偵測到。這不是問題，只要定義「**自訂位置**」，然後選擇儲存空間的根目錄即可。例如 **C:\Users\<Username>\OneDrive**.



![Image](assets/fr/018.webp)



接下來，您可以調整專家設定下的選項。



![Image](assets/fr/021.webp)



接下來，您需要定義**與加密金鑰相對應的密碼**。此密碼可讓您**解鎖 Cryptomator 保險箱**並存取其資料。 **如果您丟失了密碼，就無法存取您的資料**。最後，您仍可選擇勾選「**是，安全總比遺憾好**」選項來**建立備份金鑰**，這與 [BitLocker] 復原金鑰 (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/) 的精神相同。建議您這樣做，但不要將此備份金鑰儲存在 OneDrive 的根目錄！



按一下「**建立保險箱**」。



![Image](assets/fr/019.webp)



複製復原密鑰並將其儲存到您最喜歡的密碼管理器中。按一下「**下一步**」。



![Image](assets/fr/013.webp)



就是這樣，您的新幹線已建立並可使用！



![Image](assets/fr/014.webp)



### B.存取數字



若要存取保險箱及其資料，無論是**讀取現有資料或新增資料**，您都需要**解除鎖定**。Cryptomator 會列出已知的保險箱：IT-Connect 保險箱就會出現，您只需選取並點擊「**解鎖**」即可。



![Image](assets/fr/016.webp)



您必須輸入密碼才能解除保險箱的鎖定。然後按一下「**釋放磁碟機**」。



![Image](assets/fr/022.webp)



**您的保險櫃會以虛擬磁碟機的形式掛載在 Windows 機器上。**此磁碟機（在此繼承字母 E）可讓您存取資料（以純文字形式，因為保險櫃已解鎖）。



![Image](assets/fr/017.webp)



在 OneDrive 方面，我們無法直接瀏覽 Cryptomator 儲存庫。我們看不到資料（文件名和內容）。這表示您不需要透過一般的 OneDrive 捷徑來新增資料到您的 Cryptomator 儲存庫。**您必須使用 Cryptomator 的虛擬磁碟機來新增資料。**



![Image](assets/fr/012.webp)



### C.幹線選項



保險箱的設定可透過「**加密磁碟區選項**」按鈕進行存取（鎖定時），並會在不活動時啟用自動鎖定功能，就像您的密碼保險箱一樣。**啟動時解除鎖定加密磁碟區**」選項，顧名思義，不需您的任何介入即可解除鎖定磁碟機，並掛載虛擬磁碟機。基於安全理由，最好避免啟動此選項。



透過「**掛載**」標籤，您也可以決定以唯讀方式掛載或指定特定的字母。



![Image](assets/fr/024.webp)



此外，在 Cryptomator 設定中，您可以**啟用自動啟動應用程式**。



## IV.結論



使用 **Cryptomator**，您可以在幾分鐘內建立一個加密的保險箱，以保護您希望儲存在 OneDrive 和其他硬碟上的資料。與 Drive「配對」時，它非常容易使用：就這一目的而言，我比 **Picocrypt** 更偏好使用它。