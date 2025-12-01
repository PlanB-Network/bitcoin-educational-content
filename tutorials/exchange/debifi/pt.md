---
name: Debifi
description: Obter um empréstimo sem custódia garantido pelo Bitcoin.
---

![cover](assets/cover.webp)




## Introdução



Durante séculos, os empréstimos tradicionais permitiram financiar muitos projectos. No entanto, continua a ser lento, dispendioso e pouco inclusivo, especialmente para aqueles que não têm acesso a uma infraestrutura bancária sólida.



O surgimento do protocolo Bitcoin deu início a uma nova era financeira, trazendo consigo uma série de desafios. Um desses desafios era como obter liquidez sem ser forçado a vender o Bitcoin, perdendo assim a exposição ao seu potencial de crescimento



O resultado é **Debifi**, uma plataforma que se posiciona como uma alternativa moderna aos bancos. O objetivo é claro: tornar o crédito tão simples e transparente quanto possível, combinando as vantagens do sistema financeiro tradicional com a liberdade oferecida pela Bitcoin. O nome Debifi reflecte esta visão: ***Decentralized Bitcoin Finance***, uma contração que ilustra o encontro entre as finanças descentralizadas e a inovação Bitcoin.



A Debifi é uma plataforma de empréstimo sem custódia apoiada pelo Bitcoin, o que significa que o utilizador mantém o controlo das suas chaves privadas. Permite aos utilizadores desbloquear a liquidez em troca dos seus bitcoins bloqueados como garantia. Ao contrário dos empréstimos bancários tradicionais, a Debifi utiliza um sistema de caução com várias assinaturas (3 em 4) e não aceita a rehipoteca de garantias, garantindo maior segurança e transparência.



Na prática, isto significa que nem a Debifi nem um credor individual podem gastar o seu BTC sem o acordo de três partes (o utilizador, o credor e um terceiro de confiança). Isto torna o sistema mais seguro: se pedir um empréstimo na Debifi, mantém a propriedade do seu Bitcoin até que o empréstimo seja reembolsado na totalidade.



## Vantagens do Debifi



Com o Debifi, você obtém empréstimos garantidos pelo Bitcoin que são garantidos e garantidos pelo on-chain. Seus fundos permanecem seguros com carteiras com várias assinaturas, 2FA e controle total sobre seu Bitcoin - você mantém suas chaves, você mantém suas moedas. Empréstimo em uma variedade de stablecoins ou opções fiduciárias, a taxas competitivas e liquidez global.



Eis uma comparação rápida entre um empréstimo Debifi e um empréstimo bancário tradicional:


| Characteristics        | Loan via Debifi                                                        | Traditional Bank Loan                                                       |
| ---------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Accessibility          | ✔️ Open to any Bitcoin holder (even without banking history)           | ❌ Often limited to clients with physical collateral and strong records      |
| Speed of approval      | ✔️ Funds available within minutes or hours                             | ❌ Lengthy process (days or weeks)                                           |
| Required guarantees    | ✔️ Bitcoin used as the sole collateral                                 | ❌ Physical guarantees (property, land, stable income)                       |
| Asset control          | ✔️ You keep exposure to Bitcoin and its upside potential               | ❌ No connection between the loan and your financial assets                  |
| Geographic flexibility | ✔️ Available everywhere (no banking jurisdiction constraints)          | ❌ Restricted to the bank’s jurisdiction                                     |
| Main risk              | ❌ Liquidation risk if BTC price drops too sharply                      | ❌ Risk of asset seizure or negative impact on credit score                  |

Antes de lhe mostrar passo a passo como contrair um empréstimo no Debifi, há alguns pontos que penso que deve saber.




## Definições





- As comissões de abertura** são encargos únicos cobrados aquando da concessão de um empréstimo e calculados como uma percentagem do montante emprestado. Estas comissões cobrem os custos administrativos, operacionais e de gestão.





- O colateral** é um ativo que se deposita para garantir um empréstimo. No caso da Debifi, a garantia é Bitcoin (BTC), que o mutuário deposita no depósito de garantia Multisig 3/4.





- O sistema Multisig escrow (3/4)** é um mecanismo de depósito seguro em que os bitcoins de um mutuário são colocados num endereço com várias assinaturas. Especificamente, quatro (4) partes detêm uma chave cada (mutuário, mutuante, Debifi, terceiro independente). Para movimentar fundos, são necessárias pelo menos 3 das 4 assinaturas.





- Uma stablecoin** é uma criptomoeda cujo valor está indexado a um ativo estável (por exemplo, o dólar americano), o que evita a volatilidade da Bitcoin. Por exemplo, 1 USDC vale sempre ~$1, uma vez que é apoiado por reservas fiduciárias.





- O rácio empréstimo/valor (LTV)** de um empréstimo determina a quantidade de dinheiro que pode pedir emprestado como garantia para o seu Bitcoin. Rácio LTV = Montante do empréstimo / Montante da garantia * 100. Por exemplo, um rácio LTV de 50% significa que o valor do empréstimo é igual a 50% do valor do Bitcoin depositado.




BTC Sessions vídeo tutorial :



![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)



## Começar a utilizar o Debifi



Para começar a utilizar o Debifi, são necessários alguns pré-requisitos.


### Pré-requisitos



Antes de poder pedir emprestado à Debifi, certifique-se de que possui os seguintes elementos:





- Bitcoin wallet: onde guarda o seu BTC (idealmente sem custódia, por exemplo, Hardware Wallet ou um wallet móvel de confiança). É a partir deste wallet que enviará a garantia do Bitcoin para a Debifi e receberá a garantia de volta.



Pode usar o Aqua, um Bitcoin e Liquid wallet que também suporta a gestão de stablecoin USDT em várias redes. Ou COLDCARD (Mk4 ou Q), atualmente o único hardware suportado pela Debifi.



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3



- KYC (*Know Your Customer*): consoante a oferta de crédito escolhida, pode ser necessário um processo de verificação da identidade. Na Debifi, cada oferta indica se o KYC é necessário ou não. Por isso, prepare-se em conformidade. O KYC é efectuado por prestadores de serviços terceiros fiáveis, como a Sumsub.



![image](assets/fr/03.webp)





- Aplicação de autenticação de dois factores: A Debifi requer um código de autenticação para cada ação importante. É uma camada extra de segurança. Neste tutorial, usaremos o Google Authenticator. Em alternativa, pode utilizar outros que considere adequados.



https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc



- Sítio Web e aplicação móvel Debifi: A Debifi é simultaneamente um sítio Web e uma aplicação móvel, e os dois funcionam em conjunto. A aplicação móvel torna-se um wallet, que armazena a sua chave privada e gere a assinatura dos contratos. Além disso, é necessário utilizar o sítio Web para assinar os contratos (um grande Interface dá-lhe uma visão geral dos contratos de empréstimo e das suas especificidades).





- A aplicação móvel Debifi (iOS/Android) é necessária para contrair um empréstimo. É necessário descarregar a aplicação, criar uma conta e "associar" o seu dispositivo (registar o dispositivo na sua conta). A aplicação Debifi suporta a autenticação de dois factores (2FA) e, sem um smartphone, não é possível confirmar as transacções na Debifi.



### Criar uma conta



Visitar [o sítio Web oficial da Debifi] (https://debifi.com/app).



![image](assets/fr/04.webp)



Instale a sua aplicação de acordo com o tipo de smartphone que possui e, em seguida, abra-a.



![image](assets/fr/05.webp)



![image](assets/fr/06.webp)



Uma vez na aplicação, clique no menu **Configurações**.



![image](assets/fr/07.webp)



Em seguida, clique em **Login ou criar conta** para criar uma conta com o seu endereço de correio eletrónico.



![image](assets/fr/08.webp)



![image](assets/fr/09.webp)



![image](assets/fr/10.webp)



Receberá um código de verificação por correio eletrónico. Copia e cola este código na aplicação. Em seguida, abra a aplicação Debifi no seu smartphone e inicie sessão.



![image](assets/fr/11.webp)



### Proteger a sua conta



Por razões de segurança, a Debifi pedir-lhe-á que siga três passos.



![image](assets/fr/12.webp)





- Em primeiro lugar, terá de definir um código PIN forte para aceder à sua aplicação mais tarde.



![image](assets/fr/13.webp)





- Em seguida, configure a autenticação de dois factores (2FA) para associar o seu dispositivo à sua conta utilizando o código 2FA.



![image](assets/fr/14.webp)





- Por fim, guarde as 12 palavras da sua chave privada, escrevendo-as num suporte fiável e guardando-as num local seguro. Esta fase é essencial para recuperar a sua conta e gerir os seus fundos.



![image](assets/fr/15.webp)





- Para maior segurança, pode mesmo adicionar um passphrase.



![image](assets/fr/16.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Tenha em atenção que apenas o seu smartphone registado poderá abrir a sua conta (uma medida de segurança adicional).



Uma vez concluídas estas etapas, clique no menu **Ofertas** para ver as ofertas de crédito disponíveis. Ao clicar numa oferta, será redireccionado para o site da Debifi.



![image](assets/fr/17.webp)



### Aceder ao sítio Web e explorar as ofertas de empréstimos



Quando o seu dispositivo estiver ligado, aceda ao [sítio Web da Debifi] (https://debifi.com/). Inicie sessão para estabelecer uma ligação segura entre a aplicação móvel Debifi e a plataforma web. Desta forma, é mais fácil interagir com as ofertas de crédito disponíveis (uma visão clara dos detalhes de cada oferta) e gerir a sua conta.



![image](assets/fr/18.webp)



![image](assets/fr/19.webp)



![image](assets/fr/20.webp)



![image](assets/fr/21.webp)




Tutorial em vídeo sobre como iniciar sessão com a sua conta na plataforma :



![video](https://youtu.be/cUwCfTKDAOo)



## Pedido de empréstimo



A plataforma coloca-o em contacto com liquidez de qualidade institucional e oferece uma gama de opções que se adequam às suas necessidades. Navegue para descobrir o que está disponível. Tem também a flexibilidade de ajustar os parâmetros do empréstimo de acordo com a sua tolerância ao risco individual e a sua situação financeira.



![image](assets/fr/22.webp)



As moedas fiduciárias que a Debifi oferece atualmente podem ser visualizadas na plataforma.



![image](assets/fr/23.webp)



### Cláusulas contratuais claras e flexíveis



A Debifi baseia-se em condições de empréstimo transparentes e flexíveis para satisfazer as necessidades de cada uma das partes (mutuante e mutuário). As principais cláusulas incluem :



#### Rácio empréstimo/valor (LTV)


As fracções do empréstimo Bitcoin são geralmente em número de três (3):





- Conservador (30% - 40% LTV), que corresponde a um empréstimo de baixo risco, é ideal para maximizar a segurança contra a volatilidade dos preços do Bitcoin;





- Equilibrado (50% LTV) ;





- Agressiva (70% LTV), que oferece uma maior liquidez, mas comporta um risco muito elevado de liquidação em caso de queda do mercado. O acompanhamento ativo das condições de mercado do Bitcoin é indispensável para a escolha desta fração.



#### Taxas de juro



A fixação das taxas depende geralmente do LTV escolhido, da duração do empréstimo, da volatilidade das garantias e das avaliações de risco específicas da plataforma. As taxas permanecem fixas durante o período do empréstimo.



#### Prazo do empréstimo e flexibilidade de reembolso



Os planos de reembolso são flexíveis e concebidos para se adaptarem às necessidades do mutuário. Os empréstimos podem ser total ou parcialmente reembolsados em qualquer altura sem encargos adicionais, desde que os requisitos de garantia continuem a ser cumpridos. Durante o prazo do empréstimo, os juros são normalmente pagos periodicamente, enquanto o capital é liquidado no vencimento.



#### Direitos de liquidação (valores de cobertura adicionais)



Dada a volatilidade do Bitcoin, os empréstimos incluem uma política de valores de cobertura adicionais claramente definida. Uma chamada de margem ocorre quando o LTV aumenta devido a um declínio no valor da garantia. A Debifi notifica o mutuário por correio eletrónico e através da aplicação, permitindo-lhe adicionar garantias ou reembolsar parte do empréstimo.


75% LTV - Primeiro alerta

80% LTV - Segunda indicação

85% LTV - Alerta final

90% LTV - A garantia é liquidada



### Lançamento do processo de empréstimo



Para selecionar uma oferta de empréstimo que se adeqúe às suas necessidades, clique nela para ver as suas caraterísticas.



![image](assets/fr/24.webp)



Pode ver :


1. Nome da instituição mutuante ;


2. O montante do empréstimo varia;


3. Que receberá os fundos em USDC Ethereum ;


4. O período do empréstimo, a taxa de juro e o rácio LTV;


5. Esta oferta requer KYC;


6. Deve ser introduzido o montante exato de que necessita (este montante deve estar dentro da margem, ver 2);


7. Deve ser introduzido o endereço Ethereum USDC a utilizar para receber os fundos.



Quando estiver satisfeito com a oferta e tiver preenchido as informações necessárias, clique em "Pedido Contract".



![image](assets/fr/25.webp)



Regressar à aplicação móvel para ''**Fornecer chave pública**''.



![image](assets/fr/26.webp)



Prima '' **Fornecer chave pública** '' e, em seguida, escolha a fonte da chave pública. O mutuante também terá de fornecer uma chave pública.



![image](assets/fr/27.webp)



![image](assets/fr/28.webp)



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



A etapa seguinte é a assinatura do contrato. Ainda na aplicação móvel, prima '' **Assinar Contract** ''



![image](assets/fr/31.webp)



![image](assets/fr/32.webp)



Quando termina de assinar o contrato, a Debifi cria automaticamente um endereço Bitcoin multi-assinatura único (escrow 3-sur-4) para o seu contrato. Enquanto os seus bitcoins estiverem no escrow, não podem ser utilizados noutro local.



### Depósito da garantia e receção dos seus fundos



O passo final é depositar a sua garantia Bitcoin no sistema de caução multi-assinatura. Debifi mostra-lhe o endereço do depósito de garantia (B) e a quantidade de BTC (A) a ser enviada como (garantia + comissão).



![image](assets/fr/33.webp)



Receberá também esta notificação na sua aplicação móvel.



![image](assets/fr/34.webp)



Assim que o seu depósito for confirmado, o mutuante pagará o montante do empréstimo no endereço de receção que indicou, finalizando a transação e dando-lhe acesso aos fundos de que necessita.



Receberá então uma notificação da Debifi, pedindo-lhe que pague as taxas ou comissões do empréstimo para fazer avançar o estado do seu empréstimo.



Na realidade, uma vez criado o contrato, os encargos do empréstimo são automaticamente deduzidos da garantia depositada pelo mutuário no endereço de garantia multi-assinatura.



Basta assinar uma transação que permitirá à Debifi deduzir a sua comissão da garantia. Por seu lado, o seu mutuante também terá de assinar a transação de dedução da comissão, caso contrário a Debifi não poderá receber a sua comissão.



![image](assets/fr/35.webp)



As comissões de empréstimo aplicáveis são de 1,5-2%, consoante o prazo do contrato. A plataforma cobra comissões apenas em Bitcoin.



## Acompanhamento de empréstimos



Quando o empréstimo está ativo, a Debifi permite-lhe acompanhar o seu contrato em tempo real. Na interface, encontra:



- O montante do empréstimo e o prazo restante.
- O rácio LTV (Loan-to-Value) atual, que aumenta quando o preço do BTC diminui e o valor da sua garantia desce.




Os mutuários são notificados quando o valor da garantia diminui, e esta informação também é apresentada na página de resumo do contrato. Para repor o rácio empréstimo/valor original, o mutuário deve



- depositar garantias adicionais;
- reembolsar a totalidade ou parte da dívida.




Em caso de aumento do preço da garantia, o mutuário retém as mais-valias sobre a garantia. Deve apenas o montante do empréstimo, que é pré-determinado e independente do preço Bitcoin.




## Reembolso e recuperação de garantias



No final do prazo acordado (ou antes, se o desejar), deve reembolsar o empréstimo.


Em Debifi :





- Aceda ao seu contrato e clique em **Fazer um reembolso**. Introduzir o montante total devido (capital + juros).





- Enviar as stablecoins do seu wallet para o endereço do credor indicado e voltar a confirmar o reembolso na plataforma, copiando o **ID** da transação de reembolso para o separador dedicado. Desta forma, é mais fácil para a Debifi efetuar os seus controlos.



Uma vez confirmado o pagamento pelo mutuante (e por si), a Debifi pedir-lhe-á então o **reembolso**. A tua garantia Bitcoin é libertada e podes devolvê-la do depósito de garantia para a tua própria wallet.  Não te esqueças de recolher todos os teus Bitcoins.



Assim que receberes os teus bitcoins, o contrato de empréstimo muda para **Contract concluído**.



Parabéns! Finalizou o processo.




## Boas práticas e segurança



Quaisquer que sejam os seus objectivos ou motivações - financiamento de um projeto, aquisição de propriedades, compra de bitcoins, etc. - tenha muita cautela antes de contrair um empréstimo garantido pelo Bitcoin. Avalie cuidadosamente a sua decisão, pois o Bitcoin continua a ser um ativo volátil. **Uma queda acentuada no seu preço pode resultar na liquidação forçada dos seus bitcoins



Monitorizar o rácio empréstimo/garantia (LTV). Se possível, crie alertas (preço BTC, LTV). Não deixe que o seu rácio se aproxime dos 90%. Em caso de dúvida, aumente a garantia ou pague mais cedo.



Controle as suas chaves. Guarde as suas BTC num wallet seguro (idealmente hardware ou um wallet com boa reputação). Não defina um código PIN relacionado com uma data importante da sua vida e nunca partilhe a sua frase de recuperação. Na Debifi, você generate a sua chave privada na aplicação - a Debifi não a conhece.



Se possível, comece com pouco dinheiro. Para o seu primeiro empréstimo, teste um montante modesto para se familiarizar com o processo.



Utilize apenas o sítio Web oficial da Debifi para se manter a par das notícias da Debifi e evite ligações desconhecidas ou de phishing.  Actualize a aplicação, proteja o seu smartphone com um código PIN e escolha um Hardware Wallet compatível.



Alternativamente, se você é um credor, este vídeo tutorial irá guiá-lo através do uso da plataforma Debifi. Desde a seleção de mutuários interessados na sua oferta, ao fornecimento de chaves públicas, assinatura de acordos, transferência de stablecoins e muito mais.



![video](https://youtu.be/g8iLxwI4xT0)



Já sabe como utilizar a plataforma Debifi para obter um empréstimo.



Recomendo que faça este curso, que analisa em profundidade o Bitcoin, as Stablecoins e o seu contributo para a soberania.



https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46