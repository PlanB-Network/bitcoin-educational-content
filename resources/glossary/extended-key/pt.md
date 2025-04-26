---
term: CHAVE ALARGADA

---
Uma sequência de caracteres que combina uma chave (pública ou privada), o seu código de cadeia associado e uma série de metadados. Uma chave estendida compila todos os elementos necessários para derivar chaves filhas num único identificador. São utilizadas em carteiras determinísticas e hierárquicas e podem ser de dois tipos: uma chave pública alargada (utilizada para derivar chaves públicas filhas) ou uma chave privada alargada (utilizada para derivar chaves privadas e públicas filhas). Uma chave alargada inclui, assim, vários dados diferentes, descritos na BIP32, pela ordem seguinte


- O prefixo: `prv` e `pub` são HRP (Human Readable Part) indicando se é uma chave privada estendida (`prv`) ou uma chave pública estendida (`pub`). A primeira letra do prefixo designa a versão da chave estendida: `x` para Legacy ou SegWit V1 no Bitcoin, `t` para Legacy ou SegWit V1 no Bitcoin Testnet, `y` para Nested SegWit no Bitcoin, `u` para Nested SegWit no Bitcoin Testnet, `z` para SegWit V0 no Bitcoin, `v` para SegWit V0 no Bitcoin Testnet.
- A profundidade, que indica o número de derivações da chave mestra para alcançar a chave alargada;
- A impressão digital do pai. Representa os primeiros 4 bytes do `HASH160` da chave pública principal;
- O índice. Este é o número do par entre os seus irmãos a partir do qual a chave alargada é derivada;
- O código da cadeia;
- Um byte de preenchimento se se tratar de uma chave privada `0x00`;
- A chave privada ou pública;
- Uma soma de controlo. Representa os primeiros 4 bytes do `HASH256` do resto da chave alargada.

Na prática, a chave pública alargada é utilizada para gerar endereços de receção e para observar as transacções de uma conta sem expor as chaves privadas associadas. Isto pode permitir, por exemplo, a criação da chamada carteira "watch-only". No entanto, é importante notar que a chave pública alargada é uma informação sensível para a privacidade do utilizador, uma vez que a sua divulgação pode permitir a terceiros rastrear transacções e ver o saldo da conta associada.