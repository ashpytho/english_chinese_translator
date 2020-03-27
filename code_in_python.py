chinese=['你好','早上好','晚上好','你好吗','你好吗','我很好','你吃了
吗','吃了','你呢','欢迎']
english=['Hello','Good morning','Good evening',"How are you?",'I’m 

fine','Have you eaten?','I ate','And you?','Welcome']

#sorting the english list and chinese list at the same time
def bubbleSort(english,chinese):
    n = len(english)
    for i in range(n):
        for j in range(0, n-i-1):
 
            if english[j] > english[j+1] :
                english[j], english[j+1],chinese[j],chinese[j+1] = 

english[j+1], english[j],chinese[j+1],chinese[j]

#finding word in the english sentence but returing the chinese 

word
def binary_recursion(english,chinese,low,high,key):
    mid=(low+high)//2
    if low>high:
        return "not found"
    elif english[mid]==key:
        return chinese[mid]
    elif key<english[mid]:
        return binary_recursion(english,chinese,low,mid-1,key)
    elif key>english[mid]:
        return binary_recursion(english,chinese,mid+1,high,key)

bubbleSort(english,chinese)
word=input('Enter the sentence in english ? ')
print(binary_recursion(english,chinese,0,len(english)-1,word))
