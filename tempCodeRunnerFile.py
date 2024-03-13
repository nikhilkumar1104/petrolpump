def view_all_Petrolpump_data():
    c.execute('SELECT * FROM Petrolpump')
    data = c.fetchall()
    return data