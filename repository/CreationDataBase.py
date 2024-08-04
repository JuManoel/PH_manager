import sqlite3  # banco de dados

class CreationDataBase:

    def __init__(self):
        self.banco = sqlite3.Connection("cuentas_de_cobro.db")
        self.cursor = self.banco.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS PropriedadHorizontal"
                            "(Id INTEGER PRIMARY KEY,"
                            "nombre TEXT NOT NULL UNIQUE,"
                            "senha TEXT NOT NULL,"
                            "direccion TEXT NOT NULL);")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Proprietario"
                            "(Id INTEGER PRIMARY KEY,"
                            "cedula TEXT NOT NULL UNIQUE,"
                            "nombre TEXT NOT NULL,"
                            "direccion TEXT NOT NULL,"
                            "propriedadHorizontal INTEGER NOT NULL,"
                            "activa BOOLEAN NOT NULL CHECK (activa IN (0, 1)),"
                            "FOREIGN KEY (propriedadHorizontal) REFERENCES PropriedadHorizontal (Id));")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS CuentaPorCobrar"
                            "(Id INTEGER PRIMARY KEY,"
                            "valor REAL NOT NULL,"
                            "propriedadHorizontal INTEGER NOT NULL,"
                            "devedor INTEGER NOT NULL,"
                            "detalle TEXT,"
                            "periodo TEXT NOT NULL,"
                            "saldo REAL NOT NULL,"
                            "activa BOOLEAN NOT NULL CHECK (activa IN (0, 1)),"
                            "is_extra BOOLEAN NOT NULL CHECK (is_extra IN (0, 1)),"
                            "FOREIGN KEY (devedor) REFERENCES Proprietario (Id),"
                            "FOREIGN KEY (propriedadHorizontal) REFERENCES PropriedadHorizontal (Id));")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Pago"
                            "(Id INTEGER PRIMARY KEY,"
                            "valor REAL NOT NULL,"
                            "cuentaPorCobrar INTEGER NOT NULL,"
                            "fecha TEXT NOT NULL,"
                            "activa BOOLEAN NOT NULL CHECK (activa IN (0, 1)),"
                            "FOREIGN KEY (cuentaPorCobrar) REFERENCES CuentaPorCobrar (Id));")
        self.banco.commit()

    def insert(self, table, col, val):
        try:
            sql = f"INSERT INTO {table}({col}) VALUES ({val});"
            self.cursor.execute(sql)
            self.banco.commit()
        except:
            assert False, sql

    def select(self, col, table, extr=""):
        try:
            sql = f"SELECT {col} FROM {table} {extr}"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            dados = []
            if "," in col or col == "*":
                return result
            for i in result:
                for j in i:
                    dados.append(j)
            return dados
        except:
            assert False, {sql}

    def deleteRow(self, table, cond=""):
        try:
            sql = f"DELET FROM {table} WHERE {cond};"
            self.cursor.execute(sql)
            self.banco.commit()
        except:
            assert False, sql

    def update(self, table, col_val, cond):
        try:
            sql = f"UPDATE {table} SET {col_val} WHERE {cond}"
            self.cursor.execute(sql)
            self.banco.commit()
        except:
            assert False, sql
    def deleteDesactiva(self, table,id):
        self.update(table,"activa = 0",f"Id = {id}")