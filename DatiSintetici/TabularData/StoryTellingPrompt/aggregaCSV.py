import pandas as pd
import glob
import os

# Percorso della cartella contenente i CSV
path = './MISTRAL/'  # Modifica con il tuo percorso

# Ottieni lista di tutti i file CSV nella cartella
all_files = glob.glob(os.path.join(path, "*.csv"))

# Lista per contenere tutti i DataFrame
df_list = []

# Leggi ogni file CSV e aggiungilo alla lista
for file in all_files:
    df = pd.read_csv(file)
    df_list.append(df)

# Concatena tutti i DataFrame
df_finale = pd.concat(df_list, ignore_index=True)

# Salva il risultato
df_finale.to_csv('Mistral_storytelling_synthetic.csv', index=False)