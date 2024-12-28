var choice = prompt(" welcome to area calculator \n enter you choice \n1 area of rectancle \n2 area of triangle \n3 area of circle \n4 area of paralleogram")
if (choice == "1") {
    var l = prompt("enter the length");
    var b = prompt("enter the breadth");
    var result = Number(l) * Number(b)
    alert("the area is " + result)

}
if (choice == "2") {
    var h = prompt("enter the height");
    var ba = prompt("enter the base");
    var result = Number(h) * Number(ba) / 2
    alert("the area is " + result)

}
if (choice == "3") {
    var r = prompt("enter the radius");
    var result = 3.14 * Number(r) * Number(r)
    alert("the are is " + result)

}
if (choice == "4") {
    var h = prompt("enter the height");
    var cb = prompt("enter the corresponding base");
    var result = Number(h) * Number(cb)
    alert("the are is " + result)

}