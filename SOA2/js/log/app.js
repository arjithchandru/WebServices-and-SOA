const express = require('express')
const app = express()
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())

function nLog(x) {
    var n = 99999999
    return n * ((x ** (1 / n)) - 1)
}

function log(x, base) {

    var result = nLog(x) / nLog(base)
    return result

}

function antiLog(a, b) {

    var c = 1;
    for (var i = 1; i <= b; i++) {
        c = c * a;
    }
    return c;
}


app.get('/log', (req, res) => {


    op = req.query.opChoice
    if (op == 0) {
        var data = req.query.num3
        var base = req.query.base

        var vOpName = "Log";
        var ba = " base " + base;
        var vresult = log(data, base)

    } else if (op == 1) {
        var data = parseInt(req.query.num)

        var vresult = nLog(data)
        var vOpName = "Natural Log";

    } else if (op == 2) {
        var data = parseInt(req.query.data)
        var pow = parseInt(req.query.pow)
        var po ="power " + pow;
        var vresult = antiLog(data, pow)

        var vOpName = "AntiLog";
    } else {
        res.status(500).send('Invalid Data !')
    }

    if (vOpName == "AntiLog"){
    res.render('index.html', { data: data, pow: po, base: ba, num: data, num3: data, opName: vOpName, result: vresult });
  }else if (vOpName == "Log") {
    res.render('index.html', { data: data, pow: po, base: ba, num: data, num3: data, opName: vOpName, result: vresult });
  }else{
    res.render('index.html', { data: data, pow: po, base: ba, num: data, num3: data, opName: vOpName, result: vresult });
  }

})


app.get('/', (req, res) => {
    res.render('index.html', { data: "", pow: "", base: "", num: "", num3: "", opName: "", result: "" });
})
// console.log("running on port 3000");
app.listen(3000)
