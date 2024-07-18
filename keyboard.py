from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
import text


menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💳 Вартість дизайн проєкту", callback_data="project_cost")
        ],
        [
            InlineKeyboardButton(text="⏱️ Терміни виконання проєкту", callback_data="project_terms")
        ],
        [
            InlineKeyboardButton(text="🛠️ Авторський супровід", callback_data="author_support")
        ],
        [
            InlineKeyboardButton(text="📐Планування", callback_data="planning")
        ],
        [
            InlineKeyboardButton(text="📒 Приклад проєкту", callback_data="project_example")
        ],
        [
            InlineKeyboardButton(text="📲 Зворотній звʼязок", callback_data="recall")
        ]
    ]
)

iexit_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Повернутись на початок", callback_data="menu")]
    ]
)


project_cost_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="До 60 м²", callback_data="to_60")
        ],
        [
            InlineKeyboardButton(text="Від 60 до 100 м²", callback_data="from_60_to_100")
        ],
        [
            InlineKeyboardButton(text="Від 100 м²", callback_data="from_100")
        ],
        [
            InlineKeyboardButton(text="◀️ Повернутись назад", callback_data="menu")
        ]
    ]
)

project_cost_next_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛠️ Авторський супровід", callback_data="author_support")
        ],
        [
            InlineKeyboardButton(text="📲 Зворотній звʼязок", callback_data="recall")
        ],
        [
            InlineKeyboardButton(text="◀️ Повернутись назад", callback_data="project_cost")
        ]
    ]
)

contact_button = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Надіслати свій контакт", request_contact=True)]], resize_keyboard=True, one_time_keyboard=True
        )

author_support_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Київ", callback_data="kyiv")
        ],
        [
            InlineKeyboardButton(text="Київська обл", callback_data="kyiv_oblast")
        ],
        [
            InlineKeyboardButton(text="◀️ Повернутись на початок", callback_data="menu")
        ]
    ]
)

author_support_menu_next_kyiv = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Що входить у послугу", callback_data="what_included")
        ],
        [
            InlineKeyboardButton(text="Вартість послуги", callback_data="service_cost_kyiv")
        ],
        [
            InlineKeyboardButton(text="◀️ Повернутись назад", callback_data="author_support")
        ]
    ]
)

author_support_menu_next_kyiv_oblast = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Що входить у послугу", callback_data="what_included")
        ],
        [
            InlineKeyboardButton(text="Вартість послуги", callback_data="service_cost_kyiv_oblast")
        ],
        [
            InlineKeyboardButton(text="◀️ Повернутись назад", callback_data="author_support")
        ]
    ]
)

author_support_previous = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Повернутись назад", callback_data="kyiv")
        ]
    ]
)

author_support_cost_menu_kyiv = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="До 60 м²", callback_data="author_to_60_kyiv")
        ],
        [
            InlineKeyboardButton(text="Від 60 до 100 м²", callback_data="author_from_60_to_100_kyiv")
        ],
        [
            InlineKeyboardButton(text="Від 100 м²", callback_data="author_from_100_kyiv")
        ],
        [
            InlineKeyboardButton(text="◀️ Повернутись назад", callback_data="kyiv")
        ]
    ]
)

author_support_cost_menu_kyiv_oblast = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="До 60 м²", callback_data="author_to_60_kyiv_oblast")
        ],
        [
            InlineKeyboardButton(text="Від 60 до 100 м²", callback_data="author_from_60_to_100_kyiv_oblast")
        ],
        [
            InlineKeyboardButton(text="Від 100 м²", callback_data="author_from_100_kyiv_oblast")
        ],
        [
            InlineKeyboardButton(text="◀️ Повернутись назад", callback_data="kyiv_oblast")
        ]
    ]
)

project_example = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Переглянути проєкт", url=text.url, callback_data="project_look")
        ],
        [
            InlineKeyboardButton(text="📲 Зворотній звʼязок", callback_data="recall")
        ],
        [
            InlineKeyboardButton(text="◀️ Повернутись на початок", callback_data="menu")
        ]
    ]
)

exit_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📲 Зворотній звʼязок", callback_data="recall")
        ],
        [
            InlineKeyboardButton(text="◀️ Повернутись на початок", callback_data="menu")
        ]
    ]
)

planning_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Що входить у послугу", callback_data="what_included_planning")
        ],
        [
            InlineKeyboardButton(text="Вартість послуги", callback_data="service_cost_planning")
        ],
        [
            InlineKeyboardButton(text="◀️ Повернутись назад", callback_data="menu")
        ]
    ]
)

planning_previous = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Повернутись назад", callback_data="planning")
        ]
    ]
)

planning_cost_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="До 100 м²", callback_data="to_100_planning")
        ],
        [
            InlineKeyboardButton(text="Від 100 до 200 м²", callback_data="from_100_to_200_planning")
        ],
        [
            InlineKeyboardButton(text="Від 200 до 300 м²", callback_data="from_200_to_300_planning")
        ],
        [
            InlineKeyboardButton(text="Від 300 м²", callback_data="from_300_planning")
        ],
        [
            InlineKeyboardButton(text="◀️ Повернутись назад", callback_data="service_cost_planning")
        ]
    ]
)

planning_terms_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="До 60 м²", callback_data="to_60_terms")
        ],
        [
            InlineKeyboardButton(text="Від 60 до 100 м²", callback_data="from_60_to_100_terms")
        ],
        [
            InlineKeyboardButton(text="Від 100 до 250 м²", callback_data="from_100_to_250_terms")
        ],
        [
            InlineKeyboardButton(text="Від 250 м²", callback_data="from_250_terms")
        ],
        [
            InlineKeyboardButton(text="◀️ Повернутись назад", callback_data="menu")
        ]
    ]
)
