import mysql.connector


class Connection:
    conn = mysql.connector.connect(
        host='',
        user='',
        passwd='',
        database=''
    )
    c = conn.cursor(buffered=True)

    def get_notes(self):
        output = ""
        self.c.execute("SELECT note1, note2, note3, priority1, priority2, priority3 FROM mirror_notes")
        self.conn.commit()
        result = self.c.fetchall()
        return result
        c.close()


