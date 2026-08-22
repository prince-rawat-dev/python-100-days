# install pakage "requests" in venv1 environment
# now we will activate and use installed pakage "requests"
import requests

response = requests.get("https://example.com")

print("Status Code:",response.status_code)

# in terminal -> New terminal :-
# inside (venv1) and (day_35), if you installed any pakage(like requests) and then use that in this program and if its show error like 
# (module not found error) then go (ctrl + shift + P) and search there (Python: Select Interpreter) and select that interpreter who has this path -
# (Day_35\venv1\Scripts\python.exe) select that then your run button and terminal run command will give corect result like (Status Code: 200)