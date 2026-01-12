---
name: Ashigaru - Whirlpool Coinjoin
description: ¿Cómo hago coinjoins en la aplicación Ashigaru?
---

![cover](assets/cover.webp)



"*un bitcoin wallet para las calles*"



En este tutorial, aprenderás qué es un coinjoin y cómo hacer uno con la aplicación Ashigaru Terminal y la implementación Whirlpool, un protocolo coinjoin heredado de Samourai Wallet.



## Funcionamiento de las articulaciones articuladas Whirlpool



En este tutorial, no volveré sobre la noción de coinjoin, su utilidad o el funcionamiento teórico de Whirlpool, ya que estos temas ya se explican detalladamente en la parte 5 del curso de formación BTC 204 en Plan ₿ Academy. Si aún no dominas el funcionamiento de Whirlpool o el principio de un coinjoin, te recomiendo encarecidamente que consultes esta parte 5 antes de continuar :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Sin embargo, he aquí algunos datos y cifras que pueden ser útiles.



Las carteras compatibles con Whirlpool utilizan 4 cuentas separadas para satisfacer las necesidades del proceso de coinjoin:




- La cuenta **Depósito**, identificada por el índice `0'` ;
- La cuenta **Banco Malo** (o *cambio de divisas*), identificada por el índice `2.147.483.644'` ;
- La cuenta **Premix**, identificada por el índice `2 147 483 645'` ;
- La cuenta **Postmix**, identificada por el índice `2 147 483 646'`.



En Ashigaru, en noviembre de 2025, hay disponibles dos denominaciones de pool (esta lista probablemente evolucionará en los próximos meses: así que recuerda comprobar los valores a medida que lees):




- 0.25 BTC`, con una cuota de inscripción de `0,0125 BTC`;
- 0.025 BTC, con una cuota de inscripción de 0,00125 BTC.



Cada ciclo de mezcla puede implicar entre 5 y 10 UTXOs en entrada y salida.



![Image](assets/fr/01.webp)



## Requisitos de software



Para hacer coinjoins con Whirlpool, necesitará tres programas distintos:





- Ashigaru Terminal**, que te permite gestionar tus coinjoins directamente desde tu ordenador;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, la aplicación en tu smartphone con la que podrás gastar tus bitcoins en *postmix* desde cualquier lugar ;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, una implementación de nodo Bitcoin que le garantiza una conexión soberana a la red, sin depender de un servidor de terceros.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Instala cada una de estas herramientas siguiendo sus respectivos tutoriales y ya puedes empezar a hacer tus primeros coinjoins.



## Recibir bitcoins



Después de crear su cartera, empezará con una sola cuenta, identificada por el índice `0`. Se trata de la cuenta "Depósito". Es a esta cuenta a la que enviarás bitcoins destinados a coinjoins. Puedes recibirlos a través de la aplicación Ashigaru (ver parte 5 del tutorial dedicado), o a través del Terminal Ashigaru (también detallado en la parte 5 del tutorial dedicado).



Una vez que su cuenta de depósito contenga al menos la cantidad necesaria para participar en el fondo común más pequeño (más los gastos de servicio y el mínimo requerido para cubrir los costes de mining) estará listo para iniciar sus primeras coinjoins.



![Image](assets/fr/02.webp)



## Hacer que el Tx0



Una vez que los fondos hayan llegado a su cuenta de depósito y la transacción haya sido confirmada, puede iniciar el proceso de coinjoin. Para ello, en el Terminal Ashigaru, abra el menú "Monederos" y seleccione su wallet. Si su wallet está bloqueada, el software le pedirá su contraseña y su passphrase.



![Image](assets/fr/03.webp)



A continuación, seleccione la cuenta "Depósito".



![Image](assets/fr/04.webp)



Vaya al menú `UTXOs`.



![Image](assets/fr/05.webp)



Aquí verás una lista de todos los UTXOs en tu cuenta de depósito. Selecciona los que deseas enviar en los ciclos coinjoin.



Para una mayor confidencialidad y para evitar la *Heurística de entrada común Ownership (CIOH)*, se recomienda utilizar sólo una UTXO por entrada en Whirlpool (en BTC 204 encontrará una explicación detallada de este principio).



Pulse la tecla `ENTER` de su teclado para seleccionar un UTXO: aparecerá un asterisco `(*)` junto a él para indicar que está seleccionado.



![Image](assets/fr/06.webp)



A continuación, haga clic en el botón `Mix Selected`.



![Image](assets/fr/07.webp)



Si tienes una UTXO lo suficientemente grande como para participar en cualquiera de los dos pools disponibles, puedes seleccionar el pool de destino utilizando las flechas. En esta página, verás los detalles de tu Tx0 :




- el número de UTXOs que entrarán en el pool;
- las distintas tasas aplicadas (tasas de servicio y tasas mining) ;
- la cantidad del *cambio dóxico*.



Compruebe la información cuidadosamente, luego haga clic en `Broadcast` para transmitir el Tx0.



![Image](assets/fr/08.webp)



Ashigaru mostrará entonces el TXID de su Tx0, confirmando que la transacción ha sido emitida en la red.



![Image](assets/fr/09.webp)



## Cómo hacer coinjoins



Una vez emitido el Tx0, vuelva a la página de inicio de su cuenta de depósito, haga clic en `Cuentas` y seleccione la cuenta `Premix`.



![Image](assets/fr/10.webp)



En el menú `UTXOs`, verá las distintas partes igualadas, listas para entrar en los ciclos de coinjoin. En cuanto se confirme Tx0, el Terminal Ashigaru iniciará automáticamente su primer ciclo de mezcla.



![Image](assets/fr/11.webp)



Una vez confirmada la Tx0, la primera transacción coinjoin será creada y emitida automáticamente por Ashigaru Terminal. Accediendo a `Cuentas > Postmix > UTXOs`, podrá ver sus UTXOs igualados, a la espera de la confirmación de su primer ciclo.



![Image](assets/fr/12.webp)



Ahora puede dejar Ashigaru Terminal funcionando en segundo plano: continuará mezclando y remezclando sus pistas automáticamente.



## Acabado de uniones



Ahora puede dejar que sus monedas se remezclen automáticamente. El modelo Whirlpool significa que no hay cargos adicionales por la remezcla: ni cuotas de servicio, ni cuotas mining. Así que dejar que tus monedas participen en más ciclos de mezcla sólo puede beneficiar a tu confidencialidad.



Para entender mejor este mecanismo y cuántos ciclos merece la pena esperar, recomiendo leer este artículo:



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Para ver el número de remezclas realizadas por cada una de tus piezas, abre el menú `UTXOs` en la cuenta `Postmix`.



![Image](assets/fr/13.webp)



Para gastar sus monedas mezcladas, vaya a la aplicación Ashigaru, que utiliza la misma wallet que su software Ashigaru Terminal. La wallet que aparece al abrirla corresponde a su cuenta `Deposit`. Para acceder a la cuenta `Postmix`, que contiene sus UTXOs mezclados, haga clic en el símbolo Whirlpool de la esquina superior derecha.



![Image](assets/fr/14.webp)



En esta cuenta, verás todas tus monedas mezcladas en ese momento. Para gastarlas, pulsa el símbolo `+` en la parte inferior derecha de la pantalla y selecciona `Enviar`.



![Image](assets/fr/15.webp)



Rellene los datos de su transacción: la dirección del destinatario, el importe a enviar y, si lo desea, elija una estructura de transacción específica para reforzar aún más su confidencialidad (consulte los tutoriales correspondientes).



![Image](assets/fr/16.webp)



Compruebe cuidadosamente los detalles de la transacción y, a continuación, arrastre la flecha situada en la parte inferior de la pantalla para confirmar el envío.



![Image](assets/fr/17.webp)



Su transacción ha sido firmada y difundida en la red Bitcoin.



![Image](assets/fr/18.webp)



## Gastar el cambio doxémico



Recuerde: El modelo de Whirlpool se basa en la igualación de sus piezas en Tx0, antes de que entren en las piscinas. Es este mecanismo el que rompe el seguimiento de UTXOs. En mi opinión, este es el modelo de coinjoin más eficiente, pero tiene un inconveniente: genera un *cambio* que no pasa por el proceso de coinjoin.



Este cambio corresponde a un UTXO creado para cada Tx0. Se aísla en una cuenta específica denominada `Cambio Tóxico` o `Banco Malo`, según el software, para evitar utilizarlo con tus otros UTXOs. Esto es muy importante, porque estos UTXOs no han sido mezclados: sus vínculos de trazabilidad permanecen intactos, y pueden comprometer tu confidencialidad estableciendo una conexión entre tú y tu actividad coinjoin. Así que manipúlalos con cuidado y **nunca los utilices con otros UTXO**, mezclados o no. Combinar un UTXO tóxico con un UTXO mixto anulará todas las ganancias de confidencialidad que hayas obtenido al coinjoin.



Por el momento, Ashigaru no ofrece acceso directo a esta cuenta `Doxxic Change` (al menos, yo no lo he encontrado). Esta característica se añadirá probablemente en una futura actualización. Mientras tanto, la única forma de recuperar estos fondos es importar tu seed a Sparrow Wallet. Normalmente, esta última detectará automáticamente que se trata de una wallet utilizada con Whirlpool y te dará acceso a las cuatro cuentas, incluida la cuenta `Doxxic Change`. Entonces podrás gastar estos UTXOs como bitcoins normales desde Sparrow.



He aquí varias estrategias posibles para gestionar tus UTXOs de divisas de coinjoins sin comprometer tu privacidad:





- Mezclándolos en pools más pequeños:** Si tu UTXO tóxico es lo suficientemente grande como para unirse a un pool más pequeño, ésta suele ser la mejor opción. Sin embargo, ten cuidado de no fusionar nunca varios UTXO tóxicos para conseguirlo, ya que esto creará un vínculo entre tus distintas entradas en Whirlpool.





- Márquelos como no gastables:** Otro enfoque prudente es simplemente mantenerlos tal cual en su cuenta separada y dejarlos sin tocar. Esto evitará que los gaste accidentalmente. Si el valor del bitcoin aumenta, podrían abrirse nuevos pools adaptados a su tamaño.





- Hacer donaciones:** Puedes optar por convertir estos UTXO tóxicos en donaciones a desarrolladores de Bitcoin, proyectos de código abierto o asociaciones que acepten BTC. Esto te permite deshacerte de ellos de forma útil a la vez que apoyas el ecosistema.





- Compra tarjetas regalo prepago o tarjetas Visa:** Plataformas como [Bitrefill](https://www.bitrefill.com/) te permiten canjear tus bitcoins por tarjetas regalo o tarjetas Visa recargables que puedes utilizar en comercios. Esta puede ser una forma sencilla y discreta de gastar tus UTXO tóxicos.





- Cámbialos por Monero:** Samourai Wallet solía ofrecer un servicio de intercambio atómico BTC/XMR ya desaparecido. Si existe un servicio similar (personalmente no conozco ninguno), es una solución excelente para aislar estos UTXOs, convertirlos a Monero, y después eventualmente enviarlos de vuelta a Bitcoin. Sin embargo, este método era caro y dependía de la liquidez disponible.





- Transferirlos a la Lightning Network:** Transferir estos UTXO a la Lightning Network para beneficiarse de tarifas de transacción reducidas es una opción potencialmente interesante. Sin embargo, este método puede revelar cierta información en función del uso que hagas de Lightning, por lo que debe utilizarse con precaución.



## ¿Cómo puedo conocer la calidad de nuestros ciclos de coinjoin?



Para que una coinjoin sea realmente eficaz, debe presentar un alto grado de uniformidad entre los importes de entrada y de salida. Esta uniformidad aumenta el número de interpretaciones posibles para un observador externo, lo que a su vez aumenta la incertidumbre sobre la transacción. Para medir esta incertidumbre, utilizamos el concepto de entropía aplicado a la transacción. El modelo Whirlpool es reconocido como uno de los más eficaces a este respecto, ya que garantiza una excelente homogeneidad entre los participantes. Para profundizar en este principio, le recomiendo que consulte el último capítulo de la Parte 5 del curso de formación BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

El rendimiento de varios ciclos coinjoin se mide por el tamaño de los conjuntos en los que se oculta una moneda. Estos conjuntos definen lo que se conoce como *conjuntos anónimos*. Existen dos tipos: el primero mide la confidencialidad frente al análisis retrospectivo (del presente al pasado), y el segundo mide la resistencia al análisis prospectivo (del pasado al presente). Para una explicación completa de estos dos indicadores, lea el siguiente tutorial (o, una vez más, el curso de formación BTC 204):



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## ¿Cómo gestionar la postmezcla?



Después de ejecutar varios ciclos de coinjoin, la mejor estrategia es mantener tus UTXOs en la cuenta `Postmix`, dejándolos remezclar indefinidamente hasta que realmente necesites gastarlos.



Algunos usuarios prefieren transferir sus bitcoins mezclados a un wallet asegurado por hardware wallet. Esta opción es posible, pero requiere cierto rigor para garantizar que la confidencialidad adquirida con coinjoins no se vea comprometida.



Fusionar UTXOs es el error más frecuente. Es importante no combinar nunca UTXOs mezclados con UTXOs no mezclados en la misma transacción, ya que de lo contrario se corre el riesgo de activar la *Heurística de Entrada Común Ownership (CIOH)*. Esto implica una gestión rigurosa de sus UTXO, especialmente mediante un etiquetado claro y preciso. En general, la fusión de UTXOs es una mala práctica que a menudo conduce a una pérdida de confidencialidad cuando se gestiona mal.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

También debe ser prudente a la hora de consolidar UTXOs mixtos. Se pueden considerar consolidaciones limitadas si los UTXO tienen anonsets significativos, pero inevitablemente reducen su nivel de confidencialidad. Evite las consolidaciones masivas o apresuradas, realizadas antes de un número suficiente de remezclas, ya que podrían establecer vínculos inferenciales entre sus piezas anteriores y posteriores a la remezcla. En caso de duda, lo mejor es no consolidar sus UTXO postmezcla y transferirlos uno a uno a su hardware wallet, generando cada vez una nueva dirección de recepción en blanco. No olvide etiquetar cada UTXO transferido.



Le desaconsejamos encarecidamente que traslade sus UTXOs postmix a carteras que utilicen scripts minoritarios. Por ejemplo, si participaste en Whirlpool desde una cartera multi-sig en `P2WSH`, seréis pocos los que compartáis este tipo de script. Al enviar tus UTXOs postmix a este mismo tipo de script, reduces considerablemente tu anonimato. Más allá del tipo de script, otras huellas específicas de wallet pueden comprometer tu confidencialidad, así que lo mejor que puedes hacer es gastarlas desde la aplicación Ashigaru.



Por último, como en todas las transacciones de Bitcoin, no reutilice nunca una dirección de recepción. Cada pago debe enviarse a una dirección nueva, única y en blanco.



El método más simple y seguro es dejar que tus UTXOs mezclados descansen en su cuenta `Postmix`, dejar que se remezclen de forma natural, y sólo gastarlos cuando sea necesario desde Ashigaru.



Los monederos Ashigaru y Sparrow incorporan salvaguardas adicionales contra los errores más comunes asociados al análisis de blockchain, ayudándole a preservar la confidencialidad de sus transacciones.