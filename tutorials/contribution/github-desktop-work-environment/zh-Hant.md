---
name: GitHub Desktop
description: 如何設定您的本機工作環境？
---
![github](assets/cover.webp)


PlanB 的使命是以盡可能多的語言提供有關 Bitcoin 的頂級教育資源。網站發佈的所有內容都是開放原始碼，並託管在 GitHub 上，任何人都可以參與豐富平台的內容。貢獻可以有多種形式：修正和校對現有的文字、翻譯成其他語言、更新資訊或創造我們網站上尚未提供的新教學。


如果您想為 PlanB Network 做出貢獻，您需要使用 GitHub 來提出變更。要做到這一點，您有兩個選項：


- 直接透過 GitHub 的網頁 **Interface** 貢獻：這是最簡單的方法。如果您是初學者，或只打算做幾個小貢獻，這個選項可能最適合您；
- 使用 **Git** 進行本地貢獻：如果您打算定期或大量貢獻 PlanB Network，這個方法比較適合。雖然在您的電腦上設定本機 Git 環境一開始可能看起來很複雜，但從長遠來看，這種方法更有效率。它可以更靈活地管理變更。如果您是新手，別擔心，**我們會在本教程中解釋設定環境的整個過程**（保證您不需要輸入任何命令行^^）。


如果您不知道 GitHub 是什麼，或者您想瞭解更多關於 Git 和 GitHub 的技術術語，我建議您閱讀我們的介紹文章，以熟悉這些概念。


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c




- 要開始，您顯然需要一個 GitHub 帳戶。如果您已經有一個，您可以登入，否則，您可以使用我們的教學來建立一個新帳戶。


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



## 步驟 1：安裝 GitHub 桌面



- 前往 https://desktop.github.com/ 下載 GitHub Desktop 軟體。此軟體可讓您輕鬆與 GitHub 進行互動，而無需使用終端機：

![github-desktop](assets/1.webp)


- 首次啟動軟體時，系統會要求您連接 GitHub 帳戶。要這樣做，請點選 `Sign in to GitHub.com`：

![github-desktop](assets/2.webp)


- 您的瀏覽器將會開啟認證頁面。輸入您在建立帳戶時選擇的電子郵件 Address 和密碼，然後按一下「登入」按鈕：

![github-desktop](assets/3.webp)


- 按一下「授權桌面」以確認您的帳戶與軟體之間的連線：

![github-desktop](assets/4.webp)


- 您將被自動重定向到 GitHub Desktop 軟體。點選「完成」： ![github-desktop](assets/5.webp)
- 如果您剛剛建立 GitHub 帳戶，您會被重定向到一個頁面，顯示您尚未建立任何儲存庫。此時，請將 GitHub Desktop 軟體放在一旁；我們稍後會再回到它： ![github-desktop](assets/6.webp)


## 步驟 2：安裝 Obsidian


讓我們繼續安裝寫作軟體。在這裡，您有幾個選擇。您需要支援編輯 Markdown 檔案的軟體，因為 PlanB Network 在其儲存庫中使用此格式的文字檔。


有許多專門編輯 Markdown 檔案的軟體，例如專門為撰寫而設計的 Typora。雖然並不理想，但也可以選擇程式碼編輯器，例如 Visual Studio Code (VSC) 或 Sublime Text。不過，身為一個作家，我比較喜歡使用 Obsidian 軟體。讓我們一起看看如何安裝並開始使用它。



- 前往 https://obsidian.md/download 下載軟體： ![github-desktop](assets/7.webp)
- 安裝 Obsidian、啟動軟體、選擇您的語言，然後點選「快速開始」： ![github-desktop](assets/8.webp)
- 您將抵達 Obsidian 軟體。目前，您尚未開啟任何檔案： ![github-desktop](assets/9.webp)


## 步驟 3：Fork PlanB Network 儲存庫



- 前往 PlanB Network 資料儲存庫，網址如下 Address：[https://github.com/PlanB-Network/Bitcoin-educational-content](https://github.com/PlanB-Network/Bitcoin-educational-content)：![github-desktop](assets/10.webp)
- 從本頁面，按一下視窗右上方的 `Fork`按鈕：![github-desktop](assets/11.webp)
- 在建立選單中，您可以不使用預設設定。確定已勾選「僅複製開發分支」方塊，然後按一下「建立 Fork」按鈕： ![github-desktop](assets/12.webp)
- 然後您就會到達 PlanB Network 儲存庫的 Fork：![github-desktop](assets/13.webp)

這個 Fork 構成一個獨立於原始資源庫的資源庫，儘管它目前包含相同的資料。您現在將在這個新的儲存庫上工作。


在某種程度上，我們製作了 PlanB Network 原始碼庫的複本。您的 Fork（複本）和原始資源庫現在將獨立發展。在原始資源庫中，其他貢獻者可能會新增資料，而您的 Fork 則會進行自己的修改。

為了維持這兩個套件庫的一致性，有必要定期同步它們，使它們擷取相同的資訊。若要將變更傳送給源套件庫，您會使用所謂的 **Pull Request**。要將源套件庫中的變更整合到 Fork 中，您需要使用 GitHub Web Interface 上的 **Sync Fork** 指令。

![github-desktop](assets/14.webp)


## 步驟 4：複製 Fork



- 返回 GitHub 桌面軟件。現在，您的 Fork 應該出現在 `您的儲存庫` 部分。如果您沒有立即看到，請使用雙箭頭按鈕刷新清單。當您的 Fork 出現時，請按一下以選取它：

![github-desktop](assets/15.webp)


- 然後按一下藍色按鈕：複製 [使用者名稱]/Bitcoin-educational-content`：

![github-desktop](assets/16.webp)


- 保留預設路徑。若要確認，請按一下藍色的 `Clone` 按鈕：

![github-desktop](assets/17.webp)


- 等待 GitHub Desktop 在本機複製您的 Fork：

![github-desktop](assets/18.webp)


- 複製套件庫之後，軟體會提供您兩個選項。您必須選擇第一個：「貢獻給父專案」。這個選擇將允許您將未來的工作作為對父專案 (`PlanB-Network/Bitcoin-educational-content`)的貢獻來呈現，而不是完全作為您個人 Fork (`[使用者名稱]/Bitcoin-educational-content`)的修改。選取選項後，點選 `繼續`：

![github-desktop](assets/19.webp)


- 您的 GitHub 桌面現在已經配置完成。現在，您可以讓軟體在背景中開啟，跟隨我們要做的修改。

![github-desktop](assets/20.webp)

我們在此階段所達成的，是建立您的原始碼庫的本機複本，並將其託管在 GitHub 上。提醒您一下，這個套件庫是 PlanB Network 原始套件庫的 Fork。您將能夠對此本地副本進行修改，例如新增教學、翻譯或修正。一旦完成這些修改，您就可以使用 **Push origin** 指令，將本機的修改內容傳送至 GitHub 上的 Fork。


您也可以從 Fork 擷取修改，例如在與 PlanB Network 儲存庫同步時。為此，您會使用 **Fetch origin** 指令將修改下載到您的本機複本 (您的 clone)，然後再使用 **Pull origin** 指令將修改與您的工作合併。這可讓您在有效貢獻的同時，隨時掌握專案的最新發展。


![github-desktop](assets/21.webp)

## 步驟 5：建立新的 Obsidian 保險庫



- 開啟 Obsidian 軟體，按一下視窗左下方的小保險庫圖示：

![github-desktop](assets/22.webp)


- 按一下「開啟」按鈕，將現有資料夾開啟為儲存庫： ![github-desktop](assets/23.webp)
- 您的檔案總管將會打開。您需要找到並選擇名為`GitHub`的資料夾，它應該在您的`Documents`目錄下的檔案中。此路徑與您在步驟 4 中建立的路徑一致。選擇資料夾後，確認其選擇。然後，在 Obsidian 上建立儲存庫的動作會在軟體的新頁面上啟動：


![github-desktop](assets/24.webp)

-> **注意**，在 Obsidian 中建立新的儲存庫時，請務必不要選擇 `Bitcoin-educational-content`資料夾。請選擇父資料夾 `GitHub`。如果您選擇 `Bitcoin-educational-content` 資料夾，包含您本機 Obsidian 設定的設定資料夾 `.obsidian` 會自動整合到儲存庫中。我們希望避免這種情況，因為不需要將您的 Obsidian 設定轉移到 PlanB Network 套件庫。另一個方法是將 `.obsidian`資料夾加入`.gitignore`檔，但這個方法也會修改原始碼倉庫的`.gitignore`檔，這並不可取。



- 在視窗左側，您可以看到檔案樹，裡面有您在本地複製的不同 GitHub 套件庫。
- 按一下資料夾名稱旁邊的箭頭，即可展開資料夾以存取儲存庫的子資料夾及其文件：

![github-desktop](assets/25.webp)


- 別忘了將 Obsidian 設定為黑暗模式：「光線會吸引蟲子」 ;)


## 步驟 6：安裝程式碼編輯器


您大部分的修改都會在 Markdown 格式 (`.md`)的檔案上進行。要編輯這些文件，您可以使用我們之前討論過的 Obsidian 軟體。然而，PlanB Network 使用其他檔案格式，您需要修改其中一些格式。


例如，當您建立一個新的教學時，您需要建立一個 YAML (`.yml`)檔案來輸入您教學的標籤、它的標題和您的教師 ID。Obsidian 不提供修改此類檔案的功能，因此您需要使用程式碼編輯器。


對於這一點，有幾個選項可供您選擇。雖然可以使用電腦的標準記事本進行這些修改，但對於整潔的工作而言，此解決方案並不理想。我建議您選擇專為此目的設計的軟體，例如 [VS Code](https://code.visualstudio.com/download) 或 [Sublime Text](https://www.sublimetext.com/download)。Sublime Text 特別輕巧，足以滿足我們的需求。


- 安裝這些軟體中的一個，將它放在一旁以備您日後修改。![github-desktop](assets/26.webp)

恭喜您！您的工作環境已經設定好，可以為 PlanB Network 投稿。現在您可以針對每種貢獻方式(翻譯、校對、寫作......)探索我們其他特定的教學。


https://planb.network/tutorials/others

..).