---
name: PlanB Giáo Sư
description: Làm thế nào để thêm hồ sơ giáo sư của bạn trên Mạng PlanB?
---
![cover](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn tài nguyên giáo dục hàng đầu về Bitcoin, bằng càng nhiều ngôn ngữ khả dĩ. Tất cả nội dung được công bố trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, điều này cho phép bất kỳ ai cũng có thể tham gia vào việc làm giàu cho nền tảng. Đóng góp có thể nhận nhiều hình thức: sửa chữa và hiệu đính các văn bản hiện có, sản xuất các khóa học đào tạo, dịch sang ngôn ngữ khác, cập nhật thông tin, hoặc tạo mới các hướng dẫn chưa có trên trang web của chúng tôi.

Nếu bạn muốn thêm một hướng dẫn hoàn chỉnh mới hoặc một khóa học trên Mạng PlanB, bạn sẽ cần tạo hồ sơ giáo sư của mình. Điều này sẽ cho phép bạn được ghi công đúng mức cho nội dung bạn sản xuất trên trang web.
![tutorial](assets/1.webp)
Nếu bạn đã từng đóng góp cho Mạng PlanB, có lẽ bạn đã có ID người đóng góp. Bạn có thể tìm thấy nó trong thư mục giáo sư của mình có thể truy cập [qua trang này](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors). Nếu đây là trường hợp, bạn có thể bỏ qua hướng dẫn này và bắt đầu đóng góp trực tiếp.
![tutorial](assets/2.webp)

Hãy cùng khám phá cách thêm một giáo sư mới trong hướng dẫn này!

## Yêu cầu tiên quyết

**Phần mềm cần thiết để theo dõi hướng dẫn của tôi:**
- [GitHub Desktop](https://desktop.github.com/)
- Một trình soạn thảo mã ([VSC](https://code.visualstudio.com/) hoặc [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/3.webp)
**Yêu cầu trước khi bắt đầu hướng dẫn:**
- Có một [tài khoản GitHub](https://github.com/signup).
- Có một bản sao của [kho lưu trữ nguồn PlanB Network](https://github.com/PlanB-Network/bitcoin-educational-content).

**Nếu bạn cần trợ giúp để có được những yêu cầu tiên quyết này, các hướng dẫn khác của tôi sẽ hướng dẫn bạn:**
**[Hiểu về Git và GitHub](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
**[Tạo một Tài khoản GitHub](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Thiết lập Môi trường Làm việc của Bạn](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**

## Làm thế nào để tạo một hồ sơ giáo sư mới?

- Mở trình duyệt của bạn và điều hướng đến trang của bản sao kho lưu trữ PlanB của bạn. URL của bản sao của bạn nên trông giống như: `https://github.com/[username]/bitcoin-educational-content`
![tutorial](assets/4.webp)
- Đảm bảo bạn đang ở nhánh chính `dev` sau đó nhấp vào nút `Sync fork`. Nếu bản sao của bạn không cập nhật, GitHub sẽ đề nghị cập nhật nhánh của bạn. Tiến hành đồng bộ hóa này.

- Nếu, ngược lại, nhánh của bạn đã cập nhật, GitHub sẽ thông báo cho bạn:
![tutorial](assets/5.webp)- Mở GitHub Desktop và đảm bảo bản sao của bạn được chọn đúng cách ở góc trên bên trái của cửa sổ:
![tutorial](assets/6.webp)
- Nhấp vào nút `Fetch origin`.

- Nếu kho lưu trữ cục bộ của bạn đã cập nhật, GitHub Desktop sẽ không đề xuất thêm hành động nào. Nếu không, tùy chọn `Pull origin` sẽ xuất hiện. Nhấp vào nút này để cập nhật kho lưu trữ cục bộ của bạn:
![tutorial](assets/7.webp)
- Đảm bảo bạn đang ở nhánh chính `dev`:
![tutorial](assets/8.webp)
- Nhấp vào nhánh này, sau đó nhấp vào nút `New Branch`:
![tutorial](assets/9.webp)
- Đảm bảo nhánh mới được tạo dựa trên kho lưu trữ gốc, cụ thể là `PlanB-Network/bitcoin-educational-content`.
- Đặt tên cho nhánh của bạn theo cách mà tiêu đề rõ ràng về mục đích của nó, sử dụng dấu gạch ngang để phân cách mỗi từ. Vì nhánh này được dự định để thêm hồ sơ giáo sư, ví dụ tên có thể là: `add-professor-[tên-của-bạn]`. Sau khi nhập tên, nhấn vào `Create branch` để xác nhận việc tạo nhánh:
![hướng dẫn](assets/10.webp)
- Bây giờ nhấn vào nút `Publish branch` để lưu nhánh làm việc mới của bạn vào fork trực tuyến trên GitHub:
![hướng dẫn](assets/11.webp)
- Tại thời điểm này, trên GitHub Desktop, bạn sẽ ở trên nhánh mới của mình. Điều này có nghĩa là tất cả các thay đổi được thực hiện cục bộ trên máy tính của bạn sẽ được ghi lại độc quyền trên nhánh cụ thể này. Ngoài ra, miễn là nhánh này vẫn được chọn trên GitHub Desktop, các tệp hiển thị cục bộ trên máy tính của bạn tương ứng với những tệp của nhánh này (`add-professor-ten-cua-ban`), và không phải là những tệp của nhánh chính (`dev`):
![hướng dẫn](assets/12.webp)
- Để thêm hồ sơ giáo sư của bạn, mở trình duyệt tệp và điều hướng đến kho lưu trữ cục bộ của bạn, trong thư mục `professors`. Bạn sẽ tìm thấy nó dưới đường dẫn: `\GitHub\bitcoin-educational-content\professors`.

- Trong thư mục này, tạo một thư mục mới với tên hoặc bí danh của bạn. Đảm bảo không có khoảng trắng trong tên thư mục. Vì vậy, nếu tên của bạn là "Loic Pandul" và không có giáo sư nào khác có tên này, thư mục để tạo sẽ được đặt tên là `loic-pandul`:
![hướng dẫn](assets/13.webp)
- Để việc này trở nên dễ dàng hơn, bạn có thể sao chép và dán tất cả các tài liệu từ một giáo sư khác vào thư mục của riêng bạn. Chúng ta sau đó sẽ tiến hành chỉnh sửa các tài liệu này để tùy chỉnh chúng theo hồ sơ của bạn:
![hướng dẫn](assets/14.webp)
- Bắt đầu bằng cách điều hướng đến thư mục `assets`. Xóa ảnh hồ sơ của giáo sư mà bạn đã sao chép trước đó, và thay thế nó bằng hình ảnh hồ sơ của riêng bạn. Điều quan trọng là hình ảnh này phải ở định dạng `.webp` và được đặt tên là `profile`, từ đó tạo ra tên tệp đầy đủ `profile.webp`. Hãy lưu ý, hình ảnh này sẽ được công bố trên Internet và có thể truy cập bởi mọi người: ![hướng dẫn](assets/15.webp)
- Tiếp theo, mở tệp `professor.yml` bằng trình chỉnh sửa mã của bạn (VSC hoặc Sublime Text, ví dụ). Bạn sẽ đến với tệp được sao chép từ một giáo sư hiện có:
![hướng dẫn](assets/16.webp)
- Bạn sau đó phải cập nhật thông tin hiện có với thông tin của riêng bạn:
	- **name:** viết tên hoặc bí danh của bạn;
	- **links:** chỉ ra các tài khoản của bạn trên các mạng xã hội như Twitter và Nostr, cũng như URL của trang web cá nhân của bạn (tùy chọn);
	- **affiliation:** nêu tên công ty mà bạn làm việc (tùy chọn);
	- **tags:** chỉ định các lĩnh vực chuyên môn của bạn từ danh sách sau, biết rằng bạn có thể thêm các chủ đề của riêng mình. Tuy nhiên, hãy chắc chắn giới hạn số lượng thẻ tối đa là 4 để đảm bảo giao diện người dùng tốt:
	    - privacy,
	    - cryptography,
	    - bitcoin,
	    - mining,
	    - lightning-network,
	    - economy,
	    - history,
	    - merchants,
	    - security,
	    - ...
	- **tips:** cung cấp địa chỉ Lightning của bạn để nhận quyên góp, cho phép độc giả của các hướng dẫn tương lai của bạn gửi cho bạn một số sats (tùy chọn);
	- **company:** nếu bạn sở hữu một công ty, chỉ ra tên của công ty của bạn (tùy chọn). Sau đó bạn phải cập nhật thông tin hiện có với thông tin của riêng bạn:
![hướng dẫn](assets/17.webp)- Bạn cũng cần phải thay đổi `contributor-id`. Định danh này được sử dụng để nhận diện bạn trên website, nhưng không được công bố ngoài GitHub. Bạn có thể tự do chọn bất kỳ sự kết hợp nào của hai từ, tham khảo [danh sách tiếng Anh gồm 2048 từ từ BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). Đừng quên chèn một dấu gạch ngang giữa hai từ đã chọn. Ví dụ, ở đây, tôi đã chọn `crazy-cactus`:
![hướng dẫn](assets/18.webp)
- Khi bạn đã hoàn thành việc chỉnh sửa tài liệu `professor.yml`, nhấp vào `File > Save` để lưu tệp của bạn. Sau đó bạn có thể thoát khỏi trình biên tập mã:
![hướng dẫn](assets/19.webp)
- Trong thư mục giáo sư của bạn, bạn có thể xóa các tài liệu được viết bằng ngôn ngữ không liên quan đến bạn, ban đầu được sao chép từ một giáo sư khác. Chỉ giữ lại tệp tương ứng với ngôn ngữ mẹ đẻ của bạn. Ví dụ, trong trường hợp của tôi, tôi chỉ giữ lại tệp `fr.yml`, vì ngôn ngữ của tôi là tiếng Pháp: ![hướng dẫn](assets/20.webp)
- Nhấp đúp vào tệp này để mở nó bằng trình biên tập mã của bạn.

- Trong tệp này, bạn có cơ hội viết tiểu sử đầy đủ của mình dưới phần `bio` và một bản tóm tắt hoặc một tiêu đề súc tích dưới `short_bio`:
![hướng dẫn](assets/21.webp)
- Sau khi lưu tài liệu `fr.yml` của bạn, bạn cần tạo một bản sao của tệp này cho mỗi ngôn ngữ sau đây:
    - Đức (DE);
    - Anh (EN);
    - Pháp (FR);
    - Tây Ban Nha (ES);
    - Ý (IT);
    - Bồ Đào Nha (PT);
    - Nhật Bản (JA);
    - Việt Nam (VI).

- Tiến hành sao chép và dán tệp gốc của bạn, sau đó dịch mỗi tài liệu sang ngôn ngữ tương ứng. Nếu bạn thành thạo ngôn ngữ, bạn có thể thực hiện việc dịch một cách thủ công. Nếu không, bạn có thể sử dụng công cụ dịch tự động hoặc chatbot:
![hướng dẫn](assets/22.webp)
- Nếu bạn muốn, cũng có thể chỉ giữ tiểu sử bằng ngôn ngữ mẹ đẻ của bạn; sau đó chúng tôi sẽ xử lý việc dịch sau khi bạn gửi Yêu cầu kéo (Pull Request).

- Thư mục giáo sư của bạn do đó sẽ trông như thế này:
![hướng dẫn](assets/23.webp)
```plaintext
first-name-last-name/
├── fr.yml
├── it.yml
├── es.yml
├── en.yml
├── de.yml
├── pt.yml
├── ja.yml
├── vi.yml
├── professor.yml
└── assets/
    └── profile.webp
```
- Bây giờ quay trở lại GitHub Desktop.
- Ở phía bên trái cửa sổ của bạn, bạn sẽ quan sát thấy tất cả các thay đổi được thực hiện đối với các tài liệu, cụ thể cho nhánh của bạn. Đảm bảo những thay đổi này là chính xác:
![hướng dẫn](assets/24.webp)
- Nếu các thay đổi dường như chính xác với bạn, thêm một tiêu đề cho lần cam kết (commit) của bạn. Một cam kết là một lưu của các thay đổi được thực hiện đối với nhánh, đi kèm với một thông điệp mô tả, cho phép theo dõi sự phát triển của một dự án theo thời gian.
- Sau khi nhập tiêu đề, nhấn vào nút màu xanh `Commit to [your branch]` để xác nhận những thay đổi này:
![hướng dẫn](assets/25.webp)
- Sau đó nhấp vào nút `Push origin`. Điều này sẽ gửi cam kết của bạn đến fork của bạn:
![hướng dẫn](assets/26.webp)
- Nếu bạn đã hoàn thành các thay đổi cho nhánh này, bây giờ nhấp vào nút `Preview Pull Request`:
![hướng dẫn](assets/27.webp)
- Bạn có thể kiểm tra lần cuối cùng để đảm bảo các sửa đổi của bạn là chính xác, sau đó nhấp vào nút `Tạo yêu cầu kéo` (Create pull request): ![hướng dẫn](assets/28.webp)- Bạn sẽ được tự động chuyển hướng đến trình duyệt của mình trên GitHub đến trang chuẩn bị Yêu Cầu Kéo (Pull Request). Yêu Cầu Kéo là một yêu cầu được thực hiện để tích hợp các thay đổi từ nhánh của bạn vào nhánh chính của kho lưu trữ PlanB Network, cho phép xem xét và thảo luận về các thay đổi trước khi chúng được hợp nhất: ![hướng dẫn](assets/29.webp)
- Trên trang chuẩn bị này, hãy chỉ định một tiêu đề ngắn gọn tóm tắt các sửa đổi bạn muốn hợp nhất với kho lưu trữ nguồn.
- Thêm một bình luận ngắn gọn mô tả những thay đổi này.
- Sau khi hoàn thành các bước này, nhấp vào nút `Tạo yêu cầu kéo` (Create pull request) màu xanh để xác nhận yêu cầu hợp nhất: ![hướng dẫn](assets/30.webp)
- Yêu Cầu Kéo (PR) của bạn sau đó sẽ hiển thị trong tab `Yêu Cầu Kéo` (Pull Request) của kho lưu trữ chính của PlanB Network. Bây giờ, tất cả những gì bạn cần làm là chờ đợi cho đến khi một quản trị viên liên hệ với bạn để xác nhận việc hợp nhất đóng góp của bạn hoặc để yêu cầu bất kỳ sửa đổi bổ sung nào: ![hướng dẫn](assets/31.webp)
- Sau khi hợp nhất Yêu Cầu Kéo của bạn với nhánh chính, bạn nên xóa nhánh làm việc của mình (`add-professor-your-name`) để duy trì lịch sử sạch sẽ trên fork của bạn. GitHub sẽ tự động cung cấp cho bạn tùy chọn này trên trang PR của bạn: ![hướng dẫn](assets/32.webp)
- Trên phần mềm GitHub Desktop, bạn có thể chuyển lại về nhánh chính của fork của mình (`dev`): ![hướng dẫn](assets/8.webp)
- Nếu bạn muốn thực hiện sửa đổi hồ sơ của mình sau khi đã gửi Yêu Cầu Kéo của bạn, quy trình phụ thuộc vào tình trạng hiện tại của Yêu Cầu Kéo của bạn:
	- Nếu Yêu Cầu Kéo của bạn vẫn đang mở và chưa được hợp nhất, hãy thực hiện các sửa đổi cục bộ trong khi vẫn ở trên cùng một nhánh. Một khi các sửa đổi được hoàn thiện, sử dụng nút `Đẩy nguồn` (Push origin) để thêm một commit mới vào Yêu Cầu Kéo vẫn đang mở của bạn;
	- Trong trường hợp Yêu Cầu Kéo của bạn đã được hợp nhất với nhánh chính, bạn sẽ cần bắt đầu quy trình lại từ đầu bằng cách tạo một nhánh mới, sau đó gửi một Yêu Cầu Kéo mới. Đảm bảo rằng kho lưu trữ cục bộ của bạn được đồng bộ hóa với kho lưu trữ nguồn của PlanB Network trước khi tiến hành.
