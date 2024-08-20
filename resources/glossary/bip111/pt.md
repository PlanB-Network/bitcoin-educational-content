---
term: BIP111
---

Propõe a adição de um bit de serviço chamado `NODE_BLOOM` para permitir que os nós sinalizem explicitamente seu suporte para Filtros Bloom conforme descrito no BIP37. A introdução do `NODE_BLOOM` possibilita aos operadores de nós desabilitar este serviço para reduzir os riscos de DoS. A opção BIP37 é desativada por padrão no Bitcoin Core. Para ativá-la, o parâmetro `peerbloomfilters=1` deve ser inserido no arquivo de configuração.