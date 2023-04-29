# Tool-Collection

## FLAC 文件批量转换为 MP3 格式

### 1. 安装依赖

#### 安装 pydub 库

```bash
pip install pydub
```
安装 ffmpeg
macOS:
```bash
brew install ffmpeg
```
Windows: 请参考官方文档 Install FFmpeg on Windows[https://www.wikihow.com/Install-FFmpeg-on-Windows]
Linux:
```bash
sudo apt install ffmpeg
```
### 2. 使用方法
将代码中的 input_folder 替换为您的 FLAC 文件所在文件夹的路径，将 output_folder 替换为您想要保存 MP3 文件的文件夹路径。运行此代码，即可实现 FLAC 文件批量转换为 MP3 格式。