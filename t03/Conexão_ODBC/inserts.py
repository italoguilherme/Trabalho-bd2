from datetime import date
from conexao import ConexaoBanco

cone = ConexaoBanco()

cur = cone.cursor()

def CreateAtividade(codProjeto, dataFim, dataInicio, descricao):
    insert = '''
        INSERT INTO atividade(codprojeto, datafim, datainicio, descricao) 
        VALUES (%s, %s, %s, %s);
    '''
    value = (codProjeto, dataFim, dataInicio, descricao)
    
    cur.execute(insert, value)
    
    cone.commit()


CreateAtividade(
    codProjeto = 4,
    dataFim=date(2022, 6,30), 
    dataInicio = date(2022,6,19), 
    descricao="Tarefa 3",
)

cur.close()

cone.close()
