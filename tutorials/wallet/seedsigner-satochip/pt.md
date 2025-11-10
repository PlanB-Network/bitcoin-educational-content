---
name: Satochip x SeedSigner
description: Como utilizar um Satochip com o seu SeedSigner?
---

![cover](assets/cover.webp)



*Agradecimentos a [Crypto Guide](https://www.youtube.com/@CryptoGuide/) pelo seu fork do firmware SeedSigner para suporte de smartcard, que usaremos neste tutorial



---

O Satochip é um hardware em formato de cartão inteligente wallet com um elemento de segurança certificado EAL6+, um dos mais elevados padrões de segurança. Foi concebido e produzido pela empresa belga com o mesmo nome: Satochip.



Com um preço de cerca de 25 euros, o Satochip destaca-se da concorrência pela sua excelente relação qualidade/preço. Graças ao seu chip seguro, oferece resistência a ataques físicos. Além disso, o código-fonte da sua aplicação é inteiramente de código aberto, licenciado sob *AGPLv3*.



Por outro lado, o seu formato impõe certas limitações funcionais. O principal inconveniente do Satochip é a ausência de um ecrã integrado: os utilizadores devem, por conseguinte, assinar as transacções às cegas, baseando-se unicamente no ecrã do seu computador.



Para ultrapassar esta fraqueza, uma configuração particularmente interessante consiste em utilizá-lo em conjunto com um SeedSigner. Nesta configuração, a comunicação já não se faz diretamente entre o computador e o Satochip, mas através de trocas de códigos QR entre o computador e o SeedSigner. O SeedSigner funciona então como um ecrã de confiança: apresenta a informação a ser assinada, enquanto a assinatura propriamente dita é realizada pelo Satochip. Ao contrário do uso convencional do SeedSigner (ou mesmo do uso em combinação com o Seedkeeper), o seed nunca é carregado no SeedSigner. O SeedSigner torna-se assim o ecrã do Satochip, eliminando os riscos associados à assinatura cega.



Se olharmos para o problema de outra forma, a utilização do SeedSigner com um Satochip preenche uma lacuna importante do SeedSigner: a capacidade de armazenar e utilizar o seed num secure element.



Na minha opinião, esta configuração oferece várias vantagens em relação às carteiras de hardware convencionais:




- O Satochip custa cerca de 25 euros e, uma vez que o applet é de código aberto, pode instalá-lo num smartcard vazio. Em seguida, é necessário adicionar o custo dos componentes do SeedSigner e da extensão para leitura de cartões inteligentes: dependendo de onde comprar este hardware, o total deverá situar-se entre 70 e 100 euros.
- Todo o software envolvido na configuração é de código aberto: o firmware do SeedSigner e o applet Satochip.
- Beneficia de um elemento de segurança certificado.
- A configuração pode ser efectuada inteiramente em regime de bricolage, sem recurso a hardware explicitamente destinado à utilização de Bitcoin, o que pode constituir uma forma de negação plausível e de resistência a certas ameaças externas (incluindo, dependendo do país, pressões estatais). Esta é também uma solução interessante se o acesso a carteiras de hardware comerciais for restrito ou impossível na sua região.




## 1. Materiais necessários



Para efetuar esta configuração, são necessários os seguintes elementos




- O equipamento habitual necessário para um SeedSigner clássico :
 - um Raspberry Pi Zero com pinos GPIO,
 - 1.ecrã Waveshare de 3",
 - uma câmara compatível,
 - um cartão microSD.



![Image](assets/fr/01.webp)





- O kit de extensão SeedSigner, disponível [na loja oficial Satochip](https://satochip.io/product/seedsigner-extension-kit/), que permite ler e escrever num smartcard diretamente a partir do seu SeedSigner. Outra opção é usar [um leitor de smartcard externo](https://satochip.io/product/chip-card-reader/), que pode ser conectado por cabo a uma porta Micro-USB no Raspberry Pi. No entanto, eu próprio não testei esta solução;
- [Um Satochip](https://satochip.io/product/satochip/), ou em alternativa um [blank smartcard](https://satochip.io/product/card-for-diy-project/) no qual instalar a applet Satochip (o kit de extensão vendido pela Satochip já inclui um blank smartcard). O kit de extensão da Satochip também suporta o formato [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/). Assim, se preferir, pode optar por este formato.



![Image](assets/fr/02.webp)



Para mais detalhes sobre o equipamento necessário para montar um SeedSigner, consulte a Parte 1 deste outro tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Instalar o firmware



Para utilizar o seu SeedSigner com um Satochip, é necessário instalar um firmware alternativo, diferente do original do SeedSigner, para suportar a leitura de cartões inteligentes. Para isso, [recomendo usar o fork da "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Descarregue [a última versão da imagem](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) correspondente ao modelo de Raspberry Pi que está a usar.



![Image](assets/fr/03.webp)



Se ainda não o tiver, descarregue o software [Balena Etcher] (https://etcher.balena.io/) e proceda da seguinte forma:




- Insira o cartão microSD no seu computador;
- Lançador ;
- Selecione o ficheiro `.zip` que acabou de descarregar;
- Selecione o cartão microSD como destino;
- Clique em `Flash!`.



![Image](assets/fr/04.webp)



Aguarde até que o processo esteja concluído: o seu microSD está agora pronto a ser utilizado. Pode agora passar à montagem do seu dispositivo.



Para mais pormenores sobre a instalação do firmware e a verificação do software (um passo que recomendo vivamente), consulte o seguinte tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Montagem do leitor de cartões inteligentes



Comece por instalar a câmara no Raspberry Pi Zero, inserindo-a cuidadosamente no pino da câmara e fixando-a com a patilha preta. Em seguida, coloque o Pi na parte inferior da caixa, certificando-se de que alinha as portas com as aberturas correspondentes.



![Image](assets/fr/05.webp)



De seguida, ligue o leitor de cartões inteligentes aos pinos GPIO do Raspberry Pi Zero.



![Image](assets/fr/06.webp)



Faça deslizar a tampa de plástico sobre o leitor de cartões inteligentes até ficar corretamente posicionada.



![Image](assets/fr/07.webp)



Em seguida, adicione o ecrã aos pinos GPIO da extensão.



![Image](assets/fr/08.webp)



Por fim, insira o cartão microSD que contém o firmware na porta lateral do Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Agora pode ligar o seu SeedSigner através da porta Micro-USB do Raspberry Pi Zero, ou através da porta USB-C da extensão. Ambas as opções funcionam. Aguarde alguns segundos para a inicialização, então você deve ver a tela de boas-vindas aparecer.



![Image](assets/fr/10.webp)



Para mais detalhes sobre a configuração inicial do seu SeedSigner, recomendo que consulte a parte 4 do seguinte tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Flash de um smartcard com o applet Satochip (opcional)



Se já tem um Satochip, pode saltar este passo e ir diretamente para o passo 4. Nesta secção, veremos como instalar a applet Satochip num smartcard em branco (método DIY). A applet é simplesmente um pequeno programa que corre no smartcard e que nos permite gerir funções específicas.



Para começar, abra o menu `Ferramentas > Ferramentas de Smartcard` no seu SeedSigner.



![Image](assets/fr/11.webp)



Em seguida, selecione `Ferramentas DIY > Instalar Applet`.



![Image](assets/fr/12.webp)



Insira o seu smartcard no leitor SeedSigner, com o chip virado para baixo, e selecione a aplicação `Satochip`.



![Image](assets/fr/13.webp)



Seja paciente durante a instalação: o processo pode demorar algumas dezenas de segundos.



![Image](assets/fr/14.webp)



Quando o applet tiver sido instalado com sucesso, pode avançar para o passo 4.



![Image](assets/fr/15.webp)




## 5. Criar e guardar o seed



### 5.1. Gerar seed



Agora que tem todo o seu hardware e software a funcionar corretamente, pode proceder à criação da sua carteira Bitcoin. Para o fazer, ligue o seu SeedSigner e, em seguida, generate o seu seed como com um SeedSigner convencional, quer lançando os dados ou tirando uma fotografia:




- Vá ao menu `Ferramentas > Câmara / Lance de dados`;
- De seguida, siga o processo de geração de entropia de acordo com o método escolhido;
- Por fim, faça uma cópia de segurança do seed num suporte físico e verifique-a cuidadosamente.



![Image](assets/fr/16.webp)



Se pretender ver os pormenores deste procedimento, siga a parte 5 deste tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Guardar o seed num Guardião de Sementes



Uma vez que o seed tenha sido gerado, esta é a única vez que ele reside na RAM do SeedSigner. No meu caso, quero guardá-lo num [Seedkeeper](https://satochip.io/product/seedkeeper/), outro produto Satochip concebido para guardar segredos. Vou usar este dispositivo como último recurso, em caso de perda do meu Satochip.



A estratégia de cópia de segurança escolhida aqui depende das suas preferências, mas é imperativo ter pelo menos uma cópia da sua frase mnemónica, seja em suporte físico (papel ou metal) ou, como aqui, num Seedkeeper. Também pode multiplicar o número de cópias de segurança conforme necessário. Para mais informações sobre estratégias de backup de portefólio, sugiro que leia este tutorial :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Para fazer uma cópia de segurança do seu seed num Seedkeeper, vá diretamente para o menu `Backup Seed`.



![Image](assets/fr/17.webp)



Em seguida, insira o seu Seedkeeper no leitor de cartões inteligentes e selecione `To SeedKeeper`.



![Image](assets/fr/18.webp)



Introduza o seu PIN para o desbloquear.



![Image](assets/fr/19.webp)



Escolha um `Rótulo` para identificar facilmente os seus diferentes segredos armazenados no Seedkeeper. Pode, por exemplo, simplesmente manter a marca wallet ou indicar explicitamente `Seed`. A escolha depende da sua preferência e risco.



![Image](assets/fr/20.webp)



Se a sua estratégia de cópia de segurança depende apenas deste Seedkeeper, recomendo vivamente que execute um teste de recuperação vazio agora e, em seguida, compare as impressões digitais para verificar se a cópia de segurança está a funcionar.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

O código PIN do Seedkeeper deve ser tão longo e aleatório quanto possível, para evitar tentativas de força bruta em caso de comprometimento físico do cartão. Também deve manter uma cópia de segurança deste código PIN, armazenada num local separado do Seedkeeper. Sem este PIN, não será possível aceder à mnemónica armazenada no Seedkeeper e os seus bitcoins ficarão permanentemente perdidos.



### 5.3. Guardar o seed no Satochip



Agora que o seu portefólio foi gerado, guardado e verificado, vamos transferi-lo para o Satochip. Para fazer isso, certifique-se de que o seed está carregado na memória RAM do SeedSigner. Em seguida, vá para `Ferramentas > Ferramentas do Smartcard > Funções do Satochip`.



![Image](assets/fr/21.webp)



Insira o seu Satochip no leitor de cartões inteligentes e selecione `Inicializar com Seed`.



![Image](assets/fr/22.webp)



O aparelho pede-lhe para introduzir o código PIN Satochip; como o cartão é novo e não está inicializado, ainda não existe PIN. Introduza um código qualquer para saltar este passo (não se trata de um código de bloqueio).



![Image](assets/fr/23.webp)



O SeedSigner detecta que o seu Satochip não foi inicializado. Clique em `Eu entendo` para confirmar.



![Image](assets/fr/24.webp)



Pode então definir o código PIN Satochip, de 4 a 16 caracteres. Para reforçar a segurança do seu wallet, escolha um código longo e aleatório: é a única proteção contra o acesso físico à sua frase mnemónica.



Lembre-se de guardar este PIN assim que for criado, seja num gestor de senhas seguro ou num suporte físico, dependendo da sua estratégia pessoal. Neste último caso, certifique-se de que nunca guarda o suporte que contém o PIN no mesmo local que o seu Satochip, caso contrário a proteção tornar-se-á inútil. É importante ter uma cópia de segurança: **Sem este PIN, não conseguirá aceder ao seu seed e os seus bitcoins ficarão perdidos para sempre**.



![Image](assets/fr/25.webp)



O SeedSigner pergunta-lhe então qual o seed a importar para o Satochip. Selecione aquele cuja impressão digital corresponda à carteira que acabou de criar.



![Image](assets/fr/26.webp)



O seu seed é agora importado para o Satochip.



![Image](assets/fr/27.webp)



Pode agora desligar o seu SeedSigner.



Se pretender utilizar um passphrase BIP39 para reforçar a segurança do seu wallet, consulte a parte 6 deste tutorial:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Importar o wallet para o Sparrow



Agora que a sua carteira está a funcionar, importaremos a sua informação pública (o "*keystore*") para o Sparrow Wallet ou outro software de gestão de carteiras. Este software será utilizado para criar, distribuir e acompanhar as suas transacções. No entanto, não será capaz de as assinar, uma vez que apenas o Satochip (e quaisquer cópias de segurança) possui as chaves privadas necessárias para esta operação.



### 6.1 Preparação do SeedSigner e do Satochip



Insira o cartão microSD que contém o sistema operativo e, em seguida, ligue o seu SeedSigner. De momento, ele não pode fazer nada, pois ainda não conhece o seu seed. É preciso começar por inserir o Satochip no leitor de cartões inteligentes, pois é nele que se encontra o seed.



A partir do ecrã inicial, aceda ao menu `Ferramentas > Ferramentas Smartcard > Funções Satochip`.



![Image](assets/fr/28.webp)



Em seguida, clique em `Exportar Xpub`.



![Image](assets/fr/29.webp)



Selecione o tipo de carteira. No nosso caso, trata-se de uma carteira única: selecione `Single Sig`.



![Image](assets/fr/30.webp)



A seguir vem a escolha do padrão de scripting. Escolha o mais recente: `Native SegWit`.



![Image](assets/fr/31.webp)



Por fim, selecione o `Coordenador`, ou seja, o software de gestão de carteiras que pretende utilizar. Neste caso, vamos utilizar o Sparrow Wallet.



![Image](assets/fr/32.webp)



Aparece uma mensagem de aviso: isto é perfeitamente normal. A chave pública alargada (`xpub`) permite-lhe ver todos os endereços derivados do seu seed (na primeira conta). Não dá, no entanto, acesso aos seus fundos: a sua divulgação comprometeria a sua privacidade, mas não a segurança dos seus bitcoins. Por outras palavras, permite-lhe observar os seus saldos, mas não gastá-los.



Clique em "Compreendo".



![Image](assets/fr/33.webp)



De seguida, introduza o código PIN do seu Satochip para o desbloquear. Este é o código que definiu e guardou na etapa 5.



![Image](assets/fr/34.webp)



Por fim, clique em `Export Xpub` se estiver satisfeito com as informações apresentadas.



![Image](assets/fr/35.webp)



O SeedSigner gera então o seu xpub sob a forma de um código QR dinâmico, contendo todos os dados de que necessita para gerir a sua carteira no Sparrow Wallet. É possível regular a luminosidade do ecrã com o joystick para facilitar a leitura do código QR.



### 6.2 Importação de um novo portefólio para o Sparrow Wallet



Certifique-se de que o software Sparrow Wallet está instalado no seu computador. Se não sabe como descarregá-lo, verificar a sua autenticidade e instalá-lo corretamente, consulte o nosso tutorial completo sobre o assunto:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

No seu computador, abra o Sparrow Wallet e, em seguida, na barra de menu, clique em `File → Import Wallet`.



![Image](assets/fr/36.webp)



Desça até `SeedSigner`, depois selecione `Scan...`. A sua webcam será activada: digitalize o código QR dinâmico apresentado no ecrã do SeedSigner.



![Image](assets/fr/37.webp)



Atribua um nome ao seu portfólio e, em seguida, clique em `Criar Wallet`. O Sparrow pedir-lhe-á então para definir uma palavra-passe para bloquear o acesso local a este wallet. Escolha uma palavra-passe forte: ela protege os seus dados no Sparrow (chaves públicas, endereços, etiquetas e histórico de transacções). No entanto, esta palavra-passe não é necessária para restaurar o wallet no futuro: apenas a sua frase mnemónica (e possivelmente o seu passphrase) o será.



Recomendo que guarde esta palavra-passe num gestor de palavras-passe, para evitar perdê-la.



![Image](assets/fr/38.webp)



O seu registo de chaves foi importado com sucesso.



![Image](assets/fr/39.webp)



Verifique agora se a `Master fingerprint` apresentada em Sparrow Wallet corresponde à anteriormente encontrada no seu SeedSigner.



O SeedSigner pedir-lhe-á então que digitalize um endereço de receção aleatório do seu Sparrow wallet para confirmar a validade da importação.



![Image](assets/fr/40.webp)



O seu Satochip (via SeedSigner) e o Sparrow Wallet estão agora ligados de forma segura. O Sparrow actua como uma interface de gestão completa, enquanto o Satochip continua a ser o único dispositivo capaz de assinar as suas transacções. Está agora pronto para receber e enviar bitcoins numa configuração totalmente air-gapped.



![Image](assets/fr/41.webp)



## 7. Receber e enviar bitcoins



O seu Satochip e o Sparrow Wallet estão agora configurados para trabalhar em conjunto. Nesta secção, explicaremos passo a passo como receber e enviar bitcoins neste modo.



### 7.1 Receber bitcoins



#### 7.1.1 Gerar um endereço de receção



No seu computador, abra o Sparrow Wallet e desbloqueie o seu `Satochip-SeedSigner` wallet utilizando a sua palavra-passe. Verifique se o software está ligado a um servidor (indicador no canto inferior direito). Em seguida, na barra lateral, clique em `Receive`.



![Image](assets/fr/42.webp)



Aparece um novo endereço Bitcoin. Encontrará :




- O endereço em formato de texto (começando por `bc1q...` se estiver a utilizar o P2WPKH, como neste exemplo) ;
- O código QR associado ;
- Um campo `Label`, útil para rastrear as suas transacções.



Recomendo vivamente que adicione uma etiqueta a cada recibo de bitcoin no seu wallet. Isto ajudá-lo-á a identificar facilmente a proveniência de cada UTXO e a gerir melhor a sua privacidade. Para saber mais sobre este importante assunto, consulte a formação dedicada na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Para adicionar uma etiqueta, basta introduzir um nome no campo `Rótulo` e confirmar.



Por exemplo:



```txt
Label : Sale of the Raspberry Pi Zero
```



O seu endereço está agora associado a esta etiqueta em todas as secções do Sparrow.



![Image](assets/fr/43.webp)



#### 7.1.2 Verificação do Address no SeedSigner



Antes de comunicar o seu endereço de receção ao ordenante, é importante verificar se este pertence ao seu seed. Esta etapa garante que o seu Satochip poderá então assinar as transacções associadas a este endereço. Também evita potenciais ataques em que o Sparrow apresentaria um endereço fraudulento. Tenha em mente que o Sparrow roda num ambiente inseguro (seu computador), cuja superfície de ataque é muito maior do que a do seu Satochip, que é totalmente isolado. É por isso que nunca deve confiar cegamente nos endereços apresentados no Sparrow antes de os verificar no seu hardware wallet.



No Sparrow, clique no código QR do endereço para o ampliar: será então apresentado em ecrã completo.



![Image](assets/fr/44.webp)



No seu SeedSigner, insira o Satochip no leitor, depois no menu principal, selecione `Scan`. Digitalize o código QR exibido no seu computador, depois selecione `Utilizar cartão Satochip`.



![Image](assets/fr/45.webp)



Em seguida, confirme o tipo de script utilizado (neste caso, `Native SegWit`), introduza o código PIN do Satochip para o desbloquear e valide a informação `xpub`.



![Image](assets/fr/46.webp)



Se o endereço digitalizado corresponder ao endereço derivado do seu seed, o SeedSigner apresentará a mensagem: `Address Verificado`.



![Image](assets/fr/47.webp)



Assim, pode ter a certeza de que o endereço pertence à sua carteira.



#### 7.1.3 Receção de fundos



Pode agora transmitir este endereço sob a forma de texto ou através do seu código QR à pessoa ou departamento que precisa de lhe enviar satss. Uma vez transmitida a transação na rede, esta aparecerá no separador "Transacções" do Sparrow Wallet.



![Image](assets/fr/48.webp)



### 7.2 Enviar bitcoins



O envio de bitcoins com a configuração Satochip-SeedSigner envolve 3 passos:




- Criação de transacções no Sparrow ;
- Assinatura desta transação no Satochip, através do SeedSigner ;
- Finalmente, a transação é transmitida pela rede a partir do Sparrow.



Todos os intercâmbios entre os dois dispositivos são efectuados exclusivamente através de códigos QR.



#### 7.2.1 Criar a transação no Sparrow



No Sparrow Wallet, é possível criar uma transação clicando no separador "Enviar" na barra lateral esquerda. No entanto, prefiro utilizar o separador `UTXOs`, que permite praticar o *Controlo Coin*. Este método oferece um controlo preciso sobre os UTXOs gastos, para limitar a informação revelada durante as suas transacções.



No separador "UTXOs", selecione as moedas que pretende gastar e clique em "Enviar selecionados".



![Image](assets/fr/49.webp)



Em seguida, preencha os campos da transação:




- Em `Pagar a`, cole o endereço do destinatário ou digitalize o seu código QR utilizando o ícone da câmara ;
- Em `Label`, adicione uma etiqueta para rastrear esta despesa;
- Em `Montante`, introduza o montante a enviar;
- Finalmente, escolha a taxa de carregamento de acordo com as condições actuais da rede (as estimativas estão disponíveis em [mempool.space](https://mempool.space/)).



Depois de preencher todos os campos, reveja cuidadosamente as informações e clique em `Criar transação >>`.



![Image](assets/fr/50.webp)



Verifique uma última vez a exatidão dos detalhes da transação e, em seguida, clique em `Finalizar transação para assinatura`.



![Image](assets/fr/51.webp)



A transação está agora pronta, mas ainda não foi assinada. Para visualizar o [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) como um código QR, clique em `Mostrar QR`.



![Image](assets/fr/52.webp)



#### 7.2.2 Assinatura da transação com a Satochip



Ligue o seu SeedSigner e insira o seu Satochip como de costume. A partir do ecrã inicial, selecione `Scan`, depois digitalize o código QR apresentado no Sparrow.



![Image](assets/fr/53.webp)



Selecione a opção "Utilizar cartão Satochip".



![Image](assets/fr/54.webp)



Introduza o seu código PIN para desbloquear o smartcard.



![Image](assets/fr/55.webp)



O SeedSigner detecta que se trata de um PSBT e apresenta um resumo da transação:




   - O montante enviado,
   - Endereços de destino,
   - Custos de transação associados.



Clique em `Review Details` e examine todas as informações diretamente no ecrã do SeedSigner. Os pontos mais importantes a verificar são os montantes enviados, os endereços de destino e as taxas de transação.



![Image](assets/fr/56.webp)



Se tudo estiver em ordem, selecione `Approve PSBT` para assinar a transação utilizando o Satochip.



![Image](assets/fr/57.webp)



Uma vez concluída a assinatura, o SeedSigner gera um novo código QR contendo a transação assinada, pronto a ser digitalizado pelo Sparrow.



#### 7.2.3 Difusão da transação a partir do Sparrow



Agora que a transação está assinada e validada, tudo o que resta é transmiti-la na rede Bitcoin para que um mineiro a possa incluir num bloco. No Sparrow, clique em `Scan QR`.



![Image](assets/fr/58.webp)



Apresente o código QR exibido no seu SeedSigner (o que contém a transação assinada) à webcam. O Sparrow irá então mostrar todos os detalhes da transação. Verifique se todas as informações estão corretas e, em seguida, clique em "Broadcast Transaction" para transmiti-la na rede Bitcoin.



![Image](assets/fr/59.webp)



A sua transação é agora transmitida à rede. Pode seguir a sua confirmação no separador `Transacções` do Sparrow Wallet.



![Image](assets/fr/60.webp)



## 8. Recupere o seu wallet



Como vimos nas secções anteriores, dependendo da sua estratégia de segurança, existem várias formas de fazer cópias de segurança da sua frase de recuperação, para além do seu Satochip :




- Utilizar um *SeedQR* clássico com o SeedSigner ;
- Gravando a frase mnemónica num suporte físico;
- Ou armazenando-o num Seedkeeper, como explicado na secção 5.2.



Em qualquer caso, existem 2 situações principais em que é necessário intervir: perda do Satochip ou perda do SeedSigner. Vejamos como reagir em cada um destes cenários.



### 8.1. Recupere o seu wallet com o Satochip



Se ainda tiveres o teu Satochip mas o teu SeedSigner estiver avariado ou perdido, a situação é bastante simples de gerir, uma vez que o teu wallet ainda está no Satochip.



A melhor opção é recomendar os componentes necessários e reconstruir um novo SeedSigner a partir do zero. Como este é um dispositivo "sem estado", não importa se está a usar o mesmo ou outro SeedSigner: desde que possa inserir o seu Satochip, tudo funcionará normalmente.



Se não quiser reconstruir um, pode também utilizar o seu Satochip da forma clássica, ou seja, diretamente a partir do seu computador, sem passar pelo SeedSigner. Este método funciona perfeitamente, mas reduz consideravelmente a segurança do seu Bitcoin wallet: perde o isolamento "*air-gapped*" e deve agora assinar às cegas, uma vez que o SeedSigner actuava como um ecrã de confiança. No entanto, esta pode ser uma solução temporária numa emergência, ou se não for possível reconstruir um SeedSigner.



Para o fazer, é necessário um leitor de cartões inteligentes USB ou NFC. Abra o wallet que pretende restaurar no Sparrow, aceda ao separador "Definições" e clique em "Substituir".



![Image](assets/fr/61.webp)



Insira o seu Satochip no leitor de cartões inteligentes ligado ao computador e, em seguida, clique em `Importar` ao lado de `Satochip`.



![Image](assets/fr/62.webp)



Por fim, introduza o PIN do seu smartcard para o desbloquear. Poderá então aceder ao seu wallet, criar transacções e assiná-las diretamente utilizando o Satochip ligado.



### 8.2. Recupere a sua carteira com o SeedSigner



O outro cenário, mais delicado, é quando perde o acesso ao seu Satochip que contém o seed: quer esteja avariado, perdido, roubado ou se tenha esquecido do seu código PIN. Se o seu Satochip foi roubado ou extraviado, recomendamos vivamente que, uma vez restaurado o acesso aos seus fundos, transfira imediatamente os seus bitcoins para um novo wallet, gerado com um seed diferente. Isto garante que um potencial atacante nunca poderá ter acesso ao seu satss.



Para recuperar o acesso à sua carteira e movimentar os seus fundos, basta carregar o seu seed no SeedSigner. Dependendo do suporte de backup que utilizou, tem várias opções:





- Introduzir manualmente a frase mnemónica no menu `Sementes > Introduzir 12 palavras seed`.



![Image](assets/fr/63.webp)





- Digitalize o seu *SeedQR* clicando no botão `Digitalizar` na página inicial.



![Image](assets/fr/64.webp)





- Ou carregue seu seed de um Seedkeeper, através do menu `Seeds > From SeedKeeper` (este é o método que estou usando neste tutorial). Basta introduzir o PIN do Seedkeeper e selecionar o segredo a ser utilizado como seed no SeedSigner.



![Image](assets/fr/65.webp)



Uma vez que o seed tenha sido carregado no SeedSigner, qualquer que seja o método utilizado, será possível assinar uma ou mais transacções de digitalização para mover os seus bitcoins para um novo wallet não comprometido. Para saber como fazer isso, consulte a parte 7.2 do seguinte tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Agora já sabe como utilizar o Satochip para gerir a sua carteira Bitcoin de forma segura em combinação com o SeedSigner.



Se esta configuração o convenceu, não hesite em apoiar os projectos que a tornam possível:




- Comprando o seu equipamento diretamente [no sítio Web da Satochip] (https://satochip.io/shop/);
- Fazendo [um donativo para o projeto SeedSigner] (https://seedsigner.com/donate/);
- Subscrevendo o [canal YouTube do Crypto Guide](https://www.youtube.com/@CryptoGuide/), gerido pela pessoa que mantém o repositório GitHub que aloja o firmware modificado que utilizámos neste tutorial.