---
name: Plan ₿ Network 教授
description: 如何在 Plan ₿ Network 上新增或修改教師檔案？
---
![cover](assets/cover.webp)


如果您打算透過撰寫新的教學或課程來貢獻 Plan ₿ Network，您將需要一個教師檔案。此設定檔可讓您為貢獻至平台的內容取得適當的學分。


對於那些已經參與製作 Plan ₿ Network 上教育內容的人，您可能已經有一個教師檔案。您可以在 `/professors` 資料夾 [我們的 GitHub 套件庫](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors) 中找到它。如果您的設定檔已經存在，請在 `professor.yml` 檔案中找到您的登入帳號。


若要變更您的個人資料，請前往本教學結尾的「編輯您的教師個人資料」部分。


## 使用我們的軟體新增教師


在 Plan ₿ Network 上建立教師檔案的最簡單方法是使用我們整合的 Python 工具。以下是它的工作方式。


### 1 - 設定您的本機環境


您必須從 [GitHub 上的 Plan ₿ Network 套件庫](https://github.com/PlanB-Network/Bitcoin-educational-content) 擁有自己的 Fork。


將 Fork 的主分支 (`dev`)與原始碼套件庫同步。


更新您的本機複製檔。


```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```


### 2 - 建立新的分支


確定您在 `dev` 分支上。以描述性的名稱建立新的分支 (例如 `add-professor-loic-morel`)。


在您的 Fork 網路上發佈此分支。


```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```


### 3 - 建立您的教師簡介


前往您本機複製檔上的 `scripts/tutorial-related/data-creator/` 資料夾。確保您已安裝軟體所需的所有相依性，並已先安裝 Python ：


```bash
pip install -r requirements.txt
```


然後使用命令 ：


```bash
python3 main.py
```


進入首頁後，輸入您的複製套件庫的本機路徑、您正在撰寫的語言以及您的 GitHub ID。如果您是為他人建立此個人資料，並且已經擁有教授的個人資料，請在 "*PBN Professor's ID*"欄位中輸入您的 ID。如果您正在建立自己的個人資料，您還沒有教授的 ID，因為您正在建立教授的 ID，所以請將此欄位留空。


然後按一下「*新教授*」按鈕。


![Image](assets/fr/01.webp)


填寫所需資訊（請注意，所有這些資訊都會在我們的平台以及 GitHub 上公開）：




- 您的教師檔案名稱（使用您的名字和姓氏或假名，小寫） ；
- 您的姓名或暱稱 ；
- 您的網站和個人資料 X (選用) ；
- 接受讀者捐款的 Lightning Address (選項) ；
- 從清單中選取 2 或 3 個標籤；
- 按一下「*選擇圖片*」，從您的本機資料夾中選擇一張設定檔圖片（可使用任何名稱和格式的圖片，軟體會自動適應。只要確定圖片是正方形即可）；
- 撰寫簡短的個人資料說明。


按一下「*建立教授*」以完成建立。這將自動 generate 您個人檔案所需的所有檔案。


![Image](assets/fr/02.webp)


在本地儲存您的變更，建立一個附有說明資訊的提交。將變更推送至您的 Fork GitHub。


```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```


完成後，在 GitHub 上建立一個 Pull Request (PR)，建議整合您的修改。在 PR 中加入標題和簡短說明。


### 4 - 校對與合併


等待管理員的驗證或回饋。如有必要，進行修正並推送新的提交。


```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```


一旦 PR 已經合併，您就可以刪除工作分支。


## 修改您的教師簡介


如果您已掌握 Git 的使用方法，可直接在現有資料夾中建立新的分支並編輯相關檔案，以修改您的教師設定檔。修改可以在 `professor.yml` 檔案或 markdown 檔案中進行，視需要修正的資訊而定。當您在本機完成變更後，請將它們推送到您的 Fork 並提交 PR。


對於初學者，我建議直接透過 GitHub 的 Interface web 進行修改。確保您有一個 GitHub 帳戶。如果您不知道如何建立帳號，請遵循此教學 ：


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
前往 [專門提供資料的 Plan ₿ Network GitHub 資源庫](https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors)。


![Image](assets/fr/03.webp)


按一下「*教授*」資料夾，然後到您的個人資料夾。


![Image](assets/fr/04.webp)


若要變更您的個人資料元資料，例如 Lightning Address、名稱或連結，請選擇「*professor.yml*」檔案。若要變更您的描述，請點選您語言的 YAML 檔案 (例如「*en.yml*」或「*fr.yml*」)。


如果您修改您的描述，請記得移除所有過時的翻譯。然後，您可以在 LLM 的協助下將您的描述翻譯成其他語言，或是只保留您母語的描述，並在您的 Pull Request 中提及您的描述需要我們團隊的翻譯。


![Image](assets/fr/05.webp)


在您要修改的檔案上，按一下鉛筆圖示。


![Image](assets/fr/06.webp)


如果您還沒有 Plan ₿ Network 倉庫中的 Fork，GitHub 會建議您建立一個。點選「*Fork this repository*」。


![Image](assets/fr/07.webp)


對檔案進行所需變更。完成後，按一下「*提交變更*」。


![Image](assets/fr/08.webp)


輸入描述變更的訊息，然後選擇「*提出變更」。


![Image](assets/fr/09.webp)


您的變更摘要將會顯示。如果您希望對您的設定檔做進一步的變更，您可以返回資料夾並做進一步的提交。完成後，按一下「*建立拉取請求*」。


拉取請求（Pull Request）是將您的分支中的變更整合到 Plan ₿ Network 套件庫的主分支中的請求，允許在合併之前檢閱和討論變更。


![Image](assets/fr/10.webp)


確保在 Interface 的頂端，您的工作分支與 Plan ₿ Network 套件庫的 `dev` 分支 (也就是主分支) 合併。


輸入一個標題，簡要概括您希望與原始碼倉庫合併的變更。加入簡短的註解描述這些變更，然後按一下 Green 的「*建立拉取請求*」按鈕確認拉取請求：


![Image](assets/fr/11.webp)


您的 PR 將會在 Plan ₿ Network 主套件庫的「*Pull Request*」標籤中顯示。現在您要做的就是等待管理員合併您的修改。


![Image](assets/fr/12.webp)


如果您在提交變更時遇到任何技術困難，請不要猶豫，在 [我們專門用於貢獻的 Telegram 群組](https://t.me/PlanBNetwork_ContentBuilder) 上尋求協助。非常感謝您！