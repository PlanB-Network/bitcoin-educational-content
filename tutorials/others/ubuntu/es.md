---
name: Ubuntu
description: Guía completa para instalar y utilizar Ubuntu como alternativa a Windows
---
![cover](assets/cover.webp)

## Introducción

Un sistema operativo (SO) es el software principal que gestiona todos los recursos de tu ordenador. Elegir un sistema operativo alternativo como Ubuntu puede ofrecer muchas ventajas en términos de seguridad, coste y privacidad.

### ¿Por qué Ubuntu?


- Mayor seguridad** : Las distribuciones Linux son famosas por su seguridad y robustez
- Coste cero**: Ubuntu y la mayoría de las distribuciones de Linux son gratuitas
- Gran comunidad**: Una comunidad de usuarios dispuestos a ayudar a través de foros y tutoriales
- Respeto de la intimidad**: Sistema de código abierto para una mayor transparencia
- Sencillez**: Interfaz sencilla y fácil de usar
- Rico ecosistema** : Amplio catálogo de software de código abierto
- Asistencia periódica**: Actualizaciones seguras de Canonical

## Instalación y configuración

### 1. Requisitos previos

**Equipo necesario:**


- Una memoria USB de al menos 12 GB
- Un ordenador con al menos 25 GB disponibles

### 2. Descargar


- Ir a [ubuntu.com/download](https://ubuntu.com/download)
- Elija la versión estable (se recomienda LTS)
- Descargar imagen ISO

![Page de téléchargement Ubuntu](assets/fr/01.webp)

![Sélection de la version Ubuntu](assets/fr/02.webp)

### 3. Crear una llave USB de arranque

Puede utilizar varias herramientas, como Balena Etcher :


- Descargar e instalar [Balena Etcher](https://etcher.balena.io/)

![Page de téléchargement Balena Etcher](assets/fr/03.webp)

![Installation de Balena Etcher](assets/fr/04.webp)


- Abra Balena Etcher y seleccione la imagen ISO de Ubuntu
- Seleccione la llave USB como medio de destino
- Haga clic en Flash y espere a que termine el proceso

![Utilisation de Balena Etcher](assets/fr/05.webp)

### 4. Instalación y seguridad de Ubuntu

**4.1 Arranque desde una memoria USB** (en francés)


- Apagar el ordenador
- Conecte la llave USB (que contiene Ubuntu)
- Encienda el ordenador. En los PC recientes, el sistema debería reconocer automáticamente la llave de arranque USB. Si no es así, reinicia manteniendo pulsada la tecla de acceso a la BIOS/UEFI (normalmente F2, F12 o Supr, según la marca)
 - En el menú BIOS/UEFI, selecciona tu llave USB como dispositivo de arranque
 - Guardar y reiniciar

**4.2 Inicio de la instalación** (en francés)

**Pantalla de inicio**

Al arrancar desde la llave USB, verás esta pantalla, que te permite iniciar Ubuntu.

![Écran de démarrage Ubuntu](assets/fr/06.webp)

**Elección de lengua

Elige el idioma que prefieras para la instalación y el sistema.

![Sélection de la langue](assets/fr/07.webp)

**Opciones de accesibilidad

Configure las opciones de accesibilidad si es necesario (lector de pantalla, alto contraste, etc.).

![Options d'accessibilité](assets/fr/08.webp)

**Configuración del teclado

Seleccione la distribución de su teclado. Dispone de un campo de prueba para comprobar que las teclas corresponden a su configuración.

![Configuration du clavier](assets/fr/09.webp)

**Conexión a la red**

Conéctese a su red Wi-Fi o por cable para descargar las actualizaciones durante la instalación.

![Configuration réseau](assets/fr/10.webp)

**Tipo de instalación

Elija entre "Probar Ubuntu" (para probar sin instalar) o "Instalar Ubuntu".

![Choix du type d'installation](assets/fr/11.webp)

**Método de instalación

Seleccione la instalación interactiva.

![Mode d'installation](assets/fr/12.webp)

**Selección de aplicaciones

Elija entre la instalación por defecto o una selección ampliada de aplicaciones.

![Sélection des applications](assets/fr/13.webp)

**Aplicaciones de terceros

Decida si instala o no controladores adicionales y software propietario.

![Installation applications tierces](assets/fr/14.webp)

**Tipo de partición

Tienes dos opciones principales:


- "Borrar disco e instalar Ubuntu": utiliza todo el disco para Ubuntu
- " Instalación manual: crea un arranque dual con Windows o personaliza tus particiones

![Choix du partitionnement](assets/fr/15.webp)

**Creación de una cuenta de usuario

Establezca su nombre de usuario y contraseña para su cuenta de Ubuntu.

![Création du compte](assets/fr/16.webp)

**Zona horaria

Seleccione su zona geográfica para ajustar la hora del sistema.

![Sélection du fuseau horaire](assets/fr/17.webp)

**Resumen de la instalación**

Compruebe todas sus opciones antes de iniciar la instalación final. Una vez que haga clic en "Instalar", comenzará el proceso.

![Résumé de l'installation](assets/fr/18.webp)

**4.3 Actualización de Ubuntu tras la instalación** (en francés)

Actualizar el sistema es un paso importante tras una nueva instalación. Tiene dos opciones:

**Opción 1: A través de la interfaz gráfica de usuario**


- Busque "Software y actualizaciones" en el menú de aplicaciones
- La aplicación comprobará automáticamente si hay actualizaciones disponibles
- Siga las instrucciones en pantalla para instalar las actualizaciones

**Opción 2: Vía Terminal


- Abrir Terminal (Ctrl + Alt + T)
- Escriba el siguiente comando para comprobar si hay actualizaciones disponibles:

```bash
sudo apt update
```


- Introduzca su contraseña cuando se le solicite
- Para instalar actualizaciones, escriba :

```bash
sudo apt upgrade
```


- Confirme la instalación tecleando 'Y' y luego Enter

### 5. Descubrir las tareas básicas

**5.1 Navegar por Internet

Por defecto, a menudo encontrarás Firefox en la barra de inicio.

Abre Firefox y empieza a navegar.

Otros navegadores (Chrome, Brave, etc.) pueden instalarse a través del Gestor de Software o mediante paquetes .deb.

**5.2 Tratamiento de textos

Ubuntu incluye la suite LibreOffice (Writer para el tratamiento de textos).

Para abrirlo: Actividades > Buscar "LibreOffice Writer" o haga clic en el icono si aparece en la barra.

Puedes crear, editar y guardar documentos en diversos formatos (incluido .docx).

**5.3 Instalación de aplicaciones

Gestor de software (llamado "Ubuntu Software"): interfaz gráfica para buscar e instalar aplicaciones.

Desde Terminal, utilice el comando :

```bash
sudo apt install nom-du-paquet
```

Ejemplo:

```bash
sudo apt install vlc
```

### 6. Conclusión y recursos adicionales

Ahora ya estás listo para usar Ubuntu a diario: protege tu sistema, navega, realiza trabajos de oficina, instala software y mantén tu sistema operativo actualizado

Para llevar la seguridad de tu vida digital un paso más allá, te recomendamos que eches un vistazo a nuestro servicio de mensajería cifrada, que se adapta perfectamente a la protección de tu privacidad y complementa tu instalación de Ubuntu:

https://planb.network/tutorials/others/proton-mail