---
name: Robosats

description: Como usar Robosats
---

![cover](assets/cover.jpeg)

RoboSats (https://learn.robosats.com/) é uma maneira fácil de trocar Bitcoin por moedas nacionais de forma privada. Ele simplifica a experiência peer-to-peer e utiliza faturas de pagamento relâmpago para minimizar a custódia e os requisitos de confiança.

![video](https://youtu.be/XW_wzRz_BDI)

## Guia

> Este guia é do Bitocin Q&A (https://bitcoiner.guide/robosats/). Todo o crédito a ele, apoie-o lá (https://bitcoiner.guide/contribute); BitcoinQ&A também é um mentor de Bitcoin. Entre em contato com ele para orientação!

![image](assets/0.jpeg)

RoboSats - Uma troca P2P simples e privada baseada em Lightning

## Antes de começar

### Coisas que você precisa saber

| Jargão    | Definição                                                                                                                                                                                                              |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robô      | Sua identidade de negociação privada gerada automaticamente. Não reutilize o mesmo robô mais de uma vez, pois isso pode comprometer sua privacidade.                                                                   |
| Token     | Uma sequência de caracteres aleatórios usada para gerar seu robô exclusivo.                                                                                                                                            |
| Criador   | Um usuário que cria uma oferta para comprar ou vender Bitcoin.                                                                                                                                                         |
| Comprador | Um usuário que aceita a oferta de outro usuário para comprar ou vender Bitcoin.                                                                                                                                        |
| Garantia  | Uma quantidade de Bitcoin bloqueada por ambas as partes como garantia de que cumprirão sua parte na negociação. As garantias geralmente correspondem a 3% do valor total da negociação e são baseadas em faturas Hodl. |
| Custódia  | Usada pelo vendedor como método de retenção da quantidade de Bitcoin da negociação, também usando faturas Hodl.                                                                                                        |
| Taxas     | RoboSats cobra 0,2% do valor da negociação, que é dividido entre o criador e o comprador. O comprador paga 0,175% e o criador paga 0,025%.                                                                             |

## Coisas que você precisa ter

### Uma carteira Lightning

RoboSats é nativo do Lightning, então você vai precisar de uma carteira Lightning para financiar a garantia e receber os sats comprados como comprador. Você deve ter cuidado ao escolher sua carteira, devido à tecnologia usada para fazer o RoboSats funcionar, nem todas são compatíveis.

Se você é um operador de nó, o Zeus é de longe a melhor opção. Se você não tem seu próprio nó, eu recomendaria o Phoenix, uma carteira móvel multiplataforma com configuração simples e acesso ao Lightning. O Phoenix foi usado na produção deste guia.

### Algum Bitcoin

Compradores e vendedores precisam financiar uma garantia antes que qualquer negociação possa ocorrer. Geralmente, esse é um valor muito pequeno (~3% do valor da negociação), mas é um pré-requisito mesmo assim.

Usando o RoboSats para comprar seus primeiros sats? Que tal pedir a um amigo para emprestar a pequena quantia necessária para começar!? Se você estiver sozinho, aqui estão algumas outras ótimas opções para obter alguns sats sem KYC para começar.

### Acesso ao RoboSats

Obviamente, você vai precisar acessar o RoboSats! Existem quatro maneiras principais de fazer isso:

1. Através do navegador Tor (Recomendado!)
2. Através de um navegador web regular (Não recomendado!)
3. Através do APK para Android
4. Seu próprio cliente

Se você é novo no navegador Tor, saiba mais e faça o download [aqui](https://www.torproject.org/download/).
Uma breve nota para usuários de iOS que desejam acessar RoboSats via Tor em seus telefones. 'Onion Browser' não é o Tor Browser. Em vez disso, use Orbot + Safari e Orbot + DuckDuckGo.

## Comprando Bitcoin

Os seguintes passos foram realizados em maio de 2023 usando a versão 0.5.0, acessada através do navegador Tor. Os passos devem ser idênticos para usuários que acessam RoboSats através do APK Android.

No momento da escrita, RoboSats ainda está passando por desenvolvimento ativo, então a interface pode mudar um pouco no futuro, mas os passos básicos necessários para concluir a negociação devem permanecer em grande parte inalterados.

> Quando você carregar RoboSats pela primeira vez, você será recebido com esta página inicial. Clique em Iniciar.

![image](assets/2.jpeg)

Gere seu token e guarde-o em algum lugar seguro, como um aplicativo de notas criptografadas ou gerenciador de senhas. Este token pode ser usado para recuperar seu ID temporário de robô no caso de seu navegador ou aplicativo fechar durante uma negociação.

![image](assets/3.jpeg)

Conheça sua nova identidade de robô e clique em Continuar.

![image](assets/4.jpeg)

Clique em Ofertas para navegar pelo livro de pedidos. No topo da página, você pode filtrar suas preferências. Certifique-se de observar as porcentagens de garantia e o prêmio sobre a taxa média de câmbio.

- Escolha Comprar
- Escolha sua moeda
- Escolha seu(s) método(s) de pagamento

![image](assets/5.jpeg)

> Clique na oferta que você deseja aceitar. Insira a quantidade (em sua moeda fiduciária escolhida) que você deseja comprar do vendedor, então verifique os detalhes pela última vez e clique em Aceitar Pedido.

Se o vendedor não estiver online (indicado por um ponto vermelho em sua imagem de perfil), você verá um aviso de que a negociação pode levar mais tempo do que o normal. Se você continuar e o vendedor não prosseguir a tempo, você será compensado com 50% do valor da garantia por seu tempo perdido.

![image](assets/6.jpeg)

Em seguida, você precisa bloquear sua garantia de negociação pagando a fatura na tela. Esta é uma fatura de retenção que congela em sua carteira. Ela só será cobrada se você não cumprir sua parte na negociação.

![image](assets/7.jpeg)

Em sua carteira Lightning, escaneie o código QR e pague a fatura.

![image](assets/8.jpeg)

Em seguida, em sua carteira Lightning, gere uma fatura para o valor mostrado e cole no espaço fornecido.

![image](assets/9.jpeg)

Aguarde o vendedor bloquear o valor da negociação. Quando isso acontecer, RoboSats passará automaticamente para a próxima etapa, onde a janela de chat será aberta. Diga oi e peça ao vendedor suas informações de pagamento em moeda fiduciária. Uma vez fornecidas, envie o pagamento através do método escolhido e confirme isso em RoboSats. Todo o chat em RoboSats é criptografado com PGP, o que significa que apenas você e seu parceiro de negociação podem ler as mensagens.

![image](assets/10.jpeg)

Assim que o vendedor confirmar o recebimento do pagamento, RoboSats libera automaticamente o pagamento usando a fatura fornecida anteriormente.

![image](assets/11.jpeg)

Quando a fatura for paga, a negociação estará concluída e sua garantia será desbloqueada. Você verá um resumo da negociação.

![image](assets/12.jpeg)

Verifique sua carteira Lightning para confirmar que os sats chegaram.

![image](assets/13.jpeg)

## Recursos adicionais

Além da óbvia compra e venda de Bitcoin, RoboSats possui algumas outras características que você deve conhecer.
Garagem de Robôs
Quer ter várias negociações acontecendo ao mesmo tempo, mas não quer compartilhar a mesma identidade em todas elas? Sem problemas! Clique na aba Robô, gere um Robô adicional e crie ou aceite seu próximo pedido.
![image](assets/14.jpeg)

### Criando Pedidos

Além de aceitar a oferta de outra pessoa, você pode criar a sua própria e esperar que outro Robô venha até você.

- Abra a página de Criação.
- Defina se o seu pedido é para comprar ou vender Bitcoin.
- Insira a quantidade e a moeda que você deseja comprar/vender.
- Insira o(s) método(s) de pagamento que você está disposto a usar.
- Insira o percentual de 'Prêmio sobre o Mercado' que você está disposto a aceitar. Observe que esse valor pode ser negativo para fazer uma oferta com desconto em relação ao preço de mercado atual.
- Clique em Criar Pedido.
- Pague a fatura do Lightning para bloquear sua Garantia de Fabricante.
- Seu pedido está agora ativo. Relaxe e espere alguém aceitá-lo.

![image](assets/15.jpeg)

### Pagamentos On-chain

RoboSats é focado no Lightning, mas os compradores têm a opção de receber seus sats em um endereço de Bitcoin on-chain. Os compradores podem selecionar essa opção após bloquear sua garantia. Após selecionar on-chain, o comprador verá uma visão geral das taxas. As taxas adicionais para esse serviço incluem:

- Uma taxa de troca coletada pela RoboSats - Essa taxa é dinâmica e varia dependendo de como a rede Bitcoin está ocupada.
- Uma taxa de mineração para a transação de pagamento - Isso pode ser configurado pelo comprador.

![image](assets/16.jpeg)

### Trocas P2P

RoboSats permite que os usuários troquem sats para dentro ou para fora de sua carteira Lightning. Basta clicar no botão de troca no topo da página de ofertas para ver as ofertas de troca atuais.

Como comprador de uma oferta de 'Troca para Dentro', você envia Bitcoin on-chain para o peer e recebe sats de volta, menos as taxas e/ou prêmios anunciados, para sua carteira Lightning. Como comprador de uma oferta de 'Troca para Fora', você envia sats via Lightning e recebe Bitcoin, menos quaisquer taxas e/ou prêmios, para seu endereço on-chain. Os usuários das carteiras Samourai ou Sparrow Wallet também podem aproveitar o recurso Stowaway para concluir uma troca.

As ofertas de troca da RoboSats também podem incorporar alternativas vinculadas ao Bitcoin, como RBTC, LBTC e WBTC. Você deve ter muito cuidado ao interagir com esses tokens, pois todos eles têm várias compensações. Bitcoin vinculado não é Bitcoin!

![image](assets/17.jpeg)

### Execute seu próprio Cliente RoboSats

Os usuários dos nós Umbrel, Citadel e Start9 podem instalar seu próprio cliente RoboSats diretamente em seu nó. Os benefícios de fazer isso são listados como:

- Tempos de carregamento dramaticamente mais rápidos.
- Mais seguro: você controla qual aplicativo de cliente RoboSats você executa.
- Acesse o RoboSats com segurança de qualquer navegador/dispositivo. Não é necessário usar o TOR se você estiver em sua rede local ou usando VPN: o backend do seu nó lida com a torificação necessária para anonimização.
- Permite controlar a qual coordenador de mercado P2P você se conecta (padrão é robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)

![image](assets/18.jpeg)

## FAQ

### Posso ser enganado?

Como comprador, se você enviou o dinheiro fiduciário necessário para o seu lado da negociação, mas o vendedor não liberou os sats para você, então você pode abrir uma disputa. Se durante esse processo de disputa você conseguir provar aos árbitros do RoboSats que você enviou o dinheiro fiduciário, os fundos em garantia do vendedor e sua garantia de negociação serão liberados para você. Como faço para cancelar uma negociação?

Você pode cancelar uma negociação depois de postar sua garantia clicando no botão Cancelar Colaborativo no menu de negociação. Se o seu parceiro de negociação concordar em cancelar, você não terá nenhuma taxa. Mas se o seu parceiro de negociação quiser concluir a negociação e você cancelar mesmo assim, você perderá sua garantia de negociação.

### O RoboSats funciona com o método de pagamento 'X'?

Não há restrições quanto aos métodos de pagamento no RoboSats. Se você não encontrar nenhuma oferta no método desejado, crie sua própria oferta usando-o!

![imagem](assets/19.jpeg)

### O que o RoboSats aprende sobre mim quando eu o uso?

Desde que você use o RoboSats via Tor ou o aplicativo Android, absolutamente nada! Saiba mais aqui.

- O Tor protege sua privacidade de rede.
- A criptografia PGP mantém sua conversa de negociação privada.
- Sem contas significa um Robô por negociação. Isso significa que o RoboSats não pode correlacionar várias negociações a uma única entidade.

No entanto, existem algumas ressalvas! O Lightning é bastante privado como remetente, mas não como receptor. Se você receber em seu próprio nó Lightning, seu ID de nó é compartilhado em suas faturas. Esse ID de nó dá a qualquer pessoa com conhecimento dele um ponto de partida para tentar vincular sua atividade na cadeia. Isso também é verdade se um usuário optar por receber sua negociação por meio de um pagamento na cadeia.

Para mitigar isso, os usuários podem optar por usar uma solução como uma Carteira Proxy para Lightning ou Coinjoin para pagamentos na cadeia.

### Federação

Atualmente, existe um único coordenador do RoboSats operado pela equipe de desenvolvedores do RoboSats. No Bitcoin, qualquer forma de centralização torna um alvo mais fácil para governos ou reguladores que podem não olhar com bons olhos para um serviço específico.

Com o RoboSats sendo um projeto de código aberto, qualquer pessoa pode pegar o código e começar a executar seu próprio coordenador. Embora isso descentralize um pouco o risco de um único alvo, também fragmenta um mercado de liquidez já escasso.

A equipe do RoboSats reconhece isso e começou a trabalhar em um modelo federado. Como usuário final, isso não deve mudar muito o fluxo de negociação demonstrado acima, mas haverá visualizações ou telas extras para adicionar ou remover diferentes coordenadores que surgirem.

FIM do guia
https://bitcoiner.guide/robosats/
