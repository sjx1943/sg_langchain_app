#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

# import psycopg2

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/add','add'
)


db = web.database(
    dbn='postgres',
    host='localhost',
    port=5432,
    user='postgres',
    pw='641229',
    db='postgres',
)

class index:
    def GET(self):
        # name = '23f'
        # return render.index(name)
        # return 'nihao'
        todos = db.select('todo')
        return render.index(todos)

        # # i = web.input(name=None)
        # return render.index(name)


        # i = web.input(name=None)
        # return render.index(i.name)

class add:
    def POST(self):
        i = web.input(name=[])
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')
# post_data=web.input(name=[])

if __name__ == "__main__":
    app = web.application(urls, globals())
#     render = web.template.render('templates')
#     # print('hello')
    app.run()
#     print(render.index('hello'))