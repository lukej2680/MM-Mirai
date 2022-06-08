const NodeHelper = require("node_helper");
const bodyParser = require("body-parser");
// add require of other javascripot components here
// var xxx = require('yyy') here

module.exports = NodeHelper.create({

	init(){
		console.log("MIRAI-NODEHELPER: init module helper SampleModule");
	},

	start() {
        console.log('MIRAI-NODEHELPER: Starting module helper:' + this.name);
        this.createRoutes();
	},

	stop(){
		console.log('MIRAI-NODEHELPER: Stopping module helper: ' + this.name);
	},

    createRoutes: function() {
        var self = this;
        console.log("MIRAI-NODEHELPER: Route is running")
        var jsonParser = bodyParser.json();

        this.expressApp.post("/Mirai-API", jsonParser, function(req, res) {

            var command = req.body.cmd;
            console.log("MIRAI-NODEHELPER: " + command);

            if (command === "UPDATE_REMINDERS") {
                self.sendSocketNotification('UPDATE_REMINDERS', null)
            } else if (command === "ALARM_SET") {
                self.sendSocketNotification('ALARM_SET', req.body.data)
            } else {
                self.sendSocketNotification('REPLACE_TEXT', command)
            }

            res.sendStatus(200);
            res.end();
        });

        this.expressApp.get("/Mirai-API", function(req, res) {
            res.send("Hello World!");
        });
    },

    socketNotificationReceived: function(notification, payload) {
        console.log(this.name + " received a socket notification: " + notification + " - Payload: " + payload);
    },

});

/*
var app = require("express")();
var http = require('http').Server(app);
var bodyParser = require('body-parser');

 app.use(bodyParser.json())
 app.post('/',function(req,res){
    var msg=req.body.msg;
    console.log("python: " + msg);
    res.sendStatus(200)
    res.end()
 });

http.listen(8888, function(){
    console.log('listening...');
});
*/
