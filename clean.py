import pandas as pd

# Lege hier die Dateinamen fest.
# Stelle sicher, dass die Eingabedatei im selben Ordner wie das Skript liegt.
input_filename = 'protonpass_export.csv'
output_filename = 'protonpass_export_cleaned.csv'

try:
    # 1. CSV-Datei einlesen
    # Pandas liest die Daten in eine Tabelle, einen sogenannten DataFrame.
    df = pd.read_csv(input_filename)
    
    print(f"Datei '{input_filename}' wurde geladen.")
    print(f"Anzahl der Zeilen vor der Bereinigung: {len(df)}")
    
    # 2. Duplikate entfernen
    # drop_duplicates() entfernt alle Zeilen, die in allen Spalten identische Werte haben.
    # Um Duplikate nur anhand bestimmter Spalten zu finden (z.B. 'name' und 'username'),
    df_cleaned = df.drop_duplicates(subset=['name', 'username', 'url'])
    
    # 3. Bereinigte Daten in eine neue CSV-Datei schreiben
    # index=False verhindert, dass Pandas eine zusätzliche Spalte mit Zeilennummern hinzufügt.
    df_cleaned.to_csv(output_filename, index=False)
    
    print(f"Anzahl der Zeilen nach der Bereinigung: {len(df_cleaned)}")
    print(f"Die bereinigten Daten wurden in '{output_filename}' gespeichert. ✅")
    
except FileNotFoundError:
    print(f"FEHLER: Die Datei '{input_filename}' konnte nicht gefunden werden.")
    print("Bitte überprüfe, ob der Dateiname korrekt ist und die Datei sich im richtigen Ordner befindet.")

except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")