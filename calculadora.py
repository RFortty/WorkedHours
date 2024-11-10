# Instalar biblioteca TKInter: pip install tkinter
# Instalar biblioteca Custom TKInter: pip install customtkinter
# Instalar biblioteca Pillow: pip install pillow
# Instalar biblioteca para PDF: pip install reportlab

import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from datetime import date, datetime

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm


### C o r e s ###

cor0 = "#2e2d2b" # Preto
cor1 = "#feffff" # Branco
cor2 = "#4fa882" # Verde
cor3 = "#38576b" # Valor
cor4 = "#403d3d" # Letra
cor5 = "#ed5636" # Profit
cor6 = "#034cfc" # Azul escuro
cor7 = "#3fbfb9" # Verde
cor8 = "#263238" # Azul marinho
cor9 = "#e9edf5" # Verde

#janela = customtkinter.CTk()

### J a n e l a  P r i n c i p a l ###

janela = Tk()
janela.title(". : W o r k e d  H o u r s : .")
janela.geometry('500x550+350+80') # ('width x height + X coordinate + Y coordinate')
janela.configure(background = cor1)
janela.resizable(width=FALSE, height=FALSE)
#janela.iconify() # roda o app minimizado
#janela.deiconify()

estilo = ttk.Style(janela)
estilo.theme_use("clam")

### J a n e l a  d e  T í t u l o (Cabeçalho)

frame_top = Frame(janela, width=1043, height=40, pady=5, bg=cor6)
frame_top.grid(row=0, column=0)

app_logo_img = Image.open('images/salary_hand.png')
app_logo_img = app_logo_img.resize((32,32))
app_logo_img = ImageTk.PhotoImage(app_logo_img)

app_logo = Label(frame_top, 
                 image=app_logo_img,
                 text='Calculadora de Salário', 
                 compound=LEFT, 
                 relief=RAISED, 
                 anchor=NW,
                 font=('Verdana 15'),
                 bg=cor1,
                 fg=cor4)
app_logo.place(x=110, y=0)


# Janela Dados do Usuário

frame_down = Frame(janela, width=1043, height=185, pady=0, bg=cor1)
frame_down.grid(row=1, column=0)

# Exibir Abas no Frame
abas = ttk.Notebook(frame_down)
aba1 = Frame(abas)
aba2 = Frame(abas)
aba3 = Frame(abas)

aba1.configure(background=cor1)
aba2.configure(background=cor1)
aba3.configure(background=cor1)

abas.add(aba1, text="Dados")
abas.add(aba2, text="Adicionais")
abas.add(aba3, text="Horas")
abas.forget(aba3) # Oculta a Aba 3

abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)


# Função para criar máscara para campo data
def on_entry_change(event):
    # Obtem o valor atual do campo de entrada
    text = edt_adm.get()
    # Remove todos os caracteres que não são números
    text = ''.join(filter(str.isdigit, text))

    # Permite apagar o texto se aplicar a máscara novamente
    if not text:
        edt_adm.delete(0, tk.END)
        return

    # Verifica e ajusta o valor do dia se necessário
    if len(text) >= 2:
        day = int(text[:2])
        if day < 1:
            day = "01" # Ajusta para o mínimo
        elif day > 31:
            day = "31" # Ajusta para o máximo
        else:
            day = f"{day:02}" # Mantem no formato de dois dígitos
        text = day + text[2:]
    
    # Verifica e ajusta o valor do mês se necessário
    if len(text) >= 4:
        month = int(text[2:4])
        if month < 1:
            month = "01" # Ajusta para o mínimo
        elif month > 12:
            month = "12" # Ajusta para o máximo
        else:
            month = f"{month:02}" # Mantem no formato de dois dígitos
        text = text[:2] + month + text[4:]

    # Adiciona a máscara de data
    masked_text = ""

    if len(text) > 0:
        masked_text += text[:2]

    if len(text) >= 3:
        masked_text += "/" + text[2:4]
        
    if len(text) >= 5:
        masked_text += "/" + text[4:8]
    
    # Atualiza o campo de entrada com a máscara aplicada
    edt_adm.delete(0, tk.END)
    edt_adm.insert(0, masked_text)
    edt_adm.icursor(len(masked_text)) # Mantém o cursor na posição correta


# Função para validar a Entry Salario
def validate_input(text):
    #Permite somente números e ponto
    return text == "" or text.replace(".", "", 1).isdigit()

vcmd = (janela.register(validate_input), '%P')

# Função para validar a Entry Nome
def validate_name(text):
    # Verifica se o caracter é uma letra maiúsula ou vazio
    if text.isupper() or text == "":
        return True
    return False

# Cria a validação        
vcmd2 = (janela.register(validate_name), '%S') # a opção %S passa o valor digitado


def converter_maiusculas(event):
    # Pega o texto atual da Entry e converte para maiúscula
    texto = edt_nome.get().upper()
    # Atualiza o campo de entrada com o texto em maiúsculo
    edt_nome.delete(0, tk.END)
    edt_nome.insert(0, texto)

def limitar_tamanho(text):
    if len(text) > 2:
        return False
    return True
# Registrando a função que faz a validação.
vcmd3 = janela.register(func=limitar_tamanho)


# ABA Dados

lbl_nome = Label(aba1,#frame_down, 
                 text='Nome Completo:', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_nome.place(x=10, y=10)

edt_nome = Entry(aba1,#frame_down,
                 width=46, 
                 font=('Ivy 10 bold italic'),
                 justify='left', # posição do texto
                 relief='groove', # estilo da Entry (flat, raised, sunken, groove, ridge)
                 bg='cyan', # cor do fundo
                 highlightbackground='black', # cor da borda
                 border= 3, # espessura da borda
                 fg='red')# cor do texto
                 #validate="key", validatecommand=vcmd2) 
edt_nome.place(x=112, y=11)
edt_nome.bind("<KeyRelease>", converter_maiusculas)
edt_nome.focus()


lbl_adm = Label(aba1,#frame_down, 
                 text='Data Admissão:', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_adm.place(x=10, y=45)
edt_adm = Entry(aba1, width=10, justify='left', relief='groove')
edt_adm.place(x=112, y=45)
edt_adm.bind("<KeyRelease>", on_entry_change)

lbl_depend = Label(aba1,#frame_down, 
                 text='nº Dependentes:', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_depend.place(x=230, y=45)
edt_depend = Entry(aba1, width=5, justify='left', relief='groove', validate='key', validatecommand=(vcmd3, '%P'))
edt_depend.place(x=340, y=45)

lbl_sal = Label(aba1,#frame_down, 
                 text='Salário Base: R$', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_sal.place(x=10, y=80)
edt_sal = Entry(aba1, width=15, justify='left', relief='groove', validate="key", validatecommand=vcmd)
edt_sal.place(x=112, y=80)

lbl_cesta = Label(aba1,#frame_down, 
                 text='Cesta Básica: R$', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_cesta.place(x=230, y=80)
edt_cesta = Entry(aba1, width=15, justify='left', relief='groove', validate="key", validatecommand=vcmd)
edt_cesta.place(x=340, y=80)
edt_cesta.insert(0, "0")


# Cálculo de Horas Trabalhadas

# total dias por ano
ano = 365
# total semanas por ano
semanas = 52
# total horas trabalhadas por dia
total_horas_dia = 8
# total dias de trabalho
total_dias_trab = 5
#Calculando Total de Horas trabalhadas Semanal
total_horas_sem = total_horas_dia * total_dias_trab
#Calculando Total de Horas trabalhadas Mensal
total_horas_mes = total_horas_sem * 5 #(semanas por mês)
#Calculando Total de Horas trabalhadas Anual
total_horas_ano = semanas * total_horas_sem


lbl_horas_trab = Label(aba1, #frame_down, 
                 text='Horas Trabalhadas/dia:', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_horas_trab.place(x=10, y=110)
edt_horas_trab = Entry(aba1, width=5, justify='center', relief='groove', bg='cyan', fg='darkblue')
edt_horas_trab.place(x=60, y=130)
edt_horas_trab.insert(END, total_horas_dia)

lbl_dias_trab = Label(aba1,#frame_down, 
                 text='Dias Trabalhados/semana:', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_dias_trab.place(x=160, y=110)
edt_dias_trab = Entry(aba1, width=5, justify='center', relief='groove', bg='cyan', fg='darkblue')
edt_dias_trab.place(x=220, y=130)
edt_dias_trab.insert(END, total_dias_trab)

lbl_mes_trab = Label(aba1,#frame_down, 
                 text='Dias Trabalhados/mês:', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_mes_trab.place(x=340, y=110)
edt_mes_trab = Entry(aba1, width=5, justify='center', relief='groove', bg='cyan', fg='darkblue')
edt_mes_trab.place(x=380, y=130)
edt_mes_trab.insert(END, total_horas_mes)

# Final da ABA Dados

# ABA Adicionais

auxdoença = IntVar()
pericul = IntVar()
insalub = IntVar()
valetransp = IntVar()
valeref = IntVar()
salfamilia = IntVar()
funcgratif = IntVar()
decterc = IntVar()
ferias = IntVar()
adnoturno = IntVar()

# Função que exibe as Entry 
def on_button_toggle():

    if valetransp.get() == 1:
        edt_valetransp.place(x=185, y=96)
        edt_valetransp.focus()
    else:
        edt_valetransp.delete(0, END) # Limpar o Entry
        edt_valetransp.place_forget()

    if valeref.get() == 1:
        edt_valeref.place(x=174, y=124)
        edt_valeref.focus()
    else:
        edt_valeref.delete(0, END) # Limpar o Entry
        edt_valeref.place_forget()
    
    if decterc.get() == 1:
        edt_decterc.place(x=388, y=42)
        edt_decterc.focus()
    else:
        edt_decterc.place_forget()

    if funcgratif.get() == 1:
        edt_gratif.place(x=394, y=96)
        edt_gratif.focus()
    else:
        edt_gratif.place_forget()
    
    if adnoturno.get() == 1:
        edt_adnoturno.place(x=426, y=124)
        edt_adnoturno.focus()
    else:
        edt_adnoturno.place_forget()


chb_auxdoença = Checkbutton(aba2,
                  text='Auxílio Doença',
                  variable=auxdoença,
                  bg=cor1,
                  fg='black',
                  font=("Arial", 10),
                  relief='groove',
                  #selectcolor='green',
                    onvalue=1,
                    offvalue=0,
                    command=on_button_toggle)
chb_auxdoença.place(x=40, y=10)

chb_pericul = Checkbutton(aba2,
                  text='Periculosidade',
                  variable=pericul,
                  bg=cor1,
                  fg='black',
                  font=("Arial", 10),
                  relief='groove',
                  #selectcolor='green',
                    onvalue=1,
                    offvalue=0,
                    command=on_button_toggle)
chb_pericul.place(x=40, y=38)

chb_insalub = Checkbutton(aba2,
                  text='Insalubridade',
                  variable=insalub,
                  bg=cor1,
                  fg='black',
                  font=("Arial", 10),
                  relief='groove',
                  #selectcolor='green',
                    onvalue=1,
                    offvalue=0,
                    command=on_button_toggle)
chb_insalub.place(x=40, y=65)

chb_valetransp = Checkbutton(aba2,
                  text='Vale Transporte R$:',
                  variable=valetransp,
                  bg=cor1,
                  fg='black',
                  font=("Arial", 10),
                  relief='groove',
                  #selectcolor='green',
                    onvalue=1,
                    offvalue=0,
                    command=on_button_toggle)
chb_valetransp.place(x=40, y=92)

edt_valetransp = Entry(aba2, width=10, justify='left', relief='raised', fg='purple', bg='cyan', validate="key", validatecommand=vcmd)


chb_valeref = Checkbutton(aba2,
                  text='Vale Refeição R$:',
                  variable=valeref,
                  bg=cor1,
                  fg='black',
                  font=("Arial", 10),
                  relief='groove',
                  #selectcolor='green',
                    onvalue=1,
                    offvalue=0,
                    command=on_button_toggle)
chb_valeref.place(x=40, y=120)

edt_valeref = Entry(aba2, width=10, justify='left', relief='raised', fg='purple', bg='cyan', validate="key", validatecommand=vcmd)


chb_ferias = Checkbutton(aba2,
                  text='Férias',
                  variable=ferias,
                  bg=cor1,
                  fg='black',
                  font=("Arial", 10),
                  relief='groove',
                  #selectcolor='green',
                    onvalue=1,
                    offvalue=0,
                    command=on_button_toggle)
chb_ferias.place(x=270, y=10)

chb_decterc = Checkbutton(aba2,
                  text='13º Salário R$:',
                  variable=decterc,
                  bg=cor1,
                  fg='black',
                  font=("Arial", 10),
                  relief='groove',
                  #selectcolor='green',
                    onvalue=1,
                    offvalue=0,
                    command=on_button_toggle)
chb_decterc.place(x=270, y=38)

edt_decterc = Entry(aba2, width=10, justify='left', relief='raised', fg='purple', bg='cyan', validate="key", validatecommand=vcmd)

chb_salfamilia = Checkbutton(aba2,
                  text='Salário Família',
                  variable=salfamilia,
                  bg=cor1,
                  fg='black',
                  font=("Arial", 10),
                  relief='groove',
                  #selectcolor='green',
                    onvalue=1,
                    offvalue=0,
                    command=on_button_toggle)
chb_salfamilia.place(x=270, y=65)

chb_funcgratif = Checkbutton(aba2,
                  text='Gratificação R$:',
                  variable=funcgratif,
                  bg=cor1,
                  fg='black',
                  font=("Arial", 10),
                  relief='groove',
                  #selectcolor='green',
                    onvalue=1,
                    offvalue=0,
                    command=on_button_toggle)
chb_funcgratif.place(x=270, y=92)

edt_gratif = Entry(aba2, width=10, justify='left', relief='raised', fg='purple', bg='cyan', validate="key", validatecommand=vcmd)


chb_adnoturno = Checkbutton(aba2,
                  text='Adicional Noturno R$:',
                  variable=adnoturno,
                  bg=cor1,
                  fg='black',
                  font=("Arial", 10),
                  relief='groove',
                  #selectcolor='green',
                    onvalue=1,
                    offvalue=0,
                    command=on_button_toggle)
chb_adnoturno.place(x=270, y=120)

edt_adnoturno = Entry(aba2, width=10, justify='left', relief='raised', fg='purple', bg='cyan', validate="key", validatecommand=vcmd)


# Final ABA Adicionais

# Frame Descontos e Vencimentos
frame_calc = Frame(janela, width=1043, height=280, pady=0, bg='lightgray')
frame_calc.grid(row=2, column=0)

# Botão Calcular
app_btn_img = Image.open('images/calculator.png')
app_btn_img = app_btn_img.resize((25,25))
app_btn_img = ImageTk.PhotoImage(app_btn_img)

frame_venc = Frame(janela, width=240, height=230, pady=0, bg='cyan')
frame_venc.grid(row=2, column=0)
frame_venc.place(x=5, y=270)

frame_desc = Frame(janela, width=240, height=230, pady=0, bg='cyan')
frame_desc.grid(row=2, column=0)
frame_desc.place(x=255, y=270)

logo_tbruto = Image.open('images/coins.png')
logo_tbruto = logo_tbruto.resize((22,22))
logo_tbruto = ImageTk.PhotoImage(logo_tbruto)

logo_tdesc = Image.open('images/coins.png')
logo_tdesc = logo_tdesc.resize((22,22))
logo_tdesc = ImageTk.PhotoImage(logo_tdesc)

logo_total = Image.open('images/bag_cash.png')
logo_total = logo_total.resize((32,32))
logo_total = ImageTk.PhotoImage(logo_total)


# # # Função C Á L C U L A R : # # #

def Calcular():
    #pass
    
    nome = edt_nome.get()    
    admissao = edt_adm.get()
    edt_mes_trab.delete(0, END)
    total_horas_mes = (int(edt_horas_trab.get()) * int(edt_dias_trab.get())) * 5 
    edt_mes_trab.insert(END, total_horas_mes)
    '''
    while True:
        try:
            admissao = edt_adm.get()
        except:
            messagebox.showinfo("showinfo", "Information: Data Inválida !")
    '''
    sal_base = float(edt_sal.get())
    aux_doença = (sal_base + (sal_base * 0.07)) * (91/100)
    #sal_base = aux_doença
    cesta_basica = float(edt_cesta.get())

    data_hoje = datetime.today()
    data_hoje_formatada = data_hoje.strftime('%d/%m/%Y') # Converte Data em String
    data_adm = datetime.strptime(admissao, '%d/%m/%Y') # Converte String em Data
    data_dif = data_hoje - data_adm


    if auxdoença.get() == 1:
        sal_base = aux_doença
        #messagebox.showinfo(title="Result", message=f'{sal_base} = Checado!')


    quinquenio = (data_dif.days // ano) // 5

    # Cálculo do Quinquenio
    if quinquenio == 0:
        total_quin = 0
    elif quinquenio == 1:
        total_quin = sal_base * (5/100)
    elif quinquenio == 2:
        total_quin = sal_base * (10/100)
    elif quinquenio == 3:
        total_quin = sal_base * (15/100)
    elif quinquenio == 4:
        total_quin = sal_base * (20/100)
    elif quinquenio == 4:
        total_quin = sal_base * (25/100)
    elif quinquenio == 6:
        total_quin = sal_base * (30/100)
    else:
        total_quin = 0
    

    if edt_valetransp.get() == "":
        v_transp = 0
    else:
        v_transp = float(edt_valetransp.get())
    
    if edt_valeref.get() == "":
        v_ref = 0
    else:
        v_ref = float(edt_valeref.get())

    

    # Cálculo IPREM (Salário Base + Quinquenio) - Tabela 2024
    #Iprem = float('465.88')
    '''
    if sal_base <= 1412.00:
        Iprem = float(sal_base + total_quin) * 0.11
    elif 1412.01 <= sal_base <= 3842.08:
         Iprem = float(sal_base + total_quin) * 0.12
    elif 3842.09 <= sal_base <= 7786.02:
        Iprem = float(sal_base + total_quin) * 0.14
    elif sal_base > 7786.02:
        Iprem = float(sal_base + total_quin) * 0.16
    '''

    Iprem = float(sal_base + total_quin) * 0.14

    
    # Cálculo INSS - Tabela 2024
    if sal_base <= 1412.00:
        INSS = float(sal_base + total_quin) * 0.075
    elif 1412.01 <= sal_base <= 2666.68:
        INSS = float((sal_base + total_quin) * 0.09) - 21.18
    elif 2666.69 <= sal_base <= 4000.03:
        INSS = float((sal_base + total_quin)* 0.12) - 101.18
    elif 4000.04 <= sal_base <= 7786.02:
        INSS = float((sal_base + total_quin) * 0.14) - 181.18


    depend = edt_depend.get()
    IR_dependente = float(depend) * 189.59

    #Total_IR = (sal_base + total_quin) - (INSS + IR_dependente)
    Total_IR = (sal_base + total_quin + IR_dependente)

    # Cálculo IR - Tabela 2024
    #IR_Fonte = float('87.45')
    
    if Total_IR <= 2259.20:
        IR_Fonte = 0
    elif 2259.01 <= Total_IR <= 2826.65:
        IR_Fonte = float(Total_IR * 0.075) - 169.44
    elif 2826.66 <= Total_IR <= 3751.05:
        IR_Fonte = float(Total_IR * 0.15) - 381.44
    elif 3751.06 <= Total_IR <= 4664.68:
        IR_Fonte = float(Total_IR * 0.255) - 662.77
    elif Total_IR > 4664.68:
        IR_Fonte = float(Total_IR * 0.275) - 896.00


    #Calculando o Salário por hora
    sal_hora = (sal_base + total_quin) / total_horas_mes
    #Calculando o Salário por hora 50%
    sal_hora50 = ((sal_base + total_quin) / total_horas_mes) * 1.5
    #Calculando o Salário por hora 70%
    sal_hora70 = ((sal_base + total_quin) / total_horas_mes) * 1.7
    #Calculando o Salário por hora 100%
    sal_hora100 = ((sal_base + total_quin) / total_horas_mes) * 2
    #Calculando o Salário por hora Adicional Noturno
    sal_hora_AdNoturno = ((sal_base + total_quin) / total_horas_mes) * 0.2
    #Calculando Periculosidade = Salário * 30%
    if pericul.get() == 1:
        periculosidade = sal_base * (30 / 100)
    else:
        periculosidade = 0
    #Calculando Insalubridade = Salário * 20%
    if insalub.get() == 1:
        insalubridade = sal_base * (20 / 100)
    else:
        insalubridade = 0
    #Calculando Adicional Noturno
    #total_adnoturno = sal_hora_AdNoturno * edt_adnoturno

    #Calculando o Salário diário
    sal_dia = sal_hora * total_horas_dia
    #Calculando o Salário semanal
    sal_sem = sal_dia * total_dias_trab
    #Calculando o Salário mensal
    sal_mes = sal_sem * total_horas_sem

    total_bruto = sal_base + cesta_basica + total_quin + periculosidade + insalubridade + v_transp + v_ref

    total_desc = Iprem + IR_Fonte #+ IR_dependente
    total_liq = total_bruto - total_desc

                
    # # # V E N C I M E N T O S

    lbl_sal_base = Label(frame_venc, 
        text=f'+     Salário Base:= R$ {sal_base:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg=cor6)
    lbl_sal_base.place(x=5, y=3)

    lbl_cesta = Label(frame_venc, 
        text=f'+     Cesta Básica:= R$ {cesta_basica:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg=cor6)
    lbl_cesta.place(x=5, y=20)

    lbl_quin = Label(frame_venc, 
        text=f'+       Quinquenio:= R$ {total_quin:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg=cor6)
    lbl_quin.place(x=5, y=38)

    lbl_peric = Label(frame_venc, 
        text=f'+ Periculosidade:= R$ {periculosidade:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg=cor6)
    lbl_peric.place(x=5, y=56)

    lbl_insalub = Label(frame_venc, 
        text=f'+   Insalubridade:= R$ {insalubridade:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg=cor6)
    lbl_insalub.place(x=5, y=74)

    lbl_valetransp = Label(frame_venc, 
        text=f'+   Vale Transporte:= R$ {v_transp:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg=cor6)
    if valetransp.get() == 1:
        lbl_valetransp.place(x=5, y=92)
    else:
        lbl_valetransp.forget() # Ocultar
    
    lbl_valeref = Label(frame_venc, 
        text=f'+   Vale Refeição:= R$ {v_ref:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg=cor6)
    if valeref.get() == 1:
        lbl_valeref.place(x=5, y=110)
    else:
        lbl_valeref.forget() # Ocultar
    

    lbl_tbruto = Label(frame_venc, 
        image=logo_tbruto,
        text=f' TOTAL Bruto:= R$ {total_bruto:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg='darkblue')
    lbl_tbruto.place(x=5, y=200)

    # # # D E S C O N T O S

    lbl_iprem = Label(frame_desc, 
        text=f'-                  IPREM:= R$ {Iprem:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg='darkorange')
    lbl_iprem.place(x=5, y=5)

    lbl_irfonte = Label(frame_desc, 
        text=f'-             IR/Fonte:= R$ {IR_Fonte:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg='darkorange')
    lbl_irfonte.place(x=5, y=22)

    lbl_irdepend = Label(frame_desc, 
        #text=f'- IRRF/Dependentes:= R$ {IR_dependente:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg='darkorange')
    lbl_irdepend.place(x=5, y=40)


    lbl_tdesc = Label(frame_desc, 
        image=logo_tdesc,
        text=f' TOTAL Desc.:= R$ {total_desc:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg='red')
    lbl_tdesc.place(x=5, y=200)

    total_liq = Label(frame_total, 
        image=logo_total,
        text=f'>> T O T A L  Líquido à Receber:= R$ {total_liq:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 10 bold'),
        bg='yellow',
        fg='red')
    total_liq.place(x=5, y=0)

    # Botão gerar PDF
    pdf = Button(frame_total, image=logo_pdf, cursor='hand2', command=gerar_pdf)
    pdf.place(x=460, y=0)

    # Horas Trabalhadas
    # ABA Horas
    lbl_hora = Label(aba3, 
                 image=logo_horas,
                 text=f' Salário / Hora__________:= R$ {sal_hora:_.2f}'.replace('.',',').replace('_','.'), 
                 compound=LEFT, 
                 relief=FLAT, 
                 anchor=NW,
                 font=('Verdana 8 bold'),
                 bg=cor1,
                 fg='green')
    lbl_hora.place(x=150, y=10)

    lbl_hora50 = Label(aba3, 
                 image=logo_horas,
                 text=f' Salário / Hora 50%__:= R$ {sal_hora50:_.2f}'.replace('.',',').replace('_','.'), 
                 compound=LEFT, 
                 relief=FLAT, 
                 anchor=NW,
                 font=('Verdana 8 bold'),
                 bg=cor1,
                 fg='darkcyan')
    lbl_hora50.place(x=150, y=38)

    lbl_hora70 = Label(aba3, 
                 image=logo_horas,
                 text=f' Salário / Hora 70%__:= R$ {sal_hora70:_.2f}'.replace('.',',').replace('_','.'), 
                 compound=LEFT, 
                 relief=FLAT, 
                 anchor=NW,
                 font=('Verdana 8 bold'),
                 bg=cor1,
                 fg='blue')
    lbl_hora70.place(x=150, y=65)

    lbl_hora100 = Label(aba3, 
                 image=logo_horas,
                 text=f' Salário / Hora 100%:= R$ {sal_hora100:_.2f}'.replace('.',',').replace('_','.'), 
                 compound=LEFT, 
                 relief=FLAT, 
                 anchor=NW,
                 font=('Verdana 8 bold'),
                 bg=cor1,
                 fg='darkblue')
    lbl_hora100.place(x=150, y=92)

    lbl_hora_adnot = Label(aba3, 
                 image=logo_horas,
                 text=f' Adicional Noturno_____:= R$ {sal_hora_AdNoturno:_.2f}'.replace('.',',').replace('_','.'), 
                 compound=LEFT, 
                 relief=FLAT, 
                 anchor=NW,
                 font=('Verdana 8 bold'),
                 bg=cor1,
                 fg='purple')
    lbl_hora_adnot.place(x=150, y=120)
    

# # #

logo_venc = Image.open('images/orb_plus.png')
logo_venc = logo_venc.resize((32,32))
logo_venc = ImageTk.PhotoImage(logo_venc)

venc = Label(frame_calc, 
                 image=logo_venc,
                 text='[ VENCIMENTOS ]', 
                 compound=LEFT, 
                 relief=FLAT, 
                 anchor=NW,
                 font=('Verdana 8 bold'),
                 bg='lightgray',
                 fg='blue')
venc.place(x=5, y=5)

def Validar_Nome(nome):
    if nome.isalpha():
        return True
    return False

def Validar():
    nome = edt_nome.get()
    if not Validar_Nome(nome):
        messagebox.showerror("Invalid Input", "Information: \n Por favor preencha seu Nome corretamente !")
    elif edt_valetransp.get() == "" and valetransp.get() == 1:
        messagebox.showerror("Invalid Input", "Information: \n Por favor informe o Vale Transporte !")
        edt_valetransp[Text]="0"
        edt_valetransp.focus()
    elif edt_valeref.get() == "" and valeref.get() == 1:
        messagebox.showerror("Invalid Input", "Information: \n Por favor informe o Vale Refeição !")
        edt_valeref[Text]="0"
        edt_valeref.focus()
    else:
        Calcular()
        abas.add(aba3, text="Horas") # Mostra a Aba 3
        abas.select(aba3) 
    '''
    if edt_nome.get() == '':
        #messagebox = (showinfo, showwarning, showerror, askquestion ,askokcancel, askyesno, askretrycancel)
        messagebox.showinfo("ShowInfo", "Information: \n Informe seu Nome !")
        edt_nome.focus()
    else:
        Calcular()
    '''


# Botão Calcular
app_btn = Button(frame_calc, 
                 image=app_btn_img,
                 text=' CALCULAR ',
                 cursor='hand2', # estilo do cursor do mouse
                 width=100,
                 compound=LEFT, 
                 relief=RAISED,
                 overrelief=RIDGE,
                 anchor=NW,
                 font=('Yvi 10 bold'),
                 bg=cor1,
                 fg=cor4,
                 command=Validar)
app_btn.place(x=200, y=5)


logo_desc = Image.open('images/orb_minus.png')
logo_desc = logo_desc.resize((32,32))
logo_desc = ImageTk.PhotoImage(logo_desc)

venc = Label(frame_calc, 
                 image=logo_desc,
                 text='[ DESCONTOS ]', 
                 compound=LEFT, 
                 relief=FLAT, 
                 anchor=NW,
                 font=('Verdana 8 bold'),
                 bg='lightgray',
                 fg='red')
venc.place(x=360, y=5)

logo_horas = Image.open('images/schedule.png')
logo_horas = logo_horas.resize((22,22))
logo_horas = ImageTk.PhotoImage(logo_horas)

frame_total = Frame(janela, width=1040, height=35, pady=0, bg='yellow')
frame_total.grid(row=3, column=0)

logo_pdf = Image.open('images/pdf.png')
logo_pdf = logo_pdf.resize((32,32))
logo_pdf = ImageTk.PhotoImage(logo_pdf)

frame_footer = Frame(janela, width=1043, height=15, pady=0, bg=cor6)
frame_footer.grid(row=4, column=0)

# # #
# Função para gerar PDF padronizado com os dados fornecidos
def pdf_padrao(dados, nome_arquivo):
    try:
        # Parametros:
        # - dados: informações fornecidas pelo usuário com o título e valor de cada campo
        # - nome_arquivo: Nome do arquivo PDF que será gerado

        pdf = canvas.Canvas(nome_arquivo, pagesize=A4)
        largura, altura = A4
        y = altura - 2 * cm

        # Configurações da tabela
        largura_colunas = [5 * cm, 5 * cm, 5 *cm]
        altura_linha = 1 * cm

        # Cabeçalho da tabela
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(2 * cm, y, "Relatório de Dados")
        y -= 2 * cm

        # Desenhar cabeçalhos com fundo cinza claro e borda
        headers = ["Funcionário", "Data Admissão", "Dependentes"]
        pdf.setFont("Helvetica-Bold", 10)
        
        for i, header in enumerate(headers):
            x = 2 * cm + sum(largura_colunas[:i])
            pdf.setFillColor(colors.lightgrey)
            pdf.rect(x, y - altura_linha, largura_colunas[i], altura_linha, fill=True, stroke=True)
            pdf.setFillColor(colors.black)
            # Centralizar o texto horizontalmente na celula
            text_x = x + (largura_colunas[i] / 2) - (pdf.stringWidth(header, "Helvetica-Bold", 10) / 2)
            # Centraliza o texto verticalmente na celula
            text_y = y - altura_linha / 2 - 4
            pdf.drawString(text_x, text_y, header)
        
        # Desenhar as linhas de dados com fudo branco e borda
        y -= altura_linha
        pdf.setFont("Helvetica", 10)

        for linha in dados:
            for i, item in enumerate(linha):
                x = 2 * cm + sum(largura_colunas[:i])
                pdf.setFillColor(colors.white)
                pdf.rect(x, y - altura_linha, largura_colunas[i], altura_linha, fill=True, stroke=True)
                pdf.setFillColor(colors.black)
                pdf.drawString(x + 0.2 * cm, y - 0.75 * cm, item)
            y -= altura_linha
        
        pdf.save()

        print(f"O PDF '{nome_arquivo}' foi criado com Sucesso!")
        messagebox.showinfo("Success:", f"O PDF '{nome_arquivo}' foi criado com Sucesso!")

    except Exception as e:
        messagebox.showerror("Error:", f"Erro ao gerar PDF!\n\n{e}")


# Função para coletar os dados de entrada e gerar o PDF
def gerar_pdf():
    dados = [
        [edt_nome.get(), edt_adm.get(), edt_depend.get()]
    ]
       
    nome_arquivo = "WorkedHours.pdf"
    pdf_padrao(dados, nome_arquivo)


janela.mainloop()