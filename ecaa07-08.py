from fastapi import FastAPI # cria o serviço de Rest API
import uvicorn
from fastapi.responses import JSONResponse # converte valores para JSON
import sqlite3 #biblioteca de sqlite3

# cria a aplicação rest api
app = FastAPI()

# domínio inicial da aplicação
@app.get('/')
def home():
  return f'Restfull API da ECAA07 Banco de Dados'

@app.get('/produtos')
def prod():
  conexao = sqlite3.connect('northwind.db')
  cursor = conexao.cursor()
  cursor.execute("SELECT * FROM Products")
  items = cursor.fetchall()
  conexao.close()
  return items

@app.get('/categorias/{item_id}')
def categ(item_id:int):
  conexao = sqlite3.connect('northwind.db')
  cursor = conexao.cursor()
  cursor.execute("SELECT CategoryName, Description FROM Categories WHERE CategoryID=?",(item_id,))
  items = cursor.fetchall()
  conexao.close()
  return items

@app.post('/fornecedores')
def forn(pais:str, token_api:str):
  if token_api != 'vaisefuder':
    return 'Token incorreto '
  conexao = sqlite3.connect('northwind.db')
  cursor = conexao.cursor()
  cursor.execute("SELECT * FROM Suppliers WHERE Country=?", (pais,))
  items = cursor.fetchall()
  conexao.close()
  return items

uvicorn.run(app, port=8000)