import pandas as pd
import streamlit as st
import locale

# Initialiser la locale pour gérer le format des nombres
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Ajustez en fonction de votre locale

# Récupérer l'ID du fichier Google Sheets depuis le fichier secrets.toml
file_id = st.secrets["google_sheets"]["file_id"]

# Fonction pour transformer les colonnes d'un DataFrame
def format_dataframe(df):

    # Supprimer les virgules de la colonne 'session' en forçant le type en str, puis convertir en années (int)
    if 'session' in df.columns:
        df['session'] = df['session'].astype(str).str.replace(',', '').astype(int)

    # Convertir la colonne 'etablissements' en chaîne de caractères (str)
    if 'établissements' in df.columns:
        df['établissement'] = df['établissement'].astype(str)

    # Convertir toutes les autres colonnes en float si possible
    for col in df.columns:
        if col not in ['session', 'établissement','spécialité']:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df

# Fonction pour formater les données pour l'affichage sans séparateurs de milliers
def format_for_display(df):
    df_display = df.copy()
    if 'session' in df_display.columns:
        # Convertir les valeurs en chaînes sans séparateurs de milliers pour l'affichage
        df_display['session'] = df_display['session'].apply(lambda x: locale.format_string('%.0f', x, grouping=False))
    return df_display

def display():
    st.title("Bonjour")
    st.write("Bienvenue à l'accueil !")

    try:
        # Dictionnaire des onglets avec leurs gIDs
        sheets = {
            "eds": "455744397",
            "philosophie": "776936543",
            "eaf": "1206285985",
            "dnb": "1644783757",
            "go": "1814626375"
        }

        # Charger chaque onglet dans un DataFrame et appliquer la fonction de formatage
        dataframes = {}
        for sheet_name, gid in sheets.items():
            url = f"https://docs.google.com/spreadsheets/d/{file_id}/export?format=csv&gid={gid}"
            df = pd.read_csv(url)

            # Appliquer la fonction de formatage
            df = format_dataframe(df)
            dataframes[sheet_name] = df

            # Appliquer un formatage pour l'affichage sans séparateurs de milliers
            df_display = format_for_display(df)

            st.write(f"Données transformées de l'onglet '{sheet_name}':")
            st.dataframe(df_display)

    except Exception as e:
        st.error("Erreur lors du chargement des données.")
        st.text(str(e))

    return dataframes

# Exécuter la page principale et obtenir le dictionnaire de DataFrames
dataframes = display()

# Stocker les DataFrames dans st.session_state pour les rendre accessibles ailleurs
st.session_state['philosophie'] = dataframes['philosophie']
st.session_state['eds'] = dataframes['eds']
st.session_state['go'] = dataframes['go']
st.session_state['dnb'] = dataframes['dnb']
st.session_state['eaf'] = dataframes['eaf']


# Exemple d'utilisation des DataFrames en dehors de la fonction display()
st.write("Exemple de DataFrame 'eds' après transformation, prêt pour les opérations :")
st.dataframe(dataframes["eds"])  # Utilisez dataframes['eds'] pour effectuer des calculs ou autres opérations
