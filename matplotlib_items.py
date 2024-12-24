import pandas as pd
import matplotlib.pyplot as plt
from function import rotation_3d

df = pd.read_csv('data/user_behavior_dataset.csv')
colors = [
    'darkturquoise', 'khaki', 'orangered', 'yellowgreen', 'gold',
    'olivedrab', 'mediumspringgreen', 'deepskyblue', 'crimson', 'yellow'
]
users = df['User ID']
device = df['Device Model']
OS = df['Operating System']
app_us = df['App Usage Time (min/day)']
screen = df['Screen On Time (hours/day)']
battery = df['Battery Drain (mAh/day)']
num_app = df['Number of Apps Installed']
data_us = df['Data Usage (MB/day)']
age = df['Age']
gender = df['Gender']
UBC = df['User Behavior Class']

# fig1 = plt.figure(figsize=(8, 5), dpi=80)
# plt.bar(
#     device[:10],
#     data_us[:10],
#     color='deepskyblue',
#     width=0.58,
# )
# plt.title('Using data in models', fontsize=16)
# plt.xlabel('Device Model')
# plt.ylabel('Data Usage (MB/day)')
# plt.show()
#
# fig2 = plt.figure(figsize=(10, 4), dpi=80)
# plt.plot(users[:10], age[:10], color='lime')
# plt.scatter(users[:10], age[:10], color='magenta')
# plt.title('Age of users', fontsize=16)
# plt.xlabel('User ID')
# plt.ylabel('Age')
# plt.show()
#
# fig3, ax1 = plt.subplots(figsize=(9, 7), dpi=80)
# ax1.pie(
#     data_us[:3],
#     colors=colors,
#     autopct='%1.1f%%',
#     pctdistance=0.67,
#     explode=(0, 0, 0.25),
#     radius=0.7
#)
# ax1.legend(device[:3], title='Device Model', loc="lower left")
# plt.title('Using data in models', fontsize=16)
# plt.show()

# fig4 = plt.scatter(age, screen, c=age, alpha=0.58)
# plt.xlabel('Age')
# plt.ylabel('Screen On Time (hours/day)')
# plt.title('Screen Time by Age', fontsize=16)
# plt.show()

fig5 = plt.figure(figsize=(8, 7), dpi=100)
ax2 = fig5.add_subplot(projection='3d')
ax2.scatter(age, UBC, users, c=age, alpha=0.58)
ax2.set_xlabel('Age')
ax2.set_ylabel('User Behavior Class')
ax2.set_zlabel('User ID')
plt.title('User Behavior Class by Age', fontsize=16)
rotation_3d(ax2)

