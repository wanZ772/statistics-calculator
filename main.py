from os import system
system('cls')
print('''
  _________ __          __  .__          __  .__               
 /   _____//  |______ _/  |_|__| _______/  |_|__| ____   ______
 \_____  \\   __\__  \\   __\  |/  ___/\   __\  |/ ___\ /  ___/
 /        \|  |  / __ \|  | |  |\___ \  |  | |  \  \___ \___ \ 
/_______  /|__| (____  /__| |__/____  > |__| |__|\___  >____  >
        \/           \/             \/               \/     \/ 
      ''')
print("Coded by wanz\n\nUser space for each data\nPress Enter to calculate data")
# data = []
sorted_data = []
raw_data = input("Data: ")
data = raw_data.split(" ")
# while True:
#     raw_data = input("Enter data: ")
#     if (raw_data != ""):
#         data.append(int(raw_data))
#     else:
#         break

for i in data:
    sorted_data.append(int(i))

system('cls')
mean = 0
# median = 0
for i in data:
    mean = mean + int(i)
mean = mean / len(data)


sort_order = sorted(sorted_data)
position = int((len(data) - 1) / 2)
quartile = []
if (position % 2 != 0):
   median = (sort_order[position] + sort_order[position + 1]) / 2
else:
    median = sort_order[position]

percentile = [.25,.5,.75]
for i in range(3):
    try:
        q_position = (len(sort_order) + 1) * (percentile[i])
        if (q_position % 2 == 0):
            quartile.append(float(sort_order[int(q_position - 1)]))
        else:
            quartile.append(float(((sort_order[int(q_position)] + sort_order[int(q_position)]) / 2)))
    except:
        pass
mode = 1


for i in sort_order:
    if (sort_order.count(i) > mode):
        mode = i

# upper_fence = 0
# lower_fence = 0
lower_fence = quartile[0] - 1.5 * (quartile[2] - quartile[0]) 
upper_fence = quartile[2] + 1.5 * (quartile[2] - quartile[0]) 


print('''
Raw data:           {}
Sorted order:       {}
Mean:               {}
Median:             {}
Mode:               {}
1st Quartile:       {}
2nd Quartile:       {}
3rd Quartile:       {}
Maximum:            {}
Minium:             {}
Upper Fence:        {}
Lower Fence:        {}
      '''.format(sorted_data,sorted(data),
                 mean,median,
                mode,
                quartile[0],quartile[1],quartile[2],max(sort_order), min(sort_order), upper_fence, lower_fence
                 ))