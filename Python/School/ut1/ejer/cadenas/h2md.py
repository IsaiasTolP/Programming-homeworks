# ****************************
# CONVIRTIENDO HTML A MARKDOWN
# ****************************


def run(html: str) -> str:
    html_text = html[html.index('>') + 1 : html.index('</')]
    num_h = int(html[html.index('h') + 1 : html.index('>')])
    markdown = '#' * num_h + f' {html_text}'
    return markdown


if __name__ == '__main__':
    run('<h1>Core</h1>')
