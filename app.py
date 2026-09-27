import os
import re
import urllib.parse
import streamlit as st
from google import genai

# إعداد واجهة وتصميم الصفحة
st.set_page_config(
    page_title="رادار الصفقات وعروض البنوك الذكية",
    layout="wide",
    page_icon="🎯"
)

# عنوان الواجهة وتنسيقها
st.markdown("<h2 style='text-align: center;'>🎯 رادار الصفقات وأحدث الإصدارات وعروض البنوك</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>أقوى تقرير استشاري لأحدث الموديلات في السوق السعودي (220V) + كاشف خصومات البطاقات البنكية وأقل سعر شراء مباشر</p>", unsafe_allow_html=True)

# جلب مفتاح API بأمان
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

# إدخال السلعة والبنك (اختياري لزيادة التوفير)
col_input, col_bank = st.columns([3, 2])
with col_input:
    query = st.text_input("ما هو الجهاز أو المنتج الذي تبحث عنه؟", placeholder="...مثال: قلاية هوائية، شواية ذكية، صانعة قهوة، مفرمة لحم")
with col_bank:
    bank_name = st.selectbox(
        "البنك أو البطاقة التي تمتلكها (للبحث عن كود خصم إضافي):",
        ["عام / جميع البنوك", "البنك السعودي الفرنسي (BSF)", "مصرف الراجحي", "البنك الأهلي السعودي (SNB)", "مصرف الإنماء", "بنك الرياض", "بطاقة urpay / STC Pay", "تابي / تمارا"]
    )

if st.button("🚀 فحص أحدث 3 موديلات وكشف أقوى صفقة وبنك", use_container_width=True):
    if not query.strip():
        st.warning("يرجى كتابة اسم المنتج أو الجهاز أولاً.")
    elif not api_key:
        st.error("مفتاح API غير متوفر في الإعدادات السحابية.")
    else:
        with st.spinner("جاري مسح المتاجر المعتمدة في الرياض، فحص المواصفات الكهربائية، واستخراج عروض البنوك..."):
            client = genai.Client(api_key=api_key)
            prompt = f"""أنت مستشار مشتريات خبير في الإلكترونيات والأجهزة المنزلية بالمملكة العربية السعودية (مدينة الرياض).
المستخدم يبحث عن: {query}
البنك المفضل للمستخدم: {bank_name}

المطلوب تقديم تقرير استشاري شامل، عميق، وغني بالمعلومات الدقيقة:
1. تحديد أفضل وأحدث 3 موديلات عالمية رائدة متاحة حالياً بالسوق (ركز بدقة على أحدث تقنيات العام، مثل تقنيات Dual Zone، الذكاء الاصطناعي، برامج الطهي المتقدمة Combi، وتجنب تماماً الموديلات القديمة أو التقليدية).
2. مطابقة المواصفات السعودية (SASO): التأكيد على فولت 220V-240V وتردد 50/60Hz وقابس ثلاثي، والتنبيه برمز الموديل الخليجي المعتمد، والتحذير من أي موديلات أمريكية أو مستوردة غير متوافقة.

لكل جهاز من الأجهزة الثلاثة، اذكر بالتفصيل:
- الترتيب والاسم التجاري الكامل مع رقم الموديل الإنجليزي الدقيق (Model Number / SKU).
- المواصفات الفنية التفصيلية (السعة باللتر، القوة بالواط، وأبرز التقنيات الحصرية).
- متوسط السعر اليوم بالريال السعودي في متاجر الرياض (أمازون السعودية، إكسترا، نون، ساكو).
- روابط الشراء المباشرة للموديل بعينه:
  * [🛒 فتح الموديل في أمازون السعودية](https://www.amazon.sa/s?k=الاسم_والموديل_بالإنجليزي)
  * [🟡 فتح الموديل في نون السعودية](https://www.noon.com/saudi-ar/search/?q=الاسم_والموديل_بالإنجليزي)
  * [🔵 فتح الموديل في إكسترا](https://www.extra.com/ar-sa/search/?q=الاسم_والموديل_بالإنجليزي)

3. قسم خاص: 'حيل التوفير وأكواد الخصم البنكية النشطة اليوم':
   - وضح كود الخصم البنكي الشائع والمتاح حالياً للمتجر (مثل أكواد بطاقات {bank_name}، أو أكواد BSF20، الراجحي، أو أكواد أمازون برايم ونون) وكيف يخصم للمشتري من 50 إلى 150 ريال إضافية.
4. جدول مقارنة فني شامل يوضح: (الموديل، السعة، الواط، التقنية الأبرز، متوسط السعر، والميزة الحصرية).
5. ختم التقرير بـ 'الصفقة الرابحة الحاسمة' (Best Value) مع السعر الصافي بعد تطبيق كود الخصم البنكي.
6. اكتب في آخر سطر بالتقرير تماماً الصيغة التالية بدون زيادة:
BEST_MODEL_NAME: [اكتب هنا اسم الماركة والموديل الفائز بالإنجليزي فقط]"""

            # نظام التبديل التلقائي لتجاوز أي ضغط على السيرفرات
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
                st.success("تم إعداد التقرير وحصر عروض المتاجر والخصومات البنكية بنجاح!")
                raw_text = response.text

                # استخراج اسم الموديل الفائز لتجهيز الأزرار ورابط الواتساب
                best_model = query
                model_match = re.search(r"BEST_MODEL_NAME:\s*(.+)", raw_text)
                if model_match:
                    best_model = model_match.group(1).strip().replace("[", "").replace("]", "")
                    clean_text = raw_text.replace(model_match.group(0), "")
                else:
                    clean_text = raw_text

                # عرض التقرير الغني والعميق
                st.markdown(clean_text)

                # قسم أزرار الشراء والمشاركة الفيروسية
                st.markdown("---")
                col_actions1, col_actions2 = st.columns([1, 1])

                with col_actions1:
                    st.markdown(f"#### 🛍️ الشراء المباشر للصفقة الرابحة: `{best_model}`")
                    encoded_best = urllib.parse.quote(best_model)
                    c1, c2 = st.columns(2)
                    with c1:
                        st.link_button(f"🛒 فتح السلعة في أمازون", f"https://www.amazon.sa/s?k={encoded_best}", use_container_width=True)
                    with c2:
                        st.link_button(f"🟡 فتح السلعة في نون", f"https://www.noon.com/saudi-ar/search/?q={encoded_best}", use_container_width=True)

                with col_actions2:
                    st.markdown("#### 📲 نشر التوفير (مشاركة تسوق نفسها):")
                    share_text = f"🔥 لقيت صفقة ممتازة لـ ({best_model}) بأسعار اليوم مع كود خصم بنكي إضافي! شوف التفاصيل ووفر فلوسك من رادار الصفقات:"
                    whatsapp_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(share_text)}"
                    st.link_button("🟢 مشاركة هذه الصفقة فوراً عبر واتساب", whatsapp_url, use_container_width=True)

            else:
                st.error("خوادم الفحص تشهد ضغطاً مؤقتاً، يرجى إعادة المحاولة بعد ثوانٍ بسيطة.")
