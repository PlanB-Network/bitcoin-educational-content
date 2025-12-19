---
name: Ashigaru - Ricochet
description: Comprender y utilizar las transacciones de Ricochet
---
![cover ricochet](assets/cover.webp)



> *Una herramienta premium que añade saltos adicionales de historial a su transacción. Sorprende a las listas negras y ayuda a evitar el cierre injusto de cuentas de terceros

## ¿Qué es un Ricochet?



Ricochet es una técnica que consiste en realizar varias transacciones ficticias hacia uno mismo para simular una transferencia de propiedad de bitcoins. Esta herramienta difiere de las demás transacciones de Ashigaru (heredadas de Samurai Wallet) en que no proporciona un anonimato prospectivo, sino más bien una forma de anonimato retrospectivo. De hecho, Ricochet difumina las especificidades que pueden comprometer la fungibilidad de una pieza de Bitcoin.



Por ejemplo, si realizas un coinjoin, la pieza que salga de la mezcla se identificará como tal. Las herramientas de análisis de cadenas son capaces de detectar los paterns de las transacciones coinjoin y asignar una etiqueta a las piezas que salen de ellas. En efecto, coinjoin pretende romper los vínculos históricos de una moneda, pero su paso por coinjoins sigue siendo detectable. Por analogía, este fenómeno se asemeja a la encriptación de un texto: aunque no se pueda acceder al texto original en texto claro, es fácil identificar que se ha aplicado una encriptación.



La etiqueta "coinjoined" puede afectar a la fungibilidad de una UTXO. Las entidades reguladas, como las plataformas de intercambio, pueden negarse a aceptar un UTXO coinjoined, o incluso exigir explicaciones a su propietario, con el riesgo de que se bloquee tu cuenta o se congelen tus fondos. En algunos casos, la plataforma puede incluso denunciar su comportamiento a las autoridades estatales.



Aquí es donde entra en juego el método Ricochet. Para difuminar la huella dejada por un coinjoin, Ricochet ejecuta cuatro transacciones sucesivas en las que el usuario se transfiere a sí mismo sus fondos en diferentes direcciones. Tras esta secuencia de transacciones, la herramienta Ricochet encamina finalmente los bitcoins a su destino final, como una plataforma de intercambio. El objetivo es crear distancia entre la transacción coinjoin original y el acto final de gasto. De este modo, las herramientas de análisis de blockchain supondrán que probablemente se ha producido una transferencia de propiedad tras el coinjoin y que, por tanto, no es necesario emprender acciones contra el emisor.



![image](assets/fr/01.webp)



Frente al método Ricochet, cabría imaginar que los programas informáticos de análisis de cadenas profundizaran en su examen más allá de cuatro rebotes. Sin embargo, estas plataformas se enfrentan a un dilema a la hora de optimizar el umbral de detección. Necesitan establecer un número umbral de saltos a partir del cual acepten que probablemente se ha producido un cambio de propiedad, y que el enlace a un coinjoin anterior debe ignorarse. Sin embargo, determinar este umbral es arriesgado: cada ampliación del número de saltos observados aumenta exponencialmente el volumen de falsos positivos, es decir, individuos marcados erróneamente como participantes en una coinjoin, cuando en realidad la operación fue realizada por otra persona. Este escenario supone un riesgo importante para estas empresas, ya que los falsos positivos provocan insatisfacción, lo que puede llevar a los clientes afectados a la competencia. A largo plazo, un umbral de detección demasiado ambicioso lleva a una plataforma a perder más clientes que sus competidores, lo que podría amenazar su viabilidad. Por ello, es complicado que estas plataformas aumenten el número de rebotes observados, y 4 suele ser un número suficiente para contrarrestar sus análisis.



Así, **el caso de uso más habitual de Ricochet se plantea cuando es necesario ocultar una participación previa en un coinjoin sobre un UTXO del que se es propietario.** Idealmente, lo mejor es evitar transferir bitcoins que hayan sufrido un coinjoin a entidades reguladas. Sin embargo, en el caso de no tener otra opción, sobre todo ante la necesidad urgente de liquidar bitcoins en moneda estatal, Ricochet ofrece una solución eficaz.



## ¿Cómo funciona Ricochet en Ashigaru?



Ricochet es simplemente un método para enviarse bitcoins a uno mismo, inventado originalmente por los desarrolladores de Samurai Wallet. Por lo tanto, es perfectamente posible simular un Ricochet manualmente, sin necesidad de una herramienta especializada. Sin embargo, para aquellos que deseen automatizar el proceso disfrutando de un resultado más pulido, la herramienta Ricochet disponible a través de la aplicación Ashigaru (que es un Samourai fork) representa una buena solución.



Dado que Ashigaru cobra por su servicio, un Ricochet cuesta `100.000 sats` como tasa de servicio, más una tasa de mining. Por tanto, se recomienda su uso para transferencias de cantidades importantes.



La aplicación Ashigaru ofrece dos variantes de Ricochet:





- Ricochet reforzado, o "entrega escalonada", que ofrece la ventaja de repartir los gastos de servicio de Ashigaru entre las cinco transacciones sucesivas. Esta opción también garantiza que cada transacción se emita en un momento distinto y se registre en un bloque diferente, imitando lo más fielmente posible el comportamiento de un cambio de propietario. Aunque más lento, este método es preferible para los que no tienen prisa, ya que maximiza la eficacia de Ricochet reforzando su resistencia al análisis en cadena;





- El Ricochet clásico, concebido para ejecutar la operación con rapidez, difunde todas las transacciones en un intervalo de tiempo reducido. Este método, por lo tanto, ofrece menos confidencialidad y menos resistencia al análisis que el método reforzado. Sólo debe utilizarse para envíos urgentes.



## ¿Cómo hacer un Ricochet en Ashigaru?



Hacer un rebote en Ashigaru es muy sencillo: basta con activar la opción correspondiente al crear una transacción de envío. Para empezar, haga clic en el botón `+`, luego en `Enviar`, y seleccione la cuenta desde la que desea enviar los fondos.



![Image](assets/fr/02.webp)



Rellene la información de la transacción: el importe a enviar y la dirección final del destinatario después de los saltos Ricochet. A continuación, marque la opción `Ricochet`.



![Image](assets/fr/03.webp)



A continuación, puede elegir entre los dos modos de Ricochet analizados en la sección de teoría: Ricochet clásico, en el que todas las transacciones se incluyen en el mismo bloque, o entrega escalonada, que mejora la calidad de Ricochet a costa de un mayor retraso.



Cuando hayas elegido, pulsa la flecha de la parte inferior de la pantalla para confirmar.



![Image](assets/fr/04.webp)



En la siguiente pantalla, verá un resumen completo de su transacción. Aquí es también donde puede ajustar la tasa de comisión de sus transacciones Ricochet en función de las condiciones del mercado. Si todo es de su agrado, arrastre la flecha verde para firmar y distribuir las transacciones de Ricochet.



![Image](assets/fr/05.webp)



Espere mientras se ejecutan automáticamente los distintos saltos.



![Image](assets/fr/06.webp)



Sus transacciones se han emitido correctamente.



![Image](assets/fr/07.webp)



Ahora estás completamente familiarizado con la opción Ricochet disponible en la aplicación Ashigaru. Para ir más allá, te recomiendo que sigas mi curso de formación BTC 204, que te enseñará en detalle cómo reforzar tu confidencialidad onchain.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c