---
name: Blockstream Green - Watch-Only
description: Configuração da carteira só de observação
---
![cover](assets/cover.webp)

Neste tutorial, descobrirá como configurar facilmente uma carteira "só de observação" no telemóvel utilizando a aplicação Blockstream Green.

## O que é uma carteira só para relógios?

Uma carteira só de leitura, ou "watch-only wallet", é um tipo de software concebido para permitir ao utilizador observar as transacções associadas a uma ou mais chaves públicas Bitcoin específicas, sem ter acesso às chaves privadas correspondentes.

Este tipo de aplicação armazena apenas os dados necessários para monitorizar uma carteira Bitcoin, nomeadamente para ver o seu saldo e histórico de transacções, mas não tem acesso às chaves privadas. Como resultado, é impossível gastar Bitcoins mantidos pela carteira na aplicação apenas de vigilância.

![GREEN-WATCH-ONLY](assets/fr/01.webp)

O Watch-only é geralmente utilizado em conjunto com uma carteira de hardware. Isso permite que as chaves privadas da carteira sejam armazenadas de forma segura, em hardware que não está conectado à Internet e tem uma superfície de ataque muito pequena, isolando assim as chaves privadas de ambientes potencialmente vulneráveis. A aplicação watch-only, por outro lado, armazena exclusivamente a chave pública estendida (`xpub`, `zpub`, etc.) da carteira Bitcoin. Essa chave pai não pode ser usada para encontrar as chaves privadas associadas e, portanto, não pode ser usada para gastar Bitcoins. No entanto, ela permite a derivação de chaves públicas filhas e endereços de recebimento. Graças ao conhecimento da carteira de hardware sobre os endereços seguros da carteira, a aplicação watch-only pode rastrear estas transacções na rede Bitcoin, permitindo ao utilizador monitorizar o seu saldo e gerar novos endereços de receção, sem ter de ligar a sua carteira de hardware de cada vez.

Neste tutorial, gostaria de vos apresentar uma das mais populares soluções de carteira móvel só para relógios: **Blockstream Green**.

![GREEN-WATCH-ONLY](assets/fr/02.webp)

## Apresentação da Blockstream Green

O Blockstream Green é uma aplicação de software disponível para telemóvel e computador. Anteriormente conhecida como Green Address, esta carteira tornou-se um projeto Blockstream após a sua aquisição em 2016.

A Green é uma aplicação muito fácil de utilizar, o que a torna particularmente adequada para principiantes. Oferece uma série de funções, como a gestão de hot wallets, hardware wallets e Liquid sidechain wallets.

Neste tutorial, vamos concentrar-nos apenas na criação de uma carteira só de relógios. Para explorar outras utilizações do Green, consulte os nossos outros tutoriais dedicados:

https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da
https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143
## Instalar e configurar a aplicação Blockstream Green

O primeiro passo é, obviamente, descarregar a aplicação Green. Aceda à sua loja de aplicações:

- [Para Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Para a Apple](https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590).
![GREEN-WATCH-ONLY](assets/fr/03.webp)

Para os utilizadores de Android, também é possível instalar a aplicação através do ficheiro `.apk` [disponível no GitHub da Blockstream] (https://github.com/Blockstream/green_android/releases).

![GREEN-WATCH-ONLY](assets/fr/04.webp)

Inicie a aplicação e selecione a caixa "Aceito as condições...*".

![GREEN-WATCH-ONLY](assets/fr/05.webp)

Quando abre o Green pela primeira vez, o ecrã inicial aparece sem um portefólio configurado. Mais tarde, se criar ou importar carteiras, estas aparecerão nesta interface. Antes de começar a criar uma carteira, aconselho-o a ajustar as definições da aplicação de acordo com as suas necessidades. Clique em "Definições da aplicação".

![GREEN-WATCH-ONLY](assets/fr/06.webp)

A opção "*Privacidade melhorada*", disponível apenas no Android, melhora a privacidade ao desativar as capturas de ecrã e ao ocultar as pré-visualizações de aplicações. Também bloqueia automaticamente o acesso a aplicações assim que o telefone é bloqueado, tornando os seus dados mais difíceis de expor.

![GREEN-WATCH-ONLY](assets/fr/07.webp)

Para aqueles que desejam melhorar a sua privacidade, a aplicação oferece a opção de enraizar o seu tráfego através do Tor, uma rede que encripta todas as suas ligações e torna as suas actividades difíceis de rastrear. Embora esta opção possa abrandar ligeiramente o funcionamento da aplicação, é altamente recomendada para proteger a sua privacidade, especialmente se não estiver a utilizar o seu próprio nó completo.

![GREEN-WATCH-ONLY](assets/fr/08.webp)

Para os utilizadores que possuem o seu próprio nó completo, a Green Wallet oferece a possibilidade de se ligarem a ele através de um servidor Electrum, garantindo um controlo total sobre as informações da rede Bitcoin e a distribuição das transacções.

![GREEN-WATCH-ONLY](assets/fr/09.webp)

Outra funcionalidade alternativa é a opção "*SPV Verification*", que permite verificar diretamente determinados dados da cadeia de blocos e, assim, reduzir a necessidade de confiar no nó predefinido da Blockstream, embora este método não ofereça todas as garantias de um nó completo.

![GREEN-WATCH-ONLY](assets/fr/10.webp)

Depois de ter ajustado estas definições às suas necessidades, clique no botão "*Guardar*" e reinicie a aplicação.

![GREEN-WATCH-ONLY](assets/fr/11.webp)

## Criar uma carteira só de observação na Blockstream Green

Está agora pronto para criar uma carteira só de relógios. Clique no botão "*Começar*".

![GREEN-WATCH-ONLY](assets/fr/12.webp)

Poderá escolher entre vários tipos de carteira. Para este tutorial, queremos criar uma carteira só de relógios, por isso clique no botão correspondente.

![GREEN-WATCH-ONLY](assets/fr/13.webp)

Selecionar a opção "Assinatura única".

![GREEN-WATCH-ONLY](assets/fr/14.webp)

Em seguida, seleciona "*Bitcoin*". Pela minha parte, estou a fazer este tutorial numa carteira testnet, mas o procedimento é idêntico na rede principal.

![GREEN-WATCH-ONLY](assets/fr/15.webp)

Ser-lhe-á pedido que forneça uma chave pública alargada (`xpub`, `zpub`, etc.) ou um descritor de script de saída.

![GREEN-WATCH-ONLY](assets/fr/16.webp)

Por conseguinte, terá de obter esta informação da carteira que pretende seguir através da sua carteira só de relógio. A chave pública estendida não é sensível em termos de segurança, pois não permite o acesso a chaves privadas, mas é sensível para a sua confidencialidade, pois revela todas as suas chaves públicas e, portanto, todas as suas transacções Bitcoin.

Digamos que está a utilizar a Sparrow Wallet para gerir a sua carteira numa carteira de hardware, encontrará esta informação na secção "*Configurações*". Encontrar esta informação dependerá do software de gestão de carteiras que utiliza, mas normalmente encontra-se nas definições.

![GREEN-WATCH-ONLY](assets/fr/17.webp)

Copie a sua chave pública alargada e introduza-a na aplicação Verde e, em seguida, clique em "Ligar".

![GREEN-WATCH-ONLY](assets/fr/18.webp)

Poderá então ver o saldo associado a esta chave, bem como o histórico de transacções.

![GREEN-WATCH-ONLY](assets/fr/19.webp)

Ao clicar em "*Receive*", pode gerar um endereço de receção para receber bitcoins na sua carteira de hardware. No entanto, aconselho a não utilizar esta opção sem primeiro verificar no ecrã da carteira de hardware se esta possui a chave privada associada ao endereço gerado, antes de a utilizar para bloquear bitcoins. Esta é uma boa prática a ser seguida.

![GREEN-WATCH-ONLY](assets/fr/20.webp)

A opção "*Balayer*" permite-lhe introduzir manualmente uma chave privada para gastar fundos diretamente a partir da sua aplicação Green. Exceto em casos muito específicos, não recomendo a utilização desta função, uma vez que exige que revele a sua chave privada num telefone, que é muito mais vulnerável a ataques informáticos do que a sua carteira de hardware.

![GREEN-WATCH-ONLY](assets/fr/21.webp)

Agora já sabe como configurar facilmente uma carteira só de relógio no seu smartphone! É uma ferramenta útil para monitorizar uma carteira numa carteira de hardware sem ter de a ligar e desbloquear sempre.

Se achou este tutorial útil, agradecia que deixasse um polegar verde abaixo. Sinta-se à vontade para partilhar este artigo nas suas redes sociais. Muito obrigado!

Recomendo também que consulte este outro tutorial completo sobre a aplicação Blockstream Green para configurar uma hot wallet:

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143