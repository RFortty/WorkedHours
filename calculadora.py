# Instalar biblioteca TKInter: pip install tkinter
# Instalar biblioteca Custom TKInter: pip install customtkinter
# Instalar biblioteca Pillow: pip install pillow
import customtkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from datetime import date, datetime

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
janela.geometry('500x540+350+80') # ('width x height + X coordinate + Y coordinate')
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


frame_down = Frame(janela, width=1043, height=160, pady=0, bg=cor1)
frame_down.grid(row=1, column=0)

lbl_nome = Label(frame_down, 
                 text='Nome Completo:', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_nome.place(x=10, y=10)

edt_nome = Entry(frame_down,
                 width=46, 
                 font=('Ivy 10 bold italic'),
                 justify='left', # posição do texto
                 relief='groove', # estilo da Entry (flat, raised, sunken, groove, ridge)
                 bg='cyan', # cor do fundo
                 highlightbackground='black', # cor da borda
                 border= 3, # espessura da borda
                 fg='red', # cor do texto
                 validatecommand="%S") 
edt_nome.place(x=112, y=11)
edt_nome.focus()

lbl_adm = Label(frame_down, 
                 text='Data Admissão:', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_adm.place(x=10, y=45)
edt_adm = Entry(frame_down, width=10, justify='left', relief='groove')
edt_adm.place(x=112, y=45)

lbl_depend = Label(frame_down, 
                 text='nº Dependentes:', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_depend.place(x=230, y=45)
edt_depend = Entry(frame_down, width=5, justify='left', relief='groove')
edt_depend.place(x=340, y=45)

lbl_sal = Label(frame_down, 
                 text='Salário Base: R$', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_sal.place(x=10, y=80)
edt_sal = Entry(frame_down, width=15, justify='left', relief='groove')
edt_sal.place(x=112, y=80)

lbl_cesta = Label(frame_down, 
                 text='Cesta Básica: R$', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_cesta.place(x=230, y=80)
edt_cesta = Entry(frame_down, width=15, justify='left', relief='groove')
edt_cesta.place(x=340, y=80)

lbl_horas_trab = Label(frame_down, 
                 text='Horas Trabalhadas/dia:', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_horas_trab.place(x=10, y=110)
edt_horas_trab = Entry(frame_down, width=5, justify='center', relief='groove', bg='cyan', fg='darkblue')
edt_horas_trab.place(x=60, y=130)
edt_horas_trab.insert(END,'8')

lbl_dias_trab = Label(frame_down, 
                 text='Dias Trabalhados/semana:', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_dias_trab.place(x=160, y=110)
edt_dias_trab = Entry(frame_down, width=5, justify='center', relief='groove', bg='cyan', fg='darkblue')
edt_dias_trab.place(x=220, y=130)
edt_dias_trab.insert(END,'5')

lbl_mes_trab = Label(frame_down, 
                 text='Dias Trabalhados/mês:', 
                 anchor=NW,
                 font=('Ivy 10'),
                 bg=cor1,
                 fg=cor4)
lbl_mes_trab.place(x=340, y=110)
edt_mes_trab = Entry(frame_down, width=5, justify='center', relief='groove', bg='cyan', fg='darkblue')
edt_mes_trab.place(x=380, y=130)
edt_mes_trab.insert(END,'220')

frame_calc = Frame(janela, width=1043, height=280, pady=0, bg='lightgray')
frame_calc.grid(row=2, column=0)

app_btn_img = Image.open('images/calculator.png')
app_btn_img = app_btn_img.resize((25,25))
app_btn_img = ImageTk.PhotoImage(app_btn_img)

frame_venc = Frame(janela, width=240, height=120, pady=0, bg='cyan')
frame_venc.grid(row=2, column=0)
frame_venc.place(x=5, y=250)

frame_desc = Frame(janela, width=240, height=120, pady=0, bg='cyan')
frame_desc.grid(row=2, column=0)
frame_desc.place(x=255, y=250)

logo_tbruto = Image.open('images/coins.png')
logo_tbruto = logo_tbruto.resize((22,22))
logo_tbruto = ImageTk.PhotoImage(logo_tbruto)

logo_tdesc = Image.open('images/coins.png')
logo_tdesc = logo_tdesc.resize((22,22))
logo_tdesc = ImageTk.PhotoImage(logo_tdesc)

logo_total = Image.open('images/bag_cash.png')
logo_total = logo_total.resize((32,32))
logo_total = ImageTk.PhotoImage(logo_total)


### Função C Á L C U L A R : ###

# total dias por ano
ano = 365
# total semanas por ano
semanas = 52
# total horas trabalhadas por dia
total_horas_dia = 8
# total dias de trabalho
total_dias_trab = 5


def Calcular():
    #pass

    nome = edt_nome.get()    
    admissao = edt_adm.get()
    '''
    while True:
        try:
            admissao = edt_adm.get()
        except:
            messagebox.showinfo("showinfo", "Information: Data Inválida !")
    '''
    sal_base = float(edt_sal.get())
    aux_doença = (sal_base + (sal_base * 0.07)) * (91/100)
    sal_base = aux_doença
    cesta_basica = float(edt_cesta.get())

    data_hoje = datetime.today()
    data_hoje_formatada = data_hoje.strftime('%d/%m/%Y') # Converte Data em String
    data_adm = datetime.strptime(admissao, '%d/%m/%Y') # Converte String em Data
    data_dif = data_hoje - data_adm

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
    
    # Cálculo IPREM (Salário Base + Quinquenio) - Tabela 2024
    #Iprem = float('465.88')
    if sal_base <= 1412.00:
        Iprem = float(sal_base + total_quin) * 0.11
    elif 1412.01 <= sal_base <= 3842.08:
         Iprem = float(sal_base + total_quin) * 0.12
    elif 3842.09 <= sal_base <= 7786.02:
        Iprem = float(sal_base + total_quin) * 0.14
    elif sal_base > 7786.02:
        Iprem = float(sal_base + total_quin) * 0.16

    # Cálculo INSS - Tabela 2024
    if sal_base <= 1412.00:
        INSS = float(sal_base * 0.075)
    elif 1412.01 <= sal_base <= 2666.68:
        INSS = float(sal_base * 0.09) - 21.18
    elif 2666.69 <= sal_base <= 4000.03:
        INSS = float(sal_base * 0.12) - 101.18
    elif 4000.04 <= sal_base <= 7786.02:
        INSS = float(sal_base * 0.14) - 181.18


    depend = edt_depend.get()
    IR_dependente = float(depend) * 189.59

    Total_IR = (sal_base + total_quin) - (INSS + IR_dependente)

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

    
    #Calculando Total de Horas trabalhadas Semanal
    total_horas_sem = total_horas_dia * total_dias_trab
    #Calculando Total de Horas trabalhadas Mensal
    total_horas_mes = 220
    #Calculando Total de Horas trabalhadas Anual
    total_horas_ano = semanas * total_horas_sem

    #Calculando o Salário por hora
    sal_hora = (sal_base + total_quin) / 200
    #Calculando o Salário por hora 50%
    sal_hora50 = ((sal_base + total_quin) / 200) * 1.5
    #Calculando o Salário por hora 70%
    sal_hora70 = ((sal_base + total_quin) / 200) * 1.7
    #Calculando o Salário por hora 100%
    sal_hora100 = ((sal_base + total_quin) / 200) * 2
    #Calculando o Salário por hora Adicional Noturno
    sal_hora_AdNoturno = ((sal_base + total_quin) / 200) * 0.2
    #Calculando Periculosidade = Salário * 30%
    periculosidade = sal_base * (30 / 100)
    #Calculando Insalubridade = Salário * 20%
    insalubridade = sal_base * (20 / 100)

    #Calculando o Salário diário
    sal_dia = sal_hora * total_horas_dia
    #Calculando o Salário semanal
    sal_sem = sal_dia * total_dias_trab
    #Calculando o Salário mensal
    sal_mes = sal_sem * total_horas_sem

    total_bruto = sal_base + cesta_basica + total_quin + periculosidade
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
    lbl_sal_base.place(x=5, y=5)

    lbl_cesta = Label(frame_venc, 
        text=f'+     Cesta Básica:= R$ {cesta_basica:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg=cor6)
    lbl_cesta.place(x=5, y=22)

    lbl_quin = Label(frame_venc, 
        text=f'+       Quinquenio:= R$ {total_quin:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg=cor6)
    lbl_quin.place(x=5, y=40)

    lbl_peric = Label(frame_venc, 
        text=f'+ Periculosidade:= R$ {periculosidade:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg=cor6)
    lbl_peric.place(x=5, y=60)

    
    lbl_tbruto = Label(frame_venc, 
        image=logo_tbruto,
        text=f' TOTAL Bruto:= R$ {total_bruto:_.2f}'.replace('.',',').replace('_','.'), 
        compound=LEFT, 
        relief=FLAT, 
        anchor=NW,
        font=('Verdana 8 bold'),
        bg='cyan',
        fg='darkblue')
    lbl_tbruto.place(x=5, y=90)

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
        #text=f'- IR/Dependentes:= R$ {IR_dependente:_.2f}'.replace('.',',').replace('_','.'), 
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
    lbl_tdesc.place(x=5, y=90)

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


    lbl_hora = Label(frame_calc, 
                 image=logo_horas,
                 text=f' Salário / Hora__________:= R$ {sal_hora:_.2f}'.replace('.',',').replace('_','.'), 
                 compound=LEFT, 
                 relief=FLAT, 
                 anchor=NW,
                 font=('Verdana 8 bold'),
                 bg='lightgray',
                 fg='green')
    lbl_hora.place(x=110, y=165)

    lbl_hora50 = Label(frame_calc, 
                 image=logo_horas,
                 text=f' Salário / Hora 50%__:= R$ {sal_hora50:_.2f}'.replace('.',',').replace('_','.'), 
                 compound=LEFT, 
                 relief=FLAT, 
                 anchor=NW,
                 font=('Verdana 8 bold'),
                 bg='lightgray',
                 fg='darkcyan')
    lbl_hora50.place(x=110, y=188)

    lbl_hora70 = Label(frame_calc, 
                 image=logo_horas,
                 text=f' Salário / Hora 70%__:= R$ {sal_hora70:_.2f}'.replace('.',',').replace('_','.'), 
                 compound=LEFT, 
                 relief=FLAT, 
                 anchor=NW,
                 font=('Verdana 8 bold'),
                 bg='lightgray',
                 fg='blue')
    lbl_hora70.place(x=110, y=211)

    lbl_hora100 = Label(frame_calc, 
                 image=logo_horas,
                 text=f' Salário / Hora 100%:= R$ {sal_hora100:_.2f}'.replace('.',',').replace('_','.'), 
                 compound=LEFT, 
                 relief=FLAT, 
                 anchor=NW,
                 font=('Verdana 8 bold'),
                 bg='lightgray',
                 fg='darkblue')
    lbl_hora100.place(x=110, y=233)

    lbl_hora_adnot = Label(frame_calc, 
                 image=logo_horas,
                 text=f' Adicional Noturno_____:= R$ {sal_hora_AdNoturno:_.2f}'.replace('.',',').replace('_','.'), 
                 compound=LEFT, 
                 relief=FLAT, 
                 anchor=NW,
                 font=('Verdana 8 bold'),
                 bg='lightgray',
                 fg='purple')
    lbl_hora_adnot.place(x=110, y=255)
    
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
    else:
        Calcular()
    '''
    if edt_nome.get() == '':
        #messagebox = (showinfo, showwarning, showerror, askquestion ,askokcancel, askyesno, askretrycancel)
        messagebox.showinfo("ShowInfo", "Information: \n Informe seu Nome !")
        edt_nome.focus()
    else:
        Calcular()
    '''
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

frame_footer = Frame(janela, width=1043, height=15, pady=0, bg=cor6)
frame_footer.grid(row=4, column=0)


janela.mainloop()