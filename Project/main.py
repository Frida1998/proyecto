# importar la libreria nltk
import nltk

front = nltk.FreqDist(nltk.corpus.stopwords.words('spanish'))
nltk.download('sporwords')

# definir la ruta donde se almacenaran los datos descargados de nltk
nltk.data.path.append('C:/Users/Alba Suaréz/AppData/Roaming/nltk_data')


