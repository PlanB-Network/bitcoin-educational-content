---
name: Adicionando um Construtor
description: Como propor a adição de um novo construtor na Rede PlanB?
---
![builder](assets/cover.webp)

A missão da PlanB é fornecer recursos educacionais de primeira linha sobre Bitcoin, em tantos idiomas quanto possível. Todo o conteúdo publicado no site é de código aberto e hospedado no GitHub, o que permite que qualquer pessoa participe do enriquecimento da plataforma.

Você quer adicionar um novo "construtor" de Bitcoin ao site da Rede PlanB e dar visibilidade à sua empresa ou software, mas não sabe como? Este tutorial é para você!
![builder](assets/01.webp)
- Primeiro, você precisa ter uma conta no GitHub. Se você não sabe como criar uma conta, fizemos um tutorial detalhado para guiá-lo.

https://planb.network/tutorials/others/create-github-account


- Vá para [o repositório GitHub da PlanB dedicado a dados](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/builders) na seção `resources/builder/`:
![builder](assets/02.webp)
- Clique no canto superior direito no botão `Add file`, depois em `Create new file`:
![builder](assets/03.webp)
- Se você nunca contribuiu para os conteúdos da Rede PlanB antes, precisará criar seu fork do repositório original. Fazer um fork de um repositório significa criar uma cópia desse repositório em sua própria conta do GitHub, o que permite trabalhar no projeto sem afetar o repositório original. Clique no botão `Fork this repository`:
![builder](assets/04.webp)
- Você então chegará à página de edição do GitHub:
![builder](assets/05.webp)
- Crie uma pasta para sua empresa. Para fazer isso, na caixa `Name your file...`, escreva o nome da sua empresa em letras minúsculas com hífens no lugar de espaços. Por exemplo, se sua empresa se chama "Bitcoin Baguette", você deve escrever `bitcoin-baguette`:
![builder](assets/06.webp)
- Para validar a criação da pasta, simplesmente adicione uma barra após o nome na mesma caixa, por exemplo: `bitcoin-baguette/`. Adicionar uma barra cria automaticamente uma pasta em vez de um arquivo:
![builder](assets/07.webp)
- Nesta pasta, você criará um primeiro arquivo YAML chamado `builder.yml`:
![builder](assets/08.webp)
- Preencha este arquivo com informações sobre sua empresa usando este modelo:

```yaml
name:

address_line_1:
address_line_2:
address_line_3: 

language:
  - 

links:
  website:
  twitter:
  Github:
  youtube:
  nostr:

tags:
  - 
  - 

category:
```

Aqui está o que preencher para cada chave:
- `name`: O nome da sua empresa (obrigatório);
- `address` : A localização do seu negócio (opcional);
- `language` : Os países em que sua empresa opera ou os idiomas suportados (opcional);
- `links` : Os diversos links oficiais do seu negócio (opcional);
- `tags` : 2 termos que qualificam seu negócio (obrigatório);
- `category` : A categoria que melhor descreve o campo em que sua empresa atua dentre as seguintes opções:
	- `wallet` (carteira),
	- `infrastructure` (infraestrutura),
	- `exchange` (câmbio),
	- `education` (educação),
	- `service` (serviço),
	- `communities` (comunidades),
	- `conference` (conferência),
	- `privacy` (privacidade),
	- `investment` (investimento),
	- `node` (nó),
	- `mining` (mineração),
	- `news` (notícias),
	- `manufacturer` (fabricante).
Por exemplo, seu arquivo YAML poderia ter esta aparência:
```yaml
name: Bitcoin Baguette

address_line_1: Paris, França
address_line_2:
address_line_3: 

language:
  - fr
  - en

links:
  website: https://bitcoin-baguette.com
  twitter: https://twitter.com/bitcoinbaguette
  Github:
  youtube:
  nostr:

tags:
  - bitcoin
  - educação

category: educação
```

![builder](assets/09.webp)
- Uma vez que você tenha terminado de fazer alterações neste arquivo, salve-as clicando no botão `Commit changes...`:
![builder](assets/10.webp)
- Adicione um título para suas alterações, junto com uma breve description:
![builder](assets/11.webp)
- Clique no botão verde `Propose changes`:
![builder](assets/12.webp)
- Você então chegará a uma página resumindo todas as suas alterações:
![builder](assets/13.webp)
- Clique na foto do seu perfil do GitHub no canto superior direito, depois em `Your Repositories`:
![builder](assets/14.webp)
- Selecione o seu fork do repositório PlanB Network:
![builder](assets/15.webp)
- Você deverá ver uma notificação no topo da janela com o seu novo branch. Provavelmente se chama `patch-1`. Clique nele:
![builder](assets/16.webp)
- Agora você está no seu branch de trabalho (**certifique-se de que está no mesmo branch que suas modificações anteriores, isso é importante!**):
![builder](assets/17.webp)
- Volte para a pasta `resources/builders/` e selecione a pasta do seu negócio que você acabou de criar no commit anterior:
![builder](assets/18.webp)
- Na pasta do seu negócio, clique no botão `Add file`, depois em `Create new file`:
![builder](assets/19.webp)
- Nomeie esta nova pasta como `assets` e confirme sua criação colocando uma barra `/` no final:
![builder](assets/20.webp)
- Nesta pasta `assets`, crie um arquivo chamado `.gitkeep`:
![builder](assets/21.webp)
- Clique no botão `Commit changes...`:
![builder](assets/22.webp)
- Deixe o título do commit como padrão, e certifique-se de que a caixa `Commit directly to the patch-1 branch` esteja marcada, então clique em `Commit changes`: ![builder](assets/23.webp)
- Volte para a pasta `assets`:
![builder](assets/24.webp)
- Clique no botão `Add file`, depois em `Upload files`:
![builder](assets/25.webp)
- Uma nova página será aberta. Arraste e solte uma imagem da sua empresa ou do seu software na área. Esta imagem será exibida no site da PlanB Network:
![builder](assets/26.webp)
- Pode ser o logo ou um ícone:
![builder](assets/27.webp)
- Uma vez que a imagem esteja carregada, verifique se a caixa `Commit directly to the patch-1 branch` está marcada, então clique em `Commit changes`:
![builder](assets/28.webp)
- Tenha cuidado, sua imagem deve ser quadrada, deve ser nomeada `logo`, e deve estar no formato `.webp`. O nome completo do arquivo deve ser, portanto: `logo.webp`:
![builder](assets/29.webp)
- Volte para a sua pasta `assets` e clique no arquivo intermediário `.gitkeep`:
![builder](assets/30.webp)- Uma vez no arquivo, clique nos três pequenos pontos no canto superior direito e então em `Delete file` (Apagar arquivo):
![builder](assets/31.webp)
- Verifique se você ainda está na mesma branch de trabalho, então clique no botão `Commit changes` (Confirmar alterações):
![builder](assets/32.webp)
- Adicione um título e uma descrição ao seu commit, então clique em `Commit changes` (Confirmar alterações):
![builder](assets/33.webp)
- Volte para a pasta da sua empresa:
![builder](assets/34.webp)
- Clique no botão `Add file` (Adicionar arquivo), depois em `Create new file` (Criar novo arquivo):
![builder](assets/35.webp)
- Crie um novo arquivo YAML nomeando-o com o indicador do seu idioma nativo. Este arquivo será usado para a descrição do construtor. Por exemplo, se eu quiser escrever minha descrição em inglês, nomearei este arquivo como `en.yml`:
![builder](assets/36.webp)
- Preencha este arquivo YAML usando este modelo:
```yaml
description: |
 
contributors:
 - 
```

- Para a chave `contributors` (contribuidores), você pode adicionar seu identificador de contribuidor na Rede PlanB se tiver um. Se não tiver, deixe este campo vazio.
- Para a chave `description` (descrição), você simplesmente precisa adicionar um curto parágrafo que descreva sua empresa ou seu software. A descrição deve estar no mesmo idioma do nome do arquivo. Você não precisa traduzir esta descrição para todos os idiomas suportados no site, pois as equipes da PlanB farão isso usando seu modelo. Por exemplo, aqui está como seu arquivo poderia parecer:
```yaml
description: |
Fundada em 2017, a Bitcoin Baguette é uma associação sediada em Paris dedicada a organizar meetups de Bitcoin e workshops técnicos. Reunimos entusiastas, especialistas e mentes curiosas para explorar e discutir as complexidades da tecnologia Bitcoin. Nossos eventos fornecem uma plataforma para compartilhamento de conhecimento, networking e fomento de um entendimento mais profundo sobre os mecanismos internos do Bitcoin. Junte-se a nós na Bitcoin Baguette para fazer parte da comunidade Bitcoin de Paris e manter-se atualizado com os últimos avanços no campo.

contributors:
- 
```
![builder](assets/37.webp)
- Clique no botão `Commit changes` (Confirmar alterações):
![builder](assets/38.webp)
- Certifique-se de que a caixa `Commit directly to the patch-1 branch` (Confirmar diretamente na branch patch-1) esteja marcada, adicione um título, então clique em `Commit changes` (Confirmar alterações):
![builder](assets/39.webp)
- A pasta da sua empresa agora deve parecer assim:
![builder](assets/40.webp)
- Se tudo estiver de acordo com sua satisfação, retorne à raiz do seu fork:
![builder](assets/41.webp)
- Você deverá ver uma mensagem indicando que sua branch sofreu alterações. Clique no botão `Compare & pull request` (Comparar e criar pull request):
![builder](assets/42.webp)
- Adicione um título claro e uma descrição ao seu PR:
![builder](assets/43.webp)
- Clique no botão `Create pull request` (Criar pull request):
![builder](assets/44.webp)
Parabéns! Seu PR foi criado com sucesso. Um administrador agora irá revisá-lo e, se tudo estiver em ordem, integrá-lo ao repositório principal da Rede PlanB. Você deverá ver seu perfil de construtor aparecer no site alguns dias depois.

Certifique-se de acompanhar o progresso do seu PR. Um administrador pode deixar um comentário pedindo informações adicionais. Enquanto seu PR não for validado, você pode consultá-lo na aba `Pull requests` no repositório GitHub da Rede PlanB:
![builder](assets/45.webp)
Muito obrigado pela sua valiosa contribuição! :)
