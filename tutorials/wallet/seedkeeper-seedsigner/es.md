---
name: Seedkeeper x SeedSigner
description: ¿Cómo utilizo Seedkeeper con mi SeedSigner?
---

![cover](assets/cover.webp)



*Gracias al equipo de [Satochip](https://satochip.io/) por aceptar reutilizar [sus vídeos](https://www.youtube.com/@satochip/videos) en este tutorial. Gracias también a [CryptoGuide](https://www.youtube.com/@CryptoGuide/) por su fork del firmware SeedSigner, que permite la compatibilidad con tarjetas inteligentes



---

El SeedSigner es un hardware wallet que montas tú mismo a partir de hardware estándar, normalmente en torno a una Raspberry Pi Zero. Este wallet se denomina "*stateless*": a diferencia de la mayoría de los otros modelos del mercado (Coldcard, Trezor, Ledger, etc.), no almacena ningún dato en la memoria permanente, y opera únicamente en directo desde la RAM. Como resultado, el seed de su cartera nunca se almacena en el SeedSigner. Cada vez que reinicies, tendrás que rellenarlo para que el dispositivo pueda firmar tus transacciones. El método más común es guardar tu seed como un código QR, que luego escaneas cada vez que lo utilizas (*SeedQR*).



Sin embargo, este enfoque presenta un riesgo importante: el seed debe permanecer accesible en texto claro para que pueda ser escaneado. En caso de robo o intrusión, un atacante podría hacerse fácilmente con ella y robar tus bitcoins.



Para superar esta debilidad, SeedSigner puede combinarse con [**Seedkeeper**](https://satochip.io/product/seedkeeper/), una tarjeta inteligente desarrollada por Satochip. Esto permite almacenar frases mnemotécnicas (u otros secretos) en una secure element protegida por un código PIN. El applet Seedkeeper es de código abierto, y su secure element tiene certificación EAL6+. Utilizado junto con SeedSigner, ofrece una característica de seguridad muy interesante: tus claves permanecen gestionadas totalmente fuera de línea, firmas tus transacciones en una pantalla de confianza, y la seed está protegida físicamente en una tarjeta inteligente resistente a ataques físicos.



Todo lo que necesitas para completar la instalación son los siguientes elementos:




- El equipo habitual necesario para un SeedSigner clásico: una Raspberry Pi Zero, una pantalla Waveshare de 1,3", una cámara compatible y una tarjeta microSD (encontrarás más detalles en el tutorial de SeedSigner más abajo);
- El kit de extensión SeedSigner, disponible [en la tienda oficial de Satochip](https://satochip.io/product/seedsigner-extension-kit/), que te permite leer y escribir en la tarjeta inteligente directamente desde tu SeedSigner. Otra opción es utilizar un lector externo de tarjetas inteligentes, que se puede conectar por cable a un puerto Micro-USB de la Raspberry Pi. Sin embargo, no he probado esta solución por mí mismo;
- Un Seedkeeper o, en su defecto, una tarjeta inteligente en blanco en la que instalar el applet Seedkeeper (el kit de ampliación vendido por Satochip ya incluye una tarjeta inteligente en blanco).



![Image](assets/fr/01.webp)



Este tutorial cubre dos escenarios:




- Si ya dispone de una cartera Bitcoin gestionada a través de su SeedSigner, sólo tiene que instalar el nuevo firmware. A continuación, puede seguir utilizando su wallet existente, esta vez utilizando Seedkeeper para mayor seguridad.
- Si aún no tiene una Bitcoin wallet asociada a su SeedSigner, deberá seguir los pasos **5** y **6** del tutorial que se menciona a continuación. Estas secciones explican cómo generate una frase mnemotécnica con el SeedSigner, guardarla a través de un *SeedQR*, y luego conectar este wallet a Sparrow Wallet para gestionarlo. No voy a entrar en estos procedimientos aquí y **estoy asumiendo que ya tienes una Bitcoin wallet funcionando, configurada con Sparrow y tu SeedSigner**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Instalar firmware



Para utilizar tu SeedSigner con un Seedkeeper, necesitas instalar un firmware alternativo, diferente al del SeedSigner original, para soportar la lectura de tarjetas inteligentes. Para ello, [recomiendo utilizar fork de "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Descarga [la última versión de la imagen](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) correspondiente al modelo de Raspberry Pi que estés utilizando.



![Image](assets/fr/02.webp)



Si aún no lo tiene, descargue el software [Balena Etcher](https://etcher.balena.io/) y, a continuación, proceda como se indica a continuación:




- Inserta la tarjeta microSD en tu ordenador;
- Lanzamiento Etcher ;
- Selecciona el archivo `.zip` que acabas de descargar;
- Selecciona la tarjeta microSD como destino;
- Haga clic en "Flash".



![Image](assets/fr/03.webp)



Espera a que el proceso finalice: tu microSD ya está lista para ser utilizada. Ya puedes pasar a montar tu dispositivo.



Para más detalles sobre la instalación del firmware y la verificación del software (un paso que te recomiendo encarecidamente que realices), consulta el siguiente tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Montaje del lector de tarjetas inteligentes



![video](https://youtu.be/jqE8HDMCImA)



Empieza instalando la cámara en la Raspberry Pi Zero, introduciéndola con cuidado en el pasador de la cámara y bloqueándola con la pestaña negra. A continuación, coloca la Pi en la parte inferior de la carcasa, asegurándote de alinear los puertos con las aberturas correspondientes.



![Image](assets/fr/04.webp)



A continuación, conecta el lector de tarjetas inteligentes a los pines GPIO de la Raspberry Pi Zero.



![Image](assets/fr/05.webp)



Deslice la cubierta de plástico sobre el lector de tarjetas inteligentes hasta que quede correctamente colocada.



![Image](assets/fr/06.webp)



Luego añade la pantalla a los pines GPIO de la extensión.



![Image](assets/fr/07.webp)



Por último, inserta la tarjeta microSD que contiene el firmware en el puerto lateral de la Raspberry Pi Zero.



![Image](assets/fr/08.webp)



Ahora puedes conectar tu SeedSigner a través del puerto Micro-USB de la Raspberry Pi Zero o a través del puerto USB-C de la extensión. Ambas opciones funcionan. Espera unos segundos a que se inicie y deberías ver la pantalla de bienvenida.



![Image](assets/fr/09.webp)



Para más detalles sobre la configuración inicial de su SeedSigner, le recomiendo el siguiente tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flashear una tarjeta inteligente con el applet Seedkeeper (opcional)



![video](https://youtu.be/NF4HemyEcOY)



Si ya tienes un Seedkeeper, puedes saltarte este paso e ir directamente al paso 4. En esta sección, veremos cómo instalar el applet Seedkeeper en una tarjeta inteligente en blanco (método DIY).



Para empezar, abra el menú `Herramientas > Herramientas de tarjeta inteligente` de su SeedSigner.



![Image](assets/fr/10.webp)



A continuación, seleccione `Herramientas DIY > Instalar Applet`.



![Image](assets/fr/11.webp)



Inserte su tarjeta inteligente en el lector SeedSigner, con el chip hacia abajo, y elija el applet `SeedKeeper`.



![Image](assets/fr/12.webp)



Tenga paciencia durante la instalación: el proceso puede durar varias decenas de segundos.



![Image](assets/fr/13.webp)



Una vez que el applet se haya instalado correctamente, puede continuar con el paso 4.



![Image](assets/fr/14.webp)



## 4. Guardar un SeedQR existente en Seedkeeper



![video](https://youtu.be/X-vmFHU9Ec8)



Ahora que su Seedkeeper está operativo, puede guardar su mnemónica Bitcoin wallet en la tarjeta inteligente. Para empezar, encienda su SeedSigner como de costumbre y, a continuación, escanee el *SeedQR* de su wallet para cargarlo en el dispositivo. Una vez importada la seed, simplemente seleccione `Hecho`.



![Image](assets/fr/15.webp)



Cuando el seed esté cargado, acceda al menú `Backup Seed`.



![Image](assets/fr/16.webp)



A continuación, inserta tu Seedkeeper en la unidad SeedSigner y selecciona la opción `A SeedKeeper`.



![Image](assets/fr/17.webp)



A continuación, el SeedSigner le pedirá que introduzca un código PIN para su Seedkeeper. Como se trata de una tarjeta en blanco, aún no se ha definido ningún código. Introduzca cualquier código para omitir este paso y, a continuación, valide.



![Image](assets/fr/18.webp)



SeedSigner detecta que Seedkeeper aún no se ha inicializado (es decir, no se ha establecido ninguna contraseña). Haga clic en `Entiendo` para continuar.



![Image](assets/fr/19.webp)



Ahora elige el nuevo código PIN de tu Seedkeeper, entre 4 y 16 caracteres. Para mayor seguridad, elige un código largo y aleatorio: es la única barrera que protege el acceso físico a tu frase mnemotécnica.



Acuérdate de guardar este PIN en cuanto lo crees, bien en un gestor de contraseñas fiable, bien en un soporte físico aparte, dependiendo de tu estrategia. En este último caso, asegúrese de no guardar nunca el soporte que contiene el PIN en el mismo lugar que su Seedkeeper, ya que de lo contrario la protección perderá eficacia. Es importante tener una copia de seguridad: **Sin este PIN, no podrás acceder a tu seed, y tus bitcoins se perderán**.



![Image](assets/fr/20.webp)



A continuación, puede definir una `Etiqueta` asociada a su frase mnemotécnica. Esta etiqueta es útil si almacena varios secretos en Seedkeeper, para poder identificarlos fácilmente.



![Image](assets/fr/21.webp)



Su frase mnemotécnica está ahora guardada en la tarjeta inteligente.



![Image](assets/fr/22.webp)



En términos de estrategia de seguridad, existen varios enfoques posibles, en función de sus necesidades y nivel de exposición al riesgo. Personalmente, te recomiendo que conserves al menos 2 copias de tu seed:




- Se trata de una primicia para las tarjetas inteligentes, que puedes mantener fácilmente accesibles para operaciones cotidianas, como verificar direcciones o firmar transacciones. Este método es práctico (como veremos en la parte 5) y sigue siendo seguro gracias a la protección que ofrece el código PIN, por lo que puedes mantenerla accesible sin mayor riesgo;
- Una segunda copia de su frase mnemotécnica no encriptada, que servirá como copia de seguridad definitiva de su cartera, para ser utilizada únicamente en caso de pérdida o robo del Seedkeeper. Como esta versión no está encriptada, debe guardarse en un lugar separado y más seguro, para evitar que las 2 copias de seguridad se vean comprometidas simultáneamente.



En función de su estrategia de protección y de su perfil de riesgo, también puede duplicar el seed en varios Seedkeepers diferentes, o crear varias copias físicas del mnemónico. Para saber más sobre estas prácticas, echa un vistazo al siguiente tutorial:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Cargar un seed de Seedkeeper



![video](https://youtu.be/ms0Iq_IyaoE)



Ahora puedes utilizar tu Seedkeeper para cargar tu frase mnemotécnica en el SeedSigner al arrancar, y así firmar tus transacciones Bitcoin. Para empezar, enciende tu SeedSigner conectándolo y abre el menú `Seeds`.



![Image](assets/fr/23.webp)



A continuación, seleccione la opción `Desde SeedKeeper`.



![Image](assets/fr/24.webp)



Inserte su Seedkeeper en el lector de tarjetas inteligentes e introduzca su código PIN para desbloquearlo. Confirma tu entrada pulsando el botón de confirmación inferior derecho, `KEY3`.



![Image](assets/fr/25.webp)



Seedkeeper puede contener varios secretos, por lo que SeedSigner le pedirá que elija el que desea cargar. La etiqueta que aparece corresponde al nombre que definiste en el paso 4. Si, como en mi caso, sólo has registrado un seed, sólo habrá una opción disponible.



![Image](assets/fr/26.webp)



Su seed ya está cargado. Compruebe que se trata de la wallet correcta comparando la huella digital que aparece en pantalla con la especificada en los ajustes de su Sparrow Wallet. Esta huella digital también se proporcionó cuando se creó la wallet por primera vez.



Si utiliza un passphrase, puede aplicarlo en esta fase (véase la parte 6 de este tutorial). De lo contrario, simplemente haz clic en `Hecho`.



![Image](assets/fr/27.webp)



A continuación, puede utilizar su wallet como de costumbre: compruebe sus direcciones de entrega y firme las transacciones, igual que con un SeedSigner clásico. Para saber más sobre su uso, consulte el tutorial dedicado :



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Uso de Seedkeeper con un passphrase BIP39



¿Utiliza una passphrase para proteger su cartera de Bitcoin? También puede registrarla en su Seedkeeper, junto con su seed. Esta solución le permitirá cargar rápidamente su wallet en el SeedSigner, sin tener que introducir manualmente la passphrase en el pequeño teclado cada vez que la utilice.



Este método me parece especialmente interesante, ya que permite beneficiarse de las ventajas de seguridad de la passphrase, eliminando al mismo tiempo las limitaciones asociadas a su uso cotidiano. He aquí un ejemplo de configuración que yo recomendaría:




- Guarde su seed y passphrase en un Seedkeeper, protegido por un código PIN fuerte (esto es importante). Esta copia de seguridad le permitirá utilizar fácilmente su wallet a diario. Si lo desea, puede duplicar esta información en un segundo Seedkeeper;
- Guarde también una copia clara de su mnemónica y passphrase, en papel o metal. Esta es su copia de seguridad de último recurso si pierde su Seedkeeper o su PIN. Asegúrate de guardar estas copias en lugares separados, para que no puedan ser comprometidas simultáneamente.



En esta configuración, si alguien se hace con tu mnemónico en texto plano solamente, no podrá robar nada sin conocer la passphrase (siempre que, por supuesto, sea lo suficientemente fuerte como para resistir un ataque de fuerza bruta). Por el contrario, si alguien descubre tu passphrase en texto plano, seguirá siendo inutilizable sin la frase mnemotécnica correspondiente.



Por último, si alguien consigue acceder físicamente a tu Seedkeeper que contiene la seed y la passphrase, no podrá extraer nada sin conocer el código PIN. A diferencia de la passphrase, este código no puede forzarse, ya que la tarjeta inteligente se bloquea automáticamente tras 5 intentos no válidos.



Por tanto, la seguridad de esta configuración se basa en 2 puntos esenciales:




- Un **passphrase fuerte**: debe ser largo, aleatorio y contener una gran variedad de caracteres. Su complejidad no es un problema para ti, ya que sólo tendrás que introducirlo una vez en el teclado durante la inicialización; después, será transmitido por Seedkeeper ;
- Un **código PIN** para Seedkeeper: también aleatorio y compuesto por 16 caracteres.



Para establecer esta configuración, comience cargando su passphrase en el SeedSigner de la forma habitual. Puede seguir el procedimiento detallado en este tutorial:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Una vez que su cartera con passphrase se haya cargado correctamente en el SeedSigner, abra el menú `Seeds` y seleccione la huella correspondiente a esta cartera. Tenga en cuenta que esta huella difiere de la de la cartera sin passphrase.



![Image](assets/fr/28.webp)



A continuación, haz clic en `Backup Seed`, inserta el Seedkeeper en la unidad y selecciona `To SeedKeeper`.



![Image](assets/fr/29.webp)



Introduzca su PIN para desbloquear Seedkeeper y asigne una etiqueta a este secreto. Puedes dejar la huella digital como etiqueta para mantener algún tipo de negación plausible, o indicar explícitamente `Passphrase Wallet`, por ejemplo.



![Image](assets/fr/30.webp)



Su cartera passphrase ya está registrada en Seedkeeper.



![Image](assets/fr/31.webp)



La próxima vez que arranques, simplemente inserta tu Seedkeeper en la unidad, luego navega a `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Introduzca su PIN para desbloquear la tarjeta inteligente y, a continuación, seleccione la wallet correspondiente a su passphrase.



![Image](assets/fr/33.webp)



Compruebe la passphrase y su impresión wallet, luego confirme.



![Image](assets/fr/34.webp)



Ahora puede acceder a su cartera con passphrase y firmar sus transacciones como lo haría normalmente en un SeedSigner.



## 7. Opciones adicionales



En el menú `Herramientas > Herramientas de Smartcard`, encontrarás varias opciones para gestionar tu Seedkeeper:





- En el menú `Herramientas comunes`, puede :
 - Compruebe la autenticidad de la tarjeta;
 - Cambiar código PIN ;
 - Cambia las etiquetas asociadas a tus secretos ;
 - Desactivar la función NFC (recomendado si sólo se utiliza el lector de chip) ;
 - Realiza un restablecimiento de fábrica.





- En el menú `Funciones de SeedKeeper`, puede :
 - Consulte la lista de secretos registrados ;
 - Guardar un nuevo secreto ;
 - Borrar un secreto existente ;
 - Guarde o cargue sus descriptores (función útil para las carteras multi-sig).





- En el menú `Herramientas DIY`, puedes :
 - Compilación del applet Seedkeeper ;
 - Instale el applet en una tarjeta en blanco ;
 - Borre un applet Seedkeeper para reiniciarlo y dejarlo en blanco de nuevo.



Ahora ya sabe cómo utilizar Seedkeeper para realizar copias de seguridad de su cartera de forma segura en combinación con SeedSigner.



Si este montaje le ha convencido, no dude en apoyar los proyectos que lo hacen posible:




- Comprando su equipo directamente [en el sitio web de Satochip](https://satochip.io/shop/);
- Haciendo [una donación al proyecto SeedSigner](https://seedsigner.com/donate/);
- Suscribiéndose al [canal de YouTube de CryptoGuide](https://www.youtube.com/@CryptoGuide/), dirigido por la persona que mantiene el repositorio de GitHub que aloja el firmware modificado.