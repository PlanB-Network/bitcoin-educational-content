---
name: Ashigaru - Whirlpool Coinjoin
description: Como é que posso fazer coinjoins na aplicação Ashigaru?
---

![cover](assets/cover.webp)



"*um wallet de bitcoin para as ruas*"



Neste tutorial, vais aprender o que é uma coinjoin e como fazer uma com a aplicação Terminal Ashigaru e a implementação do Whirlpool, um protocolo de coinjoin herdado do Samourai Wallet.



## Como funcionam as juntas homólogas Whirlpool



Neste tutorial, não voltarei a abordar a noção de coinjoin, a sua utilidade ou o funcionamento teórico do Whirlpool, uma vez que estes tópicos já foram explicados em pormenor na Parte 5 do curso de formação BTC 204 na Plan ₿ Academy. Se ainda não domina o funcionamento do Whirlpool ou o princípio de um coinjoin, recomendo vivamente que consulte esta parte 5 antes de continuar :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

No entanto, aqui estão alguns factos e números rápidos que podem ser úteis.



As carteiras compatíveis com o Whirlpool utilizam 4 contas separadas para satisfazer as necessidades do processo de coinjoin:




- A conta **Deposit**, identificada pelo índice `0'` ;
- A conta do **Banco Mau** (ou *câmbio tóxico*), identificada pelo índice `2.147.483.644'` ;
- A conta **Premix**, identificada pelo índice `2 147 483 645'` ;
- A conta **Postmix**, identificada pelo índice `2 147 483 646'`.



Em Ashigaru, em novembro de 2025, estão disponíveis duas denominações de bilhar (esta lista irá provavelmente evoluir nos próximos meses: não se esqueça de verificar os valores enquanto lê):




- 0.25 BTC`, com uma taxa de entrada de `0.0125 BTC`;
- 0.025 BTC, com uma taxa de entrada de 0,00125 BTC.



Cada ciclo de mistura pode envolver entre 5 e 10 UTXOs na entrada e na saída.



![Image](assets/fr/01.webp)



## Requisitos de software



Para fazer coinjoins com o Whirlpool, são necessários três programas separados:





- Ashigaru Terminal**, que lhe permite gerir as suas moedas diretamente a partir do seu computador;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, a aplicação no teu smartphone com a qual podes gastar os teus bitcoins em *postmix* a partir de qualquer lugar ;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, uma implementação de nó Bitcoin que lhe garante uma ligação soberana à rede, sem dependência de um servidor de terceiros.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Instale cada uma destas ferramentas seguindo os respectivos tutoriais e, em seguida, pode começar a fazer os seus primeiros coinjoins.



## Receber bitcoins



Depois de criar a sua carteira, começará com uma única conta, identificada pelo índice `0'`. Esta é a conta `Deposit`. É para esta conta que enviará bitcoins destinados a coinjoins. Pode recebê-los através da aplicação Ashigaru (ver parte 5 do tutorial dedicado), ou através do Terminal Ashigaru (também detalhado na parte 5 do tutorial dedicado).



Quando a sua conta de depósito contiver, pelo menos, o montante necessário para participar na pool mais pequena (mais taxas de serviço e o mínimo necessário para cobrir os custos do mining), estará pronto para iniciar as suas primeiras adesões.



![Image](assets/fr/02.webp)



## Fazer o Tx0



Assim que os fundos tiverem chegado à sua conta de depósito e a transação tiver sido confirmada, pode iniciar o processo de junção de moedas. Para tal, no Terminal Ashigaru, abra o menu "Carteiras" e selecione o seu wallet. Se o seu wallet estiver bloqueado, o software pedir-lhe-á a sua palavra-passe e o passphrase.



![Image](assets/fr/03.webp)



Em seguida, selecione a conta `Deposit`.



![Image](assets/fr/04.webp)



Aceder ao menu `UTXOs`.



![Image](assets/fr/05.webp)



Aqui verá uma lista de todos os UTXOs na sua conta de depósito. Selecione os que pretende enviar nos ciclos de coinjoin.



Para uma maior confidencialidade e para evitar a *Common Input Ownership Heuristic (CIOH)*, recomenda-se a utilização de apenas um UTXO por entrada no Whirlpool (uma explicação pormenorizada deste princípio pode ser encontrada na BTC 204).



Prima a tecla `ENTER` do seu teclado para selecionar um UTXO: aparecerá um asterisco `(*)` ao lado do mesmo para indicar que está selecionado.



![Image](assets/fr/06.webp)



Em seguida, clique no botão `Mistura selecionada`.



![Image](assets/fr/07.webp)



Se tiver um UTXO suficientemente grande para participar numa das duas pools disponíveis, pode selecionar a pool de destino utilizando as setas. Nesta página, verá os detalhes do seu Tx0 :




- o número de UTXOs que entrarão na reserva;
- as diferentes taxas aplicadas (taxas de serviço e taxas mining) ;
- a quantidade da *alteração tóxica*.



Verifique cuidadosamente as informações e, em seguida, clique em `Broadcast` para transmitir o Tx0.



![Image](assets/fr/08.webp)



Ashigaru mostrará então o TXID do seu Tx0, confirmando que a transação foi transmitida na rede.



![Image](assets/fr/09.webp)



## Fazer coinjoins



Quando o Tx0 tiver sido transmitido, volte à página inicial da sua conta de depósito, clique em `Contas` e selecione a conta `Premix`.



![Image](assets/fr/10.webp)



No menu `UTXOs`, verá as várias partes equalizadas, prontas a entrar nos ciclos de coinjoin. Assim que Tx0 for confirmado, o Terminal Ashigaru iniciará automaticamente o seu primeiro ciclo de mistura.



![Image](assets/fr/11.webp)



Uma vez que o Tx0 tenha sido confirmado, a primeira transação de coinjoin será criada e transmitida automaticamente pelo Terminal Ashigaru. Ao ir a `Contas > Postmix > UTXOs`, pode ver os seus UTXOs equalizados, aguardando a confirmação do seu primeiro ciclo.



![Image](assets/fr/12.webp)



Pode agora deixar o Ashigaru Terminal a funcionar em segundo plano: ele continuará a misturar e a remisturar as suas faixas automaticamente.



## Acabamento de uniões



Agora pode deixar que as suas moedas se remisturem automaticamente. O modelo Whirlpool significa que não existem encargos adicionais para a remistura: sem taxas de serviço, sem taxas mining. Assim, permitir que as suas moedas participem em mais ciclos de mistura só pode beneficiar a sua confidencialidade.



Para uma melhor compreensão deste mecanismo e de quantos ciclos vale a pena esperar, recomendo a leitura deste artigo:



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Para ver o número de remixes realizados por cada uma das suas peças, abra o menu `UTXOs` na conta `Postmix`.



![Image](assets/fr/13.webp)



Para gastar as suas moedas mistas, dirija-se à aplicação Ashigaru, que utiliza o mesmo wallet que o seu software do Terminal Ashigaru. O wallet apresentado na abertura corresponde à sua conta `Deposit`. Para aceder à conta `Postmix`, que contém os seus UTXOs mistos, clique no símbolo Whirlpool no canto superior direito.



![Image](assets/fr/14.webp)



Nesta conta, verá todas as suas moedas atualmente misturadas. Para as gastar, prima o símbolo `+` no canto inferior direito do ecrã e selecione `Enviar`.



![Image](assets/fr/15.webp)



Preencha os detalhes da sua transação: o endereço do destinatário, o montante a enviar e, se desejar, escolha uma estrutura de transação específica para aumentar ainda mais a sua confidencialidade (ver os tutoriais correspondentes).



![Image](assets/fr/16.webp)



Verifique cuidadosamente os detalhes da transação e, em seguida, arraste a seta na parte inferior do ecrã para confirmar o envio.



![Image](assets/fr/17.webp)



A sua transação foi assinada e transmitida na rede Bitcoin.



![Image](assets/fr/18.webp)



## Gastar mudança tóxica



Lembre-se: O modelo do Whirlpool baseia-se na equalização das suas peças em Tx0, antes de entrarem nos pools. É este mecanismo que quebra o controlo dos UTXOs. Na minha opinião, este é o modelo de coinjoin mais eficiente, mas tem uma desvantagem: gera uma *mudança* que não passa pelo processo de coinjoin.



Esta alteração corresponde a um UTXO criado para cada Tx0. É isolada numa conta específica denominada `Doxxic Change` ou `Bad Bank`, consoante o software, para evitar a sua utilização com os seus outros UTXOs. Isto é muito importante, porque estes UTXOs não foram misturados: as suas ligações de rastreabilidade permanecem intactas, e podem comprometer a sua confidencialidade ao estabelecer uma ligação entre si e a sua atividade de coinjoin. Por isso, manuseie-os com cuidado e **nunca os utilize com outros UTXOs**, quer estejam misturados ou não. Combinar um UTXO tóxico com um UTXO misto anulará todos os ganhos de privacidade que obtiveste com o coinjoin.



De momento, o Ashigaru não oferece acesso direto a esta conta `Doxxic Change` (pelo menos, não a encontrei). Esta funcionalidade será provavelmente adicionada numa futura atualização. Entretanto, a única forma de recuperar estes fundos é importar o teu seed para o Sparrow Wallet. Este último irá normalmente detetar automaticamente que este é um wallet usado com o Whirlpool e dar-te-á acesso a todas as quatro contas, incluindo a conta `Doxxic Change`. Podes então gastar estes UTXOs como bitcoins normais a partir do Sparrow.



Aqui estão várias estratégias possíveis para gerir os seus UTXOs de moeda estrangeira a partir de coinjoins sem comprometer a sua privacidade:





- Misturando-os em pools mais pequenos:** Se o seu UTXO tóxico for suficientemente grande para se juntar a um pool mais pequeno, esta é geralmente a melhor opção. Tenha cuidado, no entanto, para nunca fundir vários UTXOs tóxicos para o conseguir, pois isso criará uma ligação entre as suas várias entradas no Whirlpool.





- Marque-os como não gastáveis:** Outra abordagem prudente é simplesmente mantê-los como estão na sua conta separada e deixá-los intocados. Isto evitará que os gaste acidentalmente. Se o valor do bitcoin aumentar, poderão ser abertos novos pools adaptados à sua dimensão.





- Fazer doações:** Pode optar por transformar estes UTXOs tóxicos em doações a programadores Bitcoin, projectos de código aberto ou associações que aceitem BTC. Isto permite-lhe eliminá-los de forma útil enquanto apoia o ecossistema.





- Comprar cartões-presente pré-pagos ou cartões Visa:** Plataformas como [Bitrefill](https://www.bitrefill.com/) permitem-lhe trocar os seus bitcoins por cartões-presente ou cartões Visa recarregáveis que podem ser utilizados em lojas. Esta pode ser uma forma simples e discreta de gastar os seus UTXOs tóxicos.





- Trocá-los por Monero:** Samourai Wallet costumava oferecer um serviço de troca atómica BTC/XMR, agora extinto. Se existir um serviço semelhante (não conheço nenhum pessoalmente), é uma excelente solução para isolar esses UTXOs, convertendo-os em Monero e, eventualmente, enviando-os de volta ao Bitcoin. No entanto, este método era caro e dependia da liquidez disponível.





- Transferi-los para o Lightning Network:** Transferir estes UTXOs para o Lightning Network para beneficiar de taxas de transação reduzidas é uma opção potencialmente interessante. No entanto, este método pode revelar certas informações, dependendo da sua utilização do Lightning, pelo que deve ser utilizado com precaução.



## Como posso saber mais sobre a qualidade dos nossos ciclos de coinjoin?



Para que um coinjoin seja verdadeiramente eficaz, deve apresentar um elevado grau de uniformidade entre os montantes de entrada e de saída. Esta uniformidade aumenta o número de interpretações possíveis para um observador externo, o que, por sua vez, aumenta a incerteza sobre a transação. Para medir esta incerteza, utilizamos o conceito de entropia aplicado à transação. O modelo Whirlpool é reconhecido como um dos mais eficazes neste aspeto, pois garante uma excelente homogeneidade entre os participantes. Para uma análise mais aprofundada deste princípio, recomendo que consulte o último capítulo da Parte 5 do curso de formação BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

O desempenho de vários ciclos de junção de moedas é medido pelo tamanho dos conjuntos em que uma moeda está escondida. Estes conjuntos definem o que se designa por *anonsets*. Existem dois tipos: o primeiro mede a confidencialidade face à análise retrospetiva (do presente para o passado) e o segundo mede a resistência à análise prospetiva (do passado para o presente). Para uma explicação completa destes dois indicadores, leia o seguinte tutorial (ou, mais uma vez, o curso de formação BTC 204):



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Como gerir o postmix?



Depois de executar vários ciclos de coinjoin, a melhor estratégia é manter seus UTXOs na conta `Postmix`, deixando-os remixar indefinidamente até que você realmente precise gastá-los.



Alguns utilizadores preferem transferir os seus bitcoins mistos para um wallet protegido por hardware wallet. Esta opção é possível, mas requer um certo rigor para garantir que a confidencialidade adquirida com as coinjoins não seja comprometida.



A fusão de UTXOs é o erro mais frequente. É importante nunca combinar UTXOs mistos com UTXOs não mistos na mesma transação, caso contrário, corre o risco de desencadear a *Common Input Ownership Heuristic (CIOH)*. Isto implica uma gestão rigorosa dos seus UTXOs, nomeadamente através de uma rotulagem clara e precisa. De um modo geral, a fusão de UTXOs é uma má prática que conduz frequentemente a uma perda de confidencialidade quando mal gerida.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Deve também ser cauteloso quanto à consolidação de UTXOs mistos. As consolidações limitadas podem ser consideradas se os UTXOs tiverem anonsets significativos, mas reduzem inevitavelmente o seu nível de confidencialidade. Evite consolidações maciças ou apressadas, efectuadas antes de um número suficiente de remisturas, pois podem estabelecer ligações inferenciais entre as suas peças pré-misturadas e pós-misturadas. Em caso de dúvida, é preferível não consolidar os seus UTXOs pós-mistura e transferi-los um a um para o seu hardware wallet, gerando de cada vez um novo endereço de receção em branco. Não se esqueça de etiquetar cada UTXO transferido.



Aconselhamos vivamente a não transferir os seus UTXOs pós-mistura para carteiras que utilizem scripts minoritários. Por exemplo, se participou no Whirlpool a partir de um portfolio multi-sig no `P2WSH`, haverá poucos de vós a partilhar este tipo de script. Ao enviar os seus UTXOs postmix para este mesmo tipo de script, reduz consideravelmente o seu anonimato. Para além do tipo de script, outras impressões digitais específicas do wallet podem comprometer a sua confidencialidade, por isso a melhor coisa a fazer é gastá-las a partir da aplicação Ashigaru.



Por último, tal como em todas as transacções Bitcoin, nunca reutilize um endereço de receção. Cada pagamento deve ser enviado para um endereço novo, único e em branco.



O método mais simples e seguro é deixar os UTXOs misturados descansarem na conta `Postmix`, deixá-los remisturar naturalmente e gastá-los apenas quando necessário do Ashigaru.



As carteiras Ashigaru e Sparrow incorporam salvaguardas adicionais contra os erros mais comuns associados à análise da cadeia de blocos, ajudando-o a preservar a confidencialidade das suas transacções.