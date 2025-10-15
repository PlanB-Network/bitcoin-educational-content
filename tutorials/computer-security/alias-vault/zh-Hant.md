---
name: Alias Vault
description: 管理密碼、雙因素驗證和別名的強大工具 (內建電子郵件伺服器) - 也可自行託管！
---

![cover](assets/cover.webp)



線上隱私權和安全性是任何人，不論其業務為何，都應該密切注意的議題。



此外，這些問題也是不斷動盪的世界的一部分：愈來愈多開發者參與這個主題，為既有的解決方案和新產品帶來實作。



這就是 **Leendert de Borst** 和他的「Alias Vault」，一個革命性的工具 (第一個)，可以讓您管理和儲存密碼、使用密碼記錄驗證網站服務、管理雙因素驗證，但最重要的是，generate 真正的 _alias_，全都在單一的 Interface 中。



**But Alias Vault doesn't stop there***.



## 主要功能



Alias Vault 可在雲端開發人員的伺服器上運作，也可在自己的基礎架構中自行託管，Docker 檔案和映像可使用 scipt 安裝。除了網頁 Interface，還有適用於所有熱門瀏覽器的擴充套件，以及適用於 iOS 和 Android 的行動應用程式；後者也可從 F-Droid 下載，繞過 Google 官方商店。



在一個 Interface Alias Vault 是：




- 免費且開放原始碼**
- 密碼管理器**，可儲存所有複雜的密碼。使用瀏覽器擴充套件，密碼管理器可完成登入網站
- 2FA**，支援雙因素驗證
- 內嵌電子郵件伺服器的別名管理器**：Alias Vault 不會建立將電子郵件轉寄到使用者信箱的別名；相反地，它會建立實際的別名，包括名、姓、性別、使用者名稱、密碼和生日 (如果需要這些資訊)。



廣泛而詳盡的說明文件是套件的一部分，它將陪伴新手發現這個強大的工具。



## 無個人資料！



一如既往，它始於 [aliasvault.net](aliasvault.net)網站。如前所述，Alias Vault 可以在自己的伺服器上使用，也可以從開發人員的雲端使用，以便在轉換到自我託管的解決方案之前熟悉它。



這個網站的圖形真的很搶眼，而且維護得很好，但如果您開始上手，好東西就來了： **建立您的帳戶**。



![img](assets/en/01.webp)



令您驚喜的是，Alias Vault 不會要求您提供個人資訊：您只需要任何暱稱、您熟悉的單字即可建立帳戶。同意服務條款，選擇詞彙，然後繼續。



![img](assets/en/02.webp)



現在設定**`主密碼`**，這是您整個新系統中最重要的資訊。事實上，有了這一個密碼，您將是唯一可以存取/復原帳號的人，因為它會讓您的 `vault ` 加密在伺服器上，而伺服器將會託管您的資訊。



![img](assets/en/03.webp)



事實：您已經建立了自己的密碼管理員和別名管理員，但沒有提供自己的工作、私人電子郵件 Address。



![img](assets/en/04.webp)



Alias Vault 歡迎您來到一個安全、嶄新、個人但也空曠的空間。現在我們開始填充一些內容。



如果您已經有密碼管理器，您可以從正在使用的管理器匯入檔案，以評估與其他提供者的差異，或者也許可以取消別名管理器，這樣您就可以在一個應用程式中管理所有東西。



![img](assets/en/05.webp)



Alias Vault 非常簡單：您有一個主頁面，也就是「主頁」，其中有兩個選單：




- 憑證」： 可讓您建立並管理身分和別名
- `Email`：收件匣，您可以在其中檢查您所產生的別名的接收訊息。



![img](assets/en/06.webp)



我們感興趣的是建立第一個「別名」，因此請移至頁面右上方，按一下 _+New Alias_。



![img](assets/en/07.webp)



根據 Alias Vault 的理念，最初的功能表看起來非常簡約。若要探索此功能的特色，請按一下 _Create via advanced mode_。



![img](assets/en/08.webp)



第一個畫面的頂部，您可以用它來匯入您已訂閱的服務，或您在線上最常使用的密碼憑證。



如果您已在上述任何（或所有）服務上啟用雙因素驗證，則使用 Alias Vault，您還可以透過匯入「秘鑰」來管理此額外的 Layer 安全性。Alias Vault 將建立存取所需的 `TOTP`。



![img](assets/en/09.webp)



**注意**：在預留給電子郵件 Address 的空間中，Alias Vault 預設會提出自己的網域；為了使用您先前建立帳號時的正確 Address，請按一下 _Enter custom domain_，以便在 `@`後設定正確的網域。



![img](assets/en/14.webp)



這個畫面最下方的部分最有趣。按一下 _Generate Random Alias_，Alias Vault 就會針對不同的需求為您建立不同的身分，每個身分都有自己的信箱、非常強大的等級密碼，並輔以其他詳細資料，例如性別、出生日期和合適的暱稱。



![img](assets/en/10.webp)



您可以從相應的功能表中變更會影響密碼產生的設定，例如僅選擇小寫字母和剔除可能含糊不清的字元。



![img](assets/en/11.webp)



您可以使用 Alias Vault 建議的別名電子郵件，或者按一下相應的下拉式功能表來變更網域。



![img](assets/en/12.webp)



在將此電子郵件用於登入服務之前，您可以從自己的 Address 向新建立的信箱傳送訊息，測試其功能。



![img](assets/en/13.webp)



**⚠️ 警告**：由於 Alias Vault 的內建伺服器，您可以接收電子郵件，但這只允許您接收電子郵件，而不允許您回覆，也不允許您使用電子郵件信箱的「傳統」「別名」服務功能。因此，它與 Simple Login、Addy 及其他專門提供此類服務的平台大不相同。有關 Simple Login 的範例，您可以查看專用教學：



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

若要刪除作為測試而建立的別名，您只需登入「主頁」，然後選取「憑證」，然後按一下您要刪除的身分。右上角會出現 _Delete_ 指令，讓您繼續。



![img](assets/en/16.webp)



## 瀏覽器延伸功能



根據您的需求，您可以求助瀏覽器擴充套件，在最廣泛使用的瀏覽器上都可以找到。



![img](assets/en/15.webp)



它的安裝方式與您安裝所有其他擴充套件的方式相同，因此我就不多說這個細節了。



瀏覽器擴充套件可讓您更輕鬆地登入線上服務，或在需要時建立新的別名：如果服務儲存在您的 Alias Vault 記錄中，自動填寫就會完成所需的工作。



![img](assets/en/17.webp)



唯一需要注意的是確認 Alias Vault 是否處於活動狀態。事實上，應用程式有一個預設設定，在一段時間不活動後會暫停。這是一個非常有用的功能，**當您必須離開電腦，例如，防止他人訪問您的帳戶**。如果之前的會話仍在快取記憶體中，簡化程序將允許您輸入「主密碼」再次登錄。登出時間是您可以自訂的參數之一，可依您的喜好縮短或延長時間。



## 行動應用程式



與所有自重的同類應用程式一樣，Alias Vault 也有 Android 和 iOS 環境下的行動裝置版本。對於 Android，您可以從 [F-Droid](https://f-droid.org/packages/net.aliasvault.app/)下載應用程式。



在撰寫這篇文章時（2025 年 8 月底），手機應用程式認為「自動填寫」是一項實驗性功能，除了極少數網站之外無法使用。在完全實現之前，在手機上使用 Alias Vault 需要複製/貼上資料。



從商店下載應用程式後，只需輸入在 Web 應用程式上建立的使用者和「主密碼」即可登入。



![img](assets/en/18.webp)



開啟您的「拱頂」時，系統會詢問您是否要啟用生物辨識控制存取，這是額外的 Layer 安全機制，可防止其他人碰巧拿著您的手機存取您的密碼。



![img](assets/en/19.webp)



如果您決定設定生物辨識檢查，請繼續。如果您跳過此步驟後改變主意，您也可以稍後從 _Settings_ 功能表進行設定。



完成登入後，您會發現已建立的資料再次同步化。



![img](assets/en/20.webp)



行動應用程式可路由至其伺服器上託管的 `vault` 連結。



![img](assets/en/22.webp)



而這正是我們將在下一節簡要介紹的 Address 自託版本。



## 自行託管：完全控制您的資料



平心而論，Alias Vault 並非第一個可讓您在基礎架構上部署服務的密碼管理器。還有其他的，但有些不是有限制就是部分封鎖了原始碼。



機會是獨一無二的： **不再依賴外部服務供應商或雲端，而是使用您自己的本機伺服器來保護和管理密碼、別名以及與之相關的極度敏感資訊**。使用 Alias Vault，您還可以讓電子郵件服務指向您自己的電子郵件伺服器，以增加機密性。



是時候轉到 [說明文件](https://docs.aliasvault.net/installation/)，瞭解如何進行自我託管 Alias Vault。



![img](assets/en/23.webp)



Alias Vault 在 Docker Compose 上執行，因此需要最低限度的 Linux 和 Docker 經驗。您可以先從基本安裝開始，然後再完成更進階的解決方案。



您的伺服器必須在 64 位元機器上執行，搭配 Linux 發行版本、1 GB 記憶體和至少 16 GB 的儲存空間；Docker (CE) 的版本必須至少是 20.10 或更高，而 Docker Compose 則需要 2.0 以上的版本。



我決定用瘦客戶機試試 Alias Vault，在瘦客戶機上安裝了 DietPi 作為發行版，Debian Bookworm base，已優化至最基本的部分，並已執行 `Docker` 和 `Docker Compose`。



首先，為了有一些秩序，在您的主目錄建立一個目錄，開啟`終端機`並貼上執行安裝腳本的指令。



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



安裝完成後，您會發現您的存取憑證：


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



安裝後檢查目錄內容。



![img](assets/en/29.webp)



要啟動 Alias Vault，請使用指令：



```` Launch-Alias-Vault


./install.sh start


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/user/start


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## 加密與安全性的考量



![img](assets/en/32.webp)



根據 Lanedirt 在網站上、文件中和 Github 上的說明，使用 Alias Vault，**您放在 Alias Vault 上的所有資訊 (元件) 都會與裝置緊密結合、加密，任何不知道「主密碼」的人都無法存取**。



因此，「主密碼」是整個「金庫」的基本要素。輸入密碼後，會以 Hard 記憶體密碼匙衍生功能的 `Argon2id` 演算法處理，以防止秘密離開裝置。



即使對雲端或主機服務管理員而言，一切仍是隱藏的。事實上，從管理面板您無法存取使用者詳細資料，您只能知道他們是否已建立別名、收到電子郵件，其他幾乎無法得知。



所有儲存的內容都會透過源自「主密碼」的加密金鑰進行加密和解密。 **只有加密資料會儲存在伺服器上，沒有任何資料會以純文字顯示**。如果用戶忘記或遺失了「主密碼」，與之相連的帳戶將不可逆轉地丟失，因為伺服器無法存取明文內容。



對於自我託管版本，有腳本可以重設「主密碼」，但這並不能防止資料遺失。



![img](assets/en/33.webp)



由於 Alias Vault 正處於 _Beta_ 階段，如果您變更/更新主密碼，可能會難以存取。我建議您從一開始就選擇穩健且複雜的密碼，以便您可以嘗試使用該服務，並最終決定是否使用。如果您在更新密碼後仍無法存取雲端，請聯絡 Alias Vault 支援。



若要完整瞭解 Alias Vault 所採用的架構和安全性，我強烈建議您參閱 [此頁面](https://docs.aliasvault.net/architecture/)，其中包含其運作所依據的密碼技術細節。



## 道路地圖


開發人員的意圖是在 2025 年底前讓 Alias Vault 變得成熟穩定，以便定義其未來的使用特性。



Alias Vault 現在是而且將永遠是開放原始碼和免費的，但可能不像 beta 版一樣是無限制的。某些付費功能正在實作中，因為這些功能已經公佈。



有團隊/家庭計劃和硬體金鑰支援，後者用於 FIDO2 或 WebAuth 的驗證。



## 誰需要 Alias Vault



**這樣的工具非常適合將網路隱私權放在第一位的人**。



您的身份很可能是您在線上進行的業務的核心，因此必須採取一切手段來保護您的身份，以防止***資料被那些為了獲取您的在線行為而不擇手段的服務、公司和經紀人獲取。



Alias Vault 讓您重新完全掌控憑證，減少或完全消除依賴第三方保護和加密您最敏感資料的需要。



Alias Vault 的架構和加密設施是主權個人、中小型企業、開發團隊以及所有**開放原始碼**應用程式愛好者的理想選擇。如果您屬於上述任何一種類型：請盡情探索 Alias Vault。