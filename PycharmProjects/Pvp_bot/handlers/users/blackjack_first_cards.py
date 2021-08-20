from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.blackjack_menu import blackjack_menu
from keyboards.inline.callback_datas import lobby_ready_callback
from states.start_game import StartGame_State


@dp.callback_query_handler(lobby_ready_callback.filter(status="start"),
                           state=StartGame_State.game)
async def bot_blackjack_give_first_cards(call:CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Ожидаем когда соперник приймет игру.\n",
        parse_mode=types.ParseMode.HTML)
    await call.message.answer(
        f"Игра начинается!\n",
        parse_mode=types.ParseMode.HTML)
    await call.message.answer(
        f"Раздаём карты. Каждый игрок получил по 2 карты.\n"
        f"Выбирите, хотите ли вы взять ещё одну карту или остановиться.",
        parse_mode=types.ParseMode.HTML, reply_markup=blackjack_menu)
    await StartGame_State.game.set()