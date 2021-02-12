const express = require('express')
const app = express();
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())

app.get('/Ecalc', (req, res) => {
  //start

function cal_watts(i, v){
      if (i != "None" && v != "None" || i != "" && v != "" ){
          // I = I
          // V = V
          var p = i * v
          return p
        }
      }

function cal_volts(i, p){
    if (i != "None" && p != "None" || i != "" && p != ""){
        // I = I
        // P = P
        var v = p / i
        return v
      }
    }

function cal_amperes(v, p){
  if(p != "None" && v != "None" || p != "" && v != ""){
    // V = V
    // P = P
  var i = p / v
    return i
  }
}
  //end
})


app.get('/', (req, res) => {

        res.render('index.html', { value: "12,12,24", gcfresponse: "",lcmresponse:"" });
    })
    //start
app.listen(3000)
