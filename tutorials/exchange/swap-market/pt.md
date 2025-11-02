---
name: SwapMarket
description: Agregador de serviços de swap Bitcoin e Lightning
---

![cover](assets/cover.webp)



A transferência de fundos entre Bitcoin On-Chain e Lightning Network requer geralmente ou a abertura manual de canais Lightning (técnicos e dispendiosos), ou a utilização de plataformas de swap centralizadas com KYC. A SwapMarket oferece uma alternativa: Swaps atómicos Trustless através de fornecedores competitivos, sem KYC.



Inovação: embora os fornecedores sejam intermediários, o HTLC (*Hash Time Locked Contracts*) garante matematicamente que os seus fundos permanecem sob o seu controlo. A agregação de vários fornecedores (Boltz, ZEUS Swaps, Eldamar, Middle Way) cria uma concorrência de preços. Interface web open-source auto-hospedável.



## O que é o SwapMarket?



Um agregador de código aberto lançado em 2024, o SwapMarket funciona como um comparador de fornecedores de swaps Bitcoin/Lightning. O utilizador compara instantaneamente as condições (taxas, liquidez, limites) e seleciona o melhor fornecedor.



### Arquitetura técnica



**Frontend do lado do cliente**: aplicação 100% do lado do cliente (Fork Boltz Web App) alojada no GitHub Pages. O código é executado no navegador sem servidor backend. Histórico armazenado localmente (cookies/cache). Código-fonte público e auditável.



**Descoberta de provedor** : Lista codificada pelo Hard em `src/configs/Mainnet.ts`. Novos provedores adicionados via Pull Request ou email.



**Backends independentes**: Cada fornecedor tem o seu próprio backend Boltz. O Interface consulta as APIs em tempo real para comparar cotações instantaneamente.



**HTLC Swaps atómicos**: Os contratos Hash Time Locked garantem a atomicidade: ou o swap é executado, ou cada parte recupera os seus fundos. O risco de contraparte é matematicamente eliminado.



### Filosofia



O SwapMarket reduz a centralização ao criar concorrência entre os fornecedores no que respeita a taxas e liquidez. Sem KYC, código open-source auto-hospedável, multiplicação de operadores independentes para evitar pontos únicos de falha.



## Principais caraterísticas



### Mercado de fornecedores



O Interface apresenta todos os fornecedores activos: nome do fornecedor, taxas aplicadas (percentuais e/ou fixas), montantes mínimos/máximos disponíveis e tipos de swap suportados. A aplicação consulta diretamente as APIs de cada fornecedor referenciado no ficheiro de configuração para obter cotações em tempo real. A concorrência entre fornecedores garante taxas óptimas, geralmente em torno de 0,5% para swaps padrão.



### Swaps bidireccionais



**Swap-in (On-Chain → Lightning)**: Converter On-Chain BTCs em Lightning satoshis. Caso de uso: alimentar um Wallet Lightning móvel, obter capacidade de entrada num nó ou ter liquidez instantânea.



**Swap-out (Lightning → On-Chain)**: Converter satoshis de Lightning em On-Chain BTC. Caso de uso: despejar Wallet Lightning em armazenamento Cold ou reequilibrar a liquidez entre camadas.



### Segurança e recuperação



**Trustless Trocas atómicas: O HTLC garante que o Exchange é concluído na totalidade ou que cada parte recupera a sua participação. O risco de contraparte é matematicamente eliminado.



**Mecanismo de resgate**: Cada swap tem uma data de expiração (TIMELOCK). Se a troca falhar, os fundos são automaticamente reembolsados após a expiração. O utilizador tem sempre a possibilidade de recuperar os seus bitcoins.



**Chaves de recuperação**: O SwapMarket permite-lhe exportar chaves de recuperação para trocas em curso. No caso de um problema, estas chaves podem ser utilizadas para finalizar ou cancelar uma troca a partir de qualquer dispositivo.



## Instalação e acesso



### Interface web



O SwapMarket não requer instalação. O acesso é feito através do browser, visitando https://swapmarket.github.io. Para obter a máxima confidencialidade, utilize o Brave, o Firefox com extensões anti-rastreio ou o LibreWolf. O navegador Tor é recomendado para o anonimato da rede.



Não é necessário registo, correio eletrónico ou verificação de identidade.



### Auto-hospedagem (opcional)



Para utilizadores técnicos que pretendam eliminar qualquer dependência do domínio oficial do GitHub Pages, o SwapMarket pode ser executado localmente :



**Via npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Via Docker** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



A aplicação estará acessível em `http://localhost:3000`. A auto-hospedagem garante um controlo total sobre o Interface, elimina o risco de censura do domínio oficial e permite que o código fonte seja auditado antes da execução.



### Configuração inicial



**Wallet Lightning**: Certifica-te de que tens um Wallet Lightning operacional (Phoenix, Zeus, BlueWallet, etc.). Para as trocas, pagará um generate e um Lightning Invoice. Para as trocas, pagarás um Lightning Invoice.



**Wallet On-Chain**: Para as trocas, é necessário um Wallet Bitcoin On-Chain para enviar fundos. Para as trocas, prepare um Bitcoin para receber o Address.



**Configuração opcional**: O SwapMarket guarda o histórico de trocas e as preferências nos cookies do browser. Não é necessário criar uma conta.



## Acesso às definições e à Chave de Recuperação



Antes de efetuar as suas primeiras trocas, recomendamos vivamente que descarregue a sua **Chave de resgate**. Esta chave de emergência permite-lhe recuperar os seus fundos em caso de problema técnico ou de perda de acesso ao seu dispositivo.



### Parâmetros de acesso



Na página principal do SwapMarket, clique no ícone da engrenagem (⚙️) no canto superior direito do Interface, junto ao formulário de troca.



![Accès aux paramètres](assets/fr/01.webp)



### Definições da página



A página Definições abre-se, apresentando várias opções de configuração:





- Denominação**: Escolha entre BTC ou Sats
- Separador decimal**: Separador decimal (, ou .)
- Notificações de áudio/navegador**: Notificações de áudio e do browser
- Chave de recuperação** : Descarregar a chave de recuperação
- Registos**: Ver, descarregar ou eliminar registos



![Page Settings](assets/fr/02.webp)



### Descarregar o Rescue Key



Clique no botão **Download** ao lado de "Rescue Key".



**Pontos importantes** :




- A Rescue Key é uma **chave de emergência** que funciona para todas as suas futuras trocas
- Guardar esta chave num local **seguro e permanente** (gestor de senhas, cofre digital)
- No caso de um problema de swap (timeout, falha técnica), esta chave permite-lhe recuperar os seus fundos



## Criar um swap passo a passo



### Troca: Relâmpago → Bitcoin



Este primeiro exemplo mostra como converter satoshis Lightning em bitcoins On-Chain.



**Passo 1: Trocar a configuração



Na página principal, selecionar o formulário de troca :




- LIGHTNING** (campo superior): Introduzir o montante que pretende enviar em Sats Lightning (exemplo: 30.000 Sats)
- Bitcoin** (campo inferior): O montante que receberá é automaticamente apresentado após a dedução das taxas (exemplo: Sats 29.320)



No campo inferior, cole o seu **receiving Bitcoin Address** onde pretende receber os fundos. Verifique cuidadosamente este Address.



O prestador predefinido é normalmente o Boltz Exchange. As taxas de rede e as taxas do fornecedor são claramente apresentadas.



![Configuration swap-out](assets/fr/03.webp)



**Etapa 2: Seleção do fornecedor



Clique no menu pendente do fornecedor (predefinição: "Boltz Exchange") para visualizar todos os fornecedores de liquidez disponíveis.



Abre-se uma janela modal que apresenta uma tabela de comparação:




- Estado**: Indicador Green se o fornecedor estiver ativo
- Pseudónimo**: Nome do fornecedor (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Taxa**: Encargos aplicados pelo prestador (geralmente entre 0,49% e 0,5%)
- Swap máximo**: Montante máximo aceite para um swap



Compare as taxas e os montantes máximos e, em seguida, selecione o prestador de serviços da sua preferência.



**Atenção**: O Interface de seleção do prestador não apresenta os **montantes mínimos** para cada prestador. Esta informação só aparece na Interface de criação de swap, depois de um prestador ter sido selecionado. Os montantes mínimos e máximos podem variar de fornecedor para fornecedor e podem mudar ao longo do tempo. **Verifique sempre estes limites no momento do seu swap**: se o montante que pretende trocar estiver fora dos limites de um prestador, pode selecionar outro mais adequado à sua transação.



![Sélection du provider](assets/fr/04.webp)



**Passo 3: Criação do swap e pagamento do Lightning



Clique no botão amarelo **"CREATE ATOMIC SWAP "**. O SwapMarket irá criar um **Lightning Invoice** (BOLT11) para pagar a partir do seu Wallet Lightning.



A página apresenta :




- ID de troca**: Identificador de swap único (exemplo: J4ymFIMVR6Hm)
- Estado**: "swap.created" (swap criado, a aguardar pagamento)
- Código QR**: Digitalize-o com o seu Wallet Lightning
- Invoice Lightning**: Cadeia de caracteres que começa por "lnbc" (exemplo: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Pague este Invoice a partir do seu Wallet Lightning (Phoenix, Zeus, BlueWallet, etc.). É indicado o montante exato a pagar (exemplo: 30 000 Sats).



![Paiement Lightning](assets/fr/05.webp)



**Etapa 4: Confirmação e aceitação



Assim que o pagamento Lightning for confirmado, o SwapMarket recebe instantaneamente o seu pagamento e o fornecedor transmite a transação Bitcoin para o seu Address.



O estado muda para **"Invoice.settled "** (Invoice pago), e aparece uma mensagem de confirmação.



Os seus bitcoins On-Chain estarão disponíveis assim que a transação for confirmada (normalmente dentro de alguns minutos a algumas horas, dependendo das taxas Mining escolhidas pelo fornecedor).



![Confirmation swap-out](assets/fr/06.webp)



Pode clicar em **"OPEN CLAIM TRANSACTION "** para visualizar a transação Bitcoin num explorador Blockchain.



### Troca: Bitcoin → Relâmpago



Este segundo exemplo mostra como converter bitcoins On-Chain em satoshis Lightning.



**Passo 1: Trocar a configuração



Na página principal, selecionar o formulário de troca :




- Bitcoin** (campo superior): Introduzir o montante que pretende enviar em Sats Bitcoin (exemplo: 63 400 Sats)
- LIGHTNING** (campo inferior): O montante que irá receber é automaticamente apresentado após a dedução das taxas (exemplo: 62 884 Sats)



No campo inferior, cole um Lightning** Invoice (BOLT11) gerado a partir do seu Lightning Wallet, ou utilize o seu LNURL Address se o seu Wallet o suportar.



![Configuration swap-in](assets/fr/07.webp)



**Passo 2: Verificação da chave de recuperação



Depois de clicar em **"CREATE ATOMIC SWAP "**, aparece uma janela modal, pedindo-lhe para verificar a sua Rescue Key.



![Modal Rescue Key](assets/fr/08.webp)



**Chave de recuperação Boltz**: Como já carregou a sua chave de recuperação durante a configuração inicial (ver secção anterior), clique no botão **"VERIFY EXISTING KEY "** para importar a chave que guardou.



Selecione o ficheiro Rescue Key transferido anteriormente. Após a verificação bem sucedida, o Interface passa automaticamente para o passo seguinte.



**Etapa 3: Bitcoin** depósito Address



O SwapMarket gera agora um **único Bitcoin Address** contendo o HTLC Contract ligado ao seu Lightning Invoice.



A página apresenta :




- ID de troca**: Identificador único (exemplo: 1kGmB6JyGqU4)
- Estado** : "Invoice.set" (Invoice definido, a aguardar pagamento Bitcoin)
- Código QR**: Depósito Bitcoin Address
- Bitcoin** Address: Normalmente começa com "bc1p..." (exemplo: bc1p5mvtwxapjkds...9d4n9f)
- Aviso em amarelo** : "Certifique-se de que a sua transação é confirmada dentro de ~24 horas após a criação desta troca!"



Este período de ~24 horas é o **timeout** do HTLC Contract. Se a sua transação Bitcoin não for confirmada dentro deste período de tempo, a troca falhará e terá de utilizar a sua Rescue Key para recuperar os seus fundos.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Pode copiar o Address clicando no botão **"Address"** ou digitalizar o código QR diretamente a partir do seu Wallet On-Chain.



**Passo 4: Enviar bitcoins



A partir do seu Wallet Bitcoin On-Chain, envie **exatamente** o montante indicado (por exemplo, 63 400 Sats) para o Address gerado.



**Importante**: Utilizar taxas Mining adequadas para garantir uma confirmação rápida. Se a taxa for demasiado baixa e a transação permanecer no Mempool para além do tempo limite (~24h), a troca falhará.



Depois de a transação ter sido enviada, o SwapMarket detecta que está em Mempool e apresenta :




- Estado** : "transação.Mempool"
- Mensagem**: "A transação está em Mempool - A aguardar confirmação para concluir a troca"



![Transaction en mempool](assets/fr/10.webp)



**Etapa 5: Confirmação e receção do relâmpago



Assim que a transação Bitcoin recebe a sua primeira confirmação, o fornecedor paga automaticamente o seu Lightning Invoice. O utilizador recebe instantaneamente os satoshis no seu Lightning Wallet.



O estado muda para **"transação.reclamação.pendente "** e, em seguida, é apresentada uma mensagem de confirmação:



![Confirmation swap-in](assets/fr/11.webp)



Os seus satoshis Lightning estão imediatamente disponíveis no seu Wallet.



## Vantagens e limitações



### Benefícios



**Concorrência tarifária**: A agregação de fornecedores cria uma concorrência natural que faz baixar as taxas (0,49% a 0,5%).



**Confidencialidade**: Sem KYC, Interface 100% do lado do cliente (sem transmissão de dados pessoais), compatível com o navegador Tor.



**Sem custódia**: O HTLC garante matematicamente o controlo exclusivo dos seus fundos. Ou a troca é bem sucedida, ou recebe os seus bitcoins de volta.



**Open-source self-hostable**: código público auditável, implementável localmente para máxima resistência à censura.



### Limitações



**Liquidez limitada**: Número limitado de fornecedores activos (Boltz, Eldamar, MiddleWay, dependendo do período). Os montantes máximos podem ser limitados.



**Tempo de expiração**: Tempo limite de 24h a 48h. Se a transação On-Chain não for confirmada antes da expiração, é necessária uma recuperação manual.



**Centralização do Interface**: Embora auto-hospedável, o Interface oficial está hospedado no GitHub Pages. Se o GitHub censurar o repositório, o acesso via swapmarket.github.io será bloqueado (solução: auto-hospedagem).



**Traços de On-Chain**: Os scripts HTLC são potencialmente identificáveis pela análise avançada do Blockchain.



## Melhores práticas



### Configuração segura



**Descarrega a tua Chave de Recuperação**: Antes das suas primeiras trocas, transfira a sua Chave de Recuperação a partir das Definições (consulte a secção dedicada acima). Esta chave única funcionará para todas as suas futuras trocas, permitindo-lhe recuperar os seus fundos em caso de problema.



**Utilize o Navegador Tor**: Para máxima confidencialidade, aceda ao SwapMarket através do Navegador Tor para ocultar o seu IP Address.



**Considere a possibilidade de auto-hospedagem**: Para utilizadores técnicos, executar a sua própria instância do SwapMarket elimina a dependência do domínio oficial do GitHub Pages.



### Otimização da troca



**Vigiar o Mempool**: Verificar o Mempool.space antes de uma troca. Escolha alturas de baixa atividade para minimizar os custos do Mining.



**Verificar endereços**: Para trocas, verifique meticulosamente o seu Address de receção. Utilize copiar e colar e verifique os primeiros 5 e os últimos 5 caracteres.



**Testar com pequenas quantidades**: Comece com o mínimo permitido (25.000 a 50.000 Sats). Aumente gradualmente quando dominar o processo.



**Documente os seus swaps**: Anote o ID de cada swap, o Address de resgate e a data de expiração. Esta informação facilita o controlo e a recuperação em caso de problema técnico.



### Estratégia de utilização



**Equilibre o seu fluxo de caixa**: Utilize o SwapMarket para ajustar a sua afetação entre On-Chain (poupanças, segurança a longo prazo) e Lightning (despesas diárias, pagamentos imediatos) de acordo com as suas necessidades reais.



**Calcular a rentabilidade**: Para necessidades permanentes de liquidez no Lightning, compare o custo acumulado de swaps repetidos versus a abertura direta de um canal Lightning. O SwapMarket é excelente para ajustes pontuais, não necessariamente para grandes fluxos regulares.



## SwapMarket vs Boltz: Qual é a diferença?



### Boltz: Tecnologia vs. Serviço



**Boltz é a tecnologia de código aberto** (`boltz-backend` no GitHub) que implementa trocas atómicas via HTLC entre Bitcoin, Lightning e Liquid.



**Ponto crítico**: Todos os fornecedores de SwapMarket (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) implementam a sua própria instância do backend Boltz. A tecnologia subjacente é, por conseguinte, idêntica. Uma vulnerabilidade no backend da Boltz afectaria potencialmente todos os fornecedores, mas a natureza de código aberto do sistema permite a auditoria da comunidade.



*o *Boltz Exchange** é um serviço único operado pela equipa Boltz, enquanto o **SwapMarket** reúne vários fornecedores que utilizam a tecnologia Boltz, criando um ambiente de preços competitivo.



Para mais informações, consulte os tutoriais Boltz e Zeus Swap:



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Principais diferenças



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**Vantagens do SwapMarket**: Concorrência de preços, diversificação de instâncias de backend, comparação em tempo real.



**Alternativas tecnológicas** (não compatíveis com o SwapMarket): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Estas soluções utilizam as suas próprias implementações de swaps submarinos.



**Recomendação**: Utilizar o Boltz Exchange para simplicidade ou o SwapMarket para otimizar os custos através da concorrência. Ambos são equivalentes em termos de segurança (HTLC sem custódia).



## Conclusão



O SwapMarket facilita as trocas Bitcoin/Lightning ao agregar múltiplos fornecedores num único Interface. A arquitetura HTLC garante a natureza não-custodial dos swaps, a ausência de KYC preserva a confidencialidade e o código auto-hospedado de fonte aberta reforça a resistência à censura.



A concorrência entre fornecedores melhora as taxas e multiplica as fontes de liquidez. Para otimizar a gestão dos dois Layer (poupanças On-Chain, despesas Lightning), o SwapMarket é uma ferramenta prática que preserva a soberania e a confidencialidade financeiras.



## Recursos



### Documentação oficial




- [SwapMarket - Aplicação Web](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Documentação técnica](https://docs.boltz.Exchange/)
- [Guia de auto-hospedagem](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Projectos relacionados




- [Boltz Exchange](https://boltz.Exchange) - Serviço de troca atómica original
- [ZEUS Swaps](https://zeusln.com) - Fornecedor de swaps de relâmpagos