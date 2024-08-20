---
term: P2P TRANSPORT V2
---

Nova versão do protocolo de transporte P2P do Bitcoin incorporando criptografia oportunista para melhorar a privacidade e segurança das comunicações entre nós. Esta melhoria visa abordar vários problemas com a versão básica do protocolo P2P, notavelmente tornando os dados trocados indistinguíveis para um observador passivo (como um provedor de serviços de internet), reduzindo assim os riscos de censura e ataques através da detecção de padrões específicos nos pacotes de dados.

A criptografia implementada não inclui autenticação para evitar adicionar complexidade desnecessária e para não comprometer a natureza sem permissões da conexão de rede. Este novo protocolo de transporte P2P oferece, no entanto, melhor segurança contra ataques passivos e torna os ataques ativos significativamente mais custosos e detectáveis (notavelmente ataques MITM). A introdução de um fluxo de dados pseudo-aleatório complica a tarefa para atacantes que desejam censurar ou manipular comunicações.

O P2P Transport V2 foi incluído como uma opção (desativada por padrão) na versão 26.0 do Bitcoin Core, implantada em dezembro de 2023. Pode ser ativado com a opção `v2transport=1` no arquivo de configuração.