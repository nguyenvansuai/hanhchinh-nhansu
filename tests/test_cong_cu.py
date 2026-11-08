#!/usr/bin/env python3
"""Kiểm thử công cụ: python3 tests/test_cong_cu.py (không cần pytest)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import goi, tat_ca  # noqa: E402

LOI = []


def kiem(ten, dk, chi_tiet=""):
    print(("  ok  " if dk else "  LỖI ") + ten + ("" if dk else f" -> {chi_tiet}"))
    if not dk:
        LOI.append(ten)


def test_lich():
    kiem("Tết 2026 = 17/02", goi("doi_lich_am_duong", {"ngay_am": "01/01/2026"})["duong_lich"].endswith("17/02/2026"))
    kiem("Tết 2027 = 06/02", goi("doi_lich_am_duong", {"ngay_am": "01/01/2027"})["duong_lich"].endswith("06/02/2027"))
    kiem("Giỗ Tổ 2025 = 07/04", goi("doi_lich_am_duong", {"ngay_am": "10/03/2025"})["duong_lich"].endswith("07/04/2025"))
    kiem("Nhuận tháng 6/2025", "nhuận" in goi("doi_lich_am_duong", {"ngay": "25/07/2025"})["am_lich"])
    le = goi("ngay_le_tet", {"nam": 2026})
    kiem("2026 có 11 ngày lễ", len(le["ngay_le"]) == 11, len(le["ngay_le"]))
    kiem("Nghỉ bù Giỗ Tổ 27/04/2026", any("27/04/2026" in x["ngay"] for x in le["nghi_bu"]), le["nghi_bu"])
    r = goi("ngay_lam_viec", {"tu_ngay": "12/02/2026", "so_ngay": 5})
    kiem("5 ngày làm việc qua Tết", r["ngay_ket_thuc"].endswith("26/02/2026"), r)
    r = goi("cong_ngay_lich", {"tu_ngay": "31/08/2026", "so_thang": 6})
    kiem("Cộng tháng cuối tháng", r["ket_qua"].endswith("28/02/2027"), r)


def test_doc_so():
    for so, chu in [(1_250_000, "Một triệu hai trăm năm mươi nghìn đồng"), (105_000, "Một trăm linh năm nghìn đồng"),
                    (21, "Hai mươi mốt đồng"), (1_000_005_000, "Một tỷ không trăm linh năm nghìn đồng")]:
        kiem(f"Đọc {so}", goi("doc_so_thanh_chu", {"so": str(so)})["bang_chu"] == chu)


def test_lao_dong():
    r = goi("tro_cap_thoi_viec", {"ngay_bat_dau": "01/03/2008", "ngay_nghi": "15/10/2026",
                                  "luong_binh_quan_6_thang": 20_000_000, "so_thang_dong_bhtn": 200})
    kiem("Trợ cấp: 23 tháng → 2 năm × 1/2 × 20tr = 20tr", r["so_tien_so"] == 20_000_000, r["so_tien"])
    r = goi("tro_cap_thoi_viec", {"ngay_bat_dau": "01/01/2025", "ngay_nghi": "01/06/2026",
                                  "luong_binh_quan_6_thang": 10_000_000, "loai": "mat_viec"})
    kiem("Mất việc tối thiểu 2 tháng lương", r["so_tien_so"] == 20_000_000, r["so_tien"])
    r = goi("phep_nam", {"ngay_bat_dau": "01/03/2016", "nam": 2026})
    kiem("Phép năm 10 năm thâm niên = 14", r["so_ngay_phep_nam"] == 14, r)
    r = goi("phep_nam", {"ngay_bat_dau": "01/05/2026", "nam": 2026})
    kiem("Phép năm vào 01/05 = 8", r["so_ngay_phep_nam"] == 8, r)
    r = goi("thoi_han_bao_truoc", {"ben": "nguoi_lao_dong", "loai_hop_dong": "khong_xac_dinh", "ngay_thong_bao": "01/10/2026"})
    kiem("Báo trước 45 ngày", r["ngay_som_nhat_cham_dut"].endswith("15/11/2026"), r["ngay_som_nhat_cham_dut"])
    r = goi("kiem_tra_thu_viec", {"trinh_do": "cao_dang_tro_len", "so_ngay_thu_viec": 90,
                                  "luong_thu_viec": 8_000_000, "luong_chinh_thuc": 10_000_000})
    kiem("Thử việc 90 ngày + 80% lương: 2 lỗi", len(r["loi"]) == 2, r["loi"])
    r = goi("thoi_hieu_ky_luat", {"ngay_xay_ra_vi_pham": "10/03/2026", "ngay_hop_du_kien": "20/04/2026"})
    kiem("Thời hiệu 6 tháng", r["het_thoi_hieu"].endswith("10/09/2026"), r["het_thoi_hieu"])
    kiem("Thông báo họp chậm nhất 13/04", r["thong_bao_hop_cham_nhat"].endswith("13/04/2026"), r["thong_bao_hop_cham_nhat"])
    r = goi("luong_net_gross", {"muc_luong": 30_000_000, "ngay_ap_dung": "2026-08-01"})
    # BH 10,5% = 3.150.000; TNTT = 30 - 3,15 - 15,5 = 11,35tr; thuế = 10tr×5% + 1,35tr×10% = 635.000
    kiem("Gross 30tr → net 26.215.000", r["net_so"] == 26_215_000, r["luong_net"])
    r2 = goi("luong_net_gross", {"muc_luong": 26_215_000, "chieu": "net_sang_gross", "ngay_ap_dung": "2026-08-01"})
    kiem("Net → gross quay lại ~30tr", abs(int(r2["luong_gross"].replace(".", "").split()[0]) - 30_000_000) < 2000, r2["luong_gross"])
    r = goi("luong_net_gross", {"muc_luong": 100_000_000, "ngay_ap_dung": "2026-08-01"})
    kiem("Trần BHXH 50,6tr sau 01/7/2026", "50.600.000" in r["tham_so"]["tran_bhxh_bhyt"], r["tham_so"]["tran_bhxh_bhyt"])
    kiem("Lương 5tr vùng I 2026 dưới tối thiểu", not goi("kiem_tra_luong_toi_thieu", {"muc_luong": 5_000_000, "ngay_ap_dung": "2026-03-01"})["dat"])


def test_so_van_ban():
    d = tempfile.mkdtemp()
    r1 = goi("cap_so_van_ban_di", {"loai_van_ban": "Quyết định", "viet_tat_co_quan": "ABC", "trich_yeu": "Bổ nhiệm",
                                   "ngay_van_ban": "05/03/2026", "thu_muc": d})
    r2 = goi("cap_so_van_ban_di", {"loai_van_ban": "Công văn", "viet_tat_co_quan": "ABC", "viet_tat_don_vi": "HCNS",
                                   "trich_yeu": "Đề nghị", "ngay_van_ban": "06/03/2026", "thu_muc": d})
    kiem("Số QĐ", r1["da_cap_so"] == "Số: 01/QĐ-ABC", r1)
    kiem("Số công văn", r2["da_cap_so"] == "Số: 02/ABC-HCNS", r2)
    r = goi("dang_ky_van_ban_den", {"co_quan_ban_hanh": "Sở Nội vụ", "so_ky_hieu": "15/SNV-LĐ", "trich_yeu": "Báo cáo lao động",
                                    "ngay_den": "02/06/2026", "so_ngay_lam_viec_xu_ly": 3, "thu_muc": d})
    kiem("Hạn xử lý 3 ngày làm việc", r["han_xu_ly"] == "05/06/2026", r)
    r = goi("dang_ky_van_ban_den", {"co_quan_ban_hanh": "Sở Nội vụ", "so_ky_hieu": "15/SNV-LĐ", "trich_yeu": "x", "thu_muc": d,
                                    "ngay_den": "03/06/2026"})
    kiem("Phát hiện trùng", "canh_bao" in r, r)
    r = goi("tra_cuu_so_van_ban", {"loai": "den", "nam": 2026, "chi_qua_han": True, "hom_nay": "10/06/2026", "thu_muc": d})
    kiem("Lọc quá hạn", r["so_ban_ghi"] == 1, r)


def test_the_thuc():
    try:
        import docx  # noqa: F401
    except ImportError:
        print("  bỏ qua kiểm thử .docx (chưa cài python-docx)")
        return
    d = tempfile.mkdtemp()
    f = os.path.join(d, "qd.docx")
    goi("tao_van_ban_docx", {"duong_dan_ra": f, "co_quan_ban_hanh": "Công ty Cổ phần ABC", "ten_loai": "QUYẾT ĐỊNH",
                             "trich_yeu": "Về việc bổ nhiệm Trưởng phòng Hành chính - Nhân sự", "so_ky_hieu": "Số: 15/QĐ-ABC",
                             "dia_danh": "Hà Nội", "ngay": "ngày 05 tháng 3 năm 2026", "quyen_han_ky": "GIÁM ĐỐC CÔNG TY CỔ PHẦN ABC",
                             "can_cu": ["Căn cứ Luật Doanh nghiệp số 59/2020/QH14;", "Căn cứ Điều lệ Công ty."],
                             "noi_dung": ["Điều 1. Bổ nhiệm bà Nguyễn Thị B.", "Điều 2. Quyết định có hiệu lực kể từ ngày ký."],
                             "nguoi_ky": "Trần Văn C", "chuc_vu_ky": "Giám đốc", "noi_nhan": ["- Như Điều 2;", "- Lưu: VT, HCNS."]})
    r = goi("kiem_tra_the_thuc", {"duong_dan": f})
    kiem("File tạo ra không có lỗi CHẶN/CẦN SỬA", all(x["muc"] == "GỢI Ý" for x in r["danh_sach_loi"]), r["danh_sach_loi"])
    vb = "Số: 5/QĐ-ABC\nHà Nội, ngày 5 tháng 3 năm 2026\nCăn cứ Bộ luật Lao động 2012;\nĐịa chỉ: quận Cầu Giấy, Hà Nội\n" \
         "Số tiền 1.500.000 đồng (Bằng chữ: Một triệu năm trăm nghìn đồng)\nKT GIÁM ĐỐC"
    r = goi("kiem_tra_the_thuc", {"van_ban": vb})
    loai = " | ".join(x["van_de"] for x in r["danh_sach_loi"])
    for kw in ["Quốc hiệu", "Ngày dưới 10", "Bộ luật Lao động 2012", "quận/huyện", "dấu chấm", "Nơi nhận"]:
        kiem(f"Bắt lỗi: {kw}", kw in loai, loai)
    kiem("Số tiền đúng không báo lỗi", "không khớp" not in loai)


if __name__ == "__main__":
    print(f"{len(tat_ca())} công cụ")
    for f in [test_lich, test_doc_so, test_lao_dong, test_so_van_ban, test_the_thuc]:
        print(f.__name__)
        f()
    print("KẾT QUẢ:", "TẤT CẢ ĐẠT" if not LOI else f"{len(LOI)} LỖI")
    sys.exit(1 if LOI else 0)
