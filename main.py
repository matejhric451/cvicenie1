import tkinter as tk
import random

# Zoznam slov
words = ["jablko", "strom", "rieka", "auto", "dom", "pes", "mačka", "slovensko", "práca", "škola", "hra", "hudba"]

def generate_sentences():
    sentences = []
    for _ in range(5):  # 5 náhodných viet
        sentence_length = random.randint(3, 6)  # Dĺžka vety od 3 do 6 slov
        selected_words = random.sample(words, sentence_length)  # Náhodný výber slov
        sentence = " ".join(selected_words).capitalize() + "."  # Formátovanie vety
        sentences.append(sentence)
    result_text.set("\n".join(sentences))  # Zobrazenie viet v GUI

# Vytvorenie GUI
root = tk.Tk()
root.title("Generátor viet")
root.geometry("400x300")

# Popis
description = tk.Label(root, text="Klikni na tlačidlo pre generovanie viet:", font=("Arial", 12))
description.pack(pady=10)

# Tlačidlo na generovanie viet
generate_button = tk.Button(root, text="Generovať vety", command=generate_sentences, font=("Arial", 12))
generate_button.pack(pady=10)

description = tk.Label(root, text="Matej Hric", font=("Arial", 12))
description.pack(pady=10)

# Výsledok (vety)
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=350, font=("Arial", 12))
result_label.pack(pady=10)

# Spustenie aplikácie
root.mainloop()
