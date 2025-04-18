---
name: Simple Login
description: Identity protected with aliases
---
![cover](assets/cover.webp)
## Login = email = loss of privacy

In the digital world, it has become standard practice to have an account for every platform one wishes to access.
Each of these services requires a login, usually associated with the _username_ and _password_ pair. Often, the username is the user's personal email.

When using one's personal email address for every login, it's easy to imagine the first consequence: loss of confidentiality, which becomes major if the address is composed of _name.surname@serviceemail.com_.

Open-source tools developers have created a series of application suites, born precisely to make users gain back a bit of privacy: they will still log in, but using an alias instead of the tool that reveals their private identity.

The simplest among those I have personally tried and am still testing is [Simple Login](https://simplelogin.io/).

## Alias

An email alias simply substitutes the _name.surname_ part of your email address with a fictitious name. For the user, nothing changes; the alias service forwards emails to and from the usual address as normal. Everyone can continue using their inbox as they always do, but instead of displaying their real name, it will show an unrecognizable user. This service needs to be efficient, and so far, Simple Login has proven to be just that.

When visiting the Simple Login site for the first time, you must create an account (here too!), using the "official" email address. Here, you must enter the email, a password, and solve a captcha.

![image](assets/it/02.webp)

Simple Login sends a verification message to the indicated email address. Instead of clicking the verification button, it is advisable to copy the link and paste it into the address bar.

![image](assets/it/03.webp)

![image](assets/it/04.webp)

The Simple Login dashboard opens immediately, with a brief tutorial for navigation.

![image](assets/it/05.webp)

It should be noted that Simple Login automatically activates the subscription to the newsletter, which can be deactivated from the appropriate command.

![image](assets/it/06.webp)

## Settings

You can take a look at the _Settings_ right away to discover the features of the service. Simple Login starts with all options active, including the _Premium_ ones, which remain usable for 10 days. Once the trial period is over, you will have the possibility to create 10 aliases with this profile and you can directly link your Proton email, as Simple Login has been acquired by the Swiss email provider.

![image](assets/it/07.webp)

You can set a series of parameters, or check if your email has already been compromised in terms of privacy.

![image](assets/it/08.webp)

Finally, you can export a backup of your profile, or import one from another provider.

![image](assets/it/09.webp)

### Work Email

Those who use email with a personal domain as a work email can set up their private domain.

![image](assets/it/10.webp)

From the main panel, by choosing _Mailboxes_, it is even possible to add other email addresses and also use the aliases that will be created accordingly. In this tutorial, for example, I decided to create the profile with a _gmail.com_ mailbox, and then associate a _proton.me_ address.

![image](assets/it/11.webp)

Adding a new address, especially if it belongs to the Proton provider, the guided procedure shows the possibility to enter _sudo_ mode, super user. Simple Login will ask to enter the password of this mailbox, to prove legitimate ownership.

⚠️ **I personally advise against doing this**. ⚠️

![image](assets/it/12.webp)

**It's better to access the email box -> copy the link for verification and paste it in the URL bar -> and obtain the verification without revealing the password.**

![image](assets/it/13.webp)

Out of the two addresses entered, one becomes the default and the other is a secondary, but they can easily be switched, and the setting is easily identifiable in the dashboard.

![image](assets/it/14.webp)

After adding a second email address (optional), let's see what we can do with Simple Login.

## Creation of aliases

In the panel, the first menu option is labeled _Alias_, which is where you can create them. You have the option to generate aliases randomly by clicking the Random Alias button, which is the green button shown in the next photo. This feature creates a unique and intriguing email address.

![image](assets/it/24.webp)

If, however, you wish differentiate services by giving them different names, you must choose _New Custom Alias_. By doing so, you can give the alias the name of the service you want to access (social media, service providers, online events, strangers met by chance, etc.). The rest is handled by Simple Login.
For fun (but not really, to tell the truth) I decided to create an alias for the bank and called it `BANK`. Even though it's true that my bank knows everything about me, I find it amusing to communicate with them using an email address that is incomprehensible to them. Simple Login indeed generates a random name, which is separated from the one we choose by a `.`

Here, the new email address can become:
- bank.breeding123@aleeas.com
- bank.platter456@slmails.com
- bank.preoccupy789@8shield.net
- and so on

One can choose more than one domain: public ones are available with the free plan, while others, indicated as private (including _@simplelogin.com_), expand the choice for users who decide to subscribe to a paid plan.

![image](assets/it/15.webp)

Once the random suffix and domain have been chosen, you can set whether this new (and bizarre) address should serve as an alias for just one of the personal email boxes, or for all of them. The alias becomes ready and active after clicking on _Create_

![image](assets/it/16.webp)

The new email address was created and it is now visible, ready to be sent (to the bank!) simply by copying it.

![image](assets/it/18.webp)

At this point, you can focus on creating an alias for every service or platform you want to access and where email is required as an essential parameter for creating an account.

![image](assets/it/19.webp)

For privacy enthusiasts, there's also the option to generate an email address based on the UUID protocol (not on identifiable names), which creates a unique 128-bit identifier that isn't controlled by centralized parties. This feature, which is useful for sensitive accounts, can be found in the _Random Alias_ menu.

![image](assets/it/21.webp)
![image](assets/it/22.webp)

As you can see, this is an email address that requires proper management.

If you change your mind and no longer want to use an alias, just click on the _More_ command of each individual alias and choose _Delete_.

![image](assets/it/23.webp)

## Alias Management

Creating aliases is simple, as is their management, which only requires a bit of care and discipline. All traffic, in fact, will still pass through the email inbox that we have defined, at the beginning, as the official one. Notifications and important communications from platforms will continue to arrive on Gmail, Proton, or whatever the email provider is.

The result, however, is that we have preserved the main address which, from the moment of the creation of the aliases, we are free to decide whom to reveal it to and whom not to.

An alias works both for receiving and sending: another user will indeed receive the reply from alias.preoccupy789@8shield.net, if this is the pseudonym chosen for that particular recipient.

## Pros

Overall, using aliases is an effective way to protect your identity and privacy. Email addresses are often collected by data brokers and websites to track user habits and behaviors. While an alias doesn't make you completely untraceable, consistently using one is a positive step toward safeguarding your information. Moreover, in our "global digital village," where hacking, data selling, and security breaches are all too common, it's highly likely that the email you use to register on various websites has already been compromised or targeted.

A unique pseudonym, used for every login, **immediately allows us to understand which platform sends spam (or worse) to our mailbox, because the email is identified by the alias associated with it**. You have no idea how much spam and phishing come from so-called reliable channels, because they are institutional, until you start using an alias for banks, one for postal services, or a specific one for some mandatory government services. Once the sender of the spam (or worse) is identified, you will know that site has been compromised, taking every precaution to protect all the data provided (think about credit cards!) to that specific website, which may realize the breach weeks later.

Regarding Simple Login, this tool has the following features:

- mobile app (also from F-Droid) and browser extension, to manage aliases in any situation;
- two-factor authentication for each new pseudonym, which increases the degree of independence from the service itself;
- PGP support (for _Premium users);
- simple creation of every type of alias (custom, random, and UUID);
- among the free plans in the sector, the ability to use aliases with more "official" email boxes. Other competitors limit to just one.

## Cons
- 10 aliases might not be enough if you plan to use Simple Login extensively. In this case, the paid plan, which is quite affordable, is useful to increase the number of possible aliases available.
- It is not possible to create an alias with a specific name and domain. The random suffix, added after a name chosen by us, generates an address that can be described as bizarre at best. Traditional social media usually refuse to grant accounts created with this type of email addresses. Nostr fixes this!
- If you use an alias to send a message to someone, it's easy to end up in the recipient's spam folder. As a first step, it's advisable to use the pseudonym for receiving, just as in the case of creating an account, subscribing to a mailing list, etc.
