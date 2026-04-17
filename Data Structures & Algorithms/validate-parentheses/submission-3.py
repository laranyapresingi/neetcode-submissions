class Solution:
    def isValid(self, s: str) -> bool:
        st=[]

        for x in s:
            if x=='{' or x=='[' or x=='(':
                st.append(x)
            elif x=='}':
                if st and st[-1]=='{':
                    st.pop()
                else:
                    st.append(x)
            elif x==')':
                if st and st[-1]=='(':
                    st.pop()
                else:
                    st.append(x)
            elif x==']' :
                if st and st[-1]=='[':
                    st.pop()
                else:
                    st.append(x)

        
        return (len(st)==0)
                