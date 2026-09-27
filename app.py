import os
import urllib.parse
import streamlit as st
from google import genai
from google.genai import types

# إعداد واجهة الصفحة
st.set_page_config(page_title="المتسوق الذكي - الصفقة المباشرة", layout="centered", page_icon="🎯")

st.markdown("<h2 style='text-align: center;'>🎯 رادار الصفقات المباشرة</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>أفضل جهاز مطابق لمواصفات السعودية (220V) مع رابط الشراء المباشر فوراً</p>", unsafe_allow_html=True)

# جلب مفتاح API بأمان
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

query = st.text_input("اكتب اسم الجهاز أو المنتج الذي تبحث عنه:", placeholder="...مثال: قلاية هوائية، شواية ذكية، مفرمة لحم")

if st.button("اعثر على أفضل صفقة ورابط الشراء المباشر 🚀", use_container_width=True):
    if not query.strip():
        st.warning("يرجى كتابة اسم المنتج أولاً.")
    elif not api_key:
        st.error("مفتاح API غير متوفر في الإعدادات.")
    else:
        with st.spinner("جاري استخراج السلعة الفائزة ورابط الشراء المباشر..."):
            try:
                client = genai.Client(api_key=api_key)
                prompt = f"""أنت مستشار مشتريات محترف في الرياض.
المستخدم يبحث عن: {query}

المطلوب إجابة مختصرة ومركزة جداً بدون حشو:
1. اختر منتجاً واحداً فقط يعتبر 'الصفقة الرابحة والأفضل عالمياً' المطابق لكهرباء السعودية 220V-240V وتردد 50/60Hz.
2. اذكر اسمه التجاري الكامل ورقم الموديل الدقيق بالإنجليزية (Model Number).
3. متوسط سعره بالريال السعودي اليوم في متاجر الرياض وأين يتوفر بأقل سعر.
4. جملتين فقط عن أهم ميزاته ولماذا هو الخيار الأفضل.
5. ضع رابطاً مباشراً لصفحة هذا المنتج بعينه على أمازون السعودية ونون وإكسترا."""

                try:
                    response = client.models.generate_content(
                        model='gemini-3.8-flash',
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            tools=[types.Tool(google_search=types.GoogleSearch())]
                        )
                    )
                except Exception:
                    response = client.models.generate_content(
                        model='gemini-3.8-flash',
                        contents=prompt
                    )

                st.success("تم اختيار الصفقة الرابحة بدقة!")
                st.markdown(response.text)

                # أزرار الشراء المباشرة الموجهة بدقة للمنتج
                st.markdown("---")
                st.markdown("#### 🛒 اضغط هنا لفتح صفحة المنتج مباشرة:")
                search_term = urllib.parse.quote(f"{query} 220V")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.link_button("🟢 فتح المنتج في أمازون السعودية", f"https://www.amazon.sa/s?k={search_term}&ref=nb_sb_noss", use_container_width=True)
                with col2:
                    st.link_button("🟡 فتح المنتج في نون السعودية", f"https://www.noon.com/saudi-ar/search/?q={search_term}", use_container_width=True)

            except Exception as e:
                st.error(f"حدث خطأ أثناء الفحص: {e}")
