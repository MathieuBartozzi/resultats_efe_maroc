# import streamlit as st

# import hashlib

# # Domaine autorisé pour l'accès
# domaine_authorisé = "@mlfmonde.org"

# # Récupérer le mot de passe commun depuis secrets.toml
# mot_de_passe_commun = st.secrets["mot_de_passe_commun"]

# # Fonction pour hacher le mot de passe
# def hacher_mot_de_passe(mot_de_passe):
#     return hashlib.sha256(mot_de_passe.encode()).hexdigest()

# # Initialiser la variable de session pour l'état de connexion
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# # Fonction de connexion
# def login():
#     st.title("Connexion à l'application")

#     email = st.text_input("Adresse e-mail")
#     mot_de_passe = st.text_input("Mot de passe", type="password")

#     if st.button("Se connecter"):
#         if email.endswith(domaine_authorisé) and hacher_mot_de_passe(mot_de_passe) == hacher_mot_de_passe(mot_de_passe_commun):
#             st.session_state.logged_in = True
#             st.success("Connexion réussie ! Utilisez le menu pour naviguer.")
#             st.rerun()
#         else:
#             st.error("Adresse e-mail ou mot de passe incorrect.")

# # Définir les pages de l'application
# pages = [
#     st.Page(page="pages/dashboard.py", title="Dashboard", icon="📊"),
#     st.Page(page="pages/alerts.py", title="Alertes Système", icon="🚨"),
#     st.Page(page="pages/bugs.py", title="Rapports de Bugs", icon="🐞"),
#     st.Page(page="pages/search.py", title="Recherche", icon="🔍"),
#     st.Page(page="pages/history.py", title="Historique", icon="🕒")
# ]

# # Vérification de l'état de connexion
# if not st.session_state.logged_in:
#     login()
# else:
#     # Ajouter les pages à la navigation dans la barre latérale
#     pg = st.navigation(pages, position="sidebar")

#     # Exécuter l'application
#     pg.run()

#     # Bouton de déconnexion
#     if st.sidebar.button("Déconnexion"):
#         st.session_state.logged_in = False
#         st.rerun()


import streamlit as st

# Définir les pages de l'application
pages = [
    st.Page(page="mes_pages/ACCUEIL.py", title="ACCUEIL",icon=":material/school:"),
    st.Page(page="mes_pages/DNB.py", title="DNB",icon=":material/add_circle:"),
    st.Page(page="mes_pages/EAF.py", title="EAF",icon=":material/add_circle:"),
    st.Page(page="mes_pages/BAC.py", title="BAC",icon=":material/add_circle:"),
]

# Ajouter les pages à la navigation dans la barre latérale
pg = st.navigation(pages, position="sidebar")

# Exécuter l'application
pg.run()
