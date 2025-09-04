---
name: BIP-85
description: Como posso utilizar o BIP-85 para generate várias frases-semente de um seed principal?
---
![cover](assets/cover.webp)



## 1. Compreender o BIP-85



### 1.1 O que é o BIP-85?



BIP-85 é uma função avançada que permite criar várias **frases secundárias seed** a partir de uma **frase principal seed**.



Cada frase secundária seed pode ser utilizada para criar uma carteira Bitcoin completamente independente. Estas carteiras podem ser utilizadas para diversos fins: uma Hot Wallet no telemóvel, uma carteira para um familiar, uma carteira de poupança separada, etc.



Todas as subfrases do seed são **derivadas matematicamente**, mas é **impossível remontar à frase principal do seed** a partir de uma subfrase. Isto assegura uma separação completa entre cada carteira.



Desde que tenha acesso à sua frase principal do seed (e ao passphrase associado, se estiver a usar um), pode regenerar qualquer frase secundária do seed **idêntica**, sem ter de a guardar separadamente.



### 1.2 Porquê utilizar o BIP-85?



O BIP-85 é útil se pretender :





- Criar vários portefólios Bitcoin independentes sem várias cópias de segurança
- Gerir os seus fundos de acordo com diferentes utilizações (poupança, despesas, família, projectos)
- Garantir a proteção dos familiares (função "Uncle Jim")
- Eliminar uma carteira sem perder o acesso aos seus fundos
- Simplifique a sua segurança: apenas uma frase-chave seed para proteger



### 1.3 Vantagens em relação ao BIP-32



Com o BIP-32, uma única frase seed pode ser usada para generate uma hierarquia completa de contas e endereços Bitcoin, usando caminhos de derivação (por exemplo: `m/44'/0'/0'/0/0`). Cada caminho pode representar uma conta separada, mas **todos permanecem ligados à mesma frase seed**. Assim, se esta frase seed for comprometida, **todas as contas derivadas ficam acessíveis**.



Com o BIP-85, uma frase principal seed pode ser utilizada para generate várias frases secundárias seed totalmente independentes: **Se uma destas sementes secundárias for comprometida, o atacante nunca poderá voltar ao seed principal ou aceder às outras carteiras**.


Isto permite compartimentar os riscos:





- Pode utilizar um seed secundário para Hot Wallet ou para utilização temporária, aceitando uma exposição mais elevada.
- Mesmo que este Hot Wallet seja comprometido, os seus outros fundos, protegidos por outras sementes secundárias ou mantidos offline, **permanecem seguros**.



Por outro lado, tanto para o BIP-32 como para o BIP-85, se o seed principal for comprometido, **todos os fundos ficam vulneráveis**. Por conseguinte, é crucial protegê-lo com o mais alto nível de segurança.



![image](assets/fr/02.webp)


## 2. Casos práticos de utilização da BIP-85



O BIP-85 permite-lhe criar várias carteiras Bitcoin a partir de uma única frase principal seed, cada uma com a sua própria frase secundária seed. Aqui estão cinco casos práticos de utilização para organizar e proteger os seus fundos Bitcoin. Cada caso explica por que razão utilizar o BIP-85 é mais prático do que gerir várias contas com uma única frase seed através do BIP-32.



### 2.1 Limitar o risco de uma carteira menos segura





- Cenário**: Utiliza um "Hot Wallet" Wallet (instalado num dispositivo ligado à Internet), para transacções diárias.
- Solução BIP-85**: Cria-se uma frase secundária seed dedicada a esta carteira.
- Vantagem em relação ao BIP-32**: Não precisa de importar a frase primária do seed para o seu telemóvel, reduzindo o risco de pirataria. Apenas a frase secundária do seed é comprometida, protegendo as suas outras carteiras. Com o BIP-32, é necessário utilizar a frase principal do seed e um caminho de desvio, expondo todos os seus fundos.



### 2.2 Criar um portefólio para um membro da família





- Cenário**: Configura um Bitcoin Wallet para alguém que lhe é próximo (por exemplo, a sua mãe), podendo recuperá-lo se a pessoa o perder.
- Solução BIP-85**: Cria-se uma frase secundária seed dedicada e partilha-se apenas esta.
- Vantagem em relação ao BIP-32**: Com o BIP-32, a criação de uma conta para um ente querido requer a partilha da sua frase principal do seed, arriscando todos os seus fundos e complicando a gestão para o seu ente querido (gestão de caminhos de ramificação), ou a criação de uma nova frase do seed para guardar para além da sua frase principal do seed.



### 2.3 Facilitar a gestão de carteiras separadas





- Cenário**: Separa os seus bitcoins para diferentes fins (por exemplo, poupanças a longo prazo, fundos não-KYC).
- Solução BIP-85**: Criar seed frases secundárias dedicadas a cada objetivo.
- Vantagem em relação ao BIP-32**: Com o BIP-32, todas as contas partilham a mesma frase seed, o que complica a gestão em carteiras de terceiros, exigindo a gestão de caminhos de derivação como `m/44'/0'/0'`. Além disso, não é possível atribuir uma conta separada por dispositivo (por exemplo, "poupanças no Coldcard", "diário no telemóvel", "férias no Trezor"). O BIP-85 atribui uma frase secundária seed única por objetivo, que é fácil de identificar e importar separadamente em cada dispositivo.



### 2.4 Utilizar um Wallet temporário para transacções





- Cenário**: Necessita de uma carteira temporária para uma transação única ou para preservar a confidencialidade (por exemplo: mistura de fundos, interação com um Exchange KYC, etc.).
- Solução BIP-85**: Cria-se uma frase secundária seed, utiliza-se para a transação e, se necessário, destrói-a, sabendo que pode ser regenerada.
- Vantagem em relação ao BIP-32**: Com o BIP-32, uma conta temporária depende da frase principal do seed, expondo todos os seus fundos se forem comprometidos.





## 3. Antes de começar





- Hardware** (opcional)
 - Coldcard Mk4 ou Q1
 - Cartão microSD





- Conhecimentos básicos
 - Compreender as frases Mnemonic (BIP-39): uma lista de 12 a 24 palavras para guardar uma carteira.
 - Saiba o que é um Bitcoin Wallet: software ou dispositivo para gerir os seus bitcoins, e como restaurá-lo com uma frase Mnemonic.
 - Mais recursos nos anexos.





- Software compatível**
 - Sparrow wallet (computador, para gestão apenas de vigilância ou avançada)
 - Nunchuck (móvel, para assinaturas múltiplas)
 - BlueWallet (telemóvel)
 - ...





- 3.4 Configuração Coldcard**
 - Inicializar uma frase seed de 24 palavras no Coldcard.
 - Opcional: Adicionar um passphrase para proteger o acesso aos ramos BIP-85.
 - Ativar opções úteis: NFC (para exportação), desativar USB na bateria (segurança).




## 4. Tutorial passo-a-passo



Siga estes passos para criar, utilizar e recuperar um Mnemonic secundário com BIP-85 no seu Coldcard.



### 4.1 generate a seed frase secundária



Criará uma frase secundária seed a partir da sua frase principal seed.


Ligue o seu Coldcard e introduza o seu código PIN.





- 1. Se tiver aplicado um passphrase ao seu seed principal:**
 - No ecrã inicial, vá para `passphrase`.
    - Escolha `Adicionar palavra` e introduza a sua palavra-passe.
    - Prima "Aplicar".
    - Verifique a identidade do Wallet: Aceda a `Advanced > View Identity` para anotar a impressão digital do Wallet.





- 2. Aceder ao menu BIP-85**
 - No ecrã inicial, vá para `Avançadas > Derivar seed B85`
 - Ler o aviso e confirmar.



O ColdCard informa-o de que as sementes geradas são matematicamente derivadas do seu seed principal, mas criptograficamente totalmente independentes.


![image](assets/fr/03.webp)





- 3. Selecionar um formato


Selecione o formato da frase seed: 12, 18 ou 24 palavras. Verifique o número de palavras aceites pelo Wallet para o qual pretende importar a sua frase seed.


![image](assets/fr/04.webp)





- 4. Selecionar índice
 - Introduzir um índice entre 0 e 9999.
 - Este índice é crucial para regenerar o seed secundário numa data posterior. Guarde-o cuidadosamente com uma etiqueta como: "Índice 1 = Wallet móvel", "Índice 2 = projeto familiar", "Índice 4 = mistura de teste", ...
 - Se o perder, não perderá o acesso aos seus fundos, mas terá de testar combinações de 0 a 9999 para os encontrar.


![image](assets/fr/05.webp)





- 5. Anotar ou exportar a frase secundária do seed**


ColdCard apresenta agora uma nova frase secundária seed. Pode :




 - A **nota manual**.
 - Imprensa :
     - 1` para o guardar no cartão SD
     - `2` para **entrar no modo "use this seed"** no ColdCard (útil para exportar ou assinar uma transação)
     - 3` para apresentar um **código QR** (para ser lido com uma aplicação móvel como a BlueWallet ou a Nunchuck)
     - 4` para o enviar por **NFC**



nesta altura, tens uma frase seed independente, utilizável em qualquer Wallet BIP39 (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Utilizar o seed secundário



Pode agora utilizar este seed derivado para criar uma nova carteira no :




- uma aplicação móvel
- outro Hardware Wallet
- uma carteira Multisig



### 4.3 Recuperar uma frase secundária perdida do seed



Para recuperar um seed secundário em qualquer altura, repita o processo:


1. Reiniciar o ColdCard


2. Introduzir o seu PIN


3. Introduza o seu passphrase, se definido


4. Aceder a `Avançadas > Derivar seed B85`


5. Escolher o formato (12/18/24 palavras)


6. Introduzir o mesmo índice (por exemplo, `1`)


7. Obterá exatamente o mesmo seed secundário




## 5. Limites, riscos e melhores práticas



### 5.1 Dependência da frase principal seed + passphrase



A utilização do BIP85 depende inteiramente da frase principal de 24 palavras seed, bem como da passphrase, se a tiver aplicado.




- A partir destas duas Elements, todas as frases secundárias seed podem ser regeneradas.
- Sem um destes 2 Elements, perde-se o acesso a todas as carteiras de derivados.



### 5.2 Riscos na configuração de assinaturas múltiplas



Desaconselhamos vivamente a utilização de frases seed secundárias geradas a partir da mesma frase seed primária numa configuração multi-sig: se o dispositivo ou a frase seed primária estiver comprometida, todas as chaves multi-sig podem ser regeneradas por um atacante.



### 5.3 Compatibilidade do software



Nem todas as aplicações suportam diretamente a derivação BIP85. No entanto, as sementes geradas através da BIP85 são sementes padrão da BIP39 (12, 18 ou 24 palavras), pelo que podem ser utilizadas em qualquer carteira compatível com a BIP39.



### 5.4 Registo de conta BIP85



Recomenda-se a manutenção de um registo pessoal atualizado das frases secundárias do seed.




- Permite-lhe descobrir rapidamente qual o índice BIP85 que corresponde a cada carteira, sem ter de manter frases secundárias seed.
- Este registo deve ser minimalista, sem menção explícita ao Bitcoin, e deve ser guardado separadamente do seed principal. Não se esqueça de o mencionar no seu plano de herança.



O registo pode conter :




- índice bIP85 utilizado (número de 0 a 9999)
- um nome de utilização ou de referência (por exemplo, Hot Wallet, poupanças pessoais, Wallet da mãe)
- se necessário, a impressão digital Wallet para verificação no ColdCard



### 5.5 Apoio



As cópias de segurança devem incluir :




- a principal seed
- gW-76 (se utilizado)



Nunca guardar em conjunto:




- os principais seed e passphrase
- o seed principal e o registo de conta BIP85



Mais recursos nos anexos.




## APÊNDICES



## A.1 Glossário





- [BEEP] (https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39] (https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [frase seed] (https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)




### A.2 Guardar a frase de recuperação



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Compreender o passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Como funcionam os portefólios Bitcoin



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f