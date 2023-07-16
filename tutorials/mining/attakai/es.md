---
name: Attakaï

description: transformación de un S9 en calefacción para el hogar
---

![cover](assets/cover.png)

# Attakai - ¡haciendo posible y accesible el home-mining!

La iniciativa "Attakaï" explora la minería de Bitcoin utilizando el calor generado. La guía propone soluciones para adaptar los mineros para su uso como radiadores en viviendas, ofreciendo así más comodidad y ahorro de energía. Bitcoin ajusta automáticamente la dificultad de la minería y recompensa a los mineros por su trabajo. Sin embargo, la concentración de la tasa de hash puede plantear riesgos para la neutralidad de la red. "Attakaï" ofrece una guía práctica para adaptar los mineros de manera económica, permitiendo a los participantes reducir su factura de electricidad y ser recompensados con sats sin KYC.

## Introducción

"Attakaï", que significa "la temperatura ideal" en japonés, es el nombre de la iniciativa que busca descubrir la minería de bitcoin a través de la reutilización del calor lanzada por @ajelexBTC y @BlobOnChain con Découvre Bitcoin. Esta guía de adaptación de un ASIC servirá como base para aprender más sobre la minería, su funcionamiento, su historia reciente y la economía subyacente.

### ¿Por qué reutilizar el calor de un ASIC?

Es importante entender la relación entre la energía y la producción de calor en un sistema eléctrico.

Por una inversión de 1 kW de energía eléctrica, un radiador eléctrico produce 1 kW de calor, ni más ni menos. Los nuevos radiadores no son más eficientes que los radiadores tradicionales. Su ventaja radica en su capacidad para difundir el calor de manera continua y uniforme en una habitación, brindando así más comodidad en comparación con los radiadores tradicionales que alternan entre una alta potencia de calefacción y la falta de calefacción, generando así variaciones regulares de temperatura e incomodidad.

Una computadora, o más ampliamente una tarjeta electrónica, no consume energía para realizar cálculos, simplemente necesita que la energía circule en sus componentes para funcionar. El consumo de energía se debe a la resistencia eléctrica de los componentes que produce pérdidas y, por lo tanto, genera calor, esto es lo que se conoce como el efecto Joule.

Ciertas empresas han tenido la idea de compartir las necesidades de potencia de cálculo y las necesidades de calefacción a través de radiadores/servidores. La idea es distribuir los servidores de una empresa en pequeñas unidades que podrían colocarse en viviendas u oficinas. Sin embargo, esta idea enfrenta varios problemas. Las necesidades de los servidores no están relacionadas con las necesidades de calefacción y las empresas no pueden utilizar las capacidades de cálculo de sus servidores de manera flexible. También existen limitaciones en el ancho de banda que los particulares pueden tener. Todas estas restricciones no permiten que la empresa rentabilice estas costosas instalaciones ni que proporcione un servicio de servidor en línea estable sin tener centros de datos capaces de asumir el relevo cuando no se necesita calefacción.

> "El calor de tu computadora no se desperdicia si necesitas calentar tu hogar. Si utilizas calefacción eléctrica donde vives, entonces el calor de tu computadora no es un desperdicio. Es el mismo costo si generas este calor con tu computadora. Si tienes otro sistema de calefacción más barato que el eléctrico, entonces el desperdicio está solo en la diferencia de costos. Si es verano y utilizas el aire acondicionado, entonces es el doble.
> La creación de bitcoins debería tener lugar donde sea más barato. Tal vez sea donde el clima es frío y donde la calefacción es eléctrica, donde minar se volvería gratuito".
> Satoshi Nakamoto - 8 de agosto de 2010

El Bitcoin y su prueba de trabajo se destacan porque ajustan automáticamente la dificultad de la minería en función de la cantidad de cálculos realizados por toda la red, esta cantidad se llama hashrate y se expresa en hash/segundo. Hoy en día se estima en 280 Exahash/segundo, es decir, 280 billones de billones de hash/segundo. Este hashrate representa trabajo y, por lo tanto, una cantidad de energía gastada. Cuanto mayor sea el hashrate, mayor será la dificultad y viceversa. De esta manera, se puede activar o desactivar un minero de Bitcoin en cualquier momento sin afectar a la red, a diferencia de los radiadores/servidores que requerirían mantenerse estables para ofrecer su servicio. El minero es recompensado por el trabajo realizado en relación con el trabajo de los demás, por pequeña que sea esta participación.

En resumen, un radiador eléctrico y un minero de Bitcoin producen ambos 1 kW de calor por cada 1 kW de electricidad gastada. Sin embargo, el minero también recibe bitcoins como recompensa. Independientemente del precio de la electricidad, del precio del bitcoin o de la competencia en la actividad minera en la red de Bitcoin, es económicamente más ventajoso calentarse con un minero que con un radiador eléctrico.

![Video presentación](https://youtu.be/gKoh44UCSnE)

### La plus-value pour Bitcoin

No entraremos en detalles sobre el funcionamiento de la minería aquí (recursos disponibles en la academia si es necesario). Lo importante de entender es cómo la minería contribuye a la descentralización de Bitcoin. Varias tecnologías ya existentes han sido ingeniosamente combinadas para dar vida al consenso de Nakamoto. Este consenso permite recompensar económicamente a los actores honestos por su participación en el funcionamiento de la red de Bitcoin, al mismo tiempo que desalienta a los actores deshonestos. Este es uno de los puntos clave que permite que la red exista de manera sostenible.

Los actores honestos, aquellos que realizan minería de acuerdo con las reglas, compiten entre sí para obtener la mayor parte posible de la recompensa por la producción de nuevos bloques. Este incentivo económico naturalmente conduce a una forma de centralización, ya que las empresas eligen especializarse en esta actividad lucrativa al reducir sus costos mediante economías de escala. Estos actores industriales tienen una posición ventajosa para la compra, mantenimiento de máquinas y también para la negociación de tarifas de electricidad al por mayor.

> "Al principio, la mayoría de los usuarios ejecutarían nodos de red, pero a medida que la red creciera más allá de cierto punto, sería cada vez más dejada en manos de especialistas con granjas de servidores de hardware especializado. Una batería de servidores solo necesitaría un nodo en la red y el resto de la LAN se conectaría a ese nodo." - Satoshi Nakamoto - 2 de noviembre de 2008

Algunas entidades poseen un porcentaje considerable del hashrate total en grandes granjas de minería. Se puede observar la reciente ola de frío en Estados Unidos, donde una parte importante del hashrate se desconectó para redirigir la energía hacia hogares con una necesidad excepcional de electricidad. Durante varios días, los mineros fueron incentivados económicamente a apagar sus granjas y, por lo tanto, se puede ver este clima excepcional en la curva del hashrate de Bitcoin.

Este tema podría volverse problemático y representa un riesgo importante para la neutralidad de la red. Un actor que posea más del 51% del hashrate podría censurar más fácilmente transacciones si así lo deseara. Por eso es importante distribuir el hashrate entre múltiples actores en lugar de entidades centralizadas que podrían ser más fácilmente confiscadas por un gobierno, por ejemplo.

**Si los mineros están distribuidos en miles, incluso millones de hogares en todo el mundo, se vuelve muy complicado para un Estado tomar el control.**

A su salida de fábrica, un minero no es adecuado para ser utilizado como radiador en una vivienda, debido a dos problemas principales: un ruido excesivo y la falta de ajuste. Sin embargo, estos problemas pueden resolverse fácilmente mediante modificaciones simples realizadas en el hardware y el software, lo que permite obtener un minero mucho más silencioso y que se puede configurar y automatizar como los calentadores eléctricos modernos.

**Attakaï es una iniciativa educativa que te enseña a realizar una adaptación del Antminer S9 de la manera más económica posible.**

Es una excelente oportunidad para aprender practicando. Además de reducir tu factura de electricidad, se te recompensa por tu participación con sats KYC gratuitos.

## Capítulo 1: Guía de compra para un ASIC de segunda mano

En esta sección veremos las buenas prácticas para comprar un Bitmain Antminer S9 de segunda mano, la máquina en la que se basará este tutorial de adaptación a radiador. Esta guía también funciona para otros modelos de ASIC, ya que es una guía de compra general para equipos de minería de segunda mano.

El Antminer S9 es un dispositivo ofrecido por Bitmain desde mayo de 2016. Consume 1323W de electricidad y produce 13,5 TH/s. Aunque se considera antiguo, sigue siendo una excelente opción para comenzar a minar. Dado que se produjo en gran cantidad, es fácil encontrar piezas de repuesto en abundancia en muchas regiones del mundo. Por lo general, se puede adquirir de persona a persona en sitios como Ebay o LeBonCoin, ya que los revendedores dirigidos a profesionales ya no lo ofrecen debido a su menor competitividad en comparación con máquinas más recientes. Es menos eficiente que ASIC como el Antminer S19, que se ofrece desde marzo de 2020, pero esto lo convierte en un equipo de segunda mano asequible y más adecuado para las modificaciones que vamos a realizar.

El Antminer S9 existe en varias variantes (i, j) que realizan modificaciones menores en el hardware de primera generación. No creemos que este elemento deba influir en tu decisión de compra y esta guía funcionará para todas estas variantes.

El precio de los ASIC varía según muchos factores, como el precio del bitcoin, la dificultad de la red, la eficiencia de la máquina y el costo de la electricidad. Por lo tanto, es difícil dar una estimación precisa para la compra de una máquina de segunda mano. En febrero de 2023, el precio esperado en Francia generalmente oscila entre 100€ y 200€, pero estos precios pueden cambiar rápidamente.

![image](assets/guide-achat/1.jpeg)

El Antminer S9 está compuesto por las siguientes partes:

- 3 placas de hash donde se encuentran los chips que producen el hash

![image](assets/guide-achat/2.jpeg)'

- Una tarjeta de control que incluye un espacio para una tarjeta SD, un puerto Ethernet y conectores para las hashboards y los ventiladores. Es el cerebro de tu ASIC.
  ![image](assets/guide-achat/3.jpeg)

- 3 cables de datos que conectan las hashboards con la tarjeta de control.

![image](assets/guide-achat/4.jpeg)

- La fuente de alimentación que funciona con 220V y puede ser conectada como un electrodoméstico común.

![image](assets/guide-achat/5.jpeg)

- 2 ventiladores de 120mm.

![image](assets/guide-achat/6.jpeg)

- Un cable macho C13.

![image](assets/guide-achat/7.jpeg)

Cuando compras una máquina de segunda mano, es importante verificar que todas las piezas estén incluidas y funcionales. Durante el intercambio, debes pedir al vendedor que encienda la máquina para verificar su correcto funcionamiento. Es importante comprobar que el dispositivo se encienda correctamente y luego verificar la conectividad a internet conectando un cable Ethernet y accediendo a la interfaz de conexión de Bitmain a través de un navegador web en la misma red local. Puedes encontrar esta dirección IP conectándote a la interfaz de tu enrutador de internet y buscando los dispositivos conectados. Esta dirección debería tener el siguiente formato: 192.168.x.x

![image](assets/guide-achat/8.gif)

También verifica que las credenciales predeterminadas funcionen (nombre de usuario: root, contraseña: root). Si las credenciales predeterminadas no funcionan, deberás realizar un reinicio de la máquina.

![image](assets/guide-achat/9.jpeg)

Una vez conectado, deberías poder ver el estado de cada hashboard en el panel de control. Si el minero está conectado a un grupo de minería, deberías ver que todas las hashboards funcionan. Es importante tener en cuenta que los mineros hacen mucho ruido, esto es normal. Asegúrate también de que los ventiladores funcionen correctamente.

Luego puedes eliminar el grupo de minería del antiguo propietario para configurar el tuyo propio más adelante. Si lo deseas, también puedes inspeccionar las hashboards desmontando la máquina. Sin embargo, este paso es más complejo y requiere más tiempo y algunas herramientas. Si deseas realizar este desmontaje, puedes consultar la siguiente parte de este tutorial que detalla cómo hacerlo. Es importante tener en cuenta que los mineros acumulan mucho polvo y requieren un mantenimiento regular. Esta acumulación de polvo y la calidad del mantenimiento se pueden observar al desmontar la máquina.
Después de revisar todos estos puntos, puedes comprar tu máquina con un alto grado de confianza. En caso de duda, acude a la comunidad y si necesitas material para realizar este tutorial, no dudes en enviarnos un mensaje.

Para sintetizar esta guía en una frase: **"No confíes, verifica"**.

## Capítulo 2: Guía de compra de piezas para modificaciones

![image](assets/piece/1.jpeg)

### ¿Cómo convertir tu Antminer S9 en una calefacción silenciosa y conectada?

Si eres propietario de un Antminer S9, probablemente sepas lo ruidoso y voluminoso que puede ser este equipo. Sin embargo, es posible convertirlo en una calefacción silenciosa y conectada siguiendo algunos pasos simples. En este artículo te presentaremos los equipos necesarios para realizar las modificaciones, mientras que un artículo posterior explicará en detalle los pasos a seguir para realizar estos cambios.

### 1. Reemplazar los ventiladores

Los ventiladores originales del Antminer S9 son demasiado ruidosos para utilizar tu Antminer como calefacción. La solución es reemplazarlos por ventiladores más silenciosos. Nuestro equipo ha probado varios modelos de la marca Noctua y ha seleccionado el Noctua NF-A14 iPPC-2000 PWM como la mejor opción, asegúrate de elegir la versión de 12V de los ventiladores. Este ventilador de 140mm puede generar hasta 1300W de calefacción manteniendo un nivel teórico de ruido de 31 dB. Para poder montar estos ventiladores de 140mm, deberás utilizar un adaptador de 140mm a 120mm que podrás encontrar en la tienda de DécouvreBitcoin. También agregaremos rejillas de protección de 140mm.

![image](assets/piece/1.jpeg)
![image](assets/piece/2.jpeg)
![image](assets/piece/3.jpeg)

El ventilador de la fuente de alimentación también es bastante ruidoso y debe ser reemplazado. Recomendamos el Noctua NF-A6x25 PWM. Ten en cuenta que los conectores de los ventiladores Noctua no son los mismos que los originales, por lo que necesitarás un adaptador para conectarlos, con 2 será suficiente. También ten cuidado de elegir la versión de 12V del ventilador.

![image](assets/piece/4.jpeg)
![image](assets/piece/5.jpeg)

### 2. Agregar un puente WIFI/Ethernet

En lugar de utilizar un cable Ethernet, puedes conectar tu Antminer a través de WIFI agregando un puente WIFI/Ethernet. Hemos seleccionado el vonets vap11g-300 porque permite recuperar fácilmente la señal WIFI de tu caja de Internet y transmitirla a tu Antminer a través de Ethernet sin crear una subred. Si tienes habilidades eléctricas, puedes alimentarlo directamente con la fuente de alimentación del Antminer sin necesidad de agregar un cargador USB, para ello necesitarás un conector hembra de 5,5mmx2,1mm.

![image](assets/piece/6.jpeg)
![image](assets/piece/7.jpeg)

### 3. Opcional: agregar un enchufe conectado

Si desea encender/apagar su Antminer desde su teléfono inteligente y monitorear su consumo de energía, puede agregar un enchufe inteligente. Hemos probado el enchufe ANTELA en su versión de 16A compatible con la aplicación smartlife. Este enchufe inteligente permite consultar el consumo diario y mensual y se conecta directamente a su caja de Internet a través de WIFI.

![image](assets/piece/8.jpeg)

> Lista de materiales y enlaces
>
> - 2X adaptador de pieza 3D de 140 mm a 120 mm
> - 2X NF-A14 iPPC-2000 PWM [enlace](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)
> - 2X rejillas de ventiladores de 140 mm [enlace](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
> - Noctua NF-A6x25 PWM [enlace](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)
> - Cable eléctrico de 2,5 mm2 [enlace](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
> - Vonets vap11g-300 https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1> - Optionnel prise connectée ANTELA https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1

## Capítulo 3 - TUTORIAL: ¿Cómo convertir un minero en una calefacción?

![imagen](assets/hardware/0.jpeg)

Si eres un manitas y estás buscando convertir un minero en una calefacción, este tutorial es para ti. Queremos advertirte que hacer modificaciones a un dispositivo electrónico puede presentar riesgos eléctricos e incendios. Por lo tanto, es esencial tomar todas las precauciones necesarias para evitar cualquier daño o lesión.
De fábrica, un minero no es realmente utilizable como radiador en una vivienda, ya que es demasiado ruidoso y no es ajustable. Sin embargo, es posible realizar modificaciones simples para solucionar estos problemas.

> ATENCIÓN: Es esencial haber instalado previamente Braiins OS+ en tu minero, u otro software que tenga la capacidad de reducir el rendimiento de tu máquina. Esta medida es crucial, ya que para reducir el ruido, vamos a instalar ventiladores menos potentes, que podrán disipar menos calor.

### Materiales necesarios

- 2 adaptadores 3D de 140mm a 120mm
- 2 ventiladores Noctua NF-A14 iPPC-2000 PWM
- 2 rejillas de ventilador de 140mm
- 1 ventilador Noctua NF-A6x25 PWM
- Cable eléctrico de 2,5mm2
- Vonets VAP11G-300
- Opcional: enchufe conectado ANTELA

### Reemplazo de los ventiladores

Comenzaremos reemplazando el ventilador de la fuente de alimentación.

> ATENCIÓN: Primero, antes de comenzar, asegúrate de haber desconectado tu minero para evitar cualquier riesgo de electrocución.

![imagen](assets/hardware/1.jpeg)

Comenzaremos reemplazando el ventilador de la fuente de alimentación.

Primero, retira los 6 tornillos en el lateral de la carcasa que la mantienen cerrada. Una vez retirados los tornillos, abre cuidadosamente la carcasa para quitar la protección de plástico que cubre los componentes.

![imagen](assets/hardware/2.jpeg)
![imagen](assets/hardware/3.jpeg)'

A continuación, es hora de retirar el ventilador original teniendo cuidado de no dañar los otros componentes. Para hacer esto, retire los tornillos que lo mantienen en su lugar y despegue suavemente el pegamento blanco que rodea el conector. Es importante proceder con delicadeza para evitar dañar los cables o los conectores.

![image](assets/hardware/4.jpeg)

Una vez retirado el ventilador original, notará que los conectores del nuevo ventilador Noctua no coinciden con los del ventilador original. De hecho, el nuevo ventilador tiene 3 cables, incluido un cable amarillo que permite controlar la velocidad. Sin embargo, este cable no se utilizará en este caso específico. Para conectar el nuevo ventilador, se recomienda utilizar un adaptador especial. Sin embargo, es importante tener en cuenta que este adaptador a veces puede ser difícil de encontrar.

![image](assets/hardware/5.jpeg)

Si no tiene este adaptador, aún puede conectar el nuevo ventilador utilizando un empalme de cables eléctricos. Para ello, deberá cortar los cables del ventilador antiguo y del nuevo ventilador.

![image](assets/hardware/6.jpeg)
![image](assets/hardware/7.jpeg)

En el nuevo ventilador, use un cortador y corte cuidadosamente los contornos de la cubierta principal a 1 cm sin cortar las cubiertas de los cables debajo.

![image](assets/hardware/8.jpeg)

Luego, tirando hacia abajo de la cubierta principal, corte las cubiertas de los cables rojo y negro de la misma manera que antes. Y corte el cable amarillo al ras.

![image](assets/hardware/9.jpeg)

En el ventilador antiguo, es más delicado cortar la cubierta principal sin dañar las cubiertas de los cables rojo y negro. Para ello, hemos utilizado una aguja que hemos deslizado entre la cubierta principal y los cables rojo y negro.

![image](assets/hardware/10.jpeg)
![image](assets/hardware/11.jpeg)

Una vez que los cables rojo y negro estén libres, corte las cubiertas siempre con cuidado para no dañar los cables eléctricos.

![image](assets/hardware/12.jpeg)

Luego, conecte los cables con un empalme, el cable negro con el negro y el cable rojo con el rojo. También puede agregar cinta aislante.

![image](assets/hardware/13.jpeg)
![image](assets/hardware/14.jpeg)

Una vez realizada la conexión, es hora de colocar el nuevo ventilador Noctua con la rejilla y los tornillos antiguos, los nuevos tornillos que se encuentran en la caja se reutilizarán más tarde. Asegúrese de colocarlo con la orientación correcta. Notará una flecha en uno de los lados del ventilador, que indica la dirección del flujo de aire. Es importante colocar el ventilador de manera que esta flecha apunte hacia el interior del estuche. Luego, vuelva a conectar el ventilador.

![image](assets/hardware/15.jpeg)
![image](assets/hardware/16.jpeg)

> Opcional: Si tienes conocimientos en electricidad, puedes agregar directamente un conector hembra de 5,5 mm en la salida de alimentación de 12V, lo cual permitirá alimentar directamente el puente Wi-Fi Vonet. Sin embargo, si no estás seguro de tus habilidades en electricidad, es mejor utilizar el conector USB con un cargador de tipo smartphone para evitar cualquier riesgo de cortocircuito o daño eléctrico.

![image](assets/hardware/17.jpeg)

Una vez realizadas las conexiones, asegúrate de colocar correctamente la cubierta de plástico sobre la carcasa y no dentro de ella.

![image](assets/hardware/18.jpeg)

Finalmente, vuelve a colocar la cubierta de la carcasa en su lugar y vuelve a atornillar los 6 tornillos en los lados para mantener todo en su lugar. ¡Y listo, tu carcasa de alimentación ahora está equipada con un nuevo ventilador!

### Reemplazo de los 2 ventiladores principales

1. En primer lugar, desconecta los ventiladores y desenróscalos.
   ![image](assets/hardware/19.jpeg)

2. Los conectores de los nuevos ventiladores Noctua no coinciden con los originales, ¡pero no te preocupes! Saca tu cutter y corta cuidadosamente las pequeñas lengüetas de plástico para que los conectores se adapten perfectamente a tu minero.

![image](assets/hardware/20.jpeg)
![image](assets/hardware/21.jpeg)

3. ¡Es hora de instalar las piezas 3D!
   Fíjalas en ambos lados del minero utilizando los tornillos que retiraste de los ventiladores. Atornilla hasta que la cabeza del tornillo se hunda en la pieza 3D y esta quede bien sujeta. Ten cuidado de no apretar demasiado, ¡podrías deformar la pieza y uno de los tornillos podría tocar un condensador! Luego corta cuidadosamente las pequeñas lengüetas de plástico para que los conectores se adapten perfectamente a tu minero.

![image](assets/hardware/22.jpeg)

4. Ahora pasemos a los ventiladores.
   Fíjalos en las piezas 3D utilizando los tornillos suministrados en la caja. Presta atención a la dirección del flujo de aire, las flechas en los lados de los ventiladores te indicarán la dirección a seguir. Ve desde el lado del puerto Ethernet hacia el otro lado. Ver foto a continuación.

![image](assets/hardware/23.jpeg)
![image](assets/hardware/24.jpeg)
![image](assets/hardware/25.jpeg)

5. Último paso: conecta los ventiladores y fija las rejillas encima con los tornillos que no se utilizaron en la caja del ventilador de la alimentación. Solo tienes 4, pero 2 por rejilla en ángulos opuestos serán suficientes. Si es necesario, también puedes buscar otros tornillos similares en una tienda de bricolaje.

![image](assets/hardware/26.jpeg)'
'![image](assets/hardware/27.jpeg)
Mientras esperas poder ofrecer una carcasa más atractiva para tu nueva calefacción, puedes sujetar la caja y la fuente de alimentación juntas con abrazaderas de electricista.

![image](assets/hardware/28.jpeg)

Y para el toque final, conecta el puente Vonet al puerto Ethernet a su fuente de alimentación. Si aún no lo has hecho, puedes seguir este tutorial para configurar tu puente.

![image](assets/hardware/29.jpeg)

¡Y listo, felicidades! Acabas de reemplazar toda la parte mecánica de tu minero. Ahora deberías escuchar mucho menos ruido.

## Capítulo 4 - Modificación del software - Restablecer un Antminer S9

**Serie de artículos propuesta por BlobOnChain & Ajelex - 15/02/2023**

### Restablecer mediante el botón "Reset"

Este método se puede aplicar dentro de los 10 minutos posteriores al inicio del minero.

Después de encender el minero durante 2 minutos, presiona el botón "Reset" durante 5 segundos y luego suéltalo. El minero se restaurará a los ajustes de fábrica en 4 minutos y se reiniciará automáticamente (no es necesario apagarlo).

![image](assets/software/1.jpeg)

Restaurar mediante el lado web

Inicia sesión en la interfaz de usuario de tu minero, haz clic en "Upgrade" >> "Realizar un restablecimiento" y luego haz clic en "OK" en la ventana emergente.

### Sistema operativo original

Para esta parte, supondremos que la máquina está funcionando, está encendida y tiene instalado su sistema operativo original. Veremos brevemente la interfaz del sistema operativo original ofrecida por Bitmain.

Primero, conéctate a tu máquina a través de tu red local:

![image](assets/software/2.gif)

Una vez en la página de inicio de sesión, deberás iniciar sesión en el ASIC utilizando las credenciales predeterminadas:

- nombre de usuario: root
- contraseña: root

(¿Cómo restablecer si la contraseña predeterminada no funciona?)

El sistema operativo principal es relativamente básico. Con las 4 pestañas: System, Miner Configuration, Miner Status, Network. En la pestaña Miner Configuration, puedes configurar hasta 3 grupos de minería.

![image](assets/software/3.jpeg)

En la pestaña Miner Status, podrás observar diferentes información sobre el funcionamiento del ASIC en tiempo real. La tasa de hash expresada en GH/s, información más detallada sobre el grupo de minería, así como detalles sobre el estado de cada placa hash y la velocidad de los ventiladores en revoluciones por minuto.

![image](assets/software/4.jpeg)

### Braiins OS+'

Ahora vamos a estudiar el software para ASICs Braiins OS+ (https://braiins.com/os/plus). El software es desarrollado por la empresa Braiins (https://braiins.com/), que es la empresa matriz del pool de minería Braiins Pool (https://braiins.com/pool). Este pool de minería tiene actualmente el 4.39% del hashrate global (https://mempool.space/fr/mining/pool/slushpool). La empresa con sede en Praga solía llamarse Slushpool y fue el primer pool de minería que comenzó en noviembre de 2010. Hoy en día, la empresa ofrece diversas herramientas de rentabilidad para la minería (https://insights.braiins.com/en), soluciones de gestión de granjas de minería junto con su actividad de pool y su software de optimización para ASICs. También ofrece la posibilidad de minar utilizando el nuevo protocolo Stratum V2 (https://braiins.com/bitcoin-mining-stack-upgrade).

Por lo tanto, vamos a estudiar más detalladamente el funcionamiento de los dispositivos de la marca Bitmain, que son actualmente los únicos modelos compatibles:

- S19, S19 Pro, S19j, S19j Pro, T19,
- 17, S17 Pro, S17+, S17e, T17, T17+, T17e & S9 [i, j]

El software Braiins OS se puede instalar fácilmente en todas las máquinas mencionadas anteriormente. Permite un control más preciso de una máquina, permitiendo overclocking o underclocking. También permite un ajuste fino de la frecuencia de cada chip gracias a una función de optimización automática llamada autotuning. Como cada chip de hash es ligeramente diferente debido a su proceso de fabricación, el software prueba la frecuencia óptima para cada uno de ellos para obtener una eficiencia (W/THs) máxima. El software anuncia un rendimiento que puede ser un 25% superior al original. Según nuestras mediciones, es posible alcanzar estas cifras.

## Instalación de Braiins OS+

Existen varias formas de instalar Braiins OS+ en un ASIC. Puede consultar esta guía, así como la documentación oficial de Braiins y los tutoriales en video.

Instalación de Braiins OS+ directamente en la memoria del Antminer

Descubra cómo instalar fácilmente Braiins OS+ directamente en la memoria de su Antminer con BOS toolbox, reemplazando así el sistema operativo original, a través de los siguientes pasos detallados. Si desea conservar el sistema operativo original en paralelo, puede instalar Braiins OS+ en una tarjeta SD.

1. Encienda su Antminer y conéctelo a su caja de internet.
2. Descargue BOS toolbox para Windows / Linux.
3. Descomprima el archivo descargado y abra el archivo bos-toolbox.bat, elija el idioma y luego después de un momento verá esta ventana:
   ![image](assets/software/5.jpeg)

4. Bos toolbox le permitirá encontrar fácilmente la dirección IP de su Antminer e instalar Braiins OS+. Si ya conoce la dirección IP de su máquina, puede pasar al paso 8. De lo contrario, vaya a la pestaña de escaneo.

![image](assets/software/6.jpeg)

5. Por lo general, en las redes domésticas, el rango de direcciones IP se encuentra entre 192.168.1.1 y 192.168.1.255, así que ingrese "192.168.1.0/24" en el campo de rango de IP. Si su red es diferente, cambie estas direcciones. Luego haga clic en "Start".

6. Atención, si el Antminer tiene una contraseña, la detección no funcionará. Si ese es el caso, lo más sencillo es realizar un restablecimiento de fábrica.

7. Debería ver todos los Antminer en su red, aquí la dirección IP es 192.168.1.37

![image](assets/software/7.jpeg)

8. Haga clic en "Back" y luego en la pestaña de instalación, ingrese la dirección IP encontrada anteriormente en el campo de "Miner(s)" y "admin" (o "root") en el campo de contraseña, que es la contraseña predeterminada, luego haga clic en "Start".
   Si la instalación no funciona, ni con "admin" ni con "root" como contraseña, puede ser necesario realizar un restablecimiento de fábrica y volver a intentarlo.

![image](assets/software/8.jpeg)

9. Después de un momento, su Antminer se reiniciará y podrá acceder a la interfaz de Braiins OS+ en la dirección IP mencionada, aquí 192.168.1.37, que debe ingresar directamente en la barra de direcciones de su navegador, el nombre de usuario predeterminado es "root" y no hay contraseña predeterminada.
   Instalación de Braiins OS+ en una tarjeta SD

![image](assets/software/9.jpeg)

![image](assets/software/10.jpeg)

El segundo método utiliza la interfaz original de su Antminer. Este método funciona para máquinas con un sistema operativo anterior a 2019.

### Interfaz Antminer

1. Descargue el nuevo sistema operativo a instalar aquí.
2. Como en la sección anterior, conéctese a su máquina a través de su red local.
3. Vaya a la pestaña de Sistema y luego a Actualización.
4. Cargue el archivo que ha descargado y flashee la imagen.

![image](assets/software/11.jpeg)

### Tarjeta micro SD

Un segundo método le permite utilizar una tarjeta micro SD. Este método solo funciona con máquinas con un sistema operativo posterior a 2019.

1. Descargue el nuevo sistema operativo a instalar aquí.

2. Flashee la imagen descargada en una tarjeta micro SD. Para ello, puede utilizar Etcher. Simplemente copiar el archivo en la tarjeta micro SD no funcionará.
3. Si tienes un Antminer S9 y sus variantes (S9i, S9j), deberás ajustar los "jumpers" para forzar que tu ASIC arranque desde el archivo contenido en la tarjeta micro SD en lugar de la NAND. Si tienes otro modelo, puedes pasar a la parte 4. Los jumpers se encuentran en la tarjeta de control en la parte superior del ASIC, cerca del puerto Ethernet. Deberás retirarla deslizándola hacia atrás. Una vez que hayas modificado la posición del jumper como se muestra en las imágenes a continuación "BOOT FROM SD", puedes volver a insertar la tarjeta de control y volver a conectar el S9.

![image](assets/software/12.jpeg)

![image](assets/software/13.jpeg)

4. Inserta la tarjeta micro SD en el ASIC.
5. Inicia el ASIC. Si se utilizó la versión de instalación automática, el nuevo sistema operativo se instalará automáticamente. La instalación se completa cuando ambos LEDs se encienden al mismo tiempo. Puedes reiniciar el ASIC y retirar la tarjeta micro SD. Si se descargó la otra versión, deberás dejar la tarjeta micro SD dentro del ASIC.

Para obtener más información sobre la instalación, puedes visitar esta sección del sitio web de Braiins.

## La interfaz

Deberás conectarte a tu ASIC de manera similar. Utilizando la dirección IP local de tu dispositivo en tu red a través de un navegador.

Las credenciales predeterminadas son las mismas que las del sistema operativo original.

- nombre de usuario: root
- contraseña: root

Entonces serás recibido por el panel de control de Brains OS+.

### Panel de control

![image](assets/software/14.jpeg)

En esta primera página podrás observar el rendimiento de tu máquina en tiempo real.

- Tres gráficos en tiempo real que muestran la temperatura, el hashrate y el estado general de tu máquina.
- A la derecha, el hashrate real, la temperatura promedio de los chips, tu eficiencia estimada en W/THs y el consumo de energía.
- Debajo, la velocidad de rotación de los ventiladores en porcentaje de la velocidad máxima y el número de rotaciones por minuto.

![image](assets/software/15.jpeg)

- Más abajo encontrarás una vista detallada de cada hashboard. La temperatura promedio de la placa y los chips que la componen, el voltaje y la frecuencia.
- Detalles sobre los pools de minería activos en Pools.
- El estado del autotuning en Tuner Status.
- A la derecha, detalles sobre las partes transmitidas al pool.

### Configuración

![image](assets/software/16.jpeg)

### Sistema

![image](assets/software/17.jpeg)

### Acciones rápidas

![image](assets/software/18.jpeg)

Configuración de un pool.

Se puede imaginar una pool de minado como una cooperativa agrícola. Los agricultores unen sus producciones para reducir la variabilidad de la oferta y la demanda y así obtener ingresos más estables para su explotación. Una pool de minado funciona de la misma manera y la materia prima que se comparte son los hash. De hecho, el descubrimiento de un solo hash válido permite la creación de un bloque y así ganar la coinbase o la recompensa actual de 6,25 BTC más las tarifas de las transacciones incluidas en el bloque. Si minas solo, solo serás recompensado cuando encuentres un bloque. Al competir contra todos los demás mineros del planeta, tendrías muy pocas posibilidades de ganar esta gran lotería y aún así tendrías que pagar las tarifas asociadas al uso de tu minero sin ninguna garantía de éxito. Las pools de minado responden a este problema al compartir la potencia de cálculo de varios (miles) de mineros y compartir la recompensa de estos en función del porcentaje de participación en el hashrate de la pool cuando se encuentra un bloque. Para visualizar tus posibilidades de minar un bloque solo, puedes utilizar esta herramienta. Al ingresar la información de un Antminer S9, se puede ver que las posibilidades de encontrar un hash que permita la creación de un bloque son de 1/24 777 849 por cada bloque o de 1/172 068 por día. En promedio (con un hashrate y una dificultad constantes), se necesitarían 471 años para encontrar un bloque.

Sin embargo, como en Bitcoin todo es probabilidad, a veces los "solo miners" son recompensados por asumir este riesgo: Solo Bitcoin Miner Solves Block With Hash Rate of Just 10 TH/s, Beating Extremely Unlikely Odds – Decrypt

Si te gusta jugar, puedes intentarlo, pero nuestra guía no se orientará en esta dirección. En cambio, nos centraremos en la pool de minado que mejor se adapte a nuestras necesidades para crear un sistema de calefacción.

Las consideraciones a tener en cuenta al elegir un grupo de minería son el funcionamiento de las recompensas del grupo, que pueden ser diferentes, así como el monto mínimo antes de poder retirar las recompensas a una dirección. Por ejemplo, Braiins, que ofrece el software del que estamos hablando aquí, también ofrece un grupo de minería. Este grupo tiene un sistema de recompensa llamado "Score" que incentiva a los mineros a minar durante largos períodos. La participación incluye un factor de tiempo de actividad que se expresa con una "tasa de hash de puntuación". En nuestro caso, donde queremos un sistema de calefacción que se pueda encender solo durante unos minutos, este no es el sistema de recompensa ideal. Preferimos un sistema de recompensa que nos dé una recompensa igual por cada participación. Además, el monto mínimo de retiro para Braiins Pool es de 100,000 sats y On-Chain. Por lo tanto, perdemos algunos sats en tarifas de transacción y parte de nuestra recompensa puede quedar bloqueada si no minamos lo suficiente durante el invierno.

El modelo de recompensa que nos interesa es el PPS, que significa "pago por acción". Esto significa que el minero recibirá una recompensa por cada acción válida. También existe una variante de este sistema, el FPPS (Pago Completo por Acción), que divide no solo la recompensa de la coinbase, sino también las tarifas de transacción incluidas en el bloque. Los grupos de minería que recomendamos para conectar su minería/calefacción son Linecoin Pool (FPPS) y Nicehash (PPS).

- Nicehash: La ventaja de Nicehash es que el retiro se puede hacer utilizando Lightning con tarifas mínimas. Además, el monto mínimo de retiro es de 2000 sats. La desventaja es que Nicehash utiliza su tasa de hash para la cadena de bloques más rentable, sin dar realmente el control al usuario y, por lo tanto, no siempre participa en la tasa de hash de Bitcoin.

- Lincoin: La ventaja de Linecoin es la cantidad de características que ofrece, como un panel de control detallado, la posibilidad de hacer retiros con un Paynym (BIP 47) para una mejor protección de la privacidad, y la integración de un bot de Telegram y automatizaciones directamente configurables en la aplicación móvil. Este grupo solo mina bloques de Bitcoin, pero el monto mínimo para retirar sigue siendo alto, 100,000 sats. Analizaremos más detalladamente la interfaz de uno de estos grupos en un próximo artículo.

Para configurar un grupo en Braiins 0S+, deberá crear una cuenta en uno de los grupos de su elección. Aquí vamos a tomar el ejemplo de Lincoin:

![image](assets/software/19.jpeg)

Una vez que haya creado su cuenta, haga clic en "Connect To Pool".

Luego copie la dirección Stratum y su nombre de usuario:

![image](assets/software/20.jpeg)

Ahora puede volver a la interfaz de Braiins OS+ para ingresar estas credenciales. Para la contraseña, puede dejar el campo vacío.

![image](assets/software/21.jpeg)

### Overclocking y Underclocking

El overclocking y el autotuning consisten en ajustar las frecuencias en las tarjetas de hash para mejorar el rendimiento del ASIC. La diferencia entre ambos radica en la complejidad de estos ajustes de frecuencia.

El **overclocking** es un ajuste sencillo que consiste en aumentar la frecuencia en las tarjetas de hash para aumentar la tasa de hash de la máquina. El underclocking, por otro lado, consiste en disminuir la frecuencia de reloj de un circuito integrado por debajo de su frecuencia nominal. Al reducir la frecuencia de reloj de un ASIC mediante el underclocking, también se reduce el calor generado por el hardware. Esto permite disminuir la velocidad de los ventiladores necesarios para enfriar el ASIC, ya que no tienen que trabajar tan duro para mantener una temperatura adecuada. Al reducir la velocidad de los ventiladores, también se reduce el ruido generado por el ASIC. Esto puede ser especialmente útil para los usuarios que utilizan ASIC en casa y buscan minimizar las molestias sonoras causadas por el hardware de minería.

Es importante tener en cuenta que el underclocking puede llevar a una reducción en el rendimiento del ASIC, por lo que es importante encontrar un buen equilibrio entre el rendimiento y el ruido.

Braiins OS+ admite el overclocking, el underclocking de los ASIC y el autotuning. Permite a los usuarios ajustar la frecuencia de reloj de su hardware de manera flexible para maximizar el rendimiento o ahorrar energía según sus preferencias.

### Autotuning

Antes de 2018, los mineros tenían dos formas de obtener una ventaja en su actividad: encontrar electricidad a un costo razonable y comprar hardware más eficiente. Sin embargo, en 2018 se descubrió un nuevo avance en el campo del software y firmware minero, llamado AsicBoost. Esta técnica permite a los mineros reducir sus costos en aproximadamente un 13% al modificar el firmware que se ejecuta en sus dispositivos.
Hoy en día, hay un nuevo avance en el sector de software y firmware minero llamado autorregulación (o autotuning) que ofrece una ventaja aún más importante que AsicBoost. Los ASIC están compuestos por numerosos chips informáticos pequeños que realizan el hashing. Estos chips están hechos de silicio, el mismo elemento ampliamente utilizado en semiconductores y otros componentes microelectrónicos. La comprensión clave aquí es que no todos los chips de silicio son idénticos, cada uno puede variar ligeramente en sus propiedades eléctricas. Los fabricantes de hardware lo saben y publican las especificaciones de rendimiento de sus máquinas mineras en función del límite inferior de sus tolerancias. En otras palabras, los fabricantes conocen la frecuencia que funciona mejor para los chips promedio y la utilizan de manera uniforme para todos los chips de la máquina.

Esto pone un límite superior a la tasa de hashing que una máquina puede tener. La autorregulación es un proceso en el cual los algoritmos evalúan las frecuencias óptimas para el hashing chip por chip, en lugar de tratar toda la máquina como una sola unidad. Esto significa que un chip de mejor calidad que puede realizar más hash por segundo obtendrá una frecuencia más alta, y un chip de menor calidad que puede realizar relativamente menos obtendrá una frecuencia más baja. La autorregulación por chip es esencialmente una forma de optimizar el rendimiento de un ASIC a través del software y firmware que se ejecutan en él.

El resultado final es una tasa de hashing más alta por vatio de electricidad, lo que significa márgenes de beneficio más grandes para los mineros. La razón por la cual las máquinas no se distribuyen con este tipo de software es que la variabilidad por máquina no es deseable, ya que los clientes quieren saber exactamente lo que están obteniendo y, por lo tanto, es una mala idea para los fabricantes vender un producto que no tiene un rendimiento constante y predecible de una máquina a otra. Además, la autorregulación por chip requiere considerables recursos de desarrollo, ya que es compleja de implementar. Los fabricantes ya gastan muchos recursos en desarrollar sus propios firmwares. Existen soluciones de software que permiten implementar el autotuning, como Braiins OS+. Además de mejorar el rendimiento del ASIC hasta en un 20%.

> Guía creada por DecouvreBitcoin, más información sobre MINAGE 201 - crédito a Jim y Ajelex.
