---
name: Profesor Plan ₿ Network
description: ¿Cómo añado o modifico mi perfil de profesor en Plan ₿ Network?
---
![cover](assets/cover.webp)

Si piensas contribuir a Plan ₿ Network escribiendo un nuevo tutorial o curso, necesitarás un perfil de profesor. Este perfil te permitirá recibir los créditos correspondientes por los contenidos que aportes a la plataforma.

Para aquellos de ustedes que ya han participado en la creación de contenidos educativos en Plan ₿ Network, probablemente ya tienen un perfil de profesor. Puedes encontrarlo en la carpeta `/professors` [en nuestro repositorio de GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors). Si tu perfil ya existe, encuentra tu nombre de usuario en el archivo `professor.yml`.

Para realizar cambios en tu perfil, ve a la sección "Editar tu perfil de profesor" al final de este tutorial.

## Añadir un nuevo profesor con nuestro software

La forma más sencilla de crear tu perfil de profesor en Plan ₿ Network es utilizar nuestra herramienta Python integrada. Así es como funciona.

### 1 - Configura tu entorno local

Debes tener tu propio Fork del [repositorio Plan ₿ Network en GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content).

Sincroniza la rama principal (`dev`) de tu Fork con el repositorio fuente.

Actualiza tu clon local.

```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```

### 2 - Crear una nueva sucursal

Asegúrate de que estás en la rama `dev`. Crea una nueva rama con un nombre descriptivo (por ejemplo, `add-professor-loic-morel`).

Publica esta rama en tu Fork en línea.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```

### 3 - Crea tu perfil de profesor

Ve a la carpeta `scripts/tutorial-related/data-creator/` en tu clon local. Asegúrate de haber instalado todas las dependencias necesarias para el software, habiendo instalado primero Python:

```bash
pip install -r requirements.txt
```

A continuación, inicia el software con el comando:

```bash
python3 main.py
```

Una vez en la página de inicio, introduce la ruta local al clon de tu repositorio, el idioma en el que estás escribiendo y tu ID de GitHub. Si estás creando este perfil para otra persona y ya tienes un perfil de Profesor, introduce tu ID en el campo "*PBN Professor's ID*". Si estás creando tu propio perfil, aún no tendrás un ID de Profesor, ya que estás en proceso de crear uno, así que deja este campo en blanco.

A continuación, haz clic en el botón "*Nuevo profesor*".

![Image](assets/fr/01.webp)

Rellena la información requerida (ten en cuenta que toda esta información será pública tanto en nuestra plataforma como en GitHub):


- Nombre de tu expediente de profesor (utiliza tu nombre y apellidos o un seudónimo, en minúsculas);
- Tu nombre o apodo;
- Tu sitio web y perfil X (opcional);
- Una dirección Lightning para recibir donativos de los lectores (opcional);
- Selecciona 2 o 3 etiquetas de la lista;
- Haz clic en "*Seleccionar imagen*" para elegir una imagen de perfil de tus carpetas locales (puedes utilizar cualquier nombre y formato para la imagen, y el software la adaptará automáticamente. Sólo asegúrate de que la imagen sea cuadrada);
- Escribe una breve descripción de tu perfil.

Finaliza la creación haciendo clic en "*Crear Profesor*". Esto automáticamente generará todos los archivos necesarios para tu perfil.

![Image](assets/fr/02.webp)

Guarda tus cambios localmente creando un commit con un mensaje explicativo. Sube los cambios a tu Fork GitHub.

```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```

Una vez terminado, crea una Pull Request (PR) en GitHub para proponer la integración de tus modificaciones. Añade un título y una breve descripción al PR.

### 4 - Corrección y fusión

Espera la validación o los comentarios de un administrador. Si es necesario, haz correcciones y envía nuevos commits.

```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```

Una vez fusionado el PR, puedes eliminar tu rama de trabajo.

## Modificar tu perfil de profesor

Si ya dominas el uso de Git, modifica tu perfil de profesor creando una nueva rama y editando el archivo correspondiente directamente en la carpeta existente. Los cambios pueden realizarse en el archivo `professor.yml` o en el archivo markdown, en función de la información que deba corregirse. Una vez que hayas hecho los cambios localmente, envíalos a tu Fork y envía un PR.

Para los principiantes, recomendamos hacer la modificación directamente a través de la interfaz web de GitHub. Asegúrate de tener una cuenta en GitHub. Si no sabes cómo crear una, sigue este tutorial:

https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Ve a [el repositorio GitHub de Plan ₿ Network dedicado a los datos](https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors).

![Image](assets/fr/03.webp)

Haz clic en la carpeta "*profesores*" y, a continuación, ve a tu carpeta personal.

![Image](assets/fr/04.webp)

Para cambiar los metadatos de tu perfil, como Lightning Address, tu nombre o los enlaces, selecciona el archivo "*professor.yml*". Para cambiar tu descripción, haz clic en el archivo YAML correspondiente a tu idioma (por ejemplo, "*en.yml*" o "*fr.yml*").

Si modificas tu descripción, recuerda eliminar todas las traducciones obsoletas. Entonces puedes encargarte de traducir tu descripción a los otros idiomas con la ayuda de un LLM, o dejar solo la descripción en tu idioma nativo y mencionar en tu Pull Request que tu descripción requiere traducción por parte de nuestro equipo.

![Image](assets/fr/05.webp)

Una vez sobre el archivo que deseas modificar, pulsa sobre el icono del lápiz.

![Image](assets/fr/06.webp)

Si aún no tienes un Fork del repositorio Plan ₿ Network, GitHub te sugerirá que crees uno. Haz clic en "*Fork este repositorio*".

![Image](assets/fr/07.webp)

Realiza los cambios deseados en el archivo. Cuando hayas terminado, haz clic en "*Commit changes*".

![Image](assets/fr/08.webp)

Introduce un mensaje que describa tu cambio y, a continuación, selecciona "*Proponer cambios*".

![Image](assets/fr/09.webp)

Aparecerá un resumen de tus cambios. Si deseas realizar más cambios en tu perfil, puedes volver a las carpetas y realizar más commits. Cuando hayas terminado, haz clic en "*Crear pull request*".

Una Pull Request es una solicitud hecha para integrar cambios de tu rama en la rama principal del repositorio Plan ₿ Network, permitiendo la revisión y discusión de los cambios antes de que sean fusionados.

![Image](assets/fr/10.webp)

Asegúrate, en la parte superior de la interfaz, de que tu rama de trabajo está fusionada con la rama `dev` del repositorio Plan ₿ Network (que es la rama principal).

Introduce un título que resuma brevemente los cambios que deseas fusionar con el repositorio fuente. Añade un breve comentario que describa estos cambios y, a continuación, haz clic en el botón verde "*Crear pull request*" para confirmar la pull request:

![Image](assets/fr/11.webp)

Tu PR será visible en la pestaña "*Pull Request*" del repositorio principal de Plan ₿ Network. Todo lo que tienes que hacer ahora es esperar a que un administrador fusione tu modificación.

![Image](assets/fr/12.webp)

Si encuentras alguna dificultad técnica al enviar tu cambio, no dudes en pedir ayuda en [nuestro grupo de Telegram dedicado a las contribuciones](https://t.me/PlanBNetwork_ContentBuilder). Muchas gracias
