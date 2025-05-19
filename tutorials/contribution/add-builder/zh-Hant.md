---
name: 新增建置者
description: 如何建議在 PlanB 網路上加入新的建置商？
---
![builder](assets/cover.webp)


PlanB 的使命是在 Bitcoin 上以儘可能多的語言提供頂尖的教育資源。網站發佈的所有內容都是開放原始碼，並託管在 GitHub 上，任何人都可以參與豐富平台的內容。


您想在 PlanB Network 網站新增 Bitcoin 「建置者」，並讓您的公司或軟體具有能見度，但卻不知道如何操作？本教學就是為您準備的！

![builder](assets/01.webp)


- 首先，您需要有一個 GitHub 帳戶。如果您不知道如何建立帳號，我們已經製作了詳細的教程來指導您。


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- 到 `resources/builder/` 區的 [PlanB 專用於資料的 GitHub 儲存庫](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/builders)：

![builder](assets/02.webp)


- 按一下右上方的「新增檔案」按鈕，然後按一下「建立新檔案」：

![builder](assets/03.webp)


- 如果您之前從未貢獻過 PlanB Network 的內容，您需要建立原始套件庫的 Fork。Forking 倉庫意味著在您自己的 GitHub 帳戶上創建該倉庫的副本，這樣您就可以在不影響原始倉庫的情況下進行專案工作。點擊 `Fork this repository` 按鈕：

![builder](assets/04.webp)


- 然後您就會到達 GitHub 編輯頁面：

![builder](assets/05.webp)


- 為您的公司建立資料夾。要這樣做，請在 `為您的檔案命名...` 方塊中，以小楷寫上您公司的名稱，並用破折號代替空格。例如，如果您的公司名為 "Bitcoin Baguette"，您應該寫成 `Bitcoin-baguette`：

![builder](assets/06.webp)


- 若要驗證資料夾的建立，只要在同一個方格中，在您的名字後面加上斜線即可，例如： `Bitcoin-baguette/`。加入斜線會自動建立資料夾，而不是檔案：

![builder](assets/07.webp)


- 在此資料夾中，您將建立第一個 YAML 檔案，名稱為 `builder.yml`：

![builder](assets/08.webp)


- 使用此範本將貴公司的相關資訊填入此檔案：


```yaml
name:

address_line_1:
address_line_2:
address_line_3:

language:
-

links:
website:
twitter:
Github:
youtube:
nostr:

tags:
-
-

category:
```


以下是每個按鍵要填寫的內容：


- `name`：您公司的名稱 (必須填寫)；
- `Address` : 您公司的位置 (選用)；
- `language` : 您的企業營運的國家或支援的語言 (選用)；
- `links` : 您企業的各種官方連結 (選用)；
- `tags` : 2 個限定您業務的詞彙 (必須填寫)；
- category`：在下列選項中，最能描述您的企業經營領域的類別：
 - `Wallet`、
 - 「基礎設施」、
 - `Exchange`、
 - `教育`、
 - `服務`、
 - `社群`、
 - `會議`、
 - `privacy`、
 - `投資`、
 - `node`、
 - `Mining`、
 - `新聞`、
 - `製造商`。


例如，您的 YAML 檔案可以如下所示：


```yaml
name: Bitcoin Baguette

address_line_1: Paris, France
address_line_2:
address_line_3:

language:
- fr
- en

links:
website: https://bitcoin-baguette.com
twitter: https://twitter.com/bitcoinbaguette
Github:
youtube:
nostr:

tags:
- bitcoin
- education

category: education
```


![builder](assets/09.webp)


- 完成對該檔案的變更後，請按一下「提交變更...」按鈕以儲存變更：

![builder](assets/10.webp)


- 為您的變更新增標題以及簡短說明：

![builder](assets/11.webp)


- 按一下 Green「提出變更」按鈕：

![builder](assets/12.webp)


- 然後，您會看到總結所有變更的頁面：

![builder](assets/13.webp)


- 按一下右上方的 GitHub 個人檔案圖片，然後按一下「您的儲存庫」：

![builder](assets/14.webp)


- 選擇您的 PlanB Network 儲存庫 Fork：

![builder](assets/15.webp)


- 您應該會在視窗頂端看到新分支的通知。它可能叫做 `patch-1`。點選它：

![builder](assets/16.webp)


- 現在您在工作分支上 (** 請確定您與之前的修改在同一個分支上，這點很重要！**)：

![builder](assets/17.webp)


- 回到 `resources/builders/` 資料夾，選擇您在之前的提交中剛建立的業務資料夾：

![builder](assets/18.webp)


- 在您的業務資料夾中，按一下「新增檔案」按鈕，然後按一下「建立新檔案」：

![builder](assets/19.webp)


- 將這個新資料夾命名為`assets`，並在最後加上斜線`/`，以確認建立：

![builder](assets/20.webp)


- 在這個 `assets` 資料夾中，建立一個名為 `.gitkeep` 的檔案：

![builder](assets/21.webp)


- 按一下「提交變更...」按鈕：

![builder](assets/22.webp)


- 保留提交標題為預設值，並確認「直接提交到 patch-1 分支」方塊已被勾選，然後點選「提交變更」： ![builder](assets/23.webp)
- 回到 `assets` 資料夾：

![builder](assets/24.webp)


- 按一下「新增檔案」按鈕，然後按一下「上傳檔案」：

![builder](assets/25.webp)


- 新頁面將會開啟。將您公司或軟體的圖片拖曳至該區域。此圖片將顯示在 PlanB Network 網站上：

![builder](assets/26.webp)


- 它可以是標誌或圖示：

![builder](assets/27.webp)


- 上傳映像後，確認已勾選「直接提交到 patch-1 分支」方塊，然後按一下「提交變更」：

![builder](assets/28.webp)


- 請注意，您的圖片必須是正方形，必須命名為 `logo` 且必須是 `.webp` 格式。因此，完整的檔案名稱應該是`logo.webp`：

![builder](assets/29.webp)


- 回到`assets`資料夾，點選`.gitkeep`中間檔案：

![builder](assets/30.webp)


- 進入檔案後，按一下右上方的三個小圓點，然後按一下「刪除檔案」：

![builder](assets/31.webp)


- 確認您仍在相同的工作分支上，然後按一下「提交變更」按鈕：

![builder](assets/32.webp)


- 為您的提交新增標題和描述，然後按一下 `提交變更`：

![builder](assets/33.webp)


- 回到您公司的資料夾：

![builder](assets/34.webp)


- 按一下「新增檔案」按鈕，然後按一下「建立新檔案」：

![builder](assets/35.webp)


- 以您母語的指標命名，建立新的 YAML 檔案。此檔案將用於建立程式的描述。例如，如果我想以英文撰寫說明，我會將這個檔案命名為 `en.yml`：

![builder](assets/36.webp)


- 使用此模板填寫此 YAML 檔案：

```yaml
description: |

contributors:
-
```



- 對於 `contributors` 鍵，如果您有的話，您可以在 PlanB Network 中加入您的貢獻者識別碼。如果沒有，請將此欄位留空。
- 對於 `description` 鍵，您只需加入一段簡短的文字，說明您的公司或軟體。描述的語言必須與檔案名稱相同。您不需要將這段描述翻譯成網站支援的所有語言，因為 PlanB 團隊會使用他們的模型來翻譯。舉例來說，您的檔案可以是這樣的：

```yaml
description: |
Founded in 2017, Bitcoin Baguette is a Paris-based association dedicated to organizing Bitcoin meetups and technical workshops. We bring together enthusiasts, experts, and curious minds to explore and discuss the intricacies of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and fostering a deeper understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be a part of Paris's Bitcoin community and stay updated with the latest advancements in the field.

contributors:
-
```

![builder](assets/37.webp)


- 按一下「提交變更」按鈕：

![builder](assets/38.webp)


- 確認已勾選「直接提交到 patch-1 分支」方塊，新增標題，然後按一下「提交變更」：

![builder](assets/39.webp)


- 您的公司資料夾現在應該是這樣的：

![builder](assets/40.webp)


- 如果一切都令您滿意，請返回 Fork 的根源：

![builder](assets/41.webp)


- 您應該會看到一則訊息，顯示您的分支已發生變更。按一下「比較與拉取請求」按鈕：

![builder](assets/42.webp)


- 為您的 PR 加入清楚的標題和說明：

![builder](assets/43.webp)


- 按一下「建立拉取請求」按鈕：

![builder](assets/44.webp)

恭喜您！您的 PR 已成功建立。管理員現在會審核它，如果一切正常，就會將其整合到 PlanB Network 的主儲存庫裡。幾天之後，您應該會看到您的建立者檔案出現在網站上。


請務必跟進您的 PR 進度。管理員可能會留言詢問其他資訊。只要您的 PR 未經驗證，您就可以在 PlanB Network GitHub 套件庫的「Pull requests」標籤中查詢：

![builder](assets/45.webp)

非常感謝您的寶貴貢獻！:)