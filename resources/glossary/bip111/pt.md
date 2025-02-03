---
term: BIP111

---
Propõe a adição de um bit de serviço denominado `NODE_BLOOM` para permitir que os nós sinalizem explicitamente seu suporte a Bloom Filters, conforme descrito no BIP37. A introdução de `NODE_BLOOM` permite aos operadores de nós desativar este serviço de forma a reduzir os riscos de DoS. A opção BIP37 é desabilitada por padrão no Bitcoin Core. Para habilitá-la, o parâmetro `peerbloomfilters=1` deve ser inserido no arquivo de configuração.