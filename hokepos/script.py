from markdown2 import Markdown 
md = Markdown()
import re
import os
import dominate
from dominate.tags import *
from dominate.util import raw
import bs4

def markdown_correction(file_str) :

    # correcting italics from __ to _ 
    replace_list = (re.findall("\_\_.*?\_\_", file_str))
    for r in replace_list:
        file_str = file_str.replace(r, '''_{0}_'''.format(r[2:-2]))
    
    # replacing [[ and ]] to links
    replace_list = (re.findall("\[\[.*?\]\]", file_str ))
    for r in replace_list:
        file_str  = file_str.replace(r, '''<a href="{0}.html" class="insidelink" target="_self"> {1} </a>'''.format(r[2:-2].replace(" ", "-"), r[2:-2]))


    # replacing > and \n to blockquote
    replace_list = (re.findall("- > .*?\n", file_str ))
    for r in replace_list:
        file_str  = file_str.replace(r, '''- <blockquote><p>{0}</p></blockquote>\n'''.format(r.replace("- >","")))

    # replacing ## and \n to blockquote
    replace_list = (re.findall("## .*?\n", file_str ))
    for r in replace_list:
        file_str  = file_str.replace(r, '''<h2>{0}</h2>\n'''.format(r.replace("##","")))

    
    return file_str

def remove_level_0_list (file_str) :
    soup = bs4.BeautifulSoup(str(md.convert(file_str)),'html.parser')
    ul = soup.find('ul')
    li_list = (ul.find_all('li', recursive=False))
    new_list = []
    for ele in li_list:
        ele.name = "p"
        new_list.append(str(ele))

    raw_html_file_str = "\n".join(new_list)
    return raw_html_file_str

month_string_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
mk_files_location = 'roam_exports/markdown/'
files_list = [f[:-3] for f in os.listdir(mk_files_location) if f.endswith('.md') and not f.startswith(tuple(month_string_list))]
print(files_list)

for file_name in files_list:

    with open('roam_exports/markdown/{}.md'.format(file_name), 'r') as f:
        file_str = f.read()
        file_str = markdown_correction(file_str)
        raw_html_file_str = remove_level_0_list(file_str)
        _html = html()
        _head, _body = _html.add(head(title("{}".format(file_name))), body(cls="typography bg-light"))   

        with _head:
            meta(charset="UTF-8")
            link(rel='stylesheet', href='style.css')
            link(rel='stylesheet',  href='https://fonts.googleapis.com/css?family=IBM+Plex+Sans', type='text/css')
            link(rel="stylesheet", type="text/css", href="../css/normalize.css")
            link(rel="stylesheet", type="text/css", href="../css/main.css")
            base(target="_blank")

        with _body:
            with nav(cls="nav sec-container-wide sec-header"):
                with ul(cls="nav-links body2 list") :
                    with li(cls="nav-link nav-title") :
                        with a("NotTheRealSanta"):
                            attr(cls="b no-underline", href="../index.html", target="_self")

        with _body:
            with main(cls="unit-page-content"):
                with div(cls="sec-content sec-container-content"):
                    with article(cls="card"):
                        with h1(file_name) :
                            attr(cls="h4 card-title measure-wide")
                        with div(cls="content body-lg-md measure-wide"):
                            raw(raw_html_file_str)

        with open('pages/{}.html'.format(file_name.replace(" ","-")), 'w') as wf:
            print('writing file : {}'.format(file_name))
            wf.write(str(_html))
