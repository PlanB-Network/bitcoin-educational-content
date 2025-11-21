---
term: CIERRE FORZOSO
---

Mecanismo no cooperativo de cierre de canales Lightning. Cuando dos usuarios abren un canal con un Multisig 2/2, cada uno de ellos puede cerrar unilateralmente el canal emitiendo el último Commitment Transaction ya firmado, para recuperar sus bitcoins onchain. Esto se conoce como "cierre forzado".


Este método se utiliza generalmente si uno de los participantes ya no responde, o si el cierre cooperativo del canal es imposible. Si se puede evitar el cierre forzado, es lo mejor, ya que lleva más tiempo recuperar los fondos onchain y puede ser mucho más caro en términos de comisiones.


En un cierre forzado, uno de los dos usuarios transmite el Commitment Transaction, que refleja el último estado conocido del canal Lightning. Se produce entonces un bloqueo temporal antes de que los bitcoins puedan recuperarse en la cadena, dando tiempo a la otra parte para verificar que la transacción corresponde al último estado del canal. Si un usuario intenta hacer trampas publicando un Commitment Transaction no actualizado, la otra parte puede utilizar el secreto de revocación para castigar al tramposo y recuperar todos los fondos del canal.