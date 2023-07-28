file2 = open("essay1.txt","w")
file2.write("My favourite bike is splender.\n My first ride was in age of 18 and i was going for my board exams.\nFirst time i feel that i was the king of my own world.\n As my wish to drive my bike alone for going anywhere and it was make stylish in school for bringing my own bike.\n my bike gives best speed in comapre to others bikes of my friends.\nAnd we also had race and most of the time i got win.")
file2.close()
file1 = open("essay.txt","w")
file1.write("My favourite bike is Honda CBR 650r\nThis bike comes with 650 cc engine\n It is a superbike that comes with powerful 150 bhp power and 165 Nm torque\n This bike comes around 10 lakhs inr\n I still didnt get chance to ride this bike but hope fo getting it sooner\n My dream is to own that bike someday and I'm gonna make it! ")
file1.close()



file1 = open("essay.txt", "r")
file2 = open("essay1.txt", "r")
data = dict()
data1 = dict()
total = 0


def file1_logic(file1):
    count = 0
    print("This is file 1")

    for line in file1:
        # Remove the leading spaces and newline character
        line = line.strip()

        # convert in to lower
        line = line.lower()

        # split the words with space
        words = line.split(" ")
        # iterate each word over in line..

        for word in words:
            count += 1
            if word in data:
                # increment count of word by 1
                data[word] = data[word] + 1
            else:
                # Add the word to dictionary with count 1
                data[word] = 1
    # print dictonary
    for key in list(data.keys()):
        print(key, ":", data[key])
    file1.close()
    return count


def file2_logic(file2):
    count = 0
    print("This is file 2")

    for line in file2:
        # Remove the leading spaces and newline character
        line = line.strip()

        # convert in to lower
        line = line.lower()

        # split the words with space
        words = line.split("\xa0")
        # iterate each word over in line..

        for word in words:
            count += 1
            if word in data1:
                # increment count of word by 1
                data1[word] = data1[word] + 1
            else:
                # Add the word to dictionary with count 1
                data1[word] = 1
    # print dictonary
    for key in list(data1.keys()):
        print(key, ":", data1[key])
    file2.close()
    return count


count1 = file1_logic(file1)
count2 = file2_logic(file2)
print(data)
print(data1)
print("This size of 1 essay", count1)
print("This size of 2 essay", count2)
for i, j in data.items():
    for k, m in data1.items():
        if i == k:
            total += min(j, m)

print(((total) / max(count1, count2)) * 100, "%")
