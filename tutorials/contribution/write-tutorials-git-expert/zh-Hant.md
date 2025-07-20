---
name: 貢獻 - Git 教學 (進階)
description: 為進階使用者提供 Plan ₿ Network 與 Git 的教學指南
---
![cover](assets/cover.webp)


在按照本教學添加新教學之前，您需要完成幾個初步步驟。如果您還沒有完成，請先看一下這個入門教學，然後再回到這裡：


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

您已經擁有 ：



- 為您的教學選擇一個主題；
- 透過 [Telegram 群組](https://t.me/PlanBNetwork_ContentBuilder) 或 paolo@planb.network 聯絡 Plan ₿ Network 團隊；
- 選擇您的貢獻工具。


在這篇給有經驗的 Git 用戶的教學中，我們將簡要總結提供新的 Plan ₿ Network 教學的關鍵步驟和基本方針。如果您不熟悉 Git 和 GitHub，我建議您參考另外 2 個更詳細的教學，它們會一步一步地教您：



- 中級 (GitHub 桌面) ：


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- 初學者 (web Interface) ：


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## 建議工具


用於編輯 Markdown 檔案 ：



- 黑曜石 (免費，非開放源碼)
- 標記文字 (免費、開放源碼)
- Zettlr (免費、開放源碼)
- Typora (付費軟體，~15 歐元，非開放源碼)


適用於 Git ：



- Git (免費、開放源碼)
- GitHub 桌面（免費、開放源碼）
- Sourcetree (免費，非開放源碼)


用於編輯 YAML 檔案 ：



- Visual Studio Code (免費、開放源碼)
- Sublime Text（免費但有限制，非開放源碼）


建立圖表和視覺效果：



- Canva (免費且有付費選項，非開放源碼)
- Inkscape (免費、開放源碼)
- Penpot (免費、開放源碼)


## 工作流程


### 1 - 設定您的本機環境



- 您必須擁有 [GitHub 上的 Plan ₿ Network 套件庫](https://github.com/PlanB-Network/Bitcoin-educational-content) 的 Fork。
- 將 Fork 的主分支 (`dev`)與原始碼套件庫同步。
- 更新您的本機複製檔。


```
# Clone your fork (if not already done)
git clone https://github.com/<your-username>/bitcoin-educational-content.git
cd bitcoin-educational-content

# Add the source repository as a remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git

# Fetch the latest changes from the source repository
git fetch upstream

# Switch to the main 'dev' branch
git checkout dev

# Merge the changes from the source repository's 'dev' branch into your fork
git merge upstream/dev

# Push the updates to your fork on GitHub
git push origin dev
```


### 2 - 建立新的分支



- 確定您在 `dev` 分支上。
- 以描述性的名稱建立新的分支 (例如 `tuto-Green-Wallet-loic`)。
- 在您的線上 Fork 上發佈此分支。


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - 新增教學文件


***註：*** 您可以使用 [我的 Python GUI 腳本](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation) 自動執行第 3 步和第 4 步。直接從本機 clone 中的資料夾執行，然後在 GUI 上填入所需欄位。有關如何安裝和使用的詳細資訊，請參閱 [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md)。


如果您喜歡手動操作，請遵循以下步驟 ：



- 在本機資源庫中找到適當的資料夾 (例如 `tutorials/Wallet`)。
- 建立一個專門用於教學的目錄，並使用明確的名稱 (例如 `Green-Wallet`)。此資料夾名稱也將決定教學的 URL 路徑。資料夾名稱應使用小寫，不能有特殊符號（連字符除外），也不能有空格。
- 將下列項目新增至此目錄：
    - 一個名為 `assets` 的子資料夾，包含 ：
        - 兩個 `.webp` 影像：
            - `logo.webp`：教學標誌 (有背景的正方形格式)。此標誌必須代表所介紹的軟體或工具。如果教程不是特定於某個工具 (例如：產生 Mnemonic 詞組的一般指南)，您可以選擇一個合適的視覺 (例如：一般圖示)。
            - `cover.webp`：在教學開始時顯示的封面圖片。
        - 包含教學原始語言代碼的子資料夾。例如，如果教學以英文撰寫，此子資料夾應命名為 `en'。將教學的所有視覺資料（圖表、影像、螢幕截圖等）放入此資料夾。
    - 包含元資料 (作者、標籤、類別、難度等) 的 `tutorial.yml` 檔案。
    - 包含教學的 Markdown 檔案，根據語言代碼命名 (例如 `fr.md`、`en.md` 等)。


```
# Navigate to the appropriate folder
cd tutorials/wallet

# Create the directory dedicated to the tutorial
mkdir green-wallet
cd green-wallet

# Create the 'assets' subfolder
mkdir -p assets

# Create the subfolder for the original language code (e.g., 'en' for English)
mkdir -p assets/en

# Create the metadata file and the Markdown tutorial file (e.g., 'en.md' for English)
touch tutorial.yml en.md
```


### 4 - 填寫 YAML 檔案



- 按以下方式完成 `tutorial.yml` 檔案：


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



- project_id** ：教程中展示的工具背後的公司或組織的 UUID [來自專案清單](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects)。例如，如果您要建立一個關於 Green Wallet 軟體的教學，您可以在下列檔案中找到這個 `project_id`：`Bitcoin-educational-content/resources/projects/blockstream/project.yml`。此資訊會加入到您的教學 YAML 檔案中，因為 Plan ₿ Network 會維護所有在 Bitcoin 或相關專案上運作的公司和組織的資料庫。透過加入連結到您教學的實體的「project_id」，您就在兩個 Elements 之間建立了連結；



- 標籤** ：從 Plan ₿ Network 標籤清單中](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) 獨家選取 2 或 3 個與教學內容相關的關鍵字；



- 類別** ：根據 Plan ₿ Network 網站結構，與教學內容對應的子類別（例如，對於錢包：`桌面`、`硬體`、`行動`、`備份`）；



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


### 5 - 撰寫內容



- 使用 ：
    - 標題 (`name`)。
    - 簡短說明 (`description`)。
- 使用 Markdown 語法在教學頂端新增封面圖片 (將 "Green" 改為所示工具的名稱)：


```
![cover-green](assets/cover.webp)
```



- 以 Markdown 撰寫教學內容：
    - 使用結構良好的標題 (`##`)、清單和段落。
    - 使用 Markdown 語法插入視覺效果：


```
![nom-image](assets/en/001.webp)
```




- 將圖表和影像放入相對應的語言子資料夾，位於 `/assets`。


### 6 - 儲存並提交教學



- 透過建立具有描述性訊息的提交，在本機儲存您的變更。
- 將變更推送至您的 GitHub Fork。


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- 完成後，在 GitHub 上建立一個 Pull Request (PR)，建議整合您的修改。
- 在 PR 中加入標題和簡短說明。在註解中提及對應的問題編號。


### 7 - 校對與合併



- 等待管理員的驗證或回饋。
- 如有必要，進行修正並推送新的提交。


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- 一旦 PR 已經合併，您就可以刪除工作分支。


## 內容建立標準



- 平台支援的格式化** ：
    - 經典 Markdown：列表、連結、影像、引文、粗體、斜體等。
    - LaTeX (僅限區塊，不得內嵌)：以 `$$` 分隔。
    - 內嵌程式碼：語法帶有單一反擊符號。
    - 程式碼區塊：有三個反標記的語法，例如 ：


```
print("Hello, Bitcoin!")
```



- 插圖和圖表** ：
    - 所有影像必須為 WebP 格式。如有需要，請使用此免費工具進行轉換：[ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - 以 2 或 3 位數命名視覺效果 (例如 `001.webp`、`002.webp`)。
    - 對於行動或 Hardware Wallet 教學，請使用模型。
    - 僅使用自行製作或免版稅的視覺效果。
    - 確保它們是相關且高品質的。
- 圖形章程** ：
    - 字型：[Rubik](https://fonts.google.com/specimen/Rubik).
    - 顏色 Plan ₿ Network ：
        - 橙色: `#FF5C00`
        - 黑色: `#000000`
        - 白色：`#FFFFFF


如果您在提交教程時遇到技術困難，請不要猶豫，在 [我們專用的 Telegram 投稿群組](https://t.me/PlanBNetwork_ContentBuilder) 上尋求幫助。非常感謝您！