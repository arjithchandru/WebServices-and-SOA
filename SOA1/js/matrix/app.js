const express = require('express')
const app = express()
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())

function transpose(array) {
    return array.reduce((prev, next) => next.map((item, i) =>
        (prev[i] || []).concat(next[i])
    ), []);
}

function upperDiagonal(matrix, row, col) {
    var RM = [],
        LM = [],
        rMatRow = [],
        lMatRow = [],
        i, j;

    for (i = 0; i < row; i++) {
        for (j = 0; j < col; j++) {
            if (j > i)
                rMatRow.push(matrix[i][j])
            else
                rMatRow.push( )
            if (j <= 1 && i + j < col - 1)
                lMatRow.push(matrix[i][j])
            else
                lMatRow.push( )
        }
        RM.push(rMatRow)
        LM.push(lMatRow)
        rMatRow = []
        lMatRow = []
    }
    return { 'Upper Left': [...LM], 'Upper Right': [...RM] }
}

function lowerDiagonal(matrix, row, col) {
    var RM = [],
        LM = [],
        rMatRow = [],
        lMatRow = [],
        i, j;

    for (i = 0; i < row; i++) {
        for (j = 0; j < col; j++) {
            if (j < i)
                lMatRow.push(matrix[i][j])
            else
                lMatRow.push( )
            if (j >= 1 && i + j > col - 1)
                rMatRow.push(matrix[i][j])
            else
                rMatRow.push( )
        }
        RM.push(rMatRow)
        LM.push(lMatRow)
        rMatRow = []
        lMatRow = []
    }
    return  { 'Lower Left': [...LM], 'Lower Right': [...RM] }
}

app.get('/matops', (req, res) => {

    

    var operation = parseInt(req.query.op)
    var row = parseInt(req.query.row)
    var col = parseInt(req.query.col)
    var matrix = req.query.matrix.split(',')
    // console.log('matrix', matrix);
    TM = []
    matrixA = []
    colBkp = col

    matrix.forEach(function(value, i) {
        if (i < col) {
            TM.push(value)
        } else {
            matrixA.push(TM)
            TM = []
            col += colBkp
            TM.push(value)
        }
    });
    matrixA.push(TM)
    col = colBkp
    // console.log('matrixA', matrixA);

    if (operation == 0)

        res.render('index.html', { op: req.query.op, row: 3, col: 5, opName: "Transpose", matrix: req.query.matrix, response: [...transpose(matrixA)] })
    else if (operation == 1)

        res.render('index.html', { op: req.query.op, row: 3, col: 5, opName: "Upper Diagonal", matrix: req.query.matrix, response: JSON.stringify(upperDiagonal(matrixA, row, col)) })
    else

        res.render('index.html', { op: req.query.op, row: 3, col: 5, opName: "Lower Diagonal ", matrix: req.query.matrix, response: JSON.stringify(lowerDiagonal(matrixA, row, col)) })


})


app.get('/', (req, res) => {

    res.render('index.html', { op: 0, opName: "", row: 3, col: 5, matrix: "1,2,3,4,5,6,7,8,9,0,11,12,13,14,15", response: "" });
})

app.listen(3000)
