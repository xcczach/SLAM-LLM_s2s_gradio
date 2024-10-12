import gradio as gr
import soundfile as sf
import os
from s2s import generate

def get_tmp_path(file_name:str):
    return os.path.join("tmp", file_name)

# 音频处理函数：模拟大模型的推理过程
def process_audio(audio_file):
    
    # 模拟大模型推理过程（这里可以对音频数组进行处理）
    result_audio_arr, sample_rate = generate(audio_file)
    
    # 将处理后的音频数组写回音频文件
    target_path = get_tmp_path("processed_audio.wav")
    sf.write(target_path, result_audio_arr, sample_rate)
    
    # 返回处理后的音频文件
    return target_path

# 文本转音频函数：加载本地音频并模拟推理过程
def text_to_audio(text):
    # 加载本地音频文件 sample.wav
    data, samplerate = sf.read("sample.wav")
    
    # 模拟大模型推理过程
    processed_data = data  # 假装TTS
    
    # 将生成的音频写回文件
    target_path = get_tmp_path("processed_text_audio.wav")
    sf.write(target_path, processed_data, samplerate)
    
    # 返回处理后的音频文件
    return target_path

# 创建Blocks页面
with gr.Blocks() as demo:
    # 第一部分：音频输入输出
    with gr.Row():
        gr.Markdown("### 输入音频，返回处理后音频")
        audio_input = gr.Audio(label="输入音频", type="filepath")
        audio_output = gr.Audio(label="输出音频")
        audio_button = gr.Button("处理音频")
        audio_button.click(process_audio, inputs=audio_input, outputs=audio_output)

    # 第二部分：文本输入，返回音频文件
    with gr.Row():
        gr.Markdown("### 输入文本，返回生成的本地音频文件")
        text_input = gr.Textbox(label="输入文本")
        file_output = gr.Audio(label="输出音频文件")
        text_button = gr.Button("生成音频")
        text_button.click(text_to_audio, inputs=text_input, outputs=file_output)

# 启动Gradio界面
demo.launch()
