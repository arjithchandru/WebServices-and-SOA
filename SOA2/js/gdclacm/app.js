const express = require('express')
const app = express();
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())


app.get('/mathlo2number', (req, res) => {

    var number = req.query.value
    var spnumber = number.split(",");
    var i;
    var respond = spnumber[0];
    console.log(spnumber);
    for (i = 0; i < spnumber.length; i++) {

      respond = gcd_function(respond,spnumber[i]);
    }

    function gcd_function(a, b){
        if (b === 0){
          console.log(a);
            return a;
          }
        else{
            a = a % b;
            return gcd_function(b, a);
          }
    }
    var gcd = respond;
    // console.log(gcd);
    //lcmresponse
    var ans = spnumber[0];
    var j = 1;

    for  (j = 0; j < spnumber.length; j++) {
        ans = (
                ((spnumber[j] * ans)) / (gcd_function(spnumber[j], ans))
        );
      }
    var lcm = ans;
    // console.log(lcm);
    res.render('index.html', { value: req.query.value, gcfresponse: gcd, lcmresponse:lcm });
        //return res.send(genOTP)
})



app.get('/', (req, res) => {

        res.render('index.html', { value: "12,12,24", gcfresponse: "",lcmresponse:"" });
    })
    //start
app.listen(3000)
