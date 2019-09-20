# ScamperWang
The internet of spiders

Deep Learning classifier built with fast.ai and PyTorch to recognise 8 species of spider

* House spider (Tegenaria domestica)
* Giant House spider (Eratigena atrica)
* Zebra Spider (Salticus scenicus)
* Sector Spider (Zygiella x-notata)
* Cellar Spider (Pholcidae)
* Cucumber Spider (Araniella cucurbitina)
* Cross Orb Weaver (Araneus diadematus)
* False Widow (Steatoda nobilis)

The server is a Starlette rest server written in python.
The architecture is Resnet50 and was trained using this Jupyter notebook on a Colab GPU: https://github.com/peetdenny/FastAI/blob/master/ScamperWang.ipynb

## Prerequisites 
You should have Python 3 installed with pip.
And then run
```
pip install uvicorn
pip install fastai
pip install aiohttp
pip install aiofiles
pip install python-multipart
```

## Running the server
```
python server.py serve
```

Then point your brower at http://localhost:8008 and upload a photo of a spider!