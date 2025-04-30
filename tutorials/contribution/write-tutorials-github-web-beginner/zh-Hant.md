---
name: 貢獻 - GitHub 網路教學 (初學者)
description: 使用 GitHub Web 的 Plan ₿ Network 教學完整指南
---
![cover](assets/cover.webp)


在按照本教學添加新教學之前，您需要完成幾個初步步驟。如果您還沒有完成，請先看一下這個入門教學，然後再回到這裡：


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

您已經擁有 ：




- 為您的教學選擇一個主題；
- 透過 [Telegram 群組](https://t.me/PlanBNetwork_ContentBuilder) 或 paolo@planb.network 聯絡 Plan ₿ Network 團隊；
- 選擇您的貢獻工具。


在本教程中，我們將介紹如何使用 GitHub 的 Web 版本將您的教程添加到 Plan ₿ Network。如果您已經精通 Git，這篇非常詳細的教學對您來說可能就沒有必要了。反之，我建議您查看另外兩篇教程中的其中一篇，在這篇教程中，我詳細介紹了從本地 .NET 系統進行變更時需要遵循的指導方針和步驟：




- 經驗豐富的使用者** ：


https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410


- 中級 (GitHub 桌面)** ：


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

## 先決條件


開始教學前的先決條件 ：




- 擁有 [GitHub 帳戶](https://github.com/signup)；
- 擁有 [Plan ₿ Network 原始碼倉庫](https://github.com/PlanB-Network/Bitcoin-educational-content) 的 Fork；
- 擁有 [Plan ₿ Network 上的教師簡介](https://planb.network/professors) (僅當您提供完整的教學)。


如果您在獲得這些先決條件方面需要幫助，我的其他教程會有所幫助：



https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.network/tutorials/contribution/others/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

一旦一切就緒，您也有了 Plan ₿ Network 儲存庫的 Fork，就可以開始新增教學了。


## 1 - 建立新的分支


打開瀏覽器，導覽到 Plan ₿ Network 套件庫中的 Fork 頁面。這是您在 GitHub 上建立的 Fork。您的 Fork 的 URL 應該如下所示：`https://github.com/[your-username]/Bitcoin-educational-content` ：


![GITHUB](assets/fr/01.webp)


確定您在主 `dev` 分支上，然後按一下「*同步 Fork*」按鈕。如果您的 Fork 不是最新版本，GitHub 會要求您更新分支。進行此更新：


![GITHUB](assets/fr/02.webp)


點選 `dev` 分支，然後為您的工作分支命名，使其標題清楚反映其目的，並使用破折號分隔字詞。例如，如果我們的目的是撰寫使用 Green Wallet 的教學，分支可以稱為：`tuto-Green-Wallet-loic`.輸入適當的名稱後，按一下「*建立分支*」以確認基於 `dev` 建立的新分支：


![GITHUB](assets/fr/03.webp)


現在您應該在新的工作分支上了：


![GITHUB](assets/fr/04.webp)


這表示您所做的任何變更都只會儲存在該特定分支上。


每發表一篇新文章，就從 `dev` 建立一個新的分支。


Git 中的分支代表專案的平行版本，讓您可以在不影響主分支的情況下進行修改，直到您的工作可以整合為止。


## 2 - 新增教學檔案


現在工作分支已經建立，是時候整合您的新教學了。


在您的分支檔案中，您需要找到適當的子資料夾，以放置您的教學。資料夾的組織反映了 Plan ₿ Network 網站的不同部分。在我們的範例中，由於我們要新增 Green Wallet 的教學，因此請前往下列路徑：`Bitcoin-educational-content/tutorials/Wallet`，它對應於網站的`Wallet`部分：


![GITHUB](assets/fr/05.webp)


在 `Wallet` 資料夾中，建立一個專門用於教學的新目錄。此資料夾的名稱應清楚說明教學中涵蓋的軟體，並使用連字線連接字詞。在我的範例中，資料夾將命名為 `Green-Wallet`。按一下「*新增檔案*」，然後按一下「*建立新檔案*」：


![GITHUB](assets/fr/06.webp)


輸入資料夾名稱，然後輸入斜線 `/`，以確認將其建立為資料夾。


![GITHUB](assets/fr/07.webp)


在這個專門用於教學的新子資料夾中，您需要新增幾個項目：




- 建立一個 `assets` 資料夾，存放教學所需的所有插圖；
- 在這個 `assets` 資料夾中，建立一個根據教學原始語言代碼命名的子資料夾。例如，如果教學以英文撰寫，則此子資料夾應命名為 `en`。將教學的所有視覺資料（圖表、影像、螢幕截圖等）放入此資料夾。
- 必須建立一個 `tutorial.yml` 檔案來記錄您教學的詳細資訊；
- 必須建立一個 markdown 檔案來撰寫教學的實際內容。此檔案必須根據撰寫語言的代碼來命名。例如，對於以法文撰寫的教學，該檔案應命名為 `fr.md`。


總括而言，以下是檔案層級結構 (我們會在下一節繼續建立)：


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (à modifier avec la bonne catégorie)
└── green-wallet/ (à modifier avec le nom du tuto)
├── assets/
│   ├── fr/ (à modifier selon le code de langue approprié)
├── tutorial.yml
└── fr.md (à modifier selon le code de langue approprié)
```


## 3 - 填寫 YAML 檔案


讓我們從 YAML 檔案開始。在建立新檔案的方塊中，輸入 `tutorial.yml` ：


![GITHUB](assets/fr/08.webp)


複製以下範本，填入 `tutorial.yml` 檔案：


```
id:

project_id:

tags:
-
-
-

category:

level:

professor_id:

# Proofreading metadata

original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributor_names:
-
reward:
```


以下是必填欄位：



- id** ：UUID (_Universally Unique Identifier_)，用來唯一識別教學。您可以使用 [線上工具](https://www.uuidgenerator.net/version4) generate 它。唯一的要求是這個 UUID 是隨機的，以避免與平台上的其他 UUID 衝突；



- project_id** ：教程中展示的工具背後的公司或組織的 UUID [來自專案清單](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects)。例如，如果您要建立一個關於 Green Wallet 軟體的教學，您可以在下列檔案中找到這個 `project_id`：`Bitcoin-educational-content/resources/projects/blockstream/project.yml`。此資訊會被加入到您的教學 YAML 檔案中，因為 Plan ₿ Network 會維護所有在 Bitcoin 或相關專案上運作的公司和組織的資料庫。透過加入連結到您教學的實體的「project_id」，您就在兩個 Elements 之間建立了連結；



- 標籤** ：從 Plan ₿ Network 標籤清單中](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) 獨家選取 2 或 3 個與教學內容相關的關鍵字；



- 類別** ：根據 Plan ₿ Network 網站結構，與教學內容相對應的子類別（例如，對於錢包：`桌面`、`硬體`、`行動`、`備份`）；



- 等級** ：教學的難度等級，可從下列項目中選擇：
    - 初學者
    - 中級
    - `進階`
    - `專家`



- professor_id** ：您的 `professor_id` (UUID) 顯示在 [您的教授簡介](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors)；



- original_language** ：教學的原始語言 (例如 `fr`、`en` 等)；



- 校對** ：有關校對過程的資訊。完成第一部分，因為校對自己的教程算作第一次驗證：
    - language** ：校對的語言代碼 (例如 `fr`、`en` 等)。
    - last_contribution_date** ：當天的日期。
    - 迫切性** ：1
    - contributor_names** ：您的 GitHub ID。
    - 獎勵** ：0


有關教師 ID 的詳細資訊，請參閱相應的教學：


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
- wallets
- software
- keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency: 1
contributor_names:
- LoicPandul
reward: 0
```


完成修改 `tutorial.yml` 檔案後，按一下「*Commit changes...*」按鈕儲存文件：


![GITHUB](assets/fr/09.webp)


添加標題和說明，並確保提交到您在本教程開始時建立的分支。然後點擊「*提交變更」確認。


![GITHUB](assets/fr/10.webp)


## 4 - 為影像建立子資料夾


再次按一下「*新增檔案*」，然後按一下「*建立新檔案*」：


![GITHUB](assets/fr/11.webp)


輸入`assets`，然後輸入斜線`/`來建立資料夾：


![GITHUB](assets/fr/12.webp)


在 `/assets` 資料夾中重複此步驟，建立語言子資料夾，例如 `fr` 如果您的教學是法語：


![GITHUB](assets/fr/13.webp)


在這個資料夾中，建立一個假檔案來強制 GitHub 保留您的資料夾（否則會是空的）。將檔案命名為 `.gitkeep`。然後點擊「*提交變更...*」。


![GITHUB](assets/fr/14.webp)


再次檢查您是否在正確的分支上，然後按一下「*提交變更」。


![GITHUB](assets/fr/15.webp)


## 5 - 建立 Markdown 檔案


現在我們要建立一個檔案來存放您的教學，檔案名稱根據您的語言代碼來命名，例如 `fr.md` 如果我們要寫法文的話。進入您的教學資料夾 ：


![GITHUB](assets/fr/16.webp)


按一下「新增檔案*」，然後按一下「建立新檔案*」。


![GITHUB](assets/fr/17.webp)


使用您的語言代碼命名檔案。在我的例子中，由於教學是以法文撰寫，因此我將檔案命名為 `fr.md`。副檔名 `.md` 表示檔案是 Markdown 格式。


![GITHUB](assets/fr/18.webp)


我們先填入文件頂端的 `Properties` 區段。手動新增並填寫下列程式碼區塊（`name:` 和`description:` 鍵必須保持英文，但其值必須以您的教學所使用的語言撰寫）：


```
---
name: [Titre]
description: [Description]
---
```


![GITHUB](assets/fr/19.webp)


填入您的教學名稱和簡短說明：


![GITHUB](assets/fr/20.webp)


然後，在您的教學開頭加入封面圖片的路徑。要做到這一點，請注意：


```
![cover-green](assets/cover.webp)
```


當您需要在教學中加入圖片時，這個語法就會派上用場。感嘆號表示圖片，其替代文字 (alt) 指定在方括號之間。圖片路徑在方括號之間：


![GITHUB](assets/fr/21.webp)


按一下「*提交變更...*」按鈕以儲存此檔案。


![GITHUB](assets/fr/22.webp)


檢查您是否在正確的分支上，然後確認提交。


![GITHUB](assets/fr/23.webp)


根據您的語言代碼，您的教學資料夾現在應該是這樣的：


![GITHUB](assets/fr/24.webp)


## 6 - 加入標誌和封面


在 `assets` 資料夾中，您需要新增一個名為 `logo.webp` 的檔案，作為您文章的縮圖。此圖片必須是「.webp」格式，且大小必須為正方形，以符合使用者 Interface。


您可以自由選擇教程中使用的軟體標誌，或任何其他相關圖片，只要是免版稅的即可。此外，請在相同位置新增標題為 `cover.webp` 的圖片。這將會顯示在您教程的頂部。請確保這張圖片與標誌一樣，尊重使用權並適合您的教學內容。


若要新增圖片到 `/assets` 資料夾，您可以從本機檔案拖放圖片。確定您在 `/assets` 資料夾中，並且在正確的分支上，然後按一下「*提交變更*」。


![GITHUB](assets/fr/26.webp)


現在您應該可以看到圖片出現在資料夾中。


![GITHUB](assets/fr/27.webp)


## 7 - 撰寫教學


繼續撰寫您的教學，在 Markdown 檔案中記下您的內容與語言代碼 (在我的範例中，法文是 `fr.md` 檔案)。移至該檔案，然後按一下鉛筆圖示 ：


![GITHUB](assets/fr/28.webp)


開始撰寫您的教學。新增副標題時，請使用適當的 Markdown 格式，在文字前加上 `##` ：


![GITHUB](assets/fr/29.webp)


交替使用「*編輯*」與「*預覽*」檢視，讓渲染更直觀。


![GITHUB](assets/fr/30.webp)


若要儲存您的工作，請按一下「*Commit Changes...*」，確定您在正確的分支上，然後再按一下「*Commit Changes*」確認。


![GITHUB](assets/fr/31.webp)


## 8 - 加入視覺效果


在 `/assets` 資料夾中的語言子資料夾 (在我的範例中： `/assets/en`)，是用來儲存您的教學所附的圖表和視覺效果。盡可能避免在您的圖像中包含文字，使您的內容能為國際觀眾所接受。當然，所介紹的軟體會包含文字，但如果您在軟體截圖上添加示意圖或其他指示，請在不包含文字的情況下進行，或者如果必要，請使用英文。


要為您的圖片命名，只需使用與它們在教學中出現順序相對應的數字，格式為兩位數字（或三位數字，如果您的教學包含超過 99 個圖片）。例如，將第一個影像命名為 `01.webp`，第二個命名為 `02.webp`，依此類推。


您的圖片必須是 `.webp` 格式。如有必要，您可以使用 [我的圖片轉換軟體](https://github.com/LoicPandul/ImagesConverter)。


![GITHUB](assets/fr/32.webp)


現在您已經把圖片加入子資料夾了，可以刪除虛擬檔案 `.gitkeep`。打開這個檔案，按一下右上角的三個小點，然後按「*刪除檔案*」。


![GITHUB](assets/fr/33.webp)


按一下「*Commit changes...*」儲存變更。


![GITHUB](assets/fr/34.webp)


若要將子資料夾中的圖表插入您的編輯文件，請使用下列 Markdown 指令，注意指定適當的替代文字以及適合您語言的正確圖片路徑：


```
![green](assets/fr/01.webp)
```


開頭的感嘆號表示圖片。替代文字放在方括號之間，有助於存取和參考。最後，圖片的路徑標示在方括號之間。


![GITHUB](assets/fr/35.webp)


如果您希望建立自己的示意圖，請務必遵循 Plan ₿ Network 圖形指引，以確保視覺一致性：




- 字型**：使用 [Rubik](https://fonts.google.com/specimen/Rubik)；
- 顏色** ：
 - 橙色：#FF5C00
 - 黑色 : #000000
 - 白色：#FFFFFF


**所有整合到您的教學中的視覺圖表都必須是無版權或尊重原始檔授權許可的**。因此，在 Plan ₿ Network 上發佈的所有圖表均採用 CC-BY-SA 授權，方式與文字相同。


**-> 提示：** 在公共場合分享圖片等檔案時，移除多餘的元資料非常重要。這可能包含敏感資訊，例如位置資料、建立日期和作者詳細資訊。為了保護您的隱私，移除這些元資料是個好主意。為了簡化這項作業，您可以使用 [Exif Cleaner](https://exifcleaner.com/) 等專業工具，只需簡單的拖放動作，就能清理文件的元資料。


## 9 - 提出教程


當您完成以您選擇的語言撰寫教學後，下一步就是提交**Pull Request**。然後，管理員將使用我們的自動翻譯方法與人工校對，將缺少的翻譯添加到您的教學中。


若要繼續拉取請求，在儲存所有變更後，按一下「*貢獻*」按鈕，然後按一下「*開啟拉取請求*」：


![GITHUB](assets/fr/36.webp)


拉取請求 (Pull Request) 是將您分支中的變更整合到 Plan ₿ Network 套件庫主分支中的請求，它允許在變更合併前進行檢閱和討論。


繼續之前，請在 Interface 底部仔細檢查這些變更是否符合您的預期：


![GITHUB](assets/fr/37.webp)


確保在 Interface 的頂端，您的工作分支已合併到 Plan ₿ Network 套件庫的 `dev` 分支 (也就是主分支)。


輸入一個標題，簡單概括您希望與原始碼倉庫合併的變更。加入簡短的註解說明這些變更 (如果您有與建立教學相關的問題編號，記得註明 `關閉 #{ 問題編號}` 作為註解)，然後點選 Green 的「*建立拉取請求*」按鈕確認合併請求：


![GITHUB](assets/fr/38.webp)


您的 PR 將會在 Plan ₿ Network 主軟體倉庫的「*Pull Request*」標籤中顯示。現在您所要做的就是等待管理員聯絡您，確認您的貢獻已被合併，或要求任何進一步的修改。


![GITHUB](assets/fr/39.webp)


在將 PR 與主分支合併之後，我們建議刪除您的工作分支 (在我的範例中： `tuto-Green-Wallet`)，以保持 Fork 的歷史清白。GitHub 會自動在您的 PR 頁面上提供這個選項：


![GITHUB](assets/fr/40.webp)


如果您希望在提交 PR 之後變更您的供款，所需的步驟取決於您 PR 的目前狀態：




- 如果您的 PR 仍未合併，請在同一工作分支上進行變更。提交的變更會加入您仍未合併的 PR；
- 如果您的 PR 已經與主分支合併，您需要重新建立新的分支，然後再提交新的 PR。在繼續之前，請確認您的 Fork 與 `dev` 分支上的 Plan ₿ Network 原始碼倉庫同步。


如果您在提交教程時遇到技術困難，請不要猶豫，在 [我們專用的 Telegram 投稿群組](https://t.me/PlanBNetwork_ContentBuilder) 上尋求幫助。非常感謝您！