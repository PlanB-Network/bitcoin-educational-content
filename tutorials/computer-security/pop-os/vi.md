---
name: Pop!_OS
description: Hướng dẫn cài đặt Pop!_OS, một bản phân phối Linux.
---

![cover](assets/cover.webp)



## Giới thiệu



Pop!OS là một hệ điều hành dựa trên Linux được phát triển bởi **System76**, một nhà sản xuất của Mỹ chuyên về máy tính dành cho các nhà phát triển, nhà thiết kế và người dùng cao cấp.



Được thiết kế để cung cấp một môi trường hiện đại, ổn định và hiệu năng cao, Pop!OS nổi bật với trải nghiệm đơn giản, các công cụ mạnh mẽ và tập trung mạnh vào năng suất.



### System76 là ai?



System76 là một công ty của Mỹ được thành lập năm 2005 và có trụ sở tại Denver, chuyên sản xuất máy tính xách tay, máy tính để bàn và máy chủ được thiết kế dành riêng cho hệ điều hành Linux.



Khác với các nhà sản xuất truyền thống, System76 phát triển các máy móc được thiết kế theo hướng mở, dễ sửa chữa và hướng tới sự tự do về phần mềm.



System76 không chỉ sản xuất máy tính.



Công ty này cũng phát triển:




- Pop!OS**, hệ điều hành dựa trên Linux do chính hãng phát triển;
- COSMIC**, môi trường máy tính để bàn hiện đại, hiệu năng cao được sử dụng bởi Pop!OS;
- Open Firmware**, một firmware mã nguồn mở dựa trên Coreboot;
- Công cụ dành cho nhà phát triển và nhà thiết kế.



Mục tiêu là cung cấp sự tích hợp phần cứng và phần mềm chất lượng cao, tương đương với hệ sinh thái của Apple, nhưng hoàn toàn mở và tập trung vào Linux.



## Một hệ thống hiện đại, ổn định và dễ tiếp cận.



Pop!OS được xây dựng trên nền tảng của Ubuntu, mang lại sự ổn định tuyệt vời, khả năng tương thích phần cứng rộng rãi và quyền truy cập vào một hệ sinh thái phần mềm khổng lồ.


Nó cung cấp một giao diện trang nhã, giao diện máy tính để bàn COSMIC, được thiết kế để mượt mà, trực quan và có thể tùy chỉnh, ngay cả đối với người dùng mới.



## Một lựa chọn lý tưởng cho các nhà phát triển, nhà thiết kế và người dùng khó tính.



Pop!OS được đánh giá cao đặc biệt bởi:





- các nhà phát triển (công cụ được cài đặt sẵn, quản lý lát gạch nâng cao),
- người dùng có card đồ họa Nvidia hoặc AMD,
- Sinh viên và các chuyên gia đang tìm kiếm một hệ thống đáng tin cậy,
- Người dùng Windows muốn thực hiện quá trình chuyển đổi đơn giản.



Nó bao gồm tính năng sắp xếp tự động, trung tâm phần mềm rõ ràng và các công cụ năng suất tích hợp để giúp việc sử dụng hàng ngày dễ dàng hơn.



## Những điểm nổi bật của Pop!OS





- Hiệu năng được tối ưu hóa** nhờ các bản cập nhật thường xuyên.
- Có hai phiên bản ISO khả dụng**: phiên bản tiêu chuẩn và phiên bản tối ưu cho Nvidia.
- Tăng cường bảo mật** (Mã hóa LUKS có sẵn khi cài đặt).
- Interface COSMIC** thiết kế tiện dụng và hiện đại.
- Tương thích cao** với phần mềm Ubuntu và Flatpak.



## Tải xuống POP!OS một cách an toàn



### 1. Điều kiện tiên quyết



Trước khi tải xuống và cài đặt POP!OS, bạn cần thực hiện một vài bước để chuẩn bị môi trường cài đặt một cách chính xác.



### Thiết bị cần thiết





- Máy tính tương thích**: Bộ xử lý Intel hoặc AMD, GPU Intel / AMD / Nvidia.
- Tối thiểu 4 GB RAM** (khuyến nghị 8 GB để sử dụng thoải mái).
- Dung lượng trống tối thiểu 20 GB** (khuyến nghị 40 GB trở lên).
- Cần một USB có dung lượng tối thiểu 4 GB** để tạo phương tiện cài đặt.



### Kết nối Internet



Kết nối ổn định rất hữu ích cho:





- Tải xuống ảnh ISO.
- Cài đặt bản cập nhật sau khi cài đặt xong.



Pop!OS có thể hoạt động mà không cần kết nối internet, nhưng quá trình cài đặt sẽ mượt mà hơn nhiều nếu có kết nối mạng.



### Sao lưu dữ liệu



Nếu bạn định thay thế hoặc sử dụng Pop!OS cùng với một hệ điều hành khác (Windows, Ubuntu, v.v.), tốt nhất nên sao lưu các tệp quan trọng trước khi tiến hành.



### Kiểm tra xem có card đồ họa Nvidia (nếu có) hay không.



Đối với máy tính được trang bị card đồ họa Nvidia, bạn cần tải xuống ảnh ISO đặc biệt có chứa trình điều khiển Nvidia.


Việc kiểm tra này rất đơn giản:





- bằng cách tham khảo thông số kỹ thuật của máy tính,
- hoặc bằng cách tra cứu kiểu card đồ họa trong cài đặt hệ thống.



### Tải xuống từ trang web chính thức



Bạn nên tải xuống ảnh ISO của Pop!OS trực tiếp từ trang chính thức của System76: [system76.com/pop](https://system76.com/pop/).



Trang này luôn cung cấp phiên bản mới nhất, được điều chỉnh phù hợp với phần cứng của bạn.



![capture](assets/fr/03.webp)



### Chọn phiên bản: Tiêu chuẩn hoặc Nvidia, hoặc Raspberry Pi (ARM64)



Pop!OS có ba phiên bản:



### Phiên bản tiêu chuẩn



Được đề xuất cho máy tính sử dụng:





- Bộ xử lý Intel hoặc AMD;
- GPU tích hợp của Intel hoặc AMD;
- một card đồ họa AMD Radeon.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Phiên bản Nvidia



Khuyến nghị sử dụng cho máy tính trang bị card đồ họa Nvidia.


Ảnh hệ thống này đã bao gồm trình điều khiển Nvidia, giúp việc cài đặt dễ dàng hơn và giảm thiểu các vấn đề về đồ họa.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Phiên bản Raspberry Pi (ARM64)



Dành cho Raspberry Pi 4 và 400 (bộ xử lý ARM).


Được điều chỉnh cho kiến trúc ARM, đây là phiên bản đặc biệt dành cho các máy tính mini này.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Tạo USB khởi động



Bạn có thể sử dụng một số công cụ, chẳng hạn như Balena Etcher:





- Tải xuống và cài đặt [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Mở Balena Etcher, sau đó chọn ảnh ISO của Pop!OS.
- Chọn USB làm thiết bị lưu trữ.
- Nhấp chuột vào Flash và đợi quá trình hoàn tất.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Cài đặt và bảo mật Pop!OS



### Khởi động từ USB





- Tắt máy tính đi.
- Cắm USB (chứa hệ điều hành Pop!OS) vào.
- Bật máy tính của bạn. Trên các máy tính đời mới, hệ thống sẽ tự động nhận diện USB khởi động. Nếu không, hãy khởi động lại bằng cách giữ phím truy cập BIOS/UEFI (thường là F2, F12 hoặc Delete, tùy thuộc vào thương hiệu).
  - Trong menu BIOS/UEFI, chọn USB của bạn làm thiết bị khởi động.
  - Lưu lại và khởi động lại.



### Khởi động quá trình cài đặt



Sau khi bạn chọn USB khởi động làm thiết bị khởi động, máy tính của bạn sẽ khởi động vào môi trường Pop!OS Live.



Chọn ngôn ngữ của bạn.



![Capture](assets/fr/10.webp)



Chọn địa điểm.



![Capture](assets/fr/11.webp)



Chọn ngôn ngữ để nhập liệu bằng bàn phím.



![Capture](assets/fr/12.webp)



Chọn bố cục bàn phím.



![Capture](assets/fr/13.webp)



Chọn tùy chọn `Cài đặt sạch` để cài đặt tiêu chuẩn. Đây là lựa chọn tốt nhất cho người dùng Linux mới, nhưng hãy lưu ý rằng nó sẽ xóa toàn bộ nội dung trên ổ đĩa đích. Ngoài ra, bạn có thể chọn `Thử chế độ Demo` để tiếp tục thử nghiệm Pop!OS trong môi trường thực tế.



![Capture](assets/fr/14.webp)



Chọn `Tùy chỉnh (Nâng cao)` để truy cập GParted. Công cụ này cho phép bạn cấu hình các tính năng nâng cao như khởi động kép, tạo phân vùng `/home` riêng biệt hoặc đặt phân vùng `/tmp` trên ổ đĩa khác.



Nhấp vào `Xóa và Cài đặt` để cài đặt Pop!OS trên ổ đĩa đã chọn.



![Capture](assets/fr/15.webp)



### Cấu hình tài khoản người dùng



Phần tiếp theo của chương trình cài đặt sẽ hướng dẫn bạn tạo tài khoản người dùng để đăng nhập vào hệ điều hành mới.



Hãy cung cấp họ tên đầy đủ (có thể bao gồm bất kỳ loại chữ nào bạn chọn, chữ hoa hoặc chữ thường), cũng như tên người dùng (phải viết thường):



![Capture](assets/fr/16.webp)



Sau khi tài khoản được tạo, bạn sẽ được yêu cầu thiết lập mật khẩu mới.



![Capture](assets/fr/17.webp)



### Mã hóa toàn bộ ổ đĩa



Mã hóa ổ đĩa hệ thống không bắt buộc, nhưng nó đảm bảo an toàn dữ liệu người dùng trong trường hợp ai đó truy cập trái phép vào thiết bị.



Bạn có thể mã hóa ổ đĩa bằng mật khẩu đăng nhập của mình bằng cách chọn ô "Mật khẩu mã hóa giống với mật khẩu tài khoản người dùng". Bạn cũng có thể bỏ chọn ô này và chọn "Đặt mật khẩu" ở phía dưới. Chọn "Không mã hóa" để bỏ qua quá trình mã hóa ổ đĩa.



![Capture](assets/fr/18.webp)



Nếu bạn đã chọn nút "Đặt mật khẩu", bạn sẽ thấy một lời nhắc bổ sung để đặt mật khẩu mã hóa của mình.



Hãy chuyển sang bước tiếp theo trong chương trình cài đặt. Pop!OS sẽ bắt đầu cài đặt lên ổ đĩa.



![Capture](assets/fr/19.webp)



Sau khi quá trình cài đặt hoàn tất, hãy khởi động lại máy tính và đăng nhập để hoàn tất quá trình cấu hình tài khoản người dùng.



Nếu bạn đã thay đổi thứ tự khởi động để ưu tiên USB cài đặt Live khi khởi động, hãy tắt máy tính hoàn toàn và tháo USB cài đặt. Nếu bạn đang ở chế độ khởi động kép, hãy nhấn các phím thích hợp để truy cập cấu hình và chọn ổ đĩa chứa bản cài đặt Pop!OS.



![Capture](assets/fr/20.webp)



### Đồ họa NVIDIA



Nếu bạn đã cài đặt từ file ISO của Intel/AMD và hệ thống của bạn có card đồ họa rời NVIDIA, hoặc nếu bạn đã thêm card đồ họa rời sau này, bạn sẽ cần cài đặt trình điều khiển cho card của mình theo cách thủ công để đạt được hiệu suất tối ưu. Chạy lệnh sau trong cửa sổ dòng lệnh để cài đặt trình điều khiển:



```bash
sudo apt install system76-driver-nvidia
```



Bạn cũng có thể cài đặt trình điều khiển đồ họa NVIDIA từ Pop!_Shop.



![Capture](assets/fr/20.webp)



## Cài đặt các công cụ thiết yếu



Pop!OS cung cấp nhiều phần mềm thông qua Pop!Shop, nhưng nhiều công cụ thiết yếu cũng có thể được cài đặt thông qua terminal bằng lệnh `apt` hoặc `flatpak`. Dưới đây là cách cài đặt các công cụ quan trọng để có một môi trường làm việc hoàn chỉnh.



### Lắp đặt thiết bị đầu cuối



| Outil                        | Description                                | Commande d’installation                         |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox                      | Navigateur web libre et populaire          | `sudo apt install firefox`                      |
| Brave                        | Navigateur web axé sur la confidentialité  | Installation via Pop!_Shop ou site officiel     |
| Visual Studio Code (VS Code) | Éditeur de code puissant pour développeurs | `flatpak install flathub com.visualstudio.code` |
| Git                          | Gestionnaire de versions                   | `sudo apt install git`                          |
| Flatpak                      | Gestionnaire de paquets alternatif         | `sudo apt install flatpak`                      |
| VLC                          | Lecteur multimédia polyvalent              | `sudo apt install vlc`                          |
| GNOME Terminal               | Terminal par défaut                        | Préinstallé sur Pop!OS                          |
| Curl                         | Outil de transfert de données en ligne     | `sudo apt install curl`                         |
| Wget                         | Téléchargement de fichiers via HTTP/FTP    | `sudo apt install wget`                         |
| Docker                       | Conteneurisation d’applications            | Installation via script officiel ou `apt`       |
| Node.js                      | Environnement JavaScript côté serveur      | Installation via `apt` ou NodeSource            |
| Python3                      | Langage de programmation                   | `sudo apt install python3 python3-pip`          |
| GIMP                         | Éditeur d’image avancé                     | `sudo apt install gimp`                         |
| Thunderbird                  | Client mail                                | `sudo apt install thunderbird`                  |
| Transmission                 | Client BitTorrent léger                    | `sudo apt install transmission-gtk`             |
| Htop                         | Moniteur de système interactif             | `sudo apt install htop`                         |

### Cài đặt thông qua Pop! Shop (giao diện đồ họa)





- Mở **Pop!_Shop** từ menu chính.
- Sử dụng thanh tìm kiếm để tìm các ứng dụng bạn muốn (ví dụ: "Brave").
- Nhấp vào **Cài đặt** cho mỗi ứng dụng.
- Pop!_Shop tự động quản lý các phụ thuộc và cập nhật.



## Cập nhật hệ thống



### Phương án 1: Thông qua giao diện người dùng đồ họa (GUI)



Pop!OS sở hữu trình quản lý cập nhật đồ họa đơn giản và trực quan.



1. Nhấp vào **menu chính** (biểu tượng ở góc dưới bên trái).


2. Mở **"Pop!_Shop"**.


3. Trong Pop!_Shop, hãy nhấp vào tab **"Cập nhật"**.


4. Hệ thống sẽ tự động kiểm tra các bản cập nhật có sẵn.


5. Nhấp vào **"Cập nhật tất cả"** để bắt đầu cài đặt bản cập nhật.


6. Nhập mật khẩu của bạn nếu được yêu cầu.


7. Hãy để quá trình hoàn tất, sau đó khởi động lại nếu cần.



### Phương án 2: Qua thiết bị đầu cuối



Mở cửa sổ dòng lệnh và gõ:



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Quản lý người dùng



Chúng tôi khuyên bạn nên sử dụng tài khoản người dùng thông thường với quyền sudo cho các hoạt động hàng ngày.



Để tạo người dùng mới:



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Đăng xuất, sau đó đăng nhập lại bằng tài khoản mới này.



### Quản lý trình điều khiển đồ họa





- Đối với card đồ họa Nvidia, hãy kiểm tra xem trình điều khiển độc quyền đã được cài đặt chưa:



```bash
sudo apt install system76-driver-nvidia
```





- Đối với AMD/Intel, trình điều khiển thường được cài đặt sẵn theo mặc định.



### Kích hoạt tường lửa (UFW)



Pop!OS không chặn lưu lượng mạng theo mặc định. Kích hoạt UFW để tăng cường bảo mật:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Cấu hình cập nhật tự động



Để cập nhật hệ thống mà không cần can thiệp thủ công:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Tùy chỉnh ngoại hình và hành vi





- Mở **Cài đặt hệ thống** → **Giao diện** để chọn chủ đề sáng hoặc tối.
- Cấu hình các góc hoạt động, hiệu ứng động và phần mở rộng thông qua trình quản lý COSMIC.
- Điều chỉnh bố cục màn hình nền để tối ưu hóa quy trình làm việc của bạn.



### Cấu hình sao lưu tự động



Pop!OS tích hợp các công cụ như Deja Dup để sao lưu dữ liệu:





- Khởi chạy chức năng **Sao lưu** từ menu.
- Chọn ổ đĩa ngoài hoặc vị trí mạng.
- Lên lịch sao lưu dữ liệu định kỳ.



### Cài đặt các tiện ích mở rộng hữu ích cho GNOME/COSMIC



Dưới đây là một vài tiện ích mở rộng được đề xuất để nâng cao trải nghiệm người dùng:





- Dash to Dock**: thanh ứng dụng luôn hiển thị.
- GSConnect**: đồng bộ hóa với Android.
- Chỉ báo Clipboard**: quản lý clipboard nâng cao.



Cài đặt chúng thông qua:



```bash
sudo apt install gnome-shell-extensions
```



Sau đó, hãy kích hoạt chúng trong phần cài đặt.



### Tối ưu hóa quản lý bộ nhớ và bộ nhớ ảo



Kiểm tra trạng thái đổi hàng của bạn:



```bash
swapon --show
```



Nếu cần, hãy tăng kích thước bộ nhớ ảo hoặc cấu hình tệp ảo:



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Thêm dòng này vào tệp `/etc/fstab` để tự động gắn kết.



## Quản lý gói và kho lưu trữ



### Hiểu về nguồn gốc gói hàng



Pop!OS, dựa trên Ubuntu, chủ yếu sử dụng:





- Kho lưu trữ chính thức của Ubuntu**: nơi chứa phần mềm ổn định nhất.
- Kho lưu trữ System76**: dành cho trình điều khiển, phần mềm nhúng và các công cụ chuyên dụng.
- Flatpak**: truy cập vào nhiều ứng dụng được chạy trong môi trường biệt lập.
- Snap** (tùy chọn): một định dạng gói phổ biến khác.



---

### Thêm và quản lý kho lưu trữ PPA



Để cài đặt phần mềm thường xuyên được cập nhật, có thể thêm một số PPA (Kho lưu trữ gói cá nhân):



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Phần kết luận



Pop!OS là một bản phân phối Linux hiện đại, ổn định, phù hợp cho cả người mới bắt đầu và người dùng nâng cao.



Nhờ giao diện COSMIC trực quan và các công cụ tích hợp, nó mang đến trải nghiệm mượt mà và hiệu quả, dù là để phát triển, sáng tạo hay sử dụng hàng ngày.



Hướng dẫn này bao gồm các giai đoạn chính: chuẩn bị, tải xuống, cài đặt, thiết lập ban đầu và các công cụ cần thiết.



Hãy thoải mái khám phá Pop!OS hơn nữa và tùy chỉnh môi trường của bạn để tận dụng tối đa các tính năng của nó.