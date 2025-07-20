---
name: 將 Podcast 加入 PlanB Network
description: 如何新增 Podcast 到 PlanB Network？
---
![podcast](assets/cover.webp)


PlanB 的使命是以盡可能多的語言提供有關 Bitcoin 的頂級教育資源。網站發佈的所有內容都是開放原始碼，並託管在 GitHub 上，讓任何人都能參與豐富平台的內容。


您是否正在尋找將 Bitcoin Podcast 加入 PlanB Network 網站並為您的節目增加能見度，但卻不知道如何操作？本教學就是為您準備的！

![podcast](assets/01.webp)


- 首先，您需要有一個 GitHub 帳戶。如果您不知道如何建立，我們已為您準備了詳細的教學。


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- 前往 `resources/podcasts/` 區塊中的 [PlanB 專用於資料的 GitHub 儲存庫](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/podcasts)：

![podcast](assets/02.webp)


- 按一下右上方的「新增檔案」按鈕，然後按一下「建立新檔案」：

![podcast](assets/03.webp)


- 如果您之前從未貢獻過 PlanB Network 的內容，您需要建立原始套件庫的 Fork。Forking 倉庫意味著在您自己的 GitHub 帳戶上建立該倉庫的副本，讓您可以在不影響原始倉庫的情況下進行專案工作。點擊 `Fork this repository` 按鈕：

![podcast](assets/04.webp)


- 然後您就會到達 GitHub 編輯頁面：

![podcast](assets/05.webp)


- 為您的 Podcast 建立資料夾。要做到這一點，請在「為您的檔案命名...」方塊中，以小楷寫下您的 Podcast 名稱，並用破折號代替空格。例如，如果您的節目叫做「Super Podcast Bitcoin」，您應該寫成 `super-podcast-Bitcoin`：

![podcast](assets/06.webp)


- 若要驗證資料夾的建立，只要在同一個方格中的 Podcast 名稱後加上斜線即可，例如：`super-podcast-Bitcoin/`。加入斜線會自動建立資料夾，而非檔案：

![podcast](assets/07.webp)


- 在此資料夾中，您將建立第一個 YAML 檔案，名稱為 `podcast.yml`：

![podcast](assets/08.webp)


- 使用此模板在此檔案中填入有關您 Podcast 的資訊：


```yaml
name:
host:
language:
links:
podcast:
twitter:
website:
description: |

tags:
-
-
contributors:
-
```


以下是每個欄位需要填寫的詳細資料：



- `name`**：指出您 Podcast 的名稱。
- `host`**：列出 Podcast 講者或主持人的姓名或假名。每個名字都應以逗號分隔。
- `language`**：指出您的 Podcast 所使用的語言代碼。例如，英文請註明 `en`，義大利語請註明 `it`...



- `links`**：提供您內容的連結。您有兩個選項：
 - `podcast`：您的播客連結、
 - twitter：播客或製作機構的 Twitter 個人資料連結、
 - 網站」：播客或製作組織網站的連結。



- `description`**：新增一段簡短的文字，描述您的 Podcast。描述的語言必須與 `language:` 欄位中的語言相同。



- `tags`**：新增兩個與您的 Podcast 相關的標籤。範例：
    - Bitcoin
    - 技術
    - 經濟
    - `教育`...



- `contributors`**：如果您有貢獻者 ID，請提及您的 ID。


例如，您的 YAML 檔案可以如下所示：


```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
twitter: https://twitter.com/decouvrebitcoin
website: https://decouvrebitcoin.fr
description: |
Super Podcast Bitcoin is a technical LIVE session held once a week on Twitter to delve deep into the Bitcoin protocol, layer two solutions, and all things that blow minds. Our hosts Lounes, Pantamis, Loïc, and Sosthene will answer your questions and offer the most technical show on Bitcoin in the world.

tags:
- bitcoin
- technology
contributors:
- rabbit-hole
```


![podcast](assets/09.webp)



- 完成對該檔案的變更後，請按一下「提交變更...」按鈕以儲存變更：

![podcast](assets/10.webp)


- 為您的變更新增標題以及簡短說明：

![podcast](assets/11.webp)


- 按一下 Green `提出變更'按鈕：

![podcast](assets/12.webp)


- 然後，您會看到一個總結所有變更的頁面：

![podcast](assets/13.webp)


- 按一下右上方的 GitHub 個人檔案圖片，然後按一下「您的儲存庫」：

![podcast](assets/14.webp)


- 選擇您的 PlanB Network 儲存庫 Fork：

![podcast](assets/15.webp)


- 您應該會在視窗頂端看到新分支的通知。它可能叫做 `patch-1`。點選它：

![podcast](assets/16.webp)


- 現在您在您的工作分支上：

![podcast](assets/17.webp)


- 回到 `resources/podcast/` 資料夾，選擇您在之前的提交中剛建立的 podcast 資料夾： ![podcast](assets/18.webp)
- 在您的 Podcast 資料夾中，按一下「新增檔案」按鈕，然後按一下「建立新檔案」：

![podcast](assets/19.webp)


- 將這個新資料夾命名為`assets`，並在最後加入斜線`/`以確認其建立：

![podcast](assets/20.webp)


- 在這個 `assets` 資料夾中，建立一個名為 `.gitkeep` 的檔案：

![podcast](assets/21.webp)


- 按一下「提交變更...」按鈕：

![podcast](assets/22.webp)


- 將提交標題保留為預設值，並確認「直接提交到 patch-1 分支」方塊已被勾選，然後按一下「提交變更」：

![podcast](assets/23.webp)


- 回到 `assets` 資料夾：

![podcast](assets/24.webp)


- 按一下「新增檔案」按鈕，然後按一下「上傳檔案」：

![podcast](assets/25.webp)


- 新頁面將會開啟。將您的 Podcast 標誌拖放至該區域。此圖片將顯示在 PlanB Network 網站上：

![podcast](assets/26.webp)


- 請注意，圖片必須是正方形，以最適合我們的網站：

![podcast](assets/27.webp)


- 上傳映像後，確認已勾選「直接提交到 patch-1 分支」方塊，然後按一下「提交變更」：

![podcast](assets/28.webp)


- 請注意，您的圖片必須命名為 `logo` 並必須是 `.webp` 格式。因此，完整的檔案名稱應該是`logo.webp`：

![podcast](assets/29.webp)


- 回到您的 `assets` 資料夾，點選中介檔案 `.gitkeep`：

![podcast](assets/30.webp)


- 進入檔案後，按一下右上方的三個小圓點，然後按一下「刪除檔案」：

![podcast](assets/31.webp)


- 確認您仍在相同的工作分支上，然後按一下「提交變更」按鈕：

![podcast](assets/32.webp)


- 為您的提交新增標題和說明，然後按一下「提交變更」：

![podcast](assets/33.webp)


- 回到儲存庫的根目錄：

![podcast](assets/34.webp)


- 您應該會看到一則訊息，顯示您的分支已發生變更。按一下「比較與拉取請求」按鈕：

![podcast](assets/35.webp)


- 為您的 PR 加入清楚的標題和說明：

![podcast](assets/36.webp)


- 按一下「建立拉取請求」按鈕：

![podcast](assets/37.webp)

恭喜您！您的 PR 已成功建立。管理員現在會審核它，如果一切正常，就會合併到 PlanB Network 的主儲存庫裡。您應該會在幾天後看到您的 Podcast 出現在網站上。


請務必跟進您的 PR 進度。管理員可能會留言詢問其他資訊。只要您的 PR 未經驗證，您就可以在 PlanB Network GitHub 套件庫的 `Pull requests` 標籤中查看：

![podcast](assets/38.webp)

非常感謝您的寶貴貢獻！:)