greet = """
Вітаємо вас у чат-боті <b>дизайн студії OV2</b>

Наша команда розроблює та реалізовує дизайн проєкти для різних обʼєктів - квартир, приватних будинків та комерційних приміщень.

◉ <b>більше 7 років досвіду</b>
◉ <b>+ 400 розроблених дизайн проєктів</b>
◉ <b>+ 150 реалізованих обʼєктів</b>
◉ <b>12 професіоналів в команді</b>

Ми точно знаємо як створити стильне, ергономічне та функціональне житло вашої мрії з урахуванням індивідуальних потреб, побажань та бюджету👌🏻

<i>Тут ви зможете отримати швидку та чітку інформацію щодо наших послуг</i> ↴
"""

project_cost_next = {
    "to_60": """
    Наразі в нас діє <b>спеціальна пропозиція</b> на розробку дизайн проєкту👌🏻

На Вашу площу вартість наших послуг (планувальні рішення + креслення для будівельників та для меблярів + фотореалістичні 3д візуалізації + повна специфікація на всі меблі, сантехніку, світло, оздоблення, тощо) - <b>2100$</b>

<i>В дизайн проєкті надана максимально деталізована та чітка інформація для успішної реалізації обʼєкту</i>
""",
    "from_60_to_100": """
    Наразі в нас діє <b>спеціальна пропозиція</b> на розробку дизайн проєкту👌🏻

На Вашу площу вартість наших послуг (планувальні рішення + креслення для будівельників та для меблярів + фотореалістичні 3д візуалізації + повна специфікація на всі меблі, сантехніку, світло, оздоблення, тощо) - <b>35$ за м²</b>

<i>В дизайн проєкті надана максимально деталізована та чітка інформація для успішної реалізації обʼєкту</i>
""", 
    "from_100": """
    Наразі в нас діє <b>спеціальна пропозиція</b> на розробку дизайн проєкту👌🏻

На Вашу площу вартість наших послуг (планувальні рішення + креслення для будівельників та для меблярів + фотореалістичні 3д візуалізації + повна специфікація на всі меблі, сантехніку, світло, оздоблення, тощо) - <b>30$ за м²</b>

<i>В дизайн проєкті надана максимально деталізована та чітка інформація для успішної реалізації обʼєкту</i>
"""
}

project_cost = "Вартість дизайн проєкту залежить від площі обʼєкту(м²)"

send_contact = "Цей клієнт замовив зворотній звʼязок, передзвоніть йому будь ласка:"

recall = "Натисни на кнопку знизу, щоб відправити контакт ↴"

thanks_recall = "Дякуємо, ми з вами звʼяжемося найближчим часом👌🏻"

author_support = """
На сьогоднішній день ми ведемо супровід в Києві та Київській області.

<b>Де знаходиться ваш обʼєкт?</b>
"""

author_support_what_included = """
В послугу <b>Авторський супровід</b> входить:

▪️Перевірена будівельна бригада та меблева компанія, які реалізують ваш обʼєкт під ключ.
▪️Перевірка та контроль якості виконання будівельних робіт після кожного етапу.
▪️Консультація будівельників щодо виконання тих чи інших вузлів під час реалізації об’єкту.
▪️Детальний підбір, формування кошторису та заміна під час ремонту по необхідності: оздоблювальних матеріалів; меблевої фурнітури; електрофурнітури; дверей; освітлення; сантехніки тощо.
▪️Системи знижок партнерів на будь-який товар, що зазначений в дизайн проєкті.
▪️Поміч у закупівлі будівельного товару завчасно, завдяки складанню графіків закупок в CRM-системі
 """

author_support_cost_text = "Вартість авторського супроводу залежить від площі обʼєкту(м²):"

author_support_cost = {
    "kyiv_to_60": """
    Авторський нагляд під час ремонту - <b>1200$</b>
    
Ця послуга  допоможе зекономити ваш час та гроші під час реалізації обʼєкту.

<i>* договір на один рік з можливістю подальшої пролонгації</i>
""",
    "kyiv_from_60_to_100": """
    Авторський нагляд під час ремонту - <b>20$ за м²</b>
    
Ця послуга  допоможе зекономити ваш час та гроші під час реалізації обʼєкту.

<i>* договір на один рік з можливістю подальшої пролонгації</i>
""", 
    "kyiv_from_100": """
    Авторський нагляд під час ремонту - <b>15$ за м²</b>
    
Ця послуга  допоможе зекономити ваш час та гроші під час реалізації обʼєкту.

<i>* договір на один рік з можливістю подальшої пролонгації</i>
""",
    "kyiv_oblast_to_60": """
    Авторський нагляд під час ремонту - <b>1500$</b>
    
Ця послуга  допоможе зекономити ваш час та гроші під час реалізації обʼєкту.

<i>* договір на один рік з можливістю подальшої пролонгації</i>
""",
    "kyiv_oblast_from_60_to_100": """
    Авторський нагляд під час ремонту - <b>25$ за м²</b>
    
Ця послуга  допоможе зекономити ваш час та гроші під час реалізації обʼєкту.

<i>* договір на один рік з можливістю подальшої пролонгації</i>
""", 
    "kyiv_oblast_from_100": """
    Авторський нагляд під час ремонту - <b>20$ за м²</b>
    
Ця послуга  допоможе зекономити ваш час та гроші під час реалізації обʼєкту.

<i>* договір на один рік з можливістю подальшої пролонгації</i>
"""
}

project_example = """
Якісна та детальна робоча документація  є запорукою подальшої успішної реалізації обʼєкту👌🏻

<b>Приклад нашого дизайн проєкту</b> можете переглянути нижче ↴
"""

planning = """
<b>Планування</b> - це основа дизайн проєкту, яка потребує особливої уваги та професійного досвіду.

Наша студія створить для вас комфортне та функціональне планування з урахуванням ергономічних норм✔️
"""

what_included_planning = """
Вам буде запропоновано до 4-х варіантів планування:
▪️<b>1-й варіант</b> - створюємо з урахуванням усіх ваших побажань та потреб відносно існуючої архітектури житла.
▪️<b>2-й варіант</b> - робимо перепланування простору покладаючись на наш досвід, з врахуванням ваших потреб та побажань.
▪️<b>3-й та 4-й варіант</b> (по необхідності) - фінальний, це поєднання двох перших варіантів з урахуванням всіх корегувань.

<i>План після перепланування житла з усіма розмірами та площами</i>
"""

service_cost_planning = "Вартість послуги <b>планування</b> залежить від площі обʼєкту(м²):"

planning_cost = {
    "to_100_planning": """
    Вартість планування на вашу площу - <b>500$</b>
""",
    "from_100_to_200_planning": """
    Вартість планування на вашу площу - <b>900$</b>
""", 
    "from_200_to_300_planning": """
    Вартість планування на вашу площу - <b>1300$</b>
""",
    "from_300_planning": """
    Вартість планування на вашу площу - <b>обговорюється індивідуально</b>
"""
}

project_terms = "Термін розробки дизайн проєкту залежить від площі обʼєкту(м²):"

planning_terms = {
    "to_60_terms": """
    На вашу площу термін виконання дизайн проєкту - <b>2 місяці</b>
    
<i>* терміни фіксуються у договорі</i>
""",
    "from_60_to_100_terms": """
    На вашу площу термін виконання дизайн проєкту - <b>2,5 місяці</b>
    
<i>* терміни фіксуються у договорі</i>
""", 
    "from_100_to_250_terms": """
    На вашу площу термін виконання дизайн проєкту - <b>2,5-3 місяці</b>
    
<i>* терміни фіксуються у договорі</i>
""",
    "from_250_terms": """
    На вашу площу термін виконання дизайн проєкту - <b>від 3 місяців</b>
    
<i>* терміни фіксуються у договорі</i>
"""
}

url = "https://ov2.com.ua/wp-content/uploads/2024/06/project_example.pdf"