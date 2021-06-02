#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json

from main.controllers.courses import courses
from main.professors import professor
from main.students import student
from main.titles import title
import decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return (str(o) for o in [o])
        return super(DecimalEncoder, self).default(o)


class S(BaseHTTPRequestHandler):
    def _set_response(self, contentType='text/html'):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        # SimpleHTTPRequestHandler.end_headers(self)
        self.send_header('Content-type', contentType)
        self.end_headers()

    def do_GET(self):
        print(str(self.path))
        self._set_response()
        self.wfile.write(bytes(open('index.html'.format(self.path)).read(), 'utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        print(post_data.decode('utf-8'))

        self._set_response('application/json')

        if self.path == '/add_student':
            student.add_student(json.loads(post_data.decode('utf-8')))
            value = {
                'success': True,
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))
            # "1POST request for {}".format(self.path).encode('utf-8'))

        elif self.path == '/delete_student':
            student.delete_student(json.loads(post_data.decode('utf-8')))
            value = {
                'success': True,
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/update_student':
            data = json.loads(post_data.decode('utf-8'))
            student.update(data['course_id'], data['student_id'])
            value = {
                'success': True,
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/add_professor':
            professor.add_professors(json.loads(post_data.decode('utf-8')))
            value = {
                'success': True,
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/delete_professor':
            professor.delete_professors(json.loads(post_data.decode('utf-8')))
            value = {
                'success': True,
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/show_all_professors':
            value = {
                'show_all_professors': professor.show_all_professors()
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/add_course':
            courses.add_courses(json.loads(post_data.decode('utf-8')))
            value = {
                'success': True,
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/delete_course':
            courses.delete_courses(json.loads(post_data.decode('utf-8')))
            value = {
                'success': True,
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/add_title':
            title.add_title(json.loads(post_data.decode('utf-8')))
            value = {
                'success': True,
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/delete_title':
            title.delete_title(json.loads(post_data.decode('utf-8')))
            value = {
                'success': True,
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/show_all_professors_and_courses':
            value = {
                'show_all_professors_and_courses': professor.show_all_professors_courses_and_students_count(),
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/show_all_Students_and_there_courses':
            value = {
                'show_all_Students_and_there_courses': student.show_all_students_and_there_courses()
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/show_top_three_courses':
            value = {
                'show_top_three_courses': courses.show_top_three_courses()
            }

            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/show_top_three_professors_enrolled_students_in_courses':
            value = {
                'show_top_three_professors_enrolled_students_in_courses': professor.show_top_three_professors_enrolled_students_in_courses()
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/show_all_courses':

            value = {
                'show_all_courses': courses.show_all_courses()
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        elif self.path == '/show_all_titles':
            value = {
                'show_all_titles': title.show_all_titles()
            }
            self.wfile.write(json.dumps(value).encode('utf-8'))

        else:
            self.wfile.write("2POST request for {}".format(self.path).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()