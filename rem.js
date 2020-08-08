const Twit = require ('twit');
const fs = require ('fs');
const path = require ('path');
const config = require (path.join(__dirname, 'config.js'));
const images = require('./images.js')
const T = new Twit (config);

//images.danbooru(function(){})

function upload_images(images){
    const image_path = path.join(__dirname, '/images/' + images.name);
    b64content = fs.readFileSync(image_path, {encoding: 'base64'});
    T.post('media/upload', {media_data: b64content}, function (err, data, response){
        if (err){
            console.log ('A ERROR HAS OCCURRED WHILE LOADING IMAGE');
            console.log (err);
        }
        else{
            console.log ('IMAGE LOADED');
            console.log ('TWEETING');
            var tweet_text = ''
            T.post ('statuses/update', {status: tweet_text,media_ids: new Array(data.media_id_string)}),
            function (err,data,response){
                if (err){
                    console.log ('A ERROR HAS OCCURRED WHILE SENDING IMAGE');
                }
                else{
                    console.log (data);
                }
            }
        }
    })
}
setInterval (function(){
    images.danbooru(function(err, end){
        if (err){
            console.log (err)
        }
        else {
            upload_images(images)
        }
    })
},55000);

