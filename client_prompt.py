import requests

print('''
##################################################################################################################
#                                                                                                                #
#                             QWEN Your local LLM. (type exit or use Ctrl-C to exit)                             #
#                                                                                                                #
##################################################################################################################
''')

def send_prompt(prompt, max_tokens=512):
    url = "http://localhost:8000/qwen"
    data = {"prompt": prompt, "max_tokens": max_tokens}

    try:
        response = requests.post(url=url, json=data)
        response.raise_for_status() # error catch
        return response.json()
    except requests.RequestException as e:
        print("API call failed" ,e)
        return None


while True:

    message = input("----> Prompt :")


    if message.lower() != "exit":

        result = send_prompt(message)

        if result:
            print("\n############################################ Response ###############################################################")

            print(f""" \n {result["response"].split("assistant")[-1]} \n """)
    else:
        break