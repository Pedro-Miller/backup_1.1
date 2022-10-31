import sqlite3
from flask import Flask, render_template, request, flash

existe = bool

#cria tabela caso nao exista
def cria_tabela() :
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contas ([nome] TEXT NOT NULL,[dre] TEXT PRIMARY KEY,[senha] TEXT NOT NULL);
    ''')

    db.commit()

class aluno():
    def __init__(self, nome, dre, senha):
        self.nome = nome
        self.dre = dre
        self.senha = senha



def checa_existe(dre) :
        db = sqlite3.connect('database.sqlite')
        cursor = db.cursor()
        cadastro = cursor.execute("SELECT * FROM contas where dre = '"+dre+"'").fetchall()
        if len(cadastro)>0 :
                return True
        else:
                
                return False       

#checa se ja existe e se nao existir ele cria
def cadastrar(nome, dre, senha):
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()
    if checa_existe(dre) == False:
        cursor.execute("INSERT INTO contas VALUES ('"+nome+"','"+dre+"','"+senha+"')")
        db.commit()
        return render_template("sucesso.html")
    else:
        flash("DRE ja cadastrado, prossiga para: ")
        return render_template("cadastro.html")



def autentica(dre, senha):
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()
    cadastro_valido = cursor.execute("SELECT * FROM contas where dre = '"+dre+"' and senha = '"+senha+"'").fetchall()
    if len(cadastro_valido) >0:
        return True
    else:
        return False


def login(dre,senha):
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()
    if autentica(dre, senha) == True:
        global logado
        logado = True
        return render_template("base.html")
    else:
        flash("DRE nao cadastrado, prossiga para: ")
        return render_template("cadastro.html")


global user 
user = aluno("","","")



