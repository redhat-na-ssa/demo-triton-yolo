from pathlib import Path
from ultralytics import YOLO

# Load the Triton Server model
scheme = "http"
url = "triton-server-demo-triton.apps.cluster-frxkq.frxkq.sandbox213.opentlc.com"
modelname = "yolo11n"
model = YOLO(f"{scheme}://{url}/{modelname}", task="detect", verbose=True)

# Run inference on the server
image_path = Path(__file__).parent.joinpath("./pizza.png")
results = model(image_path)

print(results)