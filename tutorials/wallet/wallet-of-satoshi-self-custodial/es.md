---
name: Wallet of Satoshi - Autocustodia
description: Descubra cómo configurar el modo de autocustodia de una cartera Wallet of Satoshi
---

![cover](assets/cover.webp)



***No tus claves, no tus monedas* es más que un dicho, es un principio fundamental de Bitcoin, lo que significa que si no controlas las **claves privadas** que desbloquean tus bitcoins, en realidad no eres su propietario.



Muchos usuarios suelen empezar con una wallet** **custodiada**, y luego migran a una wallet** **autocustodiada**, en la que ellos mismos controlan sus claves privadas.


En este tutorial, no le presentaremos una nueva wallet autocustodiada. En su lugar, le presentaremos una nueva característica de los wallet ***Wallet of Satoshi***: **el modo de autocustodia**.



El objetivo de esta nueva integración es permitir que los usuarios conserven el control de sus claves privadas al tiempo que se benefician de la simplicidad y de una experiencia de usuario fluida.



Antes de entrar en el meollo de la cuestión, dediquemos un momento a examinar el modo especial de autocustodia que ofrece Wallet of Satoshi (WoS).



## La particularidad del modo de autocustodia



La sencillez y fluidez del modo de autocustodia de WoS elimina la complejidad de abrir canales Lightning, administrar nodos... Pero, ¿cómo es esto posible?



El modo de autocustodia de Wallet of Satoshi está impulsado por **Spark**. Se trata de una solución Layer 2 para Bitcoin, creada por Lightspark, que utiliza tecnología **statechains**.



En consecuencia, no realiza sus transacciones directamente en la Lightning Network. Las interacciones entre la red **LN** y **Spark** tienen lugar a través de **intercambios atómicos**.



Por ejemplo, Bob desea pagar una factura Lightning utilizando WoS. Transfiere sus satoshi, pero en segundo plano, estos se enrutan a un **Spark Service Provider (SSP)** en Spark, que a su vez ejecuta el pago en la red Lightning.



Por el contrario, Alice desea obtener fondos directamente de su cartera WoS. En este caso, el **SSP** recibe sats a través de LN y acredita inmediatamente la cartera de Alice.



Por lo tanto, es importante tener en cuenta que para beneficiarte de la simplicidad y fluidez de WoS, necesitas depender de los servidores de Spark. Sin embargo, en términos de seguridad, si un SSP se vuelve malicioso o no está disponible, tienes el mecanismo de **salida unilateral**, una medida de seguridad que te permite recuperar tus fondos en Bitcoin on-chain (aunque esto puede ser lento y costoso) , garantizando una experiencia de autocustodia comparable a la de un nodo Lightning privado.



Teniendo en cuenta todos estos parámetros, puedes decidir entonces cuánto sats quieres mantener en tu autocustodia WoS.



Si eres nuevo en Wallet of Satoshi, naturalmente necesitarás descargar la aplicación móvil wallet. Sin embargo, si ya la estás utilizando y quieres saber cómo usar el **modo de autocustodia**, ve directamente a la sección **Configuración del modo de autocustodia** de este tutorial.



## Primeros pasos con Wallet of Satoshi



Ve a tu tienda de aplicaciones y descarga WoS.



![screen](assets/fr/03.webp)



Abra la aplicación una vez finalizada la descarga y pulse **Iniciar**.



![screen](assets/fr/04.webp)



Será redirigido a la interfaz principal de la aplicación. De hecho, cuando accedes a WoS por primera vez, la cartera ya es funcional y se abre sistemáticamente en modo custodia por defecto.



![screen](assets/fr/05.webp)



Aunque no quieras utilizar WoS en modo custodia, te recomendamos que lo configures primero. Para ello, consulta este tutorial.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Pasemos a la configuración de nuestro WoS en autocustodia.



## Configuración del modo de autocustodia



Haga clic en el menú hamburguesa (icono de 3 barras) situado en la esquina superior derecha de la interfaz principal.



![screen](assets/fr/06.webp)



A continuación, en el menú que aparece, haga clic en el submenú **Abrir Custodia Propia Wallet**.



![screen](assets/fr/07.webp)



WoS te dice inmediatamente que *el modo de autocustodia viene con una frase de recuperación. Además, eres el único responsable de la seguridad de tus fondos*.



![screen](assets/fr/08.webp)



Marque el botón "**Entiendo**" (1) y, a continuación, pulse el botón **Abrir Autocustodia Wallet** (2), que aparece en amarillo brillante.



![screen](assets/fr/09.webp)



### Crear una cartera de autocustodia



Después de hacer clic en el botón **Abrir Wallet de Custodia Propia**, haga clic en el botón **Crear un nuevo Wallet**.



![screen](assets/fr/10.webp)



WoS creará entonces una cartera de autocustodia para ti, de nuevo dentro de la misma aplicación. Podrás cambiar entre el modo **custodia** (disponible en algunas regiones) y el modo **autocustodia** cuando te convenga y en cualquier momento.



![screen](assets/fr/11.webp)



Una vez creada, serás redirigido a la interfaz principal de autocustodia de WoS. Notarás que no hay diferencias entre la visión general y las interfaces de una cartera de custodia WoS y las de una cartera de autocustodia WoS.



### Guardar la frase mnemotécnica



Pulse sobre el icono **Keychain + Backup Wallet** situado en la parte superior de la pantalla entre el nombre Wallet of Satoshi y el menú hamburguesa.



![screen](assets/fr/12.webp)



WoS ofrece dos formas diferentes de guardar tus 12 palabras (frase mnemotécnica): **copia de seguridad a través de Google Drive** y **copia de seguridad manual**.



Aunque te sugerimos la copia de seguridad manual, que es la más segura, también te mostraremos cómo hacerla a través de Google Drive.



#### Copia de seguridad a través de Google Drive



Haz clic en el botón **Google Drive Backup**.



![screen](assets/fr/13.webp)



Si optas por hacer una copia de seguridad con Google Drive, existe un alto riesgo de que tu cuenta de Google se vea comprometida. Una persona malintencionada tendría acceso al archivo que contiene tus 12 palabras y podría así acceder a tu wallet.



Añadir una contraseña para cifrar el archivo que contiene tus 12 palabras es sin duda una buena forma de añadir una capa extra de seguridad.



Así que activa el botón **Encriptar con contraseña** en las opciones avanzadas.



![screen](assets/fr/14.webp)



En la nueva interfaz que aparece, establece una contraseña segura y confírmala de nuevo.



![screen](assets/fr/15.webp)



Es importante recordar que, una vez elegida la contraseña, no debe olvidarla ni perder el soporte en el que la ha escrito. Si la olvidas o la pierdes, nunca más podrás acceder a tus 12 palabras y, por tanto, a tus fondos.



Tras elegir tu contraseña, selecciona una cuenta de Google para la copia de seguridad y, a continuación, concede los accesos requeridos por WoS.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Espere unos segundos. ¡Bingo! Su copia de seguridad se ha completado con éxito.



![screen](assets/fr/18.webp)



Siempre tienes la opción de hacer una copia de seguridad adicional eligiendo el segundo método de copia de seguridad: la copia de seguridad manual.


#### Copia de seguridad manual



Si optas por la copia de seguridad manual, te recomendamos encarecidamente que consultes este tutorial, que explora las mejores prácticas para hacer copias de seguridad de tu frase mnemotécnica de forma segura, para que no pierdas el acceso a tus bitcoins.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Pulse el botón **Respaldo manual**.



![screen](assets/fr/19.webp)



En la siguiente interfaz, WoS te recuerda algunas precauciones de seguridad a tener en cuenta antes de proceder con la copia de seguridad manual.



Active el botón **Comprendo** y pulse el botón **Siguiente**.



![screen](assets/fr/20.webp)



A continuación se le presentarán sus 12 palabras. Guárdelas y haga clic en el botón **Siguiente**.



![screen](assets/fr/21.webp)



En esta nueva interfaz, pulsa las palabras en el orden correcto.



![screen](assets/fr/22.webp)



Por último, haga clic en el botón **Siguiente**. ¡Enhorabuena! Su copia de seguridad se ha completado.



![screen](assets/fr/23.webp)



## Restauración de la cartera de autocustodia



Cuando quieras recuperar o restaurar tu WoS autocustodia wallet tras un cambio de teléfono o por cualquier otro motivo, estos son los pasos a seguir.



Para abrir la cartera WoS, haga clic en el menú hamburguesa situado en la esquina superior derecha de la interfaz principal.


En el menú que aparece, pulse sobre el submenú **Abrir Custodia Propia Wallet**.


En la nueva interfaz que aparece, pulse el botón **Restaurar Wallet existente**.



![screen](assets/fr/24.webp)



Elija un método de restauración y vaya al paso siguiente.



![screen](assets/fr/25.webp)



### Restaurar a través de Google Drive



1. Pulsa el botón **Restaurar desde Google Drive**.


2. Selecciona una cuenta de Google y deja que WoS recupere los datos de recuperación guardados en tu Google Drive.


3. A continuación, introduce tu contraseña de encriptación (si la habías definido previamente, claro) desde el archivo que contiene tus 12 palabras.


4. Espera unos instantes a que la restauración surta efecto y podrás acceder de nuevo a tu cartera.



### Restauración manual



1. Pulse el botón **Restablecer manualmente**.


2. A continuación, introduzca las 12 palabras de su frase mnemotécnica, escribiendo cada palabra delante de su número inicial.


3. Espera unos instantes a que la restauración surta efecto y podrás acceder de nuevo a tu cartera.




### Transferencia de bitcoins entre la custodia WoS y la autocustodia WoS



Cuando tengas bitcoins (sats) en tu wallet de custodia WoS y crees una wallet de autocustodia WoS, no perderás tus fondos. Mejor aún, puedes transferirlos a tu cartera de autocustodia y viceversa.



Para ello :


Puedes copiar tu dirección de autocustodia WoS de rayos o una factura que hayas creado.



![screen](assets/fr/26.webp)



Ahora abra su wallet de custodia y pulse el botón **Envoyer**.



A continuación, pegue la dirección o la factura. Pulsa **Envoyer** una segunda vez.



Vuelve a tu cartera de autocustodia y verás que efectivamente habías recibido los fondos.



![screen](assets/fr/27.webp)



## Enviar y recibir bitcoins



En cuanto al envío y recepción de bitcoins en modo de autocustodia, al igual que la visión general y las interfaces, no difieren del envío y recepción de bitcoins a través de un wallet de custodia de WoS.



Consulte el tutorial básico sobre el uso de Wallet of Satoshi en la Red Plan₿.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Ya puedes configurar y manejar tú mismo Wallet of Satoshi en modo de autocustodia.



Si te ha resultado útil este tutorial, déjame un pulgar verde a continuación. Muchas gracias