---
name: 新增會議重播
description: 如何在 PlanB Network 上新增會議重播？
---
![conference](assets/cover.webp)


PlanB 的使命是以盡可能多的語言提供 Bitcoin 上的頂級教育資源。網站發佈的所有內容都是開放原始碼，並託管在 GitHub 上，讓任何人都能為平台的豐富化貢獻心力。


您想在 PlanB Network 網站上新增 Bitcoin 會議的重播，並讓此活動具有能見度，但卻不知道如何操作？本教學就是為您準備的！


但是，如果您要新增將於未來舉行的會議，我建議您閱讀其他教學，其中我們會說明如何在網站上新增活動。


https://planb.network/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)


- 首先，您需要擁有一個 GitHub 帳戶。如果您不知道如何建立帳號，我們已為您準備了詳細的教學。


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- 前往 `resources/conference/` 區塊中的 [PlanB 專用於資料的 GitHub 儲存庫](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference)：

![conference](assets/02.webp)


- 按一下右上方的「新增檔案」按鈕，然後按一下「建立新檔案」：

![conference](assets/03.webp)


- 如果您之前從未貢獻過 PlanB Network 的內容，您需要建立原始套件庫的 Fork。Forking 倉庫意味著在您自己的 GitHub 帳戶上創建該倉庫的副本，這樣您就可以在不影響原始倉庫的情況下進行專案工作。點擊 `Fork this repository` 按鈕：

![conference](assets/04.webp)


- 然後您就會到達 GitHub 編輯頁面：

![conference](assets/05.webp)


- 為您的會議建立資料夾。為此，請在 `為您的檔案命名...` 方塊中，以小楷寫下您的會議名稱，並以破折號代替空格。例如，如果您的會議稱為 "Paris Bitcoin Conference「，則應註明 」paris-Bitcoin-conference"。也請加上您的會議年份，例如：`paris-Bitcoin-conference-2024`：

![conference](assets/06.webp)


- 若要驗證資料夾的建立，只要在同一個方格中，在您的名字後面加上斜線即可，例如：`paris-Bitcoin-conference-2024/`。加入斜線會自動建立資料夾，而非檔案：

![conference](assets/07.webp)


- 在此資料夾中，您將建立第一個 YAML 檔案，名稱為 `conference.yml`：

![conference](assets/08.webp)

使用此範本將會議相關資訊填入此檔案：

```yaml
year:
name:
builder:
location:
language:
-
links:
website:
twitter:
tags:
-
-
```


例如，您的 YAML 檔案可以如下所示：


```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Paris, France
language:
- fr
- en
links:
website: https://paris.bitcoin.fr/conference
twitter: https://twitter.com/ParisBitcoinConference
tags:
- International
- All Public
```


![conference](assets/09.webp)


如果您的組織還沒有 "*builder*"識別碼，您可以按照此其他教程來新增。


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- 完成對該檔案的變更後，請按一下「提交變更...」按鈕以儲存變更：

![conference](assets/10.webp)


- 為您的變更新增標題以及簡短說明：

![conference](assets/11.webp)


- 按一下 Green `提出變更'按鈕：

![conference](assets/12.webp)


- 然後，您會看到總結所有變更的頁面：

![conference](assets/13.webp)


- 按一下右上方的 GitHub 個人檔案圖片，然後按一下「您的儲存庫」：

![conference](assets/14.webp)


- 選擇您的 PlanB Network 儲存庫 Fork：

![conference](assets/15.webp)


- 您應該會在視窗頂端看到新分支的通知。它可能叫做 `patch-1`。點選它：

![conference](assets/16.webp)


- 現在您在您的工作分支上：

![conference](assets/17.webp)


- 回到 `resources/conference/` 資料夾，選擇您在之前的提交中剛建立的會議資料夾：

![conference](assets/18.webp)


- 在您的會議資料夾中，按一下「新增檔案」按鈕，然後按一下「建立新檔案」：

![conference](assets/19.webp)


- 將這個新資料夾命名為`assets`，並在最後加上斜線`/`，以確認建立：

![conference](assets/20.webp)


- 在這個 `assets` 資料夾中，建立一個名為 `.gitkeep` 的檔案：

![conference](assets/21.webp)


- 按一下「提交變更...」按鈕：

![conference](assets/22.webp)


- 將提交標題保留為預設值，並確認「直接提交到 patch-1 分支」方塊已被勾選，然後按一下「提交變更」：

![conference](assets/23.webp)


- 回到 `assets` 資料夾：

![conference](assets/24.webp)


- 按一下「新增檔案」按鈕，然後按一下「上傳檔案」：

![conference](assets/25.webp)


- 將會開啟新的頁面。拖放代表您的會議的圖片，並顯示在 PlanB Network 網站上： ![conference](assets/26.webp)
- 它可以是標誌、縮圖，甚至是海報：

![conference](assets/27.webp)


- 圖片上傳後，檢查是否勾選了 `Commit directly to the patch-1 branch` 方塊，然後按一下 `Commit changes` ：

![conference](assets/28.webp)


- 請注意，您的圖片必須命名為 `thumbnail` 並必須是 `.webp` 格式。因此，完整的檔案名稱應該是thumbnail.webp`：

![conference](assets/29.webp)


- 回到您的 `assets` 資料夾，點選 `.gitkeep` 中介檔案：

![conference](assets/30.webp)


- 進入檔案後，按一下右上角的 3 個小圓點，然後按一下「刪除檔案」：

![conference](assets/31.webp)


- 確認您仍在相同的工作分支上，然後按一下「提交變更」按鈕：

![conference](assets/32.webp)


- 為您的提交新增標題和描述，然後按一下 `提交變更`：

![conference](assets/33.webp)


- 回到您的會議資料夾：

![conference](assets/34.webp)


- 按一下「新增檔案」按鈕，然後按一下「建立新檔案」：

![conference](assets/35.webp)


- 建立一個新的 markdown (.md) 檔案，以您的母語指標命名。此檔案將用於重播您的會議。舉例來說，如果我要用英文撰寫會議說明，我會將這個檔案命名為 en.md：

![conference](assets/36.webp)


- 使用此範本填寫此 markdown 檔案，您可以根據您的會議配置調整此範本：


```markdown
---
name: Paris Bitcoin Conference 2024
description: The largest Bitcoin conference in France with over 8,000 participants each year!
---

# Main Stage

## Friday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Friday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshop Room

## The Future of Bitcoin Mining: Challenges and Innovations

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto

## Is Privacy Still Possible On Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto

## Bitcoin Core: Deep Dive into the Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Building and Securing Bitcoin Wallets With Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto
```


![conference](assets/37.webp)


- 在您文件的開頭，在「front matter」中，在`name:`欄位填入您的會議名稱和重播年份。在`description:`欄位中，以檔案的語言寫入您活動的簡短說明。例如，若檔案名稱為 `en.md`，描述應為英文。PlanB Network 團隊會使用他們的模型負責翻譯您的描述。
- 以`#`標記的第一級標題用於按場景組織會議。例如，`# Main Stage ` 表示主舞台，`# Workshop Room ` 表示專用於工作坊的舞台。



- 以雙`##`標示的第二級標題用於區分不同的重播視訊。如果會議是在半天內連續拍攝，請標示，例如，`### 星期五上午`。如果會議是單獨拍攝與播放，則直接以二級標題命名會議。



- 在每個二級標題下，插入相應重播視訊的連結。語法應為`![視訊](https://youtu.be/XXXXXXXXXXXX)`，用實際的視訊連結取代`XXXXXXXX`。



- 如果格式允許（個別會議），您可以加入演講者的姓名。要做到這一點，請在視訊連結下新增 `Speaker:` 欄位，接著是演講者的姓名或假名。若有多位講者，請以逗號分隔每位姓名，例如：`Speaker：Satoshi Nakamoto、Satoshi Nakamoto、Satoshi Nakamoto、Satoshi Nakamoto`。


---


- 完成修改後，按一下「提交變更...」按鈕以儲存檔案：

![conference](assets/38.webp)


- 為您的修改添加標題以及簡短說明：

![conference](assets/39.webp)


- 按一下「提交變更」：

![conference](assets/40.webp)


- 您的會議資料夾現在應該是這個樣子：

![conference](assets/41.webp)


- 如果一切都令您滿意，請返回 Fork 的根源：

![conference](assets/42.webp)


- 您應該會看到一則訊息，顯示您的分支已進行修改。按一下「比較與拉取請求」按鈕：

![conference](assets/43.webp)


- 為您的 PR 加入明確的標題和描述：

![conference](assets/44.webp)


- 按一下「建立拉取請求」按鈕：

![conference](assets/45.webp)

恭喜您！您的 PR 已成功建立。管理員現在會審核它，如果一切正常，就會合併到 PlanB Network 的主儲存庫裡。您應該會在幾天後看到您的會議重播出現在網站上。


請務必跟進您的 PR 進度。管理員有可能會留言詢問其他資訊。只要您的 PR 未經驗證，您就可以在 PlanB Network GitHub 套件庫的「Pull requests」標籤下檢視：

![conference](assets/46.webp)


非常感謝您的寶貴貢獻！:)