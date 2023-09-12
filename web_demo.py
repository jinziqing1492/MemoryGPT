# import gradio as gr

# filevisle = True

# with gr.Blocks() as demo:
#     gr.HTML("""<h1 align="center">MemoryGPT</h1>""")

#     chatbot = gr.Chatbot()
#     with gr.Row():
#         input_file = gr.File()

#         def hidupload(file):
#             input_file.hide()
#         input_file.upload(hidupload)
#     # submitBtn.click(predict, [user_input, chatbot, max_length, top_p, temperature, history, past_key_values],
#     #                 [chatbot, history, past_key_values], show_progress=True)
#     # submitBtn.click(reset_user_input, [], [user_input])

#     # emptyBtn.click(reset_state, outputs=[chatbot, history, past_key_values], show_progress=True)

# demo.queue().launch(share=False, inbrowser=True)
import gradio as gr

def predict_text(text):
    # 在这里进行文本处理和预测
    return "预测结果：" + text

# 创建一个文本输入框
text_input = gr.Textbox()
# 创建一个按钮组件
button = gr.Button("隐藏输入框")

# 当按钮被点击时，隐藏输入框
def hide_text_input():
    text_input.hide()

button.click(hide_text_input)

# 创建 Gradio 接口
iface = gr.Interface(fn=predict_text, inputs=text_input, outputs="text")
iface.launch()