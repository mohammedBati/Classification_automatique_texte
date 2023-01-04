var x = 20;

function exp01() {
    logger.log("x = " + x);
    // Le x se trouvera dans le scope global : L'objet window
    logger.log("window.x = " + window.x);

    window.alert("Ok")
}