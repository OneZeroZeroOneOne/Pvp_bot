from utils.db_api.close_connection import close_connection
from utils.db_api.create_connection import db_connection
from utils.db_api.execute_query import execute_query

query = """

CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    name varchar(255) NULL,
    username varchar(255)
);

CREATE TABLE IF NOT EXISTS deposits(
    id SERIAL PRIMARY KEY,
    user_id int,
    balance integer DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS rates(
    id SERIAL PRIMARY KEY,
    value INTEGER
);

CREATE TABLE IF NOT EXISTS blackjack_lobby(
    user_id BIGINT,
    rates_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (rates_id) REFERENCES rates(id)
);

CREATE TABLE IF NOT EXISTS blackjack_game(
    id SERIAL PRIMARY KEY,
    rates_id INTEGER,
    user_step_id INTEGER,
    game_round INTEGER DEFAULT 1,
    is_end varchar(5) NULL,
    FOREIGN KEY (rates_id) REFERENCES rates(id),
    FOREIGN KEY (user_step_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS blackjack_game_user(
    user_id INTEGER,
    game_id INTEGER,
    hand varchar(255) NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (game_id) REFERENCES blackjack_game(id)
);

CREATE TABLE IF NOT EXISTS blackjack_game_dealer(
    game_id int,
    deck varchar(255) NULL,
    hand varchar(255) NULL,
    FOREIGN KEY (game_id) REFERENCES blackjack_game(id)
);

"""


def create_tables_if_not_exists():
    connection = db_connection()
    try:
        execute_query(connection, query)
        print("База данных успешно создана")
    except:
        print("Ошибка при создании базы")
    close_connection(connection)
