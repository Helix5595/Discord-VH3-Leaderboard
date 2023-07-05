import glob
import json

Num_of_rank_displayed = 3

def vaultLevel(json_data):
    # define the ranking criteria here
    return json_data["vaultLevel"]

def completed(json_data):
    # define the ranking criteria here
    return json_data["completed"]

def totalVaults(json_data):
    # define the ranking criteria here
    return (json_data["completed"] + json_data["survived"] + json_data["failed"])

x = open("leaderboard_results.txt", "w")

folder_path = "playerSnapshots"
json_files = glob.glob(folder_path + "/*.json")

# load all json files into a list of directories
json_data_list = []
for json_file in json_files:
    with open(json_file, "r") as f:
        json_data = json.load(f)
        json_data["filename"] = json_file
        try:
            tmp = json_data["vaultLevel"]
            tmp = json_data["completed"]
            tmp = json_data["survived"]
            tmp = json_data["failed"]
        except KeyError:
            json_data["vaultLevel"] = 0
            json_data["completed"] = 0
            json_data["survived"] = 0
            json_data["failed"] = 0
        json_data_list.append(json_data)

# compare the json to the other jsons
for i, json_data in enumerate(json_data_list):
    json_data_list[i]["score"] = 0
    for other_json_data in json_data_list:
        if json_data != other_json_data:
            # Compare json_data to other_json_data and update score accordingly
            # You can customize the comparison logic here
            json_data_list[i]["score"] += 1

# rank the jsons based on the ranking criteria
json_data_list.sort(key=vaultLevel, reverse=True)

x.write("**__Vault Leader Board__**\n\n\n")
x.write("**__Vault Level__**\n")
x.write("```\n")

rank = 1
for i in range(len(json_data_list)):
    json_filename = json_data_list[i]["playerNickname"]
    json_score = json_data_list[i]["vaultLevel"]
    if json_score == 100:
        continue # Skip this dictionary and move on to the next one
    while i > 0 and json_data_list[i-1]["vaultLevel"] == json_score:
        i -= 1
        rank -= 1 # Decrement the rank until we find the next unique vaultLevel
    if rank == Num_of_rank_displayed + 1:
        break
    x.write(f"Rank {rank}: {json_filename} --> vaultLevel: {json_score}\n")
    rank += 1 # Increment the rank for the next player

x.write("```")
x.write("\n\n")
x.write("**__Vaults Completed__**")
x.write("\n")
x.write("```\n")

json_data_list.sort(key=completed, reverse=True)

rank = 1
for i in range(len(json_data_list)):
    json_filename = json_data_list[i]["playerNickname"]
    json_score = json_data_list[i]["completed"]
    while i > 0 and json_data_list[i-1]["completed"] == json_score:
        i -= 1
        rank -= 1 # Decrement the rank until we find the next unique vaultLevel
    if rank == Num_of_rank_displayed + 1:
        break
    x.write(f"Rank {rank}: {json_filename} --> Completed: {json_score}\n")
    rank += 1 # Increment the rank for the next player

x.write("```")
x.write("\n\n")
x.write("**__Total Vaults Ran__**")
x.write("\n")
x.write("```\n")

json_data_list.sort(key=totalVaults, reverse=True)

rank = 1
for i in range(len(json_data_list)):
    json_filename = json_data_list[i]["playerNickname"]
    json_score = json_data_list[i]["completed"] + json_data_list[i]["survived"] + json_data_list[i]["failed"]
    while i > 0 and json_data_list[i-1]["completed"] + json_data_list[i-1]["survived"] + json_data_list[i-1]["failed"] == json_score:
        i -= 1
        rank -= 1 # Decrement the rank until we find the next unique vaultLevel
    if rank == Num_of_rank_displayed + 1:
        break
    x.write(f"Rank {rank}: {json_filename} --> Total Vaults: {json_score}\n")
    rank += 1 # Increment the rank for the next player

x.write("```")
x.write("\n\n")
x.write("=========== **__Level 100 club__** ===========")
x.write("\n")
x.write("```\n")

for i in range(len(json_data_list)):
    json_filename = json_data_list[i]["playerNickname"]
    json_score = json_data_list[i]["vaultLevel"]
    if i > 0 and json_score == 100:
        x.write(f"{json_filename}\n")

x.write("```")