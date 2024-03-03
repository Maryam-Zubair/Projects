// const express = require('express')
// const dotenv = require('dotenv').config()
// const port = process.env.PORT || 5000;


import express from 'express'
import {openai_routes} from './routes/openaiRoutes.js'

// const port = process.env.PORT || 8000;
const PORT = 8000

const app = express()

app.use('/openai', openai_routes)

app.listen(PORT, ()=>
console.log(`Server started on port ${PORT}`)
)