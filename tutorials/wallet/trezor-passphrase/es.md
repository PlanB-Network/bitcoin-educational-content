---
name: BIP-39 Passphrase Trezor
description: ¿Cómo añado una passphrase a mi cartera de Trezor?
---
![cover](assets/cover.webp)



Una passphrase BIP39 es una contraseña opcional que, combinada con la frase Mnemonic, proporciona una Layer adicional de seguridad para las carteras deterministas y jerárquicas Bitcoin. En este tutorial, descubriremos juntos cómo configurar una passphrase en su Bitcoin Wallet segura en un Trezor (Safe 3, Safe 5 y Model One).



![Image](assets/fr/01.webp)



Antes de empezar este tutorial, si no estás familiarizado con el concepto passphrase, su funcionamiento y sus implicaciones para tu Bitcoin Wallet, te recomiendo encarecidamente que consultes este otro artículo teórico donde lo explico todo (esto es muy importante, ya que utilizar una passphrase sin entender bien su funcionamiento puede poner en riesgo tus bitcoins) :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase en Trezor se maneja de la forma clásica si has optado por el estándar BIP39 durante la configuración (lo que recomiendo si no necesitas *Multi-share Backup*). La particularidad de Trezor es que puedes introducir la passphrase directamente en la Hardware Wallet, o a través del teclado de tu ordenador utilizando el software Trezor Suite. Esta segunda opción es considerablemente menos segura, ya que el ordenador tiene una superficie de ataque inmensamente mayor que la Hardware Wallet. Sin embargo, escribir una passphrase compleja puede ser más rápido en un teclado convencional que en la Hardware Wallet, lo que podría fomentar el uso de contraseñas fuertes. Así que siempre es mejor utilizar una passphrase, aunque haya que teclearla, que no utilizarla en absoluto. No obstante, es importante ser consciente del mayor riesgo de ataques numéricos que ello implica.



Estas opciones no están disponibles en todos los software de gestión de carteras compatibles con Trezor. Por ejemplo, para el Modelo Uno, passphrase puede introducirse a través del teclado en Sparrow Wallet. Para los modelos Model T, Safe 3 y Safe 5, debe utilizar Trezor Suite o introducir passphrase directamente en Hardware Wallet, ya que la opción de introducir a través de Sparrow fue desactivada por HWI hace unos años.



![Image](assets/fr/02.webp)



En Trezor Suite, tiene dos formas diferentes de gestionar la demanda de passphrase. Puede activar la opción "*passphrase*" en la pestaña "*Dispositivo*". Si la activa, Trezor Suite y todos los demás programas de gestión de cartera le pedirán sistemáticamente que introduzca su passphrase cada vez que se inicie. Si prefiere un enfoque más discreto al uso de una passphrase, puede mantener la configuración en "*Estándar*". En este caso, tendrá que acceder manualmente al menú de su Hardware Wallet en la esquina superior izquierda y hacer clic en el botón "*+ passphrase*" cada vez que lo inicie.



Antes de comenzar este tutorial, asegúrese de que ya ha inicializado su Trezor y generado su frase Mnemonic. Si no lo ha hecho, y su Trezor es nuevo, siga el tutorial específico para cada modelo disponible en Plan ₿ Network. Una vez que haya completado este paso, puede volver a este tutorial.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Añadir una passphrase a una caja fuerte 3 o 5



Una vez que haya creado su Wallet, guardado su Mnemonic y establecido un PIN, accederá al menú de inicio de Trezor Suite. En la esquina superior izquierda debería aparecer una ventana invitándote a activar la passphrase BIP39.



![Image](assets/fr/03.webp)



Si esta ventana no aparece, tendrás que activar manualmente la opción "*passphrase*" en la pestaña de configuración "*Dispositivo*".



![Image](assets/fr/04.webp)



Esta ventana le pide que introduzca su passphrase. Elige un passphrase potente y haz inmediatamente una copia de seguridad física, en un soporte como papel o metal. En este ejemplo, he elegido el passphrase: `fH3&kL@9mP#2sD5qR!82`. Se trata de un ejemplo; sin embargo, le recomiendo que elija una passphrase un poco más larga. Entre 30 y 40 caracteres sería lo ideal (como una buena contraseña).



por supuesto, nunca debes compartir tu passphrase en Internet, como hago yo en este tutorial. Este ejemplo Wallet sólo se utilizará en Testnet y se eliminará al final del tutorial.



Para recomendaciones más específicas sobre la elección de su passphrase, le invito de nuevo a consultar este otro artículo:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Si desea introducir su passphrase mediante el teclado de su ordenador, introdúzcalo en el campo previsto a tal efecto y, a continuación, haga clic en "*Acceder a passphrase Wallet*".



![Image](assets/fr/05.webp)



Su Hardware Wallet mostrará entonces su passphrase. Asegúrese de que coincide con su copia de seguridad física (papel o metal) antes de hacer clic en la pantalla para continuar.



![Image](assets/fr/06.webp)



Esto le dará acceso a su cartera protegida passphrase.



![Image](assets/fr/07.webp)



Si prefiere aumentar la seguridad introduciendo su passphrase sólo en su Trezor, cuando se le solicite, haga clic en "*Introducir passphrase en Trezor*".



![Image](assets/fr/08.webp)



Aparecerá un teclado T9 en tu Trezor, que te permitirá introducir tu passphrase. Una vez que haya completado su entrada, haga clic en la marca Green para aplicar la passphrase a su Wallet.



![Image](assets/fr/09.webp)



A continuación, tendrá acceso a su passphrase seguro Wallet.



![Image](assets/fr/10.webp)



Para utilizar Sparrow Wallet, el procedimiento es similar, pero para los modelos T, Safe 3 y Safe 5, passphrase debe introducirse en el Hardware Wallet y no a través del teclado del ordenador.



Siempre que Sparrow Wallet requiera acceso a tu Trezor, y no se haya aplicado passphrase desde la última puesta en marcha, tendrás que introducirlo utilizando el teclado T9.



![Image](assets/fr/11.webp)



## Añadir una passphrase a un Modelo Uno



En el Modelo Uno, el uso de un passphrase BIP39 es casi indispensable. Como este dispositivo no incorpora un Elemento Seguro, es relativamente fácil extraer información sensible. Por lo tanto, no es resistente a los ataques físicos. Sin embargo, como la passphrase no se conserva en el dispositivo después de apagarlo, el uso de una passphrase fuerte (no brutable) puede protegerle contra la mayoría de los ataques físicos conocidos en este modelo.



En el Modelo Uno, no es posible introducir el passphrase directamente en el Hardware Wallet. Tendrás que introducirlo a través del teclado del ordenador.



Una vez que haya creado su Wallet, guardado su Mnemonic y establecido un PIN, accederá al menú de inicio de Trezor Suite. En la esquina superior izquierda, debería aparecer una ventana invitándote a activar el passphrase BIP39.



![Image](assets/fr/12.webp)



Si no aparece esta ventana, debes activar la opción "*passphrase*" en la pestaña "*Dispositivo*" de la configuración.



![Image](assets/fr/13.webp)



Esta ventana le pide que introduzca su passphrase. Elige un passphrase fuerte y haz inmediatamente una copia de seguridad física, en un soporte como papel o metal. En este ejemplo, he elegido el passphrase: `fH3&kL@9mP#2sD5qR!82`. Esto es sólo un ejemplo; sin embargo, te recomiendo que elijas una passphrase un poco más larga. Entre 30 y 40 caracteres sería lo ideal (como una buena contraseña).



Para recomendaciones más específicas sobre la elección de su passphrase, le invito de nuevo a consultar este otro artículo:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Introduzca su passphrase en el campo correspondiente y pulse el botón "*Acceder a passphrase Wallet*".



![Image](assets/fr/14.webp)



Su Hardware Wallet mostrará su passphrase. Asegúrese de que coincide con su copia de seguridad física (papel o metal) y, a continuación, haga clic en el botón de la derecha para continuar.



![Image](assets/fr/15.webp)



Esto le llevará a su cartera protegida por passphrase.



![Image](assets/fr/16.webp)



Para utilizar Sparrow Wallet a partir de entonces, el procedimiento sigue siendo el mismo. Cada vez que Sparrow requiera acceso a su Hardware Wallet, y no se haya introducido la passphrase desde la última vez que se arrancó el dispositivo, deberá introducirla.



![Image](assets/fr/17.webp)



Enhorabuena, ya estás al día en el uso de la passphrase BIP39 en los monederos hardware de Trezor. Si quieres llevar tu seguridad Wallet un paso más allá, echa un vistazo a este tutorial sobre los sistemas de copia de seguridad *Multi-share* de Trezor (*Shamir's Secret Sharing Scheme*):



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar Green a continuación. No dudes en compartir este artículo en tus redes sociales. Muchas gracias