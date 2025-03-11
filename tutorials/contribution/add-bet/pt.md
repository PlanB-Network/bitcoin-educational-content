---
name: Adicionando Ferramentas Educacionais
description: Como adicionar novos materiais educacionais na Rede PlanB?
---
![event](assets/cover.webp)

A missão da PlanB é fornecer recursos educacionais líderes sobre Bitcoin, em tantos idiomas quanto possível. Todo o conteúdo publicado no site é de código aberto e hospedado no GitHub, o que permite a qualquer pessoa participar do enriquecimento da plataforma.

Além de tutoriais e treinamentos, a Rede PlanB também oferece uma vasta biblioteca de conteúdo educacional variado sobre Bitcoin, acessível a todos, [na seção "BET" (_Bitcoin Educational Toolkit_)](https://planb.network/resources/bet). Esta base de dados inclui pôsteres educacionais, memes, pôsteres de propaganda humorística, diagramas técnicos, logotipos e outras ferramentas para os usuários. O objetivo desta iniciativa é apoiar indivíduos e comunidades que ensinam Bitcoin ao redor do mundo, fornecendo-lhes os recursos visuais necessários.

Você quer participar do enriquecimento desta base de dados, mas não sabe como? Este tutorial é para você!

*É imperativo que todo o conteúdo integrado ao site seja livre de direitos ou respeite a licença do arquivo fonte. Além disso, todos os visuais publicados na Rede PlanB estão disponíveis sob a licença [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).*
![event](assets/01.webp)
- Primeiro, você precisa ter uma conta no GitHub. Se você não sabe como criar uma conta, fizemos um tutorial detalhado para guiá-lo.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Vá para [o repositório GitHub da PlanB dedicado a dados](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/bet) na seção `resources/bet/`:
![event](assets/02.webp)
- Clique no topo direito no botão `Add file`, depois em `Create new file`:
![event](assets/03.webp)
- Se você nunca contribuiu para os conteúdos da Rede PlanB antes, precisará criar seu fork do repositório original. Fazer um fork de um repositório significa criar uma cópia desse repositório em sua própria conta do GitHub, o que permite trabalhar no projeto sem afetar o repositório original. Clique no botão `Fork this repository`:
![event](assets/04.webp)
- Você então chegará à página de edição do GitHub:
![event](assets/05.webp)
- Crie uma pasta para o seu conteúdo. Para fazer isso, na caixa `Name your file...`, escreva o nome do seu conteúdo em letras minúsculas com hífens no lugar de espaços. No meu exemplo, digamos que eu queira adicionar um visual em PDF da lista de 2048 palavras BIP39. Então, vou chamar minha pasta de `bip39-wordlist`: ![event](assets/06.webp)
- Para confirmar a criação da pasta, simplesmente adicione uma barra após o nome na mesma caixa, por exemplo: `bip39-wordlist/`. Adicionar uma barra cria automaticamente uma pasta em vez de um arquivo:
![event](assets/07.webp)
- Nesta pasta, você criará um primeiro arquivo YAML chamado `bet.yml`:
![event](assets/08.webp)
- Preencha este arquivo com informações relacionadas ao seu conteúdo usando este modelo:

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
```yaml
builder: Indique o identificador da sua organização na Rede PlanB. Se você ainda não possui um identificador "builder" para sua empresa, você pode criar um seguindo este tutorial.

https://planb.network/tutorials/others/contribution/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

 Se você não possui um, pode simplesmente usar seu nome, seu pseudônimo ou o nome da sua empresa sem ter criado um perfil de construtor.
type: Selecione a natureza do seu conteúdo entre as seguintes duas opções:
  - `Educational Content` para conteúdos educacionais.
  - `Visual Content` para outros tipos de conteúdos diversos.

links: Forneça links para seus conteúdos. Você tem duas opções:
  - Se você escolher hospedar seu conteúdo diretamente no GitHub da PlanB, precisará adicionar os links para este arquivo durante as etapas seguintes.
  - Se seus conteúdos estão hospedados em outro lugar, como no seu site pessoal, indique os links correspondentes aqui:
      - `download`: Um link para baixar seu conteúdo.
      - `view`: Um link para visualizar seu conteúdo (pode ser o mesmo que o link de download). Se seu conteúdo está disponível em múltiplos idiomas, adicione um link para cada idioma.

tags: Adicione duas tags associadas ao seu conteúdo. Exemplos:
  - bitcoin
  - tecnologia
  - economia
  - educação
  - meme...

contributors: Mencione seu identificador de contribuidor se você tiver um.

Por exemplo, seu arquivo YAML poderia parecer assim:

```yaml
builder: PlanB-Network
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view:
- No meu exemplo, deixarei os links vazios por enquanto, pois adicionarei meu PDF diretamente no GitHub:
![event](assets/09.webp)
- Uma vez que suas modificações neste arquivo estejam completas, salve-as clicando no botão `Commit changes...`:
![event](assets/10.webp)
- Adicione um título para suas modificações, bem como uma breve description:
![event](assets/11.webp)
- Clique no botão verde `Propose changes`:
![event](assets/12.webp)
- Você então chegará em uma página que resume todas as suas mudanças:
![event](assets/13.webp)
- Clique na foto do seu perfil do GitHub no canto superior direito, depois em `Your Repositories`:
![event](assets/14.webp)
- Selecione seu fork do repositório da Rede PlanB:
![event](assets/15.webp)
- Você deverá ver uma notificação no topo da janela com seu novo branch. Provavelmente se chama `patch-1`. Clique nele:
![event](assets/16.webp)
- Você está agora no seu branch de trabalho (**certifique-se de que está no mesmo branch que suas modificações anteriores, isso é importante!**):
![event](assets/17.webp)
- Volte para a pasta `resources/bet/` e selecione a pasta do seu conteúdo que você acabou de criar no commit anterior:
![event](assets/18.webp)
- Na pasta do seu conteúdo, clique no botão `Add file`, depois em `Create new file`:
![event](assets/19.webp)
- Nomeie esta nova pasta `assets` e confirme sua criação colocando uma barra `/` no final:
![event](assets/20.webp)
- Nesta pasta `assets`, crie um arquivo chamado `.gitkeep`: ![event](assets/21.webp)
```
- Clique no botão `Commit changes...`: ![event](assets/22.webp)- Deixe o título do commit como padrão e certifique-se de que a caixa `Commit directly to the patch-1 branch` esteja marcada, então clique em `Commit changes`: ![event](assets/23.webp)
- Retorne à pasta `assets`: ![event](assets/24.webp)
- Clique no botão `Add file`, depois em `Upload files`: ![event](assets/25.webp)
- Uma nova página será aberta. Arraste e solte uma miniatura que represente seu conteúdo na área. Esta imagem será exibida no site da Rede PlanB: ![event](assets/26.webp)
- Pode ser uma pré-visualização, um logo ou um ícone: ![event](assets/27.webp)
- Uma vez que a imagem esteja carregada, certifique-se de que a caixa `Commit directly to the patch-1 branch` esteja marcada, então clique em `Commit changes`: ![event](assets/28.webp)
- Tenha cuidado, sua imagem deve ser nomeada `logo` e deve estar no formato `.webp`. O nome completo do arquivo deve ser, portanto: `logo.webp`: ![event](assets/29.webp)
- Retorne à sua pasta `assets` e clique no arquivo intermediário `.gitkeep`: ![event](assets/30.webp)
- Uma vez no arquivo, clique nos três pequenos pontos no canto superior direito e depois em `Delete file`: ![event](assets/31.webp)
- Certifique-se de que você ainda está na mesma branch de trabalho, então clique no botão `Commit changes`: ![event](assets/32.webp)
- Adicione um título e uma descrição ao seu commit, então clique em `Commit changes`: ![event](assets/33.webp)
- Retorne à pasta do seu conteúdo: ![event](assets/34.webp)
- Clique no botão `Add file`, depois em `Create new file`: ![event](assets/35.webp)
- Crie um novo arquivo YAML nomeando-o com o indicador do seu idioma nativo. Este arquivo será usado para a descrição do conteúdo. Por exemplo, se eu quiser escrever minha descrição em inglês, nomearei este arquivo como `en.yml`: ![event](assets/36.webp)
- Preencha este arquivo YAML usando este modelo:

```yaml
name: 
description: |
  
```

- Para a chave `name`, você pode adicionar o nome do seu conteúdo;
- Para a chave `description`, você simplesmente precisa adicionar um curto parágrafo que descreva seu conteúdo. A descrição deve estar no mesmo idioma que o nome do arquivo. Você não precisa traduzir esta descrição para todos os idiomas suportados no site, pois as equipes da PlanB farão isso com seu modelo.
Por exemplo, aqui está como seu arquivo pode parecer:

```yaml
name: BIP39 WORDLIST
description: |
  Lista completa e numerada das 2048 palavras em inglês do dicionário BIP39 usadas para codificar frases mnemônicas. O documento pode ser impresso em uma única página.
```

![event](assets/37.webp)
- Clique no botão `Commit changes...`:
![event](assets/38.webp)
- Certifique-se de que a caixa `Commit directly to the patch-1 branch` esteja marcada, adicione um título, então clique em `Commit changes`:
![event](assets/39.webp)
- Sua pasta de conteúdo agora deve ter esta aparência:
![event](assets/40.webp)
*Se você prefere não adicionar o conteúdo no GitHub e já anotou os links no arquivo `bet.yml` durante as etapas anteriores, você pode pular esta seção e ir diretamente para a parte referente à criação do Pull Request.*
- Retorne à pasta `/assets`:
![evento](assets/41.webp)
- Clique no botão `Add file`, depois em `Upload files`:
![evento](assets/42.webp)
- Uma nova página será aberta. Arraste e solte na área o conteúdo que deseja compartilhar:
![evento](assets/43.webp)
- Por exemplo, eu adicionei o arquivo PDF da lista BIP39:
![evento](assets/44.webp)
- Uma vez que o conteúdo esteja carregado, certifique-se de que a caixa `Commit directly to the patch-1 branch` esteja marcada, então clique em `Commit changes`:
![evento](assets/45.webp)
- Retorne à sua pasta `/assets` e clique no arquivo que acabou de carregar:
![evento](assets/46.webp)
- Recupere a URL intermediária do seu arquivo. Por exemplo, no meu caso, a URL é:

```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Mantenha apenas a última parte da URL a partir de `/resources` em diante:

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Adicione à base da URL as seguintes informações para ter o link correto:

```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

O que estamos fazendo aqui é antecipar o futuro link para o seu arquivo, uma vez que sua proposta tenha sido mesclada ao repositório fonte da Rede PlanB.
- Volte ao seu arquivo `bet.yml` e clique no ícone de lápis: ![evento](assets/47.webp)
- Adicione seu link lá:
![evento](assets/48.webp)
- Uma vez que suas alterações estejam completas, clique no botão `Commit changes...`:
![evento](assets/49.webp)
- Adicione um título para suas mudanças, bem como uma breve description:
![evento](assets/50.webp)
- Clique no botão verde `Commit changes`:
![evento](assets/51.webp)

---

- Se tudo parece bom para você, retorne à raiz do seu fork:
![evento](assets/52.webp)
- Você deverá ver uma mensagem indicando que sua branch foi modificada. Clique no botão `Compare & pull request`:
![evento](assets/53.webp)
- Adicione um título claro e uma descrição para o seu PR:
![evento](assets/54.webp)
- Clique no botão `Create pull request`:
![evento](assets/55.webp)
Parabéns! Seu PR foi criado com sucesso. Um administrador agora irá revisá-lo e, se tudo estiver em ordem, mesclá-lo ao repositório principal da Rede PlanB. Você deverá ver seu BET aparecer no site alguns dias depois.

Certifique-se de acompanhar o progresso do seu PR. Um administrador pode deixar um comentário pedindo informações adicionais. Enquanto seu PR não for validado, você pode consultá-lo na aba Pull requests no repositório GitHub da Rede PlanB:
![evento](assets/56.webp)
Muito obrigado pela sua valiosa contribuição! :)
