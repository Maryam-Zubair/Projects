import * as dotenv from 'dotenv';
import OpenAI from 'openai';
dotenv.config();

const api_key = process.env.OPENAI_API_KEY;
const openai = new OpenAI({ key: api_key });

export const generateImage = async (req, res) => {
    try {
        const response = await openai.images.generate({
            model: "dall-e-3",
            prompt: 'Show under water cave with fishes, turtle, and two scuba divers.',
            n: 1,
            size: '1024x1024',
        });
        const imageUrl = response.data[0].url;
        if (imageUrl) {
            res.status(200).json({
                success: true,
                data: imageUrl,
            });
        } else {
            res.status(500).json({
                success: false,
                error: 'The image couldn\'t be generated',
                details: 'Image URL not found in the response',
            });
        }
    } catch (error) {
        console.error(error);
        res.status(500).json({
            success: false,
            error: 'The image couldn\'t be generated',
            details: error.message,
        });
    }
};
