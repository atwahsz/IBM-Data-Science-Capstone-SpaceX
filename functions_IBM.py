# function to read from database
def read(conn, read_):
    print('Read')
    cursor = conn.cursor()
    cursor.execute(read_)
    for row in cursor:
        print(f'row = {row}')
    print()
    
# function to create in postgre database     
def create(conn, create_):
    cursor = conn.cursor() # create cursor object
    cursor.execute(create_) # execute query
    conn.commit() # commit query to database
    print('Table have been created successfull!!!')
    #read(conn)
    
# function to insert in postgre database     
def insert(conn, insert_):
    cursor = conn.cursor()
    cursor.execute(insert_)
    conn.commit()
    print('Records have been successfully inserted!!!')
    #read(conn)
    
# function to update table
def update(conn, update_):
    print('Update')
    cursor = conn.cursor()
    cursor.execute(update_)
    conn.commit()
    #read(conn)
    
# function to delete in postgre database
def delete(conn, delete_):
    print('Delete')
    cursor = conn.cursor()
    cursor.execute(delete_)
    conn.commit()
    #read(conn)

# close the cursor and connection to the server 
def close():
    cursor.close()
    conn.close()   
    
# function to create pandas dataframe
def create_pandas_df(sql_query, database=conn):
    table = pd.read_sql_query(sql_query, database)
    return table