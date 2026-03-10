---
name: Bisq Easy Mobile
description: Um protocolo de negociação peer-to-peer para novos utilizadores de bitcoin - sem intermediários, sem KYC.
---
![cover](assets/cover.webp)


## Introdução


O protocolo de transacções [Bisq Easy](https://bisq.network/bisq-easy/) foi concebido para o [Bisq 2](https://github.com/bisq-network/bisq2), o sucessor do [Bisq v1](https://github.com/bisq-network/bisq). O Bisq 2 suportará vários protocolos comerciais, redes de privacidade e identidades. Facilita a compra de Bitcoin com zero taxas de comércio e sem exigência de depósito de segurança. Destina-se a novos compradores de Bitcoin que procuram uma opção sem KYC e que pretendem ser eficientemente integrados por vendedores experientes e conhecedores da plataforma Bisq.


Atualmente, o Bisq Easy é o único protocolo comercial para o Bisq 2. Estão planeados mais protocolos comerciais para o futuro. Saiba mais sobre o Bisq 2 neste tutorial:


https://planb.academy/tutorials/exchange/peer-to-peer/bisq-v2-c1c6a702-6c16-4101-8b90-62c424017b80

Este pequeno guia é um complemento ao tutorial acima sobre a compra do Bitcoin utilizando a aplicação [Bisq Easy Mobile] (https://github.com/bisq-network/bisq-mobile) e o Lightning.


## 1️⃣ Introdução


Para começar, descarregue o Bisq Easy Mobile a partir da [página de descarregamento] (https://bisq.network/downloads/). Recomenda-se que verifique a transferência. As instruções de verificação também estão disponíveis na [página de download] (https://bisq.network/downloads/). Após a instalação, é necessário aceitar o "Acordo de Utilizador". Em seguida, crie um perfil público composto por um `nickname` e um avatar (representado por um `ícone de robô`). Com o Bisq Easy, também é possível criar vários perfis de utilizador dentro de um cliente. Depois de uma breve inicialização, o utilizador irá parar ao `Home Screen`. A aplicação destaca material educacional diretamente na página principal. Toque em `Abrir Guia Comercial` para se familiarizar com as informações mais recentes.


![image](assets/en/01.webp)


O guia comercial explica tudo o que é relevante em passos simples:



- Como negociar no Bisq Easy
- Como funciona o processo de negociação
- O que preciso de saber sobre as regras comerciais.


Outra secção importante é **"Quão seguro é negociar no Bisq Easy? "**


![image](assets/en/08.webp)


Marque a caixa "Li e compreendi" e toque em "Concluir".


![image](assets/en/02.webp)


## 2️⃣ Faça uma cópia de segurança dos seus dados


Antes de começarmos, vamos tratar de algumas tarefas domésticas e criar uma `backup` do seu ficheiro de armazenamento de dados. Vá a `Mais` > `Cópia de segurança e restauro` para guardar o seu perfil e histórico de transacções. Se perder o seu dispositivo sem uma cópia de segurança, a sua reputação e as transacções em curso são irrecuperáveis. Forneça uma `Senha` para encriptar a sua cópia de segurança.


![image](assets/en/11.webp)


## 3️⃣ Ofertas


A partir do "Ecrã inicial", existem duas formas de navegar para as ofertas. Toque em `Explorar ofertas` no meio do ecrã ou toque em `Ofertas` no menu inferior. A partir daí, selecione a "moeda" que pretende negociar.


![image](assets/en/03.webp)


Ao contrário do [Bisq 1](https://planb.academy/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04), que requer garantias, o Bisq Easy depende apenas da reputação do vendedor como segurança. Embora esta abordagem permita que os compradores comprem Bitcoin pela primeira vez sem propriedade prévia, ela coloca um alto grau de confiança na capacidade do vendedor de entregar Bitcoin após receber pagamentos fiduciários. Portanto, o modelo de segurança Bisq Easy é otimizado apenas para pequenas quantidades de comércio e as negociações são limitadas a $600 USD equivalente por transação para minimizar o risco. Na secção `Offerbook`, selecione filtros para métodos de pagamento e liquidação em Lightning ou Bitcoin (on-chain).


![image](assets/en/04.webp)


Depois de aplicar os `filtros`, selecionar uma oferta adequada de um parceiro comercial de renome. O método de pagamento pré-selecionado pelo vendedor e o tipo de liquidação (`Lightning` ou `on-chain`) serão apresentados. Certifique-se de que estes correspondem às suas preferências antes de prosseguir. Seleccionamos aqui a opção Lightning ⚡.


![image](assets/en/05.webp)


Reveja e confirme os detalhes da transação tocando em "Confirmar aceitação da oferta". Em seguida, um ecrã pop-up confirma que aceitou a oferta com êxito. Toque em "Mostrar transação" em "Transacções em aberto". Na secção "Abrir negociações", cole a sua "Fatura relâmpago" e toque em "Enviar ao vendedor" para a partilhar. Agora aguarde os dados da conta de pagamento do vendedor. Os vendedores podem levar algum tempo para responder. Verifique periodicamente se há atualizações na janela de bate-papo.


![image](assets/en/06.webp)


Envie uma breve saudação no chat. O vendedor partilhará os detalhes de pagamento quando estiver online


![image](assets/en/09.webp)


Depois de receber os dados de pagamento necessários do vendedor, continue a concluir o pagamento. Em seguida, toque no botão `Confirmar que efectuou o pagamento` e aguarde pacientemente a confirmação da receção. ️ ⌛️


Por último, quando o vendedor confirmar a receção do pagamento, deve também confirmar a receção do Bitcoin. Isto completa a compra utilizando o Bisq no Modo Fácil. Parabéns! Pode agora tocar no botão `fechar a transação`.


![image](assets/en/10.webp)


## 4️⃣ Resolução de litígios no Bisq Easy


Se algo correr mal na sua transação, tanto os compradores como os vendedores podem solicitar apoio de mediação.


**O que os mediadores podem fazer

- Ajudar a facilitar a conclusão bem sucedida do comércio

- Verificar pagamentos em moeda fiduciária, altcoin e Bitcoin

- Cancelar transacções quando necessário

- Comunicar violações graves das regras aos moderadores para eventual proibição de utilização


**Consequências para os vendedores fraudulentos

Dependendo do seu tipo de reputação:



- Reputação da Obrigação BSQ**: O DAO pode confiscar o seu BSQ vinculado
- Reputação da cebola Address**: O seu endereço Bisq 1 onion pode ser banido


**Nota importante:** Uma vez que toda a reputação está ligada ao teu perfil de utilizador, um banimento desactiva a tua reputação completamente.


## 5️⃣ Criar a sua própria oferta


Em vez de aceitar ofertas existentes, pode criar a sua própria oferta de compra e deixar que os vendedores venham ter consigo. Esta é a opção correta se não encontrar ofertas com o prémio ou os métodos de pagamento adequados no mercado em que pretende negociar, embora tenha de esperar que um vendedor aceite.


No ecrã `Ofertas`, toque no ícone verde `+` no canto inferior direito. Depois selecione `Comprar Bitcoin` e escolha a sua moeda fiduciária.


Defina os seus parâmetros de negociação:



- Montante fixo ou montante variável**: Escolha o montante que pretende gastar.
- Forma de pagamento**: Selecionar entre as opções disponíveis
- Liquidação**: Escolha Relâmpago ⚡ ou ₿ on-chain


Reveja os seus dados e toque em `Criar oferta`. A sua oferta aparece agora no `Livro de ofertas`.


![image](assets/en/07.webp)


*Nota: Como comprador no Bisq Easy, não precisa de reputação - esta é a principal vantagem. Os vendedores suportam o requisito e o risco da reputação, e é por isso que cobram prémios. A sua oferta só precisa de ter um preço suficientemente atrativo para que os vendedores com reputação a considerem.*


Uma vez publicada, aguarde na secção "Livro de ofertas". Quando um vendedor aceitar a sua oferta, receberá uma notificação. Abra a negociação em `Open Trades`, onde o vendedor e você podem trocar seus detalhes de pagamento. Envie o seu endereço Bitcoin ou a fatura Lightning ao vendedor. Depois de enviar a moeda fiduciária, confirme o pagamento. Assim que o vendedor confirmar o recebimento, ele liberará os Bitcoins para concluir a troca.


## 🎯 Conclusão


O Bisq Easy permite a compra de Bitcoin sem garantias, resolvendo o clássico problema do ovo e da galinha para os novos compradores. A contrapartida é clara: a segurança depende da reputação do vendedor e não de fundos bloqueados. Esta abordagem baseada na confiança explica o prémio típico de 5-15%, que compensa os vendedores respeitáveis pelo seu investimento na construção da confiança e na prestação de apoio. Embora o sistema limite as transacções a pequenas quantias para conter potenciais perdas, mantenha-se sempre fiel aos vendedores com pontuações de reputação sólidas. Para os recém-chegados dispostos a aceitar estas condições, o Bisq Easy oferece um ponto de entrada fácil para o Bitcoin.


## 📚 Bisq Recursos móveis fáceis


[Github](https://github.com/bisq-network/bisq-mobile) | [Website ](https://bisq.network/bisq-easy/)| [Wiki](https://bisq.wiki/Bisq_Easy)