class Stack:
    def __init__ (self):
        self.stack=[]

    #return all elems of stack
    def __str__ (self):
        return "<bottom> ["+",".join(map(str,self.stack))+"]<top>"

    #write to stack
    def push(self,obj):
        self.stack.append(obj)
        return self

    #get from top of the stack
    def pop(self):
        if self.stack: return self.stack.pop()
        else: return None

    #check wether stack is empty
    def empty(self):
        return not self.stack

    #number of elems
    def len(self):
        return len(self.stack)

    #for using the same stack
    def clear(self):
        self.stack=[]

#task3
def get_res(text):
    el=""
    st=Stack()
    st2=Stack()
    for i in text:
        st.push(i)
        #print(i)
    while not st.empty():
        el=st.pop()
        if el==')':
            continue
        if el=='1' or el=='2' or el=='3' or el=='4' or el=='5' or el=='6' or el=='7' or el=='8' or el=='9' or el=='0':
            st2.push(el)
        if el==',':
            continue
        if el=='(':
            num1=''
            num2=''
            next_el=st.pop()
            #print (next_el)
            if next_el=='S':
                num1=st2.pop()
                num2=st2.pop()
                res=int(num1)+int(num2)
                st2.push(res)
            if next_el=='D':
                num1=int(st2.pop())
                num2=int(st2.pop())
                res=num1/num2
                st2.push(res)
            else:
                continue
        else:
            continue #if something else word is in text
    res=st2.pop()
    print(res)
    #return res

#task1
def brackets_nums(text):
    st=Stack()
    num=0
    for i in text:
        d=[]
        num+=1
        if i=='(' or i==')':
            d.append(i)
            d.append(num)
            #print(d)
            st.push(d)
        else:
            continue
    #print(st)
    return st

def sort_br1_by_ascending(text):
    st=brackets_nums(text)
    st2=Stack()
    num=0
    while not st.empty():
        i=st.pop()
        d=[]
        if i[0]==')':
            d.append(i[1])
            for j in text:
                num+=1
                if j=='(':
                    d.append(num)
                    break
            st2.push(d)
    l=[]
    while not st2.empty():
        l.append(st2.pop())
    print('Pairs of brackets:',l)
    s_asc=sorted(l)
    s_desc=sorted(l, reverse=True)
    print('Ascending: ',s_asc, '\nDecsending:',s_desc)
    
    #print(st2)
    #return st2

#task2
def check_simple_brackets(text):
    st=Stack()
    st2=Stack()
    for i in text:
        st.push(i)
    while not st.empty():
        i=st.pop()
        if i==')':
            st2.push(i)
        if i=='(':
            st2.pop()
    if st2.empty():
        print("There is no trouble with () brackets")
    else:
        print("Something wrong with () brackets")

def check_curl_brackets(text):
    st=Stack()
    st2=Stack()
    for i in text:
        st.push(i)
    while not st.empty():
        i=st.pop()
        if i=='}':
            st2.push(i)
        if i=='{':
            st2.pop()
    if st2.empty():
        print("There is no trouble with {} brackets")
    else:
        print("Something wrong with {} brackets")

def check_square_brackets(text):
    st=Stack()
    st2=Stack()
    for i in text:
        st.push(i)
    while not st.empty():
        i=st.pop()
        if i==']':
            st2.push(i)
        if i=='[':
            st2.pop()
    if st2.empty():
        print("There is no trouble with [] brackets")
    else:
        print("Something wrong with [] brackets")

def correct_or_not(text):
    check_simple_brackets(text)
    check_curl_brackets(text)
    check_square_brackets(text)
    
def main():
    #task 3
    text='S(S(1,D(8,4)),S(D(6,3),2))'
    # S(S(1+2),S(2+2))=S(3+4)=7
    #get_res(text)

    #task 1
    text1='2+(3*(8-5)-2)+6/(7-1)'
    #brackets_nums(text1)

    #task 1.1 and 1.2
    #sort_br1_by_ascending(text1)

    #task 2
    text2='2+{3*([8-5)]-2}+6]/(7&1)))'
    #correct_or_not(text2)

    print('Ready.')
    
main()
    
        
