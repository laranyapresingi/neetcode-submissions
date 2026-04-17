class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for t in tokens:
            if t == '+':
                a=st.pop()
                b=st.pop()
                st.append(a+b)
            elif t== '-':
                a,b=st.pop(),st.pop()
                st.append(b-a)
            elif t=='/':
                a,b=st.pop(),st.pop()
                st.append(int(b/a))
            elif t=='*':
                a=st.pop()
                b=st.pop()
                st.append(a*b)
            else:
                st.append(int(t))
        return int(st[0])