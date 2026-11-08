---
name: ky-luat-lao-dong
description: Xử lý kỷ luật lao động đúng trình tự Bộ luật Lao động 2019 và Nghị định 145/2020 — xác minh vi phạm, lập biên bản sự việc, đối chiếu nội quy đã đăng ký, tính thời hiệu (6 hoặc 12 tháng) và ngày chậm nhất gửi thông báo họp (5 ngày làm việc), thông báo họp, biên bản cuộc họp xử lý kỷ luật có tổ chức đại diện NLĐ, quyết định kỷ luật (khiển trách, kéo dài thời hạn nâng lương, cách chức, sa thải – chỉ trong 5 trường hợp Điều 125), tạm đình chỉ công việc, bồi thường thiệt hại và khấu trừ lương, xóa kỷ luật, xử lý quấy rối tình dục tại nơi làm việc; chặn các cách làm trái luật (phạt tiền, trừ lương, kỷ luật khi NLĐ đang nghỉ ốm, mang thai). Dùng khi người dùng nói "nhân viên vi phạm xử lý thế nào", "kỷ luật sa thải", "nhân viên tự ý nghỉ 5 ngày", "nhân viên trộm cắp", "lập biên bản vi phạm", "quyết định kỷ luật", "có được phạt tiền nhân viên không", "bồi thường làm hỏng tài sản".
---

# Kỷ luật lao động

Đọc trước: `references/nguyen-tac-chung.md`, `references/quy-dinh-lao-dong-2026.md`, `references/the-thuc-nd30.md`, `references/mau-ky-luat.md`.

> Kỷ luật sai trình tự → quyết định trái luật, phải nhận lại NLĐ và bồi thường. Sa thải, vụ việc có tranh chấp → khuyến nghị tham vấn luật sư trước khi ra quyết định.

## Bước 0 – Sàng lọc điều kiện (dừng nếu có điểm không đạt)

| Kiểm tra | Nếu không đạt |
|---|---|
| Hành vi có trong **nội quy lao động** (đã đăng ký nếu ≥ 10 NLĐ), HĐLĐ hoặc pháp luật? | Không được kỷ luật (Điều 127) |
| Chứng minh được **lỗi** của NLĐ (biên bản, camera, nhân chứng, chứng từ)? | Thu thập thêm chứng cứ trước |
| Còn **thời hiệu**? → `thoi_hieu_ky_luat` | Hết thời hiệu: không xử lý |
| NLĐ có đang trong thời gian **không được xử lý** (khoản 4 Điều 122)? – nghỉ ốm, điều dưỡng, nghỉ việc được đồng ý; bị tạm giữ/tạm giam; chờ kết quả xác minh; lao động nữ mang thai, nghỉ thai sản, nuôi con dưới 12 tháng | Hoãn; thời hiệu kéo dài ≤ 60 ngày sau khi hết thời gian đó |
| NLĐ vi phạm khi mắc bệnh tâm thần/bệnh làm mất khả năng nhận thức? | Không xử lý (khoản 5 Điều 122) |
| Hình thức dự kiến thuộc 4 hình thức luật định? Sa thải có thuộc 5 trường hợp Điều 125? | Đổi hình thức |
| Một hành vi chỉ một hình thức; nhiều hành vi → hình thức cao nhất | |

## Bước 1–5 – Trình tự (Điều 122 BLLĐ, Điều 70 NĐ 145)

1. **Lập biên bản vi phạm** ngay khi phát hiện (mẫu A trong `references/mau-ky-luat.md`). NSDLĐ phát hiện sau → thu thập chứng cứ.
2. **Thông báo họp** gửi NLĐ + tổ chức đại diện NLĐ (nếu NLĐ là thành viên) + người đại diện theo pháp luật (NLĐ dưới 15 tuổi) **ít nhất 5 ngày làm việc trước ngày họp**. Ngày chậm nhất: `thoi_hieu_ky_luat` với `ngay_hop_du_kien`. Gửi có bằng chứng (ký nhận, email, bưu điện).
3. **Họp xử lý kỷ luật**: thành phần đủ; NLĐ được bào chữa/nhờ luật sư, tổ chức đại diện bào chữa. Đã thông báo hợp lệ mà NLĐ/đại diện không đến → vẫn họp được (ghi rõ trong biên bản) [Chắc chắn – NĐ 145]. Lập **biên bản họp** (mẫu B), thông qua trước khi kết thúc, người tham dự ký; ai không ký ghi lý do.
4. **Quyết định kỷ luật** (mẫu C) trong thời hiệu; người có thẩm quyền theo nội quy ký; gửi NLĐ, tổ chức đại diện NLĐ.
5. **Sau quyết định**: lưu hồ sơ; sa thải → thủ tục chấm dứt (skill `cham-dut-hop-dong`, `onboarding-offboarding`); NLĐ có quyền khiếu nại/khởi kiện.

## Tạm đình chỉ công việc (Điều 128)
Khi vi phạm phức tạp, để NLĐ làm việc gây khó khăn xác minh: sau khi tham khảo ý kiến tổ chức đại diện NLĐ (nếu NLĐ là thành viên); ≤ 15 ngày, đặc biệt ≤ 90 ngày; **tạm ứng 50% lương**; hết hạn phải cho làm việc lại; không bị kỷ luật thì được trả đủ lương thời gian tạm đình chỉ.

## Bồi thường thiệt hại (Điều 129–130, Điều 102)
Do sơ suất, thiệt hại không nghiêm trọng, giá trị ≤ 10 tháng lương tối thiểu vùng → bồi thường **tối đa 3 tháng lương** khấu trừ hằng tháng ≤ 30% tiền lương thực trả. Mất tài sản/vật tư được giao, tiêu hao quá định mức → bồi thường một phần hoặc toàn bộ theo thời giá; có hợp đồng trách nhiệm thì theo hợp đồng. Trình tự xử lý bồi thường giống trình tự kỷ luật (NĐ 145). Không dùng "bồi thường" để phạt tiền trá hình.

## Xóa kỷ luật (Điều 126)
Khiển trách: sau 3 tháng; kéo dài thời hạn nâng lương: sau 6 tháng – không vi phạm tiếp thì đương nhiên được xóa. Cách chức: sau 3 năm nếu vi phạm tiếp thì không coi là tái phạm. Tính ngày bằng `cong_ngay_lich`.

## Quấy rối tình dục tại nơi làm việc
Theo trình tự trong nội quy (kênh tiếp nhận, bảo mật danh tính, thời hạn xác minh); hành vi quấy rối được quy định trong nội quy → có thể sa thải (khoản 3 Điều 125). Bảo vệ người tố giác, tách tiếp xúc giữa hai bên trong thời gian xác minh.

## Đầu ra
Kết quả sàng lọc (đạt/không đạt từng điều kiện) · lịch các mốc (thời hiệu, hạn thông báo, ngày họp) · biên bản vi phạm, thông báo họp, biên bản họp, quyết định – đúng thể thức · danh sách chứng cứ cần có · cảnh báo rủi ro.
