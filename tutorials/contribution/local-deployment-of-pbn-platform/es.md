---
name: Guía para ejecutar localmente la plataforma Plan ₿ Academy
description: ¿Cómo se puede ejecutar Plan ₿ Academy en un entorno local para probar mi aportación de contenidos o la corrección/revisión de contenidos educativos en Plan ₿ Academy?
---
![github](assets/cover.webp)

## En resumen

Este tutorial proporciona instrucciones paso a paso para configurar el Sistema de Gestión de Aprendizaje Bitcoin desde Plan ₿ Academy en tu máquina local utilizando Docker, claves falsas y configuraciones de repositorio personalizadas.

Si no has entendido la parte de arriba, no te preocupes: ¡este tutorial es para ti!

---
## **Cómo ejecutar localmente el sistema de gestión del aprendizaje Bitcoin**

Este tutorial proporciona pasos detallados para configurar la plataforma, manejar claves falsas y personalizar repositorios. Sigue estos pasos para evitar problemas comunes y configurar correctamente tu entorno local.

**1. Requisitos previos**

- Máquina Linux con Docker y Docker Compose instalados (se ha informado de que también funciona en Windows).
- Versión suficiente de `nodejs` (probado: 22.12.0)
- `pnpm` instalado en su sistema.
- Git configurado para clonar repositorios.

**2. Clonar el repositorio**

Clona el repositorio en tu máquina local:

git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-sistema de gestión del aprendizaje

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3. Configurar variables de entorno**

1\. Duplica el archivo `.env.example`:

```bash
cp .env.example .env
```

1. Edita el fichero `.env`, borrando la parte .example del nombre, ahora tendrás que incluir claves ficticias para las variables requeridas. Ejemplo:

⚠️ Este es un paso obligatorio, saltárselo dará lugar a errores como la denegación de conexión entre algunos de los contenedores.

No olvides añadir también tu PAT de Github en el archivo

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4. Instalar dependencias**

Asegúrate de tener instalada una versión adecuada de nodejs. A partir de 2024-12, se ha comprobado que funciona la v22.12.0 (LTS).

⚠️ Ubuntu 22.04 repositorio nodejs versión es 12.22.9: demasiado viejo para permitir instalar pnpm

Para instalar nodejs, encuentra las instrucciones [aquí](https://nodejs.org/en/download/package-manager); por ejemplo, puedes optar por utilizar el método de instalación `nvm`.

---
Antes de iniciar la fase de instalación pnpm de los paquetes necesarios, asegúrate de tener todas las dependencias instaladas, puedes lograrlo ejecutando el siguiente comando:

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
Dentro de la carpeta `../Bitcoin-learning-management-system/`, ejecuta el siguiente comando para instalar `pnpm`

```bash
pnpm install
```

__TIP:__ Recuerda actualizar de vez en cuando tanto las dependencias como el propio pnpm

**5. Ejecutar los contenedores**

Dentro de tu carpeta `../Bitcoin-learning-management-system/`, inicia el entorno de desarrollo con Docker:

```bash
docker compose up --build -V
```

Si también ejecutas el siguiente comando de esta forma, no verás los registros en tu terminal.

```bash
docker compose up -d --build -V
```

Esto construirá e iniciará todos los contenedores necesarios desde dockers.

**6. Acceso a la aplicación**

Una vez que los contenedores estén funcionando, accede al frontend en:

\[<http://localhost:8181](http://localhost:8181)>

![Plan ₿ Academy Local](assets/en/1.webp)

Nota: la aplicación se recargará automáticamente si cambias algún archivo fuente.

**7.** Configura tu base de datos Schema

En la primera ejecución, deberás ejecutar las migraciones de BD.

Para ello, ejecute el script de migración: `pnpm run dev:db:migrate`

```markdown
pnpm run dev:db:migrate
```

**8. Importar datos del repositorio**

Para importar datos a la base de datos, realice una solicitud a la API:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9. Solucionar problemas de acceso al volumen de sincronización**

Si tienes problemas de acceso a los volúmenes `cdn` y `sync`, ejecuta:

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

Entonces otra vez:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Academy Local](assets/en/2.webp)

**10. Personalizar el repositorio (opcional)**

Si necesitas utilizar un Fork o una rama específica:

1. Edita el archivo `.env` para actualizar las siguientes variables:

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\. Reinicia Docker:

```markdown
docker compose down -v
docker compose up --build -V
```

3\. Vuelve a sincronizar los datos del repositorio:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

Este tutorial asegura que la plataforma está correctamente configurada con claves ficticias, dependencias instaladas y repositorios personalizados según sea necesario. ¡Buena suerte con tu configuración!

**Comandos para ayuda extra**

Detener todos los contenedores

```
docker compose down
```

Podar todos los contenedores y volúmenes existentes

```
docker container prune -f
docker volume prune --all
```

Vuelve a crear los contenedores con el mismo comando utilizado en la guía oficial y lanza el script de sincronización:

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
