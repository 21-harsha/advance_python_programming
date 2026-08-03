def bold_text(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        border = "*" * 50
        return border + "\n" + text + "\n" + border
    return wrapper


class Report:
    templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, function):
        cls.templates[name] = function

    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    def __call__(self, template_name):
        template = Report.get_template(template_name)

        if template:
            return template(self)
        else:
            return "Template not found."


    def __str__(self):
        return "Report Title : " + self.title + "\nContent : " + self.content

  
    def __repr__(self):
        return "Report('{}','{}')".format(self.title, self.content)

    def __add__(self, other):
        new_title = self.title + " & " + other.title
        new_content = self.content + "\n" + other.content
        return Report(new_title, new_content)




def simple_template(report):
    return (
        "------ SIMPLE REPORT ------\n"
        "Title   : " + report.title + "\n"
        "Content : " + report.content
    )


@bold_text
def fancy_template(report):
    return (
        "FANCY REPORT\n"
        "Title   : " + report.title.upper() + "\n"
        "Content : " + report.content.upper()
    )


def main():

    # Add templates
    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    # Create reports
    report1 = Report(
        "Annual Report",
        "Sales increased by 20 percent."
    )

    report2 = Report(
        "Financial Report",
        "Profit reached 10 lakh rupees."
    )

    # Generate reports
    print("\nSimple Template\n")
    print(report1("simple"))

    print("\nFancy Template\n")
    print(report1("fancy"))

    # __str__
    print("\nUsing __str__")
    print(report1)

    # __repr__
    print("\nUsing __repr__")
    print(repr(report1))

    # __add__
    print("\nCombining Reports (__add__)")
    combined = report1 + report2
    print(combined("simple"))



if __name__ == "__main__":
    main()
