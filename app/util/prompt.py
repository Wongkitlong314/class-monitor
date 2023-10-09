class PromptConstructor:
    def __init__(self, template_path: str, *args):
        self.template_path = template_path
        self.args = args
        self.template = ""
        with open(self.template_path,'r') as f:
            for line in f:
                self.template += line
                self.template += "\n"
        self.prompt = self.template.format(*args)
    def get(self):
        return self.prompt




if __name__ == "__main__":
    import os
    prompt = PromptConstructor("app/prompt_templates/prompt_test.txt", "sports","ava","fasfa").get()
    print(prompt)


