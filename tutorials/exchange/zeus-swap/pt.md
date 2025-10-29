---
name: Troca de Zeus
description: Serviço Exchange sem custódia entre bitcoins On-Chain e Lightning Network
---

![cover](assets/cover.webp)



O ecossistema Bitcoin apresenta uma dualidade: a rede principal (On-Chain) oferece a máxima segurança, enquanto a Lightning Network permite transacções instantâneas. Esta arquitetura de duas Layer cria um desafio prático: como podem os fundos ser transferidos eficientemente entre estas duas camadas sem intermediários centralizados?



O problema é concreto: recebe um pagamento Lightning mas quer mantê-lo armazenado em Cold ou, pelo contrário, tem bitcoins On-Chain mas precisa de liquidez Lightning. As soluções tradicionais envolvem a abertura/fecho manual de canais Lightning (dispendiosos e técnicos) ou plataformas centralizadas que exigem KYC.



O Zeus Swap resolve este problema com um serviço Exchange automatizado e sem custódia. Desenvolvido pela Zeus LSP, permite-lhe converter bitcoins On-Chain em satoshis Lightning de forma bidirecional, sem confiar os seus fundos a um intermediário. O processo utiliza contratos atómicos (HTLC) que garantem que o Exchange será concluído ou cancelado.



A inovação reside na sua simplicidade: apenas alguns cliques para um Exchange que preserva a sua soberania financeira, sem necessidade de registo ou KYC.



## O que é o Zeus Swap?



O Zeus Swap é um serviço de liquidez Exchange desenvolvido pela Zeus LSP que permite swaps atómicos entre a rede principal Bitcoin e a Lightning Network. Trata-se de uma infraestrutura técnica que utiliza swaps submarinos e swaps inversos para facilitar a conversão bidirecional entre BTC On-Chain e satoshis Lightning, preservando simultaneamente a natureza não-custodial da operação.



### Arquitetura técnica



O Zeus Swap utiliza a tecnologia de troca atómica Bitcoin/Lightning de Boltz, de código aberto. O protocolo utiliza contratos bloqueados no tempo Hash (HTLC): contratos que bloqueiam fundos com duas condições de libertação (revelação de um segredo criptográfico ou expiração do tempo).



Para uma troca submarina (On-Chain → Lightning), o utilizador envia bitcoins para um Address que incorpora o Hash de um Invoice Lightning. O Zeus LSP só desbloqueia estes fundos pagando ao Invoice correspondente, revelando a pré-imagem que desbloqueia automaticamente os bitcoins. Este mecanismo garante a atomicidade.



Para uma troca inversa (Lightning → On-Chain), o utilizador paga um Lightning Invoice a partir do Zeus LSP, revelando uma pré-imagem que permite a libertação de uma transação Bitcoin preparada para o Address de destino.



Para mais pormenores sobre o funcionamento do Lightning Network, consulte o nosso curso dedicado :



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Modelo de negócio



A Zeus LSP actua como criador de mercado, mantendo a liquidez do On-Chain e do Lightning para honrar os swaps. Para os swaps, a Zeus aplica uma taxa variável (normalmente 0,1% a 0,5%, dependendo da direção e das condições) mais a taxa Mining do Bitcoin, apresentada de forma transparente antes da validação.



Como Lightning Service Provider, a Zeus optimiza os custos graças à sua experiência em abertura de canais a pedido, encaminhamento eficiente e soluções de liquidez personalizadas.



### Integração



O Zeus Wallet integra nativamente o serviço, permitindo trocas sem sair do Interface Bitcoin/Lightning. Isto elimina o atrito de copiar e colar entre aplicações.



A rede independente Interface permanece acessível a todas as carteiras, garantindo a máxima flexibilidade de utilização.



## Principais caraterísticas



### Swaps bidireccionais



O Zeus Swap oferece dois tipos de Exchange:



**Troca de submarinos (On-Chain → Lightning)**: injecta liquidez Lightning a partir das suas reservas Bitcoin, útil para alimentar um nó móvel Wallet ou Lightning sem abrir canais manualmente.



**Trocas inversas (Lightning → On-Chain)**: converter satoshis Lightning em bitcoins On-Chain para armazenamento a longo prazo, evitando o encerramento dispendioso de canais.



### Interfaces de utilizador



**Interface web** (swaps.zeuslsp.com): experiência simplificada sem registo, processo guiado com visualização em tempo real das taxas e do estado.



**Integração do Zeus Wallet**: trocas diretas a partir da aplicação, gestão automática das facturas e dos endereços, eliminando os erros de manipulação.



### Segurança e recuperação



Cada troca gera um Contract único com parâmetros imutáveis: Hash Lightning, timeout, Address de reembolso. Em caso de falha, recuperação automática através do Address fornecido, independentemente do Zeus LSP.



**Zeus Swaps Rescue Key**: durante uma troca On-Chain → Lightning, o Zeus gera automaticamente uma chave de recuperação universal que substitui os antigos ficheiros de reembolso individuais. Esta chave única funciona em qualquer dispositivo e para todas as trocas criadas com ela. É crucial descarregar e guardar esta chave num local seguro para poder recuperar os seus fundos no caso de uma falha na troca.



### Otimização da rede



O Zeus Swap ajusta automaticamente os tempos de expiração e as taxas Mining de acordo com as condições da rede. Os utilizadores do Zeus beneficiam de opções avançadas: escolha do LSP, atrasos personalizados, compatibilidade com outros serviços (Boltz).



## Instalação e utilização



### Métodos de acesso



**Interface web** (swaps.zeuslsp.com): solução universal compatível com todas as carteiras, sem necessidade de instalação, ideal para uma utilização ocasional.



**Zeus app** (iOS/Android): experiência integrada que combina Wallet e swaps, adequada para utilizadores regulares.



Consulte o nosso tutorial Zeus para saber mais sobre este Wallet completo:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Configuração Web



**On-Chain → Lightning**: O processo começa com a configuração da troca no Interface web Zeus Swap. O utilizador pode utilizar a seta entre os campos On-Chain e Lightning para inverter o sentido da troca.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: seleção do montante (Sats 50.000 → Sats 49.648 após taxas) com visualização transparente das taxas de rede (Sats 302) e do serviço Zeus (Sats 50).*



Durante o processo, o Zeus oferece-lhe a possibilidade de descarregar a chave de recuperação universal :



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Diálogo de descarregamento para a Chave de Resgate Zeus Swaps - uma chave universal que substitui os antigos ficheiros de reembolso individuais*



Se já tiver uma chave, o Zeus permite-lhe verificá-la:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface para verificar a validade de uma Chave de Resgate de Trocas Zeus existente*



Uma vez configurado, o Zeus gera o depósito Bitcoin Address e apresenta as instruções :



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Página de conclusão da troca: Código QR e Bitcoin Address para enviar 50.000 Satss, com lembrete da data de expiração de 24 horas*



A troca aguarda então a confirmação do Bitcoin:



![Attente de confirmation](assets/fr/05.webp)



*Estado "Transação no Mempool" - à espera da confirmação do Bitcoin para finalizar o swap*



Uma vez confirmada, a troca é concluída automaticamente:



![Swap réussi](assets/fr/06.webp)



*Confirmação de sucesso: 49 648 Sats recebidos no Lightning após dedução das taxas de rede e de serviço*



### Utilizar a aplicação Zeus



**Lightning → On-Chain**: A aplicação Zeus oferece uma experiência integrada para swaps inversos (Lightning para Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Ecrã principal do Zeus com os saldos Lightning (69 851 Sats) e On-Chain (38 018 Sats), acesso às trocas através do menu lateral*



![Configuration du swap reverse](assets/fr/08.webp)



*Criação de troca inversa Interface: 50.000 Sats Lightning → 49.220 Sats On-Chain, com as tarifas de rede (530 Sats) e de serviço (250 Sats) claramente indicadas. Os utilizadores podem introduzir manualmente um Bitcoin que recebe um Address, ou um generate automaticamente a partir do Wallet Zeus através do botão "generate On-Chain Address".*



![Finalisation du swap mobile](assets/fr/09.webp)



*Ecrãs de finalização: Ecrã de pagamento Lightning Invoice com "PAY THIS Invoice", confirmação do pagamento Lightning bem sucedido em 9,96 segundos e extrato de saldo com os 49 162 Sats a aguardar confirmação*



### Vigilância e segurança



Cada troca tem um identificador único com acompanhamento em tempo real. Visualização completa do progresso, alertas automáticos para as datas de expiração. Recomendações automáticas de carregamento em função das condições da rede.



## Vantagens e limitações



### Benefícios





- Simplicidade**: Troca em poucos cliques vs. manipulação manual de canais
- Sem custódia**: sem KYC, sem conta, fundos nunca confiados a terceiros
- Transparência**: taxas explicitamente apresentadas antes da validação (0,1% a 0,5% + mínimo, dependendo dos testes dos utilizadores - verificar as taxas actuais em cada swap)
- Integração móvel**: experiência nativa no Zeus Wallet



### Limitações





- Tempos de expiração**: 24-48h no máximo, falha se o Bitcoin não for confirmado a tempo
- Limites de montante**: mínimo 25 000 Sats, liquidez Zeus LSP variável em função das condições
- Traços On-Chain**: Scripts do HTLC potencialmente identificáveis pela análise do Blockchain
- Confirmação necessária**: mínimo de 10 minutos para validação do Bitcoin



## Melhores práticas



### Calendário e custos





- Ver o Mempool.space em alturas de pouco congestionamento
- Preferir fins-de-semana e horas de vazio para reduzir os custos de Mining
- Calcular a rentabilidade: pequenos montantes vs. abertura direta do canal



### Segurança





- Verificar cuidadosamente os endereços Bitcoin (recomenda-se copiar e colar)
- Cópia de segurança da chave de recuperação do Zeus Swaps**: transfira e guarde a chave de recuperação num local seguro
- Documento: Contract ID, reembolso Address, data de validade
- Utilizar as taxas Mining adequadas para uma confirmação atempada



### Estratégia de utilização





- Equilibrar a liquidez On-Chain/Lightning de acordo com as suas necessidades
- Zeus Swap para ajustamentos pontuais, canais diretos para necessidades permanentes



## Comparação com outros serviços de swap



### Zeus Swap vs Boltz Exchange



O Zeus Swap utiliza a tecnologia de backend do Boltz, mas introduz algumas melhorias cruciais:



**Benefícios do Zeus Swap** :




- Interface unificado**: integração nativa em Zeus Wallet vs Interface técnica Web Boltz
- API WebSocket**: actualizações em tempo real vs. sondagem manual
- Gestão automatizada**: faturação automática e gestão Address
- Suporte móvel**: apenas otimização para smartphone vs. desktop
- Documentação Swagger**: API REST completa para programadores



**O Boltz continua a ser vantajoso** para total independência e utilização com qualquer configuração Bitcoin/Lightning.



O Zeus Swap transforma a tecnologia Boltz comprovada numa experiência de utilizador comum, comparável à diferença entre um protocolo bruto e uma aplicação de fácil utilização.



### Zeus Swap vs Phoenix/Breez (swaps integrados)



O Phoenix e o Breez integram funcionalidades de troca transparentes que escondem a complexidade técnica do utilizador final. O Phoenix utiliza um sistema de troca automática em que o utilizador não distingue explicitamente entre camadas Bitcoin: ele "envia para um Bitcoin Address" e a aplicação trata da troca em segundo plano.



Esta abordagem ultra-simplificada é perfeitamente adequada para principiantes, mas limita a compreensão e o controlo das operações. O Zeus Swap adopta uma filosofia mais pedagógica: os utilizadores compreendem que estão a trocar entre duas camadas distintas, desenvolvendo gradualmente a sua compreensão do ecossistema de dois Layer Bitcoin.



## Comparação pormenorizada das taxas e limites (2024)



⚠️ **Aviso**: As taxas podem variar ao longo do tempo, dependendo das condições do mercado e das actualizações do serviço. Verificar sempre as taxas apresentadas no Interface antes de validar uma troca.



| Service | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Montant minimum |
|---------|-------------------------|----------------------|-----------------|
| **Zeus Swap** | ~0.1% + frais minage | 0.5% + frais minage | 25 000 sats |
| **Boltz** | 0.2% + frais minage | 0.5% + frais minage | 50 000 sats |
| **Phoenix** | Frais minage uniquement | 0.4% fixe | 10 000 sats |
| **Breez** | 0.25% + frais réseau | 0.5% + frais minage | 50 000 sats |

O Zeus Swap oferece um equilíbrio entre a facilidade de utilização e o controlo técnico: mais acessível do que o Boltz, mais flexível do que o Phoenix/Breez, com uma abordagem rigorosa e sem custódia.



## Conclusão



O Zeus Swap representa uma inovação significativa no ecossistema Bitcoin, resolvendo de forma elegante o desafio da interoperabilidade entre a rede principal e o Lightning Network. Ao combinar a robustez criptográfica dos swaps atómicos com uma experiência de utilizador acessível, este serviço democratiza a gestão dual-Bitcoin do Layer sem comprometer os princípios da soberania financeira.



A arquitetura sem custódia do Zeus Swap, herdada da comprovada tecnologia Boltz, garante que os seus fundos permanecem sob o seu controlo exclusivo durante todo o processo de swap. Esta abordagem respeita o espírito da Bitcoin, ao mesmo tempo que oferece a conveniência ao utilizador necessária para uma adoção generalizada. A transparência dos preços e a ausência de processos KYC reforçam esta proposta de valor única.



Para o utilizador moderno do Bitcoin, o Zeus Swap é uma ferramenta estratégica para otimizar a distribuição da liquidez de acordo com as necessidades: Armazenamento seguro On-Chain para poupanças a longo prazo, disponibilidade Lightning para despesas diárias e microtransacções. Esta flexibilidade transforma a gestão do Bitcoin de um constrangimento técnico numa vantagem competitiva.



A evolução futura do Zeus Swap, apoiada pela experiente equipa Zeus LSP e pela comunidade de código aberto Boltz, promete melhorias contínuas em termos de custos, tempos de processamento e experiência do utilizador. Este serviço faz parte de uma tendência mais ampla para a maturação da infraestrutura Bitcoin, em que a sofisticação técnica se torna transparente para o utilizador final.



## Recursos



### Documentação oficial




- [Zeus Swap - Portal Web](https://swaps.zeuslsp.com)
- [Zeus Wallet - Aplicação móvel](https://zeusln.app)
- [Blogue Zeus - Anúncios e tutoriais](https://blog.zeusln.com)
- [Documentação técnica Zeus](https://docs.zeusln.app)



### Comunidade e apoio




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegrama Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)