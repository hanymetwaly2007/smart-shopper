import streamlit as st
import urllib.parse

# 1. إعداد الصفحة والكلمات المفتاحية لمحركات البحث (SEO)
st.set_page_config(
    page_title="أقوى عروض وتخفيضات الأجهزة المنزلية في السعودية | مقارنة الأسعار وخصم البنوك",
    page_icon="🔥",
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
        background: linear-gradient(135deg, #fff8f0 0%, #fff0e0 100%);
        border: 1px solid #ffe0b2;
        border-right: 5px solid #ff9900;
        padding: 16px;
        border-radius: 10px;
        margin-bottom: 25px;
        font-size: 0.95rem;
        color: #333;
        line-height: 1.7;
    }
    
    .product-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #1a73e8;
        margin-bottom: 6px;
    }
    
    .price-tag {
        font-size: 1.15rem;
        font-weight: 700;
        color: #d93025;
        margin-bottom: 10px;
    }

    .badge-rank {
        display: inline-block;
        background-color: #e8f0fe;
        color: #1a73e8;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: bold;
        margin-bottom: 8px;
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
        padding: 10px;
        border-radius: 8px;
        font-weight: 700;
        text-decoration: none;
        margin-bottom: 8px;
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
        padding: 10px;
        border-radius: 8px;
        font-weight: 700;
        text-decoration: none;
        margin-bottom: 8px;
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

# 3. الترويسة الرئيسية
st.title("🔥 أقوى عروض وتخفيضات الأجهزة الكهربائية والمنزلية في السعودية")

st.markdown("""
<div class="seo-banner">
    <b>دليلك الذكي لمقارنة واختيار الأجهزة المنزلية وأدوات المطبخ:</b> 
    نرشح لك أفضل 3 ماركات أصلية ومطابقة لمواصفات SASO السعودية (الأعلى جودة، الأكثر مبيعاً، والأنسب سعراً)، ونعطيك حرية الاختيار وحساب الخصم المباشر لبطاقات <b>مصرف الراجحي، الأهلي SNB، الفرنسي BSF، ومصرف الإنماء</b>.
</div>
""", unsafe_allow_html=True)

# 4. إعدادات التتبع والعمولة
AMAZON_TAG = "habebadeals-21"
APP_URL = "https://deals-radar-habeba.streamlit.app"

# 5. إدارة الذاكرة
if "active_query" not in st.session_state:
    st.session_state.active_query = ""

def quick_select(term):
    st.session_state.active_query = term

# أزرار تنقل سريع لأشهر الفئات
st.markdown("**⚡ فئات سريعة للأجهزة الأكثر طلباً (أو اكتب اسم أي جهاز بالأسفل):**")
c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    st.button("🍳 أطقم قدور ستانلس", on_click=quick_select, args=("طقم اواني استيل",), use_container_width=True)
with c2:
    st.button("🥣 عجانات كينوود", on_click=quick_select, args=("عجانة كهربائية",), use_container_width=True)
with c3:
    st.button("🍟 قلايات هوائية", on_click=quick_select, args=("قلاية هوائية",), use_container_width=True)
with c4:
    st.button("🥤 خلاطات ومحضرات طعام", on_click=quick_select, args=("خلاط كهربائي",), use_container_width=True)
with c5:
    st.button("🍽️ غسالات صحون", on_click=quick_select, args=("غسالة صحون",), use_container_width=True)

col_search, col_bank = st.columns([3, 2])

with col_search:
    search_input = st.text_input(
        "🔎 ابحث عن أي جهاز أو أداة منزلية تريد فحصها ومقارنة خياراتها:",
        value=st.session_state.active_query,
        placeholder="مثال: طقم اواني استيل، عجانة، قلاية هوائية، خلاط، مكنسة، كواية بخار..."
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

analyze_btn = st.button("🚀 فحص الخيارات والماركات المتاحة", type="primary", use_container_width=True)

# 6. تجهيز الخيارات والبيانات
raw_query = search_input.strip()
query = raw_query.lower()

if not raw_query:
    st.info("👆 اكتب اسم أي جهاز أو أداة منزلية في مربع البحث، أو اضغط على الفئات السريعة بالأعلى لتظهر لك المنتجات بالصور والمواصفات.")
else:
    # الفئة 1: أطقم أواني وقدور الستانلس ستيل
    if any(w in query for w in ["اواني", "أواني", "استيل", "ستانلس", "كركوماز", "قدور", "قدر", "حلل", "تيفال"]):
        cat_title = "أفضل أطقم قدور ستانلس ستيل أصلية 18/10 في السعودية"
        products = [
            {
                "name": "طقم قدور كركوماز أسترا 9 قطع تركي أصلي (Korkmaz Astra A1900)",
                "tier": "الفئة الأولى: الأكثر جودة واعتمادية بالسعودية",
                "price_desc": "السعر الحالي بعروض أمازون: 459 ريال (بدلاً من 620)",
                "base_price": 459,
                "img": "https://m.media-amazon.com/images/I/61Nl-XhJ5cL._AC_SL1500_.jpg",
                "specs": [
                    "<b>معدن الصنع:</b> ستانلس ستيل نقي 18/10 Cr-Ni تركي أصلي مقاوم للصدأ مدى الحياة.",
                    "<b>القاعدة:</b> قاعدة كبسولية ثلاثية سميكة Solar Base توزع الحرارة بتساوٍ وتمنع احتراق قاع الأكل.",
                    "<b>المواصفات:</b> مقابض ستيل عازلة للحرارة، متوافق مع كافة الأفران وآمن بغسالة الصحون."
                ]
            },
            {
                "name": "طقم قدور تيفال إنتويشن 10 قطع ستانلس ستيل (Tefal Intuition)",
                "tier": "الفئة العالمية: الجودة والخبرة الفرنسية",
                "price_desc": "متوسط السعر المتداول: 549 ريال سعودي",
                "base_price": 549,
                "img": "https://m.media-amazon.com/images/I/71R2h7wWw1L._AC_SL1500_.jpg",
                "specs": [
                    "<b>الميزات الحصرية:</b> علامات قياس داخلية دقيقة مع حواف صب تمنع تساقط السوائل.",
                    "<b>الأغطية:</b> أغطية زجاجية مقواة بفتحة تنفيس للبخار لمراقبة الطهي بسهولة.",
                    "<b>الضمان:</b> خامات ستانلس ستيل 18/10 مع ضمان تيفال العالمي لمدة 5 سنوات."
                ]
            },
            {
                "name": "طقم قدور كركوماز تومبيك 9 قطع دائري (Korkmaz Tombik A1800)",
                "tier": "الفئة الكلاسيكية: الأنسب سعراً للميزانيات المتوسطة",
                "price_desc": "متوسط السعر المتداول: 389 ريال سعودي",
                "base_price": 389,
                "img": "https://m.media-amazon.com/images/I/61lD5LrqVHL._AC_SL1500_.jpg",
                "specs": [
                    "<b>التصميم:</b> شكل كروي دائري يسهل تقليب الشوربات والمرق مع قاعدة حرارية متطورة.",
                    "<b>الخامات:</b> ستانلس ستيل 18/10 تركي أصلي ومقابض ناعمة مريحة.",
                    "<b>التقييم:</b> أفضل قيمة اقتصادية لعلامة كركوماز التركية الشهيرة."
                ]
            }
        ]
        table_md = """
| اسم الطقم | عدد القطع | خامة الستانلس ستيل | نوع القاعدة | السعر بالعرض | الميزة الأبرز |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Korkmaz Astra** | 9 قطع | 18/10 Cr-Ni تركي أصلي | Solar Base ثلاثية | 459 ر.س | الطقم الأكثر انتشاراً، يوزع الحرارة ولا يحرق الطعام |
| **Tefal Intuition** | 10 قطع | ستانلس ستيل 18/10 | قاعدة سميكة مانعة للتشوه | 549 ر.س | علامات قياس داخلية وأغطية زجاجية مقواة |
| **Korkmaz Tombik** | 9 قطع | 18/10 كروي | قاعدة حرارية متساوية | 389 ر.س | تصميم دائري وسعر اقتصادي ممتاز |
"""

    # الفئة 2: العجانات الكهربائية
    elif any(w in query for w in ["عجان", "عجانه", "عجين", "مخبوزات", "كينوود"]):
        cat_title = "أفضل عجانات كهربائية منزلية في السعودية"
        products = [
            {
                "name": "عجانة كينوود شيف إكس إل 1200 واط (Kenwood Chef XL KVL4100S)",
                "tier": "الفئة الأولى: الأعلى متانة والأكثر طلباً بالسعودية",
                "price_desc": "السعر الحالي بعروض أمازون: 1,399 ريال (بدلاً من 1,899)",
                "base_price": 1399,
                "img": "https://m.media-amazon.com/images/I/61bW6f2vA8L._AC_SL1200_.jpg",
                "specs": [
                    "<b>القوة والسعة:</b> 1200 واط مع وعاء ضخم 6.7 لتر من الستانلس ستيل يكفي للكميات العائلية.",
                    "<b>الملحقات:</b> خفاقة K، ومضرب بيض ستيل، وخطاف عجين حلزوني ثقيل.",
                    "<b>المواصفات:</b> معتمدة وفق مقاييس SASO السعودية (220V/60Hz) وتتحمل الاستخدام المكثف."
                ]
            },
            {
                "name": "عجانة كيتشن إيد أرتيزان 4.8 لتر (KitchenAid Artisan 5KSM150)",
                "tier": "الفئة الاحترافية: أيقونة المخابز والحلويات العالمية",
                "price_desc": "متوسط السعر المتداول: 2,199 ريال سعودي",
                "base_price": 2199,
                "img": "https://m.media-amazon.com/images/I/71uXj6o1DUL._AC_SL1500_.jpg",
                "specs": [
                    "<b>المحرك:</b> دفع مباشر Direct Drive فائق الهدوء وعالي العزم مع حركة خلط كوكبية.",
                    "<b>الهيكل:</b> هيكل معدني ثقيل يمنع الاهتزاز وعمر افتراضي يقاس بعقود.",
                    "<b>التقييم:</b> الخيار الأمثل لصانعي الحلويات الدقيقة والخبز المنزلي الفاخر."
                ]
            },
            {
                "name": "عجانة بوش مالتي إم يو إم 1000 واط (Bosch MUM58243)",
                "tier": "الفئة الذكية: الأفضل قيمة ومتعددة الاستخدامات",
                "price_desc": "متوسط السعر المتداول: 799 ريال سعودي",
                "base_price": 799,
                "img": "https://m.media-amazon.com/images/I/71m7C+sZ8lL._AC_SL1500_.jpg",
                "specs": [
                    "<b>الأداء:</b> موتور 1000 واط مع حركة خلط ثلاثية الأبعاد 3D ووعاء 3.9 لتر.",
                    "<b>الملحقات:</b> ملحقات إضافية لبشر وتقطيع الخضروات وعصارة حمضيات.",
                    "<b>التقييم:</b> اقتصادية وعملية وتوفر مساحة في المطابخ العصرية."
                ]
            }
        ]
        table_md = """
| اسم الموديل | القوة | سعة الوعاء | نوع المحرك | السعر بالعرض | الميزة الأبرز |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Kenwood Chef XL** | 1200 واط | 6.7 لتر | تروس معدنية | 1,399 ر.س | سعة عملاقة تتحمل العجن الثقيل، والأعلى مبيعاً |
| **KitchenAid Artisan** | 300W دفع مباشر | 4.8 لتر | Direct Drive صامت | 2,199 ر.س | متانة تدوم لعقود ودقة متناهية لخلط الحلويات |
| **Bosch MUM5** | 1000 واط | 3.9 لتر | حركة ثلاثية الأبعاد | 799 ر.س | متعدد الاستخدامات وسعر اقتصادي ممتاز |
"""

    # الفئة 3: القلايات الهوائية
    elif any(w in query for w in ["قلاية", "قلايه", "هوائية", "هوائيه", "ايرفراير"]):
        cat_title = "أفضل قلاية هوائية في السعودية"
        products = [
            {
                "name": "قلاية نينجا فودي فليكس باسكت 10.4 لتر (Ninja FlexBasket AF500ME)",
                "tier": "الفئة الرائدة: المرونة الأعلى والسعة الأكبر للعائلات",
                "price_desc": "السعر الحالي بعروض أمازون: 899 ريال (بدلاً من 1,499)",
                "base_price": 899,
                "img": "https://m.media-amazon.com/images/I/81x12B3h6UL._AC_SL1500_.jpg",
                "specs": [
                    "<b>السعة:</b> 10.4 لتر مع مقسم ذكي للتحويل بين درجين 5.2 لتر أو درج عملاق 10.4 لتر.",
                    "<b>القوة:</b> 2470 واط تسخين فائق السرعة ومطابقة لمواصفات ومقابس SASO السعودية.",
                    "<b>التقييم:</b> الأكثر طلباً وتوازناً لطهي صنفين مختلفين في نفس الوقت."
                ]
            },
            {
                "name": "قلاية فيليبس كومبي سيريس 7000 (Philips Combi HD9880)",
                "tier": "الفئة التقنية الذكية: دقة الطهي بالمسبار الحراري والواي فاي",
                "price_desc": "متوسط السعر المتداول: 1,599 ريال سعودي",
                "base_price": 1599,
                "img": "https://m.media-amazon.com/images/I/71gV4eU1h-L._AC_SL1500_.jpg",
                "specs": [
                    "<b>التقنية الحصرية:</b> مسبار حراري مدمج لمتابعة درجة استواء اللحوم من القلب بدقة بالغة.",
                    "<b>السعة والقوة:</b> 8.3 لتر بقوة 2200 واط مع اتصال بتطبيق NutriU عبر الإنترنت.",
                    "<b>التقييم:</b> الفئة الأرقى لعشاق الدقة والطهي الصحي الفاخر."
                ]
            },
            {
                "name": "قلاية إنستانت فورتكس بلس نافذة شفافة (Instant Vortex ClearCook)",
                "tier": "فئة التحكم بالروائح والمطابخ المغلقة",
                "price_desc": "متوسط السعر المتداول: 749 ريال سعودي",
                "base_price": 749,
                "img": "https://m.media-amazon.com/images/I/71s8L5qj0kL._AC_SL1500_.jpg",
                "specs": [
                    "<b>الميزات الحصرية:</b> نافذة شفافة ClearCook مع فلاتر كربون مدمجة لمنع انتشار الروائح.",
                    "<b>السعة:</b> 7.6 لتر مقسمة على درجين منفصلين تماماً (3.8 لتر لكل درج).",
                    "<b>التقييم:</b> أفضل خيار للشقق والمطابخ المفتوحة لمنع روائح التحمير."
                ]
            }
        ]
        table_md = """
| اسم الموديل | السعة الفعالة | القوة | التقنية الأبرز | السعر بالعرض | الميزة الأبرز |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ninja FlexBasket** | 10.4 لتر (1 أو 2 درج) | 2470 واط | التحويل الذكي للمساحة | 899 ر.س | مرونة هائلة لطهي وجبة ضخمة أو صنفين معاً |
| **Philips Combi 7000** | 8.3 لتر | 2200 واط | مسبار حراري ذكي + واي فاي | 1,599 ر.س | استواء دقيق للحوم بالذكاء الاصطناعي |
| **Instant Vortex Dual** | 7.6 لتر | 1700 واط | فلاتر كربون لمنع الروائح | 749 ر.س | مطبخ نظيف خالي من الروائح ونافذة مراقبة |
"""

    # الفئة 4: الخلاطات ومحضرات الطعام
    elif any(w in query for w in ["خلاط", "محضر", "بلندر", "براون", "عصارة"]):
        cat_title = "أفضل خلاطات ومحضرات طعام في السعودية"
        products = [
            {
                "name": "خلاط ومحضر طعام نينجا فودي 3 في 1 (Ninja Foodi BN800ME)",
                "tier": "الفئة الشاملة: الأكثر قوة وتنوعاً في جهاز واحد",
                "price_desc": "السعر الحالي بعروض أمازون: 649 ريال (بدلاً من 899)",
                "base_price": 649,
                "img": "https://m.media-amazon.com/images/I/71mZc+k+1oL._AC_SL1500_.jpg",
                "specs": [
                    "<b>القوة والسعة:</b> موتور 1200 واط، دورق 2.1 لتر، وعاء محضر 1.8 لتر، وكوبين سموذي.",
                    "<b>التقنية:</b> برامج Auto-iQ الآلية للتقطيع والخلط والعجن بلمسة زر واحدة.",
                    "<b>التقييم:</b> يغنيك عن شراء 3 أجهزة منفصلة ويطحن الثلج والمكسرات في ثوانٍ."
                ]
            },
            {
                "name": "خفاق يدوي براون مالتي كويك 9 (Braun MultiQuick 9 MQ9147X)",
                "tier": "الفئة الاحترافية: الخفاق اليدوي الأكثر كفاءة وسرعة",
                "price_desc": "متوسط السعر المتداول: 599 ريال سعودي",
                "base_price": 599,
                "img": "https://m.media-amazon.com/images/I/61kMv-2sBBL._AC_SL1500_.jpg",
                "specs": [
                    "<b>القوة:</b> 1200 واط مع شفرات ActiveBlade تتحرك رأسياً لسحق أصلب الأطعمة بجهد أقل 40%.",
                    "<b>الملحقات:</b> ملحق هرس بطاطس، خفاقة، مفرمة بصل، وتصميم يمنع تناثر السوائل.",
                    "<b>التقييم:</b> أداة الطهي السريعة رقم 1 للشوربات والصلصات بداخل القدر مباشرة."
                ]
            },
            {
                "name": "خلاط فيليبس كور سيريس 5000 (Philips Series 5000 HR3573)",
                "tier": "الفئة الاقتصادية المعتمدة",
                "price_desc": "متوسط السعر المتداول: 289 ريال سعودي",
                "base_price": 289,
                "img": "https://m.media-amazon.com/images/I/71dM87L0a1L._AC_SL1500_.jpg",
                "specs": [
                    "<b>المواصفات:</b> 1000 واط مع دورق زجاجي مقاوم للكسر والحرارة سعة 2 لتر و 6 شفرات ProBlend.",
                    "<b>التقييم:</b> مثالي للعصائر اليومية والسموذي والميزانيات المحدودة."
                ]
            }
        ]
        table_md = """
| اسم الموديل | القوة | السعة الرئيسية | التقنية الأبرز | السعر بالعرض | الميزة الأبرز |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ninja Foodi 3-in-1** | 1200 واط | 2.1 لتر + 1.8 لتر | برامج Auto-iQ الذكية | 649 ر.س | جهاز شامل (خلاط + محضر طعام + سموذي) |
| **Braun MultiQuick 9** | 1200 واط | ملحقات متعددة | شفرات ActiveBlade عمودية | 599 ر.س | خلط مباشر بالأواني بدون تناثر أو فوضى |
| **Philips Series 5000** | 1000 واط | 2 لتر زجاجي | شفرات ProBlend Crush | 289 ر.س | اقتصادي وعملي جداً للعصائر اليومية |
"""

    # الفئة 5 الافتراضية لأي جهاز آخر
    else:
        cat_title = f"أفضل وأقوى موديلات ({raw_query}) في السعودية - أعلى جودة وماركات معتمدة"
        products = [
            {
                "name": f"الإصدار الاحترافي الأعلى جودة ومواصفات من: {raw_query}",
                "tier": "الفئة الأولى: الخيار الرائد والأعلى جودة (Top Brand)",
                "price_desc": "متوسط السعر الفاخر: 1,250 - 1,890 ريال سعودي",
                "base_price": 1290,
                "img": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=600&auto=format&fit=crop&q=80",
                "specs": [
                    "<b>أعلى جودة تصنيع:</b> مصنعة من مواد متينة فائقة التحمل ومطابقة لمعايير SASO السعودية.",
                    "<b>الأداء والتقنية:</b> أحدث إصدار مزود بأنظمة تحكم ذكية توفر أقصى طاقة تشغيل مع استهلاك اقتصادي.",
                    "<b>الضمان:</b> يشمل ضمان الوكيل المعتمد في المملكة لمدة سنتين مع توفر قطع الغيار الأصلية."
                ]
            },
            {
                "name": f"الموديل الأكثر مبيعاً وتقييماً في عروض السعودية: {raw_query}",
                "tier": "الفئة المتوازنة: الأكثر شعبية وأفضل قيمة مقابل السعر",
                "price_desc": "السعر الحالي في عروض أمازون: 680 - 890 ريال سعودي",
                "base_price": 799,
                "img": "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=600&auto=format&fit=crop&q=80",
                "specs": [
                    "<b>الخيار الأكثر شعبية:</b> حائز على تقييمات إيجابية (4.5 نجوم فأكثر) من آلاف المشترين في السعودية.",
                    "<b>الميزات العملية:</b> تصميم مريح وسهل التنظيف ومصمم للاستخدام اليومي الكثيف.",
                    "<b>سعر التخفيض:</b> مشمول بخصومات وتخفيضات تصل إلى 35% عبر الشراء الإلكتروني."
                ]
            },
            {
                "name": f"الخيار الاقتصادي العملي المطابق للمواصفات: {raw_query}",
                "tier": "الفئة الاقتصادية المعتمدة (Best Budget Value)",
                "price_desc": "متوسط السعر الاقتصادي: 290 - 450 ريال سعودي",
                "base_price": 380,
                "img": "https://images.unsplash.com/photo-1588854337221-4cf9fa96059c?w=600&auto=format&fit=crop&q=80",
                "specs": [
                    "<b>أداء يعتمد عليه:</b> يقدم الوظائف الأساسية بكفاءة عالية وبأقل تكلفة مع ضمان السلامة الكهربائية.",
                    "<b>التقييم:</b> الأنسب للميزانيات المحدودة والشقق الصغيرة والاستخدام السريع."
                ]
            }
        ]
        table_md = f"""
| فئة المنتج | معيار الجودة | كفاءة الطاقة السعودية SASO | الضمان المحلي | السعر المتوقع | الميزة الأبرز |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **الفئة الأولى الرائدة** | خامات أوروبية/عالمية ممتازة | أقصى توفير للطاقة | سنتين شامل الوكيل | 1,250+ ر.س | متانة استثنائية وأحدث تقنية بالسوق |
| **الفئة الأكثر طلباً ومبيعاً** | متوازنة وعملية جداً | فئة موفرة ممتازة | سنتين معتمد | 680 - 890 ر.س | أفضل قيمة وجودة مقابل الريال المدفوع |
| **الفئة الاقتصادية** | خامات عملية خفيفة | معتمد للمواصفات | سنتين | 290 - 450 ر.س | سعر في متناول اليد للوظائف الأساسية |
"""

    st.markdown("---")
    st.subheader(f"📋 الخيارات المرشحة لمقارنة: {raw_query}")

    # عرض كروت المنتجات مع الصور السليمة وأزرار شراء مباشرة لكل منتج
    for i, prod in enumerate(products):
        with st.container(border=True):
            col_img, col_txt = st.columns([1, 2.5])
            
            # عرض الصورة ببروتوكول يمنع الحجب
            with col_img:
                st.markdown(
                    f'<div style="text-align:center; padding: 10px;">'
                    f'<img src="{prod["img"]}" referrerpolicy="no-referrer" '
                    f'style="max-width:100%; max-height:190px; object-fit:contain; border-radius:8px;" '
                    f'alt="{prod["name"]}"/></div>',
                    unsafe_allow_html=True
                )
            
            with col_txt:
                st.markdown(f'<div class="badge-rank">{prod["tier"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="product-title">{prod["name"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="price-tag">{prod["price_desc"]}</div>', unsafe_allow_html=True)
                for s in prod["specs"]:
                    st.markdown(f"• {s}", unsafe_allow_html=True)
                
                # روابط مباشرة لكل منتج على حدة
                enc_p = urllib.parse.quote(prod["name"])
                p_amz = f"https://www.amazon.sa/s?k={enc_p}&tag={AMAZON_TAG}"
                p_noon = f"https://www.noon.com/saudi-ar/search/?q={enc_p}"
                
                c_btn1, c_btn2 = st.columns(2)
                with c_btn1:
                    st.markdown(f'<a href="{p_amz}" target="_blank" class="btn-amazon">🛒 فحص سعر هذا المنتج بأمازون</a>', unsafe_allow_html=True)
                with c_btn2:
                    st.markdown(f'<a href="{p_noon}" target="_blank" class="btn-noon">🟡 فحص سعر هذا المنتج بنون</a>', unsafe_allow_html=True)

    st.markdown("---")

    # رابعاً: جدول المقارنة الفني
    st.subheader(f"رابعاً: جدول المقارنة الفني الشامل ({cat_title})")
    st.markdown(table_md)

    st.markdown("---")

    # خامساً: حرية الاختيار وتخصيص خصم البنك
    st.subheader("🎯 خامساً: حدد المنتج الذي يناسبك لمعرفة سعره النهائي مع بطاقتك البنكية:")
    
    # قائمة اختيار تفاعلية تتيح للمستخدم تحديد أي منتج يفضله
    chosen_idx = st.radio(
        "اختر المنتج الذي تراه الأنسب لاحتياجك وميزانيتك من بين الخيارات المتاحة:",
        options=range(len(products)),
        format_func=lambda i: f"الخيار {i+1}: {products[i]['name']} (السعر الأساسي: {products[i]['base_price']} ريال)"
    )

    selected_product = products[chosen_idx]
    base_price = selected_product["base_price"]
    winner_name = selected_product["name"]

    # حساب وتفصيل الخصومات للمنتج المختار
    if "جميع البنوك" in selected_bank:
        p_french = max(base_price - 100, 0)
        p_rajhi = max(base_price - 100, 0)
        p_inma = max(base_price - 75, 0)
        net_price = p_french

        st.markdown(f"""
        <div class="deal-card">
            <h4 style="color: #28a745; margin-top: 0;">✅ تفاصيل العرض لمنتجك المختار: {winner_name}</h4>
            <p>السعر الأساسي بالعرض: <b>{base_price} ريال سعودي</b>.</p>
            <p><b>جدول الأسعار الصافية بعد خصومات بطاقات البنوك السعودية لهذا المنتج:</b></p>
            <table style="width:100%; border-collapse: collapse; text-align: right; margin-bottom: 15px;">
                <tr style="background-color: #e8f5e9;">
                    <th style="padding: 8px; border: 1px solid #c8e6c9;">البنك / البطاقة</th>
                    <th style="padding: 8px; border: 1px solid #c8e6c9;">كود / تفاصيل الخصم</th>
                    <th style="padding: 8px; border: 1px solid #c8e6c9;">السعر النهائي لطلبك</th>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>البنك السعودي الفرنسي BSF</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">كود <code>BSF20</code> (خصم 100 ر.س) / <code>BSF25</code> لبرايم</td>
                    <td style="padding: 8px; border: 1px solid #ddd; color: #d93025; font-weight: bold;">{p_french} ريال</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>مصرف الراجحي</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">خصم مباشر إضافي 100 ر.س</td>
                    <td style="padding: 8px; border: 1px solid #ddd; color: #d93025; font-weight: bold;">{p_rajhi} ريال</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>البنك الأهلي SNB</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">خصم مباشر إضافي 100 ر.س</td>
                    <td style="padding: 8px; border: 1px solid #ddd; color: #d93025; font-weight: bold;">{p_rajhi} ريال</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>مصرف الإنماء</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">خصم إضافي 75 ر.س</td>
                    <td style="padding: 8px; border: 1px solid #ddd; color: #d93025; font-weight: bold;">{p_inma} ريال</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>بدون بطاقة بنكية (كاش)</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">سعر العرض المباشر بأمازون</td>
                    <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">{base_price} ريال</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    else:
        discount_val = 0
        if "BSF" in selected_bank or "الفرنسي" in selected_bank or "الراجحي" in selected_bank or "الأهلي" in selected_bank:
            discount_val = 100
        elif "الإنماء" in selected_bank:
            discount_val = 75
        elif "الرياض" in selected_bank:
            discount_val = 50

        net_price = max(base_price - discount_val, 0)

        st.markdown(f"""
        <div class="deal-card">
            <h4 style="color: #28a745; margin-top: 0;">✅ تفاصيل العرض لمنتجك المختار: {winner_name}</h4>
            <ul>
                <li><b>السعر الأساسي بالعرض:</b> {base_price} ريال سعودي.</li>
                <li><b>السعر الصافي النهائي بعد خصم بطاقتك:</b> <span style="font-size: 1.3rem; font-weight: 800; color: #d93025;">{net_price} ريال سعودي</span> (توفير {discount_val} ريال).</li>
                <li><b>ملاحظة:</b> إذا كنت تستخدم بطاقة الفرنسي BSF مع برايم استخدم كود <code>BSF25</code> لخصم أكبر.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # 7. تجهيز روابط الشراء والمشاركة الخاصة بالمنتج المختار تحديداً
    encoded_search = urllib.parse.quote(winner_name)
    amazon_affiliate_url = f"https://www.amazon.sa/s?k={encoded_search}&tag={AMAZON_TAG}"
    noon_url = f"https://www.noon.com/saudi-ar/search/?q={encoded_search}"

    wa_message = f"""🔥 صفقة مميزة على أمازون السعودية!

المنتج المختار: {winner_name}
السعر بالعرض: {base_price} ريال
السعر بعد خصم البنوك يصل إلى: {net_price} ريال تقريباً!

فحص ومقارنة المواصفات والخصومات الفورية:
{APP_URL}

رابط الشراء المباشر من أمازون السعودية:
{amazon_affiliate_url}"""

    wa_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(wa_message)}"

    # أزرار الشراء والمشاركة للمنتج المحدد
    col_buy, col_share = st.columns(2)

    with col_buy:
        st.markdown(f"**🛍️ إتمام شراء المنتج المحدد:** `{winner_name}`")
        st.markdown(f'<a href="{amazon_affiliate_url}" target="_blank" class="btn-amazon">🛒 فتح المنتج في أمازون السعودية</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{noon_url}" target="_blank" class="btn-noon">🟡 فتح المنتج في نون السعودية</a>', unsafe_allow_html=True)

    with col_share:
        st.markdown("**📲 نشر التوفير (مشاركة تسوّق نفسها):**")
        st.markdown(f'<a href="{wa_url}" target="_blank" class="btn-whatsapp">🟢 مشاركة هذا الاختيار فوراً عبر واتساب</a>', unsafe_allow_html=True)
