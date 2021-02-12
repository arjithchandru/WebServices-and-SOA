const express = require('express')
const app = express()
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())

Set.prototype.union = function(otherSet) {
    var unionSet = new Set();
    for (var elem of this) {
        unionSet.add(elem);
    }
    for (var elem of otherSet)
        unionSet.add(elem);

    return unionSet;
}

Set.prototype.intersection = function(otherSet) {
    var intersectionSet = new Set();
    for (var elem of otherSet) {
        if (this.has(elem))
            intersectionSet.add(elem);
    }
    return intersectionSet;
}
Set.prototype.minus = function(otherSet) {
    var differenceSet = new Set();
    for (var elem of this) {
        if (!otherSet.has(elem))
            differenceSet.add(elem);
    }
    return differenceSet;
}
app.get('/setops', (req, res) => {

    var operation = req.query.opChoice
    var setA = new Set(req.query.setA)
    var setB = new Set(req.query.setB)
    var result

    console.log(req.query)
    if (operation == 0) {
      result = [...setA.union(setB)].join(',')
        res.render('index.html', { operation: req.query.operation, operationName: "Union", setA: req.query.setA, setB: req.query.setB, response: result })
    } else if (operation == 1) {
      result = [...setA.intersection(setB)].join(',')
        res.render('index.html', { operation: req.query.operation, operationName: "Intersection", setA: req.query.setA, setB: req.query.setB, response: result })
    } else {
        result = [...setA.minus(setB)].join(',')
        res.render('index.html', {operation: req.query.operation,operationName: "Minus",setA: req.query.setA,setB: req.query.setB,response: result})
      }

})



app.get('/', (req, res) => {

        res.render('index.html', { operation: 0, operationName: "", setA: "", setB: "", response: "" });
    })
    //start
app.listen(3000)
