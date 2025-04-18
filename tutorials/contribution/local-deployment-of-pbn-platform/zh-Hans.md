---
name: 本地运行 Plan ₿ Network 平台指南
description: 如何在本地环境中运行 Plan ₿ Network，以测试我对 Plan ₿ Network 教育内容的贡献或校对/审核？
---
![github](assets/cover.webp)

## 综述

本教程将逐步说明如何使用 Docker、虚拟密钥和自定义资源库配置，在本地计算机上从 Plan ₿ Network 安装 Bitcoin 学习管理系统。

如果你不明白上面的部分，别担心，本教程就是为你准备的！

---
## **如何在本地运行 Bitcoin 学习管理系统**

本教程提供了设置平台、处理假密钥和自定义存储库的详细步骤。请按照以下步骤避免常见问题，并正确配置本地环境。

**1.先决条件**


- 安装了 Docker 和 Docker Compose 的 Linux 机器（据说也能在 Windows 上运行）。
- 足够的 `nodejs` 版本（测试：22.12.0）
- 系统上安装了 `pnpm`。
- Git 配置用于克隆软件源。

**2.克隆存储库**

将版本库克隆到本地计算机上：

git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-learning-management-system

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3.设置环境变量**

1\.复制 `.env.example` 文件：

```bash
cp .env.example .env
```

1.编辑`.env`文件，删除文件名中的.example 部分，现在必须为所需变量添加虚拟键。例如

⚠️ 这是强制性步骤，跳过该步骤将导致错误，如某些容器之间的连接被拒绝。

别忘了在文件中也添加你专用的 Github PAT

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4.安装依赖项**

请确保已安装合适的 nodejs 版本。截至 2024-12 年，v22.12.0 (LTS) 已被证明可以正常工作。

⚠️ Ubuntu 22.04 版本库的 nodejs 版本为 12.22.9：太旧，无法安装 pnpm

要安装 nodejs，请查阅说明 [此处](https://nodejs.org/en/download/package-manager)；例如，您可以选择使用 `nvm` 安装方法。

---
在开始 pnpm 安装必要软件包阶段之前，请确保已安装所有依赖包，可通过运行以下命令实现：

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
在 `../Bitcoin-learning-management-system/` 文件夹中运行以下命令安装 `pnpm

```bash
pnpm install
```

__TIP:__ 切记不时更新依赖项和 pnpm 本身

**5.运行容器**

在 `../Bitcoin-learning-management-system/` 文件夹中，使用 Docker 启动开发环境：

```bash
docker compose up --build -V
```

这样运行下一条命令，就不会在终端中看到日志。

```bash
docker compose up -d --build -V
```

这将通过 dockers 构建并启动所有必要的容器。

**6.访问应用程序**

容器运行后，请访问前端：

\[<http://localhost:8181](http://localhost:8181)>

![Plan ₿ Network Local](assets/en/1.webp)

注意：如果更改任何源文件，应用程序将自动重新加载。

**7.** 设置数据库 Schema

第一次运行时，需要运行数据库迁移。

为此，请运行迁移脚本： `pnpm run dev:db:migrate`

```markdown
pnpm run dev:db:migrate
```

**8.从资源库导入数据**

要将数据导入数据库，请向 API 提出请求：

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9.修复同步卷访问问题**

如果遇到访问 `cdn` 和 `sync` 卷的问题，请运行：

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

然后又

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)

**10.自定义存储库（可选）**

如果需要使用 Fork 或特定分支：

1.编辑 `.env` 文件，更新以下变量：

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\.重启 Docker：

```markdown
docker compose down -v
docker compose up --build -V
```

3\.重新同步存储库数据：

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

本教程可确保正确设置平台的假密钥、安装依赖项并根据需要自定义软件源。祝您设置成功！

**要求额外帮助**

停止所有容器

```
docker compose down
```

修剪所有现有容器和容量

```
docker container prune -f
docker volume prune --all
```

使用官方指南和午餐同步脚本中使用的相同命令重新创建容器：

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
