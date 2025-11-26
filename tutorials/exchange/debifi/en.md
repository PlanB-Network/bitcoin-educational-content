---
name: Debifi
description: Get a non-custodial loan guaranteed by Bitcoin.
---

![cover](assets/cover.webp)



## Introduction


For centuries, traditional lending has made it possible to finance many projects. However, it remains slow, costly and not very inclusive, especially for those who do not have access to a solid banking infrastructure.


The rise of the Bitcoin protocol ushered in a new financial era, bringing with it a number of challenges. One of these challenges was how to obtain liquidity without being forced to sell Bitcoin, thereby losing exposure to its growth potential


The result is **Debifi**, a platform that positions itself as a modern alternative to banks. The aim is clear: to make credit as simple and transparent as possible, by combining the advantages of the traditional financial system with the freedom offered by Bitcoin. The name Debifi reflects this vision: ***Decentralized Bitcoin Finance***, a contraction that illustrates the meeting of decentralized finance and Bitcoin innovation.


Debifi is a non-custodial Bitcoin backed lending platform, which means you retain control of your private keys. It allows users to unlock liquidity in exchange for their locked bitcoins as collateral. Unlike traditional bank loans, Debifi uses a multi-signature escrow system (3 out of 4) and does not accept collateral rehypothecation, guaranteeing greater security and transparency.


In practice, this means that neither Debifi nor an individual lender can spend your BTC without the agreement of three parties (you, the lender and a trusted third party). This makes the system more secure: if you borrow on Debifi, you retain ownership of your Bitcoin until the loan has been repaid in full.


## Advantages of Debifi


With Debifi, you get Bitcoin-backed loans that are over-collateralized and secured on-chain. Your funds stay safe with multisignature wallets, 2FA, and total control over your Bitcoin — you hold your keys, you keep your coins. Borrow in a range of stablecoins or fiat options, at competitive rates, and global liquidity.


Here's a quick comparison between a Debifi loan and a traditional bank loan:

| Characteristics        | Loan via Debifi                                                        | Traditional Bank Loan                                                       |
| ---------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Accessibility          | ✔️ Open to any Bitcoin holder (even without banking history)           | ❌ Often limited to clients with physical collateral and strong records      |
| Speed of approval      | ✔️ Funds available within minutes or hours                             | ❌ Lengthy process (days or weeks)                                           |
| Required guarantees    | ✔️ Bitcoin used as the sole collateral                                 | ❌ Physical guarantees (property, land, stable income)                       |
| Asset control          | ✔️ You keep exposure to Bitcoin and its upside potential               | ❌ No connection between the loan and your financial assets                  |
| Geographic flexibility | ✔️ Available everywhere (no banking jurisdiction constraints)          | ❌ Restricted to the bank’s jurisdiction                                     |
| Main risk              | ❌ Liquidation risk if BTC price drops too sharply                      | ❌ Risk of asset seizure or negative impact on credit score                  |

Before I show you step-by-step how to borrow on Debifi, there are a few points I think you need to know.



## Definitions



- Origination fees** are one-off charges levied at the time a loan is granted, and calculated as a percentage of the amount borrowed. These fees cover administrative, operational and management costs.



- Collateral** is an asset you deposit to secure a loan. In Debifi's case, the collateral is Bitcoin (BTC), which the borrower deposits in the Multisig 3/4 escrow.



- The Multisig escrow (3/4)** system is a secure deposit mechanism where a borrower's bitcoins are placed in a multi-signature address. Specifically, four (4) parties each hold a key (borrower, lender, Debifi, independent third party). To move funds, at least 3 out of 4 signatures are required.



- A stablecoin** is a cryptocurrency whose value is pegged to a stable asset (e.g. US dollar), which avoids the volatility of Bitcoin. For example, 1 USDC is always worth ~$1, as it is backed by fiat reserves.



- The Loan-to-Value (LTV)** ratio of a loan determines how much cash you can borrow as collateral for your Bitcoin. LTV ratio = Loan amount / Collateral amount * 100. For example, an LTV of 50% means that the value of the loan is equal to 50% of the value of the Bitcoin deposited.



BTC Sessions video tutorial :


![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)


## Getting started with Debifi


To get started on Debifi, you'll need a few prerequisites.

### Prerequisites


Before you can borrow from Debifi, please make sure you have the following items:



- Bitcoin wallet: where you hold your BTC (ideally non-custodial, e.g. Hardware Wallet or a trusted mobile wallet). It's from this wallet that you'll send the Bitcoin collateral to Debifi and receive the collateral back.


You can use Aqua, a Bitcoin and Liquid wallet that also supports USDT stablecoin management on various networks. Or COLDCARD (Mk4 or Q), currently the only hardware supported by Debifi.


https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3


- KYC (*Know Your Customer*): depending on the loan offer chosen, an identity verification process may be required. On Debifi, each offer indicates whether KYC is required or not. So prepare accordingly. KYC is carried out by reliable third-party service providers such as Sumsub.


![image](assets/fr/03.webp)



- Two-factor authentication application: Debifi requires an Authenticator code for every important action. It's an extra layer of security. In this tutorial, we'll be using Google Authenticator. Alternatively, you can use others as you see fit.


https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc


- Debifi website and mobile application: Debifi is both a website and a mobile application, and the two work in tandem. The mobile app becomes a wallet, which stores your private key, and manages the signing of contracts. In addition, you need to use the website to commit contracts (a large Interface gives you a general view of loan contracts and their specifics).



- The Debifi mobile app (iOS/Android) is required to take out loans. You must download the app, create an account and "link" your device (registering the device to your account). The Debifi app supports two-factor authentication (2FA) and without a smartphone, you cannot confirm transactions on Debifi.


### Create an account


Visit [Debifi's official website](https://debifi.com/app).


![image](assets/fr/04.webp)


Install your application according to the type of smartphone you have, then open it.


![image](assets/fr/05.webp)


![image](assets/fr/06.webp)


Once in the application, click on the **Settings** menu.


![image](assets/fr/07.webp)


Then click on **Login or create account** to create an account with your e-mail address.


![image](assets/fr/08.webp)


![image](assets/fr/09.webp)


![image](assets/fr/10.webp)


You will receive a verification code by e-mail. Copy and paste this code into the application. Then open the Debifi application on your smartphone and log in.


![image](assets/fr/11.webp)


### Securing your account


For security, Debifi will ask you to follow three steps.


![image](assets/fr/12.webp)



- First, you'll need to set a strong PIN code to access your application later.


![image](assets/fr/13.webp)



- Next, set up two-factor authentication (2FA) to associate your device with your account using the 2FA code.


![image](assets/fr/14.webp)



- Finally, save the 12 words of your private key by writing it down on a reliable medium and keeping it in a safe place. This phase is essential for recovering your account and managing your funds.


![image](assets/fr/15.webp)



- For added security, you can even add a passphrase.


![image](assets/fr/16.webp)


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Please note that only your registered smartphone will be able to open your account (an additional security measure).


Once you have completed these steps, click on the **Offers** menu to see the available loan offers. When you click on an offer, it redirects you to the Debifi website.


![image](assets/fr/17.webp)


### Access the website and explore loan offers


Once your device is connected, go to the [Debifi website](https://debifi.com/). Log in to establish a secure connection between the Debifi mobile application and the web platform. This makes it easier for you to interact with available loan offers (a clear view of the details of each offer) and manage your account.


![image](assets/fr/18.webp)


![image](assets/fr/19.webp)


![image](assets/fr/20.webp)


![image](assets/fr/21.webp)



Video tutorial on how to log in with your account on the platform :


![video](https://youtu.be/cUwCfTKDAOo)


## Loan application


The platform puts you in touch with institutional-quality liquidity and offers a range of options to suit your needs. Browse through to find out what's available. You also have the flexibility to adjust loan parameters according to your individual risk tolerance and financial situation.


![image](assets/fr/22.webp)


The fiat currencies Debifi currently offers can be viewed on the platform.


![image](assets/fr/23.webp)


### Clear, flexible contractual clauses


Debifi relies on transparent and flexible loan conditions to meet the needs of each party (lender and borrower). Key clauses include :


#### Loan-to-value ratio (LTV)

Bitcoin loan tranches are generally three (3) in number:



- Conservative (30% - 40% LTV), which corresponds to a low-risk loan, is ideal for maximizing security against Bitcoin price volatility;



- Balanced (50% LTV) ;



- Aggressive (70% LTV), which offers greater liquidity, but carries a very high risk of liquidation during market downturns. Active monitoring of Bitcoin market conditions is a must when choosing this tranche.


#### Interest rates


Rate-setting generally depends on your chosen LTV, the length of the loan term, collateral volatility and platform-specific risk assessments. Rates remain fixed for the duration of the loan.


#### Loan term and repayment flexibility


Repayment schedules are flexible and designed to accommodate the borrower’s needs. Loans can be fully or partially repaid at any time without additional fees, provided collateral requirements remain satisfied. Throughout the term of the loan, interest is typically paid periodically, while the principal is settled at maturity.


#### Liquidation rights (Margin calls)


Given Bitcoin’s volatility, loans include a clearly defined margin call policy. A margin call occurs when the LTV rises due to a decline in collateral value. Debifi notifies the borrower by email and through the app, allowing them to add collateral or repay part of the loan.

75% LTV — First alert  
80% LTV — Second alert  
85% LTV — Final alert  
90% LTV — Collateral is liquidated


### Launching the loan process


To select a loan offer that suits your needs, click on it to view its features.


![image](assets/fr/24.webp)


You can see :

1. Name of lending institution ;

2. The loan amount range;

3. That you will receive the funds in USDC Ethereum ;

4. The loan period, interest rate and LTV ratio;

5. KYC is required for this offer;

6. The exact amount you need must be entered (this amount must be within the band, see 2);

7. The Ethereum USDC address to be used to receive the funds must be entered.


Once you are happy with the offer and have filled in the necessary information, click on "Contract request".


![image](assets/fr/25.webp)


Return to the mobile application for ''**Provide public key**''.


![image](assets/fr/26.webp)


Press '' **Provide public key** '', then choose the source of the public key. The lender will also need to supply a public key.


![image](assets/fr/27.webp)


![image](assets/fr/28.webp)


![image](assets/fr/29.webp)


![image](assets/fr/30.webp)


The next step is to sign the contract. Still in the mobile application, press '' **Sign Contract** ''


![image](assets/fr/31.webp)


![image](assets/fr/32.webp)


When you finish signing the contract, Debifi automatically creates a unique multi-signature Bitcoin address (escrow 3-sur-4) for your contract. As long as your bitcoins are in the escrow, they cannot be used elsewhere.


### Deposit of the guarantee and receipt of your funds


The final step is to deposit your Bitcoin collateral in the multi-signature escrow system. Debifi shows you the escrow address (B) and the quantity of BTC (A) to be sent as (collateral + commission).


![image](assets/fr/33.webp)


You will also receive this notification in your mobile application.


![image](assets/fr/34.webp)


As soon as your deposit is confirmed, the lender will pay the loan amount to the receiving address you have indicated, finalizing the transaction and giving you access to the funds you need.


You will then receive a notification from Debifi, asking you to pay the loan fees or commissions in order to progress the status of your loan.


In reality, once the contract has been created, the loan fees are automatically deducted from the collateral escrowed by the borrower in the multi-signature escrow address.


All you have to do is sign a transaction that will allow Debifi to deduct its commission from the guarantee. For its part, your lender will also need to sign the fee deduction transaction, otherwise Debifi will not be able to receive its commission.


![image](assets/fr/35.webp)


The applicable lending fees are 1.5-2%, depending on the term of the contract. The platform charges commissions in Bitcoin only.


## Loan tracking


Once the loan is active, Debifi allows you to track your contract in real time. In the interface, you will find:

- The amount borrowed and the remaining term.  
- The current LTV (Loan-to-Value) ratio, which rises when the price of BTC decreases and the value of your collateral falls.



Borrowers are notified when the collateral value decreases, and this information is also displayed on the contract summary page. To restore the original loan-to-value ratio, the borrower must either:

- deposit additional collateral;  
- repay all or part of the debt.



In the event of an increase in the price of the collateral, the borrower retains any capital gains on the collateral. He owes only the amount of the loan, which is predetermined and independent of the Bitcoin price.



## Repayment and recovery of collateral


At the end of the agreed term (or earlier, if you wish), you must repay the loan.

In Debifi :



- Go to your contract and click on **Make a repayment**. Enter the total amount due (principal + interest).



- Send the stablecoins from your wallet to the lender's address indicated, and return to confirm the repayment on the platform by copying the **ID** of the repayment transaction into the dedicated tab. This makes it easier for Debifi to carry out its checks.


Once payment has been confirmed by the lender (and by you), Debifi will then ask you to **refund**. Your Bitcoin collateral is released and you can return it from the escrow to your own wallet.  Don't forget to collect all your Bitcoins.


As soon as you receive your bitcoins, the loan contract changes to **Contract completed**.


Congratulations! You've finalized the process.



## Best practices and safety


Whatever your objectives or motivations—financing a project, acquiring property, buying bitcoins, etc.—exercise great caution before taking out a loan backed by Bitcoin. Take the time to assess your decision carefully, as Bitcoin remains a volatile asset. **A sharp drop in its price could result in the forced liquidation of your bitcoins.**


Monitor your loan-to-collateral (LTV) ratio. Set up alerts (BTC price, LTV) if possible. Don't let your ratio approach 90%. If in doubt, increase collateral or repay early.


Control your keys. Keep your BTC in a secure wallet (ideally hardware or a reputable wallet). Don't set a PIN code related to an important date in your life and never share your recovery phrase. On Debifi, you generate your private key in the application - Debifi doesn't know it.


Start small if possible. For your first loan, test a modest amount to familiarize yourself with the process.


Use only the official Debifi website to keep up to date with Debifi news, and avoid unknown or phishing links.  Update the application, protect your smartphone with a PIN code, and choose a compatible Hardware Wallet.


Alternatively, if you're a lender, this tutorial video will guide you through using the Debifi platform. From selecting borrowers interested in your offer, to providing public keys, signing agreements, transferring stablecoins and more.


![video](https://youtu.be/g8iLxwI4xT0)


You now know how to use the Debifi platform to obtain a loan.


I recommend you take this course, which takes an in-depth look at Bitcoin, Stablecoins and their contribution to sovereignty.


https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46