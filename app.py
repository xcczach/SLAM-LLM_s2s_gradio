import gradio as gr
import soundfile as sf
import os
from s2s import generate


def get_tmp_path(file_name: str):
    temp_dir = "tempor"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    return os.path.join(temp_dir, file_name)


def process_audio(audio_file):

    result_audio_arr, sample_rate = generate(audio_file)

    target_path = get_tmp_path("processed_audio.wav")
    sf.write(target_path, result_audio_arr, sample_rate)

    return target_path


def text_to_audio(text):
    data, samplerate = sf.read("sample.wav")

    processed_data = data

    target_path = get_tmp_path("processed_text_audio.wav")
    sf.write(target_path, processed_data, samplerate)

    return target_path


with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("### S2S")
        audio_input = gr.Audio(label="Input Audio", type="filepath", format="wav")
        audio_output = gr.Audio(label="Output Audio")
        audio_button = gr.Button("Start")
        audio_button.click(process_audio, inputs=audio_input, outputs=audio_output)

    with gr.Row():
        gr.Markdown("### TTS")
        text_input = gr.Textbox(label="Input Text")
        file_output = gr.Audio(label="Output Audio")
        text_button = gr.Button("Start")
        text_button.click(text_to_audio, inputs=text_input, outputs=file_output)

demo.launch()
