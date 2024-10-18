---
name: Public Pool
description: Introduction to Public Pool
---

![signup](assets/cover.webp)

**Public Pool** is not just any pool; it's what's also known as a **Solo Pool**. If your miner succeeds in mining a block, then you collect the entire block reward, which is not shared with other participants of the pool or with the pool itself.

**Public Pool** solely provides a **block template** for your miner so that it can perform its task without you needing to have a **Bitcoin node** and the software that communicates with your miner. Since you are not pooling your computing power with that of other participants, your chances of successfully mining a block are obviously very low, resembling somewhat of a lottery system, where sometimes a lucky individual wins the jackpot.

![signup](assets/1.webp)

On the **Dashboard** of **Public Pool**, you still have some statistics like the pool's **Total Hashrate** as well as a distribution of the different types of miners that are connected to the pool.

![signup](assets/2.webp)

In the first few lines, we can see **Bitaxe** with 1323 **Bitaxe** connected for a total of 649TH/s. **Bitaxe** is an **Open source** project that allows for the simple reuse of a chip from an **ASIC** like the **Antminer S19** on an **opensource** electronic board to make a tiny miner of 0.5TH/s for 15W. This is the miner we will use as an example for this tutorial.

## Adding a **Worker** 👷‍♂️

![signup](assets/cover.webp)

At the top of the page, you can copy the pool address **stratum+tcp://public-pool.io:21496**.

Next, for the **user** field, enter a **Bitcoin** address that you own.

If you have multiple miners, you can enter the same address for all of them so that their **hashrates** are combined and appear as a single miner. You can also distinguish them by adding a distinct name to each. To do this, simply add **.workername** after the **Bitcoin** address.

Finally, for the **password** field, use **‘x’**.

Example: If your **Bitcoin** address is **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’** and you wish to name your miner **« Brrrr »**, then you would enter the following information in your miner's interface:

- **URL**: stratum+tcp://public-pool.io:21496
- **USER**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Password**: **‘x’**
If your miner is a **Bitaxe**, the fields are a bit different, but the information remains the same:
- **URL**: public-pool.io (here, you need to remove the part at the beginning **‘stratum+tcp://’** and the part at the end **‘:21496’** which will be reported in the port field)
- **Port**: 21496
- **User**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Password**: **‘x’**

![signup](assets/3.webp)

A few minutes after you start mining, you will be able to see your data on the **Public Pool** website by searching for your address.

## Dashboard

![signup](assets/4.webp)

Once you are connected to **Public Pool**, you can access your **Dashboard** by searching with your **Bitcoin** address that you entered in the **User** field. In our case here, it is **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’**.

On the **Dashboard**, different information is displayed both about your data and about the network.

![signup](assets/5.webp)

You have **Network Hash Rate** which corresponds to the total working power of the **Bitcoin** network.

The **Network Difficulty** indicates the difficulty that must be reached to validate a block.

And **Your Best Difficulty** is the highest difficulty you have reached. If, by chance 🍀, you reach the network difficulty, then you win the entire block reward... after 100 blocks. You would have to wait 100 blocks before being able to spend them.

You also have the **Block Height** which is the number of the last block that was mined as well as its weight expressed in WU, the maximum being 4,000,000.

Below, you can see all the stats of each of your devices individually if you have given them a distinct name by adding **.name** behind your **Bitcoin** address in the **User** field.