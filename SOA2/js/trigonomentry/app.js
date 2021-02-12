const express = require('express')
const app = express();
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())

app.get('/trignomentry', (req, res) => {
  //start

var number = req.query.value

var sin = my_sin(number)
var cos = my_cos(number)
var tan = my_tan(number)
var sec = my_sec(number)
var cosec = my_cosec(number)
var cot = my_cot(number)

function factorial_function(x){
      var y = x
      // console.log(x,y)
      var i = 1 ;
      // console.log("factorial_function")
      if (x == 0){
          return 1
        }
      else{
          for (i = 1 ; i < x ; i++){
              y = parseFloat(i) * parseFloat(y)
              // console.log(y)
            }
      return y
      // console.log(y)
    }
}
function pi(){
      var pi = parseFloat(3.1415)
      return pi
    }


function  my_sin(theta){

    theta = theta * (pi() / 180)
    //theta = math.fmod(theta + math.pi, 2 * math.pi) - math.pi
    var d_theta = ( parseFloat(theta) + pi()) % ( 2 * pi())
    // console.log(d_theta)
    theta = parseFloat(d_theta) - pi()
    // console.log(theta)
    var result = 0
    var termsign = 1
    var power = 1
    var i;
    var result = 0
    for (i = 0; i < 10; i++){
        //result = result + ( ((Math.pow(theta, power) / (factorial_function(power)) )) * termsign)
        var dummypower = factorial_function(power);
        // console.log(dummypower)
        var dummy = Math.pow(theta, power) / dummypower;
        // console.log(dummy)
        result = result + parseFloat(dummy * termsign)

        // console.log(result)
        // console.log(power)
        //result += ((theta**power) / factorial_function(power)) * termsign
        termsign = parseFloat(termsign) * (-1)
        // console.log(termsign)
        power =parseFloat(power) + 2
      }
    return result
}

function my_cos(theta){
    theta = theta * (pi() / 180)
    var d_theta = (parseFloat(theta) + pi()) % (2 * pi())
    theta = d_theta - pi()
    var result = 0
    var termsign = 1
    var power = 0

    for (i = 0; i < 10; i++){
      var dummypower = factorial_function(power);
      // console.log(dummypower)
      var dummy = Math.pow(theta, power) / dummypower;
      // console.log(dummy)
      result = result + parseFloat(dummy * termsign)

      // console.log(result)
      // console.log(power)
      //result += ((theta**power) / factorial_function(power)) * termsign
      termsign = parseFloat(termsign) * (-1)
      // console.log(termsign)
      power =parseFloat(power) + 2
      // console.log(power);
    }

        // result += ((theta**power) / factorial_function(power)) * termsign
        // termsign *= -1
        // power += 2
    return result
}

function my_tan(theta){
    return my_sin(theta) / my_cos(theta)
}

function my_sec(theta){
    return  1 / my_cos(theta)
}

function my_cosec(theta){
    return  1 / my_sin(theta)
}

function my_cot(theta){
    return  1 / my_tan(theta)
}

res.render('index.html', { value: req.query.value, sinresponse: sin, cosresponse:cos, tanresponse:tan, secresponse:sec, cosecresponse:cosec, cotresponse:cot});
  //end
})



app.get('/', (req, res) => {

      res.render('index.html', { value: "60", sinresponse: "", cosresponse: "", tanresponse:"", secresponse:"", cosecresponse:"", cotresponse:""});
  })
  //start
app.listen(3000)
