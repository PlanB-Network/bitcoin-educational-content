---
name: Blockstream App - Desktop
description: Como utilizar o Hardware Wallet com a aplicação Blockstream num computador?
---
![cover](assets/cover.webp)



## 1. Introdução



### 1.1 Objetivo do tutorial





- Este tutorial explica como utilizar a **Aplicação Blockstream** num computador para gerir um Bitcoin **onchain** Wallet com um **Hardware Wallet**, permitindo transacções seguras registadas no Blockchain Bitcoin principal.
- Abrange a instalação, a configuração inicial, a ligação de um Hardware Wallet e a receção e envio de bitcoins onchain.
- Nota: Outros tutoriais nos apêndices abrangem Liquid, Watch-Only e a aplicação móvel.



### 1.2 Público-alvo





- **Iniciantes**: Utilizadores que pretendem gerir os seus bitcoins com um software de secretária seguro e um Hardware Wallet.
- **Utilizadores intermédios**: Pessoas que procuram compreender como utilizar um Hardware Wallet para transacções onchain e opções de privacidade como Tor ou SPV.



### 1.3. Antecedentes das carteiras de hardware





- **Hardware Wallet**, **Cold Wallet**: Um dispositivo físico que armazena chaves privadas offline, oferecendo um elevado nível de segurança contra ciberataques, ao contrário das **Hot wallets** (carteiras de software em dispositivos ligados).
- **Utilização recomendada**:
    - Ideal para garantir grandes montantes ou poupanças a longo prazo.
    - Adequado para utilizadores preocupados com a segurança que pretendem proteger os seus fundos contra os riscos associados aos dispositivos ligados.
- **Limitações**: Requer software como o Blockstream App para visualizar saldos, endereços generate e transmitir transacções assinadas por Hardware Wallet.



## 2. Apresentação da aplicação Blockstream





- A **Blockstream App** é uma aplicação móvel (iOS, Android) e de ambiente de trabalho para gerir carteiras e activos do Bitcoin no Liquid Network. Adquirida pela Blockstream em 2016, chamava-se *GreenAddress*, passou a chamar-se *Blockstream Green* (2019) e chama-se agora *Blockstream app* (2025).
- **Características principais**:
- **Transacções Onchain** em Blockchain Bitcoin.
    - Transacções na rede **Liquid** (Sidechain para trocas rápidas e confidenciais).
- **Carteiras só de observação** para monitorizar fundos sem acesso a chaves.
    - Opções de privacidade: ligação através de **Tor**, ligação a um **nó pessoal** através de Electrum, ou verificação **SPV** para reduzir a dependência de nós de terceiros.
    - Funções **Replace-by-fee (RBF)** para acelerar as transacções não confirmadas.
- **Compatibilidade**: Integra carteiras de hardware como **Blockstream Jade**.
- **Interface**: Intuitivo para principiantes, com opções avançadas para especialistas.
- **Nota**: Este guia centra-se na utilização do onchain com um Hardware Wallet na versão para computador. Outros tutoriais fornecidos como apêndices abrangem a utilização na aplicação móvel, para as funcionalidades onchain, Liquid e Watch-Only.



## 3. Instalar e configurar o Blockstream App Desktop



### 3.1. descarregar





- Aceda ao [sítio Web oficial] (https://blockstream.com/app/) e clique em "_Download Now_". Descarregar a versão correspondente ao seu sistema operativo (Windows, macOS, Linux).
- **Nota**: Certifique-se de que efectua a transferência a partir da fonte oficial para evitar software fraudulento.



### 3.2. configuração inicial





- **Ecrã inicial**: Quando aberta pela primeira vez, a aplicação apresenta um ecrã sem um Wallet configurado. As carteiras criadas ou importadas aparecerão aqui mais tarde.



![image](assets/fr/02.webp)





- **Personalizar definições**: Clique no ícone de definições no canto inferior esquerdo, ajuste as opções abaixo e, em seguida, saia do Interface para continuar.



![image](assets/fr/03.webp)



#### 3.2.1. Parâmetros gerais





- No menu Definições, clique em "**Geral**".
- **Função**: Alterar o idioma do software e ativar funções experimentais, se necessário.



![image](assets/fr/04.webp)



#### 3.2.2. Ligação via Tor





- No menu Definições, clique em "**Rede**".
- **Função**: Encaminhar o tráfego de rede através do **Tor**, uma rede anónima que encripta as suas ligações.
- **Porquê?**: Esconde o seu IP Address e protege a sua privacidade, ideal se não confia na sua rede (Wi-Fi pública, por exemplo).
- **Desvantagem**: Pode tornar a aplicação mais lenta devido à encriptação.
- **Recomendação**: Ativar o Tor se a confidencialidade for uma prioridade, mas testar a velocidade da ligação.



![image](assets/fr/05.webp)



#### 3.2.3. Ligação a um nó pessoal





- No menu Definições, clique em "**Servidores personalizados e validação**".
- **Função**: Liga a aplicação ao seu próprio **nó Bitcoin completo** através de um **servidor Electrum**.
- **Porquê?**: Proporciona um controlo total sobre os dados Blockchain, eliminando a dependência dos servidores Blockstream.
- **Pré-requisito**: Um nó Bitcoin configurado.
- **Recomendação**: Utilizadores avançados que pretendem o máximo de soberania.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. Verificação do SPV





- No menu Definições, clique em "**Servidores personalizados e validação**".
- **Função**: Utiliza o **Simplified Payment Verification (SPV)** que descarrega os cabeçalhos dos blocos e verifica as suas transacções por prova de inclusão (Merkle), sem armazenar o Blockchain completo.
- Porquê? Reduz a dependência do nó padrão do Blockstream, mantendo-se leve para os dispositivos.
- **Desvantagem**: Menos seguro do que um Full node, uma vez que depende de nós de terceiros para algumas informações.
- **Recomendação**: Ativar o SPV se não puder utilizar um nó pessoal, mas preferir um Full node para uma segurança óptima.



![image](assets/fr/07.webp)



## 4. Ligar um Hardware Wallet à aplicação Blockstream



### 4.1. Considerações preliminares



#### 4.1.1. Para os utilizadores do Ledger





- O Blockstream Green apenas suporta a aplicação **Bitcoin Legacy** em dispositivos Ledger (Nano S, Nano X).
- Passos a seguir no **Ledger Live** antes de ligar o seu dispositivo :


1. Vá a **"Definições "** → **"Funcionalidades experimentais "** e active o **modo de programador**.


2. Ir para **"My Ledger"** → **"App Catalogue "**, depois instalar a aplicação **Bitcoin Legacy**


3. Abra a aplicação **Bitcoin Legacy** no seu Ledger antes de lançar o Blockstream Green para estabelecer a ligação.




- **Nota**: Certifique-se de que o seu Ledger está desbloqueado com o seu código PIN e que a aplicação Bitcoin Legacy está ativa quando estabelecer a ligação.



#### 4.1.2 Inicialização de um Hardware Wallet





- Se o seu Hardware Wallet (Ledger, Trezor ou Blockstream Jade) nunca foi utilizado (quer com o Blockstream Green, quer com outro software, como o Ledger Live), terá primeiro de o inicializar. Este passo envolve, num ambiente seguro, sem câmaras ou observadores:


1. **Geração de frases seed / Frase Mnemonic** (12, 18 ou 24 palavras): Escreva-a cuidadosamente numa folha de papel.


2. **Verificação da frase seed**: Testar a importação do Wallet a partir das palavras anotadas, por exemplo, verificando a chave pública alargada. A efetuar antes de enviar fundos para o Wallet e de proteger permanentemente a frase seed.


3. **Segurança da frase seed**: Guarde a frase num suporte físico (papel ou metal) e num local seguro. Nunca a guarde digitalmente (sem capturas de ecrã, nuvem ou e-mail).




- **Importante**: A frase seed é o único meio de recuperar os seus fundos se o dispositivo se perder ou avariar. Qualquer pessoa com acesso pode roubar os seus bitcoins.
- **Recursos** para efetuar cópias de segurança e verificar a frase seed :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Configuração para este tutorial :





- Vamos assumir que o Hardware Wallet já foi inicializado com uma frase seed e um código PIN de bloqueio.
- Assumimos que o Hardware Wallet nunca foi ligado à Blockstream App, o que requer a criação de uma nova conta. Se o Hardware Wallet já tiver sido utilizado com a Blockstream App, a conta aparecerá automaticamente quando a aplicação for aberta.



### 4.2. Iniciar a ligação





- No ecrã inicial, clicar em "**Setup a New Wallet**", validar os termos e condições e clicar em "**Get Started**":



![image](assets/fr/08.webp)





- Selecionar a opção "**No Hardware Wallet**":



![image](assets/fr/09.webp)





- Se estiver a utilizar um **Blockstream Jade**, clique no botão correspondente. Caso contrário, selecione "**Ligar um dispositivo de hardware diferente**" :



![image](assets/fr/10.webp)





- Ligue o seu Hardware Wallet ao computador através de USB e selecione-o na aplicação Blockstream :



![image](assets/fr/22.webp)





- Aguarde enquanto a Blockstream App importa as informações da sua carteira:



![image](assets/fr/23.webp)



### 4.3. Criar uma conta





- Se o seu Hardware Wallet já tiver sido utilizado com a aplicação Blockstream, a sua conta aparecerá automaticamente no Interface após a importação. Caso contrário, crie uma conta clicando em "**Create Account**":



![image](assets/fr/24.webp)





- Escolha "**Standard**" para configurar uma carteira Bitcoin clássica:



![image](assets/fr/25.webp)





- Uma vez criada a sua conta, pode aceder à sua carteira principal Interface:



![image](assets/fr/26.webp)





## 5. Utilizar o Wallet em cadeia com um Hardware Wallet



### 5.1. Receber bitcoins





- No ecrã principal da carteira, clicar em "**Receber**" :



![image](assets/fr/27.webp)





- A aplicação apresenta um **Address de receção em branco**. A utilização de um novo Address para cada receção aumenta a sua confidencialidade. Clique em "**Copiar Address**" para copiar o Address ou deixe o remetente ler o código QR apresentado:



![image](assets/fr/12.webp)



**Opções** :




- (1) Clique nas setas para criar um novo Address ligado à sua carteira.
- (2) Para pedir um montante específico, clicar em "**Mais opções**" e depois em "**Pedir montante**". O QR será atualizado e o Address será substituído por um URI de pagamento Bitcoin, tal como: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Para reutilizar um Address anterior, clicar em "**Mais opções**" e depois em "**Lista de endereços**":



![image](assets/fr/14.webp)





- **Verificação**: Verificar cuidadosamente o Address partilhado para evitar erros ou ataques (por exemplo, malware que modifica a área de transferência).
- Quando a transação tiver sido transmitida na rede, aparecerá no seu Wallet. Aguarde de 1 a 6 confirmações para considerar a transação inalterável.



![image](assets/fr/28.webp)



### 5.2. enviar bitcoins





- No ecrã principal da carteira, clique em "**Enviar**".



![image](assets/fr/29.webp)





- **Introduzir dados**:
    - (1) Verificar se o ativo selecionado é **Bitcoin** (onchain).
    - (2) Introduzir o **Address do destinatário** colando-o ou digitalizando um código QR com a sua webcam.
    - (3) Indicar o **montante** a enviar (em BTC, satoshis, ou outras unidades).




![image](assets/fr/16.webp)





- Selecionar **taxas de transação** (opcional) :
 - Escolha entre as opções sugeridas (rápido, médio, lento) de acordo com a urgência, com um tempo estimado de confirmação.
 - Para tarifas personalizadas, ajuste manualmente o número de satoshis por vbyte. Estes são apresentados no ecrã inicial. Ver também [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- **Seleção manual de UTXOs** (opcional): Clique em "**Seleção manual de Coin**" para escolher os UTXOs específicos a utilizar na transação.



![image](assets/fr/18.webp)





- **Verificação preliminar**: Verificar o Address, o montante e as taxas no ecrã de resumo, depois clicar em "**Confirmar transação**". Na realidade, a transação só será libertada para a rede depois de a ter assinado com o seu Hardware Wallet, o único que possui as chaves secretas associadas aos endereços dos quais serão debitados UTXOs (satoshis).



![image](assets/fr/19.webp)





- **Verificação final e assinatura**: Certifique-se de que todos os parâmetros da transação estão corretos **no seu ecrã Hardware Wallet** e, em seguida, assine a transação utilizando-o. Um erro no Address pode resultar numa perda irreversível de fundos.





- **Transmissão**: Uma vez assinada, a aplicação Blockstream transmite automaticamente a transação na rede Bitcoin.



![image](assets/fr/20.webp)





- **Acompanhamento**:
 - A transação aparece no ecrã inicial do Wallet como "pendente" até ser confirmada.
 - Desde que a transação não tenha sido confirmada, a função **Replace-by-fee (RBF)** pode ser utilizada para acelerar a confirmação aumentando a taxa (ver Apêndice).



![image](assets/fr/21.webp)



## Apêndices



### A1. Outros tutoriais Blockstream





- Utilização do Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Importar e acompanhar uma carteira em "Watch-Only" :



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Utilizar a aplicação Blockstream em telemóveis (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Explicação do Replace-by-fee (RBF)





- **Definição**: O Replace-by-fee (RBF) é uma caraterística da rede Bitcoin que permite ao remetente acelerar a confirmação de uma transação **onchain** aumentando a taxa.
- **Limites** :
    - O RBF não está disponível para transacções Liquid ou Lightning.
    - A transação inicial deve ser marcada como compatível com o RBF, o que a Blockstream App faz automaticamente.
- Para mais informações, consultar [o nosso glossário] (https://planb.network/resources/glossary/RBF-replacebyfee).



### A3. Melhores práticas





- **Proteja a sua frase de recuperação**:
    - Guarde a sua frase Hardware Wallet's Mnemonic num suporte físico (papel, metal) num local seguro.
    - Nunca o armazene digitalmente (nuvem, e-mail, captura de ecrã).
    - Tutorial : Guardar a sua frase Mnemonic :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Proteger a sua privacidade**:





    - generate um novo Address para cada receção em cadeia.
    - Ativar **Tor** ou **SPV** para limitar o seguimento.
    - Conecte-se ao seu próprio nó Bitcoin via Electrum para obter o máximo de soberania.
- **Verificar sempre os endereços de envio**:





    - Verificar o Address no ecrã do Hardware Wallet antes de assinar.
    - Utilize copiar/colar ou um código QR para evitar erros manuais.
- **Otimizar os custos**:





    - Ajustar as tarifas em função da urgência e do congestionamento da rede (ver [Mempool.space](https://Mempool.space/)).
    - Utilize o Liquid ou o Lightning para transacções rápidas e de baixo custo que não requerem segurança onchain.
- Atualizar o **software**:





    - Mantenha a sua aplicação Blockstream e o firmware Hardware Wallet actualizados com as mais recentes funcionalidades e patches de segurança.



### A4. Recursos adicionais





- **Ligações oficiais**:
    - [Sítio Web oficial](https://blockstream.com/)
    - [Suporte para a aplicação Blockstream] (https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): documentação e conversação
    - [GitHub](https://github.com/Blockstream/green_qt)





- **Exploradores de blocos**:
    - Onchain : [Mempool.space](https://Mempool.space/)
    - Liquid : [Informações sobre o fluxo de blocos](https://blockstream.info/Liquid)
    - Raio : [1ML (Lightning Network)](https://1ml.com/)





- Proteger a sua frase de recuperação:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Glossário] (https://planb.network/fr/resources/glossary/Liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Glossário] (https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb