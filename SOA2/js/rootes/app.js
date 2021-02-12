const express = require('express')
const app = express();
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())


app.get('/mathlo2sqnumber', (req, res) => {
//start
var number = req.query.value
var times = req.query.times
var cube = "3"
var sqrot = find_sqroot(number)
var cqrot = find_nsqroot(number, cube)
var nthrot = find_nsqroot(number, times)

function Square(n, i, j){
    var mid = (i + j) / 2;
    var mul = mid * mid;
    if ((mul == n) || (Math.abs(mul - n) < 0.00001)){
        return mid;
      }
    else if (mul < n){
        return Square(n, mid, j);
      }
    else{
        return Square(n, i, mid);
      }
}

function find_sqroot(n){
    var n = n ;
    var i = 1;

    var found = "False";
    while (found == "False"){

        if (i * i == n){
            return i;
            found = "True";
          }

        else if ((i * i) > n){
            var respond = Square(n, i - 1, i);
            result = (respond.toFixed(5));
            return result;
            found = "True";
          }
        i += 1;
      }
}

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function find_nsqroot(A, N){
    // var A = fA)
    // N = float(N)
    var xPre = getRandomInt(101) % 10;
    var eps = 0.001;
    var delX = 2147483647;
    var xK = 0.0;
    while (delX > eps){
        var Si = ((N - 1.0) * xPre + A / Math.pow(xPre, N - 1));
        xK = Si / N;
        delX = Math.abs(xK - xPre);
        xPre = xK;
    }
    return xK;
}

res.render('index.html', { value: req.query.value, times:req.query.times, sqresponse:sqrot, curesponse:cqrot, nqresponse:nthrot});
//end
})

app.get('/', (req, res) => {

        res.render('index.html', {value: "25", times:"2", sqresponse:"", curesponse:"", nqresponse:""});
    })
    //start
app.listen(3000)
