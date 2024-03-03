import express from 'express'
import {generateImage} from '../controller/openaiController.js'
export const openai_routes = express.Router()

openai_routes.post('/generateimage', generateImage)