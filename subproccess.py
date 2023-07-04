import os
import glob
import json
import subprocess

root_directory = "C:\\Users\\Djoin\\Documents\\djoin-job-desk\\etl-core\\scripts"
root = r"C:\Users\Djoin\Documents\djoin-job-desk\run-script-multiple\run"


def get_files_in_directory(root_path):
    dir_list = []
    all_path = []
    for root, dirs, files in os.walk(root_path):
        dir_list.append(root)

    for dir_ in dir_list[1:]:
        for filename in os.listdir(dir_):
            if filename.endswith(".py"):
                all_path.append(os.path.join(dir_, filename))

    return all_path


def run_sub(run_py, file_monitoring):
    try:
        subprocess.run(["python", run_py], check=True)
        file_monitoring[run_py] = "[SUCCESS]"
    except Exception as e:
        print(f"there is an error {str(e)}")
        file_monitoring[run_py] = f"[FAILED] : {str(e)}"

    print("create file")
    with open("monitoring.json", "w") as outfile:
        json.dump(file_monitoring, outfile)


all_run_sub = get_files_in_directory(root_path=root_directory)

print(all_run_sub)
retries = 0
while True:
    data = []
    filtering_run_sub = []
    try:
        with open("./monitoring.json") as f:
            monitoring = json.load(f)
    except Exception as e:
        monitoring = {}

    for path in all_run_sub:
        try:
            if monitoring[path] != "[SUCCESS]":
                filtering_run_sub.append(path)
        except:
            filtering_run_sub.append(path)

    print(filtering_run_sub)
    for run_py in filtering_run_sub:
        run_sub(run_py=run_py, file_monitoring=monitoring)

    for kunci in monitoring.keys():
        if monitoring[kunci] == "[SUCCESS]":
            data.append(True)
        else:
            data.append(False)

    if all(data) == True:
        os.remove("monitoring.json")
        break

    if retries == 3:
        break

    retries += 1
