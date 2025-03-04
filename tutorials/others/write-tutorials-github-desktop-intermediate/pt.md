---
name: Contribuição - Tutorial com GitHub Desktop (Intermediário)
description: Guia completo para propor um tutorial sobre o Plano ₿ Rede usando o GitHub Desktop
---
![cover](assets/cover.webp)

Antes de seguir este tutorial sobre como adicionar um novo tutorial, deve ter completado alguns passos preliminares. Se ainda não o fez, convido-o a consultar primeiro este tutorial introdutório e depois a voltar aqui:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Já o fez:


- Escolha o tema do seu tutorial;
- Contactou a equipa do Plano ₿ Network através do [grupo Telegram] (https://t.me/PlanBNetwork_ContentBuilder) ou paolo@planb.network;
- Escolha as suas ferramentas de contribuição.

Neste tutorial, veremos como adicionar seu tutorial no Plan ₿ Network configurando seu ambiente local com GitHub Desktop. Se você já domina o Git, este tutorial muito detalhado pode não ser necessário para você. Prefiro recomendar a consulta deste outro tutorial onde apenas apresento as principais diretrizes, sem orientações detalhadas passo a passo:


- Utilizadores experientes**:

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410
Se preferir não configurar o seu ambiente local, siga este outro tutorial concebido para principiantes, onde fazemos as alterações diretamente através da interface Web do GitHub:


- Iniciantes (interface web)**:

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Pré-requisitos

Software necessário para seguir este tutorial:


- [GitHub Desktop](https://desktop.github.com/);
- Um editor de ficheiros markdown como o [Obsidian](https://obsidian.md/);
- Um editor de código ([VSC](https://code.visualstudio.com/) ou [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Pré-requisitos antes de iniciar o tutorial:


- Ter uma [conta GitHub](https://github.com/signup);
- Ter uma bifurcação do repositório de fontes do [Plano ₿ Rede] (https://github.com/PlanB-Network/bitcoin-educational-content);
- Ter [um perfil de professor no Plano ₿ Rede](https://planb.network/professors) (apenas se estiver a propor um tutorial completo).

Se precisar de ajuda para obter estes pré-requisitos, os meus outros tutoriais ajudá-lo-ão:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb
Quando tudo estiver no lugar e o seu ambiente local estiver devidamente configurado com o seu próprio fork do Plan ₿ Network, pode começar a adicionar o tutorial.

## 1 - Criar uma nova sucursal

Abra o seu navegador e vá para a página da sua bifurcação do repositório Plan ₿ Network. Esta é a bifurcação que você estabeleceu no GitHub. O URL da sua bifurcação deve ser parecido com: `https://github.com/[your-username]/bitcoin-educational-content`:

![TUTO](assets/fr/03.webp)

Certifique-se de que você está no ramo principal `dev` e clique no botão `Sync fork`. Se a sua bifurcação não estiver actualizada, o GitHub irá oferecer-se para atualizar o seu ramo. Proceda com essa atualização. Se, pelo contrário, o seu ramo já estiver atualizado, o GitHub irá informá-lo:

![TUTO](assets/fr/04.webp)

Abra o software GitHub Desktop e certifique-se de que a sua bifurcação está corretamente selecionada no canto superior esquerdo da janela:

![TUTO](assets/fr/05.webp)

Clique no botão `Fetch origin`. Se o seu repositório local já estiver atualizado, o GitHub Desktop não irá sugerir nenhuma ação adicional. Caso contrário, a opção `Pull origin` aparecerá. Clique neste botão para atualizar seu repositório local:

![TUTO](assets/fr/06.webp)

Verifique se você está realmente no ramo principal `dev`:

![TUTO](assets/fr/07.webp)

Clique neste ramo e, em seguida, clique no botão `Novo ramo`:

![TUTO](assets/fr/08.webp)

Certifique-se de que o novo ramo é baseado no repositório de origem, nomeadamente `PlanB-Network/bitcoin-educational-content`.

Dê um nome ao seu ramo de forma a que o título seja claro quanto ao seu objetivo, utilizando travessões para separar cada palavra. Por exemplo, digamos que o nosso objetivo é escrever um tutorial sobre a utilização do software Sparrow Wallet. Neste caso, o ramo de trabalho dedicado a escrever este tutorial poderia ser nomeado: `tuto-sparrow-wallet-loic`. Uma vez introduzido o nome apropriado, clique em `Criar ramo` para confirmar a criação do ramo:

![TUTO](assets/fr/09.webp)

Agora clique no botão `Publish branch` para salvar seu novo branch de trabalho no seu fork online no GitHub:

![TUTORIAL](assets/fr/10.webp)

Agora, no GitHub Desktop, deverá encontrar-se no seu novo ramo. Isso significa que todas as alterações feitas localmente no seu computador serão salvas exclusivamente nesse branch específico. Além disso, enquanto este ramo permanecer selecionado no GitHub Desktop, os arquivos visíveis localmente na sua máquina correspondem aos deste ramo (`tuto-sparrow-wallet-loic`), e não aos do ramo principal (`dev`).

![TUTORIAL](assets/fr/11.webp)

Para cada novo artigo que pretenda publicar, terá de criar um novo ramo a partir de `dev`. Um ramo no Git é uma versão paralela do projeto, que lhe permite fazer alterações sem afetar o ramo principal, até que o trabalho esteja pronto para ser fundido.

## 2 - Adicionar os ficheiros do tutorial

Agora que o ramo de trabalho está criado, é altura de integrar o seu novo tutorial. Tem duas opções: utilizar o meu script Python, que automatiza a criação dos documentos necessários, ou criar manualmente cada ficheiro. Vamos ver os passos a seguir para cada opção.

### Com o meu script Python

É necessário instalar no seu computador:


- Python 3.8 ou superior;
- As dependências necessárias para o script. Executar:

```bash
pip install customtkinter appdirs
```

Para utilizar o script, aceda à pasta onde está armazenado. O script está localizado no repositório de dados Plan ₿ Network sob o caminho: `bitcoin-educational-content/scripts/tutorial-related/new-tutorial-creation/`.

Uma vez na pasta, execute o comando:

```bash
python new-tutorial-creation.py
```

Será aberta uma interface gráfica do utilizador (GUI). Na primeira vez, terá de introduzir todas as informações necessárias, mas durante as utilizações subsequentes do script, as suas informações pessoais serão recordadas, o que evita que tenha de as introduzir novamente.

![TUTORIAL](assets/fr/37.webp)

Comece por indicar o caminho local que leva à pasta `/tutorials` no seu clone do repositório (`.../bitcoin-educational-content/tutorials/`). Pode anotá-lo manualmente ou clicar no botão "Browse" para navegar no seu explorador de ficheiros.

![TUTORIAL](assets/fr/38.webp)

Selecione a língua em que vai escrever o seu tutorial.

![TUTORIAL](assets/fr/39.webp)

Escolha uma categoria principal para o seu tutorial.

![TUTORIAL](assets/fr/40.webp)

Em seguida, selecione uma subcategoria adequada, dependendo da categoria principal que escolheu.

![TUTORIAL](assets/fr/41.webp)

Determinar um nível de dificuldade para o tutorial.

![TUTORIAL](assets/fr/42.webp)

Escolha o nome do diretório especialmente criado para o seu tutorial. O nome dessa pasta deve refletir o software abordado no tutorial, usando traços para conectar as palavras. Por exemplo, a pasta pode ser chamada de `red-wallet`:

![TUTO](assets/fr/43.webp)

O `project_id` é o UUID da empresa ou organização por detrás da ferramenta apresentada no tutorial, disponível [na lista de projectos] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Por exemplo, para um tutorial sobre o software Sparrow Wallet, você encontraria este `project_id` no arquivo: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Esta informação é adicionada ao arquivo YAML do seu tutorial porque o Plan ₿ Network mantém um banco de dados de empresas e organizações ativas em Bitcoin ou projetos relacionados. Ao adicionar o `project_id` associado ao seu tutorial, você cria um link entre o seu conteúdo e a entidade em questão.

***Atualização:*** Na nova versão do script, já não é necessário introduzir manualmente o `project_id`. Foi adicionada uma função de pesquisa para encontrar o projeto pelo seu nome e obter automaticamente o `project_id` correspondente. Digite o início do nome do projeto na caixa "Nome do projeto" para o procurar e, em seguida, selecione a empresa desejada no menu pendente. O `project_id` será automaticamente preenchido na caixa abaixo. Tem também a opção de o anotar manualmente, se necessário.

![TUTO](assets/fr/44.webp)

Para as etiquetas, selecione 2 ou 3 palavras-chave relevantes relacionadas com o conteúdo do seu tutorial, escolhendo-as exclusivamente [da lista de etiquetas Plano ₿ Rede] (https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md).

![TUTO](assets/fr/45.webp)

Na caixa "ID do GitHub do contribuidor", introduza o seu ID do GitHub.

![TUTO](assets/fr/46.webp)

Para a caixa "ID do professor PBN", introduza o seu ID utilizando as palavras da lista BIP39, tal como aparece no [seu perfil de professor] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).

![TUTO](assets/fr/47.webp)

Para mais informações sobre o ID do professor, consulte o seguinte tutorial:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Quando todas as informações tiverem sido introduzidas e verificadas, clique em "Criar tutorial" para validar a criação dos ficheiros do seu tutorial. Isto irá gerar localmente a pasta do seu tutorial e todos os ficheiros necessários na pasta da categoria selecionada.

![TUTO](assets/fr/48.webp)

Pode agora saltar a subsecção "Sem o meu script Python", bem como o passo 3 "Preencher o ficheiro YAML", porque o script já executou estas acções automaticamente para si. Avance diretamente para o passo 4 e comece a escrever o seu tutorial.

Para mais informações sobre este script Python, pode também [consultar o seu README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Sem o meu script Python

Abra o seu gestor de ficheiros e navegue até à pasta `bitcoin-educational-content`, que representa o clone local do seu repositório. Normalmente, deve encontrá-la em `Documents\GitHub\bitcoin-educational-content`.

Dentro deste diretório, será necessário localizar a subpasta adequada para colocar o seu tutorial. A organização das pastas reflecte as diferentes secções do site da Plan ₿ Network. No nosso exemplo, como queremos adicionar um tutorial sobre a Sparrow Wallet, é apropriado ir para o seguinte caminho: `bitcoin-educational-content\tutorials\wallet` que corresponde à secção `WALLET` do site:

![TUTO](assets/fr/12.webp)

Dentro da pasta `wallet`, é necessário criar um novo diretório especificamente dedicado ao seu tutorial. O nome dessa pasta deve evocar o software abordado no tutorial, certificando-se de conectar as palavras com traços. No meu exemplo, a pasta terá o título `sparrow-wallet`:

![TUTO](assets/fr/13.webp)

Nesta nova subpasta dedicada ao seu tutorial, é necessário adicionar vários elementos:


- Crie uma pasta `assets`, destinada a receber todas as ilustrações necessárias para o seu tutorial;
- Dentro desta pasta `assets`, é necessário criar uma subpasta nomeada de acordo com o código do idioma original do tutorial. Por exemplo, se o tutorial está escrito em inglês, esta subpasta deve ser nomeada `en`. Coloque aí todos os elementos visuais do tutorial (diagramas, imagens, capturas de ecrã, etc.).
- Um arquivo `tutorial.yml` deve ser criado para registrar os detalhes relacionados ao seu tutorial;
- Deve ser criado um ficheiro de formato markdown para escrever o conteúdo real do seu tutorial. Este ficheiro deve ser intitulado de acordo com o código da língua em que foi escrito. Por exemplo, para um tutorial escrito em francês, o ficheiro deve chamar-se `fr.md`.

![TUTO](assets/fr/14.webp)

Para resumir, eis a hierarquia dos ficheiros a criar:

```plaintext
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```

## 3 - Preencher o ficheiro YAML

Preencha o ficheiro `tutorial.yml` copiando o seguinte modelo:

```yaml
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
````

Eis os pormenores dos campos obrigatórios:


- **id**: Um UUID (_Universally Unique Identifier_) para identificar exclusivamente o tutorial. Pode gerá-lo com [uma ferramenta em linha] (https://www.uuidgenerator.net/version4). O único requisito é que este UUID seja aleatório para evitar conflitos com outro UUID na plataforma;
- **project_id**: O UUID da empresa ou organização por detrás da ferramenta apresentada no tutorial [da lista de projectos] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Por exemplo, se estiver a criar um tutorial sobre o software Sparrow Wallet, pode encontrar este `project_id` no seguinte ficheiro: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Esta informação é adicionada ao arquivo YAML do seu tutorial porque o Plan ₿ Network mantém um banco de dados de todas as empresas e organizações que operam em Bitcoin ou projetos relacionados. Ao adicionar o `project_id` da entidade relacionada ao seu tutorial, você cria um link entre os dois elementos;
- **tags**: 2 ou 3 palavras-chave relevantes relacionadas com o conteúdo do tutorial, escolhidas exclusivamente [da lista de etiquetas do Plano ₿ Rede] (https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- **category**: A subcategoria correspondente ao conteúdo do tutorial, de acordo com a estrutura do site da Rede Plan ₿ (por exemplo, para carteiras: `desktop`, `hardware`, `mobile`, `backup`);
- **level**: O nível de dificuldade do tutorial, entre:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`
- **professor**: O seu `contributor_id` (palavras BIP39) tal como aparece no [perfil do professor] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- **original_language**: A língua original do tutorial (por exemplo `fr`, `en`, etc.);
- **proofreading**: Informações sobre o processo de revisão. Preencher a primeira parte, uma vez que a revisão do seu próprio tutorial conta como uma primeira validação:
    - **language**: Código da língua da revisão de provas (por exemplo, `fr`, `en`, etc.).
    - **last_contribution_date**: A data de hoje.
    - **urgency**: Deixar em branco.
    - **contributors_id**: O seu ID do GitHub.
    - **reward**: Deixar em branco.

Para mais informações sobre o identificador do professor, consulte o tutorial correspondente:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Aqui está um exemplo de um arquivo `tutorial.yml` completo para um tutorial sobre a carteira Blockstream Green:

```yaml
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
Once you have finished modifying your `tutorial.yml` file, save your document by clicking on `File > Save`:
![TUTO](assets/fr/16.webp)
You can now close your code editor.
## 4 - Fill in the Markdown File
Now, you can open your file that will host your tutorial, named with the code of your language, such as `fr.md`. Go to Obsidian, on the left side of the window, scroll through the folder tree until you find the folder of your tutorial and the file you are looking for:
![TUTO](assets/fr/18.webp)
Click on the file to open it:
![TUTO](assets/fr/19.webp)
We will start by filling in the `Properties` section at the top of the document.
![TUTO](assets/fr/20.webp)
Manually add and fill in the following code block:
```

---
name: [Título]
description: [Descrição]
---
```
![TUTO](assets/fr/21.webp)
Fill in the name of your tutorial and a short description of it:
![TUTO](assets/fr/22.webp)
Then, add the path of the cover image at the beginning of your tutorial. To do this, note:
```

![cover-sparrow](assets/cover.webp)

```
This syntax will be useful whenever adding an image to your tutorial is necessary. The exclamation point indicates that it is an image, with the alternative text (alt) specified between the brackets. The path to the image is indicated between the parentheses:
![TUTO](assets/fr/23.webp)
## 5 - Add the Logo and Cover
Within the `assets` folder, you must add a file named `logo.webp`, which will serve as a thumbnail for your article. This image must be in `.webp` format and must respect a square dimension to harmonize with the user interface. You are free to choose the logo of the software covered in the tutorial or any other relevant image, provided that it is free of rights. In addition, also add an image titled `cover.webp` in the same place. This image will be displayed at the top of your tutorial. Ensure that this image, like the logo, respects usage rights and is suitable for the context of your tutorial:
## 6 - Writing the Tutorial and Adding Visuals
Continue writing your tutorial by drafting your content. When you want to integrate a subtitle, apply the appropriate markdown formatting by prefixing the text with `##`:
![TUTO](assets/fr/24.webp)
The language subfolder in the `assets` folder is used to store diagrams and visuals that will accompany your tutorial. As much as possible, avoid including text in your images to make your content accessible to an international audience. Of course, the software being presented will contain text, but if you add diagrams or additional indications on software screenshots, do so without text or, if it proves indispensable, use English.
![TUTO](assets/fr/25.webp)
To name your images, simply use numbers corresponding to their order of appearance in the tutorial, formatted with two digits (or three digits if your tutorial contains more than 99 images). For example, name your first image `01.webp`, your second `02.webp`, and so on.
Your images must be in `.webp` format exclusively. If needed, you can use [my image conversion software](https://github.com/LoicPandul/ImagesConverter).
![TUTO](assets/fr/26.webp)
To insert a diagram into your document, use the following Markdown command, making sure to specify the appropriate alternative text as well as the correct path of the image:
```

![sparrow](assets/fr/01.webp)

```