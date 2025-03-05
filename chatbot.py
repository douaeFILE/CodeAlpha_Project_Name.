import tkinter as tk
from PIL import Image, ImageTk

# Dictionnaire des réponses
reponses = {
    "bonjour": "Bonjour ! Comment puis-je vous aider ? 😊",
    "comment ça va": "Je suis un programme, donc je vais toujours bien ! Et vous ?",
    "au revoir": "À bientôt ! Passez une excellente journée ! 👋",
    "qui es-tu": "Je suis un chatbot simple créé avec Python et Tkinter.",
    "heure": "Je ne peux pas voir l'heure, mais tu peux vérifier sur ton téléphone ! 📱",
    "merci": "Avec plaisir ! 😊",
}

# Fonction pour générer une réponse intelligente
def repondre():
    user_input = entree.get().strip().lower()  # Convertir en minuscule et supprimer les espaces
    if not user_input:
        return  # Ne rien faire si l'entrée est vide

    # Chercher la réponse correspondant à l'entrée
    reponse = reponses.get(user_input, "Désolé, je ne comprends pas. 😕")

    # Afficher la conversation dans le chatbox avec le nom personnalisé
    chatbox.config(state=tk.NORMAL)  # Activer l'édition temporairement
    if nom_utilisateur.get().strip():  # Si un nom est fourni
        nom = nom_utilisateur.get().strip()
        chatbox.insert(tk.END, f"{nom}: " + user_input + "\n", "user")
        chatbox.insert(tk.END, f"Chatbot: " + reponse + "\n", "bot")
    else:
        chatbox.insert(tk.END, "Vous: " + user_input + "\n", "user")
        chatbox.insert(tk.END, "Chatbot: " + reponse + "\n", "bot")
    chatbox.config(state=tk.DISABLED)  # Désactiver l'édition
    chatbox.yview(tk.END)  # Faire défiler vers le bas

    entree.delete(0, tk.END)  # Effacer l'entrée utilisateur

# Création de la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Chatbot Tkinter")
fenetre.geometry("400x600")
fenetre.configure(bg="#87CEEB")  # Bleu ciel

# Charger l'image (avec gestion des erreurs)
chemin_image = r"C:\Users\hp\Desktop\chatbot.png"
try:
    image = Image.open(chemin_image)
    image = image.resize((100, 100))  # Redimensionner si nécessaire
    photo = ImageTk.PhotoImage(image)
    label_image = tk.Label(fenetre, image=photo, bg="#87CEEB")
    label_image.pack(pady=10)
except Exception as e:
    print(f"Erreur lors du chargement de l'image : {e}")

# Titre encadré en haut
titre = tk.Label(fenetre, text="💬 Chatbot", font=("Arial", 16, "bold"), bg="white", fg="black", relief="solid", padx=10, pady=5)
titre.pack(pady=5)

# Champ pour entrer le nom
label_nom = tk.Label(fenetre, text="Entrez votre nom:", font=("Arial", 12), bg="#87CEEB", fg="black")
label_nom.pack(pady=5)

nom_utilisateur = tk.Entry(fenetre, width=40, bg="white", fg="black", font=("Arial", 12))
nom_utilisateur.pack(pady=5)

# Zone d'affichage des messages (Chatbox)
chatbox = tk.Text(fenetre, height=18, width=50, bg="white", fg="black", state=tk.DISABLED)
chatbox.pack(pady=10)

# Ajouter des tags pour le style des messages
chatbox.tag_configure("user", foreground="blue")
chatbox.tag_configure("bot", foreground="green")

# Champ de saisie de la question (rose)
entree = tk.Entry(fenetre, width=40, bg="pink", fg="black", font=("Arial", 12))
entree.pack(pady=5)

# Bouton d'envoi
bouton_envoyer = tk.Button(fenetre, text="Envoyer", command=repondre, bg="white", fg="black", font=("Arial", 12, "bold"))
bouton_envoyer.pack(pady=5)

# Fonction pour saluer l'utilisateur une fois qu'il entre son nom
def saluer_utilisateur():
    nom = nom_utilisateur.get().strip()
    if nom:  # Si un nom est fourni
        chatbox.config(state=tk.NORMAL)  # Activer l'édition temporairement
        chatbox.insert(tk.END, f"Chatbot: Bonjour {nom} ! Comment puis-je vous aider aujourd'hui ? 😊\n", "bot")
        chatbox.config(state=tk.DISABLED)  # Désactiver l'édition
        chatbox.yview(tk.END)  # Faire défiler vers le bas
    else:
        chatbox.insert(tk.END, "Chatbot: Veuillez entrer un nom valide. 😕\n", "bot")
        chatbox.yview(tk.END)  # Faire défiler vers le bas

# Bouton pour saluer l'utilisateur
saluer_bouton = tk.Button(fenetre, text="Se présenter", command=saluer_utilisateur, bg="white", fg="black", font=("Arial", 12, "bold"))
saluer_bouton.pack(pady=5)

# Lancer l'interface graphique
fenetre.mainloop()

