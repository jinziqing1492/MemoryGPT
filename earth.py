from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

llm = ChatOpenAI(temperature=0.9, openai_api_key="18ffb1b0dd94c9cf059d922c909201df", openai_api_base="http://flag.smarttrot.com/index.php/api/v1")
messages = [
    HumanMessage(content="你会反问吗？")
]
print(llm(messages))

# 打开文件
# file = open('wanderingearth.txt', 'r', encoding='utf-8') 

# 读取文件内容并行打印
# for line in file:
#    print(line)

# 关闭文件
# file.close()