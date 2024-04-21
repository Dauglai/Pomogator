const {google} = require('googleapis');
const path = require('path')
const fs = require('fs')

const  CLIENT_ID = '503308712884-ho189eou2iq4opobamis0fgfpk7qktim.apps.googleusercontent.com';
const  CLIENT_SECRET = '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';
const REDIRECT_URI = 'https://developers.google.com/oauthplayground';

const REFRESH_TOKEN = '1//04LEgYrk2RgDgCgYIARAAGAQSNwF-L9IrtEBI5PGMDtzHCI-QnmIFJtAwsntU-YoHPyD5H0lqY_cXnjNCtTdo8g3vpCRPS13JtGo';

const oauth2Client = new google.auth.OAuth2(
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI
);

oauth2Client.setCredentials({refresh_token: REFRESH_TOKEN})

const drive = google.drive({
    version: 'v3',
    auth: oauth2Client
})

const filePath = path.join(__dirname, 'python.jpg')

async function uploadFile(){
    try {
        const response = await drive.files.create({
            requestBody: {
                name: 'python.jpg',
                mimeType: 'image/jpg'
            },
            media:{
                mimeType:'image/jpg',
                body: fs.createReadStream(filePath)
            }
        });
        console.log(response.data);

    }
    catch (error){
        console.log(error.message)
    }
}


async function deleteFile(){
        try {
        const response = await drive.files.delete({
            fileId: '1r7wikGfNnU8pQJc5zvoODzY8xfY_v3__',
        });
        console.log(response.data, response.status);
    }
    catch (error){
        console.log(error.message)
    }
}

async function generatePublicUri(){
        try {
            const fileId = '1r7wikGfNnU8pQJc5zvoODzY8xfY_v3__';
            await drive.permissions.create({
               fileId: fileId,
                requestBody: {
                   role: 'reader',
                    type: 'anyone'
                }
            });
            const result = await drive.files.get({
                fileId: fileId,
                fields: 'webViewLink, webContentLink',
            });
        console.log(result.data);
        } catch (error){
        console.log(error.message)
    }
}

//uploadFile();
//deleteFile();
generatePublicUri();

