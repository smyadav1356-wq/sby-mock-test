import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="SBY MOCK TEST", page_icon="🎓", layout="wide")

try:
    from streamlit_autorefresh import st_autorefresh
    HAS_REFRESH = True
except:
    HAS_REFRESH = False

st.markdown("""
<style>
div[data-testid="stButton"] > button { white-space: nowrap!important; height: 38px!important; font-size: 14px!important; }
</style>
<h1 style='text-align:center;'>🎓 SBY MOCK TEST</h1>
""", unsafe_allow_html=True)
st.divider()

EXAM_PATTERN = {
"1. UP Police Constable": {"A-Hindi":37, "B-GK/GS":38, "C-Math":38, "D-Reasoning":37, "time":120},
"2. UP Police SI": {"A-Hindi":40, "B-Law/GS":40, "C-Maths":40, "D-Reasoning":40, "time":120},
"3. SSC CGL": {"A-Reasoning":25, "B-GK":25, "C-Maths":25, "D-English":25, "time":60},
"4. SSC CHSL": {"A-Reasoning":25, "B-GK":25, "C-Maths":25, "D-English":25, "time":60},
"5. SSC GD": {"A-Hindi":20, "B-GK":20, "C-Maths":20, "D-Reasoning":20, "time":60},
"6. SSC MTS": {"A-Reasoning":20, "B-GK":20, "C-Maths":20, "D-English":20, "time":90},
"7. Railway NTPC": {"A-Maths":30, "B-Reasoning":30, "C-GK/GS":40, "time":90},
"8. Railway Group D": {"A-Maths":25, "B-Reasoning":25, "C-Science":25, "D-GK":25, "time":90},
"9. IBPS PO": {"A-English":30, "B-Maths":35, "C-Reasoning":35, "time":60},
"10. IBPS Clerk": {"A-English":30, "B-Maths":35, "C-Reasoning":35, "time":60},
"11. CTET": {"A-CDP":30, "B-Hindi":30, "C-Maths/Sci":30, "D-EVS/SST":30, "E-English":30, "time":150},
"12. UPTET": {"A-CDP":30, "B-Hindi":30, "C-Maths":30, "D-GK":30, "E-English":30, "time":150},
"13. Bihar Police": {"A-Hindi":30, "B-GK":30, "C-Maths":20, "D-Reasoning":20, "time":120},
"14. Bihar SI": {"A-Hindi":40, "B-GK":40, "C-Maths":40, "D-Reasoning":40, "time":120},
}
for i in range(15, 27):
    EXAM_PATTERN[f"{i}. Other Exam {i}"] = {"A-Hindi":25, "B-GK":25, "C-Maths":25, "D-Reasoning":25, "time":60}

BANK_HI = {
"Hindi": [{"q":"'अंधा' का विलोम क्या है?","o":["आँख वाला","काना","सूझ","देखने वाला"],"a":"आँख वाला"},{"q":"'गंगा' का पर्यायवाची क्या है?","o":["भागीरथी","यमुना","गोदावरी","सरयू"],"a":"भागीरथी"},{"q":"शुद्ध शब्द चुनें?","o":["अनुशासन","अनुसाशन","अनुशाशन","अनुसासन"],"a":"अनुशासन"},{"q":"'कमल' का पर्यायवाची नहीं है?","o":["पंकज","नीरज","जलज","पत्थर"],"a":"पत्थर"}]*15,
"GK": [{"q":"UP का राजकीय पक्षी क्या है?","o":["सारस","मोर","तोता","कोयल"],"a":"सारस"},{"q":"UP में कुल जिले कितने हैं?","o":["75","78","80","70"],"a":"75"},{"q":"ताजमहल कहाँ है?","o":["आगरा","लखनऊ","कानपुर","वाराणसी"],"a":"आगरा"},{"q":"धारा 302 किससे संबंधित है?","o":["हत्या","चोरी","दहेज","धोखा"],"a":"हत्या"},{"q":"UP पुलिस मुख्यालय कहाँ है?","o":["लखनऊ","कानपुर","प्रयागराज","आगरा"],"a":"लखनऊ"},{"q":"संविधान कब लागू हुआ?","o":["26 Jan 1950","15 Aug 1947","26 Nov 1949","2 Oct 1950"],"a":"26 Jan 1950"},{"q":"भारत के पहले राष्ट्रपति?","o":["Rajendra Prasad","Nehru","Gandhi","Patel"],"a":"Rajendra Prasad"}]*10,
"Math": [{"q":"12, 18, 27 का HCF क्या है?","o":["3","6","9","12"],"a":"3"},{"q":"20 का 30% + 30 का 20% =?","o":["12","10","14","18"],"a":"12"},{"q":"1 KM में कितने मीटर?","o":["1000","100","10","10000"],"a":"1000"}]*20,
"Reasoning": [{"q":"A, B, C, X में विषम क्या है?","o":["X","A","B","C"],"a":"X"},{"q":"2,4,8,16 अगला क्या?","o":["32","24","20","18"],"a":"32"}]*20,
"English": [{"q":"Brave का Synonym?","o":["Courageous","Fearful","Weak","Lazy"],"a":"Courageous"}]*40,
}

BANK_EN = {
"Hindi": [{"q":"What is antonym of Blind?","o":["Sighted","One-eyed","Vision","Seeing"],"a":"Sighted"}]*40,
"GK": [{"q":"State bird of UP?","o":["Sarus Crane","Peacock","Parrot","Koel"],"a":"Sarus Crane"},{"q":"How many districts in UP?","o":["75","78","80","70"],"a":"75"},{"q":"Where is Taj Mahal?","o":["Agra","Lucknow","Kanpur","Varanasi"],"a":"Agra"},{"q":"Section 302 related to?","o":["Murder","Theft","Dowry","Fraud"],"a":"Murder"},{"q":"First President of India?","o":["Rajendra Prasad","Nehru","Gandhi","Patel"],"a":"Rajendra Prasad"},{"q":"When Constitution implemented?","o":["26 Jan 1950","15 Aug 1947","26 Nov 1949","2 Oct 1950"],"a":"26 Jan 1950"}]*15,
"Math": [{"q":"HCF of 12,18,27?","o":["3","6","9","12"],"a":"3"}]*40,
"Reasoning": [{"q":"Find odd: A,B,C,X?","o":["X","A","B","C"],"a":"X"}]*40,
"English": [{"q":"Synonym of Brave?","o":["Courageous","Fearful","Weak","Lazy"],"a":"Courageous"}]*40,
}

def get_qs(section_name, count, is_hindi):
    BANK = BANK_HI if is_hindi else BANK_EN
    if "Hindi" in section_name: base = BANK["Hindi"]
    elif "GK" in section_name or "GS" in section_name or "Law" in section_name or "CDP" in section_name or "EVS" in section_name or "SST" in section_name: base = BANK["GK"]
    elif "Math" in section_name or "Maths" in section_name: base = BANK["Math"]
    elif "Reason" in section_name: base = BANK["Reasoning"]
    elif "Science" in section_name or "Sci" in section_name: base = BANK["GK"]
    else: base = BANK["English"]
    qs = (base * ((count//len(base))+3))[:count]
    random.shuffle(qs)
    return qs

if "start" not in st.session_state:
    st.session_state.start=False
    st.session_state.finished=False

if not st.session_state.start:
    col1, col2 = st.columns(2)
    with col1:
        exam = st.selectbox("परीक्षा चुनें", list(EXAM_PATTERN.keys()))
    with col2:
        lang = st.selectbox("पेपर किस मोड में?", ["Hindi - हिंदी में", "English - अंग्रेजी में"])
    is_hindi = "Hindi" in lang
    pattern = EXAM_PATTERN[exam]
    mins = pattern["time"]
    st.success(f"✅ {exam} | {lang}")
    p_cols = st.columns(len([k for k in pattern if k!="time"]))
    for idx, (k,v) in enumerate([(k,v) for k,v in pattern.items() if k!="time"]):
        p_cols[idx].metric(k, f"{v} Q")
    st.info(f"⏱️ समय: {mins} मिनट | कुल: {sum(v for k,v in pattern.items() if k!='time')} Q")
    if st.button(f"🚀 शुरू करें - START {exam}", type="primary", use_container_width=True):
        st.session_state.start=True
        st.session_state.exam_name=exam
        st.session_state.is_hindi=is_hindi
        st.session_state.lang=lang
        st.session_state.mins=mins
        st.session_state.pattern={k:v for k,v in pattern.items() if k!="time"}
        st.session_state.full_q={}
        for sec,cnt in st.session_state.pattern.items():
            st.session_state.full_q[sec]=get_qs(sec,cnt,is_hindi)
        st.session_state.sections=list(st.session_state.full_q.keys())
        st.session_state.sec=st.session_state.sections[0]
        st.session_state.q_idx=0
        st.session_state.answers={}
        st.session_state.t0=datetime.now()
        st.session_state.finished=False
        st.rerun()
else:
    is_running = not st.session_state.finished
    if is_running and HAS_REFRESH:
        st_autorefresh(interval=1000, key="timer")
    elapsed = int((datetime.now()-st.session_state.t0).total_seconds())
    left = st.session_state.mins*60 - elapsed
    if left<=0 and is_running:
        st.session_state.finished=True
        st.rerun()
    if is_running:
        m,s = divmod(max(0,left),60)
        st.markdown(f"<div style='background:#ff4b4b; padding:10px; border-radius:10px; text-align:center;'><h2 style='color:white; margin:0;'>⏰ {m:02d}:{s:02d} | {st.session_state.exam_name}</h2></div>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='text-align:center; color:green;'>✅ Paper Submitted</h3>", unsafe_allow_html=True)

    if not st.session_state.finished:
        cols = st.columns(len(st.session_state.sections))
        for idx, sec in enumerate(st.session_state.sections):
            done = sum(1 for k in st.session_state.answers if k.startswith(sec))
            total = len(st.session_state.full_q[sec])
            if cols[idx].button(f"{sec}\n{done}/{total}", key=f"sec_{idx}", type="primary" if sec==st.session_state.sec else "secondary", use_container_width=True):
                st.session_state.sec=sec
                st.session_state.q_idx=0
                st.rerun()
        st.divider()
        col_main, col_pal = st.columns([2.2,1])
        with col_main:
            q_list = st.session_state.full_q[st.session_state.sec]
            cur = q_list[st.session_state.q_idx]
            st.subheader(f"{st.session_state.sec} - Q{st.session_state.q_idx+1}. {cur['q']}")
            key = f"{st.session_state.sec}_{st.session_state.q_idx}"
            choice = st.radio("उत्तर चुनें:", cur['o'], index=cur['o'].index(st.session_state.answers.get(key)) if st.session_state.answers.get(key) in cur['o'] else None, key=f"r_{key}")
            b1,b2,b3 = st.columns(3)
            with b1:
                if st.button("⬅️ पीछे", disabled=(st.session_state.q_idx==0), use_container_width=True):
                    st.session_state.q_idx-=1
                    st.rerun()
            with b2:
                if st.button("⏭️ छोड़ें", use_container_width=True):
                    st.session_state.q_idx=min(st.session_state.q_idx+1, len(q_list)-1)
                    st.rerun()
            with b3:
                if st.button("✅ Save & Next", type="primary", use_container_width=True):
                    if choice: st.session_state.answers[key]=choice
                    if st.session_state.q_idx < len(q_list)-1:
                        st.session_state.q_idx+=1
                    else:
                        idx = st.session_state.sections.index(st.session_state.sec)
                        if idx < len(st.session_state.sections)-1:
                            st.session_state.sec=st.session_state.sections[idx+1]
                            st.session_state.q_idx=0
                    st.rerun()
        with col_pal:
            st.markdown(f"#### 📋 {st.session_state.sec}")
            q_list = st.session_state.full_q[st.session_state.sec]
            for r in range(0, len(q_list), 5):
                ccols = st.columns(5)
                for c in range(5):
                    qn = r+c
                    if qn>=len(q_list): continue
                    k = f"{st.session_state.sec}_{qn}"
                    is_done = k in st.session_state.answers
                    is_cur = qn==st.session_state.q_idx
                    label = f"{qn+1}✓" if is_done else str(qn+1)
                    if is_cur: label=f"▶{qn+1}"
                    if ccols[c].button(label, key=f"p_{k}", type="primary" if (is_done or is_cur) else "secondary", use_container_width=True):
                        st.session_state.q_idx=qn
                        st.rerun()
            st.divider()
            if st.button("🏁 FINAL SUBMIT", type="primary", use_container_width=True):
                st.session_state.finished=True
                st.rerun()
    else:
        st.balloons()
        total=0
        correct=0
        for sec in st.session_state.sections:
            qs = st.session_state.full_q[sec]
            c = sum(1 for i,q in enumerate(qs) if st.session_state.answers.get(f"{sec}_{i}")==q['a'])
            st.write(f"**{sec}**: {c}/{len(qs)}")
            correct+=c
            total+=len(qs)
        st.success(f"🎉 FINAL SCORE: {correct}/{total} = {correct/total*100:.1f}%")

        # ===== LANGUAGE FIX - YAHI MAIN CHANGE HAI =====
        is_hindi = st.session_state.is_hindi
        for sec in st.session_state.sections:
            with st.expander(f"{sec} - Detail", expanded=(sec==st.session_state.sections[0])):
                qs = st.session_state.full_q[sec]
                for i,q in enumerate(qs):
                    key = f"{sec}_{i}"
                    user_ans = st.session_state.answers.get(key)
                    correct_ans = q['a']
                    q_text = q['q']
                    if user_ans is None:
                        if is_hindi:
                            msg = f"⚪ छोड़ दिया | सही: {correct_ans}"
                        else:
                            msg = f"⚪ Skipped | Correct: {correct_ans}"
                        st.markdown(f"<div style='background:#f0f0f0; padding:10px; margin:5px 0; border-left:5px solid gray;'><b>Q{i+1}. {q_text}</b><br>{msg}</div>", unsafe_allow_html=True)
                    elif user_ans == correct_ans:
                        if is_hindi:
                            msg = f"✅ सही! तुम्हारा: {user_ans}"
                        else:
                            msg = f"✅ Correct! Your answer: {user_ans}"
                        st.markdown(f"<div style='background:#d4edda; padding:10px; margin:5px 0; border-left:5px solid green;'><b>Q{i+1}. {q_text}</b><br>{msg}</div>", unsafe_allow_html=True)
                    else:
                        if is_hindi:
                            msg = f"❌ गलत! तुम्हारा: {user_ans} | सही: {correct_ans}"
                        else:
                            msg = f"❌ Wrong! Your: {user_ans} | Correct: {correct_ans}"
                        st.markdown(f"<div style='background:#f8d7da; padding:10px; margin:5px 0; border-left:5px solid red;'><b>Q{i+1}. {q_text}</b><br>{msg}</div>", unsafe_allow_html=True)

        if st.button("🔄 नया टेस्ट", use_container_width=True):
            st.session_state.start=False
            st.session_state.finished=False
            st.rerun()