class Solution:
    def ParenthesisMatch(self,input):
        step=[]
        for i in range(len(input)):
            if input[i] == '(':
                step.append(1)
            elif input[i] == '{':
                step.append(2)
            elif input[i] == '[':
                step.append(3)
            elif input[i] == ')' and step[-1] == 1:
                step.pop()
            elif input[i] == '}' and step[-1] == 2:
                step.pop()
            elif input[i] == ']' and step[-1] == 3:
                step.pop()
        return step == []

    def ParenthesisMatch1(self,input):
        count=0
        for i in range(len(input)):
            if input[i] == '(': count+=1
            elif input[i] == '{': count+=1
            elif input[i] == '[': count+=1
            elif input[i] == ')' and input[i-1] == '(' and i!=0: count-=1
            elif input[i] == '}' and input[i-1] == '{' and i!=0: count-=1
            elif input[i] == ']' and input[i-1] == '[' and i!=0: count-=1
            else : return False
        return count == 0

def main():
    input='()[]' # ')[](' # '([)]'
    ans=Solution().ParenthesisMatch1(input)
    print(ans)

if __name__=="__main__":
    main()








