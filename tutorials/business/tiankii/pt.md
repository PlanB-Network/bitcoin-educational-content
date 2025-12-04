---
name: Tiankii
description: Conjunto relâmpago de ferramentas para retalhistas e consumidores
---

![cover](assets/cover.webp)



No ecossistema Bitcoin, a aceitação de pagamentos em tempo real continua a ser um grande desafio para as empresas e os particulares. As soluções tradicionais requerem frequentemente conhecimentos técnicos avançados, uma infraestrutura complexa para manter, ou exigem que os fundos sejam detidos por intermediários. Esta situação está a atrasar a adoção em massa do Bitcoin como moeda corrente, apesar da promessa dos avanços tecnológicos do Lightning Network.



A Tiankii, uma empresa salvadorenha nascida em 2021, responde a esse problema oferecendo uma infraestrutura Bitcoin acessível e modular. Em vez de forçar a adoção de um ecossistema fechado, a Tiankii oferece um conjunto de ferramentas interconectadas que permitem a qualquer pessoa integrar o Bitcoin Lightning em seus negócios sem sacrificar o controle de seus fundos.



## O que é o Tiankii?



### Origem e filosofia



Tiankii - um termo Nahuatl que significa "mercado ao ar livre acessível a todos" - é a primeira start-up 100% Bitcoin de El Salvador. Fundada por Darvin Otero após a adoção do Bitcoin como moeda legal do país, a empresa pretende transformar o Bitcoin de uma reserva de valor numa moeda transacionável para compras diárias. Ao contrário das plataformas de custódia, a Tiankii adopta uma abordagem não-custodial em que os utilizadores mantêm o controlo dos seus fundos, servindo a infraestrutura apenas como intermediário técnico.



### Arquitetura técnica



A Tiankii posiciona-se como um fornecedor de infra-estruturas Bitcoin-as-a-Service baseadas em Lightning Network. Esta tecnologia de segunda camada permite transacções quase instantâneas com custos negligenciáveis, tornando possíveis os micropagamentos e as compras diárias.



A arquitetura baseia-se em três pilares:



**Lightning-first**: Favorecer sistematicamente a rede Lightning pela sua velocidade e custos mais baixos, mantendo o suporte de transacções on-chain para grandes quantias.



**Normas abertas**: Utilização de LNURL para automatizar os pedidos de pagamento, Lightning Address para IDs de correio eletrónico legíveis e cartão Bolt para pagamentos NFC interoperáveis.



**Modularidade agnóstica em relação ao wallet**: Possibilidade de ligar diferentes carteiras Lightning (LNbits, Blink, BlueWallet) ou o seu próprio nó, oferecendo a máxima flexibilidade em função do nível de especialização e de autonomia exigido.



## Ferramentas do ecossistema Tiankii



### Bitcoin POS - Terminal de pagamento em loja



A aplicação transforma o smartphone ou tablet num terminal Lightning. O comerciante introduz o montante na moeda local e a aplicação gera um código QR Lightning ou aceita um cartão Bolt. As transacções são creditadas instantaneamente sem comissões, com conversões automáticas em mais de 150 moedas, gestão de gorjetas e histórico de vendas.



### Painel de controlo do comerciante - Gestão de vendas unificada



A Interface web centralizada para ligar os seus wallet Lightning, acompanhar as transacções em tempo real, emitir facturas e relatórios contabilísticos generate. A plataforma agrega todos os canais: pagamentos na loja (POS), vendas online (plug-ins de comércio eletrónico) ou integrações API. Os pagamentos convergem para o wallet escolhido.



### Cartão sem contacto Bitcoin (cartão Bolt)



O cartão NFC Bolt representa a maior inovação da Tiankii na democratização do Bitcoin para o público em geral. Funcionando como um cartão bancário sem contacto, permite-lhe pagar as compras do Bitcoin Lightning com um simples toque num terminal compatível.



Ao contrário das soluções de custódia tradicionais, este cartão segue uma norma aberta que garante a interoperabilidade. O utilizador pode associá-lo ao seu próprio wallet através da aplicação IBI, conservando assim as suas chaves privadas e o controlo total dos fundos associados. O pagamento é efectuado em apenas um segundo, sem que seja necessário sacar do smartphone ou ter uma ligação à Internet ativa no momento do pagamento.



Esta solução é particularmente inclusiva para pessoas não familiarizadas com smartphones, oferecendo uma porta de entrada acessível para a economia Bitcoin.



### Aplicação IBI - Interface individual Bitcoin



A aplicação IBI (Individual Bitcoin Interface) foi concebida para as pessoas que pretendem utilizar diariamente o Bitcoin Lightning. A sua principal vantagem reside na geração de um Address Lightning personalizado, um identificador de pagamento legível em formato de correio eletrónico (exemplo: alice@ibi.me).



Este identificador simplifica drasticamente a receção dos pagamentos: não é necessário generate emitir uma nova fatura para cada transação, o remetente pode simplesmente introduzir o endereço Lightning. A interface também permite gerir o cartão Bolt (ativação, desativação, limites de despesas), ligar várias carteiras Lightning e efetuar pagamentos através da leitura de códigos QR.



### Plugins de comércio eletrónico



Integrações prontas a usar para WooCommerce, Shopify e Cloudbeds. Instala-se em minutos para adicionar o Bitcoin Lightning ao checkout. Vantagens: comissão zero (vs. 2-3% para cartões de crédito), liquidação instantânea, acesso mundial, eliminação de estornos. Os pagamentos chegam diretamente ao wallet ligado ao comerciante.



### Bitcoin API e ferramentas de desenvolvimento



O Tiankii SDK permite integrar o Bitcoin Lightning em aplicações existentes sem manter o seu próprio nó. O API trata da criação de facturas, verificação de pagamentos e envios em massa através de uma infraestrutura robusta alojada no Google Cloud. O Command Center completa a oferta para organizações com o Address Lightning em domínios personalizados, pagamentos em massa e gestão centralizada de terminais e cartões NFC.



## Instalação e primeiros passos



### Pré-requisitos essenciais



A utilização do Tiankii não requer pré-requisitos técnicos complexos. As aplicações funcionam através de um navegador web num smartphone, tablet ou computador. Não é necessário instalar nenhuma aplicação nativa: basta ter acesso à Internet e um navegador recente para aceder ao IBI ou ao painel de controlo do comerciante.



**Para utilizadores privados (IBI App)**: Não é necessário um wallet Lightning anterior. Quando cria a sua conta, o Tiankii configura automaticamente um Address Lightning funcional através do [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html), uma implementação sem nó que utiliza a rede Liquid em segundo plano. Pode imediatamente receber e enviar pagamentos sem qualquer configuração técnica. Esta solução simplifica drasticamente o acesso para os principiantes, mantendo-se auto-custodial.



**Para os comerciantes (Painel de controlo do comerciante)** : A ligação de um wallet Lightning existente é obrigatória para utilizar terminais de ponto de venda e receber pagamentos. A Tiankii suporta várias soluções: carteiras móveis (Blink, Strike), soluções auto-hospedadas (LNbits, LND/CLN node) ou carteiras web (Alby). Os guias de ligação detalhados estão disponíveis na secção Recursos deste tutorial.



### Para clientes particulares: Aplicação IBI



**Criação de conta



Vá a accounts.ibi.me para criar a sua conta. Nesta página, pode escolher entre dois tipos de conta: "Personal Use" para uso individual, ou "Business Use" para uso comercial. Selecione "Personal Use" para aceder às ferramentas de receção e envio de pagamentos no Bitcoin.



![Choix du type de compte](assets/fr/01.webp)



Depois de selecionar "Uso pessoal", será automaticamente redireccionado para go.ibi.me para completar o seu registo. Este registo pode ser efectuado por e-mail, número de telefone ou através da sua conta Google, Microsoft ou Twitter. Uma vez criado, pode aceder imediatamente à sua interface IBI, com o seu Lightning Address já operacional.



![Création du compte](assets/fr/02.webp)



**Interface principal



A interface IBI apresenta o seu saldo em satoshis e na moeda local (USD). Três botões permitem-lhe interagir: "Receber" para receber pagamentos, "Digitalizar" para digitalizar um código QR e "Enviar" para enviar satoshis.



![Interface IBI](assets/fr/03.webp)



**Receber o pagamento



Para receber satoshis, prima "Receber". A aplicação gera automaticamente um código QR e apresenta o seu Address Lightning personalizado (formato nom@ibi.me). Partilhe este endereço ou o código QR com o remetente: os fundos chegam instantaneamente à sua conta IBI.



![Réception avec Lightning Address](assets/fr/04.webp)



Uma vez creditado o seu saldo, pode utilizar estes satoshis para efetuar pagamentos.



**Enviar um pagamento



Para enviar satoshis, prima "Enviar". Pode digitalizar um código QR do Lightning ou introduzir diretamente um destino Address do Lightning.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



Introduzir o montante pretendido em satoshis, verificar o montante equivalente na moeda local e confirmar o pagamento.



![Confirmation du montant](assets/fr/07.webp)



Uma notificação de sucesso confirma o envio com detalhes: montante enviado, taxa de transação e destinatário.



![Paiement réussi](assets/fr/08.webp)



**Gestão de contas



Em Definições, pode gerir os seus cartões Bitcoin NFC (Cartões Bolt). A interface permite-lhe ativar, desativar ou definir limites de despesas para os seus cartões.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### Para comerciantes: Painel de controlo do comerciante e POS



**Criação de uma conta comercial



Aceda a accounts.ibi.me para criar a sua conta. Selecione "Business Use" para aceder às ferramentas de comerciante. Este tipo de conta desbloqueia o acesso ao Painel de controlo do comerciante e aos terminais de ponto de venda.



Depois de selecionar "Utilização comercial", será automaticamente redireccionado para o Painel de controlo do comerciante (pay.tiankii.com). Isto leva-o para a interface de gestão de negócios com acompanhamento de receitas, transacções e ferramentas de pagamento. Para começar a aceitar pagamentos, deve primeiro ligar o seu wallet Lightning, clicando na ligação na parte superior da página (ver seta na imagem).



![Dashboard marchand](assets/fr/11.webp)



*ligação *wallet Lightning**



Etapa crucial para ativar o seu ponto de venda: ligar o seu wallet Lightning para receber pagamentos. A interface oferece várias opções de ligação. Tenha em atenção que algumas opções (Bitcoin Onchain e Lightning Network) ainda estão em desenvolvimento e aparecem a cinzento na interface.



![Options de connexion wallet](assets/fr/12.webp)



Para este tutorial, estamos a utilizar a ligação Lightning Address, compatível com Chivo, Blink Wallet e Strike. Introduza o seu Lightning Address (formato nom@domaine.com), por exemplo, da LN Markets, da Alby ou de qualquer outro fornecedor compatível.



![Saisie de la Lightning Address](assets/fr/13.webp)



Depois de iniciar sessão, a sua conta está operacional. Pode agora aceder ao POS ou voltar ao painel de controlo para configurar outras definições.



![Connexion réussie](assets/fr/14.webp)



*ligações de pagamento** *Ligações de pagamento



O menu "Ferramentas de pagamento" dá acesso a "Pedido de pagamento", que lhe permite criar e gerir ligações de pagamento. Esta funcionalidade é útil para gerar ligações de pagamento personalizadas a enviar por correio eletrónico ou mensagem: donativos, pagamentos únicos, pagamentos múltiplos ou mesmo paywalls para proteger conteúdos. Pode criar diferentes tipos de ligações para se adaptar às suas necessidades comerciais.



![Liens de paiement](assets/fr/15.webp)



**Configuração do terminal de vendas



Para aceitar pagamentos na loja, aceda ao menu "Terminal de vendas" a partir de "Ferramentas de pagamento". Esta secção permite-lhe criar e gerir os seus terminais POS (o número de terminais depende do seu plano, ver planos Freemium vs. Business abaixo). Clique em "Abrir" para abrir a interface POS no seu browser.



![Gestion des terminaux](assets/fr/16.webp)




**Gerar uma venda



O terminal POS apresenta um teclado numérico para introduzir o montante da venda. Introduzir o montante na sua moeda local (por exemplo, 500 sats corresponde a 630,74 ARS) e depois premir "OK" para confirmar.



![Saisie du montant](assets/fr/17.webp)



A aplicação gera instantaneamente um código QR Lightning e um Address Lightning para pagamento. Os clientes podem digitalizar o código QR com o seu wallet ou utilizar o seu cartão Bolt num terminal NFC.



![QR code de paiement](assets/fr/18.webp)



Assim que o pagamento é recebido, aparece um ecrã de confirmação, mostrando o montante recebido em moeda local e em satoshis. Pode enviar um recibo por correio eletrónico, imprimir o talão ou iniciar imediatamente uma nova venda.



![Paiement encaissé](assets/fr/19.webp)



**Controlo e gestão



Todas as transacções são registadas no seu painel de controlo do comerciante. Dispõe de um acompanhamento completo das receitas por período, do número total de vendas e de um historial detalhado para a sua contabilidade.



A interface Definições oferece vários separadores de configuração. O separador "Configurações gerais" permite-lhe gerir o seu perfil de comerciante e as notificações. O separador "Utilizadores" permite-lhe adicionar e gerir o acesso ao Painel de Controlo do Comerciante para a sua equipa (gestão multiutilizadores em função do seu plano). O separador "Espaço de trabalho de desenvolvimento" dá acesso às chaves API para integrações avançadas, enquanto "Assinatura" permite gerir a sua assinatura.



![Paramètres du compte marchand](assets/fr/20.webp)



**Planos Freeemium vs. Planos empresariais



A Tiankii oferece dois pacotes para o Dashboard do comerciante. O plano **Freemium** (gratuito) é adequado para empresas em fase de arranque com limitações: um único ponto de venda, um único utilizador, um volume mensal limitado a 1000 USD e sem acesso a conectores de comércio eletrónico. O plano **Business** (taxa de 0,5% por transação) oferece terminais ilimitados, utilizadores ilimitados, volume ilimitado, acesso aos plug-ins WooCommerce/Shopify/Cloudbeds e notificações exclusivas do WhatsApp.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Vantagens e limitações



### Destaques



**Autocustódia**: Mantém as suas chaves privadas e o controlo total dos seus fundos. Não há risco de congelamento de conta ou falência de plataforma de terceiros.



**Simplicidade**: Lightning Address como um endereço de correio eletrónico, pagamentos NFC com um simples toque, interface intuitiva sem necessidade de conhecimentos técnicos.



**Ecossistema completo**: Ferramentas para todos os perfis (particulares, retalhistas, programadores) com integrações modulares para responder às suas necessidades.



**Conformidade profissional**: Alojamento seguro na nuvem, conformidade com PCI-DSS, conformidade regulamentar salvadorenha.



### Limitações



**Restrições de iluminação**: Requer uma ligação wallet permanente, gestão de liquidez para grandes volumes, risco de falha se o destinatário estiver offline. A Tiankii atenua estes aspectos com LSPs integrados.



**Dependência de SaaS**: Se o Tiankii não estiver disponível, a geração de facturas é temporariamente impossível (os seus fundos permanecem seguros).



**Privacidade**: A Tiankii pode observar os metadados da transação (montantes, datas). Menos privado do que uma solução auto-hospedada como o BTCPay Server.



## Conclusão



A Tiankii ilustra como uma infraestrutura bem concebida pode eliminar as barreiras técnicas que impedem a adoção em massa da Bitcoin como moeda corrente. Ao combinar o poder do Lightning Network com uma abordagem sem custódia e ferramentas acessíveis, o ecossistema oferece um caminho equilibrado entre a soberania financeira e a facilidade de utilização.



Para os comerciantes, a Tiankii representa uma oportunidade para reduzir drasticamente os custos de transação e aceder a uma nova base de clientes. Para os consumidores, os cartões Lightning Address e NFC transformam o Bitcoin numa moeda prática, sem complexidade técnica.



Embora a adoção generalizada do Bitcoin continue a ser um desafio que exige formação e tempo, infra-estruturas como a Tiankii demonstram que as ferramentas técnicas já existem. A missão de simplificar os pagamentos em Bitcoin já não é uma visão distante, mas uma realidade acessível a qualquer pessoa disposta a dar o salto.



## Recursos



### Documentação oficial




- [Sítio Web oficial da Tiankii](https://tiankii.com)
- [Centro de Ajuda Tiankii] (https://help.tiankii.com)
- [Aplicação IBI] (https://go.ibi.me)
- [Painel de controlo do comerciante](https://pay.tiankii.com)
- [Centro de Comando](https://cc.ibi.me)



### Guias de ligação Wallet




- [Ligar LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Connect BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Ligar Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Comunidade




- [Lightning Network Plus](https://lightningnetwork.plus) - Recurso educativo relâmpago
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Iniciativa salvadorenha de economia circular Bitcoin



### Ferramentas relacionadas




- [Blink Wallet](https://blink.sv) - Wallet compatível com Lightning recomendado
- [LNbits](https://lnbits.com) - Solução wallet auto-hospedada
- [Cartão Bolt normalizado](https://github.com/boltcard) - Especificações técnicas dos cartões NFC