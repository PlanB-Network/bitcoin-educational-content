---
name: Aplicação Blockstream - Liquid
description: Como configurar a aplicação Blockstream e utilizar o Liquid Network
---
![cover](assets/cover.webp)


## 1. Introdução


### 1.1 Objetivo do tutorial





- Este tutorial explica como utilizar a aplicação móvel **Blockstream App** para gerir uma carteira **Bitcoin Liquid**, ou seja, transacções registadas diretamente na cadeia lateral Bitcoin "Liquid".
- Abrange a instalação, a configuração inicial, a criação de um Software Wallet e as operações de receção e envio de bitcoins no Liquid.
- Nota: Outros tutoriais nos Apêndices abrangem Onchain, Watch-Only e a versão para computador.



### 1.2 Público-alvo





- Iniciantes**: Utilizadores que pretendem gerir os seus bitcoins com uma aplicação móvel intuitiva, integrando o Liquid Network.
- Utilizadores intermédios**: Pessoas que procuram compreender as funcionalidades onchain e as opções de privacidade, como Tor ou SPV.



### 1.3 Apresentação do Liquid



*o *Liquid** é um **Sidechain** do Bitcoin, desenvolvido pela **[Blockstream](https://blockstream.com/Liquid/)**, concebido para oferecer funcionalidades mais rápidas, mais Confidential Transactions e avançadas, mantendo-se ligado ao Blockchain Bitcoin principal.



Um Sidechain é um Blockchain independente que opera em paralelo com o Bitcoin, usando um mecanismo conhecido como **two-way peg**. Este sistema bloqueia bitcoins no Blockchain principal para criar **Liquid-Bitcoins (L-BTC)**, tokens que circulam no Liquid Network mantendo a paridade de valor com os bitcoins originais. Os fundos podem ser devolvidos ao Blockchain Bitcoin em qualquer altura.



![image](assets/fr/17.webp)






- (1) Peg-in**: Bitcoins (BTC) são bloqueados no Blockchain principal pela federação Liquid. Em troca, uma quantidade equivalente de Bitcoins Liquid (L-BTC), garantindo a paridade entre as duas cadeias, é emitida no Blockchain Liquid e enviada ao utilizador.





- (2) Transacções independentes** : As transacções podem ser executadas simultaneamente e de forma independente no Blockchain (BTC) principal e no Sidechain Liquid (L-BTC), em função das necessidades do utilizador.





- (3) Peg-out**: O utilizador envia bitcoins do Liquid (L-BTC) de volta para a federação Liquid. A federação desbloqueia então uma quantidade equivalente de bitcoins (BTC) no Blockchain principal e transfere-os para o utilizador.



O Liquid assenta numa **federação** de participantes de confiança (bolsas, empresas reconhecidas pelo Bitcoin) que gerem a validação de blocos e a ancoragem bilateral. Ao contrário do Blockchain Bitcoin, que é descentralizado e depende dos mineiros, o Liquid é uma rede **federada**, o que significa que a sua segurança e governação dependem destes participantes. Embora isso implique um compromisso com a descentralização, permite um desempenho optimizado e funcionalidades avançadas.



![image](assets/fr/18.webp)



##### Porquê utilizar o Liquid?





- Velocidade**: As transacções no Liquid são confirmadas em cerca de **1 minuto**, em comparação com 10 minutos ou mais para as transacções onchain, graças aos blocos gerados a cada minuto por uma federação de validadores.
- Confidencialidade melhorada**: O Liquid utiliza o **Confidential Transactions**, que oculta o montante e o tipo de activos transferidos, tornando as transacções mais privadas (embora os endereços permaneçam visíveis).
- Taxas baixas** : As transacções no Liquid são geralmente menos dispendiosas, o que as torna ideais para transferências frequentes ou de pequenos montantes.
- Múltiplos activos**: Para além dos L-BTCs, o Liquid suporta a emissão de outros activos digitais, tais como stablecoins ou tokens, para utilização em aplicações específicas.
- Casos de utilização**: O Liquid é particularmente adequado para trocas entre plataformas, pagamentos rápidos ou aplicações que requerem contratos inteligentes, mantendo-se ligado à segurança do Bitcoin.



**Nota: Este tutorial centra-se na utilização do Liquid através da aplicação Blockstream. Para uma compreensão aprofundada do Liquid Network, encontrará recursos no apêndice.



### 1.4. Lembrete Hot Wallet





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: todos os nomes para uma aplicação instalada num smartphone, computador ou qualquer dispositivo ligado à Internet, que permite gerir e proteger as chaves privadas de um Bitcoin Wallet.
- Ao contrário das **carteiras de hardware**, também conhecidas como **carteiras Cold**, que isolam as chaves offline, as carteiras de software funcionam num ambiente ligado, o que as torna mais vulneráveis a ciberataques.





- Utilização recomendada** :
    - Ideal para gerir quantidades moderadas de Bitcoin, especialmente para transacções diárias.
    - Adequado para principiantes ou utilizadores com recursos limitados, para os quais um Hardware Wallet pode parecer supérfluo.





- Limitações**: Menos seguro para guardar fundos avultados ou poupanças a longo prazo. Neste caso, opte por um Hardware Wallet.




## 2. Apresentação da aplicação Blockstream





- Blockstream App** é uma aplicação móvel (iOS, Android) e de ambiente de trabalho para gerir carteiras Bitcoin e activos no Liquid Network. Adquirida pela [Blockstream] (https://blockstream.com/) em 2016, foi anteriormente designada *Green Address* e depois *Blockstream Green*.
- Caraterísticas principais** :
    - Transacções Onchain** em Blockchain Bitcoin.
    - Transacções na rede **Liquid** (Sidechain para trocas rápidas e confidenciais).
    - Carteiras só de observação** para monitorizar fundos sem acesso a chaves.
    - Opções de privacidade: ligação através de **Tor**, ligação a um **nó pessoal** através de Electrum, ou verificação **SPV** para reduzir a dependência de nós de terceiros.
    - Funções **Replace-by-fee (RBF)** para acelerar as transacções não confirmadas.
- Compatibilidade**: Integra carteiras de hardware como **Blockstream Jade**.
- Interface**: Intuitivo para principiantes, com opções avançadas para especialistas.
- Nota**: Este guia centra-se na utilização do Onchain. Outros tutoriais nos Apêndices abrangem Onchain, Watch-Only e a versão para computador.




## 3. Instalar e configurar a aplicação Blockstream



### 3.1. descarregar





- Para Android** :
    - Descarregue [Blockstream App] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) a partir da Google Play Store.
    - Alternativa: Instalar através do ficheiro APK disponível no [GitHub oficial da Blockstream](https://github.com/Blockstream/green_android).
- Para iOS** :
    - Descarregar [Blockstream App] (https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) da App Store.
- Nota**: Certifique-se de que descarrega a partir de fontes oficiais para evitar aplicações fraudulentas.



### 3.2. configuração inicial





- Ecrã inicial**: Quando aberta pela primeira vez, a aplicação apresenta um ecrã sem um Wallet configurado. As carteiras criadas ou importadas aparecerão aqui mais tarde.



![image](assets/fr/02.webp)





- Personalizar definições**: Clique em "Definições da aplicação", ajuste as opções abaixo, clique em "Guardar", reinicie a aplicação e crie a sua carteira.



![image](assets/fr/03.webp)



#### 3.2.1. Privacidade melhorada (apenas Android)





- Função**: Desactiva as capturas de ecrã, oculta as pré-visualizações de aplicações no gestor de tarefas e bloqueia o acesso quando o telemóvel está bloqueado.
- Porquê? Protege os seus dados contra acesso físico não autorizado ou malware de captura de ecrã.



#### 3.2.2. Ligação via Tor





- Função**: Encaminhar o tráfego de rede através do **Tor**, uma rede anónima que encripta as suas ligações.
- Porquê?**: Oculta o seu IP Address e protege a sua privacidade, ideal se não confiar na sua rede (Wi-Fi pública, por exemplo).
- Desvantagem**: Pode tornar a aplicação mais lenta devido à encriptação.
- Recomendação**: Ativar o Tor se a confidencialidade for uma prioridade, mas testar a velocidade da ligação.



#### 3.2.3. Ligação a um nó pessoal





- Função**: Liga a aplicação ao seu próprio **nó Bitcoin completo** através de um **servidor Electrum**.
- Porquê?**: Proporciona um controlo total sobre os dados Blockchain, eliminando a dependência dos servidores Blockstream.
- Pré-requisito**: Um nó Bitcoin configurado.
- Recomendação**: Utilizadores avançados que pretendem o máximo de soberania.



#### 3.2.4. Verificação do SPV





- Função**: Utiliza a **Verificação de pagamento simplificada (SPV)** para verificar diretamente determinados dados do Blockchain sem descarregar toda a cadeia.
- Porquê? Reduz a dependência do nó padrão do Blockstream, mantendo-se leve para dispositivos móveis.
- Desvantagem**: Menos seguro do que um Full node, pois depende de nós de terceiros para algumas informações.
- Recomendação**: Ativar o SPV se não puder utilizar um nó pessoal, mas preferir um Full node para uma segurança óptima.





## 4. Criar uma carteira Bitcoin onchain



### 4.1. Iniciar a criação





- Atenção**: Monte a sua carteira num ambiente privado, sem câmaras ou observadores.
- No ecrã inicial, clique em "Começar" :



![image](assets/fr/04.webp)





- Se quiser gerir um **Cold Wallet** (Wallet offline): clique em **"Connect Jade "** para utilizar o Hardware Wallet Blockstream Jade ou outras carteiras Cold compatíveis.



![image](assets/fr/05.webp)






- Aparece o ecrã seguinte:



![image](assets/fr/06.webp)






- (1) **"Setup Mobile Wallet"** : Criar um novo Hot Wallet (Hot Wallet).
- (2) **"Restore from Backup "**: Importar um portefólio existente utilizando uma frase Mnemonic (12 ou 24 palavras). Aviso: Não importar a frase de um Cold Wallet, pois esta ficará exposta num dispositivo ligado, invalidando a sua segurança.
- (3) **"Watch-Only "**: Importar uma carteira só de leitura existente, para ver o saldo (por exemplo, do seu Cold Wallet) sem expor a frase do Mnemonic. Ver o tutorial "Watch Only" no apêndice.



**Neste tutorial**: Clique em **"Setup Mobile Wallet"** para criar um Hot Wallet.


O seu Wallet é criado automaticamente e a página inicial do Wallet, aqui chamada "My Wallet 5", é exibida:



![image](assets/fr/07.webp)



**Importante**: A Blockstream App simplificou a criação de um Wallet ao não apresentar automaticamente a frase seed de 12 palavras. *Embora a carteira seja agora criada com um clique, corre o risco de perder o acesso aos seus fundos se não guardar a sua frase seed*.



### 4.2. Guardar a frase seed





- No ecrã inicial do Wallet, clique no separador "Security" (Segurança) e, em seguida, no prompt "Back Up" (Cópia de segurança) ou no menu "Recovery Phrase" (Frase de recuperação):



![image](assets/fr/08.webp)



A frase de 12 palavras seed será apresentada para guardar.





- Escreva a sua frase de recuperação com o máximo cuidado. Escreva-a em papel ou metal e guarde-a num local seguro (local seguro e offline). Esta frase é o único meio de aceder aos seus bitcoins em caso de perda do seu dispositivo ou de eliminação da aplicação.
- Também é importante notar que qualquer pessoa com esta frase pode roubar todos os seus bitcoins. Nunca as armazene digitalmente:
 - Sem captura de ecrã
 - Sem cópias de segurança na nuvem, por correio eletrónico ou por mensagens
 - Sem copiar/colar (risco de guardar na área de transferência)



**! Este ponto é crítico**. Para mais informações sobre a cópia de segurança :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Verificar a frase seed



Antes de enviar fundos para um Address associado a esta frase seed, deve testar o backup das suas 12 palavras.


Para o fazer, vamos escrever uma referência, eliminar o Wallet, restaurá-lo com a cópia de segurança e verificar se a referência se mantém inalterada.





- No ecrã inicial do Wallet, clique no separador "Settings" (Definições), depois em "Wallet Details" (Detalhes do Wallet) e copie a zPub ([extended public key](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f):



![image](assets/fr/09.webp)



Nota: um zpub Address pode ser importado para a sua aplicação Blockstream para a função "Watch Only" (ver Apêndice).





- Apague a aplicação, depois restaure o Wallet através de **"Restore from Backup "** introduzindo a frase Mnemonic e verifique se o zpub se mantém inalterado. Em caso afirmativo, a sua cópia de segurança está correta e pode enviar fundos para o Wallet.





- Para saber mais sobre como efetuar um teste de recuperação, aqui está um tutorial dedicado :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Garantir o acesso à aplicação



Bloquear o acesso à aplicação com um código PIN forte:




- No ecrã inicial do Wallet, aceda a **"Security "** e clique em **"PIN "**
- Introduzir e confirmar **um código PIN aleatório de 6 dígitos**.



**Opção biométrica**: Disponível para maior comodidade, mas menos segura do que um código PIN robusto (risco de acesso não autorizado, por exemplo, digitalização da impressão digital ou do rosto durante o sono).



**Nota**: O PIN protege o dispositivo, mas apenas a frase seed pode ser utilizada para recuperar fundos.





## 5. Utilizar o Liquid Wallet



### 5.1. Receber bitcoins "L-BTC



Para receber Liquid-Bitcoins (L-BTC), existem várias opções disponíveis. Pode pedir a alguém que lhe envie algumas diretamente, partilhando um Liquid que receba Address, como se explica a seguir.



Em alternativa, Exchange os seus bitcoins onchain ou através do Lightning Network para L-BTC usando [uma ponte como Boltz](https://boltz.Exchange/): introduza o seu Liquid recebendo Address, faça o pagamento como preferir e receba o seu L-BTC.





- No ecrã inicial da carteira, clique em "**Transacionar**" e depois em **"Receber "**.



![image](assets/fr/19.webp)





- Por defeito, a aplicação apresenta um **recibo Address, onchain** em branco (formato SegWit v0, começando por `bc1q...`). Clicar em "Bitcoin" para selecionar **Liquid Bitcoin** :



![image](assets/fr/20.webp)





- Opções** :
 - (1) Clicar nas setas para selecionar outro novo Address ligado a esta frase seed.
    - (2) Também pode escolher um Address de entre os já utilizados/apresentados, clicando nos três pontos no canto superior direito e depois em "Lista de endereços"
    - (3) Para solicitar um montante específico, clicar nos três pontos no canto superior direito, selecionar "Request amount" e introduzir o montante pretendido. O QR será atualizado e o Address será substituído por um URI de pagamento Bitcoin.



![image](assets/fr/21.webp)





- Partilhe o Address/URI clicando em "**Partilhar**", copiando o texto ou digitalizando o código QR.
- Verificação**: Verificar o Address partilhado com o destinatário, na medida do possível, para evitar erros ou ataques (por exemplo, malware que modifica a área de transferência).



### 5.2. enviar bitcoins





- No ecrã inicial da carteira, clique em "**Transação**" e depois em **"Enviar "** :



![image](assets/fr/22.webp)





- Introduzir dados** :
    - (1) Introduzir o **Address do destinatário** colando-o ou digitalizando um código QR.
    - (2) Verificar os activos e a conta a partir da qual os fundos são enviados.
    - (3) Indicar o **montante** a enviar. Pode escolher a unidade: L-BTC, L-satoshis, USD, ...



![image](assets/fr/23.webp)





- Verificação** :
    - Verificar o Address, o montante e os encargos no ecrã de resumo.
    - Um erro Address pode resultar numa perda irreversível de fundos. Cuidado com o malware que modifica a área de transferência.



![image](assets/fr/24.webp)





- Confirmação**: Deslize o botão "Enviar" para assinar e distribuir a transação.
- Seguimento**: No separador "Transact" (Transação) do Wallet, a transação aparece como "Unconfirmed" (Não confirmada), depois "Confirmed" (Confirmada) e depois "Completed" (Concluída):



![image](assets/fr/25.webp)





- O tempo entre 2 blocos é de 1 minuto no Liquid, pelo que a transação é rapidamente confirmada e concluída.




## Apêndices



### A1. Outros tutoriais da aplicação Blockstream



Utilizar a rede Onchain



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Importação e seguimento de um Wallet no modo "Watch Only



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Versão para computador



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Melhores práticas



Para utilizar a **Blockstream App** de forma segura e eficiente, siga estas recomendações. Estas irão ajudá-lo a proteger os seus fundos, a otimizar as suas transacções e a preservar a sua confidencialidade nas redes **Bitcoin (onchain)**, **Liquid** e **Lightning**.





- Proteja a sua frase de recuperação** :
 - Tutorial: Salvando sua frase do Mnemonic



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Utilizar autenticação segura** :
 - Ativar um **PIN forte** ou **autenticação biométrica** (impressão digital ou reconhecimento facial) para proteger o acesso à aplicação.
 - Nunca partilhe o seu PIN ou dados biométricos.





- Proteger a sua privacidade** :
 - generate um novo Address para cada receção em cadeia ou Liquid para limitar o rastreio no Blockchain.
 - Ativar as funções "Enhanced Privacy", "Tor" e "SPV".
 - Para obter a máxima confidencialidade, ligue o seu Wallet ao seu próprio nó Bitcoin através de um servidor Electrum em vez de utilizar o nó público





- Escolha a rede mais adequada às suas necessidades** :
 - Onchain**: Preferido para custódia a longo prazo ou transacções de grande valor (taxas insignificantes em relação ao montante).
 - Liquid**: Utilizar para transferências rápidas e económicas com maior confidencialidade.
 - Relâmpago**: Escolha transferências instantâneas e de baixo custo para pequenos montantes.





- Verificar sempre os endereços de envio** :
 - Antes de enviar fundos, verifique cuidadosamente o Address. Os fundos enviados para um Address incorreto perdem-se para sempre. Utilize copiar/colar ou a leitura de código QR, nunca copie/altere um Address à mão.





- Otimizar os custos** :
 - Para transacções onchain, escolha taxas adequadas (lentas, médias, rápidas) de acordo com a urgência e o congestionamento da rede.
 - Utilizar Liquid, ou Lightning para pequenas quantidades.





- Manter a aplicação actualizada




### A3. Recursos adicionais





- Ligações oficiais:**
 - [Sítio Web oficial](https://blockstream.com/)**
 - [Suporte para a aplicação móvel](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : documentação e chat
 - [GitHub](https://github.com/Blockstream/green_android)**





- Exploradores de blocos :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Relâmpago: **[1ML (Lightning Network)](https://1ml.com/)**





- Aprendizagem e tutoriais:** **[Plan ₿ Network](https://planb.network/)** :
 - Proteger a sua frase de recuperação



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Glossário](https://planb.network/fr/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Glossário](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
