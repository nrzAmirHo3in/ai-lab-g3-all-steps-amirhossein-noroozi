# مستندات گام دوم — آماده‌سازی داده و تمرین‌های جست‌وجو

این مستند سه مخزن مرتبط با «گام دوم» را معرفی می‌کند. این مخزن‌ها بخش‌های متفاوتی از پروژه را پوشش می‌دهند: انتخاب و آماده‌سازی داده، ارزیابی کیفیت داده و تمرین الگوریتم‌های جست‌وجوی مسیر.

| مخزن | مسیر گام دوم | تمرکز |
|---|---|---|
| [`ma-najafzadeh22/ai-lab-g2-mohammad-ali-najaf-zadeh`](https://github.com/ma-najafzadeh22/ai-lab-g2-mohammad-ali-najaf-zadeh/tree/9c840eecff85c84b3d6a0344056cc213ab30ed08/homeworks/task_2) | `homeworks/task_2` | بررسی محیط، معرفی و انتخاب مجموعه‌دادهٔ MADBase و مقایسهٔ ابتکاری الگوریتم A* |
| [`rezolens/ai-lab-all-step-reza-dehghani`](https://github.com/rezolens/ai-lab-all-step-reza-dehghani/tree/36c6c45dc639083c4c6590e53c7eeeb631dee385/step%202) | `step 2` | دریافت MADBase، تبدیل تصاویر و ذخیرهٔ دادهٔ اولیه؛ به‌علاوهٔ بررسی محیط و تمرین جست‌وجوی مسیر |
| [`deathtoconding/AI-lab-amirhossein-hassani`](https://github.com/deathtoconding/AI-lab-amirhossein-hassani/tree/11a591fe2263ea6b6b243675a79ae10097d3c998/step-2) | `step-2` | بررسی کیفیت داده و آماده‌سازی مجموعه‌های آموزش، اعتبارسنجی و آزمون؛ به‌علاوهٔ تمرین جست‌وجوی مسیر |

> **توجه:** مسیرهای `step-2`، `step 2` و `homeworks/task_2` در سه مخزن جداگانه قرار دارند و محتوای آن‌ها یکسان نیست. همچنین نوت‌بوک‌های جست‌وجوی مسیر، تمرین‌هایی مستقل از خط لولهٔ تشخیص رقم هستند.

---

## ۱. مخزن ma-najafzadeh22

**مخزن:** [ai-lab-g2-mohammad-ali-najaf-zadeh](https://github.com/ma-najafzadeh22/ai-lab-g2-mohammad-ali-najaf-zadeh)  
**پوشه:** [`homeworks/task_2`](https://github.com/ma-najafzadeh22/ai-lab-g2-mohammad-ali-najaf-zadeh/tree/9c840eecff85c84b3d6a0344056cc213ab30ed08/homeworks/task_2)

### فایل‌ها

- [`README.md`](https://github.com/ma-najafzadeh22/ai-lab-g2-mohammad-ali-najaf-zadeh/blob/9c840eecff85c84b3d6a0344056cc213ab30ed08/homeworks/task_2/README.md): معرفی MADBase، دلیل انتخاب آن، نکات استفاده و ارجاع به مقالهٔ اصلی.
- [`check_env.ipynb`](https://github.com/ma-najafzadeh22/ai-lab-g2-mohammad-ali-najaf-zadeh/blob/9c840eecff85c84b3d6a0344056cc213ab30ed08/homeworks/task_2/check_env.ipynb): نمایش نسخه و مسیر Python، نسخهٔ NumPy و Matplotlib، زمان اجرا و مشخصات گروه.
- [`lab2_heuristic_comparison.ipynb`](https://github.com/ma-najafzadeh22/ai-lab-g2-mohammad-ali-najaf-zadeh/blob/9c840eecff85c84b3d6a0344056cc213ab30ed08/homeworks/task_2/lab2_heuristic_comparison.ipynb): مقایسهٔ Dijkstra، A* با heuristic اقلیدسی و A* با heuristic منهتن در نقشه‌ها و قوانین حرکت مختلف.

### انتخاب مجموعه‌داده

README این مخزن، مجموعه‌دادهٔ **MADBase** را معرفی می‌کند: تصاویر خاکستری ۲۸×۲۸ از ارقام دست‌نویس عربی-هندی ۰ تا ۹. در مستندات پروژه اندازهٔ مجموعه حدود ۷۰٬۰۰۰ تصویر با تقسیم رسمی ۶۰٬۰۰۰ نمونهٔ آموزش و ۱۰٬۰۰۰ نمونهٔ آزمون ذکر شده است.

منبع اصلی داده، مرکز دادهٔ دانشگاه آمریکایی قاهره معرفی شده و نسخهٔ مورد استفاده از [Hugging Face](https://huggingface.co/datasets/MagedSaeed/MADBase) دریافت می‌شود. README به این نکات نیز اشاره می‌کند:

- بر اساس توضیحات کارت مجموعه‌داده، استفادهٔ پژوهشی عمومی مجاز دانسته شده و ارجاع به مقالهٔ اصلی لازم است؛ اما مجوز متن‌باز رسمی مانند MIT یا CC-BY مشخص نشده است.
- استفادهٔ توصیف‌شده برای پروژهٔ آموزشی و غیرتجاری است.
- نسخهٔ Hugging Face بنا بر README تعداد ۶۹٬۹۹۸ ردیف دارد، نه ۷۰٬۰۰۰؛ بنابراین منبع اصلی نیز برای استناد ذکر شده است.
- پیش از بازتوزیع یا استفادهٔ تجاری، شرایط اصلی مجموعه‌داده باید بررسی شود.

**ارجاع پیشنهادی در README مخزن:**

> El-Sherif, E. A., & Abdelazeem, S. (2007). *A Two-Stage System for Arabic Handwritten Digit Recognition Tested on a New Large Database*. Artificial Intelligence and Pattern Recognition, 237–242.

### بررسی محیط

نوت‌بوک `check_env.ipynb` اطلاعات محیط اجرا را نمایش می‌دهد. خروجی ثبت‌شده شامل Python 3.14.6، نسخهٔ NumPy برابر 2.4.6 و Matplotlib برابر 3.11.0 است. این مقادیر خروجی همان اجرای ذخیره‌شده‌اند؛ برای اطلاع از وضعیت فعلی، نوت‌بوک را در محیط خود اجرا کنید.

### مقایسهٔ الگوریتم‌های جست‌وجو

نوت‌بوک `lab2_heuristic_comparison.ipynb` یک آزمایش مستقل برای مقایسهٔ heuristicها در A* است. محیط‌ها شامل نقشه‌های باز، تصادفی، پرتراکم، راهروها و زمین با هزینه‌های متفاوت‌اند. حرکت چهارجهته و هشت‌جهته نیز بررسی می‌شود.

روش‌های مقایسه‌شده:

- **Dijkstra:** معادل جست‌وجو با heuristic صفر؛ مسیر بهینه را مرجع مقایسه قرار می‌دهد.
- **Manhattan:** مجموع فاصلهٔ افقی و عمودی تا مقصد.
- **Euclidean:** فاصلهٔ مستقیم اقلیدسی تا مقصد.

نوت‌بوک تعداد خانه‌های گسترش‌یافته، هزینهٔ مسیر و درصد مسیرهای بهینه را گزارش می‌کند و نقشه‌ها و نمودارها را نمایش می‌دهد. در خروجی ثبت‌شده، در سناریوی تصادفی ۲۵٪ با حرکت هشت‌جهته، Manhattan در ۴۶ مورد از ۷۱ نقشه مسیر غیربهینه پیدا کرده است؛ در بدترین مورد، هزینهٔ مسیر ۱۰٫۸٪ بیشتر از مقدار بهینه بوده است.

این نتیجه با تفاوت قوانین حرکت مرتبط است: در حرکت چهارجهته، Manhattan می‌تواند heuristic مناسبی باشد؛ اما در حرکت هشت‌جهته، ممکن است هزینهٔ واقعی را بیش‌برآورد کند. بنابراین انتخاب heuristic باید با قوانین حرکت و هزینه‌های محیط سازگار باشد.

---

## ۲. مخزن rezolens

**مخزن:** [ai-lab-all-step-reza-dehghani](https://github.com/rezolens/ai-lab-all-step-reza-dehghani)  
**پوشه:** [`step 2`](https://github.com/rezolens/ai-lab-all-step-reza-dehghani/tree/36c6c45dc639083c4c6590e53c7eeeb631dee385/step%202)

### فایل‌ها

- [`check_env.ipynb`](https://github.com/rezolens/ai-lab-all-step-reza-dehghani/blob/36c6c45dc639083c4c6590e53c7eeeb631dee385/step%202/check_env.ipynb): بررسی نسخهٔ Python، مسیر اجرا، کتابخانه‌ها و دسترسی به مجموعهٔ آزمایشی Digits در Scikit-learn.
- [`g2.ipynb`](https://github.com/rezolens/ai-lab-all-step-reza-dehghani/blob/36c6c45dc639083c4c6590e53c7eeeb631dee385/step%202/g2.ipynb): دریافت و آماده‌سازی MADBase.
- [`lab2_pathfinding-developed.ipynb`](https://github.com/rezolens/ai-lab-all-step-reza-dehghani/blob/36c6c45dc639083c4c6590e53c7eeeb631dee385/step%202/lab2_pathfinding-developed.ipynb): تمرین مستقل جست‌وجوی مسیر با BFS، DFS و A*.
- [`readme.md`](https://github.com/rezolens/ai-lab-all-step-reza-dehghani/blob/36c6c45dc639083c4c6590e53c7eeeb631dee385/step%202/readme.md): خلاصه‌ای از فرایند آماده‌سازی داده.

### بررسی محیط

نوت‌بوک `check_env.ipynb` نسخهٔ Python و نسخهٔ کتابخانه‌های NumPy، Matplotlib، Pandas و Scikit-learn را نمایش می‌دهد. همچنین با ساخت یک آرایه، رسم نمودار و بارگذاری مجموعهٔ Digits، کارکرد اولیهٔ کتابخانه‌ها را می‌آزماید.

در خروجی ثبت‌شده، نسخه‌های چاپ‌شده در سلول import با خروجی دستور `pip list` یکسان نیستند. برای مشاهدهٔ وضعیت واقعی محیط، نوت‌بوک را دوباره اجرا کنید و مطمئن شوید Jupyter از همان محیط Python استفاده می‌کند که کتابخانه‌ها در آن نصب شده‌اند.

### دریافت و آماده‌سازی MADBase

نوت‌بوک `g2.ipynb` مجموعهٔ [`MagedSaeed/MADBase`](https://huggingface.co/datasets/MagedSaeed/MADBase) را از Hugging Face دریافت می‌کند. سپس:

1. بخش‌های موجود مجموعه‌داده و ستون‌های تصاویر و برچسب‌ها را بررسی می‌کند.
2. تصاویر را به حالت خاکستری تبدیل و به آرایه‌های NumPy با نوع `uint8` تبدیل می‌کند.
3. تعداد نمونه‌ها، ابعاد، بازهٔ مقادیر پیکسل و برچسب‌های موجود را بررسی می‌کند.
4. چند تصویر نمونه را همراه با برچسب نمایش می‌دهد.
5. آرایه‌ها را در فایل فشردهٔ `handwritten_digits_data.npz` ذخیره می‌کند.

خروجی ثبت‌شده در نوت‌بوک:

- آموزش: ۵۹٬۹۹۹ تصویر ۲۸×۲۸
- آزمون: ۹٬۹۹۹ تصویر ۲۸×۲۸
- برچسب‌ها: ارقام ۰ تا ۹
- کلیدهای فایل خروجی: `train_images`، `train_labels`، `test_images` و `test_labels`

این نوت‌بوک مدل یادگیری ماشین آموزش نمی‌دهد و دقت تشخیص را محاسبه نمی‌کند؛ هدفش دریافت و آماده‌سازی داده است.

### تمرین جست‌وجوی مسیر

نوت‌بوک `lab2_pathfinding-developed.ipynb` تمرینی مستقل از تشخیص رقم است. در آن BFS و DFS با A* روی نقشه‌های شبکه‌ای مقایسه می‌شوند. نوت‌بوک مسیرها و خانه‌های گسترش‌یافته را رسم می‌کند، الگوریتم‌ها را روی نقشه‌های تصادفی می‌آزماید و نمایش انیمیشنی از روند جست‌وجو دارد.

### اجرای نوت‌بوک‌ها

محیط ذکرشده در پروژه Anaconda و Jupyter است. سلول‌ها را از ابتدا به‌ترتیب اجرا کنید. برای دریافت MADBase دسترسی اینترنت لازم است. اگر کتابخانهٔ `datasets` نصب نباشد، نوت‌بوک `g2.ipynb` تلاش می‌کند آن را نصب کند.

---

## ۳. مخزن deathtoconding

**مخزن:** [AI-lab-amirhossein-hassani](https://github.com/deathtoconding/AI-lab-amirhossein-hassani)  
**پوشه:** [`step-2`](https://github.com/deathtoconding/AI-lab-amirhossein-hassani/tree/11a591fe2263ea6b6b243675a79ae10097d3c998/step-2)

### فایل‌ها

- [`data_quality_and_evaluation.ipynb`](https://github.com/deathtoconding/AI-lab-amirhossein-hassani/blob/11a591fe2263ea6b6b243675a79ae10097d3c998/step-2/data_quality_and_evaluation.ipynb): بررسی کیفیت MADBase و ساخت مجموعه‌های آموزش، اعتبارسنجی و آزمون.
- [`lab2_pathfinding2.ipynb`](https://github.com/deathtoconding/AI-lab-amirhossein-hassani/blob/11a591fe2263ea6b6b243675a79ae10097d3c998/step-2/lab2_pathfinding2.ipynb): تمرین مستقل الگوریتم‌های BFS، DFS و A*.
- [`how.md`](https://github.com/deathtoconding/AI-lab-amirhossein-hassani/blob/11a591fe2263ea6b6b243675a79ae10097d3c998/step-2/how.md): توضیحی دربارهٔ تهیه و ویرایش محتوای پروژه.

### ارزیابی و آماده‌سازی دادهٔ ارقام

نوت‌بوک `data_quality_and_evaluation.ipynb` فایل `handwritten_digits_data.npz` را ورودی می‌گیرد. فایل باید در کنار نوت‌بوک باشد یا مسیر آن در متغیر `DATA_PATH` تنظیم شود.

بررسی‌های نوت‌بوک شامل موارد زیر است:

- وجود آرایه‌های تصاویر و برچسب‌های آموزش و آزمون، ابعاد و نوع دادهٔ آن‌ها
- شکل تصاویر (۲۸×۲۸)، بازهٔ مقادیر پیکسل و معتبر بودن برچسب‌های ۰ تا ۹
- تصاویر خالی و توزیع نمونه‌ها میان کلاس‌ها
- تصاویر تکراری دقیق درون مجموعه‌ها و تصاویر مشترک میان آموزش و آزمون
- حذف نسخه‌های تکراری و هم‌پوشانی دقیق از دادهٔ توسعه
- ساخت تقسیم‌بندی طبقه‌بندی‌شدهٔ آموزش و اعتبارسنجی با `random_state=42` و اندازهٔ اعتبارسنجی ۲۰٪

بر اساس خروجی ثبت‌شده:

- دادهٔ آموزش اولیه: ۵۹٬۹۹۹ نمونه
- داده‌های دارای برچسب متناقض برای تصویرهای یکسان که حذف شده‌اند: صفر
- نمونه‌های حذف‌شده به‌دلیل هم‌پوشانی دقیق با آزمون رسمی: ۲۳
- نسخه‌های تکراری حذف‌شده از مجموعهٔ توسعه: ۵٬۰۳۴
- دادهٔ توسعهٔ یکتا پس از پاک‌سازی: ۵۴٬۹۴۲ نمونه
- مجموعهٔ آموزش آماده‌شده: ۴۳٬۹۵۳ نمونه
- مجموعهٔ اعتبارسنجی: ۱۰٬۹۸۹ نمونه
- مجموعهٔ آزمون رسمی: ۹٬۹۹۹ نمونه و بدون تغییر
- هم‌پوشانی تصویرهای دقیق میان مجموعه‌های نهایی: صفر

خروجی‌های نوت‌بوک عبارت‌اند از:

- `prepared_handwritten_digits_data.npz`: آرایه‌های آموزش، اعتبارسنجی و آزمون
- `data_quality_report.json`: گزارش ماشین‌خوان شامل آمار داده، پاک‌سازی و بررسی کیفیت

بررسی تکرارها با hash دقیق پیکسل‌ها انجام می‌شود؛ این کار لزوماً تکرارهای نزدیک یا هم‌پوشانی در سطح نویسنده را شناسایی نمی‌کند.

### تمرین جست‌وجوی مسیر

نوت‌بوک `lab2_pathfinding2.ipynb` تمرینی جدا از خط لولهٔ تشخیص ارقام است. این نوت‌بوک BFS و DFS را با A* روی نقشه‌های تصادفی مقایسه می‌کند و مسیر و خانه‌های گسترش‌یافته را نمایش می‌دهد.

در اجرای ثبت‌شده، روی نقشهٔ نمونه BFS و A* مسیر ۲۳ حرکتی پیدا کرده‌اند؛ DFS مسیر ۵۳ حرکتی یافته است. در آزمایش ۱۰۰ نقشهٔ تصادفی، ۷۲ نقشه قابل حل بوده‌اند. این اعداد به تنظیمات نقشه و بذر تصادفی همان نوت‌بوک مربوط‌اند.

### اجرای نوت‌بوک ارزیابی

۱. فایل `handwritten_digits_data.npz` را کنار نوت‌بوک قرار دهید یا `DATA_PATH` را تنظیم کنید.
۲. نوت‌بوک را در Jupyter باز کنید.
۳. سلول‌ها را به‌ترتیب اجرا کنید.
۴. فایل‌های دادهٔ آماده‌شده و گزارش JSON را در مسیر خروجی تعیین‌شده بررسی کنید.

---

## ارتباط سه مخزن

مخزن‌های `ma-najafzadeh22` و `rezolens` دربارهٔ انتخاب و معرفی MADBase و کار با داده‌های آن اطلاعات می‌دهند. نوت‌بوک `g2.ipynb` در مخزن `rezolens` داده را دریافت و فایل اولیهٔ `handwritten_digits_data.npz` را تولید می‌کند. نوت‌بوک `data_quality_and_evaluation.ipynb` در مخزن `deathtoconding` می‌تواند آن فایل را بررسی و نسخهٔ آماده‌شدهٔ `prepared_handwritten_digits_data.npz` را تولید کند.

مخزن `ma-najafzadeh22` علاوه بر مستندات انتخاب داده، آزمایش جداگانه‌ای دربارهٔ اثر heuristicهای A* دارد. نوت‌بوک‌های جست‌وجوی مسیر در دو مخزن دیگر نیز تمرین‌های مستقل هستند و به آماده‌سازی یا آموزش مدل تشخیص رقم وابسته نیستند.

| فایل | نقش |
|---|---|
| `handwritten_digits_data.npz` | دادهٔ اولیهٔ تصاویر و برچسب‌های آموزش و آزمون |
| `prepared_handwritten_digits_data.npz` | دادهٔ بررسی‌شده و پاک‌سازی‌شده با مجموعه‌های آموزش، اعتبارسنجی و آزمون |
| `data_quality_report.json` | گزارش نتایج بررسی کیفیت و پاک‌سازی |

مقادیر و آمار بالا از خروجی‌های ذخیره‌شده در نوت‌بوک‌ها و READMEهای مخزن‌ها نقل شده‌اند؛ با اجرای دوبارهٔ نوت‌بوک‌ها ممکن است محیط، نسخهٔ داده یا خروجی‌ها متفاوت باشند.