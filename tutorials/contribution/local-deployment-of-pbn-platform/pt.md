---
name: Guia para executar a plataforma Plan ₿ Network localmente
description: Como é que podem executar o Plan ₿ Network num ambiente local para testar a minha contribuição de conteúdos ou a revisão/revisão de conteúdos educativos no Plan ₿ Network?
---
![github](assets/cover.webp)

## Em resumo

Este tutorial fornece instruções passo a passo para configurar o Bitcoin Learning Management System do Plan ₿ Network em sua máquina local usando o Docker, chaves fictícias e configurações de repositório personalizadas.

Se não percebeu a parte acima, não se preocupe - este tutorial é para si!

---
## **Como executar localmente o Sistema de Gestão de Aprendizagem Bitcoin

Este tutorial fornece etapas detalhadas para configurar a plataforma, lidar com chaves fictícias e personalizar repositórios. Siga as etapas abaixo para evitar problemas comuns e configurar corretamente seu ambiente local.

**1. Pré-requisitos**


- Máquina Linux com o Docker e o Docker Compose instalados (também foi relatado que funciona no Windows).
- versão suficiente do `nodejs` (testado: 22.12.0)
- `pnpm` instalado no seu sistema.
- Git configurado para clonagem de repositórios.

**2. Clonar o Repositório**

Clone o repositório para o seu computador local:

git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-learning-management-system

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3. Configurar as variáveis de ambiente**

1\. Duplicar o ficheiro `.env.example`:

```bash
cp .env.example .env
```

1. Edite o arquivo `.env`, apagando a parte .example do nome, agora você tem que incluir chaves fictícias para as variáveis necessárias. Exemplo:

⚠️ Este passo é obrigatório. Se não o fizer, surgirão erros como a recusa de ligação entre alguns dos contentores.

Não se esqueça de adicionar também o seu PAT dedicado do Github no ficheiro

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4. Instalar dependências**

certifique-se de ter instalado uma versão adequada do nodejs. A partir de 2024-12, a versão 22.12.0 (LTS) está comprovadamente funcionando.

⚠️ A versão do repositório nodejs do Ubuntu 22.04 é 12.22.9: demasiado antiga para permitir a instalação do pnpm

Para instalar o nodejs, encontre instruções [aqui] (https://nodejs.org/en/download/package-manager); por exemplo, pode optar por utilizar o método de instalação `nvm`.

---
Antes de iniciar a fase de instalação do pnpm dos pacotes necessários, certifique-se de que tem todas as dependências instaladas, o que pode conseguir executando o seguinte comando:

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
Dentro da sua pasta `../Bitcoin-learning-management-system/`, execute o seguinte comando para instalar o `pnpm`

```bash
pnpm install
```

__TIP:__ Lembre-se de atualizar periodicamente as dependências e o próprio pnpm

**5. Executar os contentores**

Dentro da sua pasta `../Bitcoin-learning-management-system/`, inicie o ambiente de desenvolvimento com o Docker:

```bash
docker compose up --build -V
```

Se também executar este comando seguinte desta forma, não verá os registos no seu terminal.

```bash
docker compose up -d --build -V
```

Isto irá construir e iniciar todos os contentores necessários a partir de dockers.

**6. Aceder à aplicação**

Quando os contentores estiverem a funcionar, aceda ao frontend em:

\[<http://localhost:8181](http://localhost:8181)>

![Plan ₿ Network Local](assets/en/1.webp)

Nota: a aplicação será automaticamente recarregada se alterar algum ficheiro de origem.

**Configurar a base de dados Schema

Na primeira execução, terá de executar as migrações de BD.

Para o fazer, execute o script de migração: `pnpm run dev:db:migrate`

```markdown
pnpm run dev:db:migrate
```

**8. Importar dados do repositório**

Para importar dados para a base de dados, faça um pedido à API:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9. Corrigir problemas de acesso ao volume de sincronização**

Se encontrar problemas de acesso com os volumes `cdn` e `sync`, execute:

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

e depois:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)

**10. Personalizar o repositório (opcional)**

Se precisar de utilizar um Fork ou um ramo específico:

1. Edite o ficheiro `.env` para atualizar as seguintes variáveis:

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\. Reinicie o Docker:

```markdown
docker compose down -v
docker compose up --build -V
```

3\. Re-sincronizar os dados do repositório:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

Este tutorial garante que a plataforma esteja configurada corretamente com chaves fictícias, dependências instaladas e repositórios personalizados conforme necessário. boa sorte com a sua configuração!

**Comandos para ajuda extra

parar todos os contentores

```
docker compose down
```

podar todos os contentores e volumes existentes

```
docker container prune -f
docker volume prune --all
```

recriar os contentores com o mesmo comando utilizado no guia oficial e no script de sincronização do almoço:

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
