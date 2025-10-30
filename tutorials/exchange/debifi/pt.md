---
name: Debifi
description: Obter um empréstimo sem custódia garantido pelo Bitcoin.
---

![cover](assets/cover.webp)




## Introdução



Durante séculos, os empréstimos tradicionais permitiram financiar muitos projectos. No entanto, continua a ser lento, dispendioso e pouco inclusivo, especialmente para aqueles que não têm acesso a uma infraestrutura bancária sólida.



O surgimento do protocolo Bitcoin deu início a uma nova era financeira, trazendo consigo uma série de desafios. Um desses desafios era como obter liquidez sem ser forçado a vender o Bitcoin, perdendo assim a exposição ao seu potencial de crescimento



O resultado é **Debifi**, uma plataforma que se posiciona como uma alternativa moderna aos bancos. O objetivo é claro: tornar o crédito tão simples e transparente quanto possível, combinando as vantagens do sistema financeiro tradicional com a liberdade oferecida pela Bitcoin. O nome Debifi reflecte esta visão: ***Decentralized Bitcoin Finance***, uma contração que ilustra o encontro entre as finanças descentralizadas e a inovação Bitcoin.



A Debifi é uma plataforma de empréstimo sem custódia apoiada pelo Bitcoin, o que significa que mantém o controlo das suas chaves privadas. Permite aos utilizadores desbloquear a liquidez em Exchange para os seus bitcoins bloqueados como garantia. Ao contrário dos empréstimos bancários tradicionais, a Debifi utiliza um sistema de caução com várias assinaturas (3 em 4) e não aceita hipoteca de garantias, garantindo maior segurança e transparência.



Na prática, isto significa que nem a Debifi nem um credor individual podem gastar o seu BTC sem o acordo de três partes (o utilizador, o credor e um terceiro de confiança). Isto torna o sistema mais seguro: se pedir um empréstimo na Debifi, fica com Ownership do seu Bitcoin até o empréstimo ser pago na totalidade.



## Vantagens do Debifi



Com Debifi, são empréstimos garantidos, segurança Blockchain (multisignature, 2FA), uma escolha de stablecoins / líquidos, confidencialidade e controle total de Bitcoin. Debifi "permite que você mantenha seu dinheiro" (suas chaves, suas moedas), enquanto oferece taxas competitivas e acesso global a empréstimos garantidos por BTC.



Eis uma comparação rápida entre um empréstimo Debifi e um empréstimo bancário tradicional:



| Caractéristiques       | Prêt via Debifi                                                       | Prêt bancaire traditionnel                                                 |
| ---------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Accessibilité          | ✔️ Ouvert à tout détenteur de Bitcoin (même sans historique bancaire) | ❌ Souvent réservé aux clients avec garanties physiques et dossiers solides |
| Vitesse d’obtention    | ✔️ Liquide en quelques minutes/heures                                 | ❌ Processus long (jours ou semaines)                                       |
| Garanties exigées      | ✔️ Collatéral en Bitcoin uniquement                                   | ❌ Garanties physiques (maisons, terrains, revenus stables)                 |
| Contrôle de l’actif    | ✔️ Vous conservez l’exposition au Bitcoin et son potentiel de hausse  | ❌ Vous n’avez aucun lien entre le prêt et vos actifs financiers            |
| Souplesse géographique | ✔️ Disponible partout (sans contrainte géographique bancaire)         | ❌ Limité à la juridiction de la banque                                     |
| Risque principal       | ❌ Risque de liquidation si le prix du BTC chute trop                  | ❌ Risque de saisie de biens ou impact négatif sur la cote de crédit        |

Antes de lhe mostrar passo a passo como contrair um empréstimo no Debifi, há alguns pontos que penso que deve saber.




## Definições





- As comissões de abertura** são encargos únicos cobrados aquando da concessão de um empréstimo e calculados como uma percentagem do montante emprestado. Estas comissões cobrem os custos administrativos, operacionais e de gestão.





- A garantia** é um ativo que se deposita para assegurar um empréstimo. No caso da Debifi, a garantia é Bitcoin (BTC), que o mutuário deposita no depósito de garantia Multisig 3/4.





- O sistema Multisig escrow (3/4)** é um mecanismo de depósito seguro em que os bitcoins de um mutuário são colocados num Address com várias assinaturas. Especificamente, quatro (4) partes detêm uma chave cada (mutuário, mutuante, Debifi, terceiro independente). Para movimentar fundos, são necessárias pelo menos 3 das 4 assinaturas.





- Uma stablecoin** é uma criptomoeda cujo valor está indexado a um ativo estável (por exemplo, o dólar americano), o que evita a volatilidade da Bitcoin. Por exemplo, 1 USDC vale sempre ~$1, uma vez que é apoiado por reservas fiduciárias.





- O rácio empréstimo/valor (LTV)** de um empréstimo determina a quantidade de dinheiro que pode pedir emprestado como garantia para o seu Bitcoin. Rácio LTV = montante do empréstimo / montante da garantia * 100. Por exemplo, um rácio LTV de 50% significa que o valor do empréstimo é igual a 50% do valor do Bitcoin depositado.




BTC Sessions vídeo tutorial :



![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)



## Começar a utilizar o Debifi



Para começar a utilizar o Debifi, são necessários alguns pré-requisitos.


### Pré-requisitos



Antes de poder pedir emprestado à Debifi, certifique-se de que possui os seguintes elementos:





- Bitcoin Wallet: onde guarda o seu BTC (idealmente sem custódia, por exemplo, Hardware Wallet ou um Wallet móvel de confiança). É a partir deste Wallet que enviará a garantia do Bitcoin para a Debifi e receberá os fundos.





- Moedas estáveis ou fiduciárias: A Debifi empresta em stablecoins e algumas moedas fiduciárias. As principais stablecoins utilizadas são USDT e USDC.



Pode utilizar o Aqua, um Bitcoin e um Liquid Wallet que também suporta a gestão de stablecoins USDT em várias redes. Ou COLDCARD (Mk4 ou Q), atualmente o único hardware suportado pela Debifi.



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3



- KYC (*Know Your Customer*): consoante a oferta de crédito escolhida, pode ser necessário um processo de verificação da identidade. No Debifi, cada oferta indica se o KYC é necessário ou não. Por isso, prepare-se em conformidade. O KYC é efectuado por prestadores de serviços terceiros fiáveis, como a Sumsub.



![image](assets/fr/03.webp)





- Aplicação de autenticação de dois factores: A Debifi requer um código de autenticação para cada ação importante. É um Layer extra de segurança. Neste tutorial, usaremos o Google Authenticator. Em alternativa, pode usar outros como achar melhor.



https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc



- Sítio Web e aplicação móvel Debifi: A Debifi é simultaneamente um sítio Web e uma aplicação móvel, e os dois funcionam em conjunto. A aplicação móvel torna-se um Wallet, que guarda a sua chave privada e gere a assinatura dos contratos. Além disso, é necessário utilizar o sítio Web para assinar os contratos (um grande Interface dá-lhe uma visão geral dos contratos de empréstimo e das suas especificidades).





- A aplicação móvel Debifi (iOS/Android) é necessária para contrair um empréstimo. É necessário descarregar a aplicação, criar uma conta e "associar" o seu dispositivo (registar o dispositivo na sua conta). A aplicação Debifi suporta a autenticação de dois factores (2FA) e, sem um smartphone, não é possível confirmar as transacções na Debifi.



### Criar uma conta



Visitar [o sítio Web oficial da Debifi] (https://debifi.com/app).



![image](assets/fr/04.webp)



Instale a sua aplicação de acordo com o tipo de smartphone que possui e, em seguida, abra-a.



![image](assets/fr/05.webp)



![image](assets/fr/06.webp)



Uma vez na aplicação, clique no menu **Configurações**.



![image](assets/fr/07.webp)



Em seguida, clique em **Login ou criar conta** para criar uma conta com o seu e-mail Address.



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





- Para maior segurança, pode até adicionar um passphrase.



![image](assets/fr/16.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Tenha em atenção que apenas o seu smartphone registado poderá abrir a sua conta (uma medida de segurança adicional).



Uma vez concluídas estas etapas, clique no menu **Ofertas** para ver as ofertas de crédito disponíveis. Ao clicar numa oferta, será redireccionado para o site da Debifi.



![image](assets/fr/17.webp)



### Aceder ao sítio Web e explorar as ofertas de empréstimos



Quando o seu dispositivo estiver ligado, aceda ao [sítio Web da Debifi] (https://debifi.com/). Inicie a sessão para estabelecer uma ligação segura entre a aplicação móvel Debifi e a plataforma web. Desta forma, é mais fácil interagir com as ofertas de crédito disponíveis (uma visão clara dos detalhes de cada oferta) e gerir a sua conta.



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





- Conservador (20% - 40% LTV), que corresponde a um empréstimo de baixo risco, é ideal para maximizar a segurança contra a volatilidade dos preços do Bitcoin;





- Equilibrado (50% LTV) ;





- Agressiva (70% - 85% LTV), que oferece uma maior liquidez, mas comporta um risco muito elevado de liquidação em caso de queda do mercado. O acompanhamento ativo das condições de mercado do Bitcoin é indispensável para a escolha desta fração.



#### Taxas de juro



A fixação das taxas depende geralmente do LTV escolhido, da duração do empréstimo, da volatilidade das garantias e das avaliações de risco específicas da plataforma. As taxas permanecem fixas durante o período do empréstimo.



#### Prazo do empréstimo e flexibilidade de reembolso



Os planos de reembolso dos empréstimos são frequentemente flexíveis e adaptados às necessidades do utilizador. Os pagamentos podem ser efectuados em qualquer altura, desde que sejam cumpridos os requisitos de garantia. Os pagamentos de empréstimos são geralmente juros durante o período do empréstimo, sendo o capital devido no vencimento.



#### Direitos de liquidação (valores de cobertura adicionais)



Como o preço do Bitcoin é volátil, um empréstimo responsável inclui políticas específicas de chamada de margem no acordo. Esta política permite que o mutuário seja notificado para fornecer garantias adicionais ou reembolsar uma parte do empréstimo.



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


7. O Ethereum USDC Address a ser utilizado para receber os fundos deve ser introduzido.



Quando estiver satisfeito com a oferta e tiver preenchido as informações necessárias, clique em "Pedido Contract".



![image](assets/fr/25.webp)



Regressar à aplicação móvel para ''**Fornecer chave pública**''.



![image](assets/fr/26.webp)



Prima '' **Fornecer chave pública** '' e, em seguida, escolha a fonte da chave pública. O mutuante também terá de fornecer uma chave pública Supply.



![image](assets/fr/27.webp)



![image](assets/fr/28.webp)



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



O próximo passo é assinar o Contract. Ainda na aplicação móvel, prima '' **Sign Contract** ''



![image](assets/fr/31.webp)



![image](assets/fr/32.webp)



Quando termina de assinar o Contract, a Debifi cria automaticamente um único Bitcoin Address (escrow 3-sur-4) para o seu Contract. Enquanto os seus bitcoins estiverem no escrow, não podem ser utilizados noutro local.



### Depósito da garantia e receção dos seus fundos



O passo final é depositar a sua garantia Bitcoin no sistema de caução multi-assinatura. A Debifi mostra-lhe então o Address de garantia (B) e a quantidade de BTC (A) a ser enviada como (garantia + comissão).



![image](assets/fr/33.webp)



Receberá também esta notificação na sua aplicação móvel.



![image](assets/fr/34.webp)



Assim que o seu depósito for confirmado, o mutuante pagará o montante do empréstimo ao Address que indicou, finalizando a transação e dando-lhe acesso aos fundos de que necessita.



Receberá então uma notificação da Debifi, pedindo-lhe que pague as taxas ou comissões do empréstimo para fazer avançar o estado do seu empréstimo.



Na realidade, uma vez criado o Contract, os encargos do empréstimo são automaticamente deduzidos da garantia depositada pelo mutuário no Address de garantia com várias assinaturas.



Basta assinar uma transação que permitirá à Debifi deduzir a sua comissão da garantia. Por seu lado, o seu mutuante também terá de assinar a transação de dedução da comissão, caso contrário a Debifi não poderá receber a sua comissão.



![image](assets/fr/35.webp)



As comissões de empréstimo aplicáveis são de 1,5-2%, consoante o prazo do Contract. A plataforma cobra comissões apenas no Bitcoin.



## Acompanhamento de empréstimos



Uma vez que o empréstimo está em curso, Debifi permite-lhe acompanhar o seu Contract em tempo real. No Interface, verá :





- O montante do empréstimo e o prazo restante.
- Rácio LTV (Loan-to-Value) atual: O LTV aumenta se o preço do BTC cair (uma vez que a sua garantia vale menos). É definido um limiar de alerta (geralmente 90%). Se o LTV exceder este limite, existe o risco de liquidação forçada. A Debifi dá-lhe então 24 horas para reagir.



Os mutuários serão informados da redução do preço. Esta informação estará igualmente disponível na página de resumo do Contract. Para restabelecer o rácio empréstimo/valor original de um empréstimo, o mutuário deve :





- ou depositar uma garantia adicional ;
- reembolsar a totalidade ou parte da dívida.



Em caso de aumento do preço da garantia, o mutuário conserva as mais-valias sobre a garantia. Deve apenas o montante do empréstimo, que é pré-determinado e independente do preço do Bitcoin.




## Reembolso e recuperação de garantias



No final do prazo acordado (ou antes, se o desejar), deve reembolsar o empréstimo.


Em Debifi :





- Aceda ao seu Contract e clique em **Fazer um reembolso**. Introduza o montante total devido (capital + juros).





- Envie os stablecoins do seu Wallet para o Address do credor indicado e volte para confirmar o reembolso na plataforma, copiando o **ID** da transação de reembolso para o separador dedicado. Desta forma, é mais fácil para a Debifi efetuar os seus controlos.



Depois de o pagamento ter sido confirmado pelo mutuante (e por si), a Debifi pedir-lhe-á então um **reembolso**. A sua garantia Bitcoin é libertada e pode devolvê-la do depósito de garantia para a sua própria carteira.  Não se esqueça de recolher todos os seus Bitcoins.



Assim que receberes os teus bitcoins, o empréstimo Contract muda para **Contract concluído**.



Parabéns! Finalizou o processo.




## Boas práticas e segurança



Quaisquer que sejam os seus objectivos ou motivações - financiar um projeto, adquirir um imóvel, comprar bitcoins, etc. - seja extremamente cauteloso antes de contrair um empréstimo garantido pelo Bitcoin. - seja extremamente cauteloso antes de contrair um empréstimo garantido pelo Bitcoin. Pense bem na sua decisão, pois o Bitcoin continua a ser um ativo volátil. **Uma queda acentuada no seu preço pode resultar na liquidação forçada dos seus bitcoins**.



Monitorizar o rácio empréstimo/garantia (LTV). Configure alertas (preço BTC, LTV), se possível. Não deixe que o seu rácio se aproxime dos 90%. Em caso de dúvida, aumente a garantia ou pague mais cedo.



Controle as suas chaves. Guarde as suas BTC num Wallet seguro (idealmente hardware ou um Wallet com boa reputação). Não defina um código PIN relacionado a uma data importante em sua vida e nunca compartilhe sua frase de recuperação. Na Debifi, você generate a sua chave privada na aplicação - a Debifi não a conhece.



Se possível, comece com pouco dinheiro. Para o seu primeiro empréstimo, teste um montante modesto para se familiarizar com o processo.



Utilize apenas o sítio Web oficial da Debifi para se manter a par das notícias da Debifi e evite ligações desconhecidas ou de phishing.  Actualize a aplicação, proteja o seu smartphone com um código PIN e escolha um Hardware Wallet compatível.



Alternativamente, se você é um credor, este vídeo tutorial irá guiá-lo através do uso da plataforma Debifi. Desde a seleção de mutuários interessados na sua oferta, ao fornecimento de chaves públicas, assinatura de acordos, transferência de stablecoins e muito mais.



![video](https://youtu.be/g8iLxwI4xT0)



Já sabe como utilizar a plataforma Debifi para obter um empréstimo.



Recomendo-lhe que faça este curso, que analisa em profundidade o Bitcoin, as Stablecoins e o seu contributo para a soberania.



https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46