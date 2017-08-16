
# Import Python Libraries
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# Import SQLAlchemy and CRUD Operations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant import Base, Restaurant, MenuItem

# Create Session and Connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                output = "<html><body>"
                output += "<a href = '/restaurants/new'>Make a New Restaurant Here</a></br></br>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"
                    output += "<a href ='/restaurants/%s/edit'>Edit</a>" % (restaurant.id)
                    output += "</br>"
                    output += "<a href = '/restaurants/%s/delete'>Delete</a>" % (restaurant.id)
                    output += "</br></br></br>"

                output += "</body></html>"
                self.wfile.write(output.encode())
                return

            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output +=   """
                            <form method='POST' enctype='multipart/form-data' action='/restaurants/new'>
                                <input name='newRestaurantName' type='text' placeholder='New Restaurant Name'>
                                <input type='submit' value='Create'>
                            </form>
                            """
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>%s</h1>" % (myRestaurantQuery.name)
                    output +=   """
                                <form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>
                                    <input name='newRestaurantName' type='text' placeholder='%s'>
                                    <input type='submit' value='Rename'>
                                </form>
                                """ % (restaurantIDPath, myRestaurantQuery.name)
                    output += "</body></html>"
                    self.wfile.write(output)

            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()

                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()

                    output = "<html><body>"
                    output += "<h1>Are you sure you want to delete %s?</h1>" % (myRestaurantQuery.name)
                    output +=   """
                                <form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>
                                    <input type='submit' value='Delete'>
                                </form>
                                """ % (restaurantIDPath)
                    output += "</body></html>"
                    self.wfile.write(output)

        except IOError:
            self.send_error(404, 'File Not Found: %s' % (self.path))

    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    name = fields.get('newRestaurantName')

                    # Create New Restaurant
                    newRestaurant = Restaurant(name=name[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    name = fields.get('newRestaurantName')
                    restaurantIDPath = self.path.split("/")[2]
                    myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()

                    if myRestaurantQuery != []:
                        myRestaurantQuery.name = name[0]
                        session.add(myRestaurantQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                if myRestaurantQuery:
                    session.delete(myRestaurantQuery)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            """
            output = ""
            output += "<html><body>"
            output += "<h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output +=   
                        <form method='POST' enctype='multipart/form-data' action='/hello'>
                            <h2>What would you like me to say?</h2>
                            <input name="message" type="text" >
                            <input type="submit" value="Submit">
                        </form>
                        
            output += "</body></html>"
            self.wfile.write(output)
            """
        
        except:
            pass

try:
	port = 8080
	server = HTTPServer(('', port), webServerHandler)
	print("Web Server running on localhost:%s/restaurants"  % (port))
	server.serve_forever()
except KeyboardInterrupt:
	print(" entered, stopping web server....")
	server.socket.close()
