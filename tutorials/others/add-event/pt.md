---
name: Adicionar um evento na PlanB Network
description: Como sugiro adicionar um novo evento na PlanB Network?
---
![evento](assets/cover.webp)

A missão da PlanB é fornecer recursos educacionais de primeira linha sobre Bitcoin em tantos idiomas quanto possível. Todo o conteúdo publicado no site é de código aberto e hospedado no GitHub, oferecendo a qualquer pessoa a oportunidade de contribuir para o enriquecimento da plataforma.

Se você quer adicionar uma conferência sobre Bitcoin ao site da Rede PlanB e aumentar a visibilidade do seu evento, mas não sabe como? Este tutorial é para você!
![evento](assets/01.webp)
- Primeiro, você precisa ter uma conta no GitHub. Se você não sabe como criar uma conta, fizemos um tutorial detalhado para guiá-lo.

https://planb.network/tutorials/others/create-github-account


- Vá para [o repositório GitHub da PlanB dedicado a dados](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) na seção `resources/conference/`:
![evento](assets/02.webp)
- Clique no canto superior direito no botão `Add file`, depois em `Create new file`:
![evento](assets/03.webp)
- Se você nunca contribuiu para os conteúdos da Rede PlanB antes, precisará criar seu fork do repositório original. Fazer um fork de um repositório significa criar uma cópia desse repositório em sua própria conta do GitHub, permitindo que você trabalhe no projeto sem afetar o repositório original. Clique no botão `Fork this repository`:
![evento](assets/04.webp)
- Você então chegará à página de edição do GitHub:
![evento](assets/05.webp)
- Crie uma pasta para sua conferência. Para fazer isso, na caixa `Name your file...`, escreva o nome da sua conferência em letras minúsculas com hífens no lugar de espaços. Por exemplo, se sua conferência se chama "Paris Bitcoin Conference", você deve anotar `paris-bitcoin-conference`. Adicione também o ano da sua conferência, por exemplo: `paris-bitcoin-conference-2024`:
![evento](assets/06.webp)
- Para validar a criação da pasta, simplesmente anote uma barra após o seu nome na mesma caixa, por exemplo: `paris-bitcoin-conference-2024/`. Adicionar uma barra cria automaticamente uma pasta em vez de um arquivo:
![evento](assets/07.webp)
- Nesta pasta, você criará um primeiro arquivo YAML chamado `events.yml`:
![evento](assets/08.webp)
- Preencha este arquivo com informações sobre sua conferência usando este modelo:

```yaml
- start_date:
  end_date:
  address_line_1:
  address_line_2: 
  address_line_3: 
  name:
  builder:
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description:
  language: 
    - 
  links:
    website:
    replay_url:    
    live_url :
  tags: 
    - 
```

Por exemplo, seu arquivo YAML poderia ficar assim:

```yaml
- start_date: 2024-08-15
  end_date: 2024-08-18
  address_line_1: Paris, França
  address_line_2: 
  address_line_3: 
  name: Paris Bitcoin Conference 2024
  builder: Paris Bitcoin Conference
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description: A maior conferência sobre Bitcoin na França com mais de 8.000 participantes a cada ano!
  language:
- fr    - en
    - es
    - it
  links:
    website: https://paris.bitcoin.fr/conference
    replay_url:
    live_url :
  tags: 
    - Bitcoiner
    - Geral
    - Internacional
```
![evento](assets/09.webp)
Se você ainda não possui um identificador "*builder*" para sua organização, você pode adicioná-lo seguindo este outro tutorial.

https://planb.network/tutorials/others/add-builder



- Uma vez que você tenha terminado de fazer alterações neste arquivo, salve-as clicando no botão `Commit changes...`:
![evento](assets/10.webp)
- Adicione um título para suas alterações, bem como uma breve description:
![evento](assets/11.webp)
- Clique no botão verde `Propose changes`:
![evento](assets/12.webp)
- Você então chegará a uma página resumindo todas as suas alterações:
![evento](assets/13.webp)
- Clique na foto do seu perfil do GitHub no canto superior direito, depois em `Your Repositories`:
![evento](assets/14.webp)
- Selecione seu fork do repositório PlanB Network:
![evento](assets/15.webp)
- Você deverá ver uma notificação no topo da janela com seu novo branch. Provavelmente se chama `patch-1`. Clique nele:
![evento](assets/16.webp)
- Agora você está no seu branch de trabalho:
![evento](assets/17.webp)
- Volte para a pasta `resources/conference/` e selecione a pasta da sua conferência que você acabou de criar no commit anterior:
![evento](assets/18.webp)
- Na pasta da sua conferência, clique no botão `Add file`, depois em `Create new file`:
![evento](assets/19.webp)
- Nomeie esta nova pasta como `assets` e confirme sua criação colocando uma barra `/` no final:
![evento](assets/20.webp)
- Nesta pasta `assets`, crie um arquivo chamado `.gitkeep`:
![evento](assets/21.webp)
- Clique no botão `Commit changes...`:
![evento](assets/22.webp)
- Deixe o título do commit como padrão, e certifique-se de que a caixa `Commit directly to the patch-1 branch` esteja marcada, então clique em `Commit changes`:
![evento](assets/23.webp)
- Retorne para a pasta `assets`:
![evento](assets/24.webp)
- Clique no botão `Add file`, depois em `Upload files`: ![evento](assets/25.webp)
- Uma nova página será aberta. Arraste e solte uma imagem que represente sua conferência e será exibida no site da PlanB Network:
![evento](assets/26.webp)
- Pode ser o logo, uma miniatura ou até mesmo um pôster:
![evento](assets/27.webp)
- Uma vez que a imagem esteja carregada, verifique se a caixa `Commit directly to the patch-1 branch` está marcada, então clique em `Commit changes`:
![evento](assets/28.webp)
- Cuidado, sua imagem deve ser nomeada `thumbnail` e deve estar no formato `.webp`. O nome completo do arquivo deve ser, portanto: `thumbnail.webp`:
![evento](assets/29.webp)
- Retorne para sua pasta `assets` e clique no arquivo intermediário `.gitkeep`:
![evento](assets/30.webp)
- Uma vez no arquivo, clique nos 3 pequenos pontos no canto superior direito e depois em `Delete file`:
![event](assets/31.webp)- Verifique se você ainda está na mesma branch de trabalho, então clique no botão `Commit changes`:
![event](assets/32.webp)
- Adicione um título e uma descrição ao seu commit, depois clique em `Commit changes`:
![event](assets/33.webp)
- Volte para a raiz do seu repositório:
![event](assets/34.webp)
- Você deverá ver uma mensagem indicando que sua branch passou por alterações. Clique no botão `Compare & pull request`:
![event](assets/35.webp)
- Adicione um título claro e uma descrição ao seu PR:
![event](assets/36.webp)
- Clique no botão `Create pull request`:
![event](assets/37.webp)
Parabéns! Seu PR foi criado com sucesso. Um administrador agora irá verificar e, se tudo estiver em ordem, mesclará ao repositório principal da PlanB Network. Você deverá ver seu evento aparecer no site alguns dias depois.

Certifique-se de acompanhar o progresso do seu PR. Um administrador pode deixar um comentário pedindo informações adicionais. Enquanto seu PR não for validado, você pode consultá-lo na aba `Pull requests` no repositório GitHub da PlanB Network:
![event](assets/38.webp)
Muito obrigado pela sua valiosa contribuição! :)

