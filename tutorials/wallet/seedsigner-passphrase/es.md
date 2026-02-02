---
name: BIP-39 Passphrase SeedSigner
description: ¿Cómo añado una passphrase a mi cartera SeedSigner?
---

![cover](assets/cover.webp)



Una passphrase BIP39 es una contraseña opcional que, combinada con la frase mnemotécnica, proporciona una capa adicional de seguridad para los monederos deterministas y jerárquicos Bitcoin. En este tutorial, descubriremos juntos cómo configurar una passphrase en tu Bitcoin wallet utilizada con un SeedSigner.



![Image](assets/fr/01.webp)



## Requisitos previos antes de añadir una frase de contraseña



Antes de empezar este tutorial, si no estás familiarizado con el concepto passphrase, su funcionamiento y sus implicaciones para tu Bitcoin wallet, te recomiendo encarecidamente que consultes este otro artículo teórico donde lo explico todo (esto es muy importante, ya que utilizar una passphrase sin entender bien su funcionamiento puede poner en riesgo tus bitcoins) :



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Antes de empezar este tutorial, asegúrese también de que ya ha inicializado su SeedSigner y generado su frase mnemotécnica. Si no lo ha hecho y su SeedSigner es nuevo, siga el tutorial de Plan ₿ Academy. Una vez que haya completado este paso, puede volver a este tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## ¿Cómo añado un passphrase al SeedSigner?



Al añadir una passphrase a su cartera gestionada a través de SeedSigner, se crea una cartera completamente nueva, que genera un conjunto de claves totalmente distinto. En consecuencia, si ya tiene una cartera que contiene satss, ya no podrá acceder a ella con la passphrase, puesto que genera una cartera completamente distinta.



Para aplicar una passphrase a su SeedSigner, encienda el dispositivo y escanee su SeedQR como de costumbre. El SeedSigner mostrará entonces la huella digital de su wallet actual, correspondiente a la que **sin passphrase**. La wallet con passphrase tendrá una huella diferente.



Haga clic en el botón `BIP-39 Passphrase`.



![Image](assets/fr/02.webp)



A continuación, introduzca la passphrase de su elección en el campo correspondiente, utilizando el teclado que aparece en pantalla. Asegúrate de hacer una o varias copias de seguridad físicas (en papel o metal): la pérdida de esta passphrase supondrá la pérdida permanente del acceso a tus bitcoins. **Para restaurar una wallet, tanto la mnemónica como la passphrase son esenciales ** Si se pierde cualquiera de las dos, tus bitcoins quedarán irremediablemente bloqueados.



Una vez que hayas completado tu entrada, valídala pulsando el botón `KEY3` en la parte inferior derecha del SeedSigner.



![Image](assets/fr/03.webp)



*En este ejemplo, he utilizado el passphrase `pba`. Sin embargo, en su caso, asegúrese de elegir un passphrase robusto. Para saber cómo definir un passphrase óptimo, consulta este otro artículo:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

El SeedSigner muestra entonces la nueva huella digital de su passphrase wallet. Haga varias copias de esta huella digital: es importante cuando se utiliza una wallet con passphrase, ya que permite comprobar, cada vez que se introduce la passphrase, que no se ha cometido ningún error tipográfico y que se está accediendo a la wallet correcta.



Por ejemplo, si en mi caso escribo por error la passphrase `Pba` al iniciar el SeedSigner en lugar de `pba`, este simple cambio de minúsculas a mayúsculas dará lugar a la creación de una cartera totalmente distinta a la que quiero acceder.



Esta huella digital no supone ningún riesgo para la seguridad o confidencialidad de su wallet. No revela ninguna información, pública o privada, sobre sus claves. Por lo tanto, a diferencia de la mnemónica y de la passphrase, puede guardar la huella digital en un soporte digital. Te recomiendo que guardes una copia en varios sitios: en un papel, en un gestor de contraseñas, etc.



Una vez que hayas guardado tu huella dactilar, haz clic en "Hecho".



![Image](assets/fr/04.webp)



A continuación, tendrá acceso a todas las funciones de su cartera, como en un SeedSigner clásico.



![Image](assets/fr/05.webp)



Ahora puedes importar el almacén de claves en Sparrow Wallet y utilizar tu wallet con normalidad. Cada vez que reinicies, tendrás que escanear tu SeedQR y volver a introducir tu passphrase usando el teclado, como hicimos aquí.



Antes de utilizar realmente su wallet con passphrase, le recomiendo encarecidamente que realice una prueba de recuperación completa en vacío. Esto le permitirá confirmar que sus copias de seguridad de la frase mnemónica y del passphrase son válidas. Para aprender a realizar esta comprobación, consulte el siguiente tutorial:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895