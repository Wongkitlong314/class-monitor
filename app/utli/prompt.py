class PromptConstructor:
    def __init__(self, template_path: str, args):
        self.template_path = template_path
        self.args = args
        self.template = ""
        with open(self.template_path) as f:
            for line in f:
                self.template += line
                self.template += "\n"

        self.prompt = ""
        ## use template and args to generate a prompt

    def get(self):
        return self.prompt
