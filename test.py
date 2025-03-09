import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    "run 1 - never trust": [6818, 425, 317],
    "run 2 - always trust": [5911, 317, 258],
    "run 3 - random trust": [7447, 319, 314],
    "run 4 - normal": [6572, 404, 284],
}

# Extract labels and data
labels = list(data.keys())
time_passed = [data[label][0] for label in labels]
agent_actions = [data[label][1] for label in labels]
human_actions = [data[label][2] for label in labels]

# Variable names and corresponding data
variables = ['Time Passed', 'Agent Actions', 'Human Actions']
values = [time_passed, agent_actions, human_actions]

# Colors for each run type
colors = ['skyblue', 'salmon', 'lightgreen', 'mediumpurple']  # One color per run

# Bar width
bar_width = 0.2

# Create the plot
plt.figure(figsize=(14, 7))

# Loop through each variable (Time Passed, Agent Actions, Human Actions)
for i, (variable, value_list) in enumerate(zip(variables, values)):
    # Calculate the x-positions for the bars within each group
    #   - i * (len(labels) * bar_width + gap):  Shifts the group to the right for each variable
    #   - np.arange(len(labels)) * bar_width: Spaces the bars within the group
    gap = 1  # Increase gap for more separation between variable groups
    r = [j * bar_width + i * (len(labels) * bar_width + gap) for j in range(len(labels))]

    # Create the bars for each run type within the current variable group
    for j, val in enumerate(value_list):
        plt.bar(r[j], val, color=colors[j], width=bar_width, label=labels[j] if i == 0 else "", edgecolor='grey')  # Only label the first set
        plt.text(r[j], val + 50, str(val), ha='center', fontsize=9)

# X-axis labels and ticks
# Calculate the center position for each variable group's label
x_ticks_pos = [
    (len(labels) * bar_width + gap) / 2 - bar_width/2  + i * (len(labels) * bar_width + gap)
     for i in range(len(variables))
]
plt.xticks(x_ticks_pos, variables, fontweight='bold')
plt.xlabel('Variable', fontweight='bold')

# Y-axis label and title
plt.ylabel('Values', fontweight='bold')
plt.title('Comparison of Run Types (Grouped by Run)', fontweight='bold')

# Legend (only show once, for the run types)
handles, labels_unique = plt.gca().get_legend_handles_labels() #get all labels
by_label = dict(zip(labels_unique, handles)) #remove duplicated
plt.legend(by_label.values(), by_label.keys())


plt.tight_layout()
plt.savefig("ben_stat_comparisons.png")