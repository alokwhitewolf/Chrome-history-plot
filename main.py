import os



data_path = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default" #path to user's history database (Chrome)
files = os.listdir(data_path)

history_db = os.path.join(data_path, 'history')