---
name: Slipstream
description: Sending a signed transaction directly to a miner with Slipstream, without broadcasting it to the Bitcoin network
---

![cover](assets/cover.webp)

Normalmente, quando você assina uma transação, ela é automaticamente transmitida para todos os nós Bitcoin da rede. Em seguida, ela aguarda para ser minerada.

No entanto, enquanto a transação não estiver em um bloco, um atacante que tenha obtido sua chave privada poderia substituí-la e roubar os fundos. Este é tipicamente o caso se você usar uma hardware wallet ColdCard.

A ferramenta Slipstream, da mineradora MARA, permite que você evite transmitir a transação para a rede: ela é enviada diretamente (e apenas) a um minerador, o que a mantém privada e evita expô-la na rede. É provável que a transação demore mais para ser minerada, mas ela estará protegida contra um ataque de substituição.

Abaixo, oferecemos um tutorial que permite tanto aos usuários da [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) quanto aos usuários da carteira [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) usar a ferramenta Slipstream da mineradora MARA através da página [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Aviso**: esta ferramenta é destinada apenas a determinados perfis, principalmente carteiras Liana, carteiras miniscript e alguns tipos de multisig. A Wizardsardine **desaconselha explicitamente** seu uso para carteiras cujos fundos já estejam em risco crítico de roubo, por exemplo aquelas cuja frase de recuperação foi gerada em um dispositivo ColdCard afetado pela vulnerabilidade do gerador de números aleatórios. Nessa situação, a corrida contra o atacante se conta em segundos, e uma transação enviada a um único minerador demora muito mais para confirmar do que uma transação transmitida normalmente. Se isso for relevante para o seu caso, leia primeiro nosso tutorial dedicado:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Para usuários da Liana

A Liana é mantida pela Wizardsardine, a criadora da página [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), então o caminho é direto: basta exportar o arquivo PSBT assinado em vez de transmiti-lo.

*Pré-requisito: ter fundos na sua carteira Liana.*

### Passo 1: Crie sua transação com a Liana

Como de costume, monte sua transação adicionando o endereço de destino, a descrição e o valor (aqui, o máximo disponível na carteira).

Para definir a taxa de fee:

- selecione as moedas que deseja gastar clicando na pequena caixa no canto inferior esquerdo, sob "Coins selection";
- em seguida, insira a taxa de fee. Lembre-se de definir taxas bem mais altas do que a taxa sugerida, conforme descrito nesta página: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Por fim, clique em "Next".

![Building the transaction in Liana](assets/fr/01.webp)

### Passo 2: Verifique os detalhes da sua transação

Antes de clicar em "Sign", verifique os detalhes da sua transação; em particular:

- o valor enviado;
- o número de satoshis alocados para as taxas de transação;
- mas, acima de tudo, o endereço para o qual você está enviando os fundos (lembre-se de verificar os primeiros 5/6 caracteres, os últimos 5/6 e 5/6 caracteres no meio do endereço, a fim de evitar ataques de "address poisoning").

![Checking the transaction details](assets/fr/02.webp)

### Passo 3: Selecione as carteiras de assinatura

Em seguida, selecione as carteiras de software e/ou hardware com as quais você precisa assinar sua transação. Um lembrete rápido: no caso de uma carteira multisig 2-de-2, você precisa de 2 assinaturas em 2.

### Passo 4: Exporte o arquivo PSBT da sua transação

A transação Bitcoin agora está assinada pelas chaves apropriadas. Não clique em "Broadcast", caso contrário ela será compartilhada com toda a rede e, se você usar uma hardware wallet ColdCard, sua transação ficará publicamente exposta e seus fundos estarão em risco.

Agora você pode clicar em "Export" e salvar o arquivo PSBT localmente no seu computador.

![Exporting the PSBT file from Liana](assets/fr/03.webp)

### Passo 5: Envie a transação ao minerador via outofband.wizardsardine.com

Agora, os passos finais. Para enviar a transação ao minerador, basta pegar o arquivo PSBT e arrastá-lo e soltá-lo na área designada.

![Dropping the PSBT file on outofband.wizardsardine.com](assets/fr/04.webp)

A transação é então exibida como mostrado abaixo.

![Transaction in the queue](assets/fr/05.webp)

### Passo 6: Envie a transação via Slipstream

Por fim, basta clicar em "Send" para que a transação seja enviada à MARA via Slipstream.

![Sending the transaction via Slipstream](assets/fr/06.webp)

Em poucos segundos, a transação passa de "Sending" para "Accepted":

![Transaction accepted by Slipstream](assets/fr/07.webp)

Resta apenas copiar o identificador da transação (TXID) e colá-lo no [mempool.space](https://mempool.space/) para acompanhar sua mineração:

![Looking up the TXID on mempool.space](assets/fr/08.webp)

Atenção: a transação aparecerá como "Transaction not found" até que a mineradora MARA minere um bloco e inclua sua transação nele. Isso pode levar dezenas de minutos, ou até mesmo horas, porque a MARA detém apenas cerca de 4,5% do hashrate da rede Bitcoin. Em 4 de agosto de 2026, isso corresponde a aproximadamente um bloco minerado a cada 3 horas e 45 minutos.

## Para usuários de outras carteiras

Se você não usa a [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) mas ainda assim quer usar a ferramenta, aqui está um tutorial usando uma carteira multisig 2-de-2. Para isso, usaremos a carteira de software [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Pré-requisito: ter fundos na sua carteira Sparrow.*

### Passo 1: Crie sua transação

Com o [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), crie a transação na sua carteira multisig. Lembre-se de definir taxas bem mais altas do que a taxa sugerida, conforme descrito nesta página: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Depois de criada, clique em "Create Transaction".

![Creating the transaction in Sparrow](assets/fr/09.webp)

### Passo 2: Finalize sua transação

Para finalizar sua transação, agora você precisa assiná-la. Para isso, clique em "Finalize Transaction for Signing".

![Finalizing the transaction for signing](assets/fr/10.webp)

### Passo 3: Assine sua transação com suas diferentes chaves

Agora chega o momento de assinar a transação. Para isso, basta assiná-la com a(s) carteira(s) de software ou hardware que você usa.

![Signing the transaction with the multisig keys](assets/fr/11.webp)

### Passo 4: Baixe a transação assinada, e não a transmita para a rede

A transação Bitcoin agora está assinada por ambas as chaves da nossa multisig 2-de-2. Não clique em "Broadcast Transaction", caso contrário ela será compartilhada com toda a rede e, se você usar uma hardware wallet ColdCard, sua transação ficará publicamente exposta e seus fundos estarão em risco.

![Signed transaction, ready but not broadcast](assets/fr/12.webp)

### Passo 5: Exiba o script da transação assinada, ou baixe o arquivo PSBT

Para exibir a transação Bitcoin assinada, agora clique em "View Final Transaction". Você poderá então copiar o script da transação Bitcoin assinada:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Displaying the signed transaction script](assets/fr/13.webp)

Se quiser baixar o arquivo da transação, você pode:

- clicar em "File" e depois em "Save transaction…";
- ou clicar no botão de conexão de rede no canto inferior direito (botão amarelo) e depois em "Save Final Transaction".

A transação será então salva localmente no seu computador.

![Saving the final transaction locally](assets/fr/14.webp)

### Passo 6: Envie a transação ao minerador via outofband.wizardsardine.com

Agora, os passos finais. Para enviar a transação ao minerador, basta:

- ir até [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- colar o script da transação assinada copiado no passo anterior e, em seguida, clicar em "ADD TO QUEUE" abaixo;

![Pasting the transaction script into the tool](assets/fr/15.webp)

- ou pegar o arquivo e arrastá-lo e soltá-lo na área designada.

![Dropping the transaction file on the tool](assets/fr/16.webp)

A transação é então exibida como mostrado abaixo.

![Transaction in the queue](assets/fr/17.webp)

Se uma mensagem informar que o valor total de satoshis na entrada da sua transação é desconhecido (e que, por consequência, o número de satoshis das taxas não pode ser calculado), basta inserir o valor total de satoshis de entrada manualmente. Para encontrá-lo, basta clicar na exibição da sua transação no Sparrow, no meio do diagrama:

![Total input amount shown in Sparrow](assets/fr/18.webp)

Em seguida, insira esse valor (15.904 sats em nosso exemplo) na ferramenta [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Manually entering the total input amount](assets/fr/19.webp)

Por fim, verifique se a taxa de fee está correta.

### Passo 7: Envie a transação via Slipstream

Por fim, basta clicar em "Send" para que a transação seja enviada à MARA via Slipstream.

![Sending the transaction via Slipstream](assets/fr/20.webp)

Em poucos segundos, a transação passa de "Sending" para "Accepted":

![Transaction accepted by Slipstream](assets/fr/21.webp)

Resta apenas copiar o identificador da transação (TXID) e colá-lo no [mempool.space](https://mempool.space/) para acompanhar sua mineração:

![Looking up the TXID on mempool.space](assets/fr/22.webp)

Atenção: a transação aparecerá como "Transaction not found" até que a mineradora MARA minere um bloco e inclua sua transação nele. Isso pode levar dezenas de minutos, ou até mesmo horas, porque a MARA detém apenas cerca de 4,5% do hashrate da rede Bitcoin. Em 4 de agosto de 2026, isso corresponde a aproximadamente um bloco minerado a cada 3 horas e 45 minutos.
