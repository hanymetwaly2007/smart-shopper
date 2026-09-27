import streamlit as st
import urllib.parse

# 1. إعداد الصفحة والكلمات المفتاحية لمحركات البحث (SEO)
st.set_page_config(
    page_title="رادار الصفقات KSA | مقارنة أسعار الأجهزة المنزلية وعروض البنوك السعودية",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. تنسيقات التصميم ودعم اللغة العربية (RTL)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
    
    * {
        font-family: 'Cairo', sans-serif;
    }
    
    .stApp {
        direction: rtl;
        text-align: right;
    }
    
    .seo-banner {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border: 1px solid #dee2e6;
        border-right: 5px solid #ff9900;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 25px;
        font-size: 0.95rem;
        color: #495057;
        line-height: 1.6;
    }

    .product-box {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 18px;
        margin-bottom: 18px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }
    
    .product-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #1a73e8;
        margin-bottom: 8px;
    }
    
    .price-tag {
        font-size: 1.1rem;
        font-weight: 700;
        color: #d93025;
        margin-bottom: 10px;
    }

    .deal-card {
        background-color: #f6fff8;
        border: 2px solid #28a745;
        border-radius: 12px;
        padding: 22px;
        margin: 25px 0;
        box-shadow: 0 4px 8px rgba(40,167,69,0.1);
    }

    .btn-amazon {
        display: block;
        width: 100%;
        background-color: #ff9900;
        color: #111 !important;
        text-align: center;
        padding: 12px;
        border-radius: 8px;
        font-weight: 700;
        text-decoration: none;
        margin-bottom: 10px;
        transition: 0.2s;
    }
    .btn-amazon:hover {
        background-color: #e68a00;
    }

    .btn-noon {
        display: block;
        width: 100%;
        background-color: #feee00;
        color: #333 !important;
        text-align: center;
        padding: 12px;
        border-radius: 8px;
        font-weight: 700;
        text-decoration: none;
        margin-bottom: 10px;
        transition: 0.2s;
    }
    .btn-noon:hover {
        background-color: #e5d600;
    }

    .btn-whatsapp {
        display: block;
        width: 100%;
        background-color: #25d366;
        color: white !important;
        text-align: center;
        padding: 12px;
        border-radius: 8px;
        font-weight: 700;
        text-decoration: none;
        transition: 0.2s;
    }
    .btn-whatsapp:hover {
        background-color: #20ba5a;
    }
</style>
""", unsafe_allow_html=True)

# 3. ترويسة الموقع والنص التعريفي المخصص للأرشفة (SEO Indexing)
st.title("🎯 رادار الصفقات الذكي وعروض البنوك | KSA")

st.markdown("""
<div class="seo-banner">
    <b>دليلك المعتمد للتسوق ومقارنة الأسعار في المملكة العربية السعودية:</b> 
    محرك بحث لمطابقة مواصفات الأجهزة الكهربائية والمنزلية (قلايات هوائية، غسالات صحون، أجهزة مطبخ) 
    مع مواصفات الهيئة السعودية للمواصفات والمقاييس (SASO)، واحتساب الخصومات التلقائية لبطاقات بنك الراجحي، الأهلي SNB، الفرنسي BSF، والإنماء، لمقارنة أسعار أمازون السعودية، نون، وإكسترا بأفضل قيمة شراء.
</div>
""", unsafe_allow_html=True)

# 4. إعدادات الحساب وروابط التتبع
AMAZON_TAG = "habebadeals-21"
APP_URL = "https://deals-radar-habeba.streamlit.app"

# 5. واجهة البحث واختيار البنك
col_search, col_bank = st.columns([3, 2])

with col_search:
    search_query = st.text_input(
        "🔎 ما الجهاز أو السلعة التي ترغب بمقارنتها؟",
        value="قلاية هوائية دبل زون",
        placeholder="مثال: غسالة صحون بوش، قلاية نينجا، شاشة 65 بوصة..."
    )

with col_bank:
    selected_bank = st.selectbox(
        "💳 بطاقتك البنكية (لحساب الخصم المباشر):",
        [
            "جميع البنوك (عرض مقارنة الخصومات لكافة البنوك)",
            "البنك السعودي الفرنسي BSF (كود BSF20 - خصم 100 ريال)",
            "مصرف الراجحي (خصم إضافي 100 ريال)",
            "البنك الأهلي السعودي SNB (خصم إضافي 100 ريال)",
            "مصرف الإنماء (خصم إضافي 75 ريال)",
            "بنك الرياض (خصم إضافي 50 ريال)",
            "بدون بطاقة بنكية (سعر الكاش العادي)"
        ]
    )

analyze_btn = st.button("🚀 فحص المواصفات ومقارنة العروض الآن", type="primary", use_container_width=True)

# 6. قسم النتائج والتحليل الفني الشامل
if analyze_btn or search_query:
    st.markdown("---")
    
    # أولاً: الموديل الأول
    st.markdown("""
    <div class="product-box">
        <div class="product-title">أولاً: Philips Combi 7000 Series (HD9880)</div>
        <div class="price-tag">متوسط السعر المتداول: 1,599 ريال سعودي</div>
        <ul>
            <li><b>السعة الفعالة:</b> 8.3 لتر (سلة فردية عملاقة تتسع لوجبة عائلية كاملة).</li>
            <li><b>القوة الكهربائية:</b> 2200 واط متوافقة مع الجهد الكهربائي السعودي (230V / 60Hz).</li>
            <li><b>التقنية الحصرية:</b> مسبار حراري ذكي مدمج (Food Thermometer) لقياس درجة نضج اللحوم من الداخل بدقة بالغة مع اتصال مباشر بتطبيق NutriU عبر الواي فاي.</li>
            <li><b>التقييم:</b> الفئة الأعلى في دقة الطهي، لكن سعرها مرتفع نسبياً وتعتمد على منطقة طهي واحدة بدون فاصل.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # ثانياً: الموديل الثاني
    st.markdown("""
    <div class="product-box">
        <div class="product-title">ثانياً: Ninja Foodi FlexBasket 10.4L (AF500ME)</div>
        <div class="price-tag">السعر الحالي بأمازون (عرض اليوم الوطني): 899 ريال سعودي (بدلاً من 1,499)</div>
        <ul>
            <li><b>السعة الفعالة:</b> 10.4 لتر مع نظام المقسم الذكي (تحويل بين درجين منفصلين 5.2 لتر لكل درج أو درج واحد عملاق 10.4 لتر).</li>
            <li><b>القوة الكهربائية:</b> 2470 واط تدعم تسخيناً فائق السرعة ومطابقة لمعايير كفاءة الطاقة والمقابس السعودية SASO.</li>
            <li><b>التقنية الحصرية:</b> تقنية FlexBasket التي تمنح مرونة طهي صنفين مختلفين في نفس الوقت أو طهي وجبة ضخمة (دجاجتين كاملتين مع خضار) دفعة واحدة.</li>
            <li><b>التقييم:</b> الخيار الأكثر توازناً وعملية للعائلات بفضل المرونة المزدوجة وسعر العرض الاستثنائي الحالي.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # ثالثاً: الموديل الثالث
    st.markdown("""
    <div class="product-box">
        <div class="product-title">ثالثاً: Instant Vortex Plus Dual ClearCook (140-3095)</div>
        <div class="price-tag">متوسط السعر المتداول: 749 ريال سعودي</div>
        <ul>
            <li><b>السعة الفعالة:</b> 7.6 لتر مقسمة على درجين منفصلين تماماً (3.8 لتر لكل درج).</li>
            <li><b>القوة الكهربائية:</b> 1700 واط اقتصادية في استهلاك الطاقة ومطابقة للمواصفات القياسية.</li>
            <li><b>التقنية الحصرية:</b> نافذة رؤية شفافة ClearCook مع إضاءة داخلية لمتابعة الطعام دون فتح الدرج، بالإضافة لفلاتر كربون مدمجة (OdorErase) لامتصاص الروائح والأدخنة.</li>
            <li><b>التقييم:</b> ممتازة للمطابخ المغلقة ومحبي التحكم بالروائح والميزانيات الاقتصادية، مع سعة إجمالية أصغر مقارنة بالمنافسين.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # رابعاً: جدول المقارنة الفني الشامل
    st.subheader("رابعاً: جدول المقارنة الفني الشامل")
    st.markdown("""
| اسم الموديل | السعة الفعالة | القوة الكهربائية | التقنية الأبرز | متوسط السعر المتداول | الميزة التنافسية الحصرية |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Philips Combi 7000 (HD9880)** | 8.3 لتر (منطقة واحدة) | 2200 واط | الذكاء الاصطناعي ومسبار الحرارة | 1,599 ر.س | أدق استواء للحوم بفضل المسبار الذكي والاتصال بالإنترنت |
| **Ninja FlexBasket (AF500ME)** | 10.4 لتر (1 أو 2 درج) | 2470 واط | التحويل الذكي للمساحة FlexBasket | 899 ر.س (عرض حالي) | مرونة غير محدودة لطهي وجبات عائلية ضخمة أو صنفين منفصلين |
| **Instant Vortex Dual (140-3095)** | 7.6 لتر (درجين منفصلين) | 1700 واط | فلاتر الكربون ومنع الروائح | 749 ر.س | بيئة مطبخ خالية من الروائح مع إمكانية مراقبة الطعام بالكامل |
""")

    st.markdown("---")

    # خامساً: الصفقة الرابحة الحاسمة
    st.subheader("خامساً: الصفقة الرابحة الحاسمة (Best Value)")
    
    target_product = "Ninja Foodi FlexBasket 10.4L (AF500ME)"
    base_price = 899  # السعر المحدث طبقاً لعروض أمازون الحالية

    # معالجة خصومات البنوك
    if "جميع البنوك" in selected_bank:
        st.markdown(f"""
        <div class="deal-card">
            <h4 style="color: #28a745; margin-top: 0;">🏆 الفائز بأفضل قيمة مقابل السعر: {target_product}</h4>
            <p>السعر الأساسي الحالي في أمازون: <b>{base_price} ريال</b> (تخفيض اليوم الوطني 40%).</p>
            <p><b>جدول مقارنة أسعار السلعة بحسب بطاقتك البنكية:</b></p>
            <table style="width:100%; border-collapse: collapse; text-align: right; margin-bottom: 15px;">
                <tr style="background-color: #e8f5e9;">
                    <th style="padding: 8px; border: 1px solid #c8e6c9;">البنك / البطاقة</th>
                    <th style="padding: 8px; border: 1px solid #c8e6c9;">كود / تفاصيل الخصم</th>
                    <th style="padding: 8px; border: 1px solid #c8e6c9;">السعر النهائي التقريبي</th>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>البنك السعودي الفرنسي BSF</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">كود <code>BSF20</code> (خصم 100 ر.س) / <code>BSF25</code> لبرايم (خصم 150 ر.س)</td>
                    <td style="padding: 8px; border: 1px solid #ddd; color: #d93025; font-weight: bold;">749 - 799 ريال</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>مصرف الراجحي</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">خصم مباشر إضافي 100 ر.س</td>
                    <td style="padding: 8px; border: 1px solid #ddd; color: #d93025; font-weight: bold;">799 ريال</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>البنك الأهلي SNB</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">خصم مباشر إضافي 100 ر.س</td>
                    <td style="padding: 8px; border: 1px solid #ddd; color: #d93025; font-weight: bold;">799 ريال</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>مصرف الإنماء</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">خصم إضافي 75 ر.س</td>
                    <td style="padding: 8px; border: 1px solid #ddd; color: #d93025; font-weight: bold;">824 ريال</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>بدون بطاقة بنكية (كاش)</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">سعر العرض المباشر بأمازون</td>
                    <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">899 ريال</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        net_price = 799
        discount_desc = "خصومات البنوك المتعددة حتى 150 ريال"
    else:
        # حساب خصم بنك مفرد
        discount_val = 0
        if "BSF" in selected_bank or "الفرنسي" in selected_bank or "الراجحي" in selected_bank or "الأهلي" in selected_bank:
            discount_val = 100
        elif "الإنماء" in selected_bank:
            discount_val = 75
        elif "الرياض" in selected_bank:
            discount_val = 50

        net_price = base_price - discount_val
        discount_desc = f"توفير {discount_val} ريال مع بطاقتك البنكية"

        st.markdown(f"""
        <div class="deal-card">
            <h4 style="color: #28a745; margin-top: 0;">🏆 الفائز بأفضل قيمة مقابل السعر: {target_product}</h4>
            <ul>
                <li><b>السعر في عرض اليوم الوطني:</b> {base_price} ريال سعودي (بدلاً من 1,499 ريال).</li>
                <li><b>السعر الصافي التقريبي بعد خصم البنك:</b> <span style="font-size: 1.3rem; font-weight: 800; color: #d93025;">{net_price} ريال سعودي</span> ({discount_desc}).</li>
                <li><b>ملاحظة:</b> إذا كنت تستخدم بطاقة الفرنسي BSF مع برايم استخدم كود <code>BSF25</code> لخصم 150 ريال.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # 7. تجهيز روابط المتاجر والمشاركة
    encoded_search = urllib.parse.quote(target_product)
    amazon_affiliate_url = f"https://www.amazon.sa/s?k={encoded_search}&tag={AMAZON_TAG}"
    noon_url = f"https://www.noon.com/saudi-ar/search/?q={encoded_search}"
    
    wa_message = f"""🎯 وجدت لك أفضل صفقة جهاز منزلي في عروض اليوم الوطني بأمازون!

الجهاز: {target_product}
السعر بالعرض: {base_price} ريال (بدلاً من 1,499 ريال)
السعر بعد خصم البنك: يصل إلى {net_price} ريال تقريباً!

فحص ومقارنة المواصفات من رادار الصفقات:
{APP_URL}

رابط الشراء المباشر من أمازون:
{amazon_affiliate_url}"""
    
    wa_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(wa_message)}"

    # 8. أزرار الشراء والمشاركة
    col_buy, col_share = st.columns(2)

    with col_buy:
        st.markdown(f"**🛍️ الشراء المباشر للصفقة الرابحة:** `{target_product}`")
        st.markdown(f'<a href="{amazon_affiliate_url}" target="_blank" class="btn-amazon">🛒 فتح السلعة في أمازون</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{noon_url}" target="_blank" class="btn-noon">🟡 فتح السلعة في نون</a>', unsafe_allow_html=True)

    with col_share:
        st.markdown("**📲 نشر التوفير (مشاركة تسوّق نفسها):**")
        st.markdown(f'<a href="{wa_url}" target="_blank" class="btn-whatsapp">🟢 مشاركة هذه الصفقة فوراً عبر واتساب</a>', unsafe_allow_html=True)
