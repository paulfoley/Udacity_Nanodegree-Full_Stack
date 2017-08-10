var bio = {
	"name" : "Paul",
	"age" : 28,
	"role" : "Web Developer",
	"contacts": {
		"mobile" : "(303)817-8056",
		"email" : "me@,paulnicholasfoley.com",
		"github" : "paulfoley",
		"linkedIn" : "paulnicholasfoley",
		"location" : "Denver"
	},
	"bioPic" : "images/me.jpg",
	"welcomeMessage" : "Hello There!",
	"skills": ["Python", "JavaScript", "HTML", "CSS"]
};

var formattedName = HTMLheaderName.replace("%data%", bio.name);
var formattedRole = HTMLheaderRole.replace("%data%", bio.role);

$("#header").prepend(formattedRole);
$("#header").prepend(formattedName);