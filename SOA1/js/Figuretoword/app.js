const express = require('express')
const app = express();
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())

app.get('/ftw', (req, res) => {
  var n = req.query.number

  var number = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
   var nty = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"]
   var tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen","Nineteen"]

           if (n > 999999999){
               return ("Cant solve for more than 8 digits");
             }
           else{
               var d = [0, 0, 0, 0, 0, 0, 0, 0, 0];
              var  i = 0;
               while (n > 0){
                   d[i] = n % 10;
                   i += 1;
                   n = parseInt(n / 10);
                 }
               var num = "";
               if (d[8] != 0){
                   if (d[8] == 1){
                       num += tens[d[7]] + " Crore ";
                     }
                   else{
                       num += nty[d[8]] + " " + number[d[7]] + " Crore ";
                     }
                    }
               else{
                   if (d[7] != 0){
                       num += number[d[7]] + " Crore ";
                     }
                   }
               if (d[6] != 0){
                   if (d[6] == 1){
                       num += tens[d[5]] + " Lakhs ";
                     }
                   else{
                       num += nty[d[6]] + " " + number[d[5]] + " Lakhs ";
                     }
                   }
               else{
                   if (d[5] != 0){
                       num += number[d[5]] + " Lakhs ";
                     }
                   }
               if (d[4] != 0){
                   if (d[4] == 1){
                       num += tens[d[3]] + " Thousand ";
                     }
                   else{
                       num += nty[d[4]] + " " + number[d[3]] + " Thousand ";
                     }
                   }
               else{
                   if (d[3] != 0){
                       num += number[d[3]] + " Thousand ";
                     }
               if (d[2] != 0){
                   num += number[d[2]] + " Hundred ";
                 }
               }
               if (d[1] != 0){
                   if (d[1] == 1){
                       num += tens[d[0]];
                     }
                   else{
                       num += nty[d[1]] + " " + number[d[0]];
                     }
                   }
               else{
                   if (d[0] != 0){
                       num += number[d[0]];
                     }
                   }
                 }
           var resp = num
           // var res = paisa * 0

          res.render('index.html', {number:req.query.number, word:resp});


})

app.get('/', (req, res) => {

        res.render('index.html', {number:"0369", word:""});
    })

//start
app.listen(3000)
