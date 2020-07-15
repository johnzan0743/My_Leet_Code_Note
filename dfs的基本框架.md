dfs的基本框架
result=[]
path/temp_list =[]
如果需要去重，即如果candidates中每个元素只能取一次，则需要先对原数组排序，然后加入一个start序号指针，每一次新加入元素进行dfs嵌套的时候，start +=1
这个是为了防止出现[1,2,3,4],[1,2,4,3],[1,3,2,4]等这种重复的组合项

然后通过 
i > 0 and candidates[i] == candidates[i-1]: continue 
来防止重复元素造成的重复解集 例如原candidates为[1,1,2,3,4],避免解集是[1,2,3,4],[1,2,3,4]...

弄清楚这个条件特别重要，如果没办法想得太清楚，就不建议使用回溯法
if 超出满足条件 即sum > target 则return（剪枝）
if 刚刚好满足条件，则result.append()  然后return
if 不够满足条件，则嵌套dfs()函数，注意需要改变dfs函数的自变量和因变量
*当回溯函数是嵌套在主函数之中的时候，则可以不用在回溯函数中声明return，无论在剪枝还是append的时候都不需要，因为result可以被主函数无脑继承，所以不需要return，但实际标准规范是需要return的
针对第39题的补充，之所以无论是否加不加return都会出正确结果，是因为一开始sum(temp_list)如论如何不会等于target，所以一定会进入下面的for循环，所以一定会进入dfs进行回溯，所以即使加了return也不会有错
