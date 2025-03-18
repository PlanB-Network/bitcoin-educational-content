---
name: Guide to Running the Plan ₿ Network Plattform Locally
description: How can you run the Plan ₿ Network in a local environment to test my content contribution or proofreading/review of educational content on Plan ₿ Network?
---
![github](assets/cover.webp)

## In Summary

This tutorial provides step-by-step instructions for setting up the Bitcoin Learning Management System from Plan ₿ Network on your local machine using Docker, dummy keys, and custom repository configurations. 

If you didn’t understand the part above, don’t worry—this tutorial is for you!

---

## **How to Run Bitcoin Learning Management System Locally**

This tutorial provides detailed steps to set up the platform, handle dummy keys, and customize repositories. Follow the steps below to avoid common issues and properly configure your local environment.


**1. Prerequisites**  
- Linux machine with Docker and Docker Compose installed (it has been reported working on Windows too).  
- sufficient `nodejs` version (tested: 22.12.0)  
- `pnpm` installed on your system.  
- Git configured for cloning repositories.


**2. Clone the Repository**  
Clone the repository to your local machine:  
  
git clone [https://github.com/PlanB-Network/bitcoin-learning-management-system](https://github.com/PlanB-Network/bitcoin-learning-management-system￼cd)  
[cd](https://github.com/PlanB-Network/bitcoin-learning-management-system￼cd) bitcoin-learning-management-system

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

  
**3. Set Up Environment Variables**

 1\. Duplicate the `.env.example` file:

```bash
cp .env.example .env
```

1. Edit the `.env` file, deleting the .example part of the name, now you have to include dummy keys for required variables. Example:

   ⚠️ This is a mandatory step, skipping it will result in errors such connection refusal between some of the containers.

   Don't forget to add your dedicated Github PAT too in the file


   ```markdown
   # Dummy Keys for External Services
      SBP_API_KEY=dummyApiKey
      SBP_HMAC_SECRET=dummyHmacSecret
      STRIPE_SECRET=sk_test_dummySecretKey12345
      STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
      SENDGRID_KEY=dummySendgridKey
   ```

---

**4. Install Dependencies**

`Be sure` to have installed a suitable nodejs version. As of 2024-12, v22.12.0 (LTS) has been proven working.


   ⚠️ Ubuntu 22.04 repository nodejs version is 12.22.9: too old to allow you install pnpm


To install nodejs, find instructions [here](https://nodejs.org/en/download/package-manager); for example you may choose to use `nvm` installation method.

---

Before starting pnpm installing phase of necessary packages, be sure to have all dependencies installed, you can achieve this by running the following command:

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---

Inside your `../bitcoin-learning-management-system/` folder, run the following command to install `pnpm`

```bash
pnpm install
```

> [!TIP]
> Remember to update from time to time both dependencies and pnpm itself


**5. Run the Containers**  
Inside your `../bitcoin-learning-management-system/` folder, start the development environment with Docker:

```bash
docker compose up --build -V
```
You also run this next command this way, you won't see the logs in your terminal.
```bash
docker compose up -d --build -V
```

This will build and start all the necessary containers from dockers.

**6. Access the Application**  
Once the containers are running, access the frontend at:  
\[<http://localhost:8181](http://localhost:8181)>  

![Plan ₿ Network Local](assets/en/1.webp)

Note: that the app will automatically reload if you change any source files.


**7.** Set up your database schema

On the first run, you will need to run the DB migrations.

To do so, run the migration script : `pnpm run dev:db:migrate`

```markdown
pnpm run dev:db:migrate
```

**8. Import Data from the Repository**  
To import data into the database, make a request to the API:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9. Fix Sync Volume Access Issues**  
If you encounter access issues with the `cdn` and `sync` volumes, run:

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

then again:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)


**10. Customize the Repository (Optional)**  
If you need to use a fork or a specific branch:  
1. Edit the `.env` file to update the following variables:

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
   DATA_REPOSITORY_BRANCH=<your-branch>
   PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
   PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\. Restart Docker:

```markdown
docker compose down -v
docker compose up --build -V
```

3\. Re-sync the repository data:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

This tutorial ensures the platform is correctly set up with dummy keys, dependencies installed, and repositories customized as needed. 🎉 Good luck with your setup!

**Commands for extra help**  
  
stop all containers

```
docker compose down
```

prune all existing containers and volumes

```
docker container prune -f
docker volume prune --all	
```

recreate the containers with the same command used in the official guide and lunch sync script:

```
docker-compose up --build -V 
curl -X POST http://localhost:3000/api/github/sync
```
