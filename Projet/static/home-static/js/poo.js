function exp07() {
    var p1 = {
        name : "p1",
        x : 20,
        y : 30,
        toString : function () {
            return "Point(" + this.name + ", " + this.x + ", " + this.y + ")";
        }
    }

    p1.x = 45;

    logger.log("p1 = " + p1 + " : de type " + typeof p1);

    p1.z = 30;
    logger.log("p1.z = " + p1.z);
    logger.log("p1.name = " + p1.name);
    
    var p2 = Object.create(p1);
    p2.name = "p2";
    p2.y = 100;

    p1.x = 200;

    logger.log("p2 = " + p2);
    logger.log("p1 = " + p1);

    p2.x = 567;
    logger.log("p2 = " + p2);
}

function exp08() {
    Object.prototype.name = "Objet Parent";

    var p1 = {
        name : "p1",
        x : 20,
        y : 30,
        toString : function () {
            return "Point(" + this.name + ", " + this.x + ", " + this.y + ")";
        }
    }

    var p2 = Object.create(p1);
    p2.name = "p2";
    logger.log("p1 = " + p1);
    logger.log("p2 = " + p2);

    var pp2 = Object.getPrototypeOf(p2);
    logger.log("Prototype de p2 = " + pp2.name);

    var pp1 = Object.getPrototypeOf(p1); 
    logger.log("Prototype de p1 = " + pp1.name);

    var ppp1 = Object.getPrototypeOf(pp1); 
    logger.log("Prototype du prototype de p1 = " + ppp1.name);
}

function exp09() {
    var p1 = {};
    p1 = new Object();

    p1.x = 20;
    p1.y = 30;
    p1.print = function() {
        logger.log("Point : " + this.x + ", " + this.y);       
    }

    p1.print();

    var p2 = Object.create(p1);
    p2.x = 56;
    p2.y = 90;
    p2.print();
}

function exp10() {
    /* Définition d'un type => "classe" */
    function Point(x, y) {
        this.x = x;
        this.y = y;
    }

    Point.prototype.toString = function() {
        return "Point(" + this.x + ", " + this.y + ")";
    }
    /***********************************/
    var p1 = new Point(20, 30);
    var p2 = new Point(30, 40);

    logger.log("p1 = " + p1);
    logger.log("p2 = " + p2);
}

function exp11() {
    function Point(x, y) {
        if (x <= Point.MAX_X) {
            this.x = x;
        }
        this.y = y;
    }

    Point.prototype.toString = function() {
        return "Point(" + this.x + ", " + this.y + ")";
    }
    // Remarque :
    Point.MAX_X = 200;

    var p1 = new Point(20, 30);
    p1.x = 56;
    p1["y"] = 76;
    p1["max-value"] = 1000;
    var prop = "x";

    p1[prop] = 90;

    logger.log(p1);
    logger.log(p1['max-value']);

    for (var prop in p1) {
        logger.log(prop + " : " + p1[prop]);
    }

}

function exp12() {
    x = 20;
    y = 30;

    var p1 = {
        x,
        y
    }

    for (var prop in p1) {
        logger.log(prop + " : " + p1[prop]);
    }
}

function exp13() {
    function printArray(t) {
        for(var i = 0; i < t.length; i++) {
            logger.log(" - t[" + i + "] = " + t[i])
        }
    }

    function printArray2(t) {
        for(i in t) {
            logger.log(" - t[" + i + "] = " + t[i])
        }
    }

    var t1 = new Array();
    var t2 = [];
    var t3 = [20, 40, 50];

    t1[5] = 56;
    t1["0"] = 10;
    t1.x = 20;
    t1["y"] = 50;

    t1.push(87);

    printArray2(t1);
}

