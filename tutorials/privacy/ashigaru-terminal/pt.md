---
name: Ashigaru Terminal
description: Utilizar o Ashigaru no ambiente de trabalho para fazer coinjoins
---

![cover](assets/cover.webp)



O Ashigaru Terminal é a adaptação da equipa Ashigaru do Sparrow Server, que implementa o protocolo de coinjoin Whirlpool. Este software é uma continuação do trabalho iniciado por Samourai Wallet, em particular na GUI Whirlpool, cujos princípios fundamentais adopta: auto-custódia e preservação da confidencialidade.



Este software é um fork do Sparrow Server, modificado e optimizado para integração total com o ecossistema Whirlpool, o protocolo de coinjoin ZeroLink originalmente desenvolvido pelas equipas Samourai.



O Terminal Ashigaru funciona a partir de uma interface TUI minimalista e pode ser implementado num computador pessoal ou num servidor dedicado. Permite-lhe interagir diretamente com o Whirlpool para iniciar o "*Tx0*", gerir as contas "*Deposit*", "*Premix*", "*Postmix*" e "*Badbank*" e efetuar remisturas automáticas para reforçar a confidencialidade das suas peças.



Em suma, o Terminal Ashigaru será particularmente útil se quiser criar coinjoins utilizando o Whirlpool.



Neste primeiro tutorial, vou mostrar-lhe a instalação e o funcionamento do Terminal Ashigaru. Um segundo tutorial, mais avançado, será então dedicado à criação efectiva de coinjoins.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Instalar o terminal Ashigaru



Para instalar o Terminal Ashigaru, é necessário o Navegador Tor, pois os binários só são distribuídos através da rede Tor. Se ainda não o fizeste, [instala-o na tua máquina](https://www.torproject.org/download/).



### 1.1. Descarregar o terminal Ashigaru



A partir do Navegador Tor, vá para [a página de lançamentos do seu repositório Git](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) para descarregar a última versão do Terminal Ashigaru para o seu sistema operativo.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Descarregue os 2 ficheiros seguintes para o seu sistema operativo:




- O binário (`ashigaru_terminal_v1.0.0_amd64.deb` para Debian/Ubuntu, `.dmg` para macOS ou `.zip` para Windows) ;
- O ficheiro de hashes assinados: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Verificar o terminal Ashigaru



Antes de executar o software no seu dispositivo, é necessário verificar a sua autenticidade e integridade. Este é um passo importante, pois evita que instale uma versão fraudulenta que pode comprometer os seus bitcoins ou infetar a sua máquina.



Abra um novo separador do browser e aceda a [Keybase verification tool](https://keybase.io/verify). Cole o conteúdo do ficheiro `.txt` que acabou de descarregar no campo fornecido e, em seguida, clique no botão `Verificar`.



![Image](assets/fr/02.webp)



Para diversificar as suas fontes de verificação, pode também comparar a mensagem com a que está disponível no sítio clearnet [ashigaru.rs](https://ashigaru.rs/download/), na secção `/download`.



![Image](assets/fr/03.webp)



Se a assinatura for válida, o Keybase apresentará uma mensagem a confirmar que o ficheiro foi assinado pelos programadores da Ashigaru.



![Image](assets/fr/04.webp)



Também pode clicar no perfil `ashigarudev` apresentado pelo Keybase e verificar se a impressão digital da chave corresponde exatamente a: `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Se aparecer um erro nesta fase, a assinatura é inválida. Neste caso, **não instale o software descarregado**. Comece de novo desde o início ou peça ajuda à comunidade antes de continuar.



O Keybase forneceu-lhe o hash autenticado da aplicação. Vamos agora verificar se o hash do ficheiro `.deb`, `.zip` ou `.dmg` que descarregou corresponde ao validado no Keybase. Para isso, vá até [HASH FILE ONLINE](https://hash-file.online/).



Clique no botão `BROWSE...` e selecione o arquivo `.deb`, `.zip` ou `.dmg` baixado no passo 1.1. Em seguida, escolha a função de hash `SHA-256` e clique em `CALCULATE HASH` para generate o hash do seu arquivo.



![Image](assets/fr/06.webp)



O site mostrará então o hash do software. Compare-o com o hash que verificou em Keybase.io. Se os dois corresponderem perfeitamente, a verificação de autenticidade e integridade foi bem-sucedida. Pode então utilizar o software.



![Image](assets/fr/07.webp)



### 1.3 Lançamento do terminal de Ashigaru





- Debian / Ubuntu



Para instalar o software, execute o comando :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Modificar a ordem de acordo com a versão descarregada.



Em seguida, verifique a instalação:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Em seguida, inicie o software:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Janelas**



Clique com o botão direito do rato no ficheiro `.zip` que transferiu e verificou e, em seguida, selecione `Extrair tudo...` para extrair o seu conteúdo.



Quando a extração estiver concluída, faça duplo clique no ficheiro `Ashigaru-terminal.exe` para iniciar o software.



![Image](assets/fr/08.webp)



## 2. Começar a utilizar o Terminal Ashigaru



O Terminal Ashigaru é um programa TUI (*Text-based User Interface*), ou seja, uma interface minimalista que funciona diretamente no terminal. Interage-se com ele utilizando menus e atalhos de teclado, mas sem qualquer ambiente gráfico clássico real.



![Image](assets/fr/09.webp)



É fácil de utilizar: utilize as teclas de setas do teclado para navegar pelos menus e prima a tecla `Enter` para validar uma ação ou confirmar uma escolha.



## 3. Ligar o seu nó ao terminal Ashigaru



Por defeito, o Terminal Ashigaru liga-se a um servidor público Electrum. Isto apresenta obviamente riscos em termos de confidencialidade e soberania. Por isso, vamos configurá-lo para se ligar diretamente ao seu próprio Electrum Server.



Para o fazer, abra o menu `Preferências > Servidor`.



![Image](assets/fr/10.webp)



Clique no botão `< Editar >`.



![Image](assets/fr/11.webp)



Selecione `Private Electrum Server` e, em seguida, clique em `<Continuar>`.



![Image](assets/fr/12.webp)



Introduza o URL e a porta do seu servidor. Pode especificar um endereço Tor em `.onion`. Depois clique em `< Testar >` para verificar a ligação.



![Image](assets/fr/13.webp)



Se a ligação for bem sucedida, aparecerá a mensagem `Sucesso`, juntamente com os detalhes do seu servidor.



![Image](assets/fr/14.webp)



Se ainda não tem um nó Bitcoin, recomendo que faça este curso:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*No meu caso, para este tutorial, vou desconectar-me do meu servidor Electrs porque estou a trabalhar na testnet. No entanto, o funcionamento é rigorosamente idêntico no mainnet.*



## 4. Criar um portefólio no Terminal Ashigaru



Agora que o software está corretamente configurado, podemos adicionar uma carteira Bitcoin.



Tem duas opções:




- Pode criar um novo wallet de raiz e utilizá-lo exclusivamente no Terminal Ashigaru. Neste caso, terá de abrir este software sempre que quiser interagir com o seu wallet;
- Em alternativa, pode importar o seu Ashigaru wallet existente diretamente do seu telefone para o Ashigaru Terminal. A desvantagem deste método é que reduz ligeiramente a segurança da sua configuração, uma vez que o seu wallet fica exposto a dois ambientes de risco em vez de um. Por outro lado, oferece a vantagem de poder deixar o Terminal Ashigaru a funcionar continuamente para misturar as suas moedas, ao mesmo tempo que lhe permite gastá-las à distância através da aplicação móvel Ashigaru.



Neste tutorial, vamos optar pelo segundo método. No entanto, se preferir criar uma carteira completamente nova, o procedimento continua a ser o mesmo: a única diferença será durante a criação, quando terá de guardar a sua nova frase mnemónica e o seu novo passphrase.



Observe também que o Ashigaru Terminal não permite gastar seus bitcoins diretamente. Você pode sincronizar a mesma carteira no Ashigaru Terminal e no aplicativo Ashigaru (o que farei neste tutorial), ou no Sparrow Wallet.



Se ainda não tem um wallet na aplicação Ashigaru, pode seguir o tutorial dedicado :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Aceder ao menu "Carteiras".



![Image](assets/fr/15.webp)



Em seguida, selecionar `Criar / restaurar wallet...`. A opção `Abrir Wallet...` permite-lhe aceder posteriormente a uma carteira já guardada no Terminal Ashigaru.



![Image](assets/fr/16.webp)



Dê um nome à sua carteira.



![Image](assets/fr/17.webp)



Em seguida, selecionar o tipo de carteira `Hot Wallet`.






![Image](assets/fr/18.webp)



É nesta fase que o procedimento difere consoante a sua escolha inicial:




- Se desejar criar uma nova carteira a partir do zero, clique em `<Gerar novo Wallet>`, defina um passphrase BIP39 e, em seguida, guarde cuidadosamente a sua frase mnemónica e o seu passphrase num suporte físico;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Se desejar utilizar o mesmo wallet da sua aplicação Ashigaru, introduza as 12 palavras da sua frase mnemónica e o seu passphrase BIP39 diretamente nos campos correspondentes. Escreva as palavras em minúsculas, inteiras, por ordem, separadas por um espaço, sem números nem caracteres suplementares.



Uma vez concluído este passo, clique em `< Seguinte >`.



*Nota*: Se não conseguir clicar neste botão, a sua frase mnemónica não é válida. Verifique cuidadosamente se nenhuma das palavras está incorrecta ou mal escrita.



![Image](assets/fr/19.webp)



Em seguida, terá de definir uma palavra-passe. Esta será utilizada para desbloquear o seu Terminal Ashigaru wallet e protegê-lo contra o acesso físico não autorizado. Não está envolvida na derivação criptográfica das suas chaves: por outras palavras, mesmo sem esta palavra-passe, qualquer pessoa com a sua frase mnemónica e o passphrase será capaz de restaurar o seu wallet e aceder aos seus bitcoins.



Escolha uma palavra-passe longa, complexa e aleatória. Guarde uma cópia num local seguro: de preferência, num suporte físico ou num gestor de palavras-passe seguro.



Clique em `< OK >` quando tiver terminado.



![Image](assets/fr/20.webp)



## 5. Utilizar a carteira



Pode então escolher a conta a que pretende aceder. De momento, não iniciámos qualquer mistura, por isso vamos aceder à conta `Deposit`.



![Image](assets/fr/21.webp)



O funcionamento é então idêntico ao do Sparrow, uma vez que o Terminal Ashigaru é um fork do Servidor Sparrow. Encontrará os mesmos menus:



![Image](assets/fr/22.webp)





- transacções": permite consultar o histórico das transacções ligadas a esta conta. No meu caso, algumas delas já aparecem, pois tinha efectuado algumas com a aplicação Ashigaru neste mesmo wallet.



![Image](assets/fr/23.webp)





- receive`: gera um novo endereço de recibo em branco para colocar satss na conta de depósito.



![Image](assets/fr/24.webp)





- addresses`: apresenta uma lista de todos os seus endereços, quer pertençam à cadeia interna ou externa da sua conta.



![Image](assets/fr/25.webp)





- `UTXOs`: lista todos os seus UTXOs disponíveis.



![Image](assets/fr/26.webp)





- configurações: dá acesso ao *descritor* da sua carteira. Pode também consultar o seu seed, ajustar o *Gap Limit* ou alterar a data de criação da sua carteira.



![Image](assets/fr/27.webp)



Agora você já sabe como instalar e usar o Ashigaru Terminal. No próximo tutorial, veremos como realizar coinjoins com este software e como gerenciar os fundos em "*Postmix*".
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
