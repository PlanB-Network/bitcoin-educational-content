---
term: COOKIE (.COOKIE)

---
Arquivo usado para autenticação RPC (*Remote Procedure Call*) no Bitcoin Core. Quando o bitcoind inicia, ele gera um cookie de autenticação único e o armazena neste arquivo. Clientes ou scripts que desejam interagir com o bitcoind através da interface RPC podem usar este cookie para autenticar de forma segura. Este mecanismo permite uma comunicação segura entre o bitcoind e aplicações externas (como software de carteira, por exemplo), sem requerer gestão manual de nomes de utilizador e palavras-passe. O arquivo `.cookie` é regenerado a cada reinicialização do bitcoind e excluído no desligamento.