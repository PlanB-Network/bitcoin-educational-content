---
name: Contribuição - Tutoriais
description: Como propor um novo tutorial na Rede PlanB?
---
![cover](assets/cover.webp)

A missão da PlanB é fornecer recursos educacionais de primeira linha sobre Bitcoin, em tantos idiomas quanto possível. Todo o conteúdo publicado no site é de código aberto e hospedado no GitHub, o que oferece a oportunidade para qualquer pessoa participar do enriquecimento da plataforma. As contribuições podem assumir várias formas: corrigir e revisar textos existentes, traduzir para outros idiomas, atualizar informações ou criar novos tutoriais ainda não disponíveis em nosso site.

Neste tutorial, vou explicar como modificar a seção "Tutoriais" da Rede PlanB. Se você deseja adicionar um novo tutorial ou melhorar um existente, este artigo é para você! Vamos detalhar como contribuir para a Rede PlanB via GitHub, enquanto usamos o Obsidian, uma ferramenta de escrita.

## Pré-requisitos

Para contribuir para a Rede PlanB, você tem 3 opções dependendo do seu nível de experiência com o GitHub:
1. **Usuários experientes**: Continue com seus métodos usuais e consulte este tutorial para se familiarizar com a estrutura do repositório PlanB, requisitos específicos e o fluxo de trabalho.
2. **Iniciantes prontos para aprender**: Recomendo configurar seu próprio ambiente de trabalho. Siga este tutorial, bem como nossos outros artigos listados abaixo para orientá-lo passo a passo.
3. **Iniciantes para contribuições menores**: Para tarefas que exigem menos modificação, como revisão ou correções, use diretamente a interface web do GitHub sem configurar um ambiente local completo.

**Software necessário para seguir meu tutorial:**
- [GitHub Desktop](https://desktop.github.com/)
- [Obsidian](https://obsidian.md/)
- Um editor de código ([VSC](https://code.visualstudio.com/) ou [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/1.webp)
**Pré-requisitos antes de iniciar o tutorial:**
- Ter uma [conta no GitHub](https://github.com/signup).
- Ter um fork do [repositório fonte da Rede PlanB](https://github.com/PlanB-Network/bitcoin-educational-content).
- Ter [um perfil de professor na Rede PlanB](https://planb.network/professors) (apenas se você estiver propondo um tutorial completo).

**Se você precisar de ajuda para obter esses pré-requisitos, meus outros tutoriais irão guiá-lo:**
**[Entendendo Git e GitHub](https://planb.network/tutorials/others/basics-of-github)**
**[Criando uma conta no GitHub](https://planb.network/tutorials/others/create-github-account)**
**[Configurando seu ambiente de trabalho](https://planb.network/tutorials/others/github-desktop-work-environment)**
**[Criando um perfil de professor](https://planb.network/tutorials/others/create-teacher-profile)**
## Que tipo de conteúdo escrever na Rede PlanB?
Estamos principalmente à procura de tutoriais sobre ferramentas relacionadas ao Bitcoin ou seu ecossistema. Esses conteúdos podem ser organizados em torno de seis categorias principais:
- Carteira;
- Nó;
- Mineração;
- Comerciante;
- Câmbio;
- Privacidade.
![tutorial](assets/2.webp)
Além desses tópicos especificamente relacionados ao Bitcoin, a PlanB também está procurando contribuições em temas que destacam a soberania individual, como:
- Ferramentas de código aberto;
- Computação;
- Criptografia;
- Energia;
- Matemática;
- Economia;
- Faça você mesmo (DIYs);
- LifeHacking...
Por exemplo, atualmente temos tutoriais sobre Tails, Nostr ou GrapheneOS. Essas ferramentas não estão diretamente relacionadas ao Bitcoin, mas são sistemas que podem nos interessar em um processo de soberania no mundo digital. Esses conteúdos podem ser integrados em uma subcategoria da seção "Outros".
Você tem a escolha entre projetar um tutorial do zero ou pegar um tutorial previamente publicado em seu site (desde que você detenha os direitos autorais) para também compartilhá-lo na Rede PlanB, adicionando um link para o artigo original.

Independentemente da sua escolha, tenha em mente que todo o conteúdo publicado na Rede PlanB está sob a licença livre [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/). Esta licença permite que qualquer pessoa copie e, potencialmente, modifique seu conteúdo, desde que a fonte original seja devidamente creditada.

## Como propor um tutorial na Rede PlanB?

Uma vez que tudo esteja no lugar, e seu ambiente local esteja bem configurado com seu próprio fork da Rede PlanB, você pode começar a adicionar o tutorial.

### Criar um novo branch

- Abra seu navegador e vá para a página do seu fork do repositório PlanB. Este é o fork que você estabeleceu no GitHub. A URL do seu fork deve parecer com: `https://github.com/[seu-nome-de-usuario]/bitcoin-educational-content`:
![tutorial](assets/3.webp)
- Certifique-se de que você está na branch principal `dev` e então clique no botão `Sync fork`. Se o seu fork não estiver atualizado, o GitHub oferecerá para atualizar sua branch. Prossiga com esta atualização. Se, pelo contrário, sua branch já estiver atualizada, o GitHub informará:
![tutorial](assets/4.webp)
- Abra o software GitHub Desktop e certifique-se de que seu fork está corretamente selecionado no canto superior esquerdo da janela:
![tutorial](assets/5.webp)
- Clique no botão `Fetch origin`. Se o seu repositório local já estiver atualizado, o GitHub Desktop não sugerirá nenhuma ação adicional. Caso contrário, a opção `Pull origin` aparecerá. Clique neste botão para atualizar seu repositório local: ![tutorial](assets/6.webp)
- Certifique-se de que você está na branch principal `dev`:
![tutorial](assets/7.webp)
- Clique nesta branch, depois clique no botão `New Branch`:
![tutorial](assets/8.webp)
- Certifique-se de que o novo branch é baseado no repositório fonte, ou seja, `PlanB-Network/bitcoin-educational-content`.
- Nomeie seu branch de uma maneira que o título seja claro sobre seu propósito, usando hífens para separar cada palavra. Por exemplo, digamos que nosso objetivo é escrever um tutorial sobre o uso do software Sparrow Wallet. Neste caso, o branch de trabalho dedicado à escrita deste tutorial poderia ser nomeado: `tuto-sparrow-wallet-loic`. Uma vez que o nome apropriado seja inserido, clique em `Create branch` para confirmar a criação do branch:
![tutorial](assets/9.webp)
- Agora clique no botão `Publish branch` para salvar seu novo branch de trabalho no seu fork online no GitHub:
![tutorial](assets/10.webp)
Agora, no GitHub Desktop, você deve estar no seu novo branch. Isso significa que todas as mudanças feitas localmente no seu computador serão registradas exclusivamente neste branch específico. Além disso, enquanto este branch permanecer selecionado no GitHub Desktop, os arquivos localmente visíveis em sua máquina correspondem àqueles deste branch (`tuto-sparrow-wallet-loic`), e não aos da branch principal (`dev`).
![tutorial](assets/11.webp)
Para cada novo artigo que deseja publicar, você precisará criar um novo ramo a partir do `dev`. Um ramo no Git é uma versão paralela do projeto, que permite fazer alterações sem afetar o ramo principal, até que o trabalho esteja pronto para ser mesclado.
### Adicionando o tutorial

Agora que o ramo de trabalho foi criado, é hora de integrar o seu novo tutorial.
- Abra o seu gerenciador de arquivos e navegue até a pasta `bitcoin-educational-content`, que representa o clone local do seu repositório. Normalmente, você deve encontrá-la em `Documents\GitHub\bitcoin-educational-content`. Dentro deste diretório, será necessário localizar a subpasta apropriada para colocar o seu tutorial. A organização das pastas reflete as diferentes seções do site da PlanB Network. No nosso exemplo, já que desejamos adicionar um tutorial sobre Sparrow Wallet, é apropriado ir até o seguinte caminho: `bitcoin-educational-content\tutorials\wallet` que corresponde à seção `WALLET` no site: ![tutorial](assets/12.webp)
- Dentro da pasta `wallet`, você precisa criar um novo diretório especificamente dedicado ao seu tutorial. O nome desta pasta deve evocar o software abordado no tutorial, garantindo conectar as palavras com hífens. Para o meu exemplo, a pasta será intitulada `sparrow-wallet`:
![tutorial](assets/13.webp)
- Nesta nova subpasta dedicada ao seu tutorial, vários elementos precisam ser adicionados:
	- Crie uma pasta `assets`, destinada a receber todas as ilustrações necessárias para o seu tutorial;
    - Dentro desta pasta `assets`, você precisa criar 8 subpastas nomeadas `fr`, `de`, `en`, `it`, `es`, `ja`, `vi` e `pt`, para classificar os visuais de acordo com os idiomas correspondentes. Você também deve adicionar uma subpasta `notext` para visuais que não precisam de tradução, como capturas de tela, por exemplo;
	- Um arquivo `tutorial.yml` deve ser criado para registrar os detalhes relacionados ao seu tutorial;
	- Um arquivo no formato markdown deve ser criado para escrever o conteúdo real do seu tutorial. Este arquivo deve ser intitulado de acordo com o código de idioma da escrita. Por exemplo, para um tutorial escrito em francês, o arquivo deve ser chamado `fr.md`.
![tutorial](assets/14.webp)
- Para resumir, aqui está a hierarquia de arquivos a ser criada:
```plaintext
bitcoin-educational-content/
└── tutorials/
    └── wallet/ (a ser modificado com a categoria correta)
        └── sparrow-wallet/ (a ser modificado com o nome do tutorial)
            ├── assets/
            │   ├── fr/
            │   ├── de/
            │   ├── en/
            │   ├── it/
            │   ├── es/
            │   ├── pt/
            |   ├── ja/
            |   ├── vi/
            │   └── notext/
            ├── tutorial.yml
            └── fr.md (a ser modificado de acordo com o código de idioma apropriado)
```

- Para começar, abra o seu arquivo `tutorial.yml` usando o seu editor de código.
- Preencha cada campo com as informações especificadas abaixo:
- **builder**: Insira o nome da empresa que produz o software para o qual você está criando um tutorial;
- **tags**: Determine uma série de palavras-chave intimamente relacionadas ao tópico do seu artigo, para facilitar sua busca e indexação;
- **categoria**: Selecione uma subcategoria apropriada entre as disponíveis no site PlanB, com base no conteúdo do seu tutorial. Por exemplo, para um tutorial na seção `WALLET`, as opções disponíveis são `Desktop`, `Hardware` e `Mobile`;
- **nível**: Indique o nível de dificuldade do seu tutorial escolhendo uma das seguintes quatro categorias:
    - Iniciante (`beginner`),
    - Intermediário (`intermediary`),
    - Avançado (`advanced`),
    - Especialista (`expert`).
- **professor**: Forneça seu ID de contribuidor conforme aparece no seu perfil de professor. Para mais detalhes, consulte [o tutorial correspondente](https://planb.network/fr/tutorials/others/create-teacher-profile);
- **link** (opcional): Caso deseje creditar um site fonte para o tutorial que está desenvolvendo, como seu próprio site pessoal, aqui é onde você pode adicionar o link em questão.
![tutorial](assets/15.webp)
- Uma vez que você tenha terminado de modificar seu arquivo `tutorial.yml`, salve seu documento clicando em `Arquivo > Salvar`:
![tutorial](assets/16.webp)
- Agora, você pode fechar seu editor de código.
- Na pasta `assets`, você deve adicionar um arquivo chamado `logo.webp`, que servirá como uma miniatura para o seu artigo. Esta imagem deve estar no formato `.webp` e deve respeitar uma dimensão quadrada para harmonizar com a interface do usuário. Você tem a liberdade de escolher o logo do software abordado no tutorial ou qualquer outra imagem relevante, desde que seja livre de direitos. Além disso, adicione também uma imagem intitulada `cover.webp` no mesmo local. Esta imagem será exibida no topo do seu tutorial. Certifique-se de que esta imagem, assim como o logo, respeite os direitos de uso e seja adequada para o contexto do seu tutorial:
![tutorial](assets/17.webp)
- Agora, você pode abrir seu arquivo que hospedará seu tutorial, nomeado com o código do seu idioma, como `pt.md`. Vá até o Obsidian, no lado esquerdo da janela, percorra a árvore de pastas até a pasta do seu tutorial e até o arquivo procurado:
![tutorial](assets/18.webp)
- Clique no arquivo para abri-lo:
![tutorial](assets/19.webp)
- Vamos começar preenchendo a seção `Propriedades` no topo do documento. Se esta seção estiver faltando no seu arquivo (se o documento estiver completamente em branco), você pode reproduzi-la copiando-a de outro tutorial existente: ![tutorial](assets/20.webp)
- Você também pode adicioná-la manualmente desta forma usando seu editor de código:
```markdown
---
name: [Título]
description: [Descrição]
---
```
![tutorial](assets/21.webp)
- Preencha o nome do seu tutorial e uma breve descrição dele:
![tutorial](assets/22.webp)
- Em seguida, adicione sua imagem de capa no início do seu tutorial. Para fazer isso, digite:
```markdown
![capa-sparrow](assets/cover.webp)
```
- Esta sintaxe será útil sempre que for necessário adicionar uma imagem ao seu tutorial. O ponto de exclamação indica que é uma imagem, com o texto alternativo (alt) especificado entre os colchetes. O caminho para a imagem é indicado entre os parênteses:
![tutorial](assets/23.webp)
- Continue escrevendo seu tutorial, redigindo seu conteúdo. Quando quiser integrar um subtítulo, aplique a formatação markdown apropriada prefixando o texto com `##`:
![tutorial](assets/24.webp)

### Como adicionar diagramas ao tutorial?

Para adicionar diagramas ao seu tutorial, você pode utilizar ferramentas de criação de diagramas online, como o Draw.io, Lucidchart, ou qualquer outra ferramenta de sua preferência que permita salvar ou exportar imagens em formatos compatíveis (como `.png`, `.jpg`, `.webp`). Após criar seu diagrama:

1. Exporte ou salve a imagem do diagrama no formato desejado.
2. Adicione a imagem ao seu tutorial utilizando a sintaxe markdown para imagens, conforme mostrado anteriormente.
3. Certifique-se de que a imagem esteja na pasta `assets` junto com as outras imagens do tutorial.
4. Referencie a imagem no local apropriado do seu conteúdo, garantindo que ela complemente e ilustre adequadamente os pontos que você está explicando.

Lembre-se de verificar se as imagens dos diagramas estão claras e legíveis, e se elas realmente contribuem para a compreensão do conteúdo do tutorial.
As subpastas de idiomas na pasta `assets` são destinadas a organizar os diagramas e visuais que acompanharão seu tutorial. Se suas imagens incluírem texto, certifique-se de traduzi-las para cada idioma relevante para tornar seu conteúdo acessível a um público internacional. Para diagramas sem texto para traduzir ou capturas de tela, coloque-os diretamente na subpasta `notext`. ![tutorial](assets/25.webp)
Para nomear suas imagens, simplesmente coloque números na ordem de aparição no tutorial. Por exemplo, nomeie sua primeira imagem `1.webp`, sua segunda `2.webp`, e assim por diante.

Se o mesmo diagrama for traduzido para múltiplos idiomas, mantenha o mesmo nome de arquivo para as diferentes traduções nas subpastas de idiomas, como `en/1.webp`, `fr/1.webp`, `pt/1.webp`, etc.

Você tem a opção de usar diferentes formatos de imagem, como `jpeg`, `png` ou `webp`. É recomendado optar pelo formato `webp` para que as imagens sejam menos pesadas.
![tutorial](assets/26.webp)
Para inserir um diagrama em seu documento, use o seguinte comando em Markdown, certificando-se de especificar o texto alternativo apropriado e o caminho correto da imagem:
```markdown
![pardal](assets/notext/1.webp)
```
O ponto de exclamação no início indica que é uma imagem. O texto alternativo, que auxilia na acessibilidade e SEO, é colocado entre colchetes. Finalmente, o caminho para a imagem é indicado entre parênteses: ![tutorial](assets/27.webp)
Se desejar criar seus próprios diagramas, certifique-se de aderir à carta gráfica da PlanB Network para garantir consistência visual:
- **Fonte**: Use [Rubik](https://fonts.google.com/specimen/Rubik);
- **Cores**:
	- Laranja: #FF5C00
	- Preto: #000000
	- Branco: #FFFFFF

**É imperativo que todos os visuais integrados aos seus tutoriais sejam livres de direitos autorais ou estejam em conformidade com a licença do arquivo fonte**. Além disso, todos os diagramas publicados na PlanB Network estão disponíveis sob a licença CC-BY-SA, da mesma forma que o texto.

**-> Dica:** Ao compartilhar arquivos publicamente, como imagens, é importante remover qualquer metadado supérfluo. Isso pode conter informações sensíveis, como dados de localização, datas de criação ou detalhes sobre o autor. Para proteger sua privacidade, é aconselhável remover esse metadado. Para simplificar essa operação, você pode usar ferramentas especializadas como [Exif Cleaner](https://exifcleaner.com/), que oferece a capacidade de limpar os metadados de um documento com um simples arrastar e soltar.

### Como salvar e enviar o tutorial?

Uma vez que você tenha terminado de escrever seu tutorial no idioma de sua escolha, o próximo passo é submeter um **Pull Request**. O administrador então adicionará as traduções que faltam do seu tutorial, graças ao nosso método de tradução automatizado.

- Para prosseguir com o Pull Request, abra o software GitHub Desktop.
- O software deve detectar automaticamente as alterações que você fez localmente em comparação ao repositório original. Antes de continuar, verifique cuidadosamente no lado esquerdo da interface que essas alterações correspondem exatamente ao que você esperava: ![tutorial](assets/28.webp)
- Adicione um título para o seu commit e clique no botão azul `Commit to [your branch]` para validar essas alterações: ![tutorial](assets/29.webp)
Um commit é uma gravação das alterações feitas na branch, acompanhada por uma mensagem descritiva, permitindo acompanhar a evolução de um projeto ao longo do tempo. É, portanto, uma espécie de ponto de controle intermediário.
- Em seguida, clique no botão `Push origin`. Isso enviará seu commit para o seu fork: ![tutorial](assets/30.webp) - Se você não terminou seu tutorial, pode voltar a ele mais tarde e fazer novos commits.
- Se você terminou suas edições para este branch, agora clique no botão `Preview Pull Request`: ![tutorial](assets/31.webp)
- Você pode verificar uma última vez se suas modificações estão corretas, então clique no botão `Create pull request`:
![tutorial](assets/32.webp)
Um Pull Request é uma solicitação feita para integrar as alterações do seu branch ao branch principal do repositório da PlanB Network, o que permite a revisão e discussão das alterações antes da sua fusão.

- Você será automaticamente redirecionado no seu navegador para a página de preparação do seu Pull Request no GitHub:
![tutorial](assets/33.webp)
- Forneça um título que resuma brevemente as modificações que você deseja mesclar com o repositório fonte.
- Adicione um breve comentário descrevendo essas alterações.
- Clique no botão verde `Create pull request` para confirmar a solicitação de fusão:
![tutorial](assets/34.webp)
Seu PR então será visível na aba `Pull Request` do repositório principal da PlanB Network. Agora, tudo o que você precisa fazer é esperar até que um administrador entre em contato com você para confirmar a fusão da sua contribuição ou para solicitar quaisquer modificações adicionais.
![tutorial](assets/35.webp)
Após a fusão do seu PR com o branch principal, é recomendado deletar o seu branch de trabalho (`tuto-sparrow-wallet`) para manter um histórico limpo no seu fork. O GitHub oferecerá automaticamente esta opção na página do seu PR:
![tutorial](assets/36.webp)
No software GitHub Desktop, você pode voltar para o branch principal do seu fork (`dev`).
![tutorial](assets/7.webp)
Se você desejar fazer modificações na sua contribuição após já ter enviado seu PR, o procedimento a seguir depende do estado atual do seu PR:
- Se o seu PR ainda está aberto e ainda não foi mesclado, faça as modificações localmente enquanto permanece no mesmo branch. Uma vez que as modificações estejam finalizadas, use o botão `Push origin` para adicionar um novo commit ao seu PR ainda aberto;
- No caso de seu PR já ter sido mesclado ao branch principal, você precisará refazer o processo desde o início, criando um novo branch e, em seguida, submetendo um novo PR. Certifique-se de que seu repositório local esteja sincronizado com o repositório fonte da PlanB Network antes de prosseguir.
