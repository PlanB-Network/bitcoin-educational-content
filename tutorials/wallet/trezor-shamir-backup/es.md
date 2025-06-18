---
name: Respaldo Trezor Shamir
description: Frases Mnemonic monopartitas y multipartitas en Trezor
---
![cover](assets/cover.webp)



*Crédito de la imagen: [Trezor.io](https://trezor.io/)*



## Nuevas opciones de copia de seguridad en Trezor



Desde 2023, Trezor ofrece un nuevo formato de copia de seguridad denominado ***Single-share Backup***, que sustituye gradualmente al enfoque clásico basado en BIP39 que se encuentra en la mayoría de las carteras. A diferencia de las frases tradicionales Mnemonic de 12 o 24 palabras, este nuevo formato se basa en una única frase de 20 palabras derivada de un estándar desarrollado por SatoshiLabs: **SLIP39**. El objetivo es mejorar la robustez y legibilidad de las copias de seguridad, permitiendo al mismo tiempo una migración fluida a un modelo de copia de seguridad distribuida.



Este modelo distribuido se denomina ***Multi-share Backup***. Se basa en el mismo principio, pero en lugar de generar una única frase Mnemonic, la divide en varios fragmentos llamados ***shares***, cada uno de los cuales es una frase Mnemonic por derecho propio. Para restablecer la cartera, hay que reunir un cierto número de estas *shares* (definido por un *umbral*). Por ejemplo, en un esquema de 3 de 5, 3 *acciones* de las 5 restaurarán la cartera. Tenga en cuenta que el sistema de copia de seguridad distribuida de Trezor es diferente de los monederos Multisig. Para gastar sus bitcoins, sólo se requiere su Hardware Wallet Trezor. Sólo se requiere una firma. La distribución se aplica sólo a nivel de la frase Mnemonic, es decir, la copia de seguridad.



![Image](assets/fr/01.webp)



Este sistema resuelve el problema del punto único de fallo de la frase Mnemonic sin los inconvenientes asociados a la gestión de un BIP39 Multisig o passphrase. El proceso de recuperación ya no se basa en un único dato, sino en varios, con la ventaja añadida de la tolerancia a las pérdidas gracias al umbral.



Los usuarios que hayan creado una cartera con *Single-share Backup* pueden cambiar a *Multi-share Backup* en cualquier momento sin tener que migrar su cartera. Las direcciones y cuentas receptoras seguirán siendo idénticas. El sistema *Multi-share Backup* sólo afecta a la copia de seguridad, mientras que el resto de la cartera permanece sin cambios.



Multi-share Backup* está disponible en el Trezor Model T, Safe 3 y Safe 5. Esta función no es compatible con el Trezor Model One.



**Nota importante:** El sistema *Multi-share* de Trezor es criptográficamente seguro, ya que utiliza el esquema *Shamir's Secret Sharing* para su distribución. Desaconsejamos encarecidamente aplicar un sistema similar de forma manual, dividiendo uno mismo una frase clásica de Mnemonic. Es una mala práctica que aumenta significativamente el riesgo de robo y pérdida de tus bitcoins, así que no lo hagas. Una frase clásica de Mnemonic se almacena en su totalidad.



## El secreto de Shamir compartido en SLIP39



El mecanismo criptográfico subyacente a las copias de seguridad *Multi-share* en Trezor es el *Shamir's Secret Sharing Scheme* (SSSS). Su principio es el siguiente: la información secreta (en este caso, el seed de la cartera) se transforma en un polinomio matemático. A continuación, se calculan varios puntos de este polinomio, cada uno de los cuales se convierte en una acción. El secreto original se reconstruye por interpolación polinómica, reuniendo un número mínimo de puntos (el umbral).



No se puede deducir ninguna información secreta a partir de un número de acciones inferior al umbral, lo que garantiza una seguridad teórica perfecta de la información secreta. En otras palabras, ni siquiera un atacante con una potencia de cálculo ilimitada puede adivinar seed si no se alcanza el umbral.



SLIP39 utiliza este esquema para distribuir la cartera seed. Cada acción es una frase de 20 palabras, construida a partir de una lista de 1024 palabras (diferente de la lista de BIP39).



## Configuración de una copia de seguridad compartida en un Trezor



Al crear su cartera en Trezor, tiene tres opciones diferentes:




- Utilice una frase clásica BIP39 Mnemonic de 12 o 24 palabras;
- Utilice una frase Mnemonic de uso compartido único (SLIP39);
- Configurar varias frases Mnemonic en Multi-share (SLIP39).



Si opta por una frase SLIP39 Mnemonic de participación única, podrá pasar a una multipartición más adelante sin tener que reiniciar la cartera. En cambio, si parte de una cartera BIP39 clásica (frase de 12 o 24 palabras), no podrá convertirla directamente en Multiparticipativa. Tendrá que crear una nueva cartera Multiparticipativa desde cero y transferir sus fondos de la cartera antigua a la nueva mediante una o varias operaciones Bitcoin. Se trata de una operación más compleja y costosa. Si desea realizar esta migración, le recomiendo que compre un nuevo Trezor Hardware Wallet para evitar tener que introducir su seed en un software de cartera.



En este tutorial, primero veremos cómo configurar una Multi-compartición al crear una cartera, luego, en una sección posterior, veremos cómo convertir una Single-share a Multi-share en una cartera existente.



Si necesita ayuda con la configuración inicial de su dispositivo, también disponemos de un tutorial detallado para cada modelo de Trezor:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Sobre una nueva cartera



Ya ha completado la configuración inicial de su Trezor y está listo para crear la cartera. En Trezor Suite, haga clic en el botón "*Crear nueva Wallet*".



![Image](assets/fr/02.webp)



Elige la opción "*Copia de seguridad multi-compartida*" y, a continuación, haz clic en "*Crear Wallet*".



![Image](assets/fr/03.webp)



Acepte las condiciones de uso en su Trezor y confirme la creación de la cartera.



![Image](assets/fr/04.webp)



En Trezor Suite, haga clic en "*Continuar con la copia de seguridad*".



![Image](assets/fr/05.webp)



Lee atentamente las instrucciones, confírmalas y haz clic en "*Crear copia de seguridad de Wallet*".



![Image](assets/fr/06.webp)



Para más información sobre la forma correcta de guardar y gestionar tus frases Mnemonic, te recomiendo encarecidamente que sigas este otro tutorial, especialmente si eres principiante:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

En el Trezor, seleccione el número total de acciones que desea configurar. Las configuraciones más comunes son 2-de-3 y 3-de-5. Para este ejemplo, crearé un 2-de-3, por lo que seleccionaré 3 acciones. Cada acción representará una frase Mnemonic de 20 palabras.



*Para los usuarios de Safe 5, aunque la pantalla diga "*Toque para continuar*", en realidad tendrá que deslizar el dedo hacia arriba para confirmar



![Image](assets/fr/07.webp)



A continuación, confirme el umbral, es decir, el número de acciones necesarias para recuperar el acceso al Wallet y a los bitcoins que contiene.



![Image](assets/fr/08.webp)



El Trezor creará sus distintas acciones (frases Mnemonic) utilizando su generador de números aleatorios. Asegúrese de que no le están observando durante esta operación. Escriba las palabras que aparecen en la pantalla en el soporte físico de su elección. Es importante que las palabras estén numeradas y en orden secuencial.



Te recomiendo que anotes cada acción en un soporte distinto y gestiones cuidadosamente su almacenamiento para evitar que varias estén accesibles en el mismo lugar. Por ejemplo, para una configuración 2 de 3 como la mía, una opción sería guardar una acción en mi casa, otra con un amigo de confianza y la última en una caja fuerte del banco. La elección de los lugares de almacenamiento dependerá de tu estrategia personal de seguridad.



En la parte superior de la pantalla puede ver qué acción está viendo en ese momento.



por supuesto, nunca debes compartir estas palabras en Internet, como estoy haciendo en este tutorial. Este ejemplo Wallet sólo se utilizará en el Testnet y se eliminará al final del tutorial.**_



![Image](assets/fr/09.webp)



Para pasar a las palabras siguientes, pulsa en la parte inferior de la pantalla. Puedes retroceder deslizándote hacia abajo. Cuando hayas escrito todas las palabras, mantén el dedo en la pantalla para pasar a la siguiente acción y repite la operación.



![Image](assets/fr/10.webp)



Al final de cada grabación compartida, se le pedirá que seleccione las palabras de su frase Mnemonic para confirmar que las ha escrito correctamente.



![Image](assets/fr/11.webp)



Y eso es todo, has realizado con éxito una copia de seguridad de tu cartera utilizando la opción Multi-compartir. Ahora puede continuar con el resto de las instrucciones de configuración.



### En una cartera existente de una sola acción



Si ya dispone de un Trezor Wallet con una copia de seguridad de una sola acción (una frase SLIP39 Mnemonic, no la clásica frase BIP39), y desea mejorar la disponibilidad y la seguridad de su copia de seguridad Wallet, puede configurar un sistema de varias acciones sin tener que transferir sus bitcoins.



Para ello, conecte y desbloquee su Hardware Wallet. En Trezor Suite, vaya a Ajustes.



![Image](assets/fr/12.webp)



Ve a la pestaña "*Dispositivo*".



![Image](assets/fr/13.webp)



A continuación, haz clic en "*Crear copia de seguridad multi-compartida*".



![Image](assets/fr/14.webp)



Lee las instrucciones y, a continuación, haz clic en "*Crear copia de seguridad multi-compartida*".



![Image](assets/fr/15.webp)



A continuación, deberá introducir su frase Mnemonic actual (de una sola palabra) en la pantalla de su Trezor. Seleccione el número de palabras (por defecto es 20).



![Image](assets/fr/16.webp)



A continuación, utilice el teclado en pantalla del Trezor para introducir cada palabra de la frase Mnemonic actual.



![Image](assets/fr/17.webp)



A continuación, puede elegir la configuración de su Multi-share Backup siguiendo las instrucciones proporcionadas en la sección anterior.



![Image](assets/fr/18.webp)



Una vez que haya creado su copia de seguridad multipartita, tendrá que decidir qué hacer con su frase original Mnemonic monopartita. Como la cartera Bitcoin sigue siendo la misma, esta frase única siempre permitirá acceder a ella. Esto dependerá de tu estrategia de seguridad, pero en general, es recomendable destruir esta frase para eliminar este único punto de fallo, que es precisamente el objetivo de Multi-share Backup. Si decides destruirla, asegúrate de hacerlo de forma segura, ya que **sigue dando acceso a tus bitcoins**.



Enhorabuena, ya está al día sobre el uso de las copias de seguridad simples y múltiples en los monederos hardware Trezor. Si quieres ir un paso más allá en la seguridad de tu Wallet, echa un vistazo a este tutorial sobre contraseñas BIP39:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar Green a continuación. No dudes en compartir este artículo en tus redes sociales. ¡Muchas gracias!



## Recursos adicionales





- [SLIP-0039: Intercambio de secretos de Shamir para códigos Mnemonic](https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Multi-share Backup on Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamir's secret sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).