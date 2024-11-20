import os

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
        # Genereate a unique filename
        i = 1
        filename = f"{filename_prefix}{i}.txt"
        while os.path.exists(os.path.join("wildcards", filename)):
            i += 1
            filename = f"{filename_prefix}{i}.txt"

        # Save the wildcard text to file if requested
        if save_to_file:
            with open(os.path.join("wildcards", filename), "w") as f:
                f.write(wildcard_text)

        # Return the filename for referencing in prompts
        return (filename,)
