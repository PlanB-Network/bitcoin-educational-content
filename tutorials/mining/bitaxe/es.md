---
name: Configuración de un BitAxe
Description: ¿Cómo configurar un BitAxe?
---

### Introducción

BitAxe es un proyecto de código abierto creado por Skot y [disponible en GitHub](https://github.com/skot/bitaxe) que permite la experimentación de minería de forma económica.

Ha reconstruido el funcionamiento del famoso Antminer S19 de Bitmain, el líder del mercado en ASICs, las máquinas especializadas para la minería de bitcoin. Ahora, es posible usar estos potentes chips en nuevos proyectos de código abierto. A diferencia del Nerdminer, BitAxe tiene suficiente potencia de cómputo para conectarse a un pool de minería, lo que te permitirá ganar algunos satoshis regularmente. El Nerdminer, por otro lado, solo puede conectarse a lo que se llama un solopool, que funciona como un boleto de lotería: tienes una pequeña posibilidad de ganar la recompensa completa del bloque.

Hay varias versiones de BitAxe, con diferentes chips y rendimientos:

| Serie del Modelo Bitaxe  | Chip ASIC | Usado En                     | Tasa de Hash Esperada       | Ideal Para                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Serie 100)   | 1 x BM1397| Serie Antminer 17           | 400 GH/s (hasta 450 GH/s)   | Principiantes en minería de Bitcoin, ofreciendo una sólida tasa de hash con un consumo de energía moderado.|
| Bitaxe Ultra (Serie 200) | 1 x BM1366| Antminer S19 XP y S19k Pro  | 500 GH/s (hasta 550 GH/s)   | Mineros serios que buscan equilibrar eficiencia y mayor tasa de hash.                                      |
| Bitaxe Hex (Serie 300)   | 6 x BM1366| Antminer S19k Pro y S19 XP  | 3.0 TH/s (hasta 3.3 TH/s)   | Mineros que buscan escalabilidad y alto rendimiento sin sacrificar eficiencia.                             |
| Bitaxe Supra (Serie 400) | 1 x BM1368| Antminer S21                | 600 GH/s (hasta 700 GH/s)   | Entusiastas serios que buscan las tasas de hash y eficiencia más altas.                                    |

En este tutorial, estaremos usando un BitAxe Ultra 204 equipado con un chip BM1366, usado para el Antminer S19XP. Este ya viene ensamblado y flasheado por el vendedor.

### [La lista de vendedores está disponible en esta página](https://bitaxe.org/legit.html)

![signup](assets/2.webp)

Generalmente, la fuente de alimentación se vende con él. Si no, necesitarás comprar una fuente de alimentación con un cable jack de 5V y al menos 4A.

![signup](assets/1.webp)

### Configuración
Cuando conectes tu BitAxe por primera vez, intentará conectarse a una red Wi-Fi por defecto. Después de cinco intentos, mostrará el nombre de su propia red Wi-Fi para que puedas conectarte a ella y configurarla.
Para hacer esto, puedes usar cualquier computadora o smartphone. Ve a tu configuración Wi-Fi, busca nuevas redes y verás una Wi-Fi llamada Bitaxe_XXXX. Aquí, es `Bitaxe_A859`. Conéctate a esta red Wi-Fi, y automáticamente se abrirá una ventana.

![signup](assets/3.webp)

En esta ventana, haz clic en las tres pequeñas barras horizontales en la parte superior izquierda, luego en `Settings`.

![signup](assets/4.webp)

Necesitarás ingresar manualmente la información de tu red Wi-Fi, ya que no hay un sistema de descubrimiento automático.
![signup](assets/5.webp)
Por lo tanto, indica el SSID de la Wi-Fi, es decir, el nombre de tu red, la contraseña, así como la información del pool de minería que hayas elegido. Ten cuidado, aquí la URL del pool no se presenta de la misma manera. Por ejemplo, para Braiins, la URL del pool proporcionada es: `stratum+tcp://eu.stratum.braiins.com:3333`.

![signup](assets/6.webp)

Como puedes ver en la pantalla, necesitas eliminar las partes `stratum+tcp://` y `:3333`, dejando solo `eu.stratum.braiins.com`. Luego, en el campo `Port`, introduce los 4 dígitos al final de la URL proporcionada por el pool, pero sin el `:`. Aquí, por lo tanto, es `3333`.

En este tutorial, estamos usando el pool de minería Braiins, pero eres libre de elegir otro. Puedes encontrar nuestros tutoriales sobre pools de minería [en el sitio web de PlanB Network](https://planb.network/en/tutorials/mining).

A continuación, en `User`, introduce tu identificador y luego la `Password`, usualmente, es `"x"` o `"Anything123"`.

La configuración de `Core Voltage` debe dejarse en `1200` por defecto, y para `Frequency`, también deja el valor predeterminado inicialmente. Será posible ajustar esta configuración más tarde para obtener más potencia de cómputo. Sin embargo, es importante asegurarse de que la temperatura del chip no exceda los 65-70°C, ya que el BitAxe no tiene un sistema para reducir el rendimiento en caso de sobrecalentamiento. Si la temperatura excede demasiado los 65°C, podría dañar tu BitAxe.

![signup](assets/7.webp)

Una vez que hayas ingresado correctamente todos los ajustes, haz clic en el botón `Save` en la parte inferior, luego reinicia tu BitAxe simplemente desenchufándolo y volviéndolo a enchufar.
Si has ingresado tu información correctamente, el dispositivo debería conectarse rápidamente a tu Wi-Fi, luego al pool de minería, y comenzar a mostrar información en su pequeña pantalla. Probablemente tomará unos minutos para que aparezca en el tablero de control del pool de minería.
### Tablero de Control y Pantalla

Tres pantallas diferentes se desplazarán. En la tercera página, verás la información de `IP`, que es la dirección IP que te permite conectarte al tablero de control. Aquí, la dirección es `192.168.1.19`.

![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)

Para acceder al tablero de control, simplemente introduce esta dirección en tu navegador de internet.

En el tablero de control, encontrarás toda la información mostrada en la pequeña pantalla, la cual ahora veremos en detalle.

![signup](assets/11.webp)

| Pantalla BitAxe | Tablero de Control                         | Descripción                                                                                                                                                                                                               |
| --------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh              | Hashrate                                    | La potencia de cómputo actual, expresada en GigaHash/s                                                                                                                                                                    |
| W/THs           | Eficiencia                                 | Esta es la eficiencia de tu BitAxe expresada en W/THs. Es la relación entre la potencia eléctrica consumida y la potencia de cómputo producida.                                                                            |
| A/R             | Shares                                      | Cantidad de `Shares` enviadas por tu BitAxe al pool, representando la cantidad de trabajo proporcionado.                                                                                                                 |
| UT              | Uptime                                      | Tiempo desde que tu BitAxe ha estado operando sin interrupción (disponible en el menú de la izquierda bajo `Logs`).                                                                                                      |
| BD            | Mejor Dificultad                            | Máxima dificultad alcanzada desde el último reinicio. Para comparar, la dificultad actual de la red es de aproximadamente 85T.                                                                                             |
| FAN           | FAN en la caja de `Calor`                   | Velocidad de rotación del ventilador, expresada en rotaciones por minuto.                                                                                                                                                  |
| Temp          | Temperatura ASIC en la caja de `Calor`      | Temperatura del chip, la cual no debe exceder los 65°C.                                                                                                                                                                    |
| Pwr           | Potencia                                    | Potencia en vatios consumida. Sin embargo, esta información no toma en cuenta la pantalla, el ventilador, ni la fuente de alimentación. Por ejemplo, cuando muestra 11.7W, el consumo total es en realidad de 15.8W.      |
| mV mA         | Voltaje de Entrada Corriente de Entrada     | Voltaje y corriente consumidos por la máquina. La potencia en vatios es igual al voltaje multiplicado por la corriente.                                                                                                    |
| FH            | Memoria Libre Disponible (menú izquierdo -> `Logs`) | La memoria disponible.                                                                                                                                                                                                   |
| vCore         | Voltaje ASIC (en la caja de Rendimiento)    | Voltaje medido en el chip ASIC.                                                                                                                                                                                           |
| IP            | NA                                          | Dirección IP.                                                                                                                                                                                                             |
| V2.1.0        | Versión (menú izquierdo -> `Logs`)          | Versión del firmware.                                                                                                                                                                                                     |
Puedes cambiar la configuración de Wi-Fi o del pool en cualquier momento sin ningún problema.
Dependiendo de la ventilación y la temperatura de tu habitación, puede que necesites aumentar o quizás disminuir el rendimiento para que la temperatura no exceda los 65°C. Si aumentas el rendimiento, ganarás más satoshis, ¡pero tu BitAxe también consumirá más electricidad!