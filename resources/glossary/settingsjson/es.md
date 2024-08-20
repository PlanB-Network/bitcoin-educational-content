---
term: SETTINGS.JSON
---

Archivo utilizado en Bitcoin Core para almacenar las configuraciones de la interfaz gráfica de usuario (GUI). Retiene información sobre configuraciones de usuario, como las carteras abiertas, por ejemplo. Cuando Bitcoin Core se reinicia, este archivo permite la reapertura automática de las carteras que estaban activas antes de que la aplicación se cerrara. Si una cartera se cierra a través de la GUI, también se elimina de este archivo y, por lo tanto, no se reabrirá automáticamente en el próximo inicio.