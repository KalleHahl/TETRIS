from src.database_connection import get_data_base_connection


def drop_tables(connection):
    """Deletes old table if it exists

    Args:
        connection: database connection
    """
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists scores;
    ''')

    connection.commit()


def create_tables(connection):
    """Creates sqlite table

    Args:
        connection: database connection
    """
    cursor = connection.cursor()

    cursor.execute('''
        create table scores (
            username text,
            score integer
        );
    ''')

    connection.commit()


def initialize_database():
    """Fucntion for initializing database
    """
    connection = get_data_base_connection()

    drop_tables(connection)

    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
