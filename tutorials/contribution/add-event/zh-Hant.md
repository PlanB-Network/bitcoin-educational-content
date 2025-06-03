---
name: 在 PlanB 網路上新增活動
description: 如何建議在 PlanB Network 上新增活動？
---
![event](assets/cover.webp)


PlanB 的使命是以盡可能多的語言提供 Bitcoin 上的頂級教育資源。網站發佈的所有內容都是開放原始碼，並託管在 GitHub 上，讓任何人都有機會為豐富平台做出貢獻。


如果您想將 Bitcoin 會議新增至 PlanB Network 網站，並增加您活動的能見度，但卻不知道如何操作？本教學就是為您準備的！

![event](assets/01.webp)


- 首先，您需要擁有一個 GitHub 帳戶。如果您不知道如何建立帳號，我們已為您準備了詳細的教學。


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- 前往 `resources/conference/` 區塊中的 [PlanB 專用於資料的 GitHub 儲存庫](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference)：

![event](assets/02.webp)


- 按一下右上方的「新增檔案」按鈕，然後按一下「建立新檔案」：

![event](assets/03.webp)


- 如果您之前從未貢獻過 PlanB Network 的內容，您需要建立原始套件庫的 Fork。Forking 倉庫意味著在您自己的 GitHub 帳戶上建立該倉庫的副本，讓您可以在不影響原始倉庫的情況下進行專案工作。點擊 `Fork this repository` 按鈕：

![event](assets/04.webp)


- 然後您就會到達 GitHub 編輯頁面：

![event](assets/05.webp)


- 為您的會議建立資料夾。為此，請在 `為您的檔案命名...` 方塊中，以小楷寫下您的會議名稱，並以破折號代替空格。例如，如果您的會議稱為 "Paris Bitcoin Conference「，則應註明 」paris-Bitcoin-conference"。也請加上您的會議年份，例如：`paris-Bitcoin-conference-2024`：

![event](assets/06.webp)


- 若要驗證資料夾的建立，只要在同一個方格中，在您的名字後面加上斜線即可，例如：`paris-Bitcoin-conference-2024/`。加入斜線會自動建立資料夾，而非檔案：

![event](assets/07.webp)


- 在此資料夾中，您將建立第一個 YAML 檔案，名稱為 `events.yml`：

![event](assets/08.webp)


- 使用此模板將會議資訊填入此檔案：


```yaml
start_date:
end_date:
address_line_1:
address_line_2:
address_line_3:
name:
builder:
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description:
language:
-
links:
website:
replay_url:
live_url :
tags:
-
```


例如，您的 YAML 檔案可以如下所示：


```yaml
start_date: 2024-08-15
end_date: 2024-08-18
address_line_1: Paris, France
address_line_2:
address_line_3:
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description: The largest Bitcoin conference in France with over 8,000 participants each year!
language:
- fr
- en
- es
- it
links:
website: https://paris.bitcoin.fr/conference
replay_url:
live_url :
tags:
- Bitcoiner
- General
- International
```

![event](assets/09.webp)

如果您的組織還沒有 "*builder*"識別碼，您可以按照此其他教程來新增。


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- 完成對該檔案的變更後，請按一下「提交變更...」按鈕以儲存變更：

![event](assets/10.webp)


- 為您的變更新增標題以及簡短說明：

![event](assets/11.webp)


- 按一下 Green `提出變更'按鈕：

![event](assets/12.webp)


- 然後，您會看到總結所有變更的頁面：

![event](assets/13.webp)


- 按一下右上方的 GitHub 個人檔案圖片，然後按一下「您的儲存庫」：

![event](assets/14.webp)


- 選擇您的 PlanB Network 儲存庫 Fork：

![event](assets/15.webp)


- 您應該會在視窗頂端看到新分支的通知。它可能叫做 `patch-1`。點選它：

![event](assets/16.webp)


- 現在您在您的工作分支上：

![event](assets/17.webp)


- 回到 `resources/conference/` 資料夾，選擇您在之前的提交中剛建立的會議資料夾：

![event](assets/18.webp)


- 在您的會議資料夾中，按一下「新增檔案」按鈕，然後按一下「建立新檔案」：

![event](assets/19.webp)


- 將這個新資料夾命名為`assets`，並在最後加上斜線`/`，以確認建立：

![event](assets/20.webp)


- 在這個 `assets` 資料夾中，建立一個名為 `.gitkeep` 的檔案：

![event](assets/21.webp)


- 按一下「提交變更...」按鈕：

![event](assets/22.webp)


- 將提交標題保留為預設值，並確認「直接提交到 patch-1 分支」方塊已被勾選，然後按一下「提交變更」：

![event](assets/23.webp)


- 回到 `assets` 資料夾：

![event](assets/24.webp)


- 按一下「新增檔案」按鈕，然後按一下「上傳檔案」： ![event](assets/25.webp)
- 將會開啟一個新頁面。拖放代表您的會議的圖片，並顯示在 PlanB Network 網站上：

![event](assets/26.webp)


- 它可以是標誌、縮圖，甚至是海報：

![event](assets/27.webp)


- 圖片上傳後，檢查是否勾選了「直接提交到 patch-1 分支」方塊，然後按一下「提交變更」：

![event](assets/28.webp)


- 請注意，您的圖片必須命名為 `thumbnail` 並必須是 `.webp` 格式。因此，完整的檔案名稱應該是thumbnail.webp`：

![event](assets/29.webp)


- 回到您的 `assets` 資料夾，點選中介檔案 `.gitkeep`：

![event](assets/30.webp)


- 進入檔案後，按一下右上方的 3 個小圓點，然後按一下「刪除檔案」：

![event](assets/31.webp)


- 確認您仍在相同的工作分支上，然後按一下「提交變更」按鈕：

![event](assets/32.webp)


- 為您的提交新增標題和描述，然後按一下 `提交變更`：

![event](assets/33.webp)


- 回到儲存庫的根目錄：

![event](assets/34.webp)


- 您應該會看到一則訊息，顯示您的分支已發生變更。按一下「比較與拉取請求」按鈕：

![event](assets/35.webp)


- 為您的 PR 加入清楚的標題和說明：

![event](assets/36.webp)


- 按一下「建立拉取請求」按鈕：

![event](assets/37.webp)

恭喜您！您的 PR 已成功建立。管理員現在會檢查它，如果一切正常，就會合併到 PlanB Network 的主儲存庫裡。您應該會在幾天後看到您的活動出現在網站上。


請務必跟進您的 PR 進度。管理員可能會留言詢問其他資訊。只要您的 PR 未經驗證，您就可以在 PlanB Network GitHub 套件庫的「Pull requests」標籤中查詢：

![event](assets/38.webp)

非常感謝您的寶貴貢獻！:)