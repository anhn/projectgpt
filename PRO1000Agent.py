import streamlit as st
import plotly.graph_objects as go

# ======== Khai báo chi tiết các nhóm và chỉ số ========

metrics = {
    "Công nghệ": {
        "TCH": {
            "label": "Sẵn sàng công nghệ (TCH)",
            "desc": "Mức độ chín muồi hạ tầng CNTT, hệ thống định danh số, Internet phủ (%). Giá trị từ 0–100.",
            "type": "slider",
            "min": 0,
            "max": 100,
            "step": 5
        },
        "COM": {
            "label": "Tương thích hệ thống (COM)",
            "desc": "Khả năng tích hợp API với công an, bảo hiểm, gara sửa chữa (%). Giá trị từ 0–100.",
            "type": "slider",
            "min": 0,
            "max": 100,
            "step": 5
        },
        "DAV": {
            "label": "Sẵn sàng dữ liệu (DAV)",
            "desc": "Tỷ lệ hồ sơ xe đã số hóa và có thể truy vấn realtime (%). Giá trị từ 0–100.",
            "type": "slider",
            "min": 0,
            "max": 100,
            "step": 5
        },
        "SKL": {
            "label": "Nhân lực blockchain (SKL)",
            "desc": "Số lượng nhân viên nội bộ hoặc địa phương thành thạo blockchain (số người).",
            "type": "number",
            "min": 0,
            "max": 100,
            "step": 1
        }
    },
    "Pháp lý & Chính sách": {
        "LSG": {
            "label": "Khung pháp lý rõ ràng (LSG)",
            "desc": "Đã có văn bản quy định về hồ sơ điện tử, smart contract? (1=Chưa, 5=Đầy đủ).",
            "type": "slider",
            "min": 1,
            "max": 5,
            "step": 1
        },
        "DPR": {
            "label": "Quyền riêng tư & Dữ liệu (DPR)",
            "desc": "Chính sách quốc gia về dữ liệu cá nhân và lưu trữ phân tán (1=Chưa, 5=Đủ).",
            "type": "slider",
            "min": 1,
            "max": 5,
            "step": 1
        },
        "LRR": {
            "label": "Công nhận hồ sơ blockchain (LRR)",
            "desc": "Hồ sơ/truy vết trên blockchain có giá trị pháp lý (1=Không, 5=Có).",
            "type": "slider",
            "min": 1,
            "max": 5,
            "step": 1
        }
    },
    "Tổ chức": {
        "ORG": {
            "label": "Năng lực tổ chức (ORG)",
            "desc": "Đã có đơn vị e-governance hoặc nhóm R&D blockchain trong Bộ GTVT? (1=Chưa, 5=Đủ).",
            "type": "slider",
            "min": 1,
            "max": 5,
            "step": 1
        },
        "CHM": {
            "label": "Chuyển đổi & Đào tạo (CHM)",
            "desc": "Kế hoạch đào tạo, mức độ tương tác các bên liên quan (1=Kém, 5=Tốt).",
            "type": "slider",
            "min": 1,
            "max": 5,
            "step": 1
        },
        "COL": {
            "label": "Hợp tác liên ngành (COL)",
            "desc": "Tỷ lệ cơ quan Bảo hiểm, Gara sẵn sàng tích hợp (%) (0–100).",
            "type": "slider",
            "min": 0,
            "max": 100,
            "step": 10
        }
    },
    "Tài chính": {
        "CAPEX": {
            "label": "Chi phí đầu tư (CAPEX ↓)",
            "desc": "Tỷ lệ vốn đầu tư cho blockchain so với ngân sách (%) (0–100). Thấp hơn là tốt.",
            "type": "slider",
            "min": 0,
            "max": 100,
            "step": 5
        },
        "OPEX": {
            "label": "Chi phí vận hành (OPEX ↓)",
            "desc": "Chi phí hàng năm cho hạ tầng, gas (nếu public chain) (%) so với ngân sách. Thấp hơn là tốt.",
            "type": "slider",
            "min": 0,
            "max": 100,
            "step": 5
        },
        "CBR": {
            "label": "Tỷ suất Lợi ích/Chi phí (CBR)",
            "desc": "Tỷ lệ tiết kiệm: chi phí chống gian lận, giảm thủ tục (%) so với tổng chi phí. (0–200%).",
            "type": "slider",
            "min": 0,
            "max": 200,
            "step": 10
        }
    },
    "Người dùng": {
        "TRU": {
            "label": "Niềm tin & Chấp nhận (TRU)",
            "desc": "Mức độ tin tưởng hệ thống blockchain (Khảo sát %). (1–100).",
            "type": "slider",
            "min": 1,
            "max": 100,
            "step": 5
        },
        "IND": {
            "label": "Hỗ trợ doanh nghiệp (IND)",
            "desc": "Tỷ lệ doanh nghiệp tư nhân/Gara/Bảo hiểm tham gia (%) (0–100).",
            "type": "slider",
            "min": 0,
            "max": 100,
            "step": 10
        },
        "USAB": {
            "label": "Khả năng sử dụng (USAB)",
            "desc": "Tỷ lệ người dùng hoàn thành tác vụ chính mà không cần trợ giúp (%) (0–100).",
            "type": "slider",
            "min": 0,
            "max": 100,
            "step": 10
        }
    },
    "Chiến lược & Ngoại cảnh": {
        "POL": {
            "label": "Hỗ trợ chính trị (POL)",
            "desc": "Đã nằm trong Chương trình chuyển đổi số quốc gia? (1=Chưa, 5=Có).",
            "type": "slider",
            "min": 1,
            "max": 5,
            "step": 1
        },
        "GLB": {
            "label": "Xu hướng & Tương thích quốc tế (GLB)",
            "desc": "Khả năng kết nối tiêu chuẩn ASEAN/EU cho định danh xe (1=Thấp, 5=Cao).",
            "type": "slider",
            "min": 1,
            "max": 5,
            "step": 1
        }
    }
}

# ======== Khởi tạo session state ========
if 'step' not in st.session_state:
    st.session_state.step = 0
    for grp in metrics.values():
        for key in grp:
            st.session_state[key] = grp[key]["min"]

# ======== Các hàm điều hướng ========
def next_step():
    st.session_state.step += 1

def reset():
    st.session_state.step = 0
    for grp in metrics.values():
        for key in grp:
            st.session_state[key] = metrics[list(metrics.keys())[0]][key]["min"]

# ======== Cấu hình trang ========
st.set_page_config(page_title="Đánh giá khả thi Blockchain GTVT", layout="wide")
st.title("🧠 Công cụ đánh giá khả thi Blockchain cho GTVT – Prototype")

# ======== Thanh Trạng thái 7 bước ========
st.markdown("### 🔄 Tiến trình đánh giá:")
cols = st.columns(7)
status_labels = [
    "1️⃣ Tình huống", 
    "2️⃣ Công nghệ", 
    "3️⃣ Pháp lý", 
    "4️⃣ Tổ chức", 
    "5️⃣ Tài chính", 
    "6️⃣ Người dùng", 
    "7️⃣ Kết quả"
]
for idx, lbl in enumerate(status_labels):
    if idx == st.session_state.step:
        cols[idx].markdown(f"✅ **{lbl}**")
    else:
        cols[idx].markdown(lbl)
st.divider()

# ======== Bước 0: Tình huống và Thông tin ========
if st.session_state.step == 0:
    st.subheader("📋 Bước 1: Mô tả trường hợp & thông tin cơ bản")
    domain = st.selectbox("1. Chọn lĩnh vực GTVT:", 
                          ["Quản lý đăng kiểm", "Vận tải hàng hóa", "Logistics", 
                           "Quản lý dự án hạ tầng", "Khác"],
                          help="Ví dụ: Vận hành hệ thống quản lý đăng kiểm liên bộ sử dụng blockchain.")
    case_desc = st.text_area("2. Mô tả ngắn về tình huống:", 
                             placeholder="VD: Ứng dụng blockchain minh bạch lịch sử đăng kiểm xe...")
    org_name = st.text_input("3. Tên cơ quan/đơn vị liên quan:", 
                             placeholder="VD: Cục Đăng kiểm Việt Nam")
    if st.button("▶️ Tiếp tục", on_click=next_step, key="step0"):
        pass

# ======== Các bước đánh giá chi tiết nhóm chỉ số ========
elif 1 <= st.session_state.step <= 6:
    # Xác định nhóm và index
    idx = st.session_state.step - 1  # 1→ nhóm 0
    group_name = list(metrics.keys())[idx]
    st.subheader(f"🔧 Bước {st.session_state.step+1}: Đánh giá nhóm \"{group_name}\"")

    # Hiển thị từng chỉ số trong nhóm
    for key, attr in metrics[group_name].items():
        st.write(f"• **{attr['label']}**")
        st.caption(attr["desc"])
        if attr["type"] == "slider":
            st.slider("", attr["min"], attr["max"], value=st.session_state[key], 
                      step=attr["step"], key=key)
        else:
            st.number_input("", min_value=attr["min"], max_value=attr["max"], 
                            step=attr["step"], value=st.session_state[key], key=key)

    # Nút “Tiếp tục” hoặc “Xem kết quả”
    if st.session_state.step < 6:
        if st.button("▶️ Tiếp tục", on_click=next_step, key=f"step{idx+1}"):
            pass
    else:
        if st.button("▶️ Xem kết quả", on_click=next_step, key="final_step"):
            pass

# ======== Bước 7: Kết quả & Biểu đồ ========
elif st.session_state.step == 7:
    st.subheader("📊 Kết quả đánh giá khả thi")
    # Tính điểm trung bình từng nhóm (quy về thang điểm 0-5)
    avg_scores = {}
    for grp_name, grp in metrics.items():
        total = 0
        n = len(grp)
        for key, attr in grp.items():
            raw = st.session_state[key]
            # Nếu có ký hiệu “↓” → độ tốt tỷ lệ nghịch với giá trị
            if "↓" in attr["label"]:
                val = attr["max"] + attr["min"] - raw
            else:
                val = raw
            # Quy về 0-5
            if attr["max"] > 5:
                total += (val / attr["max"]) * 5
            else:
                total += val
        avg_scores[grp_name] = round(total / n, 2)

    # Radar Chart hiển thị 6 nhóm
    radar = go.Figure()
    radar.add_trace(go.Scatterpolar(
        r=list(avg_scores.values()),
        theta=list(avg_scores.keys()),
        fill='toself',
        name='Điểm trung bình'
    ))
    radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
        showlegend=False,
        title="Radar Chart: Điểm trung bình các nhóm yếu tố"
    )
    st.plotly_chart(radar, use_container_width=True)

    # Bar chart so sánh chỉ số thực tế vs benchmark mẫu
    st.markdown("### 📈 So sánh chỉ số thực tế với chuẩn tham chiếu (mẫu)")
    benchmark_vals = {
        "TCH": 60, "COM": 60, "DAV": 50, "SKL": 10,
        "LSG": 4, "DPR": 4, "LRR": 4,
        "ORG": 3, "CHM": 3, "COL": 50,
        "CAPEX": 40, "OPEX": 30, "CBR": 100,
        "TRU": 70, "IND": 30, "USAB": 60,
        "POL": 3, "GLB": 3
    }

    for grp_name, grp in metrics.items():
        fig = go.Figure()
        for key, attr in grp.items():
            raw = st.session_state[key]
            bench = benchmark_vals.get(key, 0)
            if "↓" in attr["label"]:
                actual = attr["max"] + attr["min"] - raw
                bench_val = attr["max"] + attr["min"] - bench
            else:
                actual = raw
                bench_val = bench
            # Quy về 0-5
            if attr["max"] > 5:
                actual = round((actual / attr["max"]) * 5, 2)
                bench_val = round((bench_val / attr["max"]) * 5, 2)
            fig.add_trace(go.Bar(
                name="Thực tế", x=[attr["label"]], y=[actual], marker_color='teal'
            ))
            fig.add_trace(go.Bar(
                name="Chuẩn mẫu", x=[attr["label"]], y=[bench_val], marker_color='orange'
            ))
        fig.update_layout(
            title=f"Nhóm: {grp_name}",
            barmode='group',
            yaxis=dict(title="Điểm (0-5)", range=[0, 5])
        )
        st.plotly_chart(fig, use_container_width=True)

    # Tổng điểm chung và khuyến nghị
    overall = round(sum(avg_scores.values()), 2)
    max_possible = 5 * len(metrics)
    if overall >= max_possible * 0.8:
        level = "✅ Rất khả thi"
    elif overall >= max_possible * 0.6:
        level = "🟡 Khả thi có điều kiện"
    else:
        level = "🔴 Chưa khả thi"

    st.markdown(f"## 🏆 Mức độ khả thi chung: **{level}** (Tổng = {overall}/{max_possible})")
    st.markdown("### 📌 Khuyến nghị:")
    if st.session_state["LSG"] < 3:
        st.warning("- Cải thiện khung pháp lý & chính sách liên quan hồ sơ điện tử, smart contract.")
    if st.session_state["SKL"] < 5:
        st.info("- Đào tạo, tuyển dụng thêm chuyên gia blockchain.")
    if st.session_state["CAPEX"] > 50:
        st.info("- Xem xét blockchain mã nguồn mở để giảm chi phí đầu tư.")
    if st.session_state["TRU"] < 50:
        st.warning("- Tăng cường truyền thông, nâng cao nhận thức công chúng về blockchain.")

    if st.button("🔄 Đánh giá lại", on_click=reset):
        pass
