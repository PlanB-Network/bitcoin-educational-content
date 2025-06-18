---
name: Guía para ejecutar localmente la plataforma Plan ₿ Network
description: ¿Cómo se puede ejecutar Plan ₿ Network en un entorno local para probar mi aportación de contenidos o la corrección/revisión de contenidos educativos en Plan ₿ Network?
---
![github](assets/cover.webp)

## En resumen

Este tutorial proporciona instrucciones paso a paso para configurar el Sistema de Gestión de Aprendizaje Bitcoin desde Plan ₿ Network en su máquina local utilizando Docker, claves falsas y configuraciones de repositorio personalizadas.

Si no has entendido la parte de arriba, no te preocupes: ¡este tutorial es para ti!

---
## **Cómo ejecutar localmente el sistema de gestión del aprendizaje Bitcoin**

Este tutorial proporciona pasos detallados para configurar la plataforma, manejar claves falsas y personalizar repositorios. Sigue estos pasos para evitar problemas comunes y configurar correctamente tu entorno local.

**1. Requisitos previos**


- Máquina Linux con Docker y Docker Compose instalados (se ha informado de que también funciona en Windows).
- versión suficiente de `nodejs` (probado: 22.12.0)
- `pnpm` instalado en su sistema.
- Git configurado para clonar repositorios.

**2. Clonar el repositorio**

Clone el repositorio en su máquina local:

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

1. Edite el fichero `.env`, borrando la parte .example del nombre, ahora tiene que incluir claves ficticias para las variables requeridas. Ejemplo:

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

asegúrese de tener instalada una versión adecuada de nodejs. A partir de 2024-12, se ha comprobado que funciona la v22.12.0 (LTS).

⚠️ Ubuntu 22.04 repositorio nodejs versión es 12.22.9: demasiado viejo para permitir instalar pnpm

Para instalar nodejs, encuentre las instrucciones [aquí](https://nodejs.org/en/download/package-manager); por ejemplo, puede optar por utilizar el método de instalación `nvm`.

---
Antes de iniciar la fase de instalación pnpm de los paquetes necesarios, asegúrese de tener todas las dependencias instaladas, puede lograrlo ejecutando el siguiente comando:

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
Dentro de la carpeta `../Bitcoin-learning-management-system/`, ejecute el siguiente comando para instalar `pnpm`

```bash
pnpm install
```

__TIP:__ Recuerda actualizar de vez en cuando tanto las dependencias como el propio pnpm

**5. Ejecutar los contenedores**

Dentro de su carpeta `../Bitcoin-learning-management-system/`, inicie el entorno de desarrollo con Docker:

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

![Plan ₿ Network Local](assets/en/1.webp)

Nota: la aplicación se recargará automáticamente si cambias algún archivo fuente.

**7.** Configura tu base de datos Schema

En la primera ejecución, deberá ejecutar las migraciones de BD.

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

Si tiene problemas de acceso a los volúmenes `cdn` y `sync`, ejecute:

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

entonces otra vez:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)

**10. Personalizar el repositorio (opcional)**

Si necesita utilizar una Fork o una rama específica:

1. Edite el archivo `.env` para actualizar las siguientes variables:

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\. Reinicie Docker:

```markdown
docker compose down -v
docker compose up --build -V
```

3\. Vuelva a sincronizar los datos del repositorio:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

Este tutorial asegura que la plataforma está correctamente configurada con claves ficticias, dependencias instaladas y repositorios personalizados según sea necesario. ¡Buena suerte con tu configuración!

**Comandos para ayuda extra**

detener todos los contenedores

```
docker compose down
```

podar todos los contenedores y volúmenes existentes

```
docker container prune -f
docker volume prune --all
```

vuelva a crear los contenedores con el mismo comando utilizado en la guía oficial y el script de sincronización del almuerzo:

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
