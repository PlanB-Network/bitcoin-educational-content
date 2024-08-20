---
term: COOKIE (.COOKIE)
---

Archivo utilizado para la autenticación RPC (*Remote Procedure Call* o Llamada a Procedimiento Remoto) en Bitcoin Core. Cuando bitcoind se inicia, genera una cookie de autenticación única y la almacena en este archivo. Los clientes o scripts que deseen interactuar con bitcoind a través de la interfaz RPC pueden usar esta cookie para autenticarse de manera segura. Este mecanismo permite una comunicación segura entre bitcoind y aplicaciones externas (como software de billetera, por ejemplo), sin requerir la gestión manual de nombres de usuario y contraseñas. El archivo `.cookie` se regenera en cada reinicio de bitcoind y se elimina al apagar.