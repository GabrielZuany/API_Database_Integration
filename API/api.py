from fastapi import FastAPI
from sqlalchemy import create_engine, text
import MySQLdb
import pandas as pd
import pymysql

host = "localhost"
dbname = "banco"
user = "root"
password = "#include<Gzdv_24052002>"

api = FastAPI()
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{dbname}")
    
@api.get("/") 
def home():
    return "API Online"

@api.get("/pedidos")
def get_pedidos():
    query = '''
    SELECT 
	    pedidos.*,
        lojas.Loja
    FROM pedidos
        LEFT JOIN lojas
	        ON pedidos.ID_Loja = lojas.ID_Loja;
    '''
    
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json() 

@api.get("/pedidos/{id_pedido}")
def get_pedido_por_id(id_pedido:int):
    query = f'SELECT * FROM pedidos WHERE ID_Pedido = {id_pedido}'
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json()

@api.get("/produtos")
def get_produtos():
    query = 'SELECT * FROM produtos'
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json()

@api.get("/produtos/{id}")
def get_produto_por_id(id:int):
    query = f'SELECT * FROM produtos WHERE ID_Produto = {id}'
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json()

@api.get("/lojas")
def get_lojas():
    query = 'SELECT * FROM lojas'
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json()

@api.get("/lojas/{id}")
def get_lojas_por_id(id:int):
    query = f'SELECT * FROM lojas WHERE ID_Loja = {id}'
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json()

@api.get("/clientes")
def get_clientes():
    query = 'SELECT * FROM clientes'
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json()

@api.get("/clientes/{id}")
def get_clientes_por_id(id:int):
    query = f'SELECT * FROM clientes WHERE ID_Cliente = {id}'
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json()

@api.get("/locais")
def get_locais():
    query = 'SELECT * FROM locais'
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json()

@api.get("/locais/{UF}")
def get_locais_por_UF(UF:str):
    query = f'SELECT * FROM locais WHERE Estado = "{UF}"'
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json()

@api.get("/categorias")
def get_categorias():
    query = 'SELECT * FROM categorias'
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json()

@api.get("/categorias/{id}")
def get_categorias_por_id(id:int):
    query = f'SELECT * FROM categorias WHERE ID_Categoria = {id}'
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json() 

@api.get("/relatorio_vendas/produtos")
def get_df_relatorio_vendas_produto():
    query = "SELECT pedidos.ID_Produto, pedidos.Qtd_Vendida, pedidos.Preco_Unit, pedidos.Custo_Unit, produtos.Nome_Produto, produtos.Marca_Produto FROM pedidos INNER JOIN  produtos ON pedidos.ID_Produto = produtos.ID_Produto;"
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json()

@api.get("/relatorio_vendas/lojas")
def get_df_relatorio_vendas_loja():
    query = "SELECT pedidos.ID_Loja, pedidos.Qtd_Vendida, pedidos.Preco_Unit, pedidos.Custo_Unit, lojas.Loja FROM pedidos INNER JOIN  lojas ON pedidos.ID_Loja = lojas.ID_Loja;"
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json()
 
@api.get("/relatorio_vendas/clientes")
def get_df_relatorio_vendas_clientes():
    query = "SELECT pedidos.ID_Cliente, pedidos.Qtd_Vendida, pedidos.Receita_Venda, clientes.Nome, clientes.Sobrenome FROM pedidos INNER JOIN  clientes ON pedidos.ID_Cliente = clientes.ID_Cliente;"
    df =  pd.DataFrame(engine.connect().execute(text(query)))
    return df.to_json()

