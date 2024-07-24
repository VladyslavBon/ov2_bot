import pytz
import os

from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.types.callback_query import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import keyboard
import text
from states import Form
from config import settings

scheduler = AsyncIOScheduler(timezone=pytz.timezone("Europe/Kiev"))

if os.path.exists('counter.txt'):
    with open('counter.txt', 'r') as file:
        count = int(file.read())
else:
    count = 0
            
def setup(router: Router, bot):
    
    async def send_daily_count():
        with open('counter.txt', 'r') as file:
            count = int(file.read())
        text = f'Загальна кількість запусків бота:  {count}'
        await bot.send_message(settings.admin_id, text)

    scheduler.add_job(send_daily_count, 'cron', hour=12, minute=0)
    
    @router.message(Command("start"))
    async def start_handler(msg: types.Message):
        global count 
        count += 1
        with open('counter.txt', 'w') as file:
            file.write(str(count))
        await msg.answer(
            text.greet, reply_markup=keyboard.menu
        )


    @router.message(F.text == "Меню")
    @router.message(F.text == "Вийти в меню")
    @router.message(F.text == "◀️ Повернутись на початок")
    @router.callback_query(F.data == "menu")
    async def menu(clbck: CallbackQuery):
        await clbck.message.answer(text.greet, reply_markup=keyboard.menu)


    @router.callback_query(F.data == "project_cost")
    async def input_project_cost(clbck: CallbackQuery):
        await clbck.message.answer(text.project_cost, reply_markup=keyboard.project_cost_menu)
        
        
    @router.callback_query(F.data == "to_60")
    async def input_to_60(clbck: CallbackQuery):
        await clbck.message.answer(text.project_cost_next["to_60"], reply_markup=keyboard.project_cost_next_menu)

    @router.callback_query(F.data == "from_60_to_100")
    async def input_from_60_to_100(clbck: CallbackQuery):
        await clbck.message.answer(text.project_cost_next["from_60_to_100"], reply_markup=keyboard.project_cost_next_menu)
        
    @router.callback_query(F.data == "from_100")
    async def input_from_100(clbck: CallbackQuery):
        await clbck.message.answer(text.project_cost_next["from_100"], reply_markup=keyboard.project_cost_next_menu)

    @router.callback_query(F.data == "recall")
    async def input_recall(clbck: CallbackQuery, state: FSMContext):
        await clbck.message.answer(text.recall, reply_markup = keyboard.contact_button)
        await state.set_state(Form.waiting_for_contact)
        

    @router.message(F.contact)
    async def send_contact(msg: types.Message, state: FSMContext):
        user_id_to_send = settings.admin_id
        await bot.send_message(chat_id=user_id_to_send, text=f"{text.send_contact}")
        await bot.send_contact(
            chat_id=user_id_to_send,
            phone_number=msg.contact.phone_number,
            first_name=msg.contact.first_name,
            last_name=msg.contact.last_name if msg.contact.last_name else ''
        )
        await msg.answer(text.thanks_recall, reply_markup=ReplyKeyboardRemove())
        
        await state.clear()
        
    @router.callback_query(F.data == "author_support")
    async def input_author_support(clbck: CallbackQuery):
        await clbck.message.answer(text.author_support, reply_markup = keyboard.author_support_menu)
        
    @router.callback_query(F.data == "kyiv")
    async def input_kyiv(clbck: CallbackQuery):
        await clbck.message.answer(text.author_support_cost_text, reply_markup = keyboard.author_support_cost_menu_kyiv)
        
    @router.callback_query(F.data == "kyiv_oblast")
    async def input_kyiv_oblast(clbck: CallbackQuery):
        await clbck.message.answer(text.author_support_cost_text, reply_markup = keyboard.author_support_cost_menu_kyiv_oblast)
        
    @router.callback_query(F.data == "what_included")
    async def input_what_included(clbck: CallbackQuery):
        await clbck.message.answer(text.author_support_what_included, reply_markup = keyboard.author_support_previous)
        
    # @router.callback_query(F.data == "service_cost_kyiv")
    # async def input_service_cost_kyiv(clbck: CallbackQuery):
    #     await clbck.message.edit_reply_markup(reply_markup = keyboard.author_support_cost_menu_kyiv)
        
    # @router.callback_query(F.data == "service_cost_kyiv_oblast")
    # async def input_service_cost_kyiv_oblast(clbck: CallbackQuery):
    #     await clbck.message.edit_reply_markup(reply_markup = keyboard.author_support_cost_menu_kyiv_oblast)
        
    @router.callback_query(F.data == "author_to_60_kyiv")
    async def input_author_to_60_kyiv(clbck: CallbackQuery):
        await clbck.message.answer(text.author_support_cost["kyiv_to_60"], reply_markup=keyboard.author_exit_menu)

    @router.callback_query(F.data == "author_from_60_to_100_kyiv")
    async def input_author_from_60_to_100_kyiv(clbck: CallbackQuery):
        await clbck.message.answer(text.author_support_cost["kyiv_from_60_to_100"], reply_markup=keyboard.author_exit_menu)
        
    @router.callback_query(F.data == "author_from_100_kyiv")
    async def input_author_from_100_kyiv(clbck: CallbackQuery):
        await clbck.message.answer(text.author_support_cost["kyiv_from_100"], reply_markup=keyboard.author_exit_menu)
        
    @router.callback_query(F.data == "author_to_60_kyiv_oblast")
    async def input_author_to_60_kyiv_oblast(clbck: CallbackQuery):
        await clbck.message.answer(text.author_support_cost["kyiv_oblast_to_60"], reply_markup=keyboard.author_exit_menu)

    @router.callback_query(F.data == "author_from_60_to_100_kyiv_oblast")
    async def input_author_from_60_to_100_kyiv_oblast(clbck: CallbackQuery):
        await clbck.message.answer(text.author_support_cost["kyiv_oblast_from_60_to_100"], reply_markup=keyboard.author_exit_menu)
        
    @router.callback_query(F.data == "author_from_100_kyiv_oblast")
    async def input_author_from_100_kyiv_oblast(clbck: CallbackQuery):
        await clbck.message.answer(text.author_support_cost["kyiv_oblast_from_100"], reply_markup=keyboard.author_exit_menu)
        
    @router.callback_query(F.data == "project_example")
    async def input_project_example(clbck: CallbackQuery):
        await clbck.message.answer(text.project_example, reply_markup=keyboard.project_example)
        
    @router.callback_query(F.data == "planning")
    async def input_planning(clbck: CallbackQuery):
        await clbck.message.answer(text.planning, reply_markup=keyboard.planning_menu)
        
    @router.callback_query(F.data == "what_included_planning")
    async def input_what_included_planning(clbck: CallbackQuery):
        await clbck.message.answer(text.what_included_planning, reply_markup=keyboard.planning_previous)  
    
    @router.callback_query(F.data == "service_cost_planning")
    async def input_service_cost_planning(clbck: CallbackQuery):
        await clbck.message.answer(text.service_cost_planning, reply_markup = keyboard.planning_cost_menu)
    
    @router.callback_query(F.data == "to_100_planning")
    async def input_from_60_to_100_planning(clbck: CallbackQuery):
        await clbck.message.answer(text.planning_cost["to_100_planning"], reply_markup=keyboard.exit_menu)
        
    @router.callback_query(F.data == "from_100_to_200_planning")
    async def input_from_100_to_200_planning(clbck: CallbackQuery):
        await clbck.message.answer(text.planning_cost["from_100_to_200_planning"], reply_markup=keyboard.exit_menu)

    @router.callback_query(F.data == "from_200_to_300_planning")
    async def input_from_200_to_300_planning(clbck: CallbackQuery):
        await clbck.message.answer(text.planning_cost["from_200_to_300_planning"], reply_markup=keyboard.exit_menu)
        
    @router.callback_query(F.data == "from_300_planning")
    async def input_from_300_planning(clbck: CallbackQuery):
        await clbck.message.answer(text.planning_cost["from_300_planning"], reply_markup=keyboard.exit_menu)
        
    @router.callback_query(F.data == "project_terms")
    async def input_project_terms(clbck: CallbackQuery):
        await clbck.message.answer(text.project_terms, reply_markup=keyboard.planning_terms_menu)
        
    @router.callback_query(F.data == "to_60_terms")
    async def input_to_60_terms(clbck: CallbackQuery):
        await clbck.message.answer(text.planning_terms["to_60_terms"], reply_markup=keyboard.exit_menu)
        
    @router.callback_query(F.data == "from_60_to_100_terms")
    async def input_from_60_to_100_terms(clbck: CallbackQuery):
        await clbck.message.answer(text.planning_terms["from_60_to_100_terms"], reply_markup=keyboard.exit_menu)

    @router.callback_query(F.data == "from_100_to_250_terms")
    async def input_from_100_to_250_terms(clbck: CallbackQuery):
        await clbck.message.answer(text.planning_terms["from_100_to_250_terms"], reply_markup=keyboard.exit_menu)
        
    @router.callback_query(F.data == "from_250_terms")
    async def input_from_250_terms(clbck: CallbackQuery):
        await clbck.message.answer(text.planning_terms["from_250_terms"], reply_markup=keyboard.exit_menu)