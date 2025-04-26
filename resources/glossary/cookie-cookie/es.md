---
term: COOKIE (.COOKIE)

---
Archivo utilizado para la autenticación RPC (*Remote Procedure Call*) en Bitcoin Core. Cuando bitcoind se inicia, genera una cookie de autenticación única y la almacena en este archivo. Los clientes o scripts que deseen interactuar con bitcoind a través de la interfaz RPC pueden utilizar esta cookie para autenticarse de forma segura. Este mecanismo permite una comunicación segura entre bitcoind y aplicaciones externas (como software de monedero, por ejemplo), sin necesidad de gestionar manualmente nombres de usuario y contraseñas. El archivo `.cookie` se regenera cada vez que se reinicia bitcoind y se elimina al apagarlo.