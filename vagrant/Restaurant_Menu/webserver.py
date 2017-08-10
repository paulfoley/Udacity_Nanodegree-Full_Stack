from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant import Base, Restaurant, MenuItem

# Create teh Engine
engine = create_engine('sqlite:///restaurantmenu.db')

# Bind the engine to the metadata of the Base class so that 
Base.metadata.bind = engine

# The declaratives can be accessed through a DBSession instance
DBSession = sessionmaker(bind=engine)

'''
A DBSession() instance establishes all conversations with the database
and represents a "staging zone" for all the objects loaded into the database session object.
Any change made against the objects in the session
won't be persisted into the database until you call session.commit().
If you're not happy about the changes, 
you can revert all of them back to the last commit by calling session.rollback()
'''
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                output = ""
                output += "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"

                output += "</body></html>"
                self.wfile.write(output.encode())
                return

            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output.encode())
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>&#161 Hola !</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output.encode())
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
            
            output = ""
            output += "<html><body>"
            output += "<h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
        
        except:
            pass
try:
	port = 8080
	server = HTTPServer(('', port), webServerHandler)
	print("Web Server running on port %s"  % port)
	server.serve_forever()
except KeyboardInterrupt:
	print(" entered, stopping web server....")
	server.socket.close()