# TODO

```sh
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

curl https://www.healthyseasonalrecipes.com/wp-content/uploads/2019/12/greek-pizza-21-034.jpg > pizza.jpg

python client.py
```

```sh
podman run --rm -v /tmp/pizza.jpg:/pizza.jpg --security-opt=label=disable --entrypoint python3 docker.io/ultralytics/ultralytics:latest -c 'from ultralytics import YOLO; from pprint import pprint; pprint(YOLO("http://triton-server-demo-triton.apps.cluster-frxkq.frxkq.sandbox213.opentlc.com/yolo", task="detect", verbose=True)("/pizza.jpg"))'
```

## Links

- https://docs.ultralytics.com/guides/triton-inference-server/#exporting-yolo11-to-onnx-format
