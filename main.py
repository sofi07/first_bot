from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils import executor
import random
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboard import menu, menu2
from inline_keyboard import start_kb, admin_start

# from config import TOKEN
from states import Register

TOKEN = '1620272486:AAFVmhtB5fFDo9mgKA8A83_kpVoKTnq96hQ'

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

choices = ['камень', 'ножницы', 'бумага']
admin = ['админка', 'админ', 'администрация']


@dp.message_handler(CommandStart())
async def reg(message: types.Message):
    await message.answer('Для получения полного функционала нужно зарегистрироваться. Но вы так же можете поиграть в игру.', reply_markup=start_kb)
    await message.answer(f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}\n'
                         f'Чтобы пользоваться, вам нужно зарегистрироваться.\n',
                         reply_markup=menu2)


@dp.callback_query_handler(lambda x:
                           x.data == '1-1')
async def reg_start(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, text='Введите номер телефона.')
    await Register.First.set()




@dp.message_handler(lambda x:
                    len(str(x.text)) == 11 and str(x.text)[:2] == '89',
                    state=Register.First)
async def first(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()
    await message.answer(f'Ваш номер телефона: {data.get("phone")} \n Введите адрес почты: ')
    await Register.Second.set()



@dp.message_handler(state=Register.First)
async def first(message: types.Message, state: FSMContext):
    await message.answer('Вы не прислали номер телефона, попробуйте ещё раз.')



@dp.message_handler(lambda x:
                    '@' in x.text and '.' in x.text and x.text.index('@') > 0 and x.text.index('.') < len(
                        x.text) - 1 and x.text.index('.') - x.text.index('@') > 1,
                    state=Register.Second)
async def first(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    data = await state.get_data()
    await message.answer(f'Ваш номер телефона: {data.get("phone")} \n Ваш адресс почты: {data.get("email")} \n Придумайте пароль:')
    await Register.Third.set()

@dp.message_handler(state=Register.Third)
async def first(message: types.Message, state: FSMContext):
    await message.answer('Спасибо за регистрацию!')
    await state.update_data(pin=message.text)
    #await bot.edit_message_text(text=len(message.text)*'*', message_id=message.message_id, chat_id=message.chat.id)
    await state.reset_state()

@dp.callback_query_handler(lambda x:
                           x.data == '1-2')
async def reg_start(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, text='Напиши камень, ножницы или бумага', reply_markup=menu)

@dp.message_handler(lambda x:
                    x.text in admin)
async def admin_start(message: types.Message):
    await message.answer('Добро пожаловать в админку!', reply_markup=admin_start)

@dp.callback_query_handler(lambda x:
                           x.data == '2-1')
async def admin_mailing(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, text='Рассылка скоро будет доступна')

@dp.callback_query_handler(lambda x:
                           x.data == '2-2')
async def admin_mailing(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, text='Эта функция скоро будет доступна')


@dp.message_handler(lambda msg:
                    msg.text in choices)
async def play(message: types.Message):
    text = random.choice(choices)
    await message.answer(text)




if __name__ == '__main__':
    executor.start_polling(dp)
