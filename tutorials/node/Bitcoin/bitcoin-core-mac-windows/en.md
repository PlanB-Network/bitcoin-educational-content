---
builder: Arman The Parman

Tag:
  - node
  - privacy
  - infrastructure

difficulty: advanced
---

# Install Bitcoin Core on Mac or Windows

    The following guide was offerted by Parman (https://twitter.com/parman_the)
    you can tips him here; dandysack84@walletofsatoshi.com
    Original source; https://armantheparman.com/bitcoincore/

Installing Bitcoin Core on your regular computer can be done, but it’s not ideal. If you don’t mind leaving your computer on 24/7, then this will work fine. If you need to turn off the computer, it gets annoying waiting for the software to sync up each time you turn it back on.

These instructions are for Mac or Windows Users. Linux users won’t need my help most likely, but the instructions for Linux are very similar to Mac.

## Start Clean

Ideally, you want to use a clean computer, one with no malware. Even if you use a hardware wallet, malware can trick you out of your coins.

You can either wipe clean an old computer, and use it as a dedicated Bitcoin computer, or buy a dedicated computer/laptop.

## The Hard Drive

Bitcoin Core will take up about 400 gigabytes of data on your drive, and will continue to grow. You can use your internal drive, but you can also attach an external hard drive. I’ll explain both options. Ideally, you should use a solid-state drive. If you have an old computer, it probably doesn’t have one of these internally. Just buy a 1 or 2 terabyte external SSD and use that. The regular drive will probably work, but you might end up having issues and it will be much slower.

![image](assets\1.png)

## Download Bitcoin Core

Go to bitcoin.org (make sure you don’t go to bitcoin.com, which is a shitcoin site owned by Roger Ver, tricking people to buy Bitcoin Cash instead of Bitcoin)

Once there, it’s strangely not obvious where to get the software. Go to the resources menu and click “Bitcoin Core”, as shown below:

![image](assets\2.png)

This will bring you to the download page:

![image](assets\3.png)

Click the Download Bitcoin Core orange button:

![image](assets\4.png)

There are several options to choose from, depending on your computer. The first two are relevant to this guide; choose Windows or Mac on the left bar. It will begin downloading after you click it, most likely to your Downloads directory.

## Verify the download (part 1)

You need the file which contains the hashes of various releases. This file used to be on the downloads page of bitcoin.org, but now has moved to bitcoincore.org/en/download:

![image](assets\5.png)

You need the SHA256 binary hashes file. This file contains the SHA256 hashes of the various download packages of Bitcoin Core.

Next, we need to hash the Bitcoin Core download and compare it to what the file says the hash should be. Then we know the download is identical to what is expected, according to bitcoincore.org.

Navigate to the Downloads directory again and execute this command (replace X’s with the bitcoin core download file name exactly):

    FOR MAC —–> shasum -a 256 XXXXXXXXXXXX

    FOR WINDOWS —–> certutil -hashfile XXXXXXXXXXX SHA256

You will get a hash output. Make a note of it, and compare it to the hash contained in the SHA256SUMS file.

If the outputs are identical, then you have verified that no bit of data has been tampered with… almost. We still need to be sure the SHA256SUMS file is not malicious.

To proceed with the next step, we must have gpg installed on our computer.

To do that, see my SHA256/gpg guide, and scroll about halfway to the “Download gpg” section, and look for the subheading of your operating system. Then come back here.

## Get the Public Key

Back at the download page, get the SHA256 hash signatures file

![image](assets\6.png)

Click it and save the file to disk, preferably the Downloads directory.

This file contains signatures by various people, of the SHA256SUMS file.

We want the lead developer’s public key, Wladimir J. van der Laan on our computer’s keyring. His public key ID is:
1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964

Copy that text into the following command:

    gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964

Out of interest, at any time, you can see what keys are in the computer’s keyring with this command:

    gpg --list-keys

## Verify the download (part 2)

We have the public key, so we can now verify the SHA256SUMS file which contains the hashes of the Bitcoin Core download, and the signature for those hashes.

Open Terminal or CMD again, and make sure you are in the Downloads directory. From there, execute this command:

    gpg –verify SHA256SUMS.asc SHA256SUMS

The first listed file is the exact spelling of the signature file. The second listed file should be the exact spelling of the text file containing the hashes. Both files should be in the same directory and you need to be in the directory of the files, otherwise, you have to type out the full path for each file.

This is the output you should get

![image](assets\7.png)

It is safe to ignore the WARNING message – that just is reminding you that you haven’t met Wladimir at a key part and personally asked him what his public key was, and then told your computer to trust this key completely.

If you got this message, you now know that the SHA256SUMS.asc file has not been tampered with after Wladimir signed it.

## Install Bitcoin Core

You shouldn’t need detailed instructions on how to install the program.

![image](assets\8.png)

## Run Bitcoin Core

On a Mac, you might get a warning (Apple is still anti-Bitcoin)

![image](assets\9.png)

Click OK, and then open your System Preferences

![image](assets\10.png)

Click the Security and Privacy Icon:

![image](assets\11.png)

Then click “open anyway”:

![image](assets\12.png)

The error will appear again, but this time you’ll have an OPEN button available. Click it.

![image](assets\13.png)

Bitcoin Core should load and you’ll be presented with some options:

![image](assets\14.png)

Here you can choose to use the default pathway for where the blockchain will be downloaded to, or you can choose your external drive. I recommend no changing the default path if you are going to use the internal drive, it makes things easier to set up when you install other software to communicate with Bitcoin Core.

You can choose to run a pruned node, it saves space, but limits what you can do with your node. Either way, you’ll be downloading the entire blockchain and verifying it anyway, so if you have the space, keep what you downloaded, and don’t prune if you can avoid it.

Once you confirm, the blockchain will begin downloading. It will take many days.

![image](assets\15.png)

You can shut down the computer and come back to download if you want, it won’t do any damage.

    The following guide was offerted by Parman (https://twitter.com/parman_the)
    you can tips him here; dandysack84@walletofsatoshi.com
    Original source; https://armantheparman.com/bitcoincore/
