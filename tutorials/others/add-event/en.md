---
name: Add an event on PlanB Network
description: How do I suggest adding a new event on PlanB Network?
---
![event](assets/cover.webp)

PlanB's mission is to provide top-tier educational resources on Bitcoin in as many languages as possible. All content published on the site is open-source and hosted on GitHub, offering anyone the opportunity to contribute to the enrichment of the platform.

If you want to add a Bitcoin conference to the PlanB Network site and increase visibility for your event, but don't know how? This tutorial is for you!
![event](assets/01.webp)
- First, you need to have an account on GitHub. If you don't know how to create an account, we have made a detailed tutorial to guide you.

https://planb.network/tutorials/others/create-github-account


- Go to [the GitHub repository of PlanB dedicated to data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) in the `resources/conference/` section:
![event](assets/02.webp)
- Click on the top right on the `Add file` button, then on `Create new file`:
![event](assets/03.webp)
- If you have never contributed to the contents of PlanB Network before, you will need to create your fork of the original repository. Forking a repository means creating a copy of that repository on your own GitHub account, allowing you to work on the project without affecting the original repository. Click on the `Fork this repository` button:
![event](assets/04.webp)
- You will then arrive at the GitHub editing page:
![event](assets/05.webp)
- Create a folder for your conference. To do this, in the `Name your file...` box, write the name of your conference in lowercase with dashes instead of spaces. For example, if your conference is called "Paris Bitcoin Conference", you should note `paris-bitcoin-conference`. Also add the year of your conference, for example: `paris-bitcoin-conference-2024`:
![event](assets/06.webp)
- To validate the creation of the folder, simply note a slash after your name in the same box, for example: `paris-bitcoin-conference-2024/`. Adding a slash automatically creates a folder rather than a file:
![event](assets/07.webp)
- In this folder, you will create a first YAML file named `events.yml`:
![event](assets/08.webp)
- Fill this file with information about your conference using this template:

```yaml
- start_date:
  end_date:
  address_line_1:
  address_line_2: 
  address_line_3: 
  name:
  builder:
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description:
  language: 
    - 
  links:
    website:
    replay_url:    
    live_url :
  tags: 
    - 
```

For example, your YAML file could look like this:

```yaml
- start_date: 2024-08-15
  end_date: 2024-08-18
  address_line_1: Paris, France
  address_line_2: 
  address_line_3: 
  name: Paris Bitcoin Conference 2024
  builder: Paris Bitcoin Conference
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description: The largest Bitcoin conference in France with over 8,000 participants each year!
  language: 
    - fr
    - en
    - es
    - it
  links:
    website: https://paris.bitcoin.fr/conference
    replay_url:
    live_url :
  tags: 
    - Bitcoiner
    - General
    - International
```
![event](assets/09.webp)
If you do not yet have a "*builder*" identifier for your organization, you can add it by following this other tutorial.

https://planb.network/tutorials/others/add-builder



- Once you have finished making changes to this file, save them by clicking on the `Commit changes...` button:
![event](assets/10.webp)
- Add a title for your changes, as well as a short description:
![event](assets/11.webp)
- Click on the green `Propose changes` button:
![event](assets/12.webp)
- You will then arrive at a page summarizing all your changes:
![event](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![event](assets/14.webp)
- Select your fork of the PlanB Network repository:
![event](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It's probably called `patch-1`. Click on it:
![event](assets/16.webp)
- You are now on your working branch:
![event](assets/17.webp)
- Go back to the `resources/conference/` folder and select the folder of your conference that you just created in the previous commit:
![event](assets/18.webp)
- In the folder of your conference, click on the `Add file` button, then on `Create new file`:
![event](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![event](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`:
![event](assets/21.webp)
- Click on the `Commit changes...` button:
![event](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![event](assets/23.webp)
- Return to the `assets` folder:
![event](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`: ![event](assets/25.webp)
- A new page will open. Drag and drop an image that represents your conference and will be displayed on the PlanB Network site:
![event](assets/26.webp)
- It can be the logo, a thumbnail, or even a poster:
![event](assets/27.webp)
- Once the image is uploaded, check that the `Commit directly to the patch-1 branch` box is ticked, then click on `Commit changes`:
![event](assets/28.webp)
- Be careful, your image must be named `thumbnail` and must be in `.webp` format. The full file name should therefore be: `thumbnail.webp`:
![event](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`:
![event](assets/30.webp)
- Once on the file, click on the 3 small dots at the top right then on `Delete file`:
![event](assets/31.webp)
- Verify that you are still on the same working branch, then click on the `Commit changes` button:
![event](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`:
![event](assets/33.webp)
- Go back to the root of your repository:
![event](assets/34.webp)
- You should see a message indicating that your branch has undergone changes. Click on the `Compare & pull request` button:
![event](assets/35.webp)
- Add a clear title and a description to your PR:
![event](assets/36.webp)
- Click on the `Create pull request` button:
![event](assets/37.webp)
Congratulations! Your PR has been successfully created. An administrator will now check it and, if everything is in order, merge it into the main repository of PlanB Network. You should see your event appear on the website a few days later.

Be sure to follow the progress of your PR. An administrator may leave a comment asking for additional information. As long as your PR is not validated, you can consult it in the `Pull requests` tab on the PlanB Network GitHub repository:
![event](assets/38.webp)
Thank you very much for your valuable contribution! :)

