---
name: Amboss
description: Explorar e analisar o Lightning Network
---

![cover](assets/cover.webp)



O Lightning Network é um Layer do protocolo Bitcoin, que foi desenvolvido principalmente para promover a adoção de pagamentos Bitcoin numa base diária, aumentando a velocidade de processamento de cada transação. Baseado no princípio da descentralização, o Lightning Network consiste em nós (computadores que executam uma implementação Lightning) que comunicam entre si, retransmitindo dados (pagamentos e verificação de pagamentos).



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Tal como na cadeia principal, tornou-se essencial permitir que os utilizadores conheçam as informações e o estado da rede, a fim de facilitar as ligações entre os nós e minimizar o problema de liquidez que geralmente surge na rede. Com efeito, no Lightning Network, recomendamos micropagamentos de montantes relativamente mais reduzidos do que os das transacções na cadeia principal do Bitcoin.



É importante notar que nem todos os nós do Lightning estão disponíveis na plataforma Amboss.



Tal como [Mempool Space] (https://Mempool.space), que fornece informações úteis sobre a cadeia principal do protocolo Bitcoin, desde 2022 [Amboss] (https://amboss.space) fornece informações sobre :





- Nós no Lightning Network
- Canais de pagamento e respectiva capacidade de pagamento
- Evolução do Lightning Network ao longo do tempo
- Estatísticas sobre os encargos cobrados aos nós de retransmissão pelos seus pagamentos.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Neste tutorial, vamos fazer uma visita guiada a esta plataforma, que é um recurso essencial para os utilizadores do Lightning Network, para aqueles que querem ligar o seu nó para expandir a rede, etc.




## Encontrar pares



Um dos objectivos da plataforma Amboss é permitir que os vários nós da rede se liguem e comuniquem informações entre si. Na página inicial da plataforma, pode procurar diretamente o nome de um nó que já conhece ou encontrar nós das carteiras Lightning mais populares que utiliza.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Na página inicial, encontrará também nós classificados de acordo com :




- Evolução da capacidade: a quantidade de Bitcoin associada à chave pública do nó e o total disponível em todos os seus canais.
- Evolução do canal: o número de novas ligações a outros nós da rede.
- Popularidade do nó: a frequência com que o nó é utilizado.



![nodes](assets/fr/03.webp)



A escolha do nó correto para ligação resume-se, portanto, à verificação dos seguintes critérios:





- Certifique-se de que o nó tem uma quantidade suficiente de bitcoins; quanto maior for a capacidade do nó, maior será a quantidade de bitcoins que pode pagar.





- Certifique-se de que o nó tem um grande número de ligações e canais abertos com outros nós da rede.





- Certifique-se de que o nó está ativo e continua a ser apreciado pelos seus pares, verificando o número de novos canais; quanto mais novos canais este nó tiver abertos, mais apreciado é pelos outros nós da rede.



Depois de encontrar o nó certo, clique no seu nome para ser redireccionado para a página de informações do nó.



Neste Interface, ao verificar o Timestamp do canal recém-criado, obterá uma pista sobre a atividade deste nó. Encontrará também informação sobre a capacidade dos canais deste nó: esta informação é vital se quiser usar ativamente este nó para fazer os seus pagamentos.




![node_info](assets/fr/04.webp)



Na secção da esquerda, encontrará mais detalhes sobre a localização deste nó. Por exemplo, pode ver :




- A chave pública: o identificador logo abaixo do nome do nó.
- A posição geográfica deste nó.




![channels](assets/fr/05.webp)



Este Interface indica-lhe o Address de ligação para este nó: tem a forma `pubkey@ip:port`. No nosso exemplo, queremos ligar-nos ao nó cujo :




- a chave pública `pubkey` é: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- A porta: `9735`



![geoinfo](assets/fr/06.webp)



Na secção **Channels**, verá a lista de canais abertos e as ligações do nó a outros nós da rede. Neste Interface, várias informações são vitais para confirmar que este nó corresponde às nossas necessidades ou é fiável:





- Rácio de entrada**: O montante que o nó cobrará por cada milhão de Satoshi que receber, dependendo do canal escolhido.
- O rácio (partes por milhão)** : que representa o número de Satoshi por milhão de unidades que o nó lhe cobrará quando decidir efetuar um pagamento através de um dos seus canais. Digamos que decide fazer um pagamento de `10_000 Sats` através de um canal cujo rácio de ppm é de `500 Sats`, terá de pagar ao nó `10_000 * 500 / 1_000_000` satoshis, equivalente a `5 Sats`.
- O [HTLC](https://planb.academy/resources/glossary/htlc) máximo** : O montante máximo que este nó lhe permite transitar através de um destes canais.



Consultando a tabela deste Interface, também é possível encontrar todas estas informações no nó a que corresponde.



![channels_info](assets/fr/07.webp)



Na secção **Mapas de canais**, é possível ver a distribuição e a capacidade dos vários canais neste nó. É possível alterar os critérios de distribuição apresentados selecionando uma das opções na lista pendente à direita.



![cha_maps](assets/fr/08.webp)



A secção **Canais encerrados** agrupa todos os antigos canais do nó de acordo com o tipo de encerramento:




- Encerramento mútuo**: representa o acordo de ambas as partes, que utilizam a sua chave privada para assinar a transação que marca o encerramento do canal e a distribuição dos saldos no seu interior
- Um **encerramento forçado**: representa o encerramento abrupto e unilateral de uma parte do canal. Este tipo de encerramento não é recomendado, uma vez que o Lightning Network é um protocolo baseado em punições: quando se tenta defraudar o saldo de um canal, corre-se o risco de perder todo o saldo disponível nesse canal.



![closed](assets/fr/09.webp)



Obter informações sobre as taxas de trânsito para encaminhar os seus pagamentos através de um canal no nó que utiliza



![fees](assets/fr/10.webp)



## Informações sobre a rede



O Amboss não se concentra apenas nas informações dos membros da rede, mas também no estado da própria rede.



Na secção **Estatísticas**, no menu do lado esquerdo "Simulações", encontrará um gráfico que mostra a probabilidade de um pagamento bem sucedido em função do montante do pagamento.



De facto, notará que a curva está a diminuir porque, à medida que o montante do seu pagamento aumenta, tem menos hipóteses de ver esse pagamento ser efectuado. Isto reflecte o verdadeiro problema de liquidez do Lightning Network. Por exemplo, o seu pagamento de `10_000` satoshis tem `79%` de hipóteses de ser efectuado. Por outro lado, para um pagamento de `3_000_000` satoshis tem menos de `13%` de hipóteses de sucesso.



![network](assets/fr/11.webp)



O menu **Estatísticas de rede** permite-lhe apresentar graficamente estatísticas para :




- Canais de pagamento
- Nós
- Capacidade
- Taxas
- Evolução do canal.



![network_stat](assets/fr/12.webp)



No menu **Estatísticas do mercado**, a opção **Detalhes das ordens** permite-lhe visualizar a procura de liquidez no Lightning Network. Este gráfico pode também mostrar quais os canais com maior procura e/ou com capacidade considerável.



![markets](assets/fr/13.webp)




## Ferramentas



A Amboss oferece uma série de ferramentas para o ajudar a otimizar as suas pesquisas e acções.



### Descodificador Lightning Network



Esta ferramenta é principalmente responsável por fornecer detalhes sobre a estrutura de um Lightning Invoice, Lightning Address ou Lightning URL.



Na página inicial, na secção **Ferramentas**, apresente o seu Lightning Address, por exemplo.



![decoder](assets/fr/14.webp)



A partir deste descodificador, é possível obter informações como :




- a chave pública do nó associada ao seu Lightning Address;
- O tempo de expiração de um Invoice do seu Address;
- O mínimo e o máximo que pode enviar;
- O nó Nostr associado ao seu Address, se o Nostr estiver ativado neste nó.



![decode](assets/fr/15.webp)



### Magma IA



Descubra a mais recente ferramenta revelada pela Amboss para gerir eficazmente as suas ligações aos nós Lightning Network. A Magma AI utiliza inteligência artificial dedicada para se concentrar num problema importante: fazer uma boa seleção dos nós a ligar.



![magma](assets/fr/16.webp)



### Calculadora Satoshi



Descubra o preço atual do Bitcoin na sua moeda local (EUR / USD). Na página inicial, utilize a calculadora de satoshis para descobrir o preço de mercado atual.



![calculator](assets/fr/17.webp)




Já fez uma visita completa às funcionalidades e ferramentas de análise da plataforma. Abaixo encontra-se o nosso artigo sobre o explorador Bitcoin **Mempool.space**.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f