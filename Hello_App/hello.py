import os
import webapp2

form="""
<form method='post' action="/testform">
	<input name="q">
	<input type="submit">
</form>
"""

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a,**kw)

class HelloWorld(Handler):
    def get(self):
        self.write('Hello Google App Engine')

app = webapp2.WSGIApplication([('/', HelloWorld)], debug=True)