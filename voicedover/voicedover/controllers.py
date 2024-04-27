
class Controllers:
    

    def get_prompt(self, **kwargs):
        return self.prompt_template.format(**kwargs)