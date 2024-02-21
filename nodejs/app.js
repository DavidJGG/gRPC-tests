const express = require('express')
const app = express()
const port = 9002

app.get('/emisor', (req, res) => {
  res.send('emisor js')
})

app.get('/receptor', (req, res) => {
    res.send("receptor js")
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})