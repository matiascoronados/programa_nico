from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
import os

root = Tk()
root.title("Espectro de Diseño segun Nch2369")
root.geometry("980x510")

#Constantes
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
size_estandar = width,heigth=350,350
imagen_estandar = ImageTk.PhotoImage(Image.new("RGB",size_estandar,"white"))

#Variables globales
n_archivo = 0
directorio = ""
imagenes_actual=[]
indice_actual=0

img_pantalla = ImageTk.PhotoImage(Image.open("Imagenes/amortig_1.png"))
img_amoritg = Image.open("Imagenes/amortig_1.png")
img_coef_1 = Image.open("Imagenes/coef_1.png")
img_coef_2 = Image.open("Imagenes/coef_2.png")
img_coef_3 = Image.open("Imagenes/coef_3.png")
img_sistema_1 = Image.open("Imagenes/sistema_1.png")
img_sistema_2 = Image.open("Imagenes/sistema_2.png")
img_sistema_3 = Image.open("Imagenes/sistema_3.png")
img_tipo_1 = Image.open("Imagenes/tipo_1.png")
img_tipo_2 = Image.open("Imagenes/tipo_2.png")
img_zona_1 = Image.open("Imagenes/zona_1.png")
img_zona_2 = Image.open("Imagenes/zona_2.png")
img_zona_3 = Image.open("Imagenes/zona_3.png")
img_zona_4 = Image.open("Imagenes/zona_4.png")
img_lista_amortig = [img_amoritg]
img_lista_coef = [img_coef_1,img_coef_2,img_coef_3]
img_lista_sistema = [img_sistema_1,img_sistema_2,img_sistema_3]
img_lista_tipo = [img_tipo_1,img_tipo_2]
img_lista_zona = [img_zona_1,img_zona_2,img_zona_3,img_zona_4]


def obtener_valor_aplificador(entradas):
    zona = entradas[6]
    valor_amplicador = 0
    if zona == "I":
        valor_amplicador = 0.5
    elif zona == "II":
        valor_amplicador = 0.75
    else:
        valor_amplicador = 1
    return valor_amplicador

def funcion_calculo_principal(entradas, arr_valores_t):
    valor_t_guion = obtener_valor_numerico(entradas[2],arr_valores_t_guion,arr_tipo)
    valor_n = obtener_valor_numerico(entradas[2],arr_valores_n,arr_tipo)
    valor_i = obtener_valor_numerico(entradas[3],arr_valores_i,arr_coef)
    valor_e = obtener_valor_numerico(entradas[4],arr_valores_e,arr_amortg)
    valor_r = obtener_valor_numerico(entradas[5],arr_valores_r,arr_sistema)
    valor_a = obtener_valor_numerico(entradas[6],arr_valores_a,arr_zona)
    valor_cmax = obtener_valor_cmax(valor_r,valor_e)
    valor_amplicador = obtener_valor_aplificador(entradas)
    arr_resultado_s = []
    for valor_t in arr_valores_t:
        s_aux_a = (2.75*valor_a*valor_i)/valor_r
        s_aux_b = (valor_t_guion/valor_t)**valor_n
        s_aux_c = (0.05/valor_e)**0.4
        s_resultado = s_aux_a*s_aux_b*s_aux_c
        if s_resultado >= (valor_i*valor_cmax):
            s_resultado = valor_i*valor_cmax
        arr_resultado_s.append(round(s_resultado*valor_amplicador,3))
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

def obtener_nombre_archivo(tipo_archivo,extencion):
    global n_archivo
    global directorio
    nombre_archivo = directorio+"/"+tipo_archivo+"_"+str(n_archivo)+extencion
    while os.path.isfile(nombre_archivo):
        n_archivo = n_archivo + 1
        nombre_archivo = directorio+"/"+tipo_archivo+"_"+str(n_archivo)+extencion
    return nombre_archivo

def crear_archivo_txt(arr_valores_t, arr_valores_s):
    try:
        nombre_archivo = obtener_nombre_archivo("datos",".txt")
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
        nombre_archivo = obtener_nombre_archivo("grafico",".png")
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
        messagebox.showinfo("Informacion","Archivos creados bajo los nombres: \n\tdatos_"+str(n_archivo)+".txt \n\tgrafico_"+str(n_archivo)+".png")
        n_archivo = n_archivo+1

def normar_string(string_e, len_e):
    largo_string = len(string_e)
    if largo_string > len_e:
        string_final = ""
        for x in range(largo_string-len_e,largo_string):
            string_final = string_final+string_e[x] 
        return "..."+string_final
    else:
        return string_e

def elegir_directorio():
    global directorio
    directorio = filedialog.askdirectory()
    str_directorio = normar_string(str(directorio),40)
    lb_directorio.config(text=str_directorio)

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
    drop_sistema_menu = drop_sistema_sub_categoria['menu']
    drop_sistema_menu.delete(0,'end')
    indice_categoria = arr_categor_sistema.index(var_sistema_categoria.get())
    tupla_indices = matriz_indices_sistema[indice_categoria]
    for i in range(tupla_indices[0],tupla_indices[1]+1):
        drop_sistema_menu.add_command(label=arr_sistema[i],command=lambda val=arr_sistema[i]:var_sistema.set(val))
    var_sistema.set(arr_sistema[tupla_indices[0]])

def cambiar_valor_tipo(*args):
    valor_t_guion = obtener_valor_numerico(var_tipo.get(),arr_valores_t_guion,arr_tipo)
    valor_n = obtener_valor_numerico(var_tipo.get(),arr_valores_n,arr_tipo)
    str_t_guion = "T' = "+str(valor_t_guion)
    str_n = "n = "+str(valor_n)
    lb_t_guion.config(text=str_t_guion)
    lb_n.config(text=str_n)

def cambiar_valor_coef(*args):
    valor_i = obtener_valor_numerico(var_coef.get(),arr_valores_i,arr_coef)
    str_i = "I = "+str(valor_i)
    lb_i.config(text=str_i)

def cambiar_valor_amortg(*args):
    valor_e = obtener_valor_numerico(var_amortg.get(),arr_valores_e,arr_amortg)
    str_e = "e = "+str(valor_e)
    lb_e.config(text=str_e)

def cambiar_valor_sistema(*args):
    valor_r = obtener_valor_numerico(var_sistema.get(),arr_valores_r,arr_sistema)
    str_r = "R = "+str(valor_r)
    lb_r.config(text=str_r)

def cambiar_valor_zona(*args):
    valor_a = obtener_valor_numerico(var_zona.get(),arr_valores_a,arr_zona)
    str_a = "A₀ = "+str(valor_a)
    lb_a.config(text=str_a)

def mostrar_imagen(lista_imagenes,indice_imagen):
    global lb_imagen
    global img_pantalla
    global imagenes_actual
    global indice_actual
    indice_actual = 0
    imagenes_actual = lista_imagenes
    resize_imagen = resize_at(imagenes_actual[indice_actual],350)
    img_pantalla = ImageTk.PhotoImage(resize_imagen)
    lb_imagen.config(image=img_pantalla)

def f_next():
    global lb_imagen
    global img_pantalla
    global imagenes_actual
    global indice_actual
    if len(imagenes_actual) is not 0:
        indice_actual = indice_actual +1
        if indice_actual > len(imagenes_actual)-1:
            indice_actual = len(imagenes_actual)-1
            resize_imagen = resize_at(imagenes_actual[indice_actual],350)
            img_pantalla = ImageTk.PhotoImage(resize_imagen)
            lb_imagen.config(image=img_pantalla)
        else:
            resize_imagen = resize_at(imagenes_actual[indice_actual],350)
            img_pantalla = ImageTk.PhotoImage(resize_imagen)
            lb_imagen.config(image=img_pantalla)

def f_back():
    global lb_imagen
    global img_pantalla
    global imagenes_actual
    global indice_actual
    if len(imagenes_actual) is not 0:
        if indice_actual != 0:
            indice_actual = indice_actual -1
        if indice_actual > len(imagenes_actual)-1:
            indice_actual = 0
            resize_imagen = resize_at(imagenes_actual[indice_actual],350)
            img_pantalla = ImageTk.PhotoImage(resize_imagen)
            lb_imagen.config(image=img_pantalla)
        else:
            resize_imagen = resize_at(imagenes_actual[indice_actual],350)
            img_pantalla = ImageTk.PhotoImage(resize_imagen)
            lb_imagen.config(image=img_pantalla)

def resize_at(img,height):
    return img.resize((height,height))


var_tipo = StringVar()
var_coef = StringVar()
var_amortg = StringVar()
var_sistema_categoria = StringVar()
var_sistema = StringVar()
var_zona = StringVar()

var_sistema_categoria.trace('w',actualizar_valores_sistema)
var_sistema.trace('w',cambiar_valor_sistema)

lb_periodo =    Label(root,text="Periodo considerado",bg="grey")
lb_paso =       Label(root,text="Paso del periodo",bg="grey")
lb_tipo =       Label(root,text="Tipo de suelo",bg="grey")
lb_coef =       Label(root,text="Coef. de importancia",bg="grey")
lb_amortg =     Label(root,text="Amortiguamiento",bg="grey")
lb_sistema =    Label(root,text="Sistema resistente",bg="grey")
lb_zona =       Label(root,text="Zona sismica",bg="grey")
lb_directorio = Label(root,text="Seleccione un directorio")

datos_frame = LabelFrame(root,text="Datos",padx=10)
imagen_frame = LabelFrame(root,text="",padx=10,borderwidth=0)

lb_t_guion = Label(datos_frame,text="T' = 0")
lb_n = Label(datos_frame,text="n = 0")
lb_i = Label(datos_frame,text="I = 0")
lb_e = Label(datos_frame,text="e = 0")
lb_r = Label(datos_frame,text="R = 0")
lb_a = Label(datos_frame,text="A₀ = 0")

lb_resumen = Label(imagen_frame,text="RESUMEN",relief=GROOVE)
lb_imagen = Label(imagen_frame,image=imagen_estandar,relief=GROOVE)

entry_periodo = Entry(root,width=15)
entry_paso = Entry(root,width=15)

drop_tipo = OptionMenu(root, var_tipo,*arr_tipo,command=cambiar_valor_tipo)
drop_coef = OptionMenu(root, var_coef,*arr_coef,command=cambiar_valor_coef)
drop_amortg = OptionMenu(root, var_amortg,*arr_amortg,command=cambiar_valor_amortg)
drop_sistema_categoria = OptionMenu(root, var_sistema_categoria, *arr_categor_sistema)
drop_sistema_sub_categoria = OptionMenu(root, var_sistema, ())
drop_zona = OptionMenu(root, var_zona,*arr_zona,command=cambiar_valor_zona)

button_periodo = Button(root,text="(?)",bg="green")
button_paso = Button(root,text="(?)",bg="green")
button_tipo = Button(root,text="(?)",bg="green",command=lambda lista=img_lista_tipo: mostrar_imagen(lista,0))
button_coef = Button(root,text="(?)",bg="green",command=lambda lista=img_lista_coef: mostrar_imagen(lista,0))
button_amortg = Button(root,text="(?)",bg="green",command=lambda lista=img_lista_amortig: mostrar_imagen(lista,0))
button_sistema = Button(root,text="(?)",bg="green",command=lambda lista=img_lista_sistema: mostrar_imagen(lista,0))
button_zona = Button(root,text="(?)",bg="green",command=lambda lista=img_lista_zona: mostrar_imagen(lista,0))
button_ejecutar = Button(root,text="Ejecutar",bg="red",command=ejecutar)
button_directorio = Button(root,text="Elegir directorio",bg="blue",command=elegir_directorio)

button_siguiente = Button(root,text=">>",command=f_next)
button_anterior = Button(root,text="<<",command=f_back)

lb_periodo.grid(row=0,column=1,pady=10)
lb_paso.grid(row=1,column=1,pady=10)
lb_tipo.grid(row=2,column=1,pady=10)
lb_coef.grid(row=3,column=1,pady=10)
lb_amortg.grid(row=4,column=1,pady=10)
lb_sistema.grid(row=5,column=1,pady=10)
lb_zona.grid(row=7,column=1,pady=10)
lb_directorio.grid(row=9,column=2,pady=10)

lb_imagen.config(width=350)
lb_resumen.config(width=39)
lb_resumen.config(height=5)
lb_imagen.pack()
lb_resumen.pack()

lb_periodo.config(width=15)
lb_paso.config(width=15)
lb_tipo.config(width=15)
lb_coef.config(width=15)
lb_amortg.config(width=15)
lb_sistema.config(width=15)
lb_zona.config(width=15)
lb_directorio.config(width=30)

datos_frame.grid(row=0,column=3,rowspan=8)
imagen_frame.grid(row=0,column=5,rowspan=8,columnspan=3)
lb_t_guion.pack(pady=20,padx=10)
lb_n.pack(pady=20,padx=10)
lb_i.pack(pady=20,padx=10)
lb_e.pack(pady=20,padx=10)
lb_r.pack(pady=20,padx=10)
lb_a.pack(pady=20,padx=10)
lb_t_guion.config(width=10)

entry_periodo.grid(row=0,column=2)
entry_paso.grid(row=1,column=2)
drop_tipo.grid(row=2,column=2)
drop_coef.grid(row=3,column=2)
drop_amortg.grid(row=4,column=2)
drop_sistema_categoria.grid(row=5,column=2)
drop_sistema_sub_categoria.grid(row=6,column=2)
drop_zona.grid(row=7,column=2)
drop_tipo.config(width=15)
drop_coef.config(width=15)
drop_amortg.config(width=15)
drop_sistema_categoria.config(width=15)
drop_sistema_sub_categoria.config(width=15)
drop_zona.config(width=15)

button_periodo.grid(row=0,column=0)
button_paso.grid(row=1,column=0)
button_tipo.grid(row=2,column=0)
button_coef.grid(row=3,column=0)
button_amortg.grid(row=4,column=0)
button_sistema.grid(row=5,column=0)
button_zona.grid(row=7,column=0)
button_ejecutar.grid(row=9,column=3)
button_directorio.grid(row=9,column=1)

button_anterior.grid(row=9,column=5)
button_siguiente.grid(row=9,column=7)

root.mainloop()