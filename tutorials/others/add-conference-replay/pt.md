---
name: Adicionando uma Reprise de Conferência
description: Como adicionar uma reprise de conferência na Rede PlanB?
---
![conference](assets/cover.webp)

A missão da PlanB é fornecer recursos educacionais de primeira linha sobre Bitcoin em tantos idiomas quanto possível. Todo o conteúdo publicado no site é de código aberto e hospedado no GitHub, permitindo que qualquer pessoa contribua para o enriquecimento da plataforma.

Você quer adicionar a reprise da sua conferência sobre Bitcoin no site da Rede PlanB e dar visibilidade a este evento, mas não sabe como? Este tutorial é para você!

No entanto, se você deseja adicionar uma conferência que ocorrerá no futuro, aconselho que leia este outro tutorial no qual explicamos como adicionar um novo evento ao site.

https://planb.network/tutorials/others/add-event


![conference](assets/01.webp)
- Primeiro, você precisa ter uma conta no GitHub. Se não sabe como criar uma conta, fizemos um tutorial detalhado para orientá-lo.

https://planb.network/tutorials/others/create-github-account


- Vá para [o repositório GitHub da PlanB dedicado a dados](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) na seção `resources/conference/`:
![conference](assets/02.webp)
- Clique no canto superior direito no botão `Add file`, depois em `Create new file`:
![conference](assets/03.webp)
- Se você nunca contribuiu para os conteúdos da Rede PlanB antes, precisará criar seu fork do repositório original. Fazer um fork de um repositório significa criar uma cópia desse repositório na sua própria conta do GitHub, o que permite trabalhar no projeto sem afetar o repositório original. Clique no botão `Fork this repository`:
![conference](assets/04.webp)
- Você então chegará à página de edição do GitHub:
![conference](assets/05.webp)
- Crie uma pasta para a sua conferência. Para fazer isso, na caixa `Name your file...`, escreva o nome da sua conferência em letras minúsculas com hífens no lugar de espaços. Por exemplo, se sua conferência se chama "Paris Bitcoin Conference", você deve anotar `paris-bitcoin-conference`. Adicione também o ano da sua conferência, por exemplo: `paris-bitcoin-conference-2024`:
![conference](assets/06.webp)
- Para validar a criação da pasta, simplesmente anote uma barra após o nome na mesma caixa, por exemplo: `paris-bitcoin-conference-2024/`. Adicionar uma barra cria automaticamente uma pasta em vez de um arquivo:
![conference](assets/07.webp)
- Nesta pasta, você criará um primeiro arquivo YAML chamado `conference.yml`:
![conference](assets/08.webp)
Preencha este arquivo com informações relacionadas à sua conferência usando este modelo:
```yaml
year: 
name: 
builder: 
location: 
language: 
  - 
links:
  website: 
  twitter: 
tags: 
  - 
  - 
```

Por exemplo, seu arquivo YAML poderia ficar assim:

```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Paris, France
language: 
  - fr
  - en
links:
  website: https://paris.bitcoin.fr/conference
  twitter: https://twitter.com/ParisBitcoinConference
tags: 
  - International
  - All Public
```

![conference](assets/09.webp)
Se você ainda não possui um identificador "*builder*" para sua organização, pode adicioná-lo seguindo este outro tutorial.
https://planb.network/tutorials/others/add-builder

- Uma vez que tenha terminado de fazer alterações neste arquivo, salve-as clicando no botão `Commit changes...`:
![conferência](assets/10.webp)
- Adicione um título para suas alterações, bem como uma breve descrição:
![conferência](assets/11.webp)
- Clique no botão verde `Propose changes`:
![conferência](assets/12.webp)
- Você então chegará a uma página resumindo todas as suas alterações:
![conferência](assets/13.webp)
- Clique na sua foto de perfil do GitHub no canto superior direito, depois em `Your Repositories`:
![conferência](assets/14.webp)
- Selecione o seu fork do repositório PlanB Network:
![conferência](assets/15.webp)
- Você deve ver uma notificação no topo da janela com o seu novo branch. Provavelmente se chama `patch-1`. Clique nele:
![conferência](assets/16.webp)
- Você está agora no seu branch de trabalho:
![conferência](assets/17.webp)
- Retorne à pasta `resources/conference/` e selecione a pasta da sua conferência que você acabou de criar no commit anterior:
![conferência](assets/18.webp)
- Na pasta da sua conferência, clique no botão `Add file`, depois em `Create new file`:
![conferência](assets/19.webp)
- Nomeie esta nova pasta como `assets` e confirme sua criação colocando uma barra `/` no final:
![conferência](assets/20.webp)
- Nesta pasta `assets`, crie um arquivo chamado `.gitkeep`:
![conferência](assets/21.webp)
- Clique no botão `Commit changes...`:
![conferência](assets/22.webp)
- Deixe o título do commit como padrão, e certifique-se de que a caixa `Commit directly to the patch-1 branch` esteja marcada, depois clique em `Commit changes`:
![conferência](assets/23.webp)
- Retorne à pasta `assets`:
![conferência](assets/24.webp)
- Clique no botão `Add file`, depois em `Upload files`:
![conferência](assets/25.webp)
- Uma nova página será aberta. Arraste e solte uma imagem que represente sua conferência e será exibida no site da PlanB Network: ![conferência](assets/26.webp)
- Pode ser um logo, uma miniatura ou até mesmo um pôster:
![conferência](assets/27.webp)
- Uma vez que a imagem esteja carregada, verifique se a caixa `Commit directly to the patch-1 branch` está marcada, depois clique em `Commit changes`:
![conferência](assets/28.webp)
- Cuidado, sua imagem deve ser nomeada como `thumbnail` e deve estar no formato `.webp`. O nome completo do arquivo deve ser, portanto: `thumbnail.webp`:
![conferência](assets/29.webp)
- Retorne à sua pasta `assets` e clique no arquivo intermediário `.gitkeep`:
![conferência](assets/30.webp)
- Uma vez no arquivo, clique nos 3 pequenos pontos no canto superior direito e depois em `Delete file`:
![conferência](assets/31.webp)
- Verifique se você ainda está no mesmo branch de trabalho, depois clique no botão `Commit changes`:
![conferência](assets/32.webp)
- Adicione um título e uma descrição ao seu commit, depois clique em `Commit changes`:
![conferência](assets/33.webp)
- Volte para a sua pasta de conferência: ![conference](assets/34.webp)
- Clique no botão `Add file`, depois em `Create new file`:
![conference](assets/35.webp)
- Crie um novo arquivo markdown (.md) nomeando-o com o indicador do seu idioma nativo. Este arquivo será usado para as reprises da sua conferência. Por exemplo, se eu quiser escrever as descrições das conferências em Português, nomearei este arquivo como pt.md:
![conference](assets/36.webp)
- Preencha este arquivo markdown usando este modelo que você pode adaptar à configuração da sua conferência:

```markdown
---
name: Conferência Bitcoin Paris 2024
description: A maior conferência de Bitcoin na França com mais de 8.000 participantes a cada ano!
--- 

# Palco Principal

## Sexta-feira de manhã

![video](https://youtu.be/XXXXXXXXXXXX)

## Sexta-feira à tarde

![video](https://youtu.be/XXXXXXXXXXXX)

## Sábado de manhã

![video](https://youtu.be/XXXXXXXXXXXX)

## Sábado à tarde

![video](https://youtu.be/XXXXXXXXXXXX)

# Sala de Workshop

## O Futuro da Mineração de Bitcoin: Desafios e Inovações

![video](https://youtu.be/XXXXXXXXXXXX)

Palestrante: Satoshi Nakamoto, Satoshi Nakamoto

## A Privacidade Ainda é Possível no Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Palestrante: Satoshi Nakamoto

## Bitcoin Core: Mergulho Profundo no Código-Fonte

![video](https://youtu.be/XXXXXXXXXXXX)

Palestrante: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Construindo e Protegendo Carteiras de Bitcoin com Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Palestrante: Satoshi Nakamoto
```

![conference](assets/37.webp)
- No início do seu documento, na "front matter", preencha o campo `name:` com o nome da sua conferência e o ano das reprises. No campo `description:`, escreva uma breve descrição do seu evento no idioma do arquivo. Por exemplo, para um arquivo chamado `pt.md`, a descrição deve ser em Português. A equipe da PlanB Network cuidará da tradução da sua descrição usando o modelo deles.
- Títulos de primeiro nível, marcados por um `#`, são usados para organizar a conferência por cenas. Por exemplo, `# Palco Principal` para o palco principal e `# Sala de Workshop` para um palco dedicado a workshops.

- Títulos de segundo nível, marcados por um duplo `##`, são usados para separar os diferentes vídeos de reprise. Se as conferências foram filmadas continuamente durante meio dia, indique, por exemplo, `## Sexta-feira de manhã`. Se as conferências foram filmadas e transmitidas individualmente, nomeie a conferência diretamente com um título de segundo nível.

- Sob cada título de segundo nível, insira um link para o vídeo de reprise correspondente. A sintaxe deve ser: `![video](https://youtu.be/XXXXXXXXXXXX)`, substituindo `XXXXXXXXXXXX` pelo link real do vídeo.

- Se o formato permitir (conferências individuais), você pode adicionar os nomes dos palestrantes. Para fazer isso, adicione o campo `Speaker:` seguido pelo nome ou pseudônimo do palestrante sob o link do vídeo. Em caso de múltiplos palestrantes, separe cada nome com uma vírgula, assim por exemplo: `Palestrante: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.

---

- Uma vez que suas modificações neste arquivo estejam completas, salve-as clicando no botão `Commit changes...`:
![conference](assets/38.webp)
- Adicione um título para suas modificações, bem como uma breve descrição:
![conference](assets/39.webp)
- Clique em `Commit changes`: ![conference](assets/40.webp)
- Sua pasta de conferência agora deve parecer assim:
![conference](assets/41.webp)
- Se tudo estiver conforme sua satisfação, retorne à raiz do seu fork:
![conference](assets/42.webp)
- Você deverá ver uma mensagem indicando que sua branch passou por modificações. Clique no botão `Compare & pull request`:
![conference](assets/43.webp)
- Adicione um título claro e uma descrição para o seu PR:
![conference](assets/44.webp)
- Clique no botão `Create pull request`:
![conference](assets/45.webp)
Parabéns! Seu PR foi criado com sucesso. Um administrador agora irá revisá-lo e, se tudo estiver em ordem, mesclá-lo ao repositório principal da Rede PlanB. Você deverá ver as reprises da sua conferência aparecerem no site alguns dias depois.

Por favor, certifique-se de acompanhar o progresso do seu PR. É possível que um administrador deixe um comentário pedindo informações adicionais. Enquanto seu PR não for validado, você pode visualizá-lo sob a aba `Pull requests` no repositório GitHub da Rede PlanB:
![conference](assets/46.webp)

Muito obrigado pela sua valiosa contribuição! :)
