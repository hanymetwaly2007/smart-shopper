import os
import re
import urllib.parse
import streamlit as st
from google import genai

# إعداد واجهة وتصميم الصفحة
st.set_page_config(page_title="المتسوق الذكي - المنتج المباشر", layout="centered", page_icon="🎯")

st.markdown("<h2 style='text-align: center;'>🎯 رادار الصفقات المباشرة</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>تحديد أفضل جهاز مطابق لمواصفات السعودية (220V) والوصول لصفحة المنتج مباشرة</p>", unsafe_allow_html=True)

# جلب مفتاح API بأمان
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

query = st.text_input("اكتب اسم الجهاز أو المنتج الذي تبحث عنه:", placeholder="...مثال: قلاية هوائية، شواية ذكية، مفرمة لحم")

if st.button("اعثر على أفضل صفقة ورابط الشراء المباشر 🚀", use_container_width=True):
    if not query.strip():
        st.warning("يرجى كتابة اسم المنتج أولاً.")
    elif not api_key:
        st.error("مفتاح API غير متوفر في الإعدادات.")
    else:
        with st.spinner("جاري استخراج السلعة الفائزة وتجهيز رابط الشراء المباشر..."):
            client = genai.Client(api_key=api_key)
            prompt = f"""أنت مستشار مشتريات إلكتروني فائق الدقة في السعودية.
المستخدم يبحث عن: {query}

المطلوب بدقة تامة ومباشرة وبدون حشو:
1. حدد منتجاً واحداً فقط يعتبر 'الصفقة الرابحة والأفضل عالمياً' المطابق لكهرباء السعودية 220V-240V وتردد 50/60Hz.
2. اذكر اسمه باللغة الإنجليزية ورقم الموديل الدقيق جداً (Exact Brand and Model Number).
3. اكتب في سطر منفصل في نهاية التقرير بالضبط هكذا:
MODEL_EXACT: [اكتب هنا اسم الماركة ورقم الموديل بالإنجليزية فقط مثل Philips HD9270/90 أو Ninja AF160ME]
4. متوسط سعره بالريال السعودي في الرياض اليوم.
5. أهم 3 مميزات رئيسية باختصار شديد تجعله الأفضل.
6. ختام بنصيحة للشراء."""

            # تجربة الموديلات بالترتيب لتفادي ضغط السيرفرات (503) نهائياً
            models_to_try = ['gemini-3.8-flash', 'gemini-3.5-flash', 'gemini-2.5-flash']
            response = None

            for m in models_to_try:
                try:
                    response = client.models.generate_content(
                        model=m,
                        contents=prompt
                    )
                    if response and response.text:
                        break
                except Exception:
                    continue

            if response and response.text:
                st.success("تم اختيار المنتج الفائز بنجاح!")
                
                # استخراج اسم ورقم الموديل الدقيق لبناء رابط الشراء المباشر
                raw_text = response.text
                exact_model = query
                model_match = re.search(r"MODEL_EXACT:\s*(.+)", raw_text)
                if model_match:
                    exact_model = model_match.group(1).strip().replace("[", "").replace("]", "")
                    clean_text = raw_text.replace(model_match.group(0), "")
                else:
                    clean_text = raw_text

                st.markdown(clean_text)

                # أزرار الشراء الموجهة للسلعة بعينها
                st.markdown("---")
                st.markdown(f"#### 🛒 رابط شراء السلعة بعينها: `{exact_model}`")
                
                encoded_exact = urllib.parse.quote(exact_model)
                col1, col2 = st.columns(2)
                with col1:
                    st.link_button(
                        f"🟢 فتح {exact_model} في أمازون",
                        f"https://www.amazon.sa/s?k={encoded_exact}",
                        use_container_width=True
                    )
                with col2:
                    st.link_button(
                        f"🟡 فتح {exact_model} في نون",
                        f"https://www.noon.com/saudi-ar/search/?q={encoded_exact}",
                        use_container_width=True
                    )
            else:
                st.error("خوادم الذكاء الاصطناعي تشهد ضغطاً مؤقتاً، يرجى إعادة المحاولة بعد بضع ثوانٍ.")
