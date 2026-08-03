
def bold_text(func):
    def wrapper(*args, **kwargs):
        return "**" + func(*args, **kwargs) + "**"
    return wrapper



class Report:
    templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, template_func):
        cls.templates[name] = template_func

    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    def __call__(self, template_name):
        template = Report.get_template(template_name)
        if template:
            return template(self)
        else:
            return "Template not found!"

    def __str__(self):
        return f"Report Title: {self.title}\nContent: {self.content}"

def simple_template(report):
    return f"Title: {report.title}\nContent: {report.content}"


@bold_text
def fancy_template(report):
    return f"Title: {report.title}\nContent: {report.content}"


def main():

    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    report = Report(
        "Monthly Sales",
        "Sales increased by 20% this month."
    )

    print("Simple Report:")
    print(report("simple"))

    print("\nFancy Report:")
    print(report("fancy"))

    print("\nString Representation:")
    print(report)

if __name__ == "__main__":
    main()