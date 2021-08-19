from psycopg2._psycopg import cursor

from utils.db_api.close_connection import close_connection
from utils.db_api.create_connection import db_connection
from utils.db_api.execute_query import execute_query, fetchall_query, print_query, fetchone_query


def find_empty_room_for_blackjack(user):
    find_empty_room_to_connect_query = f"""
    SELECT bj.*, room.* FROM blackjacks as bj 
    LEFT JOIN rooms as room on bj.room_id=room.id
    WHERE room.player_two IS NULL
    ORDER BY room.id ASC LIMIT 1
    """

    create_empty_room_query = f"""
        WITH room AS (
        INSERT INTO rooms(player_one) VALUES ({user.id})
        RETURNING id
        )
        INSERT INTO blackjacks(room_id) VALUES ((SELECT id FROM room))
    """

    get_room_number_query = f"""
    SELECT id from rooms WHERE player_one = {user.id} AND room_state = 'WAITING'
    """

    connection = db_connection()
    try:
        empty_room = None
        connect_to_the_empty_room_query = None
        room_number = None
        try:
            empty_room = fetchone_query(connection, find_empty_room_to_connect_query)
            connect_to_the_empty_room_query = f"UPDATE rooms SET player_two = {user.id} WHERE rooms.id = {empty_room[8]}"
            room_number = [empty_room[8]]
        except:
            pass
        if empty_room == None:
            # Создаём свободную комнату для подключения
            execute_query(connection, create_empty_room_query)
            room_number = fetchone_query(connection, get_room_number_query)
            print("Созданна новая комната для блекджека")
        else:
            # Подключаем к первой свободной комнате
            execute_query(connection, connect_to_the_empty_room_query)
            print("Пользователь подключён к комнате для белжека")

    except:
        print("Ошибка в поиске комнаты для блекджека")
    close_connection(connection)
    return room_number