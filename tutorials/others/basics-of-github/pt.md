---
name: Os Fundamentos do GitHub
description: Entendendo os fundamentos do Git e GitHub
---

![cover](assets/cover.webp)

A missão da PlanB é fornecer recursos educacionais de primeira linha sobre Bitcoin, disponíveis em tantos idiomas quanto possível. Todo o conteúdo publicado no site é de código aberto e hospedado no GitHub, oferecendo a qualquer pessoa a oportunidade de contribuir para o enriquecimento da plataforma. As contribuições podem assumir várias formas: corrigir e revisar textos existentes, traduzir para outros idiomas, atualizar informações ou criar novos tutoriais ainda não disponíveis em nosso site.

Se você deseja contribuir para a Rede PlanB, precisará usar o Git e o GitHub. Se estas ferramentas são desconhecidas para você ou se o seu funcionamento parece obscuro, não entre em pânico, este artigo é para você! Vamos revisar juntos os fundamentos do Git e GitHub, bem como o jargão técnico associado, para permitir que você use efetivamente estas ferramentas posteriormente.

## O que é Git?

Git é um sistema de controle de versão, especificamente projetado para gerenciar projetos de software. Criado em 2005 por Linus Torvalds, o Git rapidamente se tornou o padrão na indústria de desenvolvimento de software para controle de versão. Mas o que isso realmente significa?
![git](assets/1.webp)
No seu núcleo, o Git permite que os desenvolvedores rastreiem as mudanças feitas no código-fonte de um projeto ao longo do tempo. Isso significa que a cada alteração no código, o Git registra uma nova versão do projeto. Se ocorrer um erro ou se uma funcionalidade experimental não funcionar como esperado, é possível reverter para um estado anterior do código, como uma espécie de máquina do tempo para arquivos.

Uma das características-chave do Git é o gerenciamento de branches. Uma branch é uma espécie de linha paralela onde os desenvolvedores podem trabalhar independentemente do restante do projeto. Isso facilita muito a adição de novas funcionalidades ou a correção de bugs sem perturbar o código principal. Uma vez que as modificações são testadas e validadas, elas podem ser mescladas com a branch principal.

Uma das peculiaridades do Git é sua capacidade de operar de maneira distribuída. Cada desenvolvedor tem uma cópia completa do projeto no disco rígido do próprio computador, permitindo que trabalhem offline e mesclam as alterações mais tarde, quando uma conexão com a Internet estiver disponível. Isso reduz o risco de conflitos e permite que vários desenvolvedores trabalhem simultaneamente no mesmo projeto sem atrapalhar uns aos outros.
Inicialmente, o Git foi projetado principalmente para projetos de desenvolvimento de software. No entanto, também pode ser usado para gerenciar projetos de escrita de conteúdo. Em vez de colaborar em código, colaboramos em texto. E é exatamente este método que a Rede PlanB adotou para gerenciar seu conteúdo! O Git facilita a colaboração na escrita de cursos e tutoriais, pois permite um rastreamento preciso das alterações, um gerenciamento eficiente de versões e também possibilita a revisão e melhoria do conteúdo por outros contribuidores.
## O que é GitHub?

GitHub é uma plataforma de gerenciamento e hospedagem de código-fonte baseada no sistema de controle de versão Git que acabamos de discutir. Lançado em 2008, o GitHub rapidamente ganhou popularidade e se tornou uma referência essencial para desenvolvedores em todo o mundo. Mas como o GitHub difere do Git e por que é tão crucial no nosso método de produção de conteúdo?
![github](assets/2.webp)
Primeiro, é importante entender que o GitHub é construído sobre o Git (que discutimos na seção anterior). Enquanto o Git é a ferramenta que rastreia as mudanças no código, o GitHub é o serviço online que hospeda, compartilha e gerencia esse código.

Imagine o Git como uma espécie de diário que cada desenvolvedor usa no próprio computador para registrar todas as mudanças em seu projeto. O GitHub, por outro lado, é como uma biblioteca pública onde todos esses diários podem ser compartilhados, comparados e combinados.
A diferença fundamental entre Git e GitHub reside na sua função: Git é a ferramenta utilizada localmente por cada desenvolvedor para gerenciar suas versões de código, enquanto o GitHub é a plataforma online que hospeda essas versões e facilita a colaboração.
O GitHub é muito mais do que apenas um serviço de hospedagem de código. É uma plataforma de colaboração que permite aos desenvolvedores trabalharem juntos de forma eficiente. E de fato, a PlanB Network utiliza esta plataforma para hospedar não apenas todo o código que alimenta o site, mas também, e isso é o que nos interessa, todo o conteúdo (tutoriais, treinamentos, recursos...).

## Alguns Termos Técnicos

No Git e GitHub, você encontrará comandos e recursos cujos nomes podem parecer complexos. Nesta última parte, forneço definições simples para entender os termos técnicos que você pode encontrar ao usar o Git e GitHub:

- **Fetch origin:** Comando que recupera informações recentes e alterações de um repositório remoto sem mesclá-las com seu trabalho local. Ele atualiza seu repositório local com novas branches e commits presentes no repositório remoto.

- **Pull origin:** Comando que recupera atualizações de um repositório remoto e as integra imediatamente em sua branch local para sincronizá-la. Isso combina os passos de fetch e merge em um único comando.
- **Sync Fork:** Um recurso no GitHub que permite atualizar seu fork de um projeto com as últimas mudanças do repositório fonte. Isso garante que sua cópia do projeto permaneça atualizada com o desenvolvimento principal.
- **Push origin:** Comando usado para enviar suas alterações locais para um repositório remoto.

- **Pull Request:** Uma solicitação enviada por um colaborador para indicar que eles fizeram push de alterações para uma branch em um repositório remoto e desejam que essas alterações sejam revisadas e potencialmente mescladas na branch principal do repositório.

- **Commit:** Salvar suas alterações. Um commit é como um instantâneo instantâneo do seu trabalho em um determinado momento, que permite manter um histórico de alterações. Cada commit inclui uma mensagem descritiva explicando o que foi modificado.

- **Branch:** Uma versão paralela do repositório, permitindo trabalhar em alterações sem afetar a branch principal (muitas vezes chamada de "main" ou "master"). Branches facilitam o desenvolvimento de novas funcionalidades e a correção de bugs sem o risco de perturbar o código estável.

- **Merge:** Mesclar consiste em integrar as alterações de uma branch em outra. É usado, por exemplo, para adicionar as alterações de uma branch de trabalho na branch principal, o que permite adicionar as várias contribuições.

- **Fork:** Fazer um fork de um repositório significa criar uma cópia desse repositório em sua própria conta no GitHub, o que permite trabalhar no projeto sem afetar o repositório original. O fork pode seguir seu próprio caminho e se tornar um projeto diferente do original, ou pode se sincronizar regularmente com o projeto original para contribuir com ele.

- **Clone:** Clonar um repositório significa fazer uma cópia local no seu computador, o que lhe dá acesso a todos os arquivos e ao histórico. Isso permite trabalhar diretamente no projeto localmente.

- **Repository:** Espaço de armazenamento para um projeto no GitHub. Um repositório contém todos os arquivos do projeto, bem como o histórico de todas as alterações que foram feitas nele. É a base de armazenamento e colaboração no GitHub.

- **Issue:** Uma ferramenta para rastrear tarefas e bugs no GitHub. Issues permitem relatar problemas, propor melhorias ou discutir novas funcionalidades. Cada issue pode ser atribuída, rotulada e comentada.

Esta lista obviamente não é exaustiva. Há muitos outros termos técnicos específicos para Git e GitHub. No entanto, os mencionados aqui são os principais com os quais você frequentemente se deparará.
Após ler este artigo, é possível que alguns aspectos do Git e do GitHub ainda estejam pouco claros para você. Eu o encorajo a começar a usar essas ferramentas por conta própria. A prática é frequentemente a melhor maneira de entender como a máquina funciona! E para começar, você pode descobrir estes outros 2 tutoriais:
**[Crie sua conta no GitHub](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Configurando Seu Ambiente Local para Contribuir com a PlanB Network](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**