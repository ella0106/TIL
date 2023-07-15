class q:
    def __init__(self):
        self.queue = []
        self.len = 0

    def isEmpty(self):
        if self.len == 0:
            return True
        else:
            return False

def solution(s, n):
    qlist = []
    for i in range(n):
        qlist.append(q())
    front = []
    answer = []
    star = 0
    #print(qlist)
    first_command = s.pop(0)
    front.append(first_command[1])

    for command in s:
        print("This time's command:", command)
        if command[0] == -1:
            answer.append(front.pop())
        
        else:
            qlist[command[0]].queue.append(command[1])
            qlist[command[0]].len += 1
            #print(qlist[command[0]].len)

        if len(front) == 0:
            count = 0
            while qlist[star].isEmpty():
                #print(qlist[star].isEmpty())
                star = (star + 1) % 4
                count += 1
                if count == 4:
                    break
                print("star:", star)
            if count == 4:
                pass
            else:
                front.append(qlist[star].queue.pop(0))
                qlist[star].len -= 1
                star = (star + 1) % 4

        print("star:", star)
        print(qlist[0].len, qlist[1].len, qlist[2].len, qlist[3].len)
        print(qlist[0].queue, qlist[1].queue, qlist[2].queue, qlist[3].queue)
        print("front:", front)
        print("answer:", answer)
        print()

    return answer







s = [[2, 3], [1, 4], [0, 2], [1, 6], [3, 1], [0, 9], [-1, -1], [-1, -1], [-1, -1], [3, 12], [1, 5], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
n = 4
solution(s, n)
#print(s.pop(0), s)
