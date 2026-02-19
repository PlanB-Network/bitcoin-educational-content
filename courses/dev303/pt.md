---
name: Aprender Rust com Bitcoin
goal: Melhore as suas competências de desenvolvimento Rust através da codificação Bitcoin
objectives: 

  - Habitue-se à linguagem Rust
  - Compreender por que razão se utiliza o Rust para desenvolver o Bitcoin
  - Obter a base do SDK do Lightning

---

# Uma expedição Rust para construtores de Bitcoin



Neste curso prático, que foi filmado durante um seminário organizado pela Fulgur' Ventures em outubro de 2023, irá desenvolver as suas competências em Rust através da construção de componentes e mini-projectos reais centrados no Bitcoin. Abordaremos os fundamentos do Rust, por que o Rust é usado para o desenvolvimento do Bitcoin (segurança de memória, desempenho e simultaneidade segura) e como começar a usar o SDK do Lightning para criar recursos de pagamento.


Ao longo dos capítulos, irá praticar os principais padrões Rust (propriedade, tempos de vida, caraterísticas, assíncrono), trabalhar com primitivos Bitcoin (chaves, transacções, scripting) e integrar progressivamente conceitos Lightning (nós, canais, facturas).


Não é estritamente necessário qualquer desenvolvimento prévio em Rust ou Bitcoin, embora a familiaridade com a programação básica seja útil. O curso é para principiantes, mas é suficientemente prático para os engenheiros que estão a passar para o Bitcoin.


+++

# Introdução

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Descrição geral do curso

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Introdução


Bem-vindo a este curso de programação para iniciantes sobre SDKs. Neste treinamento, você aprenderá os conceitos básicos do Rust, depois se concentrará no Rust aplicado à programação do Bitcoin e terminará com alguns casos de uso usando SDKs.


Os vídeos da formação estarão, por enquanto, disponíveis apenas em inglês e fizeram parte de um seminário ao vivo organizado em outubro passado na Toscana pela Fulgure Venture. Esta formação centrar-se-á apenas na primeira semana. A segunda parte foi direcionada para o RGB e pode ser encontrada no curso RGB.


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Esta formação dá-lhe a oportunidade de desenvolver as suas competências de programação no Lightning Network utilizando o Rust e vários SDK. Foi concebida para programadores com uma sólida experiência em programação que pretendam mergulhar no desenvolvimento específico do Lightning Network. Aprenderá os conceitos básicos do Rust, porque é adequado para o desenvolvimento do Bitcoin e, em seguida, passará à implementação prática utilizando SDKs especializados.


**Secção 2: Aprender a codificar com o Rust

Nesta secção, descobrirá os fundamentos do Rust através de uma série de capítulos progressivos. Aprenderá a escrever código Rust, a compreender as suas especificidades e a dominar as suas caraterísticas essenciais em sete partes detalhadas. Este módulo é essencial para entender por que o Rust é uma linguagem favorita para o desenvolvimento do Bitcoin.


**Secção 3: Rust e Bitcoin

Aqui, exploraremos em profundidade por que o Rust é uma escolha relevante para o desenvolvimento do Bitcoin. Aprenderá sobre o seu modelo de erro, a ferramenta UniFFI e as caraterísticas assíncronas - todos elementos-chave na construção de software robusto e seguro.


**Secção 4: Desenvolvimento LNP/BP com SDKs

Aprenderá a desenvolver nós LN usando vários SDKs como o Breez SDK e o Greenlight para Lipa. Verá como implementar aplicações Lightning Network utilizando bibliotecas concebidas para simplificar o desenvolvimento de Bitcoin e Lightning.


Pronto para aumentar as suas competências no Lightning Network com o Rust? Vamos lá!

# Aprender a programar com o livro rust

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Introdução ao Rust

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

### Instalando e gerenciando o Rust com o Rustup


Ao iniciar sua jornada com o Rust, o primeiro passo envolve a configuração de um ambiente de desenvolvimento adequado. A abordagem mais amplamente recomendada para instalar o Rust é através do Rustup, um sistema de gerenciamento de toolchain que lida com a instalação e atualizações em diferentes projetos e plataformas.


O Rustup serve como mais do que apenas um instalador - ele funciona como uma ferramenta de gerenciamento abrangente para seu ambiente de desenvolvimento Rust. Com o Rustup, pode instalar facilmente alvos de compilação adicionais para diferentes plataformas, como ARM64 para desenvolvimento Android ou outras arquitecturas que possa precisar de suportar. A ferramenta também lida com as actualizações do Rust sem problemas, o que é particularmente valioso dado que o Rust lança uma nova versão estável aproximadamente a cada seis semanas. Quando você precisa atualizar para a versão mais recente, um simples comando `rustup update` trata de tudo automaticamente.


Ao instalar o Rustup, vale a pena entender o modelo de segurança envolvido. O processo de instalação baixa e executa um script do site oficial do Rust em HTTPS, que fornece segurança criptográfica na camada de transporte. Os pacotes baixados pelo Rustup e Cargo vêm de fontes confiáveis (crates.io e infraestrutura oficial do Rust) e se beneficiam da criptografia HTTPS. Embora essa abordagem seja segura para a maioria dos cenários de desenvolvimento, algumas organizações com políticas de segurança rígidas podem preferir instalar o Rust por meio do gerenciador de pacotes de sua distribuição Linux, que fornece uma camada adicional de confiança por meio da infraestrutura de assinatura de pacotes da própria distribuição. Para fins de aprendizagem e desenvolvimento geral, o Rustup é uma ferramenta bem estabelecida e amplamente confiável no ecossistema do Rust.


Para a maioria dos cenários de desenvolvimento, você pode instalar o Rustup executando o script de instalação fornecido no site oficial do Rust. O instalador irá pedir-lhe para escolher entre diferentes opções de cadeia de ferramentas, sendo a cadeia de ferramentas estável a escolha recomendada para a maioria dos utilizadores. A instalação ocorre no seu diretório pessoal, não requer privilégios de administrador e configura todas as variáveis de ambiente necessárias para uso imediato.


### Compreender as cadeias de ferramentas e os componentes do Rust


O ecossistema de desenvolvimento do Rust consiste em vários componentes-chave que trabalham em conjunto para fornecer um ambiente de programação completo. A compreensão destes componentes ajuda-o a navegar no processo de desenvolvimento do Rust de forma mais eficaz e a resolver problemas quando estes surgem.


O compilador do Rust, conhecido como `rustc`, forma o núcleo da cadeia de ferramentas do Rust. Enquanto você poderia teoricamente usar o `rustc` diretamente para compilar programas Rust, a maior parte do trabalho de desenvolvimento depende do Cargo, o gerenciador de pacotes e sistema de compilação do Rust. Cargo funciona de forma similar ao npm no ecossistema JavaScript, gerenciando dependências, coordenando compilações e fornecendo comandos convenientes para tarefas comuns de desenvolvimento. Quando você executa comandos como `cargo build` ou `cargo run`, o Cargo orquestra o processo de compilação, lida com a resolução de dependências e gerencia a estrutura geral do projeto.


Clippy é um linter que analisa o seu código e fornece sugestões de melhorias. Ao contrário dos verificadores de sintaxe básicos, o Clippy compreende as expressões idiomáticas do Rust e pode recomendar formas mais idiomáticas de realizar tarefas específicas. Esta ferramenta ajuda a aprender as melhores práticas do Rust e a escrever código mais fácil de manter.


A cadeia de ferramentas do Rust também inclui ferramentas de documentação abrangentes e a documentação da biblioteca padrão, acessível através do sítio Web oficial da documentação do Rust. Esta documentação serve como uma referência indispensável durante o desenvolvimento, fornecendo informações detalhadas sobre funções, tipos e módulos da biblioteca padrão. A documentação inclui exemplos extensivos e explicações que o ajudam a compreender não só o que as funções fazem, mas também como as utilizar eficazmente nos seus programas.


O Rust suporta múltiplos canais de lançamento: stable, beta e nightly. O canal estável fornece versões completamente testadas adequadas para uso em produção. O canal beta oferece uma pré-visualização da próxima versão estável, usada principalmente para testes finais antes do lançamento oficial. O canal nightly inclui caraterísticas experimentais em desenvolvimento ativo, que podem ser úteis para experimentar novas capacidades do Rust, embora estas caraterísticas possam mudar ou ser removidas em futuras versões.


### Criando e gerenciando projetos Rust com o Cargo


O desenvolvimento moderno do Rust gira em torno do Cargo, que simplifica a criação de projetos, o gerenciamento de dependências e o processo de construção. Ao invés de criar manualmente diretórios e arquivos, o Cargo fornece o comando `cargo new` para criar uma estrutura de projeto completa com padrões sensatos.


Quando você cria um novo projeto com `cargo new project_name`, o Cargo estabelece uma estrutura de diretórios padrão, cria um arquivo básico `main.rs` com um programa "Hello, world!", inicializa um repositório Git e gera um arquivo `Cargo.toml` para configuração do projeto. O arquivo `Cargo.toml` serve como ponto central de configuração para seu projeto, contendo metadados sobre seu projeto e listando todas as dependências que seu código requer.


O Cargo fornece vários comandos essenciais para o trabalho diário de desenvolvimento. O comando `cargo build` compila seu projeto e suas dependências, criando arquivos executáveis no diretório `target`. Para uma rápida iteração durante o desenvolvimento, o comando `cargo run` combina compilação e execução em uma única etapa. O comando `cargo check` executa todas as verificações de compilação sem gerar o executável final, tornando-o significativamente mais rápido do que uma compilação completa quando você quer simplesmente verificar se seu código compila corretamente.


Ao preparar o código para implantação em produção, o sinalizador `--release` habilita otimizações e remove asserções de depuração. As compilações de versão são executadas mais rapidamente e produzem executáveis menores, mas levam mais tempo para compilar e removem informações úteis de depuração. O compilador aplica várias otimizações durante as compilações de lançamento e desativa as verificações em tempo de execução, como a deteção de estouro de inteiro, o que melhora o desempenho, mas remove algumas garantias de segurança presentes nas compilações de depuração.


### Variáveis, mutabilidade e a filosofia de segurança do Rust


O Rust adota uma abordagem diferente da maioria das linguagens para o gerenciamento de variáveis. Por defeito, todas as variáveis no Rust são imutáveis, o que significa que os seus valores não podem ser alterados após a atribuição inicial. Esta decisão de design tem como objetivo evitar erros de programação comuns que surgem de alterações de estado inesperadas.


Quando você declara uma variável usando `let x = 5`, essa variável se torna imutável por padrão. Qualquer tentativa de modificar seu valor posteriormente resultará em um erro de compilação. Esse requisito de imutabilidade força os desenvolvedores a pensar cuidadosamente sobre quando as mudanças de estado são realmente necessárias e torna o comportamento do código mais previsível. Muitos bugs de programação resultam de variáveis que mudam inesperadamente, e a imutabilidade padrão do Rust ajuda a evitar esses problemas.


Quando você realmente precisa modificar o valor de uma variável, o Rust requer a declaração explícita de mutabilidade usando a palavra-chave `mut`: `let mut x = 5`. Esta declaração explícita serve como um sinal claro, tanto para o compilador quanto para outros desenvolvedores, de que o valor desta variável pode mudar durante a execução do programa. O requisito de declarar explicitamente a mutabilidade encoraja uma consideração cuidadosa sobre se a mutabilidade é realmente necessária para cada variável.


O Rust também suporta shadowing, que permite declarar uma nova variável com o mesmo nome de uma variável anterior. Ao contrário da mutação, a sombra cria uma variável inteiramente nova que tem o mesmo nome, ocultando efetivamente a variável anterior. Esta técnica revela-se particularmente útil quando se transformam dados através de vários passos, como analisar uma cadeia de caracteres num número e depois processar esse número. Com a sombra, pode manter um nome de variável consistente ao longo do processo de transformação enquanto altera o tipo da variável em cada passo.


A distinção entre shadowing e mutação torna-se importante quando se consideram as alterações de tipo. Com a sombra, pode alterar tanto o valor como o tipo de uma variável, porque está a criar uma nova variável. Com a mutação, só pode alterar o valor mantendo o mesmo tipo, uma vez que está a modificar uma variável existente em vez de criar uma nova.


```rust
// Shadowing: creating new variables with the same name
let amount = "100000";           // amount is a &str (string slice)
let amount = amount.parse::<u64>().unwrap();  // amount is now u64
let amount = amount * 100;       // amount is still u64, new value

// Mutation: modifying the same variable
let mut balance = 50000_u64;
balance = balance + amount;      // OK: same type, different value
// balance = "empty";            // ERROR: cannot change type with mutation

// Practical example: processing a Bitcoin amount input
let user_input = "  0.001 ";                    // &str with whitespace
let user_input = user_input.trim();            // &str, whitespace removed
let satoshis: u64 = (user_input.parse::<f64>().unwrap() * 100_000_000.0) as u64;
println!("Amount in satoshis: {}", satoshis);  // 100000
```


### Tipos de dados e fundamentos do sistema de tipos


Rust implementa um sistema de tipo forte e estático onde cada valor deve ter um tipo bem definido conhecido em tempo de compilação. Embora isso possa parecer restritivo em comparação com linguagens dinamicamente tipadas, as capacidades de inferência de tipo do Rust significam que raramente é necessário especificar tipos explicitamente. O compilador pode normalmente determinar o tipo apropriado com base na forma como o valor é utilizado.


No entanto, certas situações exigem anotações de tipo explícitas. Ao usar funções genéricas como `parse()`, que podem converter strings em vários tipos numéricos, o compilador precisa saber qual tipo específico você deseja. Nesses casos, você fornece anotações de tipo usando a sintaxe de dois pontos: `let guess: u32 = "42".parse().expect("Não é um número!")`.


Os tipos escalares do Rust incluem inteiros, números de ponto flutuante, booleanos e caracteres. O sistema de tipos inteiros permite um controlo preciso da utilização da memória e das caraterísticas de desempenho. Os tipos inteiros são nomeados sistematicamente: `i8`, `i16`, `i32`, `i64` e `i128` para números inteiros com sinal, e `u8`, `u16`, `u32`, `u64` e `u128` para números inteiros sem sinal. Os números indicam a largura dos bits, tornando a utilização da memória e os intervalos de valores imediatamente claros.


Os tipos `isize` e `usize` merecem atenção especial, pois se adaptam à sua arquitetura de destino. Em sistemas de 64 bits, esses tipos têm 64 bits de largura, enquanto em sistemas de 32 bits, eles têm 32 bits de largura. Esses tipos são comumente usados para indexação de array e offsets de memória porque eles correspondem ao tamanho natural da palavra da arquitetura de destino, permitindo aritmética de ponteiro eficiente e operações de memória.


O Rust fornece várias formas de escrever literais inteiros, incluindo os formatos decimal, hexadecimal (`0x`), octal (`0o`) e binário (`0b`). Você também pode usar sublinhados em qualquer lugar dentro de literais numéricos para melhorar a legibilidade, como escrever `1_000_000` em vez de `1000000`. Os sublinhados não têm efeito sobre o valor, mas podem tornar números grandes mais legíveis.


Os tipos de ponto flutuante no Rust são simples: `f32` para números de precisão simples e `f64` para números de ponto flutuante de precisão dupla. O tipo `f64` é geralmente preferido devido à sua maior precisão e ao facto de os processadores modernos poderem frequentemente lidar com operações de vírgula flutuante de 64 bits tão eficientemente como as operações de 32 bits.


### Tipos compostos e organização de dados


Para além dos tipos escalares, o Rust fornece tipos compostos que agrupam vários valores. As tuplas permitem combinar valores de diferentes tipos em um único valor composto. Você cria tuplas usando parênteses e pode especificar o tipo de cada elemento: `let tup: (i32, f64, u8) = (500, 6.4, 1)`.


As tuplas suportam desestruturação, o que permite extrair valores individuais: `let (x, y, z) = tup`. Esta sintaxe cria três variáveis separadas a partir dos componentes da tupla. Alternativamente, você pode acessar os elementos da tupla diretamente usando a notação de ponto com o índice do elemento: `tup.0`, `tup.1`, `tup.2`.


```rust
// Creating a tuple with different types
let transaction: (&str, u64, bool) = ("abc123", 50000, true);

// Destructuring: extract all values at once
let (txid, amount, confirmed) = transaction;
println!("Transaction {} for {} sats", txid, amount);

// Dot notation: access individual elements by index
println!("Confirmed: {}", transaction.2);  // true

// Practical example: function returning multiple values
fn parse_utxo(data: &str) -> (String, u32, u64) {
// Returns (txid, output_index, value_in_sats)
("a]1b2c3".to_string(), 0, 100000)
}

let (txid, vout, value) = parse_utxo("raw_data");
println!("UTXO {}:{} = {} sats", txid, vout, value);
```


Arrays em Rust diferem significativamente de arrays ou listas em muitas outras linguagens porque eles têm um tamanho fixo que se torna parte de seu tipo. Um array de cinco inteiros tem o tipo `[i32; 5]`, onde o ponto e vírgula separa o tipo do elemento do comprimento do array. Essa informação de tamanho no nível do tipo permite que o compilador execute a verificação de limites e garante que as funções que recebem arrays saibam exatamente quantos elementos esperar.


É possível inicializar arrays listando todos os elementos explicitamente: `[1, 2, 3, 4, 5]`, ou utilizando uma sintaxe abreviada para arrays com valores repetidos: `[3; 5]` cria um array de cinco elementos, todos com o valor 3. Esta abreviação é útil para inicializar buffers ou criar arrays com valores padrão.


O acesso a matrizes usa notação de colchetes como a maioria das linguagens, mas o Rust fornece verificação de limites em tempo de compilação e em tempo de execução. Quando se acede a uma matriz com um índice constante que o compilador pode verificar, este irá detetar o acesso fora dos limites em tempo de compilação. Para índices dinâmicos determinados em tempo de execução, o Rust insere verificações de limites que farão com que o programa entre em pânico se tentar aceder a um índice inválido, evitando violações da segurança da memória.



## Ownership e segurança da memória no Rust

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


### Entendendo a abordagem única do Rust para o gerenciamento de memória


Este capítulo cobre um dos conceitos mais importantes do Rust. Enquanto os conceitos anteriores podem ter parecido familiares para programadores vindos de outras linguagens, a propriedade é a abordagem do Rust para resolver a segurança de memória sem coleta de lixo.


O Rust foi concebido com o objetivo fundamental de evitar erros relacionados com a memória que afectam as linguagens de baixo nível, como o C e o C++. Esses problemas incluem erros de uso após a liberação, em que a memória é acessada após ter sido liberada, e estouro de buffer, em que os programas escrevem fora dos limites de memória alocados. As soluções tradicionais para estes problemas envolveram compromissos que o Rust procura eliminar. Linguagens de alto nível como Java e Go resolvem a segurança da memória através da coleta de lixo, onde um processo automático identifica e libera periodicamente a memória não utilizada. No entanto, os coletores de lixo introduzem sobrecarga de desempenho e podem causar pausas imprevisíveis durante a execução do programa, tornando-os inadequados para a programação de sistemas onde o desempenho consistente é crítico.


O Rust alcança a segurança da memória principalmente através da análise estática efectuada em tempo de compilação. O compilador examina o código-fonte e pode determinar se a maioria das operações de memória são seguras sem a necessidade de coleta de lixo. Para casos que não podem ser verificados estaticamente - como acesso a array com índices calculados em tempo de execução - o Rust insere verificações de limites que causam pânico em vez de permitir comportamento indefinido. Essa abordagem difere fundamentalmente dos analisadores estáticos disponíveis para C e C++, que foram adaptados para linguagens não originalmente projetadas para uma análise estática abrangente. A sintaxe e as regras de linguagem do Rust foram criadas desde o início para permitir uma extensa verificação em tempo de compilação, garantindo que, uma vez que um programa seja compilado com sucesso, ele será executado com segurança ou entrará em pânico de forma previsível, em vez de exibir um comportamento indefinido.


### O sistema Ownership: Regras e princípios


A pedra angular das garantias de segurança de memória do Rust é o sistema de propriedade, que governa como a memória é gerenciada durante a execução de um programa. O Ownership opera em três regras fundamentais que o compilador impõe a todo momento:


1. Cada valor no Rust tem um proprietário (uma variável que contém o valor)

2. Só pode haver um proprietário de cada vez

3. Quando o proprietário sai do âmbito, o valor é eliminado


Os escopos no Rust são tipicamente definidos por chaves, seja em corpos de funções, blocos condicionais ou blocos de escopo criados explicitamente. Quando uma variável é declarada dentro de um escopo, esse escopo se torna o proprietário do valor da variável. A variável permanece acessível e válida durante todo o tempo de vida do escopo, mas assim que a execução deixa o escopo, todas as variáveis proprietárias são automaticamente limpas por meio de um processo chamado dropping.


Esta limpeza automática é implementada através do mecanismo de drop do Rust, onde a linguagem chama implicitamente uma função drop em variáveis que saem do escopo. Para tipos básicos, isso significa simplesmente que a memória é marcada como disponível para reutilização. Para tipos mais complexos que gerem recursos, as implementações personalizadas de drop podem efetuar operações de limpeza adicionais, tais como fechar os identificadores de ficheiros ou libertar ligações de rede. Esse padrão, emprestado do RAII (Resource Acquisition Is Initialization) do C++, garante que os recursos sejam sempre liberados corretamente sem exigir código de limpeza explícito do programador.


### Movimentação do Ownership e disposição da memória


Para entender como a propriedade é transferida entre variáveis, é necessário examinar a diferença entre tipos simples e tipos complexos em termos de layout de memória e comportamento de cópia. Tipos simples como inteiros, booleanos e números de ponto flutuante têm um tamanho fixo e conhecido em tempo de compilação e podem ser copiados com eficiência. Quando você atribui uma variável inteira a outra, o Rust cria uma cópia completa e independente do valor, permitindo que ambas as variáveis existam simultaneamente sem qualquer preocupação de propriedade.


Tipos complexos como strings apresentam um desafio diferente porque gerenciam a memória alocada dinamicamente. Uma String no Rust consiste em três componentes armazenados na pilha: um ponteiro para dados de caracteres alocados em heap, o comprimento atual da string e a capacidade total do buffer alocado. Essa estrutura permite que as strings cresçam e diminuam de forma eficiente, mantendo o conhecimento de seus limites. Quando você atribui uma variável String a outra, o Rust enfrenta uma escolha: ele pode copiar apenas a estrutura baseada na pilha (criando dois ponteiros para os mesmos dados do heap) ou executar uma cópia profunda de todos os dados do heap.


O comportamento padrão do Rust é mover a propriedade em vez de copiar, transferindo os dados do heap da variável de origem para a variável de destino e invalidando a origem. Essa abordagem evita o cenário perigoso em que várias variáveis podem modificar a mesma memória heap ou em que a mesma memória pode ser liberada várias vezes quando as variáveis saem do escopo. A operação de movimentação é eficiente porque copia apenas a pequena estrutura baseada em pilha, e não os dados de heap potencialmente grandes, mantendo a segurança da memória ao garantir a propriedade única.


### Referências e empréstimos


Embora os movimentos de propriedade proporcionem segurança, podem ser restritivos quando é necessário utilizar um valor em vários locais sem transferir a propriedade. O Rust resolve isso através do empréstimo, que permite que funções e variáveis acessem temporariamente os dados sem assumir a propriedade. Uma referência, criada utilizando o operador "e comercial", fornece acesso apenas de leitura a um valor, deixando a propriedade com a variável original.


As referências permitem que as funções operem em dados sem consumi-los, possibilitando o uso do mesmo valor várias vezes ao longo de um programa. Quando passa uma referência a uma função, está a emprestar os dados temporariamente, e a função deve devolver a referência antes que o proprietário original possa recuperar o controlo total. Esta metáfora de empréstimo reflecte a natureza temporária do acesso: tal como se empresta um livro a um amigo mantendo a propriedade, as referências permitem o acesso temporário preservando a relação de propriedade original.


As referências mutáveis estendem este conceito para permitir a modificação de dados emprestados, mas com restrições estritas para manter a segurança. O Rust permite apenas uma referência mutável a um dado num determinado momento, evitando corridas de dados em que várias partes de um programa podem modificar simultaneamente a mesma memória. Além disso, não é possível ter referências mutáveis e imutáveis aos mesmos dados simultaneamente, pois isso poderia levar a situações em que o código assume que os dados são estáveis enquanto outro código os modifica ativamente. Estas regras são aplicadas em tempo de compilação, eliminando classes inteiras de erros de concorrência que assolam outras linguagens de programação de sistemas.


```rust
fn main() {
let mut wallet_balance: u64 = 100_000; // 100,000 satoshis

// Immutable borrow: read the balance
let balance_ref = &wallet_balance;
println!("Current balance: {} sats", balance_ref);
// balance_ref goes out of scope here

// Mutable borrow: update the balance
let balance_mut = &mut wallet_balance;
*balance_mut += 50_000; // Receive payment
println!("After deposit: {} sats", balance_mut);
// balance_mut goes out of scope here

// Function that borrows immutably
fn display_balance(balance: &u64) {
println!("Balance check: {} sats", balance);
}

// Function that borrows mutably
fn deduct_fee(balance: &mut u64, fee: u64) {
*balance -= fee;
}

display_balance(&wallet_balance);
deduct_fee(&mut wallet_balance, 1_000);
println!("After fee: {} sats", wallet_balance); // 149,000
}
```


### Tipos e fatias de strings


O Rust distingue entre literais de cadeia de caracteres e o tipo String, reflectindo diferentes estratégias de gestão de memória e casos de utilização. Os literais de cadeia de caracteres são incorporados diretamente no binário compilado e têm o tipo &str (fatia de cadeia de caracteres), representando uma vista em dados de cadeia de caracteres imutáveis. Esses literais são eficientes porque não requerem alocação em tempo de execução, mas não podem ser modificados, pois fazem parte do código do programa.


O tipo String, por outro lado, gere a memória alocada dinamicamente e pode crescer, diminuir e ser modificado em tempo de execução. É possível criar uma String a partir de um literal usando String::from() ou métodos similares, que alocam memória heap e copiam o conteúdo do literal. Esta distinção permite ao Rust otimizar tanto a performance (usando literais quando possível) como a flexibilidade (usando String quando é necessária modificação).


As fatias de cadeia de caracteres (&str) fornecem uma abstração poderosa para trabalhar com partes de cadeias de caracteres sem copiar dados. Uma fatia contém um ponteiro para o início dos dados da cadeia e um comprimento, permitindo-lhe fazer referência a substrings de forma eficiente. A sintaxe de fatia usa intervalos (por exemplo, &s[0..5]) para especificar qual parte da string deve ser referenciada. Como as fatias são referências, elas estão sujeitas a regras de empréstimo, impedindo que a string subjacente seja modificada enquanto as fatias existirem. Esta aplicação em tempo de compilação evita erros comuns como aceder a memória inválida depois de a string original ter sido libertada ou modificada.


### Matrizes, vectores e fatias genéricas


O conceito de fatia estende-se para além das strings a qualquer sequência de elementos, fornecendo uma forma unificada de trabalhar com arrays de tamanho fixo e vectores dinâmicos. As matrizes no Rust têm seu comprimento codificado em seu tipo (por exemplo, [i32; 5] para uma matriz de cinco inteiros de 32 bits), tornando-as adequadas para situações que exigem garantias de tamanho em tempo de compilação. As funções que aceitam arrays podem impor requisitos de comprimento exato, úteis para operações como funções criptográficas que necessitam de entradas de tamanho preciso.


As fatias (&[T]) fornecem uma alternativa mais flexível, representando uma visão em qualquer sequência contígua de elementos, independentemente do armazenamento subjacente. É possível criar fatias a partir de matrizes, vectores ou outras fatias, e a mesma fatia pode fazer referência a diferentes porções de dados ao longo do seu tempo de vida. Esta flexibilidade torna as fatias ideais para funções que precisam de processar sequências sem se preocuparem com o mecanismo de armazenamento específico ou o tamanho exato.


A relação entre tipos próprios (String, Vec<T>) e suas contrapartes de fatias emprestadas (&str, &[T]) segue um padrão consistente em todo o Rust. Tipos próprios gerenciam sua memória e podem ser modificados, enquanto fatias fornecem acesso eficiente e somente leitura a partes desses dados. Este design permite APIs que são flexíveis (aceitando vários tipos de entrada através de slices) e eficientes (evitando cópias desnecessárias), enquanto mantém as garantias de segurança do Rust através do sistema de empréstimo.



## Estruturas, construção de tipos de dados complexos

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

As estruturas no Rust servem como base para a criação de tipos de dados complexos, semelhantes às classes noutras linguagens de programação. Elas permitem agrupar dados relacionados em uma única unidade coesa que pode conter múltiplos campos de diferentes tipos. A sintaxe para definir uma estrutura segue um padrão simples: você usa a palavra-chave `struct` seguida pelo nome da estrutura, então define os campos entre chaves usando uma sintaxe de dois pontos para especificar o tipo de cada campo.


O Rust segue convenções específicas de nomenclatura para estruturas que o compilador irá impor através de avisos. Nomes de estruturas devem usar CamelCase (também conhecido como PascalCase), enquanto nomes de campos dentro da estrutura devem usar snake_case com underscores. Essa convenção ajuda a manter a consistência entre as bases de código do Rust e torna o código mais legível para outros desenvolvedores.


A criação de instâncias de estruturas requer a especificação de valores para todos os campos utilizando o nome da estrutura seguido de chavetas que contêm as atribuições de campo. Uma vez que você tenha uma instância de estrutura, você pode acessar e modificar campos individuais usando notação de ponto, desde que a instância seja declarada como mutável. Esta notação de ponto funciona de forma consistente no Rust, ao contrário de linguagens como o C++ onde pode utilizar diferentes operadores para ponteiros versus objectos diretos.


### Funções de construtor e atalhos de campo


O Rust não tem construtores incorporados como algumas linguagens orientadas para objectos, mas pode criar funções que devolvem instâncias de estruturas para servir o mesmo propósito. Essas funções construtoras tipicamente recebem parâmetros para alguns ou todos os campos e podem definir valores padrão para outros. Ao escrever tais funções, o Rust fornece uma abreviação conveniente: se um parâmetro tem o mesmo nome de um campo da estrutura, você pode simplesmente escrever o nome do campo uma vez ao invés de repeti-lo no formato `campo: valor`.


As instâncias de estrutura também podem ser criadas copiando valores de instâncias existentes utilizando a sintaxe de atualização da estrutura. Este recurso permite criar uma nova instância especificando apenas os campos que deseja alterar, com todos os outros campos copiados de uma instância existente. No entanto, esta operação segue as regras de propriedade do Rust, o que significa que os tipos não-Copy serão movidos da instância de origem, potencialmente tornando partes da instância original inutilizáveis posteriormente. O compilador rastreia esses movimentos parciais de forma inteligente, permitindo que você continue usando campos que não foram movidos enquanto impede o acesso aos campos movidos.


### Estruturas de tuplas e estruturas de unidades


O Rust suporta estruturas de tuplas, que são estruturas com campos não nomeados acedidos por índice em vez de por nome. Elas são úteis para tipos simples de wrapper ou quando você precisa de uma estrutura mas não precisa de campos nomeados. Você acessa os campos da estrutura tupla usando a notação de ponto seguida pelo índice do campo, como `.0` para o primeiro campo, `.1` para o segundo, e assim por diante. Esta abordagem funciona bem para estruturas que envolvem um único valor ou contêm apenas alguns valores relacionados onde os nomes podem ser redundantes.


As estruturas unitárias representam a forma mais simples de estruturas - não contêm quaisquer dados. Embora isto possa parecer inútil inicialmente, as estruturas unitárias tornam-se valiosas quando se trabalha com o sistema de caraterísticas do Rust, uma vez que podem implementar comportamentos sem armazenar quaisquer dados. Estas estruturas vazias servem como marcadores ou espaços reservados em padrões Rust mais avançados.


### Métodos e funções associadas


As estruturas ganham funcionalidade adicional quando você adiciona comportamento através de blocos de implementação. Utilizando a palavra-chave `impl` seguida do nome da estrutura, você pode definir métodos que operam em instâncias da sua estrutura. Métodos são funções que recebem `self` como seu primeiro parâmetro, que pode ser um valor próprio (`self`), uma referência imutável (`&self`), ou uma referência mutável (`&mut self`), dependendo do que o método precisa fazer com a instância.


A escolha do tipo de parâmetro `self` determina o comportamento do método em relação à propriedade. Métodos com `&self` podem ler da instância sem assumir a propriedade, tornando-os adequados para operações que não modificam a estrutura. Métodos que recebem `&mut self` podem modificar a instância enquanto ainda permitem que o chamador mantenha a propriedade. Métodos que tomam `self` como valor consomem a instância, o que é apropriado para operações que transformam a estrutura em outra coisa ou quando o método representa a operação final naquela instância.


Funções associadas são funções definidas dentro de um bloco de implementação que não recebem `self` como parâmetro. Elas são similares a métodos estáticos em outras linguagens e são comumente usadas como construtores ou funções utilitárias relacionadas ao tipo. Você chama funções associadas usando a sintaxe de dois pontos (`Type::nome_da_função()`), o que as distingue claramente de métodos chamados em instâncias.


```rust
// Define a struct for a Lightning invoice
struct Invoice {
payment_hash: String,
amount_msat: u64,
description: String,
expiry_secs: u32,
}

impl Invoice {
// Associated function (constructor) - no self parameter
fn new(payment_hash: String, amount_msat: u64, description: String) -> Self {
Invoice {
payment_hash,
amount_msat,
description,
expiry_secs: 3600, // default 1 hour
}
}

// Method with &self - read-only access
fn amount_sats(&self) -> u64 {
self.amount_msat / 1000
}

// Method with &mut self - can modify the instance
fn extend_expiry(&mut self, additional_secs: u32) {
self.expiry_secs += additional_secs;
}

// Method with self - consumes the instance
fn into_payment_request(self) -> String {
format!("lnbc{}n1p{}", self.amount_msat, self.payment_hash)
}
}

fn main() {
// Use associated function to create instance
let mut invoice = Invoice::new(
"abc123".to_string(),
100_000_000, // 100,000 sats in millisats
"Coffee payment".to_string(),
);

println!("Amount: {} sats", invoice.amount_sats());
invoice.extend_expiry(1800); // Add 30 minutes

let request = invoice.into_payment_request();
// invoice is now consumed, cannot be used anymore
println!("Payment request: {}", request);
}
```


#### Enumerações: Modelagem de opções e variantes


As enumerações em Rust têm mais capacidades do que as enums em muitas outras linguagens. Embora possam representar conjuntos simples de constantes nomeadas, as enums do Rust também podem conter dados dentro de cada variante, tornando-as adequadas para modelar situações em que um valor pode ser um de vários tipos ou estados diferentes. Cada variante de enum pode conter diferentes tipos e quantidades de dados, desde nenhum dado até estruturas complexas com campos nomeados.


A capacidade de anexar dados a variantes de enum elimina muitos erros de programação comuns encontrados noutras linguagens. Em vez de manter variáveis separadas para um indicador de tipo e os dados associados - que podem facilmente tornar-se inconsistentes - os enums do Rust agrupam as informações de tipo com os próprios dados. Este design garante que os dados correspondem sempre à variante, evitando incompatibilidades que podem levar a erros de tempo de execução.


As variantes de enum podem conter dados de várias formas: sem dados para sinalizadores simples, dados do tipo tupla para campos não nomeados ou dados do tipo struct com campos nomeados. Pode até misturar estes estilos num único enum, escolhendo a forma mais apropriada para cada variante. Esta flexibilidade torna os enums adequados para modelar conceitos de domínio complexos, em que casos diferentes requerem informações diferentes.


#### O tipo de opção: Lidar com a ausência de forma segura


Um dos enums mais importantes do Rust é o `Option<T>`, que representa valores que podem ou não estar presentes. Este enum tem duas variantes: `Some(T)` contendo um valor do tipo T, e `None` representando a ausência de um valor. O tipo Option serve como a solução do Rust para os problemas de ponteiro nulo que assolam muitas outras linguagens, forçando os desenvolvedores a tratar explicitamente os casos em que valores podem estar ausentes.


A utilização de tipos Option torna o seu código mais robusto porque o compilador exige que trate tanto a presença como a ausência de valores. Não é possível usar acidentalmente um valor potencialmente ausente sem primeiro verificar se ele existe. Este tratamento explícito evita excepções de ponteiro nulo e erros de tempo de execução semelhantes que são fontes comuns de bugs noutras linguagens de programação.


O tipo Option integra-se com o sistema de correspondência de padrões do Rust, permitindo-lhe lidar com ambos os casos. Métodos como `unwrap_or()` fornecem maneiras convenientes de extrair valores com padrões de fallback, enquanto métodos como `map()` e `and_then()` permitem padrões de programação funcional para trabalhar com valores opcionais.


### Correspondência de padrões com expressões de correspondência


A correspondência de padrões através de expressões `match` fornece uma maneira de trabalhar com enums e outros tipos de dados. Uma expressão match examina um valor e executa um código diferente baseado no padrão que o valor corresponde. Cada padrão pode desestruturar o valor correspondido, vinculando partes dele a variáveis que podem ser usadas no bloco de código correspondente.


As expressões de correspondência devem ser exaustivas, o que significa que devem tratar todos os casos possíveis para o tipo que está a ser correspondido. Este requisito previne bugs que poderiam ocorrer se certos casos fossem acidentalmente deixados sem tratamento. Quando você não quer tratar todos os casos explicitamente, você pode usar o padrão curinga (`_`) para pegar todos os casos restantes, ou ligar casos não tratados a uma variável se você precisar acessar o valor.


A construção `if let` fornece uma alternativa mais concisa para match quando você só se preocupa com um padrão específico. Esta sintaxe é particularmente útil quando se trabalha com tipos Option ou quando se deseja executar código somente se um valor corresponde a uma variante enum particular. A construção `if let` pode incluir uma cláusula `else` para os casos em que o padrão não corresponde, tornando-a uma forma simplificada de lidar com cenários simples de correspondência de padrões.


#### Colecções: Gerir grupos de dados


A biblioteca padrão do Rust fornece vários tipos de colecções para gerir grupos de dados relacionados. Estas colecções são genéricas, o que significa que podem armazenar elementos de qualquer tipo, e gerem automaticamente a gestão da memória. As colecções mais utilizadas são vectores para listas ordenadas, mapas hash para associações chave-valor e cadeias de caracteres para dados de texto.


#### Vectores: Matrizes dinâmicas


Os vectores representam matrizes expansíveis que podem mudar de tamanho durante a execução do programa. Ao contrário dos vetores de tamanho fixo, os vetores alocam memória no heap e podem expandir ou diminuir conforme necessário. A criação de um vetor requer frequentemente uma anotação de tipo explícita quando se começa com um vetor vazio, uma vez que o compilador precisa de saber que tipo de elementos o vetor irá conter.


Vetores fornecem múltiplas maneiras de acessar elementos, cada um com diferentes caraterísticas de segurança. A notação de índice (`vec[0]`) fornece acesso direto, mas entrará em pânico se o índice estiver fora dos limites. O método `get()` retorna uma `Option`, permitindo que o acesso fora dos limites seja tratado de forma elegante. A escolha entre essas abordagens depende se você pode garantir que o índice é válido ou se precisa lidar com possíveis falhas.


As regras de empréstimo do Rust se aplicam a vetores, evitando problemas comuns de segurança de memória. Se você mantiver uma referência a um elemento do vetor, não poderá modificar o vetor até que essa referência saia do escopo. Isso evita situações em que as referências podem apontar para a memória desalocada após operações vetoriais, como inserir novos elementos ou limpar o vetor.


#### Mapas Hash: Armazenamento de chave-valor


Os mapas Hash fornecem um armazenamento eficiente de valores chave onde pode procurar rapidamente valores com base nas suas chaves associadas. Tanto as chaves quanto os valores podem ser de qualquer tipo, embora as chaves devam implementar as caraterísticas necessárias para comparação de hash e igualdade. Os mapas Hash assumem a propriedade dos valores inseridos, a menos que os valores implementem a caraterística Copy.


Os mapas Hash oferecem vários métodos para inserir e atualizar valores. O método básico `insert()` sobrescreverá os valores existentes, enquanto `entry()` fornece uma lógica de inserção mais flexível. A entrada API permite inserir valores apenas se eles ainda não existirem, ou atualizar valores existentes com base em seu estado atual. Este API é útil para padrões como contagem de ocorrências ou manutenção de totais em execução.


Ao recuperar valores de mapas hash, o método `get()` retorna uma `Option` já que a chave solicitada pode não existir. Você pode utilizar métodos como `copied()` para converter de `Option<&T>` para `Option<T>` para tipos Copy, e `unwrap_or()` para fornecer valores padrão quando as chaves estão faltando.


### Manipulação de strings e Unicode


As strings no Rust são codificadas em UTF-8, o que fornece suporte total ao Unicode, mas introduz complexidade em comparação com as strings simples do ASCII. O tipo `String` representa dados de texto próprios e expansíveis, enquanto as fatias de string (`&str`) fornecem visões emprestadas em dados de string. Você pode converter entre esses tipos conforme necessário, com fatias de string frequentemente usadas para parâmetros de função para aceitar tanto strings próprias quanto literais de string.


A manipulação de strings inclui métodos para anexar texto, formatar vários valores juntos e extrair substrings. O método `push_str()` anexa fatias de strings sem assumir a propriedade, enquanto a macro `format!` fornece uma maneira flexível de construir strings a partir de múltiplos componentes. Ao trabalhar com índices de strings, é preciso ter cuidado para respeitar os limites de caracteres UTF-8 para evitar panes em tempo de execução.


Para um processamento seguro caractere a caractere, as strings fornecem métodos iteradores como `chars()` para valores escalares Unicode e `bytes()` para acesso a bytes brutos. Esses iteradores lidam com a codificação UTF-8 corretamente, garantindo que você não divida acidentalmente caracteres multi-byte. Esta abordagem é mais segura e mais confiável do que a indexação manual, especialmente quando se trabalha com texto internacional que pode conter caracteres Unicode complexos.



## Sistema de tratamento de erros de duas categorias do Rust

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

O Rust adopta uma abordagem fundamentalmente diferente para o tratamento de erros em comparação com a maioria das linguagens de programação. Enquanto muitas linguagens se baseiam principalmente em exceções, o Rust distingue entre duas categorias distintas de erros e fornece mecanismos específicos para tratar cada tipo. Este capítulo explora o sistema abrangente de tratamento de erros do Rust, cobrindo tanto os erros irrecuperáveis que encerram a execução do programa quanto os erros recuperáveis que permitem que os programas continuem a ser executados graciosamente.


### Erros irrecuperáveis e pânico


Erros irrecuperáveis representam situações em que o programa entrou em um estado inconsistente ou inesperado do qual não pode se recuperar com segurança. Isso inclui cenários como acessar uma matriz fora dos limites, tentar operações que violam a segurança da memória ou encontrar condições que indicam erros lógicos fundamentais do programa. Quando esses erros ocorrem, a resposta apropriada é encerrar o programa imediatamente em vez de arriscar mais corrupção ou comportamento indefinido.


No Rust, os erros irrecuperáveis desencadeiam um pânico, o que faz com que o programa seja interrompido de forma controlada. Antes de encerrar, o Rust executa um processo chamado desenrolar, no qual ele percorre a pilha de chamadas para fornecer um rastreamento detalhado da pilha mostrando exatamente onde ocorreu o pânico. Esse processo de desenrolamento ajuda os desenvolvedores a identificar a origem do problema durante a depuração. Para aplicativos de desempenho crítico ou sistemas incorporados, é possível desativar o desenrolar e configurar o Rust para abortar imediatamente quando ocorrer uma pane, embora isso sacrifique as informações de depuração para um encerramento mais rápido.


Você pode disparar um panic explicitamente usando a macro `panic!` com uma mensagem personalizada. Quando um panic ocorre, você verá uma saída indicando qual thread entrou em panic e a mensagem associada. A definição da variável de ambiente `RUST_BACKTRACE` fornece informações adicionais de depuração, mostrando a pilha de chamadas completa que levou ao pânico. Por exemplo, ao tentar acessar o elemento 99 de um vetor contendo apenas três elementos, o generate entrará em pânico com uma mensagem "index out of bounds", juntamente com um backtrace mostrando a sequência exata de chamadas de função que resultaram no erro.


### Erros recuperáveis com resultado


Os erros recuperáveis representam condições de falha esperadas que os programas podem tratar graciosamente sem encerrar. Exemplos incluem a tentativa de abrir um arquivo que não existe, falhas de conexão de rede ou entrada inválida do usuário. Para essas situações, o Rust fornece o enum `Result`, que representa explicitamente operações que podem falhar e força os desenvolvedores a lidar com casos de sucesso e de falha.


O enum `Result` é definido com duas variantes: `Ok(T)` para operações bem sucedidas contendo um valor do tipo `T`, e `Err(E)` para falhas contendo um erro do tipo `E`. Este projeto utiliza o sistema de tipos do Rust para garantir que falhas potenciais não possam ser ignoradas. As funções que podem falhar retornam um `Result`, e o código de chamada deve explicitamente tratar tanto os casos de sucesso quanto os de erro, tipicamente utilizando correspondência de padrões com expressões `match`.


Considere a função `File::open`, que retorna um `Result<File, std::io::Error>`. Ao abrir um arquivo, você recebe um objeto `File` se for bem sucedido ou um `std::io::Error` se a operação falhar. Você pode combinar este resultado para tratar cada caso apropriadamente. No caso de sucesso, você pode prosseguir com as operações do arquivo, enquanto no caso de erro, você pode tentar criar o arquivo, tentar uma abordagem alternativa, ou propagar o erro para o código de chamada. Este tratamento explícito garante que o seu programa toma decisões conscientes sobre a recuperação de erros em vez de falhar inesperadamente.


### Padrões e atalhos para tratamento de erros


Enquanto a correspondência explícita de padrões fornece controle completo sobre o tratamento de erros, o Rust oferece vários métodos de conveniência para padrões comuns de tratamento de erros. O método `unwrap` extrai o valor de sucesso de um `Result` mas entra em pânico se um erro ocorrer, tornando-o útil para prototipagem rápida ou situações onde você está confiante que uma operação será bem sucedida. O método `expect` funciona de forma similar, mas permite que você forneça uma mensagem de pânico personalizada, tornando a depuração mais fácil quando as coisas dão errado.


Para um tratamento de erros mais flexível, métodos como `unwrap_or_else` permitem fornecer um fechamento que é executado quando ocorre um erro, permitindo uma lógica de recuperação personalizada. É possível encadear essas operações para lidar com cenários complexos, como a tentativa de abrir um arquivo e criá-lo se ele não existir, com diferentes estratégias de tratamento de erros para cada etapa.


O operador de ponto de interrogação (`?`) fornece uma sintaxe concisa para propagação de erros, que é comum em programas Rust. Quando você anexa `?` a um `Result`, ele automaticamente desembrulha os valores bem sucedidos e retorna os erros imediatamente da função atual. Este operador só pode ser utilizado em funções que retornam tipos `Result`, garantindo que os erros possam ser propagados corretamente na pilha de chamadas. O operador `?` torna o código de tratamento de erros muito mais legível, eliminando expressões de correspondência verbosas e mantendo a semântica explícita de propagação de erros.


```rust
use std::fs::File;
use std::io::{self, Read};

// Custom error type for wallet operations
#[derive(Debug)]
enum WalletError {
FileNotFound,
InvalidFormat,
InsufficientFunds,
}

// Function returning Result for recoverable errors
fn load_wallet_balance(path: &str) -> Result<u64, WalletError> {
// Simulate reading from file
let balance_str = "150000"; // Would normally read from file
balance_str
.parse::<u64>()
.map_err(|_| WalletError::InvalidFormat)
}

// Using the ? operator for clean error propagation
fn send_payment(amount: u64) -> Result<String, WalletError> {
let balance = load_wallet_balance("wallet.dat")?; // Propagates error if it fails

if balance < amount {
return Err(WalletError::InsufficientFunds);
}

Ok(format!("Sent {} sats, remaining: {}", amount, balance - amount))
}

fn main() {
// Handle the Result explicitly
match send_payment(50_000) {
Ok(msg) => println!("Success: {}", msg),
Err(WalletError::InsufficientFunds) => println!("Error: Not enough funds"),
Err(WalletError::FileNotFound) => println!("Error: Wallet file not found"),
Err(WalletError::InvalidFormat) => println!("Error: Corrupted wallet file"),
}

// Or use unwrap_or_else for custom fallback
let result = send_payment(200_000)
.unwrap_or_else(|e| format!("Payment failed: {:?}", e));
println!("{}", result);
}
```


### Propagação de erros e conceção de funções


A propagação de erros é um conceito fundamental no tratamento de erros do Rust, permitindo que as funções passem os erros para a pilha de chamadas em vez de tratá-los localmente. Ao projetar funções que podem falhar, você deve retornar tipos `Result` para dar aos chamadores a flexibilidade de decidir como tratar os erros. Esta abordagem promove o tratamento de erros compostável, onde cada função na cadeia de chamadas pode tratar os erros localmente ou passá-los para o código de nível superior que tem mais contexto para tomar decisões de recuperação.


O operador de ponto de interrogação simplifica a propagação de erros. Em vez de escrever expressões de correspondência detalhadas para cada operação potencialmente falha, é possível encadear operações com operadores `?`, criando um código legível que lida com o caminho do sucesso enquanto propaga automaticamente quaisquer erros que ocorram. Esse padrão é tão comum que muitas funções do Rust são projetadas especificamente para funcionar bem com o operador `?`, permitindo o tratamento fluente de erros em toda a sua base de código.


Ao decidir entre entrar em pânico e devolver erros, considere se o código de chamada pode razoavelmente recuperar da falha. Se uma falha representa um erro de programação ou um estado irrecuperável do sistema, entrar em pânico é apropriado. No entanto, se a falha é uma condição esperada que o código chamador pode tratar de forma diferente dependendo do contexto, retornar um `Result` fornece melhor flexibilidade e composabilidade.


### Melhores práticas e considerações de conceção


O tratamento eficaz de erros no Rust requer uma consideração cuidadosa de quando entrar em pânico versus quando retornar erros. Use panics para situações que representam erros de programação ou estados que nunca deveriam ocorrer em programas corretos, como acessar dados codificados que você sabe que são válidos. Por exemplo, analisar uma string de endereço IP codificada que você verificou estar correta pode seguramente usar `expect` com uma mensagem descritiva explicando porque a operação nunca deve falhar.


Para entradas controladas pelo utilizador ou interações com sistemas externos, prefira sempre devolver tipos `Result` em vez de entrar em pânico. Os utilizadores cometem erros, os ficheiros são apagados e as ligações de rede falham - estas são condições normais que os programas bem concebidos devem tratar graciosamente. Ao retornar erros para essas situações, você permite que o código de chamada implemente estratégias de recuperação apropriadas, seja solicitando ao usuário uma entrada diferente, voltando aos valores padrão ou exibindo mensagens de erro úteis.


Considere criar tipos personalizados que imponham a validação no momento da construção para evitar que estados inválidos se propaguem pelo programa. Por exemplo, se o seu programa requer números dentro de um intervalo específico, crie um tipo de invólucro que valide a entrada durante a construção e não forneça nenhuma maneira de criar instâncias inválidas. Essa abordagem usa o sistema de tipos do Rust para eliminar classes inteiras de erros, tornando os estados inválidos irrepresentáveis, reduzindo a necessidade de verificação de erros em tempo de execução em toda a sua base de código.


## Funcionalidades de programação funcional, fechos e ponteiros inteligentes


<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

Embora o Rust não seja uma linguagem de programação funcional pura, incorpora caraterísticas inspiradas nos paradigmas da programação funcional. Estas caraterísticas permitem aos programadores escrever código conciso, tirando partido de conceitos como fechos e iteradores. O Rust inclui esses elementos funcionais para fornecer ferramentas flexíveis para processamento de dados e mecanismos de retorno de chamada.


Os recursos de programação funcional no Rust mantêm os princípios fundamentais da linguagem de segurança de memória e abstrações de custo zero. Quando utiliza closures e iteradores, não está a sacrificar o desempenho pela expressividade - o compilador do Rust optimiza estas construções para produzir um código de máquina eficiente comparável às abordagens tradicionais baseadas em loops.


### Compreender os encerramentos


Os fechos no Rust são funções anónimas que podem capturar variáveis do seu ambiente circundante. Noutras linguagens de programação, estas são frequentemente designadas por funções lambda. A principal caraterística dos fechos é a sua capacidade de "fechar" o seu ambiente, o que significa que podem aceder e utilizar variáveis que existem no âmbito em que o fecho é definido.


A sintaxe das closures utiliza caracteres pipe (`|`) em vez de parênteses para definir parâmetros. Para uma closure sem parâmetros, você escreve `||`, e para closures com parâmetros, você os lista entre os pipes como `|x, y|`. Se o corpo da closure consistir em uma única expressão, pode-se omitir as chaves, tornando a sintaxe muito concisa.


Considere este exemplo prático de uma empresa de t-shirts que oferece t-shirts exclusivas com base nas preferências dos clientes. Se um cliente tiver especificado uma cor favorita, recebe essa cor; caso contrário, recebe a cor mais armazenada por defeito. Usando closures, essa lógica se torna: `user_preference.unwrap_or_else(|| self.most_stocked())`. A closure `|| self.most_stocked()` fornece o valor padrão apenas quando necessário, e pode acessar `self` a partir de seu ambiente.


### Inferência e flexibilidade do tipo de fecho


Um dos recursos mais convenientes do Rust com closures é a inferência automática de tipos. Ao contrário das funções regulares, onde é necessário especificar explicitamente os tipos de parâmetros e os tipos de retorno, as closures podem frequentemente inferir esses tipos a partir do contexto. O compilador analisa como a closure é usada e determina os tipos apropriados automaticamente. No entanto, quando uma closure é chamada com tipos específicos, esses tipos tornam-se fixos para essa instância da closure.


Pode armazenar fechos em variáveis como qualquer outro valor, tornando-os cidadãos de primeira classe na linguagem. Quando você atribui uma closure a uma variável, você pode chamá-la mais tarde usando parênteses: `let my_closure = |x| x + 1; let result = my_closure(5);`. Essa flexibilidade permite passar closures como argumentos para funções, retorná-los de funções e usá-los em estruturas de dados.


Se o compilador não puder inferir tipos ou se você quiser ser explícito, você pode anotar parâmetros de fechamento e tipos de retorno usando sintaxe similar a funções: `|x: i32| -> i32 { x + 1 }`. Esta tipagem explícita é por vezes necessária em cenários complexos onde o compilador precisa de informação adicional para resolver os tipos corretamente.


### Capturando variáveis de ambiente


As closures podem capturar variáveis de seu ambiente de três maneiras diferentes: por referência imutável, por referência mutável ou assumindo a propriedade. O compilador do Rust determina automaticamente o método de captura mais restritivo que satisfaz as necessidades da sua closure, seguindo o princípio do menor privilégio.


Quando uma closure só precisa de ler um valor, captura-o através de uma referência imutável. Isto permite que a variável original permaneça acessível depois de a closure ser definida e chamada. Por exemplo, um fecho que imprime uma lista irá emprestar a lista de forma imutável, permitindo-lhe continuar a utilizar a lista após a execução do fecho.


Se uma closure precisar de modificar uma variável capturada, deve capturá-la através de uma referência mutável. Neste caso, tanto a variável capturada como o próprio fecho devem ser declarados como mutáveis. O fecho pode então modificar a variável capturada, mas as regras de empréstimo continuam a aplicar-se - não pode ter outras referências a essa variável enquanto o fecho mutável existir.


O método de captura mais restritivo é a apropriação, que move as variáveis capturadas para dentro da closure. Isso é necessário quando a closure pode sobreviver ao escopo onde as variáveis foram originalmente definidas, como ao gerar threads. Você pode forçar a captura de propriedade utilizando a palavra-chave `move` antes dos parâmetros da closure: `move |x| { /* corpo da closure */ }`. Isso é essencial para a segurança das threads, já que as threads não podem pegar emprestado de outras threads que podem terminar e descartar suas variáveis.


### Caraterísticas do fecho e tipos de funções


O Rust representa closures através de um sistema de caraterísticas com três caraterísticas principais: `FnOnce`, `FnMut` e `Fn`. Essas caraterísticas formam uma hierarquia que descreve como as closures podem ser chamadas e o que elas podem fazer com as variáveis capturadas.


`FnOnce` é a caraterística mais básica que todas as closures implementam. Ele representa closures que podem ser chamados pelo menos uma vez. Algumas closures, particularmente aquelas que movem valores capturados ou os consomem de alguma forma, só podem ser chamadas uma vez porque elas destroem ou movem seus dados capturados durante a execução.


`FnMut` representa closures que podem ser chamadas várias vezes e podem alterar seu ambiente capturado. Essas closures capturam variáveis por referência mutável e podem modificá-las através de múltiplas chamadas. As regras de empréstimo garantem que quando uma closure `FnMut` está ativa, ela tem acesso mutável exclusivo às suas variáveis capturadas.


`Fn` é a caraterística mais restritiva, representando closures que podem ser chamadas várias vezes sem alterar o ambiente capturado. Essas closures apenas capturam por referência imutável e podem ser chamadas concorrentemente sem violar as garantias de segurança do Rust. Se uma closure implementa `Fn`, ela automaticamente implementa `FnMut` e `FnOnce` também, já que ser chamável múltiplas vezes sem mutação implica ser chamável com mutação e ser chamável uma vez.


### Trabalhar com Iteradores


Os iteradores no Rust fornecem uma forma de processar sequências de dados. São preguiçosos, o que significa que não realizam qualquer trabalho até que os consuma chamando métodos que efetivamente iteram através dos dados. Esta avaliação preguiçosa permite o encadeamento eficiente de operações sem criar colecções intermédias.


A caraterística `Iterator` define a funcionalidade principal com um tipo associado `Item` que representa o que o iterador produz, e um método `next` que retorna `Option<Self::Item>`. Quando `next` retorna `None`, o iterador está esgotado. Este projeto permite que iteradores representem sequências finitas e potencialmente infinitas de forma segura.


Você pode criar iteradores a partir de coleções utilizando métodos como `iter()` para emprestar iteração, `iter_mut()` para emprestar iteração mutável, e `into_iter()` para consumir iteração. A escolha entre esses métodos depende da necessidade de modificar elementos e de consumir a coleção original.


### Adaptadores e consumidores de iteradores


Os adaptadores de iteradores são métodos que transformam um iterador em outro, permitindo encadear operações. Adaptadores comuns incluem `map` para transformar cada elemento, `filter` para selecionar elementos baseados em um predicado, e `enumerate` para adicionar índices. Esses adaptadores são preguiçosos - eles não fazem nenhum trabalho até que sejam consumidos.


O método `map` aplica um fechamento a cada elemento, transformando-o em outra coisa. Por exemplo, `numbers.iter().map(|x| x * 2)` cria um iterador que duplica cada número. O método `filter` mantém apenas os elementos para os quais o fechamento do predicado retorna verdadeiro: `numbers.iter().filter(|&x| x > 10)` mantém apenas os números maiores que dez.


Os métodos de consumo realmente iteram através dos dados e produzem um resultado final. O método `collect` consome um iterador e cria uma coleção a partir dele. Muitas vezes é necessário especificar o tipo de coleção: `let vec: Vec<_> = iterator.collect()`. Outros consumidores incluem `sum` para adicionar elementos numéricos, `fold` para acumular valores com uma operação personalizada, e `for_each` para executar efeitos colaterais em cada elemento.


### Padrões avançados de iteradores


Operações adicionais de iteradores incluem `zip` para combinar dois iteradores por elemento, `chain` para concatenar iteradores, e `filter_map` para combinar filtragem e mapeamento em uma única operação. O método `zip` cria pares a partir de elementos correspondentes de dois iteradores: `a.iter().zip(b.iter())` produz tuplas `(a[0], b[0]), (a[1], b[1]), ...`.


O método `fold` é útil para acumular valores. Ele recebe um valor inicial e um fechamento que combina o acumulador com cada elemento: `numbers.iter().fold(0, |acc, x| acc + x)` soma todos os números. Este padrão pode implementar muitas outras operações como encontrar valores máximos, construir strings ou criar estruturas de dados complexas.


As cadeias de iteradores podem exprimir transformações de dados complexas de forma concisa. Por exemplo, o processamento de dados de áudio pode envolver: `coefficients.iter().zip(buffer.iter()).map(|(c, b)| c * b).sum::<i32>() >> 12`. Isto multiplica os coeficientes correspondentes e os valores do buffer, soma os resultados e desloca o valor final, tudo numa única expressão legível.


```rust
fn main() {
// Sample UTXOs: (txid_suffix, amount_sats)
let utxos = vec![
("a1b2", 50_000u64),
("c3d4", 15_000),
("e5f6", 100_000),
("g7h8", 3_000),
("i9j0", 75_000),
];

// Using closures and iterators to process UTXOs

// 1. Filter UTXOs above dust threshold (10,000 sats)
let spendable: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000)
.collect();
println!("Spendable UTXOs: {:?}", spendable);

// 2. Calculate total balance with fold
let total_balance: u64 = utxos
.iter()
.map(|(_, amount)| amount)
.fold(0, |acc, amount| acc + amount);
println!("Total balance: {} sats", total_balance);

// 3. Find UTXOs needed to cover a 120,000 sat payment
let target = 120_000u64;
let mut accumulated = 0u64;
let selected: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000) // Skip dust
.take_while(|(_, amount)| {
if accumulated >= target {
false
} else {
accumulated += amount;
true
}
})
.collect();
println!("Selected for payment: {:?}", selected);

// 4. Transform to display format using map and collect
let display_strings: Vec<String> = utxos
.iter()
.map(|(txid, amount)| format!("{}...:{} sats", txid, amount))
.collect();
println!("Display: {:?}", display_strings);
}
```


### Introdução aos ponteiros inteligentes


Os ponteiros inteligentes são estruturas de dados que actuam como os ponteiros tradicionais, mas fornecem capacidades adicionais e gestão automática da memória. Ao contrário das referências simples, os ponteiros inteligentes possuem os dados para os quais apontam e podem implementar um comportamento personalizado para padrões de alocação, desalocação e acesso à memória. Eles são ferramentas essenciais para gerenciar dados alocados em heap e implementar padrões complexos de propriedade que vão além do sistema básico de propriedade do Rust.


O aspeto "inteligente" vem da sua capacidade de tratar automaticamente tarefas de gestão de memória que, de outra forma, exigiriam intervenção manual. Quando um ponteiro inteligente sai do âmbito, pode libertar automaticamente a memória associada, diminuir as contagens de referência ou efetuar outras operações de limpeza. Esta automatização ajuda a evitar fugas de memória e erros de utilização após a libertação, ao mesmo tempo que proporciona mais flexibilidade do que a alocação apenas a pilhas.


Os ponteiros inteligentes normalmente implementam duas caraterísticas principais: `Deref` e `Drop`. A caraterística `Deref` permite que o ponteiro inteligente seja utilizado como se fosse uma referência aos dados contidos. A caraterística `Drop` permite uma lógica de limpeza personalizada quando o ponteiro inteligente é destruído. Juntas, essas caraterísticas permitem que os ponteiros inteligentes gerenciem a memória automaticamente.


### O ponteiro inteligente da caixa


`Box<T>` é o ponteiro inteligente mais simples, fornecendo alocação na pilha para qualquer tipo `T`. Quando você cria uma `Box`, o valor contido é armazenado no heap ao invés da pilha, e a própria `Box` (que é apenas um ponteiro) é armazenada na pilha. Esta indireção é útil quando se precisa armazenar grandes quantidades de dados sem movê-los, quando se precisa de um tipo com tamanho desconhecido em tempo de compilação, ou quando se quer transferir a propriedade de dados da heap eficientemente.


Criar uma `Box` é simples: `let valor_da_caixa = Box::new(42);` aloca um inteiro no heap. O `Box` gerencia automaticamente esta memória - quando o `Box` sai do escopo, ele automaticamente desaloca a memória do heap. Esta limpeza automática previne vazamentos de memória sem requerer gerenciamento manual de memória.


Um dos casos de uso mais importantes para `Box` é permitir estruturas de dados recursivas. Considere uma lista ligada onde cada nó contém um valor e um ponteiro para o próximo nó. Sem `Box`, não é possível definir tal estrutura porque o compilador não pode determinar o tamanho de um tipo que contém a si mesmo. Ao utilizar `Box<Nodo>` para o próximo ponteiro, você quebra o problema de dimensionamento recursivo porque `Box` tem um tamanho fixo e conhecido, independentemente do que ele contém.


### Implementando a caraterística Deref


A caraterística `Deref` permite que um tipo seja desreferenciado utilizando o operador `*`, fazendo com que os ponteiros inteligentes se comportem como referências aos seus dados contidos. Quando você implementa `Deref` para um ponteiro inteligente, você habilita a desreferência automática que torna o ponteiro inteligente transparente para uso. Isso significa que você pode chamar métodos no tipo contido diretamente através do smart pointer sem desreferenciamento explícito.


A caraterística `Deref` define um tipo associado `Target` que especifica o tipo de referência que a operação de dereferência deve produzir. A caraterística requer a implementação de um método `deref` que retorna uma referência para o tipo alvo. Para `Box<T>`, a implementação retorna uma referência para o valor `T` contido.


O Rust realiza coerção automática de deref, o que significa que o compilador pode inserir automaticamente chamadas para `deref` quando necessário para tornar os tipos compatíveis. É por isso que você pode passar uma `String` para uma função que espera uma `&str` - o compilador automaticamente dereferencia a `String` para obter uma fatia de string. Esta coerção pode encadear múltiplos níveis, de modo que uma `Box<String>` pode ser automaticamente convertida para uma `&str` através de múltiplas operações de deref.


### Implementação de gotas personalizadas


A caraterística `Drop` permite especificar um código de limpeza personalizado que é executado quando um valor sai do escopo. Isso é particularmente importante para ponteiros inteligentes que gerenciam recursos além da memória simples, como manipuladores de arquivos, conexões de rede ou contagens de referência. A caraterística `Drop` tem um único método, `drop`, que recebe uma referência mutável para `self` e executa a limpeza.


A maioria dos tipos não precisa de implementações personalizadas de `Drop` porque o Rust lida automaticamente com a eliminação de seus campos. No entanto, ponteiros inteligentes muitas vezes precisam de lógica personalizada para limpar adequadamente os recursos que gerenciam. Por exemplo, um ponteiro inteligente com contagem de referência precisa diminuir a contagem de referência e potencialmente desalocar dados compartilhados quando a última referência é descartada.


Você também pode explicitamente descartar um valor antes que ele saia do escopo utilizando `std::mem::drop()`. Essa função assume a propriedade de um valor e o descarta imediatamente, o que pode ser útil para liberar recursos mais cedo ou garantir que a limpeza aconteça em um ponto específico do seu programa. A função drop explícita é apenas uma função de identidade que assume a propriedade - o trabalho real acontece quando o valor é descartado no final da função.


Essa base de fechamentos, iteradores e ponteiros inteligentes fornece aos desenvolvedores do Rust ferramentas para escrever código expressivo, seguro e eficiente. Esses recursos trabalham juntos para permitir padrões de programação comuns, mantendo as garantias centrais do Rust de segurança de memória e desempenho.



## Contagem de referências e mutabilidade interior

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

### Contagem de referências com RC


A contagem de referências representa outro tipo fundamental de ponteiro inteligente no Rust, concebido especificamente para permitir cenários de propriedade múltipla. Ao contrário do Box, que segue as regras tradicionais de propriedade única, em que uma entidade é proprietária dos dados, o RC (Reference Counter) permite que várias partes do seu código partilhem a propriedade dos mesmos dados em simultâneo. Este modelo de propriedade partilhada funciona através de um mecanismo de contagem que regista o número de referências existentes a uma determinada parte dos dados.


O sistema de contagem de referências funciona através da manutenção de um contador interno que aumenta sempre que se clona uma RC e diminui quando uma RC é abandonada. A memória só é libertada quando este contador chega a zero, garantindo que os dados permanecem válidos enquanto existir qualquer referência. Esta abordagem evita a desalocação prematura e permite padrões flexíveis de partilha de dados que seriam impossíveis com a simples propriedade de caixa.


Um exemplo prático em que RC é útil envolve a criação de estruturas de dados partilhadas, como listas ligadas, em que várias listas podem fazer referência à mesma parte da cauda. Considere a tentativa de criar duas listas separadas que referenciam uma subsequência comum. Com a propriedade Box, isso se torna impossível porque mover a parte compartilhada para a primeira lista transfere a propriedade, impedindo seu uso na segunda lista. RC resolve isso permitindo clonar a referência ao invés dos dados subjacentes, tornando a estrutura compartilhada possível enquanto mantém a segurança da memória.


Quando se clona um RC, não se está a duplicar os dados internos, independentemente do seu tamanho ou complexidade. Em vez disso, está a criar outra referência para a mesma localização de memória e a incrementar o contador de referência. Isso faz com que a clonagem de instâncias RC seja eficiente mesmo para estruturas de dados grandes, já que apenas a referência em si é copiada, enquanto os dados subjacentes permanecem no lugar.


### Mutabilidade interior com RefCell


RefCell introduz a mutabilidade interior, que permite alterar dados mesmo quando se tem apenas uma referência imutável a eles. Essa capacidade muda fundamentalmente a forma como as regras de empréstimo do Rust são aplicadas, movendo as verificações do tempo de compilação para o tempo de execução. Enquanto as referências normais dependem do compilador para verificar a segurança do empréstimo, a RefCell realiza essas verificações durante a execução do programa, proporcionando maior flexibilidade ao custo de possíveis panes em tempo de execução.


O princípio central por trás da RefCell envolve manter as mesmas regras de empréstimo que o Rust normalmente impõe em tempo de compilação, mas verificando-as dinamicamente. A qualquer momento, é possível ter uma referência mutável ou qualquer número de referências imutáveis para os dados dentro de uma RefCell. Se o seu código tentar violar essas regras criando empréstimos conflitantes simultaneamente, o programa entrará em pânico em vez de produzir um comportamento indefinido.


Esta verificação em tempo de execução permite certos padrões de programação que o compilador pode rejeitar mesmo quando são realmente seguros. A análise estática do compilador nem sempre pode provar que os padrões de empréstimo complexos estão corretos, levando-o a errar por precaução. O RefCell permite que você substitua essas restrições conservadoras quando estiver confiante na correção do seu código, mas essa confiança vem com a responsabilidade de garantir o uso adequado para evitar falhas em tempo de execução.


Um caso de uso comum para RefCell envolve objetos de simulação em cenários de teste. Ao implementar uma caraterística que fornece apenas acesso imutável a si mesmo, mas sua implementação de simulação precisa rastrear alterações de estado internamente, o RefCell permite esse padrão. É possível envolver o estado interno em uma RefCell, permitindo que a simulação altere seus dados de rastreamento mesmo por meio de uma interface imutável.


### Combinação de RC e RefCell para estado mutável partilhado


A combinação de RC e RefCell cria um padrão para estado mutável partilhado, onde vários proprietários podem potencialmente modificar os mesmos dados. RC fornece a capacidade de propriedade compartilhada, enquanto RefCell permite a mutação através de referências imutáveis. Essa combinação é útil em cenários como estruturas de grafos, caches ou qualquer situação em que várias partes do seu programa precisam de acesso de leitura e gravação a dados compartilhados.


Quando você envolve uma RefCell dentro de uma RC, você cria uma estrutura que pode ser clonada e distribuída pelo seu programa, com cada clone fornecendo acesso aos mesmos dados mutáveis subjacentes. Todos os proprietários podem potencialmente modificar os dados usando o método borrow_mut da RefCell, mas eles ainda devem respeitar as regras de empréstimo em tempo de execução. Este padrão permite cenários complexos de partilha de dados, mantendo as garantias de segurança do Rust através de verificações em tempo de execução.


No entanto, essa flexibilidade vem com ressalvas importantes em relação a vazamentos de memória e ciclos de referência. Ao usar RC com RefCell, torna-se possível criar acidentalmente referências circulares onde as estruturas de dados referenciam a si mesmas, seja diretamente ou através de uma cadeia de referências. Estes ciclos impedem que a contagem de referências chegue a zero, causando fugas de memória porque os dados parecem ter sempre referências activas, mesmo quando já não estão acessíveis a partir do resto do programa.


A solução para os ciclos de referência envolve a utilização de referências fracas, que não contribuem para a contagem de referências utilizada para as decisões de gestão da memória. As referências fracas permitem-lhe manter ligações entre estruturas de dados sem as manter activas, quebrando potenciais ciclos e preservando a capacidade de aceder a dados relacionados quando estes ainda existem.


```rust
use std::rc::Rc;
use std::cell::RefCell;

// Simulating a channel state that multiple components need to access and modify
#[derive(Debug)]
struct ChannelState {
channel_id: String,
local_balance_msat: u64,
remote_balance_msat: u64,
is_active: bool,
}

fn main() {
// Rc<RefCell<T>> allows multiple owners with interior mutability
let channel = Rc::new(RefCell::new(ChannelState {
channel_id: "abc123".to_string(),
local_balance_msat: 1_000_000_000,  // 1M sats in msats
remote_balance_msat: 500_000_000,
is_active: true,
}));

// Clone Rc to share ownership (cheap - only increments counter)
let channel_for_ui = Rc::clone(&channel);
let channel_for_router = Rc::clone(&channel);

// Reference count is now 3
println!("Reference count: {}", Rc::strong_count(&channel));

// UI component reads the state (immutable borrow)
{
let state = channel_for_ui.borrow();
println!("UI shows balance: {} msats", state.local_balance_msat);
} // borrow ends here

// Router updates the state after a payment (mutable borrow)
{
let mut state = channel_for_router.borrow_mut();
state.local_balance_msat -= 100_000_000; // Sent 100k sats
state.remote_balance_msat += 100_000_000;
println!("Router updated balances");
} // mutable borrow ends here

// Original reference can still read the updated state
let state = channel.borrow();
println!("New local balance: {} msats", state.local_balance_msat);

// WARNING: This would panic at runtime!
// let borrow1 = channel.borrow();
// let borrow2 = channel.borrow_mut(); // PANIC: already borrowed
}
```


### Fundamentos de segurança e simultaneidade de threads


A abordagem do Rust para concorrência é centrada na prevenção de corridas de dados e problemas de segurança de memória em tempo de compilação. O sistema de tipos reforça a segurança de threads através de caraterísticas como `Send` e `Sync`, que marcam os tipos como seguros para transferência entre threads ou seguros para acesso concorrente, respetivamente. Esta verificação em tempo de compilação detecta muitos bugs de concorrência que só apareceriam em tempo de execução noutras linguagens de programação de sistemas.


A criação de threads no Rust segue um padrão simples usando thread::spawn, que recebe uma closure para executar na nova thread e retorna um handle para gerenciar o ciclo de vida da thread. A thread gerada é executada simultaneamente com a thread principal, e você pode usar o método join no manipulador para aguardar a conclusão. Sem junção explícita, as threads geradas podem ser encerradas quando a thread principal sair, potencialmente interrompendo o trabalho incompleto.


A palavra-chave move se torna crucial quando se trabalha com threads porque os closures passados para threads geradas frequentemente precisam possuir seus dados em vez de pegá-los emprestados. Como as threads geradas podem sobreviver ao escopo que as criou, pegar emprestado do escopo pai cria potenciais violações de tempo de vida. Mover os dados para a closure da thread transfere a propriedade, garantindo que os dados permaneçam válidos por todo o tempo de vida da thread, enquanto impede o acesso do escopo original.


A passagem de mensagens fornece uma alternativa à simultaneidade de estado partilhado através de canais que permitem que as threads comuniquem enviando dados em vez de partilharem memória. A biblioteca padrão do Rust fornece canais MPSC (Multiple Producer Single Consumer), onde vários threads podem enviar mensagens para um único thread recetor. Este padrão elimina muitos problemas de sincronização, evitando totalmente o estado mutável compartilhado, confiando na troca de mensagens para coordenação.


### Concorrência de estados partilhados com Mutex e Arc


Quando a passagem de mensagens não é adequada, o Rust fornece a concorrência tradicional de estado partilhado através do Mutex (exclusão mútua) combinado com o Arc (Atomic Reference Counter). O Mutex assegura que apenas uma thread pode aceder a dados protegidos de cada vez, exigindo que as threads adquiram um bloqueio antes de acederem aos dados. O bloqueio é libertado automaticamente quando o objeto de guarda devolvido pela operação de bloqueio sai do âmbito, evitando cenários comuns de bloqueio causados por desbloqueios esquecidos.


O Arc funciona como o equivalente thread-safe do RC, utilizando operações atómicas para gerir a contagem de referências com segurança em vários threads. Embora o RC funcione perfeitamente para cenários de thread único, a sua contagem de referência não atómica cria condições de corrida quando acedida a partir de vários threads. Os contadores atómicos do Arc garantem que as modificações da contagem de referências ocorrem em segurança, mesmo com acesso simultâneo, tornando-o adequado para a partilha de dados entre threads.


A combinação de Arc e Mutex cria um padrão para estado mutável compartilhado em programas concorrentes. Ao envolver um Mutex em um Arc, é possível clonar o Arc para distribuir o acesso ao mesmo mutex em vários threads, com cada thread capaz de adquirir o bloqueio e modificar os dados protegidos com segurança. Este padrão fornece a flexibilidade do estado partilhado enquanto mantém as garantias de segurança do Rust através da verificação em tempo de compilação e bloqueio em tempo de execução.


As caraterísticas Send e Sync funcionam nos bastidores para garantir a segurança do thread em tempo de compilação. Send indica que um tipo pode ser transferido com segurança para outro thread, enquanto Sync indica que as referências a um tipo podem ser compartilhadas com segurança entre threads. A maioria dos tipos implementa automaticamente essas caraterísticas quando seus componentes são thread-safe, mas alguns tipos, como RC e RefCell, não as implementam explicitamente porque não foram projetados para acesso simultâneo. Essa implementação automática de caraterísticas evita a introdução acidental de violações de segurança de thread, permitindo que tipos seguros funcionem perfeitamente em contextos simultâneos.


## Compreender as macros Rust

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::

### Introdução às macros no Rust


As macros no Rust são uma funcionalidade de metaprogramação que permite aos programadores escrever código que gera outro código em tempo de compilação. Ao contrário das funções, que são chamadas em tempo de execução, as macros são expandidas no início do processo de compilação, antes da verificação de tipos e das fases posteriores. Essa distinção fundamental torna as macros particularmente úteis para reduzir a repetição de código e criar linguagens específicas de domínio nos programas Rust.


O indicador mais reconhecível de uma chamada de macro é o ponto de exclamação (!) que segue o nome da macro. Por exemplo, ao utilizar `println!("Olá, mundo!")`, não está a chamar uma função mas a invocar uma macro. Esta macro se expande em um código mais complexo que lida com as operações de formatação e saída. O ponto de exclamação serve como um sinal visual para os desenvolvedores de que a geração de código em tempo de compilação está ocorrendo em vez de uma chamada de função padrão.


O Rust fornece três tipos distintos de macros, cada uma servindo diferentes propósitos no ecossistema da linguagem:



- Macros do tipo função**: Assemelham-se a chamadas de função, mas operam em tempo de compilação (por exemplo, `vec!`, `println!`)
- Derivar macros**: Implementa automaticamente caraterísticas para tipos (por exemplo, `#[derive(Debug, Clone)]`)
- Macros do tipo atributo**: Modificam o comportamento dos elementos de código aos quais são aplicadas (por exemplo, `#[test]`, `#[tokio::main]`)


A compreensão destes diferentes tipos de macros é essencial para uma programação eficaz do Rust, uma vez que cada um aborda casos de utilização e padrões de programação específicos.


### Tipos de macros e suas aplicações


As macros do tipo função representam o tipo de macro mais comummente encontrado na programação Rust. Essas macros usam sintaxe semelhante às chamadas de função, mas executam a correspondência de padrões em sua entrada para o código apropriado do generate. A macro `vec!` é um exemplo comum dessa categoria, permitindo que os desenvolvedores criem e inicializem vetores com uma sintaxe concisa. Quando você escreve `vec![1, 2, 3, 4]`, a macro expande isso em código que cria um novo vetor, empurra cada elemento individualmente e retorna o vetor completo.


As macros Derive fornecem implementações automáticas de trait para tipos personalizados, reduzindo significativamente o código boilerplate. Quando você adiciona `#[derive(Debug)]` a uma definição de struct ou enum, você está instruindo o compilador para generate uma implementação completa da caraterística Debug para esse tipo. Essa implementação gerada lida com a lógica de formatação necessária para exibir o conteúdo do tipo em um formato legível por humanos. O mecanismo de derivação suporta várias caraterísticas de biblioteca padrão, incluindo Clone, PartialEq, tornando-o uma ferramenta comumente usada para reduzir o boilerplate.


As macros do tipo atributo modificam o comportamento dos elementos de código que anotam, fornecendo uma forma de adicionar metadados ou alterar o comportamento de compilação. Essas macros aparecem como atributos colocados acima de definições de tipos, funções ou outras construções de código. Por exemplo, o atributo `#[non_exhaustive]` em um enum indica que variantes adicionais podem ser adicionadas em versões futuras, exigindo que as expressões de correspondência incluam um caso padrão. Este mecanismo garante compatibilidade futura enquanto fornece documentação clara do potencial de evolução do tipo.


### Criando macros personalizadas semelhantes a funções


A escrita de macros personalizadas do tipo função envolve a compreensão da sintaxe de correspondência de padrões do Rust para definições de macros. A definição de macro utiliza uma abordagem declarativa onde o utilizador especifica padrões que correspondem a diferentes formas de entrada e modelos de geração de código correspondentes. Cada macro pode conter várias ramificações, permitindo-lhe lidar com vários padrões de entrada e gerar código apropriado para cada caso.


Considere criar uma macro de vetor personalizada que demonstre os princípios fundamentais da construção de macros. A definição da macro começa com `macro_rules!` seguida pelo nome da macro e uma série de ramificações de correspondência de padrões. Cada ramo consiste em um padrão que corresponde a uma sintaxe de entrada específica e um modelo de código que gera o código Rust correspondente. Por exemplo, um ramo simples pode corresponder a colchetes vazios `[]` e código generate para criar um vetor vazio, enquanto outro ramo corresponde a uma única expressão e gera código para criar um vetor com um elemento.


As macros tornam-se particularmente úteis ao implementar padrões de argumentos variáveis usando a sintaxe de repetição. O padrão `$($x:expr),*` corresponde a zero ou mais expressões separadas por vírgulas, permitindo que a macro manipule um número arbitrário de argumentos. O modelo de geração de código correspondente utiliza `$(vec.push($x);)*` para iterar sobre todas as expressões correspondentes e generate instruções push individuais para cada uma delas. Este mecanismo de repetição permite que as macros generate gerem código que seria impossível ou extremamente verboso de escrever manualmente.


```rust
// A macro to create a HashMap with Bitcoin-related data
macro_rules! btc_map {
// Empty case
() => {
std::collections::HashMap::new()
};
// Key-value pairs case
($($key:expr => $value:expr),+ $(,)?) => {
{
let mut map = std::collections::HashMap::new();
$(
map.insert($key, $value);
)+
map
}
};
}

// A macro for logging with context (simulating a derive-like pattern)
macro_rules! log_payment {
($level:ident, $($arg:tt)*) => {
println!(
"[{}] [PAYMENT] {}",
stringify!($level).to_uppercase(),
format!($($arg)*)
)
};
}

fn main() {
// Using the btc_map! macro
let fee_rates = btc_map! {
"high_priority" => 50_u64,    // sats/vbyte
"medium" => 25_u64,
"low" => 10_u64,
};

println!("Fee rates: {:?}", fee_rates);

// Using the log_payment! macro
log_payment!(info, "Sending {} sats to {}", 100_000, "bc1q...");
log_payment!(warn, "Fee rate {} sats/vB is above average", 75);
log_payment!(error, "Payment failed: insufficient funds");

// Standard vec! macro usage comparison
let utxos = vec![50_000_u64, 30_000, 20_000];
let total: u64 = utxos.iter().sum();
println!("Total UTXOs: {} sats", total);
}
```


O processo de compilação transforma as chamadas de macro em código expandido antes de ocorrer a verificação do tipo e a otimização. Quando o compilador encontra uma invocação de macro, compara a entrada com os padrões definidos e substitui a chamada de macro pelo código gerado. Este código expandido passa então pelos processos normais de compilação, incluindo verificação de tipo e otimização. Ferramentas como `cargo expand` permitem que os desenvolvedores inspecionem o código gerado, fornecendo recursos valiosos de depuração ao desenvolver macros complexas.


### Conceitos avançados de macro e depuração


O desenvolvimento de macros requer a compreensão da distinção entre tempo de compilação e execução em tempo de execução. As macros são executadas durante a compilação, gerando código que será executado em tempo de execução. Esta separação temporal significa que a lógica da macro não pode depender de valores em tempo de execução, mas também permite optimizações em que os cálculos complexos podem ser efectuados uma vez durante a compilação em vez de repetidamente durante a execução.


O sistema de correspondência de padrões em macros suporta vários especificadores de fragmentos que definem que tipo de elementos de código podem ser correspondidos. O especificador `expr` corresponde a expressões, `ty` corresponde a tipos, `ident` corresponde a identificadores, e vários outros fornecem controle refinado sobre a validação de entrada. Esses especificadores garantem que as macros recebam entradas sintaticamente válidas e fornecem mensagens de erro claras quando uma sintaxe inválida é encontrada.


A depuração de macros apresenta desafios únicos devido à sua natureza de tempo de compilação. O comando `cargo expand` é útil para o desenvolvimento de macros, pois exibe o código totalmente expandido gerado por invocações de macros. Essa ferramenta permite que os desenvolvedores verifiquem se suas macros generate o código pretendido e identifiquem problemas na lógica de expansão. Quando o código gerado pela macro contém erros, a saída expandida ajuda a identificar se o problema está na definição da macro ou na estrutura do código gerado.


As macros complexas podem implementar padrões recursivos, em que uma macro se chama a si própria com argumentos modificados para lidar com a geração de código aninhado ou iterativo. No entanto, as macros recursivas requerem um design cuidadoso para evitar expansão infinita e problemas de desempenho de compilação. A natureza em tempo de compilação da expansão de macros significa que mesmo implementações de macros ineficientes apenas afectam a velocidade de compilação, não o desempenho em tempo de execução, mas macros excessivamente complexas podem abrandar significativamente o processo de compilação.



# Rust E Bitcoin

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Porquê o Rust para o desenvolvimento do Bitcoin

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


A escolha do Rust para o desenvolvimento do Bitcoin e do Lightning não é casual. O desenvolvimento do Bitcoin acarreta responsabilidades únicas que o distinguem do desenvolvimento de software normal. Ao trabalhar com o Bitcoin, os programadores lidam frequentemente com fundos de utilizadores num ambiente em que os erros podem ser irreversíveis. Ao contrário dos sistemas financeiros tradicionais com proteções regulatórias e mecanismos de estorno, a natureza descentralizada do Bitcoin significa que, uma vez que uma [transação](https://planb.academy/resources/glossary/transaction-tx) é transmitida, não há autoridade a quem apelar para a recuperação de fundos. Esta realidade exige um maior nível de responsabilidade e precisão no desenvolvimento de software.


A filosofia "avançar rapidamente e partir as coisas" que funciona em muitos sectores tecnológicos simplesmente não se aplica ao desenvolvimento do Bitcoin. Em vez disso, o ecossistema requer linguagens e ferramentas que ajudem os programadores a criar software robusto e seguro, em que as falhas são evitadas ou tratadas de forma graciosa. É por isso que muitos projectos Bitcoin proeminentes gravitaram em torno do Rust, incluindo o Kit de Desenvolvimento Bitcoin (BDK), o Kit de Desenvolvimento Lightning (LDK) e o BreezSDK.


O Rust oferece três propriedades essenciais que o tornam particularmente adequado para o desenvolvimento do Bitcoin: um sistema estático de tipos fortes, ferramentas modernas e ricas e compatibilidade entre plataformas. Cada uma destas caraterísticas contribui para a capacidade da linguagem de ajudar os programadores a escrever código mais seguro e fiável para lidar com operações de [criptomoeda](https://planb.academy/resources/glossary/cryptocurrency).


### Sistema de tipo estático forte do Rust


O sistema de tipos do Rust fornece caraterísticas de tipagem estática e forte que trabalham em conjunto para detetar erros antes que estes possam afetar os utilizadores. A natureza estática significa que a verificação de tipos ocorre em tempo de compilação, exigindo que os programadores resolvam as incompatibilidades de tipos antes mesmo de o programa poder ser construído. Isto contrasta com as linguagens tipadas dinamicamente, em que os erros de tipo só aparecem durante o tempo de execução, potencialmente depois de o software ter sido implementado e estar a tratar de fundos reais dos utilizadores.


A força do sistema de tipos do Rust refere-se à sua expressividade e rigor na modelação de problemas. Ao contrário das linguagens com sistemas de tipos mais fracos, como o C, em que os programadores estão limitados a tipos básicos como números e structs, o Rust permite uma modelação de tipos rica que pode representar conceitos de domínio complexos com precisão. Por exemplo, é possível criar tipos que distinguem entre diferentes tipos de listas ou impor que determinadas operações só sejam executadas em tipos de objectos específicos.


O que torna o sistema de tipos do Rust relevante para o desenvolvimento do Bitcoin é a sua abordagem à segurança da memória. O mesmo sistema de tipos que modela a lógica empresarial também lida com a propriedade da memória e o controlo de acesso partilhado. Essa dupla responsabilidade significa que classes comuns de vulnerabilidades, como vazamentos de memória, erros de duplo livre e condições de corrida, são eliminadas inteiramente pelo compilador. O sistema de tipos impõe estas garantias de segurança através de conceitos como propriedade, empréstimo e contagem de referências, tornando extremamente difícil a introdução de erros relacionados com a memória que possam comprometer a segurança ou a estabilidade.


```rust
// Example: Type-safe Bitcoin amount handling
// Using newtypes to prevent mixing up satoshis and other values

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Satoshis(u64);

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct FeeRate(u64); // sats per vbyte

impl Satoshis {
fn from_btc(btc: f64) -> Self {
Satoshis((btc * 100_000_000.0) as u64)
}

fn as_btc(&self) -> f64 {
self.0 as f64 / 100_000_000.0
}
}

// Calculate fee given tx size - type system ensures we can't mix up values
fn calculate_fee(tx_size_vbytes: u32, rate: FeeRate) -> Satoshis {
Satoshis(tx_size_vbytes as u64 * rate.0)
}

fn main() {
let payment = Satoshis::from_btc(0.001); // 100,000 sats
let fee_rate = FeeRate(25);              // 25 sats/vbyte
let tx_size = 250_u32;                   // vbytes

let fee = calculate_fee(tx_size, fee_rate);
println!("Payment: {:?} ({} BTC)", payment, payment.as_btc());
println!("Fee: {:?}", fee);

// This would NOT compile - type safety prevents mixing values:
// let bad_fee = calculate_fee(tx_size, payment); // ERROR: expected FeeRate, found Satoshis
}
```


### Ferramentas modernas e suporte multiplataforma


O ecossistema de ferramentas do Rust fornece aos programadores ferramentas que ajudam na produtividade e na qualidade do código. O próprio compilador Rust foi concebido não só para traduzir código para a forma binária, mas também para servir como uma ferramenta educacional que ajuda os programadores a aprender e a melhorar. Quando ocorrem erros de compilação, o compilador fornece explicações detalhadas sobre o que correu mal e sugere frequentemente correcções específicas. Esta abordagem é particularmente valiosa para os programadores novos no Rust, uma vez que o compilador ensina efetivamente boas práticas e ajuda a evitar erros comuns.


A linguagem inclui o Cargo, um gerenciador de pacotes unificado que lida com o gerenciamento de dependências, construção, testes e geração de documentação. Essa padronização elimina a fragmentação vista em linguagens mais antigas como C++, onde várias ferramentas concorrentes criam inconsistência entre projetos. O Cargo também suporta extensões como rustfmt para formatação de código e Clippy para análise estática, garantindo que o código siga diretrizes de estilo consistentes e detecte possíveis problemas antes que eles se tornem problemas.


As capacidades multiplataforma do Rust vão além dos sistemas operativos tradicionais e incluem plataformas móveis como Android e iOS, bem como WebAssembly para aplicações baseadas em browsers. Esse suporte multiplataforma é útil para aplicativos Bitcoin que precisam ser executados em diversos ambientes. Por exemplo, projectos como o Mutiny Wallet aproveitam a compilação WebAssembly do Rust para criar [carteiras](https://planb.academy/resources/glossary/wallet) Lightning que correm diretamente em navegadores Web, algo que seria impraticável apenas com tecnologias Web tradicionais.


### Compreender os tipos de erros e as suas implicações


O tratamento eficaz de erros começa com a compreensão das diferentes categorias de erros que podem ocorrer durante a execução do programa. Considere uma aplicação de roteamento simples que calcula caminhos entre pontos geográficos. Este exemplo ilustra três tipos fundamentais de erros que os programadores devem resolver: erros de entrada inválidos, erros de recursos em tempo de execução e erros lógicos.


Os erros de entrada inválidos ocorrem quando uma função recebe parâmetros que não cumprem os seus requisitos. Por exemplo, se um sistema de coordenadas geográficas utiliza números inteiros com sinal para a longitude, mas recebe um valor negativo onde apenas os valores positivos são válidos, a função não pode prosseguir de forma significativa. Estes erros representam uma violação do contrato entre o chamador e a função, e a resposta adequada é normalmente rejeitar a entrada e devolver uma indicação de erro.


Os erros de recursos em tempo de execução ocorrem quando as dependências externas não estão disponíveis ou são inacessíveis. A leitura de um ficheiro de mapa pode falhar porque o ficheiro não existe, a aplicação não tem as permissões adequadas ou o dispositivo de armazenamento não está disponível. Estes erros são externos à lógica do programa e requerem frequentemente correcções ambientais em vez de alterações ao código. No entanto, as aplicações robustas devem antecipar e lidar com estes cenários de forma graciosa.


Os erros lógicos representam falhas na implementação do programa ou mal-entendidos sobre a forma como os componentes interagem. Se um algoritmo de roteamento retorna um caminho vazio quando são dados pontos de início e fim válidos, isso indica uma falha lógica que precisa ser corrigida no próprio código. Ao contrário dos outros tipos de erro, os erros lógicos normalmente requerem depuração e modificação do código para serem resolvidos.


### Estratégias para uma gestão robusta dos erros


A criação de software fiável requer estratégias proactivas que minimizem as oportunidades de erro e tratem os erros inevitáveis de forma graciosa. A primeira estratégia envolve a limitação de possíveis erros através de uma conceção cuidadosa dos tipos. Ao escolher tipos que só podem representar valores válidos, os programadores podem eliminar classes inteiras de erros de entrada inválidos. Por exemplo, a utilização de números inteiros sem sinal para valores que não podem ser negativos evita erros de valor negativo em tempo de compilação.


As asserções fornecem outra camada de proteção, verificando explicitamente se as condições esperadas são verdadeiras durante a execução do programa. Essas verificações servem a vários propósitos: elas detectam bugs durante os testes, fazem com que os programas falhem mais cedo quando ocorrem problemas (facilitando a depuração) e servem como documentação executável que descreve as suposições do programador. Quando uma asserção falha, isso indica que uma suposição fundamental sobre o estado do programa foi violada, normalmente apontando para um erro lógico que precisa ser investigado.


O princípio das abstracções em camadas ajuda a gerir a complexidade, garantindo que os erros são tratados aos níveis adequados do sistema. Os pormenores internos de implementação, incluindo tipos de erro específicos de bibliotecas de nível inferior, não devem propagar-se para além dos limites do subsistema. Em vez disso, cada camada deve traduzir os erros em termos que sejam significativos a esse nível de abstração. Por exemplo, uma aplicação wallet que utilize uma biblioteca Bitcoin deve traduzir os erros de análise do descritor de baixo nível em mensagens de nível superior, como "configuração inválida do wallet", que fornecem informações acionáveis aos utilizadores ou ao código de chamada.


Esta abordagem ao tratamento de erros, combinada com o sistema de tipos e as ferramentas do Rust, ajuda a detetar potenciais problemas no início do processo de desenvolvimento, antes que possam afetar os utilizadores ou comprometer a segurança das aplicações Bitcoin.



## Modelo de erro

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

O Rust fornece uma abordagem abrangente para o tratamento de erros que equilibra segurança e praticidade. Embora os conceitos gerais do modelo de erro se apliquem a todas as linguagens de programação, o Rust oferece ferramentas e padrões específicos que tornam o tratamento de erros explícito e gerenciável. Compreender estes mecanismos é crucial para escrever aplicações robustas em Rust que possam lidar graciosamente com situações inesperadas, mantendo o desempenho e a segurança.


### O pânico e as suas utilizações adequadas


O mecanismo de pânico do Rust representa a maneira mais direta de lidar com erros irrecuperáveis. Quando você chama a macro `panic!`, o programa pára imediatamente a execução, abortando ou desenrolando, dependendo da sua configuração. A macro panic aceita uma mensagem string que descreve o que deu errado, fornecendo contexto para depuração. Adicionalmente, métodos como `unwrap()` e `expect()` nos tipos Result e Option servem como atalhos para o panic quando estes tipos contém valores de erro ou None respetivamente. O método `expect()` permite que você forneça uma mensagem personalizada, tornando-o um pouco mais informativo do que `unwrap()` ao depurar falhas.


Apesar de sua simplicidade, o panic deve ser usado judiciosamente em código de produção. Há vários cenários em que o panic não é apenas aceitável, mas recomendado. Ao escrever exemplos ou protótipos, o panic fornece uma maneira limpa de se concentrar na funcionalidade principal sem sobrecarregar o código com um tratamento de erros abrangente. Em ambientes de teste, o panic é frequentemente o comportamento desejado quando as asserções falham, pois indica claramente que algo inesperado ocorreu. A comunidade Rust também reconhece situações em que os desenvolvedores têm mais conhecimento do que o compilador, como quando analisam endereços IP codificados que são sabidamente válidos.


No entanto, a aparente segurança dos pânicos "verificados pelo compilador" pode ser enganosa. Considere um cenário onde você codifica um endereço IP e usa `expect()` porque você sabe que é válido. Com o tempo, à medida que o código evolui, esse valor codificado pode ser refatorado em uma constante e, mais tarde, essa constante pode ser alterada para algo como "localhost" para uma melhor experiência do usuário. De repente, o seu pânico "seguro" torna-se uma falha em tempo de execução. Essa evolução demonstra por que geralmente é melhor evitar panics em código de produção e, em vez disso, retornar tipos de erro apropriados que podem ser tratados graciosamente.


Uma notável exceção à regra de "evitar pânico" envolve operações com mutex. Quando você chama `lock()` em um mutex, ele retorna um Resultado porque o bloqueio pode falhar se outra thread entrou em pânico enquanto segurava o mutex. Isso cria uma situação confusa onde seu código local recebe um erro para algo que aconteceu em um contexto completamente diferente. Uma vez que não se pode razoavelmente lidar com um erro que se originou do pânico de outra thread, muitos desenvolvedores consideram aceitável desembrulhar bloqueios de mutex, especialmente se você mantiver uma base de código livre de pânico em outro lugar.


### Trabalho com tipos de resultado e de opção


O tipo Result forma a espinha dorsal do sistema de tratamento de erros do Rust. Como um enum que pode conter tanto um `Ok(valor)` quanto um `Err(erro)`, Result força o usuário a reconhecer explicitamente que as operações podem falhar. O tipo Option tem um propósito similar para casos onde um valor pode simplesmente estar ausente, contendo `Some(value)` ou `None`. Embora Option não forneça informações detalhadas sobre o erro, ele é perfeito para situações em que a ausência de um valor é significativa e esperada.


Tanto Result como Option fornecem vários métodos utilitários que tornam o tratamento de erros mais ergonómico. O método `unwrap_or()` retorna o valor contido se presente, ou um valor padrão se houver um erro ou None. Este padrão é particularmente útil quando se tem uma alternativa razoável, como analisar a entrada do usuário com um padrão sensato quando a análise falha. O método `unwrap_or_default()` funciona de forma similar, mas utiliza o valor padrão do tipo ao invés de exigir que você especifique um. Enquanto esses métodos não lidam tecnicamente com erros no sentido tradicional, eles fornecem uma maneira de degradar graciosamente a funcionalidade quando ocorrem problemas.


O operador de ponto de interrogação (`?`) é uma sintaxe concisa para a propagação de erros. Quando aplicado a um Resultado ou Opção, ele extrai o valor de sucesso se presente, ou retorna imediatamente o erro da função atual se houver um problema. Este operador elimina os padrões verbosos de verificação de erros comuns em linguagens como Go, onde é necessário verificar manualmente e retornar erros a cada passo. O operador de ponto de interrogação essencialmente fornece açúcar sintático para retornos antecipados, permitindo que você escreva um código limpo e linear que se concentra no caminho feliz enquanto lida automaticamente com a propagação de erros.


### Padrões avançados de tratamento de erros


O método `map()` nos tipos Result e Option permite o tratamento de erros no estilo funcional, o que pode tornar o código mais expressivo e componível. Quando você chama `map()` em um Result, a função fornecida é aplicada ao valor de sucesso se presente, enquanto os erros são automaticamente propagados sem modificação. Esse padrão é útil ao encadear operações, pois é possível focar na transformação de valores sem tratar repetidamente casos de erro. O método `map_err()` fornece a funcionalidade inversa, permitindo transformar tipos de erro enquanto deixa os valores de sucesso inalterados.


A transformação de erros torna-se crucial quando se constroem aplicações em camadas em que diferentes componentes necessitam de diferentes tipos de erros. Considere uma função que analisa a entrada do usuário e precisa converter erros de análise de baixo nível em erros específicos do domínio. Usando `map_err()`, você pode facilmente traduzir um erro genérico "formato de número inválido" em um erro mais contextual "idade inválida" que faz sentido dentro do domínio da sua aplicação. Essa transformação acontece bem no ponto em que o erro ocorre, tornando o código mais legível e de fácil manutenção do que os blocos try-catch tradicionais, onde o tratamento de erros é separado das operações que podem falhar.


A combinação do operador de ponto de interrogação com o mapeamento de erros cria padrões concisos de tratamento de erros. É possível encadear operações, transformar erros conforme necessário e propagá-los pela pilha de chamadas com o mínimo de boilerplate. Essa abordagem mantém o tratamento de erros próximo às operações que podem falhar, mantendo uma separação clara entre os caminhos de sucesso e de erro.


```rust
use std::fmt;

// Layered error types for a wallet application
#[derive(Debug)]
enum NetworkError {
ConnectionFailed(String),
Timeout,
}

#[derive(Debug)]
enum WalletError {
Network(NetworkError),
InvalidAddress(String),
InsufficientFunds { required: u64, available: u64 },
}

// Implement Display for user-friendly messages
impl fmt::Display for WalletError {
fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
match self {
WalletError::Network(e) => write!(f, "Network error: {:?}", e),
WalletError::InvalidAddress(addr) => write!(f, "Invalid address: {}", addr),
WalletError::InsufficientFunds { required, available } =>
write!(f, "Need {} sats but only have {} available", required, available),
}
}
}

// Convert from lower-level error to domain error
impl From<NetworkError> for WalletError {
fn from(err: NetworkError) -> Self {
WalletError::Network(err)
}
}

// Simulated network call
fn fetch_balance(address: &str) -> Result<u64, NetworkError> {
if address.starts_with("bc1") {
Ok(500_000) // 500k sats
} else {
Err(NetworkError::ConnectionFailed("Invalid endpoint".into()))
}
}

// Higher-level function using ? with automatic error conversion
fn send_payment(from: &str, amount: u64) -> Result<String, WalletError> {
let balance = fetch_balance(from)?; // NetworkError auto-converts to WalletError

if balance < amount {
return Err(WalletError::InsufficientFunds {
required: amount,
available: balance,
});
}

Ok(format!("Sent {} sats", amount))
}

fn main() {
match send_payment("bc1qtest...", 100_000) {
Ok(msg) => println!("Success: {}", msg),
Err(e) => println!("Failed: {}", e), // User-friendly message
}
}
```


### Bibliotecas externas e ecossistemas de tratamento de erros


O ecossistema Rust inclui várias bibliotecas populares que estendem as capacidades de tratamento de erros da biblioteca padrão. A biblioteca `anyhow` fornece uma abordagem simplificada para o tratamento de erros, oferecendo um tipo de erro universal que pode converter automaticamente de qualquer tipo de erro que implemente a caraterística padrão Error. Esta conversão automática permite-lhe utilizar o operador de ponto de interrogação com diferentes tipos de erro sem conversão manual, tornando-o particularmente útil para aplicações em que não é necessário distinguir programaticamente entre diferentes tipos de erro.


Enquanto `anyhow` é excelente em simplificar o tratamento de erros para aplicações onde os erros são exibidos principalmente para os usuários, ele tem limitações no desenvolvimento de bibliotecas. Como o `anyhow` essencialmente converte todos os erros em mensagens de string, os consumidores de sua biblioteca não podem facilmente responder programaticamente a diferentes condições de erro. Essa limitação faz com que o `anyhow` seja mais adequado para aplicativos de usuário final do que para bibliotecas que precisam fornecer informações de erro estruturadas para seus consumidores.


Abordagens mais avançadas de tratamento de erros envolvem a criação de tipos de erro personalizados que modelam os modos de falha específicos da sua aplicação ou biblioteca. Um modelo de erro bem concebido pode distinguir entre entrada inválida (que o chamador pode corrigir), erros de tempo de execução (que podem ser repetidos) e falhas permanentes (que indicam bugs ou condições irrecuperáveis). Esta abordagem estruturada permite que os consumidores do seu código tomem decisões inteligentes sobre a forma de responder a diferentes tipos de falhas, quer isso signifique repetir operações, pedir aos utilizadores uma entrada diferente ou comunicar erros aos programadores.


## UniFFI, ligando as bibliotecas Rust a vários idiomas


<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

### Introdução ao UniFFI e ao desenvolvimento multiplataforma


UniFFI é uma ferramenta para tornar as bibliotecas Rust acessíveis em várias linguagens de programação e plataformas. Desenvolvida pela Mozilla, esta ferramenta aborda um desafio fundamental no desenvolvimento de software moderno: como aproveitar os benefícios de desempenho e segurança do Rust, mantendo a compatibilidade com diversos ecossistemas de desenvolvimento. A ferramenta gera automaticamente ligações de linguagem para as bibliotecas Rust, eliminando a necessidade de os programadores criarem manualmente código de interface para cada linguagem de destino.


O problema central que a UniFFI resolve decorre da natureza do Rust como uma linguagem compilada. Quando o código Rust é compilado, ele produz uma saída binária com uma Função Estrangeira Interface (FFI) que apresenta uma interface de baixo nível que pode ser difícil de usar diretamente de linguagens de alto nível como Python, Swift ou Kotlin. Tradicionalmente, cada desenvolvedor de biblioteca precisaria escrever um código de vinculação personalizado para cada linguagem de destino, criando uma barreira significativa para a adoção entre plataformas. O UniFFI elimina essa redundância, fornecendo uma abordagem padronizada para gerar essas ligações automaticamente.


A filosofia de design da ferramenta centra-se em permitir que os desenvolvedores do Rust se concentrem em sua lógica de negócios principal, tornando suas bibliotecas acessíveis aos desenvolvedores que trabalham em outras linguagens. Um programador iOS que utilize Swift, por exemplo, pode consumir uma biblioteca Rust através de ligações geradas pela UniFFI que apresentam uma interface Swift completamente nativa, sem qualquer indicação de que a implementação subjacente está escrita em Rust. Essa integração perfeita permite que as equipes aproveitem os benefícios de desempenho do Rust sem exigir que todos os membros da equipe aprendam o Rust.


### Compreender a arquitetura e o fluxo de trabalho do UniFFI


O UniFFI funciona através de um fluxo de trabalho bem definido que transforma as bibliotecas Rust em pacotes compatíveis com vários idiomas. O processo começa com a criação de um ficheiro Unified Definition Language (UDL), que serve como uma especificação de interface que descreve que partes da sua biblioteca Rust devem ser expostas a outras linguagens. Este ficheiro UDL funciona como um contrato entre a sua implementação do Rust e os language bindings gerados.


A arquitetura segue uma clara separação de preocupações. Os programadores mantêm a sua biblioteca Rust com expressões idiomáticas e padrões Rust padrão e, em seguida, criam um ficheiro UDL separado que mapeia a interface pública para o sistema de tipos da UniFFI. O gerador de ligações UniFFI processa tanto a biblioteca Rust como a especificação UDL para produzir ligações em linguagem nativa para as plataformas alvo solicitadas. Estas ligações geradas tratam de todas as complexas operações de transferência e remoção de dados entre o tempo de execução da língua estrangeira e o código Rust.


Em tempo de execução, a arquitetura cria uma abordagem em camadas em que o código da aplicação escrito na linguagem de destino (como Kotlin para Android) interage com o código de ligação gerado que parece completamente nativo dessa linguagem. Esta camada de ligação trata da tradução entre os tipos específicos da linguagem e os tipos do Rust, gere a memória com segurança através das fronteiras da linguagem e fornece tratamento de erros que segue as convenções da linguagem de destino. A lógica comercial subjacente do Rust permanece inalterada e desconhece as interfaces de várias linguagens construídas sobre ela.


### Trabalhar com UDL: Definição Interface e mapeamento de tipos


A Linguagem de Definição Unificada serve como pedra angular da funcionalidade do UniFFI, fornecendo uma forma declarativa de especificar que partes de uma biblioteca Rust devem ser expostas e como devem ser apresentadas nas linguagens de destino. Os ficheiros UDL devem conter pelo menos um espaço de nome, que actua como um contentor para funções que podem ser chamadas diretamente sem requerer a instanciação de objectos. Essas funções de espaço de nome normalmente lidam com operações simples que recebem valores como parâmetros e retornam resultados.


A UDL suporta um conjunto abrangente de tipos incorporados que mapeiam naturalmente para os tipos Rust correspondentes. Os tipos básicos incluem primitivos padrão como booleanos, vários tamanhos de inteiros (u8, u32, etc.), números de ponto flutuante e strings. Os tipos mais complexos incluem vectores, mapas de hash e conceitos específicos do Rust, como tipos Option (representados com uma sintaxe de ponto de interrogação) e tipos Result para tratamento de erros. O sistema de tipos também suporta enumerações, tanto enums simples baseados em valores como enums complexos que contêm dados associados, permitindo a modelação de dados que se traduzem para além das fronteiras linguísticas.


Structs em Rust são traduzidos para dicionários em UDL, mantendo uma correspondência quase um-para-um enquanto se adaptam às convenções de sintaxe de UDL. Quando as estruturas Rust têm métodos associados, elas podem ser expostas como interfaces em UDL, que generate como classes com métodos em linguagens orientadas a objetos como Kotlin ou Swift. Esse mapeamento preserva os padrões de design orientado a objetos que os desenvolvedores esperam nessas linguagens, mantendo a estrutura e o comportamento da implementação Rust subjacente.


```
// Example UDL file for a Bitcoin wallet library (wallet.udl)
namespace wallet {
// Namespace functions - called directly without object
string generate_mnemonic();
Wallet create_wallet(string mnemonic);
};

// Dictionary (struct) - becomes data class in Kotlin, struct in Swift
dictionary Balance {
u64 confirmed_sats;
u64 pending_sats;
};

// Interface (class with methods) - becomes class with methods
interface Wallet {
// Constructor
constructor(string mnemonic);

// Methods
Balance get_balance();
string get_new_address();
string send_to_address(string address, u64 amount_sats);
};

// Enum with data - maps to sealed class (Kotlin) or enum with associated values (Swift)
[Enum]
interface TransactionStatus {
Pending(u32 confirmations_needed);
Confirmed(u32 block_height);
Failed(string reason);
};

// Error enum for Result types
[Error]
enum WalletError {
"InsufficientFunds",
"InvalidAddress",
"NetworkError",
};

// Function that can fail - throws in target language
interface Wallet {
[Throws=WalletError]
string send_to_address(string address, u64 amount_sats);
};
```


A implementação correspondente do Rust definiria estes tipos e implementaria o atributo `uniffi::export` para as ligações generate para Kotlin, Swift, Python e outras linguagens suportadas.


### Tratamento de erros e funcionalidades avançadas


O UniFFI fornece tratamento de erros que preserva o modelo de erro baseado em resultados do Rust, traduzindo-o adequadamente para as línguas de destino. Funções que retornam tipos de resultado no Rust podem ser marcadas com a palavra-chave "throws" no UDL, especificando quais tipos de erro podem produzir. Esses erros devem ser definidos como enums de erro no arquivo UDL e devem implementar a caraterística padrão Error do Rust no código Rust subjacente. A caixa thiserror fornece uma macro conveniente para implementar essa caraterística, reduzindo significativamente o código boilerplate.


A tradução do tratamento de erros demonstra a abordagem consciente da linguagem do UniFFI. Em Kotlin, as funções marcadas como lançando em métodos UDL generate que lançam excepções seguindo as convenções Java/Kotlin. As ligações Python utilizam de forma semelhante o modelo de exceção Python. Essa tradução garante que o tratamento de erros pareça natural e idiomático em cada idioma de destino, preservando o significado semântico dos tipos de erro originais do Rust.


As interfaces de retorno de chamada representam outro recurso avançado que permite a comunicação bidirecional entre as bibliotecas Rust e os aplicativos de consumo. Quando uma biblioteca Rust precisa de chamar de volta o código da aplicação, os programadores podem definir caraterísticas em Rust e marcá-las como interfaces de retorno de chamada em UDL. A aplicação consumidora implementa essas interfaces em sua linguagem nativa, e o UniFFI lida com o complexo marshaling necessário para invocar esses retornos de chamada do código Rust. Esse padrão requer uma consideração cuidadosa da segurança de thread, já que os callbacks podem cruzar os limites de thread, necessitando de limites de Send e Sync no lado do Rust.


### Aplicações no mundo real e limitações actuais


O UniFFI foi adotado na comunidade de desenvolvimento de criptomoedas e [cadeias de blocos](https://planb.academy/resources/glossary/blockchain), com grandes projectos como o BDK (Bitcoin Development Kit), o LDK (Lightning Development Kit) e várias implementações do wallet que o utilizam para fornecer SDKs móveis. Estes projectos demonstram a utilização da UniFFI em ambientes de produção.


A análise de ficheiros UDL reais destes projectos revela padrões e melhores práticas que surgiram da utilização prática. O ficheiro UDL do BDK, por exemplo, mostra como modelos de domínio complexos com várias enums, structs e interfaces podem ser mapeados de forma eficaz para criar SDKs móveis abrangentes. A consistência da sintaxe UDL em diferentes projectos significa que os programadores familiarizados com uma biblioteca UniFFI podem rapidamente compreender e trabalhar com outras, criando um efeito de rede que beneficia todo o ecossistema.


No entanto, a UniFFI tem limitações notáveis que os programadores devem ter em conta. A mais significativa é a falta de suporte para interfaces assíncronas. Todos os bindings gerados são síncronos, exigindo que os desenvolvedores manipulem operações assíncronas dentro de seu código Rust e apresentem interfaces síncronas para aplicações consumidoras. Além disso, a colocação de documentação representa um desafio: a documentação escrita no código Rust não é transferida para as ligações geradas, enquanto a documentação nos ficheiros UDL não está disponível para os consumidores diretos da biblioteca Rust. Embora existam esforços contínuos para resolver essas limitações através da análise e geração automáticas, elas continuam a ser considerações para as implementações atuais. Por fim, o UniFFI gera language bindings, mas não lida com o empacotamento e a distribuição específicos da plataforma, deixando que os desenvolvedores gerenciem as etapas finais da criação de pacotes distribuíveis para cada plataforma de destino.


# Desenvolvimento de LNP/BP com SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## Nó LN no SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

### Compreender a arquitetura modular do LDK


O Lightning Development Kit (LDK) adota uma abordagem diferente para a implementação do [Lightning Network](https://planb.academy/resources/glossary/lightning-network) em comparação com o software de [nó](https://planb.academy/resources/glossary/node) tradicional, como o CLightning ou o LND. Enquanto os nós Lightning convencionais operam como aplicativos daemon completos executados continuamente em uma máquina, o LDK funciona como uma biblioteca Rust modular que fornece componentes primitivos para a construção de soluções Lightning personalizadas. Essa distinção arquitetônica torna o LDK flexível, permitindo que os desenvolvedores montem a funcionalidade do Lightning de maneiras que atendam aos requisitos específicos de seus projetos.


A filosofia central do LDK está centrada na modularidade e adaptabilidade. Ao invés de fornecer uma solução monolítica, o LDK oferece componentes individuais que podem ser combinados, customizados ou substituídos completamente. Cada componente vem com implementações padrão que funcionam imediatamente, mas os desenvolvedores têm a liberdade de substituir suas próprias implementações quando necessário. Por exemplo, o LDK inclui implementações padrão para monitoramento de blockchain, assinatura de transações e comunicação de rede, mas qualquer uma delas pode ser substituída por soluções personalizadas adaptadas a casos de uso ou ambientes específicos.


Esse design modular permite que o LDK funcione em diversas plataformas e cenários que seriam desafiadores para os nós Lightning tradicionais. Aplicativos móveis, navegadores da Web, dispositivos incorporados e hardware especializado podem aproveitar os componentes da LDK de maneiras que atendam às suas restrições e requisitos exclusivos. A arquitetura da biblioteca garante que os desenvolvedores possam criar aplicativos habilitados para Lightning sem ficarem presos a padrões operacionais predeterminados ou dependências de sistema.


### Casos de uso do LDK e flexibilidade da plataforma


A flexibilidade da arquitetura do LDK abre inúmeros casos de uso que vão muito além das implantações tradicionais de nós Lightning. O desenvolvimento do wallet móvel representa uma das aplicações mais atraentes, onde o LDK permite a criação de carteiras Lightning sem custódia, semelhantes ao Phoenix wallet. Estas implementações móveis podem manter o controlo do utilizador sobre as [chaves privadas](https://planb.academy/resources/glossary/private-key) enquanto se sincronizam com os Lightning Service Providers (LSPs) quando ficam online, permitindo a receção de pagamentos e a gestão de canais sem problemas, mesmo com conetividade intermitente.


A integração do módulo de segurança de hardware (HSM) mostra outro caso de uso poderoso do LDK. Ao extrair apenas os componentes de assinatura e verificação de transações, os desenvolvedores podem criar dispositivos de assinatura com reconhecimento do Lightning que entendem o contexto e as implicações das transações do Lightning. Esse recurso vai além da simples assinatura de transações para incluir uma análise inteligente do encaminhamento de pagamentos, operações de [canal](https://planb.academy/resources/glossary/payment-channel) e decisões críticas de segurança. O HSM pode avaliar se uma transação representa um pagamento legítimo, uma operação de encaminhamento ou uma tentativa potencialmente maliciosa, fornecendo aos utilizadores informações de segurança significativas.


Os aplicativos Lightning baseados na Web se beneficiam significativamente da filosofia de design sem chamadas de sistema do LDK. Como os ambientes WebAssembly não têm acesso direto aos recursos do sistema, como sistemas de arquivos, soquetes de rede ou fontes de entropia, a abordagem pura do LDK permite que a funcionalidade Lightning opere perfeitamente em ambientes de navegador. Os desenvolvedores podem implementar camadas de rede personalizadas usando WebSockets e fornecer fontes de persistência e aleatoriedade compatíveis com o navegador, mantendo a conformidade total com o protocolo Lightning.


### Componentes principais e arquitetura orientada para eventos


A arquitetura interna do LDK gira em torno de vários componentes-chave que funcionam em conjunto através de um sistema orientado para eventos. O sistema de gerenciamento de pares lida com toda a comunicação com outros nós Lightning, implementando o protocolo de ruído para criptografia e gerenciando estruturas de mensagens para conformidade com o protocolo Lightning. Esse componente opera independentemente do mecanismo de transporte subjacente, permitindo que os desenvolvedores implementem redes sobre soquetes TCP, WebSockets, conexões seriais USB ou qualquer outro canal de comunicação bidirecional.


O gestor de canais funciona como coordenador central das operações do canal Lightning, trabalhando em conjunto com o gestor de pares para executar as operações de abertura, fecho e pagamento do canal. Quando um desenvolvedor inicia uma abertura de canal, o gerenciador de canais cria as mensagens de protocolo necessárias e coordena com o gerenciador de pares para lidar com o processo de negociação em várias etapas. Esta separação de preocupações permite uma abstração clara entre a lógica do protocolo Lightning e os detalhes de comunicação da rede.


O sistema de eventos do LDK fornece notificações assíncronas para todas as operações significativas e alterações de estado. Os eventos cobrem todo o espetro de operações do Lightning, desde conexões e desconexões de pares até sucessos e falhas de pagamento, mudanças de estado de canal e confirmações de blockchain. Essa abordagem orientada por eventos permite que os aplicativos respondam adequadamente à atividade da rede Lightning, mantendo uma separação clara entre a funcionalidade principal do LDK e a lógica específica do aplicativo. Os desenvolvedores podem implementar manipuladores de eventos personalizados que atualizam interfaces de usuário, acionam notificações ou iniciam ações de acompanhamento com base nos eventos da rede Lightning.


### Blockchain Integração e gestão de dados


A integração de dados Blockchain representa uma das camadas de abstração do LDK, projetada para acomodar tudo, desde nós Bitcoin completos até clientes móveis leves. O LDK suporta dois modos primários de interação blockchain, cada um otimizado para diferentes restrições de recursos e requisitos operacionais. O modo de bloco completo permite que aplicativos com acesso a dados completos de blockchain passem blocos inteiros para o LDK, permitindo o monitoramento abrangente de transações e a resposta imediata a eventos relevantes de blockchain.


Para ambientes com recursos limitados, o LDK fornece uma abordagem baseada em filtragem que reduz os requisitos de largura de banda e armazenamento. Nesse modo, o LDK comunica seus interesses de monitoramento por meio de interfaces abstratas, solicitando a vigilância de IDs de transação específicos, [UTXOs](https://planb.academy/resources/glossary/utxo) ou padrões de script. A camada de aplicação pode então implementar esse monitoramento usando servidores Electrum, exploradores de blocos ou outras fontes de dados de blockchain leves. Esta abordagem permite que as carteiras móveis e as aplicações Web mantenham a funcionalidade Lightning sem exigir a sincronização total da cadeia de blocos.


A camada de persistência no LDK segue os mesmos princípios de abstração, fornecendo aplicativos com blobs de dados binários que devem ser armazenados e recuperados de forma confiável. O LDK lida com toda a complexidade da serialização e desserialização dos estados do canal Lightning, dados de fofocas de rede e outras informações críticas. Os aplicativos simplesmente precisam implementar mecanismos de armazenamento confiáveis, seja usando sistemas de arquivos locais, serviços de armazenamento em nuvem ou sistemas de banco de dados especializados. Esse design garante que o gerenciamento de estado do Lightning permaneça robusto e, ao mesmo tempo, permite que os aplicativos escolham soluções de armazenamento que correspondam a seus requisitos operacionais e modelos de segurança.


### Funcionalidades avançadas e padrões de integração


Os recursos do LDK se estendem aos recursos do Lightning Network, como pagamentos de vários caminhos, otimização de rotas e gerenciamento de boatos de rede. O sistema de roteamento mantém uma visão abrangente da topologia do Lightning Network através da participação no protocolo gossip, permitindo a busca inteligente de caminhos para pagamentos. Os aplicativos podem influenciar as decisões de roteamento por meio de parâmetros de configuração e podem até mesmo implementar uma lógica de roteamento personalizada para casos de uso especializados.


O sistema de vinculação de linguagem da biblioteca permite a integração do LDK em vários ambientes de programação, suportando Java, Kotlin, Swift, TypeScript, JavaScript e C++. Essa compatibilidade entre plataformas permite que aplicativos móveis escritos em linguagens nativas incorporem a funcionalidade do Lightning, mantendo as caraterísticas de desempenho ideais. O sistema de ligação preserva a arquitetura orientada a eventos e o design modular do LDK em todas as linguagens suportadas, garantindo experiências consistentes para o desenvolvedor, independentemente da plataforma de destino.


A estimativa de taxas e a transmissão de transações representam áreas adicionais onde o LDK oferece flexibilidade. As aplicações podem implementar estratégias personalizadas de estimativa de taxas que levem em conta seus padrões operacionais específicos e requisitos do usuário. Da mesma forma, a transmissão de transações pode ser personalizada para funcionar com várias interfaces de rede Bitcoin, desde conexões diretas full node até serviços de transmissão de terceiros. Essa flexibilidade garante que os aplicativos baseados em LDK possam otimizar suas interações de blockchain para seus casos de uso específicos, mantendo a conformidade com o protocolo Lightning e os padrões de segurança.


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

### O desafio do desenvolvimento de relâmpagos


O desenvolvimento de aplicações que integram pagamentos Lightning apresenta uma barreira significativa para a maioria dos programadores. Para criar uma aplicação com a funcionalidade de pagamento Lightning, os programadores têm essencialmente de se tornar especialistas em Lightning, compreendendo conceitos complexos como gestão de canais, equilíbrio de liquidez e topologia de rede. Este requisito de especialização cria um problema fundamental para a adoção do Lightning: embora a própria rede Lightning esteja operacional e os pagamentos sejam fiáveis, a complexidade técnica impede a integração generalizada em aplicações quotidianas.


O principal desafio reside no desfasamento entre o que os programadores precisam e o que querem fornecer. Os desenvolvedores normalmente trabalham com prazos apertados e preferem soluções simples que lhes permitam se concentrar na funcionalidade principal do aplicativo em vez de se tornarem especialistas em infraestrutura de pagamento. Quando a integração do Lightning é difícil, os programadores gravitam naturalmente em torno de soluções de custódia porque oferecem o caminho de menor resistência. No entanto, essa tendência para serviços de custódia prejudica a proposta de valor fundamental do Bitcoin de soberania financeira sem custódia.


### Visão do Breez, relâmpagos por todo o lado


O Breez surgiu de uma visão simples, mas ambiciosa: fazer com que todos se conectem à rede Lightning por meio de interfaces intuitivas para a economia Lightning. A abordagem da empresa reconhece que, embora a rede Lightning funcione bem tecnicamente, precisa desesperadamente da adoção dos utilizadores para atingir todo o seu potencial. Este desafio de adoção vai para além dos utilizadores individuais, abrangendo todo o ecossistema de aplicações e serviços que podem beneficiar da integração da Lightning.


A aplicação Breez original demonstrou esta visão, fornecendo aos utilizadores um nó Lightning sem custódia, executado diretamente nos seus telemóveis. Esta aplicação apresentou as capacidades do Lightning, como a transmissão de micropagamentos para podcasters e a funcionalidade de ponto de venda. No entanto, a aplicação Breez também revelou uma limitação arquitetónica crítica: o ecossistema de aplicações móveis não facilita a comunicação fácil entre aplicações, obrigando os programadores a criar todas as funcionalidades relacionadas com o Lightning numa única aplicação, em vez de permitir que aplicações especializadas aproveitem a infraestrutura Lightning partilhada.


Os aprendizados da empresa com o aplicativo Breez levaram a um insight crucial: o futuro da adoção do Lightning depende da conquista dos desenvolvedores. Se a integração do Lightning sem custódia se tornar a opção mais fácil para os desenvolvedores, ela se tornará a escolha padrão. Esta abordagem também oferece vantagens regulamentares, uma vez que o software sem custódia enfrenta menos obstáculos regulamentares do que os serviços de custódia, facilitando aos programadores o envio das suas aplicações a nível global.


### A arquitetura do SDK do Breez


O SDK Breez fornece uma abordagem alternativa para integrar a funcionalidade do Lightning em aplicativos. Em vez de exigir que cada aplicativo execute seu próprio nó Lightning, o SDK fornece uma arquitetura que mantém os princípios não-custodiais, simplificando a experiência do desenvolvedor. Na sua essência, o SDK dá a cada utilizador final o seu próprio nó Lightning pessoal em execução na infraestrutura Greenlight, o serviço de alojamento de nós Lightning baseado na nuvem da Blockstream.


Esta arquitetura resolve vários problemas críticos em simultâneo. Os utilizadores não precisam de se preocupar com a gestão da base de dados, o tempo de funcionamento do servidor ou a manutenção da infraestrutura-preocupações que seriam esmagadoras para os consumidores típicos. No entanto, ao contrário das soluções de custódia tradicionais, a Greenlight nunca tem acesso às chaves do usuário. O nó Lightning na nuvem não pode realizar nenhuma operação sem um aplicativo ativamente conectado que possa assinar transações e mensagens. Esse design mantém os benefícios de segurança da autocustódia e elimina a complexidade operacional.


O SDK também suporta a interoperabilidade. Vários aplicativos podem se conectar ao nó do Lightning do mesmo usuário usando a mesma frase seed, permitindo que os usuários mantenham um único saldo do Lightning em diferentes aplicativos especializados. Por exemplo, um usuário pode ter um aplicativo Lightning wallet geral e um aplicativo de podcasting especializado, ambos acessando os mesmos fundos e canais Lightning. Essa arquitetura permite o desenvolvimento de aplicativos focados e especializados, mantendo uma infraestrutura financeira unificada.


### Fornecedores de serviços relâmpago e liquidez just-in-time


Um componente crítico do SDK do Breez é a sua integração com os Lightning Service Providers (LSPs), que funcionam de forma análoga aos Internet Service Providers, mas para a rede Lightning. Os LSPs resolvem um dos desafios mais complexos do Lightning: a gestão de liquidez. Nos canais Lightning, os fundos só podem fluir em direcções onde existe liquidez, semelhante a contas num ábaco que só se podem mover onde há espaço.


O SDK implementa canais "just-in-time" através de LSPs, gerindo automaticamente a liquidez sem a intervenção do utilizador. Quando um utilizador precisa de receber um pagamento mas não tem liquidez suficiente, o LSP abre automaticamente um novo canal Lightning no momento em que o pagamento chega. Este processo ocorre sem problemas em segundo plano, garantindo que os utilizadores possam sempre receber pagamentos sem compreender a mecânica subjacente do canal.


Esta integração LSP vai para além da simples gestão de liquidez. O SDK inclui uma funcionalidade Lightning abrangente e pronta a utilizar: serviços de torre de vigia incorporados para segurança, interoperabilidade on-chain através de swaps submarinos, ligações fiduciárias através de serviços como o MoonPay e suporte para protocolos LNURL. O sistema também fornece backup e recuperação contínuos, garantindo que os utilizadores nunca percam o acesso aos seus fundos, mesmo que os fornecedores de infra-estruturas mudem ou fiquem indisponíveis.


### Experiência de implementação e de desenvolvimento


O SDK Breez prioriza a experiência do desenvolvedor por meio de sua abordagem abrangente e incluída nas baterias. O SDK fornece ligações para várias linguagens de programação, incluindo Rust, Swift, Kotlin, Python, Go, React Native, Flutter e C#, permitindo que os programadores integrem pagamentos Lightning utilizando as suas ferramentas de desenvolvimento preferidas. A arquitetura abstrai a complexidade do Lightning por meio de APIs, mantendo a segurança da rede Lightning.


Os principais componentes trabalham em conjunto para proporcionar esta experiência simplificada. O analisador de entrada lida automaticamente com diferentes formatos de pagamento, determinando se uma cadeia representa uma [fatura](https://planb.academy/resources/glossary/invoice-lightning), LNURL ou outro método de pagamento e encaminhando-a para a função de tratamento adequada. O signatário integrado gere todas as operações criptográficas em segundo plano, enquanto o swapper trata as interações on-chain de forma transparente. Este design permite que os programadores se concentrem na proposta de valor única da sua aplicação em vez de se tornarem especialistas em infra-estruturas Lightning.


A arquitetura sem confiança do SDK garante que, embora a Greenlight possa observar os estados do canal e as informações de encaminhamento, não pode aceder aos fundos do utilizador nem realizar operações não autorizadas. Os utilizadores mantêm o controlo total sobre as suas chaves privadas, que nunca saem dos seus dispositivos. Esta abordagem representa um compromisso cuidadosamente considerado entre simplicidade operacional e privacidade, fornecendo um caminho prático para a adoção do Lightning, preservando os princípios fundamentais de soberania financeira do Bitcoin.


## LDK vs Breez SDK

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

### Compreender as limitações do Lightning Development Kit (LDK)


O Kit de Desenvolvimento Lightning é uma coleção de bibliotecas Rust concebidas para proporcionar aos programadores flexibilidade na criação de aplicações Lightning Network. No entanto, essa flexibilidade vem com desafios significativos de implementação que se tornaram aparentes durante o desenvolvimento no mundo real no Lipa. A natureza de baixo nível do LDK significa que os desenvolvedores devem lidar com várias tarefas complexas de forma independente, desde a sincronização do gráfico de rede até a otimização do roteamento de pagamentos. Embora esta abordagem ofereça controlo total sobre a implementação do Lightning, requer recursos de desenvolvimento substanciais e conhecimentos técnicos profundos para alcançar a fiabilidade pronta para produção.


Uma das caraterísticas mais críticas em falta no LDK era o suporte para LNURL, uma norma amplamente adoptada que simplifica as interações Lightning Network para os utilizadores finais. Além disso, a ausência de saídas de ancoragem apresentava sérios desafios operacionais, especialmente em ambientes de alta taxa. As saídas Anchor resolvem um problema fundamental com os fechamentos forçados de canais Lightning: quando as taxas de rede aumentam drasticamente, os canais com taxas predefinidas podem se tornar impossíveis de fechar unilateralmente porque a taxa predefinida se torna insuficiente para a confirmação da transação. Esta limitação revelou-se especialmente problemática para as aplicações móveis wallet, em que os utilizadores podem abandonar o wallet sem coordenar os encerramentos de canais cooperativos, deixando os fundos potencialmente retidos durante os picos de taxas.


A relativa imaturidade do LDK também se manifestou num encaminhamento de pagamentos pouco fiável, um problema crítico para qualquer aplicação Lightning. Apesar de ser uma implementação tecnicamente sólida, o amplo escopo do LDK como uma solução genérica tornou difícil resolver problemas específicos rapidamente. A equipa de desenvolvimento gastou um tempo considerável a resolver problemas de encaminhamento e a implementar funcionalidades que, idealmente, deveriam ser tratadas ao nível da biblioteca, o que acabou por afetar a velocidade de desenvolvimento e a qualidade da experiência do utilizador.


### Descobrir as vantagens do Breez SDK e do Greenlight


A transição para o SDK Breez representou uma mudança na abordagem arquitetónica, passando de um nó Lightning autogerido para uma solução baseada na nuvem alimentada pelo serviço Greenlight da Blockstream. Essa mudança abordou imediatamente vários pontos críticos de dor experimentados com a implementação do LDK. A melhoria mais significativa ocorreu na fiabilidade dos pagamentos, principalmente devido à capacidade do Greenlight de manter um gráfico de rede sempre atualizado. Ao contrário das implementações móveis tradicionais do Lightning, que têm de sincronizar as informações da rede quando a aplicação é iniciada, os nós do Greenlight são executados continuamente na nuvem, mantendo o conhecimento da rede em tempo real e fornecendo instantaneamente dados gráficos completos quando os utilizadores se ligam.


Esta arquitetura aproveita a implementação Core Lightning (CLN) testada em combate, que tem encaminhado os pagamentos com sucesso há anos como uma das implementações originais do Lightning Network. A experiência acumulada e a fiabilidade comprovada do CLN proporcionaram melhorias imediatas de estabilidade em relação ao projeto LDK mais recente. Quando os utilizadores activam o seu wallet alimentado pelo Greenlight, herdam instantaneamente todo o conhecimento da rede e as capacidades de encaminhamento de um nó Lightning em funcionamento contínuo, eliminando os atrasos de sincronização e as incertezas de encaminhamento que assolavam a implementação anterior.


A filosofia de design opinativo do SDK Breez foi útil para o desenvolvimento do wallet. Em vez de fornecer um kit de ferramentas Lightning genérico, o Breez centra-se especificamente nas aplicações wallet do utilizador final, permitindo que a equipa de desenvolvimento concentre os seus esforços na criação de soluções abrangentes para este caso de utilização específico. Esta abordagem direcionada permitiu ao Breez integrar serviços essenciais diretamente no SDK, incluindo a funcionalidade Lightning Service Provider (LSP) que permite aos utilizadores receber pagamentos imediatamente após a instalação do wallet, sem necessidade de procedimentos manuais de abertura de canais.


### Funcionalidades abrangentes e melhorias na experiência do utilizador


A abordagem integrada do SDK do Breez vai além da funcionalidade básica do Lightning, incorporando caraterísticas que melhoram a experiência do utilizador. A integração LSP incorporada elimina a barreira tradicional de exigir que os utilizadores compreendam a gestão de canais, permitindo a receção imediata de pagamentos para novas instalações wallet. Este processo de integração ajuda na adoção generalizada, uma vez que os utilizadores podem começar a receber pagamentos Lightning sem quaisquer conhecimentos técnicos ou procedimentos de configuração.


A funcionalidade de troca na cadeia fornece outra camada de otimização da experiência do utilizador, permitindo a apresentação de um saldo unificado aos utilizadores. Em vez de obrigar os utilizadores a compreender a distinção entre Lightning e on-chain Bitcoin, o serviço de troca permite a conversão automática entre estas camadas, conforme necessário. Quando os utilizadores precisam de efetuar pagamentos em on-chain, o sistema pode trocar facilmente os fundos Lightning para on-chain Bitcoin nos bastidores, mantendo a ilusão de um saldo único e líquido, ao mesmo tempo que trata internamente da complexidade técnica.


O suporte do SDK para reservas de canal zero aborda um desafio significativo da experiência do utilizador nas implementações tradicionais do Lightning. As reservas de canal normalmente impedem que os utilizadores gastem todo o seu saldo apresentado, criando confusão quando os pagamentos falham, apesar de fundos aparentemente suficientes. Ao eliminar essas reservas, o Breez permite que os utilizadores gastem todo o seu saldo apresentado, embora isso exija que o LSP aceite um risco adicional. Esta solução de compromisso exemplifica a abordagem centrada no utilizador do Breez, em que a complexidade técnica e o risco são absorvidos pelos fornecedores de serviços para criar experiências de utilização intuitivas.


Recursos adicionais como suporte a LNURL, serviços de taxa de câmbio e sincronização de vários dispositivos demonstram ainda mais a abordagem abrangente do SDK para o desenvolvimento do wallet. A arquitetura baseada em nuvem permite que os usuários acessem seu Lightning node a partir de vários dispositivos ou aplicativos, com o Breez lidando com a sincronização de estado entre esses diferentes pontos de acesso. Os itens futuros do roteiro incluem a funcionalidade spend-all para drenagem completa do wallet, emenda para gerenciamento dinâmico de canais e um mercado de LSPs concorrentes para introduzir uma concorrência saudável na prestação de serviços.


### Avaliação de compromissos e preocupações com a centralização


A transição para o Breez SDK e Greenlight introduz importantes compromissos de centralização que devem ser cuidadosamente considerados no contexto dos princípios de descentralização do Bitcoin. A arquitetura baseada na nuvem significa que os nós Lightning dos utilizadores operam na infraestrutura da Blockstream, criando dependências tanto na operação contínua da Greenlight como no desenvolvimento contínuo do Breez. Esta centralização vai para além da mera conveniência, afectando potencialmente a capacidade dos utilizadores de recuperar fundos se os serviços ficarem indisponíveis ou se ocorrer censura.


Os cenários de recuperação apresentam desafios específicos nesta arquitetura. Apesar de os utilizadores manterem o controlo das suas chaves privadas, o acesso aos fundos sem a infraestrutura do Greenlight exigiria conhecimentos técnicos especializados para criar nós Core Lightning independentes e restaurar os estados dos canais. Para os utilizadores individuais, este processo de recuperação revelar-se-ia provavelmente proibitivamente complexo, e mesmo os fornecedores de wallet enfrentariam desafios significativos para migrar bases de utilizadores inteiras para uma infraestrutura alternativa se os serviços Greenlight fossem interrompidos.


As considerações de privacidade também se alteram com esta mudança de arquitetura. O encaminhamento baseado na nuvem significa que a Greenlight ganha potencialmente visibilidade sobre os destinos dos pagamentos, ao passo que as anteriores arquitecturas baseadas apenas em LSP limitavam a fuga de informação aos montantes e prazos de pagamento. A geração do Invoice na nuvem expande ainda mais a potencial exposição da informação, uma vez que as facturas não utilizadas que anteriormente permaneciam privadas nos dispositivos dos utilizadores passam agora pela infraestrutura da Blockstream.


Apesar dessas preocupações com a centralização, os benefícios práticos geralmente superam os riscos teóricos para muitos casos de uso. A fiabilidade melhorada, o conjunto abrangente de funcionalidades e a experiência superior do utilizador permitem que os programadores do wallet se concentrem nas inovações da camada de aplicação em vez da gestão da infraestrutura Lightning. Esta divisão de trabalho reflecte um ecossistema em amadurecimento em que os fornecedores de serviços especializados lidam com desafios técnicos complexos, permitindo que os programadores de aplicações se concentrem na experiência do utilizador e na lógica empresarial. A chave está em entender claramente essas compensações e tomar decisões informadas com base em requisitos de casos de uso específicos e níveis de tolerância a riscos.




# Secção final

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Comentários e classificações

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusão

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>