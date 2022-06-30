from conexao import ConexaoBanco

cone = ConexaoBanco()

cur = conn.cursor()

def selectProjetoJoinAtividades():
    select =    '''
        SELECT PROJETO.CODIGO, PROJETO.DESCRICAO, ATIVIDADE.DESCRICAO
        FROM PROJETO INNER JOIN ATIVIDADE     
        ON PROJETO.CODIGO = ATIVIDADE.CODPROJETO;
                '''

    cur.execute(select)
    
    cone.commit()

selectProjetoJoinAtividades()

cur.close()

cone.close()
