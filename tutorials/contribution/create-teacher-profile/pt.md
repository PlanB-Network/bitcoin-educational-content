---
name: Professor Plan ₿ Network
description: Como é que adiciono ou modifico o meu perfil de professor no Plan ₿ Network?
---
![cover](assets/cover.webp)

Se tenciona contribuir para o Plan ₿ Network escrevendo um novo tutorial ou curso, precisará de um perfil de professor. Este perfil permitir-lhe-á receber os devidos créditos pelo conteúdo com que contribui para a plataforma.

Para aqueles que já estiveram envolvidos na criação de conteúdos educativos no Plan ₿ Network, provavelmente já têm um perfil de professor. Ele pode ser encontrado na pasta `/professors` [no nosso repositório GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors). Se o seu perfil já existe, encontre seu login no arquivo `professor.yml`.

Para fazer alterações ao seu perfil, vá para a secção "Editar o seu perfil de professor" no final deste tutorial.

## Adicionar um novo professor com o nosso software

A forma mais fácil de criar o seu perfil de professor no Plan ₿ Network é utilizar a nossa ferramenta Python integrada. Veja como ela funciona.

### 1 - Configurar o seu ambiente local

É necessário ter o seu próprio Fork do [repositório Plan ₿ Network no GitHub] (https://github.com/PlanB-Network/Bitcoin-educational-content).

Sincronize o ramo principal (`dev`) do seu Fork com o repositório de código fonte.

Actualize o seu clone local.

```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
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

Certifique-se de que está no ramo `dev`. Crie um novo ramo com um nome descritivo (por exemplo, `add-professor-loic-morel`).

Publique este ramo no seu Fork online.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```

### 3 - Criar o seu perfil de professor

Vá para a pasta `scripts/tutorial-related/data-creator/` no seu clone local. Certifique-se de ter instalado todas as dependências necessárias para o software, tendo primeiro instalado o Python :

```bash
pip install -r requirements.txt
```

Em seguida, inicie o software com o comando :

```bash
python3 main.py
```

Uma vez na página inicial, introduza o caminho local para o clone do seu repositório, a língua em que está a escrever e o seu ID do GitHub. Se estiver a criar este perfil para outra pessoa e já tiver um perfil de Professor, introduza o seu ID no campo "*PBN Professor's ID*". Se estiver a criar o seu próprio perfil, ainda não terá um ID de Professor, uma vez que está em processo de criação de um, por isso deixe este campo em branco.

Em seguida, clique no botão "*Novo professor*".

![Image](assets/fr/01.webp)

Preencha as informações necessárias (tenha em atenção que todas estas informações serão públicas na nossa plataforma, bem como no GitHub):


- Nome do seu dossier de professor (utilize o seu nome e apelido ou um pseudónimo, em minúsculas) ;
- O seu nome ou alcunha ;
- Geração aleatória do seu login ;
- O seu sítio Web e perfil X (facultativo) ;
- Um Lightning Address para receber donativos dos leitores (opcional) ;
- Selecione 2 ou 3 etiquetas da lista;
- Clique em "*Select Image*" para escolher uma imagem de perfil a partir das suas pastas locais (pode utilizar qualquer nome e formato para a imagem e o software adapta-a automaticamente. Certifique-se apenas de que a imagem é quadrada);
- Escreva uma breve descrição do seu perfil.

Finalizar a criação clicando em "*Criar Professor*". Isto irá automaticamente generate todos os ficheiros necessários para o seu perfil.

![Image](assets/fr/02.webp)

Guarde as suas alterações localmente, criando um commit com uma mensagem explicativa. Envie as alterações para o GitHub do Fork.

```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```

Uma vez terminado, crie um Pull Request (PR) no GitHub para propor a integração das suas modificações. Adicione um título e uma breve descrição ao PR.

### 4 - Revisão e fusão

Aguarde a validação ou o feedback de um administrador. Se necessário, faça correcções e envie novos commits.

```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```

Depois de o PR ter sido fundido, pode eliminar o seu ramo de trabalho.

## Modificar o seu perfil de professor

Se já domina a utilização do Git, modifique o seu perfil de professor criando um novo ramo e editando o ficheiro relevante diretamente na pasta existente. As alterações podem ser feitas no arquivo `professor.yml` ou no arquivo markdown, dependendo das informações a serem corrigidas. Depois de fazer suas alterações localmente, envie-as para o seu Fork e envie um PR.

Para os principiantes, recomendo que façam a modificação diretamente através do Interface web do GitHub. Certifique-se de que tem uma conta GitHub. Se não sabe como criar uma, siga este tutorial :

https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Ir para [o repositório GitHub do Plan ₿ Network dedicado aos dados] (https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors).

![Image](assets/fr/03.webp)

Clique na pasta "*professores*" e, em seguida, aceda à sua pasta pessoal.

![Image](assets/fr/04.webp)

Para alterar os metadados do seu perfil, como o Lightning Address, o nome ou as ligações, selecione o ficheiro "*professor.yml*". Para alterar a sua descrição, clique no ficheiro YAML para o seu idioma (por exemplo, "*en.yml*" ou "*fr.yml*").

Se modificar a sua descrição, lembre-se de remover todas as traduções obsoletas. Depois, pode encarregar-se de traduzir a sua descrição para as outras línguas com a ajuda de um LLM, ou deixar apenas a descrição na sua língua materna e mencionar no seu Pull Request que a sua descrição requer tradução pela nossa equipa.

![Image](assets/fr/05.webp)

Uma vez no ficheiro que pretende modificar, clique no ícone do lápis.

![Image](assets/fr/06.webp)

Se ainda não tiver um Fork do repositório Plan ₿ Network, o GitHub irá sugerir-lhe que crie um. Clique em "*Fork this repository*" (*Fork neste repositório*).

![Image](assets/fr/07.webp)

Faça as alterações desejadas no ficheiro. Quando terminar, clique em "*Commit changes*" (Confirmar alterações).

![Image](assets/fr/08.webp)

Introduza uma mensagem que descreva a sua alteração e, em seguida, selecione "*Propor alterações*".

![Image](assets/fr/09.webp)

Será apresentado um resumo das suas alterações. Se pretender fazer mais alterações ao seu perfil, pode voltar às pastas e fazer mais commits. Quando tiver terminado, clique em "*Criar pedido pull*".

Um Pull Request é um pedido feito para integrar as alterações do seu ramo no ramo principal do repositório Plan ₿ Network, permitindo a revisão e discussão das alterações antes de serem fundidas.

![Image](assets/fr/10.webp)

Certifique-se, no topo do Interface, que o seu ramo de trabalho é fundido com o ramo `dev` do repositório Plan ₿ Network (que é o ramo principal).

Introduza um título que resuma brevemente as alterações que pretende fundir com o repositório de origem. Adicione um breve comentário descrevendo essas alterações e, em seguida, clique no botão Green "*Criar pull request*" para confirmar a pull request:

![Image](assets/fr/11.webp)

O seu PR será então visível no separador "*Pull Request*" do repositório principal do Plan ₿ Network. Tudo o que tem de fazer agora é esperar que um administrador junte a sua modificação.

![Image](assets/fr/12.webp)

Se tiver alguma dificuldade técnica em submeter a sua alteração, não hesite em pedir ajuda no [nosso grupo de Telegrama dedicado às contribuições] (https://t.me/PlanBNetwork_ContentBuilder). Muito obrigado!