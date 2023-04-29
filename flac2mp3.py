import os
from pydub import AudioSegment

def convert_flac_to_mp3(file_path, output_path, bitrate='192k'):
    flac_audio = AudioSegment.from_file(file_path, format='flac')
    flac_audio.export(output_path, format='mp3', bitrate=bitrate)
    print(f"Converted: {file_path} -> {output_path}")

def batch_convert_flac_to_mp3(input_folder, output_folder, bitrate='192k'):
    for root, _, files in os.walk(input_folder):
        relative_path = os.path.relpath(root, input_folder)
        output_root = os.path.join(output_folder, relative_path)

        if not os.path.exists(output_root):
            os.makedirs(output_root)

        for file in files:
            if file.endswith('.flac'):
                file_path = os.path.join(root, file)
                output_path = os.path.join(output_root, file.replace('.flac', '.mp3'))

                convert_flac_to_mp3(file_path, output_path, bitrate=bitrate)

if __name__ == "__main__":
    input_folder = 'path/to/your/input/folder'
    output_folder = 'path/to/your/output/folder'
    bitrate = '192k'  # 自定义比特率，例如 '128k', '192k', '256k' 等
    batch_convert_flac_to_mp3(input_folder, output_folder, bitrate=bitrate)