# Building a Blog

# Imports
import os
import webapp2
import jinja2
from google.appengine.ext import db

# Setting Up Jinja Templates
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

# Setting up Web App Handler

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

# Front Page of the Blog
class Front(Handler):
	def get(self):
		blogs = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC LIMIT 10")
		self.render('blog_front.html', blogs = blogs)

# Viewing an Individual Blog Post
class Blog_Post(Handler):
	def get(self, blog_id):
		key = db.Key.from_path('Blog', int(blog_id), parent = blog_key())
		blog = db.get(key)
		self.render('blog_post.html', blog = blog)

# Adding a Blog Post
class New_Post(Handler):
	def get(self):
		self.render("new_post.html")

	def post(self):
		subject = self.request.get('subject')
		content = self.request.get('content')

		if subject and content:
			b = Blog(parent = blog_key(), subject = subject, content = content)
			b.put()
			self.redirect('/%s' % str(b.key().id()))
		else:
			error = "You need to enter both a subject and content"
			self.render('new_post.html', subject = subject, content = content, error = error)

# Setting Up the Blog Database
def blog_key(name = 'default'):
	return db.Key.from_path('blogs', name)

class Blog(db.Model):
	subject = db.StringProperty(required = True)
	content = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	last_modified = db.DateTimeProperty(auto_now = True)

	def render(self):
		self._render_text = self.content.replace('\n', '<br>')
		return render_str('blog_post.html', blog = self)

# Running the Web Application
app = webapp2.WSGIApplication([('/?',Front),('/newpost', New_Post),('/([0-9]+)', Blog_Post)], debug = True)
