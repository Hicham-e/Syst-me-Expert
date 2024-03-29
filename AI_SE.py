import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk

# Définir les listes de symptômes et diagnostics
symptoms = []
diagnostics = {}

# Définir username et mot de passe pour la session expert
expert_username = "admin"
expert_password = "admin"

# Charger les données à partir d'un fichier
def load_data():
    with open("data.txt", "r") as file:
        for line in file:
            symptom, diagnosis = line.strip().split(":")
            symptoms.append(symptom)
            diagnostics[symptom] = diagnosis

# Enregistrer les données dans un fichier
def save_data():
    with open("data.txt", "w") as file:
        for symptom, diagnosis in diagnostics.items():
            file.write(f"{symptom}:{diagnosis}\n")

# Inférer le diagnostic pour un symptôme
def infer_diagnosis(symptom):
    if symptom in diagnostics:
        return diagnostics[symptom]
    return "Aucun diagnostic trouvé"

# Supprimer un symptôme
def remove_symptom():
    symptom_to_remove = combo_symptoms.get()
    if symptom_to_remove in symptoms:
        symptoms.remove(symptom_to_remove)
        del diagnostics[symptom_to_remove]
        save_data()  # Enregistrer les données dans un fichier
        messagebox.showinfo("Confirmation", "Symptôme supprimé avec succès.")
        combo_symptoms['values'] = symptoms  # Mettre à jour les valeurs dans la combobox
    else:
        messagebox.showerror("Erreur", "Symptôme non trouvé.")

# Ajouter un nouveau symptôme
def add_symptom():
    def save_symptom():
        new_symptom = entry_new_symptom.get()
        new_diagnosis = entry_new_diagnosis.get()
        if new_symptom and new_diagnosis:
            symptoms.append(new_symptom)
            diagnostics[new_symptom] = new_diagnosis
            save_data()  # Enregistrer les données dans un fichier
            combo_symptoms['values'] = symptoms  # Mettre à jour les valeurs dans la combobox
            messagebox.showinfo("Confirmation", "Symptôme ajouté avec succès.")
            add_window.destroy()
        else:
            messagebox.showerror("Erreur", "Veuillez entrer à la fois un symptôme et un diagnostic.")

    add_window = tk.Toplevel(root)
    add_window.title("Ajouter un symptôme")
    add_window.geometry("300x150")
    add_window.configure(background="#f0f0f0")

    label_new_symptom = tk.Label(add_window, text="Nouveau symptôme:", background="#f0f0f0")
    label_new_symptom.pack()

    entry_new_symptom = ttk.Entry(add_window, width=30)
    entry_new_symptom.pack()

    label_new_diagnosis = tk.Label(add_window, text="Diagnostic:", background="#f0f0f0")
    label_new_diagnosis.pack()

    entry_new_diagnosis = ttk.Entry(add_window, width=30)
    entry_new_diagnosis.pack()

    save_button = tk.Button(add_window, text="Enregistrer", command=save_symptom, bg="#4caf50", fg="white")  # Bouton vert
    save_button.pack()

# Session utilisateur
def user_session():
    root.title("Session utilisateur")
    root.configure(background="#f0f0f0")
    
    label_symptom = tk.Label(root, text="Sélectionnez un symptôme:", background="#f0f0f0")
    label_symptom.pack()

    global combo_symptoms

    combo_symptoms = ttk.Combobox(root, values=symptoms, width=27)
    combo_symptoms.pack()

    def diagnose():
        symptom = combo_symptoms.get()
        diagnosis = infer_diagnosis(symptom)
        messagebox.showinfo("Diagnostic", diagnosis)

    diagnose_button = tk.Button(root, text="Diagnostiquer", command=diagnose, bg="#2196f3", fg="white")  # Bouton bleu
    diagnose_button.pack()

    logout_button = tk.Button(root, text="Déconnexion", command=logout, bg="#f44336", fg="white")  # Bouton rouge
    logout_button.pack()

# Session expert
def expert_session():
    root.title("Session expert")
    root.configure(background="#f0f0f0")
    
    global combo_symptoms
    
    label_symptom = tk.Label(root, text="Sélectionnez un symptôme:", background="#f0f0f0")
    label_symptom.pack()

    combo_symptoms = ttk.Combobox(root, values=symptoms, width=27)
    combo_symptoms.pack()

    add_symptom_button = tk.Button(root, text="Ajouter un symptôme", command=add_symptom, bg="#4caf50", fg="white")  # Bouton vert
    add_symptom_button.pack()

    remove_symptom_button = tk.Button(root, text="Supprimer un symptôme", command=remove_symptom, bg="#f44336", fg="white")  # Bouton rouge
    remove_symptom_button.pack()

    logout_button = tk.Button(root, text="Déconnexion", command=logout, bg="#f44336", fg="white")  # Bouton rouge
    logout_button.pack()

# Fonction de connexion expert
def expert_login():
    def check_login():
        username = entry_username.get()
        password = entry_password.get()
        if username == expert_username and password == expert_password:
            expert_session()
            login_window.destroy()
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

    login_window = tk.Toplevel(root)
    login_window.title("Connexion expert")
    login_window.geometry("300x150")
    login_window.configure(background="#f0f0f0")

    label_username = tk.Label(login_window, text="Nom d'utilisateur:", background="#f0f0f0")
    label_username.pack()

    entry_username = ttk.Entry(login_window, width=30)
    entry_username.pack()

    label_password = tk.Label(login_window, text="Mot de passe:", background="#f0f0f0")
    label_password.pack()

    entry_password = ttk.Entry(login_window, width=30, show="*")
    entry_password.pack()

    login_button = tk.Button(login_window, text="Connexion", command=check_login, bg="#2196f3", fg="white")  # Bouton bleu
    login_button.pack()

# Fonction de connexion
def login():
    login_window = tk.Toplevel(root)
    login_window.title("Connexion")
    login_window.geometry("300x100")
    login_window.configure(background="#f0f0f0")

    label_login = tk.Label(login_window, text="Sélectionnez le type d'utilisateur:", background="#f0f0f0")
    label_login.pack()

    user_type = tk.StringVar()
    user_type.set("Utilisateur")

    user_radio = tk.Radiobutton(login_window, text="Utilisateur", variable=user_type, value="Utilisateur", background="#f0f0f0")
    user_radio.pack()
    expert_radio = tk.Radiobutton(login_window, text="Expert", variable=user_type, value="Expert", background="#f0f0f0")
    expert_radio.pack()

    login_button = tk.Button(login_window, text="Connexion", command=lambda: on_login(login_window, user_type.get()), bg="#2196f3", fg="white")  # Bouton bleu
    login_button.pack()

# Gérer la connexion
def on_login(login_window, user_type):
    login_window.destroy()
    if user_type == "Utilisateur":
        user_session()
    elif user_type == "Expert":
        expert_login()

# Fonction de déconnexion    
def logout():
    root.quit()

# Créer la fenêtre principale
def create_main_window():
    global combo_symptoms

    login_button = tk.Button(root, text="Connexion", command=login, bg="#2196f3", fg="white")  # Bouton bleu
    login_button.pack()

# Charger les données au démarrage
load_data()

# Créer une fenêtre Tkinter à thème
root = ThemedTk(theme="arc")
root.title("Diagnostic des pannes informatiques")
root.geometry("400x200")
create_main_window()
root.mainloop()
