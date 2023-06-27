import os

dirc = "C:\\Users\\Djoin\\Documents\\djoin-job-desk\\etl-core\\scripts"

dir_list = []
for root, dirs, files in os.walk(dirc):
    dir_list.append(root)


all_link = []


for i in dir_list[1:]:
    for d in os.listdir(i):
        if d.endswith(".py"):
            all_link.append(os.path.join(i, d))
