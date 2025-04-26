---
term: SETTINGS.JSON

---
Archivo utilizado en Bitcoin Core para almacenar la configuración de la interfaz gráfica de usuario (GUI). Retiene información sobre las configuraciones del usuario, como por ejemplo los monederos abiertos. Cuando se reinicia Bitcoin Core, este archivo permite la reapertura automática de los monederos que estaban activos antes de que se cerrara la aplicación. Si un monedero se cierra a través de la GUI, también se elimina de este archivo, y por lo tanto, no se reabrirá automáticamente en el siguiente arranque.