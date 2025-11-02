---
name: BTCPAY SERVER - Guarda-chuva
description: Instalação e utilização do BTCPAY SERVER no Umbrel para aceitar o Bitcoin e o Lightning
---

![cover](assets/cover.webp)



No ecossistema Bitcoin, a aceitação de pagamentos representa um grande desafio para comerciantes e empresas. As soluções tradicionais, sejam bancárias (cartões de crédito, Stripe, PayPal) ou mesmo Bitcoin (BitPay, Coinbase Commerce), impõem intermediários que cobram taxas substanciais, coletam seus dados comerciais confidenciais e podem BLOCK ou censurar suas transações por capricho. Esta dependência vai contra os princípios fundamentais do Bitcoin de descentralização, confidencialidade e soberania financeira.



O BTCPAY SERVER está a emergir como a resposta de código aberto a este problema. Este processador de pagamentos auto-hospedado transforma o seu próprio nó Bitcoin numa infraestrutura profissional, sem intermediários, sem taxas de processamento adicionais e sem comprometer a privacidade. Desenvolvido por uma comunidade global de colaboradores desde 2017, o BTCPAY SERVER permite que você receba pagamentos Bitcoin e Lightning diretamente em suas carteiras, mantendo o controle total de seus fundos em todos os momentos.



Tradicionalmente, a instalação do BTCPAY SERVER requer competências técnicas avançadas: Configuração do servidor Linux, domínio do Docker, gerenciamento de certificados SSL e segurança de rede. A Umbrel revoluciona esta abordagem com uma instalação de um clique diretamente integrada no seu Bitcoin e LIGHTNING NODE. Esta simplificação torna acessível a todos o que anteriormente estava reservado a técnicos experientes.



**Importante entender**: O BTCPAY SERVER na Umbrel funciona por defeito apenas na sua rede local. Pode criar facturas, aceitar pagamentos Lightning e Bitcoin e gerir a sua contabilidade a partir de qualquer dispositivo ligado à sua rede doméstica (computador, smartphone, tablet). Esta configuração é ideal para faturar serviços presenciais, gerir pagamentos presenciais ou utilizar o BTCPAY SERVER a partir da sua rede local. Por outro lado, para integrar o BTCPAY SERVER numa loja online acessível publicamente na Internet, será necessária uma configuração adicional com exposição pública (abordaremos esta questão no final do tutorial).



Este tutorial leva-o através da instalação completa do BTCPAY SERVER na Umbrel, configurando o seu Bitcoin, Wallet e LIGHTNING NODE, criando e pagando facturas e gerindo relatórios de contabilidade. Descobrirá como utilizar eficazmente o BTCPAY SERVER na sua rede local e, em seguida, falaremos de soluções para exibição pública, caso pretenda integrá-lo num sítio de comércio eletrónico.



## Pré-requisitos



Para seguir este tutorial, é necessário ter o Umbrel corretamente instalado e configurado. Se ainda não o tiver feito, consulte o nosso tutorial sobre a instalação do Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

O seu nó Bitcoin core deve estar totalmente sincronizado com o Blockchain (100% na aplicação Bitcoin da Umbrel). Esta sincronização inicial demora normalmente entre 3 dias e 2 semanas, dependendo do seu hardware e da ligação à Internet.



Para aceitar pagamentos Lightning instantâneos, também é necessário instalar o LND (Lightning Network Daemon) na Umbrel. Consulte nosso tutorial sobre como instalar e configurar o LND na Umbrel se quiser ativar esse recurso.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Permitir pelo menos 50 GB de espaço livre em disco para o BTCPAY SERVER, as suas bases de dados e os dados do Lightning. Recomenda-se vivamente uma ligação estável à Internet através de um cabo Ethernet para evitar falhas de ligação.



## Instalação do BTCPAY SERVER no guarda-chuva



A partir do Umbrel Interface (`umbrel.local`), vá para a App Store e procure por "BTCPAY SERVER" na categoria Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Clique em Instalar. O Umbrel verifica automaticamente se o Bitcoin core e o LND estão instalados e, em seguida, inicia a implementação (2-5 minutos).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Depois de instalada, abra a aplicação. Terá de criar uma conta de administrador com credenciais fortes.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Assim que a sua conta for criada, o BTCPAY SERVER solicitará imediatamente a criação da sua primeira loja. Escolha um nome profissional e selecione uma moeda de referência (EUR, USD ou BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Aceder ao BTCPAY SERVER na sua rede local



O BTCPAY SERVER é acessível a partir de qualquer dispositivo da sua rede local (WiFi ou Ethernet). Acesso a partir do seu navegador para :



```url
http://umbrel.local
```



Ou diretamente para :



```url
http://umbrel.local:3003
```



**Acesso remoto com Tailscale**: Para aceder ao BTCPAY SERVER a partir de qualquer parte do mundo, utilize o Tailscale. Esta VPN segura permite-lhe ligar-se ao seu Umbrel como se estivesse na sua rede local. Veja o nosso tutorial dedicado ao Tailscale na Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Configurar a sua carteira Bitcoin



Para aceitar pagamentos, é necessário configurar um Bitcoin Wallet. O BTCPAY SERVER apresenta as opções de configuração no painel de controlo.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Para configurar o Wallet Bitcoin, aceda a "Carteiras" > "Bitcoin".



Tem duas opções: criar uma nova carteira diretamente no BTCPay ou importar uma carteira existente. Para a importação, estão disponíveis vários métodos:




- Ligar o Hardware Wallet** (recomendado): Importar as suas chaves públicas através da aplicação Vault
- Importar ficheiro Wallet** (recomendado): Carregar um ficheiro exportado do seu portefólio
- Introduzir a chave pública alargada**: Introduza o seu XPub/YPub/ZPub manualmente
- Digitalizar o código QR do Wallet** : Digitalizar um código QR da BlueWallet, Cobo Vault, Passport ou Specter DIY
- Introduzir Wallet seed** (não recomendado) : Introduza a sua frase de recuperação de 12 ou 24 palavras



![Options de création de portefeuille](assets/fr/06.webp)



Para este tutorial, vamos criar um novo Hot Wallet: a chave privada será, portanto, armazenada no nosso servidor Umbrel. Neste caso, aconselhamo-lo vivamente a transferir regularmente os fundos para um Cold Wallet para evitar armazenar grandes quantidades no servidor.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Uma vez configurado, o BTCPAY SERVER confirma que o seu Wallet está pronto para aceitar pagamentos On-Chain.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Ativar o Lightning Network



Para aceitar pagamentos instantâneos Lightning, vá a Wallets > Lightning. Depois, como o seu nó LND já está instalado na Umbrel, basta clicar no botão "Guardar" para validar a ligação entre o seu BTCPAY SERVER e o seu LIGHTNING NODE.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Criar e pagar facturas



Em Interface BTCPAY SERVER, navegue para Facturas > Criar Invoice. Introduza o montante, adicione uma descrição opcional e clique em Criar.



![Création d'une nouvelle facture](assets/fr/10.webp)



Pode então clicar no botão "Checkout" para exibir o Invoice. A BTCPay gera então um Invoice com um código QR unificado (BIP21) que contém o Bitcoin Address e o Lightning Invoice.



![Détails de la facture générée](assets/fr/11.webp)



O seu cliente pode ler o código QR com qualquer Wallet compatível.



![Page de paiement avec QR code](assets/fr/12.webp)



Uma vez pago, o Invoice fica "liquidado" numa questão de segundos para o Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Gestão e acompanhamento de pagamentos



Na secção "Relatórios", separador "Facturas", encontrará um histórico completo das suas facturas, com data, montante, estado e método de pagamento. Pode exportá-lo, se necessário.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Configuração da loja



O BTCPAY SERVER permite-lhe gerir várias lojas com parâmetros distintos. Cada loja representa uma entidade comercial distinta: loja de comércio eletrónico, ponto de venda físico ou faturação de serviços.



Nas definições da loja, encontrará várias secções importantes:



![Paramètres du magasin](assets/fr/15.webp)





- Definições gerais**: Nome da loja, moeda de referência (BTC, EUR, USD), tempo de expiração do Invoice (predefinição de 15 minutos), número de confirmações Blockchain necessárias
- Taxas**: Configuração de fontes de taxas Exchange e conversões fiat/Bitcoin
- Aspeto do checkout**: Personalize a aparência das suas páginas de checkout (logótipo, cores, mensagens personalizadas)
- Definições de correio eletrónico**: Configuração das notificações por correio eletrónico dos pagamentos recebidos
- Tokens de acesso**: Gestão API token para integrações de comércio eletrónico (WooCommerce, Shopify, etc.)
- Utilizadores**: Gerir o acesso dos utilizadores à loja com diferentes níveis de permissões (Proprietário, Convidado)
- Webhooks**: Configuração de Webhook para sincronização em tempo real com o seu sistema de contabilidade ou ERP



O BTCPAY SERVER também oferece uma secção de Plugins para ampliar a funcionalidade com integrações de comércio eletrónico, sistemas de ponto de venda e ferramentas adicionais.



![Gestion des plugins](assets/fr/16.webp)



## Vantagens e limitações da utilização local



**Benefícios do BTCPAY SERVER no Umbrel** :




- Soberania total: controlo exclusivo das chaves privadas e dos fundos, nenhum terceiro pode congelar ou censurar os seus pagamentos
- Poupanças substanciais: apenas custos de rede Bitcoin (alguns cêntimos no Lightning) vs. 2-3% nos processadores tradicionais
- Máxima confidencialidade: sem registo, verificação de identidade ou partilha de dados com empresas terceiras
- A arquitetura de fonte aberta garante transparência, auditabilidade e sustentabilidade através de uma grande comunidade de programadores
- Instalação fácil através da Umbrel, sem necessidade de conhecimentos técnicos avançados



**Limitações importantes** :




- Apenas rede local**: O BTCPAY SERVER na Umbrel só é acessível a partir da sua rede doméstica. Perfeito para faturação presencial, serviços freelance ou pequenas empresas físicas, mas inadequado para lojas online acessíveis ao público na Internet.
- Responsabilidade técnica total: manutenção dos nós, cópias de segurança regulares, monitorização da conetividade
- Gestão da liquidez dos relâmpagos: abertura e gestão de canais com capacidade de entrada suficiente
- Suporte limitado à documentação e fóruns da comunidade, exigindo mais autonomia do que um departamento comercial de atendimento ao cliente



Esta limitação da LAN é o principal obstáculo à integração do BTCPAY SERVER numa loja de comércio eletrónico, em que os clientes precisam de poder aceder às páginas de pagamento a partir de qualquer ponto da Internet.



## Boas práticas e segurança



Active as cópias de segurança automáticas da Umbrel e guarde uma cópia num suporte externo (pen USB, disco Hard, nuvem encriptada). Mantenha as suas sementes Bitcoin (frases de recuperação) num local seguro e fisicamente separado. Guarde o ficheiro LND channel.backup para a recuperação do Lightning.



Monitorizar regularmente a sincronização do Bitcoin core, os canais Lightning e a resposta do BTCPAY SERVER. Um simples teste semanal: generate e pagar uma fatura de alguns satoshis. Manter a Umbrel actualizada (patches de segurança, melhorias). Fazer uma cópia de segurança antes das grandes actualizações. Para utilização profissional, considere a monitorização externa (UptimeRobot) com alertas por correio eletrónico/SMS.



## Mostrar publicamente o BTCPAY SERVER para uma loja online



Para integrar o BTCPAY SERVER numa loja de comércio eletrónico baseada na Web (WooCommerce, Shopify, etc.), os seus clientes têm de poder aceder às páginas de pagamento a partir de qualquer lugar, e não apenas da sua rede local.



**Solução: Gerenciador de proxy Nginx**



Pode expor o BTCPAY SERVER publicamente utilizando o Nginx Proxy Manager (disponível na Umbrel App Store). Esta solução requer :




- Um nome de domínio (clássico ou gratuito através de DuckDNS, No-IP, Afraid.org)
- Configurar o reencaminhamento de portas (portas 80 e 443) no seu router
- Instalação do Nginx Proxy Manager, que gere automaticamente os certificados SSL



Esta configuração expõe o seu servidor à Internet e requer uma vigilância adicional (palavras-passe fortes, 2FA, actualizações regulares). Iremos preparar um tutorial dedicado que detalha este procedimento completo.



## Conclusão



O BTCPAY SERVER on Umbrel combina o poder do nó Bitcoin com a simplicidade da Umbrel para criar uma infraestrutura de pagamento profissional auto-hospedada acessível a todos. Esta soberania financeira acarreta uma responsabilidade de manutenção, mas a Umbrel simplifica muito a carga operacional em comparação com as vantagens: eliminação das taxas de processamento, proteção da sua privacidade, resistência à censura e controlo total dos seus fundos.



A utilização da rede local já abrange uma vasta gama de aplicações: faturação de serviços freelance, pagamentos presenciais, pequenas lojas físicas ou simplesmente aprender e experimentar o Bitcoin e o Lightning num ambiente controlado. Para necessidades de comércio eletrónico que requerem exposição pública, existe a solução Nginx Proxy Manager, mas requer configuração técnica adicional, que detalharemos num tutorial dedicado.



Quer esteja a gerir um negócio, um projeto incipiente ou simplesmente a experimentar, o BTCPAY SERVER na Umbrel oferece total autonomia financeira. O caminho começa com uma primeira loja, um primeiro Invoice, um primeiro pagamento recebido diretamente na sua infraestrutura soberana.



## Recursos



### Documentação oficial




- [Sítio Web oficial do BTCPAY SERVER](https://btcpayserver.org)
- [Documentação completa do BTCPAY SERVER](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Documentação Tailscale](https://tailscale.com/kb)


### Comunidade e apoio




- [Fórum BTCPAY SERVER](https://chat.btcpayserver.org)
- [Guarda-chuva do Fórum](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)