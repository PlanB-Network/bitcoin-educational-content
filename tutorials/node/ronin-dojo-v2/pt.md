---
name: RoninDojo v2
description: Instalando seu nó Bitcoin RoninDojo v2 em um Raspberry Pi
---
![capa RoninDojo v2](assets/cover.webp)

***ATENÇÃO:** Após a prisão dos fundadores da Samourai Wallet e a apreensão dos seus servidores em 24 de abril, algumas funcionalidades do RoninDojo, como o Whirlpool, não estão mais operacionais. No entanto, é possível que essas ferramentas sejam reativadas ou relançadas de forma diferente nas próximas semanas. Além disso, como o código do RoninDojo estava hospedado no GitLab da Samourai, que também foi apreendido, atualmente não é possível fazer o download do código remotamente. É provável que as equipes do RoninDojo estejam trabalhando para republicar o código.*

_Estamos acompanhando de perto a evolução deste caso, bem como os desenvolvimentos relacionados às ferramentas associadas. Fique assegurado de que atualizaremos este tutorial à medida que novas informações estiverem disponíveis._

_Este tutorial é fornecido apenas para fins educativos e informativos. Não endossamos nem encorajamos o uso dessas ferramentas para fins criminosos. É responsabilidade de cada usuário cumprir as leis em sua jurisdição._

---

> "*Use Bitcoin com privacidade.*"

Em um tutorial anterior, já havíamos explicado o procedimento para instalar e usar o RoninDojo v1. No entanto, ao longo do último ano, as equipes do RoninDojo lançaram a versão 2 de sua implementação, que marcou um ponto de virada significativo na arquitetura do software. De fato, eles se afastaram da distribuição Linux Manjaro em favor do Debian. Consequentemente, eles não oferecem mais uma imagem pré-configurada para instalação automática no Raspberry Pi. Mas ainda existe um método para proceder com uma instalação manual. Foi o que usei para meu próprio nó, e desde então, o RoninDojo v2 tem funcionado maravilhosamente no meu Raspberry Pi 4. Portanto, estou oferecendo um novo tutorial sobre como instalar manualmente o RoninDojo v2 em um Raspberry Pi.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0



## Índice:
- O que é RoninDojo?
- Qual hardware escolher para instalar o RoninDojo v2?
- Como montar o Raspberry Pi 4?
- Como instalar o RoninDojo v2 em um Raspberry Pi 4?
- Como usar seu nó RoninDojo v2?

## O que é RoninDojo?
Dojo é inicialmente uma implementação completa de nó Bitcoin, baseada no Bitcoin Core, e desenvolvida pelas equipes da Samourai Wallet. Esta solução pode ser instalada em qualquer equipamento. Ao contrário de outras implementações Core, o Dojo foi especificamente otimizado para integrar com o ambiente de aplicativos Android da Samourai Wallet. Quanto ao RoninDojo, é uma utilidade projetada para facilitar a instalação e gestão de um Dojo, bem como várias outras ferramentas complementares. Em resumo, o RoninDojo enriquece a implementação básica do Dojo integrando uma multitude de ferramentas adicionais, ao mesmo tempo que simplifica sua instalação e gestão.

Ronin também oferece [uma solução de nó-em-caixa, chamada "*Tanto*"](https://ronindojo.io/en/products), um dispositivo com RoninDojo já instalado em um sistema montado por sua equipe. O Tanto é uma opção paga, que pode ser interessante para aqueles que preferem evitar complicações técnicas. Mas, como o código-fonte do RoninDojo é aberto, também é possível implantá-lo em seu próprio hardware. Esta alternativa, mais econômica, no entanto, requer algumas manipulações adicionais, que abordaremos neste tutorial.
RoninDojo é um Dojo, portanto, permite a fácil integração do Whirlpool CLI em seu nó Bitcoin para proporcionar a melhor experiência possível de coinjoin. Com o Whirlpool CLI, torna-se possível remixar continuamente seus bitcoins, 24 horas por dia, 7 dias por semana, sem a necessidade de seu computador pessoal permanecer ligado.

Além do Whirlpool CLI, o RoninDojo inclui uma variedade de ferramentas para aprimorar as funcionalidades do seu Dojo. Entre estas, o calculador Boltzmann analisa o nível de privacidade de suas transações, o servidor Electrum permite a conexão de suas carteiras Bitcoin ao seu nó, e o servidor Mempool possibilita visualizar suas transações localmente, sem vazar informações.
Comparado a outras soluções de nó como Umbrel, RoninDojo é claramente focado em soluções on-chain e ferramentas de privacidade. Diferente do Umbrel, RoninDojo não suporta a configuração de um nó Lightning nem a integração de aplicações de servidor mais generalistas. Embora RoninDojo ofereça menos ferramentas versáteis do que Umbrel, ele possui todas as funcionalidades essenciais para gerenciar sua atividade on-chain.
Se você não precisa de funcionalidades generalistas ou aquelas relacionadas à Rede Lightning como oferecido pelo Umbrel, e está procurando por um nó simples, estável com ferramentas essenciais como Whirlpool ou Mempool, RoninDojo poderia ser a solução ideal. Enquanto Umbrel tende a se tornar um mini servidor multitarefa orientado para a Rede Lightning e versatilidade, RoninDojo, em linha com a filosofia da Samourai Wallet, foca em ferramentas fundamentais para a privacidade do usuário.

Agora que delineamos o RoninDojo, vamos ver juntos como configurar este nó.

## Que hardware escolher para instalar o RoninDojo v2?
RoninDojo oferece uma imagem para instalação automática de seu software em um [RockPro64](https://ronindojo.io/en/download). No entanto, nosso tutorial foca no procedimento de instalação manual em um Raspberry Pi 4. Embora o Raspberry Pi 5 tenha sido lançado recentemente, e este tutorial deveria teoricamente ser compatível com este novo modelo, eu ainda não tive a chance de testá-lo pessoalmente, e não encontrei feedback da comunidade. Assim que eu adquirir o Pi 5 e componentes compatíveis, atualizarei este tutorial para mantê-los informados. Enquanto isso, recomendo priorizar o Pi 4, pois funciona perfeitamente para o meu nó.
Por minha parte, eu rodo o RoninDojo em um Raspberry Pi equipado com 8 GB de RAM. Embora alguns membros da comunidade tenham conseguido fazê-lo funcionar em dispositivos com apenas 4 GB de RAM, eu não testei esta configuração pessoalmente. Dada a pequena diferença de preço, parece sensato optar pela versão de 8 GB de RAM. Isso também pode se provar útil se você planeja reutilizar seu Raspberry Pi para outros usos no futuro.
É importante notar que as equipes do RoninDojo relataram problemas frequentes relacionados ao case e ao adaptador SSD. Eu enfrentei esses problemas pessoalmente. **Portanto, é altamente recomendado evitar cases equipados com um cabo USB para o SSD do seu nó.** Em vez disso, prefira um cartão de expansão de armazenamento especificamente projetado para o seu Raspberry Pi:

![cartão de expansão de armazenamento RPI4](assets/notext/1.webp)

Para armazenar o blockchain do Bitcoin, você precisará de um SSD compatível com o cartão de expansão de armazenamento que você escolheu. Atualmente (Fevereiro de 2024), estamos em uma fase de transição. Espera-se que, em alguns meses, discos de 1 TB não sejam mais suficientes para conter o tamanho crescente do blockchain, especialmente considerando as várias aplicações que você planeja integrar ao seu nó. Alguns, portanto, recomendam investir em um SSD de 2 TB para tranquilidade a longo prazo. No entanto, com a tendência de queda nos preços dos SSDs ano após ano, outros sugerem se contentar com um disco de 1 TB, que deve ser suficiente por um ou dois anos, argumentando que, quando se tornar obsoleto, o custo dos modelos de 2 TB provavelmente terá diminuído. A escolha, portanto, depende das suas preferências pessoais. Se você planeja manter seu RoninDojo por uma duração significativa e deseja evitar qualquer manuseio técnico nos próximos anos, a opção de um SSD de 2 TB parece ser a mais prudente, pois oferece uma margem confortável para o futuro.

Além disso, você precisará de vários pequenos componentes:
- Um gabinete equipado com um ventilador para acomodar seu Raspberry Pi e seu cartão de expansão de armazenamento. Kits que incluem tanto o cartão de expansão SSD quanto um gabinete compatível estão disponíveis online;
- Um cabo de alimentação para o seu Raspberry Pi;
- Um cartão micro SD de pelo menos 16 GB (embora 8 GB tecnicamente possam ser suficientes, a diferença de preço entre cartões de 8 e 16 GB é frequentemente insignificante);
- Um cabo Ethernet RJ45 para conexão de rede.

![node material](assets/notext/2.webp)

## Como montar o Raspberry Pi 4?
A montagem do seu nó variará dependendo do hardware escolhido, especialmente o tipo de gabinete. No entanto, o esboço geral dos passos a seguir permanece geralmente similar na montagem.
Comece instalando seu SSD no cartão de expansão de armazenamento, tomando cuidado para fixar os dois parafusos de travamento na parte de trás.

![assembly1](assets/notext/3.webp)

Em seguida, prenda seu Raspberry Pi ao cartão de expansão.

![assembly2](assets/notext/4.webp)

Também, prenda o ventilador ao Raspberry Pi.

![assembly3](assets/notext/5.webp)

Conecte os vários componentes, prestando atenção para usar os pinos corretos, referindo-se ao manual do seu gabinete. Os fabricantes de gabinete frequentemente oferecem tutoriais em vídeo para ajudá-lo na montagem. No meu caso, tenho um cartão de expansão adicional equipado com um botão de ligar/desligar. Isso não é essencial para fazer um nó Bitcoin. Eu o uso principalmente para ter um botão de energia.

Se, como eu, você tem um cartão de expansão equipado com um botão de ligar/desligar, não se esqueça de instalar o pequeno jumper "Auto Power On". Isso permitirá que seu nó inicie automaticamente assim que for alimentado. Esta característica é particularmente útil no caso de uma queda de energia, pois permite que seu nó reinicie por si mesmo, sem intervenção manual da sua parte.

![assembly4](assets/notext/6.webp)

Antes de inserir todo o hardware no gabinete, é importante verificar o funcionamento adequado do seu Raspberry Pi, do cartão de expansão de armazenamento e do ventilador, ligando-os.

![assembly5](assets/notext/7.webp)

Finalmente, instale seu Raspberry Pi em seu gabinete. Esteja ciente, um passo posterior exigirá a adição do cartão micro SD no porto apropriado no Raspberry Pi. Se o seu gabinete estiver equipado com uma abertura que permite inserir o cartão SD sem ter que abri-lo (como é o caso do meu ilustrado na foto), você pode proceder para fechar o gabinete agora. No entanto, se o seu gabinete não tem acesso direto ao porto micro SD, você precisará esperar até ter preparado o cartão micro SD para inseri-lo antes de finalizar a montagem.

![assembly6](assets/notext/8.webp)

## Como instalar o RoninDojo v2 em um Raspberry Pi 4?

### Etapa 1: Prepare o micro SD inicializável
Após montar seu hardware, o próximo passo é instalar o RoninDojo. Para isso, vamos preparar um cartão micro SD inicializável a partir do seu computador, gravando a imagem de disco apropriada nele.
Você precisará usar o software _**Raspberry Pi Imager**_, projetado para facilitar o download, a configuração e a gravação de sistemas operacionais em um cartão micro SD para uso com um Raspberry Pi. Comece instalando este software no seu PC pessoal:
- Para Ubuntu/Debian: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Para Windows: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Para Mac: https://downloads.raspberrypi.org/imager/imager_latest.dmg
Uma vez que o software esteja instalado, abra-o e insira o seu cartão micro SD no seu computador pessoal. Na interface do Raspberry Pi Imager, selecione `CHOOSE OS`:
![choose OS](assets/notext/9.webp)

Em seguida, vá para o menu `Raspberry Pi OS (other)`:

![choose OS others](assets/notext/10.webp)

Escolha o sistema operacional chamado `Raspberry Pi OS (Legacy, 64-bit) Lite`, que tem `0.3 GB` de tamanho:

![choose OS Legacy Lite](assets/notext/11.webp)

Após selecionar o sistema operacional, você será redirecionado para o menu principal do Raspberry Pi Imager. Clique em `CHOOSE STORAGE`:

![choose storage](assets/notext/12.webp)

Selecione o seu cartão micro SD:

![choose micro sd](assets/notext/13.webp)

Depois de escolher o sistema operacional e o cartão micro SD, clique em `NEXT`:

![choose next](assets/notext/14.webp)

Uma nova janela aparecerá. Selecione `EDIT CONFIGURATION`:

![edit settings](assets/notext/15.webp)

Nesta janela, vá para a aba `GENERAL` e faça as seguintes configurações (que são muito importantes para que funcione):
- Ative a opção e atribua `RoninDojo` como o nome do host;
- Ative `Set username and password`, insira `pi` como o nome de usuário, escolha uma senha e anote essas informações, pois serão necessárias mais tarde. Essas credenciais são temporárias e serão excluídas posteriormente;
- Desative `Configure Wi-Fi`;
- Ative `Set locale settings` e selecione seu fuso horário, bem como o tipo de teclado correspondente ao seu computador;

![general settings](assets/notext/16.webp)

Na aba SERVICES, clique na caixa `Enable SSH` e selecione `Use a password for authentication`:

![services settings](assets/notext/17.webp)

Além disso, certifique-se de que na aba `OPTIONS`, a telemetria esteja desativada:

![options settings](assets/notext/18.webp)

Clique em `SAVE`:

![settings save](assets/notext/19.webp)
Confirme clicando em `YES` para começar a criar o cartão micro SD inicializável:
![settings yes](assets/notext/20.webp)

Uma mensagem informará que todos os dados no cartão micro SD serão apagados. Confirme clicando em `YES` para iniciar o processo:

![overwrite micro SD](assets/notext/21.webp)

Aguarde até que o software termine de preparar o seu cartão micro SD:

![writing micro SD](assets/notext/22.webp)

Quando a mensagem indicando o fim do processo aparecer, você pode remover o cartão micro SD do seu computador:

![writing micro SD completed](assets/notext/23.webp)

### Etapa 2: Complete a Montagem do Nó
Agora você pode inserir o cartão micro SD na porta apropriada do seu Raspberry Pi.

![micro SD](assets/notext/24.webp)

Em seguida, conecte o seu Raspberry Pi ao seu roteador usando o cabo Ethernet. Finalmente, ligue o seu nó conectando o cabo de energia e pressionando o botão de energia (se o seu setup incluir um).

### Etapa 3: Estabeleça uma Conexão SSH com o Nó
Primeiro, é necessário encontrar o endereço IP do seu nó. Você tem a opção de usar uma ferramenta como _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ ou _[Angry IP Scanner](https://angryip.org/)_, ou verificar a interface de administração do seu roteador. O endereço IP deve estar no formato `192.168.1.??`. **Para todos os comandos seguintes, substitua `[IP]` pelo endereço IP real do seu nó**, (removendo os colchetes).

Abra um terminal.
Para remover uma possível chave já associada ao endereço IP do seu nó, execute o comando: `ssh-keygen -R [IP]`.

Um erro após este comando não é grave; simplesmente significa que a chave não existe na sua lista de hosts conhecidos (o que é bastante provável). Por exemplo, se o IP do seu nó for `192.168.1.40`, o comando se torna: `ssh-keygen -R 192.168.1.40`.

Em seguida, estabeleça uma conexão SSH com o seu nó executando o comando:
`ssh pi@[IP]`.
Uma mensagem aparecerá sobre a autenticidade do host: `The authenticity of host '[IP]' can't be established.` Isso indica que a autenticidade do dispositivo ao qual você está tentando se conectar não pode ser verificada devido à falta de uma chave pública conhecida. Ao se conectar via SSH a um novo host pela primeira vez, essa mensagem sempre aparecerá. Você deve responder `yes` para adicionar sua chave pública ao seu diretório local, o que evitará que essa mensagem de aviso apareça durante futuras conexões SSH a este nó. Portanto, digite `yes` e pressione `enter` para validar.
Você será então solicitado a inserir sua senha, aquela previamente definida como temporária na etapa 1. Valide com `enter`. Você estará então conectado ao seu nó via SSH.

Em resumo, aqui estão os comandos a serem executados:
- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `yes`
- Insira a senha temporária e valide.

### Etapa 4: Atualização e Preparação
Você está agora conectado ao seu nó via uma sessão SSH. No seu terminal, o prompt de comando deve ser: `pi@RoninDojo:~ $`. Para começar, atualize a lista de pacotes disponíveis e instale atualizações para os pacotes existentes com o seguinte comando:
`sudo apt update && sudo apt upgrade -y`

Uma vez que as atualizações estejam completas, prossiga para instalar *Git* e *Dialog* usando o comando:
`sudo apt install git dialog -y`

Em seguida, clone a branch `master` do repositório Git do _RoninOS_ executando:
`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`

Execute o script `customize-image.sh` com o comando:
`cd /opt/RoninOS/ && sudo ./customize-image.sh`

**É importante deixar o script rodar sem interrupção e esperar pacientemente pelo fim do seu processo**, o que leva cerca de 10 minutos. Quando a mensagem `Setup is complete` aparecer, você pode passar para a próxima etapa.

### Etapa 5: Lançando o RoninOS
Lance o RoninOS com o comando:
`sudo systemctl start ronin-setup`

Exiba as linhas do arquivo de log com o comando:
`tail -f /home/ronindojo/.logs/setup.logs`

Nesta etapa, **é importante deixar o RoninOS ser lançado e esperar por ele** até terminar de rodar. Isso leva cerca de 40 minutos. Quando `All RoninDojo feature installations complete!` aparecer, você pode prosseguir para a etapa 6.

### Etapa 6: Acessando RoninUI e Alterando Credenciais
Após completar a instalação, para se conectar ao seu nó via um navegador, certifique-se de que seu computador pessoal está conectado à mesma rede local que o seu nó. Se você estiver usando uma VPN na sua máquina, desative-a temporariamente. Para acessar a interface do nó no seu navegador, insira na barra de URL:
- Diretamente o endereço IP do seu nó, por exemplo, `192.168.1.??`;
- Ou, digite `ronindojo.local`.
Uma vez na página inicial do RoninUI, será solicitado que você inicie a configuração. Para fazer isso, clique no botão `Vamos começar`.

![vamos começar](assets/notext/25.webp)

Nesta etapa, o RoninUI apresenta a você sua senha `root`. É essencial mantê-la segura. Você pode optar por um backup físico, em papel, ou salvar em um [gerenciador de senhas](https://planb.network/courses/secu101/4/2).

![senha root](assets/notext/26.webp)

Após salvar a senha `root`, marque a caixa `Eu fiz backup das credenciais do usuário Root` e clique em `Continuar` para prosseguir.

![confirmar senha root](assets/notext/27.webp)

O próximo passo envolve a criação de uma senha de usuário, que será usada tanto para acessar a interface web do RoninUI quanto para estabelecer sessões SSH com seu nó. Escolha uma senha forte e certifique-se de salvá-la de forma segura. Você precisará inserir essa senha duas vezes antes de clicar em `Concluir` para validar. Quanto ao nome de usuário, é recomendado manter a escolha padrão, `ronindojo`. Se decidir alterá-lo, lembre-se de ajustar os comandos nos passos seguintes de acordo.

![credenciais do usuário](assets/notext/28.webp)

Uma vez que estas ações estejam completas, aguarde a inicialização do seu nó. Você então acessará a interface web do RoninUI. Você está quase no final do processo, apenas alguns pequenos passos restantes!
![Ronin UI](assets/notext/29.webp)

### Etapa 7: Remover Credenciais Temporárias
Abra um novo terminal no seu computador pessoal e estabeleça uma conexão SSH com seu nó usando o seguinte comando:
`SSH ronindojo@[IP]`

Se, por exemplo, o endereço IP do seu nó for `192.168.1.40`, o comando apropriado será:
`SSH ronindojo@192.168.1.40`

Se você alterou seu nome de usuário durante a etapa anterior, substituindo o nome de usuário padrão (`ronindojo`) por outro, certifique-se de usar este novo nome no comando. Por exemplo, se você escolheu `planb` como o nome de usuário e o endereço IP é `192.168.1.40`, o comando a ser inserido será:
`SSH planb@192.168.1.40`
Será solicitado que você insira a senha do usuário. Digite-a e então pressione `enter` para validar. Você então acessará a interface RoninCLI. Use as setas do teclado para navegar até a opção `Sair do RoninDojo` e pressione `enter` para selecioná-la.
![RoninCLI](assets/notext/30.webp)

Neste ponto, você está no terminal do seu nó, com um prompt de comando similar a: `ronindojo@RoninDojo:~ $`. Para remover o usuário temporário criado durante a configuração do cartão micro SD inicializável, insira o seguinte comando e pressione `enter`:
`sudo deluser --remove-home pi`

Será solicitado que você confirme sua senha de usuário. Insira-a e valide pressionando `enter`. Aguarde a conclusão da operação, depois use o comando `exit` para sair do terminal.
Parabéns! Seu nó RoninDojo v2 está agora configurado e pronto para uso. Ele iniciará seu IBD (*Initial Block Download*), procedendo para baixar e verificar a blockchain do Bitcoin desde o bloco Gênesis. Esta etapa envolve recuperar todas as transações de Bitcoin feitas desde 3 de janeiro de 2009 e leva algum tempo. Uma vez que a blockchain esteja totalmente baixada, o indexador prosseguirá para comprimir o banco de dados. A duração do IBD pode variar consideravelmente. Seu nó RoninDojo estará totalmente operacional uma vez que este processo seja concluído.
**Se você está migrando de um antigo nó RoninDojo v1** para esta nova versão com este tutorial enquanto mantém o mesmo SSD, seu nó deve detectar automaticamente e reutilizar os dados existentes no disco, poupando-lhe a necessidade de realizar o IBD novamente. Neste caso, você só precisará esperar que seu nó ressincronize com os blocos mais recentes.

### Etapa 8: "veth* fix"
Se você encontrar um bug com seu RoninDojo v2 no Raspberry Pi, onde após uma instalação sem problemas, seu nó de repente se torna inacessível via SSH, mas se recupera após um simples reinício, então você precisa seguir esta etapa 8. Esse bug comum pode ser facilmente corrigido com uma solução desenvolvida pela comunidade: o "_veth fix_". Essa pequena correção resolve definitivamente as desconexões abruptas. Aqui está como aplicá-la.

Abra um novo terminal no seu computador pessoal e estabeleça uma conexão SSH com seu nó usando o seguinte comando: 
`SSH ronindojo@[IP]`

Se, por exemplo, o endereço IP do seu nó for `192.168.1.40`, o comando apropriado seria: 
`SSH ronindojo@192.168.1.40`

Será solicitado que você insira a senha do usuário. Digite-a e pressione `enter` para validar. Você então acessará a interface RoninCLI. Use as setas do seu teclado para navegar até a opção `Exit RoninDojo` e pressione `enter` para selecioná-la.

Neste ponto, você está no terminal do seu nó, com um prompt de comando semelhante a: `ronindojo@RoninDojo:~ $`. Para aplicar o veth* fix, digite o seguinte comando e pressione `enter`: 
`sudo nano /etc/dhcpcd.conf`

Confirme sua senha novamente e pressione `enter`.

Você chegará ao arquivo `dhcpcd.conf`. Você precisa copiar o texto seguinte, garantindo incluir o asterisco, e adicioná-lo no final do arquivo: 
`denyinterfaces veth*`

Para fazer isso, mova-se para o final do arquivo usando a seta para baixo do seu teclado, em seguida, use o clique direito do seu mouse para colar o texto em uma linha independente.

Após adicionar o texto, pressione `ctrl X` para começar a sair, seguido por `ctrl Y` para confirmar a gravação das modificações, e pressione `enter` para finalizar e retornar ao prompt de comando. Para garantir que a modificação foi aplicada corretamente, reabra o arquivo `dhcpcd.conf` usando o comando apropriado.

Para completar a aplicação da correção, reinicie seu nó executando: 
`sudo reboot now`

Neste ponto, você pode fechar seu terminal. Permita o tempo necessário para o reinício do seu RoninDojo, após o qual você deve ser capaz de se reconectar via interface gráfica do seu navegador. Este processo deve corrigir o bug encontrado.

## Como usar seu nó RoninDojo v2?

### Conectando seu software de carteira ao Electrs
O primeiro uso do seu nó recém-instalado e sincronizado será transmitir suas transações para a rede Bitcoin. Você provavelmente vai querer conectar suas diversas carteiras ao seu nó para transmitir suas transações de forma confidencial. Você pode fazer isso através do Electrum Rust Server (electrs). Esta aplicação geralmente já vem pré-instalada no seu nó RoninDojo. Caso contrário, você poderia instalá-la manualmente via interface RoninCLI em `Aplicações > Gerenciar Aplicações > Instalar Electrum Server`.

Para obter o endereço Tor do seu Electrum Server, a partir da interface web RoninUI, vá para:
`Emparelhamento > Servidor Electrum > Emparelhar agora`
![Emparelhamento](assets/notext/31.webp)
![Electrs](assets/notext/32.webp)
Você então precisará inserir o endereço `Hostname` terminando em `.onion` no seu software de carteira, acompanhado pela porta `50001`. ![hostname](assets/notext/33.webp)
Por exemplo, no Sparrow Wallet, basta ir à aba:
`Arquivo > Preferências > Servidor > Electrum Privado`

![Sparrow](assets/notext/34.webp)

### Conectando seu software de carteira ao Samourai Dojo
Como alternativa ao uso do Electrs, o Dojo permite que você conecte seu software de carteira compatível diretamente ao seu nó RoninDojo. Carteiras como Samourai Wallet e Sentinel oferecem essa funcionalidade.

Para estabelecer a conexão, você só precisará escanear o código QR do seu Dojo. Para acessar este código QR via RoninUI, navegue até:
`Emparelhamento > Samourai Dojo > Emparelhar agora`
![Samourai Dojo](assets/notext/35.webp)
Para vincular sua Samourai Wallet ao seu Dojo, basta escanear este código QR durante a instalação do aplicativo:

![Conexão Samourai Wallet](assets/notext/36.webp)
Se você já tinha uma Carteira Samourai antes de configurar seu Ronin Dojo, é necessário fazer backup da sua carteira, desinstalar e, em seguida, reinstalar o aplicativo Samourai Wallet, antes de restaurar sua carteira. Ao iniciar o aplicativo reinstalado, você terá a opção de se conectar a um novo Dojo. **Tenha cuidado, este processo carrega o risco de perder seus bitcoins se não for executado corretamente!** Certifique-se de ter o backup da sua Carteira Samourai em seus arquivos e verifique a validade da sua frase-senha através de `Configurações > Solução de Problemas > Frase-senha`. Também é importante ter um backup legível da sua frase de recuperação e da sua frase-senha. Para mais precisão nesta operação, recomenda-se seguir este tutorial detalhado: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).

### Usando seu próprio explorador de blocos Mempool.space
Um explorador de blocos transforma as informações brutas da blockchain do Bitcoin em um formato estruturado e facilmente legível. Com ferramentas como *Mempool.space*, é possível analisar transações, buscar endereços específicos ou até consultar as taxas médias de rede dos mempools em tempo real.

No entanto, usar exploradores de blocos online apresenta riscos à sua privacidade e envolve confiança nos dados fornecidos por terceiros. De fato, ao usar esses serviços sem passar pelo seu próprio nó, você pode inadvertidamente divulgar informações sobre suas transações e deve confiar na precisão das informações apresentadas pelo proprietário do site.
Para mitigar esses riscos, recomenda-se usar sua própria instância do *Mempool.space* via rede Tor, hospedada diretamente no seu nó. Esta solução garante a preservação da sua privacidade e a autonomia dos seus dados.
Para fazer isso, comece instalando o *Mempool Space Visualizer* a partir do RoninUI. Na interface web, vá para a aba `Dashboard` e clique em `Gerenciar` abaixo de `Mempool Space`:
`Dashboard > Mempool Space > Gerenciar`
![Gerenciar mempool](assets/notext/37.webp)
Em seguida, clique no botão `Instalar visualizador Mempool`:
![instalar mempool](assets/notext/38.webp)
Confirme sua senha de usuário:
![senha mempool](assets/notext/39.webp)
Aguarde a conclusão da instalação e clique novamente no botão `Gerenciar`:
![Gerenciar Mempool](assets/notext/40.webp)
Você obterá um link `.onion` para acessar sua própria instância do *Mempool.space* via rede Tor.
![Link Mempool](assets/notext/41.webp)
Aconselho que você salve este link nos seus favoritos no navegador Tor ou adicione-o ao aplicativo Tor Browser no seu smartphone para acesso fácil e seguro de qualquer lugar. Se você ainda não tem o navegador Tor, pode baixá-lo aqui: [https://www.torproject.org/download/](https://www.torproject.org/download/)
![Mempool Tor](assets/notext/42.webp)

### Usando Whirlpool para misturar seus bitcoins
Seu nó RoninDojo também integra o _WhirlpoolCLI_, uma interface de linha de comando que possibilita a automação de coinjoins do Whirlpool, e o _WhirlpoolGUI_, uma interface gráfica projetada para interagir com o _WhirlpoolCLI_.
Realizar um coinjoin via Whirlpool exige que a aplicação utilizada esteja ativa para realizar remixagens. Esta condição pode ser restritiva para aqueles que desejam alcançar altos níveis de anonimato. De fato, o dispositivo que hospeda a aplicação integrando o Whirlpool deve permanecer ligado continuamente. Isso significa que para participar de remixagens 24 horas por dia, seu computador ou smartphone deve permanecer ligado com o Samourai ou Sparrow aberto continuamente. Uma solução para esta restrição é usar o _WhirlpoolCLI_ em uma máquina que esteja sempre ligada, como um nó Bitcoin, permitindo que suas moedas sejam remixadas sem interrupção, e sem a necessidade de manter outro dispositivo ligado.
Um tutorial detalhado está sendo preparado para guiá-lo passo a passo pelo processo de coinjoining com a Samourai Wallet e RoninDojo v2, de A a Z.

Para um entendimento mais profundo sobre coinjoin e seu uso no Bitcoin, também convido você a consultar este outro artigo: Entendendo e usando coinjoin no Bitcoin, onde detalho tudo o que você precisa saber sobre esta técnica.

https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2
### Usando a Ferramenta Whirlpool Stat Tool (WST)

Após realizar coinjoins com o Whirlpool, é útil avaliar precisamente o nível de privacidade alcançado para seus UTXOs misturados. Para fazer isso, você pode usar a ferramenta Python *Whirlpool Stat Tool*. Esta ferramenta permite medir tanto os escores prospectivos quanto retrospectivos dos seus UTXOs, enquanto analisa a taxa de difusão deles na piscina.

Para aprofundar seu entendimento sobre os mecanismos de cálculo desses anonsets, recomendo a leitura do artigo: REMIX - WHIRLPOOL, que detalha o funcionamento desses índices.

https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



Para acessar a ferramenta WST, vá para RoninCLI. Para fazer isso, abra um terminal no seu computador pessoal e estabeleça uma conexão SSH com seu nó usando o seguinte comando:
`SSH ronindojo@[IP]`

Se, por exemplo, o endereço IP do seu nó for `192.168.1.40`, o comando apropriado seria:
`SSH ronindojo@192.168.1.40`

Se você alterou seu nome de usuário durante a etapa 6, substituindo o nome de usuário padrão (`ronindojo`) por outro, certifique-se de usar este novo nome no comando. Por exemplo, se você escolheu `planb` como seu nome de usuário e o endereço IP é `192.168.1.40`, o comando a ser inserido seria:
`SSH planb@192.168.1.40`

Será solicitado que você insira a senha do usuário. Digite-a e pressione `enter` para validar. Você então acessará a interface do RoninCLI. Use as setas do teclado para navegar até o menu `Samourai Toolkit` e pressione `enter` para selecioná-lo:

![Samourai Toolkit](assets/notext/43.webp)

Em seguida, selecione `Whirlpool Stat Tool`:

![WST](assets/notext/44.webp)

Ao inicializar o WST, a ferramenta procederá com sua instalação automática. Aguarde durante esta etapa. As instruções de uso serão exibidas. Uma vez que a instalação esteja concluída, pressione qualquer tecla para acessar o terminal do WST:

![Comandos WST](assets/notext/45.webp)

O seguinte prompt de comando será exibido:
`wst#/tmp>`

Se você desejar sair desta interface e retornar ao menu RoninCLI, simplesmente digite:
`quit`

Primeiro, é necessário configurar o proxy para usar o Tor, para garantir confidencialidade ao extrair dados de OXT. Digite o comando:
`socks5 127.0.0.1:9050`
Posteriormente, prossiga para baixar as informações do pool contendo sua transação:
`download 0001`
Substitua `0001` pelo código de denominação do pool de seu interesse. Os códigos de denominação são os seguintes no WST:
- Pool 0.5 bitcoins: `05`
- Pool 0.05 bitcoins: `005`
- Pool 0.01 bitcoins: `001`
- Pool 0.001 bitcoins: `0001`

Após o download, carregue os dados substituindo `0001` pelo código do seu pool neste comando: `load 0001`

![WST loading](assets/notext/46.webp)

Aguarde a conclusão do carregamento, o que pode levar alguns minutos. Uma vez que os dados estejam carregados, para saber os scores de anonset da sua moeda, execute o comando `score` seguido pelo seu TXID (sem os colchetes):
`score [TXID]`

![WST score](assets/notext/47.webp)

O WST então exibirá o score retrospectivo (_Métricas retrospectivas_), seguido pelo score prospectivo (_Métricas prospectivas_). Além dos scores de anonset, o WST também indicará a taxa de difusão da sua transação dentro do pool, relativa ao seu anonset.

**É importante notar que o score prospectivo da sua moeda deve ser calculado a partir do TXID da sua mistura inicial, e não da sua mistura mais recente. Por outro lado, o score retrospectivo de um UTXO é calculado a partir do TXID do último ciclo.**

### Usando o Calculador Boltzmann
O Calculador Boltzmann é uma ferramenta para analisar uma transação Bitcoin, oferecendo a capacidade de medir seu nível de entropia entre outras métricas avançadas. Esses dados fornecem uma avaliação quantificada da privacidade de uma transação e ajudam a identificar potenciais falhas. Esta ferramenta já está integrada ao seu nó RoninDojo, facilitando o acesso e o uso.

Antes de detalhar o procedimento para usar o Calculador Boltzmann, é importante entender o significado desses indicadores, seu método de cálculo e sua utilidade. Embora aplicáveis a qualquer transação Bitcoin, esses indicadores são particularmente úteis para avaliar a qualidade de uma transação coinjoin.

**O primeiro indicador** que o software calcula é o número total de combinações possíveis, indicado sob `nb combinations` na ferramenta. Com base nos valores dos UTXOs envolvidos, este indicador quantifica o número de maneiras pelas quais as entradas podem ser associadas às saídas. Em outras palavras, determina o número de interpretações plausíveis que uma transação pode gerar. Por exemplo, um coinjoin estruturado de acordo com o modelo Whirlpool 5x5 apresenta `1496` combinações possíveis:
![combinations](assets/notext/50.webp)
Crédito: KYCP

**O segundo indicador** calculado é a entropia de uma transação, designada por `Entropy`. Quando uma transação tem um alto número de combinações possíveis, é frequentemente mais relevante referir-se à sua entropia. Isso é definido como o logaritmo binário do número de combinações possíveis. Aqui está a fórmula usada:
- $E$: a entropia da transação;
- $C$: o número de combinações possíveis para a transação.
$$E = \log_2(C)$$
Em matemática, o logaritmo binário (logaritmo na base 2) corresponde à operação inversa de elevar 2 a uma potência. Em outras palavras, o logaritmo binário de $x$ é o expoente ao qual 2 deve ser elevado para obter $x$. Portanto, esse indicador é expresso em bits. Vamos tomar o exemplo do cálculo da entropia para uma transação coinjoin estruturada de acordo com o modelo Whirlpool 5x5, que, como mencionado anteriormente, oferece um número de combinações possíveis de `1496`:$$ C = 1496 $$
$$ E = \log_2(1496) $$
$$ E \approx 10.5469 \text{ bits}$$

Assim, essa transação coinjoin exibe uma entropia de 10.5469 bits, o que é considerado muito satisfatório. Quanto maior esse valor, mais diferentes interpretações a transação admite, aumentando assim seu nível de privacidade.

Vamos tomar um exemplo adicional com uma transação mais convencional, apresentando uma entrada e duas saídas: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/pt/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)
No caso desta transação, a única interpretação possível é: `(inp 0) > (Outp 0 ; Outp 1)`. Consequentemente, sua entropia é estabelecida em `0`:
$$ C = 1 $$
$$ E = \log_2(1) $$
$$ E \approx 0 \text{ bits}$$
**O terceiro indicador** fornecido pelo Calculador Boltzmann é denominado `Eficiência da Carteira`. Este indicador avalia a eficiência da transação comparando-a com a transação ótima concebível em uma configuração idêntica. Isso nos leva a discutir o conceito de entropia máxima, que corresponde à maior entropia que uma estrutura de transação específica pode teoricamente alcançar. Assim, para uma estrutura coinjoin Whirlpool 5x5, a entropia máxima é definida em `10.5469`. A eficiência da transação é então calculada confrontando essa entropia máxima com a entropia real da transação analisada. A fórmula usada é a seguinte:
- $ER$: a entropia real da transação, expressa em bits;
- $EM$: a entropia máxima possível para uma determinada estrutura de transação, também em bits;
- $Ef$: a eficiência da transação, em bits.
$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$
$$Ef = 0 \text{ bits}$$

Este indicador também é expresso como uma porcentagem, sua fórmula é então:
- $CR$: o número de combinações possíveis reais;
- $CM$: o número máximo de combinações possíveis com a mesma estrutura;
- $Ef$: a eficiência expressa como uma porcentagem.
$$Ef = \frac{CR}{CM}$$
$$Ef = \frac{1496}{1496}$$
$$Ef = 100\%$$

Uma eficiência de `100%` indica assim que a transação maximiza seu potencial de privacidade com base em sua estrutura.
**O quarto indicador**, a densidade de entropia, ou `Entropy Density`, oferece uma perspectiva sobre a entropia relativa a cada entrada ou saída da transação. Este indicador prova ser útil para avaliar e comparar a eficiência de transações de diferentes tamanhos. Para calculá-lo, basta dividir a entropia total da transação pelo número total de entradas e saídas envolvidas. Tomando o exemplo de um coinjoin Whirlpool 5x5:
- $ED$: a densidade de entropia expressa em bits;
- $E$: a entropia da transação expressa em bits;
- $T$: o número total de entradas e saídas na transação.
$$T = 5 + 5 = 10$$
$$ED = \frac{E}{T}$$
$$ED = \frac{10.5469}{10}$$
$$ED = 1.054 \text{ bits}$$
**A quinta informação** fornecida pelo Calculador Boltzmann é a tabela de probabilidades de correspondência entre entradas e saídas. Esta tabela indica, através do `Boltzmann score`, a probabilidade de que uma entrada específica esteja conectada a uma saída dada. Tomando o exemplo de um coinjoin Whirlpool, a tabela de probabilidade destacaria as chances de ligação entre cada entrada e saída, fornecendo uma medida quantitativa da ambiguidade ou previsibilidade das associações na transação:

| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Aqui, fica claro que cada entrada tem uma chance igual de estar associada a qualquer saída, o que reforça a ambiguidade e confidencialidade da transação. No entanto, no caso de uma transação simples com uma entrada e duas saídas, a situação é diferente:

| %       | Saída 0 | Saída 1 |
|---------|---------|---------|
| Entrada 0 | 100%    | 100%    |

Aqui, vemos que a probabilidade de cada saída vir da entrada 0 é de 100%. Uma probabilidade menor, portanto, traduz-se em maior confidencialidade, diluindo os vínculos diretos entre entradas e saídas.

**A sexta informação** fornecida é o número de ligações determinísticas, complementado pela razão dessas ligações. Este indicador revela quantas conexões entre as entradas e saídas na transação analisada são indiscutíveis, com uma probabilidade de 100%. A razão, por sua vez, oferece uma perspectiva sobre o peso dessas ligações determinísticas dentro do total de ligações da transação.

Por exemplo, uma transação do tipo coinjoin Whirlpool apresenta zero ligações determinísticas, e, portanto, exibe um indicador e razão de 0%. Por outro lado, em nossa segunda transação examinada (com uma entrada e duas saídas), o indicador está definido em 2 e a razão alcança 100%. Assim, um indicador nulo sinaliza excelente confidencialidade graças à ausência de ligações diretas e indiscutíveis entre entradas e saídas.
**Como acessar o Calculador Boltzmann no RoninDojo?** Para acessar a ferramenta *Calculador Boltzmann*, vá até o RoninCLI. Para fazer isso, abra um terminal no seu computador pessoal e estabeleça uma conexão SSH com seu nó usando o seguinte comando: `SSH ronindojo@[IP]`

Se, por exemplo, o endereço IP do seu nó for `192.168.1.40`, o comando apropriado seria:
`SSH ronindojo@192.168.1.40`

Se você alterou seu nome de usuário durante a etapa 6, substituindo o nome de usuário padrão (`ronindojo`) por outro, certifique-se de usar este novo nome no comando. Por exemplo, se você escolheu `planb` como seu nome de usuário e o endereço IP for `192.168.1.40`, o comando a ser inserido seria:
`SSH planb@192.168.1.40`

Será solicitado que você insira a senha do usuário. Digite-a e então pressione `enter` para validar. Você então acessará a interface do RoninCLI. Use as setas no seu teclado para navegar até o menu `Samourai Toolkit` e pressione `enter` para selecioná-lo:

![Samourai Toolkit](assets/notext/43.webp)

Em seguida, selecione `Calculador Boltzmann`:

![boltzmann](assets/notext/49.webp)

Você chegará à página inicial do software:

![página inicial boltzmann](assets/notext/51.webp)

Insira o TXID da transação que deseja estudar e pressione a tecla `enter`:

![txid boltzmann](assets/notext/52.webp)

O calculador então fornece todos os indicadores que discutimos anteriormente:

![resultado boltzmann](assets/notext/53.webp)

### Outras funcionalidades do seu RoninDojo v2
Seu nó RoninDojo integra várias outras funcionalidades. Em particular, você tem a capacidade de escanear informações específicas para levá-las em conta. Por exemplo, às vezes sua carteira Samourai, conectada ao RoninDojo, pode não exibir os bitcoins que você realmente possui. Se o saldo indicar 0 enquanto você tem certeza de ter bitcoins nesta carteira, várias razões podem explicar essa situação, como um erro nos caminhos de derivação. Mas uma das causas também pode ser que seu nó não está monitorando adequadamente seus endereços. Para resolver esse problema, você pode garantir que seu nó está de fato seguindo seu `xpub` usando a _ferramenta xpub_. Para acessar esta ferramenta via RoninUI, siga o caminho:
`Manutenção > Ferramenta XPUB`

Insira o `xpub` que está causando o problema e clique no botão `Verificar` para verificar essa informação:
![ferramenta xpub](assets/notext/54.webp)
Certifique-se de que todas as transações estão devidamente listadas. Também é importante verificar se o tipo de derivação usado corresponde ao da sua carteira. Se não for o caso, clique em `Retipar`, e então escolha entre `BIP44`, `BIP49`, ou `BIP84` de acordo com suas necessidades.
Além desta ferramenta, a aba `Manutenção` do RoninUI está cheia de outras funcionalidades úteis:
- *Ferramenta de Transação*: Permite examinar os detalhes de uma determinada transação;
- *Ferramenta de Endereço*: Permite confirmar o rastreamento de um determinado endereço pelo seu Dojo;
- *Reescanear Blocos*: Força seu nó a realizar um novo escaneamento de uma faixa de blocos especificada.

A aba `Push Tx` é outra funcionalidade interessante do RoninUI, que permite a transmissão de uma transação assinada na rede Bitcoin. A transação deve ser inserida em forma hexadecimal.

Quanto às outras abas disponíveis no seu painel RoninUI:
- `Apps`: Hospeda o aplicativo Whirlpool e certamente será usado para integrar novos aplicativos no futuro;
- `Logs`: Oferece acesso em tempo real aos registros de eventos do seu software;
- `System Info`: Fornece informações gerais sobre o seu nó, como temperatura da CPU, uso do espaço de armazenamento ou dados de RAM. Você também encontrará as opções `Reboot` e `Shut down` para reiniciar ou desligar o seu nó;
- `Settings`: Permite que você altere a senha do usuário.

Aí está! Obrigado por seguir este tutorial até o fim. Se você gostou, encorajo você a compartilhá-lo nas redes sociais. Além disso, se tiver a oportunidade, considere apoiar os desenvolvedores que disponibilizam esses softwares livres e de código aberto para nossa comunidade com uma doação: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). Para aprofundar seu conhecimento sobre o RoninDojo e descobrir mais recursos, recomendo vivamente a consulta dos links para os recursos externos mencionados abaixo.

**Recursos externos:**
- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/introducing-boltzmann-85930984a159](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)
