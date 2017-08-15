from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant import Base, Restaurant, MenuItem

app = Flask(__name__)
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Restaurants Page
@app.route('/')
@app.route('/restaurants/', methods=['GET', 'POST'])
def restaurants():
    restaurants = session.query(Restaurant).all()
    
    return render_template('restaurants.html', restaurants=restaurants)

# Create New Restaurant
@app.route('/restaurants/new/', methods=['GET','POST'])
def newRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['name'])
        session.add(newRestaurant)
        session.commit()
        flash('New Restaurant Created')
        
        return redirect(url_for('restaurants'))
    else:
        return render_template('new_restaurant.html')

# Edit a Restaurant
@app.route('/restaurants/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    editRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editRestaurant.name = request.form['name']
        session.add(editRestaurant)
        session.commit()
        flash('Restaurant Edited')
        
        return redirect(url_for('restaurants'))
    else:
        return render_template('edit_restaurant.html', restaurant=editRestaurant)

# Delete a Restaurant
@app.route('/restaurants/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurantDelete = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurantDelete)
        session.commit()
        flash('Restaurant Deleted')
        
        return redirect(url_for('restaurants'))
    else:
        return render_template('delete_restaurant.html', restaurant=restaurantDelete) 

# Menu For a Specific Restaurant
@app.route('/restaurants/<int:restaurant_id>/', methods=['GET', 'POST'])
def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
	
	return render_template('menu.html', restaurant=restaurant, items=items)

# Create New Item
@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET','POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
    	newItem = MenuItem(name=request.form['name'], restaurant_id=restaurant_id)
    	session.add(newItem)
    	session.commit()
    	flash('New Menu Item Created')
    	
    	return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
    	return render_template('new_menu_item.html', restaurant_id=restaurant_id)

# Edit an Item
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
    	if request.form['name']:
    		editItem.name = request.form['name']
    	session.add(editItem)
    	session.commit()
    	flash('Menu Item Edited')
    	
    	return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
    	return render_template('edit_menu_item.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editItem)

# Delete a Menu Item
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    itemDelete = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
    	session.delete(itemDelete)
    	session.commit()
    	flash('Menu Item Deleted')
    	
    	return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
    	return render_template('delete_menu_item.html', restaurant_id=restaurant_id, item=itemDelete) 


# Make an API Endpoint (GET Request)
@app.route('/restaurants/JSON')
def restaurantsJSON():
    restaurants = session.query(Restaurant).all()

    return jsonify(Restaurants=[restaurant.serialize for restaurant in restaurants])


@app.route('/restaurants/<int:restaurant_id>/menu/JSON/')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    
    return jsonify(Restaurant=restaurant.serialize, MenuItems=[item.serialize for item in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON/')
def menuItemJSON(restaurant_id, menu_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    
    return jsonify(Restaurant=restaurant.serialize, Item=item.serialize)

app.secret_key = 'super_secret_key'
app.debug = True
app.run(host = '0.0.0.0', port = 5000)
