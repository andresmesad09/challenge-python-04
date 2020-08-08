def div(func):
    # You have to code here!
    def wrapper_div(*args, **kwargs):
        html_list = ['<div>', func(*args, **kwargs), '</div>']
        html_code = ''.join(html_list)
        return html_code
    return wrapper_div
        


def article(func):
    # You have to code here!
    def wrapper_article(*args, **kwargs):
        html_list = ['<article>', func(*args, **kwargs), '</article>']
        html_code = ''.join(html_list)
        return html_code
    return wrapper_article

def p(func):
    # You have to code here!
    def wrapper_p(*args, **kwargs):
        html_list = ['<p>', func(*args, **kwargs), '</p>']
        html_code = ''.join(html_list)
        return html_code
    return wrapper_p



# Here you must apply the decorators, uncomment this later
# @div
@article
# @p
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
