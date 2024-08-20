---
term: COOKIE (.COOKIE)
---

Arquivo usado para autenticação RPC (*Remote Procedure Call* ou Chamada de Procedimento Remoto) no Bitcoin Core. Quando o bitcoind é iniciado, ele gera um cookie de autenticação único e o armazena neste arquivo. Clientes ou scripts que desejam interagir com o bitcoind através da interface RPC podem usar este cookie para se autenticar de forma segura. Esse mecanismo permite uma comunicação segura entre o bitcoind e aplicações externas (como softwares de carteira, por exemplo), sem a necessidade de gerenciamento manual de nomes de usuário e senhas. O arquivo `.cookie` é regenerado a cada reinício do bitcoind e excluído ao desligar.