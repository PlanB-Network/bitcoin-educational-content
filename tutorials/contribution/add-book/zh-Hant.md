---
name: 將書籍加入 PlanB 網路
description: 如何在 PlanB Network 加入新書？
---
![book](assets/cover.webp)


PlanB 的使命是以盡可能多的語言提供 Bitcoin 上的頂級教育資源。所有在網站上發表的內容都是開放原始碼，並託管在 GitHub 上，讓任何人都能為豐富平台做出貢獻。


**您是否想在 PlanB Network 網站上新增與 Bitcoin 相關的書籍，並增加您作品的能見度，但卻不知道如何操作？本教學就是為您準備的！**

![book](assets/01.webp)


- 首先，您需要有一個 GitHub 帳戶。如果您不知道如何建立帳號，我們已經製作了詳細的教程來指導您。


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- 到 `resources/books/` 區的 [PlanB 專用於資料的 GitHub 儲存庫](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/books)：

![book](assets/02.webp)


- 按一下右上方的「新增檔案」按鈕，然後按一下「建立新檔案」：

![book](assets/03.webp)


- 如果您之前從未貢獻過 PlanB Network 的內容，您需要建立原始套件庫的 Fork。Forking 倉庫意味著在您自己的 GitHub 帳戶上建立該倉庫的副本，讓您可以在不影響原始倉庫的情況下進行專案工作。點擊 `Fork this repository` 按鈕：

![book](assets/04.webp)


- 然後您就會到達 GitHub 編輯頁面：

![book](assets/05.webp)


- 為您的書本建立資料夾。要做到這一點，請在 「命名您的檔案... 」方塊中，以小楷寫上您的書籍名稱，並用破折號代替空格。例如，如果您的圖書名稱為 "*My Bitcoin Book*"，則應註明 `my-Bitcoin-book`：

![book](assets/06.webp)


- 若要驗證資料夾的建立，只要在同一個方格中的書籍名稱後加上斜線即可，例如： `my-Bitcoin-book/`。加入斜線會自動建立資料夾，而非檔案：

![book](assets/07.webp)


- 在此資料夾中，您將建立第一個 YAML 檔案，名稱為 `book.yml`：

![book](assets/08.webp)


- 使用此模板將您的書籍資訊填入此檔案：


```yaml
author:
level:
tags:
-
-
```


以下是每個欄位需要填寫的詳細資料：


- `author`**：表示該書的作者姓名。
- `level`**：指出能夠很好地閱讀和理解本書所需的等級。請從下列等級中選擇：
 - 初學者
 - 中級
- `進階` - `專家`
- `標籤`**：新增兩到三個與您的書籍相關的標籤。例如：
    - Bitcoin
    - 歷史
    - 技術
    - 經濟
    - `教育`...


例如，您的 YAML 檔案可以如下所示：


```yaml
author: Loïc Morel
level: beginner
tags:
- bitcoin
- technology
```


![book](assets/09.webp)


- 完成對該檔案的變更後，請按一下「提交變更...」按鈕以儲存變更：

![book](assets/10.webp)


- 為您的變更新增標題以及簡短說明：

![book](assets/11.webp)


- 按一下 Green `提出變更'按鈕：

![book](assets/12.webp)


- 然後，您會看到總結所有變更的頁面：

![book](assets/13.webp)


- 按一下右上方的 GitHub 個人檔案圖片，然後按一下「您的儲存庫」：

![book](assets/14.webp)


- 選擇您的 PlanB Network 儲存庫 Fork：

![book](assets/15.webp)


- 您應該會在視窗頂端看到新分支的通知。它可能叫做 `patch-1`。點選它：

![book](assets/16.webp)


- 現在您在您的工作分支上：

![book](assets/17.webp)


- 回到 `resources/books/` 資料夾，選擇您在之前的提交中剛建立的書籍資料夾：

![book](assets/18.webp)


- 在您的圖書資料夾中，按一下「新增檔案」按鈕，然後按一下「建立新檔案」：

![book](assets/19.webp)


- 將這個新資料夾命名為`assets`，並在最後加上斜線`/`，以確認建立：

![book](assets/20.webp)


- 在這個 `assets` 資料夾中，建立一個名為 `.gitkeep` 的檔案：

![book](assets/21.webp)


- 按一下「提交變更...」按鈕：

![book](assets/22.webp)


- 將提交標題保留為預設值，並確認「直接提交到 patch-1 分支」方塊已被勾選，然後按一下「提交變更」：

![book](assets/23.webp)


- 回到 `assets` 資料夾：

![book](assets/24.webp)


- 按一下「新增檔案」按鈕，然後按一下「上傳檔案」：

![book](assets/25.webp)


- 新頁面將會開啟。將您書籍的封面圖片拖放到該區域。此圖片將會顯示在 PlanB Network 網站上：

![book](assets/26.webp)


- 請注意，圖片必須以書本格式製作，以便最好地適應我們的網站，例如：

![book](assets/27.webp)


- 圖片上傳後，請確認已勾選「直接提交到 patch-1 分支」方塊，然後按一下「提交變更」：

![book](assets/28.webp)- Please note, your image must be named `cover_en` if the cover is in English and must be in `.webp` format. Therefore, the complete file name should be `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, etc. If you wish to use a different cover image for each language, for example in the case of a book translation, you can place them in the same location in the `assets` folder:

![book](assets/29.webp)


- 回到您的 `assets` 資料夾，點選 `.gitkeep` 中介檔案：

![book](assets/30.webp)


- 進入檔案後，按一下右上方的 3 個小圓點，然後按一下「刪除檔案」：

![book](assets/31.webp)


- 確保您仍在相同的工作分支上，然後按一下「提交變更...」按鈕：

![book](assets/32.webp)


- 為您的提交新增標題和說明，然後按一下「提交變更」：

![book](assets/33.webp)


- 回到您的書本資料夾：

![book](assets/34.webp)


- 按一下「新增檔案」按鈕，然後按一下「建立新檔案」：

![book](assets/35.webp)


- 以書籍的語言指標命名，建立新的 YAML 檔案。這個檔案將用於書籍的描述。例如，如果我想以英文撰寫說明，我會將這個檔案命名為 `en.yml`：

![book](assets/36.webp)


- 使用此模板填寫此 YAML 檔案：

```yaml
title: ""
publication_year:
cover: cover_en.webp
original: true
description: |

contributors:
-
```


以下是每個欄位需要填寫的詳細資料：


- `title`**：用引號表示書籍的名稱。
- `publication_year`**：表示書籍出版的年份。
- `cover`**：根據您目前編輯的 YAML 檔案語言，指出封面影像對應的檔案名稱。例如，如果您正在編輯 `en.yml` 檔案，而之前已新增了標題為 `cover_en.webp` 的英文封面圖片，則只需在此欄位中指出 `cover_en.webp`。
- `description`**：新增一段簡短的文字來描述這本書。描述的語言必須與 YAML 檔案標題所示的語言相同。
- `contributors`**：如果您有貢獻者 ID，請加入您的 ID。


例如，您的 YAML 檔案可以如下所示：


```yaml