import os
import glob
import json
import subprocess

root_directory = "C:\\Users\\Djoin\\Documents\\djoin-job-desk\\etl-core\\scripts"

all_list = []


def get_files_in_directory(rootdir, folder):
    join_folder = os.path.join(rootdir, folder)
    for file_path in glob.glob(os.path.join(join_folder, "*"), recursive=True):
        if os.path.isfile(file_path):
            all_list.append(file_path)


def run_sub(list_data_run):
    for run_py in list_data_run:
        try:
            subprocess.run(["python", run_py], check=True)
            monitoring_run[run_py] = "[SUCCESS]"
        except Exception as e:
            print(f"there is an error {str(e)}")
            monitoring_run[run_py] = f"[FAILED] : {str(e)}"

    with open("monitoring.json", "w") as outfile:
        json.dump(monitoring_run, outfile)


list_sub_folder = [
    "accounting",
    "admin-log-operation",
    "bank-transfer",
    "deposit",
    "employee",
    "loan",
    "log-operation",
    "members",
    "notifikasi",
    "ppob",
    "saving",
]

for sub_list in list_sub_folder:
    get_files_in_directory(root_directory, sub_list)

try:
    f = open("./monitoring.json")
    monitoring = json.load(f)
except:
    monitoring = {}


monitoring_run = {}
if len(monitoring) == 0:
    run_sub(all_list)
else:
    get_list_failed = [key for key in monitoring.keys() if monitoring[key] != "[SUCCESS]"]
    if len(get_list_failed) == 0:
        print("all running success")
    else:
        run_sub(get_list_failed)
