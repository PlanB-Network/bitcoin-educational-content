---
name: LineageOS
description: Sistema operativo Android gratuito y sin complicaciones para smartphones
---

![cover](assets/cover.webp)



Los sistemas Android convencionales preinstalados en nuestros smartphones plantean una serie de problemas bien conocidos: integración intensiva de los servicios de Google que conlleva un seguimiento constante de los datos, aplicaciones patrocinadas no deseadas (bloatware) impuestas por los fabricantes y abandono del seguimiento de actualizaciones al cabo de unos años, lo que condena a los dispositivos que aún funcionan a una obsolescencia programada.



LineageOS se presenta como una respuesta elegante a estos problemas. Producto de la comunidad de código abierto y sucesor directo de CyanogenMod (discontinuado a finales de 2016), LineageOS es un sistema operativo móvil gratuito basado en Android que devuelve a los usuarios el control de sus smartphones. Lanzado oficialmente en diciembre de 2016, el proyecto cuenta ya con más de 4,4 millones de instalaciones activas en todo el mundo y es compatible con cientos de modelos de teléfonos de más de 20 marcas diferentes.



![lineageos-homepage](assets/fr/01.webp)



*Página web oficial de LineageOS en la que se presentan el proyecto y sus objetivos*



## ¿Qué es LineageOS?



### Filosofía y objetivos



LineageOS es un sistema operativo móvil de código abierto basado en el Android Open Source Project (AOSP), desarrollado por una amplia comunidad de colaboradores voluntarios de todo el mundo. Su lema no oficial podría ser "Tu dispositivo, tus reglas": el proyecto pretende alargar la vida útil de los smartphones al tiempo que ofrece una experiencia Android optimizada y respetuosa con la privacidad.



El proyecto surgió de las cenizas de CyanogenMod, una de las ROMs alternativas de Android más populares de la historia. Cuando CyanogenMod Inc. cerró sus puertas en diciembre de 2016, la comunidad se movilizó para crear LineageOS, conservando el espíritu de innovación y la filosofía de código abierto que caracterizaron a su predecesora.



A diferencia de las distribuciones OEM de Android, LineageOS no preinstala ninguna aplicación de Google por defecto y elimina por completo el bloatware. Los usuarios empiezan con un sistema minimalista que incluye solo las aplicaciones esenciales (teléfono, mensajes, cámara, navegador) y son libres de elegir qué añadir después.



### Impacto y comunidad



Las estadísticas oficiales revelan la escala del proyecto: con más de 4,4 millones de instalaciones activas en 224 países, LineageOS representa una de las alternativas a Android más adoptadas en el mundo. Brasil encabeza la lista con más de 2 millones de usuarios, seguido de China y Estados Unidos, lo que demuestra el atractivo universal de un Android libre y personalizable.




## Características principales



### Interface y la experiencia del usuario



**Android puro**: LineageOS ofrece una auténtica experiencia Android cercana a AOSP, sin superposiciones del fabricante ni aplicaciones superfluas. Interface sigue siendo familiar para los usuarios de Android al tiempo que ofrece una fluidez óptima gracias a la ausencia de bloatware.



**Libre de Google por defecto**: No hay servicios de Google preinstalados, por razones legales y éticas. Este enfoque "sin Google" garantiza un control total sobre tus datos personales y mejora el rendimiento al evitar los servicios que se ejecutan en segundo plano.



### Personalización y seguridad



**Personalización avanzada**: LineageOS desbloquea muchas opciones no disponibles en Android stock: reconfiguración de botones de navegación, temas de sistema personalizables, perfiles de uso adaptados a diferentes contextos (trabajo, personal, juegos).



**Outil Trust**: Funcionalidad integrada que supervisa el estado de seguridad de tu dispositivo y te alerta de posibles amenazas, proporcionando visibilidad en tiempo real de la seguridad de tu sistema.



**Actualizaciones extendidas**: La comunidad LineageOS se compromete a proporcionar parches de seguridad mensuales, permitiendo que los dispositivos descatalogados por sus fabricantes sigan recibiendo los últimos parches de seguridad de Android.



## Dispositivos compatibles



LineageOS es compatible con cientos de dispositivos de más de 20 fabricantes: Samsung, Xiaomi, OnePlus, Motorola, Sony, Google Pixel, Fairphone y muchos otros. Esta amplia compatibilidad es una de las principales ventajas del proyecto frente a alternativas como GrapheneOS, que se limitan a los dispositivos Pixel.



![devices-compatibility](assets/fr/02.webp)



*Página de dispositivos compatibles con LineageOS con filtros por fabricante*



![google-devices](assets/fr/03.webp)



*Dispositivos Google compatibles, incluido el Pixel 4 (nombre en clave "flame")*



### Dispositivos populares



Según las estadísticas oficiales, los modelos más utilizados incluyen una variedad de dispositivos que cubren diferentes rangos de precio y edad, lo que demuestra la capacidad de LineageOS para insuflar nueva vida a los smartphones más antiguos, así como para optimizar los más nuevos.



### Puntos cruciales antes de la instalación



**Desbloqueo del cargador de arranque**: Comprueba que tu fabricante/operador permite el desbloqueo. Algunas marcas, como Huawei, han suprimido esta posibilidad en modelos recientes, mientras que otras imponen procedimientos específicos.



**Modelo exacto**: Es crucial descargar la ROM que corresponde exactamente a tu dispositivo. Dos modelos con nombres comerciales similares pueden diferir técnicamente (Galaxy S10 vs S10 5G por ejemplo) y requerir imágenes diferentes.



**Soporte escalable**: Es posible que los dispositivos más nuevos no reciban soporte inmediato, ya que la portabilidad requiere que un desarrollador voluntario se encargue de ellos. A la inversa, el soporte puede cesar si el mantenedor de un dispositivo se retira del proyecto.



## Instalación



### Requisitos esenciales



⚠️ **¡Lea completamente estas instrucciones antes de empezar** para evitar cualquier problema!



**Volver al firmware de stock (si es necesario) :**




- Herramienta Flash Android**: Utiliza la herramienta oficial de Google [flash.android.com](https://flash.android.com) para restaurar fácilmente tu dispositivo Pixel a Android stock desde tu navegador web (se requiere Chrome/Edge)
- Alternativa**: Imágenes de fábrica manualmente desde [developers.google.com/android/images](https://developers.google.com/android/images)



**Pruebas previas obligatorias




- Arranca tu dispositivo al menos una vez** con el sistema original
- Prueba todas las funciones**: SMS, llamadas, Wi-Fi, datos móviles
- Importante**: Comprueba que puedes enviar/recibir SMS y hacer/recibir llamadas (incluyendo vía WiFi y 4G/5G). Si no funciona en el sistema original, ¡tampoco funcionará en LineageOS!
- Dispositivos recientes**: Algunos requieren el uso de VoLTE/VoWiFi al menos una vez en el sistema stock para aprovisionar IMS



**Preparación del sistema:**




- Elimina todas las cuentas de Google** de tu dispositivo para evitar la protección contra restablecimiento de fábrica, que puede bloquear la activación
- Copia de seguridad completa** : El proceso borrará completamente tu teléfono. Copia de seguridad de fotos, contactos, aplicaciones y archivos importantes



**Herramientas ADB y Fastboot:** Siga la [guía oficial de LineageOS](https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot) para instalar las herramientas de plataforma Android SDK. Verifique la instalación con `adb version` y `fastboot --version`.



**Configuración telefónica:**




- Activar **Opciones de desarrollador**: Ajustes > Acerca de > toca 7 veces "Número de compilación"



![android-version](assets/fr/06.webp)



*Accede a Ajustes > Acerca del teléfono para activar el modo desarrollador*





- Habilita **la depuración USB** en las opciones de desarrollador
- Activar **OEM Unlock** (imprescindible para desbloquear el bootloader)



![developer-options](assets/fr/07.webp)



*Activar las opciones de desarrollador, la depuración USB y el desbloqueo OEM*



### Instalación detallada



⚠️ **Estas instrucciones son específicas para LineageOS 22.2. Sigue cada paso con precisión. ¡No sigas adelante si algo falla!



#### Paso 1: Comprobación del firmware



**Firmware requerido**: Tu dispositivo debe tener Android 13 instalado antes de continuar (para Pixel 4). Firmware se refiere a las imágenes específicas del dispositivo incluidas en el sistema de stock.



![pixel4-info](assets/fr/04.webp)



*Página oficial de Pixel 4 con enlaces de descarga y guías de instalación*



![downloads-page](assets/fr/05.webp)



*Página y archivos de descarga de la compilación de LineageOS*



**Descargas específicas de Pixel 4:**




- Construye LineageOS**: [download.lineageos.org/devices/flame/builds](https://download.lineageos.org/devices/flame/builds)
- Archivos necesarios**: Descargue los 3 archivos necesarios de esta página (se utilizarán en los pasos siguientes):
  - `lineage-22.2-YYYMMDD-nightly-flame-signed.zip` (ROM principal)
  - dtbo.img` (árbol de particiones blob)
  - `boot.img` (recuperación LineageOS)



⚠️ **Importante**: Comprueba la versión de Android, no la versión del SO del fabricante. Estar en una ROM personalizada (incluso LineageOS) no garantiza que se cumpla este requisito.



💡 **Consejo**: Si tienes dudas sobre tu firmware, ¡vuelve al sistema stock antes de continuar!



#### Paso 2: Desbloquear el bootloader



⚠️ **¡Este paso borra todos tus datos!





- Prueba la conexión ADB**: Conecta tu dispositivo vía USB y prueba con el comando `adb devices` desde el terminal de tu ordenador



![adb-devices](assets/fr/08.webp)



*Comprueba la conexión ADB con el comando `adb devices`*





- Autorizar conexión** en tu teléfono



![usb-debugging-auth](assets/fr/09.webp)



*Depuración USB habilitada con la huella digital RSA del ordenador*





- Arrancar en modo cargador de arranque** :


```
adb -d reboot bootloader
```


O mantén pulsado **Volumen Abajo + Encendido** para apagar el dispositivo





- Comprueba la conexión fastboot**:


```
fastboot devices
```



![fastboot-mode](assets/fr/10.webp)



*Comandos Fastboot en terminal para comprobar la conexión*



![bootloader-screen](assets/fr/11.webp)



*Pantalla fastboot del Pixel 4 con información del sistema*





- Desbloquear el cargador de arranque** :


```
fastboot flashing unlock
```


En el dispositivo, utilice las teclas de volumen para navegar y pulse el botón **Power** para seleccionar "Desbloquear el gestor de arranque" y confirmar la operación



![unlock-bootloader](assets/fr/12.webp)



*Confirmación del desbloqueo del cargador de arranque en el dispositivo*



⚠️ **El teléfono se reiniciará automáticamente** tras la confirmación del desbloqueo





- Tras el reinicio automático**, vuelve a activar la depuración USB en las opciones de desarrollador




#### Paso 3: Flashear particiones adicionales



⚠️ **Necesario para que la recuperación funcione correctamente**





- Reiniciar bootloader**: Bajar volumen + Encendido
- Flash** (sustituya `/ruta/a/` por la carpeta en la que descargó el archivo) :


```
fastboot flash dtbo /chemin/vers/dtbo.img
```



![flash-partitions](assets/fr/13.webp)



*Flasheo de las particiones dtbo y boot.img mediante fastboot*



#### Paso 4: Instalar LineageOS recovery





- Flash recovery** (sustituya `/ruta/a/` por la carpeta en la que descargó el archivo) :


```
fastboot flash boot /chemin/vers/boot.img
```




- Reiniciar en recuperación** para comprobar



#### Paso 5: Instalación de LineageOS





- Reiniciar en recuperación**: Bajar volumen + Encendido → Modo recuperación



![recovery-mode](assets/fr/14.webp)



*Interface desde LineageOS recovery con menú principal*





- Restablecimiento de fábrica** : Escriba "Factory Reset" → "Format data / factory reset"



![factory-reset](assets/fr/15.webp)



*Proceso de restablecimiento de fábrica en LineageOS* recovery





- Volver al menú principal**
- Sideload LineageOS** :
   - En el dispositivo: "Aplicar actualización" → "Aplicar desde ADB"
   - En PC: `adb -d sideload /path/to/lineageos.zip`



![apply-update](assets/fr/16.webp)



*Seleccione "Aplicar actualización" y luego "Aplicar desde ADB" en recovery*



![sideload-process](assets/fr/17.webp)



*Instalación de LineageOS en curso vía sideload*



![sideload-terminal](assets/fr/18.webp)



*Comando Sideload en terminal con progreso de instalación*



💡 **Normal**: El proceso puede detenerse al 47% o mostrar errores de "Éxito", ¡es normal!



#### Paso 6: Primera puesta en marcha





- Reiniciar**: "Reiniciar el sistema ahora"
- Primer arranque**: Puede tardar hasta 15 minutos



🎉 **¡Instalación completada!**



### Puntos de atención



⚠️ **Atención**: LineageOS se proporciona "tal cual" sin garantía. Aunque hacemos todo lo posible para asegurarnos de que todo funciona, ¡instálalo bajo tu propia responsabilidad!



**Comprobaciones críticas:**




- Compatibilidad con firmware**: Asegúrate de comprobar la versión de firmware necesaria en la página de descargas de tu modelo
- No volver a bloquear** el gestor de arranque después de instalar LineageOS
- Siga las instrucciones específicas** para su dispositivo



## Configuración y aplicaciones



### Primera puesta en marcha


Interface racionalizado, cercano a Android de serie, sin Google. Configuración sencilla: idioma, Wi-Fi, sin necesidad de cuenta.



### Aplicaciones alternativas



**Fuentes de aplicación seguras:**



**F-Droid** : La tienda de aplicaciones de código abierto de referencia, preinstalada con LineageOS para microG o descargable directamente. F-Droid ofrece únicamente software de código abierto verificado y compilado de forma transparente, lo que garantiza la ausencia de rastreadores o componentes maliciosos.



**Aurora Store**: Cliente anónimo para acceder a Google Play Store sin una cuenta de Google. Aurora toma prestadas cuentas anónimas compartidas, lo que te permite descargar las principales apps preservando tu privacidad.



**Aplicaciones alternativas esenciales:**





- Navegación**: Organic Maps (mapas offline basados en OpenStreetMap)
- Comunicación**: Signal (mensajes cifrados de extremo a extremo), K-9 Mail (cliente de correo electrónico gratuito)
- Medios de comunicación**: NewPipe (YouTube sin publicidad ni seguimiento), VLC (reproductor multimedia universal)
- Productividad**: Nextcloud (nube de autoalojamiento), Simple Calendar (sincronización CalDAV)
- Seguridad**: Bitwarden (gestor de contraseñas), Aegis Authenticator (códigos 2FA)



Estas aplicaciones, la mayoría de las cuales están disponibles a través de F-Droid, forman un ecosistema coherente que puede sustituir por completo a los servicios de Google al tiempo que ofrece una experiencia de usuario moderna y funcional.



## Uso y mantenimiento



### Experiencia diaria



LineageOS transforma la experiencia Android, dando prioridad a la fluidez y la capacidad de respuesta. El aerodinámico Interface es especialmente eficaz en dispositivos antiguos, a los que da una nueva vida, con un rendimiento generalmente superior al de las ROMs de fabricante gracias a la ausencia de pesadas superposiciones y procesos superfluos.



Las funciones básicas (llamadas, SMS, fotos, navegación) funcionan a la perfección, mientras que las herramientas de personalización permiten ajustar el sistema a las preferencias individuales sin comprometer la estabilidad.



### Sistema de actualización OTA



LineageOS cuenta con un sistema de actualizaciones Over-The-Air especialmente fácil de usar. Las nuevas versiones se proponen automáticamente a través de notificaciones, y la instalación se realiza en unos pocos clics, sin necesidad de intervención técnica compleja. El proceso preserva por completo los datos y aplicaciones instalados.



Estas actualizaciones periódicas son una gran ventaja, especialmente para los dispositivos que han sido descatalogados por sus fabricantes, que pueden seguir beneficiándose de los últimos parches de seguridad de Android.



### Buenas prácticas recomendadas



**Seguridad postinstalación:**




- Establece un PIN o una contraseña segura para el desbloqueo
- Compruebe que el cifrado del almacenamiento está activado (normalmente por defecto)
- Instalar un gestor de contraseñas como Bitwarden a través de F-Droid



**Mantenimiento preventivo:**




- Actualizaciones OTA periódicas de seguridad
- Limitar la instalación de aplicaciones a fuentes de confianza (F-Droid, Aurora Store)
- Revisar periódicamente los permisos concedidos a las aplicaciones
- Los reinicios ocasionales optimizan el rendimiento y liberan memoria



## Ventajas y limitaciones



✅ **Beneficios:**




- Privacidad por defecto (sin seguimiento de Google)
- Amplia compatibilidad (más de 300 modelos)
- Rendimiento superior (sin bloatware)
- Actualizaciones ampliadas en dispositivos antiguos



❌ **Limitaciones:**




- Instalación técnica
- Sin Android Auto/Google Pay
- Las aplicaciones bancarias pueden ser problemáticas



## GrapheneOS vs LineageOS: ¿Cuál es la diferencia?



### Enfoques distintos



**GrapheneOS** se centra exclusivamente en la máxima seguridad, y se ejecuta sólo en los Google Pixel para explotar sus chips de seguridad dedicados. El sistema incorpora numerosas mitigaciones avanzadas contra exploits y refuerza considerablemente el sandboxing de aplicaciones.



**LineageOS** equilibra seguridad, privacidad y comodidad en el mayor número posible de dispositivos. El enfoque es más pragmático, con el objetivo de ampliar la compatibilidad en lugar de la seguridad absoluta.



### Gestión de los servicios de Google



**GrapheneOS**: Ofrece un sistema sandboxed Google Play opcional. Google Play puede instalarse pero se ejecuta en un sandbox estricto, sin privilegios especiales del sistema. Este enfoque único permite utilizar el ecosistema de Google manteniendo un estricto control de la seguridad.



**LineageOS**: Permite al usuario elegir entre instalar los servicios de Google (GApps), microG (alternativa libre), o permanecer totalmente libre de Google. Máxima flexibilidad para adaptarse a sus necesidades.



### Comparación técnica




| **Aspecto** | **GrapheneOS** | **LineageOS** |
|------------|----------------|---------------|
| **Compatibilidad** | Solo Pixels | Cientos de dispositivos |
| **Seguridad** | Mitigaciones avanzadas | Seguridad AOSP estándar |
| **Google Play** | Aislamiento opcional | Instalación clásica posible |
| **Instalación** | Interfaz web + USB | Procedimiento manual técnico |
| **Filosofía** | Seguridad ante todo | Balance y libertad de elección |

### Recomendaciones de uso



**Elige GrapheneOS** si tienes un Pixel, si la máxima seguridad es tu máxima prioridad y si aceptas limitaciones para una protección mejorada.



**Id a por LineageOS** si tenéis un dispositivo que no sea Pixel, buscáis un buen equilibrio entre privacidad y practicidad, o queréis libertad para elegir vuestro nivel de compromiso con el ecosistema Google.



## Conclusión



LineageOS ofrece una alternativa madura para recuperar el control de tu smartphone Android. Experiencia desenfadada, rendimiento óptimo, amplia compatibilidad: la opción ideal para combinar privacidad y practicidad en el día a día.



## Recursos



### Documentación oficial




- [Sitio web oficial de LineageOS](https://lineageos.org)
- [LineageOS Wiki](https://wiki.lineageos.org) - Guías de instalación por modelo
- [LineageOS para microG](https://lineage.microg.org) - Versión con microG integrado



### Comunidad




- [Subreddit r/LineageOS](https://reddit.com/r/LineageOS)
- [Mastodon cuenta @LineageOS](https://fosstodon.org/@LineageOS)



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1