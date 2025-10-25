---
name: Dojo
description: Um nó Bitcoin de código aberto para privacidade e autonomia
---

![cover](assets/cover.webp)



*Este tutorial é baseado na [documentação oficial do Ashigaru] (https://ashigaru.rs/docs/), que eu assumi e expandi. Reescrevi todas as secções para melhorar a clareza, acrescentei explicações mais detalhadas, bem como ilustrações para principiantes, para tornar a instalação e a utilização mais fáceis de compreender.*



---

Dojo é um programa de código aberto concebido para atuar como um servidor backend para certas carteiras Bitcoin orientadas para a privacidade, com base num nó Bitcoin core. Historicamente, foi desenvolvido para trabalhar com o Samourai Wallet, um Wallet móvel que oferecia recursos avançados de privacidade como Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym... O Samourai Wallet foi encerrado na sequência da detenção dos seus criadores, mas o seu sucessor comunitário, **Ashigaru Wallet**, assumiu o controlo e continua a confiar no Dojo para oferecer uma experiência completa aos utilizadores que desejam manter o controlo dos seus dados quando utilizam o Bitcoin.



![Image](assets/fr/01.webp)



Em termos práticos, o Dojo actua como um gateway entre o Wallet e a rede Bitcoin. Sem o Dojo, um Wallet móvel leve teria de consultar servidores de terceiros para obter o estado dos seus UTXOs e o seu histórico, ou para transmitir as suas transacções. Isto implica a dependência e a fuga de dados sensíveis para um servidor de terceiros (endereços utilizados, montantes, frequência de pagamento, etc.). Com o Dojo, é o próprio utilizador que aloja este servidor, diretamente ligado ao seu próprio nó Bitcoin. Desta forma, todos os seus pedidos de carteira passam por uma infraestrutura que controla, sem intermediários, reforçando a sua confidencialidade e soberania.



## Requisitos para a criação de um Dojo



A configuração de um servidor Dojo não requer uma máquina ultra-poderosa. Qualquer pessoa com um computador de nível básico, uma ligação estável à Internet e a capacidade de o deixar ligado continuamente (24/7) pode configurar um Dojo funcional.



### Escolha o seu tipo de máquina



Pode utilizar :




- um computador portátil ;
- um computador de secretária ;
- um mini-PC (por exemplo, Intel NUC, Lenovo Thincentre Tiny...).



Cada opção tem as suas vantagens e desvantagens:




- Preço: um mini-PC ou um computador de secretária recondicionado é frequentemente mais barato do que um computador portátil novo.
- Espaço: um Mini-PC ocupa menos espaço.
- Power Supply: um computador portátil tem a vantagem de ter uma bateria, o que significa que não se desliga em caso de corte de energia, ao contrário de um mini-PC.
- Possibilidade de atualização: os barbones permitem geralmente adicionar memória ou substituir facilmente um disco Hard.



Para mais informações sobre como escolher o seu equipamento, recomendo que faça este curso:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Equipamento recomendado



Não é necessário comprar uma máquina nova. Um computador recondicionado com as especificações abaixo terá um desempenho muito melhor do que uma eletrónica de placa única (como o Raspberry Pi).



**Especificações mínimas




- Arquitetura X86-64 (processador de 64 bits).
- processador dual-core de 2 GHz ou mais rápido.
- 8 GB de RAM no mínimo.
- sSD NVMe de 2 TB ou mais (para armazenar Blockchain de Bitcoin e os índices necessários).



**Sistema operativo recomendado: **




- Uma distribuição baseada em Debian, como o Ubuntu 24.04 LTS.



**Equipamento recomendado




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- etc.



É perfeitamente possível executar um servidor Dojo noutras configurações de hardware. No entanto, para obter o melhor desempenho e limitar os problemas, aconselhamos a seguir as recomendações acima.



Neste tutorial, vou utilizar um ThinkCentre Tiny antigo com um processador Intel Pentium Dual-Core G4400T, 8 GB de RAM e um SSD de 2 TB.



## 1 - Instalar o Ubuntu



*Se desejar instalar o Dojo num dispositivo já configurado, pode saltar este passo e avançar diretamente para o passo 2.*



Tendo preparado o hardware escolhido, é hora de instalar um sistema operativo. Pode utilizar praticamente qualquer distribuição Debian, mas recomendo que opte por uma versão LTS do Ubuntu, uma vez que é perfeitamente adequada aos nossos objectivos. Eis os passos a seguir:



### 1.1. criar uma chave USB de arranque



A partir de um computador já em funcionamento (a sua máquina habitual), descarregue a imagem ISO do Ubuntu LTS [a partir do site oficial](https://ubuntu.com/download/desktop) (`24.04` no momento em que escrevo, mas escolha a mais recente se houver outra disponível).



![Image](assets/fr/02.webp)



Insira uma chave USB de pelo menos 8 GB neste computador e, em seguida, crie uma chave de arranque utilizando software como o [Balena Etcher] (https://etcher.balena.io/). Selecione a imagem ISO do Ubuntu que acabou de descarregar, escolha a chave USB como dispositivo de destino e, em seguida, inicie o processo de criação (seja paciente, pode demorar alguns minutos).



![Image](assets/fr/03.webp)



Insira a chave USB inicializável no computador desligado (aquele no qual deseja executar o Dojo). Inicie a máquina e imediatamente pressione **F12** ou **F10** em seu teclado (dependendo do modelo) para acessar o menu de inicialização. Em seguida, escolha sua chave USB como o dispositivo prioritário na ordem de inicialização do computador.



![Image](assets/fr/04.webp)



### 1.2. instalar o sistema operativo



Aparece o ecrã inicial do Ubuntu. Selecione "Experimentar ou instalar o Ubuntu*".



![Image](assets/fr/05.webp)



Em seguida, siga o processo clássico de instalação do Ubuntu:




- Selecionar o idioma.
- Selecionar o tipo de teclado.
- Se estiver ligado através de um cabo RJ45, não é necessário configurar o Wi-Fi.
- Clique em "*Instalar o Ubuntu*" e assinale a opção de instalar software de terceiros (controladores Wi-Fi, codecs multimédia, etc.).
- Quando o assistente pedir o tipo de instalação, selecione "*Apagar disco e instalar o Ubuntu*". **Aviso**: esta operação irá apagar completamente o conteúdo do disco. Verifique cuidadosamente se o disco que escolheu corresponde ao SSD NVMe destinado ao Dojo.
- Crie um nome de utilizador simples (por exemplo, "*loic*").
- Atribua um nome à máquina (por exemplo, "*dojo-node*").
- Defina uma palavra-passe forte e mantenha-a segura.
- Ativar a opção "*Pedir a minha palavra-passe para iniciar sessão*" para reforçar a segurança.
- Indique o seu fuso horário e, em seguida, clique em "*Instalar*".
- Aguarde a conclusão da instalação. Uma vez concluída, o sistema reiniciar-se-á automaticamente.
- Remova a chave de instalação USB quando reiniciar o computador.



Para mais pormenores sobre o processo de instalação do Ubuntu, consulte o nosso tutorial dedicado :



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. atualização do sistema



Após o primeiro arranque, abra um terminal utilizando a combinação de teclas ***Ctrl + Alt + T*** e execute os seguintes comandos para atualizar o sistema:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Instalação de um anexo



Para que o Dojo funcione corretamente, devem estar presentes no seu sistema determinados blocos de software. Estes são utilizados para gerir repositórios de software, comunicação, descompressão de arquivos e a execução do Dojo dentro de contentores Docker. Todas estas operações são efectuadas no terminal.



### 2.1. Preparação



O comando seguinte leva-o de volta à sua pasta pessoal. Esta é uma boa prática antes de executar uma série de instalações.



```bash
cd ~/
```



Antes de instalar qualquer software, certifique-se de que a base de dados do software disponível na sua máquina está actualizada. Desta forma, evita-se a instalação de versões obsoletas.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. instalar utilitários



É necessário acrescentar várias ferramentas ao sistema:




- `apt-transport-https`: permite baixar pacotes de forma segura via HTTPS
- `ca-certificates`: gere os certificados necessários para as ligações encriptadas
- `curl`: para obter ficheiros da Internet
- `gnupg-agent`: para gestão de chaves GPG
- software-properties-common`: fornece utilitários para manipular repositórios APT
- `unzip`: descompacta arquivos no formato ZIP



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Durante a instalação, o sistema pode pedir-lhe uma confirmação. Prima a tecla "*y*" e, em seguida, prima "*Enter*".



![Image](assets/fr/08.webp)



### 2.3. instalar o Torsocks



O Torsocks permite que determinados comandos sejam executados através da rede Tor, melhorando a confidencialidade das comunicações.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. instalar o Docker e o Docker Compose



O Dojo é executado dentro de contentores Docker. Isto significa que cada serviço é isolado num ambiente independente, simplificando a manutenção e a segurança. Para tal, é necessário instalar o Docker e a ferramenta Docker Compose, que lhe permite gerir vários contentores ao mesmo tempo.



#### Adicionar chave de assinatura do Docker



O Docker fornece sua própria chave de assinatura digital. A sua adição verifica a autenticidade dos pacotes descarregados.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Repositório oficial do Docker adicionado



Em seguida, é necessário informar ao sistema onde encontrar os pacotes oficiais do Docker. Este comando adiciona um novo repositório à configuração do seu gerenciador de pacotes.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Instalando o Docker e o Docker Compose



Os principais componentes do Docker podem agora ser instalados.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Autorização do utilizador



Por padrão, apenas comandos executados com direitos de administrador podem iniciar o Docker. Para maior conveniência, eu recomendo adicionar seu usuário atual ao grupo "*docker*". Isso permite que você use o Docker sem ter que digitar `sudo` todas as vezes.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Criação de um único utilizador (opcional)



Se quiser melhorar a segurança do seu sistema, recomendo que crie um utilizador separado exclusivamente para executar o Dojo. Esta separação limita os riscos: se ocorrer um problema de segurança no Dojo, este não comprometerá diretamente a sua conta principal.



### 3.1. criação de uma conta de utilizador



O comando a seguir cria um novo usuário chamado "*dojo*". Este usuário terá um diretório home `/home/dojo` e acesso ao terminal bash. Ele também será adicionado ao grupo sudo para permitir a execução de comandos administrativos.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Definir uma palavra-passe



É importante atribuir uma palavra-passe forte a esta conta. Idealmente, deve utilizar um gestor de palavras-passe, como o Bitwarden, para criar uma combinação generate longa e Hard difícil de adivinhar.



```bash
sudo passwd dojo
```



O sistema pedir-lhe-á então que introduza a palavra-passe escolhida e que a confirme uma segunda vez.



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Autorizar o utilizador a utilizar o Docker



Para permitir que o usuário "*dojo*" inicie os containers necessários para executar o Dojo, ele deve ser adicionado ao grupo Docker. Isso evita ter que preceder cada comando com `sudo`.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Reinício do sistema



Para que as alterações de grupo tenham efeito, a máquina deve ser reiniciada.



```bash
sudo reboot
```



### 3.5. Iniciar sessão com o novo utilizador



Quando o sistema reiniciar, inicie sessão com o login ***dojo*** e a palavra-passe que definiu anteriormente. Todos os passos subsequentes devem ser efectuados a partir desta conta dedicada.



## 4. Descarregar e verificar o Dojo



Antes de instalar o Dojo, é essencial certificar-se de que os ficheiros provêm do programador oficial e que não foram modificados. Este passo baseia-se na utilização de PGP e hashes para verificar a autenticidade e integridade dos ficheiros.



### 4.1. importar a chave PGP do programador



Descarregue a chave pública do programador através do Tor e importe-a para a sua cadeia de chaves local. Esta chave será utilizada para verificar as assinaturas associadas aos ficheiros Dojo.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. descarregar a versão mais recente do Dojo



Recupere o arquivo compactado que contém o código-fonte do Dojo. Neste exemplo, a versão mais recente é `1.27.0`: modifique o comando de acordo com [a última versão aqui no repositório oficial do GitHub](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Descarregar as impressões digitais e a assinatura



Os criadores publicam um ficheiro que lista as impressões digitais dos arquivos, bem como um ficheiro assinado pela sua chave PGP. Descarregue-os para comparar os seus ficheiros localmente.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Verificar a assinatura PGP



Verifique se o ficheiro de impressões digitais foi assinado pela chave importada.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Um resultado correto apresenta uma assinatura válida com a chave `E53AD419B242822F19E23C6D3033D463D6E544F6` e o Address associado `dojocoder@pm.me`. Pode aparecer um aviso informando que a chave não é certificada: pode ignorá-lo.



Se, por outro lado, a assinatura for inválida, interrompa imediatamente o processo de instalação e recomece desde o início.



![Image](assets/fr/17.webp)



### 4.5. Verificar a integridade do arquivo



Calcule a impressão digital SHA256 do ficheiro descarregado e, em seguida, abra o ficheiro de impressão digital para comparar os dois valores.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Se as duas impressões digitais forem idênticas, pode ter a certeza de que o arquivo não foi modificado. Se forem diferentes, não vá mais longe e elimine os ficheiros.



![Image](assets/fr/18.webp)



### 4.6. Extrair e organizar ficheiros



Quando a verificação tiver sido concluída com êxito, pode descompactar o arquivo e preparar uma pasta dedicada à instalação do Dojo.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Limpar ficheiros desnecessários



Elimine ficheiros temporários e arquivos que já não são necessários para manter o seu ambiente limpo.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Configuração do Dojo



O Dojo é um servidor backend que reúne vários serviços para interagir com a sua carteira e gerir o seu nó Bitcoin. A sua configuração pode ser complexa, mas o projeto oferece um método simplificado que instala e configura automaticamente os seguintes componentes:




- Dojo (API principal)
- Bitcoin core (nó Bitcoin completo)
- BTC-RPC Explorer (web Block explorer)
- Fulcrum Indexer (indexação rápida de blocos e transacções)
- Servidor Fulcrum Electrum disponível na rede Tor
- Fulcrum Electrum Server disponível na rede local
- Credenciais de administração



### 5.1. credenciais de administração



Para garantir o acesso aos vários serviços, é necessário generate vários identificadores únicos:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_PASSWORD`
- mYSQL_USER
- `MYSQL_PASSWORD`
- nODE_API_KEY`
- `CHAVE_DE_ADMINISTRADOR_DO_NODO`
- `NODE_JWT_SECRET`



Estes identificadores **devem ser únicos** (isto é muito importante: não deve utilizar a mesma palavra-passe para vários serviços), compostos apenas por números, letras maiúsculas e minúsculas (alfanuméricos), e ter cerca de 40 caracteres para garantir um elevado nível de segurança. Mais uma vez, recomendo vivamente a utilização de um gestor de palavras-passe.



### 5.2. Aceder aos ficheiros de configuração



Os arquivos de configuração do Dojo estão localizados na pasta `conf/`. Mova para este diretório:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Configuração do Bitcoin core



Abra o ficheiro de configuração do Bitcoin core com o editor de texto nano:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



Neste ficheiro, introduzir os identificadores gerados:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Substitua `seu-ID-aqui` e `sua-senha-aqui` pelos seus próprios logins (com uma senha forte).***



Também pode ajustar o tamanho da memória cache utilizada pelo Bitcoin core para melhorar o desempenho (pode até utilizar mais se tiver muita RAM disponível):



```
BITCOIND_DB_CACHE=2048
```



Para guardar as suas alterações e fechar o editor :




- premir `Ctrl + X
- tipo `y`
- e prima "*Enter*"



### 5.4. Configuração do MySQL



Em seguida, abra a configuração da base de dados MySQL:



```bash
nano docker-mysql.conf.tpl
```



Introduza os seus dados de acesso:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Substitua `seu-ID-aqui` e `sua-senha-aqui` pelos seus próprios logins (com senhas fortes e únicas)



Guardar da mesma forma (`Ctrl + X`, `y`, "*Enter*").



![Image](assets/fr/23.webp)



### 5.5. Configuração do indexador Fulcrum



Abrir o seguinte ficheiro:



```bash
nano docker-indexer.conf.tpl
```



Adicionar os parâmetros para ativar o Fulcrum e integrá-lo corretamente no Dojo :



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



De seguida, existem 2 possibilidades, dependendo da sua configuração. Se o Dojo estiver instalado numa máquina separada do seu computador diário (numa máquina dedicada, um servidor...), introduza o seu IP Address na sua rede local, por exemplo :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Para descobrir o IP local Address da sua máquina, abra outro terminal e introduza o seguinte comando:



```bash
hostname -I
```



Segunda possibilidade: se o Dojo for executado diretamente no seu computador pessoal diário, mantenha o valor predefinido já presente no ficheiro de configuração :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Guardar e sair do editor (`Ctrl + X`, `y`, "*Enter*").



### 5.6. Configuração do serviço de nó



Por fim, abra a configuração do serviço principal do Dojo:



```bash
nano docker-node.conf.tpl
```



Introduza os seus dados de acesso:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Substitua `sua-senha-aqui` pelas suas próprias credenciais (com palavras-passe fortes e únicas)



![Image](assets/fr/26.webp)



Em seguida, active o indexador local:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Guardar e sair do editor (`Ctrl + X`, `y`, "*Enter*").



### 5.7. Gestão do início de sessão



Uma vez concluída a configuração, não é necessário guardar todos os identificadores gerados. O único que deve absolutamente ser guardado é o :



```
NODE_ADMIN_KEY
```



Este início de sessão permitir-lhe-á iniciar sessão mais tarde na ferramenta de manutenção do Dojo. Todos os outros logins podem ser removidos do seu gestor de senhas ou notas manuscritas. Permanecem acessíveis a partir dos ficheiros de configuração do Dojo, caso necessite de os recuperar no futuro.



## 6. Instalação do Dojo



Nesta fase, o Dojo será instalado e iniciado na sua máquina. A operação lançará vários serviços (Bitcoin core, o indexador Fulcrum, o backend Dojo, etc.) e iniciará a sincronização completa do Blockchain Bitcoin. Isto pode demorar vários dias, dependendo do seu hardware e ligação à Internet.



### 6.1. Verificar se o Docker está a funcionar corretamente



Antes de iniciar a instalação, certifique-se de que o Docker está operacional. Execute o seguinte comando:



```bash
docker run hello-world
```



Este comando descarrega e lança um pequeno contentor de teste. Se tudo funcionar corretamente, deverá ver uma mensagem semelhante a :



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Se esta mensagem não for apresentada, comece por reiniciar a sua máquina com :



```bash
sudo reboot
```



Em seguida, faça login novamente em sua conta **dojo** e execute o comando de teste novamente. Se o erro persistir, o Docker não foi instalado corretamente. Neste caso, volte para a etapa `2.4.` sobre a instalação do Docker e verifique cada comando cuidadosamente.



### 6.2. Aceder ao diretório de instalação do Dojo



Os scripts necessários para a instalação estão localizados na pasta `my-dojo`. Mova para este diretório:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Utilize o comando `ls` para verificar se o arquivo `dojo.sh` está presente. Este é o script principal que automatiza a instalação do Dojo e o lançamento de todos os seus serviços.



![Image](assets/fr/29.webp)



### 6.3. Iniciar a instalação



Inicie a instalação executando o ficheiro :



```bash
./dojo.sh install
```



Confirmar a instalação premindo "y" e depois "*Enter*".



![Image](assets/fr/30.webp)



Este script irá :




- descarregar e iniciar os contentores Docker necessários,
- inicializar o Bitcoin core e iniciar a sincronização do Blockchain,
- iniciar o indexador Fulcrum para rastrear transacções e endereços,
- ativar o backend Dojo e as suas APIs.



Você verá um fluxo constante de logs rolando, com referências coloridas como `bitcoind`, `soroban`, `nodejs` ou `fulcrum`. Essa rolagem indica que o Dojo está funcionando e começando a executar os vários serviços.



![Image](assets/fr/31.webp)



### 6.4. Sair do ecrã de registo



Os logs aparecem em tempo real no seu terminal. Para retornar ao prompt de comando enquanto o Dojo está sendo executado em segundo plano, digite :



```
Ctrl + C
```



Não se preocupe: parar a exibição do log não interrompe os serviços. O Docker continua a executar o Dojo em segundo plano (obviamente não é necessário parar o computador se quiser que o IBD continue).



### 6.5. Compreender a *transferência inicial de blocos* (IBD)



No arranque, o Bitcoin core tem de descarregar e verificar todo o Blockchain desde 2009. Esta etapa é chamada de ***Initial Block Download* (IBD)**. É essencial, pois permite que seu nó Dojo verifique cada bloco e transação do Bitcoin de forma independente.



A duração desta sincronização depende de vários factores:




- a potência do seu processador e a quantidade de memória RAM disponível,
- a velocidade do seu disco,
- o número e a qualidade dos pares a que o nó se liga,
- a velocidade da sua ligação à Internet.



Na prática, esta operação demora geralmente entre **2 e 7 dias**. Durante este período, pode deixar a sua máquina em funcionamento contínuo. Quanto mais tempo a máquina estiver ligada, mais rapidamente a sincronização será concluída. Aconselho-o a verificar regularmente o estado da sincronização consultando os registos do Bitcoin core ou utilizando a ferramenta de manutenção do Dojo depois de instalada (ver secção seguinte).



Para aprofundar os seus conhecimentos sobre o IBD e, de uma forma mais geral, sobre o funcionamento e o papel do seu nó Bitcoin, recomendo que dê uma vista de olhos a este curso:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Monitorização da sincronização



Ao instalar o Dojo pela primeira vez, é necessário aguardar que duas operações principais sejam totalmente concluídas: a transferência completa do Blockchain Bitcoin (*IBD*) e a indexação deste Blockchain pela Fulcrum. Dependendo da sua ligação e da potência da máquina, isto pode demorar vários dias. Durante este tempo, pode acompanhar o progresso do processo para se certificar de que tudo está a correr bem.



Existem duas formas de monitorizar o estado da sincronização:




- utilização da ferramenta de manutenção do Dojo (ou DMT), que é simples mas fornece poucos pormenores durante o IBD;
- consulta direta dos registos do Dojo na sua máquina, mais técnica mas muito mais precisa.



### 7.1. Verificar através da Ferramenta de Manutenção do Dojo (DMT)



A Ferramenta de Manutenção Dojo é um Interface seguro, baseado na web, que permite monitorizar o estado da sua fábrica e efetuar determinadas operações. É a maneira mais fácil e acessível de monitorar o progresso do IBD. Durante a fase inicial de sincronização, as informações exibidas podem ser limitadas. Por exemplo, o DMT não mostra o progresso detalhado da indexação Fulcrum. Por outro lado, quando a sincronização estiver concluída, o DMT mostrará claramente :




- todas as luzes do Green;
- o último bloco validado para cada serviço (Nó, Indexador, Dojo DB).



Para aceder a ele, é necessário conhecer o URL do seu DMT e ligar-se a ele [através do navegador Tor] (https://www.torproject.org/download/). Para fazer isso, abra um terminal e vá para o diretório `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Em seguida, execute o seguinte comando:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Terá então acesso a toda a informação relativa às ligações ao seu Dojo através do Tor. A que nos interessa aqui é a seguinte URL:



```
Dojo API and Maintenance Tool =
```



Para aceder ao DMT a partir de qualquer máquina em qualquer rede (mesmo remotamente), abra o Navegador Tor e introduza este URL seguido de `/admin`. Por exemplo, se o seu URL é `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, terá de introduzir na barra [Tor Browser](https://www.torproject.org/download/):



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Por favor, mantenha este Address estritamente confidencial



Será então redireccionado para uma página de autenticação. O DMT é autenticado utilizando a palavra-passe `NODE_ADMIN_KEY` que gerou anteriormente.



![Image](assets/fr/33.webp)



Uma vez conectado, pode aceder à *Ferramenta de Manutenção do Dojo*! Durante a IBD, pode ver a informação "*Latest Block*" no menu "*Full node*", que lhe permite saber o estado atual do seu nó Bitcoin.



![Image](assets/fr/34.webp)



Lembra-te de marcar este Address no Navegador Tor para o recuperares mais tarde.



Assim que o seu Dojo estiver totalmente sincronizado, deverá ver Green a marcar ✅ em todos os indicadores na página inicial do DMT.



### 7.2. Verificação através dos registos do Dojo



A segunda forma de acompanhar a evolução da sua IBD é consultar diretamente os registos da sua máquina. Esta abordagem oferece uma monitorização muito mais precisa e em tempo real. Pode ver como o Bitcoin core está a progredir no download de blocos e como o Fulcrum os está a indexar.



Conecte-se à máquina que hospeda seu Dojo e abra um terminal. Todos os comandos devem ser executados a partir do diretório `my-dojo`. Posicione-se nesta pasta:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Registos Bitcoin core



Ver os registos do Bitcoin core para acompanhar o progresso do IBD:



```bash
./dojo.sh logs bitcoind
```



No início, verá uma fase de pré-sincronização dos cabeçalhos de bloco:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Quando este valor atingir 100%, o Bitcoin core iniciará o download completo do Blockchain. Você verá o progresso do IBD. Para saber a altura atual do bloco, veja o valor indicado por `height=`. Pode também seguir a chave `progress=`, que indica a percentagem de progresso do IBD.



![Image](assets/fr/36.webp)



Como sempre, para fechar os registos e voltar à linha de comandos, utilize a combinação `Ctrl + C`.



#### Registos Fulcrum



Quando o Bitcoin core tiver concluído a pré-sincronização do cabeçalho, o Fulcrum começa a indexar o Blockchain à medida que avança. Veja os seus registos com :



```bash
./dojo.sh logs fulcrum
```



Verá então a altura do último bloco indexado, indicada após `height:`, bem como a percentagem de progresso da indexação.



![Image](assets/fr/37.webp)



### 7.3. Corrupção da base de dados Fulcrum



O Fulcrum é um indexador particularmente poderoso, mas a sua instalação pode ser complexa, nomeadamente devido à sua delicada gestão da base de dados. No caso de um corte de energia ou de uma paragem súbita da máquina durante a sincronização inicial, a base de dados do indexador pode ficar corrompida. Pode ver isto, por exemplo, se tiver os seguintes registos:



```bash
fulcrum | The database has been corrupted etc...
```



**Nota:** Este tipo de erro deverá ser corrigido com a próxima versão do Fulcrum 2.0.



Se isto lhe acontecer, não há impacto no bitcoind (o seu nó Bitcoin): o seu IBD continuará a progredir independentemente da Fulcrum. No entanto, não poderá utilizar o Fulcrum até ter apagado os dados corrompidos e reiniciado a sincronização desde o início. Eis como funciona:



Parar o Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Eliminar apenas o contentor e o volume Fulcrum:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Normalmente o nome é `my-dojo_data-fulcrum`, se este não for o seu caso, adapte o nome retornado pelo comando anterior.



Em seguida, relançar o Dojo e reconstruir a Fulcrum a partir do zero:



```bash
./dojo.sh upgrade
```



Pode então verificar se o Fulcrum está a funcionar corretamente consultando os registos:



```bash
docker logs -f fulcrum
```




## 8. Utilizar a ferramenta de manutenção do Dojo



Assim que o seu nó Bitcoin estiver sincronizado com a cabeça da teia com a maioria dos Proof of Work, e o Blockchain estiver 100% indexado pela Fulcrum, pode começar a usar o seu Dojo.



O seu Dojo oferece uma vasta gama de funcionalidades, regularmente melhoradas a cada nova versão. Na minha opinião, as duas mais importantes são :




- a possibilidade de ligar o seu Ashigaru Wallet para utilizar o seu próprio nó para consultar os dados do Blockchain e transmitir as suas transacções,
- e o Block explorer, que lhe dá acesso a informações sobre o Blockchain Bitcoin sem expor os seus dados a uma instância externa que não controla.



Vamos descobrir como os utilizar.


### 8.1. Liga o Ashigaru ao teu Dojo



Ligar o seu Ashigaru Wallet ao seu Dojo é muito simples: uma vez no seu DMT, abra o menu "*Pairing*". Aparece um código QR, que pode ser lido diretamente com a aplicação Ashigaru.



![Image](assets/fr/38.webp)



Na aplicação Ashigaru, a primeira vez que a iniciar depois de criar ou restaurar o seu Wallet, será redireccionado para a página "*Configurar o seu servidor Dojo*". Prima "*Scan QR*", depois digitalize o código QR apresentado no seu DMT.



![Image](assets/fr/39.webp)



Em seguida, clique no botão "*Continuar*".



![Image](assets/fr/40.webp)



Está agora ligado ao seu Dojo.



![Image](assets/fr/41.webp)



### 8.2. Utilizar o Block explorer



O Dojo instala automaticamente um Block explorer, [BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer), que se baseia diretamente nos dados do seu próprio nó Bitcoin. Um explorador permite-lhe aceder a informação bruta do Blockchain e do seu Mempool através de uma rede Interface fácil de compreender. Assim, pode, por exemplo, verificar o estado de uma transação pendente, ver o saldo de um Address ou examinar a composição de um bloco com facilidade.



Para aceder a ele, basta obter o Tor Address a partir do seu navegador. Para o fazer, execute o mesmo comando que utilizou para obter o Address do seu DMT:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Terá acesso a toda a informação da sua ligação ao Dojo através do Tor. A que nos interessa aqui é a seguinte URL:



```
Block Explorer =
```



Se já estiver ligado ao seu DMT, pode também encontrar este Address no menu "*Pairing*", no interior do JSON de ligação:



![Image](assets/fr/43.webp)



Para aceder ao seu navegador a partir de qualquer máquina em qualquer rede (mesmo remotamente), abra o [Navegador Tor] (https://www.torproject.org/download/) e introduza o URL que acabou de obter.



⚠️ **Por favor, mantenha este Address estritamente confidencial



Terá então acesso ao seu próprio Block explorer.



![Image](assets/fr/44.webp)



*Crédito da imagem: https://ashigaru.rs/.*



Para seguir uma transação, basta introduzir o seu txid na barra de pesquisa no canto superior direito.



![Image](assets/fr/45.webp)



*Crédito da imagem: https://ashigaru.rs/.*



Para verificar os movimentos associados a um Address, proceder da mesma forma, introduzindo o Address na barra de pesquisa.



![Image](assets/fr/46.webp)



*Crédito da imagem: https://ashigaru.rs/.*



Também é possível introduzir o Hash ou a altura de um bloco na barra de pesquisa para visualizar os pormenores.



![Image](assets/fr/47.webp)



*Crédito da imagem: https://ashigaru.rs/.*



## 9. Manutenção do Dojo



### 9.1 Parar o seu Dojo



Nunca corte abruptamente a energia do seu Dojo, pois isso pode corromper certas bases de dados, particularmente o indexador Fulcrum. Se tiver de o desligar, execute sempre um encerramento limpo do Dojo e, depois de concluídos todos os procedimentos, desligue também a máquina:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Atualizar o seu Dojo



O Dojo evolui regularmente e são lançadas novas versões para corrigir erros, melhorar a estabilidade e adicionar funcionalidades. Por conseguinte, é importante [verificar regularmente se existem actualizações] (https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) e atualizar o seu Dojo. O processo é semelhante ao da instalação inicial, mas requer a substituição de determinados ficheiros pela versão mais recente disponível, mantendo a sua configuração. Aqui estão os passos detalhados a seguir para uma atualização limpa e segura:



Para descobrir a versão atual do seu Dojo, execute o comando :



```bash
./dojo.sh version
```



Embora este passo seja opcional, recomendo que comece por atualizar o seu sistema operativo. Isto reduz o risco de incompatibilidades e garante que as dependências utilizadas pelo Dojo estão actualizadas:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Vá para o diretório Dojo e pare os serviços actuais:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Em seguida, reinicie o seu sistema para obter um quadro limpo:



```bash
sudo reboot
```



O Dojo vem com ficheiros assinados digitalmente. Estas assinaturas PGP garantem que os ficheiros são originários do programador e não foram alterados de forma alguma. É importante verificá-las sempre que atualizar o Dojo, tal como fez quando o instalou pela primeira vez. Comece por descarregar a chave pública do programador através do Tor e, em seguida, importe-a :



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Regressar ao seu diretório pessoal:



```bash
cd ~/
```



Baixe a última versão do Dojo do GitHub via Tor. Neste exemplo, é a versão `1.28.0` (que ainda não existe no momento da escrita: isto é apenas para dar um exemplo). Lembre-se de substituir o arquivo e o link [com a versão que deseja instalar] (https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Descarregue também o ficheiro que contém as impressões digitais e a assinatura PGP (mais uma vez, lembre-se de ajustar a versão no comando):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Verifique se o ficheiro de impressões digitais descarregado foi assinado pela chave do programador:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Deve ser apresentado um resultado correto:



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Pode aparecer um aviso de que a chave não está certificada, mas isso não tem importância. Por outro lado, se a assinatura for inválida ou corresponder a outra chave, não avance mais e comece de novo, verificando as ligações.



Em seguida, calcula a impressão digital SHA256 do arquivo e compara-a com o ficheiro oficial de impressões digitais:



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Se as duas impressões digitais coincidirem perfeitamente, o arquivo é genuíno e está intacto. Se forem diferentes, apague os ficheiros imediatamente e não continue.



Descomprima o arquivo no seu diretório pessoal:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Depois copie o conteúdo para o diretório Dojo, substituindo o antigo ficheiro :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Esta operação mantém seus arquivos de configuração localizados em `~/dojo-app/docker/my-dojo/conf`, mas substitui todos os outros arquivos com as versões atualizadas.



Para manter o seu ambiente limpo, elimine os ficheiros desnecessários :



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Retorne ao diretório de scripts do Dojo e execute o comando update:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Esse comando instrui o Docker a reconstruir as imagens com os novos arquivos e, em seguida, reiniciar automaticamente todos os serviços. No final do processo, verifique os registos para se certificar de que o Bitcoin core, o Fulcrum e o Dojo estão todos a funcionar corretamente:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Se os serviços iniciarem sem erros e os registos mostrarem blocos a serem processados, o seu Dojo está atualizado e operacional.