import tkinter as tk
from time import sleep
from tkcalendar import DateEntry, Calendar

# black mode dark gray
bg_color = "#2d2d2d"
light_blue = "#00a8ff"

window = tk.Tk()

window.title("Calculadora de aguinaldo")
window.geometry("650x800")
# background color grey
window.config(bg=bg_color)

Lista = []
def diferencia_en_dias ():
    diferencia = (Cl2.get_date() - Cl1.get_date()).days
    Diff = tk.Label (text = str(diferencia), font=("Arial",30), fg=light_blue,bg=bg_color)
    Diff.grid (row=3,column=1,padx=10,pady=10)
    return diferencia
    
def add_item(event):
    widget = event.widget
    text_item = widget.get()
    widget.delete(0, "end")
    
    salarioso = int(text_item)
    
    diff_dias = diferencia_en_dias()
    
    aguinaldo_dias = diff_dias * 15 /365
    
    aguinaldo_final = (int(salarioso) / 15) * int(aguinaldo_dias)
    
    aguinaldo_dias_redondo = round(aguinaldo_dias,2)
    
    aguinaldo_final_redondo = round(aguinaldo_final,2)
    
    Aguinaldo_texto = tk.Label (text="Los dias de aguinaldo son " + str(aguinaldo_dias_redondo), font=("Arial", 12), fg=light_blue, bg=bg_color)
    Aguinaldo_texto.grid(row=5, column= 1, padx=20,pady=30)
    
    Aguinaldo_dinero = tk.Label (text="El aguinaldo es " + str(aguinaldo_final_redondo), font=("Arial", 12), fg=light_blue, bg=bg_color)
    Aguinaldo_dinero.grid(row=6, column= 1, padx=20,pady=30)

    
    
    
    

Titulo = tk.Label(text="Aguinaldo", font=("Arial", 24), fg=light_blue, bg=bg_color)
Titulo.grid(row=1, column= 1, padx=20,pady=30)

Cl1 = DateEntry(window,selectmode = "day")
Cl1.grid (row=2, column = 0,padx=20, pady=30)

Cl2 = DateEntry(window,selectmode = "day")
Cl2.grid (row=2, column = 1,padx=20, pady=30)

b1 =tk.Button (window,text="diferencia en dias", bg="lightgreen",font=("Arial,24"),command=lambda:diferencia_en_dias())
b1.grid(row=2,column=2, padx="10",pady="10")

textogenerico = tk.Label (text="Inserte salario quincenal", font=("Arial", 14), fg=light_blue, bg=bg_color)
textogenerico.grid(row=4, column= 0, padx=20,pady=30)


salario = tk.Entry (bg="lightgreen",font=("Arial,24"))
salario.grid(row=4,column=1, padx="10",pady="10")
salario.focus()
salario.bind('<Return>', add_item)




window.mainloop()
