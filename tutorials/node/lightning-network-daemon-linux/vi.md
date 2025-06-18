---
name: Lightning Network Daemon (Linux)
description: Cài đặt và chạy Lightning Network Daemon trên Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network là phiên bản Layer thứ hai của Bitcoin, cho phép nó đạt đến kích thước cực nhanh, đặc biệt là nhờ vào tốc độ và chi phí giao dịch thấp mà nó cung cấp.



Trong hướng dẫn này, chúng ta sẽ cài đặt Lightning Network Daemon trên máy Linux của mình (bản phân phối Ubuntu 24.04).



## Lightning Network Daemon là gì?



Lightning Network Daemon là bản triển khai Go hoàn chỉnh của Lightning Network. Nó được tạo ra bởi Lightning Labs và cho phép bạn chạy phiên bản đầy đủ của một nút Lightning trên máy của mình.


Nói cách khác, với cách triển khai này, bạn có thể:





- Tương tác với Lightning Network**: Bạn có thể sử dụng dòng lệnh để tạo danh mục đầu tư Lightning, quản lý kênh và tuyến thanh toán, cùng nhiều chức năng khác trực tiếp từ thiết bị đầu cuối của bạn.
- Liên kết một nút Bitcoin từ xa hoặc phiên bản Bitcoin Core của riêng bạn**: LND cho phép bạn liên kết một phiên bản Bitcoin và sử dụng nó làm backend của bạn. Để sử dụng triển khai này, bạn không cần phải chạy phiên bản Bitcoin Core trên máy của mình.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Tại sao bạn nên có nút Lightning riêng?


Lightning là lớp phủ Bitcoin giúp tối ưu hóa quá trình chuyển giao và giảm chi phí giao dịch.



Bằng cách xoay nút Lightning của bạn, bạn sẽ có được chủ quyền và quyền tự chủ. Bạn kiểm soát được tiền của mình, vì vậy hãy ghi nhớ:



"Không phải chìa khóa của bạn, không phải bitcoin của bạn."



Theo nghĩa này, việc chạy một nút Lightning sẽ tăng cường tính bảo mật và tính toàn vẹn của dữ liệu theo những cách sau:





- Kiểm soát hoàn toàn**: Quản lý kênh thanh toán của riêng bạn, trở thành ngân hàng của chính mình và làm chủ tài sản của bạn.
- Bảo mật**: Giao dịch mà không cần nhờ đến bên thứ ba để bảo vệ quyền riêng tư của bạn.
- Học tập và tự chủ**: Nhờ các lệnh `lncli`, bạn có thể hiểu rõ hơn các quy trình cơ bản của Lightning bằng cách tự mình áp dụng từ thiết bị đầu cuối.
- Phân cấp**: Đóng vai trò tích cực trong việc củng cố và phân cấp Bitcoin / Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Bạn có hai lựa chọn để chạy phiên bản triển khai LND trên máy của chúng tôi. Chúng tôi có thể thiết lập môi trường trên máy của mình để chạy cục bộ hoặc cài đặt LND từ vùng chứa Docker. Ở đây, chúng tôi sẽ tập trung vào lựa chọn đầu tiên và xem cách tiến hành với Docker trong hướng dẫn sau.


## Cài đặt LND từ mã nguồn



### Điều kiện tiên quyết


Vì LND được viết bằng Go, bạn cần đảm bảo rằng mình có môi trường GoLang và các phụ thuộc cần thiết trên máy Linux của mình.





- Yêu cầu về phần cứng:**


Để có trải nghiệm mượt mà, liền mạch, máy của bạn cần có đủ dung lượng cần thiết để chạy nút LND Lightning.



Bạn sẽ cần:


1. **RAM 8 GB** cho khả năng lưu trữ tối ưu,


2. **Bộ xử lý đa lõi (lõi tứ hoặc nhiều hơn)** để quản lý hiệu quả các hành động của nút của bạn,


3. **Ít nhất 5GB dung lượng đĩa** cho chế độ nút được cắt tỉa và 1TB để chạy Bitcoin Core (tùy chọn nếu sử dụng nút từ xa)





- Cài đặt các phụ thuộc hữu ích:**


Lệnh bên dưới sẽ cho phép bạn cài đặt trên máy các công cụ bạn cần để chạy LND. Trong số những thứ khác, bạn sẽ cần cài đặt `Git`, một công cụ quản lý phiên bản và `make`, có thể thực thi và xây dựng triển khai LND từ mã nguồn.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Cài đặt GoLang trên máy Linux của bạn**



Tính đến ngày viết hướng dẫn này, LND yêu cầu phiên bản 1.23.6 của Go*** để cài đặt.



Nếu bạn đã cài đặt phiên bản trước đó, hãy gỡ bỏ phiên bản đó để cài đặt Go mới.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Cấu hình môi trường Go**


Trong tệp `~/.bashrc`, hãy khởi tạo các biến môi trường sau để thêm Go vào hệ thống Linux của bạn.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Kiểm tra cài đặt** (bằng tiếng Pháp)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Sao chép kho lưu trữ GitHub LND



Sử dụng git để lấy bản sao mã nguồn LND cục bộ trên máy của bạn


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Xây dựng và cài đặt



Công cụ `make` đã được cài đặt trước đó sẽ cho phép bạn xây dựng tệp thực thi từ mã nguồn LND và tiến hành cài đặt.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Cài đặt LND trên máy của bạn



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Kiểm tra cài đặt của bạn** (bằng tiếng Pháp)



Để đảm bảo mọi thứ diễn ra suôn sẻ, chạy lệnh này sẽ cung cấp cho bạn phiên bản LND bạn đang chạy.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Bảo trì và nâng cấp



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **QUAN TRỌNG**: Các bản cập nhật LND có thể yêu cầu các phiên bản Go mới hơn, vì vậy hãy đảm bảo cập nhật hệ thống của bạn để tránh các sự cố phụ thuộc trong quá trình cài đặt.


### Cấu hình Lightning Network Daemon



Cấu hình của một nút Lightning LND tương tự như của Bitcoin và được thực hiện trong một tệp cấu hình chứa tất cả các tham số của nút của bạn. Để thực hiện việc này, tại gốc máy của bạn, bạn có thể tạo một thư mục ẩn `.LND` và sau đó tạo tệp cấu hình `LND.conf` trong thư mục này.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





Trong tệp cấu hình, bạn có thể thiết lập nút LND của mình.



```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```



## Hiểu cấu hình của bạn



Điều quan trọng là bạn phải hiểu cấu hình tối thiểu cần thiết để cài đặt chính xác và đầy đủ nút LND của mình.



Dựa trên nội dung của tệp `~/.LND/LND.conf`, sau đây là thông tin chi tiết về các trường:





- noseedbackup**: Cho phép bạn chọn xem bạn có muốn LND tự động sao lưu danh mục đầu tư của bạn hay không. Đặt thuộc tính này thành `0` cho phép bạn lưu thủ công thông tin khôi phục ở vị trí an toàn do cá nhân bạn chọn.





- debuglevel**: Cho phép bạn xác định mức độ chi tiết của lỗi và nhật ký trong trường hợp lỗi xảy ra trong quá trình thực hiện hành động.





- Bitcoin.active**: Chỉ thị cho LND hoạt động như một nút Bitcoin và tương tác với mạng Bitcoin.





- Bitcoin.Mainnet**: Chỉ định LND kết nối với mạng chính của Bitcoin (Mainnet), bạn có thể đặt các giá trị `bitcoind.signet` và `bitcoind.regtest` tương ứng cho mạng Bitcoin Signet và Bitcoin Regtest





- Bitcoin.node**: Chỉ định loại nút Bitcoin mà LND sẽ kết nối.





- Bitcoin.rpcuser** và **Bitcoin.rpcpassword**: Đại diện.


tương ứng với thông tin đăng nhập (người dùng, mật khẩu) để kết nối với nút Bitcoin của bạn





- bitcoind.zmqpubrawblock** và **bitcoind.zmqpubrawtx**: lần lượt xác định các điểm cuối ZeroMQ để nhận thông báo về các khối và giao dịch mới trên mạng Bitcoin.




## Kiểm tra cài đặt của bạn với LND



Bạn có thể muốn đảm bảo rằng quy trình đã thành công và bạn đang đồng bộ hóa với Lightning Network để thông tin nút của bạn luôn được cập nhật.



Để bắt đầu triển khai LND và lấy thông tin về nút của bạn, chỉ cần nhập lệnh:


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Thực hiện hành động trên LND



Sau khi quá trình cài đặt hoàn tất và được kiểm tra, bạn có thể bắt đầu sử dụng.


Sau đây là các lệnh cần thiết để bạn bắt đầu.



### Tạo danh mục đầu tư


Danh mục đầu tư Lightning là bước đầu tiên trong mọi hành động quản lý tiền của bạn.



⚠️ **QUAN TRỌNG**: Hãy ghi nhớ cẩn thận cụm từ **seed** gồm 24 từ của bạn. Bạn sẽ cần nó để khôi phục tiền của mình trong trường hợp có vấn đề.



Ngoài ra, hãy lưu mật khẩu Wallet để bạn có thể mở khóa bằng lệnh `lncli unlock` khi bạn khởi động lại nút LND.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Kiểm tra số dư của bạn



Tra cứu tài khoản của bạn trực tiếp từ thiết bị đầu cuối:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Thông tin về nút của bạn



Sử dụng lệnh bên dưới để tìm hiểu kênh nào đang hoạt động trên nút của bạn.



```bash
lncli listchannels
```



Bạn cũng có thể lấy danh sách các nút mà bạn đang kết nối.



```bash
lncli listpeers
```



### Quản lý kênh



Kênh Lightning cho phép bạn có **kết nối trực tiếp, từng cặp với một nút khác trên Lightning Network**. Trong kênh này, bạn có thể tự do Exchange Satoshi lên đến dung lượng của kênh.



### Kết nối tới một nút



Kết nối với các nút Lightning khác là hành động cơ bản nếu bạn muốn tham gia tích cực và hưởng lợi từ sức mạnh của Lightning.



Để kết nối với một nút ngang hàng (nút Lightning), bạn sẽ cần ba thông tin:




- Khóa công khai của nút**: Đây là mã định danh duy nhất của nút trong mạng Bitcoin;
- IP**: Địa chỉ IP của máy mà nút được cài đặt;
- PORT**: Cổng mở trên máy cho phép giao tiếp với nút này.



Bạn có thể tìm thấy các nút để kết nối trên [amboss](https://amboss.space/), một nền tảng liệt kê thông tin về các nút Lightning.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Hãy đảm bảo bạn kết nối với **các nút đáng tin cậy** để bảo toàn tính toàn vẹn của hệ thống của bạn. Sau đây là một số khuyến nghị để chọn kết nối phù hợp.





- Đa dạng hóa địa lý**: Kết nối với các nút ở các khu vực khác nhau.





- Uy tín**: Chọn các nút có tính khả dụng tốt.





- Sức chứa**: Chọn những nút có tính thanh khoản tốt.





- Phí**: Kiểm tra phí định tuyến.


### Mở kênh thanh toán


Để mở kênh thanh toán, hãy đảm bảo rằng bạn đã **kết nối** với nút ngang hàng, sau đó xác định **sức chứa** (số lượng satoshi) mà bạn muốn chặn trong kênh này.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Tạo ra một Lightning Invoice



Lightning Invoice đại diện cho một chuỗi ký tự thể hiện mong muốn nhận satoshi của bạn trong Lightning Wallet.


Việc tạo hóa đơn Lightning bằng nút riêng của bạn cho phép bạn bảo vệ dữ liệu (địa lý và cá nhân) và mang lại cho bạn quyền tự chủ 100% trong việc quản lý tiền của mình.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Trả tiền cho Lightning Invoice



```bash
lncli payinvoice <FACTURE>
```


### Đóng kênh



Có hai cách để đóng kênh đang hoạt động trên nút hiện tại của bạn.





- Đóng hợp tác**: Điều này báo hiệu mong muốn rút khỏi kênh thanh toán của nút của bạn, đảm bảo các tác vụ đang diễn ra được hoàn thành và dữ liệu được sao lưu để tránh mất tiền.


```
lncli closechannel <ID_CANAL>
```




- Đóng bắt buộc**: ⚠️ Nếu có thể, bạn nên tránh hành động này vì nó sẽ làm gián đoạn các quy trình đang diễn ra trong kênh thanh toán của bạn và làm tăng nguy cơ mất tiền.


```
lncli closechannel --force <ID_CANAL>
```


## Thực hành tốt nhất và an toàn cho nút LND của bạn.


An toàn là điều quan trọng nhất khi sử dụng nút Bitcoin/Lightning. Sau đây là một số điểm để tăng cường tính an toàn cho quá trình lắp đặt của bạn:





- Lưu trữ `cụm từ seed` của bạn ở nơi an toàn, ngoại tuyến.





- Sao lưu thường xuyên tệp `~/.LND/channel.backup`: Tệp này lưu trạng thái kênh của bạn mỗi khi một kênh mới được mở (hoặc một kênh cũ bị đóng) trên nút của bạn.


⚠️ Cho phép bạn khôi phục các kênh và thu hồi tiền bị chặn trong các kênh thanh toán trong trường hợp mất dữ liệu hoặc lỗi nút



Bạn có thể khôi phục tiền của mình bằng lệnh bên dưới bằng cách chỉ định đường dẫn sao lưu của tệp này:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Hãy đảm bảo rằng bạn đã lưu từ khôi phục và mật khẩu của Lightning Wallet.
- Hãy cập nhật hệ thống của bạn thường xuyên.



## Xử lý sự cố hiện tại


### Các vấn đề thường gặp




- Lỗi kết nối bitcoind**: Kiểm tra thông tin đăng nhập RPC của bạn
- Đồng bộ hóa bị chặn**: Kiểm tra kết nối Internet của bạn
- Lỗi quyền**: Kiểm tra quyền của thư mục `~/.LND`




Vậy là bạn đã đến phần cuối của hướng dẫn này. Nếu bạn muốn tìm hiểu thêm về Lightning, chúng tôi cung cấp khóa học giới thiệu này để giúp bạn hiểu rõ hơn về các khái niệm và hoạt động đằng sau Lightning Network.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb