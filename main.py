#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import os
import webapp2
import logging
from google.appengine.api import users
from google.appengine.ext import ndb
import datetime
import json
import unicodedata
from google.appengine.api import users

# the two lines of code below makes the jinja work
jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class HomePage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/HomePage.html')
        self.response.write(template.render())

class AboutMe(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/Aboutme.html')
        self.response.write(template.render())

class Contact(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/Contact.html')
        self.response.write(template.render())




app = webapp2.WSGIApplication([
    ('/', HomePage), #HomePage
     ('/AboutMe.html',AboutMe),
    ('/Contact.html',Contact)
    # ('/Blog.html',IsraelBlog),
    # ('/hello.html',Hello),
    # ('/Survey_input.html',SurveyHandler),
    # ('/',MainPage),
    # ('/Adim',AdminPage)

], debug=True)
