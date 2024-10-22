import kagglehub

# Download latest version
path = kagglehub.dataset_download("mashijie/eating-sound-collection")

print("Path to dataset files:", path)