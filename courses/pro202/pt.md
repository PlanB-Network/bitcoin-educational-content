---
name: Programação Bitcoin
goal: Construir uma biblioteca Bitcoin completa a partir do zero e compreender os fundamentos criptográficos do Bitcoin
objectives: 

 - Implementar aritmética de campos finitos e operações de curvas elípticas em Python
 - Construir e analisar transacções Bitcoin de forma programática
 - Criar endereços testnet e transmitir transacções através da rede
 - Dominar os fundamentos matemáticos subjacentes ao modelo de segurança do Bitcoin

---
# Uma viagem aos guiões e programas do Bitcoin


Este curso intensivo de dois dias, ministrado por Jimmy Song, leva-o a aprofundar os fundamentos técnicos do Bitcoin, construindo uma biblioteca Bitcoin completa a partir do zero. Começando com a matemática essencial de campos finitos e curvas elípticas, você irá progredir através da análise de transações, execução de scripts e comunicação de rede. Através de exercícios práticos de codificação em notebooks Jupyter, você criará seu próprio endereço de testnet, construirá transações manualmente e as transmitirá diretamente para a rede - tudo isso enquanto obtém uma profunda compreensão dos princípios criptográficos que tornam o Bitcoin seguro e sem confiança.


Boa viagem!

Nota: Os vídeos deste curso estão disponíveis apenas em inglês.

+++

# Introdução


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Visão geral do curso


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Bem-vindo ao curso PRO 202 _**Programação do Bitcoin**_, uma viagem intensiva que o leva da aritmética de campos finitos até à construção e transmissão de transacções reais no Bitcoin do Testnet.


Neste curso, irá construir progressivamente uma biblioteca Bitcoin em Python enquanto adquire os fundamentos criptográficos, de protocolo e de software necessários para raciocinar com precisão sobre a segurança e o funcionamento interno do Bitcoin. A abordagem do PRO 202 é totalmente prática: cada conceito é imediatamente implementado em notebooks Jupyter, garantindo que a teoria e o código se fortaleçam mutuamente.


### Conceitos matemáticos essenciais para o Bitcoin


Esta primeira secção estabelece as bases matemáticas indispensáveis. Irá implementar aritmética de campos finitos e operações de curvas elípticas (lei de grupo, adição, duplicação, multiplicação escalar...) - os pré-requisitos para ECDSA. O objetivo é duplo: compreender a estrutura algébrica que torna possíveis as assinaturas criptográficas e construir ferramentas Python fiáveis para as manipular.


Em seguida, formalizará os componentes do ECDSA: geração de chaves, formatação de pontos, hashing, criação de assinaturas e verificação. Esta secção liga diretamente a teoria à prática, dando ênfase aos detalhes de implementação e à robustez do modelo de segurança subjacente.


### Funcionamento interno da transação Bitcoin


Na segunda secção, irá dissecar a estrutura de uma transação Bitcoin: UTXOs, entradas/saídas, sequências, scripts, codificações e muito mais. Escreverá código para construir, assinar e verificar transacções, obtendo uma compreensão precisa do que é comprometido pelo hash e porquê.


Em seguida, implementará um executor _Script_ mínimo, analisará os principais códigos de operação e validará os caminhos de despesa. O objetivo é torná-lo capaz de auditar o comportamento das transacções, diagnosticar falhas de validação e raciocinar sobre a segurança das políticas de despesas.


### Funcionamento interno da rede Bitcoin


Na terceira secção, situará as transacções no âmbito do sistema mais vasto: estrutura dos blocos, cabeçalhos, dificuldade e o mecanismo Proof-of-Work. Lidará com mensagens de protocolo, cabeçalhos de bloco e árvores Merkle.


Por fim, estudará a comunicação entre nós ponto a ponto, a otimização de mensagens e a introdução do SegWit.


Como em todos os cursos sobre o Plan ₿ Academy, a secção final inclui uma avaliação destinada a consolidar a sua compreensão. Pronto para descobrir o funcionamento interno do Bitcoin e escrever o código que o alimenta? Vamos começar!










# Conceitos matemáticos essenciais para o Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matemática para a implementação do Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Fundamentos de programação Bitcoin: Estruturas matemáticas fundamentais


Este curso condensa a matemática essencial por trás dos sistemas criptográficos do Bitcoin num fluxo de trabalho altamente prático. Os conceitos são explicados, demonstrados com exemplos e depois implementados no Jupyter Notebook. A ideia orientadora é simples: só se compreende verdadeiramente uma primitiva criptográfica depois de a codificar. Ao longo da estrutura de dois dias, os alunos generate testnet endereços, construir e transmitir [transações](https://planb.academy/resources/glossary/transaction-tx) e, eventualmente, interagir com a rede sem exploradores de blocos. Tudo isto requer uma base sólida em campos finitos e curvas elípticas.


### Campos finitos: O motor aritmético da criptografia


Um campo finito F(p) é um sistema aritmético definido por um número primo p, contendo elementos de 0 a p-1. Os campos primos garantem que cada elemento diferente de zero tem um inverso e que todas as operações permanecem dentro do campo. A aritmética envolve o uso do módulo p para adição, subtração e multiplicação. O `pow(base, exp, mod)` do Python permite uma exponenciação modular eficiente, crucial para expoentes grandes usados em operações criptográficas reais.


#### Comportamento multiplicativo

A multiplicação de qualquer elemento não nulo k por todos os elementos de um campo primo produz uma permutação do campo. Esta propriedade garante uniformidade e evita fraquezas estruturais, tornando os campos primos ideais para a geração segura de chaves e [assinaturas digitais](https://planb.academy/resources/glossary/digital-signature).


#### Divisão e o pequeno teorema de Fermat

A divisão é efectuada através de inversões multiplicativas. O Pequeno Teorema de Fermat afirma que

n^(p-1) ≡ 1 (mod p),

portanto o inverso é n^(p-2). Python suporta isto diretamente com `pow(n, -1, p)`. Estas operações aparecem constantemente nas rotinas criptográficas subjacentes do [ECDSA](https://planb.academy/resources/glossary/ecdsa) e do Bitcoin.


### Curvas elípticas: Estruturas não lineares para segurança de chaves públicas


As curvas elípticas seguem a equação y² = x³ + ax + b. O Bitcoin utiliza o secp256k1, definido como y² = x³ + 7 num campo finito. Os pontos de uma curva elíptica formam um grupo matemático sob adição de pontos. Uma reta que passa por dois pontos P e Q intersecta a curva num terceiro ponto R; reflectindo R sobre o eixo x, obtém-se P + Q. Este sistema é associativo e inclui um elemento de identidade: o ponto no infinito.


A duplicação de um ponto utiliza uma reta tangente em vez de uma reta secante, com o declive derivado da derivada da curva. Embora estas fórmulas envolvam cálculo sobre números reais, tornam-se totalmente discretas e exactas quando a curva é definida sobre um campo finito - o contexto utilizado no Bitcoin.


### Da matemática à criptografia Bitcoin


Os campos finitos fornecem uma aritmética determinística e invertível; as curvas elípticas fornecem uma estrutura não linear em que calcular k-P é fácil, mas invertê-lo é computacionalmente inviável. A combinação de ambos produz a base para as chaves públicas/privadas do Bitcoin, assinaturas ECDSA e segurança de transacções. A compreensão destes fundamentos prepara os estudantes para implementar chaves, transacções e assinaturas diretamente - sem abstracções ou ferramentas externas.


## Criptografia de curva elíptica

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Este capítulo apresenta as curvas elípticas definidas sobre campos finitos e explica por que razão constituem a espinha dorsal matemática da [criptografia](https://planb.academy/resources/glossary/cryptography) do Bitcoin. Enquanto as curvas elípticas sobre números reais parecem suaves e contínuas, a aplicação das mesmas equações sobre um campo finito cria um conjunto discreto e disperso de pontos. Apesar da diferença visual, todas as fórmulas de adição de pontos, declives e regras algébricas comportam-se exatamente da mesma forma - apenas a aritmética muda para aritmética modular. O Bitcoin utiliza a curva y² = x³ + 7 (secp256k1), que preserva a simetria e o comportamento não linear essencial para a segurança criptográfica.


### Verificação de pontos e implementação de campos finitos


Um ponto encontra-se numa curva elíptica de campo finito se as suas coordenadas satisfazem a equação da curva sob o módulo p. Verificar um ponto como (73,128) em F₁₃₇ requer verificar que y² mod p é igual a x³ + 7 mod p. Implementar isto em código envolve a criação de classes para elementos de campo finito e pontos de curva. A sobrecarga de operadores garante que toda a aritmética - adição, multiplicação, exponenciação, divisão - é automaticamente executada no módulo p. Uma vez que estas abstracções existam, as operações criptográficas mais avançadas tornam-se simples de escrever e de raciocinar.


#### Propriedades de grupo e adição de pontos

Os pontos da curva elíptica formam um grupo matemático sob adição. O grupo satisfaz o fecho, a associatividade, a identidade (o ponto no infinito) e os inversos (reflexão sobre o eixo x). As construções geométricas confirmam estas propriedades, tornando a multiplicação escalar (P adicionado a si mesmo repetidamente) bem definida. Estas regras de grupo permitem a criptografia de curvas elípticas e asseguram um comportamento consistente e previsível sob operações de pontos repetidos.


### Grupos cíclicos e o problema do logaritmo discreto


A escolha de um ponto gerador G numa curva permite-nos gerar generate um grupo cíclico: G, 2G, 3G, ..., nG = 0. Os pontos parecem não lineares e imprevisíveis, mesmo quando gerados sequencialmente. Esta imprevisibilidade cria a base para o problema do logaritmo discreto: calcular P = sG é fácil, mas determinar s a partir de P é computacionalmente inviável para grandes grupos. Esta função unidirecional é o que torna a criptografia de chave pública segura. Os escalares ([chaves privadas](https://planb.academy/resources/glossary/private-key)) são escritos em minúsculas; os pontos ([chaves públicas](https://planb.academy/resources/glossary/public-key)) em maiúsculas.


#### Multiplicação escalar eficiente

Para calcular sG de forma eficiente, as implementações utilizam o algoritmo double-and-add: varrer a representação binária do escalar, duplicar o ponto em cada passo e adicionar G apenas quando o bit é 1. Isto reduz o cálculo de O(n) adições para O(log n), permitindo operações criptográficas práticas mesmo com escalares de 256 bits.


#### A curva secp256k1 em Bitcoin


Bitcoin usa a curva secp256k1, definida por y² = x³ + 7 num campo primo onde p = 2²⁵⁶ - 2³² - 977. O ponto gerador G tem coordenadas fixas escolhidas através de um procedimento determinístico NUMS ("nothing up my sleeve"). A ordem do grupo n é um primo grande próximo de 2²⁵⁶, garantindo que todos os pontos não nulos geram o mesmo grupo. O tamanho de 2²⁵⁶ (~10⁷⁷) é astronomicamente grande, tornando fisicamente impossível a imposição bruta de chaves privadas. Mesmo um trilião de supercomputadores a funcionar durante um trilião de anos não reduziria significativamente o espaço das chaves.


### Chaves públicas, chaves privadas e serialização SEC


Uma chave privada é um escalar aleatório s; a chave pública é P = sG. Como a resolução do problema do log discreto é inviável, P pode ser partilhada sem revelar s. As chaves públicas devem ser serializadas para transmissão usando o formato SEC. O formato SEC não comprimido utiliza 65 bytes: prefixo 0x04 + coordenada x + coordenada y. O formato comprimido utiliza apenas 33 bytes: prefixo 0x02 ou 0x03 (dependendo da paridade de y) + coordenada x. O Bitcoin utilizava originalmente chaves não comprimidas, mas atualmente prefere as comprimidas por uma questão de eficiência.


#### Bitcoin Address Criação


Os endereços Bitcoin são hashes de chaves públicas, não as próprias chaves brutas. Para generate um endereço, serialize a chave pública no formato SEC, calcule hash160 ([SHA-256](https://planb.academy/resources/glossary/sha256) e depois RIPEMD-160), acrescente o prefixo de rede (0x00 para mainnet, 0x6F para testnet), calcule um checksum usando SHA-256 duplo, acrescente os primeiros quatro bytes de checksum e codifique o resultado usando Base58. Esta codificação remove os caracteres ambíguos e inclui a soma de controlo para evitar erros de transcrição. O pipeline de várias etapas oculta a chave pública até que ocorra um gasto, adiciona identificação de rede e garante endereços legíveis por humanos e resistentes a erros.


# Funcionamento interno da transação Bitcoin

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Análise de transacções e assinaturas ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### Compreender o ECDSA: a base de assinatura digital do Bitcoin


O Bitcoin baseia-se no ECDSA, um esquema de assinatura baseado na curva elíptica que oferece uma forte segurança com tamanhos de chave muito mais pequenos do que o RSA. A sua segurança advém do problema do logaritmo discreto da curva elíptica: dado P = eG, calcular P é fácil, mas derivar e de P é computacionalmente inviável. Esta assimetria permite a criptografia de chave pública, mantendo as chaves privadas seguras.


#### Codificação DER de assinaturas ECDSA


O Bitcoin codifica as assinaturas ECDSA utilizando o formato DER:


- 0x30 (marcador de sequência)
- byte de comprimento
- 0x02 + comprimento + R bytes
- 0x02 + comprimento + S bytes


Isso adiciona sobrecarga, expandindo uma assinatura de 64 bytes para ~71-72 bytes. O [Taproot](https://planb.academy/resources/glossary/taproot) elimina esta ineficiência ao adotar assinaturas [Schnorr](https://planb.academy/resources/glossary/schnorr-protocol) de tamanho fixo.


### Compromissos de assinatura e processo de assinatura


As assinaturas ECDSA baseiam-se numa equação de compromisso: UG + VP = KG. O signatário seleciona valores U e V diferentes de zero e um [nonce](https://planb.academy/resources/glossary/nonce) aleatório K, provando o conhecimento da chave privada sem a revelar. A mensagem é introduzida em hash em Z, é gerado um K aleatório, R é a coordenada x de KG e S = (Z + RE)/K. A assinatura é o par (R, S). A segurança depende criticamente da utilização de um K único e imprevisível - se K for reutilizado ou vazado, a chave privada fica comprometida. As implementações modernas utilizam a geração determinística de K (RFC 6979) para evitar falhas de RNG.


#### Verificação da assinatura

Dado Z, (R, S), e a chave pública P, o verificador calcula U = Z/S e V = R/S, e depois verifica se a coordenada x de UG + VP é igual a R. Isto funciona porque a álgebra de verificação reconstrói KG sem precisar da chave privada. A falsificação de assinaturas exigiria a resolução do problema do registo discreto ou a quebra da função hash.


#### Assinaturas Schnorr e contexto histórico


As assinaturas Schnorr são matematicamente mais limpas e suportam recursos de agregação, mas foram patenteadas quando o Bitcoin foi lançado. O ECDSA oferecia uma alternativa gratuita, embora com mais complexidade e assinaturas maiores. Com a expiração das patentes, o Bitcoin adicionou assinaturas Schnorr através do Taproot, fornecendo assinaturas fixas de 64 bytes e maior privacidade. O ECDSA permanece suportado para compatibilidade com o legado.



### Estrutura da transação e entradas/saídas


Uma transação Bitcoin consiste em:


- versão (4 bytes, little-endian)
- lista de entrada
- lista de saída
- locktime (4 bytes)


As entradas referenciam [UTXOs](https://planb.academy/resources/glossary/utxo) anteriores pelo seu hash de transação e índice de saída, e incluem um script de desbloqueio (scriptSig) e um número de sequência utilizado para timelocks ou RBF. As saídas especificam o montante (8 bytes) e o script de bloqueio (scriptPubKey), definindo as condições de despesa. Os endereços Bitcoin são representações destes [scripts](https://planb.academy/resources/glossary/script).


#### O modelo UTXO

O Bitcoin regista as realizações não gastas e não os saldos das contas. Os UTXOs têm de ser gastos na totalidade - é impossível gastar parcialmente. Para gastar 1 BTC de um UTXO de 100 BTC, uma transação deve incluir uma saída de mudança. Esquecer a saída de mudança transforma o restante numa taxa de mineração.


#### Serialização e análise de transacções


As transacções utilizam um formato binário compacto. Após o campo da versão, um varint codifica o número de entradas. As entradas incluem:


- hash de tx anterior (32 bytes)
- índice de saída (4 bytes)
- scriptSig (varstr)
- sequência (4 bytes)


As saídas incluem um valor de 8 bytes e scriptPubKey (varstr). O locktime controla quando a transação se torna válida. A serialização usa ordenação little-endian para a maioria dos inteiros. Os analisadores consomem bytes sequencialmente e delegam a classes especializadas para entradas, saídas e scripts.


### Taxas, mudança e maleabilidade


As taxas são implícitas:

taxa = soma(valores de entrada) - soma(valores de saída).

Qualquer valor não atribuído torna-se a taxa, tornando essencial a construção correta do resultado da alteração. Antes do [SegWit](https://planb.academy/resources/glossary/segwit), as assinaturas permitiam maleabilidade - a modificação de S para N-S produzia uma nova transação válida com um ID diferente. O Bitcoin agora impõe uma regra de S baixo, e o SegWit isola as assinaturas do cálculo do txid, tornando os IDs estáveis e permitindo protocolos de segunda camada como o [Lightning](https://planb.academy/resources/glossary/lightning-network).


## Bitcoin Validação de scripts e transacções

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


O Bitcoin Script é uma pequena linguagem de contrato inteligente baseada em pilha que define como as moedas podem ser gastas. Cada saída tem uma scriptPubKey (script de bloqueio) e cada entrada tem um scriptSig (script de desbloqueio). Juntos, eles formam um programa que deve ser avaliado como "verdadeiro" para que o gasto seja válido. O script não é intencionalmente Turing-completo para que todos os caminhos de execução sejam previsíveis e fáceis de validar na rede.


### Operações de Script e Modelo de Execução


Um script é uma sequência de elementos de dados e códigos de operação. Os pushes de dados (assinaturas, chaves públicas, hashes) são colocados na pilha, enquanto os opcodes que começam com `OP_` transformam a pilha. Após a execução, o elemento do topo da pilha deve ser diferente de zero para ter sucesso. Exemplos: `OP_DUP` duplica o elemento do topo, `OP_HASH160` aplica SHA256 e depois RIPEMD160, e `OP_CHECKSIG` verifica uma assinatura contra o sighash da transação e uma chave pública, colocando 1 para válido, 0 para inválido. As regras de análise distinguem entre dados brutos (prefixados por comprimento) e opcodes (procurados por valor de byte), e uma pequena máquina virtual executa-os deterministicamente em cada [nó](https://planb.academy/resources/glossary/node).


### P2PK e P2PKH: Principais padrões de pagamento


O padrão mais antigo, Pay-to-Public-Key (P2PK), bloqueia as moedas diretamente para uma chave pública completa: o scriptPubKey é `<pubkey> OP_CHECKSIG`, e o scriptSig é apenas uma assinatura. É simples mas pouco eficiente em termos de espaço e expõe a chave pública antes de as moedas serem gastas.


#### P2PKH e endereços

O Pay-to-Public-Key-Hash (P2PKH) melhora isso bloqueando para um hash de 20 bytes da chave pública. O scriptPubKey é `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, e o scriptSig fornece `<signature> <pubkey>`. A execução verifica se a chave pública fornecida tem o hash do valor confirmado e, em seguida, verifica a assinatura. Isso oculta a chave pública até a hora de gastar, reduz o tamanho e corresponde ao familiar formato de endereço "1..." Formato de endereço mainnet.


### Validação de transacções e hashing de assinaturas


Um nó que valida uma transação deve garantir que

1) Cada entrada faz referência a uma saída existente e não gasta.

2) Valor total de entrada ≥ valor total de saída (a diferença é a taxa).

3) Cada scriptSig desbloqueia corretamente a sua scriptPubKey referenciada.


A verificação da assinatura requer a construção da mensagem exata que foi assinada, chamada de sighash. Para o ECDSA legado, a validação esvazia todos os scriptSigs, substitui o scriptSig da entrada atual pelo scriptPubKey correspondente, acrescenta um tipo de hash de 4 bytes (geralmente `SIGHASH_ALL`) e faz um hash duplo no resultado. Esse valor de 256 bits é o que o `OP_CHECKSIG` utiliza. Tipos alternativos de hash (por exemplo, `SINGLE`, `NONE`, com ou sem `ANYONECANPAY`) mudam quais partes da transação são comprometidas, permitindo casos de uso de nicho como financiamento colaborativo ou transações parcialmente especificadas, mas eles raramente são usados na prática.


#### Hashing quadrático e SegWit

Como cada entrada de uma transação antiga requer o seu próprio cálculo de cinzas suspiro sobre uma estrutura que inclui todas as entradas, o tempo de validação pode aumentar quadraticamente com o número de entradas. Grandes transações com várias entradas causavam atrasos perceptíveis na validação. O SegWit redesenhou o cálculo do sighash para armazenar em cache as partes partilhadas e reduzir a complexidade para tempo linear, melhorando a escalabilidade e dificultando os ataques de negação de serviço.


### Puzzles de Script e Lições de Segurança


O script pode exprimir muito mais do que simplesmente "uma assinatura desbloqueia estas moedas" Os puzzles Script demonstram-no codificando condições arbitrárias - problemas matemáticos, desafios de pré-imagem de hash, ou mesmo prémios de colisão - em que qualquer pessoa que forneça os dados corretos pode gastar as moedas. No entanto, as saídas que dependem apenas de dados públicos (sem assinaturas) são vulneráveis ao front-running dos [mineiros](https://planb.academy/resources/glossary/miner): assim que uma solução válida aparece no [mempool](https://planb.academy/resources/glossary/mempool), qualquer mineiro pode copiá-la e redirecionar o pagamento para si próprio.


A lição prática é que os contratos do mundo real quase sempre incluem verificações de assinatura, mesmo quando contêm uma lógica mais complexa, como multisig, timelocks ou hashlocks. As assinaturas vinculam a solução a uma parte específica, preservando incentivos e impedindo que outros roubem o pagamento. Compreender o modelo de pilha do Script, os padrões e as armadilhas subtis é essencial para conceber contratos inteligentes Bitcoin seguros e para raciocinar sobre a forma como as transacções são realmente validadas na rede.


## Construção de transacções e Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Edifício Bitcoin Transacções e P2SH


A construção de transacções Bitcoin faz a ponte entre o conhecimento teórico do protocolo e a implementação prática. Uma transação seleciona UTXOs para gastar, constrói outputs com scripts de bloqueio, cria assinaturas para cada input e serializa tudo no formato exato que os nós esperam. O processo requer a compreensão da geração de sighash, do comportamento do script e do tratamento correto de taxas e alterações.


### Construção básica de transacções


Cada entrada de transação faz referência a uma saída anterior por txid e índice. As saídas especificam os montantes em satoshis e os guiões de bloqueio. A diferença entre o total das entradas e o total das saídas é a taxa. Para assinar uma entrada, uma versão modificada da transação é serializada, o seu sighash é calculado e a chave privada assina-a. A assinatura e a chave pública resultantes formam o ScriptSig. Depois de cada entrada ser assinada, a transação em bruto pode ser transmitida para a rede.


### Transacções com várias assinaturas


Bare multisig utiliza `OP_CHECKMULTISIG` para requerer m-de-n assinaturas. Devido a um bug inicial do tipo off-by-one, o OP_CHECKMULTISIG consome um elemento extra da pilha, exigindo um `OP_0` inicial no ScriptSig. Bare multisig é funcional mas ineficiente: todas as chaves públicas aparecem on-chain, tornando scriptPubKeys grandes, caras e difíceis de codificar como endereços. Estas limitações motivaram a introdução do pay-to-script-hash.


#### Arquitetura P2SH

P2SH esconde scripts complexos atrás de um HASH160 de 20 bytes. O scriptPubKey é fixo: `OP_HASH160 <20-byte hash> OP_EQUAL`. O script de resgate subjacente - contendo multisig, timelocks ou outras condições - só é revelado e executado quando gasto. O remetente apenas vê o hash, enquanto o recetor gere o script de resgate de forma privada. Este design reduz o tamanho do on-chain, melhora a privacidade e permite contratos complexos sem sobrecarregar os remetentes.


### Despesas e implementação do P2SH


Para gastar uma saída P2SH, o ScriptSig deve incluir os dados de desbloqueio necessários *mais* o próprio script de resgate. A validação ocorre em duas etapas:

1) HASH160(redeem_script) deve corresponder ao hash scriptPubKey.

2) Após a verificação, o script da redeem é executado com os dados fornecidos.


Ao gerar assinaturas para uma entrada P2SH, o processo sighash utiliza o script redeem em vez do scriptPubKey. Cada signatário deve possuir o script redeem completo para obter assinaturas válidas generate. Os endereços P2SH utilizam o byte de versão 0x05 no mainnet (endereços "3...") e 0xC4 no testnet (endereços "2...").


#### Considerações práticas de segurança


Perder um script de resgate significa perder fundos: gastar requer tanto as chaves privadas como o próprio script de resgate. Os participantes do Multisig devem verificar se as suas chaves públicas estão corretamente incluídas antes de aceitarem depósitos. O P2SH suporta construções avançadas como multisig, timelocks e hashlocks, mas erros na lógica do script podem bloquear permanentemente os fundos, por isso é essencial testar na testnet.


O P2SH melhora a privacidade ao ocultar as condições de despesa até à primeira despesa, mas quando o script de resgate aparece no on-chain, torna-se permanentemente visível. Apesar disso, os benefícios da dimensão reduzida, da compatibilidade com versões anteriores e do suporte flexível de contratos fizeram do P2SH um marco importante, influenciando actualizações posteriores como o SegWit e o Taproot.


# Funcionamento interno da rede Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Blocos Bitcoin e Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Os [blocos](https://planb.academy/resources/glossary/block) Bitcoin agrupam transacções e protegem-nas utilizando o [proof of work](https://planb.academy/resources/glossary/proof-of-work). Cada bloco inclui um [cabeçalho](https://planb.academy/resources/glossary/block-header) de 80 bytes e uma lista de transacções. Apesar do elevado custo energético da produção de um bloco válido, a verificação de um bloco é barata: armazenar todos os cerca de 900 mil cabeçalhos requer apenas cerca de 72 MB, permitindo que mesmo pequenos dispositivos verifiquem o proof of work da cadeia de forma eficiente.


### Transacções da Coinbase e recompensas em bloco


Cada bloco começa exatamente com uma [transação da Coinbase](https://planb.academy/resources/glossary/coinbase-transaction) - a única forma de novas bitcoins entrarem em circulação. Tem um hash prev-tx zerado e um índice de 0xffffffffff, identificando-o de forma única. O subsídio começou em 50 BTC e diminui para metade a cada 210.000 blocos (50, 25, 12,5, 6,25, 3,125, ...). Os mineiros também incluem taxas de transação. Como o nonce de 4 bytes é demasiado pequeno para os ASICs modernos, os mineiros modificam os dados na transação Coinbase para alterar a raiz [Merkle](https://planb.academy/resources/glossary/merkle-tree) e criar espaço de pesquisa adicional. O [BIP34](https://planb.academy/resources/glossary/bip) requer a incorporação da altura do bloco no scriptSig da Coinbase para garantir que cada txid da Coinbase seja único.


### Campos de cabeçalho de bloco e sinalização Soft Fork


O cabeçalho de 80 bytes contém:


- versão (4 bytes)
- hash do bloco anterior (32 bytes)
- Raiz Merkle (32 bytes)
- carimbo de data/hora (4 bytes)
- bits (objetivo de [dificuldade](https://planb.academy/resources/glossary/difficulty), 4 bytes)
- nonce (4 bytes)


Os números de versão evoluíram para um sistema de sinalização de campo de bits através do BIP9, permitindo aos mineiros coordenar a prontidão do [soft-fork](https://planb.academy/resources/glossary/soft-fork). O carimbo de data/hora é um valor de tempo Unix de 32 bits e terá de ser atualizado por volta do ano 2106.


#### Campo de bits e alvos

O campo bits codifica o objetivo em formato compacto: objetivo = coeficiente × 256^(expoente-3). Os hashes de bloco válidos devem estar numericamente abaixo deste objetivo. Como os hashes são interpretados como números inteiros little-endian, os hashes válidos aparecem frequentemente com muitos zeros à direita quando apresentados em hexadecimal.


### Dificuldade, validação e ajustes


A dificuldade é definida como lowest_target / current_target, expressando o quanto o mining é mais difícil atualmente em comparação com a dificuldade mais fácil possível. A validação requer apenas a comparação do hash do cabeçalho com o alvo - extremamente barato em relação ao mining.


A cada bloco de 2016, o Bitcoin ajusta a dificuldade para atingir intervalos de blocos de aproximadamente 10 minutos. O ajustamento compara o tempo real dos blocos anteriores de 2016 com as duas semanas previstas. Os limites restringem os ajustes a um fator de quatro. Grandes eventos do mundo real - como a proibição do mining na China - demonstraram a resiliência desse mecanismo quando a taxa de hash caiu drasticamente e a dificuldade foi ajustada para baixo para compensar.


### Subsídio por categoria e total Supply


O subsídio na altura h é calculado como: subsídio = 5_000_000_000 >> (h // 210_000). Isto dá origem a um calendário de redução para metade que converge para uma oferta total de ~21 milhões de BTC. A soma da série geométrica (50 + 25 + 12,5 + ...) × 210.000 explica o limite. Os mineiros podem pedir menos do que o subsídio permitido, mas nunca mais, ou o bloco torna-se inválido. À medida que os subsídios diminuem ao longo dos sucessivos halvings, as taxas de transação tornam-se uma componente cada vez mais importante das receitas dos mineiros e da segurança da rede a longo prazo.


## Comunicação em rede e árvores de Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Bitcoin Arquitetura de rede


A rede [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) do Bitcoin opera como um sistema descentralizado de fofocas onde os nós retransmitem transacções e blocos sem confiar uns nos outros. Os novos nós arrancam contactando sementes DNS codificadas mantidas pelos programadores principais. Essas sementes DNS retornam IPs de pares ativos, permitindo que os nós descubram a rede e, em seguida, solicitem pares adicionais via getaddr. A rede não é intencionalmente crítica em termos de [consenso](https://planb.academy/resources/glossary/consensus), pelo que as implementações podem diferir desde que as regras de consenso se mantenham inalteradas.


### Estrutura da mensagem e aperto de mão


Todas as mensagens Bitcoin P2P usam um envelope fixo: um valor mágico de 4 bytes (F9BEB4D9 para mainnet), um comando ASCII de 12 bytes, um comprimento de carga útil little-endian de 4 bytes, um checksum de 4 bytes (primeiros 4 bytes do hash256) e a carga útil. Os comandos comuns incluem version, verack, inv, getdata, tx, block, getheaders, headers, ping e pong.


O aperto de mão começa quando um nó de ligação envia uma mensagem de versão. O recetor responde com verack e a sua própria versão. Quando ambas as partes trocam estas duas mensagens, a ligação está ativa e os nós podem começar a transmitir inventários e dados.


### Árvores de Merkle e Raízes de Merkle


O Bitcoin armazena uma única raiz Merkle de 32 bytes em cada cabeçalho de bloco como um compromisso com todas as transacções no bloco. As transacções são hashadas (hash256), emparelhadas, concatenadas e hashadas repetidamente até restar um hash. Quando um nível tem uma contagem ímpar, o último hash é duplicado. Internamente, os [hashes](https://planb.academy/resources/glossary/hash-function) são big-endian, enquanto os dados serializados do bloco usam little-endian, exigindo inversões antes e depois da construção da árvore.


#### Provas de Merkle e SPV

As provas de Merkle permitem verificar se uma transação está incluída num bloco sem descarregar o bloco inteiro. A prova consiste em hashes irmãos ao longo do caminho para a raiz. Os clientes SPV leves armazenam apenas os cabeçalhos dos blocos e solicitam estas provas aos [nós completos](https://planb.academy/resources/glossary/full-node). Como uma árvore de Merkle cresce logaritmicamente, provar a inclusão num bloco com milhares de transacções requer apenas algumas centenas de bytes.


O Taproot alarga este conceito, atribuindo condições de despesa a uma árvore de scripts Merklized (MAST), revelando apenas o ramo executado juntamente com uma prova de Merkle. Isto melhora tanto a eficiência como a privacidade.


### Operações de rede e sincronização de blocos


Os nós utilizam getdata para solicitar transacções ou blocos, especificando um ID de tipo (1=tx, 2=bloco, 3=bloco filtrado, 4=bloco compacto) mais um identificador de 32 bytes. Para a sincronização em cadeia, os nós enviam getheaders com um hash de bloco inicial, recebendo até 2000 cabeçalhos em resposta. Cada cabeçalho devolvido tem 80 bytes seguidos de uma contagem de transacções fictícias de zero.


A verificação completa dos blocos recebidos requer duas verificações:

1. O hash do bloco deve ser inferior ao objetivo codificado no campo bits.

2. A raiz Merkle calculada a partir de todas as transacções (com o tratamento adequado da endianidade) deve corresponder à raiz do cabeçalho.


Só se ambas as condições forem bem sucedidas é que um nó aceita o bloco, reflectindo o princípio "não confiar, verificar" do Bitcoin.


## Comunicação avançada de nós e testemunha segregada

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Esta sessão unifica a rede P2P avançada com o Segregated Witness, mostrando como o software Bitcoin moderno interage diretamente com os nós enquanto utiliza estruturas de transação com conhecimento do SegWit. Os desenvolvedores aprendem a recuperar blocos, procurar transações relevantes e construir transações usando apenas comunicação de rede bruta - não são necessários exploradores de blocos.


### Recuperação de transacções com base em blocos e privacidade


As [carteiras](https://planb.academy/resources/glossary/wallet) têm de detetar os pagamentos recebidos procurando nos blocos as saídas que correspondam à sua scriptPubKey. A recuperação de blocos inteiros protege melhor a privacidade do que o pedido de transacções individuais, o que deixa escapar fortes sinais sobre a atividade do utilizador. Mesmo pedidos de blocos podem vazar informações sobre cadeias de baixo volume, tornando os filtros de blocos compactos (BIP158) essenciais para clientes leves que preservam a privacidade. Os filtros podem produzir falsos positivos, mas nunca falsos negativos, permitindo que os clientes descarreguem apenas blocos potencialmente relevantes sem revelar endereços específicos.


### Trustless Interação em rede


O fluxo de trabalho `get_block` demonstra o uso adequado da rede: enviar getdata, receber um bloco e, em seguida, verificar independentemente sua raiz Merkle e proof of work. Um bloco é aceite apenas se o hash do cabeçalho recebido corresponder ao hash solicitado e a sua raiz Merkle computada corresponder ao cabeçalho. Isso incorpora o "não confie, verifique", garantindo que mesmo pares maliciosos não possam enganar os nós para que aceitem dados alterados.


#### Recuperação de transacções a partir de blocos

As transacções de um bloco podem ser analisadas em busca de scriptPubKeys correspondentes utilizando uma simples iteração. As carteiras de produção fazem isso continuamente à medida que novos blocos chegam, provando a propriedade das saídas estritamente por meio de validação criptográfica, em vez de depender de APIs de terceiros.


### SegWit Objectivos e conceção


O Segregated Witness (SegWit) corrigiu a maleabilidade das transacções removendo os dados de assinatura do cálculo do txid. Isto permitiu cadeias de transacções pré-assinadas fiáveis e tornou o Lightning Network prático. O SegWit também aumentou a capacidade do bloco usando o "peso do bloco": os nós antigos ainda vêem blocos ≤1 MB, enquanto os nós actualizados validam até 4 MB, incluindo os dados da testemunha. Os programas de testemunhas versionados (v0-v1 até agora) criam um caminho de atualização estruturado para futuros tipos de scripts.


#### P2WPKH (Nativo SegWit)


O P2WPKH substitui a estrutura P2PKH antiga por um script de 22 bytes: OP_0 + push20 + hash160(pubkey). O Spending move a assinatura e a pubkey para um campo de testemunha separado.


- Nós pré-SegWit: ver "anyone-can-spend", tratá-lo como válido.
- Nós pós-SegWit: reconhecer OP_0 + hash de 20 bytes e validar utilizando dados de testemunha.


Esta separação corrige a maleabilidade e reduz as taxas. A testemunha utiliza uma contagem varint seguida da assinatura e da chave pública.


#### P2SH-P2WPKH (compatível com versões anteriores do SegWit)


Para permitir que as carteiras antigas enviem para endereços SegWit, os scripts P2WPKH podem ser embrulhados em P2SH.


- scriptPubKey: padrão P2SH hash160(redeemScript)
- scriptSig: o script de resgate (o programa P2WPKH)
- testemunha: assinatura + chave pública


Camadas de validação:

1. Os nós pré-BIP16 aceitam a redeemScript como válida.

2. Os nós pós-BIP16 avaliam-no, deixando OP_0 + hash na pilha.

3. Os nós SegWit efectuam a validação completa das testemunhas.


#### P2WSH para scripts complexos


O P2WSH generaliza o SegWit para multisig e scripts avançados, fazendo o commit com SHA256(script) em vez de hash160. Uma pilha típica de testemunhas 2-de-3 multisig:


- elemento vazio (erro CHECKMULTISIG)
- sig1
- sig2
- script de testemunha (o script multisig)


Os nós do SegWit verificam se o SHA256(witnessScript) corresponde ao hash scriptPubKey e depois executam-no. A utilização do SHA256 e de um hash de 32 bytes permite distinguir o P2WSH do P2WPKH e reforça a segurança.


#### P2SH-P2WSH (Compatibilidade máxima)


Os guiões complexos SegWit também podem ser embrulhados em P2SH:


- scriptSig: redeemScript (OP_0 + hash de 32 bytes)
- testemunha: assinaturas + witnessScript


A validação passa por três gerações de regras exatamente como no P2SH-P2WPKH. Este invólucro era essencial para as primeiras implementações do Lightning que necessitavam de multisig sem maleabilidade. Embora o P2WSH nativo seja preferido hoje em dia, a forma embrulhada garante a compatibilidade com sistemas wallet mais antigos.


### Impacto do SegWit


SegWit fornecido:


- iDs de transacções estáveis
- taxas mais baixas através de dados de testemunhas com desconto
- maior rendimento do bloco através do peso do bloco
- compatibilidade para nós antigos
- um caminho de atualização limpo para o Taproot e futuras extensões


Juntamente com a interação em rede sem confiança, estas ferramentas constituem a espinha dorsal do desenvolvimento moderno da Bitcoin.



# Secção final


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Comentários e classificações


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Exame final


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Conclusão



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>