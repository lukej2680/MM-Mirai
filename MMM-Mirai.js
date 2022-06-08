Module.register("MMM-Mirai", {

	// anything here in defaults will be added to the config data
	// and replaced if the same thing is provided in config
	defaults: {
		text: "default message if none supplied in config.js"
	},

	init: function(){
		Log.log("MIRAI: " + this.name + " is in init!");
	},

	start: function(){
        Log.log("MIRAI: " + this.name + " is starting!");
        this.sendSocketNotification("OPEN_CHANNEL", 'Establishing Socket Connection');
	},

	loaded: function(callback) {
		Log.log("MIRAI: " + this.name + " is loaded!");
		callback();
	},

	// this is the major worker of the module, it provides the displayable content for this module
	getDom: function() {
		var wrapper = document.createElement("div");
        wrapper.innerHTML = this.config.text;
        return wrapper;
    },
    
    socketNotificationReceived: function(notification, payload) {
        var self = this;
        if (notification === "UPDATE_REMINDERS") {
            self.sendNotification("UPDATE_REMINDERS", null)
            Log.log("MIRAI: UPDATE_REMINDERS has been sent")
        }
        else if (notification === 'ALARM_SET') {
            self.sendNotification("ALARM_SET", payload)
            Log.log("MIRAI: ALARM_SET has been sent")
        }
		else if (notification === 'REPLACE_TEXT') {
                        console.log("STARTED notification received from node_helper");
			this.config.text = payload;3
			this.updateDom();
		}
	}

})
