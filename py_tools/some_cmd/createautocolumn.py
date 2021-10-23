
import datetime
import random 

def chunks(lst, n):
  for i in range(0, len(lst), n):
    yield lst[i:i + n]

count = 10
root = '1632377461700B00000'
rootDate = '2021-09-25 00:00:00'

randomList = random.sample(range(10000, 99999), count)
result = []
result2 = []

for i in range(count) :
  current = i + 1 
  current = root + str(current).zfill(3)   
  currentDate = datetime.datetime.strptime(rootDate, '%Y-%m-%d %H:%M:%S') +datetime.timedelta(days=i)
  startDate = currentDate.strftime('%Y-%m-%d 00:00:00')
  endDate = currentDate.strftime('%Y-%m-%d 23:59:59')
  result.append((current, startDate, endDate))
  # print(current, ',', startDate, ',', endDate)

for idx, i in enumerate(result):
  result[idx] = i + (randomList[idx],)


# 生成insert 语句
insertRootState = "insert into t_xxx(a, b, c) values "
insertState = "({0}, {1}, {2}),"
insertResult = []

# print(result)

for i  in chunks(result,3):
  currentInsertState = insertRootState
  for j in i :
    currentInsertState += insertState.format(j[0], j[1], j[2])
  insertResult.append(currentInsertState[0:-1])

for i in insertResult : print(i)