dfs的基本框架
result=[]
path/temp_list =[]
if 超出满足条件 即sum > target 则return（剪枝）
if 刚刚好满足条件，则result.append() 然后return
if 不够满足条件，则嵌套dfs()函数，注意需要改变dfs函数的自变量和因变量