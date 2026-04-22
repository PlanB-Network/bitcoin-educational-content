---
name: COLDCARD Mk4
description: Um guia para configurar e utilizar um COLDCARD Mk4 com Sparrow Wallet
---

![cover-mk4](assets/cover.webp)


*os *Hardware wallets** são dispositivos físicos feitos apenas para armazenar a chave privada do Bitcoin de forma segura. Armazenam as chaves privadas offline, o que significa que os hackers não podem aceder a elas através da Internet. Enquanto os **software wallets** são utilizados principalmente para transacções diárias, os **hardware wallets** são frequentemente utilizados para armazenar grandes quantidades de bitcoins de forma segura durante um longo período de tempo. Ao efetuar uma transação Bitcoin utilizando **hardware wallets**, o wallet pode assinar as transacções dentro do dispositivo, pelo que a chave privada nunca é exposta a ambientes ligados à Internet.


Neste tutorial, vamos explorar um dos mais populares wallets de hardware produzidos pela Coinkite, o Coldcard Mk4. Vamos ver como configurar e usar este wallet de hardware para realizar transacções Bitcoin.


## Visão geral do Coldcard Mk4


O Coldcard Mk4 é um hardware Bitcoin apenas para wallet fabricado pela Coinkite. Este dispositivo está equipado com um ecrã, um teclado numérico e uma tampa protetora deslizante. Além disso, o dispositivo oferece várias formas de ligação e interação, incluindo USB-C, funcionamento com ar comprimido utilizando um cartão MicroSD, NFC e um modo de disco virtual. O Mk4 também inclui funcionalidades de segurança avançadas, como o BIP39 passphrase e PINs de truque, dando aos utilizadores maior controlo e proteção sobre o seu Bitcoin.


## Configuração inicial: PIN e palavras anti-phishing


Para começar, o Coldcard Mk4 pode ser adquirido diretamente no [sítio Web do Coinkite] (https://store.coinkite.com/store). Os compradores também podem optar por pagar com moeda fiduciária ou Bitcoin. Para além disso, também é necessário um cartão MicroSD (4 GB é suficiente) e uma fonte de alimentação que possa ser ligada através de um cabo USB-C (o Coldcard Mk4 só tem uma porta de entrada de alimentação USB-C). Note-se que, uma vez que o Mk4 não tem uma bateria incorporada, tem de estar sempre ligado à fonte de alimentação enquanto estiver a ser utilizado.


Receberá o seu Mk4 num saco inviolável. Por favor, certifique-se de que o saco não foi comprometido. Se detectares algum problema, como danos ou rasgões no saco, podes informar o Coinkite enviando um e-mail para support@coinkite.com. Além disso, o saco inviolável contém um número de 12 algarismos, que designaremos por número do saco do Mk4. Este número de saco será utilizado mais tarde para verificar que o aparelho não foi adulterado durante o transporte e que provém diretamente do Coinkite. O número do saco é armazenado de forma segura no secure element do cartão Cold utilizando a memória flash OTP (One-Time-Programmable), o que significa que não pode ser alterado depois de programado. Quando liga o dispositivo pela primeira vez, o número apresentado no ecrã deve corresponder ao número do saco. Isto garante que o Mk4 que recebeu é o dispositivo original de fábrica e não foi substituído ou modificado. Embora esta verificação apenas confirme a integridade do dispositivo no momento da primeira ligação, o secure element continua a proteger as suas chaves privadas, PIN e passphrase, tornando extremamente difícil que qualquer adulteração comprometa o seu Bitcoin. Além disso, as boas práticas, como a proteção adequada dos dados relacionados com o wallet, serão benéficas para a segurança geral do próprio cartão Cold. Para obter mais informações, pode consultar este [artigo] (https://blog.coinkite.com/understanding-mk4-security-model/) que elabora o modelo de segurança do cartão Cold.


O teclado é composto por 10 botões numéricos, um botão OK (`✓`) e um botão cancelar (`✕`). Alguns botões numéricos também podem ser utilizados para navegação: `5` para navegar para cima (`^`), `7` para navegar para a esquerda (`<`), `8` para navegar para baixo `˅`, e `9` para navegar para a direita (`>`).


![01](assets/en/01.webp)


Se não houver problemas com a embalagem, pode abrir o saco. O Mk4 é fornecido com um cartão de segurança wallet que pode ser utilizado para guardar as informações relativas ao PIN do aparelho, às palavras anti-phishing e ao seedphrase. Siga os passos seguintes para a inicialização:


1. Prepare uma folha de papel e uma caneta.

2. Ligue o Mk4 a uma fonte de alimentação (cabo USB-C) e insira o cartão MicroSD.

3. Assim que o dispositivo for ligado pela primeira vez, o ecrã apresentará uma mensagem relativa aos Termos de Venda e Utilização do Coldcard. Navegue para baixo e, em seguida, prima `✓` para continuar.

4. Em seguida, é apresentado no ecrã um número de 12 dígitos. Compare este número com o que está no saco inviolável e com a cópia adicional do número do saco que foi incluída no saco inviolável para garantir que o dispositivo não foi adulterado. Se os números não coincidirem, contacte imediatamente a assistência do Coinkite antes de prosseguir. Caso contrário, prima `✓` para continuar.


![02](assets/en/02.webp)


5. Selecione "Escolher código PIN".

6. Navegue para baixo enquanto lê as instruções para avançar para o passo seguinte.


![03](assets/en/03.webp)


7. No Mk4, crie e introduza o prefixo PIN (deve ter 2 a 6 caracteres) e anote-o, depois prima `✓` para continuar.

8. Anote as duas palavras apresentadas no ecrã. Estas são as palavras anti-phishing. Prima `✓` para continuar.


![04](assets/en/04.webp)


9. Crie e introduza o sufixo do PIN (ou o resto do PIN, deve ter 2 a 6 caracteres) e anote-o. Prima `✓` para continuar.

10. Volte a introduzir o seu prefixo PIN. Prima `✓` para continuar.


![05](assets/en/05.webp)


11. Verifique se as palavras anti-phishing são as mesmas que escreveu no passo 8. Prima `✓` para continuar.

12. Volte a introduzir o sufixo do PIN (ou o resto do PIN). Prima `✓` para continuar.


![06](assets/en/06.webp)


13. O PIN e as palavras anti-phishing do seu Mk4 são agora criados e armazenados com sucesso pelo dispositivo.


![07](assets/en/07.webp)


Note que o Mk4 pedir-lhe-á sempre que introduza o seu PIN cada vez que ligar o aparelho. Sem este PIN, não é possível aceder ao seu Coldcard Mk4. Por isso, certifique-se de que cria uma cópia de segurança suficiente do PIN e das palavras anti-phishing.


## Configurar o Wallet


O passo seguinte é configurar o wallet. Existem três formas de o fazer:


- Criar um novo wallet (standard)
- Criar um novo wallet com lançamentos de dados
- Importação de um wallet


### Criar um novo wallet (standard)


Para criar um novo wallet, basta efetuar os seguintes passos.


1. Selecione `Novo Wallet` (ou `Novas palavras-semente`) > Selecione `12 palavras` ou `24 palavras (predefinição)`, consoante a sua preferência.


![08](assets/en/08.webp)


2. O dispositivo irá gerar 12 ou 24 palavras como seedphrase, consoante a sua escolha. Navegue para baixo enquanto escreve cuidadosamente cada palavra na ordem correta. Depois, prima `✓` para continuar.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. O aparelho pedir-lhe-á para verificar o seu seedphrase, colocando as perguntas numa ordem aleatória (por exemplo, `Palavra 1 é?`, depois `Palavra 5 é?`, depois `Palavra 12 é?`, e assim por diante) e haverá três opções de palavras para cada pergunta. Consulte a nota do Passo 2 e escolha as palavras corretamente (premindo `1`, `2` ou `3`, consoante o que corresponder à palavra correta) para completar a criação do wallet.


![09](assets/en/09.webp)


4. O Mk4 irá então perguntar se pretende Ativar NFC/Tap ou não. Por agora, selecione `✕` para esta opção. Isto pode ser alterado nas definições no futuro.

5. Por fim, o Mk4 também irá se quiser desativar a Porta USB (que pode ser utilizada para transferência de dados sem ar comprimido). Por agora, selecione `✓` para esta opção. Isto pode ser alterado nas definições no futuro.

6. O ecrã apresentará agora o menu principal com "Pronto a Assinar" no topo. Isto marca a conclusão do processo de criação do wallet.


![10](assets/en/10.webp)


### Criar um novo wallet com lançamento de dados


Em alternativa, também podes optar por gerar o novo seedphrase com entropia. Faz isso se não confias no seedphrase acabado de gerar do Mk4.


O procedimento no Coldcard Mk4 é o seguinte:


1. Selecionar `Novo Wallet` (ou `Novas palavras-semente`) > Selecionar `Rolo de dados de 12 palavras` ou `Rolo de dados de 24 palavras`, dependendo da sua preferência.

2. Ser-te-á pedido que introduzas os resultados dos teus lançamentos de dados. Cada lançamento de dados adiciona aleatoriedade ao processo de criação do wallet, assegurando que o seu seedphrase é gerado de uma forma totalmente segura e imprevisível. O número mínimo de lançamentos é de 50 para seedphrase de 12 palavras e 99 para seedphrase de 24 palavras. Prima `✓` depois de ter introduzido pelo menos 99 valores de lançamento de dados.


![11](assets/en/11.webp)


3. O dispositivo irá gerar 12 ou 24 palavras como seedphrase, consoante a sua escolha. Navegue para baixo enquanto escreve cuidadosamente cada palavra na ordem correta. Depois, prima `✓` para continuar.

4. O dispositivo pedir-lhe-á para verificar o seu seedphrase, colocando as perguntas numa ordem aleatória (por exemplo, `Palavra 1 é?`, depois `Palavra 5 é?`, depois `Palavra 12 é?`, e assim por diante) e haverá três opções de palavras para cada pergunta. Consulte a nota do Passo 3 e escolha as palavras corretamente (premindo `1`, `2` ou `3`, consoante o que corresponder à palavra correta) para completar a criação do wallet.


![12](assets/en/12.webp)


5. O Mk4 irá então perguntar se pretende Ativar NFC/Tap ou não. Por agora, selecione `✕` para esta opção. Isto pode ser alterado nas definições no futuro.

6. Por fim, o Mk4 também irá se quiser desativar a Porta USB (que pode ser utilizada para transferência de dados sem ar comprimido). Por agora, selecione `✓` para esta opção. Isto pode ser alterado nas definições no futuro.

7. O ecrã apresentará agora o menu principal com `Ready to Sign` no topo. Isto marca a conclusão do processo de criação do wallet.


![13](assets/en/13.webp)


### Importação de um wallet


A última opção é importar um wallet. Pode fazê-lo se pretender recuperar um wallet a partir de um seedphrase que já possui. Pode seguir estes passos:


1. Selecione `Importar existente`.

2. Selecione `24 Palavras`, `18 Palavras` ou `12 Palavras`, dependendo do número de palavras do seu seedphrase.


![14](assets/en/14.webp)


3. O Coldcard Mk4 perguntar-lhe-á então o que é cada palavra por ordem consecutiva. Para cada palavra, navegue para baixo ou para cima até encontrar o prefixo escrito para cada palavra. O aparelho vai reduzir as possibilidades até encontrar a palavra correta. Faça o mesmo para as restantes palavras.

4. Para a palavra final, o Coldcard Mk4 apresentará apenas uma quantidade limitada de palavras possíveis. Se não houver correspondências, poderá ter introduzido as palavras incorretamente. Caso contrário, selecione a palavra que corresponde à do seu seedphrase.


![15](assets/en/15.webp)


5. O Mk4 irá então perguntar se pretende Ativar NFC/Tap ou não. Por agora, selecione `✕` para esta opção. Isto pode ser alterado nas definições no futuro.

6. Por fim, o Mk4 também irá se quiser desativar a Porta USB (que pode ser utilizada para transferência de dados sem ar comprimido). Por agora, selecione `✓` para esta opção. Isto pode ser alterado nas definições no futuro.

7. O ecrã apresentará agora o menu principal com "Pronto a Assinar" no topo. Isto marca a conclusão do processo de criação do wallet.


![16](assets/en/16.webp)


Tenha em atenção que o seedphrase é o único acesso para recuperar o seu wallet. Cria uma cópia de segurança do teu seedphrase e guarda-a num local seguro. **Nem as tuas chaves, nem as tuas moedas**, quem tiver o teu seedphrase tem acesso aos teus bitcoins!


## Configurar o passphrase


Uma das melhores práticas no Bitcoin é utilizar um passphrase. O passphrase actua como a 13ª ou 25ª palavra para além do seedphrase. O que o torna diferente é o facto de poder escolher a frase que quiser, enquanto o seedphrase é selecionado a partir de uma lista pré-determinada de 2048 palavras. Por defeito, depois de configurar o seu wallet, começará com um wallet com um passphrase em branco. Para configurar um passphrase que não esteja em branco, basta efetuar os seguintes passos:


1. Ir para `Passphrase`.

2. Navegue para baixo para ler a descrição sobre o passphrase e, em seguida, prima `✓` para continuar.

3. Selecione `Editar Frase`.


![17](assets/en/17.webp)


4. Introduza o seu passphrase:


   - Prima `1` (letras), `2` (números) ou `3` (símbolos) para selecionar o tipo de caracteres.
   - Prima `4` para alternar entre letras minúsculas e maiúsculas (só pode ser utilizado quando se introduzem letras).
   - Navegue utilizando `^` ou `˅` para selecionar o carácter do seu passphrase.
   - Navegue utilizando `<` ou `>` para se deslocar entre caracteres. Pode também utilizar `>` para adicionar espaços.
   - Prima `✕` para apagar os caracteres.
   - Prima `✓` quando tiver terminado de editar o passphrase.

5. Adicionalmente, as outras opções têm as seguintes funcionalidades:


   - As opções `Adicionar Palavra` ou `Adicionar Números` podem ser utilizadas para acrescentar letras/números ao passphrase que está a ser editado.
   - Prima `Clear ALL` para reiniciar o passphrase que está atualmente a editar.
   - Prima `CANCEL` para voltar ao menu principal.

6. Anote o seu passphrase como cópia de segurança.

7. Prima `APPLY` para aceder ao wallet com o passphrase que acabou de definir.

8. O Mk4 apresentará então uma impressão digital de chave mestra com 8 caracteres. Isto pode ser considerado como o "ID" do wallet. Anote esta impressão digital e prima `✓` para continuar.


![18](assets/en/18.webp)


9. Agora, o wallet apresentará o menu principal do wallet com o passphrase que introduziu.

10. É importante notar que um wallet não lhe dirá que introduziu o passphrase incorreto, porque cada passphrase corresponde a cada wallet com uma identidade única (impressão digital da chave mestra). Por conseguinte, é uma boa prática voltar a introduzir o mesmo passphrase e verificar se produz a mesma impressão digital do wallet, assegurando que o introduziu corretamente. Para o fazer, execute os passos 11 a 14.

11. No menu principal, selecione `Restore Master`, depois carregue em `✓`. Está agora de volta ao menu principal do wallet com o passphrase em branco.


![19](assets/en/19.webp)


12. Vá novamente a `Passphrase` e, em seguida, prima `✓` para prosseguir.

13. Volte a introduzir o passphrase que escreveu no Passo 6 e, em seguida, prima `APPLY`.

14. Compare a impressão digital da chave mestra de 8 caracteres com a que anotou no Passo 8. Se ambas as impressões digitais não corresponderem, poderá ter introduzido caracteres incorrectos. Pode selecionar um novo passphrase e repetir o processo a partir do Passo 1. Mas se ambas as impressões digitais coincidirem, significa que introduziu o passphrase corretamente.

15. O wallet com o passphrase escolhido está pronto a ser utilizado.


## Exportar o Wallet para o Sparrow


Tal como outros wallet de hardware, o Coldcard Mk4 não pode ser utilizado isoladamente. Tem de ser ligado a um software wallet que actua como interface. O software wallet permite-lhe ver o seu saldo, criar transacções e gerir endereços, enquanto o Coldcard assina de forma segura essas transacções sem nunca expor as suas chaves privadas.


Neste tutorial, utilizaremos o Sparrow Wallet como interface. O procedimento para exportar o wallet é o seguinte:


1. Certifique-se de que tem um cartão MicroSD inserido no Mk4.

2. Execute os passos de "Configuração do passphrase" no wallet com o passphrase que pretende exportar. Se pretender exportar o wallet com o passphrase em branco, pode saltar este passo.

3. Vá a `Avançadas/Ferramentas` > Escolha `Exportar Wallet` > Selecione `Generic JSON` > Desloque-se para baixo enquanto lê as instruções e, em seguida, prima `✓`.


![20](assets/en/20.webp)


4. O Mk4 criou agora um ficheiro com o formato `.json` no cartão MicroSD.


![21](assets/en/21.webp)


5. Retire o cartão MicroSD do cartão Cold e insira-o no dispositivo onde o Sparrow Wallet está instalado.

6. Abrir Sparrow Wallet.

7. Clique em `Arquivo`


![22](assets/en/22.webp)


Em seguida, clique em `New Wallet`


![23](assets/en/23.webp)


Em seguida, introduza o nome do wallet


![24](assets/en/24.webp)


Depois disso, clique em `Criar Wallet`


![25](assets/en/25.webp)


8. Selecione o `Tipo de Script`.


![26](assets/en/26.webp)


9. Na secção Keystore, selecione `Airgapped Hardware Wallet`.


![27](assets/en/27.webp)


10. Procure por Coldcard e clique em `Importar ficheiro...`.


![28](assets/en/28.webp)


11. Selecione o ficheiro que foi criado no Passo 4 (o que tem o formato `.json`).


![29](assets/en/29.webp)


12. No Mk4, volte ao menu principal e navegue até `Avançado/Ferramentas` > `Ver Identidade`. Certifique-se de que a impressão digital apresentada no ecrã do Mk4 corresponde à do Sparrow Wallet (a impressão digital Master na secção Keystore)

13. Clique no botão "Aplicar" no canto inferior direito.


![30](assets/en/30.webp)


14. Opcionalmente, também pode adicionar uma palavra-passe para o wallet exportado. Esta palavra-passe é necessária sempre que abrir a aplicação Sparrow Wallet para aceder ao wallet. Se se esquecer da palavra-passe no futuro, pode simplesmente repetir os passos 1-13 e escolher uma nova palavra-passe.


![31](assets/en/31.webp)


15. O wallet foi exportado com sucesso e está pronto a ser utilizado.


![32](assets/en/32.webp)


## Receber bitcoin


De seguida, vamos aprender a receber o Bitcoin utilizando o Mk4. Este processo é bastante simples, pois não é necessário utilizar o próprio dispositivo Mk4. Desde que já tenha exportado o seu wallet para o Sparrow, pode receber Bitcoin diretamente através do Sparrow Wallet. Siga estes passos para receber bitcoins com o Mk4:


1. Abrir Sparrow Wallet.

2. Selecione `Open Wallet` > Escolha o ficheiro wallet para o qual pretende receber bitcoin > Introduza a palavra-passe associada a esse wallet.


![33](assets/en/33.webp)


3. Na interface do Sparrow, clique no separador `Receive` no lado esquerdo da interface.


![34](assets/en/34.webp)


4. Um endereço juntamente com um código QR aparecerá no topo. Pode copiar e colar o endereço ou digitalizar o código QR utilizando o wallet que irá utilizar para enviar bitcoin para o Sparrow Wallet. Opcionalmente, pode escrever uma etiqueta para a bitcoin que receber.


![35](assets/en/35.webp)


5. Depois de enviar os bitcoins, na interface do Sparrow, clique na aba `Transactions` no lado esquerdo da interface. Verá uma nova entrada no topo do histórico de transacções, que corresponde à transação que acabou de fazer.


![36](assets/en/36.webp)


6. Também pode navegar no separador `UTXOs` no lado esquerdo da interface para ver o bitcoin que acabou de receber.


![37](assets/en/37.webp)


## Envio de bitcoin


Ao contrário da receção de bitcoins, para gastar os bitcoins associados ao seu Coldcard é necessário utilizar o Coldcard para assinar as transacções. O procedimento de envio de bitcoins com o Mk4 é o seguinte:


1. Insira o cartão MicroSD no dispositivo onde o Sparrow Wallet está instalado.

2. Abrir Sparrow Wallet.

3. Selecione `Open Wallet` > Escolha o ficheiro wallet que pretende utilizar para enviar bitcoins > Introduza a palavra-passe associada a esse wallet.


![38](assets/en/38.webp)


4. Na interface do Sparrow, clique no separador `Send` no lado esquerdo da interface.


![39](assets/en/39.webp)


5. No separador `Pay to`, introduza o endereço para o qual pretende enviar os bitcoins.

6. Adicionar uma etiqueta para a transação.

7. Introduza o montante de bitcoins que pretende enviar.

8. Introduza a taxa alternando o `Faixa` ou introduza diretamente um número na parte `Taxa`.


![40](assets/en/40.webp)


9. No canto inferior direito, clique em `Criar transação`.


![41](assets/en/41.webp)


10. Será apresentado um novo separador de transação cujo nome é a etiqueta que introduziu no Passo 6. Clique em `Finalizar transação para assinatura`.


![42](assets/en/42.webp)


11. Clique em "Guardar transação" e guarde a transação no cartão MicroSD. Renomeie o ficheiro, se necessário. Este passo irá guardar a transação como um ficheiro PSBT.


![43](assets/en/43.webp)


12. Retire o cartão MicroSD e insira-o no seu Coldcard Mk4.

13. Ligue o seu Mk4 ligando-o a uma fonte de alimentação.

14. Introduza o seu PIN.

15. Vá a `Passphrase` e introduza o passphrase do wallet que pretende utilizar para enviar os bitcoins. Se quiseres usar o wallet com o passphrase em branco, salta este passo.

16. Certifique-se de que a impressão digital da chave mestra é a mesma que a do seu Sparrow Wallet. Pode verificar isto no separador `Settings` do Sparrow Wallet no lado esquerdo da interface. Depois, prima `✓` no seu Mk4 para prosseguir. Isto levá-lo-á para o menu principal.

17. No menu principal do Mk4, selecione `Pronto para assinar`. No ecrã aparecerá a mensagem `OKAY TO SEND?`. Certifique-se de que a quantidade de bitcoins que pretende enviar e o endereço de receção estão todos corretos. Prima `✓` para confirmar ou `✕` para cancelar.

18. Se houver vários ficheiros PSBT para escolher, o Mk4 apresentará a mensagem `Escolha o ficheiro PSBT a ser assinado`. Prima `✓` para continuar. Em seguida, selecione o arquivo PSBT que deseja assinar navegando para baixo ou para cima. Execute o Passo 17 nessa transação.


![44](assets/en/44.webp)


19. O Mk4 apresentará agora a mensagem `PSBT Signed` juntamente com o nome do ficheiro do PSBT assinado. Prima `✓` para continuar.

20. Retire o cartão MicroSD do cartão Cold e insira-o no dispositivo onde o Sparrow Wallet está instalado.

21. Em Sparrow Wallet, clique em "Carregar transação".


![45](assets/en/45.webp)


22. Selecione o ficheiro com o mesmo nome que o criado no Passo 19.


![46](assets/en/46.webp)


23. Clique em "Transmitir transação".


![47](assets/en/47.webp)


24. A sua transação foi transmitida e está a ser processada. Pode ir ao separador `Transacções` para ver o estado de confirmação da sua transação.


![48](assets/en/48.webp)


## Atualização de firmware


### Verificar a versão do firmware


O firmware do Coldcard Mk4 pode sempre ser atualizado para uma versão mais recente. Para verificar se o seu Mk4 foi atualizado para a versão mais recente ou não, execute os seguintes passos:

1. Ligue o seu Mk4 ligando-o a uma fonte de alimentação.

2. Introduza o seu PIN.

3. Vá a `Avançadas/Ferramentas` > Selecione `Atualizar Firmware` > Selecione `Mostrar Versão`.


![49](assets/en/49.webp)


Verifique a versão exibida no ecrã do Mk4 em comparação com a que está no [website do Coinkite] (https://coldcard.com/downloads). Se a versão for diferente, é possível atualizar o firmware para a versão mais recente.


![50](assets/en/50.webp)


### Atualização do firmware


Se pretender atualizar o firmware para a versão mais recente, siga os passos seguintes:


1. Insira o cartão MicroSD no seu computador portátil/PC.

2. Vá ao [sítio Web do Coinkite] (https://coldcard.com/downloads) e transfira o firmware mais recente para o seu cartão MicroSD (o botão vermelho à direita da imagem do Mk4 com o número da versão).


![51](assets/en/51.webp)


Pode também descarregar outras versões clicando em `Todos os ficheiros do Mk4` e explorando a versão que pretende descarregar. O ficheiro descarregado estará no formato `.dfu`.


![52](assets/en/52.webp)


3. Retire o cartão MicroSD e insira-o no seu Mk4.

4. Ligue o seu Mk4 ligando-o a uma fonte de alimentação.

5. Introduza o seu PIN.

6. Vá a `Advanced/Tools` > Selecione `Upgrade Firmware` > Selecione `From MicroSD` > Desloque-se para baixo enquanto lê as instruções e prima `✓`.


![53](assets/en/53.webp)


7. Selecione o ficheiro `.dfu` que descarregou no Passo 2.

8. O Coldcard Mk4 exibirá uma mensagem `Instalar este novo firmware?`. Desloque-se para baixo enquanto lê as instruções e prima `✓`.


![54](assets/en/54.webp)


9. Aguarde que o Mk4 termine de instalar o novo firmware. Não desligue a fonte de alimentação durante a instalação.

10. Após a conclusão, o Mk4 reiniciar-se-á. Pode introduzir o seu PIN e executar os passos de "Verificação da versão do firmware" para verificar se o firmware foi atualizado ou não.


## Funcionalidades avançadas


### Alterar o seu PIN


Se pretender alterar o seu PIN de início de sessão, basta efetuar os seguintes passos:


1. Prepare uma caneta e uma folha de papel.

2. Ligue o seu Mk4 ligando-o a uma fonte de alimentação.

3. Introduza o seu PIN.

4. Aceder a `Configurações` > Selecionar `Configurações de início de sessão` > Selecionar `Alterar PIN principal`

5. Navegue para baixo enquanto lê a mensagem e, em seguida, prima `✓` para prosseguir.


![55](assets/en/55.webp)


6. Introduza o seu PIN antigo.

7. Introduza o seu novo prefixo PIN (deve ter entre 2 e 6 caracteres) e anote-o.

8. O Mk4 irá agora mostrar duas novas palavras anti-phishing, escreva-as e depois prima `✓` para continuar.

9. Introduza o sufixo do seu novo PIN (ou o resto do PIN, que deve ter entre 2 e 6 caracteres) e anote-o.


![56](assets/en/56.webp)


10. Volte a introduzir o seu novo prefixo PIN.

11. Verifique se as palavras anti-phishing correspondem às que escreveu no passo 8.

12. Volte a introduzir o novo sufixo do PIN (ou o resto do PIN).


![57](assets/en/57.webp)


13. O seu PIN foi alterado com sucesso.


### PINs de truques - Adicionar novo truque


Um PIN de truque é um código PIN alternativo diferente daquele usado para configurar seu Coldcard Mk4 pela primeira vez. Quando você liga o seu Mk4, você pode inserir o(s) PIN(s) de truque em vez do seu PIN principal para acionar determinadas ações. Para configurar o PIN de truque no Mk4, siga os seguintes passos:


1. Prepare uma caneta e uma folha de papel.

2. Ligue o seu Mk4 ligando-o a uma fonte de alimentação.

3. Introduza o seu PIN.

4. Vá a `Configurações` > Selecione `Configurações de início de sessão` > Selecione `PINs de truques` > Selecione `Adicionar novo truque`.


![58](assets/en/58.webp)


5. Introduza o prefixo do seu PIN do truque (deve ter entre 2 e 6 caracteres) e anote-o.

6. O Mk4 irá agora mostrar duas novas palavras anti-phishing, escreva-as e depois prima `✓` para continuar.

7. Introduza o sufixo do seu PIN do truque (ou o resto do PIN, que deve ter 2 a 6 caracteres) e anote-o.


![59](assets/en/59.webp)


8. Navegue para baixo ou para cima para selecionar a ação que pretende associar ao PIN do truque que acabou de criar. A lista de acções é a seguinte:


    - quando selecionado, os chips do seu Mk4 serão destruídos após a introdução do PIN, tornando o seu Mk4 inutilizável para sempre.
    - `Wipe Seed`, pode escolher entre as seguintes acções:
      - "Limpar e reiniciar": O seed é limpo e o Coldcard será reiniciado após a inserção do PIN.
      - `Silent Wipe`: O seed é apagado silenciosamente, porém o cartão Cold agirá como se o PIN tivesse sido inserido incorretamente.
      - `Wipe -> Wallet`: O seed é apagado silenciosamente, e o cartão Cold leva-o para um wallet de coação.
    - `Duress Wallet`, quando selecionado, o seu Mk4 conduzirá a um wallet de coação após a introdução do PIN.
    - `Login Countdown`, pode escolher entre as seguintes acções:
      - "Limpar e contagem decrescente": O seed é imediatamente limpo e, em seguida, o Mk4 começa a apresentar uma contagem decrescente.
      - `Contagem decrescente & Brick`: Começa a contagem decrescente e o Mk4 vai-se brickar quando o tempo acabar.
      - contagem decrescente: O Mk4 iniciará a contagem decrescente e reiniciar-se-á a si próprio quando o tempo se esgotar.
    - quando selecionado, após a introdução do PIN do truque, o cartão Cold actua como se o seedphrase tivesse sido apagado, mas na realidade ainda está na memória.
    - `Just Reboot`, quando selecionado, o Coldcard reiniciar-se-á a si próprio após a introdução do PIN do truque.
    - `Delta Mode`, esta funcionalidade avançada destina-se a utilizadores experientes e foi concebida para proteger contra ameaças graves, como a coerção por alguém com conhecimentos internos. Quando o Modo Delta é ativado, o COLDCARD parece abrir o verdadeiro wallet, permitindo que o atacante navegue e confirme que parece genuíno. No entanto, ele bloqueia secretamente todas as assinaturas de transações, de modo que nenhum bitcoin pode ser enviado. Também desactiva o acesso à frase seed, e qualquer tentativa de a visualizar apaga-a completamente. Para fazer com que o falso wallet pareça mais convincente, o Trick PIN usado para o Delta Mode deve começar com os mesmos números que o PIN real (para que mostre as mesmas palavras anti-phishing) mas terminar de forma diferente.
    - `Policy Unlock`, quando selecionada, a política de despesas de assinante único (SSSP) será desactivada após a introdução do PIN do truque.
    - `Policy Unlock & Wipe`, quando selecionado, finge desativar o SSSP, mas irá limpar o seedphrase no processo.

9. Depois de ter selecionado a ação que pretende associar ao PIN do truque, confirme a sua escolha premindo `✓`. O seu PIN de truque foi configurado com sucesso.

10. Em `Configurações` > `Configurações de início de sessão` > `PINs de truque`, pode ver a lista de PINs de truque que criou e as acções associadas aos mesmos. Pode optar por reconfigurar os PINs de truques e as acções associadas aos mesmos. Pode também ocultá-lo ou eliminá-lo selecionando o PIN e, em seguida, selecionar `Ocultar truque` ou `Eliminar truque`.


![60](assets/en/60.webp)


### PINs de truque - Adicionar se estiver errado


Em alternativa, pode adicionar uma ação `Adicionar se errado` que será acionada depois de o PIN incorreto ser introduzido um determinado número de vezes. Pode configurar esta ação executando os seguintes passos:


1. Ligue o seu Mk4 ligando-o a uma fonte de alimentação.

2. Introduza o seu PIN.

3. Vá a `Configurações` > Selecione `Configurações de início de sessão` > Selecione `PINs falsos` > Selecione `Adicionar se estiver errado`.


![61](assets/en/61.webp)


4. O Mk4 apresentará uma mensagem relativa a esta definição. Navegue para baixo enquanto lê a explicação e, em seguida, prima `✓` para prosseguir.

5. Introduza o número de tentativas erradas necessárias para desencadear a ação. Nota: O número máximo de tentativas é `12`. Isto deve-se ao facto de o Mk4 ter sido concebido de forma a que, quando o PIN incorreto é introduzido `13` vezes, o dispositivo se bloqueia, ficando permanentemente inutilizável. Depois de introduzir o número, prima `✓` para continuar.

6. Navegue para cima ou para baixo para selecionar a ação. As acções disponíveis são as seguintes:


   - `Wipe, Stop`: O seedphrase é apagado e o dispositivo mostra "Seed is wiped, Stop"
   - `Wipe & Reboot`: O seedphrase é apagado e o dispositivo é reiniciado sem qualquer mensagem.
   - `Silent Wipe`: O seedphrase é apagado silenciosamente e o dispositivo comporta-se como uma tentativa de PIN errado (sem mensagem de limpeza óbvia).
   - `Brick Self`: O dispositivo está permanentemente desativado e apenas mostra "Bricked"
   - última oportunidade: O seedphrase é apagado, mas tem direito a uma última tentativa de PIN; introduza novamente o PIN errado e o dispositivo será bloqueado.
   - `Just Reboot`: O dispositivo é simplesmente reiniciado e nada mais é alterado.

Escolha a ação que pretende aplicar e prima `✓` para prosseguir


![62](assets/en/62.webp)


7. Será remetido para o diretório `Configurações > Configurações de início de sessão > PINs de truque`. Em `Trick PINs:`, encontrará a lista de pins de truques juntamente com a ação `WRONG PIN`. Pode também ocultá-lo ou apagá-lo selecionando o PIN e depois selecionar `Hide Trick` ou `Delete Trick`.


![63](assets/en/63.webp)



## Conclusão


Este tutorial fornece o guia sobre como configurar o Mk4, como realizar transacções Bitcoin com o Mk4 e como utilizar algumas funcionalidades avançadas do Mk4. Oferece formas seguras e flexíveis de armazenar e gerir os seus bitcoins. O seu design garante que as chaves privadas nunca saem do dispositivo, enquanto as funcionalidades como passphrases, PINs de truque e transacções air-gapped dão aos utilizadores controlo total sobre a sua configuração de segurança. Pode ser emparelhado com o Sparrow Wallet para uma experiência de fácil utilização na criação, assinatura e gestão de transacções Bitcoin sem comprometer a privacidade ou a segurança.


Se desejar explorar outras funcionalidades, pode consultar a documentação no sítio Web do Coinkite [aqui] (https://coldcard.com/docs/). Espero que este tutorial seja útil quando estiveres a utilizar o teu Coldcard Mk4. Obrigado e até à próxima!