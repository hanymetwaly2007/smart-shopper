import streamlit as st
import os
from google import genai
from google.genai import types

# إعداد واجهة وتصميم الصفحة
st.set_page_config(page_title="رادار المشتريات والصفقات", layout="centered", page_icon="🛒")

st.markdown("<h2 style='text-align: center;'>🛒 رادار الصفقات وأحدث الإصدارات</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>اكتشف أحدث إصدار عالمي وأقل سعر متوفر اليوم في متاجر الرياض</p>", unsafe_allow_html=True)

# جلب المفتاح بأمان من الإعدادات السحابية
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

query = st.text_input("ما هو المنتج أو الجهاز الذي تبحث عنه؟", placeholder="مثال: قلاية هوائية، شواية ذكية، مكواة بخار...")

if st.button("فحص العروض وأحدث موديل", use_container_width=True):
    if not query.strip():
        st.warning("يرجى كتابة اسم المنتج أولاً.")
    elif not api_key:
        st.error("مفتاح API غير متوفر. يرجى إضافته في إعدادات Secrets.")
    else:
        with st.spinner("جاري مسح المتاجر وتحديث أحدث الأسعار في الرياض..."):
            try:
                client = genai.Client(api_key=api_key)
                prompt = f"""
                المستخدم يريد شراء أو الاستفسار عن: {query}
                قم بالبحث اللحظي المباشر عبر الإنترنت وقدم تقريراً استشارياً دقيقاً وشاملاً:
                1. تحديد أحدث وأفضل إصدار عالمي متاح حالياً بالسوق ومطابق لكهرباء 220V و 50/60Hz.
                2. مسح ومقارنة الأسعار اليوم في متاجر الرياض (أمازون السعودية، إكسترا، نون، ساكو).
                3. توضيح أي أكواد خصم أو عروض بنكية متاحة الآن.
                4. تقديم جدول مقارنة واضح وختم التقرير بنصيحة 'الصفقة الرابحة'.
                """
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        tools=[types.Tool(google_search=types.GoogleSearch())]
                    )
                )
                st.success("تم حصر البيانات بنجاح!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ أثناء الفحص: {e}")
