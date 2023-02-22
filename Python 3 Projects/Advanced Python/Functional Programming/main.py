import csv
from functools import reduce

def count(predicate, itr):
  # task 1
  count_filter = filter(predicate, itr)
  # task 2
  count_reduce = reduce(lambda x, y: x + 1, count_filter, 0)
  return count_reduce

def average(itr):
  iterable = iter(itr)
  # task 8
  return avg_helper(0, iterable, 0)

# task 3
def avg_helper(curr_count, itr, curr_sum): 
  # task 4
  next_num = next(itr, "null")
  # task 5
  if next_num == "null": 
    return curr_sum/curr_count
  curr_count += 1 
  # task 4
  curr_sum += next_num
  # task 6
  return avg_helper(curr_count, itr, curr_sum)


with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)
  # task 9
  count_belgiums = count(lambda x: x[1] == "Belgium", reader)
  print(count_belgiums)
  csvfile.seek(0)
  # task 10
  avg_portugal = average(map(lambda x: float(x[13]),filter(lambda x: x[1] == "Portugal", reader)))
  print(avg_portugal)