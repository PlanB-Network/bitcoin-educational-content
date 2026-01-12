---
name: White Noise
description: A private, decentralized messaging application based on the Nostr and MLS protocols
---

![cover](assets/cover.webp)



## Introduction


"In the midst of difficulty lies opportunity". This quote from Albert Einstein reminds us that problems are not definitive, but contain within them the seeds of new, innovative solutions.


The motivations behind the launch of the solution we're presenting in this tutorial illustrate this perfectly. It's **White Noise**, born of necessity.


In the words of its founder, Max Hillebrand, reported by *Bitcoin Magazine*: "We launched this project for lack of alternatives." He explains that "existing encryption applications are inefficient on a large scale: adding 100 people to a group conversation slows down encryption considerably. Decentralized platforms, meanwhile, don't offer private messaging. Finally, Nostr's open relay network allows everyone to spread ideas, but the protection of direct messages remains dramatically inadequate. We realized: to protect freedom, we had to merge these systems."


## What is White Noise?


White Noise is an open source messaging application developed by a non-profit team. The application promotes security, privacy and decentralization. Unlike conventional applications, it requires neither a phone number nor an e-mail address.

White Noise is distinguished by the integration of two fundamental protocols - Nostr and MLS - which form its technical basis.


Nostr (Notes and Other Stuff Transmitted by Relays) is a decentralized, open-source protocol designed to resist censorship.  The protocol uses relays, key pairs and clients.


https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

With white Noise, you can even choose your own relay settings to maximize privacy.


MLS (Messaging Layer Security), on the other hand, is a security protocol that enables end-to-end encryption of messages. In other words, messages are accessible only at the endpoints, i.e. the sender and recipient of the message. This means that relays involved in routing messages cannot access their content.


Here's a quick comparison between White Noise and a number of the best-known messaging applications.




| Comparison points           | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| E2EE encryption / 1:1       | ✅ Yes        | Optional   | ✅ Yes            | ✅ Yes   | ✅ Yes    | ✅ Yes             | ✅ Yes  |
| Group E2EE encryption       | ✅ Yes        | ❌ No       | ✅ Yes            | ✅ Yes   | ✅ Yes    | Optional          | ✅ Yes  |
| Identity anonymization      | ✅ Yes        | Optional   | ❌ No             | ✅ Yes   | ❌ No     | ❌ No              | ❌ No   |
| Open source server          | ✅ Yes        | ❌ No       | ❌ No             | ✅ Yes   | ❌ No     | ❌ No              | ✅ Yes  |
| Open source client          | ✅ Yes        | ✅ Yes       | ❌ No             | ✅ Yes   | ❌ No     | ❌ No              | ✅ Yes  |
| Decentralized server        | ✅ Yes        | ❌ No       | ❌ No             | ✅ Yes   | ❌ No     | ❌ No              | ❌ No   |
| Year of creation            | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |

## Getting started with White Noise


### White Noise installation


Go to the [White Noise website](https://www.whitenoise.chat/), then click on **Download**.


![screen](assets/fr/03.webp)


White Noise is currently only available on mobile devices.

On the new interface that appears, press :



- the **Zapstore** or **Android APK** button if you want to download it on Android ;
- on the **iOS TestFlight** button if you're using an iPhone.


![screen](assets/fr/04.webp)


For the purposes of this tutorial, we're going to carry out an Android download.

If you choose to download via **Zapstore**, you will be redirected to it. Once on Zapstore, type **White Noise** in the search bar. Then proceed to download by clicking on **Install**.


![screen](assets/fr/05.webp)


![screen](assets/fr/06.webp)


If you opt to download the APK file, you'll be redirected to the White Noise GitHub repository to choose the right version for your smartphone.


The APK files available are :



- whitenoise-0.2.1-arm64-v8a.apk** (57.7 MB), suitable for recent phones with 64-bit processors;
- whitenoise-0.2.1-armeabi-v7a.apk** (47.5 MB) suitable for older phones with 32-bit processors.


You also have **.sha256** files, which are just checksums to verify the integrity of the download.


![screen](assets/fr/07.webp)


Once the download is complete, install and open the application.


![screen](assets/fr/08.webp)


### Initial user account setup


For your first connection to White Noise, press the **Register** button.


![screen](assets/fr/09.webp)


Next, configure your profile by choosing a profile photo, a name and adding a short description of yourself. You don't have to fill in your real identity (name and photo).

Note that White Noise automatically chooses a name (pseudonym) for you, which you can keep or change. Finally, press the **End** button.


![screen](assets/fr/10.webp)


You will be redirected to White Noise's **home screen**, where your conversations will be listed. Your account is now set up and ready to use. You can share your profile or search for friends to start a chat.


![screen](assets/fr/11.webp)



### Discovering White Noise interfaces


On the main interface, at the top of the screen you'll see :


In the top left-hand corner, the profile icon is a thumbnail of your profile photo, or the first letter of your profile name. Click on it to access your account settings.


![screen](assets/fr/12.webp)


![screen](assets/fr/13.webp)


In the top right-hand corner, you'll find the icon for starting a new conversation.


![screen](assets/fr/14.webp)


![screen](assets/fr/15.webp)



## User account settings


Press the profile icon in the top left-hand corner to access the settings.


![screen](assets/fr/16.webp)


At the top of the **Settings** interface, you'll find your photo and profile name, followed by your public key, which you can share using the QR code next to it.


![screen](assets/fr/17.webp)


Just below, you'll find the **Change account** button, which lets you connect to another profile within the application.


![screen](assets/fr/18.webp)


Then you have a first section with four (4) sub-menus such as :



- Modify profile**


In this submenu, you can modify the profile name, Nostr address (NIP-05)... Don't forget to click on **Save** to save your changes.


![screen](assets/fr/19.webp)



- Profile keys**


Here you have access to your public and private (secret) keys. As White Noise reminds you, your private key is not to be divulged under any circumstances.


![screen](assets/fr/20.webp)



- Mains relay


In this submenu, you can add or remove **general relays** (relays defined for use in all your Nostr applications), **inbox relays** and **key pack relays**.


To do so, tap on the **garbage** icon in front of a relay to delete it, or tap on the **+** (plus) icon to add a new one.


![screen](assets/fr/21.webp)



- Disconnecting**


Click on this sub-menu to disconnect your account from the application. But make sure you've saved your private keys offline, otherwise you won't be able to log in again later.


![screen](assets/fr/22.webp)



A second section offers sub-menus:



- Application settings


Here you can define the appearance (theme and display language) of the application, and even delete data if you feel it has been compromised, or if you yourself feel at risk.


![screen](assets/fr/23.webp)



- Donate to White Noise


You can support the team behind White Noise (a non-profit organization) with donations via their Lightning address or their Bitcoin silent payment address.


![screen](assets/fr/24.webp)


Finally, at the very bottom are the **developer settings**.


![screen](assets/fr/25.webp)



## Start a conversation


Now let's take a look at how to start a conversation. At the time of writing, White Noise offers three communication options. In turn, we'll explore **Private Conversations** (**Chat 1:1**), i.e. between just you and one other person, **Group Conversations** and **Sending Multimedia Files**.



### Cat 1:1


From the main interface, to add a new correspondent, click on the icon for starting a new conversation.

Then scan the QR code of the public key (1) or paste the public key (2) of your new correspondent into the search bar to find him or her.


![screen](assets/fr/26.webp)


Then tap on the **Start conversation** button to start a conversation with your correspondent. You can also **Follow** your correspondent or invite him/her to a group conversation by pressing the **Add to group** button.


![screen](assets/fr/27.webp)


Your first message to a new correspondent is akin to an invitation request. This request must be accepted by your correspondent before you can communicate with him/her. If they refuse, well, no conversation is possible.


![screen](assets/fr/28.webp)


What's more, as long as they don't accept your invitation, they won't be able to read the content of your initial message.


Once he accepts your invitation, he can now reply to you, and the two of you can communicate seamlessly and securely.


![screen](assets/fr/29.webp)


What's more, in a discussion, you have additional functionalities.


You can long press on a specific message to display options such as :


- react to the message with an emoji (1) ;
- make a **direct quote** to reply to the message by pressing **Reply** (2) ;
- copy the message by pressing **Copy** (3).


![screen](assets/fr/30.webp)



- delete a message with the **Delete** button only if it comes from you.


![screen](assets/fr/31.webp)


You can search within a conversation.


Click on the correspondent's avatar at the top of the screen to access "conversation information" and tap on the **Search in conversation** button.


![screen](assets/fr/32.webp)


![screen](assets/fr/33.webp)


In the search bar that appears, type the word you want to search for and launch the search. You'll then see your search words highlighted in **bold**.


![screen](assets/fr/34.webp)



### Group conversations


Conversation groups can be created on White Noise.


To do this, touch the icon in the new conversation start-up interface, then click on **New group conversation**. Then, in the search bar, enter the public key of the first member you wish to add to your group.


![screen](assets/fr/35.webp)


![screen](assets/fr/36.webp)


Eventually, if this option doesn't work, from the **Start a new conversation** interface, enter the public key of the first member you wish to add to the group in the search bar. You can also scan the QR code associated with his or her public key.


This time, instead of tapping the **Start conversation** button, click the **Add to group** button instead.


![screen](assets/fr/37.webp)


On the pop-up menu that appears, tap on **New group conversation**.


![screen](assets/fr/38.webp)


Then press **Continue** (you don't need to enter its public key again).


![screen](assets/fr/39.webp)


As the group's creator, you are automatically its administrator. Fill in the group details, such as **group name and description**, then click on the **Create group** button.


![screen](assets/fr/40.webp)


The user you add as the first member, and any others you add later, receive a notification inviting them to join the group. They must accept by clicking on **Accept** to join the group.


![screen](assets/fr/41.webp)


It's also possible to add a new member with whom you're already chatting to an existing group. To do so, click on the correspondant's avatar at the top of the screen to access the "conversation information" and tap on the **Add to group** button.


![screen](assets/fr/42.webp)


On the new interface that appears, **check** the group you wish to add him to and tap on **Add to group**. All that's left to do is wait for it to agree to join the group.


![screen](assets/fr/43.webp)


Note that only a group administrator can modify group information and add or expel members. Also, key rotation prevents banned members from decrypting future messages.


To remove a member, from the main group interface, tap on the group icon at the top to access the group information interface.


![screen](assets/fr/44.webp)


![screen](assets/fr/45.webp)


Then click on the member's name and **Remove from group**. From this interface, you can also send him a message, follow him or add him to another group.


![screen](assets/fr/46.webp)


### Sending multimedia files


For the moment, only photos can be shared between users on White Noise. Whether you're in a private conversation or a group chat, to do so, you need to :



- press the **plus (+)** symbol on the left-hand side of the text message input field.


![screen](assets/fr/47.webp)



- then click on the box marked **Photos** at the bottom to access your gallery.


![screen](assets/fr/48.webp)



- choose the photo(s) to send.


![screen](assets/fr/49.webp)


![screen](assets/fr/50.webp)


![screen](assets/fr/51.webp)




## Key points to remember


White Noise offers a good level of confidentiality and superior security. On the other hand, it is a very recent application, not very widespread and still in its infancy. Consequently, it's still too early to draw any active conclusions. It is possible to encounter a few malfunctions during use.


At present, it lacks certain functionalities (no audio or video calls, no sending of audio or video multimedia files) compared with popular messaging applications.


Nevertheless, White Noise remains an interesting option for conversations where confidentiality is paramount (e.g. with family, close friends or activists in a common cause), even if it does require a little effort to install (via alternative application stores or APK files) and learn (mastering a little of the concept of key pairs, clients and relays with the Nostr protocol).


Now you know how to use White Noise to communicate safely with your friends and family. Please give us a thumbs-up if you find this tutorial useful.


We recommend our tutorial on Tox Chat, an application that lets you chat without intermediaries over the decentralized Tox protocol.


https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3