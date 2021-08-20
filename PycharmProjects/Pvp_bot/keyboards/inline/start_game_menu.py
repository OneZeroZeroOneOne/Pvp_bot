# --Choose game type menu--
from os import add_dll_directory
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import create_lobby_callback, tiktaktoe_callback

start_blackjack_menu = InlineKeyboardMarkup(
            inline_keyboard=
            [
                [
                    InlineKeyboardButton(text="Старт", callback_data=create_lobby_callback.new(
                        lobby_game_name="blackjack"
                    ))
                ],
                [
                    InlineKeyboardButton(text="Отмена", callback_data=create_lobby_callback.new(
                        lobby_game_name="blackjack"
                    )),
                ]
            ],
            resize_keyboard=True,
)

start_rcp_menu = InlineKeyboardMarkup(
            inline_keyboard=
            [
                [
                    InlineKeyboardButton(text="Старт", callback_data=create_lobby_callback.new(
                        lobby_game_name="rcp"
                    ))
                ],
                [
                    InlineKeyboardButton(text="Отмена", callback_data=create_lobby_callback.new(
                        lobby_game_name="rcp"
                    )),
                ]
            ],
            resize_keyboard=True,
)


def start_tiktaktoe(rates_id):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(InlineKeyboardButton(text="Старт", callback_data=tiktaktoe_callback.new(
                            rates_id=rates_id
            )))
    markup.add(InlineKeyboardButton(text="Отмена", callback_data=create_lobby_callback.new(
                            lobby_game_name="tiktaktoe"
                        )))
    return markup