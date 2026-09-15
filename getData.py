import pandas as pd

sheet_id = "1CK-FKgwlTuqBSP-PLbBWBEiz8Ohi0TdXlgVfVPMwNT8"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

dados = pd.read_csv(url)
print(dados.head())

dados["id_formulario"] = range(1, len(dados) + 1)

def converter_dados(usuarios: dict):
    return {
        "Nome": usuarios["Nome"],
        "Data_registro": usuarios["Carimbo de data/hora"]
    }
    
    
for inicio in range(0, len(dados), 500):
    lote = dados.iloc[inicio:inicio + 500]

    usuarios = lote.to_dict(orient="records")
    registros = [
        converter_dados(usuario) 
        for usuario in usuarios
    ]
    print(registros)


