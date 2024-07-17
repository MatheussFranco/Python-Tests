import requests
import matplotlib.pyplot as plt

i=0
meses = [
    "https://asdc.larc.nasa.gov/documents/misr/plume/Global-2009_Jan/048480/Plumes_O048480-B082-SPWR02.txt",
    "https://asdc.larc.nasa.gov/documents/misr/plume/Global-2008_Feb/043247/Plumes_O043247-B058-SPWR04.txt",
    "https://asdc.larc.nasa.gov/documents/misr/plume/Global-2008_Mar/043684/Plumes_O043684-B050-SPWR02.txt",
    "https://asdc.larc.nasa.gov/documents/misr/plume/Global-2008_Apr/044078/Plumes_O044078-B073-SPWR03.txt",
    "https://asdc.larc.nasa.gov/documents/misr/plume/Global-2008_May/044523/Plumes_O044523-B074-SPWR01.txt",
    "https://asdc.larc.nasa.gov/documents/misr/plume/Global-2008_Jun/045100/Plumes_O045100-B099-SPWR02.txt",
    "https://asdc.larc.nasa.gov/documents/misr/plume/Global-2008_Jul/045434/Plumes_O045434-B103-SPWR01.txt",
    "https://asdc.larc.nasa.gov/documents/misr/plume/Global-2008_Aug/045857/Plumes_O045857-B095-SPWR05.txt",
    "https://asdc.larc.nasa.gov/documents/misr/plume/Global-2008_Sep/046309/Plumes_O046309-B094-SPWR01.txt",
    "https://asdc.larc.nasa.gov/documents/misr/plume/Global-2008_Oct/046985/Plumes_O046985-B056-SPWR02.txt",
    "https://asdc.larc.nasa.gov/documents/misr/plume/Global-2008_Nov/047202/Plumes_O047202-B064-SPWR01.txt",
    "https://asdc.larc.nasa.gov/documents/misr/plume/Global-2008_Dec/047663/Plumes_O047663-B084-SPWB05.txt"
]


# Inicialize listas para armazenar os dados
longitudes = []
latitudes = []
heat = []

for mes in meses:
    # Nome do arquivo de texto
    arquivo_txt = str(requests.get(mes).content)
    linhas = arquivo_txt.split('\\n')

    # # Ler o arquivo de texto
    # with open(arquivo_txt, "r") as arquivo:
    #     linhas = arquivo.readlines()

    # Processar cada linha do arquivo
    for linha in linhas:
        partes = linha.split(":")
        if partes[0].startswith('First point longitude'): longitudes.append(float(partes[1]))
        if partes[0].startswith('First point latitude'): latitudes.append(float(partes[1]))
        if partes[0].startswith('Total fire power (MW)'): heat.append(float(partes[1]))
    

# Exibir os dados (opcional)
for i in range(len(longitudes)):
    print(f"Longitude: {longitudes[i]}, Latitude: {latitudes[i]}, Heat: {heat[i]}")
print(len(latitudes))


# Criar um gráfico de linha4
m = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
plt.figure(figsize=(10, 6))
plt.plot(m, heat, marker='o', linestyle='-', color='b')

# Configurar rótulos e título
plt.xlabel("Mês")
plt.ylabel("Total fire power (MW)")
plt.title("Fire Risk")

# Adicionar grade
plt.grid(True)

# Exibir o gráfico
plt.tight_layout()
plt.show()


