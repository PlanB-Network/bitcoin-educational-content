---
name: Picocrypt
description: 加密資料的開放原始碼工具
---
![cover](assets/cover.webp)



___



*本教學是根據 Florian BURNEL 發表於 [IT-Connect](https://www.it-connect.fr/) 的原始內容。原始碼授權類型 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原始內容有變更。



___



## I.簡報



在本教程中，我們將介紹 Picocrypt，這是一款簡單、輕量且有效的加密軟體，可在高度安全的情況下加密資料。



適用於**加密檔案**，您可以使用它來保護電腦、USB 隨身碟上的**資料，也可以保護儲存在雲端的資料。例如，您可以加密資料並將其儲存在**Microsoft OneDrive、Google Drive、iCloud 或 Dropbox**，不過為了這個目的，我比較喜歡另一款軟體，將在未來的文章中介紹。



當您需要與第三方**共用資料時，您也可以使用它：由於有了 Picocrypt 和解密金鑰，他們將能夠解密他們機器上的資料。因此，如果您的帳戶或電腦遭到洩露，您的資料也會受到保護。



要跟進 Picocrypt 專案，只有一個 Address：





- [Picocrypt on GitHub](https://github.com/Picocrypt/Picocrypt)



PicoCrypt 完全**免費且開放原始碼**，適用於**Windows、**Linux**和**macOS**。在 Windows 上，您可以在自己的機器上安裝，或使用可攜式版本。



## II.開放原始碼加密軟體 Picocrypt



Picocrypt** 加密軟體是其他知名解決方案的***替代方案，例如 **VeraCrypt**、**Cryptomator** (*專為雲端環境加密資料*) 或 **AxCrypt**。順便一提，在 Picocrypt 的官方 GitHub 上，您可以找到與一些競爭對手的比較：



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

來源: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt 非常**輕巧**，只有**3 MB**，而且不需要安裝：它是一個**便攜的應用程式**，具有不需要管理員權限的優點！然而，它並沒有忽略安全性，因為它依賴於**強大且可靠的演算法**：





- XChaCha20** 加密演算法
- 按鍵旁路功能 **Argon2**



除了剛才提到的優點之外，真正吸引人的是**它的易用性！



它只需要一樣東西： **程式碼稽核**，但那是計劃中的，您可以從上面的比較表（最後一行）看到。但既然它是開放原始碼，就沒有什麼可以阻止您看看它的原始碼。



儘管上表將 Picocrypt 與 BitLocker 相提並論，**在我看來，BitLocker 和 Picocrypt 是用於不同的用途**：BitLocker 用於加密完整的磁碟區 (例如 Windows 的磁碟區)，而 Picocrypt 則用於加密樹狀結構或「Drive」類型的儲存空間。



## III.使用 Picocrypt



本示範將使用 Windows 11 機器。



### A.使用 Picocrypt 加密資料



首先，您需要從官方 GitHub 下載 Picocrypt.exe（[請參閱此頁](https://github.com/Picocrypt/Picocrypt/releases)）。



開啟應用程式，螢幕上會顯示簡約的 Interface。若要加密資料，不論是**檔案、多個檔案或資料夾**，只要**拖放至 Picocrypt 的 Interface**即可。這將會選擇要加密的資料。



![Image](assets/fr/020.webp)



然後，在資料加密方面，您可以使用多種選項，包括加密金鑰。它可以是 ** 強密碼** 或 ** 密鑰檔案形式的加密金鑰**，或 ** 二者皆是**。以密碼為例，您可以選擇建立自己的密碼，或是使用 Picocrypt 產生密碼。



此密碼必須強大，因為它可用於解密資料。在「**密碼**」和「**確認密碼**」下輸入密碼，然後按一下「**加密**」以加密資料！在此之前，您可以按一下「**儲存輸出為**」旁邊的「**變更**」按鈕，指定輸出目錄。



**註**：若要使用檔案格式的金鑰，請點選「**金鑰檔案**」右方的「**建立**」來建立金鑰。然後按一下「**編輯**」，將金鑰檔案拖曳到適當的區域來選取。



![Image](assets/fr/019.webp)



由於 **PCV** 是 Picocrypt 使用的副檔名，因此兩個選取的檔案會被 ** 加密並組成 ** 檔案「**Encrypted.zip.pcv**」。由於已加密，此 ZIP 檔案無法讀取。若要防止選取的檔案在單一加密的 ZIP 檔案中被集中在一起，您需要勾選「**遞歸**」選項，以便有多少個加密檔案，就有多少個要加密的檔案。



若要存取資料，我們需要使用 Picocrypt 將資料解密。



![Image](assets/fr/023.webp)



在談論資料解密之前，這裡先介紹一些可用選項的相關資訊：





- 偏執模式**：使用 Picocrypt 提供的最高安全層級。該工具將使用多種串聯加密演算法 (XChaCha20 和 Serpent) 以及 HMAC-SHA3 取代 BLAKE2b 來進行資料驗證。
- Reed-Solomon**：實作 *Reed-Solomon* 糾錯碼，以方便對損毀資料進行糾錯。這可讓您支援檔案約 3% 的損毀程度。
- 分割成小塊**或**分割成幾個部分**：如果您要加密一個大檔案，您可以要求 Picocrypt 將它分割成幾個部分。這可能會讓檔案更容易傳輸。
- Compress Files** 或 **Compress files**：壓縮檔案以減小加密檔案的大小。
- 刪除的檔案** 或 **Fichiers supprimés**：刪除原始檔案，只保留加密版本



### B.使用 Picocrypt 解密資料



如果您需要解密資料，不會比加密資料更複雜。只需開啟 Picocrypt 並 ** 拖放要解密的 PCV 檔案**。然後輸入密碼和/或選擇金鑰檔案，再按一下「**解密**」。



![Image](assets/fr/021.webp)



未加密版本的「Encrypted.zip」ZIP 存檔現在可以讓我以明確的文字復原我的兩個檔案！



![Image](assets/fr/022.webp)



## IV.結論



**已經警告過你了Picocrypt 非常容易使用，而且非常有效！雖然 Interface 非常簡約，但它整合了一些非常有用的自訂加密選項！由於它有可攜式版本，您可以隨身攜帶，讓您可以放心地解密資料**。



請務必使用強大的密碼來保護資料，如果使用金鑰檔案，一定要記得備份，否則就無法再解密 Picocrypt 所產生的 PCV container。最後，您應該知道還有 [CLI 版本](https://github.com/Picocrypt/CLI) (功能較少)，可以讓您從命令列執行 Picocrypt：在此，Picocrypt 再次為您開啟新的可能性。



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5