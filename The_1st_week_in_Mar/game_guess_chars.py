import random

name = input('请输入你的名字：')
f = open(r'C:\Users\dell\learning_python\The 1st week in Mar\game.txt')
lines = f.readlines()
f.close()

scores = {} # 初始化一个空字典
for l in lines:
    s = l.split()
    scores[s[0]] = s[1:]
score = scores.get(name)
if score is None:
    score = [0, 0, 0]

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0
print('你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (game_times, min_times, avg_times))

num = random.randint(1, 10)
times = 0
print("Guess what i'm thinking")
BINGO = False
# 定义比较函数
def compare(num1, num2):
    
    if answer > num:
        print('Too big.')
        return False

    if answer < num:
        print('Too small.')
        return False

    if answer == num:
        print('BINGO!')
        return True


while BINGO == False:
    # 游戏每进行一轮，将此变量加1
    times += 1
    answer = int(input('Please input:'))
    BINGO = compare(answer, num)

# 如果是第一次玩或者times参数比min_times还小，记录本次成绩为最小轮数
if game_times == 0 or times < min_times:
    min_times = times

# 计算总轮数
total_times += times
# 游戏次数加1
game_times += 1   

# 把成绩更新到对应的玩家数据中
# 加str转换成主辅材，为后面的格式化做准备
scores[name] = [str(game_times), str(min_times), str(total_times)] 
result = '' # 初始化一个空字符串，用来存储数据
for n in scores:
    # 把成绩按照“名字 游戏次数 最小轮数 总轮数”格式化
    # 结尾加上\n换行
    line = n + ' ' + ' '.join(scores[n]) + '\n'
    result += line # 添加到result中

# 将数据写入到文件中
with open(r'C:\Users\dell\learning_python\The 1st week in Mar\game.txt', 'w') as f:
    f.write(result)

print('Exit.')
