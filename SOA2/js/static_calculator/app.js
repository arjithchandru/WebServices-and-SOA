const express = require('express')
const app = express();
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())


app.get('/Basicstaticcalculator', (req, res) => {
//start
    var number = req.query.value
    var spnumber = number.split(",");
    console.log(spnumber);
    var sd = standard_calculus(spnumber);
    var variance = variance(spnumber);

function standard_calculus(observation){

    var oblength = observation.length;
    var tsum = 0
    var i;
    for (i = 0; i < observation.length; i++){
        tsum = parseFloat(observation[i]) + parseFloat(tsum);
        // console.log(observation[i]);
      }
    // console.log(observation)
    // var tsum = observation.reduce((a, b) => a + b, 0)
// console.log(tsum);
    var mean_of_observations = tsum / oblength ;
    // console.log(mean_of_observations);
    var sum_of_squared_deviation = 0;

    for (i = 0; i < observation.length; i++){
        //sum_of_squared_deviation = parseFloat(sum_of_squared_deviation) + Math.pow((parseFloat(observation[i]) - parseFloat((mean_of_observations)), 2))
        var dober = parseFloat(observation[i]) - parseFloat(mean_of_observations)
        var powerval = Math.pow(dober,2)
        sum_of_squared_deviation = parseFloat(sum_of_squared_deviation) + parseFloat(powerval)
        // console.log(sum_of_squared_deviation);
      }
    var std = Math.pow(((sum_of_squared_deviation) / oblength), 0.5);

    return std
  //   const n = array.length
  // const mean = array.reduce((a, b) => a + b) / n
  // var result =  Math.sqrt(array.map(x => Math.pow(x - mean, 2)).reduce((a, b) => a + b) / n)
  // return result
  }

function variance(arr){

  function getVariance(arr, mean) {
     return arr.reduce(function(pre, cur) {
         pre = parseFloat(pre) + Math.pow((parseFloat(cur) - parseFloat(mean)), 2);
         return pre;
     }, 0)
 }

 var meanTot = arr.reduce(function(pre, cur) {
     return parseFloat(pre) + parseFloat(cur);
 })
 var total = getVariance(arr, meanTot / arr.length);

 var respond = {
     mean: meanTot / arr.length,
     variance: total / arr.length
 }

    return respond.variance
  }

res.render('index.html', { value: req.query.value, stdresponse:sd, vresponse:variance});
//end
})

app.get('/', (req, res) => {

        res.render('index.html', {value: "25,12,15,16,21", stdresponse:"", vresponse:""});
    })
    //start
app.listen(3000)
