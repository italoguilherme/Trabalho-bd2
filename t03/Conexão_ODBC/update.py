from conexao import ConexaoBanco

cone = ConexaoBanco()

cur = cone.cursor()

def AtualizarResponsavelProjeto(codProjeto, novoResponsavel):
    update =    '''
        UPDATE projeto SET codresponsavel = %s
        WHERE codigo = %s;
                '''
    value = (novoResponsavel, codProjeto)
    
    cur.execute(update,value)
    
    cone.commit()

AtualizarResponsavelProjeto(codProjeto=2, novoResponsavel=4)

cur.close()

cone.close()
