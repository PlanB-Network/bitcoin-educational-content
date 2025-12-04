---
name: Ashigaru - Ricochete
description: Compreender e utilizar as transacções Ricochete
---
![cover ricochet](assets/cover.webp)



> *Uma ferramenta premium que acrescenta um histórico adicional à sua transação. Atrapalhe as listas negras e ajude a proteger-se contra o encerramento injusto de contas de terceiros

## O que é um Ricochete?



Ricochete é uma técnica que consiste em efetuar várias transacções fictícias para si próprio para simular uma transferência de propriedade de bitcoin. Esta ferramenta difere das outras transacções de Ashigaru (herdadas do Samurai Wallet) na medida em que não proporciona anonimato prospetivo, mas sim uma forma de anonimato retrospetivo. De facto, o Ricochet esbate as especificidades que podem comprometer a fungibilidade de uma peça Bitcoin.



Por exemplo, se fizer um coinjoin, a sua peça que sai da mistura será identificada como tal. As ferramentas de análise de cadeias são capazes de detetar os padrões das transacções coinjoin e atribuir um rótulo às peças que delas saem. Com efeito, o coinjoin visa quebrar as ligações históricas de uma moeda, mas a sua passagem pelos coinjoins continua a ser detetável. Por analogia, este fenómeno é semelhante à encriptação de um texto: embora o texto original não possa ser acedido em texto claro, é fácil identificar que foi aplicada uma encriptação.



O rótulo "coinjoined" pode afetar a fungibilidade de um UTXO. As entidades reguladas, como as plataformas de câmbio, podem recusar-se a aceitar um UTXO coinjoined, ou mesmo exigir explicações ao seu proprietário, com o risco de ver a sua conta bloqueada ou os seus fundos congelados. Nalguns casos, a plataforma pode mesmo denunciar o seu comportamento às autoridades estatais.



É aqui que entra o método Ricochet. Para atenuar a marca deixada por uma coinjoin, a Ricochet executa quatro transacções sucessivas em que o utilizador transfere os seus fundos para si próprio em endereços diferentes. Após esta sequência de transacções, a ferramenta Ricochet encaminha finalmente os bitcoins para o seu destino final, como uma plataforma de troca. O objetivo é criar uma distância entre a transação original de junção de moedas e o ato final de despesa. Desta forma, as ferramentas de análise da cadeia de blocos assumirão que houve provavelmente uma transferência de propriedade após a junção de moedas e que, por conseguinte, não há necessidade de tomar medidas contra o emissor.



![image](assets/fr/01.webp)



Perante o método Ricochet, poder-se-ia imaginar que o software de análise de cadeias aprofundaria o seu exame para além de quatro ressaltos. No entanto, estas plataformas enfrentam um dilema na otimização do limiar de deteção. Precisam de estabelecer um número limite de saltos após o qual aceitam que provavelmente ocorreu uma mudança de propriedade e que a ligação a uma coinjoin anterior deve ser ignorada. No entanto, a determinação deste limiar é arriscada: cada extensão do número de saltos observados aumenta exponencialmente o volume de falsos positivos, ou seja, indivíduos erradamente marcados como participantes numa coinjoin, quando na realidade a operação foi efectuada por outra pessoa. Este cenário representa um grande risco para estas empresas, uma vez que os falsos positivos conduzem à insatisfação, o que pode levar os clientes afectados a procurar a concorrência. A longo prazo, um limiar de deteção demasiado ambicioso leva uma plataforma a perder mais clientes do que os seus concorrentes, o que pode ameaçar a sua viabilidade. Por conseguinte, é complicado para estas plataformas aumentar o número de devoluções observadas, sendo que 4 é frequentemente um número suficiente para contrariar as suas análises.



Assim, **o caso de utilização mais comum da Ricochet surge quando é necessário ocultar uma participação anterior numa coinjoin num UTXO de que se é proprietário**. Idealmente, é melhor evitar a transferência de bitcoins que tenham sido objeto de uma coinjoin para entidades regulamentadas. No entanto, no caso de não haver outra opção, nomeadamente na necessidade urgente de liquidar bitcoins em moeda estatal, a Ricochet oferece uma solução eficaz.



## Como é que o Ricochete funciona no Ashigaru?



O Ricochete é simplesmente um método de envio de bitcoins para si próprio, originalmente inventado pelos criadores do Samurai Wallet. Portanto, é perfeitamente possível simular um Ricochete manualmente, sem a necessidade de uma ferramenta especializada. No entanto, para aqueles que desejam automatizar o processo enquanto desfrutam de um resultado mais polido, a ferramenta Ricochete disponível através da aplicação Ashigaru (que é um Samourai fork) representa uma boa solução.



Uma vez que a Ashigaru cobra pelo seu serviço, um Ricochete custa `100.000 sats` como taxa de serviço, mais uma taxa de mining. A sua utilização é, portanto, recomendada para transferências de montantes significativos.



A aplicação Ashigaru oferece duas variantes de Ricochete:





- Ricochete reforçado, ou "entrega escalonada", que oferece a vantagem de distribuir as taxas de serviço da Ashigaru pelas cinco transacções sucessivas. Esta opção também garante que cada transação é transmitida num momento separado e registada num bloco diferente, imitando o mais possível o comportamento de uma mudança de propriedade. Embora mais lento, este método é preferível para aqueles que não estão com pressa, pois maximiza a eficiência do Ricochete, reforçando a sua resistência à análise em cadeia;





- O Ricochete clássico, que se destina a executar a operação com rapidez, transmitindo todas as transacções num intervalo de tempo reduzido. Este método oferece, por conseguinte, menos confidencialidade e menos resistência à análise do que o método reforçado. Só deve ser utilizado para envios urgentes.



## Como fazer um Ricochete no Ashigaru?



Fazer um ricochete no Ashigaru é muito simples: basta ativar a opção correspondente ao criar uma transação de envio. Para começar, clique no botão `+`, depois em `Enviar`, e selecione a conta da qual deseja enviar os fundos.



![Image](assets/fr/02.webp)



Preencha os dados da transação: o montante a enviar e o endereço final do destinatário após os saltos Ricochete. De seguida, assinale a opção `Ricochete`.



![Image](assets/fr/03.webp)



Pode então escolher entre os dois modos Ricochet discutidos na secção teórica: o Ricochet clássico, em que todas as transacções são incluídas no mesmo bloco, ou a entrega escalonada, que melhora a qualidade do Ricochet à custa de um atraso maior.



Quando tiver feito a sua escolha, prima a seta na parte inferior do ecrã para confirmar.



![Image](assets/fr/04.webp)



No ecrã seguinte, verá um resumo completo da sua transação. É também aqui que pode ajustar a taxa de comissão das suas transacções Ricochet de acordo com as condições do mercado. Se tudo estiver a seu gosto, arraste a seta verde para assinar e distribuir transacções Ricochete.



![Image](assets/fr/05.webp)



Aguardar enquanto os vários saltos são executados automaticamente.



![Image](assets/fr/06.webp)



As suas transacções foram transmitidas com sucesso.



![Image](assets/fr/07.webp)



Agora já conhece a opção Ricochete disponível na aplicação Ashigaru. Para ir mais longe, recomendo que faça o meu curso de formação BTC 204, que lhe ensinará em pormenor como reforçar a sua confidencialidade onchain.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c