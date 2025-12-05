---
name: Jade - Electrum
description: Como utilizar o seu Jade ou Jade Plus com o Electrum (ambiente de trabalho)
---

![cover](assets/cover.webp)



_Este guia foi retirado de uma lição dos [Workshops Bitcoin](https://officinebitcoin.it/lezioni/jadeele/index.html)_



O tutorial é feito com o Jade Classic, mas as operações também são válidas para quem tem o Jade Plus.



Depois de inicializar o Jade, pode começar a utilizá-lo e, para o fazer, escolher um ecrã wallet.



O Jade é um dispositivo que pode ser utilizado com várias aplicações wallet, ou aplicações complementares, como a Blockstream as especifica no seu sítio Web.



Neste tutorial, verá os passos para utilizar o Electrum Wallet, através da ligação por cabo USB.



## Transferência de chave pública



Pegue e ligue a sua Jade inicializada. Assim que o ligares, ele terá o seguinte aspeto:




![img](assets/en/32.webp)



Se selecionar _Unlock Jade_, aparece o menu onde tem de escolher como ligar o seu dispositivo à aplicação complementar.



Com o Electrum só é possível ligar o Jade através de USB, pelo que deve optar por este método.



Lançar o Electrum, que se abrirá propondo como opção por defeito a abertura do último wallet utilizado.



Se for a primeira vez que liga a Jade ao Electrum, selecione _Create New Wallet_ e depois _Finish_.



![img](assets/en/34.webp)



Nome wallet.



![img](assets/en/35.webp)



Selecione Standard Wallet.



![img](assets/en/36.webp)



Ao escolher o armazenamento de chaves, é essencial selecionar _Utilizar um dispositivo de hardware_.



![img](assets/en/37.webp)



O Electrum começa a procurar o dispositivo de hardware.



![img](assets/en/38.webp)



Ao ligar o USB ao computador (já ligado do lado do USB C ao Jade), o hardware do wallet aparece-lhe em modo de bloqueio. A Jade desbloqueia-o introduzindo o PIN de seis dígitos definido durante a configuração.




![img](assets/en/39.webp)



Dispositivo de hardware desbloqueado, Electrum detecta Jade. Continuar clicando em _Próximo_.



![img](assets/en/40.webp)



Nesta altura, o Electrum pede-lhe para definir o guião de política: escolha _Native Segwit_.



![img](assets/en/41.webp)



Inicia-se a fase de transferência da chave pública do wallet do Jade para o ecrã Electrum.



Quando a exportação da chave pública estiver concluída, o processo está terminado.



O watch-only está pronto e o Electrum alerta para a sua conclusão com o seguinte ecrã.



![img](assets/en/42.webp)



O wallet é efetivamente criado e pode começar a explorá-lo: pode ver os _addresses_, a _wallet information_ e - o mais importante - pode ver no canto inferior direito a indicação de que se trata do dispositivo da Blockstream. O ponto verde ao lado do logotipo da Blockstream indica que o dispositivo está ligado e devidamente conectado à rede local.



![img](assets/en/43.webp)



## Receber e gastar transacções



No menu _Receive_ do Electrum, generate uma `scriptPubKey` (endereço) para receber fundos. Comece sempre com uma pequena quantia e faça um teste de receber+gastar.



![img](assets/en/44.webp)



Depois de ter recebido satss, pode verificar a sua chegada no menu _Histórico_.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Quando a transação for confirmada, pode gastar este UTXO e terminar o teste.



A despesa envolve a utilização do Jade para assinar.



Vá ao menu _Send_ do Electrum, cole um scriptPubKey e verifique-o bem.



![img](assets/en/47.webp)



Quando terminar, prima _Pagar_.



Abre-se a janela de transação, na qual é importante definir as taxas de transação corretas. Quando tiver terminado todas as definições, clique em _Preview_ no canto inferior direito.



![img](assets/en/48.webp)



A janela da transação mostra alguns detalhes importantes, em primeiro lugar o estado: `Unsigned`.



Nesta fase, pode também ver o comando _Sign_, no qual deve clicar para apor a assinatura no Jade.



![img](assets/en/49.webp)



Inicia-se agora uma fase de comunicação entre o ecrã wallet e o dispositivo de hardware, em que o Electrum alerta para seguir as instruções do dispositivo de hardware, ligado e pronto a assinar.



![img](assets/en/50.webp)



**Primeiro, porém, é melhor verificar o que está a assinar: todos os parâmetros da transação que acabou de criar também aparecem no Jade** e pode verificá-los a todos.



![img](assets/en/51.webp)



Para continuar, certifique-se de que coloca sempre o cursor sobre a seta `→` que conduz aos passos seguintes e nunca sobre o `X`, a menos que pretenda terminar a operação sem a completar.



A parte da verificação termina com a apresentação da taxa. Nesta altura, a confirmação é equivalente a colocar a sua assinatura.



![img](assets/en/52.webp)



Durante um breve momento, o Jade processa a operação e, quando esta termina, regressa ao menu inicial.



![img](assets/en/53.webp)



No Electrum, pode ver o estado da transação, que mudou de "Não assinado" para "Assinado" e agora é possível propagá-la clicando em "Transmitir".



![img](assets/en/54.webp)



O wallet, assim testado, pode ser utilizado para receber o UTXO destinado a uma armazenagem segura.



![img](assets/en/55.webp)



Este guia é um exemplo de como utilizar o seu Jade, ligado por USB, a um relógio wallet. O Electrum é um exemplo clássico, mas pode preferir outro software wallet. O Jade exporta a chave pública para muitas outras carteiras: encontre as funções semelhantes sobre as quais leu neste tutorial, para o guiar e descobrir como empregá-la na sua aplicação companheira favorita.