from tempy.tags import Html, Head, Body, Meta, Link, Div, P, A

my_text_list = ['This is foo', 'This is Bar', 'Have you met my friend Baz?']
another_list = ['Lorem ipsum ', 'dolor sit amet, ', 'consectetur adipiscing elit']
page=Html()(
Head()(Meta(charset='utf-8'),  # add tag attributes using kwargs in tag initialization
        Link(href="my.css", type="text/css", rel="stylesheet")
        ),
body=Body()(
Div(klass='linkBox')(
            A(href='www.foo.com')
        ),
(P()(text) for text in my_text_list ),
another_list
)
)


print(page.render())
