import requests

url = "https://raw.githubusercontent.com/KingAbdulRehman/TestPythonImport/refs/heads/main/test.py";

responce = requests.get(url)
if(responce.status_code == 200):
    exec(responce.text)

    print(getName())

else:
    print("Error")
