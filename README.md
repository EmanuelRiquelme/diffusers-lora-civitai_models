# Generate Images powered by [Civit.AI](https://civitai.com/) models

This is a python script allows you to generate images, you should use a  [Civit.AI](https://civitai.com/)  model and a LoRA, the code was tested in the following pc:
CPU: i5 11400f
GPU: NVIDIA RTX 3070 TI
RAM: 32GB
OS: Ubuntu 22.04.4 LTS
Python version: Python 3.10.13
## TODO:
* Make the LoRA feature optional.
* Add support for CPU.
* Add the option for custom number of epochs and resolution.
* Add the option to use SD 1.5 models as well.
* Create a docker container.
* Add images as examples.

## How to use it
1)  Create a conda environment 
``` bash
conda create -n stable-diff python=3.10.13
```
2) Activate the environment
```bash
conda activate stable-diff
```
3) Install requirements
```bash
pip3 install -r requirements.txt
```
4) Download a custom LoRA and SDXL model from [civit.ai](https://civitai.com/) or other website.

5) run the script:
``` bash
python generate_img.py --model_path 'models/zavychromaxl_v40.safetensors' --lora_model_path 'margot_lora_sdxl_v1-000006.safetensors' --prompt 'ohwx woman portrait,ohwx woman corporate headshot,ohwx woman wearing a dress,<lora:margot_lora_sdxl_v1-000006:1>'
```
	model_path: is the localization of the SDXL model.
	lora_model_path: is the localization of the LoRA model.
	prompt: it is the prompt for the SD model.
