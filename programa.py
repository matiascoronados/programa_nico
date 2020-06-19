from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt

root = Tk()
root.title("Espectro de Diseño segun Nch2369")
#root.iconbitmap("Imagenes/icono.ico")
root.geometry("780x500")

arr_tipos_variables = ["Periodo considerado",
"Paso del periodo",
"Tipo de suelo",
"Coef. de importancia",
"Amortiguamiento",
"Sistema resistente",
"Zona sismica"]
arr_tipo =["I","II","III","IV"]
arr_coef = ["C1","C2","C3"]
arr_amortg = ["Manto de acero soldado; chimeneas, silos, tolvas, tanques a presión, torres de proceso, cañerías, etc.",
"Manto de acero apernado o remachado",
"Marcos de acero apernado o remachado",
"Marcos de acero con uniones de terreno apernadas, con o sin arriostramiento",
"Estructura de H.A. y albañilería",
"Estr pref de H.A. puramente gravitacionales",
"Estr pref de H.A. con uniones húmedas, no dilatadas de los elem. no estructurales e incorporados en el modelo",
"Estr pref de H.A. con uniones húmedas dilatadas de los elem. no estructurales",
"Estr pref de H.A. uniones secas, dilatadas y no dilatadas con conex. apern. y conex. por barras embedibas en mortero",
"Estr pref de H.A. con uniones secas, dilatadas y no dilatadas con conex. soldadas",
"Otras estructuras no incluidas o asimilables a las de la lista"]
arr_categor_sistema = ["Estructuras diseñadas para permanecer elásticas",
"Otras estructuras no incluidas o aimilables a las de esta lista",
"Estructuras de acero",
"Estructuras de hormigón armado"]
matriz_indices_sistema = [[0, 0],[1,1],[2,10],[11,15]]

arr_sistema = ["Estructuras diseñadas para permanecer elásticas",
"Otras estructuras no incluidas o aimilables a las de esta lista",
"Edificios y estructuras de marcos dúctiles de acero con elementos no estructurales dilatados",
"Edificios y estrucutras de marcos dúctiles de acero con elementos no estructurales no dilatados e incorporados en el modelo estructural",
"Edificios y estructuras de marcos arriostrados, con anclajes dúctiles",
"Edificios industriales de un piso, con o sin puente grúa, y con arriostramiento continuo de techo",
"Edificios industriales de un piso, sin puente-grúa, sin arriostramiento continup de techo, que satisfacen 11.1.2",
"Naves de acero livianas que satisfacen las condiciones de 11.2.1",
"Esturcturas de péndulo invertido",
"Estructuras sísmicas isostáticas",
"Estructuras de plancha o manto de acero, cuyo comportamiento sísmico está controlado por el fenómeno de pandeo local",
"Edificio de estructuras de marcos dúctiles de hormigón armado con elementos no estructurales dilatados",
"Edificio y estructuras de marcos dúctiles de hormigón armado con elementos no estrucutrales no dilatados e incorporados en el modelo estructural",
"Edificios y estructuras de hormigón armado, con muros de corte",
"Edificios industriales de un piso, con o sin puente grúa, y con arriostramiento continuo de techo",
"Edificios industriales de un piso, sin puente-grúa, sin arriostramiento continuo de techa, que satisfacen 11.1.2"]
arr_zona = ["I","II","III"]

arr_valores_t_guion = [0.2, 0.35, 0.62, 1.35]
arr_valores_n = [1.0, 1.33, 1.8, 1.8]
arr_valores_i = [1.2 , 1.0, 0.8]
arr_valores_e = [0.02, 0.03, 0.02, 0.03, 0.05, 0.05, 0.05, 0.03, 0.03, 0.02, 0.02]
arr_valores_r = [1.0, 2.0, 5.0, 3.0, 5.0, 5.0, 3.0, 4.0, 3.0, 3.0, 3.0, 5.0, 3.0, 5.0, 5.0, 3.0]
arr_valores_a = [0.2, 0.3, 0.4]
matriz_valores_cmax = [[0.79, 0.68, 0.55], [0.6, 0.49, 0.42], [0.4, 0.34, 0.28], [0.32, 0.27, 0.22], [0.26, 0.23, 0.18]]
matriz_valores_cmax_y = [1.0,2.0,3.0,4.0,5.0]
matriz_valores_cmax_x = [0.02, 0.03, 0.05]
n_archivo = 0
directorio = ""

def funcion_calculo_principal(entradas, arr_valores_t):
    valor_t_guion = obtener_valor_numerico(entradas[2],arr_valores_t_guion,arr_tipo)
    valor_n = obtener_valor_numerico(entradas[2],arr_valores_n,arr_tipo)
    valor_i = obtener_valor_numerico(entradas[3],arr_valores_i,arr_coef)
    valor_e = obtener_valor_numerico(entradas[4],arr_valores_e,arr_amortg)
    valor_r = obtener_valor_numerico(entradas[5],arr_valores_r,arr_sistema)
    valor_a = obtener_valor_numerico(entradas[6],arr_valores_a,arr_zona)
    valor_cmax = obtener_valor_cmax(valor_r,valor_e)
    arr_resultado_s = []
    for valor_t in arr_valores_t:
        s_aux_a = (2.75*valor_a*valor_i)/valor_r
        s_aux_b = (valor_t_guion/valor_t)**valor_n
        s_aux_c = (0.05/valor_e)**0.4
        s_resultado = s_aux_a*s_aux_b*s_aux_c
        if s_resultado >= (valor_i*valor_cmax):
            s_resultado = valor_i*valor_cmax
        arr_resultado_s.append(round(s_resultado,3))
    return arr_resultado_s

def obtener_valor_cmax(valor_r, valor_e):
    indice_y = matriz_valores_cmax_y.index(valor_r)
    indice_x = matriz_valores_cmax_x.index(valor_e)
    return matriz_valores_cmax[indice_y][indice_x]

def obtener_valor_numerico(elemento,arr_valores_elemento,arr_texto_elemento):
    indice_elemento = arr_texto_elemento.index(elemento)
    return arr_valores_elemento[indice_elemento]

def crear_arreglo_t(entradas):
    e_periodo = entradas[0]
    e_paso = entradas[1]
    e_paso_decimales = cantidad_decimales(e_paso)
    arr_t = []
    arr_t.append(0.001)
    e_periodo_aux = 0
    while e_periodo_aux < e_periodo:
        e_periodo_aux += e_paso
        arr_t.append(round(e_periodo_aux,e_paso_decimales+1))
    if(arr_t[-1] > e_periodo):
        arr_t[-1] = e_periodo
    return arr_t

def cantidad_decimales(flotante):
    decimales = str(flotante).split(".")[1]
    return len(decimales)

def validar_entradas(e_periodo, e_paso):
    periodo = str(e_periodo).replace(",",".")
    paso = str(e_paso).replace(",",".")
    entradas_validadas = []
    try:
        f_periodo = float(periodo)
        f_paso = float(paso)
        if f_periodo <= 0 or f_paso <= 0:
            entradas_validadas.append("No puede ingresar valores negativos ni iguales a 0")
        elif cantidad_decimales(f_periodo) > 1:
            entradas_validadas.append("No pueden haber mas de 1 decimal en 'Periodo considerado'")
        elif f_paso > 1:
            entradas_validadas.append("El valor de 'Paso del periodo' tiene que ser menor que 1")
        else:
            entradas_validadas.append(f_periodo)
            entradas_validadas.append(f_paso)
    except:
        entradas_validadas.append("No se reconocieron los datos de entrada")
    return entradas_validadas


def entradas_faltantes(entradas):
    salida = []
    for i in range(len(entradas)):
        elemento = entradas[i]
        if elemento == "":
            salida.append(arr_tipos_variables[i])
    return salida

def actualizar_entrada(arr_entradas, entrada_actual, pos):
    arr_entradas.pop(pos)
    arr_entradas.insert(pos,entrada_actual[pos])


def crear_archivo_txt(arr_valores_t, arr_valores_s):
    try:
        global n_archivo
        nombre_archivo = directorio+"/"+"datos_"+str(n_archivo)+".txt"
        archivo = open(nombre_archivo,'x')
        for i in range(len(arr_valores_t)):
            string_aux = str(arr_valores_t[i]).replace(".",",")+"\t"+str(arr_valores_s[i]).replace(".",",")+"\r\n"
            archivo.write(string_aux)
        archivo.close()
    except:
        return False
    return True

def crear_archivo_grafico(arr_valores_t,arr_valores_s):
    try:
        global n_archivo
        nombre_archivo = directorio+"/"+"grafico_"+str(n_archivo)+".png"
        fig, ax = plt.subplots()
        ax.plot(arr_valores_t,arr_valores_s)
        ax.set(xlabel='Periodo (seg)', ylabel='S0/g',title='Espectro diseño horizontal - Analisis modal espectral Nch2369 2003')
        ax.grid()
        fig.savefig(nombre_archivo)
    except:
        return False
    return True

def mostrar_elementos_faltantes(arr_elementos,mensaje):
    salida = ""
    separador = "\t"
    if mensaje == "":
        separador = ""
    for elemento in arr_elementos:
        salida = separador+elemento+"\n"+salida
    messagebox.showerror("Error",mensaje+salida)

def proceso_principal(entradas):
    arr_valores_t = crear_arreglo_t(entradas)
    arr_valores_s = funcion_calculo_principal(entradas,arr_valores_t)
    if not crear_archivo_txt(arr_valores_t, arr_valores_s):
        messagebox.showerror("Error","Fallo inesperado en crear archivo de texto")
    elif not crear_archivo_grafico(arr_valores_t, arr_valores_s):
         messagebox.showerror("Error","Fallo inesperado en crear archivo del grafico")
    else:
        global n_archivo
        n_archivo = n_archivo + 1
        messagebox.showinfo("Informacion","Archivos creados bajo los nombres: \n\tdatos_"+str(n_archivo)+".txt \n\tgrafico_"+str(n_archivo)+".png")

def elegir_directorio():
    global directorio
    directorio = filedialog.askdirectory()

def ejecutar():
    if directorio == "":
        messagebox.showinfo("Informacion","Elige primero un directorio")
    else:
        entradas = [entry_periodo.get(),entry_paso.get(),var_tipo.get(),var_coef.get(),var_amortg.get(),var_sistema.get(),var_zona.get()]
        arr_faltantes = entradas_faltantes(entradas)
        if len(arr_faltantes) > 0:
            mostrar_elementos_faltantes(arr_faltantes,"Faltan la(s) entrada(s): \n")
        else:
            arr_entradas_actualizadas = validar_entradas(entradas[0],entradas[1])
            if len(arr_entradas_actualizadas) == 1:
                mostrar_elementos_faltantes(arr_entradas_actualizadas,"")
            else:
                actualizar_entrada(entradas, arr_entradas_actualizadas, 0)
                actualizar_entrada(entradas, arr_entradas_actualizadas, 1)
                proceso_principal(entradas)

def actualizar_valores_sistema(*args):
    try:
        menu = drop_sistema_sub_categoria['menu']
        menu.delete(0,'end')
        indice_categoria = arr_categor_sistema.index(var_sistema_categoria.get())
        tupla_indices = matriz_indices_sistema[indice_categoria]
        for i in range(tupla_indices[0],tupla_indices[1]+1):
            menu.add_command(label=arr_sistema[i],command=lambda val=arr_sistema[i]:var_sistema.set(val))
        var_sistema.set(arr_sistema[0])
    except:
        print("fallo")


var_tipo = StringVar()
var_coef = StringVar()
var_amortg = StringVar()
var_sistema_categoria = StringVar()
var_sistema = StringVar()
var_zona = StringVar()

var_sistema_categoria.trace('w',actualizar_valores_sistema)

lb_periodo =    Label(root,text="Periodo considerado",bg="grey",pady=3,padx=196)
lb_paso =       Label(root,text="Paso del periodo",bg="grey",pady=3,padx=210)
lb_tipo =       Label(root,text="Tipo de suelo",bg="grey",pady=3,padx=219)
lb_coef =       Label(root,text="Coef. de importancia",bg="grey",pady=3,padx=195)
lb_amortg =     Label(root,text="Amortiguamiento",bg="grey",pady=3,padx=207)
lb_sistema =    Label(root,text="Sistema resistente",bg="grey",pady=3,padx=202)
lb_zona =       Label(root,text="Zona sismica",bg="grey",pady=3,padx=218)

arr_categor_sistema_sub_categoria = [""]

entry_periodo = Entry(root,width=15)
entry_paso = Entry(root,width=15)
drop_tipo = OptionMenu(root, var_tipo,*arr_tipo)
drop_coef = OptionMenu(root, var_coef,*arr_coef)
drop_amortg = OptionMenu(root, var_amortg,*arr_amortg)

drop_sistema_categoria = OptionMenu(root, var_sistema_categoria, *arr_categor_sistema)
drop_sistema_sub_categoria = OptionMenu(root, var_sistema, ())

drop_zona = OptionMenu(root, var_zona,*arr_zona)

button_periodo = Button(root,text="(?)",bg="green")
button_paso = Button(root,text="(?)",bg="green")
button_tipo = Button(root,text="(?)",bg="green")
button_coef = Button(root,text="(?)",bg="green")
button_amortg = Button(root,text="(?)",bg="green")
button_sistema = Button(root,text="(?)",bg="green")
button_zona = Button(root,text="(?)",bg="green")
button_ejecutar = Button(root,text="Ejecutar",bg="red",command=ejecutar)
button_directorio = Button(root,text="Elegir directorio",bg="blue",command=elegir_directorio)

lb_periodo.grid(row=0,column=1,pady=20)
lb_paso.grid(row=1,column=1,pady=20)
lb_tipo.grid(row=2,column=1,pady=20)
lb_coef.grid(row=3,column=1,pady=20)
lb_amortg.grid(row=4,column=1,pady=20)
lb_sistema.grid(row=5,column=1,pady=20)
lb_zona.grid(row=6,column=1,pady=20)

entry_periodo.grid(row=0,column=2)
entry_paso.grid(row=1,column=2)

drop_tipo.grid(row=2,column=2)
drop_coef.grid(row=3,column=2)
drop_amortg.grid(row=4,column=2)
drop_sistema_categoria.grid(row=5,column=2)
drop_sistema_sub_categoria.grid(row=5,column=3)
drop_zona.grid(row=6,column=2)

button_periodo.grid(row=0,column=4)
button_paso.grid(row=1,column=4)
button_tipo.grid(row=2,column=4)
button_coef.grid(row=3,column=4)
button_amortg.grid(row=4,column=4)
button_sistema.grid(row=5,column=4)
button_zona.grid(row=6,column=4)
button_ejecutar.grid(row=7,column=2,columnspan=2)
button_directorio.grid(row=7,column=0,columnspan=2)

root.mainloop()