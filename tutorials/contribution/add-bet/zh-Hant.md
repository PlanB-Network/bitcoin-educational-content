---
name: 新增教育工具
description: 如何在 PlanB Network 上新增教材？
---
![event](assets/cover.webp)


PlanB 的使命是以儘可能多的語言提供有關 Bitcoin 的領先教育資源。網站發佈的所有內容都是開放原始碼，並託管於 GitHub，讓任何人都能參與豐富平台的內容。


除了教程和培訓，PlanB Network 還提供了一個關於 Bitcoin 的龐大資料庫，其中包含了各種各樣的教育內容，每個人都可以訪問，[在 "BET" (_Bitcoin Educational Toolkit_) 部分](https://planb.network/resources/bet)。這個資料庫包括教育海報、memes、幽默宣傳海報、技術圖表、標誌和其他用戶工具。此舉的目的是支援世界各地教授 Bitcoin 的個人和社群，為他們提供必要的視覺資源。


您想參與豐富這個資料庫，但不知道如何進行嗎？本教學就是為您準備的！


*所有整合到網站上的內容必須是無權或尊重原始檔案的授權。此外，PlanB Network 發佈的所有視覺圖片均以 [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) 授權提供。*

![event](assets/01.webp)


- 首先，您需要擁有一個 GitHub 帳戶。如果您不知道如何建立帳號，我們已為您準備了詳細的教學。


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- 到 `resources/bet/` 區的 [PlanB 專用於資料的 GitHub 儲存庫](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/bet)：

![event](assets/02.webp)


- 按一下右上方的「新增檔案」按鈕，然後按一下「建立新檔案」：

![event](assets/03.webp)


- 如果您之前從未貢獻過 PlanB Network 的內容，您需要建立原始套件庫的 Fork。Forking 倉庫意味著在您自己的 GitHub 帳戶上創建該倉庫的副本，這樣您就可以在不影響原始倉庫的情況下進行專案工作。點擊 `Fork this repository` 按鈕：

![event](assets/04.webp)


- 然後您就會到達 GitHub 編輯頁面：

![event](assets/05.webp)


- 為您的內容建立資料夾。要這樣做，請在「為您的檔案命名...」方塊中，以小楷寫下您的內容名稱，並以破折號取代空格。在我的範例中，比方說我要新增 2048 字 BIP39 清單的 PDF 視圖。因此，我會將我的資料夾命名為 `bip39-wordlist`: ![event](assets/06.webp)
- 若要確認資料夾是否已建立，只要在同一方塊中的名稱後加上斜線即可，例如： `bip39-wordlist/`。加入斜線會自動建立資料夾，而非檔案：

![event](assets/07.webp)


- 在此資料夾中，您將建立第一個 YAML 檔案，名稱為 `bet.yml`：

![event](assets/08.webp)


- 使用此範本將內容相關資訊填入此檔案：


```yaml
builder:
type:
links:
download:
view:
- en:
tags:
-
-
contributors:
-
```


以下是每個欄位需要填寫的詳細資料：



- `builder`**：表示您的組織在 PlanB Network 上的識別碼。如果您的公司還沒有 "builder "識別碼，您可以按照本教學建立一個。


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

如果您沒有個人資料，您可以直接使用您的姓名、假名或公司名稱，而無需建立建立者個人資料。



- `type`**：在下列兩個選項中選擇您內容的性質：
 - `教育內容'用於教育內容。
 - 其他類型的多樣內容的 ` 視覺內容



- `links`**：提供您內容的連結。您有兩個選項：
 - 如果您選擇直接在 PlanB 的 GitHub 上託管您的內容，您需要在下列步驟中將連結加入此檔案。
 - 如果您的內容寄存在其他地方，例如您的個人網站，請在此標明相應的連結：
     - `下載`：下載內容的連結。
     - `view`：檢視內容的連結 (可與下載連結相同)。如果您的內容有多種語言版本，請為每種語言加入一個連結。



- `tags`**：新增兩個與內容相關的標籤。範例：
 - Bitcoin
 - 技術
 - 經濟
 - 教育
 - meme...



- `contributors`**：如果您有貢獻者識別碼，請提及。


例如，您的 YAML 檔案可以如下所示：


```yaml
builder: PlanB-Network
type: Educational Content
links:
download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
view:
- In my example, I will leave the links empty for now, as I will add my PDF directly on GitHub:
![event](assets/09.webp)
- Once your modifications to this file are complete, save them by clicking on the `Commit changes...` button:
![event](assets/10.webp)
- Add a title for your modifications, as well as a short description:
![event](assets/11.webp)
- Click on the green `Propose changes` button:
![event](assets/12.webp)
- You will then arrive on a page that summarizes all your changes:
![event](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![event](assets/14.webp)
- Select your fork of the PlanB Network repository:
![event](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It is probably called `patch-1`. Click on it:
![event](assets/16.webp)
- You are now on your working branch (**make sure you are on the same branch as your previous modifications, this is important!**):
![event](assets/17.webp)
- Go back to the `resources/bet/` folder and select the folder of your content that you just created in the previous commit:
![event](assets/18.webp)
- In the folder of your content, click on the `Add file` button, then on `Create new file`:
![event](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![event](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`: ![event](assets/21.webp)
- Click on the `Commit changes...` button: ![event](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/23.webp)
- Return to the `assets` folder: ![event](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`: ![event](assets/25.webp)
- A new page will open. Drag and drop a thumbnail that represents your content into the area. This image will be displayed on the PlanB Network site: ![event](assets/26.webp)
- It can be a preview, a logo, or an icon: ![event](assets/27.webp)
- Once the image is uploaded, make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/28.webp)
- Be careful, your image must be named `logo` and must be in `.webp` format. The full file name should therefore be: `logo.webp`: ![event](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`: ![event](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`: ![event](assets/31.webp)
- Make sure you are still on the same working branch, then click on the `Commit changes` button: ![event](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`: ![event](assets/33.webp)
- Return to the folder of your content: ![event](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`: ![event](assets/35.webp)
- Create a new YAML file by naming it with the indicator of your native language. This file will be used for the content description. For example, if I want to write my description in English, I will name this file `en.yml`: ![event](assets/36.webp)
- Fill out this YAML file using this template:

```

name:
description: |

```

- For the `name` key, you can add the name of your content;
- For the `description` key, you simply need to add a short paragraph that describes your content. The description must be in the same language as the file name. You do not need to translate this description into all the supported languages on the site, as the PlanB teams will do so with their model.
For example, here is what your file might look like:

```

name: BIP39 WORDLIST
description: |
用於編碼 Mnemonic 詞組的 BIP39 字典中的 2048 個英文詞彙的完整和編號清單。該文件可打印在單一頁面上。

```

![event](assets/37.webp)
- Click on the `Commit changes...` button:
![event](assets/38.webp)
- Ensure that the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![event](assets/39.webp)
- Your content folder should now look like this:
![event](assets/40.webp)

---

*If you prefer not to add the content on GitHub and you have already noted the links in the `bet.yml` file during the previous steps, you can skip this section and go directly to the part concerning the creation of the Pull Request.*

- Return to the `/assets` folder:
![event](assets/41.webp)
- Click on the `Add file` button, then on `Upload files`:
![event](assets/42.webp)
- A new page will open. Drag and drop into the area the content you wish to share:
![event](assets/43.webp)
- For example, I added the PDF file of the BIP39 list:
![event](assets/44.webp)
- Once the content is uploaded, ensure that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![event](assets/45.webp)
- Return to your `/assets` folder and click on the file you just uploaded:
![event](assets/46.webp)
- Retrieve the intermediate URL of your file. For example, in my case, the URL is:

```

https://github.com/tutorial-pandul/Bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Keep only the last part of the URL from `/resources` onwards:

```

/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Add to the base of the URL the following information to have the correct link:

```

https://github.com/DiscoverBitcoin/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```