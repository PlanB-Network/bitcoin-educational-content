---
name: Chim sẻ Wallet
description: Cài đặt, cấu hình và sử dụng Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet là phần mềm quản lý danh mục đầu tư Bitcoin tự quản do Craig Raw phát triển. Phần mềm nguồn mở này được những người chơi bitcoin đánh giá cao vì nhiều tính năng và Interface trực quan.

Có hai cách để sử dụng Sparrow:


- Giống như Hot Wallet, khóa riêng của bạn được lưu trữ trên PC.
- Với tư cách là người quản lý Cold Wallet, nơi các khóa riêng được lưu giữ trên Hardware Wallet. Ở chế độ này, Sparrow chỉ thao túng thông tin công khai của Wallet, theo dõi tiền, tạo địa chỉ và xây dựng giao dịch, nhưng chữ ký Hardware Wallet là bắt buộc để làm cho các giao dịch này hợp lệ. Do đó, nó có thể thay thế các ứng dụng như Ledger Live hoặc Trezor Suite.

Sparrow hỗ trợ ví đơn chữ ký và đa chữ ký, và cho phép quản lý linh hoạt nhiều ví. Ví dụ, bạn có thể đồng thời điều khiển một Wallet được kết nối với Ledger, một Wallet khác được kết nối với Trezor và cũng có Hot Wallet.

Phần mềm này cũng cung cấp các tính năng kiểm soát tiền tiên tiến, cho phép bạn chọn chính xác UTXO nào để sử dụng trong giao dịch của mình nhằm tối ưu hóa tính bảo mật.

Về mặt kết nối, Sparrow cho phép bạn kết nối với nút Bitcoin của riêng bạn, từ xa thông qua Electrum Server hoặc với Bitcoin Core. Bạn cũng có thể sử dụng nút công khai nếu bạn chưa có nút riêng. Kết nối từ xa được thực hiện thông qua Tor.

## Cài đặt Sparrow Wallet

Truy cập [trang tải xuống Sparrow Wallet chính thức](https://sparrowwallet.com/download/) và chọn phiên bản phần mềm tương ứng với hệ điều hành của bạn.

![Image](assets/fr/01.webp)

Điều quan trọng là phải kiểm tra tính toàn vẹn và tính xác thực của phần mềm trước khi cài đặt. Nếu bạn không biết cách thực hiện, bạn sẽ tìm thấy hướng dẫn đầy đủ tại đây:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Sau khi Sparrow được cài đặt, bạn có thể bỏ qua màn hình giải thích ban đầu và đi thẳng đến màn hình quản lý kết nối.

![Image](assets/fr/02.webp)

## Kết nối với mạng Bitcoin

Để tương tác với mạng Bitcoin và phát các giao dịch của bạn, Sparrow phải được kết nối với một nút Bitcoin. Có ba cách chính để thiết lập kết nối này:


- 🟡 Sử dụng một nút công khai, tức là kết nối với một nút của bên thứ ba cho phép các kết nối như vậy. Nếu bạn không có nút Bitcoin của riêng mình, tùy chọn này cho phép bạn bắt đầu sử dụng Sparrow một cách nhanh chóng. Tuy nhiên, nút mà bạn kết nối sẽ thấy tất cả các giao dịch của bạn, điều này có thể làm mất tính bảo mật của bạn. Kiểm soát được khóa của bạn là điều cần thiết, nhưng có nút riêng của bạn thậm chí còn tốt hơn. Vì vậy, chỉ sử dụng tùy chọn này nếu bạn mới bắt đầu, đồng thời nhận thức được những rủi ro đối với quyền riêng tư của bạn.
- 🟢 Kết nối với nút Bitcoin Core. Nếu bạn có nút Bitcoin Core của riêng mình, bạn có thể kết nối nó với Sparrow Wallet, cục bộ nếu Bitcoin Core được cài đặt trên cùng một máy hoặc từ xa.
- 🔵 Kết nối qua máy chủ Electrum. Nếu nút Bitcoin của bạn được trang bị Electrs, như trường hợp của các giải pháp node-in-a-box như Umbrel hoặc Start9, bạn có thể kết nối từ xa với nó từ Sparrow.

**Tốt hơn hết là sử dụng kết nối qua Electrs hoặc Bitcoin Core trên nút của riêng bạn để giảm nhu cầu tin tưởng bên thứ ba và tối ưu hóa tính bảo mật của bạn**

### Kết nối với một nút công khai 🟡

Kết nối với một nút công khai rất đơn giản. Nhấp vào tab "*Máy chủ công khai*".

![Image](assets/fr/03.webp)

Chọn một nút từ danh sách thả xuống.

![Image](assets/fr/04.webp)

Sau đó nhấp vào "*Kiểm tra kết nối*".

![Image](assets/fr/05.webp)

Sau khi kết nối, Sparrow Wallet sẽ hiển thị dấu tích màu vàng ở góc dưới bên phải của Interface để cho biết bạn đã kết nối với một nút công cộng.

![Image](assets/fr/06.webp)

### Kết nối với lõi Bitcoin 🟢

Phương pháp thứ hai để kết nối với một nút Bitcoin là liên kết Sparrow với một Bitcoin Core. Nếu Bitcoin Core được cài đặt trên cùng một máy, xác thực sẽ thông qua tệp cookie. Nếu Bitcoin Core nằm trên một máy từ xa, bạn sẽ cần sử dụng mật khẩu được xác định trong tệp `Bitcoin.conf`.

Xin lưu ý rằng nếu bạn sử dụng nút Bitcoin Core đã cắt tỉa, bạn sẽ không thể khôi phục Wallet chứa các giao dịch trước các khối được lưu trữ cục bộ. Tuy nhiên, đối với Wallet mới được tạo trên Sparrow, điều này sẽ không thành vấn đề: các giao dịch mới của bạn sẽ hiển thị, ngay cả với nút đã cắt tỉa.

Để cấu hình nút Bitcoin Core, bạn có thể tham khảo một trong các hướng dẫn sau, tùy thuộc vào hệ điều hành của bạn:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3
https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed
Trên Sparrow, hãy chuyển đến tab "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Với Bitcoin Core cục bộ:**

Nếu Bitcoin Core được cài đặt trên máy tính của bạn, hãy tìm tệp `Bitcoin.conf` trong số các tệp phần mềm. Nếu tệp này không tồn tại, bạn có thể tạo tệp đó. Mở tệp đó bằng trình soạn thảo văn bản và chèn dòng sau:

```ini
server=1
````
Sauvegardez ensuite vos modifications.
Vous pouvez également effectuer cette configuration via l'interface graphique de Bitcoin-QT en naviguant dans "*Settings*" > "*Options...*" et en activant l'option "*Enable RPC server*".
N'oubliez pas de redémarrer le logiciel après ces modifications.
![Image](assets/fr/08.webp)
Revenez ensuite à Sparrow Wallet et renseignez le chemin vers votre fichier de cookie, généralement situé dans le même dossier que le `bitcoin.conf`, selon votre système d'exploitation :
| **macOS**   | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin                     |
| **Linux**   | ~/.bitcoin                            |
![Image](assets/fr/09.webp)
Laissez les autres paramètres par défaut, l'URL `127.0.0.1` et le port `8332`, puis cliquez sur "*Test Connection*".
![Image](assets/fr/10.webp)
La connexion est établie. Une coche verte apparaîtra en bas à droite pour indiquer que vous êtes connecté à un nœud Bitcoin Core.
![Image](assets/fr/11.webp)
**Avec Bitcoin Core à distance :**
Si Bitcoin Core est installé sur une autre machine connectée sur le même réseau, commencez par localiser le fichier `bitcoin.conf` parmi les fichiers du logiciel. Si ce fichier n'existe pas encore, vous pouvez le créer. Ouvrez ce fichier avec un éditeur de texte et ajoutez la ligne suivante :
```

máy chủ=1

```
Après avoir modifié le fichier, assurez-vous de l'enregistrer dans le dossier approprié selon votre système d'exploitation :
| **macOS**   | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin                     |
| **Linux**   | ~/.bitcoin                            |
Il est également possible de réaliser cette manipulation via l'interface graphique de Bitcoin-QT. Accédez au menu "*Settings*", puis "*Options...*", et activez l'option "*Enable RPC server*" en cochant la case correspondante. Si le fichier `bitcoin.conf` n'existe pas, vous pouvez le créer directement depuis cette interface en cliquant sur "*Open Configuration File*".
![Image](assets/fr/12.webp)
Trouvez l'adresse IP de la machine qui héberge Bitcoin Core dans votre réseau local. Pour cela, vous pouvez utiliser un outil tel que [Angry IP Scanner](https://angryip.org/). Supposons, pour l'exemple, que l'adresse IP de votre nœud soit `192.168.1.18`.
Dans le fichier `bitcoin.conf`, ajoutez les lignes suivantes, en configurant `rpcbind=192.168.1.18` pour correspondre à l'adresse IP de votre nœud.
```

[tay]

rpcbind=127.0.0.1

rpcbind=192.168.1.18

rpcallowip=127.0.0.1

rpcallowip=192.168.1.0/24

```
![Image](assets/fr/13.webp)
Ajoutez également dans le fichier `bitcoin.conf` un identifiant et un mot de passe pour les connexions à distance. Assurez-vous de remplacer `loic` par votre nom d'utilisateur et `my_password` par un mot de passe fort :
```

rpcuser=loic

rpcpassword=mật_khẩu_của_tôi

```