import kagglehub
import os

# Download latest version
path = kagglehub.dataset_download("mashijie/eating-sound-collection")

print("Path to dataset files:", path)

kagglehub.dataset_download('bricevergnou/spotify-recommendation', path='data.csv')
