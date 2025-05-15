from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, insert

DATABASE_URL = "postgresql+psycopg2://akmal:Akmal7604@localhost:5432/dicodingdb"
engine = create_engine(DATABASE_URL)

# con = engine.connect()
# print("Terhubung dengan basis data!")
 
# # Menutup koneksi database
# con.close()
    
metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String),
    Column("last_name", String),
)

metadata.create_all(engine)

data_user = [
    {"first_name": "Evans", "last_name": "Sudarsono"},
    {"first_name": "John", "last_name": "Sutiyoso"},
    {"first_name": "Indah", "last_name": "Cahya"}
]

with engine.connect() as connection:
    try:
        print("Terhubung dengan basis data!")
        insert_statement = insert(user_table).values(data_user)
        connection.execute(insert_statement)
 
        connection.commit()
        print("Data berhasil ditambahkan!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")






    
    