import mistune
from jinja2 import Environment, PackageLoader, FileSystemLoader
import os
import re

class MyRenderer(mistune.HTMLRenderer):

    def list(self, text, ordered, level, start=None) :

        # replaceing [[ and ]] to links
        replace_list = (re.findall("\[\[.*?\]\]", text))
        for r in replace_list:
            text = text.replace(r, '''<a href="{0}.html">{0}</a>'''.format(r[2:-2].replace(" ", "-") ))

        replace_list = (re.findall("\^\^.*?\^\^", text))
        for r in replace_list:
            text = text.replace(r, '''<mark>{0}</mark>'''.format(r[2:-2]))
        # print("text : ",text)
        # print("ordered : ",ordered)
        # print("level : ", level)
        return "<ul>"+text+"</ul>"


if __name__ == "__main__":

    markdown = mistune.create_markdown(renderer=MyRenderer())

    files_list = [f for f in os.listdir('roam_exports/') if f.endswith('.md')]
    print(files_list)

    for f in files_list:
        file_name = f[:-3].replace(" ", "-")
        print('file name:', file_name)
        with open('roam_exports/{}'.format(f),'r') as test_file:
            parsed_md = (markdown(test_file.read()))

            env = Environment(loader=PackageLoader('script', 'templates'))

            template_obj = env.get_template('page_template.html')

            data = {
                'title' : f[:-3],
                'content': parsed_md,
            }

            with open('pages/{}.html'.format(file_name),'w') as write_file:
                write_file.write(template_obj.render(post=data))