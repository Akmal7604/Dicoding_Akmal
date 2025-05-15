from sqlalchemy import text, create_engine, select, Table, MetaData, update, delete
from main import DATABASE_URL

engine = create_engine(DATABASE_URL)
 
metadata= MetaData()
 
user_table = Table(
    "users",
    metadata,
    autoload_with=engine
)
 
# Menghapus data dengan id == 1
with engine.connect() as connection:
    try:
        delete_statement = delete(user_table).where(user_table.c.id ==1)
        result = connection.execute(delete_statement)
 
        connection.commit()
        print("Data berhasil dihapus!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
 
 
# Membaca data terbaru
with engine.connect() as connection:
    try:
        select_statement = select(user_table)
        result = connection.execute(select_statement)
 
        for row in result:
            print(row)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")