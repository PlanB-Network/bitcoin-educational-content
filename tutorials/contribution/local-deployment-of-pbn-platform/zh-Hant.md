---
name: 本地執行 Plan ₿ Network 平台指南
description: 如何在本機環境中執行 Plan ₿ Network，以測試我在 Plan ₿ Network 上的內容貢獻或教育內容的校對/審查？
---
![github](assets/cover.webp)


## 總結


本教學提供逐步指示，說明如何使用 Docker、假金鑰和自訂儲存庫組態，在本機電腦上從 Plan ₿ Network 設定 Bitcoin 學習管理系統。


如果您不瞭解上面的部分，別擔心，本教學就是為您準備的！


---

## **如何在本地執行 Bitcoin 學習管理系統**


本教學提供設定平台、處理假金鑰和自訂套件庫的詳細步驟。請遵循下列步驟，以避免常見問題並正確配置您的本機環境。



**1.先決條件**


- 已安裝 Docker 和 Docker Compose 的 Linux 機器 (據報導也可在 Windows 上運作)。
- 足夠的 `nodejs` 版本（測試：22.12.0）
- 您的系統上安裝了 `pnpm`。
- Git 已設定用於複製套件庫。



**2.複製儲存庫**

將套件庫複製到您的本機：


git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-learning-management-system


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3.設定環境變數**


1\.複製 `.env.example` 檔案：


```bash
cp .env.example .env
```


1.編輯 `.env` 檔案，刪除名稱中的 .example 部分，現在您必須加入所需變數的虛擬值。範例：


⚠️ 這是必經的步驟，跳過此步驟會導致錯誤，例如某些容器之間的連線拒絕。


別忘了在檔案中加入您專屬的 Github PAT



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**4.安裝相依性**


請務必安裝適當的 nodejs 版本。截至 2024-12，v22.12.0 (LTS) 已證實能正常運作。



⚠️ Ubuntu 22.04 儲存庫的 nodejs 版本為 12.22.9：太舊，無法讓您安裝 pnpm



要安裝 nodejs，請在 [這裡](https://nodejs.org/en/download/package-manager) 找到說明；例如，您可以選擇使用 `nvm` 安裝方法。


---

在開始 pnpm 安裝必要套件的階段之前，請確認已經安裝所有的相依套件，您可以執行下列指令來達到此目的：


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

在您的「.../Bitcoin-learning-management-system/」資料夾中，執行下列指令來安裝「pnpm


```bash
pnpm install
```


__TIP:__請記住不時更新相依性和 pnpm 本身



**5.執行容器**

在您的「.../Bitcoin-learning-management-system/」資料夾中，使用 Docker 啟動開發環境：


```bash
docker compose up --build -V
```

您也以這種方式執行下一個指令，就不會在終端機中看到日誌。

```bash
docker compose up -d --build -V
```


這將會從 dockers 建立並啟動所有必要的容器。


**6.存取應用程式**

容器運行後，請從以下位置存取前端：

\[<http://localhost:8181](http://localhost:8181)>


![Plan ₿ Network Local](assets/en/1.webp)


請注意：如果您變更任何原始檔案，應用程式會自動重新載入。



**7.** 設定您的資料庫 Schema


第一次執行時，您需要執行 DB 遷移。


若要執行，請執行遷移指令碼： `pnpm run dev:db:migrate`


```markdown
pnpm run dev:db:migrate
```


**8.從儲存庫匯入資料**

若要將資料匯入資料庫，請向 API 提出請求：


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9.修正同步卷存取問題**

如果遇到 `cdn` 和 `sync` 卷的存取問題，請執行：


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


再來


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Network Local](assets/en/2.webp)



**10.自訂儲存庫（可選）**

如果您需要使用 Fork 或特定分支：

1.編輯 `.env` 檔案以更新下列變數：


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


2\.重新啟動 Docker：


```markdown
docker compose down -v
docker compose up --build -V
```


3\.重新同步儲存庫資料：


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


本教程可確保平台已正確設定為具有假金鑰、已安裝相依性，以及已視需要自訂套件庫。祝您設定順利！


**命令額外幫助**


停止所有容器


```
docker compose down
```


修剪所有現有的容器和容量


```
docker container prune -f
docker volume prune --all
```


使用官方指南和午餐同步腳本中使用的相同指令重新建立容器：


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```