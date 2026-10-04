import streamlit as st
import random
from datetime import datetime
import copy

st.set_page_config(page_title="SBY MOCK TEST", page_icon="🎓", layout="wide")
try:
    from streamlit_autorefresh import st_autorefresh
    HAS_REFRESH = True
except:
    HAS_REFRESH = False

st.markdown("<h1 style='text-align:center;'>🎓 SBY MOCK TEST</h1>", unsafe_allow_html=True)
st.divider()

EXAM_PATTERN = {
"1. UP Police Constable": {"A-Hindi":37, "B-GK/GS":38, "C-Math":38, "D-Reasoning":37, "time":120},
"2. UP Police SI": {"A-Hindi":40, "B-GK":40, "C-Math":40, "D-Reasoning":40, "time":120},
"3. UPSSSC PET": {"A-Hindi":20, "B-GK":25, "C-Math":25, "D-Reasoning":30, "time":120},
"4. UP Lekhpal": {"A-Hindi":25, "B-GK":25, "C-Math":25, "D-Reasoning":25, "time":90},
"5. UPSSSC VDO": {"A-Hindi":25, "B-GK":25, "C-Math":25, "D-Reasoning":25, "time":90},
"6. SSC GD": {"A-Hindi":20, "B-GK":20, "C-Math":20, "D-Reasoning":20, "time":60},
"7. SSC CGL": {"A-Hindi":25, "B-GK":25, "C-Math":25, "D-Reasoning":25, "time":60},
"8. SSC CHSL": {"A-Hindi":25, "B-GK":25, "C-Math":25, "D-Reasoning":25, "time":60},
"9. SSC MTS": {"A-Hindi":20, "B-GK":20, "C-Math":20, "D-Reasoning":20, "time":90},
"10. Railway Group D": {"A-Hindi":20, "B-GK":20, "C-Math":25, "D-Reasoning":25, "time":90},
"11. RRB NTPC": {"A-Hindi":20, "B-GK":20, "C-Math":30, "D-Reasoning":30, "time":90},
"12. RRB ALP": {"A-Hindi":20, "B-GK":20, "C-Math":20, "D-Reasoning":15, "time":60},
"13. Delhi Police": {"A-Hindi":25, "B-GK":25, "C-Math":25, "D-Reasoning":25, "time":90},
"14. Agniveer Army": {"A-Hindi":20, "B-GK":20, "C-Math":20, "D-Reasoning":15, "time":60},
"15. Airforce X Group": {"A-English":20, "B-GK":20, "C-Math":25, "D-Reasoning":25, "time":60},
"16. Navy SSR": {"A-English":20, "B-GK":20, "C-Math":20, "D-Reasoning":20, "time":60},
"17. Banking PO": {"A-Hindi":30, "B-GK":30, "C-Math":35, "D-Reasoning":35, "time":120},
"18. Banking Clerk": {"A-Hindi":30, "B-GK":30, "C-Math":35, "D-Reasoning":35, "time":60},
"19. CTET": {"A-Hindi":30, "B-GK":30, "C-Math":30, "D-Reasoning":30, "time":150},
"20. UPTET": {"A-Hindi":30, "B-GK":30, "C-Math":30, "D-Reasoning":30, "time":150},
"21. CUET": {"A-Hindi":25, "B-GK":25, "C-Math":25, "D-Reasoning":25, "time":120},
"22. NDA": {"A-English":40, "B-GK":40, "C-Math":40, "D-Reasoning":20, "time":150},
"23. CDS": {"A-English":40, "B-GK":40, "C-Math":40, "D-Reasoning":20, "time":120},
"24. UPPCS Pre": {"A-Hindi":50, "B-GK":50, "C-Math":25, "D-Reasoning":25, "time":120},
"25. UPSC Pre": {"A-Hindi":50, "B-GK":50, "C-Math":25, "D-Reasoning":25, "time":120},
"26. UP Jail Warder": {"A-Hindi":37, "B-GK/GS":38, "C-Math":38, "D-Reasoning":37, "time":120},
}

# === IMPORTANT QUESTION BANKS - PATTERN WISE ===
HINDI_BANK = [
{"q":"'अंधकार' का विलोम है?","o":["प्रकाश","उजाला","दिन","धूप"],"a":"प्रकाश"},
{"q":"'सूर्य' का पर्यायवाची?","o":["दिनकर","निशाकर","सुधाकर","हिमकर"],"a":"दिनकर"},
{"q":"'गंगा' का पर्यायवाची?","o":["भागीरथी","यमुना","सरस्वती","गोदावरी"],"a":"भागीरथी"},
{"q":"'अमृत' का विलोम?","o":["विष","जहर","मृत्यु","काल"],"a":"विष"},
{"q":"रामचरितमानस के रचयिता?","o":["तुलसीदास","सूरदास","कबीर","मीरा"],"a":"तुलसीदास"},
{"q":"'हाथी' का पर्यायवाची?","o":["गज","अश्व","मृग","सिंह"],"a":"गज"},
{"q":"'कमल' का पर्यायवाची?","o":["पंकज","नीरज","जलज","सभी"],"a":"सभी"},
{"q":"'आकाश' का पर्यायवाची?","o":["गगन","नभ","अंबर","सभी"],"a":"सभी"},
{"q":"'अतिथि' का अर्थ?","o":["मेहमान","भगवान","पुजारी","शत्रु"],"a":"मेहमान"},
{"q":"शुद्ध शब्द चुनिए?","o":["उज्ज्वल","उज्वल","उज्जवल","उजवल"],"a":"उज्ज्वल"},
{"q":"'नीर' का अर्थ?","o":["पानी","आकाश","हवा","आग"],"a":"पानी"},
{"q":"'संधि' कितने प्रकार की?","o":["3","2","4","5"],"a":"3"},
{"q":"'समास' के कितने भेद?","o":["6","4","8","5"],"a":"6"},
{"q":"'अलंकार' कितने प्रकार के?","o":["2","3","4","5"],"a":"2"},
{"q":"हिंदी वर्णमाला में वर्ण?","o":["52","48","44","36"],"a":"52"},
]

GK_BANK_HI = [
{"q":"UP में कुल जिले?","o":["75","70","80","78"],"a":"75"},
{"q":"UP की राजधानी?","o":["लखनऊ","कानपुर","आगरा","प्रयागराज"],"a":"लखनऊ"},
{"q":"ताजमहल कहाँ?","o":["आगरा","दिल्ली","जयपुर","मथुरा"],"a":"आगरा"},
{"q":"भारत के प्रथम राष्ट्रपति?","o":["राजेंद्र प्रसाद","नेहरू","गांधी","अंबेडकर"],"a":"राजेंद्र प्रसाद"},
{"q":"संविधान कब लागू हुआ?","o":["26 Jan 1950","15 Aug 1947","26 Nov 1949","2 Oct 1950"],"a":"26 Jan 1950"},
{"q":"ISRO का मुख्यालय?","o":["बेंगलुरु","दिल्ली","मुंबई","चेन्नई"],"a":"बेंगलुरु"},
{"q":"गंगा की लंबाई?","o":["2525 km","2400 km","2700 km","3000 km"],"a":"2525 km"},
{"q":"UP का राजकीय पशु?","o":["बारहसिंगा","शेर","हाथी","बाघ"],"a":"बारहसिंगा"},
{"q":"लखनऊ किस नदी पर?","o":["गोमती","गंगा","यमुना","सरयू"],"a":"गोमती"},
{"q":"कुंभ मेला कहाँ नहीं लगता?","o":["नासिक","प्रयागराज","हरिद्वार","वाराणसी"],"a":"वाराणसी"},
{"q":"भारत का राष्ट्रीय पक्षी?","o":["मोर","तोता","कबूतर","हंस"],"a":"मोर"},
{"q":"2024 ओलंपिक कहाँ?","o":["पेरिस","टोक्यो","लंदन","बीजिंग"],"a":"पेरिस"},
{"q":"UP के प्रथम मुख्यमंत्री?","o":["गोविंद वल्लभ पंत","योगी","मुलायम","कल्याण"],"a":"गोविंद वल्लभ पंत"},
{"q":"संगम किसका?","o":["गंगा-यमुना","गंगा-सरयू","यमुना-सरयू","सभी"],"a":"गंगा-यमुना"},
{"q":"भारत का सबसे बड़ा राज्य?","o":["राजस्थान","UP","MP","महाराष्ट्र"],"a":"राजस्थान"},
]

MATH_BANK_HI = [
{"q":"15 का 20% कितना?","o":["3","4","5","6"],"a":"3"},
{"q":"एक वस्तु 20% लाभ पर 120 में बिकी, लागत?","o":["100","110","90","80"],"a":"100"},
{"q":"2, 4, 8, 16 का औसत?","o":["7.5","8","10","6"],"a":"7.5"},
{"q":"5² + 12² =?","o":["13²","25","169","144"],"a":"13²"},
{"q":"10 का 10% + 20 का 20%?","o":["5","6","4","10"],"a":"5"},
{"q":"एक घन का आयतन 64, भुजा?","o":["4","8","6","2"],"a":"4"},
{"q":"sin 90° का मान?","o":["1","0","-1","1/2"],"a":"1"},
{"q":"π का मान लगभग?","o":["3.14","3","22/7","दोनों A और C"],"a":"दोनों A और C"},
{"q":"एक त्रिभुज के कोणों का योग?","o":["180°","90°","360°","270°"],"a":"180°"},
{"q":"12 x 15 =?","o":["180","150","120","200"],"a":"180"},
{"q":"50 का 60%?","o":["30","20","40","25"],"a":"30"},
{"q":"1000 का 10% =?","o":["100","10","1000","50"],"a":"100"},
{"q":"चक्रवृद्धि ब्याज में A =?","o":["P(1+R/100)^T","P+RT","P*R*T","P/T"],"a":"P(1+R/100)^T"},
{"q":"एक कार 60 km/h से 2 घंटे में दूरी?","o":["120 km","60 km","100 km","80 km"],"a":"120 km"},
{"q":"LCM of 4,6?","o":["12","24","6","2"],"a":"12"},
]

REAS_BANK_HI = [
{"q":"2,4,8,16 अगला?","o":["32","24","20","18"],"a":"32"},
{"q":"A,C,E,G अगला?","o":["I","H","J","K"],"a":"I"},
{"q":"5,10,15,20 अगला?","o":["25","30","35","40"],"a":"25"},
{"q":"यदि CAT=24, DOG=?","o":["26","24","20","28"],"a":"26"},
{"q":"राम श्याम से बड़ा, श्याम मोहन से बड़ा, सबसे बड़ा?","o":["राम","श्याम","मोहन","सभी बराबर"],"a":"राम"},
{"q":"घड़ी में 3 बजे कोण?","o":["90°","180°","45°","60°"],"a":"90°"},
{"q":"BLOOD का कूट?","o":["सम्बन्ध","परिवार","रक्त","शरीर"],"a":"रक्त"},
{"q":"विषम चुनिए: गाय, कुत्ता, शेर, कार","o":["कार","गाय","कुत्ता","शेर"],"a":"कार"},
{"q":"अंग्रेजी में कितने स्वर?","o":["5","6","21","26"],"a":"5"},
{"q":"दर्पण में ABC का प्रतिबिंब?","o":["CBA","ABC","उल्टा","सीधा"],"a":"CBA"},
]

GK_EN = [
{"q":"How many districts in UP?","o":["75","70","80","78"],"a":"75"},
{"q":"Capital of UP?","o":["Lucknow","Kanpur","Agra","Noida"],"a":"Lucknow"},
{"q":"Where is Taj Mahal?","o":["Agra","Delhi","Jaipur","Lucknow"],"a":"Agra"},
{"q":"First President of India?","o":["Rajendra Prasad","Nehru","Gandhi","Ambedkar"],"a":"Rajendra Prasad"},
{"q":"When Constitution implemented?","o":["26 Jan 1950","15 Aug 1947","26 Nov 1949","2 Oct 1950"],"a":"26 Jan 1950"},
]
MATH_EN = [
{"q":"20% of 15?","o":["3","4","5","2"],"a":"3"},
{"q":"Average of 2,4,8,16?","o":["7.5","8","10","6"],"a":"7.5"},
{"q":"5²+12²=?","o":["13²","25","169","144"],"a":"13²"},
{"q":"LCM of 4,6?","o":["12","24","6","2"],"a":"12"},
]
REAS_EN = [
{"q":"2,4,8,16 next?","o":["32","24","20","18"],"a":"32"},
{"q":"A,C,E,G next?","o":["I","H","J","K"],"a":"I"},
]
ENG_BANK = [
{"q":"Antonym of 'Big'?","o":["Small","Large","Huge","Great"],"a":"Small"},
{"q":"Synonym of 'Happy'?","o":["Joyful","Sad","Angry","Tired"],"a":"Joyful"},
{"q":"Plural of 'Child'?","o":["Children","Childs","Childrens","Childes"],"a":"Children"},
{"q":"Past of 'Go'?","o":["Went","Gone","Going","Goes"],"a":"Went"},
]

def make_big(bank, n): return (bank * ((n//len(bank))+1))[:n]
H_BANK=make_big(HINDI_BANK,100); GK_HI=make_big(GK_BANK_HI,100); M_HI=make_big(MATH_BANK_HI,100); R_HI=make_big(REAS_BANK_HI,100)
GK_E=make_big(GK_EN,100); M_E=make_big(MATH_EN,100); R_E=make_big(REAS_EN,100); E_BANK=make_big(ENG_BANK,100)

def get_qs(sec,cnt,is_hindi):
    if "Hindi" in sec: base=H_BANK
    elif "English" in sec: base=E_BANK if not is_hindi else H_BANK
    else:
        if is_hindi: base=GK_HI if "GK" in sec else M_HI if "Math" in sec else R_HI
        else: base=GK_E if "GK" in sec else M_E if "Math" in sec else R_E
    return [copy.deepcopy(q) for q in random.sample(base, min(cnt, len(base)))]

if "start" not in st.session_state:
    st.session_state.start=False; st.session_state.finished=False

if not st.session_state.start:
    exam=st.selectbox("परीक्षा चुनें", list(EXAM_PATTERN.keys()))
    lang=st.selectbox("भाषा", ["Hindi - हिंदी में", "English - अंग्रेजी में"])
    st.success(f"✅ {exam} | {lang} | {EXAM_PATTERN[exam]['time']} min")
    if st.button("🚀 शुरू करें", type="primary", use_container_width=True):
        is_hindi="Hindi" in lang
        st.session_state.start=True; st.session_state.exam_name=exam; st.session_state.is_hindi=is_hindi
        st.session_state.mins=EXAM_PATTERN[exam]["time"]
        st.session_state.pattern={k:v for k,v in EXAM_PATTERN[exam].items() if k!="time"}
        st.session_state.full_q={sec:get_qs(sec,cnt,is_hindi) for sec,cnt in st.session_state.pattern.items()}
        st.session_state.sections=list(st.session_state.full_q.keys()); st.session_state.sec=st.session_state.sections[0]
        st.session_state.q_idx=0; st.session_state.answers={}; st.session_state.t0=datetime.now(); st.session_state.finished=False
        st.rerun()
else:
    if HAS_REFRESH and not st.session_state.finished: st_autorefresh(interval=1000, key="timer")
    left=st.session_state.mins*60 - int((datetime.now()-st.session_state.t0).total_seconds())
    if left<=0 and not st.session_state.finished: st.session_state.finished=True; st.rerun()
    if not st.session_state.finished:
        m,s=divmod(max(0,left),60)
        st.markdown(f"<div style='background:#ff4b4b; padding:12px; border-radius:10px; text-align:center;'><h2 style='color:white; margin:0;'>⏰ {m:02d}:{s:02d} | {st.session_state.exam_name}</h2></div>", unsafe_allow_html=True)
        st.write("")
        cols=st.columns(len(st.session_state.sections))
        for idx,sec in enumerate(st.session_state.sections):
            done=sum(1 for k in st.session_state.answers if k.startswith(sec)); total=len(st.session_state.full_q[sec])
            if cols[idx].button(f"{sec} {done}/{total}", key=f"sec_{idx}", type="primary" if sec==st.session_state.sec else "secondary", use_container_width=True):
                st.session_state.sec=sec; st.session_state.q_idx=0; st.rerun()
        st.divider()
        col_main,col_pal=st.columns([1.8,1.2])
        with col_main:
            q_list=st.session_state.full_q[st.session_state.sec]
            cur=q_list[st.session_state.q_idx]
            st.subheader(f"{st.session_state.sec} - Q{st.session_state.q_idx+1}. {cur['q']}")
            key=f"{st.session_state.sec}_{st.session_state.q_idx}"
            def save_ans(): st.session_state.answers[key]=st.session_state[f"r_{key}"]
            st.radio("उत्तर चुनें:", cur['o'], index=cur['o'].index(st.session_state.answers.get(key)) if st.session_state.answers.get(key) in cur['o'] else None, key=f"r_{key}", on_change=save_ans)
            b1,b2,b3=st.columns(3)
            with b1:
                if st.button("⬅️ पीछे", disabled=(st.session_state.q_idx==0), use_container_width=True):
                    st.session_state.q_idx-=1; st.rerun()
            with b2:
                if st.button("⏭️ Next", use_container_width=True):
                    st.session_state.q_idx=min(st.session_state.q_idx+1, len(q_list)-1); st.rerun()
            with b3:
                if st.button("✅ Save & Next", type="primary", use_container_width=True):
                    if st.session_state.q_idx < len(q_list)-1: st.session_state.q_idx+=1
                    else:
                        i=st.session_state.sections.index(st.session_state.sec)
                        if i < len(st.session_state.sections)-1: st.session_state.sec=st.session_state.sections[i+1]; st.session_state.q_idx=0
                    st.rerun()
        with col_pal:
            st.markdown(f"#### 📋 {st.session_state.sec}")
            q_list=st.session_state.full_q[st.session_state.sec]
            for r in range(0,len(q_list),5):
                ccols=st.columns(5, gap="small")
                for c in range(5):
                    qn=r+c
                    if qn>=len(q_list): continue
                    k=f"{st.session_state.sec}_{qn}"
                    is_done=k in st.session_state.answers; is_cur=qn==st.session_state.q_idx
                    label=f"{qn+1}✓" if is_done else str(qn+1)
                    if is_cur: label=f"[{qn+1}]"
                    if ccols[c].button(label, key=f"pal_{k}", type="primary" if (is_done or is_cur) else "secondary", use_container_width=True):
                        st.session_state.q_idx=qn; st.rerun()
            if st.button("🏁 FINAL SUBMIT", type="primary", use_container_width=True):
                st.session_state.finished=True; st.rerun()
    else:
        st.balloons()
        st.markdown("## 📊 तुम्हारा रिजल्ट")
        total_q=sum(len(v) for v in st.session_state.full_q.values())
        correct=0; attempted=0
        for sec,qlist in st.session_state.full_q.items():
            for idx,q in enumerate(qlist):
                k=f"{sec}_{idx}"
                if k in st.session_state.answers:
                    attempted+=1
                    if st.session_state.answers[k]==q['a']: correct+=1
        c1,c2,c3,c4=st.columns(4)
        c1.metric("कुल", total_q); c2.metric("Attempted", attempted); c3.metric("सही", correct); c4.metric("स्कोर", f"{correct/total_q*100:.1f}%")
        st.divider()
        for sec,qlist in st.session_state.full_q.items():
            with st.expander(f"{sec} - Detail"):
                for idx,q in enumerate(qlist):
                    k=f"{sec}_{idx}"; your=st.session_state.answers.get(k,"Not Attempted"); right=q['a']
                    if your=="Not Attempted":
                        st.markdown(f"<div style='background:#f0f0f0; padding:10px; border-left:5px solid grey; margin-bottom:6px;'><b>Q{idx+1}. {q['q']}</b><br>⚪ छोड़ दिया | सही: <b>{right}</b></div>", unsafe_allow_html=True)
                    elif your==right:
                        st.markdown(f"<div style='background:#e6ffe6; padding:10px; border-left:5px solid green; margin-bottom:6px;'><b>Q{idx+1}. {q['q']}</b><br>✅ सही! तुम्हारा: <b>{your}</b></div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div style='background:#ffe6e6; padding:10px; border-left:5px solid red; margin-bottom:6px;'><b>Q{idx+1}. {q['q']}</b><br>❌ गलत! तुम्हारा: <b>{your}</b> | सही: <b>{right}</b></div>", unsafe_allow_html=True)
        if st.button("🔄 नया टेस्ट", type="primary", use_container_width=True):
            st.session_state.start=False; st.session_state.finished=False; st.rerun()