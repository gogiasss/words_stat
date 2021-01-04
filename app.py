import collections

#в кавычках имя файла в котором считаем
with open('210104-list-sample.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

c = collections.Counter()


for word in content:
    c[word] += 1
#имя файла для записи результата
my_file = open('result.txt', 'w')



for key, value in c.items():
    if value >= 10: #пороговое значение
        res = str((key,value))
        res = res[:-1]
        res = res[1:]
        res = res.replace("'",'')
        res = res.replace(",",':')
        res = res.replace(" ",'')
        my_file.write(res+'\n')

my_file.close()

        



