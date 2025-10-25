---
name: Blockstream App - Watch-Only
description: Como é que configuro um Watch-only wallet na aplicação Blockstream?
---

![cover](assets/cover.webp)


## 1. Introdução


### 1.1 Objetivo do tutorial





- Este tutorial explica como configurar e utilizar a funcionalidade **Watch-Only** da aplicação móvel **Blockstream App** para monitorizar um Bitcoin Wallet sem aceder às suas chaves privadas.
- Abrange a instalação, a configuração inicial, a importação de uma chave pública alargada e a sua utilização para controlar saldos e endereços de receção generate.
- Nota: Outros tutoriais, fornecidos no apêndice, cobrem Onchain, Liquid e a versão desktop.



### 1.2. Público-alvo





- **Iniciantes**: Utilizadores que pretendem monitorizar uma carteira Bitcoin (frequentemente associada a um Hardware Wallet) através de uma aplicação móvel intuitiva.
- **Utilizadores intermédios**: Pessoas que procuram gerir carteiras só de leitura enquanto utilizam opções de privacidade como Tor ou SPV.
- **Proprietários de Hardware Wallet**: Para verificar os seus saldos e endereços generate sem ligar o seu dispositivo.
- **Empresas e lojas**:
 - Acompanhe as suas transacções para fins contabilísticos sem expor as suas chaves privadas.
 - Verificar as transacções recebidas sem introduzir as suas chaves privadas nos sistemas de pagamento em linha.
 - Permitir que os funcionários façam o generate de novos endereços de receção sem ter acesso a chaves privadas.
- **Organizações e financiamento coletivo**: Apresentar o saldo de forma transparente aos doadores sem permitir o acesso aos fundos.



### 1.3. Introdução ao Watch-Only



Um **Watch-Only** Wallet permite-lhe monitorizar as transacções e o saldo de um Bitcoin Wallet sem ter acesso às chaves privadas. Ao contrário de um Wallet convencional, ele armazena apenas dados públicos, como a **chave pública estendida** (que deu origem ao "**xpub**", depois ao "zpub", "ypub", etc.), o que lhe permite obter endereços de receção e seguir o histórico de transacções no Blockchain Bitcoin. A ausência de chaves privadas torna impossível o desembolso de fundos a partir da aplicação, garantindo uma segurança reforçada.



![image](assets/fr/10.webp)



**Porquê usar um Watch-only wallet?**





- **Segurança**: Ideal para monitorizar uma carteira protegida por um **Hardware Wallet** sem expor as chaves privadas de um dispositivo ligado.
- **Conveniência**: Permite-lhe verificar o saldo e os novos endereços de destinatários do generate sem ligar o Hardware Wallet.
- **Confidencialidade**: Compatível com opções como **Tor** ou **SPV** para limitar a dependência de servidores de terceiros.
- **Casos de utilização**: Acompanhamento de fundos em movimento, geração de endereços para receber pagamentos ou verificação de transacções sem arriscar chaves privadas.



![image](assets/fr/01.webp)



### 1.4. Chaves públicas alargadas



Uma **chave pública alargada** (xpub, ypub, zpub, etc.) é um dado derivado de um Bitcoin Wallet que gera todas as chaves públicas secundárias e os seus endereços de receção associados, sem dar acesso às chaves privadas.





- **Como funciona**: A chave pública alargada é gerada a partir da frase seed através de um processo determinístico (BIP-32). Cria uma árvore hierárquica de chaves públicas filhas, cada uma das quais pode ser convertida numa Address recebida. Utilizando o mesmo caminho de derivação (por exemplo, `m/44'/0'/0'`) que o Wallet vigiado, o Watch-only wallet gera os mesmos endereços, permitindo o rastreio de fundos e a criação de novos endereços de receção.



![image](assets/fr/11.webp)





- Tipos de chaves públicas alargadas
- **xpub**: Utilizado para carteiras Legacy (endereços que começam por "1", BIP-44) e carteiras Taproot (endereços que começam por "bc1p", BIP-86).
- **ypub**: Concebido para carteiras SegWit compatíveis (endereços começados por "3", BIP-49).
- **zpub**: Associado a carteiras nativas SegWit (endereços que começam por "bc1q", BIP-84).
- **Outros (tpub, upub, vpub, etc.)**: Utilizado para redes alternativas (como a Testnet) ou normas específicas. Por exemplo, tpub é para a rede Testnet.





- **Distinção**: A escolha entre xpub, ypub ou zpub depende do tipo de Address (legacy, SegWit, Taproot ou nested SegWit) e da norma BIP utilizada pelo Wallet. Verifique o formato exigido pelo seu portefólio de origem para garantir a compatibilidade com a aplicação Blockstream.





- **Segurança e confidencialidade**: A chave pública alargada não é sensível em termos de segurança, uma vez que não permite que os fundos sejam gastos (sem acesso a chaves privadas). No entanto, é sensível em termos de confidencialidade, uma vez que revela todos os endereços públicos e o historial de transacções associado.



**Recomendação**: Proteja a sua chave pública alargada como informação sensível.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Lembrete Hot Wallet





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: todos os nomes para uma aplicação instalada num smartphone, computador ou qualquer dispositivo ligado à Internet, que permite gerir e proteger as chaves privadas de um Bitcoin Wallet.
- Ao contrário das **carteiras de hardware**, também conhecidas como **carteiras Cold**, que isolam as chaves offline, as carteiras de software funcionam num ambiente ligado, o que as torna mais vulneráveis a ciberataques.





- **Utilização recomendada**:
    - Ideal para gerir quantidades moderadas de Bitcoin, especialmente para transacções diárias.
    - Adequado para principiantes ou utilizadores com recursos limitados, para os quais um Hardware Wallet pode parecer supérfluo.





- **Limitações**: Menos seguro para guardar fundos avultados ou poupanças a longo prazo. Neste caso, opte por um Hardware Wallet.




## 2. Apresentação da aplicação Blockstream





- A **Blockstream App** é uma aplicação móvel (iOS, Android) e de ambiente de trabalho para gerir as carteiras Bitcoin e os activos no Liquid Network. Adquirida pela [Blockstream] (https://blockstream.com/) em 2016, foi anteriormente designada *Green Address* e depois *Blockstream Green*.
- **Características principais**:
- **Transacções Onchain** em Blockchain Bitcoin.
    - Transacções na rede **Liquid** (Sidechain para trocas rápidas e confidenciais).
- **Carteiras só de observação** para monitorizar fundos sem acesso a chaves.
    - Opções de privacidade: ligação através de **Tor**, ligação a um **nó pessoal** através de Electrum, ou verificação **SPV** para reduzir a dependência de nós de terceiros.
    - Funções **Replace-by-fee (RBF)** para acelerar as transacções não confirmadas.
- **Compatibilidade**: Integra carteiras de hardware como **Blockstream Jade**.
- **Interface**: Intuitivo para principiantes, com opções avançadas para especialistas.
- **Nota**: Este guia centra-se na utilização do Onchain. Outros tutoriais nos Apêndices abrangem Onchain, Watch-Only e a versão para computador.




## 3. Instalar e configurar a aplicação Blockstream



### 3.1. descarregar





- Para **Android**:
    - Descarregue [Blockstream App] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) a partir da Google Play Store.
    - Alternativa: Instalar através do ficheiro APK disponível no [GitHub oficial da Blockstream](https://github.com/Blockstream/green_android).
- Para **iOS**:
    - Descarregar [Blockstream App] (https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) da App Store.
- **Nota**: Certifique-se de que descarrega a partir de fontes oficiais para evitar aplicações fraudulentas.



### 3.2. configuração inicial





- **Ecrã inicial**: Quando aberta pela primeira vez, a aplicação apresenta um ecrã sem um Wallet configurado. As carteiras criadas ou importadas aparecerão aqui mais tarde.



![image](assets/fr/02.webp)





- **Personalizar definições**: Clique em "Definições da aplicação", ajuste as opções abaixo, clique em "Guardar", reinicie a aplicação e crie a sua carteira.



![image](assets/fr/03.webp)



#### 3.2.1. Privacidade melhorada (apenas Android)





- **Função**: Desactiva as capturas de ecrã, oculta as pré-visualizações de aplicações no gestor de tarefas e bloqueia o acesso quando o telemóvel está bloqueado.
- Porquê? Protege os seus dados contra acesso físico não autorizado ou malware de captura de ecrã.



#### 3.2.2. Ligação via Tor





- **Função**: Encaminhar o tráfego de rede através do **Tor**, uma rede anónima que encripta as suas ligações.
- **Porquê?**: Oculte o seu IP Address e proteja a sua privacidade, ideal se não confiar na sua rede (Wi-Fi pública, por exemplo).
- **Desvantagem**: Pode tornar a aplicação mais lenta devido à encriptação.
- **Recomendação**: Ativar o Tor se a confidencialidade for uma prioridade, mas testar a velocidade da ligação.



#### 3.2.3. Ligação a um nó pessoal





- **Função**: Liga a aplicação ao seu próprio **nó Bitcoin completo** através de um **servidor Electrum**.
- **Porquê?**: Proporciona um controlo total sobre os dados do Blockchain, eliminando a dependência dos servidores Blockstream.
- **Pré-requisito**: Um nó Bitcoin configurado.
- **Recomendação**: Utilizadores avançados que pretendem o máximo de soberania.



#### 3.2.4. Verificação do SPV





- **Função**: Utiliza a **Verificação de pagamento simplificada (SPV)** para verificar diretamente determinados dados do Blockchain sem descarregar toda a cadeia.
- Porquê? Reduz a dependência do nó padrão do Blockstream, mantendo-se leve para dispositivos móveis.
- **Desvantagem**: Menos seguro do que um Full node, pois depende de nós de terceiros para algumas informações.
- **Recomendação**: Ativar o SPV se não puder utilizar um nó pessoal, mas preferir um Full node para uma segurança óptima.





## 4. Criar uma carteira "Watch-only" Bitcoin



### 4.1. Recuperar a chave pública alargada



Para configurar um Watch-only wallet, é necessário obter primeiro a chave pública alargada (xpub, ypub, zpub, etc.) do Wallet a monitorizar. Esta informação está geralmente disponível nas definições ou na secção "Informações Wallet" do seu software ou Hardware Wallet.





- Exemplo com a aplicação Blockstream: No ecrã inicial do Wallet, vá a "Settings" (Definições), depois a "Wallet Details" (Detalhes do Wallet) e copie o ficheiro zpub :



![image](assets/fr/09.webp)





- Alternativa 1: generate um código QR que contém a chave pública alargada para ser digitalizada na etapa seguinte.
- Alternativa 2: Utilizar um output descriptor se o seu Wallet o fornecer.



### 4.2. importar Wallet Watch-only





- **Atenção**: Monte a sua carteira num ambiente privado, sem câmaras ou observadores.
- No ecrã inicial, clique em "Criar uma nova carteira" e, em seguida, em "Começar":



![image](assets/fr/04.webp)





- Aparece o ecrã seguinte:



![image](assets/fr/06.webp)






- (1) **"Setup Mobile Wallet"** : Criar um novo Hot Wallet. Ver o tutorial "Blockstream App - Onchain" no apêndice.
- (2) **"Restore from Backup "**: Importar um portefólio existente utilizando uma frase Mnemonic (12 ou 24 palavras). Atenção: Não importar a frase de um Cold Wallet, pois ela ficará exposta num dispositivo conectado, invalidando sua segurança.
- (3) **"Watch-Only "**: a opção que nos interessa para este tutorial.





- Em seguida, selecionar "**Assinatura única**" e a rede "**Bitcoin**":



![image](assets/fr/12.webp)





- Colar a chave pública alargada (xpub, ypub, zpub, etc.), digitalizar o código QR correspondente ou introduzir um output descriptor. Mesmo que a aplicação indique "xpub", as chaves ypub, zpub, etc. são igualmente autorizadas. Em seguida, clique em "Ligar":



![image](assets/fr/13.webp)




### 4.3. Utilizar o Wallet Apenas para observação



Uma vez importado, o Watch-only wallet apresenta o saldo total e o histórico de transacções dos endereços derivados da chave pública alargada. Apenas as transacções onchain são visíveis (as transacções Liquid são ignoradas). Para monitorizar um Liquid Wallet, repita a importação selecionando "Liquid" no passo anterior.





- **Ver o saldo e o histórico**: a partir do ecrã inicial, ver o saldo total e o histórico de transacções onchain:



![image](assets/fr/14.webp)





- generate um Address recetor: Clicar em "Transact" e depois em "Receive" para criar um novo Address onchain. Partilhe-o através do código QR ou copie-o para receber fundos:



![image](assets/fr/15.webp)





- **Enviar fundos**: Clicar em **"Transacionar"** e depois em **"Enviar"**. Pode introduzir:
 - O Address do destinatário.
 - O montante da transação.
 - Taxas de transação.



No entanto, como o Watch-only wallet não possui as chaves privadas, não é possível enviar fundos diretamente. Para assinar a transação, ligue os seus PSBT Hardware Wallet ou Exchange digitalizando os códigos QR (uma opção disponível no Coldcard Q, por exemplo).



![image](assets/fr/16.webp)





- **Nota**: Verifique sempre o Address de receção e os detalhes da transação para evitar erros. Os fundos enviados para o Address errado não podem ser recuperados.




## Apêndices



### A1. Outros tutoriais da aplicação Blockstream





- Utilizar a rede Onchain :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Utilização do Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Versão para computador :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Chaves públicas alargadas





- Glossário :
 - [Chaves públicas alargadas](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Curso :
 - [Les clés publiques étendues](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3. Melhores práticas



Para utilizar a **Blockstream App** de forma segura e eficiente, siga estas recomendações. Estas irão ajudá-lo a proteger os seus fundos, otimizar as suas transacções e preservar a sua confidencialidade nas redes **Bitcoin (onchain)**, **Liquid** e **Lightning**.





- **Proteja a sua frase de recuperação**:
 - Tutorial: Guardar a sua frase Mnemonic



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Utilizar autenticação segura**:
 - Ativar um **PIN forte** ou **autenticação biométrica** (impressão digital ou reconhecimento facial) para proteger o acesso à aplicação.
 - Nunca partilhe o seu PIN ou dados biométricos.





- **Proteger a sua privacidade**:
 - generate um novo Address para cada receção onchain ou Liquid para limitar o rastreio no Blockchain.
 - Ativar as funções "Enhanced Privacy", "Tor" e "SPV".
 - Para máxima confidencialidade, ligue o seu Wallet ao seu próprio nó Bitcoin através de um servidor Electrum em vez de usar o nó público





- **Escolha a rede mais adequada às suas necessidades**:
- **Onchain**: Preferido para custódia a longo prazo ou transacções de grande valor (taxas insignificantes em relação ao montante).
- **Liquid**: Utilizar para transferências rápidas e económicas com maior confidencialidade.
- **Relâmpago**: Escolha transferências instantâneas e de baixo custo para pequenos montantes.





- **Verificar sempre os endereços de envio**:
 - Antes de enviar fundos, verifique cuidadosamente o Address. Os fundos enviados para um Address incorreto perdem-se para sempre. Utilize copiar/colar ou a leitura do código QR, nunca copie/altere um Address à mão.





- **Otimizar os custos**:
 - Para transacções onchain, escolha taxas adequadas (lentas, médias, rápidas) de acordo com a urgência e o congestionamento da rede.
 - Utilizar Liquid, ou Lightning para pequenas quantidades.





- Manter a aplicação actualizada




### A4. Recursos adicionais





- **Ligações oficiais da Blockstream:**
- [Sítio Web oficial](https://blockstream.com/)
- [Suporte para a aplicação móvel](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): documentação e chat
- [GitHub](https://github.com/Blockstream/green_android)





- Exploradores de blocos :**
 - Onchain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Relâmpago: **[1ML (Lightning Network)](https://1ml.com/)**





- Aprendizagem e tutoriais: **[Plan ₿ Network](https://planb.network/)**
  - Proteger a sua frase de recuperação



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Glossário](https://planb.network/fr/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Glossário](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb