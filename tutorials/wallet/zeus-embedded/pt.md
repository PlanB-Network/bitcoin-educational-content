---
name: Zeus Embedded
description: Como utilizar o Lightning Zeus Embedded Wallet
---
![cover-zeus-embedded](assets/cover.webp)



O ZEUS é inicialmente uma aplicação móvel para a gestão remota de nós de iluminação, permitindo-lhe controlar o seu nó instalado num servidor remoto


Mas a aplicação também inclui um "nó incorporado".



**É esta faceta da aplicação que vamos explorar neste tutorial.** Isto permite a qualquer pessoa ter o seu próprio nó de relâmpago no telemóvel, sem necessidade de um servidor dedicado, da mesma forma que a ACINQ oferece o seu incrível Wallet lightning Phoenix.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*Relembrando, a Lightning é uma rede que funciona em paralelo com a Bitcoin, permitindo a troca de bitcoins sem ter de efetuar sistematicamente transacções On-Chain. O resultado são transacções quase instantâneas, sem necessidade de esperar 10 minutos para que um bloco seja validado. Isto é particularmente útil para pagar a um comerciante no mundo físico. Além disso, Lightning oferece um nível notável de **confidencialidade** que a rede Bitcoin não possui nativamente*.



**O Zeus "Integrated"** destina-se aos utilizadores de Bitcoin que pretendem maximizar a sua privacidade e autonomia.


Em suma, é **potencialmente** o telemóvel Wallet dos sonhos dos cypherpunks. Mesmo que ainda esteja na sua infância (versão alfa) e sujeito a alguns bugs, as suas funcionalidades são imensas e não há dúvida de que fará as delícias dos mais intrépidos de entre nós, que querem o máximo de controlo e de opções.



Por outro lado, não me parece que seja atualmente adequado para principiantes que não estejam familiarizados com o Bitcoin e queiram simplesmente uma forma simples de enviar/receber satoshis. No entanto, isto pode mudar no futuro, uma vez que está a ser implementada uma funcionalidade de custódia através do protocolo Cashu (chaumian Ecash) para principiantes...



## Instalar a aplicação



Ir para [o sítio Web do projeto] (https://zeusln.com/) para descarregar a aplicação para o sistema operativo do seu smartphone:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Criação de portefólio



Uma vez iniciada a aplicação, clique no botão "Quick Start" (Início rápido) para começar a criar o Wallet.



![image](assets/fr/03.webp)





Aparece então uma série de ecrãs de inicialização. Aguarde alguns instantes e, em seguida, aguarde alguns minutos até que o nó esteja 100% sincronizado através do Neutrino.



Isto pode demorar alguns minutos. Para informação, o neutrino é uma forma de as carteiras móveis acederem à informação do Blockchain Bitcoin, sem necessitarem de executar um Full node.



![image](assets/fr/04.webp)





Após alguns instantes, está pronto para começar.



![image](assets/fr/05.webp)




## Configuração da aplicação



Pronto, bem, não é bem assim, porque escusado será dizer que um utilizador de Zeus digno desse nome navega na sua Wallet com classe e estilo. Por isso, vamos ter de mudar o avatar dele.



Clique no seu avatar no canto superior direito do ecrã:



![image](assets/fr/06.webp)





Clique na roda dentada e depois no sinal de mais "+" :



![image](assets/fr/07.webp)





Selecione a fotografia mais bonita de Zeus para representar este Wallet e clique em "ESCOLHER FOTO" na parte inferior do ecrã, depois volte atrás clicando na seta no canto superior direito.



![image](assets/fr/08.webp)





Por fim, atribua uma alcunha ao seu Wallet e clique em "SAVE Wallet CONFIG" para que a alteração tenha efeito. Por fim, clique na seta para trás no canto superior esquerdo para regressar ao ecrã inicial.



![image](assets/fr/09.webp)





Desta vez, podemos realmente começar.



![image](assets/fr/10.webp)



### Biometria



Para proteger o acesso ao seu Wallet, pode adicionar um PIN/palavra-passe e ativar a biometria.



Para o fazer, aceda ao menu principal do Wallet clicando nos traços horizontais no canto superior esquerdo.



![image](assets/fr/11.webp)





Selecione "Definições", depois "Segurança" e, por fim, "Definir/Alterar PIN".



![image](assets/fr/12.webp)





Crie o seu PIN, confirme-o e active a biometria premindo o botão "Biometria" correspondente.  Regressar ao menu principal, utilizando a seta no canto superior esquerdo.



![image](assets/fr/13.webp)




### Guardar a frase Mnemonic



Quando estiveres de volta ao menu principal, clica em "Back up Wallet", depois lê o texto de aviso que te informa que perder as 24 palavras que estás prestes a receber equivale a perder o acesso aos teus fundos, e que qualquer pessoa que tenha estas palavras para além de ti pode aceder aos teus fundos. Nunca as dês a ninguém.



Selecione "I UNDERSTAND" na parte inferior do ecrã. Depois, clique em cada uma das 24 palavras para as fazer aparecer e anote-as cuidadosamente.



Pode escrevê-lo em papel, ou talvez, para maior segurança, gravá-lo em aço inoxidável para o proteger de incêndios, inundações ou desmoronamentos. A escolha do suporte para o seu Mnemonic dependerá da sua estratégia de segurança, mas se estiver a utilizar o Zeus como uma carteira de despesas com montantes moderados, o papel deverá ser suficiente.



Para mais informações sobre a forma correta de guardar e gerir a sua frase Mnemonic, recomendo vivamente que siga este outro tutorial, especialmente se for um principiante:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



Uma vez terminado, clique em "I'VE BACKUP MY 24 WORDS" na parte inferior do ecrã, e estamos de volta ao ecrã inicial, prontos para receber os nossos primeiros bitcoins.




## Opção 1 - Receber bitcoins On-Chain e abrir um canal Lightning



**O Zeus Embedded** foi concebido principalmente como um nó de relâmpago incorporado, mas também pode ser utilizado como um Wallet On-Chain.



Para receber bitcoins On-Chain, clique no botão "On-Chain" e depois em "Receber".


Por fim, digitalize o código QR ou copie o Bitcoin Address para depositar fundos.



![image](assets/fr/15.webp)





Uma vez que os fundos tenham sido confirmados e creditados no seu Wallet, pode usá-los para abrir um **Canal Lightning**. O seu canal Lightning é a sua porta de entrada para o Lightning Network, permitindo-lhe Exchange bitcoins de uma forma muito mais confidencial e rápida.





- Para o fazer, clique em "MOVE On-Chain FUNDS TO LIGHTNING"



No ecrã seguinte, é-lhe pedido que abra um canal em colaboração com **"Olympus by Zeus "**, o LSP (Lightning Service Provider) preferido pelo Wallet.


Para este tutorial, vamos escolher esta opção por uma questão de simplicidade, mas é perfeitamente possível abrir canais com qualquer nó na rede.


É mesmo possível abrir vários canais numa única transação, selecionando "OPEN ADDITIONAL CHANNEL". *Mas veremos isso numa versão "avançada" do tutorial **Zeus Embedded***.





- Em seguida, selecione o montante que pretende dedicar a este canal. No nosso caso, todos os nossos fundos On-Chain serão utilizados, pelo que activamos o botão "Utilizar todos os fundos possíveis".





- Por fim, selecione o botão "OPEN CHANNEL" na parte inferior do ecrã.



![image](assets/fr/16.webp)





Em segundos, o canal é estabelecido e estamos prontos para fazer as nossas primeiras transacções Lightning. No ecrã inicial, podemos ver um pequeno relógio junto ao nosso saldo Wallet. Isto deve-se ao facto de ainda precisarmos de esperar por 3 confirmações On-Chain antes de o canal estar verdadeiramente funcional.



![image](assets/fr/17.webp)





Após as 3 confirmações, verificamos que o nosso saldo é agora creditado na inserção Lightning.



![image](assets/fr/18.webp)



Um pequeno pormenor: quando clicamos no menu na parte inferior do ecrã para ver o estado dos nossos canais relâmpago, vemos que uma pequena parte do nosso saldo não está disponível para gastar: só podemos gastar 208253 satoshis em vez dos 210370 que temos. Isto é normal, pois é específico do protocolo Lightning.



Por fim, é de salientar que o nosso parceiro Olympus reserva-se o direito de fechar o canal à sua discrição, caso não esteja a ser utilizado, por exemplo. Para garantir a manutenção do nosso canal, teremos de pagar ao LSP (Lightning Service Provider), como veremos no parágrafo seguinte, através da 2ª via de abertura de canal.





## Enviar bitcoins via Lightning



Agora que já temos o nosso canal a funcionar, vamos ver como o podemos utilizar para pagar um raio Invoice (Invoice).



Para o fazer, clique no botão "Relâmpago" e, em seguida, em "Enviar".



![image](assets/fr/19.webp)





No ecrã seguinte, copie o seu Invoice para o campo reservado ou digitalize-o clicando no ícone no canto superior direito. Por fim, deslize o botão "Slide to Pay" para a direita para efetuar o pagamento.



![image](assets/fr/20.webp)






Espere alguns segundos e o Invoice é pago, e os seus satoshis viajaram à velocidade da luz.



![image](assets/fr/21.webp)





O Zeus permite-lhe então adicionar uma nota para denominar o seu pagamento, ou ver o percurso que os seus satoshis fizeram antes de chegarem ao seu destino (e as taxas cobradas por todos os nós intermédios). Este é o tipo de funcionalidade que adoramos no Wallet.



![image](assets/fr/22.webp)



Note-se que, ao contrário de um Wallet como [Phoenix]([Plan ₿ Network - Phoenix](https://planb.network/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), com Zeus a rota é calculada localmente e não delegada a um terceiro (ACINQ no caso de Phoenix). Assim, só o utilizador conhece o destinatário do pagamento. Perde-se um pouco de eficácia (os pagamentos demoram um pouco mais a ser efectuados, mas ganha-se muito em termos de privacidade).





Ao clicar na pequena seta na parte inferior do ecrã inicial, pode também ver o nosso histórico de pagamentos. Aqui vemos em Green os 212.121 Sats recebidos pelo On-Chain, depois em vermelho, respetivamente, os 211.756 Sats utilizados para abrir o nosso canal, depois os 121.212 satoshis utilizados para pagar o nosso relâmpago Invoice.



![image](assets/fr/23.webp)





## Opção 2 - Receber bitcoins diretamente no Lightning



Em vez de abrir um canal manualmente, como acabámos de ver, é possível receber fundos diretamente via Lightning, mesmo sem um canal pré-existente, utilizando o Olympus, o Zeus LSP.




- Para tal, clique no botão "Relâmpago" no ecrã inicial e, em seguida, em "Receber".
- Em seguida, escolha o montante que deseja receber na caixa "Montante" e selecione o botão "CRIAR Invoice" na parte inferior do ecrã.



![image](assets/fr/24.webp)





O ecrã seguinte mostra os Invoice a pagar para receber os satoshis. É-nos dito que o LSP reterá 10.000 Sats se o pagamento for efectuado por Lightning. Veremos mais tarde como se justificam estas taxas de abertura de canais.



Paga os Invoice ou pede a outra pessoa que os pague, e o canal será aberto automaticamente, mas deduzindo os 10.000 Sats como acordado.



![image](assets/fr/25.webp)





Estamos agora à frente de 2 canais de relâmpagos, cujo estado pode ser verificado clicando no botão indicado pela seta branca na parte inferior do ecrã inicial.



Podemos ver que, ao contrário do canal aberto a partir da nossa balança On-Chain, o canal aberto diretamente através de um raio não apresenta qualquer aviso.


Uma vez que pagou para criar este canal, o fornecedor de serviços Lightning (LSP) compromete-se a manter o canal durante 3 meses e oferece-lhe "liquidez de entrada". No canal inferior, pode ver que a capacidade de receção é de 96383 satoshis. Assim, o LSP mobilizou capital para lhe permitir receber pagamentos diretamente após a abertura do canal.



Assim, os 10 000 Satoshi de taxas pagas cobrem: o custo de abertura do canal (transação Bitcoin On-Chain, a garantia de manutenção do canal durante 3 meses e o bloqueio do capital).



![image](assets/fr/26.webp)





Parabéns, está agora pronto para utilizar o Zeus Embedded, o sistema de iluminação móvel Wallet com as funcionalidades mais avançadas do mercado.





Para saber mais sobre o funcionamento técnico do Lightning Network, pode encontrar a excelente formação gratuita de Fanis Michalakis sobre o Plan ₿ Network:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb