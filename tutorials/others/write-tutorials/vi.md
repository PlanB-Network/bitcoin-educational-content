---
name: Đóng góp - Hướng dẫn
description: Làm thế nào để đề xuất một hướng dẫn mới trên Mạng PlanB?
---
![cover](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn tài nguyên giáo dục hàng đầu về Bitcoin, bằng càng nhiều ngôn ngữ càng tốt. Tất cả nội dung được công bố trên trang web là mã nguồn mở và được lưu trữ trên GitHub, điều này tạo cơ hội cho bất kỳ ai tham gia vào việc làm giàu cho nền tảng. Đóng góp có thể có nhiều hình thức: chỉnh sửa và đọc lại các văn bản hiện có, dịch sang ngôn ngữ khác, cập nhật thông tin, hoặc tạo mới các hướng dẫn chưa có trên trang web của chúng tôi.

Trong hướng dẫn này, tôi sẽ giải thích cách chỉnh sửa mục "Hướng dẫn" của Mạng PlanB. Nếu bạn muốn thêm một hướng dẫn mới hoặc cải thiện một hướng dẫn hiện có, bài viết này dành cho bạn! Chúng ta sẽ xem xét chi tiết cách đóng góp cho Mạng PlanB qua GitHub, trong khi sử dụng Obsidian, một công cụ viết.

## Điều kiện tiên quyết

Để đóng góp cho Mạng PlanB, bạn có 3 lựa chọn tùy thuộc vào kinh nghiệm của bạn với GitHub:
1. **Người dùng có kinh nghiệm**: Tiếp tục với phương pháp thường dùng của bạn và tham khảo hướng dẫn này để làm quen với cấu trúc của kho lưu trữ PlanB, các yêu cầu cụ thể và quy trình làm việc.
2. **Người mới bắt đầu sẵn sàng học hỏi**: Tôi khuyên bạn nên thiết lập môi trường làm việc của riêng mình. Theo dõi hướng dẫn này cũng như các bài viết khác dưới đây của chúng tôi để được hướng dẫn từng bước một.
3. **Người mới bắt đầu cho các đóng góp nhỏ**: Đối với các nhiệm vụ yêu cầu ít sửa đổi, như đọc lại hoặc sửa lỗi, sử dụng trực tiếp giao diện web của GitHub mà không cần thiết lập môi trường địa phương đầy đủ.

**Phần mềm cần thiết để theo dõi hướng dẫn của tôi:**
- [GitHub Desktop](https://desktop.github.com/)
- [Obsidian](https://obsidian.md/)
- Một trình soạn thảo mã ([VSC](https://code.visualstudio.com/) hoặc [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/1.webp)
**Điều kiện tiên quyết trước khi bắt đầu hướng dẫn:**
- Có một [tài khoản GitHub](https://github.com/signup).
- Có một fork của [kho lưu trữ nguồn PlanB Network](https://github.com/PlanB-Network/bitcoin-educational-content).
- Có [một hồ sơ giáo sư trên Mạng PlanB](https://planb.network/professors) (chỉ khi bạn đề xuất một hướng dẫn đầy đủ).

**Nếu bạn cần trợ giúp để đạt được các điều kiện tiên quyết này, các hướng dẫn khác của tôi sẽ hướng dẫn bạn:**
**[Hiểu biết về Git và GitHub](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
**[Tạo một tài khoản GitHub](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Thiết lập môi trường làm việc của bạn](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**
**[Tạo một hồ sơ giáo sư](https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4)**
## Loại nội dung nào để viết trên Mạng PlanB?
Chúng tôi chủ yếu tìm kiếm các hướng dẫn về các công cụ liên quan đến Bitcoin hoặc hệ sinh thái của nó. Những nội dung này có thể được tổ chức xung quanh sáu danh mục chính:
- Ví;
- Node;
- Đào;
- Thương nhân;
- Trao đổi;
- Riêng tư.
![tutorial](assets/2.webp)
Ngoài những chủ đề cụ thể liên quan đến Bitcoin, PlanB cũng tìm kiếm các đóng góp về các chủ đề nổi bật về chủ quyền cá nhân, như:
- Công cụ mã nguồn mở;
- Tin học;
- Mật mã học;
- Năng lượng;
- Toán học;
- Kinh tế;
- DIYs;
- LifeHacking...
Ví dụ, hiện tại chúng tôi có các hướng dẫn về Tails, Nostr, hoặc GrapheneOS. Những công cụ này không trực tiếp liên quan đến Bitcoin, nhưng chúng là những hệ thống có thể thu hút chúng ta trong quá trình tìm kiếm quyền tự chủ trong thế giới số. Những nội dung này có thể được tích hợp vào một tiểu mục của mục "Khác".

Bạn có thể lựa chọn thiết kế một hướng dẫn từ đầu hoặc sử dụng một hướng dẫn đã được công bố trước đó trên trang web của bạn (miễn là bạn sở hữu bản quyền) để chia sẻ nó trên Mạng PlanB, kèm theo liên kết đến bài viết gốc.

Dù bạn chọn phương án nào, hãy nhớ rằng tất cả nội dung được công bố trên Mạng PlanB đều nằm dưới giấy phép tự do [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/). Giấy phép này cho phép bất kỳ ai cũng có thể sao chép và, có khả năng, chỉnh sửa nội dung của bạn, miễn là nguồn gốc được ghi công đúng cách.

## Làm thế nào để đề xuất một hướng dẫn trên Mạng PlanB?

Một khi mọi thứ đã sẵn sàng, và môi trường địa phương của bạn đã được thiết lập tốt với bản fork của riêng bạn của Mạng PlanB, bạn có thể bắt đầu thêm hướng dẫn.

### Tạo một nhánh mới

- Mở trình duyệt của bạn và truy cập vào trang của bản fork PlanB của bạn. Đây là bản fork bạn đã thiết lập trên GitHub. URL của bản fork của bạn nên trông giống như: `https://github.com/[tên-người-dùng-của-bạn]/bitcoin-educational-content`:
![hướng dẫn](assets/3.webp)
- Đảm bảo bạn đang ở nhánh chính `dev` sau đó nhấp vào nút `Sync fork`. Nếu bản fork của bạn không cập nhật, GitHub sẽ đề nghị cập nhật nhánh của bạn. Tiến hành cập nhật này. Nếu ngược lại, nhánh của bạn đã cập nhật, GitHub sẽ thông báo cho bạn:
![hướng dẫn](assets/4.webp)
- Mở phần mềm GitHub Desktop và đảm bảo bản fork của bạn được chọn đúng cách ở góc trên bên trái của cửa sổ:
![hướng dẫn](assets/5.webp)
- Nhấp vào nút `Fetch origin`. Nếu kho lưu trữ địa phương của bạn đã cập nhật, GitHub Desktop sẽ không đề xuất thêm hành động nào. Nếu không, tùy chọn `Pull origin` sẽ xuất hiện. Nhấp vào nút này để cập nhật kho lưu trữ địa phương của bạn: ![hướng dẫn](assets/6.webp)
- Đảm bảo rằng bạn đang ở nhánh chính `dev`:
![hướng dẫn](assets/7.webp)
- Nhấp vào nhánh này, sau đó nhấp vào nút `New Branch`:
![hướng dẫn](assets/8.webp)
- Đảm bảo nhánh mới được dựa trên kho lưu trữ nguồn, tức là `PlanB-Network/bitcoin-educational-content`.
- Đặt tên cho nhánh của bạn sao cho tiêu đề rõ ràng về mục đích của nó, sử dụng dấu gạch ngang để phân cách từng từ. Ví dụ, giả sử mục tiêu của chúng ta là viết một hướng dẫn về việc sử dụng phần mềm Sparrow Wallet. Trong trường hợp này, nhánh làm việc dành riêng cho việc viết hướng dẫn này có thể được đặt name: `tuto-sparrow-wallet-loic`. Sau khi nhập tên phù hợp, nhấp vào `Create branch` để xác nhận việc tạo nhánh:
![hướng dẫn](assets/9.webp)
- Bây giờ nhấp vào nút `Publish branch` để lưu nhánh làm việc mới của bạn trên bản fork trực tuyến trên GitHub:
![hướng dẫn](assets/10.webp)
Bây giờ, trên GitHub Desktop, bạn nên ở trên nhánh mới của mình. Điều này có nghĩa là tất cả các thay đổi được thực hiện địa phương trên máy tính của bạn sẽ được ghi lại độc quyền trên nhánh cụ thể này. Ngoài ra, miễn là nhánh này vẫn được chọn trên GitHub Desktop, các tệp được hiển thị địa phương trên máy của bạn tương ứng với những tệp của nhánh này (`tuto-sparrow-wallet-loic`), và không phải là những tệp của nhánh chính (`dev`).
![hướng dẫn](assets/11.webp)
Đối với mỗi bài viết mới bạn muốn xuất bản, bạn sẽ cần tạo một nhánh mới từ `dev`. Một nhánh trong Git là một phiên bản song song của dự án, cho phép bạn thực hiện các thay đổi mà không ảnh hưởng đến nhánh chính, cho đến khi công việc sẵn sàng để được hợp nhất.
### Thêm hướng dẫn

Bây giờ nhánh làm việc đã được tạo, đã đến lúc tích hợp hướng dẫn mới của bạn.
- Mở trình quản lý tệp của bạn và điều hướng đến thư mục `bitcoin-educational-content`, đại diện cho bản sao cục bộ của kho lưu trữ của bạn. Bạn nên tìm thấy nó dưới `Documents\GitHub\bitcoin-educational-content`. Trong thư mục này, bạn cần tìm thư mục phụ thích hợp để đặt hướng dẫn của mình. Cách tổ chức các thư mục phản ánh các phần khác nhau của trang web Mạng lưới PlanB. Trong ví dụ của chúng tôi, vì chúng tôi muốn thêm một hướng dẫn về Sparrow Wallet, nên thích hợp để đi đến đường dẫn sau: `bitcoin-educational-content\tutorials\wallet` tương ứng với phần `WALLET` trên trang web: ![hướng dẫn](assets/12.webp)
- Trong thư mục `wallet`, bạn cần tạo một thư mục mới cụ thể dành riêng cho hướng dẫn của bạn. Tên của thư mục này phải gợi lên phần mềm được đề cập trong hướng dẫn, đảm bảo kết nối các từ bằng dấu gạch ngang. Đối với ví dụ của tôi, thư mục sẽ được đặt tên là `sparrow-wallet`:
![hướng dẫn](assets/13.webp)
- Trong thư mục phụ mới này dành riêng cho hướng dẫn của bạn, cần thêm một số yếu tố:
	- Tạo một thư mục `assets`, dành để nhận tất cả các hình minh họa cần thiết cho hướng dẫn của bạn;
    - Trong thư mục `assets` này, bạn cần tạo 8 thư mục phụ có tên là `fr`, `de`, `en`, `it`, `es`, `ja`, `vi`, và `pt`, để phân loại hình ảnh theo ngôn ngữ tương ứng. Bạn cũng phải thêm một thư mục phụ `notext` cho các hình ảnh không cần dịch, chẳng hạn như ảnh chụp màn hình;
	- Một tệp `tutorial.yml` phải được tạo để ghi lại các chi tiết liên quan đến hướng dẫn của bạn;
	- Một tệp định dạng markdown cần được tạo để viết nội dung thực sự của hướng dẫn của bạn. Tệp này phải được đặt tên theo mã ngôn ngữ của bài viết. Ví dụ, cho một hướng dẫn viết bằng tiếng Pháp, tệp nên được gọi là `fr.md`.
![hướng dẫn](assets/14.webp)
- Để tóm tắt, đây là cấu trúc các tệp cần tạo:
```plaintext
bitcoin-educational-content/
└── tutorials/
    └── wallet/ (cần chỉnh sửa với danh mục phù hợp)
        └── sparrow-wallet/ (cần chỉnh sửa với tên của hướng dẫn)
            ├── assets/
            │   ├── fr/
            │   ├── de/
            │   ├── en/
            │   ├── it/
            │   ├── es/
            │   ├── pt/
            |   ├── ja/
            |   ├── vi/
            │   └── notext/
            ├── tutorial.yml
            └── fr.md (cần chỉnh sửa theo mã ngôn ngữ phù hợp)
```

- Để bắt đầu, mở tệp `tutorial.yml` của bạn bằng trình chỉnh sửa mã.
- Điền vào mỗi trường với thông tin được chỉ định dưới đây:
- **builder**: Nhập tên của công ty sản xuất phần mềm mà bạn đang tạo hướng dẫn;
- **tags**: Xác định một loạt các từ khóa liên quan chặt chẽ đến chủ đề của bài viết của bạn, để tạo điều kiện cho việc tìm kiếm và lập chỉ mục;
- **category**: Chọn một phân loại phụ phù hợp trong số những lựa chọn có sẵn trên trang PlanB, dựa vào nội dung của hướng dẫn của bạn. Ví dụ, đối với một hướng dẫn trong mục `WALLET`, các lựa chọn có sẵn là `Desktop`, `Hardware`, và `Mobile`;
- **level**: Chỉ định mức độ khó của hướng dẫn của bạn bằng cách chọn một trong bốn phân loại sau:
    - Người mới bắt đầu (`beginner`),
    - Trung cấp (`intermediary`),
    - Nâng cao (`advanced`),
    - Chuyên gia (`expert`).
- **professor**: Cung cấp ID người đóng góp của bạn như hiển thị trên hồ sơ giáo viên của bạn. Để biết thêm chi tiết, tham khảo [hướng dẫn tương ứng](https://planb.network/fr/tutorials/others/create-teacher-profile);
- **link** (tùy chọn): Trong trường hợp bạn muốn ghi công một trang web nguồn cho hướng dẫn bạn đang phát triển, như trang cá nhân của bạn, đây là nơi bạn có thể thêm liên kết liên quan.
![tutorial](assets/15.webp)
- Sau khi bạn hoàn thành việc chỉnh sửa tệp `tutorial.yml` của mình, lưu tài liệu của bạn bằng cách nhấp vào `File > Save`:
![tutorial](assets/16.webp)
- Bây giờ bạn có thể đóng trình soạn thảo mã của mình.
- Trong thư mục `assets`, bạn phải thêm một tệp có tên là `logo.webp`, sẽ được sử dụng làm hình thu nhỏ cho bài viết của bạn. Hình ảnh này phải ở định dạng `.webp` và phải tuân thủ kích thước vuông để hài hòa với giao diện người dùng. Bạn có tự do chọn logo của phần mềm được đề cập trong hướng dẫn hoặc bất kỳ hình ảnh liên quan nào khác, miễn là không vi phạm bản quyền. Ngoài ra, cũng thêm một hình ảnh có tiêu đề `cover.webp` tại cùng một vị trí. Hình ảnh này sẽ được hiển thị ở đầu hướng dẫn của bạn. Đảm bảo rằng hình ảnh này, giống như logo, tuân thủ quyền sử dụng và phù hợp với bối cảnh của hướng dẫn của bạn:
![tutorial](assets/17.webp)
- Bây giờ, bạn có thể mở tệp sẽ chứa hướng dẫn của bạn, được đặt tên theo mã ngôn ngữ của bạn, như `fr.md`. Đi đến Obsidian, ở phía bên trái của cửa sổ, cuộn qua cây thư mục đến thư mục của hướng dẫn của bạn và đến tệp bạn muốn tìm:
![tutorial](assets/18.webp)
- Nhấp vào tệp để mở nó:
![tutorial](assets/19.webp)
- Chúng ta sẽ bắt đầu bằng cách điền vào phần `Properties` ở đầu tài liệu. Nếu phần này không có trong tệp của bạn (nếu tài liệu hoàn toàn trống), bạn có thể sao chép nó từ một hướng dẫn khác đã tồn tại: ![tutorial](assets/20.webp)
- Bạn cũng có thể thêm nó một cách thủ công theo cách này bằng trình soạn thảo mã của bạn:
```markdown
---
name: [Tiêu đề]
description: [Mô tả]
---
```
![tutorial](assets/21.webp)
- Điền vào tên của hướng dẫn của bạn và một mô tả ngắn gọn về nó:
![tutorial](assets/22.webp)
- Sau đó thêm hình ảnh bìa của bạn ở đầu hướng dẫn. Để làm điều này, gõ:
```markdown
![cover-sparrow](assets/cover.webp)
```
- Cú pháp này sẽ hữu ích mỗi khi cần thêm một hình ảnh vào hướng dẫn của bạn. Dấu chấm than chỉ ra rằng đó là một hình ảnh, với văn bản thay thế (alt) được chỉ định giữa các dấu ngoặc vuông. Đường dẫn đến hình ảnh được chỉ định giữa các dấu ngoặc đơn:
![tutorial](assets/23.webp)
- Tiếp tục viết hướng dẫn của bạn bằng cách viết nội dung của bạn. Khi bạn muốn tích hợp một tiêu đề phụ, áp dụng định dạng markdown thích hợp bằng cách thêm tiền tố cho văn bản với `##`:
![tutorial](assets/24.webp)

### Làm thế nào để thêm sơ đồ vào hướng dẫn?
Các thư mục con ngôn ngữ trong thư mục `assets` được thiết kế để tổ chức các sơ đồ và hình ảnh minh họa sẽ đi kèm với hướng dẫn của bạn. Nếu hình ảnh của bạn bao gồm văn bản, hãy chắc chắn dịch chúng cho mỗi ngôn ngữ liên quan để nội dung của bạn có thể tiếp cận được với khán giả quốc tế. Đối với các sơ đồ không có văn bản để dịch hoặc ảnh chụp màn hình, đặt chúng trực tiếp vào thư mục con `notext`. ![hướng dẫn](assets/25.webp)
Để đặt tên cho hình ảnh của bạn, chỉ cần đặt số theo thứ tự xuất hiện trong hướng dẫn. Ví dụ, đặt tên hình ảnh đầu tiên của bạn là `1.webp`, hình ảnh thứ hai là `2.webp`, và cứ thế tiếp tục.

Nếu cùng một sơ đồ được dịch sang nhiều ngôn ngữ, giữ nguyên tên tệp cho các bản dịch khác nhau trong các thư mục ngôn ngữ, như `en/1.webp`, `fr/1.webp`, `pt/1.webp`, v.v.

Bạn có lựa chọn sử dụng các định dạng hình ảnh khác nhau như `jpeg`, `png`, hoặc `webp`. Được khuyến nghị chọn định dạng `webp` để hình ảnh ít nặng hơn.
![hướng dẫn](assets/26.webp)
Để chèn một sơ đồ vào tài liệu của bạn, sử dụng lệnh sau trong Markdown, đảm bảo chỉ định văn bản thay thế phù hợp và đường dẫn chính xác của hình ảnh:
```markdown
![sparrow](assets/notext/1.webp)
```
Dấu chấm than ở đầu chỉ ra rằng đó là một hình ảnh. Văn bản thay thế, giúp hỗ trợ khả năng tiếp cận và SEO, được đặt giữa các dấu ngoặc vuông. Cuối cùng, đường dẫn đến hình ảnh được chỉ định giữa các dấu ngoặc đơn: ![hướng dẫn](assets/27.webp)
Nếu bạn muốn tạo sơ đồ của riêng mình, hãy chắc chắn tuân thủ bảng màu đồ họa của PlanB Network để đảm bảo tính nhất quán về mặt hình ảnh:
- **Phông chữ**: Sử dụng [Rubik](https://fonts.google.com/specimen/Rubik);
- **Màu sắc**:
	- Cam: #FF5C00
	- Đen: #000000
	- Trắng: #FFFFFF

**Là điều bắt buộc rằng tất cả hình ảnh được tích hợp vào hướng dẫn của bạn phải không vi phạm bản quyền hoặc tuân thủ giấy phép của tệp nguồn**. Ngoài ra, tất cả các sơ đồ được công bố trên PlanB Network đều được cung cấp dưới giấy phép CC-BY-SA, giống như văn bản.

**-> Mẹo:** Khi chia sẻ tệp công khai, như hình ảnh, điều quan trọng là loại bỏ bất kỳ metadata không cần thiết nào. Điều này có thể chứa thông tin nhạy cảm, như dữ liệu vị trí, ngày tạo, hoặc chi tiết về tác giả. Để bảo vệ sự riêng tư, bạn nên loại bỏ metadata này. Để đơn giản hóa thao tác này, bạn có thể sử dụng các công cụ chuyên biệt như [Exif Cleaner](https://exifcleaner.com/), cung cấp khả năng làm sạch metadata của tài liệu chỉ với một thao tác kéo và thả.

### Làm thế nào để lưu và đẩy hướng dẫn?

Một khi bạn đã hoàn thành việc viết hướng dẫn của mình bằng ngôn ngữ bạn chọn, bước tiếp theo là gửi một **Pull Request**. Quản trị viên sau đó sẽ thêm các bản dịch còn thiếu của hướng dẫn của bạn, nhờ vào phương pháp dịch tự động của chúng tôi.

- Để tiến hành với Pull Request, mở phần mềm GitHub Desktop.
- Phần mềm sẽ tự động phát hiện các thay đổi bạn đã thực hiện cục bộ so với kho lưu trữ gốc. Trước khi tiếp tục, hãy kiểm tra cẩn thận ở phía bên trái giao diện rằng những thay đổi này chính xác tương ứng với những gì bạn mong đợi: ![hướng dẫn](assets/28.webp)
- Thêm một tiêu đề cho lần commit của bạn, sau đó nhấp vào nút màu xanh `Commit to [nhánh của bạn]` để xác nhận những thay đổi này: ![hướng dẫn](assets/29.webp)
Một commit là một lưu của các thay đổi được thực hiện đối với nhánh, đi kèm với một thông điệp mô tả, cho phép theo dõi sự phát triển của một dự án theo thời gian. Do đó, đó là một loại điểm kiểm tra trung gian.
- Sau đó, nhấn vào nút `Push origin`. Điều này sẽ gửi commit của bạn đến fork của bạn: ![hướng dẫn](assets/30.webp) - Nếu bạn chưa hoàn thành hướng dẫn của mình, bạn có thể quay lại sau và tạo các commit mới.
- Nếu bạn đã hoàn thành chỉnh sửa cho nhánh này, bây giờ hãy nhấn vào nút `Preview Pull Request`: ![hướng dẫn](assets/31.webp)
- Bạn có thể kiểm tra lần cuối cùng xem các chỉnh sửa của mình có chính xác không, sau đó nhấn vào nút `Create pull request`:
![hướng dẫn](assets/32.webp)
Một Pull Request là một yêu cầu được tạo ra để tích hợp các thay đổi từ nhánh của bạn vào nhánh chính của kho lưu trữ PlanB Network, cho phép xem xét và thảo luận về các thay đổi trước khi chúng được hợp nhất.

- Bạn sẽ được tự động chuyển hướng trong trình duyệt của mình đến GitHub trên trang chuẩn bị Pull Request của bạn:
![hướng dẫn](assets/33.webp)
- Cung cấp một tiêu đề ngắn gọn tóm tắt các chỉnh sửa bạn muốn hợp nhất với kho lưu trữ nguồn.
- Thêm một bình luận ngắn gọn mô tả những thay đổi này.
- Nhấn vào nút màu xanh `Create pull request` để xác nhận yêu cầu hợp nhất:
![hướng dẫn](assets/34.webp)
PR của bạn sau đó sẽ hiển thị trong tab `Pull Request` của kho lưu trữ chính của PlanB Network. Bây giờ, tất cả những gì bạn cần làm là chờ đợi cho đến khi một quản trị viên liên hệ với bạn để xác nhận việc hợp nhất đóng góp của bạn hoặc yêu cầu bất kỳ chỉnh sửa bổ sung nào.
![hướng dẫn](assets/35.webp)
Sau khi hợp nhất PR của bạn với nhánh chính, bạn nên xóa nhánh làm việc của mình (`tuto-sparrow-wallet`) để duy trì lịch sử sạch sẽ trên fork của bạn. GitHub sẽ tự động cung cấp cho bạn tùy chọn này trên trang của PR của bạn:
![hướng dẫn](assets/36.webp)
Trên phần mềm GitHub Desktop, bạn có thể chuyển lại về nhánh chính của fork của mình (`dev`).
![hướng dẫn](assets/7.webp)
Nếu bạn muốn thực hiện chỉnh sửa đối với đóng góp của mình sau khi đã gửi PR, quy trình cần tuân theo phụ thuộc vào trạng thái hiện tại của PR của bạn:
- Nếu PR của bạn vẫn đang mở và chưa được hợp nhất, thực hiện các chỉnh sửa cục bộ trong khi vẫn ở trên cùng một nhánh. Một khi các chỉnh sửa được hoàn thiện, sử dụng nút `Push origin` để thêm một commit mới vào PR vẫn đang mở của bạn;
- Trong trường hợp PR của bạn đã được hợp nhất với nhánh chính, bạn sẽ cần thực hiện lại quy trình từ đầu bằng cách tạo một nhánh mới, sau đó gửi một PR mới. Đảm bảo rằng kho lưu trữ cục bộ của bạn được đồng bộ hóa với kho lưu trữ nguồn của PlanB Network trước khi tiến hành.
