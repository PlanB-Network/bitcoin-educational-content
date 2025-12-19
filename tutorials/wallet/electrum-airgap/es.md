---
name: Electrum Airgap
description: Un primer paso hacia la seguridad, un cold wallet con Electrum
---
![cover](assets/cover.webp)



## Cold Wallet



En este tutorial voy a explicar cómo hacer su primer dispositivo de firma airgap, desconectado de Internet, incluso sin tener un Hardware Wallet dedicado. Todo lo que necesitas es tener dos ordenadores disponibles:




- que un dispositivo antiguo no pueda conectarse a Internet para siempre;
- su ordenador de uso diario.



Esta configuración permite un mayor grado de seguridad que la clásica `Hot Wallet`: el ordenador antiguo -sin conexión a la red- es el guardián de sus claves privadas, que nunca se exponen en Internet, sino que se almacenan fuera de línea ("airgap" o "Cold").



En su lugar, instalará una pantalla Wallet ("sólo reloj") en su ordenador de uso diario, que estará conectada a la red y con la que podrá, por ejemplo, consultar saldos y preparar transacciones de recibos.



## Entrehierro Wallet: Qué y cómo



Realizando los pasos de esta guía, instalaremos dos Software Wallet Electrum en los dos ordenadores diferentes y finalmente crearemos dos Billeteras con diferentes almacenes de claves: la Wallet airgap utilizará toda la jerarquía de la Wallet HD, mientras que la Wallet display se generará con la clave pública maestra.



Estas dos Carteras serán, en todos los aspectos, muy diferentes entre sí. Lo único que tendrán en común, como veremos, son las direcciones:




- gW-13 en el ordenador airgap sólo puede firmar pero, desconectado de la red, no conoce la balanza ni las direcciones utilizadas;
- el Wallet en el ordenador diario sólo podrá preparar y propagar transacciones, sin poder disponer del gasto, en ausencia de las claves privadas.



## Preparación preliminar



Para descargar Electrum, te recomiendo que sigas los primeros pasos de este tutorial:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Después de la descarga, verifique siempre la versión antes de instalarla y proceda a la configuración de "Un servidor", como encontrará en la sección de ayuda, en "Empezar con un Wallet ficticio".



La operación de configuración "Un servidor" sólo es necesaria para la Wallet instalada en el ordenador diario, ya que el otro ordenador siempre estará desconectado.



Las siguientes operaciones implican la práctica en dos ordenadores diferentes (y Carteras), así que-por conveniencia y enfoque-elegí para establecer la Wallet airgap con el tema de la luz, mientras que la Wallet pantalla tiene el tema oscuro.



## Wallet Creación de entrehierros



Después de descargar y verificar la descarga de Electrum, haga una copia del ejecutable y llévelo a su ordenador sin conexión. A continuación, ejecútelo e instale Electrum.



Haga doble clic para iniciar Electrum: el ordenador donde utilizará este Wallet está desconectado, ignore la configuración de red y vaya a la creación del Wallet que, en esta guía, llamaremos `airgap`.



![image](assets/en/01.webp)



Elija _Monedero estándar_.



![image](assets/en/02.webp)



Y luego seleccione _Crear una nueva semilla_ para que el software generate la Mnemonic.



![image](assets/en/03.webp)



Transcriba con precisión las 12 palabras generate de Electrum en un soporte de papel y proceda al paso de verificación, volviendo a introducir las palabras en orden cuando Electrum lo solicite.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Una vez finalizada la creación de la Wallet, establezca una contraseña compleja (`Fuerte`) para encriptar el archivo Wallet en el dispositivo airgap. Este paso es muy delicado e importante, ya que la contraseña elegida ahora, impide el acceso a la Wallet que tiene poder dispositivo, pudiendo gastar fondos firmar transacciones.



![image](assets/en/06.webp)



Al hacer clic en _Finalizar_ la Wallet queda definida y aparece en la pantalla. Por supuesto, el indicador de conexión a la red, es decir, el punto de color en la esquina inferior derecha, es de color rojo, ya que el ordenador está desconectado y no permite Wallet para exponer las teclas en línea.



![image](assets/en/07.webp)



## Creación Wallet de visualización



Ahora que su Wallet dispone de claves privadas offline, debe configurar un Wallet de visualización, o `watch-only`, que le permitirá ver el saldo, así como preparar transacciones de recibos para seguir acumulando Sats de forma segura.



Desde el Wallet situado en el dispositivo offline, elija el menú _Wallet_ -> _Information_



![image](assets/en/08.webp)



Aparecerá la ventana con toda la información de su Wallet, donde podrá marcar `derivation path` y `master fingerprint`, por ejemplo para marcarlos junto a las palabras de la sentencia Mnemonic (muy recomendable).



![image](assets/en/09.webp)



Recuerda que estás tomando estos datos de un ordenador desconectado, por lo que tendrás que copiar/pegar el `zpub` a un archivo de texto y guardarlo en una memoria usb.



Ahora puede pasar al ordenador conectado a Internet, para iniciar Electrum y crear un nuevo Wallet.



En el menú _Archivo_, seleccione _Nuevo/Restaurar_.



![image](assets/en/10.webp)



La nueva Wallet es sólo para ver, así que en esta guía la llamaremos `sólo para ver`.



![image](assets/en/12.webp)



En la siguiente pantalla elija _Monedero estándar_ y continúe pulsando _Siguiente_.



![image](assets/en/13.webp)



Al elegir el `Keystore` tenga cuidado: para crear la pantalla Wallet seleccione _Usar una llave maestra_. A continuación, proceda con _Siguiente_.



![image](assets/en/14.webp)



Pega aquí el `zpub` copiado de Wallet offline y que trajiste a este ordenador vía usb media.



![image](assets/en/15.webp)



Concluya estableciendo también una contraseña segura para esta Wallet, posiblemente diferente de la elegida para su correspondiente Cold.



Verá aparecer la Wallet de pantalla, con un mensaje de advertencia. El mensaje te recuerda que se trata de una Wallet de visualización y que no puedes, con ella, gastar los fondos asociados.



**Nota Bien**: **por lo tanto, necesitarás poseer siempre las claves privadas para disponer de los UTXOs de este Wallet**. Con un buen sistema de copias de seguridad, no le será difícil permanecer en plena posesión de sus Bitcoins.



![image](assets/en/16.webp)



Esta advertencia aparecerá cada vez que abras este Wallet. Haga clic en _Ok_ y pasemos al paso de verificación.



## Verificación de los dos Wallet



Como aprendimos al principio de esta guía, una Wallet airgap y su Wallet display son dos carteras que tienen facultades diferentes pero **comparten las mismas direcciones**.



Si miramos las dos Carteras una al lado de la otra, visualmente nos damos cuenta de que en la Wallet airgap hay un símbolo "seed", mientras que en la watch-only no lo hay. Incluso este detalle le ayudará a recordar que la Wallet de la pantalla Wallet no tiene claves privadas.



![image](assets/en/17.webp)



Sin embargo, para realizar una primera comprobación precisa, seleccione en ambas Carteras el menú `Direcciones`: puesto que comparten las mismas direcciones, la lista de direcciones debería ser idéntica para ambas.



![image](assets/en/18.webp)



⚠️ **ATENCIÓN**: **no puede haber término medio; las direcciones deben ser las mismas. En caso de que sean diferentes, es necesario borrar todo el trabajo realizado hasta el momento y empezar de nuevo**.



Ahora puede proceder a hacer dos comprobaciones diferentes. En primer lugar, intente borrar las dos Carteras y restaurarlas desde cero, cada una en el ordenador correspondiente. En caso de que proceda a realizar esta comprobación, los procedimientos para la visualización Wallet son idénticos a los expuestos anteriormente.



Sin embargo, para el entrehierro Wallet, en la pantalla `keystore` tendrás que elegir _Ya tengo una semilla_ e introducir las palabras copiándolas de tu copia de seguridad en papel.



Una vez finalizada la prueba "sin carga", puede intentar realizar una transacción de un importe pequeño y gastarlo inmediatamente.



## Recibir y gastar transacciones



Para empezar a utilizar su airgap Electrum, puede realizar una transacción de recibo con una pequeña cantidad, y luego gastarla en una Address propia. Así podrá familiarizarse con el procedimiento, comprobando que tiene pleno control de los fondos.



**Nota**: No le recomiendo que deposite una gran cantidad de fondos en Wallet antes de estar seguro de que puede realizar todas las operaciones sin problemas.



Los pasos que se explican a continuación pueden parecer complicados a primera vista. No se desanime: cuando los haya probado por primera vez, verá que sólo le llevará unos minutos completarlos.



Pour recevoir des fonds, vous devez nécessairement utiliser le visualisateur Wallet situé sur votre ordinateur connex à Internet. Desde el menú `Recibir` haga clic en _Crear solicitud_ para que Electrum generate la primera Address disponible y utilizarlo para enviarnos unos Satss.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



Una vez propagada la transacción ya se puede ver que -como es natural- sólo es visible en la pantalla Wallet y no en el entrehierro Wallet.



![image](assets/en/21.webp)



Después de que su transacción haya recibido alguna confirmación, puede preparar el gasto e intentar así el procedimiento de firma desde la Wallet fuera de la red. A continuación, prepare la transacción en el reloj y pulse _Preview_ para comprobarla



![image](assets/en/22.webp)



Obtendrá la ventana de transacción avanzada donde podrá verlo:




- la transacción no está firmada (`Status: Unsigned);
- los comandos `Sign` y `Broadcast` están inhibidos.



Lo único que puede hacer es exportar la transacción tal cual, llevarla al airgap Wallet y firmarla.



Introduce una memoria USB en tu ordenador y, en el menú de la parte inferior izquierda, elige _Compartir_.



![image](assets/en/23.webp)



A continuación, seleccione _Guardar en archivo_.



![image](assets/en/24.webp)



Guarda la transacción en la memoria USB.



Observará que Electrum da al archivo un nombre que lleva los primeros dígitos de transaction ID, y la extensión del archivo es `.PSBT`, lo que significa `Partially Signed Bitcoin Transaction`.



Extrae el soporte con el archivo `.PSBT` y conéctalo al ordenador sin conexión.



Desde el entrehierro Wallet, elija ahora el menú _Herramientas_, luego _Cargar transacción_ y a continuación Desde fichero_.



![image](assets/en/25.webp)



Con el gestor de archivos, seleccione `.PSBT` de su ubicación.



![image](assets/en/29.webp)



El software del ordenador fuera de la red abrirá automáticamente la ventana de transacción avanzada, completamente idéntica a como la vio en la pantalla del Wallet. El estado es `Sin firmar`, pero la diferencia es que aquí el comando `Firmar` está activo. Y eso es precisamente lo que tendrá que ejecutar.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Ahora que la transacción está firmada, recuerde que su Wallet está en una máquina desconectada. Por lo tanto -aunque vea el comando `Broadcast` activo- su Wallet no podrá propagar la transacción a la red Bitcoin.



Lo que tienes que hacer ahora es repetir la operación de exportar la transacción firmada a la memoria USB, para poder importarla a un ordenador conectado a Internet y propagarla.



En el menú inferior izquierdo, vuelve a elegir _Compartir_ y luego _Guardar en archivo_.



![image](assets/en/28.webp)



Ahora el archivo tiene una extensión diferente: **en lugar de `.PSBT` ahora la transacción tiene extensión `.txn`. A partir de ahora es así como Electrum le permitirá reconocer las transacciones firmadas de las no firmadas**.



![image](assets/en/30.webp)



Para la propagación final de la transacción, saque la memoria USB del ordenador desconectado e insértela en el ordenador conectado a Internet.



Desde el reloj, repita el procedimiento de importación, es decir, desde el menú _Herramientas_ seleccione _Cargar transacción_ y finalmente _Desde fichero_.



![image](assets/en/31.webp)



Electrum le abrirá la ventana de transacción, notablemente diferente de la mostrada anteriormente en esta Wallet, en el sentido de que ahora está firmada (`Status: Signed`) y el comando `Broadcast` accesible.



La última operación que tienes que hacer es precisamente esa:



![image](assets/en/32.webp)



## Conclusiones



Tus pruebas han terminado. Si has seguido la guía y has obtenido los mismos resultados, habrás creado una Wallet Cold con Electrum, en dos ordenadores diferentes, que podrás utilizar a modo de airgap para almacenar tus Bitcoins.



Las únicas cosas a las que tendrás que prestar mucha atención son dos:


1) **nunca utilices Wallet airgap a direcciones receptoras generate**. Al estar desconectado, siempre te ofrecerá el primer Address, que coincide con el que acabas de utilizar para hacer la transacción de prueba;



![image](assets/en/33.webp)



como se puede ver en la imagen de arriba, el Wallet desconectado no conoce su propia historia Address. Es totalmente ciega en este aspecto. **La única tarea que puede hacer por ti es almacenar tus claves offline y firmar tus transacciones**_.



2) Utiliza una memoria USB dedicada sólo a este fin, **no utilices un soporte que uses con frecuencia**. Las herramientas de uso cotidiano son más susceptibles de sufrir ciberataques y, sin querer, podrías atacar incluso al ordenador que mantienes desconectado de la red. Una memoria USB que sólo utilices para este fin tiene muy pocas oportunidades de entrar en contacto con tu PC en línea, sobre todo si eres un hodler que no tiene que gastar, reduciendo así la probabilidad de recibir y luego transmitir virus, malware, etc.