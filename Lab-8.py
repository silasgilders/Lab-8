
from tkinter import *
from tkinter import ttk
from webbrowser import get
from pokeapi import get_pokemon_info


def main():
    
    root = Tk()
    root.title("Pokedex")
    #I called it Pokedex because that's an ingame item that offers a GUI that provides Pokemon Info!
    root.iconbitmap('Pokedex.ico')
    #The Icon I chose is a Pokedex also, decided it suited it more considering my GUI Title


    #This section makes all of our frames
    frm_input = ttk.Frame(root)
    frm_input.grid(row=100, column=100, columnspan=2)
    
    frm_stats = ttk.LabelFrame(root, text="Stats")
    frm_stats.grid(row=200, column=200)

    frm_info = ttk.LabelFrame(root, text="Info")
    frm_info.grid(row=200, column=100, padx=0, pady=10)



    lbl_name = ttk.Label(frm_input, text="Pokemon Name:")
    lbl_name.grid(row=0, column=0, padx=10, pady=10)

    #Enables a Text Box to appear so we can specify a Pokemon
    ent_name = ttk.Entry(frm_input)
    ent_name.grid(row=0, column=1, pady=10)


    #Gets the Data of the Pokemon we specify
    def btn_get_info_click():
        name= ent_name.get()
        poke_dict = get_pokemon_info(name) 
        if poke_dict:
            lbl_height_val['text'] = poke_dict['height']
            
            lbl_weight_val['text'] = poke_dict['weight']


            types_list = [t['type']['name']for t in poke_dict['types']]
            lbl_type_val['text'] = ', '.join(types_list)
            prg_hp['value'] = poke_dict['stats'][0]['base_stat'] 
            prg_atk['value'] = poke_dict['stats'][1]['base_stat']
            prg_def['value'] = poke_dict['stats'][2]['base_stat']
            prg_spatk['value'] = poke_dict['stats'][3]['base_stat']
            prg_spdef['value'] = poke_dict['stats'][4]['base_stat']
            prg_spd['value'] = poke_dict['stats'][5]['base_stat']


    btn_get_info = ttk.Button(frm_input, text="Get Info", command=btn_get_info_click)
    btn_get_info.grid(row=0, column=2, padx=10, pady=10)


    #Fills out our stats 
    lbl_hp = ttk.Label(frm_stats, text= "HP:")
    lbl_hp.grid(row=100, column= 100, padx=5, pady=5, sticky=E)
    prg_hp = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_hp.grid(row=100, column= 200, padx=5, pady=5)

    lbl_atk = ttk.Label(frm_stats, text= "Attack:")
    lbl_atk.grid(row=200, column= 100, padx=5, pady=5, sticky=E)
    prg_atk = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_atk.grid(row=200, column= 200, padx=5, pady=5)

    lbl_def = ttk.Label(frm_stats, text= "Defence:")
    lbl_def.grid(row=300, column= 100, padx=5, pady=5, sticky=E)
    prg_def = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_def.grid(row=300, column= 200, padx=5, pady=5)

    #Special Attack: Damage dealt by "Special" moves, such as Acid and Aura Sphere
    lbl_spatk = ttk.Label(frm_stats, text= "Special Attack:")
    lbl_spatk.grid(row=400, column= 100, padx=5, pady=5, sticky=E)
    prg_spatk = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_spatk.grid(row=400, column= 200, padx=5, pady=5)

    #Special Defence: Defence against "Special" moves, typically things like Thunderbolt or Flamethrower
    lbl_spdef = ttk.Label(frm_stats, text= "Special Defence:")
    lbl_spdef.grid(row=500, column= 100, padx=5, pady=5, sticky=E)
    prg_spdef = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_spdef.grid(row=500, column= 200, padx=5, pady=5)

    #Speed: Defines the Turn Order of a battle, the Pokemon with a higher speed will go first, unless moves such a Quick Attack are used.
    lbl_spd = ttk.Label(frm_stats, text= "Speed:")
    lbl_spd.grid(row=600, column= 100, padx=5, pady=5, sticky=E)
    prg_spd = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_spd.grid(row=600, column= 200, padx=5, pady=5)

    #Adds info to the, you guessed it, Info frame
    lbl_height= ttk.Label(frm_info, text= "Height:")
    lbl_height.grid(row=100, column=100, padx=10, pady=(10,0), sticky=E)
    lbl_height_val= ttk.Label(frm_info, text= "TBD")
    lbl_height_val.grid(row=100, column=200, padx=10, pady=(10,0), sticky=W)

    lbl_weight= ttk.Label(frm_info, text= "Weight:")
    lbl_weight.grid(row=200, column=100, padx=10, pady=(10,0), sticky=E)
    lbl_weight_val= ttk.Label(frm_info, text= "TBD")
    lbl_weight_val.grid(row=200, column=200, padx=10, pady=(10,0), sticky=W)


    lbl_type= ttk.Label(frm_info, text= "Type:")
    lbl_type.grid(row=300, column=100, padx=10, pady=10, sticky=E)
    lbl_type_val= ttk.Label(frm_info, text= "TBD")
    lbl_type_val.grid(row=300, column=200, padx=10, pady=10, sticky=W)
    




    





    root.mainloop()

main()