---
name: SeedSigner
description: Hardware wallet de bricolage, sem estado, económico e totalmente equipado com ar
---

![cover](assets/cover.webp)



O SeedSigner é um hardware wallet Bitcoin de código aberto que qualquer pessoa pode construir usando componentes electrónicos de uso geral baratos. Ao contrário de produtos comerciais como o Ledger, Coldcard ou Trezor, este não é um dispositivo pronto a usar fabricado por uma empresa: é um projeto comunitário que permite a qualquer pessoa criar o seu próprio dispositivo, controlando cada passo.



O SeedSigner foi concebido para ser 100% ***air-gapped***: nunca se liga à Internet, não tem Wi-Fi ou Bluetooth (no caso do Raspberry Pi Zero v1.3) e nunca está ligado a um computador para trocar dados. A comunicação faz-se exclusivamente através de um sistema de troca de códigos QR. Em termos concretos, o seu software de gestão de carteiras (como o Sparrow Wallet) apresenta a transação a assinar sob a forma de códigos QR; o utilizador digitaliza-os com a câmara do SeedSigner, depois o dispositivo assina a transação utilizando as suas chaves privadas temporariamente armazenadas na sua memória RAM. Por fim, gera códigos QR com a transação assinada, que o utilizador digitaliza com o seu software para a enviar para a rede Bitcoin.



![Image](assets/fr/001.webp)



SeedSigner também é ***stateless***. Por outras palavras, não guarda o seu seed ou as suas chaves privadas permanentemente, ao contrário de outras carteiras de hardware. Sempre que reinicia, a sua memória fica completamente vazia, a menos que configure o dispositivo para guardar as suas definições num cartão microSD. Por conseguinte, tem de voltar a introduzir o seu seed sempre que o utilizar, sendo o método mais prático armazená-lo sob a forma de um código QR, que deve ser lido no arranque com a câmara do SeedSigner. Este modo de funcionamento reduz consideravelmente a superfície de ataque: mesmo que um ladrão roube o seu dispositivo, não encontrará qualquer informação nele, uma vez que está sempre vazio por defeito.



Outra opção para armazenar o seu seed e usá-lo com o SeedSigner é usar um cartão inteligente *SeedKeeper* em conjunto com um leitor compatível. Isto dá-lhe um *Elemento Seguro* muito robusto para armazenar o seu seed, enquanto utiliza o ecrã do SeedSigner para assinar transacções. Mas esta configuração em particular é objeto de outro tutorial dedicado. Aqui, vamos concentrar-nos na utilização básica do SeedSigner:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

O projeto SeedSigner ocupa um lugar importante no ecossistema Bitcoin, pois oferece a todos, em qualquer parte do mundo, a possibilidade de beneficiar de uma segurança avançada para proteger as suas bitcoins. A sua principal vantagem reside na sua acessibilidade: o hardware necessário pode ser adquirido por menos de 50 dólares. Além disso, permite que as pessoas que vivem em países restritos construam o seu próprio hardware wallet a partir de componentes informáticos padrão, que são fáceis de encontrar e menos sujeitos a restrições regulamentares.



Mas mesmo fora destes contextos particulares, o SeedSigner pode ser uma opção interessante para si: é de código aberto, funciona sem estado e com airgap e reduz os vectores de ataque ligados à cadeia de fornecimento do seu hardware wallet.



## 1. Equipamento necessário



Para construir o seu SeedSigner, precisará dos seguintes componentes:





- Raspberry Pi Zero
    - A versão 1.3 é recomendada, uma vez que não tem Wi-Fi nem Bluetooth, garantindo um isolamento total.
 - As versões W e v2 também são compatíveis, mas incorporam um chip Wi-Fi/Bluetooth. Por conseguinte, é aconselhável desactivá-lo fisicamente, retirando o módulo de rádio do cartão. A operação é relativamente simples, mas requer precisão (um alicate fino é suficiente para o Zero W, enquanto uma caneta quente é necessária para o v2 para remover a placa de metal que esconde o módulo). Não vou entrar em pormenores neste tutorial, mas podem encontrar todas as instruções neste documento: *[Desativação do WiFi/Bluetooth por hardware](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Atenção: alguns modelos Raspberry Pi Zero são vendidos sem pinos GPIO pré-soldados. Pode comprar uma versão com pinos integrados diretamente (solução mais simples), ou comprar os pinos separadamente e soldá-los você mesmo (solução mais complexa).
 - Não se esqueça de incluir uma fonte de alimentação micro-USB.



![Image](assets/fr/002.webp)





- Ecrã Waveshare de 1,3" (240×240 px)** (em francês)
    - É essencial escolher este modelo específico: existem outros ecrãs semelhantes, mas com uma resolução diferente. Sem uma definição de 240×240 px, o ecrã não poderá ser utilizado.
    - O ecrã possui três botões e um mini-joystick para a interface do utilizador.



![Image](assets/fr/003.webp)





- Câmara compatível com Raspberry Pi Zero**
    - Opção 1: a câmara standard com um tapete dourado largo (verifique a compatibilidade com a sua caixa).
    - Opção 2: a câmara mais compacta "*Zero*", concebida especificamente para o Pi Zero.



![Image](assets/fr/004.webp)





- Cartão MicroSD**
    - Capacidade recomendada: entre 4 e 32 GB.





- Habitação (facultativa mas recomendada)** (facultativa mas recomendada)** (facultativa mas recomendada)** (facultativa mas recomendada)**)
    - Protege o dispositivo e torna-o fácil de utilizar.
    - O modelo mais popular é a "*Orange Pill Case*", para a qual estão disponíveis [ficheiros STL de código aberto para impressão 3D](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - As caixas também estão disponíveis em [revendedores independentes ligados ao projeto](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Pode comprar estes componentes separadamente ou, para maior simplicidade, optar por pacotes prontos a usar que incluem todo o hardware necessário. Pessoalmente, encomendei o meu pacote [neste site francês](https://bitcoinbazar.fr/), mas também encontrará uma lista de vendedores para cada região do mundo na [página de hardware do projeto SeedSigner](https://seedsigner.com/hardware/). Se preferir comprar os componentes individualmente, estes estão disponíveis nas principais plataformas de comércio eletrónico ou em lojas especializadas.



## 2. Preparar o software



Uma vez reunido o hardware, é necessário preparar o cartão microSD, instalando nele o sistema SeedSigner. Para o fazer, vá ao seu computador pessoal e ligue o seu microSD destinado ao SeedSigner.



### 2.1. Descarregar



Ir para [o repositório oficial do projeto no GitHub](https://github.com/SeedSigner/seedsigner/releases). Para obter a versão mais recente do software, descarregue :




- A imagem `.img` correspondente ao seu modelo de Pi.
- O ficheiro `.sha256.txt`.
- O ficheiro `.sha256.txt.sig`.



![Image](assets/fr/006.webp)



Antes de iniciar a instalação, vamos verificar o software.



### 2.2 Verificação em Linux e macOS



Comece por importar a chave pública oficial do projeto SeedSigner diretamente do Keybase :



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



O terminal deve informar que uma chave foi importada ou atualizada. Em seguida, execute o comando de verificação no arquivo de assinatura (lembre-se de modificar o comando de acordo com a sua versão, aqui `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Se tudo estiver correto, a saída deve ser `Boa assinatura`. Isto significa que o ficheiro `.sha256.txt` foi assinado pela chave que acabou de importar, e que a assinatura é válida. Ignore a mensagem de aviso `WARNING: This key is not certified with a trusted signature`: isso é normal, pois agora cabe a você verificar se a chave utilizada pertence ao projeto SeedSigner.



Para tal, compare os últimos 16 caracteres da impressão digital apresentada com os disponíveis em [Keybase.io/SeedSigner](https://keybase.io/seedsigner), no seu [Twitter oficial](https://twitter.com/SeedSigner/status/1530555252373704707), ou no ficheiro publicado em [SeedSigner.com](https://seedsigner.com/keybase.txt). Se estes identificadores corresponderem exatamente, pode ter a certeza de que a chave é efetivamente a do projeto. Em caso de dúvida, pare imediatamente e peça ajuda à comunidade SeedSigner (Telegram, X, GitHub...).



Quando a chave tiver sido validada, pode verificar se a imagem descarregada não foi modificada (lembre-se de modificar o comando de acordo com a sua versão, aqui `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- No Linux, este comando está incorporado.
- Atenção: versões do macOS anteriores ao `Big Sur (11)` não reconhecem a opção `--ignore-missing`. Neste caso, remova-a e ignore os avisos sobre ficheiros em falta.



O resultado esperado é um `OK` ao lado do ficheiro `.img`. Isto confirma que a imagem carregada é idêntica à publicada pelo projeto e não foi modificada.



### 2.3 Verificação do Windows



No Windows, o procedimento é semelhante, mas os comandos são diferentes. Comece por instalar o [Gpg4win](https://www.gpg4win.org/) e abra a aplicação *Kleopatra*. Importe a chave pública do projeto SeedSigner a partir do URL Keybase :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Em seguida, abra o PowerShell na pasta onde estão localizados os arquivos baixados (`Shift` + clique com o botão direito do mouse > `Abrir PowerShell aqui`). Execute o seguinte comando para verificar a assinatura do manifesto (lembre-se de modificar o comando de acordo com a sua versão, aqui `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Se tudo estiver correto, a saída deve ser `Boa assinatura`. Isto significa que o ficheiro `.sha256.txt` foi assinado pela chave que acabou de importar, e que a assinatura é válida. Ignore a mensagem de aviso `WARNING: This key is not certified with a trusted signature`: isso é normal, pois agora cabe a você verificar se a chave utilizada pertence ao projeto SeedSigner.



Para tal, compare os últimos 16 caracteres da impressão digital apresentada com os disponíveis em [Keybase.io/SeedSigner](https://keybase.io/seedsigner), no seu [Twitter oficial](https://twitter.com/SeedSigner/status/1530555252373704707), ou no ficheiro publicado em [SeedSigner.com](https://seedsigner.com/keybase.txt). Se estes identificadores corresponderem exatamente, pode ter a certeza de que a chave é efetivamente a do projeto. Em caso de dúvida, pare imediatamente e peça ajuda à comunidade SeedSigner (Telegram, X, GitHub...).



Depois de a chave ter sido validada, é necessário verificar se o ficheiro de imagem não foi corrompido. Para o fazer, utilize o seguinte comando no PowerShell :



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Exemplo para um Raspberry Pi Zero 2 (lembre-se de modificar o comando de acordo com a sua versão, aqui `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



Em seguida, o PowerShell calcula o hash SHA256 do seu arquivo de imagem. Compare esse hash com o valor correspondente em `seedsigner.0.8.6.sha256.txt`.




- Se os dois valores forem rigorosamente idênticos, a verificação é bem sucedida e pode continuar.
- Se forem diferentes, o ficheiro está corrompido ou danificado. Não o utilize e inicie novamente a transferência.



![Image](assets/fr/013.webp)



Uma verificação bem sucedida garante que seu arquivo `.img` é autêntico (assinado pelo SeedSigner) e inalterado (não modificado). Você pode então passar com segurança para o próximo passo.



### 2.4. Pôr a imagem em flash



Se ainda não o tiver, descarregue o software [Balena Etcher](https://etcher.balena.io/) e, em seguida, :




- Insira o cartão microSD no seu computador.
- Lançamento do Etcher.
- Selecione o ficheiro `.img` transferido e verificado.
- Selecione o cartão microSD como destino.
- Clique em `Flash!`.



![Image](assets/fr/014.webp)



Aguarde até que o processo esteja concluído: o seu microSD está pronto a ser utilizado. Agora é altura de montar!



## 3. Montagem do SeedSigner



Depois de o cartão microSD ter sido preparado e flasheado com o software SeedSigner, podes prosseguir com a montagem final. Não tenha pressa, pois algumas peças são frágeis (nomeadamente a toalha de mesa, a câmara e os pinos GPIO).



### 3.1 Preparação da caixa



Em primeiro lugar, abra a sua caixa. Verifique se está limpa e se nenhum resíduo de plástico de impressão 3D está a atrapalhar os fechos internos. Procure por :




- Localização da câmara (pequeno orifício circular na frente).
- A abertura para o ecrã.
- Os recortes para as portas micro-USB e a ranhura microSD do Raspberry Pi Zero.



### 3.2 Instalação da câmara



Localize o conetor de fita da câmara no Raspberry Pi Zero: é uma tira preta fina no lado da placa, que pode ser levantada ligeiramente para abrir. Levante-a cuidadosamente, sem a forçar: deve simplesmente inclinar-se alguns milímetros.



![Image](assets/fr/015.webp)



Insira a tampa da câmara. A parte castanha/cobre deve estar virada para baixo. Certifique-se de que está firmemente encaixada no conetor, sem torcer.



![Image](assets/fr/016.webp)



Feche a barra preta para bloquear a toalha de mesa (sentirá um ligeiro clique). Verifique cuidadosamente se a toalha se mantém no sítio e não se move.



![Image](assets/fr/017.webp)



Em seguida, coloque o módulo da câmara no orifício adequado da caixa. Consoante o modelo, este pode encaixar diretamente ou necessitar de uma pequena fita adesiva para o manter no lugar. A lente deve estar perfeitamente alinhada, virada para o exterior.



### 3.3 Instalar o Raspberry Pi Zero



Se estiver a utilizar uma caixa, insira a placa Raspberry Pi Zero no seu interior. Alinhe cuidadosamente as portas com as aberturas fornecidas.



Em seguida, posicione o ecrã Waveshare em cima do Raspberry Pi Zero. Os pinos GPIO do Pi devem alinhar-se perfeitamente com o conetor fêmea do ecrã. Pressione lentamente o ecrã sobre os pinos, aplicando uma pressão uniforme em cada lado para evitar dobrá-los.



![Image](assets/fr/018.webp)



Se tiver uma caixa, complete a montagem adicionando o painel frontal e o joystick.



Por fim, insira o cartão microSD que contém o software atualizado na ranhura montada na extremidade do Raspberry Pi Zero. Certifique-se de que encaixa no lugar.



### 3.4 Primeiro arranque



Ligar um cabo de alimentação micro-USB à porta dedicada. Aguarde cerca de um minuto. O logótipo do SeedSigner deverá aparecer, seguido do ecrã inicial.



![Image](assets/fr/019.webp)



Para começar, verifique se os vários componentes estão a funcionar corretamente, indo ao menu `Configurações > Teste de E/S`.



![Image](assets/fr/020.webp)



Teste todos os botões e certifique-se de que respondem corretamente. Em seguida, clique no botão `KEY1` para verificar se a câmara está a funcionar como esperado. Isto irá tirar uma fotografia.



![Image](assets/fr/021.webp)



### 3.5 Regulação da câmara



Dependendo da forma como montou o SeedSigner, a câmara pode apresentar uma imagem invertida. Para corrigir esta situação, vá a `Configurações > Avançadas > Rotação da câmara` e selecione uma rotação de 180°, se necessário.



![Image](assets/fr/022.webp)



Se tiver alterado a orientação da câmara ou pretender alterar outras definições (como o idioma da interface) mais tarde, terá de ativar a persistência das definições no microSD. Caso contrário, as suas definições serão repostas por defeito sempre que reiniciar o sistema, uma vez que o Raspberry Pi Zero não tem memória persistente.



Para o fazer, abra o menu `Configurações > Configurações persistentes` e selecione `Ativado`.



![Image](assets/fr/023.webp)



Se tudo estiver funcional, o seu SeedSigner está pronto a ser utilizado!



## 4. Definições do SeedSigner



Antes de criares o teu Bitcoin wallet, vamos configurar o SeedSigner. Como funciona num Raspberry Pi Zero sem memória persistente, as suas definições não são guardadas automaticamente, a menos que as guarde no cartão microSD. Por isso, certifica-te de que activaste esta opção, caso contrário, estas definições perder-se-ão ao reiniciar (ver passo 3.5).



### 4.1 Acesso ao menu de parâmetros



Inicie o seu SeedSigner e aguarde que o ecrã inicial apareça. Utilizando o joystick, navegue até à opção `Settings` e valide-a premindo o botão central. Entra agora no menu principal de definições.



![Image](assets/fr/024.webp)



### 4.2 Escolha do software de gestão de carteiras



Em seguida, aceda ao menu `Software coordenador`.



![Image](assets/fr/025.webp)



O `Coordenador` refere-se ao software de gestão de carteiras com o qual o seu SeedSigner irá comunicar através de códigos QR. Este software é instalado no seu computador ou no seu smartphone. Permite-lhe gerir os seus bitcoins, mas sem nunca ter acesso às suas chaves privadas. O SeedSigner continua a ser o único dispositivo capaz de assinar as suas transacções.



A versão atual do firmware suporta vários programas: Sparrow, Specter, BlueWallet, Nunchuk e Keeper. No meu caso, utilizo o **Sparrow Wallet**, que recomendo particularmente pela sua simplicidade e riqueza de funcionalidades.



Se não sabe como o instalar, pode seguir este tutorial:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Basta selecionar o software da sua escolha no menu.



![Image](assets/fr/026.webp)



### 4.3 Indicação das unidades e da quantidade



No menu `Visualização da denominação`, pode escolher a unidade em que os montantes são apresentados:




- `BTC`
- mBTC` (mili-bitcoin, ou 0,001 BTC)
- gW-15 (satoshis, ou 1/100.000.000 BTC)



A unidade **sats** é geralmente a mais prática para pequenas quantidades.



![Image](assets/fr/027.webp)



### 4.4 Definições avançadas



Agora vá para o menu `Avançado`. Aqui encontrará várias opções úteis:




- gW-17 network`: a ser modificado apenas se desejar usar o SeedSigner no Testnet.
- qR code density`: ajusta a quantidade de informação contida em cada código QR. Pode deixar o valor predefinido, a não ser que tenha dificuldade em ler durante a leitura.
- `Xpub export`: ativa ou desactiva a exportação da sua chave pública alargada (`xpub`, `ypub`, `zpub`) para software de gestão de portefólio através de código QR (uma função que iremos utilizar mais tarde, por isso deixe-a activada por agora).
- `Script types`: define os tipos de script permitidos para bloquear seus bitcoins. Não é necessário modificar este parâmetro, pois o tipo de script será definido diretamente para Sparrow. Aqui, apenas os scripts que o SeedSigner está autorizado a manipular estão em causa.



### 4.5 Seleção da língua



Por fim, no menu `Língua`, pode alterar a língua da interface de acordo com as suas preferências.



![Image](assets/fr/028.webp)



## 5. Criar e guardar o seed



O seed (ou frase mnemónica) constitui a base da sua carteira Bitcoin. É usado para derivar as suas chaves privadas e endereços, e fornece acesso aos seus fundos. O SeedSigner oferece vários métodos para a sua geração, que veremos nesta secção.



Antes de começarmos, alguns lembretes essenciais:




- Esta frase dá acesso total e irrestrito a todos os seus bitcoins.** Qualquer pessoa na posse desta frase pode roubar os seus fundos, mesmo sem acesso físico ao seu SeedSigner ;
- Normalmente, uma frase de 12 palavras é usada para restaurar um wallet em caso de perda ou roubo do hardware do wallet. Mas como o SeedSigner é um dispositivo *sem estado*, ele nunca regista o seu seed. Assim, as suas cópias de segurança físicas não são simplesmente cópias de segurança, mas **a única forma de utilizar o seu wallet**. Se perderes estas cópias de segurança, os teus bitcoins ficarão permanentemente perdidos. Por isso, faça cópias de segurança com cuidado, em vários suportes e em locais seguros;
- Se está a começar, aconselho-o vivamente a ler este tutorial para compreender em pormenor os riscos envolvidos na gestão de uma frase mnemónica:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Acesso à ferramenta de criação do seed



No ecrã inicial do SeedSigner, vá ao menu `Ferramentas`.



![Image](assets/fr/029.webp)



Agora, o generate é o seu seed. Um seed é simplesmente um grande número aleatório. Quanto mais aleatório ele for gerado, mais seguro ele é. O SeedSigner oferece duas maneiras de fazer isso:




- câmara": O seed é gerado a partir do ruído visual de uma fotografia. Tira-se uma imagem de um ambiente aleatório (objeto, paisagem, rosto, etc.) cujas variações de pixéis são utilizadas para gerar a entropia generate. É um método rápido, mas não reproduzível.
- lance de dados": lança-se um dado para criar a entropia necessária. É mais demorado, mas reproduzível e, portanto, verificável. Se optar por este método, siga os conselhos deste tutorial (não é necessário calcular o checksum aqui, o SeedSigner trata disso):



https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Criar o seed com a fotografia



Se escolher o método da fotografia, clique em `Novo seed` (com o ícone da câmara), tire uma fotografia e valide. Em seguida, selecione o comprimento da sua frase (12 ou 24 palavras), que aparecerá no ecrã para ser guardada. Os passos seguintes são idênticos aos da secção 5.3.



### 5.3 Criar seed com dados



Neste tutorial, usaremos o método **Dice Rolls**. Clique em `Novo seed` (com o ícone do dado).



![Image](assets/fr/030.webp)



Em seguida, escolha o comprimento da sua frase mnemónica. 12 palavras já oferecem um nível de segurança suficiente, pelo que esta é a escolha que recomendo.



![Image](assets/fr/031.webp)



Lance os seus dados e introduza os números resultantes utilizando o cursor. Prima o botão central para validar cada entrada. Se cometeres um erro, podes voltar atrás. Utilize vários dados diferentes para reduzir a influência de um dado desequilibrado. Certifica-te de que não estás a ser observado durante esta operação.



![Image](assets/fr/032.webp)



Depois de ter introduzido os seus 50 lançamentos, o SeedSigner gera a sua frase. **Siga cuidadosamente as instruções deste tutorial se estiver a começar



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Visualizar e guardar o seed



Escreva cuidadosamente as palavras da sua frase mnemónica num suporte físico adequado (papel ou metal).



![Image](assets/fr/033.webp)



### 5.5 Verificar a cópia de segurança



Para evitar quaisquer erros de backup, o SeedSigner pede-lhe para verificar o seu backup. Clique em `Verificar`.



![Image](assets/fr/034.webp)



De seguida, introduza a palavra pretendida de acordo com a sua ordem na frase. Por exemplo, aqui tenho de escolher a terceira palavra da minha frase.



![Image](assets/fr/035.webp)



Se cometer um erro, o SeedSigner informá-lo-á e terá de começar de novo, certificando-se de que anota a sua frase mnemónica quando esta lhe for dada. Esta etapa de verificação garante que a sua cópia de segurança está correta e completa. Uma vez validado, o ecrã mostrará `Backup Verified`.



![Image](assets/fr/036.webp)



Para um teste de restauro mais completo, siga este tutorial :



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Compreender o conceito de "dispositivo sem estado



O SeedSigner é um dispositivo sem memória permanente. Isto significa que o seu seed nunca é guardado dentro do dispositivo (ao contrário de um Ledger, Trezor ou Coldcard, por exemplo). Assim que se desliga a alimentação, o seed desaparece completamente da sua memória RAM. Quando se reinicia, o SeedSigner volta a um estado vazio: terá então de lhe dar o seu seed novamente, para que possa assinar as suas transacções.



Isto proporciona uma proteção essencial. Ao contrário de outras carteiras de hardware, o SeedSigner é baseado num Raspberry Pi Zero, que não tem proteção física, incluindo o *Secure Element*. Mas como não são armazenados dados sensíveis, mesmo um dispositivo fisicamente comprometido não permitiria a um atacante extrair as suas chaves privadas ou gastar os seus bitcoins.



Por outro lado, esta arquitetura implica uma responsabilidade adicional: sem uma cópia de segurança, os seus fundos estão definitivamente perdidos. É por isso que recomendo uma **dupla cópia de segurança**. Já tem a sua frase de recuperação: esta é a sua principal cópia de segurança a longo prazo, que deve ser guardada num local seguro. Agora vamos criar uma cópia desta frase sob a forma de **código QR**.



Cada vez que utiliza o SeedSigner, digitaliza este código QR com a câmara do dispositivo para que este carregue temporariamente o seu seed na sua memória enquanto assina as suas transacções. Esta segunda cópia de segurança, destinada ao uso quotidiano, também deve ser guardada com o máximo cuidado: qualquer pessoa que esteja na posse deste código QR tem acesso total aos seus bitcoins.


Aconselho-o também a guardar o seu código QR e a sua frase mnemónica em dois locais distintos, para evitar perder tudo em caso de sinistro.



Finalmente, uma alternativa mais avançada e segura é usar o SeedSigner com um **SeedKeeper**, que armazena o seed num secure element. Para saber mais, consulte este tutorial:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Escrever a impressão digital da chave mestra



Quando a verificação estiver concluída, o SeedSigner exibe a impressão digital da chave mestra do seu wallet. Esta impressão digital identifica o seu wallet e garante que utiliza a frase de recuperação correta no futuro. Não revela qualquer informação sobre as suas chaves privadas, pelo que pode guardá-la em segurança num suporte digital. Certifique-se apenas de que mantém uma cópia acessível e que nunca a perde.



![Image](assets/fr/037.webp)



É também nesta fase que pode adicionar um **passphrase BIP39** para reforçar a segurança do seu wallet. Dependendo da sua estratégia de backup, esta opção pode valer a pena, mas também acarreta riscos: se perder o passphrase, o acesso aos seus bitcoins ficará permanentemente perdido.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Se ainda não está familiarizado com o conceito passphrase, convido-o a ler este tutorial completo sobre o assunto:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Guardar o seed em formato QR (*SeedQR*)



O SeedSigner permite-lhe converter o seu seed num código QR em papel, chamado *SeedQR*. Este método simplifica o recarregamento do seu wallet, uma vez que evita redigitar cada palavra manualmente.



Para isso, é necessário um papel em branco ou um código QR metálico correspondente ao comprimento da sua frase mnemónica. Se adquiriu um pacote completo para o seu SeedSigner, os modelos estão normalmente incluídos. Caso contrário, pode descarregá-los e imprimi-los (ou reproduzi-los à mão) aqui :




- [formato de 12 palavras](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [formato de 24 palavras](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Formato compacto 12 palavras](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Formato compacto 24 palavras](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



No ecrã do seed, selecione `Backup Seed`.



![Image](assets/fr/039.webp)



Em seguida, selecione `Exportar como SeedQR`.



![Image](assets/fr/040.webp)



Em seguida, selecionar o formato pretendido (normal ou compacto) de acordo com o modelo de papel disponível.



![Image](assets/fr/041.webp)



Clique em "Iniciar" para começar a criar o *SeedQR*. O SeedSigner mostrará então uma série de grelhas (A1, A2, B1, etc.), cada uma correspondendo a uma parte do código.



![Image](assets/fr/042.webp)



Reproduza cuidadosamente cada ponto preto na sua folha de registo e, em seguida, utilize o joystick para passar ao bloco seguinte. Não tenha pressa: um simples desalinhamento pode tornar o código QR inutilizável.



Algumas dicas:




- Comece com um lápis para poder corrigir eventuais erros e, depois, volte a utilizar uma caneta preta fina quando tiver terminado;
- Um ponto bem centrado no meio do quadrado é tudo o que precisa, não é necessário preenchê-lo completamente.



![Image](assets/fr/043.webp)



Em seguida, clique em `Confirmar SeedQR` e digitalize o seu código QR para verificar se está a funcionar corretamente.



![Image](assets/fr/044.webp)



Se for apresentada a mensagem `Success`, o seu *SeedQR* é válido: pode avançar para o passo seguinte.



![Image](assets/fr/045.webp)



**Guarde esta folha tão rigorosamente como a sua frase de recuperação. Qualquer pessoa na posse deste código QR pode reconstruir as suas chaves privadas e roubar os seus bitcoins



Parabéns, a sua carteira Bitcoin está agora a funcionar! Vamos agora importar os seus componentes públicos para o **Sparrow Wallet** para o gerir facilmente.



## 6. Importar o wallet para o Sparrow



Uma vez configurado o seu SeedSigner e gerado e guardado corretamente o seu seed, o passo seguinte é ligar esta carteira a um software de gestão como o Sparrow Wallet. O seu seed permanecerá sempre offline, uma vez que apenas a parte pública da sua carteira será transmitida ao Sparrow. Isto permitirá que o software mostre os seus endereços, transacções e crie novas transacções, sem nunca poder gastar os seus bitcoins. Para gastar os seus bitcoins, o seu SeedSigner terá sempre de assinar a transação preparada pelo Sparrow.



### 6.1 Preparação do SeedSigner



Insira o microSD que contém o sistema operativo, ligue o seu SeedSigner e carregue o seed que acabou de criar a partir do seu código QR de cópia de segurança. No ecrã inicial, selecione `Scan`, depois digitalize o seu SeedQR com o SeedSigner.



![Image](assets/fr/046.webp)



Verifique se a impressão digital na sua chave mestra corresponde à impressão digital no seu wallet. Se estiver a utilizar um passphrase, introduza-o nesta fase.



![Image](assets/fr/047.webp)



Isto leva-o ao menu do seu portefólio, no meu caso denominado `d4149b27`. Se estiver de volta ao ecrã inicial, selecione `Seeds`, depois escolha a impressão correspondente ao seu portfólio. De seguida, clique em `Export Xpub`.



![Image](assets/fr/048.webp)



Selecione o tipo de carteira. No nosso caso, trata-se de uma carteira única: selecione `Single Sig`.



![Image](assets/fr/049.webp)



Segue-se a escolha da norma de scripting. A mais recente e mais económica em termos de custos de transação é a `Taproot`. Por conseguinte, aconselho-o a escolher esta norma.



![Image](assets/fr/050.webp)



Aparecerá uma mensagem de aviso. Isto é normal: esta chave pública alargada (`xpub`) permite-lhe ver todos os endereços derivados do seu seed (na primeira conta). Não lhe permite gastar os seus fundos, mas revela a estrutura da sua carteira. Se alguma vez vazar, é um problema para a sua privacidade, mas não para a segurança dos seus bitcoins: permite-lhe vê-los, mas não gastá-los.



Clique em `I Understand` e depois em `Export Xpub` se estiver satisfeito com as informações apresentadas.



O SeedSigner gera então o seu xpub sob a forma de um código QR dinâmico que contém todos os dados necessários para gerir a sua carteira no Sparrow Wallet.



![Image](assets/fr/051.webp)



Pode utilizar o joystick para ajustar o brilho do ecrã para facilitar a leitura do código QR.



### 6.2 Importação de um novo portefólio para o Sparrow Wallet



Certifique-se de que tem o software Sparrow Wallet instalado no seu computador. Se não sabe como descarregar, verificar e instalar corretamente o software, consulte o nosso tutorial completo sobre o assunto:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

No seu computador, abra o Sparrow Wallet e, em seguida, na barra de menus, clique em `Arquivo → Importar Wallet`.



![Image](assets/fr/052.webp)



Desloque-se para baixo até `SeedSigner` e selecione `Scan...`. A sua webcam será aberta: digitalize o código QR dinâmico apresentado no ecrã do SeedSigner.



![Image](assets/fr/053.webp)



Atribua um nome ao seu portfólio e clique em `Create Wallet`. O Sparrow pedir-lhe-á então que defina uma palavra-passe para bloquear o acesso local a este wallet. Escolha uma senha forte: ela protege o acesso aos dados do seu portfólio no Sparrow (chaves públicas, endereços, etiquetas e histórico de transações). Esta palavra-passe não é necessária para restaurar a carteira numa data posterior: apenas a sua frase mnemónica (e possivelmente o seu passphrase) é necessária para este fim.



Recomendo que guarde esta palavra-passe num gestor de palavras-passe para evitar perdê-la.



![Image](assets/fr/054.webp)



O seu registo de chaves foi importado com sucesso.



![Image](assets/fr/055.webp)



Em seguida, verifique se a `Master fingerprint` apresentada no Sparrow corresponde à anteriormente registada no seu SeedSigner.



O seu SeedSigner e o Sparrow Wallet estão agora ligados de forma segura. O Sparrow actua como uma interface de gestão completa, enquanto o SeedSigner continua a ser o único dispositivo capaz de assinar as suas transacções. Está agora pronto para receber e enviar bitcoins numa configuração totalmente protegida pelo ar.



## 7. Receber e enviar bitcoins



O seu SeedSigner e o Sparrow Wallet estão agora configurados para trabalhar em conjunto. Nesta secção final, veremos como receber e enviar bitcoins usando esta configuração.



### 7.1 Receber bitcoins



#### 7.1.1 Gerar um endereço de receção



No seu computador, abra o Sparrow Wallet e desbloqueie o seu SeedSigner wallet utilizando a sua palavra-passe. Certifique-se de que o software está ligado a um servidor (entalhe no canto inferior direito). Na barra lateral, clique em `Receive`.



![Image](assets/fr/056.webp)



É apresentado um novo endereço Bitcoin. Verá :




- O endereço de texto (começando por `bc1p...` se utilizar o P2TR como eu),
- O código QR correspondente,
- Um campo `Label` para acompanhar as suas transacções.



Recomendo vivamente que adicione uma etiqueta a cada recibo de bitcoin no seu wallet. Isto permitir-lhe-á identificar facilmente a proveniência de cada UTXO e melhorar a sua gestão de privacidade. Para aprofundar este importante tópico, podes consultar a formação dedicada na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Para adicionar uma etiqueta, basta introduzir um nome no campo `Rótulo` e confirmar.



Por exemplo:



```txt
Label : Sale of the Raspberry Pi Zero
```



O seu endereço está agora associado a esta etiqueta em todas as secções do Sparrow.



![Image](assets/fr/057.webp)



#### 7.1.2 Verificação Address no SeedSigner



Antes de partilhar o seu endereço de receção, é muito importante verificar se este pertence ao seu seed. Este passo garante que o seu SeedSigner poderá assinar transacções associadas a este endereço. Ele também protege contra possíveis ataques em que o Sparrow exibe um endereço fraudulento. Lembre-se que o Sparrow é executado num ambiente inseguro (o seu computador), que tem uma superfície de ataque muito maior do que o seu SeedSigner, que está totalmente isolado. É por isso que nunca deve acreditar cegamente nos endereços de receção apresentados no Sparrow até que os tenha verificado com o seu hardware wallet.



No Sparrow, clique no código QR do endereço para o ampliar: será então apresentado em ecrã inteiro.



![Image](assets/fr/058.webp)



No seu SeedSigner, no menu principal, selecione `Scan`. Digitalize o código QR apresentado no ecrã do seu computador e, em seguida, escolha o seed correspondente ao seu wallet (no meu caso, a impressão digital `d4149b27`).



![Image](assets/fr/059.webp)



Se o endereço digitalizado corresponder ao endereço derivado do seu seed, o ecrã do SeedSigner apresentará a mensagem: `Address Verificado`.



![Image](assets/fr/060.webp)



Isto confirma que o endereço pertence ao seu wallet e que pode receber bitcoins dele com confiança.



#### 7.1.3 Receção de fundos



Pode agora comunicar este endereço (sob a forma de texto ou de código QR) à pessoa ou ao serviço que tem de lhe enviar satss. Assim que a transação for difundida na rede, aparecerá no separador `Transacções` do Sparrow Wallet.



![Image](assets/fr/061.webp)



### 7.2 Enviar bitcoins



O envio de bitcoins com um SeedSigner é um processo de 3 passos:




- Criação de transacções no Sparrow ;
- Assinatura da transação no SeedSigner ;
- Distribuição final da transação através do Sparrow.



Todas as trocas entre os dois dispositivos são efectuadas exclusivamente através de códigos QR.



#### 7.2.1 Criação da transação no Sparrow



No Sparrow Wallet, pode clicar no separador "Enviar" na barra lateral esquerda. No entanto, prefiro utilizar o separador `UTXOs`, que permite praticar o "*Coin Control*". Este método permite-lhe controlar com precisão os UTXOs utilizados, de modo a poder controlar a informação que revela durante a transação.



No separador "UTXOs", selecione as moedas que pretende gastar e clique em "Enviar selecionados".



![Image](assets/fr/062.webp)



Em seguida, preencha os campos da transação:




- Em "Pagar a", cole o endereço do destinatário ou clique no ícone da câmara para digitalizar o código QR;
- Em `Label`, adicione uma etiqueta para registar esta despesa;
- Em `Montante`, introduza o montante a enviar;
- Por fim, selecionar a taxa de honorários com base nas condições actuais do mercado (as estimativas estão disponíveis em [mempool.space](https://mempool.space/)).



Uma vez preenchidos os campos, verifique cuidadosamente as informações e clique em `Criar transação >>`.



![Image](assets/fr/063.webp)



Verifique os detalhes da transação para se certificar de que tudo está correto e, em seguida, clique em `Finalizar transação para assinatura`.



![Image](assets/fr/064.webp)



A transação está agora pronta, mas ainda não foi assinada. Para visualizar o [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) como um código QR, clique em `Mostrar QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 Assinar a transação com o SeedSigner



Ligue o seu SeedSigner e digitalize o seu SeedQR para aceder à sua carteira, como habitualmente. A partir do ecrã inicial, selecione `Scan`, depois digitalize o código QR apresentado no Sparrow.



![Image](assets/fr/066.webp)



Em seguida, escolha o seed que corresponde à sua carteira.



![Image](assets/fr/067.webp)



O SeedSigner detecta automaticamente que se trata de um PSBT e apresenta um resumo da transação:




   - O montante enviado,
   - Endereços de saída,
   - Custos de transação associados.



Clique em "Rever detalhes" e verifique cuidadosamente todas as informações diretamente no ecrã do SeedSigner. Os itens mais importantes a serem verificados são o valor enviado, o endereço do destinatário e o valor das taxas aplicadas.



![Image](assets/fr/068.webp)



Se tudo estiver correto, selecione `Approve PSBT` para assinar a transação utilizando a(s) chave(s) privada(s) correspondente(s).



![Image](assets/fr/069.webp)



Uma vez assinada, o SeedSigner gera um novo código QR contendo a transação assinada, pronto a ser digitalizado pelo Sparrow.



![Image](assets/fr/070.webp)



#### 7.2.3 Difusão da transação a partir do Sparrow



Agora que a transação é válida, precisa de ser transmitida na rede Bitcoin, para que chegue a um mineiro que a adicionará a um bloco.



No Sparrow, clique em `QR Scan`.



![Image](assets/fr/071.webp)



Apresente o código QR exibido pelo seu SeedSigner (o da transação assinada) à webcam. O Sparrow descodificará a assinatura e apresentará os detalhes completos da transação. Faça uma verificação final para verificar se todas as informações estão corretas e clique em Broadcast Transaction para transmiti-la na rede Bitcoin.



![Image](assets/fr/072.webp)



A sua transação foi agora enviada para a rede Bitcoin. Pode acompanhar a sua evolução no separador `Transacções` do Sparrow Wallet.



![Image](assets/fr/073.webp)



Agora já domina as noções básicas de utilização do SeedSigner. Para aprofundar os seus conhecimentos e explorar utilizações mais avançadas, convido-o a consultar o seguinte tutorial:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Também pode apoiar o desenvolvimento do projeto open-source SeedSigner fazendo um donativo em bitcoins!](https://seedsigner.com/donate/)**



*Crédito: algumas das imagens neste tutorial provêm do [sítio Web oficial do projeto SeedSigner](https://seedsigner.com/) e do [repositório GitHub](https://github.com/SeedSigner/seedsigner).*