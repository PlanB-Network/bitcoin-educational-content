texte explicatif sur les hot wallet vite fait

# Mobile Wallets

Taken from https://bitcoiner.guide/wallet/compare/

| Wallet            | Connect to own node | Coin control | iOS | Android | Lightning | Native Segwit | Tor |
| ----------------- | ------------------- | ------------ | --- | ------- | --------- | ------------- | --- |
| Blockstream Green | Y                   | N            | Y   | Y       | N         | N             | Y   |
| Blue Wallet       | Y                   | Y            | Y   | Y       | Y \*      | Y             | Y   |
| Electrum          | Y                   | Y            | N   | Y       | Y         | Y             | Y   |
| Fully Noded       | Y                   | Y            | Y   | N       | Y         | Y             | Y   |
| Hexa              | N                   | N            | Y   | Y       | N         | Y             | N   |
| Muun              | N                   | N            | Y   | Y       | N \*      | Y             | N   |
| Samourai Wallet   | Y                   | Y            | N   | Y       | N         | Y             | Y   |

- Blue Wallet lightning only allows users to connect to their own instance of LNDhub
- Muun allows payment of lightning invoices via submarine swaps

# Lightning Native

| Wallet  | Connect to own node | Send/Receive on chain | iOS | Android | LND | C Lightning | Eclair |
| ------- | ------------------- | --------------------- | --- | ------- | --- | ----------- | ------ |
| Alby    | Y                   | N                     | N   | N       | Y   | Y           | Y      |
| Breez   | Y                   | Y (via swaps)         | Y   | Y       | Y   | N           | N      |
| Phoenix | Y                   | Y (via swaps)         | N   | Y       | N   | N           | Y      |
| Zap     | Y                   | Y                     | Y   | Y       | Y   | N           | N      |
| Zeus    | Y                   | Y                     | Y   | Y       | Y   | Y           | Y      |

# Desktop Wallets

Taken from https://bitcoiner.guide/wallet/compare/

| Wallet            | Connect to own node | Coin control | Mac | Windows | Linux | Lightning | HWW Support |
| ----------------- | ------------------- | ------------ | --- | ------- | ----- | --------- | ----------- |
| Bitcoin Core      | Y                   | Y            | Y   | Y       | Y     | N         | Y \*        |
| Blockstream Green | N                   | N            | Y   | Y       | Y     | N         | N           |
| Blue Wallet       | Y                   | Y            | Y   | N       | N     | Y         | Y \*        |
| Electrum          | Y                   | Y            | Y   | Y       | Y     | Y         | Y           |
| Fully Noded       | Y                   | Y            | Y   | N       | N     | Y         | Y \*        |
| Lily Wallet       | N                   | N            | Y   | Y       | Y     | N         | Y           |
| Specter Desktop   | Y                   | Y            | Y   | Y       | Y     | N         | Y           |
| Sparrow Wallet    | Y                   | Y            | Y   | Y       | Y     | N         | Y           |

- Bitcoin Core hardware wallet support is command line only
- Blue Wallet hardware wallet support is only supoprted via PSBT
- Fully noded only supports Coldcard via PSBT

# Hardware Wallets

Taken from https://bitcoiner.guide/wallet/compare/

| Wallet      | USB | PSBT | Backup                | Price                     |
| ----------- | --- | ---- | --------------------- | ------------------------- |
| BitBox02    | Y   | N    | SD card (unencrypted) | $99                       |
| Cobo Vault  | N   | Y    | Shamir                | $99, $149 or $479         |
| Coldcard    | Y   | Y    | Encrypted to SD card  | $120                      |
| Passport    | N   | Y    | Encrypted to SD card  | $199                      |
| Specter DIY | N   | Y    | Seed only             | $100-$200 depending on HW |
| Trezor      | Y   | N    | Shamir                | $70 or $210               |
