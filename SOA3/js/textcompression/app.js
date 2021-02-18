const express = require('express')
const app = express();
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())



  class node {
      constructor(freq, char,left,right) {
        this.freq = freq;
        this.char = char;
        this.left = left;
        this.right = right;
        this.huff='';
      }
    }
  let global_node_res=[]
  app.get('/hufman', function(req, res) {
      // let message=req.body["huffman_message"]
      var message = req.query.value
      var freq = {};
      for (var i=0; i<message.length;i++) {
          var character = message.charAt(i);
          if (freq[character]) {
             freq[character]++;
          } else {
             freq[character] = 1;
          }
      }
      let h_char=[]
      let h_freq=[]
      for (const val in freq) {
          h_char.push(val)
          h_freq.push(freq[val])
      }
      let nodes=[]
      for (var i=0; i<h_char.length;i++) {
              nodes.push(new node(h_freq[i], h_char[i],null,null))
      }
      console.log(nodes)
      while(nodes.length>1){
          nodes.sort(function (a, b) {
              return a.freq - b.freq;
            });
          let left=new node
          left=nodes[0]
          let right=new node
          right=nodes[1]
          left.huff=0
          right.huff=1
          let newNode =new node(left.freq+right.freq, left.char+right.char, left, right)
          nodes.splice(0,2);
          nodes.push(newNode)
      }
      traverse(nodes[0],"")
      let result=[global_node_res]
      global_node_res=[]
    
      res.render('huffman.html', { message: message, result:result});

  });
  function traverse(node,val){
      let newVal = val + String(node.huff)
      if(node.left)
          traverse(node.left, newVal)
      if(node.right)
          traverse(node.right, newVal)
      if(node.left==null && node.right==null)
          global_node_res.push(node.char+" : "+newVal+ " ")
  }

app.get('/runlen', function(req, res) {
  var msg = req.query.value
  console.log(msg);
  let result = [run_length_algorithm_encode(msg)]
  console.log(result);
  res.render('runlength.html', { message: msg, result:result});

  });

  function run_length_algorithm_encode(msg){
      let encoded_msg = ""
      let i = 0
      while (i  <=  ( msg.length ) - 1){
          count = 1
          ch = msg[i]
          j = i
          while (j < (msg.length)-1){
              if (msg[j] == msg[j+1]){
                  count = count+1
                  j = j+1
              }
              else{
                  break
              }
          }
          encoded_msg=encoded_msg+ch+String(count)
          i = j+1
      }
      return encoded_msg
  }

  class LZW
  {
      static compress(uncompressed)
      {
          let dictionary = {};
          for (let i = 0; i < 256; i++)
          {
              dictionary[String.fromCharCode(i)] = i;
          }
          let word = '';
          let result = [];
          let dictSize = 256;

          for (let i = 0, len = uncompressed.length; i < len; i++)
          {
              let curChar = uncompressed[i];
              let joinedWord = word + curChar;
             if (dictionary.hasOwnProperty(joinedWord))
              {
                  word = joinedWord;
              }
              else
              {
                  result.push(dictionary[word]);
                  dictionary[joinedWord] = dictSize++;
                  word = curChar;
              }
          }
          if (word !== '')
          {
              result.push(dictionary[word]);
          }

          return result;
      }
      static decompress(compressed)
      {
          let dictionary = {};
          for (let i = 0; i < 256; i++)
          {
              dictionary[i] = String.fromCharCode(i);
          }
          let word = String.fromCharCode(compressed[0]);
          let result = word;
          let entry = '';
          let dictSize = 256;
          for (let i = 1, len = compressed.length; i < len; i++)
          {
              let curNumber = compressed[i];

              if (dictionary[curNumber] !== undefined)
              {
                  entry = dictionary[curNumber];
              }
              else
              {
                  if (curNumber === dictSize)
                  {
                      entry = word + word[0];
                  }
                  else
                  {
                      throw 'Error in processing';
                      return null;
                  }
              }

              result += entry;
              dictionary[dictSize++] = word + entry[0];
              word = entry;
          }
          return result;
      }
  }
app.get('/lzw', function(req, res) {
      var msg = req.query.value
      console.log(msg);
      let comp = LZW.compress(msg);
      let decomp = LZW.decompress(comp);
      console.log(comp);
      res.render('LZW.html', { message: msg, compressed:comp, decompressed:decomp });

  });




app.get('/', (req, res) => {

        res.render('index.html');
    })
app.get('/rnlc', function(req, res) {
  // console.log("inside");
  res.render('runlength.html', { message: "", result:"" });

})
app.get('/huf', function(req, res) {
  // console.log("inside");

  res.render('huffman.html', { message: "", result:""});
})
app.get('/lzwhtml', function(req, res) {
  // console.log("inside");
  res.render('LZW.html', { message: "",compressed:"", decompressed:""});
})
    //start
app.listen(3000)
