/*
    number
    boolean
    string

    function
    array
    Object

*/
function exp01() {
    var x1 = 20;
    var x2 = new Number(20);
    var x3 = new Number(20);

    logger.log("Type de x1 : " + typeof x1);
    logger.log("Type de x2 : " + typeof x2);

    logger.log("x1 == x2 : " + (x1 == x2));
    logger.log("x2 == x3 : " + (x2 == x3));
    logger.log("x1 === x2 : " + (x1 === x2));
}

function exp02() {
    var x1 = true;
    var x2 = new Boolean(true);
    var x3 = new Boolean(true);
    var x4 = 20 > 10;

    logger.log("Type de x1 : " + typeof x1);
    logger.log("Type de x2 : " + typeof x2);
    logger.log("Type de x4 : " + typeof x4);

    logger.log("x1 == x2 : " + (x1 == x2));
    logger.log("x2 == x3 : " + (x2 == x3));
    logger.log("x1 === x2 : " + (x1 === x2));
}

function exp03(p) {
    var x1 = "JavaScript";
    var x2 = new String("JavaScript");
    var x3 = new String("JavaScript");

    var x4;
    logger.log("x4 = " + x4);
    logger.log("p = " + p);

    logger.log("Type de x1 : " + typeof x1);
    logger.log("Type de x2 : " + typeof x2);

    logger.log("x1 == x2 : " + (x1 == x2));
    logger.log("x2 == x3 : " + (x2 == x3));
    logger.log("x1 === x2 : " + (x1 === x2));
}

function exp04() {
    var f1 = function(x, y) {
        return x + y;
    }

    function sum(x, y) {
        return x + y;
    }

    logger.log("Type de f1 : " + typeof f1);
    logger.log("Type de sum : " + typeof sum);

    logger.log(f1.name +", " + f1.length)
}

function exp05() {
    function sum(x, y, z) {
        var s = 0;
        if (x != undefined) s = x;
        if (y != undefined) s = s + y;
        if (z != undefined) s = s + z;
        return s;
    }

    var s1 = sum();
    var s2 = sum(20, 30);
    var s3 = sum(20, 30, 40);

    logger.log("s1 = " + s1);
    logger.log("s2 = " + s2);
    logger.log("s3 = " + s3);
}

function exp06() {
    function sum() {
        logger.log("# Nombre d'arguments d'appel : " + arguments.length);
        var s = 0;
        for (var i = 0; i < arguments.length; i++) {
            s = s + arguments[i];
        }
        return s;
    }

    var s1 = sum();
    var s2 = sum(20, 30);
    var s3 = sum(20, 30, 40, 56, 78, 98);

    logger.log("s1 = " + s1);
    logger.log("s2 = " + s2);
    logger.log("s3 = " + s3);
}

