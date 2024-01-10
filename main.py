from os import system
# from requests import post, get
# test_data = get("http://192.168.43.151:8000/data.json").json()['ParsedResults'][0]['ParsedText']
# print(test_data)

# payload = {'isOverlayRequired': 'true',
#                'apikey': 'K85363188888957',
#                'language': 'eng',
#                }
# with open('test.png', 'rb') as f:
#     r = post('https://api.ocr.space/parse/image',
#                         files={'test.png': f},
#                         data=payload,
#                         )
#     print(r.content.decode())
# exit()
system('cls')
main_banner = r'''
  _________ __          __  .__          __  .__               
 /   _____//  |______ _/  |_|__| _______/  |_|__| ____   ______
 \_____  \\   __\__  \\   __\  |/  ___/\   __\  |/ ___\ /  ___/
 /        \|  |  / __ \|  | |  |\___ \  |  | |  \  \___ \___ \ 
/_______  /|__| (____  /__| |__/____  > |__| |__|\___  >____  > Developed by WanZ
        \/           \/             \/               \/     \/  v2024.0
      '''
print(main_banner)
print("\nUse space for each data and comma for frequency\nPress Enter to calculate data")
def main_function():
    sorted_data = []
    raw_data = input("Data: ")
    data = raw_data.split(" ")
    frequency = {}
    cumulative_frequency = 0
    cumulative_item = 0
    system('cls')
    mean = 0
    if ',' not in raw_data:
        for i in data:
            sorted_data.append(int(i))
        for i in data:
            mean = mean + int(i)
        mean = mean / len(data)
    else:
        for i in data:
            sorted_data.append(int(i.split(',')[0]))
            frequency[int(i.split(',')[0])] = int(i.split(',')[1])
        sort_order = sorted(sorted_data)
        for i in range(len(sorted_data)):
            cumulative_frequency = cumulative_frequency + frequency[sort_order[i]]
            cumulative_item = cumulative_item + (sort_order[i] * frequency[sort_order[i]])
        mean = cumulative_item / sum(frequency.values())
    sort_order = sorted(sorted_data)
    quartile = []
    limit = int(len(sort_order) / 2)
    if (len(sort_order) % 2) == 0:
        for i in range(limit):
            median = (sort_order[i] + sort_order[-(i+1)]) / 2
    else:
        median = sort_order[limit]
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
    if ',' not in raw_data:
        mode = 1
        for i in sort_order:
            if (sort_order.count(i) > mode):
                mode = i
    else:
        for i in frequency:
            if (frequency[i] == max(frequency.values())):
                mode = i
    lower_fence = quartile[0] - 1.5 * (quartile[2] - quartile[0]) 
    upper_fence = quartile[2] + 1.5 * (quartile[2] - quartile[0]) 

    print(main_banner)
    print(f'''
    Raw data            :{data}
    Sorted order        :{sort_order}
    Mean                :{mean}
    Median              :{median}
    Mode                :{mode}
    Range:              :{sort_order[-1] - sort_order[0]}
    1st Quartile        :{quartile[0]}
    2nd Quartile        :{quartile[1]}
    3rd Quartile        :{quartile[2]}
    Maximum             :{max(sort_order)}
    Minium              :{min(sort_order)}
    Variance            :Not Available
    STD Deviation       :Not Available
    Upper Fence         :{upper_fence}
    Lower Fence         :{lower_fence}
        ''')
while True:
    try:
        main_function()
    except KeyboardInterrupt:
        system('cls')
        print(main_banner)
        exit()