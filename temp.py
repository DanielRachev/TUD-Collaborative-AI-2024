import csv
import os

action_header = []
action_contents=[]
trustfile_header = []
trustfile_contents = []

unique_agent_actions = []
unique_human_actions = []
with open('./logs/exp_normal_at_time_19h-03m-12s_date_09d-03m-2025y/world_1/actions__2025-03-09_190313.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar="'")
    for row in reader:
        if action_header==[]:
            action_header=row
            continue
        if row[2:4] not in unique_agent_actions and row[2]!="":
            unique_agent_actions.append(row[2:4])
        if row[4:6] not in unique_human_actions and row[4]!="":
            unique_human_actions.append(row[4:6])
        if row[4] == 'RemoveObjectTogether' or row[4] == 'CarryObjectTogether' or row[4] == 'DropObjectTogether':
            if row[4:6] not in unique_agent_actions:
                unique_agent_actions.append(row[4:6])
        res = {action_header[i]: row[i] for i in range(len(action_header))}
        action_contents.append(res)

no_ticks = action_contents[-1]['tick_nr']
score = action_contents[-1]['score']
completeness = action_contents[-1]['completeness']
# Save the output as a csv file
print("Saving output...")
with open(os.path.join('./logs/exp_normal_at_time_19h-03m-12s_date_09d-03m-2025y/world_1/output.csv'),mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['completeness','score','no_ticks','agent_actions','human_actions'])
    csv_writer.writerow([completeness,score,no_ticks,len(unique_agent_actions),len(unique_human_actions)])