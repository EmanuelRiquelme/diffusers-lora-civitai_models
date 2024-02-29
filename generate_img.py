from diffusers import StableDiffusionXLPipeline,StableDiffusionPipeline
import torch
import argparse
parser = argparse.ArgumentParser(description="Argument parser for model IDs and prompt.")
parser.add_argument("--model_path", type=str,
                    help="Path to the civit-ai model")
parser.add_argument("--lora_model_path", type=str,
                    help="Path to the LoRA model")
parser.add_argument("--prompt", type=str,
                    help="Prompt to be used.")


torch.backends.cuda.matmul.allow_tf32 = True


def lora_inference(model_path,prompt,lora_model_path):
    pipe = StableDiffusionXLPipeline.from_single_file(model_path,torch_dtype=torch.float16).to('cuda')
    pipe.unet.load_attn_procs(lora_model_path)
    negative_prompt = "unrealistic, saturated, high contrast, big nose, painting, drawing, sketch, cartoon, anime, manga, render, CG, 3d, watermark, signature, label" 
    complete_prompt = f'{prompt},(complete face:2),award winning photo,(detailed facial features), (hyperdetailed:1.15), detailed eyes,lighting, studio lighting, looking at the camera ,photorealistic, sharp'
    pipe.enable_model_cpu_offload()
    with torch.inference_mode():
        image = pipe(
            prompt = complete_prompt,
            height = 1152,
            negative_prompt = negative_prompt,
            width = 896,
            num_inference_steps = 500,
            eta=1.0,
            guidance_scale=8
        ).images[0]
    image.save(f"{model_path}_{prompt}.png")

if __name__ == '__main__':
    args = parser.parse_args()
    model_path = args.model_path
    lora_model_path = args.lora_model_path
    prompt = args.prompt
    lora_inference(model_path,prompt,lora_model_path)
