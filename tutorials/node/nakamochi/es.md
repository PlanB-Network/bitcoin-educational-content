---
name: Nakamochi
description: Ejecución de nodos simplificada - Cómo configurar y usar el nodo Nakamochi Bitcoin y Lightning.
---
![image](assets/cover.webp)

Gestionar tu propio nodo completo de Bitcoin y Lightning ya no tiene por qué ser una tarea compleja limitada a expertos técnicos. Tradicionalmente, la configuración y gestión de nodos ha exigido profundos conocimientos de criptografía, redes y desarrollo de software. Nakamochi cambia esta situación haciendo que los nodos sean accesibles a todo el mundo, independientemente de sus conocimientos técnicos.

Con Nakamochi, cualquiera puede montar y operar un nodo desde casa, lo que permite una total privacidad e independencia financiera. Dirigir un nodo completo no sólo asegura tus propias transacciones, sino que también contribuye a la fortaleza de la red Bitcoin. Una red Bitcoin descentralizada y resistente depende de una amplia distribución de nodos para garantizar su seguridad e independencia.

### Índice


- ¿Qué es el Nakamochi y cómo funciona?
- Creación de Nakamochi
- Acerca de la Red Lightning
- Abrir canales y realizar transacciones en Lightning Network

## ¿Qué es el Nakamochi y cómo funciona?

Nakamochi es un nodo completo exclusivo de Bitcoin compatible con las redes Bitcoin y Lightning. Incluye un monedero Bitcoin y Lightning integrado, lo que permite a los usuarios ejecutar un nodo Bitcoin seguro y autosuficiente a la vez que se benefician de la velocidad y los bajos costes de transacción de la red Lightning.

Tu nodo Nakamochi se gestiona a través de una aplicación móvil, [BitBanana (Android)](https://bitbanana.app) y [Zeus (iOS)](https://bitbanana.app), que te permite controlarlo cómodamente desde cualquier lugar. Estas aplicaciones actúan como un control remoto para tu nodo, permitiéndote pagar directamente con Bitcoin o Lightning, gestionar transacciones, abrir o cerrar canales, comprobar saldos y supervisar el rendimiento de tu nodo, todo con facilidad.

## Configurar Nakamochi sólo lleva 5 minutos

### Paso 1: Conéctate y empieza

1. Conecta el Nakamochi a la corriente y al Wi-Fi.

2. Haz clic en **"Configurar nueva cartera"** y guarda de forma segura tu frase de recuperación de 24 palabras.

3. Utiliza una aplicación de gestión de nodos (Zeus o BitBanana) para conectarte a tu Nakamochi:

4. Abre la aplicación y escanea el código QR que aparece en tu Nakamochi.

5. Para mayor seguridad, configura un código PIN en tu dispositivo.

![image](assets/en/01.webp)

_Conéctese a la corriente y anote su frase semilla de 24 palabras_

![image](assets/en/02.webp)

_Espere hasta que la cadena de bloques se haya puesto al día_

![image](assets/en/03.webp)

_Configure una nueva billetera en la pestaña Lightning_

![image](assets/en/04.webp)

_Escanee el código QR con la aplicación de gestión de nodos_

![image](assets/en/05.webp)

_Para mayor seguridad configure un código PIN_

**Nota:** _Permita que su nodo Nakamochi se sincronice con la cadena de bloques. Este proceso puede tardar un tiempo dependiendo de su conexión a internet._

## Acerca de la Red Lightning

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

La red Bitcoin Lightning revoluciona las transacciones de Bitcoin haciéndolas más rápidas, baratas y eficientes. Es perfecta para el uso diario, ya que permite pagos casi instantáneos con comisiones mínimas, ideales para microtransacciones como comprar un café o gestionar pequeñas compras frecuentes.

Al operar fuera de la cadena de bloques, Lightning está diseñado para escalar, soportando miles de transacciones por segundo sin sobrecargar la cadena de bloques principal de Bitcoin. Esto lo convierte en un actor clave en la evolución de Bitcoin hacia un sistema de pagos práctico y global.

La privacidad es otra ventaja, ya que las transacciones en Lightning se dirigen a través de canales de pago privados en lugar de registrarse directamente en la cadena de bloques. Esto garantiza una forma más discreta de realizar transacciones, al tiempo que se mantiene la sólida seguridad de Bitcoin.

#### Explicación de los canales de pago

La red Lightning funciona a través de canales de pago, que son conexiones entre dos partes que permiten múltiples transacciones sin interactuar directamente con la blockchain. Cuando un canal está abierto, el saldo entre las dos partes se actualiza en esta solución Lightning de segunda capa para cada transacción, lo que garantiza pagos rápidos y de bajo coste. Este diseño garantiza la escalabilidad y la privacidad, ya que las transacciones individuales no quedan registradas en el libro mayor público.

**Ejemplo:** Alice y Bob abren un canal depositando Bitcoin en él. Alice envía Bitcoins a Bob, y sus balances fuera de la cadena se actualizan instantáneamente sin un registro"on chain". Si Alice paga a Charlie, y Alice no tiene un canal directo con Charlie, el pago puede ser enrutado a través del canal de Bob para llegar a Charlie. El enrutamiento a través de nodos intermediarios garantiza los pagos incluso sin conexiones directas, lo que hace que la red sea muy eficiente.

## Abrir canales y realizar transacciones en Lightning Network

Una vez que tu Nakamochi está configurado y conectado a una aplicación de gestión de nodos, puedes empezar a utilizar la red Lightning abriendo canales y realizando transacciones.

### Abrir canales en Zeus (iOS):

1. Ve a la pestaña **"Canales"** (menú inferior).

2. Haz clic en el signo **"+"** para abrir un nuevo canal.

3. Escanea o introduce la pubkey del nodo al que deseas conectarte.

4. Introduce la cantidad bloqueada (elije con tu par o utiliza la cantidad fija mínima para nodos conocidos).

5. Haz clic en **"Abrir canal"**.

![image](assets/en/06.webp)

captura de pantalla de ZEUS

Para más información: [Canales | Documentación Zeus](https://docs.zeusln.app/)

### Abrir canales en BitBanana (Android):

1. Abre el menú hamburguesa (izquierda).

2. Ve a **"Canales"**.

3. Haz clic en el signo **"+"** para añadir o abrir un nuevo canal.

4. Escanea o pega la pubkey.

5. Introduce la cantidad bloqueada (elije con tu par o utiliza la cantidad fija mínima para nodos conocidos).

![image](assets/en/07.webp)

captura de pantalla de Bitbanana

Para más información: [BitBanana](https://bitbanana.com)

Una vez abierto tu canal, los pagos pueden enrutarse a través de él a otros participantes en la red. Los saldos se ajustan fuera de la cadena, lo que garantiza que las transacciones sean casi instantáneas e incurran en comisiones mínimas.

Si ya no necesitas un canal, puedes cerrarlo. Esta acción liquida el saldo final entre tú y tu par y lo registra en la cadena. Lo ideal es que ambas partes estén de acuerdo y en línea para un"cierre cooperativo" (más rápido y con menos comisiones que un"cierre forzado" con un peer que no responde o está desconectado).

En general, recomendamos dejar los canales abiertos para reducir costes y aumentar la fiabilidad y eficiencia de la red. Al mantener los canales abiertos, se minimizan las comisiones por transacción en la cadena, se evita el tiempo de inactividad por reconexión de canales y se mantiene una capacidad de enrutamiento estable para un procesamiento de pagos sin problemas. Este enfoque fomenta una red sólida y resistente, al tiempo que mejora la experiencia general del usuario y reduce la sobrecarga operativa.

### Enlaces útiles


- [Sobre Nakamochi](https://nakamochi.io/)
- [Suscríbase al boletín de Nakamochi](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)
