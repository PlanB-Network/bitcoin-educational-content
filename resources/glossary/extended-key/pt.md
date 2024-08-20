---
termo: CHAVE ESTENDIDA
---

Uma sequência de caracteres que combina uma chave (pública ou privada), seu código de cadeia associado e uma série de metadados. Uma chave estendida compila todos os elementos necessários para derivar chaves filhas em um único identificador. Elas são usadas em carteiras determinísticas e hierárquicas e podem ser de dois tipos: uma chave pública estendida (usada para derivar chaves públicas filhas) ou uma chave privada estendida (usada para derivar tanto chaves privadas quanto públicas filhas). Uma chave estendida inclui, portanto, várias peças diferentes de dados, descritas no BIP32, na ordem:
* O prefixo: `prv` e `pub` são partes legíveis por humanos (HRP) indicando se é uma chave privada estendida (`prv`) ou uma chave pública estendida (`pub`). A primeira letra do prefixo designa a versão da chave estendida: `x` para Legacy ou SegWit V1 no Bitcoin, `t` para Legacy ou SegWit V1 no Testnet do Bitcoin, `y` para SegWit Aninhado no Bitcoin, `u` para SegWit Aninhado no Testnet do Bitcoin, `z` para SegWit V0 no Bitcoin, `v` para SegWit V0 no Testnet do Bitcoin.
* A profundidade, que indica o número de derivações da chave mestra para alcançar a chave estendida;
* A impressão digital dos pais. Isso representa os primeiros 4 bytes do `HASH160` da chave pública pai;
* O índice. Este é o número do par entre seus irmãos do qual a chave estendida é derivada;
* O código de cadeia;
* Um byte de preenchimento se for uma chave privada `0x00`;
* A chave privada ou pública;
* Um checksum. Representa os primeiros 4 bytes do `HASH256` do resto da chave estendida.

Na prática, a chave pública estendida é usada para gerar endereços de recebimento e observar as transações de uma conta sem expor as chaves privadas associadas. Isso pode permitir, por exemplo, a criação de uma carteira chamada "somente visualização". No entanto, é importante notar que a chave pública estendida é uma informação sensível para a privacidade do usuário, pois sua divulgação pode permitir que terceiros rastreiem transações e vejam o saldo da conta associada.