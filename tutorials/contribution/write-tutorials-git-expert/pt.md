---
name: Contribuição - Tutorial Git (avançado)
description: Guia para utilizadores avançados para oferecer um tutorial sobre o Plano ₿ Rede com o Git
---
![cover](assets/cover.webp)

Antes de seguir este tutorial sobre como adicionar um novo tutorial, é necessário ter concluído algumas etapas preliminares. Se ainda não o fez, consulte primeiro este tutorial introdutório e depois volte aqui:

https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Já tem :


- Escolha um tema para o seu tutorial;
- Contactou a equipa do Plano ₿ Network através do [grupo Telegram] (https://t.me/PlanBNetwork_ContentBuilder) ou paolo@planb.network ;
- Escolha as suas ferramentas de contribuição.

Neste tutorial para usuários experientes do Git, vamos resumir brevemente as principais etapas e diretrizes essenciais para oferecer um novo tutorial Plan ₿ Network. Se você não estiver familiarizado com o Git e o GitHub, recomendo que você siga um desses outros 2 tutoriais mais detalhados que o levarão passo a passo :


- Intermediário (GitHub Desktop)** :

https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Iniciantes (interface web)** :

https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Ferramentas sugeridas

Para editar ficheiros Markdown :


- Obsidian** (Gratuito, não de código aberto)
- Mark Text** (gratuito, de fonte aberta)
- Zettlr** (gratuito, de código aberto)
- Typora** (Payware, ~15€, não é de código aberto)

Para Git :


- Git** (gratuito, de código aberto)
- GitHub Desktop** (gratuito, de código aberto)
- Sourcetree** (Gratuito, não de fonte aberta)

Para editar ficheiros YAML :


- Visual Studio Code** (gratuito, de fonte aberta)
- Sublime Text** (gratuito com limitações, não é de código aberto)

Para criar diagramas e imagens :


- Canva** (gratuito com opções pagas, não é de código aberto)
- Inkscape** (gratuito, de código aberto)
- Penpot** (gratuito, de código aberto)

## Fluxos de trabalho

### 1 - Configurar o seu ambiente local


- Tem de ter a sua própria bifurcação do repositório [Plan ₿ Network no GitHub] (https://github.com/PlanB-Network/bitcoin-educational-content).
- Sincroniza o ramo principal (`dev`) da sua bifurcação com o repositório de código fonte.
- Actualize o seu clone local.

```
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<votre-nom-utilisateur>/bitcoin-educational-content.git
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

### 2 - Criar uma nova sucursal


- Certifique-se de que está no ramo `dev`.
- Crie um novo ramo com um nome descritivo (por exemplo, `tuto-green-wallet-loic`).
- Publique este ramo na sua bifurcação em linha.

```
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Adicionar os documentos do tutorial

***Nota:*** Pode automatizar os passos 3 e 4 utilizando [o meu script Python GUI](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Execute-o diretamente a partir da sua pasta no seu clone local e, em seguida, preencha os campos necessários na GUI. Para mais informações sobre como o instalar e utilizar, consulte o [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Se preferir fazê-lo manualmente, siga estes passos :


- Localize a pasta apropriada no repositório local (por exemplo, `tutorials/wallet`).
- Crie um diretório dedicado ao tutorial com um nome claro (por exemplo, `green-wallet`). Este nome de pasta também determinará o caminho URL do tutorial. Deve estar em minúsculas, sem caracteres especiais (exceto hífenes) e sem espaços.
- Adicione os seguintes itens a este diretório:
    - Uma subpasta chamada `assets` contendo :
        - Duas imagens `.webp`:
            - `logo.webp`: O logótipo do tutorial (formato quadrado com fundo). Este logótipo deve representar o software ou a ferramenta apresentada. Se o tutorial não for específico de uma ferramenta (por exemplo: um guia geral para gerar uma frase mnemónica), pode escolher um visual adequado (por exemplo: um ícone genérico).
            - `cover.webp`: Uma imagem de capa exibida no início do tutorial.
        - Uma subpasta com o código do idioma original do tutorial. Por exemplo, se o tutorial for escrito em inglês, esta subpasta deve ser nomeada `en'. Coloque todos os elementos visuais do tutorial (diagramas, imagens, screenshots, etc.) nesta pasta.
    - Um ficheiro `tutorial.yml` contendo metadados (autor, etiquetas, categoria, nível de dificuldade, etc.).
    - Um ficheiro Markdown contendo o tutorial, nomeado de acordo com o código da língua (por exemplo, `fr.md`, `en.md`, etc.).

```
# Positionnez-vous dans le dossier approprié
cd tutorials/wallet
# Créez le répertoire dédié au tutoriel
mkdir green-wallet
cd green-wallet
# Créez le sous-dossier 'assets'
mkdir -p assets
# Créez le sous-dossier pour le code de la langue d’origine (exemple : 'en' pour l’anglais)
mkdir -p assets/en
# Créez les fichiers de métadonnées et le tutoriel Markdown (exemple : 'en.md' pour l’anglais)
touch tutorial.yml en.md
```

### 4 - Preencher o ficheiro YAML


- Complete o ficheiro `tutorial.yml` da seguinte forma:

```
id:
project_id:
tags:
-
-
-
category:
level:
credits:
professor:
# Proofreading metadata
original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributors_id:
-
reward:
```

Eis os campos obrigatórios:


- id**: Um UUID (_Universally Unique Identifier_) para identificar exclusivamente o tutorial. Pode gerá-lo com [uma ferramenta em linha] (https://www.uuidgenerator.net/version4). A única restrição é que este UUID deve ser aleatório, de modo a não entrar em conflito com outro UUID na plataforma;
- project_id** : O UUID da empresa ou organização por detrás da ferramenta apresentada no tutorial [a partir da lista de projectos] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Por exemplo, se estiver a fazer um tutorial sobre o software Green Wallet, pode encontrar este `project_id` no seguinte ficheiro: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Esta informação é adicionada no arquivo YAML do seu tutorial porque o Plan ₿ Network mantém um banco de dados de todas as empresas e organizações que operam em Bitcoin ou projetos relacionados. Ao adicionar o `project_id` da entidade vinculada ao seu tutorial, você cria um link entre os dois elementos;
- tags**: 2 ou 3 palavras-chave relevantes relacionadas com o conteúdo do tutorial, escolhidas exclusivamente [da lista de etiquetas do Plano ₿ Rede] (https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- categoria** : A subcategoria correspondente ao conteúdo do tutorial, de acordo com o Plano ₿ Estrutura da rede (por exemplo, para carteiras: `desktop`, `hardware`, `mobile`, `backup`) ;
- nível** : Nível de dificuldade do tutorial, de :
    - principiante`
    - `intermédio`
    - `avançado`
    - "especialista
- professor**: O seu `contributor_id` (palavras BIP39) tal como aparece no [seu perfil de professor] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- original_language** : A língua original do tutorial (por exemplo, `fr`, `en`, etc.) ;
- revisão**: Informações sobre o processo de revisão. Preencha a primeira parte, porque a revisão do seu próprio tutorial conta como uma primeira validação:
    - língua**: Código da língua de revisão (por exemplo, `fr`, `en`, etc.).
    - last_contribution_date**: A data de hoje.
    - urgência** : Deixar em branco.
    - contributors_id** : O seu ID do GitHub.
    - prémio** : Deixar em branco.

Para mais informações sobre o ID do professor, consulte o tutorial correspondente :

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
credits:
professor: pretty-private
# Proofreading metadata
original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency:
contributors_id:
- LoicPandul
reward:
```

### 5 - Escrever o conteúdo


- Completar as propriedades do ficheiro Markdown com :
    - O título (`nome`).
    - Uma breve descrição (`description`).
- Adicione a imagem de capa na parte superior do tutorial utilizando a sintaxe Markdown (substitua "green" pelo nome da ferramenta apresentada):

```
![cover-green](assets/cover.webp)
```


- Escreva o conteúdo do tutorial em Markdown :
    - Utilize títulos (`###`), listas e parágrafos bem estruturados.
    - Inserir imagens utilizando a sintaxe Markdown :

```
![nom-image](assets/en/001.webp)
```


- Colocar os diagramas e imagens na subpasta da língua correspondente, em `/assets`.

### 6 - Guardar e submeter o tutorial


- Guarde as suas alterações localmente, criando um commit com uma mensagem descritiva.
- Envie as alterações para a sua bifurcação do GitHub.

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- Uma vez terminado, crie um Pull Request (PR) no GitHub para propor a integração das suas modificações.
- Adicionar um título e uma breve descrição ao PR. Mencionar o número da edição correspondente no comentário.

### 7 - Revisão e fusão


- Aguardar a validação ou o feedback de um administrador.
- Se necessário, faça correcções e envie novos commits.

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- Depois de o PR ter sido fundido, pode eliminar o seu ramo de trabalho.

## Normas de criação de conteúdos


- Formatação suportada na plataforma** :
    - Markdown clássico: listas, ligações, imagens, citações, negrito, itálico, etc.
    - LaTeX (apenas em bloco, não em linha): delimitado por `$$`.
    - Código em linha: Sintaxe com um único backtick.
    - Blocos de código: Sintaxe com três pontos atrás, por exemplo :

```
print("Hello, Bitcoin!")
```


- Ilustrações e esquemas** :
    - Todas as imagens devem estar no formato WebP. Utilize esta ferramenta gratuita para as converter, se necessário: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Nomear os elementos visuais com 2 ou 3 dígitos (por exemplo, `001.webp`, `002.webp`).
    - Para tutoriais de carteiras móveis ou de hardware, utilize maquetas.
    - Utilize apenas imagens criadas por si ou isentas de direitos de autor.
    - Certifique-se de que são relevantes e de elevada qualidade.
- Carta gráfica** :
    - Fonte: [Rubik](https://fonts.google.com/specimen/Rubik).
    - Plano de Cores ₿ Rede :
        - Laranja: `#FF5C00`
        - Preto: `#000000`
        - Branco: `#FFFFFF`

Se tiveres dificuldades técnicas para enviar o teu tutorial, não hesites em pedir ajuda no [nosso grupo de Telegrama dedicado às contribuições] (https://t.me/PlanBNetwork_ContentBuilder). Muito obrigado!