var cat = {
    tiredness: 20,
    hunger: 20,
    loneliness: 20,
    happiness: 20,
    grumpy : function() {
        if (this.tiredness < 5) {
            console.log("Meow. Meow. Meow.");
        }
        if (this.hunger < 5) {
            console.log("Meow. Meow. Meow.");
        }
        if (this.loneliness < 5) {
            console.log("Meow. Meow. Meow.");
        }
        if (this.happiness < 5) {
            console.log("Meow. Meow. Meow.");
        }
    },

    feed : function(food) {
        if (food === "purina") {
            console.log("Mmm... I love " + food);
            this.hunger += 10;
        }
        else if (food === "generic") {
            console.log("Try to find better food next time");
            this.hunger += 5;
        }
        else {
            console.log("I won't eat that.");
            this.hunger -= 5;
        }
        this.grumpy();
    },

    sleep : function() {
        console.log("zzz");
        this.tiredness += 10;
        this.hunger -= 10;
        this.loneliness -= 10;
        this.grumpy();
    },

    pet : function() {
        console.log("prrr");
        this.happiness += 10;
        this.loneliness += 10;
        this.hunger -= 5;
        this.grumpy();
    },

    check : function() {
        console.log("tiredness: " + this.tiredness);
        console.log("hunger: " + this.hunger);
        console.log("loneliness: " + this.loneliness);
        console.log("happiness: " + this.happiness);
    },

};
