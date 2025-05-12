---
name: VeraCrypt
description: 如何輕鬆加密儲存裝置？
---
![cover](assets/cover.webp)


如今，實施策略以確保檔案（例如個人文件、照片或重要專案）的可存取性、安全性和備份非常重要。遺失這些資料可能是災難性的。


為了避免這些問題，我建議您在不同的媒體上維護多個檔案備份。電腦中常用的策略是「3-2-1」備份策略，可確保檔案受到保護：


- 3** 份您的檔案；
- 儲存於至少 **2 ** 種不同類型的媒體上；
- 至少有 **1** 份副本在異地保存。


換句話說，建議您使用不同性質的媒體，例如您的電腦、外接式 Hard 硬碟機、USB 隨身碟或線上儲存服務，將檔案儲存於三個不同的位置。最後，擁有異地複本表示您應該在住家或公司之外儲存備份。最後一點有助於避免在發生火災或水災等當地災害時完全遺失您的檔案。遠離您住所或公司的外部副本可確保您的資料不受當地風險的影響。


要輕鬆實施這個 3-2-1 備份策略，您可以選擇線上儲存解決方案，自動或定期將電腦中的檔案與雲端中的檔案同步。在這些線上備份解決方案中，顯然有您熟悉的大型數位公司提供的解決方案：Google Drive、Microsoft OneDrive 或 Apple iCloud。但是，這些都不是保護您隱私的最佳解決方案。在之前的教學中，我向您介紹了另一種可加密文件以提高保密性的方案：Proton Drive。


https://planb.network/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

透過採用本機和雲端備份的策略，您已經從兩種不同類型的資料媒體中獲益，其中一種是異地備份。若要完成 3-2-1 策略，您只需增加一個副本。我建議您定期將本機和雲端的資料匯出到實體媒體，例如 USB 隨身碟或外接式 Hard 硬碟機。如此一來，即使您的線上儲存解決方案的伺服器被摧毀，而您的電腦也同時癱瘓，您仍可在外部媒體上擁有第三個複本，以免遺失資料。

![VeraCrypt](assets/notext/01.webp)

但同時也要考慮資料儲存的安全性，以確保除了您或您的親人之外，其他人無法存取資料。本機和線上資料通常都是安全的。在您的電腦上，您可能已經設定了密碼，而且現代電腦的 Hard 磁碟機通常都已預設加密。至於您的線上儲存空間 (雲端)，我在之前的教學中已告訴您如何使用強大的密碼和雙重認證來保護您的帳戶。但是，對於儲存在實體媒體上的第三份複本，唯一的安全性就是其實體擁有權。如果竊賊成功偷走您的 USB 隨身碟或外接式 Hard 磁碟機，他們可以輕易存取您的所有資料。

![VeraCrypt](assets/notext/02.webp)

為了避免此風險，建議您對實體媒體進行加密。因此，任何存取資料的嘗試都需要輸入密碼來解密內容。如果沒有密碼，就無法存取資料，即使 USB 隨身碟或外接式 Hard 磁碟機遭竊，也能保護您的個人檔案。

![VeraCrypt](assets/notext/03.webp)

在本教程中，我將教您如何使用開放原始碼工具 VeraCrypt 輕鬆加密外部儲存媒體。


## VeraCrypt 簡介


VeraCrypt 是可在 Windows、macOS 和 Linux 上使用的開放原始碼軟體，可讓您以各種方式在不同媒介上加密資料。

![VeraCrypt](assets/notext/04.webp)

此軟體可即時建立和維護加密磁碟區，這表示您的資料在儲存前會自動加密，在讀取前會自動解密。此方法可確保即使儲存媒體遭竊，您的檔案仍會受到保護。VeraCrypt 不僅會加密檔案，還會加密檔案名稱、元資料、資料夾，甚至是儲存媒體上的可用空間。


VeraCrypt 可用於加密本機檔案或整個磁碟分割，包括系統磁碟。它也可用於完全加密外部媒體，如 USB 隨身碟或磁碟，我們將在本教程中看到。


與專屬解決方案相比，VeraCrypt 的一大優勢在於其完全開放原始碼，這意味著任何人都可以驗證其程式碼。


## 如何安裝 VeraCrypt？


前往 [VeraCrypt 官方網站](https://www.veracrypt.fr/en/Downloads.html) 的「*下載*」標籤。

![VeraCrypt](assets/notext/05.webp)

下載適合您作業系統的版本。如果您的作業系統是 Windows，請選擇「*EXE 安裝程式*」。

![VeraCrypt](assets/notext/06.webp)

為您的 Interface 選擇語言。

![VeraCrypt](assets/notext/07.webp)

接受授權條款。

![VeraCrypt](assets/notext/08.webp)

選擇「*安裝*」。

![VeraCrypt](assets/notext/09.webp)

最後，選擇安裝軟體的資料夾，然後按一下「*安裝*」按鈕。

![VeraCrypt](assets/notext/10.webp)

等待安裝完成。

![VeraCrypt](assets/notext/11.webp)

安裝完成。

![VeraCrypt](assets/notext/12.webp)

如果您願意，可以用比特幣捐款，以支持這個開放原始碼工具的開發。

![VeraCrypt](assets/notext/13.webp)

## 如何使用 VeraCrypt 加密儲存裝置？


第一次發射時，您會到達這個 Interface：

![VeraCrypt](assets/notext/14.webp)

若要加密您選擇的儲存裝置，請先將其連接到您的電腦。如您稍後所見，若 USB 隨身碟或 Hard 磁碟機已包含您不想刪除的資料，則在該裝置上建立新加密磁碟區的過程會花費更多時間。因此，我建議使用空白 USB 隨身碟或事先清空裝置來建立加密磁碟區，以節省時間。


在 VeraCrypt 上，按一下「*磁碟*」索引標籤。

![VeraCrypt](assets/notext/15.webp)

然後在「*建立新磁碟區...*」功能表上。

![VeraCrypt](assets/notext/16.webp)

在開啟的新視窗中，選擇「*加密非系統磁碟分割/磁碟*」選項，然後按一下「*下一步*」。

![VeraCrypt](assets/notext/17.webp)

接下來，您必須在 「*標準 VeraCrypt 加密卷*」和 「*隱藏 VeraCrypt 加密卷*」之間進行選擇。第一個選項會在您的裝置上建立標準加密磁碟區。*Hidden VeraCrypt Volume*」選項允許在標準 VeraCrypt 加密卷中建立隱藏加密卷。此方法可讓您在受到強迫時否認這個隱藏加密卷的存在。舉例來說，如果有人強迫您解密您的裝置，您可以只解密標準的部分來滿足侵略者，但不揭露隱藏的部分。在我的例子中，我會堅持使用標準加密卷。

![VeraCrypt](assets/notext/18.webp)

在接下來的頁面中，按一下「*選擇裝置...*」按鈕。

![VeraCrypt](assets/notext/19.webp)

畫面上會出現一個新視窗，您可從機器上可用的磁碟清單中選擇儲存裝置的磁碟分割。通常，您要加密的磁碟分割會列在標題為「*可移除磁碟 N*」的一行下。選擇適當的磁碟分割後，按一下「*確定*」按鈕。

![VeraCrypt](assets/notext/20.webp)

選取的支援會出現在方塊中。現在您可以點選「*下一步*」按鈕。![VeraCrypt](assets/notext/21.webp)

接下來，您需要在「*建立加密磁碟區並格式化*」或「*就地加密磁碟分割*」兩個選項中選擇一個。如前所述，第一個選項會永久刪除 USB 隨身碟或 Hard 磁碟機上的所有資料。只有當您的裝置是空的，才可選擇此選項；否則，您將會遺失裝置中的所有資料。如果您希望保留現有資料，可以暫時將資料轉移到其他地方，選擇「*建立加密磁碟區並格式化*」以加快刪除所有資料的程序，或選擇「*就地加密磁碟分割*」。最後一個選項允許在不刪除現有資料的情況下加密磁碟區，但過程會更長。在這個範例中，由於我的 USB 隨身碟是空的，所以我選擇「*建立加密磁碟區並格式化*」，這個選項會刪除所有資料。

![VeraCrypt](assets/notext/22.webp)

接下來，您可以選擇加密演算法和 Hash 功能。除非您有特殊需求，否則我建議您保留預設選項。按一下「*下一步*」繼續。

![VeraCrypt](assets/notext/23.webp)

請確認所指示的磁碟區大小正確，以加密 USB 隨身碟上的全部可用空間，而不僅是部分空間。驗證完成後，請按一下「*下一步*」。

![VeraCrypt](assets/notext/24.webp)

在此階段，您需要設定密碼來加密和解密您的裝置。選擇一個強大的密碼非常重要，可防止攻擊者使用暴力攻擊來解密您的內容。密碼應該是隨機的，盡可能長，並包含多種類型的字元。我建議您選擇至少 20 個字元的隨機密碼，包括小寫字母、大寫字母、數字和符號。


我還建議您將密碼保存在密碼管理器中。這會讓您更容易存取，並消除遺忘的風險。就我們的具體情況而言，密碼管理器比紙介質更好。事實上，如果發生盜竊案，儘管您的儲存裝置可能會被盜，但管理器中的密碼卻無法被襲擊者找到，這將會阻止資料的存取。相反，如果您的密碼管理器被洩露，仍需要實體存取裝置，才能利用密碼存取資料。


如需管理密碼的更多資訊，我建議您參考其他完整的教學：


https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

在 2 個指定欄位輸入密碼，然後按「*下一步*」。![VeraCrypt](assets/notext/25.webp)

然後 VeraCrypt 會詢問您是否打算在加密卷中儲存超過 4 GiB 的檔案。此問題可讓軟體選擇最適合的檔案系統。一般來說，會使用 FAT 系統，因為它與大多數的作業系統相容，但它規定的最大檔案大小限制為 4 GiB。如果您需要管理較大的檔案，可以選擇 exFAT 系統。

![VeraCrypt](assets/notext/26.webp)

接下來，您會到達一個頁面，可讓您使用 generate 隨機金鑰。這個金鑰很重要，因為它會用來加密和解密您的資料。它將儲存在媒體的特定區段中，並由您之前建立的密碼保護。要 generate 強大的加密金鑰，VeraCrypt 需要熵。這就是軟體要求您在視窗上隨意移動滑鼠的原因；這些移動將用於 generate 密鑰。繼續移動滑鼠，直到熵值完全填滿為止。然後點擊「*格式化*」開始創建加密卷。

![VeraCrypt](assets/notext/27.webp)

等待格式化完成。對於大容量，這可能需要很長時間。

![VeraCrypt](assets/notext/28.webp)

然後您會收到確認通知。

![VeraCrypt](assets/notext/29.webp)

## 如何使用 VeraCrypt 加密硬碟機？


目前，您的媒體已加密，因此無法開啟。若要解密，請前往 VeraCrypt。

![VeraCrypt](assets/notext/30.webp)

從清單中選擇一個磁碟機代號。例如，我選擇「*L:*」。

![VeraCrypt](assets/notext/31.webp)

按一下「*選擇裝置...*」按鈕。

![VeraCrypt](assets/notext/32.webp)

從機器上所有磁碟的清單中，選擇媒體上的加密磁碟區，然後按一下「*OK*」按鈕。

![VeraCrypt](assets/notext/33.webp)

您可以看到您的音量選擇得很好。

![VeraCrypt](assets/notext/34.webp)

按一下「*掛載*」按鈕。

![VeraCrypt](assets/notext/35.webp)

輸入建立磁碟區時選擇的密碼，然後按一下「*OK*」。

![VeraCrypt](assets/notext/36.webp)

您可以看到您的磁碟區已經解密，並可在磁碟機代號「*L:*」上存取。

![VeraCrypt](assets/notext/37.webp)

若要存取，請開啟您的檔案總管，並移至「*L:*」磁碟機（或其他取決於您在先前步驟中所選擇的字母）。![VeraCrypt](assets/notext/38.webp)

將個人檔案加入媒體後，若要再次加密磁碟區，只要按一下「*Dismount*」按鈕即可。

![VeraCrypt](assets/notext/39.webp)

您的磁碟區不再出現在字母「*L:*」之下。因此它又被加密了。

![VeraCrypt](assets/notext/40.webp)

現在您可以移除儲存媒體。


恭喜您，現在您有一個加密媒體來安全地儲存您的個人資料，因此，除了電腦上的副本和線上儲存解決方案之外，您還有一個完整的 3-2-1 策略。


如果您想支持 VeraCrypt 的開發，也可以 [在此頁面](https://www.veracrypt.fr/en/Donation.html) 以 bitcoins 捐款。