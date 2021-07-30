data = []
new = []
count = 0
comments = 0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('總共有', len(data), '筆資料')

#算留言平均長度
for comment in data:
    comments = comments + len(comment)
print('平均留言長度是', comments / len(data), '個字')

#找出小於一百字的留言數
for comment in data:
    if len(comment) < 100:
        new.append(comment)
print('共有', len(new), '筆留言小於一百字')
print(new[0])

