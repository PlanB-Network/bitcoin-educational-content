---
term: TRANSPORTE P2P V2

---
Nova versão do protocolo de transporte Bitcoin P2P que incorpora encriptação oportunista para melhorar a privacidade e a segurança das comunicações entre nós. Esta melhoria visa resolver vários problemas com a versão básica do protocolo P2P, nomeadamente tornando os dados trocados indistinguíveis para um observador passivo (como um fornecedor de serviços Internet), reduzindo assim os riscos de censura e ataques através da deteção de padrões específicos nos pacotes de dados.

A encriptação implementada não inclui autenticação, para evitar acrescentar complexidade desnecessária e não comprometer a natureza sem permissões da ligação de rede. Este novo protocolo de transporte P2P oferece, no entanto, uma melhor segurança contra ataques passivos e torna os ataques activos significativamente mais onerosos e detectáveis (nomeadamente os ataques MITM). A introdução de um fluxo de dados pseudo-aleatório complica a tarefa dos atacantes que pretendem censurar ou manipular as comunicações.

O P2P Transport V2 foi incluído como uma opção (desativado por padrão) na versão 26.0 do Bitcoin Core, implantado em dezembro de 2023. Ele pode ser ativado com a opção `v2transport=1` no arquivo de configuração.