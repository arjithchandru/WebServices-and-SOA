const express = require('express')
const app = express();
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())

app.get('/datediff', (req, res) => {
  var datea = req.query.date1
  var s1 = req.query.time1
  var dateb = req.query.date2
  var s2 = req.query.time2

  var d1 = datea.split("-")
  var d2 = dateb.split("-")
  var year2;
  var year1;
  var day1;
  var day2;
  var mon1;
  var mon2;
  var ts;
  var tm;
  var ty;
  var time1 = s1.split(":")
  var  time2 = s2.split(":")
  if (d1[0] >= d2[0] || d1[1] >= d2[1] || d1[2] >= d2[2]){
    //console.log(d1[0]);
    day1 = d1[2];
    mon1 = d1[1];
    year1 = d1[0];
    day2 = d2[2];
    mon2 = d2[1];
    year2 = d2[0];
  }else{
    // console.log("else");
    // console.log(d1[0]);
    day1 = d2[2];
    mon1 = d2[1];
    year1 = d2[0];
    day2 = d1[2];
    mon2 = d1[1];
    year2 = d1[0];
  }

  // for i in range(0, len(time1)):
  //     time1[i] = int(time1[i])
  //     # print (time1[i]);
  //
  // for i in range(0, len(time2)):
  //     time2[i] = int(time2[i])

  if (time2[2] >= time1[2]){
      ts = time2[2] - time1[2]
    }
  else{
      ts = (time2[2] + 60) - time1[2]
      time2[1] -= 1
    }

  if (time2[1] >= time1[1]){
      tm = time2[1] - time1[1]
    }
  else{
      tm = (time2[1] + 60) - time1[1]
      time2[0] -= 1
    }

  if (time2[0] >= time1[0]){
      ty = time2[0] - time1[0]
    }
  else{
      ty = (time2[0] + 24) - time1[0]
      day2 -= 1
    }

    if (day2 < day1){
        if (mon2 == 3){
            if ((year2 % 4 == 0 && year2 % 100 != 0) || (year2 % 400 == 0)){
                day2 += 29;
              }
            else{
                day2 += 28;
              }
            }
        else{
            if (mon2 == 5 || mon2 == 7 || mon2 == 10 || mon2 == 12){
                day2 += 30;
              }
            else{
                day2 += 31;
                mon2 = mon2 - 1;
              }
          }
        }
    if (mon2 < mon1){
        mon2+= 12;
        year2-= 1;
      }

    day_diff = day2 - day1;
    mon_diff = mon2 - mon1;
    year_diff = year2 - year1;

    if (year_diff < 0){
        year_diff = year_diff * -1;
      }

    // res = ("Years:" + str(year_diff) + "  Months:" + str(mon_diff) + "  Days:" + str(day_diff))
    // return(res)
    res.render('index.html', {date1: datea, date2:dateb, year:year_diff, month:mon_diff, days:day_diff, hour:ty, minute:tm, second:ts, time1:s1, time2:s2});

    // res.send(resultDiff);
})

app.get('/', (req, res) => {

        res.render('index.html', {date1: "",date2:"", year:"", month:"", days:"", time1:"", time2:"", hour:"", minute:"", second:""});
    })

//start
app.listen(3000)
