import os
import random

class WildcardCreator:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "wildcard_text": ("STRING", {"multiline": True}),
                "filename_prefix": ("STRING", {"default": "__"}),
	    },
            "optional": {
                "save_to_file": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "create_wildcard"
    CATEGORY = "Wildcards"

    def create_wildcard(self, wildcard_text, filename_prefix, save_to_file):
        # Define Paths
        base_path = "ComfyUI/wildcards"
        additional_paths = [
            "ComfyUI/custom_nodes/ComfyUI-Impact-Pack/wildcards",
            "ComfyUI/custom_nodes/ComfyUI-Impact-Pack/custom_wildcards",            
        ]

        # Ensure base path exists
        os.makedirs(base_path, exist_ok=True)

        # Genereate a unique filename
        i = 1
        filename = f"{filename_prefix}{i}.txt"
        while os.path.exists(os.path.join(base_path, filename)):
            i += 1
            filename = f"{filename_prefix}{i}.txt"

        # Save the wildcard text to file if requested
        if save_to_file:
            with open(os.path.join(base_path, filename), "w") as f:
                f.write(wildcard_text)

        # Return the filename for referencing in prompts
        return (filename,)

class WildcardLoader:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "directory": ("STRING", {"default": "ComfyUI/wildcards"}),
            },
        }
    
    RETURN_TYPES = ("LIST",)
    FUNCTION = "load_wildcards"
    CATEGORY = "Wildcards"

    def load_wildcards(self, directory):
        # Load all wildcard files from the specified directory
        files = os.listdir(directory)
        wildcards = [f for f in files if (f.endswith('.txt') | f.endswith('.yaml'))]
        return (wildcards,)
    
class WildcardSelector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "wildcard_list": ("LIST", {}),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "select_wildcards"
    CATEGORY = "Wildcards"

    def select_wildcard(self, wildcard_list):
        # Randomly select a wildcard from the list
        return (random.choice(wildcard_list),)

class DisplayString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_string": ("STRING", {}),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "display_string"
    CATEGORY = "Display"

    def display_string(self, input_string):
        # Simply return the input string for display
        return (input_string,)