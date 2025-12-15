---
name: Seedkeeper x SeedSigner
description: Como é que utilizo o Seedkeeper com o meu SeedSigner?
---

![cover](assets/cover.webp)



*Agradecimentos à equipa [Satochip](https://satochip.io/) por concordar em reutilizar [os seus vídeos](https://www.youtube.com/@satochip/videos) neste tutorial. Obrigado também ao [Crypto Guide](https://www.youtube.com/@CryptoGuide/) pelo seu fork do firmware SeedSigner, permitindo o suporte para smartcards



---

O SeedSigner é um hardware wallet que você mesmo monta a partir de hardware padrão, geralmente em torno de um Raspberry Pi Zero. Este wallet é chamado de "*stateless*": ao contrário da maioria dos outros modelos no mercado (Coldcard, Trezor, Ledger, etc.), ele não armazena quaisquer dados em memória permanente, e opera apenas ao vivo a partir da RAM. Por conseguinte, o seed da sua carteira nunca é armazenado no SeedSigner. Cada vez que reiniciar, terá de o preencher para permitir que o dispositivo assine as suas transacções. O método mais comum consiste em guardar o seu seed como um código QR, que será lido sempre que o utilizar (*SeedQR*).



Esta abordagem apresenta, no entanto, um risco significativo: o seed deve permanecer acessível em texto claro para que possa ser digitalizado. Em caso de roubo ou intrusão, um atacante poderia facilmente apoderar-se dele e roubar os seus bitcoins.



Para ultrapassar esta fraqueza, o SeedSigner pode ser combinado com o [**Seedkeeper**](https://satochip.io/product/seedkeeper/), um cartão inteligente desenvolvido pela Satochip. Isto permite que frases mnemónicas (ou outros segredos) sejam armazenadas num secure element protegido por um código PIN. O applet Seedkeeper é open-source e o seu secure element tem certificação EAL6+. Usado em conjunto com o SeedSigner, oferece uma caraterística de segurança muito interessante: as suas chaves permanecem geridas inteiramente off-line, assina as suas transacções num ecrã de confiança, e o seed está fisicamente protegido num smartcard resistente a ataques físicos.



Tudo o que é necessário para completar a instalação são os seguintes itens:




- O equipamento habitual necessário para um SeedSigner clássico: um Raspberry Pi Zero, um ecrã Waveshare de 1,3", uma câmara compatível e um cartão microSD (encontrará mais detalhes no tutorial do SeedSigner abaixo);
- O kit de extensão SeedSigner, disponível [na loja oficial Satochip] (https://satochip.io/product/seedsigner-extension-kit/), que permite ler e escrever no smartcard diretamente a partir do seu SeedSigner. Outra opção é usar um leitor de smartcard externo, que pode ser conectado por cabo a uma porta Micro-USB no Raspberry Pi. No entanto, eu mesmo não testei essa solução;
- Um Seedkeeper ou, em alternativa, um smartcard em branco para instalar a aplicação Seedkeeper (o kit de extensão vendido pela Satochip já inclui um smartcard em branco).



![Image](assets/fr/01.webp)



Este tutorial abrange dois cenários:




- Se já tem uma carteira Bitcoin gerida através do seu SeedSigner, basta instalar o novo firmware. Pode então continuar a utilizar o seu wallet existente, desta vez utilizando o Seedkeeper para maior segurança.
- Se ainda não tiver um Bitcoin wallet associado ao seu SeedSigner, terá de seguir os passos **5** e **6** do tutorial mencionado abaixo. Estas secções explicam como criar uma frase mnemónica generate com o SeedSigner, guardá-la através de um *SeedQR* e depois ligar este wallet ao Sparrow Wallet para o gerir. Não vou entrar nestes procedimentos aqui e **presumo que já tem um Bitcoin wallet a funcionar, configurado com o Sparrow e o seu SeedSigner**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Instalar o firmware



Para utilizar o seu SeedSigner com um Seedkeeper, é necessário instalar um firmware alternativo, diferente do SeedSigner original, de modo a suportar a leitura de cartões inteligentes. Para isso, [recomendo usar o fork da "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Descarregue [a última versão da imagem](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) correspondente ao modelo de Raspberry Pi que está a usar.



![Image](assets/fr/02.webp)



Se ainda não o tiver, descarregue o software [Balena Etcher] (https://etcher.balena.io/) e proceda da seguinte forma:




- Insira o cartão microSD no seu computador;
- Lançador ;
- Selecione o ficheiro `.zip` que acabou de descarregar;
- Selecione o cartão microSD como destino;
- Clique em `Flash!`.



![Image](assets/fr/03.webp)



Aguarde até o processo estar concluído: o seu microSD está agora pronto a ser utilizado. Pode agora passar à montagem do seu dispositivo.



Para mais pormenores sobre a instalação do firmware e a verificação do software (um passo que recomendo vivamente), consulte o seguinte tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Montagem do leitor de cartões inteligentes



![video](https://youtu.be/jqE8HDMCImA)



Comece por instalar a câmara no Raspberry Pi Zero, inserindo-a cuidadosamente no pino da câmara e fixando-a com a patilha preta. Em seguida, coloque o Pi na parte inferior da caixa, certificando-se de que alinha as portas com as aberturas correspondentes.



![Image](assets/fr/04.webp)



De seguida, ligue o leitor de cartões inteligentes aos pinos GPIO do Raspberry Pi Zero.



![Image](assets/fr/05.webp)



Faça deslizar a tampa de plástico sobre o leitor de cartões inteligentes até ficar corretamente posicionada.



![Image](assets/fr/06.webp)



Em seguida, adicione o ecrã aos pinos GPIO da extensão.



![Image](assets/fr/07.webp)



Por fim, insira o cartão microSD que contém o firmware na porta lateral do Raspberry Pi Zero.



![Image](assets/fr/08.webp)



Agora pode ligar o seu SeedSigner através da porta Micro-USB do Raspberry Pi Zero, ou através da porta USB-C da extensão. Ambas as opções funcionam. Aguarde alguns segundos para a inicialização, então você deve ver a tela de boas-vindas aparecer.



![Image](assets/fr/09.webp)



Para mais pormenores sobre a configuração inicial do seu SeedSigner, recomendo o seguinte tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flash de um smartcard com o applet Seedkeeper (opcional)



![video](https://youtu.be/NF4HemyEcOY)



Se já possui um Seedkeeper, pode saltar este passo e ir diretamente para o passo 4. Nesta secção, veremos como instalar o applet Seedkeeper num smartcard em branco (método DIY).



Para começar, abra o menu `Ferramentas > Ferramentas de Smartcard` no seu SeedSigner.



![Image](assets/fr/10.webp)



Em seguida, selecione `Ferramentas DIY > Instalar Applet`.



![Image](assets/fr/11.webp)



Insira o seu smartcard no leitor SeedSigner, com o chip virado para baixo, e escolha a aplicação `SeedKeeper`.



![Image](assets/fr/12.webp)



Seja paciente durante a instalação: o processo pode demorar algumas dezenas de segundos.



![Image](assets/fr/13.webp)



Quando o applet tiver sido instalado com sucesso, pode avançar para o passo 4.



![Image](assets/fr/14.webp)



## 4. Guardar um SeedQR existente no Seedkeeper



![video](https://youtu.be/X-vmFHU9Ec8)



Agora que o seu Seedkeeper está operacional, pode guardar a sua mnemónica Bitcoin wallet no smartcard. Para começar, ligue o seu SeedSigner como de costume e, em seguida, digitalize o *SeedQR* do seu wallet para carregá-lo no dispositivo. Quando o seed tiver sido importado, basta selecionar "Concluído".



![Image](assets/fr/15.webp)



Quando o seed estiver carregado, aceder ao menu `Backup Seed`.



![Image](assets/fr/16.webp)



Em seguida, insira seu Seedkeeper na unidade do SeedSigner e selecione a opção `To SeedKeeper`.



![Image](assets/fr/17.webp)



O SeedSigner pedir-lhe-á então que introduza um código PIN para o seu Seedkeeper. Como este é um cartão em branco, ainda não foi definido nenhum código. Introduza qualquer código para saltar esta etapa e, em seguida, valide.



![Image](assets/fr/18.webp)



O SeedSigner detecta que o Seedkeeper ainda não foi inicializado (ou seja, nenhuma senha foi definida). Clique em `Eu entendo` para continuar.



![Image](assets/fr/19.webp)



Escolha agora o novo código PIN do seu guardião de sementes, entre 4 e 16 caracteres. Para maior segurança, escolha um código longo e aleatório: é a única barreira que protege o acesso físico à sua frase mnemónica.



Lembre-se de guardar este PIN assim que for criado, quer num gestor de senhas fiável, quer num suporte físico separado, dependendo da sua estratégia. Neste último caso, certifique-se de que nunca mantém o suporte que contém o PIN no mesmo local que o seu Seedkeeper, caso contrário a proteção tornar-se-á ineficaz. É importante ter uma cópia de segurança: **Sem este PIN, não conseguirá aceder ao seu seed e os seus bitcoins perder-se-ão**.



![Image](assets/fr/20.webp)



Pode então definir um `Rótulo` associado à sua frase mnemónica. Esta etiqueta é útil se armazenar vários segredos no Seedkeeper, para que os possa identificar facilmente.



![Image](assets/fr/21.webp)



A sua frase mnemónica está agora guardada no smartcard.



![Image](assets/fr/22.webp)



Em termos de estratégia de segurança, são possíveis várias abordagens, dependendo das suas necessidades e do nível de exposição ao risco. Pessoalmente, recomendo que mantenha pelo menos 2 cópias do seu seed:




- Trata-se de uma novidade para os cartões inteligentes, que pode manter facilmente acessíveis para operações quotidianas, como a verificação de endereços ou a assinatura de transacções. Este método é prático (como veremos na parte 5) e permanece seguro graças à proteção oferecida pelo código PIN, pelo que pode mantê-lo acessível sem grandes riscos;
- Uma segunda cópia da sua frase mnemónica não encriptada, que serve de cópia de segurança definitiva da sua carteira, a ser utilizada apenas em caso de perda ou roubo do Seedkeeper. Como esta versão não está encriptada, deve ser guardada num local separado e mais seguro, para evitar o comprometimento simultâneo das duas cópias de segurança.



Dependendo da sua estratégia de proteção e perfil de risco, pode também duplicar o seed em vários Seedkeepers diferentes ou criar várias cópias físicas da mnemónica. Para saber mais sobre estas práticas, consulte o seguinte tutorial:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Carregamento de um seed do Seedkeeper



![video](https://youtu.be/ms0Iq_IyaoE)



Agora pode usar o seu Seedkeeper para carregar a sua frase mnemónica no SeedSigner no arranque, e assim assinar as suas transacções Bitcoin. Para começar, ligue seu SeedSigner conectando-o, e então abra o menu `Sementes`.



![Image](assets/fr/23.webp)



Em seguida, selecione a opção `From SeedKeeper`.



![Image](assets/fr/24.webp)



Insira o seu Seedkeeper no leitor de cartões inteligentes e introduza o seu código PIN para o desbloquear. Confirme a sua entrada premindo o botão de confirmação no canto inferior direito, `KEY3`.



![Image](assets/fr/25.webp)



O Seedkeeper pode conter vários segredos, pelo que o SeedSigner pede-lhe que escolha aquele que pretende carregar. A etiqueta apresentada corresponde ao nome definido no passo 4. Se, como no meu caso, só tiver registado um seed, só estará disponível uma opção.



![Image](assets/fr/26.webp)



O seu seed está agora carregado. Verifique se este é o wallet correto, comparando a impressão digital apresentada no ecrã com a especificada nas definições do Sparrow Wallet. Esta impressão digital também foi fornecida quando o wallet foi criado pela primeira vez.



Se estiver a utilizar um passphrase, pode aplicá-lo nesta fase (ver parte 6 deste tutorial). Caso contrário, basta clicar em `Fazer`.



![Image](assets/fr/27.webp)



Pode então utilizar o seu wallet como habitualmente: verificar os seus endereços de entrega e assinar transacções, tal como com um SeedSigner clássico. Para saber mais sobre como o utilizar, consulte o tutorial dedicado :



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Utilização do Seedkeeper com um passphrase BIP39



Está a utilizar um passphrase para proteger a sua carteira Bitcoin? Pode também registá-lo no seu Seedkeeper, juntamente com o seu seed. Esta solução permitir-lhe-á carregar rapidamente o seu wallet no SeedSigner, sem ter de introduzir manualmente o passphrase no pequeno teclado de cada vez que o utiliza.



Considero este método particularmente interessante, pois permite-lhe beneficiar das vantagens de segurança do passphrase, ao mesmo tempo que elimina os constrangimentos associados à sua utilização quotidiana. Aqui está um exemplo de uma configuração que eu recomendaria:




- Mantenha o seu seed e passphrase num Seedkeeper, protegido por um código PIN forte (isto é importante). Esta cópia de segurança permitir-lhe-á utilizar facilmente o seu wallet no dia a dia. Se desejar, pode duplicar esta informação num segundo Seedkeeper;
- Guarde também uma cópia clara da sua mnemónica e do passphrase, em papel ou metal. Esta é a sua cópia de segurança de último recurso, caso perca o seu Seedkeeper ou o seu PIN. Certifique-se de que guarda estas cópias em locais separados, para que não possam ser comprometidas em simultâneo.



Nesta configuração, se alguém puser as mãos apenas na sua mnemónica em texto simples, não conseguirá roubar nada sem conhecer o passphrase (desde que, claro, seja suficientemente forte para resistir a um ataque de força bruta). Por outro lado, se alguém descobrir o seu passphrase em texto simples, este permanecerá inutilizável sem a frase mnemónica correspondente.



Finalmente, se alguém conseguir aceder fisicamente ao seu Seedkeeper com o seed e o passphrase, não conseguirá extrair nada sem conhecer o código PIN. Ao contrário do passphrase, este código não pode ser forçado, uma vez que o smartcard se bloqueia automaticamente após 5 tentativas inválidas.



A segurança desta configuração baseia-se, por conseguinte, em dois pontos essenciais:




- Um **passphrase strong**: deve ser longo, aleatório e conter uma grande variedade de caracteres. A sua complexidade não é um problema para si, uma vez que só terá de o introduzir uma vez no teclado durante a inicialização; depois, será transmitido pelo Seedkeeper ;
- Um **código PIN forte** para o Seedkeeper: também aleatório e composto por 16 caracteres.



Para fazer esta configuração, comece por carregar o seu passphrase no SeedSigner da forma habitual. Pode seguir o procedimento detalhado neste tutorial:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Uma vez que a sua carteira com o passphrase tenha sido corretamente carregada no SeedSigner, abra o menu `Sementes` e selecione a área de cobertura correspondente a esta carteira. Note que esta pegada é diferente da pegada da carteira sem passphrase.



![Image](assets/fr/28.webp)



Em seguida, clique em `Backup Seed`, insira o Seedkeeper na unidade e selecione `To SeedKeeper`.



![Image](assets/fr/29.webp)



Introduza o seu PIN para desbloquear o Seedkeeper e, em seguida, atribua uma etiqueta a este segredo. Pode deixar a impressão digital como etiqueta para manter alguma forma de negação plausível, ou declarar explicitamente `Passphrase Wallet`, por exemplo.



![Image](assets/fr/30.webp)



A sua carteira passphrase está agora registada no Seedkeeper.



![Image](assets/fr/31.webp)



Da próxima vez que iniciar, basta inserir o Seedkeeper na unidade e navegar para `Sementes > Do SeedKeeper`.



![Image](assets/fr/32.webp)



Introduza o seu PIN para desbloquear o smartcard e, em seguida, selecione o wallet correspondente ao seu passphrase.



![Image](assets/fr/33.webp)



Verifique o passphrase e a impressão do wallet e, em seguida, confirme.



![Image](assets/fr/34.webp)



Pode agora aceder à sua carteira com o passphrase e assinar as suas transacções como faria normalmente com um SeedSigner.



## 7. Opções adicionais



No menu `Ferramentas > Ferramentas Smartcard`, encontrará várias opções para gerir o seu Seedkeeper:





- No menu `Ferramentas comuns`, pode :
 - Verificar a autenticidade do cartão;
 - Alterar o código PIN ;
 - Alterar as etiquetas associadas aos seus segredos ;
 - Desativar a função NFC (recomendado se utilizar apenas o leitor de chips) ;
 - Efetuar uma reposição de fábrica.





- No menu `Funções do Guarda-Semente`, é possível :
 - Consultar a lista dos segredos registados ;
 - Guardar um novo segredo ;
 - Eliminar um segredo existente ;
 - Guardar ou carregar os seus descritores (função útil para as carteiras multi-sig).





- No menu `Ferramentas DIY`, pode :
 - Compilação do applet Seedkeeper ;
 - Instalar o applet num cartão em branco ;
 - Eliminar um applet Seedkeeper para o repor e torná-lo novamente em branco.



Agora já sabe como utilizar o Seedkeeper para fazer uma cópia de segurança da sua carteira em combinação com o SeedSigner.



Se esta configuração o convenceu, não hesite em apoiar os projectos que a tornam possível:




- Comprando o seu equipamento diretamente [no sítio Web da Satochip] (https://satochip.io/shop/);
- Fazendo [um donativo para o projeto SeedSigner] (https://seedsigner.com/donate/);
- Subscrevendo o [canal YouTube do Crypto Guide](https://www.youtube.com/@CryptoGuide/), gerido pela pessoa que mantém o repositório GitHub que aloja o firmware modificado.