---
name: Jade - Electrum
description: Cómo utilizar su Jade o Jade Plus con Electrum (escritorio)
---

![cover](assets/cover.webp)



esta guía está extraída de una lección de [Talleres Bitcoin](https://officinebitcoin.it/lezioni/jadeele/index.html)_



El tutorial está hecho con Jade Classic, pero las operaciones también son válidas para los que tienen Jade Plus.



Después de inicializar Jade, puedes empezar a usarlo y, para ello, elige una pantalla wallet.



Jade es un dispositivo que puede utilizarse con varias wallet, o aplicaciones complementarias, como Blockstream las especifica en su sitio web.



En este tutorial verás los pasos para utilizar Electrum Wallet, mediante conexión por cable USB.



## Transferencia de clave pública



Coge y enciende tu Jade inicializado. Tan pronto como se enciende se ve así:




![img](assets/en/32.webp)



Si seleccionas _Desbloquear Jade_, aparecerá el menú en el que tendrás que elegir cómo conectar tu dispositivo a la aplicación complementaria.



Con Electrum sólo puedes conectar Jade a través de USB, así que elige este método.



Inicie Electrum, que se abrirá proponiendo como opción por defecto abrir el último wallet utilizado.



Si es la primera vez que conecta Jade a Electrum, seleccione _Crear nueva cartera_ y luego _Finalizar_.



![img](assets/en/34.webp)



Nombre wallet.



![img](assets/en/35.webp)



Seleccione Wallet estándar.



![img](assets/en/36.webp)



Al elegir el almacén de claves, es esencial seleccionar _Usar un dispositivo de hardware_.



![img](assets/en/37.webp)



Electrum inicia la búsqueda del dispositivo de hardware.



![img](assets/en/38.webp)



Al conectar el USB al ordenador (ya conectado por el lado USB C a Jade), el hardware wallet aparece en modo de bloqueo. Jade se desbloquea introduciendo el PIN de seis dígitos establecido durante la configuración.




![img](assets/en/39.webp)



Dispositivo de hardware desbloqueado, Electrum detecta Jade. Continúa pulsando _Siguiente_.



![img](assets/en/40.webp)



En este punto Electrum le pide que establezca el script de la política: elija _Native Segwit_.



![img](assets/en/41.webp)



Comienza la fase de transferencia de clave pública de wallet de Jade a Electrum de pantalla.



Una vez finalizada la exportación de la clave pública, el proceso habrá terminado.



El watch-only está listo y Electrum avisa de su finalización con la siguiente pantalla.



![img](assets/en/42.webp)



wallet se ha creado realmente y puedes empezar a explorarlo: puedes ver las _direcciones_, la _información de la cartera_ y -lo más importante- puedes ver en la esquina inferior derecha la indicación de que se trata de un dispositivo de Blockstream. El punto verde junto al logotipo de Blockstream indica que el dispositivo está encendido y correctamente conectado a la red local.



![img](assets/en/43.webp)



## Recibir y gastar transacciones



Desde el menú _Recibir_ de Electrum, generate una `scriptPubKey` (dirección) para recibir fondos. Empieza siempre con una cantidad pequeña y haz una prueba de recibir+gastar.



![img](assets/en/44.webp)



Una vez recibidos los satss, puede comprobar su llegada en el menú _Historia_.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Una vez confirmada la transacción, puedes gastar este UTXO y terminar la prueba.



El gasto implica utilizar Jade para firmar.



Ve al menú _Enviar_ de Electrum, pega un scriptPubKey, y compruébalo bien.



![img](assets/en/47.webp)



Cuando haya terminado, pulse _Pagar_.



Se abre la ventana de transacción, en la que es importante establecer las tasas de transacción correctas. Cuando haya terminado todos los ajustes haga clic en _Preview_ en la esquina inferior derecha.



![img](assets/en/48.webp)



La ventana de transacción muestra algunos detalles importantes, en primer lugar el estado: `Sin firmar`.



En esta fase también puede ver el comando _Firmar_, que debe pulsar para estampar la firma con Jade.



![img](assets/en/49.webp)



Ahora comienza una fase de comunicación entre la pantalla wallet y el dispositivo hardware, en la que Electrum le avisa para que siga las instrucciones del dispositivo hardware, encendido y listo para firmar.



![img](assets/en/50.webp)



**Primero, sin embargo, será mejor que verifiques lo que estás firmando: todos los parámetros de la transacción que acabas de configurar, también aparecen en Jade** y puedes verificarlos todos.



![img](assets/en/51.webp)



Para continuar asegúrese de colocar siempre el cursor sobre la flecha `→` que lleva a los siguientes pasos y nunca sobre la `X` a menos que quiera terminar la operación sin completarla.



La parte de verificación termina con la visualización de la tasa. En este punto la confirmación equivale a poner la firma.



![img](assets/en/52.webp)



Durante un breve instante Jade procesa la operación, cuando termina vuelve al menú de inicio.



![img](assets/en/53.webp)



Mientras que en Electrum puede ver el estado de la transacción, que ha cambiado de `Unsigned` a `Signed` y ahora es posible, para usted, propagarla pulsando _Broadcast_.



![img](assets/en/54.webp)



El wallet, así probado, puede utilizarse para recibir el UTXO destinado a un almacenamiento seguro.



![img](assets/en/55.webp)



Esta guía es un ejemplo de cómo utilizar su Jade, conectado vía USB, a un wallet watch-only. Electrum es un ejemplo clásico, pero usted puede preferir otro software wallet. Jade exporta la clave pública a muchos otros monederos: encuentra las funciones similares que has leído en este tutorial, para guiarte y encontrar cómo emplearlo tu aplicación companio favorita.