import pandas as pd

data = {'Nombre': ['Juan', 'María', 'Pedro'],
        'Edad': [25, 30, 35],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia']}

df = pd.DataFrame(data)
print(df)
