---
name: Voltz
description: O Lightning wallet tudo-em-um para a sua empresa.
---

![cover](assets/cover.webp)



A ideia da plataforma Voltz surgiu de um grupo de bitcoiners que pretendia fornecer o seu próprio serviço wallet de bitcoin. O resultado foi uma infraestrutura completa para aceitar bitcoin no retalho. Neste tutorial, levamo-lo numa visita guiada à Voltz e às possibilidades de integração de bitcoin que a plataforma tem para oferecer.



## Começar a utilizar o Voltz



Para além de ser um Lightning wallet de custódia que permite enviar, receber e pagar diariamente, o Voltz é uma plataforma completa que fornece inúmeras extensões para integrar a bitcoin como ponto de venda ou mercado no seu negócio.



Aceda à plataforma [Voltz](https://www.lnvoltz.xyz/en) e crie uma conta clicando no botão "Try now".



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ É importante definir uma palavra-passe alfanumérica forte para aumentar as suas hipóteses contra ataques de força bruta e verificar se está realmente no sítio Web oficial da Voltz para preencher os seus dados de início de sessão para se proteger contra phishing.



A interface do Voltz é muito semelhante à da plataforma LnBits.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

O Voltz é de facto construído num servidor LnBits; veja o nosso tutorial para aprender como montar os seus próprios servidores LnBits e construir as suas soluções neles.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

A plataforma permite-lhe gerir eficazmente várias carteiras. Por defeito, quando se regista, tem automaticamente uma carteira Lightning. No entanto, pode adicionar outras carteiras.



![wallets](assets/fr/03.webp)



### Portabilidade



O Voltz não se limita a uma interface web: na secção **Mobile Access**, pode ligar o seu Voltz wallet ativo a aplicações como o Zeus ou o Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

Para tal, é necessário instalar e ativar a extensão **LndHub** na plataforma.



![lndhub](assets/fr/04.webp)



Selecione a sua carteira Voltz ativa e, dependendo dos direitos que pretende conceder, digitalize o código QR apropriado.




- O código QR da fatura permite-lhe apenas ler o histórico da sua carteira e as novas facturas generate.
- O código QR do administrador permite-lhe ver o histórico, as facturas generate e também pagar as facturas Lightning.



![qrs](assets/fr/05.webp)



Neste tutorial, ligamos o nosso Voltz wallet à aplicação Blue Wallet.



![connect](assets/fr/06.webp)



Uma vez que a nossa carteira esteja ligada, todas as acções realizadas serão sincronizadas entre o Blue Wallet e o Voltz. Por exemplo, quando uma fatura é emitida pelo generate no Blue Wallet, também tem um histórico no Voltz.



![sync](assets/fr/07.webp)



Na secção **Configuração da carteira**, encontrará parâmetros mínimos, como a personalização do nome da carteira e a moeda em que pretende receber os seus pagamentos.



![config](assets/fr/08.webp)



### Extensões



Uma das caraterísticas especiais da plataforma Voltz é a sua modularidade, que lhe permite ativar as extensões de que necessita. A lista de extensões pode ser consultada no menu **Extensões**.



![extensions](assets/fr/09.webp)



Entre estas extensões encontra-se o TPoS, um terminal de ponto de venda que pode utilizar para manter um inventário e cobrar os pagamentos dos seus clientes.



![tpos](assets/fr/10.webp)



A partir do terminal do ponto de venda, pode :




- Obtenha uma página Web que pode partilhar com os seus clientes e parceiros;
- Gerir o inventário de produtos;
- Gerar facturas Lightning;
- Pagamentos em numerário através de cartões Bolt.



A extensão está disponível numa versão gratuita e numa versão paga para funcionalidades mais avançadas. Para criar um terminal POS, clique no botão **Abrir** abaixo do logótipo da extensão e, em seguida, clique em **Novo POS**.



![new_tpos](assets/fr/11.webp)



Defina o nome do seu ponto de venda, depois ligue o seu Voltz wallet ao seu terminal para receber os pagamentos. Pode ativar as gratificações marcando a caixa **Ativar gratificações**. Active também a opção de impressão de facturas se desejar emitir recibos aos seus clientes (esta funcionalidade ainda está em desenvolvimento, pelo que poderá haver problemas de funcionamento).



O terminal de ponto de venda também inclui a configuração de impostos quando pretende aplicar o imposto do seu país diretamente aos seus produtos.



![tpos](assets/fr/12.webp)



Uma vez criado o seu terminal POS, pode adicionar produtos e serviços pré-configurados para garantir uma experiência de pagamento e contabilidade sem problemas para si e para os seus clientes.



![product](assets/fr/13.webp)



Crie os seus produtos definindo o seu nome, adicionando uma imagem e definindo um preço de venda.  Pode categorizar os seus produtos para facilitar o acompanhamento. Pode aplicar impostos diretamente a um produto específico. Se o produto não tiver imposto aplicado, o imposto configurado na fase de criação do terminal de ponto de venda será aplicado automaticamente.



![products](assets/fr/14.webp)



Pode importar automaticamente a sua lista de produtos a partir de um formato JSON, clicando no botão **Importar/Exportar**.



![exports](assets/fr/15.webp)



Aceda à área de checkout através da ligação, clicando no ícone **Novo separador**, ou partilhe a sua plataforma POS através de um código QR com os seus clientes, clicando no ícone **Código QR**.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



Os seus clientes podem consultar o seu catálogo e efetuar o pagamento a partir desta interface.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



No grupo de extensões disponíveis, encontrará também ferramentas como as extensões **Invoice** e **Payment Link**, que lhe permitem criar facturas generate com produtos específicos para cobrar pagamentos isolados sem passar pelo terminal POS.



## Acompanhe os seus pagamentos



No menu **Pagamentos**, o Voltz dá-lhe uma visão geral dos pagamentos às suas várias carteiras.


Pode acompanhar os seus pagamentos por :




- Estado.
- A etiqueta: por exemplo, **TPOS** para pagamentos no ponto de venda e **lnhub** através da ligação móvel nas carteiras Zeus e Blue Wallet.
- A carteira de colecções.
- Total das entradas e saídas de pagamentos.
- Um período bem definido.



![payments](assets/fr/22.webp)



## Mais opções



O Voltz é também uma infraestrutura sobre a qual pode construir as suas próprias soluções. Na secção **Extensões**, encontrará um guia para desenvolver as suas próprias extensões dentro do ecossistema Voltz e LnBits.



![build](assets/fr/23.webp)



No caso de pretender desenvolver soluções fora do ecossistema, mas ainda assim utilizar a sua infraestrutura, na secção **URL do nó**, encontrará chaves API e informações de documentação com um exemplo do que pode fazer com estes dados.



Pode criar facturas Lightning a partir das suas aplicações utilizando o seu Voltz wallet, pagar facturas Lightning, descodificar e verificar facturas.



![keys](assets/fr/24.webp)



Agora já tem uma boa noção de Voltz. Se gostou deste tutorial, temos a certeza que vai aprender mais sobre os melhores métodos e ferramentas para integrar o bitcoin no seu negócio com o nosso curso: Bitcoin para empresas.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a