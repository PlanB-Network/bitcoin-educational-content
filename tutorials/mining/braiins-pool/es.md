---
name: Braiins Pool

description: Introducción a Braiins Pool
---

![signup](assets/cover.webp)

Braiins Pool, anteriormente conocido como Slush Pool, es el primer pool de minería de Bitcoin. Establecido en noviembre de 2010, minó su primer bloque el 16 de diciembre de 2010, el bloque 97834.

Para mayo de 2024, Braiins Pool cuenta con una potencia de cómputo de 13 EH/s, lo que representa aproximadamente el 1.8% del total del hashrate de Bitcoin. Ha minado un total de 1,307,188 bitcoins, lo que es aproximadamente el 6% de los 21 millones máximos de bitcoins que existirán.

### Sistema de Compensación

Desde finales de 2023, Braiins Pool ha cambiado su sistema de compensación para adoptar el sistema FPPS (Full Pay Per Share). Esto significa que los mineros reciben recompensas todos los días por todo su trabajo del día anterior, incluso si el pool no encontró un bloque. Esto difiere del sistema antiguo donde los mineros solo recibían una recompensa cuando el pool encontraba un bloque.

**Es importante destacar, [según un tweet de Mononaut](https://x.com/mononautical/status/1777686545715089605) quien analiza la TimeChain de Bitcoin, que muchos pools de minería que utilizan el sistema FPPS enviarían los bitcoins minados a una dirección de AntPool, lo que significaría que AntPool controla el hashrate de todos estos pools, aproximadamente el 47% del hashrate global de Bitcoin. Esto es una muy mala noticia para la descentralización de la red.**

### Tarifas del Pool

Las tarifas de Braiins Pool son del 2.5%, sin embargo, si usas BraiinsOS en tus máquinas las tarifas serán del 0%

### Retiros

**Retiros Lightning**
Los retiros Lightning te permiten retirar tus recompensas sin un monto mínimo una vez al día a través de una dirección Lightning.
Para usar este método, debes tener una billetera compatible con direcciones Lightning.

**Retiros On-Chain**
Los retiros On-Chain están limitados a un monto mínimo y pueden estar sujetos a tarifas.
Monto mínimo: 20,000 sats
Tarifas: 10,000 sats para montos menores a 500,000 sats
Gratis para montos superiores a 500,000 sats
Los retiros pueden ser activados por intervalo de tiempo o por cantidad.

## Creación de Cuenta

Para comenzar a usar Braiins Pool [ve a su sitio web](https://braiins.com/pool) y haz clic en "SIGN UP" en la parte superior derecha


![signup](assets/3.webp)

Ingresa tu información y valida, luego recibirás un correo electrónico solicitando la confirmación de tu dirección. Confirma con el enlace en el correo que recibiste y luego inicia sesión en la plataforma

![signup](assets/4.webp)


## Agregando un "worker"
Un worker es el minero que conectarás al pool. Para agregar un nuevo minero, haz clic en "Workers" en el menú lateral izquierdo.
![signup](assets/7.webp)

Luego haz clic en el botón morado "Connect Workers +".

En esta ventana, selecciona tu área geográfica.

Si el minero que deseas conectar usa BraiinsOS, selecciona el protocolo "Stratum V2". De lo contrario, elige "Stratum V1".

![signup](assets/8.webp)

Tendrás la información para ingresar en la página web de tu minero (consulta la documentación de tu minero para saber dónde ingresar esta información).

Aquí, **"stratum+tcp://eu.stratum.braiins.com:3333"** es la URL del pool.
**JimZap.workerName** es tu identificador y el nombre de tu minero, donde JimZap es el identificador y .workerName es el nombre del minero. Si tienes varios mineros, puedes darles el mismo nombre, en cuyo caso su potencia de cómputo se sumará en el tablero de control, o darles nombres diferentes para monitorearlos individualmente.
Y la contraseña siempre es la misma **"anything123"**

Una vez que hayas ingresado esta información en la página web de tu minero y haya comenzado a minar, lo verás aparecer después de unos minutos en el Dashboard de Braiins Pool.

## Resumen del Dashboard

![signup](assets/9.webp)

En el banner superior, puedes ver el hashrate total promedio de todos tus mineros durante 5 minutos, 1 hora y 24 horas. Y un resumen del número de mineros en línea o fuera de línea.
Abajo, un gráfico te permite seguir la evolución de tu potencia de cómputo.

![signup](assets/10.webp)

Debajo de este gráfico, tienes varias piezas de información sobre tus recompensas en sats.

**"Recompensas de Minería de Hoy"** Indica el número de sats que has minado hoy. Al final del día, este valor se restablecerá a 0 y los sats serán enviados a tu cuenta.

**"Recompensa Total de Ayer"** El número de sats que minaste el día anterior

**"Rentabilidad Estimada (1 TH/s)"** Es una estimación del número de sats que ganas en un día por una potencia de cómputo de 1 TH/s. Por ejemplo, si el valor es 77 sats, y tienes una potencia de cómputo de 10 TH/s continuamente durante todo el día, entonces teóricamente ganarías 77 x 10 = 770 sats por día.

**"Recompensa de Todos los Tiempos"** El total de sats que has minado con Braiins Pool

**"Esquema de Recompensa"** La tasa de comisión aplicada por el pool

**"Próximo Pago ETA"** Estimación del tiempo que tomará antes de que puedas retirar los sats de la plataforma. Aquí, la estimación no muestra nada porque la minería solo ha estado en marcha durante unos minutos.

**"Saldo de la Cuenta"** El número de sats disponibles en tu cuenta, que luego puedes retirar.
## Configuración de Retiros
Puedes retirar tus recompensas ya sea en cadena o a través de lightning con una dirección.

En la parte superior, haz clic en "Fondos". Por defecto, tienes una "Cuenta de Bitcoin". Puedes crear otras para compartir las recompensas. Volveremos a esto en la próxima sección.

Por ahora, haz clic en "Configurar".

![signup](assets/17.webp)

En esta nueva ventana, puedes elegir "Pago en cadena".

Nombra esta billetera, proporciona una dirección BTC y selecciona el tipo de disparador que deseas. "Umbral" significa que el pago se activará cuando hayas acumulado una cantidad definida de BTC, y con "Intervalo de tiempo", el pago se activará en intervalos regulares (día/semanas/meses).

Ten en cuenta que la cantidad mínima es 0.0002 BTC y que por debajo de 0.005 BTC, se aplicará una tarifa de 0.0001 BTC.

![signup](assets/18.webp)

Si quieres usar retiros Lightning, necesitarás una billetera que proporcione una dirección Lightning. Por ejemplo, puedes usar getAlby.

Haz clic en la parte superior de la ventana en "Pago Lightning".

Ingresa tu dirección Lightning y marca la casilla "Entiendo..." luego valida.

Con este método de retiro, tus recompensas serán enviadas a tu billetera todos los días.

![signup](assets/14.webp)
Una vez que hayas validado tus configuraciones de pago, recibirás un correo electrónico de confirmación.
![signup](assets/15.webp)

## Compartiendo Recompensas

Braiins Pool también te permite compartir tus recompensas entre múltiples carteras.

Para hacer esto, haz clic en la parte superior en "Mining" y luego a la izquierda en "Settings".

![signup](assets/19.webp)

En esta página, podrás añadir otra "Financial Account" haciendo clic en "Add Another Financial Account" y distribuir tus recompensas en % entre estas diferentes cuentas a las que debes asociar una cartera. Para asociar una nueva cartera con una Financial Account, consulta la sección anterior.