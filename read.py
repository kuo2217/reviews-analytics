data = []
count = 0
comments = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('總共有', len(data), '筆資料')

for comment in data:
    comments = comments + len(comment)
print('平均留言長度是', comments / len(data), '個字')

