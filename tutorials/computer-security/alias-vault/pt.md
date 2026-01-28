---
name: Alias Vault
description: Ferramenta poderosa para gerir palavras-passe, autenticação de dois factores e pseudónimos (com servidor de correio eletrónico integrado)
---

![cover](assets/cover.webp)



A privacidade e a segurança em linha é um tema a que qualquer pessoa, independentemente da sua atividade, deve prestar muita atenção.



Além disso, estas questões fazem parte de um mundo em constante agitação: cada vez mais programadores participam no tema, trazendo implementações para soluções estabelecidas e novos produtos.



É o caso de **Leendert de Borst** e do seu `Alias Vault`, uma ferramenta revolucionária (a primeira do seu género) que lhe permite gerir e armazenar palavras-passe, utilizar registos de palavras-passe para autenticar serviços Web, administrar a autenticação de dois factores, mas, mais importante, generate _aliases_ reais, tudo num único Interface.



**Mas o Alias Vault não se fica por aqui.



## Caraterísticas principais



O Alias Vault funciona na nuvem nos servidores do programador ou auto-hospedado na sua própria infraestrutura, uma opção para a qual estão disponíveis ficheiros e imagens Docker para instalar com um scipt. Para além do Interface Web, estão disponíveis extensões para todos os navegadores populares, bem como aplicações móveis para iOS e Android; estas últimas também podem ser descarregadas a partir do F-Droid, contornando a loja oficial da Google.



Num dos Interface, o Alias Vault é:




- Gratuito e de fonte aberta**
- Password Manager**, para armazenar todas as palavras-passe complexas. Utilizando a extensão do navegador, o gestor de senhas completa os logins em sites
- 2FA**, para suportar a autenticação de dois factores
- Gestor de aliases com servidor de correio eletrónico incorporado**: O Alias Vault não cria aliases que reencaminham correio eletrónico para a caixa de correio de um utilizador; em vez disso, cria alter-egos reais, completos com nome próprio, apelido, sexo, nome de utilizador, palavra-passe e data de nascimento (se esta informação for necessária).



Uma documentação extensa e completa faz parte do pacote, que acompanhará os recém-chegados à descoberta desta poderosa ferramenta.



## Sem dados pessoais!



Começa, como sempre, a partir do sítio Web [aliasvault.net](aliasvault.net). Como mencionado, o Alias Vault pode ser utilizado no seu próprio servidor, ou a partir da nuvem do programador para se familiarizar com ele antes de passar para a solução auto-hospedada.



O sítio tem gráficos muito apelativos e bem conservados, mas o melhor é começar a pôr as mãos na massa: **criar a sua conta**.



![img](assets/en/01.webp)



Para sua enorme surpresa, descobrirá que o Alias Vault não pede informações pessoais: tudo o que precisa para criar a conta é uma alcunha qualquer, uma palavra que lhe seja familiar, desde que esteja disponível. Concorde com os Termos de Serviço, escolha a palavra e continue.



![img](assets/en/02.webp)



Defina agora a **`senha mestra`**, que é a informação mais importante de todo o seu novo sistema. Com esta palavra-passe, de facto, será a única pessoa que poderá aceder/recuperar a conta, uma vez que manterá o seu `vault` encriptado no servidor que irá alojar a sua informação.



![img](assets/en/03.webp)



Facto: Criou o seu próprio gestor de palavras-passe e gestor de pseudónimos, mas sem fornecer o seu próprio e-mail privado e funcional Address.



![img](assets/en/04.webp)



O Alias Vault dá-vos as boas-vindas a um espaço seguro, novo, pessoal, mas também vazio. E agora começamos a povoá-lo um pouco.



Se já tiver um gestor de senhas, pode importar o ficheiro do que está a utilizar, para avaliar as diferenças com outro fornecedor, ou talvez eliminar o gestor de pseudónimos para poder gerir tudo numa única aplicação.



![img](assets/en/05.webp)



O Alias Vault é extremamente simples: tem uma página principal, que é a `Home`, com dois menus:




- `Credentials`: permite-lhe criar e gerir identidades e aliases
- `Email`: uma caixa de entrada onde pode verificar as mensagens recebidas para aliases que gerou.



![img](assets/en/06.webp)



É a criação de um primeiro `alias` que nos interessa fazer, por isso, vá para o canto superior direito da página e clique em _+New Alias_.



![img](assets/en/07.webp)



Inicialmente, o menu tem um aspeto minimalista, de acordo com a filosofia do Alias Vault. Para descobrir as caraterísticas desta função, clique em _Criar através do modo avançado_.



![img](assets/en/08.webp)



A parte superior do primeiro ecrã pode ser utilizada para importar credenciais de palavra-passe que já utiliza para serviços que subscreveu ou que utiliza mais frequentemente em linha.



Se tiver ativado a autenticação de dois factores em qualquer (ou em todos) dos serviços acima referidos, com o Alias Vault também pode gerir este Layer adicional de segurança importando a `chave secreta`. O Alias Vault criará a `TOTP` necessária para o acesso.



![img](assets/en/09.webp)



**Cuidado**: No espaço reservado para o e-mail Address, o Alias Vault propõe o seu próprio domínio por defeito; para utilizar o Address correto com que criou contas anteriormente, clique em _Enter domínio personalizado_, para que possa definir o domínio correto depois de `@`.



![img](assets/en/14.webp)



A parte inferior deste ecrã é a mais divertida. Clique em _Gerar pseudónimo aleatório_ e o Alias Vault criará identidades separadas para si para diferentes necessidades, cada uma com a sua própria caixa de correio, palavras-passe de nível muito robusto, complementadas com outros detalhes como o sexo, a data de nascimento e uma alcunha adequada.



![img](assets/en/10.webp)



A partir de um menu apropriado, pode alterar as definições que afectam a geração de palavras-passe, como escolher apenas letras minúsculas e eliminar caracteres que possam ser ambíguos.



![img](assets/en/11.webp)



Pode utilizar o pseudónimo de correio eletrónico sugerido pelo Cofre de pseudónimos ou alterar os domínios se clicar no menu pendente correspondente.



![img](assets/en/12.webp)



Antes de utilizar este correio eletrónico para um serviço de início de sessão, pode testar a sua funcionalidade enviando uma mensagem de um Address seu para a caixa de correio recém-criada.



![img](assets/en/13.webp)



**⚠️ AVISO**: A receção de e-mails é possível graças ao servidor incorporado no Alias Vault, mas este apenas permite receber e-mails e não responder, ou utilizar a caixa de e-mail com as funções "convencionais" de um serviço `alias`. Difere assim bastante do Simple Login, Addy e outras plataformas que se dedicam exclusivamente a este tipo de serviço. Para o exemplo do Simple Login, pode ver o tutorial dedicado:



https://planb.academy/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

Para eliminar um alias que criou como teste, basta entrar no seu `Home`, depois em `Credentials` e clicar na identidade que pretende eliminar. O comando _Delete_ aparecerá no canto superior direito para que possa prosseguir.



![img](assets/en/16.webp)



## Extensão do navegador



Dependendo das suas necessidades, pode recorrer à extensão do navegador, que pode ser encontrada nos navegadores mais utilizados.



![img](assets/en/15.webp)



A instalação é feita como já aconteceu com todas as outras extensões, pelo que não me vou alongar sobre esse pormenor.



A extensão do browser existe para facilitar o início de sessão em serviços online ou para criar novos pseudónimos conforme necessário: se o serviço estiver armazenado nos registos do Cofre de pseudónimos, o preenchimento automático faz o que é necessário.



![img](assets/en/17.webp)



O único cuidado a ter é verificar se o Alias Vault está ativo. De facto, a aplicação tem uma predefinição em que faz uma pausa após um período de inatividade. Trata-se de uma caraterística muito útil, **quando tem de se afastar do computador, por exemplo, e impedir que outra pessoa aceda às suas contas**. Um procedimento simplificado permite-lhe iniciar novamente a sessão introduzindo a "palavra-passe principal", se a sessão anterior ainda estiver na cache. O tempo para terminar a sessão é um dos parâmetros que pode personalizar, encurtando-o ou alongando-o de acordo com as suas preferências.



## Aplicação móvel



Como todas as aplicações deste género que se prezam, o Alias Vault tem uma versão para dispositivos móveis, tanto em ambiente Android como iOS. Para Android, pode descarregar a aplicação a partir de [F-Droid](https://f-droid.org/packages/net.aliasvault.app/).



No momento em que este texto foi escrito (final de agosto de 2025), a aplicação móvel considera o "preenchimento automático" uma funcionalidade experimental, não funcionando, exceto em muito poucos sites. Até estar totalmente implementada, a utilização do Alias Vault no telemóvel requer copiar/colar dados.



Depois de descarregar a aplicação da loja, para iniciar sessão basta introduzir o utilizador e a `palavra-passe principal` criados na aplicação Web.



![img](assets/en/18.webp)



Ao abrir o seu `vault`, ser-lhe-á perguntado se pretende ativar o acesso controlado por biometria, um Layer adicional de segurança para impedir que outra pessoa aceda às suas palavras-passe se tiver o seu telemóvel na mão.



![img](assets/en/19.webp)



Se decidir configurar o controlo biométrico, vá em frente. Se saltar esta etapa e mudar de ideias, também pode configurá-la mais tarde no menu _Configurações_.



Uma vez terminado o início de sessão, os dados já criados serão novamente sincronizados.



![img](assets/en/20.webp)



A aplicação móvel pode ser encaminhada para a ligação ao "cofre" alojado no seu próprio servidor.



![img](assets/en/22.webp)



E é precisamente a versão auto-hospedada que iremos abordar brevemente na próxima secção.



## Auto-hospedagem: controlo total sobre os seus dados



O Alias Vault, para ser justo, não é o primeiro "gestor de palavras-passe" que lhe permite implementar o serviço na sua infraestrutura. Existem outros, mas alguns têm limitações ou são parcialmente de código fechado.



A oportunidade é única: **Acabar com a dependência de fornecedores de serviços externos ou de nuvens, mas utilizar o seu próprio servidor local para guardar e gerir as palavras-passe, os pseudónimos e as informações extremamente sensíveis associadas a tudo isto**. Com o Alias Vault, também pode fazer com que o serviço de correio eletrónico aponte para o seu próprio servidor de correio eletrónico para maior confidencialidade.



É altura de consultar a [documentação](https://docs.aliasvault.net/installation/), para saber como proceder para alojar o Alias Vault.



![img](assets/en/23.webp)



O Alias Vault é executado no Docker Compose, portanto, é necessária uma experiência mínima com Linux e Docker. Pode começar com a instalação básica e depois completar com soluções mais avançadas.



O seu servidor deve estar a funcionar numa máquina de 64 bits, com uma distribuição Linux, 1 GB de RAM e, pelo menos, 16 GB de armazenamento; a versão do Docker (CE) deve ser, pelo menos, a 20.10 ou superior, enquanto o Docker Compose requer uma versão a partir da 2.0.



Decidi experimentar o Alias Vault com um thin client, no qual o DietPi está instalado como uma distribuição, uma base Debian Bookworm, otimizada para o essencial e já rodando `Docker` e `Docker Compose`.



Primeiro, para ter alguma ordem, crie um diretório em sua home, abra o `terminal` e cole o comando para executar o script de instalação.



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



Quando a instalação estiver concluída, encontrará as suas credenciais de acesso:


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



Verificar o conteúdo do diretório após a instalação.



![img](assets/en/29.webp)



Para iniciar o Alias Vault, utilize o comando:



``` Launch-Alias-Vault


./install.sh iniciar


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/user/start


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## Considerações sobre encriptação e segurança



![img](assets/en/32.webp)



De acordo com o que a Lanedirt afirma no site, na documentação e no Github, com o Alias Vault **todas as informações (componentes) que coloca no Alias Vault permanecem firmemente ligadas ao dispositivo, encriptadas e inacessíveis a qualquer pessoa que não saiba a `senha mestra`**.



A "palavra-passe mestra" é assim o elemento fundamental de todo o "cofre". Depois de introduzida, é processada com o algoritmo `Argon2id`, uma função de derivação de chaves de memória Hard, para impedir que o segredo saia do dispositivo.



Tudo permanece oculto, mesmo para o gestor da nuvem ou do serviço de alojamento. De facto, a partir do painel de administração não é possível aceder aos dados dos utilizadores, apenas é possível saber se criaram aliases, se receberam e-mails e pouco mais.



Todos os conteúdos armazenados são encriptados e desencriptados por chaves criptográficas derivadas da "palavra-passe principal". **Apenas os dados encriptados são armazenados no servidor, nada aparece em texto simples**. Se um utilizador se esquecer ou perder a sua `senha mestra`, a conta a ela associada é irreversivelmente perdida, uma vez que o servidor não pode aceder aos conteúdos em texto simples.



Para a versão auto-hospedada, existe um script para redefinir a `senha mestra`, mas isso não evita a perda de dados.



![img](assets/en/33.webp)



Uma vez que o Alias Vault se encontra na fase _Beta_, poderá ter dificuldade em aceder-lhe se alterar/atualizar a palavra-passe mestra. Sugiro que a escolha seja robusta e complexa desde o início, para que possa experimentar o serviço e, eventualmente, decidir se o quer utilizar. Se tiver dificuldade em aceder à nuvem após a atualização da palavra-passe, contacte o suporte do Alias Vault.



Para uma compreensão completa da arquitetura e da segurança adoptadas pelo Alias Vault, recomendo vivamente que consulte [esta página](https://docs.aliasvault.net/architecture/), que contém pormenores sobre a criptografia subjacente ao seu funcionamento.



## Mapa rodoviário


A intenção dos criadores é tornar o Alias Vault maduro e estável até ao final de 2025, de modo a definir as suas caraterísticas de utilização futura.



O Alias Vault é e continuará a ser de código aberto e gratuito, mas provavelmente não de forma ilimitada como na versão beta. Algumas funcionalidades pagas estão em vias de ser implementadas, tal como já foi anunciado.



Existem planos de equipa/família e suporte para chaves de hardware, este último para autenticação com FIDO2 ou WebAuth.



## Quem precisa do Alias Vault?



**Uma ferramenta como esta é ideal para quem coloca a privacidade online em primeiro lugar**.



A sua identidade está, com toda a probabilidade, no centro dos negócios que efectua em linha e deve ser salvaguardada por todos os meios para colocar **esses** dados longe de serviços, empresas e corretores dispostos a tudo para deitar a mão ao seu comportamento em linha.



O Alias Vault devolve-lhe o controlo total sobre as suas credenciais, atenuando ou eliminando completamente a necessidade de confiar em terceiros para proteger e encriptar os seus dados mais sensíveis.



A arquitetura e a facilidade criptográfica do Alias Vault são ideais para indivíduos soberanos, pequenas e médias empresas, equipas de desenvolvimento e todos os entusiastas de aplicações **open source**. Se se enquadra em qualquer uma destas categorias: divirta-se a descobrir o Alias Vault.