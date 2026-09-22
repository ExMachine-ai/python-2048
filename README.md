前期参考资料（全部都没有用上）
https://developer.aliyun.com/article/1347799
https://blog.csdn.net/hyf64/category_11455181.html?orderBy=2
制作时参考：
https://docs.python.org/zh-cn/3/library/random.html
https://docs.python.org/zh-cn/3/tutorial/datastructures.html
https://docs.python.org/zh-cn/3/library/copy.html

其中https://docs.python.org/zh-cn/3/library/copy.html让我解决了一个头疼的bug ：
此前写的while语句内的判断新旧棋盘：
        shangyici_board = []
        for i in range(4):
            shangyici_board.append(board[i])
由于shangyici_board是直接引用的board，所以说改了不管我后面game是否更改了board，shangyici_board和board一直是相等的，就无法执行change_0(1)

解决方法就是，将board中一行的元素先存入old_line[]然后再将old_line存入shangyici_board

整体的思路就是
   先创建一个board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]
随后用change_0(count)找出其中的0记录其对应的行列在record_0 = []，随后判断现有空格数量是否满足修改条件，因为常用change_0(1)，就以它举例，如果只有0个空格了，那么
判断语句就会将1改为0，然后就相当于不执行后面的换数字了，如果有大于等于1个空格就会抽出1或2个空格换成2或者4。随后print目前的board让用户选择输入WASD中的一种，将输入
放入game(userinput)函数，函数会更具WASD不同的方向排好line，再将line放入merge(line)实现相同数字的合并，执行完后，check_game()函数会检查board是否有2048和board中的数字能不能继续移动，
如果有2048或者不能移动了就将game_result设置为False，跳出游戏。
