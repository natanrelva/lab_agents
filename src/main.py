import os
import getpass
from dotenv import load_dotenv


from IPython.display import Image
from PIL import Image as PILImage
from io import BytesIO

# Carrega variáveis do .env
load_dotenv()

from graph import graphChatBot


# Função para pedir variáveis ausentes (ex: API KEY)
def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


# Solicita TAVILY_API_KEY se não estiver setada
_set_env("TAVILY_API_KEY")

# Gera e mostra o gráfico
try:
    graph = graphChatBot.get_graph()
    png_bytes = graph.draw_mermaid_png()

    # Salva imagem
    with open("grafo.png", "wb") as f:
        f.write(png_bytes)

    # Exibe imagem usando visualizador padrão do sistema
    img = PILImage.open(BytesIO(png_bytes))
    img.show()

except Exception as e:
    print(f"Erro ao gerar ou mostrar gráfico: {e}")
