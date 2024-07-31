from codigos_tkinter import *
import BDD
import conexao as c

def fechar(func):
    """
    quando fechar uma janela, deve abrir outraa
    :param func: janela q deve abrir
    :return:
    """
    func()

def fbtn_login(user,senha,destroy):
    """

    :param user:usuario
    :param senha: senha
    :param destroy: destruir
    serve para criar a janela do depois do login
    :return:
    """
    try:
        c.login(user,senha,banco)
        main_jan(user,destroy)
    except Exception as e:
        criar_MB("Error",e,'cancel')

def fbtn_criar(nome,senha1,senha2,destroy):
    """

    :param nome: nome do usuario
    :param senha1: senha
    :param senha2: confirmar senha
    :param destroy: função de destruir a janela
    :return:
    """
    try:
        c.criar_user(nome,senha1,senha2,banco,destroy)
    except Exception as e:
        criar_MB("Error",e,'cancel')

def fbtn_criarU():
    """
    janela para criar o usuario
    :return: sem returno
    """
    jan=criar_jan("Criar Usuario",'285x265')
    l_user = criar_l(jan, "Nombre Usuario", 0, 0)
    tb_user = criar_tb(jan, 0, 1, 275)
    l_senha = criar_l(jan, "Senha", 0, 2 )
    tb_senha = criar_tb(jan, 0, 3, 275)
    tb_senha.configure(show="*")
    l_confsenha = criar_l(jan, "Confirmar Senha", 0, 4)
    tb_confsenha = criar_tb(jan, 0, 5, 275)
    tb_confsenha.configure(show="*")
    btn_criar=criar_btn(jan,"Crear",0,6,lambda :fbtn_criar(tb_user.get(),tb_senha.get(),
                                                             tb_confsenha.get(),jan.destroy),)
    jan.mainloop()
def login():
    """
    Criar a janela de login
    o btn login é para fazer login
    o btn criar u é para abrir a janela de criar usuario

    :return: sem returno
    """
    jan=criar_jan("Login","285x225")
    l_user=criar_l(jan,"Nombre Usuario",0,0)
    tb_user=criar_tb(jan,0,1,275)
    l_senha=criar_l(jan,"Senha",0,2)
    tb_senha=criar_tb(jan,0,3,275)
    tb_senha.configure(show="*")
    btn_login=criar_btn(jan,"Login",0,4,lambda :fbtn_login(tb_user.get(),tb_senha.get(),jan.destroy),100)
    btn_criarU=criar_btn(jan,"Criar User",0,5,lambda :fbtn_criarU(),100)
    jan.mainloop()

def fitemsd(destroy):
    """
    caso eu queira me desloguear
    :param destroy: janela pra destruir
    :return:
    """
    destroy()
    login()

def fbtn_criarC(nome,doc):
    """
    criar as clientes
    :param nome: nome do cliente
    :param doc: documentos do cliente
    :return:
    """
    try:
        c.criar_cliente(banco,nome,doc)
        criar_MB("Sucess", "Criado com sucesso", "check")
    except Exception as e:
        criar_MB("Error",e,"cancel")

def fitemcc(user,destroy):
    """
    janela de criar clientes
    :param user: usuario
    :param destroy: destruir
    :return:
    """
    destroy()
    jan=criar_jan("Criar Cliente")
    l_nome=criar_l(jan,'Nombre cliente',0,0)
    tb_nome=criar_tb(jan,1,0)
    l_doc=criar_l(jan,"Documento",0,1)
    tb_doc=criar_tb(jan,1,1)
    btn_criarc=criar_btn(jan,'Criar',1,2,lambda :fbtn_criarC(tb_nome.get(),tb_doc.get()))
    jan.protocol("WM_DELETE_WINDOW", lambda: main_jan(user,jan.destroy))
    jan.mainloop()

def fbtn_criarP(cod, detalhe, cliente, caja, data, valor, user):
    """
    criar movimento/pago
    :param cod: codigo da conta
    :param detalhe: detalhe do pago
    :param cliente:cod do cliente
    :param caja:de onde se moveu o dinheiro
    :param valor:valor da operação
    :param user:codigo
    :return:
    """
    try:
        cliente=cliente.split()[0]
        c.criar_movimento(cod,detalhe,cliente,caja,valor,user,data,banco)
        criar_MB("Suceseso","movimento criardo","check")
    except Exception as e:
        criar_MB("Erro",e,"cancel")

def fitemmc(user,destroy):
    """
    janela Serve para criar um movimento
    :param user: usario
    :param destroy: destruir janela anterior
    :return:
    """
    destroy()
    jan=criar_jan("Criar Movimiento")
    l_cod=criar_l(jan,"Cuenta",0,0)
    cb_cod=criar_cb(jan,c.get_cod(banco),1,0)
    l_cliente = criar_l(jan, 'Cliente', 0, 1)
    cb_cliente = criar_cb(jan, c.get_cliente(banco), 1, 1, 300)
    l_detalhe=criar_l(jan,"Detalle",0,2)
    tb_detalhe=criar_tb(jan,1,2)
    l_caja=criar_l(jan,"Caja",0,3)
    cb_caja=criar_cb(jan,c.get_cajas(banco,user),1,3)
    l_dia=criar_l(jan,"Data",0,4)
    caledario=criar_calendario(jan,1,4)
    l_valor=criar_l(jan,"Valor",0,5)
    tb_valor=criar_tb(jan,1,5)
    btn_criarP=criar_btn(jan,"pago",1,6,lambda :fbtn_criarP(cb_cod.get(),tb_detalhe.get(),cb_cliente.get(),cb_caja.get(),caledario.get_date(),tb_valor,user))
    jan.protocol("WM_DELETE_WINDOW", lambda :main_jan(user,jan.destroy))
    jan.mainloop()

def fbtn_criarClasse(classeM,detalle,classe):
    """
    criar uma classe/codigo oq classifica os movimentos entre entradas e saidas
    :param classeM:classe mae, caso exista
    :param detalle:detalhe da classe
    :return:
    """
    try:
        c.criar_classe(classeM,detalle, classe, banco)
        criar_MB("sucesso","criado con sucesso","check")
    except Exception as e:
        criar_MB("Erro",e,"cancel")

def fbtn_criarClas(user,classe,destroy):
    """
    janelas criar as classes de pagamento
    :param classe:
    :param destroy:
    :return:
    """
    destroy()
    lista_classe = ["Principal", "Secundaria", "Complemento"]
    jan = criar_jan(f"Nueva Classe {classe}")
    classe=lista_classe.index(classe)
    if classe!=0:

        l_classm=criar_l(jan,'Classe madre',0,0)
        classe -= 1
        cb_class=criar_cb(jan,c.get_conta_m(banco,classe),1,0)
        classe+=1
        l_class=criar_l(jan,"detalle de la classe",0,1)
        tb_class=criar_tb(jan,1,1)
        btn_criarClasse=criar_btn(jan,"crear",1,2,lambda :fbtn_criarClasse(cb_class.get(),tb_class.get(),classe))
    else:
        l_class = criar_l(jan, "detalle de la classe", 0, 1)
        tb_class = criar_tb(jan, 1, 1)
        btn_criarClasse = criar_btn(jan, "crear", 1, 2,lambda :fbtn_criarClasse("0",tb_class.get(),classe))
    jan.protocol("WM_DELETE_WINDOW", lambda: fechar(lambda :fitemcuc(user, jan.destroy)))
    jan.mainloop()




def fitemcuc(user,destroy):
    """
    selecionar qual é a classe mae do novo codigo
    :param destroy: destruit janela anterior
    :return:
    """
    destroy()
    lista_classe=["Principal","Secundaria","Complemento"]
    jan=criar_jan('Tipo de Cuenta')
    l_class=criar_l(jan,"Classe",0,0)
    cb_class=criar_cb(jan,lista_classe,1,0)
    btn_criarClas=criar_btn(jan,"Selecionar",1,1,lambda :fbtn_criarClas(user,cb_class.get(),jan.destroy))
    jan.protocol("WM_DELETE_WINDOW", lambda: main_jan(user, jan.destroy))
    jan.mainloop()

def fbtn_criarCj(user,nome,valor):
    """

    :param user: usuario
    :param nome: nome
    :param valor: valor inicial del caja
    :return:
    """
    try:
        c.criar_caja(banco,user,nome,valor)
        criar_MB("Sucesso","Caja creado","check")
    except Exception as e:
        criar_MB("Erro",e,"cancel")

def fitemcac(user,destroy):
    """
    criar uma caja/conta bancaria e similares
    :param user: usuario
    :param destroy: destruir janela anterior
    :return:
    """
    destroy()
    jan=criar_jan("Adicionar Caja")
    l_nome=criar_l(jan,"Nombre del caja",0,0)
    tb_nome=criar_tb(jan,1,0)
    l_saldoi=criar_l(jan,"saldo inicial",0,1)
    tb_valor=criar_tb(jan,1,1)
    btn_criarCj=criar_btn(jan,"Adicionar",1,2,lambda : fbtn_criarCj(user,tb_nome.get(),tb_valor.get()))
    jan.protocol("WM_DELETE_WINDOW", lambda: main_jan(user, jan.destroy))
    jan.mainloop()

def main_jan(user,destroy):

    """
    :param user: usuario
    janela principal
    :return:
    """

    jan=criar_jan(f"{user}, Area Principal")
    destroy()
    menu=criar_menu(jan)

    itemm = item_menu(menu,"movimentos")
    itemc = item_menu(menu, "clientes")
    itemcu = item_menu(menu, "cuentas")
    itemca = item_menu(menu, "caja")
    itemi = item_menu(menu, "imprimir")
    items = item_menu(menu, "sair")

    itemmc = item_menu_comands(itemm,'criar',lambda :fitemmc(user,jan.destroy))
    itemmm = item_menu_comands(itemm, 'modificar', lambda: print('modificar'))
    itemme = item_menu_comands(itemm, 'excluir', lambda: print('excluir'))

    itemcc = item_menu_comands(itemc, 'criar', lambda: fitemcc(user,jan.destroy))
    itemcm = item_menu_comands(itemc, 'modificar', lambda: print('modificar'))
    itemce = item_menu_comands(itemc, 'excluir', lambda: print('excluir'))

    itemcuc = item_menu_comands(itemcu, 'criar', lambda: fitemcuc(user,jan.destroy))
    itemcum = item_menu_comands(itemcu, 'modificar', lambda: print('modificar'))
    itemcue = item_menu_comands(itemcu, 'excluir', lambda: print('excluir'))

    itemcac = item_menu_comands(itemca, 'criar', lambda: fitemcac(user,jan.destroy))
    itemcam = item_menu_comands(itemca, 'modificar', lambda: print('modificar'))
    itemcae = item_menu_comands(itemca, 'excluir', lambda: print('excluir'))

    itemim = item_menu_comands(itemi, 'por mes', lambda: print('mes'))
    itemic = item_menu_comands(itemi, 'por conta', lambda: print('conta'))
    itemil = item_menu_comands(itemi, 'por cliente', lambda: print('cliente'))

    itemsd = item_menu_comands(items, 'deslogar', lambda: fitemsd(jan.destroy))
    itemss = item_menu_comands(items, 'sair', lambda: jan.destroy())

    jan.mainloop()



global banco
banco=BDD.bdd()
login()