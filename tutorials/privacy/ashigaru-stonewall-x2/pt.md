---
name: Ashigaru - Stonewall x2
description: Compreender e utilizar as transacções Stonewall x2 em Ashigaru
---
![cover stonewall x2](assets/cover.webp)



> *Fazer de cada despesa uma junção de moedas

## O que é uma transação Stonewall x2?



Stonewall x2 é uma forma específica de transação Bitcoin concebida para aumentar a confidencialidade do utilizador quando gasta, colaborando com uma terceira parte não envolvida na despesa. Este método simula uma mini-coinjoin entre dois participantes, ao mesmo tempo que efectua um pagamento a um terceiro. As transacções Stonewall x2 estão disponíveis na aplicação Ashigaru, um fork do Samourai Wallet (a equipa responsável pela criação deste tipo de transação).



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

O funcionamento é relativamente simples: o utilizador utiliza um UTXO na sua posse para efetuar o pagamento e recorre à ajuda de um terceiro que também contribui com um UTXO seu. A transação termina com quatro saídas: duas delas em montantes iguais, uma destinada ao endereço do beneficiário, a outra a um endereço pertencente ao colaborador. Um terceiro UTXO é devolvido a um outro endereço pertencente ao colaborador, permitindo-lhe recuperar o montante inicial (uma ação neutra para ele, modulando os custos do mining), e um último UTXO regressa a um endereço que nos pertence, o que constitui a troca de pagamento.



Assim, são definidos três papéis diferentes nas transacções Stonewall x2:




- O emitente, que efectua o pagamento efetivo ;
- O colaborador, que disponibiliza bitcoins para melhorar o anonimato da transação, recuperando a totalidade dos seus fundos no final (uma ação neutra para ele, sem contar com os custos mining);
- O destinatário, que pode não ter conhecimento da natureza específica da transação e espera simplesmente o pagamento do remetente.



Vejamos um exemplo. Alice vai à padaria comprar a sua baguete, que custa `4 000 sats`. Ela quer pagar em bitcoins, mantendo alguma confidencialidade sobre o seu pagamento. Por isso, chama o seu amigo Bob, que a vai ajudar.



![image](assets/fr/01.webp)



Analisando esta transação, podemos ver que o padeiro recebeu efetivamente 4 000 sats` como pagamento pela baguete. O Alice utilizou `10 000 sats` na entrada e recuperou `6 000 sats` na saída, obtendo um saldo líquido de `-4 000 sats`, que corresponde ao preço da baguete. Quanto ao Bob, forneceu 15 000 sats` como entrada e recebeu duas saídas: uma de 4 000 sats` e outra de 11 000 sats`, o que perfaz um saldo de 0`.



Neste exemplo, negligenciei intencionalmente as comissões mining para facilitar a compreensão. Na realidade, as comissões de transação são partilhadas em partes iguais entre o emissor do pagamento e o colaborador.



## Qual é a diferença entre Stonewall e Stonewall x2?



Uma transação StonewallX2 funciona exatamente da mesma forma que uma transação Stonewall, exceto que a primeira é colaborativa, enquanto a segunda não é. Como vimos, uma transação Stonewall x2 envolve a participação de um terceiro, que é externo ao pagamento, e que disponibilizará as suas bitcoins para aumentar a confidencialidade da transação. Numa transação Stonewall clássica, o papel do colaborador é assumido pelo remetente.



Voltemos ao nosso exemplo da Alice na padaria. Se ela não tivesse conseguido encontrar alguém como o Bob para a acompanhar na sua farra de gastos, poderia ter feito uma Stonewall sozinha. Assim, os dois UTXOs na entrada seriam dela, e ela teria apanhado 3 na saída.



![image](assets/fr/02.webp)




De um ponto de vista externo, a transação teria permanecido inalterada.



![image](assets/fr/05.webp)



A lógica deve, portanto, ser a seguinte quando se pretende utilizar uma ferramenta de despesa Ashigaru:




- Se o comerciante não suportar o Payjoin Stowaway, pode efetuar uma transação em colaboração com outra pessoa fora do pagamento graças ao Stonewall x2 ;
- Se não conseguir encontrar ninguém para fazer uma transação Stonewall x2, pode fazer uma transação apenas Stonewall, que imitará o comportamento de uma transação Stonewall x2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Qual é o objetivo de uma transação Stonewall x2?



A estrutura x2 da Stonewall acrescenta uma enorme quantidade de entropia à transação, confundindo a análise da cadeia. Vista de fora, esta transação pode ser interpretada como um pequeno Coinjoin entre duas pessoas. Mas, na realidade, trata-se de um pagamento. Este método cria, portanto, incertezas na análise da cadeia, ou mesmo conduz a falsas pistas.



Vejamos o exemplo do Alice, do Bob e do Boulanger. A transação na cadeia de blocos teria o seguinte aspeto:



![image](assets/fr/03.webp)



Um observador externo que se baseie na heurística comum de análise de cadeias pode concluir erradamente que "*Alice e Bob fizeram uma pequena junção, com um UTXO a entrar e dois UTXOs a sair*".



![image](assets/fr/04.webp)



Esta interpretação é incorrecta porque, como sabem, foi enviado um UTXO para a Boulanger, o Alice tem apenas uma saída de permuta e o Bob tem duas.



![image](assets/fr/01.webp)



Mesmo que o observador externo consiga identificar a paterna da transação Stonewall x2, não terá toda a informação. Não será capaz de determinar qual das duas UTXOs com os mesmos montantes corresponde ao pagamento. Também não poderá determinar se foi o Alice ou o Bob que efectuou o pagamento. Finalmente, não poderá determinar se as duas UTXO registadas são de duas pessoas diferentes ou se pertencem a uma única pessoa que as fundiu. Este último ponto deve-se ao facto de as transacções clássicas da Stonewall, acima referidas, seguirem exatamente o mesmo padrão das transacções da Stonewall x2. Visto de fora e sem informação contextual adicional, é impossível diferenciar uma transação Stonewall de uma transação Stonewall x2. As primeiras não são transacções de colaboração, enquanto as segundas o são. Este facto acrescenta ainda mais dúvidas à despesa.



![image](assets/fr/05.webp)




## Como é que estabeleço uma ligação entre Paynyms?



Tal como acontece com outras transacções de colaboração em Ashigaru (*Cahoots*), Stonewall x2 envolve a troca de transacções parcialmente assinadas entre o remetente e o colaborador. Esta troca pode ser efectuada manualmente, se estiveres fisicamente presente com o teu colaborador, ou automaticamente usando o protocolo de comunicação Soroban.



Se escolheres a segunda opção, terás de estabelecer uma ligação entre Paynyms antes de poderes executar um Stonewall x2. Para isso, o teu Paynym deve "*seguir*" o Paynym do teu colaborador, e vice-versa. Para saberes como fazer isto, podes seguir o início deste outro tutorial:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Como é que faço uma transação de Stonewall x2 em Ashigaru?



Para efetuar uma transação Stonewall x2, clique na imagem do seu Paynym no canto superior esquerdo do ecrã e abra o menu "Colaborar". A pessoa que participa na transação consigo deve fazer o mesmo, a não ser que esteja a trocar códigos QR pessoalmente.



![Image](assets/fr/06.webp)



Tem duas opções: selecionar `Iniciar` se for o remetente do pagamento, ou `Participar` se for a pessoa que colabora na transação mas não é nem o pagador nem o destinatário efetivo.



![Image](assets/fr/07.webp)



Se tem o papel de colaborador, o procedimento é muito simples. Para a colaboração remota através da rede Soroban, clique em `Participar`, escolha a conta que deseja utilizar, depois prima `Esperar PEDIDOS DE CAHOOTS` para aguardar o pedido enviado pelo pagador.



![Image](assets/fr/08.webp)



Por outro lado, para a colaboração presencial através da leitura do código QR, aceda à página inicial do seu wallet, prima o ícone do código QR na parte superior do ecrã e, em seguida, leia o código QR fornecido pelo ordenante que inicia a transação.



![Image](assets/fr/09.webp)



Se estiver na função de pagador, ou seja, se for o iniciador da transação, vá ao menu `Colaborar` e selecione `Iniciar`.



![Image](assets/fr/10.webp)



Para o tipo de transação, uma vez que pretendemos realizar um Stonewall x2, selecione esta opção.



![Image](assets/fr/11.webp)



Pode então escolher entre a colaboração em linha (*Cahoots* via *Soroban*) ou a colaboração presencial, com troca de códigos QR.



![Image](assets/fr/12.webp)



### Cahoots online



Se escolheu a opção `Online`, selecione o seu colaborador entre os Paynyms que segue.



![Image](assets/fr/13.webp)



Clique em "Configurar transação" e, em seguida, escolha a conta a partir da qual pretende efetuar a despesa.



![Image](assets/fr/14.webp)



Na página seguinte, introduza os dados da transação: o endereço do destinatário efetivo do pagamento, o montante a enviar e a taxa de cobrança. Em seguida, clique em "Rever a configuração da transação".



![Image](assets/fr/15.webp)



Verifique cuidadosamente as informações, certifique-se de que o seu colaborador está a ouvir os pedidos *Cahoots*, depois clique no botão verde `BEGIN TRANSACTION` para iniciar a troca de PSBTs via Soroban.



![Image](assets/fr/16.webp)



Aguarde até que ambos os participantes tenham assinado a transação e, em seguida, transmita-a na rede Bitcoin.



![Image](assets/fr/17.webp)



### Discussões presenciais



Se desejar efetuar a troca pessoalmente, selecionar o tipo de transação `STONEWALL X2` e, em seguida, escolher a opção `Pessoal / Manual`.



![Image](assets/fr/18.webp)



Clique em "Configurar transação" e, em seguida, escolha a conta a partir da qual pretende efetuar a despesa.



![Image](assets/fr/19.webp)



Na página seguinte, introduza os dados da transação: o endereço do destinatário efetivo do pagamento, o montante a enviar e a taxa de cobrança. Em seguida, clique em "Rever a configuração da transação".



![Image](assets/fr/20.webp)



Verifique os dados e, em seguida, prima o botão verde "INICIAR TRANSAÇÃO" para iniciar a troca de PSBT através da leitura do código QR.



![Image](assets/fr/21.webp)



A troca é feita alternando a digitalização com o colaborador: clique em `MOSTRAR CÓDIGO QR` para mostrar o seu código QR ao seu colaborador, que o digitalizará. Este, por sua vez, clica em `MOSTRAR CÓDIGO QR` para mostrar o seu, e o colaborador digitaliza-o com `Lançar scanner QR`. Repita este processo até que as cinco etapas de intercâmbio tenham sido concluídas.



![Image](assets/fr/22.webp)



Quando todas as trocas estiverem concluídas, verifique os detalhes da transação e, em seguida, liberte-a arrastando a seta verde na parte inferior do ecrã.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). A sua estrutura é a seguinte:



![Image](assets/fr/24.webp)



*Crédito: [mempool.space](https://mempool.space/)*



Podemos observar duas entradas da minha carteira, respetivamente `91.869 sats` e `64.823 sats`, enquanto as outras duas entradas vêm do wallet do meu colaborador. Do lado da saída, um UTXO de `100.000 sats` é enviado para o beneficiário efetivo, e dois UTXOs de `100.000 sats` e `159.578 sats` voltam para a carteira do meu colaborador. Para ele, a operação é neutra, pois recupera o montante total dos fundos que investiu na entrada (excluindo os custos mining para os quais contribuiu). Finalmente, recebo um UTXO de troca de 56 270 sats`, correspondente à diferença entre o total das minhas entradas e o pagamento de 100 000 sats` enviado ao destinatário.



Obviamente, posso descrever esta estrutura porque eu próprio construí a transação. Mas para um observador externo, é geralmente impossível determinar que UTXOs pertencem a que participante, quer nas entradas quer nas saídas.



Para aprofundar seu conhecimento sobre gerenciamento de privacidade onchain no Bitcoin, recomendo que você faça meu treinamento BTC 204 na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c