import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class Encryption(Handler):
	def get(self):
		self.render('index.html')

	def post(self):
		text = self.request.get('text')
		new_text = ""
		if text:
			new_text = text.encode('rot13')
		self.render('index.html', text=new_text)

app = webapp2.WSGIApplication([('/', Encryption)], debug = True)