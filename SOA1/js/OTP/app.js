const express = require('express')
const app = express();
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())

app.get('/otp', (req, res) => {
  // console.log("inside");
    var numbers = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@~/$"
    var length = Math.floor(Math.random() * 10) + 4
    var num="";
    var i;
              for (i = 0; i < length; i++) {
                    num += numbers[Math.floor(Math.random() * numbers.length)]
                }
                // console.log(num)
                res.render('index.html', {otps:num});
})

app.get('/', (req, res) => {

        res.render('index.html', {otps:""});
    })

//start
app.listen(3000)
